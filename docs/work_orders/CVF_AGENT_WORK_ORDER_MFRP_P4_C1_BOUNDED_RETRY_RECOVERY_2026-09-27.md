# CVF Agent Work Order - MFRP P4-C1 Bounded Retry Recovery

Memory class: governed-worker-dispatch

docType: work_order

Status: CLOSED_PASS_BOUNDED

Date: 2026-09-27

Batch ID: MFRP_P4_C1_BOUNDED_RETRY_RECOVERY

Dispatch base head: `ee09cf7d41352bdd5bee12004c1bd809f3de7c37`

executionBaseHead: `ee09cf7d41352bdd5bee12004c1bd809f3de7c37`

Commit mode: WORKER_MAY_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker: Internal Agent bounded implementation role

Reviewer/closer: Internal Agent reviewer/closer

independentProbeRequired: NOT_APPLICABLE_WITH_REASON: pure deterministic queue selection and counter projection are covered by hostile tests; no independent-agent claim

## Dispatch Prompt Envelope

Role: Internal Agent implementer/reviewer for bounded P4-C1 retry recovery.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_BOUNDED_RETRY_RECOVERY_2026-09-27.md`

Commit mode: WORKER_MAY_COMMIT.

executionBaseHead: `ee09cf7d41352bdd5bee12004c1bd809f3de7c37`.

Current-time notes: operator released the paused P4-C1 lane specifically to fix evidence starvation.

Do-not-misread notes: do not weaken gates, bulk-drain backlog, count retries as opportunities, advance checkpoints or resume NCR.

Required first actions: read startup authority, guard orientation, paired baseline, accepted P4-C1 counter authority, collector/helper/tests and applicable checkers.

Return contract: implement the exact seven-path manifest, run focused and repository gates, commit material, synchronize continuity separately and stop.

## Purpose

Implement the paired baseline's bounded one-shot recovery lane and truthful
retry telemetry.

## Scope / Target / Owner Boundary

Target only the existing P4-C1 observability helper and post-commit collector,
their focused tests, and the paired baseline/work-order/completion artifacts.
Local owns implementation, review and material commit. Continuity rebind is a
separate Local-owned commit. Provider execution, public sync, checkpoint
promotion, NCR work and any additional runtime surface remain outside scope.

## Authority Chain

Doctrine -> AGENTS.md -> accepted 2026-09-09 counter repair -> closed
2026-09-27 diagnostic repair -> paired retry baseline -> this work order.

## Agent Roles

Local Internal Agent implements, reviews and commits this bounded repair. The
operator owns any checkpoint release or expansion.

## Required First Reads

- active session front door/bootstrap/handoff;
- guard orientation and literal gotchas;
- paired baseline and accepted P4-C1 predecessors;
- exact source/test paths and checker sources.

## Pre-Flight Checks

Confirm clean tracked worktree, no unresolved safety marker, journal counts
804/73/1, and derived retryable backlog 34 before mutation.

## Write Ownership

Only the seven manifest paths are writable. Ignored journal mutation is owned
only by the installed collector after a committed disclosure.

## Execution Plan

1. Derive a deterministic prospective retry backlog in the pure helper.
2. Add retry telemetry without inflating existing counters.
3. Use one retry only when the current parent has no eligible candidate.
4. Re-run the unchanged receipt/reconciliation/append chain.
5. Add hostile tests, shrink collector, close and sync continuity.

## Evidence Requirements

Require 69 focused tests, size compliance, exact manifest, retry queue count,
one-retry exhaustion proof, unchanged checkpoint code and normal pre-commit.

## Review Gate

Reject if retries bypass receipt generation, retry historical rows, loop more
than once, inflate candidate/eligible counters or leave collector within 25
lines of its hard limit.

## Closure Checklist

- [x] retryable outcomes limited to two source-proven recovery classes;
- [x] historical and already-collected commits excluded;
- [x] one retry per trusted commit enforced;
- [x] current candidate has priority;
- [x] retry telemetry is derived and idempotent;
- [x] full admission path unchanged;
- [x] focused tests and size guard pass.

## Acceptance Criteria

- [x] a current eligible candidate always takes priority over backlog recovery;
- [x] an otherwise-ineligible disclosure attempts no more than one retry;
- [x] each trusted commit is retried at most once;
- [x] historical, collected and non-retryable attempts remain excluded;
- [x] retry attempts do not increase candidate or eligible opportunity counts;
- [x] retry success still requires the full existing admission chain;
- [x] focused tests, size policy and repository closure gates pass.

## Return-To-Orchestrator Conditions

Close only with exact scope and passing gates. Return blocked for any required
gate weakening, provider call or write outside authorization.

## Operator Checkpoint

No checkpoint is needed for this authorized change. M5 and NCR remain parked.

## Required Artifact Manifest

| Artifact | Required action |
| --- | --- |
| paired baseline | CREATE |
| this work order | CREATE |
| `governance/compat/mfrp_p4_enrollment_observability.py` | MODIFY |
| `governance/compat/mfrp_shadow_canary_autocollect.py` | MODIFY_AND_SHRINK |
| `governance/compat/test_mfrp_p4_enrollment_observability.py` | MODIFY |
| `governance/compat/test_mfrp_shadow_canary_autocollect.py` | MODIFY |
| paired completion review | CREATE |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP_P4_C1_BOUNDED_RETRY_RECOVERY
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: TERMINAL_RESULT
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p4-c1-bounded-retry-recovery",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`protected governance path implementation`, role=`reviewer`, lifecyclePhase=`review`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "protected governance path implementation" --role reviewer --lifecycle-phase review --risk-ceiling HIGH --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned zero items |
| Dispatch impact | no defect-specific expansion |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | protected paths, shrink rule, closure rows, convergence enums |
| gateRunPurpose | confirm dispatch and closure shape |
| claimBoundary | structural conformance only |

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one Local agent performs bounded implementation, review, closure and commit stewardship |
| phase | EXECUTION; REVIEW; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=ee09cf7d4`; `executionBaseHead=ee09cf7d4`; `closureBaseHead=ee09cf7d4` |
| changedSetScope(phase) | exact seven material paths; continuity separate |
| traceScope(phase, actor) | one declared Local trace |
| commitOwner(phase) | Local reviewer/closer |
| crossBatchIsolation | NCR, M5/P5/P6, providers and public remain closed |
| Before status evidence | clean tracked worktree; no unresolved marker |
| nextMoveSurfaces | update after accepted material commit |
| Closer designation | Local reviewer/closer |

## Current Runtime Freshness Verification

| Field | Disposition |
| --- | --- |
| Runtime/source paths checked | current collector/helper/tests and ignored journal |
| Runtime behavior claimed | bounded recovery on otherwise-ineligible disclosures |
| Helper/checker implementation claimed | source diff and focused tests |
| Provider/live proof claimed | N/A_WITH_REASON: no provider/live work |
| Provider registry surfaces | N/A_WITH_REASON: out of scope |
| Public-sync claimed | N/A_WITH_REASON: private-only repair |
| Freshness disposition | PASS - inspected on 2026-09-27 |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Internal Agent implementer/reviewer |
| Provider or surface | local private CVF workspace |
| Session or invocation | P4-C1 bounded retry recovery |
| Working directory | repository root |
| Command or tool surface | source inspection, apply_patch, pytest and governance gates |
| Target paths | exact seven-path manifest |
| Allowed scope source | paired baseline and operator instruction |
| Before status evidence | clean at `ee09cf7d4`; journal 804/73/1; retryable 34 |
| After status evidence | exact seven tracked paths |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | bounded retry recovery only |
| Claim boundary | no gate weakening or checkpoint promotion |
| Agent type | Internal Agent |
| Invocation ID | `mfrp-p4-c1-bounded-retry-recovery-2026-09-27` |
| Expected manifest | exact seven paths |
| Actual changed set | exact seven paths |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | existing post-commit collector recovery lane |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: focused tests and repository gates |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact source/test diff |
| invocationBoundary | existing post-commit hook only |
| interceptionBoundary | no new hook, daemon, provider or watcher |
| claimLanguage | one bounded retry on an otherwise-ineligible disclosure |
| forbiddenExpansion | historical promotion, bulk drain, gate weakening, M5/P5/P6 |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | paired completion review | closed status | PASS |
| Roadmap state | P4-C1 collection | M5 remains closed | PASS |
| Registry JSON | N/A | N/A with reason: no registry | PASS |
| Registry Markdown | N/A | N/A with reason: no registry | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence | N/A with reason: no external evidence |
| System loop interlock | current source | unchanged | PASS |
| Session continuity | active continuity | separate rebind | N/A with reason: following commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| focused tests | all pass | 69 passed | PASS |
| retry bound | at most one | hostile test | PASS |
| opportunity counters | no retry inflation | hostile test | PASS |
| size | no violation | collector 809 lines | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private P4-C1 measurement repair.

## Claim Boundary

This work order closes only bounded retry recovery. It does not claim backlog
drain, M5 admission, NCR resume or production readiness.
