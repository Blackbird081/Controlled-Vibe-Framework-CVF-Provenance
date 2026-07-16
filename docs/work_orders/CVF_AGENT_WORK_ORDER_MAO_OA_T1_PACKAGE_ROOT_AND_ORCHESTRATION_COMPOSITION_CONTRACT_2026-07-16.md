# CVF Agent Work Order - MAO-OA-T1 Package Root And Orchestration Composition Contract

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-07-16

Batch ID: MAO-OA-T1

dispatchBaseHead: `233e1ab98`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated implementation worker for MAO-OA-T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse --short HEAD` before any write.

Current-time notes: MAO-OA-T0 is independently accepted at material commit
`2de211da0`; this T1 dispatch packet was authored from clean base `233e1ab98`.

Do-not-misread notes: this is package-root and pure deterministic composition
work only. Do not launch workers, invoke providers, add storage, run the
application, mutate session state, create CLI/MCP/UI surfaces, commit, push, or
widen into MAO-OA-T2 and later.

Required first actions: read the mandatory startup sequence, guard orientation,
literal gotchas, governing roadmap, paired GC-018, accepted T0 matrix and
completion review, the exact source files named below, both package manifests,
the file-size exception entry, and every checker source named in the read-ahead
block; then capture clean status and `executionBaseHead`.

Return contract: implement exactly the allowed manifest, create the worker
return, run focused tests, typechecks, working-tree gates, and file-size
enforcement, leave all changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Make the existing MAO graph compiler and role resolver discoverable from their
package roots and add one minimal pure composition function that compiles a
graph and derives its role-admission receipt. Preserve all current authority,
risk, and failure decisions without adding execution behavior.

## Scope / Target / Owner Boundary

The worker owns exactly nine source/test paths and one worker-return path. The
dispatcher owns this work order, paired GC-018, and roadmap dispatch
transition. The independent
reviewer/closer owns repair decisions, the completion review, material commit,
roadmap transition, and closure conversion. The session-sync steward owns a
separate continuity batch only after reviewer acceptance.

## Authority Chain

| Authority | Path / evidence | Disposition |
|---|---|---|
| operator implementation direction | operator instruction on 2026-07-16 to create the work order for delegated implementation | ACCEPT |
| active next move | `CVF_SESSION/state/entries/nextAllowedMove.json` | ACCEPT |
| governing roadmap | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md` | ACCEPT |
| T0 completion review | `docs/reviews/CVF_MAO_OA_T0_COMPLETION_REVIEW_2026-07-16.md`; `2de211da0` | ACCEPT |
| accepted T0 owner/gap matrix | `docs/reviews/CVF_MAO_OA_T0_OPERATIONAL_ADOPTION_OWNER_AND_GAP_MATRIX_2026-07-16.md`, Accepted T1 Packet Boundary | ACCEPT |
| paired GC-018 | `docs/baselines/CVF_GC018_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md` | ACCEPT |
| MAO reference front door | `docs/reference/multi_agent_orchestration/README.md` | ACCEPT |
| active handoff | `AGENT_HANDOFF_V45_2026-07-16.md` | ACCEPT |

Authority boundary: provider-local memory, chat summaries, IDE side channels,
and archived handoffs are not CVF source authority. Recompute every source
fact from current governed files.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-OA-T0 accepted | completion review at `2de211da0` records reviewer acceptance with bounded repairs | exact accepted artifact and commit exist | ACCEPT |
| T1 minimal boundary accepted | T0 matrix lines 242-261 defines two root exports, one pure composition owner, focused tests, and strict exclusions | worker scope must match this boundary | ACCEPT |
| implementation owner direction | operator requested this governed work order on 2026-07-16 | validated GC-018 plus work order releases bounded worker execution | ACCEPT |
| T2-T7 hold | roadmap rows keep durable state, worker launch, review convergence, operator projection, live value proof, and final closure in later tranches | worker must not absorb later owners | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T1 --title "MAO Package Root And Orchestration Composition Contract" --date 2026-07-16 --base 233e1ab98 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T0 accepted closure 2de211da0" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-backed composition interface, ten-path worker manifest, worker-return contract, package-root maintainability control, exact negatives, and closure conversion |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, trace, scaffold, worker-return, epistemic, delta-claim, public-export, and file-size checker sources reviewed |
| docOnlyNewFields | graphInput; receiptId; graphResult; roleResolution; composeOrchestrationPlan |
| claimBoundary | dispatch authoring provenance only; no worker execution, runtime, provider, live, public, Web, or MCP claim |

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| operator | authorizes the bounded tranche and any later scope expansion | none in worker phase |
| dispatcher | authors and validates GC-018 plus work order | dispatch packet only |
| worker | implements exact allowed source/test manifest and returns evidence | FORBIDDEN |
| independent reviewer/closer | recomputes evidence, repairs only allowed-scope defects, decides closure, and commits accepted material | material closure only |
| session-sync steward | updates active continuity after accepted material closure | separate continuity commit only |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake type | internal source implementation from accepted governed roadmap evidence |
| scope classification | R1 bounded internal TypeScript contract implementation and focused tests |
| risk sensitivity | R1; no runtime action, provider call, durable state, public surface, or external adapter authority |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| worker route | one delegated implementation worker |
| reviewer route | independent reviewer/closer recomputes source, test, and boundary evidence |
| closer | independent reviewer/closer |
| escalation condition | source contradiction, required forbidden-path change, missing dependency authority, or inability to preserve the pure no-side-effect boundary |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | MAO-OA-T1 implements a current governed package-root and composition seam; it does not ingest, rescan, map, or absorb legacy or external source content |
| Legacy path mutation | FORBIDDEN |
| Claim boundary | current MAO source implementation only; no legacy completeness or absorption claim |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/MCP/readiness claim |
| Chain map route | positive runtime, provider, MCP, or readiness claims remain `BLOCKED_UNTIL_CVF_PROOF`; this packet uses only negative boundaries and current CVF source authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | current MAO execution-plane and control-plane package contracts |
| Disposition | BLOCKED_UNTIL_CVF_PROOF for every positive runtime/provider/MCP/readiness claim; T1 authorizes contract-only source work |
| Claim boundary | no external knowledge intake, absorption, provenance, completeness, or upstream-source claim |

## Allowed Scope

The worker may modify only:

1. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts`
2. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
3. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts`
4. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts`
5. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts`
6. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.mao.barrel.ts`
7. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts`
8. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/orchestration.composition.contract.ts`
9. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.orchestration.composition.contract.test.ts`
10. `docs/reviews/CVF_MAO_OA_T1_WORKER_RETURN_2026-07-16.md`

Read-only commands against governed source, package-local tests, TypeScript
checks, Git metadata, and governance gates are allowed.

## Forbidden Scope

- every path not listed in Allowed Scope;
- both legacy cumulative `tests/index.test.ts` files;
- package manifests, locks, dependencies, generated aggregates, session state,
  handoff, roadmap, Catalog, GAP, ADIF, checkers, hooks, public-sync, source
  mirrors, and external roots;
- event/evidence ledger, durable storage, replay, recovery, queue, scheduler,
  delegation adapter, lifecycle controller, reviewer/dissent/closer/readout
  owner changes;
- worker/provider launch, server/browser/application execution, live proof,
  network call, CLI/MCP/UI work, dependency install, commit, or push.

## Write Ownership

| Path family | Worker action | Boundary |
|---|---|---|
| execution-plane source | add one root forwarder and update only comments made stale by that export | no new execution owner |
| execution-plane dedicated test | create root discoverability proof | do not edit legacy cumulative test |
| control-plane source | add one domain barrel, one pure composition contract, root forwarder, and truthful resolver comment | no provider/runtime owner |
| control-plane dedicated test | create deterministic composition and negative proof | no application or live run |
| worker return | create exact pending-review evidence packet | no completion review or closure claim |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V45_2026-07-16.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order and paired GC-018
- governing roadmap, accepted T0 matrix, and T0 completion review
- every source, test, package manifest, and exception-registry entry named in
  Source Verification Block
- every checker source named in Checker Source Read-Ahead Block

## Pre-Flight Checks

Before editing, the worker must record:

```powershell
git rev-parse --short HEAD
git status --short
```

The worktree must be clean, and HEAD must contain the committed T1 dispatch
packet. If either condition is false, return `BLOCKED_WITH_REASON` without
absorbing unrelated changes.

## Operator Checkpoint

Checkpoint disposition: `SATISFIED_FOR_BOUNDED_T1_IMPLEMENTATION`.

Evidence: the operator requested creation of this delegated implementation
work order on 2026-07-16. This does not authorize any forbidden or later-tranche
scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`orchestration contract implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "orchestration contract implementation" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | use active source-verification, handoff, worker-return, file-size, and no-commit controls |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| execution package public entrypoint is `src/index.ts` | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | `main` and `types` | `src/index.ts` | execution-plane package surface | ACCEPT |
| execution MAO local barrel exports compiler types and functions | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | lines 23-50 | `compileTaskGraph` | execution-plane MAO local barrel | ACCEPT |
| graph input contains authority, tasks, optional dependencies, and compiler version | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | lines 73-78 | `MaoTaskGraphInput` | MAO task graph contract | ACCEPT |
| graph compiler returns a typed success or failure result | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | lines 80-108 and 284-355 | `MaoGraphCompileResult` | MAO task graph contract | ACCEPT |
| execution root has no current MAO export | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | complete file token search at `233e1ab98` | `src/index.ts` | execution-plane package root | ACCEPT |
| execution root exception allows at most 1,450 lines and requires domain splitting | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | exception entry for execution root | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | governed file-size exception registry | ACCEPT |
| control package public entrypoint is `src/index.ts` | VALUE_SET | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/package.json` | `main` and `types` | `src/index.ts` | control-plane package surface | ACCEPT |
| control root forwards domain barrels | LITERAL_INVARIANT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts` | lines 1-11 | `src/index.ts` | control-plane package root | ACCEPT |
| resolver input is a compiled graph plus deterministic receipt seed | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | lines 52-67 | `MaoRoleResolverInput` | MAO role resolver | ACCEPT |
| resolver is pure, provider-neutral, fail-closed, and preserves approval-required decisions | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | lines 157-188 and 350-357 | `resolveRole` | MAO role resolver | ACCEPT |
| existing focused tests cover compiler and resolver directly | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.task.graph.state.contract.test.ts` | lines 1-90 | `compileTaskGraph` | task-graph focused test | ACCEPT |
| existing resolver test imports current owners directly | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.role.resolver.contract.test.ts` | lines 1-90 | `resolveRole` | role-resolver focused test | ACCEPT |

## New Doc-Only Fields

These names are authorized new T1 contract outputs. They are not represented as
pre-existing source facts in Source Verification Block.

| New item | Required shape | Owner path | Boundary |
|---|---|---|---|
| `MaoOrchestrationCompositionInput` | `graphInput: MaoTaskGraphInput`; `receiptId: string` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/orchestration.composition.contract.ts` | no callback, adapter, provider, storage, or runtime dependency |
| `MaoOrchestrationCompositionResult` | `graphResult: MaoGraphCompileResult`; `roleResolution: MaoRoleResolutionReceipt` or `null` | same owner | graph failure keeps role resolution null |
| `composeOrchestrationPlan` | compile first; resolve only on compile success; return frozen deterministic result | same owner | no task launch or state mutation |

No additional reason-code vocabulary is authorized. Graph failures must reuse
`MaoGraphCompileResult`; role decisions must reuse
`MaoRoleResolutionReceipt`, including `REJECTED` and
`OPERATOR_APPROVAL_REQUIRED`.

## Current Runtime Freshness Verification

At `233e1ab98`, neither package root exports MAO. The execution local barrel
already exports the graph compiler. The control role resolver imports the graph
types from execution plane and is the existing admission owner. No composition
contract or planned dedicated test file exists.

The execution root is 1,415 lines and has an active 1,450-line exception. Its
T1 change must be exactly one forwarding export through the existing MAO local
barrel. No source export list may be duplicated in the root.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| dispatch paths | paired GC-018 and work-order paths returned `False` before authoring | NO_COLLISION |
| worker output paths | all new worker-return, source, barrel, and test paths returned `False` before authoring | NO_COLLISION |
| execution root MAO token | no match at dispatch base | BOUNDED_WIRING_REQUIRED |
| control root MAO token | no match at dispatch base | BOUNDED_WIRING_REQUIRED |
| composition owner token | no existing owner found | NEW_DOC_ONLY_OWNER_AUTHORIZED |
| duplicate-owner rule | second graph compiler, resolver, event/evidence ledger, adapter, lifecycle, reviewer, closer, or readout owner forbidden | PASS_BOUNDARY |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: the worker must verify the current package roots, owner type
signatures, import direction, file-size exception, and test commands at its
captured execution base before changing source.

priorVerificationArtifact: accepted T0 matrix and completion review are boundary
inputs only.

priorVerificationAnchor: `2de211da0`.

freshRecomputeRequired: package roots, import direction, type names, comment
truthfulness, test behavior, line counts, and exact changed set.

unicodePathHandling: use literal repository-relative paths and UTF-8-safe
readers; author all new source, test, and review text in ASCII.

extractedTextAuthority: current CVF-governed source is authoritative; provider
memory and chat paraphrases are `NOT_CVF_SOURCE`.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence |
|---|---|---|
| root/package adoption seam | forward execution MAO local barrel and control MAO domain barrel through package roots | package-root imports in focused tests |
| one orchestrator contract | implement only `composeOrchestrationPlan` with current graph and resolver owners | deterministic focused composition tests |
| no duplicate foundation owners | reuse current result types and owner functions | source diff plus forbidden-import test |
| accepted graph and role admission | compile then resolve | accepted R1 case |
| authority/risk negatives | preserve graph failure, resolver rejection, and R3 approval-required result | three focused negative cases |
| no runtime action | forbid adapter, ledger, lifecycle, reviewer, closer, provider, storage, UI, CLI, or MCP imports | source inspection plus negative import test |
| later owners remain held | do not add T2-T7 behavior | changed-set review and claim boundary |

## Worker Autonomy / No-Question Rule

Repair allowed-scope source, test, typecheck, and checker failures directly by
reading the failing source and matching its contract. Return to orchestrator
only when completion requires a forbidden path, contradicts an accepted source
fact, or lacks authority that cannot be resolved inside this packet.

## Design Control Carry-Forward

| Control | Required implementation disposition |
|---|---|
| graph owner | reuse `compileTaskGraph`; do not wrap it with a second compiler |
| admission owner | reuse `resolveRole`; do not duplicate risk policy |
| dependency direction | composition owner belongs in control plane, which may consume execution-plane graph surface; execution plane must not import control plane |
| result truth | preserve compile failures, resolver rejection, and approval-required outcomes exactly |
| determinism | two independent calls with the same immutable input produce deeply equal output; returned top-level result is frozen |
| no side effect | no callbacks, clocks, I/O, env reads, storage, network, adapter, event ledger, or lifecycle ownership |
| maintainability | execution root forwards its existing domain barrel in one line; all new tests are dedicated files |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durable storage | N/A with reason: MAO-OA-T2 owns storage authority |
| in-memory run state | N/A with reason: composition returns contract values only and must not open a run store |
| generated aggregate | N/A with reason: no generated JSON owner changes |
| filesystem output | N/A with reason: no runtime file output is authorized |

## Required Composition Contract

The worker must implement this bounded behavior:

1. Accept `MaoOrchestrationCompositionInput` with `graphInput` and `receiptId`.
2. Call `compileTaskGraph(graphInput)` exactly once.
3. When compilation fails, return a frozen result containing the unchanged
   graph failure and `roleResolution: null`.
4. When compilation succeeds, call `resolveRole` exactly once with the compiled
   graph and caller-supplied `receiptId`.
5. Return a frozen result containing the compile success and exact resolver
   receipt, including `REJECTED` or `OPERATOR_APPROVAL_REQUIRED`.
6. Do not catch and reinterpret owner results, synthesize new reason codes,
   mutate inputs, or launch any downstream action.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | add one forwarding export from existing `./mao` local barrel |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | revise only root-adoption comment text that becomes stale |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | revise only root-adoption comment text that becomes stale |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts` | prove current graph compiler is callable from execution package root |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts` | add one forwarding export from `control.plane.mao.barrel` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.mao.barrel.ts` | export role resolver and composition contract values/types |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | revise only root/caller comment text that becomes stale |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/orchestration.composition.contract.ts` | implement the pure bounded contract |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.orchestration.composition.contract.test.ts` | prove root discovery, determinism, negative decisions, frozen result, and forbidden-import absence |
| `docs/reviews/CVF_MAO_OA_T1_WORKER_RETURN_2026-07-16.md` | record exact pending-review evidence and no-commit return |

## Execution Plan

1. Capture clean status and execution base.
2. Re-read current package roots, MAO owners, package manifests, focused tests,
   and file-size exception.
3. Add the execution root forwarder and truthful source comments.
4. Add the control MAO domain barrel, pure composition contract, root forwarder,
   and truthful resolver comment.
5. Add dedicated focused tests only.
6. Run focused tests, both package typechecks, diff checks, file-size guard, and
   pre-implementation autorun against the captured execution base.
7. Create the worker return using checker-safe headings and actual pending
   status evidence.
8. Run the worker-return fast gate, leave everything uncommitted, and return the
   required token.

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for its review path,
worker-return profile, trace, delta claim, epistemic process, rescan, corpus,
finding-to-governance, public export, and file-size classes.

| Output artifact | Required read-ahead result |
|---|---|
| worker return under `docs/reviews/` | derive exact review headings, worker-return terms, trace labels, delta boundary labels, N/A-with-reason sections, no-commit evidence, and real Git status shape before writing |

Required worker-return sections are: Purpose; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; Public
Export Disposition; External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Machine Closure Package; Claim
Boundary; git status --short; Changed Files; Worker Experience Retrospective;
Command Evidence; No-Commit Statement.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_OA_T1_WORKER_RETURN_2026-07-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must state actual pending paths in Git status and must not
claim closure, committed-range proof, or a clean worktree while changes remain.

## Agent Handoff Contract Control Block

Contract source stable front door: `docs/reference/agent_handoff/README.md`

Contract source archive-named canonical exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> implementation worker -> independent reviewer/closer -> session-sync steward |
| phase | pre-dispatch to pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=`233e1ab98`; executionBaseHead=worker captures current committed dispatch HEAD; closureBaseHead=reviewer sets before material commit |
| changedSetScope(phase) | worker may modify exactly nine listed source/test paths plus one worker return; dispatcher owns exact three-path packet; reviewer owns closure conversion |
| traceScope(phase, actor) | each role records only its own command, path, and changed-set evidence |
| commitOwner(phase) | worker forbidden; reviewer/closer owns material commit; session-sync steward owns separate continuity commit |
| crossBatchIsolation | no SOT3-APP, other absorption, T2-T7, public, session, Catalog, GAP, ADIF, checker, or external-root work |
| nextMoveSurfaces | unchanged by worker; reviewer/closer and session-sync steward update governed surfaces only after acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_OA_T1_COMPLETION_REVIEW_2026-07-16.md` |
| reviewerOwnedClosurePaths | paired GC-018, this work order, worker source/test outputs, worker return, completion review, governing roadmap, and separate session-sync surfaces |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|---|
| `INTERNAL_AGENT` | execution/control package-root MAO exports plus `composeOrchestrationPlan` | deterministic graph and admission contract only; no execution, storage, provider, reviewer/closer, commit, or session action | source, focused tests, and typechecks | internal TypeScript import surface | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP owner | no ingress, authentication, approval, receipt, raw-data, mutation, or public behavior | T0 OA-18 ambiguity remains unresolved | external adapter remains parked | `N/A_WITH_REASON` |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the existing compiler and resolver can be safely
composed through package-root discoverable, pure TypeScript surfaces without
creating runtime behavior.

Evidence Comparison Requirement: compare source diff, import graph, focused
positive and negative tests, typechecks, and file-size evidence with that
prediction.

Contradiction Handling Requirement: any required runtime dependency, import
cycle, type incompatibility, or forbidden-path need blocks the tranche rather
than being hidden behind an adapter or widened scope.

Claim Update Requirement: worker and reviewer state whether the prediction was
confirmed, narrowed, revised, or invalidated.

## Verification Commands

From `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION`:

```powershell
npm test -- tests/mao.package.root.exports.test.ts
npm run check
```

From `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`:

```powershell
npm test -- tests/mao.orchestration.composition.contract.test.ts
npm run check
```

From repository root:

```powershell
git diff --check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

Do not run the application, server, browser, provider, live release bundle, or
dependency installation.

## Evidence Requirements

- exact `executionBaseHead` and pre-edit clean status;
- `git diff --name-status` proving only the ten allowed worker paths;
- focused test pass counts and command outputs;
- both TypeScript checks with exit code 0;
- current line count for execution root and file-size guard result;
- source inspection showing composition imports only graph compiler/root types
  and role resolver, with none of the forbidden owners;
- worker-return fast-gate result and actual pending Git status;
- explicit no-commit statement with unchanged HEAD.

## Acceptance Criteria

- execution root has exactly one MAO forwarding export through `./mao`;
- execution local barrel and graph source comments no longer claim root absence;
- control root has exactly one MAO domain-barrel forwarding export;
- control MAO barrel exports the current resolver plus new composition contract;
- resolver comment no longer claims zero caller/root exposure;
- new composition input/result shapes match New Doc-Only Fields exactly;
- accepted graph invokes role resolution once and returns the exact receipt;
- compile failure returns unchanged failure plus null role resolution;
- role rejection and R3 approval-required results remain exact resolver outputs;
- two independent calls with the same immutable input yield deeply equal results and frozen top-level results;
- forbidden owner/import tokens are absent from composition source;
- focused tests, both typechecks, diff check, file-size guard,
  pre-implementation gate, and worker-return fast gate pass;
- only the ten allowed worker paths change and HEAD remains unchanged.

## Review Gate

The reviewer must independently inspect all changed source, recompute imports,
run focused tests and typechecks, confirm the execution root remains within its
approved maximum, and verify that no result or rejection was reinterpreted.
Structural or test PASS alone cannot establish the no-side-effect claim.

## Closure Diff Gate

Reviewer compares the roadmap T1 row, T0 Accepted T1 Packet Boundary, this work
order, actual changed set, test evidence, worker claims, and completion review.
Every requirement must be present, N/A with reason, or blocked with a
return-to-orchestrator action.

## Closure Checklist

| Item | Required closure disposition |
|---|---|
| exact changed set | reviewer recomputed |
| package-root discovery | reviewer proven |
| deterministic composition | reviewer proven |
| compile and admission negatives | reviewer proven |
| forbidden import/action boundary | reviewer proven |
| focused tests and typechecks | reviewer rerun |
| file-size guard | reviewer rerun |
| no worker commit | reviewer verified |
| roadmap and session continuity | reviewer/closer plus session-sync steward only |
| public export | DEFERRED_PRIVATE_ONLY unless separately authorized |

## Reviewer Closure Decision

Current dispatch decision: `PENDING_INDEPENDENT_REVIEW`.

Only the independent reviewer/closer may convert this packet to a
closed-equivalent status after recomputation. The worker must return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Machine Closure Package

| Closure item | Required artifact/path | Required state |
|---|---|---|
| work order | this file | reviewer-updated terminal status |
| baseline | paired GC-018 | reviewer-updated terminal status |
| completion review | `docs/reviews/CVF_MAO_OA_T1_COMPLETION_REVIEW_2026-07-16.md` | reviewer-owned final decision |
| roadmap | governing MAO operational-adoption roadmap | T1 row reconciled; T2 packet authoring only if accepted |
| registry JSON | N/A with reason: no registry mutation authorized | none |
| registry Markdown | N/A with reason: no registry mutation authorized | none |
| external evidence digest | N/A with reason: no external evidence consumed | none |
| system loop interlock | N/A with reason: pure contract seam only | none |
| session continuity | active state sources, generated state, front door, and active handoff | separate session-sync batch |

## Acceptance Receipt Assertion Matrix

| Required value | Required evidence | Dispatch state |
|---|---|---|
| runtime receipt | N/A with reason: runtime execution forbidden | N/A_WITH_REASON |
| provider acceptance | N/A with reason: provider invocation forbidden | N/A_WITH_REASON |
| contract acceptance | focused tests and typechecks | WORKER_TO_PROVE |
| reviewer acceptance | independent completion review | NOT_EXECUTED_YET |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without scope expansion when:

- a required implementation needs any path outside Allowed Scope;
- current source contradicts the accepted input or result owner;
- package-root wiring creates an import cycle that cannot be repaired inside
  the exact allowed source paths;
- the execution root would exceed 1,450 lines;
- a focused test or typecheck exposes a required later-tranche owner;
- unrelated worktree changes appear;
- a worker commit occurs or is required.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dispatch Prompt Envelope; Role:; Canonical packet:; Commit mode:; executionBaseHead; Current-time notes:; Do-not-misread notes:; Required first actions:; Return contract:; Purpose; Scope / Target / Owner Boundary; Authority Chain; Dependency Release Evidence; Scaffold Provenance Block; ADIF Defect Registry Disclosure; Source Verification Block; New Doc-Only Fields; Current Runtime Freshness Verification; Negative Search And Collision Discipline; Evidence Reuse And Encoding Plan; Roadmap-To-Work-Order Trace Matrix; Worker Autonomy / No-Question Rule; Design Control Carry-Forward; Work-Order Fulfillment Manifest; Execution Plan; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Dual Agent Surface Matrix; Epistemic Process Block; Verification Commands; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Diff Gate; Closure Checklist; Reviewer Closure Decision; Machine Closure Package; Return-To-Orchestrator Conditions; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm exact source-verified implementation dispatch and worker-output contract before material commit |
| claimBoundary | checker conformance does not prove implementation correctness, runtime adoption, provider behavior, or user value |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | Codex local private provenance workspace |
| Session or invocation | MAO-OA-T1 dispatch authoring, 2026-07-16 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, ADIF resolver, scaffold preview, apply_patch, governance gates, git |
| Target paths | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md` |
| Allowed scope source | operator request, active next move, governing roadmap, and accepted T0 boundary |
| Before status evidence | clean worktree at `233e1ab98`; all planned new paths absent |
| After status evidence | exact three-path dispatch packet pending verification and material commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; pre-dispatch range from `233e1ab98` |
| Approval boundary | MAO-OA-T1 package-root and pure composition implementation dispatch only |
| Claim boundary | no worker execution, source implementation, runtime/provider/live/public action, or production claim by dispatcher |
| Agent type | dispatcher |
| Invocation ID | `mao-oa-t1-dispatch-2026-07-16` |
| Expected manifest | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md` |
| Actual changed set | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`; `docs/baselines/CVF_GC018_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | package-root discoverability plus pure deterministic graph-and-role composition contract |
| claimDisposition | CLAIM_REJECTED for runtime control, enforcement, interception, durable execution, worker launch, or operational convergence claims |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT; only deterministic in-memory contract values are authorized |
| actionEvidence | CLAIM_REJECTED_NO_ACTION; no actor, provider, lifecycle, storage, or application action is authorized |
| invocationBoundary | package-local focused tests, typechecks, source reads, and governance checks only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, provider call, or agent coding control claim |
| claimLanguage | internal TypeScript package-root contract discovery and pure composition only |
| forbiddenExpansion | no T2-T7, runtime/provider/live/public/package-manifest/Web/MCP/session/Catalog/GAP/ADIF/checker work |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. No public artifact,
public-sync operation, or public claim is authorized.

## Claim Boundary

This work order authorizes exactly one bounded internal TypeScript adoption
seam: package-root MAO exports, one pure graph-plus-role composition contract,
focused tests, truthful comments, and a pending worker return. It does not
authorize or prove durable run state, replay, recovery, worker launch,
liveness, provider routing, reviewer/closer execution, automatic commit or
session mutation, operator projection, CLI/MCP/UI ingress, live governance,
production readiness, public readiness, scale, certification, shipment, or
demonstrated user value.
