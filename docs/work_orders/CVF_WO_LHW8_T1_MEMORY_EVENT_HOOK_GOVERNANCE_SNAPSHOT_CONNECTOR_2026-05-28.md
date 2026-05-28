# CVF Work Order — LHW8-T1 Memory Event Hook Governance Snapshot Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW8-T1: a connector spec binding W2 `MemoryEventHookDecision`
(5 values: `allow_capture`, `allow_context_read`, `allow_redacted_capture`,
`deny`, `require_human_approval`) × AIF-C `MemoryGatewayDecision`
(`operation`, `decision`, `canReinject`, `rawMemoryReleased`) × VI3
`AgentMemoryCaptureRecord` (`captureDecision`, `policyContext`) into a single
governance snapshot advisory packet. Closes the gap where no standard maps
these three surfaces into a named snapshot advisory type with explicit
promotion eligibility.

Documentation-only tranche. No source code, runtime module, route, or
provider behavior is changed. Memory injection and raw memory release remain
blocked.

## Authority Chain

- LHW8 roadmap: `docs/roadmaps/CVF_LHW8_WORKFLOW_CONNECTOR_WAVE8_ROADMAP_2026-05-28.md`
- LHW8 GC-018: `docs/baselines/CVF_GC018_LHW8_WORKFLOW_CONNECTOR_WAVE8_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW8_T1_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `agentmemory`, `tolaria`)
- W2 completion: `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
- AIF-C completion: `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`
- VI3 completion: `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`

## Agent Roles

Implementer writes spec (S1–S5) using W2, AIF-C, and VI3 vocabulary verbatim.
Reviewer checks all `MemoryEventHookDecision` values verbatim, all
`MemoryGatewayPolicyDecision` values verbatim, `runtimeExecutionAuthorized=false`
and `canReinject=false` explicit, boundary table honest, S5 Source Verification
complete. Auditor confirms LH1 triggers recorded, no memory injection or raw
memory release claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
`canReinject=true`, `rawMemoryReleased=true`, and memory injection remain
blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts`
   — confirm `MemoryEventHookDecision` values at lines 32–37;
   confirm `MemoryEventHookReceipt.rawMemoryReleased=false` at line 62;
   confirm `MemoryEventHookReceipt.canReinject=false` at line 63
4. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
   — confirm `MemoryGatewayDecision` interface at lines 40–51;
   confirm `MemoryGatewayOperation` values at lines 4–13;
   confirm `MemoryGatewayPolicyDecision` values at lines 15–21
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
   — confirm `AgentMemoryCaptureRecord.captureDecision` at line 38;
   confirm `AgentMemoryCaptureRecord.policyContext` at lines 28–34;
   confirm `AgentMemoryCaptureRecord.privacyFilters` at line 36
6. `docs/roadmaps/CVF_LHW8_WORKFLOW_CONNECTOR_WAVE8_ROADMAP_2026-05-28.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `MemoryEventHookDecision` type | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 32 | `MemoryEventHookDecision` | `MemoryEventHookDecision` | ACCEPT |
| `allow_capture` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 33 | `MemoryEventHookDecision` value | `MemoryEventHookDecision` | ACCEPT |
| `allow_context_read` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 34 | `MemoryEventHookDecision` value | `MemoryEventHookDecision` | ACCEPT |
| `allow_redacted_capture` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 35 | `MemoryEventHookDecision` value | `MemoryEventHookDecision` | ACCEPT |
| `deny` (MemoryEventHookDecision) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 36 | `MemoryEventHookDecision` value | `MemoryEventHookDecision` | ACCEPT |
| `require_human_approval` (MemoryEventHookDecision) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 37 | `MemoryEventHookDecision` value | `MemoryEventHookDecision` | ACCEPT |
| `MemoryEventHookReceipt.rawMemoryReleased=false` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 62 | `rawMemoryReleased` | `MemoryEventHookReceipt` | ACCEPT |
| `MemoryEventHookReceipt.canReinject=false` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | line 63 | `canReinject` | `MemoryEventHookReceipt` | ACCEPT |
| `MemoryGatewayDecision` interface | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 40–51 | `MemoryGatewayDecision` | `MemoryGatewayDecision` | ACCEPT |
| `MemoryGatewayDecision.operation` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 43 | `operation` | `MemoryGatewayDecision` | ACCEPT |
| `MemoryGatewayDecision.decision` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 44 | `decision` | `MemoryGatewayDecision` | ACCEPT |
| `MemoryGatewayDecision.canReinject` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 49 | `canReinject` | `MemoryGatewayDecision` | ACCEPT |
| `MemoryGatewayDecision.rawMemoryReleased=false` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 50 | `rawMemoryReleased` | `MemoryGatewayDecision` | ACCEPT |
| `AgentMemoryCaptureRecord.captureDecision` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts` | line 38 | `captureDecision` | `AgentMemoryCaptureRecord` | ACCEPT |
| `AgentMemoryCaptureRecord.policyContext` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts` | lines 28–34 | `policyContext` | `AgentMemoryCaptureRecord` | ACCEPT |
| `AgentMemoryCaptureRecord.privacyFilters` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts` | line 36 | `privacyFilters` | `AgentMemoryCaptureRecord` | ACCEPT |
| New doc-only fields `memorySnapshotAdvisoryType`, `captureDecisionSummary`, `promotionEligible` | N/A — doc-only | S3 new fields | doc-only | Snapshot advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T1 spec; W2/AIF-C/VI3 field names verbatim | S1–S5 | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | Reviewer confirms source-verbatim field names | CLOSED |
| Memory re-execution blocked explicit | S1, S3, Claim Boundary | `runtimeExecutionAuthorized=false`; explicit not-reexecute statement | `rg -n "runtimeExecutionAuthorized=false" <spec>` | CLOSED |
| `canReinject=false` and `rawMemoryReleased=false` invariants explicit | S1, S3 | invariants stated | Reviewer checks | CLOSED |
| Source Verification Table complete | S5 | Source Verification Table | Reviewer checks no `BLOCKED_SOURCE_NOT_FOUND` row | CLOSED |
| No code file modified | Evidence Requirements | git diff output | `git diff --name-only` | CLOSED |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`

Required sections S1–S5.

## Pre-Flight

- [x] Working tree clean
- [x] All required first reads done
- [x] W2 `MemoryEventHookDecision` values confirmed from source (lines 32–37)
- [x] AIF-C `MemoryGatewayDecision` fields confirmed from source (lines 40–51)
- [x] VI3 `AgentMemoryCaptureRecord` fields confirmed from source (lines 28–38)

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all W2/AIF-C/VI3 field names from source files.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity.
7. Commit.
8. Write completion review; include T2 gate answer.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps all 5 `MemoryEventHookDecision` values to snapshot advisory decisions
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- `canReinject=false` and `rawMemoryReleased=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated
- Completion review written with T2 gate answer

## Acceptance Criteria

- [x] Spec with all 5 sections created
- [x] S2 covers all 5 `MemoryEventHookDecision` values
- [x] `runtimeExecutionAuthorized=false` invariant explicit in S1 and S3
- [x] `canReinject=false` and `rawMemoryReleased=false` explicit
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:

- Missing LHW8 GC-018 baseline, missing Source Verification row, or
  Source Verification `ACCEPT` row citing a non-existent file
- Any claim that this connector re-executes memory operations, sets
  `canReinject=true`, releases raw memory, or extends W2/AIF-C/VI3 runtime
  behavior

## Review Gate

Before committing: Reviewer perspective completed; all W2/AIF-C/VI3 field
names verbatim; `runtimeExecutionAuthorized=false`, `canReinject=false`,
`rawMemoryReleased=false` explicit; S5 complete with no
`BLOCKED_SOURCE_NOT_FOUND` rows; no code file in diff.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 snapshot mapping uses W2/AIF-C/VI3 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] `canReinject=false` and `rawMemoryReleased=false` explicit
- [x] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] No code file in diff
- [x] Session continuity updated
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing;
- a W2 `MemoryEventHookDecision` value, AIF-C `MemoryGatewayDecision` field,
  or VI3 `AgentMemoryCaptureRecord` field cannot be confirmed from source;
- writing the connector requires opening a memory injection path, setting
  `canReinject=true`, or releasing raw memory;
- spec exceeds 250 lines before S4 is complete.

## T2 Gate Output

Was a concrete execution identity → authority chain gap identified during T1?

**YES.** T1 mapping reveals that memory capture decisions (W2/AIF-C/VI3) are
per-hook and per-operation, but there is no connector that maps from the
actor's execution identity (G1 `cvfRole`, `contextScope`) and tool approval
state (W3 `ToolActionApprovalState`) to a named authority chain handoff. T2
closes that gap.

T2 proceeds per roadmap gating rule (T1 CLOSED_PASS ✓).

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified W2/AIF-C/VI3 vocabulary; no operator checkpoint required
unless a memory injection path or `canReinject=true` relaxation is discovered
during implementation.

## Claim Boundary

LHW8-T1 produces a documentation artifact. It does not claim W2/AIF-C/VI3
runtime extension, memory re-execution, memory injection, raw memory release,
receipt envelope extension, provider behavior, hosted readiness, production
readiness, or public release readiness.
