"""Nine admitted inert failure classes run the actual terminal boundary; control admission, input pins and the legacy entry stay fail-closed."""
from __future__ import annotations

import ast
import copy
import functools
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cvf_ncr_html_owned_profile as H
from cvf_ncr_html_owned_profile import execution as E
from cvf_ncr_html_owned_profile import lifecycle as L
from cvf_ncr_html_owned_profile import profile as P

if {"CVF_NCR_ALLOWED_PORTS", "CVF_HCR_EGRESS_LOG"} & set(os.environ):
    raise RuntimeError("inherited network-guard activation is refused in the pure test environment")
INVOCATION = "worker-" + os.urandom(8).hex()
SCRATCH = P.ROOT / ".cvf/runtime/ncr-html-root-local-repair-20261016" / INVOCATION  # fresh per invocation; no prior receipts
RUNNER = "SUBPROCESS" if os.environ.get("CVF_LOCAL_REPAIR_SUBSTITUTE") == "subprocess" else "IN_PROCESS_FAKE"  # only the worker's final launch sets it
FIX, IMAGE = P.fixtures(), "sha256:" + "0" * 64
CHILD = re.compile(r"time\.sleep\((.*?)\);sys\.stdout\.write\((.*)\);sys\.exit\((\d+)\)$")


def in_process(argv, **kw):
    """Interprets the exact inert child program without starting a child (iteration and the Local reviewer start none)."""
    pause, out, code = CHILD.search(argv[-1]).groups()
    if float(pause) > kw["timeout"]:
        raise subprocess.TimeoutExpired(argv, kw["timeout"], output=b"", stderr=b"")
    return subprocess.CompletedProcess(argv, int(code), ast.literal_eval(out), "")


class SubstituteNative:
    """Only identity data are inert; the collector, its failure classes and the terminal boundary are the production ones."""
    container = "a" * 64

    def __init__(self, case, path, runner):
        self.case, self.stage, self.starts, self.closed = case, path / "source", 0, False

        def counted(argv, **kw):
            self.starts += 1
            return runner(argv, **kw)
        self.c = E.Collector(path, counted)
        self.stage.mkdir(parents=True)

    def command(self, kind, stdout, code=0, pause=0, parse=None):
        argv = [sys.executable, "-B", "-c", f"import time,sys;time.sleep({pause});sys.stdout.write({stdout!r});sys.exit({code})"]
        return self.c.command(kind, argv, timeout=.15 if pause else 2, parse=parse)

    def prepare_kill(self):
        if self.case == "identity-mismatch":
            raise RuntimeError("creation identity differs from recorded owner")
        return [{"pid": 43210, "creation100ns": 123, "image": "INERT_NO_PRODUCT"}]

    def kill(self, _identity):
        self.command("taskkill", "", 7 if self.case == "taskkill-nonzero" else 0, 1 if self.case == "timeout" else 0)

    def remove_container(self): pass  # no actual engine/container exists in any inert control

    def query_processes(self):
        raw = '"inert.exe","43210","Console","1","1 K"' if self.case == "still-live" else '"system.exe","4","Services","0","1 K"'
        return self.command("tasklist", "not CSV" if self.case == "tasklist-malformed" else raw, 9 if self.case == "tasklist-nonzero" else 0, parse=L.parse_tasklist)

    def query_containers(self):
        return self.command("docker-ps", "not-an-id" if self.case == "docker-ps-malformed" else "", 8 if self.case == "docker-ps-nonzero" else 0, parse=L.parse_docker_ids)

    def members(self): return [43210] if self.case in ("still-live", "identity-mismatch") else []

    def listeners(self): return []

    def verify_disposal_target(self):
        if self.case == "unsafe-path":
            L.check_disposable(self.stage, self.stage)  # wrong lexical/resolved parent: never eligible
        return True

    def close(self): self.closed = True


def run_case(case, runner, tag):
    root = SCRATCH / tag / case
    ops = SubstituteNative(case, root, runner)
    terminal = E.finalize(ops, [], ops.c)  # the same unconditional runtime boundary; no persistence, so no acceptance claim
    raw = (root / "commands.json").read_bytes()
    record = {"case": case, "invocation": INVOCATION, "commands": json.loads(raw), "commandsSha256": E.sha(raw), "substituteStarts": ops.starts,
              "terminal": terminal, "effects": dict.fromkeys(P.EFFECTS, 0)}
    (root / "result.json").write_bytes(E.dumps(record))
    return ops, terminal, record


def receipt_of(done, runner):
    return {"schema": "cvf.ncrHtmlInertControls@3", "actor": "IMPLEMENTATION_WORKER", "invocation": INVOCATION, "runner": runner, **P.control_binding(),
            "passed": len(done), "substituteStarts": sum(x["substituteStarts"] for x in done), "cases": done}


@pytest.mark.parametrize("case", P.CASES)
def test_actual_terminal_boundary_rejects_failed_native_control(case):
    ops, terminal, _ = run_case(case, subprocess.run if RUNNER == "SUBPROCESS" else in_process, "inert")
    ev = terminal["evidence"]
    assert terminal["accepted"] is False and terminal["disposalEligible"] is False and ev["preAckDisposition"] == E.UNKNOWN
    assert ops.closed and ops.stage.exists() and ev["stageRetained"] is True and terminal["actualDisposal"] == "NOT_ATTEMPTED"
    assert ev["errors"] or ev["processQuery"] == "LIVE"
    done = [json.loads(p.read_bytes()) for x in P.CASES if (p := SCRATCH / "inert" / x / "result.json").exists()]  # only this invocation's cases
    receipt = receipt_of(done, RUNNER)
    (SCRATCH / "inert-results.json").write_bytes(E.dumps(receipt))
    (SCRATCH / "inert-results.sha256").write_text(E.sha(E.dumps(receipt)), encoding="utf-8")  # frozen digest, kept apart from the receipt
    if RUNNER == "SUBPROCESS" and len(done) == len(P.CASES):  # the real-children receipt must pass the production parser exactly as written
        written = json.loads((SCRATCH / "inert-results.json").read_bytes())
        assert P.control_issue(written, 2, (SCRATCH / "inert-results.sha256").read_text(encoding="utf-8")) is None and written["substituteStarts"] <= 27


@functools.cache
def fixture_receipt():
    """Parser fixture only: nine in-process cases labelled as children. It never certifies execution or enables startup."""
    return receipt_of([run_case(case, in_process, "fixture")[2] for case in P.CASES], "SUBPROCESS")


def good(): return copy.deepcopy(fixture_receipt())
def digest(receipt): return E.sha(E.dumps(receipt))


def fix(case):  # re-freeze both case hashes so only the targeted flaw can reject
    case["commandsSha256"], case["terminal"]["evidenceSha256"] = digest(case["commands"]), digest(case["terminal"]["evidence"])


STATE = "expected failure/query/retention state"
MUTATIONS = {
    "duplicate-case": (lambda r: r["cases"].__setitem__(1, copy.deepcopy(r["cases"][0])), "duplicate, missing or reordered"),
    "missing-case": (lambda r: r["cases"].pop(), "duplicate, missing or reordered"),
    "reordered": (lambda r: r["cases"].reverse(), "duplicate, missing or reordered"),
    "fabricated-accept": (lambda r: r["cases"][0]["terminal"].update(accepted=True), STATE),
    "wrong-query": (lambda r: (r["cases"][0]["terminal"]["evidence"].update(processQuery="LIVE"), fix(r["cases"][0])), STATE),
    "stage-not-retained": (lambda r: (r["cases"][0]["terminal"]["evidence"].update(stageRetained=False), fix(r["cases"][0])), STATE),
    "pending-operation": (lambda r: (r["cases"][0]["terminal"]["evidence"].update(uncertainOperations=[1]), fix(r["cases"][0])), STATE),
    "wrong-failure-class": (lambda r: (r["cases"][0]["commands"][0].update(failureClass="TIMEOUT"), fix(r["cases"][0])), "command failure classes"),
    "unfinished-command": (lambda r: (r["cases"][0]["commands"][1].update(state="STARTED"), fix(r["cases"][0])), "command failure classes"),
    "stale-command-bytes": (lambda r: r["cases"][0]["commands"][0].update(stdout="edited"), "raw command receipts"),
    "forged-evidence-digest": (lambda r: r["cases"][0]["terminal"].update(evidenceSha256="0" * 64), "terminal evidence digest"),
    "forbidden-effect": (lambda r: r["cases"][0]["effects"].update(productStarts=1), "forbidden effects"),
    "case-invocation": (lambda r: r["cases"][0].update(invocation="other"), "case identity/shape"),
    "stale-production": (lambda r: r["production"].update({P.EXECUTION: "0" * 64}), "stale production/oracle hashes"),
    "stale-protocol-owner": (lambda r: r["production"].update({P.PROTOCOL: "0" * 64}), "stale production/oracle hashes"),
    "stale-oracle": (lambda r: r["oracles"].update({P.TEST_PROTOCOL: "0" * 64}), "stale production/oracle hashes"),
    "start-sum": (lambda r: r.update(substituteStarts=r["substituteStarts"] + 1), "aggregate counts"),
    "in-process-runner": (lambda r: r.update(runner="IN_PROCESS_FAKE"), "not produced by real inert substitute children"),
    "local-actor": (lambda r: r.update(actor="LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER"), "actor/invocation"),
    "extra-top-key": (lambda r: r.update(extra=1), "receipt shape"),
}


def test_receipt_admission_is_case_specific_hash_joined_and_never_proof_of_execution():
    base = good()
    assert P.control_issue(base, 2, digest(base)) is None and P.admit_controls(base, 2, digest(base)) == "IMPLEMENTATION_WORKER"
    assert [x["case"] for x in base["cases"]] == list(P.CASES) and base["substituteStarts"] == 26 and base["passed"] == 9
    assert set(base["production"]) == set(P.PRODUCTION) and len(base["production"]) == 6 and set(base["oracles"]) == set(P.ORACLES) and len(base["oracles"]) == 4
    assert "frozen digest" in P.control_issue(base, 2, "0" * 64) and "frozen digest" in P.control_issue(base, 2, None)
    assert "fail-closed" in P.control_issue(base, 1, digest(base)) and P.control_issue(None, 2, "x") == "receipt shape"
    with pytest.raises(RuntimeError, match="inert collector controls are required"):
        P.admit_controls(base, 2, "1" * 64)
    broken = good()
    broken["cases"][0]["commands"][0] = {"kind": "taskkill"}  # right shape of case, but a malformed raw command row
    fix(broken["cases"][0])
    with pytest.raises(RuntimeError, match="malformed receipt"):
        P.admit_controls(broken, 2, digest(broken))


@pytest.mark.parametrize("name", MUTATIONS)
def test_each_hostile_receipt_is_rejected_for_its_own_reason(name):
    mutate, reason = MUTATIONS[name]
    receipt = good()
    mutate(receipt)
    issue = P.control_issue(receipt, 2, digest(receipt))
    assert issue is not None and reason in issue, issue


@pytest.fixture
def scratch(request):
    path = SCRATCH / "t" / "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in request.node.name)[-90:]
    path.mkdir(parents=True)  # fixture trees are preserved: this suite never disposes of anything
    return path


@pytest.fixture
def effects(monkeypatch):
    hits = []
    sentinel = lambda name: lambda *_a, **_k: (hits.append(name), (_ for _ in ()).throw(AssertionError("effect: " + name)))  # an ordinary Exception, as the run reports it
    for owner, attr in ((subprocess, "Popen"), (subprocess, "run"), (H.socket, "socket"), (H.urllib.request, "urlopen"), (H, "Native"), (P, "prerequisites"), (P, "stage_source")):
        monkeypatch.setattr(owner, attr, sentinel(attr))
    monkeypatch.setattr(P, "git", lambda *a: hits.append("git") or ("\n".join(P.HELPERS).encode() if a[:2] == ("diff", "--name-only") else b"base\n" if a[0] == "rev-parse" else b""))
    return hits


def controls(scratch, change=lambda r: None):
    receipt = good()
    change(receipt)
    (scratch / "controls.json").write_bytes(E.dumps(receipt))
    return {"controls_receipt": scratch / "controls.json", "controls_digest": digest(receipt)}


def two(index=0, **change):
    return [{**FIX[0], **change}, FIX[1]] if index == 0 else [FIX[0], {**FIX[1], **change}]


BAD = [([FIX[0]], 2), (FIX, 1), (two(extra="x"), 2), (two(title=7), 2), (two(status="e" + chr(0x301)), 2), (two(sourcePath="x/../y"), 2), (two(memoryClass="ADMIN"), 2),
       (two(1, receiptAnchor=FIX[0]["receiptAnchor"]), 2), (FIX, True), (FIX, 3), ("text", 2), (None, 1), ([[FIX[0]]], 1)]


class TestAdmissionBeforeEffects:
    @pytest.mark.parametrize("inputs,cap", BAD)
    def test_wrong_input_stops_before_source_read_namespace_or_effect(self, scratch, effects, inputs, cap):
        with pytest.raises((RuntimeError, ValueError)):
            H.run(scratch / "ns", IMAGE, inputs=inputs, cap=cap, **controls(scratch))
        assert effects == [] and not (scratch / "ns").exists()

    @pytest.mark.parametrize("name", ("duplicate-case", "fabricated-accept", "stale-production", "stale-protocol-owner", "in-process-runner", "start-sum"))
    def test_wrong_control_stops_before_source_read_namespace_or_effect(self, scratch, effects, name):
        with pytest.raises(RuntimeError, match="inert collector controls are required"):
            H.run(scratch / "ns", IMAGE, **controls(scratch, MUTATIONS[name][0]))
        assert effects == [] and not (scratch / "ns").exists()
        with pytest.raises(RuntimeError, match="fail-closed"):  # Local admission stays closed: no genuine matrix exists for it
            H.run(scratch / "ns", IMAGE, inputs=[FIX[0]], cap=1, **controls(scratch))
        assert effects == []

    @pytest.mark.parametrize("drift", ("pin", "pair-missing", "env"))
    def test_source_grant_or_environment_drift_stops_before_namespace(self, scratch, effects, monkeypatch, drift):
        pins = json.loads((P.ROOT / P.PINS).read_text(encoding="utf-8"))
        if drift == "pin":
            pins["sourcePins"][P.WO] = "0" * 64
        elif drift == "pair-missing":
            del pins["sourcePins"][P.PAIR[2]]
        (scratch / "pins.json").write_text(json.dumps(pins), encoding="utf-8")
        monkeypatch.setattr(P, "PINS", str(scratch / "pins.json"))
        if drift == "env":
            monkeypatch.setenv("CVF_HCR_EGRESS_LOG", "x")
        with pytest.raises(RuntimeError):
            H.run(scratch / "ns", IMAGE, **controls(scratch))
        assert not (scratch / "ns").exists() and not {"Native", "Popen", "run", "socket", "urlopen"} & set(effects)

    def test_valid_admission_reaches_only_the_first_owned_effect_and_the_terminal_bytes_are_acknowledged(self, scratch, tmp_path, effects):
        namespace = tmp_path / "ns1"  # admission requires a fresh namespace outside the provenance tree, so this one uses pytest's tmp_path
        out = H.run(namespace, IMAGE, **controls(scratch))
        terminal = out["terminal"]
        assert effects == ["git"] * 4 + ["Native"] and out["ok"] is False and "effect: Native" in out["failures"][0]
        assert terminal["evidence"]["preAckDisposition"] == "NOT_STARTED_NO_NATIVE_RESOURCES" and terminal["accepted"] is False
        assert terminal["acknowledgment"] == {"write": "ACKNOWLEDGED", "readBack": "MATCH", "error": None} and terminal["stageRetained"] is False
        assert E.sha((namespace / "custody/terminal-evidence.json").read_bytes()) == terminal["evidenceSha256"]  # persisted bytes are the frozen bytes


CEILINGS = {P.INIT: 329, P.LIFECYCLE: 329, P.PROFILE: 329, P.EXECUTION: 349, P.JOURNEY: 329, P.PROTOCOL: 299, P.TEST_PROTOCOL: 349, P.JOURNEY_TEST: 299, P.TEST_CONTROL: 296, P.TEST_EXECUTION: 349}


def test_canonical_fixtures_exact12_family_readable_ceilings_and_pinned_immutable_legacy_blob():
    assert [len(x["sourceContent"].encode("utf-16-le")) // 2 for x in FIX] == [650, 726] and P.validate_inputs(FIX, 2) is FIX
    assert "?mode=ro" in Path(P.__file__).read_text(encoding="utf-8") and len(P.OUTPUTS) == 12 and set(P.HELPERS) < set(P.OUTPUTS)
    lines = {r: len((P.ROOT / r).read_bytes().splitlines()) for r in P.HELPERS}
    assert all(n < 350 for n in lines.values()) and all(lines[r] <= limit for r, limit in CEILINGS.items()) and not {P.ENTRY_PY, P.ENTRY_CJS} & set(P.OUTPUTS)
    pins = json.loads((P.ROOT / P.PINS).read_text(encoding="utf-8"))["sourcePins"]
    core = "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core_orchestrator.py"
    text = (P.ROOT / core).read_bytes()
    assert E.sha(text) == pins[core] and b'"decision": decision_result' in text and b"ledger_entry = {" in text  # real nested event schema, source unchanged


def test_ledger_oracle_joins_the_real_nested_schema_and_rejects_old_missing_or_mismatched_rows():
    data = {"execution_record": {"final_decision": "APPROVE", "ledger_attached": True}, "report": {"request_summary": {"request_id": "r1", "artifact_id": "a"}}}
    row = lambda **event: (1, "r1", json.dumps({"event": {"request_id": "r1", "timestamp": "2026-10-15T00:00:00", "decision": {"final_decision": "APPROVE"}, **event}}), "hash")
    P.check_row(row(), "r1", data)
    rows = [(1, "r1", json.dumps({"event": {"request_id": "r1", "timestamp": "t", "final_decision": "APPROVE"}}), "h"), row(final_decision="APPROVE"), row(timestamp=""),
            row(timestamp=None), row(decision={}), row(decision={"final_decision": "REJECT"}), row(request_id="r2"), (1, "r2", row()[2], "h"), (1, "r1", "not json", "h"),
            (1, "r1", "[]", "h"), (1, "r1", "{}", "h"), ("1", "r1", row()[2], "h"), (1, "r1", row()[2], "")]
    for candidate, joined in [(r, data) for r in rows] + [(row(), d) for d in ({}, {**data, "report": {"request_summary": {"request_id": "r2"}}}, {**data, "execution_record": {"final_decision": "REJECT"}})]:
        with pytest.raises(RuntimeError):
            P.check_row(candidate, "r1", joined)
    assert P.v1_changed([{"rows": []}, {"rows": [{"h": 1}]}], [{"h": 1}]) is False and P.v1_changed([{"rows": [{"h": 2}]}], [{"h": 1}]) is True


def test_excerpt_counts_utf16_units_like_the_renderer_including_split_surrogates():
    units = lambda text: len(text.encode("utf-16-le", "surrogatepass")) // 2
    emoji, split = "\U0001F600", "a" * 499 + "\U0001F600" + "tail"
    assert units(P.excerpt(split)) == 500 and P.excerpt(split) == "a" * 499 + "\ud83d"  # JS slice keeps the lone high surrogate
    assert P.excerpt("a" * 498 + emoji + "tail") == "a" * 498 + emoji and units(P.excerpt(emoji * 400)) == 500 and len(P.excerpt(emoji * 400)) == 250
    assert json.loads(json.dumps(P.excerpt(split))) == P.excerpt(split) and units(P.excerpt(FIX[1]["sourceContent"])) == 500 and P.excerpt("short") == "short"

def test_legacy_python_entry_is_the_pinned_immutable_blob_plus_one_routing_branch():
    target = P.ROOT / P.ENTRY_PY
    addition = b'    if "--owned-profile-root" in sys.argv:\n        from cvf_ncr_html_owned_profile import cli\n        sys.exit(cli())\n'
    assert target.read_bytes().count(addition) == 1 and E.sha(target.read_bytes().replace(addition, b"", 1)) == P.BASE_BLOBS[P.ENTRY_PY]
    spec = importlib.util.spec_from_file_location("owned_legacy_probe", target)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.make_export_body("focused")["memoryClass"] == "FULL_RECORD" and module.hcr_raised(module.hcr_admit_forward, True, 2)
