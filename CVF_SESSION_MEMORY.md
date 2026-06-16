# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-16

Current mode marker: `plcs_t1_absorption_workflow_chain_routing_closed_pass_bounded_next_authorization`
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

Current mode: `plcs_t1_absorption_workflow_chain_routing_closed_pass_bounded_next_authorization`.

Active handoff:

`AGENT_HANDOFF_V19_2026-06-15.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

PLCS-T1 Absorption To Workflow-Chain Routing Matrix is
`CLOSED_PASS_BOUNDED` at material closure commit `9f7cd413`. Codex accepted the
Claude `WORKER_MUST_NOT_COMMIT` worker material at commit `b05286fe`, synced
the handoff at `dbddf213`, then closed the bounded routing matrix.

Artifacts:

- Roadmap:
  `docs/roadmaps/CVF_PLANE_LAYER_WORKFLOW_CHAIN_SYSTEMIZATION_ROADMAP_2026-06-16.md`
- Matrix:
  `docs/reference/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_2026-06-16.md`
- Worker return:
  `docs/reviews/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_WORKER_RETURN_2026-06-16.md`
- Completion:
  `docs/reviews/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_COMPLETION_2026-06-16.md`

Next allowed move: fresh operator authorization to choose a bounded follow-up,
likely PLCS-T2 registry-companion decision, PLCS-T3 checker/template hardening,
or another CVF foundation hardening tranche that preserves Central Core + Local
View. No runtime/provider/live/public-sync/new legacy scan/registry mutation is
authorized.

Next-Move Freshness Checker Foundation is `CLOSED_PASS_BOUNDED` at material
commit `8433691f` with soft-wrap hardening commit `fc7171aa`. The checker rejects
current next-move surfaces that dispatch,
reopen, or execute work already recorded as `CLOSED_PASS` or
`CLOSED_PASS_BOUNDED` in active session state, and is wired into reviewer-fast,
pre-commit, pre-push, autorun common gates, and steward `session-sync`.

Prior closure pointer: RSF-T3 Roadmap State Reconciliation Non-CI2 Next-Move
Sample is `CLOSED_PASS_BOUNDED` at material closure commit `ab683089`. Codex
reviewed the Claude worker return against actual files, diffs, and gates, then
repaired bounded closure evidence before committing. The verified finding is
narrow: stale Model Gateway C-02 P2 next-move continuity existed at the earlier
audit and dispatch-selection time, while current front-door and active handoff
pointers now block C-02 P2 redispatch.

Follow-up foundation hardening commit `93d0eb7f` moved the RSF-T3 dispatch
prompt envelope to the read-first position, wired the dispatch prompt envelope
checker into mandatory autorun/local hook paths, and extended provider-memory
learning escape detection to work-order authoring.

Artifacts:

- Audit:
  `docs/reviews/CVF_CCLV_T2_CLAUDE_ACTUAL_WORK_AUDIT_AND_RSF_T3_SELECTION_2026-06-16.md`
- GC-018:
  `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_2026-06-16.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`
- Worker return:
  `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`
- Completion review:
  `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md`

Do not redispatch Model Gateway C-02 P2 from stale continuity text. Do not open
Model Gateway P3 without fresh operator authorization, fresh GC-018, and
source-verified work order.

Prior closure pointer: FPRC-T1 Finding Root Cause And Memory Escape Guard is
`CLOSED_PASS_BOUNDED` at material commit `51f56133`.
Codex accepted the Claude worker return after reviewer repairs to closure
status, machine-closure table shape, work-order closure state, runtime-freshness
evidence, and trace manifest coverage.

Prior closure pointer: CCLV-T1 closure central facts packet template is
`CLOSED_PASS_BOUNDED` at material commit `89debbd6`; CCLV-T1A work order
template pointer refactor is `CLOSED_PASS_BOUNDED` at material commit
`dcc114e6`.

Prior foundation pointer: Prompt Envelope Read-First Placement and Central Core
Local View foundation packet is `CLOSED_PASS_BOUNDED` at material commit
`ef6f67de`.

Prior closure pointer: Roadmap State Reconciliation RSF-T2 is
`CLOSED_PASS_BOUNDED` at material commit `4d0883fa`. The dispatch-quality
checker has a bounded stale-roadmap redispatch guard with a reviewer-repaired
completion-path boundary.

Prior closure pointer: Session-Sync Authoring Helper T2 is
`CLOSED_PASS_BOUNDED` at material commit `5cb9d472`.
`governance/compat/build_session_sync_pack.py --author-entry` now emits a
read-only state-entry skeleton, `nextAllowedMove` template, and the five
canonical session mode marker occurrences. Focused tests passed 16/16 and
reviewer-fast passed 17/17.

Prior closure pointer: Session-Sync Pack Builder And Authorization Manifest is
`CLOSED_PASS_BOUNDED` at material commit `a5e91d4b`. The same read-only tool
generates the protected-path authorization manifest and reports
`ACTIVE_SESSION_STATE.json` drift before a session-sync commit (`--suggest`,
`--enforce`, `--plan-only`; 12 original tests plus 4 authoring-helper tests).

Prior closure pointer: Agent Dispatch Prompt Envelope Standardization is
`CLOSED_PASS_BOUNDED`.

Material commit: `b2654e2e` (worker executionBaseHead `620dc039`;
dispatch commit `c0c72317`; dispatchBaseHead `4895bca3`).

Artifacts:

- Roadmap:
  `docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md`
- GC-018:
  `docs/baselines/CVF_GC018_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_2026-06-15.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_FOR_CLAUDE_2026-06-15.md`

Result: Claude returned uncommitted deliverables under `WORKER_MUST_NOT_COMMIT`.
Codex repaired reviewer findings and committed the bounded foundation batch:
dispatch prompt envelope standard, compact work-order template pointer, checker
and tests, dispatch-author fast-gate wiring, closed work order, and completion
review. The work is authoring-time governance only.

Commit Steward Session-Sync Preflight Hardening is `CLOSED_PASS_BOUNDED` at
material commit `d709071c`. `session-sync` steward preflight now runs closure
packaging preflight before generated-state and active-session checks, catching
missing protected-path authorization before `git commit`. `handoff-sync`
remains lightweight.

Previous closure: Model Gateway C-02 P4B-B Live Proof T2 is
`CLOSED_PASS_BOUNDED` at material commit `d15f973e` with DeepSeek
`deepseek-chat` receipt `gw_20260615155616612_f0mwl515`; Alibaba `qwen-turbo`
is parked as a credential follow-up after HTTP 401.
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

Next move from that older tranche was superseded by P5, P5-C, and P4B-B T2
closures. P4B-B T2 is now closed; only Alibaba second-provider parity remains
parked pending a valid DashScope credential.

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

Mode: `next_move_freshness_checker_closed_pass_bounded_fresh_auth`.

Next-Move Freshness Checker Foundation is `CLOSED_PASS_BOUNDED` at material
commit `8433691f` with soft-wrap hardening commit `fc7171aa`. Next allowed move:
fresh operator authorization only for the next bounded foundation roadmap or
another operator-selected task.

Do not redispatch Model Gateway C-02 P2 from stale continuity text. C-02 P2 is
already closed; Model Gateway P3 requires fresh operator authorization, fresh
GC-018, and a source-verified work order.

No provider/API call, credential/network use, provider/model addition, runtime
behavior mutation, governance checker implementation by the worker, session
state mutation by the worker, EPF wiring, Strategy Layer implementation, AI
Gateway absorption, public-sync, external app mutation, raw memory release,
co-work product development, production readiness, or public readiness is
authorized without fresh operator authorization.

LHW24 remains the latest closed numbered LHW wave.

Parked lanes:

1. Live Redis proof: `PARKED_PENDING_CREDENTIALS`
2. DEP2 next-auth: `HARD_BLOCKED`
3. External receipt-anchor provider: `PARKED_PENDING_OPERATOR_DECISION`
4. AI Gateway family absorption: `PARKED_PENDING_PRIVACY_OPERATOR_AUTHORIZATION`
5. Strategy Layer implementation: `DEFERRED_REQUIRES_SEPARATE_GC018`
6. Model Gateway C-02 P4B-B Alibaba second-provider parity:
   `PARKED_PENDING_VALID_DASHSCOPE_CREDENTIAL`
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
