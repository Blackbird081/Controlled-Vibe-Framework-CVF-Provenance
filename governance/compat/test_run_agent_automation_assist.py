#!/usr/bin/env python3
"""Focused tests for the AAF read-only agent automation assist helper (AAF-T1 + AAF-T2)."""

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

# AAF-T2 corpus diagnostics fixtures
_REVIEW_COMPLETE_CLAIM_NO_SECTION = """# Review

All files were read and processed.
"""

_REVIEW_CLEAN_NA_CORPUS = """# Review

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - not a corpus scan.
- Corpus root: N/A with reason - no corpus root.
- Snapshot time: 2026-06-20
- Enumeration command: filesystem-backed direct file reads
- Manifest artifact or inline manifest: N/A with reason
- Manifest hash: N/A with reason
- Processing ledger artifact or inline ledger: N/A with reason
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=none; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason
- Drift check: N/A with reason
- Output traceability: N/A with reason
- Adversarial verification: N/A with reason
- Corpus verdict: PARTIAL
"""

_REVIEW_CORPUS_SECTION_MISSING_FIELDS = """# Review

## Corpus Completeness And Report Integrity

- Corpus task class: some task class
- Corpus verdict: PARTIAL
"""

_REVIEW_UNSAFE_ENUMERATION = """# Review

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - not a corpus scan.
- Corpus root: N/A with reason - no corpus root.
- Snapshot time: 2026-06-20
- Enumeration command: rg --files
- Manifest artifact or inline manifest: N/A with reason
- Manifest hash: N/A with reason
- Processing ledger artifact or inline ledger: N/A with reason
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=none; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason
- Drift check: N/A with reason
- Output traceability: N/A with reason
- Adversarial verification: N/A with reason
- Corpus verdict: PARTIAL
"""

_REVIEW_COMPLETE_VERIFIED_WITH_EXCLUSIONS = """# Review

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - not a corpus scan.
- Corpus root: N/A with reason - no corpus root.
- Snapshot time: 2026-06-20
- Enumeration command: filesystem-backed direct file reads
- Manifest artifact or inline manifest: N/A with reason
- Manifest hash: N/A with reason
- Processing ledger artifact or inline ledger: N/A with reason
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=some; unresolved=0
- Unresolved files: 0
- Declared exclusions: some files
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason
- Drift check: N/A with reason
- Output traceability: N/A with reason
- Adversarial verification: N/A with reason
- Corpus verdict: COMPLETE_VERIFIED
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


class CorpusDiagnosticTests(unittest.TestCase):
    def test_non_applicable_prefix_is_not_flagged(self):
        """docs/reference/ is not in CORPUS_APPLICABLE_PREFIXES."""
        diag = assist.diagnose_corpus_completeness(
            "docs/reference/foo.md", "content without corpus section"
        )
        self.assertFalse(diag.applicable)
        self.assertTrue(diag.is_clean)

    def test_archive_path_is_not_applicable(self):
        """Files under /archive/ are excluded."""
        text = assist.CORPUS_REQUIRED_SECTION + "\n\n- Corpus verdict: PARTIAL\n"
        diag = assist.diagnose_corpus_completeness(
            "docs/reviews/archive/old.md", text
        )
        self.assertFalse(diag.applicable)
        self.assertTrue(diag.is_clean)

    def test_review_with_complete_claim_and_no_section_is_defect(self):
        """A review file with complete-claim language but no section header is a defect."""
        diag = assist.diagnose_corpus_completeness(
            "docs/reviews/x.md", _REVIEW_COMPLETE_CLAIM_NO_SECTION
        )
        self.assertTrue(diag.applicable)
        self.assertFalse(diag.has_section)
        self.assertFalse(diag.is_clean)
        self.assertEqual(diag.missing_fields, assist.CORPUS_REQUIRED_SECTION_FIELDS)

    def test_clean_na_corpus_block_is_not_a_defect(self):
        """A review with all N/A-with-reason fields and a valid verdict is clean."""
        diag = assist.diagnose_corpus_completeness("docs/reviews/x.md", _REVIEW_CLEAN_NA_CORPUS)
        self.assertTrue(diag.applicable)
        self.assertTrue(diag.has_section)
        self.assertEqual(diag.missing_fields, ())
        self.assertEqual(diag.missing_terminal_statuses, ())
        self.assertTrue(diag.verdict_valid)
        self.assertEqual(diag.missing_reconciliation_markers, ())
        self.assertTrue(diag.is_clean)

    def test_missing_fields_in_corpus_section_is_defect(self):
        """Corpus section present but missing most required fields."""
        diag = assist.diagnose_corpus_completeness(
            "docs/reviews/x.md", _REVIEW_CORPUS_SECTION_MISSING_FIELDS
        )
        self.assertTrue(diag.applicable)
        self.assertTrue(diag.has_section)
        self.assertGreater(len(diag.missing_fields), 0)
        self.assertFalse(diag.is_clean)

    def test_unsafe_enumeration_is_defect(self):
        """Mirror canonical gate behavior for unsafe rg enumeration."""
        diag = assist.diagnose_corpus_completeness(
            "docs/reviews/x.md", _REVIEW_UNSAFE_ENUMERATION
        )
        self.assertTrue(diag.applicable)
        self.assertIn("unsafe_enumeration", diag.extra_violations)
        self.assertFalse(diag.is_clean)

    def test_complete_verified_with_exclusions_is_defect(self):
        """Mirror canonical gate behavior for incompatible complete verdict."""
        diag = assist.diagnose_corpus_completeness(
            "docs/reviews/x.md", _REVIEW_COMPLETE_VERIFIED_WITH_EXCLUSIONS
        )
        self.assertTrue(diag.applicable)
        self.assertIn("complete_verified_has_exclusions", diag.extra_violations)
        self.assertFalse(diag.is_clean)

    def test_non_md_path_is_not_applicable(self):
        diag = assist.diagnose_corpus_completeness("docs/reviews/x.py", "content")
        self.assertFalse(diag.applicable)
        self.assertTrue(diag.is_clean)


class BuildReportCorpusTests(unittest.TestCase):
    def test_corpus_defect_appears_in_defects_list(self):
        """Changed review with complete-claim but no corpus section adds to defects."""
        plan = _plan(
            changed=("docs/reviews/x.md",),
            material=("docs/reviews/x.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_REVIEW_COMPLETE_CLAIM_NO_SECTION
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertTrue(report.defects)
        self.assertTrue(any("Corpus Completeness" in d for d in report.defects))
        self.assertEqual(len(report.corpus_diagnostics), 1)
        self.assertFalse(report.corpus_diagnostics[0].is_clean)

    def test_clean_na_corpus_block_produces_no_defect(self):
        """A clean N/A corpus block does not add defects and enforce exits zero."""
        plan = _plan(
            changed=("docs/reviews/x.md",),
            material=("docs/reviews/x.md",),
        )
        buf = io.StringIO()
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_REVIEW_CLEAN_NA_CORPUS
        ):
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD", "--enforce"])
        self.assertEqual(rc, 0)

    def test_corpus_defect_enforce_exits_nonzero(self):
        """--enforce returns non-zero when a corpus defect is detected."""
        plan = _plan(
            changed=("docs/reviews/x.md",),
            material=("docs/reviews/x.md",),
        )
        buf = io.StringIO()
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_REVIEW_COMPLETE_CLAIM_NO_SECTION
        ):
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD", "--enforce"])
        self.assertEqual(rc, 1)

    def test_json_output_has_corpus_diagnostics_key(self):
        """JSON output includes corpusDiagnostics list."""
        plan = _plan(
            changed=("docs/reviews/x.md",),
            material=("docs/reviews/x.md",),
        )
        buf = io.StringIO()
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_REVIEW_CLEAN_NA_CORPUS
        ):
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD", "--json"])
        self.assertEqual(rc, 0)
        payload = json.loads(buf.getvalue())
        self.assertIn("corpusDiagnostics", payload)
        self.assertIsInstance(payload["corpusDiagnostics"], list)
        self.assertEqual(len(payload["corpusDiagnostics"]), 1)
        self.assertTrue(payload["corpusDiagnostics"][0]["isClean"])


class PacketShapeConstantDriftTests(unittest.TestCase):
    """AC6 drift tests: helper mirrors must match canonical dispatch-quality constants."""

    @classmethod
    def _load_dispatch_quality(cls):
        spec = importlib.util.spec_from_file_location(
            "check_work_order_dispatch_quality",
            _COMPAT_DIR / "check_work_order_dispatch_quality.py",
        )
        if spec is None or spec.loader is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_required_terms_mirror_matches_canonical(self):
        dq = self._load_dispatch_quality()
        self.assertIsNotNone(dq, "check_work_order_dispatch_quality could not be loaded")
        self.assertEqual(
            assist.WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS,
            dq.WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS,
        )

    def test_conditional_terms_mirror_matches_canonical(self):
        dq = self._load_dispatch_quality()
        self.assertIsNotNone(dq)
        self.assertEqual(
            assist.WORKER_RETURN_PACKET_SHAPE_CONDITIONAL_TERMS,
            dq.WORKER_RETURN_PACKET_SHAPE_CONDITIONAL_TERMS,
        )

    def test_contract_marker_mirror_matches_canonical(self):
        dq = self._load_dispatch_quality()
        self.assertIsNotNone(dq)
        self.assertEqual(
            assist.WORKER_RETURN_PACKET_SHAPE_CONTRACT_MARKER,
            dq.WORKER_RETURN_PACKET_SHAPE_CONTRACT_MARKER,
        )


class CorpusConstantDriftTests(unittest.TestCase):
    """Reviewer-added drift tests for corpus gate mirrors used by AAF-T2."""

    @classmethod
    def _load_corpus_checker(cls):
        spec = importlib.util.spec_from_file_location(
            "check_corpus_completeness_report_integrity",
            _COMPAT_DIR / "check_corpus_completeness_report_integrity.py",
        )
        if spec is None or spec.loader is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_corpus_constant_mirrors_match_canonical(self):
        corpus = self._load_corpus_checker()
        self.assertIsNotNone(corpus)
        self.assertEqual(assist.CORPUS_REQUIRED_SECTION, corpus.REQUIRED_SECTION)
        self.assertEqual(assist.CORPUS_APPLICABLE_PREFIXES, corpus.APPLICABLE_PREFIXES)
        self.assertEqual(assist.CORPUS_ALLOWED_VERDICTS, corpus.ALLOWED_VERDICTS)
        self.assertEqual(
            assist.CORPUS_ALLOWED_TERMINAL_STATUSES,
            corpus.ALLOWED_TERMINAL_STATUSES,
        )
        self.assertEqual(
            assist.CORPUS_REQUIRED_SECTION_FIELDS,
            corpus.REQUIRED_SECTION_FIELDS,
        )

    def test_corpus_complete_claim_pattern_mirrors_match_canonical(self):
        corpus = self._load_corpus_checker()
        self.assertIsNotNone(corpus)
        self.assertEqual(
            tuple(pattern.pattern for pattern in assist._CORPUS_COMPLETE_CLAIM_PATTERNS),
            corpus.COMPLETE_CLAIM_PATTERNS,
        )


_WORKER_RETURN_MISSING_RETRO = (
    "# Worker Return\n\n"
    "Status: COMPLETE_PENDING_REVIEW\n\n"
    "Responds to work order: docs/work_orders/x.md\n\n"
    "## Findings\n\nDid the work.\n"
)

_WORKER_RETURN_WITH_RETRO = (
    "# Worker Return\n\n"
    "Status: COMPLETE_PENDING_REVIEW\n\n"
    "Responds to work order: docs/work_orders/x.md\n\n"
    "WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond normal gates; "
    "no gate surprise, no helper gap, no worktree contamination this return\n"
)


class WorkerExperienceHelperDiagnosticTests(unittest.TestCase):
    """AAF-T5: helper reports missing worker-experience retro early, read-only."""

    def test_missing_retro_token_produces_defect(self):
        plan = _plan(
            changed=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
            material=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_WORKER_RETURN_MISSING_RETRO
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertTrue(
            any("worker-experience retro" in d for d in report.defects), report.defects
        )

    def test_valid_retro_token_no_defect(self):
        plan = _plan(
            changed=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
            material=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_WORKER_RETURN_WITH_RETRO
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertFalse(
            any("worker-experience retro" in d for d in report.defects), report.defects
        )


class SignalReadoutTests(unittest.TestCase):
    """LSC-T3: helper exposes advisory signalReadout from existing helper diagnostics."""

    def _empty_plan_patch(self):
        return mock.patch.object(assist, "build_path_plan", return_value=_plan())

    def test_no_signal_gives_empty_readout(self):
        """No diagnostics on empty changed set -> empty signal_readout and no defects."""
        with self._empty_plan_patch():
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertEqual(report.signal_readout, ())
        self.assertEqual(report.defects, [])

    def test_worker_experience_missing_retro_yields_readout_item(self):
        """Missing worker-experience retro -> advisory READOUT_ONLY item in signal_readout."""
        plan = _plan(
            changed=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
            material=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_WORKER_RETURN_MISSING_RETRO
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        worker_exp_items = [
            item for item in report.signal_readout if item.source_surface == "worker-experience"
        ]
        self.assertGreater(len(worker_exp_items), 0)
        self.assertEqual(worker_exp_items[0].recommended_outcome, "READOUT_ONLY")

    def test_corpus_defect_yields_readout_item(self):
        """Corpus completeness defect -> advisory signal_readout item with corpus-completeness surface."""
        plan = _plan(
            changed=("docs/reviews/x.md",),
            material=("docs/reviews/x.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_REVIEW_COMPLETE_CLAIM_NO_SECTION
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        corpus_items = [
            item for item in report.signal_readout if item.source_surface == "corpus-completeness"
        ]
        self.assertGreater(len(corpus_items), 0)

    def test_json_output_has_signal_readout_key(self):
        """--json output must include signalReadout as a list (LSC-T3 contract)."""
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
        self.assertIn("signalReadout", payload)
        self.assertIsInstance(payload["signalReadout"], list)

    def test_human_output_has_learning_signal_readout_section(self):
        """Human output must include Learning Signal Readout section (LSC-T3 contract)."""
        buf = io.StringIO()
        with self._empty_plan_patch():
            with redirect_stdout(buf):
                rc = assist.main(["--base", "HEAD", "--head", "HEAD"])
        self.assertEqual(rc, 0)
        self.assertIn("Learning Signal Readout", buf.getvalue())

    def test_readout_items_are_not_blocking_by_default(self):
        """Routine helper-detectable items must have blocking=False (LSC-T4 policy)."""
        plan = _plan(
            changed=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
            material=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_WORKER_RETURN_MISSING_RETRO
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        self.assertTrue(len(report.signal_readout) > 0)
        self.assertFalse(any(item.blocking for item in report.signal_readout))

    def test_readout_outcomes_use_lsc_t4_vocabulary(self):
        """All recommended_outcome values must be valid LSC-T4 vocabulary terms."""
        _VALID_OUTCOMES = {
            "READOUT_ONLY",
            "WATCH_FOR_REPEAT",
            "GOVERNANCE_PROPOSAL_CANDIDATE",
            "RULE_CANDIDATE",
            "CHECKER_CANDIDATE",
            "WORK_ORDER_CANDIDATE",
            "CLOSURE_BLOCKER",
        }
        plan = _plan(
            changed=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
            material=("docs/reviews/x_WORKER_RETURN_2026-06-20.md",),
        )
        with mock.patch.object(assist, "build_path_plan", return_value=plan), mock.patch.object(
            assist, "_read_changed_text", return_value=_WORKER_RETURN_MISSING_RETRO
        ):
            report = assist.build_report("HEAD", "HEAD", "auto")
        for item in report.signal_readout:
            self.assertIn(
                item.recommended_outcome,
                _VALID_OUTCOMES,
                f"unexpected outcome: {item.recommended_outcome}",
            )


if __name__ == "__main__":
    unittest.main()
