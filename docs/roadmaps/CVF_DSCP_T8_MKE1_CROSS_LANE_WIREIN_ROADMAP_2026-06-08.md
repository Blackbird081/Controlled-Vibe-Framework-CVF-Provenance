# CVF DSCP-T8 MKE1 Cross-Lane Wire-In Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-08

---

## Authorization

Authorized by operator instruction 2026-06-08: prepare `buildLPFGovernedPackage()`
LPF-to-DSCP adapter inside `CVF_CONTROL_PLANE_FOUNDATION`.
GC-018: `docs/baselines/CVF_GC018_DSCP_T8_MKE1_CROSS_LANE_WIREIN_2026-06-08.md`.
Predecessor release evidence: DSCP-T7 is `CLOSED_PASS_BOUNDED` at closure
commit `958f8d2b`; session sync commit `28329a61`. T8 execution is released
and closed in this batch.

## Purpose

Connect MKE1-E1 memory enforcement output to DSCP governed packing by bridging
LPF `MemoryContextBlock` into DSCP `GovernedContextPackage`. The adapter
preserves the `rawMemoryReleased: false` governance lock from LPF by mapping
it directly to `rawContentReleased: false` in `GovernedContextPackageEvidence`.
This creates an auditable cross-lane path: MKE1 enforcement -> LPF memory block
-> DSCP governed package -> DSCP retrieval receipt.

## Scope / Target / Owner Boundary

**In scope:**
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.lpf.adapter.test.ts`
- Function: `buildLPFGovernedPackage(block, artifactId, envelope): GovernedContextPackage`
- Lock mapping: `block.rawMemoryReleased (false)` -> `evidence.rawContentReleased (false)`

**Out of scope:**
- No modification of `memory-context-packager.ts`, `enforcement.ts`, `route.ts`, or any existing LPF/MKE1 file.
- No live memory retrieval, advisory readout, provider call, or corpus ingestion.
- No T12 authorization, public-sync, or production readiness.

## Non-Goals

- No live memory retrieval or advisory readout call.
- No modification of existing LPF or MKE1 source files.
- No corpus ingestion, OCR, or chunking.
- No provider call or LLM query.
- No T12 authorization.
- No public-sync or production readiness.

## Predecessor Evidence

- DSCP-T2 `GovernedContextPackage`, `GovernedContextPackageEvidence`:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` lines 86-117
- LPF `MemoryContextBlock.rawMemoryReleased: false`:
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` lines 27-35
- MKE1-E1: memory enforcement gate wire-in (pending MKE1-E1 reviewer commit)
- DSCP-T6 `buildGovernedArtifactDescriptor()`: pending T6 reviewer commit
- DSCP-T7 `buildECOGovernedPackRequest()`: pending T7 implementation

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | CLOSED_PASS_BOUNDED |
| 2 | Work order | CLOSED_PASS_BOUNDED |
| 3 | Implement `dscp.lpf.adapter.ts` | CLOSED_PASS_BOUNDED |
| 4 | Implement `dscp.lpf.adapter.test.ts` | CLOSED_PASS_BOUNDED |
| 5 | tsc --noEmit + vitest + governance gates | CLOSED_PASS_BOUNDED |
| 6 | Worker return | CLOSED_PASS_BOUNDED |

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| Source file compiles | `tsc --noEmit` PASS |
| `rawContentReleased: false` in output | vitest PASS |
| `canBypassGovernance: false` in output | vitest PASS |
| `block.text` mapped to inner package content | vitest PASS |
| `GovernanceContextEnvelope` passed through | vitest PASS |
| No existing file modified | `git diff --name-status` |
| All 4 governance gates | gate runner |

## Verification

| Check | Command | Required result |
|---|---|---|
| TypeScript compilation | `npx tsc --noEmit` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` | 0 errors |
| Focused vitest | `npx vitest run tests/dscp.lpf.adapter.test.ts` | all PASS |
| Structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |
| Finding-to-governance | `python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |
| Machine closure package | `python governance/compat/check_machine_closure_package.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce` | COMPLIANT |

## Acceptance Receipt Assertion Matrix

DSCP-T8 produces no retrieval receipt. It builds an LPF-to-DSCP adapter only.

| Required value | Observed value | Status |
|---|---|---|
| Adapter compiles | `npm run check` PASS | PASS |
| `rawContentReleased: false` propagated | 9/9 vitest PASS | PASS |
| No provider call | no live memory retrieval | N/A with reason: deterministic local only |
| No corpus ingestion | adapter is type mapping only | N/A with reason: no corpus mutation |
| No T12 authorization | T8 does not authorize T12 | N/A with reason: T12 requires separate authorization |

## T12 Gate Hard Invariant (Carried Forward)

T12 remains NOT YET AUTHORIZED. This tranche does not authorize T12.

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T8_MKE1_CROSS_LANE_WIREIN_FOR_CLAUDE_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md` | reviewer completion authored | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer session sync in closure batch | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer session sync in closure batch | PASS |
| External evidence digest | no external authorized | N/A | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new adapter function only | N/A with reason: helper function only |
| Session continuity | active handoff | reviewer-owned sync in closure batch | PASS |

## Claim Boundary

This roadmap claims: tranche plan, scope, predecessor evidence, and acceptance
criteria for DSCP-T8. It does not claim: runtime provider behavior, live proof,
corpus ingestion, public readiness, production readiness, T12 authorization,
or T7 closure.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced.
