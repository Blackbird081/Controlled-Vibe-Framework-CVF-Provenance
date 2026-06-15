#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().with_name("build_session_sync_pack.py")
SPEC = importlib.util.spec_from_file_location("build_session_sync_pack", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load module from {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _plan(protected: tuple[str, ...]):
    """Build a minimal PathPlan-like object with the protected paths set."""
    return MODULE._STEWARD.PathPlan(
        changed_paths=protected,
        material_paths=(),
        protected_session_paths=protected,
        trace_artifact_paths=(),
        mixed_material_and_session=False,
        exact_manifest_collision_risk=False,
        handoff_sync_only=bool(protected),
    )


class AuthorizedProtectedPathsTests(unittest.TestCase):
    def test_parses_protected_paths_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            handoff = root / "AGENT_HANDOFF_TEST.md"
            handoff.write_text(
                "## Core Guard Self-Protection Authorization\n\n"
                "Authorized scope: test.\n\n"
                "Protected paths:\n\n"
                "- `CVF_SESSION_MEMORY.md`\n"
                "- `CVF_SESSION/ACTIVE_SESSION_STATE.json`\n\n"
                "Operator authorization: test.\n",
                encoding="utf-8",
            )
            with patch.object(MODULE, "REPO_ROOT", root):
                paths = MODULE.authorized_protected_paths("AGENT_HANDOFF_TEST.md")
        self.assertEqual(
            paths,
            ("CVF_SESSION_MEMORY.md", "CVF_SESSION/ACTIVE_SESSION_STATE.json"),
        )

    def test_returns_empty_when_no_auth_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            handoff = root / "AGENT_HANDOFF_TEST.md"
            handoff.write_text("## Some Other Section\n\nno marker here\n", encoding="utf-8")
            with patch.object(MODULE, "REPO_ROOT", root):
                paths = MODULE.authorized_protected_paths("AGENT_HANDOFF_TEST.md")
        self.assertEqual(paths, ())

    def test_returns_empty_for_missing_handoff(self) -> None:
        self.assertEqual(MODULE.authorized_protected_paths(None), ())


class MissingAuthorizationTests(unittest.TestCase):
    def test_flags_unauthorized_protected_path(self) -> None:
        missing = MODULE._missing_authorizations(
            ("CVF_SESSION_MEMORY.md", "CVF_SESSION/new-entry.json"),
            ("CVF_SESSION_MEMORY.md",),
        )
        self.assertEqual(missing, ("CVF_SESSION/new-entry.json",))

    def test_no_missing_when_all_authorized(self) -> None:
        missing = MODULE._missing_authorizations(
            ("CVF_SESSION_MEMORY.md",),
            ("CVF_SESSION_MEMORY.md", "AGENT_HANDOFF_V19_2026-06-15.md"),
        )
        self.assertEqual(missing, ())


class MainModeTests(unittest.TestCase):
    def _run_main(self, argv: list[str], *, plan, drift, authorized):
        out = io.StringIO()
        with patch.object(MODULE, "build_path_plan", return_value=plan), \
            patch.object(
                MODULE, "validate_aggregate_matches_sources", return_value=drift
            ), \
            patch.object(MODULE, "_active_handoff_path", return_value="AGENT_HANDOFF.md"), \
            patch.object(MODULE, "authorized_protected_paths", return_value=authorized), \
            patch.object(sys, "argv", ["build_session_sync_pack.py", *argv]), \
            redirect_stdout(out):
            code = MODULE.main()
        return code, out.getvalue()

    def test_suggest_exit_zero_even_with_drift(self) -> None:
        code, text = self._run_main(
            ["--suggest"],
            plan=_plan(("CVF_SESSION_MEMORY.md",)),
            drift=["aggregate drifted"],
            authorized=("CVF_SESSION_MEMORY.md",),
        )
        self.assertEqual(code, 0)
        self.assertIn("DRIFT", text)

    def test_enforce_exit_zero_on_clean(self) -> None:
        code, text = self._run_main(
            ["--enforce"],
            plan=_plan(("CVF_SESSION_MEMORY.md",)),
            drift=[],
            authorized=("CVF_SESSION_MEMORY.md",),
        )
        self.assertEqual(code, 0)
        self.assertIn("COMPLIANT", text)

    def test_enforce_exit_one_on_drift(self) -> None:
        code, text = self._run_main(
            ["--enforce"],
            plan=_plan(("CVF_SESSION_MEMORY.md",)),
            drift=["aggregate drifted from sources"],
            authorized=("CVF_SESSION_MEMORY.md",),
        )
        self.assertEqual(code, 1)
        self.assertIn("VIOLATION", text)

    def test_enforce_exit_one_on_missing_authorization(self) -> None:
        code, text = self._run_main(
            ["--enforce"],
            plan=_plan(("CVF_SESSION/unauthorized.json",)),
            drift=[],
            authorized=("CVF_SESSION_MEMORY.md",),
        )
        self.assertEqual(code, 1)
        self.assertIn("MISSING", text)

    def test_plan_only_skips_drift(self) -> None:
        code, text = self._run_main(
            ["--plan-only"],
            plan=_plan(("CVF_SESSION_MEMORY.md",)),
            drift=["this drift must not be evaluated"],
            authorized=("CVF_SESSION_MEMORY.md",),
        )
        self.assertEqual(code, 0)
        self.assertIn("PLAN-ONLY", text)
        self.assertNotIn("this drift must not be evaluated", text)

    def test_default_mode_behaves_like_suggest(self) -> None:
        code, text = self._run_main(
            [],
            plan=_plan(()),
            drift=[],
            authorized=(),
        )
        self.assertEqual(code, 0)
        self.assertIn("ADVISORY", text)

    def test_manifest_prints_paste_block(self) -> None:
        code, text = self._run_main(
            ["--suggest"],
            plan=_plan(("CVF_SESSION_MEMORY.md",)),
            drift=[],
            authorized=(),
        )
        self.assertEqual(code, 0)
        self.assertIn("Protected paths:", text)
        self.assertIn("`CVF_SESSION_MEMORY.md`", text)


if __name__ == "__main__":
    unittest.main()
