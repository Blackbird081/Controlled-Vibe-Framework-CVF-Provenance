# CVF GC-018 C Workflow Scale VI Proof

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-25

---

## Purpose

Authorize bounded C workflow scale after VI4 and D closure: apply the existing
VI1/VI4 vertical integration pattern beyond Product Brief to selected
Strategy, Marketing, and Brand workflows.

## Target / Source

Target owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/*.live.test.ts`

Primary sources:

- VI1 workflow chain completion
- VI4 evidence package completion
- D provider-scale closure
- Existing trusted templates: `strategy_analysis`, `marketing_campaign_wizard`,
  and `brand_voice`

## Source / Predecessor Evidence

Predecessor evidence:

- VI1 proved workflow state-machine/recovery on Product Brief.
- VI4 packaged workflow surfaces with W3/W4/W5/TA1 evidence.
- D proved VI4 package on additional live provider lanes.

Gap: non-Product-Brief workflows do not yet resolve to workflow bindings, so
their VI readout cannot expose workflow state-machine/recovery surfaces.

## Decision / Baseline / Proposed Tranche

Decision: authorize C workflow scale for exactly three high-value workflow
families: Strategy, Marketing Campaign, and Brand Voice.

Baseline: Product Brief remains the reference binding pattern.

Proposed tranche: add deterministic local workflow bindings, resolver tests,
and a live route proof that those workflows expose VI workflow surfaces.

## Scope

Allowed:

- add workflow binding JSON files for `strategy_analysis`,
  `marketing_campaign_wizard`, and `brand_voice`;
- register those bindings in `workflow-resolver.ts`;
- update workflow resolver tests;
- add one focused live proof for the selected workflows;
- file completion review and session updates.

Forbidden:

- route behavior changes;
- provider router/adapter changes;
- broad workflow engine;
- new receipt envelope schema;
- prompt mutation;
- workflow transition blocking;
- public-sync, hosted readiness, production readiness, broad workflow platform
  claim, or freeze release.

## Multi-Role Review

Implementer: follow the Product Brief binding pattern and keep changes local.

Auditor: verify no route handler, provider, receipt-envelope, or prompt changes.

Workflow owner: require reviewer-gate deferral and recovery readout, not
auto-completion.

Product/operator advocate: choose workflows that map to non-coder business
value: strategy decision, campaign planning, and brand consistency.

## Acceptance Criteria

- Resolver returns bindings for all three selected templates.
- Projection emits state-machine and recovery readout for all three workflows.
- Existing Product Brief behavior remains unchanged.
- Live proof returns `workflow_state_machine`, `workflow_recovery`, and VI4
  evidence package for all three selected workflows.
- `cvf-web` check PASS.

## Evidence / Verification

Required evidence:

- focused workflow resolver tests PASS;
- `npm run check` PASS;
- live route proof PASS or diagnostic filed;
- active state and handoff guards PASS.

## Claim Boundary

C proves only bounded workflow binding scale for three selected workflow
families. It does not prove a broad workflow engine, all templates, workflow
runtime enforcement, hosted readiness, production readiness, public-sync, or
freeze release.

## Next Move

After closure, pause for operator review or open a later value-screened tranche.
