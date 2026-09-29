#!/usr/bin/env python3
"""Isolated tests for SOT3-ACT-A5 release integration.

Zero network calls. Zero real Vitest/provider invocations. Every test either
exercises the A5 adapter's pure validation/build functions directly with
constructed dict fixtures, or monkeypatches its subprocess call point with a
fake in-process function, or (for the release-bundle wiring tests) monkeypatches
`run_cvf_sot3_a5_release_proof.main` so no real subprocess/network path is ever
reached.

Authorization: docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_2026-07-13.md
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import run_cvf_sot3_a5_release_proof as a5  # noqa: E402
import run_cvf_sot3_a4_failure_recovery_proof as a4  # noqa: E402
import run_cvf_sot3_a3_live_proof as a3  # noqa: E402
import run_cvf_release_gate_bundle as bundle  # noqa: E402


def _passing_a4_live_receipt() -> dict:
    return {
        "overall": "PASS",
        "claim": "SOT3_FAILURE_RECOVERY_PROVEN_BOUNDED",
        "localNegativeGatePassed": True,
        "negativeCaseCount": 19,
        "zeroProviderCallCaseCount": 18,
        "rollbackProviderCallCount": 1,
        "recoveryProviderCallCount": 1,
        "providerProof": {
            "provider": "alibaba",
            "model": "qwen-flash",
            "httpStatus": 200,
            "success": True,
            "latencyMs": 2000,
        },
        "correlation": {
            "traceCount": 1,
            "packetIds": ["RP-000001"],
            "kernelDecisionIds": ["KD-000001"],
            "truthReceiptIds": ["RCPT-000001"],
            "truthReferenceIds": ["TREF-000001"],
            "flowPackageIds": ["DPKG-000001"],
        },
        "contextObservation": {
            "approvedContextIncluded": True,
        },
        "secretSafety": {
            "rawKeyPersisted": False,
            "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False,
            "fullPromptPersisted": False,
        },
    }


def _passing_a4_diagnostic() -> dict:
    return {
        "localNegativeGatePassed": True,
        "recoveryProviderCallCount": 1,
        "diagnostic": None,
    }


def _failed_a4_diagnostic(*, observed_call_count: int = 0) -> dict:
    """An A4 `build_diagnostic_receipt(...)` shape for a real A4-side
    failure (e.g. the live test process failed or produced no observation
    file), matching `run_cvf_sot3_a4_failure_recovery_proof.py`'s own
    `build_diagnostic_receipt` output exactly."""
    return {
        "schemaVersion": "cvf.sot3ActA4LiveDiagnostic.v1",
        "batchId": "SOT3-ACT-A4",
        "executionBaseHead": "abc1234",
        "startedAtUtc": "2026-08-30T00:00:00+00:00",
        "finishedAtUtc": "2026-08-30T00:00:01+00:00",
        "localNegativeGatePassed": True,
        "recoveryProviderCallCount": observed_call_count,
        "keyAliasUsed": "DASHSCOPE_API_KEY",
        "diagnostic": {
            "stage": "provider",
            "class": "unknown_error",
            "retryable": False,
            "userAction": "inspect_receipt",
            "safeMessage": "The live test process failed or did not produce an observation file. See captured stdout/stderr for a secret-safe summary.",
        },
        "secretSafety": {
            "rawKeyPersisted": False,
            "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False,
            "fullPromptPersisted": False,
        },
    }


class AdmissionValidationTests(unittest.TestCase):
    """Pure-function tests: zero subprocess, zero network."""

    def test_fully_passing_receipt_has_no_admission_failures(self):
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), _passing_a4_live_receipt())
        self.assertEqual(failures, [])

    def test_missing_diagnostic_flagged(self):
        failures = a5._classify_admission_failures(None, _passing_a4_live_receipt())
        self.assertIn("a4_diagnostic_missing_or_unreadable", failures)

    def test_missing_live_receipt_flagged_and_short_circuits(self):
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), None)
        self.assertIn("a4_live_receipt_missing_or_unreadable", failures)

    def test_wrong_negative_case_count_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["negativeCaseCount"] = 18
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_negative_case_count_mismatch", failures)

    def test_wrong_zero_call_count_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["zeroProviderCallCaseCount"] = 19
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_zero_provider_call_case_count_mismatch", failures)

    def test_wrong_rollback_count_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["rollbackProviderCallCount"] = 0
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_rollback_provider_call_count_mismatch", failures)

    def test_wrong_recovery_count_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["recoveryProviderCallCount"] = 2
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_recovery_provider_call_count_mismatch", failures)

    def test_http_status_not_200_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["providerProof"]["httpStatus"] = 500
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_http_status_not_200", failures)

    def test_provider_success_false_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["providerProof"]["success"] = False
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_provider_success_not_true", failures)

    def test_approved_context_not_included_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["contextObservation"]["approvedContextIncluded"] = False
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_approved_context_not_included", failures)

    def test_trace_count_below_minimum_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["correlation"]["traceCount"] = 0
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_trace_count_below_minimum", failures)

    def test_empty_owner_array_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["correlation"]["packetIds"] = []
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_owner_array_empty_or_missing:packetIds", failures)

    def test_missing_owner_array_flagged(self):
        receipt = _passing_a4_live_receipt()
        del receipt["correlation"]["truthReceiptIds"]
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_owner_array_empty_or_missing:truthReceiptIds", failures)

    def test_secret_safety_flag_true_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["secretSafety"]["rawKeyPersisted"] = True
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_secret_safety_flag_not_false:rawKeyPersisted", failures)

    def test_local_negative_gate_not_passed_flagged(self):
        diagnostic = _passing_a4_diagnostic()
        diagnostic["localNegativeGatePassed"] = False
        failures = a5._classify_admission_failures(diagnostic, _passing_a4_live_receipt())
        self.assertIn("a4_local_negative_gate_not_passed", failures)

    def test_overall_not_pass_flagged(self):
        receipt = _passing_a4_live_receipt()
        receipt["overall"] = "BLOCKED"
        failures = a5._classify_admission_failures(_passing_a4_diagnostic(), receipt)
        self.assertIn("a4_overall_not_pass", failures)


class CurrentModelAlignmentStructuralTests(unittest.TestCase):
    """Non-live structural regression: no active SOT3 A4 execution path may
    retain the obsolete `qwen3.7-flash` live target. Zero subprocess, zero
    network call -- these tests only read source text from disk.

    `qwen3.7-flash` remains a valid substring inside historical evidence
    filenames/receipts and inside prose that explicitly discusses the
    obsolete-model history (this file's own docstrings, session memory, and
    already-closed receipts), so this check is scoped to the one live source
    file A4's `--live` mode actually executes, not a repository-wide grep.
    """

    def test_a4_live_test_source_contains_no_obsolete_model_string(self):
        live_test_path = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web" / a4.LIVE_TEST_RELATIVE_PATH
        self.assertTrue(live_test_path.exists(), f"expected live test file at {live_test_path}")
        source = live_test_path.read_text(encoding="utf-8")
        self.assertNotIn(
            "qwen3.7-flash", source,
            "the SOT3-ACT-A3/A4 live test must target the current qwen-flash model, not the obsolete qwen3.7-flash",
        )
        self.assertIn(
            "qwen-flash", source,
            "the SOT3-ACT-A3/A4 live test must explicitly target qwen-flash",
        )

    def test_a4_live_test_relative_path_constant_is_current(self):
        """Guards the constant itself: if a future rename moves the live test
        file, this fails loudly instead of silently reading an empty path."""
        self.assertEqual(
            a4.LIVE_TEST_RELATIVE_PATH,
            "src/app/api/execute/route.sot3-activation.alibaba.live.test.ts",
        )

    def test_a3_live_proof_runner_source_contains_no_obsolete_model_string(self):
        """`scripts/run_cvf_sot3_a3_live_proof.py` is the one-use-permit
        Python runner that authorizes and drives the live test above; it must
        request the same current model."""
        runner_path = REPO_ROOT / "scripts" / "run_cvf_sot3_a3_live_proof.py"
        source = runner_path.read_text(encoding="utf-8")
        self.assertNotIn("qwen3.7-flash", source)
        self.assertIn("qwen-flash", source)


class LiveCollectionModeSubprocessShapeTests(unittest.TestCase):
    """Non-live structural/behavioral regression for the `--mode live`
    subprocess-shape requirement.

    `vitest.config.ts` excludes `src/**/*.live.test.{ts,tsx}` from collection
    entirely unless Vite `mode` is exactly `"live"` (its EAFR-R1D barrier).
    Without `--mode live` on the vitest invocation, the governed A3/A4
    runners would silently collect zero tests rather than reaching the
    one-use permit guard -- `--mode live` authorizes collection only. The
    receipt-bound runner permit and one-call orchestrator grant must both be
    present before provider execution is authorized.

    Every subprocess-spawning test below replaces `subprocess.run` with an
    in-process fake that returns immediately; no real npx/vitest/network
    process is ever spawned by this file.
    """

    def _capture_subprocess_cmd(self, module, *, returncode: int = 0):
        captured: dict[str, object] = {}

        class FakeCompletedProcess:
            def __init__(self):
                self.returncode = returncode
                self.stdout = ""
                self.stderr = ""

        def fake_run(cmd, **kwargs):
            captured["cmd"] = cmd
            captured["env"] = kwargs.get("env")
            return FakeCompletedProcess()

        return captured, mock.patch.object(module.subprocess, "run", fake_run)

    def test_a4_child_env_uses_dashscope_authority_when_aliases_conflict(self):
        captured, patcher = self._capture_subprocess_cmd(a4)
        with mock.patch.dict(os.environ, {
            "DASHSCOPE_API_KEY": "proven-dashscope-key",
            "ALIBABA_API_KEY": "stale-conflicting-key",
        }, clear=False), patcher, mock.patch.object(a4, "npx_executable", return_value="npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a4.run_live_test(Path(tmp) / "observation.json", Path(tmp) / "permit.json", Path(tmp) / "ledger.json")
        child_env = captured["env"]
        self.assertEqual(child_env["DASHSCOPE_API_KEY"], "proven-dashscope-key")
        self.assertNotIn("ALIBABA_API_KEY", child_env)

    def test_a3_child_env_uses_dashscope_authority_when_aliases_conflict(self):
        captured, patcher = self._capture_subprocess_cmd(a3)
        with mock.patch.dict(os.environ, {
            "DASHSCOPE_API_KEY": "proven-dashscope-key",
            "ALIBABA_API_KEY": "stale-conflicting-key",
        }, clear=False), patcher, mock.patch.object(a3.shutil, "which", return_value="npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a3.run_live_test(Path(tmp) / "observation.json", Path(tmp) / "permit.json", Path(tmp) / "ledger.json")
        child_env = captured["env"]
        self.assertEqual(child_env["DASHSCOPE_API_KEY"], "proven-dashscope-key")
        self.assertNotIn("ALIBABA_API_KEY", child_env)

    def test_a4_child_env_composes_one_call_provider_grant_with_runner_permit(self):
        captured, patcher = self._capture_subprocess_cmd(a4)
        with patcher, mock.patch.object(a4, "npx_executable", return_value="npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a4.run_live_test(Path(tmp) / "observation.json", Path(tmp) / "permit.json", Path(tmp) / "ledger.json")
        child_env = captured["env"]
        grant = json.loads(child_env["CVF_PROVIDER_EXECUTION_GRANT_JSON"])
        self.assertEqual(grant["authority"], "ORCHESTRATOR_GRANT_REQUIRED")
        self.assertEqual(grant["authorizedBy"], "ORCHESTRATOR")
        self.assertEqual(grant["allowedProviders"], ["alibaba"])
        self.assertEqual(grant["maxCalls"], 1)
        self.assertEqual(grant["grantId"], child_env["CVF_PROVIDER_EXECUTION_GRANT_ID"])
        self.assertEqual(grant["subjectAgentId"], child_env["CVF_AGENT_ID"])
        self.assertEqual(grant["delegationId"], child_env["CVF_DELEGATION_ID"])

    def test_a3_child_env_composes_one_call_provider_grant_with_runner_permit(self):
        captured, patcher = self._capture_subprocess_cmd(a3)
        with patcher, mock.patch.object(a3.shutil, "which", return_value="npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a3.run_live_test(Path(tmp) / "observation.json", Path(tmp) / "permit.json", Path(tmp) / "ledger.json")
        child_env = captured["env"]
        grant = json.loads(child_env["CVF_PROVIDER_EXECUTION_GRANT_JSON"])
        self.assertEqual(grant["allowedProviders"], ["alibaba"])
        self.assertEqual(grant["maxCalls"], 1)
        self.assertEqual(grant["grantId"], child_env["CVF_PROVIDER_EXECUTION_GRANT_ID"])
        self.assertEqual(grant["subjectAgentId"], child_env["CVF_AGENT_ID"])
        self.assertEqual(grant["delegationId"], child_env["CVF_DELEGATION_ID"])

    def test_a4_run_live_test_argv_contains_mode_live(self):
        captured, patcher = self._capture_subprocess_cmd(a4)
        with patcher, mock.patch.object(a4, "npx_executable", return_value="/usr/bin/npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a4.run_live_test(
                    Path(tmp) / "observation.json",
                    Path(tmp) / "permit.json",
                    Path(tmp) / "ledger.json",
                )
        cmd = captured["cmd"]
        self.assertIn("--mode", cmd)
        mode_index = cmd.index("--mode")
        self.assertEqual(cmd[mode_index + 1], "live")

    def test_a3_run_live_test_argv_contains_mode_live(self):
        captured, patcher = self._capture_subprocess_cmd(a3)
        with patcher, mock.patch.object(a3.shutil, "which", return_value="/usr/bin/npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a3.run_live_test(
                    Path(tmp) / "observation.json",
                    Path(tmp) / "permit.json",
                    Path(tmp) / "ledger.json",
                )
        cmd = captured["cmd"]
        self.assertIn("--mode", cmd)
        mode_index = cmd.index("--mode")
        self.assertEqual(cmd[mode_index + 1], "live")

    def test_a4_argv_still_names_the_explicit_live_test_path(self):
        captured, patcher = self._capture_subprocess_cmd(a4)
        with patcher, mock.patch.object(a4, "npx_executable", return_value="/usr/bin/npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a4.run_live_test(
                    Path(tmp) / "observation.json",
                    Path(tmp) / "permit.json",
                    Path(tmp) / "ledger.json",
                )
        self.assertIn(a4.LIVE_TEST_RELATIVE_PATH, captured["cmd"])

    def test_a3_argv_still_names_the_explicit_live_test_path(self):
        captured, patcher = self._capture_subprocess_cmd(a3)
        with patcher, mock.patch.object(a3.shutil, "which", return_value="/usr/bin/npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a3.run_live_test(
                    Path(tmp) / "observation.json",
                    Path(tmp) / "permit.json",
                    Path(tmp) / "ledger.json",
                )
        self.assertIn(a3.LIVE_TEST_RELATIVE_PATH, captured["cmd"])

    def test_a4_argv_shape_matches_required_command(self):
        """Exact required shape: [npx, "vitest", "run", "--mode", "live", LIVE_TEST_RELATIVE_PATH]."""
        captured, patcher = self._capture_subprocess_cmd(a4)
        with patcher, mock.patch.object(a4, "npx_executable", return_value="npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a4.run_live_test(
                    Path(tmp) / "observation.json",
                    Path(tmp) / "permit.json",
                    Path(tmp) / "ledger.json",
                )
        self.assertEqual(
            captured["cmd"],
            ["npx", "vitest", "run", "--mode", "live", a4.LIVE_TEST_RELATIVE_PATH],
        )

    def test_a3_argv_shape_matches_required_command(self):
        """Exact required shape: [npx, "vitest", "run", "--mode", "live", LIVE_TEST_RELATIVE_PATH]."""
        captured, patcher = self._capture_subprocess_cmd(a3)
        with patcher, mock.patch.object(a3.shutil, "which", return_value="npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a3.run_live_test(
                    Path(tmp) / "observation.json",
                    Path(tmp) / "permit.json",
                    Path(tmp) / "ledger.json",
                )
        self.assertEqual(
            captured["cmd"],
            ["npx", "vitest", "run", "--mode", "live", a3.LIVE_TEST_RELATIVE_PATH],
        )

    def test_a4_argv_never_contains_a_second_run_cmd_style_bare_default_mode(self):
        """Regression guard: a future edit must not silently drop `--mode
        live` back to a bare `vitest run <path>` invocation, which the
        config's collection barrier would exclude entirely."""
        captured, patcher = self._capture_subprocess_cmd(a4)
        with patcher, mock.patch.object(a4, "npx_executable", return_value="npx"):
            with tempfile.TemporaryDirectory() as tmp:
                a4.run_live_test(
                    Path(tmp) / "observation.json",
                    Path(tmp) / "permit.json",
                    Path(tmp) / "ledger.json",
                )
        self.assertNotEqual(captured["cmd"], ["npx", "vitest", "run", a4.LIVE_TEST_RELATIVE_PATH])

    def test_vitest_config_excludes_live_pattern_by_default_mode(self):
        """Default (non-live) collection remains excluded: reads
        `vitest.config.ts` source directly (no subprocess) and confirms the
        live-test glob is still conditioned on `mode === 'live'`, i.e. the
        collection barrier itself was not weakened or removed by this
        repair."""
        config_path = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web" / "vitest.config.ts"
        source = config_path.read_text(encoding="utf-8")
        self.assertIn("mode === 'live'", source)
        self.assertIn("src/**/*.live.test.{ts,tsx}", source)

    def test_direct_mode_live_execution_without_permit_env_vars_only_runs_guard(self):
        """A direct `--mode live` invocation with none of the permit env vars
        set must still refuse to run the real provider test: the live test
        file's own `consumeRunnerPermit()`/`RUNNER_PERMIT` gate returns
        `authorized: false` whenever the permit path/token/observation-path
        env vars are absent, which is exactly the state of a bare `--mode
        live` run started outside either governed runner. This is a
        source-level assertion (the guard function's control flow), not a
        real vitest process spawn -- collection-mode selection and
        provider-execution authorization are intentionally two separate,
        independently-testable gates."""
        live_test_path = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web" / a4.LIVE_TEST_RELATIVE_PATH
        source = live_test_path.read_text(encoding="utf-8")
        self.assertIn("function consumeRunnerPermit(): RunnerPermitResult {", source)
        self.assertIn("if (!permitPath || !permitToken || !observationPath) {", source)
        self.assertIn("return { authorized: false, reason: 'runner permit variables absent' };", source)
        self.assertIn("describe.skipIf(!RUNNER_PERMIT.authorized || !ALIBABA_API_KEY)(", source)
        # The permit guard describe block runs unconditionally (never
        # skipIf'd on the permit itself); only the real-provider describe
        # block is skipped when the permit/key are absent.
        self.assertIn("describe.skipIf(RUNNER_PERMIT.authorized)('SOT3-ACT-A3 runner permit guard', () => {", source)

    def test_no_test_in_this_module_invokes_network_or_provider(self):
        """Structural self-check: every test in this class replaces
        `subprocess.run` with an in-process fake before calling
        `run_live_test`, so no real npx/vitest process -- and therefore no
        real network or provider call -- is ever reachable from this file."""
        import inspect
        source = inspect.getsource(LiveCollectionModeSubprocessShapeTests)
        # Every call site that reaches run_live_test must be inside a body
        # that also patches subprocess.run via _capture_subprocess_cmd.
        run_live_test_call_count = source.count(".run_live_test(")
        capture_helper_call_count = source.count("_capture_subprocess_cmd(")
        self.assertGreater(run_live_test_call_count, 0)
        self.assertGreaterEqual(capture_helper_call_count, run_live_test_call_count)


class ResultAndDiagnosticBuildTests(unittest.TestCase):
    """Pure-function tests for the A5 result/diagnostic shape builders."""

    def test_build_a5_result_pass_shape(self):
        result = a5.build_a5_result(
            started_at="2026-07-13T00:00:00+00:00",
            finished_at="2026-07-13T00:00:01+00:00",
            a4_returncode=0,
            diagnostic=_passing_a4_diagnostic(),
            live_receipt=_passing_a4_live_receipt(),
            admission_failures=[],
        )
        self.assertEqual(result["sot3"]["overall"], "PASS")
        self.assertEqual(result["sot3"]["negativeCaseCount"], 19)
        self.assertEqual(result["sot3"]["zeroProviderCallCaseCount"], 18)
        self.assertEqual(result["sot3"]["rollbackProviderCallCount"], 1)
        self.assertEqual(result["sot3"]["recoveryProviderCallCount"], 1)
        self.assertTrue(result["sot3"]["approvedContextIncluded"])
        self.assertTrue(result["sot3"]["durableOwnerCorrelationComplete"])
        self.assertEqual(result["sot3"]["httpStatus"], 200)
        for value in result["secretSafety"].values():
            self.assertFalse(value)

    def test_build_a5_result_fail_shape_on_admission_failures(self):
        result = a5.build_a5_result(
            started_at="2026-07-13T00:00:00+00:00",
            finished_at="2026-07-13T00:00:01+00:00",
            a4_returncode=0,
            diagnostic=_passing_a4_diagnostic(),
            live_receipt=_passing_a4_live_receipt(),
            admission_failures=["a4_http_status_not_200"],
        )
        self.assertEqual(result["sot3"]["overall"], "FAIL")
        self.assertIn("a4_http_status_not_200", result["sot3"]["admissionFailures"])

    def test_build_a5_result_fail_shape_on_nonzero_a4_returncode(self):
        result = a5.build_a5_result(
            started_at="2026-07-13T00:00:00+00:00",
            finished_at="2026-07-13T00:00:01+00:00",
            a4_returncode=1,
            diagnostic=None,
            live_receipt=None,
            admission_failures=["a4_diagnostic_missing_or_unreadable", "a4_live_receipt_missing_or_unreadable"],
        )
        self.assertEqual(result["sot3"]["overall"], "FAIL")
        self.assertIsNone(result["sot3"]["claim"])

    def test_build_diagnostic_pass_has_null_diagnostic(self):
        diag = a5.build_diagnostic(
            started_at="2026-07-13T00:00:00+00:00",
            a4_returncode=0,
            admission_failures=[],
            diagnostic=_passing_a4_diagnostic(),
        )
        self.assertIsNone(diag["diagnostic"])
        self.assertEqual(diag["admissionFailures"], [])
        for value in diag["secretSafety"].values():
            self.assertFalse(value)

    def test_build_diagnostic_failure_has_classified_stage(self):
        diag = a5.build_diagnostic(
            started_at="2026-07-13T00:00:00+00:00",
            a4_returncode=0,
            admission_failures=["a4_http_status_not_200"],
            diagnostic=_passing_a4_diagnostic(),
        )
        self.assertIsNotNone(diag["diagnostic"])
        self.assertEqual(diag["diagnostic"]["stage"], "output_validation")
        self.assertEqual(diag["diagnostic"]["class"], "output_validation_failed")
        self.assertFalse(diag["diagnostic"]["retryable"])

    def test_build_diagnostic_a4_process_failure_has_provider_stage(self):
        diag = a5.build_diagnostic(
            started_at="2026-07-13T00:00:00+00:00",
            a4_returncode=1,
            admission_failures=["a4_diagnostic_missing_or_unreadable"],
            diagnostic=None,
        )
        self.assertEqual(diag["diagnostic"]["stage"], "provider")
        self.assertEqual(diag["diagnostic"]["class"], "unknown_error")

    def test_a4_nonzero_with_diagnostic_and_no_live_receipt_preserves_underlying_diagnostic(self):
        """A4 exits nonzero with a real diagnostic but no live receipt (the
        exact `a4_live_receipt_missing_or_unreadable` scenario): A4's own
        stage/class/retryable/userAction/safeMessage must survive into A5's
        diagnostic rather than being replaced by a generic message alone."""
        a4_diag = _failed_a4_diagnostic(observed_call_count=0)
        admission_failures = a5._classify_admission_failures(a4_diag, None)
        self.assertIn("a4_live_receipt_missing_or_unreadable", admission_failures)

        diag = a5.build_diagnostic(
            started_at="2026-08-30T00:00:00+00:00",
            a4_returncode=1,
            admission_failures=admission_failures,
            diagnostic=a4_diag,
        )
        self.assertIsNotNone(diag["underlyingA4Diagnostic"])
        self.assertEqual(diag["underlyingA4Diagnostic"]["stage"], "provider")
        self.assertEqual(diag["underlyingA4Diagnostic"]["class"], "unknown_error")
        self.assertEqual(diag["underlyingA4Diagnostic"]["retryable"], False)
        self.assertEqual(diag["underlyingA4Diagnostic"]["userAction"], "inspect_receipt")
        self.assertIn("did not produce an observation file", diag["underlyingA4Diagnostic"]["safeMessage"])
        # A5 must not tell the operator to inspect a file it has already
        # deleted, now that the underlying diagnostic is embedded above.
        self.assertNotIn("its own secret-safe diagnostic for the underlying stage/class", diag["diagnostic"]["safeMessage"])

    def test_missing_diagnostic_after_a4_nonzero_remains_fail_closed_with_no_underlying_diagnostic(self):
        """When A4's diagnostic itself is missing/unreadable (not just the
        live receipt), there is nothing to preserve; the result must still
        fail closed and `underlyingA4Diagnostic` must be None, never a
        fabricated or partially-filled object."""
        diag = a5.build_diagnostic(
            started_at="2026-08-30T00:00:00+00:00",
            a4_returncode=1,
            admission_failures=["a4_diagnostic_missing_or_unreadable", "a4_live_receipt_missing_or_unreadable"],
            diagnostic=None,
        )
        self.assertIsNone(diag["underlyingA4Diagnostic"])
        self.assertIsNone(diag["a4LocalNegativeGatePassed"])
        self.assertIsNone(diag["a4RecoveryProviderCallCount"])
        self.assertIsNotNone(diag["diagnostic"])
        self.assertEqual(diag["diagnostic"]["stage"], "provider")

    def test_observed_call_count_zero_is_preserved_not_treated_as_falsy_missing(self):
        """0 is a meaningful, distinct observed-call-count value (no call was
        made yet) and must not collapse to None/missing."""
        a4_diag = _failed_a4_diagnostic(observed_call_count=0)
        diag = a5.build_diagnostic(
            started_at="t0", a4_returncode=1,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
            diagnostic=a4_diag,
        )
        self.assertEqual(diag["a4RecoveryProviderCallCount"], 0)

        result = a5.build_a5_result(
            started_at="t0", finished_at="t1", a4_returncode=1,
            diagnostic=a4_diag, live_receipt=None,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
        )
        self.assertEqual(result["sot3"]["recoveryProviderCallCount"], 0)

    def test_observed_call_count_one_is_preserved_when_live_receipt_missing(self):
        """1 real observed call (the provider call happened) must still be
        visible even though the observation/receipt file was never written
        or was unreadable."""
        a4_diag = _failed_a4_diagnostic(observed_call_count=1)
        diag = a5.build_diagnostic(
            started_at="t0", a4_returncode=1,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
            diagnostic=a4_diag,
        )
        self.assertEqual(diag["a4RecoveryProviderCallCount"], 1)

        result = a5.build_a5_result(
            started_at="t0", finished_at="t1", a4_returncode=1,
            diagnostic=a4_diag, live_receipt=None,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
        )
        self.assertEqual(result["sot3"]["recoveryProviderCallCount"], 1)

    def test_recovery_call_count_prefers_live_receipt_over_diagnostic_when_both_present(self):
        """When a live receipt exists, it remains the authoritative source
        for recoveryProviderCallCount (unchanged successful-path behavior);
        the diagnostic fallback only applies when there is no live receipt."""
        live_receipt = _passing_a4_live_receipt()
        live_receipt["recoveryProviderCallCount"] = 1
        a4_diag = _passing_a4_diagnostic()
        a4_diag["recoveryProviderCallCount"] = 99  # must never leak through
        result = a5.build_a5_result(
            started_at="t0", finished_at="t1", a4_returncode=0,
            diagnostic=a4_diag, live_receipt=live_receipt,
            admission_failures=[],
        )
        self.assertEqual(result["sot3"]["recoveryProviderCallCount"], 1)

    def test_successful_a5_path_diagnostic_shape_unchanged(self):
        """Successful A5 behavior is unchanged: null diagnostic, null
        underlyingA4Diagnostic (A4 itself reported no failure), and the
        existing a4LocalNegativeGatePassed/admissionFailures fields intact."""
        diag = a5.build_diagnostic(
            started_at="2026-07-13T00:00:00+00:00",
            a4_returncode=0,
            admission_failures=[],
            diagnostic=_passing_a4_diagnostic(),
        )
        self.assertIsNone(diag["diagnostic"])
        self.assertIsNone(diag["underlyingA4Diagnostic"])
        self.assertTrue(diag["a4LocalNegativeGatePassed"])
        self.assertEqual(diag["a4RecoveryProviderCallCount"], 1)
        self.assertEqual(diag["admissionFailures"], [])

    def test_underlying_a4_diagnostic_never_carries_secret_fields(self):
        """When A4's raw diagnostic carries none of the four optional
        context fields, the preserved underlying diagnostic is restricted to
        exactly the five required keys; it never forwards secretSafety,
        keyAliasUsed, or any other field from A4's raw diagnostic payload."""
        a4_diag = _failed_a4_diagnostic(observed_call_count=1)
        diag = a5.build_diagnostic(
            started_at="t0", a4_returncode=1,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
            diagnostic=a4_diag,
        )
        self.assertEqual(
            set(diag["underlyingA4Diagnostic"].keys()),
            {"stage", "class", "retryable", "userAction", "safeMessage"},
        )
        serialized = json.dumps(diag)
        self.assertNotIn("keyAliasUsed", serialized)
        self.assertNotIn("DASHSCOPE_API_KEY", serialized)

    def test_underlying_a4_diagnostic_preserves_optional_fields_when_present(self):
        """provider/model/httpStatus/latencyMs are forwarded verbatim when
        A4's raw diagnostic sub-object actually carries them (a failure
        classified after a provider call attempt), completing the
        preservation contract beyond the five always-required fields."""
        a4_diag = _failed_a4_diagnostic(observed_call_count=1)
        a4_diag["diagnostic"]["provider"] = "alibaba"
        a4_diag["diagnostic"]["model"] = "qwen-flash"
        a4_diag["diagnostic"]["httpStatus"] = 503
        a4_diag["diagnostic"]["latencyMs"] = 4200

        diag = a5.build_diagnostic(
            started_at="t0", a4_returncode=1,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
            diagnostic=a4_diag,
        )
        underlying = diag["underlyingA4Diagnostic"]
        self.assertEqual(underlying["provider"], "alibaba")
        self.assertEqual(underlying["model"], "qwen-flash")
        self.assertEqual(underlying["httpStatus"], 503)
        self.assertEqual(underlying["latencyMs"], 4200)
        # Required fields remain present alongside the optional ones.
        self.assertEqual(underlying["stage"], "provider")
        self.assertEqual(underlying["class"], "unknown_error")

    def test_underlying_a4_diagnostic_omits_absent_optional_fields_rather_than_nulling_them(self):
        """An optional field A4 never set is omitted from the projection
        entirely (no key at all), not present as `None` -- distinguishing
        "not applicable to this failure" from "present but unknown"."""
        a4_diag = _failed_a4_diagnostic(observed_call_count=0)
        # Only `model` is present on this diagnostic; provider/httpStatus/
        # latencyMs were never set by A4 for this particular failure.
        a4_diag["diagnostic"]["model"] = "qwen-flash"

        diag = a5.build_diagnostic(
            started_at="t0", a4_returncode=1,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
            diagnostic=a4_diag,
        )
        underlying = diag["underlyingA4Diagnostic"]
        self.assertIn("model", underlying)
        self.assertEqual(underlying["model"], "qwen-flash")
        self.assertNotIn("provider", underlying)
        self.assertNotIn("httpStatus", underlying)
        self.assertNotIn("latencyMs", underlying)

    def test_underlying_a4_diagnostic_optional_fields_still_exclude_secrets(self):
        """Even with all four optional fields present, the exact allowlist
        still excludes keyAliasUsed, secretSafety, and any raw content --
        completeness of the optional set does not loosen the exclusion
        boundary."""
        a4_diag = _failed_a4_diagnostic(observed_call_count=1)
        a4_diag["diagnostic"]["provider"] = "alibaba"
        a4_diag["diagnostic"]["model"] = "qwen-flash"
        a4_diag["diagnostic"]["httpStatus"] = 500
        a4_diag["diagnostic"]["latencyMs"] = 1000
        # Simulate a hypothetical future A4 payload that mistakenly attaches
        # forbidden content directly onto the diagnostic sub-object; the
        # allowlist in _extract_underlying_a4_diagnostic must still drop it.
        a4_diag["diagnostic"]["keyAliasUsed"] = "DASHSCOPE_API_KEY"
        a4_diag["diagnostic"]["rawProviderBody"] = '{"choices": [{"message": {"content": "leaked"}}]}'
        a4_diag["diagnostic"]["headers"] = {"authorization": "Bearer sk-should-never-appear"}

        diag = a5.build_diagnostic(
            started_at="t0", a4_returncode=1,
            admission_failures=["a4_live_receipt_missing_or_unreadable"],
            diagnostic=a4_diag,
        )
        underlying = diag["underlyingA4Diagnostic"]
        self.assertEqual(
            set(underlying.keys()),
            {"stage", "class", "retryable", "userAction", "safeMessage", "provider", "model", "httpStatus", "latencyMs"},
        )
        serialized = json.dumps(diag)
        self.assertNotIn("keyAliasUsed", serialized)
        self.assertNotIn("headers", serialized)
        self.assertNotIn("Bearer", serialized)
        self.assertNotIn("leaked", serialized)
        self.assertNotIn('"rawProviderBody":', serialized)  # the injected forbidden key itself
        self.assertNotIn("choices", serialized)  # the injected forbidden value's content

    def test_secret_safety_never_true_in_any_built_artifact(self):
        """No raw key, prompt, provider body, or output field is ever persisted."""
        result = a5.build_a5_result(
            started_at="t0", finished_at="t1", a4_returncode=0,
            diagnostic=_passing_a4_diagnostic(), live_receipt=_passing_a4_live_receipt(),
            admission_failures=[],
        )
        serialized = json.dumps(result)
        for forbidden in ("rawKey", "rawProviderBody", "rawOutput", "fullPrompt"):
            # These field names may appear as False-valued keys; the actual
            # secret content itself never appears as a literal value.
            self.assertNotIn("sk-", serialized)
            self.assertNotIn("Bearer ", serialized)
        self.assertTrue(all(v is False for v in result["secretSafety"].values()))


class CmdRunSubprocessDoubleTests(unittest.TestCase):
    """Tests cmd_run end-to-end with the A4 subprocess call point replaced by
    an in-process fake. Zero real subprocess is spawned; zero network call is
    possible through this path.
    """

    def _run_with_fake_a4(self, *, returncode: int, diagnostic: dict | None, live_receipt: dict | None,
                           output_arg: str = "", diagnostic_arg: str = ""):
        def fake_run_a4_live(diagnostic_path: Path, live_receipt_path: Path, manifest_path: Path):
            if diagnostic is not None:
                diagnostic_path.write_text(json.dumps(diagnostic), encoding="utf-8")
            if live_receipt is not None:
                live_receipt_path.write_text(json.dumps(live_receipt), encoding="utf-8")
            manifest_path.write_text(json.dumps({"schema": "fake"}), encoding="utf-8")
            return returncode, "fake a4 output"

        args = a5.parse_args([
            "--run", "--json",
            *(["--output", output_arg] if output_arg else []),
            *(["--diagnostic-output", diagnostic_arg] if diagnostic_arg else []),
        ])
        with mock.patch.object(a5, "run_a4_live", fake_run_a4_live):
            exit_code = a5.cmd_run(args)
        return exit_code

    def test_admission_pass_returns_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "result.json"
            diag_path = Path(tmp) / "diag.json"
            exit_code = self._run_with_fake_a4(
                returncode=0,
                diagnostic=_passing_a4_diagnostic(),
                live_receipt=_passing_a4_live_receipt(),
                output_arg=str(output_path),
                diagnostic_arg=str(diag_path),
            )
            self.assertEqual(exit_code, 0)
            result = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(result["sot3"]["overall"], "PASS")
            diagnostic_written = json.loads(diag_path.read_text(encoding="utf-8"))
            self.assertIsNone(diagnostic_written["diagnostic"])

    def test_admission_failure_returns_nonzero_and_writes_diagnostic(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "result.json"
            diag_path = Path(tmp) / "diag.json"
            bad_receipt = _passing_a4_live_receipt()
            bad_receipt["negativeCaseCount"] = 5
            exit_code = self._run_with_fake_a4(
                returncode=0,
                diagnostic=_passing_a4_diagnostic(),
                live_receipt=bad_receipt,
                output_arg=str(output_path),
                diagnostic_arg=str(diag_path),
            )
            self.assertEqual(exit_code, 1)
            result = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(result["sot3"]["overall"], "FAIL")
            diagnostic_written = json.loads(diag_path.read_text(encoding="utf-8"))
            self.assertIsNotNone(diagnostic_written["diagnostic"])

    def test_a4_process_failure_returns_nonzero_and_never_claims_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "result.json"
            exit_code = self._run_with_fake_a4(
                returncode=1,
                diagnostic=None,
                live_receipt=None,
                output_arg=str(output_path),
            )
            self.assertEqual(exit_code, 1)
            result = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(result["sot3"]["overall"], "FAIL")

    def test_diagnostic_written_on_both_pass_and_failure_paths(self):
        """Persist an A5 diagnostic at the caller-provided path for both PASS
        and failure, per Design Control Gate item 3."""
        with tempfile.TemporaryDirectory() as tmp:
            pass_diag_path = Path(tmp) / "pass-diag.json"
            self._run_with_fake_a4(
                returncode=0,
                diagnostic=_passing_a4_diagnostic(),
                live_receipt=_passing_a4_live_receipt(),
                diagnostic_arg=str(pass_diag_path),
            )
            self.assertTrue(pass_diag_path.exists())

            fail_diag_path = Path(tmp) / "fail-diag.json"
            self._run_with_fake_a4(
                returncode=1,
                diagnostic=None,
                live_receipt=None,
                diagnostic_arg=str(fail_diag_path),
            )
            self.assertTrue(fail_diag_path.exists())

    def test_a4_diagnostic_survives_temp_cleanup_through_a5_output(self):
        """End-to-end through the real `cmd_run`: A4's diagnostic is written
        inside `cmd_run`'s own `tempfile.TemporaryDirectory`, which is
        genuinely deleted (not mocked) when the `with` block exits. This
        proves the diagnostic content survives into the persisted A5 output
        file even though the temp file it was read from no longer exists by
        the time the assertion runs."""
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "result.json"
            diag_path = Path(tmp) / "diag.json"
            exit_code = self._run_with_fake_a4(
                returncode=1,
                diagnostic=_failed_a4_diagnostic(observed_call_count=1),
                live_receipt=None,
                output_arg=str(output_path),
                diagnostic_arg=str(diag_path),
            )
            self.assertEqual(exit_code, 1)

            diagnostic_written = json.loads(diag_path.read_text(encoding="utf-8"))
            self.assertIsNotNone(diagnostic_written["underlyingA4Diagnostic"])
            self.assertEqual(diagnostic_written["underlyingA4Diagnostic"]["stage"], "provider")
            self.assertEqual(diagnostic_written["underlyingA4Diagnostic"]["class"], "unknown_error")
            self.assertIn(
                "did not produce an observation file",
                diagnostic_written["underlyingA4Diagnostic"]["safeMessage"],
            )
            self.assertEqual(diagnostic_written["a4RecoveryProviderCallCount"], 1)
            self.assertIn("a4_live_receipt_missing_or_unreadable", diagnostic_written["admissionFailures"])

            result_written = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(result_written["sot3"]["overall"], "FAIL")
            self.assertEqual(result_written["sot3"]["recoveryProviderCallCount"], 1)
            for value in result_written["secretSafety"].values():
                self.assertFalse(value)


class MainCliTests(unittest.TestCase):
    def test_main_requires_run_flag(self):
        exit_code = a5.main([])
        self.assertEqual(exit_code, 2)

    def test_run_a4_live_never_invokes_vitest_or_route_directly(self):
        """Confirms run_a4_live's subprocess command is the A4 runner Python
        script only -- never a vitest binary or the live test path directly.
        This is a structural assertion on the command list, no subprocess is
        actually spawned (subprocess.run is mocked)."""
        captured_cmd = {}

        class FakeCompletedProcess:
            returncode = 0
            stdout = "{}"
            stderr = ""

        def fake_subprocess_run(cmd, **kwargs):
            captured_cmd["cmd"] = cmd
            return FakeCompletedProcess()

        with mock.patch.object(a5.subprocess, "run", fake_subprocess_run):
            a5.run_a4_live(Path("/tmp/d.json"), Path("/tmp/r.json"), Path("/tmp/m.json"))

        cmd = captured_cmd["cmd"]
        self.assertIn(str(a5.A4_RUNNER), cmd)
        joined = " ".join(cmd)
        self.assertNotIn("vitest", joined)
        self.assertNotIn(".live.test.ts", joined)


class ReleaseBundleWiringTests(unittest.TestCase):
    """Tests for scripts/run_cvf_release_gate_bundle.py's SOT3 wiring.

    All A5-adapter-invocation paths are replaced with in-process fakes via
    monkeypatching `bundle.run_cvf_sot3_a5_release_proof_main` (or equivalent
    call point) or `check_sot3` internals -- zero subprocess is spawned, zero
    network call is possible through this test file.
    """

    def test_dry_run_marks_sot3_as_skip(self):
        result = bundle.check_sot3(dry_run=True)
        self.assertEqual(result.status, "SKIP")

    def test_dry_run_bundle_cannot_claim_pass_release_result(self):
        """Confirms dry-run's SOT3 SKIP keeps the JSON gate_result from being
        interpretable as a genuine release PASS; SKIP is not PASS/FAIL and the
        result_payload's own gate_result is computed only from FAIL checks,
        so this test additionally asserts SOT3 is present as SKIP in the
        emitted check list used to build that payload."""
        result = bundle.check_sot3(dry_run=True)
        payload = bundle.result_payload([result], "2026-07-13")
        sot3_entries = [c for c in payload["checks"] if c["name"] == result.name]
        self.assertEqual(len(sot3_entries), 1)
        self.assertEqual(sot3_entries[0]["status"], "SKIP")

    def test_mock_flag_does_not_bypass_sot3_check(self):
        """--mock only affects check_provider_readiness; check_sot3 has no
        mock parameter at all, so a mock-mode run cannot mark SOT3 as PASS
        without actually invoking the adapter. This test verifies the
        function signature accepts no mock-bypass parameter and that calling
        it in the non-dry-run path attempts the real adapter subprocess call
        point (captured via monkeypatch, not actually executed)."""
        called = {"invoked": False}

        def fake_call_a5_adapter(output_path, diagnostic_path):
            called["invoked"] = True
            return {
                "sot3": {
                    "overall": "PASS",
                    "localNegativeGatePassed": True,
                    "negativeCaseCount": 19,
                    "zeroProviderCallCaseCount": 18,
                    "rollbackProviderCallCount": 1,
                    "recoveryProviderCallCount": 1,
                    "approvedContextIncluded": True,
                    "durableOwnerCorrelationComplete": True,
                    "httpStatus": 200,
                    "traceCount": 1,
                    "admissionFailures": [],
                },
            }, 0

        with mock.patch.object(bundle, "call_sot3_a5_adapter", fake_call_a5_adapter):
            result = bundle.check_sot3(dry_run=False)
        self.assertTrue(called["invoked"])
        self.assertEqual(result.status, "PASS")

    def test_missing_sot3_payload_fails_overall_release_result(self):
        checks = [
            bundle.CheckResult("Web build (npm run build)", "PASS", "ok"),
            bundle.CheckResult("SOT3 canonical release proof (A5)", "FAIL", "missing sot3 payload"),
        ]
        payload = bundle.result_payload(checks, "2026-07-13")
        self.assertEqual(payload["gate_result"], "FAIL")

    def test_malformed_sot3_payload_fails_overall_release_result(self):
        called = {"invoked": False}

        def fake_call_a5_adapter(output_path, diagnostic_path):
            called["invoked"] = True
            return {"sot3": {"overall": "PASS"}}, 0  # missing required fields

        with mock.patch.object(bundle, "call_sot3_a5_adapter", fake_call_a5_adapter):
            result = bundle.check_sot3(dry_run=False)
        self.assertEqual(result.status, "FAIL")

    def test_non_pass_sot3_payload_fails_overall_release_result(self):
        def fake_call_a5_adapter(output_path, diagnostic_path):
            return {
                "sot3": {
                    "overall": "FAIL",
                    "localNegativeGatePassed": True,
                    "negativeCaseCount": 19,
                    "zeroProviderCallCaseCount": 18,
                    "rollbackProviderCallCount": 1,
                    "recoveryProviderCallCount": 1,
                    "approvedContextIncluded": True,
                    "durableOwnerCorrelationComplete": True,
                    "httpStatus": 200,
                    "traceCount": 1,
                    "admissionFailures": ["a4_http_status_not_200"],
                },
            }, 1

        with mock.patch.object(bundle, "call_sot3_a5_adapter", fake_call_a5_adapter):
            result = bundle.check_sot3(dry_run=False)
        self.assertEqual(result.status, "FAIL")

    def test_default_results_list_includes_sot3_check(self):
        """The mandatory check must be part of the default results assembly.
        This inspects main()'s check-list construction indirectly via a
        source-level assertion that check_sot3 is referenced in main's
        results list, without invoking main() itself (which would attempt a
        real npm/vitest/provider run)."""
        import inspect
        source = inspect.getsource(bundle.main)
        self.assertIn("check_sot3(", source)


class NoBlindRetryTests(unittest.TestCase):
    """Confirms check_e2e no longer performs an immediate second Playwright
    invocation on failure. Verified via source inspection (no subprocess
    spawned) plus a monkeypatched single-call-count behavioral test.
    """

    def test_check_e2e_source_has_no_second_run_cmd_call(self):
        import inspect
        source = inspect.getsource(bundle.check_e2e)
        # Exactly one call site to run_cmd(cmd, ...) should exist for the
        # Playwright invocation itself (retry_code / retry_stdout must be gone).
        self.assertNotIn("retry_code", source)
        self.assertNotIn("retry_stdout", source)
        self.assertNotIn("retry_summary", source)

    def test_check_e2e_calls_run_cmd_exactly_once_on_failure(self):
        call_count = {"n": 0}

        def fake_run_cmd(cmd, cwd=None, timeout=300):
            call_count["n"] += 1
            return 1, "1 failed\n", ""

        def fake_exists(self_path):
            return True

        with mock.patch.object(bundle, "run_cmd", fake_run_cmd), \
             mock.patch.object(Path, "exists", fake_exists):
            result = bundle.check_e2e(dry_run=False, live=False)
        self.assertEqual(call_count["n"], 1)
        self.assertEqual(result.status, "FAIL")


if __name__ == "__main__":
    unittest.main()
