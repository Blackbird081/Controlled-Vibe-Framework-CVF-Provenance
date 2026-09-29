# CVF GC-018 Baseline - MAO-OA-T2 Durable Run Store Replay Recovery And Idempotent Resume

Memory class: FULL_RECORD

Date: 2026-07-16

Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR

GC-018 ID: MAO-OA-T2

Risk class: R1

Commit mode: WORKER_MUST_NOT_COMMIT

Dispatch base: `b5aa0d8a3`

Governing roadmap:
`docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`

Paired work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T2_DURABLE_RUN_STORE_REPLAY_RECOVERY_AND_IDEMPOTENT_RESUME_2026-07-16.md`

## Purpose

Release one bounded execution-plane implementation tranche for durable MAO run
snapshots, deterministic event replay, corruption-safe recovery failure, and
idempotent resume. This baseline does not release worker/provider launch,
heartbeat, timeout, cancellation, reviewer/closer execution, operator UI, or
live proof.

## Baseline Decision

`CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR`.

MAO-OA-T1 is independently accepted at material commit `1bb5ff7f3`. The
operator checkpoint on 2026-07-16 releases T2 authoring and dispatch. Exact
storage authority is source-backed by the canonical MAO runtime foundation:
the execution-plane MAO module owns orchestration state and the append-only
event/receipt ledger is execution truth. OA-16 confirms that no current durable
run-state owner exists, so this tranche creates one owner without replacing the
existing graph compiler or in-memory event ledger.

## Scope / Target / Owner Boundary

Target owner:
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`.

The owner persists immutable task-graph plus append-only event snapshots under
an explicitly supplied local root directory. It restores a run only by
revalidating the graph and replaying persisted events through
`MaoEventLedger`. It never stores secrets, invokes a worker/provider, changes
authority, infers success, writes session/workspace state, or imports the
control plane.

Allowed material families are the new store, the existing MAO local barrel, a
dedicated focused test, one GC-051 source entry and generated corpus aggregate,
and one worker return. T3-T7 remain parked.

## Authority Chain

1. Operator checkpoint in this session releases T2 authoring and dispatch.
2. Governing roadmap T2 row requires durable run store, replay, recovery, and
   idempotent resume after accepted T1 and exact storage authority.
3. MAO runtime foundation contract owns execution-plane state and persistence
   shape.
4. MAO runtime foundation schema owns task graph and event ledger entry shapes.
5. Accepted T1 closure `1bb5ff7f3` proves package discovery and composition
   only; it does not claim durability.
6. This GC-018 and paired work order bound the delegated implementation.
7. Independent reviewer/closer owns acceptance and material commit.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-OA-T1 accepted | completion review and material commit `1bb5ff7f3` | accepted package seam must exist | ACCEPT |
| operator checkpoint | operator said `tiep tuc` on 2026-07-16 after the recorded T1 checkpoint | permits T2 packet authoring and dispatch | ACCEPT |
| storage owner authority | MAO runtime foundation contract Architecture Decisions and Storage And Retention Decision | execution-plane owner plus append-only execution truth must be explicit | ACCEPT |
| current-owner gap | T0 completion review OA-16 records no durable run-state owner | new owner must not be represented as pre-existing source | ACCEPT |
| T3-T7 hold | roadmap keeps execution/liveness, reviewer convergence, operator projection, live proof, and final closure later | no later owner may enter this tranche | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T2 --title "MAO Durable Run Store Replay Recovery And Idempotent Resume" --date 2026-07-16 --base b5aa0d8a3 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T1 accepted closure 1bb5ff7f3" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact storage authority, planned source surface, six-path worker manifest, replay/corruption negatives, GC-051 generation, and closure conversion |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, trace, scaffold, worker-return, epistemic, delta-claim, public-export, corpus-registry, and file-size checker sources reviewed |
| docOnlyNewFields | durable store types and methods listed in the paired work order |
| claimBoundary | dispatch authoring only; no worker execution, provider/live action, public action, or production claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector MAO --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | apply current source verification, generated-registry, no-commit, handoff, and reviewer controls |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| orchestration state belongs to execution-plane MAO | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Architecture Decisions | `Orchestration state owner` | MAO runtime foundation contract | ACCEPT |
| execution truth is append-only event/receipt ledger | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Storage And Retention Decision | `Execution truth` | MAO runtime foundation contract | ACCEPT |
| recovery resumes from durable evidence and never infers success | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Idempotency, Retry, Cancel, And Recovery | `Orphan recovery` | MAO runtime foundation contract | ACCEPT |
| task graph is immutable runtime authority | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | `MaoTaskGraph`; `compileTaskGraph`; `deepFreezeGraph` | `MaoTaskGraph` | task graph contract | ACCEPT |
| current ledger validates authority, graph, task, duplicate key, and state transition | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | `MaoEventLedger.append` | `append` | MAO event ledger | ACCEPT |
| ledger entries contain replay inputs and deterministic sequence | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | `MaoEventLedgerEntry` | `MaoEventLedgerEntry` | MAO event ledger | ACCEPT |
| local MAO barrel is transitively exported by package root | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | export declarations | `src/mao/index.ts` | execution package MAO front door | ACCEPT |
| Node filesystem types are available without dependency change | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | `devDependencies`; `scripts` | `@types/node` | execution package manifest | ACCEPT |
| no durable run-state owner currently exists | LITERAL_INVARIANT | `docs/reviews/CVF_MAO_OA_T0_COMPLETION_REVIEW_2026-07-16.md` | Independent Recomputed Evidence; Findings R1 | `OA-16` | accepted T0 owner audit | ACCEPT |
| T1 proves only package discovery and pure composition | LITERAL_INVARIANT | `docs/reviews/CVF_MAO_OA_T1_COMPLETION_REVIEW_2026-07-16.md` | Findings / Position; Claim Boundary | `REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | accepted T1 completion review | ACCEPT |

## Current Runtime Freshness Verification

Verified at clean dispatch base `b5aa0d8a3` on 2026-07-16.

| Check | Result | Disposition |
|---|---|---|
| `src/mao/durable.run.store.ts` exists | false | create as planned T2 source |
| dedicated durable-store test exists | false | create as planned T2 test |
| execution package has filesystem source usage | no match in current `src` or `tests` | new use remains confined to T2 owner and focused test |
| package manifest supplies Node types | `@types/node` present | no install or manifest edit required |
| execution root line count | 1,418 against 1,450 exception ceiling | do not touch root; export through existing `src/mao/index.ts` |
| worktree | clean | dispatch authoring may proceed |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned baseline path | absent before authoring | CREATE |
| planned work-order path | absent before authoring | CREATE |
| durable run-store source path | absent at `b5aa0d8a3` | CREATE_BY_WORKER |
| current durable-store symbol search | no source match for durable run store, replay, recovery, or resume owner | NEW_OWNER_REQUIRED |
| collision decision | OA-16 and current source agree there is no owner | no duplicate owner |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: T2 creates a new storage owner, so current graph, event-ledger,
filesystem, package, and registry sources must be reread rather than inherited
from T0 or T1 claims.

unicodePathHandling: require literal ASCII repository paths and UTF-8-safe
readers for governed JSON and Markdown.

extractedTextAuthority: N/A with reason

No extracted text is consumed.

rawMemoryReleased=false

The worker must reread current canonical contract and source files. T0/T1
reviews are dependency and boundary evidence only, not substitutes for current
runtime source. No external evidence, extracted text, or provider memory may be
promoted to source authority.

## Required Artifact Manifest

| Artifact | Owner | Required action |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | worker | create bounded file-backed durable store |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | worker | export exact new store types/functions only |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | worker | create focused durability/replay/recovery tests |
| `docs/corpus-intelligence/registry/entries/mao-oa-t2-durable-run-store-surfaces.json` | worker | add narrow GC-051 source coverage |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | worker via generator | regenerate from source entries |
| `docs/reviews/CVF_MAO_OA_T2_WORKER_RETURN_2026-07-16.md` | worker | create no-commit pending-review packet |

## Acceptance Criteria

- durable snapshots contain one immutable graph and an ordered append-only
  event list with an explicit schema version;
- file names are derived safely and never interpolate raw graph IDs as paths;
- initial create refuses conflicting overwrite;
- append validates by rebuilding the current ledger, appending once, and using
  atomic same-directory replacement;
- duplicate idempotency keys do not add a second event or rewrite the snapshot;
- repeated resume is read-only and deeply equal;
- corrupt JSON, schema mismatch, authority mismatch, event tampering, sequence
  gaps, and invalid replay fail closed with typed diagnostics;
- no provider, launcher, heartbeat, timeout, cancellation, reviewer/closer,
  workspace/session, application, network, or environment behavior is added;
- focused tests, package typecheck, GC-051 generation/check, file-size guard,
  pre-implementation gate, and worker-return fast gate pass;
- worker changes exactly six authorized paths and leaves HEAD unchanged.

## Review Gate

Independent reviewer/closer must recompute the snapshot/replay invariants,
inspect every changed line, rerun focused tests and typecheck, verify generated
registry drift and corpus scope, and confirm no later-tranche action entered the
implementation before accepting or committing it.

## Dual Agent Surface Matrix

| Consumer class | Owner surface | Boundary | Disposition |
|---|---|---|---|
| `INTERNAL_AGENT` | execution package MAO durable run-store exports | local durable contract and replay only; no worker/provider action | `BOUNDED_INTERNAL_RUNTIME_COMPONENT` |
| `EXTERNAL_AGENT_CLI_MCP` | no adapter owner | no ingress, authentication, authorization, or remote access | `N/A_WITH_REASON` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T2 work order | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MAO_OA_T2_COMPLETION_REVIEW_2026-07-16.md` | `Status: REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | PASS |
| Roadmap state | governing MAO-OA roadmap | T2 accepted; T3-T7 held | PASS |
| Registry JSON | T2 source entry and generated aggregate | generator and zero-violation coverage checks | PASS |
| Registry Markdown | N/A with reason: GC-051 uses JSON source and aggregate | no separate Markdown registry owner; required JSON registry surfaces updated | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | N/A with reason: T2 does not launch an execution loop | none | N/A with reason |
| Session continuity | reviewer-owned protected sync after material acceptance | separate session-sync commit follows material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Required evidence | Dispatch state |
|---|---|---|
| durable component behavior | 21/21 focused tests plus 1689-test package regression suite | PASS |
| provider acceptance | N/A with reason: provider invocation forbidden | N/A_WITH_REASON |
| reviewer acceptance | independent completion review with bounded malformed-snapshot repair | PASS |
| public acceptance | N/A with reason: no public export authorized | N/A_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; ADIF Defect Registry Disclosure; Source Verification Block; Required Artifact Manifest; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm packet structure and source-backed release before dispatch commit |
| claimBoundary | checker conformance does not prove implementation correctness, durability under production concurrency, provider behavior, or user value |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. No public artifact,
public-sync action, or public claim is authorized.

## Claim Boundary

This baseline releases one bounded local file-backed MAO run-store component
with deterministic replay and fail-closed recovery tests. It does not authorize
or prove distributed concurrency, database durability, crash-proof fsync,
worker/provider launch, liveness control, review/closer execution, automatic
commit or session mutation, operator projection, CLI/MCP/UI ingress, live
governance, public readiness, production readiness, scale, shipment, or value.
