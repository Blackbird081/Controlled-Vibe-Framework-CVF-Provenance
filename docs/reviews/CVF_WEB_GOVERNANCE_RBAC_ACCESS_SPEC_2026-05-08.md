<!-- Memory class: FULL_RECORD -->
# CVF Web Governance RBAC + Access Control Specification

Date: 2026-05-08

Status: C1 BASELINE FOR RC2 TRACK C

## Purpose

This specification maps roles to read and trigger permissions for the
non-destructive Web governance job classes defined in C0.

It is a specification only. Enforcement is not implemented until C3/C4.

## Roles

| Role | Intent | Typical holder |
|---|---|---|
| `owner` | Full local project authority for non-destructive governance operations | repository owner / release operator |
| `admin` | Operational authority under owner boundary | trusted maintainer |
| `operator` | Day-to-day diagnostics and provider readiness | developer/operator |
| `reviewer` | Inspect evidence and job outcomes | reviewer / auditor |
| `viewer` | Read-only observability | community user / local reader |
| `anonymous_local` | Browser session without authenticated identity | local-only fallback mode |

## Read Permissions

| Surface | owner | admin | operator | reviewer | viewer | anonymous_local |
|---|---:|---:|---:|---:|---:|---:|
| system health read | yes | yes | yes | yes | yes | local-only |
| module registry read | yes | yes | yes | yes | yes | local-only |
| governance evidence read | yes | yes | yes | yes | yes | local-only |
| job status read | yes | yes | own/all | all | redacted/all | redacted/local-only |
| audit summary export | yes | yes | yes | yes | no | no |
| redacted output read | yes | yes | own/all | all | summary only | summary only |

`anonymous_local` exists only for an explicitly local development deployment. It
must not be treated as public-network safe.

## Trigger Permissions

| Job class | owner | admin | operator | reviewer | viewer | anonymous_local |
|---|---:|---:|---:|---:|---:|---:|
| `read_only_diagnostics` | yes | yes | yes | no | no | allowed only with local-mode warning |
| `provider_readiness_validation` | yes | yes | yes | no | no | no |
| `targeted_non_destructive_governance_check` | yes | yes | yes | no | no | no |
| `release_gate_dry_readiness` | yes | yes | yes | no | no | no |
| full live release gate | C5 only | C5 only | no | no | no | no |

## Permission Rules

- Read-only Track B endpoints remain readable by all configured roles.
- Trigger endpoints must require a recognized role.
- `anonymous_local` may trigger only `read_only_diagnostics`, and only when C3
  can determine the deployment is local mode.
- Provider validation must require an explicit user action and role
  `owner`, `admin`, or `operator`.
- Full live release gate is not part of C3/C4 and must be hard-denied until C5.
- Viewer/reviewer roles must never trigger jobs.
- Unauthorized trigger attempts must be audited as `blocked_by_policy`.

## Local Mode Boundary

Local mode is allowed only when all are true:

- request originates from loopback or explicitly configured local host;
- job class is `read_only_diagnostics`;
- no provider call is needed;
- no filesystem mutation is performed except append-only audit logging after C2;
- UI displays a local-mode warning before trigger.

If any condition is false, `anonymous_local` must be treated as `viewer`.

## Trigger Attempt Audit Fields

C2/C3 must capture these fields for every trigger attempt, including blocked
attempts:

- `jobId`;
- `jobType`;
- `requestedBy`;
- `role`;
- `authMode`;
- `localMode`;
- `requestIpClass`;
- `requestedAt`;
- `decision`: `allowed` or `blocked_by_policy`;
- `decisionReason`;
- `providerLane` when relevant, never raw key;
- `redactionApplied`;
- `uiRequestId`;
- `correlationId`.

## C3 Enforcement Inputs

C3 runner must expose a pure permission check:

```text
canTrigger(role, jobType, context) -> allowed | blocked_by_policy
```

The check must be testable without launching a job. It must fail closed for
unknown role, unknown job type, unknown auth mode, and unknown local-mode state.

## C4 UI Inputs

C4 UI must:

- hide or disable trigger controls for unauthorized roles;
- display why the control is unavailable;
- display local-mode warning for allowed anonymous diagnostics;
- distinguish dry readiness from live proof;
- display provider validation warning before any provider call;
- show audit/event id after a trigger attempt.

## Claim Boundary

Allowed after C1:

> RBAC and access boundary for non-destructive Web-triggered governance
> operations is specified.

Still forbidden after C1:

- RBAC is enforced.
- Web can trigger governance jobs.
- Audit logging exists.
- Full release gate can run from Web.
