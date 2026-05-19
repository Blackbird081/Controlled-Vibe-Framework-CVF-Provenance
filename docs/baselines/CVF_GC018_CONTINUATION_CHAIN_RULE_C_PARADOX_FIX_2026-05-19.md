# CVF GC-018 Continuation Chain Rule C Paradox Fix — 2026-05-19

Memory class: SUMMARY_RECORD

Status: AUTHORIZED — Rule C self-referential paradox fix may proceed as a bounded
R0 guard logic correction.

## Purpose

Authorize a targeted fix to `governance/compat/check_continuation_chain.py`
Rule C so that the pre-push gate stops producing a self-referential paradox
that forces operators to bypass the hook with `--no-verify`.

## Source / Predecessor Evidence

- Guard script: `governance/compat/check_continuation_chain.py`
- Guard tests: `governance/compat/test_check_continuation_chain.py`
- Guard policy: `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md`
- Original C4 authorization: `docs/baselines/CVF_GC018_C4_CONTINUATION_CHAIN_GUARD_2026-05-19.md`
- Incident: Phase 3 W1/W2/W3 push to `origin/main` on 2026-05-19 entered an
  infinite loop. Each GC-020 sync commit modified the handoff to record the
  previous HEAD SHA; the pre-push Rule C check then required the new HEAD SHA
  (the sync commit's own SHA) to appear in the handoff, which is mathematically
  impossible. Operator forced through with `git push --no-verify`. The root
  cause is in the guard, not the operator workflow.

## Decision / Baseline / Proposed Tranche

Decision: CONTINUE.

Baseline: Rule C previously required `git rev-parse --short=8 HEAD` to appear
literally inside the active handoff text at pre-push time. A commit cannot
embed its own SHA in its own content, so any GC-020 sync commit (which is the
canonical way to update the handoff anchor) would fail Rule C at push time —
forcing the operator into a loop of repeated sync commits, none of which can
ever satisfy the guard.

Proposed tranche: accept HEAD short SHA OR HEAD~1 short SHA in the handoff
text. A GC-020 sync commit naturally records the SHA it synced (its parent),
so the parent-SHA branch passes for legitimate sync commits while drift is
still detected when the handoff anchor is older than HEAD~1.

Out of scope: changing Rule A, Rule B, the exemption registry, or any other
guard. No change to which files Rule C inspects.

## Evidence / Verification

- Guard test suite: `python -m pytest governance/compat/test_check_continuation_chain.py -v`
  must pass with 11/11 tests, including two new tests:
  - `test_rule_c_accepts_parent_sha` — confirms the paradox is resolved
  - `test_rule_c_fails_when_neither_head_nor_parent_present` — confirms drift
    is still detected
- Static CI gate: existing `scripts/run_cvf_static_ci_gate.py` must continue
  to invoke the updated script unchanged.
- Policy text updated in
  `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md` Rule C
  block to record the parent-SHA acceptance and the reason.

## Scope / Target / Owner Boundary

In scope:

- `governance/compat/check_continuation_chain.py` — `_check_handoff_head()`
  and a new `_git_parent_short()` helper.
- `governance/compat/test_check_continuation_chain.py` — adjust two existing
  Rule C tests for the new return-shape (now includes `parentSha`) and add
  two new tests for the paradox case and the missing-parent fallback.
- `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md` — Rule C
  description block only.

Out of scope (must not be touched):

- Rule A and Rule B logic
- Exemption registry schema or contents
- Other GC-020 enforcement scripts (handoff guard, active session state)
- Any handoff file content (handoffs are operator artifacts, not guard logic)

## Required Follow-Up

After this baseline is filed and the fix is committed:

1. Verify pre-push hook chain runs cleanly on the next governance commit
   without `--no-verify`.
2. Add a one-line entry to `CVF_INCREMENTAL_TEST_LOG.md` recording the new
   test count.
3. Update `MEMORY.md` snapshot if HEAD changes.

## Claim Boundary

This baseline only authorizes the Rule C acceptance change (HEAD OR HEAD~1).
It does NOT authorize relaxing Rule A, Rule B, the exemption registry, or any
other GC-020 enforcement surface.

## Final Clause

A single push attempt against `origin/main` immediately after this baseline
lands must complete cleanly with the standard pre-push hook chain enabled —
no `--no-verify`, no operator workaround.

## Verification

The only required evidence is `python -m pytest
governance/compat/test_check_continuation_chain.py -v` returning 11/11 PASS
and one clean `git push origin main` run. No live API, runtime, or release
evidence is claimed by this fix.
