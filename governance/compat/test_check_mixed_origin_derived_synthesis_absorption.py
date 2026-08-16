from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().with_name("check_mixed_origin_derived_synthesis_absorption.py")
SPEC = importlib.util.spec_from_file_location("check_mixed_origin_derived_synthesis_absorption", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


VALID = """
# Corrective assessment

Mixed-origin derived synthesis: REQUIRED

## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE
authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
|---|---|---|---|---|---|---|
| environment snapshot | MIXED_ORIGIN | operator attestation plus source paths | design | owner review and tests | docs/reference/example.md | ADAPT_CANDIDATE |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
|---|---|---|---|
| Knowledge absorption | PROCEED_SELECTIVELY | contracts add value | documentation cost |
| Direct import | REJECT_DIRECT_IMPORT | authority mismatch | no copy |
| Runtime activation | DEFER | tests absent | runtime cost evaluated separately |
| Authority promotion | REVIEW_REQUIRED | candidate only | review cost |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
|---|---|---|---|---|---|
| snapshot | docs/reference/example.md | owner gap | ADAPT_CANDIDATE | UNPROVEN | open bounded work order |

## Absorption Efficiency And Provenance Reuse

manifestLedgerReuse: REUSE_IF_FRESH
semanticReviewUnit: CAPABILITY_CLUSTER
defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED
additionalValueProbe: SKIP_UNLESS_NAMED_GAP
latencyBudget: SINGLE_PASS_BOUNDED
"""


class MixedOriginDerivedSynthesisTests(unittest.TestCase):
    def check(self, text: str):
        return MODULE.check_text("docs/assessments/CVF_SAMPLE.md", text)

    def test_valid_artifact_passes(self) -> None:
        self.assertEqual([], self.check(VALID))

    def test_missing_origin_evidence_fails(self) -> None:
        text = VALID.replace("## Mixed-Origin Derived Synthesis Provenance", "## Removed")
        self.assertTrue(any(v["type"] == "mixed_origin_required_marker_missing" for v in self.check(text)))

    def test_unknown_origin_class_fails(self) -> None:
        text = VALID.replace("MIXED_ORIGIN", "SECONDARY_PROPOSAL_ONLY")
        self.assertTrue(any(v["type"] == "mixed_origin_origin_class_invalid" for v in self.check(text)))

    def test_collapsed_decision_vector_fails(self) -> None:
        text = VALID.replace("| Runtime activation | DEFER | tests absent | runtime cost evaluated separately |", "")
        self.assertTrue(any(v["type"] == "mixed_origin_decision_axis_missing" for v in self.check(text)))

    def test_missing_system_chain_fails(self) -> None:
        text = VALID.replace("## System-Chain Value Review", "## Removed Chain")
        self.assertTrue(any(v["type"] == "mixed_origin_required_marker_missing" for v in self.check(text)))

    def test_maturity_as_value_fails(self) -> None:
        text = VALID + "\nUNMERGED therefore STOP_COST_EXCEEDS_VALUE\n"
        self.assertTrue(any(v["type"] == "mixed_origin_maturity_used_as_value" for v in self.check(text)))

    def test_missing_efficiency_section_fails(self) -> None:
        text = VALID.replace("## Absorption Efficiency And Provenance Reuse", "## Removed Efficiency")
        self.assertTrue(any(v["type"] == "mixed_origin_required_marker_missing" for v in self.check(text)))

    def test_per_file_semantic_review_unit_fails(self) -> None:
        text = VALID.replace("semanticReviewUnit: CAPABILITY_CLUSTER", "semanticReviewUnit: PER_FILE")
        self.assertTrue(any(v["type"] == "mixed_origin_efficiency_control_invalid" for v in self.check(text)))

    def test_unbounded_reprobe_fails(self) -> None:
        text = VALID.replace("additionalValueProbe: SKIP_UNLESS_NAMED_GAP", "additionalValueProbe: ALWAYS_REPROBE")
        self.assertTrue(any(v["type"] == "mixed_origin_efficiency_control_invalid" for v in self.check(text)))

    def test_named_gap_reprobe_is_allowed(self) -> None:
        text = VALID.replace("additionalValueProbe: SKIP_UNLESS_NAMED_GAP", "additionalValueProbe: REQUIRED_WITH_NAMED_GAP")
        self.assertEqual([], self.check(text))

    def test_unrelated_doc_is_ignored(self) -> None:
        self.assertEqual([], MODULE.check_text("docs/assessments/CVF_OTHER.md", "# Other"))


if __name__ == "__main__":
    unittest.main()
