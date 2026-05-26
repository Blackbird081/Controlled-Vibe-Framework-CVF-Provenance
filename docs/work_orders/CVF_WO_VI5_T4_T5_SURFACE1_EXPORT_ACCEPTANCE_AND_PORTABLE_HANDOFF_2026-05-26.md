# CVF Work Order VI5-T4/T5 Surface 1 Export Acceptance And Portable Handoff

Memory class: WORK_ORDER_RECORD

docType: work_order

Date: 2026-05-26

Status: READY_FOR_OPERATOR_ACCEPTANCE

## Purpose

Implement the bounded VI5-T4/T5 roadmap:

- T4: prepare Surface 1 real non-coder export acceptance.
- T5: improve the English `app_builder_complete` export with portable
  external-agent handoff readiness.

## Authority Chain

Operator request -> VI5 Surface Fidelity correction -> GC-018 baseline ->
bounded work order. The operator's manual verdict remains authoritative for
T4 acceptance.

## Agent Roles

- Orchestrator: keep scope bounded to Surface 1 and update handoff state.
- Implementer: change the deterministic export renderer.
- QA role: verify inclusion, exclusion, and source-value preservation.
- Reviewer role: enforce claim boundary and operator acceptance status.

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
- `docs/reviews/CVF_VI5_SURFACE_FIDELITY_CODEX_RESPONSE_2026-05-26.md`

## Pre-Flight Checks

- Confirm current target is Surface 1 web export, not Surface 2 freeze output.
- Confirm `app_builder_complete` is the only template in scope.
- Confirm no live provider proof is needed for deterministic renderer content.

## Scope / Target / Owner Boundary

Files allowed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-export-portable-handoff.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.test.tsx`
- docs for roadmap, GC-018, completion, and session handoff.

Do not modify:

- provider adapters;
- `/api/execute`;
- receipt schemas;
- live benchmark runners;
- public-sync until private completion passes.

## Write Ownership

Owned writes are limited to the renderer, focused tests, roadmap/baseline/work
order/completion docs, and active handoff/session state.

## Execution Plan

1. Add the bounded handoff readiness block.
2. Add tests for English full inclusion and unrelated-surface exclusion.
3. Run focused web checks.
4. Update completion and handoff state.
5. Commit private provenance state.

## Tasks

- [x] Add portable handoff readiness block to English full export for
  `app_builder_complete`.
- [x] Include operator/external-agent acceptance checklist in the exported
  packet.
- [x] Preserve Vietnamese user-entered source values.
- [x] Add focused tests.
- [x] Run focused tests and `npm run check`.
- [x] Close with completion packet and handoff update.

## Evidence Requirements

- Focused unit tests pass.
- `npm run check` passes.
- Governance compatibility checks pass before commit.
- Operator acceptance remains explicitly pending.

## Acceptance Criteria

- The exported English full packet contains `Portable Agent Handoff Readiness`.
- The packet includes receiving-agent mission, source-value handling, and
  operator review gate.
- The block is absent from unrelated export surfaces.
- No provider, receipt, or API behavior is changed.

## Review Gate

Review must reject the work if it claims external-agent success before the
operator's real export test, or if it treats Vietnamese user values as export
chrome leakage.

## Closure Checklist

- [x] Implementation complete.
- [x] Focused tests complete.
- [x] Completion packet prepared.
- [x] Handoff state updated to `READY_FOR_OPERATOR_ACCEPTANCE`.
- [ ] Operator manual export and external-agent review complete.

## Return-To-Orchestrator Conditions

Return to implementation only if the operator's external-agent test reports
`HOLD`, or if the fresh web export does not contain the readiness block.

## Operator Checkpoint

The operator should export a fresh `app_builder_complete` English full spec
from the web surface and send it to an external agent for `PASS`,
`PASS_WITH_MINOR_FIX`, or `HOLD`.

## Closure Note

Implementation is complete and ready for operator manual acceptance. Final T4
PASS/HOLD remains dependent on the operator exporting a fresh web spec and
testing it with an external agent.

## Completion Criteria

The work order can close when:

- deterministic tests pass;
- the exported English full spec contains the readiness block;
- known Vietnamese chrome leak strings remain absent;
- private session state records operator manual test as next allowed move.

## Claim Boundary

Final claim before operator testing is readiness only. This work order does not
claim that external agents will build correctly, that all templates are
portable, or that provider governance behavior changed.
