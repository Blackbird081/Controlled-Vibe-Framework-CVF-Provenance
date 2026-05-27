# CVF Work Order — LHW3-T3 Spec-Change Workflow Packet Connector

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW3-T3: a connector spec mapping mid-workflow spec-change requests
into MA1-compatible governance change packets. Closes the gap where W1 defines
workflow phases and MA1 defines role transfer, but no connector specifies how
a spec-change request packages its delta and re-enters the handoff chain as a
governed packet that an Orchestrator or Reviewer can act on.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed.

## Authority Chain

- LHW3 roadmap: `docs/roadmaps/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW3_T3_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`OpenSpec` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- LHW1-T2 spec: `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
- MA1 standard: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
  (read full sections ##0 through ##10)
- W1: `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- W1 workflow source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`
- LHW2 T3 boundary source: `docs/reference/CVF_LHW2_TOOL_APPROVAL_MA1_HANDOFF_CONNECTOR_SPEC_2026-05-27.md`
- LHW3-T2 spec: `docs/reference/CVF_LHW3_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_SPEC_2026-05-27.md`

## Gate Conditions — CHECK FIRST

```text
Gate 1 — T1 status: CLOSED_PASS
Gate 2 — T2 status: CLOSED_PASS
```

Read `docs/reviews/CVF_LHW3_T1_*_COMPLETION_2026-05-27.md` and
`docs/reviews/CVF_LHW3_T2_*_COMPLETION_2026-05-27.md`.

If either gate is not CLOSED_PASS, stop and report to Orchestrator.

## Agent Roles

Implementer writes spec (S1–S5) using W1 phase tokens and MA1 section references
verbatim. Reviewer checks W1 phase vocabulary verbatim, MA1 section numbers
correct (##0–##10), boundary table honest, `runtimeExecutionAuthorized=false`
explicit, no `.ts` file touched, S4 Source Verification complete. Auditor
confirms both gates documented, OpenSpec LH1 trigger recorded, change packet
is not an executor. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- LHW3 roadmap (status update to `CLOSED_PASS_BOUNDED` after T3 closes)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
`src/lib/workflows/` (any file), any `.ts`/`.tsx`/`.js`/`.py` file, receipt
envelope schema, public-sync repo. Workflow mutation authority, runtime
spec-change enforcement, and execution gating remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 and T2 completions (understand the pattern both tranches establish)
4. `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
   — Section 2 phase-to-role assignment table; Section 3 MA1-compatible role
   transfer packet fields; Section 4 dissent and review handoff requirements;
   understand which phases allow dissent and which require Auditor challenge
5. `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   — sections ##0 through ##10; confirm MA1 section names and numbers for
   ##0 Surface Fidelity Gate, ##1 Authority Chain, ##2 Transfer Objective,
   ##3 Source Packet, ##4 Role Assignment, ##5 Execution Instructions,
   ##6 Role Output Schema, ##7 Dissent And Review Ledger,
   ##8 Integration Decision, ##9 Completion Evidence, and
   ##10 Claim Boundary
6. `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
   — understand W1 closure evidence and phase vocabulary:
   `intake_pending`, `design_ready`, `build_running`, `review_pending`,
   `freeze_ready`, `completed`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`
   — source-verify phase transition token spelling from existing workflow
   transition records
8. `docs/reference/CVF_LHW2_TOOL_APPROVAL_MA1_HANDOFF_CONNECTOR_SPEC_2026-05-27.md`
   — source-verify the doc-only boundary phrase
   `runtimeExecutionAuthorized=false`
9. `docs/reference/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
   — confirm T3 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

The work-order author has verified these source anchors before dispatch.
Worker must preserve exact MA1 section names, W1 phase tokens, and doc-only
boundary wording. New packet fields remain connector-document fields only.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| W1 phase tokens | `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md` | lines 68-73 | `intake_pending`, `design_ready`, `build_running`, `review_pending`, `freeze_ready`, `completed` | LHW1-T2 phase-to-role table | ACCEPT |
| Existing workflow transition tokens | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json` | lines 17-18, 35-36, 53-54, 71-72, 89-90 | `fromState` / `toState` transition records | product brief workflow JSON | ACCEPT |
| MA1 section references | `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | lines 53, 66, 77, 84, 92, 104, 114, 127, 134, 142, 151 | `##0 Surface Fidelity Gate` through `##10 Claim Boundary` | MA1 packet standard | ACCEPT |
| Tool-approval boundary phrase | `docs/reference/CVF_LHW2_TOOL_APPROVAL_MA1_HANDOFF_CONNECTOR_SPEC_2026-05-27.md` | line 48 | `runtimeExecutionAuthorized=false` | LHW2-T3 tool approval MA1 handoff connector boundary | ACCEPT |
| New change-packet fields | this work order | S3A | `changeId`, `requestingActor`, `currentPhase`, `deltaDescription`, `affectedPhaseRange`, `approverRole`, `reEntryPhaseToken`, `changePacketStatus` | doc-only connector fields, not runtime/source fields | ACCEPT |

If implementation evidence contradicts any source-backed row above, worker must
stop and return `BLOCKED_SOURCE_CONFLICT`. Worker must not cite the S3A
doc-only fields as runtime/source fields in the generated S4 table.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW3_SPEC_CHANGE_WORKFLOW_PACKET_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc mapping spec-change requests
  (arising at any W1 phase boundary) to MA1-compatible governance change packets
  with defined approver role, delta scope, and re-entry phase token.
- State what it is not: not a W1 runtime extension; not a workflow mutation
  authority; not a spec-change enforcement engine.
- Explicit statement: "`runtimeExecutionAuthorized=false` is preserved. A change
  packet is a governance record only. Accepting a change packet does not
  automatically mutate a running workflow state; it creates an authorized
  re-entry point that Orchestrator must act on explicitly."

### S2 — W1 phase to change-trigger table and packet shape

Table columns: `W1 phase` | `Change allowed?` | `Approver role` |
`MA1 sections R/O/N/A` | `Re-entry phase token`

Minimum rows covering all 6 W1 phases:

- `intake_pending` — change allowed (spec not yet committed) → Orchestrator
  approves → ##0 Surface Fidelity Gate, ##2 Transfer Objective, and
  ##3 Source Packet R; re-entry: `intake_pending`
- `design_ready` — change allowed with Reviewer sign-off → Reviewer approves
  → ##0/##2/##3/##8 R, ##9 O; re-entry: `design_ready`
- `build_running` — change requires pause + Reviewer + Auditor → ##0/##2/##3/##8/##9 R;
  re-entry: `design_ready` (must re-validate design before continuing build)
- `review_pending` — change blocked until review completes; if urgent,
  `escalate_to_governance` → ##0/##8/##9 R; re-entry: `design_ready`
- `freeze_ready` — change blocked; must reopen via WR1 `invalid_from_current_state`
  escalation; re-entry: determined by governance
- `completed` — change not applicable; new workflow instance required

Use W1 phase tokens verbatim. If a phase token cannot be verified from the W1
workflow source, LHW1-T2 connector spec, or W1 completion evidence, mark it
`BLOCKED_SOURCE_NOT_FOUND` and stop.

### S3 — Change packet minimum field list

Prose + field list (max 10 lines):

Every spec-change packet must contain:

- `changeId`: unique token for this change request
- `requestingActor`: actor initiating the change
- `currentPhase`: W1 phase token at time of request
- `deltaDescription`: one-sentence summary of what changed in the spec
- `affectedPhaseRange`: which W1 phases must re-run after the change
- `approverRole`: which role must sign MA1 ##8 Integration Decision
- `reEntryPhaseToken`: the W1 phase token where workflow re-enters after approval
- `changePacketStatus`: `pending_approval` | `approved` | `rejected`

State explicitly: "These fields are documentation-only minimum requirements.
They do not extend GovernanceEvidenceReceipt or any existing receipt envelope."

### S3A — New Doc-Only Fields Table

Required because these fields are newly proposed connector-document fields, not
current runtime/source fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `changeId` | stable ID for the change packet | Yes | Yes | present in connector examples/checklist |
| `requestingActor` | actor initiating the change | Yes | Yes | present in connector examples/checklist |
| `currentPhase` | W1 phase token at request time | Yes | Yes | value must source-verify against W1 phase tokens |
| `deltaDescription` | one-sentence change summary | Yes | Yes | present in connector examples/checklist |
| `affectedPhaseRange` | W1 phases requiring re-run | Yes | Yes | values must source-verify against W1 phase tokens |
| `approverRole` | role signing MA1 ##8 Integration Decision | Yes | Yes | role label is doc-only unless sourced elsewhere |
| `reEntryPhaseToken` | W1 phase token for re-entry | Yes | Yes | value must source-verify against W1 phase tokens |
| `changePacketStatus` | change packet disposition | Yes | Yes | doc-only enum: pending_approval / approved / rejected |

### S4 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every W1 phase token, MA1 section reference, and LHW1-T2 vocabulary item
cited in S2 and S3. Cover `runtimeExecutionAuthorized=false` from the existing
LHW2 T3 tool-approval MA1 handoff connector if the spec uses that boundary
language. Do not put S3A new doc-only fields in the Source Verification Table
as if they already exist in runtime/source. Valid dispositions are `ACCEPT`,
`REJECT`, and `BLOCKED_SOURCE_NOT_FOUND`. If any source fact cannot be
source-verified, mark it `BLOCKED_SOURCE_NOT_FOUND`, stop, and return to
Orchestrator. No blocked, guessed, draft-only, or unstaged source fact may
remain.

### S5 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W1 phase state projection | Runtime (workflow-resolver.ts) | Stable |
| MA1 transfer packet structure | Document standard (MA1) | Stable |
| Change packet field validation | Document-only | Future: MA1 packet validator |
| Phase-boundary change gate enforcement | Document-only | Future: route-level phase gate |
| Approver role signal | Document-only | Future: governance review queue |
| Spec-change re-entry execution | Document-only | Future: workflow re-entry executor |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

After T3 is CLOSED_PASS: update LHW3 roadmap Status to `CLOSED_PASS_BOUNDED`.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] T2 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] W1 phase tokens confirmed from workflow source or LHW1-T2 connector spec
- [ ] MA1 section numbers confirmed from MA1 standard

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Confirm T1 + T2 gates.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update LHW3 roadmap → `CLOSED_PASS_BOUNDED`.
7. Update session continuity (`lhw3_t3_complete`).
8. Commit: `docs(lhw3-t3): add spec-change workflow packet connector spec`.
9. Write completion review.

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- Both gates (T1 + T2) documented as CLOSED_PASS
- All 6 W1 phases mapped in S2 change-trigger table
- `runtimeExecutionAuthorized=false` explicit in S1
- S4 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- S5 boundary table present; no doc-only row labeled Runtime
- LHW3 roadmap updated to `CLOSED_PASS_BOUNDED`
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw3_t3_complete`
- Completion review written

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] All 6 W1 phases mapped with change-trigger disposition
- [ ] `runtimeExecutionAuthorized=false` and change-packet-is-not-executor explicit
- [ ] S4 Source Verification Table complete with no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S5 boundary table honest (no doc-only row labeled Runtime)
- [ ] LHW3 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all W1 phase tokens verbatim;
MA1 section numbers correct (##0–##10); `runtimeExecutionAuthorized=false`
explicit; S4 Source Verification complete with no `BLOCKED_SOURCE_NOT_FOUND`
rows; S5 boundary table honest; no code file in diff.

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] T2 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] All 6 W1 phases covered in S2
- [ ] `runtimeExecutionAuthorized=false` explicit in S1
- [ ] S4 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S5 boundary table honest; no doc-only row labeled Runtime
- [ ] LHW3 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 or T2 gate is not CLOSED_PASS;
- any required first read file is missing or unreadable;
- a W1 phase token cannot be verified from workflow source or LHW1-T2 connector
  spec;
- a MA1 section number cannot be verified from the MA1 standard;
- writing the connector requires modifying `workflow-resolver.ts`;
- spec exceeds 200 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1 +
T2 CLOSED_PASS and source-verified W1/MA1 vocabulary; no operator checkpoint
required unless a conflict with W1 phase tokens or MA1 section numbers is
discovered during implementation.

## Claim Boundary

LHW3-T3 produces a documentation artifact. It does not claim W1/MA1 runtime
extension, workflow mutation authority, spec-change enforcement, execution
authority, receipt envelope extension, provider behavior, hosted readiness,
production readiness, or public release readiness.
