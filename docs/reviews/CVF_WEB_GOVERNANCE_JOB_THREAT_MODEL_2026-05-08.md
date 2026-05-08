<!-- Memory class: FULL_RECORD -->
# CVF Web Governance Job Threat Model

Date: 2026-05-08

Status: C0 BASELINE FOR RC2 TRACK C

## Purpose

This threat model defines the boundary for future Web-triggered governance jobs.
It exists before RBAC, persistence, runner, or UI triggers are implemented.

## Allowed Job Classes

| Class | Examples | Live provider use | Mutation | C5 required? |
|---|---|---:|---:|---:|
| `read_only_diagnostics` | runtime doctor, dependency/readiness checks, docs governance dry check | No | No | No |
| `provider_readiness_validation` | Alibaba/DeepSeek provider key validation with explicit operator action | Optional | No | No |
| `targeted_non_destructive_governance_check` | docs governance check, secret scan, known bounded static checks | No | No | No |
| `release_gate_dry_readiness` | prerequisite scan for release gate availability without running live E2E | No | No | No |

## Forbidden Job Classes

| Class | Reason |
|---|---|
| arbitrary shell command | Command injection, filesystem damage, secret exfiltration |
| arbitrary filesystem write | Can mutate repo state outside governed path |
| arbitrary git operation | Can rewrite history, publish unreviewed changes, or destroy worktree |
| package install/update | Supply-chain and lockfile mutation risk |
| destructive cleanup | Data loss risk |
| full live release gate | Long-running live provider/cost/output surface; belongs to C5 |
| unbounded provider prompt | Cost, data leakage, and governance-claim risk |
| external tool/plugin execution | Expands trust boundary beyond local CVF controls |

## Assets

- Provider keys visible to the process environment.
- Local repo and worktree state.
- Evidence packets and audit logs.
- Governance policies, approvals, and ledger state.
- Operator identity and role.
- Job output, including stdout/stderr and provider diagnostic text.
- Browser session state and CSRF surface.
- Community user trust in CVF public claims.

## Trust Boundaries

| Boundary | From | To | Required control |
|---|---|---|---|
| Browser to API | User-controlled browser input | Next.js API route | RBAC, CSRF posture, schema validation |
| API to runner | Web request | allowlisted server job runner | no free-form command, typed job id |
| Runner to process | job runner | child process or internal function | fixed argv, timeout, cwd lock |
| Process to filesystem | job execution | repo files/logs | allowed paths only, no arbitrary write |
| Process to provider | provider validation job | external API | explicit role, redaction, timeout, rate limit |
| Runner to audit log | job lifecycle | persistent audit store | append-only event schema |
| API to UI | job output | browser display | raw secret redaction and output size cap |

## Entry Points

- Future `POST /api/system/jobs` or equivalent trigger endpoint.
- Future `GET /api/system/jobs/:id` status endpoint.
- Future Web Operations UI controls.
- Existing read-only endpoints from Track B must remain non-triggering.

## Abuse Cases And Controls

| Abuse case | Impact | Required control before C3/C4 |
|---|---|---|
| User submits `jobId=cmd` with shell payload | arbitrary code execution | enum-only job id, no shell interpolation |
| User changes provider validation to print env | secret exfiltration | centralized redaction, deny raw env echo |
| Repeated live provider validation spam | cost/quota exhaustion | per-role rate limit and cooldown |
| Long-running job hangs server | availability loss | hard timeout, orphan detection, status transition |
| Unauthenticated local browser triggers jobs | unauthorized local mutation/cost | C1 role model and explicit local-mode warning |
| Job output includes sensitive file content | data leak | output allowlist, size cap, redaction before persistence/display |
| Runner writes outside audit path | repo damage | C2 path allowlist and append-only audit contract |
| UI claims full governance proof from dry check | overclaim | result labels distinguish dry/readiness/live proof |
| C3 accidentally includes full release gate | cost and scope explosion | C5-only gate, explicit deny in runner allowlist |
| Concurrent jobs corrupt audit state | evidence ambiguity | job id uniqueness, lifecycle state machine, append-only events |

## Required Controls Before Implementation

- C1: Role matrix for read vs trigger permissions.
- C2: Append-only audit/persistence ADR with redaction and retention.
- C3: Allowlisted runner with typed job definitions and fixed argv.
- C3: Job lifecycle states: queued, running, succeeded, failed, timed_out,
  blocked_by_policy, orphaned.
- C3: Timeout, output size cap, cwd lock, and no shell execution.
- C3: Redaction layer before output persistence or UI display.
- C4: UI warnings for provider/cost-bearing validation jobs.
- C4: Unauthorized trigger blocked tests and authorized trigger audited tests.
- C5: Separate live-provider release gate controls before any full release gate
  trigger is allowed.

## Residual Risks

| Risk | Treatment |
|---|---|
| Local operator exposes Web app on public network | Document local-mode boundary; C1 decides unauthenticated mode |
| Provider validation still consumes small quota | C1/C3 require explicit trigger, timeout, rate limit |
| Static checks can drift from release gate truth | UI labels dry readiness separately from live proof |
| Audit log can grow on repeated jobs | C2 defines retention and compaction/export boundary |
| Redaction misses novel secret shape | C3/C4 tests cover known env names; future C5 adds live-output review |

## C1 Inputs

C1 must decide which roles can:

- read health/module/evidence state;
- trigger `read_only_diagnostics`;
- trigger `provider_readiness_validation`;
- trigger `targeted_non_destructive_governance_check`;
- trigger `release_gate_dry_readiness`;
- view raw-ish redacted output;
- export audit summaries.

## C2 Inputs

C2 must define persisted fields for:

- job id;
- job type;
- requested by;
- role;
- request timestamp;
- lifecycle transitions;
- cwd/repo root label;
- fixed argv or internal handler id;
- provider lane metadata without raw key;
- redacted stdout/stderr summary;
- exit code;
- timeout flag;
- error class;
- evidence artifact refs;
- retention policy.

## C3 Stop Rules

C3 must stop if:

- any job requires free-form command execution;
- any implementation needs arbitrary filesystem write;
- RBAC or audit ADR is not closed;
- full live release gate is requested before C5;
- redaction cannot be applied before persistence/display;
- timeout and orphan handling cannot be tested.

## Claim Boundary

Allowed after C0:

> Threat model for Web-triggered governance jobs is defined.

Still forbidden after C0:

- CVF Web can trigger governance jobs.
- RBAC is implemented.
- Audit logging exists for triggered jobs.
- Web-triggered governance operations are complete.
- Full release gate can run from Web.
