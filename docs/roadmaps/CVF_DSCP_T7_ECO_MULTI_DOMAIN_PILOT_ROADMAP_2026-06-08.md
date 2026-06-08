# CVF DSCP-T7 ECO Multi-Domain Pilot Roadmap

Memory class: FULL_RECORD

Status: HOLD_UNTIL_T6_PASS

docType: roadmap

Date: 2026-06-08

---

## Authorization

Authorized by operator instruction 2026-06-08: prepare `buildECOGovernedPackRequest()`
ECO adapter inside `CVF_ECO_v1.4_RAG_PIPELINE`.
GC-018: `docs/baselines/CVF_GC018_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_2026-06-08.md`.
Predecessor: DSCP-T6 PASS is required before T7 execution. This roadmap remains
`HOLD_UNTIL_T6_PASS` until the reviewer commits DSCP-T6 and refreshes
dependency-release evidence.

## Purpose

Prove DSCP domain-agnostic claim by bridging ECO RAG retrieval output into the
DSCP governed context pack input. `buildECOGovernedPackRequest()` maps
`RAGResult.documents` into `KnowledgeItem[]` for `ContextPackagerRequest`,
then wraps the result in `GovernedContextPackRequest` with the caller-supplied
`GovernanceContextEnvelope`. No existing ECO file is modified.

## Scope / Target / Owner Boundary

**In scope:**
- `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts`
- `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/tests/dscp.eco.adapter.test.ts`
- Input/result types exported from the new adapter file
- Mapping: `RAGDocument.content` -> `KnowledgeItem.content`; `RAGDocument.id` -> `KnowledgeItem.itemId`; `RAGDocument.title` -> `KnowledgeItem.title`

**Out of scope:**
- No modification of `retriever.ts`, `types.ts`, `document.store.ts`, or any existing ECO file.
- No live ECO retrieval query, provider call, or corpus ingestion.
- No T12 authorization, public-sync, or production readiness.

## Non-Goals

- No live retrieval or embedding call.
- No modification of existing ECO source files.
- No corpus ingestion, OCR, or chunking.
- No provider call or LLM query.
- No T12 authorization.
- No public-sync or production readiness.

## Predecessor Evidence

- DSCP-T2 `GovernedContextPackRequest`:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` lines 78-84
- ECO `RAGResult`, `RAGDocument`:
  `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` lines 23-38
- DSCP-T6 `buildGovernedArtifactDescriptor()`: CPF scan-side (pending T6 reviewer commit)

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | HOLD_UNTIL_T6_PASS |
| 2 | Work order | HOLD_UNTIL_T6_PASS |
| 3 | Implement `dscp.eco.adapter.ts` | PENDING |
| 4 | Implement `dscp.eco.adapter.test.ts` | PENDING |
| 5 | tsc --noEmit + vitest + governance gates | PENDING |
| 6 | Worker return | PENDING |

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| Source file compiles | `tsc --noEmit` PASS |
| Non-empty RAGResult maps correctly | vitest PASS |
| Empty RAGResult maps to empty knowledgeItems | vitest PASS |
| RAGDocument fields preserved | vitest PASS |
| GovernanceContextEnvelope passed through | vitest PASS |
| No existing file modified | `git diff --name-status` |
| All 4 governance gates | gate runner |

## Verification

| Check | Command | Required result |
|---|---|---|
| TypeScript compilation | `npx tsc --noEmit` in `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/` | 0 errors |
| Focused vitest | `npx vitest run tests/dscp.eco.adapter.test.ts` | all PASS |
| Structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |
| Finding-to-governance | `python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |
| Machine closure package | `python governance/compat/check_machine_closure_package.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |

## Acceptance Receipt Assertion Matrix

DSCP-T7 produces no retrieval receipt. It builds an ECO-to-DSCP adapter only.

| Required value | Observed value | Status |
|---|---|---|
| Adapter compiles | `tsc --noEmit` PASS | PENDING_WORKER_RETURN |
| RAGResult mapping correct | vitest PASS | PENDING_WORKER_RETURN |
| No provider call | no live ECO retrieval | N/A with reason: deterministic local only |
| No corpus ingestion | adapter is type mapping only | N/A with reason: no corpus mutation |
| No T12 authorization | T7 does not authorize T12 | N/A with reason: T12 requires separate authorization |

## T12 Gate Hard Invariant (Carried Forward)

T12 remains NOT YET AUTHORIZED. This tranche does not authorize T12.

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_FOR_CLAUDE_2026-06-08.md` | `Status: HOLD_UNTIL_T6_PASS` | BLOCKED with reason: dependency not released |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md` | reviewer-owned pending | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Roadmap state | this file | `Status: HOLD_UNTIL_T6_PASS` until reviewer release | BLOCKED with reason: dependency not released |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| External evidence digest | no external authorized | N/A | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new adapter function only | N/A with reason: helper function only |
| Session continuity | active handoff | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |

## Claim Boundary

This roadmap claims: tranche plan, scope, predecessor evidence, and acceptance
criteria for DSCP-T7. It does not claim: runtime provider behavior, live proof,
corpus ingestion, public readiness, production readiness, or T12 authorization.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced.
