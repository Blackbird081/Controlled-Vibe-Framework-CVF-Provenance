# CVF D2 Vision Contract Completion

Memory class: FULL_RECORD

Status: CLOSED

Reviewer / Worker: Codex

Date: 2026-05-19

---

## Purpose

Record implementation and verification evidence for D2: add a vision provider
contract and optional adapter stub without provider implementation.

---

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-contract.test.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`

Out of scope:

- Provider implementation.
- HTTP/image fetch.
- Vision runtime routing.
- Maika photo description.
- D3/D4 reasoning or embedding work.

---

## Target / Source Under Review

Work order:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_D2_VISION_CONTRACT_2026-05-19.md`

Roadmap:

- `docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md`

---

## Scope / Methodology

Method:

1. Mirrored the existing `stream-contract.ts` pattern.
2. Added `VisionRequest`, `VisionContract`, `VisionCapableProvider`, required
   field constant, and `isVisionContract()`.
3. Added optional `vision?()` to `LLMAdapter`.
4. Exported the contract from `CVF_MODEL_GATEWAY/src/index.ts`.
5. Added five focused tests for shape acceptance/rejection and provider type.

---

## Findings / Position

Position: D2 is implemented and locally verified.

Findings:

1. Contract file is 40 lines, under the 50-line limit.
2. Test file is 46 lines, under the 60-line limit.
3. Adapter interface is 51 lines, under the 55-line limit.
4. No provider name, `fetch(`, or HTTP/image retrieval was added in the new
   vision contract/test files.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Contract change accidentally implies runtime support | Claim boundary states contract-only; no provider implementation added |
| Type guard accepts malformed envelopes | Tests cover missing description, missing done, and bad confidence type |
| Adapter stub breaks downstream type check | `npm run check` passed |

---

## Evidence / Verification

### Model Gateway Tests

Command:

```powershell
npm test
```

Run in:

```text
EXTENSIONS/CVF_MODEL_GATEWAY
```

Result:

```text
Test Files  13 passed (13)
Tests       39 passed (39)
tests/vision-contract.test.ts  (5 tests)
```

Verdict: PASS.

### Type Check

Command:

```powershell
npm run check
```

Run in:

```text
EXTENSIONS/CVF_MODEL_GATEWAY
```

Result:

```text
tsc -p tsconfig.json --noEmit
```

Verdict: PASS.

### Line Counts And Static Audit

Commands:

```powershell
(Get-Content src/vision-contract.ts).Count
(Get-Content tests/vision-contract.test.ts).Count
(Get-Content contracts/llm.adapter.interface.ts).Count
rg -n "fetch\\(|openai|anthropic|dashscope|deepseek|alibaba" src/vision-contract.ts tests/vision-contract.test.ts
```

Results:

```text
40
46
51
no matches
```

Verdict: PASS.

---

## Acceptance Criteria

| Criterion | Status | Evidence |
| --- | --- | --- |
| `vision-contract.ts` created <= 50 lines | PASS | 40 lines |
| `vision-contract.test.ts` created <= 60 lines | PASS | 46 lines, 5 tests |
| `LLMAdapter` gains optional `vision?()` and stays <= 55 lines | PASS | 51 lines |
| `index.ts` exports vision contract | PASS | Export block added |
| `npm test` passes | PASS | 39 tests |
| `npm run check` passes | PASS | `tsc` PASS |
| No provider implementation or HTTP/image fetch | PASS | Static audit no matches |

---

## Decision / Recommendation / Disposition

Disposition: **CLOSED**.

D2 closes provider-method parity at the contract/type level only.

---

## Claim Boundary

D2 may be described as:

> CVF Model Gateway now defines and exports a typed vision contract with an
> optional adapter stub and passing local tests.

D2 must not be described as:

> live vision runtime, provider vision support, image fetching, Maika photo
> summary support, or embedding/reasoning implementation.
