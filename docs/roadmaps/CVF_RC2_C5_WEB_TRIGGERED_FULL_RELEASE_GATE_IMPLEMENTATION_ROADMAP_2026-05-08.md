<!-- Memory class: FULL_RECORD -->
# CVF RC2 C5 Web-Triggered Full Release Gate Implementation Roadmap

**Date:** 2026-05-08
**Track:** RC2 Pre-GA / C5.2-C5.4
**Status:** CLOSED DELIVERED
**Authorization:** `docs/baselines/CVF_GC018_RC2_C5_IMPLEMENTATION_CANDIDATE_2026-05-08.md`

## Purpose

Allow an authorized Web operator to run the full live release gate from the
Governance Operations surface without exposing arbitrary shell execution,
leaking provider keys, or corrupting the controlling Web runtime.

## Delivered

| Checkpoint | Status | Evidence |
|---|---:|---|
| C5.2 allowlisted job type | CLOSED | `full_live_release_gate` fixed to `python scripts/run_cvf_release_gate_bundle.py --json` |
| C5.3 Web surface controls | CLOSED | `/governance/operations` card with live quota warning and owner/admin/operator role boundary |
| C5.4 evidence and redaction | CLOSED | `docs/reviews/CVF_C5_WEB_TRIGGERED_FULL_RELEASE_GATE_EVIDENCE_2026-05-08.md` |

## Runtime Controls

- Unknown job types remain blocked.
- Viewer/reviewer/anonymous roles cannot trigger live gates.
- Missing live key blocks the full gate before launch.
- A second full gate is blocked while one is queued or running.
- Child process stdout/stderr are redacted before response and persistence.
- Child release gate uses `NEXT_DIST_DIR=.next-cvf-release-gate` and
  `CVF_PLAYWRIGHT_PORT=3011` so the full gate build and nested Playwright
  server do not mutate the controlling Web server's `.next` tree.

## Verification

- Targeted C5 Vitest: 18/18 PASS.
- Browser probe: `node scripts/run_cvf_c5_web_release_gate_probe.mjs` PASS.
- Web-triggered release gate result: 7/7 PASS.

## Boundary

C5 proves local Web-triggered operator execution of the full live release gate.
It does not make local JSONL runtime state a managed multi-user store, and it
does not make Supabase/Postgres the default CVF persistence layer.
