#!/usr/bin/env python3
"""Build the deterministic LHW-RESCAN-B Legacy small-roots manifest and ledger."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOTS = (
    REPO_ROOT / ".private_reference" / "legacy" / "CVF 17.05",
    REPO_ROOT / ".private_reference" / "legacy" / "CVF 25.05",
    REPO_ROOT / ".private_reference" / "legacy" / "CVF 28.05",
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "docs"
    / "audits"
    / "CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_MANIFEST_2026-06-01.json"
)

TEXT_EXTENSIONS = {"", ".md", ".py", ".yaml", ".yml", ".json", ".txt"}
KEYWORDS = (
    "agent",
    "architecture",
    "audit",
    "capability",
    "cli",
    "context",
    "execution",
    "gateway",
    "governance",
    "graph",
    "guard",
    "knowledge",
    "learning",
    "mcp",
    "memory",
    "model",
    "policy",
    "posture",
    "runtime",
    "skill",
    "trust",
    "workflow",
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return _sha256(encoded)


def _snapshot_time(value: str | None) -> str:
    if value:
        return value
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _read_signal(data: bytes) -> tuple[str, int, list[str]]:
    text = data.decode("utf-8-sig", errors="replace")
    lines = text.splitlines()
    nonempty = [line.strip() for line in lines if line.strip()]
    heading = next((line.lstrip("#").strip() for line in nonempty if line.startswith("#")), "")
    signal = heading or (nonempty[0][:180] if nonempty else "EMPTY_TEXT_ASSET")
    lowered = text.lower()
    keywords = [keyword for keyword in KEYWORDS if keyword in lowered]
    return signal, len(lines), keywords


def _source_family(root_name: str, relative: str) -> str:
    parts = relative.split("/")
    if root_name == "CVF 17.05" and len(parts) > 1:
        return parts[0]
    return "(root files)"


def _semantic_region(root_name: str, family: str, relative: str) -> str:
    lowered = relative.lower()
    if root_name == "CVF 17.05":
        if family == "CVF_EXTERNAL_CAPABILITY_INTAKE":
            return "external_capability_intake"
        return "review_and_architecture"
    if root_name == "CVF 25.05":
        return "operator_feedback"
    if "cli" in lowered or "mcp" in lowered:
        return "cli_and_mcp"
    if "multi-agent" in lowered:
        return "multi_agent"
    if "test" in lowered:
        return "verification_evidence"
    if "posture" in lowered:
        return "governance_posture_configuration"
    return "unclassified_source_region"


def _build(roots: tuple[Path, ...], snapshot_time: str) -> dict[str, Any]:
    manifest: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    exclusions: list[dict[str, str]] = []

    for root in roots:
        files = sorted((path for path in root.rglob("*") if path.is_file()), key=lambda path: path.as_posix().lower())
        for path in files:
            relative = path.relative_to(root).as_posix()
            root_name = root.name
            family = _source_family(root_name, relative)
            extension = path.suffix.lower() or "(none)"
            data = path.read_bytes()
            source_row = {
                "path": path.relative_to(REPO_ROOT).as_posix(),
                "sourceRoot": root.relative_to(REPO_ROOT).as_posix(),
                "sourceRootName": root_name,
                "relativePath": relative,
                "topLevelFamily": family,
                "extension": extension,
                "bytes": len(data),
                "sha256": _sha256(data),
            }
            manifest.append(source_row)

            if path.suffix.lower() not in TEXT_EXTENSIONS:
                reason = "Unsupported binary extension retained visibly; deeper format-specific extraction is demand-gated."
                ledger.append(
                    {
                        **source_row,
                        "terminalStatus": "SKIPPED_WITH_REASON",
                        "parser": "binary_metadata_only",
                        "semanticRegion": "unsupported_artifact_exclusion",
                        "extractedSignal": reason,
                        "keywords": [],
                    }
                )
                exclusions.append({"path": source_row["path"], "reason": reason})
                continue

            signal, line_count, keywords = _read_signal(data)
            ledger.append(
                {
                    **source_row,
                    "terminalStatus": "READ",
                    "parser": "utf8_text_with_replacement_visibility",
                    "semanticRegion": _semantic_region(root_name, family, relative),
                    "extractedSignal": signal,
                    "lineCount": line_count,
                    "keywords": keywords,
                }
            )

    root_counts = Counter(row["sourceRootName"] for row in manifest)
    family_counts = Counter(f"{row['sourceRootName']}/{row['topLevelFamily']}" for row in manifest)
    extension_counts = Counter(row["extension"] for row in manifest)
    status_counts = Counter(row["terminalStatus"] for row in ledger)
    authority_rows = [row for row in ledger if row["terminalStatus"] == "READ"]
    region_counts = Counter(row["semanticRegion"] for row in authority_rows)

    root_reconciliation = [
        {
            "sourceRoot": root,
            "manifestAssets": root_counts[root],
            "ledgerTerminalAssets": sum(1 for row in ledger if row["sourceRootName"] == root),
            "unresolvedAssets": 0,
        }
        for root in sorted(root_counts)
    ]
    family_reconciliation = [
        {
            "sourceFamily": family,
            "manifestAssets": family_counts[family],
            "ledgerTerminalAssets": sum(
                1 for row in ledger if f"{row['sourceRootName']}/{row['topLevelFamily']}" == family
            ),
            "unresolvedAssets": 0,
        }
        for family in sorted(family_counts)
    ]

    authority_assets = len(authority_rows)
    return {
        "schemaVersion": "1.0.0",
        "contractVersion": "cvf.lhwRescanB.legacySmallRootsManifest.v1",
        "roots": [root.relative_to(REPO_ROOT).as_posix() for root in roots],
        "snapshotTime": snapshot_time,
        "enumeration": {
            "method": "filesystem recursion including hidden and ignored files",
            "powershellEquivalent": 'Get-ChildItem -LiteralPath "<root>" -File -Recurse -Force',
        },
        "manifestHash": _canonical_hash(manifest),
        "ledgerHash": _canonical_hash(ledger),
        "counts": {
            "manifestAssets": len(manifest),
            "sourceRoots": len(root_counts),
            "sourceFamilies": len(family_counts),
            "authorityAssets": authority_assets,
            "declaredExclusions": len(exclusions),
            "ledgerTerminalAssets": len(ledger),
            "unresolvedAssets": 0,
            "roots": dict(sorted(root_counts.items())),
            "families": dict(sorted(family_counts.items())),
            "extensions": dict(sorted(extension_counts.items())),
            "terminalStatuses": dict(sorted(status_counts.items())),
            "semanticRegions": dict(sorted(region_counts.items())),
        },
        "knowledgeMap": {
            "authorityAssets": authority_assets,
            "mappedAssets": authority_assets,
            "deferredAssets": 0,
            "unmappedAssets": 0,
            "derivedViews": ["semanticRegions", "rootReconciliation", "familyReconciliation"],
            "rebuildableFrom": ["manifest", "processingLedger"],
        },
        "declaredExclusions": exclusions,
        "unreadableOrUnsupportedFiles": [],
        "rootReconciliation": root_reconciliation,
        "familyReconciliation": family_reconciliation,
        "manifest": manifest,
        "processingLedger": ledger,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--snapshot-time", default=None)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--expected-manifest-hash", default=None)
    args = parser.parse_args()

    roots = tuple(root.resolve() for root in DEFAULT_ROOTS)
    output = args.output.resolve()
    payload = _build(roots, _snapshot_time(args.snapshot_time))
    expected = args.expected_manifest_hash
    if expected and payload["manifestHash"] != expected:
        print(f"STALE_SNAPSHOT expected={expected} actual={payload['manifestHash']}")
        return 2

    if not args.check_only:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts = payload["counts"]
    print(f"manifestHash={payload['manifestHash']}")
    print(f"ledgerHash={payload['ledgerHash']}")
    print(
        "assets={manifestAssets}; roots={sourceRoots}; families={sourceFamilies}; authority={authorityAssets}; "
        "exclusions={declaredExclusions}; terminal={ledgerTerminalAssets}; unresolved={unresolvedAssets}".format(
            **counts
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
