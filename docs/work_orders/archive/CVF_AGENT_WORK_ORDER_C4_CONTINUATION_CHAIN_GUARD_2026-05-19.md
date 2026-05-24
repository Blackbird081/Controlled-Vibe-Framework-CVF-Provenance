# CVF Agent Work Order — C4: Continuation Chain Guard

Memory class: SUMMARY_RECORD

Status: CLOSED — C4 continuation chain guard implemented and verified.

GC-018 required: Yes — new enforcement surface, R0.
GC-018 path: `docs/baselines/CVF_GC018_C4_CONTINUATION_CHAIN_GUARD_2026-05-19.md`

## Purpose

Create `check_continuation_chain.py` to enforce three rules: every work order
that declares `GC-018 required: Yes` references a GC-018 baseline (Rule A),
every closed work order has a matching completion review (Rule B), and the
active handoff contains the current HEAD SHA (Rule C). Closes the governance
gap where closed work orders could lack evidence and handoffs could silently
drift from HEAD.

## Authority Chain

V2 roadmap (`CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`) — C4
section. GC-018 must be filed before implementation. C4 may run in parallel
with C2. Second Reviewer rebuttal must be no-blocking.

## Agent Roles

- **Orchestrator** — files GC-018; dispatches work order; accepts completion packet.
- **Worker** — runs pre-flight inventory before any code; populates exemption
  registry from discovered orphans; implements all tasks; files completion review.

## Scope

**Allowed scope:** Governance/provenance repo — exemption registry JSON, guard
script (Rules A/B/C), policy file, test file, hook-chain wiring.

**Forbidden scope:** Semantic validation of work order or review content, provider
execution checking, replacing adjacent three guards cited in work order body.

## Required First Reads

1. `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C4
2. All files in `docs/work_orders/` — record Status lines and basenames
3. All files in `docs/reviews/` — record naming patterns
4. `CVF_SESSION/ACTIVE_SESSION_STATE.json` — active handoff path
5. `docs/baselines/CVF_GC018_C4_CONTINUATION_CHAIN_GUARD_2026-05-19.md` (after filing)

## Write Ownership

Worker role owns all file creation. Pre-flight inventory is mandatory before
writing the exemption registry. Exemption registry must be written before
the guard script (guard reads from it at runtime).

## Execution Plan

Pre-flight inventory → Task 1 (exemption registry, cap = 10) → Task 2 (guard
script with Rules A/B/C) → Task 3 (policy file) → Task 4 (test file, must
pass) → Task 5 (hook-chain wiring). Do not wire before tests pass and
integration scan shows 0 non-exempted Rule B orphans.

## Evidence Requirements

Evidence trace in completion review: current `docs/work_orders/` scan showing
0 applicable Rule A violations and 0 non-exempted Rule B orphans; all 8 test
cases pass; exemption registry validates with ≤ 10 entries.

## Review Gate

Orchestrator reviews completion packet. No closure without integration scan
evidence and hook-chain `--hook pre-commit` pass confirmed in evidence trace.

## Closure Checklist

- [ ] Exemption registry valid JSON, ≤ 10 entries
- [ ] Integration scan: 0 applicable Rule A violations, 0 non-exempted Rule B orphans
- [ ] All 8 test cases pass with evidence
- [ ] Policy file present with exemption cap stated
- [ ] Hook-chain and CI gate wired without breaking existing checks
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- Pre-flight finds > 10 existing orphan work orders (cap exceeded before guard even ships)
- `check_continuation_chain.py` already exists (do not overwrite without authorization)
- Rule C emits drift on current repo state and root cause is unclear

## Target repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C4 section
- `docs/work_orders/` — all existing work orders (naming/status conventions)
- `docs/reviews/` — all existing completion reviews (naming conventions)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — active handoff pointer
- Reviewer rebuttal (first pass): status `CLOSED*`, review pattern `*_COMPLETION_*.md`,
  drop "next 5 commits", use HEAD SHA check

## Adjacent guards (must cite in policy file and GC-018)

- `check_agent_handoff_guard_compat.py` — handoff template chain; does NOT check work-order → review binding
- `check_depth_audit_continuation_compat.py` — GC-018 reopen; does NOT check work-order → review binding
- `check_active_session_state.py` — front-door pointer; does NOT check work-order → review binding

## Source-fidelity pre-flight (Worker role must run before writing any code)

```text
1. List all docs/work_orders/CVF_AGENT_WORK_ORDER_*.md — record status lines
   to confirm Status: CLOSED pattern (not DELIVERED/COMPLETE), and record
   any `GC-018 required:` declaration for Rule A applicability
2. List all docs/reviews/ — record naming patterns to confirm *_COMPLETION_*.md
3. Confirm check_continuation_chain.py does NOT exist yet
4. Confirm CVF_CONTINUATION_CHAIN_EXEMPTION_REGISTRY.json does NOT exist yet
5. Read CVF_SESSION/ACTIVE_SESSION_STATE.json → record activeHandoff path
6. Run: git rev-parse HEAD — record current HEAD SHA
7. Read active handoff file — confirm it contains or does not contain HEAD SHA
   (this tells you if Rule C would pass or report drift on current state)
```

## Implementation tasks

### Task 1 — Exemption registry

Create `governance/compat/CVF_CONTINUATION_CHAIN_EXEMPTION_REGISTRY.json`
before writing the guard. Populate with any existing work orders that close
without a matching `*_COMPLETION_*.md` review (discovered during pre-flight).

Schema:

```json
[
  {
    "workOrderFile": "CVF_AGENT_WORK_ORDER_AGENT_ROLE_ASSIGNMENT_2026-05-19.md",
    "reason": "Closed as prerequisite doc; review embedded in lane BCH completion packet",
    "addedAt": "2026-05-19",
    "addedBy": "Worker"
  }
]
```

Cap: policy file must state exemption list is capped at 10 entries.
Beyond 10 entries triggers a dedicated cleanup tranche.

### Task 2 — Guard script

Create `governance/compat/check_continuation_chain.py`.

#### Rule A — GC-018 reference for GC-018-required work orders

For every file matching `docs/work_orders/CVF_AGENT_WORK_ORDER_*.md`:
if body declares `GC-018 required: Yes`, body must contain a path matching
`docs/baselines/CVF_GC018_[^\s]+\.md`.

If body declares `GC-018 required: No`, Rule A is not applicable and must
not emit a violation. If body has no `GC-018 required:` declaration, Rule A
is not applicable for legacy/prerequisite compatibility and should be
reported as `not_applicable`, not as a violation.

```python
GC018_PATTERN = re.compile(r"docs/baselines/CVF_GC018_[^\s]+\.md")
```

If `GC-018 required: Yes` is declared and no path is found: violation
`{"rule": "A", "file": ..., "issue": "missing GC-018 reference"}`.

#### Rule B — Closed work order has completion review

Status detection (prefix match):

```python
CLOSED_PATTERN = re.compile(r"Status:\s*CLOSED", re.MULTILINE)
```

When status matches, look for any file under `docs/reviews/` matching
`CVF_*_COMPLETION_*.md` whose body contains either:
- the work order filename (basename without path), OR
- a lane identifier extracted from the work order filename
  (e.g. `LANE_G` from `CVF_AGENT_WORK_ORDER_LANE_G_*.md`)

Exemption: skip Rule B check if work order basename is in exemption registry.

If no matching review found: violation `{"rule": "B", "file": ..., "issue": "no completion review"}`.

#### Rule C — Handoff HEAD SHA current

```python
import subprocess
head_sha = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                    text=True).strip()[:8]
```

Read active handoff path from `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
Read handoff file text. If `head_sha` not in text:
emit violation `{"rule": "C", "issue": "GC-020 drift", "headSha": head_sha}`.

Rule C is informational by default. `--enforce` makes it exit non-zero.

#### Output modes

`--json` emits JSON report. Default prints human-readable.
`--enforce` exits 2 on any violation (including Rule C drift).

### Task 3 — Policy file

Create `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md`.

Required sections: Purpose, Rule (A, B, C), Enforcement Surface, Exemption
registry path and cap, Adjacent guards cited, Related Artifacts, Final Clause.

### Task 4 — Test file

Create `governance/compat/test_check_continuation_chain.py`.

Required test cases:

- `test_rule_a_missing_gc018` — work order body declaring `GC-018 required: Yes`
  without GC-018 reference → Rule A violation
- `test_rule_a_passes_with_gc018` — work order body with valid GC-018 path → no Rule A violation
- `test_rule_a_not_applicable_when_gc018_not_required` — work order body with
  `GC-018 required: No` and no GC-018 path → no Rule A violation
- `test_rule_b_missing_review` — closed work order with no matching review → Rule B violation
- `test_rule_b_passes_with_review` — closed work order + matching review → no Rule B violation
- `test_rule_b_exemption` — closed work order in exemption registry → no Rule B violation
- `test_rule_c_head_drift` — handoff text without current HEAD SHA → Rule C drift violation
- `test_rule_c_passes` — handoff text containing HEAD SHA → no Rule C violation

Use in-memory string fixtures. Do not depend on repo state for unit tests.
A separate integration test may optionally scan current `docs/work_orders/`
and assert 0 non-exempted Rule B orphans.

### Task 5 — Hook-chain wiring

Add `check_continuation_chain.py` to:

1. `governance/compat/run_local_governance_hook_chain.py` — as a step in the pre-commit hook
2. `scripts/run_cvf_static_ci_gate.py` — as a check in the static CI gate

Add only after Task 4 tests pass and Task 5 integration scan shows
0 non-exempted orphans. Wire-in must not break existing hook-chain or CI gate.

## Acceptance criteria

- [ ] Current `docs/work_orders/` scan → 0 applicable Rule A violations, 0 unexempted Rule B orphans
- [ ] `test_rule_a_missing_gc018` → Rule A violation detected
- [ ] `test_rule_b_missing_review` → Rule B violation detected
- [ ] `test_rule_b_exemption` → no false positive for exempted work orders
- [ ] `test_rule_c_head_drift` → GC-020 drift violation emitted
- [ ] Exemption registry validates (no JSON parse error, entries ≤ 10)
- [ ] Policy file present with all required sections and exemption cap stated
- [ ] Hook-chain wiring added; `run_local_governance_hook_chain.py --hook pre-commit` passes
- [ ] `scripts/run_cvf_static_ci_gate.py` includes guard; static CI gate passes

## Completion packet

File `docs/reviews/CVF_C4_CONTINUATION_CHAIN_GUARD_COMPLETION_2026-05-19.md`
with evidence trace (command → result → verdict per criterion).

Update V10 handoff HEAD SHA per GC-020 after commit.

## Claim boundary

This work order covers only the three-rule continuation chain check
(GC-018-required work order → GC-018 reference, closed work order →
completion review, handoff HEAD SHA current). It does not validate the
semantic content of work orders or reviews, does not check provider execution,
and does not replace the adjacent three guards cited above.
