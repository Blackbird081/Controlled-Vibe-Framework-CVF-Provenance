# CVF Work Order — LHW9-T1 MCP Tool Approval Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW9-T1: a connector spec binding W3 `ToolActionSurface='mcp_tool'`
+ `ToolActionApprovalReadout.requiredEvidence` + `missingEvidence` ×
TA1 `ToolActionApprovalState` (6 values) × LHW6-T1 `bridgeAdvisoryType`
(3 values: `advisory_allowed`, `hold_for_approval`, `blocked`) into a single
MCP tool approval advisory packet. Closes the gap where no standard maps MCP
tool surface + approval state + bridge advisory → a named
`mcpApprovalAdvisoryType` with `approvalEvidenceRequired`.

Documentation-only tranche. No MCP transport, CLI execution, or provider
behavior is changed.

## Authority Chain

- LHW9 roadmap: `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
- LHW9 GC-018: `docs/baselines/CVF_GC018_LHW9_WORKFLOW_CONNECTOR_WAVE9_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW9_T1_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `pancake-pos-mcp`, `OpenAgentd`)
- W3 completion: `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- TA1 completion: `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- LHW6-T1 spec: `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

## Agent Roles

Implementer writes spec (S1–S5) using W3, TA1, and LHW6-T1 vocabulary verbatim.
Reviewer checks all `ToolActionApprovalState` values verbatim, all
`bridgeAdvisoryType` values verbatim, `runtimeExecutionAuthorized=false` explicit,
boundary table honest, S5 Source Verification complete. Auditor confirms LH1
triggers recorded, no MCP execution or transport claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo,
MCP transport, CLI execution.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `governance/contracts/tool-action-taxonomy.ts`
   — confirm `ToolActionSurface` values at lines 9–14 (including `mcp_tool`);
   confirm `ToolActionApprovalState` values at lines 64–70;
   confirm `ToolActionApprovalReadout.requiredEvidence` at line 139;
   confirm `ToolActionApprovalReadout.missingEvidence` at line 140
4. `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `bridgeAdvisoryType` values `advisory_allowed`, `hold_for_approval`,
   `blocked` at S4 field list
5. `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ToolActionSurface` type | `governance/contracts/tool-action-taxonomy.ts` | lines 9–14 | `ToolActionSurface` | `ToolActionSurface` | ACCEPT |
| `local_tool` | `governance/contracts/tool-action-taxonomy.ts` | line 10 | `ToolActionSurface` value | `ToolActionSurface` | ACCEPT |
| `command_runtime` | `governance/contracts/tool-action-taxonomy.ts` | line 11 | `ToolActionSurface` value | `ToolActionSurface` | ACCEPT |
| `mcp_tool` | `governance/contracts/tool-action-taxonomy.ts` | line 12 | `ToolActionSurface` value | `ToolActionSurface` | ACCEPT |
| `database` | `governance/contracts/tool-action-taxonomy.ts` | line 13 | `ToolActionSurface` value | `ToolActionSurface` | ACCEPT |
| `capability_provider` | `governance/contracts/tool-action-taxonomy.ts` | line 14 | `ToolActionSurface` value | `ToolActionSurface` | ACCEPT |
| `ToolActionApprovalState` type | `governance/contracts/tool-action-taxonomy.ts` | lines 64–70 | `ToolActionApprovalState` | `ToolActionApprovalState` | ACCEPT |
| `not_required` | `governance/contracts/tool-action-taxonomy.ts` | line 65 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `pending_approval` | `governance/contracts/tool-action-taxonomy.ts` | line 66 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `satisfied_but_not_executable` | `governance/contracts/tool-action-taxonomy.ts` | line 67 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `blocked_before_approval` | `governance/contracts/tool-action-taxonomy.ts` | line 68 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `blocked_by_policy` | `governance/contracts/tool-action-taxonomy.ts` | line 69 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `incomplete_approval` | `governance/contracts/tool-action-taxonomy.ts` | line 70 | `ToolActionApprovalState` value | `ToolActionApprovalState` | ACCEPT |
| `ToolActionApprovalReadout.requiredEvidence` | `governance/contracts/tool-action-taxonomy.ts` | line 139 | `requiredEvidence` | `ToolActionApprovalReadout` | ACCEPT |
| `ToolActionApprovalReadout.missingEvidence` | `governance/contracts/tool-action-taxonomy.ts` | line 140 | `missingEvidence` | `ToolActionApprovalReadout` | ACCEPT |
| `ToolActionApprovalReadout.runtimeExecutionAuthorized=false` | `governance/contracts/tool-action-taxonomy.ts` | line 141 | `runtimeExecutionAuthorized` | `ToolActionApprovalReadout` | ACCEPT |
| `bridgeAdvisoryType` token | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list | `bridgeAdvisoryType` | LHW6-T1 advisory packet | ACCEPT |
| `advisory_allowed` | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list | `bridgeAdvisoryType` value | LHW6-T1 advisory packet | ACCEPT |
| `hold_for_approval` | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list | `bridgeAdvisoryType` value | LHW6-T1 advisory packet | ACCEPT |
| `blocked` (bridgeAdvisoryType) | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 field list | `bridgeAdvisoryType` value | LHW6-T1 advisory packet | ACCEPT |
| New doc-only fields `mcpApprovalAdvisoryType`, `approvalEvidenceRequired` | N/A — doc-only | S3 new fields | doc-only | MCP approval advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T1 spec; W3/TA1/LHW6-T1 field names verbatim | S1–S5 | spec at target path | Reviewer confirms source-verbatim field names | CLOSED |
| MCP execution blocked explicit | S1, S3, Claim Boundary | `runtimeExecutionAuthorized=false`; explicit not-execute statement | `rg -n "runtimeExecutionAuthorized=false" <spec>` | CLOSED |
| S2 maps all `ToolActionApprovalState` values for `mcp_tool` surface | S2 | 6 values mapped | Reviewer checks S2 rows | CLOSED |
| Source Verification Table complete | S5 | Source Verification Table | Reviewer checks no `BLOCKED_SOURCE_NOT_FOUND` | CLOSED |
| No code file modified | Evidence Requirements | git diff output | `git diff --name-only` | CLOSED |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

## Pre-Flight

- [x] Working tree clean
- [x] All required first reads done
- [x] W3 `ToolActionSurface` and `ToolActionApprovalState` confirmed from source
- [x] LHW6-T1 `bridgeAdvisoryType` values confirmed from spec

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all W3/TA1/LHW6-T1 field names from source.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity.
7. Commit.
8. Write completion review; include T2 gate answer.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps all 6 `ToolActionApprovalState` values for `mcp_tool` surface
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in diff
- Session continuity updated
- Completion review with T2 gate answer written

## Acceptance Criteria

- [x] Spec with all 5 sections created
- [x] S2 covers all 6 `ToolActionApprovalState` values for `mcp_tool` surface
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] S5 Source Verification Table complete
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:

- Missing LHW9 GC-018 baseline or Source Verification `ACCEPT` row citing
  a non-existent file
- Any claim that this connector executes MCP calls, bridges to MCP transport,
  or lifts `runtimeExecutionAuthorized=false`

## Review Gate

Before committing: all W3/TA1/LHW6-T1 field names verbatim;
`runtimeExecutionAuthorized=false` explicit; S5 complete; no code file in diff.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 advisory mapping uses W3/TA1/LHW6-T1 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [x] S4 boundary table honest; no doc-only row labeled Runtime
- [x] No code file in diff
- [x] Session continuity updated
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop if: any required first read file is missing; a W3, TA1, or LHW6-T1 token
cannot be confirmed; writing the connector requires MCP transport or lifts
`runtimeExecutionAuthorized=false`; spec exceeds 250 lines before S4.

## T2 Gate Output

Was a concrete noncoder friction advisory gap identified during T1?

**YES.** T1 MCP approval mapping reveals that when CB1 reports `missingSignals`
and C8 reports `no_certified_pack_match`, no connector maps these friction
signals to a named `frictionAdvisoryType` with an `antiOverconstraintRecommendation`
for non-coder operators. T2 closes that gap.

T2 proceeds per roadmap gating rule (T1 CLOSED_PASS ✓).

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche; no operator
checkpoint required unless MCP transport or new execution authority is
discovered.

## Claim Boundary

LHW9-T1 produces a documentation artifact. It does not claim W3/TA1/LHW6-T1
runtime extension, MCP execution, MCP transport, tool execution, memory
injection, receipt envelope extension, provider behavior, hosted readiness,
production readiness, or public release readiness.
