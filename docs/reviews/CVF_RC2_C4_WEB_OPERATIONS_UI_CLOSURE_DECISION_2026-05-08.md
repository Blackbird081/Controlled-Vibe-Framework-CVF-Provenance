<!-- Memory class: FULL_RECORD -->
# CVF RC2-C4 Web Operations UI Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

RC2-C4 is closed. CVF Web now exposes a bounded Web Operations UI for the C3
allowlisted non-destructive governance job runner.

## Delivered

- Web surface:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/page.tsx`
- Governance dashboard link:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.tsx`
- UI tests:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/page.test.tsx`

## Result

The Web Operations UI supports:

- role readout from `/api/auth/me` with `developer` mapped to `operator`;
- anonymous local warning;
- controls for `cvf_doctor`, Alibaba/DeepSeek provider check, docs governance
  check, and release-gate dry readiness;
- disabled states for unauthorized local/readonly roles;
- job status and audit trail readout from `GET /api/system/jobs`;
- job submission through `POST /api/system/jobs`;
- redacted audit summary copy/export.

## Verification

Targeted verification completed:

```bash
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/app/(dashboard)/governance/operations/page.test.tsx src/lib/server/web-governance-jobs.test.ts src/app/api/system/jobs/route.test.ts
```

Result: 3 files passed / 13 tests passed.

Typecheck note: full `npx tsc --noEmit` remains blocked by pre-existing test
typing drift recorded in B1. A filtered re-run showed no
`governance/operations`, `web-governance-jobs`, or `api/system/jobs` type
errors.

## Track C Claim Boundary

Allowed after C4:

> CVF Web can trigger selected allowlisted non-destructive governance operations
> (diagnostics, validation, evidence inspection) under RBAC-derived role checks,
> audit logging, redaction, timeout, and evidence controls.

Still forbidden:

- CVF Web can run arbitrary jobs.
- CVF Web fully replaces CLI/operator workflows.
- CVF Web fully controls every CVF runtime module.
- Full live release gate can run from Web.
- GA-ready.

## Next Checkpoint

RC2-C5 is a separate high-rigor wave for full live release gate trigger
enablement. It requires additional cost, timeout, rate-limit, redaction, and
live-provider threat review before implementation.
