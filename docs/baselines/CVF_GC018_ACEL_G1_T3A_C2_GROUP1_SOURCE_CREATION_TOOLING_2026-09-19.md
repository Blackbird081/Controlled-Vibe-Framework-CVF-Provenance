# CVF GC-018 Baseline - ACEL G1 T3A-C2 Group 1 Source-Creation Tooling

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3A-C2-GROUP1-SOURCE-CREATION-TOOLING

Dispatch base head: `835dfc39d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner and reviewer: Local orchestrator/reviewer

Worker target: shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize a bounded worker to implement and hermetically test tooling for a
later Party A creation of the Group 1 verifier-key registry and genesis
lifecycle receipt. The worker must not perform the real source write.

## Decision / Baseline / Proposed Tranche

Decision: dispatch one tooling-only tranche after Local verification of the
ceremony public product. Baseline: Group 1 is still `SOURCE_NOT_CREATED` and
Party A remains its exclusive writer. Proposed tranche: implement exact-path
writer/checker/test artifacts, then return for Local review before any real
operator write.

## Evidence / Verification

The public key decodes to 32 bytes and independently recomputes to the recorded
SHA-256; both future source paths and all worker outputs were absent at
dispatch. Pre-dispatch autorun and the material hook must pass before handoff.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3A-C2-GROUP1-SOURCE-ESTABLISHMENT --title "ACEL G1 T3A-C2 Group 1 Source Establishment" --date 2026-09-19 --base 9eabacc8b1daf58fe96cd9da34104c6095f912c5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | narrowed source establishment to principal-bound source-creation tooling; replaced every placeholder; fixed exact paths, acceptance matrix and operator checkpoint |
| checkerReadAheadConfirmation | work-order dispatch, gate-to-role closeability, worker-return quality, scaffold provenance and core-guard sources read before dispatch |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no source/runtime/public behavior exists from this baseline |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T2F Group 1 contract | accepted exact schema, hashing, owner and proposed paths | contract remains current | RELEASED |
| T3A ceremony route | fresh Ed25519 under separate Party A custody selected | real product must exist | RELEASED |
| ceremony product verification | `docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md`, commit `835dfc39d` | 32-byte key and digest independently match; exact principal/SID | RELEASED |
| source write authority | Party A exclusively | worker may build/test only; operator runs accepted tool later | PARKED_OPERATOR_EXECUTION |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase dispatch`.

Returned defects: NONE_RETURNED

Result: zero candidates and zero returned defects. Dispatch impact: none.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | Dispatch Prompt Envelope placement; Required Artifact Manifest; Worker Return Packet Shape Contract; Gate-To-Role table labels; no-commit evidence |
| gateRunPurpose | confirmation after source-driven authoring, not first discovery |
| claimBoundary | applies only to dispatch packet shape and owned paths |

## Source Verification Block

| Claimed item | Source | Verified section | Disposition |
|---|---|---|---|
| registry/lifecycle schemas | T2F operational source contract | Source Group 1; Closed Preimage Field Lists | ACCEPT |
| Party A exclusive writer | T2F operational source contract | Source Group 1 access rows | ACCEPT |
| public ceremony product | T3A-C2 Local verification | Verified Public Metadata; Verification Evidence | ACCEPT |
| output paths absent | bounded `Test-Path` ledger on 2026-09-19 | all four worker outputs and two future sources | ACCEPT_NO_COLLISION |

## Negative Search And Collision Discipline

All four worker outputs and both future source paths returned `False` before
authoring. An exact batch-ID/key-ID search returned no predecessor. The audit
is the sole existing reference to this ceremony product.

## Claim Boundary

This baseline authorizes tooling and hermetic tests only. It does not
authorize the worker to run as Party A, open the Party A profile, access the
DPAPI blob, create the real registry/lifecycle files, stage, commit, admit a
candidate, claim live proof, export publicly or deploy.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-creation preparation with a local principal; no public
artifact is authorized.
