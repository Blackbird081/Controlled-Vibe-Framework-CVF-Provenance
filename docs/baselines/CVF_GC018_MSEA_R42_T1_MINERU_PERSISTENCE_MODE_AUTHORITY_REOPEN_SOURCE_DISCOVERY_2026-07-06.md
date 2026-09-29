# CVF GC-018 Baseline - MSEA R42 T1 MinerU Persistence Mode Authority Reopen Source Discovery

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY

Dispatch base head: 680d3492a

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: reviewer or delegated reviewer

Worker target: delegated worker

## Purpose

Author a source-verified, docs-only source-discovery packet for the R41-T2
persistence-mode authority reopen condition. This baseline asks the worker to
search current governed source and accepted R41 evidence for an existing actor,
second persistence-mode literal, runtime check, receipt field, or invariant
that can satisfy the R41-T2 reopen condition.

rawMemoryReleased=false. This baseline does not authorize source/test edits,
MinerU runtime execution, private/generated output content reads, file-backed
persistence invocation, persistence-mode widening, provider/live proof, or
Memory/RAG route release.

## Baseline Decision

| Field | Disposition |
| --- | --- |
| proposed tranche | MSEA-R42-T1 MinerU Persistence Mode Authority Reopen Source Discovery |
| baseline decision | DISPATCH_READY for docs-only source discovery only |
| dependency evidence | R41-T4 completion review `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` at material commit `41802d2ff` |
| release boundary | This baseline permits worker-authored decision artifacts only; production route release, persistence invocation, runtime proof, and implementation remain forbidden. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition | T1 consequence |
| --- | --- | --- | --- | --- |
| R41-T2 persistence-mode authorization decision | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | `4a08d3ef0` | Held pending authority gaps with a specific reopen condition | R42-T1 must source-discover only the named missing elements: actor/role, second persistence-mode literal/runtime check, or receipt/invariant field. |
| R41-T4 foundation-chain stop/release decision | `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` | `41802d2ff` | Foundation chain stopped as bounded candidate | R42-T1 is allowed only because operator selected a fresh governed packet after the stop-state, not because any runtime release exists. |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `680d3492a` | Operator may author a fresh R41-T2 reopen authority packet | Operator selected work-order authoring; packet remains docs-only and no-runtime. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY --title "MSEA R42 T1 MinerU Persistence Mode Authority Reopen Source Discovery" --date 2026-07-06 --base 680d3492a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R42-T1 source-discovery scope, R41-T2/R41-T4 dependency release evidence, source verification rows, ADIF disclosure, collision evidence, and private-only claim boundary. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, `governance/compat/check_public_export_disposition.py`, `governance/compat/check_delta_execution_claim_boundary.py`, `governance/compat/check_external_knowledge_intake_routing.py`, and `governance/compat/check_foundation_storage_layout.py` before authoring. |
| docOnlyNewFields | `selectedR42T1Disposition`, `persistenceAuthoritySourceDiscoveryResult`, `reopenEvidenceClass` |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public-sync, package, Web, MCP, model-router, MinerU execution, persistence invocation, or Memory/RAG release behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; worker must cite exact files and status evidence only.
- ADIF-0002 - Use only CVF-governed sources for cited evidence; provider-local notes stay out of evidence rows.
- ADIF-0014 - Completeness is bounded to this source-discovery decision and not a broad absorption claim.
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
| Dispatch impact | Worker must perform source verification, no-commit return, fresh gate evidence, and workspace hygiene before handoff. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Resolver query`; `Checker Source Read-Ahead Block`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Required Artifact Manifest`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this baseline and paired work order only; it does not prove worker execution, closure, runtime behavior, or public export. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R41-T2 selected persistence-mode authorization held pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | line 131 | `R41_T2_PERSISTENCE_MODE_AUTHORIZATION_HELD_PENDING_AUTHORITY_GAPS` | R41-T2 decision matrix | ACCEPT |
| R41-T2 reopen condition names actor/role, second persistence-mode literal/runtime check, or new invariant field as reopen paths | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Reopen Condition section | `Reopen Condition` | R41-T2 decision matrix | ACCEPT |
| R41-T4 selected bounded-candidate stop and preserved R41-T2 reopen condition as future option | VALUE_SET | `docs/reference/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_MATRIX_2026-07-06.md` | lines 106 and 122-126 | `R41_T4_FOUNDATION_CHAIN_STOP_BOUNDED_CANDIDATE` | R41-T4 decision matrix | ACCEPT |
| R41-T4 completion review accepted the bounded-candidate stop without authorizing implementation | VALUE_SET | `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` | Reviewer Decision section | `R41_T4_STOP_RELEASE_DECISION_COMPLETE_BOUNDED_CANDIDATE` | R41-T4 completion review | ACCEPT |
| Persistence-mode type is currently a single literal | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 33 | `MineruSystemChainPersistenceMode` | MinerU system-chain route candidate | ACCEPT |
| Route authority includes `fileBackedPersistenceRequested` as the field named by R41-T2 | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 40 | `fileBackedPersistenceRequested` | MinerU system-chain route candidate | ACCEPT |
| Route candidate fail-closes when file-backed persistence is requested | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-107 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate | ACCEPT |
| Memory-owner authorization has actor role fields in the adjacent route-release helper | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 40-45 | `MineruMemoryOwnerAuthorization` | MinerU Memory/RAG route release candidate | ACCEPT |
| Durable-memory receipt already carries private-output invariants | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35 and 46-48 | `DurableMemoryReceipt` | durable memory store | ACCEPT |
| Active session next move permits a fresh source-verified R41-T2 reopen authority packet | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R42-T1 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R42-T1 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R42-T1 worker outputs | `Test-Path` for the planned matrix, worker return, and completion-review paths returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R42-T1|MSEA_R42_T1|R42_T1|CVF_MSEA_R42_T1" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION AGENT_HANDOFF_V37_2026-07-06.md CVF_SESSION_MEMORY.md` returned no matches before authoring. | ACCEPT_NO_ARTIFACT_COLLISION |
| Collision decision | R42-T1 artifact names are new in governed dispatch/review/reference artifact surfaces. | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected; internal governed source-verification dispatch only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: this baseline uses only CVF-governed repository sources and accepted R41 artifacts. |
| Claim boundary | If worker discovers external knowledge is needed, return `BLOCKED_WITH_REASON`; do not absorb it under this packet. |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Applicability | N/A with reason: this work does not create, split, relocate, refactor, or index durable governance foundation files. |
| Reference-family folder effect | N/A with reason: the worker may create one dated companion reference artifact under the existing reference root only; no stable reference family folder or README front door is created. |
| Storage layout action | N/A with reason: no folder movement, stable-path policy change, date-policy change, index update, or storage layout decision is authorized. |
| Claim boundary | This block prevents source-discovery work from being misread as durable governance storage-layout mutation. |

## Worker Output Plan

| Planned artifact | Required status at handoff | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | Pending reviewer review | Must select exactly one R42-T1 disposition token and source-verify every source-discovery result. |
| `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md` | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON | Must use worker-return scaffold and pass fast gate. |

## Verification Evidence

| Evidence item | Command or source | Expected disposition |
| --- | --- | --- |
| Dispatch source-fidelity | Source Verification Block rows above | All rows remain `ACCEPT` or packet is returned for repair. |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 680d3492a --head HEAD --enforce` | Required before commit. |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 680d3492a --head HEAD` | Required before commit. |
| Claim boundary | `rawMemoryReleased=false`; private-only Public Export Disposition | No memory release, runtime, production release, or public export claim. |

## Acceptance Criteria

- The paired work order dispatches only a docs-only source-discovery packet.
- The worker is forbidden from source/test edits, MinerU execution, private-output reads, persistence invocation, Memory/RAG release, live/provider proof, public-sync, worker commit, push, or public claim.
- The worker must determine whether source-backed evidence already satisfies any R41-T2 reopen path.
- A source-found disposition must cite the exact actor, literal/runtime check, receipt field, or invariant and name the source file and line/section.
- A source-missing disposition must identify each searched source surface and the remaining concrete missing element.
- The worker must leave artifacts uncommitted for reviewer closure conversion.

## Claim Boundary

This baseline authorizes only R42-T1 docs-only persistence-mode authority
reopen source discovery. It does not authorize implementation, hook wiring,
file-backed persistence invocation, production durable-store invocation,
Memory/RAG production route release, retrieval, vectorization, live/provider
proof, public-sync, use-case/legal work, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch baseline. No public-sync
artifact is changed or authorized by this packet.
