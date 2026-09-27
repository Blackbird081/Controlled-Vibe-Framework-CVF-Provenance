# CVF GC-018 Baseline - MFRP P4-C1 Bounded Retry Recovery

Memory class: governed-dispatch-baseline

docType: baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-09-27

Batch ID: MFRP_P4_C1_BOUNDED_RETRY_RECOVERY

Dispatch base head: `ee09cf7d41352bdd5bee12004c1bd809f3de7c37`

Commit mode: WORKER_MAY_COMMIT

Decision owner: operator

Reviewer owner: Internal Agent reviewer/closer

Worker target: Internal Agent bounded implementation role

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Repair P4-C1 evidence starvation without weakening admission: retain missed
prospective eligible evidence in a derived retry queue, attempt at most one
missed trusted commit on a later otherwise-ineligible disclosure, and preserve
the full receipt/pre-closure validation path.

## Decision / Baseline

The observed journal had 804 attempts, 73 eligible opportunities and one
collected sample. Twenty-four opportunities were historical-only; 34
prospective failures were mechanically retryable. The collector's immediate-
parent-only selection made repaired evidence permanently unreachable.

Retry is therefore allowed under all of these constraints:

- current trusted parent has no eligible candidate;
- the queued source is prospective, uniquely selected and failed only with
  `UNSAFE_AUTORUN_RECEIPT_GENERATION_FAILED` or
  `SKIPPED_NO_COMMITTED_EVIDENCE`;
- newest eligible backlog item is selected deterministically;
- one trusted commit receives at most one retry;
- candidate path and unique selection must still match committed bytes;
- retry traverses the unchanged receipt, reconciliation, order and append
  owners;
- retry attempts do not increment `eligibleCount` or `candidateCount`;
- no automatic loop drains multiple samples in one hook invocation.

## Scope / Target / Owner Boundary

The existing collector remains the sole hook owner. The existing observability
helper owns retry selection and derived telemetry. P2 receipt validation, P4
row construction, comparator behavior, checkpoint thresholds and safety
markers remain unchanged.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| one-shot parent selection strands repaired evidence | executable source | `governance/compat/mfrp_shadow_canary_autocollect.py` | `run_collection` | `_single_parent`; `_discover_candidate` | P4-C1 collector | ACCEPT_ROOT_DEFECT |
| retryable backlog contains 34 prospective items | runtime diagnostic | `.cvf/runtime/mfrp-p4-shadow-canary/pending_observations.json` | normalized v2 journal | eligible failure outcomes | ignored P4-C1 journal | DIAGNOSTIC_ONLY |
| only collected samples advance checkpoints | current authority | `docs/baselines/CVF_GC018_MFRP_P4_C1_ENROLLMENT_OBSERVABILITY_REPAIR_2026-09-09.md` | Scope boundary | `collectedCount` | P4-C1 journal | ACCEPT |
| collector must remain below size guard | machine policy | `governance/compat/check_python_automation_size.py` | near-hard rule | Python helper threshold | size guard | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
| --- | --- |
| Runtime/source paths checked | current collector, observability helper, focused tests and ignored journal |
| Runtime behavior claimed | bounded recovery on an otherwise-ineligible disclosure |
| Helper/checker implementation claimed | source diff plus focused and repository gates |
| Provider/live proof claimed | N/A_WITH_REASON: no provider or live execution is authorized |
| Provider registry surfaces | N/A_WITH_REASON: outside this private collector repair |
| Public-sync claimed | N/A_WITH_REASON: private-only repair |
| Freshness disposition | PASS - current source and journal inspected on 2026-09-27 |

## Required Artifact Manifest

| Path | Action |
| --- | --- |
| this baseline | CREATE |
| paired work order | CREATE |
| `governance/compat/mfrp_p4_enrollment_observability.py` | MODIFY |
| `governance/compat/mfrp_shadow_canary_autocollect.py` | MODIFY_AND_SHRINK |
| `governance/compat/test_mfrp_p4_enrollment_observability.py` | MODIFY |
| `governance/compat/test_mfrp_shadow_canary_autocollect.py` | MODIFY |
| paired completion review | CREATE |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded P4-C1 retry selection, telemetry,
collector integration, hostile tests and mechanical collector shrink.

Protected paths:

- `governance/compat/mfrp_p4_enrollment_observability.py`
- `governance/compat/mfrp_shadow_canary_autocollect.py`
- `governance/compat/test_mfrp_p4_enrollment_observability.py`
- `governance/compat/test_mfrp_shadow_canary_autocollect.py`

Operator authorization: operator explicitly directed Local to fix the
evidence-collection starvation after reviewing the 1-of-73 yield diagnosis.

Rollback boundary: revert only this seven-path batch; preserve prior journal,
rows, adjudicated markers, receipt owners and unrelated closures.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | protected paths, shrink threshold, closure rows, learning dispositions |
| gateRunPurpose | confirm bounded recovery and closure shape |
| claimBoundary | checker conformance does not itself prove retry collection |

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

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | N/A with reason: packet follows the accepted protected-path P4-C1 predecessor shape |
| generatedProfile | protected-governance-path plus WORKER_MAY_COMMIT profile |
| generatedSkeletonStatus | MANUALLY_AUTHORED_FROM_ACCEPTED_PREDECESSOR |
| manualEditsAfterScaffold | source-proven backlog, retry bounds, telemetry, tests and closure evidence |
| checkerReadAheadConfirmation | applicable sources listed above were inspected |
| docOnlyNewFields | `retryableCount`; `retryAttemptCount`; `retryCollectedCount`; `retryOfTrustedCommit` |
| claimBoundary | dispatch provenance only |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | paired work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | paired completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | P4-C1 active collection | M5 remains closed | PASS |
| Registry JSON | N/A | N/A with reason: no registry in scope | PASS |
| Registry Markdown | N/A | N/A with reason: no registry in scope | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence | N/A with reason: no external evidence |
| System loop interlock | current source | no loop surface changed | PASS |
| Session continuity | active continuity | separate post-material rebind | N/A with reason: following continuity commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| retry bound | one retry per trusted commit | hostile tests | PASS |
| admission strength | unchanged receipt/pre-closure path | existing collector seam reused | PASS |
| counter integrity | retry does not inflate opportunity counts | hostile tests | PASS |
| size policy | collector shrinks at least 50 lines | 809 lines versus 859 base | PASS |

## Verification And Evidence

- Focused suite: 69 tests passed across the observability helper and collector.
- Journal diagnostic: 34 prospective trusted commits are retryable under the
  bounded policy; historical attempts remain excluded.
- Size evidence: collector is 809 lines, down from 859 at dispatch base.
- Admission evidence: retry reuses the existing receipt, reconciliation,
  ordering and append chain; no provider execution is used.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private measurement recovery repair.

## Claim Boundary

This baseline authorizes bounded retry recovery only. It does not bulk-promote
historical evidence, weaken gates, advance M5, resume NCR or open P5/P6.
