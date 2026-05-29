# CVF Work Order — LHW14-T1 Agent Memory Capture Packaging Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement LHW14-T1: a connector spec mapping LHW8-T1 `memorySnapshotAdvisoryType`
(6 values) × VI3 `AgentMemoryCaptureRecord.captureDecision` ×
connector-normalized `canReinject=false` →
`agentMemoryCapturePackagingAdvisoryType` + `capturePackagingGuidance`.

Source: LH1 `agentmemory` PARTIALLY_ABSORBED trigger — "Reopen for capture/read
packaging improvements; raw reinjection remains blocked." W2/VI3/AIF-C surfaces
exist but no connector normalizes them into a packaging advisory for Orchestrators
choosing how to present captured memory context.

This connector is advisory only. It does NOT modify memory capture behavior or
authorize reinjection. Invariants: connector-normalized `canReinject=false`;
`runtimeExecutionAuthorized=false`.

## Authority Chain

- LHW14 roadmap: `docs/roadmaps/CVF_LHW14_WORKFLOW_CONNECTOR_WAVE14_ROADMAP_2026-05-29.md`
- LHW14 GC-018: `docs/baselines/CVF_GC018_LHW14_WORKFLOW_CONNECTOR_WAVE14_2026-05-29.md`
- LHW8-T1 spec: `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
- AIF-C source: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (`agentmemory` trigger at line 133)

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: all 6 `memorySnapshotAdvisoryType`
values individually row-verified in S5; connector-normalized `canReinject=false`
explicit and NOT overridden; `runtimeExecutionAuthorized=false` explicit; no
memory write or reinjection claimed. Auditor confirms `agentmemory` LH1 trigger
cited; advisory-only posture preserved. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW14_T1_AGENT_MEMORY_CAPTURE_PACKAGING_ADVISORY_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW14_T1_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW14_T1_AGENT_MEMORY_CAPTURE_PACKAGING_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md` (new)
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
4. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
   — confirm `MemoryGatewayDecision.canReinject` at line 49: `canReinject: boolean`
   — confirm `rawMemoryReleased` at line 50: `rawMemoryReleased: false`
5. `docs/roadmaps/CVF_LHW14_WORKFLOW_CONNECTOR_WAVE14_ROADMAP_2026-05-29.md`
   — confirm T1 deliverable and mapping design

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `memorySnapshotAdvisoryType` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 94 | `memorySnapshotAdvisoryType` | LHW8-T1 doc-only field | ACCEPT |
| `snapshot_full_capture` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 66 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_summary_only` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 67 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_context_read_only` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 68 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_redacted_capture` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 69 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_denied` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 70 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| `snapshot_approval_pending` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S2 line 71 | `memorySnapshotAdvisoryType` value | LHW8-T1 S2 | ACCEPT |
| EXISTS: `MemoryGatewayDecision.canReinject` boolean field | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 49 | `canReinject` | `MemoryGatewayDecision` | ACCEPT |
| LITERAL_INVARIANT: `MemoryGatewayDecision.rawMemoryReleased=false` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 50 | `rawMemoryReleased` | `MemoryGatewayDecision` | ACCEPT |
| LH1 `agentmemory` trigger | `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 133 | `agentmemory` | LH1 CVF 16.5 ledger | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `agentMemoryCapturePackagingAdvisoryType` | Names the capture packaging planning advisory | Yes |
| `capturePackagingGuidance` | Plain-language guidance for packaging captured memory context | Yes |
| connector-normalized `canReinject=false` | Blocks this connector from treating source boolean as reinjection authority | Yes |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| T1 spec; LHW8-T1/AIF-C field names verbatim | S1–S5 | spec at target path | Reviewer confirms verbatim | CLOSED_PASS |
| All 6 `memorySnapshotAdvisoryType` values individually row-verified | S5 | 6 rows | No aggregate | CLOSED_PASS |
| connector-normalized `canReinject=false` stated and not source-claimed | S1, S3 | connector invariant | grep check | CLOSED_PASS |
| `agentmemory` LH1 trigger cited | S1 | explicit in S1 Purpose | Auditor checks | CLOSED_PASS |
| `runtimeExecutionAuthorized=false` explicit | S1, S3 | invariant | grep check | CLOSED_PASS |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW14_T1_AGENT_MEMORY_CAPTURE_PACKAGING_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`

S2 design: map `memorySnapshotAdvisoryType` × connector-normalized
`canReinject=false` → `agentMemoryCapturePackagingAdvisoryType` +
`capturePackagingGuidance`:

| `memorySnapshotAdvisoryType` | `canReinject` | `agentMemoryCapturePackagingAdvisoryType` | `capturePackagingGuidance` |
| --- | --- | --- | --- |
| `snapshot_full_capture` | `false` | `packaging_full_summary` | Package full session summary; include event ids and receipt chain; no raw content release |
| `snapshot_summary_only` | `false` | `packaging_summary_partial` | Package summary only; note raw content omitted; no raw reinjection |
| `snapshot_context_read_only` | `false` | `packaging_read_no_capture` | No packaging needed; context was read-only; no stored record |
| `snapshot_redacted_capture` | `false` | `packaging_redacted_incomplete` | Package redaction log only; note incomplete evidence; no continuity claim |
| `snapshot_denied` | `false` | `packaging_none_denied` | No packaging; capture was denied; receipt-only evidence |
| `snapshot_approval_pending` | `false` | `packaging_none_pending` | No packaging until capture approved; hold continuity claim |

Key invariants: connector-normalized `canReinject=false`; `rawMemoryReleased=false`
literal invariant preserved; `runtimeExecutionAuthorized=false`.

## Pre-Flight

- [x] Working tree clean
- [x] All 6 `memorySnapshotAdvisoryType` values confirmed from LHW8-T1 S2
- [x] `canReinject` field confirmed from AIF-C source line 49
- [x] `agentmemory` trigger confirmed from LH1 line 133

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all symbols from source.
3. Draft spec (S1–S5); verify < 250 lines.
4. Run Fast Lane audit.
5. Run governance gates with `--base 173643cb`.
6. Reviewer perspective.
7. Update session continuity.
8. Commit.
9. Write completion review with T2 gate answer.

## Evidence Requirements

- Spec < 250 lines
- All 6 `memorySnapshotAdvisoryType` values individually row-verified
- connector-normalized `canReinject=false` stated and NOT overridden
- LH1 `agentmemory` trigger cited in S1
- `runtimeExecutionAuthorized=false` explicit
- No code file in diff

## Acceptance Criteria

- [x] Spec with all 5 sections; < 250 lines
- [x] All 6 `memorySnapshotAdvisoryType` values individually row-verified in S5
- [x] connector-normalized `canReinject=false` stated; not source-claimed
- [x] `runtimeExecutionAuthorized=false` explicit; no memory write or reinjection claimed
- [x] LH1 `agentmemory` trigger cited in S1
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:
- Memory write or reinjection claimed
- `canReinject=true` asserted as active capability
- Aggregate rows in S5

## Review Gate

All 6 `memorySnapshotAdvisoryType` individually verified; connector-normalized
`canReinject=false`; no memory write or reinjection; `runtimeExecutionAuthorized=false`;
spec < 250 lines; no code file.

## Closure Checklist

- [x] Spec with all 5 sections
- [x] S2 mapping covers all 6 `memorySnapshotAdvisoryType` values individually
- [x] connector-normalized `canReinject=false` explicit
- [x] S5 complete; no aggregate rows
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity updated
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop if: memory capture symbols cannot be confirmed; connector requires memory
write or reinjection; spec > 250 lines before S4.

## T2 Gate Output

Was a concrete spec-change workflow advisory gap identified during T1?

**Expected YES:** T1 memory capture packaging reveals that when a spec-change
event triggers a governance decision (LHW11-T2 `specChangeGovernanceDecision`),
no connector maps that decision × rollback recommendation → a named advisory
guiding Orchestrators on whether to pause and require spec review before acting.
T2 closes that gap.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW14-T1 produces a documentation artifact. It does not claim memory write,
reinjection, `canReinject=true`, receipt envelope extension, provider behavior,
hosted readiness, production readiness, or public release readiness.
