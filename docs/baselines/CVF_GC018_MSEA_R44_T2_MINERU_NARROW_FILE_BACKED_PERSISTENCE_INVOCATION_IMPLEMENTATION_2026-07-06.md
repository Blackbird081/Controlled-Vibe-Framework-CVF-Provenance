# CVF GC-018 Baseline - MSEA R44 T2 MinerU Narrow File Backed Persistence Invocation Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

rawMemoryReleased=false

Batch ID: MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION

Dispatch base head: 31472cfcc

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: Codex reviewer/closer

Worker target: delegated worker role

## Purpose

Authorize a narrow source/test implementation packet that lets the MinerU system-chain route candidate accept file-backed persistence only when the existing route-local actor-role gate authorizes the request. This baseline authorizes deterministic focused tests for that route behavior, including a test-only temporary file-backed durable store, and does not authorize MinerU runtime execution, private/generated output reads, provider/live proof, production Memory/RAG release, public-sync, or use-case/legal workflow.

## Baseline Decision

Dispatch the paired R44-T2 work order under `WORKER_MUST_NOT_COMMIT` for a bounded source/test implementation tranche. The proposed tranche is narrow: route-candidate persistence-mode widening plus focused tests only, with production release, provider/live proof, private-output reads, public-sync, and use-case/legal workflow held.

## Evidence / Verification

| Evidence class | Command or source | Disposition |
| --- | --- | --- |
| Clean starting point | `git rev-parse --short HEAD` returned `31472cfcc`; `git status --short --untracked-files=all` was empty before authoring | ACCEPT |
| Scaffold provenance | Dispatch scaffold command recorded in Scaffold Provenance Block | ACCEPT |
| ADIF disclosure | Resolver command recorded in ADIF Defect Registry Disclosure | ACCEPT |
| Dependency release | R44-T1 selected readiness for a narrow invocation implementation packet at material commit `c892ba922` and session-sync commit `31472cfcc` | ACCEPT |
| Source verification | Source Verification Block cites current route source, route tests, durable store source, runtime actor role source, and accepted R44-T1 decision evidence | ACCEPT |
| Claim boundary | Baseline states rawMemoryReleased=false and forbids runtime/private-output/provider/public/production claims | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION --title "MSEA R44 T2 MinerU Narrow File Backed Persistence Invocation Implementation" --date 2026-07-06 --base 31472cfcc --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled R44-T2 purpose, dependency evidence, source verification, ADIF disclosure, output manifest, implementation boundary, and private-only disposition |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| docOnlyNewFields | R44_T2_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Dependency Release Evidence

| Dependency | Required evidence | Refreshed evidence | Disposition |
| --- | --- | --- | --- |
| R44-T1 release recheck decision | Accepted source-verified decision selecting readiness for a narrow invocation packet | R44-T1 decision matrix selects `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET` at `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md`; worker return accepted at material commit `c892ba922`; session sync commit `31472cfcc` routes next move to this work-order authoring step | SATISFIED |
| R43-T2 actor-role authority gate | Accepted implementation evidence before route widening | R43-T2 worker return records `ACCEPTED_FOR_MATERIAL_COMMIT`; route source currently contains `FILE_BACKED_PERSISTENCE_ACTOR_ROLE_ALLOWLIST` and `fileBackedPersistenceActorRole`; focused tests prove OPERATOR and GOVERNOR pass the actor gate while unauthorized roles fail closed | SATISFIED |
| Operator use-case boundary | Do not drift into legal/use-case or production workflow | Active session front door and handoff keep legal/use-case workflow parked; this baseline authorizes only source/test route behavior | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Dispatch impact | Packet uses exact source verification, no provider-local authority, no-commit ownership, explicit worker scope, dependency release evidence, and worker hygiene requirements |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Public Export Disposition; WORKER_MUST_NOT_COMMIT; DISPATCH_READY; ACCEPT; VALUE_SET; EXISTS; RUNTIME_BEHAVIOR; DOC_ONLY_NEW; N/A with reason |
| gateRunPurpose | Confirmation after source-read authoring; gate runs are evidence and not first discovery for packet shape |
| claimBoundary | Read-ahead covers dispatch artifact shape and required control blocks only; it does not prove implementation behavior, runtime behavior, or release readiness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R44-T1 selected readiness for a future narrow invocation implementation packet | VALUE_SET | `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | lines 56-58 and 77-79 | `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET` | R44-T1 decision matrix | ACCEPT |
| Route candidate currently imports the runtime actor-role type | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 15 | `RuntimeMemoryActorRole` | MinerU system-chain route candidate | ACCEPT |
| Route authority contains explicit file-backed request and actor-role fields | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 49-60 | `MineruSystemChainRouteAuthority` | MinerU system-chain route candidate | ACCEPT |
| Current persistence mode type remains restricted to in-process-only and must be widened by this implementation | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 46 | `MineruSystemChainPersistenceMode` | MinerU system-chain route candidate | ACCEPT |
| Current route still blocks authorized file-backed requests with the bounded cap token | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 125-144 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `buildMineruSystemChainRouteCandidate` | ACCEPT |
| Current result shape keeps production route unauthorized while carrying a persistence mode value | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 71-79 and 188-197 | `MineruSystemChainRouteCandidateResult` | MinerU system-chain route candidate result | ACCEPT |
| Focused tests already prove authorized OPERATOR and GOVERNOR pass the actor gate but still hit the bounded cap | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 249-290 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate tests | ACCEPT |
| Focused tests already prove missing and unauthorized actor roles fail closed | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 292-361 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_ACTOR_ROLE_NOT_AUTHORIZED` | MinerU system-chain route candidate tests | ACCEPT |
| Durable memory store exposes a file-backed constructor and keeps raw-memory receipt invariants false | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35-49 and 106-110 | `createFileBackedDurableMemoryStore` | Durable memory store | ACCEPT |
| Durable memory store writes summary-only records through policy-gated write behavior | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-305 | `write` | `DurableMemoryStore` | ACCEPT |
| Runtime actor role vocabulary includes OPERATOR and GOVERNOR | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-14 | `RuntimeMemoryActorRole` | Runtime memory hierarchy | ACCEPT |
| Internal harness currently defaults file-backed persistence off and must remain untouched by this packet | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 107-115 and 139-155 | `fileBackedPersistenceUsed` | MinerU internal system-chain harness | ACCEPT |

## New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime/source status |
| --- | --- | --- | --- |
| `R44_T2_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION` | This baseline and paired work order | Batch identifier for the narrow implementation dispatch | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R44-T2 baseline before authoring | `Test-Path docs/baselines/CVF_GC018_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Path existence for R44-T2 work order before authoring | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Path existence for R44-T2 worker return before authoring | `Test-Path docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Token search before authoring | `rg -n "MSEA-R44-T2|MSEA_R44_T2|CVF_MSEA_R44_T2" docs CVF_SESSION CVF_SESSION_MEMORY.md AGENT_HANDOFF_V37_2026-07-06.md EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests` returned no matches before authoring | ACCEPT |
| Collision decision | No existing R44-T2 packet or worker-output path was present | ACCEPT |

## Claim Boundary

This baseline authorizes only dispatch of a narrow source/test implementation packet for route-candidate file-backed persistence behavior under the existing OPERATOR/GOVERNOR actor-role gate. It authorizes deterministic focused unit tests that may use a temporary file-backed durable store fixture. It does not authorize MinerU runtime execution, private/generated output content reads, production Memory/RAG route release, retrieval, vectorization, provider/live proof, Web/UI work, public-sync, use-case/legal workflow, extraction accuracy claims, document truth claims, legal quality claims, current-law correctness claims, workflow-chain production readiness claims, hosted release claims, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch baseline for a bounded source/test implementation tranche. No public-sync artifact, public catalog update, public remote proof, or exported public path is authorized by this packet.
