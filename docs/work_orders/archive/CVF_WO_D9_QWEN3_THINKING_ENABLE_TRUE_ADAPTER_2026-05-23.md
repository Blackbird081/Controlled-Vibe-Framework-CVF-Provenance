# CVF Work Order D9 - Qwen3 Thinking Enable True Adapter

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

## Required First Reads

1. `docs/baselines/CVF_GC018_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_2026-05-23.md`
2. `docs/reviews/CVF_D8_QWEN3_AI_COMMIT_HOSTED_PROOF_BLOCKER_REVIEW_2026-05-23.md`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`

## Purpose

Correct the Alibaba adapter parameter for Qwen3 thinking model ids.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_2026-05-23.md`
- D8 blocker:
  `docs/reviews/CVF_D8_QWEN3_AI_COMMIT_HOSTED_PROOF_BLOCKER_REVIEW_2026-05-23.md`

## Agent Roles

- Implementer: Codex.
- Auditor: Codex via tests, review packet, and hook chain.

## Scope / Target / Owner Boundary

Target: Alibaba provider adapter and one hosted proof. Owner: Qwen3 hosted
proof tranche.

## Allowed / Forbidden Scope

Allowed: provider adapter branch, focused tests, evidence docs, public-safe
sync.

Forbidden: route/auth/safety/receipt/guard weakening and retry loops.

## Pre-Flight Checks

Run focused providers test, `cvf-web` check, and local route preflight.

## Write Ownership

Permitted writes are provider adapter/test files, D9 docs, continuity docs, and
public-sync copies of public-safe files.

## Execution Plan

Use the steps below as the execution plan.

## Steps

1. Add a helper that detects Qwen3 thinking model ids.
2. Change Alibaba non-streaming request-body logic:
   - Qwen3 thinking -> `enable_thinking: true`;
   - other Qwen3 -> `enable_thinking: false`;
   - non-Qwen3 -> no `enable_thinking`.
3. Update provider tests.
4. Run focused provider tests and `cvf-web` check.
5. Run D9 local safety/enforcement/guard preflight.
6. Run exactly one hosted proof.
7. File completion or blocker review.
8. Commit/push private provenance.
9. Public-sync public-safe files from the public-sync clone after verifying
   remote.

## Stop Rules

- Do not hosted-call if local tests/check/preflight fail.
- Do not retry hosted under D9 after a non-pass.
- Do not alter route/auth/safety/receipt/guard semantics.

## Acceptance Criteria

Acceptance requires focused tests/checks PASS, local preflight PASS, public
deploy freshness if hosted uses public repo, and one hosted proof PASS.

## Review Gate

File completion or blocker review before final commit.

## Closure Checklist

- [ ] Focused provider tests PASS.
- [ ] `cvf-web` check PASS.
- [ ] Local route preflight PASS.
- [ ] Public-sync pushed if needed.
- [ ] One hosted proof executed.
- [ ] Review filed.

## Return-To-Orchestrator Conditions

Return blocked on any local, deploy, or hosted non-pass.

## Operator Checkpoint

Operator review is required before any new hosted retry after D9.

## Evidence Requirements

- focused test counts and depth classification;
- check result;
- local preflight facts;
- hosted sanitized facts;
- public-sync remote and push status;
- Evidence Trace Block.

## Claim Boundary

D9 can claim only the bounded adapter correction and hosted proof status.
