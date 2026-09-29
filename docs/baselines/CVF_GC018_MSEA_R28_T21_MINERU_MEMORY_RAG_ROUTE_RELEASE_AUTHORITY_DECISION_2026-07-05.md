# CVF GC-018 Baseline - MSEA R28 T21 MinerU Memory RAG Route Release Authority Decision

Memory class: governed-baseline

Status: DISPATCH_READY

Created: 2026-07-05

rawMemoryReleased: false

## Dispatch Prompt Envelope

dispatchId: MSEA-R28-T21-MINERU-MEMORY-RAG-ROUTE-RELEASE-AUTHORITY-DECISION

route: WORKER_MUST_NOT_COMMIT

taskClass: Work-order authoring / dispatch

rolePattern: dispatcher-authored source-verified decision work order to single no-commit docs-only worker, then reviewer closure conversion

dispatchBaseHead: `4c184edb6`

workerAllowedPaths:

- `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`

workerForbiddenPathsAndActions:

- no source, test, runtime, checker, hook, session, handoff, public-sync, IDE, provider-local, root barrel, durable-store source, runtime hierarchy source, or Python source/test edits;
- no actual memory/RAG route release, production durable-store invocation, file-backed production persistence, vectorization, retrieval, MinerU runtime execution, private/generated output content read, Candidate Group A import, provider/live proof, public claim, Web/UI, standalone app, legal/use-case deep dive, extraction-accuracy claim, document-truth claim, legal-quality claim, current-law correctness claim, or workflow-chain production-readiness claim;
- no worker stage, commit, push, or public-sync.

expectedWorkerDisposition:

- Worker creates a source-verified T21 decision matrix and worker return only.
- Worker selects exactly one next-route disposition:
  - `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE`
  - `MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_GAP`
  - `BLOCKED_SOURCE_NOT_FOUND`
- T21 itself does not release actual memory/RAG writes or route wiring.

## Purpose

Establish the GC-018 dispatch baseline for a bounded T21 decision worker that
can select or hold a future MinerU memory/RAG route release implementation
candidate without performing route release itself.

## Baseline Objective

Author the dispatch baseline for a fresh MSEA-R28-T21 no-commit worker packet
that decides whether the accepted T20 bounded helper/test evidence is sufficient
to select a later implementation candidate for MinerU memory/RAG route release.

The decision must remain source-verified and docs-only. It may map evidence and
select a future route, but it must not implement route wiring, write memory,
perform retrieval/vectorization, or read private/generated MinerU output
content.

## Evidence / Verification

| Evidence class | Verification |
| --- | --- |
| Baseline source verification | Source Verification Block cites current source, test, review, policy, and ADIF surfaces |
| Dispatch-quality verification | Run `python governance/compat/check_work_order_dispatch_quality.py --base 4c184edb6 --head HEAD --enforce` |
| Pre-dispatch verification | Run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 4c184edb6 --head HEAD` after final edits |
| Claim boundary | Dispatch baseline only; no worker execution, runtime, provider/live, private-output, public, memory/RAG route, source/test edit, or production claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldTool | manual scaffold from current GC-018/work-order template and passed T20 packet shape |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T21 --title "MinerU Memory RAG Route Release Authority Decision" --date 2026-07-05 --base 4c184edb6 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldSource | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; T20 dispatch baseline/work order |
| scaffoldReason | T21 requires source-verified dispatch artifact authoring rather than runtime/source implementation |
| manualEditsAfterScaffold | Filled T21 source verification, ADIF-0024 disclosure, worker-output quality controls, provider-local/Pylance boundaries, handoff controls, and claim boundary |
| docOnlyNewFields | `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE`; `MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_GAP`; `MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY`; `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| claimBoundary | Dispatch scaffold provenance only; no provider/live/public/Web/MCP/model-router/runtime behavior claim |

## Dependency Release Evidence

| Dependency | Evidence source | Release status |
| --- | --- | --- |
| T20 bounded helper/test invocation closure | `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_COMPLETION_2026-07-05.md` lines 37-48 and 205 | SATISFIED_FOR_DECISION_ONLY |
| T20 worker return provider-local and Pylance boundaries | `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md` lines 168-186 | SATISFIED_FOR_DECISION_ONLY |
| T19 selected T20 invocation implementation candidate | `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md` lines 66-72 and 87-89 | SATISFIED |
| T18 adapter candidate exists and remains metadata-only | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` lines 779-953 | SATISFIED |
| T17 authority decision criteria exist | `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` lines 43-57 | SATISFIED |
| R27 scan-to-memory prerequisites | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` lines 77-87 | SATISFIED_FOR_GATE_CRITERIA |
| R24-T4 private-output policy | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` lines 54-64 and 212 | SATISFIED_FOR_PRIVACY_BOUNDARY |
| ADIF worker-output hardening | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0024.md` lines 70-84 and 113-118 | SATISFIED_FOR_DISPATCH_CONTROLS |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Source Verification Block; New Doc-Only Fields; Worker Output Quality Controls; Provider-Local Stray Artifact Control; Pylance Static-Analysis Diagnostic Boundary; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirm T21 dispatch shape after checker source read-ahead; not first discovery |
| claimBoundary | checker read-ahead evidence only; no MinerU runtime, private-output, provider/live, public, memory/RAG route, source/test edit, or production claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001
- ADIF-0002
- ADIF-0014
- ADIF-0015
- ADIF-0020
- ADIF-0021
- ADIF-0007
- ADIF-0016
- ADIF-0017
- ADIF-0024

Disclosure count: 10

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T20 closed as bounded helper/test invocation only and kept memory/RAG route release held | `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_COMPLETION_2026-07-05.md` | lines 37-48 and 205 | `CLOSED_PASS_BOUNDED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY`; `fresh T21 authority decision` | T20 completion review | VALUE_SET | ACCEPT |
| T20 helper result returns a bounded durable-store receipt inside the helper result shape | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 66-75 and 392-398 | `durableStoreReceipt` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
| T20 helper result keeps memory-write authorization disabled in the returned result shape | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 69 and 392 | `memoryWriteAuthorized` | `invokeMineruDurableStoreWrite` | LITERAL_INVARIANT | ACCEPT |
| T20 helper rejects output-content read before store invocation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 111-123 | `outputContentRead` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
| T20 helper rejects raw memory release before store invocation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 127-139 | `rawMemoryReleased` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
| T20 helper rejects reinjection before store invocation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 143-155 | `canReinject` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
| T20 helper rejects non-summary-only payloads before store invocation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 159-171 | `summaryOnly` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
| T20 focused tests cover allowed in-process invocation, denial preservation, R27 prerequisite fail-closed cases, unsafe metadata fail-closed cases, and memory-write false invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-durable-store-invocation.test.ts` | lines 51-68, 112-145, 169-215, 223-253, 308-348 | `invokeMineruDurableStoreWrite`; `memoryWriteAuthorized`; `rawMemoryReleased`; `R27_PREREQUISITE_MISSING` | focused Vitest suite | EXISTS | ACCEPT |
| Durable store write input requires policy decision and actor authorization fields | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 and 201 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized` | durable memory store contract | EXISTS | ACCEPT |
| Durable store rejects raw payload and low provenance before authorized writes | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-145, 257-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `raw_memory_payload_rejected`; `low_provenance_score` | durable memory store write path | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store exposes file-backed persistence, but T21 does not authorize production file-backed persistence | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 100-106 and 415-450 | `createInProcessDurableMemoryStore`; `createFileBackedDurableMemoryStore`; `FileBackedDurableMemoryStore`; `writeAll` | durable memory store factories | EXISTS | ACCEPT |
| Runtime memory hierarchy limits durable write actors and denies actors not allowed for a tier | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 174-204 and 273-275 | `allowedActors`; `durablePersistenceAllowed`; `actor_not_allowed_for_memory_tier` | `evaluateRuntimeMemoryAction` | VALUE_SET | ACCEPT |
| T18 adapter builder fail-closes on unsafe output-content, memory-write authorization, policy, actor, provenance, actor-role/tier, and R27 prerequisite gaps | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 779-917 | `build_mineru_durable_memory_write_adapter_candidate`; `OUTPUT_CONTENT_READ_FORBIDDEN`; `MEMORY_WRITE_ALREADY_AUTHORIZED`; `R27_PREREQUISITE_MISSING` | MinerU metadata receipt writer | RUNTIME_BEHAVIOR | ACCEPT |
| T18 adapter payload renders metadata-only fields and carries R27 prerequisites, summary-only, no reinjection, no raw-memory release, and no output-content read | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 928-953 | `mineru_durable_memory_write_adapter_candidate_payload`; `r27ReceiptPrerequisite`; `summaryOnly`; `canReinject`; `rawMemoryReleased`; `outputContentRead` | MinerU metadata receipt writer | EXISTS | ACCEPT |
| Python focused test import warning is an existing static-analysis path issue using dynamic `sys.path.insert`, not a T21 source-edit authorization | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 11-13 | `sys.path.insert`; `from mineru_metadata_receipt_writer import` | Python focused test | EXISTS | ACCEPT |
| R27 memory/RAG route requires receipt, quality, source pointer, downstream-use status, and claim boundary before memory write authorization | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 77-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | R27 scan-to-memory route matrix | VALUE_SET | ACCEPT |
| R24-T4 policy keeps private/generated output content out of successor routing unless separately authorized | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 54-64 and 212 | `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT`; policy claim boundary | R24-T4 private-output policy | LITERAL_INVARIANT | ACCEPT |
| ADIF-0024 requires exact command reruns, git status with untracked files, provider-local/IDE cleanup or disclosure, static-analysis disposition, and negative edge-case tests for risky tranches | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0024.md` | lines 70-84 and 113-118 | `Worker Output Quality Controls` | ADIF entry | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| Field / token | Purpose | Runtime status |
| --- | --- | --- |
| `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE` | possible T21 decision result selecting a future implementation packet | DOC_ONLY_NEW |
| `MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_GAP` | possible T21 decision result holding route release for a named gap | DOC_ONLY_NEW |
| `MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY` | T21 hold token preserving no actual route release | DOC_ONLY_NEW |
| `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` | worker-return blocker token for provider-local artifact leakage | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence |
| --- | --- |
| Search roots | `docs/baselines`; `docs/work_orders`; `docs/reference`; `docs/reviews`; `CVF_SESSION/state`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests` |
| Search command or query | `Test-Path` for planned T21 artifact paths; `rg --files` for T21 artifact-name collisions; source-token search by `rg -n` for named symbols cited in Source Verification |
| Coverage | source, tests, docs, JSON state entries, and governed external-evidence summaries cited by the T21 packet |
| Planned T21 baseline path | Before-authoring path check returned false |
| Planned T21 work-order path | Before-authoring path check returned false |
| Planned T21 matrix path | Before-authoring path check returned false |
| Planned T21 worker-return path | Before-authoring path check returned false |
| `MSEA` same-token collision result | Token occurrence is expected across governed roadmap/work-order/review names; non-authoritative for any missing source claim |
| `RAG` same-token collision result | Token occurrence is expected across memory route doctrine; non-authoritative for any missing source claim |
| `GC` same-token collision result | Token occurrence is expected across governed GC-018 dispatch artifacts; non-authoritative for any missing source claim |
| `MinerU` same-token collision result | Token occurrence is expected across the active MinerU roadmap chain; non-authoritative for any missing source claim |
| `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE` same-token collision result | Token occurrence is expected in the paired T21 dispatch artifacts; doc-only proposed token, non-authoritative for existing runtime source |
| `MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_GAP` same-token collision result | Token occurrence is expected in the paired T21 dispatch artifacts; doc-only proposed token, non-authoritative for existing runtime source |
| `MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY` same-token collision result | Token occurrence is expected in the paired T21 dispatch artifacts; doc-only proposed token, non-authoritative for existing runtime source |
| `RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026` same-token collision result | Token occurrence is expected as a filename stem in the paired T21 dispatch artifacts; non-authoritative for runtime/source facts |
| `BLOCKED_SOURCE_NOT_FOUND` usage | Allowed only as a future worker selected disposition if source verification genuinely fails; not used as a current source-verification disposition in this baseline |
| Absent-versus-collision disposition | Path absence is checked only for exact planned T21 artifact paths; token collisions are recorded as not binding unless tied to a cited source row |
| Collision handling | If any planned worker output path exists at execution start, worker must stop and return to orchestrator |

## Worker Output Quality Controls

rawMemoryReleased=false. This baseline does not release raw memory, retrieval,
reinjection, private-output content, or memory/RAG write behavior.

The paired work order must require the no-commit worker to complete and record
this self-audit before `COMPLETE_PENDING_REVIEW`:

- rerun every exact required command after the last material edit, including
  worker-return gates named by the work order;
- copy each required command exactly as run, with working directory;
- classify each final command result as PASS, FAIL with allowed-scope repair
  completed and rerun, BLOCKED with reason, or N/A with reason;
- record `git status --short --untracked-files=all` after the worker-return
  file exists;
- remove or disclose any provider-local or IDE side-channel file before
  handoff, and do not stage or claim such files unless this work order
  explicitly authorizes them;
- record any static-analysis diagnostic as fixed inside Allowed scope or as
  out-of-scope with no source/test edit claim;
- include at least one negative or edge-case decision-row test for private
  output, memory-write, route-release, security, or unsafe-normalization
  surfaces, because T21 touches route-release authority.

## Provider-Local Stray Artifact Control

| Condition | Required handling |
| --- | --- |
| Pre-existing `.qwen/settings.json` | Treat as provider-local local state; do not read as CVF authority, edit, stage, commit, or cite as source evidence |
| New provider-local files | Forbidden unless a fresh work order authorizes them |
| Final evidence | Worker return must include `git status --short --untracked-files=all` and an ignored-aware provider-local scan for `.qwen` and `.vscode` |
| Blocker token | If provider/model switching creates an unremovable or uncertain provider-local file, return `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` with exact path and no clean-worktree claim |

## Pylance Static-Analysis Diagnostic Boundary

| Condition | Required handling |
| --- | --- |
| Python test import diagnostic | Treat as existing static-analysis path issue from dynamic `sys.path.insert` before import |
| T21 allowed action | Record the diagnostic disposition if encountered |
| T21 forbidden action | Do not edit Python source/tests, `.vscode/settings.json`, `pyrightconfig.json`, provider-local files, or IDE config to silence Pylance |

## Acceptance Criteria

| ID | Criteria |
| --- | --- |
| AC1 | Worker creates only the T21 decision matrix and T21 worker return paths listed in this baseline |
| AC2 | Worker source-verifies T20 helper/test/completion evidence, T19 matrix, T18 adapter, T17 criteria, R27 prerequisites, R24-T4 private-output policy, ADIF-0024, and relevant checker read-ahead |
| AC3 | Worker selects exactly one next-route disposition and explains release or hold criteria without implementing route wiring |
| AC4 | Worker states `MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY` unless reviewer later accepts a separate implementation packet |
| AC5 | Worker includes Worker Output Quality Controls evidence, provider-local/IDE side-channel cleanup or disclosure, Pylance/static-analysis disposition, and negative edge-case decision rows |
| AC6 | Worker records command evidence for worker-return fast gate, pre-implementation autorun, `git diff --name-status`, `git status --short --untracked-files=all`, and ignored-aware provider-local scan |
| AC7 | Worker does not run MinerU runtime, provider/live proof, private/generated output content read, vectorization, retrieval, file-backed production persistence, public-sync, Web/UI, legal/use-case work, stage, commit, or push |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored work order to single no-commit docs-only decision worker, then reviewer closure conversion |
| phase | dispatch |
| baseHeadFor(phase) | `dispatchBaseHead=4c184edb6`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this baseline and paired T21 work order; worker changes are limited to T21 decision matrix and T21 worker return |
| traceScope(phase, actor) | dispatcher records source verification, ADIF, checker read-ahead, worker-quality controls, provider-local and static-analysis boundaries; worker records decision evidence, command reruns, changed files, no-commit status, and workspace hygiene; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher may commit dispatch artifacts; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns continuity commit if required |
| crossBatchIsolation | T21 must not modify T17/T18/T19/T20 artifacts, source/tests, durable store source, runtime hierarchy source, session state, handoff, public-sync, provider-local files, IDE config, checker/hook files, or future T22 artifacts |
| nextMoveSurfaces | unchanged by worker; reviewer updates next-move surfaces only if T21 is accepted and a new mode/next move is opened |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-05.md`

reviewerOwnedClosurePaths:

- `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`

Reviewer conversion rule: reviewer may repair the T21 matrix and worker return
inside the decision-only scope before material closure. Reviewer must not
convert T21 into route wiring, memory/RAG writes, file-backed persistence,
private-output content handling, provider/live proof, public sync, source/test
implementation, or production-readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T21 dispatch artifacts are private provenance governance material. No
public artifact, public-sync remote, public commit, or public catalog claim is
authorized by this baseline.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map citation | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Chain map | MSEA-R28-T21 is a local source-governed decision tranche |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | Route as advisory input only; require local source verification before inclusion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T21 decision matrix and worker return |
| Disposition | No external knowledge is required or authorized for T21 |
| Claim boundary | External claims do not authorize MinerU runtime, private-output read, memory/RAG write, public claims, provider/live proof, or route wiring |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | T21 docs-only memory/RAG route release authority decision dispatch |
| claimDisposition | CLAIM_REJECTED for execution-control, interception, provider, public, production workflow-chain, memory/RAG route release, and source/test implementation claims |
| receiptEvidence | N/A with reason: dispatch creates no durable-store or runtime receipt |
| actionEvidence | N/A with reason: dispatch executes no durable-store, runtime, provider, public, retrieval, vectorization, or memory action |
| invocationBoundary | No MinerU runtime, provider, MCP, browser, public, file-backed production store, vectorization, retrieval, or memory/RAG route invocation is authorized |
| interceptionBoundary | No live interception, enforcement wrapper, runtime route, or production agent control is claimed |
| claimLanguage | Use bounded docs-only authority decision language |
| forbiddenExpansion | Do not expand T21 into private-output content handling, provider/live proof, public-sync, Web/UI, production storage, memory/RAG route release, retrieval, vectorization, source/test implementation, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage surface touched | Governed docs dispatch artifacts only |
| Durable store invoked | No |
| Foundation storage claim | T21 dispatch creates no runtime storage, memory record, vector index, retrieval store, file-backed production persistence, or durable-store receipt |
| Layout disposition | T21 worker outputs remain in `docs/reference` and `docs/reviews`; no source/runtime storage layout mutation is authorized |

## Claim Boundary

This baseline authorizes only a docs-only T21 decision worker packet. It does
not authorize actual memory/RAG route release, production durable-store
invocation, file-backed production persistence, vectorization, retrieval,
MinerU runtime execution, private/generated content read, Candidate Group A
import, provider/live proof, public-sync, Web/UI, standalone app work,
legal/use-case deep dive, extraction accuracy, document truth, legal quality,
current-law correctness, workflow-chain production readiness, worker stage,
worker commit, or push.
