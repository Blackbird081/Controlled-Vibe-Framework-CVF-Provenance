# CVF Web UX T4 R2 Supplemental Browser Acceptance Matrix

Memory class: governed-review-evidence
Status: BLOCKED_WITH_REASON

## Purpose
Matrix data for T4 R2 supplemental evidence.

## Target / Source
None

## Scope/Target/Owner Boundary
None

## Scope / Methodology
None

## Findings / Position

The 820px persistent-sidebar state and the 767px closed/open drawer pair are
visually supported. The preferences image is not an open-preferences state:
the retained screenshot shows only Home, and its own record reports
`visibleAnchorText` as `NOT_FOUND`. The five named focus records describe
generic header/sidebar controls rather than the required interaction targets.

## Risk / Corrective Action

File names and scenario labels cannot substitute for observed state. A narrow
R3 must bind every interaction to accessible target identity plus before/after
state, retain a genuinely open preferences screenshot, and classify all
diagnostics terminally.

## Decision/Recommendation/Disposition

`BLOCKED_WITH_REASON`: retain the three responsive screenshots as bounded
evidence; do not use this matrix to close T4.

## Claim Boundary
None

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | worker-return full fields; handoff route; closure conversion |
| gateRunPurpose | confirm R2 source fidelity and dispatch shape before execution |
| claimBoundary | gate PASS authorizes evidence work only |

## Epistemic Process Block
EPISTEMIC_PROCESS_NA_WITH_REASON: Matrix data only

## Matrix Data
| captureId | Viewport | Appearance | Route/state | Required visible anchor | URL | Focus/Navigation | overflow-x | Diagnostics | Status |
|---|---|---|---|---|---|---|---|---|---|
| `tablet-820-persistent-sidebar` | 820x1180 | light | persistent sidebar | `nav` | `http://localhost:3000/home` | Sidebar visibly persistent | None (820=820) | retained but not terminally classified | PASS_BOUNDED |
| `narrow-tablet-767-sidebar-closed` | 767x1024 | light | drawer closed | `h1` | `http://localhost:3000/home` | Drawer visibly closed | None (767=767) | retained but not terminally classified | PASS_BOUNDED |
| `narrow-tablet-767-sidebar-open` | 767x1024 | light | drawer open | `nav` | `http://localhost:3000/home` | Drawer visibly open | None (767=767) | retained but not terminally classified | PASS_BOUNDED |
| `desktop-dark-preferences-violet-open` | 1440x900 | dark/violet | claimed preferences open | expected close control absent; record says `NOT_FOUND` | `http://localhost:3000/home` | no selected-control proof | None (1440=1440) | retained but not terminally classified | FAIL |
