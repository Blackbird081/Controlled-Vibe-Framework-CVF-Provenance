#!/usr/bin/env python3
"""Focused unit tests for the WOAS-R1 dispatch packet authoring scaffold helper."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_dispatch_packet_scaffold import (
    ScaffoldArgs,
    build_gc018_baseline,
    build_trigger_map_table,
    build_work_order,
    detect_triggers,
    main,
    TRIGGER_FAMILIES,
)


def _base_args(**overrides) -> ScaffoldArgs:
    defaults = dict(
        packet_kind="generic-worker-dispatch",
        batch_id="TEST-BATCH",
        title="Test Packet",
        date="2026-07-01",
        base="abc1234",
        commit_mode="WORKER_MUST_NOT_COMMIT",
        dependencies=[],
    )
    defaults.update(overrides)
    return ScaffoldArgs(**defaults)


class TestGenericWorkerDispatch(unittest.TestCase):
    """AC1: helper emits a generic held worker-dispatch baseline and work order."""

    def test_baseline_has_required_machine_shape_sections(self) -> None:
        args = _base_args()
        active = detect_triggers(args)
        baseline = build_gc018_baseline(args, active)
        for marker in (
            "## Purpose",
            "## ADIF Defect Registry Disclosure",
            "## Checker Source Read-Ahead Block",
            "## Source Verification Block",
            "## Negative Search And Collision Discipline",
            "## Public Export Disposition",
        ):
            self.assertIn(marker, baseline)

    def test_work_order_has_required_machine_shape_sections(self) -> None:
        args = _base_args()
        active = detect_triggers(args)
        work_order = build_work_order(args, active)
        for marker in (
            "## Dispatch Prompt Envelope",
            "## Purpose",
            "## Worker Autonomy / No-Question Rule",
            "## ADIF Defect Registry Disclosure",
            "## Checker Source Read-Ahead Block",
            "## Source Verification Block",
            "## Negative Search And Collision Discipline",
            "## Work-Order Fulfillment Manifest",
            "## Worker Return Packet Shape Contract",
            "## Agent Operation Trace Block",
            "## Delta Execution Claim Boundary Control Block",
            "## Public Export Disposition",
        ):
            self.assertIn(marker, work_order)

    def test_dispatch_prompt_envelope_is_first_section(self) -> None:
        args = _base_args()
        active = detect_triggers(args)
        work_order = build_work_order(args, active)
        first_heading_index = work_order.find("\n## ")
        self.assertNotEqual(first_heading_index, -1)
        first_heading_line = work_order[first_heading_index + 1 :].splitlines()[0]
        self.assertEqual(first_heading_line, "## Dispatch Prompt Envelope")

    def test_checker_read_ahead_block_has_four_required_fields(self) -> None:
        args = _base_args()
        active = detect_triggers(args)
        work_order = build_work_order(args, active)
        for field in (
            "applicableCheckersRead",
            "literalTokensReviewed",
            "gateRunPurpose",
            "claimBoundary",
        ):
            self.assertIn(field, work_order)

    def test_source_verification_block_has_required_columns(self) -> None:
        args = _base_args()
        active = detect_triggers(args)
        work_order = build_work_order(args, active)
        for column in (
            "Claimed item",
            "Source file",
            "Verified line/section",
            "Verified path or symbol",
            "Owning interface/function/schema",
            "Disposition",
        ):
            self.assertIn(column, work_order)

    def test_adif_disclosure_has_exact_resolver_query_field_names(self) -> None:
        args = _base_args()
        active = detect_triggers(args)
        baseline = build_gc018_baseline(args, active)
        self.assertIn("Resolver query: taskClass=`", baseline)
        self.assertIn("role=`", baseline)
        self.assertIn("lifecyclePhase=`", baseline)


class TestHeldPacketDependencyFields(unittest.TestCase):
    """AC4: held packets contain dependency-release evidence fields."""

    def test_dependency_flag_activates_held_dependency_trigger(self) -> None:
        args = _base_args(dependencies=["upstream closure evidence"])
        active = detect_triggers(args)
        self.assertTrue(active["held_dependency"])

    def test_no_dependency_and_non_held_kind_does_not_activate_trigger(self) -> None:
        args = _base_args(dependencies=[], packet_kind="generic-worker-dispatch")
        active = detect_triggers(args)
        self.assertFalse(active["held_dependency"])

    def test_held_dependency_packet_kind_activates_without_dependency_flag(self) -> None:
        args = _base_args(dependencies=[], packet_kind="held-dependency")
        active = detect_triggers(args)
        self.assertTrue(active["held_dependency"])

    def test_dependency_release_evidence_section_lists_dependency_text(self) -> None:
        args = _base_args(dependencies=["KIOD-R8 closure evidence"])
        active = detect_triggers(args)
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Dependency Release Evidence", baseline)
        self.assertIn("KIOD-R8 closure evidence", baseline)

    def test_non_held_packet_omits_dependency_release_evidence_section(self) -> None:
        args = _base_args(dependencies=[], packet_kind="generic-worker-dispatch")
        active = detect_triggers(args)
        baseline = build_gc018_baseline(args, active)
        self.assertNotIn("## Dependency Release Evidence", baseline)


class TestNoCommitWorkerPacket(unittest.TestCase):
    """AC2: helper emits a no-commit worker packet with AHB and Reviewer Closure Conversion."""

    def test_worker_must_not_commit_activates_no_commit_trigger(self) -> None:
        args = _base_args(commit_mode="WORKER_MUST_NOT_COMMIT")
        active = detect_triggers(args)
        self.assertTrue(active["no_commit_worker"])

    def test_worker_may_commit_does_not_activate_no_commit_trigger(self) -> None:
        args = _base_args(commit_mode="WORKER_MAY_COMMIT")
        active = detect_triggers(args)
        self.assertFalse(active["no_commit_worker"])

    def test_work_order_includes_ahb_and_reviewer_closure_when_must_not_commit(self) -> None:
        args = _base_args(commit_mode="WORKER_MUST_NOT_COMMIT")
        active = detect_triggers(args)
        work_order = build_work_order(args, active)
        self.assertIn("## Agent Handoff Contract Control Block", work_order)
        self.assertIn("## Reviewer Closure Conversion", work_order)
        self.assertIn("workerCommitPermission | FORBIDDEN", work_order)

    def test_ahb_block_has_required_base_head_fields(self) -> None:
        args = _base_args(commit_mode="WORKER_MUST_NOT_COMMIT", base="deadbeef")
        active = detect_triggers(args)
        work_order = build_work_order(args, active)
        self.assertIn("dispatchBaseHead=deadbeef", work_order)
        self.assertIn("executionBaseHead=WORKER_MUST_CAPTURE_AT_START", work_order)
        self.assertIn("closureBaseHead=REVIEWER_TO_SET", work_order)

    def test_work_order_omits_ahb_when_worker_may_commit(self) -> None:
        args = _base_args(commit_mode="WORKER_MAY_COMMIT")
        active = detect_triggers(args)
        work_order = build_work_order(args, active)
        self.assertNotIn("## Agent Handoff Contract Control Block", work_order)
        self.assertNotIn("## Reviewer Closure Conversion", work_order)


class TestTriggerDrivenOptionalBlocks(unittest.TestCase):
    """AC3: trigger-driven stubs for source-intake, runtime/provider/live,
    package-skill, Web/UI, MCP/CLI, public-sync, evidence-reuse, and
    protected-path indicators."""

    def test_source_intake_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="Outside-source repo folder review")
        active = detect_triggers(args)
        self.assertTrue(active["source_intake"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Source-Intake Decision Packet Fields", baseline)

    def test_runtime_provider_live_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="Runtime provider live proof packet")
        active = detect_triggers(args)
        self.assertTrue(active["runtime_provider_live"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Current Runtime Freshness Verification", baseline)

    def test_package_skill_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="Package skill registry work")
        active = detect_triggers(args)
        self.assertTrue(active["package_skill"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Package Skill Productionization Control Block", baseline)

    def test_web_ui_dashboard_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="Web dashboard UI redesign")
        active = detect_triggers(args)
        self.assertTrue(active["web_ui_dashboard"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Web/UI Claim Boundary", baseline)

    def test_mcp_cli_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="MCP adapter and CLI boundary work")
        active = detect_triggers(args)
        self.assertTrue(active["mcp_cli"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## MCP/CLI Adapter Boundary", baseline)

    def test_public_sync_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="Public-sync export batch")
        active = detect_triggers(args)
        self.assertTrue(active["public_sync"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Public/Provenance Boundary", baseline)

    def test_unicode_evidence_reuse_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="Unicode encoding and prior evidence reuse")
        active = detect_triggers(args)
        self.assertTrue(active["unicode_evidence_reuse"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Evidence Reuse And Encoding Plan", baseline)

    def test_protected_governance_path_indicator_activates_trigger_and_stub(self) -> None:
        args = _base_args(title="Update hook catalog and checker wiring")
        active = detect_triggers(args)
        self.assertTrue(active["protected_governance_path"])
        baseline = build_gc018_baseline(args, active)
        self.assertIn("## Core Guard Self-Protection Authorization", baseline)

    def test_neutral_title_does_not_activate_content_triggers(self) -> None:
        args = _base_args(title="A quiet neutral title with no trigger words")
        active = detect_triggers(args)
        for key in (
            "source_intake",
            "runtime_provider_live",
            "package_skill",
            "web_ui_dashboard",
            "mcp_cli",
            "public_sync",
            "unicode_evidence_reuse",
            "protected_governance_path",
        ):
            self.assertFalse(active[key], f"trigger {key} unexpectedly active")


class TestTriggerMapExplainability(unittest.TestCase):
    """The helper must expose an explainable trigger map."""

    def test_trigger_map_lists_all_ten_families(self) -> None:
        table = build_trigger_map_table()
        self.assertEqual(len(TRIGGER_FAMILIES), 10)
        for _key, name, _indicators, stub in TRIGGER_FAMILIES:
            self.assertIn(name, table)
            self.assertIn(stub.split(";")[0], table)

    def test_trigger_map_reference_mode_has_na_status(self) -> None:
        table = build_trigger_map_table()
        self.assertIn("N/A (reference only)", table)
        self.assertNotIn("ACTIVE", table)

    def test_trigger_map_active_mode_shows_active_and_inactive(self) -> None:
        args = _base_args(dependencies=["dep"], commit_mode="WORKER_MUST_NOT_COMMIT")
        active = detect_triggers(args)
        table = build_trigger_map_table(active)
        self.assertIn("ACTIVE", table)
        self.assertIn("inactive", table)

    def test_explain_trigger_map_cli_exits_zero(self) -> None:
        exit_code = main(["--explain-trigger-map"])
        self.assertEqual(exit_code, 0)


class TestCliBehavior(unittest.TestCase):
    def test_missing_required_args_exits_nonzero(self) -> None:
        exit_code = main(["--packet-kind", "generic-worker-dispatch"])
        self.assertEqual(exit_code, 2)

    def test_full_args_without_stdout_exits_nonzero(self) -> None:
        exit_code = main(
            [
                "--packet-kind",
                "generic-worker-dispatch",
                "--batch-id",
                "CLI-TEST",
                "--title",
                "CLI Test Packet",
                "--date",
                "2026-07-01",
                "--base",
                "abc1234",
                "--commit-mode",
                "WORKER_MUST_NOT_COMMIT",
            ]
        )
        self.assertEqual(exit_code, 2)

    def test_full_args_with_stdout_exits_zero(self) -> None:
        exit_code = main(
            [
                "--packet-kind",
                "generic-worker-dispatch",
                "--batch-id",
                "CLI-TEST",
                "--title",
                "CLI Test Packet",
                "--date",
                "2026-07-01",
                "--base",
                "abc1234",
                "--commit-mode",
                "WORKER_MUST_NOT_COMMIT",
                "--dependency",
                "sample upstream closure",
                "--stdout",
            ]
        )
        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
