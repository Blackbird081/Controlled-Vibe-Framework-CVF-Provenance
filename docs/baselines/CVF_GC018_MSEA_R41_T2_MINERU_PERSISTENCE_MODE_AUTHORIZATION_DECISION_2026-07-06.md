# CVF GC-018 Baseline - MSEA R41 T2 MinerU Persistence Mode Authorization Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION

Dispatch base head: b5c200480

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: Codex reviewer or delegated reviewer

Worker target: delegated worker

## Purpose

Author a source-verified, docs-only authority decision for the next MinerU system-chain gap: who may set `fileBackedPersistenceRequested` true, under what receipt and invariant conditions, and whether that authority is ready for a later narrow implementation packet, must remain held, or should stop.

rawMemoryReleased=false. This baseline does not authorize raw memory release, retrieval, reinjection, private-output reading, memory write, or Memory/RAG route release.

## Baseline Decision

| Field | Disposition |
| --- | --- |
| proposed tranche | MSEA-R41-T2 MinerU Persistence Mode Authorization Decision |
| baseline decision | DISPATCH_READY for docs-only authority decision |
| dependency evidence | R41-T1 completion review `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md` at material commit `51216fb9a` |
| release boundary | This baseline permits worker-authored decision artifacts only; implementation remains forbidden. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION --title "MSEA R41 T2 MinerU Persistence Mode Authorization Decision" --date 2026-07-06 --base b5c200480 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R41-T2 authority-decision scope, source verification rows, ADIF disclosure, collision evidence, and private-only claim boundary. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, and `governance/compat/check_public_export_disposition.py` before authoring. |
| docOnlyNewFields | `persistenceAuthorityActor`, `persistenceAuthorizationConditions`, `persistenceInvariantConditions`, `selectedR41T2Disposition` |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public-sync, package, Web, MCP, model-router, MinerU execution, persistence invocation, or Memory/RAG release behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; this baseline names only owned planned artifacts and verified source files.
- ADIF-0002 - Provider-local files are not authority; only CVF-governed state, accepted R41-T1 artifacts, and runtime source are cited.
- ADIF-0014 - Completeness is bounded to this authority decision; no broad absorption or corpus scan claim is made.
- ADIF-0015 - Route mode is declared as no-commit worker dispatch and worker commit is forbidden.
- ADIF-0020 - Checker read-ahead is recorded before authoring.
- ADIF-0021 - Applicability markers are scoped to this dispatch and do not create external intake or public-sync scope.
- ADIF-0007 - Gate-sensitive terms are placed in explicit control blocks with private-only boundaries.
- ADIF-0016 - Reusable lessons are routed through ADIF only if a new repeated defect is observed.
- ADIF-0017 - Commit ownership is split: worker returns pending artifacts; reviewer/committer owns closure.
- ADIF-0024 - Worker output quality requires fresh gates, workspace hygiene, and provider-local stray-file disclosure.
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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Resolver query`; `Checker Source Read-Ahead Block`; `Source Verification Block`; `Negative Search And Collision Discipline`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this baseline and paired work order only; it does not prove worker execution, closure, runtime behavior, or public export. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R41-T1 selected disposition held file-backed persistence release pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | line 118 | `R41_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_AUTHORITY_GAPS` | R41-T1 decision matrix | ACCEPT |
| R41-T1 names persistence-mode authorization as the next allowed packet | VALUE_SET | `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | lines 153-154 | `persistence-mode authorization` | R41-T1 decision matrix | ACCEPT |
| Active session front door names the same next allowed move | VALUE_SET | `CVF_SESSION_MEMORY.md` | line 144 | `fileBackedPersistenceRequested` | active session front door | ACCEPT |
| Route authority contains `fileBackedPersistenceRequested` | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 40 | `fileBackedPersistenceRequested` | `MineruSystemChainRouteAuthority` | ACCEPT |
| Current persistence mode type is restricted to one in-process literal | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 33 | `MineruSystemChainPersistenceMode` | `MineruSystemChainPersistenceMode` | ACCEPT |
| Current system-chain route rejects file-backed persistence requests | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-107 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `evaluateMineruSystemChainRouteCandidate` | ACCEPT |
| Accepted route result currently reports in-process persistence mode | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 158 | `persistenceMode` | `evaluateMineruSystemChainRouteCandidate` | ACCEPT |
| Harness currently records no file-backed persistence use | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 49, 147 | `fileBackedPersistenceUsed` | MinerU internal system-chain harness result | ACCEPT |
| Harness default input keeps file-backed persistence unrequested | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | line 111 | `fileBackedPersistenceRequested` | MinerU internal system-chain harness input | ACCEPT |
| File-backed durable-memory store factory exists but source existence is not release authority | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 105 | `createFileBackedDurableMemoryStore` | durable memory store factory | ACCEPT |
| Durable memory receipts retain private-output invariants | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | `DurableMemoryReceipt` | ACCEPT |
| Production Memory/RAG route remains not authorized | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 33-34, 64, 231 | `productionRouteAuthorized` | MinerU Memory/RAG route release | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R41-T2 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R41-T2 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R41-T2|CVF_MSEA_R41_T2|R41_T2" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION` returned no matches before authoring. | ACCEPT_NO_COLLISION |
| Collision decision | R41-T2 artifact names are new in governed dispatch/review/reference/session surfaces. | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected; internal governed source-verification dispatch only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: this baseline uses only CVF-governed repository sources and accepted R41-T1 artifacts. |
| Claim boundary | If worker discovers external knowledge is needed, return `BLOCKED_WITH_REASON`; do not absorb it under this packet. |

## Verification Evidence

| Evidence item | Command or source | Expected disposition |
| --- | --- | --- |
| Dispatch source-fidelity | Source Verification Block rows above | All rows remain `ACCEPT` or packet is returned for repair. |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base b5c200480 --head HEAD --enforce` | Required before commit. |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b5c200480 --head HEAD` | Required before commit. |
| Claim boundary | `rawMemoryReleased=false`; private-only Public Export Disposition | No memory release, runtime, or public export claim. |

## Worker Output Plan

| Planned artifact | Required status at handoff | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Pending reviewer review | Must select exactly one R41-T2 disposition token and source-verify every authority claim. |
| `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md` | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON | Must use worker-return scaffold and pass fast gate. |

## Acceptance Criteria

- The paired work order dispatches only a docs-only authority decision.
- The worker is forbidden from source/test edits, MinerU execution, private-output reads, persistence invocation, Memory/RAG release, live/provider proof, public-sync, worker commit, push, or public claim.
- The worker must identify a specific authority actor and invariant conditions if it selects a ready-for-implementation disposition.
- A held or stop disposition must name the unresolved source-backed authority gap.
- The worker must leave artifacts uncommitted for reviewer closure conversion.

## Claim Boundary

This baseline authorizes only R41-T2 dispatch packet execution. It does not authorize implementation, hook wiring, file-backed persistence invocation, production durable-store invocation, Memory/RAG production route release, retrieval, vectorization, live/provider proof, public-sync, use-case/legal work, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch baseline. No public-sync artifact is changed or authorized by this packet.
