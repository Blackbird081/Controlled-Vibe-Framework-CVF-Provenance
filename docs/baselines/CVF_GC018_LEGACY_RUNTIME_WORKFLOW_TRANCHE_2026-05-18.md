# GC-018 Authorization - Legacy Runtime Workflow Tranche

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-LEGACY-PHASE-D-RUNTIME-WORKFLOW
- Date: 2026-05-18
- Parent roadmap / wave: docs/reviews/CVF_PHASE_D_FULL_ROADMAP_FOR_CODEX_2026-05-18.md
- Proposed scope: implement a bounded runtime workflow contract slice covering
  runtime failure states, guard enforcement points, tool/MCP/command/database
  action classes, workflow transition receipt requirements, and operational
  benchmark extension metadata.
- Continuation class: STRUCTURAL_CONTRACT
- Active quality assessment: docs/reviews/CVF_LEGACY_PHASE_C_GAP_TRIAGE_FOR_IMPLEMENTATION_2026-05-18.md
- Assessment date: 2026-05-18
- Weighted total: 8/10
- Lowest dimension: Runtime completeness (1/2 until product execution paths
  consume the contract)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Tranche 2 ORCHESTRATOR and
  Tranche 5 Memory continuity have now defined the worker and memory boundaries
  that runtime workflow needs to model failure and receipt edges without
  widening provider execution.
- Quality protection commitments: (1) Do not alter live guard dispatch. (2) Do
  not change provider routing or live execution. (3) Do not claim complete
  runtime enforcement. (4) Keep this tranche deterministic and contract-local.
- Why now: GAP-17.05-004, GAP-17.05-010, GAP-17.05-012, GAP-17.05-013, and
  GAP-17.05-015 block runtime workflow and Agent OS claims.
- Active-path impact: NONE for governed AI dispatch; deterministic contract
  only.
- Risk if deferred: matrix/ledger rows would retain untyped runtime workflow
  failure and action boundaries, making later runtime work ambiguous.
- Lateral alternative considered: YES
- Why not lateral shift: provider method work remains demand-gated and cannot
  safely start before runtime workflow contract boundaries exist.
- Real decision boundary improved: YES, later runtime work can distinguish
  typed workflow/failure/action metadata from live enforcement.
- Expected enforcement class: CI_REPO_GATE by deterministic contract tests.
- Required evidence if approved:
  - Runtime failure state vocabulary includes policy_denied, gate_timeout,
    provider_error, worker_overreach, memory_write_violation, and receipt_missing.
  - Guard enforcement points are named and phase-bound.
  - Tool action class vocabulary covers current tool/MCP/command/database
    surfaces.
  - Workflow transitions require receipts for mutation and approval transitions.
  - Failure simulations for worker_overreach and memory_write_violation route
    to denied state with receipt requirement.
```

## Purpose

Authorize Phase D Tranche 3: Runtime workflow contract absorption.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_GUARD_CONTRACT` contract surface.

Owner: CVF guard contract package.

Authorized deterministic scope:

- `RuntimeFailureState` vocabulary;
- `GuardEnforcementPoint` metadata;
- `ToolActionClass` vocabulary;
- `WorkflowTransition` state edge metadata;
- `OperationalBenchmarkExtension` schema;
- deterministic failure simulation helpers and tests.

Explicitly out of scope:

- live guard dispatch changes;
- provider routing or provider API behavior;
- new tool execution behavior;
- live metric emission;
- complete runtime enforcement or Agent OS claims.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-LEGACY-PHASE-D-RUNTIME-WORKFLOW
- Depth Audit total: 8/10
- Proposed tranche: Legacy Runtime workflow contract tranche
- Live proof: not required for this bounded implementation because it does not
  change live governed AI dispatch, provider routing, tool execution, or live
  metric emission. Later runtime consumption of the contract will require live
  proof if it affects governed AI calls.

## Evidence / Required Evidence / Verification

Required evidence:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`
- deterministic tests proving vocabulary coverage, guard enforcement point
  metadata, receipt requirements, and failure simulation decisions
- `npm run test -- --run src/contracts/contracts.phaseD-runtime-workflow.test.ts`
- `npm run check`

## Source Authorization

Phase D full roadmap:

- `docs/reviews/CVF_PHASE_D_FULL_ROADMAP_FOR_CODEX_2026-05-18.md`

Prerequisites delivered:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`

## Claim Boundary

This GC-018 authorizes deterministic runtime workflow contract work only. It
does not authorize live runtime enforcement changes, provider execution
changes, public claim expansion, or lifting `system_reconvergence_stop`.
