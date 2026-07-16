# CVF GC-018 Baseline - MAO-OA-T1 Package Root And Orchestration Composition Contract

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-07-16

Batch ID: MAO-OA-T1

dispatchBaseHead: `233e1ab98`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator and dispatcher

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Authorize one bounded implementation tranche that makes the existing MAO task
graph and role-admission contracts discoverable from their package roots and
adds one pure deterministic composition contract. The tranche must reuse the
current owners and stop before execution, durability, provider, or operator
surfaces.

## Baseline Decision

Decision: `AUTHORIZE_MAO_OA_T1_ROOT_AND_PURE_COMPOSITION_ONLY`.

The operator authorized packet creation for delegated implementation on
2026-07-16. This baseline releases only the exact source, test, and worker-return
manifest below under `WORKER_MUST_NOT_COMMIT`.

## Scope / Target / Owner Boundary

Allowed target:

- execution-plane root forwarding export through its existing MAO local barrel;
- control-plane MAO domain barrel and package-root forwarding export;
- one control-plane pure composition contract that invokes only
  `compileTaskGraph` and `resolveRole`;
- focused package-root and composition tests in new dedicated test files;
- source comments that would otherwise become false after root adoption;
- one worker-return artifact and read-only governance evidence.

Forbidden target:

- event/evidence ledger changes, durable storage, replay, recovery, scheduler,
  queue, worker launch, heartbeat, timeout, cancellation, retry, provider call,
  lifecycle execution, reviewer/closer execution, commit/session automation,
  operator projection, UI, CLI, MCP, server, browser, or live proof;
- package manifest, dependency, generated aggregate, session, handoff, roadmap,
  Catalog, GAP, ADIF, checker, hook, public-sync, or external-root mutation;
- edits to legacy cumulative `tests/index.test.ts` files;
- commit or push by the worker.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator authorization | operator instruction on 2026-07-16 to create the work order for delegated implementation | ACCEPT |
| active next move | `CVF_SESSION/state/entries/nextAllowedMove.json` releases fresh MAO-OA-T1 GC-018 and work-order authoring | ACCEPT |
| governing roadmap | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md` | ACCEPT |
| T0 completion decision | `docs/reviews/CVF_MAO_OA_T0_COMPLETION_REVIEW_2026-07-16.md`; material commit `2de211da0` | ACCEPT |
| accepted owner/gap matrix | `docs/reviews/CVF_MAO_OA_T0_OPERATIONAL_ADOPTION_OWNER_AND_GAP_MATRIX_2026-07-16.md`, Accepted T1 Packet Boundary | ACCEPT |
| paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md` | ACCEPT |
| active handoff | `AGENT_HANDOFF_V45_2026-07-16.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T0 owner/gap audit accepted | completion review at `2de211da0` records `REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIRS` | T1 packet must use the accepted minimal boundary | ACCEPT |
| exact T1 seam selected | accepted matrix lines 242-261 requires two root exports, one pure composition contract, focused negatives, and no duplicate owner | implementation scope must match that seam | ACCEPT |
| current source owners exist | `compileTaskGraph` and `resolveRole` exist in current source and have focused tests | composition must reuse both owners | ACCEPT |
| operator implementation direction | operator requested the governed work order for delegated implementation on 2026-07-16 | worker route may be released only through this validated packet | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T1 --title "MAO Package Root And Orchestration Composition Contract" --date 2026-07-16 --base 233e1ab98 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T0 accepted closure 2de211da0" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact T0 release evidence, ten-path execution manifest, source-backed type composition, package-root maintainability control, focused tests, and strict no-runtime boundary |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, trace, scaffold, read-ahead, public-export, and file-size checker sources reviewed |
| docOnlyNewFields | graphInput; receiptId; graphResult; roleResolution; composeOrchestrationPlan |
| claimBoundary | scaffold provenance only; no implementation, runtime, provider, live, public, Web, or MCP claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`orchestration contract implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "orchestration contract implementation" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific control; active work-order, handoff, file-size, and source-verification controls remain binding |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| package main and types resolve through execution-plane root index | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | `main` and `types` fields | `src/index.ts` | execution-plane package surface | ACCEPT |
| execution-plane MAO local barrel already exports task-graph types and functions | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | lines 23-50 | `compileTaskGraph` | execution-plane MAO local barrel | ACCEPT |
| task graph compiler accepts `MaoTaskGraphInput` and returns `MaoGraphCompileResult` | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | lines 73-108 and 270-355 | `compileTaskGraph` | MAO task graph contract | ACCEPT |
| execution-plane root currently lacks a MAO export | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | current complete root barrel search | `src/index.ts` | execution-plane package root | ACCEPT |
| execution-plane root has an active bounded file-size exception | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | exception entry lines 111-116 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | governed file-size exception registry | ACCEPT |
| role resolver accepts a compiled graph plus receipt seed | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | lines 52-67 and 157-188 | `resolveRole` | MAO role resolver | ACCEPT |
| role resolver already depends from control plane to execution-plane task graph | LITERAL_INVARIANT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | lines 7-20 | `MaoRoleResolverInput` | MAO role resolver | ACCEPT |
| control-plane root is a compact domain-barrel front door | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts` | lines 1-11 | `src/index.ts` | control-plane package root | ACCEPT |
| existing MAO tests import current owners directly rather than through package roots | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.task.graph.state.contract.test.ts` | lines 1-13 | `compileTaskGraph` | execution-plane MAO task-graph tests | ACCEPT |
| existing role-resolver tests import current owners directly | LITERAL_INVARIANT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.role.resolver.contract.test.ts` | lines 1-5 | `resolveRole` | control-plane MAO role-resolver tests | ACCEPT |

## Current Runtime Freshness Verification

Verified at dispatch base `233e1ab98` on 2026-07-16. The execution-plane root
contains no MAO export; the control-plane root contains no MAO domain barrel;
the execution MAO local barrel exports `compileTaskGraph`; the control MAO
resolver exports `resolveRole`; and no planned T1 source or test path exists.

The execution-plane root is 1,415 lines under an active exception capped at
1,450. T1 must reuse the existing `src/mao/index.ts` domain barrel and add only
one forwarding line to the root. New tests must remain in dedicated files.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned governed packet paths | both T1 dispatch paths returned `False` before authoring | NO_COLLISION |
| planned execution output paths | worker-return, completion-review, composition, domain-barrel, and dedicated test paths returned `False` | NO_COLLISION |
| current execution-plane package-root MAO export | current root search returned no MAO token | IMPLEMENT_BOUNDED_SEAM |
| current control-plane package-root MAO export | current root search returned no MAO token | IMPLEMENT_BOUNDED_SEAM |
| existing composition symbol | governed source search found no `orchestration.composition.contract` owner | NEW_OWNER_AUTHORIZED |
| collision decision | no planned artifact or source owner collision exists; current owners must be reused | PASS |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: implementation authority depends on current package-root,
owner-signature, import-direction, file-size, and focused-test facts at the
worker's captured execution base.

priorVerificationArtifact: the accepted T0 matrix and completion review define
the boundary but do not replace current source reads.

priorVerificationAnchor: `2de211da0`.

freshRecomputeRequired: every import/export, type signature, test command,
changed path, and no-side-effect claim.

unicodePathHandling: use literal repository-relative paths and UTF-8-safe
readers; author new source, tests, and prose in ASCII.

extractedTextAuthority: current repository source and canonical contracts are
authoritative; provider memory, chat summaries, and extracted paraphrases are
not CVF authority.

## Required Artifact Manifest

| Artifact family | Required paths | Owner | Required state |
|---|---|---|---|
| execution-plane root adoption | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | worker | bounded root export plus truthful comments |
| execution-plane proof | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts` | worker | focused package-root test |
| control-plane composition | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts`; `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.mao.barrel.ts`; `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts`; `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/orchestration.composition.contract.ts` | worker | bounded domain/root export plus pure composition |
| control-plane proof | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.orchestration.composition.contract.test.ts` | worker | focused composition and negative tests |
| worker return | `docs/reviews/CVF_MAO_OA_T1_WORKER_RETURN_2026-07-16.md` | worker | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |

## Acceptance Criteria

- exactly nine source/test paths plus one worker-return path may change;
- execution package root exposes the existing MAO local barrel through one
  forwarding export and stays at or below its approved 1,450-line maximum;
- control package root exposes a MAO domain barrel containing the current role
  resolver and the new composition contract;
- `composeOrchestrationPlan` accepts `MaoTaskGraphInput` plus `receiptId`, calls
  `compileTaskGraph` first, calls `resolveRole` only on compile success, and
  returns both results without launching any actor or producing side effects;
- graph compile failure returns a null role-resolution result;
- resolver rejection or operator-approval decisions remain visible and are not
  silently narrowed or converted to execution;
- focused tests prove root discoverability, deterministic accepted composition,
  graph rejection, role-admission rejection, R3 approval-required preservation,
  frozen result structure, and forbidden-import absence;
- focused tests and both package typechecks pass;
- governed file-size enforcement passes;
- worker leaves every change uncommitted.

## Review Gate

The independent reviewer must recompute the changed set, import direction,
public-root exports, deterministic composition, negative cases, source-comment
truthfulness, and forbidden-import boundary. Test PASS is necessary but not a
substitute for semantic review.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|---|
| `INTERNAL_AGENT` | package-root MAO exports and pure composition contract | contract construction and admission readout only; no worker, provider, storage, lifecycle, review, closer, commit, or session action | source plus focused deterministic tests | internal TypeScript import surface only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no MAO CLI/MCP owner is authorized | no ingress, authentication, approval, receipt, raw-data, mutation, or public behavior | T0 OA-18 ambiguity remains preserved | external adapter remains parked | `N/A_WITH_REASON` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Dispatch state |
|---|---|---|---|
| Work order | paired MAO-OA-T1 work order | ready status and exact manifest | DISPATCH_READY |
| Completion review | `docs/reviews/CVF_MAO_OA_T1_COMPLETION_REVIEW_2026-07-16.md` | reviewer-owned final disposition | NOT_EXECUTED_YET |
| Roadmap | MAO operational-adoption roadmap | T1 terminal status only on accepted closure | NOT_EXECUTED_YET |
| Registry JSON | N/A with reason: no registry mutation authorized | none | N/A with reason |
| Registry Markdown | N/A with reason: no registry mutation authorized | none | N/A with reason |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | N/A with reason: T1 is pure composition only | none | N/A with reason |
| Session continuity | active state, front door, and active handoff | separate session-sync batch | NOT_EXECUTED_YET |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Dispatch status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: T1 forbids runtime execution | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: no runtime query or provider call | N/A_WITH_REASON |
| Source/test evidence | focused deterministic tests and both package typechecks | WORKER_TO_PROVE |
| Worker-return acceptance | independent reviewer decision | NOT_EXECUTED_YET |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Purpose; Scope / Target / Owner Boundary; Authority Chain; Dependency Release Evidence; Scaffold Provenance Block; ADIF Defect Registry Disclosure; Source Verification Block; Current Runtime Freshness Verification; Negative Search And Collision Discipline; Evidence Reuse And Encoding Plan; Required Artifact Manifest; Acceptance Criteria; Review Gate; Dual Agent Surface Matrix; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm exact baseline and paired implementation-dispatch structure before material commit |
| claimBoundary | checker conformance does not prove implementation correctness, runtime adoption, provider behavior, or user value |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public artifact,
public-sync operation, or public claim is authorized.

## Claim Boundary

This baseline authorizes only bounded package-root discoverability, one pure
deterministic graph-plus-role composition contract, focused tests, and a
worker return. It does not authorize or prove durable scheduling, worker
launch, liveness, provider control, reviewer/closer execution, automatic
commit/session mutation, operator UI, CLI/MCP ingress, live governance,
production readiness, public readiness, scale, certification, shipment, or
demonstrated user value.
