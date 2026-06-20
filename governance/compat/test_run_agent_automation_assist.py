#!/usr/bin/env python3
"""Focused tests for the AAF-T1 read-only agent automation assist helper."""

from __future__ import annotations

import importlib.util
import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

# Ensure the flat-import sibling dependency resolves regardless of how this test
# is invoked (pytest by path or `python -m unittest governance.compat....`).
_COMPAT_DIR = Path(__file__).resolve().parent
if str(_COMPAT_DIR) not in sys.path:
    sys.path.insert(0, str(_COMPAT_DIR))

_MODULE_PATH = _COMPAT_DIR / "run_agent_automation_assist.py"
_SPEC = importlib.util.spec_from_file_location("run_agent_automation_assist", _MODULE_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError(f"Unable to load module from {_MODULE_PATH}")
assist = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = assist
_SPEC.loader.exec_module(assist)

from run_agent_commit_steward_preflight import PathPlan


def _plan(
    changed=(),
    material=(),
    protected=(),
    trace=(),
    mixed=False,
    collision=False,
    handoff_only=False,
) -> PathPlan:
    return PathPlan(
        changed_paths=tuple(changed),
        material_paths=tuple(material),
        protected_session_paths=tuple(protected),
        trace_artifact_paths=tuple(trace),
        mixed_material_and_session=mixed,
        exact_manifest_collision_risk=collision,
        handoff_sync_only=handoff_only,
    )


_NO_COMMIT_WO_WITH_CONTRACT = """# Work Order

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Worker Return Packet Shape Contract

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short.
Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package.
Use `N/A with reason` for non-applicable conditional blocks.
"""

_NO_COMMIT_WO_MISSING_CONTRACT = """# Work Order

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Do something.
"""


class RecommendModeTests(unittest.TestCase):
    def test_auto_recommends_session_sync_for_session_only(self):
        plan = _plan(
            changed=("CVF_SESSION/ACTIVE_SESSION_STATE.json",),
            protected=("CVF_SESSION/ACTIVE_SESSION_STATE.json",),
        )
        self.assertEqual(assist.recommend_mode(plan), "session-sync")

    def test_auto_recommends_handoff_sync(self):
        plan = _plan(
            changed=("AGENT_HANDOFF_V20_2026-06-19.md",),
            protected=("AGENT_HANDOFF_V20_2026-06-19.md",),
            handoff_only=True,
        )
        self.assertEqual(assist.recommend_mode(plan), "handoff-sync")

    def test_auto_recommends_implementation_for_material(self):
        plan = _plan(
            changed=("governance/compat/foo.py",),
            material=("governance/compat/foo.py",),
        )
        self.assertEqual(assist.recommend_mode(plan), "implementation")

    def test_auto_recommends_dispatch_for_dispatch_packet(self):
        plan = _plan(
            changed=("docs/work_orders/x.md",),
            material=("docs/work_orders/x.md",),
        )
        with mock.patch.object(
            assist,
            "_read_changed_text",
            return_value="# Work Order\n\nStatus: DISPATCH_READY\n",
        ):
            self.assertEqual(assist.recommend_mode(plan), "dispatch")

    def test_auto_recommends_reviewer_return_for_pending_review_packet(self):
        plan = _plan(
            changed=("docs/reviews/x.md", "governance/compat/foo.py"),
            material=("docs/reviews/x.md", "governance/compat/foo.py"),
        )
        with mock.patch.object(
            assist,
            "_read_changed_text",
            return_value="Status: COMPLETE_PENDING_REVIEW\nCommit mode: `WORKER_MUST_NOT_COMMIT`\n",
        ):
            self.assertEqual(assist.recommend_mode(plan), "reviewer-return")

    def test_auto_recommends_split_for_mixed(self):
        plan = _plan(
            changed=("governance/compat/foo.py", "CVF_SESSION/x.json"),
            material=("governance/compat/foo.py",),
            protected=("CVF_SESSION/x.json",),
            mixed=True,
        )
        self.assertEqual(assist.recommend_mode(plan), "split")

    def test_auto_recommends_none_for_empty(self):
        self.assertEqual(assist.recommend_mode(_plan()), "none")


class WorkOrderDiagnosticTests(unittest.TestCase):
    def test_missing_contract_flags_all_terms(self):
        diag = assist.diagnose_no_commit_work_order(
            "docs/work_orders/x.md", _NO_COMMIT_WO_MISSING_CONTRACT
        )
        self.assertFalse(diag.has_contract)
        self.assertFalse(diag.is_clean)
        self.assertEqual(
            diag.missing_required,
            assist.WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS,
        )

    def test_complete_contract_is_clean(self):
        diag = assist.diagnose_no_commit_work_order(
            "docs/work_orders/x.md", _NO_COMMIT_WO_WITH_CONTRACT
        )
        self.assertTrue(diag.has_contract)
        self.assertEqual(diag.missing_required, ())
        self.assertEqual(diag.missing_conditional, ())
        self.assertFalse(diag.missing_na_instruction)
        self.assertTrue(diag.is_clean)

    def test_is_no_commit_work_order_requires_path_and_marker(self):
        self.assertTrue(
            assist._is_no_commit_work_order(
                "docs/work_orders/x.md", _NO_COMMIT_WO_WITH_CONTRACT
            )
        )
        # Right marker, wrong path class.
        self.assertFalse(
            assist._is_no_commit_work_order(
                "docs/reviews/x.md", _NO_COMMIT_WO_WITH_CONTRACT
            )
        )
        # Right path class, no no-commit marker.
        self.assertFalse(
            assist._is_no_commit_work_order(
                "docs/work_orders/x.md", "# WO\nCommit mode: `WORKER_MAY_COMMIT`\n"
            )
        )


class BuildReportTests(unittest.TestCase):
    def test_unsupported_mode_raises(self):
        with self.assertRaises(ValueError):
            assist.build_report("HEAD", "HEAD", "bogus-mode")

    def test_no_commit_work_order_missing_contract_produces_defect(self):
        plan = _plan(
            changed=("docs/work_orders/x.md",),
            material=("docs/work_orders/x.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_NO_COMMIT_WO_MISSING_CONTRACT
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertEqual(len(report.no_commit_work_orders), 1)
        self.assertFalse(report.no_commit_work_orders[0].is_clean)
        self.assertTrue(report.defects)
        self.assertTrue(
            any("missing `## Worker Return Packet Shape Contract`" in d for d in report.defects)
        )

    def test_clean_contract_produces_no_defect(self):
        plan = _plan(
            changed=("docs/work_orders/x.md",),
            material=("docs/work_orders/x.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_NO_COMMIT_WO_WITH_CONTRACT
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertEqual(report.defects, [])
        self.assertTrue(report.no_commit_work_orders[0].is_clean)

    def test_session_only_sets_resolved_mode_and_hint(self):
        plan = _plan(
            changed=("CVF_SESSION/ACTIVE_SESSION_STATE.json",),
            protected=("CVF_SESSION/ACTIVE_SESSION_STATE.json",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertEqual(report.resolved_mode, "session-sync")
        self.assertIn("session-sync", report.next_command)
        self.assertIn("session/handoff", report.session_sync_hint)

    def test_worker_return_changed_set_uses_reviewer_return_command(self):
        plan = _plan(
            changed=("docs/reviews/x.md", "governance/compat/foo.py"),
            material=("docs/reviews/x.md", "governance/compat/foo.py"),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist,
            "_read_changed_text",
            return_value="Status: COMPLETE_PENDING_REVIEW\nCommit mode: `WORKER_MUST_NOT_COMMIT`\n",
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertEqual(report.resolved_mode, "reviewer-return")
        self.assertIn("run_worker_return_fast_gate.py", report.next_command)


class CliOutputTests(unittest.TestCase):
    def _empty_plan_patch(self):
        return mock.patch.object(assist, "build_path_plan", return_value=_plan())

    def test_json_output_has_expected_keys(self):
        plan = _plan(
            changed=("governance/compat/foo.py",),
            material=("governance/compat/foo.py",),
        )
        buf = io.StringIO()
        with mock.patch.object(assist, "build_path_plan", return_value=plan):
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD", "--json"])
        self.assertEqual(rc, 0)
        payload = json.loads(buf.getvalue())
        for key in ("resolvedMode", "changedPaths", "nextCommand", "defects"):
            self.assertIn(key, payload)

    def test_enforce_exits_nonzero_on_defect(self):
        plan = _plan(
            changed=("docs/work_orders/x.md",),
            material=("docs/work_orders/x.md",),
        )
        buf = io.StringIO()
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_NO_COMMIT_WO_MISSING_CONTRACT
        ):
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD", "--enforce"])
        self.assertEqual(rc, 1)

    def test_enforce_exits_zero_when_clean(self):
        buf = io.StringIO()
        with self._empty_plan_patch():
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD", "--enforce"])
        self.assertEqual(rc, 0)

    def test_human_output_renders(self):
        buf = io.StringIO()
        with self._empty_plan_patch():
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD"])
        self.assertEqual(rc, 0)
        self.assertIn("CVF Agent Automation Assist", buf.getvalue())
        self.assertIn("Exact next command", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
