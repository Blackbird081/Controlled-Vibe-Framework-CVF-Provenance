#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().with_name("check_work_order_dispatch_quality.py")
SPEC = importlib.util.spec_from_file_location("check_work_order_dispatch_quality", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load module from {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class WorkOrderDispatchQualityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temp_dir.name)
        self._seed_required_markers()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _write(self, rel_path: str, text: str) -> None:
        path = self.repo_root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _seed_required_markers(self) -> None:
        self._write(
            MODULE.STANDARD_PATH,
            "\n".join(
                [
                    "Roadmap-To-Work-Order Trace Matrix",
                    "Negative And Fail-Condition Scan",
                    MODULE.THIS_SCRIPT_PATH,
                ]
            ),
        )
        self._write(
            MODULE.WORK_ORDER_TEMPLATE_PATH,
            "\n".join(
                [
                    "Source Verification Block",
                    "Roadmap-To-Work-Order Trace Matrix",
                    MODULE.THIS_SCRIPT_PATH,
                ]
            ),
        )
        self._write(MODULE.HOOK_CHAIN_PATH, MODULE.THIS_SCRIPT_PATH)

    def test_lhw6_dispatch_without_gc018_and_trace_matrix_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW6_T1_TEST_2026-05-28.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCHED",
                    "Authority: docs/roadmaps/CVF_LHW6_TEST_ROADMAP_2026-05-28.md",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| Symbol | `governance/contracts/example.ts` | line 1 | `ExampleMode` | ExampleMode | ACCEPT |",
                ]
            ),
        )
        self._write("governance/contracts/example.ts", "export type ExampleMode = 'one';\n")

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        issues = report["violations"][0]["issues"]
        self.assertIn("roadmap-derived work order is dispatch/ready without Roadmap-To-Work-Order Trace Matrix", issues)
        self.assertIn("LHW6 connector work order is dispatch/ready without fresh GC-018 baseline", issues)

    def test_fast_lane_ready_with_closed_pass_precondition_fails(self) -> None:
        audit = "docs/reviews/CVF_LHW6_T2_FAST_LANE_AUDIT_2026-05-28.md"
        self._write(
            audit,
            "\n".join(
                [
                    "# Audit",
                    "Status: FAST_LANE_READY",
                    "Decision: FAST_LANE_READY (pre-condition: T1 CLOSED_PASS)",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([audit])

        self.assertFalse(report["compliant"])
        issues = report["violations"][0]["issues"]
        self.assertIn("FAST_LANE_READY audit has unmet/conditional CLOSED_PASS prerequisite; use HOLD_* until satisfied", issues)

    def test_accept_row_with_missing_source_file_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW6_T2_TEST_2026-05-28.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_PENDING_T1",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| Future values | `docs/reference/CVF_LHW6_MISSING_SPEC.md` | S3 | `bridgeAdvisoryType` | BridgeSpec | ACCEPT |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "Source Verification ACCEPT cites missing source file `docs/reference/CVF_LHW6_MISSING_SPEC.md`",
            report["violations"][0]["issues"],
        )

    def test_accept_value_row_missing_declared_source_value_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW6_T3_TEST_2026-05-28.md"
        self._write(
            "governance/contracts/workflow.ts",
            "\n".join(
                [
                    "export type WorkflowRecoveryAction =",
                    "  | 'resume_from_checkpoint'",
                    "  | 'request_human_review';",
                ]
            ),
        )
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_PENDING_T1_T2",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| WorkflowRecoveryAction values `resume_from_checkpoint` | `governance/contracts/workflow.ts` | lines 1-3 | `WorkflowRecoveryAction` | WorkflowRecoveryAction | ACCEPT |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "Source Verification ACCEPT row claims values for `WorkflowRecoveryAction` but omits source value(s): request_human_review",
            report["violations"][0]["issues"],
        )

    def test_compliant_hold_packet_passes(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW6_T1_TEST_2026-05-28.md"
        self._write(
            "governance/contracts/example.ts",
            "export type ExampleMode = 'one' | 'two';\n",
        )
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_PENDING_GC018",
                    "Authority: docs/roadmaps/CVF_LHW6_TEST_ROADMAP_2026-05-28.md",
                    "## Roadmap-To-Work-Order Trace Matrix",
                    "| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |",
                    "|---|---|---|---|---|",
                    "| R1 | S1 | field | check | BLOCKED |",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| ExampleMode values `one` `two` | `governance/contracts/example.ts` | line 1 | `ExampleMode` | ExampleMode | ACCEPT |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertTrue(report["compliant"])

    def test_hold_status_with_closed_token_fails_without_closed_finality(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW11_T2_TEST_2026-05-29.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_UNTIL_T1_CLOSED_PASS",
                    "## Roadmap-To-Work-Order Trace Matrix",
                    "| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |",
                    "|---|---|---|---|---|",
                    "| R1 | S1 | field | check | OPEN |",
                    "## Closure Checklist",
                    "- [ ] Keep blocked until T1 passes",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        issues = report["violations"][0]["issues"]
        self.assertIn(
            "work order hold/draft/proposed status must not contain `CLOSED`; "
            "use PASS or SATISFIED wording for prerequisite status tokens",
            issues,
        )
        self.assertNotIn("closed work order contains 1 table row(s) still marked OPEN", issues)
        self.assertNotIn("closed work order contains 1 unchecked checklist item(s)", issues)

    def test_source_verification_symbol_assignment_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW11_T1_TEST_2026-05-29.md"
        self._write(
            "governance/contracts/memory.ts",
            "export interface MemoryReceipt { rawMemoryReleased: boolean; }\n",
        )
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_PENDING_T1",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| LITERAL_INVARIANT rawMemoryReleased false | `governance/contracts/memory.ts` | line 1 | `rawMemoryReleased: false` | MemoryReceipt | ACCEPT |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        issues = report["violations"][0]["issues"]
        self.assertIn(
            "Source Verification `Verified path or symbol` must contain only a field/path/symbol, "
            "not a value assignment or type annotation",
            issues,
        )
        self.assertNotIn(
            "Source Verification ACCEPT row claims a false invariant for `false` but "
            "`governance/contracts/memory.ts` does not declare or assign that field as literal false",
            issues,
        )

    def test_source_verification_symbol_type_annotation_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW11_T3_TEST_2026-05-29.md"
        self._write(
            "governance/contracts/memory.ts",
            "export interface MemoryReceipt { canReinject: boolean; }\n",
        )
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_PENDING_T3",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| EXISTS canReinject field | `governance/contracts/memory.ts` | line 1 | `canReinject: boolean` | MemoryReceipt | ACCEPT |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "Source Verification `Verified path or symbol` must contain only a field/path/symbol, "
            "not a value assignment or type annotation",
            report["violations"][0]["issues"],
        )

    def test_closed_work_order_with_open_rows_and_unchecked_boxes_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW10_T1_TEST_2026-05-28.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: CLOSED_PASS_BOUNDED",
                    "## Roadmap-To-Work-Order Trace Matrix",
                    "| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |",
                    "|---|---|---|---|---|",
                    "| R1 | S1 | field | check | OPEN |",
                    "## Closure Checklist",
                    "- [ ] Spec complete",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        issues = report["violations"][0]["issues"]
        self.assertIn("closed work order contains 1 table row(s) still marked OPEN", issues)
        self.assertIn("closed work order contains 1 unchecked checklist item(s)", issues)

    def test_closed_roadmap_with_hold_residue_fails(self) -> None:
        roadmap = "docs/roadmaps/CVF_LHW10_TEST_ROADMAP_2026-05-28.md"
        self._write(
            roadmap,
            "\n".join(
                [
                    "# Roadmap",
                    "Status: CLOSED_PASS_BOUNDED",
                    "Dispatch status: T1 WORK_ORDER_READY. T2 HOLD until T1 CLOSED_PASS.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([roadmap])

        self.assertFalse(report["compliant"])
        self.assertTrue(
            any("closed roadmap contains stale dispatch/hold status residue" in issue
                for issue in report["violations"][0]["issues"])
        )

    def test_active_fast_lane_with_pass_disposition_fails(self) -> None:
        audit = "docs/reviews/CVF_LHW10_T3_FAST_LANE_AUDIT_2026-05-28.md"
        self._write(
            audit,
            "\n".join(
                [
                    "# Audit",
                    "Status: ACTIVE",
                    "**Decision: ACCEPT**",
                    "**Disposition: FAST_LANE_PASS**",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([audit])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "fast-lane audit status is still ACTIVE/DRAFT/HOLD while disposition or decision is pass/approve",
            report["violations"][0]["issues"],
        )

    def test_closed_work_order_changed_range_outside_allowed_scope_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW12_T1_TEST_2026-05-29.md"
        spec = "docs/reference/CVF_LHW12_T1_TEST_CONNECTOR_SPEC_2026-05-29.md"
        archive = "docs/reviews/archive/CVF_OLD_REVIEW_2026-05-01.md"
        self._write(spec, "# Spec\nStatus: DRAFT\n")
        self._write(archive, "# Old Review\nStatus: archived\n")
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: CLOSED_PASS_BOUNDED",
                    "## 4. Scope",
                    "Allowed scope:",
                    f"- Create `{spec}`.",
                    "- Update this work order status only.",
                    "- Update session continuity files.",
                    "Forbidden scope:",
                    "- Archive cleanup or unrelated maintenance.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order, spec, archive])

        self.assertFalse(report["compliant"])
        scope_issues = [
            issue
            for violation in report["violations"]
            if violation["path"] == work_order
            for issue in violation["issues"]
        ]
        self.assertTrue(
            any("outside its Allowed scope" in issue and archive in issue for issue in scope_issues)
        )

    def test_closed_lhw_roadmap_requires_full_wave_range_fails(self) -> None:
        roadmap = "docs/roadmaps/CVF_LHW12_TEST_ROADMAP_2026-05-29.md"
        t3_spec = "docs/reference/CVF_LHW12_T3_TEST_CONNECTOR_SPEC_2026-05-29.md"
        self._write("docs/baselines/CVF_GC018_LHW12_TEST_2026-05-29.md", "# GC-018\n")
        self._write(t3_spec, "# T3 Spec\nStatus: DRAFT\n")
        self._write(
            roadmap,
            "\n".join(
                [
                    "# Roadmap",
                    "Status: CLOSED_PASS_BOUNDED",
                    "LHW12 connector wave closure.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([roadmap, t3_spec])

        self.assertFalse(report["compliant"])
        roadmap_issues = [
            issue
            for violation in report["violations"]
            if violation["path"] == roadmap
            for issue in violation["issues"]
        ]
        self.assertIn(
            "closed LHW12 connector roadmap changed without full wave-range evidence; "
            "missing changed artifact(s) for T1, T2",
            roadmap_issues,
        )

    def test_connector_spec_false_line_count_claim_fails(self) -> None:
        spec = "docs/reference/CVF_LHW12_T1_TEST_CONNECTOR_SPEC_2026-05-29.md"
        self._write(
            spec,
            "\n".join(
                [
                    "# Spec",
                    "Status: DRAFT",
                    "- Connector spec < 5 lines (actual: 4 lines).",
                    "Line 4",
                    "Line 5",
                    "Line 6",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([spec])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "connector spec claims a line-count threshold under 5 lines but file has 6 lines",
            report["violations"][0]["issues"],
        )


if __name__ == "__main__":
    unittest.main()
