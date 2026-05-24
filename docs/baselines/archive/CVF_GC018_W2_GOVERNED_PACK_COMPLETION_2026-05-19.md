# CVF GC-018 — W2: Governed-Pack Completion

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-19

Authority: Orchestrator role (Claude), 2026-05-19.

Roadmap authority: `docs/roadmaps/CVF_PHASE3_REVIEW_CLOSURE_ROADMAP_V2_2026-05-19.md`

## Purpose

Authorize Worker implementation of W2: completing the 3 existing governed packs
(`strategy_analysis`, `documentation`, `app_builder_complete`) by adding the
missing `failure-recovery.ts` to each pack and creating a typed TypeScript
registry (`WorkflowPackRegistry` interface + `getGovernedPack(templateId)` loader
in `governed-packs/index.ts`).

This baseline records the authorized scope, pre-scan inventory, invariants, and
done criteria before any code is written.

## Scope / Target / Owner Boundary

In scope:

- `cvf-web/src/types/workflow-pack.ts` — new TypeScript type file
- `cvf-web/src/lib/governed-packs/*/failure-recovery.ts` — 3 new files, one per pack
- `cvf-web/src/lib/governed-packs/index.ts` — typed registry + loader
- `cvf-web/src/lib/governed-packs/index.test.ts` — test file

Out of scope:

- Existing `execution.policy.json`, `receipt.schema.json`, `workflow.spec.md` (read-only)
- Route or enforcement surface changes
- Provider runtime semantics
- Public-sync edits

Owner: Orchestrator (Claude) authorized; Worker (Codex) implements.

## Source / Predecessor Evidence

Predecessor: `docs/roadmaps/CVF_PHASE3_REVIEW_CLOSURE_ROADMAP_V2_2026-05-19.md` — W2 section authorized after Codex no-blocking verdict.

Current HEAD at baseline filing: `4b1f8219`

Pre-scan confirms:

- 9 existing JSON/MD pack artifacts (3 per pack directory) — all present
- 0 TypeScript governance files in `governed-packs/` — true gap confirmed

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED — new TypeScript governance artifact class (`WorkflowPackRegistry`, `FailureRecoveryPolicy`) justified by true gap. Pattern is bounded, no enforcement surface change, no runtime behavior change.

Proposed tranche: W2 single-slice delivery — `failure-recovery.ts` x3 + `index.ts` registry + `workflow-pack.ts` types + `index.test.ts`.

## Evidence / Verification

Pre-implementation evidence:

- Directory listing confirms 3 pack subdirs, 9 JSON/MD artifacts, 0 TS files
- `npm run build` PASS at baseline (no pre-existing type errors)

Post-implementation evidence required:

- `npm run build` PASS after changes
- `npm run test:run -- src/lib/governed-packs/index.test.ts` PASS
- `git diff --name-only` shows no changes to `.json` or `.spec.md` files

## What Already Exists (Pre-Scan)

Confirmed present in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`:

- `app_builder_complete/execution.policy.json` — EXISTS, do NOT modify
- `app_builder_complete/receipt.schema.json` — EXISTS, do NOT modify
- `app_builder_complete/workflow.spec.md` — EXISTS, do NOT modify
- `documentation/execution.policy.json` — EXISTS, do NOT modify
- `documentation/receipt.schema.json` — EXISTS, do NOT modify
- `documentation/workflow.spec.md` — EXISTS, do NOT modify
- `strategy_analysis/execution.policy.json` — EXISTS, do NOT modify
- `strategy_analysis/receipt.schema.json` — EXISTS, do NOT modify
- `strategy_analysis/workflow.spec.md` — EXISTS, do NOT modify

Confirmed missing (true gap):

- `failure-recovery.ts` in any of the 3 pack directories — MISSING
- `governed-packs/index.ts` — MISSING
- `WorkflowPackRegistry` type anywhere in cvf-web — MISSING
- `FailureRecoveryPolicy` type anywhere in cvf-web — MISSING

## Authorized Scope

Files Worker may CREATE:

- `cvf-web/src/types/workflow-pack.ts` — new type file (≤ 60 lines)
- `cvf-web/src/lib/governed-packs/strategy_analysis/failure-recovery.ts` (≤ 50 lines)
- `cvf-web/src/lib/governed-packs/documentation/failure-recovery.ts` (≤ 50 lines)
- `cvf-web/src/lib/governed-packs/app_builder_complete/failure-recovery.ts` (≤ 50 lines)
- `cvf-web/src/lib/governed-packs/index.ts` — registry + loader (≤ 80 lines)
- `cvf-web/src/lib/governed-packs/index.test.ts` — test file (≤ 100 lines)

Files Worker must NOT touch:

- Any existing `execution.policy.json`, `receipt.schema.json`, `workflow.spec.md`
- `src/app/api/execute/route.ts` — no route change authorized
- `src/lib/execute-role-resolver.ts` — no enforcement surface change
- `llm.adapter.interface.ts` — blocked by `new_provider_execution_semantics`
- Any file outside `cvf-web/src/lib/governed-packs/` and `cvf-web/src/types/`

## Key Invariants

- Existing JSON/MD pack artifacts are read-only under this baseline
- `getGovernedPack(templateId)` must return `undefined` for unknown IDs, not throw
- `FailureRecoveryPolicy.recoverySteps` must be a non-empty array
- No circular imports: `index.ts` imports from pack subdirs, pack subdirs do NOT import from `index.ts`
- `WorkflowPackRegistry` is a metadata type only — no runtime execution logic

## Done Criteria

- [ ] `cvf-web/src/types/workflow-pack.ts` created (≤ 60 lines) with `WorkflowPackRef`, `WorkflowPackRegistry`, `FailureRecoveryPolicy` interfaces
- [ ] 3 `failure-recovery.ts` files created (≤ 50 lines each) with `packId`, `recoverySteps[]`, `escalationPath`
- [ ] `governed-packs/index.ts` exports `getGovernedPack(templateId)` and all 3 pack failure-recovery policies (≤ 80 lines)
- [ ] `governed-packs/index.test.ts` covers: pack lookup by ID, unknown ID returns undefined, all 3 packs present, failure recovery shape valid (≤ 100 lines)
- [ ] `npm run build` PASS — type changes propagate cleanly
- [ ] `npm run test:run -- src/lib/governed-packs/index.test.ts` PASS
- [ ] Existing JSON/MD artifacts confirmed unmodified (git diff shows no changes to those files)

## Claim Boundary

W2 authorizes TypeScript governance artifact completion only. It does not
authorize route changes, execute-path enforcement changes, provider runtime
semantics, new template creation, or public-sync edits.
