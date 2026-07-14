#!/usr/bin/env python3
"""Invoke the canonical CF-076 through CF-084 registry chain once and emit a
current-run receipt for system-chain UC-02 (RUNTIME_TO_ENFORCEMENT)."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SCENARIO_REGISTRY = REPO_ROOT / "docs" / "reference" / "CVF_CONFORMANCE_SCENARIOS.json"
BOOTSTRAP_COMMAND = ["python", "scripts/run_cvf_packet_posture_state_bootstrap.py"]
BOOTSTRAP_SKIP_ENV = {"CVF_SKIP_PACKET_POSTURE_STATE_BOOTSTRAP": "1"}
PACKET_RUNNER_PREFIX = ["python", "scripts/run_cvf_packet_posture_gate_conformance.py", "--gate"]

TARGET_SCENARIO_IDS = (
    "CF-076",
    "CF-077",
    "CF-078",
    "CF-079",
    "CF-080",
    "CF-081",
    "CF-082",
    "CF-083",
    "CF-084",
)


@dataclass
class Scenario:
    scenario_id: str
    title: str
    command: list[str]
    workdir: Path


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _command_digest(command: list[str]) -> str:
    return hashlib.sha256(json.dumps(command, ensure_ascii=True).encode("utf-8")).hexdigest()


class ScenarioSelectionError(Exception):
    """Raised when the canonical registry does not contain the exact target set."""


def load_target_scenarios(registry_path: Path | None = None) -> list[Scenario]:
    registry = _read_json(registry_path if registry_path is not None else SCENARIO_REGISTRY)
    by_id: dict[str, Scenario] = {}
    for item in registry.get("scenarios", []):
        scenario_id = item["scenarioId"]
        if scenario_id not in TARGET_SCENARIO_IDS:
            continue
        if scenario_id in by_id:
            raise ScenarioSelectionError(f"DUPLICATE_SCENARIO_ID: {scenario_id}")
        command = item["command"]
        if command[: len(PACKET_RUNNER_PREFIX)] != PACKET_RUNNER_PREFIX:
            raise ScenarioSelectionError(
                f"COMMAND_PREFIX_MISMATCH: {scenario_id} does not route through the packet-posture runner"
            )
        gate = command[len(PACKET_RUNNER_PREFIX)] if len(command) > len(PACKET_RUNNER_PREFIX) else ""
        gate_name = Path(gate).name
        if not gate_name.startswith("check_") or not gate_name.endswith(".py"):
            raise ScenarioSelectionError(
                f"COMMAND_GATE_MISMATCH: {scenario_id} does not name a governance/compat check_*.py gate"
            )
        by_id[scenario_id] = Scenario(
            scenario_id=scenario_id,
            title=item["title"],
            command=command,
            workdir=(REPO_ROOT / item["workdir"]).resolve(),
        )

    missing = [sid for sid in TARGET_SCENARIO_IDS if sid not in by_id]
    if missing:
        raise ScenarioSelectionError(f"MISSING_SCENARIO_IDS: {missing}")

    return [by_id[sid] for sid in TARGET_SCENARIO_IDS]


def _resolve_command(command: list[str]) -> list[str]:
    if not command:
        return command
    head = command[0]
    if head == "python":
        return [sys.executable, *command[1:]]
    if sys.platform.startswith("win"):
        if head == "npm":
            return ["npm.cmd", *command[1:]]
        if head == "npx":
            return ["npx.cmd", *command[1:]]
    return command


def run_command(
    command: list[str], workdir: Path, env_overrides: dict[str, str] | None = None
) -> tuple[int, str, float]:
    started_at = time.perf_counter()
    env = os.environ.copy()
    if env_overrides:
        env.update(env_overrides)
    proc = subprocess.run(
        _resolve_command(command),
        cwd=workdir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )
    duration_seconds = round(time.perf_counter() - started_at, 3)
    return proc.returncode, proc.stdout.strip(), duration_seconds


def run_proof(scenarios: list[Scenario]) -> dict[str, Any]:
    bootstrap_code, bootstrap_output, bootstrap_duration = run_command(
        BOOTSTRAP_COMMAND, REPO_ROOT
    )
    bootstrap_result = {
        "command": BOOTSTRAP_COMMAND,
        "result": "PASS" if bootstrap_code == 0 else "FAIL",
        "exitCode": bootstrap_code,
        "durationSeconds": bootstrap_duration,
    }

    scenario_events: list[dict[str, Any]] = []
    if bootstrap_code == 0:
        for scenario in scenarios:
            code, output, duration_seconds = run_command(
                scenario.command, scenario.workdir, BOOTSTRAP_SKIP_ENV
            )
            scenario_events.append(
                {
                    "scenarioId": scenario.scenario_id,
                    "title": scenario.title,
                    "commandSha256": _command_digest(scenario.command),
                    "result": "PASS" if code == 0 else "FAIL",
                    "exitCode": code,
                    "durationSeconds": duration_seconds,
                }
            )
    else:
        for scenario in scenarios:
            scenario_events.append(
                {
                    "scenarioId": scenario.scenario_id,
                    "title": scenario.title,
                    "commandSha256": _command_digest(scenario.command),
                    "result": "SKIPPED_BOOTSTRAP_FAILED",
                    "exitCode": None,
                    "durationSeconds": 0.0,
                }
            )

    pass_count = sum(1 for event in scenario_events if event["result"] == "PASS")
    overall_pass = bootstrap_code == 0 and pass_count == len(TARGET_SCENARIO_IDS)

    registry_bytes = SCENARIO_REGISTRY.read_bytes()
    registry_sha256 = hashlib.sha256(registry_bytes).hexdigest()

    return {
        "proofClass": "CURRENT_RUNTIME_INVOCATION",
        "useCaseId": "UC-02-RUNTIME-TO-ENFORCEMENT-CURRENT-RUN",
        "scenarioRegistry": _rel(SCENARIO_REGISTRY),
        "scenarioRegistrySha256": registry_sha256,
        "scenarioDenominator": len(TARGET_SCENARIO_IDS),
        "proofRunInvocationCount": 1,
        "bootstrapResult": bootstrap_result,
        "scenarioEvents": scenario_events,
        "passCount": pass_count,
        "overallResult": "PASS" if overall_pass else "FAIL",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Invoke the canonical CF-076 through CF-084 registry chain once."
    )
    parser.add_argument("--json-output", required=True, help="Path to write the current-run JSON receipt")
    parser.add_argument(
        "--diagnostic-output",
        required=True,
        help="Path to write a secret-safe diagnostic JSON (null on first-run PASS)",
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

    try:
        scenarios = load_target_scenarios()
    except ScenarioSelectionError as exc:
        diagnostic = {
            "stage": "scenario_selection",
            "failureClass": "SELECTION_ERROR",
            "retryable": False,
            "message": str(exc),
        }
        diagnostic_output.write_text(
            json.dumps(diagnostic, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
        )
        print(f"BLOCKED: {exc}")
        return 2

    receipt = run_proof(scenarios)
    json_output.write_text(json.dumps(receipt, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    if receipt["overallResult"] == "PASS":
        diagnostic_output.write_text(json.dumps(None) + "\n", encoding="utf-8")
    else:
        failed = [
            event["scenarioId"]
            for event in receipt["scenarioEvents"]
            if event["result"] != "PASS"
        ]
        diagnostic = {
            "stage": "scenario_execution",
            "failureClass": "SCENARIO_FAILURE"
            if receipt["bootstrapResult"]["result"] == "PASS"
            else "BOOTSTRAP_FAILURE",
            "retryable": True,
            "message": f"failed or skipped scenarios: {failed}",
        }
        diagnostic_output.write_text(
            json.dumps(diagnostic, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
        )

    print(f"Wrote UC-02 current-run receipt: {_rel(json_output)}")
    print(f"Wrote UC-02 diagnostic: {_rel(diagnostic_output)}")
    print(f"Result: {receipt['overallResult']} ({receipt['passCount']}/{receipt['scenarioDenominator']})")
    return 0 if receipt["overallResult"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
