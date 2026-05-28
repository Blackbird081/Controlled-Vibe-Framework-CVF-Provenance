# CVF Work Order D7 - Qwen3 Skill Preflight Hosted Proof

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

## Required First Reads

1. `docs/baselines/CVF_GC018_D7_QWEN3_SKILL_PREFLIGHT_HOSTED_PROOF_2026-05-23.md`
2. `docs/reviews/CVF_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_BLOCKER_REVIEW_2026-05-23.md`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-route-guards.ts`

## Goal

Finish the D6 follow-up by proving, or precisely reclassifying, the corrected
Qwen3 thinking model on the hosted route with an explicit Skill Preflight
declaration.

## Purpose

Execute the D7 hosted proof payload correction.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D7_QWEN3_SKILL_PREFLIGHT_HOSTED_PROOF_2026-05-23.md`
- D6 blocker:
  `docs/reviews/CVF_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_BLOCKER_REVIEW_2026-05-23.md`

## Agent Roles

- Implementer: Codex.
- Auditor: Codex via review packet and hook chain.

## Scope / Target / Owner Boundary

Target: one hosted proof payload. Owner: Qwen3 hosted proof tranche.

## Allowed / Forbidden Scope

Allowed: payload field correction and evidence docs.

Forbidden: route/auth/safety/receipt/guard weakening and retry loops.

## Pre-Flight Checks

Run local safety and enforcement preflight before hosted proof.

## Write Ownership

Permitted writes are D7 docs, continuity docs, and public-safe sync notes.

## Execution Plan

Use the implementation steps below as the execution plan.

## Implementation Steps

1. Build one hosted proof payload for `qwen3-235b-a22b-thinking-2507` with:
   - `skillPreflightPassed: true`;
   - `skillPreflightDeclaration` containing `SKILL PREFLIGHT PASS`;
   - `skillPreflightRecordRef` pointing to the D6 blocker or D7 review;
   - no raw secrets, credentials, or unsafe strings.
2. Run local safety preflight using current `applySafetyFilters()`.
3. Run local enforcement preflight using current `evaluateEnforcement()`.
4. Run exactly one signed hosted service-token call to
   `https://vibcode.netlify.app/api/execute`.
5. Capture sanitized facts only.
6. File completion or blocker review.
7. Run focused checks needed for touched surfaces and local governance hook
   chain.
8. Commit and push private provenance.
9. Switch to public-sync clone, verify `git remote -v`, port public-safe files,
   run appropriate public checks, commit, and push public `origin/main`.

## Stop Rules

- If local safety or enforcement preflight fails, do not call hosted.
- If the hosted proof returns non-200, `success=false`, non-ALLOW, missing
  live evidence, missing receipt/trace, or wrong model/provider, stop and file
  blocker.
- Do not make a second hosted call under D7.
- Do not weaken route/auth/safety/receipt/provider behavior to pass.

## Acceptance Criteria

Acceptance requires local preflight PASS and hosted proof PASS, or a blocker
review after first non-pass.

## Review Gate

File a completion or blocker review before commit.

## Return-To-Orchestrator Conditions

Return blocked on any local or hosted non-pass.

## Operator Checkpoint

Operator review is required before any new hosted retry after D7.

## Evidence Requirements

The review must include:

- payload class and Skill Preflight declaration shape, without raw secrets;
- local preflight results;
- hosted HTTP status, success, decision, routing decision, enforcement status,
  evidence mode, provider/model, receipt id, trace id, output length, and raw
  secret flag;
- public-sync remote confirmation and push result if public sync is performed;
- governance hook result;
- Evidence Trace Block;
- explicit claim boundary.

## Closure Checklist

- [ ] D7 GC-018 filed.
- [ ] D7 work order filed.
- [ ] Local safety preflight PASS.
- [ ] Local enforcement preflight PASS.
- [ ] Exactly one hosted proof executed.
- [ ] Completion or blocker review filed.
- [ ] Private provenance committed and pushed.
- [ ] Public-sync remote verified before public push.
- [ ] Public-safe updates committed and pushed, or blocker explains why not.

## Claim Boundary

D7 can claim only Skill Preflight-compliant hosted proof status.
