# CVF Agent Work Order - MAO Web Adoption And Source Seam Decision

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS

Batch ID: CVF-WEB-INHERITANCE-T3A

Dispatch base head: `296029998`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated source-audit worker

Reviewer/closer: CVF independent reviewer/closer

Worker return path:
`docs/reviews/CVF_WEB_INHERITANCE_T3A_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: execute only CVF-WEB-INHERITANCE-T3A as a no-commit source-audit worker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3A_MAO_WEB_ADOPTION_AND_SOURCE_SEAM_DECISION_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: use the dispatcher-provided post-dispatch session HEAD and
verify it before writing either output.

Current-time notes: source verification and artifact date are 2026-07-18.

Do-not-misread notes: this is a documentation-only source-seam decision, not
a MAO Web implementation, dependency install, page build, runtime connector,
worker launcher, or provider proof.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, roadmap, T0/T2 reviews, all cited MAO
owners, package metadata, and listed checker source before writing.

Return contract: leave exactly two allowed outputs unstaged and uncommitted and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Decide from current source how, or whether, cvf-web may safely inherit the MAO
operator readout. Resolve the dependency, persistence/replay, evidence,
liveness, milestone, configuration, privacy, build, and caller seams before
T3B implementation can be released.

## Agent Roles

- Worker: direct source audit, decision artifact, and worker-return evidence.
- Reviewer/closer: independent source recomputation, bounded repair, closure,
  and material commit.
- Session-sync steward: protected continuity update in a separate commit.

## Authority Chain

Operator standing continuation authority -> CVF Web inheritance roadmap ->
accepted T2 review at `609edffbe` -> this T3A packet -> no-commit worker ->
independent reviewer/closer -> session-sync steward.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V47_2026-07-18.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `DESIGN.md`
8. paired T3A baseline, roadmap, T0 ledger/review, T2 completion review, and
   every file in Source Verification

## Pre-Flight Checks

- capture and verify the instructed execution HEAD;
- require a clean start with no staged or unstaged path;
- run pre-implementation autorun against the real execution base;
- refresh all negative searches from current source; and
- stop before writing on an execution-head mismatch or forbidden-scope need.

## Worker Autonomy / No-Question Rule

Repair allowed-output checker or evidence defects directly. Return to the
orchestrator only for an execution-head mismatch, a required source outside
the repository, inability to resolve a required seam from current source, or
a need to edit any third path.

## Intake Role Routing Decision

routeMode: SINGLE_AGENT_SINGLE_ROLE selected route

Intake summary: repository-local architecture and source-seam audit.

Scope classification: two documentation outputs, no implementation.

Risk sensitivity: HIGH because guessed persistence or evidence semantics could
turn a read-only Web surface into a misleading operational claim.

Role separation: source-audit worker cannot accept or commit its own result.

Escalation condition: a decision requires external authority, new runtime
fields, or implementation to prove a claimed seam.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Disposition |
|---|---|---|---|
| T2 accepted | `docs/reviews/CVF_WEB_INHERITANCE_T2_COMPLETION_REVIEW_2026-07-18.md` | `609edffbe` | ACCEPT |
| T3A roadmap row | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | dispatcher material commit for this packet | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| control-plane dependency exists; execution-plane dependency does not | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies lines 20-35 | `dependencies` | npm manifest | ACCEPT |
| current Web source has no MAO symbol consumer | RUNTIME_BEHAVIOR | `docs/reviews/CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md` | WEB-05 through WEB-07 plus refreshed negative search | `WEB-05`; `WEB-06`; `WEB-07` | accepted inheritance ledger | ACCEPT |
| control plane exports resolver and composition | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.mao.barrel.ts` | lines 17 and 24 | `resolveRole`; `composeOrchestrationPlan` | control-plane MAO barrel | ACCEPT |
| execution plane exports the operational readout builder | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | lines 339-358 | `buildOperationalOperatorProjection` | execution-plane MAO barrel | ACCEPT |
| operational readout requires caller-supplied facts and has no runtime caller | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts` | lines 12-17 and 68-115 | `MaoOperationalOperatorProjectionInput` | operational projection contract | ACCEPT |
| durable store resumes one named graph and returns graph/events | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 98-175 | `resumeRun` | `MaoFileRunStore` | ACCEPT |
| deterministic task-state read model folds graph events | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | `buildReadModel` section | `buildReadModel` | generated MAO read model | ACCEPT |
| evidence ledger is instance-local and in-memory | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | lines 153-227 | `MaoEvidenceLedger` | evidence readout contract | ACCEPT |
| evidence milestones exclude per-heartbeat mirroring | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | lines 388-472 | `projectWorkspaceMilestones` | evidence milestone projection | ACCEPT |
| roadmap requires bounded MAO readout | VALUE_SET | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | Tranche Plan | `CVF-WEB-INHERITANCE-T3` | roadmap | ACCEPT |

## New Doc-Only Fields

| Field | Required value boundary |
|---|---|
| `sourceSeamDisposition` | exactly one allowed terminal decision token |
| `requiredOwnerChange` | existing path/symbol, proposed prerequisite, or N/A with reason |
| `t3bAllowedScopeCandidate` | exact candidate paths or N/A with reason |
| `claimableReadoutDimensions` | only directly source-backed dimensions |

## Scope / Target / Owner Boundary

The worker decides ownership and sequencing only. Current runtime owners remain
unchanged. Proposed T3B fields, paths, configuration, or functions must be
clearly labeled proposed and must not appear as existing Source Verification
facts.

## Allowed Scope

1. `docs/reviews/CVF_WEB_INHERITANCE_T3A_MAO_WEB_ADOPTION_AND_SOURCE_SEAM_DECISION_2026-07-18.md`
2. `docs/reviews/CVF_WEB_INHERITANCE_T3A_WORKER_RETURN_2026-07-18.md`

## Write Ownership

The worker owns only the two Allowed Scope outputs. The reviewer owns those
paths for closure conversion plus the paired baseline, work order, roadmap,
and T3A completion review. Continuity remains separately owned.

## Forbidden Scope

- do not edit any package, lockfile, runtime, source, test, page, component,
  route, API, config, environment, state, registry, or generated aggregate;
- do not treat event-ledger replay as evidence-ledger reconstruction without a
  direct source contract;
- do not invent or silently promote a package, field, function, path, enum,
  environment key, persistence format, run-list contract, or caller;
- do not launch a worker, write a run, call a provider, use network/browser,
  public-sync, push, release, or make a production action;
- do not implement T3B, T4, or T5; and
- do not stage, stash, commit, or edit session surfaces.

## Required Decision Contract

The decision artifact must select exactly one `sourceSeamDisposition`:

- `ADOPT_EXECUTION_PLANE_DEPENDENCY_WITH_VERIFIED_READ_SEAM` only when every
  run/evidence/milestone/liveness input has a current source owner and caller;
- `CONTROL_PLANE_ONLY_BOUNDED_PROJECTION` only when the roadmap outcome can be
  met without duplicating execution-plane semantics or claiming run evidence;
- `SPLIT_T3B_PREREQUISITE_OWNER_REQUIRED` when a missing persistence, replay,
  discovery, or caller owner must close before Web implementation; or
- `DEFER_WITH_REASON` when expected value does not justify adoption, with one
  concrete reopen condition.

No blended or provisional verdict is allowed.

## Required Source-Seam Matrix

| Required row | Required direct checks |
|---|---|
| package/dependency | manifest, lockfile, import graph, transitive source coupling |
| control-plane adoption | exact exported MAO symbols and their bounded value |
| execution-plane adoption | exact required exports and dependency impact |
| run discovery | whether current source can list run identities safely |
| durable replay | graph/event contract and failure behavior |
| evidence replay | persistence or reconstruction owner for `MaoEvidenceLedger` |
| task-state projection | `buildReadModel` inputs and safe output fields |
| liveness | source-backed heartbeat/timeout facts without triggering mutation |
| milestones | event versus evidence milestone semantics and exclusions |
| configuration | existing source-backed path/ID configuration or missing owner |
| privacy | fields allowed, redacted, hashed, or forbidden in Web output |
| Web caller | server-only adapter/page boundary and unavailable/empty behavior |
| verification | focused tests, typecheck/build impact, and no-live boundary |

Each final row must include current owner, verified contract, gap, T3B
implication, and terminal disposition.

## Execution Plan

1. Refresh package, lockfile, import, symbol, and page negative searches.
2. Read each control-plane and execution-plane owner cited by the matrix.
3. Separate run events, generated task state, evidence records, milestones,
   and liveness facts before evaluating Web suitability.
4. Complete all 13 matrix rows and challenge at least one alternative route.
5. Select exactly one decision token and specify T3B prerequisites/scope or a
   concrete defer reopen condition.
6. Run governed gates and return the exact two-path no-commit result.

## Required Artifact Manifest

| Required artifact | Expected result |
|---|---|
| T3A decision | one terminal source-seam matrix and exact next route |
| T3A worker return | commands, evidence, exact two-path boundary, no-commit proof |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| T3A decision | create source-cited matrix, decision rationale, candidate scope or reopen rule |
| T3A worker return | record direct reads, searches, gates, changed set, and no-commit evidence |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence |
|---|---|---|
| read-only MAO run/evidence/milestone/liveness projection | resolve every source and caller seam first | required source-seam matrix |
| no worker launch/provider/queue/autonomy | documentation-only forbidden scope | diff and command evidence |
| dependency-ordered tranches | T3B remains held until reviewer accepts one route | decision and completion review |
| truthful Web inheritance | separate dependency, symbol, caller, persistence, and UI claims | row-level dispositions |

## Verification / Evidence

Evidence must include direct file/line/symbol citations, refreshed negative
searches, exact terminal row count, one decision token, candidate T3B scope or
reopen condition, worker-return fast gate, file-size guard, exact changed set,
empty cached diff, and unchanged HEAD.

## Acceptance Criteria

- AC-01: all 13 required matrix rows are present and terminal.
- AC-02: event, task-state, evidence, milestone, and liveness contracts remain
  distinct and source-backed.
- AC-03: one allowed decision token is selected with value/risk rationale.
- AC-04: any T3B candidate lists exact prerequisites, source owners, proposed
  paths, verification, and privacy boundary without false existing-source
  claims.
- AC-05: a defer route has a concrete, checkable reopen condition.
- AC-06: exactly two outputs change; nothing is staged; execution HEAD is
  unchanged; all governed gates pass.

## Evidence Requirements

Do not cite provider-specific memory as authority. Record direct source
commands and distinguish a zero-hit search from an existence claim. Do not
report a gate as passing unless its final run exits zero.

## Review Gate

Independent reviewer must recompute every source seam and negative search,
challenge the selected decision against at least one alternative, confirm no
existing field was invented, and own any roadmap release or closure commit.

## Closure Checklist

- [x] execution HEAD matches dispatcher instruction;
- [x] all 13 source-seam rows are terminal and cited;
- [x] event and evidence ledgers are not conflated;
- [x] exactly one decision token is selected;
- [x] prerequisite-owner route and bounded T3B hold are complete;
- [x] exactly two worker paths changed and nothing was staged;
- [x] worker no-commit boundary was honored; and
- [x] independent reviewer accepted with bounded semantic repairs.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if required source is absent and no allowed
terminal gap disposition can record it, the execution HEAD mismatches, the
decision requires a third output, or a required claim can be proved only by
editing or executing a forbidden surface.

## Operator Checkpoint

N/A with reason: standing authorization releases this bounded T3A source
decision. Any provider/live, public, push, production, or materially broader
implementation remains outside this packet.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current source owners and two governed outputs | audit and decide only | source-seam matrix | no adapter implementation | `DOCUMENTATION_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no changed interface | no ingress, action, receipt, or mutation | no adapter output | parked | `N/A_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_SINGLE_ROLE` |
| rolePattern | one source-audit worker followed by independent reviewer/closer |
| phase | dispatch then no-commit audit then reviewer closure then session sync |
| baseHeadFor(phase) | dispatchBaseHead=`296029998`; executionBaseHead=dispatcher-provided post-dispatch session HEAD; closureBaseHead=executionBaseHead |
| changedSetScope(phase) | dispatch=roadmap/baseline/work order; execution=exact two outputs; closure=reviewer-owned artifacts; session=protected continuity only |
| traceScope(phase, actor) | each actor records only its own reads, commands, changed set, and boundary |
| commitOwner(phase) | dispatcher; none for worker; reviewer/closer; session-sync steward |
| crossBatchIsolation | T3B and T4-T5 remain parked; external mutation lanes remain parked |
| nextMoveSurfaces | worker must not edit; session steward owns protected updates separately |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_WEB_INHERITANCE_T3A_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: two worker outputs, paired baseline and work order,
roadmap, and completion review; continuity only in a separate commit.

closureOwner: CVF independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read checker source for its path and conditional
content. Section names in checklists must not use heading prefixes. The worker
return must use the full-gate shape and include corpus/rescan non-applicability
reasons on their verdict lines when those sections apply.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_INHERITANCE_T3A_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; Work-Order Fulfillment Manifest; Required Artifact Manifest; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source verification |
| claimBoundary | structural conformance does not select or validate the decision |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3A --title "MAO Web Adoption And Source Seam Decision" --date 2026-07-18 --base 296029998 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit and Web claim-boundary profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact source, contradiction, decision, matrix, output, handoff, and no-implementation boundaries |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | four fields listed in New Doc-Only Fields |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T3A dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | startup reads, source reads, repository search, scaffold helper, artifact authoring, governance gates |
| Target paths | roadmap; paired T3A baseline; this work order |
| Allowed scope source | accepted T2 review and roadmap T3 source contradiction |
| Before status evidence | clean worktree at `296029998` |
| After status evidence | exact three-path dispatch set pending commit |
| Diff evidence | material diff captured before commit |
| Approval boundary | documentation-only T3A source-seam decision dispatch |
| Claim boundary | no dependency, runtime, source, test, UI, provider/live, public, push, or production mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-t3a-dispatch-2026-07-18` |
| Expected manifest | roadmap; paired T3A baseline; this work order |
| Actual changed set | exact three-path dispatch set |
| Manifest delta | MATCH after verification |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only MAO Web source-seam decision |
| claimDisposition | N/A with reason: no execution-control or enforcement behavior is implemented |
| receiptEvidence | N/A with reason: source audit creates no runtime receipt |
| actionEvidence | N/A with reason: no command or mutation action is exposed |
| invocationBoundary | exact two-output T3A worker packet |
| interceptionBoundary | no IDE, shell, provider, filesystem, or agent-action interception claim |
| claimLanguage | read, verify, distinguish, decide, and report only |
| forbiddenExpansion | dependency install, runtime adapter, persistence, page, action, provider/live, public-sync, push, production |

## Current Runtime Freshness Verification

At dispatch base `296029998`, cvf-web has a control-plane dependency with no
MAO consumer and no execution-plane package row. The MAO operational
projection accepts caller-supplied in-memory evidence; the durable run store
replays graph events for one known graph. No current source owner bridges those
facts into a Web readout.

## Web/UI Claim Boundary

`DESIGN.md` was read. T3A changes no UI and proves no live-data, hosted,
production-ready, or operator-value behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T3A dispatch; no public-sync action.

## Claim Boundary

This work order authorizes exactly two no-commit documentation outputs for a
terminal source-seam decision. It does not authorize dependency, runtime,
source, test, UI, provider/live, public, push, release, production, or session
mutation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired T3A GC-018 baseline | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Completion or reviewer artifact | T3A completion review | `Status: REVIEWER_ACCEPTED_WITH_REPAIRS` | PASS |
| Worker return | T3A worker return | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS` | PASS |
| Roadmap state | CVF Web inheritance roadmap | `Status: CVF_WEB_INHERITANCE_T3A_PASS_T3P1_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | corpus registry generated aggregate | existing governed docs scope coverage; aggregate drift check passed | PASS |
| Registry Markdown | corpus registry read model | existing governed docs scope coverage | PASS |
| External evidence digest | N/A with reason: repository-local source audit | none | N/A with reason |
| System loop interlock | N/A with reason: no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate session-sync commit follows material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: documentation-only source decision | N/A_WITH_REASON |
| Query acceptance evidence | 13 terminal source-seam rows independently recomputed | PASS |
| Worker-return acceptance | exact two paths, unchanged HEAD, no staging, gates passed | PASS |
| Closure claim | split prerequisite owner required, with reviewer repairs | PASS |
