"""Finite, opt-in owned synthetic HTML invocation; legacy branches are not called."""
from __future__ import annotations

import argparse
import json
import os
import queue
import re
import secrets
import socket
import subprocess
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import execution as E
from . import profile as P
from . import protocol as PR
from .lifecycle import Native, child_evidence, no_reparse


class Proxy(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, port, c, prefix, container, cap):
        super().__init__(("127.0.0.1", port), Handler)
        self.c, self.prefix, self.container, self.cap = c, prefix, container, cap
        self.lock, self.arrived, self.attempts, self.observed, self.failure = threading.Lock(), 0, 0, {}, None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_args):
        pass

    def do_POST(self):
        s = self.server
        with s.lock:
            s.arrived += 1
            if self.path != "/api/v1/evaluate" or s.attempts >= s.cap or s.failure:
                s.failure = "unadmitted evaluate arrival"
                self.send_error(429)
                return
            s.attempts += 1  # charged before effect, including failures/ambiguity
        try:
            # Body: bounded size and reads. The forward below is a protocol-admitted command, so close or expiry while this read was
            # pending refuses the forward at the final admission immediately before the engine call.
            body = json.loads(PR.read_body(self.rfile, self.headers.get("Content-Length"), s.c.proto, arm=self.connection.settimeout))
            if (set(body) - {"request_id", "artifact_id", "payload", "cvf_phase", "cvf_risk_level", "skill_preflight"}
                    or body.get("cvf_phase") != "REVIEW" or body.get("cvf_risk_level") != "R0"):
                raise RuntimeError("unexpected engine recipient envelope")
            if "x-cvf-service-token" in self.headers or "cookie" in self.headers:
                raise RuntimeError("app authentication leaked to engine recipient")
            status, raw = P.engine_http(s.c, s.prefix, s.container, "POST", self.path, body)
            with s.lock:
                s.observed[body["request_id"]] = {"request": body, "status": status, "response": json.loads(raw),
                                                    "recipientExcerptSha256": E.sha(body["payload"]["content"].encode("utf-8", "surrogatepass"))}
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)
        except Exception as error:
            with s.lock:
                s.failure = f"engine hop failed/ambiguous: {type(error).__name__}: {E.bounded(error, 100)}"
            self.close_connection = True


def fetch(url, wait):
    with urllib.request.urlopen(url, timeout=wait) as response:
        return response.status


def child_probe(helper, custody, proto, claim):
    """Cleanup-phase parent verification of the child: independent exit, snapshot bytes and hash."""
    def probe():
        wait = proto.left(5)
        try:
            code = helper.wait(timeout=wait) if wait > 0 else None
        except subprocess.TimeoutExpired:
            code = None
        return child_evidence(lambda: (custody / "browser.json").read_bytes(), code, claim[0])
    return probe


def run(namespace, image, *, inputs=None, cap=2, controls_receipt=None, controls_digest=None, clock=None):
    started, failures = time.monotonic(), []
    # Pure admission precedes every effect: exact inputs, typed current controls, pinned sources, fresh namespace.
    if {"CVF_NCR_ALLOWED_PORTS", "CVF_HCR_EGRESS_LOG"} & set(os.environ):
        raise RuntimeError("inherited network-guard activation is refused")
    inputs = P.validate_inputs(P.fixtures() if inputs is None and cap == 2 else inputs, cap)
    actor = P.admit_controls(json.loads(Path(controls_receipt).read_text(encoding="utf-8")) if controls_receipt else None, cap, controls_digest)
    sources = P.admit_sources()
    namespace = Path(namespace).absolute()
    no_reparse(namespace.parent)
    if namespace.exists() or namespace.resolve().is_relative_to(P.ROOT) or not namespace.parent.is_dir():
        raise RuntimeError("a fresh namespace outside provenance is required")
    namespace.mkdir()
    custody, stage = namespace / "custody", namespace / "source"
    custody.mkdir()
    (namespace / "owner.json").write_text(json.dumps({"owner": actor, "nonce": secrets.token_hex(16), "namespace": str(namespace.resolve()),
        "source": sources, "profile": "NCR_HTML_OWNED_SYNTHETIC_FRESH_SOURCE_V1"}, indent=2), encoding="utf-8")
    proto = PR.Protocol(clock or time.monotonic, P.WORK_SECONDS, P.CLEANUP_SECONDS).start()  # the one phase/time owner; workEnd is fixed here
    c, ops, proxy, thread, reader_thread, helper = E.Collector(custody, proto=proto), None, None, None, None, None
    logs, reservations, budget, seen, claim = [], [], E.Budget(actor), set(), [None]
    output = {"schemaVersion": "cvf.ncrHtmlOwnedProfile.v1", "namespace": str(namespace), "sources": sources,
              "caps": {"exports": cap, "evaluates": cap, "readinessGets": budget.GLOBAL, "readinessBuckets": budget.LIMITS,
                       "runtimeSeconds": P.WORK_SECONDS, "cleanupSeconds": P.CLEANUP_SECONDS},
              "state": {"exports": 0, "readinessGets": budget.used}, "checkpoints": [], "failures": failures,
              "providerStarts": 0, "actualDataConfigStoreReads": 0, "retentionSeconds": None}

    def persist():
        (custody / "runner-result.json").write_bytes(E.dumps(output))

    def send(line):  # an admitted, bounded pipe write: an unfinished write stays a tracked UNKNOWN operation
        def write(_wait):
            helper.stdin.write(line + "\n")
            helper.stdin.flush()
        c.op("controller-reply", write, 10, bounded=True)
    try:
        ops = Native(c, [], stage, namespace)  # job policy is read back before any utility query or child exists
        c.runner = ops.run_utility
        prereq = P.prerequisites(c, image)
        ops.docker = prereq["dockerPrefix"]
        output["prerequisites"], output["controllerIdentity"] = prereq, ops.identity(os.getpid())
        manifest = P.stage_source(stage)
        (custody / "staged-source-manifest.json").write_text(json.dumps(manifest, sort_keys=True, indent=2), encoding="utf-8")
        output["staging"] = {"fileCount": len(manifest), "manifestSha256": E.sha((custody / "staged-source-manifest.json").read_bytes()),
                             "envAndActiveLedgerExcluded": True, "sourceCwd": str(stage / P.WEB)}
        modules, web, engine = Path(prereq["modules"]), stage / P.WEB, stage / P.ENGINE
        link = web / "node_modules"
        c.command("dependency-junction", ["cmd", "/c", "mklink", "/J", str(link), str(modules)])
        ops.dependency = (link, modules)
        if link.resolve() != modules.resolve():
            raise RuntimeError("read-only dependency-sharing identity mismatch")
        store, events = namespace / "stores/engine/proof.sqlite", namespace / "stores/control-plane-events.json"
        store.parent.mkdir(parents=True)
        events.write_text("[]", encoding="utf-8")
        for _ in range(2):
            sock = socket.socket()
            sock.bind(("127.0.0.1", 0))
            reservations.append(sock)
        web_port, proxy_port = [s.getsockname()[1] for s in reservations]
        ops.ports = [web_port, proxy_port]
        if ops.listeners():
            raise RuntimeError("reserved listener collision before startup")
        base = f"http://localhost:{web_port}"
        output["origin"], output["ports"] = base, ops.ports
        env = {k: os.environ[k] for k in os.environ if k.upper() in P.SAFE_ENV}
        name = "cvf-ncr-html-" + secrets.token_hex(8)
        for label in ("engine", "web", "helper"):
            logs.append(open(custody / (label + ".log"), "wb"))
        output["engineCandidate"] = {"name": name, "image": image, "context": prereq["dockerContext"]}
        ops.container_identity_pending = True
        persist()
        cid = c.command("engine-create", [*prereq["dockerPrefix"], "create", "--pull=never",
            "--name", name, "--network", "none", "--label", "cvf.owned=" + namespace.name,
            "--mount", f"type=bind,src={engine},dst=/engine,readonly", "--mount", f"type=bind,src={store.parent},dst=/data",
            "-w", "/engine", "-e", "CVF_GOVERNANCE_LEDGER_PATH=/data/proof.sqlite", image,
            "python", "-m", "uvicorn", "api.server:app", "--host", "127.0.0.1", "--port", "8100"], timeout=30).strip()
        if not re.fullmatch(r"[a-f0-9]{64}", cid):
            raise RuntimeError("malformed owned container ID")
        ops.container, ops.container_identity = cid, [cid, image, "/" + name]
        inspect = c.command("engine-identity", [*prereq["dockerPrefix"], "inspect", cid], parse=lambda raw: json.loads(raw)[0])
        if (inspect["Image"] != image or inspect["Name"] != "/" + name or inspect["HostConfig"]["NetworkMode"] != "none"
                or inspect["HostConfig"]["PortBindings"] or set(inspect["NetworkSettings"]["Networks"]) != {"none"}
                or {m["Destination"]: m["RW"] for m in inspect["Mounts"]} != {"/engine": False, "/data": True}):
            raise RuntimeError("engine identity, network or mounts not admitted")
        output["engineIdentity"] = {"id": cid, "image": image, "name": name, "networkMode": "none", "portBindings": None,
            "mounts": [{"source": m["Source"], "destination": m["Destination"], "rw": m["RW"]} for m in inspect["Mounts"]]}
        ops.container_identity_pending = False
        persist()  # exact container identity exists in custody before its first start
        ops.launch([*prereq["dockerPrefix"], "start", "-a", cid], cwd=namespace, env=env, stdout=logs[0])
        E.poll(c, budget, "engine", lambda: P.engine_http(c, prereq["dockerPrefix"], cid, "GET", "/api/v1/health")[0] == 200, 4, .5)
        network_probe = c.command("engine-network-proof", [*prereq["dockerPrefix"], "exec", cid, "python", "-c",
            "import socket;print(','.join(n for _,n in socket.if_nameindex()))\ntry:socket.create_connection(('1.1.1.1',53),1);print('OPEN')\nexcept OSError:print('BLOCKED')"], timeout=5).split()
        if network_probe != ["lo", "BLOCKED"]:
            raise RuntimeError("engine socket isolation proof failed")
        output["engineNetworkProbe"] = network_probe
        if P.read_rows(store) or json.loads(events.read_text(encoding="utf-8")) != []:
            raise RuntimeError("owned stores did not begin empty")
        reservations[1].close()
        proxy = Proxy(proxy_port, c, prereq["dockerPrefix"], cid, cap)
        thread = threading.Thread(target=proxy.serve_forever, daemon=True)
        thread.start()
        guard = P.ROOT / P.JOURNEY
        egress_log = custody / "egress.jsonl"
        env.update({"NODE_ENV": "development", "NODE_OPTIONS": f'--require "{guard}"', "CVF_HCR_EGRESS_LOG": str(egress_log),
            "CVF_NCR_ALLOWED_PORTS": json.dumps(ops.ports), "NEXT_TELEMETRY_DISABLED": "1", "AUTH_URL": base, "NEXTAUTH_URL": base,
            "AUTH_SECRET": secrets.token_hex(24), "NEXTAUTH_SECRET": secrets.token_hex(24), "CVF_SERVICE_TOKEN": "synthetic-ncr-" + secrets.token_hex(24),
            "CVF_STORAGE_ADAPTER_TYPE": "file", "CVF_CONTROL_PLANE_EVENTS_PATH": str(events), "GOVERNANCE_ENGINE_ENABLED": "true",
            "GOVERNANCE_ENGINE_URL": f"http://127.0.0.1:{proxy_port}", "GOVERNANCE_ENGINE_TIMEOUT": "3000", "CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS": "10000"})
        reservations[0].close()
        web_process = ops.launch([prereq["tools"]["node"], str(modules / "next/dist/bin/next"), "dev", "--webpack", "-p", str(web_port), "-H", "127.0.0.1"], cwd=web, env=env, stdout=logs[1])

        def web_ready():
            if web_process.poll() is not None:
                raise E.Stop("owned Web exited before readiness")
            return c.op("web-ready", lambda wait: fetch(base + "/login", wait) == 200, 60)
        E.poll(c, budget, "web", web_ready, 6, 2)
        for route in ("/api/artifacts/export", "/api/governance/evaluate"):
            budget.debit("route")  # charged before the GET, including a failing one
            try:
                c.op("route-compile", lambda wait: urllib.request.urlopen(base + route, timeout=wait).close(), 90)
            except urllib.error.HTTPError as response:
                if response.code != 405:
                    raise RuntimeError("non-effectful route compilation GET did not return405")
        entries = P.egress(egress_log)
        if not any(e["event"] == "denied" and e["host"] == "egress-selftest.invalid" for e in entries):
            raise RuntimeError("Node egress guard not proven before login")
        listeners = ops.listeners()
        if {int(x["address"].rsplit(":", 1)[1]) for x in listeners} != set(ops.ports) or any(x["pid"] not in set(ops.members()) | {os.getpid()} or not x["address"].startswith("127.0.0.1:") for x in listeners):
            raise RuntimeError("owned loopback listener identity mismatch")
        output["listenerIdentity"] = listeners
        config = custody / "journey-input.json"
        # The child clock is advisory: limits derive from the parent's remainder and the child may only shorten its waits.
        config.write_text(json.dumps({"inputs": inputs, "cap": cap, "browserProfile": str(stage / "browser-profile"),
                                      **PR.child_limits(proto, int(time.time() * 1000), P.CLEANUP_SECONDS)}, ensure_ascii=True, indent=2), encoding="utf-8")
        helper = ops.launch([prereq["tools"]["node"], str(P.ROOT / P.ENTRY_CJS), str(modules), base,
            str(custody / "browser.json"), str(custody), "owned-profile", str(guard), str(config)], cwd=web, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        lines = queue.Queue()

        def reader():
            for line in helper.stdout:
                lines.put(line.strip())
            lines.put(None)
        reader_thread = threading.Thread(target=reader, daemon=True)
        reader_thread.start()
        while True:
            wait = proto.left(.5, work_only=True)
            if wait <= 0:
                raise E.Deadline("controller loop: work cutoff reached")
            try:
                line = lines.get(timeout=wait)
            except queue.Empty:
                continue
            if line is None:
                break
            proto.check()  # recheck WORK after the queue wait, before any line is processed, granted or answered
            logs[2].write((line + "\n").encode())
            if line.startswith("SNAPSHOT "):  # the child's diagnostic claim is compared against independently read bytes, never trusted
                claim[0] = line.split(" ", 1)[1]
                continue
            kind, arg, op_id, gate = PR.parse_request(line, proto.generation, seen)
            if kind == "EXPORT_GATE_OK":
                P.egress(egress_log, gate["external"])
                if gate["aiPosts"] or proxy.failure or gate["n"] != output["state"]["exports"] + 1 or gate["n"] > cap:
                    raise RuntimeError("export admission failed before click")
                if len(proxy.observed) != gate["n"] - 1 or len(P.read_rows(store)) != gate["n"] - 1:
                    raise RuntimeError("prior request/row checkpoint mismatch")
                output["state"]["exports"] += 1
            else:
                output["checkpoints"].append({"label": arg, "rows": P.row_view(store), "arrived": proxy.arrived, "attempts": proxy.attempts})
            send(PR.reply(kind, arg, proto.generation, op_id))
            persist()
        exit_code = c.op("helper-exit", lambda wait: helper.wait(timeout=wait), 5)
        browser = json.loads((custody / "browser.json").read_bytes())
        output["browser"], output["engineObservations"], output["finalRows"] = browser, proxy.observed, P.row_view(store)
        output["finalEgress"] = P.egress(egress_log, browser["external"])
        output["counters"] = {"exports": output["state"]["exports"], "evaluateArrivals": proxy.arrived, "evaluateAttempts": proxy.attempts, "completed": len(proxy.observed)}
        if E.completion(exit_code) != "SUCCESS" or browser["partial"] or proxy.failure or set(output["counters"].values()) != {cap}:
            raise RuntimeError("browser/engine flow incomplete or ambiguous")
        ids = [b["attemptId"] for b in browser["builds"]]
        if ids != [r["requestId"] for r in output["finalRows"]] or len(set(ids)) != cap:
            raise RuntimeError("request rows do not join current browser versions")
        incoming = [e for e in output["finalEgress"] if e["event"] == "evaluate-recipient"]
        for row, b, src in zip(P.read_rows(store), browser["builds"], inputs):
            observed = proxy.observed[b["attemptId"]]
            request, data = observed["request"], observed["response"]["data"]
            P.check_row(row, b["attemptId"], data)  # real event.decision.final_decision schema; request_summary join
            expected = P.excerpt(src["sourceContent"])
            matches = [e for e in incoming if e["body"].get("request_id") == b["attemptId"]]
            if (len(matches) != 1 or not matches[0]["serviceTokenPresent"] or matches[0]["cookiePresent"]
                    or matches[0]["body"]["payload"]["content"] != expected or request["payload"]["content"] != expected
                    or data["report"]["request_summary"] != {"request_id": b["attemptId"], "artifact_id": b["receiptAnchor"]}
                    or data["execution_record"]["ledger_attached"] is not True):
                raise RuntimeError("recipient excerpt/request/artifact association failed")
        if P.v1_changed(output["checkpoints"], output["finalRows"]):
            raise RuntimeError("v1 row changed at observed checkpoints")
        (custody / "sql-rows.json").write_text(json.dumps(P.read_rows(store), indent=2), encoding="utf-8")
    except Exception as error:
        failures.append(E.safe(error))
    finally:
        proto.close("RUN_END")  # the irreversible fence precedes every shutdown, join and listener close

        def join(t):
            t.join(timeout=proto.left(3))
            if t.is_alive():
                raise RuntimeError("owned thread still alive")
        before = [("proxy-shutdown", proxy.shutdown)] if proxy and thread and thread.is_alive() else []
        before += [("proxy-close", proxy.server_close)] if proxy else []
        before += [("proxy-join", lambda: join(thread))] if thread else []
        before += [(f"reservation-{i}", r.close) for i, r in enumerate(reservations)]
        after = [("reader-join", lambda: join(reader_thread))] if reader_thread else []
        after += [(f"log-{i}", log.close) for i, log in enumerate(logs)]
        terminal = E.finalize(ops, failures, c, stage=stage, before=before, after=after, child_required=True,
                              child=child_probe(helper, custody, proto, claim) if helper else None,
                              persist=(custody / "terminal-evidence.json").write_bytes, read_back=(custody / "terminal-evidence.json").read_bytes)
        output.update(terminal=terminal, elapsedSeconds=round(time.monotonic() - started, 3), ok=not failures and terminal["accepted"])
        try:
            persist()
        except OSError as error:  # the immutable terminal evidence above is the authority; this convenience copy may fail alone
            output["runnerResultPersistence"] = "FAILED: " + type(error).__name__
    return output


def cli():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owned-profile-root", required=True)
    parser.add_argument("--engine-docker-image", required=True)
    parser.add_argument("--owned-profile-input", help="Local reviewer own synthetic JSON input array; no old grant")
    parser.add_argument("--owned-profile-cap", type=int, choices=(1, 2), default=2)
    parser.add_argument("--owned-profile-controls", required=True)
    parser.add_argument("--owned-profile-controls-sha256", required=True, help="separately frozen digest of the receipt bytes' canonical form")
    args = parser.parse_args()
    inputs = json.loads(Path(args.owned_profile_input).read_text(encoding="utf-8")) if args.owned_profile_input else None
    outcome = run(args.owned_profile_root, args.engine_docker_image, inputs=inputs, cap=args.owned_profile_cap,
                  controls_receipt=args.owned_profile_controls, controls_digest=args.owned_profile_controls_sha256)
    print(json.dumps(E.safe(outcome), indent=2))
    return 0 if outcome["ok"] else 1
