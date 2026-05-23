# CVF Work Order D3 — Qwen3 Provider Expansion

Memory class: SUMMARY_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-23

---

## Required First Reads

Before starting implementation, read in order:

1. `docs/baselines/CVF_GC018_D3_QWEN3_PROVIDER_EXPANSION_2026-05-23.md`
2. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
5. `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`

---

## Purpose

Extend the Alibaba provider entry in `PROVIDER_CAPABILITY_REGISTRY` with
two Qwen3 models (`qwen3-32b` and `qwen3-235b-a22b-thinking`) and run one
live hosted proof call per model against `https://vibcode.netlify.app/api/execute`
before the free-tier quota expires on 2026-06-02.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_D3_QWEN3_PROVIDER_EXPANSION_2026-05-23.md`
- D2 predecessor: `docs/baselines/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- P3 hosted proof: `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`
- Operator authorization: explicit — "nên tiến hành cái này, tăng giá trị cho CVF và tận dụng free tier"

---

## Agent Roles

- Implementer: Codex
- Reviewer: Codex (GC-019 structural review)
- Auditor: Codex (completion review with sanitized evidence)
- Quality assessor: Claude (external verification after closure)

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
  — add two model entries under `providerId: "alibaba"`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
  — add two model entries
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
  — add assertions for two new models
- `docs/baselines/CVF_GC018_D3_QWEN3_PROVIDER_EXPANSION_2026-05-23.md`
  — GC-018 (already filed)
- `docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_COMPLETION_2026-05-23.md`
  — completion review with sanitized receipt facts

### Out of scope (forbidden)

- `vision-contract.ts`, `reasoning-contract.ts` — read-only, do not touch
- `/api/execute` route, receipt envelopes, auth semantics — no change
- stream adapter or json_mode adapter for Qwen3 — defer to future tranche
- any memory tier, persistence, or database work
- public-sync — no update in this tranche
- any freeze release or kernel-owner replacement
- claiming broad Qwen3 stability, all-provider parity, or production readiness

---

## Implementation Steps

### Step 1 — Registry update

Add to `PROVIDER_CAPABILITY_REGISTRY` under the existing `"alibaba"` entry:

```typescript
{
  modelId: "qwen3-32b",
  supportedMethods: ["complete", "chat"],
  defaultMethod: "complete",
},
{
  modelId: "qwen3-235b-a22b-thinking",
  supportedMethods: ["complete", "chat", "reasoning"],
  defaultMethod: "complete",
},
```

`reasoning` is an existing `ProviderMethodName` — no new type needed.

### Step 2 — capability.json update

Add the two models to
`EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
mirroring the registry structure.

### Step 3 — Tests

Add to `tests/provider-capability-registry.test.ts`:

- assert `qwen3-32b` is registered under `"alibaba"` with methods
  `["complete", "chat"]`
- assert `qwen3-235b-a22b-thinking` is registered under `"alibaba"` with
  methods `["complete", "chat", "reasoning"]`
- assert `getProviderMethodContract` resolves both models correctly
- assert `assertRegistryProviderMethodSupported` does not throw for
  `"complete"` on both models

Run `npm test` in `CVF_MODEL_GATEWAY` — all tests must PASS.

### Step 4 — Hosted proof (two calls)

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

### Step 5 — Completion review

File `docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_COMPLETION_2026-05-23.md`
with:

- registry change summary
- test result: N/N PASS
- sanitized hosted proof table for each model (one row per criterion)
- claim boundary statement

---

## Pre-flight Checks (GC-023)

Before adding lines to any existing governed file:

1. Check current line count of
   `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
2. Check exception registry at
   `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json`
3. If adding would exceed the approved limit, create a dedicated test file
   instead of appending to the existing one.

---

## Acceptance Criteria

- [ ] `PROVIDER_CAPABILITY_REGISTRY` contains `qwen3-32b` and
  `qwen3-235b-a22b-thinking` under `"alibaba"`
- [ ] `capability.json` updated accordingly
- [ ] `npm test` in `CVF_MODEL_GATEWAY` all PASS
- [ ] Hosted proof for `qwen3-32b`: HTTP 200, ALLOW, evidenceMode=live,
  receipt present, rawSecretPrinted=false
- [ ] Hosted proof for `qwen3-235b-a22b-thinking`: HTTP 200, ALLOW,
  evidenceMode=live, receipt present, rawSecretPrinted=false
- [ ] Completion review filed with sanitized facts only
- [ ] No raw secret in any committed artifact
- [ ] No claim beyond bounded two-model hosted proof

---

## Allowed / Forbidden Scope Detail

Allowed scope:

- Additive-only changes to registry and capability.json
- New test assertions for two named models
- Two hosted proof calls using P3 pass/fail matrix
- Completion review with sanitized evidence

Forbidden scope:

- Modifying existing alibaba/deepseek model entries
- Touching vision-contract.ts or reasoning-contract.ts
- Changing route.ts, types.ts, receipt schema, or auth logic
- Adding stream() or json_mode() adapters for Qwen3
- Claiming thinking-mode governance completeness
- Any public-sync commit

---

## Execution Plan

1. Read required first reads (see above).
2. Add `qwen3-32b` and `qwen3-235b-a22b-thinking` to `PROVIDER_CAPABILITY_REGISTRY` under `"alibaba"`.
3. Update `providers/alibaba/capability.json` to match.
4. Add test assertions for both models; run `npm test` — all PASS.
5. Run one signed hosted proof call per model; capture sanitized facts.
6. File completion review with sanitized receipt table and claim boundary.
7. Commit all changes with descriptive message.

---

## Evidence Requirements

- `PROVIDER_CAPABILITY_REGISTRY` diff showing two new model entries
- `npm test` output: N/N PASS in `CVF_MODEL_GATEWAY`
- Sanitized hosted proof table per model: HTTP 200, success=true, ALLOW,
  evidenceMode=live, receipt id, trace id, rawSecretPrinted=false
- No raw secret value in any committed file

---

## Review Gate

Codex self-reviews as GC-019 structural reviewer before filing completion
review. Check:

- registry entries are additive only (no existing entry modified)
- test assertions cover both new models
- completion review contains sanitized facts only
- claim boundary statement present

---

## Operator Checkpoint

No blocked-work override required for this tranche. Registry extension
is additive only. Operator has authorized this tranche explicitly.

If either hosted proof call returns a non-200 or non-ALLOW result, stop
and file a blocker review — do not retry in a loop.

---

## Return-To-Orchestrator Conditions

Return to operator when:

- all acceptance criteria are checked
- completion review is committed
- `npm test` PASS confirmed in commit

Do not proceed to further tranches without fresh operator authorization.

---

## Closure Checklist

- [ ] GC-018 filed and present
- [ ] Registry updated with two new Alibaba models
- [ ] capability.json updated
- [ ] Tests pass: all existing + new assertions
- [ ] Hosted proof qwen3-32b: PASS (all 8 matrix criteria)
- [ ] Hosted proof qwen3-235b-a22b-thinking: PASS (all 8 matrix criteria)
- [ ] Completion review filed with sanitized facts
- [ ] No raw secret in any committed artifact
- [ ] Commit message references D3 closure

---

## Claim Boundary

This work order delivers a bounded provider registry extension and two
hosted proof calls. It does not claim broad Qwen3 stability, production
readiness, hosted SaaS readiness, thinking-mode governance completeness,
all-provider parity, or any capability beyond two named models executing
one governed call each on free-tier quota.

Free-tier quota note: evidence is bounded to Alibaba free-tier quota
expiring 2026-06-02. Claims based on this evidence do not extend to
paid-tier behavior, rate limits, or production load.
