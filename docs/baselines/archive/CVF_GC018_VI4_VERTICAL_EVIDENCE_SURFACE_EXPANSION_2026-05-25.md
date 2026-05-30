# CVF GC-018 VI4 Vertical Evidence Surface Expansion

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_VI4_VERTICAL_EVIDENCE_SURFACE_EXPANSION

docType: gc018_baseline

Date: 2026-05-25

---

## Purpose

Authorize VI4 as the combined B + evidence-packaging tranche: extend the
existing VI1 vertical aggregator with bounded W3, W4, W5, and TA1 evidence
surfaces, then package the result so API/operator readers can understand the
route chain without reading raw nested objects.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts`
- optional focused helper file under `cvf-web/src/lib`
- VI4 completion/session/handoff files

Allowed behavior:

- add response-level packaging for existing VI surfaces;
- add W3 tool/action taxonomy and TA1 approval readout as readout-only
  evidence derived from the existing route action;
- add W4 live-call operational scorecard packaging derived from the current
  live route receipt, with explicit event-model denominator;
- add W5 provider-method readiness/fallback posture derived from the current
  provider/model/method/result, with unsupported/failed states visible;
- update tests and one live Alibaba proof.

Forbidden:

- route-level blocking based on the new surfaces;
- tool/MCP/database/browser execution;
- provider adapter behavior or provider routing changes;
- new receipt envelope schema;
- runtime context injection or prompt mutation;
- memory reinjection or raw memory release;
- external skill import, public-sync, hosted readiness, production readiness,
  or freeze release.

## Source / Predecessor Evidence

Predecessors:

- `docs/reviews/CVF_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - W3 tool/MCP/database action taxonomy;
  - W4 operational benchmark scorecard and event denominator clarification;
  - W5 provider method fallback normalization;
  - TA1 tool action approval readout;
  - VI1-VI3 aggregator/readout files.
- Prior absorption evidence resolved:
  - W3/TA1 are local deterministic contracts and explicitly authorize no
    runtime execution;
  - W4 is an offline/evidence-ingest benchmark, so VI4 may only derive a
    current-call scorecard and must not claim a suite run;
  - W5 is a provider method/fallback readout, so VI4 may surface posture but
    must not change adapters or routing;
  - VI1-VI3 already prove the live route can carry vertical readouts.
- Detailed source files used:
  - `governance/contracts/tool-action-taxonomy.ts`
  - `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
  - `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Source families skipped:
  - workflow expansion beyond Product Brief;
  - DeepSeek/OpenAI provider-scale proof;
  - UI workflow scale and public-sync.
- File-level accepted value:
  - W3/TA1: tool/action risk and approval readout for the route action;
  - W4: call-level denominator clarity for one live route call;
  - W5: provider method readiness/failure posture for the current provider
    call;
  - packaging: concise operator summary and next action.
- Owner-surface normalization:
  - implement as response-level readout fields and VI surfaces, not as policy
    gates, adapters, or receipt schema changes.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: readout-only surfaces and concise evidence package.
  - DEFER_DEMAND_GATED: D provider-scale DeepSeek/OpenAI proof, C workflow
    scale, UI dashboard, public catalog.
  - REJECT_DIRECT: new execution authority, provider routing changes, MCP/tool
    execution, database connection, or broad benchmark claim.
- Adversarial roles completed:
  - Implementer: add small helper/readout and route response wiring.
  - Skeptic/Auditor: W4 must state this is current-call packaging, not the
    offline benchmark suite.
  - Product/Operator Advocate: response should be readable enough to diagnose
    what CVF controlled and what remains advisory.
  - Safety/Boundary Owner: W3/TA1 must preserve
    `runtimeExecutionAuthorized=false`.
- Thin proof target:
  - live Product Brief route response includes new surfaces and package while
    preserving VI status and existing route behavior.
- Blind-spot verdict: CLEAR.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_VI4_VERTICAL_EVIDENCE_SURFACE_EXPANSION.

Baseline:

- VI1-VI3 prove a route vertical chain but omit W3/W4/W5/TA1 surfaces.
- Claude's B proposal and Codex's evidence-packaging recommendation align.
- D and C remain valuable, but B/VI4 should come first so later provider and
  workflow proofs share a richer evidence surface.

Proposed tranche:

- add `cvf.verticalEvidencePackage.vi4.v1`;
- attach W3, W4, W5, and TA1 readout surfaces to VI;
- keep all new surfaces advisory/readout-only;
- run focused tests, TypeScript check, live Alibaba proof, session guards, and
  commit.

## Acceptance Criteria

- `verticalIntegrationReadout` includes W3, W4, W5, and TA1 surfaces;
- response exposes a concise VI4 evidence package;
- W3/TA1 preserve `runtimeExecutionAuthorized=false`;
- W4 reports both call-level and event-model denominator language;
- W5 reports provider-method readiness or failure posture without changing
  routing;
- no new route block, prompt mutation, provider routing change, tool execution,
  or receipt envelope change is introduced;
- focused tests and live proof pass.

## Verification Plan

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run -- src/lib/vertical-integration-readout.test.ts src/app/api/execute/route.test.ts
npm run check
npm run test:run -- src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts
cd ../../..
python governance/compat/check_active_session_state.py
python governance/compat/check_agent_handoff_guard_compat.py
```

## Claim Boundary

VI4 may claim only response-level evidence surface expansion and packaging for
the existing Product Brief `/api/execute` path. It does not prove DeepSeek or
OpenAI parity, workflow scale beyond Product Brief, broad provider reliability,
runtime tool/MCP/database execution, hosted readiness, production readiness,
public release readiness, or freeze release.
