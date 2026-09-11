# CVF Agent Work Order - Committed Evidence Fingerprint Contract
Memory class: governed-worker-dispatch
docType: work_order
Status: DISPATCH_READY
Date: 2026-09-11
Batch ID: MFRP-FINGERPRINT-T1
dispatchBaseHead: a6823f497
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: NOT_EXECUTED_YET
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchSurface: INTERNAL_AGENT
providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: internal implementation worker.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md
Paired authority: docs/baselines/CVF_GC018_MFRP_FINGERPRINT_T1_2026-09-11.md
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: WORKER_MUST_CAPTURE_AT_START.
Current-time notes: 2026-09-11, source-verified at a6823f497.
Do-not-misread notes: fingerprint contract only; no pilot, no main-workspace commit, no historical receipt rewriting.
Required first actions: read startup front doors, active handoff, this packet, paired baseline, guard orientation/gotchas and source/checker owners; capture HEAD/status and pass pre-implementation.
Return contract: exact eleven-path delta, actual tests/gates, COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON; staging empty.

## Purpose

Repair the worktree/Git-object identity mismatch while preserving raw cache freshness and receipt integrity.

## Required First Reads

CVF_SESSION_MEMORY.md; bootstrap; active handoff; paired GC-018; this work order; guard orientation and literal gotchas; all Source Verification owners and listed checkers. Read existing receipt/readout/replay consumer tests before editing. Provider-specific memories are not authority.

## Write Ownership

Exactly eleven Required Artifact Manifest paths. Worker may create the named helper/test/contract/return only. Dispatcher packet and continuity remain frozen during the worker lane.

## Closure Checklist

- [ ] raw/Git mismatch reproduced in isolated fixture
- [ ] optional binding and canonical producer/validator/collector agree
- [ ] legacy, hostile and consumer tests pass
- [ ] full worker-return fast gate passes
- [ ] exact eleven-path delta, empty staging, no commit
- [ ] independent Local reviewer acceptance and completion companion

## Return-To-Orchestrator Conditions

COMPLETE_PENDING_REVIEW on complete evidence; BLOCKED_WITH_REASON only for source contradiction, forbidden-path need or missing authority. Do not clear a production safety marker to pass a gate.

## Current Runtime Freshness Verification

Read-only inspection at a6823f497 confirms _worktree_fingerprint reads disk bytes, _reconstruct_fingerprint_from_commit reads Git blobs, and the canonical validator binds changedPathPlanDigest to worktreeFingerprint. These observations concern deterministic metadata only. The proposed committedEvidence field is a new dispatch contract, not existing behavior.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy absorption payload is processed; old receipt compatibility is not a corpus absorption claim.


## Mission

Repair the recurring worktree/Git-blob fingerprint contradiction without weakening cache freshness, receipt integrity or collector safety.

## Authority Chain

Operator explicitly approved this separate guard-maintenance work order on 2026-09-11. AGENTS.md -> paired GC-018 -> this bounded work order -> existing P2/P4 owners. Standalone defect repair, no roadmap advancement.

## Verified Defect And Rejected Measurement

Attempt ATTEMPT-a4ec8bfaa9c112ca compared trusted material 3de0ba07ce213ce2e6fb5668b5d41f6fb663fab1 with disclosure a6823f497a2746ca496dbc196483baff14689850.
Read-only recomputation over the nine material paths produced:
- worktree bytes SHA-256: f3d5a50582a5bc594a79a66676a2e0b13e2520777a3c337c96dd1af1df197f54
- Git blob bytes SHA-256: 57ba3abdca179495fd537421a880e810b28a0ff95430e25dc76958259807fc26
- six raw differences; all nine match after CRLF-to-LF conversion; core.autocrlf=true.

This establishes representation mismatch for this named range only. Normalizing text is diagnostic, not the authorized hashing repair. The reviewer rejected the measurement, preserved the pending journal, and recoverably archived the marker as .cvf/runtime/mfrp-p4-shadow-canary/ADJUDICATED_REJECTED_OBSERVATION_2026-09-11_TPGR.json with SHA-256 56d22b53dc9587d4916c0b9a235b339d432ad80f9315b4250d5a02f7d3d8db98. No sample was promoted. Ignored runtime evidence is supporting diagnostic input only; current source and this operator-authorized packet control. This dispatch neither claims a permanent fix nor permits automatic marker deletion.


## Required Fingerprint Contract

1. Preserve worktreeFingerprint and changedPathPlanDigest as raw worktree/cache identities. A byte change, including line endings, must still invalidate exact cache reuse. Do not normalize these identities or reinterpret v3 historical receipts.
2. Add a separate optional committedEvidence object under an explicit profile cvf.committedEvidenceFingerprint.v1. Closed fields: profile, baseSha, headSha, fingerprint. SHAs are resolved full 40-character commit IDs; fingerprint is lowercase SHA-256. Bind this complete object into machineVerification and receiptDigest, with strict top-level/nested equality. Missing object retains the old v3 builder/validator behavior; malformed, extra-key, unknown-profile, one-sided or tampered objects reject. No new receipt schema or machineVerification profile version is authorized.
3. Canonical helper owns the Git-blob recipe for both producer and collector. Use an explicitly versioned deterministic path-set policy: git diff --no-renames --name-only base..head with NUL-delimited output (old/new paths for renames, normal Git deletion semantics), sorted ordinal repo-relative slash paths, UTF-8 path bytes, NUL, SHA-256 digest of raw head blob bytes or the existing missing sentinel for an actual deletion, NUL. No text decoding, newline replacement, clean/smudge filter execution, or checkout mutation. Robust filename enumeration must preserve spaces and non-ASCII paths. Git errors, missing objects and unsupported entry kinds are explicit failure, never a fake deletion. Reject invalid/traversing paths, ambiguous refs and unresolved ancestry. Document symlink and gitlink policy; unsupported entries must be skipped/rejected explicitly, never followed into the filesystem.
4. Produce committed evidence only for a successful committed-range pre-closure on clean worktree with resolvable immutable range and current evidence paths matching the trusted target. No binding for uncommitted/dirty/failed/partial gates. A later continuity-only HEAD must be supportable; later semantic changes to target paths must not be certified as execution against the historical target. Preserve existing verifier identity, input-drift checks, full-gate/finality and receipt cache semantics. Git-object identity alone is NOT proof of what gate commands executed.
5. P4 validates through the canonical P2 owner, validates the profile and exact expected parent/trusted range, then recomputes the committed evidence fingerprint through the shared helper. It must never compare committed bytes with worktreeFingerprint. Legacy v3 receipts without committedEvidence remain valid under old P2 rules but are explicitly ineligible for new P4 committed-evidence collection, not upgraded or silently rehashed. An explicitly supplied malformed/tampered binding remains fail-closed, not treated as a benign legacy omission. Preserve existing safety-marker behavior for genuinely unsafe observations.
6. Readout and replay consumers keep their current raw changedPathPlanDigest meaning; receiptDigest covers the additive binding. Verify compatibility against existing tests without editing unrelated consumers. If proof requires a consumer outside this manifest to change, return the exact source-backed dependency to Local reviewer before modifying it.
7. No production journal mutation, historical sample promotion, marker removal, full post-commit collector invocation or commits in the main workspace by the worker. Hermetic temporary Git commits are allowed solely as test fixtures; isolate Git configuration/hooks and keep provider/network disabled. Local reviewer owns actual commit/continuity collection and any safety adjudication.

## Test And Acceptance Matrix

| Case | Required proof |
|---|---|
| Reproduced CRLF checkout vs LF blobs; core.autocrlf true/false | real temporary Git repository, real producer -> canonical validator -> collector reconciliation; same committed binding, distinct raw cache hashes |
| Binary bytes, mixed line endings, Unicode/spaces paths | exact raw blob hash; no lossy normalization or filename splitting |
| Added, modified, deleted, renamed paths | producer/collector path and missing-entry agreement using explicit non-rename-aware enumeration |
| Dirty tracked, staged, untracked or mid-run drift | no new committed proof, no stale cache acceptance |
| Later continuity commit vs later material edit to target | continuity case admitted; changed evidence not misrepresented as historical execution |
| Wrong base/head, unknown profile, extra/missing fields, bad digest, nested/top mismatch | deterministic fail-closed rejection; no legacy fallback |
| Missing commit/blob, failed Git command, symlink/gitlink unsupported case | explicit failure/ineligible result, never missing-file sentinel for an error |
| Historical v3 without object | exact prior validator/builder behavior; P4 explicitly ineligible; historical artifacts untouched |
| Existing AAF/readout/replay and raw-cache tests | no changed meaning; real canonical validator used, not copied digest implementation |
| Tests vs live measurement | hermetic end-to-end proof is not sample promotion or provider/runtime proof |

Use independently constructed Git expected values, not helper compared with itself. Compare complete old receipt output for representative legacy fixtures. Tests must exercise actual producer/canonical validator/collector integration, not just isolated dict helpers.

## Execution Plan

1. Capture clean HEAD/status and dispatch ancestry; read current authority and checker owners, run pre-implementation.
2. Reproduce the mismatch in a disposable Git fixture and record the raw/cache versus committed distinction.
3. Implement shared helper, additive binding, strict validation and collector consumption; update reference and focused tests.
4. Run existing plus new focused tests and required worker-return fast gate; repair in-scope failures together.
5. Return eleven-path uncommitted delta with COMPLETE_PENDING_REVIEW or source-backed BLOCKED_WITH_REASON; leave staging empty.

## Required Artifact Manifest

| Path | Required worker action |
|---|---|
| governance/compat/run_agent_autorun_workflow_gate.py | bounded fingerprint implementation |
| governance/compat/agent_autorun_machine_verification.py | bounded fingerprint implementation |
| governance/compat/mfrp_shadow_canary_autocollect.py | bounded fingerprint implementation |
| governance/compat/committed_evidence_fingerprint.py | bounded fingerprint implementation |
| governance/compat/test_run_agent_autorun_workflow_gate.py | regression tests |
| governance/compat/test_agent_autorun_machine_verification.py | regression tests |
| governance/compat/test_mfrp_shadow_canary_autocollect.py | regression tests |
| governance/compat/test_committed_evidence_fingerprint.py | regression tests |
| docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md | CREATE canonical additive contract |
| docs/reference/review_cost_control/README.md | add family link to the new contract; preserve existing review-cost owner |
| docs/reviews/CVF_MFRP_FINGERPRINT_T1_WORKER_RETURN_2026-09-11.md | CREATE no-commit evidence return |

## Work-Order Fulfillment Manifest

Exactly eleven paths. The new helper and its test are the planned maintainability split; do not grow near-limit producer/collector files through duplicated hashing code. No other split, registry entry, hook wiring, Git config change or generated aggregate mutation. New contract is undated under the existing review-cost folder; no dated-owner active-window mutation is needed.

## Evidence Requirements

Record actual executionBaseHead; source/contract/consumer matrix, independent Git expected hashes, focused command results, full fast gate result, known limitations, exact changed paths and untracked return. Report missing full-gate evidence honestly. No provider proof needed for this pure deterministic metadata repair.

## Acceptance Criteria

All matrix rows pass with executable evidence. Raw cache behavior and legacy receipts preserved; new committed binding is integrity-covered and collector-reconstructible. No silent failure downgrade, historical promotion or scope expansion. Reviewer independently accepts before any main-workspace commit.

## Forbidden Scope And Stop Conditions

No pilot, acquisition/research, network/provider/API, credentials, dependency install, runtime/product implementation, public sync/push/deploy, hook/catalog/registry edit, configuration/line-ending rewrite, main-workspace staging/commit, marker clearing or historical receipt migration. Stop for source contradiction, missing authority or needed path outside manifest. Keep RABA/DARA-T5/P5/P6 parked.

## Review Gate

EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Local reviewer evaluates the contract/schema/path/authority/test/range matrix as one dependency class; use M5/M10/safety/M20 measurement boundaries, not broad repeated execution.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | docs/reviews/CVF_MFRP_FINGERPRINT_T1_COMPLETION_2026-09-11.md - required by check_continuation_chain.py Rule B before closure |
| reviewerOwnedClosurePaths | eleven worker paths, paired baseline/work-order status, required completion companion; separate active continuity |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Verification Commands

Run pre-implementation using actual executionBaseHead. Run:
python -m pytest governance/compat/test_committed_evidence_fingerprint.py governance/compat/test_run_agent_autorun_workflow_gate.py governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_mfrp_shadow_canary_autocollect.py -q
Also run existing readout/replay compatibility tests relevant to unchanged consumers, identified by source references. Then python governance/compat/run_worker_return_fast_gate.py and git diff --check. No full release/provider bundle.


## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Producer fingerprints mutable disk bytes | LOCAL_SOURCE | governance/compat/run_agent_autorun_workflow_gate.py | fingerprint and receipt context | _worktree_fingerprint | P2 receipt producer | ACCEPT |
| Collector independently fingerprints committed blobs | LOCAL_SOURCE | governance/compat/mfrp_shadow_canary_autocollect.py | committed reconstruction | _reconstruct_fingerprint_from_commit | P4 collector | ACCEPT |
| Mismatch creates fail-closed marker | LOCAL_SOURCE | governance/compat/mfrp_shadow_canary_autocollect.py | receipt reconciliation | UNSAFE_FINGERPRINT_MISMATCH | P4 safety | ACCEPT |
| Digest and strict envelope owned centrally | LOCAL_SOURCE | governance/compat/agent_autorun_machine_verification.py | builder and validator | _validate_receipt_integrity | v3 canonical owner | ACCEPT |
| Readout delegates validation and retains raw changed-path identity | LOCAL_SOURCE | governance/compat/agent_automation_machine_verification_readout.py | read and build | read_receipt_readonly | AAF consumer | ACCEPT |
| Producer tests cover raw-byte drift | LOCAL_TEST | governance/compat/test_run_agent_autorun_workflow_gate.py | fingerprint regression | test_worktree_fingerprint_changes_with_file_content | cache tests | ACCEPT |
| Receipt tests preserve legacy rejection | LOCAL_TEST | governance/compat/test_agent_autorun_machine_verification.py | compatibility | test_unknown_schema_fails_closed | validator tests | ACCEPT |


## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_task_governance_route.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_worker_return_quality_gate.py; governance/compat/check_review_cost_control.py |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; WORKER_MUST_NOT_COMMIT; closeabilityContractVersion; Self-declared worker-return artifact; Required Artifact Manifest |
| gateRunPurpose | confirm source-verified bounded dispatch and ownership, not discover implementation semantics |
| claimBoundary | dispatch evidence only; no implemented repair claim |


## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-FINGERPRINT-T1 --title "Committed Evidence Fingerprint Contract" --date 2026-09-11 --base a6823f497 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout |
| generatedProfile | protected-governance-path; internal no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Reused governed role/closeability envelope, added separate immutable identity contract, exact eleven-path manifest and hostile proof matrix |
| checkerReadAheadConfirmation | sources named in Checker Source Read-Ahead Block read for field/enum requirements |
| docOnlyNewFields | committedEvidence proposed additive profile, not current machine behavior |
| claimBoundary | dispatch authoring only |


## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-machine-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: python governance/compat/run_adif_defect_resolver.py --task-class governance-machine-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json
Returned defect count: 0. Returned defects: NONE_RETURNED. Disclosed defectIds: none. Dispatch impact: no matching active resolver item; explicit contract and guard obligations remain.


## Core Guard Self-Protection Authorization

Operator authorization: explicit yes on 2026-09-11 to dispatch internal worker repair of the fingerprint contract and regression tests before any pilot.

Authorized guard-maintenance scope: only the eleven worker targets below; preserve raw cache invalidation, receipt integrity, full gate selection and P4 safety. Worker copies this block into its return. No hook/catalog/registry/config edits.

Protected worker paths:
- governance/compat/run_agent_autorun_workflow_gate.py
- governance/compat/agent_autorun_machine_verification.py
- governance/compat/mfrp_shadow_canary_autocollect.py
- governance/compat/committed_evidence_fingerprint.py
- governance/compat/test_run_agent_autorun_workflow_gate.py
- governance/compat/test_agent_autorun_machine_verification.py
- governance/compat/test_mfrp_shadow_canary_autocollect.py
- governance/compat/test_committed_evidence_fingerprint.py

Rollback boundary: only newly introduced fingerprint binding behavior and associated tests/reference. Never rewrite old receipts or journals, clear safety markers automatically, normalize the checkout, amend history, or restore unrelated work.


## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | P2 producer/validator, P4 collector | deterministic evidence only, no worker commit | source/test matrix | existing internal Python consumers | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no new external consumer | no research or external invocation | operator authorization internal only | adapter absent and not authorized | N/A_WITH_REASON |


## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-FINGERPRINT-T1
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
  "problemKey": "committed-evidence-fingerprint",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [
      "worktree-versus-committed-bytes"
    ],
    "reopened": [],
    "current": [
      "worktree-versus-committed-bytes"
    ]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "legacy-and-additive-fingerprint-contract",
      "claimClass": "SCHEMA_COMPATIBILITY",
      "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
      "evidenceRef": "governance/compat/test_agent_autorun_machine_verification.py"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-FINGERPRINT-T1",
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
    "governance/compat/run_agent_autorun_workflow_gate.py",
    "governance/compat/agent_autorun_machine_verification.py",
    "governance/compat/mfrp_shadow_canary_autocollect.py",
    "governance/compat/committed_evidence_fingerprint.py",
    "governance/compat/test_run_agent_autorun_workflow_gate.py",
    "governance/compat/test_agent_autorun_machine_verification.py",
    "governance/compat/test_mfrp_shadow_canary_autocollect.py",
    "governance/compat/test_committed_evidence_fingerprint.py",
    "docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md",
    "docs/reference/review_cost_control/README.md",
    "docs/reviews/CVF_MFRP_FINGERPRINT_T1_WORKER_RETURN_2026-09-11.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md",
    "docs/baselines/CVF_GC018_MFRP_FINGERPRINT_T1_2026-09-11.md",
    "AGENT_HANDOFF_V60_2026-09-08.md",
    "CVF_SESSION",
    "CVF_SESSION_MEMORY.md"
  ],
  "claims": [
    "deterministic additive committed-evidence identity only"
  ],
  "requiredProof": [
    "legacy receipt equivalence",
    "CRLF binary and dirty-range regressions",
    "canonical producer validator collector integration"
  ],
  "operatorCheckpoints": [
    "pilot source acquisition",
    "runtime or public effect",
    "scope expansion"
  ],
  "forbiddenEffects": [
    "worker commit",
    "network",
    "provider calls",
    "source acquisition",
    "runtime implementation",
    "legacy gate suppression"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Intake Role Routing Decision

Intake summary: operator-authorized repair of committed-evidence fingerprint binding.
Route mode: MULTI_AGENT_MULTI_ROLE.
Internal worker implements; independent Local reviewer accepts/repairs; Local closer commits.
Risk sensitivity: P3_ELEVATED governance-machine surface. No external invocation.
Scope classification: bounded local deterministic validation maintenance.
Escalation condition: manifest expansion, source contradiction, or forbidden effects.

## Agent Roles

Dispatcher/reviewer/closer: Local orchestrator. Worker: operator-selected internal agent in same VS Code workspace. External Web agent: no execution role.

## Pre-Flight Checks

Capture HEAD/status; require clean staging and no pre-existing worker-path delta; prove dispatch anchor ancestry; run pre-implementation before editing. Worker does not edit dispatcher-owned packet/continuity paths.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker failures directly and rerun the applicable gate.
Ask no routine preference questions. Stop only for a source contradiction,
missing pinned source, forbidden-path need, or missing authority that prevents
honest completion.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher/reviewer/closer; operator-selected internal worker |
| phase | worker implementation then independent Local review |
| baseHeadFor(phase) | dispatchBaseHead=a6823f497; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=NOT_EXECUTED_YET |
| changedSetScope(phase) | worker exactly eleven manifest paths; reviewer may repair same paths |
| traceScope(phase, actor) | full worker command/status/diff and manifest evidence |
| commitOwner(phase) | worker forbidden; Local closer |
| crossBatchIsolation | dispatcher packet and continuity frozen during worker lane |
| nextMoveSurfaces | return -> Local review -> material/continuity commit -> separate operator decision |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: operator-selected internal worker
laneOwnedPaths: exactly eleven Required Artifact Manifest paths
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: worker terminal return, exact manifest reconciliation and empty staging

Clean worktree required at lane handoff. Dispatcher commits only dispatch material and continuity before the operator transfers this packet. Worker captures actual execution HEAD, not dispatchBaseHead as a substitute. Dispatcher will not modify worker-owned paths while the lane is active.

## Commit Mode And Base-Anchor Lifecycle

dispatchBaseHead=a6823f497; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=NOT_EXECUTED_YET. Worker must record actual start HEAD and prove dispatch anchor ancestry. Reviewer captures closureBaseHead immediately before material commit, commits material before separate continuity, and verifies homogeneous committed ranges. No future SHA prediction.

## Commit Prompt Readiness

Only Local closer may stage and commit after independent evidence review and required gates. No push. Reviewer may repair only authorized worker paths and closure artifacts; forbidden-path repair needs renewed scope.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | reviewer | PRE_DISPATCH | paired baseline, work order and the paired dispatch packets | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline, work order and the paired dispatch packets | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V60_2026-09-08.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact eleven-path Required Artifact Manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | exact Required Artifact Manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact Required Artifact Manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | worker return and exact manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact material paths and reviewer repair | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact material paths and reviewer repair | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker return reviewer disposition or separate completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | exact material paths | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

Return-Time Closeability Recheck: REQUIRED_BEFORE_REPAIR. Worker must report
whether every mandatory gate is passable without touching forbidden paths.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MFRP_FINGERPRINT_T1_WORKER_RETURN_2026-09-11.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required section names: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary; git status --short; Changed Files; Command Evidence; No-Commit Statement; Return-Time Closeability Recheck; Semantic Convergence Outcome.

Conditional section names: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. Use N/A with reason where genuinely inapplicable.

Required markers: Self-declared worker-return artifact: yes; Responds to work order:; dispatchWorkOrder; executionBaseHead; WORKER_MUST_NOT_COMMIT honored. Record actual pending paths, invocation counts and cost as UNKNOWN if unavailable. Never claim clean status while the return is untracked.

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read its applicable checker source and derive exact field/heading/enum requirements. Dispatch checklist is not a substitute. Standard additions require reference shape; worker return requires all quality/trace/delta/epistemic/closeability fields. Reproduce this packet's core guard authorization in the worker return for the worker changed set.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON
Reason: internal governed validator maintenance; no external invocation or runtime integration.

## Negative Search And Collision Discipline

Test-Path on the exact paired baseline/work-order paths returned False before creation. New helper and contract paths also returned False. Existing producer/validator/collector owners are reused; no replacement authority owner. The new helper is an implementation extraction, not a second receipt validator.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: this packet Verified Defect And Rejected Measurement
priorVerificationAnchor: trusted 3de0ba07c; disclosure a6823f497
freshRecomputeRequired: YES - reproduce exact representation mismatch in isolated Git tests
unicodePathHandling: preserve literal UTF-8 paths using NUL-delimited Git output
extractedTextAuthority: source bytes and Git objects control; normalized diagnostic text is not hash authority

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/reviewer |
| Provider or surface | local VS Code workspace |
| Session or invocation | MFRP-FINGERPRINT-T1 dispatch, 2026-09-11 |
| Working directory | repository root |
| Command or tool surface | read-only Git/search, read-only fingerprint diagnostics, apply_patch |
| Target paths | paired baseline and work order |
| Allowed scope source | operator agreement of 2026-09-11 |
| Before status evidence | clean worktree at a6823f497 before dispatch authoring; empty staging |
| After status evidence | two dispatcher-owned packets plus no registry change; no worker implementation performed |
| Diff evidence | git diff --name-status; git status --short |
| Approval boundary | exact fingerprint repair worker dispatch only |
| Claim boundary | no implemented behavior or pilot survey claim |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | mfrp-fingerprint-t1-dispatch |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order before separate continuity |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | fingerprint maintenance dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: diagnostic hashes above, not a promoted P4 observation |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no implementation performed by dispatcher |
| invocationBoundary | local source inspection and document authoring |
| interceptionBoundary | no interception or sandbox |
| claimLanguage | proposed additive binding |
| forbiddenExpansion | no provider/live/public/runtime/pilot authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator method requirement -> existing P2/P4 fingerprint owners -> internal implementation review |
| Matching local-view guard | governance/compat/check_core_guard_self_protection.py |
| Owner surface | existing receipt producer/validator/collector |
| Disposition | ADAPT the operator-approved fingerprint requirement; no source-value acceptance |
| Claim boundary | routing maintenance only, no source acquisition or absorption execution |

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: no external corpus processed.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: receipt metadata maintenance only.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus scan.

## Claim Boundary

Internal deterministic evidence-contract maintenance only. No runtime/governance-provider proof, pilot execution, absorption acceptance, public or deployment claim.

## Foundation Storage Layout Block

Use existing governance/compat owner folder and existing review_cost_control reference folder. The named helper/test are the planned size-control split. The undated contract is reached from this governed work order; no new folder, aggregate or registry owner. No dated reference is modified.

## Operator Checkpoint

Pilot source acquisition, provider invocation, public export, deployment and other effects remain outside this packet. This assignment is internal-only; the worker has no commit permission in the provenance workspace. Any wider requested effect must receive a separate bounded authorization packet. This boundary does not transfer a research recommendation into execution authority or turn a historical observation into a current trusted sample.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: internal repair and independent review only.
