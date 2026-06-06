# CVF Worker Autonomy Dispatch Prompt Standard

Memory class: POINTER_RECORD

Status: canonical dispatch prompt standard for delegated worker autonomy

docType: reference

Date: 2026-06-01

## Purpose

Prevent delegated worker agents from converting routine allowed-scope checks,
documentation fixes, and gate remediation into repeated operator confirmation
questions.

This standard gives orchestrators a reusable prompt block to send with a work
order and gives work-order authors a required autonomy clause to include before
dispatch.

## Scope

This applies to delegated CVF work orders, roadmap-derived worker packets,
completion remediation, documentation-only source analysis, and governed
closure batches where the worker has an explicit Allowed scope.

It does not authorize scope expansion, runtime edits outside ownership, live
proof, public-sync, secrets/quota use, destructive action, or claim-boundary
changes.

## Worker Autonomy Prompt

Orchestrators must attach this block to worker prompts for READY/DISPATCHED
governed work orders:

```text
Worker Autonomy Rule:

Do not ask the operator before performing non-destructive actions inside the
work order's Allowed scope.

Proceed autonomously with:
- reading files named by the work order;
- running git status, git diff, git rev-parse;
- running manifest/hash checks;
- running markdown, corpus, work-order, autorun, and closure gates;
- fixing documentation format defects inside Allowed scope;
- adding missing required evidence blocks;
- rerunning failed gates after allowed-scope remediation.

You must stop and ask only if the next action would:
- edit runtime/source code outside Allowed scope;
- edit legacy source under .private_reference/legacy;
- run live/provider/API proof;
- use secrets, quota, or paid external services;
- public-sync, push, or publish;
- change claim boundary, risk level, or release a HOLD prerequisite;
- touch forbidden paths;
- perform destructive or irreversible actions.

If a machine gate fails inside Allowed scope, repair it and rerun. Do not ask
whether to fix routine gate failures.
```

## Work Order Requirement

Every new or amended work order in `READY`, `DISPATCHED`, `APPROVED`, or
equivalent execution status must include a `## Worker Autonomy / No-Question
Rule` section or equivalent literal heading.

The exact marker `Worker Autonomy / No-Question Rule` is machine-checked by
`governance/compat/check_work_order_dispatch_quality.py`.

The section must state:

- non-destructive read/check/gate actions inside Allowed scope proceed without
  operator confirmation;
- allowed-scope documentation/gate remediation must be fixed and rerun;
- escalation is reserved for scope expansion, forbidden paths, live proof,
  public-sync, secrets/quota, destructive action, risk changes, or claim
  boundary changes.

## Orchestrator Authoring Hygiene

Work-order authors must write autonomy clauses so machine gates can distinguish
mandatory allowed-scope remediation from operator-preference questions.

Use this pattern in work orders:

```text
Allowed-scope markdown, registry, classification, reconciliation, and
dispatch-quality failures are mandatory remediation. Escalation is reserved
only for scope expansion, forbidden paths, live/provider proof, secrets/quota,
public-sync, commit/push, destructive action, risk changes, or claim-boundary
changes.
```

Avoid preference phrasing near gate/remediation language in dispatched work
orders. In particular, do not place terms such as `operator checkpoint`,
`operator approval`, `ask operator`, `should I`, or `may I` within the same
paragraph as allowed-scope gate remediation instructions.

If an `Operator Checkpoint` section is required by a structural template, keep
it factual: who selected the scope, what source count or boundary was chosen,
and what task is next. Do not include allowed-scope remediation wording in that
section.

## Corpus Scan Dispatch Requirement

When a work order dispatches corpus scanning, classification, absorption,
search/filter readiness, or "not found" evidence, the worker prompt must say
where the scan output becomes machine-readable downstream input.

Minimum required routing language:

```text
If findings exist, record them in the corpus scan registry and finding packet.
Deferred or blocked findings must include F2G-compatible defectClass,
learningLane, nextAction, and f2gRef, roadmapRef, or workOrderRef evidence.
The scan report is not final if findings exist only as prose.
```

This keeps scan output available to the Learning Loop, roadmap backlog, and
future work-order source verification.

## Commit Mode And Base-Anchor Requirement

Orchestrators must state the commit mode in every delegated worker prompt:

```text
Commit mode: WORKER_MAY_COMMIT | WORKER_MUST_NOT_COMMIT

Capture executionBaseHead with git rev-parse --short HEAD immediately before
material edits. Do not reuse a stale dispatchBaseHead as current worker proof.

If commit mode is WORKER_MUST_NOT_COMMIT:
- run working-tree-aware component gates;
- repair allowed-scope defects and rerun those component gates;
- record actual git status --short;
- return COMPLETE_PENDING_REVIEW;
- return a worker handoff/evaluation artifact, not a reviewer completion review;
- do not claim autorun pre-closure PASS.

Reviewer / committer owns the later commit and non-empty committed-range
pre-closure gate. Reviewer / committer also owns the completion review unless
the orchestrator explicitly changes role and commit mode before dispatch.
```

Anchor vocabulary:

| Anchor | Meaning |
| --- | --- |
| `dispatchBaseHead` | orchestrator audit anchor before dispatch |
| `executionBaseHead` | worker anchor captured immediately before edits |
| `closureBaseHead` | reviewer / committer anchor for committed-range closure |

This prevents a no-commit worker from being trapped between two contradictory
instructions: leave pending artifacts for review, but prove committed closure
before handoff.

## Enforcement / Verification

Machine enforcement:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
```

The guard hard-fails ready/dispatch work orders missing the autonomy section.
Existing operator-facing chat cannot be fully machine-checked unless it is
recorded in an artifact, so the prompt block remains mandatory at dispatch.

## Related Artifacts

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- `governance/compat/check_work_order_dispatch_quality.py`

## Claim Boundary

This standard authorizes routine non-destructive execution within an already
approved Allowed scope. It does not authorize new work, new runtime behavior,
public export, live/provider proof, or autonomous mutation.
