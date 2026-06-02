# CVF KGR1 Knowledge Graph Retrieval — Wave 1 Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-01

GC-018: `docs/baselines/CVF_GC018_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_WAVE1_2026-06-01.md`

## Purpose

Turn the absorbed Graphify knowledge graph retrieval concept into a bounded LPF
implementation with deterministic local KGR retrieval and one targeted live
provider proof of graph-assisted retrieval value. This does not claim runtime
persistence, prompt reinjection, web-route graph integration, public readiness,
hosted readiness, or production readiness.

## Authorization / Decision

Authorized decision: `REVIEW_READY_LIVE_PROVEN_BOUNDED`.

The roadmap accepts local KGR implementation and the follow-on T5 live proof
recorded in
`docs/reviews/CVF_KGR1_T5_LIVE_PROVIDER_PROOF_COMPLETION_2026-06-02.md`.

## Scope

In scope: KGR schema/store, deterministic local graph builder, LPF barrel
exports, `graph_search` integration via injected `kgrStore`, focused local
tests, and targeted Alibaba live provider proof.

## Non-Goals

- No vector database.
- No web-route live governance proof.
- No prompt reinjection.
- No public-sync or push.
- No production-readiness claim.

## Work Plan

| Tranche | Scope | Status | Evidence |
| --- | --- | --- | --- |
| KGR1-T1 | Absorb Graphify retrieval concepts into CVF owner surfaces | REVIEW_READY_LOCAL_ONLY | KGR prereview + this roadmap |
| KGR1-T2 | Add KGR node, edge, store, and guard-policy schema | REVIEW_READY_LOCAL_ONLY | `knowledge-graph-store.ts` + focused tests |
| KGR1-T3 | Add deterministic in-process graph builder | REVIEW_READY_LOCAL_ONLY | `knowledge-graph-builder.ts` + full-output projection test |
| KGR1-T4 | Add local `kgrStore` branch to `graph_search` retrieval | REVIEW_READY_LOCAL_ONLY | `memory-retrieval-policy.kgr.test.ts` |
| KGR1-T5 | Live provider proof of graph-assisted retrieval value | REVIEW_READY_LIVE_PROVEN_BOUNDED | `knowledge-graph-live.alibaba.test.ts` PASS |

## Acceptance Criteria

- KGR local tests pass.
- LPF TypeScript check passes.
- KGR docs state bounded LPF-layer claim boundary.
- T5 targeted live provider proof passes.
- No unrelated archive or governance batch is included in KGR closure.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Retrieval policy accepts graph search | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | `MemoryRetrievalMethod` union | `graph_search` | `evaluateRetrievalRequest` | ACCEPT |
| KGR store implementation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-store.ts` | file created in this batch | `KgrStore` | LPF KGR local store | ACCEPT |
| KGR builder implementation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-builder.ts` | file created in this batch | `buildKnowledgeGraph` | LPF KGR local builder | ACCEPT |

## Verification Plan

- `npm test -- tests/knowledge-graph-store.test.ts tests/knowledge-graph-builder.test.ts tests/memory-retrieval-policy.kgr.test.ts tests/memory-retrieval-policy.test.ts`
- `npm test -- tests/knowledge-graph-live.alibaba.test.ts`
- `npm run check`
- Markdown structural, public export, finding-learning, and governed file-size
  gates before any closure claim.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Next control action |
| --- | --- | --- | --- |
| Prior worker claimed live proof while evidence was mocked/local only | RULE_GAP | GOVERNANCE_CONTROL_PLANE | HANDLED — T5 now has targeted live provider test evidence |
| Prior worker staged unrelated archive changes while fixing KGR findings | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE — closure review must compare changed files to allowed scope |

`autonomousMutationAuthorized=false`

## Claim Boundary

KGR1 Wave 1 proves deterministic schema/builder behavior, local graph retrieval
policy wiring, and one bounded live provider response using KGR-selected
context. It does not prove web-route integration, durable vector persistence,
production retrieval quality, or public readiness.

## Final Boundary

This roadmap is final for KGR1 Wave 1 at the bounded LPF KGR layer. It is not
final product closure for web-route graph retrieval, durable graph persistence,
or public release.

## Verification Boundary

Verification includes local TypeScript, focused Vitest, and a targeted Alibaba
`qwen-turbo` live provider test using KGR-selected context. No hosted app,
public-sync, web-route graph integration, or push proof is claimed.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Public-sync boundary: no KGR1 artifacts are to be copied to the public-sync
remote (`Controlled-Vibe-Framework-CVF-public-sync`) until a separate governed
public readiness review authorizes it.

Reason: KGR1 remains private provenance work pending later public readiness
review.
