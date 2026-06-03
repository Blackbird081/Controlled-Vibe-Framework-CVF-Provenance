# CVF Work Order — LHW7-T1 Workflow Recovery → Tool Bridge Re-Entry Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW7-T1: a connector spec binding WR1 `WorkflowRecoveryAction` +
`lastRestorableCheckpoint` → LHW6-T1 `bridgeAdvisoryType` → TA1
`ToolActionApprovalState` into a single Orchestrator-readable re-entry advisory
packet. Closes the gap where WR1 says which step to restart, LHW6-T1 says how
to bridge each tool surface, and TA1 says whether approval is needed — but no
connector says whether prior approval survives a restart.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. Tool re-execution remains blocked.

## Authority Chain

- LHW7 roadmap: `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
- LHW7 GC-018: `docs/baselines/CVF_GC018_LHW7_WORKFLOW_CONNECTOR_WAVE7_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW7_T1_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- LH1 ledger triggers (`Agent Harnesses`, `OpenAgentd`):
  `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- WR1: `docs/reviews/archive/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
- LHW6-T1: `docs/reviews/CVF_LHW6_T1_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
- TA1: `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`

## Agent Roles

Implementer writes spec (S1–S5) using WR1, LHW6-T1, and TA1 vocabulary verbatim.
Reviewer checks all `WorkflowRecoveryAction` values verbatim, all
`ToolActionApprovalState` values verbatim, all `bridgeAdvisoryType` values
verbatim, `runtimeExecutionAuthorized=false` explicit, boundary table honest,
S5 Source Verification complete. Auditor confirms LH1 triggers recorded, no tool
re-execution or approval-automation claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Tool re-execution, workflow re-execution, and approval automation remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
   — confirm `WorkflowRecoveryAction` type and all 4 values (lines 50–54);
   confirm `lastRestorableCheckpoint` (line 89), `validationGate` (line 91),
   `recoveryAction` (line 92)
4. `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `bridgeAdvisoryType` and values `advisory_allowed`,
   `hold_for_approval`, `blocked` (S4 field list line 80)
5. `governance/contracts/tool-action-taxonomy.ts`
   — confirm `ToolActionApprovalState` type and all 6 values (lines 64–70)
6. `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `WorkflowRecoveryAction` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 50 | `WorkflowRecoveryAction` | `WorkflowRecoveryAction` | ACCEPT |
| `resume_from_checkpoint` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 51 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `hold_for_reviewer_gate` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 52 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `escalate_to_governance` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 53 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `request_human_review` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 54 | `WorkflowRecoveryAction` value | `WorkflowRecoveryAction` | ACCEPT |
| `lastRestorableCheckpoint` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 89 | `WorkflowRecoveryReadout.lastRestorableCheckpoint` | `WorkflowRecoveryReadout` | ACCEPT |
| `validationGate` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 91 | `WorkflowRecoveryReadout.validationGate` | `WorkflowRecoveryReadout` | ACCEPT |
| `recoveryAction` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 92 | `WorkflowRecoveryReadout.recoveryAction` | `WorkflowRecoveryReadout` | ACCEPT |
| `ToolActionApprovalState` type | `governance/contracts/tool-action-taxonomy.ts` | lines 64–70 | `ToolActionApprovalState` | `ToolActionApprovalState` | ACCEPT |
| `not_required` | `governance/contracts/tool-action-taxonomy.ts` | line 65 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `pending_approval` | `governance/contracts/tool-action-taxonomy.ts` | line 66 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `satisfied_but_not_executable` | `governance/contracts/tool-action-taxonomy.ts` | line 67 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `blocked_before_approval` | `governance/contracts/tool-action-taxonomy.ts` | line 68 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `blocked_by_policy` | `governance/contracts/tool-action-taxonomy.ts` | line 69 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `incomplete_approval` | `governance/contracts/tool-action-taxonomy.ts` | line 70 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `bridgeAdvisoryType` token | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list line 80 | LHW6-T1 advisory packet field | LHW6-T1 connector | ACCEPT |
| `advisory_allowed` value | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list line 80 | `bridgeAdvisoryType` enum value | LHW6-T1 connector | ACCEPT |
| `hold_for_approval` value | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list line 80 | `bridgeAdvisoryType` enum value | LHW6-T1 connector | ACCEPT |
| `blocked` value | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list line 80 | `bridgeAdvisoryType` enum value | LHW6-T1 connector | ACCEPT |
| `reEntryAdvisoryType` | N/A — new doc-only field | S3 new fields block | doc-only; no runtime source | connector S3 | ACCEPT |
| `approvalReuseAdvisory` | N/A — new doc-only field | S3 new fields block | doc-only; no runtime source | connector S3 | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T1 spec with 5 sections; WR1/LHW6-T1/TA1 field names verbatim | S1–S5 deliverable | spec at target path | Reviewer confirms source-verbatim field names | CLOSED |
| Tool re-execution blocked explicit | S1, S3, claim boundary | `runtimeExecutionAuthorized=false`; `does not re-execute tool calls` | `rg -n "runtimeExecutionAuthorized=false" <spec>` | CLOSED |
| Source Verification Table complete | S5 | Source Verification Table | Reviewer checks no `BLOCKED_SOURCE_NOT_FOUND` row | CLOSED |
| No code file modified | Evidence Requirements | git diff output | `git diff --name-only` | CLOSED |
| Session continuity updated | Execution Plan | `ACTIVE_SESSION_STATE.json` | `git diff --name-status` | CLOSED |

## Deliverable

File: `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md`

Required sections S1–S5: Purpose/Claim Boundary, Re-Entry Advisory Mapping,
Re-Entry Packet Minimum Fields, Boundary Table, Source Verification Table.

## Pre-Flight

- [x] Working tree clean
- [x] All required first reads done
- [x] WR1 `WorkflowRecoveryAction` values confirmed from source (lines 50–54)
- [x] LHW6-T1 `bridgeAdvisoryType` values confirmed from spec (S4 line 80)
- [x] TA1 `ToolActionApprovalState` values confirmed from source (lines 64–70)

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all WR1/LHW6-T1/TA1 field names from source.
3. Draft spec (S1–S5) with S5 Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity.
7. Commit.
8. Write completion review; include T2 gate answer.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps all `WorkflowRecoveryAction` values to re-entry advisory decisions
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated
- Completion review written with T2 gate answer

## Acceptance Criteria

- [x] Spec with all 5 sections created
- [x] S2 covers all `WorkflowRecoveryAction` values
- [x] `runtimeExecutionAuthorized=false` invariant explicit in S1 and S3
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:

- Missing LHW7 GC-018 baseline, missing Source Verification row, or
  Source Verification `ACCEPT` row citing a non-existent file
- Any claim that this connector re-executes tools, auto-revalidates approvals,
  extends receipt envelopes, or treats restart as automatic approval-preservation

## Review Gate

Before committing: Reviewer perspective completed; all WR1/LHW6-T1/TA1 field
names verbatim; `runtimeExecutionAuthorized=false` explicit; S5 complete with no
`BLOCKED_SOURCE_NOT_FOUND` rows; no code file in diff.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 re-entry mapping uses WR1/LHW6-T1/TA1 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] No code file in diff
- [x] Session continuity updated
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing;
- a WR1 `WorkflowRecoveryAction` value, LHW6-T1 `bridgeAdvisoryType` value, or
  TA1 `approvalState` value cannot be confirmed from source;
- writing the connector requires re-executing a tool call or lifting
  `runtimeExecutionAuthorized=false`;
- spec exceeds 250 lines before S4 is complete.

## T2 Gate Output

Was a concrete cross-session memory handoff gap identified during T1 work?

**YES.** T1 mapping reveals that restart semantics for tool-approvals are
undefined across WR1/LHW6-T1/TA1. The same disconnect exists one layer up:
when the restarted step queries prior session context, neither LHW6-T3 project
memory readout nor CB1 context-budget readout define a seeding handoff. T2
closes that gap.

T2 proceeds per the roadmap gating rule (T1 CLOSED_PASS ✓).

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified WR1/LHW6-T1/TA1 vocabulary; no operator checkpoint required
unless a tool re-execution authorization relaxation or new surface token is
discovered during implementation.

## Claim Boundary

LHW7-T1 produces a documentation artifact. It does not claim WR1/TA1/LHW6-T1
runtime extension, tool re-execution, approval automation, workflow re-execution,
receipt envelope extension, provider behavior, hosted readiness, production
readiness, or public release readiness.
