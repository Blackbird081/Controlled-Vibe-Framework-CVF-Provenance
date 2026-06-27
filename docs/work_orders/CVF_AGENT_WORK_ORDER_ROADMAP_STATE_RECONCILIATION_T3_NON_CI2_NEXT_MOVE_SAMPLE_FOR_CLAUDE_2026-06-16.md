# CVF Agent Work Order - Roadmap State Reconciliation T3 Non-CI2 Next-Move Sample For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Owner / Orchestrator: Codex

Implementer: Claude

Reviewer / closer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 72fa2427

executionBaseHead: f8d468c1

closureBaseHead: f8d468c1

riskCeiling: R1_GOVERNANCE_DOCUMENTATION_ONLY

rawMemoryReleased: false

workerReturnPath:
`docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`

completionReviewPath:
`docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md`

## Dispatch Prompt Envelope

```text
Role: Claude is worker/implementer. Codex is reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: executionBaseHead WORKER_MUST_CAPTURE_AT_START with git rev-parse --short HEAD before edits.
Current-time notes: RSF-T3 is documentation/audit only. Worker execution started at f8d468c1 after dispatch commit 8450707a, prompt/provider-memory hardening commit 93d0eb7f, and session sync f8d468c1. No live/provider/key/public-sync/runtime work is authorized.
Do-not-misread notes: Do not redispatch Model Gateway C-02 P2; C-02 P2 is already closed. Do not open Model Gateway P3. Do not edit session state, active handoff, governance checker source, or runtime files.
Required first actions: read CVF_SESSION_MEMORY.md, CVF_SESSION/ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V19_2026-06-15.md, this work order, the RSF-T3 GC-018, the audit review, the RSF roadmap, the RSF-T2 completion, the C-02 P2 work order, and the C-02 P2 state entry; then capture executionBaseHead and run the pre-flight checks.
Return contract: COMPLETE_PENDING_REVIEW with executionBaseHead, HEAD unchanged, git status --short, git diff --name-status, required gate outputs, source evidence table, and explicit BLOCKED_WITH_REASON if forbidden scope is required.
```

## Purpose

Apply the RSF stale-roadmap freshness pattern to one non-CI2 sample: current
session continuity that points to Model Gateway C-02 P2 even though C-02 P2 is
already closed.

This is a source-backed audit and documentation task. It is not Model Gateway
implementation and it is not permission to redispatch C-02 P2.

## Scope / Target / Owner Boundary

Target: one no-commit worker-return audit for the RSF-T3 non-CI2 stale
next-move sample.

Owner boundary: Claude may create or update only the listed documentation
artifacts in Write Ownership. Codex owns reviewer closure, material commit, and
any session continuity sync.

This work order does not authorize runtime, provider, credential, public-sync,
legacy, session-state, active-handoff, governance-checker, Model Gateway
implementation, or C-02 P2/P3 dispatch work.

## 1. Mission

Independently verify the non-CI2 stale next-move sample from current source
files, document operator-facing behavior, and return a no-commit worker packet
for Codex review.

Success means the worker return states whether the current source evidence
confirms or rejects the suspected stale next-move contradiction and whether a
future machine-check extension is needed.

## 2. Authority Chain

- Operator request: 2026-06-16 request to evaluate Claude actual work, audit,
  choose next roadmap, and issue a work order.
- Actual-work audit:
  `docs/reviews/CVF_CCLV_T2_CLAUDE_ACTUAL_WORK_AUDIT_AND_RSF_T3_SELECTION_2026-06-16.md`.
- Roadmap:
  `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_2026-06-16.md`.
- RSF-T2 completion:
  `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_COMPLETION_2026-06-16.md`.
- Active state registry: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and reconcile
  before implementation.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | source audit, dispatch, reviewer closure |
| Worker | Claude | no-commit documentation/audit worker return |
| Reviewer / closer | Codex | inspect diff, run gates, commit if accepted |
| Operator | Human | scope expansion, runtime, live/provider, public-sync |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | CCLV-T2 actual-work audit found the current continuity points toward a closed non-CI2 target, C-02 P2 |
| Scope classification | R1 governance documentation only |
| Risk sensitivity | Session/roadmap continuity claim; no runtime/provider/secret/public-sync |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Codex orchestrates/reviews/commits; Claude verifies and returns no-commit evidence |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| Role separation basis | Codex selected RSF-T3 from source evidence; Claude independently verifies the sample; Codex reviews closure |
| Escalation condition | Stop for runtime changes, session-state edits, public-sync, provider/live work, broad legacy scan, broad repository scan, or claim expansion |

## 4. Scope

Allowed scope:

- create the worker-return packet named in `workerReturnPath`;
  `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`;
- create the reviewer-owned completion packet named in `completionReviewPath`
  during Codex closure:
  `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md`;
- update this work order status/evidence only after worker-return gates pass;
- update the RSF roadmap RSF-T3 row/evidence only if the worker return supports
  the update:
  `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`;
- run the required local governance and evidence commands.

Forbidden scope:

- runtime Model Gateway implementation;
- redispatching or modifying C-02 P2 implementation artifacts;
- creating Model Gateway P3 work order or GC-018;
- modifying `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, or
  `AGENT_HANDOFF_V19_2026-06-15.md`;
- modifying `governance/compat/*.py` or tests;
- provider calls, credentials, network use, live proof, or public-sync;
- broad legacy scan or broad repository scan;
- committing.

Risk ceiling: R1_GOVERNANCE_DOCUMENTATION_ONLY.

## 5. Required First Reads

Before editing files, read:

| File | Required use |
|---|---|
| `CVF_SESSION_MEMORY.md` | startup front door and current next-move surface |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active handoff and generated aggregate state |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | source entry for generated nextAllowedMove |
| `AGENT_HANDOFF_V19_2026-06-15.md` | current continuity and active handoff |
| `docs/reviews/CVF_CCLV_T2_CLAUDE_ACTUAL_WORK_AUDIT_AND_RSF_T3_SELECTION_2026-06-16.md` | dispatch audit and suspected sample |
| `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md` | governing roadmap and RSF-T3 purpose |
| `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_2026-06-16.md` | authorized scope |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md` | C-02 P2 status evidence |
| `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json` | C-02 P2 state evidence |
| `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_COMPLETION_2026-06-16.md` | RSF-T2 guard boundary |

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_session_mode_consistency.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 72fa2427 --head HEAD
```

Expected results:

- `git rev-parse --short HEAD` records `executionBaseHead`.
- Active-state and mode-consistency gates may pass even if semantic next-move
  drift exists; record that boundary honestly.
- Pre-implementation gate passes before edits or stops with a recorded failure.

If a pre-flight check fails outside Allowed scope, stop and return to Codex.

Mandatory Gate-Failure Remediation Protocol:

- Allowed-scope failures are mandatory remediation. Complete the remediation
  and execute the failed gate again.
- Escalation is reserved for remediation that would exceed Allowed scope,
  change the claim boundary, release a `HOLD_*` prerequisite, change risk
  level, open public-sync, run live/provider proof, consume secrets/quota,
  touch forbidden paths, or perform destructive/irreversible actions.

## 6A. Source-Fidelity Pass

Before writing the worker return, verify every status and next-move claim from
the source files listed in Required First Reads. Do not cite `CLAUDE.md`, Codex
memory, IDE summaries, or chat text as canonical evidence.

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| RSF-T3 candidate exists | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md` | line 101 | `RSF-T3` | RSF roadmap tranche table | ACCEPT |
| C-02 P2 work order is closed | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md` | line 5 | `Status` | C-02 P2 work order | ACCEPT |
| C-02 P2 state entry is closed | `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json` | JSON `value.status` | `modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615` | active session source entry | ACCEPT |
| Front door currently names RSF-T3 and blocks C-02 P2 redispatch | `CVF_SESSION_MEMORY.md` | `## Next Allowed Move` | `Next Allowed Move` | active session front door | ACCEPT |
| Handoff startup acknowledgment currently names RSF-T3 and blocks C-02 P2 redispatch | `AGENT_HANDOFF_V19_2026-06-15.md` | `## Startup Acknowledgment` | `Startup acknowledged` | active handoff | ACCEPT |
| Generated nextAllowedMove source currently carries RSF-T3 dispatch text | `CVF_SESSION/state/entries/nextAllowedMove.json` | JSON `value` | `nextAllowedMove` | active session source entry | ACCEPT |
| RSF-T2 is closed and left RSF-T3 candidate-only before RSF-T3 dispatch | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_COMPLETION_2026-06-16.md` | Implementation Summary; Claim Boundary | `RSF-T3` | RSF-T2 completion review | ACCEPT |
| Worker return confirms the stale C-02 P2 contradiction existed at dispatch-selection time and is now pointer-remediated | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md` | `## Findings / Position` | `F-RSF3-002` | RSF-T3 worker return | ACCEPT |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Apply guard to one non-CI2 sample | Sections 1, 4, and 7 | worker-return findings | source reads plus active-session checks | PASS |
| Document operator-facing next-move behavior | Sections 7 and 9 | worker-return decision section | reviewer reads worker return | PASS |
| Keep runtime/provider/public/legacy out of scope | Sections 4 and Claim Boundary | changed-file set | `git diff --name-status` | PASS |
| Preserve reviewer-owned closure | Review Gate | completion review by Codex only | reviewer closure gate | PASS |

## 6C. Worker Autonomy / No-Question Rule

Claude may repair documentation and gate-format failures inside Allowed Scope
without asking the operator. Stop only for forbidden scope, claim expansion,
runtime/provider/live work, public-sync, credential use, broad legacy scan,
broad repository scan, session-state edits, checker edits, or changes outside
Allowed Scope.

## Reviewer Closure Conversion

Because `Commit mode: WORKER_MUST_NOT_COMMIT`, Claude returns uncommitted
artifacts only. Codex owns the final completion review, committed-range gates,
material commit, and any session-sync decision.

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md`

Claude must not set a closed status, must not commit, and must not author
session-continuity files.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: RSF-T3 verifies a current governed continuity
sample from active session, roadmap, work-order, and completion artifacts. It
does not absorb, reopen, or scan legacy material and does not modify a
legacy-adjacent capability surface.

## 6D. Pending Artifact Evidence Finality

Because this is `WORKER_MUST_NOT_COMMIT`, the worker return must not claim
committed-range closure. Record actual `git status --short` with pending files
and leave material commit, pre-closure, and session sync to Codex.

## 6E. Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` after Codex review | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md` | source-backed findings and reviewer-fast pass | PASS |
| Roadmap state | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md` | RSF-T3 row `CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` | reviewer-owned closure artifact | PASS |
| Registry JSON | BLOCKED with reason | no corpus registry JSON mutation authorized; RSF-T3 is not a corpus registry tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry Markdown mutation authorized; RSF-T3 is not a corpus registry tranche | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, or live-proof artifact | N/A with reason |
| System loop interlock | N/A with reason | no system loop interlock registry mutation authorized | N/A with reason |
| Session continuity | `CVF_SESSION/**`; `CVF_SESSION_MEMORY.md`; active handoff | separate session-sync commit after material closure | N/A with reason |
| Public export | this work order | `DEFERRED_PRIVATE_ONLY` | PASS |

## 7. Write Ownership

Owned files:

- `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`
- `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`

Forbidden paths:

- `CVF_SESSION/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `governance/compat/*.py`
- `EXTENSIONS/**`
- public-sync clone paths
- credential or `.env*` files

Write mode: modify-listed / create-listed only.

## 8. Execution Plan

| Step | Action | Owner |
|---|---|---|
| 1 | Capture `executionBaseHead` and read required files | Claude |
| 2 | Verify C-02 P2 closure evidence and current stale continuity evidence | Claude |
| 3 | Run current active-session and mode-consistency gates and record their boundary | Claude |
| 4 | Create worker-return packet with findings, F2G disposition, and operator-facing next-move behavior | Claude |
| 5 | Update this work order status/evidence and RSF roadmap T3 row/evidence only if gates pass | Claude |
| 6 | Run worker-return gates and return uncommitted artifacts | Claude |
| 7 | Review, author completion, commit, and session sync if accepted | Codex |

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | RSF roadmap Scope and Non-Goals | documentation-only non-CI2 sample audit | PASS |
| Non-goals | RSF roadmap Non-Goals | forbids runtime, provider, public-sync, legacy, product work | PASS |
| Lane split | RSF roadmap Tranche Plan | executes RSF-T3 candidate only | PASS |
| Dependency/source-verification plan | RSF roadmap Verification and RSF-T2 closure | source verification block and required first reads | PASS |
| Claim boundary | RSF roadmap Claim / Final / Verification Boundary | one non-CI2 sample only | PASS |
| Acceptance criteria | RSF-T3 GC-018 | T3-AC rows reflected below | PASS |
| Verification/evidence | RSF-T3 GC-018 | commands in Evidence Requirements | PASS |
| Dispatch-readiness decision | RSF-T3 GC-018 | authorized for no-commit worker dispatch | PASS |

## 8B. Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude worker; Codex reviewer/closer |
| Provider or surface | Claude worker return; Codex local workspace |
| Session or invocation | 2026-06-16 RSF-T3 non-CI2 next-move sample |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, git status, active-session checks, worker-return fast gate |
| Target paths | RSF roadmap, this work order, RSF-T3 worker return |
| Allowed scope source | RSF-T3 GC-018 and actual-work audit |
| Before status evidence | dispatch base `72fa2427` |
| After status evidence | worker must record pending status before return |
| Diff evidence | worker must record `git diff --name-status` |
| Approval boundary | bounded documentation/audit worker return only |
| Claim boundary | no runtime/provider/public/live/legacy broad scan claim |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude worker; Codex reviewer/closer |
| Provider or surface | Claude worker return; Codex local workspace |
| Session or invocation | 2026-06-16 RSF-T3 non-CI2 next-move sample |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, git status, active-session checks, worker-return fast gate |
| Target paths | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` |
| Allowed scope source | RSF-T3 GC-018; worker return; Codex reviewer closure authority |
| Before status evidence | clean worktree at worker execution base `f8d468c1` before reviewer acceptance |
| After status evidence | RSF-T3 worker return accepted with reviewer repairs; material closure pending commit |
| Diff evidence | material closure batch uses `f8d468c1..HEAD`; `git diff --name-status` |
| Approval boundary | bounded documentation/audit closure only |
| Claim boundary | one non-CI2 next-move sample; no runtime/provider/public/live/legacy/session-state claim in material commit |
| Agent type | Claude worker `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer |
| Invocation ID | `rsf-t3-non-ci2-next-move-sample-closure-2026-06-16` |
| Expected manifest | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` |
| Actual changed set | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: current source evidence confirms C-02 P2 is
closed while at least one operator-facing continuity surface still points to
C-02 P2 as next move.

Evidence Comparison Requirement: worker return compares actual evidence against
the prediction.

Contradiction Handling Requirement: contradictory evidence requires a
Contradiction Or Gap Disposition and claim-boundary update.

Claim Update Requirement: worker return records whether the claim was
confirmed, revised, narrowed, or invalidated.

## Evidence Requirements

Required worker evidence:

- `git rev-parse --short HEAD`;
- `git status --short`;
- source evidence table for C-02 P2 status, front-door next move, handoff next
  move, and `nextAllowedMove` source entry;
- `python governance/compat/check_active_session_state.py --enforce`;
- `python governance/compat/check_session_mode_consistency.py --enforce`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- `git diff --check`;
- `git diff --name-status`;
- explicit `N/A with reason` for runtime, provider, live proof, public-sync,
  legacy absorption, and checker implementation.

## 9. Evidence Requirements

Required worker evidence:

- `git rev-parse --short HEAD`;
- `git status --short`;
- source evidence table for C-02 P2 status, front-door next move, handoff next
  move, and `nextAllowedMove` source entry;
- `python governance/compat/check_active_session_state.py --enforce`;
- `python governance/compat/check_session_mode_consistency.py --enforce`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- `git diff --check`;
- `git diff --name-status`;
- explicit `N/A with reason` for runtime, provider, live proof, public-sync,
  legacy absorption, and checker implementation.

Base-anchor evidence:

- `dispatchBaseHead`: `72fa2427`
- `executionBaseHead`: `WORKER_MUST_CAPTURE_AT_START`
- `closureBaseHead`: `N/A - pending review`
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Committed-range `pre-closure`: `N/A - pending review`

## 10. Acceptance Criteria

| ID | Criterion |
|---|---|
| T3-AC1 | Worker return verifies from source files whether C-02 P2 is closed and whether current continuity points to it. |
| T3-AC2 | Worker return records active-session and mode-consistency gate results and their semantic boundary. |
| T3-AC3 | Worker return states operator-facing next-move behavior without authorizing Model Gateway P2/P3 implementation. |
| T3-AC4 | Worker return includes Finding-To-Governance Learning Disposition and next control recommendation. |
| T3-AC5 | Changed-file set stays inside Allowed Scope. |

Fail conditions:

- Missing source verification for C-02 P2 closure or continuity next-move claim.
- Any runtime, provider, credential, public-sync, broad legacy scan, checker
  implementation, session-state edit, or Model Gateway implementation claim.
- Any closed-equivalent claim before Codex reviewer commit and pre-closure gate.

## 11. Review Gate

Implementation may proceed only after:

- this work order and GC-018 are committed by Codex;
- pre-dispatch gate passed for the dispatch batch;
- worker pre-implementation gate passes or returns a source-backed failure.

Closure may proceed only after:

- Codex inspects the real worker diff;
- worker-return fast gate passes or failures are dispositioned;
- Codex authors the reviewer-owned completion review;
- committed-range pre-closure gate passes on a non-empty range.

For `WORKER_MUST_NOT_COMMIT`, worker handoff is not closure.

## 12. Closure Checklist

| Item | Required state |
|---|---|
| Work order | `COMPLETE_PENDING_REVIEW` after Claude return |
| Worker return | present, source-backed, and pending review |
| Roadmap | RSF-T3 worker-return evidence updated only if supported |
| Runtime/provider/public/live/legacy | explicitly N/A with reason |
| Completion review | reviewer-owned, created by Codex |
| Commit | Codex only |

## 13. Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all Allowed Scope edits are on disk,
uncommitted, and gates have passed. Return `BLOCKED` if source evidence rejects
the sample, the required gates cannot run, or the task requires Forbidden Scope.

## Operator Checkpoint

No operator checkpoint is required for actions inside Allowed Scope. Return to
the operator only for runtime changes, provider/live work, public-sync, broad
legacy scan, broad repository scan, session-state edits, active-handoff edits,
governance-checker edits, Model Gateway implementation, C-02 P2/P3 dispatch,
or widening the claim boundary.

## Claim Boundary

Allowed claim after successful worker return:

One non-CI2 next-move sample was source-checked and the operator-facing behavior
was documented for Codex review.

Forbidden claims:

- all stale roadmap/session states are solved;
- Model Gateway C-02 P2 or P3 is authorized for implementation;
- runtime behavior changed;
- provider routing or live governance behavior changed;
- public readiness, production readiness, or provider readiness;
- legacy content was absorbed;
- a new machine checker was implemented.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_CANDIDATE` |
| Next control action | Verify the non-CI2 stale next-move sample and recommend whether a next-move freshness checker extension is needed |
| Worker blame | `N/A_WITH_REASON`: this is a continuity/control-plane freshness gap, not an implementation-quality blame assignment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance work order. No public-sync batch is
authorized.
