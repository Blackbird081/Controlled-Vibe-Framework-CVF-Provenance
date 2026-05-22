# CVF Work Order G1 Execution Identity Runtime Gate

Memory class: FULL_RECORD

Status: CLOSED_G1_EXECUTION_IDENTITY_RUNTIME_GATE

Date: 2026-05-22

## Purpose

Implement the G1 execution identity runtime gate authorized by GC-018.

## Authority Chain

- Original source oracle: `.private_reference/legacy/CVF 17.05/Review CVF.md`
- Post-B/C assessment:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- Roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- Rebuttal:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_ROADMAP_MULTI_ROLE_REBUTTAL_2026-05-22.md`
- GC-018:
  `docs/baselines/CVF_GC018_G1_EXECUTION_IDENTITY_RUNTIME_GATE_2026-05-22.md`

## Agent Roles

- Orchestrator: Codex
- Implementer: Codex
- Reviewer: Codex, via tests and completion review
- Auditor: Codex, via completion packet and governance hooks

## Scope / Allowed Scope / Forbidden Scope

Allowed:

- add small helper modules and tests under `cvf-web/src/lib`;
- update `/api/execute` to include execution identity decision in response and
  audit payloads;
- update route actor-gate tests.

Forbidden:

- new role taxonomy;
- auth/RBAC redesign;
- provider behavior changes;
- receipt-envelope mutation;
- memory hierarchy expansion;
- public-sync update;
- generated artifact commits.

## Required First Reads

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.actor-gate.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-permission-gate.ts`

## Pre-Flight Checks

- Confirm no new role taxonomy is needed.
- Confirm denied actor path returns before provider dispatch.
- Confirm receipt type is unchanged.

## Write Ownership

Primary write scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- focused route tests
- completion documentation

## Execution Plan / Execution Rules

1. Add execution identity helper.
2. Add helper tests for allowed, denied, and unknown actor cases.
3. Wire helper into `/api/execute` route.
4. Include identity decision in route response and audit payloads.
5. Update denied actor route test.
6. Verify targeted tests and TypeScript check.
7. File completion review.

## Evidence Requirements

- Targeted unit and route tests pass.
- `npm run check` passes.
- Local governance hook chain passes before final commit.

## Acceptance Criteria

- Allowed actor path includes execution identity readout.
- Denied actor path includes execution identity readout and does not call
  provider dispatch.
- Unknown actor path remains denied and has a deterministic identity decision.
- Audit payload includes execution identity.
- No receipt-envelope mutation.

## Review Gate

Completion review must state whether G1 is closed, partial, or failed, and
must include exact tests run.

## Closure Checklist / Completion Requirements

- [x] Helper implemented.
- [x] Route wired.
- [x] Tests updated.
- [x] Completion review filed.
- [ ] Commit created for G1 phase.

Completion review:

`docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`

## Return-To-Orchestrator Conditions

Return if implementation requires new role taxonomy, receipt-envelope mutation,
provider behavior change, or auth/RBAC redesign.

## Operator Checkpoint

operator.checkpoint.waiver: Operator already authorized Codex to proceed
through the six remaining phases in priority order and to use API keys when
needed; G1 does not require live key usage.

## Claim Boundary

This work order closes only G1 minimum viable execution identity runtime gate.
It does not close full multi-agent actor orchestration or future G phases
beyond the existing `/api/execute` path.
