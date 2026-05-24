# CVF GC-018 H2 Audit Memory Policy Refinement

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize H2 to surface `writesRequireReceipt` and `privacyFilters` from the
frozen session tier policy in the `AuditMemoryReceipt` return type, add an
explicit degraded-capture path when write is policy-denied, and add two new
tests asserting `session.ownerRole = OPERATOR` and
`writesRequireReceipt = true`.

This closes the H2 gap: consumers of `buildAuditMemoryReceipt()` currently
cannot tell whether a write was gated or skipped. The refinement makes policy
enforcement observable in the receipt output without changing the gateway
behavior or the `canReinject: false` invariant.

## Scope

In scope:

- extend `AuditMemoryReceipt` interface with `writesRequireReceipt: boolean`
  and `privacyFilters: readonly string[]`;
- populate both fields from `MEMORY_TIER_OWNER_POLICIES['session']` in
  `buildAuditMemoryReceipt()`;
- add a degraded-capture `policy_skipped` gate before `capture()` call (≤ 15
  lines; never triggered at runtime for session tier today — defensive gate);
- add 2 new tests: `session ownerRole is OPERATOR`,
  `writesRequireReceipt is true for session tier`;
- preserve `canReinject: false` in all paths;
- `audit-memory-receipt.ts` stays ≤ 220 lines; `npm run build` PASS.

Out of scope:

- modifying `memory-continuity.contract.ts` (frozen policy data — read only);
- adding memory reinjection or persistent/archive writes;
- changing `canReinject: false` to any other value;
- using `reinjectionAllowed` field from tier policy as a write gate;
- changing `route.ts` beyond what is strictly required by type changes;
- public-sync repo edits under this baseline;
- adding new memory tiers.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` — H2 section
- `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
  (178 lines — baseline confirmed)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`
  — `session.ownerRole = 'OPERATOR'`, `session.writesRequireReceipt = true`,
  `session.reinjectionAllowed = true` (reinjection field, NOT write gate),
  `session.privacyFilters = ['scope_minimization', 'pii_redaction']`
- `docs/baselines/CVF_GC018_LANE_H_MEMORY_RUNTIME_WIRING_2026-05-19.md`
  — H1 predecessor baseline (session-tier audit memory receipt already wired)

## Decision / Baseline / Proposed Tranche

Decision: implement H2 as a policy-field surfacing refinement. The existing
`buildAuditMemoryReceipt()` function already reads `MEMORY_TIER_OWNER_POLICIES`
but does not expose `writesRequireReceipt` or `privacyFilters` in its return
type. H2 surfaces these fields and adds a defensive gate for the case where a
tier policy does not require a receipt write.

Selected invariants:

| Invariant | Value | Enforcement |
|---|---|---|
| `canReinject` | `false` | Hardcoded in capture call — must not change |
| `session.ownerRole` | `'OPERATOR'` | From frozen policy — asserted in new test |
| `reinjectionAllowed` | Not used as write gate | Gate uses `writesRequireReceipt` only |
| `writesRequireReceipt` | `true` for session tier | Surfaced in receipt + asserted in test |

## Rule

H2 may claim:

> `buildAuditMemoryReceipt()` now surfaces `writesRequireReceipt` and
> `privacyFilters` from the frozen session tier policy. A defensive
> `policy_skipped` gate is present for tiers where `writesRequireReceipt`
> is false.

H2 must not claim:

> memory reinjection, persistent or archive tier writes, new memory tiers,
> or any change to the `canReinject: false` invariant.

## Claim Boundary

This baseline authorizes only the policy-field surfacing and degraded-capture
gate in `audit-memory-receipt.ts` and its test file. It does not authorize
changes to `memory-continuity.contract.ts`, `route.ts` (beyond type propagation),
or any provider-side memory behavior.

## Allowed And Forbidden Requirements

Allowed:

- add `writesRequireReceipt: boolean` and `privacyFilters: readonly string[]`
  to `AuditMemoryReceipt` interface;
- populate both fields from `ownerPolicy` (already read in function);
- add `if (!ownerPolicy.writesRequireReceipt)` gate returning
  `decision: 'policy_skipped'` before `capture()` call;
- add 2 new tests asserting `ownerRole === 'OPERATOR'` and
  `writesRequireReceipt === true`;
- read `memory-continuity.contract.ts` as frozen source of truth.

Forbidden:

- changing `canReinject: false` to any other value;
- using `reinjectionAllowed` as a write gate;
- writing to persistent or archive memory tiers;
- modifying `memory-continuity.contract.ts`;
- making `audit-memory-receipt.ts` exceed 220 lines.

## Exceptions

None. Any reinjection path or new memory tier requires a separate GC-018.

## Enforcement Surface

Verification must include:

- `npm run test:run -- src/lib/audit-memory-receipt.test.ts` — all tests PASS
  including 2 new;
- `npm run build` PASS (type changes propagate cleanly);
- `audit-memory-receipt.ts` line count ≤ 220;
- `canReinject: false` still present in capture call (grep confirmation);
- `reinjectionAllowed` not used as write gate (grep confirmation);
- `result.ownerRole === 'OPERATOR'` confirmed in test output.

## Evidence / Verification

Expected commands:

```powershell
npm run test:run -- src/lib/audit-memory-receipt.test.ts
npm run build
```

Run in:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
```

## Claim / Final / Verification Boundary

Final boundary: H2 refines the audit memory receipt to surface policy fields
and adds a defensive degraded-capture gate. Verification is limited to targeted
library tests and the TypeScript build. Provider-side memory, reinjection, and
broad runtime changes are outside this baseline.
