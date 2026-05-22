# CVF Work Order - B/C Product Outcome Runtime and CLI Distribution

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

Date: 2026-05-22

## Purpose

Close Review CVF Problem B and Problem C cleanly by adding product-outcome
runtime plans for certified skill packs and package-level installable CLI
semantics for `cvf`.

## Authority Chain

- Operator request: 2026-05-22, "Tôi muốn hoàn tất, không để nó mãi là pain point".
- GC-018: `docs/baselines/CVF_GC018_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_2026-05-22.md`
- Predecessor completions:
  - `docs/reviews/CVF_T2_PRODUCT_SKILL_PACK_MVP_COMPLETION_2026-05-22.md`
  - `docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`
  - `docs/reviews/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`

## Agent Roles

- Orchestrator: preserve B/C scope and prevent route/provider/receipt drift.
- Reviewer: check that the runtime plan delegates to existing execution truth.
- Implementer: add package code, tests, and package scripts.
- Auditor: run targeted tests, build/bin smoke, full CLI tests, and governance
  guards.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/baselines/CVF_GC018_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_2026-05-22.md`
- `docs/reviews/CVF_CANONICAL_CLI_RUNTIME_GATEWAY_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_T3_WORKFLOW_COMPOSITION_OUTCOME_SURFACE_COMPLETION_2026-05-22.md`

## Pre-Flight Checks

Before editing code:

- confirm worktree status;
- confirm no public-sync repository changes are involved;
- confirm the existing execute owner remains `cvf-web /api/execute`;
- confirm package-level CLI is the only distribution surface in scope.

## Scope / Target / Owner Boundary

Target files may include:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/bin/cvf.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/package.json`
- focused tests under `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/`

Out of scope:

- no `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  changes;
- no provider adapter changes;
- no receipt-envelope type changes;
- no durable memory or database changes;
- no public-sync changes.

## Write Ownership

Codex owns this tranche's changes inside the Governance CLI package and the
new B/C governance docs only. Existing user-authored unrelated changes must not
be reverted.

## Execution Plan

1. Add `ProductOutcomeRuntimePlan` helpers that load the certified pack registry
   and map every certified pack to an existing execute template.
2. Add `cvf skill plan <pack-or-outcome>` for runtime-plan inspection.
3. Extend `cvf run <pack-or-outcome>` to resolve certified pack IDs/outcome keys
   into existing execute templates before delegation.
4. Add a package `bin` entrypoint and build/bin smoke scripts.
5. Add JSON output behavior at the binary boundary.
6. Add focused tests for all certified pack plans, `skill plan`, `run`
   resolution, and bin smoke.
7. File completion and structural review artifacts.

## Review Gate

The tranche may close only if:

- all seven certified packs have runtime plans;
- every runtime plan references an existing receipt schema and failure recovery
  path;
- `cvf run` still delegates to the existing execute client;
- package build and bin smoke pass;
- no route/provider/receipt-envelope/public-sync changes are present.

## Evidence Requirements

Required evidence:

- runtime-plan tests prove all seven certified packs have executable plans;
- `cvf skill plan` tests prove inspectable plan output;
- `cvf run <certified-pack> --dry-run` tests prove execute-template resolution;
- package build/bin smoke proves `cvf` binary semantics;
- full Governance CLI tests prove existing CLI behavior remains intact;
- governance hook chain proves repository guard compliance.

## Acceptance Criteria

Accept only if:

- `ProductOutcomeRuntimePlan` exists and covers every certified pack in
  `governance/registries/cvf-certified-skill-pack-registry.json`;
- each runtime plan names an existing execute template and existing pack
  artifacts;
- `cvf skill list --certified` and `cvf skill plan <id>` work;
- `cvf run <certified-pack>` delegates through the existing execute client;
- `package.json` declares `cvf` and `cvf-guard` bins;
- JSON output mode works at the binary boundary;
- no route, provider, receipt-envelope, durable state, or public-sync changes
  are required.

## Closure Checklist

- Completion review filed.
- GC-019 structural review filed if the foundational guard requires it.
- Incremental test log updated.
- Active review queue, session state, session memory, and handoff updated.
- Local governance hook chain passes.
- Commit created.

## Operator Checkpoint

No mid-tranche operator checkpoint is required unless implementation would
touch route behavior, provider behavior, receipt envelopes, durable memory, or
public-sync.

## Return-to-Orchestrator Conditions

Return to the operator instead of continuing if:

- live provider proof becomes mandatory for a claim that cannot be proven with
  available keys;
- package build requires broad module-system migration outside the CLI package;
- route/provider/receipt changes become necessary to pass tests.

## Claim Boundary

This work order closes B/C at the product-outcome plan and package-level CLI
distribution layer only. It does not claim public npm release, hosted SaaS
readiness, public-sync publication, provider parity, new execution semantics,
new receipt envelopes, or durable runtime state.
