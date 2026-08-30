#!/usr/bin/env python3
"""Secret-safe observation validation and call-count reconciliation for SOT3 A4."""

from __future__ import annotations

from typing import Any
from datetime import datetime, timezone

_EXPECTED_BLOCKED_DIAGNOSTIC = {
    "stage": "provider", "class": "post_call_assertion_or_contract_failure", "retryable": False,
    "userAction": "inspect_receipt", "safeMessage": "The live proof assertions or governance contract checks failed after the provider call attempt.",
}
_EXPECTED_PROVIDER_DIAGNOSTICS: dict[str, tuple[bool, str, str]] = {
    "invalid_api_key": (False, "check_api_key", "The provider rejected the configured API key or token."),
    "insufficient_balance": (False, "top_up_or_check_quota", "The provider account appears to lack balance or quota."),
    "quota_exceeded": (False, "top_up_or_check_quota", "The execution was blocked by quota limits."),
    "rate_limited": (True, "wait_and_retry", "The request was rate limited."),
    "provider_timeout": (True, "wait_and_retry", "The provider call exceeded the configured timeout."),
    "provider_http_error": (True, "wait_and_retry", "The provider returned an HTTP error."),
    "model_unavailable": (False, "change_model", "The selected model is unavailable for the current provider account or endpoint."),
    "provider_empty_output": (True, "wait_and_retry", "The provider returned no usable output."),
    "provider_parse_error": (True, "wait_and_retry", "The provider response could not be parsed into the expected shape."),
    "network_error": (True, "wait_and_retry", "A network error interrupted execution."),
    "unknown_error": (False, "do_not_retry_without_new_evidence", "The execution failed for an unclassified reason."),
}
_EXPECTED_PROVIDER = "alibaba"
_EXPECTED_MODEL = "qwen-flash"
_ALLOWED_OBSERVED_CALL_COUNTS = (0, 1)
_MIN_HTTP_STATUS, _MAX_HTTP_STATUS = 100, 599
_MIN_LATENCY_MS, _MAX_LATENCY_MS = 0, 600_000


def _is_valid_bool(value: Any) -> bool:
    return isinstance(value, bool)


def _is_valid_optional_http_status(value: Any) -> bool:
    return value is None or (isinstance(value, int) and not isinstance(value, bool) and _MIN_HTTP_STATUS <= value <= _MAX_HTTP_STATUS)


def _is_valid_optional_latency_ms(value: Any) -> bool:
    return value is None or (isinstance(value, (int, float)) and not isinstance(value, bool) and _MIN_LATENCY_MS <= value <= _MAX_LATENCY_MS)


def _extract_valid_blocked_observation_diagnostic(observation: Any) -> dict[str, Any] | None:
    if not isinstance(observation, dict) or observation.get("overall") != "BLOCKED" or observation.get("success") is not False:
        return None
    observed_call_count = observation.get("observedCallCount")
    if not isinstance(observed_call_count, int) or isinstance(observed_call_count, bool) or observed_call_count not in _ALLOWED_OBSERVED_CALL_COUNTS:
        return None
    if observation.get("providerRequestObserved") is not (observed_call_count > 0):
        return None
    for field in ("rawKeyPersisted", "rawProviderBodyPersisted", "rawOutputPersisted", "fullPromptPersisted"):
        if observation.get(field) is not False:
            return None
    if observation.get("provider") != _EXPECTED_PROVIDER or observation.get("model") != _EXPECTED_MODEL:
        return None
    diagnostic = observation.get("diagnostic")
    if not isinstance(diagnostic, dict):
        return None
    diagnostic_class = diagnostic.get("class")
    if diagnostic_class == _EXPECTED_BLOCKED_DIAGNOSTIC["class"]:
        expected = _EXPECTED_BLOCKED_DIAGNOSTIC
    elif isinstance(diagnostic_class, str) and diagnostic_class in _EXPECTED_PROVIDER_DIAGNOSTICS:
        retryable, user_action, safe_message = _EXPECTED_PROVIDER_DIAGNOSTICS[diagnostic_class]
        expected = {"stage": "provider", "class": diagnostic_class, "retryable": retryable, "userAction": user_action, "safeMessage": safe_message}
    else:
        return None
    if any(diagnostic.get(field) != value for field, value in expected.items()) or not _is_valid_bool(diagnostic.get("retryable")):
        return None
    if "provider" in diagnostic and diagnostic["provider"] != _EXPECTED_PROVIDER:
        return None
    if "model" in diagnostic and diagnostic["model"] != _EXPECTED_MODEL:
        return None
    if "httpStatus" in diagnostic and not _is_valid_optional_http_status(diagnostic["httpStatus"]):
        return None
    if "latencyMs" in diagnostic and not _is_valid_optional_latency_ms(diagnostic["latencyMs"]):
        return None
    extracted: dict[str, Any] = {field: diagnostic[field] for field in expected}
    for field in ("provider", "model"):
        if field in diagnostic:
            extracted[field] = diagnostic[field]
    for field in ("httpStatus", "latencyMs"):
        if diagnostic.get(field) is not None:
            extracted[field] = diagnostic[field]
    return {"diagnostic": extracted, "observedCallCount": observed_call_count}


_CALL_COUNT_EVIDENCE_MISMATCH_DIAGNOSTIC = {
    "stage": "provider", "class": "call_count_evidence_mismatch", "retryable": False,
    "userAction": "inspect_receipt",
    "safeMessage": "The independently written call ledger and the persisted observation disagree on the observed provider call count.",
}


class _CallCountEvidenceMismatch(Exception):
    pass


def _reconcile_call_count_evidence(ledger_call_count: int | None, observation_call_count: int | None) -> int | None:
    if ledger_call_count is None:
        return observation_call_count
    if observation_call_count is None:
        return ledger_call_count
    if ledger_call_count != observation_call_count:
        raise _CallCountEvidenceMismatch()
    return ledger_call_count


def _conservative_call_count_upper_bound(*counts: int | None) -> int | None:
    available = [count for count in counts if count is not None]
    return max(available) if available else None


def build_diagnostic_receipt(
    *, execution_base_head: str, started_at: str,
    diagnostic: dict[str, Any] | None, observed_call_count: int | None,
    key_alias_used: str | None, local_negative_gate_passed: bool,
) -> dict[str, Any]:
    return {
        "schemaVersion": "cvf.sot3ActA4LiveDiagnostic.v1",
        "batchId": "SOT3-ACT-A4", "executionBaseHead": execution_base_head,
        "startedAtUtc": started_at, "finishedAtUtc": datetime.now(timezone.utc).isoformat(),
        "localNegativeGatePassed": local_negative_gate_passed,
        "recoveryProviderCallCount": observed_call_count,
        "keyAliasUsed": key_alias_used, "diagnostic": diagnostic,
        "secretSafety": {
            "rawKeyPersisted": False, "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False, "fullPromptPersisted": False,
        },
    }
