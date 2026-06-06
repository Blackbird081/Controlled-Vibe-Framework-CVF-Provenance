# CVF GC-018 - MKE1-E2 Memory Durable Write Route

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize MKE1-E2: add a governed `POST /api/memory/write` route that exposes
the already-fail-closed `DurableMemoryStore.write()` path through an
authenticated HTTP surface. The route must not accept raw memory content, must
enforce actor authorization and policy gates, and must return a `DurableMemoryReceipt`
with `summaryOnly:true`, `canReinject:false`, `rawMemoryReleased:false`.

MKE1-E2 depends on MKE1-E1 (enforcement gate) being complete. MKE1-E3 (live
proof of REVOKED→BLOCK) is a separate tranche.

## Scope / Target / Owner Boundary

Target owner surfaces (NEW):

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route-constants.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.test.ts`
- `docs/reviews/CVF_MKE1_E2_MEMORY_DURABLE_WRITE_ROUTE_COMPLETION_2026-06-01.md`

Source-of-truth files (read-only):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` — existing store interface and fail-closed write path
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` — authentication pattern reference

Boundary: new route only; no edits to `durable-memory-store.ts`; no raw content
intake; no public-sync; no autonomous mutation.

## Decision

Authorize MKE1-E2 as a bounded governed write route. Route is authenticated
(service-token or session), rejects raw content fields, enforces
`actorAuthorized` and `policyDecision === 'allow'` gates before calling the
existing store, and returns a summary-only receipt. Route version:
`cvf.memoryDurableWriteRoute.mke1.e2.v1`.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Durable store write (existing) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts:90` | ACCEPT_AS_CONTRACT_SOURCE — must not be modified |
| Durable store fail-closed branch | `durable-memory-store.ts:201` | ACCEPT_AS_INVARIANT_SOURCE |
| Auth pattern reference | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | ACCEPT_AS_PATTERN |

## Source / Predecessor Evidence

- MKE1-E1 complete: `docs/reviews/CVF_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_COMPLETION_2026-06-01.md`
- Durable store write already fail-closed: `actorAuthorized` false or `policyDecision !== 'allow'` → denied (line 201)
- Receipt invariants locked: `summaryOnly:true`, `canReinject:false`, `rawMemoryReleased:false`

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

Bounded cvf-web owner set. No Legacy folder absorption. `N/A with reason`.

### Gate 2 - Prior Absorption Resolution

MKE1-E1 complete. Durable store contract source-verified in MKG7-T5 and MKE1 roadmap.

### Gate 3 - File-Level Value Extraction

Route adds an authenticated HTTP surface over the existing store write path.
Key controls: raw field rejection (`content`, `rawContent`, `value` fields blocked),
auth gate (service-token or session), policy gate (`actorAuthorized` + `policyDecision`),
store path env var required, receipt returned as `summaryOnly:true`.

### Gate 4 - Owner-Surface Normalization

New route lives in `cvf-web/src/app/api/memory/write/` — sibling to the readout
route. Does not modify the durable store.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Governed write route | ACCEPT_NOW | completes MKE1-E2 scope |
| Modifying `durable-memory-store.ts` | REJECT_DIRECT | store is read-only source |
| Raw content field intake | REJECT_DIRECT | blocked by route validation |

### Gate 6 - Adversarial Role Review

Risk: route could accept raw content through an unvalidated field. Required:
`hasRawPayloadField` guard rejects any body containing `content`, `rawContent`,
or `value` before validation proceeds.

### Gate 7 - Thin Proof And Closure Delta

Route file, constants, tests (auth, raw rejection, policy gate, allowed write,
store-not-configured), TypeScript check, file-size guard.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- route file with auth, raw field rejection, policy gate, store write, receipt return;
- focused tests covering all paths;
- cvf-web `npm run check` PASS;
- file-size guard PASS;
- completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

MKE1-E2 authorizes a governed durable write HTTP route only. Does not authorize
raw content intake, autonomous mutation, provider calls, prompt injection,
public-sync, or push.
