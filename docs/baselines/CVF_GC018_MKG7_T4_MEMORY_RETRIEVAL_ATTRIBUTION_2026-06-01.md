# CVF GC-018 - MKG7-T4 Memory Retrieval Attribution

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize MKG7-T4: extend the existing retrieval result
(`MemoryRetrievalResult` @ `memory-retrieval-policy.ts:40`) with attribution
fields — source, freshness, rank reason, and exclusion reason — without
releasing raw candidate content. T4 is a delta on the existing retrieval
surface, not a new retrieval engine.

## Scope / Target / Owner Boundary

Target owner surfaces:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-attribution.ts` (NEW — attribution schema/helper)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-attribution.test.ts` (NEW)
- `docs/reviews/CVF_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_COMPLETION_2026-06-01.md` (NEW)

Source-of-truth files (read-only):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` — existing `MemoryRetrievalResult`, `MemoryRetrievalCandidate`, `evaluateRetrievalRequest`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts` — subpath export, may be extended

Boundary: additive attribution helper only; must not modify `evaluateRetrievalRequest`
or `MemoryRetrievalResult` in the existing file; no raw `content` release; no
provider calls; no public-sync.

## Decision

Authorize T4 as an additive attribution layer: new helper file that wraps
or annotates an existing `MemoryRetrievalResult`, adds source/freshness/rank/
exclusion evidence, and omits raw candidate `content`. Leave pending and
uncommitted.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Existing retrieval result | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts:40` | ACCEPT_AS_READ_ONLY — must not be modified |
| Retrieval candidate (has optional `content`) | `memory-retrieval-policy.ts:16` | ACCEPT_AS_READ_ONLY — `content` must be stripped in attribution output |
| `evaluateRetrievalRequest` | `memory-retrieval-policy.ts:88` | ACCEPT_AS_READ_ONLY |

## Source / Predecessor Evidence

- `MemoryRetrievalResult` (line 40): has `selected`, `excluded`, `rawMemoryReleased:false`, `method`, `status`, `reason`.
- `MemoryRetrievalCandidate` (line 16): has optional `content` — attribution output must not include this field.
- Existing exclusion reasons already present: `out_of_scope`, `privacy_filtered`, `lifecycleState`, `low_relevance` (lines 167–180).

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

Bounded LPF owner set. No Legacy folder absorption. `N/A with reason`.

### Gate 2 - Prior Absorption Resolution

MKG1–MKG6 closed, T1 contract complete.

### Gate 3 - File-Level Value Extraction

Attribution output must answer: authority source, freshness (createdAt), rank
reason (auditTrust score basis), exclusion reason (already in excluded array),
stale/partial/complete status, raw-content boundary. All derivable from existing
`MemoryRetrievalResult` without raw `content`.

### Gate 4 - Owner-Surface Normalization

New attribution helper lives in LPF alongside the existing retrieval policy. It
consumes but does not modify the existing result shape.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Attribution layer over existing result | ACCEPT_NOW | additive, no raw content |
| Modifying `evaluateRetrievalRequest` | REJECT_DIRECT | delta only |
| Raw candidate `content` in output | REJECT_DIRECT | forbidden by boundary |

### Gate 6 - Adversarial Role Review

Risk: attribution output leaks raw `content` field from `MemoryRetrievalCandidate`.
Required: attribution schema must explicitly exclude the `content` field; tests
must assert absence.

### Gate 7 - Thin Proof And Closure Delta

New attribution file, focused tests asserting attribution fields present and
raw `content` absent, LPF `npm run check` PASS, file-size guard PASS.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- attribution helper with source/freshness/rank/exclusion fields;
- focused tests: attribution fields populated, raw `content` absent, `rawMemoryReleased=false` preserved;
- LPF `npm run check` PASS;
- file-size guard PASS;
- pending completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T4 authorizes an additive attribution helper over the existing retrieval result.
Does not authorize modifying the retrieval engine, releasing raw content,
provider calls, prompt injection, persistence mutation, public-sync, or push.
