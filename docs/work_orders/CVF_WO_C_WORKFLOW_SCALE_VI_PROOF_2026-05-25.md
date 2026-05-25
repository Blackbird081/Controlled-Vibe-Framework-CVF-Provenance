# CVF Work Order C Workflow Scale VI Proof

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-25

---

## Purpose

Execute the bounded C workflow-scale proof authorized by
`docs/baselines/CVF_GC018_C_WORKFLOW_SCALE_VI_PROOF_2026-05-25.md`.

## Authority Chain

- Operator approved order: B+VI4, then D, then C.
- VI1 proved Product Brief workflow integration.
- VI4 packaged the vertical evidence surfaces.
- D proved the VI4 package across DeepSeek/OpenAI provider lanes.

## Agent Roles

- Implementer: add deterministic workflow bindings and tests.
- Auditor: keep route/provider/receipt/prompt behavior unchanged.
- Workflow reviewer: verify recovery gate behavior remains deferred.
- Operator advocate: verify the selected workflows are high-value for
  non-coder users.

## Allowed / Forbidden Scope

Allowed:

- workflow binding JSON files;
- workflow resolver registration;
- workflow resolver tests;
- one focused live route proof;
- completion/session/handoff docs.

Forbidden:

- `/api/execute/route.ts` behavior changes;
- provider router/adapter changes;
- prompt mutation;
- receipt envelope changes;
- broad workflow engine;
- workflow transition blocking;
- public-sync, hosted readiness, production readiness, broad workflow claims,
  or freeze release.

## Scope / Target / Owner Boundary

Scope: deterministic workflow binding scale for exactly three selected
templates.

Target: `strategy_analysis`, `marketing_campaign_wizard`, and `brand_voice`
inside the cvf-web workflow resolver surface.

Owner boundary: workflow binding and evidence proof only; no route/provider/
receipt/prompt ownership is opened.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`
- `docs/baselines/CVF_GC018_C_WORKFLOW_SCALE_VI_PROOF_2026-05-25.md`

## Pre-Flight Checks

- confirm worktree clean after D closure;
- confirm no planned route/provider/receipt/prompt edits;
- confirm chosen templates exist.

## Write Ownership

Writes are limited to workflow binding files, workflow resolver/test, live spec,
completion review, this work order, active state, front door, and handoff.

## Execution Plan

1. Add Strategy, Marketing Campaign, and Brand Voice workflow bindings.
2. Register bindings in resolver.
3. Add focused resolver tests.
4. Add focused live proof for the three workflows.
5. Run focused tests, `npm run check`, live proof, and guards.
6. File completion review and commit closure.

## Acceptance Criteria

- Three selected workflows resolve to valid bindings.
- Their projections expose state-machine and recovery readouts.
- Product Brief behavior remains unchanged.
- Live proof asserts VI workflow surfaces and VI4 package for each selected
  workflow.

## Evidence Requirements

- focused resolver tests PASS;
- `npm run check` PASS;
- live proof PASS or diagnostic filed;
- active session state guard PASS;
- handoff guard PASS.

## Review Gate

Before closure, verify no route behavior, provider/router/adapter, prompt,
receipt-envelope, public/hosted/product-readiness, or freeze-release change.

## Operator Checkpoint

No checkpoint is required unless live proof needs a non-retryable diagnostic,
or implementation requires route/provider/receipt/prompt changes.

## Return Conditions

Return blocked if implementation requires route handler behavior changes,
provider/router/adapter changes, prompt mutation, receipt-envelope changes, or
a claim broader than the three selected workflow bindings.

## Return-To-Orchestrator Conditions

Same as return conditions above. Stop and return if the work needs route,
provider, prompt, receipt-envelope, or broad workflow-engine scope expansion.

## Claim / Final / Verification Boundary

C may close only bounded workflow binding scale for Strategy, Marketing
Campaign, and Brand Voice. It must not claim all-template workflow runtime,
broad workflow engine, hosted readiness, production readiness, or freeze
release.

## Claim Boundary

Same as above: bounded workflow binding scale for exactly three selected
non-Product-Brief workflows.

## Closure Checklist

- [ ] workflow bindings added
- [ ] resolver registration added
- [ ] focused resolver tests PASS
- [ ] cvf-web check PASS
- [ ] live proof PASS or diagnostic filed
- [ ] completion review filed
- [ ] active state/front door/handoff updated
- [ ] active state guard PASS
- [ ] handoff guard PASS
- [ ] commit created
