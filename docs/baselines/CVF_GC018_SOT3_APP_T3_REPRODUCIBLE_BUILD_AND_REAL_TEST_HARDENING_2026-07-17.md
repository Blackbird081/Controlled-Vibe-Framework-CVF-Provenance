# CVF GC-018 Baseline - SOT3-APP-T3 Reproducible Build And Real Test Hardening

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SOT3-APP-T3

Dispatch base head: `59eec0f02`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator standing roadmap-continuation authority

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Convert the external SOT-Application workspace from source-only evidence into
a reproducible pnpm workspace with a committed lockfile, owned build/typecheck/
test commands, real T2 boundary execution, and at least one failure-injection
test that invokes production behavior rather than asserting a constant.

## Decision

The operator's standing roadmap-continuation instruction and accepted T2
closure release this exact T3 dispatch. T4+ and all unrelated service lanes
remain held.

## Verification Evidence

Current source evidence is the directly read external manifest/config/test set,
the absent lockfile and dependency directory enumeration, accepted T2 closure,
and the pre-dispatch command evidence produced for this packet.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T2 closure | `docs/reviews/CVF_SOT3_APP_T2_COMPLETION_REVIEW_2026-07-17.md`; material commit `8ee6c0030` | bounded T2 closure exists and routes dependency/test proof to T3 | SATISFIED |
| clean authoring base | session-sync commit `59eec0f02` | no unresolved provenance worktree change | SATISFIED |
| roadmap T3 release | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md`; T3 row | T2 closure releases fresh T3 packet authoring | SATISFIED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| pnpm version owner | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `package.json` | `packageManager` | `packageManager` | root package manifest | ACCEPT |
| root build command | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `package.json` | `scripts.build` | `build` | root package scripts | ACCEPT |
| root test command | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `package.json` | `scripts.test` | `test` | root package scripts | ACCEPT |
| root typecheck command | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `package.json` | `scripts.typecheck` | `typecheck` | root package scripts | ACCEPT |
| workspace membership | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `pnpm-workspace.yaml` | `packages` | `packages` | pnpm workspace config | ACCEPT |
| lockfile absence | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read filesystem evidence | direct lockfile enumeration on 2026-07-17 | `pnpm-lock.yaml` | dependency snapshot | ACCEPT |
| Vitest workspace candidates | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `vitest.workspace.ts` | `defineWorkspace` array | `defineWorkspace` | Vitest workspace config | ACCEPT |
| API executable scripts | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `apps/api/package.json` | `scripts` | `build`; `typecheck`; `test` | API package manifest | ACCEPT |
| Web executable scripts | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; external `apps/web/package.json` | `scripts` | `build`; `typecheck`; `test` | Web package manifest | ACCEPT |
| library packages lack scripts | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; seven external package manifests | direct manifest reads | `scripts` | library package manifests | ACCEPT |
| T2 boundary test source | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; external T2 integration test | test declarations | `GovernedOutputService`; `ReviewFreezeService` | integration test | ACCEPT |
| API admission test source | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; external API middleware test | test declarations | `buildApp`; `OutputApplicationBoundary` | API middleware test | ACCEPT |
| failure-injection runner is constant matrix | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; external failure-injection script | `tests` array | `tests`; `all_passed` | script smoke matrix | ACCEPT |
| legacy failure tests assert constants | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; external failure-injection tests | current test bodies | `expect` | failure-injection test set | ACCEPT |

No source fact in this packet relies on provider-local memory. External paths
above are read-only source evidence for dispatch authoring, not CVF authority.

## New Doc-Only Fields

| Field | Purpose | Runtime effect |
|---|---|---|
| `DEPENDENCY_RESOLUTION_CALL_COUNT` | record bounded package-registry resolution attempts | none |
| `ROOT_TEST_DISCOVERY_COUNT` | record real tests discovered by the root runner | none |
| `PRODUCTION_BEHAVIOR_FAILURE_TEST_COUNT` | record failure tests invoking product source | none |

## Scope / Methodology

The worker may change only the exact manifest/config/test paths declared by the
paired work order, may generate `pnpm-lock.yaml`, and may create disposable
`node_modules` content only through pnpm. Package-registry network access is
authorized solely for dependency resolution from manifest-declared packages.
No provider, model, browser, application server, public, or production network
action is authorized.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T3 instruction | Required evidence |
|---|---|---|
| lockfile | generate and freeze pnpm dependency graph | committed external lockfile hash and frozen reinstall result |
| owned package scripts | make root commands cover intended packages/tests | manifest diff plus command transcript |
| schema compatibility | run real TypeScript build and typecheck | zero-exit command evidence or source-backed block |
| request admission | execute T2 API admission tests | nonzero discovered test count and pass/fail result |
| behavior-path failure injection | add one production-source negative test | source import, action counter, rejection assertion |
| non-tautological proof | prohibit preassigned-constant-only acceptance | test source read plus executed receipt |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reproducible TypeScript monorepo compilation and real test hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "reproducible TypeScript monorepo compilation and real test hardening" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | DISPATCHER_TO_WORKER_TO_REVIEWER_CLOSER |
| baseHeadFor(phase) | dispatchBaseHead=`59eec0f02`; executionBaseHead=worker captures committed post-dispatch HEAD; closureBaseHead=reviewer-owned |
| changedSetScope(phase) | exact external manifest/config/test list, generated lockfile, disposable pnpm install state, and two provenance outputs |
| traceScope(phase, actor) | hashes, dependency commands, exit codes, discovered tests, build/typecheck results, and no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; T4+, provider/live/browser/public/push and unrelated external files remain excluded |
| nextMoveSurfaces | reviewer/session steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T3_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | paired GC-018; work order; roadmap; two worker outputs; optional completion review; protected sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm a source-verified exact-scope T3 dispatch after accepted T2 closure |
| claimBoundary | structural dispatch evidence only; no dependency, build, test, or runtime success claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T3 --title "Reproducible Build And Real Test Hardening" --date 2026-07-17 --base 59eec0f02 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T2 closure 8ee6c0030" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit worker-return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact external scope, package-registry boundary, direct source verification, real command/test evidence, and T4+ hold |
| checkerReadAheadConfirmation | dispatch, handoff, trace, public, closure, and size checkers read |
| docOnlyNewFields | `DEPENDENCY_RESOLUTION_CALL_COUNT`; `ROOT_TEST_DISCOVERY_COUNT`; `PRODUCTION_BEHAVIOR_FAILURE_TEST_COUNT` |
| claimBoundary | scaffold provenance only; no implementation or command-success claim |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: DISPATCH_READY` | PASS |
| Work order status | paired T3 work order | `Status: DISPATCH_READY` | PASS |
| Roadmap state | SOT3-APP roadmap | `Status: SOT3_APP_T3_DISPATCHED_WORKER_NEXT` | PASS |
| Registry JSON | existing GC-051 aggregate | no new CVF source registry path at dispatch | PASS |
| Registry Markdown | existing registry standard | unchanged | PASS |
| Completion or reviewer artifact | future reviewer-owned T3 completion review | N/A with reason: no worker return yet |
| External evidence digest | T2 final nine-path hashes plus T3 worker-owned refreshed manifest | T2 completion review is dependency evidence; T3 outputs pending | PASS |
| System loop interlock | T2 closure -> T3 dispatch -> independent review | T4+ parked | PASS |
| Session continuity | protected sync after material dispatch commit | separate batch | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private external workspace build hardening; no public-safe artifact set
or public-sync authorization exists.

## Claim Boundary

This baseline authorizes only deterministic local T3 dependency/build/test
hardening and narrowly bounded package-registry access. It does not authorize a
provider, model, live service, browser, UI feature, server deployment,
production action, public export, push, T4 proof, or universal SOT3 claim.
