#!/usr/bin/env python3
"""
CVF Agent Operation Trace and Workspace Integrity Gate.

This guard keeps CVF focused on control-plane evidence: it requires changed
agent execution artifacts to leave a repo-local operation trace, and it flags
protected-path deletions or renames unless the changed packet records explicit
deletion/rename disposition evidence.

It does not claim OS-level user attribution, endpoint monitoring, or physical
machine identity.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
STANDARD_PATH = "docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md"
TRACE_MARKER = "## Agent Operation Trace Block"
DELETE_RENAME_LABEL = "Deletion or rename disposition"

TRACE_REQUIRED_LABELS = (
    "Actor",
    "Provider or surface",
    "Session or invocation",
    "Working directory",
    "Command or tool surface",
    "Target paths",
    "Allowed scope source",
    "Before status evidence",
    "After status evidence",
    "Diff evidence",
    "Approval boundary",
    "Claim boundary",
)

TRACE_ARTIFACT_PREFIXES = (
    "docs/work_orders/",
    "docs/reviews/",
)

TRACE_REVIEW_TRIGGERS = (
    "WORKER_RETURN",
    "WORKER_MUST_NOT_COMMIT",
    "WORKER_MAY_COMMIT",
    "completion_review",
    "Owner / reviewer",
    "Worker:",
    "Machine Closure Package",
    "Closure Diff Gate",
)

PROTECTED_REPO_PREFIXES = (
    ".github/",
    "AGENTS.md",
    "CVF_SESSION/",
    "CVF_SESSION_MEMORY.md",
    "docs/baselines/",
    "docs/reference/",
    "docs/reviews/",
    "docs/roadmaps/",
    "docs/work_orders/",
    "governance/compat/",
)


def _normalize(path: str) -> str:
    return path.replace("\\", "/").strip()


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


def _parse_name_status(output: str) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    for raw in output.splitlines():
        parts = raw.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0].strip()
        if status.startswith(("R", "C")) and len(parts) > 2:
            old_path = _normalize(parts[1])
            new_path = _normalize(parts[2])
            changed.setdefault(old_path, set()).add(status)
            changed.setdefault(new_path, set()).add(status)
        else:
            path = _normalize(parts[1])
            if path:
                changed.setdefault(path, set()).add(status)
    return changed


def _merge_changed(target: dict[str, set[str]], source: dict[str, set[str]]) -> None:
    for path, statuses in source.items():
        target.setdefault(path, set()).update(statuses)


def get_changed_paths(base: str | None, head: str | None) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    if base and head and base != head:
        code, out, err = _run_git(["diff", "--name-status", f"{base}..{head}"])
        if code != 0:
            raise RuntimeError(err or out or f"git diff failed for {base}..{head}")
        _merge_changed(changed, _parse_name_status(out))

    for args in (["diff", "--name-status"], ["diff", "--name-status", "--cached"]):
        code, out, _ = _run_git(args)
        if code == 0 and out:
            _merge_changed(changed, _parse_name_status(out))

    code, out, _ = _run_git(["ls-files", "--others", "--exclude-standard"])
    if code == 0 and out:
        for raw in out.splitlines():
            path = _normalize(raw)
            if path:
                changed.setdefault(path, set()).add("A")

    return changed


def is_trace_artifact(path: str, text: str) -> bool:
    normalized = _normalize(path)
    if "/archive/" in normalized or not normalized.endswith(".md"):
        return False
    if not normalized.startswith(TRACE_ARTIFACT_PREFIXES):
        return False
    if normalized.startswith("docs/work_orders/"):
        return True
    return any(trigger in text for trigger in TRACE_REVIEW_TRIGGERS)


def missing_trace_labels(text: str) -> list[str]:
    if TRACE_MARKER not in text:
        return list(TRACE_REQUIRED_LABELS)
    lower_text = text.lower()
    return [label for label in TRACE_REQUIRED_LABELS if label.lower() not in lower_text]


def _is_protected_path(path: str) -> bool:
    normalized = _normalize(path)
    return any(
        normalized == prefix.rstrip("/") or normalized.startswith(prefix)
        for prefix in PROTECTED_REPO_PREFIXES
    )


def protected_delete_or_rename_paths(changed: dict[str, set[str]]) -> list[str]:
    flagged: list[str] = []
    for path, statuses in sorted(changed.items()):
        if not _is_protected_path(path):
            continue
        if any(status.startswith(("D", "R")) for status in statuses):
            flagged.append(path)
    return flagged


def find_trace_violations(
    changed: dict[str, set[str]],
    file_texts: dict[str, str],
) -> list[str]:
    violations: list[str] = []
    changed_trace_blocks: list[str] = []

    for path, statuses in sorted(changed.items()):
        if not any(status.startswith(("A", "M", "R")) for status in statuses):
            continue
        text = file_texts.get(path, "")
        if TRACE_MARKER in text:
            changed_trace_blocks.append(path)
        if not is_trace_artifact(path, text):
            continue
        missing = missing_trace_labels(text)
        if missing:
            violations.append(
                f"{path}: missing or incomplete {TRACE_MARKER}; missing labels: "
                + ", ".join(missing)
            )

    protected_changes = protected_delete_or_rename_paths(changed)
    if protected_changes:
        has_delete_disposition = any(
            DELETE_RENAME_LABEL.lower() in file_texts.get(path, "").lower()
            for path in changed_trace_blocks
        )
        if not has_delete_disposition:
            violations.append(
                "protected delete/rename detected without Agent Operation Trace "
                f"`{DELETE_RENAME_LABEL}` evidence: " + ", ".join(protected_changes)
            )

    return violations


def _read_changed_texts(changed: dict[str, set[str]]) -> dict[str, str]:
    texts: dict[str, str] = {}
    for path in changed:
        full_path = REPO_ROOT / path
        if not full_path.is_file():
            texts[path] = ""
            continue
        try:
            texts[path] = full_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            texts[path] = ""
    return texts


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check changed agent execution artifacts leave an operation trace"
    )
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--enforce", action="store_true")
    args = parser.parse_args()

    print("=== CVF Agent Operation Trace And Workspace Integrity Gate ===")
    print(f"Standard: {STANDARD_PATH}")
    if args.base:
        print(f"Range: {args.base}..{args.head}")

    try:
        changed = get_changed_paths(args.base, args.head)
        texts = _read_changed_texts(changed)
        violations = find_trace_violations(changed, texts)
    except Exception as exc:  # noqa: BLE001 - CLI guard should print safe failure
        print(f"FAIL: {exc}")
        return 2 if args.enforce else 0

    trace_artifacts = [
        path
        for path, text in texts.items()
        if is_trace_artifact(path, text)
        and any(status.startswith(("A", "M", "R")) for status in changed.get(path, set()))
    ]
    protected_changes = protected_delete_or_rename_paths(changed)

    print(f"Changed paths observed: {len(changed)}")
    print(f"Trace artifacts checked: {len(trace_artifacts)}")
    print(f"Protected delete/rename paths observed: {len(protected_changes)}")
    print(f"Violations: {len(violations)}")

    if violations:
        print("\nViolations:")
        for violation in violations:
            print(f"  - {violation}")
        print(
            "\nAction: add a complete Agent Operation Trace Block or restore/justify "
            "the protected delete/rename in the trace disposition."
        )
        return 1 if args.enforce else 0

    print("\nCOMPLIANT - agent operation trace and repo-local workspace integrity evidence are aligned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
