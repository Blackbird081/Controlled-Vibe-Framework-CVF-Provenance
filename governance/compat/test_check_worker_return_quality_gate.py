#!/usr/bin/env python3
"""Focused tests for the worker-return quality gate."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


_COMPAT_DIR = Path(__file__).resolve().parent
_MODULE_PATH = _COMPAT_DIR / "check_worker_return_quality_gate.py"
_STANDARD_PATH = (
    _COMPAT_DIR.parents[1]
    / "docs"
    / "reference"
    / "work_order_authoring"
    / "CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md"
)
_SPEC = importlib.util.spec_from_file_location("check_worker_return_quality_gate", _MODULE_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError(f"Unable to load module from {_MODULE_PATH}")
chk = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = chk
_SPEC.loader.exec_module(chk)


VALID_RETURN = """# Worker Return
Status: COMPLETE_PENDING_REVIEW
Self-declared worker-return artifact: yes
Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_X_2026-07-01.md`
dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_X_2026-07-01.md`
executionBaseHead: abc1234
## Purpose
Implemented the bounded work.
## Scope / Methodology
Read source and ran focused tests.
## Findings / Position
Review-ready with evidence.
## Risk / Corrective Action
No unresolved risk.
## Checker Source Read-Ahead Block
| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `CLAIM_REJECTED_NO_RECEIPT`; `WORKER_MUST_NOT_COMMIT honored`; `Agent Operation Trace Block` |
| gateRunPurpose | confirmation/evidence before return |
| claimBoundary | worker-return quality shape only |
## Agent Operation Trace Block
| Field | Evidence |
| --- | --- |
| Actor | worker |
| Provider or surface | local workspace |
| Session or invocation | X, 2026-07-01 |
| Working directory | repository root |
| Command or tool surface | shell |
| Target paths | helper, test, worker return |
| Allowed scope source | work order |
| Before status evidence | `git status --short` before |
| After status evidence | `git status --short` after |
| Diff evidence | `git diff --name-status` |
| Approval boundary | worker no-commit |
| Claim boundary | no runtime claim |
| Agent type | worker |
| Invocation ID | `x-2026-07-01` |
| Expected manifest | helper; test; worker return |
| Actual changed set | helper; test; worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason |
## Delta Execution Claim Boundary Control Block
| Field | Value |
| --- | --- |
| claimScope | worker return only |
| claimDisposition | CLAIM_REJECTED |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | manual local command only |
| interceptionBoundary | no wrapper/proxy enforcement |
| claimLanguage | helper/test evidence only |
| forbiddenExpansion | no runtime/provider/public expansion |
## Public Export Disposition
DEFERRED_PRIVATE_ONLY
Reason: private worker return.
## External Knowledge Intake Routing
| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: not external intake |
| Matching local-view guard | N/A with reason |
| Owner surface | worker return |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external intake |
## Rescan Intelligence Hardening
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
## Corpus Completeness And Report Integrity
- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus scan.
## Finding-To-Governance Learning Disposition
| Field | Value |
| --- | --- |
| Defect class | N/A_WITH_REASON: no defect |
| Learning lane | N/A_WITH_REASON: no learning |
| Finding | none |
| Disposition | N/A_WITH_REASON - none |
| Runtime/provider/cost lane | N/A_WITH_REASON: none |
| Next control action | none |
## Epistemic Process Block
- Expected result / prediction: pass
- Evidence Comparison: pass
- Contradiction or gap disposition: none
- Claim update: bounded
## Claim Boundary
No runtime claim.
## git status --short
```
 M helper.py
?? docs/reviews/x.md
```
## Changed Files
`git diff --name-status` -> PASS
## Command Evidence
`python -m unittest x` -> PASS
## No-Commit Statement
WORKER_MUST_NOT_COMMIT honored: HEAD unchanged; no git commit performed by worker.
"""


class EligibilityTests(unittest.TestCase):
    def test_valid_return_is_eligible(self) -> None:
        self.assertTrue(chk.is_eligible_worker_return("docs/reviews/CVF_X_WORKER_RETURN.md", VALID_RETURN))

    def test_completion_review_is_excluded(self) -> None:
        self.assertFalse(chk.is_eligible_worker_return("docs/reviews/CVF_X_COMPLETION_2026-07-01.md", VALID_RETURN))

    def test_reference_outside_reviews_is_excluded(self) -> None:
        self.assertFalse(chk.is_eligible_worker_return("docs/reference/x.md", VALID_RETURN))


class DiagnoseTests(unittest.TestCase):
    def test_valid_return_is_clean(self) -> None:
        d = chk.diagnose("docs/reviews/CVF_X_WORKER_RETURN.md", VALID_RETURN)
        self.assertTrue(d.is_clean, d.issues)

    def test_unresolved_fill_me_fails(self) -> None:
        d = chk.diagnose("docs/reviews/CVF_X_WORKER_RETURN.md", VALID_RETURN + "\nFILL_ME\n")
        self.assertFalse(d.is_clean)
        self.assertTrue(any("FILL_ME" in issue for issue in d.issues))

    def test_missing_self_declaration_fails(self) -> None:
        text = VALID_RETURN.replace("Self-declared worker-return artifact: yes\n", "")
        d = chk.diagnose("docs/reviews/CVF_X_WORKER_RETURN.md", text)
        self.assertFalse(d.is_clean)
        self.assertTrue(any("Self-declared worker-return artifact" in issue for issue in d.issues))

    def test_missing_checker_source_fails(self) -> None:
        text = VALID_RETURN.replace("governance/compat/check_worker_return_quality_gate.py", "worker quality gate")
        text = text.replace("governance/compat/check_delta_execution_claim_boundary.py", "delta gate")
        d = chk.diagnose("docs/reviews/CVF_X_WORKER_RETURN.md", text)
        self.assertFalse(d.is_clean)
        self.assertTrue(any("does not name any" in issue for issue in d.issues))

    def test_missing_delta_receipt_token_fails(self) -> None:
        text = VALID_RETURN.replace("CLAIM_REJECTED_NO_RECEIPT", "no receipt")
        d = chk.diagnose("docs/reviews/CVF_X_WORKER_RETURN.md", text)
        self.assertFalse(d.is_clean)
        self.assertTrue(any("receipt evidence token" in issue for issue in d.issues))

    def test_command_evidence_without_disposition_fails(self) -> None:
        text = VALID_RETURN.replace("`python -m unittest x` -> PASS", "`python -m unittest x`")
        d = chk.diagnose("docs/reviews/CVF_X_WORKER_RETURN.md", text)
        self.assertFalse(d.is_clean)
        self.assertTrue(any("command evidence" in issue for issue in d.issues))

    def test_noncanonical_external_input_fails(self) -> None:
        text = VALID_RETURN.replace(
            "operator-provided external comparison, critique, or recommendation",
            "N/A with reason",
        )
        d = chk.diagnose("docs/reviews/CVF_X_WORKER_RETURN.md", text)
        self.assertFalse(d.is_clean)
        self.assertTrue(any("canonical" in issue for issue in d.issues))


class StandardParityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard_text = _STANDARD_PATH.read_text(encoding="utf-8")

    def test_standard_lists_all_required_headings(self) -> None:
        for heading in chk.REQUIRED_HEADINGS:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.standard_text)

    def test_standard_lists_checker_field_constants(self) -> None:
        for label in (
            *chk.READ_AHEAD_FIELDS,
            *chk.AOT_FIELDS,
            *chk.DELTA_FIELDS,
        ):
            with self.subTest(label=label):
                self.assertIn(label, self.standard_text)

    def test_standard_lists_canonical_tokens(self) -> None:
        expected_tokens = (
            *chk.PLACEHOLDER_MARKERS,
            chk.EXTERNAL_INPUT_CANONICAL,
            *chk.DELTA_RECEIPT_TOKENS,
            *chk.DELTA_ACTION_TOKENS,
            *chk.PUBLIC_EXPORT_TOKENS,
            "WORKER_MUST_NOT_COMMIT honored",
            "--base <executionBaseHead> --head HEAD --enforce",
            "confirmation/evidence",
        )
        for token in expected_tokens:
            with self.subTest(token=token):
                self.assertIn(token, self.standard_text)


if __name__ == "__main__":
    unittest.main()
