# GC-018 Baseline — KGR1 Knowledge Graph Retrieval Wave 1

Memory class: SUMMARY_RECORD

Status: ACTIVE

Date: 2026-06-01

## Purpose

Authorize a bounded local implementation of Knowledge Graph Retrieval in the
Learning Plane Foundation after the KGR absorption prereview identified graph
retrieval value in the legacy Graphify corpus.

## Decision / Baseline

Decision: `APPROVED_LOCAL_ONLY`.

Baseline: KGR1 may implement local deterministic schema, builder, and retrieval
policy integration in LPF. KGR1 may not claim live proof, public readiness, or
runtime persistence mutation.

## Proposed Tranche

KGR1 Wave 1 proposed tranche is T1-T4 local-only implementation with T5 held for
separate live provider proof.

## Scope

KGR1 covers:

- T1: doc-only absorption of the Graphify knowledge graph retrieval concepts.
- T2: in-memory TypeScript KGR node, edge, store, and guard-policy schema.
- T3: deterministic in-process graph builder with no file I/O and no external
  AST or graph library.
- T4: local `MemoryRetrievalPolicyOptions.kgrStore` integration for
  `graph_search`.

KGR1 does not close live provider proof. T5 remains `HOLD_LIVE_PROVIDER_PROOF`
until a separate live-governance proof run is authorized and executed.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| KGR source corpus exists | `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_DATA_MODEL.md` | active IDE source context and KGR prereview | `CVF_GRAPH_MEMORY_DATA_MODEL.md` | KGR absorption source | ACCEPT |
| LPF retrieval owner exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | existing `graph_search` method | `evaluateRetrievalRequest` | `MemoryRetrievalPolicyOptions` | ACCEPT |
| LPF barrel owner exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` | root export barrel | `src/index.ts` | LPF public export surface | ACCEPT |

## Constraints

- No vector database.
- No remote service.
- No prompt reinjection.
- No raw memory release.
- No public-sync.
- No live proof claim in this baseline.

## Claim Boundary

This baseline authorizes local deterministic KGR schema, builder, and retrieval
policy integration only.

## Final Boundary

Not a final KGR product closure. T5 live proof remains explicitly held.

## Verification Boundary

Verification is limited to local TypeScript check and focused Vitest tests until
live provider proof is separately authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: KGR1 is private provenance work and has not been exported to the public
CVF repository.
