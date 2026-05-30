# CVF Work Order C7C External Skill Candidate Record Validator

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-25

---

## Purpose

Implement the local deterministic validator/readout authorized by
`docs/baselines/CVF_GC018_C7C_EXTERNAL_SKILL_CANDIDATE_RECORD_VALIDATOR_2026-05-25.md`.

## Scope / Target / Owner Boundary

Allowed owner files:

- `governance/contracts/external-skill-candidate-screen.ts`
- `governance/contracts/external-skill-candidate-screen.test.ts`
- C7C completion/session/handoff files

Forbidden:

- external skill import;
- certified product pack creation/modification;
- registry publication or marketplace/public-sync claims;
- external tools, MCP, CLI, script, model, provider, browser, or database
  execution;
- live external repository fetch;
- `/api/execute`, receipt envelopes, auth/RBAC, hosted readiness, production
  readiness, or freeze release.

## Authority Chain

- ES1 created the pre-import screening standard.
- C7B ranked Candidate 7 source families and recommended a validator/readout.
- TA1 provides the local no-execution readout pattern.
- C7C authorizes only a local contract evaluator plus tests.

## Agent Roles

- Implementer: add the contract and focused tests.
- Auditor: verify no execution/import/registry authority appears.
- Product/operator advocate: keep diagnostics actionable for non-coder
  skill-candidate decisions.
- Safety/boundary owner: preserve `runtimeExecutionAuthorized=false`.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
- `docs/reference/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
- `docs/baselines/CVF_GC018_C7C_EXTERNAL_SKILL_CANDIDATE_RECORD_VALIDATOR_2026-05-25.md`

## Pre-Flight Checks

- confirm worktree state;
- confirm C7C GC-018 includes the Knowledge Absorption Blind-Spot Control
  Block;
- inspect existing governance/contracts style;
- confirm no parser, network fetch, registry write, or runtime execution is
  required.

## Write Ownership

Writes are limited to the C7C contract, tests, completion, and session
continuity files.

## Execution Plan

1. Add `external-skill-candidate-screen.ts` with typed record, evaluation, and
   readout.
2. Add focused tests for pass/defer/reject/incomplete scenarios.
3. Run focused and full governance/contracts tests.
4. File completion review and update session/handoff.
5. Run active state and handoff guards.
6. Commit.

## Evidence Requirements

Required evidence:

- focused C7C tests PASS;
- full `governance/contracts` tests PASS;
- active state guard PASS;
- handoff guard PASS.

Live proof N/A because C7C is local deterministic contract validation.

## Acceptance Criteria

- ES1 required fields are validated;
- C7B dilution/readiness fields are represented;
- unknown side effects and direct import are rejected;
- runtime/tool/provider/browser/database cases are deferred;
- duplicate/low-value candidates do not pass;
- `runtimeExecutionAuthorized=false` is invariant.

## Review Gate

Before closure, verify the diff does not modify registries, packs, runtime
code, provider adapters, MCP/database layers, `/api/execute`, receipt schemas,
auth/RBAC, public-sync, or external source files.

## Closure Checklist

- [x] contract added
- [x] tests added and PASS
- [x] completion review filed
- [x] active state/front door/handoff updated
- [x] active state guard PASS
- [x] handoff guard PASS
- [x] commit created

## Return-To-Orchestrator Conditions

Return blocked if implementation needs external skill import, live fetch,
registry publication, runtime execution, or a concrete candidate source beyond
a test fixture.

## Operator Checkpoint

No checkpoint is required unless a specific external source is selected for
actual import, registry admission, or runtime evaluation.

## Claim Boundary

C7C closes only a local candidate-record validator/readout. It does not close
external skill ingestion, runtime execution, registry publication, public
marketplace readiness, hosted readiness, production readiness, or freeze
release.
