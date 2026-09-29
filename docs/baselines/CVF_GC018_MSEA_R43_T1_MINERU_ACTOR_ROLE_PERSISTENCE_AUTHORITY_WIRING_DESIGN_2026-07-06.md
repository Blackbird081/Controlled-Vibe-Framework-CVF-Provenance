# CVF GC-018 Baseline - MSEA R43 T1 MinerU Actor Role Persistence Authority Wiring Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN

Dispatch base head: 6a36aaa2e

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: reviewer or delegated reviewer

Worker target: delegated worker

## Purpose

Author a fresh source-verified, docs-only design packet for explicitly wiring
actor-role authority into the MinerU `fileBackedPersistenceRequested` decision
path. This baseline is opened because R42-T1 confirmed the authority source is
still missing: adjacent actor-role controls exist, but no accepted source uses
them to decide the system-chain file-backed persistence request.

rawMemoryReleased=false. This baseline does not authorize source/test edits,
MinerU runtime execution, private/generated output content reads, file-backed
persistence invocation, persistence-mode widening, provider/live proof,
production Memory/RAG release, public-sync, worker commit, push, or public
claim.

## Baseline Decision

| Field | Disposition |
| --- | --- |
| proposed tranche | MSEA-R43-T1 MinerU Actor Role Persistence Authority Wiring Design |
| baseline decision | DISPATCH_READY for docs-only implementation-design decision only |
| dependency evidence | R42-T1 completion review `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` at material commit `f88ecfaca` |
| release boundary | This baseline permits worker-authored design artifacts only; implementation, runtime proof, persistence invocation, and production release remain forbidden. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition | T1 consequence |
| --- | --- | --- | --- | --- |
| R41-T2 persistence-mode authorization decision | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | `4a08d3ef0` | Held pending authority gaps with a specific reopen condition | R43-T1 must design how the actor-role authority mechanism would satisfy the missing `fileBackedPersistenceRequested` path. |
| R42-T1 source discovery | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` | `f88ecfaca` | Missing source authority confirmed | R43-T1 must not claim existing source already satisfies the gap; it must produce a design only. |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `6a36aaa2e` | Operator may select a fresh actor-role authority wiring design packet | Operator selected this dispatch; packet remains docs-only and no-runtime. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN --title "MSEA R43 T1 MinerU Actor Role Persistence Authority Wiring Design" --date 2026-07-06 --base 6a36aaa2e --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R43-T1 design-only scope, R41/R42 dependency release evidence, source verification rows, ADIF disclosure, collision evidence, and private-only claim boundary. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, `governance/compat/check_public_export_disposition.py`, `governance/compat/check_delta_execution_claim_boundary.py`, `governance/compat/check_external_knowledge_intake_routing.py`, and `governance/compat/check_foundation_storage_layout.py` before authoring. |
| docOnlyNewFields | `selectedR43T1Disposition`, `actorRoleWiringDesignDisposition`, `implementationPacketReadiness` |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public-sync, package, Web, MCP, model-router, MinerU execution, persistence invocation, source/test edit, or Memory/RAG release behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; worker must cite exact files and status evidence only.
- ADIF-0002 - Use only CVF-governed sources for cited evidence; provider-local notes stay out of evidence rows.
- ADIF-0014 - Completeness is bounded to this design decision and not a broad absorption claim.
- ADIF-0015 - Route mode is no-commit worker dispatch and closure conversion is reviewer-owned.
- ADIF-0020 - Checker read-ahead is mandatory before worker writes outputs.
- ADIF-0021 - Applicability markers are scoped; no external intake or public-sync scope is created.
- ADIF-0007 - Gate-sensitive markers are placed only in control/evidence blocks.
- ADIF-0016 - New reusable defect patterns must be promoted to ADIF before closure.
- ADIF-0017 - Commit steward and split ownership are required before any reviewer commit.
- ADIF-0024 - Worker must provide fresh gates, workspace hygiene, static-analysis note handling, and provider-local stray-file disclosure.
- ADIF-0006 - Source Verification symbol cells must contain symbols only.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0006 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0006 |
| Dispatch impact | Worker must perform source verification, no-commit return, fresh gate evidence, static-analysis disposition, and workspace hygiene before handoff. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Resolver query`; `Checker Source Read-Ahead Block`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Required Artifact Manifest`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this baseline and paired work order only; it does not prove worker execution, closure, runtime behavior, implementation readiness, or public export. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R42-T1 accepted missing source authority for the R41-T2 reopen condition | VALUE_SET | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` | lines 64-82 | `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_MISSING_CONFIRMED` | R42-T1 completion review | ACCEPT |
| R42-T1 matrix says the nearest actor-role controls are real but not connected to `fileBackedPersistenceRequested` | VALUE_SET | `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | lines 141-152 | `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_MISSING_CONFIRMED` | R42-T1 decision matrix | ACCEPT |
| R41-T2 reopen condition requires actor/role, second persistence-mode literal/runtime check, or a new invariant field before accepting file-backed persistence | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | lines 137-156 | `Reopen Condition` | R41-T2 decision matrix | ACCEPT |
| Route authority currently carries `fileBackedPersistenceRequested` as a plain boolean field | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 36-44 | `MineruSystemChainRouteAuthority` | MinerU system-chain route candidate | ACCEPT |
| Route candidate currently fail-closes any true file-backed persistence request | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-107 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate | ACCEPT |
| Runtime memory hierarchy defines actor roles and an actor-role decision function | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12 and 245 | `RuntimeMemoryActorRole`; `evaluateRuntimeMemoryAction` | runtime memory hierarchy | ACCEPT |
| Runtime memory action denies durable persistence when the tier does not authorize it and denies actors outside the allowlist | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 253-255 and 273-275 | `evaluateRuntimeMemoryAction` | runtime memory hierarchy | ACCEPT |
| Durable-store invocation helper imports `RuntimeMemoryActorRole`, casts `actorRole`, and calls the supplied store, but does not decide the system-chain file-backed request | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 18 and 371-383 | `invokeMineruDurableStoreWrite` | MinerU durable-store invocation helper | ACCEPT |
| Durable memory store exposes a file-backed store factory that is not selected by the system-chain route candidate | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 105 | `createFileBackedDurableMemoryStore` | durable memory store | ACCEPT |
| Active session next move permits this fresh actor-role wiring design packet | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R43-T1 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R43-T1 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R43-T1|MSEA_R43_T1|R43_T1|CVF_MSEA_R43_T1" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION AGENT_HANDOFF_V37_2026-07-06.md CVF_SESSION_MEMORY.md` returned no matches before authoring. | ACCEPT_NO_ARTIFACT_COLLISION |
| Collision decision | R43-T1 artifact names are new in governed dispatch, review, and reference artifact surfaces. | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected; internal governed source-verification dispatch only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: this baseline uses only CVF-governed repository sources and accepted R41/R42 artifacts. |
| Claim boundary | If worker discovers external knowledge is needed, return `BLOCKED_WITH_REASON`; do not absorb it under this packet. |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Applicability | N/A with reason: this work does not create, split, relocate, refactor, or index durable governance foundation files. |
| Reference-family folder effect | N/A with reason: the worker may create one dated companion reference artifact under the existing reference root only; no stable reference family folder or README front door is created. |
| Storage layout action | N/A with reason: no folder movement, stable-path policy change, date-policy change, index update, or storage layout decision is authorized. |
| Claim boundary | This block prevents design-packet work from being misread as durable governance storage-layout mutation. |

## Worker Output Plan

| Planned artifact | Required status at handoff | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md` | Pending reviewer review | Must select exactly one R43-T1 disposition token and source-verify every design option. |
| `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md` | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON | Must use worker-return scaffold and pass fast gate. |

## Verification Evidence

| Evidence item | Command or source | Expected disposition |
| --- | --- | --- |
| Dispatch source-fidelity | Source Verification Block rows above | All rows remain `ACCEPT` or packet is returned for repair. |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 6a36aaa2e --head HEAD --enforce` | Required before commit. |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 6a36aaa2e --head HEAD` | Required before commit. |
| Claim boundary | `rawMemoryReleased=false`; private-only Public Export Disposition | No memory release, runtime, production release, source/test edit, or public export claim. |

## Acceptance Criteria

- The paired work order dispatches only a docs-only actor-role wiring design packet.
- The worker is forbidden from source/test edits, MinerU execution, private-output reads, persistence invocation, Memory/RAG release, live/provider proof, public-sync, worker commit, push, or public claim.
- The worker must distinguish type-cast existence from decision-path authority.
- The worker must evaluate whether to reuse `evaluateRuntimeMemoryAction`, introduce a narrow route-authority actor-role field, or keep the lane held.
- A design-ready disposition must name the exact implementation surfaces to be changed in a later packet, but must not implement them.
- The worker must leave artifacts uncommitted for reviewer closure conversion.

## Claim Boundary

This baseline authorizes only R43-T1 docs-only actor-role persistence
authority wiring design. It does not authorize implementation, hook wiring,
source/test edits, file-backed persistence invocation, production durable-store
invocation, Memory/RAG production route release, retrieval, vectorization,
live/provider proof, public-sync, use-case/legal work, worker commit, push, or
public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch baseline. No public-sync
artifact is changed or authorized by this packet.
