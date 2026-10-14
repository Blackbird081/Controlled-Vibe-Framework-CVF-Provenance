#!/usr/bin/env python3
"""Disposable HTTP proof of Web export -> engine -> SQLite; no user config."""

from __future__ import annotations

import hashlib
import argparse
import hmac
import json
import os
import secrets
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = Path("EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web")
ENGINE = Path("EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core")
RUNTIME = ROOT / ".cvf/runtime"
RECEIPT_TIMEOUT_MS = 1200
ENGINE_TIMEOUT_MS = 8000


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def stage_tracked_source(target: Path) -> int:
    """Copy Git-visible current files, excluding env and the active JSON ledger."""
    proc = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", WEB.as_posix(), ENGINE.parent.as_posix()],
        cwd=ROOT, check=True, capture_output=True,
    )
    count = 0
    seen = set()
    for raw in proc.stdout.split(b"\0"):
        if not raw:
            continue
        relative = Path(os.fsdecode(raw))
        if relative in seen:
            continue
        seen.add(relative)
        if any(part.startswith(".env") for part in relative.parts) or relative.name == "ledger_chain.json":
            continue
        source = ROOT / relative
        if not source.exists():
            continue  # Tracked deletion in the current worktree.
        if source.is_symlink() or not source.resolve().is_relative_to(ROOT.resolve()):
            raise RuntimeError("source staging encountered an unsafe path")
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        count += 1
    if not count or (target / WEB / ".env.local").exists() or (target / ENGINE / "ledger_layer/ledger_chain.json").exists():
        raise RuntimeError("tracked-source staging isolation failed")
    return count


def request_json(url: str, body: dict | None = None, *, token: str | None = None,
                 signed: bool = False, timeout: float = 12) -> tuple[int, dict]:
    raw = json.dumps(body, separators=(",", ":"), ensure_ascii=False).encode() if body is not None else None
    headers = {"Content-Type": "application/json"}
    if token is not None:
        headers["x-cvf-service-token"] = token
        if signed:
            timestamp = str(int(time.time() * 1000))
            headers["x-cvf-service-timestamp"] = timestamp
            headers["x-cvf-service-signature"] = hmac.new(
                token.encode(), timestamp.encode() + b"." + raw, hashlib.sha256,
            ).hexdigest()
    request = urllib.request.Request(url, data=raw, headers=headers,
                                     method="POST" if raw is not None else "GET")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read())


def wait_ready(url: str, process: subprocess.Popen, deadline: float = 100) -> None:
    until = time.monotonic() + deadline
    while time.monotonic() < until:
        if process.poll() is not None:
            raise RuntimeError(f"server exited before readiness: {process.returncode}")
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                if response.status < 500:
                    return
        except (OSError, urllib.error.HTTPError):
            pass
        time.sleep(0.4)
    raise TimeoutError(f"server readiness timeout: {url}")


def stop(process: subprocess.Popen | None) -> None:
    if process is None:
        return
    docker_name = getattr(process, "cvf_docker_name", None)
    if docker_name:
        if not docker_name.startswith("cvf-q001-web-"):
            raise RuntimeError("Refusing cleanup outside the owned Docker namespace")
        state = subprocess.run(["docker", "container", "inspect", docker_name], capture_output=True, timeout=30)
        if state.returncode == 0:
            subprocess.run(["docker", "rm", "-f", docker_name], check=True, capture_output=True, timeout=30)
        elif b"no such" not in state.stderr.lower():
            raise RuntimeError("Cannot verify owned Docker container cleanup state")
        if process.poll() is None:
            process.wait(timeout=15)
        return
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


class EngineProxy(ThreadingHTTPServer):
    def __init__(self, port: int, engine_port: int):
        super().__init__(("127.0.0.1", port), ProxyHandler)
        self.engine_port = engine_port
        self.mode = "forward"
        self.forwarded = 0
        self.attempted = 0
        self.forward_failures = 0
        self.engine_observations: dict[str, dict] = {}
        self.committed_before_delay = threading.Event()
        self.daemon_threads = True


class ProxyHandler(BaseHTTPRequestHandler):
    def log_message(self, *_args) -> None:
        pass

    def do_POST(self) -> None:
        server: EngineProxy = self.server  # type: ignore[assignment]
        if self.path != "/api/v1/evaluate":
            self.send_error(404)
            return
        raw = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        mode = server.mode
        if mode == "unavailable":
            status, payload = 503, b'{}'
        elif mode == "malformed":
            status, payload = 200, b'{"status":"ok","data":{"not_a_report":true}}'
        else:
            request = urllib.request.Request(
                f"http://127.0.0.1:{server.engine_port}/api/v1/evaluate",
                data=raw, headers={"Content-Type": "application/json"}, method="POST",
            )
            server.attempted += 1
            try:
                with urllib.request.urlopen(request, timeout=6) as response:
                    status, payload = response.status, response.read()
            except urllib.error.HTTPError as error:
                status, payload = error.code, error.read()
            except OSError:
                server.forward_failures += 1  # engine unreachable: drop the connection, do not simulate a status
                self.close_connection = True
                return
            server.forwarded += 1
            if status == 200:
                submitted = json.loads(raw)
                engine_data = json.loads(payload).get("data", {})
                report = engine_data.get("report", {})
                server.engine_observations[submitted["request_id"]] = {
                    "requestId": report.get("request_summary", {}).get("request_id"),
                    "artifactId": report.get("request_summary", {}).get("artifact_id"),
                    "decision": report.get("decision_analysis", {}).get("final_decision"),
                    "action": report.get("cvf_enforcement", {}).get("action"),
                    "ledgerAttached": engine_data.get("execution_record", {}).get("ledger_attached"),
                }
            if mode == "delay_after_commit" and status == 200:
                server.committed_before_delay.set()
                time.sleep((RECEIPT_TIMEOUT_MS + 1500) / 1000)
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        except (BrokenPipeError, ConnectionResetError):
            pass


def make_export_body(suffix: str) -> dict:
    return {
        "title": f"Q001 Synthetic {suffix}",
        "sourcePath": "synthetic://q001/probe",
        "sourceContent": "Synthetic Q001 proof content. No user data.",
        "memoryClass": "FULL_RECORD",
        "status": "SUCCESS",
        "claimBoundary": "Synthetic receipt is not artifact acceptance.",
        "receiptAnchor": f"q001-{suffix}-{int(time.time() * 1000)}",
    }


def inspect_store(stage: Path, store: Path, attempt: str) -> dict:
    sys.path.insert(0, str(stage / ENGINE))
    try:
        from ledger_layer.sqlite_ledger import SqliteLedger  # type: ignore
        ledger = SqliteLedger(store)
        chain = ledger.read_chain()
        block = ledger.lookup_request_id(attempt)
        return {
            "count": len(chain),
            "tipHash": chain[-1]["hash"] if chain else "GENESIS",
            "exactIdFound": block is not None,
            "blockHash": block["hash"] if block else None,
            "blockDecision": block["event"].get("decision") if block else None,
            "chainValid": True,
        }
    finally:
        sys.path.pop(0)


def run_probe(engine_docker_image: str | None = None, *, browser_export_only: bool = False) -> dict:
    RUNTIME.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="q001-system-chain-", dir=RUNTIME) as directory:
        scratch = Path(directory).resolve()
        if not scratch.is_relative_to(RUNTIME.resolve()):
            raise RuntimeError("disposable path escaped runtime")
        stage = scratch / "source"
        staged_count = stage_tracked_source(stage)
        web = stage / WEB
        engine = stage / ENGINE
        original_modules = ROOT / WEB / "node_modules"
        if not original_modules.is_dir():
            raise RuntimeError("installed Web dependencies unavailable")
        junction = web / "node_modules"
        subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(original_modules)],
                       check=True, capture_output=True)
        if not junction.is_dir():
            raise RuntimeError("dependency junction failed")
        store = scratch / "store" / "proof.sqlite"
        store.parent.mkdir()
        if store.exists() or store.resolve() == (ROOT / ENGINE / "ledger_layer/ledger_chain.json").resolve():
            raise RuntimeError("synthetic store was not fresh")
        token = "synthetic-q001-" + os.urandom(24).hex()
        engine_port, proxy_port, web_port = free_port(), free_port(), free_port()
        if len({engine_port, proxy_port, web_port}) != 3:
            raise RuntimeError("port collision")
        engine_log = open(scratch / "engine.log", "wb")
        web_log = open(scratch / "web.log", "wb")
        engine_process = None
        web_process = None
        proxy = None
        proxy_thread = None
        def start_engine() -> subprocess.Popen:
            env = os.environ.copy()
            for key in list(env):
                if key.upper().endswith("API_KEY"):
                    env.pop(key, None)
            env["CVF_GOVERNANCE_LEDGER_PATH"] = str(store)
            command = [sys.executable, "-m", "uvicorn", "api.server:app", "--host", "127.0.0.1", "--port", str(engine_port)]
            docker_name = None
            if engine_docker_image:
                docker_name = "cvf-q001-web-" + os.urandom(6).hex()
                command = ["docker", "run", "--rm", "--pull=never", "--name", docker_name,
                           "-p", f"127.0.0.1:{engine_port}:8100",
                           "--mount", f"type=bind,src={engine},dst=/engine,readonly",
                           "--mount", f"type=bind,src={store.parent},dst=/data",
                           "-w", "/engine", "-e", "CVF_GOVERNANCE_LEDGER_PATH=/data/proof.sqlite",
                           engine_docker_image, "python", "-m", "uvicorn", "api.server:app",
                           "--host", "0.0.0.0", "--port", "8100"]
            process = subprocess.Popen(
                command,
                cwd=engine, env=env, stdout=engine_log, stderr=subprocess.STDOUT,
            )
            if docker_name:
                process.cvf_docker_name = docker_name
            try:
                wait_ready(f"http://127.0.0.1:{engine_port}/api/v1/health", process)
            except BaseException:
                stop(process)
                raise
            return process
        try:
            engine_process = start_engine()
            engine_pid_initial = engine_process.pid
            proxy = EngineProxy(proxy_port, engine_port)
            proxy_thread = threading.Thread(target=proxy.serve_forever, daemon=True)
            proxy_thread.start()
            env = os.environ.copy()
            for key in list(env):
                if key in {"GITHUB_ID", "GITHUB_SECRET", "AUTH_SECRET", "NEXTAUTH_SECRET", "DATABASE_URL"} or key.startswith("CVF_") or key.upper().endswith("API_KEY"):
                    env.pop(key, None)
            env.update({
                "CVF_SERVICE_TOKEN": token,
                "NEXTAUTH_URL": f"http://127.0.0.1:{web_port}",
                "GOVERNANCE_ENGINE_URL": f"http://127.0.0.1:{proxy_port}",
                "GOVERNANCE_ENGINE_ENABLED": "true",
                "GOVERNANCE_ENGINE_TIMEOUT": str(ENGINE_TIMEOUT_MS),
                "CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS": str(RECEIPT_TIMEOUT_MS),
                "NEXT_TELEMETRY_DISABLED": "1",
            })
            if browser_export_only:
                env.update({"CVF_STORAGE_ADAPTER_TYPE": "file",
                            "CVF_CONTROL_PLANE_EVENTS_PATH": str(scratch / "browser-events.json")})
            web_process = subprocess.Popen(
                ["node", str(original_modules / "next/dist/bin/next"), "dev", "--webpack", "-p", str(web_port), "-H", "127.0.0.1"],
                cwd=web, env=env, stdout=web_log, stderr=subprocess.STDOUT,
            )
            wait_ready(f"http://127.0.0.1:{web_port}/login", web_process)
            if browser_export_only:
                # Compile the nested proxy without invoking the engine, so the
                # measured receipt timeout is not spent on Next dev compilation.
                warm_status, _ = request_json(f"http://127.0.0.1:{web_port}/api/governance/evaluate", {})
                if warm_status != 401 or proxy.forwarded != 0:
                    raise AssertionError("unauthenticated proxy warmup must not invoke engine")
                helper = ROOT / "scripts/probe_cvf_w05_browser_chain.cjs"
                staged_helper = scratch / helper.name
                shutil.copy2(helper, staged_helper)
                browser_output = scratch / "browser.json"
                browser_process = subprocess.run(
                    ["node", str(staged_helper), str(original_modules), f"http://127.0.0.1:{web_port}",
                     str(browser_output), str(scratch)],
                    cwd=web, env=env, timeout=150, capture_output=True, text=True,
                )
                if browser_process.returncode:
                    raise RuntimeError("Synthetic browser consumer failed: " + browser_process.stderr[-4000:])
                browser = json.loads(browser_output.read_text(encoding="utf-8"))
                attempt = browser["attemptId"]
                sqlite = inspect_store(stage, store, attempt)
                engine = proxy.engine_observations.get(attempt, {})
                if (proxy.forwarded != 1 or sqlite["count"] != 1 or not sqlite["exactIdFound"]
                        or engine.get("requestId") != attempt or engine.get("ledgerAttached") is not True):
                    raise AssertionError("browser receipt did not join single engine/store request")
                identities = [WEB / "src/app/(dashboard)/work-transfer/page.tsx",
                    WEB / "src/components/ArtifactExportPanel.tsx", WEB / "src/app/api/artifacts/export/route.ts",
                    WEB / "src/app/api/artifacts/export/proof.ts", WEB / "src/app/api/governance/evaluate/route.ts",
                    WEB / "src/lib/governance-engine.ts", WEB / "src/lib/route-governance-proof.ts",
                    WEB / "src/lib/bounded-request-body.ts",
                    ENGINE / "api/server.py", ENGINE / "ledger_layer/sqlite_ledger.py"]
                return {
                    "schemaVersion": "cvf.w05BrowserConsumerEvidence.v1", "browser": browser,
                    "sqlite": sqlite, "engineReport": engine, "forwardedEngineCalls": proxy.forwarded,
                    "executionBaseHead": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                    "stagedSourceHashes": {p.as_posix(): hashlib.sha256((stage / p).read_bytes()).hexdigest() for p in identities},
                    "stagedHelperSha256": hashlib.sha256(staged_helper.read_bytes()).hexdigest(),
                    "engineDockerImage": engine_docker_image,
                    "scope": "SYNTHETIC_BROWSER_TRANSPORT_PERSISTENCE_PRESENTATION",
                    "claimBoundary": "No live AI governance, artifact approval, independent review or real-data R2/R3 proof.",
                }
            export_url = f"http://127.0.0.1:{web_port}/api/artifacts/export"
            denied_status, denied = request_json(export_url, make_export_body("denied"), token=token)
            if denied_status != 401 or denied.get("routeGovernanceProof", {}).get("decision") != "DENY":
                raise AssertionError("unsigned service-token request did not deny")
            status, positive = request_json(export_url, make_export_body("positive"), token=token, signed=True)
            data = positive.get("data", {})
            proof = positive.get("routeGovernanceProof", {})
            attempt = data.get("governanceReceiptAttemptId")
            if status != 200 or not attempt or data.get("governanceReceiptStatus") != "PRESENT" or proof.get("authMode") != "service_token" or proof.get("decision") != "ALLOW":
                raise AssertionError("Web export did not retain signed service-token receipt")
            before_restart = inspect_store(stage, store, attempt)
            engine_positive = proxy.engine_observations.get(attempt, {})
            if (not before_restart["exactIdFound"] or data.get("governanceReceipt", {}).get("receiptId") != attempt
                    or engine_positive.get("requestId") != attempt or engine_positive.get("decision") != "ALLOW"
                    or engine_positive.get("action") != "ALLOW" or engine_positive.get("ledgerAttached") is not True):
                raise AssertionError("positive receipt did not join exact SQLite block")
            stop(engine_process)
            engine_process = start_engine()
            after_restart = inspect_store(stage, store, attempt)
            if before_restart != after_restart:
                raise AssertionError("SQLite exact-ID/tip changed across engine restart")
            proxy.mode = "malformed"
            malformed_status, malformed = request_json(export_url, make_export_body("malformed"), token=token, signed=True)
            proxy.mode = "unavailable"
            unavailable_status, unavailable = request_json(export_url, make_export_body("unavailable"), token=token, signed=True)
            proxy.mode = "delay_after_commit"
            timeout_status, timed = request_json(export_url, make_export_body("timeout"), token=token, signed=True)
            timeout_data = timed.get("data", {})
            timeout_attempt = timeout_data.get("governanceReceiptAttemptId")
            if not proxy.committed_before_delay.wait(2) or not timeout_attempt:
                raise AssertionError("response-loss commit/attempt not observed")
            timeout_store = inspect_store(stage, store, timeout_attempt)
            engine_timeout = proxy.engine_observations.get(timeout_attempt, {})
            if malformed_status != 200 or malformed.get("data", {}).get("governanceReceiptStatus") != "INVALID_RESPONSE":
                raise AssertionError("malformed response was not classified")
            if unavailable_status != 200 or unavailable.get("data", {}).get("governanceReceiptStatus") != "UNAVAILABLE":
                raise AssertionError("unavailable engine was not classified")
            if (timeout_status != 200 or timeout_data.get("governanceReceiptStatus") != "TIMED_OUT"
                    or not timeout_store["exactIdFound"] or engine_timeout.get("requestId") != timeout_attempt
                    or engine_timeout.get("ledgerAttached") is not True):
                raise AssertionError("response-loss ambiguity or exact-ID reconciliation failed")
            if data.get("governanceState") != "DRAFT_UNACCEPTED" or timeout_data.get("governanceState") != "DRAFT_UNACCEPTED":
                raise AssertionError("receipt was mistaken for artifact acceptance")
            if inspect_store(stage, store, "wrong-" + attempt)["exactIdFound"]:
                raise AssertionError("wrong request ID unexpectedly found")
            wrong_store = scratch / "store/wrong.sqlite"
            if inspect_store(stage, wrong_store, attempt)["exactIdFound"]:
                raise AssertionError("wrong store unexpectedly held request ID")
            if proxy.forwarded != 2:
                raise AssertionError("unexpected engine forwarding/replay count")
            return {
                "schemaVersion": "cvf.q001SyntheticSystemChainEvidence.v1",
                "scope": "DISPOSABLE_GIT_VISIBLE_WORKTREE_SOURCE_ONLY",
                "executionBaseHead": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                "stagedGitVisibleFileCount": staged_count,
                "stagedSourceHashes": {
                    str(relative).replace("\\", "/"): hashlib.sha256((stage / relative).read_bytes()).hexdigest()
                    for relative in (
                        WEB / "src/app/api/artifacts/export/route.ts",
                        WEB / "src/app/api/artifacts/export/proof.ts",
                        WEB / "src/lib/bounded-request-body.ts",
                        ENGINE / "api/server.py",
                        ENGINE / "ledger_layer/sqlite_ledger.py",
                    ) if (stage / relative).exists()
                },
                "stageExcludesEnvLocalAndCurrentJsonLedger": True,
                "storeIdentityCategory": "fresh-disposable-sqlite-in-ignored-runtime",
                "engineRuntime": "DOCKER_BIND_SYNTHETIC_STORE" if engine_docker_image else "HOST_PROCESS",
                "engineDockerImage": engine_docker_image,
                "processes": {"webPid": web_process.pid, "enginePidInitial": engine_pid_initial, "enginePidRestart": engine_process.pid if engine_process else None, "proxyPort": proxy_port},
                "timeoutMs": {"outerReceipt": RECEIPT_TIMEOUT_MS, "innerEngine": ENGINE_TIMEOUT_MS},
                "deniedAuth": {"httpStatus": denied_status, "decision": "DENY"},
                "positive": {"httpStatus": status, "authMode": proof["authMode"], "routeDecision": proof["decision"], "attemptId": attempt, "receiptStatus": data["governanceReceiptStatus"], "engineReport": engine_positive, "artifactState": data["governanceState"], "sqlite": before_restart},
                "restart": {"sameExactIdCountAndTip": before_restart == after_restart, "sqlite": after_restart},
                "malformed": {"httpStatus": malformed_status, "receiptStatus": malformed["data"]["governanceReceiptStatus"]},
                "unavailable": {"httpStatus": unavailable_status, "receiptStatus": unavailable["data"]["governanceReceiptStatus"]},
                "responseLoss": {"httpStatus": timeout_status, "receiptStatus": timeout_data["governanceReceiptStatus"], "attemptId": timeout_attempt, "engineReport": engine_timeout, "exactIdReconciliation": "FOUND", "safeToRetry": False, "artifactState": timeout_data["governanceState"], "sqlite": timeout_store},
                "negativeControls": {"wrongRequestIdAbsent": True, "wrongStoreAbsent": True, "forwardedEngineCalls": proxy.forwarded},
                "claimBoundary": "Synthetic process/store proof only; no artifact approval, real GitHub cutover, provider call or Q001/R0 exit.",
            }
        finally:
            stop(web_process)
            stop(engine_process)
            if proxy is not None:
                proxy.shutdown()
                proxy.server_close()
            if proxy_thread is not None:
                proxy_thread.join(timeout=3)
            engine_log.close()
            web_log.close()
            if junction.exists():
                os.rmdir(junction)


HCR_ROOT = RUNTIME / "ncr-html-configured-receipt-20261014" / "worker"
HCR_PRODUCT_PINS = "docs/reviews/evidence/ncr-html-configured-receipt-dispatch-20261014.json"
HCR_SAFE_ENV = {"PATH", "SYSTEMROOT", "SYSTEMDRIVE", "TEMP", "TMP", "USERPROFILE", "HOMEDRIVE", "HOMEPATH", "APPDATA",
                "LOCALAPPDATA", "COMSPEC", "PATHEXT", "WINDIR", "PROCESSOR_ARCHITECTURE", "NUMBER_OF_PROCESSORS", "OS", "USERNAME"}
HCR_RELAY = ("import asyncio,sys\nT=sys.argv[1]\n"
             "async def pipe(r,w):\n try:\n  while d:=await r.read(65536):\n   w.write(d);await w.drain()\n except Exception:pass\n finally:\n  w.close()\n"
             "async def h(r,w):\n try:u=await asyncio.open_connection(T,8100)\n except Exception:\n  w.close();return\n await asyncio.gather(pipe(r,u[1]),pipe(u[0],w))\n"
             "async def m():\n s=await asyncio.start_server(h,'0.0.0.0',8100);await s.serve_forever()\nasyncio.run(m())\n")
# Owned Node preload (written into the ignored namespace, never a tracked helper): loopback-only TCP/DNS for Next and the browser helper.
HCR_PRELOAD = r"""'use strict';
const fs = require('node:fs'), net = require('node:net'), dns = require('node:dns');
const LOG = process.env.CVF_HCR_EGRESS_LOG, LOCAL = new Set(['127.0.0.1', 'localhost', '::1']), seen = new Set();
const log = entry => { try { fs.appendFileSync(LOG, JSON.stringify({ pid: process.pid, title: process.title, argv: process.argv.slice(1, 4).map(a => String(a).split(/[\\/]/).pop()), ...entry }) + '\n'); } catch (_) {} };
const kind = host => (/(^|\.)(googleapis|gstatic)\.com$/i.test(host) ? 'passive-font-asset' : /dashscope|aliyun|openai|anthropic|deepseek|generativelanguage/i.test(host) ? 'provider-or-ai-api' : 'other-external');
const denied = host => ({ event: /\.invalid$/.test(host) ? 'selftest-denied' : 'denied', category: kind(host) });
const connect = net.Socket.prototype.connect;
net.Socket.prototype.connect = function (...args) {
  let a = Array.isArray(args[0]) ? args[0][0] : args[0];
  if (a === null || typeof a !== 'object') a = /^\d+$/.test(String(a)) ? { port: Number(a), host: typeof args[1] === 'string' ? args[1] : 'localhost' } : { path: String(a) };
  if (a.path) return connect.apply(this, args);
  const host = String(a.host || 'localhost').replace(/^\[|\]$/g, '').toLowerCase();
  if (!LOCAL.has(host)) {
    log(denied(host));
    process.nextTick(() => this.destroy(Object.assign(new Error('egress denied'), { code: 'ECVFEGRESSDENIED' })));
    return this;
  }
  if (!seen.has(a.port)) { seen.add(a.port); log({ event: 'loopback-connect', port: Number(a.port) }); }
  return connect.apply(this, args);
};
const lookup = dns.lookup;
dns.lookup = function (host, ...rest) {
  if (host && !LOCAL.has(String(host).toLowerCase())) {
    log({ ...denied(String(host)), event: 'denied-dns' });
    return process.nextTick(rest[rest.length - 1], Object.assign(new Error('egress denied'), { code: 'ECVFEGRESSDENIED' }));
  }
  return lookup.call(this, host, ...rest);
};
log({ event: 'loaded', nodeOptionsActive: Boolean(process.env.NODE_OPTIONS) });
net.connect({ host: 'egress-selftest.invalid', port: 9 }).on('error', () => {});
"""

def hcr_env(extra: dict) -> dict:
    env = {k: v for k, v in os.environ.items() if k.upper() in HCR_SAFE_ENV}
    env.update(extra)
    return env

def hcr_docker(*args: str, check: bool = True, timeout: int = 90) -> subprocess.CompletedProcess:
    return subprocess.run(["docker", *args], capture_output=True, text=True, check=check, timeout=timeout)

def hcr_ro_rows(store: Path) -> list:
    conn = sqlite3.connect(store.resolve().as_uri() + "?mode=ro", uri=True, timeout=1)
    try:
        return conn.execute("SELECT ordinal, request_id, block_json, block_hash FROM blocks ORDER BY ordinal").fetchall()
    finally:
        conn.close()

class HcrPoller(threading.Thread):
    def __init__(self, store: Path):
        super().__init__(daemon=True)
        self.store, self.halt, self.samples, self.errors = store, threading.Event(), [], 0

    def run(self) -> None:
        while not self.halt.is_set():
            try:
                rows = hcr_ro_rows(self.store)
                self.samples.append((int(time.time() * 1000), [(r[1], r[3], hashlib.sha256(r[2].encode()).hexdigest()) for r in rows]))
            except sqlite3.Error:
                self.errors += 1
            time.sleep(0.15)

def hcr_window(poller: HcrPoller, steps: list, start: str, end: str) -> dict:
    at = {s["step"]: s["atMs"] for s in steps}
    counts = [len(rows) for ms, rows in poller.samples if at[start] <= ms <= at[end]]
    return {"from": start, "to": end, "samples": len(counts), "min": min(counts, default=None), "max": max(counts, default=None)}

def run_configured_receipt_browser_composition(image: str) -> dict:
    started = time.time()
    failures: list[str] = []
    dispatch = json.loads((ROOT / HCR_PRODUCT_PINS).read_text(encoding="utf-8"))
    drift = [p["path"] for p in dispatch["sourcePins"] if not p["path"].startswith("scripts/")
             and hashlib.sha256((ROOT / p["path"]).read_bytes()).hexdigest() != p["rawSha256"]]
    if drift: raise RuntimeError(f"product pin drift: {drift}")
    inspected = hcr_docker("image", "inspect", image, "--format", "{{.Id}} {{.Os}} {{.Architecture}}").stdout.split()
    if inspected != [image, "linux", "amd64"]: raise RuntimeError("immutable image ID/os/architecture mismatch")
    HCR_ROOT.mkdir(parents=True, exist_ok=True)
    scratch = HCR_ROOT / ("run-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "-" + secrets.token_hex(3))
    scratch.mkdir()
    if scratch.is_symlink() or not scratch.resolve().is_relative_to(RUNTIME.resolve()): raise RuntimeError("namespace escaped ignored runtime")
    stage, custody, logs = scratch / "source", scratch / "custody", scratch / "logs"
    custody.mkdir(); logs.mkdir()
    staged_count = stage_tracked_source(stage)
    web, engine = stage / WEB, stage / ENGINE
    modules = ROOT / WEB / "node_modules"
    junction = web / "node_modules"
    subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(modules)], check=True, capture_output=True)
    store = scratch / "store" / "proof.sqlite"
    store.parent.mkdir()
    while len(ports := {free_port(), free_port(), free_port()}) < 3:
        pass
    engine_port, proxy_port, web_port = sorted(ports)
    token = "synthetic-hcr-" + secrets.token_hex(24)
    preload, egress_log = scratch / "egress-preload.cjs", logs / "egress.jsonl"
    preload.write_text(HCR_PRELOAD, encoding="utf-8")
    suffix = secrets.token_hex(4)
    net_name, engine_name, relay_name = f"cvf-ncr-hcr-net-{suffix}", f"cvf-q001-web-{suffix}", f"cvf-q001-web-relay-{suffix}"
    names_only = sorted(k for k in os.environ if any(t in k.upper() for t in ("KEY", "TOKEN", "SECRET", "PASSWORD", "AUTH", "DATABASE", "CREDENTIAL", "DASHSCOPE", "ALIBABA", "OPENAI", "ANTHROPIC")))
    engine_process = relay_process = web_process = helper = proxy = proxy_thread = poller = None
    logs_open = [open(logs / n, "wb") for n in ("engine.log", "relay.log", "web.log", "helper.stderr.log")]
    ipc: dict = {"stopRequests": 0, "other": [], "error": None}
    output = {"schemaVersion": "cvf.ncrHtmlConfiguredReceiptComposition.v1", "scope": "SYNTHETIC_BROWSER_TRANSPORT_PERSISTENCE_PRESENTATION_ONLY",
              "namespace": scratch.relative_to(ROOT).as_posix(), "image": inspected, "stagedGitVisibleFileCount": staged_count,
              "ports": {"engineRelay": engine_port, "proxy": proxy_port, "web": web_port}, "credentialLikeEnvNamesCleared": names_only,
              "executionBaseHead": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()}
    try:
        hcr_docker("network", "create", "--internal", net_name)
        engine_process = subprocess.Popen(
            ["docker", "run", "--rm", "--pull=never", "--name", engine_name, "--network", net_name,
             "--mount", f"type=bind,src={engine},dst=/engine,readonly", "--mount", f"type=bind,src={store.parent},dst=/data",
             "-w", "/engine", "-e", "CVF_GOVERNANCE_LEDGER_PATH=/data/proof.sqlite", image, "python", "-m", "uvicorn",
             "api.server:app", "--host", "0.0.0.0", "--port", "8100"], stdout=logs_open[0], stderr=subprocess.STDOUT)
        engine_process.cvf_docker_name = engine_name
        relay_process = subprocess.Popen(
            ["docker", "run", "--rm", "--pull=never", "--name", relay_name, "--network", "bridge", "-p", f"127.0.0.1:{engine_port}:8100",
             image, "python", "-c", HCR_RELAY, engine_name], stdout=logs_open[1], stderr=subprocess.STDOUT)
        relay_process.cvf_docker_name = relay_name
        for _ in range(60):
            if hcr_docker("container", "inspect", relay_name, "--format", "{{.State.Running}}", check=False).stdout.strip() == "true":
                break
            time.sleep(0.5)
        hcr_docker("network", "connect", net_name, relay_name)
        wait_ready(f"http://127.0.0.1:{engine_port}/api/v1/health", engine_process)
        inspect = json.loads(hcr_docker("container", "inspect", engine_name).stdout)[0]
        engine_id = inspect["Id"]
        probe = hcr_docker("exec", engine_name, "python", "-c",
                           "import socket\ns=socket.socket();s.settimeout(3)\ntry:\n s.connect(('1.1.1.1',53));print('OPEN')\nexcept OSError:\n print('BLOCKED')\n", check=False)
        output["engineContainer"] = {"idPrefix": engine_id[:12], "networks": sorted(inspect["NetworkSettings"]["Networks"]), "internalNetwork": net_name,
                                     "mounts": [{"dst": m["Destination"], "rw": m["RW"]} for m in inspect["Mounts"]], "credentialEnvNames": [e.split("=")[0] for e in inspect["Config"]["Env"] if e.split("=")[0] != "PATH"],
                                     "egressProbe": probe.stdout.strip(), "relay": "same image, no mounts, no credentials; bridge plus internal network; forwards loopback port to engine"}
        if output["engineContainer"]["egressProbe"] != "BLOCKED" or output["engineContainer"]["networks"] != [net_name]:
            failures.append("engine container is not egress-isolated")
        if store.exists() and hcr_ro_rows(store):
            failures.append("fresh store did not begin empty")
        proxy = EngineProxy(proxy_port, engine_port)
        proxy_thread = threading.Thread(target=proxy.serve_forever, daemon=True)
        proxy_thread.start()
        base = f"http://127.0.0.1:{web_port}"
        env = hcr_env({
            "NODE_OPTIONS": f'--require "{preload.as_posix()}"', "CVF_HCR_EGRESS_LOG": str(egress_log), "NEXT_TELEMETRY_DISABLED": "1",
            "NEXTAUTH_URL": base, "AUTH_URL": base, "NEXTAUTH_SECRET": secrets.token_hex(24), "AUTH_SECRET": secrets.token_hex(24),
            "CVF_SERVICE_TOKEN": token, "GOVERNANCE_ENGINE_URL": f"http://127.0.0.1:{proxy_port}", "GOVERNANCE_ENGINE_ENABLED": "true",
            "GOVERNANCE_ENGINE_TIMEOUT": str(ENGINE_TIMEOUT_MS), "CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS": str(RECEIPT_TIMEOUT_MS),
            "CVF_STORAGE_ADAPTER_TYPE": "file", "CVF_CONTROL_PLANE_EVENTS_PATH": str(scratch / "events.json"),
        })
        web_process = subprocess.Popen(["node", str(modules / "next/dist/bin/next"), "dev", "--webpack", "-p", str(web_port), "-H", "127.0.0.1"],
                                       cwd=web, env=env, stdout=logs_open[2], stderr=subprocess.STDOUT)
        wait_ready(f"{base}/login", web_process)
        warm_status, _ = request_json(f"{base}/api/governance/evaluate", {})
        if warm_status != 401 or proxy.attempted != 0:
            failures.append("unauthenticated proxy warmup reached the engine")
        entries = [json.loads(line) for line in egress_log.read_text(encoding="utf-8").splitlines() if line.strip()] if egress_log.exists() else []
        server_pids = {e["pid"] for e in entries if "start-server.js" in e.get("argv", []) or str(e.get("title", "")).startswith("next-server")}
        proven = {e["pid"] for e in entries if e["event"] == "selftest-denied"} & server_pids
        output["preflightEgress"] = {"loadedProcesses": len({e["pid"] for e in entries if e["event"] == "loaded"}), "serverPids": len(server_pids), "serverSelftestDenied": len(proven)}
        if not proven or hcr_ro_rows(store):
            raise RuntimeError("egress preload not proven in the Next server before first export, or store not empty")
        poller = HcrPoller(store)
        poller.start()
        helper_out = custody / "browser.json"
        helper = subprocess.Popen(["node", str(ROOT / "scripts/probe_cvf_w05_browser_chain.cjs"), str(modules), base, str(helper_out), str(custody), "configured-receipt-composition"],
                                  cwd=web, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=logs_open[3], text=True)

        def pump() -> None:
            for line in helper.stdout:
                line = line.strip()
                if line != "OWNED_ENGINE_STOP_REQUEST":
                    ipc["other"].append(line[:200])
                    continue
                ipc["stopRequests"] += 1
                if ipc["stopRequests"] > 1:
                    ipc["error"] = "second stop request"
                    continue
                try:
                    if json.loads(hcr_docker("container", "inspect", engine_name).stdout)[0]["Id"] != engine_id or engine_process.poll() is not None:
                        raise RuntimeError("owned engine identity changed")
                    stop(engine_process)
                    if hcr_docker("container", "inspect", engine_name, check=False).returncode == 0 or engine_process.poll() is None:
                        raise RuntimeError("owned engine did not exit")
                    ipc["engineStoppedAtMs"] = int(time.time() * 1000)
                    helper.stdin.write("OWNED_ENGINE_STOPPED\n")
                    helper.stdin.flush()
                except Exception as error:  # noqa: BLE001 - recorded as the consolidated blocker
                    ipc["error"] = str(error)[:300]
        pumper = threading.Thread(target=pump, daemon=True)
        pumper.start()
        try:
            helper.wait(timeout=300)
        except subprocess.TimeoutExpired:
            helper.kill()
            failures.append("browser helper timed out")
        pumper.join(timeout=5)
        time.sleep(0.5)
        poller.halt.set()
        poller.join(timeout=3)
        browser = json.loads(helper_out.read_text(encoding="utf-8")) if helper_out.exists() else {"partial": True, "error": "no helper output"}
        output["browser"] = browser
        output["ipc"] = ipc
        if helper.returncode or browser.get("partial") or ipc["error"] or ipc["stopRequests"] != 1:
            failures.append(f"browser composition incomplete: {browser.get('error') or ipc['error'] or helper.returncode}")
        final_rows = hcr_ro_rows(store)
        ids = [r[1] for r in final_rows]
        builds = [browser.get("req01", {}), browser.get("req04", {}).get("build2", {})]
        attempts = [b.get("attemptId") for b in builds]
        joins = []
        for build in builds:
            observed = proxy.engine_observations.get(build.get("attemptId"), {})
            matching = [r for r in final_rows if r[1] == build.get("attemptId")]
            joins.append({"attemptId": build.get("attemptId"), "sqlRowsWithRequestId": len(matching), "orchestratorBlockHash": matching[0][3] if matching else None,
                          "rowJson": json.loads(matching[0][2]) if matching else None, "engineArtifactId": observed.get("artifactId"),
                          "panelReceiptAnchor": build.get("receiptAnchor"), "engineRequestId": observed.get("requestId"), "ledgerAttached": observed.get("ledgerAttached"),
                          "engineDecisionLabel": observed.get("decision")})
            if len(matching) != 1 or observed.get("artifactId") != build.get("receiptAnchor") or observed.get("requestId") != build.get("attemptId"):
                failures.append("request/row/anchor join failed")
        first_hashes = {s[1][0][2] for s in poller.samples if s[1]}
        steps = browser.get("steps", [])
        windows = {}
        if steps and {"stale-edit-start", "stale-window-end", "reset-start", "reset-end", "engine-stopped", "build-3-end"} <= {s["step"] for s in steps}:
            windows = {"stale": hcr_window(poller, steps, "stale-edit-start", "stale-window-end"), "reset": hcr_window(poller, steps, "reset-start", "reset-end"),
                       "fallback": hcr_window(poller, steps, "engine-stopped", "build-3-end")}
        output["sql"] = {"finalCount": len(final_rows), "finalRequestIds": ids, "attemptIds": attempts, "joins": joins, "samples": len(poller.samples), "sampleErrors": poller.errors,
                         "maxCountObserved": max((len(s[1]) for s in poller.samples), default=None), "firstRowJsonHashesSeen": sorted(first_hashes), "windows": windows,
                         "tipHash": final_rows[-1][3] if final_rows else None, "readMode": "native sqlite3 URI mode=ro"}
        if len(final_rows) != 2 or sorted(ids) != sorted(attempts) or len(first_hashes) != 1 or output["sql"]["maxCountObserved"] != 2:
            failures.append("SQLite row accounting differs from two exact builds")
        if windows and (windows["stale"]["max"] != 1 or windows["reset"]["min"] != 2 or windows["reset"]["max"] != 2 or windows["fallback"]["max"] != 2):
            failures.append("row counts moved inside a no-export window")
        if windows and min(windows[k]["samples"] for k in windows) == 0:
            failures.append("a no-export window had no SQL sample")
        output["proxy"] = {"evaluateAttempted": proxy.attempted, "forwardedCompleted": proxy.forwarded, "forwardFailures": proxy.forward_failures, "mode": proxy.mode}
        if proxy.forwarded != 2 or proxy.attempted > 3 or proxy.mode != "forward":
            failures.append("evaluate accounting differs from 2 completed forwards")
        entries = [json.loads(line) for line in egress_log.read_text(encoding="utf-8").splitlines() if line.strip()]
        denied = {}
        for e in entries:
            if e["event"] in ("denied", "denied-dns"):
                denied[e["category"]] = denied.get(e["category"], 0) + 1
        output["finalEgress"] = {"serverDeniedByCategory": denied, "browserExternalRequests": browser.get("req07", {}).get("externalRequests"),
                                 "loopbackPortsSeen": sorted({e["port"] for e in entries if e["event"] == "loopback-connect"}), "providerStarts": 0}
        if denied.get("provider-or-ai-api") or browser.get("req07", {}).get("observedBrowserAiPosts"):
            failures.append("provider/AI egress attempt observed")
    finally:
        if poller is not None:
            poller.halt.set()
        cleanup = {}
        for label, proc in (("helper", helper), ("web", web_process), ("engine", engine_process), ("relay", relay_process)):
            try:
                if label == "helper":
                    if proc is not None and proc.poll() is None:
                        proc.kill()
                else:
                    stop(proc)
            except Exception as error:  # noqa: BLE001
                cleanup[label + "Error"] = str(error)[:200]
        hcr_docker("network", "rm", net_name, check=False)
        if proxy is not None:
            proxy.shutdown(); proxy.server_close()
        if proxy_thread is not None:
            proxy_thread.join(timeout=3)
        for handle in logs_open:
            handle.close()
        if junction.exists():
            os.rmdir(junction)
        left = hcr_docker("ps", "-a", "--format", "{{.Names}}", check=False).stdout.split() + hcr_docker("network", "ls", "--format", "{{.Name}}", check=False).stdout.split()
        cleanup["ownedDockerObjectsRemaining"] = [n for n in left if n.endswith(suffix)]
        cleanup["portsListening"] = [p for p in (engine_port, proxy_port, web_port) if socket.socket().connect_ex(("127.0.0.1", p)) == 0]
        output["cleanup"] = cleanup
        output["elapsedSeconds"] = round(time.time() - started, 1)
        output["failures"] = failures
        output["ok"] = not failures and not cleanup["ownedDockerObjectsRemaining"] and not cleanup["portsListening"]
        (custody / "runner-result.json").write_text(json.dumps(output, indent=2, sort_keys=True), encoding="utf-8")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine-docker-image", help="Explicit prebuilt local test image; never builds or pulls it")
    parser.add_argument("--browser-export-only", action="store_true", help="One browser export/download; do not replay five HTTP cases")
    parser.add_argument("--configured-receipt-browser-composition", action="store_true", help="Opt-in: one fresh configured-receipt browser composition (requires immutable --engine-docker-image)")
    args = parser.parse_args()
    if args.configured_receipt_browser_composition:
        if not args.engine_docker_image or not args.engine_docker_image.startswith("sha256:"):
            parser.error("--configured-receipt-browser-composition requires --engine-docker-image sha256:<id>")
        outcome = run_configured_receipt_browser_composition(args.engine_docker_image)
        print(json.dumps(outcome, indent=2, sort_keys=True))
        sys.exit(0 if outcome["ok"] else 1)
    print(json.dumps(run_probe(args.engine_docker_image, browser_export_only=args.browser_export_only), indent=2, sort_keys=True))
