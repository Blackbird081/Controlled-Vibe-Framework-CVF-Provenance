#!/usr/bin/env python3
"""Build the deterministic LHW-RESCAN-C Legacy partial-roots manifest."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOTS = (
    REPO_ROOT / ".private_reference" / "legacy" / "CVF ADD",
    REPO_ROOT / ".private_reference" / "legacy" / "CVF 16.5",
    REPO_ROOT / ".private_reference" / "legacy" / "CVF_Restructure",
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "docs"
    / "audits"
    / "CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json"
)

TEXT_EXTENSIONS = {"", ".md", ".ts", ".json", ".py", ".yaml", ".yml", ".txt"}
KEYWORDS = (
    "adapter",
    "agent",
    "approval",
    "architecture",
    "artifact",
    "audit",
    "boundary",
    "capability",
    "checkpoint",
    "cli",
    "context",
    "database",
    "delegation",
    "diagnostic",
    "evidence",
    "execution",
    "gateway",
    "governance",
    "graph",
    "guard",
    "handoff",
    "knowledge",
    "learning",
    "mcp",
    "memory",
    "model",
    "non-coder",
    "operator",
    "policy",
    "provider",
    "receipt",
    "reinject",
    "risk",
    "runtime",
    "sandbox",
    "skill",
    "strategy",
    "trace",
    "workflow",
)

LANE_LABELS = {
    "capability_tool_intake": "R1 capability/tool intake",
    "memory_knowledge_graph": "R2 memory/knowledge/graph",
    "context_continuity": "R3 context/continuity",
    "agent_orchestration": "R4 agent orchestration",
    "execution_runtime_provider": "R5 execution/runtime/provider",
    "governance_policy_evidence": "R6 governance/policy/evidence",
    "product_noncoder": "R7 product/non-coder",
    "strategy_topology": "R8 strategy/topology",
}

FAMILY_PRIMARY_REGION = {
    "CVF ADD/AGENT ENGINEER": "capability_tool_intake",
    "CVF ADD/Agent Harnesses": "context_continuity",
    "CVF ADD/AI-first vs Human-first": "governance_policy_evidence",
    "CVF ADD/caveman": "context_continuity",
    "CVF ADD/CLI-Anything": "capability_tool_intake",
    "CVF ADD/code-review-graph": "memory_knowledge_graph",
    "CVF ADD/cortex-hub": "memory_knowledge_graph",
    "CVF ADD/deepagents": "agent_orchestration",
    "CVF ADD/gridex": "execution_runtime_provider",
    "CVF ADD/Hermes Agent": "agent_orchestration",
    "CVF ADD/Hugging Face": "capability_tool_intake",
    "CVF ADD/Human System Harness": "product_noncoder",
    "CVF ADD/openrouter-cli.git": "execution_runtime_provider",
    "CVF ADD/REVIEW FOLDER": "governance_policy_evidence",
    "CVF ADD/Workflow GoClaw": "context_continuity",
    "CVF 16.5/abtop": "execution_runtime_provider",
    "CVF 16.5/agentmemory": "memory_knowledge_graph",
    "CVF 16.5/Claude Kit": "agent_orchestration",
    "CVF 16.5/free Claude Code": "execution_runtime_provider",
    "CVF 16.5/freellmapi": "execution_runtime_provider",
    "CVF 16.5/md2html": "product_noncoder",
    "CVF 16.5/Memento-Skills": "memory_knowledge_graph",
    "CVF 16.5/OpenAgentd": "agent_orchestration",
    "CVF 16.5/OpenSpec": "governance_policy_evidence",
    "CVF 16.5/pancake-pos-mcp": "capability_tool_intake",
    "CVF 16.5/REVIEW FOLDER": "governance_policy_evidence",
    "CVF 16.5/tolaria": "memory_knowledge_graph",
    "CVF_Restructure/(root files)": "product_noncoder",
    "CVF_Restructure/CVF_AI Systems": "strategy_topology",
    "CVF_Restructure/CVF_ECOSYSTEM": "strategy_topology",
    "CVF_Restructure/Independent Review": "strategy_topology",
}

REGION_KEYWORDS = {
    "capability_tool_intake": {"capability", "skill", "mcp", "cli", "tool", "sandbox", "approval"},
    "memory_knowledge_graph": {"memory", "knowledge", "graph", "retriev", "reinject", "drift"},
    "context_continuity": {"context", "checkpoint", "handoff", "continuity", "profile", "cache"},
    "agent_orchestration": {"agent", "delegation", "worker", "subagent", "scheduler", "mailbox"},
    "execution_runtime_provider": {"execution", "runtime", "provider", "gateway", "database", "quota"},
    "governance_policy_evidence": {"governance", "policy", "guard", "receipt", "audit", "evidence", "risk"},
    "product_noncoder": {"non-coder", "operator", "brief", "artifact", "renderer", "dashboard"},
    "strategy_topology": {"strategy", "roadmap", "architecture", "ecosystem", "layer", "doctrine"},
}


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return _sha256(encoded)


def _snapshot_time(value: str | None) -> str:
    if value:
        return value
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _source_family(root: Path, relative: str) -> str:
    parts = relative.split("/")
    if root.name == "CVF_Restructure" and len(parts) == 1:
        return "(root files)"
    return parts[0] if len(parts) > 1 else "(root files)"


def _read_signal(data: bytes, relative: str) -> tuple[str, int, list[str], str]:
    text = data.decode("utf-8-sig", errors="replace")
    lines = text.splitlines()
    nonempty = [(index + 1, line.strip()) for index, line in enumerate(lines) if line.strip()]
    heading = next(((line_no, line.lstrip("#").strip()) for line_no, line in nonempty if line.startswith("#")), None)
    if heading:
        line_no, signal = heading
    elif nonempty:
        line_no, signal = nonempty[0][0], nonempty[0][1][:180]
    else:
        line_no, signal = 1, "EMPTY_TEXT_ASSET"
    lowered = f"{relative}\n{text}".lower()
    keywords = [keyword for keyword in KEYWORDS if keyword in lowered]
    locator = f"line {line_no}"
    return signal, len(lines), keywords, locator


def _regions_for(family_key: str, relative: str, keywords: list[str]) -> tuple[str, list[str]]:
    primary = FAMILY_PRIMARY_REGION.get(family_key, "governance_policy_evidence")
    haystack = f"{relative} {' '.join(keywords)}".lower()
    regions = {primary}
    for region, needles in REGION_KEYWORDS.items():
        if any(needle in haystack for needle in needles):
            regions.add(region)
    ordered = [primary] + sorted(region for region in regions if region != primary)
    return primary, ordered


def _semantic_summary(ledger: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_region: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in ledger:
        if row["terminalStatus"] == "READ":
            by_region[row["semanticRegion"]].append(row)
    summary: list[dict[str, Any]] = []
    for region in sorted(by_region):
        rows = by_region[region]
        families = Counter(f"{row['sourceRootName']}/{row['topLevelFamily']}" for row in rows)
        cross_links = Counter(link for row in rows for link in row["crossRegionLinks"])
        examples = [
            {
                "path": row["path"],
                "sourceLocator": row["sourceLocator"],
                "extractedSignal": row["extractedSignal"],
            }
            for row in rows[:8]
        ]
        summary.append(
            {
                "semanticRegion": region,
                "label": LANE_LABELS[region],
                "authorityAssets": len(rows),
                "sourceFamilies": dict(sorted(families.items())),
                "crossRegionLinks": dict(sorted(cross_links.items())),
                "representativeExamples": examples,
            }
        )
    return summary


def _build(roots: tuple[Path, ...], snapshot_time: str) -> dict[str, Any]:
    manifest: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    exclusions: list[dict[str, str]] = []
    unreadable: list[dict[str, str]] = []

    for root in roots:
        files = sorted((path for path in root.rglob("*") if path.is_file()), key=lambda path: path.as_posix().lower())
        for path in files:
            relative = path.relative_to(root).as_posix()
            root_name = root.name
            family = _source_family(root, relative)
            family_key = f"{root_name}/{family}"
            extension = path.suffix.lower() or "(none)"
            data = path.read_bytes()
            source_row = {
                "path": path.relative_to(REPO_ROOT).as_posix(),
                "sourceRoot": root.relative_to(REPO_ROOT).as_posix(),
                "sourceRootName": root_name,
                "relativePath": relative,
                "topLevelFamily": family,
                "sourceFamilyKey": family_key,
                "extension": extension,
                "bytes": len(data),
                "sha256": _sha256(data),
            }
            manifest.append(source_row)

            if path.suffix.lower() not in TEXT_EXTENSIONS:
                reason = "Unsupported extension retained visibly; format-specific extraction is demand-gated."
                ledger.append(
                    {
                        **source_row,
                        "terminalStatus": "SKIPPED_WITH_REASON",
                        "parser": "metadata_only",
                        "semanticRegion": "governance_policy_evidence",
                        "deepReviewLane": LANE_LABELS["governance_policy_evidence"],
                        "crossRegionLinks": [],
                        "extractedSignal": reason,
                        "sourceLocator": "N/A with reason: metadata-only unsupported format",
                        "keywords": [],
                    }
                )
                exclusions.append({"path": source_row["path"], "reason": reason})
                continue

            signal, line_count, keywords, locator = _read_signal(data, relative)
            primary, regions = _regions_for(family_key, relative, keywords)
            ledger.append(
                {
                    **source_row,
                    "terminalStatus": "READ",
                    "parser": "utf8_text_with_replacement_visibility",
                    "semanticRegion": primary,
                    "deepReviewLane": LANE_LABELS[primary],
                    "crossRegionLinks": [region for region in regions if region != primary],
                    "extractedSignal": signal,
                    "sourceLocator": locator,
                    "lineCount": line_count,
                    "keywords": keywords,
                }
            )

    root_counts = Counter(row["sourceRootName"] for row in manifest)
    family_counts = Counter(row["sourceFamilyKey"] for row in manifest)
    extension_counts = Counter(row["extension"] for row in manifest)
    status_counts = Counter(row["terminalStatus"] for row in ledger)
    authority_rows = [row for row in ledger if row["terminalStatus"] == "READ"]
    region_counts = Counter(row["semanticRegion"] for row in authority_rows)
    cross_region_counts = Counter(link for row in authority_rows for link in row["crossRegionLinks"])

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
            "ledgerTerminalAssets": sum(1 for row in ledger if row["sourceFamilyKey"] == family),
            "unresolvedAssets": 0,
        }
        for family in sorted(family_counts)
    ]

    authority_assets = len(authority_rows)
    return {
        "schemaVersion": "1.0.0",
        "contractVersion": "cvf.lhwRescanC.legacyPartialRootsManifest.v1",
        "roots": [root.relative_to(REPO_ROOT).as_posix() for root in roots],
        "snapshotTime": snapshot_time,
        "enumeration": {
            "method": "filesystem recursion including hidden and ignored files",
            "powershellEquivalent": 'Get-ChildItem -LiteralPath "<root>" -File -Recurse -Force',
            "ripgrepCrossCheck": 'rg --files --hidden --no-ignore -- "<root>"',
        },
        "manifestHash": _canonical_hash(manifest),
        "ledgerHash": _canonical_hash(ledger),
        "counts": {
            "manifestAssets": len(manifest),
            "sourceRoots": len(root_counts),
            "sourceFamilies": len(family_counts),
            "authorityAssets": authority_assets,
            "declaredExclusions": len(exclusions),
            "unreadableOrUnsupportedFiles": len(unreadable),
            "ledgerTerminalAssets": len(ledger),
            "unresolvedAssets": 0,
            "roots": dict(sorted(root_counts.items())),
            "families": dict(sorted(family_counts.items())),
            "extensions": dict(sorted(extension_counts.items())),
            "terminalStatuses": dict(sorted(status_counts.items())),
            "semanticRegions": dict(sorted(region_counts.items())),
            "crossRegionLinks": dict(sorted(cross_region_counts.items())),
        },
        "knowledgeMap": {
            "authorityAssets": authority_assets,
            "mappedAssets": authority_assets,
            "deferredAssets": 0,
            "unmappedAssets": 0,
            "derivedViews": [
                "semanticRegionSummary",
                "rootReconciliation",
                "familyReconciliation",
                "crossRegionLinks",
            ],
            "rebuildableFrom": ["manifest", "processingLedger"],
        },
        "declaredExclusions": exclusions,
        "unreadableOrUnsupportedFiles": unreadable,
        "rootReconciliation": root_reconciliation,
        "familyReconciliation": family_reconciliation,
        "semanticRegionSummary": _semantic_summary(ledger),
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
    print("semanticRegions=" + json.dumps(counts["semanticRegions"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
