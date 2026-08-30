# CVF MAO Atomic Delegation Lifecycle Composition Standard

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-08-29

Memory class: REFERENCE_KNOWLEDGE

Knowledge source lineage: CVF-native normalization of failure-semantics ideas
verified against pinned `spinabot/brigade` commit
`e084f08dfb9aafa01e991c738cfd88e4c554ab4d`, then reconciled with existing
MAO task-graph, lifecycle, delegation, launcher and durable-ledger owners.

`EPISTEMIC_PROCESS_NA_WITH_REASON`: this artifact defines a design contract
and records bounded integration evidence; representative runtime use proof is
still pending and no effectiveness or production claim is made.

## Purpose

Define one compositional contract for four delegation failure boundaries that
must not be designed independently: atomic child reservation, parent-local and
global concurrency accounting, descendant abort with exactly-once budget
release, and per-parent completion serialization with one continuation wake.

This is CVF knowledge and executable owner guidance. A bounded provider-free
coordinator is integrated into the existing launcher; full runtime-use proof
remains a separately checkpointed action.

## Scope / Applies To

Applies to MAO child admission, concurrency accounting, subtree abort,
reservation/budget release, child settlement and parent continuation design.
It does not apply to single-agent work without child delegation, and this
standard by itself activates no runtime path.

## Authority And Owner Boundary

The existing owner remains
`docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`.
This standard owns only the cross-control composition previously described in
separate concurrency, cancellation, idempotency and completion clauses.

Relevant implementation owners are:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts`;
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts`;
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts`;
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`;
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`.

No upstream source is imported and no foreign runtime becomes a CVF authority.

## Composition State Model

Each child attempt has one reservation lifecycle:

`PROPOSED -> RESERVED -> STARTED -> SETTLING -> SETTLED`

Before `STARTED`, a reservation may terminate as `RELEASED`. After start, an
accepted abort moves the attempt through `SETTLING` to a terminal outcome such
as `CANCELLED`, `FAILED`, `TIMED_OUT`, or `COMPLETED`; it never rewrites the
immutable task graph.

Each state-changing operation carries a stable idempotency key. Replay returns
the prior receipt. Conflicting reuse fails closed.

## Normative Invariants

### I-1 Atomic Reservation Before Dispatch

A child may be dispatched only after one atomic admission transition has:

- verified parent and global admission remain open;
- verified authority/task-graph identity;
- checked both parent-local and global concurrency ceilings;
- reserved one concurrency slot and the declared invocation budget;
- emitted a durable reservation receipt.

Check-then-dispatch without a reservation receipt is invalid. Failed
reservation changes no counter and launches no child.

### I-2 Dual-Scope Concurrency Conservation

At every replayable ledger position:

`parentReservedOrRunning <= parentConcurrencyLimit`

`globalReservedOrRunning <= globalConcurrencyLimit`

The same reservation identity contributes exactly once to both scopes. A
parent-local allowance cannot bypass the global ceiling, and unused capacity
under one parent cannot be borrowed without a governed reallocation.

### I-3 Close Admission Before Abort Traversal

An accepted abort first closes admission for the target subtree. Only then may
the controller enumerate descendants. This prevents a racing child admission
from appearing after the cascade boundary was established.

Active descendants settle leaf-first in deterministic reverse topological
order. A descendant already terminal is observed, not cancelled again.
Cancellation is cooperative unless a separately authorized execution owner
defines a stronger termination mechanism.

### I-4 Exactly-Once Budget Release

Only the owner of a successful reservation may emit its release. Release is
bound to the reservation ID and is idempotent:

- a reservation is released at most once;
- a non-acquired reservation cannot be released;
- counters never become negative;
- retry/replay returns the existing release receipt;
- parent and global counters update in the same settlement transaction.

For every scope, reconciliation must hold:

`acquired = active + released`

### I-5 Per-Parent Completion Serialization

Child settlements for the same parent enter one ordered completion lane with a
monotonic parent settlement sequence. Exactly one evaluator may decide the
parent continuation for a given sequence.

A child completion contributes once. Duplicate or late events are replayed or
rejected and cannot wake the parent again. The parent wakes only when its
declared join policy is satisfied; sibling completion order must not change the
resulting continuation decision.

Different parents may settle concurrently when they do not share a governed
resource or global-budget transaction.

### I-6 Settlement Is One Logical Boundary

Terminal child outcome, reservation release, budget reconciliation, parent
completion registration and possible wake decision form one logical
settlement boundary. If storage cannot commit it atomically, the durable ledger
must make partial progress detectable and replayable without double release or
double wake.

## Required Receipts

| Receipt | Minimum identity | Required evidence |
| --- | --- | --- |
| Reservation | graph, parent, child attempt, reservation, idempotency key | parent/global limits, counters before/after, authority hash |
| Admission close | graph, subtree root, abort request | accepted sequence and no-new-child boundary |
| Child settlement | reservation and attempt | terminal outcome, settlement sequence, release result |
| Budget reconciliation | parent and global scopes | acquired, active, released, invariant result |
| Parent continuation | parent and join policy | contributing child settlements, decision, wake count |

Receipts are metadata evidence. They must not contain raw prompts, secrets,
provider payloads, or unrestricted child output.

## Failure Semantics Matrix

| Failure | Required behavior |
| --- | --- |
| Two children race for the last slot | one reservation succeeds; all others fail without dispatch or counter change |
| Parent abort races with child admission | admission-close sequence decides; no reservation after that boundary is valid |
| Abort replay | existing cascade/release receipts return; no counter or wake changes |
| Child completes during cascade | one terminal settlement wins; the other path observes/replays it |
| Duplicate child completion | reject or replay; never increment join count or wake count twice |
| Storage interruption during settlement | recovery detects incomplete boundary and resumes from durable receipts |
| Cross-parent global-cap race | global reservation transaction admits only capacity available at its sequence |
| Late completion after parent wake | record duplicate/late evidence; do not run parent continuation again |

## Deterministic Runtime Acceptance Cases

Any future implementation must prove at least:

1. last-slot contention under two concurrent reservation attempts;
2. parent abort versus new-child admission race;
3. cascade across a three-level descendant tree;
4. duplicate abort and duplicate completion replay;
5. child completion during cascade;
6. exactly-once parent/global budget release;
7. sibling completion permutations producing one identical parent decision;
8. crash/replay between terminal outcome and final settlement receipt.

The initial coordinator/launcher suite covers eight focused reservation,
capacity, cascade, release, completion and consumer-integration cases. Passing
those tests is integration evidence, not completion of this stronger list;
race interleavings and crash/replay remain required in representative proof.

## Runtime Admission Gate

Runtime work may open only when all are true:

- a named MAO non-test consumer exists;
- one listed race/failure is reproduced or the consumer explicitly requires
  the composed guarantee before activation;
- current MAO owners accept the smallest implementation surface;
- storage and receipt ownership are named;
- deterministic negative cases and rollback are predeclared;
- expected value exceeds implementation and review cost.

Until representative proof passes, current code is a bounded provider-free
integration, not an assertion that every invariant is durably enforced across
all restart, storage-interruption or concurrent-process boundaries.

## Source Absorption Disposition

The Brigade-derived value is `RUNTIME_INTEGRATED_USE_PENDING`. The source
contributed the need to treat reservation, cascade, release and completion as
one failure-semantics chain. CVF terminology, authority, invariants, receipts,
tests and runtime gate are defined here and remain owned by CVF. The native
coordinator is integrated into `MaoOperationalWorkerLauncher`; deterministic
integration tests pass, while representative use proof still requires the
operator checkpoint. Therefore the absorption status remains
`ABSORPTION_NOT_COMPLETE`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This standard normalizes the knowledge gap and now binds to a provider-free
coordinator in the existing worker launcher. It does not implement process
termination, an event bus, provider routing or production runtime, and it does
not claim `ABSORPTION_COMPLETE_USE_PROVEN` before the representative pilot.
