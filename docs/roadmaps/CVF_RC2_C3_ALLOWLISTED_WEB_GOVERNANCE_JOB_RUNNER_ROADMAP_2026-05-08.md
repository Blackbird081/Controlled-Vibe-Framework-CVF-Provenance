<!-- Memory class: SUMMARY_RECORD -->
# CVF RC2-C3 Allowlisted Web Governance Job Runner Roadmap

> Authorization: `docs/baselines/CVF_GC018_RC2_C3_ALLOWLISTED_WEB_GOVERNANCE_JOB_RUNNER_AUTHORIZATION_2026-05-08.md`
> Track: RC2 Foundation / C — Governed Web Operations Enablement
> Status: CLOSED DELIVERED

## Purpose

Implement a minimal allowlisted runner for non-destructive Web governance jobs,
grounded in C0 threat model, C1 RBAC spec, and C2 persistence ADR.

## Checkpoints

| CP | Work |
|---|---|
| CP0 | GC-018 authorization and C3 scope lock |
| CP1 | Add typed job definitions and permission check |
| CP2 | Add append-only JSONL audit events |
| CP3 | Add fixed-argv command runner and timeout handling |
| CP4 | Add API route for submit/list |
| CP5 | Add failure-mode tests |
| CP6 | Publish closure and handoff sync |

## Exit Criteria

- No free-form command execution.
- Unknown job/role/provider fails closed.
- Viewer/reviewer triggers are blocked and audited.
- Anonymous local mode can only run read-only diagnostics.
- Output is redacted before persistence/response.
- Full live release gate is not runnable.
- Targeted tests pass.

## Closure Result

RC2-C3 closed on 2026-05-08.

Closure:
`docs/reviews/CVF_RC2_C3_ALLOWLISTED_WEB_GOVERNANCE_JOB_RUNNER_CLOSURE_DECISION_2026-05-08.md`
