<!-- Memory class: FULL_RECORD -->
# CVF C5 Full Release Gate Web Trigger Threat Model

**Date:** 2026-05-08  
**Track:** RC2 Pre-GA / C5.0  
**Status:** ACCEPTED DESIGN INPUT  

## Purpose

Define the threat model for allowing CVF Web to trigger the canonical full live
release gate:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

## Assets

- Live provider keys available to the local process.
- Local repository state and uncommitted work.
- Release gate stdout/stderr.
- Web governance job audit log.
- Evidence artifacts and screenshots.
- Operator identity and role.
- User trust in release-quality governance claims.

## Threats And Required Controls

| Threat | Impact | Required control |
|---|---|---|
| Arbitrary command injection | code execution / data loss | fixed job type, fixed argv, cwd locked to repo root |
| Cost/quota exhaustion | provider spend / throttling | role gate, confirmation copy, cooldown, one active gate at a time |
| Provider key leakage | secret exposure | pre-display redaction, persisted-state redaction, fake-key positive test |
| Confused deputy provider use | unauthorized live calls | owner/admin/operator only; no anonymous full gate |
| Long-running Playwright process | availability loss | bounded timeout, running status, orphan transition |
| Concurrent gate trigger | evidence ambiguity / resource contention | block while any full gate is running |
| Dirty/unsupported preflight | invalid evidence | preflight block where gate state would be misleading |
| Partial output overclaim | false release signal | UI labels partial/failed/timed-out separately from PASS |
| Stale replay | misleading old evidence | every run has unique job id, timestamp, evidence refs |
| Browser response leakage | secret in network payload | C5.4 verifies browser-visible response/HAR contains no fake key |

## Required Implementation Inputs

- New job type may be added only as `full_live_release_gate`.
- The browser must not provide arbitrary argv.
- The handler must execute the canonical command only.
- Redaction must run before stdout/stderr are persisted or returned.
- Missing-key and invalid-key states must fail closed.
- C5.4 must include a deterministic fake-key redaction probe.

## Residual Risks

| Risk | Treatment |
|---|---|
| Local operator exposes Web to public network | keep full gate role-gated; document local install boundary |
| Provider billing varies by account | warn before running; do not estimate exact cost as fact |
| Redaction misses unknown secret shape | positive fake-key test plus known env-name redaction; future expanders add patterns |
| CI2 later differs from C5 local path | CI2 must reuse canonical release command and redaction posture |

## Claim Boundary

Allowed:

> C5 full live release-gate Web trigger threats and controls are defined.

Forbidden:

- Web can trigger the full live release gate.
- C5 implementation is complete.
- Release gate CI is implemented.
