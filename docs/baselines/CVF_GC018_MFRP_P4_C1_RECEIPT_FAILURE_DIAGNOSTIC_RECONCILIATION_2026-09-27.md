# CVF GC-018 Baseline - MFRP P4-C1 Receipt Failure Diagnostic Reconciliation

Memory class: governed-dispatch-baseline

docType: baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-09-27

Batch ID: MFRP_P4_C1_RECEIPT_FAILURE_DIAGNOSTIC_RECONCILIATION

Dispatch base head: `bc4a969bf27e7e56521e1b93a660d0665f1e0e99`

Commit mode: WORKER_MAY_COMMIT

Decision owner: operator

Reviewer owner: Internal Agent reviewer/closer

Worker target: Internal Agent bounded implementation role

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Reconcile the active P4-C1 evidence collector after a receipt-generation
safety marker lost the identity of the failing checker. Preserve the accepted
counter model and improve only bounded failure diagnostics plus regression
proof.

## Decision / Baseline

The 2026-09-09 observability repair remains controlling authority:
`eligibleCount` counts deterministic enrollment opportunities and
`collectedCount` counts validated samples; only `collectedCount` drives
M5/M10/M20. The older 2026-09-02 wording is superseded on this point and is
not authority to collapse these counters.

The current marker is real safety evidence but its 2,000-character tail lost
the named failure. The collector must preserve stdout and stderr, retain
explicit failure-bearing lines when bounded, and never exceed a fixed marker
diagnostic limit.

## Scope / Target / Owner Boundary

Authorized implementation is limited to the existing collector, its focused
test, this paired dispatch packet, and one completion review. Receipt logic,
P4 comparison, journal rows, counter derivation, checkpoint thresholds, hook
installation, provider calls, public sync and P5/P6 activation are read-only
or forbidden.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| counter split is intentional | current authority | `docs/baselines/CVF_GC018_MFRP_P4_C1_ENROLLMENT_OBSERVABILITY_REPAIR_2026-09-09.md` | Scope / Target / Owner Boundary | `eligibleCount`; `collectedCount` | P4-C1 v2 journal | ACCEPT |
| checkpoints use collected samples | executable source | `governance/compat/mfrp_shadow_canary_autocollect.py` | `_prepare_journal`; `_persist_attempt` | `checkpoint_for_population(journal["collectedCount"])` | P4-C1 collector | ACCEPT |
| failure detail discards early output | executable source | `governance/compat/mfrp_shadow_canary_autocollect.py` | `generate_current_receipt` | prior `(proc.stderr or proc.stdout)[-2000:]` | P4-C1 collector | ACCEPT_ROOT_DEFECT |
| exact failed range now passes | measured diagnostic | `governance/compat/run_agent_autorun_workflow_gate.py` | pre-closure over `e5ce21cb7..bc4a969bf` | one serial plus eight parallel reruns | P2 gate | DIAGNOSTIC_ONLY_NON_REPRODUCED |

## Required Artifact Manifest

| Path | Action |
| --- | --- |
| `docs/baselines/CVF_GC018_MFRP_P4_C1_RECEIPT_FAILURE_DIAGNOSTIC_RECONCILIATION_2026-09-27.md` | CREATE |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_RECEIPT_FAILURE_DIAGNOSTIC_RECONCILIATION_2026-09-27.md` | CREATE |
| `governance/compat/mfrp_shadow_canary_autocollect.py` | MODIFY |
| `governance/compat/test_mfrp_shadow_canary_autocollect.py` | MODIFY |
| `governance/compat/mfrp_p4_enrollment_observability.py` | MODIFY |
| `docs/reviews/CVF_MFRP_P4_C1_RECEIPT_FAILURE_DIAGNOSTIC_RECONCILIATION_COMPLETION_2026-09-27.md` | CREATE |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded P4-C1 receipt-failure diagnostic preservation and its focused regression proof.

Authorized protected paths:

- `governance/compat/mfrp_shadow_canary_autocollect.py`
- `governance/compat/test_mfrp_shadow_canary_autocollect.py`
- `governance/compat/mfrp_p4_enrollment_observability.py`

Operator authorization: the operator directed Local to finish the returned
work, pause NCR, and switch to handling the P4-C1 evidence mechanism.

Rollback boundary: revert only the six-path material batch. Preserve the
accepted P4-C1 hook, journal, receipts, prior commits and unrelated closures.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP_P4_C1_RECEIPT_FAILURE_DIAGNOSTIC_RECONCILIATION --title "MFRP P4-C1 Receipt Failure Diagnostic Reconciliation" --date 2026-09-27 --base bc4a969bf27e7e56521e1b93a660d0665f1e0e99 --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MAY_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with audited counter authority, exact diagnostic defect, bounded manifest and verification contract |
| checkerReadAheadConfirmation | existing accepted P4-C1 packet and focused tests were read before implementation disposition |
| docOnlyNewFields | `FAILURE_DIAGNOSTIC_LIMIT` is implementation-owned, not a journal field |
| claimBoundary | dispatch provenance only; no provider, public, checkpoint or readiness claim |

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
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | protected-path authorization, size threshold, source-verification columns, learning disposition |
| gateRunPurpose | confirm bounded packet and implementation shape |
| claimBoundary | checker conformance does not prove runtime correctness |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| paired paths | both exact paths returned `False` before authoring | CREATE_NEW_SUCCESSOR |
| owner collision | existing collector remains the only hook owner | NO_PARALLEL_OWNER |
| counter collision | 2026-09-09 repair explicitly owns the split semantics | PRESERVE_CURRENT_AUTHORITY |

## Verification / Evidence

Focused tests must prove that a named failure before a long success tail, the
aggregate violation, and stderr all survive within the fixed size limit.
Existing collector/helper tests, size guard, dispatch guards and normal
pre-commit must pass. No flaky-checker identity is claimed without preserved
evidence.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | paired work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | paired completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | active MFRP P4-C1 authority | checkpoint remains initialization | PASS |
| Registry JSON | N/A | N/A with reason: no registry is in scope | PASS |
| Registry Markdown | N/A | N/A with reason: no registry is in scope | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence used | N/A with reason: no external evidence used |
| System loop interlock | current source | no system-loop surface changed | PASS |
| Session continuity | active continuity | rebind follows this closure-shape correction | N/A with reason: performed in the following continuity commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| diagnostic preservation | named failure plus both streams within bound | focused hostile test passes | PASS |
| counter semantics | accepted split unchanged | no counter code changed | PASS |
| marker evidence | recoverable archives | hashes preserved | PASS |
| closure shape | all closed artifacts carry closure package | this block plus paired artifacts | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private collector diagnostic repair only.

## Claim Boundary

This baseline authorizes bounded diagnostic preservation. It does not change
sample eligibility, promote a row, open a checkpoint, identify the prior
transient checker failure, or claim P5/P6 readiness.
