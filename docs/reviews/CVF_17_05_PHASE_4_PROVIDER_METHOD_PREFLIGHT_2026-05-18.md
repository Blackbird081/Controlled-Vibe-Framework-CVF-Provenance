# CVF 17.05 Phase 4 Provider Method Preflight - 2026-05-18

Memory class: FULL_RECORD

Status: PHASE 4 PREFLIGHT - DEMAND GATED / BLOCKED BEFORE GC-018

## Purpose

Evaluate Phase 4.T1/T2 provider method extension without implementing provider
methods yet, preserving the roadmap rule that provider extension is
method-by-method and demand-gated.

## Scope / Target / Owner Boundary

Target: Phase 4 provider method extension from the 17.05 converged roadmap.

Owner: `EXTENSIONS/CVF_MODEL_GATEWAY/` for provider execution model.

In scope:

- identify current provider-method evidence;
- classify near-term and demand-gated methods;
- decide which methods, if any, may join the consolidated live proof bundle;
- preserve demand gate before GC-018.

Out of scope:

- adding provider interface methods now;
- broad provider abstraction rewrite;
- live provider calls;
- web provider runtime changes;
- public claims.

## Target / Source Under Review

Sources:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `docs/reviews/CVF_17_05_CONSOLIDATED_LIVE_PROOF_PLAN_2026-05-18.md`

## Scope / Methodology

Method:

1. Read the Phase 4.T1/T2 roadmap gates.
2. Scan current provider gateway surfaces for existing stream/tool/json
   awareness.
3. Determine whether a concrete Phase 2.C/3.E consumer requires a provider
   method now.
4. Classify live-proof bundle inclusion.

## Findings / Position

Phase 4 is blocked before implementation.

The model gateway already has provider output contract awareness, including
`parseProviderNdjsonStream()` and JSON/NDJSON stdout policy. The roadmap
explicitly says the missing piece is a first-class provider interface method,
not a broad rewrite. No selected Phase 2.C vertical slice currently requires
`stream()`, `tool_call()`, `json_mode()`, `vision()`, `embedding()`, or
`reasoning()` as a new provider method.

## Method Disposition

| Method | Current evidence | Disposition |
|---|---|---|
| `stream()` | NDJSON parsing exists in `provider-output-contract.ts` | Candidate only; needs consumer |
| `tool_call()` | No selected Phase 2.C consumer | Blocked |
| `json_mode()` | JSON envelope parsing exists; no first-class method | Candidate only; needs consumer |
| `vision()` | No named vertical slice | Blocked |
| `embedding()` | No named vertical slice | Blocked |
| `reasoning()` | No named vertical slice | Blocked |

## Live Bundle Relationship

Provider-method proof should join the consolidated live bundle only if the
Phase 2.C GC-018 explicitly selects a provider method as necessary for the
`Create Product Brief` slice or a later named vertical slice.

Default live bundle membership: no Phase 4 method.

Conditional membership:

- `json_mode()` may join if Phase 2.C requires provider-enforced structured
  output rather than local output validation.
- `stream()` may join if Phase 2.C requires first-class streaming evidence.
- `tool_call()` / `vision()` / `embedding()` / `reasoning()` remain excluded
  until a named consumer exists.

## Risk / Corrective Action

Risk:

- Implementing provider methods before a consumer exists would reopen broad
  provider abstraction work and make live proof larger than needed.

Corrective action:

- Keep Phase 4 blocked until a fresh GC-018 names the method and consuming
  vertical slice/runtime need.
- Reuse the consolidated live proof bundle only when the provider method is
  necessary for the selected slice.

## Decision / Recommendation / Disposition

Decision: Phase 4.T1/T2 implementation is blocked.

Recommendation: do not implement provider methods before Phase 2.C selects a
vertical slice and proves a concrete method need.

Disposition: `phase_4_demand_gate_blocked`.

## Claim Boundary

This preflight does not authorize provider method implementation, does not run
live provider proof, does not change provider runtime behavior, does not expand
public claims, and does not lift `system_reconvergence_stop`.

