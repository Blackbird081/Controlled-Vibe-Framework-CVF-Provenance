#!/usr/bin/env python3
"""Invoke the GC-011 SDK-to-PipelineOrchestrator proof once and emit a
current-run receipt for system-chain UC-03 (CONTRACT-TO-RUNTIME)."""

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

_ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")
EXTENSIONS_DIR = REPO_ROOT / "EXTENSIONS" / "CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL"
PROOF_TEST_FILE = EXTENSIONS_DIR / "tests" / "system.chain.uc03.contract.runtime.proof.test.ts"

PROOF_COMMAND_BASE = ["npx", "vitest", "run", "--reporter=verbose"]
PROOF_ENV = os.environ.copy()

SELECTED_CONTROL_ID = "GC-011"
CASE_DENOMINATOR = 2


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def _resolve_command(command: list[str]) -> list[str]:
    if not command:
        return command
    head = command[0]
    if sys.platform.startswith("win"):
        if head == "npx":
            return ["npx.cmd", *command[1:]]
        if head == "npm":
            return ["npm.cmd", *command[1:]]
    return command


def run_proof(proof_test: Path) -> dict[str, Any]:
    started_at = time.perf_counter()
    command = [*PROOF_COMMAND_BASE, str(proof_test)]

    proc = subprocess.run(
        _resolve_command(command),
        cwd=EXTENSIONS_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=PROOF_ENV,
    )
    duration_seconds = round(time.perf_counter() - started_at, 3)
    output = proc.stdout.strip()
    exit_code = proc.returncode

    # Parse vitest output for individual test results
    test_results = _parse_vitest_results(output)

    pass_count = sum(1 for t in test_results if t["result"] == "PASS")
    overall_pass = exit_code == 0 and pass_count == CASE_DENOMINATOR

    return {
        "proofClass": "CONTRACT_TO_RUNTIME_INVOCATION",
        "useCaseId": "UC-03-CONTRACT-TO-RUNTIME-REPRESENTATIVE-PATH",
        "selectedControlId": SELECTED_CONTROL_ID,
        "callerChain": "CvfSdk -> PipelineOrchestrator",
        "proofRunInvocationCount": 1,
        "retryCount": 0,
        "providerCallCount": 0,
        "caseDenominator": CASE_DENOMINATOR,
        "casePassCount": pass_count,
        "overallResult": "PASS" if overall_pass else "FAIL",
        "durationSeconds": duration_seconds,
        "cases": test_results,
        "command": [str(c) for c in command],
        "commandSha256": hashlib.sha256(
            json.dumps([str(c) for c in command], ensure_ascii=True).encode("utf-8")
        ).hexdigest(),
        "workdir": _rel(EXTENSIONS_DIR),
    }


def _parse_vitest_results(output: str) -> list[dict[str, Any]]:
    """Parse vitest output to extract individual test case results."""
    clean = _ANSI_ESCAPE_RE.sub("", output)
    cases: list[dict[str, Any]] = []

    # vitest outputs lines like:
    #   [PASS] GC-011 positive: ... (N ms)
    #   [FAIL] GC-011 negative: ... (N ms)
    for line in clean.splitlines():
        stripped = line.strip()
        if stripped.startswith("\u2713") or stripped.startswith("\u2714"):
            # Pass case
            name = stripped[1:].strip()
            # Remove trailing duration
            paren = name.rfind("(")
            if paren > 0:
                name = name[:paren].strip()
            cases.append({"name": name, "result": "PASS"})
        elif stripped.startswith("\u00d7"):
            # Fail case
            name = stripped[1:].strip()
            paren = name.rfind("(")
            if paren > 0:
                name = name[:paren].strip()
            cases.append({"name": name, "result": "FAIL"})

    return cases


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Invoke the GC-011 SDK-to-PipelineOrchestrator proof once."
    )
    parser.add_argument(
        "--json-output",
        required=True,
        help="Path to write the UC-03 proof JSON receipt",
    )
    parser.add_argument(
        "--diagnostic-output",
        required=True,
        help="Path to write a secret-safe diagnostic JSON (null on PASS)",
    )
    args = parser.parse_args(argv)

    json_output = Path(args.json_output)
    if not json_output.is_absolute():
        json_output = (REPO_ROOT / json_output).resolve()
    json_output.parent.mkdir(parents=True, exist_ok=True)

    diagnostic_output = Path(args.diagnostic_output)
    if not diagnostic_output.is_absolute():
        diagnostic_output = (REPO_ROOT / diagnostic_output).resolve()
    diagnostic_output.parent.mkdir(parents=True, exist_ok=True)

    if not PROOF_TEST_FILE.exists():
        diagnostic = {
            "stage": "proof_file_verification",
            "failureClass": "MISSING_PROOF_FILE",
            "retryableWithinWorkerScope": False,
            "message": f"Proof test file not found: {_rel(PROOF_TEST_FILE)}",
        }
        diagnostic_output.write_text(
            json.dumps(diagnostic, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        print(f"BLOCKED: proof test file not found: {_rel(PROOF_TEST_FILE)}")
        return 2

    receipt = run_proof(PROOF_TEST_FILE)
    json_output.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    if receipt["overallResult"] == "PASS":
        diagnostic_output.write_text(
            json.dumps(None, ensure_ascii=True) + "\n", encoding="utf-8"
        )
    else:
        failed = [c["name"] for c in receipt["cases"] if c["result"] != "PASS"]
        if not failed:
            failed = ["UNKNOWN_VITEST_FAILURE"]
        diagnostic = {
            "stage": "proof_execution",
            "failureClass": "CASE_FAILURE",
            "retryableWithinWorkerScope": False,
            "providerModel": "N/A (zero provider calls)",
            "message": f"failed cases: {failed}",
        }
        diagnostic_output.write_text(
            json.dumps(diagnostic, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )

    print(f"Wrote UC-03 proof receipt: {_rel(json_output)}")
    print(f"Wrote UC-03 diagnostic: {_rel(diagnostic_output)}")
    print(
        f"Result: {receipt['overallResult']} "
        f"({receipt['casePassCount']}/{receipt['caseDenominator']})"
    )
    return 0 if receipt["overallResult"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
