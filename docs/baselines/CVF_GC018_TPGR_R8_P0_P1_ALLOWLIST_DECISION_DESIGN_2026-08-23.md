# CVF GC-018 TPGR-R8 P0/P1 Allowlist Decision Design Baseline

Memory class: governed-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-23

Task ID: TPGR-R8

dispatchBaseHead: `ac678d0cbea841087e9896c5242ee69d978a0471`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one bounded documentation-only design pass that decides whether any
exact task identity has enough current, independently reviewable evidence to
enter a proposed P0 allowlist, while every non-qualifying or ambiguous identity
remains P1 and continues to require the full legacy bundle. This tranche designs
the decision and evidence contract only; it does not activate either route.

## Authorization / Source

TPGR-R7 is independently accepted with bounded scope at `723382cfc` with
final disposition `PROCEED_TO_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`. The operator
authorized roadmap continuation on 2026-08-23. The governing R7 assessment is
`docs/assessments/CVF_TPGR_R7_DUAL_RUN_CANARY_AND_ROLLBACK_REHEARSAL_DESIGN_2026-08-18.md`.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R7 material closure | `723382cfc373f8da8971326733f0ed4c074066f1` | ACCEPT |
| R7 assessment | SHA-256 `ca58d33e218e9c3160a49edb450eaf3f71454e0f5641e928a17b1d07615538ca` | ACCEPT |
| R7 worker return | SHA-256 `000f867606e9c39837791876e9cbb4e2a9ac6fcd5999b12296c5ece0773c3a49` | ACCEPT |
| R7 continuity closure | `9bbc6bf31014608633380d36e70f8319e2483e87`; handoff sync `ac678d0cbea841087e9896c5242ee69d978a0471` | ACCEPT |
| Operator checkpoint | roadmap continuation requested 2026-08-23 | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R8 --title "P0 P1 Allowlist Decision Design" --date 2026-08-23 --base ac678d0cbea841087e9896c5242ee69d978a0471 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with R7 evidence, eligibility identity, admission/default rules, hostile cases, expiry/revocation, thresholds, and exact two-path manifest |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `decisionCaseId`, `eligibilityIdentity`, `evidenceState`, `allowlistClass`, `admissionReason`, `expiryState`, `revocationTier`, `reentryProof` |
| scaffoldClaimBoundary | documentary R8 decision design; no implementation or activation |
| claimBoundary | dispatch provenance only; no executable allowlist, route change, or runtime behavior |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | exact roles and paths, checker read-ahead, evidence-state honesty, no-commit ownership, and independent review are mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | `Memory class:`; `Status:`; `docType:`; `## Purpose`; `## Authorization`; `## Source Verification Block`; `## Proposed Tranche`; `## Evidence / Verification`; `## Agent Operation Trace Block`; `## Claim Boundary`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary` |
| gateRunPurpose | final gates are confirmation evidence, not first discovery of required baseline shape |
| claimBoundary | read-ahead proves only that current checker literals were inspected before authoring |

## Source Verification Block

| Source | Verification | Disposition |
|---|---|---|
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | fully read for profile, escalation, shadow interlock, activation, and rollback rules | ACCEPT |
| R7 baseline and work order | fully read for the authorized successor scope and exact no-commit pattern | ACCEPT |
| R7 assessment and worker return | fully read for comparator, mismatch, rollback, cost, and zero-edit R8 candidate evidence | ACCEPT |
| `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json` and schema | current enum and manifest shape checked | ACCEPT |
| external/provider source | none used | N/A with reason: bounded CVF-owned evidence only |

## Negative Search And Collision Discipline

Repository search found no active TPGR-R8 artifact, checker, harness, allowlist,
or R9 authority. The candidate checker and harness names in R7 are explicitly
nonexistent and unauthorized. This dispatch therefore creates only the paired
R8 baseline/work order and reserves unique R8 assessment/worker-return paths.

## Design Contract

The worker must design and reconcile all of the following:

1. A closed P0/P1 vocabulary in which P0 means only "candidate for a future
   lighter route after separate activation authority" and P1 means "full
   legacy bundle remains mandatory." Neither label changes execution in R8.
2. An exact eligibility identity bound to task kind, authority impact, external
   effect, sensitivity, reversibility, source scale, delegation, novelty,
   path-family set, claim set, proof set, route receipt identity, legacy bundle
   catalog identity, confirming reviewer identity, and freshness state.
3. Fail-closed P0 admission predicates: current exact identity; current H3
   binding; complete R7 comparator evidence; `EXACT_AGREEMENT` only; zero
   mismatch, unknown, partial, timeout, stale, or semantic-drift state; no
   protected/state/runtime/live/public/destructive trigger; independent review;
   and a named expiry/re-entry rule.
4. Deterministic default-to-P1 rules for every missing, malformed, conflicting,
   stale, widened, or unreviewed field. Empty P0 is a valid result.
5. A case-by-case decision for C1-C6 using only current evidence. Design-time
   expectations and historical value evidence must not be promoted to observed
   current dual-run agreement.
6. At least eight hostile admission cases covering identity drift, checker
   semantic drift behind stable filenames, stale reviewer binding, partial
   receipts, task-scope widening, protected-path contamination, contradictory
   results, and expiry.
7. An immutable decision-record schema with candidate identity, evidence
   hashes, observed/projected label, decision, reasons, reviewer, expiry,
   rollback tier, and re-entry proof. No new registry/store is created.
8. A revocation and rollback design: any ambiguity or cross-class effect
   revokes candidate P0 status globally to advisory-off/full-legacy posture;
   exact class-local revocation is allowed only with proven dependency closure.
9. Separated observed/projected cost and value accounting. No predicted saving
   may be presented as observed or used to authorize activation.
10. A zero-edit R9 candidate manifest that names possible future artifacts and
    exact prerequisites without drafting, scaffolding, or authorizing them.
11. Negative-test designs proving P0 classification cannot suppress, reorder,
    or skip legacy commands; P1 stays full-bundle; unknown/partial is P1;
    stale H3 cannot enter P0; semantic drift revokes; and serialized decisions
    cannot be consumed as execution plans.
12. Exactly one allowed final disposition.

## Acceptance Thresholds

- 6/6 R7 cases receive an evidence-bounded P0/P1 decision;
- 100% of unobserved, stale, unknown, partial, or conflicting cases select P1;
- zero design-time or projected result is treated as observed agreement;
- zero protected/state/runtime/live/public/destructive case enters P0;
- at least 8/8 hostile admission cases fail closed;
- 100% identity widening or semantic drift revokes P0 candidacy;
- zero legacy command suppression, reorder, skip, or TPGR-added enforcement;
- decision schema, expiry, revocation, rollback, and re-entry are deterministic;
- costs are separated and projected savings are not treated as observed;
- R9 manifest is zero-edit and activation-neutral;
- exact two-output worker manifest and no commit;
- one allowed final disposition.

Any miss forbids a proceed disposition.

## Stop Conditions

Stop and return `BLOCKED_WITH_REASON` if a required source is absent, the exact
identity cannot be derived without inventing an owner, a third output is
required, an executable allowlist/checker/harness/config is needed, any legacy
command would change, or any provider/network/live/public/deploy action is
required.

## Allowed Final Dispositions

- `PROCEED_TO_R9_ACTIVATION_AND_ROLLBACK_AUTHORITY_DESIGN`
- `HOLD_EMPTY_P0_ALLOWLIST_PENDING_OBSERVED_DUAL_RUN_EVIDENCE`
- `REVISE_R8_P0_P1_ALLOWLIST_DECISION_DESIGN`
- `STOP_TPGR_SECOND_UPGRADE`

## Proposed Tranche

One external no-commit design worker creates exactly:

- `docs/assessments/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md`
- `docs/reviews/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_WORKER_RETURN_2026-08-23.md`

The internal reviewer independently verifies every case, hostile probe,
identity rule, cost label, disposition, and gate before any commit.

## Evidence / Verification

Required dispatch verification is task-route compliance, pre-dispatch autorun,
worker-return fast-gate compatibility, diff hygiene, exact manifest, and clean
status. R8 makes no corpus-completeness, runtime, live, or public claim.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | documentation-only decision design; no runtime or activation surface exists in this tranche |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | primary reviewer/orchestrator dispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | TPGR-R8 dispatch authoring, 2026-08-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, repository search, apply_patch, local gates, Git |
| Target paths | this baseline and paired R8 work order |
| Allowed scope source | R7 accepted disposition plus operator continuation checkpoint |
| Before status evidence | clean worktree at `ac678d0cbea841087e9896c5242ee69d978a0471` |
| After status evidence | exactly two dispatch artifacts before commit |
| Diff evidence | `git diff --check`; `git status --short --untracked-files=all` |
| Approval boundary | documentation-only R8 allowlist-decision design dispatch |
| Claim boundary | no allowlist implementation, activation, real canary, or selective execution |
| Agent type | reviewer/orchestrator dispatch author |
| Invocation ID | `tpgr-r8-dispatch-authoring-2026-08-23` |
| Expected manifest | paired R8 baseline and work order |
| Actual changed set | same two paths before dispatch commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes documentation-only P0/P1 decision design. It does not
authorize an allowlist, checker, harness, receipt store, standard change,
activation, selective gate execution, legacy suppression, R9 execution,
runtime/provider/live/public/deploy/production action, or any third output.
