# CVF Work Order — LHW13-T2 Memory Continuity Level Advisory Connector

Memory class: FULL_RECORD

Status: HOLD_UNTIL_T1_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement LHW13-T2: a connector spec mapping LHW8-T1 `memorySnapshotAdvisoryType`
(6 values) × LHW11-T3 `memoryContextSeedDecayAdvisoryType` ×
AIF-C `MemoryGatewayDecision.canReinject` →
`memoryContinuityLevelAdvisoryType` (L0/L1/L2/L3) +
`continuityLevelBoundaryNote`.

Source: CVF 25.05 Gop_y.md Gap 4 — CVF is at L0/L1 memory. No connector maps
existing snapshot and decay advisories into a named L0-L3 taxonomy advisory.
The 4-level taxonomy (L0 receipt-only, L1 session summary, L2 governed
reinjection, L3 cross-workflow) makes the boundary visible and explicit.

This connector is advisory only. It does NOT reinject memory or lift
`canReinject=false`. Invariants: `canReinject=false` preserved;
`runtimeExecutionAuthorized=false`.

## Authority Chain

- LHW13 roadmap: `docs/roadmaps/CVF_LHW13_WORKFLOW_CONNECTOR_WAVE13_ROADMAP_2026-05-29.md`
- LHW13 GC-018: `docs/baselines/CVF_GC018_LHW13_WORKFLOW_CONNECTOR_WAVE13_2026-05-29.md`
- LHW8-T1 spec: `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
- LHW11-T3 spec: `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- AIF-C source: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (`tolaria` trigger at line 129)
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  (GAP 4 section)
- **T1 gate: `docs/reviews/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS_BOUNDED**

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: all 6 `memorySnapshotAdvisoryType`
values individually row-verified in S5; `canReinject=false` preserved and NOT
overridden; `runtimeExecutionAuthorized=false` explicit. Auditor confirms
`tolaria` trigger and CVF 25.05 Gap 4 cited; no memory reinjection claimed.
No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW13_T2_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `memorySnapshotAdvisoryType` values at S2 lines 66–71:
   `snapshot_full_capture`, `snapshot_summary_only`, `snapshot_context_read_only`,
   `snapshot_redacted_capture`, `snapshot_denied`, `snapshot_approval_pending`
4. `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `memoryContextSeedDecayAdvisoryType` values at S3 field list
5. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
   — confirm `MemoryGatewayDecision.canReinject` at line 49: `canReinject: boolean`
   — confirm `rawMemoryReleased` at line 50: `rawMemoryReleased: false`
6. `docs/reviews/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-29.md`
   — confirm T1 CLOSED_PASS_BOUNDED

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `memorySnapshotAdvisoryType` field | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 94 | `memorySnapshotAdvisoryType` | LHW8-T1 doc-only field | ACCEPT |
| `snapshot_full_capture` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 66 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_summary_only` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 67 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_context_read_only` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 68 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_redacted_capture` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 69 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_denied` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 70 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_approval_pending` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 71 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `memoryContextSeedDecayAdvisoryType` field | `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `memoryContextSeedDecayAdvisoryType` | LHW11-T3 doc-only field | ACCEPT |
| `MemoryGatewayDecision.canReinject` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 49 | `canReinject` | `MemoryGatewayDecision` | ACCEPT |
| `MemoryGatewayDecision.rawMemoryReleased` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 50 | `rawMemoryReleased` | `MemoryGatewayDecision` | ACCEPT |
| LH1 `tolaria` trigger | `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 129 | `tolaria` | LH1 CVF 16.5 ledger | ACCEPT |
| `memoryContinuityLevelAdvisoryType` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Memory continuity level advisory packet | ACCEPT |
| `continuityLevelBoundaryNote` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Memory continuity level advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| T2 spec; LHW8-T1/LHW11-T3/AIF-C field names verbatim | S1–S5 | spec at target path | Reviewer confirms verbatim | OPEN |
| All 6 `memorySnapshotAdvisoryType` values individually row-verified | S5 | 6 rows | No aggregate | OPEN |
| `canReinject=false` preserved and not overridden | S1, S3 | invariant preserved | grep check | OPEN |
| L0-L3 taxonomy mapped in S2 | S2 | 4-level advisory table | Reviewer checks | OPEN |
| T1 gate confirmed | Authority Chain | T1 completion review | Read T1 review | OPEN |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`

S2 design — map `memorySnapshotAdvisoryType` × `canReinject` ×
`memoryContextSeedDecayAdvisoryType` → `memoryContinuityLevelAdvisoryType`:

| `memorySnapshotAdvisoryType` | `canReinject` | decay advisory | `memoryContinuityLevelAdvisoryType` | `continuityLevelBoundaryNote` |
| --- | --- | --- | --- | --- |
| `snapshot_full_capture` | `false` | healthy | `L1_session_summary` | L1: full session capture; summary-level continuity; no reinjection |
| `snapshot_summary_only` | `false` | healthy | `L1_summary_partial` | L1: summary-only capture; partial continuity; no raw reinjection |
| `snapshot_context_read_only` | `false` | any | `L0_receipt_only` | L0: context read, no capture; receipt-only evidence |
| `snapshot_redacted_capture` | `false` | contaminated | `L0_receipt_redacted` | L0: redacted capture; evidence is incomplete; no continuity claim |
| `snapshot_denied` | `false` | any | `L0_no_capture` | L0: no capture; receipt-only; no continuity |
| `snapshot_approval_pending` | `false` | any | `L0_pending_approval` | L0: approval pending; no continuity until capture approved |
| any | `false` | high contamination | `L0_contamination_hold` | L0: contamination; hold all continuity claims |
| N/A — L2 | N/A | N/A | `L2_governed_reinjection_not_claimed` | L2 is NOT claimed by CVF; `canReinject=false` is invariant |
| N/A — L3 | N/A | N/A | `L3_cross_workflow_not_claimed` | L3 is NOT claimed by CVF; no cross-workflow memory |

Key invariants in S1:
- "`canReinject=false` is invariant. This connector does not lift it."
- "L2 and L3 are NOT currently claimed by CVF."
- "`memoryContinuityLevelAdvisoryType` is a governance planning record."
- `runtimeExecutionAuthorized=false`.

## Pre-Flight

- [ ] Working tree clean
- [ ] T1 CLOSED_PASS_BOUNDED confirmed
- [ ] All 6 `memorySnapshotAdvisoryType` values confirmed from LHW8-T1 S2
- [ ] `canReinject` field confirmed from AIF-C source line 49

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads; confirm T1 gate.
2. Confirm all symbols.
3. Draft spec; verify < 250 lines.
4. Run Fast Lane audit.
5. Run governance gates.
6. Update session continuity.
7. Commit.
8. Write completion review with T3 gate answer.

## Evidence Requirements

- Spec < 250 lines
- All 6 `memorySnapshotAdvisoryType` values individually row-verified
- `canReinject=false` preserved and NOT overridden
- L2/L3 explicitly stated as NOT claimed
- T1 gate confirmed
- No code file in diff

## Acceptance Criteria

- [ ] T1 CLOSED_PASS_BOUNDED confirmed
- [ ] Spec with all 5 sections; < 250 lines
- [ ] All 6 `memorySnapshotAdvisoryType` values individually row-verified in S5
- [ ] `canReinject=false` preserved; L2/L3 explicitly NOT claimed
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] No code file in diff
- [ ] Session continuity updated

Fail conditions:
- T1 gate not confirmed
- `canReinject=true` anywhere in spec
- L2/L3 claimed as active CVF capability
- Aggregate rows in S5

## Review Gate

T1 confirmed; all 6 `memorySnapshotAdvisoryType` individually verified;
`canReinject=false` preserved; L2/L3 not claimed; spec < 250 lines; no code file.

## Closure Checklist

- [ ] T1 CLOSED_PASS_BOUNDED confirmed
- [ ] Spec with all 5 sections
- [ ] S2 L0-L3 taxonomy uses LHW8-T1/LHW11-T3/AIF-C vocabulary verbatim
- [ ] `canReinject=false` preserved
- [ ] S5 complete; no aggregate rows
- [ ] No code file in diff
- [ ] Fast Lane audit created
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop if: T1 gate missing; `canReinject` cannot be confirmed; connector lifts
`canReinject=false` or claims L2/L3; spec > 250 lines before S4.

## T3 Gate Output

Was a concrete graph context resolver boundary gap identified during T2?

**Expected YES:** T2 memory level mapping reveals that while AIF-B graph modules
exist (`GraphKnowledgeService` in graph-schema.ts), no connector maps their
boundary status × current text-retrieval posture → a named
`graphContextResolverBoundaryAdvisoryType` defining which resolution mode is
active. T3 closes that gap.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW13-T2 produces a documentation artifact. It does not claim memory reinjection,
`canReinject=true`, L2/L3 memory levels, receipt envelope extension, hosted
readiness, production readiness, or public release readiness.
