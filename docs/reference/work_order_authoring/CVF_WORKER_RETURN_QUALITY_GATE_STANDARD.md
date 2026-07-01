# CVF Worker Return Quality Gate Standard

Memory class: governed-reference-standard
Status: ACTIVE_REFERENCE
Date: 2026-07-01

EPISTEMIC_PROCESS_NA_WITH_REASON: this reference standard defines a structural
quality gate and does not compare implementation evidence.

## Purpose

Define the minimum review-ready machine shape for changed no-commit worker
return packets. The gate catches unresolved scaffold placeholders, missing
trace/read-ahead fields, weak Delta evidence tokens, non-canonical external
input wording, and empty command evidence before reviewer acceptance.

## Applies To

Applies to changed Markdown files under `docs/reviews/` that self-declare as a
worker-return artifact or combine `Status: COMPLETE_PENDING_REVIEW` or
`Status: BLOCKED_WITH_REASON` with a work-order pointer.

Completion reviews, rebuttal/classification packets, baselines, work orders,
roadmaps, archived reviews, and reference standards are out of scope.

## Required Worker-Return Shape

Eligible worker-return packets must include:

- `Self-declared worker-return artifact: yes`
- `Responds to work order:`
- `dispatchWorkOrder:`
- `executionBaseHead:`
- Checker Source Read-Ahead Block section
- Agent Operation Trace Block section
- Delta Execution Claim Boundary Control Block section
- Public Export Disposition section
- External Knowledge Intake Routing section
- Rescan Intelligence Hardening section
- Corpus Completeness And Report Integrity section
- Finding-To-Governance Learning Disposition section
- Epistemic Process Block section
- git status section
- Changed Files section
- Command Evidence section
- No-Commit Statement section

The packet must not retain scaffold placeholders such as `FILL_ME` or
`WORKER_MUST_CAPTURE_AT_START`.

## Claim Boundary

This standard defines a structural quality gate only. It does not prove worker
implementation correctness, source absorption completeness, runtime/provider
behavior, public-sync readiness, MCP/CLI adapter behavior, model-router work,
action authority, automatic invocation, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance-control reference standard; no public-sync artifact
is created by this tranche.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | worker-return quality gate standard |
| claimDisposition | CLAIM_REJECTED: this standard defines structural packet checks only |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local checker/helper invocation only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control |
| claimLanguage | structural worker-return quality guidance only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router behavior without fresh source-verified authorization |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | WOAS-R4 worker-return quality gate, 2026-07-01 |
| Working directory | repository root |
| Command or tool surface | apply_patch, focused tests, governance gates |
| Target paths | this standard; worker-return quality checker; focused tests; fast-gate and hook catalog wiring |
| Allowed scope source | operator instruction to reduce worker-return latency and increase output quality after WOAS-R3 reviewer repairs |
| Before status evidence | WOAS-R3 closed with reviewer repairs to worker-return skeleton and closure package |
| After status evidence | material files ready for verification before commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | structural worker-return quality gate only |
| Claim boundary | no runtime/provider/public/source-import/MCP/model-router claim |
| Agent type | reviewer/closer |
| Invocation ID | `woas-r4-worker-return-quality-gate-2026-07-01` |
| Expected manifest | reference standard; checker; tests; fast gate and hook/autorun catalogs; completion review |
| Actual changed set | to be verified with `git diff --name-status` before material commit |
| Manifest delta | TO_VERIFY_BEFORE_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename planned |
