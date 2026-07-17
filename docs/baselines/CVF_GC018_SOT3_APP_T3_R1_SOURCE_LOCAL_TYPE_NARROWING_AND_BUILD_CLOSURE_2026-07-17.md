# CVF GC-018 - SOT3-APP-T3-R1 Source-Local Type Narrowing And Build Closure

Memory class: governed-baseline

Status: DISPATCH_READY

Batch ID: SOT3-APP-T3-R1

Dispatch base head: `7e347cae0`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one narrow retry that fixes the two independently verified
application-source type errors blocking T3 build/typecheck, adds focused
regression proof, and reruns the complete deterministic T3 command set.

## Decision

Proceed with source-local narrowing. Do not weaken `useUnknownInCatchVariables`,
`strict`, `noUncheckedIndexedAccess`, or any workspace compiler option. T4 and
all provider/live/browser/public/production lanes remain parked.

## Verification Evidence

The accepted T3 blocked return is committed at `30dbcae4a`. Independent review
reproduced frozen-install and 42/42 test PASS, root web build/typecheck failure,
and direct source evidence for the separate API `unknown` dereference.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T3 blocked return accepted | `docs/reviews/CVF_SOT3_APP_T3_BLOCKED_RETURN_REVIEW_2026-07-17.md`; commit `30dbcae4a` | SATISFIED |
| exact blocker paths verified | external API middleware line 6 and web layout line 27 | SATISFIED |
| T4 hold | roadmap sequence | SATISFIED_WITH_HOLD |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| API error handler dereferences unknown error | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `apps/api/src/middleware/error.middleware.ts` | line 6 | `error.message` | `registerErrorMiddleware` | ACCEPT |
| API redaction regression owner exists | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `apps/api/src/middleware/application-boundary.middleware.test.ts` | application boundary suite | `buildApp` | API middleware tests | ACCEPT |
| web links are inferred from nested string arrays | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `apps/web/src/layouts/application-layout.tsx` | lines 3-17 and 26-27 | `links`; `links.map` | `ApplicationLayout` | ACCEPT |
| current root commands own closure proof | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; `package.json` | `scripts` | `build`; `typecheck`; `test`; `doctor` | root package manifest | ACCEPT |

External sibling source is direct implementation evidence, not CVF canonical
authority.

## New Doc-Only Fields

| Field | Purpose | Runtime effect |
|---|---|---|
| `API_TYPE_ERROR_COUNT` | record isolated API compiler result | none |
| `WEB_TYPE_ERROR_COUNT` | record isolated web compiler result | none |

## Scope / Methodology

Allowed external source outputs are exactly the API error middleware, its
existing regression test, the web application layout, and one new focused web
layout test. Allowed provenance outputs are exactly the T3-R1 evidence and
worker-return documents. Existing dependencies and build outputs may be read or
regenerated only by the declared commands.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence | Status |
|---|---|---|---|
| build/typecheck command-backed | repair both source-local errors and rerun root commands | T3-R1 command receipts | READY |
| tests non-tautological | exercise error narrowing/redaction and rendered navigation targets | focused regression tests | READY |
| T4 held until T3 review | worker stops after T3-R1 return | status and changed-set proof | READY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`TypeScript application type-narrowing remediation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "TypeScript application type-narrowing remediation" --role dispatcher --lifecycle-phase pre-dispatch`

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | DISPATCHER_TO_WORKER_TO_REVIEWER_CLOSER |
| baseHeadFor(phase) | dispatchBaseHead=`7e347cae0`; executionBaseHead=capture post-dispatch HEAD; closureBaseHead=reviewer-owned |
| changedSetScope(phase) | four external source outputs and two provenance outputs |
| traceScope(phase, actor) | source hashes, compiler/test receipts, changed-set and no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean provenance worktree; T4+ and service lanes excluded |
| nextMoveSurfaces | reviewer/session-sync steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T3_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | paired baseline, work order, roadmap, two worker outputs, completion review, protected session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dependency Release Evidence; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm source-verified evidence supporting narrow T3-R1 dispatch; gates are not first discovery |
| claimBoundary | structural confirmation does not prove build, typecheck, or test success |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T3-R1 --title "Source Local Type Narrowing And Build Closure" --date 2026-07-17 --base 7e347cae0 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T3 blocked return review 30dbcae4a" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit worker-return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact two-defect source scope, tests, commands, and closure criteria |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, trace, closure, and public checkers read |
| docOnlyNewFields | `API_TYPE_ERROR_COUNT`; `WEB_TYPE_ERROR_COUNT` |
| claimBoundary | scaffold provenance only; no implementation claim |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: DISPATCH_READY` | PASS |
| Work order status | paired T3-R1 work order | `Status: DISPATCH_READY` | PASS |
| Roadmap state | SOT3-APP roadmap | `Status: SOT3_APP_T3_R1_DISPATCHED_WORKER_NEXT` | PASS |
| Registry JSON | existing GC-051 aggregate | no new provenance source path | PASS |
| Registry Markdown | existing registry documentation | unchanged | PASS |
| Completion or reviewer artifact | future completion review | N/A with reason: worker has not executed |
| External evidence digest | accepted T3 blocked-return review | commit `30dbcae4a` | PASS |
| System loop interlock | T3 block -> T3-R1 worker -> independent review | T4+ parked | PASS |
| Session continuity | protected sync after dispatch | reviewer/session-sync steward-owned | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private downstream source repair; no public export is authorized.

## Claim Boundary

This baseline authorizes only four external source/test outputs and two
provenance returns for deterministic local T3 closure. It authorizes no
provider/live/browser/public/push/production/T4 action or compiler weakening.
