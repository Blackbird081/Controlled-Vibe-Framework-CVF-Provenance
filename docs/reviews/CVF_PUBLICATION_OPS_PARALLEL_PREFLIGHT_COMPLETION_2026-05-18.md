# CVF Publication Ops Parallel Preflight Completion - 2026-05-18

Memory class: FULL_RECORD
Status: PUBLICATION_OPS_PREFLIGHT_PROGRESS_READY

## Purpose

Record the publication-ops audit and implementation that makes local push
governance preflight visible while it is running.

## Scope / Target / Owner Boundary

Target files:

- `governance/compat/run_local_governance_hook_chain.py`
- `scripts/cvf-provenance-push.ps1`

Owner boundary: local provenance-publication operations only.

## Source

Operator request on 2026-05-18 asked Codex to check the existing Claude
publication helper, identify why hook progress was opaque, and add a faster or
more observable method for the many push guards.

Existing helper found:

- `scripts/cvf-provenance-push.ps1`

## Non-Goals

- No public repository push is performed by this packet.
- No provenance push is performed by this packet.
- No guard is removed, skipped, weakened, or marked optional.
- No public claim, release gate, GA posture, provider behavior, or governance
  proof claim is changed.

## Work Plan

1. Audit existing provenance push helper and hook-chain runner.
2. Preserve the default hook-chain behavior for normal Git hooks.
3. Add explicit progress flushing for sequential mode.
4. Add opt-in parallel local preflight mode for operator-run checks.
5. Wire the provenance push helper to stream hook output directly and expose
   `-ParallelPreflight`.
6. Verify both sequential and parallel paths locally.

## Findings / Position

The existing push helper already contained the correct safety model: it checks
that it is running in the provenance repo, requires the push URL to be locked,
requires a clean working tree, runs the pre-push hook chain before enabling the
push URL, and re-locks the URL after push.

The visibility failure was caused by capturing the hook output into a
PowerShell variable. That meant operators saw no per-check progress until the
Python process completed.

The corrected implementation streams hook output live and adds an opt-in
parallel preflight mode that reports:

- total check count;
- check start events;
- PASS/FAIL completion count;
- per-check runtime;
- failure summaries with command output.

## Decision

Accept the publication-ops improvement as local operator tooling.

Default Git hook behavior remains sequential. Parallel mode is explicit:

```bash
python governance/compat/run_local_governance_hook_chain.py --hook pre-push --parallel --max-workers 6
```

The provenance helper exposes the same behavior:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -DryRun -ParallelPreflight
```

## Acceptance Criteria

| Criterion | Result |
|---|---|
| Existing publication helper identified | PASS |
| Hook output streams live instead of being captured until completion | PASS |
| Sequential mode prints `[current/total]` progress | PASS |
| Parallel preflight prints start, completion, runtime, and failures | PASS |
| Default Git hook behavior remains available | PASS |
| No guard is skipped or removed | PASS |
| No push is performed during this packet | PASS |

## Risk / Corrective Action

Risk: parallel execution can interleave long-running guard work and expose
ordering assumptions in guards that were originally run sequentially.

Corrective action: parallel mode is opt-in for local preflight visibility.
Default hook mode remains sequential, and failures still block push.

Risk: the push helper cannot proceed if the local push URL is not locked.

Corrective action: the helper aborts before running push operations and prints
the exact local remote state that must be corrected.

## Evidence Trace Block

| Claim | Evidence | Result |
|---|---|---|
| Existing Claude provenance helper was found | `scripts/cvf-provenance-push.ps1` | ACCEPTED |
| Sequential progress output works | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS |
| Parallel progress output works | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit --parallel --max-workers 3` | PASS |
| Provenance helper safety guard remains active | `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -DryRun -ParallelPreflight` | ABORTED before checks because local push URL was not locked |
| Full pre-push parallel runner exposes progress and failure location | `python governance/compat/run_local_governance_hook_chain.py --hook pre-push --parallel --max-workers 6` | Reached 38/39 PASS before this review packet existed; failed only baseline update compatibility |

## Verification

Commands run:

```bash
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit --parallel --max-workers 3
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -DryRun -ParallelPreflight
python governance/compat/run_local_governance_hook_chain.py --hook pre-push --parallel --max-workers 6
```

Results:

- parallel pre-commit: PASS;
- sequential pre-commit: PASS;
- provenance helper dry-run: safety ABORT before checks because `origin` push
  URL was not in the expected disabled state;
- pre-push parallel preflight before this packet: 38/39 PASS, with only
  baseline update compatibility blocking due to missing review artifact.

Test depth markers: T1=0, T2=0, T3=0, T4=0, Meaningful=NO. These results are
governance/tooling preflight outcomes, not product test-count coverage claims.

## Related Artifacts

- `AGENT_HANDOFF_V9_2026-05-18.md`
- `governance/compat/run_local_governance_hook_chain.py`
- `scripts/cvf-provenance-push.ps1`
