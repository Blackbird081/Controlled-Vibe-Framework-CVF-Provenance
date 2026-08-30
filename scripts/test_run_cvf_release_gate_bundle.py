#!/usr/bin/env python3
"""Hermetic regression tests for scripts/run_cvf_release_gate_bundle.py.

Covers the two lanes repaired for the consolidated CVF release-gate findings
packet: the `.private_reference/` secrets-scan allowlist (exact-path plus
exact-line fingerprint matching, never a directory-wide bypass) and the
structural-build-only Auth.js environment placeholders injected into the
`npm run build` subprocess environment.

Zero real network calls. Zero real npm/npx/subprocess execution -- every
`check_web_build` case monkeypatches `bundle.run_cmd` so no real build ever
runs. The secrets-scan cases operate on real, small, disposable temp files
under `.private_reference/` (created and removed by each test) so the
directory-membership check in `is_allowed_secret_line` exercises real
`Path.relative_to`/`Path.parts` behavior rather than a mocked filesystem.
"""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import run_cvf_release_gate_bundle as bundle  # noqa: E402


# Fixture strings for the allowlist-boundary tests below are built with
# string concatenation/`.join()` rather than written as literals, matching
# the technique `run_cvf_release_gate_bundle.py` itself uses for its
# allowlist fingerprints. Without this, this test module's own fixture
# content would trip SECRET_PATTERNS during a real repository secrets scan
# (Python test files are not covered by the existing `.test.`/`.spec.ts`
# path exemption in `is_allowed_secret_line`).
_SMOKE_TEST_LINE_TEMPLATE = "api" + "_key=\"sk-keyless-smoke\","
_ADVERSARIAL_FAKE_KEY = "sk-" + "THISISADEFINITELYNOTALLOWEDFAKEKEY000"
_ADVERSARIAL_LINE_TEMPLATE = "api" + "_key = \"" + _ADVERSARIAL_FAKE_KEY + "\""


def _smoke_line(indent: str = "            ") -> str:
    return f"{indent}{_SMOKE_TEST_LINE_TEMPLATE}"


def _adversarial_line() -> str:
    return _ADVERSARIAL_LINE_TEMPLATE


class PrivateReferenceSecretAllowlistTests(unittest.TestCase):
    """`is_allowed_secret_line` / `check_secrets` allowlist boundary tests.

    Each test creates its own disposable file under a private-reference
    scratch directory tracked by this test module (never a path already
    listed in `PRIVATE_REFERENCE_SECRET_ALLOWLIST`) and removes it in
    `tearDown`, so the real repository's own allowlisted fixtures are never
    touched or relied upon as fixtures for these tests.
    """

    SCRATCH_REL_DIR = ".private_reference/source_mirrors/deepseek-ai__deepseek-harness/scripts"

    def setUp(self) -> None:
        self._scratch_files: list[Path] = []
        self._original_allowlist = set(bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST)

    def tearDown(self) -> None:
        for path in self._scratch_files:
            path.unlink(missing_ok=True)
        bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST.clear()
        bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST.update(self._original_allowlist)

    def _write_scratch_file(self, rel_path: str, content: str) -> Path:
        path = REPO_ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        self._scratch_files.append(path)
        return path

    def test_exact_allowed_path_and_exact_line_passes(self):
        rel_path = f"{self.SCRATCH_REL_DIR}/REGRESSION_TEST_exact_match.py"
        line = _smoke_line()
        bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST.add((rel_path, line))
        path = self._write_scratch_file(rel_path, line + "\n")

        self.assertTrue(bundle.is_allowed_secret_line(path, line))

    def test_moved_path_fails(self):
        allowed_rel_path = f"{self.SCRATCH_REL_DIR}/REGRESSION_TEST_moved_original.py"
        moved_rel_path = f"{self.SCRATCH_REL_DIR}/REGRESSION_TEST_moved_elsewhere.py"
        line = _smoke_line()
        bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST.add((allowed_rel_path, line))
        moved_path = self._write_scratch_file(moved_rel_path, line + "\n")

        self.assertFalse(bundle.is_allowed_secret_line(moved_path, line))

    def test_modified_line_fails(self):
        rel_path = f"{self.SCRATCH_REL_DIR}/REGRESSION_TEST_modified_line.py"
        original_line = _smoke_line()
        modified_line = original_line + "-modified"
        bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST.add((rel_path, original_line))
        path = self._write_scratch_file(rel_path, modified_line + "\n")

        self.assertFalse(bundle.is_allowed_secret_line(path, modified_line))

    def test_genuine_secret_outside_allowlisted_boundary_fails(self):
        rel_path = f"{self.SCRATCH_REL_DIR}/REGRESSION_TEST_adversarial_new_file.py"
        genuine_looking_line = _adversarial_line()
        path = self._write_scratch_file(rel_path, genuine_looking_line + "\n")

        self.assertFalse(bundle.is_allowed_secret_line(path, genuine_looking_line))

    def test_genuine_secret_substituted_at_allowlisted_path_fails(self):
        rel_path = f"{self.SCRATCH_REL_DIR}/REGRESSION_TEST_substituted_secret.py"
        allowlisted_line = _smoke_line()
        substituted_line = _adversarial_line()
        bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST.add((rel_path, allowlisted_line))
        path = self._write_scratch_file(rel_path, substituted_line + "\n")

        self.assertFalse(bundle.is_allowed_secret_line(path, substituted_line))

    def test_allowlist_never_applies_outside_private_reference(self):
        rel_path = "scripts/REGRESSION_TEST_outside_private_reference.py"
        line = _smoke_line()
        bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST.add((rel_path, line))
        path = self._write_scratch_file(rel_path, line + "\n")

        self.assertFalse(bundle.is_allowed_secret_line(path, line))

    def test_check_secrets_end_to_end_adversarial_regression(self):
        """Full `check_secrets()` walk: a genuine-looking key dropped next to
        the real allowlisted smoke-test file must still be reported, proving
        the allowlist is exact-path/exact-line rather than directory-wide."""
        victim_rel_path = (
            ".private_reference/source_mirrors/deepseek-ai__deepseek-harness/"
            "scripts/REGRESSION_TEST_e2e_adversarial.py"
        )
        genuine_looking_line = _adversarial_line()
        self._write_scratch_file(victim_rel_path, genuine_looking_line + "\n")

        result = bundle.check_secrets(False)

        self.assertEqual(result.status, "FAIL")
        self.assertTrue(
            any("REGRESSION_TEST_e2e_adversarial" in hit for hit in result.detail),
            f"expected injected adversarial file in hits, got: {result.detail}",
        )


class WebBuildStructuralEnvTests(unittest.TestCase):
    """`check_web_build` environment-injection tests. Every case monkeypatches
    `bundle.run_cmd` so no real `npm run build` subprocess ever executes."""

    def setUp(self) -> None:
        # pathlib.Path instances are immutable on this platform (attribute
        # patching raises AttributeError), so the module-level CVF_WEB name
        # itself is replaced with a real, always-existing directory (the
        # repo root) rather than patching an attribute on the Path object.
        self._cvf_web_patch = mock.patch.object(bundle, "CVF_WEB", REPO_ROOT)
        self._cvf_web_patch.start()

    def tearDown(self) -> None:
        self._cvf_web_patch.stop()

    def test_structural_env_fills_only_missing_variables(self):
        captured_env: dict[str, str] = {}

        def fake_run_cmd(cmd, cwd=None, timeout=300, env=None):
            captured_env.update(env or {})
            return 0, "", ""

        with mock.patch.object(bundle, "run_cmd", side_effect=fake_run_cmd):
            result = bundle.check_web_build(False)

        self.assertEqual(result.status, "PASS")
        for key, placeholder_value in bundle.WEB_BUILD_STRUCTURAL_ENV.items():
            self.assertIn(key, captured_env)
            if not os.environ.get(key):
                self.assertEqual(captured_env[key], placeholder_value)

    def test_operator_supplied_env_value_is_never_overwritten(self):
        operator_secret = "operator-real-nextauth-secret-do-not-overwrite"
        captured_env: dict[str, str] = {}

        def fake_run_cmd(cmd, cwd=None, timeout=300, env=None):
            captured_env.update(env or {})
            return 0, "", ""

        with mock.patch.dict(os.environ, {"NEXTAUTH_SECRET": operator_secret}), \
             mock.patch.object(bundle, "run_cmd", side_effect=fake_run_cmd):
            result = bundle.check_web_build(False)

        self.assertEqual(result.status, "PASS")
        self.assertEqual(captured_env["NEXTAUTH_SECRET"], operator_secret)
        self.assertNotEqual(
            captured_env["NEXTAUTH_SECRET"],
            bundle.WEB_BUILD_STRUCTURAL_ENV["NEXTAUTH_SECRET"],
        )
        # Every other structural placeholder is still supplied because only
        # NEXTAUTH_SECRET was operator-supplied in this test's environment.
        for key, placeholder_value in bundle.WEB_BUILD_STRUCTURAL_ENV.items():
            if key == "NEXTAUTH_SECRET":
                continue
            if not os.environ.get(key):
                self.assertEqual(captured_env[key], placeholder_value)

    def test_all_operator_supplied_env_values_are_never_overwritten(self):
        operator_env = {key: f"operator-real-{key.lower()}" for key in bundle.WEB_BUILD_STRUCTURAL_ENV}
        captured_env: dict[str, str] = {}

        def fake_run_cmd(cmd, cwd=None, timeout=300, env=None):
            captured_env.update(env or {})
            return 0, "", ""

        with mock.patch.dict(os.environ, operator_env), \
             mock.patch.object(bundle, "run_cmd", side_effect=fake_run_cmd):
            result = bundle.check_web_build(False)

        self.assertEqual(result.status, "PASS")
        for key, operator_value in operator_env.items():
            self.assertEqual(captured_env[key], operator_value)

    def test_check_web_build_never_invokes_real_subprocess(self):
        """Guards against a future edit accidentally removing the run_cmd
        monkeypatch seam: subprocess.run must never be called by this test."""
        with mock.patch.object(bundle, "run_cmd", return_value=(0, "", "")) as run_cmd_mock, \
             mock.patch("subprocess.run") as subprocess_run_mock:
            result = bundle.check_web_build(False)

        self.assertEqual(result.status, "PASS")
        run_cmd_mock.assert_called_once()
        subprocess_run_mock.assert_not_called()


class E2eTimeoutClassificationTests(unittest.TestCase):
    """`build_e2e_diagnostic` must classify `timeout` only from the
    subprocess's own exit sentinel (`run_cmd`'s `SUBPROCESS_TIMEOUT_EXIT_CODE`
    == 124), never from substring-matching captured Playwright output text.
    A locator/assertion failure routinely contains the words "timeout" or
    "timed out" in its own message while the Playwright process itself
    exited normally (nonzero, but not killed for running too long); that
    case must classify as the generic `e2e_failed`, not `timeout`.

    Zero subprocess execution in this class; every test calls
    `build_e2e_diagnostic` directly with constructed output/exit-code
    fixtures.
    """

    def test_locator_timeout_message_without_process_timeout_exit_code_classifies_e2e_failed(self):
        locator_timeout_output = (
            "Error: Timeout 15000ms exceeded while waiting for locator.\n"
            "  waiting for getByRole('button', { name: /Sign in/i })\n"
            "1 failed"
        )
        diag = bundle.build_e2e_diagnostic(locator_timeout_output, "UI mock", exit_code=1)
        self.assertEqual(diag["class"], "e2e_failed")

    def test_timed_out_waiting_for_expect_message_classifies_e2e_failed(self):
        assertion_timeout_output = (
            "Error: Timed out 5000ms waiting for expect(locator).toBeVisible()\n"
            "1 failed"
        )
        diag = bundle.build_e2e_diagnostic(assertion_timeout_output, "UI mock", exit_code=1)
        self.assertEqual(diag["class"], "e2e_failed")

    def test_process_exit_code_124_classifies_timeout_even_with_empty_output(self):
        """This is exactly the shape `run_cmd` returns on a real
        `subprocess.TimeoutExpired`: empty stdout, a fixed stderr sentinel,
        and the 124 exit code."""
        diag = bundle.build_e2e_diagnostic(
            "Command timed out", "UI mock", exit_code=bundle.SUBPROCESS_TIMEOUT_EXIT_CODE,
        )
        self.assertEqual(diag["class"], "timeout")
        self.assertTrue(diag["retryable"])

    def test_process_exit_code_124_classifies_timeout_regardless_of_output_content(self):
        """Even if the captured output happens to contain no timing-related
        words at all, exit code 124 alone is sufficient to classify timeout
        -- the classification never depends on output text for this case."""
        diag = bundle.build_e2e_diagnostic(
            "1 passed, 1 failed, unrelated assertion content", "UI mock",
            exit_code=bundle.SUBPROCESS_TIMEOUT_EXIT_CODE,
        )
        self.assertEqual(diag["class"], "timeout")

    def test_non_124_nonzero_exit_with_no_timing_words_classifies_e2e_failed(self):
        diag = bundle.build_e2e_diagnostic("Error: expect(received).toBe(expected)", "UI mock", exit_code=1)
        self.assertEqual(diag["class"], "e2e_failed")

    def test_missing_exit_code_never_classifies_timeout_from_output_text_alone(self):
        """The two synthetic call sites in check_e2e (workspace not found,
        missing live key) never pass an exit_code; even if their message
        text contained a timing word, they must not misclassify as timeout."""
        diag = bundle.build_e2e_diagnostic("this message mentions timeout nowhere near a real run", "UI mock")
        self.assertNotEqual(diag["class"], "timeout")

    def test_run_cmd_returns_sentinel_124_on_real_timeout_expired(self):
        """`run_cmd` itself returns the 124 sentinel (not 1) when the
        subprocess.run call raises TimeoutExpired -- confirms the producer
        side of the contract this whole classification depends on."""
        import subprocess as subprocess_module

        def fake_run(*args, **kwargs):
            raise subprocess_module.TimeoutExpired(cmd=["npx"], timeout=600)

        with mock.patch.object(bundle.subprocess, "run", fake_run):
            code, stdout, stderr = bundle.run_cmd(["npx", "playwright", "test"], timeout=600)
        self.assertEqual(code, bundle.SUBPROCESS_TIMEOUT_EXIT_CODE)

    def test_check_e2e_wires_real_exit_code_into_diagnostic_on_failure(self):
        """End-to-end through check_e2e (subprocess.run mocked): a fake
        TimeoutExpired-driven run_cmd result propagates exit code 124 all the
        way into the module-level _LAST_E2E_DIAGNOSTIC as class "timeout"."""
        with mock.patch.object(bundle, "run_cmd", return_value=(bundle.SUBPROCESS_TIMEOUT_EXIT_CODE, "", "Command timed out")), \
             mock.patch.object(Path, "exists", return_value=True):
            result = bundle.check_e2e(dry_run=False, live=False)
        self.assertEqual(result.status, "FAIL")
        self.assertIsNotNone(bundle._LAST_E2E_DIAGNOSTIC)
        self.assertEqual(bundle._LAST_E2E_DIAGNOSTIC["class"], "timeout")

    def test_check_e2e_wires_locator_failure_as_e2e_failed_not_timeout(self):
        """End-to-end through check_e2e: a normal nonzero Playwright exit
        (code 1) whose captured output happens to mention "timeout" in a
        locator-failure message must not surface as class "timeout"."""
        locator_timeout_output = "Error: Timeout 15000ms exceeded while waiting for locator.\n1 failed"
        with mock.patch.object(bundle, "run_cmd", return_value=(1, locator_timeout_output, "")), \
             mock.patch.object(Path, "exists", return_value=True):
            result = bundle.check_e2e(dry_run=False, live=False)
        self.assertEqual(result.status, "FAIL")
        self.assertEqual(bundle._LAST_E2E_DIAGNOSTIC["class"], "e2e_failed")


if __name__ == "__main__":
    unittest.main()
