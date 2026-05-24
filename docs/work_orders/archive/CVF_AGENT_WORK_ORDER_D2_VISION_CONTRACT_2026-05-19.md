# CVF Agent Work Order — D2: Vision Contract

Memory class: SUMMARY_RECORD

Status: CLOSED

GC-018 required: Yes — new enforcement surface in CVF_MODEL_GATEWAY.
GC-018 path: `docs/baselines/CVF_GC018_D2_VISION_CONTRACT_2026-05-19.md`

## Purpose

Add `vision-contract.ts` to `CVF_MODEL_GATEWAY/src/`, mirroring the
`stream-contract.ts` pattern exactly. Adds optional `vision?()` stub to
`LLMAdapter`. Closes the D2 provider method parity gap (contract definition
only; no provider implementation or live call).

## Authority Chain

`docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` — D2
section. GC-018 must be filed and accepted before implementation begins.

## Agent Roles

- **Orchestrator** — files GC-018; dispatches work order; accepts completion
  packet.
- **Worker** — implements all tasks in governance repo only; runs pre-flight
  before any code; files completion review upon closure.

## Scope

**Allowed scope:** `CVF_MODEL_GATEWAY` and `CVF_v1.7.3_RUNTIME_ADAPTER_HUB` only.

- New: `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts`
- New: `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-contract.test.ts`
- Modified: `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` — export vision-contract types
- Modified: `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts` — add `vision?()` stub

**Forbidden scope:**

- Provider implementation (no OpenAI vision, no Anthropic vision call)
- Routing or execution changes in cvf-web
- D3 (vision runtime), D4 (reasoning) — separate work orders
- Embedding contract — deferred, no demand gate yet
- Any public-sync repo edits under this WO

## Required First Reads

1. `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` (35 lines) — pattern
   to follow exactly
2. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` — current exports
3. `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
   (45 lines) — existing `stream?()` stub pattern
4. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/stream-contract.test.ts` — test pattern
5. Roadmap D2 section — done criterion, line count constraints

## Write Ownership

Worker owns: `vision-contract.ts`, `vision-contract.test.ts`, `index.ts`
export additions, `llm.adapter.interface.ts` stub addition. No other files.

## Pre-Flight Checks

Worker must verify before writing any code:

```text
1. Confirm CVF_MODEL_GATEWAY/src/stream-contract.ts exists (35 lines) — read it
2. Confirm CVF_MODEL_GATEWAY/src/vision-contract.ts does NOT exist yet
3. Confirm CVF_MODEL_GATEWAY/tests/vision-contract.test.ts does NOT exist yet
4. Confirm llm.adapter.interface.ts is 45 lines with stream?() stub but no vision?()
5. Confirm CVF_MODEL_GATEWAY/src/index.ts does not export vision-contract
```

## Execution Plan

Task 1 → Task 2 → Task 3 → Task 4 in sequence. Tests must pass before Task 4.

### Task 1 — `vision-contract.ts`

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts` (≤ 50 lines).

Pattern mirrors `stream-contract.ts` exactly:

```typescript
export interface VisionRequest {
  traceId: string;
  imageUrl?: string;
  imageBase64?: string;
  mimeType?: string;
  prompt: string;
  metadata?: Record<string, unknown>;
}

export interface VisionContract {
  description: string;
  confidence?: number;
  done: boolean;
  receiptObligation?: string;
}

export interface VisionCapableProvider {
  vision(request: VisionRequest): Promise<VisionContract>;
}

export const VISION_CONTRACT_REQUIRED_FIELDS = ["description", "done"] as const;

export function isVisionContract(value: unknown): value is VisionContract {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return false;
  }
  const candidate = value as Record<string, unknown>;
  return (
    typeof candidate.description === "string"
    && typeof candidate.done === "boolean"
    && (
      candidate.confidence === undefined
      || typeof candidate.confidence === "number"
    )
    && (
      candidate.receiptObligation === undefined
      || typeof candidate.receiptObligation === "string"
    )
  );
}
```

### Task 2 — `llm.adapter.interface.ts` stub

Add after `stream?()` stub in `LLMAdapter` (≤ 8 lines added; file stays ≤ 55 lines):

```typescript
  /**
   * Optional vision support — describes image content
   * If not implemented, adapter may throw NotImplementedError
   */
  vision?(request: LLMRequest & { imageUrl?: string; imageBase64?: string; mimeType?: string }): Promise<LLMResponse>
```

### Task 3 — Test file

Create `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-contract.test.ts` (≤ 60 lines).

Required test cases:

- `test_isVisionContract_passes_valid` — `{ description: "a cat", done: true }` → `true`
- `test_isVisionContract_passes_with_confidence` — adds `confidence: 0.9` → `true`
- `test_isVisionContract_fails_missing_description` — `{ done: true }` → `false`
- `test_isVisionContract_fails_missing_done` — `{ description: "a cat" }` → `false`
- `test_VisionCapableProvider_shape` — object implementing `vision()` method
  satisfies `VisionCapableProvider` type (TypeScript structural check via cast)

### Task 4 — `index.ts` export

Add to `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`:

```typescript
export type { VisionRequest, VisionContract, VisionCapableProvider } from "./vision-contract";
export { isVisionContract, VISION_CONTRACT_REQUIRED_FIELDS } from "./vision-contract";
```

Run `npm test` — all tests pass (existing + 5 new).
Run `npm run check` — must pass.

## Acceptance Criteria

- [ ] `vision-contract.ts` created (≤ 50 lines); `isVisionContract` type guard correct
- [ ] `vision-contract.test.ts` created (≤ 60 lines); all 5 tests PASS
- [ ] `llm.adapter.interface.ts` gains `vision?()` stub; file ≤ 55 lines
- [ ] `index.ts` exports vision-contract types
- [ ] `npm test` PASS (existing + 5 new tests)
- [ ] `npm run check` PASS
- [ ] No provider implementation, no HTTP call, no image fetch added

## Evidence Requirements

Completion review must include:

1. `npm test` output: all tests PASS including 5 new vision-contract tests.
2. `npm run check` output: PASS.
3. `vision-contract.ts` line count ≤ 50.
4. `vision-contract.test.ts` line count ≤ 60.
5. `llm.adapter.interface.ts` line count ≤ 55.
6. Confirmation: no provider implementation, no HTTP call, no image fetch.

## Review Gate

Orchestrator reviews completion packet. No closure without `npm test` PASS and
`npm run check` PASS with line counts verified.

## Closure Checklist

- [ ] GC-018 filed and accepted before implementation
- [ ] All acceptance criteria verified with evidence
- [ ] Completion review filed in CVF `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- `vision-contract.ts` would exceed 50 lines — report and stop
- `llm.adapter.interface.ts` would exceed 55 lines — report and stop
- `npm run check` fails after stub addition
- Any existing model gateway test breaks

## Target repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).
`EXTENSIONS/CVF_MODEL_GATEWAY/` and
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/` only.

## Claim Boundary

D2 covers contract definition and type guard only. It does not authorize
provider implementation, live vision call, Maika photo description, D3
runtime, D4 reasoning, or embedding contract. No provider execution is
claimed or authorized by this work order.
