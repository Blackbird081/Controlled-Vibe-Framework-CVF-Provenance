# CVF GC-018 - MKG7-T5 Memory Durable Write Readiness

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize MKG7-T5: wire a bounded readiness/read surface over the existing
durable store and pin its already-fail-closed write behavior with regression
tests. The durable store (`durable-memory-store.ts`) already exists with an
active `write()` that fails closed (`!actorAuthorized || policyDecision !== "allow"`
→ denied, line 201) and `read()` that requires `actorAuthorized` (line 312).
T5 does NOT add new mutation authority — it proves and pins the existing
guarantees and prepares a bounded read surface.

## Scope / Target / Owner Boundary

Target owner surfaces:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-durable-readiness.ts` (NEW — bounded read adapter)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-durable-readiness.test.ts` (NEW — includes write deny-branch regression tests)
- `docs/reviews/CVF_MKG7_T5_MEMORY_DURABLE_WRITE_READINESS_COMPLETION_2026-06-01.md` (NEW)

Source-of-truth files (read-only):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` — existing store (must not be modified)
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` — T1 contract

Boundary: additive readiness layer only; existing `durable-memory-store.ts` must
not be modified; no new write path authorized without separate GC-018; no route
changes; no provider calls; no public-sync.

## Decision

Authorize T5 as a bounded readiness layer: new helper that wraps the existing
read path plus regression tests that pin the existing write deny-branches.
Worker must not modify `durable-memory-store.ts`. Leave pending and uncommitted.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Durable store (read-only for T5) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` (456 lines) | ACCEPT_AS_READ_ONLY — must not be modified |
| Write fail-closed branch | `durable-memory-store.ts:201` | ACCEPT_AS_REGRESSION_TARGET — pin with tests |
| Read auth branch | `durable-memory-store.ts:312` | ACCEPT_AS_REGRESSION_TARGET — pin with tests |
| Provenance floor | `MIN_PROVENANCE_SCORE` at `durable-memory-store.ts:98` | ACCEPT_AS_REGRESSION_TARGET |

## Source / Predecessor Evidence

Verified fail-closed branches (source-confirmed 2026-06-01):

- Write deny: `!input.actorAuthorized || input.policyDecision !== "allow"` → `decision:"denied"` (line 201).
- Read deny: `!input.actorAuthorized` → `decision:"denied"` (line 312).
- Provenance floor: `MIN_PROVENANCE_SCORE = 0.7` (line 98).
- Receipt invariants: `summaryOnly:true`, `canReinject:false`, `rawMemoryReleased:false`.

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

Bounded LPF owner set. No Legacy folder absorption. `N/A with reason`.

### Gate 2 - Prior Absorption Resolution

MKG1–MKG6 closed, T1 contract complete.

### Gate 3 - File-Level Value Extraction

Readiness layer provides a bounded `readMemory(input)` that calls the existing
`DurableMemoryStore.read()` and returns only `summary`, `scope`, `tier`, and
the receipt — no raw `content`. Tests pin all three deny-branches.

### Gate 4 - Owner-Surface Normalization

New readiness helper wraps existing store. Does not replace it. Receipt
invariants propagated from existing store.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Bounded read adapter | ACCEPT_NOW | wires readiness surface without mutation |
| Write deny-branch regression tests | ACCEPT_NOW | pins existing guarantees |
| New write path / route mutation | REJECT_DIRECT — requires separate GC-018 | T5 is readiness only |
| Modifying `durable-memory-store.ts` | REJECT_DIRECT | read-only source |

### Gate 6 - Adversarial Role Review

Risk: worker adds a new write path bypassing the existing deny-branch.
Required: diff must show zero edits to `durable-memory-store.ts`; all write
tests must exercise the existing deny-branch, not bypass it.

### Gate 7 - Thin Proof And Closure Delta

New readiness helper, regression tests covering write-denied (unauthorized),
write-denied (policy not allow), write-denied (provenance below floor),
read-denied (unauthorized), read-allowed (authorized + valid tier), and receipt
invariant assertions. LPF `npm run check` PASS, file-size guard PASS.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- new readiness helper returning summary-only read result;
- regression tests: 5+ deny/allow scenarios, receipt invariants asserted;
- zero edits to `durable-memory-store.ts` (verify with `git diff --name-status`);
- LPF `npm run check` PASS;
- file-size guard PASS;
- pending completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T5 authorizes a bounded readiness layer and regression tests over the existing
durable store only. Does not authorize new write paths, route integration,
provider calls, raw Memory release, prompt injection, any mutation of
`durable-memory-store.ts`, public-sync, or push.
