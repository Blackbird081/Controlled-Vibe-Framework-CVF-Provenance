"""Focused tests: the rehearsal's classification oracle must discriminate mutants and classify controls.

They exercise oracle discrimination and injection hygiene; they do not assert that any product behavior
is safe, and they do not repeat the accepted ledger suite.
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe_cvf_q001_sqlite_migration_recovery_rehearsal as P  # noqa: E402

STATES = {"CLEAN_ABSENT", "SIDECAR_ONLY", "PARTIAL_OPENABLE_INCOMPLETE", "PARTIAL_UNOPENABLE", "USABLE_COMPLETE"}


@pytest.fixture()
def ctx():
    with P.DisposableRoot() as root:
        yield root


def test_controls_classify_as_declared_and_mutants_are_rejected(ctx):
    result = P.oracle_selfcheck(ctx)
    assert all(c["ok"] for c in result["controls"].values()), result["controls"]
    assert all(m["rejected"] for m in result["mutants"].values()), result["mutants"]
    assert result["mutants"]["leavesPartialTarget"]["naiveExceptionOnlyOracleAccepts"]
    assert result["allRejectedAndClassified"]


def test_weak_target_exists_oracle_would_accept_short_chain_but_classifier_does_not(ctx):
    d, chain = ctx.fresh("weak"), P.build_chain(P.N, "weak")
    src, target = d / "source.json", d / "target.sqlite"
    P.write_json(src, chain)
    assert P.mutant_import_short_chain(src, target)["count"] == P.N
    assert target.exists()
    state = P.classify(target, chain, ctx.scratch)
    assert (state["state"], state["reason"]) == ("PARTIAL_OPENABLE_INCOMPLETE", "SHORT_CHAIN")


def test_digest_rule_separates_raw_only_change_from_logical_change():
    base = {"raw": "1", "logical": "L", "sidecars": []}
    assert P.compare_snap(base, dict(base))["verdict"] == "UNCHANGED"
    assert P.compare_snap(base, {**base, "raw": "2"})["verdict"] == "RAW_CHANGED_LOGICAL_EQUAL"
    assert P.compare_snap(base, {**base, "logical": "M"})["verdict"] == "LOGICAL_DIGEST_CHANGED"


@pytest.mark.parametrize("raised,state,expected", [
    (True, "CLEAN_ABSENT", "CLEAN_ABSENT_AFTER_RAISE"),
    (True, "PARTIAL_OPENABLE_INCOMPLETE", "PARTIAL_TARGET_FINDING"),
    (True, "PARTIAL_UNOPENABLE", "PARTIAL_TARGET_FINDING"),
    (True, "USABLE_COMPLETE", "COMPLETE_BUT_REPORTED_FAILED_FINDING"),
    (True, "SIDECAR_ONLY", "SIDECAR_RESIDUE_FINDING"),
    (False, "USABLE_COMPLETE", "SUCCESS_CORRECT_STATE"),
    (False, "PARTIAL_OPENABLE_INCOMPLETE", "SUCCESS_WRONG_STATE_FINDING"),
])
def test_outcome_tags_are_observation_labels(raised, state, expected):
    assert P.tag_outcome(raised, state, {})[0] == expected


def test_real_peer_barrier_orders_events_and_early_entry_mutant_is_rejected(ctx):
    d, chain = ctx.fresh("peer"), P.build_chain(P.N, "peer")
    ok = P.run_barrier_peer(P.product_sqlite(d, "ok", chain), "peer-ok")
    assert [name for name, _ in ok["events"]] == ["READY", "START_ATTEMPT", "ATTEMPTING", "PARENT_RELEASE", "ENTERED", "COMPLETE"]
    assert ok["orderVerdict"] == "ORDER_OK" and ok["peerExit"] == 0 and ok["enteredNs"] >= ok["releaseNs"]
    bad = P.run_barrier_peer(P.product_sqlite(d, "bad", chain), "peer-bad", early=True)
    assert bad["orderVerdict"] == "REJECT_ENTRY_BEFORE_PARENT_RELEASE"


def test_positive_round_trip_records_chain_equality(ctx):
    records = P.scen_positive(ctx)
    assert records[-1]["literal"] == "ROUNDTRIP_CHAIN_EQUAL" and records[-1]["ok"] is True
    assert all(r["targetState"]["state"] == "USABLE_COMPLETE" for r in records[:3])


def test_import_fault_records_are_complete_and_injection_is_restored(ctx):
    original_connect, original_path = P.LEDGER._connect, P.SL.Path
    records = P.scen_import(ctx)
    assert P.LEDGER._connect is original_connect and P.SL.Path is original_path
    assert {r["scenarioId"] for r in records} == {"RH-IMP-F1", "RH-IMP-F2", "RH-IMP-F3", "RH-IMP-F4"}
    for rec in records:
        assert rec["outcome"]["returnedOrRaised"] in ("RAISED", "RETURNED")
        assert rec["targetState"]["state"] in STATES
        assert set(rec["digests"]["verdicts"]) == {"source"} and rec["tag"] and "retry" in rec
