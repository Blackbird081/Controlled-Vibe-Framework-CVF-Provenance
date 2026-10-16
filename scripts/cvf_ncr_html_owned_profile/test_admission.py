"""Actor/cap joins and exact current source locks; fixture receipts are never execution evidence."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path

import pytest

from . import execution as E
from . import profile as P
from . import test_control as T

OWN = P.ROOT / ".cvf/runtime/ncr-source-admission-20261016/worker" / ("admission-" + os.urandom(8).hex())
CURRENT = (*P.HELPERS, "scripts/cvf_ncr_html_owned_profile/test_win32.py", "scripts/cvf_ncr_html_owned_profile/test_admission.py")
CURRENT = tuple(dict.fromkeys(CURRENT))


@pytest.fixture(scope="module")
def receipt():
    T.SCRATCH = OWN / ("fixture-" + os.urandom(8).hex())
    return T.good()


def frozen(receipt):
    return E.sha(E.dumps(receipt))


@pytest.mark.parametrize("cap,actor", [(1, "LOCAL_REVIEWER"), (2, "IMPLEMENTATION_WORKER")])
def test_each_actor_accepts_only_its_cap(receipt, cap, actor):
    value = copy.deepcopy(receipt)
    value["actor"] = actor
    assert P.control_issue(value, cap, frozen(value)) is None
    assert P.admit_controls(value, cap, frozen(value)) == actor
    assert "actor/cap" in P.control_issue(value, 3 - cap, frozen(value))


@pytest.mark.parametrize("cap", [True, False, 1.0, 2.0, "1", "2", None, 0, 3, [], {}])
def test_invalid_cap_never_admits_receipt(receipt, cap):
    assert P.control_issue(receipt, cap, frozen(receipt)) is not None


@pytest.mark.parametrize("name", T.MUTATIONS)
def test_local_control_keeps_existing_case_and_hash_rejections(receipt, name):
    value = copy.deepcopy(receipt)
    value["actor"] = "LOCAL_REVIEWER"
    mutate, _ = T.MUTATIONS[name]
    mutate(value)
    assert P.control_issue(value, 1, frozen(value)) is not None


def test_local_control_needs_own_frozen_digest_and_current_whole_family(receipt):
    value = copy.deepcopy(receipt)
    value["actor"] = "LOCAL_REVIEWER"
    assert P.control_issue(value, 1, frozen(value)) is None
    assert P.control_issue(value, 1, "0" * 64) is not None
    assert len(P.PRODUCTION) == 7 and len(P.ORACLES) == 6
    assert set(P.HELPERS) == set(CURRENT) and len(P.HELPERS) == 13
    for path in (*P.PRODUCTION, *P.ORACLES):
        hostile = copy.deepcopy(value)
        family = "production" if path in P.PRODUCTION else "oracles"
        hostile[family][path] = "0" * 64
        assert P.control_issue(hostile, 1, frozen(hostile)) == "stale production/oracle hashes"


@pytest.fixture
def sources(monkeypatch):
    root = OWN / ("sources-" + os.urandom(8).hex())
    root.mkdir(parents=True)
    pins = {}
    for path in dict.fromkeys((*P.PAIR, *CURRENT)):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(("fixture " + path).encode())
        pins[path] = E.sha(target.read_bytes())
    calls = []

    def git(*args):
        calls.append(args)
        return b"fixture-head\n" if args == ("rev-parse", "HEAD") else b""

    monkeypatch.setattr(P, "ROOT", root)
    monkeypatch.setattr(P, "PINS", "pins.json")
    monkeypatch.setattr(P, "git", git)

    def write(value):
        (root / "pins.json").write_bytes(E.dumps(value))

    write({"sourcePins": pins})
    return root, pins, calls, write


def test_exact_current_sources_report_all_verified_pins(sources):
    _, pins, calls, _ = sources
    admitted = P.admit_sources()
    assert admitted["executionBaseHead"] == "fixture-head"
    assert admitted["immutablePins"] == pins
    assert admitted["implementedHelpers"] == {p: pins[p] for p in P.HELPERS}
    assert len(calls) == 4


@pytest.mark.parametrize("path", CURRENT)
def test_changed_helper_bytes_refuse_before_git_or_runtime(sources, path):
    root, _, calls, _ = sources
    (root / path).write_bytes(b"drift")
    with pytest.raises(RuntimeError, match="source pin drift"):
        P.admit_sources()
    assert calls == []


@pytest.mark.parametrize("path", CURRENT)
def test_missing_current_helper_pin_refuses_before_git(sources, path):
    _, pins, calls, write = sources
    pins.pop(path)
    write({"sourcePins": pins})
    with pytest.raises(RuntimeError, match="source pin missing"):
        P.admit_sources()
    assert calls == []


@pytest.mark.parametrize("value", [None, [], {}, {"sourcePins": []}, {"sourcePins": None}])
def test_malformed_source_manifest_refuses_before_git(sources, value):
    _, _, calls, write = sources
    write(value)
    with pytest.raises(RuntimeError, match="source pin"):
        P.admit_sources()
    assert calls == []


def test_historical_runtime_manifest_cannot_admit_current_source(monkeypatch):
    calls = []
    monkeypatch.setattr(P, "git", lambda *args: calls.append(args) or b"")
    with pytest.raises(RuntimeError, match="source pin missing|source pin drift"):
        P.admit_sources()
    assert calls == []


@pytest.fixture
def released(monkeypatch):
    from . import source_release as S
    root = OWN / ("release-" + os.urandom(8).hex())
    pins = {}
    for path in (*P.HELPERS, *S.ENTRYPOINTS, *S.AUTHORITY, S.SPEC):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(("isolated source " + path).encode())
        pins[path] = E.sha(target.read_bytes())
    objects = {p: str(i + 1) * 40 for i, p in enumerate(S.SCOPES)}
    doc = {"schemaVersion": S.SCHEMA, "profile": S.PROFILE, "scope": "SOURCE_IDENTITY_ONLY",
           "sourcePins": {p: pins[p] for p in P.HELPERS}, "productCommit": "a" * 40,
           "productScopeGitObjects": objects, "fixture": {"path": S.SPEC, "sha256": pins[S.SPEC]},
           "entrypoints": {p: pins[p] for p in S.ENTRYPOINTS}, "authority": {p: pins[p] for p in S.AUTHORITY}}
    calls, responses = [], {}
    def git(*args):
        calls.append(args)
        if args in responses:
            return responses[args]
        if args == ("rev-parse", "HEAD"):
            return b"b" * 40
        if args[0] == "rev-parse":
            return (objects[args[1].split(":", 1)[1]] if ":" in args[1] else "a" * 40).encode()
        return b""
    monkeypatch.setattr(P, "ROOT", root)
    monkeypatch.setattr(P, "git", git)
    name = "docs/reviews/evidence/release-fixture.json"
    def write(value=doc, raw=None):
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        data = E.dumps(value) if raw is None else raw
        target.write_bytes(data)
        return name, E.sha(data)
    return root, doc, calls, responses, write


def test_explicit_current_release_and_later_metadata_are_identity_only(released):
    _, doc, _, _, write = released
    admitted = P.admit_sources(*write())
    assert admitted["executionBaseHead"] != doc["productCommit"]
    assert admitted["productBinding"]["productScopeGitObjects"] == doc["productScopeGitObjects"]
    assert admitted["implementedHelpers"] == doc["sourcePins"] and len(admitted["implementedHelpers"]) == 13
    assert admitted["sourceRelease"]["scope"] == "SOURCE_IDENTITY_ONLY"


@pytest.mark.parametrize("kind", ["path-only", "digest-only", "wrong-digest", "oversize", "bad-json", "duplicate", "nested-duplicate"])
def test_explicit_partial_or_changed_bytes_refuse_without_legacy_or_git(released, kind):
    _, _, calls, _, write = released
    path, hashed = write()
    if kind == "path-only": hashed = None
    if kind == "digest-only": path = None
    if kind == "wrong-digest": hashed = "0" * 64
    if kind in ("oversize", "bad-json", "duplicate", "nested-duplicate"):
        path, hashed = write(raw={"oversize": b" " * 65537, "bad-json": b"{", "duplicate": b'{"x":1,"x":2}',
                                  "nested-duplicate": b'{"x":{"a":1,"a":2}}'}[kind])
    with pytest.raises(RuntimeError, match="explicit source release"):
        P.admit_sources(path, hashed)
    assert calls == []


@pytest.mark.parametrize("kind", ["candidate", "foreign", "scope", "extra", "missing", "not-object", "commit", "objects", "fixture"])
def test_closed_release_schema(released, kind):
    _, doc, _, _, write = released
    if kind == "candidate": doc["schemaVersion"] = "cvf.ncrHtmlDocumentaryReleaseCandidate.v2"
    if kind == "foreign": doc["profile"] = "FOREIGN"
    if kind == "scope": doc["scope"] = "RUNTIME_GRANTED"
    if kind == "extra": doc["extra"] = True
    if kind == "missing": doc.pop("entrypoints")
    if kind == "commit": doc["productCommit"] = "HEAD"
    if kind == "objects": doc["productScopeGitObjects"]["foreign"] = "f" * 40
    if kind == "fixture": doc["fixture"]["extra"] = "x"
    with pytest.raises(RuntimeError):
        P.admit_sources(*write([] if kind == "not-object" else doc))


PIN_CASES = [(family, path) for family, paths in (("sourcePins", P.HELPERS), ("entrypoints", P.S.ENTRYPOINTS),
             ("authority", P.S.AUTHORITY)) for path in paths]


@pytest.mark.parametrize("family,path", PIN_CASES)
@pytest.mark.parametrize("mutation", ["missing", "extra", "stale", "malformed"])
def test_every_pinned_family_is_exact_current_bytes(released, family, path, mutation):
    _, doc, calls, _, write = released
    if mutation == "missing": doc[family].pop(path)
    if mutation == "extra": doc[family]["foreign"] = "0" * 64
    if mutation == "stale": doc[family][path] = "0" * 64
    if mutation == "malformed": doc[family][path] = True
    with pytest.raises(RuntimeError):
        P.admit_sources(*write())
    assert calls == []


@pytest.mark.parametrize("path", ["/abs.json", "C:/x.json", "//host/x", "docs/reviews/evidence/a.json:stream",
    "docs\\reviews\\evidence\\x.json", "docs/reviews/evidence/../x.json", "docs//reviews/evidence/x.json", "docs/reviews/evidence/./x.json"])
def test_selector_paths_never_escape(released, path):
    _, _, calls, _, _ = released
    with pytest.raises(RuntimeError):
        P.admit_sources(path, "0" * 64)
    assert calls == []


@pytest.mark.parametrize("kind", ["reparse", "nonregular", "fixture-drift"])
def test_file_boundaries_are_checked_before_reads(released, monkeypatch, kind):
    root, _, calls, _, write = released
    args = write()
    if kind == "fixture-drift":
        (root / P.S.SPEC).write_bytes(b"changed fixture")
    elif kind == "nonregular":
        name = "docs/reviews/evidence/nonregular.json"
        (root / name).mkdir()
        args = (name, args[1])
    else:
        original = Path.lstat
        def lstat(path, *a, **k):
            info = original(path, *a, **k)
            if path == root / "docs":
                from types import SimpleNamespace
                return SimpleNamespace(st_mode=info.st_mode, st_file_attributes=0x400)
            return info
        monkeypatch.setattr(Path, "lstat", lstat)
    with pytest.raises(RuntimeError):
        P.admit_sources(*args)
    assert calls == []


@pytest.mark.parametrize("args", [("diff", "--name-only", "HEAD"), ("diff", "--cached", "--name-only"),
    ("ls-files", "--others", "--exclude-standard"), ("rev-parse", "HEAD:" + P.S.SCOPES[0])])
def test_explicit_dirty_index_untracked_and_product_drift_refuse(released, args):
    _, _, _, responses, write = released
    responses[args] = b"unexpected"
    with pytest.raises(RuntimeError):
        P.admit_sources(*write())


def test_staging_consumes_bindings_and_rechecks_before_copy(released):
    root, _, calls, responses, write = released
    admitted = P.admit_sources(*write())
    staged = root / "tiny-model-stage"
    scoped = P.S.SCOPES[0] + "/tiny.txt"
    target = root / scoped
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(b"tiny synthetic source")
    responses[("ls-files", "-z", "--", *P.S.SCOPES)] = scoped.encode() + b"\0"
    assert P.stage_source(staged, admitted) == {scoped: E.sha(target.read_bytes())}
    responses[("rev-parse", "HEAD:" + P.S.SCOPES[0])] = b"changed"
    with pytest.raises(RuntimeError):
        P.stage_source(root / "never-created", admitted)
    assert not (root / "never-created").exists() and calls


def test_failed_explicit_release_stops_run_before_namespace(released, monkeypatch):
    import cvf_ncr_html_owned_profile as H
    root, _, _, _, write = released
    path, _ = write()
    monkeypatch.setattr(P, "admit_controls", lambda *a: "IMPLEMENTATION_WORKER")
    with pytest.raises(RuntimeError, match="external digest"):
        H.run(root / "never", T.IMAGE, inputs=T.FIX, source_release=path, source_release_sha256="0" * 64)
    assert not (root / "never").exists()


def test_cli_forwards_explicit_release_pair(monkeypatch):
    import sys
    import cvf_ncr_html_owned_profile as H
    captured = {}
    def run(*args, **kw):
        captured.update(kw)
        return {"ok": True}
    monkeypatch.setattr(H, "run", run)
    monkeypatch.setattr(sys, "argv", ["owned", "--owned-profile-root", "unused", "--engine-docker-image", T.IMAGE,
        "--owned-profile-controls", "unused", "--owned-profile-controls-sha256", "0" * 64,
        "--owned-profile-source-release", "docs/reviews/evidence/release.json", "--owned-profile-source-release-sha256", "a" * 64])
    assert H.cli() == 0 and captured["source_release"] == "docs/reviews/evidence/release.json" and captured["source_release_sha256"] == "a" * 64
