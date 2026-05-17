#!/usr/bin/env python3
"""
CVF Active Session State Compatibility Gate

Ensures the session-memory front door stays usable by agents and future
cvf-cli/cvf-mcp-server entrypoints:
- root front door exists
- machine-readable active session state exists and points to existing files
- exactly one root handoff declares Status: ACTIVE
- AGENTS.md and CLAUDE.md route agents through the front door
- local governance hook chain runs this gate
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]

FRONT_DOOR_PATH = "CVF_SESSION_MEMORY.md"
STATE_PATH = "CVF_SESSION/ACTIVE_SESSION_STATE.json"
READ_FIRST_PATH = "CVF_SESSION/READ_FIRST.md"
STARTUP_GUARDS_PATH = "CVF_SESSION/REQUIRED_STARTUP_GUARDS.md"
AGENTS_PATH = "AGENTS.md"
CLAUDE_PATH = "CLAUDE.md"
HOOK_CHAIN_PATH = "governance/compat/run_local_governance_hook_chain.py"
THIS_SCRIPT_PATH = "governance/compat/check_active_session_state.py"

REQUIRED_STATIC_FILES = (
    FRONT_DOOR_PATH,
    STATE_PATH,
    READ_FIRST_PATH,
    STARTUP_GUARDS_PATH,
    AGENTS_PATH,
    CLAUDE_PATH,
    HOOK_CHAIN_PATH,
)

FRONT_DOOR_MARKERS = (
    "ACTIVE SESSION FRONT DOOR",
    STATE_PATH,
)

AGENT_ROUTER_MARKERS = (
    FRONT_DOOR_PATH,
    STATE_PATH,
)


def _read_text(path: str) -> str:
    abs_path = REPO_ROOT / path
    if not abs_path.exists() or abs_path.is_dir():
        return ""
    return abs_path.read_text(encoding="utf-8")


def _load_state() -> tuple[dict[str, Any] | None, str | None]:
    state_path = REPO_ROOT / STATE_PATH
    if not state_path.exists():
        return None, "state file is missing"
    try:
        return json.loads(state_path.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON: {exc}"


def _git_head_sha() -> str | None:
    """Return the current HEAD SHA (full 40-char), or None if git is unavailable."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _root_handoff_paths() -> list[Path]:
    return sorted(REPO_ROOT.glob("AGENT_HANDOFF*.md"))


def _active_handoffs() -> list[str]:
    active: list[str] = []
    for path in _root_handoff_paths():
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines()[:40]:
            if line.strip().startswith("Status: ACTIVE"):
                active.append(path.name)
                break
    return active


def _as_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def _classify() -> dict[str, Any]:
    missing_files = [path for path in REQUIRED_STATIC_FILES if not (REPO_ROOT / path).exists()]

    state, state_error = _load_state()
    state_violations: list[str] = []
    active_handoff = None
    current_mode = None
    freeze_posture = None
    required_first_reads: list[str] = []
    required_startup_guards: list[str] = []

    if state_error:
        state_violations.append(state_error)
    elif state is not None:
        if state.get("activeSessionFrontDoor") != FRONT_DOOR_PATH:
            state_violations.append("activeSessionFrontDoor must point to CVF_SESSION_MEMORY.md")
        if state.get("activeStateRegistry") != STATE_PATH:
            state_violations.append("activeStateRegistry must point to CVF_SESSION/ACTIVE_SESSION_STATE.json")
        active_handoff = state.get("activeHandoff")
        if not isinstance(active_handoff, str) or not active_handoff:
            state_violations.append("activeHandoff must be a non-empty string")
        elif not (REPO_ROOT / active_handoff).exists():
            state_violations.append(f"activeHandoff does not exist: {active_handoff}")
        current_mode = state.get("currentMode")
        if not isinstance(current_mode, str) or not current_mode:
            state_violations.append("currentMode must be a non-empty string")
        freeze_posture = state.get("freezePosture")
        if not isinstance(freeze_posture, str) or not freeze_posture:
            state_violations.append("freezePosture must be a non-empty string")

        required_first_reads = _as_list(state.get("requiredFirstReads"))
        if not required_first_reads:
            state_violations.append("requiredFirstReads must be a non-empty list")
        for path in required_first_reads:
            if not (REPO_ROOT / path).exists():
                state_violations.append(f"requiredFirstReads path does not exist: {path}")

        required_startup_guards = _as_list(state.get("requiredStartupGuards"))
        if not required_startup_guards:
            state_violations.append("requiredStartupGuards must be a non-empty list")
        for path in required_startup_guards:
            if not (REPO_ROOT / path).exists():
                state_violations.append(f"requiredStartupGuards path does not exist: {path}")

        archive_path = state.get("historicalHandoffArchive")
        if isinstance(archive_path, str) and archive_path:
            if not (REPO_ROOT / archive_path).is_dir():
                state_violations.append(f"historicalHandoffArchive does not exist: {archive_path}")
        else:
            state_violations.append("historicalHandoffArchive must be a non-empty string")

        for field in ("supersededHandoffs", "relatedHandoffs"):
            for path in _as_list(state.get(field)):
                if not (REPO_ROOT / path).exists():
                    state_violations.append(f"{field} path does not exist: {path}")

        blocked = _as_list(state.get("blockedWorkClasses"))
        if not blocked:
            state_violations.append("blockedWorkClasses must be a non-empty list")

    marker_violations: dict[str, list[str]] = {}
    front_door_text = _read_text(FRONT_DOOR_PATH)
    missing_front_door_markers = [
        marker for marker in FRONT_DOOR_MARKERS
        if marker not in front_door_text
    ]
    if active_handoff and active_handoff not in front_door_text:
        missing_front_door_markers.append(active_handoff)
    if current_mode and current_mode not in front_door_text:
        missing_front_door_markers.append(current_mode)
    if freeze_posture and freeze_posture not in front_door_text:
        missing_front_door_markers.append(freeze_posture)
    if missing_front_door_markers:
        marker_violations[FRONT_DOOR_PATH] = missing_front_door_markers

    for path in (READ_FIRST_PATH, STARTUP_GUARDS_PATH, AGENTS_PATH, CLAUDE_PATH):
        text = _read_text(path)
        missing_markers = [
            marker for marker in AGENT_ROUTER_MARKERS
            if marker not in text
        ]
        if missing_markers:
            marker_violations[path] = missing_markers

    hook_text = _read_text(HOOK_CHAIN_PATH)
    if THIS_SCRIPT_PATH not in hook_text:
        marker_violations[HOOK_CHAIN_PATH] = [THIS_SCRIPT_PATH]

    active_handoffs = _active_handoffs()
    handoff_violations: list[str] = []
    if len(active_handoffs) != 1:
        handoff_violations.append(
            f"expected exactly one root AGENT_HANDOFF*.md with Status: ACTIVE, found {len(active_handoffs)}"
        )
    if active_handoff and active_handoffs and active_handoffs != [active_handoff]:
        handoff_violations.append(
            f"active handoff registry mismatch: registry={active_handoff}, detected={active_handoffs}"
        )

    # GC-020 In-Place Update Rule: active handoff must contain the current HEAD SHA.
    # An active handoff that does not mention the current HEAD is stale — it was not
    # updated after the last commit and will mislead the next agent about repo state.
    head_sha = _git_head_sha()
    head_sha_in_handoff: bool | None = None  # None = check skipped (git unavailable)
    if head_sha and active_handoff:
        handoff_path = REPO_ROOT / active_handoff
        if handoff_path.exists():
            handoff_text = handoff_path.read_text(encoding="utf-8", errors="replace")
            # Accept either the full SHA or the first 8 characters (short SHA).
            head_sha_in_handoff = (
                head_sha in handoff_text or head_sha[:8] in handoff_text
            )
            if not head_sha_in_handoff:
                handoff_violations.append(
                    f"active handoff does not contain current HEAD SHA {head_sha[:8]} "
                    f"({head_sha}) — update the handoff HEAD block after every commit "
                    "(GC-020 In-Place Update Rule)"
                )

    compliant = (
        not missing_files
        and not state_violations
        and not marker_violations
        and not handoff_violations
    )

    return {
        "frontDoor": FRONT_DOOR_PATH,
        "statePath": STATE_PATH,
        "activeHandoff": active_handoff,
        "detectedActiveHandoffs": active_handoffs,
        "requiredFirstReadCount": len(required_first_reads),
        "requiredStartupGuardCount": len(required_startup_guards),
        "missingFiles": missing_files,
        "missingFileCount": len(missing_files),
        "stateViolations": state_violations,
        "stateViolationCount": len(state_violations),
        "markerViolations": marker_violations,
        "markerViolationCount": len(marker_violations),
        "handoffViolations": handoff_violations,
        "handoffViolationCount": len(handoff_violations),
        "headSha": head_sha,
        "headShaInHandoff": head_sha_in_handoff,
        "compliant": compliant,
    }


def _print_report(report: dict[str, Any]) -> None:
    print("=== CVF Active Session State Compatibility Gate ===")
    print(f"Front door: {report['frontDoor']}")
    print(f"State registry: {report['statePath']}")
    print(f"Active handoff: {report['activeHandoff']}")
    print(f"Detected active handoffs: {', '.join(report['detectedActiveHandoffs']) or 'none'}")
    print(f"Required first reads: {report['requiredFirstReadCount']}")
    print(f"Required startup guards: {report['requiredStartupGuardCount']}")
    print(f"Missing files: {report['missingFileCount']}")
    print(f"State violations: {report['stateViolationCount']}")
    print(f"Marker violations: {report['markerViolationCount']}")
    print(f"Handoff violations: {report['handoffViolationCount']}")
    head_sha = report.get("headSha")
    head_in_handoff = report.get("headShaInHandoff")
    if head_sha:
        status = "present" if head_in_handoff else ("MISSING" if head_in_handoff is False else "skipped")
        print(f"HEAD SHA in handoff: {head_sha[:8]} — {status}")

    if report["missingFiles"]:
        print("\nMissing files:")
        for path in report["missingFiles"]:
            print(f"  - {path}")

    if report["stateViolations"]:
        print("\nState violations:")
        for issue in report["stateViolations"]:
            print(f"  - {issue}")

    if report["markerViolations"]:
        print("\nMarker violations:")
        for path, markers in report["markerViolations"].items():
            print(f"  - {path}")
            for marker in markers:
                print(f"    missing: {marker}")

    if report["handoffViolations"]:
        print("\nHandoff violations:")
        for issue in report["handoffViolations"]:
            print(f"  - {issue}")

    if report["compliant"]:
        print("\nCOMPLIANT - active session front door, registry, handoff pointer, and startup routing are aligned.")
        return

    print("\nVIOLATION - active session state is incomplete or misaligned.")
    print("Action required:")
    print(f"  1. Update {STATE_PATH} first.")
    print(f"  2. Keep {FRONT_DOOR_PATH}, {AGENTS_PATH}, and {CLAUDE_PATH} routed through the registry.")
    print("  3. Ensure exactly one root AGENT_HANDOFF*.md declares Status: ACTIVE.")
    print(f"  4. Ensure {HOOK_CHAIN_PATH} runs {THIS_SCRIPT_PATH}.")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(errors="replace")

    parser = argparse.ArgumentParser(description="CVF active session state compatibility gate")
    parser.add_argument("--enforce", action="store_true", help="Return exit 2 when active session state is misaligned")
    parser.add_argument("--json", action="store_true", help="Print JSON report")
    parser.add_argument("--write-report", default=None, help="Optional output path for JSON report file")
    args = parser.parse_args()

    report = {
        "timestamp": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        **_classify(),
    }

    if args.write_report:
        out_path = Path(args.write_report)
        if not out_path.is_absolute():
            out_path = (REPO_ROOT / out_path).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        _print_report(report)

    if args.enforce and not report["compliant"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
