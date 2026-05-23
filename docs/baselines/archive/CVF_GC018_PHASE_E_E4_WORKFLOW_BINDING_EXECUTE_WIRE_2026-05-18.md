# CVF GC-018 Phase E E.4 Workflow Binding Execute Wire - 2026-05-18

Memory class: FULL_RECORD
Status: GC018_FILED

## Candidate ID

`CVF_GC018_PHASE_E_E4_WORKFLOW_BINDING_EXECUTE_WIRE_2026-05-18`

## Date

2026-05-18

## Parent Roadmap

- `docs/reviews/CVF_PHASE_E_GOVERNED_EXECUTION_CHAIN_ROADMAP_2026-05-18.md`
- Tranche: E.4 - Wire Workflow Binding into Execute Path
- Prerequisite audit:
  `docs/reviews/CVF_PHASE_E_EXECUTION_CHAIN_AUDIT_2026-05-18.md`
- Prerequisite implementations:
  `docs/reviews/CVF_PHASE_E_E2_ROLE_PERMISSION_GATE_COMPLETION_2026-05-18.md`
  and
  `docs/reviews/CVF_PHASE_E_E3_WORKFLOW_BINDING_COMPLETION_2026-05-18.md`

## Purpose

Authorize the bounded E.4 runtime wire-up that resolves the existing Product
Brief workflow binding in the live web execute path and emits observable step
traces for the active selected-flow steps.

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`

Owner boundary:

- `CVF_GUARD_CONTRACT` remains the source of truth for
  `WorkflowBinding`, `WorkflowStepExecutionTrace`, role/output contracts, and
  runtime workflow vocabulary.
- `cvf-web` owns binding lookup and response/audit projection for the selected
  `/api/execute` flow.
- E.4 does not add new workflow schemas, new providers, or public catalog
  claim changes.

## Proposed Scope

Wire the E.3 Product Brief workflow binding into the E.2-gated execute path.

Implementation scope:

- add `workflow-resolver.ts` to load and validate the selected Product Brief
  binding by template ID or workflow ID;
- after role/output permission passes, resolve the binding for
  `app_builder_complete`;
- emit `WorkflowStepExecutionTrace` records for active steps 1, 2, 3, and 5;
- skip step 4 because its status is `deferred_until_reviewer_surface`;
- include `workflowId`, `stepTraces[]`, and `receipts[]` in the response when
  a binding is resolved;
- include the same step trace data in the audit event;
- preserve fallback behavior for unbound requests.

## Continuation Class

`bounded_runtime_wire_up`

This consumes the E.3 binding artifact in one selected live route. It is not a
new governance concept or provider expansion.

## Quality-First Decision

Proceed.

E.2 and E.3 now provide the prerequisite role gate and validated binding
metadata. E.4 is the minimum runtime continuation needed to prove workflow
binding is observable in a real governed request instead of remaining a static
contract artifact.

## Quality Protection Commitments

- Do not dispatch deferred reviewer step 4.
- Do not widen the selected flow beyond `app_builder_complete`.
- Preserve unbound route fallback behavior.
- Keep role/output permission gate before workflow dispatch.
- Emit a trace only when `preconditionChecked`, `decision`, `receiptId`, and
  `source` are observable.
- Run deterministic route tests and live Alibaba proof.
- Do not update public catalog claims in E.4.

## Source / Predecessor Evidence

| Source | Evidence | Result |
| --- | --- | --- |
| E.2 completion | Role/output gate fires before provider dispatch | ACCEPTED |
| E.3 completion | Product Brief workflow binding validates with active steps 1, 2, 3, and 5 | ACCEPTED |
| Phase E roadmap | E.4 requires response and audit event step traces plus live Alibaba proof | ACCEPTED |
| Operator prompt | Requires live proof for E.4, not for E.2/E.3/E.5 | ACCEPTED |

## Decision / Baseline / Proposed Tranche

Decision: APPROVE_E4_WORKFLOW_BINDING_EXECUTE_WIRE_IMPLEMENTATION.

Baseline:

- `/api/execute` now normalizes caller role and gates output class;
- the Product Brief workflow binding exists and validates;
- `/api/execute` does not yet resolve or return workflow traces.

Proposed tranche:

- add binding resolver and route projection;
- add deterministic tests for bound/fallback/deferred-step behavior;
- run live release-quality proof with Alibaba lane.

## Why Now

E.4 is ordered after E.2 and E.3. Without this tranche, Phase E cannot claim
the governed workflow checkpoint fires in a real request.

## Active-Path Impact

Limited.

The selected `app_builder_complete` execute path will include workflow binding
metadata and step traces after the existing role/output permission gate passes.
Unbound requests should continue through the existing governed route without
workflow metadata.

## Risk If Deferred

If deferred, Phase E remains a set of contracts plus a role gate. The workflow
binding would not be observable in route responses or audit events, leaving the
E.1 workflow rows open.

## Live Proof Boundary

Live provider proof is required for E.4.

Required live proof:

- run `python scripts/run_cvf_release_gate_bundle.py --json`;
- run or extend a targeted Product Brief live route test that returns
  `workflowId`, `stepTraces[]`, and `receipts[]`;
- ensure `.env.local` keys are loaded only into process environment and never
  printed.

## Required Evidence

- Bound request resolves `workflow.product.create_product_brief.v1`.
- Active steps 1, 2, 3, and 5 emit `WorkflowStepExecutionTrace` records.
- Deferred REVIEWER step 4 is skipped and not counted as fired.
- Each emitted trace includes `stepId`, `preconditionChecked`, `decision`,
  `receiptId`, and `source`.
- Response includes `workflowId`, `stepTraces[]`, and `receipts[]`.
- Audit event includes the same step trace data.
- Unbound request path remains backwards compatible.
- Live Alibaba proof PASS.

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| E.2 prerequisite is complete | `docs/reviews/CVF_PHASE_E_E2_ROLE_PERMISSION_GATE_COMPLETION_2026-05-18.md`; commit `235aad63` | ACCEPTED |
| E.3 prerequisite is complete | `docs/reviews/CVF_PHASE_E_E3_WORKFLOW_BINDING_COMPLETION_2026-05-18.md`; commit `f41d0411` | ACCEPTED |
| E.4 requires live proof | Phase E roadmap E.4 section requires Alibaba live proof and observable traces | ACCEPTED |
| Public catalog update is out of scope | Phase E roadmap reserves public catalog update for E.6 from public-sync only | ACCEPTED |

## Claim Boundary

This GC-018 authorizes only Tranche E.4. It does not authorize E.5 receipt
obligation expansion, E.6 closure, public catalog changes, provider method
expansion, or any change to `system_reconvergence_stop`.
