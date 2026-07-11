# CVF MSEA-R94 System Chain Gap Closure Roadmap

Memory class: FULL_RECORD

Status: PROPOSED

Date: 2026-07-11

Roadmap ID: MSEA-R94

## Purpose

Turn the bounded MSEA-R90 system-chain audit into an evidence-first closure
program for the three lanes that remain partial. Preserve the two proven lanes,
avoid reopening settled lifecycle decisions, and retain the MSEA-R91 freshness
control as the maintenance mechanism after closure.

## Target / Source

Canonical semantic sources:

- `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`;
- `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`;
- `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`;
- `docs/reference/system_chain/README.md`;
- `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`;
- `docs/reviews/CVF_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_COMPLETION_2026-07-10.md`.

Active advisory input, not semantic authority:

- `.private_reference/external_reviews/system_chain_gap_closure_2026-07-10/`;
- `docs/reviews/archive/msea_r90_system_chain_scout_2026-07-10/README.md`.

The 16 advisory files may inform methods, dissent checks, and task discovery.
Every roadmap claim and every later work order must re-verify relevant facts
against current CVF-governed sources before dispatch.

## Authorization / Decision

The operator authorized roadmap authoring after the R93 storage cleanup. This
decision authorizes planning only. Each audit, repair, reconciliation, or UI
tranche still requires its own GC-018 baseline and work order.

## Scope

In scope: sequencing evidence collection and bounded closure for the three
partial lanes; defining dependencies, acceptance targets, fail conditions,
freshness continuity, and the next dispatchable tranche.

## Non-Goals

Not in scope: implementing a runtime caller, changing the control matrix,
building a Web inventory, adding a checker, changing hooks or CI, re-deciding
R72F/R73F, changing public artifacts, or replacing the R91 freshness system.

## Design Control Gate

Before any implementation tranche, the dispatcher must prove that the proposed
change closes an accepted row-level gap, reuses the current owner surface, and
does not duplicate a registry, read model, freshness control, or operator UI.
T3B also requires the operator value checkpoint defined below.

## Work Plan

Execute T0 through T4 in the dependency order defined in this roadmap. T0 is
the only immediately authorable work-order lane. Later tranches become eligible
only after their named dependency and decision evidence exists.

## Acceptance Criteria

- T0 accounts for all 50 control-matrix rows with source-backed dispositions.
- T1 resolves every accepted repair candidate without widening unrelated scope.
- T2 provides an active doctrine-to-contract route or explicit separation.
- T3B remains unstarted unless the operator accepts T3A's value case.
- T4 preserves the proven lanes and reuses R91 freshness enforcement.

## Verification / Evidence

Each tranche must record exact source paths and symbols, caller or generated-edge
searches, test pairing, command outputs, changed-file evidence, and applicable
governance gate receipts. Aggregate PASS output cannot replace row evidence.

## Current Five-Lane Baseline

| Lane | Accepted R90 posture | R94 disposition |
|---|---|---|
| Doctrine to contract | `PARTIAL_CHAIN_WITH_DOCUMENTED_DRIFT` | close documented mapping and ownership gaps |
| Contract to runtime | `PARTIAL_RUNTIME_CONNECTION_FOR_SAMPLED_ROWS` | highest-priority full inventory and targeted repair lane |
| Runtime to enforcement | `PROVEN_CONNECTED_VIA_DATA_DRIVEN_REGISTRY` | preserve; regression-check only |
| Enforcement to evidence | `TWELVE_OF_TWELVE_DISPOSITIONED` | preserve; regression-check only |
| Evidence to operator surface | `PARTIAL_OPERATOR_VISIBILITY_BY_ENFORCEMENT_CLASS` | decision-gated visibility improvement; no automatic Web build |

## Roadmap Principles

1. Evidence precedes implementation. A file existing is not proof of a caller,
   invocation route, or correct test pairing.
2. Capability is not execution. Parameterized runners count only when a real
   registry, workflow, scenario, or caller supplies the relevant value.
3. Partial is not broken. Each row must distinguish absent, implemented,
   invoked, tested, operator-visible, intentionally separated, and retired.
4. Settled lanes are not reopened merely because neighboring lanes are partial.
5. Advisory evidence remains active input but never substitutes for current
   source verification.
6. No new checker, runtime call, Web surface, or governance refactor is created
   without a fresh GC-018 baseline and work order.

## Priority And Sequence

```text
R94-T0 full contract-to-runtime inventory
  -> R94-T1 targeted matrix/runtime/test corrections
  -> R94-T2 doctrine-to-contract reconciliation
  -> operator value checkpoint
     -> R94-T3A operator-surface documentation only
     -> R94-T3B bounded unified readout implementation, if authorized
  -> R94-T4 closure and MSEA-R91 freshness continuity
```

T1 cannot start until T0 has a reviewer-accepted row ledger. T3B cannot start
from this roadmap alone; it requires an explicit operator value decision and a
fresh governed implementation packet.

## R94-T0 - Complete Contract-To-Runtime Inventory

Objective: classify all 50 Governance Control Matrix rows using a consistent,
source-backed connection model rather than extrapolating from the three R90
samples.

Required row evidence:

| Evidence dimension | Required proof |
|---|---|
| Contract claim | exact matrix row and claimed enforcement behavior |
| Implementation | current source symbol and owning interface or function |
| Invocation | production caller, registry edge, generated command, lifecycle hook, or explicit absence |
| Test pairing | test exercises the cited implementation, not a same-named but different class |
| Operator/evidence route | output or receipt route when the row claims one |
| Final disposition | one bounded vocabulary value with reason and next action |

Minimum disposition vocabulary:

- `PROVEN_CONNECTED`;
- `IMPLEMENTED_NOT_INVOCATION_PROVEN`;
- `INVOKED_TEST_PAIRING_MISMATCH`;
- `CONTRACT_ONLY_WITH_REASON`;
- `DOCUMENTATION_DRIFT`;
- `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE`.

GC-001, GC-009, and GC-011 must be re-derived first as calibration rows. The
expected baseline is: GC-001 has a real caller but its cited test pairs with a
different implementation; GC-009 has matched source/test evidence but no
confirmed production caller; GC-011 has a proven source-caller-test chain.
These are starting hypotheses, not substitutes for the fresh trace.

Deliverable: one 50-row machine-readable ledger plus a human review explaining
counts, contradictions, risk-ranked repair candidates, and explicit no-change
rows.

Exit condition: 50 of 50 rows have terminal evidence dispositions, zero silent
omissions, and reviewer acceptance. T0 does not repair runtime or matrix files.

## R94-T1 - Targeted Contract And Runtime Corrections

Objective: repair only the T0 rows whose accepted disposition proves a material
claim mismatch or a missing connection that should exist.

Initial candidate decisions:

- GC-001: correct the matrix test citation or add a matching test for the cited
  implementation; do not call the current mismatched pairing proven.
- GC-009: decide whether production invocation is required. Add a caller only
  if doctrine and runtime ownership demand one; otherwise downgrade the matrix
  enforcement claim.
- Remaining rows: prioritize false `PROVEN_CONNECTED` claims, safety-critical
  missing invocation, and stale evidence paths before naming or formatting debt.

Each repair must have a separate source-verified work order, bounded tests, and
before/after row evidence. One work order may group rows only when they share an
owner, failure mechanism, and verification route.

Exit condition: every T0 repair candidate is `FIXED_AND_PROVEN`,
`CLAIM_DOWNGRADED_WITH_REASON`, `DEFERRED_WITH_REOPEN_CONDITION`, or
`BLOCKED_WITH_OWNER_ACTION`.

## R94-T2 - Doctrine-To-Contract Reconciliation

Objective: remove ambiguity without forcing unrelated architecture schemes into
one numbering vocabulary.

Required decisions:

1. Identify current active-tree owners for the L0-L6 doctrine model.
2. Decide whether the missing active L1/L2 named content is a source gap, an
   intentional archive-only state, or content owned under different names.
3. Cross-reference the independent architecture/module maps where they describe
   the same concerns.
4. Explicitly record intentional separation where the maps serve different
   abstractions; do not manufacture false one-to-one equivalence.

Exit condition: an operator can start at doctrine, reach the owning contract or
an explicit intentional-separation record, and avoid relying on a legacy mirror
as the only active route.

## R94-T3 - Evidence-To-Operator Decision Lane

R90 proves CLI per-checker PASS/FAIL output for the CI gate class and a bounded
Web subset of five job types with one directly wired checker. It does not prove
a unified Web inventory for all 186 checker scripts.

### T3A - Documentation And Readout Contract

Define the minimum useful operator question, audience, read model, freshness
source, filtering, and evidence links. Compare the expected reduction in search
time and stale interpretation against implementation and maintenance cost.

### T3B - Optional Bounded Implementation

Implement a unified readout only if the operator explicitly authorizes it after
T3A. Reuse the R91 system-chain map/freshness source where possible. Do not
create a second checker registry or infer runtime health from file existence.

Reopen condition: proceed only when T3A demonstrates a concrete operator task
that the CLI and current five-job subset cannot serve efficiently, and names a
measurable acceptance target.

## R94-T4 - Closure And Maintenance Continuity

Objective: close repaired rows without allowing the map to become stale again.

Required closure actions:

- refresh the canonical system-chain map from current source evidence;
- retain the MSEA-R91 30-day freshness policy and existing local, CI, and weekly
  enforcement paths;
- ensure every new owner or repaired edge is covered by the existing freshness
  input model, or explicitly extend that model in a separate authorized packet;
- record closure state in the active handoff and generated session state;
- keep partial or deferred rows explicit rather than claiming universal closure.

This roadmap does not authorize a second freshness mechanism. R91 remains the
maintenance owner unless later evidence proves it insufficient.

## Preserved And Parked Boundaries

- The nine cross-family checkers are invoked through the data-driven scenario
  registry. They are not orphaned merely because no literal direct import is
  present.
- The R72F `RETIREMENT_HOLD_SOURCE_GAP` lifecycle decision remains unchanged.
- R73F remains parked until its recorded source condition is satisfied.
- Deep names and duplication are maintainability debt, not proof of a broken
  execution chain.
- Runtime-to-enforcement and enforcement-to-evidence receive regression checks,
  not speculative repair.
- R84 effectiveness work remains parked until its evidence threshold is met.

## Success Measures

| Measure | Target |
|---|---|
| Control-matrix row coverage | 50/50 terminal dispositions |
| Silent or inferred row outcomes | 0 |
| Accepted repair candidates without owner/action | 0 |
| Doctrine routes ending only in an unexplained legacy mirror | 0 |
| Proven lanes accidentally downgraded without new evidence | 0 |
| Freshness mechanism duplication | 0 |
| Operator readout implementation without value checkpoint | 0 |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap tranche | Required future packet | Minimum deliverable | Dependency |
|---|---|---|---|
| R94-T0 | fresh GC-018 plus audit work order | 50-row connection ledger and review | R93 closed |
| R94-T1 | one or more source-verified repair packets | corrected rows, source, tests, evidence | T0 reviewer acceptance |
| R94-T2 | fresh reconciliation packet | active doctrine/contract route map | T0 may run independently; no runtime edit |
| R94-T3A | fresh value-assessment packet | operator task/readout contract | T0 evidence available |
| R94-T3B | fresh implementation packet | bounded unified readout | explicit operator authorization after T3A |
| R94-T4 | fresh closure packet | refreshed map, freshness proof, continuity | all authorized earlier tranches terminal |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | dispatcher, worker, reviewer, closer | governed GC-018, work order, source tree, gates | CVF-governed artifacts and current source only | source citations, commands, row ledger, gate receipts | native governed route; ALLOWED_WITH_FRESH_PACKET |
| EXTERNAL_AGENT_CLI_MCP | optional external reviewer | exported bounded evidence packet or CLI review input | advisory only; no direct authority or mutation | dissent and source references re-verified by internal reviewer | no adapter authorized by this roadmap; DEFERRED |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | `Status:`; `Checker Source Read-Ahead Block`; `Roadmap-to-Work-Order Trace Matrix`; `Public Export Disposition`; `PROPOSED` |
| gateRunPurpose | confirmation and evidence after source-backed roadmap authoring; not first discovery |
| claimBoundary | roadmap sequencing and authorization boundaries only; no gap repair or runtime claim |

## Epistemic Process Block

### Expected Result / Prediction

The highest-value first move is a full contract-to-runtime inventory because
the three-row sample already found two materially unproven connections.

### Evidence Comparison

R90 found GC-001 test-pairing mismatch, GC-009 missing production invocation,
and GC-011 fully connected. R90 also proved the registry-driven enforcement
lane and dispositioned all 12 evidence paths, so broad repair of those lanes
would not be evidence-led.

### Contradiction Or Gap Disposition

The current matrix cannot support a universal runtime-connection claim from a
three-row sample. R94-T0 converts this uncertainty into a complete row ledger
before selecting implementation work.

### Claim Update

This roadmap prioritizes closing observed connection and routing gaps while
preserving proven lanes and explicit partial states.

## Fail Conditions

Stop and return to the operator or reviewer if a tranche:

- treats an advisory file as canonical CVF authority;
- marks a row connected from file existence alone;
- modifies runtime, checkers, hooks, Web, or lifecycle state without a fresh
  authorized work order;
- re-decides R72F or reopens R73F without its recorded condition;
- builds T3B before the operator value checkpoint;
- creates a second freshness owner without evidence that R91 is insufficient;
- closes with incomplete row counts, stale citations, or unresolved checklist
  residue hidden by an aggregate PASS.

## Next Allowed Move

R94-T0, T1A, and T1B are reviewer-accepted. Operator authorization on
2026-07-11 permits one integrated `MSEA-R94-REMAINING-WAVE` no-commit worker
packet for T1C, T2, T3A, and T4 readiness. The packet may group these remaining
documentation/read-model phases to reduce repeated dispatch latency, but each
phase must retain its own evidence ledger and terminal disposition. T3B runtime
or UI implementation remains excluded. A phase needing runtime, tests, a new
checker, or a second freshness owner must return `BLOCKED_WITH_OWNER_ACTION`
without stopping independent documentation phases.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance roadmap. No public artifact, runtime
feature, or public catalog claim is authorized.

## Claim Boundary

This roadmap defines evidence order, tranche boundaries, success measures, and
reopen conditions. It does not claim the three partial lanes are already
closed, authorize runtime or Web implementation, modify lifecycle decisions,
or promote the active advisory files to semantic authority.
