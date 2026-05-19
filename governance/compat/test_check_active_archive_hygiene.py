#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().with_name("check_active_archive_hygiene.py")
SPEC = importlib.util.spec_from_file_location("check_active_archive_hygiene", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load module from {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ActiveArchiveHygieneTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temp_dir.name)
        (self.repo_root / "docs" / "reviews").mkdir(parents=True)
        (self.repo_root / "docs" / "reviews" / "archive").mkdir(parents=True)
        (self.repo_root / "docs" / "audits").mkdir(parents=True)
        (self.repo_root / "docs" / "reference").mkdir(parents=True)
        (self.repo_root / "governance" / "compat").mkdir(parents=True)

        (self.repo_root / "governance" / "compat" / "CVF_ACTIVE_WINDOW_REGISTRY.json").write_text(
            json.dumps({"windows": []}),
            encoding="utf-8",
        )
        (self.repo_root / "governance" / "compat" / "CVF_AUDIT_RETENTION_REGISTRY.json").write_text(
            json.dumps({"retainEvidencePaths": ["docs/audits/CVF_RETAINED_AUDIT_2026-01-01.md"]}),
            encoding="utf-8",
        )
        (self.repo_root / "governance" / "compat" / "CVF_REVIEW_RETENTION_REGISTRY.json").write_text(
            json.dumps({"retainEvidencePaths": ["docs/reviews/CVF_RETAINED_REVIEW_2026-01-01.md"]}),
            encoding="utf-8",
        )
        (self.repo_root / "governance" / "compat" / "CVF_ACTIVE_ARCHIVE_BASELINE.json").write_text(
            json.dumps(
                {
                    "files": {
                        "docs/reviews/CVF_BASELINE_BLOCKED_REVIEW_2026-01-01.md": {
                            "bucket": "archive_candidate",
                            "blocked": True,
                            "reason": "protected_reference",
                        }
                    }
                }
            ),
            encoding="utf-8",
        )

        (self.repo_root / "docs" / "reviews" / "CVF_OLD_REVIEW_2026-01-01.md").write_text(
            "old\n",
            encoding="utf-8",
        )
        (self.repo_root / "docs" / "reviews" / "CVF_RETAINED_REVIEW_2026-01-01.md").write_text(
            "retained\n",
            encoding="utf-8",
        )
        (self.repo_root / "docs" / "reviews" / "CVF_BASELINE_BLOCKED_REVIEW_2026-01-01.md").write_text(
            "blocked\n",
            encoding="utf-8",
        )
        (self.repo_root / "docs" / "audits" / "CVF_RETAINED_AUDIT_2026-01-01.md").write_text(
            "retained\n",
            encoding="utf-8",
        )
        (self.repo_root / "docs" / "reviews" / "archive" / "CVF_ARCHIVED_2026-01-01.md").write_text(
            "archived\n",
            encoding="utf-8",
        )
        (self.repo_root / "docs" / "reference" / "README.md").write_text("permanent\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_counts_stale_actionable_without_counting_retained_or_archived(self) -> None:
        with patch.object(MODULE, "REPO_ROOT", self.repo_root), patch.object(
            MODULE, "ACTIVE_WINDOW_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_ACTIVE_WINDOW_REGISTRY.json"
        ), patch.object(
            MODULE, "AUDIT_RETENTION_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_AUDIT_RETENTION_REGISTRY.json"
        ), patch.object(
            MODULE, "REVIEW_RETENTION_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_REVIEW_RETENTION_REGISTRY.json"
        ), patch.object(
            MODULE, "ACTIVE_ARCHIVE_BASELINE_PATH", self.repo_root / "governance" / "compat" / "CVF_ACTIVE_ARCHIVE_BASELINE.json"
        ), patch.object(MODULE, "_changed_paths", return_value=set()):
            report = MODULE.build_report(max_stale=10)

        self.assertEqual(report["staleActionableCount"], 1)
        self.assertEqual(report["staleBlockedCount"], 1)
        self.assertEqual(report["staleRetainedCount"], 2)
        self.assertTrue(report["compliant"])

    def test_fails_when_stale_backlog_exceeds_threshold(self) -> None:
        with patch.object(MODULE, "REPO_ROOT", self.repo_root), patch.object(
            MODULE, "ACTIVE_WINDOW_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_ACTIVE_WINDOW_REGISTRY.json"
        ), patch.object(
            MODULE, "AUDIT_RETENTION_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_AUDIT_RETENTION_REGISTRY.json"
        ), patch.object(
            MODULE, "REVIEW_RETENTION_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_REVIEW_RETENTION_REGISTRY.json"
        ), patch.object(
            MODULE, "ACTIVE_ARCHIVE_BASELINE_PATH", self.repo_root / "governance" / "compat" / "CVF_ACTIVE_ARCHIVE_BASELINE.json"
        ), patch.object(MODULE, "_changed_paths", return_value=set()):
            report = MODULE.build_report(max_stale=0)

        self.assertFalse(report["compliant"])
        self.assertEqual(report["violations"][0]["type"], "active_archive_backlog_exceeds_threshold")

    def test_can_fail_only_for_changed_stale_files(self) -> None:
        with patch.object(MODULE, "REPO_ROOT", self.repo_root), patch.object(
            MODULE, "ACTIVE_WINDOW_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_ACTIVE_WINDOW_REGISTRY.json"
        ), patch.object(
            MODULE, "AUDIT_RETENTION_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_AUDIT_RETENTION_REGISTRY.json"
        ), patch.object(
            MODULE, "REVIEW_RETENTION_REGISTRY_PATH", self.repo_root / "governance" / "compat" / "CVF_REVIEW_RETENTION_REGISTRY.json"
        ), patch.object(
            MODULE, "ACTIVE_ARCHIVE_BASELINE_PATH", self.repo_root / "governance" / "compat" / "CVF_ACTIVE_ARCHIVE_BASELINE.json"
        ), patch.object(
            MODULE,
            "_changed_paths",
            return_value={"docs/reviews/CVF_OLD_REVIEW_2026-01-01.md"},
        ):
            report = MODULE.build_report(max_stale=10, fail_on_changed_stale=True)

        self.assertFalse(report["compliant"])
        self.assertEqual(report["changedStaleCount"], 1)


if __name__ == "__main__":
    unittest.main()
