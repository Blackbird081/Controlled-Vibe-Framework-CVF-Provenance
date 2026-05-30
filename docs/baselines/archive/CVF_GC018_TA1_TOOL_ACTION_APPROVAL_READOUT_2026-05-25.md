# CVF GC-018 TA1 Tool Action Approval Readout

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_TA1_TOOL_ACTION_APPROVAL_READOUT

docType: gc018_baseline

Date: 2026-05-25

---

## Purpose

Authorize a bounded TA1 implementation that adds a deterministic local approval
readout on top of the existing W3 tool/MCP/database action taxonomy.

## Scope / Target / Owner Boundary

Allowed owner files:

- `governance/contracts/tool-action-taxonomy.ts`
- `governance/contracts/tool-action-taxonomy.test.ts`
- TA1 completion/session/handoff files

Forbidden:

- real tool, command, MCP, database, browser, or provider execution;
- MCP bridge/client/server wiring;
- database adapter, driver, query, mutation, export, or migration execution;
- `/api/execute` route changes;
- receipt-envelope changes;
- auth/RBAC changes;
- public-sync, hosted readiness, production readiness, or freeze release.

## Source / Predecessor Evidence

Predecessor:

- `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`

Legacy sources read for this authorization:

- `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_AGENT_NATIVE_TOOL_SURFACE_MODEL.md`
- `.private_reference/legacy/CVF ADD/CLI-Anything/CVF_TOOL_SURFACE_POLICY_RULEBOOK.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_TOOL_CALL_TRACE_PROTOCOL.md`
- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/mcp-business-approval-gate.ts`
- `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_ACTION_MODEL.md`
- `.private_reference/legacy/CVF ADD/gridex/CVF_DATABASE_POLICY_BINDING.md`
- `.private_reference/legacy/CVF ADD/AI-first vs Human-first/CVF_POLICY_GATE_MINIMAL_RESPONSE.md`

## Knowledge Absorption Blind-Spot Control Block

- Standard applied:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Prior absorption evidence resolved: LH1 ledger, W3 completion, WC-3 scan map.
- Detailed source files read: listed in Source / Predecessor Evidence.
- Accepted value:
  - callable does not imply approvable;
  - approval has states and must distinguish not-required, pending, satisfied,
    incomplete, and blocked;
  - missing trace/scope/target blocks before approval can matter;
  - blocked actions need concise reason and safe next action;
  - database actions require normalized approval posture before execution.
- Deferred value:
  - actual approval workflow;
  - persistence of approval tickets;
  - runtime executor admission;
  - MCP or database bridge wiring;
  - UI approval surface.
- Rejected value:
  - allowing execution because an approval flag is present;
  - treating read-only allow as runtime authority;
  - importing external MCP/database runtime semantics.
- Owner normalization:
  - extend the existing W3 owner, `governance/contracts/tool-action-taxonomy.ts`.
- Adversarial role review:
  - Implementer: approval readout can be a pure deterministic wrapper around W3.
  - Skeptic/Auditor: approval state must not be confused with execution
    authorization.
  - Product/Operator Advocate: readout gives non-coder/operator-facing reason
    for why an action is held, blocked, or ready for a separately authorized
    executor.
  - Safety/Boundary Owner: no runtime bridge, tool call, database call, or
    provider call is opened.
- Blind-spot delta: reduced; W3 taxonomy says what the action is, TA1 will say
  what approval state it is in and what the next safe action is.
- Verdict: CLEAR.

## Implementation Target

Add `cvf.toolActionApprovalReadout.ta1.v1` with:

- approval state;
- approval mode/level;
- required evidence;
- missing evidence;
- next safe action;
- concise safe message;
- `runtimeExecutionAuthorized=false` preserved.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_TA1_TOOL_ACTION_APPROVAL_READOUT.

Baseline:

- W3 already classifies planned tool/MCP/command/database actions.
- W3 does not provide a separate approval-state packet for agents/operators.
- Runtime execution remains closed.

Proposed tranche:

- add deterministic approval/readout on top of W3;
- keep all execution, persistence, route, MCP, database, and provider behavior
  out of scope;
- close only after focused and full `governance/contracts` tests pass.

## Acceptance Criteria

- read-only traced local action reports approval not required;
- mutation without approval reports approval pending;
- mutation with approval and required controls reports approval satisfied but
  still not runtime-authorized;
- missing trace/scope/target reports blocked before approval;
- destructive/privileged action reports policy block;
- tests prove no runtime execution authority is exported or implied.

## Verification Plan

Run:

```bash
cd governance/contracts
npm test -- tool-action-taxonomy.test.ts
npm test
```

Live proof N/A because TA1 is deterministic local contract readout only and does
not assert live governance behavior.

## Claim Boundary

TA1 may claim only deterministic local approval/readout for planned
tool/MCP/command/database action evaluations. It must not claim runtime
execution, live MCP/database behavior, route enforcement, approval-ticket
persistence, public capability graduation, hosted readiness, production
readiness, or freeze release.
