# CVF Work Order — LHW6-T2 CLI Tool Onboarding Governance Connector

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW6-T2: a connector spec binding W3 `command_runtime` surface
classification → TA1 approval gate → LHW6-T1 bridge advisory type into a CLI
tool onboarding governance packet. Closes the gap where W3 classifies CLI
commands in the `command_runtime` surface and TA1 reports their approval state,
but no connector packages these proven surfaces into a first-use onboarding
record that tells Orchestrator what governance classification a CLI tool carries,
what approval gate applies to its first execution, and what the boundary advisory
says about its bridgeability.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. CLI command execution remains blocked.

## Authority Chain

- LHW6 roadmap: `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW6_T2_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- LH1 ledger (`CLI-Anything` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- W3: `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- TA1: `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- LHW6-T1 spec: `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

## Gate Condition — CHECK FIRST

```text
Gate 1 — T1 status: CLOSED_PASS
```

Read `docs/reviews/CVF_LHW6_T1_*_COMPLETION_2026-05-28.md`.

If T1 is not CLOSED_PASS, stop and report to Orchestrator.

## Agent Roles

Implementer writes spec (S1–S5) using W3, TA1, and LHW6-T1 vocabulary verbatim.
Reviewer checks W3 `command_runtime` surface token verbatim, TA1 approval state
tokens verbatim, LHW6-T1 `bridgeAdvisoryType` values verbatim, CLI-execution-
blocked explicit, boundary table honest, S5 Source Verification complete.
Auditor confirms T1 gate documented, `CLI-Anything` LH1 trigger recorded, no
CLI execution claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
CLI command execution and command runtime bridging remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 completion (understand the bridge advisory chain T2 builds on)
4. `governance/contracts/tool-action-taxonomy.ts`
   — confirm W3 `surface=command_runtime`; confirm relevant sideEffect values
   for command_runtime: `read_only`, `local_write`, `workspace_mutation`,
   `install`, `network_egress`, `destructive`, `privileged`;
   confirm `runtimeExecutionAuthorized=false`; confirm `sandboxRequired` logic
   for `command_runtime` surface
5. `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
   — confirm TA1 approval state tokens
6. `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm S3 `bridgeAdvisoryType` values: `advisory_allowed` |
   `hold_for_approval` | `blocked`; confirm `toolBridgeBlocking=false`
7. `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
   — confirm T2 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| W3 `command_runtime` surface token | `governance/contracts/tool-action-taxonomy.ts` | lines 9-14 | `command_runtime` | `ToolActionSurface` | ACCEPT |
| W3 `command_runtime` sideEffect values | `governance/contracts/tool-action-taxonomy.ts` | lines 16-31 | `read_only`, `local_write`, `workspace_mutation`, `install`, `network_egress`, `destructive`, `privileged` | `ToolActionSideEffect` | ACCEPT |
| W3 `sandboxRequired` for `command_runtime` | `governance/contracts/tool-action-taxonomy.ts` | lines 381-386 | `surface === 'command_runtime'` → sandbox required | `resolveSandboxRequired` | ACCEPT |
| W3 `runtimeExecutionAuthorized=false` | `governance/contracts/tool-action-taxonomy.ts` | lines 106-120, 130-142 | `runtimeExecutionAuthorized` | `ToolActionTaxonomyEvaluation` / `ToolActionApprovalReadout` | ACCEPT |
| TA1 approval state tokens | `governance/contracts/tool-action-taxonomy.ts` | lines 64-70, 130-142 | `not_required`, `pending_approval`, `satisfied_but_not_executable`, `blocked_before_approval`, `blocked_by_policy`, `incomplete_approval` | `ToolActionApprovalState` / `ToolActionApprovalReadout` | ACCEPT |
| LHW6-T1 `bridgeAdvisoryType` values | `docs/reference/CVF_LHW6_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `advisory_allowed`, `hold_for_approval`, `blocked` | LHW6-T1 bridge advisory packet | ACCEPT |

New doc-only fields proposed by this work order: `onboardingPacketId`,
`cliToolId`, `onboardingClassification`, `firstRunApprovalRequired`,
`bridgeAdvisoryRef`, and `onboardingGuidance`. These must be labeled
documentation-only in the connector spec.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc binding W3 `command_runtime`
  surface classification → TA1 approval state → LHW6-T1 bridge advisory type
  into a CLI tool onboarding governance packet.
- State what it is not: not a W3/TA1 runtime extension; not a CLI command
  executor; not an automated onboarding runner.
- Explicit statement: "This connector does not execute CLI commands. The
  onboarding packet is a governance planning record. Sandbox is required for
  all `command_runtime` surface actions per W3 `resolveSandboxRequired`."

### S2 — W3 command_runtime → TA1 approval → LHW6-T1 advisory onboarding mapping

Table columns: `W3 sideEffect` | `TA1 approvalState` | `LHW6-T1 bridgeAdvisoryType` |
`Onboarding classification` | `First-run guidance`

Minimum rows:

- `read_only` + `not_required` + `advisory_allowed` → `safe_first_use` →
  "This CLI command reads state only. No approval needed."
- `local_write` + `pending_approval` + `hold_for_approval` → `review_before_first_use` →
  "This CLI command modifies local state. Obtain approval before first run."
- `workspace_mutation` + `blocked_by_policy` + `blocked` → `blocked_first_use` →
  "This CLI command mutates the workspace. Blocked by current policy."
- `install` + `blocked_by_policy` + `blocked` → `install_blocked` →
  "Install commands are blocked. Contact your administrator."
- `network_egress` + `pending_approval` + `hold_for_approval` → `network_review_required` →
  "This command reaches external networks. Network review required before first run."

Use W3 sideEffect and TA1 approval state tokens verbatim.

### S3 — CLI onboarding governance packet minimum fields

Prose + field list (max 10 lines):

Every CLI tool onboarding governance packet must contain:

- `onboardingPacketId`: unique token
- `cliToolId`: identifier for the CLI tool or command being onboarded
- `surface`: from W3 (always `command_runtime` for this connector)
- `sideEffect`: from W3 `ToolActionSideEffect`
- `approvalState`: from TA1
- `bridgeAdvisoryType`: from LHW6-T1 (`advisory_allowed` | `hold_for_approval` | `blocked`)
- `runtimeExecutionAuthorized`: always `false`
- `onboardingClassification`: one of `safe_first_use` | `review_before_first_use` |
  `blocked_first_use` | `install_blocked` | `network_review_required`
- `onboardingGuidance`: plain-language guidance for operator or non-coder

State explicitly: "These fields are documentation-only minimum requirements.
`runtimeExecutionAuthorized=false` is invariant. The onboarding packet does
not extend `GovernanceEvidenceReceipt` or any existing receipt envelope."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W3 tool action taxonomy classification | Runtime (governance/contracts) | Stable |
| TA1 tool action approval readout | Runtime (governance/contracts) | Stable |
| LHW6-T1 tool bridge advisory packet | Document-only (LHW6-T1) | Future: tool bridge advisory engine |
| CLI onboarding packet composition | Document-only | Future: CLI onboarding governance engine |
| CLI sandbox enforcement | Document-only (W3 contract rule) | Future: sandbox execution gate |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every W3 sideEffect token, TA1 approval state token, and LHW6-T1
bridgeAdvisoryType value cited in S2 and S3.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] W3 `command_runtime` sideEffect tokens confirmed from source
- [ ] TA1 approval state tokens confirmed from source
- [ ] LHW6-T1 `bridgeAdvisoryType` values confirmed from T1 spec

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Confirm T1 gate.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw6_t2_complete`).
7. Commit: `docs(lhw6-t2): add CLI tool onboarding governance connector spec`.
8. Write completion review; include T3 gate answer.

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps minimum 5 CLI onboarding combinations
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw6_t2_complete`
- Completion review written with T3 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers minimum 5 CLI onboarding combinations
- [ ] `runtimeExecutionAuthorized=false` invariant explicit in S1 and S3
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all W3/TA1 field names
verbatim; LHW6-T1 `bridgeAdvisoryType` values verbatim; `runtimeExecutionAuthorized=false`
explicit; S5 complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; no code file
in diff.

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] S2 onboarding mapping uses W3+TA1+LHW6-T1 vocabulary verbatim
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 gate is not CLOSED_PASS;
- any required first read file is missing;
- a W3 sideEffect token or TA1 approval state token cannot be confirmed from
  source files;
- writing the connector requires executing a CLI command, lifting
  `runtimeExecutionAuthorized=false`, or creating a sandbox runtime;
- spec exceeds 200 lines before S4 is complete.

## T3 Gate Output (required in completion review)

Answer explicitly: "Was a concrete project memory readout gap identified
during T2 work?"

- YES → describe gap in one sentence; T3 proceeds.
- NO → "No gap found. T3 proceeds per roadmap rationale."
  (T3 proceeds regardless — this output is informational.)

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1
CLOSED_PASS and source-verified W3/TA1/LHW6-T1 vocabulary; no operator
checkpoint required unless a CLI execution authorization or new surface token
is discovered during implementation.

## Claim Boundary

LHW6-T2 produces a documentation artifact. It does not claim W3/TA1 runtime
extension, CLI command execution, command bridging, sandbox creation, receipt
envelope extension, provider behavior, hosted readiness, production readiness,
or public release readiness.
