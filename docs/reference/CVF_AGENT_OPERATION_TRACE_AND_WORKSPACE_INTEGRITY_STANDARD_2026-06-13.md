# CVF Agent Operation Trace And Workspace Integrity Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

docType: reference_standard

Date: 2026-06-13

Owner: Codex

rawMemoryReleased=false

## Purpose

Define the repo-local evidence that CVF requires when agents or provider
surfaces execute governed work.

CVF does not develop `codex_cowork`, `claude_cowork`, agent computer-control
surfaces, operating-system audit tooling, endpoint monitoring, or provider
runtime features. Those capabilities belong to their platform providers and to
operator-selected infrastructure.

CVF's core responsibility is control-plane supervision: when an agent/provider
surface performs governed work, the work must leave enough evidence for review,
scope validation, rollback, and bounded attribution inside the repository.

## Scope / Target / Owner Boundary

In scope:

- repo-local operation trace evidence for work orders, worker returns, and
  completion reviews;
- changed-path evidence from `git status --short` and `git diff --name-status`;
- detection of protected governed path deletion or rename in changed ranges;
- explicit claim boundaries separating repo evidence from OS-level identity or
  endpoint audit claims.

Out of scope:

- Windows Security Audit policy configuration;
- Sysmon, EDR, file watcher services, or endpoint telemetry installation;
- destructive broker design;
- agent computer-control permission changes;
- provider platform feature development;
- proof of who physically used the machine;
- proof that no external process modified the filesystem outside repo-visible
  evidence.

## Rule

Any changed work order, worker-return packet, or completion review that acts as
agent execution evidence must include an `Agent Operation Trace Block`.

The block must be filled with command, path, or artifact evidence where
available. `N/A with reason` is allowed only when the field truly cannot apply
to the work being closed.

Protected governed path deletion or rename must be visible in the trace block
through a `Deletion or rename disposition` row before the work may pass the
agent-operation trace gate.

## Required Agent Operation Trace Block

```text
## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | <agent/operator/provider role> |
| Provider or surface | <Codex, Claude, CLI, IDE tab, MCP, browser, etc.> |
| Session or invocation | <session id, commit range, or N/A with reason> |
| Working directory | <cwd or repo root> |
| Command or tool surface | <commands/tools used; safe summaries allowed> |
| Target paths | <changed or intended paths> |
| Allowed scope source | <operator instruction, roadmap, GC-018, work order> |
| Before status evidence | <git status --short, base HEAD, or N/A with reason> |
| After status evidence | <git status --short or closure status evidence> |
| Diff evidence | <git diff --name-status / committed range> |
| Approval boundary | <what was authorized and by whom/source> |
| Claim boundary | <repo-local trace only; no OS/user attribution unless separately proven> |
| Deletion or rename disposition | <required only when protected paths are deleted/renamed; otherwise N/A with reason> |
```

## Protected Repo-Local Integrity Surface

The protected repo-local surface includes:

- `.github/`;
- `AGENTS.md`;
- `CVF_SESSION/`;
- `CVF_SESSION_MEMORY.md`;
- `docs/baselines/`;
- `docs/reference/`;
- `docs/reviews/`;
- `docs/roadmaps/`;
- `docs/work_orders/`;
- `governance/compat/`.

The checker may expand this list later through a separate governed work order.

## Enforcement

Machine checker:

`governance/compat/check_agent_operation_trace.py`

Focused tests:

`governance/compat/test_check_agent_operation_trace.py`

Initial hook placement:

- `reviewer-fast`;
- `pre-commit`;
- `pre-push`;
- autorun common phase gates.

The checker operates on changed files and changed ranges. It does not scan
every historical artifact for retroactive compliance.

## Claim Boundary

This standard proves only repo-local trace completeness and protected-path
visibility in changed ranges. It does not prove OS-level user attribution,
provider-internal action logs, endpoint telemetry, physical machine identity,
or the absence of external filesystem events.

OS-level attribution requires a separate operator decision and a separate
control surface outside this standard.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control standard. Public-sync is not
authorized by this batch.

rawMemoryReleased=false
