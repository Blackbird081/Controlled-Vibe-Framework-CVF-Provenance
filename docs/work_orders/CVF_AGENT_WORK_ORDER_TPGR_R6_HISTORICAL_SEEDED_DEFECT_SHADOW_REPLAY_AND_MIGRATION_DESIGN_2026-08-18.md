# CVF Agent Work Order - TPGR-R6 Historical Seeded-Defect Shadow Replay And Migration Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Batch ID: TPGR-R6

Dispatch base head: `044a221f7eb82721fc7e4dc72786736dbe1f1336`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated design worker

Reviewer/closer: CVF reviewer/orchestrator

Worker return path: `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md`

## Dispatch Prompt Envelope

Role: delegated no-commit design worker for TPGR-R6.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse HEAD` at start; it must equal the
clean post-dispatch-continuity HEAD supplied by the operator.

Current-time notes: artifact date is 2026-08-18; verify current repository
state locally and do not use provider memory as authority.

Do-not-misread notes: this is documentation-only historical replay and
migration design. It authorizes no checker/fixture implementation, receipt
persistence, selective command omission, R7, source intake, or external effect.

Required first actions: verify clean worktree and exact HEAD; read the paired
baseline, this work order, startup surfaces, guard orientation, literal
gotchas, every Required First Read, and applicable checker source before
writing. Run the two preflight commands before the first edit.

Return contract: create exactly the two authorized output files, run all
required gates, leave them uncommitted and unstaged, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Independently shadow-replay the accepted R3-R5 design against governed
historical A1-A6 evidence and seeded defects, then design a fail-closed,
non-promoting migration of historical evidence into the R4/R5 field model.
The result must expose whether the design catches known failures and preserves
the A3 reuse saving without weakening any current guard.

## Worker Autonomy / No-Question Rule

Repair checker-shape or contract defects directly only inside the two allowed
paths. Return early only for a source contradiction, missing authority, or a
required write outside the exact manifest. Do not invent evidence or widen
scope to avoid a block.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R5 accepted material | R5 assessment and worker return; commit `d8699b713eec35d6f17b3e0820712247cd2b18b2` | RELEASED |
| R5 closure continuity | `CVF_SESSION/state/entries/tpgrR5ShadowCommandApplicabilityAndReceiptInvalidationDesignClosed20260818.json`; commit `044a221f7` | RELEASED |
| R7 and selective execution | outside this tranche | NOT_AUTHORIZED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R6 --title "Historical Seeded-Defect Shadow Replay And Migration Design" --date 2026-08-18 --base 044a221f7eb82721fc7e4dc72786736dbe1f1336 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact sources, replay corpus, seeded cases, migration rules, thresholds, manifests, and role boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `replayCaseId`, `fixtureClass`, `expectedRoute`, `observedShadowRoute`, `migrationDisposition`, `identityComparisonCost` |
| claimBoundary | dispatch provenance only; no executable route, fixture, receipt, or migration behavior |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | source fidelity, exact manifest, honest gate evidence, anti-aggregation, checker read-ahead, and independent reviewer replay are mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | dispatch-ready status; mandatory work-order groups; Source Verification columns; no-commit terms; task governance JSON; worker-return headings, trace fields, delta/public/corpus/status and every other hardening literal |
| gateRunPurpose | confirmation and evidence after source-led authoring |
| claimBoundary | structural conformance only; semantic replay acceptance remains reviewer-owned |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R6 next-step authority | predecessor disposition | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | Final Disposition; Zero-Edit R6 Candidate Manifest | assessment path | accepted R5 design | ACCEPT |
| historical archetypes and thresholds | replay authority | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | A1-A6 Worksheets; Proof Floors; Hostile Test Matrix | assessment path | accepted R3 design | ACCEPT |
| eight fields, eight tokens, false-positive classes | replay interface | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | Shadow Interface; Exact Claim Vocabulary; Hostile Cases | assessment path | accepted R4 design | ACCEPT |
| applicability, identity, invalidation, cost boundaries | replay evaluator | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | Applicability Matrix; Identity-Binding Contract; Invalidation Precedence; Cost Proof | assessment path | accepted R5 design | ACCEPT |
| shadow-only legacy interlock | authority boundary | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock; Activation Rule | standard path | TPGR standard | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact four R6 paths | all returned false under `Test-Path` before authoring | PASS |
| namespace collision | exact token search under `docs` and `CVF_SESSION` returned no prior artifact | PASS |
| collision decision | exact new namespace available | CREATE_NEW |

## Required First Reads

Read fully unless a targeted section is explicitly named:

1. paired R6 baseline and this work order;
2. bootstrap read model, `CVF_SESSION_MEMORY.md`, and active handoff;
3. guard orientation and literal-format gotchas;
4. R2G assessment's six archetype worksheets and evidence summary;
5. R3 Route Outcomes, A1-A6 Worksheets, Proof Floors, Cost Ceilings,
   Dependency Invalidation Graph, Hostile Matrix, and reviewer addendum;
6. R4 assessment in full and its worker-return reviewer addendum;
7. R5 assessment in full and its worker-return reviewer addendum;
8. TPGR standard Mandatory Classification, Mandatory Escalation, legacy
   interlock, Activation Rule, and rollback sections;
9. `governance/compat/agent_autorun_command_catalog.py` in full;
10. applicable checker source for both outputs before authoring them.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/assessments/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md` | create complete replay results and migration design assessment |
| `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md` | create full worker-return evidence packet |

Forbidden paths: every other repository path. Do not stage or commit.

## Replay And Migration Contract

The assessment must include all of the following:

1. An exact historical fixture inventory with one governed case for each A1-A6,
   preserving source commit/path and accepted historical disposition.
2. Six replay worksheets containing `replayCaseId`, `fixtureClass`, historical
   outcome, objective facts, inherited/refreshed evidence, expected route,
   independently derived `observedShadowRoute`, mismatches, Layer A cost,
   TPGR comparison overhead, escalation cost, and replay verdict.
3. A seeded-defect matrix covering all twelve R5 hostile cases plus the three
   reviewer-repair cases: unbound receipt identity, incorrect phase-cost
   accounting, and contradictory gate evidence.
4. A false-positive replay matrix for descriptive prose, taxonomy tables,
   archived history, code fences, quoted examples, and incomplete drafts.
5. A migration table covering all eight R4 fields and all six R5 fields for
   every fixture. Historical evidence is immutable; migration may reference
   it but may never rewrite it or synthesize `CURRENT`.
6. Exact migration dispositions:
   `MIGRATABLE_CURRENT_WITH_IDENTITY`, `NEEDS_FRESH_EVIDENCE`,
   `HISTORICAL_ONLY`, `NOT_APPLICABLE_WITH_REASON`, or
   `BLOCKED_CONTRADICTORY_EVIDENCE`.
7. Identity comparison must use R5's immutable owner, semantic-dependency,
   catalog-row, and confirming-review bindings. Missing closure or identity
   routes to `FULL_LAYER_A_REQUIRED`, never a guessed match.
8. Cost accounting must keep unavoidable Layer A work outside TPGR savings,
   record `identityComparisonCost`, and classify unmeasured values as
   `UNKNOWN`/`PROJECTED`.
9. A3 must demonstrate bounded receipt reuse without repeating full-corpus
   enumeration or inheriting semantic understanding of a new cluster.
10. A zero-edit R7 candidate manifest for dual-run advisory comparison and
    rollback rehearsal, plus exactly one allowed final disposition.

The replay is documentary/manual shadow evaluation only. Do not create test
fixtures, scripts, checkers, receipts, schemas, registry fields, catalog rows,
or runtime plans that execute commands selectively.

## Required Historical Replay Cases

| Case | Archetype | Minimum fixture authority | Required posture |
|---|---|---|---|
| H1 | A1 new upstream corpus | R2G/R3 A1 worksheet and its governed cited evidence | full first-intake floor preserved; no inheritance saving claimed |
| H2 | A2 mixed-origin synthesis | R2G/R3 A2 worksheet | dual-origin separation and selected-cluster semantic reading preserved |
| H3 | A3 accepted-corpus cluster | R2G/R3 A3 worksheet plus an accepted named-cluster cycle | positive reuse case; no full-corpus re-enumeration |
| H4 | A4 upstream delta | R2G/R3 A4 worksheet | delta-scope re-read and earliest-node invalidation preserved |
| H5 | A5 advisory item | R2G/R3 A5 worksheet and reconciled critique chain | advisory authority boundary; near-zero extra ceremony |
| H6 | A6 downstream project source | R2G/R3 A6 worksheet and GC-051 Rule 5 evidence | registration never promotes project material to CVF authority |

Do not select easier substitutes. If a named historical fixture cannot be
verified from governed evidence, mark that row blocked and choose a non-proceed
disposition rather than inventing it.

## Required Seeded Defect And Negative Cases

Seed and resolve all twelve R5 hostile cases without modifying source files.
Additionally seed:

- same path and catalog row, but missing checker semantic-dependency identity;
- a catalog command whose arguments changed while its stable name remained;
- a role label still valid while the confirming review artifact was revised;
- pre-push commands incorrectly charged to a pre-implementation replay;
- worker summary saying first-pass success while detailed evidence says fail;
- one absent identity fact paired with worker-declared low uncertainty.

Each seeded case must record expected detection, actual shadow determination,
route, preserved historical evidence, invalidation scope, and pass/fail. Every
material defect must be detected; none may select `LIGHT_ROUTE_ALLOWED`.

## Acceptance Thresholds

- historical fixture coverage: 6/6;
- material seeded-defect recall: 100%; false negatives: 0;
- declared false-positive class activations: 0/6;
- unknown/missing/contradictory facts routed light: 0;
- authority contamination or completion-claim laundering: 0;
- migration-created or upgraded `CURRENT` claims without identity: 0;
- R4 fields reconciled: 8/8; R5 candidate fields reconciled: 6/6;
- A3 repeats of full-corpus enumeration absent a corpus-level invalidator: 0;
- Layer A evidence counted as TPGR savings: 0;
- phase-inapplicable command cost charged to a fixture: 0;
- all mismatches disclosed; no historical outcome rewritten;
- full phase-appropriate legacy bundle remains mandatory.

Any threshold miss forbids the proceed disposition.

## Acceptance Criteria

- exact two-path worker output manifest, staged zero, and no worker commit;
- 6/6 historical fixtures with source identity and preserved historical result;
- every Acceptance Threshold met and independently reproducible;
- all fourteen migration fields reconciled without synthetic currency;
- identity closure is immutable and missing identity fails closed;
- cost separates Layer A, TPGR comparison, escalation, and duplicate work;
- A3 preserves bounded reuse without inherited semantic understanding;
- zero-edit R7 manifest and exactly one allowed disposition;
- required gates pass and reviewer independently accepts.

## Allowed Final Dispositions

- `PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN`
- `REVISE_R6_REPLAY_OR_MIGRATION_DESIGN`
- `NARROW_TO_REPLAY_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external no-commit design worker followed by independent internal reviewer/closer |
| phase | R6 worker execution then independent review |
| baseHeadFor(phase) | dispatchBaseHead=`044a221f7eb82721fc7e4dc72786736dbe1f1336`; executionBaseHead=worker captures clean post-continuity HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | worker exact two output paths; reviewer bounded corrections only in those paths; continuity separate |
| traceScope(phase, actor) | worker records reads, replay method, commands, manifest, and no-commit evidence; reviewer independently replays and gates |
| commitOwner(phase) | reviewer/closer only; worker commit forbidden |
| crossBatchIsolation | no R7+, T15, RSPB, source-intake, runtime, or external-effect lane may enter this batch |
| nextMoveSurfaces | reviewer updates active continuity only after material acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_COMPLETION_2026-08-18.md` (optional reviewer-owned path; prefer an Independent Reviewer Addendum unless distinct closure evidence becomes necessary) |
| reviewerOwnedClosurePaths | exact two worker outputs; active continuity separately after acceptance |
| closureOwner | CVF reviewer/orchestrator |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing either output, read checker source for its docType, path family,
and triggered evidence classes. The assessment must satisfy baseline structural
groups. The worker return must derive all real headings, trace/delta fields,
external-intake/corpus/public/status/no-commit and every other mandatory
hardening literal, and first-run
evidence shape from checker source. Gate failures are not a substitute for
read-ahead.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections include Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Checker Source Read-Ahead Block, Agent
Operation Trace Block, Delta Execution Claim Boundary Control Block, Public
Export Disposition, External Knowledge Intake Routing, every checker-required
hardening block, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Claim
Boundary, git status, Changed Files, Command Evidence, and No-Commit Statement.

## Verification Commands

Run from repository root after authoring both outputs:

```powershell
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --check
git status --short --untracked-files=all
```

No individual checker substitutes for the full fast gate. Record every first
failure and repair honestly; do not overwrite failed evidence with a final-only
summary.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated design worker, then independent reviewer/closer |
| Provider or surface | operator-transferred external worker; local private provenance workspace |
| Session or invocation | TPGR-R6 replay and migration design, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, manual documentary replay, local git inspection, Python governance commands, file authoring |
| Target paths | exact two output paths in fulfillment manifest |
| Allowed scope source | paired R6 baseline and this work order |
| Before status evidence | clean worktree and captured executionBaseHead required before edits |
| After status evidence | exactly two untracked output paths |
| Diff evidence | `git status --short --untracked-files=all`; `git diff --check` |
| Approval boundary | documentation-only R6 replay and migration design |
| Claim boundary | no implementation, source mutation, selective execution, or external effect |
| Agent type | external delegated worker |
| Invocation ID | `tpgr-r6-worker-execution-2026-08-18` |
| Expected manifest | exact two output paths |
| Actual changed set | worker fills from actual status |
| Manifest delta | must be MATCH or return blocked |
| Deletion or rename disposition | N/A with reason unless evidence differs, which blocks completion |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R6 documentation-only historical replay and migration design |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime enforcement, receipt admission, or selective-command behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: historical artifacts are read as evidence; no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two governed design artifacts and local verification commands only |
| invocationBoundary | local reads, documentary replay, authoring, and governance gates |
| interceptionBoundary | no wrapper, proxy, runtime gate, CLI/MCP adapter, or coding interception |
| claimLanguage | observed historical comparison plus proposed migration design, not implemented behavior |
| forbiddenExpansion | no executable fixture, standard/checker/registry/catalog/hook/source/session edit by worker; no R7+, T15, runtime/provider/live/public/deploy/production |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | critique already reconciled through R2G/R3/R4/R5; R6 replays only accepted CVF artifacts |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | TPGR standard and accepted R2G-R5 evidence |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no new outside input, corpus registration, direct import, or authority promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: R6 replays a bounded, predeclared set of committed
historical fixtures and seeded design cases; it does not refresh an external
source or make a new corpus completeness claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: fixture
coverage is exactly the six archetypes and declared seeded cases, not a claim
that any source repository was rescanned or fully absorbed.

## Finding-To-Governance Learning Disposition

Record any new repeatable defect with a checker-accepted defect class and
learning lane. If none exists, use N/A_WITH_REASON. Contradictory first-run
gate evidence is itself a finding and must not be silently normalized away.

## Epistemic Process Block

Expected Result / Prediction: R3-R5 rules should reproduce fail-closed
historical outcomes, catch every seeded material defect, avoid the six false
positives, and preserve the A3 bounded reuse case without duplicate corpus work.

Evidence Comparison: compare expected versus observed shadow routes, field
migration eligibility, identity closure, and separated cost for every fixture.

Contradiction Or Gap Disposition: any missed material defect, false current
claim, false positive, rewritten history, or negative A3 value requires
revision, narrowing, or stop.

Claim Update: one allowed R6 disposition only; no active authority changes.

## Foundation Storage Layout Block

N/A with reason: R6 creates no receipt store, fixture directory, cache, or
persistence surface. Any required storage is an out-of-scope blocker.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | documentary replay of committed evidence only; no runtime/provider/live/selective behavior |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design work; no public-sync authority.

## Claim Boundary

This work order authorizes exactly two documentation outputs and read-only
analysis of committed evidence. It does not authorize executable replay
fixtures, implementation, migration mutation, standards/checkers/registries/
catalogs/hooks/session edits by the worker, source intake, R7-R9, T15,
selective execution, runtime, provider/live, public sync, deployment,
production, or destructive action.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-R6",
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
  "claims": ["bounded historical shadow replay and migration design"],
  "requiredProof": ["A1-A6 replay", "seeded defects", "false-positive matrix", "14-field migration", "cost separation", "full legacy gate"],
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

## Authority Chain

Operator standing authorization -> accepted R5 disposition -> paired R6
baseline/work order -> no-commit worker -> independent reviewer/closer. No
worker-authored route or migration state becomes CVF authority before review.

## Agent Roles

- Worker: reads, replays, authors exact two outputs, runs gates, does not commit.
- Reviewer/closer: independently checks sources/routes/costs, may repair only
  bounded defects in the two outputs, owns acceptance and commit.
- Operator: retains decisions that expand scope or open implementation/external
  effects; no such checkpoint is needed for the bounded worker execution.

## Pre-Flight Checks

1. `git rev-parse HEAD` equals supplied execution base.
2. `git status --short --untracked-files=all` is empty.
3. All Required First Reads exist.
4. Both output paths do not exist.
5. Run task route checker and full pre-implementation gate before editing.

## Intake Role Routing Decision

Intake summary: accepted CVF evidence only; no new source intake.

Scope classification: bounded documentation-only replay and migration design.

Risk sensitivity: medium because completion/authority claims are replayed, but
no implementation or external effect is permitted.

Selected role route: `routeMode=MULTI_AGENT_SINGLE_ROLE`.

Role separation basis: worker produces evidence; reviewer independently
recomputes and owns commit.

Worker role: external no-commit design worker.

Reviewer role: internal CVF reviewer/closer.

Escalation condition: source contradiction, missing governed fixture, required
out-of-manifest write, or any acceptance-threshold miss.

Source authority: committed CVF artifacts named in Source Verification only.

Corpus action: no scan or registration; bounded historical fixture reads.

Direct import: forbidden.

## Write Ownership

Worker owns only the two fulfillment-manifest paths while uncommitted.
Reviewer owns corrections within those paths, staging, material commit, and
separate continuity. No shared simultaneous editing is allowed.

## Execution Plan

1. Preflight and source/checker read-ahead.
2. Freeze the exact H1-H6 fixture inventory before evaluating routes.
3. Replay six historical worksheets without changing historical outcomes.
4. Evaluate all seeded and false-positive cases.
5. Build the 14-field migration matrix and cost accounting.
6. Reconcile thresholds, R7 zero-edit manifest, and one disposition.
7. Complete worker return and run required gates.
8. Leave exact two paths unstaged and return to reviewer.

## Evidence Requirements

Every route must cite objective facts and canonical owners. Every cost cell
must label observed/projected/unknown and separate Layer A from TPGR overhead.
Every migration cell must name its disposition and missing identity, if any.
Self-report counts are not evidence; tables must reconcile exactly.

## Review Gate

Reviewer must inspect the full assessment, independently replay at least one
case from each archetype and every material seeded-defect class, verify all
counts/thresholds, rerun gates, and reject any proceed disposition that depends
on invented identity, hidden Layer A cost, or rewritten history.

## Operator Checkpoint

No checkpoint is required for exact worker execution. Any R7 dispatch remains
a fresh governed action after accepted R6 closure; implementation, selective
execution, or protected edits require separate authority.

## Closure Checklist

- exact two-path manifest;
- execution base and staged-zero evidence;
- 6/6 historical replay;
- seeded/false-positive thresholds reconciled;
- 8/8 plus 6/6 migration coverage;
- cost separation and A3 positive case;
- one allowed disposition;
- worker-return fast, pre-implementation, diff hygiene PASS;
- independent reviewer acceptance before commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every required artifact, matrix,
threshold, and gate is complete. Otherwise return `BLOCKED_WITH_REASON` naming
the exact missing source, contradiction, threshold miss, or forbidden path.

## Legacy Absorption Coverage Index Disposition

N/A with reason: R6 neither changes nor claims completion of a source corpus;
it replays a bounded governed fixture set and must not update absorption indexes.
