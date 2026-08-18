# CVF GC-018 Baseline - TPGR-R6 Historical Seeded-Defect Shadow Replay And Migration Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: TPGR-R6

Dispatch base head: `044a221f7eb82721fc7e4dc72786736dbe1f1336`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF reviewer/orchestrator

Worker target: delegated design worker

## Purpose

Run a documentation-only shadow replay of the accepted R3-R5 routing design
against six governed historical archetypes and seeded defects, then design a
non-promoting migration from historical evidence to the R4/R5 shadow fields.
No checker, receipt, registry, catalog, standard, router, or selective command
execution is implemented.

## Authorization / Source

R5 is independently accepted at
`d8699b713eec35d6f17b3e0820712247cd2b18b2`; its recorded final disposition is
`PROCEED_TO_R6_SHADOW_REPLAY_AND_MIGRATION_DESIGN`. Standing operator
authorization permits this fresh documentation-only R6 dispatch. It does not
authorize R6 implementation, R7, or selective execution.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R3 thresholds and replay floors | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`; commit `b029e61de` | RELEASED |
| R4 interface and claim vocabulary | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md`; commit `dbdc0888e` | RELEASED |
| R5 applicability, identity binding, and invalidation | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md`; worker return; commit `d8699b713` | RELEASED |
| selective execution | TPGR remains shadow-only; phase-appropriate legacy bundle remains mandatory | NOT_AUTHORIZED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R6 --title "Historical Seeded-Defect Shadow Replay And Migration Design" --date 2026-08-18 --base 044a221f7eb82721fc7e4dc72786736dbe1f1336 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact historical fixtures, replay contract, seeded-defect matrix, migration rules, thresholds, and two-path manifest |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `replayCaseId`, `fixtureClass`, `expectedRoute`, `observedShadowRoute`, `migrationDisposition`, `identityComparisonCost` |
| claimBoundary | dispatch provenance only; no executable fixture, checker, route, receipt, or runtime behavior |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | exact fixtures and paths, checker read-ahead, no authority aggregation, honest first-run evidence, no-commit ownership, and reviewer-independent replay are mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | dispatch-ready status; Source Verification columns; scaffold fields; task routing JSON; no-commit terms; baseline/review structural groups; worker-return headings and status literals |
| gateRunPurpose | confirmation after source-led authoring, not first discovery |
| claimBoundary | structural conformance only; replay semantics remain reviewer-owned |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R6 is the accepted next design step | predecessor disposition | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | Final Disposition; Zero-Edit R6 Candidate Manifest | assessment path | accepted R5 design | ACCEPT |
| six historical archetypes and proof floors exist | replay fixture authority | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | A1-A6 Threshold Worksheets; Proof Floors; Dependency Invalidation Graph | assessment path | accepted R3 design | ACCEPT |
| shadow fields and exact tokens are fixed inputs | migration source | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | Shadow Interface Field Table; Exact Claim Vocabulary | assessment path | accepted R4 design | ACCEPT |
| identity-bound freshness and phase-aware cost are binding | replay contract | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | Identity-Binding Contract; Cost Proof; Hostile Cases | assessment path | accepted R5 design | ACCEPT |
| TPGR remains shadow-only | authority fact | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock; Activation Rule | standard path | TPGR standard | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact four R6 lifecycle paths | `Test-Path` returned false for baseline, work order, assessment, and worker-return paths before authoring | PASS |
| namespace collision | exact token search under `docs` and `CVF_SESSION` returned no prior artifact | PASS |
| collision decision | exact namespace available | CREATE_NEW |

## Design Contract

R6 must produce actual documentation-only replay results and a migration
design, not executable routing:

1. Replay A1-A6 against the accepted R3 proof floors, R4 interface, and R5
   applicability/invalidation rules using committed historical artifacts.
2. Separate `expectedRoute` from independently derived `observedShadowRoute`;
   never rewrite historical outcomes to make them agree.
3. Seed every R5 hostile case, the six R5 false-positive boundary classes,
   and the three R5 reviewer-repair defects. Record deterministic detection,
   route, preserved evidence, and earliest invalidation scope.
4. Require 100% recall for material authority, semantic-completion,
   self-downgrade, stale-receipt, and scope-widening defects; zero false
   activation across all six declared false-positive classes; no unknown fact
   may light-route.
5. Design a migration table from historical evidence into all eight R4 fields
   and six R5 candidate fields. Missing identity or authority binds to
   `NEEDS_FRESH_EVIDENCE` or `HISTORICAL_ONLY`, never synthetic `CURRENT`.
6. Measure replay work separately as Layer A evidence cost, TPGR comparison
   overhead, escalation cost, and duplicate discovery/replay. Do not call
   unknown or projected cost a saving.
7. Preserve the A3 bounded positive-reuse case without repeating full-corpus
   enumeration or weakening semantic reading of the named cluster.
8. Produce a zero-edit R7 dual-run canary/rollback-rehearsal candidate manifest
   and exactly one allowed final disposition.

No fixture, standard, checker, registry, catalog, receipt store, hook, session
surface, source corpus, or runtime code may be created or changed by the worker.

## Proposed Tranche

One no-commit external design worker creates exactly one R6 assessment and one
worker return. The reviewer independently replays representative rows,
inspects all seeded cases, repairs only those two paths if bounded, and owns
any commit and continuity transition.

## Evidence / Verification

Evidence must include an exact fixture inventory, A1-A6 replay worksheets,
seeded-defect and false-positive matrices, all 14-field migration rows, cost
separation, R7 zero-edit manifest, actual worktree status, worker-return fast
gate, full pre-implementation gate, and no-commit proof.

## Stop Conditions

Return revision, narrowing, or stop if R6 rewrites history, fabricates missing
identity, lets any material defect light-route, promotes cluster evidence to a
corpus claim, triggers on declared false-positive prose/archive/code examples,
repeats full-corpus work for A3 without a named invalidator, counts Layer A
evidence as TPGR savings, creates a second truth store, or enables selective
execution.

## Allowed Final Dispositions

- `PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN`
- `REVISE_R6_REPLAY_OR_MIGRATION_DESIGN`
- `NARROW_TO_REPLAY_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/orchestrator as dispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | TPGR-R6 dispatch authoring, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold preview, resolver, collision checks, apply_patch, gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | accepted R5 disposition plus standing operator authorization |
| Before status evidence | clean at `044a221f7eb82721fc7e4dc72786736dbe1f1336` |
| After status evidence | exactly two dispatch artifacts before material commit |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | documentation-only R6 replay and migration design dispatch |
| Claim boundary | no implementation, source mutation, or external effect |
| Agent type | internal reviewer/orchestrator |
| Invocation ID | `tpgr-r6-dispatch-2026-08-18` |
| Expected manifest | this baseline; paired work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R6 documentation-only dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime execution-control, receipt enforcement, or selective-command behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two governed dispatch artifacts and local gates only |
| invocationBoundary | local documentation and governance gates |
| interceptionBoundary | no wrapper, proxy, runtime gate, CLI/MCP adapter, or coding interception |
| claimLanguage | replay/migration design authority only |
| forbiddenExpansion | no standard/checker/registry/catalog/hook/source/session mutation by worker; no R7+, T15, runtime/provider/live/public/deploy/production action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; public sync is outside scope.

## Claim Boundary

This baseline authorizes only two R6 documentation outputs and read-only
analysis of committed evidence. It does not authorize executable fixtures,
implementation, migration mutation, command omission, R7-R9, T15, source
intake, runtime, provider/live, public sync, deployment, or production.
