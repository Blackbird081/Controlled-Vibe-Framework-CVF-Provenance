<!-- Memory class: FULL_RECORD -->
# CVF RC2-A0 Install Reality Audit Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

RC2-A0 is closed. The fresh Windows clone audit identified the install
productization blockers that must feed RC2-A1 and RC2-A2.

## Evidence

- Fresh clone path:
  `C:\Users\DELL\AppData\Local\Temp\cvf-rc2-a0-fresh-clone-20260508-133140`
- Probe commit: `27307b88`
- `npm ci --dry-run --ignore-scripts` in `cvf-web`: PASS
- Node/npm/Python present on the probe machine
- Ports 3000 and 3001 free at probe time

## Blocking Findings

1. `cvf-web/.env.example` is missing from fresh clone because `.env*` ignores
   it, while deploy docs reference it as the `.env.local` shape.
2. No one-command readiness doctor exists.
3. No secret-safe provider readiness command exists.
4. No guided first-run setup orchestrator exists.

## Next Checkpoint

Proceed to RC2-A1 only after fresh GC-018 authorization:

- `scripts/cvf_doctor.py --json`
- `scripts/cvf_provider_check.py --provider alibaba --json`
- structured classification for dependency, env, port, Playwright, and
  provider readiness failures

## Boundary

A0 is audit-only. No runtime behavior, Web UI, provider lane, release gate, or
setup command changed in this checkpoint.
