# CVF GC-018 Baseline - WP-ARCH-003 AR1 Canonical Owner Runtime Path Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-08

Batch ID: WP-ARCH-003-AR1-CANONICAL-OWNER-RUNTIME-PATH-DESIGN

Dispatch base head: `c444aed6cb00deb8b4f423112d6307a795c5850c`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one fresh documentation-only architecture decision tranche for
`WP-ARCH-003`. The worker must produce a closed-field proposal identifying one
canonical owner for each unresolved behavior and the complete producer through
runtime-consumer path; the independent reviewer owns semantic acceptance.

## Accepted Authority

- Operator authorization on 2026-09-08 selects the fresh `WP-ARCH-003` design
  route after DARA-T4 R1 parked with no eligible P4 evidence.
- DARA-T1, DARA-T2B, and DARA-T3 R2 satisfy the first three interlock clauses.
- The old assessment and worker return at `c2a1f7c7c` remain incident evidence,
  not architecture authority and not writable in this tranche.
- P4-C1 remains active at `b9bdba712`; this tranche creates no MFRP sample,
  receipt, collector, readout, or checkpoint.

## Scope / Target / Owner Boundary

The worker may create exactly two artifacts: a fresh assessment and its worker
return. Current TypeScript, tests, old `WP-ARCH-003` incident files, roadmap,
baseline, work order, checkers, continuity, and registries are read-only.

The assessment must cover `ARCH-ABS-007`, `ARCH-ABS-017`, and `ARCH-ABS-021`.
For every unresolved behavior it must name exact producer, trust source,
context carrier, export, registration, composition root, runtime consumer,
positive/negative/bypass/composition tests, compatibility disposition,
rollback paths, and evidence output. Unknown facts fail closed as
a missing-source blocked disposition; the worker must not invent symbols or paths.

## Source / Predecessor Evidence

| Evidence | Source | Accepted fact | Disposition |
|---|---|---|---|
| WP interlock | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | fresh reviewer-owned matrix and complete producer-to-runtime-consumer path are required | ACCEPT |
| matrix contract | `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md` | closed `cvf.dara.architectureBindingMatrix.v1` fields separate machine coverage from reviewer semantics | ACCEPT |
| historical replay | `docs/reviews/CVF_DARA_T3_R2_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-08.md` | DARA-T3 is accepted only as bounded offline evidence | ACCEPT |
| prior proposal | `docs/assessments/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md` | proposed owner/path claims remain incident input, not authority | REJECT_FOR_AUTHORITY_REUSE |

## Decision / Baseline

Decision: `AUTHOR_FRESH_ARCHITECTURE_PROPOSAL_PENDING_REVIEW`.

The worker performs source-bound architecture analysis only. A PASS-shaped
proposal does not open implementation. Reviewer acceptance of the canonical
matrix, its digest, and its committed bytes is required before a later work
order may use `NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO`.

## Required Artifact Manifest

| Path | Action | Owner | Required result |
|---|---|---|---|
| `docs/assessments/CVF_WP_ARCH_003_AR1_CANONICAL_OWNER_RUNTIME_PATH_DESIGN_2026-09-08.md` | CREATE | worker | closed-field architecture proposal with exact source evidence |
| `docs/reviews/CVF_WP_ARCH_003_AR1_CANONICAL_OWNER_RUNTIME_PATH_DESIGN_WORKER_RETURN_2026-09-08.md` | CREATE | worker | pending-review evidence, commands, changed-set and no-commit receipt |

## Acceptance Contract

1. Exactly one canonical owner is selected per unresolved behavior.
2. No implementation symbol is planned in two owner packages unless an exact
   adapter/delegation relation is source-proven.
3. Every path and symbol is repository-relative, current, exact, and free of
   placeholders.
4. Producer-to-runtime-consumer coverage is complete or the criterion blocks.
5. `ARCH-ABS-021` is either source-proven satisfied or blocks; it is not
   converted into unnecessary implementation work.
6. The old incident files remain byte-unchanged.
7. Worker writes only the two manifest paths, stages nothing, and commits
   nothing.

## Review Strategy

The reviewer will consume the returned source table, digest preimage, and
command evidence; inspect all rows as one dependency class; then sample only
decision-changing owner and runtime-path claims. Broad duplicate reruns and
per-row recreation are forbidden without a named contradiction and expected
information gain.

## Evidence / Verification

Dispatch evidence is the source-verification table, exact manifest, negative
search receipt, ADIF resolver result, and successful pre-dispatch autorun gate.
Worker evidence is pending and must return through the paired work order.

## Negative Search And Collision Discipline

| Check | Exact evidence | Disposition |
|---|---|---|
| artifact collision | `Test-Path` over the four exact AR1 paths returned False before authoring | PASS_NO_COLLISION |
| batch collision | `rg -n "WP-ARCH-003-AR1-CANONICAL-OWNER-RUNTIME-PATH-DESIGN" docs CVF_SESSION` returned no match before authoring | PASS_NO_COLLISION |
| authority boundary | historical names remain present by design and are not reused as AR1 output paths | PASS_PRESERVE_HISTORY |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: WP-ARCH-003-AR1-CANONICAL-OWNER-RUNTIME-PATH-DESIGN

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 1

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: INITIAL_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | assessment plus reviewer-owned completion review | design evidence only; no source mutation or implementation authority | exact current source locators and reviewer disposition | N/A with reason: internal design evidence has no adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | operator-relayed worker packet | one invocation, two writable artifacts, no commit | work order, trace, changed-set receipt | external CLI transports a proposal only; no runtime/MCP adapter is created | CONTRACT_ONLY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture owner path design`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch-ready status, source-verification columns, no-commit anchors, external-invocation ceiling, dual-agent dispositions, checker read-ahead fields and private export token |
| gateRunPurpose | confirm the authored packet shape before dispatch, not first discovery |
| claimBoundary | structural conformance cannot accept the future architecture proposal |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id WP-ARCH-003-AR1-CANONICAL-OWNER-AND-RUNTIME-PATH --title "WP-ARCH-003 AR1 Canonical Owner And Runtime Path" --date 2026-09-08 --base c444aed6cb00deb8b4f423112d6307a795c5850c --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --new-independent-critical-evidence NONE --stdout` |
| generatedProfile | generic no-commit external initial dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the operator-approved exact-two design contract and current source boundaries |
| checkerReadAheadConfirmation | applicable dispatch, architecture, dual-agent, read-ahead and export checkers read |
| docOnlyNewFields | none |
| claimBoundary | provenance only; no architecture or runtime acceptance claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture-dispatch evidence; no public-sync authority.

## Claim Boundary

This baseline authorizes one external-worker, two-output, documentation-only
architecture proposal. It does not accept the proposal, edit the old incident
evidence, implement `WP-ARCH-003`, open DARA-T5, change P4-C1, invoke a runtime
provider, expose credentials, stage/commit worker files, publish, push, deploy,
or claim production readiness.
