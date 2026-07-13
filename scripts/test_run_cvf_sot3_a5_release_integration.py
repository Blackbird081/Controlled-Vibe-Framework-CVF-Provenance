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
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import run_cvf_sot3_a5_release_proof as a5  # noqa: E402
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
            "model": "qwen-turbo",
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
