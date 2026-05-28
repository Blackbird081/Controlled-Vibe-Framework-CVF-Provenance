# CVF Work Order — LHW10-T3 Provider Health Degradation Advisory Connector

Memory class: FULL_RECORD

Status: HOLD_UNTIL_T1_AND_T2_CLOSED_PASS

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW10-T3: a connector spec binding W5
`ProviderMethodFallbackEvaluation.status` (8 values) × W4
`OperationalBenchmarkScorecard.clarityStatus` (3 values) × LHW9-T1
`mcpApprovalAdvisoryType` (6 values) into a provider health degradation advisory
packet. Closes the gap where no connector maps provider fallback posture ×
benchmark clarity → a named `providerHealthAdvisoryType` + `fallbackRecoveryStep`.

LH1 triggers: `free Claude Code` (PARTIALLY_ABSORBED — provider method/public
claim); `freellmapi` (PARTIALLY_ABSORBED — credential/quota/health UX);
`CVF_EDIT_ANALYSIS.md` (PARTIALLY_ABSORBED — next runtime workflow hardening).
Documentation-only tranche. No provider routing change, retry execution, or MCP
transport.

## Authority Chain

- LHW10 roadmap: `docs/roadmaps/CVF_LHW10_WORKFLOW_CONNECTOR_WAVE10_ROADMAP_2026-05-28.md`
- LHW10 GC-018: `docs/baselines/CVF_GC018_LHW10_WORKFLOW_CONNECTOR_WAVE10_2026-05-28.md`
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `free Claude Code`, `freellmapi`, `CVF_EDIT_ANALYSIS.md`)
- W5 completion: `docs/reviews/CVF_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION_COMPLETION_2026-05-24.md`
- W4 completion: `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
- LHW9-T1 spec: `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- **T1 gate: `docs/reviews/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
  must be CLOSED_PASS_BOUNDED**
- **T2 gate: `docs/reviews/CVF_LHW10_T2_RUNTIME_MATURITY_EVIDENCE_CHAIN_CONNECTOR_COMPLETION_2026-05-28.md`
  must be CLOSED_PASS_BOUNDED**

## Agent Roles

Implementer writes spec (S1–S5) using W5, W4, and LHW9-T1 vocabulary verbatim.
Reviewer checks all 8 `ProviderMethodFallbackStatus` values individually
row-verified, all 3 `clarityStatus` values individually row-verified, all 6
`mcpApprovalAdvisoryType` values individually row-verified, `runtimeExecutionAuthorized=false`
explicit, boundary table honest. Auditor confirms LH1 triggers recorded, no
provider routing or retry execution claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- `docs/reviews/CVF_LHW10_T3_FAST_LANE_AUDIT_2026-05-28.md` (new)
- `docs/reviews/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
  (new)
- this work order (status update only)
- session continuity files (including LHW10 roadmap Status update to
  `CLOSED_PASS_BOUNDED`)

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo,
provider routing change, retry execution, MCP transport.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts`
   — confirm `ProviderMethodFallbackStatus` values at lines 46–54;
   confirm `ProviderMethodFallbackEvaluation.status` at line 87
4. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
   — confirm `OperationalBenchmarkClarityStatus` values at line 46;
   confirm `OperationalBenchmarkScorecard.clarityStatus` at line 75
5. `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `mcpApprovalAdvisoryType` values at S2 mapping rows
6. `docs/reviews/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
   — confirm T1 CLOSED_PASS_BOUNDED (gate check)
7. `docs/reviews/CVF_LHW10_T2_RUNTIME_MATURITY_EVIDENCE_CHAIN_CONNECTOR_COMPLETION_2026-05-28.md`
   — confirm T2 CLOSED_PASS_BOUNDED (gate check)

If T1 or T2 completion review does not exist or is not CLOSED_PASS_BOUNDED,
stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ProviderMethodFallbackStatus` type | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 46 | `export type ProviderMethodFallbackStatus` | `ProviderMethodFallbackStatus` | ACCEPT |
| `ready` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 47 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `missing_provider_model` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 48 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `unsupported_method` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 49 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `fallback_available` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 50 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `fallback_unavailable` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 51 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `blocked_non_retryable` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 52 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `blocked_quota` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 53 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `provider_unhealthy` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 54 | union type value | `ProviderMethodFallbackStatus` | ACCEPT |
| `ProviderMethodFallbackEvaluation.status` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` | line 87 | `readonly status: ProviderMethodFallbackStatus` | `ProviderMethodFallbackEvaluation` | ACCEPT |
| `OperationalBenchmarkClarityStatus` type | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` | line 46 | `export type OperationalBenchmarkClarityStatus` | `OperationalBenchmarkClarityStatus` | ACCEPT |
| `clear` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` | line 46 | union type value | `OperationalBenchmarkClarityStatus` | ACCEPT |
| `needs_context` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` | line 46 | union type value | `OperationalBenchmarkClarityStatus` | ACCEPT |
| `insufficient_evidence` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` | line 46 | union type value | `OperationalBenchmarkClarityStatus` | ACCEPT |
| `OperationalBenchmarkScorecard.clarityStatus` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` | line 75 | `clarityStatus` field | `OperationalBenchmarkScorecard` | ACCEPT |
| `mcp_advisory_clear` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 row 1 | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `mcp_advisory_hold_pending` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 row 2 | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `mcp_advisory_satisfied_but_not_executable` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `mcp_advisory_blocked_before_approval` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `mcp_advisory_blocked_by_policy` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `mcp_advisory_incomplete_approval` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `providerHealthAdvisoryType` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Provider health degradation advisory packet | ACCEPT |
| `fallbackRecoveryStep` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Provider health degradation advisory packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T3 spec; W5/W4/LHW9-T1 field names verbatim | S1–S5 | spec at target path | Reviewer confirms source-verbatim field names | OPEN |
| `runtimeExecutionAuthorized=false` explicit | S1, S3, Claim Boundary | invariant stated | `rg -n "runtimeExecutionAuthorized=false" <spec>` | OPEN |
| S2 covers all 8 `ProviderMethodFallbackStatus` values | S2 | 8 fallback status rows | Reviewer checks S2 rows | OPEN |
| S5 individual rows for all 3 `clarityStatus` and all 6 `mcpApprovalAdvisoryType` values | S5 | 9 individual rows | Reviewer checks no aggregate rows | OPEN |
| T1 + T2 CLOSED_PASS_BOUNDED gate | Authority Chain | both completion reviews exist | Read both completion reviews | OPEN |
| No code file modified | Evidence Requirements | git diff output | `git diff --name-only` | OPEN |
| LHW10 wave closure summary in completion review | Closure Checklist | wave closure table in completion review | Reviewer checks T1+T2+T3 summary present | OPEN |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`

Spec must include 5 sections: S1 Purpose and Claim Boundary; S2 Fallback Status
× Benchmark Clarity → Provider Health Advisory Mapping (table covering all 8
W5 `ProviderMethodFallbackStatus` values × 3 W4 `clarityStatus` values × MCP
context advisory); S3 Minimum Fields; S4 Boundary Table; S5 Source Verification
Table (individual rows per enum value).

Key invariants:

- "This connector does not change provider routing, execute retries, or modify
  the MCP approval state."
- `runtimeExecutionAuthorized=false` explicit in S1 and S3.
- "A `provider_health_blocked_quota` or `provider_health_unavailable` advisory
  suspends all pending MCP tool approvals until provider health is restored."

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] T1 CLOSED_PASS_BOUNDED confirmed
- [ ] T2 CLOSED_PASS_BOUNDED confirmed
- [ ] All 8 W5 `ProviderMethodFallbackStatus` values confirmed from source
- [ ] All 3 W4 `clarityStatus` values confirmed from source
- [ ] All 6 LHW9-T1 `mcpApprovalAdvisoryType` values confirmed from spec

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads; confirm T1 and T2 gates.
2. Confirm all W5/W4/LHW9-T1 field names and enum values from source.
3. Draft spec (S1–S5) with Source Verification Table (individual rows per enum
   value — no aggregate rows).
4. Run Fast Lane audit.
5. Confirm no code file staged.
6. Run governance gates:
   `check_work_order_dispatch_quality.py --base 118b8d48 --head HEAD --enforce`
   `check_markdown_structural_completeness.py --base 118b8d48 --head HEAD --enforce`
7. Reviewer perspective — record result.
8. Update session continuity; mark `lhw10WorkflowConnectorWave10` CLOSED_PASS_BOUNDED.
9. Update LHW10 roadmap: set Status to CLOSED_PASS_BOUNDED; replace
   `<lhw10-commit>` in Verification section with actual commit SHA; check all
   Acceptance Criteria boxes.
10. Commit.
11. Write completion review with LHW10 wave closure summary.

Spec size guard: < 250 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 covers all 8 W5 `ProviderMethodFallbackStatus` values
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; individual rows per enum value; no
  `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in diff
- T1 and T2 gates confirmed before dispatch
- Session continuity updated with LHW10 CLOSED_PASS_BOUNDED
- Completion review with LHW10 wave closure summary

## Acceptance Criteria

- [ ] T1 AND T2 CLOSED_PASS_BOUNDED confirmed before dispatch
- [ ] Spec with all 5 sections created
- [ ] S2 covers all 8 `ProviderMethodFallbackStatus` values in mapping
- [ ] All 3 `clarityStatus` values individually row-verified in S5
- [ ] All 6 `mcpApprovalAdvisoryType` values individually row-verified in S5
- [ ] All 8 `ProviderMethodFallbackStatus` values individually row-verified in S5
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no aggregate rows
- [ ] No code file in diff
- [ ] Session continuity updated to LHW10 CLOSED_PASS_BOUNDED
- [ ] LHW10 roadmap updated with actual commit SHA and Status CLOSED_PASS_BOUNDED
- [ ] Completion review includes LHW10 wave closure summary table

Fail conditions:

- T1 or T2 gate not confirmed
- Missing LHW10 GC-018 baseline or Source Verification `ACCEPT` row citing
  a non-existent file
- Any claim that this connector changes provider routing, executes retries, or
  lifts `runtimeExecutionAuthorized=false`
- Aggregate rows in S5 for any multi-value type

## Review Gate

Before committing: T1 and T2 gates confirmed; all W5/W4/LHW9-T1 field names
verbatim; all 17 individual enum value rows in S5; `runtimeExecutionAuthorized=false`
explicit; S5 complete; no code file in diff.

## Closure Checklist

- [ ] T1 AND T2 CLOSED_PASS_BOUNDED confirmed
- [ ] Spec created with all 5 sections
- [ ] S2 mapping uses W5/W4/LHW9-T1 vocabulary verbatim
- [ ] `runtimeExecutionAuthorized=false` explicit
- [ ] S5 Source Verification Table complete; no aggregate rows; no
  `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Fast Lane audit created
- [ ] Session continuity updated; LHW10 marked CLOSED_PASS_BOUNDED
- [ ] LHW10 roadmap updated: Status CLOSED_PASS_BOUNDED, actual commit SHA in
  Verification, all Acceptance Criteria checked
- [ ] Completion review with LHW10 wave closure summary written

## Return-To-Orchestrator Conditions

Stop if: T1 or T2 completion review missing or not CLOSED_PASS_BOUNDED; any
required first read file is missing; a W5, W4, or LHW9-T1 token cannot be
confirmed; writing the connector requires provider routing change, retry
execution, or MCP transport, or lifts `runtimeExecutionAuthorized=false`; spec
exceeds 250 lines before S4.

## LHW10 Wave Closure Gate

This is the final tranche. After T3 is committed, the completing agent must:

1. Update `CVF_SESSION/ACTIVE_SESSION_STATE.json`:
   - `lhw10WorkflowConnectorWave10.status = CLOSED_PASS_BOUNDED`
   - `nextAllowedMove` must name LHW10 as latest CLOSED_PASS_BOUNDED wave and
     state that any further connector wave requires a fresh roadmap and GC-018
2. Update `CVF_SESSION_MEMORY.md` to reference LHW10 CLOSED_PASS_BOUNDED
3. Update `AGENT_HANDOFF_V14_2026-05-27.md` with full LHW10 wave note

Failure to update all three continuity artifacts blocks the Latest-Closure
Continuity Gate enforced by `run_agent_autorun_workflow_gate.py`.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche; no operator
checkpoint required unless provider routing, retry execution, or new execution
authority is discovered during implementation.

## Claim Boundary

LHW10-T3 produces a documentation artifact. It does not claim W5/W4/LHW9-T1
runtime extension, provider routing change, retry execution, MCP transport,
tool execution, memory injection, receipt envelope extension, provider behavior,
hosted readiness, production readiness, or public release readiness.
