# CVF DSCP Domain-Agnostic Scan and Context Pack Readiness Roadmap

Memory class: FULL_RECORD

Status: OPEN

docType: roadmap

Date: 2026-06-07

---

## Authorization

Authorized by operator instruction 2026-06-07: open DSCP roadmap; generalize
PolicyLocal lessons into domain-agnostic standard; no T12; doc-only for T1.
GC-018: `docs/baselines/CVF_GC018_DSCP_T1_OWNER_SURFACE_MAP_AND_SCHEMA_PROPOSAL_2026-06-07.md`.
Predecessor closure: LPCI2-T11D `CLOSED_PASS_BOUNDED` at `bd36e808`;
next allowed move = choose new roadmap lane
(`CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` field).

## Purpose

Define and execute a domain-agnostic scan -> classification -> context pack
readiness standard, generalizing lessons from the LPCI2 PolicyLocal corpus
expansion sequence into a reusable CVF pattern not bound to any specific
document domain (legal, policy, operational, or other).

The LPCI2 T9-T11 sequence proved that a governed scan/classify/retrieve
pipeline can produce deterministic context packs with governance evidence
for LLM consumption. This roadmap extracts the pattern so any future corpus
expansion lane can follow it without reimplementing LPCI-specific schemas.

---

## Scope / Target / Owner Boundary

**In scope:**
- Mapping all existing scan, classification, context-pack, and retrieval
  receipt surfaces currently in CVF.
- Identifying which fields in those surfaces are domain-specific
  (e.g., `jurisdiction`, `ec02Gate`, `authorityLevel`) vs domain-agnostic
  (e.g., `sourceHash`, `artifactRole`, `governanceGate`).
- Proposing a domain-agnostic schema standard (`GovernedArtifactDescriptor`,
  `GovernanceGateSet`, `GovernedContextPackRequest`,
  `GovernedContextPackage`, `GovernedRetrievalReceipt`).
- TypeScript interface definitions (doc-only contract proposals).
- Authoring a standard context packet format that any domain lane can use.

**Out of scope:**
- Runtime TypeScript implementation of proposed interfaces.
- Body extraction, OCR, ingestion, chunking, or any corpus mutation.
- New provider calls, live proof, or LLM quality claims.
- LPCI2 T12 or any domain-specific ingestion work.
- Public-sync, production readiness, or deployment claims.

---

## Predecessor Evidence

- LPCI2-T9 Search Runtime: `CLOSED_PASS_BOUNDED` at `094d82d0`/`fcc9f50f`
- LPCI2-T10 Foundation Readiness: `CLOSED_PASS_BOUNDED` at `866f92cd`
- LPCI2-T11D Readiness Gate: `CLOSED_PASS_BOUNDED` at `bd36e808`
  - Verdict: `READY_WITH_CONDITIONS`; 0 `t12Eligible=YES`
- MLW1-MLW6 Memory/Learning Core Workflow Chain: `CLOSED_PASS_BOUNDED`
- MKE1-E1 Memory Enforcement Gate Wire-In: implemented pending review

Key source surfaces confirmed live in repo:
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`
- `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`

---

## Tranche Plan

### DSCP-T1: Owner Surface Map and Schema Proposal (CLOSED_PASS_BOUNDED)

**Goal:** Produce a source-verified map of all existing scan/classify/context-pack
surfaces and propose a domain-agnostic standard schema before any runtime
implementation.

**Deliverables:**
- Owner Surface Map: `docs/reference/CVF_DSCP_T1_OWNER_SURFACE_MAP_2026-06-07.md`
- Schema Proposal: `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md`
- Worker return: `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_WORKER_RETURN_2026-06-07.md`
- GC-018: `docs/baselines/CVF_GC018_DSCP_T1_OWNER_SURFACE_MAP_AND_SCHEMA_PROPOSAL_2026-06-07.md`
- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T1_OWNER_SURFACE_MAP_FOR_CLAUDE_2026-06-07.md`

**Acceptance criteria:**
- All source paths in the surface map cite an existing file with line range.
- Domain-specific fields are explicitly labelled per surface.
- Schema proposal defines at minimum: scan descriptor, governance gate set,
  governed context pack request, governed context package, governed retrieval
  receipt.
- All proposed interfaces are doc-only TypeScript (not implemented).
- Governance gates PASS on committed range.
- No runtime implementation, ingestion, provider call, or commit by worker.

**Commit mode:** `WORKER_MUST_NOT_COMMIT`

---

### DSCP-T2: Standard Contract Authoring (CLOSED_PASS_BOUNDED)

**Goal:** Author TypeScript interface files for the proposed domain-agnostic
schema. Wire them into the appropriate EXTENSIONS module (likely
`CVF_CONTROL_PLANE_FOUNDATION`). Add contract-level tests.

**Deliverables:**
- Contract: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
- Tests: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts`
- GC-018: `docs/baselines/CVF_GC018_DSCP_T2_STANDARD_CONTRACT_AUTHORING_2026-06-07.md`
- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T2_STANDARD_CONTRACT_AUTHORING_FOR_CLAUDE_2026-06-07.md`
- Worker return: `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_WORKER_RETURN_2026-06-07.md`
- Completion review: `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_COMPLETION_2026-06-07.md`

**Closure result:** 8 type exports authored as type-only contracts with
literal governance locks and focused vitest coverage. No runtime pilot,
provider call, corpus ingestion, public-sync, production readiness, or
public readiness claim is made.

---

### DSCP-T3: Runtime Pilot (FUTURE - NOT YET AUTHORIZED)

**Goal:** Wire the domain-agnostic governed context pack into at least one
live domain pilot (e.g., a non-legal corpus lane). Produce deterministic
test proof.

**Prerequisites:**
- DSCP-T2 closes with contracts accepted.
- Operator explicitly authorizes DSCP-T3 runtime pilot with named domain.

**Not authorized until:** DSCP-T2 `CLOSED_PASS_BOUNDED` and explicit operator
authorization.

---

## Non-Goals

- Runtime TypeScript implementation of any proposed interface.
- Body extraction, OCR, ingestion, chunking, or any corpus mutation.
- New provider calls, live proof, or LLM quality claims.
- LPCI2 T12 or any domain-specific corpus ingestion work.
- Public-sync, production readiness, or hosted/deployment claims.
- Replacing or modifying any existing CVF EXTENSIONS TypeScript source.

## Work Plan

| Tranche | Goal | Status |
|---|---|-|
| DSCP-T1 | Owner surface map and domain-agnostic schema proposal (doc-only) | CLOSED_PASS_BOUNDED |
| DSCP-T2 | Standard contract authoring (TypeScript interfaces) | CLOSED_PASS_BOUNDED |
| DSCP-T3 | Runtime pilot (non-legal domain) | NOT_YET_AUTHORIZED |

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| T1: all source paths cite existing file + line range | Source verification table in work order Section 6A |
| T1: domain-specific fields labelled per surface | Owner surface map, column `Domain-specific?` |
| T1: schema proposal defines 5 proposed interfaces | Schema proposal Sections 2-4 |
| T1: no new `.ts` file created | `git status --short` at return |
| T1: all component gates PASS | Worker Pending-Return Gate table |
| T2 (future): proposed interfaces compile | TypeScript check in DSCP-T2 scope |
| T3 (future): pilot produces deterministic test proof | Live test in DSCP-T3 scope |

## Verification

| Verification step | Command / Evidence |
|---|---|
| T1 source verification | Section 6A table in DSCP-T1 work order |
| T1 governance gates | Worker Pending-Return Gate table in worker return |
| T1 no `.ts` new files | `git status --short` |
| T2 TypeScript validity | `tsc --noEmit` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` |
| T3 deterministic proof | Deterministic test in DSCP-T3 worker return |

## T12 Gate Hard Invariant (Carried Forward from T11D)

The LPCI2 PolicyLocal T12 corpus ingestion work order remains **NOT YET
AUTHORIZED**. This roadmap does not authorize T12. T12 requires separate
operator authorization resolving EC-02 freshness (on or after 2026-07-01),
`currentStatus`, and `jurisdiction` for at least one `t12Eligible=YES`
candidate.

---

## Machine Closure Package

This roadmap is open. The Machine Closure Package below tracks T1 closure state.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T1_OWNER_SURFACE_MAP_FOR_CLAUDE_2026-06-07.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_WORKER_RETURN_2026-06-07.md` | worker return reviewed and committed by Codex | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Roadmap state | this file `DSCP-T1` row | updated to `CLOSED_PASS_BOUNDED` after reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session sync updated by reviewer on DSCP-T1 reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V16_2026-06-06.md` | session markdown updated by reviewer on DSCP-T1 reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| External evidence digest | source surface citations in DSCP-T1 owner surface map | all source surfaces verified at `8e61f65d`; no external artifact produced | N/A with reason: doc-only tranche |
| System loop interlock | no system-loop mutation authorized | DSCP T1 is doc-only; no runtime loop changed | N/A with reason: doc-only |
| Session continuity | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V16_2026-06-06.md` | session sync updated by reviewer on DSCP-T1 reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |

## Current Runtime Freshness Verification

Verified at `executionBaseHead: 8e61f65d` (2026-06-07). The interfaces
proposed in DSCP-T1 (`GovernedArtifactDescriptor`, `GovernanceGateSet`,
`GovernedContextPackRequest`, `GovernedContextPackage`,
`GovernedRetrievalReceipt`) are **doc-only proposals** - they do not exist
as TypeScript implementations in the EXTENSIONS source tree as of this
commit. This is intentional for DSCP-T1; implementation is gated on
DSCP-T2 authorization. The absence is a deliberate tranche boundary, not
a gap requiring remediation.

Source surfaces that DO exist (verified in owner surface map at `8e61f65d`):
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`
- `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/rag.context.engine.convergence.contract.ts`

## Acceptance Receipt Assertion Matrix

This roadmap references `GovernedRetrievalReceipt` as a doc-only proposed
interface name. No runtime retrieval query or provider call was made.

| Required value | Observed value | Status |
|---|---|---|
| No runtime query performed | Worker confirms: no provider call, no live retrieval, no LLM query; `GovernedRetrievalReceipt` is a doc-only proposal name | N/A with reason: doc-only roadmap; no runtime query executed |
| No query receipt generated | `GovernedRetrievalReceipt` appears only as a proposed interface name; no instance created | N/A with reason: doc-only proposal |

## Claim Boundary

This roadmap claims: tranche plan, scope, predecessor evidence citation, and
acceptance criteria for DSCP-T1. It does not claim: runtime implementation,
corpus ingestion, provider calls, public readiness, production readiness, or
any domain-specific eligibility promotion.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced and no public-facing
artifact or public catalog claim is made in this batch.
