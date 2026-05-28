# CVF Work Order — LHW7-T3 Failure Simulation Spec-Change Re-Intake Connector

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW7-T3: a connector spec binding LHW5-T3 failure simulation scenario
packet (`scenarioType`, `wr1RecoveryAction`, `lhw3TrendSignal`) → LHW3-T3
spec-change packet fields (`changeId`, `deltaDescription`, `affectedPhaseRange`,
`changePacketStatus`) → LHW3-T2 clarification re-intake packet type → WR1
`WorkflowRecoveryAction` into a single fault-to-respec advisory packet. Closes
the gap where no standard chains a failure scenario to a spec-change trigger,
re-intake type recommendation, and recovery action recommendation.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. Spec change execution and re-intake automation remain
blocked. T3 completes the LHW7 Workflow Connector Wave 7.

## Authority Chain

- LHW7 roadmap: `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
- LHW7 GC-018: `docs/baselines/CVF_GC018_LHW7_WORKFLOW_CONNECTOR_WAVE7_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW7_T3_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- T1 gate: `docs/reviews/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_COMPLETION_2026-05-28.md`
  — CLOSED_PASS_BOUNDED
- T2 gate: `docs/reviews/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_COMPLETION_2026-05-28.md`
  — CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `CVF Edit`, `Review CVF_3.md`)
- LHW5-T3 spec: `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md`
- LHW3-T3 spec: `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md`
- LHW3-T2 spec: `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`
- WR1 source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`

## Agent Roles

Implementer writes spec (S1–S5) using LHW5-T3, LHW3-T3, LHW3-T2, and WR1
vocabulary verbatim. Reviewer checks field names verbatim, `runtimeExecutionAuthorized=false`
and `scenarioPlanningOnly=true` invariants explicit, chain mapping honest, S5
Source Verification complete. Auditor confirms LH1 triggers recorded, no spec
change execution or re-intake automation claimed, LHW7 wave closure summary
present. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files
- LHW7 roadmap status update to `CLOSED_PASS_BOUNDED` on wave closure

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Spec change execution, re-intake automation, and workflow transitions remain
blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S3 fields: `scenarioType` values, `wr1RecoveryAction`,
   `lhw3TrendSignal`, `scenarioId`, `boundaryStatement`, `scenarioPlanningOnly=true`
4. `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S3 fields at lines 60–67: `changeId`, `deltaDescription`,
   `affectedPhaseRange`, `changePacketStatus` values
5. `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S2 clarification packet types at lines 47–50 (all 4 values)
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
   — confirm `WorkflowRecoveryAction` values at lines 50–54
7. `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
   — confirm T3 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| LHW5-T3 `scenarioType` values | `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 `scenarioType` | `scenarioType` | LHW5-T3 packet field | ACCEPT |
| LHW5-T3 `wr1RecoveryAction` | `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 `wr1RecoveryAction` | `wr1RecoveryAction` | LHW5-T3 packet field | ACCEPT |
| LHW5-T3 `lhw3TrendSignal` | `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 `lhw3TrendSignal` | `lhw3TrendSignal` | LHW5-T3 packet field | ACCEPT |
| LHW5-T3 `scenarioId` | `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 `scenarioId` | `scenarioId` | LHW5-T3 packet field | ACCEPT |
| LHW5-T3 `boundaryStatement` | `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 `boundaryStatement` | `boundaryStatement` | LHW5-T3 packet field | ACCEPT |
| LHW5-T3 `scenarioPlanningOnly=true` | `docs/reference/CVF_LHW5_FAILURE_SIMULATION_SCENARIO_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 `scenarioPlanningOnly` | `scenarioPlanningOnly` | LHW5-T3 invariant | ACCEPT |
| LHW3-T3 `changeId`, `deltaDescription`, `affectedPhaseRange`, `changePacketStatus` | `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md` | S3 lines 60–67 | LHW3-T3 packet fields | LHW3-T3 packet | ACCEPT |
| LHW3-T2 clarification packet types (all 4) | `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md` | S2 lines 47–50 | clarification packet type enum | LHW3-T2 packet | ACCEPT |
| WR1 `resume_from_checkpoint` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 51 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| WR1 `hold_for_reviewer_gate` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 52 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| WR1 `escalate_to_governance` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 53 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| WR1 `request_human_review` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 54 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| New doc-only fields `faultToRespecAdvisoryType`, `reIntakePacketTypeRecommended` | N/A — doc-only | S3 new fields | doc-only | Fault-to-respec advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T3 spec created; LHW5-T3/LHW3-T3/LHW3-T2/WR1 field names verbatim | S1–S5 | `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md` | Reviewer confirms source-verbatim field names | BLOCKED until spec exists |
| `runtimeExecutionAuthorized=false` and `scenarioPlanningOnly=true` explicit | S1, S3, Claim Boundary | invariants in S1 and S3 | `rg -n "runtimeExecutionAuthorized=false\|scenarioPlanningOnly=true" <spec>` | BLOCKED until spec exists |
| Fault-to-respec chain mapping covering 6 scenario types | S2 | 6 chain rows with LHW3-T2 type + WR1 action per row | Reviewer checks S2 rows | BLOCKED until spec exists |
| Source Verification Table complete | S5 | Source Verification Table | `rg -n "Disposition" <spec>` plus reviewer check | BLOCKED until spec exists |
| LHW7 wave closure summary | Completion review | T1 + T2 + T3 table all CLOSED_PASS_BOUNDED | Completion review filed | BLOCKED until closure |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md`

Required sections S1–S5. See LHW7 roadmap for full deliverable shape.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] LHW5-T3 field names confirmed from source
- [ ] LHW3-T3 field names confirmed from source
- [ ] LHW3-T2 clarification packet types confirmed from source
- [ ] WR1 `WorkflowRecoveryAction` values confirmed from source

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all field names from source files.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw7_t3_complete`).
7. Update LHW7 roadmap status to `CLOSED_PASS_BOUNDED`.
8. Commit: `docs(lhw7-t3): add failure sim spec-change re-intake connector spec`.
9. Write completion review with LHW7 wave closure summary.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 chain mapping covers all 6 LHW5-T3 `scenarioType` values
- `runtimeExecutionAuthorized=false` and `scenarioPlanningOnly=true` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw7_t3_complete`
- LHW7 roadmap updated to `CLOSED_PASS_BOUNDED`
- Completion review written with LHW7 wave closure summary

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 chain mapping covers all 6 scenario types
- [ ] `runtimeExecutionAuthorized=false` and `scenarioPlanningOnly=true` invariants explicit
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] LHW7 roadmap updated to `CLOSED_PASS_BOUNDED`

Fail conditions:

- [ ] Missing LHW7 GC-018 baseline, missing Source Verification row, or
  Source Verification `ACCEPT` row citing a non-existent file
- [ ] Any claim that this connector executes spec changes, automates re-intake
  actions, triggers workflow transitions, or lifts `runtimeExecutionAuthorized=false`

## Review Gate

Before committing: Reviewer perspective completed; all LHW5-T3/LHW3-T3/LHW3-T2/WR1
field names verbatim; `runtimeExecutionAuthorized=false` and `scenarioPlanningOnly=true`
explicit; S5 complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; no code file
in diff.

## Closure Checklist

- [ ] Spec created with all 5 sections
- [ ] S2 chain mapping uses LHW5-T3/LHW3-T3/LHW3-T2/WR1 vocabulary verbatim
- [ ] `runtimeExecutionAuthorized=false` and `scenarioPlanningOnly=true` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] LHW7 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] Completion review with LHW7 wave closure summary written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T2 completion review is not CLOSED_PASS_BOUNDED before proceeding;
- any required first read file is missing;
- a LHW5-T3, LHW3-T3, LHW3-T2, or WR1 field token cannot be confirmed from
  source files;
- writing the connector requires executing a spec change, automating re-intake,
  or lifting `runtimeExecutionAuthorized=false`;
- spec exceeds 250 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified LHW5-T3/LHW3-T3/LHW3-T2/WR1 vocabulary; T1 + T2 gates
confirmed; no operator checkpoint required unless a spec-change execution
authorization or `scenarioPlanningOnly=false` relaxation is discovered during
implementation.

## Claim Boundary

LHW7-T3 produces a documentation artifact. It does not claim LHW5-T3/LHW3-T3/
LHW3-T2/WR1 runtime extension, spec-change execution, re-intake automation,
workflow transition execution, receipt envelope extension, provider behavior,
hosted readiness, production readiness, or public release readiness. T3
completes the LHW7 wave; any further connector wave requires a fresh roadmap
and GC-018.
