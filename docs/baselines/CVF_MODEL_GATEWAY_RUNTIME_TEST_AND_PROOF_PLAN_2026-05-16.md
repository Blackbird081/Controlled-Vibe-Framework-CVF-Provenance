<!-- Memory class: SUMMARY_RECORD -->

# CVF Model Gateway Runtime Test And Proof Plan - 2026-05-16

Status: roadmap-ready planning artifact; implementation pending approval.

## Test Principle

Every adopted runtime primitive from `freellmapi` needs focused vitest coverage.
Cross-file behavior needs integration tests. Governance enforcement claims need
live proof.

## Unit Test Coverage

| Runtime primitive | Test file |
|---|---|
| Provider registry | `tests/provider-registry.test.ts` |
| Provider health | `tests/provider-health.test.ts` |
| Quota ledger | `tests/quota-ledger.test.ts` |
| Routing policy | `tests/routing-policy.test.ts` |
| Fallback policy | `tests/fallback-policy.test.ts` |
| Sticky session | `tests/sticky-session.test.ts` |
| Credential boundary | `tests/credential-boundary.test.ts` |
| Gateway receipt | `tests/gateway-receipt.test.ts` |

## Integration Tests

Required integration coverage:

- route denied when Guard Contract result is `deny`;
- route requires approval when Guard Contract result is `requires_approval`;
- route allowed only when provider is registered, enabled, healthy, quota
  allowed, and model exists;
- fallback preserves requested model, actual model, reason, health, and quota
  state in receipt;
- credential boundary never returns raw secret in receipt or public metadata.

Suggested file:

`tests/model-gateway-runtime.integration.test.ts`

## Package Checks

Run from `EXTENSIONS/CVF_MODEL_GATEWAY/`:

```bash
npm run check
npm test
```

If package source changes, this package-level verification is mandatory under
GC-029.

## Repository Proof

Docs/code governance checks:

```bash
git diff --check
python governance/compat/check_governed_file_size.py
```

Release-quality governance proof, only when claiming runtime enforcement:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Live proof must use operator-supplied keys through environment variables only.
Raw keys must never be printed or committed.

## Claim Boundary

Passing unit tests may claim implementation correctness for deterministic local
gateway primitives.

Passing package checks may claim package-level type/test health.

Only live release-gate proof may support claims that CVF governance enforcement
works through the live AI/provider path.

