# CVF Agent Work Order - DARA-T3 R1 WP-ARCH-003 Historical Replay Repair

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-07

Batch ID: DARA-T3-R1-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR

Dispatch base head: `537dad6ce752f75d6dc2e36e272639758e7ca829`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: bounded external worker repairing the rejected DARA-T3 historical replay.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_REPAIR_2026-09-07.md`.

Paired baseline:
`docs/baselines/CVF_GC018_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_REPAIR_2026-09-07.md`.

Committed rejection:
`docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md`
at `537dad6ce752f75d6dc2e36e272639758e7ca829`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: the five rejected worker files are already present
untracked. Repair those files in place. This is rework round 1 of the same
parent assignment, moving external usage from 1 to ceiling 2. The operator
manually relays this packet; Codex does not invoke Claude/CLI/MCP.

Do-not-misread notes: do not restart from zero, create a sixth path, edit the
committed review/baseline/work order, alter an active DARA checker, implement
`WP-ARCH-003`, open DARA-T4, stage, commit, call a provider, publish or deploy.

Required first actions: acknowledge authority; capture full HEAD and status;
confirm the dispatch base is an ancestor; read this packet, paired baseline,
committed rejection, original packet, all five pending files and the existing
DARA validator sources; run pre-implementation before editing.

Return contract: update the existing ledger and worker return in place, leave
all five files uncommitted and unstaged, and return `COMPLETE_PENDING_REVIEW`
only when every R1 acceptance item and mandatory command passes. Otherwise
return `RETURN_TO_DESIGN` or `BLOCKED_WITH_REASON` with exact evidence.

## Purpose

Repair the three consolidated reviewer findings without recreating the entire
historical replay. Preserve valid source/hash/raw-case work, replace seeded
expected-to-actual copying with genuine accepted-oracle evaluation, make
metrics input-sensitive, and prove fixture/ledger freeze identity.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

Intake summary: operator request to prepare one Claude worker packet after a
Codex rejection of the first DARA-T3 return.

Scope classification: bounded exact-five local replay correction with no
runtime or public effect.

Risk sensitivity: medium governance-evidence risk because a false PASS could
open later readiness work; provider/live/secret/production effects remain
forbidden.

Selected role route: the committed Codex review supplies immutable findings,
one external worker acts through operator manual relay, and Codex later reviews
evidence without recreating implementation.

Escalation condition: stop on a new root cause, sixth path, active-checker edit,
post-freeze mutation or invocation 3.

## Authority Chain

1. `ECOSYSTEM/doctrine/` and `ECOSYSTEM/operating-model/`.
2. `AGENTS.md`, active continuity surfaces and current review-cost rules.
3. DARA roadmap and architecture-readiness admission standard.
4. Committed DARA-T3 rejection at `537dad6ce752f75d6dc2e36e272639758e7ca829`.
5. Paired R1 GC-018 baseline and this work order.
6. Operator instruction on 2026-09-07 authorizing manual relay to Claude.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY

reviewRoundCount: 1

priorFindingSetDigest: 88aabb6fcc1043945efde94d0010f67c508bf0fdffc883ace2406a9ad260b63d

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: DARA-T3-R1-01,DARA-T3-R1-02,DARA-T3-R1-03

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 1

externalInvocationCeiling: 2

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

This is the final admitted external repair for this parent. A new independent
defect, forbidden-path need or non-passing final packet stops; no third
invocation is automatic.

## Semantic Convergence Outcome

Standard:
`docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "dara-t3-wp-arch-003-historical-replay",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": ["seeded-replay-tautological", "error-accounting-not-measured", "ledger-freeze-proof-missing"],
    "resolved": [],
    "retained": ["seeded-replay-tautological", "error-accounting-not-measured", "ledger-freeze-proof-missing"],
    "new": [],
    "reopened": [],
    "current": ["seeded-replay-tautological", "error-accounting-not-measured", "ledger-freeze-proof-missing"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 1,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "DARA-T3-R1-DISPATCH",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The R1 return is ordinal 2 and may resolve the blockers only with executable,
input-sensitive proof. No successor opens automatically.

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for reads, local provider-free commands,
and repairs inside the exact five paths. Repair allowed-scope test/gate defects
and rerun them. Stop only for source drift, a sixth path, an active-checker edit,
post-freeze fixture/ledger edit, forbidden external action or a new independent
semantic defect.

## Agent Roles

| Role | Responsibility | Forbidden overlap |
|---|---|---|
| Operator | manually relay the committed packet and returned status | does not author or accept evidence |
| External worker | repair and verify exactly five pending paths | no commit, staging, self-acceptance or authority edit |
| Orchestrator/reviewer/closer | evaluate returned evidence and own any later commit | does not recreate implementation or invoke Claude |

## Required First Reads

1. This work order and paired R1 baseline in full.
2. The committed DARA-T3 completion review in full.
3. Original DARA-T3 baseline/work order and all seven frozen sources.
4. All five pending worker artifacts before editing.
5. `docs/reference/guard_orientation/README.md` and literal-format gotchas.
6. `governance/compat/check_work_order_dispatch_quality_range.py`,
   `check_work_order_dispatch_quality_source.py`, and
   `check_work_order_dispatch_quality_architecture_schema.py`.

## Pre-Flight Checks

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git merge-base --is-ancestor 537dad6ce752f75d6dc2e36e272639758e7ca829 HEAD
git diff --cached --name-only
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 537dad6ce752f75d6dc2e36e272639758e7ca829 --head HEAD
```

Expected: dispatch base is an ancestor; staging is empty; only the five prior
worker paths are pending before edits; pre-implementation exits zero.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "DARA-T3-R1-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["AGENT_HANDOFF_V59_2026-08-11.md", "CVF_SESSION/", "CVF_SESSION_MEMORY.md", "docs/baselines/", "docs/work_orders/", "docs/reviews/", "governance/compat/"],
  "claims": ["bounded repair of an offline historical replay"],
  "requiredProof": ["accepted-oracle observed results", "input-sensitive metrics", "fixture-ledger freeze", "exact-five no-commit return"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["active checker edit", "runtime or provider effect", "public sync", "deployment", "worker commit"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named source set; no corpus-completeness claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, `P3_ELEVATED`, selective execution false and
`RUN_FULL_LEGACY_BUNDLE`.

## Scope / Target / Owner Boundary

Allowed scope is exactly the five paths in the fulfillment manifest. Imports
from existing DARA modules are read-only. Temporary replay/hash captures must
remain outside the repository and be deleted or retained outside Git according
to the worker environment; they are not a sixth repository path.

Forbidden: any change to committed review, baseline, work order, roadmap,
session, checker, hook, historical source, `WP-ARCH-003`, runtime, provider,
public or deployment surfaces.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_EXTERNAL_LOW_RISK_WITH_REASON:OFFLINE_REPAIR_OF_EXACT_FIVE_REPLAY_ARTIFACTS_NO_ACTIVE_GUARD_WIRING

Reason: reversible provider-free helper/test/evidence repair with owners,
paths, source identities and stop conditions frozen by reviewer authority.

## Required Artifact Manifest

| Path | Action | Required proof |
|---|---|---|
| `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json` | MODIFY | structured seeded stimuli; frozen source identities retained |
| `governance/compat/dara_t3_historical_replay.py` | MODIFY | accepted-oracle execution and measured metrics |
| `governance/compat/test_dara_t3_historical_replay.py` | MODIFY | hostile input-sensitivity and CLI tests |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md` | MODIFY | R1 reconciliation and truthful freeze method |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md` | MODIFY | R1 evidence and pending status |

## Work-Order Fulfillment Manifest

| Path | Action | Required proof |
|---|---|---|
| `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json` | MODIFY | structured `oracleInput` for every seeded case; seven source hashes and raw identities preserved |
| `governance/compat/dara_t3_historical_replay.py` | MODIFY | accepted-oracle observed results; derived metrics; meaningful CLI exit codes |
| `governance/compat/test_dara_t3_historical_replay.py` | MODIFY | metamorphic sensitivity, clean control, metric and exit-code tests |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md` | MODIFY | append R1 section; preserve rejected history; no self-hash |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md` | MODIFY | append/reconcile R1 evidence and final pending status |

Forbidden paths: every repository path not listed above.

## Write Ownership

Worker write ownership is exactly the five manifest paths. The worker may read
accepted validators and sources but may not edit them. Reviewer-owned closure,
work-order status, roadmap and continuity paths are excluded from worker writes.

## R1 Repair Requirements

### R1-01 - real seeded oracle evaluation

- Add structured defect-bearing input for all ten named seeded families.
- Actual output must be derived without reading any `expected*`, case-label,
  `sourceFinding` or `note` field.
- Prefer calling
  `check_work_order_dispatch_quality_range._validate_architecture_readiness_admission`
  on deterministic synthetic work-order text rendered from `oracleInput`.
- Do not duplicate architecture-validation semantics in the replay helper.
- Map observed issue tokens to the frozen earliest-stop/violation taxonomy in
  one explicit, tested adapter.

### R1-02 - measured error accounting

- `matched` compares independently observed and expected results.
- False negatives count defect cases for which the required block is absent or
  wrong; false positives count clean controls that are blocked.
- Add at least one clean passing control stimulus.
- Zero-tolerance recall is observed caught count divided by required cases,
  with both numerator and denominator in JSON.
- Removing, neutralizing or misrouting each sampled defect changes output and
  causes the expected test failure or terminal `RETURN_TO_DESIGN`.
- No result metric may be a constant merely initialized to the claimed value.

### R1-03 - byte freeze proof

- Complete all fixture and ledger edits before the first R1 replay.
- Capture SHA-256 for fixture and ledger externally immediately before replay.
- Run replay twice, tests and gates without editing either frozen file.
- Capture both hashes again and record pre/post equality in the worker return.
- Do not embed a ledger hash inside the ledger itself.
- Any need to change fixture or ledger after first replay returns
  `RETURN_TO_DESIGN`; do not tune and rerun.

### R1-04 - command truth

- CLI returns zero only for `REPLAY_BLOCKS_AVOIDABLE_INVOCATIONS`.
- CLI returns nonzero for source drift, malformed input and
  `RETURN_TO_DESIGN`.
- Worker return distinguishes expected nonzero negative-test subprocesses from
  mandatory clean-command PASS.

## Hostile Test And Acceptance Matrix

| ID | Probe | Required result |
|---|---|---|
| R1-A01 | preserve frozen sources | 7/7 source hashes match |
| R1-A02 | raw Initial/R1/R2 | three independently observed pre-invocation stops |
| R1-A03 | remove all seeded prose only | observed seeded results unchanged |
| R1-A04 | neutralize defect-bearing stimulus | observed result changes; stale expected claim cannot pass |
| R1-A05 | invert expected label only | actual stays fixed and mismatch/error count increases |
| R1-A06 | duplicate owner stimulus | existing DARA validator emits duplicate-owner issue |
| R1-A07 | missing registration/runtime/trust/placeholder/rollback stimuli | each emits its own accepted issue class |
| R1-A08 | self-authored review, unknown usage, exhausted ceiling, unclassified applicability | each emits its accepted fail-closed issue class |
| R1-A09 | clean control | no architecture issue and no false positive |
| R1-A10 | metric aggregation | observed per-case rows reconcile exactly with totals and recall fraction |
| R1-A11 | freeze | fixture and ledger pre/post hashes are byte-identical |
| R1-A12 | determinism | two normalized clean outputs are byte-identical |
| R1-A13 | scope | exact five paths, empty staging, no commit |
| R1-A14 | quota | external assignment becomes 2/2; providerCallCount remains 0 |

All rows are conjunctive.

## Execution Plan

1. Capture execution identity, status and pre-implementation gate.
2. Read and preserve valid initial evidence; design structured oracle inputs.
3. Repair helper and tests, then complete fixture and ledger before freeze.
4. Capture external pre-replay hashes and freeze fixture/ledger.
5. Run focused tests, two clean replays, hostile probes and fast gate.
6. Capture post-replay hashes, update only the worker return, and verify scope.

## Review Gate

Return to the independent reviewer at the first terminal status. The reviewer
will inspect the exact-five diff, validate freeze receipts, sample four
decision-changing cases and rerun only focused/fast checks unless a named
contradiction justifies more.

## Return-To-Orchestrator Conditions

- `COMPLETE_PENDING_REVIEW`: every R1-A01 through R1-A14 item passes.
- `RETURN_TO_DESIGN`: any zero-tolerance miss, post-freeze edit,
  nondeterminism or unrepresentable real-oracle case.
- `BLOCKED_WITH_REASON`: source drift, forbidden-path need or non-remediable
  required-gate failure.

## Operator Checkpoint

No routine pause is required inside the exact-five assignment. Stop for fresh
direction only if another external invocation, expanded authority,
provider/live action, public sync, deployment or destructive action would be
required.

## Verification Commands

```powershell
python -m pytest governance/compat/test_dara_t3_historical_replay.py -q
python governance/compat/dara_t3_historical_replay.py --fixture governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json --json
python governance/compat/dara_t3_historical_replay.py --fixture governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json --json
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_dara_t3_historical_replay.py
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

The worker must also run explicit negative CLI probes for malformed input,
source drift and a zero-tolerance miss and record their expected nonzero exits.

## Evidence Requirements

Return command/exit evidence, 7/7 source hashes, per-case expected and observed
oracle results, issue tokens, reconciled error totals, recall numerator and
denominator, clean control, two-run byte identity, fixture/ledger pre/post hash
receipt, exact changed paths, empty staging and providerCallCount 0.

## Acceptance Criteria

`COMPLETE_PENDING_REVIEW` is allowed only when R1-A01 through R1-A14 pass, all
mandatory clean commands exit zero, negative probes fail as expected, exact
scope is preserved, and no fixture/ledger edit occurs after the first R1
replay. A zero-tolerance miss, nondeterminism or post-freeze change returns
`RETURN_TO_DESIGN`. Source drift, forbidden-path need or gate failure outside
allowed remediation returns `BLOCKED_WITH_REASON`.

## Reviewer Non-Duplication Contract

The reviewer will consume valid evidence, inspect the five-path diff, sample
one matrix, semantic, quota and clean-control stimulus, and rerun focused/fast
checks. Do not ask the reviewer to rebuild all fixtures or repeat every case.

## Worker Return Packet Shape Contract

Update the existing worker return in place. Preserve the initial execution and
rejection history. Add an R1 section containing this packet identity, captured
execution HEAD, all fourteen acceptance rows, command evidence, pre/post freeze
hashes, changed-file proof, providerCallCount 0 and one allowed terminal status.
Do not create a reviewer completion artifact or self-accept.

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_dara_t3_historical_replay.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

workerReturnRequiredCommands: exact command and exit-code record

workerReturnChangedFiles: exact five-path table

workerReturnClaimBoundary: no DARA-T3 acceptance until independent review

## Commit Mode And Base-Anchor Lifecycle

- `dispatchBaseHead`: `537dad6ce752f75d6dc2e36e272639758e7ca829`.
- `executionBaseHead`: capture at worker start.
- Worker must not stage or commit.
- `closureBaseHead`: reviewer captures only after acceptance.
- Do not use the original dispatch base as closure evidence.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator manual relay -> external worker -> orchestrator/reviewer -> closer |
| phase | DARA-T3 R1 historical replay repair |
| baseHeadFor(phase) | dispatchBaseHead=`537dad6ce752f75d6dc2e36e272639758e7ca829`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact five worker paths only |
| traceScope(phase, actor) | worker records commands/diff; reviewer records focused evidence evaluation and commit range |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns commits |
| crossBatchIsolation | clean worktree Before status evidence exists at initial execution base `b23f0b7db8b24993f999ba38d9f445b89a06fa76`; R1 intentionally inherits only the exact five pending paths and no unrelated changes |
| nextMoveSurfaces | R1 worker return, then reviewer-owned closure/roadmap/session surfaces only after acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md` |
| reviewerOwnedClosurePaths | completion review; DARA roadmap and this work order terminal metadata only after acceptance; session continuity in a separate batch |
| closureOwner | orchestrator/reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| initial rejection | committed reviewer authority | `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md` | Findings / Decision | DARA-T3-R1-01 through R1-03 | DARA reviewer | ACCEPT |
| executable admission oracle | current checker source | `governance/compat/check_work_order_dispatch_quality_range.py` | architecture-readiness validation | `_validate_architecture_readiness_admission` | work-order dispatch-quality gate | ACCEPT |
| matrix row validation | current checker source | `governance/compat/check_work_order_dispatch_quality_source.py` | architecture matrix validation | `_validate_architecture_matrix_row_identity` | DARA source validator | ACCEPT |
| immutable review binding | current checker source | `governance/compat/check_work_order_dispatch_quality_architecture_schema.py` | immutable review identity | `_validate_immutable_review_identity_fields` | DARA schema helper | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | provider-free offline replay repair; no runtime behavior is claimed |

## Negative Search And Collision Discipline

The exact five paths already exist only as the rejected untracked worker
candidate. No alternative DARA-T3 R1 helper, fixture, ledger, return or test
owner is authorized. Disposition: `NO_NEW_OWNER_COLLISION`; edit in place.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-readiness historical replay repair`,
role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | dispatch envelope, REWORK fields, source rows, architecture declaration, no-commit profile, exact manifest, trace and private export |
| gateRunPurpose | confirm the complete R1 worker packet before manual relay |
| claimBoundary | checker conformance cannot prove the repaired replay |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id DARA-T3-R1-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR --title "DARA T3 R1 WP-ARCH-003 Historical Replay Repair" --date 2026-09-07 --base 537dad6ce752f75d6dc2e36e272639758e7ca829 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind REWORK --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 1 --root-cause-cluster-id DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY --prior-finding-set-digest 88aabb6fcc1043945efde94d0010f67c508bf0fdffc883ace2406a9ad260b63d --cumulative-external-invocation-count 1 --external-invocation-ceiling 2 --new-independent-critical-evidence DARA-T3-R1-01,DARA-T3-R1-02,DARA-T3-R1-03 --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit external REWORK profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bound rejection, exact-five repair, real-oracle stimuli, hostile tests, freeze receipts and final-invocation stop |
| checkerReadAheadConfirmation | dispatch, source, architecture, convergence, return, trace and protected-path guards read |
| docOnlyNewFields | `oracleInput`, `observedIssueTokens`, recall numerator/denominator and freeze receipt fields |
| claimBoundary | dispatch provenance only; no implementation or replay-success claim |

## Evidence Reuse And Encoding Plan

Reuse mode: `REUSE_WITH_FRESHNESS_CHECK`.

Retain the seven frozen source hashes and three raw cases after recomputation;
do not re-author them. Replace only invalid seeded stimulus/result logic and
freeze evidence. Agent-authored prose/code defaults to ASCII; existing source
names and required literals may be preserved verbatim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent packet request |
| Chain map route | committed rejection -> bounded rework packet -> operator manual relay -> external return -> independent local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_review_cost_control.py` |
| Owner surface | DARA roadmap, paired R1 baseline, this work order and committed review |
| Disposition | `PACKET_READY` after pre-dispatch and pre-commit gates pass |
| Claim boundary | manual relay does not make worker output canonical or accepted |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded repair of five new DARA-T3 artifacts; no
legacy source family, copied repository or prior corpus is being absorbed.

## Foundation Storage Layout Block

The existing `governance/compat/fixtures/`, `governance/compat/` and
`docs/reviews/` owners remain unchanged. No new folder, registry, index,
runtime owner or parallel replay surface is created.

## Core Guard Self-Protection Authorization

Protected paths:

- `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json`
- `governance/compat/dara_t3_historical_replay.py`
- `governance/compat/test_dara_t3_historical_replay.py`
- `AGENT_HANDOFF_V59_2026-08-11.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/entries/daraT3R1WpArch003HistoricalReplayRepairDispatch20260907.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: 2026-09-07 instruction directing Codex to act as
orchestrator/reviewer and prepare a packet for manual relay to Claude.

Authorized guard-maintenance scope: repair only the new offline replay candidate; no edit to
active `check_*.py` guards, hook catalogs, dispatch behavior or session state.
The six continuity paths above are orchestrator-only dispatch synchronization
paths and remain forbidden to the worker.

Rollback boundary: revert/remove only the exact five worker files after
reviewer disposition. Worker must not execute rollback.

## Closure Checklist

- [ ] Exact five paths and no other worker changes.
- [ ] Seven source hashes match.
- [ ] R1-A01 through R1-A14 reconcile truthfully.
- [ ] Fixture and ledger pre/post hashes are byte-identical.
- [ ] Required clean commands pass and negative CLI probes fail as expected.
- [ ] Staging is empty and worker made no commit.
- [ ] Return uses one allowed pending/stop status and does not self-accept.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/reviewer |
| Provider or surface | local private CVF workspace; operator-owned manual relay later |
| Session or invocation | DARA-T3 R1 dispatch authoring, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | governed reads, Git, ADIF resolver, scaffold helper, apply_patch and pre-dispatch gates |
| Target paths | paired R1 baseline and this work order |
| Allowed scope source | operator instruction plus committed DARA-T3 rejection |
| Before status evidence | clean worktree at initial execution base `b23f0b7db8b24993f999ba38d9f445b89a06fa76`; current review commit `537dad6ce752f75d6dc2e36e272639758e7ca829` intentionally retains exactly five rejected untracked paths |
| After status evidence | two dispatch artifacts added; rejected worker bytes unchanged during authoring |
| Diff evidence | exact dispatch-doc staging and Git status before commit |
| Approval boundary | one same-parent R1 external repair, count 1 to ceiling 2 |
| Claim boundary | no Claude invocation by Codex, worker edit, acceptance, DARA-T4 or external effect |
| Agent type | orchestrator/reviewer |
| Invocation ID | `dara-t3-r1-dispatch-authoring-2026-09-07` |
| Expected manifest | paired R1 baseline and this work order |
| Actual changed set | same two dispatch paths in material commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker dispatch; no public-sync authority.

## Claim Boundary

This packet authorizes one final same-parent R1 repair of exactly five pending
DARA-T3 artifacts through operator manual relay. It does not accept the
current replay, implement `WP-ARCH-003`, open DARA-T4, permit a third external
invocation, let Codex call Claude/CLI/MCP, run provider/live behavior, expose
credentials, publish, deploy, push or claim production readiness.
