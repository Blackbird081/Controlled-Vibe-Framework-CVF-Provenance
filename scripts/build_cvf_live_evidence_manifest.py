#!/usr/bin/env python3
"""Build a secret-safe manifest for CVF live evidence artifacts."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def file_record(path: Path) -> dict[str, Any]:
    resolved = path.resolve()
    if not resolved.exists() or not resolved.is_file():
        raise FileNotFoundError(f"evidence file not found: {path}")
    try:
        rel = resolved.relative_to(REPO_ROOT)
        display_path = rel.as_posix()
    except ValueError:
        display_path = str(resolved)
    data = resolved.read_bytes()
    return {
        "path": display_path,
        "sizeBytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def canonical_json(data: dict[str, Any]) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")


def build_manifest(args: argparse.Namespace) -> dict[str, Any]:
    evidence = [file_record(Path(item)) for item in args.evidence]
    manifest: dict[str, Any] = {
        "schema": "cvf.liveEvidenceManifest.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "repository": {
            "remoteOrigin": run_git(["remote", "get-url", "origin"]),
            "branch": run_git(["branch", "--show-current"]),
            "commit": run_git(["rev-parse", "HEAD"]),
            "dirtyStatus": run_git(["status", "--short"]),
        },
        "rerun": {
            "command": args.command,
            "requiresLiveProviderKey": True,
            "acceptedSecretEnv": [
                "DASHSCOPE_API_KEY",
                "ALIBABA_API_KEY",
                "CVF_ALIBABA_API_KEY",
                "CVF_BENCHMARK_ALIBABA_KEY",
            ],
        },
        "evidence": evidence,
        "externalAnchor": {
            "anchorId": args.anchor_id or "",
            "anchorUrl": args.anchor_url or "",
            "status": "PROVIDED" if args.anchor_id or args.anchor_url else "NOT_PROVIDED",
        },
        "claimBoundary": (
            "Manifest records file hashes, rerun command, repo commit, and optional HMAC. "
            "It does not prove third-party execution unless an external anchor is provided."
        ),
    }

    signing_key = os.environ.get("CVF_AUDIT_SIGNING_KEY", "").strip()
    if signing_key:
        digest = hmac.new(signing_key.encode("utf-8"), canonical_json(manifest), hashlib.sha256).hexdigest()
        manifest["signature"] = {
            "algorithm": "hmac-sha256",
            "status": "SIGNED",
            "digest": digest,
        }
    else:
        manifest["signature"] = {
            "algorithm": "hmac-sha256",
            "status": "UNSIGNED",
            "digest": "",
        }
    return manifest


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", action="append", required=True, help="Evidence artifact path. Repeatable.")
    parser.add_argument("--command", required=True, help="Secret-safe command needed to reproduce the run.")
    parser.add_argument("--output", required=True, help="Manifest JSON output path.")
    parser.add_argument("--anchor-id", default="", help="Optional external immutable anchor identifier.")
    parser.add_argument("--anchor-url", default="", help="Optional external immutable anchor URL.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    manifest = build_manifest(args)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
