# CVF Corpus Scan Registry

Memory class: FULL_RECORD

Status: ACTIVE

docType: reference

Date: 2026-06-02

Standard: `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`

Guard: `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

Machine registry: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

---

## Scope / Target / Owner Boundary

Applies to: all agents and operators working on any CVF-governed project.
Owner: CVF governance control chain.
Scope: all corpora — legacy, project, policy, company docs, external sources.

## Scope / Applies To

This registry applies to every corpus scan, classification, or absorption task
in CVF and CVF-governed projects. See standard for full scope definition.

## Claim Boundary

Claims: structured index of all scanned corpora with findings and negative
search evidence. Does not claim semantic correctness of entries; production
readiness; complete coverage of all possible corpora.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: establish GC-051 Corpus Scan Registry as a
new CVF governance control. This batch adds a new checker, a new guard file,
new standard, and wires both into the autorun gate and local hook chain.
CLAUDE.md is updated to add GC-051 to Governance Controls to Know.

Protected paths:

- `CLAUDE.md`
- `governance/compat/check_corpus_scan_registry.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

Operator authorization: operator direction on 2026-06-02 to establish a
corpus scan registry as a CVF-wide rule for all agents and projects, with a
dedicated folder, machine registry, standard, guard, and checker.

Rollback boundary: revert all files in this commit if the batch is unwound.
No runtime behavior changes — documentation, guard, checker, and wiring only.

---

## Purpose

Human-readable companion to the JSON registry. Provides a quick overview of
all corpora, their scan status, and key findings — searchable by domain keyword.
Any agent with a task touching a known corpus domain should find the relevant
prior scan here before starting new work.

---

## Quick Lookup: corpus status at-a-glance

| Corpus | Type | Status | Wave | Files | Key findings |
| --- | --- | --- | --- | --- | --- |
| `CVF_Important/Knowledge Base_Graphify/` | LEGACY | SCANNED_WITH_FINDINGS | CI1-T2 | 5 | G-GM-* guard absent; CLI absent; KGR1 partial |
| `CVF_Important/` (broad) | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-A | 230 | Inventory only; Graphify subfamily done |
| `CVF ADD/` | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-C | 167 | `code-review-graph/` is CI1-T3 candidate |
| `CVF 16.5/` | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-C | 100 | Broad routing only |
| `CVF_Restructure/` | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-C | 74 | Broad routing; Independent Review deferred |
| `CVF 17.05 + 25.05 + 28.05` | LEGACY | SCANNED | LHW-RESCAN-B | 38 | Governance decision artifacts; low priority |
| `CVF Edit/` | LEGACY | PARTIALLY_SCANNED | LHW18 | 10 | Integration SDK deferred; GC-047/050 not yet run |
| `App onboarding/` | LEGACY | NOT_STARTED | — | ? | UI design reference; low priority |

---

## Finding Index

Use this index to find prior findings by domain keyword.

### Graph / Knowledge Graph

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| F1-kgr1-partial | `Graphify/` | KGR1 partially absorbed data model + builder; full spec not implemented | ACCEPT_NO_ACTION |
| F2-guard-spec-absent | `Graphify/` | G-GM-01 through G-GM-08 guard IDs absent from CVF TS source | DEFER_WITH_ROADMAP |
| F3-cli-commands-absent | `Graphify/` | `cvf graph build/query/visualize/export/validate/status/purge` absent from CLI | DEFER_PHASED |
| RESCAN-C-code-review-graph | `CVF ADD/` | `code-review-graph/` subfolder (7 files) not yet deep-classified | DEFER_WITH_ROADMAP |

### Performance Claims

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| F4-performance-claim-unverified | `Graphify/` | 71.5x token reduction — author-reported, not CVF-verified | ACCEPT_WITH_BOUNDARY |

### Integration / Adapters

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| LHW18-integration-sdk | `CVF Edit/` | Integration SDK adapters not absorbed; frameworks connect INTO CVF | DEFER_DEMAND_GATED |

---

## Negative Search Evidence Index

Searches that confirmed absence — prevents re-doing the same negative search.

| Term | Search performed | Corpus | Result |
| --- | --- | --- | --- |
| `cvf graph` (CLI) | `rg "cvf graph" --include="*.ts"` in EXTENSIONS/ | Graphify | NOT FOUND |
| `G-GM-0` (guard IDs) | `rg "G-GM-0" --include="*.ts"` | Graphify | NOT FOUND |
| `GraphMemoryRecord` | `rg "GraphMemoryRecord"` | Graphify | NOT FOUND |
| `PreToolUse` hook | `rg "PreToolUse" --include="*.ts"` | Graphify | NOT FOUND in CVF TS source |
| `GRAPH_REPORT` | `rg "GRAPH_REPORT"` | Graphify | NOT FOUND in runtime |
| `NetworkX` / `leiden` | `rg "NetworkX\|leiden"` | Graphify | NOT FOUND |

---

## Next Scan Recommendations

| Priority | Target | Reason |
| --- | --- | --- |
| HIGH | `CVF ADD/code-review-graph/` (7 files) | Directly relates to Finding F2 (graph guard spec); CI1-T3 candidate |
| MEDIUM | `CVF Edit/` — full GC-047/050 scan | Only LHW18 doc-only absorption done; no manifest or classification yet |
| MEDIUM | `CVF_Important/` remaining subfamilies | 230 files inventoried; deep classification pending per-family |
| LOW | `CVF 16.5/` + `CVF_Restructure/` deep scan | Broad routing done; deep classification when operator prioritizes |
| LOW | `App onboarding/` | UI design reference; not a knowledge absorption target |

---

## How to Add a New Entry

1. Add to `CVF_CORPUS_SCAN_REGISTRY.json` (machine truth).
2. Add a row to the Quick Lookup table above.
3. Add any findings to the Finding Index.
4. Add any negative searches to the Negative Search Evidence Index.
5. Add a next scan recommendation row if applicable.
6. Commit both files together in the same governed batch.
