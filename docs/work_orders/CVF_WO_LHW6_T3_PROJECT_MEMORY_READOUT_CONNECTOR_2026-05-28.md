# CVF Work Order — LHW6-T3 Project Memory Readout Connector

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW6-T3: a connector spec tying M1 durable tier state →
WR1 recovery checkpoint → AIF-C memory gateway decision into a project-memory
readout packet. Closes the gap where M1 holds durable `skill` and `long-term`
memory receipts, WR1 supplies the `lastRestorableCheckpoint`, and AIF-C
provides `MemoryGatewayDecision.memoryIdsAffected` — but no connector defines
the project-memory readout packet that an Orchestrator can read when resuming
a session or workflow to understand where memory stands and what recovery path
exists. `canReinject=false` and `rawMemoryReleased=false` are preserved.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed.

## Authority Chain

- LHW6 roadmap: `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW6_T3_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- LH1 ledger (`Review CVF_1.md` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- M1 source: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- AIF-C source: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- WR1 source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- LHW4-T1 spec: `docs/reference/CVF_LHW4_MEMORY_SNAPSHOT_GOVERNANCE_CONNECTOR_SPEC_2026-05-27.md`
- LHW6-T1 spec: `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LHW6-T2 spec: `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md`

## Gate Conditions — CHECK FIRST

```text
Gate 1 — T1 status: CLOSED_PASS
Gate 2 — T2 status: CLOSED_PASS
```

Read `docs/reviews/CVF_LHW6_T1_*_COMPLETION_2026-05-28.md` and
`docs/reviews/CVF_LHW6_T2_*_COMPLETION_2026-05-28.md`.

If either gate is not CLOSED_PASS, stop and report to Orchestrator.

## Agent Roles

Implementer writes spec (S1–S5) using M1, AIF-C, WR1, and LHW4-T1 vocabulary
verbatim. Reviewer checks M1 field names verbatim, AIF-C field names verbatim,
WR1 `WorkflowRecoveryReadout` fields verbatim, `canReinject=false` explicit,
`rawMemoryReleased=false` explicit, boundary table honest, S5 Source
Verification complete. Auditor confirms both gates documented, `Review CVF_1.md`
LH1 trigger recorded, no memory reinjection or new memory tier claimed. No
self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- LHW6 roadmap (status update to `CLOSED_PASS_BOUNDED` after T3 closes)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Memory reinjection, new memory tiers, and raw memory release remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 and T2 completions (understand the tool boundary chain T3 builds beside)
4. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
   — confirm M1 `DurableMemoryTier` values: `skill`, `long-term`; confirm
   `DurableMemoryReceipt` fields: `contractVersion`, `operation`, `tier`,
   `scope`, `memoryIds`, `summaryOnly`, `canReinject`, `rawMemoryReleased`;
   confirm `DURABLE_MEMORY_STORE_VERSION = "cvf.durableMemoryStore.m1.v1"`
5. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
   — confirm AIF-C `MemoryGatewayDecision` fields: `contractVersion`,
   `memoryIdsAffected`, `auditReceiptRequired`, `canReinject`,
   `rawMemoryReleased`; confirm `rawMemoryReleased: false` is hardcoded
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
   — confirm WR1 `WorkflowRecoveryReadout` fields: `contractVersion`,
   `workflowId`, `lastRestorableCheckpoint`, `blockedStepIds`,
   `validationGate`, `recoveryAction`, `recommendedNextAction`;
   confirm `WorkflowRecoveryAction` values: `resume_from_checkpoint`,
   `hold_for_reviewer_gate`, `escalate_to_governance`
7. `docs/reference/CVF_LHW4_MEMORY_SNAPSHOT_GOVERNANCE_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S3 `snapshotBoundary` values and `canReinject=false` invariant;
   use LHW4-T1 snapshot receipt as evidence anchor for T3
8. `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
   — confirm T3 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| M1 `DurableMemoryTier` values | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 13 | `skill`, `long-term` | `DurableMemoryTier` | ACCEPT |
| M1 `DurableMemoryReceipt` fields | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35-49 | `contractVersion`, `tier`, `scope`, `memoryIds`, `summaryOnly`, `canReinject`, `rawMemoryReleased` | `DurableMemoryReceipt` | ACCEPT |
| M1 `summaryOnly=true` invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 46 | `summaryOnly: true` | `DurableMemoryReceipt` | ACCEPT |
| M1 `canReinject=false` / `rawMemoryReleased=false` invariants | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 47-48 | `canReinject: false`, `rawMemoryReleased: false` | `DurableMemoryReceipt` | ACCEPT |
| AIF-C `MemoryGatewayDecision.memoryIdsAffected` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 40-51 | `memoryIdsAffected`, `auditReceiptRequired`, `canReinject`, `rawMemoryReleased` | `MemoryGatewayDecision` | ACCEPT |
| AIF-C `rawMemoryReleased: false` hardcoded | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 50 | `rawMemoryReleased: false` | `MemoryGatewayDecision` | ACCEPT |
| WR1 `WorkflowRecoveryReadout` fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | lines 85-94 | `contractVersion`, `lastRestorableCheckpoint`, `blockedStepIds`, `validationGate`, `recoveryAction`, `recommendedNextAction` | `WorkflowRecoveryReadout` | ACCEPT |
| WR1 `WorkflowRecoveryAction` values | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | lines 50-54 | `resume_from_checkpoint`, `hold_for_reviewer_gate`, `escalate_to_governance` | `WorkflowRecoveryAction` | ACCEPT |

New doc-only fields proposed by this work order: `projectMemoryReadoutId`,
`durableTierSummary`, `gatewayMemoryIds`, `recoveryAnchor`,
`projectMemoryReadoutBoundary`, and `projectMemoryCanResume`. These must be
labeled documentation-only in the connector spec.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc tying M1 `DurableMemoryReceipt`
  tier state → AIF-C `MemoryGatewayDecision.memoryIdsAffected` → WR1
  `lastRestorableCheckpoint` + `recoveryAction` into a project-memory readout
  packet for Orchestrator session-resume planning.
- State what it is not: not an M1/AIF-C/WR1 runtime extension; not a memory
  reinjection authority; not a new memory tier.
- Explicit statement: "`canReinject=false` and `rawMemoryReleased=false` are
  preserved from M1 and AIF-C boundaries. This connector does not relax either
  constraint. The project-memory readout packet is a governance summary record;
  it does not grant memory reinjection or raw memory release."

### S2 — M1 tier + AIF-C decision + WR1 checkpoint readout mapping

Table columns: `M1 tier present` | `AIF-C gateway decision` |
`WR1 recoveryAction` | `Project memory state` | `Orchestrator guidance`

Minimum rows:

- `skill` tier readable + `canReinject=false` + `resume_from_checkpoint` →
  `skill_memory_available` → "Skill-tier memory is available. Resume from
  last restorable checkpoint."
- `long-term` tier readable + `canReinject=false` + `resume_from_checkpoint` →
  `long_term_memory_available` → "Long-term memory is available. Resume from
  last restorable checkpoint."
- either tier readable + AIF-C denied + `hold_for_reviewer_gate` →
  `memory_gated_pending_review` → "Memory gateway denied access. Hold for
  reviewer gate before resuming."
- either tier readable + AIF-C denied + `escalate_to_governance` →
  `memory_gated_escalate` → "Memory gateway denied; invalid transition detected.
  Escalate to governance before resuming."
- neither tier readable + `lastRestorableCheckpoint=null` →
  `no_memory_state` → "No durable memory available. Begin fresh session."

Use M1, AIF-C, and WR1 field names verbatim.

### S3 — Project memory readout packet minimum fields

Prose + field list (max 10 lines):

Every project memory readout packet must contain:

- `projectMemoryReadoutId`: unique token
- `durableTierSummary`: list of M1 `DurableMemoryTier` values present with
  `summaryOnly=true` and `memoryIds`
- `gatewayMemoryIds`: from AIF-C `MemoryGatewayDecision.memoryIdsAffected`
- `canReinject`: always `false`
- `rawMemoryReleased`: always `false`
- `recoveryAnchor`: from WR1 `lastRestorableCheckpoint` (or `null`)
- `recoveryAction`: from WR1 `WorkflowRecoveryAction`
- `projectMemoryReadoutBoundary`: one of `skill_memory_available` |
  `long_term_memory_available` | `memory_gated_pending_review` |
  `memory_gated_escalate` | `no_memory_state`
- `projectMemoryCanResume`: `true` only when boundary is `skill_memory_available`
  or `long_term_memory_available` and `recoveryAction=resume_from_checkpoint`

State explicitly: "These fields are documentation-only minimum requirements.
`canReinject=false` and `rawMemoryReleased=false` are invariant. The readout
packet does not extend `GovernanceEvidenceReceipt` or any existing receipt
envelope. It uses LHW4-T1 snapshot receipt as its evidence anchor."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| M1 durable memory read | Runtime (M1 LPF) | Stable |
| AIF-C memory gateway retrieval | Runtime (AIF-C LPF) | Stable |
| WR1 workflow recovery readout | Runtime (cvf-web workflow resolver) | Stable |
| LHW4-T1 snapshot receipt (evidence anchor) | Document-only (LHW4-T1) | Future: snapshot assembler service |
| Project memory readout packet composition | Document-only | Future: session-resume readout engine |
| Automated session-resume decision | Document-only | Future: Orchestrator session-resume gate |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

After T3 is CLOSED_PASS: update LHW6 roadmap Status to `CLOSED_PASS_BOUNDED`.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every M1 field, AIF-C field, and WR1 field cited in S2 and S3.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] T2 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] M1 `DurableMemoryReceipt` fields confirmed from source
- [ ] AIF-C `MemoryGatewayDecision` fields confirmed from source
- [ ] WR1 `WorkflowRecoveryReadout` fields confirmed from source

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Confirm T1 + T2 gates.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update LHW6 roadmap → `CLOSED_PASS_BOUNDED`.
7. Update session continuity (`lhw6_t3_complete`).
8. Commit: `docs(lhw6-t3): add project memory readout connector spec`.
9. Write completion review.

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps minimum 5 M1+AIF-C+WR1 state combinations to project memory states
- `canReinject=false` and `rawMemoryReleased=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- LHW6 roadmap updated to `CLOSED_PASS_BOUNDED`
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw6_t3_complete`
- Completion review written

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers minimum 5 project memory state combinations
- [ ] `canReinject=false` and `rawMemoryReleased=false` invariant explicit
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] LHW6 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all M1/AIF-C/WR1 field
names verbatim; `canReinject=false` and `rawMemoryReleased=false` explicit; S5
complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; LHW6 roadmap updated; no
code file in diff.

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] T2 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] S2 project memory mapping uses M1+AIF-C+WR1 vocabulary verbatim
- [ ] `canReinject=false` and `rawMemoryReleased=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] LHW6 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 or T2 gate is not CLOSED_PASS;
- any required first read file is missing;
- an M1, AIF-C, or WR1 field name cannot be confirmed from source files;
- writing the connector requires relaxing `canReinject=false`,
  `rawMemoryReleased=false`, adding a new memory tier, or granting raw memory
  release authority;
- spec exceeds 200 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1 +
T2 CLOSED_PASS and source-verified M1/AIF-C/WR1 vocabulary; no operator
checkpoint required unless a `canReinject` relaxation, new memory tier, or raw
memory release is discovered during implementation.

## Claim Boundary

LHW6-T3 produces a documentation artifact. It does not claim M1/AIF-C/WR1
runtime extension, memory reinjection, new memory tiers, raw memory release,
receipt envelope extension, provider behavior, hosted readiness, production
readiness, or public release readiness.
