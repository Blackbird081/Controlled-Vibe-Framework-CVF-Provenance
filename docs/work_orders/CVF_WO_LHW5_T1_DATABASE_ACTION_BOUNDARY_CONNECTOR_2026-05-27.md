# CVF Work Order — LHW5-T1 Database Action Boundary Connector

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW5-T1: a connector spec binding W3 database surface/sideEffect/
databaseFamily → TA1 approval state → LHW4-T2 dispatchDecision into a single
database-action boundary packet. Closes the gap where W3 classifies database
actions and TA1 reports approval state, but no connector defines the boundary
packet that records what is read-only-allowed versus blocked for Orchestrator
to read before dispatching any database-facing operation.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. `databaseMutationAuthorized=false` is invariant throughout.

## Authority Chain

- LHW5 roadmap: `docs/roadmaps/CVF_LHW5_WORKFLOW_CONNECTOR_WAVE5_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW5_T1_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`gridex` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- W3: `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- TA1: `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- LHW4-T2 spec: `docs/reference/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md`

## Agent Roles

Implementer writes spec (S1–S5) using W3, TA1, and LHW4-T2 vocabulary verbatim.
Reviewer checks W3 field names verbatim, TA1 approval state tokens verbatim,
`databaseMutationAuthorized=false` explicit, boundary table honest, S5 Source
Verification complete. Auditor confirms `gridex` LH1 trigger recorded, no
mutation execution claimed, no database driver or runtime extension. No
self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW5_DATABASE_ACTION_BOUNDARY_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Database mutation, query execution, schema changes, and driver execution remain
blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `governance/contracts/tool-action-taxonomy.ts`
   — confirm W3 `ToolActionSurface`, `ToolActionSideEffect`, `DatabaseActionFamily`,
   `ToolTransport`, `ToolActionTaxonomyRequest`, `ToolActionTaxonomyEvaluation`,
   `ToolActionApprovalReadout`, `runtimeExecutionAuthorized=false`;
   confirm database sideEffect values and their approval levels
4. `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
   — confirm TA1 approval state tokens: `not_required`, `pending_approval`,
   `satisfied_but_not_executable`, `blocked_before_approval`,
   `blocked_by_policy`, `incomplete_approval`
5. `docs/reference/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md`
   — confirm S3 `dispatchDecision` field values: `allowed` | `hold_for_approval` | `blocked`;
   confirm `authorityChainSignal` vocabulary
6. `docs/roadmaps/CVF_LHW5_WORKFLOW_CONNECTOR_WAVE5_ROADMAP_2026-05-27.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| W3 surface tokens | `governance/contracts/tool-action-taxonomy.ts` | lines 9-14 | `local_tool`, `command_runtime`, `mcp_tool`, `database`, `capability_provider` | `ToolActionSurface` | ACCEPT |
| W3 sideEffect database tokens | `governance/contracts/tool-action-taxonomy.ts` | lines 23-28 | `database_read`, `database_write`, `database_export`, `database_schema_mutation`, `database_recovery`, `database_admin` | `ToolActionSideEffect` | ACCEPT |
| W3 `DatabaseActionFamily` values | `governance/contracts/tool-action-taxonomy.ts` | lines 33-40 | `schema_inspection`, `query_drafting`, `read_execution`, `write_execution`, `schema_mutation`, `export_movement`, `backup_recovery`, `administrative` | `DatabaseActionFamily` | ACCEPT |
| W3 `destructive` sideEffect token | `governance/contracts/tool-action-taxonomy.ts` | lines 29-31 | `destructive` | `ToolActionSideEffect` | ACCEPT |
| W3 `databaseFamily` field | `governance/contracts/tool-action-taxonomy.ts` | lines 82-96 | `databaseFamily?: DatabaseActionFamily` | `ToolActionTaxonomyRequest` | ACCEPT |
| W3 `runtimeExecutionAuthorized=false` | `governance/contracts/tool-action-taxonomy.ts` | lines 106-120, 130-142 | `runtimeExecutionAuthorized` | `ToolActionTaxonomyEvaluation` / `ToolActionApprovalReadout` | ACCEPT |
| TA1 approval state tokens | `governance/contracts/tool-action-taxonomy.ts` | lines 64-70, 130-142 | `not_required`, `pending_approval`, `satisfied_but_not_executable`, `blocked_before_approval`, `blocked_by_policy`, `incomplete_approval` | `ToolActionApprovalState` / `ToolActionApprovalReadout` | ACCEPT |
| LHW4-T2 `dispatchDecision` values | `docs/reference/CVF_LHW4_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-27.md` | S3 field list | `allowed`, `hold_for_approval`, `blocked` | LHW4-T2 authority chain packet | ACCEPT |

New doc-only fields proposed by this work order: `dbBoundaryId`,
`dbBoundaryDecision`, `mutationGuard`, and `databaseBoundarySignal`.
These must be labeled documentation-only in the connector spec.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW5_DATABASE_ACTION_BOUNDARY_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc binding W3 database surface/
  sideEffect/databaseFamily → TA1 approval state → LHW4-T2 dispatchDecision
  into a single database-action boundary packet readable by Orchestrator before
  any database-facing operation.
- State what it is not: not a W3/TA1 runtime extension; not a database driver
  or query executor; not a mutation authorization grant.
- Explicit statement: "`databaseMutationAuthorized=false` is invariant. The
  database-action boundary packet is a governance advisory; it does not grant
  query execution, mutation authority, or schema-change permission. All
  `database_write`, `database_schema_mutation`, `database_admin`,
  `database_recovery`, and `destructive` sideEffects map to `blocked`
  `dbBoundaryDecision` unless a future tranche explicitly lifts this."

### S2 — W3 database surface → TA1 approval → LHW4-T2 dispatch field mapping

Table columns: `W3 sideEffect` | `DatabaseActionFamily` | `TA1 approvalState` |
`Dispatch decision` | `Database boundary signal`

Minimum rows:

- `database_read` + `read_execution` + `not_required` → `allowed` →
  read-only boundary satisfied; no approval gate
- `database_read` + `query_drafting` + `pending_approval` → `hold_for_approval` →
  query must be reviewed before execution
- `database_write` + `write_execution` + `blocked_by_policy` → `blocked` →
  mutation blocked by policy; `databaseMutationAuthorized=false`
- `database_schema_mutation` + `schema_mutation` (any TA1 state) → `blocked` →
  schema change blocked; always maps to blocked regardless of approval state
- `database_recovery` + `backup_recovery` (any TA1 state) → `blocked` →
  recovery/admin path remains blocked in the current boundary
- `database_admin` + `administrative` (any TA1 state) → `blocked` →
  administrative path remains blocked in the current boundary
- `database_export` + (any family) + `satisfied_but_not_executable` → `blocked` →
  export approved but not executable; `runtimeExecutionAuthorized=false`

Use W3 and TA1 field and token names verbatim. If any name cannot be confirmed,
mark `BLOCKED_SOURCE_NOT_FOUND` and stop.

### S3 — Database-action boundary packet minimum fields

Prose + field list (max 10 lines):

Every database-action boundary packet must contain:

- `dbBoundaryId`: unique token for this readout
- `surface`: from W3 (always `database` for this connector)
- `sideEffect`: from W3 `ToolActionSideEffect`
- `databaseFamily`: from W3 `DatabaseActionFamily` when present
- `approvalState`: from TA1
- `runtimeExecutionAuthorized`: always `false` from W3/TA1 boundary
- `dbBoundaryDecision`: one of `allowed` | `hold_for_approval` | `blocked`
- `mutationGuard`: always `false` for any mutation sideEffect
- `databaseBoundarySignal`: plain-language summary of the boundary decision

State explicitly: "These fields are documentation-only minimum requirements.
`databaseMutationAuthorized=false` is invariant. The boundary packet does not
extend `GovernanceEvidenceReceipt` or any existing receipt envelope type."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W3 database action taxonomy classification | Runtime (governance/contracts) | Stable |
| TA1 tool action approval readout | Runtime (governance/contracts) | Stable |
| LHW4-T2 authority chain readout packet | Document-only (LHW4-T2) | Future: authority chain validator |
| Database boundary packet composition | Document-only | Future: database boundary validator |
| Database query execution gate | Document-only | Future: route-level database gate |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every W3 surface/sideEffect/databaseFamily token, TA1 approval state
token, and LHW4-T2 dispatch field cited in S2 and S3. This includes
`export_movement`, `backup_recovery`, and `administrative` when those families
are named in the connector.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] W3 database sideEffect tokens confirmed from source files
- [ ] W3 `DatabaseActionFamily` values confirmed from source files
- [ ] TA1 approval state tokens confirmed from source files
- [ ] LHW4-T2 `dispatchDecision` values confirmed from spec

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all database surface/sideEffect/databaseFamily field names.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw5_t1_complete`).
7. Commit: `docs(lhw5-t1): add database action boundary connector spec`.
8. Write completion review; include T2 gate answer.

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps minimum 5 W3+TA1 combinations to boundary decisions
- `databaseMutationAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw5_t1_complete`
- Completion review written with T2 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers minimum 5 database boundary combinations
- [ ] `databaseMutationAuthorized=false` invariant explicit in S1 and S3
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

## T2 Gate Output (required in completion review)

Answer explicitly: "Was a concrete artifact export boundary gap identified
during T1 work?"

- YES → describe gap in one sentence; T2 proceeds.
- NO → "No gap found. T2 proceeds per roadmap rationale."
  (T2 proceeds regardless — this output is informational.)

## Review Gate

Before committing: Reviewer perspective completed; all W3/TA1 field names
verbatim; LHW4-T2 `dispatchDecision` values verbatim; `databaseMutationAuthorized=false`
explicit; S5 complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; no code file
in diff.

## Closure Checklist

- [ ] Spec created with all 5 sections
- [ ] S2 database boundary mapping uses W3+TA1+LHW4-T2 vocabulary verbatim
- [ ] `databaseMutationAuthorized=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing;
- a W3 sideEffect token, DatabaseActionFamily value, or TA1 approval state
  token cannot be confirmed from source files;
- writing the connector requires relaxing `databaseMutationAuthorized=false`
  or authorizing any database write, schema mutation, or admin operation;
- spec exceeds 200 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified W3/TA1/LHW4-T2 vocabulary; no operator checkpoint required
unless a database mutation authorization relaxation or new sideEffect token
is discovered during implementation.

## Claim Boundary

LHW5-T1 produces a documentation artifact. It does not claim W3/TA1 runtime
extension, database query execution, mutation authorization, driver creation,
receipt envelope extension, provider behavior, hosted readiness, production
readiness, or public release readiness.
