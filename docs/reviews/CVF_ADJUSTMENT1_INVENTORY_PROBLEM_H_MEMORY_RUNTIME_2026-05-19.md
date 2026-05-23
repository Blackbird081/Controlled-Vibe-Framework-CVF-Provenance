# CVF Adjustment 1 Inventory — Problem H: Memory Runtime

Memory class: SUMMARY_RECORD

Status: FILED — 2026-05-19. Pre-GC-018 factual inventory per
`docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
Adjustment 1 requirement.

## Purpose

Record the factual pre-GC-018 inventory for Problem H so memory runtime work
remains demand-gated and does not wire contract-only memory paths prematurely.

## Source

- `docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` §
  Adjustment 1 + corrected Problem H
- Live scan of `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`,
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`, and
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  performed 2026-05-19 by coordinating agent (Claude)

## Scope / Target / Owner Boundary

Scope: Problem H only — Memory Hierarchy / Memory Runtime enforcement.
Owner: Claude (reviewer role) per Adjustment 1 instruction.

## Findings

### What already exists

**`CVF_GUARD_CONTRACT` — memory contracts:**

| File | Lines | Key exports |
|---|---|---|
| `src/contracts/memory-continuity.contract.ts` | 223 | `MemoryTierOwnerRole`, `MemoryTierOwnerPolicy`, `MemoryReinjectionPolicy`, `MemoryContinuityTier`, `MemoryContinuityContractTable` |

`MemoryReinjectionPolicy` (line 46) defines: `canReinject: boolean`,
`requiresProvenance: boolean`, `maxReinjectTokens: number`,
`allowedTiers: MemoryContinuityTier[]`, `sensitivityGate`.

`MemoryTierOwnerPolicy` (line 38) defines: `ownerRole`, `writeAllowed`,
`readAllowed`, `crossSessionAllowed`.

30 test files in `CVF_GUARD_CONTRACT`.

**`CVF_LEARNING_PLANE_FOUNDATION` — controlled memory gateway:**

| File | Lines | Key exports |
|---|---|---|
| `src/controlled.memory.gateway.contract.ts` | 395 | `ControlledMemoryRecord`, `ControlledMemoryCaptureRequest`, `ControlledMemoryQueryRequest`, `ControlledMemoryReinjectionRequest`, `ControlledMemoryReceipt`, `ControlledMemoryPolicyResult` |
| `src/controlled.memory.subcontracts.ts` | — | Subcontract layer for memory operations |

`controlled.memory.gateway.contract.ts` defines:
- `ControlledMemoryKind`: `working | episodic | semantic | procedural`
- `ControlledMemoryScope`: `session | project | user | global`
- `ControlledMemorySensitivity`: `public | internal | confidential | restricted`
- `ControlledMemoryDecision`: `captured | retrieved | reinjectable | denied | requires_approval`
- `canReinject` flag on `ControlledMemoryPolicyContext` (line 23)
- Reinjection denial path at line 354: `"memory_reinjection_not_authorized"`

`src/index.ts` (703 lines) exports reinjection consumer pipeline
contracts (`learning.reinjection.consumer.pipeline.contract`,
`.batch.contract`, `learning.reinjection.contract`).

**Live execute path (`route.ts`):**

`route.ts` imports `buildRouteAuditMemoryCapture` from
`@/lib/audit-memory-receipt` (line 33) and calls it at line 927 to
produce `auditMemoryReceipt` and `auditEventPayload`. This is a
**governance audit receipt** (records that an execution happened) —
it is NOT a `ControlledMemoryReinjectionRequest` or a
`ControlledMemoryCaptureRequest`. The live execute path does not
currently call `controlled.memory.gateway.contract` at all.

### What the actual gap is

The memory contract infrastructure is mature and comprehensive:
`MemoryReinjectionPolicy`, `MemoryTierOwnerPolicy`,
`ControlledMemoryRecord`, and a full reinjection pipeline all exist in
contract form. The gap is **live-path wiring**: no flow in the current
execute path calls `ControlledMemoryCaptureRequest` or
`ControlledMemoryReinjectionRequest`. Memory enforcement is
contract-local only — it does not gate or enrich any real execution.

A demand gate is required before this lane can be authorized: a specific
execution flow that actually writes or reads memory must be identified.
The Product Brief flow (`app_builder_complete`) has no memory write step,
so it is not a valid demand gate for H.

### What "done" looks like for the next tranche

Lane H acceptance criterion (when demand-gated): at least one named flow
(not Product Brief) calls `ControlledMemoryCaptureRequest` in the live
execute path and produces a `ControlledMemoryReceipt` in the audit event
payload. Gate: `MemoryReinjectionPolicy.canReinject` is evaluated for
that flow. Confirmed by route integration test.

**Lane H is NOT in the current authorized sequence (D→E→F→G).** It
requires a separate GC-018 with a named memory-writing flow, filed after
Lane G closes.

## Risk

None. Read-only inventory. No code changed. Premature wiring of
`ControlledMemoryCaptureRequest` into route.ts without a named flow
would bloat the route and create untestable code paths.

## Decision / Recommendation / Disposition

Problem H: **GAP CONFIRMED, DEMAND-GATED** — contract infrastructure
is complete (GUARD_CONTRACT + LEARNING_PLANE); live-path wiring is
absent. Not authorized in Lanes D–G. Requires separate GC-018 with
named memory-writing flow after Lane G closure.

## Claim Boundary

This packet is read-only inventory evidence. It does not authorize Lane H
implementation, memory reinjection, or live-path memory capture without a
separate demand-gated GC-018.
