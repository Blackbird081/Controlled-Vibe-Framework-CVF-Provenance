<!-- Memory class: FULL_RECORD -->
# CVF RC2-C3 Allowlisted Web Governance Job Runner Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

RC2-C3 is closed. CVF Web now has a bounded allowlisted non-destructive
governance job runner with policy blocking, fixed argv, timeout handling,
redaction, and append-only JSONL audit events.

## Delivered

- Runner:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts`
- API route:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts`
- Tests:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.test.ts`
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.test.ts`

## Allowed Jobs

| Job type | Fixed argv | Notes |
|---|---|---|
| `cvf_doctor` | `python scripts/cvf_doctor.py --json` | read-only diagnostics |
| `provider_check` | `python scripts/cvf_provider_check.py --provider <alibaba|deepseek> --json` | no live flag by default |
| `docs_governance_check` | `python governance/compat/check_docs_governance_compat.py --base HEAD~1 --head HEAD --json` | static docs governance check |
| `release_gate_dry_readiness` | `python scripts/run_cvf_release_gate_bundle.py --dry-run --json` | dry readiness only |

Full live release gate is not included in C3.

## Audit

Audit events are append-only JSONL at:

```text
.cvf/runtime/web-governance-jobs.jsonl
```

Recorded lifecycle states include `requested`, `running`, `succeeded`,
`failed`, `timed_out`, and `blocked_by_policy`.

## Verification

Targeted verification completed:

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/lib/server/web-governance-jobs.test.ts src/app/api/system/jobs/route.test.ts
```

Result: 2 files passed / 10 tests passed.

Coverage includes:

- authorized allowlisted diagnostic job;
- viewer trigger blocked before launch;
- anonymous local mode restricted to diagnostics;
- invalid provider blocked before launch;
- redaction before persistence;
- timeout state;
- GET/POST route behavior;
- 403 for blocked triggers.

Typecheck note: full `npx tsc --noEmit` remains blocked by pre-existing test
typing drift recorded in B1. A filtered re-run showed no `web-governance-jobs`
or `api/system/jobs` type errors.

## Boundary

C3 implements the runner and API, not the user-facing Web Operations UI. Live
provider validation is not enabled by default. Full live release gate remains
excluded until C5.

## Next Checkpoint

Proceed to RC2-C4 after fresh GC-018 authorization:

- Add Web Operations UI for the C3 job runner.
- Render role-aware trigger controls.
- Show job status and audit trail.
- Preserve redaction and blocked-trigger behavior.
