# CVF GC-018 Baseline - MSEA R28 T19 MinerU Durable Store Invocation Release Decision

Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Date: 2026-07-05
Batch ID: MSEA-R28-T19-MINERU-DURABLE-STORE-INVOCATION-RELEASE-DECISION
Dispatch base head: 70632c8c
Commit mode: WORKER_MUST_NOT_COMMIT
Worker role: implementation-release-decision worker
Reviewer role: reviewer/closer
rawMemoryReleased: false

## Purpose

This baseline opens MSEA-R28-T19 as a source-verified, docs-only release-decision tranche for MinerU durable-store invocation. T19 may decide whether a future T20 packet may implement an actual durable-store invocation path using the accepted T18 adapter candidate.

T19 does not authorize actual durable-memory writes, RAG writes, vectorization, retrieval, MinerU runtime execution, private/generated content reads, public-sync, provider/live proof, source edits, test edits, checker edits, hook edits, session-state edits, or worker commits.

## Decision Baseline

| Item | Baseline decision |
| --- | --- |
| T19 scope | Source-verified decision matrix and worker return only |
| Candidate release route under review | Future T20 actual durable-store invocation implementation work order |
| Current durable-store invocation status | Held by T18 adapter-only closure evidence |
| Current memory/RAG write status | Held by T18 adapter-only closure evidence |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closure authority | Reviewer may repair/accept T19 matrix and worker return, then commit material closure |
| Public export disposition | DEFERRED_PRIVATE_ONLY |

## Scope / Target / Owner Boundary

Allowed worker changes:

- Create `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md`.
- Create `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`.
- Source-verify the accepted T18 adapter candidate, durable store write contract, runtime memory hierarchy actor gates, R27 route prerequisites, R24-T4 private-output policy, and current session next-move surfaces.
- Select exactly one T19 decision disposition for the next tranche route.

Forbidden worker changes or claims:

- Do not edit runtime source, tests, checkers, hooks, session state, active handoff, front doors, public-sync files, dashboards, Web/UI, or model-router surfaces.
- Do not call durable memory store write paths, write memory/RAG, vectorize, retrieve, read private/generated MinerU output content, import Candidate Group A, run MinerU runtime, run provider/live proof, run standalone PDF apps, or make public claims.
- Do not claim extraction accuracy, document truth, legal quality, current-law correctness, workflow-chain production readiness, memory write completion, durable-store invocation completion, or RAG availability.
- Do not stage, commit, push, or public-sync.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| T18 adapter-only material closure | `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`, material commit `51966467` | ACCEPT |
| T18 current session route | `CVF_SESSION/state/entries/mseaR28T18MineruActualDurableMemoryWriteAdapterImplementationClosure20260704.json` records T19 next move and held memory/invocation dispositions | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `70632c8c` before T19 authoring | ACCEPT |
| T19 planned paths absent before authoring | `Test-Path` returned `False` for the planned T19 baseline, work order, matrix, and worker-return paths before authoring | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / prior tranche requirement | T19 dispatch handling |
| --- | --- |
| T18 produced an adapter candidate but kept actual durable-store invocation unauthorized | T19 performs a release decision only; no write invocation is allowed inside T19 |
| Durable store persistence has policy, actor, provenance, raw-payload, and receipt invariants | T19 matrix must cite the durable store source before selecting any future T20 route |
| R27 memory/RAG route requires receipt, quality, source pointer, downstream-use status, and claim boundary | T19 matrix must keep memory/RAG write held unless it selects a future implementation packet with those prerequisites explicit |
| R24-T4 private-output policy keeps generated output content private unless later authorized | T19 may use receipt/source metadata only and must not read generated output content |
| Agent handoff contract requires no-commit worker return conversion | T19 is dispatched as WORKER_MUST_NOT_COMMIT with reviewer-owned closure conversion |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T19 --title "MinerU Durable Store Invocation Release Decision" --date 2026-07-05 --base 70632c8c --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added T19 source verification, dependency evidence, handoff contract control, worker return contract, and claim boundaries |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| docOnlyNewFields | `DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX`; `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T19_DECISION_ONLY`; `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T19_DECISION_ONLY` |
| claimBoundary | Dispatch scaffold provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Disclosure count: 0

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Source Verification Block`; source-not-found disposition spelling; `Negative Search And Collision Discipline`; `Evidence Reuse And Encoding Plan`; `Worker Return Packet Shape Contract`; `Public Export Disposition`; `External Knowledge Intake Routing`; `Foundation Storage Layout Block` |
| gateRunPurpose | confirm T19 dispatch artifact shape after checker source read-ahead; not first discovery |
| claimBoundary | checker read-ahead evidence only; no durable-store invocation, memory write, runtime, provider, or public claim |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T18 closure selected an adapter candidate and kept actual invocation and memory write held | `CVF_SESSION/state/entries/mseaR28T18MineruActualDurableMemoryWriteAdapterImplementationClosure20260704.json` | lines 18-22 | `selectedImplementationDisposition`; `memoryWriteDisposition`; `durableStoreInvocationDisposition`; `nextRecommendedMove` | active session generated-source entry | VALUE_SET | ACCEPT |
| T18 worker return states actual durable-store invocation and memory/RAG write remain held beyond T18 | `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | lines 106-108 and 263 | `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T18`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T18_ADAPTER_ONLY` | T18 worker return | VALUE_SET | ACCEPT |
| T18 adapter source exposes metadata-only adapter candidate and durable-store invocation hold token | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 22-27, 198-228, 779-787, and 928-953 | `MineruDurableMemoryWriteAdapterCandidate`; `build_mineru_durable_memory_write_adapter_candidate`; `render_mineru_durable_memory_write_adapter_candidate_payload` | MinerU metadata receipt writer | EXISTS | ACCEPT |
| T18 adapter source fail-closes on unsafe output-content and memory-write inputs | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 824-862 and 871-879 | `output_content_read`; `memory_write_authorized`; `policy_decision`; `actor_authorized`; `provenance_score`; `r27_receipt_prerequisite` | `build_mineru_durable_memory_write_adapter_candidate` | RUNTIME_BEHAVIOR | ACCEPT |
| T18 tests cover deterministic metadata-only adapter payload and fail-closed unsafe inputs | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 787-912 | `test_durable_memory_write_adapter_candidate_is_deterministic_and_metadata_only`; fail-closed parameter cases | pytest suite | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store write input includes provenance, policy, and actor fields | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 | `DurableMemoryWriteInput`; `provenanceScore`; `policyDecision`; `actorAuthorized` | durable memory store TypeScript contract | EXISTS | ACCEPT |
| Durable store write path requires an allowed policy and authorized actor before write admission | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-206 | `write`; `durable_memory_policy_denied` | `DurableMemoryStore.write` | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store rejects raw-payload conditions and low provenance for durable admission | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-155, 249, and 256-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `durable_memory_low_provenance`; `durable_memory_raw_payload_detected` | durable memory store validation helpers | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store persistence occurs through record upsert and backing store write methods | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 291, 402, and 448-450 | `this.upsert(record)`; `upsert`; `writeAll` | durable memory store implementations | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store receipt declares summary-only, non-reinjectable, non-raw-memory release fields | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48 and 173-175 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | `DurableMemoryReceipt`; `makeDurableMemoryReceipt` | VALUE_SET | ACCEPT |
| Runtime memory hierarchy defines durable write actors and durable persistence allowance by tier | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-19, 40-46, 172-201, and 273-275 | `RuntimeMemoryActorRole`; `allowedActors`; `durablePersistenceAllowed`; `actor not allowed` | runtime memory hierarchy | RUNTIME_BEHAVIOR | ACCEPT |
| R27 memory/RAG route requires receipt, quality, source pointer, downstream-use status, and claim boundary before memory authorization | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 71-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | VALUE_SET | ACCEPT |
| R24-T4 private-output policy keeps generated outputs private and exposes only file name/count unless later authorized | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 54 and 64 | `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT` | R24-T4 policy matrix | VALUE_SET | ACCEPT |
| T17 selected T18 adapter implementation candidate and kept memory write unauthorized by decision-only scope | `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | lines 56-57, 141, and 144 | `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` | T17 decision matrix | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| Field / token | Purpose | Runtime status |
| --- | --- | --- |
| `DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX` | Names the T19 decision matrix artifact class | DOC_ONLY_NEW |
| `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE` | Candidate next-route disposition if T19 accepts source evidence for a future implementation packet | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T19_DECISION_ONLY` | T19 hold token for actual memory/RAG write | DOC_ONLY_NEW |
| `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T19_DECISION_ONLY` | T19 hold token for actual durable-store invocation | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

| Evidence class | Encoding plan |
| --- | --- |
| T18 adapter source facts | Cite source paths, symbols, and line anchors in the T19 matrix; do not repeat generated-output content |
| Durable store source facts | Cite contract and write-path symbols; do not call the store |
| Runtime hierarchy facts | Cite actor/tier fields and denial logic; do not change runtime hierarchy |
| Prior review evidence | Use accepted T17/T18 artifacts only as dependency and decision-route evidence; prefer runtime source where source exists |
| Worker return evidence | Use scalar dispositions, command summaries, and changed-file manifests only |

## Current Runtime Freshness Verification

| Check | Result |
| --- | --- |
| Existing T18 adapter source path located | PASS |
| Existing durable store source path located | PASS |
| Existing runtime hierarchy source path located | PASS |
| Existing T18 worker return located | PASS |
| Existing T17 decision matrix located | PASS |
| Planned T19 matrix path absent before authoring | PASS |
| Planned T19 worker-return path absent before authoring | PASS |

## Negative Search And Collision Discipline

| Token / path checked | Result |
| --- | --- |
| `MSEA_R28_T19` | No existing governed T19 artifact found before authoring |
| `MSEA-R28-T19` | Only current next-move/session references found before authoring |
| `DURABLE_STORE_INVOCATION_RELEASE_DECISION` | No existing artifact found before authoring |
| Planned T19 baseline path | Absent before authoring |
| Planned T19 work-order path | Absent before authoring |
| Planned T19 matrix path | Absent before authoring |
| Planned T19 worker-return path | Absent before authoring |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`

Required worker-return sections:

- `# CVF MSEA R28 T19 MinerU Durable Store Invocation Release Decision Worker Return`
- `## Summary`
- `## Scope Completed`
- `## Files Changed`
- `## Source Verification Summary`
- `## Decision Matrix Result`
- `## Guardrail Compliance`
- `## Tests / Gates Run`
- `## Claim Boundary`
- `## Return-To-Orchestrator`

## Acceptance Criteria

| AC | Criterion |
| --- | --- |
| AC1 | Worker creates only the T19 decision matrix and T19 worker return paths listed in this baseline |
| AC2 | T19 matrix source-verifies T18 adapter payload, durable store write contract, durable persistence point, runtime actor gates, R27 prerequisites, and R24-T4 private-output policy |
| AC3 | T19 matrix selects exactly one decision disposition: future T20 invocation implementation candidate, hold pending missing authority, or blocked with source-backed reason |
| AC4 | T19 keeps actual durable-store invocation and memory/RAG write unauthorized by T19 decision-only scope |
| AC5 | Worker return reports changed files, source verification summary, selected decision, gates, and claim boundary |
| AC6 | Worker runs the worker-return fast gate and pre-implementation autorun gate for the T19 changed range |
| AC7 | Worker leaves changes unstaged and uncommitted for reviewer closure conversion |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored work order to single no-commit worker, then reviewer closure conversion |
| phase | dispatch |
| baseHeadFor(phase) | `dispatchBaseHead=70632c8c`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this GC-018 baseline and the paired T19 work order; worker changes are limited to the T19 matrix and T19 worker return; reviewer closure changes may repair those T19 artifacts only |
| traceScope(phase, actor) | dispatcher records scaffold, source verification, ADIF, and checker read-ahead; worker records execution commands and changed files; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher may commit dispatch artifacts; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns continuity commit if required |
| crossBatchIsolation | T19 must not modify T18 artifacts, future T20 artifacts, runtime source, tests, session state, handoff, or public-sync surfaces |
| nextMoveSurfaces | unchanged by worker; reviewer updates next-move surfaces only if T19 is accepted and a new mode/next move is opened |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`

reviewerOwnedClosurePaths:

- `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`

Reviewer conversion rule: reviewer may repair review-packet formatting, GC-051 path-literal issues, closure checklist residue, or source-verification wording inside the T19 matrix and worker return before material closure. Reviewer must not silently convert T19 into runtime implementation.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map citation | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Chain map | MSEA-R28-T19 is a local source-governed release-decision tranche |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | Route as advisory input only; require local source verification before inclusion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T19 matrix and worker return |
| Disposition | No external knowledge is required or authorized for T19 |
| Claim boundary | External claims do not authorize durable-store invocation, memory write, public claims, or runtime edits |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage surface touched | None |
| Runtime storage implementation changed | No |
| Durable store invoked | No |
| Foundation storage claim | T19 may inspect source contracts only; it may not create, mutate, or validate stored runtime records |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | T19 source-verified release-decision dispatch only |
| claimDisposition | CLAIM_REJECTED for execution-control, interception, provider, public, durable-store invocation, and memory-write claims |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT for runtime execution claims; dispatch baseline and work order source verification only |
| actionEvidence | ACTION_EVIDENCE_PRESENT for authored dispatch artifacts only |
| invocationBoundary | No durable store, MinerU, provider, MCP, browser, or runtime invocation is authorized |
| interceptionBoundary | No live interception, enforcement, routing, or production workflow-chain control is claimed |
| claimLanguage | Use decision-route and hold-token language only |
| forbiddenExpansion | Do not expand T19 into implementation, durable write, memory/RAG write, public-sync, provider/live proof, or production-readiness claim |
| Runtime execution authorized | No |
| Provider/live proof authorized | No |
| MinerU runtime execution authorized | No |
| Durable memory write authorized | No |
| Durable-store invocation authorized | No |
| Memory/RAG write authorized | No |
| Public claim authorized | No |
| Worker commit authorized | No |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T19 is private provenance governance work. No public-sync artifact or public catalog claim is authorized by this baseline.

## Claim Boundary

This baseline authorizes only a source-verified T19 release-decision work order and no-commit worker execution. It does not authorize durable-store invocation, durable-memory persistence, memory/RAG write, private/generated output reads, runtime source changes, public-sync, provider/live proof, or any production-readiness claim.
