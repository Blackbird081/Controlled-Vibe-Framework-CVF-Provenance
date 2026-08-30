#!/usr/bin/env python3
"""Secret-safe E2E diagnostic classification for the CVF release runner."""

from __future__ import annotations

import re

SUBPROCESS_TIMEOUT_EXIT_CODE = 124


def build_e2e_diagnostic(
    output: str,
    mode: str,
    latency_ms: int | None = None,
    exit_code: int | None = None,
) -> dict:
    """Classify failure from the subprocess sentinel, never output wording."""
    lowered = output.lower()
    http_match = re.search(r"(?:http(?: status)?|status)\D{0,8}(\d{3})", lowered)
    http_status = int(http_match.group(1)) if http_match else None
    if exit_code == SUBPROCESS_TIMEOUT_EXIT_CODE:
        failure_class, retryable = "timeout", True
        user_action = "classify_timeout_stage_then_retry"
        safe_message = "The E2E run exceeded its bounded timeout."
    elif "cannot resolve" in lowered or "module not found" in lowered:
        failure_class, retryable = "dependency_resolution_failed", True
        user_action = "repair_dependency_resolution_then_retry"
        safe_message = "The E2E route did not compile because a dependency import could not be resolved."
    elif "no dashscope-compatible live key" in lowered:
        failure_class, retryable = "credential_unavailable", False
        user_action = "provide_operator_managed_live_key"
        safe_message = "A DashScope-compatible live key was not available to the release runner."
    else:
        failure_class, retryable = "e2e_failed", False
        user_action = "inspect_secret_safe_test_artifacts_before_retry"
        safe_message = f"The {mode} E2E suite failed; inspect the retained test artifacts before retrying."
    return {
        "stage": "e2e_execution", "class": failure_class, "retryable": retryable,
        "userAction": user_action, "safeMessage": safe_message,
        "provider": "alibaba" if mode == "live governance" else None,
        "model": None, "httpStatus": http_status, "latencyMs": latency_ms,
        "traceOrReceipt": None,
    }
