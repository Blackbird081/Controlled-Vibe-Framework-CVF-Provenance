#!/usr/bin/env python3
"""CVF SOT3-ACT-A5 canonical release proof adapter.

Bounded adapter invoked by `scripts/run_cvf_release_gate_bundle.py` as a
mandatory release check. It calls ONLY the already-accepted
`scripts/run_cvf_sot3_a4_failure_recovery_proof.py` runner (via subprocess,
with isolated temporary A4 output paths), captures its child output, and
strictly validates the A4 result before declaring PASS. It never invokes
Vitest or the provider route directly itself.

Authorization: docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_2026-07-13.md
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
A4_RUNNER = REPO_ROOT / "scripts" / "run_cvf_sot3_a4_failure_recovery_proof.py"

# The exact A4 denominators/correlations this adapter must validate before
# declaring PASS, per the A5 work order Design Control Gate item 2 and the
# accepted A4 completion review's Acceptance Receipt Assertion Matrix.
REQUIRED_NEGATIVE_CASE_COUNT = 19
REQUIRED_ZERO_PROVIDER_CALL_CASE_COUNT = 18
REQUIRED_ROLLBACK_PROVIDER_CALL_COUNT = 1
REQUIRED_RECOVERY_PROVIDER_CALL_COUNT = 1
REQUIRED_MIN_TRACE_COUNT = 1

OWNER_ARRAY_FIELDS = (
    "packetIds",
    "kernelDecisionIds",
    "truthReceiptIds",
    "truthReferenceIds",
    "flowPackageIds",
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_a4_live(diagnostic_path: Path, live_receipt_path: Path, manifest_path: Path) -> tuple[int, str]:
    """Invokes the accepted A4 runner's `--live` mode with isolated temp output paths.

    Never invokes Vitest or the provider route directly; the A4 runner owns
    that invocation internally.
    """
    cmd = [
        sys.executable,
        str(A4_RUNNER),
        "--live",
        "--json",
        "--diagnostic", str(diagnostic_path),
        "--live-receipt", str(live_receipt_path),
        "--manifest", str(manifest_path),
    ]
    result = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    combined = (result.stdout or "") + (result.stderr or "")
    return result.returncode, combined


def _classify_admission_failures(
    diagnostic: dict[str, Any] | None,
    live_receipt: dict[str, Any] | None,
) -> list[str]:
    """Returns a list of secret-safe admission-failure reason strings.

    Empty list means every strict admission check passed.
    """
    reasons: list[str] = []

    if diagnostic is None:
        reasons.append("a4_diagnostic_missing_or_unreadable")
    elif diagnostic.get("localNegativeGatePassed") is not True:
        reasons.append("a4_local_negative_gate_not_passed")

    if live_receipt is None:
        reasons.append("a4_live_receipt_missing_or_unreadable")
        return reasons

    if live_receipt.get("overall") != "PASS":
        reasons.append("a4_overall_not_pass")
    if live_receipt.get("localNegativeGatePassed") is not True:
        reasons.append("a4_local_negative_gate_flag_not_true")
    if live_receipt.get("negativeCaseCount") != REQUIRED_NEGATIVE_CASE_COUNT:
        reasons.append("a4_negative_case_count_mismatch")
    if live_receipt.get("zeroProviderCallCaseCount") != REQUIRED_ZERO_PROVIDER_CALL_CASE_COUNT:
        reasons.append("a4_zero_provider_call_case_count_mismatch")
    if live_receipt.get("rollbackProviderCallCount") != REQUIRED_ROLLBACK_PROVIDER_CALL_COUNT:
        reasons.append("a4_rollback_provider_call_count_mismatch")
    if live_receipt.get("recoveryProviderCallCount") != REQUIRED_RECOVERY_PROVIDER_CALL_COUNT:
        reasons.append("a4_recovery_provider_call_count_mismatch")

    provider_proof = live_receipt.get("providerProof") or {}
    if provider_proof.get("success") is not True:
        reasons.append("a4_provider_success_not_true")
    if provider_proof.get("httpStatus") != 200:
        reasons.append("a4_http_status_not_200")

    context_observation = live_receipt.get("contextObservation") or {}
    if context_observation.get("approvedContextIncluded") is not True:
        reasons.append("a4_approved_context_not_included")

    correlation = live_receipt.get("correlation") or {}
    trace_count = correlation.get("traceCount")
    if not isinstance(trace_count, int) or trace_count < REQUIRED_MIN_TRACE_COUNT:
        reasons.append("a4_trace_count_below_minimum")

    for field_name in OWNER_ARRAY_FIELDS:
        value = correlation.get(field_name)
        if not isinstance(value, list) or len(value) == 0:
            reasons.append(f"a4_owner_array_empty_or_missing:{field_name}")

    secret_safety = live_receipt.get("secretSafety") or {}
    for key in ("rawKeyPersisted", "rawProviderBodyPersisted", "rawOutputPersisted", "fullPromptPersisted"):
        if secret_safety.get(key) is not False:
            reasons.append(f"a4_secret_safety_flag_not_false:{key}")

    return reasons


def _load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return None


def build_a5_result(
    *,
    started_at: str,
    finished_at: str,
    a4_returncode: int,
    diagnostic: dict[str, Any] | None,
    live_receipt: dict[str, Any] | None,
    admission_failures: list[str],
) -> dict[str, Any]:
    overall_pass = a4_returncode == 0 and not admission_failures and live_receipt is not None

    sot3_projection = {
        "overall": "PASS" if overall_pass else "FAIL",
        "localNegativeGatePassed": bool(live_receipt.get("localNegativeGatePassed")) if live_receipt else False,
        "negativeCaseCount": live_receipt.get("negativeCaseCount") if live_receipt else None,
        "zeroProviderCallCaseCount": live_receipt.get("zeroProviderCallCaseCount") if live_receipt else None,
        "rollbackProviderCallCount": live_receipt.get("rollbackProviderCallCount") if live_receipt else None,
        "recoveryProviderCallCount": (
            live_receipt.get("recoveryProviderCallCount") if live_receipt
            # Falls back to A4's own diagnostic count only when no live
            # receipt exists at all (e.g. the observation file was never
            # written), so a real observed call count is not silently lost
            # even though this FAIL-path projection never affects the PASS
            # admission contract in run_cvf_release_gate_bundle.py, which
            # requires a live_receipt-backed PASS regardless.
            else (diagnostic.get("recoveryProviderCallCount") if diagnostic else None)
        ),
        "approvedContextIncluded": (
            (live_receipt.get("contextObservation") or {}).get("approvedContextIncluded")
            if live_receipt else None
        ),
        "durableOwnerCorrelationComplete": overall_pass and not any(
            reason.startswith("a4_owner_array_empty_or_missing") for reason in admission_failures
        ),
        "httpStatus": (live_receipt.get("providerProof") or {}).get("httpStatus") if live_receipt else None,
        "providerSuccess": (live_receipt.get("providerProof") or {}).get("success") if live_receipt else None,
        "traceCount": (live_receipt.get("correlation") or {}).get("traceCount") if live_receipt else None,
        "claim": live_receipt.get("claim") if live_receipt else None,
        "admissionFailures": admission_failures,
    }

    return {
        "schemaVersion": "cvf.sot3ActA5ReleaseProof.v1",
        "batchId": "SOT3-ACT-A5",
        "startedAtUtc": started_at,
        "finishedAtUtc": finished_at,
        "a4ReturnCode": a4_returncode,
        "sot3": sot3_projection,
        "secretSafety": {
            "rawKeyPersisted": False,
            "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False,
            "fullPromptPersisted": False,
        },
    }


# Exact allowlist of keys `_extract_underlying_a4_diagnostic` may forward
# from A4's raw diagnostic payload into A5's `underlyingA4Diagnostic`. The
# first five are always required (present as `None` when A4 did not set
# them); the remaining four are optional secret-safe context that A4's
# `diagnostic` sub-object may carry when a failure occurred after a provider
# call attempt (e.g. HTTP error, timeout) rather than before one (e.g. an
# auth/governance block) -- forwarded only when present, never fabricated.
# Every other key on A4's raw payload (keyAliasUsed, secretSafety, or any
# future addition) is never forwarded: headers, environment values, prompts,
# request/response bodies, and raw provider output are never present on this
# sub-object in the first place, and this allowlist is the second, structural
# barrier against ever forwarding them even if one were added by mistake.
UNDERLYING_A4_DIAGNOSTIC_REQUIRED_FIELDS = ("stage", "class", "retryable", "userAction", "safeMessage")
UNDERLYING_A4_DIAGNOSTIC_OPTIONAL_FIELDS = ("provider", "model", "httpStatus", "latencyMs")


def _extract_underlying_a4_diagnostic(diagnostic: dict[str, Any] | None) -> dict[str, Any] | None:
    """Returns A4's own secret-safe `diagnostic` sub-object when the caller's
    already-loaded A4 diagnostic payload carries one. `diagnostic` here is
    the in-memory dict `cmd_run` already read from `a4_diagnostic_path`
    before that path's temporary directory was deleted -- this function
    never touches the filesystem, so it works whether or not the temp file
    still exists.

    Always includes the five required fields (`None` when A4 did not set a
    given one). Includes `provider`/`model`/`httpStatus`/`latencyMs` only
    when A4's raw sub-object actually carries that key, so a diagnostic
    built before a provider call was attempted (no optional fields) looks
    different from one built after a provider call failed (optional fields
    present) -- an absent optional key is omitted rather than set to `None`,
    distinguishing "not applicable" from "present but unknown".
    """
    if not diagnostic:
        return None
    underlying = diagnostic.get("diagnostic")
    if not isinstance(underlying, dict):
        return None
    extracted: dict[str, Any] = {
        field: underlying.get(field) for field in UNDERLYING_A4_DIAGNOSTIC_REQUIRED_FIELDS
    }
    for field in UNDERLYING_A4_DIAGNOSTIC_OPTIONAL_FIELDS:
        if field in underlying:
            extracted[field] = underlying[field]
    return extracted


def build_diagnostic(
    *,
    started_at: str,
    a4_returncode: int,
    admission_failures: list[str],
    diagnostic: dict[str, Any] | None,
) -> dict[str, Any]:
    underlying_a4_diagnostic = _extract_underlying_a4_diagnostic(diagnostic)

    if a4_returncode != 0:
        stage = "provider"
        cls = "unknown_error"
        retryable = False
        user_action = "inspect_receipt"
        if underlying_a4_diagnostic is not None:
            # A4's own diagnostic survived its temp-directory cleanup (it was
            # read into memory by cmd_run before that directory was removed)
            # and is projected verbatim below in `underlyingA4Diagnostic`, so
            # A5 must not tell the operator to inspect a file A5 itself
            # already deleted.
            safe_message = (
                "The A4 live runner subprocess exited non-zero. Its own secret-safe "
                "diagnostic is preserved in this A5 diagnostic's underlyingA4Diagnostic field."
            )
        else:
            safe_message = (
                "The A4 live runner subprocess exited non-zero and its own diagnostic "
                "could not be read (missing or unreadable). No further stage/class detail "
                "is available."
            )
    elif admission_failures:
        stage = "output_validation"
        cls = "output_validation_failed"
        retryable = False
        user_action = "inspect_receipt"
        safe_message = (
            "The A4 live receipt did not satisfy every required SOT3-ACT-A5 admission "
            "check. See admissionFailures for the exact secret-safe reason codes."
        )
    else:
        stage = "unknown"
        cls = None
        retryable = False
        user_action = "none"
        safe_message = "No failure; A5 SOT3 admission passed every required check."

    return {
        "schemaVersion": "cvf.sot3ActA5Diagnostic.v1",
        "batchId": "SOT3-ACT-A5",
        "startedAtUtc": started_at,
        "finishedAtUtc": utc_now_iso(),
        "a4ReturnCode": a4_returncode,
        "a4LocalNegativeGatePassed": (
            bool(diagnostic.get("localNegativeGatePassed")) if diagnostic else None
        ),
        "a4RecoveryProviderCallCount": diagnostic.get("recoveryProviderCallCount") if diagnostic else None,
        "admissionFailures": admission_failures,
        "diagnostic": None if (a4_returncode == 0 and not admission_failures) else {
            "stage": stage,
            "class": cls,
            "retryable": retryable,
            "userAction": user_action,
            "safeMessage": safe_message,
        },
        # A4's own preserved secret-safe diagnostic (stage/class/retryable/
        # userAction/safeMessage), read into memory before its temporary
        # directory was deleted. Present whenever A4 wrote one, independent
        # of A4's return code, so the operator is never pointed at evidence
        # this adapter has already removed from disk.
        "underlyingA4Diagnostic": underlying_a4_diagnostic,
        "secretSafety": {
            "rawKeyPersisted": False,
            "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False,
            "fullPromptPersisted": False,
        },
    }


def cmd_run(args: argparse.Namespace) -> int:
    started_at = utc_now_iso()

    with tempfile.TemporaryDirectory(prefix="cvf-sot3-a5-a4-out-") as tmp:
        a4_diagnostic_path = Path(tmp) / "a4-live-diagnostic.json"
        a4_live_receipt_path = Path(tmp) / "a4-live-receipt.json"
        a4_manifest_path = Path(tmp) / "a4-live-manifest.json"

        a4_returncode, a4_output = run_a4_live(a4_diagnostic_path, a4_live_receipt_path, a4_manifest_path)
        if args.verbose:
            print(a4_output[-4000:])

        a4_diagnostic = _load_json(a4_diagnostic_path)
        a4_live_receipt = _load_json(a4_live_receipt_path)

    admission_failures = _classify_admission_failures(a4_diagnostic, a4_live_receipt)

    finished_at = utc_now_iso()
    result = build_a5_result(
        started_at=started_at,
        finished_at=finished_at,
        a4_returncode=a4_returncode,
        diagnostic=a4_diagnostic,
        live_receipt=a4_live_receipt,
        admission_failures=admission_failures,
    )
    diagnostic_out = build_diagnostic(
        started_at=started_at,
        a4_returncode=a4_returncode,
        admission_failures=admission_failures,
        diagnostic=a4_diagnostic,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.diagnostic_output:
        diagnostic_path = Path(args.diagnostic_output)
        diagnostic_path.parent.mkdir(parents=True, exist_ok=True)
        diagnostic_path.write_text(json.dumps(diagnostic_out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"SOT3-ACT-A5 result: {result['sot3']['overall']}")
        if admission_failures:
            for reason in admission_failures:
                print(f"  admission failure: {reason}")

    return 0 if result["sot3"]["overall"] == "PASS" else 1


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true", help="Invoke the accepted A4 runner's --live mode and validate strictly.")
    parser.add_argument("--json", action="store_true", help="Print the A5 result JSON to stdout.")
    parser.add_argument("--verbose", action="store_true", help="Print captured A4 child-process output tail.")
    parser.add_argument("--output", default="", help="A5 result JSON output path.")
    parser.add_argument("--diagnostic-output", default="", help="A5 diagnostic JSON output path (written for both PASS and failure).")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if not args.run:
        print("VIOLATION: --run is required.", file=sys.stderr)
        return 2
    return cmd_run(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
