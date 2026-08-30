#!/usr/bin/env python3
"""Fail-closed projection helpers for the portable external-agent snapshot."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


class SnapshotProjectionError(RuntimeError):
    """Raised when public posture cannot be projected without guessing."""


def _replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise SnapshotProjectionError(f"cannot update {label}: expected one match, found {count}")
    return updated


def update_snapshot_metadata(
    text: str,
    *,
    protocol_version: str,
    sha: str,
    commit_date: str,
    subject: str,
    tree_count: int,
    snapshot_date: str,
) -> str:
    """Update identity metadata while rejecting an unexpected template shape."""
    text = _replace_once(text, r"^protocolVersion: .+$", f"protocolVersion: {protocol_version}", "protocolVersion")
    text = _replace_once(text, r"^updatedAt: .+$", f"updatedAt: {snapshot_date}", "updatedAt")
    text = _replace_once(text, r"^Verified: .+$", f"Verified: {snapshot_date} (Asia/Ho_Chi_Minh)", "Verified")
    text = _replace_once(text, r"(?m)(^Audit-anchor commit:\s*\n)`[0-9a-f]{40}`", rf"\g<1>`{sha}`", "audit-anchor commit")
    text = _replace_once(text, r"^Commit date: `[^`]+`$", f"Commit date: `{commit_date}`", "commit date")
    safe_subject = subject.replace("`", "'")
    text = _replace_once(text, r"^Commit subject: `[^`]*`$", f"Commit subject: `{safe_subject}`", "commit subject")
    return _replace_once(text, r"contained [0-9,]+ entries;", f"contained {tree_count:,} entries;", "tree entry count")


def _release_posture(public_repo: Path) -> tuple[str, str]:
    changelog = (public_repo / "CHANGELOG.md").read_text(encoding="utf-8")
    release = re.search(r"^## \[(v[^\]]+)\].*$", changelog, re.MULTILINE)
    status = re.search(r"^Status:\s*([A-Z][A-Z0-9_]+)\s*$", changelog, re.MULTILINE)
    if not release or not status:
        raise SnapshotProjectionError("cannot derive current release/version posture from CHANGELOG.md")
    return release.group(1), status.group(1)


def _provider_posture(public_repo: Path) -> list[tuple[str, str, str]]:
    matrix_path = public_repo / "docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md"
    matrix = matrix_path.read_text(encoding="utf-8")
    rows = re.findall(
        r"^\|\s*(Alibaba|DeepSeek|OpenAI)\s*\|\s*`([^`]+)`\s*\|\s*`([A-Z][A-Z0-9_]+)`\s*\|",
        matrix,
        re.MULTILINE,
    )
    by_provider = {provider: (model, status) for provider, model, status in rows}
    required = ("Alibaba", "DeepSeek", "OpenAI")
    missing = [provider for provider in required if provider not in by_provider]
    if missing:
        raise SnapshotProjectionError("cannot derive provider posture for: " + ", ".join(missing))
    return [(provider, *by_provider[provider]) for provider in required]


def project_current_public_posture(text: str, public_repo: Path) -> str:
    """Project release/provider claims from pinned public source owners."""
    version, release_status = _release_posture(public_repo)
    providers = _provider_posture(public_repo)
    text = _replace_once(
        text,
        r"^- (?:a )?local-first .*?, not hosted SaaS;$",
        f"- local-first `{version}` GA release (`{release_status}`), not hosted SaaS;",
        "public product release posture",
    )
    provider_lines = "\n".join(
        f"- {provider} `{model}`: `{status}` public lane;" for provider, model, status in providers
    )
    provider_block = (
        "At this commit, the governed public provider matrix identifies:\n\n"
        f"{provider_lines}\n\n"
        "Projection sources: `CHANGELOG.md` and "
        "`docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` at the audit-anchor commit.\n"
    )
    text = _replace_once(
        text,
        r"(?ms)^At this commit, (?:the public README|the governed public provider matrix) identifies:\n\n.*?(?=\nThese are lane-specific evidence statements\.)",
        provider_block.rstrip(),
        "provider posture block",
    )
    return text


def _run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], text=True, encoding="utf-8", errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if proc.returncode:
        raise SnapshotProjectionError(proc.stderr.strip() or proc.stdout.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def _hashes(root: Path, names: list[str]) -> dict[str, str]:
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in sorted(names)}


def refresh_public_snapshot(
    public_repo: Path,
    packet_root: Path,
    owner_index_source: Path,
    *,
    protocol_version: str,
    public_repository: str,
    packet_files: tuple[str, ...],
    required_public_paths: tuple[str, ...],
) -> dict[str, Any]:
    """Verify live public main, project posture, and write a bound receipt."""
    if not public_repo.is_dir() or not (public_repo / ".git").exists():
        raise SnapshotProjectionError(f"public repo is not a Git worktree: {public_repo}")
    if _run_git(public_repo, "status", "--porcelain"):
        raise SnapshotProjectionError("public-sync worktree must be clean before snapshot refresh")
    remote = _run_git(public_repo, "remote", "get-url", "origin")
    canonical = lambda value: value.strip().removesuffix(".git").rstrip("/")
    if canonical(remote) != canonical(public_repository):
        raise SnapshotProjectionError(f"origin is not the canonical public repository: {remote}")
    live_tokens = _run_git(public_repo, "ls-remote", "origin", "refs/heads/main").split()
    if len(live_tokens) < 2 or not re.fullmatch(r"[0-9a-f]{40}", live_tokens[0]):
        raise SnapshotProjectionError("could not resolve live origin/main")
    live_sha = live_tokens[0]
    local_sha = _run_git(public_repo, "rev-parse", "HEAD")
    if local_sha != live_sha:
        raise SnapshotProjectionError(f"public-sync HEAD {local_sha} does not equal live origin/main {live_sha}")
    branch = _run_git(public_repo, "branch", "--show-current")
    if branch != "main":
        raise SnapshotProjectionError(f"public-sync checkout must be main, found {branch or 'detached HEAD'}")

    public_files = set(_run_git(public_repo, "ls-tree", "-r", "--name-only", live_sha).splitlines())
    missing = sorted(set(required_public_paths) - public_files)
    if missing:
        raise SnapshotProjectionError("required public paths missing: " + ", ".join(missing))
    for name in packet_files:
        if not (packet_root / name).is_file():
            raise SnapshotProjectionError(f"packet file missing: {name}")
    if not owner_index_source.is_file():
        raise SnapshotProjectionError(f"owner index source missing: {owner_index_source}")

    commit_date = _run_git(public_repo, "show", "-s", "--format=%cI", live_sha)
    subject = _run_git(public_repo, "show", "-s", "--format=%s", live_sha)
    stamp = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh"))
    snapshot = packet_root / "CVF_CURRENT_PUBLIC_SNAPSHOT.md"
    snapshot_text = update_snapshot_metadata(
        snapshot.read_text(encoding="utf-8"), protocol_version=protocol_version,
        sha=live_sha, commit_date=commit_date, subject=subject,
        tree_count=len(public_files), snapshot_date=stamp.date().isoformat(),
    )
    snapshot.write_text(project_current_public_posture(snapshot_text, public_repo), encoding="utf-8", newline="\n")
    local_owner_index = packet_root / "CVF_PUBLIC_OWNER_SURFACE_INDEX.json"
    shutil.copyfile(owner_index_source, local_owner_index)
    receipt = {
        "schema": "cvf.externalAgentPacketRefreshReceipt.v1",
        "protocolVersion": protocol_version,
        "status": "REFRESHED_LIVE_PUBLIC_MAIN",
        "verifiedAt": stamp.isoformat(timespec="seconds"),
        "publicRepository": public_repository,
        "publicBranch": "main",
        "publicCommit": live_sha,
        "publicCommitDate": commit_date,
        "publicCommitSubject": subject,
        "publicTreeEntries": len(public_files),
        "publicPostureSourceHashes": _hashes(
            public_repo, ["README.md", "CHANGELOG.md", "docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md"],
        ),
        "packetRoot": str(packet_root.resolve()),
        "packetFileHashes": _hashes(packet_root, [*packet_files, local_owner_index.name]),
        "claimBoundary": "Proves packet refresh against live public main only; no push, CI, provider, runtime, or production claim.",
    }
    receipt_path = packet_root / "CVF_EXTERNAL_AGENT_PACKET_REFRESH_RECEIPT.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return receipt
