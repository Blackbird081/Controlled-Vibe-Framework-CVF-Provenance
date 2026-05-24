# CVF Agent Work Order — W1: Provider Contract Completion

Memory class: SUMMARY_RECORD

Status: OPEN

GC-018 required: No — pure contract + type guard, gateway files only, no adapter interface
touch, no enforcement surface change. Same pattern as D2.

## Purpose

Add 4 missing provider method contracts to `CVF_MODEL_GATEWAY/src/`: `reasoning-contract.ts`,
`json-mode-contract.ts`, `tool-call-contract.ts`, `embedding-contract.ts`. Each file follows
the exact same pattern as `stream-contract.ts` and `vision-contract.ts`. Contract definition
only — no provider implementation, no runtime adapter interface touch.

Closes: Review CVF Problem D (partial — gateway contract slice D3–D6).

## Authority Chain

`docs/roadmaps/CVF_PHASE3_REVIEW_CLOSURE_ROADMAP_V2_2026-05-19.md` — W1 section.
No GC-018 required. Worker may begin after reading this work order and completing
the source-fidelity pre-flight below.

## Agent Roles

- **Orchestrator** — dispatches this work order; accepts completion packet.
- **Worker** — implements all tasks in `CVF_MODEL_GATEWAY` only; runs pre-flight
  before any code; files completion review upon closure.

## Scope

**Allowed scope:**

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/reasoning-contract.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/json-mode-contract.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/tool-call-contract.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/reasoning-contract.test.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/json-mode-contract.test.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/tool-call-contract.test.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/embedding-contract.test.ts` — CREATE
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` — MODIFY (add 4 export blocks)

**Forbidden scope:**

- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
  — BLOCKED by `new_provider_execution_semantics`; do NOT add any stubs
- Any provider implementation file
- Any live HTTP call or AI provider call
- Any file outside `CVF_MODEL_GATEWAY/`

## Write Ownership

Worker owns: all 4 contract files + 4 test files + `index.ts` export additions.
No other files.

## Execution Plan

Task 1 (reasoning-contract.ts) → Task 2 (json-mode-contract.ts) → Task 3 (tool-call-contract.ts) → Task 4 (embedding-contract.ts) → Task 5 (index.ts exports) → Task 6 (test files) in sequence.

## Required First Reads

1. `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` — the canonical pattern to mirror
2. `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts` — second reference pattern
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` — to understand current export structure
4. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-contract.test.ts` — test pattern to mirror
5. This work order — done criteria and invariants

## Source-Fidelity Pre-Flight (Worker must verify before writing)

```text
1. Confirm stream-contract.ts exists and is 35 lines
2. Confirm vision-contract.ts exists and is 40 lines
3. Confirm llm.adapter.interface.ts is 51 lines (generate, stream?, vision? only)
4. Confirm reasoning-contract.ts does NOT exist (would be a collision)
5. Confirm json-mode-contract.ts does NOT exist
6. Confirm tool-call-contract.ts does NOT exist
7. Confirm embedding-contract.ts does NOT exist
8. Confirm npm test currently passes (baseline before changes)
```

## Contract Specifications

Each contract follows the pattern: `Request` interface, `Contract` interface,
`CapableProvider` interface, `REQUIRED_FIELDS` const, `is<Name>Contract()` type guard.

### Task 1 — `reasoning-contract.ts`

```typescript
export interface ReasoningRequest {
  traceId: string;
  prompt: string;
  systemPrompt?: string;
  chainOfThought?: boolean;
  metadata?: Record<string, unknown>;
}

export interface ReasoningContract {
  reasoning: string;
  conclusion: string;
  done: boolean;
  receiptObligation?: string;
}

export interface ReasoningCapableProvider {
  reasoning(request: ReasoningRequest): Promise<ReasoningContract>;
}

export const REASONING_CONTRACT_REQUIRED_FIELDS = ["reasoning", "conclusion", "done"] as const;

export function isReasoningContract(value: unknown): value is ReasoningContract {
  // guard: reasoning string, conclusion string, done boolean, optional receiptObligation string
}
```

Line count target: ≤ 50 lines.

### Task 2 — `json-mode-contract.ts`

```typescript
export interface JsonModeRequest {
  traceId: string;
  prompt: string;
  schema?: Record<string, unknown>;
  metadata?: Record<string, unknown>;
}

export interface JsonModeContract {
  output: Record<string, unknown>;
  done: boolean;
  receiptObligation?: string;
}

export interface JsonModeCapableProvider {
  jsonMode(request: JsonModeRequest): Promise<JsonModeContract>;
}

export const JSON_MODE_CONTRACT_REQUIRED_FIELDS = ["output", "done"] as const;

export function isJsonModeContract(value: unknown): value is JsonModeContract {
  // guard: output is non-null object, done boolean, optional receiptObligation string
}
```

Line count target: ≤ 50 lines.

### Task 3 — `tool-call-contract.ts`

```typescript
export interface ToolCallRequest {
  traceId: string;
  prompt: string;
  tools: Array<{ name: string; description: string; parameters?: Record<string, unknown> }>;
  metadata?: Record<string, unknown>;
}

export interface ToolCallContract {
  toolName: string;
  arguments: Record<string, unknown>;
  done: boolean;
  receiptObligation?: string;
}

export interface ToolCallCapableProvider {
  toolCall(request: ToolCallRequest): Promise<ToolCallContract>;
}

export const TOOL_CALL_CONTRACT_REQUIRED_FIELDS = ["toolName", "arguments", "done"] as const;

export function isToolCallContract(value: unknown): value is ToolCallContract {
  // guard: toolName string, arguments non-null object, done boolean, optional receiptObligation string
}
```

Line count target: ≤ 50 lines.

### Task 4 — `embedding-contract.ts`

```typescript
export interface EmbeddingRequest {
  traceId: string;
  input: string | string[];
  model?: string;
  metadata?: Record<string, unknown>;
}

export interface EmbeddingContract {
  embeddings: number[][];
  dimensions: number;
  done: boolean;
  receiptObligation?: string;
}

export interface EmbeddingCapableProvider {
  embedding(request: EmbeddingRequest): Promise<EmbeddingContract>;
}

export const EMBEDDING_CONTRACT_REQUIRED_FIELDS = ["embeddings", "dimensions", "done"] as const;

export function isEmbeddingContract(value: unknown): value is EmbeddingContract {
  // guard: embeddings is array, dimensions is number, done boolean, optional receiptObligation string
}
```

Line count target: ≤ 50 lines.

### Task 5 — Export from `index.ts`

Add 4 export blocks to `index.ts` following the exact pattern of the existing
`stream-contract` and `vision-contract` export blocks:

```typescript
export type {
  ReasoningCapableProvider,
  ReasoningContract,
  ReasoningRequest,
} from "./reasoning-contract";
export {
  isReasoningContract,
  REASONING_CONTRACT_REQUIRED_FIELDS,
} from "./reasoning-contract";
// ... repeat for json-mode, tool-call, embedding
```

### Task 6 — Test files (one per contract)

Each test file mirrors `vision-contract.test.ts` pattern (4–5 tests, ≤ 60 lines):

- minimal valid object passes type guard
- optional metadata field passes
- missing required field fails type guard
- done=false still passes (done is boolean, not must-be-true)
- wrong type on required field fails

## Acceptance Criteria

- [ ] `reasoning-contract.ts` created (≤ 50 lines), exports `ReasoningRequest`, `ReasoningContract`, `ReasoningCapableProvider`, `REASONING_CONTRACT_REQUIRED_FIELDS`, `isReasoningContract`
- [ ] `json-mode-contract.ts` created (≤ 50 lines), exports `JsonModeRequest`, `JsonModeContract`, `JsonModeCapableProvider`, `JSON_MODE_CONTRACT_REQUIRED_FIELDS`, `isJsonModeContract`
- [ ] `tool-call-contract.ts` created (≤ 50 lines), exports `ToolCallRequest`, `ToolCallContract`, `ToolCallCapableProvider`, `TOOL_CALL_CONTRACT_REQUIRED_FIELDS`, `isToolCallContract`
- [ ] `embedding-contract.ts` created (≤ 50 lines), exports `EmbeddingRequest`, `EmbeddingContract`, `EmbeddingCapableProvider`, `EMBEDDING_CONTRACT_REQUIRED_FIELDS`, `isEmbeddingContract`
- [ ] All 4 contracts exported from `index.ts`
- [ ] 4 test files (≤ 60 lines each), 4–5 tests each, all PASS
- [ ] `llm.adapter.interface.ts` line count = 51 (unchanged — grep proof required)
- [ ] `npm test` PASS (all existing + new)
- [ ] `npm run check` PASS

## Evidence Requirements

Completion review must include:

1. `npm test` output — all tests PASS including new (show test count before and after)
2. `npm run check` output — PASS
3. Line count for each new contract file (wc -l or equivalent)
4. `wc -l EXTENSIONS/CVF_MODEL_GATEWAY/src/llm.adapter.interface.ts` = 51 (unchanged)
5. Confirmation: no provider implementation in any new file (no fetch, no HTTP, no AI SDK import)

## Review Gate

Orchestrator reviews completion packet. No closure without:

- All 4 contracts + test files created and within line limits
- `llm.adapter.interface.ts` line count = 51 (unchanged — confirmed by grep)
- `npm test` PASS (all existing + new)
- `npm run check` PASS
- No provider implementation in any new file (confirmed by grep — no fetch, no HTTP)

## Closure Checklist

- [ ] GC-018 not required — confirmed no enforcement surface change
- [ ] `reasoning-contract.ts` created ≤ 50 lines
- [ ] `json-mode-contract.ts` created ≤ 50 lines
- [ ] `tool-call-contract.ts` created ≤ 50 lines
- [ ] `embedding-contract.ts` created ≤ 50 lines
- [ ] All 4 contracts exported from `index.ts`
- [ ] 4 test files created (≤ 60 lines each), all PASS
- [ ] `llm.adapter.interface.ts` NOT modified (51 lines, confirmed)
- [ ] `npm test` PASS
- [ ] `npm run check` PASS
- [ ] Completion review filed in CVF `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- Any contract file would exceed 50 lines — report and stop
- `llm.adapter.interface.ts` needs to be modified for any reason — stop; it is blocked
- `npm test` baseline fails before changes (pre-existing failure must be reported)
- `npm run check` fails after additions (type error in index.ts exports)

## Target Repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).
`EXTENSIONS/CVF_MODEL_GATEWAY/` only.

## Claim Boundary

W1 covers 4 gateway contract files (reasoning, json_mode, tool_call, embedding) and
their exports. It does not add adapter interface stubs, provider implementations,
live AI calls, or any enforcement surface change.
