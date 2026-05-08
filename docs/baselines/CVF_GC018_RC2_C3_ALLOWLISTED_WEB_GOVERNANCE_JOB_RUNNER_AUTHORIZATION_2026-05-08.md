<!-- Memory class: SUMMARY_RECORD -->
# CVF GC-018 Authorization — RC2-C3 Allowlisted Web Governance Job Runner

Date: 2026-05-08

Status: AUTHORIZED

## Authorization

Operator authorized continuing the accepted RC2 Foundation roadmap with:
"tiến hành làm theo roadmap".

This authorization applies only to:

- Track: C — Governed Web Operations Enablement
- Checkpoint: C3 — Allowlisted Non-Destructive Governance Job Runner

## Scope Lock

Allowed:

- Implement an allowlisted non-destructive job runner.
- Add fixed-argv jobs for doctor, provider check, docs governance check, and
  release-gate dry readiness.
- Add job lifecycle and append-only JSONL audit logging.
- Add permission check from C1.
- Add redaction, timeout, fixed cwd, and failure-mode tests.
- Add `GET/POST /api/system/jobs`.
- Publish roadmap, closure, and handoff sync.

Forbidden:

- Free-form shell commands.
- Arbitrary filesystem writes.
- Full live release gate.
- Web Operations UI trigger controls.
- Live provider validation by default.
- Claiming Web operations UI is complete.

## Claim Boundary

C3 may claim only that a bounded allowlisted non-destructive Web governance job
runner exists with audit, redaction, timeout, and policy-block behavior. It may
not claim the Web operations UI is complete or that full live release gate can
run from Web.
