# CVF GC-018 — EVT-4 Output Quality A/B Baseline

**Date:** 2026-05-14  
**Status:** APPROVED BY USER FOR EXECUTION  
**Scope:** EVT-4 only — compare output quality of ungoverned provider calls vs CVF-governed `/api/execute` for R0/R1 non-coder tasks.

## Authorization

User explicitly authorized completion of the remaining EVT roadmap and allowed
use of available provider keys for testing. This GC-018 authorizes a bounded
measurement harness and live run. It does not authorize QBS reopening, hard-gate
logic changes, provider-routing policy changes, or new quality ladder claims.

## Allowed Work

- Create a frozen 20-prompt R0/R1 non-coder corpus.
- Run CFG-A: direct Alibaba/DashScope call without CVF governance overlay.
- Run CFG-B: same task through CVF `/api/execute` with live governance receipt.
- Use one model-assisted reviewer when available; otherwise fall back to the
  deterministic rubric and mark reviewer mode clearly.
- Publish evidence with output excerpts, hashes, scores, and delta summary.

## Boundaries

- This is not a QBS rerun.
- No BLOCK/CLARIFY/NEEDS_APPROVAL threshold changes.
- No execution-order optimization.
- No provider parity claim.
- No raw API keys printed or committed.
- Claims must be scoped to this 20-prompt R0/R1 corpus only.

## Exit Criteria

- [ ] Preregistration artifact exists before/with the run protocol.
- [ ] 20 prompts are frozen in the runner.
- [ ] 40 executions complete or failures are explicitly counted.
- [ ] Reviewer/scoring mode is documented.
- [ ] Evidence summary records CFG-B vs CFG-A delta and caveats.
