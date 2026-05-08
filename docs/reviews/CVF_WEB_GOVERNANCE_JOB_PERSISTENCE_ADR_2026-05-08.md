<!-- Memory class: FULL_RECORD -->
# CVF Web Governance Job Persistence ADR

Date: 2026-05-08

Status: ACCEPTED FOR RC2 TRACK C

## Decision

Use file-backed JSONL for RC2 Web governance job audit persistence.

Default path:

```text
.cvf/runtime/web-governance-jobs.jsonl
```

SQLite and PostgreSQL are deferred. JSONL is sufficient for RC2 because C3/C4
need append-only lifecycle evidence and recent-job inspection, not complex
multi-user query behavior.

## Context

C0 requires auditability for every Web-triggered governance job attempt,
including blocked attempts. C1 requires role, auth mode, and policy decision
data. C3 needs a minimal implementation with low operational friction for fresh
clone users.

## Alternatives Considered

| Option | Decision | Reason |
|---|---|---|
| in-memory only | rejected | loses audit trail and cannot prove trigger attempts |
| JSONL | accepted | simple, append-only, inspectable, fresh-clone friendly |
| SQLite | deferred | useful later for filters but unnecessary for RC2 minimum |
| PostgreSQL | rejected for RC2 | too heavy for local-first RC target |

## Event Schema

Each line is one JSON object.

Required fields:

| Field | Type | Notes |
|---|---|---|
| `eventId` | string | deterministic or UUID-like unique id |
| `jobId` | string | stable id shared across lifecycle events |
| `eventType` | string | `requested`, `blocked_by_policy`, `queued`, `running`, `succeeded`, `failed`, `timed_out`, `orphaned` |
| `jobType` | string | enum from C0 allowlist |
| `requestedBy` | string | user/session label, never secret |
| `role` | string | enum from C1 |
| `authMode` | string | `authenticated`, `service_token`, `anonymous_local`, `unknown` |
| `localMode` | boolean | whether local-mode exception was active |
| `requestIpClass` | string | `loopback`, `private_network`, `public_or_unknown`, `not_recorded` |
| `requestedAt` | string | ISO timestamp |
| `recordedAt` | string | ISO timestamp |
| `decision` | string | `allowed` or `blocked_by_policy` |
| `decisionReason` | string | human-safe reason |
| `status` | string | current lifecycle status |
| `cwdLabel` | string | basename/relative label, not full private path when avoidable |
| `handlerId` | string | fixed internal handler id |
| `fixedArgv` | string[] | fixed argv only; no raw shell |
| `providerLane` | string or null | provider name/model label when relevant |
| `redactionApplied` | boolean | must be true before output persistence |
| `stdoutSummary` | string | redacted and capped |
| `stderrSummary` | string | redacted and capped |
| `exitCode` | number or null | process/internal result |
| `timeoutMs` | number | configured timeout |
| `timedOut` | boolean | timeout result |
| `errorClass` | string or null | normalized error label |
| `evidenceRefs` | string[] | repo-relative artifact refs |
| `uiRequestId` | string | UI correlation id |
| `correlationId` | string | cross-event correlation id |

## Redaction Rules

Before persistence and before UI display:

- replace values of known key env vars with `[REDACTED]`;
- redact any token-like substring matching high-entropy secret patterns;
- cap stdout and stderr summaries to 12,000 characters each for RC2;
- store provider lane labels but never raw provider key values;
- store repo-relative paths where practical, not full user-private paths.

Known key names include:

- `DASHSCOPE_API_KEY`
- `ALIBABA_API_KEY`
- `CVF_ALIBABA_API_KEY`
- `CVF_BENCHMARK_ALIBABA_KEY`
- `DEEPSEEK_API_KEY`

## Retention

RC2 default:

- retain latest 500 events;
- compaction may keep the newest 500 complete JSONL lines;
- export uses redacted summaries only;
- raw stdout/stderr full logs are not retained in RC2.

## Local Privacy Boundary

The JSONL file is local workspace state. It may contain:

- user/session labels;
- job type and timing;
- redacted outputs;
- provider lane labels;
- evidence refs.

It must not contain:

- raw API keys;
- arbitrary file contents;
- arbitrary command input;
- full unbounded provider output;
- private absolute paths unless unavoidable for an error class.

## C3 Implementation Requirements

- append-only write path only;
- create `.cvf/runtime/` if missing;
- fail closed if audit append fails for allowed trigger attempts;
- blocked attempts should still be audited when possible;
- no shell command may be constructed from user input;
- job status is derived from latest event for a `jobId`;
- orphan detection emits an `orphaned` event rather than mutating prior lines.

## C4 UI Requirements

- show lifecycle status and latest redacted summary;
- show audit event id and job id;
- show provider lane metadata, never raw key;
- allow redacted summary export for authorized roles only;
- distinguish `blocked_by_policy` from runtime failure.

## Claim Boundary

Allowed after C2:

> Persistence and audit log boundary is decided.

Still forbidden after C2:

- Audit logging is implemented.
- Web can trigger governance jobs.
- Full release gate can run from Web.
