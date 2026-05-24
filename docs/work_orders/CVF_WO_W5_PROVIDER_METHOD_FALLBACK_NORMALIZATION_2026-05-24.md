# CVF Work Order W5 Provider Method And Fallback Normalization

Memory class: SUMMARY_RECORD

Status: DISPATCHED_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION

Date: 2026-05-24

docType: work_order

---

## Purpose

Close WC-3 Candidate 5 with a bounded Model Gateway helper that makes provider
method support, fallback posture, provider failure class, and user action clear
before adapter calls or repeated live runs.

## Authority Chain

Authorized by:

- `docs/baselines/CVF_GC018_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION_2026-05-24.md`
- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`

Operator instruction: continue the roadmap in priority order, commit after
each completed part, and use live API keys only when live proof is required.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Orchestrator | Keep W5 contract-only and commit authorization/closure separately. |
| Legacy Source Extractor | Preserve only method/fallback/error concepts from the scanned provider sources. |
| Implementer | Add the local Model Gateway helper and focused tests. |
| QA | Run focused/full Model Gateway tests, TypeScript check, and session/docs guards. |
| Skeptic/Auditor | Reject broad provider-soak, OpenRouter runtime, and public-readiness claims. |
| Product/Operator Advocate | Ensure the result tells a user whether to retry, top up, add a key, or choose another method/provider. |
| Safety/Boundary Owner | Confirm no keys, raw prompts, proxy runtime, or hidden fallback are introduced. |

## Scope / Allowed Scope / Forbidden Scope

Allowed files:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-method-fallback-normalization.test.ts`
- W5 completion review, WC roadmap, session state, and handoff progress updates

Forbidden files/classes:

- provider adapters or OpenRouter runtime/command execution;
- `/api/execute`;
- `GovernanceEvidenceReceipt` envelope types;
- provider router behavior;
- proxy server or remote ingress;
- raw prompt/output logging;
- auth/RBAC;
- public-sync, hosted-readiness, production-readiness, or freeze-release surfaces.

## Required First Reads

- `docs/baselines/CVF_GC018_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- `docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`

Legacy first reads are enumerated in the W5 GC-018 control block.

## Pre-Flight Checks

- Confirm W4 is closed pass bounded.
- Confirm W5 GC-018 includes a CLEAR blind-spot control block.
- Confirm W5 does not require live provider proof because it is contract-only.
- Confirm any accidental live/API-key failure is diagnosed under the V3
  diagnostic standard before rerun.

## Write Ownership

Implementation ownership:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-method-fallback-normalization.test.ts`

Documentation ownership:

- W5 completion review
- WC roadmap status update
- active session state, front door, and handoff sync

## Execution Plan

Implement the bounded W5 contract helper in `EXTENSIONS/CVF_MODEL_GATEWAY`.

The helper must answer, without making a provider call:

1. Is the requested provider/model known?
2. Is the requested method supported after legacy alias normalization?
3. If the call failed, what secret-safe diagnostic class applies?
4. Is fallback or retry available under the existing fallback policy?
5. What user action should be taken: retry, choose supported method, add key,
   top up, change provider/model, inspect provider status, or stop?

## Execution Rules

- Reuse existing `ProviderCapabilityFile`, `FallbackPolicy`, and
  `classifyProviderExitCode` surfaces.
- Keep the helper deterministic and local.
- Do not introduce network calls, command execution, provider adapters,
  OpenRouter runtime integration, `/api/execute` changes, receipt-envelope
  fields, auth/RBAC changes, or public-sync changes.
- Do not treat `retry`, `cost`, or `risk` as provider methods.
- Preserve `chat` as a legacy alias for `complete`.
- Keep messages secret-safe and do not include raw provider output, API keys,
  prompts, or stack traces.

## Evidence Requirements

- focused W5 test file PASS;
- adjacent provider method/fallback/output tests PASS;
- full Model Gateway tests PASS;
- Model Gateway TypeScript check PASS;
- active session state/docs guards PASS;
- completion review records that live provider proof was not required.

## Acceptance Criteria

- [ ] Known provider/model and supported method returns a clear `ready` result.
- [ ] Unsupported method returns supported alternatives and does not authorize
      adapter execution.
- [ ] Missing provider/model is classified separately from unsupported method.
- [ ] Retryable HTTP status or provider exit class reports fallback/retry
      available only while attempts remain.
- [ ] Auth/config/insufficient-credit/quota style failures return non-retryable
      user actions.
- [ ] Health/quota/fallback posture is represented in one normalized result.
- [ ] Focused and full Model Gateway tests pass.
- [ ] Completion review records blind spots closed/still open and confirms
      live proof was not required for the contract-only claim.

## Review Gate

Reject W5 pass if:

- it executes a provider call, command, OpenRouter adapter, or proxy server;
- fallback is hidden or presented as provider reliability;
- unsupported methods can still look adapter-ready;
- retry/cost/risk are treated as provider methods;
- messages include raw secrets, prompts, output, stack traces, or API keys;
- closure claims provider stability, DeepSeek repair, public readiness, or
  production readiness.

## Closure Checklist

- [ ] Authorization commit created before implementation.
- [ ] W5 helper implemented and exported.
- [ ] Focused and adjacent tests PASS.
- [ ] Full Model Gateway tests and TypeScript check PASS.
- [ ] Completion review filed.
- [ ] WC roadmap/session/handoff updated.
- [ ] Final W5 closure commit created.

## Return-To-Orchestrator Conditions

Return instead of closing if:

- useful normalization requires provider runtime or route changes;
- fallback clarity requires receipt-envelope changes;
- OpenRouter runtime support becomes necessary;
- a live/API-key proof fails and cannot be diagnosed without expanding scope;
- the helper cannot remain secret-safe.

## Operator Checkpoint

operator.checkpoint.waiver: W5 is a local contract-only helper with no provider
execution, no new runtime authority, and no public claim expansion.

## Completion Evidence Required

- changed source and test file list;
- test/check commands and PASS counts;
- claim boundary;
- next candidate recommendation.

## Claim Boundary

This work order authorizes only local provider method/fallback/error clarity in
Model Gateway contracts. It does not authorize provider reliability claims,
DeepSeek rerun repair, OpenRouter support, runtime fallback execution, public
capability, production readiness, hosted readiness, or freeze release.
