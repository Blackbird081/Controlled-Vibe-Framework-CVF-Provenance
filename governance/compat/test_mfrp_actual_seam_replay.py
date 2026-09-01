#!/usr/bin/env python3
"""Hostile focused tests for the MFRP P3-R1B actual-seam replay."""

from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

try:
    import mfrp_actual_seam_replay as replay
except ModuleNotFoundError:
    from governance.compat import mfrp_actual_seam_replay as replay


ORACLE = replay.REPO_ROOT / replay.ORACLE_PATH


def _load() -> dict:
    return json.loads(ORACLE.read_text(encoding="utf-8"))


def _bytes(value: dict) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def _sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _validate_mutated(value: dict) -> None:
    raw = _bytes(value)
    required = replay._required_set(value)
    with (
        patch.object(replay, "ORACLE_SHA256", _sha(raw)),
        patch.object(replay, "ORACLE_JCS_SHA256", _sha(replay._jcs_bytes(value))),
        patch.object(replay, "REQUIRED_SET_SHA256", _sha(replay._jcs_bytes(required))),
    ):
        replay.validate_oracle(value, raw)


class TestOracleAdmission(unittest.TestCase):
    def test_frozen_oracle_and_exact_coverage_pass(self) -> None:
        oracle = _load()
        required = replay.validate_oracle(oracle, ORACLE.read_bytes())
        self.assertEqual(19, len(required["requiredCaseIds"]))
        self.assertEqual(18, len(required["requiredFamilies"]))
        self.assertEqual(7, len(required["requiredZeroToleranceClasses"]))

    def test_one_case_cannot_pass(self) -> None:
        oracle = _load()
        oracle["cases"] = oracle["cases"][:1]
        oracle["requiredCaseIds"] = oracle["requiredCaseIds"][:1]
        with self.assertRaisesRegex(ValueError, "exactly 19"):
            _validate_mutated(oracle)

    def test_missing_required_family_fails(self) -> None:
        oracle = _load()
        oracle["requiredFamilies"] = oracle["requiredFamilies"][:-1]
        with self.assertRaisesRegex(ValueError, "family coverage"):
            _validate_mutated(oracle)

    def test_missing_zero_tolerance_class_fails(self) -> None:
        oracle = _load()
        oracle["requiredZeroToleranceClasses"] = oracle["requiredZeroToleranceClasses"][:-1]
        with self.assertRaisesRegex(ValueError, "zero-tolerance coverage"):
            _validate_mutated(oracle)

    def test_source_locator_or_excerpt_drift_fails(self) -> None:
        oracle = _load()
        oracle["cases"][0]["sourceRef"]["locator"] = ""
        with self.assertRaisesRegex(ValueError, "source locator/excerpt drift"):
            _validate_mutated(oracle)

    def test_oracle_identity_drift_fails(self) -> None:
        oracle = _load()
        oracle["profile"] = "drifted"
        with self.assertRaisesRegex(ValueError, "oracle identity drift"):
            replay.validate_oracle(oracle, _bytes(oracle))

    def test_unknown_mutation_fails(self) -> None:
        oracle = _load()
        oracle["cases"][0]["mutation"]["operator"] = "INVENTED_MUTATION"
        with self.assertRaisesRegex(ValueError, "unknown mutation"):
            _validate_mutated(oracle)


class TestActualP2Replay(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = replay.build_ledger(ORACLE, execution_base="test-base")

    def _case(self, case_id: str) -> dict:
        return next(item for item in self.ledger["cases"] if item["caseId"] == case_id)

    def test_digest_tamper_reaches_actual_validator(self) -> None:
        item = self._case("C02")
        self.assertFalse(item["validatorAccepted"])
        self.assertIn("receiptDigest mismatch", item["validatorReason"])
        self.assertTrue(item["validatorReadoutSamePayloadObject"])

    def test_fully_rebound_attacker_remains_structural_gap(self) -> None:
        item = self._case("C07")
        self.assertEqual("NOT_REPRESENTABLE_BY_CURRENT_P2", item["executionDisposition"])
        self.assertFalse(item["predicateSatisfied"])

    def test_fixed_sentinel_is_honestly_observed_and_not_a_real_secret(self) -> None:
        item = self._case("C15")
        self.assertFalse(item["predicateSatisfied"])
        self.assertIn(replay.SECRET_SENTINEL, item["readout"]["exceptions"])
        serialized = replay.ledger_bytes(self.ledger).decode("utf-8")
        for forbidden in ("AWS_SECRET_ACCESS_KEY=", "Bearer ", "-----BEGIN PRIVATE KEY-----"):
            self.assertNotIn(forbidden, serialized)

    def test_real_readout_fields_are_preserved(self) -> None:
        item = self._case("C01")
        self.assertTrue(item["validatorAccepted"])
        self.assertEqual(replay.DETERMINISTIC_PREFLIGHT_COMPLETE, item["readout"]["status"])
        for field in ("receiptIdentity", "notCheckedScope", "limitations", "unclassified", "exceptions", "deterministicResults", "candidateProbes", "claimBoundary"):
            self.assertIn(field, item["readout"])

    def test_zero_totals_fail(self) -> None:
        oracle = _load()
        oracle["cases"] = []
        oracle["requiredCaseIds"] = []
        oracle["requiredFamilies"] = []
        oracle["requiredZeroToleranceClasses"] = []
        with self.assertRaisesRegex(ValueError, "exactly 19"):
            _validate_mutated(oracle)

    def test_runner_cannot_emit_reviewer_outcomes(self) -> None:
        self.assertEqual("REVIEWER_OWNED_NOT_SET", self.ledger["reviewerDisposition"])
        self.assertFalse(
            replay.FORBIDDEN_REVIEWER_OUTCOMES.intersection(replay._walk_strings(self.ledger))
        )

    def test_owner_files_are_byte_identical_before_after(self) -> None:
        before = {path: replay._sha_file(replay.REPO_ROOT / path) for path in replay.OWNER_HASHES}
        replay.build_ledger(ORACLE, execution_base="test-base")
        after = {path: replay._sha_file(replay.REPO_ROOT / path) for path in replay.OWNER_HASHES}
        self.assertEqual(before, after)
        self.assertEqual(replay.OWNER_HASHES, after)

    def test_repeated_same_base_is_byte_identical(self) -> None:
        first = replay.ledger_bytes(replay.build_ledger(ORACLE, execution_base="same-base"))
        second = replay.ledger_bytes(replay.build_ledger(ORACLE, execution_base="same-base"))
        self.assertEqual(first, second)

    def test_all_typed_mutations_are_consumed_and_change_bytes(self) -> None:
        cases = {case["caseId"]: case for case in _load()["cases"]}
        for case_id, case in cases.items():
            if case_id in replay.NON_REPRESENTABLE:
                continue
            receipt = replay._canonical_receipt()
            changed = replay.apply_mutation(receipt, case)
            self.assertEqual(case["mutation"]["operator"] != "NO_MUTATION", changed, case_id)

    def test_normative_label_cannot_manufacture_observation(self) -> None:
        case = copy.deepcopy(_load()["cases"][0])
        case["requiredSafetyPredicate"] = "REPLAY_PASS"
        observation = replay.observe_receipt(replay._canonical_receipt())
        with self.assertRaisesRegex(ValueError, "unknown predicate"):
            replay.evaluate_predicate(case, observation)

    def test_weakened_evaluator_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "negative calibration"):
            replay.assert_evaluator_conformance(lambda _case, _observation: True)

    def test_complete_ledger_reconciles_and_returns_to_design_candidate(self) -> None:
        coverage = self.ledger["coverage"]
        self.assertEqual((19, 18, 7), (
            coverage["observedCaseCount"], coverage["observedFamilyCount"],
            coverage["observedZeroToleranceClassCount"],
        ))
        self.assertEqual(["C07", "C08", "C15", "C18"], self.ledger["predicateMissCaseIds"])
        self.assertEqual(
            "REPLAY_EVIDENCE_COMPLETE_RETURN_TO_DESIGN_CANDIDATE",
            self.ledger["workerTerminalCandidate"],
        )

    def test_cli_write_is_only_requested_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "ledger.json"
            output.write_bytes(replay.ledger_bytes(self.ledger))
            self.assertEqual([output], list(Path(temp_dir).iterdir()))


if __name__ == "__main__":
    unittest.main()
