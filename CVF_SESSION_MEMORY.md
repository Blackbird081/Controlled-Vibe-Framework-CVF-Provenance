# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-05-28

Current mode marker: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It intentionally points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V14_2026-05-27.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `agent_autorun_workflow_control_enforced`.

Active handoff:

`AGENT_HANDOFF_V14_2026-05-27.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Active Rule Additions

Work-order dispatch quality is machine-enforced by:

`governance/compat/check_work_order_dispatch_quality.py`

Governed file-size maintainability now requires proactive rotation/splitting
instead of last-minute text compression when active governed files approach
hard thresholds.

This applies to broad external knowledge absorption records, session front
doors, handoffs, reviews, work orders, and other blocked work classes that
would become hard to test or review if oversized.

Canonical size guard:

`governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`

Agent autorun workflow control is mandatory for governed work phases. Agents
must pass the phase wrapper before dispatch, implementation, closure, or push:

`governance/compat/run_agent_autorun_workflow_gate.py`

Canonical autorun standard:

`docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

Autorun gates are now range-aware. Governed closure must use a captured
`baseHead` and a non-empty committed range; `--base HEAD --head HEAD` is not
valid closure evidence for changed artifacts. Source Verification false
invariants require literal source proof or runtime-path proof.

Latest-closure continuity is now machine-enforced. When a connector wave is
closed, the active front door, state registry, and handoff must all reference
the latest closed LHW wave; stale lower-wave `nextAllowedMove` text blocks the
active-session gate.

Closure finality is now machine-enforced. Closed-equivalent governed artifacts
must not retain `| OPEN |` rows, unchecked `- [ ]` checklist items, stale
roadmap dispatch/hold residue, or Fast Lane active/pass status conflicts.

Agent-error learning philosophy is now canonical:

`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`

Repeated agent mistakes are governance training samples, not merely worker
blame. Promote repeated defects from finding to written rule, from rule to
machine check, and from late machine check to the earliest applicable autorun
phase gate.

LHW scope rejection is not source rejection. For doc-only LHW connector waves,
families such as `abtop` or `gridex` that require live route execution must be
labeled `rejected from this LHW wave (doc-only scope) - requires live route;
eligible for separate live-proof roadmap post-LHW`, not globally rejected.
Finish absorption of remaining `PARTIALLY_ABSORBED` LH1 connector value before
opening separate live-proof roadmaps.

## Next Allowed Move

LHW10 is present in HEAD as `CLOSED_PASS_BOUNDED`; any follow-on wave must be
reviewed through the autorun `pre-dispatch`, `pre-implementation`,
`pre-closure`, and applicable `pre-push` gates before it can be trusted as
closed.

LHW sequencing remains: continue connector absorption first. Do not move
`abtop`, `gridex`, or other route-execution families into a live-proof roadmap
until the Orchestrator confirms there is no remaining connector value in LH1
`PARTIALLY_ABSORBED` families.

Future connector waves require fresh GC-018, roadmap, source-verified work
orders, roadmap-to-work-order trace matrix, dispatch-quality gate, closure
quality gate, and governed file-size maintainability planning.

Parked checkpoints:

- VI5-T4/T5 hosted Netlify freshness and operator external-agent retest
- Delta production hardening for MCP/client memory direction

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.
