# CVF 17.05 Legacy Absorption Gap Ledger - 2026-05-18

Memory class: FULL_RECORD

Status: ACTIVE GAP LEDGER

## Purpose

Track gaps discovered while completing or reviewing the 17.05 converged
roadmap, especially gaps that surface scans do not catch because the source
concept exists only in legacy/private design material.

This ledger exists so agents can finish bounded, authorized roadmap work
without silently absorbing new scope or losing discovered gaps.

## Scope / Target / Owner Boundary

Target: gaps discovered during 17.05 roadmap completion, surface scans, or
legacy/private source review.

Owner: CVF session-continuity and legacy absorption review surface.

In scope:

- missing or partially absorbed concepts found in `.private_reference/legacy/`;
- surface-scan misses that affect future GC-018 packets;
- deferred role, permission, orchestration, receipt, memory, policy, risk,
  guard, provider, or runtime concepts that need later review.

Out of scope:

- implementing any recorded gap;
- changing runtime behavior;
- changing public claims, release gates, or GA posture;
- promoting private legacy material into public canon.

## Target / Source Under Review

Primary sources under review:

- `.private_reference/legacy/`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/`
- `.private_reference/legacy/CVF 16.5/Claude Kit/`
- `AGENT_HANDOFF_V9_2026-05-18.md`
- `scripts/run_cvf_17_05_drift_inventory.py`
- `docs/reviews/archive/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`

## Scope / Methodology

This ledger uses two methods:

- Surface scan: identify duplicated or drifted implemented surfaces.
- Legacy absorption audit: compare preserved legacy design intent against
  current CVF implementation and contracts.

Only the second method can catch concepts that were never implemented or were
flattened during previous absorption.

## Operating Rule

When a surface scan, roadmap implementation, or legacy folder read discovers a
missing or partially absorbed concept:

1. Record the gap here with source evidence, current CVF evidence, and proposed
   disposition.
2. Do not implement it immediately unless the gap invalidates the active
   handoff, active-state registry, governance guard, or current phase acceptance
   criteria.
3. Defer implementation to a later legacy absorption audit or a fresh GC-018
   roadmap.
4. Before Phase 2.B runtime wire-up, run both:
   - surface scan for duplicated/drifted implemented surfaces;
   - legacy absorption audit for source concepts that were never implemented or
     were flattened during earlier absorption.

## Current Decision

Finish the already authorized 17.05 roadmap sequence first. Do not turn
every newly discovered legacy gap into immediate implementation work.

Handle new discoveries as follows:

| Discovery type | Action |
|---|---|
| Active handoff, registry, guard, test, or acceptance-criteria contradiction | Fix immediately and record the fix here |
| Missing/partial legacy concept without current-phase blocker | Record here; defer to legacy absorption audit |
| New runtime semantics, new role taxonomy, new policy/risk/guard behavior, new receipt/memory layer | Record here; requires fresh GC-018 before implementation |
| Public claim or release-gate implication | Record here; do not change public claims without live governance proof and explicit authorization |

## Findings / Position

The current position is that the 17.05 roadmap may be completed as bounded
contract and schema work, while newly discovered gaps are recorded for later
legacy absorption review. ORCHESTRATOR and agent role permission gaps are
examples of this rule.

## Risk / Corrective Action

Risk:

- Treating every discovered gap as immediate implementation work would reopen
  broad absorption under the `system_reconvergence_stop` posture.
- Treating completed surface scans as full absorption proof would create false
  confidence because unimplemented legacy concepts are invisible to those
  scans.

Corrective action:

- Record discovered gaps here.
- Require both surface scan and legacy absorption audit before Phase 2.B
  runtime wire-up.
- Require fresh GC-018 before implementing new runtime semantics or new
  contract surfaces.

## Decision / Recommendation / Disposition

Decision: continue the bounded roadmap to closure, then handle recorded gaps in
a dedicated legacy absorption audit or separately authorized phase.

Recommendation: do not claim full role/orchestration absorption until the
legacy role catalog, permission profile, orchestration rules, audit receipt,
handoff contract, risk policy, registry spec, and adapter boundary have been
reviewed against current contracts and either implemented under GC-018 or
explicitly rejected.

Current dispositions are listed per entry below.

Phase A freeze pointer: accepted at HEAD `ffae9346` by
`docs/reviews/CVF_LEGACY_ABSORPTION_PHASE_A_FREEZE_2026-05-18.md`.

## Controlled Vocabulary

All future structured entries in this ledger must use exactly these six
dispositions:

| Disposition | Meaning |
|---|---|
| `absorbed` | current CVF has an implemented or canonical surface matching the concept |
| `partially_absorbed` | current CVF has pieces, but composition or enforcement is incomplete |
| `doc_only` | current CVF has doctrine/docs but no enforceable runtime binding |
| `not_absorbed` | no current CVF owner surface exists |
| `rejected_or_superseded` | concept is reference-only or intentionally replaced |
| `needs_gc018` | concept is ready for a future tranche but must not be implemented without GC-018 |

Severity values:

`blocker | high | medium | low | noise`

## Structured Gap Crosswalk

This table upgrades the original freeform entries with concept axis, current CVF
files, controlled disposition, severity, dependency, and proposed tranche. It is
the controlling scan view until the freeform entries are rewritten individually.

| GAP ID | Matrix rows | Concept axis | Current CVF files | Disposition | Severity | Blocks | Depends on | Proposed tranche |
|---|---|---|---|---|---|---|---|---|
| GAP-17.05-001 | 3.1, 3.2, 3.3 | orchestrator | `docs/reviews/archive/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts` | `partially_absorbed` | high | full ORCHESTRATOR runtime; broad Phase 2.B orchestration semantics | GAP-17.05-002 | live runtime enforcement requires fresh GC-018 |
| GAP-17.05-002 | 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3 | role; permission | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts`; `EXTENSIONS/CVF_ECO_v2.3_AGENT_IDENTITY/src/agent.registry.ts` | `needs_gc018` | blocker | broad Phase 2.B runtime wire-up; full agent role governance claim | GAP-17.05-003 | Role/Permission tranche |
| GAP-17.05-003 | all high/blocker rows | benchmark; agent OS | `scripts/run_cvf_17_05_drift_inventory.py`; `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md` | `needs_gc018` | high | Phase A knowledge-map freeze; all later absorption tranches | none | none |
| GAP-17.05-004 | 4.1, 4.2, 7.1 | runtime; workflow | `docs/reviews/CVF_17_05_PHASE_2B_PREFLIGHT_OWNER_MIGRATION_PLAN_2026-05-18.md`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phase2b-wireup.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | medium | broad Phase 2.B runtime expansion and live workflow consumption | GAP-17.05-001; GAP-17.05-002 | none for contract-local tranche; runtime consumption requires fresh GC-018 |
| GAP-17.05-005 | 1.1, 2.1, 3.1, 4.3, 5.2, 11.2 | role; orchestrator; runtime; memory | `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md` | `needs_gc018` | high | full Agent OS / role-permission / orchestration claim | GAP-17.05-002; GAP-17.05-011; GAP-17.05-013 | Role/Permission tranche |
| GAP-17.05-006 | 10.1 | workflow; UI/noncoder | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase2c-product-brief-slice.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `absorbed` | low | none for bounded Phase 2.C slice | none | none |
| GAP-17.05-007 | 9.1 | benchmark | `scripts/run_cvf_release_gate_bundle.py`; `docs/reviews/CVF_17_05_CONSOLIDATED_LIVE_PROOF_PLAN_2026-05-18.md` | `absorbed` | low | violation would block public/release governance claims | none | none |
| GAP-17.05-008 | 8.3, 9.2 | benchmark; receipt | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/operational-metrics.schema.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts` | `absorbed` | low | none for bounded Phase 3.E pilot | none | none |
| GAP-17.05-009 | 6.1, 6.2, 6.3 | provider | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts` | `needs_gc018` | medium | Phase 4.T1/T2 provider method implementation | consuming slice not selected as of 2026-05-18 | demand-gated; no placeholder implementation |
| GAP-17.05-010 | 8.3, 9.2 | benchmark; runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/operational-metrics.schema.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts`; `EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME/observability/token.metrics.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | medium | full observability plane / operator cockpit claim | GAP-17.05-013 | none for metadata-only extension; live emission requires fresh GC-018 |
| GAP-17.05-011 | 5.1, 5.2, 5.3 | memory | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-tier.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts`; `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` | `partially_absorbed` | high | full governed memory / runtime reinjection / Agent OS claim | GAP-17.05-013 | live runtime memory consumption requires fresh GC-018 |
| GAP-17.05-012 | 2.1, 7.2, 10.3 | permission; workflow | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/tool-policy-guard.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | uniform tool/MCP/command/database governance claim | GAP-17.05-002 | none for action vocabulary; runtime enforcement requires fresh GC-018 |
| GAP-17.05-013 | 3.2, 4.3, 5.3 | orchestrator; runtime; memory | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sandbox-worker.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | async worker/subagent runtime claim | GAP-17.05-001; GAP-17.05-002; GAP-17.05-011 | none for contract-local transition metadata; scheduler lifecycle requires fresh GC-018 |
| GAP-17.05-014 | 5.1, 7.3 | memory; workflow | `none` | `not_absorbed` | medium | graph-native code intelligence claim | none | none |
| GAP-17.05-015 | 4.1, 4.2, 9.3, 11.1 | runtime; benchmark; agent OS | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/state_enforcement/state.machine.validator.ts`; `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/guard.runtime.engine.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `partially_absorbed` | high | complete governance runtime / Agent OS claim | GAP-17.05-002; GAP-17.05-011 | none for deterministic contract-local failure vocabulary; live enforcement requires fresh GC-018 |
| GAP-17.05-016 | 11.1, 11.2, 11.3 | agent OS; UI/noncoder | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`; public-sync `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | `partially_absorbed` | medium | customer-facing catalog promotion | GAP-17.05-003 | none |

## Initial Entries

Canonical disposition rule: the Structured Gap Crosswalk is the single source
of truth for each GAP disposition. The narrative entries below are
supplementary evidence and context; if a body entry disagrees with the
crosswalk, edit the body to match the crosswalk rather than changing the
crosswalk silently.

Last reconciled with crosswalk: 2026-05-18 (Step 2 Codex pass, 16/16 body
dispositions checked).

### GAP-17.05-001 - ORCHESTRATOR Role Boundary Is Doc-Only

Source:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md`

Observed gap:

- CVF contains an `orchestrator` role string / concept, but the fuller
  CEO/dispatcher boundary is not implemented as a runtime contract.
- Missing concepts include mandatory worker-lane delegation, overreach guard,
  and an orchestrator task router.

Current disposition:

- `partially_absorbed`.
- Phase D ORCHESTRATOR GC-018 filed and contract-local tranche completed in
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`.
  Runtime ORCHESTRATOR enforcement remains deferred to the Runtime workflow
  tranche.

Phase impact:

- Does not block completion of the already delivered 17.05 phases.
- Must be considered before any Phase 2.B runtime wire-up that relies on
  agent orchestration semantics.

### GAP-17.05-002 - Agent Role Catalog Permission Model Not Absorbed

Source:

- `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`

Observed gap:

- `allowed_outputs` per role is not represented in Phase 1.I contracts.
- `default_permissions` such as `write_code`, `database_limited`, and
  `deployment_guarded` are not represented in current auth/RBAC axis.
- The legacy catalog's domain role IDs are more granular than the current
  generic `AgentFunctionRole` values.
- Role Deny Rule is not represented as a role-specific output restriction.

Current disposition:

- `needs_gc018`
- Blocker for broad Phase 2.B runtime wire-up. The delivered bounded fixture
  path does not resolve the role/permission model.
- Claude Kit must be decomposed into role catalog, permission profile,
  orchestration rules, audit receipt, handoff contract, risk policy, registry
  spec, and adapter boundary before runtime authorization.

Phase impact:

- Does not block completed Phase 1.I taxonomy work because Phase 1.I was
  scoped to axis separation and adapter planning.
- Blocks any claim that agent role governance is fully absorbed.
- Blocks broad non-bounded Phase 2.B runtime wire-up until a Role/Permission
  GC-018 resolves the permission model or explicitly rejects it.

### GAP-17.05-003 - Surface Scan Is Not Legacy GAP Discovery

Source:

- Phase 1.0 drift inventory method:
  `scripts/run_cvf_17_05_drift_inventory.py`
- Current handoff open questions:
  `AGENT_HANDOFF_V9_2026-05-18.md`

Observed gap:

- Surface scans find duplicated or drifted implemented surfaces.
- They do not find legacy source concepts that were never implemented, were
  partially absorbed, or were flattened into broader contracts.

Current disposition:

- `needs_gc018` (Claude N-2 rewrite: replaces ad-hoc `method_gap`; the gap is a
  methodology requirement that future GC-018 packets must adopt).
- Future GC-018 packets for absorption/runtime wire-up must include both
  surface scan and legacy absorption audit requirements.

Phase impact:

- Phase 2.B GC-018 must include migration order, owner assignment, done
  criteria, and legacy absorption audit coverage before runtime wire-up starts.

### GAP-17.05-004 - Phase 2.B Runtime Wire-Up Lacks Owner-Confirmed Migration Plan

Source:

- `docs/reviews/CVF_17_05_PHASE_2B_PREFLIGHT_OWNER_MIGRATION_PLAN_2026-05-18.md`
- `AGENT_HANDOFF_V9_2026-05-18.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`

Observed gap:

- Phase 1.P / 1.I / 1.R / 1.M / 2.A contracts exist, but Phase 2.B does not
  yet have a selected bounded runtime path, owner-confirmed adapter migration
  order, or accepted done criteria.
- Direct runtime wire-up would risk absorbing ORCHESTRATOR, agent permission,
  receipt producer, and memory runtime semantics without a fresh GC-018.

Current disposition:

- `partially_absorbed` (Claude N-2 rewrite: replaces ad-hoc
  `bounded_resolved_for_phase_2b_fixture`; bounded fixture path is absorbed,
  broad runtime expansion is not).
- Phase 2.B preflight produced a bounded fixture-driven GC-018 and completion
  packet. Broad runtime wire-up remains deferred outside that fixture.
- Phase D Runtime workflow added a contract-local failure/action/transition
  vocabulary in `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`.
  Runtime consumption and live recovery enforcement remain deferred.

Phase impact:

- No longer blocks bounded Phase 2.B fixture implementation.
- Still blocks broad Phase 2.B-style runtime expansion without a new GC-018.
- Does not block the already delivered 17.05 bounded roadmap phases.

### GAP-17.05-005 - Broad Legacy Runtime Concepts Deferred After Phase 2.B Audit

Source:

- `docs/reviews/CVF_17_05_PHASE_2B_LEGACY_ABSORPTION_AUDIT_2026-05-18.md`
- `.private_reference/legacy/CVF Edit/Review CVF_1.md`
- `.private_reference/legacy/CVF Edit/De_xuat.md`
- `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md`

Observed gap:

- Legacy sources raise valid but broad runtime concepts: workflow failure
  states, scheduler, context/memory strategy, skill runtime binding,
  observability/telemetry, role `allowed_outputs`, granular permissions,
  role deny rules, and ORCHESTRATOR overreach/delegation semantics.

Current disposition:

- `needs_gc018` (Claude N-2 rewrite: replaces ad-hoc `out_of_scope_deferred`;
  concepts are queued for future tranches but must not be implemented without
  GC-018).
- These concepts were explicitly excluded from the bounded Phase 2.B fixture
  path and require a later legacy absorption audit/roadmap plus fresh GC-018.

Phase impact:

- Does not block Phase 2.B bounded fixture completion.
- Blocks any claim that CVF has fully absorbed the legacy Agent OS / role
  permission / orchestration model.

### GAP-17.05-006 - Phase 2.C Requires Fresh Vertical-Slice Authorization

Source:

- `docs/reviews/CVF_17_05_PHASE_2C_VERTICAL_SLICE_PREFLIGHT_2026-05-18.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts`

Observed gap:

- Phase 2.C moves from local contract proof into product runtime: noncoder
  trigger, web `/api/execute`, deliverable pack, receipt visibility, output
  validation, and live governance proof.
- The exact minimal `Create Product Brief` path and receipt adapter plan are
  not yet authorized.

Current disposition:

- `absorbed` for the bounded Phase 2.C slice (Claude N-2 rewrite: replaces
  ad-hoc `phase_2c_bounded_slice_complete`; the bounded vertical-slice scope
  is absorbed with live proof; broader Phase 2.C-style runtime expansion
  remains out of scope).
- Fresh Phase 2.C GC-018 was filed and the bounded `app_builder_complete`
  vertical slice was implemented with live Alibaba proof. Broad runtime and
  legacy role/orchestration absorption remain deferred.

Phase impact:

- No longer blocks bounded Phase 2.C roadmap acceptance.
- Still blocks broad noncoder runtime, role-permission, or orchestration
  claims without a new GC-018.

### GAP-17.05-007 - Live/API-Key Proof Should Be Consolidated

Source:

- `docs/reviews/CVF_17_05_CONSOLIDATED_LIVE_PROOF_PLAN_2026-05-18.md`
- `AGENTS.md` Mandatory Live Governance Proof
- `docs/reviews/CVF_17_05_PHASE_2C_VERTICAL_SLICE_PREFLIGHT_2026-05-18.md`
- `docs/reviews/CVF_17_05_PHASE_3E_EMISSION_PILOT_PREFLIGHT_2026-05-18.md`

Observed gap:

- Phase 2.C and Phase 3.E both need real runtime/live governance evidence.
- Running separate live/API-key sessions for each phase would increase
  key-handling risk and scatter proof across multiple packets.

Current disposition:

- `absorbed` (Claude N-2/N-3 rewrite: replaces ad-hoc
  `phase_2c_3e_live_bundle_executed_phase_4_deferred`; aligns with the
  crosswalk `absorbed` + low severity. Phase 4 deferral is preserved in
  GAP-17.05-009, not duplicated here).
- Phase 2.C live vertical-slice proof and Phase 3.E metric emission pilot were
  executed together on the Alibaba lane. Phase 4 remains demand-gated under
  GAP-17.05-009.

Phase impact:

- No longer blocks bounded Phase 2.C / 3.E live evidence.
- Does not replace release-quality gate proof for public/release claims.

### GAP-17.05-008 - Phase 3.E Waits For Phase 2.C Runtime Source

Source:

- `docs/reviews/CVF_17_05_PHASE_3E_EMISSION_PILOT_PREFLIGHT_2026-05-18.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/operational-metrics.schema.ts`

Observed gap:

- Phase 3.S schema exists, but Phase 3.E emission pilot needs runtime source
  events. Bounded Phase 2.B fixture output is not enough for operational
  metric emission.

Current disposition:

- `absorbed` for the bounded Phase 3.E pilot (Claude N-2 rewrite: replaces
  ad-hoc `phase_3e_bounded_pilot_complete`; bounded pilot is absorbed,
  dashboard/persistence/full operational intelligence remain out of scope).
- First metrics emitted from the Phase 2.C response-local source:
  `policy-violation-rate`, `receipt-integrity`, and `task-completion-rate`.

Phase impact:

- No longer blocks bounded Phase 3.E pilot acceptance.
- Still blocks dashboard, persistence, and full operational intelligence
  claims without a new GC-018.

### GAP-17.05-009 - Phase 4 Provider Methods Are Demand-Gated

Source:

- `docs/reviews/CVF_17_05_PHASE_4_PROVIDER_METHOD_PREFLIGHT_2026-05-18.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`

Observed gap:

- Provider output parsing already supports JSON/NDJSON, but no selected
  vertical slice currently requires first-class `stream()`, `tool_call()`,
  `json_mode()`, `vision()`, `embedding()`, or `reasoning()` methods.

Current disposition:

- `needs_gc018` (Claude N-2 rewrite: replaces ad-hoc
  `phase_4_demand_gate_blocked`; demand gate is encoded as "needs a fresh
  GC-018 that names the consuming slice", matching the controlled
  vocabulary).
- Do not implement provider methods until a fresh GC-018 names the method and
  consuming vertical slice/runtime need.
- As of 2026-05-18, no consuming vertical slice has been selected. The Phase D
  closure therefore records this as demand-gated rather than opening a
  placeholder provider method implementation.

Phase impact:

- Blocks Phase 4.T1/T2 implementation.
- Conditional live-bundle inclusion only if a selected Phase 2.C/later slice
  needs a provider method.

### GAP-17.05-010 - Legacy Observability Plane Is Broader Than Current Metrics

Source:

- `.private_reference/legacy/CVF 16.5/abtop/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/cortex-hub/Thong_tin.md`
- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`

Observed gap:

- Legacy sources describe a broader read-only observability plane covering
  sessions, token/context tracking, process/port state, scheduler status,
  provider health, telemetry, and receipts.
- Current CVF has operational metrics, runtime observability, release gates,
  and web operations surfaces, but does not yet claim a unified observability
  plane across all runtime/tool/worker surfaces.

Current disposition:

- `partially_absorbed` (Step 2 reconciliation rewrite: replaces body
  `needs_gc018` mismatch; the crosswalk is canonical. Current metrics and
  runtime observability pieces exist, but the unified observability plane and
  operator cockpit remain incomplete and require future GC-018 before runtime
  expansion.)
- Phase D Runtime workflow added metadata-only operational benchmark extension
  entries with `liveEmissionWired: false`. This improves the contract boundary
  but does not wire live emission, a durable dashboard, or an operator cockpit.

Phase impact:

- Does not block bounded 17.05 roadmap closure.
- Blocks public claims of full operator observability or Agent OS cockpit.

### GAP-17.05-011 - Governed Persistent Memory And Reinjection Remain Fragmented

Source:

- `.private_reference/legacy/CVF 16.5/agentmemory/Thong_tin.md`
- `.private_reference/legacy/CVF 16.5/tolaria/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/cortex-hub/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md`

Observed gap:

- Legacy sources converge on controlled memory capture, retrieval, privacy
  filtering, provenance, context packaging, memory tiering, and governed
  reinjection.
- CVF has knowledge store, file-backed persistence, audit trail, continuity
  metadata, and memory governance docs, but no single enforceable memory
  authority covers external capability intake, worker notes, context packs,
  and runtime reinjection.

Current disposition:

- `partially_absorbed`.
- Phase D Memory continuity GC-018 was filed and the contract-local tranche
  completed in `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`.
  The contract now defines memory tier owner policies, privacy-filtered
  reinjection metadata, archive ownership, and worker persistent/archive write
  restrictions. Runtime workflow now carries memory-write-violation transition
  metadata, but runtime memory-store enforcement and live provider-path
  reinjection remain deferred.

Phase impact:

- Blocks claims of complete governed memory or cross-agent long-term memory.
- Runtime consumption remains required before any live memory reinjection or
  worker memory enforcement claim can be made.

### GAP-17.05-012 - Tool, MCP, Command, And Database Actions Need A Canonical Action Vocabulary

Source:

- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/CLI-Anything/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/gridex/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/openrouter-cli.git/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md`

Observed gap:

- Legacy sources provide overlapping action vocabularies for MCP business
  tools, agent-native CLI surfaces, provider CLI envelopes, and database
  actions.
- CVF has tool registry and tool policy guards, but no single canonical action
  model spanning command, MCP, provider, and database surfaces.

Current disposition:

- `partially_absorbed`.
- Phase D Runtime workflow added a canonical action-class vocabulary covering
  tool, MCP, command, database, artifact export, and provider-call surfaces in
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`.
  Runtime enforcement across those surfaces remains deferred and requires
  fresh GC-018 before any uniform governance claim.

Phase impact:

- Blocks broad claims that every tool/action surface is uniformly governed.
- Future work should start as a vocabulary/contract tranche before runtime
  expansion.

### GAP-17.05-013 - Async Worker, Subagent, Scheduler, And Delegation Lifecycle Is Not Canonical

Source:

- `.private_reference/legacy/CVF ADD/deepagents/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/Agent Harnesses/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/Hermes Agent/Thong_tin.md`
- `.private_reference/legacy/CVF 16.5/OpenAgentd/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/Human System Harness/Thong_tin.md`

Observed gap:

- Legacy sources describe work tickets, worker-scoped context, context
  quarantine, background lifecycle, no-recursive-delegation, scheduler jobs,
  and orchestrator delegation boundaries.
- CVF has sandbox worker and continuity concepts, but no canonical async
  work-ticket/delegation state machine with receipt and memory restrictions.

Current disposition:

- `partially_absorbed`.
- Phase D ORCHESTRATOR tranche provides the worker-lane ticket type,
  delegation receipt boundary, overreach vocabulary, and worker memory write
  restriction metadata. Runtime scheduler lifecycle and async state transitions
  remained open until the Runtime workflow contract tranche.
- Phase D Runtime workflow now adds transition metadata and deterministic
  failure decisions for worker-overreach and memory-write-violation cases.
  Scheduler execution, async worker lifecycle, and live dispatch consumption
  remain deferred.

Phase impact:

- Blocks claims of complete multi-agent or async-agent runtime.
- Strongly related to GAP-17.05-001 and GAP-17.05-002.

### GAP-17.05-014 - Graph And Code-Intelligence Context Is Valuable But Not Absorbed

Source:

- `.private_reference/legacy/CVF ADD/code-review-graph/Thong_tin.md`
- `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md`
- `.private_reference/legacy/CVF ADD/cortex-hub/Thong_tin.md`

Observed gap:

- Legacy sources identify graph-based code context as a structured knowledge
  source for dependency, impact, and relevant-file narrowing.
- Current CVF has knowledge and context paths, but no canonical graph index or
  graph context resolver.

Current disposition:

- `not_absorbed` (Claude N-2/N-3 rewrite: aligned with the crosswalk
  `not_absorbed` token. Replaces ad-hoc `deferred_legacy_absorption`. There is
  no current CVF owner surface for graph context, so `needs_gc018` was
  premature; first a Phase D ranking pass should decide whether this concept
  enters a tranche at all).

Phase impact:

- Blocks claims that CVF has graph-native code intelligence.
- Does not block current governed non-coder/product path.

### GAP-17.05-015 - CVF Edit Identifies Runtime Enforcement And State-Machine Hardening Gaps

Source:

- `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`
- `.private_reference/legacy/CVF Edit/Review CVF_1.md`
- `.private_reference/legacy/CVF Edit/De_xuat.md`
- `.private_reference/legacy/CVF Edit/Failure Simulation cho CVF.md`

Observed gap:

- CVF Edit repeatedly distinguishes strong governance/safety doctrine from
  incomplete enforceable runtime: formal state transitions, failure states,
  role permission enforcement, context stability, self-review determinism, and
  observability.
- These critiques align with 17.05 but go broader than the completed bounded
  Phase 2.B/2.C/3.E slices.

Current disposition:

- `partially_absorbed` (Step 2 reconciliation rewrite: replaces body
  `needs_gc018` mismatch; the crosswalk is canonical. Current state-machine
  and guard-runtime surfaces exist, but complete runtime enforcement,
  deterministic failure-state handling, and full Agent OS claims remain
  incomplete.)
- Phase D Runtime workflow added deterministic failure-state vocabulary and
  contract tests for denial paths. This narrows the gap to runtime consumption;
  it does not prove live enforcement or complete Agent OS behavior.

Phase impact:

- Blocks public claims of complete Agent OS/runtime enforcement.
- Should feed the next hardening roadmap and the public technical catalog
  boundary.

### GAP-17.05-016 - Public Technical Catalog Was Missing A Single Truthful Product Surface

Source:

- User direction on 2026-05-18
- `docs/reference/CVF_PUBLIC_STRUCTURE_OVERVIEW.md`
- `docs/reference/archive/CVF_PUBLIC_NONCODER_VALUE_STATEMENT_2026-04-17.md`
- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`

Observed gap:

- CVF has many public-ready docs and evidence packets, but no single concise
  technical product catalog that separates proven capabilities, bounded
  capabilities, and roadmap candidates after the 17.05/legacy audit.

Current disposition:

- `partially_absorbed`
- Source draft created at
  `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`.
- Public-sync target created at
  `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`.
- Claude rebuttal found provenance/public-sync wording divergence. Chosen
  model: public-sync is the customer-facing derivative; provenance is the
  internal annotated source copy. Promotion remains blocked until evidence-link
  polish and content-alignment review are complete.

Phase impact:

- Does not complete implementation gaps.
- Provides the public claim boundary needed before customer-facing promotion.

## Review Cadence

Review this ledger before opening the next legacy absorption implementation
tranche. Add entries during future scans, but do not use this ledger itself as
authorization to implement them.

## Claim Boundary

This ledger records discovered gaps and the operator-approved handling rule for
those gaps. It does not authorize implementation, does not complete legacy
absorption audit, does not change public claims, and does not lift
`system_reconvergence_stop`.

## Verification Run

Commands run after structured crosswalk update:

```bash
python governance/compat/check_docs_governance_compat.py
python governance/compat/check_memory_governance_compat.py
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_agent_handoff_guard_compat.py
```

Result: all four checks passed after the crosswalk was added and matrix row
references were included.
