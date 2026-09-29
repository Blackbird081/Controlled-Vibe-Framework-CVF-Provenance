# CVF Agent Work Order - MSEA R28 T19 MinerU Durable Store Invocation Release Decision

Memory class: governed-work-order
Status: DISPATCH_READY
Date: 2026-07-05
Batch ID: MSEA-R28-T19-MINERU-DURABLE-STORE-INVOCATION-RELEASE-DECISION
GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_2026-07-05.md`
Dispatch base head: 70632c8c
Commit mode: WORKER_MUST_NOT_COMMIT
Worker role: implementation-release-decision worker
Reviewer role: reviewer/closer
rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: implementation-release-decision worker

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_2026-07-05.md`

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: Worker must capture `git rev-parse --short HEAD` at start and report it in the worker return.

Current-time notes: Artifact date is 2026-07-05. T18 material commit `51966467` accepted the durable-memory write adapter candidate, and session-sync head `70632c8c` routes the next allowed move to this T19 release decision. Actual durable-store invocation and memory/RAG write remain held.

Do-not-misread notes: T19 is not actual invocation, not memory write, not source/test implementation, not MinerU runtime, not provider/live proof, not public-sync, and not production-readiness evidence.

Required first actions: read the mandatory startup files, read the T19 GC-018 baseline, capture start HEAD/status, confirm planned worker output paths are absent, then write only the T19 matrix and worker return.

You are executing MSEA-R28-T19 in the private CVF provenance repository.

Task: create a source-verified release-decision matrix and worker return for MinerU durable-store invocation. Decide whether a future T20 packet may implement actual durable-store invocation using the accepted T18 adapter candidate.

Required output paths:

- `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`

Hard boundary: T19 is docs-only decision work. Do not implement durable-store invocation, call durable store write paths, write memory/RAG, vectorize, retrieve, read private/generated MinerU output content, run MinerU runtime, edit source/tests/checkers/hooks/session state/handoff/public-sync, or commit.

Return contract: leave the two T19 worker artifacts unstaged and uncommitted, with worker-return fast gate and pre-implementation autorun evidence recorded.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| canonicalRouteMode | MULTI_AGENT_SINGLE_ROLE |
| selected role route | single no-commit implementation-release-decision worker followed by reviewer closure conversion |
| intake summary | T19 creates a source-verified decision matrix for future durable-store invocation release; it does not implement invocation |
| scope classification | docs-only governed release-decision artifact authoring |
| risk sensitivity | high, because durable memory persistence and private-output boundaries are adjacent but remain unauthorized |
| escalation condition | Return to orchestrator if source facts are missing, planned worker paths collide, or any gate requires out-of-scope source/test/session/checker/hook edits |
| Dispatch role | Orchestrator/dispatcher |
| Worker role | Single implementation-release-decision worker |
| Reviewer role | Reviewer/closer |
| Commit authority | Worker must not commit |
| Closure conversion | Reviewer owns material acceptance, repairs, and commit |

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Dispatcher | Author GC-018 baseline and work order, run pre-dispatch gates, commit dispatch artifacts |
| Worker | Create T19 decision matrix and worker return only, run worker gates, leave changes uncommitted |
| Reviewer/closer | Review and repair T19 worker artifacts if needed, convert worker return to closure, commit material acceptance |
| Session-sync steward | Update session continuity only upon accepted reviewer closure |

## Purpose

T18 implemented and tested a metadata-only durable-memory write adapter candidate, but kept actual durable-store invocation and memory/RAG write unauthorized. T19 must inspect the accepted adapter, durable store source contract, runtime memory hierarchy, and prior route policies, then produce a decision matrix selecting exactly one next-route disposition.

T19 may select a future implementation candidate route. T19 itself may not perform the implementation.

## Authority Chain

| Authority | Required use in T19 |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Confirm current mode and next allowed move before work |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Confirm compact startup state |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Confirm canonical active handoff and current mode |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Confirm active handoff instructions and T19 next allowed move |
| `docs/reference/guard_orientation/README.md` | Identify required governed artifact surfaces |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Avoid known literal-format failures |
| `docs/baselines/CVF_GC018_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_2026-07-05.md` | Execute only the authorized T19 scope |

## Operator Checkpoint

No operator checkpoint blocks T19 worker dispatch. Operator authorization is limited to writing the T19 decision matrix and worker return. Actual durable-store invocation and memory/RAG write remain parked.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| T18 adapter-only material closure | `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`, material commit `51966467` | ACCEPT |
| T18 current session route | `CVF_SESSION/state/entries/mseaR28T18MineruActualDurableMemoryWriteAdapterImplementationClosure20260704.json` records T19 next move and held memory/invocation dispositions | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `70632c8c` before T19 authoring | ACCEPT |
| T19 artifact collision check | Planned T19 baseline, work order, matrix, and worker-return paths were absent before authoring | ACCEPT |

## Scope / Target / Owner Boundary

Allowed worker changes:

- Create the T19 decision matrix.
- Create the T19 worker return.
- Cite accepted T18, T17, R27, R24-T4, durable store source, runtime hierarchy source, and current session evidence.
- Run worker-return fast gate and pre-implementation autorun gate.

Forbidden worker changes or claims:

- Do not edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`.
- Do not edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`.
- Do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`.
- Do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`.
- Do not edit session front doors, generated session source files, active handoff, checkers, hooks, public-sync files, dashboard/Web/UI, or model-router surfaces.
- Do not call durable store write methods, create durable memory records, write memory/RAG, vectorize, retrieve, read generated output content, run MinerU runtime, run provider/live proof, create a standalone PDF app, or import Candidate Group A.
- Do not make extraction accuracy, document truth, legal quality, current-law correctness, workflow-chain production-readiness, public, or provider-backed claims.
- Do not stage, commit, push, or public-sync.

## Write Ownership

| Actor | Owned paths |
| --- | --- |
| Dispatcher | T19 GC-018 baseline and this work order |
| Worker | T19 decision matrix and T19 worker return only |
| Reviewer/closer | Review, repair if needed, material closure commit |
| Session-sync steward | Session memory/state/handoff updates only upon accepted T19 reviewer closure |

## Required First Reads

Worker must read these files before writing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V36_2026-07-04.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
- `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`
- `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md`
- `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`

## Preflight Checks

Worker must run or capture equivalent local evidence:

```text
git status --short
git rev-parse --short HEAD
rg -n "MSEA_R28_T19|MSEA-R28-T19|DURABLE_STORE_INVOCATION_RELEASE_DECISION|durable-store invocation release" docs CVF_SESSION AGENT_HANDOFF_V36_2026-07-04.md
Test-Path docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md
Test-Path docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md
```

Expected preflight result: existing T19 references may appear only in dispatch artifacts and session next-move surfaces. The planned worker output paths should not already exist at worker start.

## Execution Plan

1. Read the required files and confirm T19 boundaries.
2. Create the T19 decision matrix at the required reference path.
3. In the matrix, source-verify:
   - T18 adapter candidate payload and hold dispositions.
   - Durable store write input, policy/actor/provenance checks, raw-payload checks, receipt invariants, and persistence point.
   - Runtime memory hierarchy actor and durable-persistence rules.
   - R27 memory/RAG prerequisites.
   - R24-T4 private-output policy.
4. Select exactly one T19 decision disposition:
   - `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE`
   - `DURABLE_STORE_INVOCATION_RELEASE_HELD_PENDING_SOURCE_OR_AUTHORITY`
   - `DURABLE_STORE_INVOCATION_RELEASE_BLOCKED_WITH_REASON`
5. Keep these hold tokens unless reviewer closure later opens a future T20 authoring route:
   - `MEMORY_WRITE_NOT_AUTHORIZED_BY_T19_DECISION_ONLY`
   - `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T19_DECISION_ONLY`
6. Create the T19 worker return with scope, files changed, source verification summary, selected decision, gates, claim boundary, and return-to-orchestrator.
7. Run required gates and repair in scope.
8. Leave changes unstaged and uncommitted.

## Worker Autonomy / No-Question Rule

Worker may choose the exact matrix layout, provided it includes:

- Source Verification Block.
- Decision Criteria Table.
- Release Decision Matrix.
- Selected Decision Disposition.
- Hold / Block / Future-Route Consequences.
- Guardrail Compliance.
- Claim Boundary.

Worker may repair only the T19 matrix and T19 worker return. Source, tests, session, handoff, checker, hook, runtime, public, and future T20 artifacts are out of scope.

No-Question Rule: If a gate failure is repairable within the two authorized worker artifacts, repair it directly and rerun the gate. Ask the operator only if the requested repair would require out-of-scope files, runtime invocation, private/generated output reads, provider/live proof, commit authority, or a new product decision.

## Return-To-Orchestrator Conditions

Return without completing T19 if any condition is true:

- A required source file is missing.
- A required source fact cannot be verified from source or canonical contract.
- Planned T19 worker output paths already exist with conflicting content at worker start.
- Any gate demands source/test/session/checker/hook edits to pass.
- Durable-store invocation or memory/RAG write would be required to support a claim.
- Private/generated output content would need to be read.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T19 --title "MinerU Durable Store Invocation Release Decision" --date 2026-07-05 --base 70632c8c --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added T19 source verification, dependency evidence, handoff contract control, worker return contract, and claim boundaries |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| docOnlyNewFields | `DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX`; `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE`; `DURABLE_STORE_INVOCATION_RELEASE_HELD_PENDING_SOURCE_OR_AUTHORITY`; `DURABLE_STORE_INVOCATION_RELEASE_BLOCKED_WITH_REASON`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T19_DECISION_ONLY`; `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T19_DECISION_ONLY` |
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
| `DURABLE_STORE_INVOCATION_RELEASE_HELD_PENDING_SOURCE_OR_AUTHORITY` | T19 decision token for a held release route | DOC_ONLY_NEW |
| `DURABLE_STORE_INVOCATION_RELEASE_BLOCKED_WITH_REASON` | T19 decision token for a blocked release route | DOC_ONLY_NEW |
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
| `MSEA-R28-T19` | Only current next-move/session references and newly authored dispatch artifacts found before dispatch |
| `DURABLE_STORE_INVOCATION_RELEASE_DECISION` | No existing worker output artifact found before authoring |
| Planned T19 matrix path | Absent before authoring |
| Planned T19 worker-return path | Absent before authoring |

## Dual Agent Surface Matrix

| Surface | Claude worker allowed | Codex/reviewer allowed | Boundary |
| --- | --- | --- | --- |
| T19 matrix | Yes | Reviewer may repair/accept | Decision artifact only |
| T19 worker return | Yes | Reviewer may repair/accept | Review packet only |
| Runtime source/tests | No | No under T19 | Future T20 requires fresh packet |
| Session state/handoff | No | Session-sync steward only upon accepted reviewer closure | No worker edit |
| Public-sync | No | No | Private provenance only |

## Work-Order Fulfillment Manifest

| Output | Required action |
| --- | --- |
| `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md` | Create source-verified decision matrix |
| `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md` | Create worker return and gate evidence |

No other output files are authorized.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored work order to single no-commit worker, then reviewer closure conversion |
| phase | dispatch |
| baseHeadFor(phase) | `dispatchBaseHead=70632c8c`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this work order and the paired T19 GC-018 baseline; worker changes are limited to the T19 matrix and T19 worker return; reviewer closure changes may repair those T19 artifacts only |
| traceScope(phase, actor) | dispatcher records scaffold, source verification, ADIF, and checker read-ahead; worker records execution commands and changed files; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher may commit dispatch artifacts; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns continuity commit if required |
| crossBatchIsolation | T19 must not modify T18 artifacts, future T20 artifacts, runtime source, tests, session state, handoff, or public-sync surfaces |
| Before status evidence | HEAD `70632c8c`; clean worktree confirmed before T19 dispatch authoring |
| nextMoveSurfaces | unchanged by worker; reviewer updates next-move surfaces only if T19 is accepted and a new mode/next move is opened |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_COMPLETION_2026-07-05.md`

reviewerOwnedClosurePaths:

- `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_COMPLETION_2026-07-05.md`

Reviewer conversion rule: reviewer may repair review-packet formatting, GC-051 path-literal issues, closure checklist residue, or source-verification wording inside the T19 matrix and worker return before material closure. Reviewer must not silently convert T19 into runtime implementation.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

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

## Evidence Requirements

Worker return must include:

- Worker start HEAD.
- `git status --short` before and after.
- `git diff --name-status` for worker changes.
- Worker-return fast gate command and result.
- Pre-implementation autorun command and result.
- A direct statement that no runtime source, tests, checkers, hooks, session state, active handoff, public-sync files, durable-store invocation, memory/RAG write, private/generated output read, MinerU runtime, provider/live proof, stage, commit, push, or public claim occurred.

## Verification Commands

Worker must run:

```text
python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 70632c8c --head HEAD
git diff --name-status
git status --short
```

If a gate fails because of out-of-scope required edits, stop and return to orchestrator with the failure evidence.

## Acceptance Criteria

| AC | Criterion |
| --- | --- |
| AC1 | Worker creates only the T19 decision matrix and T19 worker return paths listed in this work order |
| AC2 | T19 matrix source-verifies T18 adapter payload, durable store write contract, durable persistence point, runtime actor gates, R27 prerequisites, and R24-T4 private-output policy |
| AC3 | T19 matrix selects exactly one decision disposition: future T20 invocation implementation candidate, hold pending missing authority, or blocked with source-backed reason |
| AC4 | T19 keeps actual durable-store invocation and memory/RAG write unauthorized by T19 decision-only scope |
| AC5 | Worker return reports changed files, source verification summary, selected decision, gates, and claim boundary |
| AC6 | Worker runs the worker-return fast gate and pre-implementation autorun gate for the T19 changed range |
| AC7 | Worker leaves changes unstaged and uncommitted for reviewer closure conversion |

## Review Gate

Reviewer must verify:

- Changed files are limited to T19 matrix and T19 worker return before material closure.
- Matrix source verification is source-backed and does not cite provider-specific memory as authority.
- Decision disposition is exactly one of the allowed T19 choices.
- Actual invocation and memory/RAG write remain unauthorized in T19.
- Worker did not commit.
- Worker-return fast gate and pre-implementation autorun evidence are present.
- Closure conversion is performed by reviewer if the worker return is accepted.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Local repository authoring through shell and apply_patch |
| Session or invocation | 2026-07-05 T19 work-order authoring |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Get-Content`; `Test-Path`; `python governance/compat/run_adif_defect_resolver.py`; `python governance/compat/build_dispatch_packet_scaffold.py`; `python governance/compat/run_agent_autorun_workflow_gate.py`; `apply_patch` |
| Target paths | T19 GC-018 baseline and T19 work order |
| Allowed scope source | Operator request for fresh MSEA-R28-T19 GC-018/source-verified work order |
| Before status evidence | HEAD `70632c8c`; clean worktree before T19 authoring confirmed by `git status --short` |
| After status evidence | Two untracked dispatch artifacts before commit |
| Diff evidence | `git diff --name-status` to be recorded before dispatch commit |
| Approval boundary | Approval policy never; no external approval requested; no runtime/provider/live/public action authorized |
| Claim boundary | Dispatch authoring only; no worker execution, durable-store invocation, memory write, provider proof, public-sync, or production-readiness claim |
| Agent type | Codex dispatcher |
| Invocation ID | T19-dispatch-authoring-2026-07-05 |
| Expected manifest | T19 GC-018 baseline and T19 work order |
| Actual changed set | T19 GC-018 baseline and T19 work order |
| Manifest delta | None |

## Closure Checklist

- [x] GC-018 baseline exists.
- [x] Source Verification Block exists in dispatch.
- [x] ADIF Defect Registry Disclosure exists in dispatch.
- [x] Agent Handoff Contract Control Block exists in dispatch.
- [x] Reviewer Closure Conversion exists in dispatch.
- [x] Worker Return Packet Shape Contract exists in dispatch.
- [x] External Knowledge Intake Routing exists in dispatch.
- [x] Public Export Disposition exists in dispatch.
- [x] Foundation Storage Layout Block exists in dispatch.
- [x] T19 is docs-only and no-commit by worker.

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
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT for runtime execution claims; dispatch work order source verification only |
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

Reason: T19 is private provenance governance work. No public-sync artifact or public catalog claim is authorized by this work order.

## Claim Boundary

This work order authorizes only T19 source-verified decision artifacts. It does not authorize durable-store invocation, durable-memory persistence, memory/RAG write, private/generated output reads, runtime source changes, public-sync, provider/live proof, or any production-readiness claim.
