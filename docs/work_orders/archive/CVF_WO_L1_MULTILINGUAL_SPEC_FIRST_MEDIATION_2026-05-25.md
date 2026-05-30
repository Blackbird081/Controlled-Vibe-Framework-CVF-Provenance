# CVF Work Order - L1 Multilingual Spec-First Mediation

Memory class: WORK_ORDER

Date: 2026-05-25

Status: DISPATCHED

## Authorization

GC-018:

`docs/baselines/CVF_GC018_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_2026-05-25.md`

Roadmap:

`docs/roadmaps/CVF_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_ROADMAP_2026-05-25.md`

## Purpose

Dispatch the first L1 remediation tranche so CVF can turn non-coder intent,
templates, skills, advisory LLM drafts, and language metadata into one
standard agent-readable CVF Execution Spec.

## Authority Chain

- Operator request: proceed with workflow/templates/skills/specs after the
  non-coder language/spec-first diagnosis.
- Result blocker:
  `docs/reviews/CVF_REAL_NONCODER_USAGE_TEST_RESULT_2026-05-25.md`
- GC-018:
  `docs/baselines/CVF_GC018_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_2026-05-25.md`
- Roadmap:
  `docs/roadmaps/CVF_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_ROADMAP_2026-05-25.md`

## Agent Roles

- Implementer: add the smallest deterministic compiler/readout.
- Reviewer: check that the prior operator sample is not relabeled PASS.
- Product/Operator Advocate: keep the Spec useful for Vietnamese/non-coder
  handoff.
- Safety/Boundary Owner: ensure advisory LLM output and external skills do not
  become implementation authority.

## Task

Implement the first bounded L1 foundation:

1. Build a deterministic CVF Execution Spec compiler/readout.
2. Support the four web-facing entry modes:
   - Template-First;
   - Describe Your Goal;
   - AI-Assisted Prompt Preparation;
   - User-Paid Provider Advisory Lane.
3. Preserve original user prompt and language metadata.
4. Prefer English working language when source language is Vietnamese while
   keeping user-facing summary localized.
5. Record user-paid provider/model advisory usage as source material only.
6. Wire an additive readout into `/api/execute`.
7. Add targeted unit and route tests.

## Allowed / Forbidden Scope

Allowed:

- deterministic Spec-first readout;
- reuse existing templates, recommender, spec gate, and skill-template map;
- additive `/api/execute` response field;
- targeted tests and docs.

Forbidden:

This work order does not authorize:

- external skill import;
- new certified skill packs;
- live external repo fetching;
- provider adapter changes;
- receipt envelope breaking changes;
- broad prompt tuning;
- hosted readiness;
- public readiness;
- tool, MCP, browser, database, CLI, or spend execution.

## Required First Reads

- `docs/reviews/CVF_REAL_NONCODER_USAGE_TEST_RESULT_2026-05-25.md`
- `docs/roadmaps/CVF_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_ROADMAP_2026-05-25.md`
- `docs/reference/CVF_NONCODER_SPEC_FIRST_WEB_FLOW_2026-05-25.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

## Pre-Flight Checks

- Confirm current worktree state before editing.
- Confirm existing template/spec/skill surfaces before adding new concepts.
- Confirm no live proof is claimed by deterministic tests.

## Write Ownership

Primary write surfaces:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `docs/baselines/`, `docs/work_orders/`, `docs/reviews/`

No public-sync writes are authorized.

## Execution Plan

1. Add `spec-first-mediation` library.
2. Add unit coverage for four entry modes.
3. Wire route response additively.
4. Add route-level assertion.
5. Run targeted tests and type check.
6. File completion and update session memory/handoff.

## Evidence Requirements

- Targeted test command and PASS count.
- Type-check command and PASS.
- Completion packet with claim boundary.

## Acceptance Criteria

- All four entry modes produce the same standard Spec sections.
- Vietnamese input can produce Vietnamese output metadata and English working
  language.
- Original prompt is preserved.
- Advisory provider/model usage is recorded as source-only.
- Route response exposes `specFirstMediation`.

## Review Gate

Reviewer must reject the tranche if it:

- imports external skills directly;
- treats advisory LLM output as implementation authorization;
- changes provider adapters or receipt envelopes;
- claims the prior real non-coder sample is now PASS without a new operator
  review.

## Return-To-Orchestrator Conditions

Return blocked if targeted tests or `npm run check` fail, or if file-size
guards require a broader refactor outside this work order.

## Operator Checkpoint

No mid-tranche operator checkpoint is required. Operator review resumes after
the bounded foundation is committed.

## Required Verification

- `npm run test:run -- src/lib/spec-first-mediation.test.ts src/app/api/execute/route.test.ts`
- `npm run check`

Live proof is not required for this T1 deterministic foundation unless the
implementation claims live governance behavior beyond the existing route path.

## Claim Boundary

This work order can close only the deterministic T1 foundation. It cannot close
the full real non-coder usage PASS gate, hosted readiness, public readiness, or
external skill absorption.

## Completion Requirements

Before closure:

- update the active session memory and handoff;
- record whether Real Non-Coder Usage Test remains HOLD or can move to a new
  operator review packet;
- commit changes with a clear bounded message.
