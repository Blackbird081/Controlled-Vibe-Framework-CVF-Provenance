# Work Order — Residual D1: Provider Method Contract Residual Decision

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (Candidate D1, corrected after rebuttal)
- `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (Codex verdict: NON_BLOCKING_WITH_GATE_UPDATE)
- `docs/reviews/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md` (W1 closed)
- `docs/reviews/CVF_LANE_D_PROVIDER_METHOD_PARITY_COMPLETION_2026-05-19.md` (D2 closed)

Prerequisite update (Codex rebuttal 2026-05-19): original prerequisite cited
CDH Candidate D rebuttal. That requirement is superseded — W1 and D2 delta
evidence is already closed. D1 proceeds directly against completed evidence.

---

## Purpose

Decide, per residual method, whether `retry()`, `cost()`, and `risk()` belong
at the method-contract layer (alongside the 8 existing gateway contracts) or
at the policy/routing layer (where `quickRiskScore` and routing policy already
live). Record the decision in a GC-018 baseline. Execute the chosen path for
each method: either author a contract file or write an explicit rejection with
the existing coverage citation.

---

## Scope / Target / Owner Boundary

In scope:

- One GC-018 baseline with per-method analysis for `retry`, `cost`, `risk`.
- Zero to three new contract files under
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/` (depending on per-method outcome).
- Zero to three new test files (one per contract, if contract-closure chosen).
- One closure review recording all three decisions.

Out of scope:

- Changes to `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
  (forbidden — still inside the `new_provider_execution_semantics` blocked work class).
- New provider execution semantics.
- Changes to existing contract files.
- Changes to pack policy files.
- Network provider calls.

Constraint: rejection outcomes must name the EXISTING surface that already
covers the semantic, so future agents do not re-open the ask.

---

## Per-Method Analysis Required in GC-018

### `retry()`

Question: is retry a per-method-call surface (provider-level) or a
routing-policy surface (gateway-level)?

Evidence to consider:

- Does any existing file under `EXTENSIONS/CVF_MODEL_GATEWAY/src/` define
  retry behavior? If yes, name it.
- Does the existing CLI `evaluate` command or any routing policy define retry
  semantics? If yes, name the file and the relevant field or function.

Acceptable outcomes:

- CONTRACT_CLOSURE: build `retry-contract.ts` under
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/`, 30–60 lines, parallel to the 8
  existing contracts.
- EXPLICIT_REJECTION: name the existing surface that owns retry semantics
  and state why a separate contract file would duplicate it.

### `cost()`

Question: is cost a per-method-call surface or a risk/policy surface?

Evidence to consider:

- The existing CLI `evaluate` command includes a `quickRiskScore` that
  includes amount thresholds. Does this constitute a cost-equivalent surface
  for risk policy?
- Does any existing gateway contract file carry cost or quota semantics?

Acceptable outcomes:

- CONTRACT_CLOSURE: build `cost-contract.ts`, 30–60 lines.
- EXPLICIT_REJECTION: cite `quickRiskScore` or the relevant routing-policy
  surface as the existing coverage.

### `risk()`

Question: is risk a per-method-call surface or an audit/evaluation surface?

Evidence to consider:

- Risk classification already exists in the `evaluate` command and in the
  audit event taxonomy.
- Does any existing gateway contract file carry risk classification semantics?

Acceptable outcomes:

- CONTRACT_CLOSURE: build `risk-contract.ts`, 30–60 lines.
- EXPLICIT_REJECTION: cite the existing `evaluate`/risk-classification surface.

---

## Deliverables

### Step D1.1 — GC-018 Baseline

File: `docs/baselines/CVF_GC018_D1_PROVIDER_METHOD_CONTRACT_RESIDUAL_2026-05-20.md`

Required sections: `## Status`, `## Source or Predecessor Evidence`,
`## Purpose / Decision / Baseline`, `## Scope or Proposed Tranche`,
`## Evidence / Required Evidence / Verification`, `## Claim Boundary`.

The baseline must contain the per-method analysis for all three methods with
explicit outcome chosen for each. The analysis must be concrete (file names,
function names, field names) — not narrative.

### Step D1.2 — Contract Files (contract-closure methods only)

For each method where CONTRACT_CLOSURE is chosen:

- File: `EXTENSIONS/CVF_MODEL_GATEWAY/src/<method>-contract.ts`
- Size: 30–60 lines (consistent with the 8 existing contracts)
- Must export a typed contract interface or class.
- Must NOT import from `llm.adapter.interface.ts`.
- Must NOT add provider execution logic.

### Step D1.3 — Test Files (contract-closure methods only)

For each new contract file:

- File: `EXTENSIONS/CVF_MODEL_GATEWAY/tests/<method>-contract.test.ts`
- Size: ≤60 lines, 4–5 tests.
- Tests verify contract shape and type safety; no live provider calls.

### Step D1.4 — Closure Review

File: `docs/reviews/CVF_D1_PROVIDER_METHOD_CONTRACT_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must:

- Record the per-method decision (CONTRACT_CLOSURE or EXPLICIT_REJECTION)
  for each of retry, cost, risk.
- For explicit rejections: name the existing surface that covers the semantic.
- Confirm `llm.adapter.interface.ts` was not changed.
- Confirm `npm test` PASS in `CVF_MODEL_GATEWAY`.
- Confirm `npm run check` PASS.
- Confirm pre-commit and pre-push hooks PASS.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] GC-018 baseline exists and is AUTHORIZED with explicit per-method analysis.
- [ ] Each of retry, cost, risk has a recorded outcome (CONTRACT_CLOSURE or
      EXPLICIT_REJECTION with citation).
- [ ] Any contract-closure method has a contract file (30–60 lines) and test
      file (≤60 lines, 4–5 tests), both PASS.
- [ ] `llm.adapter.interface.ts` is unchanged (verify with `git diff`).
- [ ] `npm test` PASS in `CVF_MODEL_GATEWAY`.
- [ ] `npm run check` PASS.
- [ ] Pre-commit and pre-push hooks PASS.
- [ ] Closure review filed with per-method decisions recorded.

---

## Forbidden Actions

- Do NOT change `llm.adapter.interface.ts` (blocked work class).
- Do NOT add provider execution semantics.
- Do NOT ship contract files for methods where EXPLICIT_REJECTION is chosen.
- Do NOT use narrative analysis — every decision must cite a specific file,
  function, or field name.
- Do NOT make provider API calls in tests.

---

## Authority Chain

- Authorized by: Codex rebuttal (D1: NON_BLOCKING_WITH_GATE_UPDATE); prerequisite updated to W1/D2 evidence 2026-05-20
- Roadmap: `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (REBUTTAL_ACCEPTED)
- Predecessors: `docs/reviews/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md` + `docs/reviews/CVF_LANE_D_PROVIDER_METHOD_PARITY_COMPLETION_2026-05-19.md`
- Orchestrator: Claude; Worker: Codex; Operator approval required for GC-018

---

## Agent Roles

- Worker (Codex): per-method analysis, GC-018, optional contract files and tests, closure review
- Orchestrator (Claude): reviews closure review

---

## Required First Reads

1. `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` — D1 scope and per-method analysis requirements
2. `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` — D1 verdict and gate update
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/` — all existing contract files (8 contracts)
4. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/` — `evaluate` command for `quickRiskScore` and cost/risk surfaces

---

## Pre-Flight Checks

- [ ] List all 8 existing contract files in `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
- [ ] Confirm `llm.adapter.interface.ts` is NOT to be modified (blocked work class)
- [ ] Confirm W1 and D2 closure reviews remain CLOSED
- [ ] Confirm `npm test` baseline PASS in `CVF_MODEL_GATEWAY`

---

## Write Ownership

May create or modify only:

- `docs/baselines/CVF_GC018_D1_PROVIDER_METHOD_CONTRACT_RESIDUAL_2026-05-20.md` (new)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/retry-contract.ts` (new, only if CONTRACT_CLOSURE)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/cost-contract.ts` (new, only if CONTRACT_CLOSURE)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/risk-contract.ts` (new, only if CONTRACT_CLOSURE)
- Corresponding test files in `EXTENSIONS/CVF_MODEL_GATEWAY/tests/` (only for contract-closure methods)
- `docs/reviews/CVF_D1_PROVIDER_METHOD_CONTRACT_CLOSURE_REVIEW_2026-05-20.md` (new)

`llm.adapter.interface.ts` must NOT be touched under any circumstances.

---

## Execution Plan

1. File GC-018 baseline with per-method analysis for retry, cost, risk (Step D1.1) — AUTHORIZED before any contract file
2. Author contract files for contract-closure methods only (Step D1.2)
3. Author test files for each new contract file (Step D1.3)
4. File closure review recording all three decisions (Step D1.4)

---

## Evidence Requirements

- GC-018 AUTHORIZED with explicit per-method outcome (CONTRACT_CLOSURE or EXPLICIT_REJECTION with citation)
- Zero to three contract files depending on outcome (each 30–60 lines)
- Zero to three test files (each ≤60 lines, 4–5 tests)
- `npm test` PASS, `npm run check` PASS in `CVF_MODEL_GATEWAY`
- Closure review with per-method decisions recorded

---

## Review Gate

Stop and return to Orchestrator if:

- Any method's analysis is ambiguous and cannot reach a clear outcome
- Contract-closure would require importing from `llm.adapter.interface.ts`

---

## Closure Checklist

- [ ] GC-018 AUTHORIZED with explicit per-method analysis
- [ ] Each of retry/cost/risk has a recorded outcome
- [ ] Contract files authored only for CONTRACT_CLOSURE methods
- [ ] Test files authored for each new contract
- [ ] `llm.adapter.interface.ts` unchanged
- [ ] `npm test` PASS, `npm run check` PASS
- [ ] Pre-commit and pre-push hooks PASS
- [ ] Closure review filed

---

## Return-To-Orchestrator Conditions

Return if: per-method analysis is ambiguous; contract-closure would require blocked imports; hook failure outside this scope.

---

## Claim Boundary

This work order covers the per-method decision baseline + zero to three contract
files + zero to three test files + closure review only. It does not extend to
CDH Candidate D scope, new provider execution semantics, or any runtime changes.
