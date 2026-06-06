# CVF GC-018 - MKG7-T1 Memory Plane Operational Contract

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize the first MKG7 tranche: a documentation-only Memory Plane Operational
Contract that formalizes, from current source, the bounded runtime contract the
Memory plane already implements and the advisory boundary every later MKG7
tranche must cite.

T1 does not change runtime behavior. It produces one reference document that
names inputs, authorization signals, route surfaces, the returned readout shape,
forbidden fields, lifecycle states, the advisory-only execution boundary, and
the layer scope of the `canReinject=false` invariant, each backed by a
source-verified citation.

## Scope / Target / Owner Boundary

Target owner surface:

- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` (NEW)

Source-of-truth files the contract must cite (read-only for T1):

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route-constants.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts`

Boundary:

- documentation-only; no runtime/source code edits;
- the contract must cite source files with line/symbol evidence, not memory
  summaries;
- no provider/live proof;
- no public-sync.

## Decision

Decision: authorize MKG7-T1 as a documentation-only operational-contract
tranche, dispatched as the first MKG7 work order. All later MKG7 tranches
(T2-T7) depend on and must cite this contract. T1 carries no runtime risk and
fixes the source-verified vocabulary the rest of MKG7 reuses.

The worker may create one reference document and the pending completion review.
The worker must leave both pending and uncommitted for orchestrator review.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Memory readout route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | ACCEPT_AS_CONTRACT_SOURCE |
| Memory readout projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | ACCEPT_AS_CONTRACT_SOURCE |
| Memory runtime workflow chain | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | ACCEPT_AS_CONTRACT_SOURCE |
| Tier lifecycle policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | ACCEPT_AS_CONTRACT_SOURCE |
| Retrieval policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | ACCEPT_AS_CONTRACT_SOURCE |
| Durable store | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | ACCEPT_AS_CONTRACT_SOURCE |

## Source / Predecessor Evidence

Predecessors:

- MKG1-MKG6 are committed (`2ebc0b92`, `6f825820`); the MKG tranche completion
  review records closure.
- MKG5 added the deterministic LPF Memory runtime workflow chain.
- MKG6 added the authenticated `POST /api/memory/readout` route and the
  sanitized projection.

Current source evidence (verified 2026-06-01):

- the readout route returns `rawMemoryReleased:false` and `canReinject:false`
  and guards against `RAW_MEMORY_CONTENT_MUST_NOT_LEAK`;
- the tier lifecycle policy returns `canReinject:true` for semantic/procedural
  tiers, so the `canReinject=false` invariant is surface-scoped, not global;
- the durable store `write()` already fails closed unless
  `actorAuthorized===true` and `policyDecision==="allow"`;
- the LPF subpath export does not yet re-export the lifecycle policy or durable
  store.

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

This tranche does not absorb a new Legacy folder or external corpus. It reads
the bounded MKG5/MKG6 Memory runtime owner set listed above. Filesystem corpus
listing is `N/A with reason`: T1 documents existing owner surfaces and claims no
corpus completeness or new absorption.

### Gate 2 - Prior Absorption Resolution

Resolved predecessors: MKG1 owner reconciliation, MKG2 deferred triage, MKG3
negative owner evidence, MKG4 gate-evidence probe, MKG5 runtime chain, MKG6
readout route.

### Gate 3 - File-Level Value Extraction

Accepted value: the readout request/response shape, authorization signals,
projection sanitization, tier-state lifecycle, retrieval result fields, and
durable fail-closed branches are already source-defined and can be formalized
into one contract without inventing new fields.

### Gate 4 - Owner-Surface Normalization

The contract normalizes existing owners: cvf-web owns route auth/validation and
HTTP projection; LPF owns the workflow chain, lifecycle, retrieval, and durable
store. No owner is moved or duplicated.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Formalize existing readout contract | ACCEPT_NOW | documentation-only, source-backed |
| Document advisory-only execution boundary | ACCEPT_NOW | needed by T3 |
| Define new readout-eligibility states | DEFER_TO_T2 | T2 owns new lifecycle logic |
| Wire advisory into `/api/execute` | DEFER_TO_T3 | requires route change tranche |
| New runtime fields | REJECT_DIRECT | T1 is documentation-only |

### Gate 6 - Adversarial Role Review

Reviewer challenge:

- a contract that cites memory summaries instead of source would repeat the
  Codex draft error;
- a blanket `canReinject=false` claim would mis-state the tier policy;
- describing the durable write as disabled or as an open exposure would both be
  wrong.

Required response: every contract claim cites a source file with line/symbol
evidence; the `canReinject=false` claim is explicitly scoped to the
readout/advisory surface; the durable write is described as present and
fail-closed.

### Gate 7 - Thin Proof And Closure Delta

Required closure delta:

- one reference contract document with a Source Verification table;
- a pending completion review;
- markdown structural completeness and public-export gates pass.

Gate 7 completeness cross-check is `N/A with reason`: no folder absorption or
subfolder completeness claim is made.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- new contract document citing source files with line/symbol evidence;
- Source Verification table inside the contract;
- markdown structural completeness gate pass;
- public-export disposition gate pass;
- pending uncommitted completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only contract packet. No public-sync remote,
public repository commit, or public artifact path is included.

## Claim Boundary

MKG7-T1 authorizes a documentation-only Memory Plane Operational Contract that
formalizes existing source behavior. It does not authorize runtime/source code
changes, new fields, provider execution, live proof, prompt injection,
reinjection, raw Memory release, persistence mutation, graph mutation, new
memory tiers, hosted readiness, production readiness, public readiness,
public-sync, push, or autonomous mutation.
