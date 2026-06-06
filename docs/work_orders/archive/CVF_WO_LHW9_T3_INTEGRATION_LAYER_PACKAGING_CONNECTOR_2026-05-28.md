# CVF Work Order — LHW9-T3 Integration Layer Packaging Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW9-T3: a connector spec binding G1 `ExecutionIdentityDecision`
(`executionBoundary.boundary`, `cvfRole`, `authority.canExecute`) × LHW6-T2
`onboardingClassification` (5 values) × LHW7-T1 `reEntryAdvisoryType`
(5 values) into an integration layer packaging advisory packet
(`integrationLayerAdvisoryType`, `onboardingStepRecommended`). Closes the gap
where no standard maps execution boundary + onboarding classification +
re-entry advisory to a named first-governance-record advisory for new
integrations.

Documentation-only tranche. T3 completes the LHW9 wave.

## Authority Chain

- LHW9 roadmap: `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
- LHW9 GC-018: `docs/baselines/CVF_GC018_LHW9_WORKFLOW_CONNECTOR_WAVE9_2026-05-28.md`
- Fast Lane audit: `docs/reviews/CVF_LHW9_T3_FAST_LANE_AUDIT_2026-05-28.md` → FAST_LANE_READY
- T1 gate: `docs/reviews/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
  — CLOSED_PASS_BOUNDED
- T2 gate: `docs/reviews/CVF_LHW9_T2_NONCODER_FRICTION_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
  — CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (triggers: `Review CVF_2.md`, `De_xuat.md`)
- G1 completion: `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- LHW6-T2 spec: `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md`
- LHW7-T1 spec: `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md`

## Agent Roles

Implementer writes spec (S1–S5) using G1, LHW6-T2, and LHW7-T1 vocabulary
verbatim. Reviewer checks all `ExecutionIdentityBoundary` values verbatim, all
`onboardingClassification` values verbatim, all `reEntryAdvisoryType` values
verbatim, `runtimeExecutionAuthorized=false` explicit, boundary table honest,
S5 complete. Auditor confirms LH1 triggers and LHW9 wave closure summary
present. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW9_T3_INTEGRATION_LAYER_PACKAGING_CONNECTOR_SPEC_2026-05-28.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files
- LHW9 roadmap status update to `CLOSED_PASS_BOUNDED` on wave closure

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts`
   — confirm `ExecutionIdentityBoundary` values at lines 20–23;
   confirm `executionBoundary.boundary` at line 45;
   confirm `authority.canExecute` at line 35
4. `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `onboardingClassification` values at S3 line 84 (all 5 values)
5. `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `reEntryAdvisoryType` values at lines 110–111 (all 5 values)
6. `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
   — confirm T3 deliverable shape

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ExecutionIdentityBoundary` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | lines 20–23 | `ExecutionIdentityBoundary` | `ExecutionIdentityBoundary` | ACCEPT |
| `governed_pack_actor_policy` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 21 | `ExecutionIdentityBoundary` value | `ExecutionIdentityBoundary` | ACCEPT |
| `template_execution_policy` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 22 | `ExecutionIdentityBoundary` value | `ExecutionIdentityBoundary` | ACCEPT |
| `role_resolution_denied` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 23 | `ExecutionIdentityBoundary` value | `ExecutionIdentityBoundary` | ACCEPT |
| `executionBoundary.boundary` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 45 | `executionBoundary.boundary` | `ExecutionIdentityDecision` | ACCEPT |
| `authority.canExecute` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 35 | `authority.canExecute` | `ExecutionIdentityDecision` | ACCEPT |
| `safe_first_use` | `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md` | S3 line 84 | `onboardingClassification` value | LHW6-T2 packet | ACCEPT |
| `review_before_first_use` | `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md` | S3 line 84 | `onboardingClassification` value | LHW6-T2 packet | ACCEPT |
| `blocked_first_use` | `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md` | S3 line 84 | `onboardingClassification` value | LHW6-T2 packet | ACCEPT |
| `install_review_required` | `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md` | S3 line 84 | `onboardingClassification` value | LHW6-T2 packet | ACCEPT |
| `network_review_required` | `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md` | S3 line 84 | `onboardingClassification` value | LHW6-T2 packet | ACCEPT |
| `safe_reentry` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | lines 110–111 | `reEntryAdvisoryType` value | LHW7-T1 packet | ACCEPT |
| `reapproval_required` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | lines 110–111 | `reEntryAdvisoryType` value | LHW7-T1 packet | ACCEPT |
| `blocked_no_reentry` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | lines 110–111 | `reEntryAdvisoryType` value | LHW7-T1 packet | ACCEPT |
| `blocked_pending_reviewer` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | lines 110–111 | `reEntryAdvisoryType` value | LHW7-T1 packet | ACCEPT |
| `escalated_no_reentry` | `docs/reference/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_SPEC_2026-05-28.md` | lines 110–111 | `reEntryAdvisoryType` value | LHW7-T1 packet | ACCEPT |
| New doc-only fields `integrationLayerAdvisoryType`, `onboardingStepRecommended` | N/A — doc-only | S3 new fields | doc-only | Integration layer packaging packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T3 spec; G1/LHW6-T2/LHW7-T1 field names verbatim | S1–S5 | spec at target path | Reviewer confirms source-verbatim field names | CLOSED |
| `runtimeExecutionAuthorized=false` explicit | S1, S3, Claim Boundary | invariant stated | `rg -n "runtimeExecutionAuthorized=false" <spec>` | CLOSED |
| Integration layer mapping covering all 5 `onboardingClassification` values | S2 | 5 rows | Reviewer checks S2 rows | CLOSED |
| Source Verification Table complete | S5 | Source Verification Table | Reviewer checks no `BLOCKED_SOURCE_NOT_FOUND` | CLOSED |
| LHW9 wave closure summary | Completion review | T1 + T2 + T3 CLOSED_PASS_BOUNDED | Filed | CLOSED |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW9_T3_INTEGRATION_LAYER_PACKAGING_CONNECTOR_SPEC_2026-05-28.md`

## Pre-Flight

- [x] Working tree clean
- [x] All required first reads done
- [x] G1 `ExecutionIdentityBoundary` confirmed from source (lines 20–23)
- [x] LHW6-T2 `onboardingClassification` values confirmed (S3 line 84)
- [x] LHW7-T1 `reEntryAdvisoryType` values confirmed (lines 110–111)

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all G1/LHW6-T2/LHW7-T1 field names.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective.
6. Update session continuity (`lhw9_t3_complete`).
7. Update LHW9 roadmap to `CLOSED_PASS_BOUNDED`.
8. Commit.
9. Write completion review with LHW9 wave closure summary.

## Evidence Requirements

- Spec at target path with all 5 sections
- S2 integration layer mapping covers all 5 `onboardingClassification` values
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table present
- S5 complete; no `BLOCKED_SOURCE_NOT_FOUND`
- No code file in diff
- Session continuity updated
- LHW9 roadmap updated to `CLOSED_PASS_BOUNDED`
- Completion review with LHW9 wave closure summary

## Acceptance Criteria

- [x] Spec with all 5 sections created
- [x] S2 covers all 5 `onboardingClassification` values
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S4 boundary table honest
- [x] S5 complete
- [x] No code file in diff
- [x] Session continuity updated
- [x] LHW9 roadmap updated to `CLOSED_PASS_BOUNDED`

Fail conditions:

- Missing LHW9 GC-018 or ACCEPT row citing non-existent file
- Any claim of integration execution, role taxonomy change, or lifting
  `runtimeExecutionAuthorized=false`

## Review Gate

All G1/LHW6-T2/LHW7-T1 field names verbatim; `runtimeExecutionAuthorized=false`
explicit; S5 complete; no code file in diff.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 mapping uses G1/LHW6-T2/LHW7-T1 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 complete
- [x] S4 boundary table honest
- [x] No code file in diff
- [x] Session continuity updated
- [x] LHW9 roadmap updated to `CLOSED_PASS_BOUNDED`
- [x] Completion review with LHW9 wave closure summary written

## Return-To-Orchestrator Conditions

Stop if: T2 not CLOSED_PASS; any required read missing; any field cannot be
confirmed; connector requires integration execution or role taxonomy change;
spec exceeds 250 lines.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche; T1 + T2
gates confirmed; no operator checkpoint required.

## Claim Boundary

LHW9-T3 produces a documentation artifact. It does not claim G1/LHW6-T2/
LHW7-T1 runtime extension, integration execution, role taxonomy change, RBAC
change, receipt envelope extension, provider behavior, hosted readiness,
production readiness, or public release readiness. T3 completes the LHW9 wave.
