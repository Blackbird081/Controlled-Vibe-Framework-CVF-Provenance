# CVF Work Order — LHW14-T2 Spec-Change Workflow Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement LHW14-T2: a connector spec mapping LHW11-T2 `specChangeGovernanceDecision`
× LHW11-T2 `rollbackRecommended` × LHW7-T3 `faultToRespecAdvisoryType` →
`specChangeWorkflowAdvisoryType` + `workflowPauseAdvisory`.

Source: LH1 `OpenSpec` PARTIALLY_ABSORBED trigger — "Reopen only if spec-change
workflow is selected." LHW11-T2 `specChangeGovernanceDecision` exists but no
connector maps it into a named workflow advisory for Orchestrators deciding
whether to pause and require spec review before acting on a change.

This connector is advisory only. It does NOT enforce spec-change behavior or
authorize governance override. `runtimeExecutionAuthorized=false`.

## Authority Chain

- LHW14 roadmap: `docs/roadmaps/CVF_LHW14_WORKFLOW_CONNECTOR_WAVE14_ROADMAP_2026-05-29.md`
- LHW14 GC-018: `docs/baselines/CVF_GC018_LHW14_WORKFLOW_CONNECTOR_WAVE14_2026-05-29.md`
- LHW11-T2 spec: `docs/reference/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_SPEC_2026-05-28.md`
- LHW7-T3 spec: `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md`
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (`OpenSpec` trigger at line 140)
- **T1 gate: `docs/reviews/CVF_LHW14_T1_AGENT_MEMORY_CAPTURE_PACKAGING_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS_BOUNDED**

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: `specChangeGovernanceDecision`
values individually row-verified in S5; `rollbackRecommended` boolean field
confirmed (not cited as false invariant); `faultToRespecAdvisoryType` values
covered; `runtimeExecutionAuthorized=false` explicit; no spec enforcement claimed.
Auditor confirms `OpenSpec` LH1 trigger cited; advisory-only posture preserved.
No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW14_T2_SPEC_CHANGE_WORKFLOW_ADVISORY_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW14_T2_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW14_T2_SPEC_CHANGE_WORKFLOW_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `specChangeGovernanceDecision` values at S2 mapping table;
   confirm `rollbackRecommended` boolean field at S3
4. `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `faultToRespecAdvisoryType` values at S3 line 112
5. `docs/reviews/CVF_LHW14_T1_AGENT_MEMORY_CAPTURE_PACKAGING_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md`
   — confirm T1 CLOSED_PASS_BOUNDED
6. `docs/roadmaps/CVF_LHW14_WORKFLOW_CONNECTOR_WAVE14_ROADMAP_2026-05-29.md`
   — confirm T2 deliverable and mapping design

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `specChangeGovernanceDecision` field | `docs/reference/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_SPEC_2026-05-28.md` | S3 line 78 | `specChangeGovernanceDecision` | LHW11-T2 doc-only field | ACCEPT |
| `rollbackRecommended` boolean field | `docs/reference/CVF_LHW11_T2_SPEC_CHANGE_GOVERNANCE_DECISION_CONNECTOR_SPEC_2026-05-28.md` | S3 line 79 | `rollbackRecommended` | LHW11-T2 doc-only field | ACCEPT |
| `faultToRespecAdvisoryType` field | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | S3 line 112 | `faultToRespecAdvisoryType` | LHW7-T3 doc-only field | ACCEPT |
| LH1 `OpenSpec` trigger | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 140 | `OpenSpec` | LH1 CVF 16.5 ledger | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `specChangeWorkflowAdvisoryType` | Names the spec-change workflow planning advisory | Yes |
| `workflowPauseAdvisory` | Plain-language guidance on whether to pause before acting on a spec change | Yes |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| T2 spec; LHW11-T2/LHW7-T3 field names verbatim | S1–S5 | spec at target path | Reviewer confirms verbatim | CLOSED_PASS |
| `specChangeGovernanceDecision` values individually row-verified | S5 | rows | No aggregate | CLOSED_PASS |
| `rollbackRecommended` treated as boolean, not invariant | S1, S3 | invariant statement | grep check | CLOSED_PASS |
| `faultToRespecAdvisoryType` values covered | S2, S5 | rows | Reviewer checks | CLOSED_PASS |
| LH1 `OpenSpec` trigger cited | S1 | explicit in S1 | Auditor checks | CLOSED_PASS |
| T1 gate confirmed | Authority Chain | T1 completion review | Read T1 review | CLOSED_PASS |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW14_T2_SPEC_CHANGE_WORKFLOW_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`

S2 design: map `specChangeGovernanceDecision` × `rollbackRecommended` ×
`faultToRespecAdvisoryType` → `specChangeWorkflowAdvisoryType` + `workflowPauseAdvisory`:

| `specChangeGovernanceDecision` | `rollbackRecommended` | `specChangeWorkflowAdvisoryType` | `workflowPauseAdvisory` |
| --- | --- | --- | --- |
| `spec_change_blocked_rollback_required` | `true` | `workflow_pause_rollback_required` | Pause all downstream work; initiate rollback before any spec change proceeds |
| `spec_change_deferred_review_required` | `false` | `workflow_pause_review_required` | Pause until human reviewer approves spec change |
| `spec_change_allowed_with_caution` | `false` | `workflow_proceed_with_caution` | Proceed; log change packet; monitor for fault reintake |
| `spec_change_allowed` | `false` | `workflow_proceed_clear` | Proceed; no pause required |

Key invariant: "This connector does not enforce spec-change behavior. The
workflow advisory is a governance planning record. `runtimeExecutionAuthorized=false`."

## Pre-Flight

- [x] Working tree clean
- [x] T1 CLOSED_PASS_BOUNDED confirmed
- [x] `specChangeGovernanceDecision` values confirmed from LHW11-T2 S2
- [x] `rollbackRecommended` confirmed as doc-only boolean from LHW11-T2 S3
- [x] `faultToRespecAdvisoryType` confirmed from LHW7-T3 S3 line 112
- [x] `OpenSpec` trigger confirmed from LH1 line 140

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads; confirm T1 gate.
2. Confirm all LHW11-T2 and LHW7-T3 symbols.
3. Draft spec; verify < 250 lines.
4. Run Fast Lane audit.
5. Run governance gates.
6. Update session continuity.
7. Commit.
8. Write completion review with T3 gate answer.

## Evidence Requirements

- Spec < 250 lines
- `specChangeGovernanceDecision` values individually row-verified
- `rollbackRecommended` treated as boolean field, not false invariant
- `faultToRespecAdvisoryType` values covered
- LH1 `OpenSpec` trigger cited in S1
- T1 gate confirmed
- No code file in diff

## Acceptance Criteria

- [x] T1 CLOSED_PASS_BOUNDED confirmed
- [x] Spec with all 5 sections; < 250 lines
- [x] `specChangeGovernanceDecision` values individually row-verified in S5
- [x] `rollbackRecommended` treated as boolean field, not false invariant
- [x] `faultToRespecAdvisoryType` values covered in S2 and S5
- [x] `runtimeExecutionAuthorized=false` explicit; no spec enforcement claimed
- [x] LH1 `OpenSpec` trigger cited in S1
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:
- T1 gate not confirmed
- Spec enforcement or governance override claimed
- Aggregate rows in S5

## Review Gate

T1 confirmed; `specChangeGovernanceDecision` values verified; `rollbackRecommended`
as boolean; no spec enforcement; `runtimeExecutionAuthorized=false`; spec < 250 lines;
no code file.

## Closure Checklist

- [x] T1 CLOSED_PASS_BOUNDED confirmed
- [x] Spec with all 5 sections
- [x] S2 mapping uses LHW11-T2/LHW7-T3 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 complete; no aggregate rows
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity updated
- [x] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop if: T1 gate missing; `specChangeGovernanceDecision` values cannot be confirmed;
connector requires spec enforcement or governance override; spec > 250 lines before S4.

## T3 Gate Output

Was a concrete noncoder clarification gap identified during T2?

**Expected YES:** T2 spec-change advisory reveals that when a noncoder operator
submits an ambiguous request, no connector maps C8 pack selection status ×
CB1 missing signals × WR1 recovery action → a named advisory guiding the
operator on what clarification is needed or what recovery step to take. T3
closes that gap.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW14-T2 produces a documentation artifact. It does not claim spec-change
enforcement, governance override, receipt envelope extension, provider behavior,
hosted readiness, production readiness, or public release readiness.
