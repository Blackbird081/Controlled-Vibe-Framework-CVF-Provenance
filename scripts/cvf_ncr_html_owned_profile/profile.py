"""Fresh source admission, bounded real-engine transport, and exact receipt joins."""
# Text Encoding Exception: exact Vietnamese SPEC replacement strings preserve the approved synthetic fixture.
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import socket
import sqlite3
import subprocess
import threading
import unicodedata
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from .lifecycle import no_reparse

ROOT = Path(__file__).resolve().parents[2]
WEB = Path("EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web")
ENGINE = Path("EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core")
WO = "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_INTEGRATED_ROOT_BUILD_RELEASE_2026-10-15.md"
PINS = "docs/reviews/evidence/ncr-html-root-build-release-local-20261015.json"
REGISTRY = ("governance/toolkit/03_CONTROL/CVF_AGENT_REGISTRY.md",
            "governance/toolkit/04_TESTING/CVF_SELF_UAT_DECISION_LOG.md",
            "docs/reference/CVF_GOVERNANCE_STATE_REGISTRY.json")
OUTPUTS = ("scripts/probe_cvf_q001_synthetic_system_chain.py", "scripts/probe_cvf_w05_browser_chain.cjs",
           *("scripts/cvf_ncr_html_owned_profile/" + n for n in ("__init__.py", "lifecycle.py", "profile.py", "test_control.py", "journey.cjs", "journey.test.cjs")),
           "docs/reviews/CVF_NCR_HTML_INTEGRATED_ROOT_BUILD_WORKER_RETURN_2026-10-15.md",
           "docs/reviews/evidence/ncr-html-integrated-root-build-worker-20261015.json")
SAFE_ENV = {"PATH", "SYSTEMROOT", "SYSTEMDRIVE", "TEMP", "TMP", "USERPROFILE", "HOMEDRIVE", "HOMEPATH",
            "APPDATA", "LOCALAPPDATA", "COMSPEC", "PATHEXT", "WINDIR", "PROCESSOR_ARCHITECTURE", "NUMBER_OF_PROCESSORS", "OS", "USERNAME"}
PASSIVE = {"fonts.googleapis.com", "fonts.gstatic.com", "registry.npmjs.org", "egress-selftest.invalid"}
EXEC = ("import http.client,json,sys\nx=json.load(sys.stdin);c=http.client.HTTPConnection('127.0.0.1',8100,timeout=2)\n"
        "c.request(x['method'],x['path'],json.dumps(x['body']) if x.get('body') is not None else None,{'Content-Type':'application/json'})\n"
        "r=c.getresponse();print(json.dumps({'status':r.status,'body':r.read().decode()}))\n")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, timeout=30)


def admit_sources():
    pins = json.loads((ROOT / PINS).read_text(encoding="utf-8"))["sourcePins"]
    immutable = {p: h for p, h in pins.items() if p not in OUTPUTS}
    if any(sha((ROOT / p).read_bytes()) != h for p, h in immutable.items()):
        raise RuntimeError("immutable release/source pin drift")
    dirty = set(git("diff", "--name-only", "HEAD").decode().splitlines()) | set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    if dirty - set(OUTPUTS) or git("diff", "--cached", "--name-only").strip():
        raise RuntimeError("exclusive worker lane drift or staged paths")
    helpers = {p: sha((ROOT / p).read_bytes()) for p in OUTPUTS[:8]}
    return {"executionBaseHead": git("rev-parse", "HEAD").decode().strip(), "immutablePins": immutable, "implementedHelpers": helpers}


def fixtures():
    spec = (ROOT / "docs/assessments/CVF_NCR_HTML_FRESH_PROFILE_USER_JOURNEY_SPEC_2026-10-14.md").read_text(encoding="utf-8")
    source = spec.split("```text\n", 1)[1].split("\n```", 1)[0]
    rows = dict(re.findall(r"^\| (title|sourcePath|memoryClass|status|receiptAnchor|claimBoundary) \| (.*?) \|$", spec, re.M))
    v1 = {**rows, "sourceContent": source}
    v2 = {**v1, "title": v1["title"].replace("v1", "v2"), "sourcePath": v1["sourcePath"].replace("v1", "v2"),
          "status": "Revised draft for review", "receiptAnchor": "onboarding-synth-v2",
          "sourceContent": source.replace("Review status: Draft for review", "Review status: Revised draft for review")
              .replace("ba việc", "bốn việc").replace("\n\n## Review Boundary", "\n- Báo cho người phụ trách biết mình đã đọc xong bản hướng dẫn này.\n\n## Review Boundary")}
    expected = ("a078550b8cf59759d4eb78413e019ab4f412c5f8fd885bbce5fdb7a721e7a7bd", "cf39b5355aab4603131a4468845881b5d5d9c2ca01ac96a967ff42b5124a1edd")
    if any(sha(v["sourceContent"].strip().encode()) != h or any(unicodedata.normalize("NFC", x) != x for x in v.values()) for v, h in zip((v1, v2), expected)):
        raise RuntimeError("canonical SPEC fixture mismatch")
    return [v1, v2]


def stage_source(stage):
    scopes = [WEB.as_posix(), ENGINE.parent.as_posix(), *REGISTRY]
    if git("diff", "HEAD", "--", *scopes).strip():
        raise RuntimeError("selected product source differs from Git pin")
    paths = git("ls-files", "-z", "--", *scopes).split(b"\0")
    manifest = {}
    for raw in paths:
        if not raw:
            continue
        rel = Path(os.fsdecode(raw))
        if any(x.startswith(".env") for x in rel.parts) or rel.name == "ledger_chain.json":
            continue
        src, dst = ROOT / rel, stage / rel
        for p in [src, *src.parents]:
            if p == ROOT.parent:
                break
            no_reparse(p)
        if not src.is_file() or not src.resolve().is_relative_to(ROOT):
            raise RuntimeError("unsafe or missing selected source")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        digest = sha(src.read_bytes())
        if sha(dst.read_bytes()) != digest:
            raise RuntimeError("staged bytes changed")
        manifest[rel.as_posix()] = digest
    if not manifest:
        raise RuntimeError("empty source manifest")
    return manifest


def prerequisites(c, image):
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", image or ""):
        raise RuntimeError("explicit immutable cached engine image required")
    paths = {n: shutil.which(n) for n in ("node", "docker", "git", "taskkill", "tasklist", "netstat")}
    modules = ROOT / WEB / "node_modules"
    for p in (modules / "next/dist/bin/next", modules / "@playwright/test/package.json"):
        if not p.is_file():
            raise RuntimeError("installed read-only dependency missing")
    if not all(paths.values()):
        raise RuntimeError("installed native prerequisite missing")
    context = c.command("docker-context", [paths["docker"], "context", "show"]).strip()
    info = json.loads(c.command("docker-context-inspect", [paths["docker"], "context", "inspect", context]))[0]
    endpoint = info["Endpoints"]["docker"]["Host"]
    if not endpoint.startswith("npipe://") or any(k in os.environ for k in ("DOCKER_HOST", "DOCKER_CONTEXT")):
        raise RuntimeError("unknown or remote Docker context")
    prefix = [paths["docker"], "--context", context]
    c.command("docker-local-server", [*prefix, "version", "--format", "{{.Server.Os}}"])
    image_info = json.loads(c.command("cached-image", [*prefix, "image", "inspect", image]))[0]
    if (image_info["Id"], image_info["Os"], image_info["Architecture"]) != (image, "linux", "amd64"):
        raise RuntimeError("cached image identity/platform mismatch")
    # An installed browser is required. No install/download operation exists here.
    exe = c.command("installed-browser-path", [paths["node"], "-e", "console.log(require(process.argv[1]).chromium.executablePath())", str(modules / "@playwright/test")]).strip()
    if not Path(exe).is_file():
        raise RuntimeError("installed Chromium missing")
    return {"tools": paths, "modules": str(modules.resolve()), "dependencyAccess": "PRE_EXISTING_READ_ONLY_NOT_DISPOSABLE",
            "browserExecutable": exe, "dockerContext": context, "dockerEndpoint": endpoint, "image": image, "dockerPrefix": prefix}


def engine_http(c, prefix, container, method, path, body=None):
    raw = c.command("engine-" + method, [*prefix, "exec", "-i", container, "python", "-c", EXEC],
                    timeout=5, data=json.dumps({"method": method, "path": path, "body": body}))
    reply = json.loads(raw)
    return reply["status"], reply["body"].encode()


def read_rows(store):
    if not store.is_file():
        return []
    with closing(sqlite3.connect(store.resolve().as_uri() + "?mode=ro", uri=True, timeout=1)) as conn:
        return conn.execute("SELECT ordinal,request_id,block_json,block_hash FROM blocks ORDER BY ordinal").fetchall()


def row_view(store):
    return [{"ordinal": r[0], "requestId": r[1], "blockJsonSha256": sha(r[2].encode()), "blockHash": r[3]} for r in read_rows(store)]


def egress(log, browser=()):
    entries = [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines()] if log.exists() else []
    denied = [x for x in entries if x["event"] == "denied"] + list(browser)
    if any(x["host"].lower() not in PASSIVE for x in denied):
        raise RuntimeError("unknown/provider egress attempt; no further effects")
    return entries


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
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            if (set(body) - {"request_id", "artifact_id", "payload", "cvf_phase", "cvf_risk_level", "skill_preflight"}
                    or body.get("cvf_phase") != "REVIEW" or body.get("cvf_risk_level") != "R0"):
                raise RuntimeError("unexpected engine recipient envelope")
            if "x-cvf-service-token" in self.headers or "cookie" in self.headers:
                raise RuntimeError("app authentication leaked to engine recipient")
            status, raw = engine_http(s.c, s.prefix, s.container, "POST", self.path, body)
            with s.lock:
                s.observed[body["request_id"]] = {"request": body, "status": status, "response": json.loads(raw),
                                                    "recipientExcerptSha256": sha(body["payload"]["content"].encode())}
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)
        except Exception as error:
            s.failure = f"engine hop failed/ambiguous: {type(error).__name__}: {str(error)[:100]}"
            self.close_connection = True
