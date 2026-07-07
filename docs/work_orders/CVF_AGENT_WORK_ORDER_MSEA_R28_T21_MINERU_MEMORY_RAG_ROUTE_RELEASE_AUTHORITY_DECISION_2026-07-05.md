# CVF Agent Work Order - MSEA R28 T21 MinerU Memory RAG Route Release Authority Decision

Memory class: governed-work-order

Status: DISPATCH_READY

Created: 2026-07-05

rawMemoryReleased: false

## Dispatch Prompt Envelope

dispatchId: MSEA-R28-T21-MINERU-MEMORY-RAG-ROUTE-RELEASE-AUTHORITY-DECISION

route: WORKER_MUST_NOT_COMMIT

taskClass: Worker execution (WORKER_MUST_NOT_COMMIT)

role: worker

dispatchBaseHead: `4c184edb6`

executionBaseHead: WORKER_CAPTURE_AT_START

Commit mode: WORKER_MUST_NOT_COMMIT

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_2026-07-05.md`

Current-time notes: Artifact date is 2026-07-05. T20 material commit
`696c01224` closed bounded durable-store invocation evidence, and worker-output
quality hardening at `cb4e296db` added ADIF-0024 and Worker Output Quality
Controls. Current session head is `4c184edb6` before T21 dispatch authoring.

Do-not-misread notes: T21 is a docs-only authority decision packet. It does not
authorize actual memory/RAG route release, route wiring, memory write,
retrieval, vectorization, file-backed production persistence, MinerU runtime,
private/generated output content read, provider/live proof, public-sync,
source/test edits, worker stage, worker commit, or push.

Required first actions: read startup/state/handoff, guard orientation, literal
gotchas, paired GC-018 baseline, this work order, T20/T19/T18/T17/R27/R24-T4
evidence, ADIF-0024, and checker sources; capture start HEAD/status; confirm
worker output paths are absent; then write only the allowed T21 matrix and
worker return.

Return contract: leave the two T21 worker artifacts unstaged and uncommitted,
with exact final command reruns, worker-return fast gate, pre-implementation
autorun, provider-local/IDE hygiene evidence, Pylance/static-analysis
disposition, negative edge-case decision rows, and no-commit statement.

workerTargetPaths:

- `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`

Do not commit. Do not stage. Do not push.

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intake summary | Operator requested continuation of the governed T21 work order using accepted T20 closure evidence and worker-output quality hardening |
| scope classification | Bounded docs-only decision worker; changed paths are limited to the T21 decision matrix and T21 worker return |
| risk sensitivity | High governance risk because route release, memory write, private output, provider/live, public-sync, legal, production, and readiness claims remain parked |
| selected role route | routeMode: MULTI_AGENT_SINGLE_ROLE |
| role separation basis | Dispatcher authors this work order; single no-commit worker creates decision artifacts; reviewer/closer owns closure conversion and any material commit |
| escalation condition | Hold or return to orchestrator if source facts are missing, worker paths collide, forbidden actions are required, provider-local files cannot be cleaned or disclosed, or route release would require implementation |

## Worker Autonomy / No-Question Rule

Worker should complete the allowed docs-only decision packet without asking
preference questions. Ask the operator only if a required source is missing,
the allowed paths collide, or completion would require forbidden scope. Allowed
artifact defects must be repaired and rerun by the worker before return.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Dispatcher | Author this source-verified T21 work order and paired baseline |
| Worker | Create only the T21 decision matrix and T21 worker return under WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | Review worker output, perform allowed docs-only repair if needed, run closure gates, and own material commit |
| Session-sync steward | Update session state only if reviewer acceptance changes next move |

## Purpose

Decide, with source-verified evidence, whether accepted T20 bounded helper/test
evidence supports selecting a future implementation candidate for MinerU
memory/RAG route release, while keeping T21 itself decision-only.

## Authority Chain

| Authority | Role in T21 |
| --- | --- |
| Current session next allowed move | Author fresh T21 GC-018/source-verified work order |
| T20 completion review and worker return | Accepted bounded helper/test invocation evidence and workspace hygiene controls |
| T19 decision matrix | Selected T20 invocation candidate and preserved memory/RAG holds |
| T18 adapter candidate | Metadata-only adapter payload and fail-closed criteria |
| T17 authority matrix | Durable-memory write criteria and R27/R24-T4 gates |
| R27 decision ledger | Scan-to-memory prerequisite route matrix |
| R24-T4 private-output policy | Private/generated output boundary |
| ADIF-0024 and work-order template | Worker Output Quality Controls and stale-evidence prevention |

## Operator Checkpoint

No fresh operator checkpoint is required for the worker to execute this
docs-only decision packet. Return to orchestrator if execution would require
route implementation, source/test edits, private/generated content reads,
provider/live proof, public-sync, or a changed commit mode.

## Pre-flight Checks

| Check | Required worker evidence |
| --- | --- |
| Start head | `git rev-parse --short HEAD` captured as executionBaseHead |
| Worktree state | `git status --short --untracked-files=all` before writing |
| Path collision | Planned T21 matrix and worker-return paths do not already exist |
| Authority reads | Required First Reads completed |
| Provider-local boundary | `.qwen` and `.vscode` treated as local side-channel state, not CVF authority |

## Write Ownership

| Surface | Owner |
| --- | --- |
| T21 decision matrix | Worker may create, reviewer may repair inside decision scope |
| T21 worker return | Worker may create, reviewer may repair inside decision scope |
| Source/test/runtime/session/handoff/checker/provider-local/public files | Not worker-owned in T21 |
| Commit | Reviewer/closer only after acceptance; worker must not commit |

## Required First Reads

Before writing the worker artifacts, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by session state
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_2026-07-05.md`
- this work order
- `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_COMPLETION_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md`
- `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
- `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`
- `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md`
- `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md`
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0024.md`
- `governance/compat/check_worker_return_quality_gate.py`
- `governance/compat/check_governed_artifact_checker_read_ahead.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_adif_defect_registry_disclosure.py`

## Mission

Create the T21 docs-only authority decision matrix and worker return that decide
whether accepted T20 evidence supports selecting a future T22 implementation
candidate for MinerU memory/RAG route release.

T21 is not an implementation packet. It must not release actual memory/RAG
writes, route wiring, vectorization, retrieval, file-backed production
persistence, runtime MinerU execution, private/generated output content, or
production workflow claims.

## Allowed Scope

You may create only:

- `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`

The decision matrix must select exactly one:

- `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE`
- `MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_GAP`
- `BLOCKED_SOURCE_NOT_FOUND`

If selecting the T22 candidate, preserve this hold token:

`MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY`

## Forbidden Scope

Do not:

- edit source, tests, runtime hierarchy, durable store source, root barrels,
  checker/hook files, session state, handoff files, public-sync files, IDE
  config, provider-local files, or prior T17-T20 artifacts;
- run MinerU runtime, provider/live proof, browser proof, public-sync,
  vectorization, retrieval, file-backed production persistence, or production
  durable-store invocation;
- read, quote, copy, import, stage, or commit private/generated output content;
- import Candidate Group A or any private source-mirror output;
- claim extraction accuracy, document truth, legal quality, current-law
  correctness, workflow-chain production readiness, public readiness, or
  automatic route enforcement;
- stage, commit, push, or write public artifacts.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Record initial `git status --short --untracked-files=all`.
3. Confirm the two T21 worker output paths are absent before writing.
4. Read the required sources and checker files.
5. Create the T21 decision matrix with source verification, release/hold
   gates, negative edge-case decision rows, and a clear selected disposition.
6. Create the T21 worker return with command evidence, worker-output quality
   controls, provider-local/IDE hygiene, Pylance/static-analysis disposition,
   claim boundary, and no-commit statement.
7. Rerun all required commands after the final material edit.

## Evidence Requirements

Worker return must include:

- executionBaseHead;
- `git status --short --untracked-files=all` before writing and after the worker return exists;
- `git diff --name-status`;
- ignored-aware provider-local scan for `.qwen` and `.vscode`;
- worker-return fast gate command and final result;
- pre-implementation autorun command and final result;
- Source Verification Summary;
- Provider-Local Stray Artifact Control;
- Pylance Static-Analysis Diagnostic Boundary;
- Worker Output Quality Controls;
- at least one negative edge-case decision row for private-output, memory-write,
  route-release, security, or unsafe-normalization surfaces;
- a direct no-commit statement.

## Verification Commands

Run these after the final material edit:

```text
python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short --untracked-files=all
git status --short --ignored .qwen .vscode
```

If a command fails because of an allowed-scope artifact defect, repair it and
rerun after the last edit. If a command would require forbidden scope, return
`BLOCKED` with reason and do not claim completion.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

individualCheckerSubstitution: FORBIDDEN

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --path docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without heading prefixes. The worker return must include Purpose, Target
/ Source, Source Inventory, Scope / Methodology, Changed Files, Command
Evidence, Source Verification Summary, Findings / Position, Risk / Corrective
Action, Worker Output Quality Controls, Provider-Local Stray Artifact Control,
Pylance Static-Analysis Diagnostic Boundary, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, External Knowledge Intake Routing, Rescan
Intelligence Hardening, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Claim
Boundary, git status --short, Return-To-Orchestrator, Worker Experience
Retrospective, and No-Commit Statement.

## Worker Output Quality Controls

rawMemoryReleased=false. This work order does not release raw memory,
retrieval, reinjection, private-output content, or memory/RAG write behavior.

Before `COMPLETE_PENDING_REVIEW`, complete and record this self-audit:

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
- include at least one negative or edge-case decision row proving risky route
  release/private-output/memory-write/security/unsafe-normalization input fails
  closed or holds.

## Provider-Local Stray Artifact Control

| Condition | Required handling |
| --- | --- |
| Existing `.qwen/settings.json` | Pre-existing provider-local local state; do not read as authority, edit, stage, commit, or cite for source evidence |
| New provider-local files | Forbidden; examples include `.qwen`, IDE-local settings, provider-local memory/config/cache files, and tool-generated settings |
| Final evidence | Worker return must include `git status --short --untracked-files=all` and an ignored-aware provider-local scan for `.qwen` and `.vscode` |
| Blocker token | If provider/model switching creates an unremovable or uncertain provider-local file, return `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` with exact path and no clean-worktree claim |

## Pylance Static-Analysis Diagnostic Boundary

| Condition | Required handling |
| --- | --- |
| Pylance may report missing import in the Python test | Record as static-analysis path issue, not as a failing Python runtime test |
| Allowed T21 action | Record disposition in the worker return if encountered |
| Forbidden T21 action | Do not edit Python source/tests, `.vscode/settings.json`, `pyrightconfig.json`, provider-local files, or IDE config |

## Decision Matrix Requirements

The matrix must include:

- Source Verification Block using only source-verified rows, not provider-local
  memory or chat history;
- Decision Candidate Table with the three allowed route dispositions;
- Release Gate Matrix covering T20 helper/test evidence, T19 route decision,
  T18 adapter metadata-only boundary, T17 durable-memory write criteria, R27
  receipt/quality/source-pointer/downstream-use/claim-boundary prerequisites,
  R24-T4 private-output policy, durable store actor/provenance/raw-payload
  gates, and ADIF-0024 worker-quality requirements;
- Negative Edge-Case Decision Rows for private output, memory write,
  route-release overclaim, unsafe metadata/normalization, provider-local files,
  and static-analysis/Pylance drift;
- selected disposition and next recommended move;
- Claim Boundary and Public Export Disposition.

## Acceptance Criteria

| ID | Criteria |
| --- | --- |
| AC1 | Worker creates only the T21 decision matrix and worker return |
| AC2 | Matrix source-verifies all release/hold criteria from T20, T19, T18, T17, R27, R24-T4, ADIF-0024, and relevant runtime source |
| AC3 | Matrix selects exactly one allowed route disposition and preserves a no-release hold token for T21 |
| AC4 | Worker return includes exact final command reruns after final edits |
| AC5 | Worker return includes current git status with untracked files and ignored-aware provider-local scan |
| AC6 | Worker return dispositions Pylance/static-analysis issues without source/test edits |
| AC7 | Worker includes negative edge-case decision rows for route-release and private-output/memory/security surfaces |
| AC8 | Worker performs no forbidden source/test/runtime/session/provider-local/public/live actions |

## Review Gate

Reviewer must reject or return the worker packet if:

- the selected disposition is not one of the three allowed tokens;
- the worker edits any path outside the two workerTargetPaths;
- command evidence is stale, missing final rerun evidence, or omits untracked
  status/provider-local scan;
- provider-local or IDE side-channel files are created and hidden;
- static-analysis/Pylance issues are silently ignored or fixed through
  forbidden source/test/IDE edits;
- matrix rows infer route release from T20 without source verification;
- private/generated output content is read, quoted, imported, or used as
  authority;
- worker claims actual memory/RAG route release, production persistence,
  vectorization, retrieval, runtime workflow, provider/live proof, public
  readiness, legal quality, extraction accuracy, document truth, current-law
  correctness, or production readiness.

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

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Evidence Requirements; Verification Commands; Worker Return Packet Shape Contract; Worker Output Quality Controls; Provider-Local Stray Artifact Control; Pylance Static-Analysis Diagnostic Boundary; Decision Matrix Requirements; ADIF Defect Registry Disclosure; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirm T21 dispatch artifact shape after checker source read-ahead; not first discovery |
| claimBoundary | checker read-ahead evidence only; no worker execution, MinerU runtime, private-output, provider/live, public, memory/RAG route, source/test edit, or production claim |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T20 closed as bounded helper/test invocation only and kept memory/RAG route release held | `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_COMPLETION_2026-07-05.md` | lines 37-48 and 205 | `CLOSED_PASS_BOUNDED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T20_INVOCATION_ONLY`; `fresh T21 authority decision` | T20 completion review | VALUE_SET | ACCEPT |
| T20 worker return records provider-local and Pylance/static-analysis boundaries | `docs/reviews/CVF_MSEA_R28_T20_MINERU_ACTUAL_DURABLE_STORE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-05.md` | lines 168-186 | `Pylance Static-Analysis Diagnostic Boundary`; `Provider-Local Stray Artifact Control` | T20 worker return | VALUE_SET | ACCEPT |
| T20 helper result returns bounded durable-store receipt evidence only inside helper result | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 66-75 and 392-398 | `durableStoreReceipt` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
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
| T19 selected T20 as candidate but kept actual memory/RAG write held | `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md` | lines 66-72 and 87-89 | `T20_DURABLE_STORE_INVOCATION_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T19_DECISION_ONLY`; `PRIVATE_OUTPUT_NOT_READ_OR_RELEASED` | T19 decision matrix | VALUE_SET | ACCEPT |
| T18 adapter builder fail-closes on unsafe output-content, memory-write authorization, policy, actor, provenance, actor-role/tier, and R27 prerequisite gaps | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 779-917 | `build_mineru_durable_memory_write_adapter_candidate`; `OUTPUT_CONTENT_READ_FORBIDDEN`; `MEMORY_WRITE_ALREADY_AUTHORIZED`; `R27_PREREQUISITE_MISSING` | MinerU metadata receipt writer | RUNTIME_BEHAVIOR | ACCEPT |
| T18 adapter payload renders metadata-only fields and carries R27 prerequisites, summary-only, no reinjection, no raw-memory release, and no output-content read | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 928-953 | `mineru_durable_memory_write_adapter_candidate_payload`; `r27ReceiptPrerequisite`; `summaryOnly`; `canReinject`; `rawMemoryReleased`; `outputContentRead` | MinerU metadata receipt writer | EXISTS | ACCEPT |
| T17 durable-memory authority criteria require allow policy, authorized actor, provenance, raw-payload exclusion, summary-only receipt, actor-role authorization, R27 prerequisites, and R24-T4 privacy | `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | lines 43-57 | `policyDecision`; `actorAuthorized`; `provenanceScore`; `raw-payload rejection`; `summary-only receipt`; `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE` | T17 authority matrix | VALUE_SET | ACCEPT |
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
| `BLOCKED_SOURCE_NOT_FOUND` usage | Allowed only as a future worker selected disposition if source verification genuinely fails; not used as a current source-verification disposition in this work order |
| Absent-versus-collision disposition | Path absence is checked only for exact planned T21 artifact paths; token collisions are recorded as not binding unless tied to a cited source row |
| Collision handling | If any planned worker output path exists at execution start, worker must stop and return to orchestrator |

## Work-Order Fulfillment Manifest

| Field | Value |
| --- | --- |
| expectedWorkerPaths | T21 decision matrix; T21 worker return |
| workerMayCommit | false |
| workerMayEditSource | false |
| workerMayRunRuntime | false |
| workerMayReadPrivateGeneratedOutput | false |
| reviewerOwnsClosure | true |

## Agent Operation Trace Block

| Field | Value |
| --- | --- |
| Session or invocation | 2026-07-05 T21 work-order authoring |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Target paths | T21 GC-018 baseline and T21 work order |
| Allowed scope source | Current session next allowed move using accepted T20 closure evidence and worker-output quality hardening |
| Before status evidence | HEAD `4c184edb6`; clean worktree before T21 authoring confirmed by `git status --short --untracked-files=all` empty output |
| Approval boundary | Approval policy never; no external approval requested; no runtime/provider/live/public action authorized |
| Claim boundary | Dispatch authoring only; no worker execution, MinerU runtime, private-output read, provider proof, public-sync, memory/RAG route release, source/test edit, or production-readiness claim |
| Actor | Codex dispatcher |
| Provider or surface | Local filesystem and governance commands |
| Command or tool surface | `rg`; `Get-Content`; `Test-Path`; `python governance/compat/run_adif_defect_resolver.py`; `python governance/compat/check_*`; `python governance/compat/run_agent_autorun_workflow_gate.py`; `apply_patch` |
| After status evidence | Two untracked T21 dispatch artifacts before commit |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Agent type | Codex dispatcher |
| Invocation ID | T21-dispatch-authoring-2026-07-05 |
| Expected manifest | T21 GC-018 baseline and T21 work order |
| Actual changed set | T21 GC-018 baseline and T21 work order |
| Manifest delta | MATCH |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldTool | manual scaffold from current work-order template and passed T20 packet shape |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T21 --title "MinerU Memory RAG Route Release Authority Decision" --date 2026-07-05 --base 4c184edb6 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldSource | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; T20 dispatch baseline/work order |
| scaffoldReason | T21 requires source-verified decision worker dispatch rather than runtime/source implementation |
| manualEditsAfterScaffold | Filled T21 envelope fields, authority chain, roles, pre-flight checks, source verification, ADIF-0024 disclosure, worker-output quality controls, provider-local/Pylance boundaries, handoff controls, and claim boundary |
| docOnlyNewFields | `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE`; `MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_GAP`; `MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY`; `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| claimBoundary | Dispatch scaffold provenance only; no provider/live/public/Web/MCP/model-router/runtime behavior claim |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored work order to single no-commit docs-only decision worker, then reviewer closure conversion |
| phase | dispatch |
| baseHeadFor(phase) | `dispatchBaseHead=4c184edb6`; `executionBaseHead=WORKER_CAPTURE_AT_START`; `closureBaseHead=REVIEWER_SET_AT_CLOSURE` |
| changedSetScope(phase) | dispatch changes are this work order and paired T21 GC-018 baseline; worker changes are limited to T21 decision matrix and T21 worker return |
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

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker paths limited to two target artifacts | PASS or BLOCKED with reason |
| Selected disposition exactly one allowed token | PASS or BLOCKED with reason |
| Source verification complete | PASS or BLOCKED with reason |
| Worker Output Quality Controls complete | PASS or BLOCKED with reason |
| Provider-local and IDE hygiene disclosed | PASS or BLOCKED with reason |
| Pylance/static-analysis boundary honored | PASS or BLOCKED with reason |
| No runtime/private-output/provider/public/source/test/session action | PASS or BLOCKED with reason |
| No worker commit/stage/push | PASS or BLOCKED with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T21 dispatch artifacts are private provenance governance material. No
public artifact, public-sync remote, public commit, or public catalog claim is
authorized by this work order.

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

This work order authorizes only a no-commit docs-only T21 decision matrix and
worker return. It does not authorize actual memory/RAG route release,
production durable-store invocation, file-backed production persistence,
vectorization, retrieval, MinerU runtime execution, private/generated content
read, Candidate Group A import, provider/live proof, public-sync, Web/UI,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, worker stage, worker commit, or push.
