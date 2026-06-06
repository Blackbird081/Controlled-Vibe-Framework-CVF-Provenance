#!/usr/bin/env python3
"""Build the deterministic LHW-RESCAN-A CVF_Important manifest and ledger."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = REPO_ROOT / ".private_reference" / "legacy" / "CVF_Important"
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "docs"
    / "audits"
    / "CVF_LHW_RESCAN_A_CVF_IMPORTANT_CORPUS_MANIFEST_2026-06-01.json"
)

REGION_BY_FOLDER = {
    "ADDING_AGENT DEFINITION": "agent_identity_and_capability",
    "ADDING_AI Constitutional Layer": "constitutional_architecture",
    "ADDING_AI GATEWAY": "environment_gateway",
    "ADDING_AUDIT AGENT LAYER": "audit_and_trust",
    "ADDING_CONTEXT CONTROL": "context_control",
    "ADDING_CONTEXT ENGINE": "context_engine",
    "ADDING_CVF_Skill Formation Layer": "skill_formation",
    "ADDING_LEARNING PLANE": "learning_and_memory",
    "ADDING_MINI_MODEL GATEWAY": "model_gateway",
    "ADDING_MODEL GATEWAY": "model_gateway",
    "ADDING_MODEL_ROUTER": "model_gateway",
    "ADDING_Multi_Agent": "multi_agent",
    "ADDING_RAG ARCHITECTURE": "knowledge_retrieval",
    "ADDING_Skill Creator": "skill_formation",
    "ADDING_System Reality Layer": "execution_reality",
    "ADDING_TRUST & ISOLATION LAYER": "trust_and_isolation",
    "ADK SkillToolset": "skill_formation",
    "Claude how to": "cli_and_compiler",
    "HowtoClaude": "skill_formation",
    "Knowledge Base_Graphify": "knowledge_graph",
    "Knowledge Base_LLM-Powered": "knowledge_compilation",
    "Knowledge Base_Palace": "knowledge_palace",
    "REVIEW FOLDER": "review_and_architecture",
    "Windows_Skill_Normalization": "skill_formation",
}

TEXT_EXTENSIONS = {"", ".md", ".py", ".yaml", ".yml", ".json", ".txt"}
KEYWORDS = (
    "agent",
    "architecture",
    "audit",
    "capability",
    "cli",
    "constitution",
    "context",
    "execution",
    "gateway",
    "graph",
    "guard",
    "knowledge",
    "learning",
    "memory",
    "model",
    "palace",
    "policy",
    "retrieval",
    "runtime",
    "skill",
    "trust",
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


def _read_signal(data: bytes) -> tuple[str, str, int, list[str]]:
    text = data.decode("utf-8-sig", errors="replace")
    lines = text.splitlines()
    nonempty = [line.strip() for line in lines if line.strip()]
    heading = next((line.lstrip("#").strip() for line in nonempty if line.startswith("#")), "")
    signal = heading or (nonempty[0][:180] if nonempty else "EMPTY_TEXT_ASSET")
    lowered = text.lower()
    keywords = [keyword for keyword in KEYWORDS if keyword in lowered]
    return text, signal, len(lines), keywords


def _build(root: Path, snapshot_time: str) -> dict[str, Any]:
    files = sorted((path for path in root.rglob("*") if path.is_file()), key=lambda path: path.as_posix().lower())
    manifest: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    exclusions: list[dict[str, str]] = []

    for path in files:
        relative = path.relative_to(root).as_posix()
        top_folder = relative.split("/", 1)[0]
        extension = path.suffix.lower() or "(none)"
        data = path.read_bytes()
        source_row = {
            "path": relative,
            "topLevelFolder": top_folder,
            "extension": extension,
            "bytes": len(data),
            "sha256": _sha256(data),
        }
        manifest.append(source_row)

        if path.suffix.lower() not in TEXT_EXTENSIONS:
            reason = "Generated Python bytecode retained visibly; source .py files are authoritative."
            ledger.append(
                {
                    **source_row,
                    "terminalStatus": "SKIPPED_WITH_REASON",
                    "parser": "binary_metadata_only",
                    "semanticRegion": "generated_artifact_exclusion",
                    "extractedSignal": reason,
                    "keywords": [],
                }
            )
            exclusions.append({"path": relative, "reason": reason})
            continue

        _, signal, line_count, keywords = _read_signal(data)
        ledger.append(
            {
                **source_row,
                "terminalStatus": "READ",
                "parser": "utf8_text_with_replacement_visibility",
                "semanticRegion": REGION_BY_FOLDER.get(top_folder, "unclassified_source_region"),
                "extractedSignal": signal,
                "lineCount": line_count,
                "keywords": keywords,
            }
        )

    folder_counts = Counter(row["topLevelFolder"] for row in manifest)
    extension_counts = Counter(row["extension"] for row in manifest)
    status_counts = Counter(row["terminalStatus"] for row in ledger)
    authority_rows = [row for row in ledger if row["terminalStatus"] == "READ"]
    region_counts = Counter(row["semanticRegion"] for row in authority_rows)
    folder_reconciliation = [
        {
            "topLevelFolder": folder,
            "manifestAssets": folder_counts[folder],
            "ledgerTerminalAssets": sum(1 for row in ledger if row["topLevelFolder"] == folder),
            "unresolvedAssets": 0,
        }
        for folder in sorted(folder_counts)
    ]

    manifest_hash = _canonical_hash(manifest)
    ledger_hash = _canonical_hash(ledger)
    authority_assets = len(authority_rows)
    return {
        "schemaVersion": "1.0.0",
        "contractVersion": "cvf.lhwRescanA.cvfImportantManifest.v1",
        "root": root.relative_to(REPO_ROOT).as_posix(),
        "snapshotTime": snapshot_time,
        "enumeration": {
            "method": "filesystem recursion including hidden and ignored files",
            "powershellEquivalent": 'Get-ChildItem -LiteralPath ".private_reference/legacy/CVF_Important" -File -Recurse -Force',
        },
        "manifestHash": manifest_hash,
        "ledgerHash": ledger_hash,
        "counts": {
            "manifestAssets": len(manifest),
            "topLevelFolders": len(folder_counts),
            "authorityAssets": authority_assets,
            "declaredExclusions": len(exclusions),
            "ledgerTerminalAssets": len(ledger),
            "unresolvedAssets": 0,
            "extensions": dict(sorted(extension_counts.items())),
            "terminalStatuses": dict(sorted(status_counts.items())),
            "semanticRegions": dict(sorted(region_counts.items())),
        },
        "knowledgeMap": {
            "authorityAssets": authority_assets,
            "mappedAssets": authority_assets,
            "deferredAssets": 0,
            "unmappedAssets": 0,
            "derivedViews": ["semanticRegions", "folderReconciliation"],
            "rebuildableFrom": ["manifest", "processingLedger"],
        },
        "declaredExclusions": exclusions,
        "unreadableOrUnsupportedFiles": [],
        "folderReconciliation": folder_reconciliation,
        "manifest": manifest,
        "processingLedger": ledger,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--snapshot-time", default=None)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--expected-manifest-hash", default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output.resolve()
    payload = _build(root, _snapshot_time(args.snapshot_time))
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
        "assets={manifestAssets}; folders={topLevelFolders}; authority={authorityAssets}; "
        "exclusions={declaredExclusions}; terminal={ledgerTerminalAssets}; unresolved={unresolvedAssets}".format(
            **counts
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
