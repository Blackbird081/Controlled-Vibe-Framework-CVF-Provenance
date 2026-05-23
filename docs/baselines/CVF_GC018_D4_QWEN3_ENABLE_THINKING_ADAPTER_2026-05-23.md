# CVF GC-018 D4 Qwen3 Enable Thinking Adapter Fix

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_READY_FOR_IMPLEMENTATION

Date: 2026-05-23

## Purpose

Authorize a bounded fix to `executeAlibaba` in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts` to
inject `enable_thinking: false` for non-streaming Qwen3 model calls, unblocking
the D3 hosted Qwen3 proof.

The D3 tranche delivered the Qwen3 registry entries and passing tests, but the
first hosted proof call returned `success=false` with error:
`parameter.enable_thinking must be set to false for non-streaming calls`.
This tranche fixes only that provider parameter injection.

## Scope

In scope:

- add an `isQwen3Model` helper in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
  that matches models prefixed `qwen3-`;
- inject `enable_thinking: false` into the DashScope request body when
  `isQwen3Model(config.model)` is true and the call is non-streaming;
- add unit test assertions in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`
  covering the new injection condition;
- run one hosted proof call per model (`qwen3-32b` and
  `qwen3-235b-a22b-thinking`) against
  `https://vibcode.netlify.app/api/execute` using the P3 pass/fail matrix;
- file a completion review with sanitized receipt facts per model.

Out of scope:

- any change to `vision-contract.ts` or `reasoning-contract.ts`;
- any change to `/api/execute` route logic, receipt envelopes, or
  auth semantics;
- stream/json_mode adapters for Qwen3;
- any new memory tier, persistence, or database work;
- any public-sync update;
- any freeze release or kernel-owner replacement;
- claiming broad Qwen3 stability, all-provider parity, or production
  readiness.

## Source / Predecessor Evidence

- D3 partial closure:
  `docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_BLOCKER_REVIEW_2026-05-23.md`
- D3 GC-018:
  `docs/baselines/CVF_GC018_D3_QWEN3_PROVIDER_EXPANSION_2026-05-23.md`
- P3 hosted proof:
  `docs/reviews/CVF_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_COMPLETION_2026-05-23.md`
- Blocker root cause: Alibaba DashScope requires `enable_thinking: false` in
  non-streaming request body for Qwen3 models.
- Free-tier expiry: Alibaba Qwen3 free quota expires 2026-06-02.

## GC-018 Candidate Screening

| Candidate | Class | Score | Decision | Rationale |
| --- | ---: | ---: | --- | --- |
| enable_thinking=false for Qwen3 non-streaming | BUG_FIX / VALIDATION_TEST | 9/10 | CONTINUE | D3 registry and tests already done; only one provider param blocks hosted proof; free-tier expires 2026-06-02. |
| Qwen3 streaming adapter | IMPLEMENTATION | 4/10 | DEFER | Streaming path already works for qwen-turbo; out of D4 scope. |
| Qwen3 thinking-mode governance | BROAD_TEST | 3/10 | DEFER | Separate tranche; broader governance scope needed. |

## Depth Audit

Candidate: `D4_QWEN3_ENABLE_THINKING_ADAPTER`

- Risk reduction: 2 (unblocks D3 which is blocked at provider param; free-tier expiry creates time pressure)
- Decision value: 2 (proves two Qwen3 models on hosted governed path)
- Machine enforceability: 2 (unit test asserts injection; hosted proof asserts success=true)
- Operational efficiency: 2 (minimal delta — ~10 lines; no new types or interfaces)
- Portfolio priority: 1 (time-bounded by free-tier expiry 2026-06-02)
- Total: 9
- Decision: CONTINUE

## Authorization Boundary

- Authorized now: YES
- Tranche name: `D4_QWEN3_ENABLE_THINKING_ADAPTER`
- Blocked-work override required: NO
- Active-path impact: ADDITIVE only — one conditional param injection in
  existing `executeAlibaba`; no existing logic removed or altered
- Expected enforcement class: PROVIDER_ADAPTER_PARAM_FIX
- Required evidence:
  - `providers.ts` updated with `isQwen3Model` helper and `enable_thinking: false` injection;
  - `providers.test.ts` assertions cover the new injection;
  - `npm test` (or equivalent) PASS in `cvf-web`;
  - two hosted proof calls (qwen3-32b and qwen3-235b-a22b-thinking), each
    returning HTTP 200, success=true, decision ALLOW, evidenceMode=live,
    receipt id present, rawSecretPrinted=false;
  - completion review filed with sanitized receipt facts.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline: D3 partial closure is filed at
`docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_BLOCKER_REVIEW_2026-05-23.md`.
Registry entries `qwen3-32b` and `qwen3-235b-a22b-thinking` are present in
`PROVIDER_CAPABILITY_REGISTRY` and `capability.json`. All Model Gateway tests
pass (81 tests, 20 files) in `CVF_MODEL_GATEWAY`. The hosted target
`https://vibcode.netlify.app` is
confirmed reachable and governed (P3 receipt `rcpt-env-mpi55je6-hiddxq`).

Proposed tranche: `D4_QWEN3_ENABLE_THINKING_ADAPTER` — single provider param
injection fix. No registry, route, receipt, or auth change.

## Evidence / Verification

Required evidence before closure:

- `providers.ts` diff showing `isQwen3Model` helper and `enable_thinking: false`
  conditional injection under non-streaming Alibaba path;
- `providers.test.ts` assertions for the new condition;
- `npm test` PASS in `cvf-web` (all existing + new assertions);
- two hosted proof calls passing the P3 pass/fail matrix (HTTP 200,
  success=true, ALLOW, evidenceMode=live, receipt present,
  rawSecretPrinted=false);
- completion review filed with sanitized receipt facts only.

## Claim Boundary

This GC-018 authorizes a single provider parameter injection fix and two
hosted proof calls only. It does not claim broad Qwen3 stability, production
readiness, hosted SaaS readiness, thinking-mode governance completeness, or
any capability beyond two named models executing one governed call each.

Free-tier quota note: evidence is bounded to Alibaba free-tier quota
expiring 2026-06-02. Claims based on this evidence do not extend to
paid-tier behavior, rate limits, or production load.
