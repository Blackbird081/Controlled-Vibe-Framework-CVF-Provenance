Memory class: SUMMARY_RECORD

# CVF GAP-MEM Subcontracts Runtime Adoption Roadmap - 2026-05-17

Status: COMPLETED LOCALLY.

## Authorization

Authorized by:

- `docs/baselines/CVF_GC018_GAP_MEM_SUBCONTRACTS_AUTHORIZATION_2026-05-17.md`

## Purpose

Complete CD-3 Step 6 by closing the three reduced memory-specific gaps:
privacy filter, capture adapter source gate, and retention policy.

## Scope

Owner surface:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`

## Non-Goals

- no memory server;
- no hidden memory write;
- no cross-project sharing;
- no automatic semantic promotion;
- no reinjection bypass.

Runtime files:

- `src/controlled.memory.subcontracts.ts`
- `src/controlled.memory.gateway.contract.ts`
- `tests/controlled.memory.subcontracts.test.ts`
- `tests/controlled.memory.gateway.contract.test.ts`

## Work Plan

| Step | Work | Status |
|---|---|---|
| 1 | GC-018 authorization | complete |
| 2 | Memory-specific privacy filter | complete |
| 3 | Approved capture-source gate | complete |
| 4 | Retention and review-gate decision helper | complete |
| 5 | Integrate subcontracts into controlled memory gateway | complete |
| 6 | focused tests and typecheck | complete |

## Acceptance Criteria

The tranche is acceptable only if:

- raw email, password, token, and private-key-like values are filtered before
  memory storage;
- capture sources outside the approved adapter list are denied;
- working and episodic memory are not permanent by default;
- sensitive memory records carry a review-gate signal;
- existing controlled memory gateway tests still pass.

## Verification

Executed:

```bash
cd EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION
npm run check
npx vitest run tests/controlled.memory.gateway.contract.test.ts tests/controlled.memory.subcontracts.test.ts --config vitest.config.ts
```

## Claim Boundary

This tranche strengthens memory capture. It does not create hidden memory,
cross-project sharing, automatic semantic promotion, or reinjection without
the existing policy gate.
