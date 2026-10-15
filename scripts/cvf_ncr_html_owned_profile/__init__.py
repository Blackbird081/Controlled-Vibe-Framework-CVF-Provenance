"""Finite, opt-in owned synthetic HTML invocation; legacy branches are not called."""
from __future__ import annotations

import argparse
import json
import os
import queue
import secrets
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

from . import profile as P
from .lifecycle import Collector, Native, finalize, no_reparse


def run(namespace, image, *, inputs=None, cap=2, controls_receipt=None):
    started, failures = time.monotonic(), []
    deadline = started + 900
    namespace = Path(namespace).absolute()
    no_reparse(namespace.parent)
    if namespace.exists() or namespace.resolve().is_relative_to(P.ROOT) or not namespace.parent.is_dir():
        raise RuntimeError("a fresh namespace outside provenance is required")
    sources = P.admit_sources()
    control = json.loads(Path(controls_receipt).read_text(encoding="utf-8"))
    worker_controls = (cap == 2 and control.get("passed") == 9 and control.get("substituteStarts", 100) <= 27
                       and control.get("testSourceSha256") == P.sha((P.ROOT / P.OUTPUTS[5]).read_bytes()))
    local_controls = (cap == 1 and inputs is not None and control.get("passed") == 6 and control.get("substituteStarts", 100) <= 18
                      and control.get("actor") == "LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER"
                      and control.get("oracleSha256") == P.sha(Path(control["oraclePath"]).read_bytes()))
    if not (worker_controls or local_controls):
        raise RuntimeError("current actual actor-owned inert collector controls are required before product startup")
    inputs = P.fixtures() if inputs is None else inputs
    if cap not in (1, 2) or len(inputs) != cap:
        raise RuntimeError("finite actor export/evaluate cap mismatch")
    namespace.mkdir()
    custody, stage = namespace / "custody", namespace / "source"
    custody.mkdir()
    (namespace / "owner.json").write_text(json.dumps({"owner": "Local-reviewer-after-worker", "nonce": secrets.token_hex(16),
        "namespace": str(namespace.resolve()), "source": sources, "profile": "NCR_HTML_OWNED_SYNTHETIC_FRESH_SOURCE_V1"}, indent=2), encoding="utf-8")
    c, ops, proxy, thread = Collector(custody), None, None, None
    c.deadline = deadline
    logs, reservations, helper = [], [], None
    output = {"schemaVersion": "cvf.ncrHtmlOwnedProfile.v1", "namespace": str(namespace), "sources": sources,
              "caps": {"exports": cap, "evaluates": cap, "readinessGets": 12, "runtimeSeconds": 900, "cleanupSeconds": 120},
              "state": {"exports": 0, "readinessGets": 0}, "checkpoints": [], "failures": failures,
              "providerStarts": 0, "actualDataConfigStoreReads": 0, "retentionSeconds": None}
    def persist():
        (custody / "runner-result.json").write_text(json.dumps(output, indent=2), encoding="utf-8")
    try:
        prereq = P.prerequisites(c, image)
        output["prerequisites"] = prereq
        ops = Native(c, prereq["dockerPrefix"], stage, namespace)
        output["controllerIdentity"] = ops.identity(os.getpid())
        manifest = P.stage_source(stage)
        (custody / "staged-source-manifest.json").write_text(json.dumps(manifest, sort_keys=True, indent=2), encoding="utf-8")
        output["staging"] = {"fileCount": len(manifest), "manifestSha256": P.sha((custody / "staged-source-manifest.json").read_bytes()),
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
        safe_env = dict(env)
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
        if not __import__("re").fullmatch(r"[a-f0-9]{64}", cid):
            raise RuntimeError("malformed owned container ID")
        ops.container, ops.container_identity = cid, [cid, image, "/" + name]
        inspect = json.loads(c.command("engine-identity", [*prereq["dockerPrefix"], "inspect", cid]))[0]
        if (inspect["Image"] != image or inspect["Name"] != "/" + name or inspect["HostConfig"]["NetworkMode"] != "none"
                or inspect["HostConfig"]["PortBindings"] or set(inspect["NetworkSettings"]["Networks"]) != {"none"}
                or {m["Destination"]: m["RW"] for m in inspect["Mounts"]} != {"/engine": False, "/data": True}):
            raise RuntimeError("engine identity, network or mounts not admitted")
        output["engineIdentity"] = {"id": cid, "image": image, "name": name, "networkMode": "none", "portBindings": None,
            "mounts": [{"source": m["Source"], "destination": m["Destination"], "rw": m["RW"]} for m in inspect["Mounts"]]}
        ops.container_identity_pending = False
        persist()  # exact container identity exists in custody before its first start
        engine_process = ops.launch([*prereq["dockerPrefix"], "start", "-a", cid], cwd=namespace, env=env, stdout=logs[0])
        for _ in range(6):
            output["state"]["readinessGets"] += 1
            try:
                if P.engine_http(c, prereq["dockerPrefix"], cid, "GET", "/api/v1/health")[0] == 200:
                    break
            except (RuntimeError, ValueError):
                time.sleep(.5)
        else:
            raise RuntimeError("engine not healthy within charged readiness budget")
        network_probe = c.command("engine-network-proof", [*prereq["dockerPrefix"], "exec", cid, "python", "-c",
            "import socket;print(','.join(n for _,n in socket.if_nameindex()))\ntry:socket.create_connection(('1.1.1.1',53),1);print('OPEN')\nexcept OSError:print('BLOCKED')"], timeout=5).split()
        if network_probe != ["lo", "BLOCKED"]:
            raise RuntimeError("engine socket isolation proof failed")
        output["engineNetworkProbe"] = network_probe
        if P.read_rows(store) or json.loads(events.read_text(encoding="utf-8")) != []:
            raise RuntimeError("owned stores did not begin empty")
        reservations[1].close()
        proxy = P.Proxy(proxy_port, c, prereq["dockerPrefix"], cid, cap)
        thread = threading.Thread(target=proxy.serve_forever, daemon=True)
        thread.start()
        guard = P.ROOT / "scripts/cvf_ncr_html_owned_profile/journey.cjs"
        egress_log = custody / "egress.jsonl"
        env.update({"NODE_ENV": "development", "NODE_OPTIONS": f'--require "{guard}"', "CVF_HCR_EGRESS_LOG": str(egress_log),
            "CVF_NCR_ALLOWED_PORTS": json.dumps(ops.ports), "NEXT_TELEMETRY_DISABLED": "1", "AUTH_URL": base, "NEXTAUTH_URL": base,
            "AUTH_SECRET": secrets.token_hex(24), "NEXTAUTH_SECRET": secrets.token_hex(24), "CVF_SERVICE_TOKEN": "synthetic-ncr-" + secrets.token_hex(24),
            "CVF_STORAGE_ADAPTER_TYPE": "file", "CVF_CONTROL_PLANE_EVENTS_PATH": str(events), "GOVERNANCE_ENGINE_ENABLED": "true",
            "GOVERNANCE_ENGINE_URL": f"http://127.0.0.1:{proxy_port}", "GOVERNANCE_ENGINE_TIMEOUT": "3000", "CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS": "10000"})
        reservations[0].close()
        web_process = ops.launch([prereq["tools"]["node"], str(modules / "next/dist/bin/next"), "dev", "--webpack", "-p", str(web_port), "-H", "127.0.0.1"], cwd=web, env=env, stdout=logs[1])
        for _ in range(6):
            output["state"]["readinessGets"] += 1
            try:
                with urllib.request.urlopen(base + "/login", timeout=c.remaining(60)) as response:
                    if response.status == 200:
                        break
            except (OSError, urllib.error.URLError):
                if web_process.poll() is not None:
                    raise RuntimeError("owned Web exited before readiness")
                time.sleep(2)
        else:
            raise RuntimeError("Web readiness budget exhausted")
        for route in ("/api/artifacts/export", "/api/governance/evaluate"):
            if output["state"]["readinessGets"] >= 12:
                raise RuntimeError("no readiness GET budget for route compilation")
            output["state"]["readinessGets"] += 1
            try:
                urllib.request.urlopen(base + route, timeout=c.remaining(90)).close()
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
        config.write_text(json.dumps({"inputs": inputs, "cap": cap, "browserProfile": str(stage / "browser-profile")}, ensure_ascii=True, indent=2), encoding="utf-8")
        helper = ops.launch([prereq["tools"]["node"], str(P.ROOT / P.OUTPUTS[1]), str(modules), base,
            str(custody / "browser.json"), str(custody), "owned-profile", str(guard), str(config)], cwd=web, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        lines = queue.Queue()
        def reader():
            for line in helper.stdout:
                lines.put(line.strip())
            lines.put(None)
        threading.Thread(target=reader, daemon=True).start()
        while time.monotonic() < deadline:
            try:
                line = lines.get(timeout=.5)
            except queue.Empty:
                continue
            if line is None:
                break
            logs[2].write((line + "\n").encode())
            if line.startswith("EXPORT_GATE_REQUEST "):
                gate = json.loads(line.split(" ", 1)[1])
                P.egress(egress_log, gate["external"])
                if gate["aiPosts"] or proxy.failure or gate["n"] != output["state"]["exports"] + 1 or gate["n"] > cap:
                    raise RuntimeError("export admission failed before click")
                if len(proxy.observed) != gate["n"] - 1 or len(P.read_rows(store)) != gate["n"] - 1:
                    raise RuntimeError("prior request/row checkpoint mismatch")
                output["state"]["exports"] += 1
                reply = f"EXPORT_GATE_OK {gate['n']}"
            elif line.startswith("CHECKPOINT "):
                label = line.split(" ", 1)[1]
                output["checkpoints"].append({"label": label, "rows": P.row_view(store), "arrived": proxy.arrived, "attempts": proxy.attempts})
                reply = "CHECKPOINT_OK " + label
            else:
                raise RuntimeError("unknown browser controller output")
            helper.stdin.write(reply + "\n")
            helper.stdin.flush()
            persist()
        else:
            raise TimeoutError("runtime deadline exhausted")
        helper.wait(timeout=5)
        browser = json.loads((custody / "browser.json").read_text(encoding="utf-8"))
        output["browser"], output["engineObservations"], output["finalRows"] = browser, proxy.observed, P.row_view(store)
        output["finalEgress"] = P.egress(egress_log, browser["external"])
        output["counters"] = {"exports": output["state"]["exports"], "evaluateArrivals": proxy.arrived, "evaluateAttempts": proxy.attempts, "completed": len(proxy.observed)}
        if helper.returncode or browser["partial"] or proxy.failure or set(output["counters"].values()) != {cap}:
            raise RuntimeError("browser/engine flow incomplete or ambiguous")
        ids = [b["attemptId"] for b in browser["builds"]]
        if ids != [r["requestId"] for r in output["finalRows"]] or len(set(ids)) != cap:
            raise RuntimeError("request rows do not join current browser versions")
        incoming = [e for e in output["finalEgress"] if e["event"] == "evaluate-recipient"]
        for b, src in zip(browser["builds"], inputs):
            observed = proxy.observed[b["attemptId"]]
            request, data = observed["request"], observed["response"]["data"]
            excerpt = src["sourceContent"].encode("utf-16-le")[:1000].decode("utf-16-le")
            matches = [e for e in incoming if e["body"].get("request_id") == b["attemptId"]]
            if (len(matches) != 1 or not matches[0]["serviceTokenPresent"] or matches[0]["cookiePresent"]
                    or matches[0]["body"]["payload"]["content"] != excerpt or request["payload"]["content"] != excerpt
                    or data["report"]["request_summary"] != {"request_id": b["attemptId"], "artifact_id": b["receiptAnchor"]}
                    or data["execution_record"]["ledger_attached"] is not True):
                raise RuntimeError("recipient excerpt/request/artifact association failed")
        if cap == 2 and any(cp["rows"][0] != output["finalRows"][0] for cp in output["checkpoints"] if cp["rows"]):
            raise RuntimeError("v1 row changed at observed checkpoints")
        (custody / "sql-rows.json").write_text(json.dumps(P.read_rows(store), indent=2), encoding="utf-8")
    except Exception as error:
        failures.append(f"{type(error).__name__}: {str(error)[:600]}")
    finally:
        for reservation in reservations:
            reservation.close()
        if proxy:
            proxy.shutdown()
            proxy.server_close()
        if thread:
            thread.join(timeout=3)
        c.deadline = min(time.monotonic() + 120, deadline + 120)
        output["cleanup"] = finalize(ops, failures, seconds=max(0, c.deadline - time.monotonic())) if ops else {"disposition": "NOT_STARTED_NO_NATIVE_RESOURCES", "stageRemoved": not stage.exists()}
        for log in logs:
            log.close()
        output["elapsedSeconds"] = round(time.monotonic() - started, 3)
        output["ok"] = not failures and output["cleanup"]["disposition"] == "ACCEPTED_CLEANUP"
        persist()
    return output


def cli():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owned-profile-root", required=True)
    parser.add_argument("--engine-docker-image", required=True)
    parser.add_argument("--owned-profile-input", help="Local reviewer own synthetic JSON input array; no old grant")
    parser.add_argument("--owned-profile-cap", type=int, choices=(1, 2), default=2)
    parser.add_argument("--owned-profile-controls", required=True)
    args = parser.parse_args()
    inputs = json.loads(Path(args.owned_profile_input).read_text(encoding="utf-8")) if args.owned_profile_input else None
    outcome = run(args.owned_profile_root, args.engine_docker_image, inputs=inputs, cap=args.owned_profile_cap, controls_receipt=args.owned_profile_controls)
    print(json.dumps(outcome, indent=2))
    return 0 if outcome["ok"] else 1
