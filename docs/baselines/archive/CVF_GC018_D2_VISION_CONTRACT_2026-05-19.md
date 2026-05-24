# CVF GC-018 D2 Vision Contract

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize D2 to add a vision contract definition to `CVF_MODEL_GATEWAY/src/`
and an optional `vision?()` stub to `LLMAdapter`. This closes the D2 provider
method parity gap at the contract level only — no provider implementation, no
live vision call, no image fetch.

The goal is to bring vision capability parity to the model gateway contract
layer, mirroring the stream-contract pattern that already exists.

## Scope

In scope:

- create `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts` (≤ 50 lines);
- export `VisionRequest`, `VisionContract`, `VisionCapableProvider`,
  `isVisionContract()`, `VISION_CONTRACT_REQUIRED_FIELDS`;
- add optional `vision?()` stub to `LLMAdapter` in
  `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
  (file stays ≤ 55 lines);
- export vision-contract types from `CVF_MODEL_GATEWAY/src/index.ts`;
- create `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-contract.test.ts`
  (≤ 60 lines, 5 tests);
- pass `npm test` and `npm run check` in `CVF_MODEL_GATEWAY`.

Out of scope:

- provider implementation (no OpenAI vision, no Anthropic vision call);
- routing or execution changes in cvf-web;
- D3 vision runtime or D4 reasoning (separate demand gates required);
- embedding contract (deferred, no demand gate yet);
- any public-sync repo edits under this baseline.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` — D2 section
- `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` — pattern to mirror exactly
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`

## Decision / Baseline / Proposed Tranche

Decision: implement D2 as contract definition only. The `isVisionContract()`
type guard and `VisionCapableProvider` interface establish the enforcement
surface. The optional `vision?()` stub on `LLMAdapter` marks the method as a
recognized capability without requiring implementation.

Selected pattern:

| File | Change |
|---|---|
| `vision-contract.ts` | New file — mirrors `stream-contract.ts` exactly |
| `llm.adapter.interface.ts` | Add optional `vision?()` stub (≤ 8 lines) |
| `index.ts` | Export vision-contract types and `isVisionContract` |
| `vision-contract.test.ts` | New test file — 5 tests for type guard |

## Rule

D2 may claim:

> CVF Model Gateway now defines a vision contract (`VisionRequest`,
> `VisionContract`, `VisionCapableProvider`) with a validated type guard
> (`isVisionContract`) and an optional `vision?()` stub on `LLMAdapter`.

D2 must not claim:

> live vision call, image fetch, provider implementation, Maika photo
> description, D3 runtime, D4 reasoning, or embedding contract.

## Claim Boundary

This baseline authorizes only the contract definition and type guard in
`CVF_MODEL_GATEWAY/src/` and the adapter stub in
`CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/`. It does not authorize any
provider execution, HTTP call, or runtime vision capability.

## Allowed And Forbidden Requirements

Allowed:

- define `VisionRequest`, `VisionContract`, `VisionCapableProvider` interfaces;
- implement `isVisionContract(value: unknown): value is VisionContract` type guard;
- export `VISION_CONTRACT_REQUIRED_FIELDS` constant;
- add optional `vision?()` stub to `LLMAdapter`;
- export vision-contract types from `index.ts`;
- write 5 unit tests for the type guard.

Forbidden:

- importing or calling any AI provider SDK (Anthropic, OpenAI, etc.);
- making any HTTP call or fetching image data;
- modifying the execute route or cvf-web;
- adding persistent memory or reinjection behavior;
- exceeding file line-count limits (vision-contract.ts ≤ 50,
  llm.adapter.interface.ts ≤ 55, vision-contract.test.ts ≤ 60).

## Exceptions

None. Any live vision call requires a separate D3 demand gate and GC-018.

## Enforcement Surface

Verification must include:

- `vision-contract.test.ts` with 5 tests passing (type guard pass/fail,
  `VisionCapableProvider` shape);
- `npm run check` PASS in `CVF_MODEL_GATEWAY`;
- `npm test` PASS (existing + 5 new tests);
- line count verification: `vision-contract.ts` ≤ 50, `llm.adapter.interface.ts`
  ≤ 55, `vision-contract.test.ts` ≤ 60.

## Evidence / Verification

Expected commands:

```powershell
npm test
npm run check
```

Run in:

```text
EXTENSIONS/CVF_MODEL_GATEWAY
```

## Claim / Final / Verification Boundary

Final boundary: D2 wires the vision contract definition and type guard into the
model gateway. Verification is limited to unit tests and TypeScript checks.
Provider execution, image handling, and D3/D4 capabilities are outside this
baseline.
