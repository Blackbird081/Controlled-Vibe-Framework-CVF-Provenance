# CVF GC-018 Fast Lane — CBP-1 Context Budget Policy

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent: LHW18 T3 `cvf.contextManagementStrategyAdvisory.lhw18.t3.v1` (MACHINE_CHECK_CANDIDATE)

---

## Purpose

Authorize CBP-1: a bounded implementation tranche that promotes the Context Budget Guard
from `MACHINE_CHECK_CANDIDATE` (LHW18 T3) to a governed policy module + advisory readout.
Adds `context-budget-policy.ts` to `CVF_LEARNING_PLANE_FOUNDATION` defining `tokenBudget`
defaults per CVFRole task class, and exposes `contextBudgetReadout` as an additive advisory
field in `/api/execute` ALLOW response — identical pattern to EL-2/EL-3.

## Scope / Target / Owner Boundary

Target: `cvf.contextBudgetPolicy.cbp1.v1`
Owner: `CVF_LEARNING_PLANE_FOUNDATION` (policy module) + `/api/execute` (readout field).
Boundary: additive only; no existing behavior changed; no route.ts logic altered;
`runtimeExecutionAuthorized=false` for enforcement — readout is advisory.

## Source / Predecessor Evidence

- LHW18 T3 advisory: `docs/reference/CVF_LHW18_T3_CONTEXT_MANAGEMENT_STRATEGY_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
- Existing: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` — `tokenBudget` param already accepted; `tokenBudgetExceeded` already tracked
- Existing: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/aif-operational-context-preview.ts` — passes `input.tokenBudget` to packager; no default policy
- Pattern reference: EL-2 `worker-timeout-handler.ts` + EL-3 `reviewer-deadlock-handler.ts`

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED as Fast Lane R1 tranche (additive policy module + advisory readout).

Proposed deliverables:
1. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-policy.ts` — exports `getContextBudget(role: CVFRole, taskClass: ContextTaskClass): number` with default budgets per task class
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/context-budget-readout.ts` — `buildContextBudgetReadout()` additive advisory
3. `route.ts` +1 field `contextBudgetReadout` on ALLOW path (additive, same as `workerTimeoutReadout`)
4. Unit tests: `route.context-budget-readout.test.ts` (≥6 tests)

## Evidence / Verification

- `context-budget-policy.ts` exports at least 4 task classes with default budgets
- `buildContextBudgetReadout()` returns advisory readout with `taskClass`, `budgetTokens`, `withinBudget`, `advisoryNote`
- route.ts line count stays ≤ 1000 after adding field
- Unit tests PASS
- TypeScript PASS
- Live receipt with `contextBudgetReadout` present in response

## Claim Boundary

`runtimeExecutionAuthorized=false` — readout is advisory only. No enforcement that blocks
execution when budget is exceeded. No persistent context state. No new memory tier.
No route logic change beyond additive field. Route.ts hard limit 1000 lines.

## Fast Lane Risk Assessment

Risk class: R1 (additive advisory field; no behavior change; no security boundary crossed).
Fast Lane authorized: YES — same pattern as EL-2/EL-3 which passed without issues.
