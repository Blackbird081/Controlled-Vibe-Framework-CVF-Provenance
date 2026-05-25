# CVF Work Order D Provider Scale Live VI Proof

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-25

---

## Purpose

Execute the bounded D provider-scale live proof authorized by
`docs/baselines/CVF_GC018_D_PROVIDER_SCALE_LIVE_VI_PROOF_2026-05-25.md`.

## Owner Files

Allowed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/*.live.test.ts`
- `docs/reviews/CVF_D_PROVIDER_SCALE_LIVE_VI_PROOF_*`
- active state/front door/handoff files

Forbidden:

- provider adapter/router implementation changes;
- `/api/execute/route.ts` behavior changes;
- model registry changes;
- receipt envelope changes;
- prompt mutation;
- public-sync or hosted/product readiness claims.

## Authority Chain

- Operator approved order: B+VI4 first, then D provider scale, then C workflow
  scale.
- VI4 closed with Alibaba live receipts and `cvf.verticalEvidencePackage.vi4.v1`.
- This work order implements only the D provider-scale slice authorized by the
  paired GC-018 packet.

## Agent Roles

- Implementer: add the smallest focused live spec.
- Auditor: verify no provider/router/route behavior changes.
- Provider-risk owner: classify live failures before any rerun.
- Product/operator advocate: ensure evidence is readable as provider breadth,
  not as broad stability.

## Allowed / Forbidden Scope

Allowed: test/evidence-only DeepSeek + OpenAI live proof, completion packet,
and session continuity updates.

Forbidden: provider adapter/router implementation changes, route behavior
changes, model registry changes, prompt mutation, receipt envelope change,
public-sync, hosted readiness, production readiness, broad provider stability,
or freeze release.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reviews/CVF_VI4_VERTICAL_EVIDENCE_SURFACE_EXPANSION_COMPLETION_2026-05-25.md`
- `docs/baselines/CVF_GC018_D_PROVIDER_SCALE_LIVE_VI_PROOF_2026-05-25.md`
- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

## Pre-Flight Checks

- confirm `.env.local` has DeepSeek and OpenAI keys without printing values;
- confirm worktree is clean after VI4 closure;
- confirm planned diff does not touch provider adapters, router, route handler,
  or model registries.

## Write Ownership

Writes are limited to the live spec, completion review, this work order, active
state, session front door, and active handoff.

## Execution Plan

1. Add focused DeepSeek + OpenAI VI4 live proof spec.
2. Run local TypeScript check if code changed.
3. Load keys from `.env.local` secret-safely.
4. Run the live proof once.
5. If any lane fails, classify with mandatory live diagnostics before rerun.
6. File completion review and update session/handoff.
7. Commit closure.

## Acceptance Criteria

- DeepSeek live proof PASS or diagnostic filed.
- OpenAI live proof PASS or diagnostic filed.
- VI4 evidence package asserted on both provider lanes.
- No provider/router/route behavior code changes.
- Active state and handoff guards PASS.

## Evidence Requirements

- `npm run check` PASS when TypeScript test code changes.
- Live DeepSeek proof PASS or diagnostic filed.
- Live OpenAI proof PASS or diagnostic filed.
- Active session state guard PASS.
- Handoff guard PASS.

## Review Gate

Before closure, verify the diff contains no provider adapter/router
implementation changes, route behavior changes, model registry changes,
receipt-envelope changes, or public/hosted/product-readiness claims.

## Operator Checkpoint

No checkpoint is required unless a live provider returns a non-retryable
diagnostic that requires account/key/model access, adapter/router changes, or
scope expansion.

## Claim / Final / Verification Boundary

This work order may close only a two-provider live VI4 proof for DeepSeek and
OpenAI. It may not claim broad provider stability, repeated soak, hosted
readiness, production readiness, or freeze release.

## Claim Boundary

Same as above: the final claim is limited to bounded DeepSeek + OpenAI VI4 live
proof on the existing route.

## Closure Checklist

- [x] live spec added
- [x] cvf-web check PASS
- [x] DeepSeek live proof PASS or diagnostic filed
- [x] OpenAI live proof PASS or diagnostic filed
- [x] completion review filed
- [x] active state/front door/handoff updated
- [x] active state guard PASS
- [x] handoff guard PASS
- [x] commit created

## Return-To-Orchestrator Conditions

Return blocked if either provider fails with a non-retryable diagnostic that
requires adapter/router changes, model access changes, account/key action, or
scope expansion.
