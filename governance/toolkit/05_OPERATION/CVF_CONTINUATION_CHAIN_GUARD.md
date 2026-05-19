# CVF Continuation Chain Guard

Memory class: POINTER_RECORD

Status: ACTIVE — enforced by `governance/compat/check_continuation_chain.py`.

## Purpose

Ensure work-order closure remains connected to GC-018 authority, completion
review evidence, and active handoff sync.

## Scope / Target / Owner Boundary

Target: `docs/work_orders/`, `docs/reviews/`, and the active handoff path in
`CVF_SESSION/ACTIVE_SESSION_STATE.json`.

Owner: governance compatibility guard surface.

In scope: read-only validation of GC-018-required work-order references,
closed work-order completion reviews, and active handoff HEAD SHA presence.

Out of scope: semantic review scoring, provider execution, runtime proof, and
replacement of adjacent handoff/session/depth-audit guards.

## Rule

- Rule A: any work order declaring `GC-018 required: Yes` must contain a
  `docs/baselines/CVF_GC018_*.md` reference.
- Rule B: any work order whose status line starts with `Status: CLOSED` must
  have a matching `docs/reviews/CVF_*_COMPLETION_*.md` file. A match is a
  review body containing the work order filename or an extracted lane/candidate
  identifier.
- Rule C: the active handoff must contain the current `git rev-parse HEAD`
  short SHA. Rule C is informational by default and blocking under `--enforce`.

## Enforcement Surface

- Local script: `governance/compat/check_continuation_chain.py`
- Exemption registry:
  `governance/compat/CVF_CONTINUATION_CHAIN_EXEMPTION_REGISTRY.json`
- Local hook chain: `governance/compat/run_local_governance_hook_chain.py`
- Static CI gate: `scripts/run_cvf_static_ci_gate.py`

## Exemption Registry

Rule B exemptions are capped at 10 entries. Exceeding 10 entries requires a
dedicated cleanup tranche before the guard may be widened further.

## Adjacent Guards

- `check_agent_handoff_guard_compat.py` validates handoff template chain.
- `check_depth_audit_continuation_compat.py` validates GC-018 reopen logic.
- `check_active_session_state.py` validates front-door pointer alignment.

This guard does not duplicate those surfaces; it validates the upstream
work-order to review binding.

## Related Artifacts

- `docs/baselines/CVF_GC018_C4_CONTINUATION_CHAIN_GUARD_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_C4_CONTINUATION_CHAIN_GUARD_2026-05-19.md`
- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`

## Final Clause

This guard is a process continuity check. It does not certify that any closed
work order delivered correct runtime behavior.
