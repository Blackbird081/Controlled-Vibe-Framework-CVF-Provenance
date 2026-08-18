# CVF GC-018 Baseline - TPGR-R7 Dual-Run Canary And Rollback Rehearsal Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: TPGR-R7

Dispatch base head: `4c620f30d3bf716a8791be12c8ebec803fde414d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF reviewer/orchestrator

Worker target: delegated design worker

## Purpose

Design, without executing, a dual-run advisory canary and deterministic
rollback rehearsal for TPGR. The design must compare a proposed TPGR shadow
route with the existing phase-appropriate legacy gate outcome while preserving
the legacy bundle as the only enforcement authority.

## Authorization / Source

R6 is independently accepted at `27e87a1ca`; its final disposition is
`PROCEED_TO_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN`. Standing
operator authorization permits this fresh documentation-only R7 dispatch.
It does not authorize a harness, live canary, selective execution, R8, or
activation.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R3 route precedence and rollback floors | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | RELEASED |
| R4 interface and claim vocabulary | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | RELEASED |
| R5 identity, applicability, and invalidation | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | RELEASED |
| R6 replay and migration evidence | `docs/assessments/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md`; commit `27e87a1ca` | RELEASED_WITH_H3_STRICT_ROUTE |
| selective execution | TPGR remains advisory; full phase-appropriate legacy bundle remains mandatory | NOT_AUTHORIZED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R7 --title "Dual-Run Canary And Rollback Rehearsal Design" --date 2026-08-18 --base 4c620f30d3bf716a8791be12c8ebec803fde414d --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with comparator schema, canary cases, mismatch policy, two-tier rollback rehearsal, thresholds, and exact two-path manifest |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
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

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | dispatch-ready status; Source Verification columns; scaffold fields; task routing JSON; no-commit terms; baseline/review structural groups; worker-return headings and status literals |
| gateRunPurpose | confirmation after source-led authoring, not first discovery |
| claimBoundary | structural conformance only; canary and rollback semantics remain reviewer-owned |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R7 is the accepted next design step | predecessor disposition | `docs/assessments/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_2026-08-18.md` | Final Disposition; Zero-Edit R7 Candidate Manifest | assessment path | accepted R6 design | ACCEPT |
| mismatch precedence is fail-closed | route authority | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Route Outcomes And Deterministic Precedence; rollback floors | assessment path | accepted R3 design | ACCEPT |
| identity and invalidation are bound inputs | comparison authority | `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | Identity-Binding Contract; Invalidation Precedence | assessment path | accepted R5 design | ACCEPT |
| H3 cannot light-route without current identity | reviewer repair | `docs/reviews/CVF_TPGR_R6_HISTORICAL_SEEDED_DEFECT_SHADOW_REPLAY_AND_MIGRATION_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum | worker-return path | accepted R6 review | ACCEPT |
| legacy gates remain authoritative | interlock authority | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock; Activation Rule | standard path | TPGR standard | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact four R7 lifecycle paths | `Test-Path` returned false for baseline, work order, assessment, and worker-return paths before authoring | PASS |
| namespace collision | exact R7 token search found no prior lifecycle artifact | PASS |
| collision decision | exact namespace available | CREATE_NEW |

## Design Contract

R7 must produce a documentation-only canary and rollback design:

1. Define a comparator record that keeps legacy observed evidence and TPGR
   advisory evidence separate and identity-bound.
2. Use at least six design cases covering A1-A6, including H3 as
   `ESCALATE_FOR_REVIEW` until identity is freshly proven.
3. Define mismatch classes for advisory-lighter, advisory-stricter,
   identity/freshness ambiguity, catalog/checker drift, timeout/partial result,
   and evidence contradiction.
4. The legacy result always controls. TPGR output cannot suppress, skip,
   reorder, shorten, or reinterpret a legacy command.
5. Rehearse Tier 1 global rollback and Tier 2 class-scoped rollback on paper.
   Ambiguous scope defaults to Tier 1.
6. Define deterministic stop, rollback, preservation, and re-entry evidence.
   Re-entry requires the full R6/R7 path; timestamps or copied receipts do not
   restore eligibility.
7. Cost accounting separates unavoidable legacy work, comparator overhead,
   identity comparison, mismatch diagnosis, and rollback rehearsal.
8. Define negative tests proving advisory-only behavior, but create no tests,
   fixtures, scripts, checkers, config, or harness.
9. Produce a zero-edit R8 P0/P1 allowlist-decision candidate manifest and one
   allowed final disposition.

## Acceptance Thresholds

- design cases reconciled: 6/6 archetypes;
- advisory-lighter outcomes controlling execution: 0;
- legacy commands suppressed, reordered, or skipped: 0;
- unknown or partial comparator results treated as agreement: 0;
- stale or unbound identity treated as current: 0;
- mismatch classes with deterministic disposition: 6/6;
- Tier 1 rollback scenarios rehearsed: at least 4;
- Tier 2 rollback scenarios rehearsed: at least 3;
- ambiguous rollback scope defaults to Tier 1: 100%;
- re-entry without full R6/R7 proof path: 0;
- costs counted as savings before observation: 0;
- selective execution remains unauthorized.

## Stop Conditions

Return revision, narrowing, or stop if the design lets TPGR control execution,
uses the advisory comparison to omit legacy gates, treats H3 as current without
identity, makes rollback depend on unavailable runtime infrastructure, permits
ambiguous class-scoped rollback, invents observed savings, creates a second
truth store, or opens R8 activation authority.

## Allowed Final Dispositions

- `PROCEED_TO_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`
- `REVISE_R7_DUAL_RUN_OR_ROLLBACK_DESIGN`
- `NARROW_TO_ROLLBACK_REHEARSAL_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Proposed Tranche

The proposed tranche is a bounded documentation-only R7 design performed by
one no-commit worker and independently reviewed by the CVF reviewer/closer.
It produces exactly the assessment and worker-return paths named by the paired
work order and leaves all legacy enforcement unchanged.

## Evidence / Verification

The worker must cite the accepted R3-R6 sources, reconcile C1-C6, all six
mismatch classes, the Tier 1/Tier 2 rehearsal floors, ten negative designs,
and separated costs. The reviewer independently rechecks those results and
runs the governed route, worker-return, pre-implementation, and diff gates.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/orchestrator as dispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | TPGR-R7 dispatch authoring, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold preview, resolver, collision checks, apply_patch, gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | accepted R6 disposition plus standing operator authorization |
| Before status evidence | clean at `4c620f30d3bf716a8791be12c8ebec803fde414d` |
| After status evidence | exactly two dispatch artifacts before material commit |

## Claim Boundary

This baseline authorizes only two documentation outputs under the paired work
order. It authorizes no harness, receipt, fixture, checker, catalog or registry
change, command execution change, selective gate execution, canary run,
runtime/provider/live/public/deploy/production action, R8, or activation.
