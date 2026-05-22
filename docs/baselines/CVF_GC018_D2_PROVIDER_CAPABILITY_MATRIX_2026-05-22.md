# CVF GC-018 D2 Provider Capability Matrix

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_D2_PROVIDER_CAPABILITY_MATRIX

Date: 2026-05-22

## Source or Predecessor Evidence

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`

## Purpose / Decision / Baseline

Authorize D2, the provider capability matrix and method-contract hardening
phase after G1.

Decision: proceed with a bounded Model Gateway registry and deterministic
unsupported-method gate for the provider methods named by Review CVF.md:
`complete`, `stream`, `tool_call`, `reasoning`, `json_mode`, `vision`,
`embedding`, and `receipt`.

## Decision / Baseline / Proposed Tranche

Baseline: Model Gateway already has individual contracts for stream, vision,
reasoning, JSON mode, tool call, and embedding, plus a small provider-method
gate used by Alibaba stream and DeepSeek JSON mode adapters.

Gap: method support is scattered across files and does not expose one
machine-readable capability matrix that future devs/agents can inspect before
attempting provider behavior.

Proposed tranche: add a canonical capability registry, preserve legacy `chat`
compatibility as an alias of `complete`, and provide registry-backed positive
and negative gates.

## Scope / Proposed Tranche

In scope:

- expand Model Gateway provider method vocabulary to include the Review-CVF
  method axis;
- add a provider capability registry for currently bounded provider/model
  support;
- add owner references for `retry`, `cost`, and `risk` without treating them
  as provider methods;
- add registry lookup/list/assert helpers;
- prove unsupported methods fail deterministically before adapter calls;
- preserve existing adapter behavior.

Out of scope:

- new live provider execution semantics;
- new providers;
- all-provider parity;
- route changes;
- receipt-envelope changes;
- retry, cost, or risk ownership changes;
- public-sync, hosted readiness, Maika proof, or freeze release.

## Blocked-Work Override

`new_provider_execution_semantics` override: granted only for the provider
method taxonomy, capability registry, and pre-adapter unsupported-method gate.

This override does not authorize new live adapter calls, new route dispatch,
SSE route behavior, provider parity claims, or new provider methods beyond
contract/registry declaration and negative gating.

## Evidence / Required Evidence / Verification

Required evidence:

- registry tests proving the Review-CVF method axis;
- registry tests proving retry/cost/risk remain owner references;
- registry tests for supported Alibaba and DeepSeek methods;
- registry tests for unsupported method errors;
- existing provider method coverage tests still pass;
- Model Gateway TypeScript check passes;
- local governance hook chain passes before final commit.

Live provider proof:

- Not required for this D2 tranche because it does not claim new runtime
  provider behavior.
- If later work claims new runtime provider behavior, use a separate GC-018 and
  redacted live proof.

## Claim Boundary / Approval Gate

D2 closes only provider capability matrix and deterministic unsupported-method
behavior for the current private baseline. It does not claim all-provider
parity, broad provider stability, or runtime behavior for unsupported methods.
