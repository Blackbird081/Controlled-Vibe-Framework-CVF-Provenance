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

OWN = P.ROOT / ".cvf/runtime/ncr-html-cap1-admission-local-20261016"
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
    assert len(P.PRODUCTION) == 6 and len(P.ORACLES) == 6
    assert set(P.HELPERS) == set(CURRENT) and len(P.HELPERS) == 12
    for path in P.ORACLES:
        hostile = copy.deepcopy(value)
        hostile["oracles"][path] = "0" * 64
        assert P.control_issue(hostile, 1, frozen(hostile)) is not None


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
