# CVF GC-018 Baseline - TPGR-R4 Shadow Interface And Claim Vocabulary Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: TPGR-R4

Dispatch base head: `783cf1e96cb634beb6bc2b2b119f8a0d8d8a67a3`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF reviewer/orchestrator

Worker target: delegated design worker

## Purpose

Design, without implementing, the smallest shadow interface that binds the
accepted R3 thresholds to CVF's existing absorption lifecycle and an exact
stage-safe claim vocabulary. Prevent cluster-level evidence from being
laundered into corpus-level absorption claims.

## Authorization / Source

Operator standing authorization on 2026-08-18 permits the reviewer/orchestrator
to continue through CVF-allowed next steps without repeated micro-approval.
R3 is closed at `b029e61de9c44bcb428debb2627d283995a53966` with final
disposition `PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN`.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R3 threshold design | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`; commit `b029e61de9c44bcb428debb2627d283995a53966` | SATISFIED |
| Operator authority | standing instruction to proceed under CVF rules | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R4 --title "Shadow Interface And Claim Vocabulary Design" --date 2026-08-18 --base 783cf1e96cb634beb6bc2b2b119f8a0d8d8a67a3 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with R4 authority, exact two-path manifest, shadow-interface contract, claim vocabulary, hostile cases, and closure boundaries |
| checkerReadAheadConfirmation | dispatch, read-ahead, structural, trace, handoff, public-disposition, and worker-return checkers reviewed |
| docOnlyNewFields | `intakeStage`; `claimToken`; `claimScopeRef`; `evidenceRefs`; `invalidatedBy`; `reviewAuthority`; `routeOutcome`; `eligibilityState` |
| claimBoundary | provenance for documentation-only dispatch; no implementation or runtime behavior claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22 results, not truncated.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Disclosed defectIds | same exact 22 IDs |
| Dispatch impact | keep claims scope-exact, authority source-bound, paths collision-checked, outputs exact, worker no-commit, and implementation parked |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `COMPLETE_PENDING_REVIEW`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation after checker-source inspection, not first discovery |
| claimBoundary | packet-shape evidence only; semantic correctness remains independently reviewable |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R3 authorizes only a future R4 decision | predecessor authority | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Decision; Final Disposition; Claim Boundary | `PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN` | R3 closure contract | ACCEPT |
| R4 is shadow interface and claim vocabulary design | roadmap authority | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Revised Delivery Sequence | R4 row | TPGR second-upgrade sequence | ACCEPT |
| R3 proposes a threshold reference and escalation-only uncertainty evaluation | design evidence | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | R4 Candidate Delta Manifest | candidate standard rows | R3 zero-edit manifest | ACCEPT |
| Stage claims require scope-safe vocabulary | reconciled advisory input | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md` | Semantic Completeness Vocabulary; Binding Rules | eight claim tokens | advisory input through accepted reconciliation | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact four R4 paths | `Test-Path` returned false for baseline, work order, assessment, and worker-return targets before authoring | PASS |
| Token collision search | `rg -n "TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN" docs CVF_SESSION` returned no prior artifact | PASS |
| Collision decision | exact new namespace is available | CREATE_NEW |

## Design Contract

R4 must specify a documentation-only shadow interface, not edit the active
standard. It must:

- bind S0-S8 stage identifiers by reference to existing CVF owners;
- define exactly eight claim tokens: `SOURCE_REGISTERED`,
  `STRUCTURALLY_ENUMERATED`, `LEDGER_DISPOSITIONED`, `TRIAGE_CLASSIFIED`,
  `CLUSTER_SEMANTICALLY_READ`, `CAPABILITY_ABSORBED`,
  `CORPUS_SEMANTICALLY_ABSORBED`, and `DELTA_ACCOUNTED`;
- prevent aggregation from promoting cluster claims to corpus claims;
- make any uncertainty signal escalation-only;
- bind claim scope, evidence refs, invalidators, review authority, route
  outcome, and eligibility without creating a second truth store;
- design negative/hostile cases for claim laundering, stale receipt reuse,
  missing scope, unknown token, and worker self-downgrade;
- name exact candidate R5/R6 implementation targets while editing none.

## Proposed Tranche

One no-commit design worker creates exactly the assessment and worker return;
an independent reviewer verifies and owns any repair and commit.

## Evidence / Verification

Evidence is the accepted R3 commit, source-verification table, collision
checks, resolver result, full pre-dispatch gate, reviewer-fast gate,
commit-steward preflight, exact manifest, and diff hygiene.

## Stop Conditions

Return revision or stop if the design duplicates the absorption lifecycle,
requires a new registry/catalog, permits worker-controlled downgrade, implies
corpus understanding from a ledger or cluster receipt, cannot invalidate an
upstream-drifted claim, or cannot remain smaller than Layer A.

## Allowed Final Dispositions

- `PROCEED_TO_R5_SHADOW_COMMAND_AND_RECEIPT_INVALIDATION`
- `REVISE_R4_INTERFACE`
- `NARROW_TO_CLAIM_VOCABULARY_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | reviewer/orchestrator as dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | TPGR-R4 dispatch, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, resolver, collision checks, scaffold preview, governance gates |
| Target paths | exact baseline and work-order paths |
| Allowed scope source | operator standing authorization plus accepted R3 disposition |
| Before status evidence | clean HEAD `783cf1e96cb634beb6bc2b2b119f8a0d8d8a67a3` |
| After status evidence | exact two dispatch paths only |
| Diff evidence | untracked-aware Git status and exact manifest check |
| Approval boundary | documentation-only R4 dispatch |
| Claim boundary | no implementation, selective execution, runtime, provider/live, public, deploy, or production claim |
| Agent type | reviewer/orchestrator |
| Invocation ID | tpgr-r4-dispatch-2026-08-18 |
| Expected manifest | exact baseline and work-order paths |
| Actual changed set | exact baseline and work-order paths |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only R4 dispatch |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | local reads and dispatch authoring only |
| interceptionBoundary | no wrapper, proxy, hook, runtime gate, or agent-control interception |
| claimLanguage | design authority only |
| forbiddenExpansion | implementation, R5-R9 execution, T15, protected edits, new intake, runtime/provider/live/public/deploy/production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only design dispatch.

## Claim Boundary

This baseline authorizes exactly R4 design assessment and worker return. It
does not authorize standard/checker/registry/catalog/hook edits, selective
execution, source intake, implementation, R5-R9, T15, runtime/provider/live,
public-sync, deployment, or production.
