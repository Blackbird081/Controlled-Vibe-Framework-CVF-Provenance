"""
Focused tests for check_raw_memory_release_invariant.py.

Covers FPC-T3-C06 requirements:
- memory-write/raw-memory/reinjection surfaces fail without rawMemoryReleased=false;
- equals and colon false assertions pass;
- unrelated governed Markdown passes;
- archive paths are skipped;
- CLI --base/--head/--enforce/--json behavior;
- checker implementation stays read-only and network-free.
"""

from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from governance.compat import check_raw_memory_release_invariant as checker


GOVERNED_PATH = "docs/work_orders/test_memory_write.md"
ARCHIVE_PATH = "docs/work_orders/archive/test_memory_write.md"


def _doc(body: str) -> str:
    return f"""\
# Test Memory Artifact

Status: TEST

## Purpose

{body}
"""


class TestRawMemoryReleaseInvariantDetection(unittest.TestCase):

    def test_memory_write_without_false_assertion_detected(self) -> None:
        violations = checker.diagnose_raw_memory_release_invariant(
            GOVERNED_PATH,
            _doc("This memory-write artifact captures a durable memory signal."),
        )
        self.assertEqual([item["type"] for item in violations], ["raw_memory_release_false_missing"])

    def test_raw_memory_without_false_assertion_detected(self) -> None:
        violations = checker.diagnose_raw_memory_release_invariant(
            GOVERNED_PATH,
            _doc("This worker return discusses raw memory release boundaries."),
        )
        self.assertEqual([item["type"] for item in violations], ["raw_memory_release_false_missing"])

    def test_reinjection_without_false_assertion_detected(self) -> None:
        violations = checker.diagnose_raw_memory_release_invariant(
            GOVERNED_PATH,
            _doc("Memory reinjection and canReinject boundaries are discussed here."),
        )
        self.assertEqual([item["type"] for item in violations], ["raw_memory_release_false_missing"])

    def test_equals_false_assertion_passes(self) -> None:
        violations = checker.diagnose_raw_memory_release_invariant(
            GOVERNED_PATH,
            _doc("Memory retrieval packet. rawMemoryReleased=false"),
        )
        self.assertEqual(violations, [])

    def test_colon_false_assertion_passes(self) -> None:
        violations = checker.diagnose_raw_memory_release_invariant(
            GOVERNED_PATH,
            _doc("Memory retrieval packet. rawMemoryReleased: false"),
        )
        self.assertEqual(violations, [])

    def test_unrelated_governed_markdown_passes(self) -> None:
        violations = checker.diagnose_raw_memory_release_invariant(
            "docs/reviews/test_registry_review.md",
            _doc("This registry-only review does not discuss memory surfaces."),
        )
        self.assertEqual(violations, [])

    def test_archive_path_is_skipped(self) -> None:
        violations = checker.diagnose_raw_memory_release_invariant(
            ARCHIVE_PATH,
            _doc("This memory-write artifact lacks the invariant."),
        )
        self.assertEqual(violations, [])


class TestRawMemoryReleaseInvariantCli(unittest.TestCase):

    def _run_main(self, argv: list[str], doc_text: str) -> tuple[int, str]:
        with mock.patch.object(sys, "argv", ["check_raw_memory_release_invariant.py", *argv]), \
             mock.patch.object(checker, "_get_changed_name_status", return_value={GOVERNED_PATH: {"M"}}), \
             mock.patch.object(checker, "_get_worktree_name_status", return_value={}), \
             mock.patch.object(checker, "_read_rel", return_value=doc_text), \
             mock.patch.object(checker.Path, "exists", return_value=True), \
             mock.patch.object(checker.Path, "is_dir", return_value=False):
            output = io.StringIO()
            with redirect_stdout(output):
                rc = checker.main()
            return rc, output.getvalue()

    def test_non_enforcing_mode_reports_violation_but_returns_zero(self) -> None:
        rc, output = self._run_main(
            ["--base", "BASE", "--head", "HEAD"],
            _doc("Memory consolidation packet without invariant."),
        )
        self.assertEqual(rc, 0)
        self.assertIn("VIOLATION", output)

    def test_enforcing_mode_returns_nonzero_for_violation(self) -> None:
        rc, output = self._run_main(
            ["--base", "BASE", "--head", "HEAD", "--enforce"],
            _doc("Memory consolidation packet without invariant."),
        )
        self.assertEqual(rc, 2)
        self.assertIn("rawMemoryReleased=false", output)

    def test_json_mode_returns_structured_report(self) -> None:
        rc, output = self._run_main(
            ["--base", "BASE", "--head", "HEAD", "--json"],
            _doc("Memory consolidation packet without invariant."),
        )
        self.assertEqual(rc, 0)
        report = json.loads(output)
        self.assertEqual(report["violationCount"], 1)
        self.assertEqual(report["range"]["base"], "BASE")
        self.assertEqual(report["range"]["head"], "HEAD")

    def test_enforcing_mode_returns_zero_when_clean(self) -> None:
        rc, output = self._run_main(
            ["--base", "BASE", "--head", "HEAD", "--enforce"],
            _doc("Memory consolidation packet. rawMemoryReleased=false"),
        )
        self.assertEqual(rc, 0)
        self.assertIn("COMPLIANT", output)


class TestReadOnlyImplementationBoundary(unittest.TestCase):

    def test_checker_source_has_no_write_or_network_primitives(self) -> None:
        source = Path(checker.__file__).read_text(encoding="utf-8")
        forbidden_tokens = (
            ".write_text(",
            ".write_bytes(",
            "open(",
            "requests.",
            "urllib.",
            "socket.",
            "http.client",
        )
        for token in forbidden_tokens:
            with self.subTest(token=token):
                self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
