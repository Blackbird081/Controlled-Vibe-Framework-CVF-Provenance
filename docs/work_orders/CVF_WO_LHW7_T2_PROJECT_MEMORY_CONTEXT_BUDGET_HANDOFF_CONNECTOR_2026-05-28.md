# CVF Work Order — LHW7-T2 Project Memory Context Budget Handoff Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW7-T2: a connector spec binding LHW6-T3 project memory readout
packet (`durableTierSummary`, `gatewayMemoryIds`, `canReinject=false`) →
CB1 `RouteRequestContextReadout` (`budgetTier`, `missingSignals`,
`contaminationFlags`) → VI2 `missingSignals` into a cross-session handoff
packet. Closes the gap where no standard defines which project memory summary
fields can populate CB1 `missingSignals` on session resume without violating
`canReinject=false` or `rawMemoryReleased=false`.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. Memory injection and raw memory release remain blocked.

## Authority Chain

- LHW7 roadmap: `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
- LHW7 GC-018: `docs/baselines/CVF_GC018_LHW7_WORKFLOW_CONNECTOR_WAVE7_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW7_T2_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- T1 gate: `docs/reviews/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_COMPLETION_2026-05-28.md`
  — CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `caveman`, `Workflow GoClaw`, `Review CVF_1.md`)
- LHW6-T3 spec: `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md`
- CB1 completion: `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- VI2 completion: `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`

## Agent Roles

Implementer writes spec (S1–S5) using LHW6-T3, CB1, VI2, M1, and AIF-C
vocabulary verbatim. Reviewer checks field names verbatim, `canReinject=false`
and `rawMemoryReleased=false` invariants explicit, seeding map honest, S5
Source Verification complete. Auditor confirms LH1 triggers recorded, no memory
injection or raw memory release claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
`canReinject=true`, `rawMemoryReleased=true`, and memory injection remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md`
   — confirm S3 fields: `durableTierSummary`, `gatewayMemoryIds`, `canReinject=false`,
   `rawMemoryReleased=false`
4. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
   — confirm `DurableMemoryReceipt` fields: `summaryOnly`, `canReinject`,
   `rawMemoryReleased`, `tier` at lines 35–49
5. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
   — confirm `MemoryGatewayDecision.memoryIdsAffected` at lines 40–51;
   confirm `rawMemoryReleased=false` hardcoded at line 50
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts`
   — confirm `RouteRequestContextBudgetTier` values at line 6;
   confirm `budgetTier` at line 16; `missingSignals` at line 22;
   `contaminationFlags` at line 24; `noiseFlags` at line 23
7. `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
   — confirm T2 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| LHW6-T3 `durableTierSummary` | `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 82 | `durableTierSummary` | LHW6-T3 packet field | ACCEPT |
| LHW6-T3 `gatewayMemoryIds` | `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 83 | `gatewayMemoryIds` | LHW6-T3 packet field | ACCEPT |
| LHW6-T3 `canReinject=false` | `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 84 | `canReinject` | LHW6-T3 invariant | ACCEPT |
| LHW6-T3 `rawMemoryReleased=false` | `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 85 | `rawMemoryReleased` | LHW6-T3 invariant | ACCEPT |
| M1 `DurableMemoryReceipt` (`summaryOnly`, `canReinject`, `rawMemoryReleased`, `tier`) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35–49 | `DurableMemoryReceipt` | `DurableMemoryReceipt` | ACCEPT |
| AIF-C `MemoryGatewayDecision.memoryIdsAffected` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 40–51 | `memoryIdsAffected` | `MemoryGatewayDecision` | ACCEPT |
| AIF-C `rawMemoryReleased=false` hardcoded | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 50 | `rawMemoryReleased` | `MemoryGatewayDecision` | ACCEPT |
| CB1 `RouteRequestContextBudgetTier` values (`minimal`, `standard`, `expanded`) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 6 | `RouteRequestContextBudgetTier` | `RouteRequestContextBudgetTier` | ACCEPT |
| CB1 `budgetTier` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 16 | `budgetTier` | `RouteRequestContextReadout` | ACCEPT |
| CB1 `missingSignals` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 22 | `missingSignals` | `RouteRequestContextReadout` | ACCEPT |
| CB1 `contaminationFlags` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 24 | `contaminationFlags` | `RouteRequestContextReadout` | ACCEPT |
| CB1 `noiseFlags` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 23 | `noiseFlags` | `RouteRequestContextReadout` | ACCEPT |
| `RouteRequestContextReadiness` values (`ready`, `needs_clarification`, `needs_context_compaction`, `blocked_contaminated_brief`) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | lines 7–11 | `ready`, `needs_clarification`, `needs_context_compaction`, `blocked_contaminated_brief` | `RouteRequestContextReadiness` | ACCEPT |
| New doc-only fields `seedableSummaryFields`, `signalsSeededBySummary`, `signalsStillMissing`, `contaminationRiskAfterSeed` | N/A — doc-only | S3 new fields | doc-only | Handoff packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T2 spec created; LHW6-T3/CB1/VI2 field names verbatim | S1–S5 | `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md` | Reviewer confirms source-verbatim field names | BLOCKED until spec exists |
| `canReinject=false` and `rawMemoryReleased=false` invariants explicit | S1, S3, Claim Boundary | invariants in S1 and S3 | `rg -n "canReinject=false\|rawMemoryReleased=false" <spec>` | BLOCKED until spec exists |
| Seeding map with 4 derived doc-only fields | S2 | `seedableSummaryFields`, `signalsSeededBySummary`, `signalsStillMissing`, `contaminationRiskAfterSeed` | Reviewer checks S2 rows | BLOCKED until spec exists |
| Source Verification Table complete | S5 | Source Verification Table | `rg -n "Disposition" <spec>` plus reviewer check | BLOCKED until spec exists |
| No code file modified | Evidence Requirements | git diff output | `git diff --name-only` | BLOCKED until closure evidence |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md`

Required sections S1–S5. See LHW7 roadmap for full deliverable shape.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] LHW6-T3 field names confirmed from source
- [ ] M1 `DurableMemoryReceipt` fields confirmed from source
- [ ] AIF-C `MemoryGatewayDecision` fields confirmed from source
- [ ] CB1/VI2 `RouteRequestContextReadout` fields confirmed from source

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all field names from source files.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw7_t2_complete`).
7. Commit: `docs(lhw7-t2): add project memory context budget handoff connector spec`.
8. Write completion review; include T3 gate answer.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 seeding map covers minimum 5 LHW6-T3 tier + CB1 signal combinations
- `canReinject=false` and `rawMemoryReleased=false` explicit in S1 and S3
- `runtimeExecutionAuthorized=false` explicit
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw7_t2_complete`
- Completion review written with T3 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 seeding map covers minimum 5 tier/signal combinations
- [ ] `canReinject=false` and `rawMemoryReleased=false` invariants explicit
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

Fail conditions:

- [ ] Missing LHW7 GC-018 baseline, missing Source Verification row, or
  Source Verification `ACCEPT` row citing a non-existent file
- [ ] Any claim that this connector injects memory into the prompt, authorizes
  `canReinject=true`, or performs cross-session memory reinjection

## Review Gate

Before committing: Reviewer perspective completed; all LHW6-T3/CB1/VI2 field
names verbatim; `canReinject=false` and `rawMemoryReleased=false` explicit;
S5 complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; no code file in diff.

## Closure Checklist

- [ ] Spec created with all 5 sections
- [ ] S2 seeding map uses LHW6-T3/CB1/VI2 vocabulary verbatim
- [ ] `canReinject=false` and `rawMemoryReleased=false` explicit
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing;
- a LHW6-T3, CB1, VI2, M1, or AIF-C field token cannot be confirmed from
  source files;
- writing the connector requires opening a memory injection path, setting
  `canReinject=true`, or releasing raw memory;
- spec exceeds 250 lines before S4 is complete.

## T3 Gate Output (required in completion review)

Answer explicitly: "Was a concrete failure simulation → spec-change gap
identified during T2 work?"

- YES → describe gap in one sentence; T3 proceeds.
- NO → "No gap found. T3 proceeds per roadmap rationale."
  (T3 proceeds regardless — this output is informational.)

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified LHW6-T3/CB1/VI2 vocabulary; no operator checkpoint required
unless a memory injection path or `canReinject=true` relaxation is discovered
during implementation.

## Claim Boundary

LHW7-T2 produces a documentation artifact. It does not claim LHW6-T3/CB1/VI2
runtime extension, memory injection, prompt seeding from raw memory, memory
reinjection, receipt envelope extension, provider behavior, hosted readiness,
production readiness, or public release readiness.
