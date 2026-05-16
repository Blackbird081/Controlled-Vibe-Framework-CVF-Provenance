Memory class: SUMMARY_RECORD

# CVF ADD Provider Output Contracts Runtime Adoption Roadmap - 2026-05-17

Status: COMPLETED LOCALLY.

## Authorization

Authorized by:

- `docs/baselines/CVF_GC018_ADD_PROVIDER_OUTPUT_CONTRACTS_AUTHORIZATION_2026-05-17.md`

## Purpose

Complete CD-3 Step 5 by standardizing provider command output handling inside
the CVF Model Gateway.

## Scope

Owner surface:

- `EXTENSIONS/CVF_MODEL_GATEWAY/`

## Non-Goals

- no new provider adapter;
- no routing change;
- no live provider proof claim;
- no output-quality claim.

Runtime files:

- `src/provider-output-contract.ts`
- `tests/provider-output-contract.test.ts`

## Work Plan

| Step | Work | Status |
|---|---|---|
| 1 | GC-018 authorization | complete |
| 2 | JSON envelope parser | complete |
| 3 | NDJSON stream parser | complete |
| 4 | stdout/stderr machine-readability policy | complete |
| 5 | exit-code classification | complete |
| 6 | focused tests and typecheck | complete |

## Acceptance Criteria

The tranche is acceptable only if:

- JSON envelopes normalize missing fields safely;
- NDJSON chunks preserve order;
- empty or human-log stdout is rejected;
- rate-limit and timeout exits are retryable;
- auth, config, provider, and contract exits are not retryable by default.

## Verification

Executed:

```bash
cd EXTENSIONS/CVF_MODEL_GATEWAY
npm run check
npx vitest run tests/provider-output-contract.test.ts --config vitest.config.ts
```

## Claim Boundary

This tranche standardizes provider output interpretation. It does not add a
provider, change routing, or claim live provider behavior.
