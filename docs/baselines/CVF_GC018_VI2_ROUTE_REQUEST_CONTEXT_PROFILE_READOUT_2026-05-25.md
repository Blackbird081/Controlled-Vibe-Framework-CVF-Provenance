# CVF GC-018 VI2 Route Request Context Profile Readout

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT

docType: gc018_baseline

Date: 2026-05-25

---

## Purpose

Authorize VI2 as the selected vertical-adjacent horizontal absorption tranche
after VI1.

VI2 wires the highest-value remaining context/profile source into the live
`/api/execute` vertical chain: deterministic request-context readiness and
context-profile readout from `caveman` plus Workflow GoClaw, using CB1 as the
prior CLI proof.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts`
- VI2 completion/session/handoff files

Allowed behavior:

- add response-level `requestContextReadout`;
- add a `request_context_profile` surface to `verticalIntegrationReadout`;
- classify route request readiness, context budget/profile, missing signals,
  contamination/noise flags, and next action;
- run focused tests and one live `/api/execute` proof through the existing VI1
  live spec updated for the new surface.

Forbidden:

- runtime context injection or prompt mutation beyond existing route behavior;
- LLM scoring or model selection changes;
- new receipt envelope schema;
- route-level blocking based on context readiness;
- memory reinjection or raw memory release;
- MCP/tool/database/browser automation;
- provider adapter semantic changes, external skill import, public-sync,
  hosted readiness, production readiness, or freeze release.

## Source / Predecessor Evidence

Predecessors:

- `docs/reviews/CVF_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `.private_reference/legacy/CVF ADD/caveman/CVF_CONTEXT_BUDGETING_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/caveman/CVF_RELEVANCE_FILTERING_SPEC.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_PROFILE_MODEL.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_PACKAGING_POLICY.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_GUARDRAIL_RULEBOOK.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_EXECUTION_PROFILE_BINDING.md`

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - caveman context budgeting and relevance filtering;
  - Workflow GoClaw context profile, packaging policy, guardrail rulebook, and
    execution-profile binding;
  - CB1 Governance CLI request-context readout;
  - VI1 route vertical integration readout;
  - agentmemory capture/event-hook files as the non-selected comparator.
- Prior absorption evidence resolved:
  - CB1 already absorbed context budgeting/readiness into Governance CLI only.
  - VI1 already surfaced W2 memory event hook and audit memory receipt in the
    route chain.
  - LH1 leaves caveman/GoClaw as deferred until selector or route context grows.
- Detailed source files used:
  - `.private_reference/legacy/CVF ADD/caveman/CVF_CONTEXT_BUDGETING_PROTOCOL.md`
  - `.private_reference/legacy/CVF ADD/caveman/CVF_RELEVANCE_FILTERING_SPEC.md`
  - `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_PROFILE_MODEL.md`
  - `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_PACKAGING_POLICY.md`
  - `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_GUARDRAIL_RULEBOOK.md`
  - `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_EXECUTION_PROFILE_BINDING.md`
  - `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_EVENT_HOOKS.md`
  - `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_CAPTURE_ADAPTER.md`
  - `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- Source families skipped:
  - direct GoClaw cache/learning loop;
  - agentmemory capture expansion beyond the already wired W2 event hook;
  - any external context engine/runtime import.
- File-level accepted value:
  - caveman -> deterministic budget tier, relevance, missing-signal, and noise
    classification;
  - Workflow GoClaw -> context profile, allowed/excluded surfaces, guardrails,
    execution ceiling, and traceability;
  - CB1 -> conservative heuristic shape already proven locally;
  - VI1 -> route-level vertical surface attachment.
- Owner-surface normalization:
  - implement as a `cvf-web/src/lib` readout and a new VI surface, not a prompt
    builder, context injector, cache, profile runtime, or policy gate.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: response-level request context/profile readout.
  - DEFER_DEMAND_GATED: runtime context packager, profile escalation, cache
    boundary, learning loop, UI visualization, and reverse-brief flow.
  - REJECT_DIRECT: changing provider selection, mutating prompt context,
    blocking route execution, or enabling memory/tool/MCP access from profile.
- Adversarial roles completed:
  - Implementer: smallest proof is one deterministic helper plus VI readout
    surface.
  - Skeptic/Auditor: readout must not become a route block or hidden prompt
    mutation.
  - Product/Operator Advocate: this reduces wasted live calls by making vague,
    noisy, or contaminated route requests visible in the same live receipt
    chain.
  - Safety/Boundary Owner: profile selection is advisory and subordinate to
    existing governance.
- Thin proof target:
  - live Product Brief route response reports `request_context_profile` present
    in `verticalIntegrationReadout` without changing execution behavior.
- Blind-spot verdict: CLEAR.

## Candidate Selection

Selected: route request-context/profile readout from `caveman` + Workflow
GoClaw.

Rejected for VI2 now:

- agentmemory event capture wire-in: valuable, but VI1 already wires W2 hook +
  audit memory receipt, so marginal route value is lower without a broader
  memory-capture tranche.
- Workflow GoClaw runtime/cache/learning loop: valuable, but runtime/cache
  behavior would exceed a readout-only VI2.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT.

Baseline:

- VI1 proves the `/api/execute` vertical chain but does not show whether the
  incoming request had enough context, too much noise, or contamination risk.
- CB1 proves deterministic request-context readiness in Governance CLI, but not
  in live route responses.
- caveman and Workflow GoClaw provide the highest-value route-adjacent source
  family because their value can be surfaced as diagnostics without changing
  prompt/provider behavior.

Proposed tranche:

- add `cvf.routeRequestContextProfile.vi2.v1`;
- add route response `requestContextReadout`;
- add `request_context_profile` to `verticalIntegrationReadout`;
- update tests and live proof to assert the new surface.

## Acceptance Criteria

- route response includes `requestContextReadout`;
- vertical readout includes `request_context_profile` surface;
- readout reports profile, budget tier, readiness, detected/missing signals,
  noise/contamination flags, execution ceiling, and boundaries;
- no route block or prompt mutation is introduced;
- focused tests pass;
- live VI route proof passes with the new surface present.

## Verification Plan

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run -- src/lib/route-request-context-readout.test.ts src/lib/vertical-integration-readout.test.ts src/app/api/execute/route.test.ts
npm run check
npm run test:run -- src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts
cd ../../..
python governance/compat/check_active_session_state.py
python governance/compat/check_agent_handoff_guard_compat.py
```

## Claim Boundary

VI2 may claim only a deterministic response-level route request-context/profile
readout attached to the VI chain. It does not claim runtime context packaging,
prompt mutation, profile enforcement, provider selection, memory reinjection,
external execution, hosted readiness, production readiness, public release
readiness, or freeze release.
