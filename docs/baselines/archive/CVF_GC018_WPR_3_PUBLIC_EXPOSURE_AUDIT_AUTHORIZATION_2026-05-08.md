<!-- Memory class: FULL_RECORD -->
# CVF GC-018 - WPR-3 Authorization

> Date: 2026-05-08
> Tranche: WPR-3 - Public Exposure Audit
> Status: AUTHORIZED

## Decision

WPR-3 is authorized as a documentation and audit-only public-release packaging
tranche.

## Scope Lock

Allowed:

- Run file-name/count-based exposure scans that avoid printing raw secret
  values.
- Create one public exposure audit report with findings classified as
  `RESOLVED`, `ACCEPTED_BOUNDARY`, or `DEFERRED_TO_WPR_4`.
- Cross-reference the audit from handoff.
- Run docs hygiene and release gate verification.

Not allowed:

- Print, copy, or commit raw provider keys.
- Delete historical/canonical evidence files solely because their names contain
  `internal` or `handoff`.
- Perform broad license/package rewrites.
- Tag or publish a release; that is WPR-4 only.

## Exit Criteria

- `docs/reviews/CVF_PUBLIC_EXPOSURE_AUDIT_2026-05-08.md` exists.
- No raw key value is printed in the audit report.
- Every finding is classified.
- `git diff --check` passes.
- `python scripts/run_cvf_release_gate_bundle.py --json` passes.
