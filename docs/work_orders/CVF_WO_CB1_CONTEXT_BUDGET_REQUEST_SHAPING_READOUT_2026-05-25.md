# CVF Work Order CB1 Context Budget Request Shaping Readout

Memory class: SUMMARY_RECORD

Status: DISPATCHED_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT

docType: work_order

Date: 2026-05-25

---

## Purpose

Implement the CB1 deterministic context-budget/request-shaping readout
authorized by
`docs/baselines/CVF_GC018_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_2026-05-25.md`.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/commands/cvf-skill.test.ts`
- CB1 completion/session/handoff files

Forbidden:

- LLM scoring;
- runtime execution;
- provider/API calls;
- `/api/execute` changes;
- receipt-envelope changes;
- memory, MCP, database, or tool execution;
- public-sync, hosted readiness, production readiness, or freeze release.

## Authority Chain

- LH1 selected context-budget/request-shaping as the next highest-value
  absorption candidate.
- CB1 GC-018 authorizes only deterministic CLI readout.

## Agent Roles

- Implementer: add nested request-context readout to C8 selector.
- Auditor: verify no runtime context packager or reverse-brief execution claim.
- Product/operator advocate: ensure readout explains user action.
- Boundary owner: keep memory/tool/MCP/provider behavior closed.

## Allowed / Forbidden Scope

Allowed:

- request signal detection;
- missing-context detection;
- contamination/noise detection;
- budget tier/readiness classification;
- text and JSON readout formatting;
- focused tests.

Forbidden:

- storing request memory;
- using a provider to score context;
- invoking a selected pack;
- creating a new prompt runtime or profile engine.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/baselines/CVF_GC018_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_2026-05-25.md`
- C8 owner files and tests

## Pre-Flight Checks

- confirm worktree state;
- confirm LH1 is closed;
- confirm selected source files were read and listed in GC-018.

## Write Ownership

Implementation writes are limited to Governance CLI and CB1 documentation/session
continuity files.

## Execution Plan

1. Add request-context readout types and deterministic evaluator.
2. Nest request-context readout in `selectProductSkillPackForRequest`.
3. Surface summary in text output.
4. Add focused tests for ready, clarification, compaction, and contamination.
5. Run focused tests and TypeScript check.
6. File completion review and update active state/front door/handoff.
7. Commit.

## Evidence Requirements

Required evidence:

- focused `cvf skill` tests PASS;
- Governance CLI TypeScript check PASS;
- active state gate PASS;
- handoff guard PASS.

Live proof N/A because CB1 is deterministic local CLI readout only.

## Acceptance Criteria

- C8 selection JSON includes request-context readout;
- insufficient vague requests report `needs_clarification`;
- oversized/noisy requests report `needs_context_compaction`;
- implementation-heavy pseudo-brief requests report
  `blocked_contaminated_brief`;
- ready requests report `ready` with a budget tier;
- no runtime/provider/memory/tool surface changes.

## Review Gate

Before closure, verify the diff does not touch `/api/execute`, provider
adapters, memory stores, MCP/tool/database runtime, receipt schemas, or
public-sync.

## Closure Checklist

- [ ] implementation complete
- [ ] focused tests PASS
- [ ] TypeScript check PASS
- [ ] completion review filed
- [ ] active state/front door/handoff updated
- [ ] commit created

## Return-To-Orchestrator Conditions

Return blocked if useful request shaping requires LLM scoring, runtime context
packaging, or memory/tool/provider execution.

## Operator Checkpoint

No operator checkpoint is required unless scope expansion becomes necessary.

## Claim Boundary

CB1 closes only deterministic local request-context readout for Governance CLI
skill selection. It does not close runtime context packaging, reverse-brief
execution, memory injection, provider behavior, hosted readiness, production
readiness, or freeze release.
