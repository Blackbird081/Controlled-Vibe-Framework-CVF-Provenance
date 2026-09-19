# CVF GC-018 Baseline - Review Independent Probe Admission T1

Memory class: governed-dispatch-baseline

Status: READY_FOR_DISPATCH

Date: 2026-09-19

Batch ID: REVIEW-INDEPENDENT-PROBE-ADMISSION-T1

Dispatch base head: `ec31f42e61af106d7a818ca19e0411918f3bfb63`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: Local reviewer/closer

Worker target: shared-workspace INTERNAL_AGENT implementation worker

## Purpose

Convert the repeated high-risk self-attestation failure pattern exposed by
ACEL-G1-T3A-C2 into one written rule, one machine guard, and the earliest
applicable autorun enforcement while preserving reviewer judgment and the
machine-first non-duplication boundary.

## Decision / Baseline

Extend the existing Review Cost/MFRP owner; do not create a parallel review
system. High-risk authority, canonicalization, integrity, secret, irreversible,
live, or public-effect work must declare an independent adversarial probe plan
before dispatch. Worker-owned tests may support implementation evidence but
cannot satisfy the independent-probe result. Closure remains blocked until a
reviewer-owned execution records a terminal pass or a reasoned fail/block.

## Scope / Target / Owner Boundary

In scope: the Review Cost standard, a focused checker and tests, binding into
the existing pre-dispatch/pre-closure autorun and worker-return fast gate, and
one worker-return packet. Out of scope: provider calls, live proof, Party A
execution, ACEL source creation, runtime interception, public sync, and changes
to the thirteen parked G1 paths.

## Source / Predecessor Evidence

- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`, Escalation Ladder and Closure Rule.
- `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`, Trigger-Based Review Admission Boundary and Machine-Enforceable Boundary.
- `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md`, Independence And Anti-Self-Attestation Controls.
- `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md`, accepted R3-R1 reviewer evidence.

## Acceptance Boundary

Acceptance requires deterministic trigger classification, a machine-readable
dispatch block, role-separated reviewer evidence at closure, hostile fixtures
covering self-attestation and same-oracle evasions, and no regression in the
existing dispatch/worker-return/pre-commit suites. The guard may validate
evidence shape and role separation; it must not claim semantic truth.

## Verification / Evidence

The worker must run focused tests, existing dispatch-quality tests, existing
worker-return tests, both affected fast gates, governed file-size checks, and
the pre-commit suite after the last edit. The reviewer will evaluate returned
evidence and run only bounded contradiction probes with named information gain.

## Required Artifact Manifest

| Artifact | Required action |
| --- | --- |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | MODIFY with the canonical independent-probe admission rule |
| `governance/compat/check_independent_review_probe_admission.py` | CREATE focused phase-aware guard |
| `governance/compat/test_check_independent_review_probe_admission.py` | CREATE positive and hostile regression suite |
| `governance/compat/run_agent_autorun_workflow_gate.py` | MODIFY to invoke the guard at pre-dispatch and pre-closure |
| `governance/compat/run_worker_return_fast_gate.py` | MODIFY to validate worker-return probe disposition without converting worker evidence into reviewer evidence |
| `docs/reviews/CVF_REVIEW_INDEPENDENT_PROBE_ADMISSION_T1_WORKER_RETURN_2026-09-19.md` | CREATE full worker return |

## Core Guard Self-Protection Authorization

| Protected path | Authorized scope | Operator authorization | Rollback boundary |
| --- | --- | --- | --- |
| `governance/compat/check_independent_review_probe_admission.py` | create the bounded admission guard | operator approved foundation hardening after ACEL review | remove the new guard if focused regression proves false-positive or bypass behavior |
| `governance/compat/test_check_independent_review_probe_admission.py` | create focused tests | same | revert with guard |
| `governance/compat/run_agent_autorun_workflow_gate.py` | add phase-scoped invocation only | same | remove only the new invocation |
| `governance/compat/run_worker_return_fast_gate.py` | add worker-return disposition check only | same | remove only the new invocation |

No authorization is granted for hooks, registries, provider/live paths,
session-state mutation, or any other `governance/compat/` file.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id REVIEW-INDEPENDENT-PROBE-ADMISSION-T1 --title "Independent Review Probe Admission Foundation" --date 2026-09-19 --base ec31f42e61af106d7a818ca19e0411918f3bfb63 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the source-verified owner extension, exact six-path manifest, role separation, and closure semantics |
| checkerReadAheadConfirmation | dispatch-quality, core-guard self-protection, autorun, worker-return and reference structural requirements reviewed |
| docOnlyNewFields | independentProbeRequired; independentProbeDisposition; probeExecutorRole; implementationOracleSeparation; expectedInformationGain; rerunCostReason |
| claimBoundary | dispatch provenance only; no runtime/provider/live/public behavior claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`guard checker maintenance`, role=`WORK_ORDER_AUTHOR`, lifecyclePhase=`WORK_ORDER`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "guard checker maintenance" --role WORK_ORDER_AUTHOR --lifecycle-phase WORK_ORDER --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no extra ADIF-specific control beyond the source-derived acceptance matrix |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; its core/source/table/lifecycle modules; `governance/compat/check_core_guard_self_protection.py`; autorun and worker-return gate entrypoints |
| literalTokensReviewed | governed baseline metadata, exact path authorization, Source Verification, Claim Boundary, Public Export Disposition, worker no-commit return shape |
| gateRunPurpose | confirmation of known artifact shape and dispatch evidence, not discovery by failure |
| claimBoundary | read-ahead covers this baseline/work order and authorized checker bindings only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| repeated errors escalate to written rule, machine check, earliest gate | governance rule | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | Escalation Ladder | rule-to-check-to-gate progression | learning philosophy | ACCEPT |
| independent review must not become worker self-attestation | review authority | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Independence And Anti-Self-Attestation Controls | high-risk canonicalization and authority checks | MFRP roadmap | ACCEPT |
| review admission and non-duplication already have a canonical owner | owner reuse | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Trigger-Based Review Admission Boundary; Machine-Enforceable Boundary | reviewer judgment versus machine shape | Review Cost standard | ACCEPT |
| concrete recurrence exists | empirical evidence | `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md` | reviewer acceptance and R3-R1 evidence | worker self-tests missed authority/JSON defects; Local probes found them | accepted review record | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| baseline/work-order path existence before authoring | both absent at `ec31f42e6` | CREATE |
| independent-probe owner search | Review Cost and MFRP already own review admission/anti-self-attestation | EXTEND_EXISTING_OWNER |
| collision decision | no new roadmap, receipt family, daemon, or parallel reviewer subsystem | NO_COLLISION |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | source-level cooperative gate and deterministic tests only |
| claimDisposition | CLAIM_REJECTED: no runtime interception or universal agent compliance is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: focused test and gate output is required later in the worker return |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: implementation action is delegated and has not occurred |
| invocationBoundary | repository-local Python entrypoints only |
| interceptionBoundary | direct out-of-band invocation remains outside the cooperative gate |
| claimLanguage | enforcement applies when named repository gates run |
| forbiddenExpansion | no provider/live/public/Party A/source-creation action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; public projection is a separate authorized batch.

## Claim Boundary

This baseline authorizes design and implementation of an independent-probe
admission evidence contract inside existing CVF gates. It does not prove probe
semantic quality, execute Party A, create a Group 1 source, or authorize any
external effect.
