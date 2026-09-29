#!/usr/bin/env python3
"""Tests for check_absorption_blindspot_control_presence.py (ADIF-0014)."""

from __future__ import annotations

import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "governance" / "compat"))

import check_absorption_blindspot_control_presence as checker


ARTIFACT_WITH_BOTH_BLOCKS = textwrap.dedent("""\
# Test Artifact With Both Blocks

Some content here.

## Mandatory Blind-Spot Control Block

- Gate 1: source enumerated
- Blind-spot verdict: CLEAR

## Corpus Completeness And Report Integrity

- Corpus task class: test
- Corpus verdict: COMPLETE_VERIFIED

## After Section

More content.
""")

ARTIFACT_MISSING_BOTH_BLOCKS = textwrap.dedent("""\
# Test Artifact Missing Both Blocks

Some content here without control blocks.

## Some Other Section

Content.
""")

ARTIFACT_WITH_ALLOWED_DISPOSITION = textwrap.dedent("""\
# Test Artifact With Allowed Disposition

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this artifact does not absorb legacy content.

## Corpus Completeness And Report Integrity

NOT_APPLICABLE_WITH_REASON: no corpus inventory in scope.

## After Section

More content.
""")

ARTIFACT_WITH_BLIND_SPOT_ONLY = textwrap.dedent("""\
# Test Artifact With Blind-Spot Only

## Mandatory Blind-Spot Control Block

- Gate 1: source enumerated
- Blind-spot verdict: CLEAR

## Other Section

Content.
""")


class TestArtifactReferencesAbsorptionSource(unittest.TestCase):
    """Tests for the content-based absorption source trigger.

    The real scenario is: a changed governed artifact *contains text* that
    references ``.private_reference/legacy/`` or ``.private_reference/external_repos/``
    paths, while no private file is in the git diff.  The checker must scan
    artifact content, not changed paths.
    """

    def test_returns_true_for_artifact_citing_legacy_path(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("# Test\n\nReferences `.private_reference/legacy/old.md` here.\n")
            f.flush()
            result = checker._artifact_references_absorption_source(f.name)
        Path(f.name).unlink()
        self.assertTrue(result)

    def test_returns_true_for_artifact_citing_external_repos_path(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("# Test\n\nSee .private_reference/external_repos/agent-skills/README.md\n")
            f.flush()
            result = checker._artifact_references_absorption_source(f.name)
        Path(f.name).unlink()
        self.assertTrue(result)

    def test_returns_false_for_artifact_without_absorption_references(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("# Test\n\nSome unrelated content.\n")
            f.flush()
            result = checker._artifact_references_absorption_source(f.name)
        Path(f.name).unlink()
        self.assertFalse(result)

    def test_returns_false_for_unreadable_file(self):
        result = checker._artifact_references_absorption_source("nonexistent/file.md")
        self.assertFalse(result)


class TestIntegrationContentTrigger(unittest.TestCase):
    """Integration test: a governed artifact cites absorption source paths in
    its text but no private file is changed.  The checker must still fire."""

    def test_governed_artifact_with_absorption_reference_missing_blocks(self):
        """A work-order-like artifact references .private_reference/legacy/
        but omits both required blocks.  _check_artifact must report
        violations."""
        artifact = textwrap.dedent("""\
        # Work Order Touching Legacy Source

        This work order authorizes absorption from
        `.private_reference/legacy/old_framework/README.md`.

        ## Some Other Section

        Content without control blocks.
        """)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(artifact)
            f.flush()
            violations = checker._check_artifact(f.name)
        Path(f.name).unlink()
        self.assertEqual(len(violations), 2)
        types = {v["type"] for v in violations}
        self.assertIn("MISSING_BLIND_SPOT_CONTROL_BLOCK", types)
        self.assertIn("MISSING_CORPUS_COMPLETENESS_BLOCK", types)

    def test_governed_artifact_with_absorption_reference_and_blocks_passes(self):
        """A work-order-like artifact references .private_reference/legacy/
        and carries both required blocks.  No violations."""
        artifact = textwrap.dedent("""\
        # Work Order Touching Legacy Source

        This work order authorizes absorption from
        `.private_reference/legacy/old_framework/README.md`.

        ## Mandatory Blind-Spot Control Block

        - Gate 1: source enumerated
        - Blind-spot verdict: CLEAR

        ## Corpus Completeness And Report Integrity

        - Corpus task class: test
        - Corpus verdict: COMPLETE_VERIFIED

        ## After Section

        Content.
        """)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(artifact)
            f.flush()
            violations = checker._check_artifact(f.name)
        Path(f.name).unlink()
        self.assertEqual(violations, [])

    def test_governed_artifact_with_absorption_reference_and_na_disposition_passes(self):
        """A work-order-like artifact references .private_reference/external_repos/
        and carries both required blocks with N/A dispositions.  No violations."""
        artifact = textwrap.dedent("""\
        # Work Order Touching External Repo

        This work order references
        `.private_reference/external_repos/agent-skills/README.md`.

        ## Mandatory Blind-Spot Control Block

        NOT_APPLICABLE_WITH_REASON: no legacy content absorbed.

        ## Corpus Completeness And Report Integrity

        NOT_APPLICABLE_WITH_REASON: no corpus inventory in scope.

        ## After Section

        Content.
        """)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(artifact)
            f.flush()
            violations = checker._check_artifact(f.name)
        Path(f.name).unlink()
        self.assertEqual(violations, [])


class TestIsGovernedArtifact(unittest.TestCase):
    def test_work_order_is_governed(self):
        self.assertTrue(checker._is_governed_artifact(
            "docs/work_orders/CVF_AGENT_WORK_ORDER_TEST.md"
        ))

    def test_baseline_is_governed(self):
        self.assertTrue(checker._is_governed_artifact(
            "docs/baselines/CVF_GC018_TEST.md"
        ))

    def test_review_is_governed(self):
        self.assertTrue(checker._is_governed_artifact(
            "docs/reviews/CVF_TEST_REVIEW.md"
        ))

    def test_archive_path_is_not_governed(self):
        self.assertFalse(checker._is_governed_artifact(
            "docs/reviews/archive/CVF_OLD_REVIEW.md"
        ))

    def test_non_markdown_is_not_governed(self):
        self.assertFalse(checker._is_governed_artifact(
            "governance/compat/check_something.py"
        ))

    def test_random_path_is_not_governed(self):
        self.assertFalse(checker._is_governed_artifact(
            "EXTENSIONS/some_file.ts"
        ))


class TestCheckArtifact(unittest.TestCase):
    def test_artifact_with_both_blocks_passes(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(ARTIFACT_WITH_BOTH_BLOCKS)
            f.flush()
            violations = checker._check_artifact(f.name)
        Path(f.name).unlink()
        self.assertEqual(violations, [])

    def test_artifact_missing_both_blocks_fails(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(ARTIFACT_MISSING_BOTH_BLOCKS)
            f.flush()
            violations = checker._check_artifact(f.name)
        Path(f.name).unlink()
        self.assertEqual(len(violations), 2)
        types = {v["type"] for v in violations}
        self.assertIn("MISSING_BLIND_SPOT_CONTROL_BLOCK", types)
        self.assertIn("MISSING_CORPUS_COMPLETENESS_BLOCK", types)

    def test_artifact_with_allowed_disposition_passes(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(ARTIFACT_WITH_ALLOWED_DISPOSITION)
            f.flush()
            violations = checker._check_artifact(f.name)
        Path(f.name).unlink()
        self.assertEqual(violations, [])

    def test_artifact_with_blind_spot_only_fails_for_corpus(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(ARTIFACT_WITH_BLIND_SPOT_ONLY)
            f.flush()
            violations = checker._check_artifact(f.name)
        Path(f.name).unlink()
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0]["type"], "MISSING_CORPUS_COMPLETENESS_BLOCK")


class TestExtractSection(unittest.TestCase):
    def test_extracts_section_content(self):
        text = "## Mandatory Blind-Spot Control Block\n\ntest content\n\n## Next Section\n"
        section = checker._extract_section(text, "## Mandatory Blind-Spot Control Block")
        self.assertIn("test content", section)
        self.assertNotIn("## Next Section", section)

    def test_returns_empty_for_missing_section(self):
        text = "## Other Heading\ncontent\n"
        section = checker._extract_section(text, "## Mandatory Blind-Spot Control Block")
        self.assertEqual(section, "")


class TestHasAllowedDisposition(unittest.TestCase):
    def test_returns_true_for_not_applicable(self):
        text = "## Mandatory Blind-Spot Control Block\n\nNOT_APPLICABLE_WITH_REASON: test\n"
        self.assertTrue(checker._has_allowed_disposition(text, "## Mandatory Blind-Spot Control Block"))

    def test_returns_true_for_skipped(self):
        text = "## Corpus Completeness And Report Integrity\n\nSKIPPED_WITH_REASON: test\n"
        self.assertTrue(checker._has_allowed_disposition(text, "## Corpus Completeness And Report Integrity"))

    def test_returns_false_for_missing_section(self):
        text = "## Other\ncontent\n"
        self.assertFalse(checker._has_allowed_disposition(text, "## Mandatory Blind-Spot Control Block"))

    def test_returns_false_for_section_without_disposition(self):
        text = "## Mandatory Blind-Spot Control Block\n\n- Gate 1: test\n- verdict: CLEAR\n"
        self.assertFalse(checker._has_allowed_disposition(text, "## Mandatory Blind-Spot Control Block"))


class TestRunCheckEndToEnd(unittest.TestCase):
    """End-to-end tests for run_check() with monkeypatched git helpers.

    Simulates the real scenario: a governed Markdown artifact appears in the
    git diff, its content references ``.private_reference/legacy/``, but it
    omits the required control blocks.  run_check() must return violations.

    This regression test guards against the original P0 defect where the
    checker only looked at changed *paths* (which never include gitignored
    ``.private_reference/`` files) instead of scanning artifact *content*.
    """

    def test_run_check_returns_violations_for_artifact_citing_legacy_without_blocks(self):
        fake_path = "docs/work_orders/CVF_FAKE_WORK_ORDER.md"
        fake_content = textwrap.dedent("""\
        # Fake Work Order

        This artifact references `.private_reference/legacy/old_framework/README.md`.

        ## Some Other Section

        Content without control blocks.
        """)

        original_git = checker._get_changed_name_status
        original_worktree = checker._get_worktree_name_status
        original_read = checker._read_rel

        def fake_changed_name_status(base, head):
            return {fake_path: {"A"}}

        def fake_worktree_name_status():
            return {}

        def fake_read_rel(path):
            if path == fake_path:
                return fake_content
            return original_read(path)

        try:
            checker._get_changed_name_status = fake_changed_name_status
            checker._get_worktree_name_status = fake_worktree_name_status
            checker._read_rel = fake_read_rel

            violations = checker.run_check(base="fake-base", head="fake-head")
        finally:
            checker._get_changed_name_status = original_git
            checker._get_worktree_name_status = original_worktree
            checker._read_rel = original_read

        self.assertEqual(len(violations), 2)
        types = {v["type"] for v in violations}
        self.assertIn("MISSING_BLIND_SPOT_CONTROL_BLOCK", types)
        self.assertIn("MISSING_CORPUS_COMPLETENESS_BLOCK", types)
        self.assertEqual(violations[0]["path"], fake_path)

    def test_run_check_returns_no_violations_when_artifact_has_blocks(self):
        fake_path = "docs/reviews/CVF_FAKE_REVIEW.md"
        fake_content = textwrap.dedent("""\
        # Fake Review

        This artifact references `.private_reference/external_repos/agent-skills/README.md`.

        ## Mandatory Blind-Spot Control Block

        - Gate 1: source enumerated
        - Blind-spot verdict: CLEAR

        ## Corpus Completeness And Report Integrity

        - Corpus task class: test
        - Corpus verdict: COMPLETE_VERIFIED

        ## After Section

        Content.
        """)

        original_git = checker._get_changed_name_status
        original_worktree = checker._get_worktree_name_status
        original_read = checker._read_rel

        def fake_changed_name_status(base, head):
            return {fake_path: {"M"}}

        def fake_worktree_name_status():
            return {}

        def fake_read_rel(path):
            if path == fake_path:
                return fake_content
            return original_read(path)

        try:
            checker._get_changed_name_status = fake_changed_name_status
            checker._get_worktree_name_status = fake_worktree_name_status
            checker._read_rel = fake_read_rel

            violations = checker.run_check(base="fake-base", head="fake-head")
        finally:
            checker._get_changed_name_status = original_git
            checker._get_worktree_name_status = original_worktree
            checker._read_rel = original_read

        self.assertEqual(violations, [])

    def test_run_check_silent_for_artifact_without_absorption_references(self):
        fake_path = "docs/work_orders/CVF_UNRELATED_WORK_ORDER.md"
        fake_content = textwrap.dedent("""\
        # Unrelated Work Order

        No absorption source references here.

        ## Some Section

        Content.
        """)

        original_git = checker._get_changed_name_status
        original_worktree = checker._get_worktree_name_status
        original_read = checker._read_rel

        def fake_changed_name_status(base, head):
            return {fake_path: {"A"}}

        def fake_worktree_name_status():
            return {}

        def fake_read_rel(path):
            if path == fake_path:
                return fake_content
            return original_read(path)

        try:
            checker._get_changed_name_status = fake_changed_name_status
            checker._get_worktree_name_status = fake_worktree_name_status
            checker._read_rel = fake_read_rel

            violations = checker.run_check(base="fake-base", head="fake-head")
        finally:
            checker._get_changed_name_status = original_git
            checker._get_worktree_name_status = original_worktree
            checker._read_rel = original_read

        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
