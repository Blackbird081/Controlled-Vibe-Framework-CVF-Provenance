# Work Order — Residual H1: Memory Tier Gate Decision

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (Candidate H1, corrected after rebuttal)
- `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (Codex verdict: NON_BLOCKING_WITH_GATE_UPDATE)
- `docs/reviews/CVF_RUNTIME_MATURITY_H2_AUDIT_MEMORY_COMPLETION_2026-05-19.md` (H2 closed)

Prerequisite update (Codex rebuttal 2026-05-19): original prerequisite cited
CDH Candidate H rebuttal. That requirement is superseded — H2 delta evidence
is already closed and covers audit memory policy refinement. H1 proceeds
directly against completed H2 evidence.

---

## Purpose

Choose exactly one architectural path for the memory tier gate contract layer
(five typed-per-tier contracts OR one classifier contract), ship the chosen
path, and record the rejected path with explicit rationale. Neither path
ships runtime data flow.

---

## Scope / Target / Owner Boundary

In scope:

- One GC-018 baseline that names the chosen path.
- Either: five new contract files under
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` (Path A), OR one new
  contract file (Path B).
- Test file(s) verifying tier-identity discrimination.
- One closure review recording the chosen path and the rejected-path rationale.

Out of scope:

- Runtime data flow wiring of any kind.
- Provider prompt reinjection.
- Organizational memory runtime.
- Changes to any existing file outside
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`.
- Memory retrieval, injection, or retention policy changes.
- Shipping both Path A and Path B (forbidden).

Constraint: the GC-018 baseline MUST name exactly one path. If Codex cannot
determine which path to choose during the baseline phase, it must hold and
report to the Orchestrator before proceeding.

---

## Path Options

### Path A — Typed-Per-Tier (5 contract files)

Five new files under `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`:

- `working-memory-tier.contract.ts`
- `task-memory-tier.contract.ts`
- `skill-memory-tier.contract.ts`
- `organizational-memory-tier.contract.ts`
- `long-term-memory-tier.contract.ts`

Each contract must define:

```typescript
// Required fields per tier contract:
//   tierIdentity: string literal type (e.g., "working")
//   retentionSemantic: description of how long content persists
//   injectionPermit: which actor roles may inject into this tier
//   retrievalPermit: which actor roles may retrieve from this tier
//   privacyScope: "session" | "user" | "org" | "global"
//   contaminationBoundary: what this tier must not bleed into
```

No runtime wiring — these are contract definitions only.

### Path B — Single Classifier (1 contract file)

One new file under `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`:

- `memory-tier-classifier.contract.ts`

Must define:

```typescript
// MemoryTier: discriminated union with values:
//   "working" | "task" | "skill" | "organizational" | "long-term"
//   | "audit" | "receipt"
// (audit and receipt are the existing tiers from H2)

// classifyMemoryTier(input: MemoryTierInput): MemoryTier
//   — pure classifier function; no side effects; no runtime I/O
```

No runtime wiring — the classifier is a contract definition and pure function
only.

---

## Path Selection Guidance

Codex should choose based on the following criteria:

- **Choose Path A** if the five tiers have meaningfully different
  retention, injection, retrieval, privacy, or contamination semantics
  that would be obscured by a single discriminated union.
- **Choose Path B** if the five tiers share the same contract shape and
  differ only in their identity label, making five separate files redundant.

The choice must be justified in the GC-018 baseline with reference to the
existing H2 implementation evidence.

---

## Deliverables

### Step H1.1 — GC-018 Baseline

File: `docs/baselines/CVF_GC018_H1_MEMORY_TIER_GATE_DECISION_2026-05-20.md`

Required sections: `## Status`, `## Source or Predecessor Evidence`,
`## Purpose / Decision / Baseline`, `## Scope or Proposed Tranche`,
`## Evidence / Required Evidence / Verification`, `## Claim Boundary`.

The baseline must:

- Name the chosen path (A or B) explicitly.
- Justify the choice with reference to H2 evidence.
- Name the rejected path and state the reason for rejection.
- Confirm no runtime wiring is claimed.
- Confirm both paths are not shipped simultaneously.

### Step H1.2 — Contract File(s)

**If Path A chosen:** five files as described above. Each file:
- 30–80 lines.
- Exports a typed contract interface or type alias.
- Contains a `// Claim Boundary:` comment block stating it is a contract
  definition only, not a runtime enforcement surface.

**If Path B chosen:** one file as described above.
- 40–100 lines.
- Exports `MemoryTier` discriminated union and `classifyMemoryTier` function.
- Function is pure (no I/O, no side effects).
- Contains a `// Claim Boundary:` comment block.

### Step H1.3 — Test File(s)

Verify tier-identity discrimination. Size within `test_code` governed threshold
(advisory 800 lines, hard 1000 lines).

**If Path A:** one test file `tests/memory-tier-contracts.test.ts`.

Minimum tests:
- Each of the 5 tier contracts has a test confirming its `tierIdentity`
  literal is the correct value.
- A test confirming each tier's `privacyScope` is set to one of the allowed
  values.
- Total: approximately 10–15 tests.

**If Path B:** one test file `tests/memory-tier-classifier.test.ts`.

Minimum tests:
- `classifyMemoryTier` returns the correct `MemoryTier` for each of the 7
  tier inputs (5 new + audit + receipt).
- `classifyMemoryTier` is a pure function: same input always returns same
  output (no side effects).
- Total: approximately 8–10 tests.

All tests: no live API calls, no I/O, pure function assertions only.

### Step H1.4 — Closure Review

File: `docs/reviews/CVF_H1_MEMORY_TIER_GATE_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must:

- State the chosen path (A or B) and the rejected path with rationale.
- Confirm no runtime wiring was introduced.
- Confirm test files pass.
- Confirm `npm test` PASS in `CVF_LEARNING_PLANE_FOUNDATION`.
- Confirm `npm run check` PASS (TypeScript type-check).
- Confirm pre-commit and pre-push hooks PASS.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] GC-018 baseline exists and is AUTHORIZED with explicit path choice and
      rejected-path rationale.
- [ ] Contract file(s) exist (5 files for Path A, 1 file for Path B).
- [ ] Test file(s) exist with minimum test counts, all PASS.
- [ ] No runtime wiring introduced (verify with `git diff` — no changes to
      existing runtime files).
- [ ] `npm test` PASS in `CVF_LEARNING_PLANE_FOUNDATION`.
- [ ] `npm run check` PASS.
- [ ] Pre-commit and pre-push hooks PASS.
- [ ] Closure review filed confirming chosen path, rejected path, and no
      runtime wiring.

---

## Forbidden Actions

- Do NOT ship both Path A and Path B.
- Do NOT wire any contract to a runtime data flow, provider, or injection
  pipeline.
- Do NOT claim organizational memory runtime.
- Do NOT change existing files outside `CVF_LEARNING_PLANE_FOUNDATION/`.
- Do NOT add live API calls to tests.
- Do NOT proceed if the path choice is unclear — hold and report to
  Orchestrator.

---

## Authority Chain

- Authorized by: Codex rebuttal (H1: NON_BLOCKING_WITH_GATE_UPDATE); prerequisite updated to H2 evidence 2026-05-20
- Roadmap: `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (REBUTTAL_ACCEPTED)
- Predecessor: `docs/reviews/CVF_RUNTIME_MATURITY_H2_AUDIT_MEMORY_COMPLETION_2026-05-19.md` (H2 CLOSED)
- Orchestrator: Claude; Worker: Codex; Operator approval required for GC-018

---

## Agent Roles

- Worker (Codex): path-choice analysis, GC-018, contract file(s), test file(s), closure review
- Orchestrator (Claude): reviews closure review; if path choice is unclear, Worker must return before GC-018

---

## Required First Reads

1. `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` — H1 scope and Path A/B options
2. `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` — H1 verdict and path-choice guards
3. `docs/reviews/CVF_RUNTIME_MATURITY_H2_AUDIT_MEMORY_COMPLETION_2026-05-19.md` — H2 evidence (audit + receipt tiers already done)
4. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` — existing learning plane contracts

---

## Pre-Flight Checks

- [ ] Confirm H2 closure review remains CLOSED
- [ ] List existing contract files in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` to understand current shape
- [ ] Confirm `npm test` baseline PASS in `CVF_LEARNING_PLANE_FOUNDATION`
- [ ] If path choice is unclear after reading evidence, return to Orchestrator before filing GC-018

---

## Write Ownership

May create only:

- `docs/baselines/CVF_GC018_H1_MEMORY_TIER_GATE_DECISION_2026-05-20.md` (new)
- If Path A: five contract files under `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`
- If Path B: one contract file under `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`
- Test file(s) under `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/`
- `docs/reviews/CVF_H1_MEMORY_TIER_GATE_CLOSURE_REVIEW_2026-05-20.md` (new)

May NOT ship both Path A and Path B files.

---

## Execution Plan

1. Analyze existing evidence to choose Path A or Path B (Step H1.1 analysis phase)
2. File GC-018 baseline naming the chosen path (Step H1.1) — AUTHORIZED before contract files
3. Author contract file(s) for chosen path (Step H1.2)
4. Author test file(s) (Step H1.3)
5. File closure review (Step H1.4)

---

## Evidence Requirements

- GC-018 AUTHORIZED with chosen path named and rejected path justified
- Contract file(s) exist (5 for Path A, 1 for Path B)
- Test file(s) with minimum 8–15 tests depending on path, all PASS
- No runtime wiring introduced
- `npm test` PASS, `npm run check` PASS in `CVF_LEARNING_PLANE_FOUNDATION`

---

## Review Gate

Stop and return to Orchestrator if:

- Path choice is ambiguous after reading H2 evidence
- Contract implementation would require runtime wiring or data flow changes

---

## Closure Checklist

- [ ] GC-018 AUTHORIZED with path choice and rejected-path rationale
- [ ] Contract file(s) at named paths (Path A: 5 files, Path B: 1 file)
- [ ] Test file(s) with required test counts, all PASS
- [ ] No runtime wiring introduced (verified via `git diff`)
- [ ] `npm test` PASS, `npm run check` PASS
- [ ] Pre-commit and pre-push hooks PASS
- [ ] Closure review filed with chosen path, rejected path, and no-wiring confirmation

---

## Return-To-Orchestrator Conditions

Return if: path choice is ambiguous; contract would require runtime wiring; hook failure outside this scope.

---

## Claim Boundary

This work order covers the path-choice baseline + contract file(s) + test
file(s) + closure review only. It does not authorize runtime memory wiring,
provider integration, retrieval or injection pipeline changes, or any work
outside `CVF_LEARNING_PLANE_FOUNDATION/`.
