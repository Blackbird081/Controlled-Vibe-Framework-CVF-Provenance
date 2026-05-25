# CVF Work Order VI1 W-Series Vertical Execute Chain

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-25

---

## Purpose

Implement the bounded VI1 vertical integration tranche authorized by
`docs/baselines/CVF_GC018_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_2026-05-25.md`.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts`
- VI1 completion/session/handoff files

Forbidden:

- new receipt envelope schema;
- broad workflow engine, route-level transition blocking, worker queue, or
  planner runtime;
- memory reinjection or raw memory prompt injection;
- MCP/tool/database/browser automation or external skill import;
- provider adapter semantics changes, public-sync, hosted readiness, production
  readiness, or freeze release.

## Authority Chain

- Claude review recommends vertical integration before more horizontal
  absorption.
- W1, WR1, W2, W6, Phase 2.C, and Phase 3.E are already closed bounded
  surfaces.
- VI1 authorizes only route response aggregation and live proof of an existing
  chain.

## Agent Roles

- Implementer: add the readout helper and route/test wiring.
- Auditor: verify no receipt/provider/workflow semantics are expanded.
- Product/operator advocate: make the response explain which chain surface is
  present or missing.
- Safety/boundary owner: preserve no-reinjection memory posture and live run
  diagnostics.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/baselines/CVF_GC018_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_2026-05-25.md`
- existing `/api/execute` route and surface helper files

## Pre-Flight Checks

- confirm clean worktree;
- confirm live keys can be loaded only through environment or `.env.local`;
- confirm the implementation can reuse existing W-series contracts;
- confirm no raw secret values are printed.

## Write Ownership

Writes are limited to the VI1 route helper, tests, type extension, completion,
and session continuity files.

## Execution Plan

1. Add typed vertical integration readout helper.
2. Extend execute request typing with optional chain descriptor.
3. Attach readout to `/api/execute` response.
4. Add focused unit/route tests, including 2-turn continuity.
5. Add live Alibaba-compatible 2-turn route proof.
6. Run focused tests, TypeScript check, live proof, and session guards.
7. File completion review, close this work order, update session/handoff, and
   commit.

## Evidence Requirements

Required evidence:

- focused VI1 readout tests PASS;
- route tests PASS;
- cvf-web TypeScript check PASS;
- live 2-turn `/api/execute` proof PASS with receipt IDs recorded secret-safe;
- active state gate PASS;
- handoff guard PASS.

If the live proof fails, classify the failure per Mandatory Live Run
Diagnostics before any rerun and do not claim live closure.

## Acceptance Criteria

- response-level `verticalIntegrationReadout` exists;
- at least five W-series/adjacent surfaces are reported together in successful
  product-brief route responses;
- second turn can reference first-turn receipt through chain metadata;
- memory hook reports no raw memory release and no reinjection;
- missing surfaces are visible as partial, not hidden.

## Review Gate

Before closure, verify the diff does not create a new receipt schema, new
workflow engine, new memory reinjection authority, provider adapter behavior,
external skill import, public-sync change, hosted readiness, production
readiness, or freeze release claim.

## Closure Checklist

- [ ] readout helper added
- [ ] route wiring complete
- [ ] unit/route tests PASS
- [ ] TypeScript check PASS
- [ ] live 2-turn proof PASS or diagnostic filed
- [ ] completion review filed
- [ ] active state/front door/handoff updated
- [ ] active state guard PASS
- [ ] handoff guard PASS
- [ ] commit created

## Return-To-Orchestrator Conditions

Return blocked if integration requires changing receipt envelope semantics,
adding workflow enforcement, enabling memory reinjection, or broadening provider
runtime behavior.

## Operator Checkpoint

No checkpoint is required unless live proof requires new keys, rerun after an
unclear failure, or scope expansion beyond the VI1 owner files.

## Claim Boundary

VI1 closes only bounded vertical response integration plus one 2-turn live
proof. It does not close broad workflow runtime, autonomous agent orchestration,
provider stability, hosted readiness, production readiness, or freeze release.
