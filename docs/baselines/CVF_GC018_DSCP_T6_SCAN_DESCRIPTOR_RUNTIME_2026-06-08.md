# CVF GC-018 DSCP-T6 Scan Descriptor Runtime Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-08

---

## Authorization

Authorized by operator instruction 2026-06-08: implement DSCP-T6 scan
descriptor runtime. Operator confirmed all 3 DSCP extension candidates
(T6, T7, T8) have value; T6 is executed first. Parent roadmap updated
to add T6/T7/T8 tranche entries.

## Decision

Decision: implement `buildGovernedArtifactDescriptor()` as a new deterministic
local function in `CVF_CONTROL_PLANE_FOUNDATION`. This completes the scan-side
of the DSCP pipeline (scan layer) so the full scan → pack → receipt cycle is
exercisable end-to-end. No live provider call, corpus ingestion, or public-sync
is authorized by this baseline.

## Purpose

Authorize the deterministic local `buildGovernedArtifactDescriptor()` function
inside `CVF_CONTROL_PLANE_FOUNDATION`. This completes the scan-side of the
DSCP pipeline so the full cycle can be expressed:

```
buildGovernedArtifactDescriptor()  [T6 — this tranche]
        ↓
GovernedContextPackerContract.pack()  [T3]
        ↓
buildGovernedRetrievalReceipt()   [T4]
```

## Predecessor Evidence

- DSCP-T2: `dscp.governed.context.contract.ts` — defines `GovernedArtifactDescriptor`,
  `GovernanceGateSet` interfaces. `CLOSED_PASS_BOUNDED` at `932a40aa`.
- DSCP-T3: `dscp.governed.context.packer.ts` — governed pack runtime.
  `CLOSED_PASS_BOUNDED` at `a368dae9`.
- DSCP-T4: `dscp.governed.retrieval.receipt.ts` — receipt builder.
  `CLOSED_PASS_BOUNDED` at `a98396dd`.
- DSCP-T5: parent roadmap consolidation. `CLOSED_PASS_BOUNDED` at `1f140042`.

## Scope

**In scope:**
- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts`
- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.artifact.descriptor.test.ts`
- Input type: `GovernedArtifactDescriptorInput` (defined in the new source file)
- Result type: `GovernedArtifactDescriptorResult` (defined in the new source file)
- Function: `buildGovernedArtifactDescriptor(input): GovernedArtifactDescriptorResult`
- Gate enforcement: `classificationGate=BLOCKED` or `freshnessGate=BLOCKED` returns
  `{ descriptor: null, blocked: true, blockReason: string }`
- PASS/CONDITIONAL/NOT_APPLICABLE/UNKNOWN gates: build and return the descriptor

**Out of scope:**
- No modification of `dscp.governed.context.contract.ts` or any existing file.
- No provider calls, live retrieval, LLM queries, or corpus ingestion.
- No LPCI2 T12 authorization.
- No public-sync, production readiness, or public readiness.
- No modification of T3 packer or T4 receipt builder.

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| `buildGovernedArtifactDescriptor()` compiles | `tsc --noEmit` PASS |
| PASS-gate path returns populated descriptor | vitest PASS |
| BLOCKED classificationGate returns blocked result | vitest PASS |
| BLOCKED freshnessGate returns blocked result | vitest PASS |
| CONDITIONAL gates pass through | vitest PASS |
| `metadata` defaults to `{}` when omitted | vitest PASS |
| All 4 `artifactRole` values accepted | vitest PASS |
| Governance gate: `rawContentReleased: false` not required on descriptor | N/A — descriptor is metadata, not content package |
| No existing file modified | `git diff --name-status` |

## Evidence / Verification

Predecessor source surfaces verified at `10b02a79`:

| Surface | File | Lines | Status |
|---|---|---|---|
| `GovernedArtifactDescriptor` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | 31-51 | VERIFIED |
| `GovernanceGateSet` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | 13-26 | VERIFIED |
| T3 governed packer (gate enforcement pattern) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | 1-96 | VERIFIED |
| T4 receipt builder (output type pattern) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | 1-52 | VERIFIED |

Acceptance verification: `tsc --noEmit` PASS + focused vitest all PASS + all 4
governance gates COMPLIANT on committed range.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_FOR_CLAUDE_2026-06-08.md` | `Status: DISPATCHED`; reviewer updates | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md` | reviewer-owned pending | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_ROADMAP_2026-06-08.md` | `Status: DISPATCHED` | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer-owned session sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer-owned session sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| External evidence digest | external artifact | no external artifact authorized | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | no runtime loop mutation in scope | N/A with reason: new local helper function only |
| Session continuity | active session front door and handoff | reviewer-owned sync | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |

## Claim Boundary

This baseline authorizes `buildGovernedArtifactDescriptor()` as a deterministic
local CPF helper function. It does not claim: runtime provider behavior, live
governance proof, corpus ingestion, answer quality, public readiness, production
readiness, T12 authorization, or public-sync.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced and no public-facing
artifact or public catalog claim is made in this batch.
