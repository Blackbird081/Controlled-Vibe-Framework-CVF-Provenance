#!/usr/bin/env python3
"""
CVF Agent Autorun Workflow Gate

Runs the phase-specific guard bundle agents must pass before dispatch,
implementation, closure, or push. The wrapper does not replace the underlying
guards; it makes the autorun stop points explicit and repeatable.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class GateCommand:
    name: str
    command: tuple[str, ...]


COMMON_COMMANDS: tuple[GateCommand, ...] = (
    GateCommand(
        "docs governance compatibility",
        (
            "python",
            "governance/compat/check_docs_governance_compat.py",
            "--base",
            "HEAD",
            "--head",
            "HEAD",
            "--enforce",
        ),
    ),
    GateCommand(
        "markdown structural completeness",
        (
            "python",
            "governance/compat/check_markdown_structural_completeness.py",
            "--base",
            "HEAD",
            "--head",
            "HEAD",
            "--enforce",
        ),
    ),
    GateCommand(
        "work-order dispatch quality",
        (
            "python",
            "governance/compat/check_work_order_dispatch_quality.py",
            "--base",
            "HEAD",
            "--head",
            "HEAD",
            "--enforce",
        ),
    ),
    GateCommand(
        "active session state compatibility",
        ("python", "governance/compat/check_active_session_state.py", "--enforce"),
    ),
    GateCommand(
        "governed file size compatibility",
        ("python", "governance/compat/check_governed_file_size.py", "--enforce"),
    ),
)

PRE_PUSH_COMMANDS: tuple[GateCommand, ...] = (
    GateCommand("git remote verification", ("git", "remote", "-v")),
    GateCommand(
        "local pre-push governance hook chain",
        ("python", "governance/compat/run_local_governance_hook_chain.py", "--hook", "pre-push"),
    ),
)


def _run(command: GateCommand) -> int:
    print(f"\n=== {command.name} ===")
    print(" ".join(command.command))
    proc = subprocess.run(
        list(command.command),
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.stdout:
        print(proc.stdout.rstrip())
    if proc.returncode == 0:
        print(f"PASS: {command.name}")
    else:
        print(f"FAIL: {command.name} exited {proc.returncode}")
    return proc.returncode


def _git_status_short() -> str:
    proc = subprocess.run(
        ["git", "status", "--short"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.stdout.strip()


def _run_phase(phase: str) -> int:
    print("=== CVF Agent Autorun Workflow Gate ===")
    print(f"Phase: {phase}")
    print("Policy: docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md")

    failures = 0
    commands: list[GateCommand] = list(COMMON_COMMANDS)
    if phase == "pre-push":
        commands.extend(PRE_PUSH_COMMANDS)

    for command in commands:
        failures += 1 if _run(command) != 0 else 0

    if phase == "pre-closure":
        print("\n=== closure worktree finality ===")
        status = _git_status_short()
        if status:
            print(status)
            print(
                "FAIL: pre-closure cannot claim CLOSED while worktree changes are "
                "uncommitted, untracked, or otherwise unresolved."
            )
            failures += 1
        else:
            print("PASS: worktree is clean for closure claim finality.")

    if failures:
        print(f"\nVIOLATION: {phase} blocked by {failures} failing gate(s).")
        return 1

    print(f"\nCOMPLIANT: {phase} autorun gate passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run CVF agent autorun workflow gate")
    parser.add_argument(
        "--phase",
        choices=("pre-dispatch", "pre-implementation", "pre-closure", "pre-push"),
        required=True,
    )
    args = parser.parse_args()
    return _run_phase(args.phase)


if __name__ == "__main__":
    sys.exit(main())
