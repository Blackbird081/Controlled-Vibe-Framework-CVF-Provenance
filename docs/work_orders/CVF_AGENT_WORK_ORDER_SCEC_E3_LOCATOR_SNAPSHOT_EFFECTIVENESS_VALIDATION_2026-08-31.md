# CVF Agent Work Order - SCEC-E3 Locator Snapshot Effectiveness Validation

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: SCEC-E3

Dispatch base head: `8db4e9f87e4f4d63f0844e368dd4d80cf6fed3ba`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md`

successorTrancheOpened: NO

## Dispatch Prompt Envelope

Role: external governance effectiveness-validation worker for SCEC-E3.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_2026-08-31.md`.

Paired baseline: `docs/baselines/CVF_GC018_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_2026-08-31.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: packet authored on 2026-08-31 from clean committed base
`8db4e9f87e4f4d63f0844e368dd4d80cf6fed3ba`; T1-R3 is accepted with reviewer
repair at `008ff0685`.

Do-not-misread notes: this is validation-only. Do not edit checker, tests,
standard, ADIF, fixtures, session state, GC010, or product/runtime sources.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired packet, SCEC standard/checker/tests, T1-R3 return, E2 evidence,
ADIF-0055, and worker-output checker sources; then run pre-implementation.

Return contract: create exactly two authorized uncommitted artifacts; run all
named gates; return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Evaluate accepted T1-R3 material `008ff0685` without modifying it. Construct
fresh cases, record exact results and select one terminal foundation verdict.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "scec-locator-snapshot-effectiveness-validation",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [], "resolved": [], "retained": [],
    "new": [], "reopened": [], "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0, "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "SCEC-E3-VALIDATION-SEED",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/baselines/CVF_GC018_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_2026-08-31.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The worker return uses ordinal 1 and this work order's exact raw SHA-256. An
effective verdict retains empty blockers with `CONTINUE_BOUNDED` and
`NO_SUCCESSOR`. A bypass becomes one precisely named current foundation
blocker using `ROOT_CONTRACT_REQUIRED` and `INTEGRATED_ROOT_CONTRACT`.
`successorTrancheOpened: NO` is invariant.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: EXTERNAL_AGENT_CLI_MCP
parentAssignmentId: SCEC-E3
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 1
usageAvailability: KNOWN_FOR_ADMISSION
quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

## Scope / Target / Owner Boundary

In scope: read-only accepted standard/checker/tests/T1-R3 return; fresh
ephemeral harness; exactly two new Markdown outputs.

Authorized outputs:

1. `docs/assessments/CVF_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_2026-08-31.md`
2. `docs/reviews/CVF_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md`

No other path may change. Temporary harness files must remain outside governed
repository paths and be removed before handoff.

## Write Ownership

Worker owns only the two authorized Markdown outputs. Every source, checker,
test, fixture, standard, ADIF, dispatch, session, product and runtime path is
read-only. Reviewer/closer alone owns material and continuity commits.

## Authority Chain

1. Active SCEC standard.
2. Accepted checker behavior at `008ff0685`.
3. Reviewer-corrected T1-R3 return and its immutable digest
   `f4575b71c794efd1e682a4f0450a97ecab32fbd379bf7dbafbe222baa9e2f2ed`.
4. Paired E3 baseline and this work order.
5. Worker results remain recommendations until independent review.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | Transfers the packet and retains all expansion checkpoints. |
| Dispatcher | Defines cases, mechanical verdicts, and exact scope. |
| External worker | Builds fresh cases, writes two outputs, runs gates, does not commit. |
| Reviewer/closer | Independently reruns adversarial probes and owns acceptance/commits. |

## Dual Agent Surface Matrix

| Surface | Disposition | Evidence boundary |
|---|---|---|
| INTERNAL_AGENT | REVIEWER_ONLY | Orchestrator/reviewer validates and closes. |
| EXTERNAL_AGENT_CLI_MCP | AUTHORIZED_ONCE | One no-commit invocation, ceiling 1. |
| Adapter boundary | DOCUMENTATION_ONLY_NO_RUNTIME_ADAPTER | File handoff only; no interception or runtime claim. |

## Required First Reads

1. startup bootstrap, memory, and active handoff;
2. guard orientation and literal gotchas;
3. paired E3 baseline and work order;
4. active SCEC standard;
5. accepted T1-R3 worker return;
6. checker and focused test source in full;
7. accepted E2 assessment/return for the exact historical probe;
8. ADIF-0055 and applicable output checkers.

## Pre-Flight Checks

Capture HEAD/status and packet hashes. Confirm both outputs are absent and HEAD
equals committed dispatch HEAD. Run:

`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 8db4e9f87e4f4d63f0844e368dd4d80cf6fed3ba --head HEAD`

Stop on unexpected changes. Use no credentials, provider, network, install, or
live proof.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "SCEC-E3",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["docs/baselines", "docs/work_orders", "docs/assessments", "docs/reviews"],
  "claims": ["SCEC locator snapshot effectiveness"],
  "requiredProof": ["fresh adversarial matrix", "resolver call ledger", "exact E2 replay", "positive controls", "independent review"],
  "operatorCheckpoints": ["foundation source change", "product runtime implementation", "provider live or public action"],
  "forbiddenEffects": ["checker or source edit", "GC010 product edit", "provider or network execution", "public sync or deployment", "worker commit"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE

intakeSummary: repository-owned foundation effectiveness validation

scopeClassification: VALIDATION_ONLY_GOVERNANCE

riskSensitivity: HIGH_LOCAL_GOVERNANCE_EVIDENCE

escalationCondition: any accepted negative, rejected valid control, second
resolver read, forbidden-path need, provider/live need, or authority expansion
returns to the orchestrator and does not self-dispatch.

## Execution Plan

1. Read contract and implementation, but do not copy committed test payloads.
2. Build a fresh ephemeral case factory and resolver call ledger.
3. Run all mandatory cases and record expected/observed validity, codes, calls,
   hashes, and snapshot order.
4. Run focused/direct gates as comparison evidence only.
5. Select the verdict mechanically and write both outputs.
6. Rerun final gates and return uncommitted.

## Implementation Requirements

The assessment answers all ten questions:

1. Which standard clauses and symbols own locator and snapshot behavior?
2. How are cases independent from committed fixture payloads?
3. Does exact E2 artifact/hash/sentinel replay fail with the correct code?
4. Do two valid bindings sharing one path cause exactly one resolver call?
5. Can a second resolver snapshot influence a later binding in the same tree?
6. Is the same snapshot cache inherited by predecessor revalidation?
7. Do absent, ambiguous, non-canonical, invalid-UTF-8, unreadable/non-file, and
   hash-mismatch cases fail with exact codes and appropriate cascade behavior?
8. Do accepted-review, executable-proof, shared-path, and predecessor controls
   pass?
9. Did any observation contradict the T1-R3 contract or reveal a residual?
10. Which verdict follows, what is proven, and what remains parked/unproven?

Required case IDs:

- `EXACT_E2_ABSENT_LOCATOR_REPLAY`
- `SHARED_PATH_TWO_VALID_BINDINGS_ONE_READ`
- `CHANGING_SHARED_PATH_SECOND_SNAPSHOT_CANNOT_WIN`
- `CROSS_PREDECESSOR_SNAPSHOT_CACHE`
- `ABSENT_LOCATOR`
- `AMBIGUOUS_LOCATOR`
- `NON_CANONICAL_LOCATOR`
- `INVALID_UTF8_CONTENT`
- `UNREADABLE_OR_NON_FILE_PATH`
- `HASH_MISMATCH_NO_LOCATOR_CASCADE`
- `VALID_ACCEPTED_REVIEW_CONTROL`
- `VALID_EXECUTABLE_PROOF_CONTROL`
- `VALID_PREDECESSOR_CONTROL`

For changing-resolver cases record exact call count and returned snapshot order.
The second-snapshot case must place a required locator only in the second
payload; correct caching yields one call and rejection, never split-view pass.

Allowed verdicts:

- `EFFECTIVE_CLOSE_FOUNDATION_LOOP`
- `EFFECTIVE_WITH_ONE_NAMED_RESIDUAL`
- `INEFFECTIVE_REOPEN_FOUNDATION`

Any required negative acceptance, positive-control contract rejection, call
count above one for a shared path in one validation tree, or missing exact E2
replay forces the ineffective verdict. Passing committed tests alone is
insufficient. Every verdict retains `successorTrancheOpened: NO`.

## Evidence Requirements

- Exact expected/observed code and validity ledger for every case.
- Resolver call count and snapshot-order ledger for all shared-path cases.
- Exact E2 evidence path and recomputed digest.
- Fresh harness command or reproducible inline script description.
- Focused suite/direct checker results, execution base, final HEAD, exact diff,
  status, and no-commit evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Standard requires exact-unique locator and cached path snapshot | contract | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | invariant 13; Resolution Evidence | `resolutionEvidence` | SCEC standard | ACCEPT |
| Validator owns one cache per validation tree | executable source | `governance/compat/check_semantic_convergence_control.py` | `validate_block` | `_evidence_snapshot_cache` | SCEC checker | ACCEPT |
| Binding validator reuses cached content | executable source | `governance/compat/check_semantic_convergence_control.py` | `_validate_resolution_evidence` | `evidence_snapshot_cache` | SCEC checker | ACCEPT |
| Repository resolver returns safe file bytes | executable source | `governance/compat/check_semantic_convergence_control.py` | repository resolver | `_repo_evidence_bytes_resolver` | SCEC checker | ACCEPT |
| Reviewer correction added exact replay and cache | accepted review | `docs/reviews/CVF_SCEC_T1_R3_LOCATOR_TO_CONTENT_EVIDENCE_BINDING_HARDENING_WORKER_RETURN_2026-08-31.md` | Independent Reviewer Correction | accepted T1-R3 evidence | SCEC review | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: `docs/reviews/CVF_SCEC_T1_R3_LOCATOR_TO_CONTENT_EVIDENCE_BINDING_HARDENING_WORKER_RETURN_2026-08-31.md`
priorVerificationAnchor: `008ff0685fabe169b326a6683fc5ca9bbbb07afb`
freshRecomputeRequired: every E3 case, evidence hashes, resolver calls, focused/direct gates and status
unicodePathHandling: normalized repository-relative paths and strict UTF-8 content; no replacement decoding
extractedTextAuthority: direct source and fresh observed checker output control; prior review controls accepted history only

## Negative Search And Collision Discipline

- Search roots: repository root covering source, tests, docs, JSON and external
  evidence.
- Search command: `rg -n "SCEC_E3|CHANGING_SHARED_PATH|CROSS_PREDECESSOR_SNAPSHOT" governance docs`.
- Structured query: exact existence checks for both authorized output paths.
- Same-token collision result: generic snapshot words have contextual
  occurrences, but no competing E3 output or machine owner was found.
- Disposition: `ABSENT_E3_OUTPUTS_CONFIRMED`; context is non-authoritative for
  the new evaluation.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy/external corpus absorption.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | governed dispatch to uncommitted return to independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired SCEC-E3 packet |
| Disposition | PACKET_READY; no external knowledge absorption |
| Claim boundary | worker output is non-authoritative until independent review. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring dispatch SCEC effectiveness validation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring dispatch SCEC effectiveness validation" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defects: `NONE_RETURNED`
- Required read: `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md`
- Disposition: `APPLIED_READ_ONLY`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Commit mode: WORKER_MUST_NOT_COMMIT`; prompt labels; Source Verification columns; SCEC fields; review-control fields; trace labels; `successorTrancheOpened: NO` |
| gateRunPurpose | Confirm source-derived packet structure after authoring. |
| claimBoundary | Shape/read-ahead only; effectiveness remains unproven. |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SCEC-E3 --title "Locator Snapshot Effectiveness Validation" --date 2026-08-31 --base 8db4e9f87 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --scec-problem-key scec-locator-snapshot-effectiveness-validation --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | generic external no-commit validation profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Exact T1-R3 sources, thirteen-case matrix, terminal verdicts and two-path boundary replace placeholders. |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | case IDs, snapshot/call ledger and verdict |
| claimBoundary | Dispatch provenance only. |

## Core Guard Self-Protection Authorization

Authorized protected-path changes: NONE.

Protected guard paths: N/A with reason: checker, test, fixture, hook, catalog,
standard, ADIF and session paths are read-only.

Rollback boundary: remove only the two uncommitted outputs; do not rewrite T1-R3.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator to dispatcher to external worker to reviewer/closer |
| phase | external validation pending reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=`8db4e9f87e4f4d63f0844e368dd4d80cf6fed3ba`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly two Markdown outputs |
| traceScope(phase, actor) | worker records cases, calls, hashes, commands, status and no-commit evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no unrelated edit or staging |
| nextMoveSurfaces | continuity only after accepted material commit |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_COMPLETION_2026-08-31.md`

reviewerOwnedClosurePaths: the two worker outputs, with the conventional
completion review optional when an Independent Reviewer Correction section in
the worker return is sufficient; continuity surfaces remain a separate commit.

Reviewer recomputes the work-order hash, independently implements the changing-
resolver and cross-predecessor probes, checks exact E2 evidence, audits verdict
mechanics, then runs reviewer-fast and commit steward. A correction may touch
only the two outputs; a checker defect reopens foundation instead of being
silently repaired in E3.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections include Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Decision / Disposition,
External Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus
Completeness And Report Integrity, Finding-To-Governance Learning Disposition,
Epistemic Process Block, Checker Source Read-Ahead Block, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, Public Export Disposition,
Changed Files, git status --short, Worker Experience Retrospective, and
No-Commit Statement.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: every negative fails, every valid control passes,
and one path is resolved once across a validation tree even under a changing
resolver.

Evidence Comparison Requirement: compare every expected validity, code, call
count and snapshot order with fresh observed output.

Contradiction Handling Requirement: record `Contradiction Or Gap Disposition`;
never omit or relabel a mismatch.

Claim Update Requirement: select one exact allowed verdict and state whether
the T1-R3 claim is confirmed, narrowed or invalidated.

## System Loop Interlock Routing

The loop stops at the worker return for independent review. No hardening or
product successor may be dispatched by the worker. `successorTrancheOpened:
NO` throughout.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: validation produces two Markdown records and no
storage/runtime/generated aggregate.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/orchestrator |
| Provider or surface | local provenance workspace |
| Session or invocation | SCEC-E3 dispatch authoring, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, local gates, git |
| Target paths | paired SCEC-E3 baseline and work order |
| Allowed scope source | operator instruction to validate the hardened CVF foundation before continuing |
| Before status evidence | worktree clean at HEAD `8db4e9f87e4f4d63f0844e368dd4d80cf6fed3ba`; targets absent |
| After status evidence | paired packet only pending validation |
| Diff evidence | exact two-path dispatcher manifest |
| Approval boundary | validation dispatch only; no implementation/product authority |
| Claim boundary | effectiveness pending; no runtime/provider claim |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `scec-e3-dispatch-2026-08-31` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local adversarial validation of declared-evidence behavior |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or interception claim |
| receiptEvidence | N/A with reason: no provider/product receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two records plus reproducible local outputs |
| invocationBoundary | one external worker invocation then independent review |
| interceptionBoundary | no IDE, shell, filesystem, provider or agent-thought interception claim |
| claimLanguage | validates addressability, hashes, snapshots, schema and codes only |
| forbiddenExpansion | source/checker edit, semantic truth, product/runtime, provider/live, public/deploy/production |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m unittest governance.compat.test_check_semantic_convergence_control
python governance/compat/check_semantic_convergence_control.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

Record the exact fresh harness command separately. Do not run a live release
bundle or any provider-backed test.

## Acceptance Criteria

- [ ] Exactly two authorized uncommitted paths.
- [ ] Ten questions and all thirteen case IDs covered.
- [ ] Exact E2 path and hash replayed.
- [ ] Shared path call count is exactly one across each validation tree.
- [ ] Changing second snapshot cannot create a pass.
- [ ] Predecessor revalidation shares the cache.
- [ ] All negatives and positives match expected results.
- [ ] One exact verdict selected mechanically.
- [ ] Ordinal-1 successor SCEC block uses exact work-order digest.
- [ ] `successorTrancheOpened: NO`; no commit/provider/forbidden edit.

## Review Gate

Gates are necessary, not sufficient. Reviewer independently reruns exact E2,
changing-resolver, shared-path, predecessor and positive probes before verdict
acceptance.

## Operator Checkpoint

No checkpoint inside the exact two-path validation. Stop only if a real defect
requires forbidden source change or expanded external/product authority.

## Closure Checklist

- exact manifest and no-commit evidence;
- fresh case independence and complete ledger;
- focused/direct/fast gates and diff hygiene;
- independent reviewer probes;
- separate material and continuity commits;
- product/runtime remains parked until foundation-loop verdict.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when complete. Return `BLOCKED_WITH_REASON`
only for a source contradiction, forbidden-scope necessity, or missing
authority. Do not open another tranche.

## Worker Autonomy / No-Question Rule

Worker chooses its ephemeral harness and reasoning method within the evidence,
authority, budget, output and effect boundaries. Do not expose chain-of-thought.

## Claim Boundary

This work order authorizes only SCEC-E3 validation documents. It authorizes no
SCEC source/checker/test edit, GC010/product work, provider/network, public
sync, deployment, production, or automatic successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation-effectiveness validation.
