# CVF Agent Work Order - MAO-LIVE-T1 Provider Adapter Value Pilot

Memory class: governed-worker-dispatch

Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN

Batch ID: MAO-LIVE-T1

dispatchBaseHead: `93662e2a2`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated live-pilot worker

Canonical packet: this file

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Current-time notes: use actual clean post-dispatch HEAD and configured local key bootstrap.

Do-not-misread notes: maximum four live calls; no UI, durable queue, public-sync, provider parity, production claim, or prompt tuning.

Required first actions: read startup, roadmap, baseline, cited source/checkers; capture HEAD/status and confirm key presence without printing it.

Return contract: produce exactly six outputs, run required tests/live proof/gates, leave uncommitted, return COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON.

## Purpose

Implement and evaluate one thin MAO-to-Model-Gateway live bridge against a
same-task direct-call baseline.

## Scope / Methodology

Use one provider lane, identical task/model/rubric, one direct call, then one
worker and identity-distinct reviewer; allow at most one repair and one final
closer decision. Stop at four calls total.

## Worker Autonomy / No-Question Rule

Resolve allowed-scope implementation details from verified sources. Stop only
for missing authority, source contradiction, key/policy/secret failure, or need
to exceed four calls. Never rerun before diagnosing the prior failure.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | reuse repository-local MAO and Model Gateway live contracts |
| scopeClassification | bounded live runtime adapter and comparative evidence |
| riskSensitivity | R2 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | worker, independent reviewer, designated closer |
| escalationCondition | credential/policy failure, ambiguous side effect, secret exposure, fifth call, or owner-surface expansion |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| MAO foundation | `29c55ca36` | ACCEPT |
| live health | `a0b40ecfb` | ACCEPT |
| roadmap | `82b3fb511` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live multi-agent provider adapter pilot`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch envelope, source columns, return shape, live diagnostics, Delta fields, handoff fields, export token, trace labels |
| gateRunPurpose | dispatch confirmation |
| claimBoundary | one live comparison only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| execute adapter factory | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported factory | `createOpenAiCompatibleExecuteAdapter` | Model Gateway live harness | ACCEPT |
| harness result | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | result interface | `LiveProofResult` | Model Gateway live harness | ACCEPT |
| MAO invocation adapter | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | adapter class | `MaoDelegationAdapter` | MAO delegation adapter | ACCEPT |
| MAO invocation receipt | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | receipt interface | `MaoInvocationReceipt` | MAO delegation adapter | ACCEPT |
| review/closer chain | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/representative.pilot.contract.ts` | phase functions | `runReviewerPhase` | MAO representative pilot | ACCEPT |
| local key loading | RUNTIME_BEHAVIOR | `scripts/run_cvf_release_gate_bundle.py` | env bootstrap | `bootstrap_live_provider_env` | release gate bundle | ACCEPT |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` | create thin bridge/comparison contract |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.live.provider.value.pilot.test.ts` | deterministic unit/negative tests with fake fetch only |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | bounded exports |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts` | secret-safe live runner and four-call enforcement |
| `docs/reviews/CVF_MAO_LIVE_T1_COMPARATIVE_LIVE_EVIDENCE_2026-07-12.md` | record direct/MAO metrics, diagnostics and verdict |
| `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_WORKER_RETURN_2026-07-12.md` | exact six-path no-commit return |

## Required Artifact Manifest

| Artifact group | Owner | Required final status |
|---|---|---|
| six manifest outputs | worker | COMPLETE_PENDING_REVIEW |
| completion/roadmap/session decisions | reviewer/closer | REVIEWER_TO_DECIDE |

## Execution Plan

Implement bridge and fakes; pass focused tests/typecheck; load key without
printing; run direct and governed lanes once; diagnose before retry; calculate
latency/call/usage/receipt/quality comparison; return one terminal value verdict.

## Acceptance Criteria

- [x] identical task, model lane, rubric and secret-safe input;
- [x] four calls maximum and one revision maximum;
- [x] independent reviewer and designated closer enforced;
- [x] no failed call or retry occurred;
- [x] receipts contain no raw key or raw provider payload;
- [x] verdict is VALUE_NOT_PROVEN;
- [x] worker did not commit.

## Evidence Requirements

Exact call count, per-lane latency/usage, quality rubric scores, receipt
completeness, diagnostics, secrets scan, focused tests, typecheck, diff/status.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker, independent reviewer, designated closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=93662e2a2; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly six manifest outputs |
| traceScope(phase, actor) | live call and role receipts per actor |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree at `93662e2a2`; MAO foundation closed |
| Before status evidence | clean worktree at dispatchBaseHead `93662e2a2`; no pending paths |
| nextMoveSurfaces | reviewer/session steward only using accepted closure commit |

Before status evidence: clean worktree at `93662e2a2`; no pending paths.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_COMPLETION_2026-07-12.md` |
| reviewerOwnedClosurePaths | completion, roadmap verdict, GC-051, session sync |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Control | Evidence |
|---|---|---|
| same-task comparison | shared fixture/model/rubric | comparative packet |
| four-call budget | runner hard ceiling | call ledger |
| fail-closed roles | MAO identity/closer contracts | focused negatives |
| value decision | terminal enum | metrics and reviewer recomputation |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_WORKER_RETURN_2026-07-12.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | YES_BOUNDED |
| freshnessVerificationMode | FRESH_LIVE_RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reviews/CVF_MAO_POST_CLOSURE_LIVE_GOVERNANCE_PROOF_2026-07-12.md` |
| requiredFutureAction | run the new MAO bridge, not merely the generic release bundle |

## MCP/CLI Adapter Boundary

| Field | Value |
|---|---|
| Adapter scope | local TypeScript live runner only |
| No-runtime-overclaim | no MCP/CLI product adapter, interception, wrapper enforcement, or production command surface |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one live same-task direct-versus-MAO value comparison |
| claimDisposition | CLAIM_REJECTED: no result exists at dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker has not run live pilot |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: implementation has not started |
| invocationBoundary | configured provider through existing Model Gateway live adapter |
| interceptionBoundary | no IDE/MCP/Web/proxy/wrapper interception |
| claimLanguage | verdict requires fresh secret-safe receipts |
| forbiddenExpansion | no durable queue, UI, public-sync, provider parity, production, or fifth call |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private workspace |
| Session or invocation | MAO-LIVE-T1 dispatch 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | source reads, resolver, scaffold, patch, gates |
| Target paths | paired baseline and work order |
| Allowed scope source | operator and MAO-LIVE roadmap |
| Before status evidence | clean worktree at `93662e2a2`; no pending paths |
| After status evidence | source-verified packet, later closed VALUE_NOT_PROVEN |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring only |
| Claim boundary | no new API call or result claim |
| Agent type | dispatcher |
| Invocation ID | `mao-live-t1-dispatch-2026-07-12` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Verification Commands

```powershell
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run --config vitest.config.ts tests/mao.live.provider.value.pilot.test.ts
npx tsc -p tsconfig.json --noEmit
cd ../..
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Authority Chain

Operator -> MAO-LIVE roadmap -> GC-018 baseline -> this work order.

## Agent Roles

Worker implements/runs without commit; independent reviewer recomputes value;
designated closer decides acceptance; session steward updates continuity.

## Required First Reads

Startup front doors, guard orientation, literal gotchas, roadmap, baseline, this
work order, cited MAO/Model Gateway sources, and live diagnostic authority.

## Pre-Flight Checks

Capture clean HEAD/status, confirm key presence without printing, verify call
counter starts at zero, and run pre-implementation autorun gate.

## Write Ownership

Worker owns exactly six manifest outputs. Reviewer owns completion, GC-051,
roadmap verdict, and session surfaces.

## Review Gate

Independent receipt/metric recomputation, focused tests/typecheck, secrets scan,
worker-return fast gate, and committed-range closure gates.

## Closure Checklist

- [ ] six outputs only; - [ ] call count at most four; - [ ] diagnostics complete; - [ ] terminal value verdict; - [ ] no worker commit.

## Return-To-Orchestrator Conditions

Return BLOCKED_WITH_REASON on credential/policy failure, secret risk, ambiguous
side effect, source contradiction, fifth-call need, or forbidden scope.

## Operator Checkpoint

Required for any fifth call, new provider lane, prompt tuning, durable queue,
UI, public-sync, production claim, or broader roadmap.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing execution-plane MAO source/test/scripts |
| Storage decision | add one bridge module, one test, one runner; evidence under dated reviews |
| Existing aggregate impact | bounded `src/mao/index.ts` export only |
| Generated state impact | none |
| Durable governance boundary | no hidden store; secret-safe review packets only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

One private bounded live value pilot only; no production or broader authorization.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id MAO-LIVE-T1 --title "Live Provider Adapter Value Pilot" --date 2026-07-12 --base 93662e2a2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | runtime-provider-live plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact sources, outputs, budgets, diagnostics and boundaries |
| checkerReadAheadConfirmation | dispatch, return, handoff, Delta, public and trace checkers read |
| docOnlyNewFields | comparative metrics and value verdict |
| claimBoundary | authoring provenance only |
