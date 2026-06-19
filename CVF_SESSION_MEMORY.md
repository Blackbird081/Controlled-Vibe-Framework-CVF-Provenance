# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-19

Current mode marker: `delta_t11_durable_audit_evidence_bundle_closed_next_foundation_ready`
Enforcement posture: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

Active handoff predecessor archived in this batch:

`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V19_2026-06-15.md`

Compaction archive (prior closed-tranche prose from this file):

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V20_2026-06-19.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `delta_t11_durable_audit_evidence_bundle_closed_next_foundation_ready`.

Previous mode: `delta_t11_durable_audit_evidence_bundle_dispatched_claude_execution_pending`.

Active handoff:

`AGENT_HANDOFF_V20_2026-06-19.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

Detailed pre-GGL-T1 continuity was compacted to:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_GGL_T1_COMPACTION_2026-06-19.md`

GGL-T1 Governance Gate Latency Audit And Optimization is
`CLOSED_PASS_BOUNDED` at closure commit `913c8c9b`, after dispatch commit
`7de440d2`, dispatch handoff bridge `309e9f57`, material commit `b71bde91`,
and material handoff bridge `969455b3`.

GGL-T1 added bounded parallel autorun scheduling, per-command and total timing,
exact fail-closed local PASS receipt reuse by commit steward, and stderr-safe
Git path parsing. Focused tests passed 19/19. The complete 44-command parallel
pre-implementation run passed in 3.35s; serial passed in 9.19s; exact receipt
reuse reduced the following steward run to 1.2s total on this host. Git hooks
remain complete and outside receipt reuse.

Delta-T7 Receipt-To-Execution Evidence Auditor is `CLOSED_PASS_BOUNDED` at
closure commit `d82870b9`, after dispatch `264cc598`, dispatch handoff bridge
`2fb39e44`, material `fcf28c0d`, material handoff bridge `b13632e0`, and
closure handoff bridge `c4b49fbd`. Focused tests passed 11/11, the full MCP
suite passed 31 files / 628 tests, and TypeScript build passed.

GGL-T2 Git Hook Lane And Worktree Finality Reliability is
`CLOSED_PASS_BOUNDED` at closure commit `a7b2f1d2`, after dispatch
`cc6e4666`, dispatch handoff bridge `01836f18`, material commit `02678968`,
and material handoff bridge `96a3611b`. Focused tests passed 17/17; direct
hook proof passed 54/54 with parallel preflight enabled; worker-return fast
gate passed; implementation steward passed with pre-implementation rerun 44/44;
material-range pre-closure passed 43/43 with clean finality; closure pre-commit
passed 54/54.

Delta-T9 Durable Execution Audit Store is `CLOSED_PASS_BOUNDED` at closure
commit `38292bee`, after dispatch `7f603b49`, dispatch handoff bridge
`8a9ee919`, material commit `ac390222`, and material handoff bridge
`8b1cb2d5`. It adds a bounded durable audit contract/local JSONL store for
supplied Delta receipt-to-execution evidence only. Focused tests passed 30/30,
full MCP tests passed 32 files / 658 tests, build passed, worker-return fast
gate passed, and pre-closure content gates passed with only expected
post-closure session-sync HEAD drift before this sync.

Delta-T10 Durable Audit Integrity Readout is `CLOSED_PASS_BOUNDED` at closure
commit `b496146f`, after dispatch `0b286d03`, dispatch repair `b14df7b4`,
material commit `8f4abb28`, and material handoff bridge `1a08cbd0`. It adds a
bounded deterministic integrity readout for supplied Delta-T9 durable audit
records only. Codex reviewer hardened JSONL primitive/null classification and
secret-like receipt identity handling. Focused tests passed 30/30, full MCP
tests passed 33 files / 688 tests, build passed, worker-return fast gate
passed, and pre-closure content gates passed with only expected post-closure
session-sync HEAD drift before this sync.

Delta-T11 Durable Audit Evidence Bundle External Reviewer Readout is
`CLOSED_PASS_BOUNDED` at closure commit `3d0b70c5`, after dispatch
`53aca070`, material commit `0a3e298e`, and material handoff bridge
`26a9491e`. It adds a bounded deterministic evidence bundle and external
reviewer readout over supplied Delta-T9/T10 durable audit artifacts only.
Codex reviewer hardened deterministic `bundledAt` defaulting, rejected forged
readout contract/bounded-flag inputs, repaired packet evidence/scaffold, and
preserved `NOT_CLAIMED` rows for forbidden expansion claims. Focused tests
passed 39/39, full MCP tests passed 34 files / 727 tests, build passed,
worker-return fast gate passed, reviewer-fast passed 31/31, and closure
pre-commit hook passed 54/54.

## Next Allowed Move

Mode: `delta_t11_durable_audit_evidence_bundle_closed_next_foundation_ready`.

Next allowed move: select the next high-value lane with fresh GC-018 and source
verification. Recommended lane: public/external-evaluation package and catalog
alignment from the public-sync clone only, so external agents and user
developers can inspect the latest bounded CVF evidence without treating the
2026-06-19 snapshot as the whole catalog. Do not open Delta-T12 by default
unless a fresh operator decision chooses another foundation tranche.

Parked: runtime profile expansion, arbitrary commands, EDIT/COMMIT execution,
provider/live calls, public-sync, queue/daemon, CVF Web action execution, direct
IDE/shell/git/filesystem interception, broad wrapper/proxy/runtime enforcement,
readiness claims, and universal governed-coding claims. LHW24 remains the latest
closed numbered LHW wave.

## Active Rule Additions

Agents must use the active standards named in `AGENTS.md` and the machine
guards named in `CVF_SESSION/ACTIVE_SESSION_STATE.json`. This pointer record
does not duplicate those long rules.

## Blocked Work Classes

Marker phrase for compatibility guards: blocked work classes.

broad external knowledge absorption remains blocked unless opened through a
fresh GC-018, source verification, and the governed external knowledge
absorption chain. Marker phrase for compatibility guards: broad external
knowledge absorption.

## Enforcement

Startup acknowledgment, active-session state compatibility, autorun workflow
gates, and governed file-size checks enforce this front-door contract.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `AGENT_HANDOFF_V20_2026-06-19.md`
- `docs/reviews/CVF_GGL_T1_GOVERNANCE_GATE_LATENCY_AUDIT_OPTIMIZATION_COMPLETION_2026-06-19.md`
- `docs/reviews/CVF_DELTA_T7_RECEIPT_TO_EXECUTION_EVIDENCE_AUDITOR_COMPLETION_2026-06-19.md`
- `docs/reviews/CVF_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_COMPLETION_2026-06-19.md`
- `docs/reviews/CVF_DELTA_T9_DURABLE_EXECUTION_AUDIT_CONTRACT_STORE_BOUNDARY_COMPLETION_2026-06-19.md`
- `docs/baselines/CVF_GC018_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_2026-06-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_FOR_CLAUDE_2026-06-19.md`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_agent_commit_steward_preflight.py`

## Claim Boundary

This front door is a pointer record only. GGL-T1 and GGL-T2 timing and hook
evidence are host-specific local governance-control evidence. They do not
prove runtime behavior, provider behavior, hosted freshness, public readiness,
production readiness, universal speedup, direct interception, universal
governed-coding control, or automatic loading by external agents.
