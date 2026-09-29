#!/usr/bin/env python3
"""Deterministic two-phase helper for governed CVF tranche commits.

The helper never invents continuity semantics. It commits an already-staged
material batch, then lets the caller author governed session sources and
resume with a SHA-keyed manifest. Dry-runs are strictly read-only.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CORE_STATE = Path("CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json")
AGGREGATE = Path("CVF_SESSION/ACTIVE_SESSION_STATE.json")
BOOTSTRAP = Path("CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json")
SESSION_MEMORY = "CVF_SESSION_MEMORY.md"
NEXT_MOVE = "CVF_SESSION/state/entries/nextAllowedMove.json"
DERIVED_OUTPUTS = {AGGREGATE.as_posix(), BOOTSTRAP.as_posix()}
MANIFEST_SCHEMA = "cvf.gc020ContinuityManifest.v1"
OUTPUT_SCHEMA = "cvf.gc020TerminalOutput.v1"
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
ACTIVE_STATUS_RE = re.compile(r"^Status:\s*ACTIVE\s*$", re.MULTILINE)
LEGACY_HEAD_RE = re.compile(r"^Current HEAD recorded for this handoff: `[^`]+`.*$", re.MULTILINE)
EVIDENCE_RE = re.compile(
    r"\n?<!-- CVF-GC020-MATERIAL-SHA:START -->\n.*?"
    r"<!-- CVF-GC020-MATERIAL-SHA:END -->\n?", re.DOTALL
)
TERMINAL_EXIT = {
    "ARGUMENT_VALIDATION_FAILED": 2,
    "DRY_RUN_MATERIAL_VALIDATED": 0,
    "MATERIAL_VALIDATION_FAILED": 1,
    "MATERIAL_COMMIT_FAILED": 1,
    "MATERIAL_COMMITTED_CONTINUITY_PENDING": 0,
    "DRY_RUN_CONTINUITY_PLAN_VALIDATED": 0,
    "CONTINUITY_VALIDATION_FAILED": 3,
    "CONTINUITY_COMMIT_FAILED": 4,
    "CONTINUITY_POSTCOMMIT_VALIDATION_FAILED": 5,
    "COMPLETE_ONE_MATERIAL_ONE_CONTINUITY": 0,
    "ALREADY_SYNCHRONIZED": 0,
}
CONTINUITY_CHECKS = [
    [sys.executable, "governance/compat/generate_active_session_state.py", "--check"],
    [sys.executable, "governance/compat/check_active_session_state.py", "--enforce"],
    [sys.executable, "governance/compat/check_next_move_freshness.py", "--enforce"],
]


class ArgumentFailure(Exception):
    """Raised instead of allowing argparse to emit non-JSON output."""


@dataclass
class SemanticFailure(Exception):
    code: str
    details: dict[str, Any]


@dataclass
class CommandFailure(Exception):
    argv: list[str]


class TerminalParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ArgumentFailure(message)


def _configure_stdout() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def _run(argv: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        argv, cwd=REPO_ROOT, capture_output=True, text=True,
        encoding="utf-8", errors="replace", check=False
    )


def _command(argv: list[str]) -> subprocess.CompletedProcess[str]:
    result = _run(argv)
    if result.returncode:
        raise CommandFailure(argv)
    return result


def _git(argv: list[str], *, required: bool = True) -> subprocess.CompletedProcess[str]:
    result = _run(["git", *argv])
    if required and result.returncode:
        raise CommandFailure(["git", *argv])
    return result


def _lines(value: str) -> list[str]:
    return sorted({line.strip().replace("\\", "/") for line in value.splitlines() if line.strip()})


def _head(ref: str = "HEAD") -> str | None:
    result = _git(["rev-parse", ref], required=False)
    return result.stdout.strip() if result.returncode == 0 else None


def _path_state() -> tuple[list[str], list[str], list[str]]:
    staged = _lines(_git(["diff", "--cached", "--name-only"]).stdout)
    unstaged = _lines(_git(["diff", "--name-only"]).stdout)
    untracked = _lines(_git(["ls-files", "--others", "--exclude-standard"]).stdout)
    return staged, unstaged, untracked


def _best_effort_handoff() -> str | None:
    for source in (REPO_ROOT / CORE_STATE, REPO_ROOT / AGGREGATE):
        try:
            value = json.loads(source.read_text(encoding="utf-8")).get("activeHandoff")
            if isinstance(value, str) and value:
                return value
        except (OSError, ValueError, AttributeError):
            pass
    return None


def _resume_template(material_sha: str | None, base: str | None,
                     manifest: str | None, *, execute: bool = True) -> list[str] | None:
    if not material_sha or not base:
        return None
    manifest = manifest or f".cvf/runtime/tranche-continuity/{material_sha}.json"
    result = [
        "python", "scripts/cvf_commit_tranche.py", "--mode", "resume",
        "--resume-material-sha", material_sha, "--base", base,
        "--continuity-manifest", manifest, "--continuity-message",
        "<continuityCommitMessage>",
    ]
    if execute:
        result.append("--execute")
    return result


def _emit(state: str, *, material_sha: str | None = None,
          active_handoff: str | None = None,
          failed_command: list[str] | None = None,
          diagnostic_code: str | None = None,
          diagnostic_details: dict[str, Any] | None = None,
          resume_argv: list[str] | None = None) -> int:
    try:
        staged, unstaged, untracked = _path_state()
    except CommandFailure:
        staged, unstaged, untracked = [], [], []
    payload = {
        "schemaVersion": OUTPUT_SCHEMA,
        "terminalState": state,
        "materialSha": material_sha,
        "currentHead": _head(),
        "activeHandoff": active_handoff,
        "stagedPaths": staged,
        "unstagedPaths": unstaged,
        "untrackedPaths": untracked,
        "failedCommand": failed_command,
        "diagnosticCode": diagnostic_code,
        "diagnosticDetails": diagnostic_details,
        "resumeArgvTemplate": resume_argv,
        "resumeCommand": None,
    }
    print(json.dumps(payload, ensure_ascii=False))
    return TERMINAL_EXIT[state]


def _parser() -> TerminalParser:
    parser = TerminalParser(add_help=True)
    parser.add_argument("--mode", choices=("material", "resume"), required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--message")
    parser.add_argument("--resume-material-sha")
    parser.add_argument("--continuity-manifest")
    parser.add_argument("--continuity-message")
    parser.add_argument("--execute", action="store_true")
    return parser


def _validate_args(args: argparse.Namespace) -> None:
    if not SHA_RE.fullmatch(args.base or ""):
        raise ArgumentFailure("--base must be exactly 40 hexadecimal characters")
    if args.mode == "material":
        if not args.message:
            raise ArgumentFailure("--message is required in material mode")
        if args.resume_material_sha or args.continuity_manifest or args.continuity_message:
            raise ArgumentFailure("resume-only arguments are forbidden in material mode")
        return
    if args.message:
        raise ArgumentFailure("--message is forbidden in resume mode")
    if not SHA_RE.fullmatch(args.resume_material_sha or ""):
        raise ArgumentFailure("--resume-material-sha must be exactly 40 hexadecimal characters")
    if not args.continuity_manifest:
        raise ArgumentFailure("--continuity-manifest is required in resume mode")
    if args.execute and not args.continuity_message:
        raise ArgumentFailure("--continuity-message is required in resume execute mode")


def _validate_material() -> None:
    staged, unstaged, untracked = _path_state()
    if not staged:
        raise SemanticFailure("NO_STAGED_MATERIAL", {})
    if unstaged or untracked:
        raise SemanticFailure("UNRELATED_MATERIAL_PRESENT", {"paths": sorted(set(unstaged + untracked))})


def _material(args: argparse.Namespace) -> int:
    active = _best_effort_handoff()
    try:
        _validate_material()
    except SemanticFailure as exc:
        return _emit("MATERIAL_VALIDATION_FAILED", active_handoff=active,
                     diagnostic_code=exc.code, diagnostic_details=exc.details)
    if not args.execute:
        return _emit("DRY_RUN_MATERIAL_VALIDATED", active_handoff=active)
    preflight = [
        sys.executable, "governance/compat/run_agent_autorun_workflow_gate.py",
        "--phase", "pre-implementation", "--base", args.base, "--head", "HEAD",
    ]
    try:
        _command(preflight)
    except CommandFailure as exc:
        return _emit("MATERIAL_VALIDATION_FAILED", active_handoff=active, failed_command=exc.argv)
    commit_argv = ["git", "commit", "-m", args.message]
    try:
        _command(commit_argv)
    except CommandFailure:
        return _emit("MATERIAL_COMMIT_FAILED", active_handoff=active, failed_command=commit_argv)
    material_sha = _head()
    active = _best_effort_handoff()  # Preserved post-material re-resolution.
    return _emit(
        "MATERIAL_COMMITTED_CONTINUITY_PENDING", material_sha=material_sha,
        active_handoff=active, resume_argv=_resume_template(material_sha, args.base, None)
    )


def _manifest_path(raw: str, material_sha: str) -> Path:
    posix = PurePosixPath(raw)
    if Path(raw).is_absolute() or posix.is_absolute() or re.match(r"^[A-Za-z]:", raw):
        raise SemanticFailure("MANIFEST_PATH_MUST_BE_REPO_RELATIVE", {"path": raw})
    if "\\" in raw or ".." in posix.parts:
        raise SemanticFailure("PATH_TRAVERSAL_REJECTED", {"path": raw})
    expected = f".cvf/runtime/tranche-continuity/{material_sha}.json"
    if not raw.startswith(".cvf/runtime/tranche-continuity/"):
        raise SemanticFailure("MANIFEST_PATH_OUTSIDE_RUNTIME_DIRECTORY", {"path": raw})
    if posix.name != f"{material_sha}.json":
        raise SemanticFailure("MANIFEST_SHA_MISMATCH", {"path": raw, "materialSha": material_sha})
    if raw != expected:
        raise SemanticFailure("MANIFEST_PATH_OUTSIDE_RUNTIME_DIRECTORY", {"path": raw})
    return REPO_ROOT / Path(*posix.parts)


def _active_handoff_from_core() -> str:
    try:
        core = json.loads((REPO_ROOT / CORE_STATE).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SemanticFailure("STALE_HANDOFF_REJECTED", {"reason": str(exc)}) from exc
    active = core.get("activeHandoff") if isinstance(core, dict) else None
    if not isinstance(active, str) or not re.fullmatch(r"AGENT_HANDOFF[^/\\]*\.md", active):
        raise SemanticFailure("STALE_HANDOFF_REJECTED", {"activeHandoff": active})
    path = REPO_ROOT / active
    if not path.is_file() or not ACTIVE_STATUS_RE.search(path.read_text(encoding="utf-8")):
        raise SemanticFailure("STALE_HANDOFF_REJECTED", {"activeHandoff": active})
    active_roots = [
        candidate.name for candidate in REPO_ROOT.glob("AGENT_HANDOFF*.md")
        if ACTIVE_STATUS_RE.search(candidate.read_text(encoding="utf-8", errors="replace"))
    ]
    if active_roots != [active]:
        raise SemanticFailure("STALE_HANDOFF_REJECTED",
                              {"activeHandoff": active, "activeRootHandoffs": active_roots})
    return active


def _load_manifest(raw: str, material_sha: str, active: str) -> tuple[Path, list[str]]:
    path = _manifest_path(raw, material_sha)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SemanticFailure("MANIFEST_PATH_NOT_FOUND", {"path": raw, "reason": str(exc)}) from exc
    if not isinstance(data, dict) or data.get("schemaVersion") != MANIFEST_SCHEMA:
        raise SemanticFailure("MANIFEST_SCHEMA_REJECTED", {"path": raw})
    paths = data.get("paths")
    if not isinstance(paths, list) or any(not isinstance(item, str) for item in paths):
        raise SemanticFailure("MANIFEST_SCHEMA_REJECTED", {"path": raw})
    seen: set[str] = set()
    for item in paths:
        pure = PurePosixPath(item)
        if "\\" in item or pure.is_absolute() or ".." in pure.parts:
            raise SemanticFailure("PATH_TRAVERSAL_REJECTED", {"path": item})
        if item in seen:
            raise SemanticFailure("DUPLICATE_MANIFEST_PATH", {"path": item})
        seen.add(item)
        if item in DERIVED_OUTPUTS:
            raise SemanticFailure("GENERATED_OUTPUT_MUST_NOT_BE_MANIFESTED", {"path": item})
        if not (item == SESSION_MEMORY or item.startswith("CVF_SESSION/state/") or item == active):
            raise SemanticFailure("NON_SESSION_SYNC_PATH_REJECTED", {"path": item})
        if not (REPO_ROOT / Path(*pure.parts)).exists():
            raise SemanticFailure("MANIFEST_PATH_NOT_FOUND", {"path": item})
    required = {
        "activeRootHandoff": active, "sessionMemory": SESSION_MEMORY,
        "coreSource": CORE_STATE.as_posix(), "nextAllowedMove": NEXT_MOVE,
    }
    for member_class, member in required.items():
        if member not in seen:
            raise SemanticFailure("MANIFEST_MISSING_REQUIRED_MEMBER",
                                  {"memberClass": member_class, "path": member})
    additional = [item for item in paths
                  if item.startswith("CVF_SESSION/state/entries/") and item != NEXT_MOVE]
    if not additional:
        raise SemanticFailure("MANIFEST_MISSING_REQUIRED_MEMBER",
                              {"memberClass": "additionalStateEntry"})
    return path, paths


def _classify_topology(material_sha: str, base: str) -> str:
    material_parent = _head(f"{material_sha}^")
    if material_parent != base:
        raise SemanticFailure("MATERIAL_PARENT_MISMATCH",
                              {"materialParent": material_parent, "base": base})
    current = _head()
    if current == material_sha:
        return "PENDING_OR_RETRY"
    if _head("HEAD^") == material_sha:
        return "POSTCOMMIT_RECHECK"
    raise SemanticFailure("UNCLASSIFIABLE_TOPOLOGY",
                          {"currentHead": current, "materialSha": material_sha})


def _validate_pending(paths: list[str]) -> None:
    staged, unstaged, untracked = _path_state()
    pending = set(staged + unstaged + untracked)
    manifest = set(paths)
    missing = sorted(manifest - pending)
    if missing:
        raise SemanticFailure("MANIFESTED_PATH_HAS_NO_PENDING_CHANGE", {"paths": missing})
    extra = sorted(pending - manifest - DERIVED_OUTPUTS)
    if extra:
        code = "UNRELATED_MATERIAL_STAGED" if set(extra) & set(staged) else "UNRELATED_MATERIAL_PRESENT"
        raise SemanticFailure(code, {"paths": extra})


def _evidence_block(material_sha: str) -> str:
    return (
        "<!-- CVF-GC020-MATERIAL-SHA:START -->\n"
        f"Current HEAD recorded for this handoff: `{material_sha}`. "
        "Material parent anchor for the dedicated continuity synchronization commit.\n"
        "<!-- CVF-GC020-MATERIAL-SHA:END -->"
    )


def _update_handoff(active: str, material_sha: str) -> None:
    path = REPO_ROOT / active
    text = EVIDENCE_RE.sub("\n", path.read_text(encoding="utf-8")).rstrip() + "\n"
    text = LEGACY_HEAD_RE.sub("", text).replace("\n\n\n", "\n\n")
    first_break = text.find("\n")
    if first_break < 0 or not text.startswith("# "):
        raise SemanticFailure("HANDOFF_STRUCTURE_REJECTED", {"path": active})
    updated = (text[:first_break + 1] + "\n" + _evidence_block(material_sha) + "\n" +
               text[first_break + 1:].lstrip("\n"))
    path.write_text(updated, encoding="utf-8", newline="\n")


def _verify_generated_handoff(active: str) -> None:
    values: dict[str, Any] = {}
    for label, rel in (("core", CORE_STATE), ("aggregate", AGGREGATE), ("bootstrap", BOOTSTRAP)):
        try:
            values[label] = json.loads((REPO_ROOT / rel).read_text(encoding="utf-8")).get("activeHandoff")
        except (OSError, ValueError, AttributeError) as exc:
            raise SemanticFailure("GENERATED_HANDOFF_DISAGREEMENT", {"source": label}) from exc
    if set(values.values()) != {active}:
        raise SemanticFailure("GENERATED_HANDOFF_DISAGREEMENT", values)


def _run_checks() -> None:
    for argv in CONTINUITY_CHECKS:
        _command(argv)


def _resume_failure(state: str, args: argparse.Namespace, active: str | None, *,
                    command: list[str] | None = None,
                    semantic: SemanticFailure | None = None) -> int:
    return _emit(
        state, material_sha=args.resume_material_sha, active_handoff=active,
        failed_command=command,
        diagnostic_code=semantic.code if semantic else None,
        diagnostic_details=semantic.details if semantic else None,
        resume_argv=_resume_template(args.resume_material_sha, args.base, args.continuity_manifest),
    )


def _postcommit_recheck(args: argparse.Namespace, active: str, paths: list[str]) -> int:
    try:
        staged, unstaged, untracked = _path_state()
        if staged or unstaged or untracked:
            raise SemanticFailure("POSTCOMMIT_WORKTREE_NOT_CLEAN",
                                  {"paths": sorted(set(staged + unstaged + untracked))})
        changed = set(_lines(_git(["diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"]).stdout))
        expected = set(paths) | DERIVED_OUTPUTS
        if changed != expected:
            raise SemanticFailure("POSTCOMMIT_PATH_SET_MISMATCH",
                                  {"expected": sorted(expected), "actual": sorted(changed)})
        if args.resume_material_sha not in (REPO_ROOT / active).read_text(encoding="utf-8"):
            raise SemanticFailure("HANDOFF_EVIDENCE_MISMATCH", {"path": active})
        _verify_generated_handoff(active)
        _run_checks()
    except SemanticFailure as exc:
        return _resume_failure("CONTINUITY_POSTCOMMIT_VALIDATION_FAILED", args, active, semantic=exc)
    except CommandFailure as exc:
        return _resume_failure("CONTINUITY_POSTCOMMIT_VALIDATION_FAILED", args, active, command=exc.argv)
    return _emit("ALREADY_SYNCHRONIZED", material_sha=args.resume_material_sha, active_handoff=active)


def _pending_or_retry(args: argparse.Namespace, active: str, paths: list[str]) -> int:
    try:
        _validate_pending(paths)
    except SemanticFailure as exc:
        return _resume_failure("CONTINUITY_VALIDATION_FAILED", args, active, semantic=exc)
    if not args.execute:
        return _emit("DRY_RUN_CONTINUITY_PLAN_VALIDATED",
                     material_sha=args.resume_material_sha, active_handoff=active)
    try:
        _update_handoff(active, args.resume_material_sha)
        _command([sys.executable, "governance/compat/generate_active_session_state.py", "--generate"])
        _verify_generated_handoff(active)
        expected = set(paths) | DERIVED_OUTPUTS
        _command(["git", "add", "--", *paths, *sorted(DERIVED_OUTPUTS)])
        staged, _, _ = _path_state()
        if set(staged) != expected:
            raise SemanticFailure("STAGED_PATH_SET_MISMATCH",
                                  {"expected": sorted(expected), "actual": staged})
        unchanged = [item for item in sorted(DERIVED_OUTPUTS)
                     if _git(["diff", "--cached", "--quiet", "--", item], required=False).returncode == 0]
        if unchanged:
            raise SemanticFailure("GENERATED_OUTPUT_UNCHANGED", {"paths": unchanged})
        _run_checks()
    except SemanticFailure as exc:
        return _resume_failure("CONTINUITY_VALIDATION_FAILED", args, active, semantic=exc)
    except CommandFailure as exc:
        return _resume_failure("CONTINUITY_VALIDATION_FAILED", args, active, command=exc.argv)
    commit_argv = ["git", "commit", "-m", args.continuity_message]
    try:
        _command(commit_argv)
    except CommandFailure:
        return _resume_failure("CONTINUITY_COMMIT_FAILED", args, active, command=commit_argv)
    try:
        if _head("HEAD^") != args.resume_material_sha or _head(f"{args.resume_material_sha}^") != args.base:
            raise SemanticFailure("POSTCOMMIT_TOPOLOGY_MISMATCH", {})
        _run_checks()
    except SemanticFailure as exc:
        return _resume_failure("CONTINUITY_POSTCOMMIT_VALIDATION_FAILED", args, active, semantic=exc)
    except CommandFailure as exc:
        return _resume_failure("CONTINUITY_POSTCOMMIT_VALIDATION_FAILED", args, active, command=exc.argv)
    return _emit("COMPLETE_ONE_MATERIAL_ONE_CONTINUITY",
                 material_sha=args.resume_material_sha, active_handoff=active)


def _resume(args: argparse.Namespace) -> int:
    active: str | None = None
    try:
        active = _active_handoff_from_core()
        _, paths = _load_manifest(args.continuity_manifest, args.resume_material_sha, active)
        branch = _classify_topology(args.resume_material_sha, args.base)
    except SemanticFailure as exc:
        return _resume_failure("CONTINUITY_VALIDATION_FAILED", args, active, semantic=exc)
    if branch == "POSTCOMMIT_RECHECK":
        return _postcommit_recheck(args, active, paths)
    return _pending_or_retry(args, active, paths)


def main(argv: list[str] | None = None) -> int:
    _configure_stdout()
    raw = list(sys.argv[1:] if argv is None else argv)
    forbidden = {"--handoff-message", "--handoff-summary", "--allow-unstaged", "--skip-preclosure"}
    rejected = sorted({item.split("=", 1)[0] for item in raw} & forbidden)
    try:
        if rejected:
            raise ArgumentFailure(f"rejected legacy or bypass option: {rejected[0]}")
        args = _parser().parse_args(raw)
        _validate_args(args)
    except ArgumentFailure as exc:
        return _emit(
            "ARGUMENT_VALIDATION_FAILED", active_handoff=_best_effort_handoff(),
            diagnostic_code="ARGUMENT_VALIDATION_FAILED",
            diagnostic_details={"message": str(exc)},
        )
    return _material(args) if args.mode == "material" else _resume(args)


if __name__ == "__main__":
    raise SystemExit(main())
