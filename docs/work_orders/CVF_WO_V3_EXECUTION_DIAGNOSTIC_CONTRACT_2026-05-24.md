# CVF Work Order: V3 Execution Diagnostic Contract

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-24

Tranche: V3

Roadmap: `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`

---

## Purpose

Implement a stable, secret-safe execution diagnostic contract so CVF live runs,
CLI/MCP/API-key flows, and proof scripts can explain failed or empty-output
executions without wasting repeated live provider calls.

## Scope / Target / Owner Boundary

Target:

- provider error normalization
- `/api/execute` failure diagnostics
- CLI/MCP/script diagnostic rendering
- live-run probe diagnostic capture

Owner: Codex implementer.

Out of scope:

- new provider behavior
- broad provider stability proof
- model-specific proof loops
- receipt-envelope expansion unless required and separately reviewed
- memory reinjection
- graph authority
- hosted readiness or production readiness claims
- freeze release

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_V3_EXECUTION_DIAGNOSTIC_CONTRACT_2026-05-24.md`
- Standard:
  `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- Roadmap:
  `docs/roadmaps/CVF_VALUE_SCREENED_NEXT_TRANCHE_ROADMAP_2026-05-24.md`

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Map current failure surfaces before implementation. |
| Implementer | Add stable diagnostic contract and bounded wiring. |
| QA | Verify taxonomy, secret hygiene, and user-actionable rendering. |
| Governance Reviewer | Confirm diagnostics do not become new governance semantics. |
| Release Manager | File closure review and update session routing. |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Write Ownership

Allowed future implementation targets:

- typed diagnostic module in cvf-web
- provider adapter error mapping
- `/api/execute` response diagnostic wiring
- focused tests for diagnostics
- live proof/probe scripts
- CLI/MCP/script rendering path if present and locally discoverable

Forbidden without separate authorization:

- provider behavior changes unrelated to diagnostics
- receipt-envelope schema expansion unless reviewed as necessary
- new provider/model additions
- broad provider soak expansion
- public production-readiness claims

## Pre-Flight Checks

- Confirm the live diagnostic standard has been read.
- Confirm current response/error surfaces before editing.
- Confirm no raw API key, signed header, bearer token, or unredacted provider
  body will be printed.
- Confirm whether CLI/MCP rendering target exists locally before promising it.
- Confirm any live proof has operator-supplied env keys available without
  printing values.

## Work Plan

1. Add a typed diagnostic contract with stable `stage`, `class`,
   `retryable`, `userAction`, and safe message fields.
2. Normalize provider adapter failures into the contract.
3. Attach diagnostics to failed `/api/execute` responses without printing raw
   keys or signed headers.
4. Update live probe scripts to require diagnostics before rerun.
5. Add CLI/MCP or script-facing rendering so end users see what to do next.
6. Add tests for provider timeout, missing key, invalid key/auth, insufficient
   balance/quota, rate limit, model unavailable, routing denied, policy block,
   output validation failure, and receipt missing.
7. Run one bounded live diagnostic proof.

## Execution Plan

1. Inspect current `ExecutionResponse` and `/api/execute` failure returns.
2. Add the smallest typed diagnostic contract.
3. Map provider/route failures to stable classes.
4. Add or update tests.
5. Add one live proof that intentionally captures a safe diagnostic without
   leaking secrets.
6. File completion review.
7. Update session routing.

## Evidence Requirements

- Unit test output for diagnostic mapping.
- Route/API response proof for at least one failed execution class.
- CLI/MCP/script rendering proof or explicit N/A if no rendering path exists in
  the selected scope.
- One live diagnostic proof with `rawSecretPrinted=false`.
- Release gate PASS if runtime route behavior changes.

## Acceptance Criteria

- [ ] Stable diagnostic type exists.
- [ ] Provider failures map to stable classes.
- [ ] `/api/execute` failed responses include a safe diagnostic.
- [ ] No raw API key, bearer token, signed header, or raw provider secret is
      emitted in diagnostic output.
- [ ] CLI/MCP/script path can render `safeMessage` and `userAction`.
- [ ] Tests cover at least six failure classes.
- [ ] One live bounded diagnostic proof is filed.
- [ ] Mandatory release gate remains PASS.

## Verification / Evidence

Required closure evidence:

- completion review
- targeted unit tests
- live diagnostic proof
- release gate result
- public catalog update or explicit N/A

## Review Gate

The closure review must confirm:

- every failed live run in the tranche has a diagnostic or an explicit reason
  diagnostic capture was impossible
- diagnostics are secret-safe
- userAction is actionable for CLI/MCP/API-key users
- no broad provider stability or production readiness claim is introduced

## Operator Checkpoint

Operator selected V3 on 2026-05-24 and declared it a required standard for all
AI/agent live runs.

## Closure Checklist

- [ ] Diagnostic standard cited.
- [ ] Runtime implementation evidence filed.
- [ ] Tests passed.
- [ ] Live diagnostic proof filed.
- [ ] Release gate PASS or explicitly N/A if no runtime behavior changed.
- [ ] Public catalog updated or explicitly N/A.
- [ ] Session state and handoff updated.

## Return-To-Orchestrator Conditions

Return blocked if:

- diagnostic implementation would require broad provider behavior changes
- safe redaction cannot be guaranteed
- live proof would print raw keys or signed headers
- CLI/MCP/API-key userAction cannot be made actionable in the selected scope

## Claim Boundary

V3 may claim user-actionable diagnostic classification only for implemented
paths and tested classes. It must not claim provider reliability, production
readiness, hosted SaaS readiness, memory/graph authority, or freeze release.
