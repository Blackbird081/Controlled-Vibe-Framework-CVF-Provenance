# CVF GC-018 PRFC-T3 PLCS Companion Routing Checker Interlock

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-18

Owner: Codex

rawMemoryReleased: false

GC-018 class: governance-checker-hardening

## Purpose

Authorize PRFC-T3, the third tranche of the Pre-Runtime Foundation Cleanup And
Pilot roadmap. PRFC-T3 implements a narrow pre-dispatch checker/interlock for
future FPC-T2 C01-C04 registry-edit work orders so they must carry the PLCS
companion routing block approved by PLCS-T3.

## Scope / Target / Owner Boundary

Target: work-order structure and gate wiring only. The implementation may add
one checker, focused tests, and hook/autorun wiring for future C01-C04
registry-edit work orders.

Owner boundary: this GC-018 authorizes dispatch and later Codex implementation.
It does not authorize system-loop interlock registry edits, provider-registry
work, runtime queue execution, scheduler work, UI implementation, provider/live
proof, public-sync, Model Gateway work, production release, or public release.

## Authorization / Decision

Operator instruction: continue the pre-runtime foundation cleanup sequence after
PRFC-T2 closure. Current session state names PRFC-T3 as the next allowed move
only through fresh GC-018 and a source-verified work order.

Decision: AUTHORIZE PRFC-T3 as a bounded checker/interlock hardening task under
`WORKER_MAY_COMMIT` for Codex combined worker/reviewer/committer/closer.
Runtime execution remains parked.

## Source Authority

- Parent roadmap:
  `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md`
- PLCS-T3 decision:
  `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`
- PLCS-T2 decision:
  `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md`
- PLCS-T1 routing matrix:
  `docs/reference/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_2026-06-16.md`
- Autorun workflow gate runner:
  `governance/compat/run_agent_autorun_workflow_gate.py`
- Local hook chain:
  `governance/compat/run_local_governance_hook_chain.py`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| PRFC-T3 is the next PRFC tranche | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` | `## Tranche Plan`; `## PRFC-T3 Acceptance Criteria` | `PRFC-T3`; T3-AC1..T3-AC5 | PRFC roadmap | ACCEPT |
| PRFC-T3 target is PLCS companion-routing checker/interlock | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` | `## Work Plan` | `PRFC-T3 adds the narrow PLCS checker/interlock placement` | PRFC roadmap | ACCEPT |
| PLCS-T3 approved a future checker | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | `## Checker Disposition Decision` | `checker_disposition`; `enforcement_placement` | PLCS-T3 decision | ACCEPT |
| Required companion block has seven fields | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | `## Reusable Companion-Block Template` | `plcs_routing_row`; `plcs_routing_disposition`; `cclv_disposition`; `parallel_lane_risk`; `plcs_cross_reference`; `registry_edit_boundary`; `c05_boundary` | PLCS-T3 decision | ACCEPT |
| C01-C04 are in checker scope | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | `## Scope / Applies-To`; `## Per-Candidate Template Defaults` | C01; C02; C03; C04 | PLCS-T3 decision | ACCEPT |
| C05 remains out of checker scope | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | `## C05 Boundary` | `DEFERRED_PENDING_FPC_T3_C01` | PLCS-T3 decision | ACCEPT |
| PLCS-T2 made companion blocks required for C01-C04 | `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md` | `## Per-Candidate Decision Table`; `## Registry-Edit Work Order Dispatch Constraint` | C01-C04 companion ruling `REQUIRED` | PLCS-T2 decision | ACCEPT |
| Pre-dispatch autorun gate runner exists | `governance/compat/run_agent_autorun_workflow_gate.py` | phase command list | `pre-dispatch` gate command wiring surface | autorun gate runner | ACCEPT |
| Local hook-chain runner exists | `governance/compat/run_local_governance_hook_chain.py` | command list | checker command wiring surface | local hook-chain runner | ACCEPT |

## Current Runtime Freshness Verification

Runtime, provider-registry, hardcoded model, queue, scheduler, UI, API,
provider/live behavior, and provider configuration are explicitly out of scope
and untouched. This GC-018 does not make provider-registry absence,
hardcoded-model, or runtime readiness claims.

Current provider-registry/accounting surfaces checked for boundary only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`: exists and remains
  untouched by PRFC-T3.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`:
  declares `PROVIDER_CAPABILITY_REGISTRY` and remains untouched by PRFC-T3.

## Continuation Class And Depth Audit

GC-018 Continuation Candidate

- Candidate ID: PRFC-T3
- Date: 2026-06-18
- Parent roadmap / wave:
  `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md`
- Proposed scope: PLCS companion-routing checker/interlock for future C01-C04
  registry-edit work orders
- Continuation class: STRUCTURAL
- Quality-first decision: CONTINUE
- Remediation target if not expanding: keep PLCS-T3 guidance as documentation
  only
- Why now: the next registry-edit work orders would otherwise rely on every
  agent remembering the PLCS-T2/T3 companion-block requirement
- Active-path impact: LIMITED
- Risk if deferred: future C01-C04 work orders can dispatch without shared
  workflow-chain routing evidence
- Lateral alternative considered: YES
- Why not lateral shift: runtime execution remains parked until pre-runtime
  foundation surfaces stop relying on memory-only guidance
- Real decision boundary improved: YES
- Expected enforcement class: PRE_DISPATCH_GOVERNANCE_GATE
- Required evidence if approved:
- focused checker implementation
- focused tests for missing block, incomplete fields, wrong candidate scope,
  C05 boundary, and unrelated work-order exemption
- hook/autorun placement evidence
- no registry edit or runtime claim

Depth Audit

- Risk reduction: 2
- Decision value: 1
- Machine enforceability: 2
- Operational efficiency: 1
- Portfolio priority: 1
- Total: 7
- Decision: CONTINUE
- Reason: bounded machine-check promotion of an already-ratified PLCS rule with
  no provider/live/runtime blast radius.

## Authorized Deliverables

Implementation deliverables:

- `governance/compat/check_plcs_companion_routing_block.py`
- `governance/compat/test_plcs_companion_routing_block.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reviews/CVF_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_COMPLETION_2026-06-18.md`
- bounded updates to this work order, this GC-018, and the PRFC roadmap for
  closure evidence

## Protected Boundary

No protected session or active handoff edit is authorized for the implementation
phase. If PRFC-T3 closure changes next allowed move, Codex must perform any
session-sync in a separate session-sync range after the material closure commit.

## Tranche Closure Checklist

- [x] Checker enforces the seven-field PLCS companion block only for future
  C01-C04 registry-edit work orders
- [x] Checker exempts unrelated work orders
- [x] Checker preserves C05 deferral and does not decide C05
- [x] Focused tests cover missing block, incomplete field set, candidate scope,
  C05 boundary, and unrelated exemption
- [x] Autorun/hook placement matches PLCS-T3 recommendation or records a
  bounded alternative with reason
- [x] No system-loop interlock registry entry, provider-registry source, runtime
  source, provider/live proof, public-sync, production readiness, or public
  readiness is added

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_IMPLEMENTED` |
| Next control action | Future FPC-T2 C01-C04 registry-edit work orders must pass the PLCS companion routing block checker before dispatch |
| Worker blame | `N/A_WITH_REASON`: PLCS-T3 already classified this as a structural dispatch-layer drift risk |

## Decision

PRFC-T3 is closed bounded as a PLCS companion-routing checker/interlock under
`WORKER_MAY_COMMIT` for Codex. Runtime execution remains parked.

## Verification

Required pre-dispatch evidence:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 15816000 --head HEAD`
- `python governance/compat/check_work_order_dispatch_quality.py --base 15816000 --head HEAD --enforce`
- `git diff --check`

Required implementation evidence:

- focused pytest for `governance/compat/test_plcs_companion_routing_block.py`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <implementationBaseHead> --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base <implementationBaseHead> --head HEAD --enforce`
- `git diff --check`

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker hardening. No public-sync batch is
authorized.

## Claim Boundary

This GC-018 authorizes only a bounded governance checker/interlock for future
C01-C04 work-order structure. It does not edit any system-loop interlock
registry entry, provider registry, runtime queue, provider adapter, Model
Gateway path, public repository, production release, or public release claim.
