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
