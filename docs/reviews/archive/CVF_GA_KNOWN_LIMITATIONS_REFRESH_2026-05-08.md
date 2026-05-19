<!-- Memory class: FULL_RECORD -->
# CVF GA Known Limitations Refresh

**Date:** 2026-05-08
**Status:** CURRENT
**Readiness tier:** `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS`

## Still True After Post-RC2 GA Work

| Limitation | Current Boundary |
|---|---|
| Hosted CI2-H proof | Deferred. The protected GitHub hosted live gate was not dispatched from this local session because `gh` was unavailable and the local branch was ahead of `origin/main`. |
| Cost/quota precision | CQ counts expected live provider calls and enforces local caps. It does not calculate exact dollars or provider-side billable token cost. |
| Cost/quota deployment model | CQ is local-first via `.cvf/config/cost-quota-policy.json` and `.cvf/runtime/` audit. It is not multi-tenant cloud quota enforcement. |
| Runtime job persistence | Web governance jobs remain local-file backed. Supabase/Postgres can be added as an optional managed-deployment store later, not as the default local developer path. |
| DeepSeek coverage | Post-RC2 DS evidence is 8/8 smoke/sanity under CQ. It is not DeepSeek regression confirmation or full parity with Alibaba. |
| Clean-machine replay | This packet did not perform a new clean Windows bootstrap replay. Prior workspace-bootstrap evidence remains referenced but not freshly expanded. |
| Public learning loop | Issue triage SLO and contributor onboarding metrics remain future product maturity work. |
| Plugin/extension SDK | External community SDK depth remains future work. |

## Newly Reduced Risks

| Risk | Current Improvement |
|---|---|
| Browser-visible secret leakage in Web jobs | BR now covers 6 streams, including browser-visible response and network capture, using a deterministic fake-key probe. |
| Unbounded Web-triggered live gates | CQ preflight now gates Web `full_live_release_gate` and provider checks before command execution. |
| Cost/quota audit absence | CQ writes local append-only audit events for estimates, allowed/blocked decisions, override handling, and usage increments. |
| DeepSeek post-hardening unknown | DS smoke passed 8/8 live governed calls under CQ. |

## Public-Safe Summary

CVF is ready for local-first GA positioning with explicit limits: live Web
governance operations are allowlisted, redacted, and cost/quota guarded; hosted
CI2-H proof, multi-tenant quota enforcement, and broader provider parity remain
follow-up work.
