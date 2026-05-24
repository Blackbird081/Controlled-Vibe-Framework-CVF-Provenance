# CVF Lane D Provider Method Parity Completion

Memory class: FULL_RECORD
Status: CLOSED - DEFINED AND UNIT TESTED

## Purpose

Close Lane D by defining the bounded stream contract surface in
`CVF_MODEL_GATEWAY` and wiring `cvf execute --stream` into the existing
governance CLI request body.

## Scope

Completed:

- added `StreamContract`, `StreamRequest`, and `StreamCapableProvider` in the
  model gateway;
- exported the stream contract from the gateway barrel;
- added `--stream` as a known boolean flag in the governance CLI parser;
- serialized `stream: true` into execute POST bodies when requested;
- added `streamingEnabled: false` to all three governed pack policy files;
- added unit tests for gateway stream contract shape and CLI stream flag
  behavior.

Not completed:

- live SSE streaming in the Next.js execute route;
- provider implementation of streaming;
- reasoning, vision, or embedding method parity;
- public claim upgrade.

## Source / Predecessor Evidence

- `docs/baselines/CVF_GC018_LANE_D_PROVIDER_METHOD_PARITY_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_D_PROVIDER_METHOD_PARITY_2026-05-19.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/stream-contract.test.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`

## Decision / Baseline / Proposed Tranche

Decision: Lane D is closed as a contract-and-flag tranche.

The source-fidelity pass found that `LLMAdapter.stream()` already exists in
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
with an `onToken` callback signature. Because that file is outside Lane D write
ownership and the existing method is already present, this tranche did not
rewrite the Runtime Adapter Hub. It added the smallest gateway-side
normalization contract needed for provider method parity:
`StreamCapableProvider.stream(request): AsyncIterable<StreamContract>`.

## Findings

The CLI argument parser already supported generic boolean flags, but without
an explicit `--stream` entry it could consume a following positional value.
Lane D records `stream` as a known boolean flag and proves
`execute --stream --template documentation` parses correctly.

The governed pack policies now include `streamingEnabled: false`. This is a
schema-ready field only; it does not enable route streaming.

## Risk / Corrective Action

Risk: readers may infer that the execute route streams responses.

Corrective action: `route.ts` was not modified, `streamingEnabled` is `false`,
and this packet explicitly limits the claim to a defined contract and request
flag.

## Evidence / Verification

Evidence trace:

- Claim: stream contract file and test exist.
- Command: `Test-Path "EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts";
  Test-Path "EXTENSIONS/CVF_MODEL_GATEWAY/tests/stream-contract.test.ts"`
- Result: both returned `True`.
- Key path: `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`
- Verdict: PASS.

Evidence trace:

- Claim: gateway barrel exports `StreamContract`.
- Command: `rg -n "StreamContract" EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- Result: `StreamContract` found in the export block.
- Key path: `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- Verdict: PASS.

Evidence trace:

- Claim: CLI parser recognizes `--stream` as a boolean flag.
- Command: `rg -n "stream" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts`
- Result: `const BOOLEAN_FLAGS = new Set(["stream"]);`
- Key path: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts`
- Verdict: PASS.

Evidence trace:

- Claim: governed pack policy exposes streaming readiness without enabling it.
- Command: `rg -n "streamingEnabled"
  EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json`
- Result: `streamingEnabled: false`.
- Key path:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json`
- Verdict: PASS.

Verification commands:

```powershell
npm test
```

Run in `EXTENSIONS/CVF_MODEL_GATEWAY`: 12 test files passed, 34 tests passed.

```powershell
npm run check
```

Run in `EXTENSIONS/CVF_MODEL_GATEWAY`: pass.

```powershell
npm test
```

Run in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`: 4 test files passed, 50 tests
passed.

```powershell
npm run check
```

Run in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`: pass.

Line-count check after implementation:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`: 157 lines.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`: 35 lines.
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts`: 65 lines.
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`: 189 lines.

## Recommendation

Lane D+1, if authorized, should reconcile the pre-existing Runtime Adapter Hub
callback-style `LLMAdapter.stream()` with the new gateway
`AsyncIterable<StreamContract>` envelope before any live SSE route work.

## Claim Boundary

Lane D may be described as:

> Stream method parity is defined at the gateway contract level and the
> governance CLI can request streaming with `--stream`.

Lane D must not be described as:

> The execute route streams live SSE responses or providers have implemented
> the standardized stream contract.
