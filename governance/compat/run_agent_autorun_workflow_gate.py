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


RANGE_GATE_NAMES = (
    "docs governance compatibility",
    "markdown structural completeness",
    "work-order dispatch quality",
)


def _range_command(name: str, script: str, base: str, head: str) -> GateCommand:
    return GateCommand(
        name,
        (
            "python",
            script,
            "--base",
            base,
            "--head",
            head,
            "--enforce",
        ),
    )


def _common_commands(base: str, head: str) -> tuple[GateCommand, ...]:
    return (
        _range_command(
            "docs governance compatibility",
            "governance/compat/check_docs_governance_compat.py",
            base,
            head,
        ),
        _range_command(
            "markdown structural completeness",
            "governance/compat/check_markdown_structural_completeness.py",
            base,
            head,
        ),
        _range_command(
            "work-order dispatch quality",
            "governance/compat/check_work_order_dispatch_quality.py",
            base,
            head,
        ),
        _range_command(
            "multi-provider execution log quality",
            "governance/compat/check_multi_provider_execution_log.py",
            base,
            head,
        ),
        _range_command(
            "finding-to-governance learning quality",
            "governance/compat/check_finding_to_governance_learning.py",
            base,
            head,
        ),
        _range_command(
            "public export disposition quality",
            "governance/compat/check_public_export_disposition.py",
            base,
            head,
        ),
        _range_command(
            "corpus completeness and report integrity",
            "governance/compat/check_corpus_completeness_report_integrity.py",
            base,
            head,
        ),
        _range_command(
            "corpus-to-knowledge-map reconciliation",
            "governance/compat/check_corpus_to_knowledge_map_reconciliation.py",
            base,
            head,
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


def _git_rev_parse(ref: str) -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "--short", ref],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout.strip() or f"failed to resolve {ref}")
    return proc.stdout.strip()


def _git_diff_name_status(base: str, head: str) -> str:
    proc = subprocess.run(
        ["git", "diff", "--name-status", f"{base}..{head}"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        return proc.stdout.strip()
    return proc.stdout.strip()


def _default_base_for_phase(phase: str) -> str:
    if phase in {"pre-closure", "pre-push"}:
        return "HEAD~1"
    return "HEAD"


def _run_phase(phase: str, base: str | None, head: str) -> int:
    resolved_base = base or _default_base_for_phase(phase)
    print("=== CVF Agent Autorun Workflow Gate ===")
    print(f"Phase: {phase}")
    print("Policy: docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md")
    print(f"Range: {resolved_base}..{head}")

    try:
        base_sha = _git_rev_parse(resolved_base)
        head_sha = _git_rev_parse(head)
    except RuntimeError as exc:
        print(f"FAIL: could not resolve autorun gate range: {exc}")
        return 1
    print(f"Base HEAD anchor: {base_sha}")
    print(f"Head anchor: {head_sha}")

    failures = 0
    commands: list[GateCommand] = list(_common_commands(resolved_base, head))
    if phase == "pre-push":
        commands.extend(PRE_PUSH_COMMANDS)

    if phase in {"pre-closure", "pre-push"} and base_sha == head_sha:
        print(
            "FAIL: closure/push autorun gates require a non-empty committed "
            "range. Pass --base <baseHead> --head HEAD or run after a commit "
            "with default HEAD~1..HEAD."
        )
        failures += 1
    elif phase in {"pre-closure", "pre-push"}:
        changed = _git_diff_name_status(resolved_base, head)
        print("\n=== committed range evidence ===")
        print(changed if changed else "No committed files changed in range.")
        if not changed:
            print("FAIL: closure/push range has no committed diff evidence.")
            failures += 1

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
    parser.add_argument(
        "--base",
        default=None,
        help="Base commit/ref for range-aware gates. Defaults to HEAD for pre-dispatch/pre-implementation and HEAD~1 for pre-closure/pre-push.",
    )
    parser.add_argument("--head", default="HEAD", help="Head commit/ref for range-aware gates.")
    args = parser.parse_args()
    return _run_phase(args.phase, args.base, args.head)


if __name__ == "__main__":
    sys.exit(main())
