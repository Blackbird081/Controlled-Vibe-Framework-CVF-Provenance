# CVF Work Order — LHW12-T3 Async Worker Lifecycle Boundary Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement LHW12-T3: a connector spec mapping WR1 `WorkflowRecoveryAction`
(4 values) × MA1 role lanes (4 values: Orchestrator/Implementer/Reviewer/
Auditor) × LHW10-T1 `transitionEnforcementAdvisoryType` →
`workerLifecycleAdvisoryType` + `spawnAuthorizationAdvisory` +
`maxScopeAdvisory`.

Source: CVF 25.05 Gop_y.md Gap 7 — subagent spawn boundary is undefined (not
allowed, not forbidden). LH1 `deepagents` trigger: "bounded worker delegation
proof; no autonomous queues." No connector maps recovery action × role × enforcement advisory → a named lifecycle advisory telling Orchestrators when a
worker sub-task is advisory-eligible and what boundary applies.

This connector is advisory only. It does NOT spawn subagents or authorize
autonomous execution. `runtimeExecutionAuthorized=false` invariant.

## Authority Chain

- LHW12 roadmap: `docs/roadmaps/CVF_LHW12_WORKFLOW_CONNECTOR_WAVE12_ROADMAP_2026-05-29.md`
- LHW12 GC-018: `docs/baselines/CVF_GC018_LHW12_WORKFLOW_CONNECTOR_WAVE12_2026-05-29.md`
- WR1 completion: `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_READOUT_COMPLETION_2026-05-25.md`
- MA1 completion: `docs/reviews/archive/CVF_MA1_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_COMPLETION_2026-05-26.md`
- LHW10-T1 spec: `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (`deepagents` trigger at line 156)
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  (GAP 7 section)
- **T1 gate: `docs/reviews/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS_BOUNDED**
- **T2 gate: `docs/reviews/CVF_LHW12_T2_OUTCOME_PACK_TAXONOMY_GROUPING_CONNECTOR_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS_BOUNDED**

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: all 4 `WorkflowRecoveryAction`
values individually row-verified in S5; all 4 MA1 role lane values individually
row-verified; `runtimeExecutionAuthorized=false` explicit; no subagent spawn
claimed; LH1 `deepagents` trigger cited. Auditor confirms CVF 25.05 Gap 7
recorded; no autonomous execution claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW12_T3_ASYNC_WORKER_LIFECYCLE_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW12_T3_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW12_T3_ASYNC_WORKER_LIFECYCLE_BOUNDARY_CONNECTOR_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files (including LHW12 roadmap status + handoff)

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
   — confirm `WorkflowRecoveryAction` values at lines 50–54:
   `resume_from_checkpoint`, `hold_for_reviewer_gate`, `escalate_to_governance`,
   `request_human_review`
4. `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   — confirm MA1 role lanes at lines 96–99: `Orchestrator`, `Implementer`,
   `Reviewer`, `Auditor`
5. `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `transitionEnforcementAdvisoryType` blocked-tier values at S2
6. `docs/reviews/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md`
   — confirm T1 CLOSED_PASS_BOUNDED
7. `docs/reviews/CVF_LHW12_T2_OUTCOME_PACK_TAXONOMY_GROUPING_CONNECTOR_COMPLETION_2026-05-29.md`
   — confirm T2 CLOSED_PASS_BOUNDED

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `WorkflowRecoveryAction` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 50 | `export type WorkflowRecoveryAction` | `WorkflowRecoveryAction` | ACCEPT |
| `resume_from_checkpoint` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 51 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `hold_for_reviewer_gate` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 52 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `escalate_to_governance` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 53 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `request_human_review` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 54 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `Orchestrator` role lane | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | line 96 | `Orchestrator` | MA1 role lane | ACCEPT |
| `Implementer` role lane | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | line 97 | `Implementer` | MA1 role lane | ACCEPT |
| `Reviewer` role lane | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | line 98 | `Reviewer` | MA1 role lane | ACCEPT |
| `Auditor` role lane | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | line 99 | `Auditor` | MA1 role lane | ACCEPT |
| `transitionEnforcementAdvisoryType` field | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 137 | `transitionEnforcementAdvisoryType` | LHW10-T1 doc-only field | ACCEPT |
| `escalated_blocked` | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 lines 88–102 | blocked-tier value | LHW10-T1 S2 mapping | ACCEPT |
| LH1 `deepagents` trigger | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 156 | `deepagents` | LH1 CVF ADD ledger | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `workerLifecycleAdvisoryType` | Names the worker lifecycle planning advisory. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |
| `spawnAuthorizationAdvisory` | Records advisory-only spawn posture without runtime authority. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |
| `maxScopeAdvisory` | States the maximum advisory scope for a worker sub-task. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| T3 spec; WR1/MA1/LHW10-T1 field names verbatim | S1–S5 | spec at target path | Reviewer confirms verbatim | CLOSED |
| All 4 `WorkflowRecoveryAction` values individually row-verified | S5 | 4 rows | No aggregate | CLOSED |
| All 4 MA1 role lane values individually row-verified | S5 | 4 rows | No aggregate | CLOSED |
| LH1 `deepagents` trigger cited | S1 | explicit in S1 Purpose | Auditor checks | CLOSED |
| `runtimeExecutionAuthorized=false` explicit | S1, S3 | invariant | grep check | CLOSED |
| T1 AND T2 gates confirmed | Authority Chain | both completion reviews | Read both | CLOSED |
| LHW12 wave closure summary in completion review | Closure Checklist | T1+T2+T3 table | Reviewer checks | CLOSED |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW12_T3_ASYNC_WORKER_LIFECYCLE_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md`

S2 design: map `WorkflowRecoveryAction` × MA1 role lane × enforcement advisory
tier → `workerLifecycleAdvisoryType` + `spawnAuthorizationAdvisory` +
`maxScopeAdvisory`.

Key rows:

| `recoveryAction` | MA1 role | Enforcement tier | `workerLifecycleAdvisoryType` | `spawnAuthorizationAdvisory` | `maxScopeAdvisory` |
| --- | --- | --- | --- | --- | --- |
| `resume_from_checkpoint` | `Implementer` | CLEAR | `worker_eligible_bounded` | `advisory_allowed_with_scope_limit` | single workflow step; receipt required |
| `resume_from_checkpoint` | `Orchestrator` | CLEAR | `worker_eligible_orchestrator_scope` | `advisory_allowed` | full workflow sub-task; MA1 transfer required |
| `hold_for_reviewer_gate` | any | HOLD | `worker_suspended_pending_gate` | `advisory_suspended` | no sub-tasks until gate clears |
| `escalate_to_governance` | any | BLOCKED | `worker_blocked_governance_escalation` | `advisory_blocked` | no spawn; escalate to governance |
| `request_human_review` | any | any | `worker_suspended_human_review` | `advisory_deferred` | no spawn until human review completes |

Key invariant in S1: "This connector does not spawn subagents or authorize
autonomous execution. The lifecycle advisory is a governance planning record.
`runtimeExecutionAuthorized=false`. Spawn authorization advisory is advisory
only — no runtime spawn gate."

## Pre-Flight

- [x] Working tree clean
- [x] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [x] `WorkflowRecoveryAction` values confirmed from workflow-resolver.ts lines 50–54
- [x] MA1 role lanes confirmed from MA1 standard lines 96–99
- [x] LH1 `deepagents` trigger at line 156 confirmed

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads; confirm T1 and T2 gates.
2. Confirm all WR1/MA1/LHW10-T1 symbols from source.
3. Draft spec (S1–S5); verify < 250 lines.
4. Run Fast Lane audit.
5. Run governance gates with `--base 7de75901`.
6. Reviewer perspective.
7. Update session continuity; mark LHW12 CLOSED_PASS_BOUNDED.
8. Update LHW12 roadmap: Status → CLOSED_PASS_BOUNDED; actual commit SHA in
   Verification section.
9. Commit.
10. Write completion review with LHW12 wave closure summary.

## Evidence Requirements

- Spec < 250 lines
- All 4 WR1 `WorkflowRecoveryAction` + all 4 MA1 role lanes individually row-verified
- LH1 `deepagents` trigger cited in S1
- `runtimeExecutionAuthorized=false` explicit
- T1 AND T2 gates confirmed
- No code file in diff
- LHW12 wave closure summary in completion review

## Acceptance Criteria

- [x] T1 AND T2 CLOSED_PASS_BOUNDED confirmed before dispatch
- [x] Spec with all 5 sections; < 250 lines
- [x] All 4 `WorkflowRecoveryAction` values individually row-verified in S5
- [x] All 4 MA1 role lane values individually row-verified in S5
- [x] LH1 `deepagents` trigger cited in S1
- [x] `runtimeExecutionAuthorized=false` explicit; no subagent spawn claimed
- [x] No code file in diff
- [x] Session continuity updated; LHW12 CLOSED_PASS_BOUNDED
- [x] LHW12 roadmap Status → CLOSED_PASS_BOUNDED; actual commit SHA in Verification
- [x] Completion review includes LHW12 wave closure summary table

Fail conditions:
- T1 or T2 gate not confirmed
- WR1 or MA1 values aggregated in S5
- Any claim that connector spawns subagents or authorizes autonomous execution
- Completion review missing LHW12 wave closure summary

## Review Gate

T1 and T2 confirmed; all WR1 (4) + MA1 (4) individually verified; `runtimeExecutionAuthorized=false`; `deepagents` trigger cited; spec < 250 lines; no code file.

## Closure Checklist

- [x] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [x] Spec with all 5 sections
- [x] S2 mapping uses WR1/MA1/LHW10-T1 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit; no subagent spawn
- [x] S5 complete; no aggregate rows
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity: LHW12 CLOSED_PASS_BOUNDED
- [x] LHW12 roadmap updated with actual commit SHA + Status CLOSED_PASS_BOUNDED
- [x] Completion review with LHW12 wave closure summary written

## Return-To-Orchestrator Conditions

Stop if: T1 or T2 gate missing; WR1/MA1 tokens cannot be confirmed; connector
requires subagent spawn or autonomous execution; spec > 250 lines before S4.

## LHW12 Wave Closure Gate

After T3 committed, completing agent must update:
1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`: `lhw12WorkflowConnectorWave12.status = CLOSED_PASS_BOUNDED`; `nextAllowedMove` names LHW12 as latest fully closed after all 3 tranches reach CLOSED_PASS_BOUNDED
2. `CVF_SESSION_MEMORY.md` Next Allowed Move: reference LHW12 CLOSED_PASS_BOUNDED
3. Active handoff: add LHW12 wave closure note with contract versions + commit SHA

Failure to update all three blocks the Latest-Closure Continuity Gate.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW12-T3 produces a documentation artifact. It does not claim subagent
spawning, autonomous worker execution, worker lifecycle enforcement, pipeline
chain dispatch, memory reinjection, receipt envelope extension, provider
behavior, hosted readiness, production readiness, or public release readiness.
