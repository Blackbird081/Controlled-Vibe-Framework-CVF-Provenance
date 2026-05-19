#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().with_name("check_active_session_state.py")
SPEC = importlib.util.spec_from_file_location("check_active_session_state", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load module from {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ActiveSessionStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temp_dir.name)
        self.first_read = "reviews/current.md"
        self.startup_guard = "guards/current.md"

        for rel in (
            "CVF_SESSION_MEMORY.md",
            "CVF_SESSION/ACTIVE_SESSION_STATE.json",
            "CVF_SESSION/READ_FIRST.md",
            "CVF_SESSION/REQUIRED_STARTUP_GUARDS.md",
            "AGENTS.md",
            "CLAUDE.md",
            "governance/compat/run_local_governance_hook_chain.py",
            "AGENT_HANDOFF_V8_2026-05-17.md",
            self.first_read,
            self.startup_guard,
        ):
            path = self.repo_root / rel
            path.parent.mkdir(parents=True, exist_ok=True)

        state = {
            "activeSessionFrontDoor": "CVF_SESSION_MEMORY.md",
            "activeStateRegistry": "CVF_SESSION/ACTIVE_SESSION_STATE.json",
            "activeHandoff": "AGENT_HANDOFF_V8_2026-05-17.md",
            "historicalHandoffArchive": "CVF_SESSION/handoffs/archive",
            "supersededHandoffs": ["CVF_SESSION/handoffs/archive/AGENT_HANDOFF.md"],
            "relatedHandoffs": [],
            "currentMode": "system_reconvergence_stop",
            "freezePosture": "governance_kernel_freeze_recommended",
            "requiredFirstReads": [self.first_read],
            "requiredStartupGuards": [self.startup_guard],
            "blockedWorkClasses": [
                "broad_external_knowledge_absorption",
                "public_claims_of_coherent_governed_capability_runtime",
            ],
        }
        (self.repo_root / "CVF_SESSION/ACTIVE_SESSION_STATE.json").write_text(
            json.dumps(state),
            encoding="utf-8",
        )
        (self.repo_root / "CVF_SESSION_MEMORY.md").write_text(
            "ACTIVE SESSION FRONT DOOR\nCVF_SESSION/ACTIVE_SESSION_STATE.json\n"
            "system_reconvergence_stop\ngovernance_kernel_freeze_recommended\n"
            "AGENT_HANDOFF_V8_2026-05-17.md\n",
            encoding="utf-8",
        )
        for rel in ("CVF_SESSION/READ_FIRST.md", "CVF_SESSION/REQUIRED_STARTUP_GUARDS.md", "AGENTS.md", "CLAUDE.md"):
            (self.repo_root / rel).write_text(
                "CVF_SESSION_MEMORY.md\nCVF_SESSION/ACTIVE_SESSION_STATE.json\n",
                encoding="utf-8",
            )
        (self.repo_root / "governance/compat/run_local_governance_hook_chain.py").write_text(
            "governance/compat/check_active_session_state.py\n",
            encoding="utf-8",
        )
        (self.repo_root / "CVF_SESSION/handoffs/archive").mkdir(parents=True, exist_ok=True)
        (self.repo_root / "CVF_SESSION/handoffs/archive/AGENT_HANDOFF.md").write_text(
            "Status: ARCHIVED\n",
            encoding="utf-8",
        )
        (self.repo_root / self.first_read).write_text("Memory class: POINTER_RECORD\n", encoding="utf-8")
        (self.repo_root / self.startup_guard).write_text("Memory class: POINTER_RECORD\n", encoding="utf-8")
        (self.repo_root / "AGENT_HANDOFF_V8_2026-05-17.md").write_text(
            "Status: ACTIVE - current\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_compliant_session_state_passes(self) -> None:
        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify()

        self.assertTrue(report["compliant"])
        self.assertEqual(report["activeHandoff"], "AGENT_HANDOFF_V8_2026-05-17.md")
        self.assertEqual(report["detectedActiveHandoffs"], ["AGENT_HANDOFF_V8_2026-05-17.md"])

    def test_multiple_active_handoffs_fail(self) -> None:
        (self.repo_root / "AGENT_HANDOFF_V7_2026-05-16.md").write_text(
            "Status: ACTIVE - stale\n",
            encoding="utf-8",
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root):
            report = MODULE._classify()

        self.assertFalse(report["compliant"])
        self.assertGreaterEqual(report["handoffViolationCount"], 1)

    def test_handoff_sync_commit_can_reference_parent_head(self) -> None:
        (self.repo_root / "AGENT_HANDOFF_V8_2026-05-17.md").write_text(
            "Status: ACTIVE - current\nCurrent HEAD: `parent123`\n",
            encoding="utf-8",
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root), patch.object(
            MODULE, "_git_head_sha", return_value="head4567890abcdef"
        ), patch.object(
            MODULE, "_git_parent_sha", return_value="parent12390abcdef"
        ), patch.object(
            MODULE, "_head_changed_path", return_value=True
        ):
            report = MODULE._classify()

        self.assertTrue(report["compliant"])
        self.assertFalse(report["headShaInHandoff"])
        self.assertTrue(report["parentShaInHandoff"])

    def test_non_handoff_commit_must_reference_current_head(self) -> None:
        (self.repo_root / "AGENT_HANDOFF_V8_2026-05-17.md").write_text(
            "Status: ACTIVE - current\nCurrent HEAD: `parent123`\n",
            encoding="utf-8",
        )

        with patch.object(MODULE, "REPO_ROOT", self.repo_root), patch.object(
            MODULE, "_git_head_sha", return_value="head4567890abcdef"
        ), patch.object(
            MODULE, "_git_parent_sha", return_value="parent12390abcdef"
        ), patch.object(
            MODULE, "_head_changed_path", return_value=False
        ):
            report = MODULE._classify()

        self.assertFalse(report["compliant"])
        self.assertEqual(report["handoffViolationCount"], 1)


if __name__ == "__main__":
    unittest.main()
