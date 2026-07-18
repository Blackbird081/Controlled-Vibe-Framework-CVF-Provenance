# CVF Agent Work Order - CVF Web Inheritance T3B MAO Durable Event Operator Readout

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-INHERITANCE-T3B

Dispatch base head: `f16432325`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation worker

Reviewer/closer: independent CVF reviewer/closer

Worker return path:
`docs/reviews/CVF_WEB_INHERITANCE_T3B_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: execute only T3B as one no-commit cvf-web implementation worker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3B_MAO_DURABLE_EVENT_OPERATOR_READOUT_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: dispatcher-provided post-dispatch HEAD; capture and verify
before editing.

Current-time notes: source verified on 2026-07-18 at dispatch base
`f16432325`.

Do-not-misread notes: "liveness" in prior tranches does not authorize
heartbeat or live-process status. This packet exposes durable events only.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, this work order, paired baseline, T3P2 completion review,
and all source/checkers named below before editing.

Return contract: change exactly the twelve allowed paths, run every required
command, leave everything unstaged and uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement a safe read-only MAO durable-run operator page in cvf-web by
composing current execution-plane owners without duplicating their validation
or transition semantics.

## Authority Chain

Operator standing roadmap-continuation authority -> CVF Web inheritance
roadmap -> accepted T3A/T3P1/T3P2 reviews -> this bounded T3B work order.

## Agent Roles

| Role | Owner | Authority |
|---|---|---|
| dispatcher | CVF orchestrator | packet authoring and dispatch commit only |
| worker | delegated implementation worker | exact twelve allowed paths, no commit |
| reviewer/closer | independent CVF reviewer | recompute, bounded repair, material closure commit |
| session steward | CVF continuity owner | protected state sync only |

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, generated bootstrap/state, active handoff, guard
orientation, literal gotchas, `DESIGN.md`, paired baseline, T3P2 completion
review, every Source Verification file, and every checker named in the
Checker Source Read-Ahead Block before editing.

## Pre-Flight Checks

Verify the dispatcher-provided execution HEAD, clean initial worktree, exact
allowed-path existence/nonexistence, current package/lockfile state, and a
passing pre-implementation autorun baseline. Stop before edits on mismatch.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` only, plus this worker
return. The execution package owns discovery, replay, and generated state.
cvf-web owns configuration, bounded projection, presentation, registry truth,
and discoverability only.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| T3A | `docs/reviews/CVF_WEB_INHERITANCE_T3A_COMPLETION_REVIEW_2026-07-18.md` | `c0d88ff34` | ACCEPT |
| T3P1 | `docs/reviews/CVF_WEB_INHERITANCE_T3P1_COMPLETION_REVIEW_2026-07-18.md` | `c282312b9` | ACCEPT |
| T3P2 | `docs/reviews/CVF_WEB_INHERITANCE_T3P2_COMPLETION_REVIEW_2026-07-18.md` | `32813a983` | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| execution package name | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | name field | `name` | package manifest | ACCEPT |
| package-root MAO export | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | final export | `./mao` | package root | ACCEPT |
| durable store | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | class declaration | `MaoFileRunStore` | class | ACCEPT |
| run discovery | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | method declaration | `listRunIds` | `MaoFileRunStore` | ACCEPT |
| run replay | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | method declaration | `resumeRun` | `MaoFileRunStore` | ACCEPT |
| replay failure vocabulary | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | failure union | `MaoDurableRunStoreFailureReason` | type | ACCEPT |
| generated task state | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | function declaration | `buildReadModel` | function | ACCEPT |
| task-state safe fields | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | interface declaration | `MaoReadModelTaskState` | interface | ACCEPT |
| durable event timestamp | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | interface declaration | `occurredAt` | `MaoEventLedgerEntry` | ACCEPT |
| durable timeout token | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | event union | `TIMEOUT_DETECTED` | `MaoEventType` | ACCEPT |
| file dependency pattern | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies | `cvf-control-plane-foundation` | package manifest | ACCEPT |
| lockfile link pattern | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | packages map | `node_modules/cvf-control-plane-foundation` | npm lockfile | ACCEPT |
| safe readout state pattern | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/sot3-activation-evidence-readout.ts` | report and function | `Sot3ActivationEvidenceReadoutState` | server readout | ACCEPT |
| registry entry | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | execution-plane entry | `execution-plane-foundation` | module registry | ACCEPT |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeClass | repository-local implementation; no external source intake |
| Route | `SINGLE_AGENT_SINGLE_ROLE` |
| risk sensitivity | R1; read-only local Web projection over validated durable state |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` |
| workerRole | implementation worker |
| reviewerRole | independent reviewer/closer |
| routingDisposition | direct bounded T3B execution |
| externalAuthority | N/A with reason: no external authority is consumed |
| escalation condition | source contradiction, forbidden path, scope or claim expansion, provider/live, public-sync, secret exposure, destructive action, or dependency beyond the authorized file package |

## New Implementation Symbols

| Symbol | Required owner | Contract |
|---|---|---|
| `CVF_MAO_DURABLE_RUN_PATH` | `.env.example` and server readout | explicit optional path; absent means unavailable |
| `MaoDurableRunReadoutState` | new readout file | `AVAILABLE`, `EMPTY`, or `UNAVAILABLE` |
| `MaoDurableRunReadoutReport` | new readout file | bounded safe report |
| `getMaoDurableRunReadout` | new readout file | read-only composition function |
| `/governance/mao-runs` | new page | read-only operator surface |

## Allowed Scope

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/mao-durable-run-readout.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/mao-durable-run-readout.test.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.test.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/mao-runs/page.tsx`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/mao-runs/page.test.tsx`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.tsx`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.test.tsx`
12. `docs/reviews/CVF_WEB_INHERITANCE_T3B_WORKER_RETURN_2026-07-18.md`

The worker owns only these twelve paths. Package installation may update only
the two allowed manifest/lock paths; `node_modules` is not evidence and must
not be staged or reported as a governed output.

## Write Ownership

| Path family | Worker action | Reviewer action |
|---|---|---|
| allowed cvf-web source/tests/config/manifests | implement and verify, no commit | inspect, repair if bounded, commit |
| worker return | author exact evidence | accept or repair evidence |
| baseline/work order/roadmap/completion review | no edit | close and update |
| session/handoff/generated registries | no edit | separate closure sync only |

## Forbidden Scope

- execution-plane source/test mutation;
- evidence ledger, evidence records, evidence milestones, evidence freshness,
  heartbeat, or live-worker/process status;
- worker launch, `recordTimeout`, cancellation, retry, queue, provider, or network call;
- raw graph authority, event payload/detail, idempotency key, store path, stack,
  exception message, or filesystem error detail in returned data or UI;
- implicit default store root or directory creation;
- API route, auth/RBAC, new UI library, browser/live proof, public-sync, push,
  production, registry aggregate, session, handoff, staging, or commit.

## Required Readout Contract

The default function reads `CVF_MAO_DURABLE_RUN_PATH`. Missing or blank config
returns `UNAVAILABLE` with `MAO_RUN_STORE_NOT_CONFIGURED`. It must not create a
directory or choose a fallback path.

Injectable tests may supply a port with `listRunIds` and `resumeRun`. Any
failure returns one `UNAVAILABLE` report with zero runs, no partial result,
and a diagnostic class derived only from the failure reason. Never return the
store's `detail` string.

For valid runs, call `buildReadModel` and project only:

- run: `taskGraphId`, `eventCount`, `taskCount`, `timeoutCount`,
  `latestEventAt`, and bounded `tasks`;
- task: `taskId`, `state`, `terminalOutcome`, `lastEventId`, `lastSequence`;
- report: `state`, `generatedAt`, `boundary`, `diagnosticClass`, `totalRuns`,
  and returned `runs`.

Limit output to 50 runs and 100 tasks per run. Sort runs by non-null
`latestEventAt` descending, null last, then `taskGraphId`; retain
`buildReadModel` task ordering. Count timeouts only where event type is
`TIMEOUT_DETECTED`. Do not label event recency as heartbeat, evidence recency,
or system liveness.

## Required UI And Registry Contract

The server page at `/governance/mao-runs` renders distinct available, empty,
and unavailable states; states the durable-event-only boundary and explicit
evidence/heartbeat exclusion; shows no button, form, launch, cancel, retry, or
refresh mutation control; and links back to governance overview.

Add localized English/Vietnamese governance-overview discoverability using
the existing file convention. Update the execution-plane registry entry from
`NOT_EXPOSED` to `PARTIAL_INHERITED`, keep `exposedActions: []`, and explain
that only the read-only durable-run projection is inherited.

## Test Matrix

- missing and blank config fail visibly unavailable without store creation;
- empty discovery is empty;
- valid replay maps exact allowlisted fields and deterministic ordering;
- timeout count and latest event time derive from replayed events;
- discovery failure and failure on any resumed run return no partial records;
- diagnostic output never contains raw detail or configured path;
- 50-run and 100-task caps hold;
- page covers all three states, boundary/exclusion copy, and no mutation controls;
- governance overview links to the new route in both languages;
- registry reports execution plane partial with zero actions.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | verify execution HEAD and clean worktree | git evidence |
| 2 | add file dependency and lock entry | manifest diff |
| 3 | implement safe readout and focused tests | Vitest |
| 4 | implement page, registry truth, discoverability, and tests | jsdom/Vitest |
| 5 | run typecheck and production build | command output |
| 6 | run governed gates and return exact no-commit packet | worker return |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order owner | Closure evidence |
|---|---|---|
| T3 read-only run/evidence/milestone/liveness projection | narrowed by T3P2 to durable run/task/timeout/event recency | readout tests and page |
| no launch/provider/queue/autonomous mutation | Forbidden Scope and zero-action registry | negative UI/source assertions |
| dependency-ordered implementation | accepted T3A/T3P1/T3P2 commits | dependency table |
| DESIGN.md compliance | UI contract | page tests and reviewer inspection |

## Evidence Requirements

Record initial/final HEAD, exact `git status --short --untracked-files=all`,
`git diff --name-status`, cached diff, package commands, focused tests,
typecheck, build, file-size guard, pre-implementation autorun, and worker-fast
gate. Disclose every repair and never claim browser or live proof.

## Verification Commands

From repository root:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
git diff --cached --name-status
```

From `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`:

```powershell
npm install --package-lock-only --ignore-scripts
npx vitest run src/lib/server/mao-durable-run-readout.test.ts src/lib/server/runtime-modules.test.ts "src/app/(dashboard)/governance/mao-runs/page.test.tsx" "src/app/(dashboard)/governance/page.test.tsx"
npm run check
npm run build
```

## Acceptance Criteria

- AC-01 through AC-09 in the paired baseline all pass.
- Exactly twelve allowed paths change; nothing is staged; HEAD is unchanged.
- `WORKER_MUST_NOT_COMMIT` is honored.
- Any source contradiction or required forbidden path returns
  `BLOCKED_WITH_REASON` before scope expansion.

## Review Gate

Independent reviewer must inspect the allowlist, failure redaction, no-partial
behavior, caps/order, page language, dependency/registry truth, and all command
evidence before material commit. T4 and T5 remain parked.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all twelve allowed paths, tests,
typecheck, build, governance gates, unchanged HEAD, and no-staging evidence
pass. Return `BLOCKED_WITH_REASON` for any source contradiction, base mismatch,
or required forbidden path. Do not return a provisional success token.

## Operator Checkpoint

N/A with reason: the operator already authorized automatic roadmap
continuation. Independent reviewer acceptance remains mandatory before T4.

## Closure Checklist

- [ ] execution HEAD matches dispatcher instruction;
- [ ] exact twelve-path manifest holds;
- [ ] dependency and lockfile resolve the execution package;
- [ ] readout state/failure/allowlist/cap/order matrix passes;
- [ ] page, link, and registry tests pass;
- [ ] typecheck, build, file-size, autorun, and worker-fast gates pass;
- [ ] nothing is staged or committed; and
- [ ] excluded evidence/heartbeat/mutation dimensions remain absent.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| existingStorageOwner | caller-supplied `MaoFileRunStore` root |
| newStorageLayout | N/A with reason: this packet adds no storage and only reads an explicit existing root |
| aggregateDiscipline | N/A with reason: no generated aggregate is introduced |
| mutationBoundary | no create, append, repair, delete, or default-root selection |
| rollbackBoundary | remove the cvf-web dependency/readout/page projection only; durable store data is untouched |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_SINGLE_ROLE` |
| rolePattern | one implementation worker followed by independent reviewer/closer |
| phase | dispatch, no-commit implementation, reviewer closure, session sync |
| baseHeadFor(phase) | dispatchBaseHead=`f16432325`; executionBaseHead=dispatcher-provided post-dispatch HEAD; closureBaseHead=executionBaseHead |
| changedSetScope(phase) | dispatch=roadmap/baseline/work order; execution=exact twelve paths; closure=reviewer-owned allowed source/docs; session=protected continuity |
| traceScope(phase, actor) | each actor records its own commands and exact changed set |
| commitOwner(phase) | dispatcher; none for worker; reviewer/closer; session steward |
| crossBatchIsolation | evidence/heartbeat, T4-T5, provider/live, public, push, production parked |
| nextMoveSurfaces | session steward only |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_WEB_INHERITANCE_T3B_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: twelve worker-owned paths, paired baseline/work
order, roadmap, and completion review; continuity in a separate commit.

closureOwner: CVF independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_INHERITANCE_T3B_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker, type, build, and test failures directly. Return
to orchestrator only for source contradiction, forbidden-scope need, or
missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`worker`, lifecyclePhase=`pre-implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role worker --lifecycle-phase pre-implementation --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; New Implementation Symbols; Allowed Scope; Forbidden Scope; Required Readout Contract; Test Matrix; Execution Plan; Roadmap-To-Work-Order Trace Matrix; Verification Commands; Acceptance Criteria; Review Gate; Closure Checklist; Foundation Storage Layout Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source and checker read-ahead |
| claimBoundary | structural conformance does not prove implementation or UI quality |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3B --title "MAO Durable Event Operator Readout" --date 2026-07-18 --base f16432325 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact dependency, source, implementation, UI, test, and twelve-path contracts |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | N/A with reason: all new fields are proposed implementation symbols |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T3B dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | startup/design/source reads, repository search, scaffold, apply_patch, gates |
| Target paths | roadmap; paired T3B baseline; this work order |
| Allowed scope source | accepted T3P2 completion review and roadmap |
| Before status evidence | clean worktree at `f16432325` |
| After status evidence | exact three-path dispatch set pending commit |
| Diff evidence | bounded material diff before commit |
| Approval boundary | bounded T3B no-commit implementation dispatch |
| Claim boundary | no implementation executed by dispatcher; excluded evidence/live/public lanes parked |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-t3b-dispatch-2026-07-18` |
| Expected manifest | roadmap; T3B baseline; T3B work order |
| Actual changed set | exact three-path dispatch set before commit |
| Manifest delta | MATCH after verification |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | bounded read-only Web projection implementation packet |
| claimDisposition | CLAIM_REJECTED_NO_RECEIPT until reviewer accepts source/test/build evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker command evidence is not a runtime action receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no mutation action is exposed or authorized |
| invocationBoundary | exact twelve-path no-commit worker packet |
| interceptionBoundary | no agent/provider/action interception or enforcement claim |
| claimLanguage | read, project, display, and report only |
| forbiddenExpansion | evidence/heartbeat, worker execution, provider/live, public, push, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync action.

## Claim Boundary

This work order authorizes exactly the bounded twelve-path T3B implementation.
It does not authorize evidence/heartbeat projection, MAO execution, browser or
live proof, public-sync, push, release, production, session mutation, staging,
or worker commit.
