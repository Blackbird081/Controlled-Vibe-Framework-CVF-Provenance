#!/usr/bin/env python3
"""
CVF Agent Packet Authority And Encoding Gate

Blocks two recurring no-commit worker packet defects early:
- reviewer packets that cite missing authority artifacts;
- newly added agent-authored non-ASCII text without a local exception note.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
THIS_SCRIPT = "governance/compat/check_agent_packet_authority_and_encoding.py"
STANDARD_PATH = "docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md"

AUTHORITY_REFERENCE_RE = re.compile(
    r"(docs/(?:baselines|roadmaps|work_orders|reviews)/[A-Za-z0-9_./ -]+?\.md)"
)
ACTIVE_REVIEW_PREFIXES = ("docs/reviews/",)
ENCODING_EXTENSIONS = {".md", ".py", ".ts", ".tsx", ".js", ".jsx", ".json"}
ENCODING_PATH_PREFIXES = (
    "docs/",
    "governance/",
    "EXTENSIONS/",
    "CVF_SESSION/",
    "scripts/",
)
ENCODING_EXACT_PATHS = {
    "AGENTS.md",
    "CLAUDE.md",
    "CVF_SESSION_MEMORY.md",
    "DESIGN.md",
}
EXCEPTION_MARKERS = (
    "Text Encoding Exception",
    "Unicode exception",
    "Non-ASCII exception",
)
PROVIDER_SPECIFIC_AUTHORITY_FILES = (
    "CLAUDE.md",
    "MEMORY.md",
    ".codex/memories",
    ".claude",
)
PROVIDER_SPECIFIC_AUTHORITY_CONTEXTS = (
    "Source Authority",
    "Source Verification",
    "source evidence",
    "Primary source evidence",
    "Source File Manifest",
    "Terminal status",
    "Evidence / repair",
    "Machine-readable evidence",
)
PROVIDER_SPECIFIC_AUTHORITY_ALLOW_MARKERS = (
    "NOT_CVF_SOURCE",
    "NOT_SOURCE_AUTHORITY",
    "provider-specific",
    "not CVF source",
    "not source of truth",
)


@dataclass(frozen=True)
class AddedLine:
    line_number: int
    text: str


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
    return proc.returncode, proc.stdout, proc.stderr


def _parse_name_status(output: str) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    for raw in output.splitlines():
        parts = raw.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0].strip()
        path = parts[2] if status.startswith(("R", "C")) and len(parts) > 2 else parts[1]
        normalized = path.replace("\\", "/").strip()
        if normalized:
            changed.setdefault(normalized, set()).add(status)
    return changed


def _merge_status(target: dict[str, set[str]], source: dict[str, set[str]]) -> None:
    for path, statuses in source.items():
        target.setdefault(path, set()).update(statuses)


def _get_changed(base: str | None, head: str | None) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    if base and head:
        code, out, err = _run_git(["diff", "--name-status", f"{base}..{head}"])
        if code != 0:
            raise RuntimeError(f"git diff failed for range {base}..{head}: {err or out}")
        _merge_status(changed, _parse_name_status(out))

    for args in (["diff", "--name-status"], ["diff", "--name-status", "--cached"]):
        code, out, _ = _run_git(args)
        if code == 0 and out:
            _merge_status(changed, _parse_name_status(out))

    code, out, _ = _run_git(["ls-files", "--others", "--exclude-standard"])
    if code == 0 and out:
        for raw in out.splitlines():
            path = raw.replace("\\", "/").strip()
            if path:
                changed.setdefault(path, set()).add("A")
    return changed


def _read_rel(path: str) -> str:
    full = REPO_ROOT / path
    if not full.exists() or full.is_dir():
        return ""
    return full.read_text(encoding="utf-8", errors="replace")


def _is_review_packet(path: str) -> bool:
    normalized = path.replace("\\", "/")
    return normalized.endswith(".md") and any(
        normalized.startswith(prefix) for prefix in ACTIVE_REVIEW_PREFIXES
    )


def _is_encoding_scoped(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if normalized in ENCODING_EXACT_PATHS:
        return True
    if Path(normalized).suffix not in ENCODING_EXTENSIONS:
        return False
    return any(normalized.startswith(prefix) for prefix in ENCODING_PATH_PREFIXES)


def _path_exists(path: str) -> bool:
    return (REPO_ROOT / path).exists()


def find_authority_reference_violations(path: str, text: str) -> list[str]:
    if not _is_review_packet(path):
        return []
    missing: list[str] = []
    for match in AUTHORITY_REFERENCE_RE.finditer(text):
        referenced = match.group(1).replace("\\", "/").rstrip(".,;:)")
        if referenced and not _path_exists(referenced):
            missing.append(referenced)
    if not missing:
        return []
    return [
        "review packet cites missing authority artifact(s): "
        + ", ".join(sorted(set(missing)))
    ]


def find_provider_specific_authority_violations(path: str, text: str) -> list[str]:
    normalized = path.replace("\\", "/")
    if not normalized.endswith(".md"):
        return []
    issues: list[str] = []
    active_context = False
    for line_number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("#"):
            active_context = any(
                marker.lower() in stripped.lower()
                for marker in PROVIDER_SPECIFIC_AUTHORITY_CONTEXTS
            )
            continue
        line_lower = raw.lower()
        has_provider_file = False
        for provider_file in PROVIDER_SPECIFIC_AUTHORITY_FILES:
            pattern = re.escape(provider_file.lower())
            if provider_file in {"CLAUDE.md", "MEMORY.md"}:
                pattern = rf"(?<![A-Za-z0-9_./-]){pattern}(?![A-Za-z0-9_./-])"
            if re.search(pattern, line_lower):
                has_provider_file = True
                break
        if not has_provider_file:
            continue
        if any(marker.lower() in line_lower for marker in PROVIDER_SPECIFIC_AUTHORITY_ALLOW_MARKERS):
            continue
        line_context = active_context or any(
            marker.lower() in line_lower
            for marker in PROVIDER_SPECIFIC_AUTHORITY_CONTEXTS
        )
        if line_context or "|" in raw:
            issues.append(
                f"line {line_number}: provider-specific agent memory/guidance "
                "file is cited as authority; use CVF-governed source or mark NOT_CVF_SOURCE"
            )
    return issues


def _has_encoding_exception(text: str) -> bool:
    return any(marker in text for marker in EXCEPTION_MARKERS)


def find_non_ascii_line_violations(
    path: str,
    added_lines: list[AddedLine],
    *,
    has_exception: bool,
) -> list[str]:
    if not _is_encoding_scoped(path) or has_exception:
        return []
    issues: list[str] = []
    for line in added_lines:
        if any(ord(char) > 127 for char in line.text):
            issues.append(
                f"line {line.line_number}: newly added non-ASCII text without "
                "Text Encoding Exception"
            )
    return issues


def _all_file_lines(path: str) -> list[AddedLine]:
    text = _read_rel(path)
    return [AddedLine(index, line) for index, line in enumerate(text.splitlines(), start=1)]


def _parse_added_lines_from_diff(diff_text: str) -> list[AddedLine]:
    added: list[AddedLine] = []
    next_line: int | None = None
    for raw in diff_text.splitlines():
        if raw.startswith("@@"):
            match = re.search(r"\+(\d+)(?:,(\d+))?", raw)
            next_line = int(match.group(1)) if match else None
            continue
        if next_line is None:
            continue
        if raw.startswith("+++") or raw.startswith("---"):
            continue
        if raw.startswith("+"):
            added.append(AddedLine(next_line, raw[1:]))
            next_line += 1
        elif raw.startswith("-"):
            continue
        else:
            next_line += 1
    return added


def _added_lines_from_git_diff(args: list[str]) -> list[AddedLine]:
    code, out, _ = _run_git(args)
    if code != 0 or not out:
        return []
    return _parse_added_lines_from_diff(out)


def _added_lines(path: str, statuses: set[str], base: str | None, head: str | None) -> list[AddedLine]:
    if statuses == {"D"}:
        return []
    if statuses == {"A"} and not (base and head):
        return _all_file_lines(path)

    lines: list[AddedLine] = []
    if base and head:
        if any(status.startswith("A") for status in statuses):
            lines.extend(_all_file_lines(path))
        else:
            lines.extend(
                _added_lines_from_git_diff(
                    ["diff", "--unified=0", "--no-ext-diff", f"{base}..{head}", "--", path]
                )
            )

    for diff_args in (
        ["diff", "--unified=0", "--no-ext-diff", "--", path],
        ["diff", "--cached", "--unified=0", "--no-ext-diff", "--", path],
    ):
        lines.extend(_added_lines_from_git_diff(diff_args))

    if not lines and any(status.startswith("A") for status in statuses):
        lines.extend(_all_file_lines(path))
    return lines


def _run_check(base: str | None, head: str | None) -> dict[str, Any]:
    changed = _get_changed(base, head)
    violations: list[dict[str, Any]] = []

    for path, statuses in sorted(changed.items()):
        text = _read_rel(path)
        path_issues: list[str] = []
        if text:
            path_issues.extend(find_authority_reference_violations(path, text))
            path_issues.extend(find_provider_specific_authority_violations(path, text))
            path_issues.extend(
                find_non_ascii_line_violations(
                    path,
                    _added_lines(path, statuses, base, head),
                    has_exception=_has_encoding_exception(text),
                )
            )
        if path_issues:
            violations.append({"path": path, "issues": path_issues})

    return {
        "policy": STANDARD_PATH,
        "script": THIS_SCRIPT,
        "changedFileCount": len(changed),
        "violationCount": len(violations),
        "violations": violations,
        "compliant": not violations,
    }


def _print_report(report: dict[str, Any], base: str | None, head: str | None) -> None:
    print("=== CVF Agent Packet Authority And Encoding Gate ===")
    if base or head:
        print(f"Range: {base or '<worktree>'}..{head or '<worktree>'}")
    print(f"Policy: {report['policy']}")
    print(f"Changed files: {report['changedFileCount']}")
    print(f"Violations: {report['violationCount']}")
    if report["violations"]:
        print("\nViolations:")
        for violation in report["violations"]:
            print(f"  - {violation['path']}")
            for issue in violation["issues"]:
                print(f"    - {issue}")
    if report["compliant"]:
        print("\nCOMPLIANT - authority references exist and added agent text is ASCII-disciplined.")
    else:
        print("\nVIOLATION - repair missing authority artifacts or record a bounded encoding exception.")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(errors="replace")

    parser = argparse.ArgumentParser(description="Run CVF agent packet authority and encoding gate")
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default=None)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--enforce", action="store_true")
    args = parser.parse_args()

    try:
        report = _run_check(args.base, args.head)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        _print_report(report, args.base, args.head)
    return 1 if args.enforce and not report["compliant"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
