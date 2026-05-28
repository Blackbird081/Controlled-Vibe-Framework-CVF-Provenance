# CVF Work Order D2 Provider Capability Matrix

Memory class: FULL_RECORD

Status: CLOSED_D2_PROVIDER_CAPABILITY_MATRIX

Date: 2026-05-22

## Purpose

Implement the D2 provider capability matrix and method-contract hardening
authorized by GC-018.

## Authority Chain

- Original source oracle: `.private_reference/legacy/CVF 17.05/Review CVF.md`
- Post-B/C assessment:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- Roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- G1 completion:
  `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- GC-018:
  `docs/baselines/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`

## Agent Roles

- Orchestrator: Codex
- Implementer: Codex
- Reviewer: Codex, via tests and completion review
- Auditor: Codex, via completion packet and governance hooks

## Scope / Allowed Scope / Forbidden Scope

Allowed:

- update Model Gateway provider method contract types;
- add a provider capability registry;
- add registry-backed list/lookup/assert helpers;
- update existing Alibaba and DeepSeek capability literals for `complete`;
- add focused registry tests and update existing method tests;
- file completion documentation.

Forbidden:

- new live provider calls;
- new adapter runtime behavior;
- route or `/api/execute` changes;
- receipt-envelope changes;
- provider parity claims;
- retry/cost/risk ownership changes;
- public-sync or hosted-readiness work.

## Required First Reads

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-method-coverage.test.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts`

## Pre-Flight Checks

- Confirm D2 is bounded to Model Gateway contract/registry/gate behavior.
- Confirm no `/api/execute` route behavior is changed.
- Confirm no new live provider adapter behavior is introduced.
- Confirm `retry`, `cost`, and `risk` stay at existing owner surfaces.
- Confirm live proof is not required because D2 makes no new runtime provider
  behavior claim.

## Write Ownership

Primary write scope:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
- existing provider method coverage tests
- completion documentation and session state

## Execution Plan / Execution Rules

1. Expand the provider method vocabulary.
2. Add canonical registry and owner references.
3. Add registry lookup/list/assert helpers.
4. Preserve legacy `chat` compatibility as alias for `complete`.
5. Update focused provider capability tests.
6. Run targeted and full Model Gateway checks.
7. File completion review and commit D2.

## Acceptance Criteria

- The registry exposes the eight Review-CVF provider methods.
- `retry`, `cost`, and `risk` are owner references, not provider methods.
- Alibaba `qwen-turbo` and DeepSeek `deepseek-chat` have registry contracts.
- Unsupported methods throw `UnsupportedMethodError` deterministically.
- Existing adapter tests still pass.
- No new live provider behavior is claimed.

## Evidence Requirements

- Focused registry and provider-method tests pass.
- Full Model Gateway tests pass.
- Model Gateway TypeScript check passes.
- Local governance hook chain passes before commit.

## Review Gate

Completion review must state whether D2 is closed, partial, or failed, and must
include exact tests run.

## Closure Checklist / Completion Requirements

- [x] Contract types updated.
- [x] Registry added.
- [x] Registry gate helpers added.
- [x] Tests updated.
- [x] Completion review filed.
- [x] Commit created for D2 phase.

Completion review:

`docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`

## Operator Checkpoint

operator.checkpoint.waiver: Operator already authorized Codex to proceed
through the six remaining phases in priority order and to use API keys when
needed; D2 does not require live key usage because it makes no new runtime
provider claim.

## Return-To-Orchestrator Conditions

Return to the operator if D2 requires new live provider behavior, route
dispatch changes, all-provider parity claims, receipt-envelope changes,
retry/cost/risk ownership changes, public-sync, hosted readiness, Maika proof,
or freeze release.

## Claim Boundary

This work order closes only D2 provider capability matrix and deterministic
unsupported-method behavior for the current private baseline.
