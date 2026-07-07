# CVF Agent Work Order - MSEA R28 T20 MinerU Actual Durable Store Invocation Implementation

Memory class: governed-worker-dispatch
Status: DISPATCH_READY
Date: 2026-07-05
Batch ID: MSEA-R28-T20-MINERU-ACTUAL-DURABLE-STORE-INVOCATION-IMPLEMENTATION
GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_2026-07-05.md`
Dispatch base head: d59fbdb3e
Commit mode: WORKER_MUST_NOT_COMMIT
Worker role: implementation worker
Reviewer role: reviewer/closer
rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: implementation worker for MSEA-R28-T20.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_2026-07-05.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: Worker must capture `git rev-parse --short HEAD` at start and report it in the worker return.

Current-time notes: Artifact date is 2026-07-05. T19 material commit
`dc687360` selected `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE`
while keeping memory/RAG write and production invocation routes held. Session
sync head `d59fbdb3e` routes the next allowed move to T20 work-order authoring.

Do-not-misread notes: T20 may implement and test a bounded helper that calls
the existing in-process durable store through `DurableMemoryStore.write`. T20
does not authorize MinerU runtime execution, private/generated output content
reads, provider/live proof, public-sync, memory/RAG route release, production
file-backed storage proof, Web/UI, checker/hook/session/handoff edits by
worker, worker stage, worker commit, or push.

Required first actions: read the mandatory startup files, read the paired T20
GC-018 baseline, capture start HEAD/status, confirm planned worker output
paths are absent, confirm pre-existing provider-local stray state without
reading it as authority, then write only the allowed T20 source/test/worker
return paths.

You are executing MSEA-R28-T20 in the private CVF provenance repository.

Task: implement a bounded Learning Plane Foundation helper that consumes the
accepted T18 adapter payload shape, maps it to `DurableMemoryWriteInput`, calls
`DurableMemoryStore.write`, and returns durable-store receipt evidence in
focused deterministic tests.

Required output paths:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-durable-store-invocation.test.ts`
- `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`

Hard boundary: do not edit Python source/tests, durable store source, runtime
hierarchy source, root barrel exports, ignored IDE config, provider-local
files, session/handoff surfaces, checker/hook files, public-sync files, Web/UI,
or future T21 artifacts.

Return contract: leave the three T20 worker artifacts unstaged and uncommitted,
with focused test, typecheck or bounded typecheck disposition, worker-return
fast gate, pre-implementation autorun, provider-local no-stray evidence, and
Pylance diagnostic boundary recorded.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| canonicalRouteMode | MULTI_AGENT_SINGLE_ROLE |
| selected role route | single no-commit implementation worker followed by reviewer closure conversion |
| intake summary | T20 implements a bounded helper/test path for adapter-payload-to-durable-store invocation |
| scope classification | Learning Plane Foundation source/test helper implementation plus worker return |
| risk sensitivity | high, because durable memory persistence and private-output boundaries are adjacent but remain bounded |
| escalation condition | Return to orchestrator if source facts are missing, planned paths collide, package checks require out-of-scope edits, provider-local files are created and cannot be safely removed, or completion would require private-output read/provider/live/public/session/checker/hook edits |
| Dispatch role | Orchestrator/dispatcher |
| Worker role | Single implementation worker |
| Reviewer role | Reviewer/closer |
| Commit authority | Worker must not commit |
| Closure conversion | Reviewer owns material acceptance, repairs, and commit |

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Dispatcher | Author GC-018 baseline and work order, run pre-dispatch gates, commit dispatch artifacts |
| Worker | Create T20 helper source, focused tests, and worker return only, run worker gates, leave changes uncommitted |
| Reviewer/closer | Review and repair T20 worker artifacts if needed, convert worker return to closure, commit material acceptance |
| Session-sync steward | Update session continuity only upon accepted reviewer closure |

## Purpose

T19 accepted source evidence for a future T20 durable-store invocation
implementation candidate. T20 must now implement the first bounded helper that
actually calls the existing durable store write contract from a validated
MinerU adapter payload shape, while keeping memory/RAG route release,
private-output content handling, provider/live proof, public-sync, and
production-readiness claims out of scope.

## Authority Chain

| Authority | Required use in T20 |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Confirm current mode and next allowed move before work |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Confirm compact startup state |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Confirm canonical active handoff and current mode |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Confirm active handoff instructions and T20 next allowed move |
| `docs/reference/guard_orientation/README.md` | Identify required governed artifact surfaces |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Avoid known literal-format failures |
| `docs/baselines/CVF_GC018_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_2026-07-05.md` | Execute only the authorized T20 scope |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator requested T20 work order | ACCEPT - this packet releases only T20 worker execution after dispatch gates pass |
| Operator noted Python Pylance warning | ACCEPT - recorded as IDE static-analysis path issue; no Python source/test edit is authorized in T20 |
| Operator noted `.qwen/settings.json` provider-local stray risk | ACCEPT - worker must not create, edit, hide, stage, commit, or use provider-local files as authority |
| Parked lanes | HELD - MinerU runtime, private-output content, provider/live proof, public-sync, memory/RAG route release, retrieval/vectorization, Web/UI, app, legal/use-case, and production workflow-chain claims remain unauthorized |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| T19 material closure | `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`, material commit `dc687360` | ACCEPT |
| T19 selected T20 route | `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md` lines 66-72 selected `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE` | ACCEPT |
| T19 kept memory/RAG write held | `CVF_SESSION/state/entries/mseaR28T19MineruDurableStoreInvocationReleaseDecisionClosure20260705.json` lines 17-20 | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `d59fbdb3e` before authoring | ACCEPT |
| T20 artifact collision check | Planned T20 baseline, work order, and worker-return paths were absent before authoring | ACCEPT |

## Scope / Target / Owner Boundary

Allowed worker changes:

- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts`;
- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-durable-store-invocation.test.ts`;
- create `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`;
- define a T20 TypeScript adapter-payload input interface that matches the T18 payload keys used by T19;
- implement a helper named close to `invokeMineruDurableStoreWrite`;
- make the helper fail closed before store invocation when adapter payload is unsafe, prerequisites are false, output content was read, raw memory was released, reinjection is enabled, summary-only is false, or memory write is already authorized;
- call `store.write` with a `DurableMemoryWriteInput` built only from metadata fields;
- return the durable store receipt and bounded metadata while preserving `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY`;
- add focused tests for allowed write, policy denial, actor denial, low provenance, invalid actor/tier denial, unsafe adapter payload rejection, and no raw/private content fields.

Forbidden worker changes or claims:

- do not edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- do not edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`;
- do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`;
- do not edit `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`;
- do not edit `.vscode/settings.json`, `.qwen/settings.json`, `.git/info/exclude`, provider-local memory/config/cache files, session front doors, generated session state, active handoff, root agent instruction files, checkers, hooks, public-sync files, dashboard/Web/UI, or model-router surfaces;
- do not run MinerU runtime, read private/generated MinerU output content,
  import Candidate Group A, run provider/live proof, vectorize, retrieve, write
  a memory/RAG route, create production file-backed storage evidence, run a
  standalone PDF app, make public claims, stage, commit, or push.

## Write Ownership

| Actor | Owned paths |
| --- | --- |
| Dispatcher | T20 GC-018 baseline and this work order |
| Worker | T20 helper source, focused test, and T20 worker return only |
| Reviewer/closer | Review, repair if needed, material closure commit |
| Session-sync steward | Session memory/state/handoff updates only upon accepted T20 reviewer closure |

## Required First Reads

Worker must read these files before writing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V36_2026-07-04.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_2026-07-05.md`
- `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json`

## Preflight Checks

Worker must run or capture equivalent local evidence:

```text
git rev-parse --short HEAD
git status --short --untracked-files=all
Test-Path EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts
Test-Path EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-durable-store-invocation.test.ts
Test-Path docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md
git status --short --ignored .qwen .vscode
```

Expected preflight result: the three planned worker output paths should not
already exist at worker start. `.qwen/settings.json` may exist as pre-existing
provider-local state and must not be edited or cited as authority.

## Execution Plan

1. Read startup, state, handoff, guard orientation, literal gotchas, this work
   order, paired GC-018, source files, and worker-output checker source.
2. Capture executionBaseHead and exact worktree/provider-local status.
3. Create the T20 helper source file with a narrow adapter-payload interface,
   fail-closed validation, a metadata-only `DurableMemoryWriteInput` mapper,
   and a helper that calls `DurableMemoryStore.write`.
4. Ensure the helper rejects unsafe adapter payloads before store invocation:
   output content read, raw memory release, reinjection, summary-only false,
   memory write already authorized, missing R27 prerequisite, missing metadata,
   or raw-content-like markers in metadata fields.
5. Ensure the helper preserves store-level denials rather than bypassing them:
   non-allow policy, actor unauthorized, low provenance, invalid actor/tier,
   secret flag, blocked lifecycle, or runtime hierarchy denial.
6. Add focused Vitest tests using `createInProcessDurableMemoryStore`.
7. Do not modify the durable store source, runtime hierarchy source, Python
   source/test, `.vscode`, `.qwen`, session/handoff, or public-sync paths.
8. Create the worker return with changed-file manifest, command evidence,
   provider-local no-stray statement, Pylance diagnostic boundary, and
   no-commit statement.
9. Run focused Vitest, package check if feasible, worker-return fast gate, and
   pre-implementation autorun; repair allowed-scope failures directly.
10. Leave changes unstaged and uncommitted.

## Implementation Guidance

The worker may choose exact internal names if tests and source verification
remain satisfied, but the preferred shape is:

- `MineruDurableStoreInvocationInput` for the adapter-payload-like input shape;
- `MineruDurableStoreInvocationResult` for helper output;
- `invokeMineruDurableStoreWrite(store, input)` as the main helper;
- `MINERU_DURABLE_STORE_INVOCATION_IMPLEMENTED` as a successful helper
  disposition token;
- `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY` as the explicit hold
  token confirming that memory/RAG route release remains outside T20;
- no root barrel export in T20.

## Pylance Static-Analysis Diagnostic Boundary

| Observation | Required handling |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` uses `sys.path.insert` before importing `mineru_metadata_receipt_writer` | Treat as existing pytest runtime pattern |
| Pylance may report missing import in the IDE | Record as static-analysis path issue, not as a failing Python runtime test |
| `.vscode/settings.json` is ignored by `.gitignore` | Do not edit it in T20 |
| If worker believes IDE config must be changed | Return `BLOCKED_WITH_REASON`; do not add ignored config or a new `pyrightconfig.json` under T20 |

## Provider-Local Stray Artifact Control

| Rule | Required worker handling |
| --- | --- |
| Existing `.qwen/settings.json` | Pre-existing provider-local local state; do not read as authority, edit, stage, commit, or cite for source evidence |
| New provider-local files | Forbidden; examples include `.qwen`, IDE-local settings, provider-local memory/config/cache files, and tool-generated settings |
| Local excludes | Worker must not add or change `.git/info/exclude` and must not use local excludes to hide material changes |
| Final evidence | Worker return must include `git status --short --untracked-files=all` and an ignored-aware provider-local scan for `.qwen` and common provider-local roots |
| Blocker token | If provider/model switching creates an unremovable or uncertain provider-local file, return `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` with exact path and no clean-worktree claim |

## Worker Autonomy / No-Question Rule

Worker may choose the exact helper layout, provided all allowed-scope tests,
gates, and claim boundaries are satisfied. Worker must repair only T20 helper,
focused test, and worker-return defects. Source/test/session/handoff/checker/
hook/public/provider-local/IDE config edits outside the listed ownership are
out of scope.

No-Question Rule: If a gate failure is repairable within the three authorized
worker artifacts, repair it directly and rerun the gate. Ask the operator only
if the requested repair would require out-of-scope files, private/generated
output reads, provider/live proof, commit authority, public-sync, or a new
product decision.

## Return-To-Orchestrator Conditions

Return without completing T20 if any condition is true:

- a required source file is missing;
- a required source fact cannot be verified from source or canonical contract;
- planned T20 worker output paths already exist with conflicting content at
  worker start;
- any gate demands Python source/test, durable store source, runtime hierarchy,
  root barrel, session, handoff, checker, hook, IDE config, provider-local, or
  public-sync edits;
- private/generated output content would need to be read;
- provider/live proof, MinerU runtime, production file-backed storage evidence,
  retrieval/vectorization, or memory/RAG route release would be required to
  support a claim;
- provider/model switching creates a provider-local stray file that cannot be
  confidently removed as worker-created local output.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T20 --title "MinerU Actual Durable Store Invocation Implementation" --date 2026-07-05 --base d59fbdb3e --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added T20 source verification, dependency evidence, bounded Learning Plane helper scope, Pylance diagnostic boundary, provider-local stray control, handoff control, worker return contract, and claim boundaries |
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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Provider-Local Stray Artifact Control; Pylance Static-Analysis Diagnostic Boundary; Public Export Disposition; Foundation Storage Layout Block |
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
| `MineruDurableStoreInvocationResult` | proposed T20 TypeScript result interface for bounded receipt evidence | DOC_ONLY_NEW |
| `invokeMineruDurableStoreWrite` | proposed T20 helper that validates adapter payload and calls `DurableMemoryStore.write` | DOC_ONLY_NEW |
| `MINERU_DURABLE_STORE_INVOCATION_IMPLEMENTED` | proposed T20 helper disposition token | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY` | proposed hold token for memory/RAG route release | DOC_ONLY_NEW |
| `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` | worker-return blocker token for provider-local artifact leakage | DOC_ONLY_NEW |

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
| Existing T20 helper source path | PASS: planned helper source path absent before authoring |
| Existing T20 focused test path | PASS: planned focused test path absent before authoring |
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
| Planned T20 helper source path | Absent before authoring |
| Planned T20 focused test path | Absent before authoring |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
| --- | --- |
| Applicability | NOT_APPLICABLE_WITH_REASON: T20 does not reopen or close a legacy absorption coverage index row |
| Coverage index row evidence | N/A with reason: no legacy coverage row is accepted, modified, or closed by this dispatch |
| Claim boundary | no legacy copied folder, historical adapter, or prior absorption source is promoted to current authority |

## Dual Agent Surface Matrix

| Surface | Worker allowed | Reviewer allowed | Boundary |
| --- | --- | --- | --- |
| T20 helper source | Yes | Reviewer may repair/accept | Local helper/test invocation only |
| T20 focused test | Yes | Reviewer may repair/accept | Deterministic in-process durable store tests only |
| T20 worker return | Yes | Reviewer may repair/accept | Review packet only |
| Python source/test | No | No under T20 | Static-analysis diagnostic is noted, not repaired |
| Durable store source/runtime hierarchy source | No | No under T20 | Existing source contracts are used read-only |
| Session state/handoff | No | Session-sync steward only upon accepted material closure | No worker edit |
| Provider-local files | No | No | Must not be material output |
| Public-sync | No | No | Private provenance only |

## Work-Order Fulfillment Manifest

| Output | Required action |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | Create bounded helper source |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-durable-store-invocation.test.ts` | Create focused Vitest coverage |
| `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md` | Create worker return and gate evidence |

No other output files are authorized.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`

Shape-list rule: when listing required worker-output sections, write section
names without heading prefixes. The worker return must include Purpose,
Target / Source, Source Inventory, Scope / Methodology, Changed Files, Command
Evidence, Source Verification Summary, Findings / Position, Risk / Corrective
Action, Provider-Local Stray Artifact Control, Pylance Static-Analysis
Diagnostic Boundary, Checker Source Read-Ahead Block, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, Public Export Disposition,
External Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus
Completeness And Report Integrity, Finding-To-Governance Learning Disposition,
Epistemic Process Block, Claim Boundary, git status --short, Return-To-
Orchestrator, Worker Experience Retrospective, and No-Commit Statement.

## Evidence Requirements

Worker return must include:

- executionBaseHead;
- `git status --short --untracked-files=all` before and after;
- ignored-aware provider-local scan for `.qwen` and `.vscode`;
- `git diff --name-status` for worker changes;
- focused Vitest command and result;
- TypeScript check command and result, or source-bounded blocker if unrelated package debt appears;
- worker-return fast gate command and result;
- pre-implementation autorun command and result;
- a direct statement that no Python source/test, durable store source, runtime
  hierarchy source, root barrel, session state, active handoff, public-sync,
  provider-local file, IDE config, MinerU runtime, private/generated output
  read, provider/live proof, stage, commit, push, or public claim occurred.

## Verification Commands

Worker must run:

```text
npm --prefix EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION exec vitest run --config vitest.config.ts tests/mineru-durable-store-invocation.test.ts
npm --prefix EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION run check
python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short --untracked-files=all
git status --short --ignored .qwen .vscode
```

If package-level TypeScript check fails because of unrelated legacy debt,
worker must run and record a focused `tsc` or Vitest evidence path if feasible,
then return `BLOCKED_WITH_REASON` or `COMPLETE_PENDING_REVIEW_WITH_BOUNDED_TYPECHECK`
for reviewer disposition. Do not edit out-of-scope files to make package checks
green.

## Acceptance Criteria

| AC | Criterion |
| --- | --- |
| AC1 | Worker creates only the T20 helper source, T20 focused test, and T20 worker return paths listed in this work order |
| AC2 | Helper consumes the T18 adapter payload shape and rejects unsafe values before calling the durable store |
| AC3 | Helper invokes an in-process `DurableMemoryStore.write` in tests and captures allowed and denied durable store receipts |
| AC4 | Helper preserves `summaryOnly: true`, `canReinject: false`, `rawMemoryReleased: false`, `outputContentRead: false`, and no raw/private content fields |
| AC5 | T20 keeps memory/RAG route release held by `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY` and does not perform vectorization, retrieval, MinerU runtime, private-output reads, provider/live proof, public-sync, or production storage evidence |
| AC6 | Focused Vitest and package TypeScript check pass, or package-level blocker is bounded and reviewer-approved |
| AC7 | Worker return reports changed files, command evidence, no-commit status, provider-local no-stray evidence, and Pylance diagnostic boundary |
| AC8 | No provider-local stray file is created or hidden by worker execution |

## Review Gate

Reviewer must verify:

- changed files are limited to T20 helper source, focused test, and T20 worker
  return before material closure;
- helper uses existing durable store and runtime hierarchy read-only;
- helper rejects unsafe adapter payloads before store invocation;
- tests prove both allowed and denied receipt paths;
- Python import warning was not "fixed" through unauthorized test/source or
  ignored IDE config edits;
- provider-local stray artifact controls are satisfied;
- actual memory/RAG route release remains unauthorized in T20;
- worker did not stage, commit, push, public-sync, run provider/live proof,
  read private/generated output content, or run MinerU runtime.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Local repository authoring through shell and apply_patch |
| Session or invocation | 2026-07-05 T20 work-order authoring |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Get-Content`; `Test-Path`; `python governance/compat/run_adif_defect_resolver.py`; `python governance/compat/build_dispatch_packet_scaffold.py`; `python governance/compat/check_*`; `apply_patch` |
| Target paths | T20 GC-018 baseline and T20 work order |
| Allowed scope source | Operator request to create T20 work order after accepted T19 closure selected the T20 implementation candidate route |
| Before status evidence | HEAD `d59fbdb3e`; clean worktree before T20 authoring confirmed by `git status --short --untracked-files=all` empty output |
| After status evidence | Two untracked dispatch artifacts before commit |
| Diff evidence | `git status --short --untracked-files=all` and `git diff --name-status --cached` to be recorded before dispatch commit |
| Approval boundary | Approval policy never; no external approval requested; no runtime/provider/live/public action authorized |
| Claim boundary | Dispatch authoring only; no worker execution, MinerU runtime, private-output read, provider proof, public-sync, memory/RAG route release, or production-readiness claim |
| Agent type | Codex dispatcher |
| Invocation ID | T20-dispatch-authoring-2026-07-05 |
| Expected manifest | T20 GC-018 baseline and T20 work order |
| Actual changed set | T20 GC-018 baseline and T20 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored work order to single no-commit implementation worker, then reviewer closure conversion |
| phase | dispatch |
| baseHeadFor(phase) | `dispatchBaseHead=d59fbdb3e`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this work order and paired T20 GC-018 baseline; worker changes are limited to T20 helper source, T20 focused test, and T20 worker return |
| traceScope(phase, actor) | dispatcher records scaffold, source verification, ADIF, checker read-ahead, Pylance boundary, and provider-local stray controls; worker records execution commands and changed files; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher may commit dispatch artifacts; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns continuity commit if required |
| crossBatchIsolation | T20 must not modify T18/T19 artifacts, Python source/tests, durable store source, runtime hierarchy source, session state, handoff, public-sync, provider-local files, IDE config, or future T21 artifacts |
| Before status evidence | HEAD `d59fbdb3e`; clean worktree confirmed before T20 dispatch authoring by `git status --short --untracked-files=all` empty output |
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

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| T20 helper source present and source-bounded | PASS or BLOCKED with reason |
| Focused test present and covers allowed/denied invocation receipts | PASS or BLOCKED with reason |
| Worker return present and gate-clean | PASS or BLOCKED with reason |
| No forbidden Python/durable-store/runtime/session/provider-local/public path touched by worker | PASS or BLOCKED with reason |
| Memory/RAG route release remains held beyond T20 | PASS or BLOCKED with reason |
| Provider-local no-stray evidence recorded | PASS or BLOCKED with reason |
| Pylance diagnostic boundary honored | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage surface touched | In-process durable store invocation in focused tests only |
| Runtime storage implementation changed | No |
| Durable store invoked | Yes, bounded to focused in-process tests through existing `DurableMemoryStore.write` |
| Foundation storage claim | T20 proves only local helper-to-store invocation behavior under deterministic tests; no file-backed production persistence, memory/RAG route release, public storage, provider/live behavior, or runtime workflow-chain claim |

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
work order.

## Claim Boundary

This work order authorizes only a bounded T20 source/test durable-store
invocation helper and worker return. It does not authorize MinerU runtime,
private/generated output content reads, Candidate Group A import, provider/live
proof, public-sync, Web/UI, file-backed production persistence, memory/RAG
route release, vectorization, retrieval, standalone app work, legal/use-case
deep dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, session-sync by worker,
worker stage, worker commit, or push.
