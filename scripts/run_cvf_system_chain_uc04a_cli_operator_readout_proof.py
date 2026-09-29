#!/usr/bin/env python3
"""Invoke the current autorun CLI exactly twice and emit a two-case operator
readout receipt for system-chain UC-04A (CLI Operator Readout)."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CLI_SCRIPT = REPO_ROOT / "governance" / "compat" / "run_agent_autorun_workflow_gate.py"
DEFAULT_RECEIPT_DIR = REPO_ROOT / ".cvf" / "runtime" / "autorun-receipts"

_ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")

POSITIVE_CASE_ID = "positive_pre_dispatch"
NEGATIVE_CASE_ID = "negative_pre_closure"
HARNESS_INVOCATION_COUNT = 1
CLI_INVOCATION_COUNT = 2
RETRY_COUNT = 0
PROVIDER_CALL_COUNT = 0
CASE_DENOMINATOR = 2

NON_EMPTY_RANGE_MARKER = "closure/push autorun gates require a non-empty committed range"
DIRTY_FINALITY_MARKER = "worktree changes are uncommitted"
CLEAN_FINALITY_MARKER = "worktree is clean"


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def _resolve_command(command: list[str]) -> list[str]:
    if not command:
        return command
    head = command[0]
    if sys.platform.startswith("win") and head == "python":
        return [sys.executable, *command[1:]]
    return command


def _command_digest(command: list[str]) -> str:
    return hashlib.sha256(
        json.dumps([str(c) for c in command], ensure_ascii=True).encode("utf-8")
    ).hexdigest()


def _strip_ansi(text: str) -> str:
    return _ANSI_ESCAPE_RE.sub("", text)


def run_cli(command: list[str]) -> dict[str, Any]:
    started = time.perf_counter()
    proc = subprocess.run(
        _resolve_command(command),
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    duration = round(time.perf_counter() - started, 3)
    stdout = proc.stdout or ""
    clean = _strip_ansi(stdout)

    return {
        "command": [str(c) for c in command],
        "commandSha256": _command_digest(command),
        "exitCode": proc.returncode,
        "durationSeconds": duration,
        "stdout": stdout,
        "perCheckResults": _parse_per_check_results(clean),
        "aggregateCompliant": "COMPLIANT:" in clean,
        "compliantLine": _find_compliant_line(clean),
        "printedDenominator": _count_per_check_lines(clean),
    }


def _parse_per_check_results(output: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("[PASS]") or stripped.startswith("[FAIL]"):
            bracket_end = stripped.index("]")
            status = stripped[1:bracket_end]
            rest = stripped[bracket_end + 1 :].strip()
            paren = rest.rfind("(")
            name = rest[:paren].strip() if paren > 0 else rest
            results.append({"name": name, "status": status})
    return results


def _count_per_check_lines(output: str) -> int:
    count = 0
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("[PASS]") or stripped.startswith("[FAIL]"):
            count += 1
    return count


def _find_compliant_line(output: str) -> str | None:
    for line in output.splitlines():
        if "COMPLIANT:" in line:
            return line.strip()
    return None


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_receipt(receipt_path: Path) -> dict[str, Any] | None:
    if not receipt_path.exists():
        return None
    try:
        data = _read_json(receipt_path)
        return {
            "path": _rel(receipt_path),
            "schema": data.get("schema"),
            "status": data.get("status"),
            "phase": data.get("phase"),
            "checkCount": len(data.get("checks", [])),
            "allChecksPass": all(
                c.get("status") == "PASS" for c in data.get("checks", [])
            ),
        }
    except (json.JSONDecodeError, OSError, KeyError):
        return None


def _parse_negative_markers(output: str) -> dict[str, Any]:
    has_range_failure = NON_EMPTY_RANGE_MARKER in output
    has_dirty_finality = DIRTY_FINALITY_MARKER in output
    has_clean_finality = CLEAN_FINALITY_MARKER in output
    return {
        "nonEmptyRangeFailure": has_range_failure,
        "dirtyFinalityObserved": has_dirty_finality,
        "cleanFinalityObserved": has_clean_finality,
    }


def run_proof(
    execution_base: str,
    receipt_dir: Path,
) -> dict[str, Any]:
    positive_command = [
        sys.executable,
        str(CLI_SCRIPT),
        "--phase", "pre-dispatch",
        "--base", execution_base,
        "--head", "HEAD",
        "--receipt-dir", str(receipt_dir),
    ]

    negative_command = [
        sys.executable,
        str(CLI_SCRIPT),
        "--phase", "pre-closure",
        "--base", execution_base,
        "--head", execution_base,
    ]

    # Positive call
    positive = run_cli(positive_command)
    positive_receipt_path = receipt_dir / "pre-dispatch.json"
    positive_receipt = _parse_receipt(positive_receipt_path)

    # Negative call
    negative = run_cli(negative_command)
    negative_markers = _parse_negative_markers(_strip_ansi(negative["stdout"]))

    # Reconcile positive denominators
    printed_denom = positive["printedDenominator"]
    receipt_denom = positive_receipt["checkCount"] if positive_receipt else 0
    denominator_match = printed_denom == receipt_denom and printed_denom > 0

    positive_pass = (
        positive["exitCode"] == 0
        and positive["aggregateCompliant"]
        and printed_denom > 0
        and all(r["status"] == "PASS" for r in positive["perCheckResults"])
        and positive_receipt is not None
        and positive_receipt.get("status") == "PASS"
        and denominator_match
    )

    negative_pass = (
        negative["exitCode"] != 0
        and negative_markers["nonEmptyRangeFailure"]
    )

    case_pass_count = sum([1 if positive_pass else 0, 1 if negative_pass else 0])
    overall_pass = case_pass_count == 2

    receipt = {
        "proofClass": "CLI_OPERATOR_READOUT_INVOCATION",
        "useCaseId": "UC-04A-CLI-OPERATOR-READOUT",
        "cliOwner": _rel(CLI_SCRIPT),
        "positive_pre_dispatch": {
            "exitCode": positive["exitCode"],
            "aggregateCompliant": positive["aggregateCompliant"],
            "printedDenominator": printed_denom,
            "perCheckResults": positive["perCheckResults"],
            "receiptDenominator": receipt_denom,
            "denominatorMatch": denominator_match,
            "receipt": positive_receipt,
            "commandSha256": positive["commandSha256"],
            "durationSeconds": positive["durationSeconds"],
        },
        "negative_pre_closure": {
            "exitCode": negative["exitCode"],
            "nonEmptyRangeFailure": negative_markers["nonEmptyRangeFailure"],
            "dirtyFinalityObserved": negative_markers["dirtyFinalityObserved"],
            "cleanFinalityObserved": negative_markers["cleanFinalityObserved"],
            "commandSha256": negative["commandSha256"],
            "durationSeconds": negative["durationSeconds"],
        },
        "harnessInvocationCount": HARNESS_INVOCATION_COUNT,
        "cliInvocationCount": CLI_INVOCATION_COUNT,
        "retryCount": RETRY_COUNT,
        "providerCallCount": PROVIDER_CALL_COUNT,
        "caseDenominator": CASE_DENOMINATOR,
        "casePassCount": case_pass_count,
        "overallResult": "PASS" if overall_pass else "FAIL",
    }
    return receipt


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Invoke the autorun CLI twice for UC-04A operator readout proof."
    )
    parser.add_argument("--execution-base", required=True, help="Worker execution base HEAD")
    parser.add_argument("--json-output", required=True, help="Path to write the two-case proof receipt")
    parser.add_argument("--diagnostic-output", required=True, help="Path to write diagnostic JSON (null on PASS)")
    parser.add_argument("--receipt-dir", required=True, help="Directory for the generated CLI PASS receipt")
    args = parser.parse_args(argv)

    execution_base = args.execution_base
    json_output = Path(args.json_output)
    if not json_output.is_absolute():
        json_output = (REPO_ROOT / json_output).resolve()
    json_output.parent.mkdir(parents=True, exist_ok=True)

    diagnostic_output = Path(args.diagnostic_output)
    if not diagnostic_output.is_absolute():
        diagnostic_output = (REPO_ROOT / diagnostic_output).resolve()
    diagnostic_output.parent.mkdir(parents=True, exist_ok=True)

    receipt_dir = Path(args.receipt_dir)
    if not receipt_dir.is_absolute():
        receipt_dir = (REPO_ROOT / receipt_dir).resolve()
    receipt_dir.mkdir(parents=True, exist_ok=True)

    if not CLI_SCRIPT.exists():
        diagnostic = {
            "stage": "cli_owner_verification",
            "failureClass": "MISSING_CLI_OWNER",
            "retryableWithinWorkerScope": False,
            "message": f"CLI owner not found: {_rel(CLI_SCRIPT)}",
        }
        diagnostic_output.write_text(
            json.dumps(diagnostic, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        print(f"BLOCKED: CLI owner not found: {_rel(CLI_SCRIPT)}")
        return 2

    receipt = run_proof(execution_base, receipt_dir)
    json_output.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    if receipt["overallResult"] == "PASS":
        diagnostic_output.write_text(
            json.dumps(None, ensure_ascii=True) + "\n", encoding="utf-8"
        )
    else:
        failed = []
        if not receipt["positive_pre_dispatch"].get("aggregateCompliant"):
            failed.append("positive_pre_dispatch: NOT_COMPLIANT")
        if not receipt["negative_pre_closure"].get("nonEmptyRangeFailure"):
            failed.append("negative_pre_closure: MISSING_RANGE_FAILURE_MARKER")
        if not failed:
            failed.append("UNKNOWN_FAILURE")
        diagnostic = {
            "stage": "cli_proof_execution",
            "failureClass": "EXPECTED_BEHAVIOR_NOT_MET",
            "retryableWithinWorkerScope": False,
            "providerModel": "N/A (zero provider calls)",
            "message": f"failed cases: {failed}",
        }
        diagnostic_output.write_text(
            json.dumps(diagnostic, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )

    print(f"Wrote UC-04A proof receipt: {_rel(json_output)}")
    print(f"Wrote UC-04A diagnostic: {_rel(diagnostic_output)}")
    print(
        f"Result: {receipt['overallResult']} "
        f"({receipt['casePassCount']}/{receipt['caseDenominator']})"
    )
    print(f"CLI calls: {receipt['cliInvocationCount']}, "
          f"harness: {receipt['harnessInvocationCount']}, "
          f"retries: {receipt['retryCount']}, "
          f"provider: {receipt['providerCallCount']}")
    return 0 if receipt["overallResult"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
