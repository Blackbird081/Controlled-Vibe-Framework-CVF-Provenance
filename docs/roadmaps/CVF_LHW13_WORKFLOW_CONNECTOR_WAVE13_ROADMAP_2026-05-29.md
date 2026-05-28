# CVF LHW13 Workflow Connector Wave 13 Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-29

---

## Authorization / Decision

Authorized by operator direction on 2026-05-29: continuation of the LHW
connector wave pattern. LHW13 runs in parallel with LHW12 (no shared source
dependencies). Source: CVF 25.05 Gop_y.md GAPs 1, 4, 9.

Fresh GC-018:
`docs/baselines/CVF_GC018_LHW13_WORKFLOW_CONNECTOR_WAVE13_2026-05-29.md`

Dispatch status: T1 WORK_ORDER_READY. T2 HOLD until T1 CLOSED_PASS.
T3 HOLD until T1 + T2 CLOSED_PASS.

## Scope / Target / Owner Boundary

Target: three documentation connector specs closing governance-protocol and
boundary-definition gaps.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (new), Fast Lane
audit (new), completion review (new), session continuity update. No
`.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/` source. No receipt envelope
schema. No public-sync repo.

## Purpose

LHW12 closes product-layer gaps (posture tier, pack taxonomy, worker lifecycle).
LHW13 closes governance-protocol gaps from CVF 25.05 Gop_y.md:

- T1 — Agent Reading Protocol Governance Connector
- T2 — Memory Continuity Level Advisory Connector
- T3 — Graph Context Resolver Boundary Connector

None executes agent enforcement, memory reinjection, or graph retrieval.

## Operator Direction

CVF 25.05 Gap 1: CLAUDE.md + AGENTS.md cover reading rules piecemeal; no
connector maps canonical-file × claim-tier × phase-gate → a named
`agentReadingAdvisoryType` for Orchestrators routing incoming agent actions.
CVF 25.05 Gap 4: CVF is at L0/L1 memory; no connector maps
`memorySnapshotAdvisoryType` × `canReinject` × `memoryContextSeedDecayAdvisoryType`
→ `memoryContinuityLevelAdvisoryType` telling Orchestrator what level is active.
CVF 25.05 Gap 9: AIF-B graph modules exist but are not wired; no connector
maps AIF-B `GraphKnowledgeService` boundary × current text-retrieval posture
→ `graphContextResolverBoundaryAdvisoryType` defining phases.

## Authority Chain

- LHW12 roadmap: `docs/roadmaps/CVF_LHW12_WORKFLOW_CONNECTOR_WAVE12_ROADMAP_2026-05-29.md`
  — Status: ACTIVE (parallel wave; no dependency)
- LHW11 roadmap: `docs/roadmaps/CVF_LHW11_WORKFLOW_CONNECTOR_WAVE11_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — `tolaria` trigger at line 129
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Knowledge Absorption Blind-Spot Control Block

Prior surfaces used (all CLOSED_PASS_BOUNDED or runtime-proven at HEAD
`7de75901`):

- `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/graph-schema.ts`

Source families:

| Family | LH1 disposition | LH1 remaining trigger | LHW13 tranche |
| --- | --- | --- | --- |
| `tolaria` | PARTIALLY_ABSORBED | Governed memory snapshot packaging or graph context readout | T2, T3 |

CVF 25.05 gaps (not in LH1):

| Gap | Source | LHW13 tranche |
| --- | --- | --- |
| Gap 1 — Agent Reading Protocol | CVF 25.05 Gop_y.md | T1 |
| Gap 4 — Memory L0-L3 boundary | CVF 25.05 Gop_y.md | T2 |
| Gap 9 — Graph context resolver | CVF 25.05 Gop_y.md | T3 |

Blind-spot verdict: CLEAR.

## Candidate Screen

| Priority | Connector | Existing surfaces | Gap | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Agent Reading Protocol Governance | CLAUDE.md startup acknowledgment; `CVF_SESSION_MEMORY.md` front door; `ACTIVE_SESSION_STATE.json` `requiredFirstReads`; status-tier vocabulary (roadmap/schema-defined/active/proven) in governance docs | No connector maps claim-tier × canonical-file-type × phase-gate state → a named `agentReadingAdvisoryType` that Orchestrators can check to route agent action (e.g. "this agent claimed X but X is only schema-defined, not runtime-proven"). Gap 1: "CVF has rules but no single binding protocol connector." | ACCEPT for T1 |
| 2 | Memory Continuity Level Advisory | LHW8-T1 `memorySnapshotAdvisoryType` (6 values); LHW11-T3 `memoryContextSeedDecayAdvisoryType`; AIF-C `MemoryGatewayDecision.canReinject=false` | CVF is at L0 (receipt-only) + partial L1 (session summary). LHW8-T1 says snapshot advisory; LHW11-T3 says decay advisory. But no connector maps these into a named `memoryContinuityLevelAdvisoryType` (L0/L1/L2/L3) per Gap 4 taxonomy, with `canReinject=false` binding. Orchestrators cannot currently determine what memory continuity level is active. | ACCEPT for T2 |
| 3 | Graph Context Resolver Boundary | AIF-B `GraphKnowledgeService` interface (graph-schema.ts); LH1 `tolaria` trigger; current text-retrieval posture (LHW7-T2 `signalsStillMissing`) | AIF-B graph modules exist but are not wired into any runtime path. No connector maps AIF-B graph capability boundary × current text-retrieval readout → `graphContextResolverBoundaryAdvisoryType` defining which resolution mode (text/project-knowledge/graph-future) is active and what the phase boundary is. Gap 9: "Do not build now, just define boundary." | ACCEPT for T3 |

Rejection log:

- `abtop` — rejected *from this LHW wave* (doc-only scope). NOT permanent.
- `gridex` — rejected *from this LHW wave* (doc-only scope). NOT permanent.
- Operations Cockpit (CVF 25.05 Gap 5) — requires product UX surface; not
  a doc connector. Eligible for separate product roadmap.
- External Capability Admission Expansion (CVF 25.05 Gap 6) — requires MCP/tool
  scope expansion beyond ES1. Eligible for separate extension roadmap.

## Recommended Sequence

### LHW13-T1 — Agent Reading Protocol Governance Connector

Maps: claim-tier vocabulary (`roadmap`/`schema_defined`/`active`/`proven`) ×
canonical-file-type (`session_front_door`/`gc018_baseline`/`completion_review`/
`runtime_source`) × startup acknowledgment status →
`agentReadingAdvisoryType` + `claimValidationAdvisory`

Explicit statement: "This connector does not enforce agent behavior at runtime.
The reading advisory is a governance planning record."

### LHW13-T2 — Memory Continuity Level Advisory Connector

Maps: LHW8-T1 `memorySnapshotAdvisoryType` (6 values) ×
LHW11-T3 `memoryContextSeedDecayAdvisoryType` ×
AIF-C `MemoryGatewayDecision.canReinject` →
`memoryContinuityLevelAdvisoryType` (L0/L1/L2/L3) +
`continuityLevelBoundaryNote` + `canReinject=false` preserved

### LHW13-T3 — Graph Context Resolver Boundary Connector

Maps: AIF-B `GraphKnowledgeService` boundary status (`interface_only`/`wired`/
`active`) × LHW7-T2 `signalsStillMissing` (context completeness) ×
current text-retrieval posture →
`graphContextResolverBoundaryAdvisoryType` +
`activeResolutionMode` (`text_retrieval`/`project_knowledge`/`graph_future`) +
`phaseToNextMode`

## Non-Goals

- Runtime agent protocol enforcement or behavior blocking
- Memory reinjection or `canReinject=true`
- Graph context retrieval execution or `GraphKnowledgeService` route wiring
- L2/L3 memory level activation
- Operations Cockpit UX surface (product scope, separate roadmap)
- External Capability Admission Expansion for MCP/tool/repo (separate roadmap)
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Agent Reading Protocol Governance spec (5 sections) | None |
| T2 | Memory Continuity Level Advisory spec (5 sections) | HOLD until T1 CLOSED_PASS |
| T3 | Graph Context Resolver Boundary spec (5 sections) | HOLD until T1 + T2 CLOSED_PASS |

## Acceptance Criteria

- [ ] T1: claim-tier vocabulary values (4) individually row-verified; no runtime enforcement claimed
- [ ] T2: `memorySnapshotAdvisoryType` (6 values) individually row-verified; `canReinject=false` preserved
- [ ] T3: `GraphKnowledgeService` boundary status values individually row-verified; no graph retrieval execution claimed
- [ ] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [ ] Each spec < 250 lines
- [ ] Both governance gates PASS per tranche

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 7de75901 --head <lhw13-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 7de75901 --head <lhw13-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 7de75901 --head <lhw13-commit> --enforce
```

## Claim Boundary

LHW13 does not claim runtime agent enforcement, memory reinjection, graph
context retrieval execution, MCP transport, tool execution, CLI invocation,
new role taxonomy, RBAC changes, receipt envelope extensions, external skill
ingestion, provider behavior changes, hosted readiness, production readiness,
or public release readiness.
