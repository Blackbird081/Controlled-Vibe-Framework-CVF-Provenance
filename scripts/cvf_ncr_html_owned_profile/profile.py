"""Fresh source admission, case-specific control receipts, bounded real-engine transport, and exact receipt joins."""
# Text Encoding Exception: exact Vietnamese SPEC replacement strings preserve the approved synthetic fixture.
from __future__ import annotations

import json
import os
import re
import shutil
import sqlite3
import subprocess
import unicodedata
from contextlib import closing
from pathlib import Path

from .execution import UNKNOWN, dumps, sha
from .lifecycle import no_reparse

ROOT = Path(__file__).resolve().parents[2]
WEB = Path("EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web")
ENGINE = Path("EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core")
ENTRY_PY, ENTRY_CJS = "scripts/probe_cvf_q001_synthetic_system_chain.py", "scripts/probe_cvf_w05_browser_chain.cjs"  # read-only inputs
BASE_COMMIT = "0850546dea01b0f15586132549e4330a1af25c72"  # immutable pre-build entrypoint commit; never moving HEAD
BASE_BLOBS = {ENTRY_PY: "26b34890e3031f5b13ca4965585adbdf14a483aefe246834d3848cb165c3fe9d",  # sha256 of `git show BASE_COMMIT:<path>`
              ENTRY_CJS: "2f0981b2356a51a85f34d3d6ed94a0d0a0606c48d306888711876a5c2b225dec"}
WO = "docs/baselines/CVF_GC018_NCR_HTML_DIRECT_LOCAL_REPAIR_2026-10-16.md"  # legacy variable: direct Local authorization, not a dispatch order
PINS = "docs/reviews/evidence/ncr-html-direct-local-repair-pins-20261016.json"
PAIR = (WO, "docs/baselines/CVF_GC018_NCR_HTML_SEMANTIC_STATE_MACHINE_DESIGN_2026-10-15.md",
        "docs/reviews/CVF_NCR_HTML_ROOT_SEMANTIC_R5_COMPLETION_2026-10-15.md",
        "docs/reviews/evidence/ncr-html-root-semantic-local-r5-20261015.json")
REGISTRY = ("governance/toolkit/03_CONTROL/CVF_AGENT_REGISTRY.md",
            "governance/toolkit/04_TESTING/CVF_SELF_UAT_DECISION_LOG.md",
            "docs/reference/CVF_GOVERNANCE_STATE_REGISTRY.json")
HELPERS = tuple("scripts/cvf_ncr_html_owned_profile/" + n for n in (
    "__init__.py", "lifecycle.py", "profile.py", "test_control.py", "journey.cjs", "journey.test.cjs",
    "execution.py", "test_execution.py", "protocol.py", "test_protocol.py"))
INIT, LIFECYCLE, PROFILE, TEST_CONTROL, JOURNEY, JOURNEY_TEST, EXECUTION, TEST_EXECUTION, PROTOCOL, TEST_PROTOCOL = HELPERS
PRODUCTION = (INIT, LIFECYCLE, PROFILE, EXECUTION, PROTOCOL, JOURNEY)  # control receipts bind all six production owners
ORACLES = (TEST_CONTROL, TEST_EXECUTION, TEST_PROTOCOL, JOURNEY_TEST)  # ...and the four oracle sources
OUTPUTS = (*HELPERS, "docs/assessments/CVF_NCR_HTML_DIRECT_LOCAL_REPAIR_DISPOSITION_2026-10-16.md",
           "docs/reviews/evidence/ncr-html-direct-local-repair-20261016.json")  # source10 plus direct disposition/evidence
WORK_SECONDS, CLEANUP_SECONDS = 900, 120
SAFE_ENV = {"PATH", "SYSTEMROOT", "SYSTEMDRIVE", "TEMP", "TMP", "USERPROFILE", "HOMEDRIVE", "HOMEPATH",
            "APPDATA", "LOCALAPPDATA", "COMSPEC", "PATHEXT", "WINDIR", "PROCESSOR_ARCHITECTURE", "NUMBER_OF_PROCESSORS", "OS", "USERNAME"}
PASSIVE = {"fonts.googleapis.com", "fonts.gstatic.com", "registry.npmjs.org", "egress-selftest.invalid"}
EXEC = ("import http.client,json,sys\nx=json.load(sys.stdin);c=http.client.HTTPConnection('127.0.0.1',8100,timeout=2)\n"
        "c.request(x['method'],x['path'],json.dumps(x['body']) if x.get('body') is not None else None,{'Content-Type':'application/json'})\n"
        "r=c.getresponse();print(json.dumps({'status':r.status,'body':r.read().decode()}))\n")
KEYS = ("title", "sourcePath", "sourceContent", "memoryClass", "status", "claimBoundary", "receiptAnchor")
KINDS = ("taskkill", "tasklist", "docker-ps")
CASES = ("taskkill-nonzero", "tasklist-nonzero", "docker-ps-nonzero", "timeout", "tasklist-malformed",
         "identity-mismatch", "still-live", "unsafe-path", "docker-ps-malformed")
# case -> (failing action label, command failure class or None, process/container/descendant query verdicts, expected command kinds)
MATRIX = {"taskkill-nonzero": ("taskkill", "NONZERO_EXIT", ("ABSENT", "ABSENT", "ABSENT"), KINDS),
          "tasklist-nonzero": ("tasklist", "NONZERO_EXIT", ("UNKNOWN", "ABSENT", "ABSENT"), KINDS),
          "docker-ps-nonzero": ("docker-ps", "NONZERO_EXIT", ("ABSENT", "UNKNOWN", "ABSENT"), KINDS),
          "timeout": ("taskkill", "TIMEOUT", ("ABSENT", "ABSENT", "ABSENT"), KINDS),
          "tasklist-malformed": ("tasklist", "PARSE", ("UNKNOWN", "ABSENT", "ABSENT"), KINDS),
          "identity-mismatch": ("identity", None, ("ABSENT", "ABSENT", "LIVE"), KINDS[1:]),
          "still-live": (None, None, ("LIVE", "ABSENT", "LIVE"), KINDS),
          "unsafe-path": ("disposal-target", None, ("ABSENT", "ABSENT", "ABSENT"), KINDS),
          "docker-ps-malformed": ("docker-ps", "PARSE", ("ABSENT", "UNKNOWN", "ABSENT"), KINDS)}
CONTROL_KEYS = {"schema", "actor", "invocation", "runner", "production", "oracles", "passed", "substituteStarts", "cases"}
CASE_KEYS = {"case", "invocation", "commands", "commandsSha256", "substituteStarts", "terminal", "effects"}
EFFECTS = ("productStarts", "engineStarts", "providerStarts", "nativeChildren", "networkCalls")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, timeout=30)


def admit_sources():
    """Four read-only Git commands; current Local authorization/contract/evidence pins must match. Runtime needs separate admission."""
    pins = json.loads((ROOT / PINS).read_text(encoding="utf-8"))["sourcePins"]
    if any(p not in pins for p in PAIR):
        raise RuntimeError("release pair/grant/companion pin missing")
    immutable = {p: h for p, h in pins.items() if p not in OUTPUTS}
    if any(sha((ROOT / p).read_bytes()) != h for p, h in immutable.items()):
        raise RuntimeError("immutable release/source pin drift")
    dirty = set(git("diff", "--name-only", "HEAD").decode().splitlines()) | set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    if dirty - set(OUTPUTS) or git("diff", "--cached", "--name-only").strip():
        raise RuntimeError("exclusive worker lane drift or staged paths")
    helpers = {p: sha((ROOT / p).read_bytes()) for p in HELPERS}
    return {"executionBaseHead": git("rev-parse", "HEAD").decode().strip(), "immutablePins": immutable, "implementedHelpers": helpers}


def validate_inputs(inputs, cap):
    """Pure exact-shape admission before any namespace/child; mirrors journey.validateInputs."""
    if type(cap) is not int or cap not in (1, 2) or type(inputs) is not list or len(inputs) != cap:
        raise ValueError("finite actor cap/input count mismatch")
    for x in inputs:
        if type(x) is not dict or set(x) != set(KEYS) or any(type(x[k]) is not str or not x[k] or unicodedata.normalize("NFC", x[k]) != x[k] for k in KEYS):
            raise ValueError("input must be exactly seven non-empty NFC strings")
        path = x["sourcePath"]
        if (x["memoryClass"] != "FULL_RECORD" or not re.fullmatch(r"synthetic/[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*", path)
                or {".", ".."} & set(path.split("/")) or not re.fullmatch(r"[a-zA-Z0-9 -]+", x["title"])):
            raise ValueError("input is not a synthetic FULL_RECORD with a safe title/path")
    if len({x["receiptAnchor"] for x in inputs}) != cap:
        raise ValueError("receipt anchors must be distinct")
    return inputs


def control_binding():
    return {"production": {p: sha((ROOT / p).read_bytes()) for p in PRODUCTION}, "oracles": {p: sha((ROOT / p).read_bytes()) for p in ORACLES}}


def case_issue(x, name, invocation):
    """One inert case against its own expected failure class, query verdicts, command kinds and zero-effect counters."""
    label, klass, (process, container, descendant), kinds = MATRIX[name]
    if type(x) is not dict or set(x) != CASE_KEYS or x["case"] != name or x["invocation"] != invocation:
        return "case identity/shape"
    commands, term = x["commands"], x["terminal"]
    if (type(commands) is not list or type(x["substituteStarts"]) is not int or x["substituteStarts"] != len(kinds)
            or tuple(c.get("kind") if type(c) is dict else None for c in commands) != kinds or x["commandsSha256"] != sha(dumps(commands))):
        return "raw command receipts"
    failing = [(c["kind"], c["failureClass"]) for c in commands if c["failureClass"]]
    if failing != ([] if klass is None else [(label, klass)]) or any(c["state"] != "FINISHED" for c in commands):
        return "command failure classes"
    ev = term.get("evidence") if type(term) is dict else None
    if type(ev) is not dict or term.get("evidenceSha256") != sha(dumps(ev)) or type(ev.get("errors")) is not list:
        return "terminal evidence digest"
    errors = ev["errors"]
    if not (ev.get("processQuery") == process and ev.get("containerQuery") == container and ev.get("descendantQuery") == descendant
            and ev.get("listenerQuery") == "ABSENT" and len(errors) == (0 if label is None else 1) and (label is None or errors[0].startswith(label + ":"))
            and ev.get("preAckDisposition") == UNKNOWN and ev.get("stageRetained") is True and ev.get("primaryFailures") == []
            and ev.get("uncertainOperations") == [] and term.get("accepted") is False and term.get("disposalEligible") is False
            and term.get("actualDisposal") == "NOT_ATTEMPTED"):
        return "expected failure/query/retention state"
    effects = x["effects"]
    if type(effects) is not dict or set(effects) != set(EFFECTS) or any(type(effects[k]) is not int or effects[k] != 0 for k in EFFECTS):
        return "forbidden effects"
    return None


def control_issue(control, cap, frozen_digest):
    """Closed-shape, case-specific, hash-joined receipt admission. Declared joins only: editable bytes are not proof of execution."""
    if cap != 2:
        return "Local collector receipt admission is fail-closed until a future exact case matrix and actual controls exist"
    if type(control) is not dict or set(control) != CONTROL_KEYS or control["schema"] != "cvf.ncrHtmlInertControls@3":
        return "receipt shape"
    if control["actor"] != "IMPLEMENTATION_WORKER" or type(control["invocation"]) is not str or not control["invocation"]:
        return "actor/invocation"
    if control["runner"] != "SUBPROCESS":
        return "receipt was not produced by real inert substitute children"
    if {k: control[k] for k in ("production", "oracles")} != control_binding():
        return "stale production/oracle hashes"
    cases = control["cases"]
    if type(cases) is not list or [x.get("case") if type(x) is dict else None for x in cases] != list(CASES):
        return "duplicate, missing or reordered case matrix"
    for name, x in zip(CASES, cases):
        issue = case_issue(x, name, control["invocation"])
        if issue:
            return f"{name}: {issue}"
    total = sum(x["substituteStarts"] for x in cases)
    if type(control["passed"]) is not int or control["passed"] != len(CASES) or type(control["substituteStarts"]) is not int or control["substituteStarts"] != total or total > 27:
        return "aggregate counts do not reconcile"
    if type(frozen_digest) is not str or frozen_digest != sha(dumps(control)):
        return "receipt digest differs from the separately frozen digest"
    return None


def admit_controls(control, cap, frozen_digest):
    try:
        issue = control_issue(control, cap, frozen_digest)
    except (KeyError, TypeError, AttributeError, ValueError) as error:
        issue = f"malformed receipt ({type(error).__name__})"
    if issue:
        raise RuntimeError("current actual actor-owned inert collector controls are required before product startup: " + issue)
    return control["actor"]


def excerpt(text, units=500):
    """Renderer semantics: JS slice(0, 500) counts UTF-16 code units and may split a surrogate pair."""
    return text.encode("utf-16-le", "surrogatepass")[:units * 2].decode("utf-16-le", "surrogatepass")


def check_row(row, request_id, data):
    """Join one SQL ledger block to the engine response using the real event.decision.final_decision schema."""
    try:
        ordinal, rid, raw, digest = row
        event = json.loads(raw)["event"]
        decision = event["decision"]["final_decision"]
        ok = (type(ordinal) is int and rid == request_id and event["request_id"] == request_id and "final_decision" not in event
              and type(event["timestamp"]) is str and bool(event["timestamp"]) and type(decision) is str and bool(decision)
              and decision == data["execution_record"]["final_decision"] and data["report"]["request_summary"]["request_id"] == request_id
              and type(digest) is str and bool(digest))
    except (TypeError, ValueError, KeyError, AttributeError):
        ok = False
    if not ok:
        raise RuntimeError("ledger block/response join malformed or mismatched")


def v1_changed(checkpoints, final_rows):
    return any(cp["rows"] and cp["rows"][0] != final_rows[0] for cp in checkpoints)


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
    info = c.command("docker-context-inspect", [paths["docker"], "context", "inspect", context], parse=lambda raw: json.loads(raw)[0])
    endpoint = info["Endpoints"]["docker"]["Host"]
    if not endpoint.startswith("npipe://") or any(k in os.environ for k in ("DOCKER_HOST", "DOCKER_CONTEXT")):
        raise RuntimeError("unknown or remote Docker context")
    prefix = [paths["docker"], "--context", context]
    c.command("docker-local-server", [*prefix, "version", "--format", "{{.Server.Os}}"])
    image_info = c.command("cached-image", [*prefix, "image", "inspect", image], parse=lambda raw: json.loads(raw)[0])
    if (image_info["Id"], image_info["Os"], image_info["Architecture"]) != (image, "linux", "amd64"):
        raise RuntimeError("cached image identity/platform mismatch")
    # One installed-browser module query per actor: Collector refuses a repeat, and no fallback or install follows a failure.
    exe = c.command("installed-browser-path", [paths["node"], "-e", "console.log(require(process.argv[1]).chromium.executablePath())", str(modules / "@playwright/test")], timeout=30).strip()
    if not Path(exe).is_file():
        raise RuntimeError("installed Chromium missing")
    return {"tools": paths, "modules": str(modules.resolve()), "dependencyAccess": "PRE_EXISTING_READ_ONLY_NOT_DISPOSABLE",
            "browserExecutable": exe, "dockerContext": context, "dockerEndpoint": endpoint, "image": image, "dockerPrefix": prefix}


def _reply(raw):
    reply = json.loads(raw)
    if type(reply["status"]) is not int or type(reply["body"]) is not str:
        raise ValueError("malformed engine reply")
    return reply["status"], reply["body"].encode()


def engine_http(c, prefix, container, method, path, body=None):
    return c.command("engine-" + method, [*prefix, "exec", "-i", container, "python", "-c", EXEC], timeout=5,
                     data=json.dumps({"method": method, "path": path, "body": body}), parse=_reply)


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
