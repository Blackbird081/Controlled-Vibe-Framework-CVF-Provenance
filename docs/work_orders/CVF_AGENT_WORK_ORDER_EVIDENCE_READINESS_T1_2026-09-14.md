# CVF Work Order - Evidence Readiness Foundation
Memory class: governed-worker-dispatch
docType: work_order
Status: CLOSED_PASS_BOUNDED
Date: 2026-09-14
Batch ID: EVIDENCE-READINESS-T1
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: 7a4501c5a20430c1283d02949537d0fc1b2d06a1
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: internal implementation worker. Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EVIDENCE_READINESS_T1_2026-09-14.md`.
Paired authority: `docs/baselines/CVF_GC018_EVIDENCE_READINESS_T1_2026-09-14.md`. Commit mode: WORKER_MUST_NOT_COMMIT.
Worker return path: `docs/reviews/CVF_EVIDENCE_READINESS_T1_WORKER_RETURN_2026-09-14.md`.
executionBaseHead: WORKER_MUST_CAPTURE_AT_START.
Current-time notes: 2026-09-14; recapture HEAD/status at worker start.
Do-not-misread notes: R4 repair parked; only foundation paths owned.
Required first actions: startup/front door/handoff, paired authority, guard orientation,
literal gotchas, named source owners; capture HEAD/status and parked-output hashes.
Return contract: COMPLETE_PENDING_REVIEW only after the acceptance table below passes.
Operator explicitly parks QM R4 finding repair and prioritizes this foundation.
The two existing R4 outputs remain untracked, read-only and byte-identical.
MATCH: reviewer SHA-256 verification matches the frozen hashes in Parked R4 Evidence.
Worker must not fix, stage, remove or reclassify them to make any gate pass.

## Purpose

Prevent repeated mechanical evidence defects before review across external-repository
audits and local projects, using the existing worker-return checker invocation.
This is a foundation implementation lane, not further QM audit or absorption.
No added standalone hook process, network call, whole-repository scan or human
checkpoint on the ordinary worker-return path. Measure overhead before release.

## Acceptance Table

| Outcome | Required evidence |
| --- | --- |
| Set accounting | Reject missing, duplicate, overlapping or unknown paths; exact candidate = selected + excluded partition; reported totals derived and reconciled |
| Read identity | Exact source root/pin/blob, line count and union of read spans; partial cannot satisfy full read; reusable evidence binds artifact digest and exact blob |
| Evidence projection | Audit content digest matches structured return binding; current counts agree; current placeholders rejected while labelled historical failures remain valid |
| Automatic entry | Existing worker-return quality gate calls shared validator; generated applicable dispatch/return skeletons contain the contract without operator reminder; omission/tampering cannot opt out |
| Bounded cost | No new top-level gate process; no network/upstream execution; no-op adds zero Git calls; source verification batched by root/pin; same-run reuse prevents duplicate reads |
| Negative proof | Minimal R4-shaped fixtures reproduce 37/39 mismatch, 41/60 missing-candidate mismatch, partial-as-full, missing hashes, stale digest and placeholders |
| Compatibility | Legacy unchanged artifacts retain existing checks; changed governed returns with applicable declared evidence cannot silently bypass; non-corpus project returns avoid mandatory corpus ledgers |
| Semantics boundary | PASS certifies evidence consistency and bound source identity, never actual human/agent reading, discovery completeness outside the declared set, or correctness of behavior claims |
| Handoff | Exact owned delta, no commit, R4 outputs byte-identical, complete test/benchmark/gate history |

## Required Implementation Contract

1. Extend the existing quality checker through a reusable, importable validator
   (`worker_evidence_readiness.py`). Keep data-model validation pure where possible;
   use one bounded resolver for source bytes and artifact digests. Do not add a
   second checker invocation to hook catalogs or a new governance framework.
2. Define one compact versioned evidence binding in the existing quality standard.
   Bind report, audit digest, declared candidate manifest and processing rows.
   Support multiple source roots, immutable Git blobs and exact file snapshots for
   non-Git local projects. Keep paths normalized and source-root relative. Reject
   traversal, unsafe symlinks, ambiguous refs, duplicate JSON keys and invalid types.
   Never execute recorded shell queries or source code to validate a receipt.
3. A row records path, source identity, blob/content digest, line count, actual read
   spans and read/reuse/exclusion status. Validate bounds, overlap policy and full
   span coverage. Read reuse points to an immutable prior artifact digest and row;
   changed source identity invalidates reuse. Evidence is an attestation, not a
   machine proof that an agent read it. A known candidate cannot disappear through
   counts, aliases or an unnamed aggregate exclusion.
4. Accept an independent declared discovery manifest and reconcile its exact set
   with processing rows. A checker cannot prove a search was exhaustive or an
   exclusion semantically valid; expose these as reviewer obligations. Store
   reproducible query metadata, but never rerun arbitrary command strings. Do not
   hard-code QM path names, 19/41/60 counts or one audit schema as the only model.
5. Read only declared changed evidence and bound dependencies. Reject current
   readiness placeholders, count drift and stale audit digest. Historical fail/fix
   entries stay explicit and do not trip a blanket recursive token grep. Avoid a
   self-hash cycle: final JSON hashes into Markdown, not both directions.
6. Derive applicability from trusted work-order scope/contract and recognized
   structured evidence, not a worker-selected opt-out. Update dispatch and return
   scaffold owners to include the compact acceptance/binding block automatically
   for relevant tasks. Ordinary source-change projects need their own applicable
   evidence types, not a forced exhaustive corpus scan. Unknown relevant schemas
   must produce a clear diagnostic, not fabricated compliance.
7. Integrate inside check_worker_return_quality_gate's existing path collection;
   standalone CLI, fast gate, reviewer-fast and pre-commit must reach the validator.
   Prove audit-only changes cannot bypass validation when its bound Markdown is
   unchanged; find the reverse binding through a bounded declared index/manifest
   or existing packet references, never a full repository search. Use an explicit
   migration rule for unchanged historical packets and the parked R4 evidence.
8. On input mismatch, report all mechanically knowable issues in one deterministic
   report with JSON pointers/paths, expected and observed values. Do not rerun or
   reconstruct semantic review. Block COMPLETE_PENDING_REVIEW for applicable
   inconsistent evidence; BLOCKED_WITH_REASON may disclose incomplete evidence
   but must not carry a successful readiness result.
9. Reuse parsed bytes and Git batch results within one invocation. Persistent
   caching is optional only if correctness and bounded invalidation are proven;
   prefer no persistent cache over another authority surface. No repeated full
   test suite, network scan, watcher or daemon in ordinary return validation.
10. Preserve current guard behavior and R4 failure evidence. New enforcement is
    forward-scoped by an explicit contract/activation rule, not by arbitrary
    filename exemptions. Reproduce legacy R4 defects in synthetic fixtures without
    editing the parked originals. Unsupported out-of-scope legacy packets are
    labelled legacy/unvalidated by the new layer; do not claim they passed it.

## Latency Acceptance And Measurement

Measure same-host baseline and changed checker using repeated paired runs after
warmup, retaining raw timings, median and p95 plus file/byte/Git-process counts.
Cases: no eligible return; one 60-row packet; one 1000-row packet; audit-only drift;
same packet reached twice in-process. Compare the existing end-to-end command too.
Acceptance budgets: no-op zero new Git/network/subprocess calls and <=5 ms median
increment; 60-row incremental validator <=100 ms median and <=250 ms p95; 1000-row
<=500 ms median and <=1 s p95 on this workspace, measured separately from baseline
checker startup. No statistically meaningful end-to-end regression outside measured
noise; disclose variance instead of claiming zero cost. These are ceilings, not a
license to add that latency routinely. Optimize before return if over budget;
if still over budget report BLOCKED_WITH_REASON, no operator reminder required.
Do not run benchmarking in production hooks. Commit compact measured results in
the worker return; no new benchmark service or repeated reviewer benchmark needed.

## Write Ownership

Worker owns exactly these nine paths:

- `governance/compat/worker_evidence_readiness.py`
- `governance/compat/test_worker_evidence_readiness.py`
- `governance/compat/check_worker_return_quality_gate.py`
- `governance/compat/test_check_worker_return_quality_gate.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md`
- `docs/reviews/CVF_EVIDENCE_READINESS_T1_WORKER_RETURN_2026-09-14.md`

All other paths are read-only. Existing R4 outputs are pre-existing untracked
operator work, not this lane's deliverables. Hash both before/after. Tests may use
isolated temporary Git repositories outside the workspace; no commits here.
If a real dependency requires another path, return the exact source-backed need;
do not edit hooks/checkers outside this list or suppress existing failures.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Existing checker validates return shape | LOCAL_SOURCE | governance/compat/check_worker_return_quality_gate.py | diagnose and run | diagnose | return quality owner | ACCEPT |
| Existing fast gate invokes quality checker | LOCAL_SOURCE | governance/compat/run_worker_return_fast_gate.py | build_commands | worker-return quality gate | no-commit fast gate | ACCEPT |
| Reviewer path already invokes quality checker | LOCAL_SOURCE | governance/compat/local_governance_hook_catalog_reviewer_fast.py | REVIEWER_FAST_CHECKS | REVIEWER_FAST_CHECKS | reviewer-fast catalog | ACCEPT |
| Commit path invokes quality checker | LOCAL_SOURCE | governance/compat/local_governance_hook_catalog_pre_commit.py | PRE_COMMIT_CHECKS | PRE_COMMIT_CHECKS | pre-commit catalog | ACCEPT |
| Return skeleton is shared authoring owner | LOCAL_SOURCE | governance/compat/build_worker_return_skeleton_scaffold.py | module and render functions | render_scec_outcome_block | return scaffold | ACCEPT |
| Current standard is structural | LOCAL_STANDARD | docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md | Purpose and Required Worker-Return Shape | worker-return shape | canonical quality standard | ACCEPT |

## Authority Chain

Operator instruction on 2026-09-14 explicitly parks R4 findings and prioritizes reusable low-latency foundation hardening -> AGENTS.md -> `docs/baselines/CVF_GC018_EVIDENCE_READINESS_T1_2026-09-14.md` -> this packet. No source-program exit or new external repository admission.

## Parked R4 Evidence

Operator checkpoint: R4 finding repair PARKED_BY_OPERATOR_PRIORITY until this
foundation lane is accepted and Local explicitly releases the retained findings.
ProgramId DOMAIN-PILOT-THREE-REPO-2026-09 remains active, all three repos INCOMPLETE.
Frozen inputs:

- docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json SHA-256 0ef9a50b98de55c3ff40c05b6fc4a1f719efe4872d67af57bcb3ec599f2e559a
- docs/reviews/CVF_QM_RUNTIME_VALUE_R4_WORKER_RETURN_2026-09-14.md SHA-256 341c8f4a7eb677a86a4385483939f2b8de54e77bda6041ab9f297b3a5f0d2349

Neither input is accepted. R4 worker ownership is suspended during this lane.
These are diagnostic inputs only and must not be copied wholesale into fixtures.

## Verification Commands

Run focused validator tests plus existing quality/scaffold regressions:
`python -m pytest governance/compat/test_worker_evidence_readiness.py governance/compat/test_check_worker_return_quality_gate.py governance/compat/test_build_dispatch_packet_scaffold.py -q`.
Run `python governance/compat/run_worker_return_fast_gate.py`; preserve actual
outcomes and prior failures. Static checker proof requires no provider call.
Run pre-implementation before editing; use captured executionBaseHead for ranges.
Record expected parked legacy diagnostics separately; do not fix R4 to pass.
If a legacy failure blocks the full chain, report the exact boundary to Local.
Return-time hashes must match the two parked inputs above.

## Core Guard Self-Protection Authorization

Operator authorization: explicit request to prioritize this foundation upgrade,
wire it automatically, and avoid increased latency across future repos/projects.
Authorized guard-maintenance scope is exactly the worker list plus dispatcher
baseline/work order and active continuity. Changes to checker semantics within
that list are authorized only for evidence-readiness enforcement, regression tests
and automatic scaffold binding. No unrelated hook/catalog/guard weakening.
Protected paths:

- `governance/compat/worker_evidence_readiness.py`
- `governance/compat/test_worker_evidence_readiness.py`
- `governance/compat/check_worker_return_quality_gate.py`
- `governance/compat/test_check_worker_return_quality_gate.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`

Rollback boundary: revert only this lane; preserve prior receipts, R4 files and
all accepted source tranches. No upstream execution/provider/public/deploy.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EVIDENCE-READINESS-T1",
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
    "governance/compat/worker_evidence_readiness.py",
    "governance/compat/test_worker_evidence_readiness.py",
    "governance/compat/check_worker_return_quality_gate.py",
    "governance/compat/test_check_worker_return_quality_gate.py",
    "governance/compat/build_worker_return_skeleton_scaffold.py",
    "governance/compat/build_dispatch_packet_scaffold.py",
    "governance/compat/test_build_dispatch_packet_scaffold.py",
    "docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md",
    "docs/reviews/CVF_EVIDENCE_READINESS_T1_WORKER_RETURN_2026-09-14.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_EVIDENCE_READINESS_T1_2026-09-14.md",
    "docs/baselines/CVF_GC018_EVIDENCE_READINESS_T1_2026-09-14.md",
    "docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json",
    "docs/reviews/CVF_QM_RUNTIME_VALUE_R4_WORKER_RETURN_2026-09-14.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_QM_RUNTIME_VALUE_R4_2026-09-14.md",
    "CVF_SESSION",
    "CVF_SESSION_MEMORY.md",
    "AGENT_HANDOFF_V60_2026-09-08.md"
  ],
  "claims": [
    "Deterministic evidence consistency only; measured bounded overhead"
  ],
  "requiredProof": [
    "Set and identity regressions",
    "Existing gate integration and omission resistance",
    "Paired latency measurements"
  ],
  "operatorCheckpoints": [
    "Scope expansion only"
  ],
  "forbiddenEffects": [
    "Worker commit",
    "Upstream execution",
    "Network",
    "Provider calls",
    "R4 finding repair"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Worker Autonomy / No-Question Rule

Proceed autonomously through all in-scope evidence. Resolve routine choices by
the packet and cited authority. Do not pause for the operator to say `next` or
ask which hypothesis to inspect first. If a stop condition occurs, preserve
completed evidence and return `BLOCKED_WITH_REASON`; do not widen scope or
substitute another repository.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | Local author/reviewer/closer; internal evidence worker |
| phase | evidence-readiness implementation then independent Local review |
| baseHeadFor(phase) | dispatchBaseHead=7a4501c5a20430c1283d02949537d0fc1b2d06a1; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch pair and priority projection; then nine worker paths; then Local review/continuity |
| traceScope(phase, actor) | exact commands, hashes, mirror state, and changed set for each actor |
| commitOwner(phase) | Local closer; worker forbidden |
| crossBatchIsolation | foundation worker active; QM R4 parked; no concurrent repository mutation |
| nextMoveSurfaces | active-program state and Local-owned completion/continuity only after review |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: internal foundation worker after committed dispatch
laneOwnedPaths: exactly the nine worker-owned paths; mirror read-only
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
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired dispatch documents | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired dispatch documents | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V60_2026-09-08.md` material-SHA marker plus active program and current authority | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | exact worker-owned outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| source_identity_license | WORKER_RETURN | worker | IMPLEMENTATION | helper, integration, tests, standard and return | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| inventory_depth_value | WORKER_RETURN | worker | IMPLEMENTATION | helper, integration, tests, standard and return | EXACT_PATHS | closer | MATERIAL_COMMIT | source_identity_license |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | helper, integration, tests, standard and return | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, inventory_depth_value |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker-owned outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker outputs and completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact reviewed material set | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | completionReviewPath | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | Local continuity paths | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | exact reviewed ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all criteria and gates pass. Return
`BLOCKED_WITH_REASON` with completed partial evidence and the exact stop
condition otherwise. Never self-close, self-accept, or issue a successor.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: EVIDENCE-READINESS-T1
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

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "EVIDENCE-READINESS-T1",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

This independent lane has no predecessor. Do not bind it to the stopped
aggregate recovery chain or use that chain's blocker count as this lane's
closure evidence.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The Markdown return must include:

- `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON`;
- exact HEAD/status before and after;
- exact parked-input hashes before and after;
- output paths and hashes;
- focused and integration test evidence plus measured latency;
- acceptance table with actual evidence for each row;
- material contradictions and retained unknowns;
- explicit statement that QM and the parent program remain open;
- commands run and exit results;
- confirmation of zero commits and zero unauthorized mutations.

Do not label the return `ACCEPTED_REVIEW`, `CLOSED_PASS_BOUNDED`, or equivalent.
Only Local may review, accept, update program state, select implementation, or
issue the next independent lane.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | Paired work order and nine implementation/evidence paths | Local implementation and pending return | Exact manifest and authority | Internal relay; no adapter needed | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | No external interface selected | No CLI/MCP or provider invocation | Private owner comparison requires local inspection | No external consumer requirement; adapter deferred | N/A_WITH_REASON |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order with no public artifact or sync scope.

## Agent Roles

Worker implements the exact manifest; Local dispatches, reviews, closes and synchronizes continuity. Operator relays to internal worker. No external invocation. Worker has no commit or R4-repair authority.

## Intake Role Routing Decision

Intake summary: operator parks R4 repair and prioritizes reusable evidence readiness.
Escalation condition: source-backed out-of-manifest dependency or unmet measured latency budget; return bounded evidence without widening scope.

| Field | Value |
| --- | --- |
| canonical route mode | MULTI_AGENT_SINGLE_ROLE |
| selected role route | Internal worker implementation; Local independent reviewer/closer |
| Scope classification | Bounded protected governance maintenance |
| External-agent role | NOT_INVOKED; no CLI/MCP adapter or provider calls |
| Disposition | ACCEPT |

## Reviewer Closure Conversion

completionReviewPath: docs/reviews/CVF_EVIDENCE_READINESS_T1_COMPLETION_2026-09-14.md
reviewerOwnedClosurePaths: worker manifest, completion, source registry entries if required, separate continuity.
Local consumes tests/benchmark output and samples malformed set/identity/omission paths;
no duplicate full read or routine repeated benchmark. A consolidated contradiction
report precedes any rework. Closure requires actual integration, no legacy bypass
and measured latency; only then resume parked R4 with existing findings preserved.

## Closure Checklist

- Exact manifest and parked-input hashes match.
- Focused and integration tests pass.
- Measured cost meets budgets; no automatic extra scan/process.
- Full return gate results disclosed.
- Worker does not commit or self-accept.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | governance/compat/check_worker_return_quality_gate.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py |
| literalTokensReviewed | diagnose, run, REQUIRED_HEADINGS, changed-path collection, protected path ownership and INITIAL convergence |
| gateRunPurpose | Confirm dispatch structure and closeability |
| claimBoundary | No implementation or semantic evidence acceptance yet |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | NOT_RUN_WITH_REASON: build_dispatch_packet_scaffold.py; reused prior contract sections while authoring compact implementation scope |
| generatedProfile | protected governance, no-commit, INITIAL |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | New requirements, automatic integration, migration, latency budgets and parked R4 boundaries |
| checkerReadAheadConfirmation | Quality checker, gate call sites and current contract sources inspected |
| docOnlyNewFields | Reusable evidence-readiness acceptance matrix |
| claimBoundary | Dispatch only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-machine-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`; riskCeiling=MEDIUM.
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class governance-machine-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`.
Returned defects: NONE_RETURNED; items=[], totalCandidates=0, truncated=false on 2026-09-14.

## Negative Search And Collision Discipline

New EVIDENCE-READINESS-T1 packet/output names checked for collisions before writing. Existing R4 files are expected frozen inputs, not owned output collisions.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: deterministic quality-control maintenance; no legacy knowledge payload or new runtime absorption owner.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | Existing worker-return readiness owner enhancement |
| Matching local-view guard | governance/compat/check_worker_return_quality_gate.py |
| Owner surface | docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md |
| Disposition | Internal deterministic governance hardening only |
| Claim boundary | No external source acquisition or acceptance |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local dispatcher; internal worker after relay |
| Provider or surface | Local shared workspace |
| Session or invocation | EVIDENCE-READINESS-T1 |
| Working directory | repository root |
| Command or tool surface | source reads, Python, Git and governance gates |
| Target paths | paired dispatch; worker nine paths; Local continuity |
| Allowed scope source | operator priority change on 2026-09-14 |
| Before status evidence | HEAD 7a4501c5a20430c1283d02949537d0fc1b2d06a1; tracked worktree clean; two untracked parked R4 outputs explicitly retained (whole worktree is not clean) |
| After status evidence | dispatch/continuity authored; R4 outputs unchanged |
| Diff evidence | git diff --name-status; git status --short |
| Approval boundary | Exact foundation scope only |
| Claim boundary | No implementation acceptance in dispatch |
| Agent type | orchestrator / internal worker |
| Invocation ID | EVIDENCE-READINESS-T1-DISPATCH |
| Expected manifest | paired baseline/work order and Local continuity; worker manifest separately above |
| Actual changed set | Local reports dispatch delta; worker must record exact paths and parked-input MATCH |
| Manifest delta | Compare by phase; existing R4 untracked inputs excluded from this lane's delta |
| Deletion or rename disposition | none authorized |

## Claim Boundary

This packet authorizes local checker/scaffold implementation, tests and measured performance. It does not prove actual reading or semantic correctness, close R4, absorb QM code, or open provider/live/public/deployment. R4 findings remain parked until reviewer release.

## Required First Reads
Startup front door/bootstrap and active handoff; baseline; acceptance table;
guard orientation and literal gotchas; source-verification owners and their tests.

## Pre-Flight Checks
Capture executionBaseHead and status; verify two parked R4 hashes; inspect call
sites, run pre-implementation, record baseline measurements before changes.

## Execution Plan
Implement pure validation and fixtures, integrate existing checker, bind authoring
scaffolds, run regressions and paired timing, then return exact evidence.

## Evidence Requirements
Source-backed integration, independent negative fixtures, measured timings and
parked-input hashes. Preserve failed runs; no placeholder PASS or semantic claim.

## Acceptance Criteria
All rows in Acceptance Table and Latency Acceptance And Measurement must pass;
a legacy or outside-scope blocker is disclosed without changing parked evidence.

## Review Gate
Local consumes valid test and timing results, checks omission resistance and one
malformed identity/set fixture. Rerun only for a named contradiction with expected
information gain. Consolidate all known findings before a repair dispatch.

## Operator Checkpoint
R4 finding repair remains PARKED_BY_OPERATOR_PRIORITY. No routine confirmation;
Local releases R4 only after foundation acceptance. Scope expansion remains separate.

## Foundation Storage Layout Block
Extend existing governance/compat and the current worker-return quality standard.
No new root, service, registry aggregate or public package. Helper/test are bounded
siblings; canonical authoring owners provide automatic future discoverability.

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
  "parentArtifact": "docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md"
}
```


## Current Runtime Freshness Verification

Source inspection at dispatchBaseHead confirms diagnose/run in the quality checker
validate structural Markdown fields; build_commands in the fast gate and the
REVIEWER_FAST_CHECKS/PRE_COMMIT_CHECKS catalogs already invoke that checker.
The new evidence validator is proposed implementation, not an existing runtime
capability. No provider or production-runtime claim is made.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_EVIDENCE_READINESS_T1_2026-09-14.md | Original dispatch retained; closure decision in this review | PASS |
| Completion or reviewer artifact | docs/reviews/CVF_EVIDENCE_READINESS_T1_COMPLETION_2026-09-14.md | bounded reviewer acceptance | PASS |
| Roadmap state | N/A | standalone foundation work order | N/A with reason: no roadmap closure |
| Registry JSON | CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json | source program remains open | PASS |
| Registry Markdown | docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md | existing registry retained; no new source scan or package admission | PASS |
| External evidence digest | N/A | no new external evidence accepted | N/A with reason: deterministic local checker |
| System loop interlock | N/A | no runtime transition | N/A with reason: local validation only |
| Session continuity | CVF_SESSION/state/entries/nextAllowedMove.json | separate post-material synchronization | N/A with reason: separate continuity batch |


Closure authority: docs/reviews/CVF_EVIDENCE_READINESS_T1_COMPLETION_2026-09-14.md.
Historical dispatch instructions above are retained; Local accepts the foundation
and releases bounded R4 review on explicit operator continuation.

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| Focused regression | 206 passed, 2 capability skips | PASS |
| Existing fast chain | 68/68 | PASS |
| Source execution | zero upstream/provider calls | PASS |
| R4 frozen evidence | original hashes unchanged during foundation work | PASS |
| Latency | paired measurements within stated budgets and noise limits | PASS |


## Reviewer-Owned Packaging Extension

Operator continuation authorizes Local closure repair. The original worker
manifest remains historical; reviewer modularization for the size guard adds:

- `governance/compat/worker_evidence_contract.py`
- `governance/compat/worker_evidence_sources.py`
- `governance/compat/test_worker_evidence_readiness_git.py`
- `governance/compat/test_build_dispatch_evidence_scaffold.py`
