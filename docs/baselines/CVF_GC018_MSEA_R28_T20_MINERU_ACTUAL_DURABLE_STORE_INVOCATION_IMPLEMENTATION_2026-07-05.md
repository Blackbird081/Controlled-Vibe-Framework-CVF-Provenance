# CVF GC-018 Baseline - MSEA R28 T20 MinerU Actual Durable Store Invocation Implementation

Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Date: 2026-07-05
Batch ID: MSEA-R28-T20-MINERU-ACTUAL-DURABLE-STORE-INVOCATION-IMPLEMENTATION
Dispatch base head: d59fbdb3e
Commit mode: WORKER_MUST_NOT_COMMIT
Worker role: implementation worker
Reviewer role: reviewer/closer
rawMemoryReleased: false

## Purpose

This baseline opens MSEA-R28-T20 as a source-verified implementation tranche
for a bounded MinerU durable-store invocation helper. T20 may create a Learning
Plane Foundation helper that consumes the accepted T18 adapter payload shape,
maps it into the existing `DurableMemoryStore.write` input contract, invokes an
in-process durable memory store in focused tests, and captures the durable
store receipt.

T20 does not authorize MinerU runtime execution, private/generated output
content reads, Candidate Group A import, provider/live proof, public-sync,
Web/UI/dashboard work, memory/RAG route release, vectorization, retrieval,
Learning Plane runtime route wiring, file-backed production storage, standalone
app work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production readiness, worker
commit, or push.

## Decision Baseline

| Item | Baseline decision |
| --- | --- |
| T20 scope | Source/test implementation of a bounded durable-store invocation helper plus worker return |
| Implementation surface | New Learning Plane Foundation helper and focused tests |
| Invocation mode | In-process durable store invocation for deterministic local tests only |
| Memory/RAG route status | HELD beyond T20 |
| Private/generated output status | HELD; metadata-only adapter payload may be consumed, generated output content may not be read |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closure authority | Reviewer may repair/accept T20 source/test/worker-return artifacts, then commit material closure |
| Public export disposition | DEFERRED_PRIVATE_ONLY |

## Scope / Target / Owner Boundary

Allowed worker changes:

- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts`;
- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-durable-store-invocation.test.ts`;
- create `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`;
- implement a deterministic helper that accepts the T18 adapter payload shape,
  verifies the T19 prerequisites, calls `DurableMemoryStore.write`, and returns
  the durable write receipt plus bounded metadata;
- run focused Vitest, TypeScript check if feasible, worker-return fast gate,
  and pre-implementation autorun.

Forbidden worker changes or claims:

- do not edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- do not edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`;
- do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`;
- do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` unless reviewer later opens a separate export-surface packet;
- do not edit session front doors, generated session state, active handoff,
  root agent instruction files, checkers, hooks, public-sync files,
  dashboard/Web/UI, or model-router surfaces;
- do not run MinerU runtime, read private/generated MinerU output content,
  import Candidate Group A, run provider/live proof, vectorize, retrieve, write
  a memory/RAG route, create production file-backed storage evidence, run a
  standalone PDF app, make public claims, stage, commit, or push.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| T19 material closure | `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`, material commit `dc687360` | ACCEPT |
| T19 selected T20 route | `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md` lines 66-72 selected `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE` | ACCEPT |
| T19 held memory/RAG write | `CVF_SESSION/state/entries/mseaR28T19MineruDurableStoreInvocationReleaseDecisionClosure20260705.json` lines 17-20 keep `MEMORY_WRITE_NOT_AUTHORIZED_BY_T19_DECISION_ONLY` and private-output hold tokens | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `d59fbdb3e` before T20 authoring | ACCEPT |
| Planned T20 paths absent before authoring | `Test-Path` returned `False` for the planned T20 baseline, work order, and worker-return paths before authoring | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Prior tranche requirement | T20 dispatch handling |
| --- | --- |
| T19 selected future durable-store invocation implementation candidate | T20 authorizes only a bounded helper and focused tests, not production route wiring |
| T18 adapter payload must remain metadata-only and fail-closed | T20 helper must consume only the rendered adapter payload fields and reject raw/private/output-content flags |
| Durable store requires policy, actor, provenance, tier, and raw-payload gates | T20 helper must call the existing `DurableMemoryStore.write` contract without editing that store |
| Runtime memory hierarchy limits durable write actors by tier | T20 helper must preserve `actorRole` and target tier from the adapter payload so the store can deny invalid actors |
| R27 route prerequisites remain required before any memory authorization | T20 helper must require all five adapter prerequisite flags and keep memory/RAG route release held |
| R24-T4 private-output policy keeps generated content private | T20 must not read or quote private/generated output content |
| Operator noted Pylance import warning in the Python test | T20 treats this as an IDE static-analysis path issue, not a Python runtime failure; no Python test/source edit is authorized for that warning |
| Operator noted provider-local `.qwen/settings.json` stray risk | T20 adds provider-local stray artifact control and final no-stray evidence requirements |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T20 --title "MinerU Actual Durable Store Invocation Implementation" --date 2026-07-05 --base d59fbdb3e --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added T20 source verification, dependency evidence, bounded Learning Plane helper scope, Pylance diagnostic boundary, provider-local stray control, handoff contract control, worker return contract, and claim boundaries |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| docOnlyNewFields | `MineruDurableStoreInvocationInput`; `invokeMineruDurableStoreWrite`; `MINERU_DURABLE_STORE_INVOCATION_IMPLEMENTED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY`; `PROVIDER_LOCAL_STRAY_ARTIFACT_CONTROL` |
| claimBoundary | Dispatch scaffold provenance only; no provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Disclosure count: 0

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Source Verification Block; source-not-found disposition spelling; Negative Search And Collision Discipline; Evidence Reuse And Encoding Plan; Worker Return Packet Shape Contract; Public Export Disposition; External Knowledge Intake Routing; Foundation Storage Layout Block; Provider-Local Stray Artifact Control |
| gateRunPurpose | confirm T20 dispatch artifact shape after checker source read-ahead; not first discovery |
| claimBoundary | checker read-ahead evidence only; no MinerU runtime, private-output, provider/live, public, memory/RAG route, or production claim |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T19 closure selected T20 implementation candidate while keeping memory/RAG write and durable-store invocation held by T19 decision-only scope | `CVF_SESSION/state/entries/mseaR28T19MineruDurableStoreInvocationReleaseDecisionClosure20260705.json` | lines 17-20 | `selectedDecisionDisposition`; `memoryWriteDisposition`; `durableStoreInvocationDisposition`; `privateOutputDisposition` | active session generated-source entry | VALUE_SET | ACCEPT |
| T19 matrix selected the future T20 route and kept held tokens | `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md` | lines 66-72 and 87-89 | `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T19_DECISION_ONLY`; `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T19_DECISION_ONLY` | T19 decision matrix | VALUE_SET | ACCEPT |
| T19 matrix requires T20 to wire the validated adapter payload into `DurableMemoryStore.write` and capture receipt | `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md` | lines 103-105 | `DurableMemoryStore.write`; `Durable store receipt capture`; `No memory/RAG write in T20` | T19 future prerequisites | VALUE_SET | ACCEPT |
| T18 adapter payload exposes policy, actor, provenance, R27 prerequisite, privacy, summary-only, and durable-store invocation hold fields | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 928-955 | `mineru_durable_memory_write_adapter_candidate_payload`; `policyDecision`; `actorAuthorized`; `provenanceScore`; `outputContentRead`; `rawMemoryReleased`; `summaryOnly` | MinerU metadata receipt writer | EXISTS | ACCEPT |
| T18 adapter builder fail-closes on unsafe output-content, memory-write-authorized, policy, actor, provenance, actor-role/tier, and R27 prerequisites | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 779-917 | `build_mineru_durable_memory_write_adapter_candidate`; `OUTPUT_CONTENT_READ_FORBIDDEN`; `MEMORY_WRITE_ALREADY_AUTHORIZED`; `POLICY_DECISION_DENIED`; `ACTOR_NOT_AUTHORIZED`; `LOW_PROVENANCE_SCORE`; `ACTOR_ROLE_NOT_ALLOWED_FOR_TIER`; `R27_PREREQUISITE_MISSING` | MinerU metadata receipt writer | RUNTIME_BEHAVIOR | ACCEPT |
| T18 focused tests cover deterministic adapter payload and fail-closed unsafe inputs | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 787-923 | `test_durable_memory_write_adapter_candidate_is_deterministic_and_metadata_only`; `test_durable_memory_write_adapter_candidate_fails_closed_for_unsafe_inputs` | pytest suite | EXISTS | ACCEPT |
| Durable store exposes `DurableMemoryStore.write` and `DurableMemoryWriteInput` for T20 helper invocation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63, 89-90, and 195 | `DurableMemoryWriteInput`; `DurableMemoryStore`; `write` | durable memory store contract | EXISTS | ACCEPT |
| Durable store write path denies non-allow policy or unauthorized actor before persistence | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-206 | `policyDecision`; `actorAuthorized`; `durable_memory_policy_denied` | `DurableMemoryStore.write` | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store rejects invalid durable tier, invalid actor, raw payload, secrets, blocked lifecycle, and low provenance before upsert | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 208-273 | `isDurableTier`; `evaluateRuntimeMemoryAction`; `hasRawPayload`; `MIN_PROVENANCE_SCORE`; `low_provenance_score` | `DurableMemoryStore.write` | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store writes only through `upsert` and returns a summary-only receipt | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48, 173-175, 291, and 294 | `summaryOnly`; `canReinject`; `rawMemoryReleased`; `this.upsert(record)` | durable memory store receipt/write path | RUNTIME_BEHAVIOR | ACCEPT |
| In-process durable store factory exists for deterministic focused tests | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 100-103 | `createInProcessDurableMemoryStore` | durable memory store factory | EXISTS | ACCEPT |
| Runtime memory hierarchy allows skill writes by OPERATOR, GOVERNOR, BUILDER, SERVICE_AGENT and long-term writes by OPERATOR, GOVERNOR, SERVICE_AGENT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 171-201 | `allowedActors`; `durablePersistenceAllowed` | runtime memory hierarchy | VALUE_SET | ACCEPT |
| Runtime memory hierarchy denies actors not allowed for a tier | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 273-275 | `actor_not_allowed_for_memory_tier` | `evaluateRuntimeMemoryAction` | RUNTIME_BEHAVIOR | ACCEPT |
| Learning Plane package has focused Vitest and TypeScript check commands | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` | scripts section | `test`; `check`; `vitest run --config vitest.config.ts`; `tsc -p tsconfig.json --noEmit` | package scripts | EXISTS | ACCEPT |
| Python test Pylance warning is explained by dynamic `sys.path.insert` before import; pytest can use it but static analysis may not | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 6-13 | `sys.path.insert`; `from mineru_metadata_receipt_writer import` | Python focused test | EXISTS | ACCEPT |
| `.vscode/settings.json` is ignored by repo gitignore, so it is not a governed material proof path in T20 | `.gitignore` | line 20 | `.vscode/` | repository ignore policy | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| Field / token | Purpose | Runtime status |
| --- | --- | --- |
| `MineruDurableStoreInvocationInput` | proposed T20 TypeScript input interface for adapter-payload invocation helper | DOC_ONLY_NEW |
| `invokeMineruDurableStoreWrite` | proposed T20 helper that validates adapter payload and calls `DurableMemoryStore.write` | DOC_ONLY_NEW |
| `MINERU_DURABLE_STORE_INVOCATION_IMPLEMENTED` | proposed T20 helper disposition token | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY` | proposed hold token to keep memory/RAG route release outside T20 | DOC_ONLY_NEW |
| `PROVIDER_LOCAL_STRAY_ARTIFACT_CONTROL` | dispatch control label for provider-local hygiene requirements | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`
priorVerificationAnchor: `dc687360`
freshRecomputeRequired: true
recomputeReason: T20 authorizes source/test implementation, so T19 matrix, T18 adapter payload, durable store, runtime hierarchy, package scripts, Python IDE diagnostic context, and provider-local boundary evidence were rechecked at current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason
extractedTextAuthorityReason: no extracted text, private/generated output text, or document body is source authority for T20.

## Current Runtime Freshness Verification

| Check | Result |
| --- | --- |
| Dispatch base | PASS: `git rev-parse --short HEAD` returned `d59fbdb3e` before authoring |
| Worktree state | PASS: `git status --short --untracked-files=all` returned empty output before authoring |
| Existing T20 artifact collision | PASS: planned T20 baseline, work order, and worker-return paths were absent |
| T18 adapter source located | PASS |
| Durable store source located | PASS |
| Runtime hierarchy source located | PASS |
| Learning Plane package scripts located | PASS |
| Python IDE diagnostic boundary located | PASS |
| Pre-existing provider-local path | PRESENT_EXEMPTED: `.qwen/settings.json` exists locally and is ignored/excluded; worker must not edit, stage, cite as authority, or hide new provider-local output |

## Negative Search And Collision Discipline

| Token / path checked | Result |
| --- | --- |
| `MSEA_R28_T20` | No existing governed T20 artifact found before authoring |
| `MSEA-R28-T20` | Only current next-move/session references and this dispatch batch after authoring |
| `ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION` | No existing T20 worker output artifact found before authoring |
| Planned T20 baseline path | Absent before authoring |
| Planned T20 work-order path | Absent before authoring |
| Planned T20 worker-return path | Absent before authoring |

## Provider-Local Stray Artifact Control

| Rule | Required worker handling |
| --- | --- |
| Pre-existing `.qwen/settings.json` | Treat as pre-existing provider-local state; do not read as CVF authority, edit, stage, commit, or use as evidence of implementation |
| New provider-local files | Forbidden unless a fresh work order authorizes them |
| Final evidence | Worker return must include `git status --short --untracked-files=all` and an ignored-aware provider-local scan for `.qwen` and common provider-local roots |
| If provider/model switch creates files | Remove only worker-created provider-local files before return, or return `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` with exact path and no clean-worktree claim |
| Local exclude discipline | Worker must not add new `.git/info/exclude` entries or use local excludes as cleanliness evidence |

## Pylance Static-Analysis Diagnostic Boundary

| Observation | T20 handling |
| --- | --- |
| Python focused test imports `mineru_metadata_receipt_writer` after dynamic `sys.path.insert` | Treat as existing pytest runtime pattern, not a failing Python test |
| Pylance may report missing import because it does not execute dynamic path mutation | Record as IDE static-analysis path issue |
| `.vscode/settings.json` is ignored | Do not edit it in T20 as material proof |
| Allowed worker action | Do not worsen the import path; mention the diagnostic in the worker return if encountered |
| Forbidden worker action | Do not rewrite Python imports, add ignored IDE config, or create `pyrightconfig.json` inside T20 without a separate source-verified config packet |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`

Required worker-return sections:

- Purpose
- Target / Source
- Scope / Methodology
- Changed Files
- Source Verification Summary
- Findings / Position
- Risk / Corrective Action
- Tests / Gates Run
- Provider-Local Stray Artifact Control
- Pylance Static-Analysis Diagnostic Boundary
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Claim Boundary
- Return-To-Orchestrator
- No-Commit Statement

## Acceptance Criteria

| AC | Criterion |
| --- | --- |
| AC1 | Worker creates only the T20 helper source, T20 focused test, and T20 worker return paths listed in this baseline |
| AC2 | Helper consumes the T18 adapter payload shape and rejects unsafe values before calling the durable store |
| AC3 | Helper invokes an in-process `DurableMemoryStore.write` in tests and captures allowed and denied durable store receipts |
| AC4 | Helper preserves `summaryOnly: true`, `canReinject: false`, `rawMemoryReleased: false`, `outputContentRead: false`, and no raw/private content fields |
| AC5 | T20 keeps memory/RAG route release held by an explicit token and does not perform vectorization, retrieval, MinerU runtime, private-output reads, provider/live proof, public-sync, or production storage evidence |
| AC6 | Focused Vitest and package TypeScript check pass or any package-level unrelated blocker is source-bounded and reviewer-approved |
| AC7 | Worker return reports changed files, command evidence, no-commit status, provider-local no-stray evidence, and Pylance diagnostic boundary |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored work order to single no-commit implementation worker, then reviewer closure conversion |
| phase | dispatch |
| baseHeadFor(phase) | `dispatchBaseHead=d59fbdb3e`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this GC-018 baseline and paired T20 work order; worker changes are limited to T20 helper source, T20 focused test, and T20 worker return |
| traceScope(phase, actor) | dispatcher records scaffold, source verification, ADIF, checker read-ahead, Pylance boundary, and provider-local stray controls; worker records execution commands and changed files; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher may commit dispatch artifacts; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns continuity commit if required |
| crossBatchIsolation | T20 must not modify T18/T19 artifacts, Python source/tests, durable store source, runtime hierarchy source, session state, handoff, public-sync, provider-local files, or future T21 artifacts |
| nextMoveSurfaces | unchanged by worker; reviewer updates next-move surfaces only if T20 is accepted and a new mode/next move is opened |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_COMPLETION_2026-07-05.md`

reviewerOwnedClosurePaths:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-durable-store-invocation.test.ts`
- `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`

Reviewer conversion rule: reviewer may repair T20 helper/test/worker-return
formatting and allowed source/test defects before material closure. Reviewer
must not convert T20 into production route wiring, file-backed persistent
operator memory, private-output content handling, provider/live proof, public
sync, or memory/RAG route release.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map citation | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Chain map | MSEA-R28-T20 is a local source-governed implementation tranche |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | Route as advisory input only; require local source verification before inclusion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T20 helper, focused test, and worker return |
| Disposition | No external knowledge is required or authorized for T20 |
| Claim boundary | External claims do not authorize MinerU runtime, private-output read, memory/RAG write, public claims, provider/live proof, or runtime route wiring |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage surface touched | In-process durable store invocation in focused tests only |
| Runtime storage implementation changed | No |
| Durable store invoked | Yes, bounded to focused in-process tests through the existing `DurableMemoryStore.write` contract |
| Foundation storage claim | T20 proves only local helper-to-store invocation behavior under deterministic tests; no file-backed production persistence, memory/RAG route release, public storage, provider/live behavior, or runtime workflow-chain claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | T20 source/test durable-store invocation helper dispatch |
| claimDisposition | CLAIM_REJECTED for execution-control, interception, provider, public, production workflow-chain, and memory/RAG route claims |
| receiptEvidence | N/A with reason: dispatch creates no durable-store receipt; worker return must record any focused in-process test receipt evidence |
| actionEvidence | N/A with reason: dispatch executes no durable-store action; worker return must record any local deterministic helper/test invocation evidence |
| invocationBoundary | No MinerU runtime, provider, MCP, browser, public, file-backed production store, vectorization, retrieval, or memory/RAG route invocation is authorized |
| interceptionBoundary | No live interception, enforcement wrapper, runtime route, or production agent control is claimed |
| claimLanguage | Use bounded helper/test invocation language only |
| forbiddenExpansion | Do not expand T20 into private-output content handling, provider/live proof, public-sync, Web/UI, production storage, memory/RAG route release, retrieval, vectorization, or production-readiness claim |
| Runtime execution authorized | Local deterministic unit-test helper invocation only |
| Provider/live proof authorized | No |
| MinerU runtime execution authorized | No |
| Durable memory write authorized | Only in-process focused test invocation through T20 helper |
| Memory/RAG write authorized | No |
| Public claim authorized | No |
| Worker commit authorized | No |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T20 is private provenance governance and foundation-plane source/test
work. No public-sync artifact or public catalog claim is authorized by this
baseline.

## Claim Boundary

This baseline authorizes only a bounded T20 source/test durable-store invocation
helper and no-commit worker execution. It does not authorize MinerU runtime,
private/generated output content reads, Candidate Group A import, provider/live
proof, public-sync, Web/UI, file-backed production persistence, memory/RAG
route release, vectorization, retrieval, standalone app work, legal/use-case
deep dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, worker stage, worker commit,
or push.
