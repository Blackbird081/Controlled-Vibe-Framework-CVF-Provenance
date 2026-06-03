# CVF Work Order — LHW11-T1 Session Governance Posture Aggregator Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-28

---

## Purpose

Implement LHW11-T1: a second-order connector spec that maps four prior LHW
advisory type outputs into a single `sessionGovernancePostureType` +
`highestRiskAdvisory`. Closes the gap where Orchestrators must read 4+ separate
advisory dimensions to determine "what is the overall governance posture of this
session?"

LH1 trigger: `Review CVF_5.md` (PARTIALLY_ABSORBED — "reopen when a concrete
enforcement owner file is selected"; this aggregator is that concrete owner).

**Design constraint:** LHW10-T1 `transitionEnforcementAdvisoryType` has 16
values; LHW10-T3 `providerHealthAdvisoryType` has 24 values. S2 must use
**risk-tier grouping** (not exhaustive combination rows) to stay < 250 lines.
Define 3 risk tiers: `CLEAR` (no blocking advisory), `HOLD` (one or more hold
advisory), `BLOCKED` (any blocked/escalated advisory). Map each input advisory
type to its tier, then derive posture from worst tier across all 4 inputs.

## Authority Chain

- LHW11 roadmap: `docs/roadmaps/CVF_LHW11_WORKFLOW_CONNECTOR_WAVE11_ROADMAP_2026-05-28.md`
- LHW11 GC-018: `docs/baselines/CVF_GC018_LHW11_WORKFLOW_CONNECTOR_WAVE11_2026-05-28.md`
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  (trigger: `Review CVF_5.md`)
- LHW10-T1 spec: `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LHW10-T3 spec: `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LHW9-T1 spec: `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LHW8-T2 spec: `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md`

## Agent Roles

Implementer uses risk-tier grouping in S2 (see Design constraint above) to stay
< 250 lines. Reviewer confirms: tier-to-posture logic is deterministic; all 4
input advisory types are individually row-verified in S5; `runtimeExecutionAuthorized=false`
explicit. Auditor confirms no re-evaluation of source surfaces claimed.
No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
  (new)
- `docs/reviews/CVF_LHW11_T1_FAST_LANE_AUDIT_2026-05-28.md` (new)
- `docs/reviews/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_COMPLETION_2026-05-28.md`
  (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `transitionEnforcementAdvisoryType` S2 values (16 values at lines 84–103)
4. `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `providerHealthAdvisoryType` S2 values (lines 80–115)
5. `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `mcpApprovalAdvisoryType` values at S2 (6 values)
6. `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `authorityChainAdvisoryType` values at S2 (4 values)
7. `docs/roadmaps/CVF_LHW11_WORKFLOW_CONNECTOR_WAVE11_ROADMAP_2026-05-28.md`

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `transitionEnforcementAdvisoryType` field | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 line 137 | `transitionEnforcementAdvisoryType` | LHW10-T1 doc-only field | ACCEPT |
| `safe_transition_resume` | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 line 84 | `transitionEnforcementAdvisoryType` value | LHW10-T1 S2 mapping | ACCEPT |
| `escalated_blocked` | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 lines 88, 90, 94, 98, 102 | `transitionEnforcementAdvisoryType` value | LHW10-T1 S2 mapping | ACCEPT |
| `hold_for_reviewer` | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 line 89 | `transitionEnforcementAdvisoryType` value | LHW10-T1 S2 mapping | ACCEPT |
| `human_review_required` | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 line 91 | `transitionEnforcementAdvisoryType` value | LHW10-T1 S2 mapping | ACCEPT |
| `invalid_transition_blocked` | `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 line 92 | `transitionEnforcementAdvisoryType` value | LHW10-T1 S2 mapping | ACCEPT |
| `providerHealthAdvisoryType` field | `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 new fields | `providerHealthAdvisoryType` | LHW10-T3 doc-only field | ACCEPT |
| `provider_health_nominal` | `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 line 80 | `providerHealthAdvisoryType` value | LHW10-T3 S2 mapping | ACCEPT |
| `provider_health_degraded_fallback_ready` | `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `providerHealthAdvisoryType` value | LHW10-T3 S2 mapping | ACCEPT |
| `provider_health_blocked_quota` | `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 line 104 | `providerHealthAdvisoryType` value | LHW10-T3 S2 mapping | ACCEPT |
| `provider_health_unavailable` | `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 line 107 | `providerHealthAdvisoryType` value | LHW10-T3 S2 mapping | ACCEPT |
| `mcp_advisory_clear` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 row 1 | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `mcp_advisory_hold_pending` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 row 2 | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `mcp_advisory_blocked_by_policy` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `mcpApprovalAdvisoryType` value | LHW9-T1 doc-only field | ACCEPT |
| `authority_chain_clear` | `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S2 row 1 | `authorityChainAdvisoryType` value | LHW8-T2 doc-only field | ACCEPT |
| `authority_chain_blocked` | `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `authorityChainAdvisoryType` value | LHW8-T2 doc-only field | ACCEPT |
| `authority_chain_hold_for_approval` | `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S2 row 2 | `authorityChainAdvisoryType` value | LHW8-T2 doc-only field | ACCEPT |
| `authority_chain_handoff_recommended` | `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `authorityChainAdvisoryType` value | LHW8-T2 doc-only field | ACCEPT |
| `sessionGovernancePostureType` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Session governance posture aggregator packet | ACCEPT |
| `highestRiskAdvisory` (new) | N/A — canonical doc-only field | S3 new fields | doc-only | Session governance posture aggregator packet | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification | Status |
| --- | --- | --- | --- | --- |
| T1 spec; all 4 input advisory types verbatim | S1–S5 | spec at target path | Reviewer confirms verbatim field names | CLOSED |
| Risk-tier grouping in S2 to stay < 250 lines | S2 | tier table with CLEAR/HOLD/BLOCKED rows | Reviewer checks line count | CLOSED |
| `runtimeExecutionAuthorized=false` explicit | S1, S3 | invariant stated | `rg "runtimeExecutionAuthorized=false"` | CLOSED |
| All 4 advisory type names individually row-verified in S5 | S5 | 4 field-level rows | No aggregate rows | CLOSED |
| No code file modified | Evidence | git diff | `git diff --name-only` | CLOSED |

## Deliverable — Connector Spec

File:
`docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`

S2 design: define three risk tiers per input advisory type, then worst-tier
across all 4 inputs determines `sessionGovernancePostureType`:

- `CLEAR` tier: advisory values that allow forward progress
- `HOLD` tier: advisory values that suspend progress pending review/approval
- `BLOCKED` tier: advisory values that block or escalate

`sessionGovernancePostureType` values: `posture_clear` | `posture_hold` | `posture_blocked`

`highestRiskAdvisory`: the specific advisory type value (from any of the 4
inputs) that determines the final posture tier.

Invariants:
- "This connector aggregates advisory outputs. It does not re-evaluate source
  surfaces or change their values."
- `runtimeExecutionAuthorized=false`

## Pre-Flight

- [x] Working tree clean
- [x] All required first reads done
- [x] All 4 input advisory type values confirmed from source specs
- [x] Design constraint understood: use risk-tier grouping, not exhaustive rows

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all 4 input advisory type values from source specs.
3. Design S2 risk-tier table: 3 rows (CLEAR/HOLD/BLOCKED) per advisory type,
   then posture derivation rule.
4. Draft spec (S1–S5); verify line count < 250 after S4.
5. Run Fast Lane audit.
6. Run governance gates.
7. Reviewer perspective.
8. Update session continuity.
9. Commit.
10. Write completion review with T2 gate answer.

## Evidence Requirements

- Spec < 250 lines; S2 uses risk-tier grouping
- All 4 input advisory type names individually row-verified in S5
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table: input advisory types labeled Doc-proven; new fields labeled
  Doc-only; no re-evaluation of source surfaces labeled Not authorized
- No code file in diff

## Acceptance Criteria

- [x] Spec with all 5 sections; < 250 lines
- [x] S2 risk-tier approach; all 4 input advisory types mapped to tiers
- [x] All 4 input advisory type field names individually verified in S5
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S4 boundary honest; no doc-only row labeled Runtime
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:

- Missing LHW11 GC-018 or Source Verification row citing non-existent file
- Spec claims to re-evaluate source surfaces
- `sessionGovernancePostureType` claims runtime enforcement

## Review Gate

Before committing: all 4 input advisory type names verbatim; risk-tier logic
deterministic; `runtimeExecutionAuthorized=false` explicit; S5 complete; spec
< 250 lines; no code file in diff.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 risk-tier mapping covers all 4 input advisory types
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 Source Verification Table complete; no aggregate rows
- [x] S4 boundary honest
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity will be updated after commit
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop if: any required first read file is missing; an input advisory type cannot
be confirmed; writing the connector requires runtime re-evaluation or claims
enforcement; spec exceeds 250 lines before S4.

## T2 Gate Output

Was a concrete spec-change governance decision gap identified during T1?

**Expected YES:** T1 posture aggregator shows that when both
`faultToRespecAdvisoryType` (LHW7-T3) and `transitionEnforcementAdvisoryType`
(LHW10-T1) are active, no connector maps their combination into a named
`specChangeGovernanceDecision` + `rollbackRecommended` boolean. T2 closes that
gap.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche; no operator
checkpoint required unless re-evaluation of source surfaces is discovered.

## Claim Boundary

LHW11-T1 produces a documentation artifact. It does not claim re-evaluation of
source surfaces, runtime aggregation, enforcement, memory reinjection, receipt
envelope extension, provider behavior, hosted readiness, production readiness,
or public release readiness.
