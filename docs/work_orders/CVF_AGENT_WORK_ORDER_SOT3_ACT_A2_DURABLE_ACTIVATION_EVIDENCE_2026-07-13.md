# CVF Agent Work Order - SOT3 Activation A2 Durable Activation Evidence

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-07-13

Work Order ID: SOT3-ACT-A2

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `656c176a2`

executionBaseHead: `8d928802b`

closureBaseHead: `8d928802b`

Worker return path: `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_WORKER_RETURN_2026-07-13.md`

## Dispatch Prompt Envelope

Role: bounded A2 implementation worker.

Canonical packet: paired A2 GC-018 and this work order.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture clean HEAD before any edit.

Current-time notes: A1 closed at material commit `149832b16`; continuity was
synced at `656c176a2`; A2 is the only active implementation tranche.

Do-not-misread notes: no A3-A5, live provider call, database/distributed
ledger, public export, UI work, production claim, or new whole-request denial
policy.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, A1 completion, parent roadmap, verified runtime/type
sources, and listed checker sources; capture HEAD and clean status.

Return contract: leave all changes uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement A2 durable activation evidence for the A1 knowledge-context path so
each SOT3 evaluation has an integrity-bound, restart-readable, secret-safe
record persisted before provider prompt construction.

## Target / Source

The paired GC-018 is the dispatch baseline. Runtime source and canonical SOT3
types control if any summary conflicts with the actual implementation.

## Scope / Methodology

Create a dedicated atomic local-file evidence store, extend the A1 adapter with
one actual lifecycle trace per evaluated chunk, persist one request-level
record between evaluation and prompt construction, emit secret-safe audit
evidence, and add deterministic storage and route tests.

## Authority Chain

Operator instruction -> activation roadmap -> A1 completion `149832b16` ->
paired A2 GC-018 -> this work order -> no-commit worker -> reviewer/closer.

## Agent Roles

The dispatcher owns packet source fidelity. The worker implements and tests
within Allowed Scope without commit. The reviewer independently reviews data
semantics, atomicity, ordering, negative paths, and evidence, repairs bounded
defects if needed, owns closure and material commit, then syncs session state.

## Write Ownership

The worker owns only the exact Allowed Scope as uncommitted changes. The
reviewer owns the completion review, accepted packet status conversion,
roadmap transition, material commit, and later session continuity. Preserve
and report any pre-existing change outside scope.

## Worker Autonomy / No-Question Rule

Repair allowed-scope source, test, formatting, and machine-gate failures
directly. Stop only for a dirty start, verified source contradiction,
forbidden-scope need, or missing authority that makes completion impossible.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intakeClass | private-provenance product evidence persistence |
| workerRole | bounded implementation worker |
| reviewerRole | independent reviewer/closer |
| externalReviewer | N/A with reason: no external advisory source is being absorbed |
| routingDecision | direct governed implementation from a source-verified packet |
| selectedRoleRoute | dispatcher -> worker -> reviewer/closer -> session steward |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| riskSensitivity | R2: persistence affects context admission only when SOT3 is enabled |
| escalationCondition | source contradiction, forbidden path, or required expansion |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V42_2026-07-12.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_2026-07-13.md`
- `docs/reviews/CVF_SOT3_ACT_A1_SCOPED_KNOWLEDGE_CONTEXT_PRODUCT_ADAPTER_COMPLETION_2026-07-13.md`
- `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`
- all source files cited in the Source Verification Block

## Allowed Scope

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts`
- `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_WORKER_RETURN_2026-07-13.md`

## Forbidden Scope

- `route.ts`, package manifests, lockfiles, generic storage adapters, and the
  knowledge store unless a verified contradiction stops and returns the batch;
- Refinery, Truth Kernel, or Truth Flow package source, tests, schemas, or
  authority semantics;
- database, migration, network store, distributed ledger, public-sync, release,
  deployment, hosted, or production configuration;
- real provider/API invocation, browser E2E, A3-A5 proof, or live receipt;
- provider routing, model selection, DLP, approval, output validation, memory,
  bypass guard, or new whole-request denial behavior;
- visible UI, styling, dashboard, governance checker/hook, Catalog/GAP,
  session, handoff, retained legacy, or unrelated refactor;
- git commit, push, merge, destructive cleanup, or secret disclosure.

## Source Verification Block

Reopen each row before editing. A mismatch requires
`BLOCKED_WITH_REASON` with direct source evidence.

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| SOT3 evaluation occurs before prompt construction | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | `resolveKnowledgeContext` | `resolveKnowledgeContext` | execute knowledge-context helper | ACCEPT |
| Provider call occurs downstream of the helper | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | execute block | `executeAI` | execute route | ACCEPT |
| A1 computes the canonical packet hash | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | packet construction | `computeRefineryPacketHash` | SOT3 knowledge adapter | ACCEPT |
| A1 currently exposes summarized result IDs | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | activation result declaration | `Sot3KnowledgeActivationResult` | SOT3 knowledge adapter | ACCEPT |
| Decision fields are owner-declared | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-decision.ts` | `KernelDecision` | `KernelDecision` | Truth Kernel decision contract | ACCEPT |
| Receipt fields and hash are owner-declared | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-receipt.ts` | `TruthReceipt` | `TruthReceipt` | Truth Kernel receipt contract | ACCEPT |
| Reference scope and lifecycle are owner-declared | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts` | `TruthReference` | `TruthReference` | Truth Kernel reference contract | ACCEPT |
| Flow routing and acknowledgement fields are owner-declared | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/types/distribution-package.ts` | `DistributionPackage` | `DistributionPackage` | Truth Flow distribution contract | ACCEPT |
| Temporary-write then rename pattern exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `_persist` | `_persist` | knowledge store | ACCEPT |
| Existing knowledge-store error swallowing satisfies A2 | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `_persist` catch branch | `_persist` | knowledge store | REJECT |
| Generic direct-write/repair behavior satisfies A2 | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | `FileEventListAdapter` read/write paths | `FileEventListAdapter` | generic storage adapter | REJECT |
| Runtime evidence default is Git-ignored | VALUE_SET | `.gitignore` | runtime ignore entries | `.cvf/runtime/` | repository ignore policy | ACCEPT |
| Provider prompt and call count are test-observable | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts` | route knowledge tests | `executeAIMock` | execute knowledge route test | ACCEPT |

## New Doc-Only Fields

| Proposed field or symbol | Type | Required semantics |
|---|---|---|
| `CVF_SOT3_ACTIVATION_EVIDENCE_PATH` | `DOC_ONLY_NEW` | optional path with default `.cvf/runtime/sot3-activation-evidence.json` |
| `cvf.sot3.activation-evidence.v1` | `DOC_ONLY_NEW` | exact document schema version |
| `Sot3KnowledgeLifecycleTrace` | `DOC_ONLY_NEW` | actual one-per-chunk Source-to-Flow trace |
| `Sot3ActivationEvidenceRecord` | `DOC_ONLY_NEW` | integrity-bound request batch without raw content |
| `DUPLICATE_NOOP` | `DOC_ONLY_NEW` | same identity and integrity yields no write |
| `SOT3_EVIDENCE_DUPLICATE_CONFLICT` | `DOC_ONLY_NEW` | same identity and different integrity rejects |
| `SOT3_EVIDENCE_CORRUPT_STORE` | `DOC_ONLY_NEW` | invalid main file is preserved and blocks read/write |
| `SOT3_EVIDENCE_PERSISTENCE_FAILED` | `DOC_ONLY_NEW` | write or atomic replace failure is propagated |
| `EVIDENCE_PERSISTENCE_FAILED` | `DOC_ONLY_NEW` | route-visible activation failure stage |
| `SOT3_ACTIVATION_EVIDENCE_PERSISTED` | `DOC_ONLY_NEW` | secret-safe audit event for persistence outcome |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A1 accepted material | completion review at `docs/reviews/CVF_SOT3_ACT_A1_SCOPED_KNOWLEDGE_CONTEXT_PRODUCT_ADAPTER_COMPLETION_2026-07-13.md`; commit `149832b16` | `CLOSED_PASS_BOUNDED` and `PRODUCT_PATH_WIRED_LOCAL` | ACCEPT |
| Roadmap routes to A2 | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` at `656c176a2` | top status names A2 packet next | ACCEPT |
| Session front door agrees | generated state and active handoff at `656c176a2` | current mode and next move agree | ACCEPT |

## Implementation Contract

### 1. Evidence Schema And Trace Ownership

- Add one request-level record with stable record ID, request ID, actor ID,
  organization/team scope, activation mode, terminal outcome, failure stage,
  timestamp, diagnostic class, schema version, traces, and integrity hash.
- Extend the adapter to return `Sot3KnowledgeLifecycleTrace[]`; create exactly
  one trace for every evaluated chunk and preserve collection/chunk/source IDs.
- Populate trace data from actual owner outputs: Refinery packet ID and packet
  hash; Kernel decision fields; Truth receipt ID/hash, evidence references,
  policy/rule versions and status; reference ID/scope/version/state/validity;
  Flow package ID, recipient/role/task/phase, references, restrictions,
  routing decision, expiry, and acknowledgement state.
- Do not reconstruct downstream traces from parallel ID arrays. Do not invent
  fields or values absent from actual outputs.
- Define one canonical serialization for record integrity. Exclude the record
  integrity field itself from its hash projection and verify it on every read.
- Persist no raw chunk content, raw reference payload, prompt, provider output,
  API key, bearer token, cookie, or secret.

### 2. Dedicated Atomic Store

- Implement `sot3-activation-evidence-store.ts`; do not adapt the generic
  event-list or knowledge-store failure semantics.
- Resolve `CVF_SOT3_ACTIVATION_EVIDENCE_PATH`; missing or empty uses
  `.cvf/runtime/sot3-activation-evidence.json`.
- Store one versioned document containing the record list. Validate document
  schema and every record integrity hash before lookup or append.
- Serialize append operations within the process to prevent lost updates.
- Write a uniquely named temporary file in the same directory, flush/close it,
  then atomically rename it over the main file. Clean up only the temp file
  created by that failed attempt.
- A missing main file represents an empty store. A leftover temp file is not
  authoritative and must not replace or invalidate a valid main file.
- A corrupt main file must produce `SOT3_EVIDENCE_CORRUPT_STORE`; preserve its
  bytes and do not seed, reset, repair, rename, or overwrite it.
- A write or rename failure must produce
  `SOT3_EVIDENCE_PERSISTENCE_FAILED`, leave any prior main bytes unchanged,
  and propagate to the caller.

### 3. Identity, Duplicate, And Lookup Semantics

- Derive a deterministic record identity from the request-level activation
  identity; record the exact projection in code and tests.
- Existing same identity plus same integrity hash returns `DUPLICATE_NOOP` and
  performs no main-file mutation.
- Existing same identity plus different integrity hash throws
  `SOT3_EVIDENCE_DUPLICATE_CONFLICT` and leaves the main file unchanged.
- Expose read/list or lookup operations sufficient for a fresh store instance
  to retrieve by record ID and request ID after restart.
- Stable sorting and canonical serialization must make replay inspection and
  integrity recomputation deterministic.

### 4. Route Ordering And Mode Policy

- Persist after A1 SOT3 evaluation and before `buildKnowledgeSystemPrompt`.
- `OFF`: perform no SOT3 evaluation and no activation-evidence write.
- `SHADOW`: persist the evaluation record on success; on persistence failure,
  emit a classified secret-safe audit and preserve the A1 raw-context
  downstream contract.
- `ENFORCE`: persist before approved context may be placed into the prompt. On
  persistence failure, set `EVIDENCE_PERSISTENCE_FAILED`, emit classified
  audit, and admit no knowledge block. Preserve A1 policy that the request may
  call the provider mock once without knowledge; do not add whole-request
  denial behavior.
- Emit `SOT3_ACTIVATION_EVIDENCE_PERSISTED` with record ID, request ID, mode,
  disposition, trace count, diagnostic class, and layer IDs only. Never put
  raw context or secrets in audit.
- Make storage dependencies injectable so route tests do not touch shared
  workspace evidence or depend on wall-clock/random values.

### 5. Error And Diagnostic Contract

- Use explicit typed/classified errors rather than unstructured warnings.
- Distinguish corrupt store, duplicate conflict, write/replace failure, and
  record-integrity failure in tests and audit projection.
- Do not retry an unclear persistence failure. A future live-run retry remains
  subject to the mandatory diagnostic standard; A2 itself performs no live
  call.

## Required Test Matrix

| Case | Required result |
|---|---|
| deterministic record | identical semantic input produces identical canonical integrity projection |
| secret/content negative | persisted JSON and audit contain no raw chunk, prompt, provider output, key, or test secret |
| multi-chunk evaluation | exactly one complete trace per evaluated chunk; no cross-chunk ID mixing |
| atomic first write | valid versioned document appears only at the main path after replace |
| restart lookup | fresh store instance retrieves by record ID and request ID and verifies integrity |
| identical duplicate | returns `DUPLICATE_NOOP`; main bytes and record count unchanged |
| conflicting duplicate | throws classified conflict; main bytes unchanged |
| corrupt main JSON | throws corrupt-store class; exact corrupt bytes preserved |
| valid JSON with bad record hash | classified integrity/corrupt result; bytes preserved |
| leftover temp | valid main remains authoritative and readable |
| injected write failure | failure propagates; prior valid main bytes unchanged |
| injected rename failure | failure propagates; prior valid main bytes unchanged |
| concurrent local appends | serialization prevents lost records and produces valid final document |
| `OFF` | no store call and A1 context behavior unchanged |
| `SHADOW` success | evidence stored before prompt build; raw downstream context preserved |
| `SHADOW` persistence failure | classified audit emitted; raw downstream context preserved |
| `ENFORCE` success | approved context reaches provider mock only after durable write succeeds |
| `ENFORCE` persistence failure | no knowledge block; provider mock may run once without knowledge |
| audit inspection | IDs/counts/diagnostic only; no raw content or secret |

## Execution Plan

1. Capture clean execution base and run the pre-implementation gate.
2. Reopen every source row and record any source drift before editing.
3. Define trace, record, canonical integrity, and classified error contracts.
4. Implement the dedicated store test-first for restart, duplicate, corrupt,
   partial-write, and concurrency behavior.
5. Extend the adapter with actual per-chunk lifecycle traces.
6. Wire persistence between evaluation and prompt construction with explicit
   mode behavior and secret-safe audit.
7. Run focused tests, existing route knowledge tests, non-live suite,
   typecheck, build, file-size and worker-return gates.
8. Author the checker-safe worker return and stop with all work uncommitted.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Verification Commands

Run Web commands from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` and
repository governance commands from the root.

```powershell
npx vitest run src/lib/sot3-activation-evidence-store.test.ts src/lib/sot3-knowledge-adapter.test.ts src/app/api/execute/route-knowledge-context.test.ts src/app/api/execute/route.knowledge.test.ts
npm run test:run
npm run check
npm run build
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

If a source-verified script or test filename differs, report the exact
replacement command and reason.

## Acceptance Evidence

Return exact commands, exit codes, test counts, evidence-file temporary paths,
schema/integrity fixture results, restart/duplicate/corrupt/partial-write
outcomes, multi-chunk trace counts, mode/prompt/provider-mock assertions, audit
inspection, ordering evidence, diff, status, and unchanged HEAD.

## Evidence Requirements

Evidence must distinguish a stored activation record from the Truth Kernel
receipt it references. Local filesystem durability proves bounded restart and
replay inspection only; it is not database, distributed, live-provider,
release, or production proof.

## Acceptance Criteria

All paired-baseline criteria and test rows pass; actual trace fields come from
owner outputs; atomic and corrupt-file invariants hold; mode contracts and
ordering hold; no secret/raw content is persisted; changes remain in Allowed
Scope; worker makes no commit.

## Closure Checklist

- REQUIRED: document schema, record identity, canonical hash projection, and
  every diagnostic class are explicit and tested.
- REQUIRED: one actual lifecycle trace exists per evaluated chunk.
- REQUIRED: restart, duplicate, corrupt main, leftover temp, write failure,
  rename failure, and concurrent append tests pass.
- REQUIRED: `OFF`, `SHADOW`, and `ENFORCE` route behavior and ordering pass.
- REQUIRED: persisted and audit payloads contain no raw content or secrets.
- REQUIRED: focused/full non-live tests, typecheck, build, and file-size gate pass.
- REQUIRED: worker-return full gate passes and worker HEAD is unchanged.
- REQUIRED: reviewer independently resolves every item before closure.

## Review Gate

Reviewer must inspect canonical serialization, integrity coverage, identity and
duplicate semantics, actual per-chunk owner bindings, atomic replace and prior
main preservation, corruption handling, process-local concurrency, route
ordering, mode-specific failure behavior, audit secrecy, and test strength
before a material commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with exact source
evidence. Do not broaden scope, consume provider quota, or commit.

## Operator Checkpoint

Stop for a database/distributed durability decision, SOT3 owner semantic
change, new whole-request deny policy, real provider call, production/public
change, visible UI work, or scope outside the listed product files.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work order owner | Output | Verification | Status |
|---|---|---|---|---|
| correlated activation evidence | schema and adapter contracts | request record plus per-chunk traces | fixture and cardinality tests | REQUIRED |
| content and policy integrity | schema contract | packet, receipt, versions, and record hash | integrity recomputation tests | REQUIRED |
| atomic local persistence | dedicated store | temp-write and replace implementation | write/rename/partial tests | REQUIRED |
| restart lookup | dedicated store | record/request lookup | fresh-instance test | REQUIRED |
| duplicate handling | dedicated store | no-op and conflict dispositions | byte-preservation tests | REQUIRED |
| corrupt-file behavior | dedicated store | classified stop with byte preservation | corrupt JSON/hash tests | REQUIRED |
| context-path ordering | route helper | evaluation -> persist -> prompt | injected dependency and provider-mock tests | REQUIRED |
| bounded local claim | review gate | completion evidence | reviewer decision | REQUIRED |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | packet dispatch, bounded implementation, reviewer closure, separate session sync |
| baseHeadFor(phase) | dispatchBaseHead=`656c176a2`; executionBaseHead=worker start HEAD; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact Allowed Scope only |
| traceScope(phase, actor) | worker return records actual manifest and commands; reviewer records independent diff and closure evidence |
| commitOwner(phase) | reviewer/closer for material; session steward for continuity |
| crossBatchIsolation | no A3-A5, live provider, SOT3 package, database, public, UI, governance, or session mutation |
| nextMoveSurfaces | reviewer updates only after accepted evidence and material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_COMPLETION_2026-07-13.md` |
| reviewerOwnedClosurePaths | completion review, accepted baseline/work-order status, roadmap A2 transition, material commit, and separate session continuity |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for its docType, path
family, and conditional content. Derive the exact review headings, trace
labels, no-commit evidence, learning disposition, epistemic block, and
machine-closure-not-applicable shape before authoring.

Required section names: Purpose; Target / Source; Scope / Methodology;
Findings / Position; Risk / Corrective Action; Dependency Release Evidence;
Source Verification Recheck; Checker Source Read-Ahead Block; Agent Operation
Trace Block; Delta Execution Claim Boundary Control Block; Public Export
Disposition; External Knowledge Intake Routing; Rescan Intelligence Hardening;
Corpus Completeness And Report Integrity; Finding-To-Governance Learning
Disposition; Epistemic Process Block; Claim Boundary; git status --short;
Changed Files; Worker Experience Retrospective; Command Evidence; No-Commit
Statement.

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| SOT3 knowledge adapter | expose actual one-per-chunk lifecycle traces without weakening A1 |
| activation evidence store | add versioned, integrity-bound, atomic local persistence and lookup |
| focused store tests | prove deterministic, restart, duplicate, corrupt, partial, concurrency, and secrecy behavior |
| execute knowledge helper | persist before prompt construction with explicit mode/error policy and audit |
| helper and route tests | prove ordering, prompts, call counts, modes, and secret-safe audit |
| worker return | record exact changed set, evidence, limitations, and no-commit status |

Forbidden worker outputs: completion review, roadmap/session/handoff mutation,
live receipt, database, public artifact, or commit.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_WORKER_RETURN_2026-07-13.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact packet paths | `Test-Path` returned false for both A2 packet paths before authoring | CREATE_NEW |
| Batch collision | `rg -n --fixed-strings "SOT3_ACT_A2" docs CVF_SESSION EXTENSIONS` returned no match before authoring | CREATE_NEW |
| Evidence path key collision | `rg -n --fixed-strings "CVF_SOT3_ACTIVATION_EVIDENCE_PATH" docs CVF_SESSION EXTENSIONS` returned no match before authoring | DOC_ONLY_NEW |
| Existing store collision | source review found atomic patterns but no activation-specific store satisfying A2 corruption and failure semantics | CREATE_FOCUSED_OWNER |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | accepted SOT3 architecture -> A1 product path -> A2 durable evidence |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | CVF Web activation-evidence integration |
| Disposition | implement CVF-native evidence without reopening retained legacy |
| Claim boundary | no new external authority or corpus-completeness claim |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| applicability | NOT_APPLICABLE_WITH_REASON |
| reason | A2 operates on already-accepted CVF-native A1/SOT3 outputs and does not rescan or absorb a corpus |
| coverageIndexMutation | none |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024, ADIF-0028, ADIF-0029.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; New Doc-Only Fields; Dependency Release Evidence; Roadmap-to-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Output Checker Read-Ahead Mandate; Planned Worker Fulfillment Manifest; Worker Return Packet Shape Contract; Public Export Disposition |
| gateRunPurpose | confirmation and evidence after direct source and checker review; not first discovery |
| claimBoundary | dispatch compliance does not prove A2 implementation or durable/live behavior |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-ACT-A2 --title "Durable Activation Evidence" --date 2026-07-13 --base 656c176a2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SOT3-ACT-A1 closed at 149832b16" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with verified schema, atomicity, duplicate, corruption, route, test, handoff, and return contracts |
| checkerReadAheadConfirmation | dispatch, handoff, return, trace, public-export, and file-size guards |
| docOnlyNewFields | path/schema, trace/record, persistence dispositions, failure stage, and audit event from paired baseline |
| claimBoundary | dispatch provenance only |

## Dual-Agent Surface Accounting

| Consumer class | Surface | Required treatment |
|---|---|---|
| INTERNAL_AGENT | canonical work order and worker return | exact Allowed Scope, source rows, tests, no-commit route, and reviewer closure |
| EXTERNAL_AGENT_CLI_MCP | operator-transferred prompt or CLI/MCP reading this packet | use this canonical path; no shortened chat prompt may broaden authority or claim live proof |

## Evidence Reuse And Encoding Plan

| Field | Value |
|---|---|
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | A1 completion review supplies dependency release only |
| priorVerificationAnchor | material commit `149832b16`; session-sync commit `656c176a2` |
| freshRecomputeRequired | all A2 tests, hashes, diffs, gates, and source rechecks must be fresh |
| unicodePathHandling | use repository-root working directory and literal PowerShell paths; do not normalize unrelated paths |
| extractedTextAuthority | N/A with reason: no PDF/image/OCR evidence is used |

## Foundation Storage Layout Block

N/A with reason: A2 creates a Git-ignored runtime evidence file and a focused
CVF Web source module. It does not create, split, relocate, or refactor a
durable governance foundation under `docs/reference/`, and therefore requires
no governed foundation folder index or stable reference front door.

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md applicability | N/A with reason: server-side evidence persistence and tests only |
| UI claim boundary | no visible, hosted, production, or live-data claim |

## MCP/CLI Adapter Boundary

| Field | Value |
|---|---|
| Adapter scope | TypeScript server-side evidence adapter in CVF Web only; no MCP or CLI runtime surface |
| No-runtime-overclaim | local tests prove bounded wiring and filesystem behavior only; no command interception or agent-control claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | A2 local durable activation-evidence implementation |
| claimDisposition | CLAIM_REJECTED: no arbitrary execution-control or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: local activation records reference owner receipts but are not live provider or release receipts |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: only local filesystem writes and mocked-provider tests are authorized |
| invocationBoundary | deterministic local tests and build in the private workspace |
| interceptionBoundary | no IDE, shell, git, provider, MCP, or CLI interception |
| claimLanguage | bounded local restart/replay evidence only upon reviewer acceptance |
| forbiddenExpansion | no A3-A5, live provider, public, production, universal control, or user-validation claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private-provenance A2 implementation and local proof only.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_COMPLETION_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | `Status: A2_CLOSED_PASS_BOUNDED_A3_PACKET_NEXT` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/README.md` | existing registry front door | PASS |
| External evidence digest | N/A with reason: local non-live implementation | N/A | N/A with reason |
| System loop interlock | N/A with reason: no automated loop edge | N/A | N/A with reason |
| Session continuity | separate post-material session sync | pending until material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| worker return and reviewer repair satisfy A2 | 71 focused tests; 274 full-suite files and 3207 tests PASS | PASS |
| local evidence record is not a live receipt | A3-A5 remain unclaimed and open | PASS |

## Claim Boundary

Successful reviewer closure may claim
`DURABLE_EVIDENCE_REPLAY_PROVEN_LOCAL`. It cannot claim real-provider behavior,
`LIVE_GOVERNANCE_PROVEN_BOUNDED`, production readiness, distributed durability,
public availability, or real-user validation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | SOT3-ACT-A2 packet authoring, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, scaffold helper, ADIF resolver, patch authoring, dispatch gates |
| Target paths | paired A2 GC-018 and work order |
| Allowed scope source | operator instruction plus A1/roadmap next allowed move |
| Before status evidence | clean worktree at `656c176a2`; exact A2 paths and tokens absent |
| After status evidence | source-verified no-commit A2 implementation packet ready for delegated worker |
| Diff evidence | `git diff --name-status` before packet commit |
| Approval boundary | packet dispatch only; worker cannot commit or perform external invocation |
| Claim boundary | authorizes bounded A2 execution; does not prove it |
| Agent type | dispatcher |
| Invocation ID | `sot3-act-a2-dispatch-2026-07-13` |
| Expected manifest | paired A2 GC-018 and work order |
| Actual changed set | paired A2 GC-018 and work order |
| Manifest delta | MATCH |
