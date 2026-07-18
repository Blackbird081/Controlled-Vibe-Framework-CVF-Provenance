# CVF GC-018 Baseline - MAO Evidence And Liveness Availability Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-WEB-INHERITANCE-T3P2

Dispatch base head: `f2e0b7161`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator under standing roadmap-continuation authority

Reviewer owner: CVF independent reviewer/closer

Worker target: delegated source-audit worker

## Purpose

Decide whether T3B requires a new durable MAO evidence substrate, may proceed
with a narrower durable-event-only readout, or should defer. Resolve heartbeat
claimability separately from evidence recency and durable timeout state.

## Scope / Target / Owner Boundary

This is a two-output documentation-only source decision. It changes no source,
test, persistence, Web, configuration, runtime, or provider behavior.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Disposition |
|---|---|---|---|
| T3A accepted | `docs/reviews/CVF_WEB_INHERITANCE_T3A_COMPLETION_REVIEW_2026-07-18.md` | `c0d88ff34` | ACCEPT |
| T3P1 accepted | `docs/reviews/CVF_WEB_INHERITANCE_T3P1_COMPLETION_REVIEW_2026-07-18.md` | `c282312b9` | ACCEPT |
| roadmap T3P2 row | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | dispatcher material commit for this packet | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| evidence records are held in one ledger instance | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | `MaoEvidenceLedger` | `MaoEvidenceLedger` | evidence ledger | ACCEPT |
| evidence freshness is derived from last recorded evidence | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | `classifyReadoutFreshness` | `classifyReadoutFreshness` | evidence readout contract | ACCEPT |
| workspace milestones exclude heartbeat mirroring | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | `projectWorkspaceMilestones` | `projectWorkspaceMilestones` | evidence milestone projection | ACCEPT |
| runtime contract requires batch-life plus closure-window receipt retention | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Storage And Retention Decision | `Retention` | MAO runtime foundation contract | ACCEPT |
| heartbeat is liveness-only and process-local | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | `MaoLifecycleController` heartbeat methods | `heartbeat`; `isHeartbeatStale` | lifecycle controller | ACCEPT |
| detected timeout becomes a durable event | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | `recordTimeout` | `recordTimeout` | operational worker launcher | ACCEPT |
| durable run discovery and replay now exist | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `listRunIds`; `resumeRun` | `listRunIds`; `resumeRun` | durable run store | ACCEPT |

## New Doc-Only Fields

| Field | Required value boundary |
|---|---|
| `availabilityDisposition` | exactly one terminal route token |
| `claimableLivenessDimensions` | heartbeat, timeout, and recency classified separately |
| `requiredNextOwner` | exact prerequisite owner or N/A with reason |
| `t3bReleaseBoundary` | exact released dimensions or N/A with reason |

## Required Decision Vocabulary

Select exactly one:

- `DURABLE_EVIDENCE_SUBSTRATE_REQUIRED`;
- `BOUNDED_DURABLE_EVENT_ONLY_WEB_ROUTE`;
- `EXPLICIT_IN_PROCESS_EVIDENCE_ROUTE` only if process-lifetime evidence has
  sufficient operator value without retention overclaim; or
- `DEFER_T3_WITH_REASON` with a checkable reopen condition.

## Baseline Decision

Dispatch the source decision before any persistence or Web implementation.
Heartbeat, timeout, and evidence recency must never be collapsed into one
generic liveness claim.

## Verification / Evidence

Require direct citations, refreshed searches for persistence/reconstruction
owners and callers, a terminal decision matrix, challenged alternative,
worker-return fast gate, file-size enforcement, exact two-path status, empty
cached diff, and unchanged execution HEAD.

## Current Runtime Freshness Verification

At dispatch base `f2e0b7161`, direct source confirms durable run discovery and
replay, process-local heartbeat records, durable timeout events, and an
in-memory evidence ledger. No evidence reconstruction owner or durable
heartbeat read owner was found. This packet decides the product boundary; it
does not infer one from prior chat or provider memory.

## Allowed Scope

1. `docs/reviews/CVF_WEB_INHERITANCE_T3P2_EVIDENCE_AND_LIVENESS_AVAILABILITY_DECISION_2026-07-18.md`
2. `docs/reviews/CVF_WEB_INHERITANCE_T3P2_WORKER_RETURN_2026-07-18.md`

## Forbidden Scope

- no source, test, package, lockfile, Web, page, route, persistence, config,
  environment, registry, generated aggregate, or session edit;
- no heartbeat persistence, evidence store, adapter, provider/live call,
  browser, run/event mutation, public-sync, push, release, or production action;
- no claim that evidence recency proves a live worker; and
- no staging, stash, or worker commit.

## Acceptance Criteria

- AC-01: evidence retention, reconstruction, caller, and restart behavior are
  separately resolved.
- AC-02: heartbeat, durable timeout, task state, and evidence recency remain
  distinct.
- AC-03: one terminal route is selected with value, risk, and rejected
  alternative evidence.
- AC-04: any next prerequisite or T3B release boundary is exact and does not
  claim proposed symbols as existing.
- AC-05: exactly two outputs change; nothing is staged; HEAD is unchanged; all
  governed gates pass.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture --role dispatcher --lifecycle-phase pre-dispatch --surface-selector execution-plane --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Required Decision Vocabulary; Baseline Decision; Verification / Evidence; Current Runtime Freshness Verification; Allowed Scope; Forbidden Scope; Acceptance Criteria; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source verification |
| claimBoundary | structural conformance does not select the product route |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3P2 --title "MAO Evidence And Liveness Availability Decision" --date 2026-07-18 --base f2e0b7161 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact decision vocabulary, source matrix, two-path scope, and no-implementation boundary |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | four fields listed in New Doc-Only Fields |
| claimBoundary | dispatch-authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision dispatch; no public-sync action.

## Claim Boundary

This baseline authorizes two documentation outputs only. It does not authorize
evidence or heartbeat persistence, T3B, Web implementation, provider/live,
public, push, release, production, or session mutation.
