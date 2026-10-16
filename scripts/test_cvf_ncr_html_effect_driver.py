"""Focused in-process models only: no native, subprocess, network or provider effects."""
import copy
import json
import threading
from pathlib import Path
from types import SimpleNamespace

import pytest

from scripts import cvf_ncr_html_effect_fence as F
from scripts import run_cvf_ncr_html_effect_driver as D


class Memory:
    def __init__(self):
        self.files, self.directories, self.events = {}, set(), []

    def read(self, path):
        return self.files[str(path)]

    def check(self, path):
        pass

    def exists(self, path):
        return str(path) in self.files or str(path) in self.directories

    def is_dir(self, path):
        return str(path) in self.directories

    def write(self, path, raw):
        self.files[str(path)] = raw

    def exclusive(self, path, raw):
        if self.exists(path):
            raise FileExistsError(str(path))
        self.events.append("marker")
        self.write(path, raw)

    def sources(self, release):
        self.events.append("source")

    def controls(self, receipt, cap, expected):
        return "IMPLEMENTATION_WORKER" if cap == 2 else "LOCAL_REVIEWER"


@pytest.fixture
def model(monkeypatch):
    io, raw = Memory(), b"synthetic pinned bytes"
    sha = F.digest(raw)
    monkeypatch.setattr(F, "RELEASE_SHA", sha)
    chrome = {"path": str(F.ROOT / ".cvf/runtime/ncr-be-adjunct-source-20261016/fake-chrome.exe"), "sha256": sha}
    monkeypatch.setattr(F, "CHROME", chrome)
    namespace = str(F.ROOT.parent / "ncr-be-source-fake-never-created")
    custody = str(F.ROOT / ".cvf/runtime/ncr-be-adjunct-source-20261016/fake-custody")
    pins = {"schemaVersion": "cvf.ncrHtmlBEEffectPins@1", "scope": "RUNTIME_INVOCATION_PINS",
            "adjunctSources": {path: sha for path in F.SOURCES}, "sourceRelease": {"path": F.RELEASE, "sha256": sha},
            "tools": {key: {"path": str(F.ROOT / (key + ".exe")), "sha256": sha}
                      for key in ("python", "node", "docker", "git", "cmd", "taskkill", "tasklist", "netstat")},
            "modules": {"path": str(F.ROOT / F.owned.P.WEB / "node_modules")},
            "helpers": {"entry": {"path": str(F.ROOT / F.owned.P.ENTRY_CJS), "sha256": sha},
                        "journey": {"path": str(F.ROOT / F.owned.P.JOURNEY), "sha256": sha}},
            "docker": dict(F.DOCKER), "chrome": chrome, "custodyRoot": custody}
    inputs = [{"title": "Synthetic One", "sourcePath": "synthetic/one", "sourceContent": "sample",
               "memoryClass": "FULL_RECORD", "status": "DRAFT", "claimBoundary": "fake only", "receiptAnchor": str(n)} for n in (1, 2)]
    authority = {key + suffix: ("docs/fake-" + key + ".md" if suffix == "Path" else sha)
                 for key in ("baseline", "dispatchWorkOrder", "adjunctAcceptance") for suffix in ("Path", "Sha256")}
    admission = {"schemaVersion": "cvf.ncrHtmlBEEffectAdmission@1", "scope": "OWNED_SYNTHETIC_B_E",
                 "decisionOwner": "LOCAL", "disposition": "RUNTIME_EFFECT_ADMITTED", "authority": authority,
                 "sourceRelease": pins["sourceRelease"], "invocation": {"runId": "fake-1", "ordinal": 1,
                 "actor": "IMPLEMENTATION_WORKER", "cap": 2, "namespace": namespace, "inputsSha256": F.digest(F.canonical(inputs))},
                 "controls": {"path": str(Path(custody) / "controls.json"), "canonicalDigest": sha},
                 "pins": {"manifestPath": str(Path(custody) / "pins.json"), "sha256": F.digest(F.canonical(pins))},
                 "limits": {"workSeconds": 900, "cleanupSeconds": 120, "workStarts": 56, "cleanupStarts": 8,
                            "readiness": {"engine": 4, "web": 6, "route": 2, "total": 12}},
                 "effects": {"job": 1, "container": 1, "web": 1, "browserSession": 1, "exports": 2,
                             "evaluates": 2, "providerStarts": 0, "stageDeletion": 0},
                 "readiness": {"disposition": "READY", "evidence": [{"path": "docs/fake-ready.md", "sha256": sha}]}, "predecessor": None}
    for path in [*(F.ROOT / p for p in F.SOURCES), F.ROOT / F.RELEASE, *[F.ROOT / authority[k] for k in authority if k.endswith("Path")],
                 F.ROOT / "docs/fake-ready.md", *[r["path"] for r in pins["tools"].values()],
                 *[r["path"] for r in pins["helpers"].values()], chrome["path"]]:
        io.write(path, raw)
    io.write(admission["controls"]["path"], b"{}")
    io.write(admission["pins"]["manifestPath"], F.canonical(pins))
    location = str(Path(custody) / "admission.json")
    io.write(location, F.canonical(admission))
    io.directories.update((custody, str(Path(namespace).parent), pins["modules"]["path"]))
    return io, pins, admission, inputs, location


def frame_for(proto, *, cleanup=False):
    c = SimpleNamespace(proto=proto)
    op = proto.queue("launch")
    proto.grant(op, 1)
    c.current_op = lambda: op
    native = SimpleNamespace(c=c)
    frame = {"native": native, "collector": c, "proto": proto, "op": op, "charged": False, "admitted": False}
    F._frames.active = frame
    return op, native, c, frame


def test_boundaries_persistence_and_snapshot():
    proto = F.owned.PR.Protocol(clock=lambda: 0).start()
    persisted, ledger = [], F.StartLedger()
    ledger.persist = lambda row: persisted.append(row)
    for number in range(56):
        op, native, c, frame = frame_for(proto)
        ledger.charge(op, native=native, collector=c, frame=frame)
    op, native, c, frame = frame_for(proto)
    with pytest.raises(ValueError):
        ledger.charge(op, native=native, collector=c, frame=frame)
    proto.close(); proto.begin_cleanup()
    for number in range(8):
        with_scope = proto.scoped(lambda: frame_for(proto))
        op, native, c, frame = with_scope()
        ledger.charge(op, native=native, collector=c, frame=frame)
    op, native, c, frame = proto.scoped(lambda: frame_for(proto))()
    with pytest.raises(ValueError):
        ledger.charge(op, native=native, collector=c, frame=frame)
    assert (ledger.work, ledger.cleanup) == (56, 8)
    persisted[0]["attempts"].clear()
    assert len(ledger.snapshot()["attempts"]) == 64
    F._frames.active = None


@pytest.mark.parametrize("bad", ["inactive", "native", "collector", "op", "state", "registered", "reuse"])
def test_invalid_frame_never_charges(bad):
    proto = F.owned.PR.Protocol(clock=lambda: 0).start()
    op, native, c, frame = frame_for(proto)
    if bad == "inactive": F._frames.active = None
    if bad == "native": frame["native"] = object()
    if bad == "collector": frame["collector"] = object()
    if bad == "op": frame["op"] = object()
    if bad == "state": op.state = "DONE"
    if bad == "registered": proto.ops.clear()
    if bad == "reuse": frame["charged"] = True
    ledger = F.StartLedger()
    with pytest.raises(ValueError): ledger.charge(op, native=native, collector=c, frame=frame)
    assert ledger.work == ledger.cleanup == 0
    F._frames.active = None


def test_spent_after_persistence_failure_and_expiry():
    now = [0]
    proto = F.owned.PR.Protocol(clock=lambda: now[0]).start()
    op, native, c, frame = frame_for(proto)
    ledger = F.StartLedger(lambda row: now.__setitem__(0, 901))
    with pytest.raises(F.owned.PR.Stop): ledger.charge(op, native=native, collector=c, frame=frame)
    assert ledger.work == 1
    F._frames.active = None
    proto = F.owned.PR.Protocol(clock=lambda: 0).start()
    op, native, c, frame = frame_for(proto)
    ledger = F.StartLedger(lambda row: (_ for _ in ()).throw(OSError("persist failed")))
    with pytest.raises(OSError): ledger.charge(op, native=native, collector=c, frame=frame)
    assert ledger.work == 1
    F._frames.active = None


def test_concurrent_final_slot():
    ledger, results = F.StartLedger(), []
    ledger.work = 55
    barrier = threading.Barrier(2)
    def attempt():
        proto = F.owned.PR.Protocol(clock=lambda: 0).start()
        op, native, c, frame = frame_for(proto)
        barrier.wait()
        try: ledger.charge(op, native=native, collector=c, frame=frame); results.append("charged")
        except ValueError: results.append("refused")
        finally: F._frames.active = None
    threads = [threading.Thread(target=attempt) for _ in range(2)]
    for thread in threads: thread.start()
    for thread in threads: thread.join(2); assert not thread.is_alive()
    assert sorted(results) == ["charged", "refused"]


def test_original_spawn_order_and_exception_restore(model, monkeypatch):
    io, pins, admission, inputs, location = model
    events = []
    class API:
        def create_job(self): events.append("job"); return 1
        def set_limits(self, job, active): pass
        def query_limits(self, job): return {"active": 32, "killOnClose": True, "breakaway": False, "silentBreakaway": False}
        def assign(self, job, handle): events.append("assign")
        def identity(self, pid, handle): events.append("identity"); return {"pid": pid}
        def resume(self, pid): events.append("resume")
    def spawn(argv, **kw):
        assert kw["creationflags"] == 4
        events.append("popen")
        return SimpleNamespace(pid=7, _handle=7)
    original = F.owned.Native
    monkeypatch.setattr(original, "_record", lambda self: events.append("record"))
    policy = {"io": io, "invocation": admission["invocation"], "inputs": inputs}
    with F.installed_fences(policy, pins, lambda row: events.append("charge"), api_factory=API, popen=spawn) as ledger:
        proto = F.owned.PR.Protocol(clock=lambda: 0).start()
        c = F.owned.E.Collector(Path("unused"), proto=proto)
        native = F.owned.Native(c, [], Path("unused"), Path("unused"))
        native.launch(["node", "fake"], cwd="unused", env={}, stdout=None)
        assert ledger.work == 1
        assert events == ["job", "charge", "popen", "assign", "identity", "record", "resume"]
        op = proto.queue("utility"); proto.grant(op, 1); c.local.op = op
        native._spawn(["node", "fake"], admitted=True)
        assert ledger.work == 2
        with pytest.raises(ValueError):
            with F.installed_fences(policy, pins, lambda row: None): pass
    assert F.owned.Native is original
    with pytest.raises(RuntimeError):
        with F.installed_fences(policy, pins, lambda row: None): raise RuntimeError("runner")
    assert F.owned.Native is original


@pytest.mark.parametrize("name", ["NODE_OPTIONS", "node_path", "PWDEBUG", "PLAYWRIGHT_BROWSERS_PATH",
                                  "npm_config_playwright_browsers_path", "npm_package_config_pwdebug", "DOCKER_HOST", F.KEYS[0]])
def test_environment_refusal(name):
    with pytest.raises(ValueError): F.reject_environment({name: "never print"})


@pytest.mark.parametrize("change", ["scope", "extra", "bool", "actor", "namespace", "inputs", "predecessor", "readiness", "pinextra"])
def test_closed_admission_refusal(model, change):
    io, pins, a, inputs, location = model
    if change == "scope": a["scope"] = "SOURCE_ADJUNCT_ONLY"
    if change == "extra": a["extra"] = 1
    if change == "bool": a["limits"]["workStarts"] = True
    if change == "actor": a["invocation"]["actor"] = "LOCAL_REVIEWER"
    if change == "namespace": a["invocation"]["namespace"] = str(F.ROOT / "bad")
    if change == "inputs": a["invocation"]["inputsSha256"] = "0" * 64
    if change == "predecessor": a["predecessor"] = {}
    if change == "readiness": a["readiness"]["evidence"] *= 2
    if change == "pinextra": pins["extra"] = 1
    with pytest.raises(ValueError): D.validate_admission(a, pins, inputs=inputs)
    assert io.events == []


def test_marker_before_runner_retained_on_error_and_no_duplicate(model):
    io, pins, a, inputs, location = model
    expected = F.digest(io.read(location))
    def runner(*args, **kwargs):
        assert io.events[-1] == "marker"
        io.events.append("runner")
        raise RuntimeError("modeled failure")
    with pytest.raises(RuntimeError): D.execute(location, expected, inputs=inputs, io=io, runner=runner)
    with pytest.raises(FileExistsError): D.execute(location, expected, inputs=inputs, io=io, runner=runner)
    assert io.events.count("runner") == 1
    marker = Path(pins["custodyRoot"]) / "fake-1.spent.json"
    assert json.loads(io.read(marker))["admissionSha256"] == expected


def test_raw_digest_duplicate_and_missing_terminal_refuse(model):
    io, pins, a, inputs, location = model
    with pytest.raises(ValueError): D.load_admission(location, "0" * 64, io=io)
    with pytest.raises(ValueError): D._parse(b'{"x":{"z":1,"z":2}}')
    output = D.execute(location, F.digest(io.read(location)), inputs=inputs, io=io, runner=lambda *a, **k: {"ok": False})
    assert output["ok"] is False and output["effectFence"]["joinsAccepted"] is False
    assert output["effectFence"]["ledger"] == {"workUsed": 0, "cleanupUsed": 0, "attempts": []}


@pytest.mark.parametrize("kind,result", [("docker-context", "other"),
    ("docker-context-inspect", {"Endpoints": {"docker": {"Host": "npipe://wrong"}}}),
    ("cached-image", {"Id": "wrong", "Os": "linux", "Architecture": "amd64"}),
    ("installed-browser-path", "other")])
def test_identity_fence_before_next_effect(model, monkeypatch, kind, result):
    io, pins, a, inputs, location = model
    events = []
    monkeypatch.setattr(F.owned.E.Collector, "command", lambda *args, **kwargs: events.append(kind) or result)
    with F.installed_fences({"io": io}, pins, lambda row: None):
        collector = F.owned.E.Collector(Path("unused"), proto=F.owned.PR.Protocol(clock=lambda: 0).start())
        with pytest.raises(ValueError): collector.command(kind, ["fake"])
    assert events == [kind]


def test_terminal_and_browser_joins_are_required(model):
    io, pins, a, inputs, location = model
    binding = {"runId": "fake-1", "actor": "IMPLEMENTATION_WORKER", "cap": 2, "config": {"sha256": "1" * 64},
               "preload": {"sha256": "2" * 64}, "chrome": pins["chrome"], "observationPath": "fake-observation"}
    policy = {"invocation": a["invocation"], "binding": binding}
    evidence = {key: "ABSENT" for key in ("processQuery", "containerQuery", "descendantQuery", "listenerQuery")}
    evidence["child"] = {"confirmed": True}
    raw = F.canonical(evidence)
    io.write(Path(a["invocation"]["namespace"]) / "custody/terminal-evidence.json", raw)
    terminal = {"evidence": evidence, "evidenceSha256": F.digest(raw), "evidenceBytes": len(raw), "accepted": True,
                "acknowledgment": {"write": "ACKNOWLEDGED", "readBack": "MATCH", "error": None}}
    observation = {"schemaVersion": "cvf.ncrHtmlBrowserFenceObservation@1", "runId": binding["runId"],
                   "actor": binding["actor"], "cap": binding["cap"], "bindingSha256": F.digest(F.canonical(binding)),
                   "configSha256": "1" * 64, "preloadSha256": "2" * 64, "chrome": pins["chrome"], "verified": True, "invocations": 1}
    io.write("fake-observation", F.canonical(observation))
    assert D._terminal_join({"terminal": terminal}, policy, io) == observation
    before = copy.deepcopy(terminal)
    for key, value in (("accepted", False), ("evidenceSha256", "0" * 64), ("evidenceBytes", True)):
        bad = copy.deepcopy(before); bad[key] = value
        with pytest.raises(ValueError): D._terminal_join({"terminal": bad}, policy, io)
    observation["cap"] = 1
    io.write("fake-observation", F.canonical(observation))
    with pytest.raises(ValueError): D._terminal_join({"terminal": terminal}, policy, io)
    assert terminal == before
