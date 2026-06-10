# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-10

Current mode marker: `dscp_t11_profile_aware_pipeline_harness_closed_pass_bounded`
Enforcement posture: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

Active handoff predecessor archived in this batch:

`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V16_2026-06-06.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V17_2026-06-07.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `dscp_t11_profile_aware_pipeline_harness_closed_pass_bounded`.

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

DSCP-T11 Profile-Aware Pipeline Harness is `CLOSED_PASS_BOUNDED` at material
commit `4c39ce77`. All DSCP tranches T1 through T11 are
`CLOSED_PASS_BOUNDED`.

DSCP-T11 closure package:

- GC-018:
  `docs/baselines/CVF_GC018_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_2026-06-10.md`;
- roadmap:
  `docs/roadmaps/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_ROADMAP_2026-06-10.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-10.md`;
- worker return:
  `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_WORKER_RETURN_2026-06-10.md`;
- completion:
  `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md`.

Recent Claude/co-authored updates after T9:

- implementation-first absorption pattern added:
  `docs/reference/CVF_IMPLEMENTATION_FIRST_ABSORPTION_PATTERN_2026-06-08.md`;
- PolicyLocal UI audit lessons promoted into `DESIGN.md` Section 14 and the
  canonical web UX skill pointer;
- large worktree debt cleanup closed archive hygiene and retroactive governance
  section gaps, with active-archive stale count reduced to zero;
- history was rewritten to remove a corrupt 527MB blob and the branch was
  synchronized with origin.

Delivered scope for T9:

- New test harness:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts`
  (216 lines; 3 describe blocks; 3/3 vitest PASS; 0 TypeScript errors);
- GC-051 registry entry `dscp-t9-local-pipeline-harness` added at `5c90506a`;
- Worker return:
  `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_WORKER_RETURN_2026-06-08.md`;
- Completion review:
  `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md`;
- Work order closed:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T9_LOCAL_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-08.md`;
- Roadmap closed:
  `docs/roadmaps/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_ROADMAP_2026-06-08.md`.

Boundary: DSCP-T11 closed a local deterministic CPF test harness only. No
external Policy_Local edits, provider call, corpus ingestion, OCR, vector
retrieval, T12 authorization, public-sync claim from this provenance repo,
production readiness, public readiness, or live governance proof.

## Next Allowed Move

Next allowed move: Codex audits post-T11 DSCP/PolicyLocal foundation options
and either authors the next bounded roadmap/work order for Claude or returns
to operator with the recommended lane. DSCP-T1 through T11 are all
`CLOSED_PASS_BOUNDED`. T12 remains forbidden until EC-02 resolves on or after
2026-07-01.

LHW24 remains the latest closed numbered LHW wave in the state registry.

LPCI2-T12 remains forbidden until a separate operator-authorized evidence path
resolves EC-02 review on or after 2026-07-01, known `currentStatus`, known
`jurisdiction`, and a later eligibility re-evaluation produces at least one
`t12Eligible=YES` candidate.

The prior product lanes remain parked:

- DEP2 next-auth stable migration: `HARD_BLOCKED`;
- external receipt-anchor provider/service selection:
  `PARKED_PENDING_OPERATOR_DECISION`;
- live Redis service proof: `PARKED_PENDING_CREDENTIALS`.

LHW24 remains the latest closed numbered LHW wave in the state registry.

## Active Rule Additions

Agents must use the active standards named in `AGENTS.md` and the machine
guards named in `CVF_SESSION/ACTIVE_SESSION_STATE.json`. This pointer record
does not duplicate those long rules.

Active blocked work classes: no broad external knowledge absorption, no legacy
folder scan, no corpus expansion, no T12 claim, no public-sync outside
authorized batches, and no production/hosted/readiness claim until the
relevant EC gate resolves. These blocked work classes are resolved only by
the operator selecting a specific unblocking tranche. Consult
`CVF_SESSION/ACTIVE_SESSION_STATE.json` for the machine-readable list.

Broad external knowledge absorption (legacy folders, external API families,
third-party tool families) requires a Knowledge Absorption Priority Guard
check and a GC-018 authorization before dispatch. Unauthorized absorption is
blocked at the pre-push gate.

## Enforcement

Startup acknowledgment, active-session state compatibility, autorun workflow
gates, and governed file-size checks enforce this front-door contract.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `AGENT_HANDOFF_V17_2026-06-07.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.
