# CVF Phase 2.B Safety External Policy Risk Fanout Migration Codex Rebuttal

Memory class: FULL_RECORD

Status: NON_BLOCKING_WITH_BOUNDARY_LOCK

docType: review

Reviewer: Codex

Date: 2026-05-21

---

## Verdict

NON_BLOCKING_WITH_BOUNDARY_LOCK.

The requested chains may proceed together because they are additive
adapter/snapshot closures over already-existing risk and policy decisions.
They must not be treated as new runtime enforcement, live governance proof,
provider behavior, Maika behavior, or public capability evidence.

---

## Purpose

Review whether the requested safety-tail, external/ecosystem risk fanout, and
external policy chains can proceed as a single bounded Phase 2.B tranche without
widening governance claims.

---

## Reviewed Chains

- Safety Tail Risk Chain: `R-02 -> R-04 / R-05 / R-15 / R-16`
- External / Ecosystem Risk Fanout:
  `R-01 -> R-06 / R-07 / R-08 / R-09 / R-10 / R-11 / R-12`
- External policy chain: `P-01 -> P-07 / P-08`

---

## Scope Gate

Allowed:

- versioned adapter snapshots;
- `WithAdapter` helpers that preserve existing outputs;
- focused conformance tests;
- docs/session closure packet.

Forbidden:

- new risk or policy engine semantics;
- provider runtime or live API calls;
- Maika, memory, database schema, public-sync, or public catalog changes;
- kernel owner replacement;
- global freeze lift;
- Claude participation or co-signature claim.

---

## Evidence Trace Block

| Claim | Evidence required | Rebuttal result |
| --- | --- | --- |
| Safety-tail risk surfaces can be wrapped | Existing safety runtime and hardening scorer/gate/lock outputs remain unchanged | non-blocking |
| Ecosystem risk fanout can be wrapped | Existing scorer/aggregator/guard outputs remain unchanged | non-blocking |
| External policy surfaces can be wrapped | Existing certification and policy decisions remain unchanged | non-blocking |
| Live governance behavior is not proved | No release gate or provider call is in scope | boundary locked |

---

## Decision

Proceed under a fresh GC-018 and work order limited to these chains. Completion
must report tests and any package-tooling boundary honestly.

---

## Findings / Position

Position: NON_BLOCKING_WITH_BOUNDARY_LOCK.

Findings:

- The chains are structurally compatible because each target already returns a
  local risk/policy decision or score.
- The safe closure mechanism is additive adapter snapshots, not replacement of
  engines.
- The tranche is unsuitable as live governance proof because it does not
  exercise a runtime/provider path.

---

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Adapter becomes a new risk engine | Preserve existing direct output and test wrapped output against it |
| Fanout is overclaimed as runtime proof | Mark no-live-proof boundary in GC-018 and completion |
| External policy adapters widen certification semantics | Keep transition/evaluate behavior unchanged |
| Claude dependency is implied | Record Codex-only role chain |

---

## Claim Boundary

This rebuttal clears only the bounded adapter/snapshot migration. It does not
clear broad Phase 2.B bulk migration, provider runtime behavior, Maika behavior,
persistent memory, database schema migration, public-sync, public catalog
claims, live governance proof, Claude review, kernel owner replacement, or
global freeze release.
