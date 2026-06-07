# CVF GC-018: DSCP-T4 Retrieval Receipt Runtime Boundary

Memory class: FULL_RECORD

Status: ACTIVE_BASELINE

docType: gc018_baseline

Date: 2026-06-07

GC-018 control: `docs/reference/CVF_GC018_GOVERNANCE_CONTROL_STANDARD.md`

dispatchBaseHead: `a368dae9`

---

## Proposed Tranche

DSCP-T4: Retrieval Receipt Runtime Boundary.

Predecessor: DSCP-T3 Runtime Pilot - CPF Internal
(`CLOSED_PASS_BOUNDED` at `a368dae9`). DSCP-T4 adds a deterministic local
helper that creates a `GovernedRetrievalReceipt` from an already governed
context package and caller-supplied retrieval metadata.

## Purpose

Authorize a bounded CPF internal receipt-boundary implementation after DSCP-T3.
The baseline closes the local gap identified in the post-T3 audit: DSCP has a
governed package runtime, but no runtime receipt object builder.

## Authorization

Operator instruction 2026-06-07: after DSCP-T3 review, audit CVF, propose the
optimal next roadmap, and write a work order for Claude.

Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`

## Scope

### In Scope

- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts`
  - `GovernedRetrievalReceiptInput` interface
  - `buildGovernedRetrievalReceipt()` function
  - deterministic mapping from `GovernedContextPackage` evidence to
    `GovernedRetrievalReceipt`
- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.retrieval.receipt.test.ts`
  - focused deterministic vitest coverage for PASS mapping and governance
    locks

### Non-Goals

- No live provider/API call.
- No LLM query, retrieval execution, or answer generation.
- No response hashing implementation; `modelResponseHash` is caller-supplied.
- No corpus ingestion, OCR, extraction, or chunking.
- No public-sync, production readiness, public readiness, or release readiness.
- No existing TypeScript source mutation or barrel export.
- No session continuity mutation by worker.

## Acceptance Criteria

1. `buildGovernedRetrievalReceipt()` compiles and returns a
   `GovernedRetrievalReceipt`.
2. `contextPackageId` equals `contextPackage.innerPackage.packageId`.
3. `sourceArtifactIds` equals
   `contextPackage.governanceEvidence.sourceArtifactIds`.
4. `governanceGateResults.classificationGate` and `freshnessGate` are copied
   from package evidence.
5. Caller-provided `governanceGateResults` cannot override package
   `classificationGate` or `freshnessGate`.
6. `rawSourceReleased` is literal `false`.
7. `tsc --noEmit` PASS in CPF directory.
8. Focused vitest PASS.
9. No existing `.ts` file modified.

## Predecessor Evidence

| Predecessor | Path | Status |
|---|---|---|
| DSCP-T2 contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | CLOSED_PASS_BOUNDED at `932a40aa` |
| DSCP-T3 runtime packer | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | CLOSED_PASS_BOUNDED at `a368dae9` |
| DSCP-T3 completion review | `docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_COMPLETION_2026-06-07.md` | CLOSED_PASS_BOUNDED |
| Post-T3 audit | `docs/audits/CVF_DSCP_POST_T3_NEXT_ROADMAP_AUDIT_2026-06-07.md` | DISPATCHED |
| DSCP-T4 roadmap | `docs/roadmaps/CVF_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_ROADMAP_2026-06-07.md` | DISPATCHED |

## Evidence

- Source verification: work order Section 6A table.
- TypeScript compilation: `npx tsc --noEmit` in CPF directory.
- Deterministic vitest: focused T4 receipt test.
- Governance gates: worker pending-return gate table in worker return.
- No existing file modified: worker return `git status --short`.

## Acceptance Receipt Assertion Matrix

This baseline authorizes deterministic receipt object construction only.

| Required value | Observed value | Status |
|---|---|---|
| Receipt object can be instantiated locally | Worker must implement T4 helper | PENDING_WORKER_RETURN |
| No provider call | Forbidden by scope | N/A with reason: no live/provider route in scope |
| No raw source release | `rawSourceReleased` must be false | PENDING_WORKER_RETURN |
| No model response hash computation | `modelResponseHash` caller-supplied | N/A with reason: no provider response in scope |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_FOR_CLAUDE_2026-06-07.md` | DISPATCHED at baseline publication; reviewer updates when worker result is reviewed | BLOCKED with reason: WORKER_MUST_NOT_COMMIT |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_WORKER_RETURN_2026-06-07.md` | worker-owned pending return packet | BLOCKED with reason: pending worker return |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T4_RETRIEVAL_RECEIPT_RUNTIME_BOUNDARY_ROADMAP_2026-06-07.md` | reviewer updates when worker result is reviewed | BLOCKED with reason: pending worker return |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer-owned session sync after dispatch commit | BLOCKED with reason: reviewer sync pending |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer-owned session sync after dispatch commit | BLOCKED with reason: reviewer sync pending |
| External evidence digest | TypeScript + vitest output | local only; no external artifact | N/A with reason: deterministic local proof |
| System loop interlock | no system-loop mutation authorized | receipt helper only | N/A with reason: no system-loop mutation authorized |
| Session continuity | active session front door and handoff | reviewer-owned sync | BLOCKED with reason: reviewer sync pending |

## Claim Boundary

This GC-018 baseline authorizes only DSCP-T4 deterministic CPF receipt-boundary
implementation. It does not claim provider behavior, answer quality,
retrieval completeness, corpus ingestion, public-sync, production readiness,
hosted readiness, release readiness, or public readiness.

## Finding-To-Governance Learning Disposition

Defect class coverage: RUNTIME_SIGNAL_GAP. Learning lane coverage:
GOVERNANCE_CONTROL_PLANE. Disposition coverage: DEFER_WITH_ROADMAP. Next
action: execute DSCP-T4 work order.

| Finding | Defect class | Lane | Disposition | Next action | N/A reason |
|---|---|---|---|---|---|
| Receipt contract lacks runtime builder | RUNTIME_SIGNAL_GAP | GOVERNANCE_CONTROL_PLANE | DEFER_WITH_ROADMAP | Implement deterministic T4 helper | N/A |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; no public-sync, public catalog update, or
public artifact export authorized.
