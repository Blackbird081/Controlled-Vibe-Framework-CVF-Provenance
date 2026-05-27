# CVF Work Order — LHW4-T2 Execution Authority Chain Readout Connector

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW4-T2: a connector spec binding G1 execution identity fields →
W3 tool action category → TA1 approval state → MA1 role assignment into a
single authority-chain readout packet. Closes the gap where G1, W3, and TA1
are each proven closed surfaces but no connector ties them into a readable
packet that an Orchestrator can evaluate before dispatching work to a role agent.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. `runtimeExecutionAuthorized=false` is preserved throughout.

## Authority Chain

- LHW4 roadmap: `docs/roadmaps/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW4_T2_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`Claude Kit` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- G1: `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- W3: `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- TA1: `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- MA1 standard: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
  (read sections ##0 through ##10)
- LHW4-T1 spec: `docs/reference/CVF_LHW4_MEMORY_SNAPSHOT_GOVERNANCE_CONNECTOR_SPEC_2026-05-27.md`

## Gate Condition — CHECK FIRST

Confirm T1 is `CLOSED_PASS` by reading:
`docs/reviews/CVF_LHW4_T1_*_COMPLETION_2026-05-27.md`

If T1 is not CLOSED_PASS, stop and report to Orchestrator.

## Agent Roles

Implementer writes spec (S1–S5) using G1, W3, TA1, and MA1 vocabulary verbatim.
Reviewer checks G1 field names verbatim, W3 category tokens verbatim, TA1 state
names verbatim, MA1 section numbers correct (##0–##10), boundary table honest,
`runtimeExecutionAuthorized=false` explicit, no `.ts` file touched, S5 Source
Verification complete. Auditor confirms T1 gate documented, `Claude Kit` LH1
trigger recorded, no new role taxonomy created. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
New role taxonomy, RBAC changes, and execution authority remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 completion (understand memory snapshot foundation T2 builds beside)
4. `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
   — confirm G1 fields: `actorId`, `sessionRole`, `cvfRole`,
   `contextScope`, `executionBoundary`, `receiptOwnership`; confirm
   existing CVFRole values (e.g. `ORCHESTRATOR`, `REVIEWER`, `IMPLEMENTER`,
   `AUDITOR`)
5. `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
   — confirm W3 `actionCategory` tokens: `tool`, `command`, `mcp`,
   `capability`, `database`; confirm `runtimeExecutionAuthorized=false`
6. `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
   — confirm TA1 approval state tokens: `not_required`, `pending_approval`,
   `satisfied_but_not_executable`, `blocked_before_approval`,
   `blocked_by_policy`, `incomplete_approval`
7. `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   — sections ##0–##10; confirm ##4 Role Assignment and ##8 Integration
   Decision section names verbatim
8. `docs/reference/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
   — confirm T2 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc binding G1 execution identity
  → W3 tool category → TA1 approval state → MA1 role assignment into a single
  authority-chain readout packet readable by Orchestrator before dispatch.
- State what it is not: not a G1/W3/TA1 runtime extension; not a new role
  taxonomy; not an execution authority grant.
- Explicit statement: "`runtimeExecutionAuthorized=false` is preserved from
  W3 and TA1 boundaries. The authority-chain readout packet is a governance
  advisory; it does not grant execution authority or change actor permissions."

### S2 — G1 → W3 → TA1 → MA1 authority chain field mapping

Table columns: `G1 field` | `W3 field / token` | `TA1 state` | `MA1 section` |
`Authority chain signal`

Minimum rows:

- `cvfRole=ORCHESTRATOR` + any `actionCategory` + `not_required` TA1 →
  ##4 Role Assignment R → dispatch allowed; no approval gate
- `cvfRole=IMPLEMENTER` + `actionCategory=tool` or `command` + `pending_approval` →
  ##4 R, ##8 Integration Decision R → hold for approval before dispatch
- `cvfRole=IMPLEMENTER` + `actionCategory=mcp` or `database` + `blocked_by_policy` →
  ##4 R, ##8 R → dispatch blocked; stop and record in ##8
- `executionBoundary=denied` (any role, any action) + any TA1 state →
  ##4 R, ##8 R → dispatch blocked; G1 denial overrides TA1 approval
- `cvfRole=REVIEWER` + `actionCategory=capability` + `satisfied_but_not_executable` →
  ##4 R, ##8 O → advisory: capability approved but not yet executable

Use G1, W3, and TA1 field and token names verbatim. If any name cannot be
confirmed from completion reviews, mark `BLOCKED_SOURCE_NOT_FOUND` and stop.

### S3 — Authority chain packet minimum fields

Prose + field list (max 10 lines):

Every authority-chain readout packet must contain:

- `chainId`: unique token for this readout
- `actorId`: from G1
- `cvfRole`: from G1
- `executionBoundary`: from G1
- `actionCategory`: from W3
- `approvalState`: from TA1
- `dispatchDecision`: one of `allowed` | `hold_for_approval` | `blocked`
- `authorityChainSignal`: plain-language summary of the chain signal
- `ma1RoleAssignmentSection`: MA1 ##4 reference token

State explicitly: "These fields are documentation-only minimum requirements.
They do not extend `GovernanceEvidenceReceipt` or any existing receipt
envelope type."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| G1 execution identity resolution | Runtime (cvf-web route) | Stable |
| W3 tool action taxonomy classification | Runtime (governance/contracts) | Stable |
| TA1 approval state readout | Runtime (governance/contracts) | Stable |
| MA1 role assignment packet structure | Document standard (MA1) | Stable |
| Authority chain packet composition | Document-only | Future: authority chain validator |
| Dispatch gate enforcement | Document-only | Future: route-level authority gate |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified path or symbol` |
`Owning interface/function/schema` | `Disposition`

Cover every G1 field, W3 category token, TA1 state token, and MA1 section
reference cited in S2 and S3. Valid dispositions are `ACCEPT`, `REJECT`, and
`BLOCKED_SOURCE_NOT_FOUND`. No blocked, guessed, or confirm-later item may
remain in S2.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] G1 field names confirmed from G1 completion review
- [ ] W3 actionCategory tokens confirmed from W3 completion review
- [ ] TA1 approval state tokens confirmed from TA1 completion review
- [ ] MA1 section names confirmed from MA1 standard

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Confirm T1 gate.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw4_t2_complete`).
7. Commit: `docs(lhw4-t2): add execution authority chain readout connector spec`.
8. Write completion review; include T3 gate answer (see below).

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps at minimum 5 G1+W3+TA1 combinations to authority chain signals
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw4_t2_complete`
- Completion review written with T3 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers minimum 5 chain combinations
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S4 boundary table honest (no doc-only row labeled Runtime)
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all G1/W3/TA1 field names
verbatim; MA1 section numbers correct; `runtimeExecutionAuthorized=false`
explicit; S5 complete; no code file in diff.

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] S2 chain mapping uses G1+W3+TA1+MA1 vocabulary verbatim
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 gate is not CLOSED_PASS;
- any required first read file is missing;
- a G1, W3, TA1 field name, or MA1 section number cannot be confirmed from
  completion reviews or the MA1 standard;
- writing the connector requires adding a new CVFRole value not in the existing
  G1 vocabulary;
- spec exceeds 200 lines before S4 is complete.

## T3 Gate Output (required in completion review)

Answer explicitly: "Was a concrete noncoder friction advisory gap identified
during T2 work?"

- YES → describe gap in one sentence; T3 proceeds.
- NO → "No gap found. T3 proceeds per roadmap rationale."
  (T3 proceeds regardless — this output is informational.)

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1
CLOSED_PASS and source-verified G1/W3/TA1/MA1 vocabulary; no operator checkpoint
required unless a conflict with CVFRole values or TA1 approval state tokens is
discovered during implementation.

## Claim Boundary

LHW4-T2 produces a documentation artifact. It does not claim G1/W3/TA1 runtime
extension, new execution authority, new role taxonomy, RBAC change, receipt
envelope extension, provider behavior, hosted readiness, production readiness,
or public release readiness.
