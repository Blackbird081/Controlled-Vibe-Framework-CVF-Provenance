# CVF Work Order VI4 Vertical Evidence Surface Expansion

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-25

---

## Purpose

Implement the bounded VI4 vertical evidence surface expansion authorized by
`docs/baselines/CVF_GC018_VI4_VERTICAL_EVIDENCE_SURFACE_EXPANSION_2026-05-25.md`.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts`
- optional focused helper file under `cvf-web/src/lib`
- VI4 completion/session/handoff files

Forbidden:

- runtime tool/MCP/database/browser execution;
- provider adapter behavior or provider routing changes;
- route blocking based on W3/W4/W5/TA1 readouts;
- new receipt envelope schema;
- prompt mutation or runtime context injection;
- memory reinjection or raw memory release;
- public-sync, hosted readiness, production readiness, or freeze release.

## Agent Roles

- Implementer: add deterministic readout surfaces and response package.
- Auditor: verify no runtime authority, provider routing, or receipt envelope
  changes.
- Product/operator advocate: make VI chain readable for API/non-coder
  consumers.
- Safety/boundary owner: keep W3/TA1 `runtimeExecutionAuthorized=false` and W4
  denominator claims bounded to current-call packaging.

## Authority Chain

- VI1-VI3 closed route vertical integration, request context, and memory
  capture record readouts.
- Claude B proposal recommends W3/W4/W5/TA1 vertical wiring.
- Operator approved B+VI4 first, then D provider scale, then C workflow scale.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
- `docs/baselines/CVF_GC018_VI4_VERTICAL_EVIDENCE_SURFACE_EXPANSION_2026-05-25.md`
- `governance/contracts/tool-action-taxonomy.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts`

## Pre-Flight Checks

- confirm clean worktree after VI3 closure;
- confirm `/api/execute/route.ts` remains inside file-size guard;
- confirm all new surfaces are readout-only;
- confirm live key loading remains secret-safe.

## Write Ownership

Writes are limited to VI4 helper/readout files, route response wiring, tests,
completion review, and session continuity files.

## Execution Plan

1. Add VI4 evidence package/readout types and builders.
2. Attach W3, W4, W5, and TA1 surfaces to VI.
3. Wire route response with the smallest safe route diff.
4. Update unit/route/live assertions.
5. Run focused tests, check, live proof, session guards.
6. File completion review, close work order, update session/handoff, commit.

## Acceptance Criteria

- VI includes W3, W4, W5, and TA1 surfaces;
- response exposes concise VI4 evidence package;
- W3/TA1 preserve `runtimeExecutionAuthorized=false`;
- W4 reports call-level result and event-model denominator;
- W5 reports provider method readiness/failure posture without routing changes;
- focused tests, TypeScript check, live proof, and session guards pass.

## Evidence Requirements

- focused VI/route tests PASS;
- cvf-web TypeScript check PASS;
- live VI route proof PASS or diagnostic filed;
- active state guard PASS;
- handoff guard PASS.

## Review Gate

Before closure, verify the diff does not introduce tool/MCP/database/browser
execution, provider adapter or routing changes, route blocking, prompt
mutation, receipt envelope changes, memory reinjection, public-sync, hosted
readiness, production readiness, or freeze release.

## Closure Checklist

- [ ] VI4 evidence package added
- [ ] W3 surface attached
- [ ] W4 surface attached
- [ ] W5 surface attached
- [ ] TA1 surface attached
- [ ] focused tests PASS
- [ ] TypeScript check PASS
- [ ] live proof PASS or diagnostic filed
- [ ] completion review filed
- [ ] active state/front door/handoff updated
- [ ] active state guard PASS
- [ ] handoff guard PASS
- [ ] commit created

## Return-To-Orchestrator Conditions

Return blocked if implementation requires provider routing changes, a new
receipt envelope, tool/MCP/database execution, or broad benchmark/provider
stability claims.

## Operator Checkpoint

No checkpoint is required unless live proof lacks a usable key, an unclear live
failure needs a rerun, or implementation requires scope expansion beyond VI4.

## Claim Boundary

VI4 closes only Product Brief route evidence surface expansion and packaging.
It does not close D provider scale, C workflow scale, broad provider stability,
hosted readiness, production readiness, or freeze release.
