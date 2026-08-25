# CVF Agent Work Order - EAFR-R1 Amendment 1 Execution Anchor Repair

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-08-25

Batch ID: EAFR-R1-AMENDMENT-1

dispatchBaseHead: `8e6447a47`

executionBaseHead: capture committed Amendment 1 authority HEAD at worker start

closureBaseHead: reviewer captures after worker return

Commit mode: `WORKER_MUST_NOT_COMMIT`

rawMemoryReleased=false

Worker return path: `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

completionReviewPath: `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md`

## Dispatch Prompt Envelope

Role: delegated worker executing the parent EAFR-R1 implementation under this
command-only amendment.

Canonical packet: parent roadmap, baseline, work order, and paired Amendment 1
baseline/work order; Amendment 1 controls only where they conflict.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: dispatch continuity is committed through `8e6447a47`;
capture the actual clean current HEAD rather than assuming that short SHA.

Do-not-misread notes: the parent implementation scope and acceptance remain
unchanged; this amendment does not authorize a session path, live call, API
key, route/schema/policy change, stage, commit, push or public action.

Required first actions: read startup surfaces, parent packet, this paired
amendment, capture clean current HEAD, then run the replacement pre-flight.

Return contract: follow the parent worker-return contract and return exactly
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

operator.checkpoint.waiver: ACTIVE_BY_2026_08_25_DELEGATION

## Purpose

Replace only the stale parent pre-flight range with an execution-base range
that excludes already committed dispatch/session choreography.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1-AMENDMENT-1 --title "EAFR-R1 Amendment 1 Execution Anchor Repair" --date 2026-08-25 --base 8e6447a47 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact execution-anchor replacement and unchanged parent boundary |
| checkerReadAheadConfirmation | autorun, task-route, worker-return, handoff, active-state and dispatch-quality sources read |
| docOnlyNewFields | none |
| claimBoundary | command repair only; no implementation PASS claim |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R1-AMENDMENT-1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/baselines/CVF_GC018_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_AMENDMENT_1_2026-08-25.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_AMENDMENT_1_2026-08-25.md",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts",
    "docs/reviews/"
  ],
  "claims": ["pre-implementation uses the captured clean execution base"],
  "requiredProof": ["pre-implementation 80/80", "parent deterministic test and gate contract", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["worker stage or commit", "session edit", "provider/live/network call", "credential access", "deployment", "public write"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| operator | explicit orchestrator delegation, 2026-08-25 | ACCEPT |
| parent roadmap | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | ACCEPT |
| parent baseline/work order | committed at `4c5040573` | ACCEPT_EXCEPT_REPLACED_COMMAND |
| amendment baseline | paired Amendment 1 baseline | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| orchestrator | packet repair and commit | no worker implementation |
| worker | parent implementation and evidence | no review, commit or scope expansion |
| reviewer/closer | independent acceptance | closure only after evidence |

## Scope

Allowed scope: replace the parent three pre-flight base arguments at execution
time, then execute exactly the parent allowed source/test/return scope.

Forbidden scope: every path and action forbidden by the parent, plus all
session/continuity edits by the worker.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | command-anchor packet repair |
| scope classification | GOVERNANCE_COMMAND_REPAIR |
| primary task class | implementation |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| orchestration requirement | no-commit worker plus independent reviewer |
| role separation basis | worker cannot accept its own safety change |
| escalation condition | parent-scope contradiction, live need, forbidden edit or failed gate |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Required First Reads

Read every parent first-read plus this paired amendment. Amendment 1 controls
only the three commands below.

## Pre-Flight Checks

```powershell
git status --short --untracked-files=all
$eafrExecutionBase = git rev-parse HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $eafrExecutionBase --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base $eafrExecutionBase --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base $eafrExecutionBase --head HEAD --enforce
```

Expected: clean worktree before worker edits and all gates PASS. Record the
captured full SHA as `executionBaseHead`. Stop on any failure before editing.

## Worker Autonomy / No-Question Rule

Repair any gate failure inside the unchanged parent Allowed scope autonomously
and rerun it. Return `BLOCKED_WITH_REASON` only when repair
requires forbidden scope, claim/risk change, live/provider activity,
credentials, destructive action, public action, or contradicts source authority.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| parent hard-coded base crosses continuity | PACKET_GAP | `docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_2026-08-25.md` | Pre-Flight Checks | pre-implementation base | parent work order | ACCEPT |
| current-base control probe passes | GATE_EVIDENCE | `governance/compat/run_agent_autorun_workflow_gate.py` | pre-implementation | phase gate | autorun workflow | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | clean worktree; executionBaseHead; pathFamilies; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | confirm and record the command repair after negative/control probes; not first discovery |
| claimBoundary | checker PASS does not prove the parent source repair |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R1 fail-closed implementation | parent packet | parent source/test/return manifest | parent tests | PASS at authority level; implementation pending |
| independent closure | Review Gate | reviewer-owned completion | reviewer preflight | PASS |
| bounded execution | Pre-Flight Checks | captured executionBaseHead | pre-implementation 80/80 | PASS |

## Write Ownership

Write ownership remains exactly the three parent paths: two AIF helper/test
files and the named worker return. Amendment files are read-only to the worker.

## Execution Plan

1. Capture clean execution base and run replacement pre-flight.
2. Execute parent plan without any other amendment.
3. Return parent evidence under `WORKER_MUST_NOT_COMMIT`.

## Evidence Requirements

Record the full execution base, exact replacement commands/results, parent
tests/gates/hashes, actual status/diff and no-commit statement.

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git status --short --untracked-files=all
```

## Acceptance Criteria

- [ ] replacement pre-implementation gate passes before material edits;
- [ ] parent source/test acceptance is fully satisfied;
- [ ] no scope, live, credential, stage or commit expansion occurs.

## Review Gate

Worker return remains pending until the independent reviewer validates parent
and amendment evidence and owns any accepted commit.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit worker plus independent reviewer |
| phase | implementation pending review |
| baseHeadFor(phase) | dispatchBaseHead=8e6447a47; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | parent exact-three-path worker manifest |
| traceScope(phase, actor) | worker execution evidence; separate reviewer closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | parked RFR and later EAFR tranches untouched; clean worktree required |
| nextMoveSurfaces | parent worker return then independent review |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md` |
| reviewerOwnedClosurePaths | parent roadmap, baseline, work order, worker return, completion and continuity |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Findings / Position; Agent Operation Trace Block; Public Export
Disposition; executionBaseHead; git status --short; External Knowledge Intake
Routing; Rescan Intelligence Hardening; Corpus Completeness And Report
Integrity; Finding-To-Governance Learning Disposition; Machine Closure Package.
Include each real section or `N/A with reason`; do not list heading syntax as a
substitute for real sections.

## Closure Checklist

- execution base captured from clean current HEAD;
- replacement gates pass;
- parent closure checklist remains controlling;
- worker leaves all changes uncommitted.

## Return-To-Orchestrator Conditions

Return on any replacement-gate failure, dirty start, source contradiction,
forbidden path need, claim change, live/provider need or inability to satisfy
the unchanged parent acceptance.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | Codex local repository tools |
| Session or invocation | EAFR-R1 Amendment 1, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | negative/control pre-implementation probes and governed authoring |
| Target paths | paired amendment files |
| Allowed scope source | operator delegation and parent EAFR authority |
| Before status evidence | clean worktree at `8e6447a47` before amendment authoring |
| After status evidence | two untracked amendment files pending orchestrator commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | command repair only |
| Claim boundary | repo-local trace; no runtime interception claim |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `eafr-r1-amendment-1-2026-08-25` |
| Expected manifest | paired amendment baseline and work order |
| Actual changed set | paired amendment baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | pre-flight execution-base selection only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: command repair creates no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT through negative/control gate results |
| invocationBoundary | manual local governance commands |
| interceptionBoundary | no direct shell, git, IDE, provider or agent-runtime interception claim |
| claimLanguage | command-anchor correction only |
| forbiddenExpansion | no source-scope, live, credential, commit, deployment, public or readiness expansion |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: current packet command repair, not legacy or corpus work.

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
| --- | --- |
| Chain map | CVF external knowledge absorption chain |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: Amendment 1 derives from local gate probes, not advisory content |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired Amendment 1 authority |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | command repair only; no knowledge claim admitted |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private dispatch repair only.

## Claim Boundary

This amendment supersedes only the three parent pre-flight base arguments. All
other parent authority remains unchanged, including no live/API-key use and
`WORKER_MUST_NOT_COMMIT`.
