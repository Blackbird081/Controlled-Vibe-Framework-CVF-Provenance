# CVF Agent Work Order - QM Service-Token Replay Deduplication T1

Memory class: governed-worker-dispatch

docType: work_order

Status: APPROVED_FOR_EXECUTION

Date: 2026-09-14

Batch ID: QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 79927acaa1ecf6525bef92ab32a41145077bfe56

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT implementation worker in the shared Local workspace. Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md`.
Paired authority: `docs/baselines/CVF_GC018_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md`. Roadmap: `docs/roadmaps/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPLICATION_ROADMAP_2026-09-14.md`. Worker return: `docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_WORKER_RETURN_2026-09-14.md`.
Commit mode: WORKER_MUST_NOT_COMMIT. Capture executionBaseHead and status at start.
Required first actions: read startup/front door/handoff, external/local role methods, this authority pair, M5 record, exact source/test owners and applicable checker sources; run pre-implementation before edits.
Do not misread: process-local exact-request dedupe only. No distributed protection, M4 rotation/claims, protocol migration, real credentials, provider/live, network, public or deployment work.
Return contract: `COMPLETE_PENDING_REVIEW` with exact five-path delta, current focused proof, benchmark and worker-return fast gate. Local remains reviewer/closer.

## Purpose

Implement a bounded process-local replay ledger inside the current service-token verification owner so an exact valid signed request is accepted once and rejected on replay during the existing five-minute window. Preserve all existing HMAC/timestamp/token behavior and explicitly retain the cross-process limitation.

## Acceptance Table

| Outcome | Required evidence |
| --- | --- |
| Exact replay | same valid token/timestamp/body/signature returns true once and false on second use |
| Consumer proof | QBS route returns its normal first response and 401 on exact replay using direct route invocation |
| Non-poisoning | invalid token, signature, timestamp and stale requests do not reserve the later valid key |
| Independence | distinct valid tuples do not collide |
| Data boundary | ledger stores no raw token or body and emits no replay key |
| Capacity/lifecycle | fixed cap, expiry pruning, deterministic fail-closed exhaustion, no timer/background task |
| Compatibility | existing focused tests and TypeScript pass |
| Latency | paired local synthetic median <=0.10 ms, p95 <=0.25 ms, at least 50 paired samples |
| Claim | process-local only; no deployment-wide or live claim |

## Required Implementation Contract

1. Keep `verifyServiceTokenRequest` synchronous and its current boolean API. Validate configured/presented token, timestamp window and expected HMAC before any replay-ledger mutation.
2. Add a module-owned bounded process-local replay ledger. Derive a non-secret replay identity using a cryptographic digest of already-validated identity material. Never retain raw token, body, presented headers or credentials.
3. A first valid identity consumes one entry and returns true. An exact duplicate before expiry returns false. Invalid requests cannot consume entries.
4. Expire entries no later than the existing signature window. Prune deterministically on verification; add no timer, daemon or background I/O.
5. Use a fixed maximum entry count. When a new valid identity cannot be recorded because unexpired capacity is full, fail closed. Do not evict an unexpired entry merely to admit another request.
6. Provide a narrow test-only reset/configuration seam that cannot be supplied through HTTP, environment, CLI or serialized input. Production default remains enabled and bounded.
7. Do not alter signature inputs, route production files, auth precedence or error bodies. A method/path-binding redesign is outside T1.
8. Use synthetic values only. Do not read `process.env` beyond existing route behavior, execute an external request, start a server or call a provider.

## Latency Acceptance And Measurement

Create a deterministic local benchmark using installed TypeScript tooling and synthetic inputs. Compare the verifier path at dispatch HEAD with the changed path using the same fixture; measure first-use valid verification and rejected replay separately after warmup. Use at least 50 paired samples and report median/p95, Node version and fixture size. Added first-use median must be <=0.10 ms and p95 <=0.25 ms. These are bounded host measurements, not a universal SLA. One profiling/repair pass is allowed if exceeded; never raise thresholds silently.

## Write Ownership

Exactly five worker-owned paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/benchmark-service-token-replay-dedupe.ts`
- `docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_WORKER_RETURN_2026-09-14.md`

All other paths are read-only, including route production files, package manifests/locks, session state, roadmap, baseline, this work order, source mirrors and governance. No new dependency. If another owner is required, stop with evidence.

## Source Verification Block

| Fact | Source file | Verified section | Disposition |
| --- | --- | --- | --- |
| QM candidate | `docs/audits/CVF_QM_RUNTIME_VALUE_R1_2026-09-14.json` | M5 and `terminalValueDisposition` | ACCEPT |
| Current verifier | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `SERVICE_TOKEN_SIGNATURE_WINDOW_MS`; `verifyServiceTokenRequest`; `computeServiceRequestSignature` | ACCEPT |
| Current verifier tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | `service-token-auth` suite | ACCEPT |
| Named current consumer | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.ts` | `POST` calls `verifyServiceTokenRequest` | ACCEPT |
| Consumer test owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts` | QBS direct route suite | ACCEPT |
| Prior closure gate | `docs/reviews/CVF_OUTPUT-REDACTION-T1_COMPLETION_2026-09-14.md` | Decision | ACCEPT |

Current source hashes at dispatch: verifier `e2fa4b495a688becb3e5d550679d852d0f9e49d939846a4832c07b5552cad599`; verifier test `a149330043eb5a2865b1f3755d72822a478d9663285612b369bd0ac56f28c11c`; QBS route `11609d1ef4063662cf39f365387a1ee1d0705be64aad70c527fbeb0d510838fe`; QBS test `52d4d1da301f929f998351c07f74e4182a38542895eca49891cb96127d9f305a`; QM R1 audit `b3912cfe1a6e861abf78a579d50192bb0711f0fdf8e230be371950a618604889`.

## Authority Chain

Operator instruction on 2026-09-14 assigns Local as orchestrator/reviewer and an internal Claude worker as implementer. Roadmap, paired GC-018 and active handoff control. External QM evidence is advisory input; Local source verification and final disposition control.

## Verification Commands

From `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`:

- `npm exec --offline -- vitest run src/lib/service-token-auth.test.ts src/app/api/qbs/front-door-clarification/route.test.ts`
- `npm run check`
- `npm exec --offline -- tsx scripts/benchmark-service-token-replay-dedupe.ts`

From repository root:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`
- `python governance/compat/run_worker_return_fast_gate.py`

Run broader tests only for a named dependency contradiction. Record all actual exits and failed-run history.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NONE",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/roadmaps/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPLICATION_ROADMAP_2026-09-14.md",
    "docs/baselines/CVF_GC018_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/benchmark-service-token-replay-dedupe.ts",
    "docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_WORKER_RETURN_2026-09-14.md"
  ],
  "claims": ["Process-local exact valid-request replay deduplication only"],
  "requiredProof": ["unit replay and non-poisoning tests", "QBS route replay test", "bounded paired benchmark", "exact five-path return"],
  "operatorCheckpoints": ["scope expansion or distributed-store requirement only"],
  "forbiddenEffects": ["worker commit", "route production edit", "new dependency", "credential use", "network/provider call", "public sync", "deployment"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Worker Autonomy / No-Question Rule

Proceed autonomously for reversible edits, focused tests, benchmark and routine in-scope repair. Do not ask the operator to choose implementation details already fixed here. Stop only when a forbidden path/effect, authority contradiction, durable/shared storage need or risk above R2 is necessary.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | Local orchestrator/reviewer/closer; internal implementation worker |
| phase | process-local replay implementation then independent Local review |
| baseHeadFor(phase) | dispatchBaseHead=79927acaa1ecf6525bef92ab32a41145077bfe56; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | three dispatch artifacts; five worker paths; Local review/continuity |
| traceScope(phase, actor) | exact commands, hashes and changed set per actor |
| commitOwner(phase) | Local closer; worker forbidden |
| crossBatchIsolation | one worker lane; all other paths read-only |
| nextMoveSurfaces | Local-owned continuity only after review |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: internal implementation worker after pre-dispatch PASS and continuity projection
laneOwnedPaths: exactly five worker-owned paths
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return and exact changed-set reconciliation

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | three dispatch artifacts | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | three dispatch artifacts | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V60_2026-09-08.md` material-SHA marker plus active current-authority and next-move continuity | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | five worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | code, tests, benchmark, return | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | five worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker outputs and completion review | PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewed material | PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | committed ranges | PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all acceptance rows and required gates pass. Return `BLOCKED_WITH_REASON` with completed evidence and exact blocker otherwise. Do not self-close, commit, update continuity or issue a successor.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package; Return-Time Closeability Recheck; executionBaseHead; exact before/after status; exact five-path hashes; commands/results; zero commits and unauthorized mutations. Use `N/A_WITH_REASON` where valid. Status must be `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, never accepted/closed.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | work order and five worker paths | local reversible implementation; no commit | exact manifest and return | same workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none | no external/provider execution | N/A | no adapter | N/A_WITH_REASON |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Agent Roles

Worker implements the exact manifest. Local dispatches, reviews, closes and synchronizes. Operator transports the prompt; transport does not confer review authority. Worker must not commit or mutate session/governance surfaces.

## Intake Role Routing Decision

Intake summary: accepted QM R1 M5 evidence plus current CVF consumer verification.
Resolved route: INTERNAL_AGENT local implementation.
Promotion state: bounded implementation authority only.
Final decision owner: Local reviewer/closer.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_COMPLETION_2026-09-14.md`
reviewerOwnedClosurePaths: five worker outputs plus Local completion review; continuity separately.
Local verifies non-poisoning, secret-storage boundary, capacity/expiry, consumer behavior, latency and exact changed set.

## Closure Checklist

- Exact five-path manifest matches.
- Focused tests and TypeScript pass.
- Benchmark meets fixed ceilings.
- Process-local limitation is explicit.
- Full worker-return gate passes.
- Worker makes zero commits and no authority edits.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | dispatch prompt placement, source table, exact paths, closeability, INITIAL convergence, return packet and review budget |
| gateRunPurpose | confirm dispatch structure and return-time closeability |
| claimBoundary | no implementation acceptance yet |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | NOT_RUN_WITH_REASON: reused the accepted no-commit packet structure from OUTPUT-REDACTION-T1 and adapted it through `apply_patch` |
| generatedProfile | internal local implementation, no commit, INITIAL |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | exact replay, process boundary, capacity, tests and benchmark |
| checkerReadAheadConfirmation | applicable dispatch/quality/closeability contracts inspected |
| docOnlyNewFields | no new governance schema |
| claimBoundary | dispatch only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`. Returned defects: NONE_RETURNED; items=[], totalCandidates=0, truncated=false.

## Negative Search And Collision Discipline

Exact search query: `rg -n --fixed-strings "QM-SERVICE-TOKEN-REPLAY-DEDUPE" docs CVF_SESSION` plus `rg -n "service-token-auth|replay" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src -g "*.ts"`.

Exact search roots: `docs/`, `CVF_SESSION/`, and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/`.

| Search token | Same-token collision result | Disposition |
|---|---|---|
| `QM` | Same-token occurrences exist in accepted source evidence and current governed QM artifacts. | `NON_AUTHORITATIVE_COLLISION_FOR_EXACT_TRANCHE_NAMING` |
| `NOT_APPLICABLE_WITH_REASON` | Same-token occurrences exist as controlled governance status vocabulary. | `NON_AUTHORITATIVE_COLLISION_FOR_EXACT_TRANCHE_NAMING` |

Absent-versus-collision disposition: exact target-path result=`NEW_TARGET_PATHS`. Same-token collisions for `QM`, `service-token-auth`, `replay`, and `NOT_APPLICABLE_WITH_REASON` are expected and non-authoritative for naming: they are accepted source evidence, the current owner, unrelated approval/store logic, or controlled status vocabulary. They do not own this exact process-local request-deduplication tranche. No `BLOCKED_SOURCE_NOT_FOUND` disposition is asserted.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: reuse one accepted QM mechanism record; no legacy or source-wide corpus work.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | QM R1 M5 -> Local current-consumer verification -> bounded CVF-native implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` |
| Disposition | ADAPT without direct source copy |
| Claim boundary | no new source acquisition or completeness claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local dispatcher |
| Provider or surface | internal workspace |
| Session or invocation | QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1 dispatch |
| Working directory | repository root |
| Command or tool surface | startup/source reads, hashes, artifact authoring and pre-dispatch gate |
| Target paths | roadmap; baseline; this work order |
| Allowed scope source | operator instruction on 2026-09-14 |
| Before status evidence | clean worktree at HEAD `79927acaa1ecf6525bef92ab32a41145077bfe56` |
| After status evidence | exact three dispatch artifacts pending |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | exact five-path worker lane after dispatch continuity |
| Claim boundary | dispatch only |
| Agent type | dispatcher |
| Invocation ID | QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1-dispatch |
| Expected manifest | roadmap; baseline; this work order |
| Actual changed set | roadmap; baseline; this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

Process-local exact valid-request replay deduplication only. No key rotation, claims/audience, protocol migration, distributed protection, provider/live behavior, deployment, public export, QM closure or three-repository program closure.

## Required First Reads

Read `AGENTS.md`; `CVF_SESSION_MEMORY.md`; active bootstrap and handoff; both external/local coordination methods; roadmap; paired baseline; this work order; QM R1 M5 only; verifier and focused test/consumer owners; applicable checker sources.

## Pre-Flight Checks

Capture HEAD/status and source hashes. Run pre-implementation before edits. Stop on source drift or pending paths outside the declared lane. Do not edit authority files to make a gate pass.

## Execution Plan

Reproduce exact replay in a failing unit test; implement bounded post-validation consumption; prove non-poisoning, expiry and capacity; add QBS integration; benchmark; run required gates; return one consolidated packet.

## Evidence Requirements

Exact test names/results, benchmark recipe/results, source hashes, five-path delta, no raw-token/body retention, no commits, no unauthorized effects and all failed-run history.

## Acceptance Criteria

All Acceptance Table rows pass. Worker returns pending Local review and makes no closure or deployment claim.

## Review Gate

Local evaluates returned evidence without recreating implementation. Routine review is limited to security boundary, M5 behavior, capacity/expiry, latency and exact scope unless a new contradiction is named.

## Operator Checkpoint

No routine checkpoint inside exact scope. Escalate only a needed durable/shared store, signature change, forbidden path/effect or risk above R2.

## Foundation Storage Layout Block

The existing service-token owner contains the process-local ledger; existing unit and QBS route suites prove behavior; benchmark stays under existing cvf-web scripts. No new storage subsystem or framework.

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/roadmaps/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPLICATION_ROADMAP_2026-09-14.md"
}
```

## Current Runtime Freshness Verification

Current source is bound to dispatch HEAD and the five hashes recorded above. Worker rechecks those hashes before edits and stops on contract drift. QM source remains historical pinned evidence; no upstream freshness or execution claim is made.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: one accepted mechanism and a named current consumer are used; no corpus/rescan completeness claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded implementation of one accepted mechanism; no source-wide inventory or complete-reading claim.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local code/test/benchmark behavior only |
| claimDisposition | CLAIM_REJECTED: no live execution-control claim from dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | direct function and route-fixture tests only |
| interceptionBoundary | no network/runtime interception proved |
| claimLanguage | bounded synthetic process-local behavior |
| forbiddenExpansion | distributed, provider/live, credential, public and deployment claims |
