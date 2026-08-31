# CVF Agent Work Order SCEC-T1-R3 - Locator-To-Content Evidence Binding Hardening

Memory class: governed-work-order

- Status: `READY_FOR_DISPATCH`
- Date: `2026-08-31`
- Task ID: `SCEC-T1-R3`
- Problem key: `scec-locator-content-binding`
- GC-018 baseline: `docs/baselines/CVF_GC018_SCEC_T1_R3_LOCATOR_TO_CONTENT_EVIDENCE_BINDING_HARDENING_2026-08-31.md`
- dispatchBaseHead: `4a8719deda9f31a2c389760f2de0bddf43cdeb30`
- executionBaseHead: worker captures the full committed dispatch HEAD at start
- closureBaseHead: reviewer captures after the uncommitted return is accepted
- Commit mode: WORKER_MUST_NOT_COMMIT
- successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

| Field | Value |
|---|---|
| Mission | Implement one integrated SCEC root-contract hardening that binds each locator to the exact content bytes already bound by SHA-256. |
| Exact outputs | Four named foundation implementation/reference paths plus one named worker return. |
| Forbidden expansion | GC010; T1J-R4; T1K/T2; product/runtime; provider/live; public sync; deployment; production; unrelated cleanup. |
| Return condition | `COMPLETE_PENDING_REVIEW` with every exact gate rerun after the final edit; no commit. |
| Operator handoff | Operator may copy this committed work order to one worker; the orchestrator/reviewer independently reviews returned uncommitted files. |

## Purpose

Close the locator-content defect exposed by SCEC-E2 as one implementation
batch. Do not create another decision-only tranche and do not resume GC010.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "scec-locator-content-binding",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["SCEC_LOCATOR_NOT_BOUND_TO_EVIDENCE_CONTENT"],
    "reopened": [],
    "current": ["SCEC_LOCATOR_NOT_BOUND_TO_EVIDENCE_CONTENT"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "SCEC-T1-R3-DISPATCH-GAP",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/reviews/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md"
  }],
  "requiredDisposition": "ROOT_CONTRACT_REQUIRED",
  "successorScope": "INTEGRATED_ROOT_CONTRACT"
}
```

## Review Dispatch Convergence And Invocation Budget Control

dispatchKind: INITIAL
reviewRoundCount: 0
rootCauseClusterId: `SCEC-T1-R3-LOCATOR-CONTENT-BINDING`
priorFindingSetDigest: `INITIAL_CONSOLIDATED_FROM_REVIEWER_CORRECTED_SCEC_E2`
successorTrancheOpened: NO
implementationAutonomyDisposition: `CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY`
internalAgentInvocationCount: 0
externalAgentInvocationCount: 0
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 2
newIndependentCriticalEvidence: YES - E2 accepted a non-empty locator absent from the correctly hash-bound evidence file.
terminalReadinessVerdict: READY_FOR_DISPATCH

The worker receives one consolidated root contract. If review finds a defect,
the reviewer must return one consolidated finding digest rather than opening a
new narrow design tranche.

## Scope / Target / Owner Boundary

Allowed paths:

1. `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`
2. `governance/compat/check_semantic_convergence_control.py`
3. `governance/compat/test_check_semantic_convergence_control.py`
4. `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md`
5. `docs/reviews/CVF_SCEC_T1_R3_LOCATOR_TO_CONTENT_EVIDENCE_BINDING_HARDENING_WORKER_RETURN_2026-08-31.md`

No other path may change. The worker may compact the two governed Python files
inside their authorized paths when needed to remain under the file-size guard,
provided focused behavior stays covered. No hook/catalog/scaffold change is
needed because the `resolutionEvidence` field shape does not change.

## Authority Chain

The operator authorized iterative CVF foundation learning. Reviewer-corrected
SCEC-E2 provides the defect evidence; the paired baseline defines the root
contract. This work order delegates implementation only. Reviewer/closer owns
acceptance and commits.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | Transfers the committed packet and retains expansion checkpoints. |
| Dispatcher/orchestrator | Owns authority, exact scope, and consolidated semantics. |
| Worker | Implements and verifies only the five authorized paths; does not commit. |
| Reviewer/closer | Replays the bypass independently, reviews semantics, and commits accepted material. |

## Required First Reads

| Path | Action | Reason |
|---|---|---|
| `docs/reference/guard_orientation/README.md` | FULL_READ | role and guard routing |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal-format traps |
| paired baseline and this work order | FULL_READ | controlling authority |
| `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | FULL_READ | canonical SCEC semantics |
| `governance/compat/check_semantic_convergence_control.py` | FULL_READ | checker and resolver behavior |
| `governance/compat/test_check_semantic_convergence_control.py` | FULL_READ | focused regression surface |
| accepted SCEC-E2 assessment and worker return | FULL_READ | exact defect and probe evidence |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md` | FULL_READ | reusable learning owner |

## Pre-Flight Checks

Record `git rev-parse HEAD`, `git status --short --untracked-files=all`, exact
baseline/work-order hashes, and run:

`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4a8719deda9f31a2c389760f2de0bddf43cdeb30 --head HEAD`

Stop if HEAD differs from the committed dispatch head supplied by the operator
or unexpected files are present.

## Task Governance Routing Manifest

| Field | Value |
|---|---|
| taskClass | protected governance checker hardening |
| riskCeiling | HIGH_LOCAL_GOVERNANCE |
| mutationScope | exact five-path manifest |
| runtimeOrExternalEffect | NONE |
| liveProviderAuthority | FORBIDDEN |
| commitAuthority | reviewer/closer only |
| route | GC-018 integrated root-contract implementation with independent review |

## Intake Role Routing Decision

| Input | Role | Disposition |
|---|---|---|
| Reviewer-corrected SCEC-E2 | CVF-governed defect evidence | `USE_AS_ACCEPTED_EVIDENCE` |
| Worker implementation choice | bounded implementation proposal | `REVIEW_REQUIRED` |
| Provider-local memory | non-authoritative execution aid | `NOT_CVF_SOURCE` |

## Work-Order Fulfillment Manifest

| Deliverable | Required outcome |
|---|---|
| Standard | deterministic same-byte hash and locator-content contract, stable failures, semantic boundary |
| Checker | fail-closed snapshot/hash/strict-UTF-8/exact-unique-locator enforcement |
| Tests | exact E2 replay, adversarial negatives, positive compatibility, predecessor revalidation |
| ADIF | record the fourth SCEC instance and prevention pattern |
| Worker return | full no-commit packet with pre/post evidence and exact gates |

## Write Ownership

Worker owns only the five paths named above. Dispatch artifacts, accepted E2
artifacts, historical reviews, session state, handoff, hook catalogs,
scaffolds, product/runtime sources, and every other path are forbidden edits.

## Execution Plan

1. Reproduce the exact E2 absent-locator acceptance before implementation.
2. Add a single-snapshot evidence-content resolver contract without weakening
   path, hash, predecessor, or claim-link validation.
3. Enforce strict UTF-8 and canonical exact-unique locator resolution with
   stable violation codes.
4. Add focused positive/negative tests, including exact E2 replay and accepted
   R2 locator compatibility.
5. Update the standard and ADIF-0055 to match implemented behavior exactly.
6. Keep governed Python files within size limits, run every final gate, and
   return the five-path uncommitted packet.

## Implementation Requirements

- Repository enforcement reads a safe evidence file once as bytes. SHA-256 and
  locator lookup use the same returned bytes, preventing split-view validation.
- Strict UTF-8 decoding is mandatory for locator-bearing evidence. Do not use
  replacement decoding or silently skip content validation.
- `locator` must be a non-empty string equal to `locator.strip()` and its exact
  Unicode code-point sequence must occur exactly once in decoded content.
- Emit stable codes at least for non-canonical locator, content decode failure,
  locator not found, and locator ambiguous. Preserve existing empty-locator,
  unsafe/unreadable path, malformed/hash-mismatch, coverage, and claim-link
  codes.
- Hash mismatch and unreadable/non-file evidence remain independently visible;
  avoid cascading locator diagnostics when no trustworthy content snapshot is
  available.
- Predecessor revalidation uses the same hardened resolution logic so a stale,
  missing, or now-unresolvable predecessor locator cannot inherit trust.
- Preserve the callable API compatibility needed by existing unit callers, or
  migrate every caller inside the authorized checker/test paths. The actual CLI
  enforcement path must never degrade to hash-only validation.
- Do not modify the SCEC JSON field shape, worker-return scaffolds, hook
  catalogs, GC010 artifacts, or product/runtime code.
- The standard must state explicitly that unique textual occurrence is an
  addressability check, not proof of relevance, correctness, or semantic truth.

## Mandatory Regression Matrix

| Case | Required observation |
|---|---|
| Exact E2 absent locator | `RESOLUTION_EVIDENCE_LOCATOR_NOT_FOUND` |
| Locator appears once | valid when every other binding field is valid |
| Locator appears twice | `RESOLUTION_EVIDENCE_LOCATOR_AMBIGUOUS` |
| Leading/trailing whitespace | non-canonical-locator violation |
| Invalid UTF-8 bytes | content-decode violation |
| Directory or missing path | existing unreadable-path violation; no false pass |
| Correct path with wrong hash | existing hash-mismatch violation |
| R2 symbol locators | both resolve exactly once in the current hash-bound test file |
| Successor consumes invalid predecessor locator | `PREDECESSOR_BLOCK_INVALID` carrying the locator violation |
| Mixed markdown fences | existing parser regression remains passing |

## Evidence Requirements

The worker return must record the pre-fix exact E2 reproducer and its unexpected
acceptance, post-fix stable violation, positive controls, full observed-code
matrix, focused test counts, direct checker result, file-size gate, ADIF result,
worker-return fast gate, diff hygiene, HEAD, status, and no-commit evidence.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Locator is checked only for non-emptiness | `governance/compat/check_semantic_convergence_control.py` | `_validate_resolution_evidence` | locator branch | SCEC checker | `ACCEPT` |
| Current resolver returns only a digest | `governance/compat/check_semantic_convergence_control.py` | repository resolver and CLI validation | `_repo_predecessor_hash_resolver` | SCEC checker | `ACCEPT` |
| Absent non-empty locator currently passes | `docs/assessments/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_2026-08-31.md` | questions 7/10 and case matrix | exact reviewer probe | accepted E2 evidence | `ACCEPT` |
| Accepted verdict reopens foundation only | `docs/reviews/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md` | Independent Reviewer Correction; Decision / Disposition | `INEFFECTIVE_REOPEN_FOUNDATION` | accepted E2 review | `ACCEPT` |
| Existing R2 locators are named test symbols | `docs/reviews/CVF_SCEC_T1_R2_BLOCKER_RESOLUTION_EVIDENCE_BINDING_AND_HISTORICAL_REPLAY_CORRECTION_WORKER_RETURN_2026-08-31.md` | active SCEC block | two executable evidence bindings | accepted compatibility evidence | `ACCEPT_AS_REGRESSION_EVIDENCE` |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: `docs/reviews/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md`
priorVerificationAnchor: `ff95b77d63fe332cb04dbabe61ecd85b88ea7232`
freshRecomputeRequired: exact bypass replay, checker/tests, hashes, size, status and gates after implementation
unicodePathHandling: use normalized repository-relative paths; evidence content uses strict UTF-8 with no replacement decoding
extractedTextAuthority: direct hash-bound bytes control locator occurrence; reviewer-accepted artifacts control defect history

## Negative Search And Collision Discipline

Before dispatch authoring, exact path checks confirmed that the paired
SCEC-T1-R3 baseline, this work order, and the named worker-return output did
not already exist at the clean execution base. Source search also confirmed
that the planned locator-content violation codes and byte-snapshot resolver
owner were not already implemented under another symbol. The worker must
repeat exact-path collision checks and symbol searches from the committed
dispatch HEAD before writing; a collision or pre-existing equivalent owner is
returned to the orchestrator rather than duplicated.

- Search roots: repository root, with explicit coverage of governance source,
  tests, docs, JSON fixtures, and external-evidence references.
- Search command: `rg -n "RESOLUTION_EVIDENCE_LOCATOR_NOT_FOUND|RESOLUTION_EVIDENCE_LOCATOR_AMBIGUOUS|evidence_bytes_resolver" governance docs`.
- Structured query: exact output-path existence checks for the paired baseline,
  work order, and named worker return at the execution base.
- Same-token collision result: occurrences of generic locator wording belong
  to the existing SCEC contract; no competing machine owner or equivalent
  implemented code was found for the three searched symbols.
- Disposition: `ABSENT_IMPLEMENTATION_CONFIRMED`; prose occurrences are
  non-authoritative context and do not bind or replace the missing machine
  enforcement owner.

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`: no legacy or external corpus is absorbed.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | `NOT_APPLICABLE_WITH_REASON`: this is a CVF-owned local implementation packet, not external knowledge intake. |
| Matching local-view guard | `governance/compat/check_semantic_convergence_control.py` |
| Owner surface | SCEC standard and checker |
| Disposition | `NOT_APPLICABLE_WITH_REASON`: no external knowledge item is absorbed. |
| Claim boundary | worker output is pending implementation evidence and never canonical authority without independent review. |

## ADIF Defect Registry Disclosure

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Worker execution" --role worker --lifecycle-phase implementation --json`
- Resolver query: taskClass=`Worker execution`, role=`worker`, lifecyclePhase=`implementation`
- Applied entries: worker records the resolver's complete returned set before editing.
- Required update: `ADIF-0055` records the E2 locator-content bypass as another observed instance and promotes same-byte deterministic locator resolution as the prevention pattern.
- Disposition: `APPLY_AND_UPDATE_EXISTING`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_adif_entry_integrity.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `READY_FOR_DISPATCH`; `WORKER_MUST_NOT_COMMIT`; `Semantic Convergence Outcome`; `Core Guard Self-Protection Authorization`; `Risk / Corrective Action`; `Decision / Disposition`; worker-return markers and trace labels |
| gateRunPurpose | Confirm source-derived structure after read-ahead; not discover requirements by failure. |
| claimBoundary | Read-ahead covers artifact shape only, not implementation correctness. |

## Scaffold Provenance Block

- scaffoldHelperCommand: `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id SCEC-T1-R3 --title "Locator-To-Content Evidence Binding Hardening" --date 2026-08-31 --base 4a8719deda9f31a2c389760f2de0bddf43cdeb30 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --include-worker-return-skeleton --stdout`
- generatedProfile: `protected-governance-path`
- generatedSkeletonStatus: `PATTERN_REUSED_FROM_ACCEPTED_SCEC_T1_R2_PACKET`
- manualEditsAfterScaffold: `YES - exact integrated locator-content contract replaces generic placeholders`
- checkerReadAheadConfirmation: `COMPLETE`
- docOnlyNewFields: `none beyond pending contract descriptions`
- claimBoundary: `dispatch only`

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement only SCEC evidence snapshot,
hash, strict-UTF-8, and exact-unique locator binding; focused regressions;
standard alignment; ADIF learning; and the named worker return. No hook,
scaffold, unrelated checker, or product semantics may change.

Protected paths:

- `governance/compat/check_semantic_convergence_control.py`
- `governance/compat/test_check_semantic_convergence_control.py`

Operator authorization: operator explicitly requested improving the CVF
foundation, testing it through successor tranches, and hardening it again when
the test exposed a real gap.

Rollback boundary: revert only SCEC-T1-R3 material if rejected; do not revert
accepted SCEC-T1/T1-R1/T1-R2/E1/E2 commits or rewrite historical evidence.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | one implementation worker; independent orchestrator/reviewer/closer |
| phase | committed dispatch to uncommitted worker return |
| baseHeadFor(phase) | dispatchBaseHead=`4a8719deda9f31a2c389760f2de0bddf43cdeb30`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact five-path fulfillment manifest |
| traceScope(phase, actor) | worker records reproduction, implementation, tests, gates, status, and no-commit evidence; reviewer independently replays bypasses |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no unrelated edit, staging, commit, provider-local file, or generated continuity mutation |
| nextMoveSurfaces | continuity changes only after accepted material commit |

## Reviewer Closure Conversion

Reviewer first replays absent, ambiguous, invalid-UTF-8, and split-view risks
without trusting the worker matrix. Reviewer verifies the actual CLI uses one
byte snapshot, checks existing R2 locators, runs reviewer-fast and commit
steward preflight, then makes at most one material commit plus one separate
continuity commit. Gate success alone is not acceptance.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real section names include Purpose, Target / Source, Scope /
Methodology, Findings / Position, Risk / Corrective Action, Decision /
Disposition, External Knowledge Intake Routing, Epistemic Process Block,
Checker Source Read-Ahead Block, Agent Operation Trace Block, Delta Execution
Claim Boundary Control Block, Public Export Disposition, Changed Files, git
status --short, and No-Commit Statement.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: same-snapshot hash and exact-unique textual
resolution reject the exact E2 bypass without weakening valid bindings or
claiming semantic truth.

Evidence Comparison Requirement: compare pre-fix and post-fix exact E2 replay,
then compare every mandatory negative and positive control to its predicted
stable code or valid result.

Contradiction Handling Requirement: record `Contradiction Or Gap Disposition`;
do not omit, relabel, or explain away a contradicting case.

Claim Update Requirement: classify the prediction as confirmed, revised,
narrowed, or invalidated.

## System Loop Interlock Routing

This changes a governance checker already present in the local gate chain. It
creates no watcher, daemon, queue, provider call, or product runtime owner.
GC010 progression remains parked through independent closure.

## Foundation Storage Layout Block

The standard stays in its semantic-convergence reference folder; checker and
focused tests stay in governance compatibility; learning stays in ADIF-0055;
the worker return stays under reviews. No new storage surface is introduced.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/orchestrator |
| Provider or surface | local provenance workspace |
| Session or invocation | SCEC-T1-R3 dispatch authoring, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | governed source reads, rg, apply_patch, and local gates |
| Target paths | paired SCEC-T1-R3 baseline and work order |
| Allowed scope source | operator instruction to continue CVF foundation learning after E2 exposed a gap |
| Before status evidence | clean HEAD `4a8719deda9f31a2c389760f2de0bddf43cdeb30` |
| After status evidence | two dispatch paths pending pre-dispatch validation |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | dispatch authoring only; worker cannot commit |
| Claim boundary | repository-local trace; no OS identity, provider, or runtime behavior claim |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `scec-t1-r3-dispatch-authoring-2026-08-31` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local SCEC standard/checker/test/learning hardening |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: no product action is executed |
| invocationBoundary | governed local file editing and local tests only |
| interceptionBoundary | no IDE, shell, filesystem, provider, or worker-thought interception claim |
| claimLanguage | checker validates same-file locator addressability and immutable evidence shape only |
| forbiddenExpansion | semantic-truth scoring, GC010/product runtime, provider/live, public sync, deployment, production |

## Verification Commands

```powershell
python -m unittest governance.compat.test_check_semantic_convergence_control
python governance/compat/check_semantic_convergence_control.py --base 4a8719deda9f31a2c389760f2de0bddf43cdeb30 --head HEAD --enforce
python governance/compat/check_adif_entry_integrity.py --enforce
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_semantic_convergence_control.py
git diff --check
git status --short --untracked-files=all
```

If the repository's canonical size-guard command differs, resolve it from
`governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`, run that
canonical command, and record both the resolved command and result.

## Acceptance Criteria

- [ ] Exact five-path manifest and no other change.
- [ ] Exact E2 absent-locator probe fails with the stable not-found code.
- [ ] Hash and locator resolution use one evidence byte snapshot.
- [ ] Canonical, strict-UTF-8, exact-unique locator rules are machine-enforced.
- [ ] All mandatory negative and positive cases match the matrix.
- [ ] Existing predecessor, path/hash, parser, and claim-link controls remain passing.
- [ ] Standard and ADIF-0055 describe implemented behavior without overclaim.
- [ ] All final commands pass after the final edit.
- [ ] Worker return is `COMPLETE_PENDING_REVIEW`; no commit.

Fail conditions: hash-only CLI enforcement, absent or ambiguous locator pass,
replacement decoding, split-view reads, weakened existing control, semantic-
truth claim, unexpected path, failed final gate, product/runtime edit, or
worker commit.

## Review Gate

Implementation begins only from the committed dispatch HEAD and passing
pre-implementation gate. Closure requires independent semantic/source review,
exact adversarial replay, reviewer-fast, committed-range pre-closure, and
reviewer/closer commit.

## Operator Checkpoint

No operator checkpoint is required inside the exact five-path local contract.
Stop only if completion requires another path, schema-shape change, hook or
scaffold mutation, product/runtime authority, provider/live activity, public
sync, deployment, production, destructive action, or risk-ceiling increase.
Ordinary in-scope implementation defects remain worker-owned.

## Closure Checklist

- [ ] Source facts reverified
- [ ] Exact manifest reconciled
- [ ] E2 bypass independently replayed
- [ ] Focused tests and direct checker pass
- [ ] File-size and ADIF checks pass or pre-existing out-of-scope defect is precisely disclosed
- [ ] Worker-return fast gate and diff hygiene pass
- [ ] No commit by worker
- [ ] Reviewer separately commits material and continuity

## Return-To-Orchestrator Conditions

Return without continuing for a forbidden-path need, incompatible schema-shape
need, unresolvable same-snapshot constraint, unexpected dirty worktree, or a
failed gate outside allowed scope. Do not open a successor tranche.

## Worker Autonomy / No-Question Rule

Within this exact root contract, the worker chooses implementation structure,
repairs allowed-scope failures, compacts authorized Python files when needed,
and reruns gates autonomously. This grants no scope or claim expansion.

## Claim Boundary

This work order authorizes one local SCEC foundation hardening batch. It does
not authorize GC010, T1J-R4, T1K/T2, product/runtime work, semantic-truth
scoring, provider/live use, public sync, deployment, production, or commit by
the worker.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: private provenance implementation dispatch only.
