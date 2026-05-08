<!-- Memory class: FULL_RECORD -->
# CVF GC-018 Authorization — RC2-A1 Runtime Doctor + Provider Validation

Date: 2026-05-08

Status: AUTHORIZED

## Authorization

Operator authorized continuing the accepted RC2 Foundation roadmap with:
"tiến hành làm theo roadmap".

This authorization applies only to:

- Track: A — Install Productization
- Checkpoint: A1 — Runtime Doctor + Provider Validation

## Scope Lock

Allowed:

- Add a one-command runtime doctor.
- Add a secret-safe provider readiness command.
- Track the local env template required by A0.
- Add A1 roadmap, closure decision, and handoff sync.

Forbidden:

- Guided setup orchestration (`cvf_setup.py`) — reserved for A2.
- Web runtime health UI — reserved for Track B.
- Web-triggered governance jobs — reserved for Track C.
- New provider lanes.
- Raw key printing or credential commits.
- GA claims.

## Claim Boundary

A1 may claim that clone/runtime readiness and provider key readiness are
locally diagnosable. It may not claim guided first-run setup or zero-friction
install.
