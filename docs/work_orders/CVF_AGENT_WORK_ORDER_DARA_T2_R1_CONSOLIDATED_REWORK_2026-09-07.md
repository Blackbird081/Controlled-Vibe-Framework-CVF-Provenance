# CVF Agent Work Order - DARA T2 R1 Consolidated Rework

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-07

Batch ID: DARA-T2-R1-CONSOLIDATED-REWORK

Dispatch base head: 491396f361dec5c2127f67384d0b5d706b401026

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated implementation worker

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker repairing the held DARA-T2 candidate.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T2_R1_CONSOLIDATED_REWORK_2026-09-07.md`.

Paired baseline: `docs/baselines/CVF_GC018_DARA_T2_R1_CONSOLIDATED_REWORK_AMENDMENT_2026-09-07.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: the prior worker delta and its return are already present
uncommitted when this packet is handed off. The prior result is rejected by
the committed R1 review. The corrected contract and feasible manifest are
accepted bounded for exactly this consolidated rework. MFRP P4-C1 remains the
sole automatic reviewer-evidence collector; WP-ARCH-003 remains parked.

Do-not-misread notes: repair the existing held delta; do not restart from the
original implementation, create another worker return, edit dispatcher or
reviewer authority, change MFRP/session/roadmap/ADIF/WP paths, bump a size
exception, invoke providers, or commit.

Required first actions: acknowledge startup authority; capture full HEAD,
status, and unstaged/staged changed sets; read guard orientation, literal
gotchas, paired baseline, this packet, original R1 rejection, root-contract
amendment and review, the current held diff, size registries, and every checker
source named below; then run pre-implementation before editing.

Return contract: update the existing worker return in place, leave all changes
uncommitted and unstaged, and return `COMPLETE_PENDING_REVIEW` only if every
mandatory command and AM-01 through AM-10 pass. Otherwise return
`BLOCKED_WITH_REASON` with truthful evidence.

providerExecutionAuthority: FORBIDDEN

Completion review path: optional reviewer-owned later artifact; the committed R1 rejection remains immutable.

## Purpose

Close DARA-T2 findings R1-01 through R1-05 in one consolidated external-worker
rework. Implement fail-closed applicability, immutable committed-review
binding, complete chain checks, truthful return evidence, and the accepted
three-path maintainability split without duplicating MFRP or reviewer work.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

The orchestrator freezes the accepted repair contract, an external worker
repairs the held implementation without commit, and the reviewer evaluates
returned evidence without recreating implementation. Governed paths, committed
hashes, tests, and gate results control trust; provider identity does not.

Intake summary: the operator authorized orchestrator-managed agent exchange
after the first implementation return was rejected and the root contract was
corrected and reviewed.

Risk sensitivity: protected governance code and the final admitted external
invocation make fail-closed scope, evidence truth, and no-commit enforcement
material.

Escalation condition: stop on a new independent defect, forbidden-path need,
authority contradiction, exception bump, or requirement for invocation 3.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id DARA-T2-R1-CONSOLIDATED-REWORK --title "DARA T2 R1 Consolidated Architecture Readiness Admission Rework" --date 2026-09-07 --base 491396f361dec5c2127f67384d0b5d706b401026 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind REWORK --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 1 --root-cause-cluster-id DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION --prior-finding-set-digest 57b8e57cf888f3228fff7c322066373fb250bf71de454e84ddb18722827e665f --cumulative-external-invocation-count 1 --external-invocation-ceiling 2 --new-independent-critical-evidence DARA-T2-R1-01,DARA-T2-R1-02,DARA-T2-R1-03,DARA-T2-R1-04,DARA-T2-R1-05 --stdout` |
| generatedProfile | protected-governance-path plus no-commit external REWORK profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bound committed R1 findings and accepted amendment, exact final/cleanup manifests, AM-01 through AM-10, evidence truth, and final-invocation stop |
| checkerReadAheadConfirmation | dispatch, convergence, route, cost, source, protected-path, return, trace, size, and public guards |
| docOnlyNewFields | cleanup-only path and accepted-contract identity digest explanation only |
| claimBoundary | dispatch provenance only; no implementation or acceptance is predeclared |

## Authority Chain

1. `ECOSYSTEM/doctrine/` and `ECOSYSTEM/operating-model/`.
2. `AGENTS.md`, current work-order/review standards, and current active handoff.
3. `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_COMPLETION_2026-09-06.md` at commit `6746abf74e7ee691275a7979f78aa1b84b8b2c5a`.
4. `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md` at commit `203e9e6f7bc63873da008284688f7b533f65fbf9`.
5. `docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md` at commit `1316ea7340541ab8e675c5b1965f5a1ff3ef52d0`.
6. Paired GC-018 baseline and current code/tests.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: DARA-T2-IMPLEMENTATION

reviewRoundCount: 1

priorFindingSetDigest: 57b8e57cf888f3228fff7c322066373fb250bf71de454e84ddb18722827e665f

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: DARA-T2-R1-01,DARA-T2-R1-02,DARA-T2-R1-03,DARA-T2-R1-04,DARA-T2-R1-05

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 1

externalInvocationCeiling: 2

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

Admission rationale: the five findings were consolidated before repair and the
corrected root contract received a committed sequential design review. This
dispatch consumes invocation 2 of ceiling 2. A new independent defect, scope
expansion, or unresolved contradiction stops; it does not authorize round 3.

## Accepted Architecture Identity Echo

Architecture-Readiness Admission: NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO

architectureMatrixSchema: cvf.dara.architectureBindingMatrix.v1

architectureMatrixCanonicalDigest: 8d82ed44b5f5e66576639e54e610f4bd659210561fe6a2b6ac1a4b8b15b221b2

architectureSemanticReviewPath: docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md

architectureSemanticReviewCommit: 1316ea7340541ab8e675c5b1965f5a1ff3ef52d0

architectureSemanticReviewFileSha256: 677a7647a810fd78340b217c319dfbb7201da7ee5d3426889c503435b1008984

architectureBindingEchoDisposition: EXACT_MATCH

The canonical digest is the raw SHA-256 of the committed accepted root-contract
amendment. This work order is a documentation-only transcription of that
reviewed repair contract; it does not introduce a new worker-selected matrix.
All six identities must be emitted unchanged by both return scaffold routes
and recorded unchanged in the worker return.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "DARA-T2-R1-CONSOLIDATED-REWORK",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["implementation-repair-not-yet-proven"],
    "reopened": [],
    "current": ["implementation-repair-not-yet-proven"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "DARA-T2-R1-REWORK-DISPATCH",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Worker Autonomy / No-Question Rule

Resolve routine in-scope extraction, validation, test, and literal-shape issues
from the named authority and checker source. Ask no preference question. Stop
only for a source contradiction, forbidden path need, new independent defect,
or an acceptance requirement impossible inside the authorized manifest.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"DARA-T2-R1-CONSOLIDATED-REWORK","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reference/","governance/compat/","docs/reviews/"],"claims":["held DARA-T2 candidate can be repaired under accepted amendment"],"requiredProof":["R1-01 through R1-05","AM-01 through AM-10","exact thirteen final paths","cleanup-only base restoration","truthful no-commit return"],"operatorCheckpoints":["new independent defect","fourth new path or exception bump","provider/live/public effect"],"forbiddenEffects":["MFRP duplicate collector","worker commit","third external invocation","runtime provider live public deploy production effect"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

Expected route: `P3_ELEVATED`; shadow routing only. Full legacy gates remain
required.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | authorizes sequential orchestration/review and external rework ceiling |
| dispatcher/orchestrator | freezes findings, accepted contract, exact paths, and stop rules |
| worker | repairs held implementation and updates return without commit |
| reviewer/closer | evaluates returned evidence without implementation and owns accepted material commit |
| session-sync steward | updates continuity only after a material disposition |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, bootstrap read model, and named active handoff.
2. `docs/reference/guard_orientation/README.md` and literal gotchas.
3. Paired baseline and this work order.
4. Original T1 design/review, committed R1 rejection, root-contract amendment,
   and its accepted review.
5. All current held-diff paths and the two size exception registries.
6. Applicable checker sources in the read-ahead block, including the return
   gate and both size guards.

## Pre-Flight Checks

- Capture full HEAD and confirm it equals the committed dispatch HEAD handed to
  the worker, not the earlier authoring base shown in this packet.
- Confirm staging is empty.
- Confirm the existing uncommitted delta is exactly the held DARA-T2 candidate
  plus the existing worker return; do not treat it as accepted authority.
- Confirm the paired baseline/work order, amendment, and reviews are committed
  and absent from the worker diff.
- Run the pre-implementation gate before editing; record its exact exit state.

## Scope / Target / Owner Boundary

In scope: the thirteen final worker paths, the one cleanup-only restoration,
local source reads, Git identity/blob checks, focused tests, size gates,
pre-implementation/automation-assist, and truthful worker-return evidence.

Out of scope: dispatcher/reviewer authority, MFRP, session/roadmap/ADIF/WP,
exception registry, extra evidence system, external source intake, runtime,
provider/live/network, public sync, deployment, production, staging, commit,
push, and successor opening.

## Required Final Artifact Manifest

| Path | Required worker action |
|---|---|
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | MODIFY: retain compact pointer and common dispatch fields |
| `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | CREATE: full canonical DARA schema, applicability, binding, chain, echo, evidence-truth, and claim boundary |
| `governance/compat/build_dispatch_packet_scaffold.py` | MODIFY: extract DARA renderer; finish at or below 874 physical lines |
| `governance/compat/build_dispatch_packet_architecture_readiness.py` | CREATE: DARA renderer/constants only |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | MODIFY: exact six-field echo |
| `governance/compat/check_work_order_dispatch_quality.py` | MODIFY: fail-closed top-level DARA validation while preserving entrypoint |
| `governance/compat/check_work_order_dispatch_quality_range.py` | MODIFY: applicable changed-work-order integration |
| `governance/compat/check_work_order_dispatch_quality_source.py` | MODIFY: closed-chain and immutable committed-review validation helpers |
| `governance/compat/run_worker_return_scaffold.py` | MODIFY: exact six-field echo parity |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | MODIFY: extraction/default/no-second-review regressions |
| `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py` | CREATE: all DARA positive/negative/hostile tests |
| `governance/compat/test_run_worker_return_scaffold.py` | MODIFY: both route echo parity and drift rejection |
| `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md` | MODIFY in place: truthful R1 rework evidence; no second return |

Exact final-manifest rule: final `git diff --name-only` relative to the worker's
captured execution base must equal these thirteen paths. No fourth new path,
deletion, rename, or generated cache is allowed.

## Cleanup-Only Writable Path

`governance/compat/test_check_work_order_dispatch_quality.py` is authorized
only to remove the prior worker's DARA additions and restore the exact
execution-base blob. It must be byte-identical to
`<executionBaseHead>:governance/compat/test_check_work_order_dispatch_quality.py`
and absent from the final diff. All DARA tests belong in the exact new dedicated
test file. Failure of either condition blocks return readiness.

## Work-Order Fulfillment Manifest

| Requirement | Required proof |
|---|---|
| final equality | thirteen final paths exactly; cleanup-only file absent |
| findings | R1-01 through R1-05 each map to code, regression, and evidence ID |
| acceptance | AM-01 through AM-10 each PASS with command/locator evidence |
| size | main scaffold at most 874 lines; both size guards zero violations; no exception change |
| immutable review | real commit/ancestor/path/blob/SHA/criterion checks, never current-tree substitution |
| evidence truth | every reported PASS has zero exit and complete required case count |
| no external effect | providerCallCount=0; no runtime/public/deploy action |
| no commit | HEAD unchanged through worker execution and staging empty |

## Architecture Readiness Repair Contract

### R1-01 - fail closed on missing declaration

Every active `EXTERNAL_AGENT_CLI_MCP` work order must carry exactly one
architecture declaration. Absence, unknown value, or ambiguous classification
returns `BLOCKED_ARCHITECTURE_APPLICABILITY_UNCLASSIFIED`. Allowed external
declarations are `REQUIRED`, `NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO`, and
`NOT_APPLICABLE_EXTERNAL_LOW_RISK_WITH_REASON:<reason>`. Internal dispatch has
its separate explicit with-reason form. Remove or invert any test that treats
external omission as non-applicable.

### R1-02 - bind semantic acceptance to committed bytes

For accepted bounded and accepted-design echo, require exactly 40 lowercase
hex characters, resolve to a commit, prove ancestor of current HEAD, require
the normalized review path in that commit, read `<commit>:<path>` bytes, match
their SHA-256, and confirm all relevant criterion identities/verdicts. Reject
nonexistent, non-ancestor, wrong-path, wrong-blob-hash, stale-working-tree, and
missing-criterion cases. Positive tests must use a genuine repository commit.

### R1-03 - validate the full closed chain

Parse `trustSource` as exact normalized repo-relative authority path plus a
non-empty resolving locator. Resolve `contextCarrierPath` plus `contextField`.
Reject archive, provider-private/memory, traversal, absolute, and outside-repo
authority/owner identities. Require `evidenceOutputPath` to be a normalized,
dated, authorized repo-relative Markdown evidence/review path with existing
parent. Split every semicolon-delimited rollback path and require containment
in the work order's writable manifest. Keep exemptions field-specific. Emit
specific diagnostics and one negative test per rule.

### R1-04 - make evidence labels truthful

No command with a nonzero exit or an incomplete required case set may be
labeled PASS. Use FAIL, KNOWN_FAILURE_WITH_REASON, or BLOCKED_WITH_REASON.
`COMPLETE_PENDING_REVIEW` is allowed only when every mandatory gate passes.
Base replay may attribute a failure but cannot change its exit state.

### R1-05 - implement the feasible split

Move the full schema/contract from the near-threshold template into the exact
new same-directory standard, leaving a compact canonical pointer. Extract the
renderer into the exact new helper and keep the main scaffold at or below 874
physical lines. Restore the frozen monolithic test to its execution-base blob
and move all DARA tests into the exact new dedicated file. Do not change either
exception registry or compress statements to game a threshold.

## Hostile Test And Acceptance Matrix

| ID | Required case | Acceptance |
|---|---|---|
| AM-01 | active external work order without declaration | blocks as unclassified |
| AM-02 | accepted echo bound to genuine committed review | passes without second review |
| AM-03 | fake/non-ancestor/wrong-path/wrong-blob/stale/missing-criterion review identity | every variant blocks |
| AM-04 | missing trust/locator, carrier/field, rollback containment, dated output, or authority boundary | each variant blocks independently |
| AM-05 | original HT-01 through HT-16 | all pass with HT-02 omission blocked and HT-09 immutable-blob meaning |
| AM-06 | paired and standalone worker-return generators | six fields match exactly; drift blocks |
| AM-07 | Python and Markdown size guards | zero violations and no exception bump |
| AM-08 | pre-implementation and automation-assist | both zero-exit after unrelated-path isolation |
| AM-09 | worker-return command ledger | no false PASS and terminal status reconciles |
| AM-10 | final manifest and cleanup | exact thirteen; cleanup-only path absent and base-identical |

The original sixteen families remain mandatory: complete accepted matrix;
missing declaration/row; placeholder output; duplicate behavior owner;
nonexistent path/locator/symbol; missing producer chain; missing production
composition test; worker-selected/pending semantics; immutable review mismatch;
digest drift; unknown/reached usage; reviewer-recreation contradiction;
accepted-design echo; internal non-applicability; MFRP non-regression; and
historical WP-ARCH-003 isolation.

## Execution Plan

1. Freeze full execution base, worker diff, old monolithic-test blob, and first
   command states.
2. Remove the inverse omission test and restore the monolithic test base blob.
3. Add the standard/helper/dedicated-test split before expanding semantics.
4. Implement R1-01 through R1-03 with a targeted negative regression for each
   defect and accepted-echo validation against genuine committed bytes.
5. Align both return scaffold routes and the exact six identity fields.
6. Run focused tests and size guards; repair only inside authorized paths.
7. Run pre-implementation/automation-assist/worker-return gates with exact
   unrelated-path isolation and record their true exit states.
8. Reconcile AM-01 through AM-10, final diff, counters, invocation 1-to-2, and
   update the existing return in place.

## Evidence Requirements

The worker return must include:

- start/end full HEAD, unstaged/staged status, and exact final paths;
- before/after line counts for template, main scaffold, frozen monolithic test,
  and each new split file;
- execution-base versus final SHA-256 for the cleanup-only test file;
- one evidence row per R1 and AM item with code/test locator and command result;
- genuine review commit/path/blob/SHA test fixture identities;
- every first-run and final-run command, exit code, case counts, and repair;
- a gate-failure ledger with truthful status labels;
- non-negative fault counters and evidence IDs;
- external invocation before=1, after=2; provider calls=0; elapsed/usage or exact
  unavailability reason;
- no exception, MFRP, dispatcher/reviewer, session/roadmap/ADIF/WP, or commit
  change; and
- natural P4 observation fields only if current P4-C1 marks the return eligible.

## Fault Attribution And Foundation Learning Contract

Retain the prior review's attribution: R1-05 is an
`ORCHESTRATOR_ARCHITECTURE_DEFECT`; do not charge it to the worker. R1-01
through R1-03 are worker contract-execution defects under the complete T1
intent, R1-04 is worker evidence interpretation, and any new deterministic
admission gap must be reported without blame until evidence resolves it.

Required scalars remain `dispatcherDefectCount`,
`workerExecutionDefectCount`, `reviewerLateDiscoveryCount`,
`repairIntroducedDefectCount`, `machineCoverageGapCount`,
`unattributedDefectCount`, and `faultAttributionEvidenceIds`. Every nonzero
count needs a resolvable evidence row.

## Reviewer Non-Duplication Contract

The reviewer consumes valid hashes, diff, test outputs, and failure ledger.
Routine review is limited to source/diff inspection, targeted contradictions,
worker-return fast/steward gates, and M5/M10/safety/M20 when admitted by MFRP.
No broad suite is rerun merely to recreate worker evidence. The reviewer does
not edit implementation. Since this dispatch reaches the cumulative ceiling,
rejection cannot automatically create another external rework round.

## Verification Commands

Confirm each command signature from source or `--help` before execution.

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m unittest governance.compat.test_build_dispatch_packet_scaffold governance.compat.test_run_worker_return_scaffold governance.compat.test_check_work_order_dispatch_quality_architecture_readiness
python governance/compat/check_python_automation_size.py
python governance/compat/check_governed_file_size.py
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status <executionBaseHead>
git diff --cached --name-status
git status --short
```

Do not run the restored monolithic test module as a DARA test owner. Its base
blob equality and absence from final diff are mandatory separate proofs.

## Acceptance Criteria

- R1-01 through R1-05 and AM-01 through AM-10 all have zero-exit evidence.
- Missing external declarations and every malformed closed-chain identity fail
  before invocation.
- Accepted echo is validated from immutable committed bytes and does not open
  a second reviewer workflow.
- Both return scaffold routes emit exactly the six accepted identity values.
- Main scaffold is at most 874 lines; both size guards pass; registries remain
  unchanged; cleanup-only test is base-identical and absent final diff.
- Final changed set equals the exact thirteen paths.
- All mandatory commands pass; return evidence contains no false PASS label.
- HEAD is unchanged by the worker, staging is empty, and provider calls are zero.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if all acceptance criteria pass. Otherwise
return one `BLOCKED_WITH_REASON` containing the exact blocker and preserved
evidence. Do not silently add a path, weaken a test, change authority, or start
another agent. Do not request an automatic third external invocation.

## Operator Checkpoint

No operator micro-checkpoint is required for in-scope repair. Stop for a new
independent defect, fourth new path, exception bump, authority contradiction,
provider/live/public effect, destructive operation, or any condition requiring
external invocation 3. The orchestrator owns all subsequent agent exchange.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_COMPLETION_2026-09-06.md`

priorVerificationAnchor: commit `6746abf74e7ee691275a7979f78aa1b84b8b2c5a`; SHA-256 `57b8e57cf888f3228fff7c322066373fb250bf71de454e84ddb18722827e665f`

freshRecomputeRequired: YES

recomputeReason: rework changes executable admission, Git binding, closed-chain validation, scaffold echo, and test ownership

unicodePathHandling: use literal paths and UTF-8-safe readers; do not rewrite unrelated Unicode paths

extractedTextAuthority: committed governed repository bytes and direct local command output only

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| paired baseline/work order | exact `Test-Path -LiteralPath` returned false before authoring | ACCEPT_NO_COLLISION |
| batch token | exact hidden/no-ignore search across docs/session returned no earlier packet | ACCEPT_NO_COLLISION |
| worker return | existing rejected candidate is deliberately reused in place | REUSE_EXACT_PATH |
| standard/helper/dedicated test | exact new paths authorized by accepted amendment | CREATE_AUTHORIZED |
| second collector/return/review | forbidden | REJECT_PARALLEL_OWNER |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| consolidated R1 findings | review evidence | `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_COMPLETION_2026-09-06.md` | Findings / Position | DARA-T2-R1-01 through DARA-T2-R1-05 | R1 reviewer | ACCEPT |
| fail-closed and split contract | design authority | `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md` | Amended Applicability Contract | Architecture-Readiness Admission | DARA R1 amendment | ACCEPT |
| rework release | review authority | `docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md` | Decision / Disposition | DESIGN_ACCEPTED_BOUNDED_FOR_ONE_CONSOLIDATED_REWORK | amendment reviewer | ACCEPT |
| Python split requirement | size authority | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | exceptions | governance/compat/test_check_work_order_dispatch_quality.py | Python size registry | ACCEPT |
| Markdown rotation | size authority | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | proactiveOwnerSurfaces | docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md | governed file-size registry | ACCEPT |
| reviewer non-recreation | review authority | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Reviewer Work Boundary | EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION | Review Cost standard | ACCEPT |
| MFRP collector ownership | current work order authority | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_2026-09-02.md` | Automatic Collection Boundary | mfrp_shadow_canary_autocollect.py | MFRP P4-C1 | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 22 |
| Returned defects | all IDs listed above |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | source-first packet, exact protected/split manifest, immutable bindings, truthful return, and no-commit/final-ceiling stop |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/run_agent_automation_assist.py` |
| literalTokensReviewed | DISPATCH_READY, REWORK scalars, source columns, protected paths, worker-return full-gate fields, trace labels, accepted design echo, exact final/cleanup manifests, private export disposition |
| gateRunPurpose | confirm the completed packet and collect dispatch evidence; not discover semantics after dispatch |
| claimBoundary | checker PASS proves packet conformance only; it does not prove the held implementation repaired |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing reference/checker/scaffold owners, three exact same-domain split paths, one existing worker return |
| Storage decision | split within current `docs/reference` and `governance/compat` roots; create no new root, registry, index, or evidence store |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | new reference owns full DARA contract; existing dispatch-quality entrypoint remains the machine gate; MFRP remains measurement owner |

## Write Ownership

The worker owns uncommitted edits only to the thirteen final paths and the one
cleanup-only path. Dispatcher inputs and accepted design/reviews are read-only.
Reviewer/closer alone may accept, stage, commit, create a completion review if
needed, and update continuity later.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> orchestrator/dispatcher -> no-commit external implementation worker -> reviewer/closer |
| phase | DARA-T2 R1 consolidated rework |
| baseHeadFor(phase) | dispatchBaseHead=491396f361dec5c2127f67384d0b5d706b401026; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact thirteen final worker paths plus one cleanup-only path that must be absent final diff |
| traceScope(phase, actor) | worker records diff, hashes, lines, R1/AM evidence, failures, usage and no-commit; reviewer consumes returned evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only after acceptance |
| crossBatchIsolation | exclude dispatcher/reviewer/session/MFRP/WP material; parked WP files remain hash-preserved and are not worker inputs |
| nextMoveSurfaces | existing worker return, then one reviewer decision; no automatic third invocation, DARA-T3, or WP repair |

## Dual Agent Surface Matrix

| Surface | Status | Authority boundary |
|---|---|---|
| INTERNAL_AGENT | ORCHESTRATOR_REVIEWER_ONLY | orchestrator authors dispatch and reviewer evaluates returned evidence; neither implements worker delta |
| EXTERNAL_AGENT_CLI_MCP | AUTHORIZED_FINAL_INVOCATION | one no-commit implementation rework within exact manifest |
| adapter boundary | MANUAL_OPERATOR_MEDIATED | prompt/packet handoff only; no runtime adapter or provider authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | held candidate -> committed R1 rejection -> accepted local contract amendment -> bounded rework |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | committed R1 review, amendment/review, paired baseline and this work order |
| Disposition | REUSE_REJECTED_CANDIDATE_FOR_AUTHORIZED_REPAIR_ONLY |
| Claim boundary | worker output remains candidate evidence until reviewer acceptance; no external statement becomes authority |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is a bounded repair of named current
governance owners and a previously returned worker delta; it makes no legacy
corpus, scan-completeness, or absorption-coverage claim.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | reviewer may create one conventional completion review only if needed; must not overwrite committed R1 rejection |
| reviewerOwnedClosurePaths | accepted thirteen-path material, existing worker return, optional new completion review, and separate continuity update |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before editing the return and new reference, read checker source for each
output's path family and docType. The new reference must contain its own Scope /
Applies To, Target / Source, implementation boundary, risk/corrective action,
trace, public disposition, and claim boundary as required by active checkers.
The return must satisfy the full-gate profile and replace every stale prior
claim and placeholder with final truthful evidence.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Checker Source
Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Rework Convergence Self-Proof; Conditional Controls
Disposition; Public Export Disposition; executionBaseHead; git status --short;
Changed Files; Command Evidence; No-Commit Statement; Claim Boundary.

Conditional controls must use an exact N/A-with-reason disposition when truly
inapplicable. Do not create a machine closure package; reviewer/closer owns it.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: close R1-01 through R1-05 only on the
protected final-manifest paths plus the cleanup-only base restoration.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/build_dispatch_packet_architecture_readiness.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
- `governance/compat/test_check_work_order_dispatch_quality.py` (cleanup only; final diff forbidden)

Operator authorization: on 2026-09-07 the operator authorized the sequential
orchestrator/reviewer route and delegated agent-to-agent exchange without
operator intervention.

Rollback boundary: revert only the eventual accepted DARA-T2 rework material;
preserve committed R1 review, amendment/review, MFRP P4-C1, continuity history,
and parked WP artifacts.

Not authorized: worker commit, fourth new path, exception bump, MFRP or session
mutation, roadmap/ADIF/WP repair, third external invocation, provider/live,
public sync, deployment, or successor work.

## Commit Mode And Base-Anchor Lifecycle

dispatchBaseHead: `491396f361dec5c2127f67384d0b5d706b401026`

executionBaseHead: worker captures the final committed dispatch HEAD after the
orchestrator restores the held delta.

closureBaseHead: reviewer captures only after acceptance and material commit.

The worker must not stage or commit. The reviewer/closer owns all material and
continuity commits.

## Review Gate

Review occurs once at worker return. The reviewer checks the returned diff,
immutable review-binding implementation, exact manifest/cleanup proof, size
outcomes, targeted contradiction evidence, and worker-return/steward gates.
The reviewer does not implement code or duplicate broad suites. A rejection at
ceiling 2 stops for operator/design reassessment; it does not auto-dispatch.

## Closure Checklist

- [ ] R1-01 through R1-05 and AM-01 through AM-10 reconcile to evidence.
- [ ] exact thirteen final paths; cleanup-only path absent and base-identical.
- [ ] three new paths only; exception registries and MFRP untouched.
- [ ] main scaffold at most 874 lines and both size guards pass.
- [ ] accepted echo uses genuine committed review bytes and exact six fields.
- [ ] all mandatory commands zero-exit; no false PASS or stale completion claim.
- [ ] invocation count is 2 of 2, provider calls zero, HEAD unchanged, staging empty.
- [ ] reviewer disposition precedes any material commit or successor decision.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/dispatch author preparing later reviewer-only evaluation |
| Provider or surface | local private CVF workspace; external-worker handoff is manual |
| Session or invocation | DARA-T2 R1 consolidated rework dispatch authoring, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | committed source/hash reads, size registry/checker reads, ADIF resolver, scaffold preview, collision checks, apply_patch, pre-dispatch gate |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator authorization for sequential orchestration/review and autonomous inter-agent exchange |
| Before status evidence | clean worktree at HEAD `491396f361dec5c2127f67384d0b5d706b401026`; worker delta held in named stash; WP files hash-preserved outside worktree |
| After status evidence | exactly two dispatch artifacts; worker delta not edited during dispatch authoring |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | one consolidated DARA-T2 external rework packet only |
| Claim boundary | no implementation, acceptance, provider/live/public effect, or third invocation |
| Agent type | orchestrator/dispatcher now; reviewer after worker return |
| Invocation ID | `dara-t2-r1-consolidated-rework-dispatch-2026-09-07` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local DARA dispatch-quality/template/scaffold implementation and tests |
| claimDisposition | CLAIM_REJECTED until worker evidence and reviewer acceptance exist |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no new runtime receipt is authorized |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime/provider action is authorized |
| invocationBoundary | exactly one final external implementation invocation; local tests only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control |
| claimLanguage | bounded pre-invocation governance implementation candidate |
| forbiddenExpansion | MFRP duplication, runtime/provider/live/public/package/deploy behavior, third external invocation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation rework work order; public sync is forbidden.

## Claim Boundary

This work order authorizes exactly one no-commit repair of the held DARA-T2
candidate on thirteen final paths plus one cleanup-only restoration. It does
not accept the result, authorize another worker return or external round,
modify MFRP/session/roadmap/ADIF/WP authority, open DARA-T3, run providers,
publish, deploy, or claim runtime or production readiness.
