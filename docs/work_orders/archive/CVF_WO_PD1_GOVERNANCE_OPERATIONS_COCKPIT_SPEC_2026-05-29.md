# CVF Work Order — PD-1 Governance Operations Cockpit Specification

Memory class: FULL_RECORD

Status: HOLD_SOURCE_VERIFICATION_REQUIRED

docType: work_order

Date: 2026-05-29

---

## Purpose

Prepare `docs/product/CVF_GOVERNANCE_OPERATIONS_COCKPIT_SPEC.md` — a
documentation spec mapping each cockpit element to an existing CVF surface.
Closes CVF 25.05 Gap 5 at Phase A.

Gap 5: CVF has per-call advisory outputs (LHW10-T1, LHW10-T3, LHW11-T1,
W4, V3) but no unified operator-grade dashboard spec defining what an operator
sees, at what refresh cadence, with what drill-down paths.

This is documentation only. No UI code change. Phase B (cvf-web wiring)
requires a separate GC-018.

## Authority Chain

- PD GC-018: `docs/baselines/CVF_GC018_PRODUCT_DEPTH_2026-05-29.md`
- PD Roadmap: `docs/roadmaps/CVF_PRODUCT_DEPTH_ROADMAP_2026-05-29.md`
- LHW11-T1: `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
- LHW10-T3: `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- W4 source: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
- V3 source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`

## Agent Roles

Implementer may proceed only after every cockpit element has an existing
source/canonical contract. Reviewer checks: each element has a source-verified
CVF surface; no UI implementation claimed; Phase B explicitly deferred.
No self-review.

## Scope

**Allowed:**

- `docs/product/CVF_GOVERNANCE_OPERATIONS_COCKPIT_SPEC.md` (new — create
  `docs/product/` directory if needed)
- `docs/reviews/CVF_PD1_GOVERNANCE_OPERATIONS_COCKPIT_SPEC_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** Any `EXTENSIONS/` source change, `cvf-web/` UI change, receipt
envelope schema, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md`
   — S3 `sessionGovernancePostureType` field
4. `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — S3 `providerHealthAdvisoryType` field
5. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
   — line 75 `clarityStatus`; line 46 `OperationalBenchmarkClarityStatus`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
   — lines 16–38 `ExecutionDiagnosticClass`
7. `docs/reference/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`
   — required only after LHW13-T2 closes; dispatch remains blocked until this
   exists

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `sessionGovernancePostureType` | `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `sessionGovernancePostureType` | LHW11-T1 doc-only field | ACCEPT |
| `providerHealthAdvisoryType` | `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `providerHealthAdvisoryType` | LHW10-T3 doc-only field | ACCEPT |
| `clarityStatus` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` | line 75 | `clarityStatus` | `OperationalBenchmarkScorecard` | ACCEPT |
| `ExecutionDiagnosticClass` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | lines 16–38 | `ExecutionDiagnosticClass` | `ExecutionDiagnostic` | ACCEPT |
| `mcpApprovalAdvisoryType` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 field list | `mcpApprovalAdvisoryType` | LHW9-T1 doc-only field | ACCEPT |
| `memoryContinuityLevelAdvisoryType` | `docs/reference/CVF_LHW13_T2_MEMORY_CONTINUITY_LEVEL_ADVISORY_CONNECTOR_SPEC_2026-05-29.md` | pending LHW13-T2 closure | `memoryContinuityLevelAdvisoryType` | LHW13-T2 doc-only field | BLOCKED_SOURCE_NOT_FOUND |
| latest release gate evidence file | `docs/evidence/latest-release-gate.md` | file missing at dispatch | `docs/evidence/latest-release-gate.md` | release gate evidence surface | BLOCKED_SOURCE_NOT_FOUND |
| `ExecutionIdentityDecision.decision` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | source verification required before dispatch | `decision` | `ExecutionIdentityDecision` | BLOCKED_SOURCE_NOT_FOUND |
| PD GC-018 authorization | `docs/baselines/CVF_GC018_PRODUCT_DEPTH_2026-05-29.md` | full document | PD-1 authorization | PD GC-018 | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Cockpit spec mapping elements to CVF surfaces | Deliverable | spec doc | Each element has verified source | OPEN |
| Refresh cadence defined | Deliverable | spec doc | per-call vs session-level noted | OPEN |
| Phase B explicitly deferred | Deliverable | spec doc claim boundary | UI wiring not claimed | OPEN |
| No UI code change | Scope Forbidden | git diff | `git diff --name-only` | OPEN |
| All 9 cockpit elements source-verified before dispatch | Pre-Dispatch | source verification table | no `BLOCKED_SOURCE_NOT_FOUND` rows | BLOCKED |

## Deliverable — Cockpit Spec

File: `docs/product/CVF_GOVERNANCE_OPERATIONS_COCKPIT_SPEC.md`

The spec must define 9 cockpit elements, each mapped to a verified CVF surface:

| Cockpit element | CVF surface | Source path | Refresh cadence |
| --- | --- | --- | --- |
| Session governance posture | LHW11-T1 `sessionGovernancePostureType` | LHW11-T1 spec S3 | Per-call |
| Provider lane health | LHW10-T3 `providerHealthAdvisoryType` | LHW10-T3 spec S3 | Per-call |
| Benchmark clarity status | W4 `clarityStatus` | `operational-benchmark-suite.ts` line 75 | Per-session |
| Latest execution diagnostic | V3 `ExecutionDiagnosticClass` | `execution-diagnostics.ts` lines 16–38 | Per-call |
| MCP approval posture | LHW9-T1 `mcpApprovalAdvisoryType` | LHW9-T1 spec S3 | Per-call |
| Memory continuity level | LHW13-T2 `memoryContinuityLevelAdvisoryType` (after T2 closes) | LHW13-T2 spec | Per-session |
| Policy block/allow ratio | V3 `policyViolationRate` from W4 | `operational-benchmark-suite.ts` | Per-session aggregate |
| Release gate status | blocked until a current release-gate evidence path is selected | source path required before dispatch | On-demand |
| Role rejection events | G1 `ExecutionIdentityDecision.decision` | `execution-identity.ts` line 53 | Per-call |

Spec must also define: drill-down paths (which surface to read for detail),
Phase B deferral statement, claim boundary.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] Gate confirmations checked; no `BLOCKED_SOURCE_NOT_FOUND` rows remain

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Return-To-Orchestrator Conditions

Stop if: required gate evidence missing; a cited source file cannot be found;
any cockpit element remains source-unverified; implementing the deliverable
requires a forbidden file change.

## Execution Plan

1. Read all required first reads.
2. Verify all 9 source paths exist and fields are correct; if not, keep this
   work order on HOLD.
3. Write cockpit spec with element table and Phase B deferral.
4. Write completion review.
5. Run governance gates.
6. Update session continuity.
7. Commit.

## Evidence Requirements

- Spec doc with 9 elements, each source-verified
- Refresh cadence noted per element
- Phase B explicitly deferred
- No EXTENSIONS/ source changed

## Acceptance Criteria

- [ ] `docs/product/CVF_GOVERNANCE_OPERATIONS_COCKPIT_SPEC.md` created
- [ ] All 9 cockpit elements mapped to verified CVF surfaces
- [ ] Phase B deferred explicitly
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

All elements source-verified; no `BLOCKED_SOURCE_NOT_FOUND` rows remain;
Phase B deferred; no UI code; no code file.

## Closure Checklist

- [ ] Spec created
- [ ] 9 elements with source verification
- [ ] Phase B deferral explicit
- [ ] Completion review written
- [ ] Governance gates PASS
- [ ] Session continuity updated

## Operator Checkpoint

operator.checkpoint.waiver: Documentation-only; no UI change; R0 risk.

## Claim Boundary

PD-1 Phase A produces a documentation spec only. It does not claim a
functioning governance cockpit, UI implementation, real-time data aggregation,
hosted readiness, production readiness, or public release readiness.
