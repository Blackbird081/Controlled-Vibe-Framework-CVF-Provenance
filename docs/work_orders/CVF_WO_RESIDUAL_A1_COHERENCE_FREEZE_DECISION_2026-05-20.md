# Work Order — Residual A1: Coherence Freeze Decision

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (Candidate A1, REBUTTAL_ACCEPTED)
- `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (Codex verdict: NON_BLOCKING)

---

## Purpose

Determine whether dedicated freeze documents (`CVF_KERNEL_LAW.md`,
`CVF_CORE_ONTOLOGY.md`, `CVF_RUNTIME_AUTHORITY_MODEL.md`,
`CVF_EXECUTION_STATE_MODEL.md`) add marginal coherence value on top of CVF's
existing 43-guard pre-push chain and review chain, then record the decision
and execute the chosen path.

This work order authorizes a bounded necessity audit followed by exactly one
of two closure actions. It does not pre-commit to either outcome.

---

## Scope / Target / Owner Boundary

In scope:

- A necessity audit document comparing the proposed four freeze files against
  specific guards and review-chain artifacts that already enforce the same
  semantics.
- One GC-018 baseline that authorizes the chosen outcome.
- Either: authoring four freeze files (contract-closure path), OR: a written
  justification that the guard chain already covers the ask
  (explicit-rejection path).

Out of scope:

- New L0–L5 layer creation.
- Changes to any guard implementation file.
- Runtime code changes.
- Promotion of `.private_reference/` material into canon.
- Any RBAC or role taxonomy changes.

Constraint: the four named files (`CVF_KERNEL_LAW.md`,
`CVF_CORE_ONTOLOGY.md`, `CVF_RUNTIME_AUTHORITY_MODEL.md`,
`CVF_EXECUTION_STATE_MODEL.md`) must NOT be authored before the necessity
audit is complete and the GC-018 baseline is AUTHORIZED.

---

## Deliverables

### Step A1.1 — Necessity Audit Document

File: `docs/reviews/CVF_A1_COHERENCE_FREEZE_NECESSITY_AUDIT_2026-05-20.md`

Required content:

1. List each of the four named files and the specific named guards or review-chain
   artifacts that currently enforce or document the same semantic. Be explicit:
   name the guard file, the rule it enforces, and whether it is runtime-checked
   (pre-commit / pre-push) or documentation-only.
2. For each of the four files, state whether the existing coverage is
   sufficient (explicit-rejection supported) or has a gap the named file would
   fill (contract-closure supported).
3. Conclude with one of:
   - `Outcome: CONTRACT_CLOSURE` — at least one of the four files adds
     non-duplicate value.
   - `Outcome: EXPLICIT_REJECTION` — all four files duplicate existing guard
     and review-chain coverage; the 17.05 ask is answered by guard chain.
4. If CONTRACT_CLOSURE: list which files to author and their proposed scope
   (200–400 lines each, frozen on completion).

Structure required (for structural completeness guard):

- `## Purpose`
- `## Source or Predecessor Evidence`
- `## Scope or Methodology`
- `## Findings or Position`
- `## Decision / Recommendation / Disposition`
- `## Claim Boundary`

### Step A1.2 — GC-018 Baseline

File: `docs/baselines/CVF_GC018_A1_COHERENCE_FREEZE_DECISION_2026-05-20.md`

Required sections: `## Status`, `## Source or Predecessor Evidence`,
`## Purpose / Decision / Baseline`, `## Scope or Proposed Tranche`,
`## Evidence / Required Evidence / Verification`, `## Claim Boundary`.

The baseline must:

- Reference the necessity audit from Step A1.1.
- Name the chosen outcome (CONTRACT_CLOSURE or EXPLICIT_REJECTION).
- If CONTRACT_CLOSURE: list the files to be authored, their proposed paths,
  and the size bound.
- If EXPLICIT_REJECTION: cite each guard by name and state what semantic it
  covers, so future agents do not re-open the ask.

### Step A1.3 — Contract-Closure Path Only (skip if EXPLICIT_REJECTION)

If the necessity audit concludes CONTRACT_CLOSURE, author the named files:

- `docs/reference/CVF_KERNEL_LAW.md` (200–400 lines, FROZEN on completion)
- `docs/reference/CVF_CORE_ONTOLOGY.md` (200–400 lines, FROZEN on completion)
- `docs/reference/CVF_RUNTIME_AUTHORITY_MODEL.md` (200–400 lines, FROZEN)
- `docs/reference/CVF_EXECUTION_STATE_MODEL.md` (200–400 lines, FROZEN)

Each file must:

- Carry `Memory class: FULL_RECORD`, `Status: FROZEN`, `docType: reference`.
- Contain `## Claim Boundary` or `## Final Clause` section.
- Not duplicate what any existing guard already enforces at runtime.

### Step A1.4 — Closure Review

File: `docs/reviews/CVF_A1_COHERENCE_FREEZE_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Review/Rebuttal/Response template (Purpose, Target,
Scope/Methodology, Findings, Decision/Disposition, Claim Boundary).

The closure review must confirm:

- Necessity audit completed and conclusion recorded.
- GC-018 authorized before any freeze files were authored.
- Chosen outcome (CONTRACT_CLOSURE or EXPLICIT_REJECTION) executed.
- If EXPLICIT_REJECTION: 17.05 Problem A marked answered-by-guard-chain in
  this review.
- Continuation chain guard Rule A: active GC-018 baseline reference present.
- Continuation chain guard Rule B: completion review present.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] Necessity audit document exists at the specified path with all required
      structural sections.
- [ ] GC-018 baseline exists and is AUTHORIZED (not merely filed).
- [ ] Chosen outcome is executed (freeze files authored OR explicit-rejection
      written with guard citations).
- [ ] Closure review confirms guard alignment and records the chosen outcome.
- [ ] `npm run lint` and `npm run build` remain PASS (no new files introduced
      that break the build).
- [ ] Pre-commit hook passes: structural completeness, file size, docs taxonomy.
- [ ] Pre-push hook passes: all 43 guards.

---

## Forbidden Actions

- Do NOT author any of the four named files before the GC-018 is AUTHORIZED.
- Do NOT create new L0–L5 layers.
- Do NOT change any guard implementation.
- Do NOT promote `.private_reference/` text directly; re-author in canonical form.
- Do NOT claim the freeze files are "runtime-enforced" — they are
  documentation artifacts, not executable contracts.

---

## Authority Chain

- Authorized by: Codex rebuttal `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (A1: NON_BLOCKING)
- Roadmap: `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (REBUTTAL_ACCEPTED)
- Orchestrator: Claude (dispatch role)
- Worker: Codex (implementer role)
- Operator approval required: Yes, for GC-018 baseline before any freeze files are authored

---

## Agent Roles

- Orchestrator (Claude): dispatches this work order; reviews closure review
- Worker (Codex): executes all steps; writes necessity audit, GC-018, optional freeze files, closure review
- Reviewer (Codex or Operator): approves GC-018 before freeze files are authored

---

## Required First Reads

1. `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` — Candidate A1 scope
2. `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` — A1 NON_BLOCKING verdict and downstream guard requirements
3. `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md` — Rule A/B enforcement surface
4. `governance/toolkit/05_OPERATION/` (scan the 43-guard chain to know what each guard already enforces)

---

## Pre-Flight Checks

Before authoring any file:

- [ ] Confirm none of the four named files exist anywhere in the working tree
- [ ] Confirm the GC-018 baseline is AUTHORIZED before any freeze file is written
- [ ] Confirm `npm run lint` and `npm run build` pass in cvf-web (baseline health)

---

## Write Ownership

The Worker may create or modify only:

- `docs/reviews/CVF_A1_COHERENCE_FREEZE_NECESSITY_AUDIT_2026-05-20.md` (new)
- `docs/baselines/CVF_GC018_A1_COHERENCE_FREEZE_DECISION_2026-05-20.md` (new)
- `docs/reference/CVF_KERNEL_LAW.md` (new, contract-closure path only)
- `docs/reference/CVF_CORE_ONTOLOGY.md` (new, contract-closure path only)
- `docs/reference/CVF_RUNTIME_AUTHORITY_MODEL.md` (new, contract-closure path only)
- `docs/reference/CVF_EXECUTION_STATE_MODEL.md` (new, contract-closure path only)
- `docs/reviews/CVF_A1_COHERENCE_FREEZE_CLOSURE_REVIEW_2026-05-20.md` (new)

No other files may be created or modified without explicit authorization.

---

## Execution Plan

See `## Deliverables` above for per-step details. Sequence:

1. Step A1.1 — necessity audit document
2. Step A1.2 — GC-018 baseline (must be AUTHORIZED before Step A1.3)
3. Step A1.3 — freeze files (contract-closure path only; skip if EXPLICIT_REJECTION)
4. Step A1.4 — closure review

---

## Evidence Requirements

- Necessity audit document confirming which guards cover which semantics
- GC-018 baseline with chosen outcome and justification
- If contract-closure: four freeze files at named paths, each FROZEN on completion
- Closure review confirming GC-018 authorized first, outcome executed, guard alignment confirmed

---

## Review Gate

The Worker must stop and return to Orchestrator before Step A1.3 if:

- The necessity audit cannot reach a clear verdict (CONTRACT_CLOSURE or EXPLICIT_REJECTION)
- Any of the four named files already exists in the working tree
- The GC-018 baseline is not yet AUTHORIZED

---

## Closure Checklist

- [ ] Necessity audit complete and verdict recorded
- [ ] GC-018 baseline AUTHORIZED
- [ ] Chosen outcome executed (freeze files OR explicit rejection with guard citations)
- [ ] Closure review filed
- [ ] All acceptance criteria satisfied
- [ ] Pre-commit and pre-push hooks PASS (11/11 and 43/43)

---

## Return-To-Orchestrator Conditions

Return immediately if:

- Necessity audit reaches ambiguous verdict and cannot choose CONTRACT_CLOSURE or EXPLICIT_REJECTION
- Any freeze file already exists (unexpected working-tree state)
- GC-018 cannot be AUTHORIZED (structural or policy violation)
- Pre-commit or pre-push hook fails for reasons outside this work order's scope

---

## Claim Boundary

This work order authorizes the necessity audit and one GC-018 baseline.
It does not authorize runtime changes, RBAC changes, public claim expansion,
or any work beyond the A1 scope defined here.

The closure review is the final deliverable. No further work on A1 may proceed
after the closure review is filed without a new work order.
