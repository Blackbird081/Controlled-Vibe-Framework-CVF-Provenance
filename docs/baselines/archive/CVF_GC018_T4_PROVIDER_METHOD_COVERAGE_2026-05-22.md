# CVF GC-018 - T4 Provider Method Coverage

Memory class: GOVERNANCE_BASELINE

Status: ACCEPTED
Date: 2026-05-22
Parent Commit: b8e3fb92
Roadmap: docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md
Work Order: docs/work_orders/CVF_WO_T4_PROVIDER_METHOD_COVERAGE_2026-05-22.md

## Purpose
Authorize a bounded Model Gateway provider-method coverage tranche for Alibaba qwen-turbo stream support, DeepSeek deepseek-chat JSON mode support, and a negative unsupported-method gate.

## Scope / Target / Owner Boundary
In scope: provider method contract, provider capability files, Alibaba stream adapter, DeepSeek JSON-mode adapter, unsupported-method gate, and Model Gateway tests.

Out of scope: cvf-web, API routes, receipt types, memory wiring, new providers, reasoning/vision expansion, live provider calls, public-sync, hosted readiness, and freeze release.

## Target / Source Under Review
Targets:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/capability.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-method-coverage.test.ts`

## Source / Predecessor Evidence
T3 closure: `docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`.

Existing Model Gateway contracts: `stream-contract.ts` and `json-mode-contract.ts`.

## Scope / Methodology
Codex executed Orchestrator, Reviewer, Implementer, and Auditor roles in one bounded session. The tranche uses mocked fetch responses only and does not perform live provider calls.

## Evidence Trace Block
Operator override confirmation source: 2026-05-22 user instruction, "Codex executes T1→T2→T3→T4→T5 sequentially ... cần api key thì cứ lấy dùng, ko cần hỏi tôi".

Blocked-work class: `new_provider_execution_semantics`.

Override status: GRANTED, bounded only to:

- `stream()` on Alibaba `qwen-turbo`.
- `json_mode()` on DeepSeek `deepseek-chat`.
- negative `UnsupportedMethodError` gate.

## Findings / Position
The T4 scope is valid with the recorded override. It does not add live execution paths to cvf-web and does not change any provider routing surface.

## Risk / Defect / Corrective Action
Residual risk: adapters are unit-tested against mocked provider responses only.

Corrective action: live provider method invocation remains demand-gated and outside T4.

## Decision / Baseline / Proposed Tranche
Decision: ACCEPT T4 implementation baseline with bounded override GRANTED.

Baseline: Model Gateway method contracts and mocked adapters only.

Proposed tranche: close T4 after Model Gateway tests and typecheck pass.

## Verification
Required verification:

- Model Gateway targeted provider-method test.
- Model Gateway full test suite.
- Model Gateway TypeScript check.
- markdown structural and file-size governance checks.

## Claim Boundary
T4 proves bounded method coverage contracts and mock-tested adapters only. It does not claim live streaming reliability, live JSON-mode provider behavior, cvf-web route integration, memory wiring, public deployment readiness, or broad provider stability.
