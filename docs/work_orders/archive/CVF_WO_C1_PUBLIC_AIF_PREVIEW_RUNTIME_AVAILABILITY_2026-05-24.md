# CVF Work Order — C1 Public AIF Preview Runtime Availability

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

Date: 2026-05-24

## Purpose

Make the Post-AIF AIF operational context preview harness publicly available
in the public-sync code subset while preserving the summary-only boundary.

## Authority Chain

- Operator instruction: 2026-05-24 claim blockers should be completed where
  possible and otherwise moved to a new tranche.
- GC-018:
  `docs/baselines/CVF_GC018_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_2026-05-24.md`
- Roadmap:
  `docs/roadmaps/CVF_POST_AIF_CLAIM_GRADUATION_ROADMAP_2026-05-24.md`

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Select the claim that can close without route/provider/ops changes. |
| Governance Reviewer | Preserve public repo boundary and no-overclaim language. |
| Implementer | Publish public-sync LPF preview harness and minimal dependencies. |
| QA | Run targeted, TypeScript, and full LPF verification. |
| Release Manager | Commit public-sync and record provenance closure. |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/CVF_POST_AIF_OPERATIONAL_READINESS_MATRIX_2026-05-24.md`
- `docs/roadmaps/CVF_POST_AIF_OPERATIONALIZATION_ROADMAP_2026-05-24.md`

## Pre-Flight Checks

- Confirm provenance worktree is clean before cross-repo work.
- Confirm public-sync remote points to
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`.
- Confirm no raw API keys are printed or copied.

## Scope / Target / Owner Boundary

In scope:

- `aif-operational-context-preview.ts`
- `memory-retrieval-policy.ts`
- `memory-context-packager.ts`
- minimal graph schema/index/parser dependencies
- `aif-operational-context-preview.test.ts`
- LPF barrel exports
- public-safe catalog/evidence update

Out of scope:

- live `/api/execute` route changes;
- provider dispatch changes;
- graph approval authority;
- hosted/production readiness.

## Write Ownership

Public-sync files only for implementation. Provenance files only for closure
records and session pointers.

## Execution Plan

1. Create public-sync graph dependency directories.
2. Publish the bounded preview harness and dependency files.
3. Export the public LPF surface.
4. Run targeted preview test, TypeScript check, and full LPF test suite.
5. Update public catalog/evidence.
6. Commit public-sync.
7. Record C1 closure in provenance.

## Acceptance Criteria

- [x] Public-sync remote points to the public repository.
- [x] Preview harness and minimal dependencies exist in public-sync.
- [x] LPF barrel exports the preview surface.
- [x] Targeted preview test passes.
- [x] Public-sync LPF TypeScript check passes.
- [x] Full public-sync LPF suite passes.
- [x] Public-safe catalog/evidence boundary is updated.
- [x] Public-sync commit is created.

## Evidence Requirements

- Public-sync targeted preview test: PASS.
- Public-sync LPF `npm run check`: PASS.
- Public-sync LPF full `npm test`: PASS.
- Public-sync commit exists.
- Public evidence keeps no-reinjection/no-authority/no-production boundary.

## Review Gate

PASS.

## Closure Checklist

- [x] Public-sync remote checked.
- [x] Public harness implemented.
- [x] Targeted test passed.
- [x] TypeScript check passed.
- [x] Full LPF suite passed.
- [x] Public-sync committed.
- [x] Provenance closure packet filed.

## Return-To-Orchestrator Conditions

Return if public-sync has unrelated dirty work, if tests fail, or if route
integration is required.

## Operator Checkpoint

Completed under the operator's broad instruction to finish feasible claim
conditions and move the rest to a new tranche.

## Decision / Recommendation / Disposition

Disposition: CLOSED_PASS.

## Claim Boundary

C1 supports public runtime availability for the local, summary-only AIF preview
harness. It does not support live memory reinjection, graph authority, broad
provider stability, hosted readiness, production readiness, or freeze release.
