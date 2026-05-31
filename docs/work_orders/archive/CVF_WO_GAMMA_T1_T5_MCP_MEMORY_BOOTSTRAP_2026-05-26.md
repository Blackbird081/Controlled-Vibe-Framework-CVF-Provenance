# CVF Work Order Gamma-T1-T5 MCP Memory Bootstrap

Memory class: WORK_ORDER

docType: work_order

Date: 2026-05-26

Status: DISPATCHED_BY_OPERATOR_FULL_GAMMA

## Purpose

Implement the bounded Gamma memory-bootstrap MCP tools on the existing CVF MCP
server package.

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/`
- `docs/guides/CVF_GAMMA_MCP_SERVER_LOCAL_SETUP_2026-05-26.md`
- session/handoff/roadmap state docs.

Owner: Codex multi-role implementer/auditor/product-boundary reviewer.

Boundary: local MCP server, local SDK-client verification, private provenance
only.

## Authority Chain

- Operator request: continue through full Gamma and operator will test after
  completion.
- GC-018:
  `docs/baselines/CVF_GC018_GAMMA_T1_T5_MCP_MEMORY_BOOTSTRAP_2026-05-26.md`
- Predecessor:
  `docs/reviews/CVF_GAMMA_T0_MCP_SERVER_READINESS_AUDIT_COMPLETION_2026-05-26.md`

## Agent Roles

- Orchestrator: keep Gamma sub-tranches bounded.
- Implementer: add tools and verifier.
- Auditor: run package and governance checks.
- Product/operator advocate: keep startup use pattern simple.
- Boundary owner: prevent public/provider/runtime overclaim.

## Allowed / Forbidden Scope

Allowed scope:

- Read-only repo-state MCP tools.
- Secret redaction.
- In-process MCP tool-call audit.
- Local SDK-client verification script.
- Local setup guide.

Forbidden scope:

- Provider/API-key calls.
- `/api/execute` route changes.
- Write/mutation MCP tools.
- Remote transport.
- Public-sync.
- Alpha/Beta retirement.
- Hosted readiness, production readiness, public release readiness, or freeze
  release.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V13_2026-05-25.md`
- `docs/reviews/CVF_GAMMA_T0_MCP_SERVER_READINESS_AUDIT_COMPLETION_2026-05-26.md`
- `docs/roadmaps/CVF_CROSS_AGENT_MEMORY_PROGRESSION_ROADMAP_2026-05-26.md`

## Pre-Flight Checks

- Verify MCP package builds before completion.
- Verify current MCP docs confirm TypeScript SDK stdio server/tool registration
  pattern.
- Confirm no live provider proof is required for this local MCP tool tranche.

## Write Ownership

Code ownership:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/startup/`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/`
- MCP server entrypoint and SDK barrel.
- MCP package scripts and README.

Docs ownership:

- Gamma GC/work order/completion packet.
- Local setup guide.
- Roadmap/session/handoff state updates.

## Execution Plan

1. Add secret-safe startup-state helpers.
2. Add in-process MCP tool audit helper.
3. Register Gamma tools in the existing MCP server.
4. Export helpers through SDK barrel.
5. Add tests and SDK-client verification script.
6. Add local setup guide.
7. Run build/test/verify/gates.
8. Commit and sync handoff state.

## Evidence Requirements

- Focused tests for startup state and audit.
- Full MCP package tests.
- MCP package build.
- `npm run verify:gamma` local SDK-client proof.
- Governance gates.

## Acceptance Criteria

- Existing seven guard tools preserved.
- New Gamma tools exposed:
  - `cvf_get_session_memory`
  - `cvf_get_active_handoff`
  - `cvf_get_session_state`
  - `cvf_get_startup_acknowledgment`
  - `cvf_get_governance_rules`
  - `cvf_check_governance_action`
  - `cvf_get_mcp_tool_audit_log`
- Tool responses are read-only and secret-redacted.
- Local SDK-client can call required tools via stdio.
- Audit log records Gamma tool calls.

## Review Gate

Do not close Gamma if build/test/verify fails without a classified blocker.

## Closure Checklist

- [x] GC-018 present.
- [x] Work order present.
- [x] Code implemented.
- [x] Local setup guide present.
- [x] Tests/build/verify recorded.
- [x] Claim boundary recorded.

## Return-To-Orchestrator Conditions

Return if MCP SDK incompatibility blocks local stdio verification, secret
redaction fails, or any implementation requires provider/route/public scope.

No return condition was triggered.

## Operator Checkpoint

Operator will perform external/client-side testing after completion. External
client auto-start remains operator-acceptance gated.

## Claim Boundary

Gamma closes local MCP memory-bootstrap readiness only. It does not claim every
third-party MCP client auto-starts the server, hosted availability, public
release readiness, production readiness, provider behavior, route behavior,
Alpha/Beta retirement, or freeze release.
