# CVF GC-018 Baseline - MSEA R28 T23 MinerU Production Memory RAG Route Release Authority Decision

Memory class: governed-baseline

Status: DISPATCH_READY

Created: 2026-07-05

rawMemoryReleased: false

## Dispatch Prompt Envelope

dispatchId: MSEA-R28-T23-MINERU-PRODUCTION-MEMORY-RAG-ROUTE-RELEASE-AUTHORITY-DECISION

route: WORKER_MUST_NOT_COMMIT

taskClass: Work-order authoring / dispatch

rolePattern: dispatcher-authored source-verified decision work order to single no-commit docs-only worker, then reviewer closure conversion

dispatchBaseHead: `15f61130a`

workerAllowedPaths:

- `docs/reference/CVF_MSEA_R28_T23_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T23_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`

workerForbiddenPathsAndActions:

- no source, test, runtime, checker, hook, session, handoff, public-sync, IDE, provider-local, root barrel, durable-store source, runtime hierarchy source, or prior T20-T22 artifact edits;
- no production memory/RAG route release, production durable-store invocation, file-backed production persistence, vectorization, retrieval, MinerU runtime execution, private/generated output content read, Candidate Group A import, provider/live proof, public claim, Web/UI, standalone app, legal/use-case deep dive, extraction-accuracy claim, document-truth claim, legal-quality claim, current-law correctness claim, or workflow-chain production-readiness claim;
- no worker stage, commit, push, or public-sync.

expectedWorkerDisposition:

- Worker creates a source-verified T23 decision matrix and worker return only.
- Worker selects exactly one next-route disposition:
  - `T24_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_WORK_ORDER_AUTHORING_READY`
  - `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_AUTHORITY_GAP`
  - `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_BLOCKED_WITH_REASON`
- T23 itself does not release production memory/RAG route behavior, production durable-store invocation, file-backed persistence, retrieval, vectorization, private-output handling, or public claims.

## Purpose

Establish the GC-018 dispatch baseline for a bounded T23 decision worker that
can decide whether accepted T22 bounded helper/test evidence is sufficient to
open a later production memory/RAG route-release implementation packet.

T23 is an authority decision tranche only. It may source-verify evidence,
identify gaps, and select a future route, but it must not implement production
route wiring, run MinerU, write memory, retrieve, vectorize, read private
outputs, or claim workflow-chain production readiness.

## Baseline Objective

Author the dispatch baseline for a fresh MSEA-R28-T23 no-commit worker packet
that decides whether the T22 bounded implementation-candidate helper can
support T24 work-order authoring for production memory/RAG route release.

The decision must preserve the explicit T22 hold token unless a later
source-verified implementation packet is authored and accepted. The worker may
not change runtime code or treat T23 as implementation authority.

## Evidence / Verification

| Evidence class | Verification |
| --- | --- |
| Baseline source verification | Source Verification Block cites current source, test, review, policy, session, and ADIF surfaces |
| Dispatch-quality verification | Run `python governance/compat/check_work_order_dispatch_quality.py --base 15f61130a --head HEAD --enforce` |
| Pre-dispatch verification | Run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 15f61130a --head HEAD` after final edits |
| Claim boundary | Dispatch baseline only; no worker execution, runtime, provider/live, private-output, public, production memory/RAG route, source/test edit, or production-readiness claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldTool | `governance/compat/build_dispatch_packet_scaffold.py` |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T23 --title "MinerU Production Memory RAG Route Release Authority Decision" --date 2026-07-05 --base 15f61130a --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldSource | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; passed T21/T22 packet shape |
| scaffoldReason | T23 requires source-verified dispatch artifact authoring rather than runtime/source implementation |
| manualEditsAfterScaffold | Filled T23 source verification, dependency release evidence, decision-only worker outputs, ADIF disclosure, worker-quality controls, provider-local/Pylance boundaries, handoff controls, and claim boundary |
| docOnlyNewFields | `T24_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_WORK_ORDER_AUTHORING_READY`; `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_AUTHORITY_GAP`; `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_BLOCKED_WITH_REASON`; `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T23_DECISION_ONLY`; `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| claimBoundary | Dispatch scaffold provenance only; no provider/live/public/Web/MCP/model-router/runtime behavior claim |

## Dependency Release Evidence

| Dependency | Evidence source | Release status |
| --- | --- | --- |
| T22 bounded implementation-candidate closure | `docs/reviews/CVF_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_COMPLETION_2026-07-05.md` lines 39-54, 83-96, and 224-233; material commit `62f9b9c0c` | SATISFIED_FOR_DECISION_ONLY |
| T22 bounded helper source | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` lines 1-13, 27-34, 40-64, 93-237 | SATISFIED_FOR_DECISION_ONLY |
| T22 focused test evidence | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-memory-rag-route-release.test.ts` lines 83-121, 125-183, 199-307, and 326-340 | SATISFIED_FOR_DECISION_ONLY |
| T21 authority decision selected T22 candidate | `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md` lines 91-112 and 135-148 | SATISFIED |
| T20 durable-store invocation helper remains bounded | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` lines 1-10, 30-31, 105-187, and 392 | SATISFIED_FOR_DELEGATION_EVIDENCE |
| Durable store production file-backed surface exists but was not authorized by T22 | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` lines 100-110 and 415-450 | SATISFIED_FOR_GAP_DECISION |
| R27 scan-to-memory prerequisites | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` lines 86-87 and 123 | SATISFIED_FOR_GATE_CRITERIA |
| R24-T4 private-output policy | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` lines 54, 64, and 89 | SATISFIED_FOR_PRIVACY_BOUNDARY |
| ADIF worker-output hardening | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0024.md` lines 70-84 and 113-118 | SATISFIED_FOR_DISPATCH_CONTROLS |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Source Verification Block; New Doc-Only Fields; Negative Search And Collision Discipline; Evidence Reuse And Encoding Plan; Worker Output Quality Controls; Provider-Local Stray Artifact Control; Pylance Static-Analysis Diagnostic Boundary; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; External Knowledge Intake Routing; Foundation Storage Layout Block |
| gateRunPurpose | confirm T23 dispatch shape after checker source read-ahead; not first discovery |
| claimBoundary | checker read-ahead evidence only; no MinerU runtime, private-output, provider/live, public, production memory/RAG route release, source/test edit, or production-readiness claim |

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
| T22 closed only as a bounded implementation-candidate helper/test tranche and preserved production-route hold | `docs/reviews/CVF_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_COMPLETION_2026-07-05.md` | lines 39-54, 65-74, 96, 224, and 233 | `CLOSED_PASS_BOUNDED`; `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22`; `productionRouteAuthorized` | T22 completion review | VALUE_SET | ACCEPT |
| T22 helper declares bounded scope and forbids production route release, file-backed production persistence, retrieval, vectorization, MinerU runtime, private-output reads, provider/live proof, and public-sync | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 1-13 | `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` | T22 helper module header | LITERAL_INVARIANT | ACCEPT |
| T22 helper exports bounded candidate and production-hold tokens | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 27-34 | `MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTED_BOUNDED_CANDIDATE`; `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` | T22 helper constants | VALUE_SET | ACCEPT |
| T22 helper input requires explicit memory-owner authorization and adapter payload | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 40-55 | `MineruMemoryOwnerAuthorization`; `MineruMemoryRagRouteReleaseInput` | T22 helper interfaces | EXISTS | ACCEPT |
| T22 result shape hard-codes production route authorization to false | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 61-68, 78-85, and 228-236 | `productionRouteAuthorized` | `MineruMemoryRagRouteReleaseResult`; `blocked`; `releaseMineruMemoryRagRouteCandidate` | LITERAL_INVARIANT | ACCEPT |
| T22 helper fail-closes on policy, actor, provenance, actor-role, and durable-tier authorization gaps | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 101-145 | `policyDecision`; `actorAuthorized`; `provenanceScore`; `actorRole`; `targetDurableTier` | `releaseMineruMemoryRagRouteCandidate` | RUNTIME_BEHAVIOR | ACCEPT |
| T22 helper fail-closes on all five R27 prerequisites before T20 delegation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 147-183 | `r27ReceiptPrerequisite`; `r27QualityPrerequisite`; `r27SourcePointerPrerequisite`; `r27DownstreamUsePrerequisite`; `r27ClaimBoundaryPrerequisite` | `releaseMineruMemoryRagRouteCandidate` | RUNTIME_BEHAVIOR | ACCEPT |
| T22 helper fail-closes on private-output, raw-memory, reinjection, and summary-only invariant gaps before T20 delegation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 185-217 | `outputContentRead`; `rawMemoryReleased`; `canReinject`; `summaryOnly` | `releaseMineruMemoryRagRouteCandidate` | RUNTIME_BEHAVIOR | ACCEPT |
| T22 helper delegates only to the accepted T20 helper after gates pass and still returns productionRouteAuthorized false | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 219-236 | `invokeMineruDurableStoreWrite`; `productionRouteAuthorized` | `releaseMineruMemoryRagRouteCandidate` | RUNTIME_BEHAVIOR | ACCEPT |
| T22 focused tests prove bounded in-process pass cases and production-route false invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-memory-rag-route-release.test.ts` | lines 83-121 and 326-340 | `createInProcessDurableMemoryStore`; `productionRouteAuthorized`; `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` | focused Vitest suite | RUNTIME_BEHAVIOR | ACCEPT |
| T22 focused tests prove authorization, R27, and private-output fail-closed cases | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-memory-rag-route-release.test.ts` | lines 125-183, 199-257, and 261-307 | `FAIL_CLOSED_AUTHORIZATION_POLICY_DENIED`; `FAIL_CLOSED_R27_RECEIPT_MISSING`; `FAIL_CLOSED_OUTPUT_CONTENT_READ` | focused Vitest suite | RUNTIME_BEHAVIOR | ACCEPT |
| T21 selected the T22 implementation candidate while keeping route release unauthorized by T21 | `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md` | lines 91-112 and 135-148 | `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE`; `MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY` | T21 authority decision matrix | VALUE_SET | ACCEPT |
| T20 helper remains invocation-only and preserves memoryWriteAuthorized false | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 1-10, 30-31, 105-187, and 392 | `invokeMineruDurableStoreWrite`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY`; `memoryWriteAuthorized` | T20 durable-store invocation helper | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store exposes in-process and file-backed factories, but T22 did not authorize file-backed production persistence | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 100-110 and 415-450 | `createInProcessDurableMemoryStore`; `createFileBackedDurableMemoryStore`; `FileBackedDurableMemoryStore`; `writeAll` | durable memory store factories | EXISTS | ACCEPT |
| R27 requires memory-safe candidate prerequisites and a fresh memory-owner work order before memory write authorization | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 86-87 and 123 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | R27 scan-to-memory route matrix | VALUE_SET | ACCEPT |
| R24-T4 private-output policy keeps generated outputs private and limited to file name/count unless later authorized | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 54, 64, and 89 | `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT` | R24-T4 private-output policy | LITERAL_INVARIANT | ACCEPT |
| Active session state routes the next move to fresh T23 work-order authoring only and keeps production route release unauthorized until T23 packet/gates pass | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | lines 79-80, 2731, and 8194-8219 | `currentMode`; `nextAllowedMove`; `nextRecommendedMove`; `memoryRouteDisposition` | generated active session state | VALUE_SET | ACCEPT |
| ADIF-0024 requires exact command reruns, git status with untracked files, provider-local/IDE cleanup or disclosure, static-analysis disposition, and negative edge-case evidence for risky tranches | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0024.md` | lines 70-84 and 113-118 | `Worker Output Quality Controls` | ADIF entry | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| Field / token | Purpose | Runtime status |
| --- | --- | --- |
| `T24_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_WORK_ORDER_AUTHORING_READY` | possible T23 decision result selecting future T24 implementation-work-order authoring | DOC_ONLY_NEW |
| `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_AUTHORITY_GAP` | possible T23 decision result holding production route release for a named gap | DOC_ONLY_NEW |
| `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_BLOCKED_WITH_REASON` | possible T23 decision result blocking the route for a named source or authority contradiction | DOC_ONLY_NEW |
| `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T23_DECISION_ONLY` | T23 hold token preserving no production route release | DOC_ONLY_NEW |
| `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` | worker-return blocker token for provider-local artifact leakage | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence |
| --- | --- |
| Search roots | `docs/baselines`; `docs/work_orders`; `docs/reference`; `docs/reviews`; `CVF_SESSION`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests` |
| Search command or query | `Test-Path` for planned T23 artifact paths; `rg -n` for source tokens cited in Source Verification |
| Planned T23 baseline path | Before-authoring Test-Path result: COLLISION_FREE |
| Planned T23 work-order path | Before-authoring Test-Path result: COLLISION_FREE |
| Planned T23 matrix path | Before-authoring Test-Path result: COLLISION_FREE |
| Planned T23 worker-return path | Before-authoring Test-Path result: COLLISION_FREE |
| `MSEA` same-token collision result | Token occurrence is expected across governed roadmap/work-order/review names; non-authoritative for any missing source claim |
| `RAG` same-token collision result | Token occurrence is expected across memory route doctrine; non-authoritative for any missing source claim |
| `MinerU` same-token collision result | Token occurrence is expected across the active MinerU roadmap chain; non-authoritative for any missing source claim |
| T23 decision tokens | Expected only in the paired T23 dispatch artifacts before worker execution; doc-only proposed tokens, non-authoritative for runtime/source facts |
| source-not-found selected disposition | Allowed only as a future worker selected disposition if source verification genuinely fails; not used as a current source-verification disposition in this baseline |
| Collision handling | If any planned worker output path exists at execution start, worker must stop and return to orchestrator |

## Evidence Reuse And Encoding Plan

| Field | Value |
| --- | --- |
| priorEvidenceReuse | T22/T21/T20 accepted artifacts are reused only as dependency and decision evidence; runtime source remains preferred where source exists |
| commandEvidenceReuse | Previous PASS results may be cited as predecessor evidence only; T23 worker must rerun required worker-return and pre-implementation gates after final edits |
| sourceLineEncoding | Source Verification rows cite file paths, symbols, and line anchors; no private/generated content is quoted or imported |
| generatedOutputHandling | Private/generated MinerU output content remains unread and unreleased |
| workerReturnEncoding | Worker return must use scalar dispositions, command summaries, changed-file manifests, and exact no-commit status |
| staleEvidencePrevention | Worker must rerun final commands after the last material edit and record current `git status --short --untracked-files=all` |

## Worker Output Quality Controls

rawMemoryReleased=false. This baseline does not release raw memory, retrieval,
reinjection, private-output content, production route release, or memory/RAG
write behavior.

The paired work order must require the no-commit worker to complete and record
this self-audit before `COMPLETE_PENDING_REVIEW`:

- rerun every exact required command after the last material edit;
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
- include negative or edge-case decision rows for production route release,
  file-backed persistence, private output, R27 prerequisites, memory-write,
  provider-local files, and unsafe source/test edit requests.

## Provider-Local Stray Artifact Control

| Condition | Required handling |
| --- | --- |
| Pre-existing `.qwen/settings.json` | Treat as provider-local local state; do not read as CVF authority, edit, stage, commit, or cite as source evidence |
| New provider-local files | Forbidden unless a fresh work order authorizes them |
| Provider/model switching side effect | If switching providers/models creates a side-channel file, remove it if safe before handoff or return `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` with exact path and no clean workspace claim |
| Final evidence | Worker return must include `git status --short --untracked-files=all` and an ignored-aware provider-local scan for `.qwen` and `.vscode` |

## Pylance Static-Analysis Diagnostic Boundary

| Condition | Required handling |
| --- | --- |
| Python test import diagnostic | Treat as an existing static-analysis path issue from dynamic `sys.path.insert` before import |
| T23 allowed action | Record the diagnostic disposition if encountered |
| T23 forbidden action | Do not edit Python source/tests, `.vscode/settings.json`, `pyrightconfig.json`, provider-local files, or IDE config to silence Pylance |

## Acceptance Criteria

| ID | Criteria |
| --- | --- |
| AC1 | Worker creates only the T23 decision matrix and T23 worker return paths listed in this baseline |
| AC2 | Worker source-verifies T22 helper/test/completion evidence, T21 decision, T20 helper, durable-store factory boundary, R27 prerequisites, R24-T4 private-output policy, ADIF-0024, and relevant checker read-ahead |
| AC3 | Worker selects exactly one next-route disposition and explains release or hold criteria without implementing production route wiring |
| AC4 | Worker states `PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T23_DECISION_ONLY` unless reviewer later accepts a separate implementation packet |
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
| baseHeadFor(phase) | `dispatchBaseHead=15f61130a`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this baseline and paired T23 work order; worker changes are limited to T23 decision matrix and T23 worker return |
| traceScope(phase, actor) | dispatcher records source verification, ADIF, checker read-ahead, worker-quality controls, provider-local and static-analysis boundaries; worker records decision evidence, command reruns, changed files, no-commit status, and workspace hygiene; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher may commit dispatch artifacts; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns continuity commit if required |
| crossBatchIsolation | T23 must not modify T20/T21/T22 artifacts, source/tests, durable store source, runtime hierarchy source, session state, handoff, public-sync, provider-local files, IDE config, checker/hook files, or future T24 artifacts |
| nextMoveSurfaces | unchanged by worker; reviewer updates next-move surfaces only if T23 is accepted and a new mode/next move is opened |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R28_T23_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-05.md`

reviewerOwnedClosurePaths:

- `docs/reference/CVF_MSEA_R28_T23_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T23_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T23_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-05.md`

Reviewer conversion rule: reviewer may repair the T23 matrix and worker return
inside the decision-only scope before material closure. Reviewer must not
convert T23 into production route wiring, production durable-store invocation,
file-backed persistence, private-output content handling, provider/live proof,
public sync, source/test implementation, or production-readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T23 dispatch artifacts are private provenance governance material. No
public artifact, public-sync remote, public commit, or public catalog claim is
authorized by this baseline.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 chain -> T20 invocation helper -> T21 route release decision -> T22 implementation candidate -> T23 production route authority decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T23 decision matrix and worker return |
| Disposition | No external knowledge is required or authorized for T23 |
| Claim boundary | External claims do not authorize MinerU runtime, private-output read, production memory/RAG write, public claims, provider/live proof, or route wiring |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | T23 docs-only production memory/RAG route release authority decision dispatch |
| claimDisposition | CLAIM_REJECTED for execution-control, interception, provider, public, production workflow-chain, production memory/RAG route release, and source/test implementation claims |
| receiptEvidence | N/A with reason: dispatch creates no durable-store or runtime receipt |
| actionEvidence | N/A with reason: dispatch executes no durable-store, runtime, provider, public, retrieval, vectorization, or memory action |
| invocationBoundary | No MinerU runtime, provider, MCP, browser, public, file-backed production store, vectorization, retrieval, or production memory/RAG route invocation is authorized |
| interceptionBoundary | No live interception, enforcement wrapper, runtime route, or production agent control is claimed |
| claimLanguage | Use bounded docs-only authority decision language |
| forbiddenExpansion | Do not expand T23 into private-output content handling, provider/live proof, public-sync, Web/UI, production storage, production memory/RAG route release, retrieval, vectorization, source/test implementation, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage surface touched | Governed docs dispatch artifacts only |
| Durable store invoked | No |
| Foundation storage claim | T23 dispatch creates no runtime storage, memory record, vector index, retrieval store, file-backed production persistence, or durable-store receipt |
| Layout disposition | T23 worker outputs remain in reference and review artifacts; no source/runtime storage layout mutation is authorized |

## Claim Boundary

This baseline authorizes only a docs-only T23 decision worker packet. It does
not authorize actual production memory/RAG route release, production durable
store invocation, file-backed production persistence, vectorization, retrieval,
MinerU runtime execution, private/generated content read, Candidate Group A
import, provider/live proof, public-sync, Web/UI, standalone app work,
legal/use-case deep dive, extraction accuracy, document truth, legal quality,
current-law correctness, workflow-chain production readiness, worker stage,
worker commit, or push.
