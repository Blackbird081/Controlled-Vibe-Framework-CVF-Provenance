# CVF Agent Work Order - Web Inheritance T1 SOT3 Runtime Module Registry Truth Correction

Memory class: governed-worker-dispatch

Status: CLOSED_PASS

Batch ID: CVF-WEB-INHERITANCE-T1

Dispatch base head: `884f69849`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation worker

Reviewer/closer: CVF independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_INHERITANCE_T1_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: implement only CVF-WEB-INHERITANCE-T1 as a no-commit worker.

Canonical packet: this work order.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture and verify the exact dispatcher-provided clean HEAD
before editing; return blocked if it differs.

Current-time notes: T0 is accepted at material commit `90aa165c6`; current
session head before this dispatch is `884f69849`; T1 is the only released
implementation tranche.

Do-not-misread notes: this is a registry-truth correction, not a new Web action
surface. `PARTIAL_INHERITED` means backend inheritance is represented in a
read-only registry; it does not mean directly runnable or action-exposed.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, the roadmap, paired baseline, this work order, both
allowed source/test files, and all checker source listed below. Confirm a clean
worktree and exact execution HEAD before editing.

Return contract: leave exactly the allowed changes unstaged and uncommitted,
then return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Add three source-backed SOT3 entries to cvf-web's existing read-only runtime
module registry and strengthen focused tests so registry truth cannot be
mistaken for direct Web runnable authority.

## Authority Chain

1. operator instruction to continue the roadmap automatically;
2. accepted T0 completion review at commit `90aa165c6`;
3. Web capability inheritance roadmap T1 objective;
4. paired T1 GC-018 baseline; and
5. this exact no-commit work order.

## Agent Roles

- dispatcher: authors and commits this packet;
- worker: implements the exact allowed source/test/return scope without commit;
- independent reviewer/closer: recomputes evidence, repairs if needed, and
  owns material closure;
- session-sync steward: updates protected continuity separately.

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, generated active state, active handoff, guard
orientation, literal gotchas, `DESIGN.md`, the roadmap, paired baseline, this
work order, both source/test owners, and listed checker source.

## Pre-Flight Checks

Confirm clean worktree, exact dispatcher-provided execution HEAD, all three
allowed paths, zero staging, and pre-implementation autorun PASS before edits.

## Write Ownership

Worker owns only the three Allowed writes during execution. Reviewer owns
closure conversion and commit. Session steward owns protected continuity.

## Scope / Target / Owner Boundary

### Allowed reads

Repository-local startup, roadmap, baseline, source, package metadata, tests,
governance checkers, and accepted T0 evidence.

### Allowed writes

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.test.ts`
3. `docs/reviews/CVF_WEB_INHERITANCE_T1_WORKER_RETURN_2026-07-18.md`

### Forbidden scope

All other paths; existing module-definition changes; MAO entries; page,
navigation, package, adapter, route, README, browser, provider/live, public,
push, production, session, or commit mutation.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| accepted T0 | `docs/reviews/CVF_WEB_INHERITANCE_T0_COMPLETION_REVIEW_2026-07-18.md` | `90aa165c6` | SATISFIED |
| T1 roadmap release | current Web inheritance roadmap | `90aa165c6` | SATISFIED_FOR_T1_ONLY |
| T2-T5 | later independent T1 closure | N/A with reason: absent | HELD |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| registry array is the editable source | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | `MODULES` | `MODULES` | `ModuleDefinition[]` | ACCEPT |
| bounded runtime class exists | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | `RuntimeModuleClass` | `HAS_RUNTIME_CODE` | source type union | ACCEPT |
| bounded inherited exposure exists | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | `WebExposureState` | `PARTIAL_INHERITED` | source type union | ACCEPT |
| entries support empty action lists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | `ModuleDefinition` | `exposedActions` | `ModuleDefinition` | ACCEPT |
| summary derives total and exposure counts | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | `summarize` | `readOnlyVisible` | registry report summary | ACCEPT |
| focused test owns fake module paths and summary | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.test.ts` | `MODULE_PATHS`; enumeration test | `getRuntimeModuleRegistry` | Vitest suite | ACCEPT |
| Refinery verified package path | VALUE_SET | `EXTENSIONS/CVF_REFINERY/package.json` | name/version | `cvf-refinery` | package metadata | ACCEPT |
| Kernel verified package path | VALUE_SET | `EXTENSIONS/CVF_TRUTH_KERNEL/package.json` | name/version | `cvf-truth-kernel` | package metadata | ACCEPT |
| Flow verified package path | VALUE_SET | `EXTENSIONS/CVF_TRUTH_FLOW/package.json` | name/version | `cvf-truth-flow` | package metadata | ACCEPT |
| Web depends on all three | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependency rows 27-29 | `dependencies` | npm dependency map | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence |
|---|---|---|
| correct runtime-module truth | add exactly three SOT3 definitions | source diff plus entry assertions |
| avoid runnable overclaim | use `PARTIAL_INHERITED`, empty actions | focused negative boundary assertions |
| preserve current registry behavior | do not edit existing definitions or health functions | scoped diff and existing negative tests |
| independent closure before T2 | worker does not commit | worker return and reviewer-owned commit |

## Execution Plan

1. Capture clean execution HEAD and run pre-implementation gate.
2. Add `cvf-refinery`, `cvf-truth-kernel`, and `cvf-truth-flow` definitions.
3. Use each verified package path, `HAS_RUNTIME_CODE`,
   `PARTIAL_INHERITED`, and `exposedActions: []`.
4. Update fake workspace paths and expected summary from 10 to 13 modules,
   available 10 to 13, readOnlyVisible 2 to 5; keep webRunnable=1 and
   notExposed=7.
5. Assert all three entries' IDs, paths, class, exposure, and empty actions.
6. Run focused tests, cvf-web typecheck, file-size enforcement, and worker-fast.
7. Write the full worker return with exact command and git evidence.

## Evidence Requirements

Required command evidence:

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/lib/server/runtime-modules.test.ts
npm run check
Set-Location ../../..
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

If the package-manager command requires the repository's existing invocation
form, use that existing form and record the exact command; do not modify lock
files or dependencies.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `runtime-modules.ts` | add exactly three bounded SOT3 registry definitions |
| `runtime-modules.test.ts` | extend fake workspace, summary, and entry assertions |
| T1 worker return | record full evidence, changed set, no-commit statement, and return status |

## Required Artifact Manifest

| Required artifact | Owner | Required disposition |
|---|---|---|
| `runtime-modules.ts` | worker | modified within exact registry boundary |
| `runtime-modules.test.ts` | worker | modified with focused assertions |
| T1 worker return | worker | new, complete, unstaged, uncommitted |

## Acceptance Criteria

- AC-01: exactly three SOT3 definitions are added.
- AC-02: each definition is `HAS_RUNTIME_CODE` and `PARTIAL_INHERITED`.
- AC-03: each definition exposes zero actions.
- AC-04: focused suite proves total=13 and all three entry boundaries.
- AC-05: existing negative health cases pass unchanged.
- AC-06: typecheck and governed file-size gate pass.
- AC-07: exact three-path changed set, nothing staged, HEAD unchanged.
- AC-08: no forbidden scope or runnable/operator-action claim appears.

## Review Gate

The independent reviewer must recompute all three definitions, rerun the
focused suite and typecheck, inspect the full diff, confirm no existing module
definition changed, and own any repair, closure, and commit.

## Closure Checklist

- [x] execution HEAD matches dispatcher instruction;
- [x] three definitions and no others added;
- [x] summary and entry assertions pass;
- [x] no existing definition changed;
- [x] typecheck and file-size gate pass;
- [x] exact allowed changed set and no staging;
- [x] worker no-commit boundary honored;
- [x] independent reviewer closure accepted.

## Stop Conditions

Return `BLOCKED_WITH_REASON` before forbidden edits if source types do not
permit the required bounded classifications, the focused test owner is absent,
the execution HEAD differs, or completion requires any forbidden path.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all acceptance criteria and gates
pass with exactly three unstaged paths and unchanged HEAD. Otherwise return
`BLOCKED_WITH_REASON` with secret-safe command evidence.

## Operator Checkpoint

N/A with reason: the operator already authorized automatic continuation across
roadmap tranches. Independent T1 review remains mandatory before T2 release.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | operator request to continue the accepted Web inheritance roadmap |
| scopeClassification | bounded three-path repository-local registry/test change with narrow blast radius |
| riskSensitivity | no secret, provider, live, public-sync, production, or readiness claim; source overclaim remains reviewer-sensitive |
| routeMode | `SINGLE_AGENT_SINGLE_ROLE` selected route |
| roleSeparationBasis | one worker implements without commit; independent reviewer/closer owns evidence acceptance and commit |
| escalationCondition | return blocked on source contradiction, execution-head mismatch, or forbidden-scope need |
| externalSourceRoute | N/A with reason: no external source intake |

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation or checker failures directly. Ask no
preference question. Return only for a source contradiction, forbidden-scope
need, or missing authority that makes completion impossible.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | read-only module registry | truthful inventory only | source plus focused tests | existing report | `IMPLEMENT_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | no changed interface | no ingress, action, receipt, or mutation | no adapter output | parked | `N/A_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_SINGLE_ROLE` |
| rolePattern | one implementation worker followed by independent reviewer/closer |
| phase | dispatch then no-commit execution then reviewer closure then session sync |
| baseHeadFor(phase) | dispatchBaseHead=`884f69849`; executionBaseHead=dispatcher-provided post-dispatch session HEAD; closureBaseHead=executionBaseHead |
| changedSetScope(phase) | dispatch=baseline/work order/roadmap; execution=exact three allowed paths; closure=reviewer-owned artifacts; session=protected continuity only |
| traceScope(phase, actor) | each actor records only its commands, changed set, manifest delta, and boundary |
| commitOwner(phase) | dispatcher; none for worker; reviewer/closer; session-sync steward |
| crossBatchIsolation | T2-T5 and all forbidden lanes remain parked |
| nextMoveSurfaces | worker must not edit; session steward owns any separately authorized protected update |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_WEB_INHERITANCE_T1_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: the two source/test files, worker return, paired
baseline and work order, roadmap, and completion review; protected continuity
only in a separate session-sync commit.

closureOwner: CVF independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_INHERITANCE_T1_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/lib/server/runtime-modules.test.ts
npm run check
Set-Location ../../..
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; Work-Order Fulfillment Manifest; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source verification |
| claimBoundary | structural conformance does not replace implementation review |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T1 --title "SOT3 Runtime Module Registry Truth Correction" --date 2026-07-18 --base 884f69849 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact source, test, execution, evidence, and handoff contracts |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | none |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T1 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, repository search, artifact authoring, governance gates |
| Target paths | roadmap; paired T1 baseline; this work order |
| Allowed scope source | accepted T0 review and roadmap T1 release |
| Before status evidence | clean worktree at `884f69849` |
| After status evidence | exact three-path dispatch set pending commit |
| Diff evidence | material diff captured before commit |
| Approval boundary | T1 registry/test dispatch only |
| Claim boundary | no worker execution, Web action, MAO, provider/live, public, push, or production mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-t1-dispatch-2026-07-18` |
| Expected manifest | roadmap; baseline; work order |
| Actual changed set | exact three-path dispatch set |
| Manifest delta | MATCH expected after verification |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | static read-only registry truth correction and focused tests |
| claimDisposition | N/A with reason: no execution-control or enforcement behavior is implemented |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: registry visibility is not an action |
| invocationBoundary | exact T1 worker packet |
| interceptionBoundary | no IDE, shell, provider, filesystem, or agent-action interception claim |
| claimLanguage | add, classify, assert, and report only |
| forbiddenExpansion | pages, actions, MAO, provider/live, public-sync, push, production, universal inheritance claims |

## Current Runtime Freshness Verification

At dispatch base `884f69849`, the registry has ten definitions and zero SOT3
entries; the focused suite expects ten modules. All three SOT3 package roots and
cvf-web dependency rows exist. This packet authorizes static source/test
correction only and makes no provider or live-governance proof claim.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired T1 GC-018 baseline | `Status: CLOSED_PASS` | PASS |
| Work order status | this file | `Status: CLOSED_PASS` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WEB_INHERITANCE_T1_COMPLETION_REVIEW_2026-07-18.md` | `Status: REVIEWER_ACCEPTED` | PASS |
| Worker return | T1 worker return | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| Roadmap state | CVF Web inheritance roadmap | `Status: CVF_WEB_INHERITANCE_T1_PASS_T2_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | corpus registry generated aggregate | existing GC-051 coverage and drift check | PASS |
| Registry Markdown | corpus registry read model | existing GC-051 coverage; no source mutation needed | PASS |
| External evidence digest | N/A with reason: repository-local evidence only | none | N/A with reason |
| System loop interlock | N/A with reason: no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate session-sync commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: static registry projection only | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: no runtime query changed | N/A_WITH_REASON |
| Worker-return acceptance | independently recomputed | PASS |
| Closure claim | bounded registry truth only | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T1 dispatch; no public-sync action.

## Claim Boundary

This work order authorizes exactly three no-commit worker paths. It does not
authorize any other Web, MAO, package, route, UI, provider/live, public, push,
production, release, or session mutation.
