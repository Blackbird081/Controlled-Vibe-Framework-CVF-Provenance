# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-05-25

Current mode marker: `c7c_external_skill_candidate_record_validator_closed`

Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the single session-memory entry point for new agents, resumed
agents, future `cvf-cli`, and future `cvf-mcp-server` startup.

It is intentionally compact. The previous long front-door snapshot was archived
verbatim at
`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_C7A_REFRESH_ARCHIVE_2026-05-25.md`.

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff:
   `AGENT_HANDOFF_V13_2026-05-25.md`
5. Read mandatory startup guards listed in the state registry.

Pain-point closure direction:

`docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

Previous handoff archive:

`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V12_2026-05-23.md`

## Current State

Current mode: `c7c_external_skill_candidate_record_validator_closed`.

C7A closed PASS bounded at:

`docs/reviews/CVF_C7A_PRODUCT_SKILL_PACK_TOP10_COMPLETION_2026-05-25.md`

The certified product skill pack inventory now has ten unique static packs:

- `strategy_analysis`
- `product_brief`
- `sop_generator`
- `proposal_writer`
- `meeting_summarizer`
- `contract_review`
- `landing_page_builder`
- `competitor_review`
- `data_analysis`
- `app_requirements_spec`

Registry:

`governance/registries/cvf-certified-skill-pack-registry.json`

Validation evidence: `scripts/validate_skill_pack_certification.py` PASS for
all ten packs; registry check `entries=10 unique=10 c7a=3`.

## Candidate 7 Decision

Candidate 7 is not a green light for broad external ingestion.

What is closed:

- C7A completed the practical product-skill-pack inventory from seven to ten
  strong workflows using the existing T1/T2/W7 intake chain.

What remains held:

- external skill/model ingestion;
- direct tool execution;
- MCP or database action execution;
- provider/runtime behavior changes;
- public-sync or hosted/product-readiness claims.

Candidate 7 may reopen only with fresh GC-018, the mandatory Knowledge
Absorption Blind-Spot Control Block, and a concrete source/use-case binding.

## Latest Closed Tranche

LH1 legacy harvest closeout ledger is closed PASS bounded:

`docs/reviews/CVF_LH1_LEGACY_HARVEST_CLOSEOUT_LEDGER_COMPLETION_2026-05-25.md`

Closeout ledger:

`docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`

LH1 dispositioned every WC-3 source family, linked absorbed slices to W1-W6,
C7A, C8, AIF, and PBR evidence, and recorded the remaining high-value
absorption queue. It does not claim full legacy absorption.

C8 product skill pack selection/readout is closed PASS bounded:

`docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`

C8 delivered deterministic read-only `cvf skill select <request> [--json]`
over the ten certified packs, completed runtime bindings for
`competitor_review`, `data_analysis`, and `app_requirements_spec`, and surfaced
risk/human-review/no-match readout. Verification: focused Governance CLI
`cvf skill` tests PASS 10/10; Governance CLI TypeScript check PASS.

## Latest Closed Tranche

CB1 context-budget/request-shaping readout is closed PASS bounded:

`docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`

CB1 added deterministic local `cvf.productSkillPackRequestContext.v1` inside
Governance CLI `cvf skill select`, with budget tier, readiness, detected and
missing signals, contamination/noise flags, preservation priority, and next
action. Verification: focused Governance CLI `cvf skill` tests PASS 14/14;
Governance CLI TypeScript check PASS.

## Latest Closed Tranche

WR1 workflow recovery state proof is closed PASS bounded:

`docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`

Work order:

`docs/work_orders/CVF_WO_WR1_WORKFLOW_RECOVERY_STATE_PROOF_2026-05-25.md`

WR1 added deterministic local `cvf.workflowRecoveryReadout.wr1.v1` to the
Product Brief workflow projection, with checkpoint, invalid-transition
classification, reviewer-gate hold, escalation action, and explicit boundaries.
Verification: focused workflow resolver tests PASS 5/5; `cvf-web` TypeScript
check PASS.

Candidate 7 external skill/model ingestion remains held until there is a
concrete source/use-case binding.

## Latest Closed Tranche

TA1 tool/action approval readout is closed PASS bounded:

`docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`

Work order:

`docs/work_orders/CVF_WO_TA1_TOOL_ACTION_APPROVAL_READOUT_2026-05-25.md`

TA1 added deterministic local `cvf.toolActionApprovalReadout.ta1.v1` over W3
tool action taxonomy. It reports approval state, required/missing evidence,
next safe action, concise message, and explicit boundaries while preserving
`runtimeExecutionAuthorized=false`. Verification: focused taxonomy tests PASS
16/16; full `governance/contracts` tests PASS 114/114.

Do not add packs, runtime execution, provider behavior, receipt envelopes,
memory, MCP/tool/database execution, public-sync, hosted readiness, production
readiness, or freeze release without a new authorized tranche.

## Latest Closed Tranche

ES1 external skill intake screening packet is closed PASS bounded:

`docs/reviews/CVF_ES1_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_COMPLETION_2026-05-25.md`

Reference:

`docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`

ES1 added the docs-only pre-import filter for Candidate 7: source/use-case
requirement, value screen, duplicate/dilution screen against ten certified
packs, risk screen, normalization minimum, owner-surface routing, dispatch
dispositions, stop conditions, and required screening record. No external skill
import or runtime/public claim was opened.

## Latest Closed Tranche

C7B Candidate 7 external skill source screening matrix is closed PASS bounded:

`docs/reviews/CVF_C7B_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_COMPLETION_2026-05-25.md`

Reference:

`docs/reference/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`

C7B audited Hugging Face, Hermes Agent, Memento-Skills, Agent Engineer, and the
local skillsmp shortlist as evidence only. It accepted normalization/package/
evolution/schema-contract patterns, deferred runtime/import/registry/new-pack
work, and recommended C7C external skill candidate record validator/readout as
the next highest-value bounded tranche.

## Latest Closed Tranche

C7C External Skill Candidate Record Validator is closed PASS bounded:

`docs/reviews/CVF_C7C_EXTERNAL_SKILL_CANDIDATE_RECORD_VALIDATOR_COMPLETION_2026-05-25.md`

Implementation:

`governance/contracts/external-skill-candidate-screen.ts`

Tests:

`governance/contracts/external-skill-candidate-screen.test.ts`

C7C added local deterministic `cvf.externalSkillCandidateScreen.c7c.v1`.
Focused tests PASS 9/9; full `governance/contracts` tests PASS 123/123. It
does not import external skills, modify packs, publish registries, execute
tools/MCP/CLI/scripts/models/providers, fetch live external repositories, make
public-sync/marketplace claims, or touch `/api/execute`, receipt envelopes,
auth/RBAC, hosted readiness, production readiness, or freeze release.

## Latest Closed Tranche

VI1 W-Series Vertical Execute Chain is closed PASS bounded:

Mode marker: `vi1_w_series_vertical_execute_chain_closed`

`docs/reviews/CVF_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_COMPLETION_2026-05-25.md`

Authorization:

`docs/baselines/CVF_GC018_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_2026-05-25.md`

Work order:

`docs/work_orders/CVF_WO_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_2026-05-25.md`

VI1 added `cvf.verticalWorkflowIntegration.vi1.v1`, optional
`verticalIntegrationChain` typing, `/api/execute` response wiring, and
unit/route/live tests. Live Alibaba-compatible 2-turn proof PASS:
turn 1 `rcpt-env-mpkh0117-b27yr9`, turn 2
`rcpt-env-mpkh0dbw-kvohgm`. Second turn asserted `status=integrated`,
`integratedSurfaceCount=6`, `requiredSurfaceCount=5`,
`continuityProven=true`, and W2 memory hook
`rawMemoryReleased=false` / `canReinject=false`.

Verification: focused VI1/route tests PASS 33/33, cvf-web check PASS, live
VI1 test PASS 1/1.

Recommended next work is VI2 candidate selection for vertical-adjacent
horizontal absorption only after fresh GC-018: choose caveman context engine
wiring, Workflow GoClaw runtime normalization, or agentmemory event capture
only if it adds concrete diagnostic value to `verticalIntegrationReadout`
without widening runtime authority.

Do not create a new receipt envelope schema, workflow engine, route-level
transition blocking, memory reinjection, MCP/tool/database/browser automation,
external skill import, provider adapter semantic change, public-sync claim,
hosted readiness, production readiness, or freeze release.

## Latest Closed Tranche

VI2 Route Request Context Profile Readout is closed PASS bounded:

Mode marker: `vi2_route_request_context_profile_readout_closed`

`docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`

Authorization:

`docs/baselines/CVF_GC018_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_2026-05-25.md`

Work order:

`docs/work_orders/CVF_WO_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_2026-05-25.md`

VI2 selects caveman context budgeting/relevance plus Workflow GoClaw context
profile/guardrail concepts as the next vertical-adjacent source because CB1
proved the value in CLI, while `/api/execute` still lacks request-context
readiness/profile visibility inside `verticalIntegrationReadout`. Agentmemory
event capture is deferred because VI1 already wires W2 memory hook and audit
memory receipt into the route chain.

Delivered: deterministic `cvf.routeRequestContextProfile.vi2.v1`,
response-level `requestContextReadout`, and `request_context_profile` surface
on `verticalIntegrationReadout`. Successful route responses now expose profile,
budget tier, readiness, signal/noise/contamination fields, execution ceiling,
next action, and boundaries. Live VI route proof PASS: turn 1
`rcpt-env-mpkjdbnb-8jl53i`, turn 2 `rcpt-env-mpkjdnuv-e7os02`.

Forbidden: runtime context injection, prompt mutation, route blocking based on
context profile, receipt-envelope change, LLM scoring, provider routing change,
memory reinjection, MCP/tool/database/browser automation, external skill
import, public-sync, hosted readiness, production readiness, or freeze release.

Recommended next work needs fresh GC-018 and value screen. Prefer a VI3 that
makes existing live route behavior easier to diagnose, such as bounded
agentmemory capture expansion or an operator-facing readout display, instead
of broad horizontal absorption.

## Latest Closed Tranche

VI3 Agentmemory Capture Record Readout is closed PASS bounded:

Mode marker: `vi3_agentmemory_capture_record_readout_closed`

`docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`

Authorization:

`docs/baselines/CVF_GC018_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_2026-05-25.md`

Work order:

`docs/work_orders/CVF_WO_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_2026-05-25.md`

VI3 selected the agentmemory hook/capture contract as the next bounded
vertical-adjacent source. Delivered response-level
`auditMemoryReceipt.captureRecord` and VI memory surface references to capture
event/audit receipt ids. Live VI proof PASS: turn 1
`rcpt-env-mpkjrcho-bped1p`, turn 2 `rcpt-env-mpkjrojq-o9wc3n`. Focused tests
PASS 42/42; cvf-web check PASS; route.ts unchanged at 999 lines.

Forbidden: editing `/api/execute/route.ts`, memory reinjection, direct memory
search/write beyond the existing governed audit capture, automatic memory
promotion, external memory adapters, provider routing changes, receipt-envelope
changes, MCP/tool/database/browser automation, public-sync, hosted readiness,
production readiness, or freeze release.

Recommended next work requires fresh GC-018. Prefer operator/API evidence
packaging that exposes VI1-VI3 response diagnostics to non-coder/API consumers
without changing runtime authority.

## Mandatory Standards

Live run diagnostics:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

Knowledge absorption blind-spot prevention:

`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Every GC-018 memory/graph/intelligence tranche must include the Knowledge
Absorption Blind-Spot Control Block.

## Boundary

This front door is routing state only. It does not replace evidence packets,
roadmaps, handoffs, governance guards, or the machine-readable state registry.

Do not continue broad F-1 tuning. Do not claim output-quality parity. Do not
push public-facing changes from this provenance workspace.
