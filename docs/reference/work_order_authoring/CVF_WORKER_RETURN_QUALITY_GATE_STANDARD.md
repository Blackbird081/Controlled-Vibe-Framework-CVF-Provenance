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

## Checker-Source Authoring Checklist

Before writing the first line of a no-commit worker return, read
`governance/compat/check_worker_return_quality_gate.py` and use the checker as
the literal source for packet shape. This standard intentionally mirrors the
checker constants below so workers do not learn these requirements by repeated
gate failure.

### Required Headings

The checker `REQUIRED_HEADINGS` tuple currently requires each heading below as
an exact physical-line heading:

- `## Purpose`
- `## Scope / Methodology`
- `## Findings / Position`
- `## Risk / Corrective Action`
- `## Checker Source Read-Ahead Block`
- `## Agent Operation Trace Block`
- `## Delta Execution Claim Boundary Control Block`
- `## Public Export Disposition`
- `## External Knowledge Intake Routing`
- `## Rescan Intelligence Hardening`
- `## Corpus Completeness And Report Integrity`
- `## Finding-To-Governance Learning Disposition`
- `## Epistemic Process Block`
- `## Claim Boundary`
- `## git status --short`
- `## Changed Files`
- `## Command Evidence`
- `## No-Commit Statement`

### Raw Placeholder Scan

The checker `PLACEHOLDER_MARKERS` scan is full-document raw text. The literal
tokens below must not appear anywhere in a worker return, including prose,
quoted examples, code spans, `literalTokensReviewed`, risk notes, or repair
history:

- `FILL_ME`
- `WORKER_MUST_CAPTURE_AT_START`

If a worker needs to discuss the class of defect, say "unresolved scaffold
placeholder token" instead of spelling the token inside the worker-return
packet.

### Required Field Labels

The `## Checker Source Read-Ahead Block` must include:

- `applicableCheckersRead`
- `literalTokensReviewed`
- `gateRunPurpose`
- `claimBoundary`

The `## Agent Operation Trace Block` must include:

- `Actor`
- `Provider or surface`
- `Session or invocation`
- `Working directory`
- `Command or tool surface`
- `Target paths`
- `Allowed scope source`
- `Before status evidence`
- `After status evidence`
- `Diff evidence`
- `Approval boundary`
- `Claim boundary`
- `Agent type`
- `Invocation ID`
- `Expected manifest`
- `Actual changed set`
- `Manifest delta`
- `Deletion or rename disposition`

The `## Delta Execution Claim Boundary Control Block` must include:

- `claimScope`
- `claimDisposition`
- `receiptEvidence`
- `actionEvidence`
- `invocationBoundary`
- `interceptionBoundary`
- `claimLanguage`
- `forbiddenExpansion`

### Canonical Tokens

For `## External Knowledge Intake Routing`, the `Input type` row must use this
canonical value exactly when the packet is shaped for operator-provided
external comparison, critique, or recommendation:

`operator-provided external comparison, critique, or recommendation`

For Delta evidence, use one receipt token and one action token accepted by the
checker:

- `CLAIM_REJECTED_NO_RECEIPT`
- `CVF_RECEIPT_PRESENT`
- `CLAIM_REJECTED_NO_ACTION`
- `ACTION_EVIDENCE_PRESENT`

For public export disposition, use exactly one allowed disposition token:

- `DEFERRED_PRIVATE_ONLY`
- `EXPORTED`
- `BLOCKED_MISSING_PUBLIC_ARTIFACTS`

The no-commit statement must include:

`WORKER_MUST_NOT_COMMIT honored`

### Command Evidence Range Discipline

Command evidence must use real base/head anchors captured for the tranche. Do
not record a placeholder range where both base and head are `HEAD`; use the
captured `executionBaseHead` and current `HEAD`, for example:

`python governance/compat/run_worker_return_fast_gate.py --pytest-target <test path>`

`python governance/compat/check_worker_return_quality_gate.py --base <executionBaseHead> --head HEAD --enforce`

The purpose of the gate run is confirmation/evidence after reading checker
source, not first discovery of required literal tokens.

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
| Session or invocation | WOAS-R4 worker-return quality gate and WOAS-R6 standard-checklist parity hardening, 2026-07-01 |
| Working directory | repository root |
| Command or tool surface | apply_patch, focused tests, governance gates |
| Target paths | this standard; worker-return quality checker parity tests; WOAS-R6 completion review |
| Allowed scope source | operator instruction to process the WOAS-R5 worker-return lessons by adding a worker authoring checklist and reducing repeated gate-discovery loops |
| Before status evidence | WOAS-R5 review identified repeated worker-return failures caused by hidden checker constants and literal-token traps already covered by ADIF entries |
| After status evidence | focused parity tests and pre-implementation autorun pass before material commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | structural worker-return authoring checklist and checker-standard parity only |
| Claim boundary | no runtime/provider/public/source-import/MCP/model-router claim |
| Agent type | reviewer/closer |
| Invocation ID | `woas-r6-worker-return-standard-checklist-parity-2026-07-01` |
| Expected manifest | reference standard; parity test; completion review |
| Actual changed set | `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md`; `governance/compat/test_check_worker_return_quality_gate.py`; `docs/reviews/CVF_WOAS_R6_WORKER_RETURN_STANDARD_CHECKLIST_PARITY_COMPLETION_2026-07-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename planned |
