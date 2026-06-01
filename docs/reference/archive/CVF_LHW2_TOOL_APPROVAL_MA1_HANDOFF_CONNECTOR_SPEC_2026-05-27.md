# CVF LHW2 Tool Approval MA1 Handoff Connector — Specification

Memory class: FULL_RECORD

docType: reference

Status: ACTIVE

Contract version: `cvf.toolApprovalMA1HandoffConnector.lhw2.t3.v1`

Date: 2026-05-27

Authority: `docs/work_orders/CVF_WO_LHW2_T3_TOOL_APPROVAL_MA1_HANDOFF_CONNECTOR_2026-05-27.md`

---

## Purpose

A normative document mapping each TA1 tool approval state to its MA1 transfer
packet outcome. Closes the gap where TA1 outputs a detailed approval state
but no connector defines how that state routes into a governance handoff packet
for the Orchestrator or Auditor to act on.

Gate 1 — T1: CLOSED_PASS (`cvf.memoryEventCaptureWorkflowReceiptLoopConnector.lhw2.t1.v1`).

Gate 2 — T2: CLOSED_PASS (`cvf.workflowRecoveryActionPacketConnector.lhw2.t2.v1`).

## Scope

Source authority:

- TA1: `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- W3: `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- MA1: `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- LHW1-T2 boundary: `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`
- LHW2 roadmap: `docs/roadmaps/CVF_LHW2_WORKFLOW_CONNECTOR_COMPLETION_ROADMAP_2026-05-27.md`

---

## S1 — Purpose and Claim Boundary

What this connector is: a normative doc mapping TA1 approval states to MA1
transfer packet outcomes.

What this connector is not: not a TA1/W3 runtime extension; not a tool
execution authority; not an approval persistence mechanism.

"`runtimeExecutionAuthorized=false` is preserved from W3 and TA1. This
connector does not grant any form of execution authority. Approval state in a
packet is a governance signal, not an execution trigger."

Source: `governance/contracts/tool-action-taxonomy.ts` —
`ToolActionApprovalReadout.runtimeExecutionAuthorized: false` (line 141,
hardcoded literal). See S3 Source Verification Table.

---

## S2 — TA1 Approval State to MA1 Packet Mapping

TA1 approval state names are verbatim from `ToolActionApprovalState` in
`governance/contracts/tool-action-taxonomy.ts` (lines 64–70).
MA1 section numbers (##0-##10) from
`docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`.

| TA1 state | Packet type | When issued | Required MA1 sections | Minimum packet fields | Next role action |
|---|---|---|---|---|---|
| `not_required` | No packet | Approval level is `none`; advance immediately | N/A all | — | Proceed; `runtimeExecutionAuthorized=false` still holds; a separately authorized executor is required |
| `pending_approval` | `approval_request_packet` | Approval required; evidence not yet submitted | R: ##0, ##1, ##2, ##3, ##4, ##7, ##8, ##9 | `approvalState`, `approvalLevel`, `requiredEvidence`, `missingEvidence`, `receiverRole` | Designated approver submits evidence; records decision in MA1 ##8 and evidence in ##9 |
| `satisfied_but_not_executable` | `readiness_confirmed_packet` | Evidence satisfied but no runtime executor authorized | R: ##0, ##1, ##2, ##8, ##10; N/A: ##5 | `approvalState`, `pendingGate: runtime_executor_not_yet_authorized` | Hold; do not execute; await dedicated execution tranche |
| `blocked_before_approval` | `block_notification_packet` | Required scope/target/trace evidence missing before approval can be evaluated | R: ##0, ##1, ##2, ##3, ##8, ##10 | `approvalState`, `safeMessage`, `correctiveAction: add_missing_evidence` | Stop; add missing evidence; resubmit for approval |
| `blocked_by_policy` | `policy_block_packet` | Action is blocked by local policy contract | R: ##0, ##1, ##2, ##7, ##8, ##10; O: ##3 | `approvalState`, `safeMessage`, `escalationPath: open_governed_work_order` | Stop; Auditor confirms; open fresh governed work order if operator pursues |
| `incomplete_approval` | `missing_evidence_packet` | Approval partially submitted but missing approver id, reason, or evidence id | R: ##0, ##1, ##2, ##3, ##4, ##7 | `approvalState`, `missingEvidence` (list), `resolverRole` | Named resolver attaches approval evidence; resubmits |

---

## S3 — Source Verification Table

| Claimed field | Source file | Verified field path | Owning interface/function | Disposition |
|---|---|---|---|---|
| `not_required` | `governance/contracts/tool-action-taxonomy.ts` | `ToolActionApprovalState = 'not_required'` (line 65) | `ToolActionApprovalState` type | ACCEPT |
| `pending_approval` | `governance/contracts/tool-action-taxonomy.ts` | `ToolActionApprovalState = 'pending_approval'` (line 66) | `ToolActionApprovalState` type | ACCEPT |
| `satisfied_but_not_executable` | `governance/contracts/tool-action-taxonomy.ts` | `ToolActionApprovalState = 'satisfied_but_not_executable'` (line 67) | `ToolActionApprovalState` type | ACCEPT |
| `blocked_before_approval` | `governance/contracts/tool-action-taxonomy.ts` | `ToolActionApprovalState = 'blocked_before_approval'` (line 68) | `ToolActionApprovalState` type | ACCEPT |
| `blocked_by_policy` | `governance/contracts/tool-action-taxonomy.ts` | `ToolActionApprovalState = 'blocked_by_policy'` (line 69) | `ToolActionApprovalState` type | ACCEPT |
| `incomplete_approval` | `governance/contracts/tool-action-taxonomy.ts` | `ToolActionApprovalState = 'incomplete_approval'` (line 70) | `ToolActionApprovalState` type | ACCEPT |
| `runtimeExecutionAuthorized: false` | `governance/contracts/tool-action-taxonomy.ts` | `ToolActionApprovalReadout.runtimeExecutionAuthorized: false` (line 141) | `ToolActionApprovalReadout` interface | ACCEPT |
| MA1 section numbers `##0`-`##10` | `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | Section headers `## 0` through `## 10` | MA1 standard | ACCEPT |

No `BLOCKED_SOURCE_NOT_FOUND` rows.

---

## S4 — Demand-Gated Items

The following are explicitly NOT absorbed by this connector:

- `pancake-pos-mcp` approval transport and business tool runtime: remains
  PARTIALLY_ABSORBED per LH1 ledger; reopen only for MCP approval proof with
  a dedicated runtime GC-018.
- Persisted approval tickets or approval queue: demand-gated; not in scope.
- Live tool/MCP/database execution proof: demand-gated; requires a dedicated
  execution tranche with live provider proof.
- `CLI-Anything` sandboxed execution integration: demand-gated; not in scope.

---

## S5 — Runtime-Enforcement Boundary Table

| Behavior | Current status | Future path |
|---|---|---|
| W3 tool action risk classification | Runtime (`governance/contracts`) | Stable |
| TA1 approval state readout | Runtime (`governance/contracts`) | Stable |
| MA1 transfer packet format | Document standard | Future: MA1 schema validator |
| Approval request packet routing | Document-only | Future: approval request queue |
| Block notification delivery | Document-only | Future: governed notification surface |
| Execution gate enforcement | Document-only | Future: role-gate in `/api/execute` |

---

## Claim Boundary

This connector is a documentation artifact only. It does not claim TA1/W3
runtime extension, tool/MCP/database execution authority, approval ticket
persistence, MCP bridge or transport, route-level enforcement, receipt envelope
extension, provider behavior, hosted readiness, production readiness, or public
release readiness.

Contract version: `cvf.toolApprovalMA1HandoffConnector.lhw2.t3.v1`.

LHW2 roadmap: CLOSED_PASS_BOUNDED (T1 + T2 + T3 delivered).
