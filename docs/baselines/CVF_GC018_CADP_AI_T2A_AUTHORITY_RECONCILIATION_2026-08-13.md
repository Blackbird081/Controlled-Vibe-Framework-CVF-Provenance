# CVF GC-018 Baseline - CADP-AI-T2A Authority Reconciliation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-13

Batch ID: CADP-AI-T2A-R1

Dispatch base head: `27f5a9c9ce531214d439942dc9e111efd5ced160`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Repair the post-closure authority drift exposed by T3A without mutating grant
v1 or weakening the production binder.

## Scope

Commit grant v2 with a new durable identity and current closed-work-order pin;
then independently prove v1 fail-closed, v2 current-HEAD binding, artifact hash
recomputation, reopen/replay behavior, and no authority widening.

## Non-Goals

No production-source change, old-grant rewrite, provider/live call, raw secret,
T3A implementation, public sync, deployment, production, or cross-runtime
claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation evidence after hash and source inspection |
| claimBoundary | packet conformance is not v2 binding or independent closure evidence |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| v1 fails because its work-order pin differs from current HEAD | current runtime evidence | `docs/reviews/CVF_CADP_AI_T3A_EXECUTION_PLANE_VERIFIED_CAPABILITY_CONSUMER_WORKER_RETURN_2026-08-13.md` | Findings / Position | pinned and current SHA-256 | T3A blocker return | ACCEPT |
| changed bytes must fail closed | runtime source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.ts` | artifact verification | `loadCommittedRepositoryCapabilityGrant` | repository owner source | ACCEPT |
| same grant ID cannot rebind changed bytes | runtime source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.ts` | durable grant registration | `GRANT_ID_REBOUND` | repository owner source | ACCEPT |

## Decision / Baseline

Use additive grant v2. Preserve grant v1 as negative historical evidence.

## Evidence / Verification

Dispatch evidence is the committed T3A blocker, independently recomputed
current Git-blob hashes, current production source, and committed grant v2.
Repair success remains pending worker execution and independent review.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T2A-R1 --title "Authority Reconciliation" --date 2026-08-13 --base 27f5a9c9c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | current hash evidence, additive v2 design and bounded claim |
| checkerReadAheadConfirmation | applicable checker sources inspected |
| docOnlyNewFields | authority drift disposition |
| claimBoundary | scaffold provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defect count: 0.

Returned defects: NONE_RETURNED

Dispatch impact: fresh independent probes remain required.

## Machine Closure Package

N/A with reason: dispatch baseline; reviewer owns closure evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private authority repair.

## Claim Boundary

This baseline authorizes a hermetic additive grant repair only. It does not
re-close T2/F11 or resume T3A without independent acceptance.
