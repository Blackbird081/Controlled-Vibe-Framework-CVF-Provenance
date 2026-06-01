# CVF Work Order — LHW6-T1 Tool Runtime Bridge Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW6-T1: a connector spec binding W3 `local_tool`/`command_runtime`
surface → sideEffect → optional transport → TA1 approval state → LHW4-T2
dispatchDecision into a single tool-runtime bridge advisory packet. Closes the
gap where W3 classifies local and command-runtime tool actions and TA1 reports
approval state, but no connector defines the advisory packet that records what
is bridgeable (read-only, advisory) vs. blocked for Orchestrator before
dispatching a tool call to any non-MCP runtime surface.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. Tool execution remains blocked.

## Authority Chain

- LHW6 roadmap: `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
- LHW6 GC-018: `docs/baselines/CVF_GC018_LHW6_WORKFLOW_CONNECTOR_WAVE6_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW6_T1_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- LH1 ledger (`OpenAgentd` trigger): `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- W3: `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- TA1: `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- LHW4-T2 spec: `docs/reference/archive/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md`

## Agent Roles

Implementer writes spec (S1–S5) using W3, TA1, and LHW4-T2 vocabulary verbatim.
Reviewer checks W3 surface/sideEffect/transport tokens verbatim, TA1 approval
state tokens verbatim, `runtimeExecutionAuthorized=false` explicit, boundary
table honest, S5 Source Verification complete. Auditor confirms `OpenAgentd`
LH1 trigger recorded, no tool execution or MCP bridge claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Tool execution, command runtime bridging, and MCP client creation remain
blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `governance/contracts/tool-action-taxonomy.ts`
   — confirm W3 `ToolActionSurface` values: `local_tool`, `command_runtime`;
   confirm `ToolActionSideEffect` values from source before selecting the
   local/command-relevant subset used by the spec; confirm `ToolTransport` values; confirm
   `runtimeExecutionAuthorized=false`; confirm `ToolActionApprovalReadout`
4. `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
   — confirm TA1 approval state tokens: `not_required`, `pending_approval`,
   `satisfied_but_not_executable`, `blocked_before_approval`,
   `blocked_by_policy`, `incomplete_approval`
5. `docs/reference/archive/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S3 `dispatchDecision` values: `allowed` | `hold_for_approval` | `blocked`;
   confirm `authorityChainSignal` vocabulary
6. `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| W3 `local_tool` / `command_runtime` surface tokens | `governance/contracts/tool-action-taxonomy.ts` | lines 9-14 | `local_tool`, `command_runtime` | `ToolActionSurface` | ACCEPT |
| W3 `ToolActionSideEffect` values: `read_only`, `local_write`, `workspace_mutation`, `external_mutation`, `install`, `network_egress`, `database_read`, `database_write`, `database_export`, `database_schema_mutation`, `database_recovery`, `database_admin`, `destructive`, `privileged`, `unknown` | `governance/contracts/tool-action-taxonomy.ts` | lines 16-31 | `ToolActionSideEffect` | `ToolActionSideEffect` | ACCEPT |
| W3 `ToolTransport` values: `local`, `stdio_mcp`, `remote_mcp`, `http`, `browser`, `database_connection` | `governance/contracts/tool-action-taxonomy.ts` | line 43 | `ToolTransport` | `ToolTransport` | ACCEPT |
| W3 `runtimeExecutionAuthorized=false` | `governance/contracts/tool-action-taxonomy.ts` | lines 106-120, 130-142 | `runtimeExecutionAuthorized` | `ToolActionTaxonomyEvaluation` / `ToolActionApprovalReadout` | ACCEPT |
| TA1 approval state values: `not_required`, `pending_approval`, `satisfied_but_not_executable`, `blocked_before_approval`, `blocked_by_policy`, `incomplete_approval` | `governance/contracts/tool-action-taxonomy.ts` | lines 64-70, 130-142 | `ToolActionApprovalState` | `ToolActionApprovalState` / `ToolActionApprovalReadout` | ACCEPT |
| LHW4-T2 `dispatchDecision` values | `docs/reference/archive/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md` | S3 field list | `allowed`, `hold_for_approval`, `blocked` | LHW4-T2 authority chain packet | ACCEPT |

New doc-only fields proposed by this work order: `bridgeAdvisoryId`,
`bridgeSurface`, `bridgeAdvisoryType`, `toolBridgeSignal`, and
`toolBridgeBlocking`. These must be labeled documentation-only in the
connector spec.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T1 spec created; W3/TA1/LHW4-T2 field names used verbatim | S1-S5 deliverable sections | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | Reviewer confirms source-verbatim field names | BLOCKED until spec exists |
| Tool execution blocked explicit | S1, S3, S4, Claim Boundary | `runtimeExecutionAuthorized=false`; tool execution non-claim | `rg -n "runtimeExecutionAuthorized=false|does not execute tool" <spec>` | BLOCKED until spec exists |
| Source Verification Table complete | S5 | Source Verification Table | `rg -n "Source Verification Table|Disposition" <spec>` plus reviewer check | BLOCKED until spec exists |
| No code file modified | Evidence Requirements | Git diff output | `git diff --name-only` | BLOCKED until closure evidence exists |
| Session continuity updated | Execution Plan | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, active handoff as applicable | `git diff --name-status` | BLOCKED until closure evidence exists |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc binding W3 `local_tool` or
  `command_runtime` surface → sideEffect → optional transport → TA1 approval
  state → LHW4-T2 dispatchDecision into a single tool-bridge advisory packet.
- State what it is not: not a W3/TA1 runtime extension; not a tool executor
  or command bridge; not an MCP client.
- Explicit statement: "`runtimeExecutionAuthorized=false` is preserved from W3
  and TA1 boundaries. This connector does not execute tool calls. The advisory
  packet is a non-blocking governance record."

### S2 — W3 surface + sideEffect → TA1 approval → dispatch field mapping

Table columns: `W3 surface` | `W3 sideEffect` | `TA1 approvalState` |
`Dispatch decision` | `Tool bridge signal`

Minimum rows:

- `local_tool` + `read_only` + `not_required` → `allowed` →
  read-only tool bridge satisfied; no approval gate
- `local_tool` + `local_write` + `pending_approval` → `hold_for_approval` →
  local write must be reviewed before tool dispatch
- `command_runtime` + `workspace_mutation` + `blocked_by_policy` → `blocked` →
  command runtime mutation blocked by policy
- `command_runtime` + `install` + `pending_approval` → `hold_for_approval` →
  install is R3 explicit approval; advisory holds before any dispatch;
  `runtimeExecutionAuthorized=false`
- `command_runtime` + `destructive` + `blocked_by_policy` → `blocked` →
  destructive commands are blocked by W3 policy; `runtimeExecutionAuthorized=false`
- `local_tool` + `network_egress` + `satisfied_but_not_executable` → `blocked` →
  network egress approved but not executable in current boundary

Use W3 and TA1 field and token names verbatim.

### S3 — Tool bridge advisory packet minimum fields

Prose + field list (max 10 lines):

Every tool-bridge advisory packet must contain:

- `bridgeAdvisoryId`: unique token
- `bridgeSurface`: from W3 `ToolActionSurface` (`local_tool` or `command_runtime`)
- `sideEffect`: from W3 `ToolActionSideEffect`
- `transport`: from W3 `ToolTransport` when present
- `approvalState`: from TA1
- `runtimeExecutionAuthorized`: always `false` from W3/TA1 boundary
- `bridgeAdvisoryType`: one of `advisory_allowed` | `hold_for_approval` | `blocked`
- `toolBridgeSignal`: plain-language summary of the bridge advisory
- `toolBridgeBlocking`: always `false`

State explicitly: "These fields are documentation-only minimum requirements.
`runtimeExecutionAuthorized=false` is invariant. The advisory packet does not
extend `GovernanceEvidenceReceipt` or any existing receipt envelope type."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W3 tool action taxonomy classification | Runtime (governance/contracts) | Stable |
| TA1 tool action approval readout | Runtime (governance/contracts) | Stable |
| LHW4-T2 authority chain readout packet | Document-only (LHW4-T2) | Future: authority chain validator |
| Tool bridge advisory packet composition | Document-only | Future: tool bridge advisory engine |
| Local tool execution gate | Document-only | Future: route-level tool execution gate |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every W3 surface/sideEffect/transport token, TA1 approval state token,
and LHW4-T2 dispatch field cited in S2 and S3.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] W3 `local_tool`/`command_runtime` surface tokens confirmed from source
- [ ] W3 sideEffect tokens confirmed from source files
- [ ] TA1 approval state tokens confirmed from source files
- [ ] LHW4-T2 `dispatchDecision` values confirmed from spec

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all surface/sideEffect/transport field names.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw6_t1_complete`).
7. Commit: `docs(lhw6-t1): add tool runtime bridge advisory connector spec`.
8. Write completion review; include T2 gate answer.

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps minimum 5 W3+TA1 combinations to bridge advisory decisions
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw6_t1_complete`
- Completion review written with T2 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers minimum 5 tool bridge combinations
- [ ] `runtimeExecutionAuthorized=false` invariant explicit in S1 and S3
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

Fail conditions:

- [ ] Missing LHW6 GC-018 baseline, missing Source Verification row, or
  Source Verification `ACCEPT` row citing a non-existent file
- [ ] Any claim that this connector executes tools, authorizes runtime
  execution, extends receipt envelopes, or treats `install` as policy-blocked
  without source-backed approval/escalation mapping

## Review Gate

Before committing: Reviewer perspective completed; all W3/TA1 field names
verbatim; LHW4-T2 `dispatchDecision` values verbatim; `runtimeExecutionAuthorized=false`
explicit; S5 complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; no code file
in diff.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 tool bridge mapping uses W3+TA1+LHW4-T2 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] No code file in diff
- [x] Session continuity updated
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing;
- a W3 surface token, sideEffect token, or TA1 approval state token cannot be
  confirmed from source files;
- writing the connector requires executing a tool call, bridging a command, or
  lifting `runtimeExecutionAuthorized=false`;
- spec exceeds 200 lines before S4 is complete.

## T2 Gate Output (required in completion review)

Answer explicitly: "Was a concrete CLI tool onboarding gap identified during
T1 work?"

- YES → describe gap in one sentence; T2 proceeds.
- NO → "No gap found. T2 proceeds per roadmap rationale."
  (T2 proceeds regardless — this output is informational.)

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified W3/TA1/LHW4-T2 vocabulary; no operator checkpoint required
unless a tool execution authorization relaxation or new surface token is
discovered during implementation.

## Claim Boundary

LHW6-T1 produces a documentation artifact. It does not claim W3/TA1 runtime
extension, tool execution, command bridging, MCP client creation, receipt
envelope extension, provider behavior, hosted readiness, production readiness,
or public release readiness.
