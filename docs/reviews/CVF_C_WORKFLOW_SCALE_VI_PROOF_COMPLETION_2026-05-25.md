# CVF C Workflow Scale VI Proof Completion

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-25

---

## Purpose

Close the bounded C workflow-scale proof authorized by
`docs/baselines/CVF_GC018_C_WORKFLOW_SCALE_VI_PROOF_2026-05-25.md`.

## Target / Source

Target owner surface: `cvf-web` workflow binding resolver and existing
`/api/execute` vertical integration readout.

Selected workflows:

- `strategy_analysis`
- `marketing_campaign_wizard`
- `brand_voice`

Prior pattern sources: VI1 workflow readout and VI4 evidence package.

## Scope / Methodology

Implemented deterministic workflow binding files for the three selected
templates, registered them in `workflow-resolver.ts`, and extended resolver
coverage to prove the same reviewer-gated projection behavior used by Product
Brief.

The live proof used Alibaba `qwen-turbo` through the existing `/api/execute`
route and asserted live receipt, workflow state-machine, workflow recovery, and
VI4 package surfaces for all three workflows.

No `/api/execute/route.ts` behavior, provider routing, provider adapter,
prompt, receipt envelope, or transition blocking change was made.

## Findings / Position

C closes as PASS for bounded workflow scale. Strategy, Marketing Campaign, and
Brand Voice now resolve to workflow bindings and expose `workflow_state_machine`
and `workflow_recovery` through the existing VI surface.

The runtime workflow transition vocabulary is intentionally closed by
`cvf-guard-contract`; the C bindings therefore reuse the existing
`intake_pending -> design_ready -> build_running -> review_pending ->
freeze_ready -> completed` transition vocabulary with workflow-specific labels,
capability ids, and step ids. This is the correct integration boundary for now.

## Delivered

- Added `workflow.strategy.strategy_analysis.v1`.
- Added `workflow.marketing.create_campaign_brief.v1`.
- Added `workflow.brand.brand_voice_review.v1`.
- Registered all three bindings in `workflow-resolver.ts`.
- Extended `workflow-resolver.test.ts`.
- Added focused live spec:
  `src/app/api/execute/route.c-workflow-scale.alibaba.live.test.ts`.

## Evidence

Focused resolver test:

`npm run test:run -- src/lib/workflows/workflow-resolver.test.ts`

Result: PASS, 6/6.

Static check:

`npm run check`

Result: PASS.

Live proof:

`npm run test:run -- src/app/api/execute/route.c-workflow-scale.alibaba.live.test.ts`

Result: PASS, 1/1.

Live receipts:

- `strategy_analysis`: `rcpt-env-mpkllvuc-ob4af6`
- `marketing_campaign_wizard`: `rcpt-env-mpklmhlb-sj4uju`
- `brand_voice`: `rcpt-env-mpklmr3d-pkhoeb`

Provider/model: Alibaba `qwen-turbo`.

Route line guard: `/api/execute/route.ts` remained 999 lines; route test file
remained 1199 lines.

## Live Diagnostic Note

The first live C run returned HTTP 200 and `success=true`, but the test failed
with `workflowExecution` undefined. Classification: `test_harness_contract_mismatch`.
Cause: `/api/execute` spreads workflow execution fields at the response root,
while the first live spec expected a nested `workflowExecution` object. User
action: no provider/top-up/model action required. Retryability: retryable after
harness correction. The rerun passed with the receipts above.

## Risk / Corrective Action

Risk: readers may infer this proves a broad workflow engine. Correction: claim
is limited to deterministic binding scale for exactly three selected workflows.

Risk: workflow-specific state names are not represented in the runtime
transition vocabulary. Correction: use workflow-specific labels/capability ids
while preserving the contract-approved transition vocabulary.

## Claim Boundary

This completion proves bounded workflow binding scale for
`strategy_analysis`, `marketing_campaign_wizard`, and `brand_voice` on the
existing live `/api/execute` VI path.

It does not claim all-template workflow runtime, broad workflow engine,
workflow transition enforcement, public-sync, hosted readiness, production
readiness, broad provider stability, prompt improvement, receipt-envelope
change, or freeze release.

Public catalog update: N/A for this provenance commit. The work order forbids
public-sync/public-facing claims, and this tranche adds private response-level
workflow binding evidence rather than a public product surface.

## Decision / Recommendation / Disposition

Disposition: CLOSED_PASS_BOUNDED.

Recommended next move: pause for operator review, or open a fresh GC-018 for a
new value-screened tranche. Do not continue workflow scale horizontally without
fresh value screening and a concrete non-coder outcome reason.
