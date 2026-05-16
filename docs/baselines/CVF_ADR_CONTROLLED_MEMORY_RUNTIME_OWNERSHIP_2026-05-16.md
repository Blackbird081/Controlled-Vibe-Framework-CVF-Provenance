<!-- Memory class: SUMMARY_RECORD -->

# ADR - CVF Controlled Memory Runtime Ownership - 2026-05-16

Status: ACCEPTED.

## Purpose

Decide where the controlled-memory runtime primitive should live after the
CVF 16.5 `agentmemory` intake.

## Scope

This ADR applies only to the local deterministic Controlled Memory primitive in
the Learning Plane. It does not authorize persistence infrastructure or live
provider integration.

## Context

The legacy `agentmemory` folder proposes shared memory, capture hooks,
retrieval, lifecycle policy, access control, privacy filtering, and reinjection.
Those patterns fit CVF, but a standalone memory server would violate the CVF
boundary that external knowledge can inform CVF but cannot become authority.

## Decision

`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/` owns the adapted runtime primitive:

- `src/controlled.memory.gateway.contract.ts`
- `tests/controlled.memory.gateway.contract.test.ts`

The Learning Plane owns memory lifecycle, learning/reinjection semantics, and
receiptable deterministic behavior. Control Plane context packaging and
Governance Expansion policy concepts are represented in the contract boundary,
not as separate runtime owners in this tranche.

## Alternatives

### Agentmemory Runtime

Rejected. It would create a parallel memory authority and bypass CVF policy.

### Docs-Only Absorption

Rejected for this tranche. The operator requires absorbed knowledge to become
alive inside CVF when selected for implementation.

### Control Plane Owner

Deferred. Context packaging remains a consumer boundary, but memory lifecycle
and reinjection semantics already fit the Learning Plane better.

## Consequences

- memory capture requires policy and write authorization;
- privacy filtering happens before memory persistence;
- retrieval respects scope, lifecycle, sensitivity, denied ids, and token
  budget;
- reinjection requires explicit authorization and emits provenance-bearing
  context segments;
- receipts are deterministic local evidence.

## Verification

Verification is package-level deterministic testing:

```bash
cd EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION
npm run check
npx vitest run tests/controlled.memory.gateway.contract.test.ts --config vitest.config.ts
```

## Claim Boundary

This ADR proves ownership and deterministic local contract behavior only. It
does not claim live provider governance enforcement.
