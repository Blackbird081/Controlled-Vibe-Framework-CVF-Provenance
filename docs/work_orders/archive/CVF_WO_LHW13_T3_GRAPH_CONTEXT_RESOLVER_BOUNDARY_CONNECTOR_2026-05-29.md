# CVF Work Order — LHW13-T3 Graph Context Resolver Boundary Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement LHW13-T3: a connector spec mapping AIF-B `GraphKnowledgeService`
boundary status × LHW7-T2 `signalsStillMissing` (context completeness) ×
LHW11-T3 `memoryContextSeedDecayAdvisoryType` →
`graphContextResolverBoundaryAdvisoryType` + `activeResolutionMode` +
`phaseToNextMode`.

Source: CVF 25.05 Gop_y.md Gap 9 — AIF-B graph modules exist
(`GraphKnowledgeService` in
`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts`
at line 62) but are not wired into any runtime path. No
connector defines which resolution mode is active (text-retrieval /
project-knowledge / graph-future) and what phase boundary separates them.
Gap 9 direction: "Do not build now, just define boundary."

This connector is advisory only. It does NOT execute graph retrieval.
`runtimeExecutionAuthorized=false` invariant.

## Authority Chain

- LHW13 roadmap: `docs/roadmaps/CVF_LHW13_WORKFLOW_CONNECTOR_WAVE13_ROADMAP_2026-05-29.md`
- LHW13 GC-018: `docs/baselines/CVF_GC018_LHW13_WORKFLOW_CONNECTOR_WAVE13_2026-05-29.md`
- AIF-B source: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts`
- LHW7-T2 spec: `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md`
- LHW11-T3 spec: `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (`tolaria` trigger at line 129)
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  (GAP 9 section)
- **T1 gate: `docs/reviews/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS_BOUNDED**
- **T2 gate: `docs/reviews/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS_BOUNDED**

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: `GraphKnowledgeService`
interface individually row-verified in S5; all 3 doc-only
`graphServiceBoundaryStatus` values covered; `runtimeExecutionAuthorized=false`
explicit; no
graph retrieval execution claimed. Auditor confirms `tolaria` and CVF 25.05
Gap 9 cited; defines boundary not execution. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_SPEC_2026-05-29.md` (wave marker update)
- `docs/reference/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_SPEC_2026-05-29.md` (wave marker update)
- `docs/reference/CVF_LHW13_T3_GRAPH_CONTEXT_RESOLVER_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW13_T3_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW13_T3_GRAPH_CONTEXT_RESOLVER_BOUNDARY_CONNECTOR_COMPLETION_2026-05-29.md` (new)
- `docs/roadmaps/CVF_LHW13_WORKFLOW_CONNECTOR_WAVE13_ROADMAP_2026-05-29.md` (wave closure status update)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts`
   — confirm `GraphKnowledgeService` interface at line 62; confirm `buildIndex`
   and `queryImpact` methods; confirm interface-only status (not wired to route)
4. `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `signalsStillMissing` field at S3 line 114
5. `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `memoryContextSeedDecayAdvisoryType` field at S3
6. `docs/reviews/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-29.md`
   — confirm T1 CLOSED_PASS_BOUNDED
7. `docs/reviews/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md`
   — confirm T2 CLOSED_PASS_BOUNDED

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `GraphKnowledgeService` interface | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` | line 62 | `GraphKnowledgeService` | `GraphKnowledgeService` | ACCEPT |
| `buildIndex` method | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` | line 63 | `buildIndex` | `GraphKnowledgeService` | ACCEPT |
| `queryImpact` method | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` | line 64 | `queryImpact` | `GraphKnowledgeService` | ACCEPT |
| `signalsStillMissing` field | `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md` | S3 line 114 | `signalsStillMissing` | LHW7-T2 doc-only field | ACCEPT |
| `memoryContextSeedDecayAdvisoryType` field | `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `memoryContextSeedDecayAdvisoryType` | LHW11-T3 doc-only field | ACCEPT |
| LH1 `tolaria` trigger | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 129 | `tolaria` | LH1 CVF 16.5 ledger | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `graphContextResolverBoundaryAdvisoryType` | Names the graph resolver boundary planning advisory. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |
| `graphServiceBoundaryStatus` values: `interface_only`, `schema_proven`, `route_wired` | Defines the graph boundary status taxonomy for this connector. | Yes | Yes | Defined only in the connector spec; no runtime route wiring claim. |
| `activeResolutionMode` | Records the currently permitted resolution mode as advisory text. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |
| `phaseToNextMode` | States the doc-only phase boundary before another mode may be claimed. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| T3 spec; AIF-B/LHW7-T2/LHW11-T3 field names verbatim | S1–S5 | spec at target path | Reviewer confirms verbatim | CLOSED |
| `GraphKnowledgeService` interface individually row-verified | S5 | interface row | No aggregate | CLOSED |
| All 3 doc-only `graphServiceBoundaryStatus` values covered | S5 | 3 rows | No aggregate | CLOSED |
| `runtimeExecutionAuthorized=false` explicit; no graph retrieval | S1, S3 | invariant | grep check | CLOSED |
| T1 AND T2 gates confirmed | Authority Chain | both completion reviews | Read both | CLOSED |
| LHW13 wave closure summary in completion review | Closure Checklist | T1+T2+T3 table | Reviewer checks | CLOSED |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW13_T3_GRAPH_CONTEXT_RESOLVER_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md`

S2 design: map `GraphKnowledgeService` boundary status × `signalsStillMissing`
× `memoryContextSeedDecayAdvisoryType` → `graphContextResolverBoundaryAdvisoryType`:

Define `graphServiceBoundaryStatus` (3 values, doc-only):
- `interface_only` — `GraphKnowledgeService` exists as interface; `buildIndex`/`queryImpact` not wired to any route
- `schema_proven` — graph schema and storage exist; not called from runtime route
- `route_wired` — wired to runtime path (not current state)

S2 mapping table:

| `graphServiceBoundaryStatus` | `signalsStillMissing` | `memoryContextSeedDecayAdvisoryType` | `graphContextResolverBoundaryAdvisoryType` | `activeResolutionMode` | `phaseToNextMode` |
| --- | --- | --- | --- | --- | --- |
| `interface_only` | empty | healthy | `graph_boundary_interface_only` | `text_retrieval` | Route wiring required before advancing to `project_knowledge` |
| `interface_only` | non-empty | any | `graph_boundary_signals_missing` | `text_retrieval` | Resolve missing signals before graph mode |
| `schema_proven` | empty | healthy | `graph_boundary_schema_ready` | `project_knowledge` | Schema present; route wiring is next phase |
| `schema_proven` | non-empty | contaminated | `graph_boundary_schema_contaminated` | `text_retrieval` | Memory contamination; hold graph advancement |
| `route_wired` | empty | healthy | `graph_boundary_active` | `graph_future` | Graph resolver active (future state) |

Key invariant: "This connector does not execute graph retrieval or wire
`GraphKnowledgeService` to any route. The boundary advisory is a governance
planning record. `runtimeExecutionAuthorized=false`."

## Pre-Flight

- [x] Working tree clean
- [x] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [x] `GraphKnowledgeService` confirmed at graph-schema.ts line 62
- [x] `signalsStillMissing` confirmed from LHW7-T2 S3
- [x] `tolaria` trigger confirmed from LH1 line 129

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads; confirm T1 and T2 gates.
2. Confirm all AIF-B/LHW7-T2/LHW11-T3 symbols.
3. Draft spec; verify < 250 lines.
4. Run Fast Lane audit.
5. Run governance gates.
6. Update session continuity; mark LHW13 CLOSED_PASS_BOUNDED.
7. Update LHW13 roadmap: Status → CLOSED_PASS_BOUNDED; actual commit SHA.
8. Commit.
9. Write completion review with LHW13 wave closure summary.

## Evidence Requirements

- Spec < 250 lines
- `GraphKnowledgeService` interface individually row-verified
- All 3 doc-only `graphServiceBoundaryStatus` values covered
- `runtimeExecutionAuthorized=false` explicit; no graph retrieval
- T1 AND T2 gates confirmed
- No code file in diff
- LHW13 wave closure summary in completion review

## Acceptance Criteria

- [x] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [x] Spec with all 5 sections; < 250 lines
- [x] `GraphKnowledgeService` interface individually row-verified in S5
- [x] All 3 doc-only `graphServiceBoundaryStatus` values covered
- [x] `runtimeExecutionAuthorized=false` explicit; no graph execution claimed
- [x] `tolaria` and CVF 25.05 Gap 9 cited in S1
- [x] No code file in diff
- [x] Session continuity: LHW13 CLOSED_PASS_BOUNDED
- [x] LHW13 roadmap updated with actual commit SHA
- [x] Completion review with LHW13 wave closure summary

Fail conditions:
- T1 or T2 gate not confirmed
- Connector claims to execute graph retrieval or wire `GraphKnowledgeService`
- `graphServiceBoundaryStatus` values aggregated in S5

## Review Gate

T1 and T2 confirmed; `GraphKnowledgeService` verified and all 3 doc-only graph
boundary status values covered; `runtimeExecutionAuthorized=false`; no graph
execution; spec < 250 lines; no code file.

## Closure Checklist

- [x] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [x] Spec with all 5 sections
- [x] S2 boundary mapping uses AIF-B/LHW7-T2/LHW11-T3 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 complete; no aggregate rows
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity: LHW13 CLOSED_PASS_BOUNDED
- [x] LHW13 roadmap Status → CLOSED_PASS_BOUNDED
- [x] Completion review with LHW13 wave closure summary written

## Return-To-Orchestrator Conditions

Stop if: T1 or T2 gate missing; `GraphKnowledgeService` cannot be confirmed;
connector requires graph route wiring; spec > 250 lines before S4.

## LHW13 Wave Closure Gate

After T3 committed, completing agent must update:
1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`: `lhw13WorkflowConnectorWave13.status = CLOSED_PASS_BOUNDED`; `nextAllowedMove` names LHW13 as latest fully closed (after both LHW12 and LHW13 reach CLOSED_PASS_BOUNDED, whichever finishes last becomes latest)
2. `CVF_SESSION_MEMORY.md` Next Allowed Move: reference whichever of LHW12/LHW13 closed last
3. Active handoff: add LHW13 wave closure note with contract versions + commit SHA

Note: LHW12 and LHW13 run in parallel. The registry recognizes whichever fully
closes (all 3 tranches CLOSED_PASS_BOUNDED) latest as the `latestClosedLhwWave`.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW13-T3 produces a documentation artifact. It does not claim graph retrieval
execution, `GraphKnowledgeService` route wiring, memory reinjection, receipt
envelope extension, provider behavior, hosted readiness, production readiness,
or public release readiness.
