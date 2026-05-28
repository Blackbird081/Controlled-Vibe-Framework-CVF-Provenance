# CVF Work Order — LHW10-T1 Workflow Transition Enforcement Advisory Connector

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW10-T1: a connector spec binding W1
`WorkflowStateMachineProjection.finalState` + WR1
`WorkflowRequestedTransitionDisposition` (4 values) + WR1
`WorkflowRecoveryAction` (4 values) + LHW7-T1 `reEntryAdvisoryType` (5 values)
into a transition enforcement advisory packet. Closes the gap where no standard
maps transition disposition × recovery action → a named
`transitionEnforcementAdvisoryType` + `invalidTransitionDisposition`.

LH1 triggers: `Agent Harnesses` (PARTIALLY_ABSORBED — workflow resume/recovery
proof); `Review CVF_3.md` (PARTIALLY_ABSORBED — route-level invalid-transition
enforcement). Documentation-only tranche. No workflow transition execution or
state mutation.

## Authority Chain

- LHW10 roadmap: `docs/roadmaps/CVF_LHW10_WORKFLOW_CONNECTOR_WAVE10_ROADMAP_2026-05-28.md`
- LHW10 GC-018: `docs/baselines/CVF_GC018_LHW10_WORKFLOW_CONNECTOR_WAVE10_2026-05-28.md`
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `Agent Harnesses`, `Review CVF_3.md`)
- W1 completion: `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- WR1 completion: `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_READOUT_COMPLETION_2026-05-25.md`
- LHW7-T1 spec: `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md`

## Agent Roles

Implementer writes spec (S1–S5) using W1, WR1, and LHW7-T1 vocabulary verbatim.
Reviewer checks all `WorkflowRecoveryAction` values verbatim, all
`WorkflowRequestedTransitionDisposition` values verbatim, all LHW7-T1
`reEntryAdvisoryType` values verbatim, `runtimeExecutionAuthorized=false`
explicit, boundary table honest, S5 Source Verification complete with individual
rows per enum value. Auditor confirms LH1 triggers recorded, no workflow
transition execution claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- `docs/reviews/CVF_LHW10_T1_FAST_LANE_AUDIT_2026-05-28.md` (new)
- `docs/reviews/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
  (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo,
workflow execution, state mutation.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
   — confirm `WorkflowRecoveryAction` values at lines 50–54;
   confirm `WorkflowRequestedTransitionDisposition` values at lines 56–60;
   confirm `WorkflowRecoveryReadout.currentState` at line 88;
   confirm `WorkflowStateMachineProjection.finalState` at line 201
4. `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `reEntryAdvisoryType` values `safe_reentry`, `reapproval_required`,
   `blocked_no_reentry`, `blocked_pending_reviewer`, `escalated_no_reentry` at S3
5. `docs/roadmaps/CVF_LHW10_WORKFLOW_CONNECTOR_WAVE10_ROADMAP_2026-05-28.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `WorkflowStateMachineProjection` interface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 39 | `export interface WorkflowStateMachineProjection` | `WorkflowStateMachineProjection` | ACCEPT |
| `WorkflowStateMachineProjection.finalState` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 201 | `finalState: currentState` | `WorkflowStateMachineProjection` | ACCEPT |
| `WorkflowRecoveryReadout` interface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 85 | `export interface WorkflowRecoveryReadout` | `WorkflowRecoveryReadout` | ACCEPT |
| `WorkflowRecoveryReadout.currentState` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 88 | `readonly currentState: string` | `WorkflowRecoveryReadout` | ACCEPT |
| `WorkflowRecoveryReadout.recoveryAction` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 92 | `readonly recoveryAction: WorkflowRecoveryAction` | `WorkflowRecoveryReadout` | ACCEPT |
| `WorkflowRequestedTransitionReadout.disposition` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 80 | `readonly disposition: WorkflowRequestedTransitionDisposition` | `WorkflowRequestedTransitionReadout` | ACCEPT |
| `resume_from_checkpoint` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 51 | `WorkflowRecoveryAction` union type | `WorkflowRecoveryAction` | ACCEPT |
| `hold_for_reviewer_gate` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 52 | `WorkflowRecoveryAction` union type | `WorkflowRecoveryAction` | ACCEPT |
| `escalate_to_governance` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 53 | `WorkflowRecoveryAction` union type | `WorkflowRecoveryAction` | ACCEPT |
| `request_human_review` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 54 | `WorkflowRecoveryAction` union type | `WorkflowRecoveryAction` | ACCEPT |
| `valid_from_current_state` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 57 | `WorkflowRequestedTransitionDisposition` union type | `WorkflowRequestedTransitionDisposition` | ACCEPT |
| `invalid_from_current_state` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 58 | `WorkflowRequestedTransitionDisposition` union type | `WorkflowRequestedTransitionDisposition` | ACCEPT |
| `configured_deferred_gate` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 59 | `WorkflowRequestedTransitionDisposition` union type | `WorkflowRequestedTransitionDisposition` | ACCEPT |
| `no_requested_transition` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 60 | `WorkflowRequestedTransitionDisposition` union type | `WorkflowRequestedTransitionDisposition` | ACCEPT |
| `safe_reentry` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 110 | `reEntryAdvisoryType` value | LHW7-T1 doc-only field | ACCEPT |
| `reapproval_required` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 110 | `reEntryAdvisoryType` value | LHW7-T1 doc-only field | ACCEPT |
| `blocked_no_reentry` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 110 | `reEntryAdvisoryType` value | LHW7-T1 doc-only field | ACCEPT |
| `blocked_pending_reviewer` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 111 | `reEntryAdvisoryType` value | LHW7-T1 doc-only field | ACCEPT |
| `escalated_no_reentry` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 111 | `reEntryAdvisoryType` value | LHW7-T1 doc-only field | ACCEPT |
| `transitionEnforcementAdvisoryType` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Transition enforcement advisory packet | ACCEPT |
| `invalidTransitionDisposition` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Transition enforcement advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T1 spec; W1/WR1/LHW7-T1 field names verbatim | S1–S5 | spec at target path | Reviewer confirms source-verbatim field names | OPEN |
| Transition execution blocked explicit | S1, S3, Claim Boundary | `runtimeExecutionAuthorized=false`; explicit not-execute statement | `rg -n "runtimeExecutionAuthorized=false" <spec>` | OPEN |
| S2 maps all 4 `WorkflowRecoveryAction` values | S2 | 4 recovery action rows mapped | Reviewer checks S2 rows | OPEN |
| S2 maps all 4 `WorkflowRequestedTransitionDisposition` values | S2 | 4 disposition rows mapped | Reviewer checks S2 rows | OPEN |
| S5 Source Verification Table: individual rows per enum value | S5 | all ACCEPT, no aggregates | Reviewer checks no `BLOCKED_SOURCE_NOT_FOUND` | OPEN |
| No code file modified | Evidence Requirements | git diff output | `git diff --name-only` | OPEN |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

Spec must include 5 sections: S1 Purpose and Claim Boundary; S2 Transition
Disposition × Recovery Action → Enforcement Advisory Mapping (table with all
meaningful combinations of 4 `WorkflowRequestedTransitionDisposition` × 4
`WorkflowRecoveryAction` values); S3 Minimum Fields; S4 Boundary Table; S5
Source Verification Table (individual rows per enum value).

Key invariants:
- "This connector does not execute workflow transitions or modify workflow state."
- `runtimeExecutionAuthorized=false` explicit in S1 and S3.
- "Prior `reEntryAdvisoryType` does not override `escalate_to_governance`."

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] `WorkflowRecoveryAction` and `WorkflowRequestedTransitionDisposition`
  values confirmed from source (lines 50–60 of `workflow-resolver.ts`)
- [ ] LHW7-T1 `reEntryAdvisoryType` values confirmed from S3

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all W1/WR1/LHW7-T1 field names and enum values from source.
3. Draft spec (S1–S5) with Source Verification Table (individual rows per
   enum value — no aggregate rows for multi-value types).
4. Run Fast Lane audit.
5. Confirm no code file staged.
6. Run governance gates:
   `check_work_order_dispatch_quality.py --base 118b8d48 --head HEAD --enforce`
   `check_markdown_structural_completeness.py --base 118b8d48 --head HEAD --enforce`
7. Reviewer perspective — record result.
8. Update session continuity.
9. Commit.
10. Write completion review; include T2 gate answer.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps all 4 `WorkflowRecoveryAction` + all 4 `WorkflowRequestedTransitionDisposition`
  value combinations
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; individual row per enum value; no
  `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in diff
- Session continuity updated
- Completion review with T2 gate answer written

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 maps all 4 `WorkflowRecoveryAction` values and all 4 `WorkflowRequestedTransitionDisposition` values
- [ ] All 5 LHW7-T1 `reEntryAdvisoryType` values individually row-verified in S5
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no aggregate rows
- [ ] No code file in diff
- [ ] Session continuity updated

Fail conditions:

- Missing LHW10 GC-018 baseline or Source Verification `ACCEPT` row citing
  a non-existent file
- Any claim that this connector executes workflow transitions, modifies workflow
  state, or lifts `runtimeExecutionAuthorized=false`
- Aggregate rows in S5 for multi-value types

## Review Gate

Before committing: all W1/WR1/LHW7-T1 field names verbatim; all enum values
individually row-verified; `runtimeExecutionAuthorized=false` explicit; S5
complete with no aggregate rows; no code file in diff.

## Closure Checklist

- [ ] Spec created with all 5 sections
- [ ] S2 transition advisory mapping uses W1/WR1/LHW7-T1 vocabulary verbatim
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S5 Source Verification Table complete; no aggregate rows; no
  `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Fast Lane audit created
- [ ] Session continuity updated
- [ ] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop if: any required first read file is missing; a W1, WR1, or LHW7-T1 token
cannot be confirmed; writing the connector requires workflow transition execution
or lifts `runtimeExecutionAuthorized=false`; spec exceeds 250 lines before S4.

## T2 Gate Output

This section is completed by Implementer after T1 spec is delivered.

Was a concrete runtime maturity evidence chain gap identified during T1?

**Expected YES:** T1 transition enforcement mapping reveals that while
`WorkflowStateMachineProjection.finalState` (W1), `recoveryAction` (WR1), and
`authorityChainAdvisoryType` (LHW8-T2) all exist, no connector maps their
combined evidence posture to a named `runtimeMaturityAdvisoryType` identifying
which surface gap exists. T2 closes that gap.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche; no operator
checkpoint required unless workflow transition execution or new execution
authority is discovered.

## Claim Boundary

LHW10-T1 produces a documentation artifact. It does not claim W1/WR1/LHW7-T1
runtime extension, workflow transition execution, workflow state mutation,
runtime enforcement, memory injection, receipt envelope extension, provider
behavior, hosted readiness, production readiness, or public release readiness.
