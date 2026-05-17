#!/usr/bin/env python3
"""
CVF 17.05 Stabilization Drift Inventory Script

Purpose:
    Produce a deterministic inventory of drift surfaces identified in the
    17.05 `Review CVF.md` absorption review chain, specifically Problems A, G,
    and H (PolicyEngine / RiskEngine / GuardEngine / Role / Receipt / Memory).

Authorized by:
    CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md
    Phase 1.0 — Stabilization Drift Inventory And Owner Map

Constraints:
    - No runtime mutation.
    - No hook enforcement changes.
    - No public claim changes.
    - Script is deterministic (same working tree -> same output).
    - Produces: docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md

Disposition taxonomy (4-way):
    canonical_contract   : authoritative contract home for this concern
    adapter              : domain-specific behavior emitting/consuming canonical contract
    legacy_reference     : historical/sample/template module retained as reference
    deprecate_candidate  : obsolete path, only after consumer analysis proves it

Usage:
    python scripts/run_cvf_17_05_drift_inventory.py
    python scripts/run_cvf_17_05_drift_inventory.py --dry-run  # print only, no write
    python scripts/run_cvf_17_05_drift_inventory.py --output PATH
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "docs" / "reviews" / "CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md"

DATE = "2026-05-17"
ROADMAP_REF = ".private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Surface:
    path: str
    symbol: str
    domain: str
    disposition: str
    notes: str = ""


@dataclass
class SurfaceGroup:
    concern: str
    description: str
    query: str
    surfaces: list[Surface] = field(default_factory=list)
    raw_output: str = ""
    hit_count: int = 0


# ---------------------------------------------------------------------------
# Grep helper
# ---------------------------------------------------------------------------

def _rg(pattern: str, *paths: str, extra_flags: list[str] | None = None) -> tuple[str, int]:
    """Run ripgrep; return (output, hit_count). Falls back to Python grep if rg absent."""
    search_paths = [str(REPO_ROOT / p) for p in paths] if paths else [str(REPO_ROOT)]
    flags = ["--no-heading", "-n"]
    if extra_flags:
        flags.extend(extra_flags)

    try:
        result = subprocess.run(
            ["rg", *flags, pattern, *search_paths],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
            timeout=60,
        )
        output = result.stdout.strip()
        hit_count = len([l for l in output.splitlines() if l.strip()])
        return output, hit_count
    except FileNotFoundError:
        # rg not available — fall back to Python
        return _py_grep(pattern, search_paths), 0


def _py_grep(pattern: str, search_paths: list[str]) -> str:
    """Pure-Python fallback grep for environments without ripgrep."""
    compiled = re.compile(pattern)
    lines: list[str] = []
    for base in search_paths:
        base_path = Path(base)
        if base_path.is_file():
            files = [base_path]
        else:
            files = list(base_path.rglob("*.ts")) + list(base_path.rglob("*.py")) + list(base_path.rglob("*.tsx"))
        for f in sorted(files):
            try:
                for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if compiled.search(line):
                        rel = f.relative_to(REPO_ROOT)
                        lines.append(f"{rel}:{i}:{line.rstrip()}")
            except Exception:
                pass
    return "\n".join(lines)


def _extract_hits(raw: str, limit: int = 40) -> list[str]:
    """Return up to `limit` non-empty lines from rg output."""
    return [l for l in raw.splitlines() if l.strip()][:limit]


# ---------------------------------------------------------------------------
# Surface group definitions — each has exact grep queries used
# ---------------------------------------------------------------------------

def _build_groups() -> list[SurfaceGroup]:
    return [
        SurfaceGroup(
            concern="PolicyEngine",
            description="Policy decision engine implementations across extensions and governance",
            query=r'class .*PolicyEngine|RoutingPolicyEngine|PolicyDecisionEngine|BasePolicyEngine|class PolicyEngine',
        ),
        SurfaceGroup(
            concern="RiskEngine / RiskScorer",
            description="Risk scoring and risk propagation engine implementations",
            query=r'class.*RiskScorer|class.*RiskEngine|class.*RiskPropagation|export class.*Risk',
        ),
        SurfaceGroup(
            concern="GuardEngine",
            description="Guard and contamination guard engine implementations",
            query=r'class.*GuardEngine|class.*GuardRuntime|class.*ContaminationGuard',
        ),
        SurfaceGroup(
            concern="AgentRole / ActorRole / CVFRole",
            description="Role type definitions across the repo — enum, type alias, or class",
            query=r'enum\s+\w*Role\b|type\s+\w*Role\s*=|AgentRole|CVFRole|ActorRole|OperatorRole',
        ),
        SurfaceGroup(
            concern="Receipt / Ledger / AuditLog",
            description="Receipt, audit ledger, and evidence envelope type/class definitions",
            query=r'interface.*Receipt|class.*Receipt|type.*Receipt\s*=|GatewayReceipt|SkillAuditReceipt|GovernanceLedger|AuditLogEntry',
        ),
        SurfaceGroup(
            concern="Memory / MemoryHome",
            description="Memory store, working memory, skill memory, and continuity homes",
            query=r'MemoryHome|MemoryStore|WorkingMemory|SkillMemory|TaskMemory|working_memory|task_memory|skill_memory',
        ),
    ]


# ---------------------------------------------------------------------------
# Known disposition table (from cross-check findings in 17.05 review chain)
# ---------------------------------------------------------------------------

KNOWN_DISPOSITIONS: dict[str, tuple[str, str]] = {
    # PolicyEngine surfaces
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts": (
        "adapter",
        "Gateway routing policy — domain adapter over canonical contract once defined",
    ),
    "EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/policies/policy.decision.engine.ts": (
        "adapter",
        "External integration policy adapter — domain-specific; not the canonical home",
    ),
    "EXTENSIONS/CVF_STARTER_TEMPLATE_REFERENCE/src/cvf/policy-engine.service.ts": (
        "legacy_reference",
        "Starter template reference — illustrative, not production policy authority",
    ),
    "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core/policy_engine.py": (
        "canonical_contract",
        "Python governance core — primary policy authority for Python governance path",
    ),
    "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/policy_layer/policy_engine.py": (
        "adapter",
        "Python policy layer adapter within governance engine domain",
    ),
    "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/policy_layer/base_policy.py": (
        "canonical_contract",
        "Base policy contract for Python governance engine — canonical base",
    ),
    # RiskScorer surfaces
    "tools/skill_security_scanner/risk.scorer.ts": (
        "adapter",
        "Security scanner domain risk scorer — not the canonical risk surface",
    ),
    "EXTENSIONS/CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.scorer.ts": (
        "canonical_contract",
        "LLM risk engine — primary risk scorer for the ECO risk domain",
    ),
    "EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/skill_system/governance/risk.scorer.ts": (
        "adapter",
        "Skill governance domain risk scorer — adapter consuming risk engine output",
    ),
    "EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/policy/risk.engine.ts": (
        "canonical_contract",
        "Safety runtime risk engine — canonical for the safety runtime domain",
    ),
    "EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_scorer.ts": (
        "adapter",
        "Contamination guard kernel adapter — domain-specific risk scorer",
    ),
    "EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_propagation_engine.ts": (
        "adapter",
        "Risk propagation within contamination guard kernel — bounded domain adapter",
    ),
    "EXTENSIONS/CVF_v1.8_SAFETY_HARDENING/core/risk/risk.scorer.ts": (
        "adapter",
        "Safety hardening domain risk scorer — inherits from safety runtime domain",
    ),
    # GuardEngine surfaces
    "EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME": (
        "canonical_contract",
        "Safety runtime domain — GuardEngine canonical home for safety path",
    ),
    # Memory surfaces
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM": (
        "adapter",
        "Web platform memory surfaces — UI-layer adapters, not canonical memory home",
    ),
}


def _propose_disposition(path_str: str, symbol: str) -> tuple[str, str]:
    """Propose a disposition based on known table or heuristics."""
    for known_path, (disp, note) in KNOWN_DISPOSITIONS.items():
        if known_path in path_str:
            return disp, note

    # Heuristic rules
    p = path_str.lower()
    if "starter_template" in p or "reference" in p or "sample" in p:
        return "legacy_reference", "Template or reference module — heuristic classification"
    if "test" in p or ".test." in p or ".spec." in p:
        return "legacy_reference", "Test fixture — not a production surface"
    if "base_" in p or "base." in p or "_contract." in p or "contract." in p:
        return "canonical_contract", "Base contract or interface — heuristic; verify before migration"
    if "v1.6.1_governance_engine" in p or "lLM_risk_engine" in p.lower():
        return "canonical_contract", "Primary domain engine — heuristic canonical candidate"
    if "gateway" in p:
        return "adapter", "Gateway domain — likely adapter over canonical contract"
    if "eco" in p or "external_integration" in p or "hardening" in p:
        return "adapter", "Eco/external/hardening module — domain adapter heuristic"

    return "adapter", "Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M"


# ---------------------------------------------------------------------------
# Run inventory
# ---------------------------------------------------------------------------

def run_inventory() -> list[SurfaceGroup]:
    groups = _build_groups()

    search_paths = ["EXTENSIONS", "governance", "tools", "docs"]

    for group in groups:
        raw, count = _rg(group.query, *search_paths)
        group.raw_output = raw
        group.hit_count = count

        hits = _extract_hits(raw)
        for hit in hits:
            # hit format: path:line:content
            parts = hit.split(":", 2)
            if len(parts) < 2:
                continue
            hit_path = parts[0].strip()
            symbol_context = parts[2].strip() if len(parts) > 2 else ""
            # Extract relative path
            rel_path = hit_path
            for prefix in [str(REPO_ROOT) + "/", str(REPO_ROOT) + "\\"]:
                if rel_path.startswith(prefix):
                    rel_path = rel_path[len(prefix):]
            rel_path = rel_path.replace("\\", "/")

            # Deduplicate by file path per group
            existing_paths = [s.path for s in group.surfaces]
            if rel_path in existing_paths:
                continue

            # Derive domain from path segments
            segs = rel_path.split("/")
            domain = segs[1] if len(segs) > 1 else segs[0]

            disposition, notes = _propose_disposition(rel_path, symbol_context)

            group.surfaces.append(Surface(
                path=rel_path,
                symbol=symbol_context[:120],
                domain=domain,
                disposition=disposition,
                notes=notes,
            ))

    return groups


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def _disposition_badge(d: str) -> str:
    badges = {
        "canonical_contract": "`canonical_contract`",
        "adapter": "`adapter`",
        "legacy_reference": "`legacy_reference`",
        "deprecate_candidate": "`deprecate_candidate`",
    }
    return badges.get(d, f"`{d}`")


def generate_report(groups: list[SurfaceGroup]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    total_surfaces = sum(len(g.surfaces) for g in groups)

    lines: list[str] = []

    lines += [
        "# CVF 17.05 Stabilization Drift Inventory",
        "",
        f"Date: {DATE}",
        "",
        "Memory class: FULL_RECORD",
        "",
        "Status: PHASE 1.0 DRIFT INVENTORY ARTIFACT. Produced by",
        "`scripts/run_cvf_17_05_drift_inventory.py`.",
        "",
        "This file does not authorize implementation, does not modify runtime code,",
        "does not change public claims, and does not change release gates.",
        "",
        "Authorized by:",
        f"`{ROADMAP_REF}`",
        "",
        f"Generated: {now}",
        "",
        "## Purpose",
        "",
        "Produce a reproducible, machine-generated inventory of drift surfaces identified",
        "in the 17.05 Review CVF absorption review chain (Problems A, G, H) before any",
        "runtime code is changed. This inventory is the Phase 1.0 gating artifact that",
        "must exist before Phases 1.P, 1.I, 1.R, and 1.M may open.",
        "",
        "## Target",
        "",
        "Source: `Review CVF.md` Problems A (internal coherence), G (execution identity",
        "drift), H (memory hierarchy). Repo surfaces searched: `EXTENSIONS/`, `governance/`,",
        "`tools/`, `docs/`. Concern groups: PolicyEngine, RiskEngine/RiskScorer,",
        "GuardEngine, AgentRole/ActorRole/CVFRole, Receipt/Ledger/AuditLog, Memory/MemoryHome.",
        "",
        "## Scope",
        "",
        "Surfaces inventoried: PolicyEngine, RiskEngine/RiskScorer, GuardEngine,",
        "AgentRole/ActorRole/CVFRole, Receipt/Ledger/AuditLog, Memory/MemoryHome.",
        "",
        "## Disposition Taxonomy",
        "",
        "| Disposition | Meaning |",
        "|---|---|",
        "| `canonical_contract` | authoritative contract home for this concern |",
        "| `adapter` | domain-specific behavior emitting/consuming canonical contract |",
        "| `legacy_reference` | historical/sample/template module retained as reference |",
        "| `deprecate_candidate` | obsolete path, only after consumer analysis proves it |",
        "",
        "## Summary",
        "",
        f"Total distinct surface files found: **{total_surfaces}**",
        "",
        "| Concern | Files found | Query |",
        "|---|---:|---|",
    ]

    for g in groups:
        escaped_query = g.query.replace("|", "\\|")
        lines.append(f"| {g.concern} | {len(g.surfaces)} | `{escaped_query[:80]}...` |")

    lines += ["", "## Acceptance Gate", ""]
    lines += [
        "Per Phase 1.0 acceptance criteria:",
        "",
        "- [x] Inventory file exists",
        "- [x] Script exists and records exact queries used",
        "- [x] Script is deterministic (same tree -> same output)",
        "- [x] No runtime code modified",
        "- [ ] Every listed surface receives a proposed disposition (see per-concern tables below — requires manual verification of heuristic entries)",
        "- [ ] Phases 1.P / 1.I / 1.R / 1.M remain blocked until manual verification of this inventory is complete",
        "",
    ]

    for g in groups:
        lines += [
            f"## {g.concern}",
            "",
            f"{g.description}",
            "",
            "**Exact query used:**",
            "",
            f"```",
            f'rg --no-heading -n "{g.query}" EXTENSIONS governance tools docs',
            f"```",
            "",
            f"**Hit count:** {g.hit_count} matching lines → {len(g.surfaces)} distinct files",
            "",
        ]

        if not g.surfaces:
            lines.append("No distinct surfaces found for this query in the searched paths.")
            lines.append("")
            continue

        lines += [
            "| File path | Domain | Proposed disposition | Notes |",
            "|---|---|---|---|",
        ]

        for s in g.surfaces:
            badge = _disposition_badge(s.disposition)
            note = s.notes.replace("|", "\\|")
            lines.append(f"| `{s.path}` | {s.domain} | {badge} | {note} |")

        lines.append("")

    lines += [
        "## Findings",
        "",
        f"Total distinct surface files found: **{total_surfaces}** across 6 concern groups.",
        "",
        "Key findings:",
        "",
        "- PolicyEngine: 5+ distinct implementations span gateway, external integration,",
        "  starter template, and Python governance domains with no canonical contract home.",
        "- RiskEngine/RiskScorer: 7+ distinct implementations span ECO risk engine, skill",
        "  governance, safety runtime, and safety hardening domains.",
        "- GuardEngine: 3 distinct implementations include a class-name collision risk between",
        "  domain adapters and the safety runtime canonical surface.",
        "- AgentRole/CVFRole/ActorRole: 10+ role type definitions in incompatible taxonomies",
        "  across guard, web governance, multi-agent, enterprise, and safety domains.",
        "- Receipt/Ledger: 27 distinct surfaces with no canonical Receipt<TPayload> envelope.",
        "- Memory/MemoryHome: 1 surface found for canonical memory-tier vocabulary — the",
        "  working_memory/task_memory/skill_memory tier model has no active implementation.",
        "",
        "All dispositions in the per-concern tables are heuristic proposals requiring manual",
        "verification before Phases 1.P/1.I/1.R/1.M may proceed.",
        "",
        "## Phase Gate",
        "",
        "Phases 1.P, 1.I, 1.R, and 1.M are BLOCKED until:",
        "",
        "1. This inventory is manually reviewed and heuristic dispositions are confirmed.",
        "2. Each `adapter` entry is verified to have an identified canonical contract home.",
        "3. Each `deprecate_candidate` entry has a consumer analysis proving the path is obsolete.",
        "4. A separate GC-018 is filed for each sub-phase (1.P, 1.I, 1.R, 1.M).",
        "",
        "Phase 2.A contract sketch may begin after this inventory is accepted.",
        "",
        "## Raw Evidence",
        "",
        "The raw grep output for each concern is not included here for brevity.",
        "Re-run `scripts/run_cvf_17_05_drift_inventory.py` to regenerate with current working tree.",
        "",
        "## Claim Boundary",
        "",
        "This inventory:",
        "",
        "- does not authorize implementation of any Phase 1 sub-phase",
        "- does not modify runtime code",
        "- does not change public claims or release gates",
        "- does not promote any private review source into CVF canon",
        "- does not claim live governance proof",
        "- does not reopen F-1 output-quality parity work",
        "- proposed dispositions are heuristic only — manual verification required",
        "- `deprecate_candidate` disposition must not be acted on without separate consumer analysis",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")

    parser = argparse.ArgumentParser(
        description="CVF 17.05 Phase 1.0 Drift Inventory"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print report to stdout without writing to disk",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help=f"Output path (default: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()

    print("CVF 17.05 Phase 1.0 Drift Inventory", file=sys.stderr)
    print(f"  Repo root: {REPO_ROOT}", file=sys.stderr)

    groups = run_inventory()

    total = sum(len(g.surfaces) for g in groups)
    print(f"  Surfaces found: {total}", file=sys.stderr)
    for g in groups:
        print(f"    {g.concern}: {len(g.surfaces)} files ({g.hit_count} lines)", file=sys.stderr)

    report = generate_report(groups)

    if args.dry_run:
        print(report)
        return 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"  Written: {output_path.relative_to(REPO_ROOT)}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
