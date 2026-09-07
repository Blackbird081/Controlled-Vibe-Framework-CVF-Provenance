# CVF Agent Work Order - DARA-T3 R2 WP-ARCH-003 Historical Replay Repair

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-08

Batch ID: DARA-T3-R2-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR

Dispatch base head: `51f60c33ac1ca8f557a47056ac5589e5d8f5af48`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

externalAgentCliInvocationAuthority: ALLOWED_ONCE_BY_OPERATOR_2026_09_08

## Dispatch Prompt Envelope

Role: bounded external-agent CLI worker repairing the terminally rejected DARA-T3 R1
historical replay.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T3_R2_WP_ARCH_003_HISTORICAL_REPLAY_REPAIR_2026-09-08.md`.

Committed rejection:
`docs/reviews/CVF_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md`
at `c9e3c88e0355491cd2e6bfffda3c04249352a553`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: the operator explicitly reopened DARA-T3 and authorized one
external-agent CLI invocation on 2026-09-08. The five rejected files remain untracked.
Repair them in place. This fresh bounded authority moves same-parent external
usage from 2 to ceiling 3; it does not rewrite the historical R1 authority.

Do-not-misread notes: do not create a sixth worker path, edit committed
authority, implement `WP-ARCH-003`, alter DARA-T4 closure, stage, commit, invoke
another agent/provider, publish, push or deploy.

Required first actions: acknowledge this packet; capture HEAD/status/staging;
read the R1 work order and final rejection plus all five pending files; run the
pre-implementation gate before editing.

Return contract: modify exactly the same five pending paths, leave them
unstaged and uncommitted, and return `COMPLETE_PENDING_REVIEW` only when every
R2 acceptance row passes. Otherwise return `RETURN_TO_DESIGN` or
`BLOCKED_WITH_REASON` with exact evidence.

## Purpose

Resolve the three final R1 findings without recreating already-valid source and
architecture evidence: exercise the real fail-closed usage/ceiling admission
classes, compare both expected class and earliest stop, and create a new valid
pre/post ledger freeze receipt before claiming completion.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

Intake summary: the operator reopened the stopped DARA-T3 lane and authorized
one external-agent CLI correction of the final rejected finding set.

Scope classification: bounded exact-five local replay correction with no
runtime or public effect.

Risk sensitivity: medium governance-evidence risk because an incorrect PASS
could misstate dispatcher-readiness effectiveness.

Selected role route: one external CLI worker owns exact-five repair while a
separate orchestrator/reviewer owns acceptance and commits.

Escalation condition: stop on a new root cause, sixth path, post-freeze
mutation, active-checker edit, or invocation 4.

The external worker owns exact-five repair only; the independent
orchestrator/reviewer remains sole commit owner. This is a reversible local
governance-evidence repair; runtime/live/public/deployment effects are forbidden.

## Authority Chain

1. `ECOSYSTEM/doctrine/`, `ECOSYSTEM/operating-model/`, and `AGENTS.md`.
2. DARA roadmap and architecture-readiness admission standard.
3. R1 final rejection at `c9e3c88e0355491cd2e6bfffda3c04249352a553`.
4. Operator instruction on 2026-09-08 reopening DARA-T3 and authorizing one external-agent CLI call.
5. This committed R2 work order.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY

reviewRoundCount: 2

priorFindingSetDigest: 7ef311ddf7c6a89b7a8296ee0d05676abe08e5e2ebf54fcc0c05f325017ec412

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: DARA-T3-R2-01,DARA-T3-R2-02,DARA-T3-R2-03

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 2

externalInvocationCeiling: 3

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY

reworkGeneration: 2

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

This is the only invocation admitted by this reopened boundary. Failure or a
new independent defect stops; no fourth invocation is automatic.

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
    "prior": ["usage-ceiling-fail-closed-not-exercised", "ledger-freeze-proof-absent", "earliest-stop-not-compared"],
    "resolved": [],
    "retained": ["usage-ceiling-fail-closed-not-exercised", "ledger-freeze-proof-absent", "earliest-stop-not-compared"],
    "new": [],
    "reopened": [],
    "current": ["usage-ceiling-fail-closed-not-exercised", "ledger-freeze-proof-absent", "earliest-stop-not-compared"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 2,
    "nonDecreasingBlockerTransitions": 1
  },
  "claims": [{
    "claimId": "DARA-T3-R2-DISPATCH",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/reviews/CVF_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md"
  }],
  "requiredDisposition": "ROOT_CONTRACT_REQUIRED",
  "successorScope": "INTEGRATED_ROOT_CONTRACT"
}
```

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures directly. Stop only for source contradiction,
sixth-path need, post-freeze fixture/ledger mutation, forbidden action, or new
independent semantic defect.

## Agent Roles

| Role | Responsibility | Forbidden overlap |
|---|---|---|
| Operator | opens one R2 CLI invocation | does not author or accept worker evidence |
| Orchestrator/reviewer | invokes CLI, evaluates return, owns commits | does not recreate worker implementation |
| External CLI worker | repairs and verifies exact five paths | no commit, staging, self-acceptance or further agent invocation |

## Required First Reads

1. This work order in full.
2. The R1 final completion review in full.
3. The R1 work order and architecture-readiness admission standard.
4. All five pending artifacts and the imported DARA validator sources.
5. `docs/reference/guard_orientation/README.md` and literal-format gotchas.
6. Worker-return, dispatch-quality, review-cost and structural checker sources.

## Pre-Flight Checks

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git diff --cached --name-only
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 51f60c33ac1ca8f557a47056ac5589e5d8f5af48 --head HEAD
```

Expected: work-order commit descends from the dispatch base, staging is empty,
exactly five prior worker paths are pending, and pre-implementation exits zero.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "DARA-T3-R2-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR",
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
  "pathFamilies": ["docs/work_orders/", "docs/reviews/", "governance/compat/"],
  "claims": ["bounded repair of an offline historical replay"],
  "requiredProof": ["usage-ceiling fail-closed outcomes", "class-and-stop comparison", "fixture-ledger freeze", "exact-five no-commit return"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["active checker edit", "runtime/provider/live effect", "public sync", "deployment", "worker commit"],
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

Allowed worker scope is exactly the five paths in the fulfillment manifest.
All committed paths are read-only to the worker. Temporary hash/probe files
must remain outside the repository.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_EXTERNAL_LOW_RISK_WITH_REASON:OFFLINE_REPAIR_OF_EXACT_FIVE_REPLAY_ARTIFACTS_NO_ACTIVE_GUARD_WIRING

Reason: reversible helper/test/evidence repair with exact paths, existing
owners and stop conditions already frozen by reviewer authority.

## Required Artifact Manifest

| Path | Action | Required proof |
|---|---|---|
| `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json` | MODIFY | real usage/ceiling stimuli and frozen sources |
| `governance/compat/dara_t3_historical_replay.py` | MODIFY | full expected/actual comparison through accepted owners |
| `governance/compat/test_dara_t3_historical_replay.py` | MODIFY | three finding regressions |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md` | MODIFY | finalized R2 truth before freeze |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md` | MODIFY | R2 evidence and terminal return |

## Work-Order Fulfillment Manifest

| Path | Action | Required proof |
|---|---|---|
| `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json` | MODIFY | usage and ceiling are actual admission-stage inputs |
| `governance/compat/dara_t3_historical_replay.py` | MODIFY | `matched` requires both class and earliest-stop equality |
| `governance/compat/test_dara_t3_historical_replay.py` | MODIFY | earliest-stop inversion and real fail-closed cases |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md` | MODIFY | final content before first R2 replay; never edited afterward |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md` | MODIFY | external pre/post hashes and exact command receipts |

## Write Ownership

The external worker owns only the five manifest paths. The orchestrator owns this work order, later
review/closure, commits and continuity. No other path may change.

## R2 Repair Requirements

### R2-01 - real usage and ceiling fail-closed classes

- Unknown usage must exercise the existing review-cost/quota admission owner
  and observe `BLOCKED_USAGE_UNKNOWN` before invocation.
- Reached ceiling must exercise the existing convergence/quota owner and
  observe `BLOCKED_INVOCATION_CEILING_REACHED` before invocation.
- Do not encode either result as an architecture declaration or duplicate the
  owning admission semantics in the helper.
- Unclassified architecture applicability remains a separate case.

### R2-02 - fresh ledger freeze proof

- Finish all fixture and ledger edits before the first R2 replay.
- Capture external SHA-256 values for both immediately before replay.
- After that capture, never edit fixture or ledger.
- Run two replay commands, focused tests and fast gate; capture both hashes
  again and record the equal pairs only in the worker return.
- Any post-freeze fixture/ledger edit returns `RETURN_TO_DESIGN`.

### R2-03 - conjunctive matching

- A seeded case matches only when both `expectedViolationClass` and
  `expectedEarliestStop` equal independently observed values.
- Add a regression that changes only expected earliest stop, confirms actual
  is unchanged, and requires mismatch/error accounting plus non-success.

## Acceptance Matrix

| ID | Probe | Required result |
|---|---|---|
| R2-A01 | seven frozen sources | 7/7 hashes match |
| R2-A02 | unknown usage | real owner emits `BLOCKED_USAGE_UNKNOWN` before invocation |
| R2-A03 | exhausted ceiling | real owner emits `BLOCKED_INVOCATION_CEILING_REACHED` before invocation |
| R2-A04 | unclassified applicability | remains distinct and fail-closed |
| R2-A05 | earliest-stop inversion | actual unchanged; `matched=false`; error increases; terminal non-success |
| R2-A06 | class inversion | actual unchanged; `matched=false`; error increases |
| R2-A07 | all prior valid cases | remain input-sensitive and reconciled |
| R2-A08 | clean control | no false positive |
| R2-A09 | freeze | fixture and ledger pre/post hashes are byte-identical |
| R2-A10 | determinism | two normalized clean outputs are byte-identical |
| R2-A11 | commands | focused tests, replay and fast gate pass; negative probes fail as expected |
| R2-A12 | scope/quota | exact five, empty staging, no worker commit, external usage 3/3 |

All rows are conjunctive.

## Execution Plan

1. Capture identity/status and run pre-implementation.
2. Repair helper, tests, fixture, then finalize ledger.
3. Capture fixture/ledger pre-hashes outside the repository and freeze both.
4. Run two clean replays, tests, negative probes and fast gate.
5. Capture post-hashes; update only worker return; verify exact scope/staging.

## Review Gate

The reviewer will inspect the five-path diff, consume receipts, sample usage, ceiling,
earliest-stop and freeze evidence, then rerun focused/fast checks. It will not
recreate the implementation.

## Return-To-Orchestrator Conditions

- `COMPLETE_PENDING_REVIEW`: R2-A01 through R2-A12 all pass.
- `RETURN_TO_DESIGN`: any zero-tolerance miss, post-freeze mutation or nondeterminism.
- `BLOCKED_WITH_REASON`: source drift, forbidden-path need or non-remediable gate failure.

## Operator Checkpoint

No routine pause inside exact-five scope. Stop before another external call,
scope expansion, provider/live action, public sync, deployment or destructive action.

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

Also run explicit negative probes for malformed input, source drift, class
inversion, earliest-stop inversion and zero-tolerance miss; expected nonzero
exits must be recorded separately from mandatory clean PASS commands.

## Evidence Requirements

Return command/exit evidence, source hashes, independently observed per-case
class and stop, reconciled metrics, negative probes, two-run identity,
fixture/ledger pre/post hash pairs, exact-five status, empty staging,
externalAgentInvocationCount 3 and providerCallCount 0 inside the worker.

## Acceptance Criteria

`COMPLETE_PENDING_REVIEW` is allowed only when all R2 acceptance rows and clean
commands pass, negative probes fail as expected, exact scope is preserved and
fixture/ledger remain unchanged after pre-hash. Otherwise use the bounded stop.

## Reviewer Non-Duplication Contract

Reviewer consumes valid returned evidence and performs only decision-changing
samples plus focused/fast gates unless a named contradiction justifies more.

## Worker Return Packet Shape Contract

Update the existing worker return in place and preserve prior rejection history.
Add an R2 section with packet identity, execution HEAD, all twelve rows,
commands, fresh freeze hashes, exact scope and terminal status.

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_dara_t3_historical_replay.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

workerReturnRequiredCommands: exact command and exit-code record

workerReturnChangedFiles: exact five-path table

workerReturnClaimBoundary: no DARA-T3 acceptance or successor authority

## Commit Mode And Base-Anchor Lifecycle

Worker must not stage or commit. The reviewer may commit worker material only after an
independent PASS review. The dispatch base remains the operator checkpoint;
worker captures the later committed work-order HEAD as execution base.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | orchestrator/reviewer -> external CLI worker -> reviewer/closer |
| phase | R2 repair dispatch and pending return |
| baseHeadFor(phase) | dispatchBaseHead=51f60c33ac1ca8f557a47056ac5589e5d8f5af48; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact five pending worker paths |
| traceScope(phase, actor) | one external-agent CLI invocation and local exact-five commands |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | DARA-T4 closure and all unrelated work remain untouched |
| nextMoveSurfaces | reviewer completion and continuity are reviewer-owned after PASS only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | reviewer will create a versioned DARA-T3 R2 completion review |
| reviewerOwnedClosurePaths | completion review, DARA roadmap and continuity only if verdict requires updates |
| closureOwner | orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| three final R1 findings and no automatic third call | governed review evidence | `docs/reviews/CVF_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md` | Findings / Position; Risk / Corrective Action | `docs/reviews/CVF_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md` | DARA-T3 reviewer authority | ACCEPT |
| original conjunctive R1 acceptance rows | governed work-order contract | `docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_REPAIR_2026-09-07.md` | R1 Repair Requirements; Hostile Test And Acceptance Matrix | `docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T3_R1_WP_ARCH_003_HISTORICAL_REPLAY_REPAIR_2026-09-07.md` | DARA-T3 dispatch authority | ACCEPT |
| architecture admission and quota classes use existing owners | canonical contract | `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | Quota And Admission Progression | `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | architecture-readiness admission standard | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: this packet authorizes an offline helper/test/evidence repair
and makes no runtime, provider or deployment behavior claim.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| R2 path existence | `Test-Path` returned False before authoring | PASS |
| R2 token collision | `rg -n` across `docs` and `CVF_SESSION` returned no match before authoring | PASS |
| Collision decision | one new versioned work order; same five worker outputs intentionally reused | PASS |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-readiness historical replay repair`,
role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, rework convergence scalars, source columns, exact manifests, no-commit return, trace fields and private export disposition |
| gateRunPurpose | confirm R2 authority shape and worker-return contract before dispatch |
| claimBoundary | checker conformance does not prove repaired replay effectiveness |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id DARA-T3-R2-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR --title "DARA T3 R2 WP-ARCH-003 Historical Replay Repair" --date 2026-09-08 --base 51f60c33ac1ca8f557a47056ac5589e5d8f5af48 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind REWORK --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 2 --root-cause-cluster-id DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY --prior-finding-set-digest 7ef311ddf7c6a89b7a8296ee0d05676abe08e5e2ebf54fcc0c05f325017ec412 --cumulative-external-invocation-count 2 --external-invocation-ceiling 3 --new-independent-critical-evidence DARA-T3-R2-01,DARA-T3-R2-02,DARA-T3-R2-03 --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit external REWORK profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bound operator reopening, exact-five scope, three rejected findings, one CLI call and fresh freeze sequence |
| checkerReadAheadConfirmation | dispatch, convergence, source, worker-return, trace and public guards read |
| docOnlyNewFields | `externalAgentCliInvocationAuthority` records this operator-approved CLI boundary only |
| claimBoundary | dispatch provenance only; no repair-success claim |

## Evidence Reuse And Encoding Plan

Reuse the seven frozen source identities and already-valid matrix evidence.
Write UTF-8 text, preserve prior rejection history, and add only R2 evidence.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | committed R2 work order -> external CLI exact-five return -> independent review |
| Matching local-view guard | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py` |
| Owner surface | DARA roadmap, this work order and later completion review |
| Disposition | worker output is evidence input pending independent acceptance |
| Claim boundary | external output is not CVF authority or self-acceptance |

## Legacy Absorption Coverage Index Disposition

N/A with reason: no legacy absorption or knowledge-map completeness claim.

## Foundation Storage Layout Block

N/A with reason: exact-five repair does not create or move foundation storage.

## Core Guard Self-Protection Authorization

No active checker, hook or governance catalog edit is authorized. The helper
and focused test are inactive historical replay surfaces only.

## Closure Checklist

- [x] Operator reopened DARA-T3 and allowed one external-agent CLI invocation.
- [x] Three final findings are consolidated into one repair.
- [x] Exact-five write scope and no-commit ownership are explicit.
- [x] Usage count 2 and ceiling 3 are known before dispatch.
- [x] Fresh freeze sequence is executable without self-reference.
- [x] Provider/live/public/deployment actions remain forbidden.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/dispatcher |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T3 R2 dispatch, 2026-09-08 |
| Working directory | repository root |
| Command or tool surface | governed reads, Git status/history, ADIF resolver, scaffold stdout and patch authoring |
| Target paths | this R2 work order only before worker execution |
| Allowed scope source | operator instruction reopening DARA-T3 and allowing one external-agent CLI call |
| Before status evidence | clean worktree for the orchestrator-owned dispatch path; HEAD `51f60c33ac1ca8f557a47056ac5589e5d8f5af48`; exactly five declared worker paths remain untracked and isolated |
| After status evidence | this work order plus the same five untracked worker files; staging controlled by orchestrator |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | one external CLI invocation after committed pre-dispatch authority |
| Claim boundary | dispatch only; no worker success or DARA-T3 acceptance |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `dara-t3-r2-dispatch-2026-09-08` |
| Expected manifest | this work order only for dispatch commit |
| Actual changed set | this work order only for dispatch commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair dispatch with no public-sync authority.

## Claim Boundary

This packet authorizes exactly one external-agent CLI repair invocation over the five
pending DARA-T3 artifacts and independent reviewer evaluation. It does not accept the
current replay, implement `WP-ARCH-003`, reverse DARA-T4 closure, authorize a
fourth external call, permit a worker commit, invoke a downstream provider/live
service, expose credentials, publish, deploy, push or claim production readiness.
