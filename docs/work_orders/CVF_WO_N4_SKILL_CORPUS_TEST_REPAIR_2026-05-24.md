# CVF Work Order: N4 Skill Corpus Test Repair

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-24

Tranche: N4

Roadmap: `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Fix 2 failing tests in `skill-corpus-governance.test.ts`. Root cause:
`loadSkillIndex()` calls `readFileSync(path.resolve(process.cwd(), 'public/data/skills-index.json'))`.
When vitest runs from the repo root (not from `cvf-web/`), `process.cwd()` is
`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` and the path
resolves to the wrong location — `skillIndex.categories` becomes `undefined`,
causing `Cannot read properties of undefined (reading 'flatMap')`.

---

## Authority Chain

Operator → Claude (roadmap author) → Codex (implementer).

Authorization: Fast Lane (GC-021). Pure bug fix — no runtime, provider,
governance semantic, or schema change.

---

## Agent Roles

- Codex: implementer — fixes the path resolution and verifies 4/4 tests pass
- Claude: reviewer — confirms test pass count and no regression
- Operator: pre-authorized under Fast Lane

---

## Required First Reads

Before implementing:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-corpus-governance.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/skill-corpus-governance.js`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` (check root/cwd setting)

---

## Pre-Flight Checks

1. Confirm current failure: `npx --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web vitest run src/lib/skill-corpus-governance.test.ts` → 2 failures
2. Confirm root cause: `process.cwd()` in `loadSkillIndex()` returns repo root, not `cvf-web/`
3. Check GC-023 line count for `skill-corpus-governance.test.ts` before editing

---

## Write Ownership

Codex owns:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-corpus-governance.test.ts` (fix path resolution)

No other files may be modified unless the regeneration script (`scripts/skill-corpus-governance.js`) also needs path fix — document that decision in the completion review.

---

## Execution Plan

1. Read `skill-corpus-governance.test.ts` fully — understand `loadSkillIndex()`
2. Read `vitest.config.ts` — check if `root` or `testDir` is set
3. Identify fix: either (a) use `path.resolve(__dirname, '../../public/data/skills-index.json')` in `loadSkillIndex()`, or (b) use vitest `root` config to set `cvf-web/` as cwd — choose the approach that doesn't break other tests
4. Apply fix
5. Run `npx --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web vitest run src/lib/skill-corpus-governance.test.ts` → confirm 4/4 PASS
6. Run full `cvf-web` test suite: `npx --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web vitest run` → confirm no regression (baseline: ~2747 pass)
7. Run TypeScript check: `npm run check --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
8. Update roadmap Progress Tracker N4 row → `CLOSED_PASS`
9. File completion review
10. Commit

---

## Evidence Requirements

- `skill-corpus-governance.test.ts` 4/4 PASS (screenshot or test output)
- Full `cvf-web` test suite: pass count ≥ pre-existing baseline
- TypeScript check PASS
- GC-023 compliant for modified file

---

## Scope / Target / Owner Boundary

In scope:

- `skill-corpus-governance.test.ts` path resolution fix
- `scripts/skill-corpus-governance.js` if it has the same path issue

Out of scope:

- No changes to `skills-index.json` content
- No changes to skill governance policy logic
- No new skill categories or templates
- No provider, receipt, or session state change

---

## Acceptance Criteria

- [ ] `skill-corpus-governance.test.ts` 4/4 PASS
- [ ] Full `cvf-web` test suite regression-clean (pass count ≥ baseline)
- [ ] TypeScript check PASS
- [ ] GC-023 compliant for modified files
- [ ] Roadmap Progress Tracker N4 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Review Gate

Claude reviews the completion package for:

- 4/4 tests passing in `skill-corpus-governance.test.ts`
- No regression in full `cvf-web` suite
- TypeScript check PASS
- Fix approach documented (why `__dirname` or vitest root config was chosen)

---

## Closure Checklist

- [ ] Root cause confirmed: `process.cwd()` mismatch
- [ ] Fix applied to `skill-corpus-governance.test.ts`
- [ ] 4/4 tests PASS
- [ ] Full `cvf-web` suite: no regression
- [ ] TypeScript check PASS
- [ ] GC-023 compliant
- [ ] Roadmap N4 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Return-To-Orchestrator Conditions

Return to Claude when:

- All closure checklist items above are complete
- OR: a blocker is encountered (e.g., fix breaks other tests, regeneration script also has the bug)

---

## Operator Checkpoint

operator.checkpoint.waiver: N4 is a pure test path-resolution bug fix with no
runtime, provider, governance semantic, or schema change — Fast Lane pre-authorized
under operator directive on 2026-05-24.

---

## Completion Review

After implementation, file at:
`docs/reviews/CVF_N4_SKILL_CORPUS_TEST_REPAIR_COMPLETION_2026-05-24.md`

Minimum sections: Purpose, Root Cause Confirmed, Fix Applied, Test Evidence (4/4 PASS), Regression Evidence, Claim Boundary.

---

## Claim Boundary

This work order authorizes only a test path-resolution fix in
`skill-corpus-governance.test.ts`. It does not authorize skill policy changes,
new skill categories, provider changes, runtime changes, or governance semantic
changes.
