# CVF CBG-1 — Context Budget Guard Completion

Memory class: COMPLETION_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.contextBudgetGuard.cbg1.v1`

GC-018: `docs/baselines/CVF_GC018_CBG1_CONTEXT_BUDGET_GUARD_2026-05-31.md`

Fast Lane: `docs/reviews/CVF_CBG1_CONTEXT_BUDGET_GUARD_FAST_LANE_2026-05-31.md`

---

## Purpose

Record completion of CBG-1 Context Budget Guard. Closes MACHINE_CHECK_CANDIDATE
from LHW18 T3 P2 (Context Budget Boundary advisory). Adds typed enforcement
function `checkContextBudgetGuard()` to `CVF_LEARNING_PLANE_FOUNDATION`.

## Scope / Target / Owner Boundary

Target: `cvf.contextBudgetGuard.cbg1.v1`.
Owner: CVF learning plane / context management surface.
Boundary: new file only + one re-export line in index.ts. No route.ts change.

## Target / Source Under Review

- New: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-guard.ts`
- Modified: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` (+9 lines re-export)
- Tests: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/context-budget-guard.test.ts`
- GC-018: `docs/baselines/CVF_GC018_CBG1_CONTEXT_BUDGET_GUARD_2026-05-31.md`
- Fast Lane: `docs/reviews/CVF_CBG1_CONTEXT_BUDGET_GUARD_FAST_LANE_2026-05-31.md`

## Scope / Methodology

Fast Lane (R1). Additive enforcement function; tests in dedicated file. No route.ts change.

## Findings / Position

| Gate | Result |
| --- | --- |
| `checkContextBudgetGuard()` returns PASS within budget | PASS |
| `checkContextBudgetGuard()` returns ESCALATE over budget | PASS |
| `checkContextBudgetGuardForTaskClass()` direct task class variant | PASS |
| `escalationReason` null on PASS, non-null on ESCALATE | PASS |
| `runtimeExecutionAuthorized: false` on all results | PASS |
| TypeScript check: no errors | PASS |
| Tests: 1595/1595 PASS (65 test files) | PASS |
| GC-023 file sizes: all within limits | PASS |

## Risk / Corrective Action

No violations. ESCALATE wiring to human surface is advisory — deferred to future tranche.

## Deliverables

| Artifact | Status |
| --- | --- |
| `src/context-budget-guard.ts` — `checkContextBudgetGuard()` + `checkContextBudgetGuardForTaskClass()` | DELIVERED |
| `src/index.ts` — re-export of CBG-1 symbols | DELIVERED |
| `tests/index.test.ts` — 14 CBG-1 tests (12 checkContextBudgetGuard + 4 checkContextBudgetGuardForTaskClass) | DELIVERED |
| GC-018 baseline | DELIVERED |
| Fast Lane audit | DELIVERED |

## Test Evidence

Tests: **1595/1595 PASS** (all prior tests + 14 new CBG-1 tests).
TypeScript: PASS (tsc --noEmit, no errors).

## Behaviour Summary

`checkContextBudgetGuard(role, estimatedTokens)`:
- Resolves role → `ContextTaskClass` via `resolveTaskClass()` (from CBP-1)
- Compares `estimatedTokens` against `getContextBudget(taskClass).budgetTokens`
- Returns `ContextBudgetGuardResult` with:
  - `disposition: "PASS"` when within budget or estimate is 0
  - `disposition: "ESCALATE"` when over budget
  - `escalationReason` (null on PASS, human-readable on ESCALATE)
  - `runtimeExecutionAuthorized: false` always
- Does not block execution — ESCALATE is advisory signal only

## Invariants

- `runtimeExecutionAuthorized=false` on all results
- No route.ts change
- No receipt-envelope extension
- No provider call change
- ESCALATE disposition is advisory; caller is responsible for surfacing to human

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| LHW18 T3 P2 gap now closed | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | CBG-1 closes the gap | HANDLED |
| ESCALATE wiring to human surface | `RULE_GAP` | `DOCUMENTATION_ONLY_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Future tranche can wire ESCALATE into route response or UI surface | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A | No runtime execution, no provider call, no cost impact in this tranche | N/A |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY` — CBG-1 is a private provenance implementation tranche.
Public export eligible after public-sync connector spec is authored if needed.

## Claim Boundary

CBG-1 adds a typed machine check for context budget enforcement. It does not
claim production enforcement, execution blocking, provider behavior, hosted
readiness, or public release readiness.
