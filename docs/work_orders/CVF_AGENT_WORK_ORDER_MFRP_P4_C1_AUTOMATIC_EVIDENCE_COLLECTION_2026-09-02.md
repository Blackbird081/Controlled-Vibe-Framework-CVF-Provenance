# CVF Agent Work Order - MFRP P4-C1 Automatic Evidence Collection

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION

Dispatch base head: `a0ca90e3486ca80a1f0a3ba94906c763cba00470`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: bounded local implementation worker

Reviewer/closer: reviewer/closer at returned-result boundary or declared safety trigger

Worker return path: `docs/reviews/CVF_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_WORKER_RETURN_2026-09-02.md`

## Dispatch Prompt Envelope

Role: implement P4-C1 automatic natural-evidence collection within the exact
nine-path manifest.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_2026-09-02.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: P4 shadow canary is open; P5 is sample-gated at 20 eligible
returns, with day 30 only a sunset and not a waiting requirement.

Do-not-misread notes: do not change P2, manufacture phase work, create a
daemon/watcher/queue, review each return, treat machine consistency as truth,
or open P5/P6.

Required first actions: acknowledge startup, capture clean HEAD, read this
packet and paired baseline plus named owners/checkers, recompute the
predecessor hash, run pre-implementation, then touch exactly nine paths.

Return contract: implement and test, leave all changes unstaged and
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
Routine review occurs only at the returned-result boundary.

## Purpose

Implement a fail-closed Git post-commit bridge that automatically collects
eligible natural P4 observations into an ignored pending journal, without
changing trusted routing or adding routine review.

providerExecutionAuthority: FORBIDDEN
successorTrancheOpened: NO

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION --title "MFRP P4-C1 Automatic Evidence Collection" --date 2026-09-02 --base a0ca90e3486ca80a1f0a3ba94906c763cba00470 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact P4-C1 sources, nine-path manifest, hostile tests and review-cost boundaries |
| checkerReadAheadConfirmation | checker sources listed in Checker Source Read-Ahead Block |
| docOnlyNewFields | p4ObservationEligibility; p4ObservationPhase; p4HardObligationLocator; p4HardObligationPattern; p4SourceAuthorityLocator |
| claimBoundary | dispatch provenance only; no implementation claim |

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

Roles are execution labels. Trust derives from committed return bytes, Git
ancestry/blobs, the validated P2 receipt, the actual P4 seam, and
reviewer/closer adjudication at admitted boundaries.

Scope classification: bounded protected local governance implementation.

Intake summary: connect already accepted P2 receipt evidence to the existing
P4 shadow seam after trusted commit, collecting natural rows without adding a
review boundary.

Escalation condition: only a genuine authority contradiction, forbidden tenth
path, P2/schema change, provider/network need, or inability to preserve the
trusted-before-machine order.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION
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

No pre-execution review is admitted. After acceptance, deterministic collection
does not create per-row review; review is aggregated at M5, M10, M20 or an
existing safety trigger.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p4-shadow-canary",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 1,
  "predecessor": {
    "path": "docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md",
    "sha256": "e779eabf09787e0642bac5cb48a9b0557365eb53ae6bd0e4bfcfd5c42010d176"
  },
  "blockerDelta": {
    "prior": ["eligible-pair-not-observed", "review-recall-not-yet-estimable"],
    "resolved": [],
    "retained": ["eligible-pair-not-observed", "review-recall-not-yet-estimable"],
    "new": ["automatic-collector-not-yet-implemented"],
    "reopened": [],
    "current": ["eligible-pair-not-observed", "review-recall-not-yet-estimable", "automatic-collector-not-yet-implemented"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 1
  },
  "claims": [{
    "claimId": "MFRP-P4-C1-DISPATCH",
    "claimClass": "SCHEMA_COMPATIBILITY",
    "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
    "evidenceRef": "docs/baselines/CVF_GC018_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_2026-09-02.md"
  }],
  "requiredDisposition": "READY_WITH_EXECUTABLE_PROOF",
  "successorScope": "EXECUTABLE_IMPLEMENTATION"
}
```

## Worker Autonomy / No-Question Rule

Resolve routine implementation and allowed-scope test failures directly.
Return only for a real authority/source/scope contradiction. Do not request
review of the plan or intermediate implementation. Small evidence-determined
findings at return are reviewer-local under the Review Cost standard.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| operator instruction | conversation dated 2026-09-02: record reopen chain and open P4-C1 | ACCEPT |
| P4 design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | ACCEPT |
| P4 accepted implementation return | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md` | ACCEPT |
| sample-gated P5 amendment | `docs/baselines/CVF_MFRP_P4_SAMPLE_GATED_P5_REOPEN_AMENDMENT_2026-09-02.md` | ACCEPT |
| review-cost owner | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | ACCEPT |

## Agent Roles

- Operator owns scope and any material expansion.
- Dispatcher owns this baseline/work order.
- Worker implements exactly nine uncommitted paths.
- Reviewer evaluates returned evidence without recreating implementation.
- Closer commits accepted material and synchronizes session continuity.

## Required First Reads

1. startup front door, bootstrap read model and active handoff;
2. guard orientation and literal-format gotchas;
3. this work order and paired baseline;
4. accepted P4 design, implementation return and sample-gate amendment;
5. P2 receipt owner and P4 helper/core seams;
6. hook installer, worker-return scaffolds, Review Cost standard and applicable checker sources.

## Pre-Flight Checks

- capture clean execution HEAD and prove dispatch-base ancestry;
- recompute both SCEC predecessor identities;
- confirm six CREATE targets are absent and three MODIFY targets exist;
- run ADIF resolver and pre-implementation autorun;
- confirm the exact nine-path boundary before the first write.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-P4-C1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [".githooks", "governance/compat", "scripts", "docs/reviews", "docs/baselines", "docs/work_orders", "AGENT_HANDOFF_V59_2026-08-11.md"],
  "claims": ["bounded automatic P4 shadow-evidence collection only"],
  "requiredProof": ["receipt-to-commit fingerprint linkage", "trusted-before-machine ordering", "fail-closed skip and safety behavior", "exact nine-path return"],
  "operatorCheckpoints": ["tenth path", "P2 mutation", "P5 or P6 opening", "provider or public effect"],
  "forbiddenEffects": ["trusted-route replacement", "worker commit", "provider network live public deploy production", "automatic P5 opening"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named source set",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`; full legacy bundle remains controlling.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | external critique -> committed independent review -> accepted local P4 design/return -> this bounded local successor |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | committed CVF P4 design and review artifacts, not provider memory |
| Disposition | ACCEPT_AS_ALREADY_ABSORBED_INPUT |
| Claim boundary | external text is context only; repo-governed accepted surfaces remain SOT |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded named local P2/P4 sources and already
absorbed external review evidence; no legacy source family or corpus scan is
introduced by this implementation.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`protected governance path implementation`,
role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "protected governance path implementation" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned zero items |
| Dispatch impact | no additional defect-specific constraint |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Required Artifact Manifest; Core Guard Self-Protection Authorization; Agent Handoff Contract Control Block; Worker Return Packet Shape Contract |
| gateRunPurpose | confirmation of authored evidence after source read-ahead |
| claimBoundary | bounded to this dispatch and exact changed-set gates |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| receipt binds changed bytes | implementation seam | `governance/compat/run_agent_autorun_workflow_gate.py` | `_worktree_fingerprint` and `_receipt_context` | receipt `worktreeFingerprint` | `cvf.autorun.pass-receipt.v3` | ACCEPT |
| receipt integrity is canonical | implementation seam | `governance/compat/run_agent_autorun_workflow_gate.py` | `_validate_receipt_integrity` | machineVerification digest validation | autorun owner | ACCEPT |
| P4 supports append | implementation seam | `governance/compat/mfrp_shadow_canary.py` | CLI append arguments | `--prior-ledger` and `--new-return-path` | P4 CLI | ACCEPT |
| P4 duplicate/rebound checks exist | implementation seam | `governance/compat/mfrp_shadow_canary_core.py` | observation append validation | receipt/row uniqueness | P4 core | ACCEPT |
| Git hook path already owned | integration seam | `scripts/install-cvf-git-hooks.ps1` | `core.hooksPath` setup | `.githooks` | local hook installer | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| target path existence | six new target paths absent before authoring/dispatch; three existing targets present | ACCEPT |
| token search | `rg -n "MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION" docs CVF_SESSION governance scripts .githooks` returned no prior artifact before authoring | ACCEPT |
| system-chain fingerprint collision | candidate hook/scaffold/helper paths are not pinned in `CVF_SYSTEM_CHAIN_MAP.json` | ACCEPT |
| collision decision | create one successor baseline/work order and exact implementation manifest | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> bounded worker -> reviewer/closer |
| phase | BUILD |
| baseHeadFor(phase) | dispatchBaseHead=a0ca90e3486ca80a1f0a3ba94906c763cba00470; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact nine paths in Required Artifact Manifest |
| traceScope(phase, actor) | worker commands and writes only; no private reasoning |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | execution begins from a clean descendant of dispatch base and may not absorb unrelated changes |
| nextMoveSurfaces | worker return, then reviewer/closer evidence evaluation |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement P4-C1 on these protected Python
surfaces only.

Protected paths:

- `AGENT_HANDOFF_V59_2026-08-11.md` (dispatcher-owned pre-dispatch continuity-anchor repair only; forbidden to worker)
- `governance/compat/mfrp_shadow_canary_autocollect.py`
- `governance/compat/test_mfrp_shadow_canary_autocollect.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`

Operator authorization: explicit instruction on 2026-09-02 to record the
reopen conditions durably in session and open P4-C1 automatic evidence
collection.

Rollback boundary: remove the new hook/helper/test, restore three modified
scaffold/test files and installer/pre-commit bytes, and delete only the
repository-bounded ignored P4-C1 runtime directory.

## Dual Agent Surface Accounting Matrix

| Surface | Dispatcher | Worker | Reviewer/closer |
| --- | --- | --- | --- |
| baseline/work order | author | read-only | accept or amend |
| exact nine implementation paths | authorize | implement uncommitted | inspect, locally repair small evidence-determined findings, commit |
| trusted disposition | no fabrication | read-only | owns before commit |
| pending journal | contract only | implement behavior | reconcile/promote at checkpoint |
| P5/P6/session authority | record closed conditions | forbidden | separate decision after gates |

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `.githooks/post-commit` | CREATE bounded Python launcher; always return without rewriting commit |
| `.githooks/pre-commit` | MODIFY to block unresolved P4-C1 safety marker before normal chain |
| `governance/compat/mfrp_shadow_canary_autocollect.py` | CREATE collector owner |
| `governance/compat/test_mfrp_shadow_canary_autocollect.py` | CREATE hostile/unit/integration tests |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | MODIFY optional P4 observation block |
| `governance/compat/run_worker_return_scaffold.py` | MODIFY identical optional P4 observation block |
| `governance/compat/test_run_worker_return_scaffold.py` | MODIFY cross-generator parity tests |
| `scripts/install-cvf-git-hooks.ps1` | MODIFY disclose/install post-commit hook via existing hooksPath |
| `docs/reviews/CVF_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_WORKER_RETURN_2026-09-02.md` | CREATE full evidence return |

## Work-Order Fulfillment Manifest

Fulfillment is exact equality between the nine required paths, the nine actual
changed paths and the nine paths named in the worker return. No deletion or
rename is allowed.

## Scope / Target / Owner Boundary

Allowed writes are exactly the Required Artifact Manifest. All other paths are
read-only. In particular, P2 owners, the P4 core/helper/committed ledger,
roadmaps, standards, registries, session surfaces and accepted evidence are
forbidden worker writes.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | existing hook/scaffold owners plus one bounded compat helper/test and one review return |
| Storage decision | reuse `.githooks`, `governance/compat`, `scripts`, `docs/reviews` and ignored `.cvf/runtime/mfrp-p4-shadow-canary/` |
| Existing aggregate impact | none during worker execution |
| Generated state impact | ignored atomic pending journal and unresolved safety marker only |
| Durable governance boundary | committed P4 ledger remains evidence owner after checkpoint promotion |

## Write Ownership

Worker owns uncommitted writes to the exact nine paths. Reviewer/closer owns
any in-place evidence repair, acceptance, material commit, safety-marker
adjudication, checkpoint promotion and continuity sync. The post-commit hook
owns only ignored runtime pending bytes and never a tracked commit.

## P4-C1 Automatic Collection Contract

The collector runs only after commit. It must:

1. discover zero or one changed `docs/reviews/` return carrying the exact
   optional P4 observation block;
2. require eligibility `YES`, one seven-phase label, one source-authority
   locator, one hard-obligation locator and one exact locator pattern;
3. find exactly one repository-bounded current P2 receipt candidate;
4. call the existing P2 integrity validator, never copy its digest/evaluator;
5. prove receipt base/head ancestry and reconstruct the committed-range
   fingerprint from Git blobs with the same canonical path/byte recipe;
6. compare that fingerprint to the receipt's recorded
   `worktreeFingerprint` and reject stale, ambiguous or rebound receipts;
7. read the committed return through `git cat-file`, derive its commit/blob,
   and require a reviewer/closer-owned trusted disposition already in those
   committed bytes;
8. call the existing P4 append seam once and write an atomic ignored pending
   journal under `.cvf/runtime/mfrp-p4-shadow-canary/`;
9. preserve the receipt content/digest and every immutable linkage field in
   the pending row;
10. emit only a concise local status and never amend/revert the trusted commit.

Zero candidates, multiple candidates, missing metadata, receipt mismatch or an
irrelevant commit are explicit `SKIPPED_*` results and do not increment the
sample. A semantic divergence, machine-clean/trusted-block contradiction,
hidden limitation, `UNCLASSIFIED`, order failure, identity/source drift,
external effect or audit-scope excess writes the unresolved safety marker.

The pre-commit hook checks only marker existence and invokes no AI. Its message
routes to reviewer/closer. Clearing the marker without reviewer evidence is
forbidden.

## Scaffold Metadata Contract

Both worker-return generators must emit byte-equivalent content for this
optional block:

| Field | Required placeholder/domain |
| --- | --- |
| p4ObservationEligibility | `NO` by default; worker/reviewer changes to `YES` only for a natural candidate |
| p4ObservationPhase | one of `INTAKE DESIGN SPEC WORK_ORDER BUILD REVIEW FREEZE` or `N/A with reason` |
| p4HardObligationLocator | exact committed-return section/field locator or `N/A with reason` |
| p4HardObligationPattern | exact bounded literal/regex or `N/A with reason` |
| p4SourceAuthorityLocator | exact committed source-verification locator or `N/A with reason` |

Default `NO` prevents ordinary scaffolds from accidentally enrolling. This
block adds no trusted disposition field; reviewer/closer authority remains in
the committed adjudication.

## Required Hostile Regression Matrix

- ordinary commit and default-`NO` return skip without blocking;
- zero/multiple candidate returns skip without guessing;
- missing/invalid phase or locator metadata skip;
- invalid/tampered/partial/unknown receipt rejects;
- receipt verifier-body, base/head, ancestry and fingerprint rebound reject;
- reconstructed committed bytes must change when a committed target changes;
- mutable worktree bytes cannot substitute for Git blob bytes;
- duplicate row and reused receipt do not increment;
- simulated P4 divergence writes a marker and next pre-commit blocks;
- successful collection never writes tracked paths;
- interrupted journal write preserves the prior journal;
- same immutable inputs yield the same row identity;
- both scaffold generators expose identical optional fields/defaults;
- no provider/network command or semantic phase rerun is reachable.

## Execution Plan

1. Freeze execution HEAD, identities and exact path inventory.
2. Add the optional fail-safe observation block to both scaffold generators.
3. Implement the collector and post/pre-commit hook boundaries.
4. Implement hostile tests, including real temporary Git repositories.
5. Run focused suites twice and both autorun phases.
6. Write the full worker return and reconcile exactly nine paths.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m unittest governance.compat.test_mfrp_shadow_canary_autocollect governance.compat.test_run_worker_return_scaffold
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
git diff --name-status
git diff --cached --name-status
git status --short
```

Run the focused suite twice. Record actual counts, HEAD, changed-set equality,
runtime journal test location and zero provider/network evidence.

## Acceptance Criteria

- exact nine-path changed set; no deletion/rename/stage/commit;
- collector uses actual P2 validation and actual P4 append ownership;
- Git-blob fingerprint linkage is proven by hostile tests;
- trusted disposition precedes machine disclosure;
- successful row is collected once and only once;
- skip paths are non-blocking and never increase eligible count;
- safety marker fail-closes the next commit;
- default worker returns are not enrolled;
- no tracked evidence path is dirtied by post-commit collection;
- focused tests pass twice and required gates pass;
- no P5/P6, provider, network, live, public or route authority is claimed.

## Evidence Requirements

Record execution HEAD and ancestry, source hashes, exact commands, focused
test counts from two runs, valid/skip/safety fixtures, Git blob and fingerprint
proof, pending-journal atomicity, marker blocking, both scaffold outputs,
changed-set equality, zero provider/network calls, and no-stage/no-commit
status.

## Review Gate

Routine review is admitted only after `COMPLETE_PENDING_REVIEW`. Reviewer
checks the required evidence and reruns proportional machine gates; reviewer
does not reimplement the collector. After acceptance, row accumulation has no
per-return review. M5, M10, M20 and safety triggers remain the only checkpoint
review admissions.

## Closure Checklist

- exact nine-path manifest equals returned changed set;
- all acceptance criteria have direct evidence;
- no protected owner outside authorization changed;
- tests/gates pass and HEAD remains unchanged by worker;
- reviewer disposition and material commit precede continuity sync;
- P5 and P6 remain explicitly closed.

## Operator Checkpoint

Stop and return before any tenth path, P2/P4-owner mutation, receipt schema or
family change, provider/network/live/public effect, trusted-route change, or
P5/P6 opening. No operator checkpoint is required for ordinary in-scope code
and test choices.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_COMPLETION_2026-09-02.md` (optional; prefer in-place worker-return adjudication) |
| reviewerOwnedClosurePaths | worker return in-place adjudication; material commit; session continuity sync |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_WORKER_RETURN_2026-09-02.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; Public Export Disposition; executionBaseHead;
git status --short.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Machine Closure Package.

Use `N/A with reason` for non-applicable controls.

## Stop Conditions

Stop before writing outside the nine paths, changing P2/P4 owners or committed
ledger, needing a new schema/receipt family, losing trusted-before-machine
ordering, requiring provider/network access, or encountering a real authority
contradiction. Do not stop for routine implementation choices or fixable test
failures within scope.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with executable evidence and exact
changed-set reconciliation. Return `BLOCKED_WITH_REASON` only for a stop
condition. Never emit reviewer acceptance, P4 checkpoint acceptance, P5/P6
opening or route replacement.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION dispatch, 2026-09-02 |
| Working directory | repository root |
| Command or tool surface | read-only inspection, scaffold helper and apply_patch |
| Target paths | paired baseline and work order only |
| Allowed scope source | operator instruction dated 2026-09-02 |
| Before status evidence | clean worktree at `a0ca90e3486ca80a1f0a3ba94906c763cba00470` |
| After status evidence | two new dispatch artifacts before material commit |
| Diff evidence | `git diff --name-status` plus untracked inventory |
| Approval boundary | author and commit dispatch authority; no implementation |
| Claim boundary | P4-C1 contract only |
| Agent type | dispatcher |
| Invocation ID | `mfrp-p4-c1-dispatch-2026-09-02` |
| Expected manifest | two dispatch artifacts |
| Actual changed set | reviewer/closer records before commit |
| Manifest delta | must be zero |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | dispatch authority for exact P4-C1 implementation |
| claimDisposition | CLAIM_REJECTED: implementation is not yet complete |
| receiptEvidence | N/A with reason: dispatcher consumed no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: baseline/work-order authoring only |
| invocationBoundary | local read-only inspection and two documentation writes |
| interceptionBoundary | no runtime interception exists until accepted implementation |
| claimLanguage | dispatch-ready, not implementation-complete |
| forbiddenExpansion | P2/P5/P6/provider/live/public/project effects |

## Claim Boundary

This work order authorizes exactly nine uncommitted implementation paths. It
does not assert collector correctness, activate P5/P6, alter the trusted route,
or authorize any provider/live/public/project effect.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; public sync is outside scope.
