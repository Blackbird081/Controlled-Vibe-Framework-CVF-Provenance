<!-- Memory class: SUMMARY_RECORD -->

# CVF Controlled Memory Test And Proof Plan - 2026-05-16

Status: ACCEPTED LOCAL TEST PLAN.

## Purpose

Define verification required for the Controlled Memory runtime absorption
tranche.

## Source

Source lane:

- CVF 16.5 `agentmemory`

Owner package:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`

## Required Evidence

Focused deterministic tests must prove:

- capture fails closed on deny;
- approval-required policy pauses memory use;
- restricted memory requires restricted authorization;
- privacy filtering masks PII and secrets before persistence;
- retrieval respects scope, kind, lifecycle, query, and token budget;
- expired memory is not returned;
- reinjection requires explicit authorization;
- reinjection context segments include provenance.

## Verification

Commands:

```bash
cd EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION
npm run check
npx vitest run tests/controlled.memory.gateway.contract.test.ts --config vitest.config.ts
```

## Baseline

Live provider proof is not required for this tranche because the claim is a
deterministic local memory-governance contract. Live proof becomes required only
if a later tranche claims live AI/provider memory enforcement.

## Claim Boundary

Passing this plan may claim `runtime-owned` controlled memory primitives. It may
not claim live governance enforcement or production persistence.
