# CVF Agent Work Order - GFC-T3 Roadmap State Hygiene Remediation For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-18

Owner: Claude dispatcher; Claude worker; Codex reviewer/closer

rawMemoryReleased: false

dispatchBaseHead: ecd74bbe

executionBaseHead: ecd74bbe

closureBaseHead: ecd74bbe

## Dispatch Prompt Envelope

Role: worker/implementer. Codex (or operator-designated reviewer) is
reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`

Base: executionBaseHead `ecd74bbe` (captured with `git rev-parse --short HEAD`
at dispatch time; re-confirm at worker start).

Current-time notes: GFC-T3 is roadmap-status remediation only. The dispatch
authoring batch (this work order, the GC-018, and the GFC roadmap update)
contains no implementation, runtime, or registry change. The P5C row was
re-verified by direct reading before this dispatch and its closure is now
confirmed complete and bounded rather than undetermined; it is included as
the eighth row.

Do-not-misread notes: do not edit any roadmap field other than the
top-of-file `Status:` line and one additive closure-note section per roadmap.
Do not touch tranche tables, scope, acceptance criteria, or work plans inside
the eight roadmaps. Do not edit `CVF_SESSION_MEMORY.md`, `CVF_SESSION/**`,
`AGENT_HANDOFF_V19_2026-06-15.md`, runtime/source/test code, registries, or
public-sync. If any cited closure-evidence artifact (commit hash, completion
review, checker/source file) cannot be found on disk, return
`BLOCKED_WITH_REASON` for that specific roadmap row instead of guessing a
substitute citation.

Required first actions: read this work order, the GFC-T3 GC-018, the GFC
roadmap's `## GFC-T3 Dispatch Record` section, the accepted GFC-T1 decision
packet's `## Roadmap State Hygiene Matrix`, and the post-closure state drift
finding; then run the pre-flight checks in Section 6 below.

Return contract: return `COMPLETE_PENDING_REVIEW` with worker packet path,
worker return path, executionBaseHead, `git status --short`, gates run, exact
changed-path list, and HEAD-unchanged evidence; or return
`BLOCKED_WITH_REASON` naming the specific roadmap row and the missing/changed
source artifact.

## Purpose

Claude must remediate seven confirmed-stale roadmap status rows from the
accepted GFC-T1 matrix plus the re-verified P5C row, for eight total rows, by
updating each roadmap's own top-of-file `Status:` line to a closed-equivalent
value with a pointer to closure evidence that already exists on disk, and by
reconciling the AHB roadmap's internal self-reference mismatch.

## Scope / Target / Owner Boundary

Target: the top-of-file `Status:` line of the eight roadmap files named in
Section 7 (Write Ownership), plus the AHB roadmap's own `Machine Closure
Package` "Roadmap state" row.

Owner boundary: Claude authors the worker packet and worker return under
`WORKER_MUST_NOT_COMMIT`. Codex (or operator-designated reviewer) reviews
actual files, commits accepted material, authors closure, and performs
session sync if needed.

## Intake Role Routing Decision

intake summary: Claude (acting as dispatcher per operator instruction)
dispatches GFC-T3 to a Claude worker as a bounded roadmap-status remediation
packet.

scope class: governance roadmap-status hygiene edit; no runtime, provider/live,
public-sync, registry mutation, workspace runtime, product code, production
readiness, or public readiness.

risk sensitivity: R1; low blast radius (status-line text only), high
context-scan-ambiguity value if remediated correctly.

selected role route: `MULTI_AGENT_MULTI_ROLE`

role separation basis: Claude performs source-backed remediation authoring
without commit. The reviewer performs review, accepted material commit,
closure, and session sync.

escalation condition: stop and return `BLOCKED_WITH_REASON` for a specific
row only if its cited closure-evidence artifact is missing, moved, or
contradicts the GFC-T1 matrix; otherwise continue with the remaining rows.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher (Claude, this batch); worker (Claude, no-commit); reviewer/closer (Codex or operator-designated) |
| phase | DISPATCH_AUTHORING now; EXECUTION by Claude worker; CLOSURE by reviewer; SESSION_SYNC by reviewer if needed |
| baseHeadFor(phase) | `dispatchBaseHead=ecd74bbe`; `executionBaseHead=ecd74bbe`; `closureBaseHead=ecd74bbe` until reviewer review starts |
| changedSetScope(phase) | dispatch changed set is GFC roadmap update, this GC-018, and this work order; worker changed set is the worker packet, worker return, and the eight roadmap status-line edits; closure changed set belongs to the reviewer |
| traceScope(phase, actor) | worker trace covers the worker-owned packet/return and the eight roadmap edits; reviewer trace covers closure/session-sync ranges |
| commitOwner(phase) | reviewer for dispatch acceptance, closure, and session sync; no execution commit by the worker |
| crossBatchIsolation | one clean worktree per batch; worker must stop if unrelated dirty files appear |
| nextMoveSurfaces | reviewer owns any later next-move surface updates |
| Closer designation | Codex (or operator-designated reviewer) |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_COMPLETION_2026-06-18.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_COMPLETION_2026-06-18.md`
- `docs/roadmaps/CVF_GOVERNANCE_FOUNDATION_CONSOLIDATION_ROADMAP_2026-06-18.md`
- `docs/baselines/CVF_GC018_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_2026-06-18.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`

The reviewer may perform narrow reviewer repairs to worker-owned artifacts
only if needed for gate compliance and must record the reviewer delta if the
worker's substantive status-line choice changes.

## Core Guard Self-Protection Authorization

The worker is not authorized to edit protected session, handoff, guard,
runtime, or reference-core files.

Protected paths mentioned in this work order are read-only authority surfaces:

- `AGENT_HANDOFF_V19_2026-06-15.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/**`

The reviewer may update protected session/front-door paths only in a later
session-sync range if accepted GFC-T3 closure changes next allowed move.

Authorized guard-maintenance scope: none. This work order does not authorize
guard source edits or protected-path edits by the worker.

Operator authorization: 2026-06-18 operator confirmed GFC-T3 as the next
roadmap and asked for an audit and a work order for an agent to execute.

Rollback boundary: if the worker packet is rejected, revert only the eight
roadmap status-line/closure-note edits and the GFC-T3 worker outputs from the
accepted-material review range. Do not revert prior GFC-T1, PRFC, AHB, CCLV,
FPRC, P5C, or session-sync commits.

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | N/A with reason: this work order does not design, build, or modify an agent workspace |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | N/A with reason: no workspace artifact is created or changed |
| Storage class | N/A with reason: no workspace storage or state record is changed |
| Handoff fields | governed by the Agent Handoff Contract Control Block above |
| State ownership | N/A with reason: no workspace state change is authorized |
| Guard owner | N/A with reason: no workspace checker change is authorized |
| Build boundary | Workspace runtime queues, workspace state, workspace UI, runtime source, provider proof, public-sync, and registry edits are forbidden |

## Worker Autonomy / No-Question Rule

The worker should repair allowed-scope gate failures (markdown structural
completeness, machine closure package, epistemic process block, finding
disposition formatting) and rerun the failed gate. Do not ask the operator
whether to fix these. Return to the reviewer only if a specific roadmap row's
closure evidence is missing/moved, or the repair would exceed this work
order's scope or touch a forbidden path.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `N/A with reason: GFC-T3 must inspect current
governed roadmap files and their cited closure evidence directly`

priorVerificationAnchor: `N/A with reason: no prior command output is reused`

freshRecomputeRequired: YES

recomputeReason: each roadmap's current `Status:` line and each cited
closure-evidence artifact's existence must be checked against current repo
files at worker-execution time, not against the GFC-T1 audit snapshot, in
case anything changed between dispatch and execution.

unicodePathHandling: use literal repo-relative paths and UTF-8-safe readers.

New governed markdown must use ASCII. Do not introduce non-ASCII punctuation
or decorative symbols.

## Foundation Storage Layout Block

This task uses existing indexed execution folders:

- roadmap under `docs/roadmaps/` (the eight files being remediated, plus the
  GFC roadmap itself, already exist; no new folder is created);
- GC-018 under `docs/baselines/`;
- work order under `docs/work_orders/`;
- worker packet and worker return under `docs/reviews/`.

No new foundation folder is authorized. If the worker finds a reusable
foundation rule that lacks a stable front door or index while remediating
these rows, record it as a finding with a governed disposition; do not create
a new folder.

## 1. Mission

Remediate the seven accepted GFC-T1 roadmap status rows plus the re-verified
P5C row, eight rows total. Success means the
reviewer can review one source-backed worker packet plus eight roadmap diffs
where each `Status:` line now reads a closed-equivalent value citing existing
closure evidence, and the AHB self-reference mismatch is resolved.

## 2. Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-18 instruction confirming GFC-T3 and asking for audit plus work order | ACCEPTED |
| GFC roadmap (dispatch record) | `docs/roadmaps/CVF_GOVERNANCE_FOUNDATION_CONSOLIDATION_ROADMAP_2026-06-18.md` | CLOSED_PASS_BOUNDED |
| GC-018 baseline | `docs/baselines/CVF_GC018_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_2026-06-18.md` | CLOSED_PASS_BOUNDED |
| Accepted GFC-T1 decision packet | `docs/reviews/CVF_GFC_T1_CCLV_FPRC_STATE_HYGIENE_AUDIT_DECISION_PACKET_2026-06-18.md` | ACCEPT |
| Post-closure state drift finding | `docs/reviews/CVF_GFC_T1_POST_CLOSURE_STATE_DRIFT_FINDING_2026-06-18.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |

## Agent Roles

| Role | Actor | Responsibility |
|---|---|---|
| Dispatcher | Claude (this batch) | Author GFC roadmap update, GC-018, and this work order |
| Worker | Claude | Author worker-owned remediation packet and worker return, and edit the eight roadmap status lines, without commit |
| Reviewer / closer | Codex (or operator-designated) | Review actual files, repair within reviewer scope, commit accepted material |
| Operator | Human | Decide any scope expansion, runtime authorization, or unresolved conflict |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | N/A with reason: selected route is `MULTI_AGENT_MULTI_ROLE`, not single-agent execution |
| actor | dispatcher and worker may be the same model identity (Claude) across separate invocations; reviewer is a distinct actor |
| role set | dispatcher (this batch); worker (no-commit); reviewer/closer |
| Role separation ledger | handled by Agent Handoff Contract Control Block |
| Evidence basis independent of memory | governed source verification, worker return, and reviewer review |
| Gate sequence | dispatch gate before worker execution; worker-return fast gate before reviewer acceptance; pre-closure after accepted material commit |
| Self-review boundary | N/A with reason: reviewer reviews worker output; dispatcher does not self-accept |
| escalation condition | N/A with reason: multi-agent route; escalation conditions are defined in Intake Role Routing Decision and Return-To-Orchestrator Conditions |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Worker deliverable | Disposition |
|---|---|---|---|
| Remediate prompt-envelope roadmap status | Section 7 | `Status:` line update + closure note | ACCEPT |
| Remediate session-sync-pack-builder roadmap status | Section 7 | `Status:` line update + closure note | ACCEPT |
| Remediate AHB roadmap self-reference mismatch | Section 7 | `Status:` line update + Machine Closure Package row reconciliation | ACCEPT |
| Remediate Model Gateway C-02 P2 roadmap status | Section 7 | `Status:` line update + closure note | ACCEPT |
| Remediate Model Gateway C-02 P4A roadmap status | Section 7 | `Status:` line update + closure note | ACCEPT |
| Remediate Model Gateway C-02 P5 roadmap status | Section 7 | `Status:` line update + closure note | ACCEPT |
| Remediate Session Continuity Rotation Guard Hardening roadmap status | Section 7 | `Status:` line update + closure note | ACCEPT |
| Remediate Model Gateway C-02 P5C roadmap status | Section 7 | `Status:` line update + closure note | ACCEPT |
| No runtime/provider/public/registry/workspace runtime scope | Dispatch envelope; Scope; Claim Boundary | worker return forbidden-path evidence | ACCEPT |
| Worker no-commit split | Dispatch envelope; Reviewer Closure Conversion | worker return HEAD unchanged evidence | ACCEPT |

## 3. Required First Reads

Claude must read:

- this work order;
- `docs/baselines/CVF_GC018_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_2026-06-18.md`;
- `docs/roadmaps/CVF_GOVERNANCE_FOUNDATION_CONSOLIDATION_ROADMAP_2026-06-18.md` `## GFC-T3 Dispatch Record` section;
- `docs/reviews/CVF_GFC_T1_CCLV_FPRC_STATE_HYGIENE_AUDIT_DECISION_PACKET_2026-06-18.md` `## Roadmap State Hygiene Matrix` section;
- `docs/reviews/CVF_GFC_T1_POST_CLOSURE_STATE_DRIFT_FINDING_2026-06-18.md`;
- each of the eight roadmap files named in Section 7, in full, before editing
  any of them;
- the closure-evidence artifact cited for each row (completion review,
  commit, or checker/source file) to confirm it still exists before writing
  any new `Status:` line.

## 4. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Eight-row remediation scope is source-backed | `docs/baselines/CVF_GC018_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_2026-06-18.md` | `## Source Verification Block` | row-by-row citations | GFC-T3 GC-018 | ACCEPT |
| P5C is closed, not undetermined | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_COMPLETION_2026-06-15.md`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-bridge-admission-guard.ts` | completion review status line; guard file imported by bridge | `provider-bridge-admission-guard.ts` | P5C roadmap | ACCEPT |
| AHB self-reference mismatch is real and at named lines | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | line 5 vs. line 480 | `## Machine Closure Package` | AHB roadmap | ACCEPT |

If the worker finds a claimed source fact above, or in the GC-018's Source
Verification Block, to be stale at execution time (e.g., a cited commit hash
no longer matches, or a completion review path was moved), return
`BLOCKED_WITH_REASON` for that specific row and cite the corrected source;
continue remediating the remaining rows.

## 5. Write Ownership

Claude may create only:

- `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_PACKET_2026-06-18.md`
- `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_WORKER_RETURN_2026-06-18.md`

Claude may edit only the top-of-file `Status:` line and add one additive
closure-note section in each of:

1. `docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md`
2. `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md`
3. `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` (also reconcile the `Machine Closure Package` "Roadmap state" row)
4. `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md`
5. `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_AND_CONFORMANCE_ROADMAP_2026-06-15.md`
6. `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md`
7. `docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md`
8. `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_ROADMAP_2026-06-15.md`

Claude must not edit:

- any other field, section, tranche table, scope, or acceptance criteria in
  the eight roadmaps above;
- any other roadmap not listed above;
- `CVF_SESSION/**`;
- `AGENT_HANDOFF_V19_2026-06-15.md`;
- runtime/source/test code;
- registry or interlock files;
- public-sync repository;
- workspace runtime queue files;
- provider configuration or credential files.

## 6. Pre-Flight Checks

Claude must run before authoring:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md
Test-Path docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md
Test-Path docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md
Test-Path docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md
Test-Path docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_AND_CONFORMANCE_ROADMAP_2026-06-15.md
Test-Path docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md
Test-Path docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md
Test-Path docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5C_BRIDGE_ADMISSION_BOUNDARY_ROADMAP_2026-06-15.md
Test-Path EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-bridge-admission-guard.ts
```

Expected result:

- HEAD equals `ecd74bbe` at worker start unless the reviewer gives a newer
  explicit execution base;
- worktree contains no unrelated dirty files before Claude authoring;
- all eight roadmap files exist;
- the P5C guard source file exists, confirming the closure evidence for row 8.

## 7. Execution Instructions

For each of the eight roadmap rows:

1. Read the current top-of-file `Status:` line.
2. Re-confirm the cited closure-evidence artifact still exists (completion
   review path, commit hash appearing in `CVF_SESSION_MEMORY.md` or git log,
   or checker/source file path).
3. If confirmed, update the `Status:` line to a closed-equivalent value (the
   worker chooses the exact suffix wording, consistent with this roadmap's
   own existing vocabulary, e.g. `_CLOSED_PASS_BOUNDED` or
   `_CLOSED_PASS_BOUNDED_REMEDIATED_GFC_T3`) and add a short closure-note
   section (or a one-paragraph addition near the top) citing the
   closure-evidence artifact and commit hash.
4. For the AHB roadmap only, also update its own `## Machine Closure Package`
   "Roadmap state" row so its expected-status string matches the corrected
   top-of-file `Status:` line exactly (no new self-reference mismatch).
5. If not confirmed, do not edit that roadmap; record it as
   `BLOCKED_WITH_REASON` in the worker packet and continue with the remaining
   rows.

Claude must create the worker packet with these sections:

1. `## Required First-Read Ledger`
2. `## Pre-Flight Evidence`
3. `## Per-Row Remediation Record` (one entry per of the eight rows: before
   status, after status, cited closure evidence, confirmation method, edit or
   blocked disposition)
4. `## AHB Self-Reference Reconciliation`
5. `## Finding-To-Governance Learning Disposition`
6. `## Claim Boundary`
7. Agent Operation Trace Block section

Claude must not mark any roadmap's substantive tranche/scope content closed;
only the `Status:` line and the additive closure note may change.

## Execution Plan

1. Confirm execution base and worktree status.
2. Read all Required First Reads.
3. Verify the Source Verification Block and the GC-018's Source Verification
   Block from current repo files.
4. For each of the eight rows, confirm closure evidence, then edit the
   `Status:` line and add the closure note, or mark `BLOCKED_WITH_REASON`.
5. Reconcile the AHB roadmap's internal self-reference.
6. Author the worker packet at the worker-owned path.
7. Author the worker return at the worker-owned path.
8. Run the worker-return fast gate and diff hygiene.
9. Return to the reviewer with `COMPLETE_PENDING_REVIEW` or
   `BLOCKED_WITH_REASON`.

## Evidence Requirements

Claude worker return must include:

- executionBaseHead;
- `git status --short` output or explicit empty-output statement;
- changed path list (worker packet, worker return, plus up to eight roadmap
  files);
- command evidence for pre-flight checks;
- worker-return fast gate result;
- `git diff --check` result;
- HEAD unchanged statement;
- any unresolved blocker with source path and section, per row.

## Review Gate

The reviewer must not accept the worker return until:

- changed paths stay inside Write Ownership;
- no forbidden path changed;
- no roadmap's substantive content (tranche table, scope, acceptance
  criteria, work plan) changed beyond the `Status:` line and closure note;
- the AHB roadmap's self-reference is reconciled;
- findings carry governed learning disposition;
- worker-return fast gate is clean or any failure is repaired within reviewer
  scope and rerun.

## Closure Checklist

- [x] Claude worker packet exists.
- [x] Claude worker return exists.
- [x] HEAD unchanged evidence is present.
- [x] No forbidden path is changed.
- [x] Each of the eight rows' `Status:` line is either remediated with cited
  evidence or marked `BLOCKED_WITH_REASON`.
- [x] AHB roadmap self-reference is reconciled.
- [x] Reviewer decision is recorded in accepted-material commit `f68ff8ce` and
  completion review `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_COMPLETION_2026-06-18.md`.

## Return-To-Orchestrator Conditions

Claude returns `COMPLETE_PENDING_REVIEW` if all acceptance criteria pass for
at least the rows that were not blocked.

Claude returns `BLOCKED_WITH_REASON` if a required source is missing for all
eight rows, the worktree isolation fails, or fulfilling the task would require
forbidden-scope edits.

## Operator Checkpoint

No operator checkpoint is required during Claude worker execution unless:

- a majority of the eight rows' closure evidence cannot be confirmed;
- runtime, provider/live, public-sync, registry mutation, or workspace
  runtime work becomes necessary;
- the recommended remediation would rewrite historical closed artifacts in
  bulk beyond the named `Status:` line/closure-note scope;
- the decision changes the claim boundary of this work order.

## 8. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker packet has all required sections. |
| AC2 | Each of the eight rows is either remediated with cited evidence or explicitly `BLOCKED_WITH_REASON`. |
| AC3 | AHB roadmap self-reference mismatch is reconciled. |
| AC4 | Worker return includes HEAD unchanged evidence and changed path list. |
| AC5 | No forbidden paths changed and no commit made by Claude. |
| AC6 | No roadmap's substantive content changed beyond the `Status:` line and closure note. |

## 9. Return Contract

Return `COMPLETE_PENDING_REVIEW` only when:

- both worker-owned files exist;
- no forbidden paths changed;
- HEAD is unchanged from execution base;
- worker return includes command evidence and any gate failures with repairs
  or blockers;
- all findings have governed learning disposition.

Return `BLOCKED_WITH_REASON` if:

- worktree isolation is violated by unrelated dirty files;
- fulfilling the task requires editing forbidden paths or roadmap content
  beyond the authorized `Status:` line/closure note;
- the majority of rows cannot be confirmed and require operator input.

## 10. Verification To Run Before Return

Claude should run:

```powershell
git status --short
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

If a gate fails inside allowed scope, repair and rerun. If a gate fails
outside allowed scope, return `BLOCKED_WITH_REASON` and cite the failing
check.

## 11. Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `ORCHESTRATOR_PACKET_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `ROADMAP_ADDED` |
| Next control action | Claude must remediate the eight stale roadmap status rows using only already-existing closure evidence |
| Worker blame | `N/A_WITH_REASON`: this dispatch assigns a cross-roadmap status-hygiene remediation, not a worker error fix |

## 12. Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance worker dispatch. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 GFC-T3 work order closure update |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, git, CVF governance gates |
| Target paths | GFC roadmap; GFC-T3 GC-018; this work order; GFC-T3 completion review |
| Allowed scope source | Reviewer Closure Conversion in this work order |
| Before status evidence | accepted material commit `f68ff8ce`; clean worktree before closure authoring |
| After status evidence | closure artifacts authored; pending pre-closure gate |
| Diff evidence | `git diff --name-status f68ff8ce..HEAD` |
| Approval boundary | closure update only; no runtime/provider/live/public/registry/workspace runtime claim |
| Claim boundary | no runtime/provider/live/public/registry/workspace runtime claim |
| Agent type | Codex |
| Invocation ID | `gfc-t3-codex-work-order-closure-2026-06-18` |
| Expected manifest | `docs/roadmaps/CVF_GOVERNANCE_FOUNDATION_CONSOLIDATION_ROADMAP_2026-06-18.md`; `docs/baselines/CVF_GC018_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`; `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_COMPLETION_2026-06-18.md` |
| Actual changed set | `docs/roadmaps/CVF_GOVERNANCE_FOUNDATION_CONSOLIDATION_ROADMAP_2026-06-18.md`; `docs/baselines/CVF_GC018_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`; `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_COMPLETION_2026-06-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## GFC-T3 Closure Note (2026-06-18)

GFC-T3 closed bounded at accepted-material commit `f68ff8ce` and closure
review `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_COMPLETION_2026-06-18.md`.
Claude returned `COMPLETE_PENDING_REVIEW`; Codex accepted the worker material,
repaired the worker-reported Rotation Guard D3/D4 stale table cells, and left
runtime/provider/live/public-sync/registry/workspace runtime work parked.

## Current Runtime Freshness Verification

Runtime/source mutation applicability: N/A with reason: GFC-T3 is
roadmap-state hygiene closure only. The accepted material range
`24848d66..f68ff8ce` changes governed roadmap/review documentation and does
not touch runtime/source/test/provider/workspace runtime files.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline | `docs/baselines/CVF_GC018_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_GOVERNANCE_FOUNDATION_CONSOLIDATION_ROADMAP_2026-06-18.md` | `Status: GFC_T1_T3_CLOSED_PASS_BOUNDED_RUNTIME_PARKED` | PASS |
| Accepted material commit | `f68ff8ce` | eight roadmap files plus worker packet and worker return | PASS |
| Worker no-commit evidence | `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_WORKER_RETURN_2026-06-18.md` | HEAD unchanged at `24848d66` | PASS |
| Session continuity | pending separate session-sync range | closure claim does not include session-sync commit yet | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry edit authorized | no registry JSON path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized | no registry Markdown path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof authorized | repo-local governance docs only | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit authorized | no interlock path changed | N/A with reason |
| Provider/live proof | N/A with reason: no provider/live proof authorized | no live/provider command run | N/A with reason |
| Public-sync | N/A with reason: private provenance closure only | `DEFERRED_PRIVATE_ONLY` | N/A with reason |

## Claim Boundary

This work order authorizes only Claude-authored roadmap-status remediation
worker artifacts and the nine named status-line/closure-note edits. It does
not authorize runtime execution, provider/live proof, public-sync, registry
mutation, workspace runtime, product runtime mutation, production readiness,
public readiness, or bulk historical rewrite.
