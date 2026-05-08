<!-- Memory class: FULL_RECORD -->
# CVF Cost/Quota Guard Threat Model

**Date:** 2026-05-08
**Status:** FILED
**Track:** CQ0 - Cost/Quota Guard Threat Model

## Threats

| Threat | Risk | Control |
|---|---|---|
| Repeated Web `full_live_release_gate` clicks | Live provider quota/cost spike | Server-side preflight, cooldown, usage audit |
| Repeated hosted CI/manual release gates | Quota exhaustion and noisy evidence | CI2-H manual confirmation plus CQ local guard for Web jobs |
| Provider matrix expansion before budget check | DS/Alibaba evidence consumes more calls than planned | CQ before DS sequencing |
| Direct API bypass of Web confirmation | UI warning can be skipped | `/api/system/jobs` enforces the same preflight |
| Operator override misuse | Budget controls bypassed without trace | Owner/admin-only override plus audit event |
| Policy file contains secrets | Accidental key exposure | `.cvf/config/` ignored; policy scanner blocks secret-like values |
| Quota exhaustion mistaken for regression | False negative in DS/live matrix | Provider-lane usage and explicit failure classification |

## Boundary

- CQ is a local-first call-count guard, not exact billing reconciliation.
- No cloud FinOps dashboard or multi-tenant quota enforcement is claimed.
- Supabase/Postgres remains deferred optional managed-mode work.
