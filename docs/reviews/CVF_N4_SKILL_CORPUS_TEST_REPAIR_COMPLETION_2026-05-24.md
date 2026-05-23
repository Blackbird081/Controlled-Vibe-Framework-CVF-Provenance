# CVF N4 Skill Corpus Test Repair Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS

Date: 2026-05-24

## Purpose

Close N4 after fixing the skill corpus public index path used by
`skill-corpus-governance.test.ts`.

## Target / Source

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-corpus-governance.test.ts`.

Source: `docs/work_orders/CVF_WO_N4_SKILL_CORPUS_TEST_REPAIR_2026-05-24.md`.

## Scope / Target / Owner Boundary

In scope: test path-resolution fix only.

Out of scope: skill index content, skill governance policy, provider behavior,
runtime behavior, or governance semantics.

## Scope / Methodology

Confirmed the failure, inspected the generator script and Vitest config, then
changed the test helper to resolve the public index relative to the test file.

## Findings / Position

Position: N4 is closed pass. The root cause was the `process.cwd()` mismatch.

## Risk / Corrective Action

Risk: a path fix could hide generator drift. Corrective action: no generator
change was made, and full `cvf-web` regression passed.

## Decision / Recommendation / Disposition

Disposition: CLOSED_PASS.

## Root Cause Confirmed

`loadSkillIndex()` resolved `public/data/skills-index.json` from
`process.cwd()`. When Vitest ran from the repository root, that pointed outside
`cvf-web`, so `skillIndex.categories` was undefined and 2/4 tests failed.

## Fix Applied

Changed the test helper to resolve from `__dirname`:

`../../public/data/skills-index.json`

The generation script already resolves from its own `BASE_DIR`, so no script
change was needed.

## Test Evidence

- Pre-fix targeted run: 2 failed / 2 passed, matching the work order root cause.
- Post-fix targeted run:
  `npx --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web vitest run src/lib/skill-corpus-governance.test.ts`
  - PASS: 1 file / 4 tests.
- Full `cvf-web` regression:
  `npm run test:run`
  - PASS: 221 files / 2753 passed / 2 skipped.
- `cvf-web` TypeScript:
  `npm run check`
  - PASS.

## GC-023

`skill-corpus-governance.test.ts` remains 84 lines.

## Claim Boundary

N4 changed only test path resolution. It does not change skill governance
policy, skill categories, provider behavior, runtime behavior, or governance
semantics.
