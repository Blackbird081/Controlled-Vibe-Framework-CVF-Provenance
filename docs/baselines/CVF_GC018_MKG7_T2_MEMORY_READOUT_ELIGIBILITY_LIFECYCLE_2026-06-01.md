# CVF GC-018 - MKG7-T2 Memory Readout-Eligibility Lifecycle

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize MKG7-T2: add a deterministic readout-eligibility lifecycle policy
distinct from the existing tier-state machine
(`memory-lifecycle-policy.ts:evaluateLifecycleTransition`). The existing policy
governs tier transitions (working/episodic/semantic/procedural/expired/
disputed/forgotten). T2 adds an orthogonal policy that answers: is a given
Memory candidate eligible to appear in the readout surface right now?

T2 is an additive delta. It must not modify the existing tier machine.

## Scope / Target / Owner Boundary

Target owner surfaces (NEW):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-readout-eligibility-policy.test.ts`
- `docs/reviews/CVF_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_COMPLETION_2026-06-01.md`

Source-of-truth files (read-only):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` — existing tier machine, must not be modified
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts` — subpath export, may be extended
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` — T1 contract, defines boundary

Boundary: additive delta only; `rawMemoryReleased=false` and `canReinject=false`
on the readout/advisory surface; no route changes, no provider calls, no prompt
injection, no persistence mutation, no public-sync.

## Decision

Authorize T2 as a bounded additive delta: one new policy file + focused tests.
Worker must not modify `memory-lifecycle-policy.ts` or LPF root `index.ts`.
Leave pending and uncommitted.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Existing tier machine (read-only) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | ACCEPT_AS_READ_ONLY |
| LPF subpath export | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts` | ACCEPT — may add export if within Allowed scope |

## Source / Predecessor Evidence

- MKG7-T1 contract (`docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`) defines the readout-eligibility boundary.
- Existing `MemoryLifecycleState` (lines 4–11 @ `memory-lifecycle-policy.ts`) is the tier model; the new eligibility states are orthogonal.

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

Bounded LPF owner set. No Legacy folder absorption. Filesystem corpus listing is
`N/A with reason`.

### Gate 2 - Prior Absorption Resolution

MKG1–MKG6 closed, MKG7-T1 complete.

### Gate 3 - File-Level Value Extraction

Six new readout-eligibility states: `READOUT_ALLOWED`, `READOUT_DENIED`,
`STALE_NEEDS_REFRESH`, `REVOKED`, `NO_AUTHORITY_SOURCE`,
`OUT_OF_SCOPE_FOR_ACTOR`. Policy enforces `rawMemoryReleased=false` and
`canReinject=false` on the output surface.

### Gate 4 - Owner-Surface Normalization

New file sits alongside the existing lifecycle policy in LPF. Does not replace
the tier machine. LPF barrel may optionally re-export the new type.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| New readout-eligibility policy | ACCEPT_NOW | needed by T3 for route integration |
| Modifying existing tier machine | REJECT_DIRECT | additive delta only |
| Route integration | DEFER_TO_T3 | T3 owns route wire-in |

### Gate 6 - Adversarial Role Review

Risk: worker merges eligibility states into the existing tier machine. Required:
keep the two files separate; `evaluateLifecycleTransition` must remain unchanged.

### Gate 7 - Thin Proof And Closure Delta

New policy file covering all 6 states, focused unit tests, LPF `npm run check`
PASS, governed file-size guard PASS, pending completion review.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- new policy file with all 6 eligibility states and invariant enforcement;
- focused tests: all 6 states covered, `rawMemoryReleased=false` and `canReinject=false` asserted;
- LPF `npm run check` PASS;
- `python governance/compat/check_governed_file_size.py --enforce` PASS;
- pending completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T2 authorizes a new readout-eligibility policy helper and tests only. Does not
authorize route changes, provider calls, prompt injection, persistence mutation,
tier-machine modification, public-sync, or push.
