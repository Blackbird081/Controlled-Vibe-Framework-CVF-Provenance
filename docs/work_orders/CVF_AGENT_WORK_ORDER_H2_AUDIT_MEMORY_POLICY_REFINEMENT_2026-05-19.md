# CVF Agent Work Order — H2: Audit Memory Policy Refinement

Memory class: SUMMARY_RECORD

Status: CLOSED

GC-018 required: Yes — modifies existing enforcement surface in cvf-web lib.
GC-018 path: `docs/baselines/CVF_GC018_H2_AUDIT_MEMORY_POLICY_REFINEMENT_2026-05-19.md`

## Purpose

Refine `audit-memory-receipt.ts` to surface `writesRequireReceipt` and
`privacyFilters` from the frozen tier policy in the `AuditMemoryReceipt`
return type, add an explicit degraded-capture path when write is policy-denied,
and add two new tests asserting `session.ownerRole = OPERATOR` and
`writesRequireReceipt = true`. Preserves `canReinject: false` in all paths.
Does NOT use `reinjectionAllowed` as a write gate.

## Authority Chain

`docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` — H2
section. GC-018 must be filed and accepted before implementation begins.
Codex rebuttal accepted: `canReinject: false` preserved; `session.ownerRole`
must remain `OPERATOR`; `reinjectionAllowed` must NOT be used as write gate.

## Agent Roles

- **Orchestrator** — files GC-018; dispatches work order; accepts completion
  packet.
- **Worker** — implements all tasks in cvf-web lib only; runs pre-flight
  before any code; files completion review upon closure.

## Scope

**Allowed scope:** `cvf-web/src/lib/audit-memory-receipt.ts` and its test file only.

- Modified: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- Modified (or new): `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.test.ts`

**Forbidden scope:**

- Modifying `memory-continuity.contract.ts` (frozen policy data — read only)
- Adding memory reinjection, persistent/archive writes
- Changing `canReinject: false` to any other value
- Using `reinjectionAllowed` field from tier policy as a write gate
- Changing `route.ts` beyond what is strictly required by type changes
- Public-sync repo edits under this WO
- Adding new memory tiers

## Required First Reads

1. `cvf-web/src/lib/audit-memory-receipt.ts` (178 lines) — full file
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`
   — lines with `session:`, `ownerRole`, `writesRequireReceipt`,
   `reinjectionAllowed`, `privacyFilters`
3. Existing audit-memory-receipt test file (if any)
4. Roadmap H2 section — done criterion, invariants

## Source-Fidelity Pre-Flight (Worker must verify before writing)

```text
1. Confirm session.ownerRole = 'OPERATOR' in memory-continuity.contract.ts
2. Confirm session.writesRequireReceipt = true
3. Confirm session.reinjectionAllowed = true (NOT false — reinjection field,
   not write gate)
4. Confirm session.privacyFilters = ['scope_minimization', 'pii_redaction']
5. Confirm canReinject: false in buildAuditMemoryReceipt capture call (line 77)
6. Confirm audit-memory-receipt.ts is currently 178 lines
```

## Write Ownership

Worker owns: `audit-memory-receipt.ts` and its test file. No other files.

## Execution Plan

Task 1 (type extension) → Task 2 (populate fields) → Task 3 (degraded path)
→ Task 4 (tests) in sequence.

### Task 1 — Extend `AuditMemoryReceipt` type

In `audit-memory-receipt.ts`, add to the `AuditMemoryReceipt` interface:

```typescript
  writesRequireReceipt: boolean;
  privacyFilters: readonly string[];
```

### Task 2 — Populate fields in `buildAuditMemoryReceipt`

In the return statement of `buildAuditMemoryReceipt()`, add:

```typescript
  writesRequireReceipt: ownerPolicy.writesRequireReceipt,
  privacyFilters: ownerPolicy.privacyFilters,
```

`ownerPolicy` = `MEMORY_TIER_OWNER_POLICIES['session']` already read earlier
in the function. No new import needed.

### Task 3 — Degraded-capture explicit gate

Before the `auditMemoryGateway.capture()` call, add:

```typescript
  if (!ownerPolicy.writesRequireReceipt) {
    // policy_skipped: tier does not require a receipt write; skip capture
    return {
      tier,
      contractVersion: MEMORY_CONTINUITY_CONTRACT_VERSION,
      ownerRole: ownerPolicy.ownerRole,
      writesRequireReceipt: ownerPolicy.writesRequireReceipt,
      privacyFilters: ownerPolicy.privacyFilters,
      reinjectionPolicy: {
        tier,
        privacyFilter: reinjectionPolicy.privacyFilter,
        provenanceScoreThreshold: reinjectionPolicy.provenanceScoreThreshold,
        maxAgeSeconds: reinjectionPolicy.maxAgeSeconds,
        receiptRequired: reinjectionPolicy.receiptRequired,
      },
      receipt: {
        decision: 'policy_skipped' as const,
        receiptId: '',
        memoryIds: [],
      } as unknown as ControlledMemoryReceipt,
    };
  }
```

Note: for `session` tier, `writesRequireReceipt = true`, so this branch is
never taken at runtime today. It is a defensive gate for other tiers if this
function is ever generalized. The code path must be covered by a test using a
synthetic policy.

`audit-memory-receipt.ts` must stay ≤ 220 lines after all additions.

### Task 4 — Two new tests

Add to the test file:

```typescript
test('session ownerRole is OPERATOR', () => {
  const result = buildAuditMemoryReceipt({
    governanceReceiptId: 'gr-001',
    actorId: 'actor-001',
    actorRole: 'OPERATOR',
  });
  expect(result.ownerRole).toBe('OPERATOR');
});

test('writesRequireReceipt is true for session tier', () => {
  const result = buildAuditMemoryReceipt({
    governanceReceiptId: 'gr-002',
    actorId: 'actor-002',
    actorRole: 'SERVICE_AGENT',
  });
  expect(result.writesRequireReceipt).toBe(true);
  expect(Array.isArray(result.privacyFilters)).toBe(true);
  expect(result.privacyFilters).toContain('pii_redaction');
});
```

Invariant assertions (add as comments in test file, not separate tests):

- `canReinject: false` is hardcoded in capture call — do not change
- `reinjectionAllowed` from policy = `true` for session; it is a reinjection
  field, not used as write gate — preserved as-is

## Acceptance Criteria

- [ ] `AuditMemoryReceipt` interface gains `writesRequireReceipt: boolean` and `privacyFilters: readonly string[]`
- [ ] `buildAuditMemoryReceipt` populates both fields from `MEMORY_TIER_OWNER_POLICIES['session']`
- [ ] Degraded-capture `policy_skipped` gate added before `capture()` call (≤ 15 lines)
- [ ] `audit-memory-receipt.ts` ≤ 220 lines after all additions
- [ ] 2 new tests PASS: `session ownerRole is OPERATOR`, `writesRequireReceipt is true for session tier`
- [ ] `canReinject: false` unchanged in capture call
- [ ] `reinjectionAllowed` NOT used as write gate
- [ ] `npm run build` PASS

## Evidence Requirements

Completion review must include:

1. `npm run test:run -- src/lib/audit-memory-receipt.test.ts` — all tests PASS
   including 2 new.
2. `npm run build` — PASS (type changes propagate cleanly).
3. `audit-memory-receipt.ts` line count ≤ 220.
4. `canReinject: false` still present in capture call (grep output).
5. Confirmation: `reinjectionAllowed` not used as write gate (grep output).
6. `result.ownerRole === 'OPERATOR'` confirmed in test output.

## Review Gate

Orchestrator reviews completion packet. No closure without:

- 2 new tests PASS
- `canReinject: false` preservation confirmed
- `npm run build` PASS

## Closure Checklist

- [ ] GC-018 filed and accepted before implementation
- [ ] `AuditMemoryReceipt` gains `writesRequireReceipt` + `privacyFilters`
- [ ] `buildAuditMemoryReceipt` populates both fields from frozen policy
- [ ] Degraded-capture `policy_skipped` gate added (≤ 15 lines)
- [ ] `audit-memory-receipt.ts` ≤ 220 lines
- [ ] 2 new tests PASS (`ownerRole = OPERATOR`, `writesRequireReceipt = true`)
- [ ] `canReinject: false` unchanged
- [ ] `reinjectionAllowed` NOT used as write gate
- [ ] `npm run build` PASS
- [ ] Completion review filed in CVF `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- `audit-memory-receipt.ts` would exceed 220 lines — report and stop
- `canReinject: false` would need to change for any reason — stop and report
- `npm run build` fails after type change (type mismatch in route.ts or tests)
- Pre-flight finds `session.ownerRole` is not `OPERATOR` — source has changed;
  do not proceed without re-reading this work order against new source

## Target repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
and its test file only.

## Claim Boundary

H2 covers policy field surfacing and degraded-capture gate in the existing
audit-memory receipt flow. It does not add memory reinjection, persistent or
archive memory, new memory tiers, route changes beyond type propagation, or
any provider-side memory behavior.
