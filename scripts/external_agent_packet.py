#!/usr/bin/env python3
"""Prepare CVF external-agent packets and validate returned folders.

The packet refresh path is deliberately fail-closed: the public-sync worktree
must be clean, its HEAD must equal live origin/main, and required public files
must exist before an operator-local snapshot is rewritten.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any
from zoneinfo import ZoneInfo


PROTOCOL_VERSION = "1.1.0"
PROTOCOL_ID = "cvf.external-agent-round-trip"
PUBLIC_REPOSITORY = "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git"
PACKET_FILES = (
    "CVF_EXTERNAL_AGENT_BOOTSTRAP_INSTRUCTIONS.md",
    "CVF_CONTEXT_BRIEF.md",
    "CVF_CURRENT_PUBLIC_SNAPSHOT.md",
    "CVF_EXTERNAL_AGENT_RETURN_CONTRACT.md",
)
REQUIRED_PUBLIC_PATHS = (
    "README.md",
    "ARCHITECTURE.md",
    "AGENTS.md",
    "docs/guides/external-agent-review-guide.md",
    "docs/guides/CVF_EXTERNAL_AGENT_ROUND_TRIP_KIT.md",
    "docs/reference/CVF_EXTERNAL_AGENT_OWNER_SURFACE_INDEX.json",
    "docs/reference/CVF_PUBLIC_EVALUATION_CLAIM_BOUNDARY_2026-06-04.md",
    "docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md",
    "docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md",
)
RETURN_REQUIRED = (
    "README.md",
    "EXTERNAL_AGENT_RETURN_MANIFEST.json",
    "SOURCE_MANIFEST.md",
    "DECISION_LOG.md",
    "TEST_EVIDENCE.md",
    "CLAIM_BOUNDARY.md",
    "FILE_INVENTORY.sha256",
)
INVENTORY_EXCLUDED_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__", ".pytest_cache"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")
IMMUTABLE_GITHUB = re.compile(r"^https://github\.com/[^/]+/[^/]+/(?:blob|tree)/[0-9a-f]{40}/")


class PacketError(RuntimeError):
    """A fail-closed packet preparation or validation error."""


def _run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode:
        raise PacketError(proc.stderr.strip() or proc.stdout.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def _canonical_remote(value: str) -> str:
    return value.strip().removesuffix(".git").rstrip("/")


def _now() -> datetime:
    return datetime.now(ZoneInfo("Asia/Ho_Chi_Minh"))


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise PacketError(f"cannot update {label}: expected one match, found {count}")
    return updated


def _update_snapshot_text(text: str, sha: str, commit_date: str, subject: str, tree_count: int, stamp: datetime) -> str:
    text = _replace_once(text, r"^protocolVersion: .+$", f"protocolVersion: {PROTOCOL_VERSION}", "protocolVersion")
    text = _replace_once(text, r"^updatedAt: .+$", f"updatedAt: {stamp.date().isoformat()}", "updatedAt")
    text = _replace_once(text, r"^Verified: .+$", f"Verified: {stamp.date().isoformat()} (Asia/Ho_Chi_Minh)", "Verified")
    text = _replace_once(text, r"(?m)(^Audit-anchor commit:\s*\n)`[0-9a-f]{40}`", rf"\g<1>`{sha}`", "audit-anchor commit")
    text = _replace_once(text, r"^Commit date: `[^`]+`$", f"Commit date: `{commit_date}`", "commit date")
    safe_subject = subject.replace("`", "'")
    text = _replace_once(text, r"^Commit subject: `[^`]*`$", f"Commit subject: `{safe_subject}`", "commit subject")
    text = _replace_once(text, r"contained [0-9,]+ entries;", f"contained {tree_count:,} entries;", "tree entry count")
    return text


def _packet_hashes(packet_root: Path, names: list[str]) -> dict[str, str]:
    return {name: hashlib.sha256((packet_root / name).read_bytes()).hexdigest() for name in sorted(names)}


def refresh_snapshot(public_repo: Path, packet_root: Path, owner_index_source: Path) -> dict[str, Any]:
    if not public_repo.is_dir() or not (public_repo / ".git").exists():
        raise PacketError(f"public repo is not a Git worktree: {public_repo}")
    if _run_git(public_repo, "status", "--porcelain"):
        raise PacketError("public-sync worktree must be clean before snapshot refresh")
    remote = _run_git(public_repo, "remote", "get-url", "origin")
    if _canonical_remote(remote) != _canonical_remote(PUBLIC_REPOSITORY):
        raise PacketError(f"origin is not the canonical public repository: {remote}")
    live_tokens = _run_git(public_repo, "ls-remote", "origin", "refs/heads/main").split()
    if len(live_tokens) < 2 or not SHA40.fullmatch(live_tokens[0]):
        raise PacketError("could not resolve live origin/main")
    live_sha = live_tokens[0]
    local_sha = _run_git(public_repo, "rev-parse", "HEAD")
    if local_sha != live_sha:
        raise PacketError(f"public-sync HEAD {local_sha} does not equal live origin/main {live_sha}")
    branch = _run_git(public_repo, "branch", "--show-current")
    if branch != "main":
        raise PacketError(f"public-sync checkout must be main, found {branch or 'detached HEAD'}")

    public_files = set(_run_git(public_repo, "ls-tree", "-r", "--name-only", live_sha).splitlines())
    missing = sorted(set(REQUIRED_PUBLIC_PATHS) - public_files)
    if missing:
        raise PacketError("required public paths missing: " + ", ".join(missing))
    for name in PACKET_FILES:
        if not (packet_root / name).is_file():
            raise PacketError(f"packet file missing: {name}")
    if not owner_index_source.is_file():
        raise PacketError(f"owner index source missing: {owner_index_source}")

    commit_date = _run_git(public_repo, "show", "-s", "--format=%cI", live_sha)
    subject = _run_git(public_repo, "show", "-s", "--format=%s", live_sha)
    stamp = _now()
    snapshot = packet_root / "CVF_CURRENT_PUBLIC_SNAPSHOT.md"
    snapshot.write_text(
        _update_snapshot_text(snapshot.read_text(encoding="utf-8"), live_sha, commit_date, subject, len(public_files), stamp),
        encoding="utf-8",
        newline="\n",
    )
    local_owner_index = packet_root / "CVF_PUBLIC_OWNER_SURFACE_INDEX.json"
    shutil.copyfile(owner_index_source, local_owner_index)
    names = [*PACKET_FILES, local_owner_index.name]
    receipt = {
        "schema": "cvf.externalAgentPacketRefreshReceipt.v1",
        "protocolVersion": PROTOCOL_VERSION,
        "status": "REFRESHED_LIVE_PUBLIC_MAIN",
        "verifiedAt": stamp.isoformat(timespec="seconds"),
        "publicRepository": PUBLIC_REPOSITORY,
        "publicBranch": "main",
        "publicCommit": live_sha,
        "publicCommitDate": commit_date,
        "publicCommitSubject": subject,
        "publicTreeEntries": len(public_files),
        "packetRoot": str(packet_root.resolve()),
        "packetFileHashes": _packet_hashes(packet_root, names),
        "claimBoundary": "Proves packet refresh against live public main only; no push, CI, provider, runtime, or production claim.",
    }
    _write_json(packet_root / "CVF_EXTERNAL_AGENT_PACKET_REFRESH_RECEIPT.json", receipt)
    return receipt


def create_capsule(args: argparse.Namespace, public_sha: str) -> dict[str, Any]:
    if not SHA40.fullmatch(args.source_commit):
        raise PacketError("--source-commit must be a lowercase 40-character Git SHA")
    stamp = _now()
    capsule = {
        "schema": "cvf.externalAgentTaskCapsule.v1",
        "protocolVersion": PROTOCOL_VERSION,
        "projectionOf": PROTOCOL_ID,
        "generatedAt": stamp.isoformat(timespec="seconds"),
        "task": {
            "id": args.task_id,
            "title": args.title,
            "objective": args.objective,
            "workingMode": args.working_mode,
            "outputRoot": args.output_root,
            "nonGoals": args.non_goal,
        },
        "cvfPublicSource": {"repository": PUBLIC_REPOSITORY, "commit": public_sha},
        "sourceRepositories": [{"repository": args.source_repository, "commit": args.source_commit, "usage": "REFERENCE_AND_ANALYSIS"}],
        "gateA": {
            "name": "SOURCE_OWNER_OVERLAP",
            "requiredBefore": "DESIGN_OR_CODE",
            "requiredEvidence": ["immutable source identity", "license expression and source", "CVF owner surface", "overlap/novelty disposition"],
            "terminalStates": ["PASS", "RETURN_FOR_REPAIR", "BLOCKED"],
        },
        "gateB": {
            "name": "DESIGN_CODE_TEST",
            "opensOnlyWhen": "gateA=PASS",
            "requiredEvidence": ["positive tests", "negative semantic tests", "malformed-input tests", "claim boundary", "exact commands and results"],
        },
        "authorityEnvelope": {
            "commit": False,
            "push": False,
            "publication": False,
            "deployment": False,
            "providerCalls": False,
            "credentials": False,
            "destructiveActions": False,
        },
    }
    _write_json(Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json", capsule)
    return capsule


def _safe_rel_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts and "\\" not in value


def _inventory_entries(root: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in INVENTORY_EXCLUDED_DIRS for part in path.relative_to(root).parts):
            continue
        rel = path.relative_to(root).as_posix()
        if rel in {"FILE_INVENTORY.sha256", "RETURN_VALIDATION_RECEIPT.json"}:
            continue
        entries[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return dict(sorted(entries.items()))


def _parse_inventory(path: Path, errors: list[str]) -> dict[str, str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("FILE_INVENTORY.sha256 must not contain a UTF-8 BOM")
    if b"\r\n" in raw or (raw and not raw.endswith(b"\n")):
        errors.append("FILE_INVENTORY.sha256 must use LF and one trailing LF")
    result: dict[str, str] = {}
    previous = ""
    for number, line in enumerate(raw.decode("utf-8-sig", errors="replace").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"inventory line {number} has invalid format")
            continue
        digest, rel = match.groups()
        if not _safe_rel_path(rel):
            errors.append(f"inventory line {number} has unsafe path: {rel}")
        if previous and rel <= previous:
            errors.append("inventory paths are not unique ordinal-sorted")
        previous = rel
        result[rel] = digest
    return result


def _validate_source_rows(manifest: dict[str, Any], errors: list[str]) -> None:
    sources = manifest.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("manifest.sources must be a non-empty list")
        return
    for index, source in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{prefix} must be an object")
            continue
        commit = source.get("commit")
        if not isinstance(commit, str) or not SHA40.fullmatch(commit):
            errors.append(f"{prefix}.commit must be a lowercase 40-character Git SHA")
        immutable = source.get("immutableReference")
        if not isinstance(immutable, str) or not IMMUTABLE_GITHUB.match(immutable):
            errors.append(f"{prefix}.immutableReference must be a GitHub blob/tree URL pinned to a 40-character SHA")
        elif isinstance(commit, str) and f"/{commit}/" not in immutable:
            errors.append(f"{prefix}.immutableReference SHA must equal {prefix}.commit")
        license_source = source.get("licenseSource")
        if not isinstance(license_source, str) or not IMMUTABLE_GITHUB.match(license_source):
            errors.append(f"{prefix}.licenseSource must be a GitHub blob/tree URL pinned to a 40-character SHA")
        elif isinstance(commit, str) and f"/{commit}/" not in license_source:
            errors.append(f"{prefix}.licenseSource SHA must equal {prefix}.commit")
        for field in ("licenseExpression", "usageType", "ownerSurface", "overlapDisposition"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                errors.append(f"{prefix}.{field} must be non-empty")


def validate_return(root: Path, receipt_path: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    for name in RETURN_REQUIRED:
        if not (root / name).is_file():
            errors.append(f"missing required root artifact: {name}")
    manifest: dict[str, Any] = {}
    manifest_path = root / "EXTERNAL_AGENT_RETURN_MANIFEST.json"
    if manifest_path.is_file():
        try:
            loaded = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest = loaded if isinstance(loaded, dict) else {}
            if not isinstance(loaded, dict):
                errors.append("return manifest must be a JSON object")
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"return manifest is invalid JSON: {exc}")

    expected = {
        "schema": "cvf.externalAgentReturn.v1",
        "artifactClass": "PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE",
        "authorityStatus": "NON_AUTHORITATIVE_UNTIL_REVIEWED",
        "secretsReturned": False,
    }
    for field, value in expected.items():
        if manifest.get(field) != value:
            errors.append(f"manifest.{field} must equal {value!r}")
    cvf_source = manifest.get("cvfPublicSource")
    if not isinstance(cvf_source, dict) or not SHA40.fullmatch(str(cvf_source.get("commit", ""))):
        errors.append("manifest.cvfPublicSource.commit must be a lowercase 40-character Git SHA")
    elif cvf_source.get("repository") != PUBLIC_REPOSITORY:
        errors.append("manifest.cvfPublicSource.repository is not the canonical public repository")
    _validate_source_rows(manifest, errors)

    files = manifest.get("files")
    manifest_files: dict[str, str] = {}
    if not isinstance(files, list) or not files:
        errors.append("manifest.files must be a non-empty list")
    else:
        for index, item in enumerate(files):
            if not isinstance(item, dict) or not _safe_rel_path(str(item.get("path", ""))):
                errors.append(f"manifest.files[{index}].path is invalid")
                continue
            rel = item["path"]
            digest = item.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                errors.append(f"manifest.files[{index}].sha256 is invalid")
            elif rel in manifest_files:
                errors.append(f"manifest.files contains duplicate path: {rel}")
            else:
                manifest_files[rel] = digest

    actual = _inventory_entries(root) if root.is_dir() else {}
    inventory = _parse_inventory(root / "FILE_INVENTORY.sha256", errors) if (root / "FILE_INVENTORY.sha256").is_file() else {}
    if inventory != actual:
        errors.append("FILE_INVENTORY.sha256 does not exactly match returned files and hashes")
    manifest_expected = {path: digest for path, digest in actual.items() if path != "EXTERNAL_AGENT_RETURN_MANIFEST.json"}
    if manifest_files != manifest_expected:
        errors.append("manifest.files does not exactly match returned files and hashes, excluding the self-referential manifest")

    verification = manifest.get("verification")
    if not isinstance(verification, dict) or not isinstance(verification.get("commands"), list):
        errors.append("manifest.verification.commands must be a list")
    else:
        executed = [row for row in verification["commands"] if isinstance(row, dict) and row.get("executed") is True]
        negative = [row for row in executed if row.get("testClass") in {"negative", "malformed", "authority-widening", "replay-expiry", "secret-redaction", "dependency-failure"}]
        if not executed:
            errors.append("verification must contain at least one executed command record")
        if not negative:
            errors.append("verification must contain executed negative semantic evidence")
    effects = manifest.get("externalEffects")
    if not isinstance(effects, list):
        errors.append("manifest.externalEffects must be a list")
    else:
        for index, effect in enumerate(effects):
            if not isinstance(effect, dict) or not all(effect.get(field) for field in ("type", "target", "authorizedBy", "evidence", "rollback")):
                errors.append(f"externalEffects[{index}] lacks authorization/evidence/rollback fields")

    readme = (root / "README.md").read_text(encoding="utf-8", errors="replace") if (root / "README.md").is_file() else ""
    for marker in (expected["artifactClass"], expected["authorityStatus"]):
        if marker not in readme:
            errors.append(f"README.md lacks authority marker: {marker}")

    status = "PASS" if not errors else "RETURN_FOR_REPAIR"
    receipt = {
        "schema": "cvf.externalAgentReturnValidationReceipt.v1",
        "protocolVersion": PROTOCOL_VERSION,
        "validatedAt": _now().isoformat(timespec="seconds"),
        "returnRoot": str(root.resolve()),
        "status": status,
        "gateA": "PASS" if not any("source" in error.lower() or "license" in error.lower() or "owner" in error.lower() or "overlap" in error.lower() for error in errors) else "RETURN_FOR_REPAIR",
        "gateB": "PASS" if not any("verification" in error.lower() or "inventory" in error.lower() or "hash" in error.lower() for error in errors) else "RETURN_FOR_REPAIR",
        "filesObserved": len(actual),
        "errors": errors,
        "warnings": warnings,
        "claimBoundary": "Structural, integrity, and bounded semantic intake validation only; not CVF acceptance or absorption approval.",
    }
    _write_json(receipt_path, receipt)
    return receipt


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    refresh = sub.add_parser("refresh-snapshot", help="bind an operator packet to verified live public main")
    refresh.add_argument("--public-repo", required=True)
    refresh.add_argument("--packet-root", required=True)
    refresh.add_argument("--owner-index-source", required=True)

    prepare = sub.add_parser("prepare-task", help="refresh the packet and generate a per-task capsule")
    prepare.add_argument("--public-repo", required=True)
    prepare.add_argument("--packet-root", required=True)
    prepare.add_argument("--owner-index-source", required=True)
    prepare.add_argument("--task-id", required=True)
    prepare.add_argument("--title", required=True)
    prepare.add_argument("--objective", required=True)
    prepare.add_argument("--working-mode", required=True, choices=("REVIEW_ONLY", "DESIGN_ONLY", "BUILD_NEW_REPOSITORY", "EXTEND_SUPPLIED_REPOSITORY", "SOURCE_PACK_PREPARATION"))
    prepare.add_argument("--source-repository", required=True)
    prepare.add_argument("--source-commit", required=True)
    prepare.add_argument("--output-root", required=True)
    prepare.add_argument("--non-goal", action="append", default=[])

    validate = sub.add_parser("validate-return", help="validate a returned external-agent folder")
    validate.add_argument("--return-root", required=True)
    validate.add_argument("--receipt")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        if args.command in {"refresh-snapshot", "prepare-task"}:
            receipt = refresh_snapshot(Path(args.public_repo), Path(args.packet_root), Path(args.owner_index_source))
            if args.command == "prepare-task":
                create_capsule(args, receipt["publicCommit"])
                capsule_path = Path(args.packet_root) / "CVF_EXTERNAL_AGENT_TASK_CAPSULE.json"
                receipt["taskCapsuleSha256"] = hashlib.sha256(capsule_path.read_bytes()).hexdigest()
                receipt["taskId"] = args.task_id
                _write_json(Path(args.packet_root) / "CVF_EXTERNAL_AGENT_PACKET_REFRESH_RECEIPT.json", receipt)
            print(json.dumps(receipt, indent=2, sort_keys=True))
            return 0
        root = Path(args.return_root)
        receipt_path = Path(args.receipt) if args.receipt else root.parent / f"{root.name}.RETURN_VALIDATION_RECEIPT.json"
        receipt = validate_return(root, receipt_path)
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return 0 if receipt["status"] == "PASS" else 1
    except (OSError, PacketError, ValueError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
