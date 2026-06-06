#!/usr/bin/env python3
"""Conservative helper for CVF governed tranche commits.

The helper intentionally commits only files that are already staged. It does
not stage arbitrary worktree changes, does not push, and does not bypass hooks.
After the staged artifact commit, it can create a dedicated active-handoff sync
commit so the final continuity marker is not mixed into the artifact batch.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ACTIVE_STATE = REPO_ROOT / "CVF_SESSION" / "ACTIVE_SESSION_STATE.json"
HEAD_LINE_RE = re.compile(r"^Current HEAD recorded for this handoff: `[^`]+`.*$", re.MULTILINE)


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def _run(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=check,
    )


def _git(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return _run(["git", *args], check=check)


def _lines(output: str) -> list[str]:
    return [line.strip() for line in output.splitlines() if line.strip()]


def _staged_files() -> list[str]:
    return _lines(_git(["diff", "--cached", "--name-only"]).stdout)


def _unstaged_files() -> list[str]:
    modified = _lines(_git(["diff", "--name-only"]).stdout)
    untracked = _lines(_git(["ls-files", "--others", "--exclude-standard"]).stdout)
    return sorted(set(modified + untracked))


def _short_head() -> str:
    return _git(["rev-parse", "--short", "HEAD"]).stdout.strip()


def _subject(ref: str = "HEAD") -> str:
    return _git(["log", "-1", "--pretty=%s", ref]).stdout.strip()


def _active_handoff_path() -> Path:
    state = json.loads(ACTIVE_STATE.read_text(encoding="utf-8"))
    handoff = state.get("activeHandoff")
    if not isinstance(handoff, str) or not handoff.strip():
        raise SystemExit("ACTIVE_SESSION_STATE.json does not contain activeHandoff")
    path = REPO_ROOT / handoff
    if not path.exists():
        raise SystemExit(f"Active handoff not found: {handoff}")
    return path


def _ensure_clean_for_staged_commit(allow_unstaged: bool) -> None:
    staged = _staged_files()
    if not staged:
        raise SystemExit("No staged files found. Stage the intended artifact batch first.")

    unstaged = _unstaged_files()
    if unstaged and not allow_unstaged:
        rendered = "\n".join(f"  - {path}" for path in unstaged)
        raise SystemExit(
            "Unstaged or untracked files are present. Stage or clear them before using "
            "the helper, or pass --allow-unstaged for inspection-only residuals.\n"
            f"{rendered}"
        )


def _replace_handoff_head(handoff_path: Path, head: str, summary: str) -> None:
    text = handoff_path.read_text(encoding="utf-8")
    date = datetime.now().strftime("%Y-%m-%d")
    subject = _subject(head)
    summary = " ".join(summary.split())
    replacement = (
        f"Current HEAD recorded for this handoff: `{head}` ({subject}). "
        f"Updated {date} after {summary}."
    )
    if HEAD_LINE_RE.search(text):
        updated = HEAD_LINE_RE.sub(replacement, text, count=1)
    else:
        updated = f"{replacement}\n\n{text}"
    handoff_path.write_text(updated, encoding="utf-8", newline="\n")


def _commit_staged(message: str) -> str:
    _git(["commit", "-m", message])
    return _short_head()


def _run_preclosure(base: str) -> None:
    _run(
        [
            sys.executable,
            "governance/compat/run_agent_autorun_workflow_gate.py",
            "--phase",
            "pre-closure",
            "--base",
            base,
            "--head",
            "HEAD",
        ]
    )


def _print_plan(args: argparse.Namespace) -> None:
    staged = _staged_files()
    unstaged = _unstaged_files()
    handoff = _active_handoff_path().relative_to(REPO_ROOT)
    print("CVF governed tranche commit helper plan")
    print(f"Current HEAD: {_short_head()}")
    print(f"Active handoff: {handoff}")
    print(f"Staged files: {len(staged)}")
    for path in staged:
        print(f"  + {path}")
    print(f"Unstaged/untracked files: {len(unstaged)}")
    for path in unstaged:
        print(f"  ! {path}")
    print("Execution mode:", "execute" if args.execute else "dry-run")


def main() -> int:
    _configure_stdout()
    parser = argparse.ArgumentParser(
        description="Commit an already-staged CVF artifact batch and create a dedicated handoff sync commit."
    )
    parser.add_argument("--base", required=True, help="Closure base head for final pre-closure gate.")
    parser.add_argument("--message", required=True, help="Commit message for the already-staged artifact batch.")
    parser.add_argument(
        "--handoff-message",
        default="docs(session): sync governed tranche handoff",
        help="Commit message for the dedicated handoff-only sync commit.",
    )
    parser.add_argument(
        "--handoff-summary",
        required=True,
        help="Short summary written into the active handoff HEAD marker.",
    )
    parser.add_argument(
        "--allow-unstaged",
        action="store_true",
        help="Allow unrelated unstaged files to remain present while committing only staged files.",
    )
    parser.add_argument("--skip-preclosure", action="store_true", help="Skip the final pre-closure autorun gate.")
    parser.add_argument("--execute", action="store_true", help="Perform commits. Without this flag, print a dry-run plan.")
    args = parser.parse_args()

    _print_plan(args)
    _ensure_clean_for_staged_commit(args.allow_unstaged)

    if not args.execute:
        print("Dry-run complete. Re-run with --execute to commit.")
        return 0

    artifact_head = _commit_staged(args.message)
    print(f"Artifact commit created: {artifact_head}")

    handoff_path = _active_handoff_path()
    _replace_handoff_head(handoff_path, artifact_head, args.handoff_summary)
    _git(["add", str(handoff_path.relative_to(REPO_ROOT)).replace("\\", "/")])

    staged_after_handoff = _staged_files()
    expected = str(handoff_path.relative_to(REPO_ROOT)).replace("\\", "/")
    if staged_after_handoff != [expected]:
        rendered = "\n".join(f"  - {path}" for path in staged_after_handoff)
        raise SystemExit(
            "Refusing handoff sync commit because staged files are not handoff-only:\n"
            f"{rendered}"
        )

    handoff_head = _commit_staged(args.handoff_message)
    print(f"Handoff sync commit created: {handoff_head}")

    if not args.skip_preclosure:
        _run_preclosure(args.base)
        print("Pre-closure autorun gate: PASS")

    status = _git(["status", "--short"]).stdout.strip()
    if status:
        print("Remaining worktree changes:")
        print(status)
    else:
        print("Working tree clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
