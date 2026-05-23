# CVF Work Order D10 - Qwen3 R1 Compatible Hosted Proof

Memory class: FULL_RECORD

Status: COMPLETED

## Required First Reads

1. `docs/baselines/CVF_GC018_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_2026-05-23.md`
2. `docs/reviews/CVF_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`

## Purpose

Execute one hosted proof with a provider-router-compatible `R1` payload.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_2026-05-23.md`
- D9 blocker:
  `docs/reviews/CVF_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`

## Agent Roles

- Implementer: Codex.
- Auditor: Codex via tests, local router preflight, review packet, and hook
  chain.

## Scope / Target / Owner Boundary

Target: hosted `/api/execute` proof for Alibaba
`qwen3-235b-a22b-thinking-2507`.

Owner boundary: proof payload posture only, unless local preflight exposes a
direct implementation blocker.

## Allowed / Forbidden Scope

Allowed: local verification, one hosted proof, evidence docs, continuity docs,
and public-safe sync only if code changes become necessary.

Forbidden: route/auth/safety/receipt/guard weakening, provider-router risk
ceiling changes, and retry loops.

## Pre-Flight Checks

Run focused providers test, `cvf-web` check, and local router preflight for the
exact `R1` provider request.

## Write Ownership

Permitted writes are D10 docs, continuity docs, and test log entries. Source
code writes are permitted only if local preflight exposes an implementation
defect.

## Execution Plan

Use the steps below as the execution plan.

## Steps

1. Confirm focused provider tests still pass.
2. Confirm `cvf-web` check still passes.
3. Confirm local `routeWebProvider()` returns `ALLOW` for Alibaba `R1`.
4. Run exactly one hosted proof using the same safe `strategy_analysis` payload
   shape with `cvfRiskLevel=R1`.
5. File completion or blocker review.
6. Commit/push private provenance.

## Stop Rules

- Do not hosted-call if local tests/check/preflight fail.
- Do not retry hosted under D10 after a non-pass.
- Do not alter provider-router policy just to force a proof.

## Acceptance Criteria

Acceptance requires focused tests/checks PASS, local router preflight PASS, and
one hosted proof PASS.

## Review Gate

File completion or blocker review before final commit.

## Evidence Requirements

Record focused test counts, `cvf-web` check result, local router preflight
facts, hosted sanitized facts, public commit hash, and an Evidence Trace Block
in the completion or blocker review.

## Closure Checklist

- [x] Focused provider tests PASS.
- [x] `cvf-web` check PASS.
- [x] Local router preflight PASS.
- [x] One hosted proof executed.
- [x] Review filed.

## Return-To-Orchestrator Conditions

Return blocked on any local or hosted non-pass.

## Operator Checkpoint

Operator review is required before any new hosted retry after D10.

## Claim Boundary

D10 can claim only the bounded `R1` compatible hosted proof result.
