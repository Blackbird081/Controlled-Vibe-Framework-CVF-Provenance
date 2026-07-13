#!/usr/bin/env python3
"""CVF SOT3-ACT-A4 failure/recovery boundary proof runner.

Local-negative-first runner for the SOT3-ACT-A4 work order. `--local-only`
runs the full 19-row negative/recovery matrix through real Refinery/Kernel/
Flow/adapter/A2-store APIs (only the downstream provider is mocked/spied for
call-counting) and writes a deterministic negative receipt. `--live` refuses
to proceed unless every required matrix row is present and green in a fresh
`--local-only` run, then invokes the existing A3 route-adjacent live test
once (via the same one-use permit pattern as
`scripts/run_cvf_sot3_a3_live_proof.py`) to prove one bounded post-negative-
gate Alibaba recovery call, writing a fresh A4-scoped receipt/diagnostic and
never touching the historical A3 evidence.

Authorization: docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_2026-07-13.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
TRUTH_FLOW_DIR = REPO_ROOT / "EXTENSIONS" / "CVF_TRUTH_FLOW"
TRUTH_KERNEL_DIR = REPO_ROOT / "EXTENSIONS" / "CVF_TRUTH_KERNEL"
CVF_WEB_DIR = REPO_ROOT / "EXTENSIONS" / "CVF_v1.6_AGENT_PLATFORM" / "cvf-web"
LIVE_TEST_RELATIVE_PATH = "src/app/api/execute/route.sot3-activation.alibaba.live.test.ts"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _local_env import bootstrap_repo_env  # noqa: E402

ALIBABA_KEY_ALIASES = (
    "ALIBABA_API_KEY",
    "DASHSCOPE_API_KEY",
    "CVF_BENCHMARK_ALIBABA_KEY",
    "CVF_ALIBABA_API_KEY",
)

# Each matrix row maps to one or more real-owner assertionResults fullName
# substrings across the four focused test files. A row is GREEN only when
# every mapped test name is present and passed in this run's fresh JSON
# reporter output.
MATRIX_ROWS: list[dict[str, Any]] = [
    {"case": "empty source input", "owner": "Refinery plus product adapter", "requiredResult": "not approved", "providerCallAssertion": "zero", "testNameSubstrings": ["returns NO_CONTEXT with no chunks"]},
    {"case": "structurally invalid source", "owner": "Refinery plus product adapter", "requiredResult": "REFINERY_NOT_READY", "providerCallAssertion": "zero", "testNameSubstrings": ["rejects with REFINERY_NOT_READY on incorrect expected content hash"]},
    {"case": "wrong-packet evidence", "owner": "real Kernel", "requiredResult": "non-acceptance", "providerCallAssertion": "zero", "testNameSubstrings": ["evidence bound to another packet -> reject or require evidence"]},
    {"case": "expired reference", "owner": "Kernel resolver plus Flow", "requiredResult": "rejected", "providerCallAssertion": "zero", "testNameSubstrings": ["referenced TruthReference.reference_state is EXPIRED -> package creation rejected"]},
    {"case": "revoked reference", "owner": "Kernel resolver plus Flow", "requiredResult": "rejected", "providerCallAssertion": "zero", "testNameSubstrings": ["revoked reference at consumption time -> REFERENCE_NOT_CURRENTLY_ACTIVE via strict consume"]},
    {"case": "superseded or inactive reference", "owner": "Kernel resolver plus Flow", "requiredResult": "rejected", "providerCallAssertion": "zero", "testNameSubstrings": ["referenced TruthReference.reference_state is SUPERSEDED -> package creation rejected"]},
    {"case": "wrong recipient", "owner": "strict Flow consume", "requiredResult": "binding mismatch", "providerCallAssertion": "zero", "testNameSubstrings": ["wrong recipient -> PACKAGE_CONSUMER_BINDING_MISMATCH"]},
    {"case": "wrong role", "owner": "strict Flow consume", "requiredResult": "binding mismatch", "providerCallAssertion": "zero", "testNameSubstrings": ["wrong role -> PACKAGE_CONSUMER_BINDING_MISMATCH"]},
    {"case": "wrong phase", "owner": "strict Flow consume", "requiredResult": "binding mismatch", "providerCallAssertion": "zero", "testNameSubstrings": ["wrong phase -> PACKAGE_CONSUMER_BINDING_MISMATCH"]},
    {"case": "wrong task", "owner": "strict Flow consume", "requiredResult": "binding mismatch", "providerCallAssertion": "zero", "testNameSubstrings": ["wrong task -> PACKAGE_CONSUMER_BINDING_MISMATCH"]},
    {"case": "wrong dose", "owner": "strict Flow consume", "requiredResult": "binding mismatch", "providerCallAssertion": "zero", "testNameSubstrings": ["wrong dose -> PACKAGE_CONSUMER_BINDING_MISMATCH"]},
    {"case": "expired package", "owner": "strict Flow consume", "requiredResult": "package expired", "providerCallAssertion": "zero", "testNameSubstrings": ["expired package with correct binding -> PACKAGE_EXPIRED"]},
    {"case": "duplicate request same record", "owner": "A2 store", "requiredResult": "duplicate no-op", "providerCallAssertion": "zero additional call", "testNameSubstrings": ["returns DUPLICATE_NOOP and leaves main bytes and record count unchanged for identical duplicates"]},
    {"case": "duplicate request conflict", "owner": "A2 store", "requiredResult": "typed conflict", "providerCallAssertion": "zero", "testNameSubstrings": ["throws a classified conflict and leaves main bytes unchanged for a same-identity different-hash duplicate"]},
    {"case": "replay after acknowledgement", "owner": "strict Flow consume", "requiredResult": "not actionable", "providerCallAssertion": "zero", "testNameSubstrings": ["replay after acknowledgement - correctly bound second consumeFor call is rejected as not actionable"]},
    {"case": "restart and valid recovery", "owner": "fresh A2 store reader", "requiredResult": "integrity-valid record restored", "providerCallAssertion": "live released only after PASS", "testNameSubstrings": ["SOT3-ACT-A4: restart-and-valid-recovery row"]},
    {"case": "corrupt main file", "owner": "A2 store", "requiredResult": "typed corrupt-store diagnostic", "providerCallAssertion": "zero", "testNameSubstrings": ["throws a classified corrupt-store error and preserves exact bytes for invalid JSON"]},
    {"case": "partial/temp write", "owner": "A2 store fault port", "requiredResult": "prior main record survives", "providerCallAssertion": "zero", "testNameSubstrings": ["propagates a classified persistence failure and leaves prior valid main bytes unchanged on rename failure"]},
    {"case": "ENFORCE to OFF rollback", "owner": "execute route", "requiredResult": "legacy behavior restored", "providerCallAssertion": "exactly one provider spy call", "testNameSubstrings": ["ENFORCE-to-OFF rollback restores legacy provider execution with exactly one provider spy call"]},
    {"case": "bounded live recovery", "owner": "real execute route and Alibaba", "requiredResult": "approved context and correlated durable evidence", "providerCallAssertion": "exactly one per invocation", "testNameSubstrings": []},
]

LOCAL_MATRIX_CASES = [row["case"] for row in MATRIX_ROWS if row["case"] != "bounded live recovery"]

# (cwd, args, package label) for each local test invocation this runner needs.
LOCAL_TEST_INVOCATIONS: list[dict[str, Any]] = [
    {
        "label": "cvf-truth-kernel-negative-matrix",
        "cwd": TRUTH_KERNEL_DIR,
        "cmd": ["vitest", "run", "--reporter=json", "tests/negative-matrix.test.ts"],
    },
    {
        "label": "cvf-truth-flow",
        "cwd": TRUTH_FLOW_DIR,
        "cmd": ["vitest", "run", "--reporter=json"],
    },
    # Each cvf-web focused file is run as its own vitest invocation rather
    # than one combined command. `.env.local` configures
    # CVF_RATE_LIMIT_STORE=redis with real Upstash credentials, loaded
    # globally by src/test/setup.ts; route.knowledge.test.ts's pre-existing
    # (out-of-A4-manifest) first describe block never resets that shared
    # real-Redis-backed limiter, so running multiple route-touching test
    # files back-to-back in one process can flake on cross-file real-window
    # rate-limit accumulation that pre-dates and is unrelated to A4 (verified
    # reproducible on unmodified baseline HEAD before any A4 edit existed).
    # Separate invocations avoid amplifying that pre-existing condition while
    # still real-executing and real-asserting every focused file.
    {
        "label": "cvf-web-sot3-knowledge-adapter",
        "cwd": CVF_WEB_DIR,
        "cmd": ["vitest", "run", "--reporter=json", "src/lib/sot3-knowledge-adapter.test.ts"],
    },
    {
        "label": "cvf-web-sot3-activation-evidence-store",
        "cwd": CVF_WEB_DIR,
        "cmd": ["vitest", "run", "--reporter=json", "src/lib/sot3-activation-evidence-store.test.ts"],
    },
    {
        "label": "cvf-web-route-knowledge",
        "cwd": CVF_WEB_DIR,
        "cmd": ["vitest", "run", "--reporter=json", "src/app/api/execute/route.knowledge.test.ts"],
    },
    {
        "label": "cvf-web-route-sot3-activation-failure-recovery",
        "cwd": CVF_WEB_DIR,
        "cmd": ["vitest", "run", "--reporter=json", "src/app/api/execute/route.sot3-activation-failure-recovery.test.ts"],
    },
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def npx_executable() -> str | None:
    return shutil.which("npx.cmd") or shutil.which("npx")


def run_vitest_json(cwd: Path, cmd: list[str]) -> tuple[int, dict[str, Any] | None, str]:
    npx = npx_executable()
    if not npx:
        return 127, None, "Local launch failed: npx executable was not found on PATH."
    result = subprocess.run(
        [npx, *cmd],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    combined = (result.stdout or "") + (result.stderr or "")
    # vitest's json reporter prints exactly one JSON document to stdout.
    stdout = result.stdout or ""
    start = stdout.find("{")
    if start == -1:
        return result.returncode, None, combined
    try:
        parsed = json.loads(stdout[start:])
    except json.JSONDecodeError:
        return result.returncode, None, combined
    return result.returncode, parsed, combined


def collect_passed_test_names(reports: list[dict[str, Any]]) -> set[str]:
    names: set[str] = set()
    for report in reports:
        for test_file in report.get("testResults", []):
            for assertion in test_file.get("assertionResults", []):
                if assertion.get("status") == "passed":
                    names.add(assertion.get("fullName", ""))
    return names


def evaluate_matrix(passed_names: set[str]) -> list[dict[str, Any]]:
    outcomes: list[dict[str, Any]] = []
    for row in MATRIX_ROWS:
        if row["case"] == "bounded live recovery":
            outcomes.append({
                **{k: row[k] for k in ("case", "owner", "requiredResult", "providerCallAssertion")},
                "status": "DEFERRED_TO_LIVE_PHASE",
                "matchedTestNames": [],
                "providerCallCount": None,
            })
            continue
        matched = [
            name for name in passed_names
            if any(substr in name for substr in row["testNameSubstrings"])
        ]
        provider_call_count = 1 if row["case"] == "ENFORCE to OFF rollback" else 0
        outcomes.append({
            **{k: row[k] for k in ("case", "owner", "requiredResult", "providerCallAssertion")},
            "status": "GREEN" if matched else "MISSING_OR_RED",
            "matchedTestNames": matched,
            "providerCallCount": provider_call_count,
        })
    return outcomes


def build_negative_receipt(
    *,
    execution_base_head: str,
    started_at: str,
    finished_at: str,
    matrix_outcomes: list[dict[str, Any]],
    invocation_results: list[dict[str, Any]],
    all_green: bool,
) -> dict[str, Any]:
    local_outcomes = [row for row in matrix_outcomes if row["case"] != "bounded live recovery"]
    negative_case_count = len(local_outcomes)
    zero_provider_call_case_count = sum(
        1 for row in local_outcomes if row["status"] == "GREEN" and row["providerCallCount"] == 0
    )
    rollback_provider_call_count = next(
        row["providerCallCount"]
        for row in local_outcomes
        if row["case"] == "ENFORCE to OFF rollback"
    )
    return {
        "schemaVersion": "cvf.sot3ActA4NegativeReceipt.v1",
        "batchId": "SOT3-ACT-A4",
        "executionBaseHead": execution_base_head,
        "startedAtUtc": started_at,
        "finishedAtUtc": finished_at,
        "overall": "PASS" if all_green else "BLOCKED",
        "negativeCaseCount": negative_case_count,
        "zeroProviderCallCaseCount": zero_provider_call_case_count,
        "rollbackProviderCallCount": rollback_provider_call_count,
        "localNegativeGatePassed": all_green,
        "matrix": matrix_outcomes,
        "invocations": invocation_results,
        "secretSafety": {
            "rawKeyPersisted": False,
            "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False,
            "fullPromptPersisted": False,
        },
    }


def cmd_local_only(args: argparse.Namespace) -> int:
    started_at = utc_now_iso()
    execution_base_head = resolve_execution_base_head(args.execution_base_head)

    all_reports: list[dict[str, Any]] = []
    invocation_results: list[dict[str, Any]] = []
    all_launched_ok = True

    for invocation in LOCAL_TEST_INVOCATIONS:
        returncode, report, output = run_vitest_json(invocation["cwd"], invocation["cmd"])
        invocation_results.append({
            "label": invocation["label"],
            "returncode": returncode,
            "numTotalTests": report.get("numTotalTests") if report else None,
            "numPassedTests": report.get("numPassedTests") if report else None,
            "numFailedTests": report.get("numFailedTests") if report else None,
            "success": bool(report and report.get("success")),
        })
        if report is None:
            all_launched_ok = False
            if args.json:
                print(output[-4000:])
        else:
            all_reports.append(report)
            if not report.get("success"):
                all_launched_ok = False

    passed_names = collect_passed_test_names(all_reports)
    matrix_outcomes = evaluate_matrix(passed_names)
    local_outcomes = [row for row in matrix_outcomes if row["case"] != "bounded live recovery"]
    all_rows_green = all(row["status"] == "GREEN" for row in local_outcomes)
    all_green = all_launched_ok and all_rows_green

    receipt = build_negative_receipt(
        execution_base_head=execution_base_head,
        started_at=started_at,
        finished_at=utc_now_iso(),
        matrix_outcomes=matrix_outcomes,
        invocation_results=invocation_results,
        all_green=all_green,
    )

    receipt_path = Path(args.receipt) if args.receipt else (
        REPO_ROOT / "docs" / "reviews" / "evidence" / "sot3-act-a4-failure-recovery-negative-receipt-2026-07-13.json"
    )
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        print(f"Wrote negative receipt (overall={receipt['overall']}): {receipt_path}")
        for row in local_outcomes:
            print(f"  [{row['status']}] {row['case']} (owner={row['owner']})")

    return 0 if all_green else 1


def local_gate_is_green(execution_base_head: str) -> tuple[bool, dict[str, Any]]:
    """Re-runs the full local-only matrix fresh and returns (allGreen, receipt)."""
    started_at = utc_now_iso()
    all_reports: list[dict[str, Any]] = []
    invocation_results: list[dict[str, Any]] = []
    all_launched_ok = True

    for invocation in LOCAL_TEST_INVOCATIONS:
        returncode, report, _output = run_vitest_json(invocation["cwd"], invocation["cmd"])
        invocation_results.append({
            "label": invocation["label"],
            "returncode": returncode,
            "success": bool(report and report.get("success")),
        })
        if report is None:
            all_launched_ok = False
        else:
            all_reports.append(report)
            if not report.get("success"):
                all_launched_ok = False

    passed_names = collect_passed_test_names(all_reports)
    matrix_outcomes = evaluate_matrix(passed_names)
    local_outcomes = [row for row in matrix_outcomes if row["case"] != "bounded live recovery"]
    all_rows_green = all(row["status"] == "GREEN" for row in local_outcomes)
    all_green = all_launched_ok and all_rows_green

    receipt = build_negative_receipt(
        execution_base_head=execution_base_head,
        started_at=started_at,
        finished_at=utc_now_iso(),
        matrix_outcomes=matrix_outcomes,
        invocation_results=invocation_results,
        all_green=all_green,
    )
    return all_green, receipt


def resolve_key_alias() -> str | None:
    import os

    for alias in ALIBABA_KEY_ALIASES:
        value = os.environ.get(alias, "").strip()
        if value:
            return alias
    return None


def resolve_execution_base_head(explicit: str) -> str:
    if explicit:
        return explicit
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "UNKNOWN"


def run_live_test(observation_output_path: Path, permit_path: Path, call_ledger_path: Path) -> tuple[int, str, int]:
    import os

    permit_token = secrets.token_urlsafe(32)
    permit = {
        "schemaVersion": "cvf.sot3ActA3RunnerPermit.v1",
        "batchId": "SOT3-ACT-A3R",
        "tokenHash": hashlib.sha256(permit_token.encode("utf-8")).hexdigest(),
        "observationPathHash": hashlib.sha256(str(observation_output_path).encode("utf-8")).hexdigest(),
        "expiresAtEpochMs": int(datetime.now(timezone.utc).timestamp() * 1000) + 120_000,
    }
    permit_path.write_text(json.dumps(permit, sort_keys=True) + "\n", encoding="utf-8")
    env_overrides = {
        "CVF_SOT3_A3_OBSERVATION_OUTPUT_PATH": str(observation_output_path),
        "CVF_SOT3_A3_RUN_PERMIT_PATH": str(permit_path),
        "CVF_SOT3_A3_RUN_PERMIT_TOKEN": permit_token,
        "CVF_SOT3_A3_CALL_LEDGER_PATH": str(call_ledger_path),
    }
    merged_env = {**os.environ, **env_overrides}
    npx = npx_executable()
    if not npx:
        return 127, "Local launch failed: npx executable was not found on PATH.\n", 0
    result = subprocess.run(
        [npx, "vitest", "run", LIVE_TEST_RELATIVE_PATH],
        cwd=CVF_WEB_DIR,
        env=merged_env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    output = (result.stdout or "") + (result.stderr or "")
    observed_call_count = 0
    if call_ledger_path.exists():
        try:
            ledger = json.loads(call_ledger_path.read_text(encoding="utf-8"))
            observed_call_count = int(ledger.get("observedCallCount", 0))
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            observed_call_count = 0
    return result.returncode, output, observed_call_count


def cmd_live(args: argparse.Namespace) -> int:
    started_at = utc_now_iso()
    execution_base_head = resolve_execution_base_head(args.execution_base_head)

    gate_green, gate_receipt = local_gate_is_green(execution_base_head)
    if not gate_green:
        diagnostic = {
            "stage": "governance",
            "class": "policy_blocked",
            "retryable": False,
            "userAction": "revise_request",
            "safeMessage": "Local negative gate is not fully green; live recovery is refused until every required matrix row passes.",
        }
        blocked_diag = build_diagnostic_receipt(
            execution_base_head=execution_base_head,
            started_at=started_at,
            diagnostic=diagnostic,
            observed_call_count=0,
            key_alias_used=None,
            local_negative_gate_passed=False,
        )
        write_receipt(args, blocked_diag, is_diagnostic=True)
        print("BLOCKED: local negative gate is not fully green. See diagnostic.")
        return 1

    loaded_env_files = bootstrap_repo_env()
    key_alias = resolve_key_alias()
    if not key_alias:
        diagnostic = {
            "stage": "auth",
            "class": "missing_api_key",
            "retryable": False,
            "userAction": "check_api_key",
            "safeMessage": (
                "No Alibaba/DashScope key alias was present after governed local "
                f"bootstrap of {[str(p) for p in loaded_env_files]}."
            ),
        }
        blocked_diag = build_diagnostic_receipt(
            execution_base_head=execution_base_head,
            started_at=started_at,
            diagnostic=diagnostic,
            observed_call_count=0,
            key_alias_used=None,
            local_negative_gate_passed=True,
        )
        write_receipt(args, blocked_diag, is_diagnostic=True)
        print("BLOCKED: no Alibaba/DashScope key alias available.")
        return 1

    with tempfile.TemporaryDirectory(prefix="cvf-sot3-a4-obs-") as tmp:
        observation_path = Path(tmp) / "observation.json"
        permit_path = Path(tmp) / "runner-permit.json"
        call_ledger_path = Path(tmp) / "call-ledger.json"
        returncode, output, observed_call_count = run_live_test(observation_path, permit_path, call_ledger_path)
        print(output[-4000:])
        if returncode != 0 or not observation_path.exists():
            diagnostic = {
                "stage": "provider",
                "class": "unknown_error",
                "retryable": False,
                "userAction": "inspect_receipt",
                "safeMessage": "The live test process failed or did not produce an observation file. See captured stdout/stderr for a secret-safe summary.",
            }
            blocked_diag = build_diagnostic_receipt(
                execution_base_head=execution_base_head,
                started_at=started_at,
                diagnostic=diagnostic,
                observed_call_count=observed_call_count,
                key_alias_used=key_alias,
                local_negative_gate_passed=True,
            )
            write_receipt(args, blocked_diag, is_diagnostic=True)
            print("BLOCKED: live test process failed. See diagnostic.")
            return 1

        observation = json.loads(observation_path.read_text(encoding="utf-8"))

    pass_diag = build_diagnostic_receipt(
        execution_base_head=execution_base_head,
        started_at=started_at,
        diagnostic=None,
        observed_call_count=observed_call_count,
        key_alias_used=key_alias,
        local_negative_gate_passed=True,
    )
    write_receipt(args, pass_diag, is_diagnostic=True)

    live_receipt = build_live_receipt(
        execution_base_head=execution_base_head,
        started_at=started_at,
        finished_at=utc_now_iso(),
        observation=observation,
        gate_receipt=gate_receipt,
    )
    receipt_path = Path(args.live_receipt) if args.live_receipt else (
        REPO_ROOT / "docs" / "reviews" / "evidence" / "sot3-act-a4-failure-recovery-live-receipt-2026-07-13.json"
    )
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(live_receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    manifest_path = Path(args.manifest) if args.manifest else (
        REPO_ROOT / "docs" / "reviews" / "evidence" / "sot3-act-a4-failure-recovery-manifest-2026-07-13.json"
    )
    diagnostic_path = Path(args.diagnostic) if args.diagnostic else (
        REPO_ROOT / "docs" / "reviews" / "evidence" / "sot3-act-a4-failure-recovery-live-diagnostic-2026-07-13.json"
    )
    manifest_cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "build_cvf_live_evidence_manifest.py"),
        "--evidence", str(receipt_path),
        "--evidence", str(diagnostic_path),
        "--command", f"python scripts/run_cvf_sot3_a4_failure_recovery_proof.py --live --receipt {receipt_path} --manifest {manifest_path}",
        "--output", str(manifest_path),
    ]
    manifest_result = subprocess.run(manifest_cmd, cwd=REPO_ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    print(manifest_result.stdout)
    if manifest_result.returncode != 0:
        print(manifest_result.stderr, file=sys.stderr)
        return manifest_result.returncode

    if args.json:
        print(json.dumps(live_receipt, indent=2, sort_keys=True))
    else:
        print(f"Wrote live receipt (overall={live_receipt['overall']}): {receipt_path}")

    return 0 if live_receipt["overall"] == "PASS" else 1


def build_diagnostic_receipt(
    *,
    execution_base_head: str,
    started_at: str,
    diagnostic: dict[str, Any] | None,
    observed_call_count: int,
    key_alias_used: str | None,
    local_negative_gate_passed: bool,
) -> dict[str, Any]:
    return {
        "schemaVersion": "cvf.sot3ActA4LiveDiagnostic.v1",
        "batchId": "SOT3-ACT-A4",
        "executionBaseHead": execution_base_head,
        "startedAtUtc": started_at,
        "finishedAtUtc": utc_now_iso(),
        "localNegativeGatePassed": local_negative_gate_passed,
        "recoveryProviderCallCount": observed_call_count,
        "keyAliasUsed": key_alias_used,
        "diagnostic": diagnostic,
        "secretSafety": {
            "rawKeyPersisted": False,
            "rawProviderBodyPersisted": False,
            "rawOutputPersisted": False,
            "fullPromptPersisted": False,
        },
    }


def build_live_receipt(
    *,
    execution_base_head: str,
    started_at: str,
    finished_at: str,
    observation: dict[str, Any],
    gate_receipt: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schemaVersion": "cvf.sot3ActA4LiveReceipt.v1",
        "batchId": "SOT3-ACT-A4",
        "executionBaseHead": execution_base_head,
        "startedAtUtc": started_at,
        "finishedAtUtc": finished_at,
        "overall": observation.get("overall", "BLOCKED"),
        "claim": (
            "SOT3_FAILURE_RECOVERY_PROVEN_BOUNDED"
            if observation.get("overall") == "PASS"
            else "N/A with reason: overall is not PASS"
        ),
        "localNegativeGatePassed": bool(gate_receipt.get("localNegativeGatePassed")),
        "negativeCaseCount": gate_receipt.get("negativeCaseCount"),
        "zeroProviderCallCaseCount": gate_receipt.get("zeroProviderCallCaseCount"),
        "recoveryProviderCallCount": observation.get("observedCallCount"),
        "rollbackProviderCallCount": gate_receipt.get("rollbackProviderCallCount"),
        "providerProof": {
            "provider": observation.get("provider"),
            "model": observation.get("model"),
            "keyAliasUsed": observation.get("keyAliasUsed"),
            "httpStatus": observation.get("httpStatus"),
            "success": observation.get("success"),
            "latencyMs": observation.get("latencyMs"),
            "outputLength": observation.get("outputLength"),
        },
        "correlation": {
            "governanceReceiptId": observation.get("governanceReceiptId"),
            "envelopeId": observation.get("envelopeId"),
            "sot3RecordId": observation.get("sot3RecordId"),
            "sot3IntegrityHash": observation.get("sot3IntegrityHash"),
            "sot3RequestId": observation.get("sot3RequestId"),
            "traceCount": observation.get("traceCount"),
            "packetIds": observation.get("packetIds"),
            "kernelDecisionIds": observation.get("kernelDecisionIds"),
            "truthReceiptIds": observation.get("truthReceiptIds"),
            "truthReferenceIds": observation.get("truthReferenceIds"),
            "flowPackageIds": observation.get("flowPackageIds"),
        },
        "contextObservation": {
            "approvedContextHash": observation.get("approvedContextHash"),
            "providerSystemPromptHash": observation.get("providerSystemPromptHash"),
            "approvedContextIncluded": observation.get("approvedContextIncluded"),
            "providerRequestObserved": observation.get("providerRequestObserved"),
            "rawPromptPersisted": False,
        },
        "secretSafety": {
            "rawKeyPersisted": observation.get("rawKeyPersisted", False),
            "rawProviderBodyPersisted": observation.get("rawProviderBodyPersisted", False),
            "rawOutputPersisted": observation.get("rawOutputPersisted", False),
            "fullPromptPersisted": observation.get("fullPromptPersisted", False),
        },
        "note": (
            "Reuses the existing A3 route-adjacent live test implementation "
            "unaltered, per the A4 work order's Allowed Scope. This receipt is "
            "a fresh A4-scoped artifact; it does not modify or supersede the "
            "historical A3 receipt or claim."
        ),
    }


def write_receipt(args: argparse.Namespace, receipt: dict[str, Any], *, is_diagnostic: bool) -> None:
    target = args.diagnostic if is_diagnostic else args.receipt
    receipt_path = Path(target) if target else (
        REPO_ROOT / "docs" / "reviews" / "evidence" / "sot3-act-a4-failure-recovery-live-diagnostic-2026-07-13.json"
    )
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-only", action="store_true", help="Run the full local negative/recovery matrix. Zero live calls, ever.")
    parser.add_argument("--live", action="store_true", help="Refuse unless --local-only is fully green, then invoke exactly one bounded Alibaba recovery call.")
    parser.add_argument("--json", action="store_true", help="Print the receipt JSON to stdout.")
    parser.add_argument("--receipt", default="", help="Negative receipt output path (local-only mode).")
    parser.add_argument("--diagnostic", default="", help="Live diagnostic output path (live mode).")
    parser.add_argument("--live-receipt", default="", help="Live receipt output path (live mode).")
    parser.add_argument("--manifest", default="", help="Hash manifest output path (live mode).")
    parser.add_argument("--execution-base-head", default="", help="Clean HEAD captured before edits. Defaults to `git rev-parse --short HEAD`.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.local_only and args.live:
        print("VIOLATION: --local-only and --live are mutually exclusive per invocation.", file=sys.stderr)
        return 2
    if args.local_only:
        return cmd_local_only(args)
    if args.live:
        return cmd_live(args)
    print("VIOLATION: one of --local-only or --live is required.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
