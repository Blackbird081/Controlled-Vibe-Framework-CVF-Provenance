# CVF Agent Work Order - MAO-OA-T6A Harder Candidate Direct Baseline Calibration

Memory class: governed-worker-dispatch

Status: DISPATCHED

Batch ID: MAO-OA-T6A

dispatchBaseHead: `95fb21377`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: delegated live-calibration worker

Canonical packet: this file

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Current-time notes: use the actual clean post-dispatch HEAD and configured local
key bootstrap on 2026-07-17; do not reuse prior result receipts.

Required first actions: read startup front doors, active handoff, baseline, this
work order, cited sources and guards; capture HEAD/status; confirm a supported
key exists without printing it.

Do-not-misread notes: one direct call maximum, zero retries, no MAO lane, no
comparison verdict, and exactly seven output paths.

Return contract: leave all changes uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create, test, execute, and record one fixed harder-candidate direct-provider
baseline so an independent reviewer can decide whether T6B is released.

## Authority Chain

Operator standing continuation instruction -> MAO operational-adoption roadmap
-> paired T6A GC-018 baseline -> this work order.

## Agent Roles

- Worker implements, tests, runs one call, and does not commit.
- Independent reviewer recomputes rubric, defects, call count, and secret safety.
- Designated closer owns material commit and completion review.
- Session-sync steward updates protected continuity from the accepted material
  commit recorded by the reviewer.

## Required First Reads

`CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; active handoff;
`docs/reference/guard_orientation/README.md`;
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
paired baseline; this packet; and every source below.

## Pre-Flight Checks

Capture `executionBaseHead`; require clean post-dispatch HEAD and no staged or
unstaged paths; confirm supported key presence without value output.

## Write Ownership

Exactly seven fulfillment paths. Reviewer completion, roadmap, registry entries
outside the one named entry, and protected continuity are forbidden.

## Evidence Requirements

Record exact call count, sanitized provider/model, latency, usage metadata when
returned, raw-response hash, parsed candidate, rubric rows, score, material
defects, diagnostic if failed, and command results. Never persist a key,
authorization header, or raw provider payload.

## Target / Source

Fixed task: plan a 48-hour evidence-backed release with two engineers and no
production mutation. JSON must contain `objective`, exactly three
`dependencies`, exactly three `risks` each with non-empty `mitigation`, exactly
three `verification` steps, `rollback`, and `stopCondition`.

## Scope / Target / Owner Boundary

Reuse Model Gateway `runLiveProof`; add one pure scorer and one runner. The
runner may attempt exactly one direct call. It must not invoke MAO worker,
reviewer, revision, closer, retry, or second call.

## Operator Checkpoint

Standing bounded continuation authority is sufficient inside this exact scope.
Any call, provider, model-lane, secret-handling, or path expansion returns to
the operator.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | calibrate one harder direct baseline before comparison |
| scopeClassification | bounded live runtime and evidence |
| riskSensitivity | R2 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | no-commit worker, independent reviewer/closer, session steward |
| escalationCondition | missing credential, source contradiction, secret exposure, or any additional call |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/MCP/readiness claim |
| Chain map route | current source verification, fresh live proof, and reviewer recomputation |
| Matching local-view guard | `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | paired baseline and this work order |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch |
| Claim boundary | no web, copied benchmark, or provider-local memory authority |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T5 accepted | `3e259039a`; `docs/reviews/CVF_MAO_OA_T5_COMPLETION_REVIEW_2026-07-17.md` | ACCEPT |
| harder-candidate discipline | concrete reopen conditions in `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | ACCEPT |
| live authority | operator standing continuation instruction | ACCEPT_BOUNDED_ONE_CALL |
| base freshness | clean `95fb21377` | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldTool | `governance/compat/build_dispatch_packet_scaffold.py` |
| packetKind | `runtime-provider-live` |
| scaffoldBase | `95fb21377` |
| scaffoldDisposition | completed against current sources and checkers |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id MAO-OA-T6A --title "Harder Candidate Direct Baseline Calibration" --date 2026-07-17 --base 95fb21377 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T5 accepted closure 3e259039a" --stdout --include-worker-return-skeleton` |
| generatedProfile | `runtime-provider-live` |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact manifest, rubric, release rule, and live controls |
| checkerReadAheadConfirmation | applicable checker sources were read before final packet text |
| docOnlyNewFields | `T6B_RELEASED`; `T6B_NOT_RELEASED` |
| claimBoundary | scaffold provenance does not prove execution or live results |

## Worker Autonomy / No-Question Rule

Resolve details inside seven-path scope. Stop for missing key, policy/secret
failure, source contradiction, or need for another call. Never rerun.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`MAO harder candidate live calibration`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch envelope; source columns; return shape; diagnostics; handoff; manifest; export token |
| gateRunPurpose | confirm and evidence that the one-call packet is source-faithful before execution |
| claimBoundary | validation is not live-result evidence |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| live call owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported function around line 188 | `runLiveProof` | Model Gateway live proof harness | ACCEPT |
| injectable fetch | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported type around line 51 | `LiveProofFetch` | Model Gateway live proof harness | ACCEPT |
| live options | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported interface at line 64 | `LiveProofHarnessOptions` | Model Gateway live proof harness | ACCEPT |
| live result | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported interface at line 94 | `LiveProofResult` | Model Gateway live proof harness | ACCEPT |
| credential reference | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | exported interface | `CredentialReference` | Model Gateway credential boundary | ACCEPT |
| key bootstrap pattern | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts` | environment constant and loader around lines 40-42 and 102 | `ENV_LOCAL` | prior MAO live runner | ACCEPT |
| diagnostic fields | EXISTS | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | required diagnostic fields | `Live Run Diagnostic` | governed diagnostic standard | ACCEPT |
| GC-051 source layout | EXISTS | `governance/compat/generate_corpus_scan_registry.py` | source directory and loader around lines 18 and 65 | `ENTRIES_DIR` | registry generator | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `T6B_RELEASED` | reviewer release token | NONE_AT_DISPATCH |
| `T6B_NOT_RELEASED` | reviewer hold token | NONE_AT_DISPATCH |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | YES_BOUNDED |
| freshnessVerificationMode | current-source verification plus one new call |
| requiredExecutionBase | clean post-dispatch HEAD captured by worker |
| staleEvidenceRule | prior pilot receipts cannot satisfy this packet |

## Negative Search And Collision Discipline

Search proposed basename and scorer symbols before create. If an exact owner
already exists, stop and report collision. Do not duplicate provider or key
ownership.

## Evidence Reuse And Encoding Plan

Reuse interfaces and secret-loading patterns, not prior results. Write ASCII.
Hash raw response in memory; persist only sanitized parsed content, metadata,
rubric evidence, and diagnostic.

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| expansionClass | one local direct-call runner plus pure scorer |
| providerOwner | existing Model Gateway harness |
| callBudget | one attempted call maximum |
| retryBudget | zero |
| governedComparison | forbidden in T6A |
| persistentRuntimeState | N/A with reason: evidence JSON only |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationRoot | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` |
| sourcePlacement | `src/mao/harder.value.candidate.contract.ts` |
| testPlacement | `tests/mao.harder.value.candidate.contract.test.ts` |
| runnerPlacement | `scripts/run-mao-oa-t6a-candidate-calibration.ts` |
| duplicateOwnerCheck | required before create |
| splitDisposition | focused new files; no near-threshold owner expanded |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Closure evidence |
|---|---|---|
| materially harder task | fixed 48-hour/two-engineer/no-production-mutation candidate | parsed candidate and rubric |
| predeclared hypothesis | T6B only at score <=80 or material defect | reviewer release token |
| real provider evidence | one live call | secret-safe receipt |
| bounded cost | one call, zero retries | call ledger |
| independent acceptance | no-commit worker and reviewer recomputation | completion review |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | create fixed task/schema, parser, rubric, defects, release-candidate result |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.harder.value.candidate.contract.test.ts` | create fake-output positive and negative tests |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | create one-call secret-safe runner |
| `docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json` | write sanitized call/rubric/diagnostic evidence |
| `docs/corpus-intelligence/registry/entries/mao-oa-t6a-harder-candidate-calibration-surfaces.json` | add exact changed-surface source entry |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate from sources |
| `docs/reviews/CVF_MAO_OA_T6A_WORKER_RETURN_2026-07-17.md` | return exact seven-path no-commit evidence |

## Required Artifact Manifest

| Artifact group | Owner | Required final status |
|---|---|---|
| seven paths | worker | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON |
| completion review | reviewer/closer | REVIEWER_TO_DECIDE |
| roadmap and continuity | reviewer/session steward | REVIEWER_TO_DECIDE |

## Execution Plan

1. Capture clean base; verify collision and key presence.
2. Implement fixed contract and deterministic rubric.
3. Prove behavior with fake outputs and typecheck.
4. Run exactly one direct call through `runLiveProof`.
5. Persist secret-safe evidence; add GC-051 entry; regenerate aggregate.
6. Run gates and return without staging or commit.

## Required Behavior

Rubric totals 100: 40 schema/completeness, 30 fixed-constraint correctness,
30 risk/verification specificity. Material defect means invalid JSON, missing
required key/cardinality, violation of no-production-mutation, or missing/empty
rollback or stop condition. `releaseCandidate` is true exactly when score <=80
or a material defect exists. Only the reviewer may release T6B.

## Focused Test Matrix

| Case | Expected result |
|---|---|
| complete faithful JSON | deterministic score; no invented defect |
| invalid JSON | material defect and fail-closed score |
| wrong cardinality | material defect |
| production mutation | material defect |
| empty rollback/stop | material defect |
| score 80 | release candidate true |
| score 81 without defect | release candidate false |
| repeat evaluation | identical result; no mutation |

## Mandatory Live Run Diagnostic Block

On failed, partial, timed-out, or empty call, record a secret-safe diagnostic
with stage, class, retryability, user action, provider/model when known, HTTP
status/latency when available, receipt/trace when available, and safe message.
Do not retry. Separate call-level result from event denominator.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MAO_OA_T6A_WORKER_RETURN_2026-07-17.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Return includes base, exact status/diff, seven-path manifest, call ledger,
tests/gates, secret scan, score/defects as worker evidence, no-commit proof, and
one terminal token.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker, independent reviewer/designated closer, session-sync steward |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=95fb21377; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly seven fulfillment paths |
| traceScope(phase, actor) | worker call receipt; reviewer recomputation; closer commit; steward continuity |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | clean worktree at `95fb21377`; T5 closure `3e259039a`; protected sync through `95fb21377` |
| Before status evidence | clean worktree at `95fb21377` |
| nextMoveSurfaces | reviewer/session steward only from the accepted material commit |

Before status evidence: clean worktree at `95fb21377`; no pending paths.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MAO_OA_T6A_HARDER_CANDIDATE_DIRECT_BASELINE_CALIBRATION_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | completion, baseline/work-order/roadmap dispositions, and disclosed narrow repair |
| closureOwner | independent reviewer/designated closer |
| workerCommitPermission | FORBIDDEN |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the harder task may expose score <=80 or a
material planning defect, making one bounded MAO comparison worth running.

Evidence Comparison Requirement: compare parsed response against every rubric
row and material-defect rule.

Contradiction Handling Requirement: score >80 with no defect blocks T6B and is
valid evidence; do not reframe it as failure.

Claim Update Requirement: reviewer records `T6B_RELEASED` or
`T6B_NOT_RELEASED`.

## Verification Commands

```powershell
cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run --config vitest.config.ts tests/mao.harder.value.candidate.contract.test.ts
npx tsc -p tsconfig.json --noEmit
npx tsx scripts/run-mao-oa-t6a-candidate-calibration.ts
cd ../..
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_corpus_scan_registry_changed_coverage.py
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git status --short
git diff --cached --name-only
git rev-parse --short HEAD
```

## Acceptance Criteria

- [ ] exactly one attempted call and zero retries;
- [ ] task/schema/rubric/defects implemented and tested;
- [ ] evidence is secret-safe with no raw payload;
- [ ] score/defects deterministic from sanitized content;
- [ ] GC-051 source and aggregate synchronized;
- [ ] exactly seven paths, nothing staged, HEAD unchanged;
- [ ] terminal worker return present.

## Review Gate

Reviewer independently parses/rescores, verifies count and secrets, reruns
tests/gates, and rejects any worker-authored release. T6B releases only at score
<=80 or material defect.

## Closure Diff Gate

Compare roadmap, baseline, work order, seven artifacts, return, commands, and
claims. Missing fields, ambiguous thresholds, stale sources, extra calls/paths,
secrets, or overclaims fail.

## Closure Checklist

- [ ] dependency evidence current;
- [ ] exact changed set verified;
- [ ] call count/no-retry recomputed;
- [ ] score/defects recomputed;
- [ ] secrets/diagnostics accepted;
- [ ] tests and gates pass;
- [ ] material commit reviewer-owned;
- [ ] continuity updated separately;
- [ ] next move exactly T6B dispatch or T7 closure authoring.

## Reviewer Closure Decision

OPEN_REVIEWER_TO_DECIDE

Worker must not edit this section.

## Machine Closure Package

| Field | Value |
|---|---|
| workerTerminalState | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON |
| requiredReviewerEvidence | score, defects, ledger, secret scan, tests, gates, diff/status |
| registryMutation | required for exact GC-051 pair only |
| protectedStateMutation | N/A with reason: reviewer/session steward only |
| materialCommit | N/A with reason: worker commit forbidden |
| publicMutation | N/A with reason: private provenance only |

## Acceptance Receipt Assertion Matrix

| Assertion | Evidence owner | Dispatch state |
|---|---|---|
| one call, zero retries | worker and reviewer | NOT_YET_EXECUTED |
| score/material defects | scorer and reviewer | NOT_YET_EXECUTED |
| secret safety | worker and reviewer | NOT_YET_EXECUTED |
| T6B release | reviewer only | NOT_YET_DECIDED |

## Return-To-Orchestrator Conditions

Missing credential, contradiction, secret exposure, extra-call need, provider
expansion, or path outside manifest blocks execution.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | MAO-OA-T6A dispatch 2026-07-17 |
| Working directory | repository root |
| Command or tool surface | source reads, resolver, scaffold, patch, gates |
| Target paths | baseline, work order, roadmap |
| Allowed scope source | operator instruction and roadmap |
| Before status evidence | clean worktree at `95fb21377`; `git status --short` empty |
| After status evidence | source-verified T6A packet |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring and one-call dispatch |
| Claim boundary | no call, score, defect, or value result at dispatch |
| Agent type | dispatcher |
| Invocation ID | `mao-oa-t6a-dispatch-2026-07-17` |
| Expected manifest | baseline, work order, roadmap |
| Actual changed set | baseline, work order, roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one direct harder-candidate calibration |
| claimDisposition | CLAIM_REJECTED: no result exists at dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | configured Alibaba/DashScope-compatible Model Gateway lane |
| interceptionBoundary | no IDE, MCP, web, proxy, wrapper, or production interception |
| claimLanguage | result requires fresh receipt and independent review |
| forbiddenExpansion | retry, second call, MAO comparison, UI, queue, public-sync, push, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance packet and evidence; no public export is authorized.

## Claim Boundary

This work order authorizes one direct calibration only. It does not authorize
or prove MAO comparison, quality gain, provider adoption, production readiness,
public readiness, or shipment.
