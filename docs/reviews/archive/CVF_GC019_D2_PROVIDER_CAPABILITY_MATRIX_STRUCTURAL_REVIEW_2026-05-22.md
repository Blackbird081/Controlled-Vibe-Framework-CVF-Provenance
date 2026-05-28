# CVF GC019 D2 Provider Capability Matrix Structural Review

Memory class: FULL_RECORD

Status: APPROVED_BOUNDED_STRUCTURAL_DELTA

Date: 2026-05-22

## Purpose

Record the GC-019 structural review required because D2 adds a new registry
module under `EXTENSIONS/CVF_MODEL_GATEWAY`.

## Scope / Target / Owner Boundary

Target: the bounded D2 implementation files under
`EXTENSIONS/CVF_MODEL_GATEWAY/src` and focused tests.

Owner: Codex as implementing and reviewing agent under the operator-authorized
post-B/C Review-CVF remaining pain-point sequence.

Boundary: this is a contract/registry/gate addition only. It is not a package
merge, extension merge, ownership transfer, directory relocation, route change,
live adapter expansion, provider parity claim, receipt-envelope change,
public-sync update, hosted readiness, or freeze release.

## Target / Source

Source artifacts:

- `docs/baselines/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- `docs/work_orders/CVF_WO_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- `docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`

Changed structural surface:

- added `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- added focused registry tests
- expanded existing provider method contract and gate helpers
- updated package index exports

## Scope / Methodology

Methodology:

- inspect whether the new file creates a new package, plane, extension root, or
  ownership boundary;
- verify registry additions are bounded to the existing Model Gateway owner;
- verify no route, receipt, provider runtime, or public-sync surface changed;
- verify package tests and TypeScript check pass.

## Findings / Position

Finding 1: the new registry module is structurally bounded to the existing
Model Gateway package.

Finding 2: no package root, extension root, route ownership, or authority
boundary moved.

Finding 3: the registry records current provider capability facts and negative
gate behavior; it does not introduce new runtime provider calls.

Finding 4: `retry`, `cost`, and `risk` remain owner references to existing
Model Gateway surfaces.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Registry file becomes hidden provider runtime expansion | Completion review states no new live adapter behavior |
| New method axis implies parity | Tests and docs distinguish declared axis from supported pairs |
| Structural trigger lacks GC-019 artifact | Filed this bounded structural review |
| Public claim drifts | Public catalog disposition is N/A |

## Decision / Recommendation / Disposition

Disposition: `APPROVED_BOUNDED_STRUCTURAL_DELTA`.

Recommendation: accept the D2 registry addition as structurally safe. Continue
to E2 only through a fresh GC-018/work order and any required blocked-work
override.

## Evidence Trace Block

Verification:

```text
npm test -- tests/provider-capability-registry.test.ts tests/provider-method-coverage.test.ts
-> PASS, 2 files / 11 tests

npm run check
-> PASS

npm test
-> PASS, 20 files / 80 tests
```

## Claim Boundary

This GC-019 review approves only the bounded Model Gateway registry and method
gate addition needed for D2. It does not approve new provider runtime behavior,
all-provider parity, route changes, receipt-envelope changes, public-sync,
hosted readiness, Maika proof, or freeze release.
