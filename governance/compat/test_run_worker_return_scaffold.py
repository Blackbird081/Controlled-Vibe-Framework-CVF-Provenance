from __future__ import annotations

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).resolve().with_name("run_worker_return_scaffold.py")
SPEC = importlib.util.spec_from_file_location("run_worker_return_scaffold", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
scaffold = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scaffold)


class WorkerReturnScaffoldTests(unittest.TestCase):
    def test_scaffold_text_has_required_headings(self):
        text = scaffold.build_scaffold("Example Worker Return")
        self.assertTrue(text.startswith("# Example Worker Return"))
        self.assertIn("dispatchWorkOrder:", text)
        self.assertIn("executionBaseHead:", text)
        for section in scaffold.WORKER_RETURN_SCAFFOLD_SECTIONS:
            self.assertIn(f"## {section}", text)
        self.assertIn("CVF_RECEIPT_PRESENT", text)
        self.assertIn("NOT_APPLICABLE_WITH_REASON", text)
        self.assertIn("## External Knowledge Intake Routing", text)
        self.assertIn("## Rescan Intelligence Hardening", text)
        self.assertIn("## Finding-To-Governance Learning Disposition", text)
        self.assertIn("## Epistemic Process Block", text)
        self.assertIn("## Worker Return Scaffold Effectiveness Measurement", text)
        self.assertIn("## Worker Return Jurisdiction Block", text)
        self.assertIn("## Machine Closure Package", text)
        self.assertIn("| TODO: fill before review | READ |", text)

    def test_external_knowledge_intake_routing_uses_required_row_label_shape(self):
        text = scaffold.build_scaffold("Example Worker Return")
        section_start = text.index("## External Knowledge Intake Routing")
        section_end = text.index("## Rescan Intelligence Hardening", section_start)
        section = text[section_start:section_end]
        self.assertIn("| Field | Value |", section)
        self.assertNotIn("| External item | Route | Local guard | Disposition | Claim boundary |", section)
        for required_row_label in (
            "Chain map",
            "Input type",
            "Chain map route",
            "Matching local-view guard",
            "Owner surface",
            "Disposition",
            "Claim boundary",
        ):
            self.assertIn(f"| {required_row_label} |", section)

    def test_delta_execution_claim_boundary_uses_required_field_table_shape(self):
        text = scaffold.build_scaffold("Example Worker Return")
        section_start = text.index("## Delta Execution Claim Boundary Control Block")
        section_end = text.index("## Public Export Disposition", section_start)
        section = text[section_start:section_end]
        self.assertIn("| Field | Disposition |", section)
        self.assertNotIn("executionBaseHead: `TODO_EXECUTION_BASE_HEAD`", section)
        for required_row_label in (
            "claimScope",
            "claimDisposition",
            "receiptEvidence",
            "actionEvidence",
            "invocationBoundary",
            "interceptionBoundary",
            "claimLanguage",
            "forbiddenExpansion",
        ):
            self.assertIn(f"| {required_row_label} |", section)

    def test_emit_prints_without_writing(self):
        real_open = open

        def guarded_open(file, mode="r", *args, **kwargs):
            if any(flag in mode for flag in ("w", "a", "x", "+")):
                raise AssertionError(f"emit attempted a write open: {file!r} mode={mode!r}")
            return real_open(file, mode, *args, **kwargs)

        buf = io.StringIO()
        with mock.patch("builtins.open", side_effect=guarded_open):
            with redirect_stdout(buf):
                rc = scaffold.main(["--emit"])
        self.assertEqual(rc, 0)
        self.assertIn("## Source Inventory", buf.getvalue())

    def test_write_creates_one_new_file_under_reviews(self):
        with tempfile.TemporaryDirectory() as tmp:
            reviews = Path(tmp) / "docs" / "reviews"
            reviews.mkdir(parents=True)
            target = reviews / "CVF_WORKER_RETURN_SAMPLE_2026-06-26.md"
            with mock.patch.object(scaffold, "REPO_ROOT", Path(tmp)):
                written = scaffold.write_scaffold(str(target))
            self.assertTrue(written.exists())
            body = written.read_text(encoding="utf-8")
            self.assertIn("## Actual Changed Set", body)
            self.assertEqual(list(reviews.glob("*.md")), [written])

    def test_write_refuses_overwrite_and_outside_reviews(self):
        with tempfile.TemporaryDirectory() as tmp:
            reviews = Path(tmp) / "docs" / "reviews"
            reviews.mkdir(parents=True)
            target = reviews / "EXISTING.md"
            target.write_text("original content", encoding="utf-8")
            with mock.patch.object(scaffold, "REPO_ROOT", Path(tmp)):
                with self.assertRaises(ValueError):
                    scaffold.write_scaffold(str(target))
            self.assertEqual(target.read_text(encoding="utf-8"), "original content")

            outside = Path(tmp) / "docs" / "baselines" / "X.md"
            outside.parent.mkdir(parents=True)
            with mock.patch.object(scaffold, "REPO_ROOT", Path(tmp)):
                with self.assertRaises(ValueError):
                    scaffold.write_scaffold(str(outside))
            self.assertFalse(outside.exists())

    def test_cli_requires_exactly_one_action(self):
        self.assertEqual(scaffold.main([]), 2)
        self.assertEqual(scaffold.main(["--emit", "--write", "docs/reviews/x.md"]), 2)


if __name__ == "__main__":
    unittest.main()
