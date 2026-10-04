#!/usr/bin/env python3
"""Regression tests for worker-return scaffold friction repair (WRS-FR1)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

REPO_ROOT = Path(__file__).resolve().parents[2]
COMPAT_DIR = Path(__file__).resolve().parent
if str(COMPAT_DIR) not in sys.path:
    sys.path.insert(0, str(COMPAT_DIR))

import build_worker_return_skeleton_scaffold as bws
import check_review_cost_control as crcc
import check_work_order_acceptance_ledger as cwoal
import check_worker_experience_retrospective as cwer
import run_worker_return_scaffold as rws

SYNTHETIC_WORK_ORDER = """# Work Order
docType: work_order

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{
  "schemaVersion": "cvf.workOrderAcceptanceLedger@1.0.0",
  "requirements": [
    {
      "requirementId": "REQ-1",
      "mandatory": true,
      "expectedArtifacts": ["docs/reviews/sample_return.md"],
      "requiredProofIds": ["PROOF-1"]
    }
  ],
  "proofCatalog": [
    {"proofId": "PROOF-1", "kind": "COMMAND", "locator": "python -m unittest"}
  ]
}
```
"""


def _make_scaffold_args(profile: str = rws.FULL_PROFILE) -> SimpleNamespace:
    return SimpleNamespace(
        batch_id="CVF-TEST-FR1",
        title="Test Friction Repair",
        date="2026-10-04",
        base="438ee56b093b732b6b5ea01a8e27c1fa0c084d96",
        commit_mode="WORKER_MUST_NOT_COMMIT",
        worker_return_profile=profile,
        include_p4_observation_block=True,
        include_architecture_readiness_echo=True,
        evidence_readiness_applicable=False,
    )


class WorkerReturnScaffoldFrictionTests(unittest.TestCase):
    def test_raw_scaffold_guidance_present_in_both_generators(self) -> None:
        generators = [
            ("run_full", rws.build_scaffold("Test Return", rws.FULL_PROFILE)),
            ("run_fast", rws.build_scaffold("Test Fast", rws.FAST_DOC_PROFILE)),
            ("build_full", bws.build_worker_return_skeleton(_make_scaffold_args(rws.FULL_PROFILE))),
            ("build_fast", bws.build_worker_return_skeleton(_make_scaffold_args(rws.FAST_DOC_PROFILE))),
        ]
        for name, text in generators:
            with self.subTest(generator=name):
                self.assertIn("Evidence completion guidance:", text)
                self.assertIn("Readiness completion guidance:", text)
                self.assertIn("requirementId", text)
                self.assertIn("actualArtifacts", text)
                self.assertIn("proofRefs", text)
                self.assertIn("status (PASS or BLOCKED)", text)
                self.assertIn("WORKER_EXPERIENCE_RETRO:", text)
                self.assertIn("frictionLevel: TO_FILL_FROM_ACTUAL_EXECUTION", text)
                self.assertIn("frictionType: TO_FILL_FROM_ACTUAL_EXECUTION", text)
                self.assertIn("observedStep: TO_FILL_FROM_ACTUAL_EXECUTION", text)
                self.assertIn("preventiveControlCandidate: TO_FILL_FROM_ACTUAL_EXECUTION", text)

    def test_raw_scaffolds_remain_fail_closed_before_completion(self) -> None:
        generators = [
            ("run_full", rws.build_scaffold("Test Return", rws.FULL_PROFILE)),
            ("run_fast", rws.build_scaffold("Test Fast", rws.FAST_DOC_PROFILE)),
            ("build_full", bws.build_worker_return_skeleton(_make_scaffold_args(rws.FULL_PROFILE))),
            ("build_fast", bws.build_worker_return_skeleton(_make_scaffold_args(rws.FAST_DOC_PROFILE))),
        ]
        for name, text in generators:
            with self.subTest(generator=name):
                ledger_issues = cwoal.validate_return(SYNTHETIC_WORK_ORDER, text)
                self.assertTrue(any("missing evidence row" in i or "results" in i for i in ledger_issues))
                retro_diag = cwer.diagnose("docs/reviews/sample_return.md", text)
                self.assertTrue(retro_diag.eligible)
                self.assertFalse(retro_diag.is_clean)
                self.assertTrue(any("invalid frictionLevel" in i for i in retro_diag.issues))

    def test_completed_acceptance_rows_and_ready_for_review_pass(self) -> None:
        base_text = rws.build_scaffold("Sample Return", rws.FULL_PROFILE)
        return_text = (
            base_text.replace("Status: TODO_WORKER_STATUS", "Status: COMPLETE_PENDING_REVIEW")
            .replace(
                '{"schemaVersion":"cvf.workOrderAcceptanceEvidence@1.0.0","executionBaseHead":"TO_FILL","results":[]}',
                '{"schemaVersion":"cvf.workOrderAcceptanceEvidence@1.0.0","executionBaseHead":"438ee56b093b732b",'
                '"results":[{"requirementId":"REQ-1","actualArtifacts":["docs/reviews/sample_return.md"],'
                '"proofRefs":["PROOF-1"],"status":"PASS"}]}',
            )
            .replace("rootCauseClusterId: INITIAL_SCOPE_PENDING_WORK_ORDER_BINDING", "rootCauseClusterId: CVF-TEST-FR1")
            .replace("consolidatedDefectClassSweep: PENDING_BEFORE_READY", "consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES")
            .replace("productionBindingEvidence: PENDING_BEFORE_READY", "productionBindingEvidence: VERIFIED_SOURCE_TEST_EVIDENCE")
            .replace("adversarialRegressionDisposition: PENDING_BEFORE_READY", "adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS")
            .replace("terminalReadinessVerdict: BLOCKED_WITH_REASON: generated scaffold pending worker evidence", "terminalReadinessVerdict: READY_FOR_REVIEW")
            .replace("frictionLevel: TO_FILL_FROM_ACTUAL_EXECUTION", "frictionLevel: LOW")
            .replace("frictionType: TO_FILL_FROM_ACTUAL_EXECUTION", "frictionType: KEYWORD_TRAP")
            .replace("observedStep: TO_FILL_FROM_ACTUAL_EXECUTION", "observedStep: scaffold guidance verification")
            .replace("preventiveControlCandidate: TO_FILL_FROM_ACTUAL_EXECUTION", "preventiveControlCandidate: WORK_ORDER_TEMPLATE")
        )
        ledger_issues = cwoal.validate_return(SYNTHETIC_WORK_ORDER, return_text, {"docs/reviews/sample_return.md"})
        self.assertEqual(ledger_issues, [])
        cost_diag = crcc.diagnose_worker_return("docs/reviews/sample_return.md", return_text)
        self.assertTrue(cost_diag.is_clean, cost_diag.issues)
        retro_diag = cwer.diagnose("docs/reviews/sample_return.md", return_text)
        self.assertTrue(retro_diag.is_clean, retro_diag.issues)

    def test_unknown_readiness_token_and_wrong_row_keys_refuse(self) -> None:
        base_text = rws.build_scaffold("Sample Return", rws.FULL_PROFILE)
        wrong_keys_text = base_text.replace(
            '"results":[]',
            '"results":[{"requirementId":"REQ-1","artifacts":["docs/reviews/sample_return.md"],'
            '"proofs":["PROOF-1"],"status":"PASS"}]',
        )
        ledger_issues = cwoal.validate_return(SYNTHETIC_WORK_ORDER, wrong_keys_text)
        self.assertTrue(any("each evidence row must contain exactly" in i for i in ledger_issues))

        bad_ready_text = base_text.replace(
            "terminalReadinessVerdict: BLOCKED_WITH_REASON: generated scaffold pending worker evidence",
            "terminalReadinessVerdict: READY",
        )
        cost_diag = crcc.diagnose_worker_return("docs/reviews/sample_return.md", bad_ready_text)
        self.assertTrue(any("terminalReadinessVerdict" in i for i in cost_diag.issues))

        incomplete_ready = (
            base_text.replace("rootCauseClusterId: INITIAL_SCOPE_PENDING_WORK_ORDER_BINDING", "rootCauseClusterId: CVF-TEST-FR1")
            .replace("consolidatedDefectClassSweep: PENDING_BEFORE_READY", "consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES")
            .replace("adversarialRegressionDisposition: PENDING_BEFORE_READY", "adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS")
            .replace("terminalReadinessVerdict: BLOCKED_WITH_REASON: generated scaffold pending worker evidence", "terminalReadinessVerdict: READY_FOR_REVIEW")
        )
        cost_diag_incomplete = crcc.diagnose_worker_return("docs/reviews/sample_return.md", incomplete_ready)
        self.assertTrue(any("pending production-binding evidence" in i for i in cost_diag_incomplete.issues))

    def test_truthful_no_friction_na_and_structured_retro_forms_pass(self) -> None:
        header = "# Return\nStatus: COMPLETE_PENDING_REVIEW\nResponds to work order: docs/work_orders/x.md\n\n"
        na_text = (
            header
            + f"WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: {cwer.RETRO_NA_REQUIRED_REASON}\n"
        )
        d_na = cwer.diagnose("docs/reviews/sample_return.md", na_text)
        self.assertTrue(d_na.is_clean, d_na.issues)

        struct_text = (
            header
            + "WORKER_EXPERIENCE_RETRO:\n"
            + "frictionLevel: LOW\n"
            + "frictionType: KEYWORD_TRAP\n"
            + "observedStep: scaffold guidance verification\n"
            + "preventiveControlCandidate: WORK_ORDER_TEMPLATE\n"
        )
        d_struct = cwer.diagnose("docs/reviews/sample_return.md", struct_text)
        self.assertTrue(d_struct.is_clean, d_struct.issues)

    def test_wrong_na_reason_and_duplicate_retro_declarations_refuse(self) -> None:
        header = "# Return\nStatus: COMPLETE_PENDING_REVIEW\nResponds to work order: docs/work_orders/x.md\n\n"
        wrong_na = header + "WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction observed\n"
        d_wrong = cwer.diagnose("docs/reviews/sample_return.md", wrong_na)
        self.assertFalse(d_wrong.is_clean)
        self.assertTrue(any("exact asserting reason" in i for i in d_wrong.issues))

        duplicate_text = (
            header
            + f"WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: {cwer.RETRO_NA_REQUIRED_REASON}\n\n"
            + "WORKER_EXPERIENCE_RETRO:\n"
            + "frictionLevel: LOW\n"
            + "frictionType: KEYWORD_TRAP\n"
            + "observedStep: x\n"
            + "preventiveControlCandidate: WORK_ORDER_TEMPLATE\n"
        )
        d_dup = cwer.diagnose("docs/reviews/sample_return.md", duplicate_text)
        self.assertFalse(d_dup.is_clean)
        self.assertTrue(any("multiple worker-experience tokens" in i for i in d_dup.issues))


if __name__ == "__main__":
    unittest.main()
