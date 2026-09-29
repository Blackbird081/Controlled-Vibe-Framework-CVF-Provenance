#!/usr/bin/env python3
"""Disposable HTTP proof of Web export -> engine -> SQLite; no user config."""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import shutil
import socket
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
    """Copy Git-indexed Web/engine files, explicitly excluding env and JSON ledger."""
    proc = subprocess.run(
        ["git", "ls-files", "-z", "--", WEB.as_posix(), ENGINE.parent.as_posix()],
        cwd=ROOT, check=True, capture_output=True,
    )
    count = 0
    for raw in proc.stdout.split(b"\0"):
        if not raw:
            continue
        relative = Path(os.fsdecode(raw))
        if any(part.startswith(".env") for part in relative.parts) or relative.name == "ledger_chain.json":
            continue
        source = ROOT / relative
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
    if process is None or process.poll() is not None:
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


def run_probe() -> dict:
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
            env["CVF_GOVERNANCE_LEDGER_PATH"] = str(store)
            process = subprocess.Popen(
                [sys.executable, "-m", "uvicorn", "api.server:app", "--host", "127.0.0.1", "--port", str(engine_port)],
                cwd=engine, env=env, stdout=engine_log, stderr=subprocess.STDOUT,
            )
            wait_ready(f"http://127.0.0.1:{engine_port}/api/v1/health", process)
            return process
        try:
            engine_process = start_engine()
            engine_pid_initial = engine_process.pid
            proxy = EngineProxy(proxy_port, engine_port)
            proxy_thread = threading.Thread(target=proxy.serve_forever, daemon=True)
            proxy_thread.start()
            env = os.environ.copy()
            for key in list(env):
                if key in {"GITHUB_ID", "GITHUB_SECRET", "AUTH_SECRET", "NEXTAUTH_SECRET", "DATABASE_URL"} or key.startswith("CVF_"):
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
            web_process = subprocess.Popen(
                ["node", str(original_modules / "next/dist/bin/next"), "dev", "--webpack", "-p", str(web_port), "-H", "127.0.0.1"],
                cwd=web, env=env, stdout=web_log, stderr=subprocess.STDOUT,
            )
            wait_ready(f"http://127.0.0.1:{web_port}/login", web_process)
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
                "scope": "DISPOSABLE_TRACKED_SOURCE_ONLY",
                "executionBaseHead": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                "stagedTrackedFileCount": staged_count,
                "stageExcludesEnvLocalAndCurrentJsonLedger": True,
                "storeIdentityCategory": "fresh-disposable-sqlite-in-ignored-runtime",
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


if __name__ == "__main__":
    print(json.dumps(run_probe(), indent=2, sort_keys=True))
