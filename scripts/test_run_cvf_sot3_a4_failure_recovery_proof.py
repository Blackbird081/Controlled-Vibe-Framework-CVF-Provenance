#!/usr/bin/env python3
"""Hermetic regression tests for scripts/run_cvf_sot3_a4_failure_recovery_proof.py.

Text Encoding Exception: Unicode and malformed-character payloads below are
intentional adversarial fixtures for output-sanitization recovery proof.

Zero network calls. Zero real npx/vitest/provider subprocess execution.
`cmd_live`'s real gate-check and live-test call sites (`local_gate_is_green`,
`bootstrap_repo_env`, `resolve_key_alias`, `run_live_test`) are monkeypatched
with in-process fakes so this file never spawns a real child process and
never reads real repository/environment state.

Covers the diagnostic-persistence-before-console-output ordering repair: on
a nonzero Vitest return or a missing observation file, the secret-safe
diagnostic must be built and atomically persisted before any console output,
and raw captured Vitest stdout/stderr must never be printed on that failure
path -- even when the captured output contains Unicode, ANSI escape
sequences, or other malformed terminal content.

Authorization: docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_2026-07-13.md
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import run_cvf_sot3_a4_failure_recovery_proof as a4  # noqa: E402


def _green_gate_receipt() -> dict:
    return {
        "localNegativeGatePassed": True,
        "negativeCaseCount": 19,
        "zeroProviderCallCaseCount": 18,
        "rollbackProviderCallCount": 1,
    }


def _valid_blocked_observation(*, observed_call_count: int, **diagnostic_overrides: Any) -> dict:
    """A structured BLOCKED observation matching the TS live test's
    `Sot3A3LiveObservation` shape exactly, as persisted by
    `buildBlockedObservation`/`writeObservationAtomic` on the failure path."""
    diagnostic = {
        "stage": "provider",
        "class": "post_call_assertion_or_contract_failure",
        "retryable": False,
        "userAction": "inspect_receipt",
        "safeMessage": "The live proof assertions or governance contract checks failed after the provider call attempt.",
        "provider": "alibaba",
        "model": "qwen-flash",
        **diagnostic_overrides,
    }
    return {
        "overall": "BLOCKED",
        "provider": "alibaba",
        "model": "qwen-flash",
        "keyAliasUsed": "DASHSCOPE_API_KEY",
        "httpStatus": None,
        "success": False,
        "latencyMs": None,
        "observedCallCount": observed_call_count,
        "providerRequestObserved": observed_call_count > 0,
        "approvedContextHash": None,
        "providerSystemPromptHash": None,
        "approvedContextIncluded": False,
        "approvedContextLength": None,
        "providerSystemPromptLength": None,
        "governanceReceiptId": None,
        "envelopeId": None,
        "sot3RecordId": None,
        "sot3IntegrityHash": None,
        "sot3RequestId": None,
        "traceCount": None,
        "packetIds": [],
        "kernelDecisionIds": [],
        "truthReceiptIds": [],
        "truthReferenceIds": [],
        "flowPackageIds": [],
        "outputLength": None,
        "rawKeyPersisted": False,
        "rawProviderBodyPersisted": False,
        "rawOutputPersisted": False,
        "fullPromptPersisted": False,
        "diagnostic": diagnostic,
    }


class BlockedObservationValidatorTests(unittest.TestCase):
    """`_extract_valid_blocked_observation_diagnostic` pure-function tests.
    Zero subprocess, zero filesystem I/O -- every case passes a constructed
    dict/value directly."""

    def test_valid_blocked_observation_extracts_diagnostic_and_call_count(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        result = a4._extract_valid_blocked_observation_diagnostic(observation)
        self.assertIsNotNone(result)
        self.assertEqual(result["observedCallCount"], 1)
        self.assertEqual(result["diagnostic"]["stage"], "provider")
        self.assertEqual(result["diagnostic"]["class"], "post_call_assertion_or_contract_failure")

    def test_valid_blocked_observation_call_count_zero_extracted(self):
        observation = _valid_blocked_observation(observed_call_count=0)
        result = a4._extract_valid_blocked_observation_diagnostic(observation)
        self.assertIsNotNone(result)
        self.assertEqual(result["observedCallCount"], 0)

    def test_canonical_provider_timeout_diagnostic_is_accepted(self):
        observation = _valid_blocked_observation(
            observed_call_count=1,
            **{
                "class": "provider_timeout",
                "retryable": True,
                "userAction": "wait_and_retry",
                "safeMessage": "The provider call exceeded the configured timeout.",
                "latencyMs": 60001,
            },
        )
        result = a4._extract_valid_blocked_observation_diagnostic(observation)
        self.assertIsNotNone(result)
        self.assertEqual(result["diagnostic"]["class"], "provider_timeout")
        self.assertEqual(result["diagnostic"]["latencyMs"], 60001)

    def test_provider_class_with_noncanonical_message_is_rejected(self):
        observation = _valid_blocked_observation(
            observed_call_count=1,
            **{
                "class": "provider_timeout",
                "retryable": True,
                "userAction": "wait_and_retry",
                "safeMessage": "arbitrary marker content",
            },
        )
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_optional_fields_preserved_when_present(self):
        observation = _valid_blocked_observation(observed_call_count=1, httpStatus=503, latencyMs=4200)
        result = a4._extract_valid_blocked_observation_diagnostic(observation)
        self.assertEqual(result["diagnostic"]["httpStatus"], 503)
        self.assertEqual(result["diagnostic"]["latencyMs"], 4200)
        self.assertEqual(result["diagnostic"]["provider"], "alibaba")
        self.assertEqual(result["diagnostic"]["model"], "qwen-flash")

    def test_optional_fields_omitted_when_absent(self):
        """`_valid_blocked_observation`'s default fixture never sets
        httpStatus/latencyMs on the diagnostic (only provider/model), so
        this exercises the omit-when-absent path directly without needing
        to delete anything."""
        observation = _valid_blocked_observation(observed_call_count=0)
        self.assertNotIn("httpStatus", observation["diagnostic"])
        self.assertNotIn("latencyMs", observation["diagnostic"])
        result = a4._extract_valid_blocked_observation_diagnostic(observation)
        self.assertNotIn("httpStatus", result["diagnostic"])
        self.assertNotIn("latencyMs", result["diagnostic"])

    def test_pass_overall_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["overall"] = "PASS"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_missing_diagnostic_key_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        del observation["diagnostic"]
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_diagnostic_not_a_dict_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"] = "not a dict"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_missing_required_field_is_rejected(self):
        for field in ("stage", "class", "retryable", "userAction", "safeMessage"):
            with self.subTest(field=field):
                observation = _valid_blocked_observation(observed_call_count=1)
                del observation["diagnostic"][field]
                self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_wrong_typed_required_field_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["retryable"] = "false"  # string, not bool
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_missing_observed_call_count_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        del observation["observedCallCount"]
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_bool_observed_call_count_is_rejected(self):
        """bool is a subclass of int in Python; must not be accepted as a
        valid call count."""
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["observedCallCount"] = True
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_non_dict_observation_is_rejected(self):
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic("not a dict"))
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(None))
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic([1, 2, 3]))

    def test_injected_secret_fields_never_survive_extraction(self):
        """Even if a malicious/corrupted observation attaches forbidden
        content directly onto the diagnostic sub-object, the strict
        allowlist in the validator drops it -- only the exact allowed keys
        are ever copied into the result."""
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["keyAliasUsed"] = "DASHSCOPE_API_KEY"
        observation["diagnostic"]["rawProviderBody"] = '{"leaked": "content"}'
        observation["diagnostic"]["headers"] = {"authorization": "Bearer sk-should-not-appear"}
        result = a4._extract_valid_blocked_observation_diagnostic(observation)
        self.assertIsNotNone(result)
        self.assertEqual(
            set(result["diagnostic"].keys()),
            {"stage", "class", "retryable", "userAction", "safeMessage", "provider", "model"},
        )
        serialized = json.dumps(result)
        self.assertNotIn("keyAliasUsed", serialized)
        self.assertNotIn("DASHSCOPE_API_KEY", serialized)
        self.assertNotIn("Bearer", serialized)
        self.assertNotIn("leaked", serialized)


class BlockedObservationAdversarialSemanticValidationTests(unittest.TestCase):
    """Strict SEMANTIC (content-equality) validation, per reviewer rework
    item 1: a value with the right Python type but wrong CONTENT must be
    rejected exactly like a structurally malformed one. Every test here
    starts from a fully valid `_valid_blocked_observation` fixture and
    corrupts exactly one field, proving that field alone is enough to fail
    closed. Zero subprocess, zero filesystem I/O."""

    def test_arbitrary_safe_message_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["safeMessage"] = "attacker-controlled arbitrary message"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_arbitrary_stage_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["stage"] = "not_a_real_stage"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_arbitrary_class_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["class"] = "attacker_chosen_class"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_arbitrary_user_action_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["userAction"] = "do_something_else"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_arbitrary_top_level_provider_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["provider"] = "openai"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_arbitrary_diagnostic_provider_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["provider"] = "openai"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_arbitrary_top_level_model_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["model"] = "gpt-4o"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_arbitrary_diagnostic_model_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["model"] = "gpt-4o"
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_retryable_true_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["diagnostic"]["retryable"] = True
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_success_true_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["success"] = True
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_each_secret_safety_flag_true_is_rejected(self):
        for field in ("rawKeyPersisted", "rawProviderBodyPersisted", "rawOutputPersisted", "fullPromptPersisted"):
            with self.subTest(field=field):
                observation = _valid_blocked_observation(observed_call_count=1)
                observation[field] = True
                self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_negative_call_count_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["observedCallCount"] = -1
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_call_count_greater_than_one_is_rejected(self):
        for count in (2, 3, 100):
            with self.subTest(count=count):
                observation = _valid_blocked_observation(observed_call_count=1)
                observation["observedCallCount"] = count
                observation["providerRequestObserved"] = True
                self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_inconsistent_provider_request_observed_true_with_zero_calls_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=0)
        observation["providerRequestObserved"] = True
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_inconsistent_provider_request_observed_false_with_one_call_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1)
        observation["providerRequestObserved"] = False
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_http_status_below_minimum_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1, httpStatus=99)
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_http_status_above_maximum_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1, httpStatus=600)
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_negative_http_status_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1, httpStatus=-1)
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_http_status_wrong_type_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1, httpStatus="500")
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_negative_latency_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1, latencyMs=-100)
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_implausibly_large_latency_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1, latencyMs=99_999_999)
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_latency_wrong_type_is_rejected(self):
        observation = _valid_blocked_observation(observed_call_count=1, latencyMs="4200")
        self.assertIsNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_boundary_valid_http_status_values_accepted(self):
        for status in (100, 200, 404, 500, 599):
            with self.subTest(status=status):
                observation = _valid_blocked_observation(observed_call_count=1, httpStatus=status)
                self.assertIsNotNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_boundary_valid_latency_values_accepted(self):
        for latency in (0, 1, 600_000):
            with self.subTest(latency=latency):
                observation = _valid_blocked_observation(observed_call_count=1, latencyMs=latency)
                self.assertIsNotNone(a4._extract_valid_blocked_observation_diagnostic(observation))

    def test_fully_valid_observation_still_accepted(self):
        """Sanity check: the strengthened semantic validator does not
        over-reject a genuinely conformant observation."""
        observation = _valid_blocked_observation(observed_call_count=1)
        self.assertIsNotNone(a4._extract_valid_blocked_observation_diagnostic(observation))
        observation_zero = _valid_blocked_observation(observed_call_count=0)
        self.assertIsNotNone(a4._extract_valid_blocked_observation_diagnostic(observation_zero))


class CmdLiveBlockedObservationPropagationTests(unittest.TestCase):
    """End-to-end through the real `cmd_live` (gate check / env bootstrap /
    key resolution / live-test subprocess call all monkeypatched): proves
    that a nonzero Vitest exit accompanied by a valid, structured BLOCKED
    observation propagates that observation's diagnostic class instead of
    being silently replaced by the generic `unknown_error`, while a missing
    or malformed observation still falls back safely.
    """

    def _run_cmd_live(
        self,
        *,
        returncode: int,
        observed_call_count: int | None,
        observation_payload: Any = None,
        observation_raw_text: str | None = None,
        diagnostic_arg: str,
    ) -> int:
        def fake_run_live_test(observation_output_path, permit_path, call_ledger_path):
            if observation_raw_text is not None:
                observation_output_path.write_text(observation_raw_text, encoding="utf-8")
            elif observation_payload is not None:
                observation_output_path.write_text(json.dumps(observation_payload), encoding="utf-8")
            return returncode, "captured output never printed on this path", observed_call_count

        args = a4.parse_args(["--live", "--diagnostic", diagnostic_arg])
        with mock.patch.object(a4, "local_gate_is_green", return_value=(True, _green_gate_receipt())), \
             mock.patch.object(a4, "bootstrap_repo_env", return_value=[]), \
             mock.patch.object(a4, "resolve_key_alias", return_value="DASHSCOPE_API_KEY"), \
             mock.patch.object(a4, "run_live_test", fake_run_live_test):
            return a4.cmd_live(args)

    def test_nonzero_with_valid_blocked_observation_propagates_its_class(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                observed_call_count=1,  # the run_live_test/ledger count -- agrees with the observation's own count
                observation_payload=_valid_blocked_observation(observed_call_count=1),
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "post_call_assertion_or_contract_failure")
            self.assertNotEqual(diagnostic["diagnostic"]["class"], "unknown_error")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_malformed_observation_json_falls_back_to_generic_diagnostic(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                observed_call_count=1,
                observation_raw_text="{not valid json!!!",
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "unknown_error")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_missing_observation_falls_back_to_generic_diagnostic(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                observed_call_count=0,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "unknown_error")

    def test_unsafe_observation_shape_falls_back_to_generic_diagnostic(self):
        """A BLOCKED-labeled observation missing required diagnostic fields
        (e.g. corrupted mid-write, or a future schema mismatch) must not be
        partially trusted."""
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            unsafe_observation = _valid_blocked_observation(observed_call_count=1)
            del unsafe_observation["diagnostic"]["safeMessage"]
            exit_code = self._run_cmd_live(
                returncode=1,
                observed_call_count=1,
                observation_payload=unsafe_observation,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "unknown_error")

    def test_injected_secrets_in_observation_never_survive_into_persisted_diagnostic(self):
        """A malicious/corrupted observation attaches forbidden content
        (headers with a Bearer token, a raw provider body, and a
        second/duplicate keyAliasUsed) directly onto its diagnostic
        sub-object; none of that content may survive into the persisted A4
        diagnostic file. This is distinct from the receipt's own legitimate
        top-level `keyAliasUsed` field (the resolved env-var alias NAME,
        e.g. "DASHSCOPE_API_KEY", never a secret value), which every A4
        diagnostic receipt has always included independent of this repair
        -- so this test targets content that has no legitimate reason to
        appear anywhere in the output at all.
        """
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            malicious_observation = _valid_blocked_observation(observed_call_count=1)
            malicious_observation["diagnostic"]["headers"] = {"authorization": "Bearer sk-should-not-appear"}
            malicious_observation["diagnostic"]["rawProviderBody"] = '{"leaked": "provider response content"}'
            self._run_cmd_live(
                returncode=1,
                observed_call_count=1,
                observation_payload=malicious_observation,
                diagnostic_arg=diag_path,
            )
            raw_diag_text = Path(diag_path).read_text(encoding="utf-8")
            self.assertNotIn("headers", raw_diag_text)
            self.assertNotIn("Bearer", raw_diag_text)
            self.assertNotIn("sk-should-not-appear", raw_diag_text)
            self.assertNotIn('"rawProviderBody":', raw_diag_text)  # the injected forbidden key itself
            self.assertNotIn("leaked", raw_diag_text)

            diagnostic = json.loads(raw_diag_text)
            # The propagated diagnostic sub-object is restricted to the
            # exact allowlisted keys -- the injected fields never reach it,
            # regardless of what the top-level receipt separately includes.
            self.assertEqual(
                set(diagnostic["diagnostic"].keys()),
                {"stage", "class", "retryable", "userAction", "safeMessage", "provider", "model"},
            )

    def test_observed_call_count_exactly_one_preserved_through_propagation(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            self._run_cmd_live(
                returncode=1,
                observed_call_count=1,
                observation_payload=_valid_blocked_observation(observed_call_count=1),
                diagnostic_arg=diag_path,
            )
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_raw_captured_output_never_printed_when_valid_blocked_observation_exists(self):
        printed: list[str] = []
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")

            def fake_run_live_test(observation_output_path, permit_path, call_ledger_path):
                observation_output_path.write_text(
                    json.dumps(_valid_blocked_observation(observed_call_count=1)), encoding="utf-8"
                )
                return 1, "UNMISTAKABLE_RAW_OUTPUT_MARKER_99999", 1

            args = a4.parse_args(["--live", "--diagnostic", diag_path])
            with mock.patch.object(a4, "local_gate_is_green", return_value=(True, _green_gate_receipt())), \
                 mock.patch.object(a4, "bootstrap_repo_env", return_value=[]), \
                 mock.patch.object(a4, "resolve_key_alias", return_value="DASHSCOPE_API_KEY"), \
                 mock.patch.object(a4, "run_live_test", fake_run_live_test), \
                 mock.patch("builtins.print", side_effect=lambda *a, **k: printed.append(" ".join(str(x) for x in a))):
                a4.cmd_live(args)

            for line in printed:
                self.assertNotIn("UNMISTAKABLE_RAW_OUTPUT_MARKER_99999", line)


class CallCountEvidenceReconciliationPureFunctionTests(unittest.TestCase):
    """`_reconcile_call_count_evidence` pure-function tests. Zero
    subprocess, zero filesystem I/O -- every case passes constructed
    ledger/observation counts directly."""

    def test_both_none_returns_none(self):
        self.assertIsNone(a4._reconcile_call_count_evidence(None, None))

    def test_ledger_none_observation_present_returns_observation(self):
        self.assertEqual(a4._reconcile_call_count_evidence(None, 1), 1)
        self.assertEqual(a4._reconcile_call_count_evidence(None, 0), 0)

    def test_observation_none_ledger_present_returns_ledger(self):
        self.assertEqual(a4._reconcile_call_count_evidence(1, None), 1)
        self.assertEqual(a4._reconcile_call_count_evidence(0, None), 0)

    def test_equal_counts_return_the_agreed_value(self):
        self.assertEqual(a4._reconcile_call_count_evidence(0, 0), 0)
        self.assertEqual(a4._reconcile_call_count_evidence(1, 1), 1)

    def test_ledger_zero_observation_one_raises_mismatch(self):
        with self.assertRaises(a4._CallCountEvidenceMismatch):
            a4._reconcile_call_count_evidence(0, 1)

    def test_ledger_one_observation_zero_raises_mismatch(self):
        with self.assertRaises(a4._CallCountEvidenceMismatch):
            a4._reconcile_call_count_evidence(1, 0)

    def test_never_silently_prefers_the_larger_count_on_mismatch(self):
        """A mismatch must raise, not resolve to max(ledger, observation)."""
        try:
            result = a4._reconcile_call_count_evidence(0, 1)
        except a4._CallCountEvidenceMismatch:
            pass
        else:
            self.fail(f"expected _CallCountEvidenceMismatch to be raised, got a value: {result!r}")

    def test_conservative_upper_bound_never_under_reports_available_evidence(self):
        self.assertEqual(a4._conservative_call_count_upper_bound(0, 1), 1)
        self.assertEqual(a4._conservative_call_count_upper_bound(1, 0), 1)
        self.assertEqual(a4._conservative_call_count_upper_bound(None, 1), 1)
        self.assertEqual(a4._conservative_call_count_upper_bound(0, None), 0)
        self.assertIsNone(a4._conservative_call_count_upper_bound(None, None))


class CmdLiveCallCountEvidenceReconciliationTests(unittest.TestCase):
    """End-to-end through the real `cmd_live`: proves the independently
    written call ledger and the persisted observation's own
    `observedCallCount` are reconciled rather than one silently overriding
    the other, per reviewer rework item 2. Zero subprocess spawned; every
    case monkeypatches `run_live_test` with an in-process fake.
    """

    def _run_cmd_live(
        self,
        *,
        returncode: int,
        ledger_call_count: int | None,
        observation_payload: Any = None,
        diagnostic_arg: str,
    ) -> int:
        def fake_run_live_test(observation_output_path, permit_path, call_ledger_path):
            if observation_payload is not None:
                observation_output_path.write_text(json.dumps(observation_payload), encoding="utf-8")
            return returncode, "captured output never printed on this path", ledger_call_count

        args = a4.parse_args(["--live", "--diagnostic", diagnostic_arg])
        with mock.patch.object(a4, "local_gate_is_green", return_value=(True, _green_gate_receipt())), \
             mock.patch.object(a4, "bootstrap_repo_env", return_value=[]), \
             mock.patch.object(a4, "resolve_key_alias", return_value="DASHSCOPE_API_KEY"), \
             mock.patch.object(a4, "run_live_test", fake_run_live_test):
            return a4.cmd_live(args)

    def test_ledger_zero_observation_one_fails_closed_to_mismatch_diagnostic(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                ledger_call_count=0,
                observation_payload=_valid_blocked_observation(observed_call_count=1),
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "call_count_evidence_mismatch")
            self.assertNotEqual(diagnostic["diagnostic"]["class"], "post_call_assertion_or_contract_failure")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_ledger_one_observation_zero_fails_closed_to_mismatch_diagnostic(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                ledger_call_count=1,
                observation_payload=_valid_blocked_observation(observed_call_count=0),
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "call_count_evidence_mismatch")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_mismatch_fails_closed_without_under_reporting_the_larger_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            self._run_cmd_live(
                returncode=1,
                ledger_call_count=0,
                observation_payload=_valid_blocked_observation(observed_call_count=1),
                diagnostic_arg=diag_path,
            )
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            # The verdict remains a mismatch, while cost/accounting evidence
            # conservatively preserves the largest call count seen.
            self.assertEqual(diagnostic["diagnostic"]["class"], "call_count_evidence_mismatch")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_equal_counts_agree_and_propagate_normally(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                ledger_call_count=1,
                observation_payload=_valid_blocked_observation(observed_call_count=1),
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "post_call_assertion_or_contract_failure")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_ledger_unavailable_observation_present_uses_observation_count(self):
        """The ledger genuinely missing (npx unavailable, or the call-ledger
        file was never written) is not a mismatch -- the observation's own
        count is used when it is the only source."""
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                ledger_call_count=None,
                observation_payload=_valid_blocked_observation(observed_call_count=1),
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "post_call_assertion_or_contract_failure")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_ledger_present_observation_unavailable_uses_ledger_count(self):
        """No valid observation exists at all (missing/malformed/unsafe);
        the ledger is the only source and is used directly -- still not a
        mismatch, since there is nothing to disagree with."""
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                ledger_call_count=1,
                observation_payload=None,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["class"], "unknown_error")
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_both_sources_unavailable_reports_unknown_call_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code = self._run_cmd_live(
                returncode=1,
                ledger_call_count=None,
                observation_payload=None,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertIsNone(diagnostic["recoveryProviderCallCount"])

    def test_mismatch_diagnostic_is_fixed_and_secret_safe(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            self._run_cmd_live(
                returncode=1,
                ledger_call_count=0,
                observation_payload=_valid_blocked_observation(observed_call_count=1),
                diagnostic_arg=diag_path,
            )
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["diagnostic"]["stage"], "provider")
            self.assertEqual(diagnostic["diagnostic"]["retryable"], False)
            self.assertEqual(diagnostic["diagnostic"]["userAction"], "inspect_receipt")
            for value in diagnostic["secretSafety"].values():
                self.assertFalse(value)

    def test_mismatch_path_never_issues_another_provider_call(self):
        """Reconciliation is pure comparison of two already-collected
        counts; this test proves cmd_live's mismatch path never calls
        run_live_test (or anything else) a second time."""
        call_count = {"n": 0}

        def counting_fake_run_live_test(observation_output_path, permit_path, call_ledger_path):
            call_count["n"] += 1
            observation_output_path.write_text(
                json.dumps(_valid_blocked_observation(observed_call_count=1)), encoding="utf-8"
            )
            return 1, "output", 0  # ledger=0, observation=1 -> mismatch

        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            args = a4.parse_args(["--live", "--diagnostic", diag_path])
            with mock.patch.object(a4, "local_gate_is_green", return_value=(True, _green_gate_receipt())), \
                 mock.patch.object(a4, "bootstrap_repo_env", return_value=[]), \
                 mock.patch.object(a4, "resolve_key_alias", return_value="DASHSCOPE_API_KEY"), \
                 mock.patch.object(a4, "run_live_test", counting_fake_run_live_test):
                a4.cmd_live(args)

        self.assertEqual(call_count["n"], 1)


class WriteJsonAtomicTests(unittest.TestCase):
    """`write_json_atomic` never leaves a partial/corrupt file, even for
    payloads embedding unusual byte sequences. No subprocess involved."""

    def test_writes_valid_json_readable_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.json"
            payload = {"a": 1, "b": [1, 2, 3]}
            a4.write_json_atomic(path, payload)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), payload)

    def test_no_leftover_temp_file_after_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.json"
            a4.write_json_atomic(path, {"ok": True})
            remaining = list(Path(tmp).iterdir())
            self.assertEqual(remaining, [path])

    def test_survives_unicode_and_ansi_content_in_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.json"
            payload = {
                "safeMessage": "caught ☃ unicode, \x1b[31mANSI\x1b[0m, and 😀 emoji-adjacent text",
            }
            a4.write_json_atomic(path, payload)
            reloaded = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(reloaded, payload)

    def test_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "dir" / "out.json"
            a4.write_json_atomic(path, {"ok": True})
            self.assertTrue(path.exists())

    def test_replaces_existing_file_atomically(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.json"
            a4.write_json_atomic(path, {"version": 1})
            a4.write_json_atomic(path, {"version": 2})
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["version"], 2)

    def test_cleans_up_temp_file_on_write_failure(self):
        """If json.dumps or the write itself raises, no `.tmp` file is left
        behind in the target directory."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.json"
            unserializable = {"bad": object()}
            with self.assertRaises(TypeError):
                a4.write_json_atomic(path, unserializable)
            leftover_tmp_files = list(Path(tmp).glob(f".{path.name}.*.tmp"))
            self.assertEqual(leftover_tmp_files, [])
            self.assertFalse(path.exists())


class CmdLiveDiagnosticOrderingTests(unittest.TestCase):
    """End-to-end through the real `cmd_live`, with only the gate check,
    env bootstrap, key resolution, and live-test subprocess call replaced by
    in-process fakes. Proves the required ordering: read ledger -> build and
    persist diagnostic -> only then print a fixed summary; never print raw
    captured output on this failure path.
    """

    def _run_cmd_live_with_fake_live_test(
        self,
        *,
        returncode: int,
        captured_output: str,
        observed_call_count: int,
        write_observation: bool = False,
        observation_payload: Any = None,
        observation_raw_text: str | None = None,
        diagnostic_arg: str = "",
    ) -> tuple[int, list[str]]:
        printed: list[str] = []

        def fake_run_live_test(observation_output_path, permit_path, call_ledger_path):
            if observation_raw_text is not None:
                observation_output_path.write_text(observation_raw_text, encoding="utf-8")
            elif observation_payload is not None:
                observation_output_path.write_text(
                    json.dumps(observation_payload), encoding="utf-8"
                )
            elif write_observation:
                observation_output_path.write_text(
                    json.dumps({"overall": "PASS"}), encoding="utf-8"
                )
            return returncode, captured_output, observed_call_count

        args = a4.parse_args([
            "--live",
            *(["--diagnostic", diagnostic_arg] if diagnostic_arg else []),
        ])

        with mock.patch.object(a4, "local_gate_is_green", return_value=(True, _green_gate_receipt())), \
             mock.patch.object(a4, "bootstrap_repo_env", return_value=[]), \
             mock.patch.object(a4, "resolve_key_alias", return_value="DASHSCOPE_API_KEY"), \
             mock.patch.object(a4, "run_live_test", fake_run_live_test), \
             mock.patch("builtins.print", side_effect=lambda *a, **k: printed.append(" ".join(str(x) for x in a))):
            exit_code = a4.cmd_live(args)

        return exit_code, printed

    def test_nonzero_returncode_persists_diagnostic_with_call_count_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=1,
                captured_output="plain ascii failure output",
                observed_call_count=0,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 0)
            self.assertEqual(diagnostic["diagnostic"]["stage"], "provider")
            self.assertTrue(diagnostic["localNegativeGatePassed"])

    def test_nonzero_returncode_persists_diagnostic_with_call_count_one(self):
        """A real provider call happened (count=1) before the process still
        exited nonzero (e.g. it crashed after the call but before writing
        the observation file); the call count must not be lost or zeroed."""
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=1,
                captured_output="crashed after the call",
                observed_call_count=1,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_missing_observation_file_persists_diagnostic_with_call_count_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=0,  # process exited zero but never wrote the observation file
                captured_output="no observation written",
                observed_call_count=0,
                write_observation=False,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 0)

    def test_missing_observation_file_persists_diagnostic_with_call_count_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=0,
                captured_output="call happened, observation write failed",
                observed_call_count=1,
                write_observation=False,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_unicode_captured_output_never_blocks_diagnostic_persistence(self):
        unicode_output = "☃ snowman 中文 \U0001F600 emoji output with mixed scripts"
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=1,
                captured_output=unicode_output,
                observed_call_count=0,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            self.assertTrue(Path(diag_path).exists())
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 0)

    def test_ansi_escape_captured_output_never_blocks_diagnostic_persistence(self):
        ansi_output = "\x1b[31mERROR\x1b[0m: \x1b[1msomething failed\x1b[0m\x1b[2J\x1b[H"
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=1,
                captured_output=ansi_output,
                observed_call_count=1,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 1)

    def test_malformed_and_arbitrary_binary_like_captured_output_never_blocks_diagnostic(self):
        """Arbitrary bytes decoded with errors='replace' by run_live_test can
        surface as U+FFFD replacement characters and other unusual code
        points; the diagnostic must still be built and persisted."""
        malformed_output = "��\x00\x07\x1b]0;terminal title\x07 garbled � text"
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=1,
                captured_output=malformed_output,
                observed_call_count=0,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            diagnostic = json.loads(Path(diag_path).read_text(encoding="utf-8"))
            self.assertEqual(diagnostic["recoveryProviderCallCount"], 0)

    def test_raw_captured_output_never_printed_on_failure_path(self):
        """The fixed console summary is printed, but the raw captured
        content itself must never appear in any print() call on this
        failure path."""
        distinctive_marker = "UNMISTAKABLE_RAW_VITEST_OUTPUT_MARKER_12345"
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            exit_code, printed = self._run_cmd_live_with_fake_live_test(
                returncode=1,
                captured_output=f"...stack trace...\n{distinctive_marker}\n...more trace...",
                observed_call_count=0,
                diagnostic_arg=diag_path,
            )
            self.assertEqual(exit_code, 1)
            for line in printed:
                self.assertNotIn(distinctive_marker, line)

    def test_raw_captured_output_never_written_into_diagnostic_file(self):
        distinctive_marker = "UNMISTAKABLE_RAW_VITEST_OUTPUT_MARKER_67890"
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = str(Path(tmp) / "diag.json")
            self._run_cmd_live_with_fake_live_test(
                returncode=1,
                captured_output=f"trace...\n{distinctive_marker}\n...trace",
                observed_call_count=0,
                diagnostic_arg=diag_path,
            )
            raw_diag_text = Path(diag_path).read_text(encoding="utf-8")
            self.assertNotIn(distinctive_marker, raw_diag_text)

    def test_diagnostic_persisted_before_any_print_call(self):
        """Structural ordering proof: monkeypatch print() to record whether
        the diagnostic file already exists at the moment of each print call.
        On the failure path, the file must exist by the time of the very
        first print() invocation that follows run_live_test."""
        with tempfile.TemporaryDirectory() as tmp:
            diag_path = Path(tmp) / "diag.json"
            file_existed_at_first_print: list[bool] = []

            def fake_run_live_test(observation_output_path, permit_path, call_ledger_path):
                return 1, "some failure output", 0

            def recording_print(*a, **k):
                file_existed_at_first_print.append(diag_path.exists())

            args = a4.parse_args(["--live", "--diagnostic", str(diag_path)])
            with mock.patch.object(a4, "local_gate_is_green", return_value=(True, _green_gate_receipt())), \
                 mock.patch.object(a4, "bootstrap_repo_env", return_value=[]), \
                 mock.patch.object(a4, "resolve_key_alias", return_value="DASHSCOPE_API_KEY"), \
                 mock.patch.object(a4, "run_live_test", fake_run_live_test), \
                 mock.patch("builtins.print", side_effect=recording_print):
                exit_code = a4.cmd_live(args)

            self.assertEqual(exit_code, 1)
            self.assertTrue(len(file_existed_at_first_print) >= 1)
            self.assertTrue(
                file_existed_at_first_print[0],
                "the diagnostic file must already exist by the first print() call on the failure path",
            )


if __name__ == "__main__":
    unittest.main()
