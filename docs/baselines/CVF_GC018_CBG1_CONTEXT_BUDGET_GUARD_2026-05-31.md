# CVF GC-018 Continuation Candidate
## CBG-1 — Context Budget Guard

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent advisory: LHW18 T3 `cvf.contextManagementStrategyAdvisory.lhw18.t3.v1` (P2 MACHINE_CHECK_CANDIDATE)

---

## Purpose

Authorize CBG-1: implement the Context Budget Guard as a governed enforcement
function in `CVF_LEARNING_PLANE_FOUNDATION`. This closes the MACHINE_CHECK_CANDIDATE
gap from LHW18 T3 P2 — the advisory identified that no explicit token budget
enforcement existed; this tranche adds it.

## Scope / Target / Owner Boundary

Target: new `src/context-budget-guard.ts` in `CVF_LEARNING_PLANE_FOUNDATION`.
Owner: CVF learning plane / context management surface.
Boundary:
- New file only — no changes to `src/index.ts`, `route.ts`, or `memory-context-packager.ts`
- Export `checkContextBudgetGuard()` and `ContextBudgetGuardResult` from the new file
- Add export re-export line in `src/index.ts` (one line)
- Add tests to `tests/index.test.ts`
- No receipt-envelope extension, no route.ts change, no provider call change

## Source / Predecessor Evidence

- LHW18 T3 spec: `docs/reference/archive/CVF_LHW18_T3_CONTEXT_MANAGEMENT_STRATEGY_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` (P2 advisory, line 87-93)
- CBP-1: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-policy.ts` (policy + resolveTaskClass)
- Packager: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` (tokenBudgetExceeded flag exists but not enforced)

---

## GC-018 Continuation Candidate

- Candidate ID: `gc018-cbg1-context-budget-guard-2026-05-31`
- Date: 2026-05-31
- Parent: LHW18 T3 P2 MACHINE_CHECK_CANDIDATE
- Proposed scope: `checkContextBudgetGuard()` enforcement function + tests
- Continuation class: IMPLEMENTATION
- Quality-first decision: EXPAND_NOW — closes a documented machine-check gap; bounded to one new file
- Active-path impact: ADDITIVE — new export only
- Expected enforcement class: MACHINE_CHECK

### Depth Audit

- Risk reduction: 2 — closes the only enforcement gap in context budget surface
- Decision value: 2 — enables callers to enforce budget rather than silently overflow
- Machine enforceability: 2 — typed result with PASS/ESCALATE disposition
- Operational efficiency: 2 — one new file, re-uses existing policy constants
- Portfolio priority: 2 — MACHINE_CHECK_CANDIDATE from LHW18 T3 explicitly
- Total: 10/10
- Decision: **CONTINUE**

### Authorization Boundary

- Authorized now: **YES**
- Contract: `cvf.contextBudgetGuard.cbg1.v1`
- Hard invariants: no route.ts change; no receipt-envelope extension; no provider change; `runtimeExecutionAuthorized` advisory field preserved; escalation is advisory signal only (does not auto-block execution)

---

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.
Baseline: CBG-1 Context Budget Guard.

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-guard.ts` — new file
- Export re-export in `src/index.ts` — one line addition
- Tests in `tests/index.test.ts`
- Fast Lane audit + completion review

## Evidence / Verification

- New file: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-guard.ts` — DELIVERED
- Tests: `tests/index.test.ts` CBG-1 section — 14 tests, 1595/1595 PASS
- Fast Lane audit: `docs/reviews/CVF_CBG1_CONTEXT_BUDGET_GUARD_FAST_LANE_2026-05-31.md` — PASS
- Completion review: `docs/reviews/CVF_CBG1_CONTEXT_BUDGET_GUARD_COMPLETION_2026-05-31.md` — CLOSED_PASS_BOUNDED

## Claim Boundary

This GC-018 authorizes a bounded enforcement function only. No context engine,
no route.ts change, no receipt-envelope extension, no public release readiness claim.

---

*Authorized: 2026-05-31 | Operator sign-off in-session*
