# CVF Agent Work Order: DSCP-T7 ECO Multi-Domain Pilot

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-08

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `10b02a79`

executionBaseHead: `c51a7045`

closureBaseHead: `c51a7045`

---

## Purpose

Prepare Claude to implement `buildECOGovernedPackRequest()` - an ECO-to-DSCP
adapter - inside `CVF_ECO_v1.4_RAG_PIPELINE`. Proves the DSCP domain-agnostic
claim by mapping `RAGResult` into `GovernedContextPackRequest` without
modifying any existing ECO file.

## Authority Chain

Operator instruction 2026-06-08 -> GC-018:
`docs/baselines/CVF_GC018_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_2026-06-08.md`
-> this work order.

Prerequisite release evidence: DSCP-T6 is `CLOSED_PASS_BOUNDED` at closure
commit `13cc1505`; session sync commit `c51a7045`. T7 execution is released
in this batch.

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Implement adapter + tests; author worker return; stage artifacts |
| Reviewer | Codex | Review worker return; run governance gates; commit if PASS |
| Operator | Human | Authorized T7 preparation; owns session sync and registry updates |

## Scope / Target / Owner Boundary

**Allowed scope:**
- Create `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts`
- Create `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/tests/dscp.eco.adapter.test.ts`
- Create `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_WORKER_RETURN_2026-06-08.md`
- Reviewer correction to `docs/baselines/CVF_GC018_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_2026-06-08.md`
- Reviewer closure update to `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md`
- Reviewer closure update to `docs/roadmaps/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_ROADMAP_2026-06-08.md`
- Reviewer closure update to `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`
- Reviewer closure update to `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- Reviewer closure sync to `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Reviewer closure sync to `CVF_SESSION_MEMORY.md`
- Reviewer closure sync to `AGENT_HANDOFF_V17_2026-06-07.md`

**Forbidden scope:** see Forbidden Scope section below.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap section | Work order section | Status |
|---|---|---|
| Goal: implement `buildECOGovernedPackRequest()` | Implementation Contract | TRACED |
| Scope: new adapter file, no existing ECO file modified | Scope / Target / Owner Boundary | TRACED |
| Non-goals: no live ECO retrieval, no provider call | Forbidden Scope | TRACED |
| Acceptance criteria: TypeScript + vitest + gates PASS | Acceptance Criteria | TRACED |
| Verification commands | Evidence Requirements | TRACED |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure that is
within allowed implementation scope (TypeScript errors, vitest failures, markdown
violations) must be repaired and rerun by the worker without escalating to
the operator.

## Required Artifact Manifest

| Artifact | Type | Required path | Proof literal |
|---|---|---|---|
| ECO adapter | new TypeScript source | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | cross-extension TypeScript check 0 errors |
| Test suite | new TypeScript test | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/tests/dscp.eco.adapter.test.ts` | vitest all PASS |
| Worker return | new Markdown review | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_WORKER_RETURN_2026-06-08.md` | all 4 gates COMPLIANT |

## Required First Reads

| File | Purpose |
|---|---|
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | Verify `RAGResult`, `RAGDocument` exact interfaces |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | Verify `GovernedContextPackRequest`, `GovernanceContextEnvelope` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | Verify `ContextPackagerRequest` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.query.contract.ts` | Verify `KnowledgeItem` |
| `docs/baselines/CVF_GC018_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_2026-06-08.md` | Confirm authorized scope |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Clean working tree | `git status --short` | no unexpected modified files |
| Base HEAD confirmed | `git rev-parse --short HEAD` | capture as `executionBaseHead` |
| T6 dependency released | verify DSCP-T6 closure commit and completion packet | PASS with commit evidence |
| ECO adapter does not yet exist | confirm `dscp.eco.adapter.ts` absent | NOT FOUND |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
|---|---|---|---|---|---|
| `RAGResult` interface | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | lines 30-38 | `export interface RAGResult` | `types.ts` | ACCEPT |
| `RAGDocument` interface | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | lines 23-29 | `export interface RAGDocument` | `types.ts` | ACCEPT |
| `GovernedContextPackRequest` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 78-84 | `export interface GovernedContextPackRequest` | `dscp.governed.context.contract.ts` | ACCEPT |
| `GovernanceContextEnvelope` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 58-73 | `export interface GovernanceContextEnvelope` | `dscp.governed.context.contract.ts` | ACCEPT |
| `KnowledgeItem` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.query.contract.ts` | lines 5-11 | `export interface KnowledgeItem` | `knowledge.query.contract.ts` | ACCEPT |

## Implementation Contract

### New file: `dscp.eco.adapter.ts`

**Imports:**
```typescript
import type { RAGResult, RAGDocument } from "./types";
import type {
  GovernedContextPackRequest,
  GovernanceContextEnvelope,
} from "../../CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract";
import type { ContextPackagerRequest } from "../../CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract";
```

**Function (export):**
```typescript
export function buildECOGovernedPackRequest(
  ragResult: RAGResult,
  envelope: GovernanceContextEnvelope,
): GovernedContextPackRequest
```

**Mapping logic:**
- Map each `RAGDocument` to a `KnowledgeItem`: `itemId: doc.id`, `title: doc.title`, `content: doc.content`, `relevanceScore: doc.score ?? 1`, `source: doc.domain ?? doc.documentType`
- Build `ContextPackagerRequest`: `query: ragResult.query`, `contextId: ragResult.query`, `knowledgeItems: mappedItems`
- Return `GovernedContextPackRequest`: `packRequest`, `governanceEnvelope: envelope`

### New file: `dscp.eco.adapter.test.ts`

Required test cases:
1. Non-empty RAGResult: maps all documents to knowledgeItems
2. Empty RAGResult: maps to empty knowledgeItems array
3. RAGDocument fields preserved: id, content, source
4. GovernanceContextEnvelope passed through unchanged
5. RAGResult.query mapped to packRequest.query
6. RAGDocument without domain: source falls back to `documentType`

## Write Ownership

| Path | Ownership |
|---|---|
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | Worker-created |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/tests/dscp.eco.adapter.test.ts` | Worker-created |
| `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_WORKER_RETURN_2026-06-08.md` | Worker-created |
| `docs/baselines/CVF_GC018_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_2026-06-08.md` | Reviewer-updated |
| `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md` | Reviewer-created |
| `docs/roadmaps/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_ROADMAP_2026-06-08.md` | Reviewer-updated |
| `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | Reviewer-updated |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Reviewer-updated |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Reviewer-updated |
| `CVF_SESSION_MEMORY.md` | Reviewer-updated |
| `AGENT_HANDOFF_V17_2026-06-07.md` | Reviewer-updated |
| All other existing files | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` via `git rev-parse --short HEAD`.
2. Confirm pre-flight checks PASS.
3. Read `types.ts`, `context.packager.contract.ts`, and `knowledge.query.contract.ts`.
4. Implement `dscp.eco.adapter.ts` per Implementation Contract.
5. Implement `dscp.eco.adapter.test.ts` with all required test cases.
6. Run `npx tsc -p tsconfig.json --noEmit --rootDir ..` - confirm 0 errors.
7. Run focused vitest - confirm all tests PASS.
8. Stage all new files.
9. Run all 4 governance gates.
10. Author and stage worker return packet.

## Work-Order Fulfillment Manifest

See `## Required Artifact Manifest` above.

Forbidden paths (must NOT appear in `git diff --name-status`):
- Any existing `.ts` file in ECO or CPF directory
- Session, handoff, or registry files

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `npx tsc -p tsconfig.json --noEmit --rootDir ..` | 0 errors |
| vitest result | all PASS |
| `git diff --name-status` | only new worker-owned files |
| 4 governance gates | all COMPLIANT |

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| `buildECOGovernedPackRequest()` exported and compiles | PASS |
| Non-empty RAGResult maps correctly | vitest PASS |
| Empty RAGResult maps to empty array | vitest PASS |
| RAGDocument fields preserved | vitest PASS |
| GovernanceContextEnvelope passed through | vitest PASS |
| No existing file modified | `git diff` clean |
| All 4 governance gates COMPLIANT | PASS |

## Fail Conditions

| Condition | Action |
|---|---|
| `npx tsc -p tsconfig.json --noEmit --rootDir ..` errors | fix before returning |
| Any vitest FAIL | fix before returning |
| Any governance gate VIOLATION | fix before returning |
| Existing ECO `.ts` file modified | STOP - escalate to operator |

## Forbidden Scope

| Forbidden action | Reason |
|---|---|
| Modify `types.ts` | existing source; T7 creates new files only |
| Modify `retriever.ts` or `document.store.ts` | existing source; no modification authorized |
| Live ECO retrieval or provider call | deterministic local only |
| Corpus ingestion | out of scope |
| T12 authorization | separately forbidden |
| Public-sync | out of scope |
| Commit or push | WORKER_MUST_NOT_COMMIT |

## Review Gate

Reviewer must confirm:
1. vitest all PASS (count matches expected).
2. Cross-extension TypeScript check 0 errors.
3. All 4 governance gates COMPLIANT.
4. `git diff --name-status` only new worker-owned files.
5. Worker return packet contains all required evidence.

## Closure Checklist

- [x] Worker return reviewed and accepted
- [x] cross-extension TypeScript check PASS confirmed
- [x] vitest all PASS confirmed (6/6)
- [x] Governance gates COMPLIANT
- [x] Reviewer commits material artifacts
- [x] Session sync updated to `dscp_t7_closed_pass_bounded`
- [x] Completion review packet authored by reviewer

## Return-To-Orchestrator Conditions

Worker returns when:
- All new files staged and uncommitted
- Cross-extension TypeScript check PASS
- All vitest PASS
- All 4 gates COMPLIANT
- Worker return complete and staged

## Acceptance Receipt Assertion Matrix

DSCP-T7 produces no retrieval receipt.

| Required value | Observed value | Status |
|---|---|---|
| Adapter compiles | `npx tsc -p tsconfig.json --noEmit --rootDir ..` PASS | PASS |
| RAGResult maps correctly | 6/6 vitest PASS | PASS |
| No provider call | no live ECO retrieval | N/A with reason: deterministic local only |
| No corpus ingestion | adapter is type mapping only | N/A with reason: no corpus mutation |
| No T12 | T7 does not authorize T12 | N/A with reason: separately forbidden |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md` | reviewer completion authored | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_ROADMAP_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer session sync in closure batch | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer session sync in closure batch | PASS |
| External evidence digest | no external authorized | N/A | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new adapter function only | N/A with reason: helper function only |
| Session continuity | active handoff | reviewer-owned sync in closure batch | PASS |

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized T7 preparation via explicit
chat instruction 2026-06-08; dispatch still requires refreshed DSCP-T6 closure
evidence.

## Reviewer Closure Conversion

```yaml
completionReviewPath: docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md
reviewerOwnedClosurePaths:
  - CVF_SESSION/ACTIVE_SESSION_STATE.json
  - CVF_SESSION_MEMORY.md
  - AGENT_HANDOFF_V17_2026-06-07.md
  - docs/roadmaps/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_ROADMAP_2026-06-08.md
  - docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_FOR_CLAUDE_2026-06-08.md
closedStatusTokens:
  - CLOSED_PASS_BOUNDED
reviewerClosureCompleted: true
forbiddenClosedEquivalentResidue: []
```

## Claim Boundary

This work order claims: implementation contract, source verification, and
gate requirements for DSCP-T7. It does not claim: runtime provider behavior,
live proof, corpus ingestion, public readiness, production readiness, or T12.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
