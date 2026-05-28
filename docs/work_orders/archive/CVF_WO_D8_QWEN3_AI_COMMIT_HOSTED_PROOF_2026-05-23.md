# CVF Work Order D8 - Qwen3 AI Commit Hosted Proof

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

## Required First Reads

1. `docs/baselines/CVF_GC018_D8_QWEN3_AI_COMMIT_HOSTED_PROOF_2026-05-23.md`
2. `docs/reviews/CVF_D7_QWEN3_SKILL_PREFLIGHT_HOSTED_PROOF_BLOCKER_REVIEW_2026-05-23.md`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Goal

Run the corrected Qwen3 thinking model hosted proof with all route-level
pre-provider gates declared: Skill Preflight plus `aiCommit`.

## Purpose

Execute the D8 `aiCommit` payload correction.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D8_QWEN3_AI_COMMIT_HOSTED_PROOF_2026-05-23.md`
- D7 blocker:
  `docs/reviews/CVF_D7_QWEN3_SKILL_PREFLIGHT_HOSTED_PROOF_BLOCKER_REVIEW_2026-05-23.md`

## Agent Roles

- Implementer: Codex.
- Auditor: Codex via review packet and hook chain.

## Scope / Target / Owner Boundary

Target: one hosted proof payload. Owner: Qwen3 hosted proof tranche.

## Allowed / Forbidden Scope

Allowed: payload field correction and evidence docs.

Forbidden: route/auth/safety/receipt/guard weakening and retry loops.

## Pre-Flight Checks

Run local safety, enforcement, and guard-runtime preflight before hosted proof.

## Write Ownership

Permitted writes are D8 docs and continuity docs.

## Execution Plan

Use the steps below as the execution plan.

## Steps

1. Build one payload for `qwen3-235b-a22b-thinking-2507`.
2. Include Skill Preflight fields from D7.
3. Include `aiCommit` with `commitId`, `agentId`, `timestamp`, and description.
4. Run local safety, enforcement, and guard-runtime preflight.
5. Run exactly one hosted proof call.
6. Stop on first non-pass.
7. File completion/blocker review.
8. Commit/push private provenance.
9. Port public-safe changes through public-sync only after remote verification.

## Stop Rules

- Do not call hosted if any local preflight fails.
- Do not retry the hosted call under D8 after any non-pass.
- Do not change governance gates to pass the proof.

## Acceptance Criteria

Acceptance requires local preflight PASS and hosted proof PASS, or a blocker
review after first non-pass.

## Review Gate

File a completion or blocker review before commit.

## Closure Checklist

- [ ] Local preflight PASS.
- [ ] One hosted proof executed.
- [ ] Review filed.

## Return-To-Orchestrator Conditions

Return blocked on any local or hosted non-pass.

## Operator Checkpoint

Operator review is required before any new hosted retry after D8.

## Evidence Requirements

- local safety/enforcement/guard preflight facts;
- hosted sanitized matrix;
- raw-secret printed flag;
- governance hook result;
- public-sync remote and push status if public sync is performed;
- Evidence Trace Block.

## Claim Boundary

D8 can claim only `aiCommit`-compliant hosted proof status.
