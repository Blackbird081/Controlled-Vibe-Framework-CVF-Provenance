# CVF Adjustment 1 Inventory — Problem D: Provider Method Parity

Memory class: SUMMARY_RECORD

Status: FILED — 2026-05-19. Pre-GC-018 factual inventory per
`docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
Adjustment 1 requirement.

## Purpose

Record the factual pre-GC-018 inventory for Problem D so Lane D starts from
existing provider gateway infrastructure instead of replacing it.

## Source

- `docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` §
  Adjustment 1 + corrected Problem D
- Live scan of `EXTENSIONS/CVF_MODEL_GATEWAY/src/` performed 2026-05-19
  by coordinating agent (Claude)

## Scope / Target / Owner Boundary

Scope: Problem D only — Provider Method Parity. Covers what already
exists in `CVF_MODEL_GATEWAY` before Lane D GC-018 is filed.
Owner: Claude (reviewer role) per Adjustment 1 instruction.

## Findings

### What already exists

**`CVF_MODEL_GATEWAY` — source files:**

| File | Lines | Role |
|---|---|---|
| `src/provider-output-contract.ts` | 151 | `ProviderJsonEnvelope`, `ProviderStreamChunk`, `ProviderExitClassification`, `ProviderStdoutPolicy`; `parseProviderNdjsonStream()` at line 92 |
| `src/routing-policy.ts` | 104 | Provider selection logic; routing rules |
| `src/fallback-policy.ts` | 54 | Fallback chain on provider failure |
| `src/gateway-receipt.ts` | 96 | `GatewayReceipt` envelope — wraps provider response with governance metadata |
| `src/gateway-policy.ts` | 18 | Policy composition |
| `src/provider-registry.ts` | 113 | Provider registration, lookup |
| `src/provider-health.ts` | 74 | Health check per provider |
| `src/credential-boundary.ts` | 51 | API key boundary enforcement |
| `src/quota-ledger.ts` | 102 | Per-provider quota tracking |
| `src/sticky-session.ts` | 52 | Session affinity to a provider |
| `src/index.ts` | 147 | Exports for all of the above |

**Existing stream-related types:**

- `ProviderStreamChunk` (line 21 of `provider-output-contract.ts`):
  defined but is a low-level output envelope, not a standardized
  cross-provider stream contract.
- `parseProviderNdjsonStream()` (line 92): parses NDJSON stdout into
  `ProviderStreamChunk[]` — for local subprocess output, not for HTTP SSE.

**Tests:** 11 test files covering all 10 non-index source files plus
one integration test (`model-gateway-runtime.integration.test.ts`).

**No `LLMAdapter` interface found.** No `stream()`, `reasoning()`,
`vision()`, or `embedding()` method defined at the gateway level. The
gateway has routing and receipt infrastructure but no standardized
method-level contract across providers.

### What the actual gap is

`CVF_MODEL_GATEWAY` has robust routing, fallback, receipt, quota, and
credential infrastructure. The gap is that **provider method-level
contracts are not standardized**: there is no `StreamContract` interface
defining the normalized stream envelope (chunk, role, done, receipt
obligation), and no `stream()` stub on a gateway adapter interface.
The existing `ProviderStreamChunk` covers subprocess NDJSON output only.

### What "done" looks like for the next tranche

Lane D acceptance criterion: `StreamContract` interface created in
`CVF_MODEL_GATEWAY/src/stream-contract.ts` with fields `chunk`, `role`,
`done`, optional `receiptObligation`; exported from `index.ts`; `stream()`
stub added to provider adapter interface; `--stream` flag wired in CLI
`arg.parser.ts` and `execute.client.ts`. Confirmed by unit tests.

## Risk

None. Read-only inventory. No code changed.
`ProviderStreamChunk` must NOT be replaced — Lane D adds a new
`StreamContract` alongside it, not instead of it.

## Decision / Recommendation / Disposition

Problem D: **GAP CONFIRMED** — existing `ProviderStreamChunk` covers
subprocess NDJSON only; cross-provider `StreamContract` does not exist.
Lane D work order authorized to create it.
`docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_D_PROVIDER_METHOD_PARITY_2026-05-19.md`

## Claim Boundary

This packet is read-only inventory evidence. It does not authorize live SSE
implementation, provider registration changes, or public method-parity claims.
