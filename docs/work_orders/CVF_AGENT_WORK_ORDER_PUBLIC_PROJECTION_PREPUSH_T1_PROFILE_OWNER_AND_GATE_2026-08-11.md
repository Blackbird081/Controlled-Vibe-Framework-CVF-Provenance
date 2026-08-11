# CVF Agent Work Order - Public Projection Pre-Push T1 Profile Owner And Gate

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-08-11

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1

dispatchBaseHead: `5a25a3328bcc5016eac41c1fe712989447bbe791`

executionBaseHead: captured after authority and session-sync commits.

closureBaseHead: same as executionBaseHead because worker must not commit.

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Task ID: PUBLIC-PROJECTION-PREPUSH-T1

Role: implementation worker

Objective: implement the provenance-owned public-projection pre-push profile
defined by the paired GC-018 baseline, with fail-closed policy and tests.

Allowed tools: local file reads, apply_patch, Git read-only inspection, Python,
pytest, PowerShell focused projection proof, and governance gates.

Forbidden tools/actions: commit, push, deploy, browser/provider/store, secrets,
network install, public-clone mutation, production, or public `main`.

Expected outputs: exact four owner paths plus one worker return.

Terminal status: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Satisfy the accepted T0 `BLOCKED_NO_OWNER` reopen predicate and provide a
public-projection-aware gate that preserves private gate authority while
evaluating only public-owned risks against an explicit public root.

## Scope / Target / Owner Boundary

Worker owns exactly:

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`

Reviewer/closer owns acceptance and commits. Session-sync steward owns later
continuity changes. Public clone remains read-only evidence.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | delegated orchestrator/reviewer authority plus `next` | ACCEPT |
| T0 completion | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_COMPLETION_2026-08-06.md` | ACCEPT |
| T0 audit | `docs/audits/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_2026-08-06.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_2026-08-11.md` | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T0 is blocked for no stable owner | VALUE_SET | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_COMPLETION_2026-08-06.md` | Findings / Position | `Decision` | T0 completion decision | ACCEPT |
| reopen requires owner, taxonomy/policy, and fresh four-defect confirmation | VALUE_SET | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_COMPLETION_2026-08-06.md` | Findings / Position | `concrete reopen condition` | T0 completion decision | ACCEPT |
| generic pre-push has public/private ownership mismatch | BEHAVIOR | `docs/audits/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_2026-08-06.md` | Findings 1-4 | `PRE_PUSH_CHECKS` | generic hook catalog | ACCEPT |
| public projection selection already has an owner | EXISTS | `scripts/cvf-public-sync.ps1` | allowlist and policy loading | `Get-AllowedFiles` | public projection script | ACCEPT |
| current public candidate is exact 41 paths | VALUE_SET | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_COMPLETION_2026-08-11.md` | Verification | `Public scope` | Amendment 2 reviewer closure | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch envelope, source verification columns, protected paths, operation trace, bounded claim fields, public disposition |
| gateRunPurpose | confirm source-backed work-order shape before dispatch; not first discovery |
| claimBoundary | packet validation only; no implementation or push claim |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Dispatcher | orchestrator | committed authority only |
| Worker | delegated implementation worker | exact five-path no-commit implementation |
| Reviewer/closer | independent reviewer | semantic review, tests, material commit |
| Session-sync steward | orchestrator | separate continuity commit |

## Intake Role Routing Decision

route: MULTI_AGENT_MULTI_ROLE

selected role route: MULTI_AGENT_MULTI_ROLE

implementation owner: delegated worker

review/commit owner: independent reviewer/closer

intake summary: implement the operator-nominated owner and public-specific gate required by accepted T0 evidence.

risk sensitivity: HIGH because a false pass could authorize public push.

scope classification: BOUNDED_GOVERNANCE_CONTROL_IMPLEMENTATION.

escalation condition: public mutation, generic-gate weakening, secrets/network, ambiguous inherited debt, or any path beyond the exact manifest.

## Worker Autonomy / No-Question Rule

Repair any failure inside the exact owned paths and rerun. Return only for a
scope conflict, missing authority, required public mutation, secret/network
need, or irreparable gate failure outside scope.

## Current Runtime Freshness Verification

At dispatch, Core is clean at `5a25a3328`; public clone is clean on
`lpci1-ref-staging@021f8b852`, remote is the public CVF repository, and the
remote staging branch does not yet exist. Re-verify read-only at execution.

## Required First Reads

Read startup surfaces, guard orientation, paired GC-018, this work order, T0
audit/completion, the generic pre-push catalog, projection script/policy, and
the four target checker sources before editing.

## Pre-Flight Checks

Require Core clean at exact executionBaseHead. Require public clone clean at
exact commit `021f8b852`, branch `lpci1-ref-staging`, correct remote, and zero
staging. Run the pre-implementation autorun gate before material edits.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Public projection pre-push gate implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Worker must rerun the exact resolver query and record the result.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one new isolated public-projection
runner, its policy registry, focused tests, and the companion standard. Do not
change generic checkers, hook catalogs, or existing guard semantics.

Protected paths:

- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`

Operator authorization: delegated decision authority and `next` after the
pre-push blocker was reported.

Rollback boundary: revert exactly the four implementation owner paths and
worker return if rejected; do not revert candidate commits `492e11eab`,
`021f8b852`, or session-sync `5a25a3328`.

## Large-Scope Change Authorization

AUTHORIZED_EXACT_INHERITED_PUBLIC_RANGE for read-only evaluation of the exact
41-path range `2103a38fda01ee827e9fc6c3be38a824fa5d54ad..021f8b852afc245a6383177dd69bf56caf488b02`.
No public clone mutation is authorized.

## Execution Instructions

Implement the baseline literally. The CLI must require explicit `--public-root`,
`--base`, `--head`, and policy path or safe default. Resolve and contain the
root before Git commands. Never inspect secrets. Use subprocess argument lists,
timeouts, captured output, stable JSON, and exit codes. Reject an unexpected
remote, branch, dirty/staged tree, wrong HEAD, empty range, manifest drift,
unknown classification, or missing command.

The policy must identify the Public Projection Release Steward, classify each
included control, pin inherited debt at the base, declare gate/report behavior,
and list the exact candidate manifest. A report-only result is allowed only for
an exact unchanged inherited finding; any new, removed-without-explanation, or
worsened finding fails.

## Write Ownership

Exactly the five paths in Scope. No deletion or rename. No generated aggregate,
session, public clone, hook catalog, or existing checker edits.

## Execution Plan

1. Reconfirm source, path absence, bases, remotes, and ADIF.
2. Write the standard and policy schema/data.
3. Implement the runner with deterministic JSON and human output.
4. Add positive and fail-closed tests using temporary Git fixtures; never use
   the real public clone as a mutable test fixture.
5. Run focused tests, help, syntax/type checks, the runner read-only against the
   real candidate, worker-return fast gate, and final status evidence.
6. Return without commit.

## Work-Order Fulfillment Manifest

Expected changed set is exactly four implementation paths plus the worker
return. Manifest delta must be `MATCH`.

## Evidence Requirements

Record command, working directory, result, exit code, relevant safe output,
exact manifest, policy hash, current Core/public Git state, and negative tests.
Do not record credentials, headers, tokens, cookies, or Netlify configuration
values.

## Verification Commands

- `python -m pytest governance/compat/test_run_public_projection_pre_push_gate.py -q`
- `python governance/compat/run_public_projection_pre_push_gate.py --help`
- exact runner invocation against the read-only public candidate using the
  committed policy, base, and head required by the baseline
- `python governance/compat/run_worker_return_fast_gate.py`
- `git diff --check`

## Acceptance Criteria

- AC-01: T0 owner, taxonomy owner, and gate/report owner are explicit.
- AC-02: policy and runner deterministically cover the exact 41-path candidate.
- AC-03: all four T0 public defect families are freshly recomputed.
- AC-04: inherited debt reports only when exactly pinned; regression fails.
- AC-05: wrong root/remote/branch/head, dirty state, manifest drift, unknown
  classification, missing command, timeout, and command failure fail closed.
- AC-06: generic pre-push and public clone remain unchanged.
- AC-07: focused tests and all required gates pass.
- AC-08: no push, deploy, secret, provider, or production action occurs.

## Review Gate

Independent reviewer must inspect all code and policy, rerun negative tests and
the real-candidate read-only profile, confirm the four-defect classification,
and run reviewer-fast plus committed-range pre-closure before acceptance.

## Closure Checklist

No open acceptance item; exact manifest; all tests/gates PASS; no public
mutation; worker did not commit; reviewer owns material commit; session sync is
separate; push remains a later tranche.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any required public edit, generic-gate
weakening, missing stable owner, secret/network need, ambiguous inherited debt,
or failure outside the exact owned scope.

## Operator Checkpoint

No checkpoint inside owned local implementation. Push and Netlify deployment
remain separate external-action checkpoints after accepted closure.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | exact committed executionBaseHead |
| changedSetScope(phase) | exact five worker-owned paths |
| traceScope(phase, actor) | local gate implementation and proof only |
| commitOwner(phase) | reviewer/closer |
| crossBatchIsolation | public candidate and unrelated Core remain unchanged |
| nextMoveSurfaces | reviewer/session steward owned |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_COMPLETION_2026-08-11.md`

reviewerOwnedClosurePaths: exact worker paths, optional completion review if
needed, then separate session sync.

## Foundation Storage Layout Block

N/A with reason: this tranche adds governance control-plane files, not
foundation runtime storage.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | N/A with reason: no external knowledge intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T1 standard, policy, runner, and tests |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external authority admitted |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required section names include Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
External Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus
Completeness And Report Integrity, Epistemic Process Block, Machine Closure
Package, Public Export Disposition, Claim Boundary, git status --short, Changed
Files, Worker Experience Retrospective, Command Evidence, No-Commit Statement,
and Terminal Disposition.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | local Python CLI and policy | read-only public-root evaluation | JSON receipt and exit code | subprocess/Git boundary | BUILD |
| EXTERNAL_AGENT_CLI_MCP | CLI may be invoked by an external worker only under the same explicit arguments | no MCP/provider authority | identical local receipt | CLI only; no MCP adapter | CONTRACT_ONLY |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | private Core plus read-only public clone |
| Session or invocation | `public-projection-prepush-t1-dispatch-20260811` |
| Working directory | private Core root |
| Command or tool surface | local reads, Git inspection, ADIF resolver, apply_patch, governance gates |
| Target paths | paired baseline and work order |
| Allowed scope source | operator `next`, T0 accepted completion, current session next move |
| Before status evidence | Core clean at `5a25a3328`; public clean at `021f8b852` |
| After status evidence | authority pending commit; implementation/public untouched |
| Diff evidence | exact two-path dispatch manifest before commit |
| Approval boundary | local implementation dispatch only |
| Claim boundary | no implementation, push, deploy, provider/store, secret, or production action |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `public-projection-prepush-t1-dispatch-20260811` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: two new authority files only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a narrow provenance-owned profile can separate
private-only checks from public-owned risks and gate only new/worsened public
defects without waiving inherited debt.

Evidence Comparison Requirement: compare the prediction with fixtures and the
real exact public candidate.

Contradiction Handling Requirement: any ambiguity or false pass requires a
Contradiction Or Gap Disposition and blocked return.

Claim Update Requirement: confirm, revise, narrow, or invalidate the profile
claim from evidence.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_CURRENT_SOURCE

priorVerificationArtifact: T0 audit and completion are predecessor authority,
not substituted execution proof.

priorVerificationAnchor: public base `2103a38f` and candidate `021f8b852`.

freshRecomputeRequired: yes, all four public-relevant defects and Git facts.

unicodePathHandling: use resolved literal paths and UTF-8-safe readers.

extractedTextAuthority: repository bytes and command results only.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local public-projection gate implementation and read-only proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: worker has not executed yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source-backed dispatch packet |
| invocationBoundary | exact local owner paths; public clone read-only |
| interceptionBoundary | no IDE, provider, browser, network, or remote mutation claim |
| claimLanguage | ready for no-commit implementation |
| forbiddenExpansion | generic gate weakening, public mutation, push, deploy, secrets, provider/store, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order authorizes local provenance gate implementation only.

## Claim Boundary

This work order does not authorize push or Netlify deployment. Successful
worker return still requires independent review, material commit, and a later
explicit external-action tranche.
