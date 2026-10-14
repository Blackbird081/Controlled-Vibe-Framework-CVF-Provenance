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
from collections import Counter
from contextlib import closing, suppress
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
            try:
                with urllib.request.urlopen(request, timeout=6) as response:
                    status, payload = response.status, response.read()
            except urllib.error.HTTPError as error:
                status, payload = error.code, error.read()
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


HCR_ROOT = RUNTIME / "ncr-html-configured-receipt-20261014" / "conditional-worker"
HCR_PINS = "docs/reviews/evidence/ncr-html-configured-receipt-repair-dispatch-20261014.json"
HCR_PATHS = {"scripts/probe_cvf_q001_synthetic_system_chain.py", "scripts/probe_cvf_w05_browser_chain.cjs", "docs/reviews/CVF_NCR_HTML_CONFIGURED_RECEIPT_CONDITIONAL_RETURN_2026-10-14.md",
             "docs/reviews/evidence/ncr-html-configured-receipt-conditional-worker-20261014.json"}
HCR_EXPORT_CAP, HCR_ALIVE_CAP = 3, 2
HCR_PASSIVE = {"fonts.googleapis.com": "passive-font-asset", "fonts.gstatic.com": "passive-font-asset", "registry.npmjs.org": "framework-version-metadata"}
HCR_SAFE_ENV = {"PATH", "SYSTEMROOT", "SYSTEMDRIVE", "TEMP", "TMP", "USERPROFILE", "HOMEDRIVE", "HOMEPATH", "APPDATA",
                "LOCALAPPDATA", "COMSPEC", "PATHEXT", "WINDIR", "PROCESSOR_ARCHITECTURE", "NUMBER_OF_PROCESSORS", "OS", "USERNAME"}
# Bounded transport into the network=none engine container: one fixed loopback HTTP call per docker exec.
HCR_EXEC = ("import http.client,json,sys\nx=json.load(sys.stdin);c=http.client.HTTPConnection('127.0.0.1',8100,timeout=4)\n"
            "c.request(x['method'],x['path'],json.dumps(x['body']) if x.get('body') is not None else None,{'Content-Type':'application/json'})\n"
            "r=c.getresponse();print(json.dumps({'status':r.status,'body':r.read().decode()}))\n")

def hcr_docker(*args: str, check: bool = True, timeout: int = 90) -> subprocess.CompletedProcess:
    return subprocess.run(["docker", *args], capture_output=True, text=True, check=check, timeout=timeout)

def hcr_exec(container: str, method: str, path: str, body: dict | None = None, timeout: int = 6) -> tuple[int, bytes]:
    proc = subprocess.run(["docker", "exec", "-i", container, "python", "-c", HCR_EXEC], capture_output=True, text=True, timeout=timeout, check=True,
                          input=json.dumps({"method": method, "path": path, "body": body}))
    reply = json.loads(proc.stdout)
    return reply["status"], reply["body"].encode()

def hcr_ro_rows(store: Path) -> list:
    if not store.exists():
        return []
    with closing(sqlite3.connect(store.resolve().as_uri() + "?mode=ro", uri=True, timeout=1)) as conn:
        return conn.execute("SELECT ordinal, request_id, block_json, block_hash FROM blocks ORDER BY ordinal").fetchall()

def hcr_egress(path: Path, event: str | None = None) -> list:
    return [e for e in (json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()) if event in (None, e["event"])] if path.exists() else []

def hcr_classify(host: str) -> str:
    host = host.lower()
    if host == "egress-selftest.invalid" or host in HCR_PASSIVE:
        return HCR_PASSIVE.get(host, "selftest")
    return "provider-or-ai-api" if any(t in host for t in ("dashscope", "aliyun", "openai", "anthropic", "deepseek", "generativelanguage")) else "unknown-external"

def hcr_admit_egress(denied: list) -> list:  # fail closed: every denied destination must be the self-test or an exact known passive request
    for entry in denied:
        if (category := hcr_classify(entry["host"])) not in ("selftest", *HCR_PASSIVE.values()):
            raise RuntimeError(f"unclassified egress {category}: host={entry['host']} via={entry.get('via')} site={entry.get('site')}")
    return sorted(hcr_classify(e["host"]) for e in denied)

def hcr_admit_export(n: int, state: dict, denied: list, alive: bool, failure: str | None) -> None:  # pre-effect admission: failure, cap/order, egress, planned engine liveness
    if failure or state["error"] or n != state["exports"] + 1 or n > HCR_EXPORT_CAP or alive != (n <= 2):
        raise RuntimeError(f"export POST {n} refused (cap {HCR_EXPORT_CAP}, alive={alive}): {failure or state['error']}")
    hcr_admit_egress(denied)
    state["exports"] = n

def hcr_raised(fn, *args) -> bool:
    with suppress(RuntimeError):
        fn(*args)
        return False
    return True

def hcr_admit_forward(alive: bool, attempts: int) -> str:
    if alive and attempts >= HCR_ALIVE_CAP:
        raise RuntimeError("alive-engine forward budget exhausted")
    return "alive" if alive else "dead"

def hcr_admit_stop(requests: int, completed: int, matched_rows: int) -> None:
    if requests != 1 or completed != 2 or matched_rows != 2:
        raise RuntimeError(f"stop refused: request {requests}, completed {completed}, matched rows {matched_rows}")

def hcr_final_ok(failures: list, cleanup: dict) -> bool:
    return not (failures or cleanup["errors"] or cleanup["pidsAlive"] or cleanup["dockerRemaining"] or cleanup["portsListening"]) and cleanup["stageRemoved"]

class HcrProxy(ThreadingHTTPServer):  # opt-in; legacy EngineProxy/ProxyHandler stay untouched; the engine is reachable only through bounded docker exec
    def __init__(self, port: int, container: str):
        super().__init__(("127.0.0.1", port), HcrHandler)
        self.container, self.lock, self.alive, self.failure, self.daemon_threads, self.order, self.observed = container, threading.Lock(), True, None, True, [], {}
        self.arrived = self.alive_attempts = self.dead_failures = self.refused = 0

class HcrHandler(BaseHTTPRequestHandler):
    log_message = lambda *_args: None  # noqa: E731 - quiet like the legacy handler

    def do_POST(self) -> None:
        s: HcrProxy = self.server  # type: ignore[assignment]
        raw = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        if self.path != "/api/v1/evaluate":
            return self.send_error(404)
        with s.lock:
            s.arrived += 1
            try:
                mode = hcr_admit_forward(s.alive, s.alive_attempts)
            except RuntimeError as error:  # a refused extra evaluate is never executed
                s.refused, s.failure = s.refused + 1, s.failure or str(error)
                return self.send_error(429)
            s.alive_attempts += mode == "alive"
        try:
            status, payload = hcr_exec(s.container, "POST", self.path, json.loads(raw))
        except (OSError, subprocess.SubprocessError, ValueError, KeyError) as error:  # actual absence/ambiguity: no replay, no simulated status
            with s.lock:
                s.dead_failures += mode == "dead"
                s.failure = s.failure or (None if mode == "dead" else f"alive forward failed or ambiguous: {type(error).__name__}")
            self.close_connection = True
            return
        with s.lock:
            s.failure = s.failure or ("engine answered after confirmed stop" if mode == "dead" else None)
            s.order.append(json.loads(raw)["request_id"])
            s.observed[s.order[-1]] = (status, payload)
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

def hcr_controls() -> dict:  # tiny generic harness probes (no product, engine or provider call); original gaps and legacy identity: separate static comparisons
    bad, clean, first = {"host": "example.org", "via": "tcp", "site": ["x.js:1"]}, {"errors": [], "pidsAlive": [], "dockerRemaining": [], "portsListening": [], "stageRemoved": True}, {"exports": 0, "error": None}
    corrected = {
        "unknownAndProviderEgressRaise": hcr_raised(hcr_admit_egress, [bad]) and hcr_raised(hcr_admit_egress, [{"host": "dashscope.aliyuncs.com"}]),
        "knownPassiveClassified": hcr_admit_egress([{"host": h} for h in (*HCR_PASSIVE, "egress-selftest.invalid")]) == ["framework-version-metadata", "passive-font-asset", "passive-font-asset", "selftest"],
        "unknownPreflightBlocksFirstExport": hcr_raised(hcr_admit_export, 1, first, [bad], True, None) and first["exports"] == 0,
        "fourthExportAndWrongLivenessRaise": hcr_raised(hcr_admit_export, 4, {"exports": 3, "error": None}, [], False, None) and hcr_raised(hcr_admit_export, 3, {"exports": 2, "error": None}, [], True, None),
        "thirdAliveForwardRaises": hcr_raised(hcr_admit_forward, True, HCR_ALIVE_CAP) and hcr_admit_forward(False, HCR_ALIVE_CAP) == "dead",
        "earlyOrRepeatedStopRaises": hcr_raised(hcr_admit_stop, 1, 1, 2) and hcr_raised(hcr_admit_stop, 1, 2, 1) and hcr_raised(hcr_admit_stop, 2, 2, 2) and hcr_admit_stop(1, 2, 2) is None,
        "cleanupErrorCannotBeOk": not any(hcr_final_ok(f, {**clean, **c}) for f, c in (([], {"errors": ["x"]}), ([], {"pidsAlive": [1]}), (["f"], {}), ([], {"stageRemoved": False}))) and hcr_final_ok([], clean)}
    if not all(corrected.values()):
        raise RuntimeError("harness control probes failed: " + json.dumps(corrected, sort_keys=True))
    return corrected

def hcr_verify_engine(name: str, image: str, engine_process: subprocess.Popen) -> dict:
    host = hcr_docker("context", "inspect", "--format", "{{.Endpoints.docker.Host}}").stdout.strip()
    info = json.loads(hcr_docker("container", "inspect", name).stdout)[0]
    image_env = {e.split("=")[0] for e in json.loads(hcr_docker("image", "inspect", image).stdout)[0]["Config"]["Env"]}
    probe = hcr_docker("exec", name, "python", "-c", "import socket;print(','.join(n for _, n in socket.if_nameindex()))\ntry:socket.create_connection(('1.1.1.1',53),3);print('OPEN')\nexcept OSError:print('BLOCKED')").stdout.split()
    ev = {"dockerEndpointKind": host.split(":")[0], "idPrefix": info["Id"][:12], "name": info["Name"], "image": info["Image"], "networkMode": info["HostConfig"]["NetworkMode"],
          "networks": sorted(info["NetworkSettings"]["Networks"]), "portBindings": info["HostConfig"]["PortBindings"], "interfaces": probe[0], "egressProbe": probe[1],
          "mounts": {m["Destination"]: ("rw" if m["RW"] else "ro") for m in info["Mounts"]}, "addedEnvNames": sorted({e.split("=")[0] for e in info["Config"]["Env"]} - image_env)}
    if not (ev["dockerEndpointKind"] == "npipe" and os.environ.get("DOCKER_HOST", "npipe:").startswith("npipe:") and ev["name"] == "/" + name and ev["image"] == image and ev["networkMode"] == "none"
            and ev["networks"] == ["none"] and not ev["portBindings"] and ev["interfaces"] == "lo" and ev["egressProbe"] == "BLOCKED" and ev["mounts"] == {"/engine": "ro", "/data": "rw"}
            and ev["addedEnvNames"] == ["CVF_GOVERNANCE_LEDGER_PATH"] and engine_process.poll() is None):
        raise RuntimeError("engine container identity/isolation not verified: " + json.dumps(ev, sort_keys=True))
    return {**ev, "id": info["Id"]}

def hcr_remove_stage(stage: Path, namespace: Path) -> None:
    if (stage / WEB / "node_modules").exists():
        os.rmdir(stage / WEB / "node_modules")  # junction to the installed dependencies: remove the link, never the target
    if stage.is_symlink() or not stage.resolve().is_relative_to(namespace.resolve()):
        raise RuntimeError("stage escaped the owned namespace")
    for base, dirs, files in os.walk(stage):
        if any(os.lstat(Path(base) / item).st_file_attributes & 0x400 for item in dirs + files):
            raise RuntimeError("reparse point inside stage; not removed")
    shutil.rmtree(stage)

def run_configured_receipt_browser_composition(image: str) -> dict:
    started, failures, state = time.time(), [], {"exports": 0, "stopRequests": 0, "gates": [], "error": None}
    controls, git = hcr_controls(), lambda *a: subprocess.check_output(["git", *a], cwd=ROOT, text=True)
    pins = json.loads((ROOT / HCR_PINS).read_text(encoding="utf-8"))["sourcePins"]
    drift = [p["path"] for p in pins if not p["path"].startswith("scripts/") and hashlib.sha256((ROOT / p["path"]).read_bytes()).hexdigest() != p["rawSha256"]]
    dirty = sorted(x[3:].strip('"') for x in git("status", "--porcelain", "--untracked-files=all").splitlines() if x[3:].strip('"') not in HCR_PATHS)
    inspected = hcr_docker("image", "inspect", image, "--format", "{{.Id}} {{.Os}} {{.Architecture}}").stdout.split()
    if drift or dirty or git("diff", "--cached", "--name-only").split() or inspected != [image, "linux", "amd64"]:
        raise RuntimeError(f"pin drift {drift}, extra dirty paths {dirty}, staged paths or image mismatch {inspected}")
    scratch = HCR_ROOT / ("run-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "-" + secrets.token_hex(3))
    stage, custody, logs, store = scratch / "source", scratch / "custody", scratch / "logs", scratch / "store" / "proof.sqlite"
    for folder in (custody, logs, store.parent):
        folder.mkdir(parents=True)
    proxy_port, web_port = sorted({free_port(), free_port()})  # a collision raises here, before any effect
    name, base, egress_log, cjs = f"cvf-q001-web-{secrets.token_hex(4)}", f"http://127.0.0.1:{web_port}", logs / "egress.jsonl", ROOT / "scripts/probe_cvf_w05_browser_chain.cjs"
    engine_process = web_process = helper = proxy = proxy_thread = None
    owned_pids: set = set()  # Next server, browser helper and every Node process that loaded the egress guard
    logs_open = [open(logs / n, "wb") for n in ("engine.log", "web.log", "helper.stderr.log")]
    output = {"schemaVersion": "cvf.ncrHtmlConfiguredReceiptComposition.v2", "scope": "SYNTHETIC_BROWSER_TRANSPORT_PERSISTENCE_PRESENTATION_ONLY", "controls": controls, "state": state,
              "namespace": scratch.relative_to(ROOT).as_posix(), "image": inspected, "ports": {"proxy": proxy_port, "web": web_port}, "executionBaseHead": git("rev-parse", "HEAD").strip(),
              "credentialLikeEnvNamesCleared": sorted(k for k in os.environ if any(t in k.upper() for t in ("KEY", "TOKEN", "SECRET", "PASSWORD", "AUTH", "DATABASE", "CREDENTIAL", "DASHSCOPE", "ALIBABA", "OPENAI", "ANTHROPIC")))}
    try:
        output["stagedGitVisibleFileCount"] = stage_tracked_source(stage)
        web, engine, modules = stage / WEB, stage / ENGINE, ROOT / WEB / "node_modules"
        subprocess.run(["cmd", "/c", "mklink", "/J", str(web / "node_modules"), str(modules)], check=True, capture_output=True)
        engine_process = subprocess.Popen(
            ["docker", "run", "--rm", "--pull=never", "--name", name, "--network", "none",
             "--mount", f"type=bind,src={engine},dst=/engine,readonly", "--mount", f"type=bind,src={store.parent},dst=/data",
             "-w", "/engine", "-e", "CVF_GOVERNANCE_LEDGER_PATH=/data/proof.sqlite", image, "python", "-m", "uvicorn",
             "api.server:app", "--host", "127.0.0.1", "--port", "8100"], stdout=logs_open[0], stderr=subprocess.STDOUT)
        engine_process.cvf_docker_name = name
        for _ in range(150):  # health through the same bounded exec transport
            time.sleep(0.4)
            try:
                if engine_process.poll() is None and hcr_exec(name, "GET", "/api/v1/health")[0] == 200:
                    break
            except (OSError, subprocess.SubprocessError, ValueError):
                pass
        else:
            raise TimeoutError("owned engine not healthy")
        output["engineContainer"] = hcr_verify_engine(name, image, engine_process)
        if hcr_ro_rows(store):
            raise RuntimeError("fresh store did not begin empty")
        proxy = HcrProxy(proxy_port, name)
        proxy_thread = threading.Thread(target=proxy.serve_forever, daemon=True)
        proxy_thread.start()
        shutil.copy2(cjs, custody / "browser-helper.cjs")  # runs as the entry module; the repository path is the --require guard copy
        env = {k: v for k, v in os.environ.items() if k.upper() in HCR_SAFE_ENV}
        env.update({
            "NODE_OPTIONS": f'--require "{cjs.as_posix()}"', "CVF_HCR_EGRESS_LOG": str(egress_log), "NEXT_TELEMETRY_DISABLED": "1",
            "NEXTAUTH_URL": base, "AUTH_URL": base, "NEXTAUTH_SECRET": secrets.token_hex(24), "AUTH_SECRET": secrets.token_hex(24),
            "CVF_SERVICE_TOKEN": "synthetic-hcr-" + secrets.token_hex(24), "GOVERNANCE_ENGINE_URL": f"http://127.0.0.1:{proxy_port}", "GOVERNANCE_ENGINE_ENABLED": "true",
            "GOVERNANCE_ENGINE_TIMEOUT": str(ENGINE_TIMEOUT_MS), "CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS": str(RECEIPT_TIMEOUT_MS),
            "CVF_STORAGE_ADAPTER_TYPE": "file", "CVF_CONTROL_PLANE_EVENTS_PATH": str(scratch / "events.json")})
        web_process = subprocess.Popen(["node", str(modules / "next/dist/bin/next"), "dev", "--webpack", "-p", str(web_port), "-H", "127.0.0.1"],
                                       cwd=web, env=env, stdout=logs_open[1], stderr=subprocess.STDOUT)
        wait_ready(f"{base}/login", web_process)
        if request_json(f"{base}/api/governance/evaluate", {})[0] != 401 or proxy.arrived:
            raise RuntimeError("unauthenticated proxy warmup reached the engine")
        entries = hcr_egress(egress_log)
        proven = {e["pid"] for e in entries if e["event"] == "denied" and hcr_classify(e["host"]) == "selftest" and ("start-server.js" in e.get("argv", []) or str(e.get("title", "")).startswith("next-server"))}
        output["preflightEgress"] = {"loadedProcesses": len({e["pid"] for e in entries if e["event"] == "loaded"}), "serverSelftestDenied": len(proven), "classified": hcr_admit_egress(hcr_egress(egress_log, "denied"))}
        if not proven:
            raise RuntimeError("egress guard not proven in the Next server before the first export")
        helper = subprocess.Popen(["node", str(custody / "browser-helper.cjs"), str(modules), base, str(custody / "browser.json"), str(custody), "configured-receipt-composition"],
                                  cwd=web, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=logs_open[2], text=True)
        view = lambda: {"arrived": proxy.arrived, "aliveAttempts": proxy.alive_attempts, "completed": len(proxy.order), "alive": proxy.alive,  # noqa: E731 - read-only SQL view at a boundary
                        "rows": [(r[3], hashlib.sha256(r[2].encode()).hexdigest()) for r in hcr_ro_rows(store)]}

        def handle(line: str) -> str:
            try:
                if line.startswith("EXPORT_GATE_REQUEST "):
                    gate = json.loads(line.split(" ", 1)[1])
                    hcr_admit_export(gate["n"], state, hcr_egress(egress_log, "denied") + gate["external"], proxy.alive, proxy.failure or ("browser AI POST observed" if gate["aiPosts"] else None))
                    state["gates"].append({"n": gate["n"], **view()})
                    return f"EXPORT_GATE_OK {gate['n']}"
                if line == "OWNED_ENGINE_STOP_REQUEST":
                    state["stopRequests"] += 1
                    ids = {r[1] for r in hcr_ro_rows(store)}
                    hcr_admit_stop(state["stopRequests"], len(proxy.order), len([r for r in proxy.order if r in ids]))
                    if json.loads(hcr_docker("container", "inspect", name).stdout)[0]["Id"] != output["engineContainer"]["id"] or engine_process.poll() is not None:
                        raise RuntimeError("owned engine identity changed")
                    stop(engine_process)
                    if hcr_docker("container", "inspect", name, check=False).returncode == 0 or engine_process.poll() is None:
                        raise RuntimeError("owned engine did not exit")
                    proxy.alive = False
                    return "OWNED_ENGINE_STOPPED"
                raise RuntimeError("unknown control line")
            except Exception as error:  # noqa: BLE001 - recorded as the consolidated blocker
                state["error"] = state["error"] or str(error)[:300]
                return "EXPORT_GATE_DENY" if line.startswith("EXPORT_GATE") else "OWNED_ENGINE_STOP_DENIED"
        (watchdog := threading.Timer(300, helper.kill)).start()
        for line in helper.stdout:  # sequential admission: the helper blocks until each reply
            helper.stdin.write(handle(line.strip()) + "\n")
            helper.stdin.flush()
        helper.wait()
        watchdog.cancel()
        browser = json.loads((custody / "browser.json").read_text(encoding="utf-8")) if (custody / "browser.json").exists() else {"partial": True, "error": "no helper output"}
        output["browser"], output["finalView"], rows = browser, (final := view()), hcr_ro_rows(store)
        (custody / "raw-observations.json").write_text(json.dumps({"sqlRows": rows, "enginePayloads": {k: [v[0], v[1].decode()] for k, v in proxy.observed.items()}}), encoding="utf-8")
        builds = [browser.get("req01", {}), browser.get("req04", {}).get("build2", {})]
        reports = [json.loads(proxy.observed.get(b.get("attemptId"), (0, b"{}"))[1]).get("data", {}) for b in builds]
        denied, g = hcr_egress(egress_log, "denied"), state["gates"]
        external = [{**x, "category": hcr_classify(x["host"])} for x in browser.get("req07", {}).get("externalRequests", [])]
        provider = sum(hcr_classify(e["host"]) == "provider-or-ai-api" for e in denied + external)
        output["finalEgress"] = {"serverDenied": sorted(f"{h}|{c}|{v}|{s}|{n}" for (h, c, v, s), n in Counter((e["host"], hcr_classify(e["host"]), e["via"], ",".join(e.get("site", []))) for e in denied).items()),
                                 "browserExternal": external, "browserAiPosts": browser.get("req07", {}).get("observedBrowserAiPosts"), "providerAttempts": provider, "providerStarts": provider}
        output["checks"] = checks = {
            "helperCompleted": not (helper.returncode or browser.get("partial") or state["error"]) and state["stopRequests"] == 1,
            "requestRowAnchorJoins": [r[1] for r in rows] == [b.get("attemptId") for b in builds] and all(len([r for r in rows if r[1] == b.get("attemptId")]) == 1 and d.get("report", {}).get("request_summary", {}).get("request_id") == b.get("attemptId")
                                         and d.get("report", {}).get("request_summary", {}).get("artifact_id") == b.get("receiptAnchor") and d.get("execution_record", {}).get("ledger_attached") is True for b, d in zip(builds, reports)),
            "gateCounters": [(x["arrived"], x["aliveAttempts"], x["completed"], x["alive"], len(x["rows"])) for x in g] == [(0, 0, 0, True, 0), (1, 1, 1, True, 1), (2, 2, 2, False, 2)],
            "firstRowUnchanged": len(final["rows"]) == 2 and g[1]["rows"][0] == g[2]["rows"][0] == final["rows"][0] if len(g) == 3 else False,
            "noExtraAfterFallback": (final["arrived"], final["aliveAttempts"], final["completed"], proxy.dead_failures, proxy.refused, state["exports"], browser.get("req07", {}).get("exportPostCount")) == (3, 2, 2, 1, 0, 3, 3) and not proxy.failure,
            "noProviderOrAi": not provider and not browser.get("req07", {}).get("observedBrowserAiPosts"),
            "allEgressClassified": all(hcr_classify(e["host"]) in ("selftest", *HCR_PASSIVE.values()) for e in denied + external)}
        failures += [k for k, ok in checks.items() if not ok]
    except Exception as error:  # noqa: BLE001 - any preflight/runtime stop fails the outcome
        failures.append(f"stopped: {type(error).__name__}: {str(error)[:400]}")
    finally:
        cleanup: dict = {"errors": [], "pidsAlive": [], "dockerRemaining": [], "portsListening": [], "stageRemoved": False}
        roots = {p.pid for p in (web_process, helper) if p is not None}

        def attempt(label: str, fn, *args) -> None:
            try:
                fn(*args)
            except Exception as error:  # noqa: BLE001 - every cleanup error fails the outcome
                cleanup["errors"].append(f"{label}: {type(error).__name__}: {str(error)[:160]}")
        owned_pids.update(roots | {e["pid"] for e in hcr_egress(egress_log) if e["event"] == "loaded"})
        attempt("kill", lambda: [subprocess.run(["taskkill", "/PID", str(p), "/T", "/F"], capture_output=True, timeout=30) for p in sorted(roots)])
        attempt("engine", stop, engine_process)
        attempt("proxy", lambda: (proxy_thread and proxy.shutdown(), proxy and proxy.server_close()))
        [handle_.close() for handle_ in logs_open]
        attempt("stage", lambda: stage.exists() and hcr_remove_stage(stage, scratch))
        cleanup["stageRemoved"] = not stage.exists()
        time.sleep(1.0)
        attempt("pids", lambda: cleanup.update(pidsAlive=[p for p in sorted(owned_pids) if f'"{p}"' in subprocess.run(["tasklist", "/FI", f"PID eq {p}", "/NH", "/FO", "CSV"], capture_output=True, text=True, timeout=30).stdout]))
        cleanup["dockerRemaining"] = [n for n in hcr_docker("ps", "-a", "--format", "{{.Names}}", check=False).stdout.split() if n == name]
        cleanup["portsListening"] = [p for p in (proxy_port, web_port) if socket.socket().connect_ex(("127.0.0.1", p)) == 0]
        output["cleanup"], output["elapsedSeconds"], output["failures"], output["ok"] = cleanup, round(time.time() - started, 1), failures, hcr_final_ok(failures, cleanup)
        (custody / "runner-result.json").write_text(json.dumps(output, indent=2, sort_keys=True, default=str), encoding="utf-8")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine-docker-image", help="Explicit prebuilt local test image; never builds or pulls it")
    parser.add_argument("--browser-export-only", action="store_true", help="One browser export/download; do not replay five HTTP cases")
    parser.add_argument("--configured-receipt-browser-composition", action="store_true", help="Opt-in: one fresh configured-receipt browser composition (requires immutable --engine-docker-image)")
    args = parser.parse_args()
    if args.configured_receipt_browser_composition:
        outcome = run_configured_receipt_browser_composition(args.engine_docker_image or parser.error("--configured-receipt-browser-composition requires --engine-docker-image sha256:<id>"))
        print(json.dumps(outcome, indent=2, sort_keys=True))
        sys.exit(0 if outcome["ok"] else 1)
    print(json.dumps(run_probe(args.engine_docker_image, browser_export_only=args.browser_export_only), indent=2, sort_keys=True))
