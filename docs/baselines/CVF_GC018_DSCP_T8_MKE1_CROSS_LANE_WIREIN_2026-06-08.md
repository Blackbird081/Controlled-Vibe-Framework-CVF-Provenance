# CVF GC-018 DSCP-T8 MKE1 Cross-Lane Wire-In Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-08

---

## Authorization

Authorized by operator instruction 2026-06-08: implement DSCP-T8 MKE1
cross-lane wire-in. Operator confirmed all 3 DSCP extension candidates
(T6, T7, T8) have value. T8 follows T7 closure.

## Decision

Decision: implement `buildLPFGovernedPackage()` as a new deterministic
adapter in `CVF_CONTROL_PLANE_FOUNDATION`. This adapter maps LPF
`MemoryContextBlock` into DSCP `GovernedContextPackage`, connecting MKE1-E1
memory enforcement output to DSCP governed packing. The `rawMemoryReleased: false`
governance lock on `MemoryContextBlock` maps directly to `rawContentReleased: false`
on `GovernedContextPackageEvidence`. No modification of existing LPF or MKE1 files.

## Purpose

Prove the DSCP governance lock propagation claim by bridging the LPF memory
domain into the DSCP packing layer. The adapter preserves LPF's existing
governance invariant (`rawMemoryReleased: false`) in the DSCP output
(`rawContentReleased: false`), making memory-governed packs auditable
through the DSCP receipt layer.

## Predecessor Evidence

- DSCP-T2: `GovernedContextPackage`, `GovernedContextPackageEvidence` interfaces.
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
- LPF `MemoryContextBlock` interface with `rawMemoryReleased: false` lock:
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` lines 27-35
- MKE1-E1: memory enforcement gate wire-in. `CLOSED_PASS_BOUNDED` at MKE1-E1 closure commit.
- DSCP-T6: `buildGovernedArtifactDescriptor()`. Pending reviewer.
- DSCP-T7: `buildECOGovernedPackRequest()`. Pending T7 implementation.

## Scope / Target / Owner Boundary

**In scope:**
- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts`
- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.lpf.adapter.test.ts`
- Function: `buildLPFGovernedPackage(block: MemoryContextBlock, artifactId: string, envelope: GovernanceContextEnvelope): GovernedContextPackage`
- Lock mapping: `block.rawMemoryReleased (false)` → `evidence.rawContentReleased (false)`

**Out of scope:**
- No modification of `memory-context-packager.ts` or any existing LPF/MKE1 file.
- No live memory retrieval, advisory readout, provider call, or corpus ingestion.
- No T12 authorization, public-sync, or production readiness.

## Evidence / Verification

Predecessor source surfaces verified at `10b02a79`:

| Surface | File | Lines | Status |
|---|---|---|---|
| `MemoryContextBlock` interface | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | 27-35 | VERIFIED |
| `rawMemoryReleased: false` lock | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | 35 | VERIFIED |
| `GovernedContextPackage` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | 111-117 | VERIFIED |
| `GovernedContextPackageEvidence.rawContentReleased: false` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | 102 | VERIFIED |
| `GovernanceContextEnvelope` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | 58-73 | VERIFIED |

Acceptance verification: `tsc --noEmit` PASS + focused vitest all PASS + all 4
governance gates COMPLIANT on committed range.

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| `buildLPFGovernedPackage()` compiles | `tsc --noEmit` PASS |
| `rawContentReleased: false` in output | vitest PASS |
| `canBypassGovernance: false` in output | vitest PASS |
| `MemoryContextBlock.text` mapped to inner package | vitest PASS |
| `GovernanceContextEnvelope` passed through | vitest PASS |
| No existing LPF/MKE1 file modified | `git diff --name-status` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T8_MKE1_CROSS_LANE_WIREIN_FOR_CLAUDE_2026-06-08.md` | `Status: DISPATCHED` | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md` | reviewer-owned pending | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_ROADMAP_2026-06-08.md` | `Status: DISPATCHED` | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| External evidence digest | no external artifact | no external authorized | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new adapter function only | N/A with reason: helper function only |
| Session continuity | active handoff | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |

## Claim Boundary

This baseline authorizes `buildLPFGovernedPackage()` as a deterministic
local LPF-to-DSCP adapter. It does not claim: runtime provider behavior,
live memory query proof, corpus ingestion, answer quality, public readiness,
production readiness, T12 authorization, or public-sync.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.
