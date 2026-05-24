# CVF GC-018 W5 Provider Method And Fallback Normalization

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION

docType: baseline

Date: 2026-05-24

---

## Source Or Predecessor Evidence

- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`
- `docs/baselines/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- `.private_reference/legacy/CVF 16.5/freellmapi/`
- `.private_reference/legacy/CVF 16.5/free Claude Code/`
- `.private_reference/legacy/CVF ADD/openrouter-cli.git/`

## Purpose / Decision / Baseline / Proposed Tranche

Authorize W5, the next ranked WC-3 candidate, as a bounded Model Gateway
contract tranche that makes provider method support, fallback posture, and
provider failure class legible before any repeated live run or adapter call.

Baseline: D2 already delivered a provider capability registry and deterministic
unsupported-method error. V3 and W4 established that live/provider failures
must be classified clearly. The remaining D pain point is that a caller can
still see fragmented signals: unsupported method, fallback decision, exit code,
health, or quota class are not normalized into one secret-safe pre-runtime
evaluation.

Decision: add a local Model Gateway normalization helper and tests. Keep it
contract-only. Do not add provider runtime behavior, new adapters, route
dispatch, live provider soak, receipt-envelope fields, auth/RBAC, public-sync,
or production-readiness claims.

## Decision / Baseline / Proposed Tranche

Decision: proceed with W5 as a contract-only Model Gateway tranche.

Baseline: D2 owns the provider capability registry and unsupported-method
gate. W5 does not replace that registry; it composes the existing signals into
a clearer pre-runtime result.

Proposed tranche: add one deterministic W5 helper that evaluates known
provider/model/method support, classifies provider failure inputs when present,
summarizes fallback/retry posture, and returns a secret-safe user action.

## Knowledge Absorption Blind-Spot Control Block

- Standard read: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF 16.5/freellmapi/` - 10 files
  - `.private_reference/legacy/CVF 16.5/free Claude Code/` - 7 files
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/` - 23 files
- Prior absorption evidence resolved:
  - `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  - `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
  - `docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`
  - `docs/baselines/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- Detailed source files used:
  - `.private_reference/legacy/CVF 16.5/freellmapi/FREELLMAPI_MAPPING.md`
  - `.private_reference/legacy/CVF 16.5/freellmapi/fallback.policy.ts`
  - `.private_reference/legacy/CVF 16.5/freellmapi/provider.health.ts`
  - `.private_reference/legacy/CVF 16.5/freellmapi/gateway.receipt.ts`
  - `.private_reference/legacy/CVF 16.5/freellmapi/provider.registry.ts`
  - `.private_reference/legacy/CVF 16.5/freellmapi/quota.ledger.ts`
  - `.private_reference/legacy/CVF 16.5/freellmapi/routing.policy.ts`
  - `.private_reference/legacy/CVF 16.5/freellmapi/sticky.session.ts`
  - `.private_reference/legacy/CVF 16.5/freellmapi/credential.vault.ts`
  - `.private_reference/legacy/CVF 16.5/free Claude Code/ANTHROPIC_OPENAI_COMPAT_MAPPING.md`
  - `.private_reference/legacy/CVF 16.5/free Claude Code/PROVIDER_PROTOCOL_TRANSLATOR.md`
  - `.private_reference/legacy/CVF 16.5/free Claude Code/CONTROLLED_PROVIDER_ROUTING_POLICY.md`
  - `.private_reference/legacy/CVF 16.5/free Claude Code/MODEL_GATEWAY_AUDIT_TRACE.md`
  - `.private_reference/legacy/CVF 16.5/free Claude Code/MODEL_GATEWAY_PROXY_ADAPTER.md`
  - `.private_reference/legacy/CVF 16.5/free Claude Code/PROXY_SECURITY_BOUNDARY.md`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/model_gateway/providers/openrouter/openrouter.contract.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/model_gateway/providers/openrouter/openrouter.capability.map.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/model_gateway/providers/openrouter/openrouter.error.map.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/model_gateway/providers/openrouter/openrouter.config.doctor.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/model_gateway/providers/openrouter/openrouter.adapter.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/pipeline/policies/openrouter_retry.policy.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/command_runtime/contracts/openrouter_cli.exit_codes.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/command_runtime/contracts/openrouter_cli.stdout_policy.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/governance/w7_integration/decision/openrouter_provider_decision.policy.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/governance/w7_integration/trace_records/openrouter_trace.mapper.ts`
  - `.private_reference/legacy/CVF ADD/openrouter-cli.git/governance/w7_integration/runtime_records/openrouter_runtime.record.ts`
- Source families skipped:
  - `.private_reference/legacy/CVF ADD/cortex-hub/` - secondary provider/tool source; deferred because W5 targets existing Model Gateway method/fallback clarity, not MCP/code-intelligence bridge implementation.
- File-level accepted value:
  - `freellmapi/fallback.policy.ts` -> retryable status and max-attempt fallback posture
  - `freellmapi/provider.health.ts` -> health states should affect fallback clarity
  - `freellmapi/quota.ledger.ts` -> quota denial must be distinct from provider failure
  - `free Claude Code/ANTHROPIC_OPENAI_COMPAT_MAPPING.md` -> unsupported capability must be explicit, not silently dropped
  - `free Claude Code/CONTROLLED_PROVIDER_ROUTING_POLICY.md` -> fallback must disclose provider/model substitution and never reduce safety
  - `free Claude Code/MODEL_GATEWAY_AUDIT_TRACE.md` -> provider call failures need traceable status/error class
  - `openrouter.error.map.ts` and `openrouter_cli.exit_codes.ts` -> normalize auth/config/rate-limit/timeout/contract/provider classes
  - `openrouter_retry.policy.ts` -> retry/fallback should be allowed only for retryable classes while budget remains
- Owner-surface normalization:
  - method support -> `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts`
  - fallback posture -> `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts`
  - provider failure class -> `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`
  - registry/capability truth -> `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
  - W5 helper surface -> `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts`
- Accept/defer/reject matrix:
  - provider method/fallback/error normalization -> `ACCEPT_NOW`; reduces unclear provider failures without runtime broadening
  - OpenRouter CLI adapter execution -> `DEFER_DEMAND_GATED`; valuable but would add external command/runtime behavior
  - proxy adapter ingress/server -> `DEFER_DEMAND_GATED`; high-risk boundary and not needed for W5
  - third-party proxy routing -> `REJECT_DIRECT`; must remain denied/default-gated
  - hidden model substitution/fallback -> `REJECT_DIRECT`; contradicts CVF transparency boundary
  - raw prompt/output logging -> `REJECT_DIRECT`; secret and privacy risk
- Adversarial roles completed:
  - Implementer: smallest useful proof is a deterministic helper that combines method support, fallback budget, status/exit class, and safe user action.
  - Skeptic/Auditor: the main overclaim risk is calling this provider stability or adding OpenRouter runtime; both remain out of scope.
  - Product/Operator Advocate: the user pain reduced is "the system failed but I do not know why or whether rerun helps."
  - Safety/Boundary Owner: no provider keys, raw prompts, proxy servers, runtime tool execution, hidden fallback, or new provider calls may be introduced.
- Thin proof target:
  - focused Model Gateway tests showing supported method, unsupported method, retryable fallback, non-retryable auth/config, quota/health distinctions, and secret-safe messages.
- Blind-spot verdict: CLEAR

## Scope / Proposed Tranche

In scope:

- add a local provider method/fallback normalization helper in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src`;
- expose secret-safe diagnostic class, retryability, fallback availability,
  user action, and human-readable message;
- reuse existing provider capability registry, method gate, fallback policy,
  and provider output exit-code classifier;
- add focused tests and export the helper from Model Gateway.

Out of scope:

- live provider execution;
- new provider adapters or OpenRouter runtime execution;
- `/api/execute` route changes;
- receipt-envelope fields;
- provider router behavior changes;
- proxy server or remote ingress;
- raw prompt/output logging;
- auth/RBAC changes;
- public-sync;
- hosted readiness, production readiness, freeze release, or broad provider
  stability claim.

## Required Evidence / Verification

- focused W5 tests for the new helper pass;
- adjacent provider method/fallback/output tests pass;
- full Model Gateway tests pass;
- Model Gateway TypeScript check passes;
- active session state/docs guards pass;
- live provider proof is not required because W5 is contract-only and does not
  claim new runtime provider behavior.

If any live/API-key command is run despite this boundary, it must follow
`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`.

## Claim Boundary / Approval Gate

W5 may claim only provider method/fallback/error clarity in local Model Gateway
contracts. It does not claim provider reliability, successful DeepSeek rerun,
OpenRouter support, runtime fallback execution, public capability, production
readiness, hosted readiness, or freeze release.
