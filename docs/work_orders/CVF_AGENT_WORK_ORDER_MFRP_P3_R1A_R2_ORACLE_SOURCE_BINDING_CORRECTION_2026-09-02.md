# CVF Agent Work Order - MFRP-P3-R1A-R2 Oracle Source-Binding Correction

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP-P3-R1A-R2

Dispatch base head: `184a290e9729b0a196db156d83375ae080bb6930`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: bounded provider-free oracle source-binding correction worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_2026-09-02.md`.

Paired baseline: `docs/baselines/CVF_GC018_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_2026-09-02.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: the first R1B replay is committed rejected evidence at
`2b06d928d`; its reviewer disposition is `RETURN_TO_DESIGN`. The operator
authorized R1A-R2 correction followed by R1B repair. P4 remains closed.

Do-not-misread notes: correct evidence binding, not case semantics. Do not
import or call P2, construct receipts, execute replay, alter the rejected R1B
artifacts, or add an executable helper. Do not stage or commit.

Required first actions: acknowledge startup authority; capture HEAD and clean
status; read this packet, its baseline, guard orientation, literal gotchas,
the R1 redesign, the full reviewer adjudication and the current oracle;
recompute every pinned source/P2 hash; run the pre-implementation gate; then
touch only the exact two-path manifest.

Return contract: return `COMPLETE_PENDING_REVIEW` with worker terminal
candidate `ORACLE_CORRECTION_CANDIDATE`, or `BLOCKED_WITH_REASON`. The worker
must not emit reviewer ratification, R1B acceptance, or P4 readiness.

Worker: bounded local evidence-correction worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_WORKER_RETURN_2026-09-02.md`

successorTrancheOpened: NO

## Purpose

Make all 19 historical source references in the committed oracle mechanically
reconstructable, repair C02/C06, and freeze a corrected oracle identity for a
later R1B-R2 packet.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

The dispatcher fixes scope, a worker corrects two artifacts, and a reviewer
evaluates the returned evidence without recreating implementation. SOT paths,
hashes, locators, line ranges, and recomputed digests control trust; agent and
role labels do not.

Intake summary: the operator requested R1A-R2 oracle correction followed by
R1B repair to satisfy P4 prerequisites.

Risk sensitivity: protected governance fixture, false-confidence, and later
P4 readiness are material; provider/live/public/production effects are closed.

Escalation condition: stop and return to the operator only for source identity
contradiction, required semantic change, or an out-of-manifest dependency.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-P3-R1A-R2
reviewRoundCount: 2
priorFindingSetDigest: a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: R1B_RV_1_SOURCE_BINDING_NOT_EXECUTED_R1B_RV_2_ORACLE_BINDING_DEFECT_R1B_RV_3_LEDGER_EVIDENCE_GAP
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 1
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: mfrp-p3-r1-oracle-source-binding-and-replay-evidence
reworkGeneration: 2
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

The source-binding defects were already independently reviewed and committed;
another pre-execution review would add no new evidence. Review resumes once at
the worker return. A discovered identity contradiction is a stop condition,
not a reason to improvise or invoke another reviewer mid-step.

## Worker Autonomy / No-Question Rule

Resolve routine in-scope line ranges, hashes, JSON formatting, and return-gate
issues directly from the named source and checker. Ask no preference question.
Stop only for an actual contradiction or out-of-scope need.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p3-r1a-r2-source-binding-correction",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["oracle-source-binding-not-executable", "oracle-c02-locator-invalid", "oracle-c06-excerpt-unreproducible", "r1b-ledger-evidence-incomplete"],
    "reopened": [],
    "current": ["oracle-source-binding-not-executable", "oracle-c02-locator-invalid", "oracle-c06-excerpt-unreproducible", "r1b-ledger-evidence-incomplete"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "MFRP-P3-R1A-R2-DISPATCH",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/baselines/CVF_GC018_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_2026-09-02.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator correction instruction | operator message dated 2026-09-02 | ACCEPT |
| R1 replay/source-binding contract | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | ACCEPT |
| committed adjudication | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | ACCEPT |
| accepted P4 prerequisite boundary | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_REVISION_1_INDEPENDENT_REREVIEW_2026-09-02.md` | ACCEPT |

## Agent Roles

- Operator: authorizes R1A-R2 and later R1B repair authoring.
- Dispatcher: owns this exact packet and source verification.
- Worker: corrects only the oracle and produces the return.
- Reviewer/closer: verifies returned evidence and alone ratifies/commits.
- Session-sync steward: updates continuity only after a material disposition.

## Scope / Target / Owner Boundary

In scope: static file reads, UTF-8/LF normalization, line-range extraction,
SHA-256/JCS recomputation, JSON edits, and local non-provider validation.

Out of scope: P2 import/invocation/mutation, receipt construction, R1B replay,
checker/standard/hook/catalog/session changes, P4 execution, downstream
workspace, provider/live/network, public sync, deployment, and production.

## Required First Reads

1. `CVF_SESSION_MEMORY.md` and bootstrap read model.
2. `docs/reference/guard_orientation/README.md`.
3. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
4. Paired baseline and this work order.
5. R1 redesign and committed R1B worker return including adjudication.
6. Current oracle and all seven sources in its `sourceManifest`.
7. Applicable checker sources named below.

## Pre-Flight Checks

- Confirm HEAD descends from `184a290e9729b0a196db156d83375ae080bb6930`.
- Confirm clean worktree and empty staging area.
- Confirm current oracle SHA-256 is
  `6aa32c3157092c974441c269d17e85aed20d5ba535479523eda5b64d23b3fbf2`.
- Confirm reviewer finding-set SHA-256 is
  `a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c`.
- Recompute all seven sourceManifest and two P2 seam identities.
- Run pre-implementation gate before editing.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-P3-R1A-R2",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["governance/compat/fixtures", "docs/baselines", "docs/work_orders", "docs/reviews"],
  "claims": ["deterministic source-binding correction candidate only"],
  "requiredProof": [
    "nine pinned source identities",
    "nineteen locator-contained line ranges and excerpt digests",
    "C02 and C06 source-faithful correction",
    "unchanged normative case fields and exact 19/18/7 coverage",
    "exact two-path no-commit manifest",
    "independent reviewer disposition"
  ],
  "operatorCheckpoints": [
    "source contradiction or semantic change",
    "any third path or P2 execution",
    "any P4 or external effect"
  ],
  "forbiddenEffects": [
    "runtime provider network public deploy production or downstream effect",
    "worker oracle ratification or automatic P4 opening",
    "worker commit or P2 owner mutation"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named source set",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`; shadow routing only. Full legacy gates remain
required.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing non-executable oracle fixture plus reviewer return |
| Storage decision | reuse current fixture/review directories; create no folder, index, registry or front door |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | corrected oracle remains normative machine data; no helper runtime or parallel SOT |

## Required Artifact Manifest

| Path | Action | Owner |
|---|---|---|
| `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | MODIFY | worker |
| `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_WORKER_RETURN_2026-09-02.md` | CREATE | worker |

No other path may change.

## Write Ownership

| Path | Owner | Mode |
|---|---|---|
| `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | worker edits; reviewer verifies | MODIFY |
| `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_WORKER_RETURN_2026-09-02.md` | worker authors; reviewer evaluates | CREATE |

## Work-Order Fulfillment Manifest

| Requirement | Required proof |
|---|---|
| exact manifest | final status lists exactly two paths |
| closed extraction | every case has exact locator-contained line range and digest |
| semantic preservation | 19/18/7 and normative-field diff show no drift |
| deterministic identity | two independent validations are byte-identical |
| no external effect | providerCallCount is zero |

## Source Locator And Excerpt Contract

For every case add `sourceExcerptLineRange` with one-based inclusive
`startLine`, `endLine`, and exact `includeTrailingLf: false`. Set byte recipe
to `UTF8_NO_BOM_LF_NORMALIZED_LINE_RANGE_V1`. Normalize CRLF and lone CR to
LF, split into lines, select the inclusive range, join with LF, add no trailing
LF, encode UTF-8 without BOM, and hash those exact bytes. The exact locator
string must occur inside the selected range.

C02 must use `## Risk / Corrective Action`. C06 must select a concise range
under `## Risk / Corrective Action` whose text supports manifest omission or
unauthorized-path risk. Recompute its digest from that range. Do not select
unrelated text merely to obtain a hash.

## Oracle Preservation Contract

Apart from `sourceRef.locator`, `sourceRef.sourceExcerptLineRange`,
`sourceRef.sourceExcerptSha256`, and `sourceRef.byteRecipe`, every case field
must remain byte-for-byte/JCS-value equivalent. Preserve schema/profile,
sourceManifest, p2SeamIdentity, required sets, ordering, feasibility and claim
boundary. Any needed semantic change blocks this work order.

## Execution Plan

1. Freeze pre-edit oracle and authority hashes.
2. Resolve all 19 locator-contained source ranges from pinned source bytes.
3. Correct C02 and choose a truthful new C06 range.
4. Add closed ranges and recompute all 19 excerpt digests.
5. Validate source/P2 identities, coverage, semantic preservation and JSON.
6. Run two independent reconstruction passes and compare output bytes.
7. Create the worker return, run the required gate, and stop uncommitted.

## Acceptance Criteria

- Exactly two changed paths; no staging/commit.
- All seven source and two P2 hashes match.
- 19/19 locators occur inside their exact line ranges.
- 19/19 excerpt digests recompute from the one published recipe.
- C02 and C06 corrections satisfy the baseline.
- Non-sourceRef normative values, 19 case IDs, 18 families and seven classes
  are unchanged.
- Worker return includes new raw/JCS/required-set hashes and replay pinning
  data for R1B-R2.
- Focused local validation and worker-return fast gate pass.

## Evidence Requirements

Record execution base, before/after status, exact changed set, all authority
hashes, per-case line ranges/digests, C02/C06 excerpts, semantic-preservation
comparison, deterministic double-run evidence, gate outputs, zero provider
calls, and no-commit proof. Evidence must be reproducible, not self-attested.

## Stop Conditions

Stop for any hash drift, missing source/locator, unsupported semantic change,
third-path need, P2 execution/edit need, live/provider/network need, or gate
failure that cannot be repaired inside the exact two paths.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` with `ORACLE_CORRECTION_CANDIDATE` only when
all acceptance criteria and required gates pass. Otherwise return one
`BLOCKED_WITH_REASON` containing the exact evidence gap. Never return a
reviewer-owned ratification, R1B acceptance, or P4 authorization token.

## Operator Checkpoint

No extra review is required before this worker executes. Routine review occurs
at its return. If the correction is accepted and committed, R1B-R2 authoring
is already operator-authorized and needs no new operator micro-checkpoint; its
work order must pin the new oracle commit/hash before dispatch. P4 remains
closed until R1B-R2 is accepted.

## Forbidden Actions

Do not stage/commit, modify a third path, edit executable governance code,
execute/import P2, build receipts, alter case semantics, rewrite rejected
evidence, call any provider/network/live surface, open P4, or claim improvement.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
git diff --cached --name-status
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 184a290e9729b0a196db156d83375ae080bb6930 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
```

The worker may use a non-writing inline local script for hashing and JSON
validation. It must not create a helper or cache file in the repository.

## Evidence Reuse And Encoding Plan

| Evidence | Mode | Encoding |
|---|---|---|
| committed source/P2 bytes | RECOMPUTE_REQUIRED | raw SHA-256 |
| current oracle identity | RECOMPUTE_REQUIRED | raw bytes plus RFC 8785 JCS |
| reviewer findings | REUSE_PRIOR_VERIFICATION | UTF-8 source text, exact committed hash |
| worker output | REVIEWER_RECOMPUTE_ONLY | UTF-8 JSON/Markdown |

No provider-specific memory is CVF authority.

## Negative Search And Collision Discipline

The baseline, work order, and worker-return target were absent before
authoring. Existing R1A-R1 and R1B paths are predecessor evidence, not naming
collisions. No competing R1A-R2 owner was found.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| source-binding requirement | governed design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | Source And Locator Binding | committed oracle sourceRef | R1 redesign | ACCEPT |
| three correction findings | reviewer evidence | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | Independent Reviewer Adjudication | R1B-RV-1 through R1B-RV-3 | reviewer disposition | ACCEPT |
| current oracle bytes | committed fixture | `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | complete JSON | oracle v1 | R1A oracle | ACCEPT |
| P4 prerequisite | accepted design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | Dependency And Opening Rule | accepted R1B | P4 design | ACCEPT |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded correction of a named committed oracle; no
legacy corpus or absorption coverage claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | committed advisory evidence -> CVF reconciliation -> local correction authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R1 redesign, R1 reconciliation, adjudicated R1B return and this packet |
| Disposition | NO_NEW_ABSORPTION |
| Claim boundary | local correction only; no external statement becomes runtime truth |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`oracle source binding correction`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

Disclosed defectIds: NONE

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | exact dispatch/no-commit fields, review admission, Source Verification columns, protected-path authorization, worker-return full-gate contract |
| gateRunPurpose | confirm the already-authored packet shape and collect pre-dispatch evidence before local worker dispatch |
| claimBoundary | gate PASS proves shape, not source meaning or oracle ratification |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1A-R2 --title "Oracle Source-Binding Correction" --date 2026-09-02 --base 184a290e9729b0a196db156d83375ae080bb6930 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 2 --root-cause-cluster-id mfrp-p3-r1-oracle-source-binding-and-replay-evidence --prior-finding-set-digest a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --new-independent-critical-evidence R1B_RV_1_R1B_RV_2_R1B_RV_3 --scec-problem-key mfrp-p3-r1a-r2-source-binding-correction --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | protected-governance-path internal no-commit rework |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact oracle correction contract, line recipe, two-path manifest and conditional R1B-R2 rule |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | sourceExcerptLineRange, line-recipe definition, R1B-R2 pinning data |
| claimBoundary | provenance only; no result is predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify only the existing named oracle
fixture. No executable guard/checker/helper, P2 owner, hook, standard, catalog,
registry, or session surface may change.

Protected path:

- `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json`

Operator authorization: explicit 2026-09-02 instruction opening R1A-R2 oracle
correction and R1B repair toward P4 eligibility.

Rollback boundary: restore the oracle's pre-worker committed bytes and remove
the one new worker return; rejected evidence remains immutable.

## Commit Mode And Base-Anchor Lifecycle

dispatchBaseHead: `184a290e9729b0a196db156d83375ae080bb6930`

executionBaseHead: worker captures the clean descendant at start.

closureBaseHead: reviewer captures after the accepted material commit.

The worker must not commit. Reviewer/closer owns material and continuity
commits under the exact accepted changed set.

## Single-Agent Multi-Role Control Block

Route selected: MULTI_AGENT_MULTI_ROLE. If one runtime happens to perform more
than one named role, authority does not transfer: worker output stays a
candidate, the reviewer evaluates only returned evidence, and source hashes
and machine reconstruction remain controlling. No role-switch claim is proof.

| Control | Binding |
|---|---|
| role separation ledger | operator authorizes; dispatcher scopes; worker edits/returns; reviewer evaluates/commits |
| self-review boundary | worker self-check is not independent acceptance and cannot ratify the oracle |
| escalation conditions | source contradiction, semantic change, or third-path need stops to operator |
| gate sequence | pre-dispatch -> pre-implementation -> worker-return fast gate -> reviewer/closure gate |

## Dual Agent Surface Matrix

| Surface | Status | Authority boundary |
|---|---|---|
| INTERNAL_AGENT | AUTHORIZED | exact two-path local no-commit worker |
| EXTERNAL_AGENT_CLI_MCP | FORBIDDEN | no external invocation or quota use |
| adapter boundary | NOT_APPLICABLE_WITH_REASON | no adapter is used |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> dispatcher -> bounded no-commit correction worker -> reviewer/closer |
| phase | R1A-R2 oracle correction candidate pending reviewer ratification |
| baseHeadFor(phase) | dispatchBaseHead=`184a290e9729b0a196db156d83375ae080bb6930`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly one modified oracle and one new worker return |
| traceScope(phase, actor) | initial/final status, nine hashes, 19 ranges/digests, semantic preservation, gates and no-commit evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no P2, rejected R1B, checker, standard, session, downstream or P4 edit; worktree must be clean before worker start |
| Before status evidence | clean worktree at captured execution base before any worker edit |
| nextMoveSurfaces | reviewer adjudicates R1A-R2; accepted committed identity permits R1B-R2 authoring without another operator micro-checkpoint |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_COMPLETION_2026-09-02.md`

reviewerOwnedClosurePaths: corrected oracle, worker return, conventional
completion review above when needed, and separate post-material continuity
surfaces.

closureOwner: reviewer/closer.

workerCommitPermission: FORBIDDEN.

Reviewer may accept and commit only after independently sampling/recomputing
the machine reconstruction, checking C02/C06 and verifying the full automated
19-case reconciliation. Reviewer does not repeat the worker's manual source
selection. If accepted, record the corrected oracle raw/JCS/required-set
identities and containing commit for R1B-R2. Otherwise retain
`RETURN_TO_DESIGN`. No P4 execution opens here.

## Worker Output Checker Read-Ahead Mandate

Before writing the return, read the worker-return quality, structural,
operation-trace, Delta claim-boundary, Core Guard and review-cost checker
sources. Use the wrapper gate; do not substitute selected individual checks.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain Purpose; Target / Source; Scope / Methodology;
Findings / Position; Risk / Corrective Action; Decision / Disposition; Core
Guard Self-Protection Authorization; Checker Source Read-Ahead Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; Rework
Convergence Self-Proof; Conditional Controls Disposition; Public Export
Disposition; No-Commit Statement; status evidence; and Claim Boundary.

## Review Gate

Routine review occurs once at worker return. Reviewer checks full automated
reconstruction and a bounded sample including C02/C06, rather than repeating
all range selection. Reviewer cannot modify P2 or open P4 in this tranche.

## Closure Checklist

- [ ] clean execution base and exact two-path diff recorded;
- [ ] nine identities match and all 19 line ranges reconstruct;
- [ ] C02/C06 corrections are source-faithful;
- [ ] normative fields and 19/18/7 sets are unchanged;
- [ ] deterministic double-run and required gates pass;
- [ ] zero provider/live/network calls and no worker commit;
- [ ] reviewer disposition and corrected oracle identities recorded;
- [ ] `successorTrancheOpened: NO` remains exact.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/author |
| Provider or surface | local repository only |
| Session or invocation | MFRP-P3-R1A-R2 dispatch authoring |
| Working directory | repository root |
| Command or tool surface | read-only shell, apply_patch and local governance gates |
| Target paths | paired R1A-R2 baseline and work order |
| Allowed scope source | operator instruction opening R1A-R2 and R1B repair authoring |
| Before status evidence | clean worktree at HEAD `184a290e9729b0a196db156d83375ae080bb6930`; `git status --short` empty |
| After status evidence | exactly two untracked dispatch artifacts |
| Diff evidence | `git status --short`; unstaged/staged name-status checks |
| Approval boundary | dispatch authoring only; worker execution/result not claimed |
| Claim boundary | no oracle edit, R1B execution, P4 or external effect |
| Agent type | dispatcher/author |
| Invocation ID | `mfrp-p3-r1a-r2-dispatch-authoring-2026-09-02` |
| Expected manifest | paired R1A-R2 baseline and work order |
| Actual changed set | paired R1A-R2 baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local oracle evidence correction |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement, acceptance or P4 readiness is claimed |
| receiptEvidence | N/A with reason: dispatch authoring constructs no receipt |
| actionEvidence | N/A with reason: worker correction has not executed |
| invocationBoundary | local filesystem and Python hashing only |
| interceptionBoundary | no lifecycle interception or route activation |
| claimLanguage | correction candidate only |
| forbiddenExpansion | no P2, R1B execution, P4, provider/live/public/deploy/production claim |

## Claim Boundary

This work order authorizes exactly one no-commit static oracle correction. It
does not accept the result, execute/repair R1B, run P4, change route authority,
or claim safety, latency, quota, provider/live, public, deployment, or
production improvement.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; public sync is forbidden.
