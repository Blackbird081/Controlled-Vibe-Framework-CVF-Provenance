# CVF Agent Work Order - EACQ-FV EV-2 Capsule Effectiveness Evidence Reconciliation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Amendment: 1 - post-dispatch roadmap pin correction

Batch ID: EACQ-FV-EV2

Date: 2026-08-28

Dispatch base head: `51fe7edddfa591f15c29d57d79c0da5d37737835`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated evidence worker

Reviewer/closer: designated internal reviewer

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_WORKER_RETURN_2026-08-28.md`

## Dispatch Prompt Envelope

Role: delegated evidence worker for EACQ-FV-EV2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_2026-08-28.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: evidence is pinned at the 2026-08-28 dispatch base.

Do-not-misread notes: this is evidence reconciliation, not a request to prove uplift, modify capsule machinery, or execute UAA/provider work.

Required first actions: read startup surfaces, guard orientation, literal gotchas, paired baseline, task capsule, all pinned evidence, and checker sources before writing.

Return contract: create exactly two worker-owned artifacts, run required gates, leave both unstaged and uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Build a traceable comparison of the three capsule-governed EACQ-FV tranches
and determine the strongest conclusion supported today. Preserve missing data
and comparability limits rather than filling them by inference.

## Authority Chain

Operator continuation -> fresh four-part value gate -> EACQ-FV roadmap
comparison requirement -> paired EV-2 GC-018 baseline -> this no-commit work
order -> independent reviewer/closer. No worker output is self-authoritative.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| operator | authorizes the bounded EV-2 lane |
| dispatcher | pins sources and defines the exact evidence contract |
| worker | creates exactly two unstaged documents and returns evidence |
| reviewer/closer | independently verifies, repairs within scope, accepts or rejects, and owns commits |

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md`
3. `AGENT_HANDOFF_V59_2026-08-11.md`
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. paired EV-2 baseline, this work order, task capsule, and all five pinned sources

## Pre-Flight Checks

- capture `git rev-parse HEAD` as `executionBaseHead`;
- require `git status --short --untracked-files=all` to contain no pre-existing
  path outside this dispatch packet;
- recompute all five source hashes and stop on mismatch;
- run the pre-implementation command before material edits;
- confirm both planned output paths do not collide with an existing owner.

## Worker Autonomy / No-Question Rule

Repair any allowed-scope document-shape or citation defect directly and rerun
the named checks. Return to the orchestrator only for a pin contradiction,
required third path, forbidden authority expansion, or irreducible evidence
conflict.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | operator requested the next value-gated roadmap action; EV-2 is the bounded local evidence reconciliation selected |
| scope classification | two document outputs, read-only governed inputs, small blast radius |
| risk sensitivity | no public-sync, provider/live, secret, legal, production, or readiness action |
| selected role route | `MULTI_AGENT_MULTI_ROLE` - delegated worker followed by a separate reviewer/closer |
| role separation basis | worker creates pending evidence; orchestrator/reviewer independently accepts or rejects and owns commits |
| escalation condition | stop and return `BLOCKED_WITH_REASON` on pin mismatch, third-path need, evidence contradiction, or operator-checkpoint scope expansion |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| literalTokensReviewed | work-order structural section groups; compact documentation profile terms; Source Verification columns; operation trace labels; dispatch envelope fields |
| gateRunPurpose | Confirm the fully authored packet against known contracts. |
| claimBoundary | Read-ahead evidence only; no worker-result or semantic-acceptance proof. |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EACQ-FV-EV2 --title "Capsule Effectiveness Evidence Reconciliation" --date 2026-08-28 --base 51fe7eddd --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added exact two-output evidence scope, five pins, comparison/verdict contract, and capsule binding. |
| checkerReadAheadConfirmation | Applicable dispatch, structural, trace, handoff, route, lifecycle, and output-shape checker sources were inspected. |
| docOnlyNewFields | comparison verdict and evidence sufficiency only |
| claimBoundary | Dispatch authoring provenance only. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`evidence reconciliation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

The exact resolver command in the paired baseline returned zero candidates and
was not truncated.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EACQ-FV-EV2",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["docs/assessments", "docs/reviews", "docs/baselines", "docs/roadmaps", "docs/work_orders", "CVF_SESSION"],
  "claims": ["bounded non-causal capsule-effectiveness evidence reconciliation"],
  "requiredProof": ["five source-pin matches", "three-tranche comparison", "comparability adjustment", "missing-data ledger", "exact two-path worker manifest", "independent review"],
  "operatorCheckpoints": ["independent review before commit", "fresh value gate before any successor"],
  "forbiddenEffects": ["code/checker/schema/session mutation", "provider/network use", "UAA execution", "public sync/deploy/push", "worker commit"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named-artifact reconciliation",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P2_BOUNDED`; shadow routing only. The full legacy governance
bundle remains authoritative.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | This is local document reconciliation and makes no runtime-routing claim. Current registry owners include `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY`; both remain outside write scope. |
| requiredFutureAction | Any runtime or live claim requires a fresh source-verified work order and the mandated real-provider proof. |

## Target / Source

Pinned inputs:

| Path | SHA-256 | Required action |
| --- | --- | --- |
| `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | `ed5514590fda9728f43a40a671041bfc1f5d3f00d6c13eddb48e7920f98e584d` | FULL_READ |
| `docs/reviews/CVF_EACQ_FV_EV1_CAPSULE_ENHANCED_OWNER_MAP_EVIDENCE_COMPLETION_2026-08-28.md` | `c95f4b3bd6d09c132f289b7cc075169f7e6ae037d1fd73539e580ea5c75ad88c` | FULL_READ |
| `docs/reviews/CVF_EACQ_FV_L2_EXECUTION_BASE_PACKET_SHAPE_SCAFFOLD_HARDENING_COMPLETION_2026-08-28.md` | `4bccc2da6a4c7a3964ab2cf579fa4a79e1a7a285926c444810f39e8f79431995` | FULL_READ |
| `docs/reviews/CVF_EACQ_FV_L3_AUTOMATION_ASSIST_OWNER_DRIFT_RECONCILIATION_COMPLETION_2026-08-28.md` | `24e6842b99d42eef2c2a8f813ff84a5ad97a1577b612ccbc77e9e7d91ca65459` | FULL_READ |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | `9dc8ff4a57a05f2db0242529281d22e60ead3450133ddd0c00e4c490a9726a7e` | SOURCE_VERIFIED |

Stop before editing if any pin mismatches.

Task capsule expected SHA-256:
`5902be07d78deaa50ec7161ea5a98c5c37cc2fdda0a27c346ad696c73752d12c`.

## Amendment 1 - Post-Dispatch Roadmap Pin Correction

The original roadmap pin was captured before the dispatcher changed that
roadmap in the same material dispatch. The worker correctly stopped when the
committed roadmap recomputed to
`ed5514590fda9728f43a40a671041bfc1f5d3f00d6c13eddb48e7920f98e584d`.
Amendment 1 replaces only that stale pin and the derived capsule pin. It does
not waive source verification, change the two-output manifest, broaden the
verdict vocabulary, or authorize any new path or action.

## Scope / Methodology

Create one assessment and the worker return. For each EV-1/L2/L3 tranche,
extract only source-backed observations for:

1. first-return acceptance or repair route;
2. implementation versus evidence-only correction count and severity;
3. owner overlap, protected path, staging, and manifest defects;
4. positive and negative verification delivered;
5. context/capsule fields demonstrably used;
6. preparation, execution, and review latency when actually recorded;
7. task difficulty, write-scope size, and authority-envelope differences;
8. repeated correction classes or absence thereof.

Then provide an unadjusted table, a comparability-adjusted interpretation,
missing-data ledger, and exactly one verdict: `PROMISING_NON_CAUSAL`,
`NEUTRAL`, `NEGATIVE`, or `INSUFFICIENT_COMPARABILITY`.

## Allowed Scope

Worker may create exactly:

- `docs/assessments/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_2026-08-28.md`
- `docs/reviews/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_WORKER_RETURN_2026-08-28.md`

All other paths are read-only.

## Write Ownership

| Path | Worker permission |
| --- | --- |
| `docs/assessments/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_2026-08-28.md` | CREATE_ONLY |
| `docs/reviews/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_WORKER_RETURN_2026-08-28.md` | CREATE_ONLY |
| every other repository path | READ_ONLY |

## Non-Goals / Forbidden Scope

- no code, schema, checker, helper, test, roadmap, baseline, work-order, session, registry, or external-folder edit;
- no invented latency, token, quota, difficulty score, counterfactual control, or causal estimate;
- no provider/model ranking or superiority claim;
- no provider call, credential use, network refresh, public sync, push, deploy, staging, or commit;
- no UAA-G1/G2/G3 reopen and no automatic successor recommendation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| comparison dimensions are required | governed requirement | `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | Verification / Evidence Plan | comparison dimensions | EACQ-FV roadmap | ACCEPT |
| EV-1 observation is bounded | governed evidence | `docs/reviews/CVF_EACQ_FV_EV1_CAPSULE_ENHANCED_OWNER_MAP_EVIDENCE_COMPLETION_2026-08-28.md` | F-03 | effectiveness classification | completion review | ACCEPT |
| L2 observation is bounded | governed evidence | `docs/reviews/CVF_EACQ_FV_L2_EXECUTION_BASE_PACKET_SHAPE_SCAFFOLD_HARDENING_COMPLETION_2026-08-28.md` | F-06 | effectiveness classification | completion review | ACCEPT |
| L3 observation is bounded | governed evidence | `docs/reviews/CVF_EACQ_FV_L3_AUTOMATION_ASSIST_OWNER_DRIFT_RECONCILIATION_COMPLETION_2026-08-28.md` | Findings / Position | capsule effectiveness | completion review | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Search roots | `docs CVF_SESSION` | COMPLETE_FOR_NAMED_TOKEN |
| Exact query | `rg -n "EACQ-FV-EV2|Capsule Effectiveness Evidence Reconciliation" docs CVF_SESSION` | no prior owner before dispatch |
| Owner decision | roadmap owns criteria; completion reviews own observations; new assessment is a derived reconciliation only | ENRICH_EXISTING |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: the three pinned completion reviews

priorVerificationAnchor: exact SHA-256 rows in Target / Source

freshRecomputeRequired: source hashes, cited observations, comparison table arithmetic, and final manifest only

unicodePathHandling: use repository-relative literal paths and UTF-8-safe readers; do not normalize evidence paths into a different identity

extractedTextAuthority: governed markdown contents are evidence; provider memory and side-channel summaries are not authority

## Execution Plan

| Step | Action | Evidence | Stop condition |
| --- | --- | --- | --- |
| 1 | capture `executionBaseHead`, status, and verify all five pins | hash table in worker return | any mismatch |
| 2 | create checker-safe skeletons for both outputs | direct heading inspection and fast gate | required shape unavailable |
| 3 | extract per-tranche facts with citations | evidence ledger | uncited or contradictory fact |
| 4 | compare with explicit task-difference adjustments | comparison and missing-data matrices | forced causal inference needed |
| 5 | choose one allowed verdict and bounded next-evidence disposition | deterministic decision table | verdict conditions ambiguous |
| 6 | run all final checks and return without staging | command receipts and status | unexpected path or failing gate |

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/assessments/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_2026-08-28.md` | CREATE |
| `docs/reviews/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_WORKER_RETURN_2026-08-28.md` | CREATE |

## Work-Order Fulfillment Manifest

The worker must return both Required Artifact Manifest rows, no extra path,
empty staging, all placeholders resolved, and exact command evidence. The
reviewer compares expected and actual manifests before any material commit.

## Assessment Decision Contract

| Verdict | Required condition |
| --- | --- |
| `PROMISING_NON_CAUSAL` | at least two source-backed positive observations, no repeated owner/protected-path violation, and all contrary evidence disclosed; causal attribution still forbidden |
| `NEUTRAL` | mixed observations with neither bounded positive nor negative direction |
| `NEGATIVE` | source-backed repeated material regression, boundary failure, or repair burden attributable only as observed association |
| `INSUFFICIENT_COMPARABILITY` | task/scope differences or missing required metrics prevent even a bounded directional classification |

When evidence supports a direction but precise latency or a matched control is
missing, prefer the bounded non-causal verdict and explicitly list the missing
evidence. Never upgrade it to causality.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated evidence worker followed by independent reviewer/closer |
| phase | no-commit evidence execution |
| baseHeadFor(phase) | dispatchBaseHead=`51fe7eddd`; executionBaseHead=worker captures current clean HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exact two-path worker manifest |
| traceScope(phase, actor) | worker records commands and files; reviewer independently verifies |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns accepted commits |
| crossBatchIsolation | no unrelated path or parked lane may enter the diff |
| nextMoveSurfaces | worker return only; roadmap/session changes remain reviewer/closer-owned |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer an independent reviewer addendum in the worker return |
| reviewerOwnedClosurePaths | paired work order and roadmap only if the evidence is accepted |
| closureOwner | designated internal reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before authoring, derive exact shape for the assessment and review output from
the structural, worker-return, trace, epistemic, corpus, rescan, and public
disposition checkers. Required review section names include Purpose, Target /
Source, Scope / Methodology, Findings / Position, Risk / Corrective Action,
Decision / Disposition, External Knowledge Intake Routing, Epistemic Process
Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control
Block, Public Export Disposition, executionBaseHead, git status --short,
Changed Files, and No-Commit Statement.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EACQ_FV_EV2_CAPSULE_EFFECTIVENESS_EVIDENCE_RECONCILIATION_WORKER_RETURN_2026-08-28.md`

contractProfile: WORKER_RETURN_FAST_DOC_V1

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

Use `N/A with reason` for conditional blocks that genuinely do not apply.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_markdown_structural_completeness.py
git diff --check
git diff --name-status
git diff --cached --name-only
git status --short --untracked-files=all
```

## Acceptance Criteria

- [ ] all five source pins match before writing;
- [ ] exactly two worker-owned outputs exist and no other path changes;
- [ ] every metric cell is cited or explicitly `NOT_AVAILABLE_WITH_REASON`;
- [ ] task comparability and missing-data matrices are complete;
- [ ] exactly one allowed verdict is selected by the decision contract;
- [ ] no causal, provider-superiority, runtime, public, or UAA claim appears;
- [ ] final gates pass and staging is empty.

Fail if any pin differs, evidence is invented, scope expands, a causal claim is
made, or the worker cannot choose a verdict without exceeding the evidence.

## Evidence Requirements

Evidence Trace Block:

| Claim | Command or source | Required result |
| --- | --- | --- |
| source identity | SHA-256 recomputation for all five pins | exact match |
| comparison completeness | assessment metric and missing-data matrices | every required dimension present |
| verdict determinism | Assessment Decision Contract | exactly one allowed token |
| path integrity | `git diff --name-status` and staging/status commands | exact two paths and empty staging |
| packet quality | pre-implementation, worker-return fast, and structural commands | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap control | Work-order handling | Verdict |
| --- | --- | --- |
| comparable-task effectiveness dimensions | extracted across all three pinned completion reviews | PASS |
| explicit adjustment for materially different tasks | comparability matrix and missing-data ledger required | PASS |
| no provider/model superiority claim | forbidden scope and decision contract | PASS |
| UAA stays gated | no UAA output or action permitted | PASS |
| value must exceed cost | two docs-only outputs, local proof, zero external quota | PASS_BOUNDED |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the three observations will support at most a
promising non-causal direction, with latency and matched-control evidence still
insufficient for a causal claim.

Evidence Comparison Requirement: compare the extracted facts against that
prediction and disclose contrary evidence.

Contradiction Handling Requirement: contradictory evidence narrows the verdict
to `NEUTRAL` or `INSUFFICIENT_COMPARABILITY`; it must not be averaged away.

Claim Update Requirement: state whether the roadmap's effectiveness claim is
confirmed, revised, narrowed, or remains unproved.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher/reviewer |
| Provider or surface | local private-provenance repository |
| Session or invocation | EACQ-FV-EV2 dispatch, 2026-08-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, hashing, scaffold helper, ADIF resolver, `apply_patch` |
| Target paths | paired baseline, this work order, paired task capsule, roadmap |
| Allowed scope source | operator continuation plus fresh four-part value gate |
| Before status evidence | clean worktree at `51fe7eddd` |
| After status evidence | exact dispatch-author manifest before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only; worker remains no-commit |
| Claim boundary | no implementation, causal uplift, provider, public, push, or deployment claim |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eacq-fv-ev2-dispatch-2026-08-28` |
| Expected manifest | paired baseline; this work order; paired capsule; blocked-attempt worker return; bootstrap read model; current state core; generated state aggregate |
| Actual changed set | exact seven paths listed in Expected manifest |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | local document evidence reconciliation only |
| claimDisposition | N/A with reason: no execution-control or runtime-enforcement claim |
| receiptEvidence | N/A with reason: no runtime receipt is required or produced |
| actionEvidence | N/A with reason: only governed file reads and two document outputs |
| invocationBoundary | local no-commit worker invocation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or network interception claim |
| claimLanguage | bounded comparison of governed completion evidence |
| forbiddenExpansion | runtime, provider/live, public, package, deployment, UAA, causal uplift, or universal control |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | orchestrator/reviewer/closer | dispatch, independent review, commit, and closure only | baseline, work order, later reviewer addendum | no worker self-acceptance | ALLOWED_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | delegated worker through copied canonical packet | exactly two unstaged document outputs | worker return and Git status | no runtime adapter or authority transfer | ALLOWED_BOUNDED |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance evidence reconciliation only.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | governed EV-1/L2/L3 returns -> independent completion evidence -> EV-2 derived reconciliation -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EACQ-FV roadmap criteria and three named completion reviews |
| Disposition | RECONCILE_BOUNDED_NON_CAUSAL_EVIDENCE |
| Claim boundary | no direct import, authority transfer, causal uplift, provider action, or public mutation |

## Foundation Storage Layout Block

N/A with reason: the worker creates one bounded assessment and one return; no
foundation file family, registry, generated aggregate, split, relocation, or
durable runtime owner is created.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: EV-2 compares three current governed completion
reviews and does not absorb, reclassify, or reopen a legacy source family or
change a legacy coverage index.

## Core Guard Self-Protection Authorization - Amendment 1

Authorized guard-maintenance scope: reconcile only the current-authority
hash carriers required because Amendment 1 changes the active baseline and
work-order bytes.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Operator authorization: operator returned the worker's valid fail-closed
blocker to the orchestrator/reviewer for continuation.

Rollback boundary: revert the exact seven-path Amendment 1 batch atomically;
retain original dispatch `9ac836be0`, session sync `69c42a55d`, and all prior
closures.

Not authorized: mode or next-move change, code/checker/runtime/provider/public
mutation, UAA, deployment, push, secrets, or unrelated work.

## Mixed Protected-Path Atomicity Authorization - Amendment 1

Disposition: AUTHORIZED_EXACT_MANIFEST

Reason: baseline/work-order bytes and their current-authority hashes must land
atomically; the blocked worker return is preserved as the reason receipt.

Exact changed manifest: paired baseline; this work order; paired capsule;
blocked-attempt worker return; bootstrap read model; current state core;
generated state aggregate.

## Claim Boundary

This work order authorizes exactly two uncommitted documents. It does not
authorize code or governance-owner mutation, causal uplift, UAA, provider,
public, push, deployment, production, or an automatic successor.

## Closure Checklist

- [ ] worker returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`
- [ ] reviewer independently verified citations, verdict, and exact manifest
- [ ] accepted material committed by reviewer/closer only
- [ ] exact material-range pre-closure gate passed
- [ ] session continuity updated separately if mode or next move changes

## Review Gate

Worker handoff is not closure. The reviewer must independently verify source
pins, citations, comparability adjustments, contrary evidence, verdict,
changed-set accuracy, and worker-return fast evidence. Only the reviewer may
accept, repair, commit, close, or update the roadmap/session surfaces.

## Operator Checkpoint

operator.checkpoint.waiver: N/A with reason - the operator's `next`
continuation authorizes this evidence-only dispatch through the recorded value
gate. Any provider/live, public, UAA, implementation, or scope expansion still
requires a fresh operator decision.

## Return-To-Orchestrator Conditions

Return immediately for pin mismatch, contradictory source ownership, required
third output, forbidden path need, provider/public need, or inability to bound
the verdict without inventing evidence.
