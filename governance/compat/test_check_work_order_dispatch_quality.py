#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
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
                    "Current Runtime Freshness Verification",
                    "ACCEPT_AS_OWNER_MAP coverage",
                    "Mandatory Gate-Failure Remediation Protocol",
                    "Worker Autonomy / No-Question Rule",
                    "Pending Artifact Evidence Finality",
                    "Commit Mode And Base-Anchor Lifecycle",
                    "Self-Reported Gate Evidence Consistency",
                    "Near-Threshold Owner Maintainability Plan",
                    "Work-Order Fulfillment Manifest",
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
                    "Current Runtime Freshness Verification",
                    "ACCEPT_AS_OWNER_MAP coverage",
                    "Mandatory Gate-Failure Remediation Protocol",
                    "Worker Autonomy / No-Question Rule",
                    "Pending Artifact Evidence Finality",
                    "Commit Mode And Base-Anchor Lifecycle",
                    "Self-Reported Gate Evidence Consistency",
                    "Near-Threshold Owner Maintainability Plan",
                    "Work-Order Fulfillment Manifest",
                    MODULE.THIS_SCRIPT_PATH,
                ]
            ),
        )
        self._write(
            MODULE.WORKER_AUTONOMY_STANDARD_PATH,
            "\n".join(
                [
                    "Worker Autonomy Prompt",
                    "Worker Autonomy / No-Question Rule",
                    "Commit Mode And Base-Anchor Requirement",
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

    def test_ready_work_order_with_blocked_source_row_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_PM1_TEST_2026-05-29.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: READY_FOR_IMPLEMENTATION",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| Executable proof path | `docs/reference/CVF_MISSING_METHOD_SPEC.md` | missing | `json_mode` | Method runner | BLOCKED_SOURCE_NOT_FOUND |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "dispatch/ready work order contains blocking Source Verification disposition; "
            "use HOLD/DRAFT until source facts are resolved",
            report["violations"][0]["issues"],
        )

    def test_ready_work_order_with_required_dependency_placeholder_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_CI2_T5_TEST_2026-06-03.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCH_READY",
                    "dispatchBaseHead: abc1234",
                    "executionBaseHead: WORKER_MUST_CAPTURE_AT_START",
                    "closureBaseHead: NOT_EXECUTED_YET",
                    "Commit mode: WORKER_MUST_NOT_COMMIT",
                    "## Authority Chain",
                    "| Authority | Path / basis | Disposition |",
                    "| --- | --- | --- |",
                    "| Prior tranche | T4 pilot pack after closure | REQUIRED |",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| Existing use-case roadmap | `docs/roadmaps/CVF_LPCI_TEST.md` | title | `LPCI` | use-case roadmap | ACCEPT |",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside allowed scope.",
                ]
            ),
        )
        self._write("docs/roadmaps/CVF_LPCI_TEST.md", "# LPCI\n")

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        issues = report["violations"][0]["issues"]
        self.assertIn(
            "dispatch/ready work order contains unresolved prerequisite disposition `REQUIRED`; "
            "release HOLD only after replacing it with source-backed ACCEPT evidence",
            issues,
        )

    def test_ready_work_order_without_worker_autonomy_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_AUTONOMY_TEST_2026-06-01.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: READY_FOR_IMPLEMENTATION",
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
        self.assertIn(
            "dispatch/ready work order lacks Worker Autonomy / No-Question Rule",
            report["violations"][0]["issues"],
        )

    def test_ready_work_order_without_commit_mode_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_COMMIT_MODE_TEST_2026-06-02.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: READY_FOR_IMPLEMENTATION",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside allowed scope.",
                    "dispatchBaseHead: abc1234",
                    "executionBaseHead: capture before edits",
                    "closureBaseHead: reviewer stage",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "dispatch/ready work order lacks explicit `Commit mode: "
            "WORKER_MAY_COMMIT | WORKER_MUST_NOT_COMMIT`",
            report["violations"][0]["issues"],
        )

    def test_ready_work_order_without_anchor_lifecycle_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_ANCHOR_LIFECYCLE_TEST_2026-06-02.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCHED_TO_WORKER",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside allowed scope.",
                    "Commit mode: WORKER_MUST_NOT_COMMIT",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "dispatch/ready work order lacks base-anchor lifecycle marker(s): "
            "dispatchBaseHead, executionBaseHead, closureBaseHead",
            report["violations"][0]["issues"],
        )

    def test_ready_work_order_with_invalid_commit_mode_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_INVALID_COMMIT_MODE_TEST_2026-06-02.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCHED_TO_WORKER",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside allowed scope.",
                    "Commit mode: ASK_OPERATOR_LATER",
                    "dispatchBaseHead: abc1234",
                    "executionBaseHead: capture before edits",
                    "closureBaseHead: reviewer stage",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "dispatch/ready work order has invalid commit mode "
            "`ASK_OPERATOR_LATER`; use WORKER_MAY_COMMIT or WORKER_MUST_NOT_COMMIT",
            report["violations"][0]["issues"],
        )

    def test_ready_no_commit_work_order_with_anchor_lifecycle_passes(self) -> None:
        work_order = "docs/work_orders/CVF_WO_VALID_NO_COMMIT_TEST_2026-06-02.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCHED_TO_WORKER",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside allowed scope.",
                    "Commit mode: WORKER_MUST_NOT_COMMIT",
                    "dispatchBaseHead: abc1234",
                    "executionBaseHead: capture before edits",
                    "closureBaseHead: reviewer stage",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertTrue(report["compliant"])

    def test_ready_work_order_cannot_forbid_near_threshold_owner_surface(self) -> None:
        work_order = "docs/work_orders/CVF_WO_OWNER_ROTATION_TEST_2026-06-01.md"
        owner_path = "EXTENSIONS/CVF_WEB/src/app/api/execute/route.ts"
        adjacent_path = "EXTENSIONS/CVF_WEB/src/app/api/memory/readout/route.ts"
        self._write(owner_path, "\n".join(f"line {index}" for index in range(118)) + "\n")
        self._write(
            MODULE.FILE_SIZE_REGISTRY_PATH,
            json.dumps(
                {
                    "thresholds": {
                        "general_source": {
                            "softThresholdLines": 90,
                            "hardThresholdLines": 120,
                        }
                    },
                    "nearHardRotationMarginLines": 5,
                    "nearHardMinShrinkLines": 10,
                    "proactiveOwnerSurfaces": [
                        {
                            "path": owner_path,
                            "status": "ACTIVE",
                            "domainPrefixes": ["EXTENSIONS/CVF_WEB/src/app/api/"],
                        }
                    ],
                }
            ),
        )
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCHED_TO_WORKER",
                    "Allowed scope:",
                    f"- add `{adjacent_path}`",
                    "Forbidden scope:",
                    f"- `{owner_path}`",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside scope.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "dispatch/ready work order enters registered near-threshold owner domain for "
            f"`{owner_path}` (118/120 lines) without `## Near-Threshold Owner Maintainability Plan`",
            report["violations"][0]["issues"],
        )

    def test_pending_review_claiming_clean_git_status_fails(self) -> None:
        review = "docs/reviews/CVF_PENDING_REVIEW_2026-06-01.md"
        self._write(
            review,
            "\n".join(
                [
                    "# Pending Review",
                    "Status: IN_PROGRESS_DISPATCHED",
                    "## Governance Gates Run",
                    "- `git status --short` -> clean",
                ]
            ),
        )

        with (
            patch.object(MODULE, "REPO_ROOT", self.repo_root),
            patch.object(MODULE, "_get_changed", return_value={review: {"A"}}),
        ):
            report = MODULE._classify([review], base_ref="HEAD")

        self.assertFalse(report["compliant"])
        self.assertIn(
            "pending changed artifact records `git status --short` as clean even though the artifact "
            "itself is not committed; record the actual pending status or commit first",
            report["violations"][0]["issues"],
        )

    def test_pending_review_with_head_prev_range_evidence_fails(self) -> None:
        review = "docs/reviews/CVF_PENDING_RANGE_REVIEW_2026-06-01.md"
        self._write(
            review,
            "\n".join(
                [
                    "# Pending Range Review",
                    "Status: IN_PROGRESS_DISPATCHED",
                    "## Governance Gates Run",
                    "- `python governance/compat/check_work_order_dispatch_quality.py --base HEAD~1 --head HEAD --enforce` -> PASS",
                    "- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base HEAD~1 --head HEAD` -> PASS",
                ]
            ),
        )

        with (
            patch.object(MODULE, "REPO_ROOT", self.repo_root),
            patch.object(MODULE, "_get_changed", return_value={review: {"A"}}),
        ):
            report = MODULE._classify([review], base_ref="HEAD")

        self.assertFalse(report["compliant"])
        self.assertIn(
            "pending changed artifact cites `--base HEAD~1 --head HEAD` gate evidence that does not "
            "prove the pending artifact; use a working-tree-aware validation or commit the artifact "
            "and rerun the real changed range",
            report["violations"][0]["issues"],
        )

    def test_pending_review_status_output_must_include_self_path(self) -> None:
        review = "docs/reviews/CVF_PENDING_STATUS_REVIEW_2026-06-01.md"
        self._write(
            review,
            "\n".join(
                [
                    "# Pending Status Review",
                    "Status: IN_PROGRESS_DISPATCHED",
                    "## Governance Gates Run",
                    "- `git status --short` ->",
                    "  - `?? docs/reviews/OTHER_REVIEW_2026-06-01.md`",
                ]
            ),
        )

        with (
            patch.object(MODULE, "REPO_ROOT", self.repo_root),
            patch.object(MODULE, "_get_changed", return_value={review: {"A"}}),
        ):
            report = MODULE._classify([review], base_ref="HEAD")

        self.assertFalse(report["compliant"])
        self.assertIn(
            "pending changed artifact records `git status --short` but omits its own pending path; "
            "record the actual pending status line for this artifact",
            report["violations"][0]["issues"],
        )

    def test_nonblocked_artifact_with_self_reported_gate_fail_fails(self) -> None:
        review = "docs/reviews/CVF_PENDING_GATE_FAIL_REVIEW_2026-06-01.md"
        self._write(
            review,
            "\n".join(
                [
                    "# Pending Gate Fail Review",
                    "Status: IN_PROGRESS_DISPATCHED",
                    "## Governance Gates Run",
                    "- `python governance/compat/check_work_order_dispatch_quality.py --base abc1234 --head HEAD --enforce` -> FAIL",
                ]
            ),
        )

        with (
            patch.object(MODULE, "REPO_ROOT", self.repo_root),
            patch.object(MODULE, "_get_changed", return_value={review: {"A"}}),
        ):
            report = MODULE._classify([review], base_ref="HEAD")

        self.assertFalse(report["compliant"])
        self.assertIn(
            "artifact records a failed self-reported governance gate while status is not BLOCKED/HOLD; "
            "repair allowed-scope failures and rerun, or mark the artifact BLOCKED with return action",
            report["violations"][0]["issues"],
        )

    def test_finding_bearing_artifact_with_autorun_pass_missing_learning_disposition_fails(self) -> None:
        review = "docs/reviews/CVF_PENDING_STALE_PASS_REVIEW_2026-06-01.md"
        self._write(
            review,
            "\n".join(
                [
                    "# Pending Stale Pass Review",
                    "Status: IN_PROGRESS_DISPATCHED",
                    "## Findings / Position",
                    "- Finding: gate evidence is current.",
                    "## Governance Gates Run",
                    "- `git status --short` ->",
                    f"  - `?? {review}`",
                    "- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base abc1234 --head HEAD` -> PASS",
                ]
            ),
        )

        with (
            patch.object(MODULE, "REPO_ROOT", self.repo_root),
            patch.object(MODULE, "_get_changed", return_value={review: {"A"}}),
        ):
            report = MODULE._classify([review], base_ref="HEAD")

        self.assertFalse(report["compliant"])
        self.assertIn(
            "artifact records autorun gate PASS but is finding-bearing without "
            "`## Finding-To-Governance Learning Disposition`; rerun after adding the required section",
            report["violations"][0]["issues"],
        )

    def test_blocked_artifact_may_record_gate_fail_with_return_action(self) -> None:
        review = "docs/reviews/CVF_BLOCKED_GATE_FAIL_REVIEW_2026-06-01.md"
        self._write(
            review,
            "\n".join(
                [
                    "# Blocked Gate Fail Review",
                    "Status: BLOCKED",
                    "Return action: orchestrator must expand scope.",
                    "## Governance Gates Run",
                    "- `python governance/compat/check_work_order_dispatch_quality.py --base abc1234 --head HEAD --enforce` -> FAIL",
                ]
            ),
        )

        with (
            patch.object(MODULE, "REPO_ROOT", self.repo_root),
            patch.object(MODULE, "_get_changed", return_value={review: {"A"}}),
        ):
            report = MODULE._classify([review], base_ref="HEAD")

        self.assertTrue(report["compliant"])

    def test_runtime_work_order_fulfillment_manifest_catches_missing_artifacts_and_forbidden_paths(self) -> None:
        work_order = "docs/work_orders/CVF_WO_MKG6_TEST_2026-06-01.md"
        changed_forbidden = "EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts"
        changed_runtime = "EXTENSIONS/CVF_WEB/src/app/api/execute/route.ts"
        proof_path = "EXTENSIONS/CVF_WEB/src/app/api/memory/readout/route.test.ts"
        self._write(changed_forbidden, "export const touched = true;\n")
        self._write(changed_runtime, "export const route = true;\n")
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCHED_TO_WORKER",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside scope.",
                    "## Work-Order Fulfillment Manifest",
                    "Manifest applies.",
                    "## Required Artifact Manifest",
                    "| Path | Required at handoff | Purpose |",
                    "|---|---|---|",
                    "| `EXTENSIONS/CVF_WEB/src/app/api/memory/readout/route.ts` | Yes | route |",
                    "| `docs/reviews/CVF_MKG6_COMPLETION.md` | Yes | completion |",
                    "## Forbidden Path Manifest",
                    "| Path | Reason |",
                    "|---|---|",
                    f"| `{changed_forbidden}` | forbidden by work order |",
                    "## Required Proof Manifest",
                    "| Proof | Path | Required literal | Required at handoff |",
                    "|---|---|---|---|",
                    f"| raw leak sentinel | `{proof_path}` | `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` | Yes |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order, changed_runtime, changed_forbidden])

        self.assertFalse(report["compliant"])
        issues = [
            issue
            for violation in report["violations"]
            if violation["path"] == work_order
            for issue in violation["issues"]
        ]
        self.assertIn(
            "required handoff artifact is missing: `EXTENSIONS/CVF_WEB/src/app/api/memory/readout/route.ts`",
            issues,
        )
        self.assertIn(
            "required handoff artifact is missing: `docs/reviews/CVF_MKG6_COMPLETION.md`",
            issues,
        )
        self.assertIn(
            f"changed file violates forbidden path manifest: `{changed_forbidden}` matches `{changed_forbidden}`",
            issues,
        )
        self.assertIn(
            f"required proof file is missing: `{proof_path}`",
            issues,
        )

    def test_required_proof_literal_must_exist_in_named_file(self) -> None:
        work_order = "docs/work_orders/CVF_WO_SENTINEL_TEST_2026-06-01.md"
        route_path = "EXTENSIONS/CVF_WEB/src/app/api/memory/readout/route.ts"
        proof_path = "EXTENSIONS/CVF_WEB/src/app/api/memory/readout/route.test.ts"
        self._write(route_path, "export const route = true;\n")
        self._write(proof_path, "it('checks response', () => {});\n")
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: DISPATCHED_TO_WORKER",
                    "## Worker Autonomy / No-Question Rule",
                    "Proceed inside scope.",
                    "## Work-Order Fulfillment Manifest",
                    "Manifest applies.",
                    "## Required Artifact Manifest",
                    "| Path | Required at handoff | Purpose |",
                    "|---|---|---|",
                    f"| `{route_path}` | Yes | route |",
                    "## Required Proof Manifest",
                    "| Proof | Path | Required literal | Required at handoff |",
                    "|---|---|---|---|",
                    f"| raw leak sentinel | `{proof_path}` | `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` | Yes |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order, route_path, proof_path])

        self.assertFalse(report["compliant"])
        issues = [
            issue
            for violation in report["violations"]
            if violation["path"] == work_order
            for issue in violation["issues"]
        ]
        self.assertIn(
            f"required proof literal `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` is missing from `{proof_path}`",
            issues,
        )

    def test_new_doc_only_field_in_source_verification_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW12_T1_TEST_2026-05-29.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_PENDING_T1",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| `modelTierAdvisoryType` (new doc-only field) | N/A - canonical doc-only field | S3 | `modelTierAdvisoryType` | LHW12-T1 packet | ACCEPT |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "New doc-only fields must be listed in a separate New Doc-Only Fields table, "
            "not as Source Verification ACCEPT rows",
            report["violations"][0]["issues"],
        )

    def test_ready_live_method_proof_without_executable_path_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_PM1_JSON_MODE_TEST_2026-05-29.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: READY_FOR_IMPLEMENTATION",
                    "Purpose: live proof for provider method json_mode.",
                    "Run `/api/execute` with a method flag.",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| Provider lane | `governance/contracts/example.ts` | line 1 | `provider` | Provider map | ACCEPT |",
                ]
            ),
        )
        self._write("governance/contracts/example.ts", "export const provider = 'deepseek';\n")

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "dispatch/ready live-method proof cites generic `/api/execute` or a method flag "
            "without a source-verified executable proof path",
            report["violations"][0]["issues"],
        )

    def test_memory_gateway_can_reinject_false_prose_without_source_fails(self) -> None:
        baseline = "docs/baselines/CVF_GC018_LHW13_TEST_2026-05-29.md"
        self._write(
            baseline,
            "\n".join(
                [
                    "# Baseline",
                    "Status: PROPOSED",
                    "GC says `MemoryGatewayDecision.canReinject=false` is preserved.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([baseline])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "Prose claims `MemoryGatewayDecision.canReinject=false`; the known source contract "
            "declares `canReinject` as a boolean unless a cited source proves a literal false assignment",
            report["violations"][0]["issues"],
        )

    def test_connector_doc_only_field_accept_citing_roadmap_fails(self) -> None:
        work_order = "docs/work_orders/CVF_WO_EL3_TEST_2026-05-29.md"
        roadmap = "docs/roadmaps/CVF_LHW12_TEST_ROADMAP_2026-05-29.md"
        self._write(roadmap, "# Roadmap\nStatus: PROPOSED\n")
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: HOLD_PENDING_T1",
                    "## Source Verification Block",
                    "| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |",
                    "|---|---|---|---|---|---|",
                    "| `modelTierAdvisoryType` doc-only field | `docs/roadmaps/CVF_LHW12_TEST_ROADMAP_2026-05-29.md` | S3 planned field list | `modelTierAdvisoryType` | LHW12-T1 doc-only field | ACCEPT |",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order, roadmap])

        self.assertFalse(report["compliant"])
        issues = [
            issue
            for violation in report["violations"]
            if violation["path"] == work_order
            for issue in violation["issues"]
        ]
        self.assertIn(
            "Source Verification ACCEPT for connector doc-only field cites a roadmap; "
            "cite the connector spec after it exists or move the field to New Doc-Only Fields",
            issues,
        )
        self.assertIn(
            "Source Verification ACCEPT uses pending/planned/future line or section language; "
            "use BLOCKED_SOURCE_NOT_FOUND until the source exists",
            issues,
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

    def test_accept_owner_map_complete_coverage_claim_requires_each_concept(self) -> None:
        roadmap = "docs/roadmaps/CVF_LHW22_TEST_ROADMAP_2026-05-31.md"
        self._write(
            MODULE.IMPORTANT_FULL_SCAN_AUDIT_PATH,
            "\n".join(
                [
                    "| Concept | Disposition | Reason |",
                    "|---|---|---|",
                    "| UCO — Capability-based constraint binding | `ACCEPT_AS_OWNER_MAP` | maps to guard |",
                    "| Artifact Store abstraction | `ACCEPT_AS_OWNER_MAP` | maps to git |",
                ]
            ),
        )
        self._write(
            roadmap,
            "\n".join(
                [
                    "# Roadmap",
                    "Status: HOLD_FOR_FRESH_GC018",
                    "This roadmap covers all `ACCEPT_AS_OWNER_MAP` items.",
                    "UCO — Capability-based constraint binding is in LHW22.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([roadmap])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "artifact claims complete ACCEPT_AS_OWNER_MAP coverage but lacks disposition for: Artifact Store abstraction",
            report["violations"][0]["issues"],
        )

    def test_absent_runtime_claim_requires_current_freshness_section(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW23_TEST_2026-05-31.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Work Order",
                    "Status: HOLD_FOR_FRESH_GC018",
                    "Gap: provider list is hardcoded strings and no registry is present.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        issues = report["violations"][0]["issues"]
        self.assertIn(
            "artifact makes absent/not-implemented/hardcoded runtime claims without a "
            "`Current Runtime Freshness Verification` section",
            issues,
        )
        self.assertIn(
            "provider registry absence/hardcoded claim must account for current "
            "`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and "
            "`PROVIDER_CAPABILITY_REGISTRY` surfaces",
            issues,
        )

    def test_resolve_provider_claim_requires_current_owner_path(self) -> None:
        work_order = "docs/work_orders/CVF_WO_LHW23_TEST_2026-05-31.md"
        self._write(
            work_order,
            "\n".join(
                [
                    "# Work Order",
                    "Status: HOLD_FOR_FRESH_GC018",
                    "## Current Runtime Freshness Verification",
                    "`resolveProviderForRole()` is mapped to an old MCP source.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order])

        self.assertFalse(report["compliant"])
        self.assertIn(
            "`resolveProviderForRole()` claim must cite current source "
            "`EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`",
            report["violations"][0]["issues"],
        )

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

    def test_closed_work_order_allows_explicit_root_governance_path(self) -> None:
        work_order = "docs/work_orders/CVF_WO_ROOT_GOVERNANCE_TEST_2026-06-01.md"
        root_governance_path = "AGENTS.md"
        self._write(root_governance_path, "# Agent instructions\n")
        self._write(
            work_order,
            "\n".join(
                [
                    "# Test",
                    "Status: CLOSED_PASS_BOUNDED",
                    "## Scope",
                    "Allowed scope:",
                    f"- Update `{root_governance_path}`.",
                    "Forbidden scope:",
                    "- Other root files.",
                ]
            ),
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify([work_order, root_governance_path])

        self.assertTrue(report["compliant"])

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
