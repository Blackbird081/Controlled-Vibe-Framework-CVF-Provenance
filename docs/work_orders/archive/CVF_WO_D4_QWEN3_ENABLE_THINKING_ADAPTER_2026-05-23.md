# CVF Work Order D4 — Qwen3 Enable Thinking Adapter Fix

Memory class: SUMMARY_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-23

---

## Required First Reads

Before starting implementation, read in order:

1. `docs/baselines/CVF_GC018_D4_QWEN3_ENABLE_THINKING_ADAPTER_2026-05-23.md`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`
4. `docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_BLOCKER_REVIEW_2026-05-23.md`
5. `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`

---

## Purpose

Fix the Alibaba DashScope provider in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
to inject `enable_thinking: false` for non-streaming Qwen3 model calls.

This unblocks the D3 hosted Qwen3 proof, which returned
`success=false` with error:
`parameter.enable_thinking must be set to false for non-streaming calls`.

After the fix, run one live hosted proof call per model
(`qwen3-32b` and `qwen3-235b-a22b-thinking`) against
`https://vibcode.netlify.app/api/execute` before the free-tier
quota expires on 2026-06-02.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_D4_QWEN3_ENABLE_THINKING_ADAPTER_2026-05-23.md`
- D3 blocker: `docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_BLOCKER_REVIEW_2026-05-23.md`
- D3 predecessor: `docs/baselines/CVF_GC018_D3_QWEN3_PROVIDER_EXPANSION_2026-05-23.md`
- P3 hosted proof: `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`
- Operator authorization: explicit — "đồng ý"

---

## Agent Roles

- Implementer: Codex
- Reviewer: Codex (GC-019 structural review)
- Auditor: Codex (completion review with sanitized evidence)
- Quality assessor: Claude (external verification after closure)

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
  — add `isQwen3Model` helper; inject `enable_thinking: false` in
  `executeAlibaba` for non-streaming Qwen3 calls
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`
  — add assertions for `enable_thinking: false` injection
- `docs/reviews/CVF_D4_QWEN3_ENABLE_THINKING_ADAPTER_COMPLETION_2026-05-23.md`
  — completion review with sanitized receipt facts

### Out of scope (forbidden)

- `vision-contract.ts`, `reasoning-contract.ts` — read-only, do not touch
- `/api/execute` route.ts, types.ts, receipt schema, or auth logic — no change
- `PROVIDER_CAPABILITY_REGISTRY` or `capability.json` — already updated in D3
- stream adapter or json_mode adapter for Qwen3 — defer to future tranche
- any memory tier, persistence, or database work
- public-sync — no update in this tranche
- any freeze release or kernel-owner replacement
- claiming broad Qwen3 stability, all-provider parity, or production readiness

---

## Implementation Steps

### Step 1 — GC-023 Pre-flight

Check current line counts before modifying any governed file:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
  — current: 492 lines; hard threshold: 1000 lines (general_source); safe
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`
  — current: 576 lines; hard threshold: 1200 lines (test_code); safe

No exception registry entry needed.

### Step 2 — Add isQwen3Model helper

In `providers.ts`, add after the existing `isAlibabaStreamingOnlyModel`
function (line 5):

```typescript
function isQwen3Model(model: string): boolean {
    return /^qwen3-/i.test(model);
}
```

### Step 3 — Inject enable_thinking: false

In `executeAlibaba`, inside the `body: JSON.stringify({...})` block,
after the existing `...(isStreamingOnly ? {...} : {})` spread, add:

```typescript
...(isQwen3Model(config.model) && !isStreamingOnly
    ? { enable_thinking: false }
    : {}),
```

The final body should look like:

```typescript
body: JSON.stringify({
    model: config.model,
    messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
    ],
    max_tokens: config.maxTokens || 4096,
    temperature: config.temperature || 0.7,
    ...(isStreamingOnly
        ? {
            stream: true,
            stream_options: { include_usage: true },
        }
        : {}),
    ...(isQwen3Model(config.model) && !isStreamingOnly
        ? { enable_thinking: false }
        : {}),
}),
```

### Step 4 — Tests

Add to `providers.test.ts`:

- assert that for `model: "qwen3-32b"` (non-streaming), the DashScope
  request body includes `enable_thinking: false`
- assert that for `model: "qwen3-235b-a22b-thinking"` (non-streaming),
  the DashScope request body includes `enable_thinking: false`
- assert that for `model: "qwen-turbo"` (non-streaming), the DashScope
  request body does NOT include `enable_thinking`

Run `npm test:run` in `cvf-web` — all tests must PASS.

### Step 5 — Hosted proof (two calls)

For each model, POST one signed service-token request to
`https://vibcode.netlify.app/api/execute` using a concrete
`strategy_analysis` payload (same payload class that passed P3).

Pass/fail matrix per call (inherited from P3):

| Criterion | Required value |
| --- | --- |
| HTTP status | 200 |
| `success` | true |
| `decision` | ALLOW |
| `routingDecision` | ALLOW |
| `evidenceMode` | live |
| `provider` | alibaba |
| `model` | matches requested model |
| Receipt id | present (non-empty) |
| Trace id | present (non-empty) |
| Raw secret printed | false |

Record only sanitized facts — no raw API key, service token, HMAC
signature, or signed request headers in any artifact.

If the first hosted proof call returns `success=false`, stop and file
a blocker review. Do not retry in a loop.

### Step 6 — Completion review

File `docs/reviews/CVF_D4_QWEN3_ENABLE_THINKING_ADAPTER_COMPLETION_2026-05-23.md`
with:

- implementation change summary (helper + injection location)
- test result: N/N PASS
- sanitized hosted proof table for each model (one row per criterion)
- claim boundary statement

---

## Pre-flight Checks (GC-023)

Before modifying any governed file:

1. Check current line count of
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
   (currently 492 — safe below 700 advisory)
2. Check current line count of
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`
   (currently 576 — safe below 800 advisory)
3. Check exception registry at
   `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json`
4. If adding would exceed the approved limit, create a dedicated file
   instead of appending to the existing one.

---

## Acceptance Criteria

- [ ] `isQwen3Model` helper present in `providers.ts`
- [ ] `enable_thinking: false` injected for Qwen3 non-streaming calls
- [ ] `npm test:run` in `cvf-web` all PASS
- [ ] Hosted proof for `qwen3-32b`: HTTP 200, success=true, ALLOW,
  evidenceMode=live, receipt present, rawSecretPrinted=false
- [ ] Hosted proof for `qwen3-235b-a22b-thinking`: HTTP 200, success=true,
  ALLOW, evidenceMode=live, receipt present, rawSecretPrinted=false
- [ ] Completion review filed with sanitized facts only
- [ ] No raw secret in any committed artifact
- [ ] No claim beyond bounded two-model hosted proof

---

## Allowed / Forbidden Scope Detail

Allowed scope:

- Additive helper function `isQwen3Model` in `providers.ts`
- One conditional spread in `executeAlibaba` body
- New test assertions for `enable_thinking` injection
- Two hosted proof calls using P3 pass/fail matrix
- Completion review with sanitized evidence

Forbidden scope:

- Modifying existing provider logic for non-Qwen3 models
- Touching `vision-contract.ts` or `reasoning-contract.ts`
- Changing `route.ts`, `types.ts`, receipt schema, or auth logic
- Modifying `PROVIDER_CAPABILITY_REGISTRY` or `capability.json`
- Adding stream() or json_mode() adapters for Qwen3
- Claiming thinking-mode governance completeness
- Any public-sync commit

---

## Execution Plan

1. Read required first reads (see above).
2. Run GC-023 pre-flight line count checks.
3. Add `isQwen3Model` helper to `providers.ts`.
4. Add `enable_thinking: false` conditional spread in `executeAlibaba`.
5. Add test assertions for the injection; run `npm test:run` — all PASS.
6. Run one signed hosted proof call for `qwen3-32b`; capture sanitized facts.
7. Run one signed hosted proof call for `qwen3-235b-a22b-thinking`; capture
   sanitized facts.
8. File completion review with sanitized receipt table and claim boundary.
9. Commit all changes with descriptive message referencing D4 closure.

---

## Evidence Requirements

- `providers.ts` diff showing `isQwen3Model` helper and conditional
  `enable_thinking: false` spread
- `npm test:run` output in `cvf-web`: N/N PASS
- Sanitized hosted proof table per model: HTTP 200, success=true, ALLOW,
  evidenceMode=live, receipt id, trace id, rawSecretPrinted=false
- No raw secret value in any committed file

---

## Review Gate

Codex self-reviews as GC-019 structural reviewer before filing completion
review. Check:

- `isQwen3Model` helper is additive; no existing logic removed
- `enable_thinking: false` injection is conditional on non-streaming path only
- no other providers or models affected
- test assertions cover both new models and the negative case (qwen-turbo)
- completion review contains sanitized facts only
- claim boundary statement present

---

## Operator Checkpoint

No blocked-work override required for this tranche. Provider param injection
is additive and conditional. Operator has authorized this tranche explicitly.

If either hosted proof call returns a non-200 or `success=false` result,
stop and file a blocker review — do not retry in a loop.

---

## Return-To-Orchestrator Conditions

Return to operator when:

- all acceptance criteria are checked
- completion review is committed
- `npm test:run` PASS confirmed in commit

Do not proceed to further tranches without fresh operator authorization.

---

## Closure Checklist

- [ ] GC-018 filed and present
- [ ] `isQwen3Model` helper added to `providers.ts`
- [ ] `enable_thinking: false` injection in `executeAlibaba`
- [ ] Tests pass: all existing + new assertions
- [ ] Hosted proof qwen3-32b: PASS (all 10 matrix criteria including success=true)
- [ ] Hosted proof qwen3-235b-a22b-thinking: PASS (all 10 matrix criteria)
- [ ] Completion review filed with sanitized facts
- [ ] No raw secret in any committed artifact
- [ ] Commit message references D4 closure

---

## Claim Boundary

This work order delivers a bounded provider adapter parameter fix and two
hosted proof calls. It does not claim broad Qwen3 stability, production
readiness, hosted SaaS readiness, thinking-mode governance completeness,
all-provider parity, or any capability beyond two named models executing
one governed call each on free-tier quota.

Free-tier quota note: evidence is bounded to Alibaba free-tier quota
expiring 2026-06-02. Claims based on this evidence do not extend to
paid-tier behavior, rate limits, or production load.
