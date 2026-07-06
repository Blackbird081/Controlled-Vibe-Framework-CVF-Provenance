# CVF GC-018 Baseline - MSEA R41 T4 MinerU Foundation Chain Stop Release Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION

Dispatch base head: 9046647dc

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: reviewer or delegated reviewer

Worker target: delegated worker

## Purpose

Author a source-verified, docs-only stop/release decision for the MinerU to
memory/scanlayer foundation chain after R38, R39, R40, R41-T1, R41-T2, and
R41-T3 closure evidence. This baseline decides only whether the current
foundation chain remains a bounded candidate, whether a fresh reopen authority
packet is justified, or whether a different held lane should be selected.

rawMemoryReleased=false. This baseline does not authorize raw memory release,
retrieval, reinjection, private-output reading, memory write, file-backed
persistence invocation, persistence-mode widening, provider/live proof, or
Memory/RAG route release.

## Baseline Decision

| Field | Disposition |
| --- | --- |
| proposed tranche | MSEA-R41-T4 MinerU Foundation Chain Stop Release Decision |
| baseline decision | DISPATCH_READY for docs-only stop/release decision only |
| dependency evidence | R41-T3 completion review `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_COMPLETION_2026-07-06.md` at material commit `7c5d94ac5` |
| release boundary | This baseline permits worker-authored decision artifacts only; production route release, persistence invocation, runtime proof, and use-case/legal work remain forbidden. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition | T4 consequence |
| --- | --- | --- | --- | --- |
| R38 system-chain closure audit | `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_COMPLETION_2026-07-06.md` | `42a0f1f02` | Foundation/internal system-chain only | T4 may summarize the bounded foundation state but must not claim production readiness. |
| R39 production Memory/RAG route release authority decision | `docs/reviews/CVF_MSEA_R39_T1_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md` | `bdc865ce0` | Held pending authority gaps | T4 must keep production Memory/RAG route release held unless fresh accepted evidence resolves it. |
| R40 bounded provider/live proof | `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_COMPLETION_2026-07-06.md` | `513a41c66` | Bounded private proof only | T4 must not convert bounded proof into production or public release. |
| R41-T1 file-backed persistence release decision | `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md` | `51216fb9a` | Held pending authority gaps | T4 must keep file-backed persistence release held. |
| R41-T2 persistence-mode authorization decision | `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md` | `4a08d3ef0` | Held pending authority gaps | T4 must preserve the R41-T2 reopen condition. |
| R41-T3 persistence harness readiness decision | `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_COMPLETION_2026-07-06.md` | `7c5d94ac5` | Harness implementation blocked by R41-T2 authority gaps | T4 must not authorize harness implementation. |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `9046647dc` | Operator may stop, select a fresh source-verified reopen packet, select a different held lane, or author R41-T4 | Operator selected continuation; dispatch remains docs-only and no-runtime. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION --title "MSEA R41 T4 MinerU Foundation Chain Stop Release Decision" --date 2026-07-06 --base 9046647dc --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R41-T4 stop/release-decision scope, dependency-release evidence, source verification rows, ADIF disclosure, collision evidence, and private-only claim boundary. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, `governance/compat/check_public_export_disposition.py`, and `governance/compat/check_delta_execution_claim_boundary.py` before authoring. |
| docOnlyNewFields | `selectedR41T4Disposition`, `foundationChainReleaseBoundary`, `nextReopenCondition` |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public-sync, package, Web, MCP, model-router, MinerU execution, persistence invocation, or Memory/RAG release behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; this baseline names only owned planned artifacts and verified source files.
- ADIF-0002 - Provider-local files are not authority; only CVF-governed state and accepted R38-R41 artifacts are cited.
- ADIF-0014 - Completeness is bounded to this stop/release decision and not a broad absorption claim.
- ADIF-0015 - Route mode is declared as no-commit worker dispatch and worker commit is forbidden.
- ADIF-0020 - Checker read-ahead is recorded before authoring.
- ADIF-0021 - Applicability markers are scoped to this dispatch and do not create external intake or public-sync scope.
- ADIF-0007 - Gate-sensitive terms are placed in explicit control blocks with private-only boundaries.
- ADIF-0016 - Reusable lessons are routed through ADIF only if a new repeated defect is observed.
- ADIF-0017 - Commit ownership is split: worker returns pending artifacts; reviewer/committer owns closure.
- ADIF-0024 - Worker output quality requires fresh gates, workspace hygiene, static-analysis note handling, and provider-local stray-file disclosure.
- ADIF-0006 - Source Verification symbol cells contain symbols only, not values or type annotations.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0006 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0006 |
| Dispatch impact | The dispatch is docs-only, no-commit, source-verified, and requires fresh worker-return gates plus workspace hygiene evidence. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Resolver query`; `Checker Source Read-Ahead Block`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Evidence Reuse And Encoding Plan`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this baseline and paired work order only; it does not prove worker execution, closure, runtime behavior, or public export. |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_COMPLETION_2026-07-06.md`
priorVerificationAnchor: `7c5d94ac5`
freshRecomputeRequired: ADIF resolver, R41-T4 token collision search, planned path existence checks, dispatch-quality gate, and pre-dispatch autorun gate
unicodePathHandling: use literal repo paths and UTF-8 safe readers; do not read private/generated MinerU output
extractedTextAuthority: N/A with reason: this dispatch does not extract or validate document body text

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R38 selected foundation-complete stop for the system-chain audit | VALUE_SET | `docs/reviews/CVF_MSEA_R38_T1_T4_MINERU_TO_MEMORY_SCANLAYER_SYSTEM_CHAIN_CLOSURE_AUDIT_COMPLETION_2026-07-06.md` | Accepted T4 disposition and Reviewer Decision sections | `SYSTEM_FOUNDATION_COMPLETE_STOP` | R38 completion review | ACCEPT |
| R39 production Memory/RAG route release remained held pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R39_T1_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | Decision Options and Selected Disposition sections | `R39_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_AUTHORITY_GAPS` | R39-T1 decision matrix | ACCEPT |
| R40 completed only bounded private provider/live proof | VALUE_SET | `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_COMPLETION_2026-07-06.md` | Reviewer Decision section | `R40_T1_PROVIDER_LIVE_PROOF_COMPLETE_BOUNDED_PRIVATE` | R40-T1 completion review | ACCEPT |
| R41-T1 file-backed persistence release remained held pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | Selected Disposition section | `R41_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_AUTHORITY_GAPS` | R41-T1 decision matrix | ACCEPT |
| R41-T2 persistence-mode authorization remained held pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Selected Disposition section | `R41_T2_PERSISTENCE_MODE_AUTHORIZATION_HELD_PENDING_AUTHORITY_GAPS` | R41-T2 decision matrix | ACCEPT |
| R41-T3 minimal persistence harness remained blocked by R41-T2 authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_MATRIX_2026-07-06.md` | Selected Disposition section | `R41_T3_MINIMAL_PERSISTENCE_HARNESS_BLOCKED_BY_R41_T2_AUTHORITY_GAPS` | R41-T3 decision matrix | ACCEPT |
| Active session next move allows R41-T4 docs-only stop/release decision work-order authoring | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| Current R41-T4 dispatch is docs-only stop/release decision authoring | DOC_ONLY_NEW | `docs/baselines/CVF_GC018_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_2026-07-06.md` | Purpose and Baseline Decision sections | `selectedR41T4Disposition` | R41-T4 dispatch baseline | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R41-T4 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R41-T4 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R41-T4 worker outputs | `Test-Path` for the planned matrix, worker return, and completion review paths returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R41-T4|MSEA_R41_T4|R41_T4|CVF_MSEA_R41_T4" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION` returned only active-session next-move references before authoring. | ACCEPT_NO_ARTIFACT_COLLISION |
| Collision decision | R41-T4 artifact names are new in governed dispatch/review/reference artifact surfaces. | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected; internal governed source-verification dispatch only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: this baseline uses only CVF-governed repository sources and accepted R38-R41 artifacts. |
| Claim boundary | If worker discovers external knowledge is needed, return `BLOCKED_WITH_REASON`; do not absorb it under this packet. |

## Verification Evidence

| Evidence item | Command or source | Expected disposition |
| --- | --- | --- |
| Dispatch source-fidelity | Source Verification Block rows above | All rows remain `ACCEPT` or packet is returned for repair. |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 9046647dc --head HEAD --enforce` | Required before commit. |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 9046647dc --head HEAD` | Required before commit. |
| Claim boundary | `rawMemoryReleased=false`; private-only Public Export Disposition | No memory release, runtime, production release, or public export claim. |

## Worker Output Plan

| Planned artifact | Required status at handoff | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_MATRIX_2026-07-06.md` | Pending reviewer review | Must select exactly one R41-T4 disposition token and source-verify any release or stop claim. |
| `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_WORKER_RETURN_2026-07-06.md` | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON | Must use worker-return scaffold and pass fast gate. |

## Acceptance Criteria

- The paired work order dispatches only a docs-only stop/release decision.
- The worker is forbidden from source/test edits, MinerU execution, private-output reads, persistence invocation, Memory/RAG release, live/provider proof, public-sync, worker commit, push, or public claim.
- The worker must select a bounded-candidate stop disposition unless it can source-verify accepted evidence satisfying all held authority gaps named by R39 and R41.
- A reopen disposition must name the exact fresh authority packet class and its concrete reopen condition.
- The worker must leave artifacts uncommitted for reviewer closure conversion.

## Claim Boundary

This baseline authorizes only R41-T4 docs-only stop/release-decision packet
execution. It does not authorize implementation, hook wiring, file-backed
persistence invocation, production durable-store invocation, Memory/RAG
production route release, retrieval, vectorization, live/provider proof,
public-sync, use-case/legal work, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch baseline. No public-sync
artifact is changed or authorized by this packet.
