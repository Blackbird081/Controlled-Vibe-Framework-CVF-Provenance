# CVF GC-018 V3 Execution Diagnostic Contract

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Purpose

Authorize V3 as the next mandatory diagnostic standard and implementation
tranche for live CVF execution paths.

V3 exists to prevent repeated live runs that consume time, token budget, and
provider quota without recording why a run failed or what a user/operator
should do next.

## Scope / Target / Owner Boundary

Scope: diagnostic contract and future implementation wiring for live-run
failure classification.

Target:

- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- `/api/execute` diagnostic response surface
- provider adapter error normalization
- CLI/MCP/API-key user-facing error rendering
- live proof/probe scripts

Owner: Codex implementer, with operator authorization.

Out of scope:

- new provider behavior
- new model proof loops
- broad provider stability claims
- receipt-envelope expansion unless separately justified
- memory reinjection
- graph authority
- hosted readiness or production readiness claim
- freeze release

## Source / Trigger

Operator decision on 2026-05-24:

- V3 is important and must become the required standard for all AI/agent live
  runs.
- End users using CLI/MCP/API keys through CVF must receive actionable error
  diagnostics instead of only `success=false` or empty output.

Related evidence:

- S2 DeepSeek blocker and superseding diagnostic closure:
  `docs/reviews/CVF_S2_PROVIDER_SOAK_HARDENING_COMPLETION_2026-05-24.md`
- S3 metric clarity issue:
  `docs/reviews/CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_COMPLETION_2026-05-24.md`

## Decision / Baseline / Proposed Tranche

Decision: `AUTHORIZED`

Baseline:

- CVF has partial historical diagnostic language (`provider_timeout`,
  `provider_error`, `api_timeout`) and S2 probe-level diagnostics, but no
  mandatory cross-agent live-run diagnostic standard or end-user-ready
  execution diagnostic contract.

Proposed tranche:

- V3 Execution Diagnostic Contract.
- Add stable diagnostic taxonomy and secret-safe output requirements.
- Prepare runtime implementation through
  `docs/work_orders/CVF_WO_V3_EXECUTION_DIAGNOSTIC_CONTRACT_2026-05-24.md`.

## Depth Audit

| Dimension | Score | Rationale |
| --- | --- | --- |
| Risk reduction | 2 | Prevents ambiguous failed live runs and unsafe over-retries. |
| Decision value | 2 | Distinguishes key/balance/rate-limit/model/policy/provider/runtime failures. |
| Machine enforceability | 2 | Stable fields and classes can be tested and rendered. |
| Operational efficiency | 2 | Reduces wasted reruns, token use, and manual triage. |
| Portfolio priority | 2 | Required for real CLI/MCP/API-key end-user operation. |

Total: `10/10`

Decision: `CONTINUE`

## Authorization Boundary

Authorized now: YES

Next batch name: V3 Execution Diagnostic Contract.

V3 implementation must remain bounded to diagnostics and user-actionable
failure reporting. It must not use diagnostic work as a pretext for broad
provider tuning, provider soaking, model expansion, or governance semantic
changes.

## Required Evidence

- Standard document filed and linked from active session routing.
- Work order filed.
- S3 benchmark evidence clarified so call-level pass rate is not confused with
  event-model denominator metrics.
- Future implementation closure must include:
  - unit tests for stable taxonomy mapping
  - route/API response proof for failed provider execution
  - CLI/MCP or script rendering proof
  - one live bounded diagnostic proof with no raw secret leakage

## Claim Boundary

This GC-018 authorizes V3 diagnostic standardization and implementation
planning. It does not itself close runtime implementation, change provider
semantics, or claim end-user diagnostic readiness until the V3 work order is
implemented and verified.
