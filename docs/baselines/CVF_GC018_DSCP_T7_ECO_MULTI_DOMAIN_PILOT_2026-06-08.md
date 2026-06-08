# CVF GC-018 DSCP-T7 ECO Multi-Domain Pilot Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-08

---

## Authorization

Authorized by operator instruction 2026-06-08: implement DSCP-T7 ECO
multi-domain pilot. Operator confirmed all 3 DSCP extension candidates
(T6, T7, T8) have value. T7 follows T6 closure.

## Decision

Decision: implement `buildECOGovernedPackRequest()` as a new deterministic
adapter in `CVF_ECO_v1.4_RAG_PIPELINE`. This adapter maps `RAGResult`
(ECO retrieval output) into `GovernedContextPackRequest` (DSCP pack input),
proving the "domain-agnostic" claim. No modification of existing ECO files.

## Purpose

Prove that the DSCP pack-layer contract (`GovernedContextPackRequest`) is
genuinely domain-agnostic by bridging the ECO RAG retrieval domain.
`buildECOGovernedPackRequest()` maps `RAGDocument[]` from ECO into
`KnowledgeItem[]` expected by `ContextPackagerRequest`.

## Predecessor Evidence

- DSCP-T2: `GovernedContextPackRequest`, `GovernanceContextEnvelope` interfaces.
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
- ECO `RAGResult`, `RAGDocument`, `RAGQuery` types:
  `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` lines 23-38
- ECO `Retriever` class (read-only reference for type awareness):
  `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/retriever.ts`
- DSCP-T6: `buildGovernedArtifactDescriptor()`. `CLOSED_PASS_BOUNDED` pending reviewer.

## Scope / Target / Owner Boundary

**In scope:**
- New file: `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts`
- New file: `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/tests/dscp.eco.adapter.test.ts`
- Function: `buildECOGovernedPackRequest(ragResult: RAGResult, envelope: GovernanceContextEnvelope): GovernedContextPackRequest`
- Mapping: `RAGDocument.content` → `KnowledgeItem.content`; `RAGDocument.id` → `KnowledgeItem.id`; `RAGDocument.score` → metadata

**Out of scope:**
- No modification of `retriever.ts`, `types.ts`, `document.store.ts`, or any existing ECO file.
- No live ECO retrieval query, provider call, or corpus ingestion.
- No T12 authorization, public-sync, or production readiness.

## Evidence / Verification

Predecessor source surfaces verified at `10b02a79`:

| Surface | File | Lines | Status |
|---|---|---|---|
| `RAGResult` interface | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | 30-38 | VERIFIED |
| `RAGDocument` interface | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | 23-29 | VERIFIED |
| `GovernedContextPackRequest` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | 78-84 | VERIFIED |
| `GovernanceContextEnvelope` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | 58-73 | VERIFIED |
| `ContextPackagerRequest.knowledgeItems` field | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | (to be verified by worker) | ACCEPT_PENDING_WORKER |

Acceptance verification: `tsc --noEmit` PASS + focused vitest all PASS + all 4
governance gates COMPLIANT on committed range.

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| `buildECOGovernedPackRequest()` compiles | `tsc --noEmit` PASS |
| Non-empty RAGResult maps to populated request | vitest PASS |
| Empty RAGResult maps to empty knowledgeItems | vitest PASS |
| RAGDocument fields preserved in KnowledgeItem | vitest PASS |
| GovernanceContextEnvelope passed through | vitest PASS |
| No existing ECO file modified | `git diff --name-status` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_FOR_CLAUDE_2026-06-08.md` | `Status: DISPATCHED` | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md` | reviewer-owned pending | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_ROADMAP_2026-06-08.md` | `Status: DISPATCHED` | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer-owned session sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| External evidence digest | no external artifact | no external authorized | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new adapter function only | N/A with reason: helper function only |
| Session continuity | active handoff | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |

## Claim Boundary

This baseline authorizes `buildECOGovernedPackRequest()` as a deterministic
local ECO adapter. It does not claim: runtime provider behavior, live ECO
query proof, corpus ingestion, answer quality, public readiness, production
readiness, T12 authorization, or public-sync.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.
