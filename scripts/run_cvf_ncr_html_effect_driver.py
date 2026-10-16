"""Explicit effect admission and immutable-owner invocation; importing grants nothing."""
from __future__ import annotations

import json
import re
from pathlib import Path

try:
    from . import cvf_ncr_html_effect_fence as F
except ImportError:
    import cvf_ncr_html_effect_fence as F


class Admission(dict):
    """Closed document plus out-of-band raw digest and resolved pin document."""


def _parse(raw):
    F.require(type(raw) is bytes and len(raw) <= 2 * 1024 * 1024, "bounded JSON bytes required")
    def pairs(rows):
        result = {}
        for key, value in rows:
            F.require(key not in result, "duplicate JSON key")
            result[key] = value
        return result
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                      parse_constant=lambda value: F.require(False, "nonfinite JSON"))


def _pair(value, *, relative=False):
    F.closed(value, "path sha256")
    F.safe_path(value["path"], relative=relative)
    F.hexhash(value["sha256"])


def _number(value, expected):
    F.require(type(value) is int and value == expected, "exact integer required")


def _pins(pins):
    F.closed(pins, "schemaVersion scope adjunctSources sourceRelease tools modules helpers docker chrome custodyRoot")
    F.require(pins["schemaVersion"] == "cvf.ncrHtmlBEEffectPins@1" and pins["scope"] == "RUNTIME_INVOCATION_PINS", "pin scope")
    F.require(type(pins["adjunctSources"]) is dict and set(pins["adjunctSources"]) == set(F.SOURCES), "adjunct family mismatch")
    for value in pins["adjunctSources"].values():
        F.hexhash(value)
    F.require(pins["sourceRelease"] == {"path": F.RELEASE, "sha256": F.RELEASE_SHA}, "original release required")
    F.closed(pins["tools"], "python node docker git cmd taskkill tasklist netstat")
    for value in pins["tools"].values():
        _pair(value)
    F.closed(pins["modules"], "path")
    F.require(pins["modules"]["path"] == str(F.ROOT / F.owned.P.WEB / "node_modules"), "module directory mismatch")
    F.closed(pins["helpers"], "entry journey")
    for key, source in (("entry", F.owned.P.ENTRY_CJS), ("journey", str(F.owned.P.JOURNEY))):
        _pair(pins["helpers"][key])
        F.require(pins["helpers"][key]["path"] == str(F.ROOT / source), "helper path mismatch")
    F.require(pins["docker"] == F.DOCKER and pins["chrome"] == F.CHROME, "qualified identities required")
    F.safe_path(pins["custodyRoot"])


def validate_admission(document, pins, *, inputs):
    F.closed(document, "schemaVersion scope decisionOwner disposition authority sourceRelease invocation controls pins limits effects readiness predecessor")
    F.require((document["schemaVersion"], document["scope"], document["decisionOwner"], document["disposition"]) ==
              ("cvf.ncrHtmlBEEffectAdmission@1", "OWNED_SYNTHETIC_B_E", "LOCAL", "RUNTIME_EFFECT_ADMITTED"), "runtime admission required")
    _pins(pins)
    authority = document["authority"]
    F.closed(authority, "baselinePath baselineSha256 dispatchWorkOrderPath dispatchWorkOrderSha256 adjunctAcceptancePath adjunctAcceptanceSha256")
    for key in ("baseline", "dispatchWorkOrder", "adjunctAcceptance"):
        F.safe_path(authority[key + "Path"], relative=True)
        F.hexhash(authority[key + "Sha256"])
    F.require(document["sourceRelease"] == pins["sourceRelease"], "source release mismatch")
    inv = document["invocation"]
    F.closed(inv, "runId ordinal actor cap namespace inputsSha256")
    F.require(type(inv["runId"]) is str and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", inv["runId"]), "unsafe run ID")
    F.require(type(inv["ordinal"]) is int and inv["ordinal"] in (1, 2), "actor ordinal")
    cap, actor = (2, "IMPLEMENTATION_WORKER") if inv["ordinal"] == 1 else (1, "LOCAL_REVIEWER")
    _number(inv["cap"], cap)
    F.require(inv["actor"] == actor, "actor mismatch")
    namespace = F.safe_path(inv["namespace"])
    F.require(not namespace.is_relative_to(F.ROOT) and not Path(pins["custodyRoot"]).is_relative_to(namespace), "namespace ownership")
    F.owned.P.validate_inputs(inputs, cap)
    F.require(inv["inputsSha256"] == F.digest(F.canonical(inputs)), "input identity mismatch")
    F.closed(document["controls"], "path canonicalDigest")
    F.safe_path(document["controls"]["path"])
    F.hexhash(document["controls"]["canonicalDigest"])
    F.closed(document["pins"], "manifestPath sha256")
    F.safe_path(document["pins"]["manifestPath"])
    F.hexhash(document["pins"]["sha256"])
    limits = document["limits"]
    F.closed(limits, "workSeconds cleanupSeconds workStarts cleanupStarts readiness")
    for key, value in (("workSeconds", 900), ("cleanupSeconds", 120), ("workStarts", 56), ("cleanupStarts", 8)):
        _number(limits[key], value)
    F.closed(limits["readiness"], "engine web route total")
    for key, value in (("engine", 4), ("web", 6), ("route", 2), ("total", 12)):
        _number(limits["readiness"][key], value)
    effects = document["effects"]
    F.closed(effects, "job container web browserSession exports evaluates providerStarts stageDeletion")
    for key in effects:
        _number(effects[key], cap if key in ("exports", "evaluates") else 0 if key in ("providerStarts", "stageDeletion") else 1)
    F.closed(document["readiness"], "disposition evidence")
    rows = document["readiness"]["evidence"]
    F.require(document["readiness"]["disposition"] == "READY" and type(rows) is list and rows, "readiness missing")
    for row in rows:
        _pair(row, relative=True)
    F.require(len({x["path"] for x in rows}) == len(rows), "duplicate readiness proof")
    predecessor = document["predecessor"]
    if inv["ordinal"] == 1:
        F.require(predecessor is None, "first run predecessor")
    else:
        F.closed(predecessor, "runId terminalPath terminalSha256 acceptancePath acceptanceSha256")
        F.require(type(predecessor["runId"]) is str and predecessor["runId"] != inv["runId"]
                  and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", predecessor["runId"]), "predecessor run ID")
        F.safe_path(predecessor["terminalPath"])
        F.safe_path(predecessor["acceptancePath"], relative=True)
        F.hexhash(predecessor["terminalSha256"])
        F.hexhash(predecessor["acceptanceSha256"])
    return document


def _verify(io, path, expected):
    raw = io.read(path)
    F.require(F.digest(raw) == expected, "pinned byte drift")
    return raw


def load_admission(path, expected_sha256, *, io=None):
    io = io or F.Disk()
    F.hexhash(expected_sha256)
    raw = _verify(io, F.safe_path(str(path)), expected_sha256)
    document = Admission(_parse(raw))
    F.closed(document, "schemaVersion scope decisionOwner disposition authority sourceRelease invocation controls pins limits effects readiness predecessor")
    F.closed(document["pins"], "manifestPath sha256")
    F.hexhash(document["pins"]["sha256"])
    pins = _parse(_verify(io, F.safe_path(document["pins"]["manifestPath"]), document["pins"]["sha256"]))
    _pins(pins)
    document.raw_sha256, document.pin_document = expected_sha256, pins
    return document


def consume_run(admission, pins, *, io=None):
    io = io or F.Disk()
    F.require(isinstance(admission, Admission) and hasattr(admission, "raw_sha256"), "loaded admission required")
    inv, root = admission["invocation"], F.safe_path(pins["custodyRoot"])
    F.require(io.is_dir(root) and not root.is_relative_to(Path(inv["namespace"])), "existing external custody required")
    F.require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", inv["runId"]), "unsafe marker")
    marker = root / (inv["runId"] + ".spent.json")
    row = {"admissionSha256": admission.raw_sha256, **{key: inv[key] for key in ("runId", "ordinal", "actor", "namespace")}}
    io.exclusive(marker, F.canonical(row))
    return str(marker)


def _terminal_join(output, policy, io):
    terminal = output.get("terminal", {})
    namespace = Path(policy["invocation"]["namespace"])
    raw = io.read(namespace / "custody/terminal-evidence.json")
    evidence = _parse(raw)
    F.require(terminal.get("evidence") == evidence and terminal.get("evidenceSha256") == F.digest(raw)
              and type(terminal.get("evidenceBytes")) is int and terminal["evidenceBytes"] == len(raw), "terminal byte join")
    F.require(terminal.get("accepted") is True and terminal.get("acknowledgment", {}).get("write") == "ACKNOWLEDGED"
              and terminal["acknowledgment"].get("readBack") == "MATCH", "terminal ACK join")
    F.require(all(evidence.get(k) == "ABSENT" for k in ("processQuery", "containerQuery", "descendantQuery", "listenerQuery"))
              and evidence.get("child", {}).get("confirmed") is True, "positive absence join")
    binding = policy.get("binding")
    F.require(binding is not None, "helper binding missing")
    observation = _parse(io.read(binding["observationPath"]))
    expected = {"schemaVersion": "cvf.ncrHtmlBrowserFenceObservation@1", "runId": binding["runId"],
                "actor": binding["actor"], "cap": binding["cap"], "bindingSha256": F.digest(F.canonical(binding)),
                "configSha256": binding["config"]["sha256"], "preloadSha256": binding["preload"]["sha256"],
                "chrome": binding["chrome"], "verified": True, "invocations": 1}
    F.require(F.canonical(observation) == F.canonical(expected), "browser observation join")
    return observation


def execute(path, expected_sha256, *, inputs, io=None, runner=None, api_factory=None, popen=None):
    io = io or F.Disk()
    admission = load_admission(path, expected_sha256, io=io)
    pins = admission.pin_document
    validate_admission(admission, pins, inputs=inputs)
    F.reject_environment(F.os.environ)
    inv, authority = admission["invocation"], admission["authority"]
    for key in ("baseline", "dispatchWorkOrder", "adjunctAcceptance"):
        _verify(io, F.ROOT / authority[key + "Path"], authority[key + "Sha256"])
    for row in admission["readiness"]["evidence"]:
        _verify(io, F.ROOT / row["path"], row["sha256"])
    for source, expected in pins["adjunctSources"].items():
        _verify(io, F.ROOT / source, expected)
    _verify(io, F.ROOT / F.RELEASE, F.RELEASE_SHA)
    for row in (*pins["tools"].values(), *pins["helpers"].values(), pins["chrome"]):
        _verify(io, row["path"], row["sha256"])
    F.require(io.is_dir(pins["modules"]["path"]), "installed module directory missing")
    F.require(not io.exists(inv["namespace"]) and io.is_dir(Path(inv["namespace"]).parent), "fresh namespace required")
    receipt = _parse(io.read(admission["controls"]["path"]))
    F.require(io.controls(receipt, inv["cap"], admission["controls"]["canonicalDigest"]) == inv["actor"], "actor receipt mismatch")
    io.sources(admission["sourceRelease"])
    predecessor = admission["predecessor"]
    if predecessor is not None:
        terminal = _parse(_verify(io, predecessor["terminalPath"], predecessor["terminalSha256"]))
        acceptance = _parse(_verify(io, F.ROOT / predecessor["acceptancePath"], predecessor["acceptanceSha256"]))
        F.require(acceptance.get("runId") == predecessor["runId"] and acceptance.get("decisionOwner") == "LOCAL"
                  and acceptance.get("accepted") is True and acceptance.get("terminalSha256") == predecessor["terminalSha256"], "predecessor acceptance")
        F.require(all(terminal.get(k) == "ABSENT" for k in ("processQuery", "containerQuery", "descendantQuery", "listenerQuery"))
                  and terminal.get("child", {}).get("confirmed") is True, "predecessor absence")
    consume_run(admission, pins, io=io)
    policy = {"invocation": inv, "inputs": inputs, "io": io}
    location = Path(pins["custodyRoot"]) / (inv["runId"] + ".starts.json")
    with F.installed_fences(policy, pins, lambda row: io.write(location, F.canonical(row)), api_factory=api_factory, popen=popen) as ledger:
        output = (runner or F.owned.run)(inv["namespace"], pins["docker"]["image"], inputs=inputs, cap=inv["cap"],
                    controls_receipt=admission["controls"]["path"], controls_digest=admission["controls"]["canonicalDigest"],
                    source_release=F.RELEASE, source_release_sha256=F.RELEASE_SHA)
        observation, joined = None, False
        if output.get("ok") is True:
            try:
                observation = _terminal_join(output, policy, io)
                joined = True
            except (ValueError, OSError, KeyError, TypeError):
                pass
        return {**output, "ok": output.get("ok") is True and joined,
                "effectFence": {"ledger": ledger.snapshot(), "browserVerification": observation, "joinsAccepted": joined}}


if __name__ == "__main__":
    raise SystemExit("Explicit separately admitted runtime invocation required; no effect started")
