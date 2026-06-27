# CVF DSCP-T6 Scan Descriptor Runtime Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-08

---

## Authorization

Authorized by operator instruction 2026-06-08: implement `buildGovernedArtifactDescriptor()`
scan-side function inside `CVF_CONTROL_PLANE_FOUNDATION`.
GC-018: `docs/baselines/CVF_GC018_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_2026-06-08.md`.
Predecessor closure: DSCP-T5 `CLOSED_PASS_BOUNDED` at `1f140042`.

## Purpose

Complete the DSCP scan-side runtime. After T2 (contracts), T3 (packer), and
T4 (receipt), the `GovernedArtifactDescriptor` interface has no builder function.
T6 supplies `buildGovernedArtifactDescriptor()` with gate enforcement so the
full governed pipeline can be exercised end-to-end:

```
[scan descriptor]  <- T6 (this tranche)
      |
[GovernedContextPackRequest]
      |
GovernedContextPackerContract.pack()  <- T3
      |
[GovernedContextPackage]
      |
buildGovernedRetrievalReceipt()  <- T4
      |
[GovernedRetrievalReceipt]
```

## Scope / Target / Owner Boundary

**In scope:**
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.artifact.descriptor.test.ts`
- Input/result types exported from the new source file
- Gate enforcement: BLOCKED gates refuse descriptor construction

**Out of scope:**
- No modification of existing CPF, ECO, LPF, or LPCI files.
- No provider calls, live retrieval, or corpus ingestion.
- No T12 authorization, public-sync, or production readiness.

## Non-Goals

- No modification of `dscp.governed.context.contract.ts` or any other existing file.
- No modification of `dscp.governed.context.packer.ts` or `dscp.governed.retrieval.receipt.ts`.
- No provider calls, live retrieval queries, LLM queries, or corpus ingestion.
- No LPCI2 T12 authorization.
- No public-sync, production readiness, or public readiness.
- No response hashing, embedding generation, or external I/O of any kind.

## Predecessor Evidence

- DSCP-T2 `GovernedArtifactDescriptor` interface:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` lines 31-51
- DSCP-T3 governed packer: `dscp.governed.context.packer.ts`
- DSCP-T4 receipt builder: `dscp.governed.retrieval.receipt.ts`

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | CLOSED_PASS_BOUNDED |
| 2 | Work order | CLOSED_PASS_BOUNDED |
| 3 | Implement `dscp.governed.artifact.descriptor.ts` | CLOSED_PASS_BOUNDED |
| 4 | Implement `dscp.governed.artifact.descriptor.test.ts` | CLOSED_PASS_BOUNDED |
| 5 | tsc --noEmit + vitest + governance gates | CLOSED_PASS_BOUNDED |
| 6 | Worker return | CLOSED_PASS_BOUNDED |

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| Source file compiles | `tsc --noEmit` PASS |
| PASS path builds descriptor | vitest PASS |
| BLOCKED classificationGate → blocked result | vitest PASS |
| BLOCKED freshnessGate → blocked result | vitest PASS |
| CONDITIONAL gates pass through | vitest PASS |
| metadata defaults to `{}` | vitest PASS |
| No existing file modified | `git diff --name-status` |
| All 4 governance gates PASS | gate runner |

## Verification

Verification commands (to be run by worker before returning):

| Check | Command | Required result |
|---|---|---|
| TypeScript compilation | `npx tsc --noEmit` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` | 0 errors |
| Focused vitest | `npx vitest run tests/dscp.governed.artifact.descriptor.test.ts` | all PASS |
| Structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base 10b02a79 --head HEAD --enforce` | COMPLIANT |
| Finding-to-governance | `python governance/compat/check_finding_to_governance_learning.py --base 10b02a79 --head HEAD --enforce` | COMPLIANT |
| Machine closure package | `python governance/compat/check_machine_closure_package.py --base 10b02a79 --head HEAD --enforce` | COMPLIANT |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 10b02a79 --head HEAD --enforce` | COMPLIANT |
| Changed file scope | `git diff --name-status HEAD` | only new files; no existing file modified |

## Acceptance Receipt Assertion Matrix

DSCP-T6 produces no retrieval receipt. It builds a scan-layer descriptor only.

| Required value | Observed value | Status |
|---|---|---|
| Scan descriptor builder compiles | `tsc --noEmit` PASS; 0 errors | PASS |
| Gate enforcement blocks BLOCKED gates | 12/12 vitest PASS at `executionBaseHead` | PASS |
| No provider call | no live/provider route in T6 | N/A with reason: deterministic local only |
| No corpus ingestion | T6 is scan-metadata only | N/A with reason: no corpus mutation |
| No T12 authorization | T6 does not authorize T12 | N/A with reason: T12 requires separate authorization |

## T12 Gate Hard Invariant (Carried Forward)

T12 remains NOT YET AUTHORIZED. This tranche does not authorize T12.

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_FOR_CLAUDE_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md` | reviewer completion authored | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer session sync in closure batch | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer session sync in closure batch | PASS |
| External evidence digest | external artifact | no external artifact authorized | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new local function only | N/A with reason: helper function only |
| Session continuity | active session front door and handoff | reviewer-owned sync in closure batch | PASS |

## Claim Boundary

This roadmap claims: tranche plan, scope, predecessor evidence, and acceptance
criteria for DSCP-T6. It does not claim: runtime provider behavior, live proof,
corpus ingestion, public readiness, production readiness, or T12 authorization.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced and no public-facing
artifact or public catalog claim is made in this batch.
