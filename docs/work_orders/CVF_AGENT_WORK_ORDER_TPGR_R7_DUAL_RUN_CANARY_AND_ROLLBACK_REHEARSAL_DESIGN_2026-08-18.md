# CVF Agent Work Order - TPGR-R7 Dual-Run Canary And Rollback Rehearsal Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Batch ID: TPGR-R7

Dispatch base head: `4c620f30d3bf716a8791be12c8ebec803fde414d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated design worker

Reviewer/closer: CVF reviewer/orchestrator

Worker return path: `docs/reviews/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_WORKER_RETURN_2026-08-18.md`

## Dispatch Prompt Envelope

Role: delegated no-commit design worker for TPGR-R7.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse HEAD` at start; it must equal the
clean post-dispatch-continuity HEAD supplied by the operator.

Current-time notes: artifact date is 2026-08-18; verify current repository
state locally and do not use provider memory as authority.

Do-not-misread notes: documentation-only; no harness, canary execution,
selective execution, command suppression, R8 activation, or external effect.

Required first actions: verify clean worktree and exact HEAD; read the paired
baseline, this work order, startup surfaces, guard orientation, literal
gotchas, every Required First Read, and applicable checker source before
writing. Run the two preflight commands before the first edit.

Return contract: create exactly the two authorized output files, run all
required gates, leave them uncommitted and unstaged, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Design a strictly advisory dual-run comparison and paper rollback rehearsal
that can later test TPGR against the unchanged phase-appropriate legacy gate
bundle. This tranche performs no canary execution and changes no authority.

## Worker Autonomy / No-Question Rule

Repair checker-shape or contract defects directly only inside the two allowed
paths. Return early only for a source contradiction, missing authority, or a
required write outside the exact manifest. Do not invent evidence or widen
scope to avoid a block.

## Scope / Target / Owner Boundary

- Dispatcher: reviewer/orchestrator; owns this committed packet.
- Worker: owns only the exact assessment and worker-return paths below.
- Reviewer/closer: independently checks route precedence, comparator safety,
  rollback determinism, evidence, and gates; owns all commits and continuity.
- Operator: owns any future R8 authorization or scope expansion.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R6 accepted material | R6 assessment and reviewer addendum; commit `27e87a1ca` | RELEASED_WITH_H3_STRICT_ROUTE |
| R6 closure continuity | committed R6 closure continuity at `e55e9e001` | RELEASED |
| R8 and selective execution | outside this tranche | NOT_AUTHORIZED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R7 --title "Dual-Run Canary And Rollback Rehearsal Design" --date 2026-08-18 --base 4c620f30d3bf716a8791be12c8ebec803fde414d --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact sources, comparator fields, C1-C6 cases, mismatch policy, rollback rehearsals, thresholds, and manifests |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `canaryCaseId`, `legacyObservedOutcome`, `tpgrAdvisoryOutcome`, `comparisonDisposition`, `rollbackTier`, `rollbackFromNode` |
| claimBoundary | dispatch provenance only; no executable comparison, command suppression, receipt, or runtime behavior |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | exact roles and paths, checker read-ahead, no authority aggregation, honest first-run evidence, no-commit ownership, and reviewer-independent comparison are mandatory |

## Required First Reads

1. `AGENTS.md`
2. `docs/reference/guard_orientation/README.md`
3. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
4. paired R7 baseline
5. this work order
6. `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`
7. R3 assessment sections on deterministic precedence and rollback floors
8. R5 assessment sections on identity binding, invalidation, and cost
9. R6 assessment in full, including the reviewer-corrected H3 route and its
   Zero-Edit R7 Candidate Manifest
10. R6 worker return Independent Reviewer Addendum
11. `governance/compat/agent_autorun_command_catalog.py` as the single legacy
    command-universe owner; read only, do not duplicate it.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R7 design is authorized | predecessor disposition | `docs/assessments/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md` | Final Disposition | assessment path | accepted R6 design | ACCEPT |
| legacy route remains controlling | interlock fact | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock | standard path | TPGR standard | ACCEPT |
| ambiguity cannot light-route | threshold fact | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Route Outcomes And Deterministic Precedence | assessment path | accepted R3 design | ACCEPT |
| H3 current identity is not proven | review finding | `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum | worker-return path | accepted R6 review | ACCEPT |
| phase-aware command ownership exists | catalog fact | `governance/compat/agent_autorun_command_catalog.py` | common, pre-implementation, and pre-push command collections | command collections | command catalog module | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| requiredLiteralShapes | assessment baseline sections; worker-return full-gate profile; exact status and no-commit terms; Source Verification columns; task-routing JSON |
| authoringRule | checker sources inform exact artifact shape before drafting; gates confirm rather than discover requirements |
| literalTokensReviewed | dispatch-ready status; mandatory work-order groups; Source Verification columns; no-commit terms; routing JSON; worker-return headings, trace fields, delta/public/corpus/status and hardening literals |
| gateRunPurpose | confirmation and evidence after source-led authoring |
| claimBoundary | checker conformance is not semantic acceptance of comparator or rollback design |

## Protocol / Contract / Requirements

### Comparator Record

Define a documentary schema with, at minimum:

- `canaryCaseId`, task/archetype and lifecycle phase;
- exact source/diff/command-catalog/checker/review identities;
- `legacyObservedOutcome` and evidence reference;
- `tpgrAdvisoryOutcome` and evidence reference;
- comparison status: exact agreement, advisory stricter, advisory lighter,
  unknown/partial, or contradiction;
- controlling outcome, always the legacy outcome in R7;
- mismatch class, earliest affected node, preserved evidence;
- rollback tier, scope, trigger, action, and re-entry requirements;
- separated observed/projected costs.

Never call a projected or documentary value observed. A copied timestamp,
path match, or role label is not identity currency.

### Required Canary Design Cases

| Case | Archetype | Required posture |
|---|---|---|
| C1 | A1 new upstream corpus | both routes retain full first-intake floor |
| C2 | A2 mixed-origin synthesis | dual-origin and semantic-reading controls remain mandatory |
| C3 | A3 accepted-corpus cluster | historical reuse value preserved, but H3 stays `ESCALATE_FOR_REVIEW` until current identity is earned |
| C4 | A4 upstream delta | earliest-node full verification controls affected scope |
| C5 | A5 advisory item | authority ambiguity escalates; small size never downgrades |
| C6 | A6 downstream project source | registration never promotes project evidence to CVF authority |

The cases are paper/design comparisons only. Do not run a canary or execute a
selective plan.

### Required Mismatch Classes

1. TPGR advisory is lighter than the legacy outcome.
2. TPGR advisory is stricter than the legacy outcome.
3. receipt owner, checker closure, catalog row, or confirming-review identity
   is missing/stale.
4. checker or catalog semantics drift while names remain stable.
5. either comparison side times out, is partial, malformed, or unavailable.
6. evidence sources contradict each other or the worker summary.

For each, specify detection, controlling outcome, evidence preservation,
rollback tier/scope, operator visibility, and re-entry proof. No mismatch may
silently become agreement.

### Rollback Rehearsal

Design at least four Tier 1 global scenarios and three Tier 2 class-scoped
scenarios. Tier 1 covers unknown scope, cross-class contamination, command
suppression risk, or comparator integrity failure. Tier 2 is allowed only when
the affected class and dependency closure are exact and independently proven.
Ambiguity always promotes Tier 2 to Tier 1.

Rollback is a design-time state transition back to legacy-only advisory-off
posture. Do not claim a config switch exists unless a current CVF-owned source
proves it. Re-entry requires full R6 replay plus R7 comparison/rehearsal proof
for the affected identity; copying a receipt or changing time does not qualify.

### Negative-Test Design

Specify, but do not implement, tests proving:

- advisory lighter never suppresses a legacy command;
- advisory stricter never adds enforcement in R7;
- unknown/partial cannot be agreement;
- stale H3 identity cannot light-route;
- stable filenames do not mask semantic checker drift;
- class-scope ambiguity invokes Tier 1;
- rollback preserves immutable historical evidence;
- re-entry fails without exact proof identities;
- result serialization cannot be consumed as an execution plan;
- legacy bundle selection remains phase-appropriate and complete.

### Cost And Value

Separate unavoidable legacy execution, TPGR classification, identity
comparison, dual-run comparison, mismatch diagnosis, rollback rehearsal, and
maintenance cost. All R7 values are documentary/projected unless backed by an
already observed historical value. No projected saving authorizes activation.

## Acceptance Thresholds

- 6/6 canary design cases;
- 6/6 mismatch classes with deterministic outcomes;
- at least 4 Tier 1 and 3 Tier 2 rehearsals;
- 100% ambiguous rollback scopes promoted to Tier 1;
- zero TPGR-controlled legacy suppression/reorder/skip;
- zero TPGR-added enforcement;
- zero unknown/partial agreements;
- zero current eligibility from stale/unbound identity;
- all ten negative-test designs have expected outcomes;
- full cost separation with no projected saving presented as observed;
- exact two-path manifest and no commit;
- one allowed final disposition.

Any miss forbids the proceed disposition.

## Acceptance Criteria

- sources and exact identities are cited;
- comparator and mismatch schemas are deterministic;
- legacy outcome remains the sole controller;
- two-tier rollback and re-entry are fail-closed;
- H3 reviewer repair remains binding;
- R8 manifest is zero-edit and does not pre-authorize activation;
- required gates pass and reviewer independently accepts.

## Allowed Final Dispositions

- `PROCEED_TO_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`
- `REVISE_R7_DUAL_RUN_OR_ROLLBACK_DESIGN`
- `NARROW_TO_ROLLBACK_REHEARSAL_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md` | create complete comparison and rollback design assessment |
| `docs/reviews/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_WORKER_RETURN_2026-08-18.md` | create full worker-return evidence packet |

Forbidden paths: every other repository path. Do not stage or commit.

## Forbidden Actions

- edit any existing file;
- create any third output;
- stage, commit, push, or change Git configuration;
- create a harness, checker, fixture, test, schema, receipt, registry field,
  catalog row, config switch, or runtime plan;
- execute a canary or selective command plan;
- invoke provider/live/network/public-sync/deploy/production actions;
- authorize R8 or activation.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-R7",
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
  "claims": ["bounded dual-run canary and rollback rehearsal design"],
  "requiredProof": ["A1-A6 comparator cases", "six mismatch classes", "two-tier rollback rehearsal", "negative-test design", "cost separation", "full legacy gate"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["protected mutation", "source intake", "selective execution", "runtime or external effects"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: accepted design evidence only; no corpus claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, `P2_BOUNDED`, selective execution false,
and `RUN_FULL_LEGACY_BUNDLE`.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_WORKER_RETURN_2026-08-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package.

Use `N/A with reason` for non-applicable conditional blocks.

Required real sections include Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Checker Source Read-Ahead Block, Agent
Operation Trace Block, Delta Execution Claim Boundary Control Block, Public
Export Disposition, External Knowledge Intake Routing, every checker-required
hardening block, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Claim
Boundary, git status, Changed Files, Command Evidence, No-Commit Statement,
and exactly one design disposition.

## Worker Output Checker Read-Ahead Mandate

Before writing either output, read checker source for its docType, path family,
and triggered evidence classes. The assessment must satisfy baseline structural
groups. The worker return must derive all real headings, trace and delta
fields, external-intake/corpus/public/status/no-commit and every other
mandatory hardening literal, and first-run evidence shape from checker source.
Gate failures are not a substitute for read-ahead.

## Verification Commands

Required final commands:

```powershell
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --check
git status --short --untracked-files=all
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | prior critique already reconciled through R2G/R3/R4/R5/R6; R7 uses only accepted CVF artifacts |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | TPGR standard and accepted R2G-R6 evidence |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no new outside input, corpus registration, direct import, or authority promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: R7 evaluates a bounded set of committed design cases;
it does not refresh an external source or make a new corpus claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: the declared
case set is exactly C1-C6 plus mismatch and rollback scenarios, not a claim
that an upstream repository was fully absorbed.

## Finding-To-Governance Learning Disposition

Record a repeatable new defect only if semantic review finds one not already
owned by the cited rules. Otherwise use `N/A_WITH_REASON`.

## Epistemic Process Block

Expected Result / Prediction: a dual-run comparison can remain advisory while
making disagreements and rollback decisions deterministic.

Evidence Comparison: compare every proposed field and state transition against
R3-R6 authority and the unchanged legacy interlock.

Contradiction Or Gap Disposition: any path by which TPGR controls execution,
ambiguous scope stays class-local, or identity is assumed requires revision,
narrowing, or stop.

Claim Update: one allowed R7 disposition only; no active authority change.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external no-commit design worker followed by independent internal reviewer/closer |
| phase | R7 worker execution then independent review |
| baseHeadFor(phase) | dispatchBaseHead=`4c620f30d3bf716a8791be12c8ebec803fde414d`; executionBaseHead=worker captures clean post-continuity HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | worker exact two output paths; reviewer bounded corrections only in those paths; continuity separate |
| traceScope(phase, actor) | worker records reads, comparison method, commands, manifest, and no-commit evidence; reviewer independently recomputes and gates |
| commitOwner(phase) | reviewer/closer only; worker commit forbidden |
| crossBatchIsolation | no R8+, T15, source-intake, runtime, or external-effect lane may enter this batch |
| nextMoveSurfaces | reviewer updates active continuity only after material acceptance |

## Dual Agent Surface Matrix

| Surface | Role | Access | Disposition |
|---|---|---|---|
| INTERNAL_AGENT | dispatcher/reviewer/closer | author packet, review, commit, sync | ACTIVE |
| EXTERNAL_AGENT_CLI_MCP | no-commit worker | exact two documentation outputs only | AUTHORIZED_BOUNDED |
| adapter boundary | runtime bridge | none in R7 | NOT_AUTHORIZED |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_COMPLETION_2026-08-18.md` (optional reviewer-owned path; prefer an Independent Reviewer Addendum unless distinct closure evidence becomes necessary) |
| reviewerOwnedClosurePaths | exact two worker outputs; active continuity separately after acceptance |
| closureOwner | CVF reviewer/orchestrator |
| workerCommitPermission | FORBIDDEN |

Reviewer independently inspects all cases, mismatch and rollback logic, cost,
H3 binding, exact paths, hashes, and gates. Bounded repairs may touch only the
two worker outputs and must be disclosed. Material and continuity commits stay
separate.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/orchestrator as dispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | TPGR-R7 dispatch authoring, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold preview, resolver, collision checks, apply_patch, gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | accepted R6 disposition plus standing operator authorization |
| Before status evidence | clean worktree at `4c620f30d3bf716a8791be12c8ebec803fde414d` |
| After status evidence | exactly two dispatch artifacts before material commit |
| Diff evidence | `git status --short --untracked-files=all`; `git diff --check` |
| Approval boundary | documentation-only R7 comparison and rollback rehearsal design |
| Claim boundary | no implementation, canary execution, selective execution, or external effect |
| Agent type | reviewer/orchestrator dispatch author; external delegated worker follows |
| Invocation ID | `tpgr-r7-dispatch-authoring-2026-08-18` |
| Expected manifest | paired R7 baseline and work order at dispatch; exact two worker outputs at execution |
| Actual changed set | exactly paired R7 baseline and work order before dispatch commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R7 documentation-only comparison and rollback rehearsal design |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime enforcement, canary, or selective-command behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: accepted artifacts are evidence; no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two governed design artifacts and local verification commands only |
| invocationBoundary | local reads, documentary analysis, authoring, and governance gates |
| interceptionBoundary | no wrapper, proxy, runtime gate, CLI/MCP adapter, or coding interception |
| claimLanguage | proposed documentary comparison and rehearsal, not implemented behavior |
| forbiddenExpansion | no executable fixture, standard/checker/registry/catalog/hook/source/session edit by worker; no R8+, T15, runtime/provider/live/public/deploy/production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance design dispatch with no public artifact change.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | documentary comparison and rehearsal design only; no runtime, provider, live, canary, or selective behavior |

## Foundation Storage Layout Block

N/A with reason: R7 creates no durable foundation store, receipt directory,
cache, fixture tree, or persistence surface. Any such write is out of scope.

## Stop Conditions

Stop if exact sources are missing, output requires a third path, a real canary
or config switch is needed, legacy execution would be changed, rollback scope
is ambiguous but not global, or any external effect is required.

## Authority Chain

Operator standing authorization -> accepted R6 disposition -> paired R7
baseline/work order -> no-commit worker -> independent reviewer/closer. No
worker-authored comparison or rollback state becomes CVF authority before
review.

## Agent Roles

- Worker: reads, analyzes, authors exact two outputs, runs gates, does not commit.
- Reviewer/closer: independently checks sources, cases, mismatch outcomes,
  rehearsals, and costs; owns acceptance and commit.
- Operator: retains decisions that expand scope or open implementation and
  external effects; no checkpoint is needed for bounded worker execution.

## Pre-Flight Checks

1. `git rev-parse HEAD` equals supplied execution base.
2. `git status --short --untracked-files=all` is empty.
3. All Required First Reads exist.
4. Both output paths do not exist.
5. Run task route checker and full pre-implementation gate before editing.

## Intake Role Routing Decision

Intake summary: accepted CVF evidence only; no new source intake.

Scope classification: bounded documentation-only comparison and rehearsal.

Risk sensitivity: medium because execution authority is compared, but no
implementation or external effect is permitted.

Selected role route: `routeMode=MULTI_AGENT_SINGLE_ROLE`.

Role separation basis: worker produces evidence; reviewer independently
recomputes and owns commit.

Worker role: external no-commit design worker.

Reviewer role: internal CVF reviewer/closer.

Escalation condition: source contradiction, missing governed evidence,
required out-of-manifest write, or any acceptance-threshold miss.

Source authority: committed CVF artifacts named in Source Verification only.

Corpus action: bounded reads only; no source registration.

Direct import: forbidden.

## Write Ownership

Worker owns only the two fulfillment-manifest paths while uncommitted.
Reviewer owns corrections within those paths, staging, material commit, and
separate continuity. No shared simultaneous editing is allowed.

## Execution Plan

1. Preflight and source/checker read-ahead.
2. Freeze the C1-C6 inputs and identity evidence.
3. Build the comparator and resolve six mismatch classes.
4. Rehearse Tier 1 and Tier 2 rollback scenarios on paper.
5. Specify negative designs and separated cost accounting.
6. Reconcile thresholds, zero-edit R8 manifest, and one disposition.
7. Complete worker return and run required gates.
8. Leave exact two paths unstaged and return to reviewer.

## Evidence Requirements

Every comparison must cite objective facts and canonical owners. Every cost
cell must label observed, projected, or unknown and separate unavoidable
legacy work from TPGR overhead. Every rollback row must identify scope,
trigger, action, preserved evidence, and re-entry proof. Self-reported counts
are not evidence; tables must reconcile exactly.

## Review Gate

Reviewer must inspect the full assessment, independently recompute at least one
case from each archetype and every mismatch class, verify all thresholds,
rerun gates, and reject any proceed disposition depending on suppressed legacy
work, stale identity, ambiguous class scope, or invented savings.

## Operator Checkpoint

No checkpoint is required for exact worker execution. Any R8 dispatch remains
a fresh governed action after accepted R7 closure; implementation, selective
execution, or protected edits require separate authority.

## Closure Checklist

- exact two paths and zero staging;
- 6/6 cases and 6/6 mismatch classes;
- Tier 1/Tier 2 rehearsal floors;
- ten negative-test designs;
- H3 strict-route binding;
- one allowed disposition;
- worker-return fast, pre-implementation, and diff hygiene pass;
- independent reviewer acceptance before commit.

## Claim Boundary

This order authorizes documentary design only. It does not authorize actual
dual-run execution, selective gates, command suppression, rollback mutation,
implementation, R8, provider/live/network/public/deploy/production actions, or
any change outside the exact two worker outputs.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every required design element,
threshold, artifact, and gate is complete. Otherwise return
`BLOCKED_WITH_REASON` with the exact unmet requirement and no scope widening.

## Legacy Absorption Coverage Index Disposition

N/A with reason: R7 neither changes nor claims completion of a source corpus;
it evaluates a bounded governed case set and must not update absorption indexes.
