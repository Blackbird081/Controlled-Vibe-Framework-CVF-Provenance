# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-15

Current mode marker: `model_gateway_c02_p5c_closed_p4b_b_hold`
Enforcement posture: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

Active handoff predecessor archived in this batch:

`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`

Compaction archive (prior closed-tranche prose from this file):

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V19_2026-06-15.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `model_gateway_c02_p5c_closed_p4b_b_hold`.

Active handoff:

`AGENT_HANDOFF_V19_2026-06-15.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

Model Gateway C-02 P5-C Bridge Admission Boundary is `CLOSED_PASS_BOUNDED`.

Material commit: `b7a88782` (executionBaseHead `5fd4dbd2`).

Artifacts:

- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_FOR_CODEX_2026-06-15.md`
- Completion review:
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_COMPLETION_2026-06-15.md`

Result: Deterministic provider-agnostic bridge admission guard implemented and
wired additively into `ProviderExecutionBridge`. 28 files / 207 tests PASS.
Reviewer-fast 16/16 PASS. P4B-B concrete provider wiring and live proof remain
on explicit hold. Next move requires fresh operator authorization.
Long historical continuity remains in the compaction archive.

Prior closed tranche (pointer):

Model Gateway C-02 P5 Provider Adapter Admission And Capability Negotiation is
`CLOSED_PASS_BOUNDED` at material commit `a4907f2c`.
Completion: `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`

Prior-prior closed tranche (pointer):

Model Gateway C-02 P3 Unified Gateway Interface and P4A Unified Gateway
Runtime Skeleton are `CLOSED_PASS_BOUNDED` at material implementation commit
`5d46bc62`.

Completion reviews:

- `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md`

Session Continuity Rotation Guard Hardening is `CLOSED_PASS_BOUNDED`.

Model Gateway C-02 P4B-A is `CLOSED_PASS_BOUNDED` at material commit
`3c5b1d3d` after Codex reviewer repair. The bridge is deterministic and
provider-neutral; Model Gateway tests pass 25 files / 154 tests.

Model Gateway C-02 P4C Provider Adapter Contract Conformance is
`CLOSED_PASS_BOUNDED` at material commit `8d8f0871` and closure commit
`64a80684` after Codex reviewer repair. P4C is provider-agnostic: Alibaba and
DeepSeek are sample/current live-run providers only, not canonical product
scope.

Model Gateway C-02 P5 Provider Adapter Admission And Capability Negotiation
is `DISPATCHED_TO_CODEX` at commit `f26afe68`.

Next move: Codex implements P5-A/P5-B provider-agnostic adapter admission and
capability negotiation, authors completion review, commits material artifacts,
runs material-range pre-closure, and syncs session separately if closure changes
next move. P4B-B concrete provider wiring and live proof remain
`HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`.

Earlier closed tranches (pointer only):

Full closed-tranche history (Agent Commit Steward, Model Gateway P2, P1,
Legacy coverage-index dispatch guard, C-02 Resume Decision, FPC, DICE/DIR,
MEMCON T1-T5, MEOR, EXA T1-T2, LPCI2 EX-T1 through EX-T9, LPCI2 EC-T1
through EC-T5, DSCP T1-T11F, LHW1-LHW24, GC-051 registry hardening, active
session state authoring hardening, single-agent multi-role hardening, negative
search discipline, intake role routing hardening, governed work design-control
hardening, public README sync) is preserved in:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`

and `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`.

## Next Allowed Move

Mode: `model_gateway_c02_p5c_closed_p4b_b_hold`.

Next move: P4B-B concrete live proof requires fresh explicit operator
authorization, fresh GC-018 with live credential boundary, source-verified work
order, and live-run diagnostic discipline.

No provider/API call, credential/network use, provider/model addition, EPF
wiring, Strategy Layer implementation, AI Gateway absorption, public-sync,
external app mutation, raw memory release, co-work product development,
production readiness, or public readiness is authorized without fresh operator
authorization.

LHW24 remains the latest closed numbered LHW wave.

Parked lanes:

1. Live Redis proof: `PARKED_PENDING_CREDENTIALS`
2. DEP2 next-auth: `HARD_BLOCKED`
3. External receipt-anchor provider: `PARKED_PENDING_OPERATOR_DECISION`
4. AI Gateway family absorption: `PARKED_PENDING_PRIVACY_OPERATOR_AUTHORIZATION`
5. Strategy Layer implementation: `DEFERRED_REQUIRES_SEPARATE_GC018`
6. Model Gateway C-02 P4B-B live proof:
   `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`
7. DT-CVF-T0, Policy_Local PL-S1, EC activation/retrieval, T12: `PARKED`

## Active Rule Additions

Agents must use the active standards named in `AGENTS.md` and the machine
guards named in `CVF_SESSION/ACTIVE_SESSION_STATE.json`. This pointer record
does not duplicate those long rules.

Active blocked work classes: no broad external knowledge absorption, no legacy
folder scan, no corpus expansion, no T12 claim, no public-sync outside
authorized batches, and no production/hosted/readiness claim until the
relevant EC gate resolves.

## Enforcement

Startup acknowledgment, active-session state compatibility, autorun workflow
gates, and governed file-size checks enforce this front-door contract.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.

Prior closed-tranche history archived at: `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`
