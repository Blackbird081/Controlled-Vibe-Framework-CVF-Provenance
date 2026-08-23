# CVF Agent Work Order - TPGR-R8 P0/P1 Allowlist Decision Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Batch ID: TPGR-R8

Dispatch base head: `ac678d0cbea841087e9896c5242ee69d978a0471`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated design worker

Reviewer/closer: CVF reviewer/orchestrator

Worker return path: `docs/reviews/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_WORKER_RETURN_2026-08-23.md`

## Dispatch Prompt Envelope

Role: delegated no-commit design worker for TPGR-R8.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse HEAD` at start; it must equal the
clean post-dispatch-continuity HEAD supplied by the operator.

Current-time notes: artifact date is 2026-08-23; verify repository state
locally and use only CVF-governed authority.

Do-not-misread notes: decision design only; no allowlist implementation,
activation, checker/harness/config/store, real canary, selective execution,
legacy suppression, R9 execution, or external effect.

Required first actions: verify exact clean HEAD; read paired baseline, this
work order, startup surfaces, guard orientation, literal gotchas, all Required
First Reads, and applicable checker sources. Run both preflight commands before
the first edit.

Return contract: create exactly the two authorized outputs, run all required
gates, leave both unstaged and uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Design an evidence-bound P0/P1 decision model for the six accepted R7 cases.
P0 is only a candidate label for separate future activation authority; P1
retains the full legacy bundle. R8 changes no execution behavior.

## Worker Autonomy / No-Question Rule

Repair artifact-shape or semantic defects directly only inside the two allowed
paths. Stop only for missing/contradictory authority, a required out-of-manifest
write, or an external effect. Do not invent current observations or identities.

## Scope / Target / Owner Boundary

- Dispatcher owns this committed documentation-only packet.
- Worker owns only the exact assessment and worker-return paths.
- Reviewer independently recomputes admission decisions, hostile cases,
  revocation, cost labels, and final disposition; reviewer owns all commits.
- Operator owns any R9, implementation, activation, or expanded authority.

Allowed scope: read accepted CVF evidence and create the exact two outputs.

Forbidden scope: every other repository path and every runtime/external action.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R7 accepted material | commit `723382cfc`; accepted assessment and worker-return hashes in paired baseline | ACCEPT |
| R7 closure continuity | commit `9bbc6bf31` | ACCEPT |
| Operator continuation checkpoint | user request on 2026-08-23 | ACCEPT |
| R8 implementation/activation and R9 | outside this packet | NOT_AUTHORIZED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R8 --title "P0 P1 Allowlist Decision Design" --date 2026-08-23 --base ac678d0cbea841087e9896c5242ee69d978a0471 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact R7 evidence, eligibility identity, admission, revocation, hostile cases, thresholds, output paths, and dispositions |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `decisionCaseId`, `eligibilityIdentity`, `evidenceState`, `allowlistClass`, `admissionReason`, `expiryState`, `revocationTier`, `reentryProof` |
| claimBoundary | dispatch provenance only; no executable allowlist or route behavior |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: 22; not truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | exact roles/paths, checker read-ahead, honest evidence labels, no-commit ownership, and independent review are mandatory |

## Required First Reads

1. `AGENTS.md`.
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
3. `CVF_SESSION_MEMORY.md` and active handoff.
4. `docs/reference/guard_orientation/README.md`.
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
6. Paired R8 baseline and this work order.
7. `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`.
8. R7 baseline, work order, assessment, and worker return in full.
9. R6 assessment and worker-return Independent Reviewer Addendum for binding H3.
10. `governance/compat/agent_autorun_command_catalog.py`, read-only.
11. Applicable checker sources for baseline and review output shape.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R8 design is authorized | predecessor disposition | `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | Final Disposition | accepted assessment path | accepted R7 design | ACCEPT |
| legacy bundle remains sole controller | interlock fact | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock | standard path | TPGR standard | ACCEPT |
| C1-C6 evidence is documentary | evidence-state fact | `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | Required Canary Design Cases | assessment path | accepted R7 design | ACCEPT |
| stale H3 identity cannot light-route | reviewer binding | `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum | worker-return path | accepted R6 review | ACCEPT |
| R8 candidate paths are zero-edit | successor boundary | `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | Zero-Edit R8 P0/P1 Allowlist-Decision Candidate Manifest | assessment path | accepted R7 design | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_agent_operation_trace.py` |
| requiredLiteralShapes | baseline assessment groups; full worker-return profile; Source Verification columns; routing JSON; trace, delta, public, corpus, status, and no-commit evidence |
| authoringRule | checker source determines output shape before drafting; gates confirm rather than discover requirements |
| literalTokensReviewed | `Status: COMPLETE_PENDING_REVIEW`; `Purpose`; `Scope / Methodology`; `Findings / Position`; `Risk / Corrective Action`; `Claim Boundary`; `executionBaseHead`; `git status --short`; `WORKER_MUST_NOT_COMMIT`; routing JSON |
| gateRunPurpose | confirmation and evidence after source-led authoring, not first discovery |
| claimBoundary | checker conformance does not semantically approve admission or activation |

## Protocol / Contract / Requirements

### Closed P0/P1 Vocabulary

Define P0 only as a documentation-time candidate for a future lighter route.
Define P1 as full legacy bundle required. R8 must explicitly state that both
classes execute the unchanged full legacy bundle because activation is absent.

### Exact Eligibility Identity

The identity must bind all eight TPGR classification dimensions, sorted path
families, claims, required proof, route-receipt identity, legacy command-catalog
identity, checker semantic identities, confirming reviewer identity, evidence
hashes, and freshness/expiry. Any missing or widened component selects P1.

### Admission Predicates

Specify a deterministic conjunction. P0 candidacy requires current exact
identity, current H3 binding, complete R7 comparator evidence, only
`EXACT_AGREEMENT`, zero mismatch/unknown/partial/timeout/stale/drift state,
no P3/P4 trigger, independent review, and unexpired evidence. A proposed
threshold that cannot be met from accepted evidence must remain unmet.

### C1-C6 Decision Table

Evaluate all six R7 cases. Separate `OBSERVED_CURRENT`, `HISTORICAL_BOUNDED`,
`DESIGN_TIME_EXPECTATION`, `PROJECTED`, and `UNKNOWN`. Design-time expected
agreement cannot become observed agreement. Empty P0 is valid and must not be
treated as failure.

### Hostile Admission Cases

Design at least eight cases: one each for identity drift, checker semantic
drift under stable filenames, stale reviewer binding, partial receipt, widened
task/path scope, protected-path contamination, contradictory comparator state,
and expiry. Each must state detection, P1 outcome, preserved evidence,
revocation tier, operator visibility, and exact re-entry proof.

### Decision Record, Expiry, Revocation, And Re-entry

Specify an immutable documentary record with identity, hashes, evidence label,
decision/reasons, reviewer, expiry, revocation tier, and re-entry proof. Do not
create a registry/store. Ambiguous or cross-class scope invokes global Tier 1
reversion to advisory-off/full legacy; class-local Tier 2 requires exact
dependency closure. Re-entry requires fresh exact proof, never copied receipts
or timestamp-only refresh.

### Negative-Test Design

Specify at least ten tests proving: P0 cannot suppress/reorder/skip commands;
P1 remains full-bundle; unknown/partial/stale selects P1; H3 remains binding;
stable names cannot hide semantic drift; protected scope cannot enter P0;
expiry revokes; ambiguous class scope promotes Tier 1; serialized decisions
cannot execute; and R9 candidate text grants no activation.

### Cost And Value

Separate unavoidable legacy execution, classification, identity verification,
comparison, review, expiry maintenance, revocation/re-entry, and future
activation cost. Label every value `OBSERVED`, `HISTORICAL_BOUNDED`,
`PROJECTED`, or `UNKNOWN`. No projection is a saving or activation reason.

### Zero-Edit R9 Candidate Manifest

Name possible future paths and prerequisites only. Do not create or edit a
checker, harness, registry, store, standard, config, test, receipt, or runtime
plan. R9 remains a fresh operator decision after independent R8 closure.

## Acceptance Thresholds

- 6/6 C1-C6 decisions with explicit evidence labels;
- 100% unobserved/stale/unknown/partial/conflicting cases select P1;
- zero projected/design-time agreement promoted to observed;
- zero protected/state/runtime/live/public/destructive case enters P0;
- at least 8/8 hostile cases fail closed;
- at least 10/10 negative-test designs have expected outcomes;
- 100% ambiguous revocation scope selects Tier 1;
- zero legacy suppression/reorder/skip and zero added enforcement;
- deterministic decision, expiry, revocation, rollback, and re-entry fields;
- separated costs with no projected saving presented as observed;
- zero-edit activation-neutral R9 manifest;
- exact two paths, no staging, no commit;
- exactly one allowed disposition.

Any miss forbids `PROCEED_TO_R9_ACTIVATION_AND_ROLLBACK_AUTHORITY_DESIGN`.

## Acceptance Criteria

Sources and exact identities are cited; every case and hostile scenario is
deterministic; evidence states remain honest; P1/full legacy is fail-closed;
empty P0 is allowed; R9 has no authority; gates pass; reviewer independently
accepts or returns the packet.

## Allowed Final Dispositions

- `PROCEED_TO_R9_ACTIVATION_AND_ROLLBACK_AUTHORITY_DESIGN`
- `HOLD_EMPTY_P0_ALLOWLIST_PENDING_OBSERVED_DUAL_RUN_EVIDENCE`
- `REVISE_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`
- `STOP_TPGR_SECOND_UPGRADE`

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/assessments/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md` | create complete P0/P1 decision-design assessment |
| `docs/reviews/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_WORKER_RETURN_2026-08-23.md` | create full worker-return evidence packet |

Forbidden paths: every other repository path. Do not stage or commit.

## Forbidden Actions

- edit any existing file or create a third output;
- stage, commit, push, or modify Git configuration;
- implement an allowlist, checker, harness, store, receipt, standard, config,
  test, fixture, registry, hook, or autorun/CI change;
- execute a real canary or selective command plan;
- invoke provider/network/live/public-sync/deploy/production actions;
- authorize R9 or activation.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-R8",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["docs/baselines/", "docs/assessments/", "docs/reviews/"],
  "claims": ["bounded P0/P1 allowlist decision design"],
  "requiredProof": ["C1-C6 decisions", "hostile admission cases", "expiry and revocation", "negative-test design", "cost separation", "full legacy gate"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["protected mutation", "allowlist activation", "selective execution", "runtime or external effects"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: accepted bounded design evidence only; no corpus claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, `P2_BOUNDED`, selective execution false, and
`RUN_FULL_LEGACY_BUNDLE`.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_WORKER_RETURN_2026-08-23.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Source Inventory; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Claim
Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; Public Export Disposition; executionBaseHead; git status --short;
Changed Files; Command Evidence; No-Commit Statement; Machine Closure Package.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block. Use `N/A with reason` when not
applicable, but retain every real heading.

## Worker Output Checker Read-Ahead Mandate

Before writing, inspect checker source for both output docTypes and path
families. Derive headings, tables, trace/delta/public/corpus/status/no-commit
literals and first-run evidence shape before drafting. Gate failure is not a
substitute for read-ahead.

## Verification Commands

Required preflight before first edit and final rerun after last edit:

```powershell
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | prior critique is already reconciled through accepted TPGR evidence |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | TPGR standard plus accepted R6-R7 evidence |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no corpus registration, direct import, or authority promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: R8 evaluates a fixed committed six-case design set and does not refresh
an external source.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - the bounded C1-C6 set plus
hostile cases is not a claim that any upstream corpus was fully absorbed.

## Finding-To-Governance Learning Disposition

Record a new repeatable defect only if semantic review finds one not already
owned by current rules; otherwise use `N/A_WITH_REASON`.

## Epistemic Process Block

Expected Result / Prediction: honest evidence labeling is expected to keep any
unobserved R7 design case in P1 while still defining a deterministic future P0
admission contract.

Evidence Comparison: compare every identity, evidence-state, admission,
revocation, cost, and disposition field against R6-R7 accepted authority and
the unchanged legacy interlock.

Contradiction Or Gap Disposition: any invented observation, incomplete identity,
light-route control, ambiguous class-local rollback, or R9 preauthorization
requires revision, hold, or stop.

Claim Update: exactly one R8 disposition; no active authority changes.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external no-commit design worker followed by independent internal reviewer/closer |
| phase | R8 worker execution then independent review |
| baseHeadFor(phase) | dispatchBaseHead=`ac678d0cbea841087e9896c5242ee69d978a0471`; executionBaseHead=worker captures clean post-continuity HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | worker exact two outputs; reviewer bounded repairs only there; continuity separate |
| traceScope(phase, actor) | worker records reads, decisions, commands, manifest, and no-commit evidence; reviewer independently recomputes |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no implementation, activation, R9, T15, source intake, runtime, or external-effect lane |
| nextMoveSurfaces | continuity changes only after independent material acceptance |

## Dual Agent Surface Matrix

| Surface | Role | Access | Disposition |
|---|---|---|---|
| INTERNAL_AGENT | dispatcher/reviewer/closer | author packet, review, commit, sync | ACTIVE |
| EXTERNAL_AGENT_CLI_MCP | no-commit worker | exact two documentation outputs | AUTHORIZED_BOUNDED |
| adapter/runtime boundary | none in R8 | no access | NOT_AUTHORIZED |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_COMPLETION_2026-08-23.md` (optional reviewer-owned path; prefer an Independent Reviewer Addendum unless distinct closure evidence becomes necessary) |
| reviewerOwnedClosurePaths | exact two worker outputs; continuity separately after acceptance |
| closureOwner | CVF reviewer/orchestrator |
| workerCommitPermission | FORBIDDEN |

Reviewer independently recomputes C1-C6 decisions and every hostile case,
verifies evidence labels, empty-P0 safety, thresholds, identity binding, costs,
R9 neutrality, exact paths, hashes, and gates.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/orchestrator as dispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | TPGR-R8 dispatch authoring, 2026-08-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, collision search, apply_patch, local gates, Git |
| Target paths | paired R8 baseline and this work order |
| Allowed scope source | accepted R7 disposition plus operator continuation checkpoint |
| Before status evidence | clean worktree at `ac678d0cbea841087e9896c5242ee69d978a0471` |
| After status evidence | exactly two dispatch artifacts before commit |
| Diff evidence | `git diff --check`; `git status --short --untracked-files=all` |
| Approval boundary | documentation-only R8 decision-design dispatch |
| Claim boundary | no implementation, activation, canary, selective execution, or external effect |
| Agent type | reviewer/orchestrator dispatch author |
| Invocation ID | `tpgr-r8-dispatch-authoring-2026-08-23` |
| Expected manifest | paired R8 baseline and work order |
| Actual changed set | same two paths before dispatch commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R8 documentation-only P0/P1 decision design |
| claimDisposition | CLAIM_REJECTED: no execution-control, allowlist activation, or selective-command behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: accepted documents are evidence; no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two design dispatch artifacts and local gates only |
| invocationBoundary | local reads, documentary authoring, gates, and Git commit |
| interceptionBoundary | no wrapper, proxy, runtime gate, CLI/MCP adapter, or coding interception |
| claimLanguage | proposed decision and evidence contract, not implemented behavior |
| forbiddenExpansion | no source/checker/standard/registry/config/test/session edit by worker; no R9/runtime/provider/live/public/deploy/production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only design dispatch with no public artifact.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | no runtime, provider, live, allowlist activation, or selective execution |

## Foundation Storage Layout Block

N/A with reason: R8 creates no store, receipt directory, cache, fixture tree,
registry, or persistence surface.

## Stop Conditions

Stop for missing authority, source contradiction, required third path,
unprovable identity that is nevertheless needed for a proceed claim, any
executable artifact requirement, legacy behavior change, or external effect.

## Authority Chain

Operator continuation checkpoint -> accepted R7 disposition -> paired R8
baseline/work order -> no-commit worker -> independent reviewer/closer. No
worker decision becomes authority before review.

## Agent Roles

- Worker reads, analyzes, authors exactly two outputs, gates, and does not commit.
- Reviewer recomputes, repairs only within scope if needed, accepts/rejects,
  commits material, and synchronizes continuity separately.
- Operator owns any expansion, R9, implementation, activation, or external effect.

## Pre-Flight Checks

1. `git rev-parse HEAD` equals supplied execution base.
2. `git status --short --untracked-files=all` is empty.
3. Required First Reads exist and output paths do not exist.
4. Task route checker and pre-implementation gate pass before editing.

## Intake Role Routing Decision

Intake summary: accepted CVF evidence only; no new source intake.

Scope classification: bounded documentation-only decision design.

Risk sensitivity: medium because future execution eligibility is discussed,
but no behavior or authority is changed.

Selected role route: `routeMode=MULTI_AGENT_SINGLE_ROLE`.

Role separation basis: worker produces evidence; reviewer independently
recomputes and owns commit.

Escalation condition: missing/contradictory source, out-of-manifest write,
threshold miss, or external effect.

Source authority: committed CVF artifacts only.

Corpus action: bounded reads; no registration or import.

Direct import: forbidden.

## Write Ownership

Worker owns only the two uncommitted fulfillment paths. Reviewer owns bounded
repairs in those paths, staging, material commit, and separate continuity.

## Execution Plan

1. Preflight and checker/source read-ahead.
2. Freeze R7 cases and eligibility identity fields.
3. Define admission/default rules and decide C1-C6.
4. Exercise hostile cases and revocation/re-entry.
5. Design negative tests and cost/value separation.
6. Reconcile thresholds, zero-edit R9 manifest, and one disposition.
7. Complete worker return and run final gates.
8. Leave exactly two paths unstaged and return.

## Evidence Requirements

Every decision cites current governed facts and an explicit evidence-state
label. Tables reconcile exactly. Costs distinguish observed, historical,
projected, and unknown. Self-reported counts without rows are not evidence.

## Review Gate

Reviewer independently recomputes every C1-C6 decision and hostile case,
verifies all thresholds, reruns gates, and rejects a proceed disposition that
depends on invented observation, incomplete identity, suppressed legacy work,
ambiguous class-local rollback, or R9 preauthorization.

## Operator Checkpoint

No checkpoint is needed for exact worker execution. R9 or any implementation,
activation, real canary, selective execution, protected mutation, or external
effect requires fresh operator authority after accepted R8 closure.

## Closure Checklist

- exact two paths and zero staging;
- 6/6 case decisions and at least 8 hostile cases;
- at least 10 negative-test designs;
- exact H3 binding and evidence-state honesty;
- deterministic expiry/revocation/re-entry;
- one allowed disposition;
- task route, worker-return fast, pre-implementation, and diff hygiene pass;
- independent reviewer acceptance before commit.

## Claim Boundary

This order authorizes documentary P0/P1 decision design only. It does not
authorize an allowlist, checker, harness, store, receipt, standard/config
change, activation, selective gate execution, legacy suppression, R9,
provider/live/network/public/deploy/production, or any third output.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every required case, hostile test,
threshold, artifact, and gate is complete. Otherwise return
`BLOCKED_WITH_REASON` with the exact unmet requirement and no scope widening.

## Legacy Absorption Coverage Index Disposition

N/A with reason: R8 changes no source corpus and makes no completeness claim.
