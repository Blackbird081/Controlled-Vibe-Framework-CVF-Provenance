# CVF Agent Work Order Projection Automation T0 Landmark And Seam Audit

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-PROJECTION-AUTO-T0

Dispatch base head: `221698716`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_PROJECTION_AUTOMATION_T0_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: delegated source-audit worker.

Canonical packet: this work order.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture committed dispatch/session-sync HEAD.

Current-time notes: both prerequisite roadmaps are closed on 2026-07-18.

Do-not-misread notes: audit only; no tool, apply, commit, push, or provider call.

Required first actions: read startup front doors, guard orientation, literal gotchas, paired baseline, this packet, and cited source/checkers.

Return contract: leave two outputs uncommitted and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a terminal landmark/seam ledger that T1 can use to implement a safe
dry-run mapper without guessing paths, allowlists, remote rules, or cvf-web owners.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PROJECTION-AUTO-T0 --title "Projection Landmark And Mapper Seam Audit" --date 2026-07-18 --base 221698716 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated exact scope, verified sources, roles, evidence, and boundaries |
| checkerReadAheadConfirmation | dispatch-quality, structural, handoff, worker-return, public-disposition checkers |
| docOnlyNewFields | mapping and receipt proposals belong only to T0 ledger |
| claimBoundary | dispatch authoring provenance only |

## Authority Chain

Operator request -> closed projection and cvf-web roadmaps -> this packet ->
worker evidence -> independent reviewer -> later T1 packet.

## Agent Roles

Dispatcher owns packet; worker owns two outputs; reviewer/closer owns acceptance,
commit, roadmap release, and session sync.

## Required First Reads

Read both prerequisite completion reviews, `scripts/cvf-public-sync.ps1`,
workspace sync script, cvf-web runtime modules owner, paired baseline, and checkers.

## Pre-Flight Checks

Confirm clean HEAD, exact two paths, prerequisite commits, source paths, and
pre-implementation autorun PASS before writing.

## Write Ownership

Worker may write only the two allowed review outputs.

## Scope / Target / Owner Boundary

Allowed paths:

1. `docs/reviews/CVF_PROJECTION_AUTOMATION_T0_LANDMARK_AND_SEAM_LEDGER_2026-07-18.md`
2. `docs/reviews/CVF_PROJECTION_AUTOMATION_T0_WORKER_RETURN_2026-07-18.md`

Every other path is forbidden for mutation.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| private projection closure | T4 completion review | `9f7c92663` | PASS |
| cvf-web inheritance closure | T5 completion review | `64ec0f672` | PASS |

## Source Verification Block

Use and reconfirm all six ACCEPT rows in the paired baseline. A contradiction
requires `BLOCKED_WITH_REASON`; do not invent corrected symbols.

## Required Implementation

The ledger must include:

- landmark commits/artifacts for SOT3 CVF projection and cvf-web inheritance;
- exact provenance/public-sync/cvf-web roots and remote/status evidence;
- public-sync allowlist, mapped-file, dry-run, no-commit, and no-push seams;
- workspace updater patterns worth reusing;
- cvf-web package, registry, operator-page, and test seams;
- terminal mapping rows with `MECHANICAL`, `SEMANTIC_REVIEW`, `NOT_APPLICABLE_WITH_REASON`, or a source-block return disposition;
- proposed T1 manifest and receipt fields as doc-only new fields;
- fail-closed negative cases for missing root, wrong remote, dirty target, and path escape.

## Acceptance Criteria

- Every seed seam is terminal and source-cited.
- Presence is not treated as semantic inheritance.
- T1 inputs/outputs and forbidden mutations are unambiguous.
- No source, public-sync, or cvf-web file is edited.

## Execution Plan

Capture roots/status/remotes, read seams, build terminal rows, reconcile totals,
define doc-only T1 fields, run gates, and return without commit.

## Evidence Requirements

Record commands, source line/section, hashes where stable, exact row totals,
negative cases, changed set, staged state, and unchanged HEAD.

## Return-To-Orchestrator Conditions

Complete only with terminal rows and passing gates; otherwise stop with a
source-backed reason before forbidden mutation.

## Operator Checkpoint

N/A with reason: operator already authorized T0 audit; T1 remains reviewer-held.

## Worker Autonomy / No-Question Rule

Repair allowed-scope format defects directly. Return only for source
contradiction, missing authority, or forbidden-scope need.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator-requested local projection landmark and automation seam audit |
| scope classification | repository-local documentation audit; no external source absorption |
| risk sensitivity | R1; read-only source inspection and two governed outputs |
| escalation condition | source contradiction, missing authority, forbidden-scope requirement, or dirty foreign worktree |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to independent reviewer/closer closure conversion |

## Review Gate

Reviewer recomputes roots, remotes, allowlists, hashes, row totals, and T1 field
contract before releasing implementation.

## Closure Checklist

- [x] T0 dispatch scope is exactly two outputs.
- [x] T1 implementation remains dependency-held.
- [x] Public mutation and push remain forbidden.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> independent reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`221698716`; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exactly two review outputs |
| traceScope(phase, actor) | base, status, reads, rows, commands, diff, no-commit evidence |
| commitOwner(phase) | reviewer/closer; worker forbidden |
| crossBatchIsolation | clean worktree required; foreign changes block execution |
| nextMoveSurfaces | reviewer/session steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_PROJECTION_AUTOMATION_T0_COMPLETION_REVIEW_2026-07-18.md` |
| reviewerOwnedClosurePaths | baseline, work order, roadmap, completion review, session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PROJECTION_AUTOMATION_T0_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`projection automation baseline audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "projection automation baseline audit" --role dispatcher --lifecycle-phase pre-dispatch --json`

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | local source read -> terminal ledger -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | automation roadmap and future mapper manifest |
| Disposition | QUESTION_OR_HYPOTHESIS until source-verified; T0 performs that verification |
| Claim boundary | local source verification only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Source Verification Block; Required Implementation; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and evidence for T0 worker dispatch |
| claimBoundary | audit output shape only |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git status --short
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | projection automation T0 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, governed gates |
| Target paths | roadmap, baseline, work order |
| Allowed scope source | operator automation request and closed projection roadmap |
| Before status evidence | clean worktree at HEAD `221698716` |
| After status evidence | exact three-path dispatch pending commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T0 audit dispatch only |
| Claim boundary | no tool/public/provider/runtime mutation |
| Agent type | dispatcher |
| Invocation ID | `projection-automation-t0-dispatch-2026-07-18` |
| Expected manifest | roadmap, baseline, work order |
| Actual changed set | roadmap, baseline, work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | source-seam audit |
| claimDisposition | N/A with reason: no execution-control implementation |
| receiptEvidence | N/A with reason: T0 defines future receipt fields only |
| actionEvidence | N/A with reason: audit performs no target mutation |
| invocationBoundary | T0 no-commit worker |
| interceptionBoundary | no wrapper, provider, IDE, or runtime interception |
| claimLanguage | inspect, map, classify, and propose only |
| forbiddenExpansion | tool implementation, apply, commit, push, provider/live, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private audit only.

## Claim Boundary

This work order authorizes two documentation outputs only. It does not build or
run the mapper, mutate public-sync/cvf-web, commit, push, or call providers.
