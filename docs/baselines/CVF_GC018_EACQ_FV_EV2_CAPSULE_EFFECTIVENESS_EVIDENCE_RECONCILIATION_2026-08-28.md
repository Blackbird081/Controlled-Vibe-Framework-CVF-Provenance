# CVF GC-018 Baseline - EACQ-FV EV-2 Capsule Effectiveness Evidence Reconciliation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EACQ-FV-EV2

Date: 2026-08-28

Dispatch base head: `51fe7edddfa591f15c29d57d79c0da5d37737835`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Worker: delegated no-commit evidence worker

Orchestrator/reviewer/closer: designated internal reviewer

providerExecutionAuthority: FORBIDDEN

## Purpose

Reconcile the three governed capsule-effectiveness observations from EV-1,
L2, and L3 against the roadmap's comparison dimensions. Produce a bounded
decision on what the evidence supports now and what remains unproved.

## Baseline Decision / Proposed Tranche

| Field | Decision |
| --- | --- |
| Candidate | EACQ-FV-EV2 evidence reconciliation |
| Value gate | PASS_BOUNDED |
| Serious finding | The roadmap requires an effectiveness evaluation, while current evidence remains split across three completion artifacts. |
| Source-backed | Three independently governed completion reviews are pinned below. |
| Non-duplicate | Targeted search found no existing EV-2 aggregate or cross-tranche decision artifact. |
| Value versus cost | Two docs-only outputs, local reads, no implementation or provider quota; closes an explicit roadmap evidence question. |
| Required uncertainty | Task difficulty and authority envelopes differ; `INSUFFICIENT_COMPARABILITY` must remain an allowed result. |

## Scope / Methodology

Compare EV-1, L2, and L3 on first-return disposition, reviewer correction
count/severity, owner/protected-path defects, positive and negative evidence,
manifest accuracy, context size, preparation/review latency, and recurrence.
Separate observed facts, adjusted comparison, and inference. Do not construct
missing latency or token values.

## Acceptance Criteria

1. Every comparison cell cites one of the three pinned completion artifacts.
2. Material differences in task difficulty, scope, and authority are explicit.
3. The decision is exactly one of `PROMISING_NON_CAUSAL`, `NEUTRAL`,
   `NEGATIVE`, or `INSUFFICIENT_COMPARABILITY`.
4. Any recommendation has a named owner, bounded next evidence need, and stop
   condition; no automatic successor follows.
5. UAA, runtime, provider, public, deploy, checker, and code lanes stay parked.

## Verification Evidence

Dispatch verification consists of exact source hashes, schema-valid capsule
JSON, the exact four-path dispatcher manifest, targeted artifact guards, and
the full pre-dispatch autorun bundle. Worker findings require independent
review and cannot be accepted from this baseline alone.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| roadmap requires comparable-task quality evidence | governed requirement | `docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md` | Acceptance Criteria and Verification / Evidence Plan | criterion 10 and comparison dimensions | EACQ-FV roadmap | ACCEPT |
| EV-1 is promising but non-causal | governed review fact | `docs/reviews/CVF_EACQ_FV_EV1_CAPSULE_ENHANCED_OWNER_MAP_EVIDENCE_COMPLETION_2026-08-28.md` | F-03 and Epistemic Process Block | effectiveness classification | EV-1 completion review | ACCEPT |
| L2 is neutral and required amendment plus semantic repair | governed review fact | `docs/reviews/CVF_EACQ_FV_L2_EXECUTION_BASE_PACKET_SHAPE_SCAFFOLD_HARDENING_COMPLETION_2026-08-28.md` | F-04 through F-06 | `NEUTRAL_NON_CAUSAL` | L2 completion review | ACCEPT |
| L3 is promising with no implementation repair | governed review fact | `docs/reviews/CVF_EACQ_FV_L3_AUTOMATION_ASSIST_OWNER_DRIFT_RECONCILIATION_COMPLETION_2026-08-28.md` | Findings and Finding-To-Governance Learning Disposition | capsule effectiveness | L3 completion review | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| candidate token search | `rg -n "EACQ-FV-EV2|Capsule Effectiveness Evidence Reconciliation" docs CVF_SESSION` before authoring returned no owner | ABSENT_BEFORE_AUTHORING |
| existing evidence owners | EV-1, L2, and L3 completion reviews own their observations; the roadmap owns comparison criteria | ENRICH_ROADMAP_EVIDENCE_ONLY |
| collision decision | no new capsule protocol, metric owner, checker, or runtime owner is created | PASS |

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EACQ-FV-EV2 --title "Capsule Effectiveness Evidence Reconciliation" --date 2026-08-28 --base 51fe7eddd --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added the four-part value gate, pinned evidence set, exact comparison dimensions, and non-causal stop rule. |
| checkerReadAheadConfirmation | Dispatch, structural, trace, handoff, lifecycle, and checker-read-ahead sources were inspected. |
| docOnlyNewFields | comparison verdict and evidence sufficiency; no runtime field |
| claimBoundary | Dispatch provenance only. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`evidence reconciliation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "evidence reconciliation" --role dispatcher --lifecycle-phase dispatch`

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `providerExecutionAuthority: FORBIDDEN`; Source Verification table columns; trace labels |
| gateRunPurpose | Confirm the authored packet against known literal contracts. |
| claimBoundary | Read-ahead evidence only; no semantic acceptance or execution proof. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | internal orchestrator/dispatcher/reviewer |
| Provider or surface | local private-provenance repository |
| Session or invocation | EACQ-FV-EV2 dispatch, 2026-08-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, scaffold helper, ADIF resolver, `apply_patch` |
| Target paths | paired baseline, work order, task capsule, and roadmap dispatch row |
| Allowed scope source | operator continuation through the fresh value gate |
| Before status evidence | clean worktree at dispatch base head |
| After status evidence | dispatch-author manifest only; worker outputs absent |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | EV-2 evidence-only dispatch |
| Claim boundary | no implementation, causal uplift, provider, public, push, or deployment claim |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eacq-fv-ev2-dispatch-2026-08-28` |
| Expected manifest | this baseline; paired work order; paired capsule; roadmap |
| Actual changed set | this baseline; paired work order; paired capsule; roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline opens one private, provider-free evidence reconciliation. It
does not prove causal uplift, authorize implementation, reopen UAA, or alter
runtime, checker, public, deployment, or production authority.
