# CVF GC-018 Baseline - Active Continuity Read-Cost T2A Core Surface Compaction

Memory class: governed-dispatch-baseline

Status: T2A_DISPATCH_BASELINE_READY

Batch ID: ACRC-T2A

Dispatch base head: `9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Authorization / Decision

The operator selected `next` on 2026-08-11 after T1 was closed and parked.
This releases packet authoring and, once the paired Work Order passes
pre-dispatch, one bounded T2A implementation. T2B instruction-carrier
compaction and T3 downstream migration remain parked.

## Purpose

Archive the oversized Core front door and V57 handoff, open compact current
surfaces, refresh generated state and bootstrap routing, bind the current
authority paths and hashes, and remove the two exact-hash migration-debt rows.

## Baseline Decision

Proceed with one no-commit implementation worker under the paired exact-scope
Work Order. Historical evidence is moved, never deleted. Root `AGENTS.md` may
receive only the V57-to-V58 pointer replacement; its broad compaction belongs
to T2B.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T1 implementation acceptance | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T1_COMPLETION_REVIEW_2026-08-10.md`; material commit `f5c2aabf1` | PASS |
| T1 parked continuity | active mode `active_continuity_read_cost_t1_closed_parked`; closure anchor `9c7d9cc63` | PASS |
| T2 roadmap authority | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md`; T2A split and operator next selection | PASS |
| clean authoring base | HEAD `9c7d9cc63`; staged zero and empty worktree before packet edits | PASS |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACRC-T2A --title "Active Continuity Core Surface Compaction And V58 Rotation" --date 2026-08-11 --base 9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact Core archive/rotation scope, authority freshness, source verification, tranche split, and zero-external-effect boundary |
| checkerReadAheadConfirmation | dispatch-quality, active-session, generated-state, core-protection, handoff, trace, file-size, archive-hygiene, and worker-return checker sources reviewed |
| docOnlyNewFields | `currentAuthority`; `active_continuity_read_cost_t2a_complete_pending_review` |
| claimBoundary | dispatch provenance only; no runtime, provider, downstream, public, deployment, or production claim |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_active_session_state.py`; `governance/compat/generate_active_session_state.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_active_archive_hygiene.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `MULTI_AGENT_MULTI_ROLE`; `WORKER_RETURN_FULL_GATE_V1`; `Core Guard Self-Protection Authorization`; `Expected manifest`; `Actual changed set`; `Manifest delta`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation and evidence after direct source verification, not first discovery |
| claimBoundary | checker read-ahead confirms packet and planned-output form only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | exact manifest, no-commit ownership, source freshness, archive preservation, and independent review remain mandatory |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2 owns Core front-door and handoff compaction | VALUE_SET | `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md` | section 9 | `T2` | active-continuity standard | ACCEPT |
| Current front door exceeds its target budget under exact debt | VALUE_SET | `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json` | entries[0] | `CVF_SESSION_MEMORY.md` | migration registry | ACCEPT |
| Current handoff exceeds its target budget under exact debt | VALUE_SET | `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json` | entries[1] | `AGENT_HANDOFF_V57_2026-08-10.md` | migration registry | ACCEPT |
| Active handoff and archive pointers are core state fields | EXISTS | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | lines 4, 35, 39-98 | `activeHandoff` | active-session core source | ACCEPT |
| Current and previous modes are core state fields | EXISTS | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | lines 100-101 | `currentMode` | active-session core source | ACCEPT |
| Next move is a generated entry source | EXISTS | `CVF_SESSION/state/entries/nextAllowedMove.json` | complete object | `nextAllowedMove` | generated state entry | ACCEPT |
| Aggregate and bootstrap are generator outputs | RUNTIME_BEHAVIOR | `governance/compat/generate_active_session_state.py` | `generate_aggregate`; `generate_bootstrap_read_model` | `BOOTSTRAP_FIELDS` | active-session state generator | ACCEPT |
| Active checker enforces budgets and authority routing | RUNTIME_BEHAVIOR | `governance/compat/check_active_session_state.py` | `_classify` | `readBudgetViolations` | active-session compatibility gate | ACCEPT |
| Root AGENTS points directly to V57 | VALUE_SET | `AGENTS.md` | Session Memory Front Door | `AGENT_HANDOFF_V57_2026-08-10.md` | root startup router | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| six planned new artifact paths | exact `Test-Path` checks returned False before authoring | ACCEPT_NO_COLLISION |
| ACRC-T2A token search | bounded `rg` over governed docs and session surfaces returned no pre-existing packet | ACCEPT_NO_COLLISION |
| successor handoff | V58 root and V57 archive paths were absent | ACCEPT_NO_COLLISION |
| collision decision | packet/output names are new; worker must refresh all source facts from executionBaseHead | ACCEPT |

## Allowed Scope

One no-commit worker may implement only the exact manifest in the paired Work
Order, run repository-local tests and governance gates, and return the named
worker-return packet.

## Forbidden Scope

T2B instruction-carrier compaction; any downstream mutation; deletion of
history; provider, network, live, browser, server, database, package, API/UI,
deployment, production, public-sync, push, stage, or worker commit.

## Acceptance Criteria

- V57 and the pre-compaction front door are preserved as governed archives.
- V58 is the only active root handoff and stays within 220 lines/32,768 bytes.
- The compact front door stays within 120 lines/20,480 bytes.
- Bootstrap, state sources, aggregate, front door, V58, and `AGENTS.md` agree.
- `currentAuthority` paths exist and hashes match repository bytes.
- Both migration-debt rows are removed only after their active replacements
  pass canonical budgets.
- Generated-state, active-session, archive, file-size, focused tests, and
  worker-return fast gates pass with staged zero and unchanged HEAD.

## Evidence / Verification

Evidence must include before/after SHA-256, line and byte facts, archive-copy
equivalence, exact name-status, focused tests, generated-state drift check,
active-session report, file-size gates, diff hygiene, HEAD/staged state, and
zero external-call accounting.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance continuity maintenance only; public sync is outside
authority.

## Claim Boundary

This baseline releases only T2A Core continuity compaction after the paired
Work Order passes pre-dispatch. It does not release T2B, T3, application work,
runtime/provider/live behavior, downstream mutation, public sync, push,
deployment, or production readiness.
