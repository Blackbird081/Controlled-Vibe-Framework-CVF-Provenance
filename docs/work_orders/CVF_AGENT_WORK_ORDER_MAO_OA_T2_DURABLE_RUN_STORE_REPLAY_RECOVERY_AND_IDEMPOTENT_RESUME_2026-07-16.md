# CVF Agent Work Order - MAO-OA-T2 Durable Run Store Replay Recovery And Idempotent Resume

Memory class: FULL_RECORD

Date: 2026-07-16

Status: DISPATCH_READY

Work Order ID: MAO-OA-T2

Risk class: R1

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `b5aa0d8a3`

Paired baseline:
`docs/baselines/CVF_GC018_MAO_OA_T2_DURABLE_RUN_STORE_REPLAY_RECOVERY_AND_IDEMPOTENT_RESUME_2026-07-16.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for MAO-OA-T2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T2_DURABLE_RUN_STORE_REPLAY_RECOVERY_AND_IDEMPOTENT_RESUME_2026-07-16.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse --short HEAD` before any write.

Current-time notes: MAO-OA-T1 is independently accepted at material commit
`1bb5ff7f3`; this T2 packet was authored from clean base `b5aa0d8a3` after the
the human release was recorded.

Do-not-misread notes: this is a local file-backed durable run-store and replay
component only. Do not launch workers, invoke providers, implement heartbeat,
timeout, cancellation, reviewer/closer execution, mutate session/workspace
state, create CLI/MCP/UI surfaces, commit, push, or widen into T3 and later.

Required first actions: read the mandatory startup sequence, guard orientation,
literal gotchas, governing roadmap, paired GC-018, canonical MAO contract and
schema, accepted T1 completion review, exact execution-plane sources below,
package manifest, GC-051 generator/checker source, and every checker named in
the read-ahead block; then capture clean status and `executionBaseHead`.

Return contract: implement exactly the six-path worker manifest, create the
worker return from the checker-safe scaffold, run focused tests, typecheck,
registry generator/check, working-tree gates, and file-size enforcement, leave
all changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Add one execution-plane owner that durably stores immutable MAO task graphs and
append-only event entries, reloads them after a fresh store instance, validates
all persisted authority and event invariants, and resumes read-only without
duplicating events. Preserve all later execution and governance owners.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION`.

Owner: new `src/mao/durable.run.store.ts`, exported only through the existing
`src/mao/index.ts` local barrel. The package root already forwards that barrel,
so `src/index.ts` must not change.

Storage authority: caller supplies a local root directory; the store owns only
files below that root whose names are derived from a deterministic hash of the
task-graph ID. Stored truth is an explicit-version snapshot of one immutable
graph plus ordered event entries. The store must not read environment variables
or select a global/user/session/workspace path.

## Authority Chain

1. Human authorization in this session releases MAO-OA-T2.
2. Governing MAO-OA roadmap defines T2 and keeps T3-T7 held.
3. Canonical MAO runtime foundation contract selects execution-plane ownership,
   append-only execution truth, deterministic replay, and fail-closed recovery.
4. Canonical schema and current TypeScript source own graph/event field names.
5. Accepted T1 completion at `1bb5ff7f3` supplies package discovery but no
   durability claim.
6. Paired GC-018 and this work order define exact worker scope.
7. Independent reviewer/closer recomputes evidence and owns material commit.
8. Session-sync steward owns protected continuity after accepted closure.

Provider-specific memory, `CLAUDE.md`, IDE summaries, and chat paraphrase are
`NOT_CVF_SOURCE` and may not appear as source authority.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| accepted T1 | completion review plus material commit `1bb5ff7f3` | package discovery and pure composition must be closed | ACCEPT |
| human authorization | continuation was released on 2026-07-16 | T2 authoring and dispatch only | ACCEPT |
| exact storage authority | MAO runtime foundation Architecture Decisions and Storage And Retention Decision | execution-plane owner and append-only truth must remain exact | ACCEPT |
| current durable-owner absence | accepted T0 review OA-16 plus current source search | new owner is permitted; duplicate owner is forbidden | ACCEPT |
| current source primitives | `MaoTaskGraph`, `MaoEventLedgerEntry`, and `MaoEventLedger.append` exist | implementation must reuse them | ACCEPT |
| T3-T7 hold | roadmap Work Plan And Dependencies | no later behavior enters worker scope | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T2 --title "MAO Durable Run Store Replay Recovery And Idempotent Resume" --date 2026-07-16 --base b5aa0d8a3 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T1 accepted closure 1bb5ff7f3" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact storage authority, planned source API, six-path manifest, atomic write boundary, corruption/replay negatives, registry generation, and reviewer closure conversion |
| checkerReadAheadConfirmation | all checker paths in Checker Source Read-Ahead Block reviewed before dispatch |
| docOnlyNewFields | T2 planned source symbols listed below; none claimed as current runtime facts |
| claimBoundary | authoring provenance only; no implementation or durability result is claimed by this packet |

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| operator | releases bounded T2 and any later expansion | none in worker phase |
| dispatcher | source-verifies and validates dispatch packet | dispatch packet only |
| worker | implements exact six-path manifest and returns evidence | FORBIDDEN |
| independent reviewer/closer | recomputes storage/replay evidence, repairs only in-scope defects, decides closure | accepted material commit only |
| session-sync steward | updates protected continuity following reviewer acceptance and the material commit | separate continuity commit only |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake type | internal source implementation from canonical MAO contract and accepted roadmap chain |
| scope classification | R1 bounded local TypeScript filesystem component and focused tests |
| risk sensitivity | local filesystem writes below caller-supplied temp/root boundary; no application, provider, network, or external adapter |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| worker route | one delegated implementation worker |
| reviewer route | independent reviewer/closer recomputes snapshot, replay, corruption, scope, and no-commit evidence |
| closer | independent reviewer/closer |
| escalation condition | source contradiction, required forbidden path, unsafe path derivation, concurrency claim expansion, or missing authority |

## Legacy Absorption Coverage Index Disposition

N/A with reason: this is internal MAO roadmap implementation, not legacy or
external-source absorption.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/MCP/readiness claim |
| Chain map route | external source, runtime/provider, MCP, or readiness claims remain `BLOCKED_UNTIL_CVF_PROOF` |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | canonical MAO contract and current execution-plane TypeScript owners |
| Disposition | `NOT_APPLICABLE_WITH_REASON` for external intake; only internal governed sources are authorized |
| Claim boundary | no external absorption, upstream provenance, web knowledge, provider-memory authority, or completeness claim |

## Allowed Scope

Worker may change exactly:

1. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`
2. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
3. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`
4. `docs/corpus-intelligence/registry/entries/mao-oa-t2-durable-run-store-surfaces.json`
5. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`, only by running
   `python governance/compat/generate_corpus_scan_registry.py`
6. `docs/reviews/CVF_MAO_OA_T2_WORKER_RETURN_2026-07-16.md`

Focused tests may create and delete temporary directories only through test
fixtures under the operating-system temporary root. No test artifact may
remain in the repository.

## Forbidden Scope

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts`, package manifests,
  lockfiles, other MAO sources/tests, control-plane source, application source;
- worker/provider launch, delegation adapter wiring, lifecycle heartbeat,
  timeout, cancellation, retry execution, orphan scanning, reviewer/dissent,
  closer/commit, operator readout, CLI/MCP/UI, server, browser, network, live
  provider, environment, secret, or external-root behavior;
- database, daemon, queue, scheduler, watcher, distributed lock, multi-process
  safety, fsync, production durability, migration, retention-policy expansion;
- governance checker, hook, Catalog, GAP, ADIF, session/workspace state, active
  handoff, public-sync, release, certification, commit, push, or registry other
  than the exact GC-051 source entry and generator-owned aggregate above;
- any path outside the six-path manifest.

## Write Ownership

The worker owns only the six pending paths. The reviewer/closer owns the paired
baseline, this work order, governing roadmap, completion review, any allowed
review repair, and material commit. The session-sync steward exclusively owns
`CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and the active handoff following
reviewer acceptance and the material commit.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: startup and continuity
paths are read-only references; this worker has no protected-path mutation
authority.

Protected paths:

- `CVF_SESSION_MEMORY.md` - READ_ONLY_NOT_IN_CHANGED_SET
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` - READ_ONLY_NOT_IN_CHANGED_SET
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` - READ_ONLY_NOT_IN_CHANGED_SET
- active handoff named by state - READ_ONLY_NOT_IN_CHANGED_SET

Operator authorization: none for protected mutation; only the exact six worker
paths in Allowed Scope may change.

Rollback boundary: N/A with reason: the worker must not create a protected-path
diff. Any such diff is removed before handoff without reverting accepted T1
material or the committed T2 dispatch packet.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. active handoff named by state
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. governing roadmap and paired GC-018
8. `docs/reference/multi_agent_orchestration/README.md`
9. `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`
10. `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json`
11. accepted T1 completion review
12. current `task.graph.contract.ts`, `event.ledger.contract.ts`,
    `read.model.contract.ts`, and `src/mao/index.ts`
13. execution package manifest and TypeScript config
14. GC-051 registry generator, coverage checker, and all checker sources named
    in the read-ahead block.

## Pre-Flight Checks

From repository root, before edits:

```powershell
git status --short --untracked-files=all
git rev-parse --short HEAD
Test-Path EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts
Test-Path EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected: empty status output, both planned source/test paths absent, generated corpus
registry aligned, file-size guard PASS, and pre-implementation PASS. Any
unrelated change blocks worker start.

## Operator Checkpoint

Authorization disposition: `SATISFIED_FOR_BOUNDED_T2_IMPLEMENTATION`.

Evidence: after T1 closure and the recorded hold, the human instructed the
dispatcher to continue on 2026-07-16. This releases only the exact T2
manifest and does not release T3-T7 or forbidden behavior.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector MAO --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | current no-commit, source-verification, generated-registry, path-safety, and independent-review controls apply |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| execution-plane MAO owns orchestration state | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Architecture Decisions | `Orchestration state owner` | MAO runtime foundation contract | ACCEPT |
| append-only event/receipt ledger is execution truth | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Storage And Retention Decision | `Execution truth` | MAO runtime foundation contract | ACCEPT |
| recovery resumes only from durable evidence and never silence | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Idempotency, Retry, Cancel, And Recovery | `Orphan recovery` | MAO runtime foundation contract | ACCEPT |
| task graph identity and authority are immutable | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | `compileTaskGraph`; `deepFreezeGraph`; `verifyAuthorityEnvelope` | `MaoTaskGraph` | task graph contract | ACCEPT |
| event entry provides persisted replay fields | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | `MaoEventLedgerEntry` | `MaoEventLedgerEntry` | event ledger contract | ACCEPT |
| append already rejects bad authority, graph, task, duplicate key, and transition | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | `MaoEventLedger.append` | `append` | event ledger contract | ACCEPT |
| ledger defensive read exposes immutable ordered entries | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | `getEntries` | `getEntries` | event ledger contract | ACCEPT |
| MAO local barrel is package-root discoverable | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | current exports and T1 root-adoption comment | `src/mao/index.ts` | execution MAO front door | ACCEPT |
| Node types are available | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | `devDependencies` | `@types/node` | package manifest | ACCEPT |
| current durable owner is absent | LITERAL_INVARIANT | `docs/reviews/CVF_MAO_OA_T0_COMPLETION_REVIEW_2026-07-16.md` | Findings R1 | `OA-16` | accepted T0 review | ACCEPT |

## New Doc-Only Fields

The following are planned T2 source outputs, not pre-existing runtime facts.
They are listed here to prevent the worker from inventing a second API.

| New item | Required shape | Boundary |
|---|---|---|
| `MAO_DURABLE_RUN_SNAPSHOT_SCHEMA_VERSION` | literal `mao-durable-run-snapshot.v1` | exact-version validation; no migration |
| `MaoDurableRunSnapshot` | `schemaVersion`; immutable `graph`; readonly ordered `events` | JSON-safe graph and event truth only |
| `MaoDurableRunStoreFailureReason` | `RUN_ALREADY_EXISTS`; `RUN_NOT_FOUND`; `INVALID_SNAPSHOT_JSON`; `SNAPSHOT_SCHEMA_MISMATCH`; `AUTHORITY_HASH_MISMATCH`; `GRAPH_ID_MISMATCH`; `EVENT_SEQUENCE_INVALID`; `EVENT_REPLAY_REJECTED`; `IO_FAILURE` | typed fail-closed diagnostics; no silent repair |
| `MaoDurableRunStoreFailure` | `ok: false`; exact reason; secret-safe detail | no raw file contents in detail |
| `MaoDurableRunCreateSuccess` | `ok: true`; stored snapshot | create-only; no overwrite |
| `MaoDurableRunAppendSuccess` | `ok: true`; appended entry; stored snapshot | one validated append and atomic replacement |
| `MaoDurableRunResumeSuccess` | `ok: true`; restored graph; readonly replayed entries | read-only; repeated calls equal |
| `MaoFileRunStore` | constructor with explicit `rootDirectory`; async `createRun`, `appendEvent`, and `resumeRun` | no env/global/session path; no provider or launcher |

Result unions may combine the matching success shape with
`MaoDurableRunStoreFailure`. No additional reason tokens or public methods are
authorized without returning to orchestrator.

## Current Runtime Freshness Verification

At `b5aa0d8a3`, the planned store and test paths do not exist; no current
execution-package source/test imports `node:fs`; `@types/node` exists; the local
MAO barrel is already forwarded through the package root; and the execution
root is 1,418/1,450 lines. Therefore this tranche needs no package-root,
manifest, lockfile, install, or exception-registry edit.

## Negative Search And Collision Discipline

| Search target | Result at dispatch | Disposition |
|---|---|---|
| exact T2 baseline and work-order paths | absent before authoring | dispatcher creates once |
| `durable.run.store.ts` and focused test | absent | worker creates once |
| current filesystem use in execution package source/tests | none | keep new use confined to T2 files |
| current durable owner | OA-16 and source search agree absent | new execution-plane owner authorized |
| root export change need | local MAO barrel already root-forwarded | root edit forbidden |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: current graph, event-ledger, filesystem, package, and registry
source must be reread because T2 creates a new owner and prior reviews do not
prove its implementation surface.

unicodePathHandling: require literal ASCII repository paths and UTF-8-safe
readers for governed JSON and Markdown.

extractedTextAuthority: N/A with reason

No extracted text is consumed.

rawMemoryReleased=false

The worker must re-read canonical contracts and current source. Prior reviews
support dependency and boundary facts only. No external or provider-local
content may be reused as implementation authority.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence |
|---|---|---|
| durable run store | persist explicit-version graph-plus-events snapshot below caller root | focused restart test and source review |
| replay | rebuild through current `MaoEventLedger.append` in sequence order | replay equivalence and tamper negatives |
| recovery | fail closed on missing/corrupt/mismatched/tampered state | typed negative tests |
| idempotent resume | resume performs no write and repeated results are equal | byte-stability and deep-equality test |
| no duplicate execution | duplicate idempotency key produces conflict and no second event | duplicate append test |
| exact storage authority | execution-plane owner; append-only truth; no workspace/session storage | import/path inspection |
| T3-T7 held | no worker/provider/liveness/reviewer/operator/live behavior | manifest and forbidden-token inspection |

## Worker Autonomy / No-Question Rule

Repair allowed-scope source, test, registry, typecheck, and gate failures by
reading the failing owner/checker and rerunning. Return to orchestrator only if
completion requires a forbidden path, new public method/reason token, a later
tranche owner, unsafe path expansion, or source contradiction.

## Design Control Carry-Forward

| Control | Required implementation disposition |
|---|---|
| state owner | new store remains execution-plane MAO only |
| graph authority | persist and revalidate exact immutable graph; never recompile or rewrite authority |
| event truth | persist append-only event entries; replay only through current ledger owner |
| path authority | explicit caller root plus deterministic hashed filename; no raw graph ID path interpolation |
| atomicity | write complete JSON to a unique same-directory temporary file, then rename; clean temporary file on failure where safe |
| corruption | no auto-repair, partial acceptance, success inference, or migration |
| idempotency | duplicate key never creates a second event or rewrites persisted truth |
| determinism | stable JSON formatting and sequence ordering; repeated resume is read-only |
| maintainability | dedicated source/test files; do not touch near-limit package root |
| secrecy | no prompt, secret, environment, or provider-private data |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| storage owner | execution-plane `MaoFileRunStore` |
| root authority | explicit constructor input from caller; no implicit path |
| file identity | deterministic hash of taskGraphId plus `.json`; raw ID never becomes path segment |
| persisted shape | exact schema version, immutable graph, ordered event entries |
| write discipline | create-only initial write and atomic same-directory replacement for append |
| read discipline | bounded JSON parse, exact version/graph/authority validation, sequential ledger replay |
| generated aggregate | only GC-051 corpus aggregate, generated from its source entry; not runtime truth |
| retention/deletion | N/A with reason: T2 adds no delete, archive, pruning, or retention policy |
| concurrency | N/A with reason: multi-process locking and distributed concurrency are outside bounded claim |

## Required Durable Store Contract

1. Constructor accepts one non-empty root directory and performs no I/O.
2. `createRun(graph)` verifies authority, creates the root when needed, refuses
   an existing run, and atomically writes the versioned zero-event snapshot.
3. File identity uses deterministic hashing; raw graph IDs cannot escape or
   shape the filesystem path.
4. `resumeRun(taskGraphId)` reads without writing, validates JSON/version,
   graph identity and authority, validates contiguous sequences starting at 1,
   replays each event in order through a fresh `MaoEventLedger`, and requires
   replayed entries to match persisted event ID and fields exactly.
5. `appendEvent(taskGraphId, input)` first performs the same validated replay,
   invokes current ledger append exactly once, returns a typed failure without
   writing on rejection, and atomically replaces the snapshot on success.
6. Duplicate idempotency key is rejected through existing ledger semantics;
   snapshot bytes and event count remain unchanged.
7. All failure details are secret-safe and do not echo raw persisted content.
8. No method deletes, migrates, repairs, launches, retries, or infers success.

## Work-Order Fulfillment Manifest

| Artifact | Owner | Dispatch disposition |
|---|---|---|
| paired T2 GC-018 baseline | dispatcher | present and source-verified |
| this T2 work order | dispatcher | present and dispatch-ready |
| governing MAO-OA roadmap | dispatcher | T2 route updated; T3-T7 held |
| six worker paths listed below | delegated worker | pending implementation |
| T2 completion review | independent reviewer/closer | N/A with reason: created only after worker return |
| protected session continuity | session-sync steward | N/A with reason: separate batch only after accepted material commit |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | create exact bounded store and planned API |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | export exact planned values/types/class; no unrelated edit |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | focused positive, restart, idempotency, path, and corruption tests |
| `docs/corpus-intelligence/registry/entries/mao-oa-t2-durable-run-store-surfaces.json` | create narrow source entry covering new source/test paths |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate only through canonical generator |
| `docs/reviews/CVF_MAO_OA_T2_WORKER_RETURN_2026-07-16.md` | record exact no-commit pending-review evidence |

## Execution Plan

1. Complete first reads and pre-flight; stop on dirty/unrelated state.
2. Implement the dedicated store with planned API and no other exports.
3. Add focused tests covering create, fresh-instance replay, append-after-resume,
   repeated read-only resume, duplicate key, safe path derivation, missing run,
   corrupt JSON, schema mismatch, authority mismatch, graph mismatch, sequence
   gap, event tamper, invalid transition, and temporary-file cleanup.
4. Export only through `src/mao/index.ts`.
5. Add the exact GC-051 source entry and run the canonical generator.
6. Run focused test, typecheck, registry checks, diff/file-size checks, and
   pre-implementation gate; repair only allowed-scope failures.
7. Create the worker return with the canonical scaffold, fill all required
   sections, rerun the worker-return fast gate, record actual pending status,
   and stop without commit.

## Worker Output Checker Read-Ahead Mandate

Before authoring the worker return, read checker source for review structure,
worker-return quality, trace, delta claim, epistemic process, corpus completeness,
rescan, finding-to-governance, public export, generated registry, and file size.

Required review headings include: Purpose; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Disposition; External Knowledge Intake
Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity;
Finding-To-Governance Learning Disposition; Epistemic Process Block; Checker
Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim
Boundary Control Block; Machine Closure Package; Public Export Disposition;
Claim Boundary; Changed Files; Command Evidence; git status --short; Worker
Experience Retrospective; No-Commit Statement.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_OA_T2_WORKER_RETURN_2026-07-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Create it before long-form drafting:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MAO_OA_T2_WORKER_RETURN_2026-07-16.md --title "CVF MAO-OA-T2 Worker Return"
```

The return must state the actual six pending paths, unchanged HEAD, and
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`; it must not claim closure,
committed-range proof, or a clean worktree.

## Agent Handoff Contract Control Block

Contract source stable front door: `docs/reference/agent_handoff/README.md`

Contract source archive-named canonical exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> implementation worker -> independent reviewer/closer -> session-sync steward |
| phase | pre-dispatch to pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=`b5aa0d8a3`; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer sets before material commit |
| changedSetScope(phase) | worker may change exactly six listed paths; dispatcher owns baseline, work order, and roadmap dispatch state; reviewer owns closure conversion |
| traceScope(phase, actor) | each actor records only its own commands, paths, and changed-set evidence |
| commitOwner(phase) | worker forbidden; reviewer/closer owns material commit; session-sync steward owns separate continuity commit |
| crossBatchIsolation | no T3-T7, SOT3-APP, other absorption, worker/provider/live/public, session, Catalog, GAP, ADIF, checker, or external-root work |
| nextMoveSurfaces | unchanged by worker; reviewer/closer and session-sync steward update only after acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_OA_T2_COMPLETION_REVIEW_2026-07-16.md` |
| reviewerOwnedClosurePaths | paired GC-018, this work order, worker six-path output, completion review, governing roadmap, and separate protected session-sync surfaces |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | package-root-transitive `MaoFileRunStore` | local explicit-root durable component; no execution launch or authority widening | source, focused temp-directory tests, typecheck, independent review | internal TypeScript API | `BOUNDED_INTERNAL_RUNTIME_COMPONENT` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no ingress, auth, remote path, body read, or mutation authority | no adapter artifact | external adapter parked | `N/A_WITH_REASON` |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: current immutable graph and append-only ledger
primitives can support deterministic local file-backed persistence and replay
without changing authority or introducing an execution launcher.

Evidence Comparison Requirement: compare source diff, persisted bytes, fresh-
instance replay, negative corruption tests, duplicate-key byte stability,
typecheck, registry evidence, and forbidden-import/action inspection with the
prediction.

Contradiction Handling Requirement: inability to replay through current ledger,
need for a later-tranche owner, unsafe path behavior, or unresolvable source
conflict requires `BLOCKED_WITH_REASON`; do not add a bypass.

Claim Update Requirement: worker and reviewer state whether the prediction was
confirmed, narrowed, revised, or invalidated.

## Verification Commands

From `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION`:

```powershell
npm test -- tests/mao.durable.run.store.test.ts
npm run check
```

From repository root:

```powershell
python governance/compat/generate_corpus_scan_registry.py
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_changed_corpus_registry_coverage.py --base <executionBaseHead> --head HEAD --enforce
git diff --check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts
git diff --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

Do not install dependencies or run application, server, browser, provider,
release bundle, public-sync, commit, or push commands.

## Evidence Requirements

- exact `executionBaseHead`, unchanged final HEAD, and clean pre-edit status;
- six-path `git diff --name-status` and actual pending `git status`;
- focused pass count and TypeScript check exit code 0;
- temp-directory evidence for fresh-store replay and no repository artifacts;
- before/after snapshot bytes proving duplicate key and repeated resume do not
  mutate truth;
- typed failures for every required corruption/tamper negative;
- source inspection proving no control-plane, delegation, lifecycle, reviewer,
  closer, provider, network, environment, workspace, or session import;
- corpus source entry, generator check, coverage check, file-size guard,
  pre-implementation gate, and worker-return fast-gate results;
- explicit no-commit statement.

## Acceptance Criteria

- planned API and reason vocabulary are implemented exactly;
- snapshot schema version is exact and required on every load;
- graph authority and identity are verified before event replay;
- replay requires contiguous sequence and exact reconstructed event equality;
- create never overwrites an existing run;
- successful append uses atomic same-directory replacement;
- rejected append, duplicate key, and resume perform no write;
- raw graph IDs cannot create or traverse filesystem paths;
- all required positive and negative tests pass without repository residue;
- local barrel exports new surface without root/package edits;
- GC-051 source entry and generated aggregate are aligned and cover new files;
- focused test, typecheck, diff, file-size, pre-implementation, and worker-return
  gates pass;
- exactly six paths remain pending and worker HEAD is unchanged.

Fail conditions:

- any persisted field, method, reason token, or owner differs from the planned
  contract without orchestrator release;
- replay bypasses current ledger validation or silently repairs evidence;
- any raw taskGraphId becomes a path segment or storage escapes caller root;
- any later-tranche, provider/live, session/workspace, public, commit, or
  unlisted path enters the diff;
- any required test/check/gate remains failed.

## Review Gate

Implementation may begin only from committed dispatch state after
pre-dispatch passes on the real material range. Closure requires independent
review of all source and persisted invariants, rerun of focused tests/typecheck/
registry/file-size gates, exact manifest proof, reviewer-owned completion
review, material commit, and committed-range pre-closure PASS.

Worker handoff is not closure.

## Closure Diff Gate

Reviewer compares roadmap T2 row, canonical storage/recovery decisions, paired
GC-018, this work order, six-path worker diff, focused evidence, worker claims,
completion review, and final roadmap/session state. Every item must be PASS,
N/A with reason, or BLOCKED with return action.

## Closure Checklist

| Item | Required closure disposition |
|---|---|
| exact six-path worker set | reviewer recomputed |
| storage authority and path boundary | reviewer proven |
| graph and event replay integrity | reviewer proven |
| corruption and duplicate negatives | reviewer rerun |
| focused tests and typecheck | reviewer rerun |
| GC-051 source/aggregate alignment | reviewer rerun |
| file-size and governance gates | reviewer rerun |
| no worker commit | reviewer verified |
| roadmap and session continuity | reviewer/closer plus session-sync steward only |
| public export | DEFERRED_PRIVATE_ONLY unless separately authorized |

## Reviewer Closure Decision

N/A with reason: pending worker implementation and independent review. This
dispatch packet makes no acceptance or closure decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Dispatch status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | planned T2 completion review | reviewer-owned after worker return | N/A with reason |
| Roadmap state | governing MAO-OA roadmap | T2 dispatched; T3-T7 held | PASS |
| Registry JSON | T2 source entry and generated aggregate | worker generator and reviewer check | N/A with reason |
| Registry Markdown | N/A with reason: GC-051 uses JSON source and aggregate | no separate Markdown owner | N/A with reason |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | N/A with reason: no launcher or runtime loop | none | N/A with reason |
| Session continuity | protected sync following reviewer acceptance and the material commit | worker forbidden | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Required evidence | Dispatch state |
|---|---|---|
| durable behavior | focused local temp-directory tests | PENDING_WORKER |
| provider acceptance | N/A with reason: provider invocation forbidden | N/A_WITH_REASON |
| reviewer acceptance | independent completion review | PENDING_REVIEW |
| public acceptance | N/A with reason: no public action | N/A_WITH_REASON |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without scope expansion when:

- required implementation needs any path outside Allowed Scope;
- current graph/event source contradicts a planned invariant;
- safe hashed path confinement or atomic same-directory replacement cannot be
  implemented within the exact owner;
- replay requires bypassing `MaoEventLedger` or changing existing ledger code;
- a new reason token/public method, package dependency, install, database,
  lock, migration, retention, or later-tranche owner becomes necessary;
- unrelated worktree changes appear;
- a worker commit occurs or is required.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dispatch Prompt Envelope; Role:; Canonical packet:; Commit mode:; executionBaseHead; Current-time notes:; Do-not-misread notes:; Required first actions:; Return contract:; Dependency Release Evidence; Scaffold Provenance Block; ADIF Defect Registry Disclosure; Source Verification Block; New Doc-Only Fields; Current Runtime Freshness Verification; Negative Search And Collision Discipline; Evidence Reuse And Encoding Plan; Roadmap-To-Work-Order Trace Matrix; Worker Autonomy / No-Question Rule; Design Control Carry-Forward; Foundation Storage Layout Block; Required Artifact Manifest; Execution Plan; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Epistemic Process Block; Verification Commands; Acceptance Criteria; Review Gate; Closure Diff Gate; Machine Closure Package; Return-To-Orchestrator Conditions; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm exact source-backed T2 dispatch and worker-return contract before material commit |
| claimBoundary | checker conformance does not prove implementation correctness, production durability, concurrency safety, provider behavior, or value |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | Codex local private provenance workspace |
| Session or invocation | MAO-OA-T2 dispatch authoring, 2026-07-16 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, ADIF resolver, scaffold preview, apply_patch, governance gates, git |
| Target paths | governing roadmap; paired T2 GC-018; this T2 work order |
| Allowed scope source | human continuation instruction, active next move, governing roadmap, canonical MAO contract, accepted T1 closure |
| Before status evidence | clean worktree at `b5aa0d8a3`; planned T2 packet/source paths absent |
| After status evidence | exact three-path dispatch packet pending verification and material commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; pre-dispatch range from `b5aa0d8a3` |
| Approval boundary | T2 local durable run-store implementation dispatch only |
| Claim boundary | no worker execution, source implementation, provider/live/public action, or production claim by dispatcher |
| Agent type | dispatcher |
| Invocation ID | `mao-oa-t2-dispatch-2026-07-16` |
| Expected manifest | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T2_DURABLE_RUN_STORE_REPLAY_RECOVERY_AND_IDEMPOTENT_RESUME_2026-07-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T2_DURABLE_RUN_STORE_REPLAY_RECOVERY_AND_IDEMPOTENT_RESUME_2026-07-16.md` |
| Actual changed set | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T2_DURABLE_RUN_STORE_REPLAY_RECOVERY_AND_IDEMPOTENT_RESUME_2026-07-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T2_DURABLE_RUN_STORE_REPLAY_RECOVERY_AND_IDEMPOTENT_RESUME_2026-07-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local explicit-root file-backed MAO graph/event persistence and deterministic replay component |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE after focused tests and independent review only |
| receiptEvidence | CVF_RECEIPT_PRESENT only as persisted MAO graph/event contract entries; no provider or action receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT only for bounded temp-directory filesystem tests; no worker/provider/application action |
| invocationBoundary | package-local focused tests, typecheck, temp-directory filesystem I/O, registry generation, and governance checks |
| interceptionBoundary | no IDE/shell/git/provider interception, wrapper/proxy enforcement, runtime gate, or agent coding control claim |
| claimLanguage | bounded internal durable component with validated replay; not an operational orchestrator |
| forbiddenExpansion | no T3-T7, worker/provider/live/public, lifecycle/reviewer/closer, package-manifest, Web/MCP, session, Catalog/GAP/ADIF/checker work |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. No public artifact,
public-sync operation, or public claim is authorized.

## Claim Boundary

This work order authorizes exactly one bounded local file-backed MAO run-store
owner, local-barrel exports, focused temp-directory tests, narrow GC-051 source
and generated aggregate coverage, and a no-commit worker return. It does not
authorize or prove distributed/multi-process concurrency, database durability,
fsync guarantees, migrations, retention, worker/provider launch, heartbeat,
timeout, cancellation, retry execution, reviewer/closer convergence, automatic
commit/session mutation, operator projection, CLI/MCP/UI ingress, live
governance, public or production readiness, scale, shipment, or user value.
