# CVF GC-018 Baseline: DSCP-T2 Standard Contract Authoring

Memory class: FULL_RECORD

Status: ACTIVE_BASELINE

docType: gc018_baseline

Date: 2026-06-07

GC-018 control: `docs/reference/CVF_GC018_GOVERNANCE_CONTROL_STANDARD.md`

dispatchBaseHead: `6535568d`

---

## Proposed Tranche

DSCP-T2: Standard Contract Authoring.

Predecessor: DSCP-T1 Owner Surface Map and Schema Proposal
(`CLOSED_PASS_BOUNDED` at `62fa6943`). DSCP-T2 converts the doc-only
interface proposals into compilable TypeScript type contracts with unit
test coverage. No runtime pilot, corpus ingestion, provider call,
public-sync, or readiness claim is included in this tranche.

## Purpose

GC-018 authorization for DSCP-T2: author TypeScript contract interfaces
and unit tests for the domain-agnostic scan -> classify -> pack -> retrieve
standard schema accepted in DSCP-T1. This tranche converts the doc-only
interface proposals into compilable TypeScript type contracts with shape
validation test coverage.

---

## Authorization

DSCP-T2 is authorized to:

- Create one new TypeScript source file in
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/`:
  `dscp.governed.context.contract.ts`
- Create one new TypeScript test file in
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/`:
  `dscp.governed.context.contract.test.ts`
- Export the 8 types/interfaces defined in the DSCP-T1 schema proposal:
  `GovernanceGateSet`, `GovernedArtifactDescriptor`,
  `GovernanceContextEnvelope`, `GovernedContextPackRequest`,
  `GovernedContextPackageEvidence`, `GovernedContextPackage`,
  `ContentDeliveryClass`, `GovernedRetrievalReceipt`
- Import existing CPF types (`ContextPackagerRequest`,
  `TypedContextPackage`) via relative import from
  `./context.packager.contract`
- Write shape validation and boundary tests using vitest

DSCP-T2 is NOT authorized to:

- Implement runtime logic or class bodies beyond type-narrowing helpers
- Modify any existing `.ts` file
- Ingest, scan, or classify corpus content
- Make provider or API calls
- Perform public-sync or push to the public repository
- Author T3 runtime pilot code or a runtime implementation of the pipeline
- Claim production readiness, public readiness, or hosted readiness
- Promote or mutate LPCI2 eligibility status

---

## Non-Goals

- Runtime scan/classify/pack/retrieve pipeline implementation (DSCP-T3)
- Provider calls or live governance proof
- Corpus ingestion or document body extraction
- LPCI2 T12 promotion or eligibility mutation
- Public-sync or public catalog update
- Modification of any existing TypeScript or Python file

---

## Predecessor Evidence

DSCP-T1 Owner Surface Map and Schema Proposal:
`CLOSED_PASS_BOUNDED` at `62fa6943`

- Schema proposal: `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md`
- Owner surface map: `docs/reference/CVF_DSCP_T1_OWNER_SURFACE_MAP_2026-06-07.md`
- GC-018 (T1): `docs/baselines/CVF_GC018_DSCP_T1_OWNER_SURFACE_MAP_AND_SCHEMA_PROPOSAL_2026-06-07.md`
- Completion review: `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_COMPLETION_2026-06-07.md`
- Roadmap: `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`

Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`

---

## Scope of Contract File

Target file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`

Exported types:

| Export | Kind | Description |
|---|---|---|
| `GovernanceGateSet` | `interface` | Domain-agnostic gate result set (freshness, classification, eligibility, customGates) |
| `GovernedArtifactDescriptor` | `interface` | Domain-agnostic artifact descriptor for the scan layer |
| `GovernanceContextEnvelope` | `interface` | Governance envelope attached to a context pack request |
| `GovernedContextPackRequest` | `interface` | `ContextPackagerRequest` wrapped with `GovernanceContextEnvelope` |
| `GovernedContextPackageEvidence` | `interface` | Governance evidence block attached to a context package |
| `GovernedContextPackage` | `interface` | `TypedContextPackage` wrapped with `GovernedContextPackageEvidence` |
| `ContentDeliveryClass` | `type` | Domain-agnostic replacement for `AnswerClass` |
| `GovernedRetrievalReceipt` | `interface` | Domain-agnostic retrieval receipt |

---

## Scope of Test File

Target file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts`

Coverage required:

- Shape construction for each of the 8 exported types
- Governance lock literal type enforcement (`rawContentReleased: false`,
  `canBypassGovernance: false`, `rawSourceReleased: false`)
- `GovernanceGateSet.customGates` open-map acceptance
- `ContentDeliveryClass` all 4 values accepted
- `GovernedContextPackRequest` wraps a valid `ContextPackagerRequest`
- `GovernedContextPackage` wraps a valid `TypedContextPackage`
- `GovernedRetrievalReceipt.governanceGateResults` open-map acceptance

---

## Acceptance Criteria

- `dscp.governed.context.contract.ts` TypeScript compilation passes
  (`tsc --noEmit`) with zero errors
- All exported types are used in the test file
- All vitest tests PASS
- No existing file modified
- No runtime logic implemented in contract file
- All governance gates PASS on committed range:
  - markdown structural completeness
  - finding-to-governance learning
  - machine closure package
  - dispatch quality

---

## Evidence

| Source fact | Source file | Lines | Disposition |
|---|---|---|---|
| `ContextPackagerRequest` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | 29-38 | ACCEPT |
| `TypedContextPackage` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | 49-59 | ACCEPT |
| `GovernanceGateSet` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 72-86 | ACCEPT |
| `GovernedArtifactDescriptor` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 100-125 | ACCEPT |
| `GovernanceContextEnvelope` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 144-160 | ACCEPT |
| `GovernedContextPackRequest` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 170-176 | ACCEPT |
| `GovernedContextPackageEvidence` + `GovernedContextPackage` proposals | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 193-218 | ACCEPT |
| `ContentDeliveryClass` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 230-234 | ACCEPT |
| `GovernedRetrievalReceipt` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 244-276 | ACCEPT |
| Schema proposal scope (doc-only; DSCP-T2 for TypeScript) | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | 19-36 | ACCEPT |
| DSCP roadmap T2 authorization scope | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | 102-114 | ACCEPT |
| CPF tests directory (target test path) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/context.packager.test.ts` | 1-5 | ACCEPT |

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T2_STANDARD_CONTRACT_AUTHORING_FOR_CLAUDE_2026-06-07.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_WORKER_RETURN_2026-06-07.md` | worker return reviewed and committed by Codex | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Roadmap state | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | DSCP-T2 row updated to `CLOSED_PASS_BOUNDED` by reviewer | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session sync updated by reviewer/committer on DSCP-T2 reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | session markdown updated by reviewer/committer on DSCP-T2 reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| External evidence digest | TypeScript compilation + vitest PASS evidence | `tsc --noEmit` PASS + all vitest PASS | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| System loop interlock | no system-loop mutation authorized | DSCP-T2 is contract-only; no runtime loop changed | N/A with reason: contracts + tests only |
| Session continuity | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | session sync updated by reviewer/committer on DSCP-T2 reviewer commit | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |

## Claim Boundary

This GC-018 baseline authorizes DSCP-T2 TypeScript contract authoring and
test coverage only. It does not authorize: runtime logic implementation,
corpus ingestion, provider calls, DSCP-T3 runtime pilot, LPCI2 T12
promotion, public-sync, production readiness, or public readiness.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced and no public-facing
artifact or public catalog claim is made in this batch.
