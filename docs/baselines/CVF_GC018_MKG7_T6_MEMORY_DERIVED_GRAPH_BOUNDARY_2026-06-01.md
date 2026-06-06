# CVF GC-018 - MKG7-T6 Memory Derived Graph Boundary

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize MKG7-T6: produce a documentation-only reference packet that records
the boundary between source authority and rebuildable derived views (graph,
semantic-region, Palace, summary, cache, snapshot, retrieval indexes). This
packet makes the boundary explicit and drift-detectable so that future agents
do not treat derived graph lookups as overriding source authority.

T6 is documentation-only. No runtime/source code changes.

## Scope / Target / Owner Boundary

Target owner surfaces (NEW):

- `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_COMPLETION_2026-06-01.md`

Source-of-truth files (read-only):

- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` — T1 contract
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` — chain produces derived views
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` — graph method in retrieval

Boundary: documentation-only; no runtime/source edits; no graph persistence
mutation; no public-sync.

## Decision

Authorize T6 as a documentation-only boundary reference packet. Worker must not
edit any `.ts` file. Leave pending and uncommitted.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Workflow chain (produces derived views) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | ACCEPT_AS_CONTRACT_SOURCE |
| Retrieval graph method | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | ACCEPT_AS_CONTRACT_SOURCE |

## Source / Predecessor Evidence

- T1 contract documents the advisory-only boundary.
- Workflow chain produces `contextBlock` (derived summary), not source authority.
- Retrieval policy `MemoryRetrievalMethod` includes `graph` method but output is still a `MemoryRetrievalResult` with `rawMemoryReleased:false`.

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

Documentation-only tranche. No Legacy folder absorption. `N/A with reason`.

### Gate 2 - Prior Absorption Resolution

MKG1–MKG6 closed, T1 contract complete.

### Gate 3 - File-Level Value Extraction

The boundary document must state: source authority files are primary; derived
views (graph nodes, summaries, semantic-region maps, cache) are rebuildable from
source; graph lookup cannot overrule source authority; public or runtime claims
from derived views require separate live proof.

### Gate 4 - Owner-Surface Normalization

Single reference document under `docs/reference/`. No owner-surface changes.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Derived-graph boundary reference doc | ACCEPT_NOW | documentation-only |
| Graph persistence mutation | REJECT_DIRECT | out of scope for T6 |
| Public claims from derived views | DEFER — requires live proof | T6 records boundary only |

### Gate 6 - Adversarial Role Review

Risk: boundary document is vague enough to be read as authorizing graph lookups
as source authority. Required: document must explicitly state that derived views
cannot overrule source authority and that drift is detectable.

### Gate 7 - Thin Proof And Closure Delta

Reference document with explicit source-vs-derived boundary, markdown structural
completeness gate PASS, public-export gate PASS.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- reference document with source-vs-derived boundary and drift-detectability statement;
- markdown structural completeness gate PASS;
- public-export gate PASS;
- pending completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T6 authorizes a documentation-only derived-graph boundary reference packet. Does
not authorize graph persistence mutation, new retrieval routes, provider calls,
raw Memory release, prompt injection, public-sync, or push.
