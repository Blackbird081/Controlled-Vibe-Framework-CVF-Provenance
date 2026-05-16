<!-- Memory class: SUMMARY_RECORD -->

# CVF Model Gateway Runtime Adoption Roadmap - 2026-05-16

Status: ROADMAP CANDIDATE - awaiting operator approval before implementation.

Authorization:
`docs/baselines/CVF_GC018_MODEL_GATEWAY_RUNTIME_AUTHORIZATION_2026-05-16.md`

ADR candidate:
`docs/baselines/CVF_ADR_MODEL_GATEWAY_RUNTIME_OWNERSHIP_2026-05-16.md`

Source adoption matrix:
`docs/baselines/CVF_MODEL_GATEWAY_RUNTIME_SOURCE_ADOPTION_MATRIX_2026-05-16.md`

Test/proof plan:
`docs/baselines/CVF_MODEL_GATEWAY_RUNTIME_TEST_AND_PROOF_PLAN_2026-05-16.md`

## Decision

Recommended ownership decision: **implementation-owner upgrade**.

`EXTENSIONS/CVF_MODEL_GATEWAY/` should move from wrapper-only package to the
implementation owner for the bounded gateway primitives adopted in this tranche.

This decision must be recorded by accepting or amending:

`docs/baselines/CVF_ADR_MODEL_GATEWAY_RUNTIME_OWNERSHIP_2026-05-16.md`

## Why This Tranche

The CVF 16.5 intake and Claude rebuttal identified Model Gateway as the highest
fit first runtime adoption surface because:

- CVF already has `EXTENSIONS/CVF_MODEL_GATEWAY/`;
- the source bundle has 8 small TypeScript artifacts already written;
- provider registry, health, quota, routing, fallback, sticky session,
  credential boundary, and gateway receipt are central CVF runtime boundaries;
- adopting them reduces future token waste and prevents parallel gateway drift.

## Scope

Adopt and adapt these source candidates:

- `provider.registry.ts`
- `provider.health.ts`
- `quota.ledger.ts`
- `routing.policy.ts`
- `fallback.policy.ts`
- `sticky.session.ts`
- `credential.vault.ts`
- `gateway.receipt.ts`

Target package:

- `EXTENSIONS/CVF_MODEL_GATEWAY/`

## Non-Goals

- No wholesale copy from private reference.
- No free-provider, subscription-bypass, or unlimited-access claim.
- No second Model Gateway package.
- No public provider support claim.
- No live governance enforcement claim until live proof passes.
- No GC-023 exception request before file splitting.

## Work Plan

### CP1 - Ownership And Package Shape

- Accept or amend ADR decision.
- Keep existing re-export lineage.
- Add new runtime modules under `EXTENSIONS/CVF_MODEL_GATEWAY/src/`.
- Keep module files small and responsibility-scoped.

Exit criteria:

- ADR accepted.
- README updated with wrapper lineage plus runtime owner upgrade boundary.

### CP2 - Core Gateway Primitives

- Adapt provider registry.
- Adapt provider health.
- Adapt quota ledger.
- Adapt gateway receipt.

Exit criteria:

- 4 focused vitest files pass.
- Types export from package entrypoint.

### CP3 - Route Decision Primitives

- Adapt routing policy.
- Adapt fallback policy.
- Adapt sticky session.
- Adapt credential boundary.

Exit criteria:

- 4 focused vitest files pass.
- Credential tests prove no raw key appears in public metadata/receipt.

### CP4 - Guard Contract Integration

- Add gateway policy context type.
- Require policy result before routing.
- Fail closed on `deny` and `requires_approval`.
- Preserve policy decision in gateway receipt.

Exit criteria:

- Integration test proves deny/approval/allow paths.
- No route selection without policy boundary.

### CP5 - Verification And Closure

- Run package checks.
- Run governed file-size check.
- Run release-gate bundle only if claiming live enforcement.
- Publish closure note and update handoff.

Exit criteria:

- `npm run check` pass in `EXTENSIONS/CVF_MODEL_GATEWAY/`.
- `npm test` pass in `EXTENSIONS/CVF_MODEL_GATEWAY/`.
- GC-023 pass without new exception.
- Live proof artifact exists if enforcement claim is made.
- End-of-tranche commit message is descriptive and references Model Gateway
  runtime adoption.

## Acceptance Criteria

- All 8 source candidates are either adapted or explicitly rejected with reason.
- Each adopted runtime primitive has a focused vitest file.
- Routing cannot proceed without Guard Contract policy context.
- Receipts preserve provider, model, health, quota, fallback, policy, and
  validation state.
- Credential boundary never exposes raw key values.
- Package-level check and tests pass.
- No file-size exception is requested before splitting.

## Approval Gate

Implementation may begin only after the operator approves this roadmap-ready
packet.

Suggested approval phrase:

```text
APPROVE MODEL GATEWAY RUNTIME ROADMAP PACKET 2026-05-16
```

