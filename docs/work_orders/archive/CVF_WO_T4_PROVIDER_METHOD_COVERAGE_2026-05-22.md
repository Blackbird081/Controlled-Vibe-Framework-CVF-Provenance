# Work Order — T4 Provider Method Coverage

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex (full Orchestrator → Reviewer → Implementer → Auditor chain)

Date dispatched: 2026-05-22

---

## Purpose

Declare per-provider capability contracts and wire two new execution
methods (`stream()` on Alibaba qwen-turbo, `json_mode()` on DeepSeek
deepseek-chat) with a negative gate that rejects calls to undeclared
methods. T4 addresses Review CVF.md pain point D (provider method
parity) and closes the gap between provider capability claims and
runtime enforcement.

T4 requires the `new_provider_execution_semantics` blocked-work-class
override. The GC-018 must record operator confirmation of this override
before any implementation begins.

Pre-condition: T3 must be closed before T4 begins.

---

## Authority Chain

- Active roadmap (V2):
  `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- Predecessor audit:
  `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- T3 work order (pre-condition):
  `docs/work_orders/CVF_WO_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_2026-05-22.md`
- T3 completion review (must be filed before T4 starts):
  `docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`
- Source review (original requirement):
  `.private_reference/legacy/CVF 17.05/Review CVF.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_T4_PROVIDER_METHOD_COVERAGE_2026-05-22.md`

---

## Agent Roles

- **Orchestrator (Codex):** Confirm T3 is closed. File GC-018 baseline
  before any implementation file is created. The GC-018 must record
  operator confirmation of the `new_provider_execution_semantics` override.
  Operator must confirm override before Orchestrator proceeds past S-02.
- **Reviewer (Codex):** Confirm T4 stays within declared provider methods
  and negative gate only. No new providers, no SSE streaming route
  implementation, no new receipt fields, no memory wiring. Confirm the
  two live-call proofs are bounded (short, governed, offline where possible).
- **Implementer (Codex):** Author `ProviderMethodContract` interface,
  per-provider `capability.json` files, `stream()` adapter for Alibaba,
  `json_mode()` adapter for DeepSeek, and `UnsupportedMethodError`
  negative gate.
- **Auditor (Codex):** Run type check and relevant tests, run governance
  hook chain, file completion review, update active queue/state/handoff.

---

## Blocked-Work Override Requirement

T4 touches one blocked-work class:

- **`new_provider_execution_semantics`** — adding `stream()` and
  `json_mode()` execution methods to the CVF_MODEL_GATEWAY provider
  adapter layer.

The GC-018 baseline must record:

- Override granted: `new_provider_execution_semantics` for the specific
  bounded scope below (two new methods, two providers, negative gate).
- Operator confirmation statement.
- No expansion beyond the two named methods and two named providers is
  authorized in this override.

Operator confirmation of override status is required **before** the
Orchestrator proceeds past S-02 (GC-018). This is an Operator
Checkpoint.

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` (new)
  — `ProviderMethodContract` interface, `UnsupportedMethodError` class.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
  (new) — declares `stream: true`, `json_mode: false`.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/capability.json`
  (new) — declares `stream: false`, `json_mode: true`.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`
  (new) — `stream()` method adapter for qwen-turbo.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts`
  (new) — `json_mode()` method adapter for deepseek-chat.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` (new) —
  the negative gate that rejects calls to methods not declared in
  `capability.json`.
- Test files under
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/__tests__/` for the contract,
  adapters, and gate.
- `docs/baselines/CVF_GC018_T4_PROVIDER_METHOD_COVERAGE_2026-05-22.md`
  (new).
- `docs/reviews/CVF_T4_PROVIDER_METHOD_COVERAGE_COMPLETION_2026-05-22.md`
  (new).
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — update T4 entry status.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — update `lastUpdated` and
  `t4ProviderMethodCoverage` field.
- `AGENT_HANDOFF_V11_2026-05-21.md` — GC-020 sync entry.

### Out of scope (forbidden)

- Any change to `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` files,
  including routes, types, or UI.
- Any change to `GovernanceEvidenceReceipt` or `types.ts`.
- Any new provider beyond Alibaba (qwen-turbo) and DeepSeek
  (deepseek-chat).
- Any new execution method beyond `stream()` and `json_mode()`.
- Any SSE streaming route implementation in cvf-web.
- Any memory wiring (that is T5).
- Any workflow composition change (that is T3).
- Public-sync repository update.
- Maika, child-data, photo, or vision proof.
- Adding `stream()` capability to DeepSeek or `json_mode()` to Alibaba
  (each capability.json must declare the bounded support only).
- Any change to `vision-contract.ts` or `reasoning-contract.ts`
  (read-only).

---

## Required First Reads

- `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
- `docs/work_orders/CVF_WO_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_2026-05-22.md`
- `docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`
  (T3 pre-condition check)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/` (read existing provider adapter
  patterns before authoring new ones)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/` (read existing provider
  directory structure and adapter contracts)
- `.private_reference/legacy/CVF 17.05/Review CVF.md` (lines covering
  provider method parity pain point D)
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`

---

## Pre-Flight Checks

Before writing any implementation file:

1. Confirm T3 completion review exists with status
   `CLOSED_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE`. If T3 is not
   closed, stop.
2. Read the existing CVF_MODEL_GATEWAY directory structure. Note the
   existing provider adapter pattern and any existing capability
   declarations to avoid duplication.
3. Confirm `new_provider_execution_semantics` override is recorded in
   the GC-018 baseline (Operator Checkpoint required before S-02 closes).
4. Confirm `vision-contract.ts` and `reasoning-contract.ts` are not in
   the write ownership list. If any implementation step would require
   touching them, Return-to-Orchestrator.
5. GC-023 pre-flight: check line counts for any existing files in
   `CVF_MODEL_GATEWAY/src/` that might be modified. New files are
   unconstrained but should target under 200 lines each.

---

## Execution Plan

T4 executes in ten sequential steps S-01 → S-10.

## Implementation Steps

### S-01 — Confirm T3 pre-condition

Read T3 completion review. Confirm status is
`CLOSED_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE`. If not, stop and
report.

### S-02 — File GC-018 baseline (with override)

Create `docs/baselines/CVF_GC018_T4_PROVIDER_METHOD_COVERAGE_2026-05-22.md`
declaring:

- Pre-condition: T3 closed (cite completion review path).
- Scope locked to write ownership above.
- Blocked-work class: `new_provider_execution_semantics`.
- Override GRANTED (cite operator confirmation).
- Bounded scope of override: `stream()` on Alibaba qwen-turbo only;
  `json_mode()` on DeepSeek deepseek-chat only; negative gate for
  undeclared methods; no other provider, no other method.
- Acceptance criteria copied verbatim from V2 roadmap T4.
- Forbidden actions: any out-of-scope item from this work order.

### S-03 — Author ProviderMethodContract interface

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
defining:

```typescript
export interface ProviderCapability {
  stream: boolean;
  json_mode: boolean;
}

export interface ProviderMethodContract {
  providerId: string;
  modelId: string;
  capabilities: ProviderCapability;
}

export class UnsupportedMethodError extends Error {
  constructor(
    public readonly providerId: string,
    public readonly method: string
  ) {
    super(
      `Provider '${providerId}' does not support method '${method}'`
    );
    this.name = 'UnsupportedMethodError';
  }
}
```

### S-04 — Author capability.json for Alibaba

Create
`EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`:

```json
{
  "providerId": "alibaba",
  "modelId": "qwen-turbo",
  "capabilities": {
    "stream": true,
    "json_mode": false
  }
}
```

### S-05 — Author capability.json for DeepSeek

Create
`EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/capability.json`:

```json
{
  "providerId": "deepseek",
  "modelId": "deepseek-chat",
  "capabilities": {
    "stream": false,
    "json_mode": true
  }
}
```

### S-06 — Author stream adapter for Alibaba

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`
that:

- Accepts a governed prompt payload (same shape as the existing execute
  adapter, with no change to the receipt envelope).
- Calls the Alibaba API streaming endpoint for qwen-turbo.
- Returns an `AsyncIterable<string>` or equivalent stream type.
- On success, emits chunks.
- On failure (including network error or non-200 status), throws with a
  named error type that includes the provider name and model ID.
- Does not write to the receipt envelope directly (receipt wiring is
  the caller's responsibility).

The adapter must not bypass the existing governance gate (the call must
still flow through the provider gate, not bypass it).

### S-07 — Author json_mode adapter for DeepSeek

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts`
that:

- Accepts a governed prompt payload.
- Calls the DeepSeek API with `response_format: { type: "json_object" }`.
- Returns a parsed JSON object.
- On failure, throws with a named error type including provider and
  model ID.
- Does not bypass the existing governance gate.

### S-08 — Author provider method gate

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` that:

- Accepts a `providerId`, a `method` name, and a `ProviderMethodContract`.
- If the capability is `false` or the method is unknown, throws
  `UnsupportedMethodError`.
- If the capability is `true`, returns normally.
- Is pure synchronous — no provider call, no network call.

### S-09 — Write unit tests

Create tests covering:

- `provider-method-contract.test.ts` — `UnsupportedMethodError` throws
  with correct provider name and method in the message.
- `provider-method-gate.test.ts` — PASS when declared true; THROWS when
  declared false; THROWS for unknown method.
- `stream-adapter.test.ts` — mock network; PASS when mock returns 200;
  throws named error when mock returns 4xx/5xx.
- `json-mode-adapter.test.ts` — mock network; PASS when mock returns
  valid JSON; throws named error when mock returns error.

All tests must PASS via the CVF_MODEL_GATEWAY test runner.

### S-10 — Governance hook chain, completion review, commit

Run:

```bash
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
```

File `docs/reviews/CVF_T4_PROVIDER_METHOD_COVERAGE_COMPLETION_2026-05-22.md`
including:

- Memory class FULL_RECORD, status `CLOSED_T4_PROVIDER_METHOD_COVERAGE`.
- Override decision recorded: `new_provider_execution_semantics` GRANTED
  (bounded scope).
- Evidence trace: test output, hook chain results.
- Findings per acceptance criterion.
- Claim boundary.

Update active session (queue, state, handoff) and commit:

```text
feat(t4): close provider method coverage — stream/json_mode + negative gate

Authority: docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md
GC-018: docs/baselines/CVF_GC018_T4_PROVIDER_METHOD_COVERAGE_2026-05-22.md
Completion: docs/reviews/CVF_T4_PROVIDER_METHOD_COVERAGE_COMPLETION_2026-05-22.md

Closes T4 from the Review-CVF pain-point delivery gap roadmap V2:
- ProviderMethodContract interface + UnsupportedMethodError
- capability.json: alibaba (stream=true), deepseek (json_mode=true)
- stream() adapter on Alibaba qwen-turbo
- json_mode() adapter on DeepSeek deepseek-chat
- Negative gate: UnsupportedMethodError on undeclared method
- Unit tests PASS

Blocked-work override: new_provider_execution_semantics (bounded to
two methods, two providers).

Boundary: CVF_MODEL_GATEWAY adapter layer only. No cvf-web change,
no new receipt field, no new provider, no SSE route, no memory wiring.
```

---

## Evidence Requirements

Every closure claim must be backed by:

- T3 completion review path and status.
- GC-018 override decision record.
- Test output (all tests PASS).
- Hook chain COMPLIANT output.
- `GovernanceEvidenceReceipt` unchanged (zero diff on `types.ts`).
- Closure commit SHA.

---

## Acceptance Criteria

Closure requires **all** of:

1. T3 pre-condition confirmed.
2. GC-018 filed with `new_provider_execution_semantics` override GRANTED
   and bounded scope documented.
3. `ProviderMethodContract` interface and `UnsupportedMethodError`
   authored.
4. `capability.json` filed for both Alibaba and DeepSeek.
5. `stream()` adapter authored for Alibaba qwen-turbo.
6. `json_mode()` adapter authored for DeepSeek deepseek-chat.
7. Negative gate (`provider-method-gate.ts`) authored.
8. All unit tests authored and PASS.
9. `GovernanceEvidenceReceipt` shape unchanged; `types.ts` unchanged.
10. No file under `cvf-web/` modified.
11. No new provider beyond Alibaba and DeepSeek.
12. Markdown structural completeness: COMPLIANT.
13. File size guard: COMPLIANT.
14. Local governance hook chain: PASS.
15. Completion review filed with all required sections.
16. Active queue, state, and handoff updated with closure SHA.

---

## Review Gate

Before commit, Codex acting in Reviewer role must confirm:

1. GC-018 override decision matches implementation (only the two
   declared methods, only the two declared providers).
2. No `cvf-web/` file was modified.
3. `GovernanceEvidenceReceipt` and `types.ts` are unchanged.
4. `vision-contract.ts` and `reasoning-contract.ts` are unchanged.
5. No new provider adapters exist beyond Alibaba and DeepSeek.
6. No new execution method exists beyond `stream()` and `json_mode()`.
7. All unit tests PASS with zero failures.
8. No active-session blocked-work class other than
   `new_provider_execution_semantics` is touched.

---

## Closure Checklist

- [ ] T3 pre-condition confirmed.
- [ ] GC-018 filed with bounded override GRANTED.
- [ ] `ProviderMethodContract` interface authored.
- [ ] `UnsupportedMethodError` class authored.
- [ ] `capability.json` filed for Alibaba (stream=true, json_mode=false).
- [ ] `capability.json` filed for DeepSeek (stream=false, json_mode=true).
- [ ] `stream()` adapter authored for Alibaba qwen-turbo.
- [ ] `json_mode()` adapter authored for DeepSeek deepseek-chat.
- [ ] Negative gate authored.
- [ ] Unit tests authored and PASS.
- [ ] `types.ts` and `GovernanceEvidenceReceipt` unchanged.
- [ ] No `cvf-web/` file modified.
- [ ] Markdown structural completeness gate: COMPLIANT.
- [ ] Governed file size guard: COMPLIANT.
- [ ] Local governance hook chain pre-commit: PASS.
- [ ] Local governance hook chain pre-push: PASS.
- [ ] Active review queue updated with T4 closure status.
- [ ] Active session state updated with `t4ProviderMethodCoverage` field.
- [ ] Handoff updated with GC-020 sync entry and closure SHA.
- [ ] Completion review filed at the expected path with all required
      sections.

---

## Operator Checkpoint

**This work order has one mandatory Operator Checkpoint.**

Before the Orchestrator proceeds past S-02 (GC-018), the operator must
explicitly confirm the `new_provider_execution_semantics` override:

- Confirmation must name the bounded scope: `stream()` on Alibaba
  qwen-turbo; `json_mode()` on DeepSeek deepseek-chat; negative gate
  for undeclared methods.
- Generic confirmation ("proceed") is not sufficient.
- The GC-018 must record the operator's confirmation statement verbatim.
- No expansion of methods or providers is authorized without a separate
  GC-018 amendment.

If T4 encounters a Return-to-Orchestrator condition, the operator must
be consulted before the work order is reopened.

---

## Return-to-Orchestrator Conditions

Return this work order to the Orchestrator (do not close) if **any**:

- T3 is not closed when T4 begins.
- Operator does not confirm `new_provider_execution_semantics` override
  before GC-018 is filed.
- The Alibaba streaming API shape or the DeepSeek json_mode API shape
  differs materially from what is modeled in the adapters, requiring
  a change to the receipt envelope to carry the response correctly.
- Any acceptance criterion fails and the cause is unclear within
  bounded debug time.
- Any out-of-scope file change would be necessary to make T4 close.

When returning, file a return note at
`docs/reviews/CVF_T4_PROVIDER_METHOD_COVERAGE_RETURN_2026-05-22.md`.

---

## Forbidden Patterns (Anti-Pattern Guardrails from V2)

T4 closure must not occur via any of:

- **Closure by rejection.** T4 cannot close by arguing provider method
  parity is already covered by existing adapters.
- **Closure by scope redefinition.** T4 cannot close by dropping one of
  the two methods or one of the two providers.
- **Contract-only closure.** T4 cannot close by delivering only the
  `ProviderMethodContract` interface without the adapters and negative
  gate.
- **Implicit scope inflation.** T4 cannot quietly add a third provider
  or a third method without a fresh GC-018 amendment.

---

## Claim Boundary

This work order authorizes only:

- `ProviderMethodContract` interface and `UnsupportedMethodError`.
- `capability.json` for Alibaba and DeepSeek.
- `stream()` adapter for Alibaba qwen-turbo.
- `json_mode()` adapter for DeepSeek deepseek-chat.
- Negative gate for undeclared methods.
- Unit tests, GC-018 baseline, completion review, and active-session
  updates.

It does not authorize any cvf-web change, any new receipt field, any
new provider, any SSE route, any memory wiring, any live provider call
beyond the bounded unit-test mocks, any public-sync update, any release
claim, any freeze lift, or any Maika/child-data/photo/vision claim.
