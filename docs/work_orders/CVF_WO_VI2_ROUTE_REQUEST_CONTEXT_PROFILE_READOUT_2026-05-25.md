# CVF Work Order VI2 Route Request Context Profile Readout

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-25

---

## Purpose

Implement the bounded VI2 route request-context/profile readout authorized by
`docs/baselines/CVF_GC018_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_2026-05-25.md`.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts`
- VI2 completion/session/handoff files

Forbidden:

- runtime context injection or prompt mutation;
- route-level blocking based on request context profile;
- new receipt envelope schema;
- LLM scoring, model/provider routing changes, memory reinjection, MCP/tool/
  database/browser automation, external skill import, public-sync, hosted
  readiness, production readiness, or freeze release.

## Agent Roles

- Implementer: add the deterministic readout and attach it to VI.
- Auditor: verify advisory-only status and no route-block/prompt mutation.
- Product/operator advocate: make bad input quality visible before future
  reruns waste live quota.
- Safety/boundary owner: profile cannot authorize broader execution.

## Authority Chain

- VI1 closed the vertical route readout and recommended vertical-adjacent source
  selection.
- CB1 proved request-context readiness in Governance CLI only.
- LH1 keeps caveman and Workflow GoClaw deferred until selector or route
  context grows.
- VI2 authorizes only advisory response-level route readout wiring.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reviews/CVF_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- `docs/baselines/CVF_GC018_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_2026-05-25.md`
- VI owner files in `cvf-web/src/lib` and `/api/execute`

## Pre-Flight Checks

- confirm clean worktree after VI2 authorization;
- confirm `/api/execute/route.ts` remains inside file-size guard;
- confirm no prompt construction, provider routing, or enforcement decision is
  modified;
- confirm live key loading remains secret-safe.

## Write Ownership

Writes are limited to VI2 helper/test files, existing VI/route wiring, live
spec assertions, completion review, and session continuity files.

## Execution Plan

1. Add route request-context/profile readout helper and tests.
2. Add the readout to `verticalIntegrationReadout`.
3. Wire `/api/execute` response without exceeding route size guard.
4. Update live VI spec to assert `request_context_profile`.
5. Run focused tests, check, live proof, session guards.
6. File completion review, close work order, update session/handoff, commit.

## Acceptance Criteria

- `requestContextReadout` is returned by successful route responses;
- vertical readout includes `request_context_profile`;
- readout reports profile, budget tier, readiness, signal/noise/contamination
  fields, execution ceiling, next action, and boundaries;
- readout is advisory only and does not block, mutate prompts, or change
  provider selection;
- focused tests, TypeScript check, live proof, and session guards pass.

## Evidence Requirements

- focused readout/VI/route tests PASS;
- cvf-web TypeScript check PASS;
- live VI route proof PASS with request-context surface present;
- active state guard PASS;
- handoff guard PASS.

## Review Gate

Before closure, verify the diff does not introduce runtime context packaging,
prompt mutation, route blocking, provider selection changes, new receipt
envelope fields, memory reinjection, MCP/tool/database execution, public-sync,
hosted readiness, production readiness, or freeze release.

## Closure Checklist

- [x] readout helper added
- [x] VI surface attached
- [x] route response wired
- [x] focused tests PASS
- [x] TypeScript check PASS
- [x] live proof PASS or diagnostic filed
- [x] completion review filed
- [x] active state/front door/handoff updated
- [x] active state guard PASS
- [x] handoff guard PASS
- [x] commit created

## Return-To-Orchestrator Conditions

Return blocked if implementation requires prompt mutation, route blocking,
provider routing changes, runtime context packaging, memory reinjection, or a
new receipt schema.

## Operator Checkpoint

No checkpoint is required unless live proof lacks a usable key, an unclear live
failure needs a rerun, or implementation requires scope expansion beyond the
VI2 owner files.

## Claim Boundary

VI2 closes only response-level request-context/profile readout wiring. It does
not close runtime context packaging, prompt mutation, route blocking, provider
selection, memory reinjection, hosted readiness, production readiness, or
freeze release.
