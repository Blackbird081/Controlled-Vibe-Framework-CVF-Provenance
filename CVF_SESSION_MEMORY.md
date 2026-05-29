# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-05-29

Current mode marker: `wce_w1_w3_closed_pass_bounded_w2_unblocked`
Enforcement posture: `agent_autorun_workflow_control_enforced`
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
   `AGENT_HANDOFF_V15_2026-05-29.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `lhw14_wave_closed_pass_bounded`.

Active handoff:

`AGENT_HANDOFF_V15_2026-05-29.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Owner Surface

Owner surface: CVF active session startup, continuity routing, and front-door
rule pointers for new or resumed agents.

## Protocol

Agents must treat this file as a compact pointer record, then resolve the
machine-readable registry, active review queue, active handoff, and required
startup guards before material governed work.

## Active Rule Additions

Work-order dispatch quality is machine-enforced by:

`governance/compat/check_work_order_dispatch_quality.py`

Governed file-size maintainability now requires proactive rotation/splitting
instead of last-minute text compression when active governed files approach
hard thresholds.

This applies to broad external knowledge absorption records, session front
doors, handoffs, reviews, work orders, and other blocked work classes that
would become hard to test or review if oversized.

Redefine size guard:

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

Status-token and Source Verification symbol hygiene are now machine-enforced:
`HOLD_*`, `DRAFT`, or `PROPOSED` statuses must not contain `CLOSED`, and
`Verified path or symbol` cells must contain only symbols only, not value
assignments such as `rawMemoryReleased: false`.

Allowed-scope and whole-wave range closure hygiene are now machine-enforced:
single-work-order closure ranges must not include files outside Allowed scope,
closed LHW wave roadmaps must be checked with a full T1/T2/T3 changed range,
and connector spec line-count claims must match the current file.

Agent-error learning philosophy is now canonical:

`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`

Repeated agent mistakes are governance training samples, not merely worker
blame. Promote repeated defects from finding to written rule, from rule to
machine check, and from late machine check to the earliest applicable autorun
phase gate.

IDE-extension multi-provider execution logging is now machine-enforced:

`docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md`

`governance/compat/check_multi_provider_execution_log.py`

Mixed-provider sessions using VS Code extension tabs, Antigravity, direct
provider scripts, CLI, MCP, or browser agents must record provider/model,
execution surface, role, evidence basis, commit range, direct-provider-proof
boundary, quality findings, cost attribution, and an Execution Attribution
Block that separates roadmap/order author, worker/executor, and reviewer/closer
when closing governed work or claiming provider effectiveness. Autorun and
local hook chains now fail missing or overclaimed multi-provider execution logs.

Finding-to-governance learning disposition is now machine-enforced:

`docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD_2026-05-29.md`

`governance/compat/check_finding_to_governance_learning.py`

Changed logs, reviews, assessments, or audits that record findings or known
issues must classify each material finding into governance/control-plane,
runtime-behavior, provider-output, cost/economics, or documentation-only
learning lanes, with next control action.

Learning Signal Intake Bridge is now the typed Learning Plane intake route for
those learning lanes:

`docs/reference/CVF_LEARNING_SIGNAL_INTAKE_BRIDGE_STANDARD_2026-05-29.md`

`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`

Runtime/provider/cost candidates, phase-gate placement gaps, design-review
candidates, and machine-check candidates must normalize into
`LearningSignalIntakeRecord` / `LearningFeedbackInput` before a follow-up
roadmap claims Learning Plane routing. Autonomous mutation remains false unless
a separate governed roadmap authorizes it.

LHW scope rejection is not source rejection. For doc-only LHW connector waves,
families such as `abtop` or `gridex` that require live route execution must be
labeled `rejected from this LHW wave (doc-only scope) - requires live route;
eligible for separate live-proof roadmap post-LHW`, not globally rejected.
Finish absorption of remaining `PARTIALLY_ABSORBED` LH1 connector value before
opening separate live-proof roadmaps.

## Next Allowed Move

LHW14 is the latest closed LHW wave (T1+T2+T3 CLOSED_PASS_BOUNDED; agentmemory/OpenSpec/Human System Harness LH1 triggers closed). Any further connector wave requires a fresh roadmap and GC-018. Continue LHW connector absorption for remaining PARTIALLY_ABSORBED LH1 families before opening separate live-proof roadmaps for abtop, gridex, or other route-execution families.

Parked checkpoints:

- VI5-T4/T5 hosted Netlify freshness and operator external-agent retest
- Delta production hardening for MCP/client memory direction

## Enforcement

Startup acknowledgment, active-session state compatibility, autorun workflow
gates, and governed file-size checks enforce this front-door contract.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.
