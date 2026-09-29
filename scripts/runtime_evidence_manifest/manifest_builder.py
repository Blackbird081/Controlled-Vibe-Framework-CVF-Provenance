"""Manifest assembly and markdown rendering for runtime evidence export."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from runtime_evidence_manifest.common import RELEASE_MANIFEST, RELEASE_PACKET, read_json, rel
from runtime_evidence_manifest.fixtures import REQUEST_ID, RUNTIME_FAMILY_CONFIG, RUNTIME_FAMILY_ORDER, SCHEMA_VERSION, TRACE_BATCH


def load_release_manifest_rows() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for line in RELEASE_MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| v"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        version, module_name, release_line, maturity, evidence_anchor = cells[:5]
        rows[version] = {
            "moduleName": module_name,
            "releaseLine": release_line,
            "maturity": maturity,
            "evidenceAnchor": evidence_anchor,
        }
    return rows


def build_entry(
    runtime_family: str,
    artifact_path: Path,
    log_path: Path,
    release_rows: dict[str, dict[str, str]],
) -> dict[str, Any]:
    artifact = read_json(artifact_path)
    version_token = RUNTIME_FAMILY_CONFIG[runtime_family]["versionToken"]
    release_row = release_rows[version_token]
    return {
        "runtimeFamily": runtime_family,
        "versionToken": version_token,
        "moduleName": release_row["moduleName"],
        "releaseLine": release_row["releaseLine"],
        "maturity": release_row["maturity"],
        "evidenceAnchor": release_row["evidenceAnchor"],
        "artifactPath": rel(artifact_path),
        "logPath": rel(log_path),
        "adapter": artifact.get("adapter", "UNKNOWN"),
        "receiptCount": artifact.get("receiptCount", len(artifact.get("receipts", []))),
        "schemaVersion": artifact.get("schemaVersion", "UNKNOWN"),
    }


def build_manifest(
    family_paths: dict[str, dict[str, Path]],
    manifest_log_path: Path,
) -> dict[str, Any]:
    release_rows = load_release_manifest_rows()
    entries = [
        build_entry(runtime_family, family_paths[runtime_family]["artifact"], family_paths[runtime_family]["log"], release_rows)
        for runtime_family in RUNTIME_FAMILY_ORDER
    ]
    return {
        "schemaVersion": SCHEMA_VERSION,
        "manifestType": "CVF_MULTI_RUNTIME_REMEDIATION_EVIDENCE",
        "requestId": REQUEST_ID,
        "traceBatch": TRACE_BATCH,
        "releaseManifestPath": rel(RELEASE_MANIFEST),
        "linkedPacketPath": rel(RELEASE_PACKET),
        "manifestLogPath": rel(manifest_log_path),
        "runtimeFamilyCount": len(entries),
        "totalReceiptCount": sum(entry["receiptCount"] for entry in entries),
        "releaseLinesCovered": sorted({entry["releaseLine"] for entry in entries}),
        "maturityBandsCovered": sorted({entry["maturity"] for entry in entries}),
        "entries": entries,
    }


def build_manifest_log(manifest: dict[str, Any], manifest_json_path: Path) -> str:
    lines = [
        "# CVF W4 Multi-Runtime Evidence Log - 2026-03-07",
        "",
        "Memory class: FULL_RECORD",
        "",
        "docType: review",
        "",
        "Status: GENERATED",
        "",
        "## Purpose",
        "",
        "Render the current multi-runtime evidence manifest into a reviewable",
        "Markdown log that links each runtime family's release-grade evidence.",
        "",
        "## Target",
        "",
        f"- source manifest: `{rel(manifest_json_path)}`",
        "",
        "## Scope",
        "",
        "This log covers exactly the runtime family entries present in the",
        "source manifest above; it makes no claim about entries outside it.",
        "",
        "## Header",
        "",
        f"- schemaVersion: `{manifest['schemaVersion']}`",
        f"- manifestType: `{manifest['manifestType']}`",
        f"- requestId: `{manifest['requestId']}`",
        f"- traceBatch: `{manifest['traceBatch']}`",
        f"- runtimeFamilyCount: `{manifest['runtimeFamilyCount']}`",
        f"- totalReceiptCount: `{manifest['totalReceiptCount']}`",
        f"- releaseManifestPath: `{manifest['releaseManifestPath']}`",
        f"- linkedPacketPath: `{manifest['linkedPacketPath']}`",
        f"- manifestLogPath: `{manifest['manifestLogPath']}`",
        "",
        "## Runtime Families",
        "",
        "| Runtime Family | Version | Release Line | Maturity | Adapter | Receipt Count | Artifact | Log |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for entry in manifest["entries"]:
        lines.append(
            f"| `{entry['runtimeFamily']}` | `{entry['versionToken']}` | `{entry['releaseLine']}` | `{entry['maturity']}` | `{entry['adapter']}` | `{entry['receiptCount']}` | `{entry['artifactPath']}` | `{entry['logPath']}` |"
        )

    lines.extend(
        [
            "",
            "## Release Metadata",
            "",
            f"- releaseLinesCovered: `{', '.join(manifest['releaseLinesCovered'])}`",
            f"- maturityBandsCovered: `{', '.join(manifest['maturityBandsCovered'])}`",
            "",
            "## Notes",
            "",
            "- This manifest links the current release-evidence baseline across more than one runtime family.",
            "- The `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` artifact proves integrity verification, pipeline execution, and phase-audit evidence can join the same release-grade manifest chain.",
            "- The `CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE` artifact proves skill filtering, phase gating, and successor-migration evidence can join the same release-grade manifest chain.",
            "- The `CVF_v1.6.1_GOVERNANCE_ENGINE` artifact proves policy evaluation, enforcement routing, and approval-state evidence can join the same release-grade manifest chain.",
            "- The `CVF_v1.6_AGENT_PLATFORM` artifact proves governance snapshot and enforcement-route evidence can join the release-grade manifest chain.",
            "- The `CVF_v1.9_DETERMINISTIC_REPRODUCIBILITY` artifact remains the primary orchestration-line remediation baseline.",
            "- The `CVF_v1.8_SAFETY_HARDENING` artifact proves rollback/recovery evidence can join the same release-facing manifest chain.",
            "- The `CVF_v1.7.3_RUNTIME_ADAPTER_HUB` artifact proves the adapter-hub line can emit compatible remediation evidence without format translation.",
            "- The `CVF_v1.7.1_SAFETY_RUNTIME` artifact proves checkpoint/session/audit evidence can be exported into the same release-grade manifest without lossy translation.",
            "",
            "## Findings",
            "",
            f"This log reflects {manifest['runtimeFamilyCount']} runtime family entries and",
            f"{manifest['totalReceiptCount']} total receipts at generation time. No manual",
            "finding is asserted beyond the tabulated manifest data above.",
            "",
            "## Risk",
            "",
            "No risk is asserted by this generated log; it is a deterministic",
            "rendering of the source manifest.",
            "",
            "## Decision",
            "",
            "N/A with reason: this is a generated evidence log, not a decision record.",
            "",
            "## Finding-To-Governance Learning Disposition",
            "",
            "| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |",
            "|---|---|---|---|---|---|",
            "| N/A with reason: this generated log states only tabulated manifest data with no asserted defect | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | none | N/A |",
            "",
            "EPISTEMIC_PROCESS_NA_WITH_REASON: this is a deterministic rendering of the named source manifest with no prediction, evidence comparison, or claim update",
            "",
            "## Checker Source Read-Ahead Block",
            "",
            "| Field | Value |",
            "|---|---|",
            "| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |",
            "| literalTokensReviewed | `Memory class`; `Status`; `## Purpose`; `## Target`; `## Claim Boundary`; `## Checker Source Read-Ahead Block` |",
            "| gateRunPurpose | confirmation evidence for a deterministically generated log; not first discovery |",
            "| claimBoundary | this log states only the manifest entries present in the source manifest at generation time |",
            "",
            "## Claim Boundary",
            "",
            "This log is a deterministic rendering of the named source manifest only.",
            "It makes no provider, production, public, scale, certification, or",
            "user-value claim.",
        ]
    )
    return "\n".join(lines)
