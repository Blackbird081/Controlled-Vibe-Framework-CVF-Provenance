# CVF Agent Work Order - MAO-T9 Independent Critique, Reconciliation, And Closure

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MAO-T9

dispatchBaseHead: `1b0835c17`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: independent critic worker

Canonical packet: this file

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Current-time notes: use actual clean post-dispatch HEAD.

Do-not-misread notes: critique and candidate reconciliation only; do not edit roadmap, runtime, session, public-sync, ASC aggregate, or gap registry.

Required first actions: read startup, full roadmap, T0-T8 closure artifacts, current sources, and checker sources; capture HEAD/status.

Return contract: produce exactly four outputs, leave them uncommitted, and return COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON.

## Purpose

Define the held independent critique and final reconciliation/closure tranche.

## Scope / Methodology

Independently source-check every finding, classify it, repair or reject with
reasons, run closure diff, decide export/catalog/gap disposition, then let the
session-sync steward update continuity separately.

## Worker Autonomy / No-Question Rule

Independently search and classify all material findings without asking how many
findings to produce. Do not create findings for wording preference. Stop only
for missing authority, scope expansion, or an unsafe external-state change.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Independently critique repository-local MAO roadmap execution evidence. |
| scopeClassification | bounded read-heavy critique and candidate reconciliation |
| riskSensitivity | R1 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | independent critic worker followed by Codex reviewer/closer |
| escalationCondition | any runtime, roadmap, session, public, ASC aggregate, or gap-registry mutation by worker |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T8 evidence | accepted at `f5a3def2a`; session sync `1b0835c17` | accepted evidence exists | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | finding dispositions, closure package, export enum |
| gateRunPurpose | held-packet confirmation |
| claimBoundary | no critique or closure yet |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| closure freshness checker | EXISTS | `governance/compat/check_roadmap_closure_freshness.py` | entrypoint | `main` | roadmap closure checker | ACCEPT |
| public export checker | EXISTS | `governance/compat/check_public_export_disposition.py` | entrypoint | `main` | export checker | ACCEPT |

## Work-Order Fulfillment Manifest

| Artifact | Required action |
|---|---|
| `docs/reviews/CVF_MAO_T9_INDEPENDENT_RUNTIME_FOUNDATION_CRITIQUE_2026-07-11.md` | independently source-verify T0-T8 and record all material findings |
| `docs/reviews/CVF_MAO_T9_FINDING_CLASSIFICATION_AND_RECONCILIATION_CANDIDATE_2026-07-11.md` | classify every finding and propose repair/rejection without mutating owners |
| `docs/reviews/CVF_MAO_T9_ROADMAP_CLOSURE_DIFF_EVIDENCE_2026-07-11.md` | map every roadmap requirement to current evidence or gap |
| `docs/reviews/CVF_MAO_T9_INDEPENDENT_CRITIQUE_WORKER_RETURN_2026-07-11.md` | return exactly four uncommitted outputs |

## Required Artifact Manifest

| Artifact | Owner | Required final status |
|---|---|---|
| four critique outputs | worker | COMPLETE_PENDING_REVIEW |
| roadmap/completion/catalog-gap decisions | reviewer/closer | REVIEWER_TO_DECIDE |

## Execution Plan

Verify T8 evidence and every critique claim, classify findings, repair within
scope, run closure diff, decide public/catalog/gap status, and prepare separate
session-sync instructions.

## Acceptance Criteria

- [x] T8 evidence dependency released;
- [ ] every finding has source-backed ACCEPT/CALIBRATE/REJECT/BLOCKED disposition;
- [ ] closure diff has no unresolved roadmap requirement;
- [ ] export and ASC/gap dispositions are explicit;
- [ ] worker does not commit or mutate session state.

## Evidence Requirements

Source citations, finding ledger, repair diffs, committed-range closure gates,
public disposition, and separate session-sync evidence.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | independent critic, reviewer/closer, session-sync steward |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=1b0835c17; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly four critique outputs; no owner-surface mutation |
| traceScope(phase, actor) | per-role trace at release |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material |
| crossBatchIsolation | clean worktree at `1b0835c17`; T8 closed; no overlap |
| Before status evidence | clean worktree at `1b0835c17`; T8 accepted; no pending paths |
| nextMoveSurfaces | session-sync steward only, using the accepted material closure commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_T9_INDEPENDENT_CRITIQUE_RECONCILIATION_AND_CLOSURE_COMPLETION_2026-07-11.md` |
| reviewerOwnedClosurePaths | critique, reconciliation, roadmap closure and export disposition |
| closureOwner | designated reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Control | Evidence |
|---|---|---|
| critique/classification | independent source verification | finding ledger |
| closure/export/admission | closure diff and explicit decisions | gates and review |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | independent source-backed critique and candidate reconciliation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: critique execution has not started |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no worker critique action at dispatch |
| invocationBoundary | local repository reads and governed review outputs only |
| interceptionBoundary | no provider, IDE, MCP, Web, wrapper, proxy, or runtime interception claim |
| claimLanguage | findings remain candidates until reviewer classification |
| forbiddenExpansion | no runtime, roadmap, session, public-sync, ASC aggregate, gap registry, provider, or T0-T8 rewrite |

## Claim Boundary

Independent critique and candidate reconciliation only. Reviewer/closer owns
all roadmap, export, catalog, gap, and session decisions.

## Authority Chain

Operator -> roadmap -> T8 evidence -> baseline -> work order.

## Agent Roles

Independent critic, reviewer/closer, and separate session-sync steward.

## Required First Reads

Startup, guards, baseline, work order, T8 evidence, roadmap and checker sources.

## Pre-Flight Checks

Refresh T8 evidence/range, anchors, critique independence and worktree.

## Write Ownership

Worker owns exactly four critique outputs and must not mutate owner surfaces.

## Review Gate

Source-backed finding classification, closure diff and committed-range gates.

## Closure Checklist

- [x] T8 complete; - [ ] findings classified; - [ ] closure diff reconciled; - [ ] export decided by reviewer.

## Return-To-Orchestrator Conditions

No execution while held; critic returns uncommitted packet for reviewer closure.

## Operator Checkpoint

Required for scope-expanding repairs or public export.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private workspace |
| Session or invocation | MAO-T9 held packet 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads and apply patch |
| Target paths | paired T9 packet |
| Allowed scope source | operator and roadmap |
| Before status evidence | clean worktree at `1b0835c17`; T8 accepted |
| After status evidence | source-verified DISPATCH_READY critique packet |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet preparation only |
| Claim boundary | no critique/closure executed |
| Agent type | dispatcher |
| Invocation ID | `mao-t9-held-2026-07-11` |
| Expected manifest | paired T9 packet |
| Actual changed set | captured before commit |
| Manifest delta | MATCH for dispatch authoring paths |
| Deletion or rename disposition | N/A with reason: none |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_T9_INDEPENDENT_CRITIQUE_WORKER_RETURN_2026-07-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required section names: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary; git status --short; Changed Files; No-Commit Statement.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind direct --batch-id MAO-T9 --title "Independent Critique Reconciliation And Closure" --date 2026-07-11 --base 1b0835c17 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | direct no-commit dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact critique outputs, role boundary, T8 dependency, sources, and anchors |
| checkerReadAheadConfirmation | dispatch, roadmap closure, public disposition, handoff, and worker-return checkers read |
| docOnlyNewFields | critique finding IDs and candidate disposition fields only |
| claimBoundary | authoring provenance only |

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_roadmap_closure_freshness.py --base 1b0835c17 --head HEAD
python governance/compat/check_public_export_disposition.py --base 1b0835c17 --head HEAD
git diff --check
git status --short
```
