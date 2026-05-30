# CVF Work Order — LHW11-T2 Spec-Change Governance Decision Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW11-T2: a second-order connector spec that maps LHW7-T3
`faultToRespecAdvisoryType` (6 values) × LHW10-T1
`transitionEnforcementAdvisoryType` × LHW3-T3 `changePacketStatus` (3 values)
into a named `specChangeGovernanceDecision` + `rollbackRecommended` boolean.

LH1 triggers: `Review CVF_5.md` (PARTIALLY_ABSORBED — code-level enforcement
themes); `CVF_EDIT_ANALYSIS.md` (PARTIALLY_ABSORBED — next runtime workflow
hardening tranche).

Gap: when a failure-sim triggers a spec change (LHW7-T3) AND a workflow
transition enforcement advisory is active (LHW10-T1), no connector maps both
into a named governance decision + rollback recommendation. An Orchestrator
must infer this manually.

## Authority Chain

- LHW11 roadmap: `docs/roadmaps/CVF_LHW11_WORKFLOW_CONNECTOR_WAVE11_ROADMAP_2026-05-28.md`
- LHW11 GC-018: `docs/baselines/CVF_GC018_LHW11_WORKFLOW_CONNECTOR_WAVE11_2026-05-28.md`
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `Review CVF_5.md`, `CVF_EDIT_ANALYSIS.md`)
- LHW7-T3 spec: `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md`
- LHW10-T1 spec: `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LHW3-T3 spec: `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md`
- **T1 gate: `docs/reviews/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_COMPLETION_2026-05-28.md`
  must be CLOSED_PASS_BOUNDED before dispatch**

## Agent Roles

Implementer writes spec (S1–S5) using LHW7-T3, LHW10-T1, and LHW3-T3
vocabulary verbatim. Reviewer checks all 6 `faultToRespecAdvisoryType` values
individually row-verified in S5, all 3 `changePacketStatus` values individually
row-verified in S5, `runtimeExecutionAuthorized=false` explicit. Auditor
confirms LH1 triggers recorded. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_SPEC_2026-05-28.md`
  (new)
- `docs/reviews/CVF_LHW11_T2_FAST_LANE_AUDIT_2026-05-28.md` (new)
- `docs/reviews/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_COMPLETION_2026-05-28.md`
  (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `faultToRespecAdvisoryType` values at S2 lines 75–81
4. `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `transitionEnforcementAdvisoryType` S2 mapping for posture-blocked values
5. `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md`
   — confirm `changePacketStatus` values at S3 line 67: `pending_approval`, `approved`, `rejected`
6. `docs/reviews/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_COMPLETION_2026-05-28.md`
   — confirm T1 CLOSED_PASS_BOUNDED (gate check)

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `faultToRespecAdvisoryType` field | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S3 line 112 | `faultToRespecAdvisoryType` | LHW7-T3 doc-only field | ACCEPT |
| `spec_exception_required` | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S2 line 75 | `faultToRespecAdvisoryType` value | LHW7-T3 S2 mapping | ACCEPT |
| `spec_retry_boundary_update` | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S2 line 76 | `faultToRespecAdvisoryType` value | LHW7-T3 S2 mapping | ACCEPT |
| `spec_success_criteria_tighten` | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S2 lines 77–78 | `faultToRespecAdvisoryType` value | LHW7-T3 S2 mapping | ACCEPT |
| `spec_human_gate_insertion` | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S2 line 79 | `faultToRespecAdvisoryType` value | LHW7-T3 S2 mapping | ACCEPT |
| `spec_route_constraint_update` | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S2 line 80 | `faultToRespecAdvisoryType` value | LHW7-T3 S2 mapping | ACCEPT |
| `spec_fallback_model_update` | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S2 line 81 | `faultToRespecAdvisoryType` value | LHW7-T3 S2 mapping | ACCEPT |
| `transitionEnforcementAdvisoryType` field | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 137 | `transitionEnforcementAdvisoryType` | LHW10-T1 doc-only field | ACCEPT |
| `escalated_blocked` | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 lines 88, 90, 94, 98, 102 | `transitionEnforcementAdvisoryType` blocked-tier value | LHW10-T1 S2 mapping | ACCEPT |
| `pending_approval` | `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 line 67 | `changePacketStatus` value | LHW3-T3 doc-only field | ACCEPT |
| `approved` | `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 line 67 | `changePacketStatus` value | LHW3-T3 doc-only field | ACCEPT |
| `rejected` | `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 line 67 | `changePacketStatus` value | LHW3-T3 doc-only field | ACCEPT |
| `specChangeGovernanceDecision` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Spec-change governance decision packet | ACCEPT |
| `rollbackRecommended` (new) | N/A — canonical doc-only field | S3 new fields | doc-only boolean | Spec-change governance decision packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification | Status |
| --- | --- | --- | --- | --- |
| T2 spec; LHW7-T3/LHW10-T1/LHW3-T3 field names verbatim | S1–S5 | spec at target path | Reviewer confirms verbatim | CLOSED |
| `rollbackRecommended` boolean explicit | S3 | boolean field with derivation rule | Reviewer checks S3 | CLOSED |
| All 6 `faultToRespecAdvisoryType` values individually row-verified | S5 | 6 rows | No aggregate | CLOSED |
| All 3 `changePacketStatus` values individually row-verified | S5 | 3 rows | No aggregate | CLOSED |
| `runtimeExecutionAuthorized=false` explicit | S1, S3 | invariant | `rg` check | CLOSED |
| T1 gate confirmed | Authority Chain | T1 completion review | Read T1 review | CLOSED |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_SPEC_2026-05-28.md`

S2 design: map `faultToRespecAdvisoryType` × whether transition enforcement
advisory is in BLOCKED tier → `specChangeGovernanceDecision` value +
`rollbackRecommended` boolean.

Key mapping logic:
- If `faultToRespecAdvisoryType` ∈ `{spec_exception_required, spec_route_constraint_update}`
  AND `transitionEnforcementAdvisoryType` is in BLOCKED tier → `spec_change_blocked_rollback_required`, `rollbackRecommended=true`
- If `faultToRespecAdvisoryType` ∈ `{spec_retry_boundary_update, spec_fallback_model_update}`
  AND `changePacketStatus=pending_approval` → `spec_change_pending_approval`, `rollbackRecommended=false`
- If `faultToRespecAdvisoryType` = `spec_success_criteria_tighten` → `spec_change_review_required`, `rollbackRecommended=false`
- If `faultToRespecAdvisoryType` = `spec_human_gate_insertion` → `spec_change_human_gate_required`, `rollbackRecommended=false`
- If `changePacketStatus=rejected` → `spec_change_rejected_revert`, `rollbackRecommended=true`
- If `changePacketStatus=approved` AND no BLOCKED advisory → `spec_change_approved_proceed`, `rollbackRecommended=false`

Invariants: "This connector does not execute spec changes or mutate workflow
state." `runtimeExecutionAuthorized=false`.

## Pre-Flight

- [x] Working tree clean
- [x] T1 CLOSED_PASS_BOUNDED confirmed
- [x] All `faultToRespecAdvisoryType` values confirmed from LHW7-T3 S2
- [x] All `changePacketStatus` values confirmed from LHW3-T3 S3

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads; confirm T1 gate.
2. Confirm all input field values from source specs.
3. Draft spec (S1–S5); verify line count < 250 after S4.
4. Run Fast Lane audit.
5. Run governance gates.
6. Reviewer perspective.
7. Update session continuity.
8. Commit.
9. Write completion review with T3 gate answer.

## Evidence Requirements

- Spec < 250 lines
- All 6 `faultToRespecAdvisoryType` values individually row-verified in S5
- All 3 `changePacketStatus` values individually row-verified in S5
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- T1 gate confirmed before dispatch
- No code file in diff

## Acceptance Criteria

- [x] T1 CLOSED_PASS_BOUNDED confirmed before dispatch
- [x] Spec with all 5 sections; < 250 lines
- [x] All 6 `faultToRespecAdvisoryType` values individually row-verified in S5
- [x] All 3 `changePacketStatus` values individually row-verified in S5
- [x] `rollbackRecommended` boolean with derivation rule explicit in S3
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:

- T1 gate not confirmed
- `rollbackRecommended` claimed as runtime enforcement
- Aggregate rows in S5 for `faultToRespecAdvisoryType` or `changePacketStatus`

## Review Gate

Before committing: T1 gate confirmed; all input field names verbatim; all 9
individual enum value rows in S5; `runtimeExecutionAuthorized=false`; spec < 250
lines; no code file.

## Closure Checklist

- [x] T1 CLOSED_PASS_BOUNDED confirmed
- [x] Spec with all 5 sections
- [x] S2 maps `faultToRespecAdvisoryType` × transition posture → governance decision
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 Source Verification: no aggregate rows
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity updated
- [x] Completion review with T3 gate answer

## Return-To-Orchestrator Conditions

Stop if: T1 gate missing; any source spec token cannot be confirmed; writing
requires spec mutation or transition execution; spec exceeds 250 lines before S4.

## T3 Gate Output

Was a concrete memory context seed decay advisory gap identified during T2?

**YES** — T2 spec-change decision mapping reveals that when a spec change is pending AND memory snapshot advisory shows contaminated context (`memorySnapshotAdvisoryType=snapshot_redacted_capture` or `snapshot_approval_pending`), no connector maps this combination + LHW7-T2 `signalsStillMissing` + AIF-C `MemoryGatewayDecision.decision` into a named `memoryContextSeedDecayAdvisoryType`. T3 closes that gap.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW11-T2 produces a documentation artifact. It does not claim spec mutation,
workflow state change, rollback execution, memory reinjection, receipt envelope
extension, provider behavior, hosted readiness, production readiness, or public
release readiness.
