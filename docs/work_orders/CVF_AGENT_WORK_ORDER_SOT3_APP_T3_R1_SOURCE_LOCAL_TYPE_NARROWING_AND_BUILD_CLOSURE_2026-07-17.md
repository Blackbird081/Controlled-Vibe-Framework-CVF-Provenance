# CVF Agent Work Order - SOT3-APP-T3-R1 Source-Local Type Narrowing And Build Closure

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR

Batch ID: SOT3-APP-T3-R1

Dispatch base head: `7e347cae0`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_SOT3_APP_T3_R1_WORKER_RETURN_2026-07-17.md`

## Dispatch Prompt Envelope

Current-time notes: T3's reproducible install and 42 tests passed; build and
typecheck remain blocked by exactly two out-of-scope application source errors.

Do-not-misread notes: this is source-local type narrowing, not permission to
relax strictness, redesign navigation, or reopen package resolution.

Required first actions: confirm clean provenance status, capture
`executionBaseHead`, run pre-implementation, and hash all four allowed external
outputs before editing.

Return contract: return exactly `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`; create exactly two provenance outputs; do not commit.

Role: implement one bounded T3-R1 remediation.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T3_R1_SOURCE_LOCAL_TYPE_NARROWING_AND_BUILD_CLOSURE_2026-07-17.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the committed post-dispatch HEAD before any edit.

Required gate before external edit:

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7e347cae0 --head HEAD
```

Return exactly `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`. Do not stage
or commit.

## Authority Chain

Standing operator continuation -> SOT3-APP roadmap T3 -> accepted blocked-return
review at `30dbcae4a` -> paired T3-R1 GC-018 -> this work order.

## Agent Roles

Dispatcher owns packet truth. Worker owns exact source/test repair and evidence
without commit. Independent reviewer/closer owns rerun, acceptance, material
commit, roadmap state, and session sync.

## Required First Reads

- paired T3-R1 GC-018 and this work order;
- T3 worker evidence and blocked-return review;
- all four allowed external source/test paths;
- worker-return, handoff, trace, closure, public, and size checker source.

## Pre-Flight Checks

- provenance worktree clean and HEAD equals committed post-dispatch base;
- external application root remains non-Git;
- current compiler failures reproduce before edit;
- pre-implementation autorun gate passes before external edit.

## Write Ownership

Worker owns exactly four external source/test outputs and two provenance
outputs. Reviewer owns baselines, work orders, roadmap, commits, completion
review, registries, and session surfaces.

## Worker Autonomy / No-Question Rule

Proceed autonomously inside exact scope and repair allowed-scope gate failures.
Stop for any required unlisted path, compiler relaxation, destructive action,
secret/quota need, service lane, or forbidden claim expansion.

## Authorization / Decision

Repair each compiler defect at its source. Preserve error redaction semantics
and all navigation destinations. Do not change TypeScript compiler options.

## Purpose

Make isolated API and web typechecks pass, make root build/typecheck pass, add
behavior-focused regression coverage, and preserve the 42-test T3 evidence.

## Dependency Release Evidence

| Dependency | Evidence | Release result | Disposition |
|---|---|---|---|
| T3 block independently accepted | blocked-return review; commit `30dbcae4a` | exact two defects released | SATISFIED |
| reproducible dependencies | T3 evidence and lockfile | no new resolution needed | SATISFIED |
| T4+ hold | roadmap | no later-tranche action | SATISFIED_WITH_HOLD |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| API handler reads `error.message` from unknown | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `apps/api/src/middleware/error.middleware.ts` | line 6 | `error.message` | `registerErrorMiddleware` | ACCEPT |
| API regression suite exists | EXISTS | CANONICAL_CONTRACT: external sibling direct-read evidence; `apps/api/src/middleware/application-boundary.middleware.test.ts` | application boundary suite | `buildApp` | API middleware tests | ACCEPT |
| web navigation uses nested array destructuring | RUNTIME_BEHAVIOR | CANONICAL_CONTRACT: external sibling direct-read evidence; `apps/web/src/layouts/application-layout.tsx` | lines 3-27 | `links`; `links.map` | `ApplicationLayout` | ACCEPT |
| root closure commands exist | VALUE_SET | CANONICAL_CONTRACT: external sibling direct-read evidence; `package.json` | `scripts` | `build`; `typecheck`; `test`; `doctor` | root manifest | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime effect |
|---|---|---|
| `API_TYPE_ERROR_COUNT` | isolated API compiler count | none |
| `WEB_TYPE_ERROR_COUNT` | isolated web compiler count | none |

## Allowed Scope

External root: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Allowed external outputs only:

- `apps/api/src/middleware/error.middleware.ts`
- `apps/api/src/middleware/application-boundary.middleware.test.ts`
- `apps/web/src/layouts/application-layout.tsx`
- `apps/web/src/layouts/application-layout.test.tsx`

Allowed provenance outputs only:

- `docs/reviews/CVF_SOT3_APP_T3_R1_TYPE_NARROWING_AND_BUILD_EVIDENCE_2026-07-17.md`
- `docs/reviews/CVF_SOT3_APP_T3_R1_WORKER_RETURN_2026-07-17.md`

Existing `node_modules`, pnpm cache, and build outputs may be read or regenerated
only by listed commands. They are not hand-edited source outputs.

priorVerificationAnchor: material commit `30dbcae4a`

freshRecomputeRequired: four hashes, isolated and root compiler results, focused
tests, full tests, doctor, provenance status, and HEAD

unicodePathHandling: literal paths and UTF-8-safe readers; new text defaults ASCII

extractedTextAuthority: current source and command output control

## Forbidden Scope

- any external path not listed above;
- `tsconfig*`, manifests, lockfile, workspace config, dependency versions;
- weakening strictness or catch-variable typing;
- UI redesign, route additions/removals, service launch, browser proof;
- provider/model/live/network beyond already-installed local dependency reads;
- database/production, public-sync, push, Git initialization, T4 or T5 work;
- staging or committing by the worker.

## Execution Plan

1. Reproduce isolated API and web typecheck errors before edit.
2. In the API handler, narrow `unknown` before reading a message. Preserve the
   existing token-only response and generic fallback behavior. Add regression
   cases for non-Error thrown values and SOT-token Errors.
3. Give the web navigation data an explicit tuple/object type so `to` is always
   a string. Preserve all thirteen path/label pairs. Add a focused test that
   renders the layout under a router and verifies every target is defined.
4. Run isolated API/web typecheck and build, then root typecheck/build/test,
   focused tests, and doctor.
5. Record before/after SHA-256 for all four allowed outputs and exact receipts.
6. Run worker-return fast gate; leave exactly two untracked provenance outputs.

## Evidence Requirements

- before/after hash manifest for four paths, including ABSENT for a new test;
- exact command, exit code, pass/fail, file/test counts;
- `API_TYPE_ERROR_COUNT=0` and `WEB_TYPE_ERROR_COUNT=0` after repair;
- proof no error suffix or non-Error value is returned raw;
- proof thirteen navigation targets and labels are unchanged;
- exact provenance `git status --short`, staged set, and HEAD.

## Fail Conditions

- build/typecheck remains nonzero;
- a required repair needs an unlisted path or compiler relaxation;
- API response exposes raw internal detail;
- any navigation destination changes;
- focused or full test fails;
- changed set exceeds four external plus two provenance outputs;
- provider/live/browser/public/production/T4 action occurs;
- worker stages or commits.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| build/typecheck command-backed | Execution Plan | command receipts | isolated plus root compiler commands | READY |
| tests invoke behavior | Execution Plan | focused regression receipts | focused Vitest command | READY |
| no broad claim | Forbidden Scope | worker claim boundary | changed-set and receipt review | READY |
| T4 remains parked | Return Conditions | worker status | no T4 path/action | READY |

## Acceptance Criteria

- isolated API typecheck/build PASS;
- isolated web typecheck/build PASS;
- root typecheck and build PASS;
- root tests pass with at least the prior 42 tests plus new regression tests;
- focused API and web tests PASS and exercise production source;
- doctor reports healthy;
- strict compiler settings and thirteen navigation pairs remain unchanged;
- exact scope and no-commit contract are honored.

## Review Gate

Independent reviewer rereads both fixes, reruns all commands, adversarially
checks raw-detail redaction and navigation target preservation, and alone owns
closure conversion and commit.

## Verification Commands

```text
corepack pnpm@9.15.0 --filter @sot/api typecheck
corepack pnpm@9.15.0 --filter @sot/api build
corepack pnpm@9.15.0 --filter @sot/web typecheck
corepack pnpm@9.15.0 --filter @sot/web build
corepack pnpm@9.15.0 typecheck
corepack pnpm@9.15.0 build
corepack pnpm@9.15.0 test
corepack pnpm@9.15.0 exec vitest run --workspace vitest.workspace.ts apps/api/src/middleware/application-boundary.middleware.test.ts apps/web/src/layouts/application-layout.test.tsx
corepack pnpm@9.15.0 doctor
python governance/compat/run_worker_return_fast_gate.py
```

## Return Conditions

Return `COMPLETE_PENDING_REVIEW` only when every acceptance criterion passes.
Otherwise return `BLOCKED_WITH_REASON` with the exact command, error, required
path/authority, and retryability. Do not stage or commit.

## Return-To-Orchestrator Conditions

Return immediately if any fix needs an unlisted path, a compiler-policy change,
dependency/network resolution, service credential, browser, public, production,
or later-tranche authority.

## Operator Checkpoint

N/A with reason: the operator already authorized sequential roadmap execution;
this retry does not release any parked service or public lane.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | standing roadmap continuation plus accepted T3 blocked return |
| scope classification | bounded deterministic source-local type repair in a private copied-folder workspace |
| risk sensitivity | application source and tests only; strictness, provider/live/public, and production authority excluded |
| Intake role | dispatcher authors exact packet; worker implements without commit |
| Reviewer role | independent command rerun and closure owner |
| Routing decision | `WORKER_MUST_NOT_COMMIT` |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to independent reviewer/closer |
| escalation condition | unlisted path, compiler relaxation, dependency resolution, service credential, or forbidden browser/public/T4 action |
| Claim boundary | role routing only; no implementation or success claim |

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: this is repair of the already-governed external
application target, not a new repository absorption or source-mirror intake.

## Mandatory Blind-Spot Control Block

The complete denominator is four exact external outputs and two provenance
outputs. Hash every external path and list every provenance path; no sampling.

## Closure Checklist

- [x] exact two blockers source-verified
- [x] fresh GC-018 and work order filed
- [x] T4+ hold retained
- [x] fail conditions explicit
- [x] reviewer closure conversion assigned
- [x] worker commit forbidden

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`TypeScript application type-narrowing remediation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "TypeScript application type-narrowing remediation" --role dispatcher --lifecycle-phase pre-dispatch`

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted T3 block -> T3-R1 repair -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | SOT3-APP roadmap and this packet |
| Disposition | ADAPT_CONTRACT; no CVF Core import |
| Claim boundary | private deterministic source repair only |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this is an exact six-output repair batch, not a corpus completeness claim.

## Evidence Reuse And Encoding Plan

priorVerificationAnchor: T3 blocked-return review at `30dbcae4a`

freshRecomputeRequired: all hashes, compiler/test receipts, and status evidence

unicodePathHandling: literal paths; ASCII-authored outputs

extractedTextAuthority: current source and command output control

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | DISPATCHER_TO_WORKER_TO_REVIEWER_CLOSER |
| baseHeadFor(phase) | dispatchBaseHead=`7e347cae0`; executionBaseHead=capture post-dispatch HEAD; closureBaseHead=reviewer-owned |
| changedSetScope(phase) | four external outputs and two provenance outputs |
| traceScope(phase, actor) | hashes, command receipts, changed set, no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree; no overlapping batch |
| nextMoveSurfaces | reviewer/session-sync steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T3_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | paired baseline, this work order, roadmap, two worker outputs, completion review, protected sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_APP_T3_R1_WORKER_RETURN_2026-07-17.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required scalar: executionBaseHead

Required evidence section: Delta Execution Claim Boundary Control Block

Required conditional section: Rescan Intelligence Hardening

Required conditional section: Corpus Completeness And Report Integrity

Required conditional section: Machine Closure Package

Required disposition section: Public Export Disposition

Required status section: git status --short

Conditional non-applicability instruction: N/A with reason or NOT_APPLICABLE_WITH_REASON.

The return also requires Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Checker Source Read-Ahead Block,
Agent Operation Trace Block, External Knowledge Intake Routing,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Claim
Boundary, Changed Files, Worker Experience Retrospective, Command Evidence, and
No-Commit Statement as real sections.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR; Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm independently established source and dependency evidence before dispatch; gates are not first discovery |
| claimBoundary | structural confirmation does not prove compiler or test success |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T3-R1 --title "Source Local Type Narrowing And Build Closure" --date 2026-07-17 --base 7e347cae0 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T3 blocked return review 30dbcae4a" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit worker-return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact four-source/test scope, commands, failures, and evidence |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, trace, epistemic, closure, public, and size checkers read |
| docOnlyNewFields | `API_TYPE_ERROR_COUNT`; `WEB_TYPE_ERROR_COUNT` |
| claimBoundary | scaffold provenance only; no implementation claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | private provenance repository plus read-only external source inspection |
| Session or invocation | SOT3-APP-T3-R1 dispatch, 2026-07-17 |
| Working directory | provenance root and external application root |
| Command or tool surface | source reads, reviewer commands, ADIF resolver, scaffold helper, apply_patch, gates |
| Target paths | paired baseline, this work order, roadmap |
| Allowed scope source | standing continuation and accepted T3 blocked-return review |
| Before status evidence | clean worktree at `7e347cae0` |
| After status evidence | exact T3-R1 packet ready; no source implementation by dispatcher |
| Diff evidence | three governed dispatch paths before material commit |
| Approval boundary | packet authoring and dispatch only |
| Claim boundary | no source repair, provider/live/browser/public/T4 action by dispatcher |
| Agent type | dispatcher |
| Invocation ID | `sot3-app-t3-r1-dispatch-2026-07-17` |
| Expected manifest | paired baseline; this work order; roadmap |
| Actual changed set | paired baseline; this work order; roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | dispatch packet authoring only |
| claimDisposition | CLAIM_REJECTED: no source repair or compiler/test success by dispatcher |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | source inspection and governed dispatch commands only |
| interceptionBoundary | no provider, server, browser, or production interception |
| claimLanguage | T3-R1 ready for bounded worker execution only |
| forbiddenExpansion | compiler weakening, provider/live/browser/public/T4/unlisted source |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| isolated API/web typecheck and build | final reviewer recomputation PASS | PASS |
| root typecheck/build/test | final reviewer recomputation PASS; 30 files and 45 tests | PASS |
| focused API/web regression tests | final reviewer recomputation PASS; 2 files and 10 tests | PASS |
| doctor structural health | final reviewer recomputation `healthy: true` | PASS |
| receipt/query acceptance closure | N/A with reason: no runtime acceptance query or provider receipt was authorized | N/A_WITH_REASON |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| GC-018 status | paired baseline | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| Roadmap state | SOT3-APP roadmap | `Status: SOT3_APP_T3_CLOSED_T4_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | existing GC-051 aggregate | no new provenance source path | PASS |
| Registry Markdown | existing registry docs | unchanged | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_APP_T3_COMPLETION_REVIEW_2026-07-17.md` | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| External evidence digest | final four-path external SHA-256 manifest plus accepted T3 blocked-return review commit `30dbcae4a` | `7A49558F9AE2DFC044DC000C4CDE0C69C8AC0A6BB4766D364EDD646D2EA6E38D`; `2A99B6CD895ED2DDD48D4006C9E94EDD972F076937A622CB32A99CFF512AAE22`; `03F3736A5D63D2237900835E9373387399C1FD672994DBE9D5E4E93F71E96F1B`; `A8B33B6F4C99BAB26EC89A453C1BD012736573E3ECC1DEFBB0DDE7AAC61E70F3` | PASS |
| System loop interlock | T3 block -> T3-R1 worker -> independent review -> T3 closure | T4 packet authoring released; T4 execution and later lanes parked | PASS |
| Session continuity | protected sync after dispatch | reviewer/session-sync steward-owned | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private deterministic source repair; no public export is authorized.

## Claim Boundary

This work order authorizes four exact external source/test outputs and two
provenance returns. It authorizes no compiler weakening, new dependency,
provider/live/browser/public/push/production/T4 action, staging, or commit.
