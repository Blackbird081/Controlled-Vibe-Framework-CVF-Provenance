# CVF GC-018 Lane D Provider Method Parity

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize Lane D to add the first bounded provider method parity surface:
a normalized stream envelope contract in `CVF_MODEL_GATEWAY` and a CLI
`--stream` request flag for the existing governed execute route caller.

## Scope

In scope:

- add `StreamContract` in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`;
- add the minimal `StreamRequest` and `StreamCapableProvider.stream()` contract
  beside the gateway provider-output contracts;
- export the new stream contract from `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`;
- wire `cvf execute --stream` through the governance CLI argument parser and
  execute POST body as `stream: true`;
- add `streamingEnabled: false` to the three governed pack
  `execution.policy.json` files so later lanes can enable streaming without a
  schema churn;
- prove the behavior with unit tests only.

Out of scope:

- live SSE implementation in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`;
- new providers, routing-policy changes, provider registry changes, reasoning,
  vision, or embedding contracts;
- public claims that streaming execution works end to end.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_D_PROVIDER_METHOD_PARITY_2026-05-19.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`

## Source-Fidelity Pass

The required grep found an existing `LLMAdapter.stream()` optional method in
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`.
That contract currently returns a full `LLMResponse` through an `onToken`
callback and is outside the Lane D write-ownership list.

Lane D therefore must not invent a second broad adapter taxonomy or rewrite
the Runtime Adapter Hub. The authorized implementation adds only a minimal
gateway-side stream contract:

- `StreamContract`
- `StreamRequest`
- `StreamCapableProvider.stream(request): AsyncIterable<StreamContract>`

This records the real source state while still creating the normalized
gateway envelope needed by the roadmap.

## Decision / Baseline / Proposed Tranche

Decision: implement Lane D as a contract-and-flag tranche.

The exact interface name is `StreamContract`. The exact method contract name is
`stream()` on the new minimal `StreamCapableProvider` type. The exact CLI flag
is `--stream`, parsed as a boolean and serialized into the execute request body
as `stream: true`.

Risk ceiling: R1, because this touches typed request contracts and governed
pack policy metadata but does not dispatch live provider streams.

## Rule

Lane D may claim:

> The gateway has a normalized stream envelope contract and `cvf execute
> --stream` can request streaming from the existing execute route caller.

Lane D must not claim:

> The web execute route streams SSE responses, providers implement streaming,
> or streaming is live-proven.

## Evidence / Verification

Required commands:

```powershell
npm test
npm run check
```

Run separately in:

```text
EXTENSIONS/CVF_MODEL_GATEWAY
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI
```

Repository guard:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

## Tranche Closure Checklist

- `StreamContract` exists and is exported.
- Existing `LLMAdapter.stream()` source finding is recorded.
- `--stream` is parsed as a boolean CLI flag.
- Execute POST body includes `stream: true` only when the flag is set.
- All three governed pack policies include `streamingEnabled: false`.
- Unit tests and TypeScript checks pass for touched packages.
- Current governance hook chain passes without bypassing hooks.

## Claim Boundary

This authorization closes only a defined, unit-tested stream contract and CLI
request flag. It does not authorize live streaming behavior or public
production streaming claims.
