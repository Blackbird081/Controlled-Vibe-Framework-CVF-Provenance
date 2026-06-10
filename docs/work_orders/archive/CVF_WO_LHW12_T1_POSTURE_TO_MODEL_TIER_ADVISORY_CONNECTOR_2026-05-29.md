# CVF Work Order — LHW12-T1 Posture-to-Model Tier Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement LHW12-T1: a connector spec mapping LHW11-T1
`sessionGovernancePostureType` (3 values) × CB1 `budgetTier` (3 values) ×
G1 `cvfRole` → `modelTierAdvisoryType` + `recommendedModelTier`.

Source: CVF 28.05 Gap A — no connector maps posture tier to model assignment
advisory. LHW11-T1 says whether session posture is `posture_clear/hold/blocked`;
CB1 says context budget; G1 says actor role. No connector combines these into
a named advisory telling Orchestrators what model tier is appropriate.

This connector is advisory only. It does NOT dispatch model selection or change
provider routing. `runtimeExecutionAuthorized=false` invariant.

## Authority Chain

- LHW12 roadmap: `docs/roadmaps/CVF_LHW12_WORKFLOW_CONNECTOR_WAVE12_ROADMAP_2026-05-29.md`
- LHW12 GC-018: `docs/baselines/CVF_GC018_LHW12_WORKFLOW_CONNECTOR_WAVE12_2026-05-29.md`
- LHW11-T1 spec: `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
- CB1 completion: `docs/reviews/archive/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- G1 completion: `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- CVF 28.05 gap record: GC-018 LHW11 section "New Source Family: CVF 28.05"

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: all 3
`sessionGovernancePostureType` values individually row-verified in S5; all 3
`budgetTier` values individually row-verified; `runtimeExecutionAuthorized=false`
explicit; no runtime model dispatch claimed. Auditor confirms CVF 28.05 Gap A
recorded; no provider routing change. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW12_T1_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo, provider routing change.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
   — confirm `sessionGovernancePostureType` values at S3: `posture_clear`,
   `posture_hold`, `posture_blocked`; confirm `highestRiskAdvisory` field
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts`
   — confirm `RouteRequestContextBudgetTier` at line 6: `minimal`, `standard`,
   `expanded`; confirm `budgetTier` field at line 16
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts`
   — confirm `CVFRole` import at line 1; confirm `cvfRole` field at line 29
6. `docs/roadmaps/CVF_LHW12_WORKFLOW_CONNECTOR_WAVE12_ROADMAP_2026-05-29.md`
   — confirm T1 deliverable shape and mapping design

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `sessionGovernancePostureType` field | `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `sessionGovernancePostureType` | LHW11-T1 doc-only field | ACCEPT |
| `posture_clear` | `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md` | S3 line 55 | `sessionGovernancePostureType` value | LHW11-T1 S3 | ACCEPT |
| `posture_hold` | `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md` | S3 line 55 | `sessionGovernancePostureType` value | LHW11-T1 S3 | ACCEPT |
| `posture_blocked` | `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md` | S3 line 56 | `sessionGovernancePostureType` value | LHW11-T1 S3 | ACCEPT |
| `highestRiskAdvisory` field | `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `highestRiskAdvisory` | LHW11-T1 doc-only field | ACCEPT |
| `RouteRequestContextBudgetTier` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 6 | `RouteRequestContextBudgetTier` | CB1 runtime type | ACCEPT |
| `minimal` (budgetTier) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 6 | `RouteRequestContextBudgetTier` value | CB1 runtime type | ACCEPT |
| `standard` (budgetTier) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 6 | `RouteRequestContextBudgetTier` value | CB1 runtime type | ACCEPT |
| `expanded` (budgetTier) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 6 | `RouteRequestContextBudgetTier` value | CB1 runtime type | ACCEPT |
| `budgetTier` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 16 | `budgetTier` | `RouteRequestContextReadout` | ACCEPT |
| `CVFRole` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 1 import | `CVFRole` from `cvf-guard-contract` | `ExecutionIdentityDecision.cvfRole` | ACCEPT |
| `cvfRole` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 29 | `cvfRole: CVFRole \| null` | `ExecutionIdentityDecision` | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `modelTierAdvisoryType` | Names the posture-to-model planning advisory. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |
| `recommendedModelTier` | Records the non-executing model tier recommendation. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| T1 spec; LHW11-T1/CB1/G1 field names verbatim | S1-S5 | spec at target path | Reviewer confirms verbatim | CLOSED |
| 3 `sessionGovernancePostureType` values individually row-verified | S5 | 3 rows | No aggregate | CLOSED |
| 3 `budgetTier` values individually row-verified | S5 | 3 rows | No aggregate | CLOSED |
| `runtimeExecutionAuthorized=false` explicit | S1, S3 | invariant | grep check | CLOSED |
| No provider routing change | Evidence | git diff | `git diff --name-only` | CLOSED |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`

S2 design — mapping table:

| `sessionGovernancePostureType` | `budgetTier` | `modelTierAdvisoryType` | `recommendedModelTier` | Notes |
| --- | --- | --- | --- | --- |
| `posture_blocked` | any | `model_tier_premium_required` | `premium` | Blocked posture requires highest-capability model regardless of budget |
| `posture_hold` | `expanded` | `model_tier_standard_or_premium` | `standard` | Hold + large context: standard minimum; premium recommended |
| `posture_hold` | `standard` | `model_tier_standard` | `standard` | Hold + normal context: standard tier sufficient |
| `posture_hold` | `minimal` | `model_tier_eco_with_hold_note` | `eco` | Hold + minimal context: eco tier with advisory note about hold status |
| `posture_clear` | `expanded` | `model_tier_standard` | `standard` | Clear + large context: standard for throughput |
| `posture_clear` | `standard` | `model_tier_eco_or_standard` | `eco` | Clear + normal context: eco sufficient |
| `posture_clear` | `minimal` | `model_tier_eco` | `eco` | Clear + minimal: eco tier advised |

Key invariants in S1: "This connector does not dispatch model selection or
change provider routing. `modelTierAdvisoryType` is a governance planning record.
`runtimeExecutionAuthorized=false`."

## Pre-Flight

- [x] Working tree clean
- [x] All required first reads done
- [x] `sessionGovernancePostureType` values confirmed from LHW11-T1 S3
- [x] `budgetTier` values confirmed from CB1 source line 6

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all source symbols from required files.
3. Draft spec (S1–S5); verify < 250 lines after S4.
4. Run Fast Lane audit.
5. Run governance gates:
   `check_work_order_dispatch_quality.py --base 7de75901 --head HEAD --enforce`
   `check_markdown_structural_completeness.py --base 7de75901 --head HEAD --enforce`
6. Reviewer perspective.
7. Update session continuity.
8. Commit.
9. Write completion review with T2 gate answer.

## Evidence Requirements

- Spec < 250 lines
- All 3 `sessionGovernancePostureType` + all 3 `budgetTier` values individually row-verified in S5
- `runtimeExecutionAuthorized=false` explicit in S1 and S3
- S4 boundary table: LHW11-T1 and CB1 fields labeled Runtime-proven / Doc-proven; new fields labeled Doc-only; model dispatch labeled Not authorized
- No code file in diff

## Acceptance Criteria

- [x] Spec with all 5 sections; < 250 lines
- [x] S2 mapping covers all 3 × 3 posture × budget combinations
- [x] All 3 `sessionGovernancePostureType` values individually row-verified in S5
- [x] All 3 `budgetTier` values individually row-verified in S5
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] No model dispatch or provider routing change claimed
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:
- Any claim that this connector dispatches model selection or routes providers
- Aggregate rows in S5 for `sessionGovernancePostureType` or `budgetTier`
- Missing LHW12 GC-018

## Review Gate

All 3 `sessionGovernancePostureType` + 3 `budgetTier` individually verified;
`runtimeExecutionAuthorized=false`; no model dispatch; spec < 250 lines; no code file.

## Closure Checklist

- [x] Spec created with all 5 sections
- [x] S2 mapping uses LHW11-T1/CB1/G1 vocabulary verbatim
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 complete; no aggregate rows
- [x] S4 boundary honest
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity updated
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop if: any required first read missing; connector requires model dispatch or
provider routing; spec > 250 lines before S4.

## T2 Gate Output

Was a concrete outcome pack taxonomy grouping gap identified during T1?

**Expected YES:** T1 model tier mapping reveals that when C8 selects a pack,
no connector maps the pack `domain` field × `missingSignals` → a named
`outcomeGroupAdvisoryType` grouping packs by business outcome. T2 closes that.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW12-T1 produces a documentation artifact. It does not claim runtime model
routing, provider dispatch, receipt envelope extension, memory reinjection,
hosted readiness, production readiness, or public release readiness.
