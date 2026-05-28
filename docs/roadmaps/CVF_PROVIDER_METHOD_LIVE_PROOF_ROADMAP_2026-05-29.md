# CVF Provider Method Live Proof Roadmap

Memory class: SUMMARY_RECORD

Status: DEMAND_GATED

docType: roadmap

Date: 2026-05-29

---

## Purpose

Define the evidence-collection scope needed to close CVF 25.05 Gap 3 and
prove provider method contracts live (json_mode, tool_call, streaming,
embedding, reasoning_contract). This roadmap is a planning record only.
No tranche may begin without explicit operator authorization and a fresh GC-018.

## Source

- CVF 25.05 Gop_y.md: `.private_reference/legacy/CVF 25.05/Gop_y.md` — Gap 3
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 3 section: "Effort: requires live provider runs with quota. Medium risk."
- W5 `ProviderMethodFallbackEvaluation`: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts`
- Provider capability registry: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts`

## Why This Roadmap Exists

W5 delivered provider method fallback normalization (schema + contract). D-wave
proved `complete` method on DeepSeek + OpenAI. But `json_mode`, `tool_call`,
`streaming`, `embedding`, `reasoning_contract` have no live receipt evidence.

CVF currently claims these method contracts are `schema_defined` — this roadmap
closes them to `proven` by collecting live evidence packets per method per
provider.

## Scope

Each sub-tranche = one method × one or more providers = one evidence packet:

```
docs/evidence/provider-methods/
  json-mode/
    alibaba-qwen-turbo.md     ← PM-1
    deepseek-chat.md          ← PM-1
  tool-call/
    alibaba-qwen-turbo.md     ← PM-2
  streaming/
    alibaba-qwen-turbo.md     ← PM-3
  embedding/                  ← PM-4 (demand-gated separately)
  reasoning-contract/         ← PM-5 (demand-gated separately)
```

### PM-1 — JSON Mode Evidence Packets (Priority: HIGH)

**Gap:** `json_mode` method contract in W5 schema; no live proof.

**What to collect per packet:**
- provider/model
- method tested: `json_mode`
- input payload (schema-constrained JSON request)
- CVF policy applied (risk level, guard contract result)
- output validation (response matches schema)
- receipt id
- limitation notes
- PASS/FAIL

**Providers to test:** Alibaba qwen-turbo + DeepSeek deepseek-chat (both have
`json_mode` in PROVIDER_CAPABILITY_REGISTRY).

**Risk class:** R1 — live provider call, existing API keys.

**Prerequisites:** Fresh GC-018; API keys available (Alibaba + DeepSeek).

---

### PM-2 — Tool Call Evidence Packets (Priority: HIGH)

**Gap:** `tool_call` method contract schema-defined; no live proof.

**What to collect:** Same packet structure as PM-1 but for `tool_call` method
— send a tool-definition payload, validate the provider returns a tool-call
response, capture receipt.

**Risk class:** R1.

**Prerequisites:** PM-1 CLOSED_PASS; fresh GC-018.

---

### PM-3 — Streaming Evidence Packets (Priority: MEDIUM)

**Gap:** `streaming` method contract schema-defined; no live proof. Alibaba
qwen-turbo has `stream` in `supportedMethods`.

**What to collect:** SSE stream response capture; first-token latency; receipt
with `evidenceMode=live`.

**Risk class:** R1 — streaming response handling; no new route changes needed.

**Prerequisites:** PM-1 CLOSED_PASS; fresh GC-018.

---

### PM-4 — Embedding Evidence Packets (Priority: LOW, DEMAND_GATED)

**Gap:** Embedding method not yet in active provider registry.

**Unlock:** Operator names a concrete embedding use case or provider with
embedding support. No ceremony beyond that.

---

### PM-5 — Reasoning Contract Evidence (Priority: LOW, DEMAND_GATED)

**Gap:** `reasoning_contract` (Qwen3 thinking models) partially proven via D10
receipt `rcpt-env-mpigxtmn-pml5ky`, but no structured evidence packet in
`docs/evidence/provider-methods/reasoning-contract/`.

**What to collect:** Formalize D10 proof into structured packet; add
`enable_thinking=true` model behavior boundary note.

**Unlock:** After PM-1/PM-2/PM-3 all CLOSED_PASS.

---

## CVF 25.05 Gap 3 Closure Condition

Gap 3 will be closed when PM-1 + PM-2 + PM-3 are all CLOSED_PASS with live
receipts in `docs/evidence/provider-methods/`. PM-4/PM-5 remain demand-gated
but do not block Gap 3 closure.

- [ ] PM-1 json_mode: Alibaba + DeepSeek evidence packets
- [ ] PM-2 tool_call: at least 1 provider evidence packet
- [ ] PM-3 streaming: at least 1 provider evidence packet
- [ ] PM-4 embedding: DEMAND_GATED
- [ ] PM-5 reasoning-contract: DEMAND_GATED (D10 receipt already exists as partial proof)

## Sequencing

```
PM-1 (json_mode) → PM-2 (tool_call) → PM-3 (streaming)
PM-4 / PM-5 demand-gated independently
```

## Unlock Conditions

- Operator authorizes PM-1
- API keys available (Alibaba + DeepSeek — confirmed available)
- LHW12/LHW13 not required as prerequisites (can run in parallel)
- Fresh GC-018 per sub-tranche

## Authorization / Decision

Status: DEMAND_GATED. Operator must authorize PM-1 and issue a fresh GC-018
before any sub-tranche begins. LHW12/LHW13 completion is not a prerequisite
— PM-1/PM-2/PM-3 can run in parallel with LHW waves.

## Non-Goals

- Broad provider stability claims (PM evidence is bounded per method per provider)
- New provider adapters or route behavior changes
- Embedding or reasoning_contract proof before PM-1/PM-2/PM-3 close
- Claiming CVF supports all provider methods before each has a live receipt

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| PM-1 | json_mode evidence packets (Alibaba + DeepSeek) | Operator authorization + fresh GC-018 |
| PM-2 | tool_call evidence packet (1+ provider) | PM-1 CLOSED_PASS |
| PM-3 | streaming evidence packet (1+ provider) | PM-1 CLOSED_PASS |
| PM-4 | embedding evidence packet | DEMAND_GATED separately |
| PM-5 | reasoning_contract formal packet | DEMAND_GATED separately |

## Acceptance Criteria

PM-1: 2 evidence packets (Alibaba + DeepSeek) with live receipts in
`docs/evidence/provider-methods/json-mode/`; `evidenceMode=live`; PASS/FAIL
documented; GC-018 + work order + completion review; governance gates PASS.

PM-2: 1+ evidence packet in `docs/evidence/provider-methods/tool-call/`.

PM-3: 1+ evidence packet in `docs/evidence/provider-methods/streaming/`.

Gap 3 closure: PM-1 + PM-2 + PM-3 all CLOSED_PASS.

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base <pre-PM-commit> --head <PM-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base <pre-PM-commit> --head <PM-commit> --enforce
```

## Claim Boundary

This roadmap is a planning record. It does not authorize implementation and
does not claim any provider method is currently proven beyond what D-wave
evidence already supports.
