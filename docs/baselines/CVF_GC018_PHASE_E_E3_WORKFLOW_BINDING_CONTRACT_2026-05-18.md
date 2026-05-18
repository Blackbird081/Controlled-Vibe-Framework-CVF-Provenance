# CVF GC-018 Phase E E.3 Workflow Binding Contract - 2026-05-18

Memory class: FULL_RECORD
Status: GC018_FILED

## Candidate ID

`CVF_GC018_PHASE_E_E3_WORKFLOW_BINDING_CONTRACT_2026-05-18`

## Date

2026-05-18

## Parent Roadmap

- `docs/reviews/CVF_PHASE_E_GOVERNED_EXECUTION_CHAIN_ROADMAP_2026-05-18.md`
- Tranche: E.3 - Workflow Binding Contract
- Prerequisite audit:
  `docs/reviews/CVF_PHASE_E_EXECUTION_CHAIN_AUDIT_2026-05-18.md`
- Prerequisite implementation:
  `docs/reviews/CVF_PHASE_E_E2_ROLE_PERMISSION_GATE_COMPLETION_2026-05-18.md`

## Purpose

Authorize the bounded E.3 contract-local workflow binding layer for the
selected `Create Product Brief` golden path.

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/workflow-binding.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-workflow-binding.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`

Owner boundary:

- `CVF_GUARD_CONTRACT` owns the typed `WorkflowBinding`,
  `WorkflowStep`, and `WorkflowStepExecutionTrace` vocabulary.
- `cvf-web` owns only the concrete binding file for the selected existing
  golden path.
- E.3 does not wire the binding into `/api/execute`; runtime dispatch is E.4.
- No public-sync catalog edit is authorized by this tranche.

## Proposed Scope

Implement the deterministic workflow binding contract and one concrete
`workflow.product.create_product_brief.v1` binding.

Implementation scope:

- define `WorkflowBinding`, `WorkflowStep`, `WorkflowStepRole`, and
  `WorkflowStepExecutionTrace`;
- define step status vocabulary including
  `deferred_until_reviewer_surface`;
- validate step IDs, role vocabulary, output-class vocabulary, transition
  shape, receipt typing, and deferred-step membership;
- export the contract from the guard-contract barrel;
- add deterministic tests for valid and invalid bindings;
- add one concrete JSON binding for `Create Product Brief`.

## Continuation Class

`bounded_contract_wire_up`

This is not runtime dispatch and not a new governance concept. It materializes
the workflow binding layer already named by the Phase E roadmap and legacy
workflow composition source.

## Quality-First Decision

Proceed.

E.2 has closed the role/output pre-dispatch gate. E.3 is the smallest next
step because E.4 cannot safely dispatch a workflow unless the workflow binding
schema exists, validates deterministically, and represents the deferred
reviewer step without faking runtime proof.

## Quality Protection Commitments

- Do not change `/api/execute` behavior in E.3.
- Do not fire or simulate the REVIEWER step.
- Mark step 4 as `deferred_until_reviewer_surface`.
- Validate roles against `CVFRole` and outputs against
  `RolePermissionOutputClass`.
- Reuse existing `WorkflowTransition` and `ToolActionClass` vocabulary from
  `runtime-workflow.contract.ts`.
- Keep the binding limited to the selected `Create Product Brief` flow.
- Run deterministic guard-contract tests; no live provider proof is required
  for E.3.

## Source / Predecessor Evidence

| Source | Evidence | Result |
| --- | --- | --- |
| E.1 audit | Workflow transition and provider-call typing rows are `wiring_gap` | ACCEPTED |
| E.2 completion | Role/output pre-dispatch gate is wired before E.3 begins | ACCEPTED |
| Phase D runtime workflow contract | `runtime-workflow.contract.ts` exists and provides transition/action vocabulary | ACCEPTED |
| Operator prompt | Requires fresh GC-018 before E.3 implementation and forbids live proof for E.3 | ACCEPTED |

## Decision / Baseline / Proposed Tranche

Decision: APPROVE_E3_WORKFLOW_BINDING_CONTRACT_IMPLEMENTATION.

Baseline:

- `runtime-workflow.contract.ts` exists with workflow transition and action
  vocabulary;
- E.2 now normalizes caller role and selected output class in `/api/execute`;
- no `WorkflowBinding` contract or concrete Product Brief workflow binding
  exists yet.

Proposed tranche:

- add contract-local workflow binding types and validator;
- export binding types from `CVF_GUARD_CONTRACT`;
- add a concrete `workflow.product.create_product_brief.v1.json` fixture;
- prove valid and invalid bindings with deterministic tests;
- leave route dispatch untouched until E.4.

## Why Now

Phase E is operator-authorized on 2026-05-18 despite the roadmap file retaining
`PROPOSED_V2` status text. E.3 is ordered after E.2 and before E.4. Without a
validated binding contract, E.4 would have to invent route-local workflow
semantics instead of consuming a typed contract.

## Active-Path Impact

None.

E.3 adds a contract and a concrete binding artifact only. The live execute path
continues to behave as it did after E.2 until E.4 explicitly resolves and
dispatches the binding.

## Risk If Deferred

If deferred, Phase E cannot move to observable workflow dispatch. The selected
flow would remain a direct governed route with role gating but without a typed
sequence of governed steps.

## Live Proof Boundary

No live provider proof is required for E.3.

E.3 is a deterministic contract and fixture-binding tranche. Live Alibaba proof
is reserved for E.4 and E.6.

## Required Evidence

- `Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`
  returns `True`.
- `WorkflowBinding` type is exported from `CVF_GUARD_CONTRACT`.
- `WorkflowStepExecutionTrace` type is exported from `CVF_GUARD_CONTRACT`.
- `validateWorkflowBinding()` accepts the concrete
  `workflow.product.create_product_brief.v1` binding.
- Tests prove invalid role and invalid output-class bindings fail validation.
- Tests prove receipt-required steps are typed.
- Tests prove deferred REVIEWER steps are valid binding members but not active
  runtime steps.
- `cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`
  includes active steps 1, 2, 3, and 5, and deferred step 4.

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| Runtime workflow contract exists before E.3 | `Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` returned `True` | ACCEPTED |
| E.3 requires no route behavior change | Phase E roadmap marks E.3 as binding definition and E.4 as route dispatch | ACCEPTED |
| Step 4 must not be force-fired | Phase E roadmap requires `status: "deferred_until_reviewer_surface"` and says E.4 proof covers only steps 1-3 and 5 | ACCEPTED |
| E.3 does not require live proof | Phase E roadmap says E.3 tests pass and no runtime behavior change yet | ACCEPTED |

## Claim Boundary

This GC-018 authorizes only Tranche E.3. It does not authorize route dispatch,
workflow step firing, receipt persistence, live provider proof, public catalog
claim changes, or any change to `system_reconvergence_stop`.
