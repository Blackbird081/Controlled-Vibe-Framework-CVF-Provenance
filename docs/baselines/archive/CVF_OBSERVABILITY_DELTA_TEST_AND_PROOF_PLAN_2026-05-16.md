Memory class: SUMMARY_RECORD

# CVF Observability Delta Test And Proof Plan - 2026-05-16

Status: ACTIVE TEST PLAN.

## Purpose

Define the proof required to close Observability Delta as a living CVF runtime
contract.

## Scope

Target package:

- `EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME/`

Runtime file:

- `observability/observe.only.signal.contract.ts`

Test file:

- `tests/observe.only.signal.contract.test.ts`

## Source

Source folder:

- `.private_reference/legacy/CVF 16.5/abtop/`

Predecessor evidence:

- `docs/baselines/CVF_GC018_OBSERVABILITY_DELTA_AUTHORIZATION_2026-05-16.md`
- `docs/baselines/CVF_ADR_OBSERVABILITY_DELTA_RUNTIME_OWNERSHIP_2026-05-16.md`
- `docs/baselines/CVF_OBSERVABILITY_DELTA_SOURCE_ADOPTION_MATRIX_2026-05-16.md`

## Decision

Use deterministic local tests as the proof source for this tranche.

The proof is sufficient because this tranche claims observe-only runtime signal
behavior, not live provider enforcement, dashboard streaming, or operating
system process control.

## Test Matrix

| Behavior | Required proof | Status |
|---|---|---|
| Token/context thresholds | NORMAL, NOTICE, WARNING, HIGH, CRITICAL boundaries | required |
| Token source boundary | trusted runtime/provider/billing source accepted; agent self-report flagged | required |
| Receipt requirement | HIGH and CRITICAL signals require receipt | required |
| Rate/quota pressure | normal, provider warning, repeated throttle, quota exhausted mapping | required |
| Process/port anomaly | unknown process, orphan process, external exposure mapping | required |
| Receipt determinism | same signal creates same receipt | required |
| Observe-only boundary | observe/alert allowed; approve/kill/reroute/truncate blocked | required |

## Commands

Run focused test:

```bash
cd EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME
npx vitest run tests/observe.only.signal.contract.test.ts --config vitest.config.ts
```

Run package check:

```bash
cd EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME
npm run check
```

Run repository governance checks before commit and push:

```bash
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

## Evidence

Required evidence at closure:

- focused vitest result for `tests/observe.only.signal.contract.test.ts`;
- full package `npm run check`;
- governance pre-push chain result;
- closure note preserving the observe-only claim boundary.

## Live Proof Position

No live provider proof is required for this tranche because the claim is
deterministic local observe-only signal behavior.

Any future claim that observability enforces provider routing, live governance,
dashboard streaming, or process control requires a fresh GC-018 and live proof.

## Claim Boundary

Passing this plan proves observe-only runtime behavior. It does not prove live
provider enforcement or operating-system process control.
