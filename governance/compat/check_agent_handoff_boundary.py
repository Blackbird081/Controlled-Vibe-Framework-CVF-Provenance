#!/usr/bin/env python3
"""
CVF Agent Handoff Boundary Gate.

Checks changed governed handoff work orders against the ratified AHB contract.
The guard stays above AOT: AOT validates trace evidence, while this gate
validates the work-order contract fields that tell agents how to hand off work.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    from guard_binding_catalog import has_binding_marker
except ModuleNotFoundError:
    from governance.compat.guard_binding_catalog import has_binding_marker


REPO_ROOT = Path(__file__).resolve().parents[2]
STANDARD_PATH = "docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md"
CONTRACT_PATH = "docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md"
THIS_SCRIPT_PATH = "governance/compat/check_agent_handoff_boundary.py"
AUTORUN_PATH = "governance/compat/run_agent_autorun_workflow_gate.py"
HOOK_CHAIN_PATH = "governance/compat/run_local_governance_hook_chain.py"
DEFAULT_BASE_CANDIDATES = ("origin/main", "origin/master", "main", "master")

WORK_ORDER_PREFIX = "docs/work_orders/"
REVIEW_PREFIX = "docs/reviews/"
ARCHIVE_MARKER = "/archive/"
CONTROL_BLOCK = "Agent Handoff Contract Control Block"
REVIEWER_CONVERSION = "Reviewer Closure Conversion"
ROUTE_TOKENS = {
    "SINGLE_AGENT_SINGLE_ROLE",
    "SINGLE_AGENT_MULTI_ROLE",
    "MULTI_AGENT_SINGLE_ROLE",
    "MULTI_AGENT_MULTI_ROLE",
}
HANDOFF_MARKERS = (
    "Agent Handoff Contract",
    "handoff-boundary",
    "handoff boundary",
    "AHB-T",
    "dispatchBaseHead",
    "executionBaseHead",
    "closureBaseHead",
    "WORKER_MUST_NOT_COMMIT",
    "WORKER_MAY_COMMIT",
    "Intake Role Routing Decision",
)
REQUIRED_BLOCK_FIELDS = (
    "route",
    "rolePattern",
    "phase",
    "baseHeadFor(phase)",
    "changedSetScope(phase)",
    "traceScope(phase, actor)",
    "commitOwner(phase)",
    "crossBatchIsolation",
    "nextMoveSurfaces",
)
BASE_HEAD_FIELDS = ("dispatchBaseHead", "executionBaseHead", "closureBaseHead")
DISPATCH_READY_TOKENS = (
    "Status: DISPATCH_READY",
    "Status: DISPATCHED",
    "Status: READY_FOR_REVIEW",
    "Status: APPROVED_FOR_EXECUTION",
)
CLOSED_TOKENS = ("Status: CLOSED", "Status: CLOSED_PASS", "Status: CLOSED_PASS_BOUNDED")
C3_MARKERS = (
    "three-or-more-agent",
    "three or more agent",
    "N-plus-agent",
    "3-plus-agent",
    "C3",
)
CLEAN_WORKTREE_MARKERS = (
    "clean worktree",
    "worktree clean",
    "git status --short (empty",
    "git status --short` (empty",
)


def _run_git(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def _ref_exists(ref: str) -> bool:
    code, _, _ = _run_git(["rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"])
    return code == 0


def _discover_default_base(head: str) -> tuple[str, str]:
    env_base = os.getenv("CVF_COMPAT_BASE")
    if env_base:
        return env_base, "env:CVF_COMPAT_BASE"
    for ref in DEFAULT_BASE_CANDIDATES:
        if not _ref_exists(ref):
            continue
        code, out, _ = _run_git(["merge-base", ref, head])
        if code == 0 and out:
            return out, f"merge-base({ref},{head})"
    return "HEAD~1", "fallback:HEAD~1"


def _resolve_range(base: str | None, head: str | None) -> tuple[str, str, str]:
    resolved_head = head or "HEAD"
    if base:
        return base, resolved_head, "explicit:--base"
    resolved_base, source = _discover_default_base(resolved_head)
    return resolved_base, resolved_head, source


def _normalize(path: str) -> str:
    return path.replace("\\", "/").strip()


def _parse_name_status(output: str) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    for raw_line in output.splitlines():
        parts = raw_line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0].strip()
        if status.startswith(("R", "C")) and len(parts) > 2:
            path = parts[2]
        else:
            path = parts[1]
        normalized = _normalize(path)
        if normalized:
            changed.setdefault(normalized, set()).add(status)
    return changed


def _get_changed(base: str, head: str) -> dict[str, list[str]]:
    merged: dict[str, set[str]] = {}
    code, out, err = _run_git(["diff", "--name-status", f"{base}..{head}"])
    if code != 0:
        raise RuntimeError(f"git diff failed for range {base}..{head}: {err or out}")
    for path, statuses in _parse_name_status(out).items():
        merged.setdefault(path, set()).update(statuses)
    for args in (["diff", "--name-status"], ["diff", "--name-status", "--cached"]):
        code, out, _ = _run_git(args)
        if code == 0 and out:
            for path, statuses in _parse_name_status(out).items():
                merged.setdefault(path, set()).update(statuses)
    code, out, _ = _run_git(["ls-files", "--others", "--exclude-standard"])
    if code == 0 and out:
        for raw_line in out.splitlines():
            path = _normalize(raw_line)
            if path:
                merged.setdefault(path, set()).add("A")
    return {path: sorted(statuses) for path, statuses in sorted(merged.items())}


def _read_rel(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8", errors="replace")


def _add(violations: list[dict[str, str]], path: str, issue_type: str, message: str) -> None:
    violations.append({"path": path, "type": issue_type, "message": message})


def _is_deleted(statuses: list[str]) -> bool:
    return bool(statuses) and all(status.startswith("D") for status in statuses)


def _is_archive_path(path: str) -> bool:
    return ARCHIVE_MARKER in path.lower()


def _extract_section(text: str, heading_fragment: str) -> str:
    pattern = re.compile(
        rf"^##\s+.*{re.escape(heading_fragment)}.*$([\s\S]*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match.group(1) if match else ""


def _mentions_handoff_contract(text: str) -> bool:
    return any(marker in text for marker in HANDOFF_MARKERS)


def _requires_handoff_control(path: str, text: str) -> bool:
    if not path.startswith(WORK_ORDER_PREFIX) or not path.endswith(".md") or _is_archive_path(path):
        return False
    return _mentions_handoff_contract(text)


def _is_ready_dispatch_work_order(text: str) -> bool:
    return any(token in text for token in DISPATCH_READY_TOKENS) and not any(
        token in text for token in CLOSED_TOKENS
    )


def _route_tokens_in(text: str) -> set[str]:
    return {token for token in ROUTE_TOKENS if re.search(rf"\b{re.escape(token)}\b", text)}


def _selected_commit_mode(text: str) -> str:
    patterns = (
        r"^\s*Commit mode:\s*`?(WORKER_MAY_COMMIT|WORKER_MUST_NOT_COMMIT)`?",
        r"^\s*Execution mode:\s*`?(WORKER_MAY_COMMIT|WORKER_MUST_NOT_COMMIT)`?",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            return match.group(1)
    return ""


def _validate_standard(path: str, text: str) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    required = (
        "Status: ACTIVE_STANDARD_AND_MACHINE_ENFORCED",
        CONTRACT_PATH,
        THIS_SCRIPT_PATH,
        CONTROL_BLOCK,
        "## Machine Enforcement",
    )
    for marker in required:
        if marker not in text:
            _add(violations, path, "standard_marker_missing", f"missing marker `{marker}`")
    return violations


def _validate_binding(path: str, text: str) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    if path == AUTORUN_PATH and not has_binding_marker(path, THIS_SCRIPT_PATH, text):
        _add(violations, path, "autorun_binding_missing", f"autorun gate must run `{THIS_SCRIPT_PATH}`")
    if path == HOOK_CHAIN_PATH and not has_binding_marker(path, THIS_SCRIPT_PATH, text):
        _add(violations, path, "hook_binding_missing", f"local hook chain must run `{THIS_SCRIPT_PATH}`")
    return violations


def _validate_work_order(path: str, text: str) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    if not _requires_handoff_control(path, text):
        return violations

    block = _extract_section(text, CONTROL_BLOCK)
    if not block:
        _add(
            violations,
            path,
            "handoff_contract_control_block_missing",
            f"handoff work orders must include `## {CONTROL_BLOCK}`",
        )
        return violations

    if CONTRACT_PATH not in block and CONTRACT_PATH not in text:
        _add(
            violations,
            path,
            "handoff_contract_source_missing",
            f"control block must cite `{CONTRACT_PATH}`",
        )

    routes = _route_tokens_in(block)
    if len(routes) != 1:
        _add(
            violations,
            path,
            "handoff_route_not_singleton",
            "control block must select exactly one canonical route token",
        )

    lowered_block = block.lower()
    for field in REQUIRED_BLOCK_FIELDS:
        if field.lower() not in lowered_block:
            _add(
                violations,
                path,
                "handoff_contract_field_missing",
                f"control block missing `{field}`",
            )

    for field in BASE_HEAD_FIELDS:
        if field not in text:
            _add(
                violations,
                path,
                "handoff_base_head_missing",
                f"work order must state `{field}`",
            )

    if _selected_commit_mode(text) == "WORKER_MUST_NOT_COMMIT":
        conversion = _extract_section(text, REVIEWER_CONVERSION)
        if not conversion:
            _add(
                violations,
                path,
                "reviewer_closure_conversion_missing",
                "WORKER_MUST_NOT_COMMIT work orders must include Reviewer Closure Conversion",
            )
        for marker in ("completionReviewPath", "reviewerOwnedClosurePaths"):
            if marker not in conversion:
                _add(
                    violations,
                    path,
                    "reviewer_closure_conversion_field_missing",
                    f"Reviewer Closure Conversion missing `{marker}`",
                )

    if any(marker in text for marker in C3_MARKERS):
        if not re.search(r"\b(closerOwner|designated closer|closer identity|Closer)\b", block, re.IGNORECASE):
            _add(
                violations,
                path,
                "c3_closer_not_designated",
                "C3 or N-plus-agent work orders must designate the closer in the contract block",
            )

    if _is_ready_dispatch_work_order(text):
        trace_block = _extract_section(text, "Agent Operation Trace Block")
        if not any(marker in trace_block.lower() for marker in CLEAN_WORKTREE_MARKERS):
            _add(
                violations,
                path,
                "cross_batch_isolation_clean_worktree_missing",
                "dispatch-ready handoff work orders must record clean worktree Before status evidence",
            )

    return violations


def _validate_completion(path: str, text: str) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    if not path.startswith(REVIEW_PREFIX) or not path.endswith(".md") or _is_archive_path(path):
        return violations
    if "AHB-T3" not in text and "handoff-boundary" not in text:
        return violations
    if "Status: CLOSED_PASS_BOUNDED" not in text:
        return violations
    required = (
        "Agent Handoff Boundary Checker Evidence",
        THIS_SCRIPT_PATH,
        "CF-01",
        "CF-09",
    )
    for marker in required:
        if marker not in text:
            _add(violations, path, "handoff_completion_evidence_missing", f"missing marker `{marker}`")
    return violations


def _validate_path(path: str, statuses: list[str]) -> list[dict[str, str]]:
    if _is_deleted(statuses):
        return []
    full = REPO_ROOT / path
    if not full.exists():
        return []
    text = _read_rel(path)
    violations: list[dict[str, str]] = []
    if path == STANDARD_PATH:
        violations.extend(_validate_standard(path, text))
    if path in {AUTORUN_PATH, HOOK_CHAIN_PATH}:
        violations.extend(_validate_binding(path, text))
    violations.extend(_validate_work_order(path, text))
    violations.extend(_validate_completion(path, text))
    return violations


def _validate_changed(changed_paths: dict[str, list[str]]) -> list[dict[str, str]]:
    paths = set(changed_paths)
    for path in (STANDARD_PATH, AUTORUN_PATH, HOOK_CHAIN_PATH):
        if (REPO_ROOT / path).exists():
            paths.add(path)
    violations: list[dict[str, str]] = []
    for path in sorted(paths):
        statuses = changed_paths.get(path, [])
        violations.extend(_validate_path(path, statuses))
    return violations


def _build_report(base: str | None, head: str | None) -> dict[str, Any]:
    resolved_base, resolved_head, base_source = _resolve_range(base, head)
    changed_paths = _get_changed(resolved_base, resolved_head)
    violations = _validate_changed(changed_paths)
    return {
        "base": resolved_base,
        "head": resolved_head,
        "baseSource": base_source,
        "changedPaths": changed_paths,
        "violations": violations,
        "compliant": not violations,
    }


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    parser = argparse.ArgumentParser(description="Enforce CVF agent handoff boundary contract")
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--enforce", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = _build_report(args.base, args.head)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print("=== CVF Agent Handoff Boundary Gate ===")
        print(f"Standard: {STANDARD_PATH}")
        print(f"Base: {report['base']} ({report['baseSource']})")
        print(f"Head: {report['head']}")
        print(f"Changed paths checked: {len(report['changedPaths'])}")
        if report["violations"]:
            print("\nViolations:")
            for issue in report["violations"]:
                print(f"- {issue['path']}: {issue['type']} - {issue['message']}")
            print("\nVIOLATION - repair agent handoff boundary contract evidence before proceeding.")
        else:
            print("\nCOMPLIANT - agent handoff boundary gate is satisfied.")
    return 1 if args.enforce and report["violations"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
