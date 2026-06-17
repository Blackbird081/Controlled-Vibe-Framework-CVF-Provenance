# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-17

Current mode marker: `ahb_tn3_agent_workspace_state_topology_contract_closed_pass_bounded_ahb_tn4_operator_decision`
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

Current mode: `ahb_tn3_agent_workspace_state_topology_contract_closed_pass_bounded_ahb_tn4_operator_decision`.

Active handoff:

`AGENT_HANDOFF_V19_2026-06-15.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

AHB-Tn.3 Agent Workspace State Topology Contract is `CLOSED_PASS_BOUNDED` at
material commit `e1ebaa17`. It adds the stable topology contract that future
workspace build or generated-state work must cite before creating workspace
state, queues, inboxes, review lanes, dashboards, or generated state sources:

- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`

This is topology foundation only. It does not build the workspace, create
generated workspace state, mutate runtime/product code, run provider/live proof,
public-sync, edit registries, or claim production/public readiness.

AHB-Tn.2 Agent Workspace Design Checker is `CLOSED_PASS_BOUNDED` at material
commit `38e98f8c`. It converts the Agent Workspace Design Control Block into a
mandatory machine-checked local view for changed workspace work orders:

- `governance/compat/check_agent_workspace_design.py`
- `governance/compat/test_check_agent_workspace_design.py`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`

This is machine enforcement only. It does not build the workspace, mutate
runtime/product code, run provider/live proof, public-sync, edit registries, or
claim production/public readiness.

AHB-Tn.1 Agent Interaction Workspace Analysis Design remains
`CLOSED_PASS_BOUNDED` at material commit `4b8278be`. It created the stable
agent-workspace front door and design standard:

- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`

This is design foundation only. It does not build the workspace, mutate
runtime/product code, run provider/live proof, public-sync, edit registries, or
claim production/public readiness.

AHB-T2 Agent Handoff Contract Ratification is `CLOSED_PASS_BOUNDED` at material
commit `cabbca87` after dispatch commit `4b78355f`. Codex accepted Claude's
worker return with reviewer repairs, ratified the bounded Agent Handoff
Contract, and recorded AHB-T2-F1 as a standing foundation storage/layout
finding: governance refactor work must include stable folder/index/storage
layout review, with foundation files on stable indexed paths and
execution/evidence files kept dated and archive-bound.

AHB-T2-F1 Foundation Storage Layout Remediation is `CLOSED_PASS_BOUNDED` at
material commit `959e2d78`. It created the stable foundation storage front door
and standard:

- `docs/reference/foundation_storage/README.md`
- `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`

AHB-T2-F2 Foundation Storage And Memory Learning Enforcement is
`CLOSED_PASS_BOUNDED` at material commit `abfd9015`. It added the foundation
storage/layout machine gate, bound it into autorun/local hooks, and stabilized
the active Finding-To-Governance standard path:

- `governance/compat/check_foundation_storage_layout.py`
- `governance/compat/test_check_foundation_storage_layout.py`
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`

AHB-T3 Unified Handoff Boundary Checker is `CLOSED_PASS_BOUNDED` at material
commit `e0927de5`. It adds a stable agent-handoff front door, machine-check
standard, checker, focused tests, and autorun/local hook binding for the
ratified Agent Handoff Contract:

- `docs/reference/agent_handoff/README.md`
- `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`
- `governance/compat/check_agent_handoff_boundary.py`
- `governance/compat/test_check_agent_handoff_boundary.py`

AHB-T1A Finding Cleanup remains `CLOSED_PASS_BOUNDED` at material commit
`9b21a901`; AHB-T1 remains `CLOSED_PASS_BOUNDED` at material commit
`11f4c4a2`.

Artifacts:

- AHB-T2 contract:
  `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`
- AHB-T2 completion:
  `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md`
- AHB-T2 worker return:
  `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_WORKER_RETURN_2026-06-16.md`
- AHB-T2-F1 completion:
  `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md`
- AOT-T3 GC-018:
  `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`
- AOT-T3 work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md`
- AOT-T3 completion:
  `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md`
- AOT checker:
  `governance/compat/check_agent_operation_trace.py`
- AOT focused tests:
  `governance/compat/test_check_agent_operation_trace.py`
- AOT standard:
  `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- AHB roadmap:
  `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`

AHB-T1 Agent Handoff Boundary Audit remains `CLOSED_PASS_BOUNDED` at material
commit `11f4c4a2`.

Prior AHB-T1 artifacts:

- Audit:
  `docs/audits/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md`
- Worker return:
  `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_WORKER_RETURN_2026-06-16.md`
- Codex rebuttal:
  `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_CODEX_REBUTTAL_2026-06-16.md`
- Completion:
  `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_COMPLETION_2026-06-16.md`
- Roadmap:
  `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`
- GC-018:
  `docs/baselines/CVF_GC018_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T1_HANDOFF_BOUNDARY_AUDIT_FOR_CLAUDE_2026-06-16.md`

Superseded AHB-Tn.1 next-move note: the AHB-Tn.2 checker path is now closed.
Future workspace build or generated state work remains parked behind AHB-Tn.4
or another fresh operator-authorized tranche. Do not build the workspace,
create generated workspace state, edit registries, mutate runtime/product code,
run provider/live proof, or public-sync without later operator authorization.

PLCS-T3 Companion Routing Checker/Template Decision is `CLOSED_PASS_BOUNDED` at
material commit `6fc43136` after dispatch commit `992c2270` and session-sync
commit `8d375b24`. Codex authored the documentation-only decision packet,
completion review, and bounded roadmap/work-order closure updates.

Artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_FOR_CODEX_2026-06-16.md`
- Decision:
  `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`
- Completion:
  `docs/reviews/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_COMPLETION_2026-06-16.md`
- PLCS roadmap:
  `docs/roadmaps/CVF_PLANE_LAYER_WORKFLOW_CHAIN_SYSTEMIZATION_ROADMAP_2026-06-16.md`
- Finding propagation roadmap:
  `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`
- Standards:
  `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
  and
  `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`

Result: future C01-C04 registry-edit work orders must embed the locked
seven-field PLCS companion block; checker disposition is `CHECKER_APPROVED` as
a future separate-tranche machine-check candidate; recommended enforcement
placement is future pre-dispatch autorun; C05 remains
`DEFERRED_PENDING_FPC_T3_C01`.

AOT-T3 B12 machine-check hardening is closed at material commit `08659a5d`.
No registry edit, additional checker implementation outside later authorized
scope, runtime/source/test mutation, provider/live/public-sync/new legacy scan,
C05 companion ruling, production readiness, or public readiness is authorized.

PLCS-T2 Registry-Companion Decision is `CLOSED_PASS_BOUNDED` at material
closure commit `6ab05918` after dispatch commit `9b483168` and handoff-sync
commit `29ec11b0`.

Artifacts:

- Decision:
  `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md`
- Completion:
  `docs/reviews/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_COMPLETION_2026-06-16.md`
- Roadmap:
  `docs/roadmaps/CVF_PLANE_LAYER_WORKFLOW_CHAIN_SYSTEMIZATION_ROADMAP_2026-06-16.md`

Decision: future FPC-T2 C01-C04 registry-edit work orders must carry a PLCS
companion block with PLCS-T1 Section C row, routing disposition, CCLV
disposition, parallel-lane risk, PLCS cross-reference, and registry-edit
boundary. C05 remains `DEFERRED_PENDING_FPC_T3_C01`.

Next allowed move: fresh operator authorization to choose PLCS-T3
checker/template hardening, individual FPC-T2 C01-C04 registry-edit work
orders with fresh GC-018/work orders, or another bounded CVF foundation
hardening tranche that preserves Central Core + Local View. No registry edit,
runtime/provider/live/public-sync/new legacy scan, Model Gateway redispatch,
Model Gateway P3 authorization, co-work product development, production
readiness, or public readiness is authorized.

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

PLCS-T1 is superseded for next-move routing by the PLCS-T2 closure note above.

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

Mode: `ahb_tn3_agent_workspace_state_topology_contract_closed_pass_bounded_ahb_tn4_operator_decision`.

AHB-Tn.3 Agent Workspace State Topology Contract is `CLOSED_PASS_BOUNDED` at
material commit `e1ebaa17`. Next allowed move: operator decision whether to
authorize AHB-Tn.4 workspace build or generated workspace state source/checker
tranche, or another bounded CVF foundation/refactor tranche with fresh GC-018.
The workspace is not opened unilaterally.

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
