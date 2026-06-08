# CVF Agent Work Order: DSCP-T8 MKE1 Cross-Lane Wire-In

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-08

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `10b02a79`

executionBaseHead: `28329a61`

closureBaseHead: `28329a61`

---

## Purpose

Prepare Claude to implement `buildLPFGovernedPackage()` - an LPF-to-DSCP
adapter - inside `CVF_CONTROL_PLANE_FOUNDATION`. Bridges MKE1-E1 memory
enforcement output (via LPF `MemoryContextBlock`) into DSCP
`GovernedContextPackage`, propagating `rawMemoryReleased: false` governance
lock to `rawContentReleased: false` in DSCP evidence.

## Authority Chain

Operator instruction 2026-06-08 -> GC-018:
`docs/baselines/CVF_GC018_DSCP_T8_MKE1_CROSS_LANE_WIREIN_2026-06-08.md`
-> this work order.

Prerequisite release evidence: DSCP-T6 is `CLOSED_PASS_BOUNDED` at `13cc1505`.
DSCP-T7 is `CLOSED_PASS_BOUNDED` at closure commit `958f8d2b`; session sync
commit `28329a61`. T8 execution is released in this batch.

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Implement adapter + tests; author worker return; stage artifacts |
| Reviewer | Codex | Review worker return; run governance gates; commit if PASS |
| Operator | Human | Authorized T8 preparation; owns session sync and registry updates |

## Scope / Target / Owner Boundary

**Allowed scope:**
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts`
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.lpf.adapter.test.ts`
- Create `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_WORKER_RETURN_2026-06-08.md`
- Reviewer correction to `docs/baselines/CVF_GC018_DSCP_T8_MKE1_CROSS_LANE_WIREIN_2026-06-08.md`
- Reviewer closure update to `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md`
- Reviewer closure update to `docs/roadmaps/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_ROADMAP_2026-06-08.md`
- Reviewer closure update to `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`
- Reviewer closure update to `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- Reviewer closure sync to `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Reviewer closure sync to `CVF_SESSION_MEMORY.md`
- Reviewer closure sync to `AGENT_HANDOFF_V17_2026-06-07.md`

**Forbidden scope:** see Forbidden Scope section below.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap section | Work order section | Status |
|---|---|---|
| Goal: implement `buildLPFGovernedPackage()` | Implementation Contract | TRACED |
| Scope: new CPF file, no existing LPF/MKE1 file modified | Scope / Target / Owner Boundary | TRACED |
| Non-goals: no live memory retrieval, no advisory readout | Forbidden Scope | TRACED |
| Acceptance: `rawContentReleased: false` propagated | Acceptance Criteria | TRACED |
| Verification commands | Evidence Requirements | TRACED |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within
allowed scope (tsc errors, vitest failures, markdown violations) must be
repaired and rerun by the worker without escalating to the operator.

## Required Artifact Manifest

| Artifact | Type | Required path | Proof literal |
|---|---|---|---|
| LPF adapter | new TypeScript source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | `tsc --noEmit` 0 errors |
| Test suite | new TypeScript test | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.lpf.adapter.test.ts` | vitest all PASS |
| Worker return | new Markdown review | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_WORKER_RETURN_2026-06-08.md` | all 4 gates COMPLIANT |

## Required First Reads

| File | Purpose |
|---|---|
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | Verify `MemoryContextBlock` exact interface and `rawMemoryReleased: false` lock |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | Verify `GovernedContextPackage`, `GovernedContextPackageEvidence`, `GovernanceContextEnvelope` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | Verify `TypedContextPackage` shape |
| `docs/baselines/CVF_GC018_DSCP_T8_MKE1_CROSS_LANE_WIREIN_2026-06-08.md` | Confirm authorized scope |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Clean working tree | `git status --short` | no unexpected modified files |
| Base HEAD confirmed | `git rev-parse --short HEAD` | capture as `executionBaseHead` |
| T7 dependency released | verify DSCP-T7 closure commit and completion packet | PASS with commit evidence |
| LPF adapter does not yet exist | confirm `dscp.lpf.adapter.ts` absent | NOT FOUND |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
|---|---|---|---|---|---|
| `MemoryContextBlock` interface | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | lines 27-35 | `export interface MemoryContextBlock` | `memory-context-packager.ts` | ACCEPT |
| `rawMemoryReleased: false` lock | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | line 35 | `rawMemoryReleased` | `MemoryContextBlock` | ACCEPT |
| `GovernedContextPackage` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 111-117 | `export interface GovernedContextPackage` | `dscp.governed.context.contract.ts` | ACCEPT |
| `GovernedContextPackageEvidence.rawContentReleased` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | line 102 | `rawContentReleased` | `GovernedContextPackageEvidence` | ACCEPT |
| `GovernedContextPackageEvidence.canBypassGovernance` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | line 103 | `canBypassGovernance` | `GovernedContextPackageEvidence` | ACCEPT |
| `GovernanceContextEnvelope` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 58-73 | `export interface GovernanceContextEnvelope` | `dscp.governed.context.contract.ts` | ACCEPT |

## Implementation Contract

### New file: `dscp.lpf.adapter.ts`

**Imports:**
```typescript
import type { MemoryContextBlock } from "../../CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager";
import type {
  GovernedContextPackage,
  GovernedContextPackageEvidence,
  GovernanceContextEnvelope,
} from "./dscp.governed.context.contract";
import type { TypedContextPackage } from "./context.packager.contract";
```

**Function (export):**
```typescript
export function buildLPFGovernedPackage(
  block: MemoryContextBlock,
  artifactId: string,
  envelope: GovernanceContextEnvelope,
): GovernedContextPackage
```

**Implementation notes:**
- Build a minimal `TypedContextPackage` stub from `block.text` (single segment with `segmentType: "knowledge"`).
- Build `GovernedContextPackageEvidence`:
  - `classificationGate: envelope.classificationGate`
  - `freshnessGate: envelope.freshnessGate`
  - `policyDecision: envelope.policyDecision`
  - `sourceArtifactIds: [artifactId]`
  - `rawContentReleased: false` (literal `false` - governance lock from LPF)
  - `canBypassGovernance: false` (literal `false` - governance lock)
  - `authorizationRef: envelope.authorizationRef`
- Return `GovernedContextPackage`: `{ innerPackage, governanceEvidence }`

**Governance note:** `rawContentReleased: false` and `canBypassGovernance: false` must be
typed as literal `false`, not `boolean`, to satisfy the TypeScript interface contract.
`TypedContextPackage` shape is source-verified from
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`:
`packageId`, `builtAt`, `contextId`, `query`, `segments`, `totalSegments`,
`estimatedTokens`, `perTypeTokens`, and `packageHash`.

### New file: `dscp.lpf.adapter.test.ts`

Required test cases:
1. `rawContentReleased` is `false` in output evidence
2. `canBypassGovernance` is `false` in output evidence
3. `block.text` mapped into inner package content/segments
4. `GovernanceContextEnvelope.classificationGate` preserved in evidence
5. `GovernanceContextEnvelope.freshnessGate` preserved in evidence
6. `GovernanceContextEnvelope.policyDecision` preserved in evidence
7. `artifactId` appears in `sourceArtifactIds`
8. `authorizationRef` passed through when provided
9. `authorizationRef` undefined when envelope has none

## Write Ownership

| Path | Ownership |
|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | Worker-created |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.lpf.adapter.test.ts` | Worker-created |
| `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_WORKER_RETURN_2026-06-08.md` | Worker-created |
| `docs/baselines/CVF_GC018_DSCP_T8_MKE1_CROSS_LANE_WIREIN_2026-06-08.md` | Reviewer-updated |
| `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md` | Reviewer-created |
| `docs/roadmaps/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_ROADMAP_2026-06-08.md` | Reviewer-updated |
| `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | Reviewer-updated |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Reviewer-updated |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Reviewer-updated |
| `CVF_SESSION_MEMORY.md` | Reviewer-updated |
| `AGENT_HANDOFF_V17_2026-06-07.md` | Reviewer-updated |
| All other existing files | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` via `git rev-parse --short HEAD`.
2. Confirm pre-flight checks PASS.
3. Read `memory-context-packager.ts`, `dscp.governed.context.contract.ts`, `context.packager.contract.ts`.
4. Implement `dscp.lpf.adapter.ts` per Implementation Contract.
5. Implement `dscp.lpf.adapter.test.ts` with all required test cases.
6. Run `npx tsc --noEmit` - confirm 0 errors.
7. Run focused vitest - confirm all tests PASS.
8. Stage all new files.
9. Run all 4 governance gates.
10. Author and stage worker return packet.

## Work-Order Fulfillment Manifest

See `## Required Artifact Manifest` above.

Forbidden paths (must NOT appear in `git diff --name-status`):
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- Any existing `.ts` file in LPF, MKE1, or CPF directories
- Session, handoff, or registry files

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `tsc --noEmit` | 0 errors |
| vitest result | all PASS |
| `git diff --name-status` | only new worker-owned files |
| 4 governance gates | all COMPLIANT |

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| `buildLPFGovernedPackage()` exported and compiles | PASS |
| `rawContentReleased: false` in output | vitest PASS |
| `canBypassGovernance: false` in output | vitest PASS |
| `block.text` mapped to inner package | vitest PASS |
| `GovernanceContextEnvelope` passed through | vitest PASS |
| No existing file modified | `git diff` clean |
| All 4 governance gates COMPLIANT | PASS |

## Fail Conditions

| Condition | Action |
|---|---|
| `tsc --noEmit` errors | fix before returning |
| Any vitest FAIL | fix before returning |
| Any governance gate VIOLATION | fix before returning |
| Existing LPF/MKE1 `.ts` file modified | STOP - escalate to operator |

## Forbidden Scope

| Forbidden action | Reason |
|---|---|
| Modify `memory-context-packager.ts` | existing source; T8 creates new files only |
| Modify `enforcement.ts` or `route.ts` (MKE1) | existing source; no modification authorized |
| Live memory retrieval or advisory readout | deterministic local only |
| Corpus ingestion | out of scope |
| T12 authorization | separately forbidden |
| Public-sync | out of scope |
| Commit or push | WORKER_MUST_NOT_COMMIT |

## Review Gate

Reviewer must confirm:
1. vitest all PASS (count matches expected).
2. `tsc --noEmit` 0 errors.
3. All 4 governance gates COMPLIANT.
4. `git diff --name-status` only new worker-owned files.
5. Worker return contains all required evidence.

## Closure Checklist

- [x] Worker return reviewed and accepted
- [x] `tsc --noEmit` PASS confirmed
- [x] vitest all PASS confirmed (9/9)
- [x] Governance gates COMPLIANT
- [x] Reviewer commits material artifacts
- [x] Session sync updated to `dscp_t8_closed_pass_bounded`
- [x] Completion review packet authored by reviewer

## Return-To-Orchestrator Conditions

Worker returns when:
- All new files staged and uncommitted
- `tsc --noEmit` PASS
- All vitest PASS
- All 4 gates COMPLIANT
- Worker return complete and staged

## Acceptance Receipt Assertion Matrix

DSCP-T8 produces no retrieval receipt.

| Required value | Observed value | Status |
|---|---|---|
| Adapter compiles | `npm run check` PASS | PASS |
| `rawContentReleased: false` propagated | 9/9 vitest PASS | PASS |
| No provider call | no live memory retrieval | N/A with reason: deterministic local only |
| No corpus ingestion | adapter is type mapping only | N/A with reason: no corpus mutation |
| No T12 | T8 does not authorize T12 | N/A with reason: separately forbidden |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md` | reviewer completion authored | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_ROADMAP_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer session sync in closure batch | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer session sync in closure batch | PASS |
| External evidence digest | no external authorized | N/A | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new adapter function only | N/A with reason: helper function only |
| Session continuity | active handoff | reviewer-owned sync in closure batch | PASS |

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized T8 preparation via explicit
chat instruction 2026-06-08; dispatch still requires refreshed DSCP-T7 closure
evidence.

## Reviewer Closure Conversion

```yaml
completionReviewPath: docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md
reviewerOwnedClosurePaths:
  - CVF_SESSION/ACTIVE_SESSION_STATE.json
  - CVF_SESSION_MEMORY.md
  - AGENT_HANDOFF_V17_2026-06-07.md
  - docs/roadmaps/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_ROADMAP_2026-06-08.md
  - docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T8_MKE1_CROSS_LANE_WIREIN_FOR_CLAUDE_2026-06-08.md
closedStatusTokens:
  - CLOSED_PASS_BOUNDED
reviewerClosureCompleted: true
forbiddenClosedEquivalentResidue: []
```

## Claim Boundary

This work order claims: implementation contract, source verification, and
gate requirements for DSCP-T8. It does not claim: runtime provider behavior,
live proof, corpus ingestion, public readiness, production readiness, or T12.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
