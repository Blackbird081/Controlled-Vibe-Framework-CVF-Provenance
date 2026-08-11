# CVF Active Continuity Read-Cost Reduction Roadmap

Memory class: ACTIVE_ROADMAP

Status: T1_T2A_T2B_T3_PASS

Date: 2026-08-10

Risk ceiling: R2

## Purpose

Reduce agent startup read cost by making compact, current authority routing the
default and moving historical detail behind targeted archive/state lookups.

## Authorization

The operator authorized this roadmap on 2026-08-10 after observing excessive
worker startup time caused by long active continuity surfaces. T1 closed at
material commit `f5c2aabf1`. On 2026-08-11 the operator selected the next move,
authorizing T2 packet authoring. T2A and T2B require separate exact-scope Work
Orders. After T2B acceptance, the operator selected continuation on 2026-08-11
under delegated orchestrator/reviewer authority. The T3 entry condition was
freshly verified against the stopped and accepted P4-A1 closure, and T3 is now
dispatch-ready under its exact GC-018 baseline and Work Order.

## Scope

This roadmap covers Core startup routing, active-continuity read budgets,
machine enforcement, later Core compaction, and later downstream migration.

## Non-Goals

It does not delete governed history, develop application features, change
provider/runtime behavior, deploy, publish, or perform public sync.

## Design Control Gate

Each tranche requires an exact changed set, source-verified authority,
machine-gate evidence, and an independent review before closure. T1 must not
compact current continuity; T2 and T3 remain parked until separately released.

## Problem

The active continuity surfaces are routing agents through large historical
records before the agent reaches the current task authority.

Measured on 2026-08-10:

| Repository | Active surface | Lines | Bytes | Material issue |
|---|---|---:|---:|---|
| CVF Core | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | 11 | 1,145 | already compact and should become the default first read |
| CVF Core | `CVF_SESSION_MEMORY.md` | 522 | 97,464 | active front door contains long prior-work tables |
| CVF Core | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | 14,849 | 1,686,764 | machine aggregate contains extensive historical entries |
| CVF Core | `AGENT_HANDOFF_V57_2026-08-10.md` | 922 | 47,102 | active handoff accumulated prior transitions |
| shift operations | `SESSION/SESSION_MEMORY.md` | 375 | 81,641 | front door contains extensive completed history |
| shift operations | `SESSION/ACTIVE_SESSION_STATE.json` | 1,364 | 120,284 | 251 mandatory reads and 42 blocked-history entries |
| shift operations | active P4-A1 handoff | 116 | 6,915 | compact enough, but points to the original Work Order instead of the current amendment |

The defect has three parts:

1. startup instructions require full reads of machine/history-heavy surfaces;
2. active surfaces retain closed history instead of pointers to archives; and
3. the active authority pointer is not refreshed when a repair amendment
   supersedes the original worker authority.

## Target Operating Model

Agents start from a small routing packet and expand only when the current task
requires more authority.

```text
bootstrap read model
  -> compact session front door
  -> current active handoff
  -> current authority packet only
  -> targeted state/history lookup only when unresolved
```

The full state registry may remain available as machine-readable evidence
during migration, but it is not a default human or agent first read.

## Binding Rules

### Rule 1 - Bootstrap first

Every governed repository must provide a compact bootstrap read model. Startup
instructions read it before session memory, full state, or handoff content.

The bootstrap must identify only:

- current mode;
- active handoff;
- current authority paths and hashes when a worker is dispatched;
- next allowed move;
- parked checkpoint;
- compact front-door and full-state paths; and
- claim boundary.

### Rule 2 - Progressive continuity disclosure

Default startup reads are limited to bootstrap, compact front door, active
handoff, and current authority packet. Agents must not read the full active
state aggregate or historical handoffs unless a current field is missing,
contradictory, or a task explicitly requires historical evidence.

Targeted JSON field extraction is allowed and preferred over a full aggregate
read.

### Rule 3 - No closed history in active surfaces

Active front doors and handoffs contain current facts and pointers only.
Closed tranche narratives, old test counts, superseded authority chains, and
historical blocked-work explanations move to governed archive or history-index
surfaces.

An active surface may retain at most one predecessor pointer and a concise
reason it was superseded. It must not copy predecessor narrative.

### Rule 4 - Current authority freshness

When a Work Order amendment, repair authority, or successor review becomes the
current worker authority, the bootstrap and active handoff must point directly
to that latest accepted packet and its review hash. Pointing only to the
original Work Order is stale routing.

### Rule 5 - Read budgets

| Surface | Hard budget |
|---|---:|
| bootstrap read model | 60 lines and 4 KiB |
| active session front door | 120 lines and 20 KiB |
| active handoff | 220 lines and 32 KiB |
| default current-authority read list | 12 paths |
| predecessor narrative retained inline | 0; pointer only |

Both line and byte limits apply. A file exceeding either limit fails the
continuity read-budget guard.

The machine state aggregate receives a migration warning at 128 KiB and a
default-startup prohibition immediately. A later schema tranche may split the
aggregate into active and historical registries without blocking the first
latency reduction.

### Rule 6 - Rotation at authority transition

Open a successor handoff when the active authority family changes or a repair
amendment supersedes the current dispatch. Archive the superseded handoff;
never append the entire new phase to the old handoff.

### Rule 7 - Downstream safety

Do not compact or rotate a downstream project's protected continuity files
while a no-commit worker or independent reviewer is active. Apply compaction
only after that worker/review checkpoint returns and protected hashes are
released by fresh authority.

## Tranches

### T1 - Standard, checker, and distributed startup rule

Deliver:

- canonical active-continuity read-budget standard;
- machine checker and adversarial tests;
- Core startup instruction update;
- downstream AGENTS template update;
- autorun registration in a bounded protected-path batch.

T1 does not compact current Core or downstream continuity content. Enforcement
must support an explicit migration disposition so existing debt is measured
without silently declaring it compliant.

### T2A - CVF Core active-surface compaction and handoff rotation

Status: `CLOSED_PASS_BOUNDED` at reviewer-owned material commit `fd4d61e73`.
Completion evidence:
`docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2A_COMPLETION_REVIEW_2026-08-11.md`.
The accepted exact-18 includes the operator-authorized legacy test-fixture
path. T2B and T3 remain parked pending fresh selection.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this T2A closure remains private provenance evidence. A later
public-sync batch requires separate operator authority and repository-boundary
proof.

After T1 acceptance:

- archive the current long front door and V57 handoff;
- create compact current front door and successor handoff;
- refresh bootstrap/current authority routing;
- retain historical state sources outside default startup reads; and
- prove the new budgets and existing session-state invariants.

T2A must edit generated state sources and regenerate aggregates; no direct
aggregate-only edit is allowed. T2A may update the `AGENTS.md` active-handoff
pointer only; broad root-instruction compaction belongs to T2B.

### T2B - Core and inherited agent-instruction carrier compaction

Status: `CLOSED_PASS_BOUNDED` after independent review on 2026-08-11.
Source map:
`docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_SOURCE_BINDING_MATRIX_V2_2026-08-11.md`.
Authority packet:
`docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T2B_INSTRUCTION_CARRIER_COMPACTION_2026-08-11.md`
and
`docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2B_INSTRUCTION_CARRIER_COMPACTION_V2_2026-08-11.md`.
Completion evidence:
`docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_COMPLETION_REVIEW_2026-08-11.md`.
T3 remained parked until its fresh dispatch authority was committed; it is now
closed as recorded in the T3 section below.

After T2A acceptance, compact the instruction carriers that agents may load
before task routing:

- reduce root `AGENTS.md` to a compact mandatory router plus machine-required
  binding markers;
- reduce provider-local `CLAUDE.md` to provider guidance and canonical CVF
  pointers, without promoting it to source authority;
- compact the downstream AGENTS template so newly initialized hidden-CVF
  workspaces inherit progressive disclosure;
- preserve every still-binding rule through a canonical owner or a new compact
  rule-routing index; and
- archive the superseded full carriers without treating archives as active
  authority.

T2B requires a source/binding matrix for every current `AGENTS.md` heading and
every checker that reads `AGENTS.md` or `CLAUDE.md`. It must not begin inside
T2A and must not weaken live-proof, repository-boundary, source-verification,
closure, handoff, corpus, or public-export controls.

### T3 - shift-operations-workspace application

Status: `CLOSED_PASS_BOUNDED` after independent review on 2026-08-11 under
`docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T3_SHIFT_OPERATIONS_APPLICATION_2026-08-11.md`
and
`docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T3_SHIFT_OPERATIONS_APPLICATION_2026-08-11.md`.
Target execution base:
`b62271d42150da68d4fb80983cd56260ee11cee1`. The worker made no commit; the
independent reviewer accepted and committed the bounded exact-15 closure at
`0b835be3ff1ac1fbd1c95e365471887202d718b5`. Core evidence:
`docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T3_COMPLETION_REVIEW_2026-08-11.md`.

Entry condition: the active P4-A1 Repair 4 worker and its independent review
have stopped, and fresh authority releases the protected continuity paths.

Then:

- add a downstream bootstrap read model;
- compact `SESSION/SESSION_MEMORY.md` to current pointers only;
- replace the 251-path default read list with at most 12 current paths;
- move historical required reads and blocked-work narrative to an archive or
  history index;
- rotate the handoff to the latest accepted P4-A1 authority; and
- update the compatibility mirror and Project Knowledge pin atomically.

T3 changes governance continuity only. It does not develop P4-A, P4-A2,
provider, API/UI, RAG, audit, persistence, or any deeper project capability.

## Work Plan

Execute T1, T2A, T2B, and T3 in order under the tranche boundaries above. A
later tranche may start only after the preceding tranche is accepted and its
entry condition is freshly verified.

## Acceptance Criteria

- A new agent can identify current mode, current authority, next move, and
  parked boundary without reading more than four compact routing files.
- No default startup instruction requires a full historical state aggregate.
- Active front door, bootstrap, and handoff pass both line and byte budgets.
- Current authority paths and hashes match the latest accepted Work Order or
  amendment and review.
- Historical facts remain discoverable through explicit archive/history
  pointers; compaction does not delete governed evidence.
- Machine probes reject oversize files, excess default reads, stale authority,
  and inline predecessor narrative.
- Existing provider/live/public/deployment boundaries remain unchanged.

## Stop Conditions

- Stop T1 if the checker requires changing current continuity content before a
  migration disposition exists.
- Stop T2A on generated-state drift, handoff ambiguity, or missing archive
  evidence.
- Stop T2B if any active mandatory rule lacks a canonical owner, any checker
  binding would be lost, or a compact carrier would exceed its approved budget.
- Stop T3 if the P4-A1 worker/reviewer is still active or protected hashes are
  not freshly released.
- No tranche may delete historical evidence; it may only move it to governed
  archive/history ownership.

## Verification

T1 verification is recorded in its completion review. T2A verification is
defined by its Work Order and must include archive byte/hash evidence, focused
generator and active-session tests, generated-state drift checks, read-budget
enforcement, exact-scope evidence, staged-zero evidence, and sanitized local
governance gates. T2B requires a separately reviewed binding/source matrix
before any instruction-carrier rewrite.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | `Memory class:`, `## Purpose`, `## Authorization`, `## Scope`, `## Non-Goals`, `## Design Control Gate`, `## Work Plan`, `## Verification`, `## Checker Source Read-Ahead Block` |
| gateRunPurpose | confirmation and evidence after checker-source read-ahead, not first discovery |
| claimBoundary | read-ahead evidence covers this roadmap's governed Markdown shape only |

## Claim Boundary

This roadmap addresses agent startup latency, continuity routing freshness,
and active-surface maintainability. It does not prove runtime governance,
provider behavior, deployment readiness, production readiness, or completion
of LPCI1 Web or shift-operations project features.
