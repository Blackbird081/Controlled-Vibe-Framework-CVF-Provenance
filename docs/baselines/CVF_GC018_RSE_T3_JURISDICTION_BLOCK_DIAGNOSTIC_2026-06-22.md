# CVF GC-018 - RSE-T3 Jurisdiction Block Diagnostic

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: baseline

dispatchBaseHead: 31faa6bc

Batch ID: RSE-T3

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This baseline
authorizes one bounded read-only diagnostic tranche; it does not map, enumerate,
project, or classify CVF state.

## Purpose

Authorize RSE-T3, the fourth and final tranche of the Role Switch Envelope lane.
RSE-T3 adds one bounded read-only diagnostic to the existing AAF helper that
flags a changed worker-return artifact which contains finding or gate-trap
language but lacks a `## Worker Return Jurisdiction Block`, the block defined by
the closed RSE-T2 addendum.

The diagnostic is advisory only at L2A safety level L0: it prints or serializes a
read-only readout item, makes no closure decision, edits no file, and performs no
provider, live, or runtime action. It is the first bounded slice of the roadmap
T3 candidate diagnostics; the remaining four candidates are deferred to a
separate future slice.

## Operator Authorization

The operator directed on 2026-06-22 that RSE-T2 is closed and chose to open
RSE-T3 work-order authoring, with two scope decisions: the diagnostic is hosted
as a read-only advisory readout inside the existing AAF helper rather than a new
standalone checker, and the first slice implements one to two diagnostics rather
than all five roadmap candidates. This baseline authorizes exactly one diagnostic
plus focused tests under that direction. The remaining roadmap T3 candidates
require a separate future slice and fresh authorization.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 close RSE-T2; open RSE-T3 as a read-only AAF-helper diagnostic, bounded first slice of one diagnostic | ACCEPT |
| RSE roadmap | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | ACCEPT |
| RSE-T2 addendum | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | ACCEPT |
| RSE-T1 addendum | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | ACCEPT |
| RSE-T0 standard | `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | ACCEPT |
| L2A classification standard | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | ACCEPT |
| Existing AAF helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Existing AAF helper tests | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V21_2026-06-22.md` | ACCEPT |

Provider-specific memory is not CVF authority. This dispatch is based on
repo-local CVF-governed artifacts and current helper source.

## Scope / Owner Boundary

Allowed worker scope:

- update `governance/compat/run_agent_automation_assist.py` to add one bounded
  read-only diagnostic that flags a changed worker-return artifact which contains
  finding or gate-trap language but lacks a `## Worker Return Jurisdiction Block`:
  - the diagnostic is advisory readout output only, populated only for the
    worker-return shape, derived from changed-file text already read by the
    helper;
  - it makes no closure decision, writes no file, stages nothing, commits
    nothing, and runs no provider or live or arbitrary command;
- update `governance/compat/test_run_agent_automation_assist.py` with focused
  tests covering a positive case, a negative case, the read-only property, and
  the absence of any closure or write behavior;
- create
  `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_WORKER_RETURN_2026-06-22.md`.

Reviewer/closer scope:

- update this baseline and the paired work order status after review;
- create
  `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_COMPLETION_2026-06-22.md`;
- perform session-sync if accepted.

Forbidden worker scope:

- no closure-blocking enforcement, no new exit-nonzero defect class, and no
  change to existing enforce-mode defect behavior; the diagnostic is advisory
  readout only;
- no edit to other `governance/compat/` checkers, the autorun gate wiring, the
  dispatch-quality checker, or the work-order template;
- no edit to the closed RSE-T0 standard, RSE-T1 addendum, or RSE-T2 addendum;
- no implementation of the remaining four roadmap T3 candidate diagnostics;
- no provider, live, web, CLI/MCP adapter, workspace, queue, daemon, watcher,
  public-sync, direct interception, L3 apply, arbitrary command execution,
  readiness, or universal control behavior or claim;
- no generated aggregate edits and no session, handoff, or front-door edits by
  the worker.

Risk ceiling: R2 bounded read-only helper diagnostic plus focused tests; no
enforcement, no mutation.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_WORKER_RETURN_2026-06-22.md`

No worker commit is authorized.

## Decision / Baseline / Proposed Tranche

Baseline decision: RSE-T3 is closed as a bounded read-only diagnostic tranche,
one diagnostic in the first slice.

Proposed tranche: `RSE-T3 Jurisdiction Block Diagnostic`.

Tranche owner split: the roadmap author owns the roadmap; the dispatch author
owns this GC-018 baseline and the paired work order; the worker implements the
diagnostic and focused tests without committing; the reviewer/closer reviews and
commits accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Roadmap T3 names the jurisdiction-block-missing diagnostic as a candidate | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 259 | T3 - Early Diagnostic / Checker Wire-In | RSE roadmap T3 section | ACCEPT |
| RSE-T2 addendum defines the Worker Return Jurisdiction Block the diagnostic detects | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | line 51 | The Worker Return Jurisdiction Block | RSE-T2 addendum | ACCEPT |
| AAF helper has a read-only advisory readout item dataclass to mirror | `governance/compat/run_agent_automation_assist.py` | line 487 | ReviewerReadoutItem | AAF helper readout item | ACCEPT |
| AAF helper builds a read-only readout only for the reviewer-return shape | `governance/compat/run_agent_automation_assist.py` | line 708 | _build_reviewer_readout | AAF helper readout builder | ACCEPT |
| AAF helper assembles the report in build_report | `governance/compat/run_agent_automation_assist.py` | line 867 | build_report | AAF helper report assembly | ACCEPT |
| AAF helper reads changed-file text without a runtime call | `governance/compat/run_agent_automation_assist.py` | line 197 | _read_changed_text | AAF helper changed-text reader | ACCEPT |
| AAF helper has a focused readout test class to mirror | `governance/compat/test_run_agent_automation_assist.py` | line 830 | ReviewerReadoutTests | AAF helper test module | ACCEPT |
| L2A safety level L0 is a read-only suggestion that changes nothing | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | line 104 | L0 read-only suggestion | L2A Acceleration Safety Levels | ACCEPT |

## New Helper Terms

| Proposed term | Owner in RSE-T3 | Runtime status | Reason |
|---|---|---|---|
| `jurisdictionReadout` | RSE-T3 helper output | NEW_HELPER_OUTPUT_FIELD | names the read-only advisory list flagging worker-returns missing a jurisdiction block |
| `JurisdictionReadoutItem` | RSE-T3 helper dataclass | NEW_HELPER_DATACLASS | a frozen advisory item with text fields only, mirroring ReviewerReadoutItem |

These names are proposed; the worker may use a source-verified equivalent if it
mirrors the existing read-only readout pattern. No checker key, exit code, or
enforce-mode defect is created by RSE-T3.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `31faa6bc`.
- `git status --short` was clean before RSE-T3 dispatch authoring.
- `rg` and direct reads verified the roadmap T3 candidate list, the RSE-T2
  jurisdiction block definition, the existing AAF helper readout dataclass,
  builder, report assembly, and test class, and the L2A L0 safety level.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 31faa6bc --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 31faa6bc --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 31faa6bc --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 31faa6bc --head HEAD --enforce
```

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_agent_automation_assist.py`; `governance/compat/test_run_agent_automation_assist.py` |
| Runtime behavior claimed | N/A_WITH_REASON: governance compatibility helper only; no product runtime, provider route, web route, CLI/MCP adapter, or Learning Plane mutation |
| Helper/checker implementation claimed | BOUNDED: add one read-only advisory readout diagnostic and focused tests |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded read-only helper diagnostic only; no provider, public-sync, runtime product behavior, enforcement, or generated aggregate behavior is claimed |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker returns with findings can omit the jurisdiction block, leaving routing implicit | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | RSE-T3 adds a read-only diagnostic flagging the omission | handled by this dispatch |
| The remaining four roadmap T3 diagnostics are not yet implemented | RULE_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | a later RSE-T3 slice may add them with fresh authorization | deferred |
| Closure-blocking enforcement of the jurisdiction block | CONTROL_PROOF_GAP | GOVERNANCE_CONTROL_PLANE | OUT_OF_SCOPE | enforcement remains out of scope; advisory only | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime, provider, or cost behavior changed or claimed | handled |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded read-only
  diagnostic tranche.
- Corpus root: repo-local files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus `rg --files --hidden --no-ignore` for targeted confirmation.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows
  in this baseline.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Authority Chain and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo sweep, generated aggregate mutation, runtime/provider/web/MCP/public-sync sweep; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full-repo sweep, generated aggregate mutation,
  runtime/provider/web/MCP/public-sync sweep, public-sync proof, provider/live
  proof.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: RSE-T3 baseline maps one roadmap T3 candidate diagnostic
  to a bounded read-only helper diagnostic work order.
- Adversarial verification: source rows distinguish the new read-only diagnostic
  from closure-blocking enforcement and from the remaining deferred candidates.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: RSE-T3 is private provenance governance-helper work. No public-sync
repository work or public catalog claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | RSE-T3 read-only jurisdiction block diagnostic dispatch |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | explicit helper invocation only; advisory readout output |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception claim |
| claimLanguage | read-only advisory diagnostic only |
| forbiddenExpansion | closure-blocking enforcement, new exit-nonzero defect, other checker edits, autorun wiring change, remaining T3 candidates, L3 apply, provider/live, public-sync, queue/daemon/watcher, direct interception, readiness, and universal control remain out of scope |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | N/A with reason: extends two existing helper files; creates no new durable foundation directory and relocates nothing. |
| New durable foundation directory | N/A with reason |
| Generated aggregate impact | N/A with reason: no generated aggregate is created or edited. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or INDEX storage tranche. |
| Guard owner | reviewer/closer verifies the diagnostic is read-only and the changed set stays within the two helper files plus the worker return. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one read-only advisory diagnostic to the
existing AAF helper and add focused tests for it, without adding any
closure-blocking enforcement, new exit-nonzero defect class, patch apply, closure
decision, staging, commit, push, provider or live, or runtime behavior.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator directed RSE-T2 closed and chose to open
RSE-T3 as a read-only AAF-helper diagnostic with a bounded first slice of one
diagnostic. This baseline authorizes only that scope.

Rollback boundary: revert the accepted RSE-T3 material closure commit to remove
the read-only diagnostic and its focused tests together.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher (work-order author role) |
| Provider or surface | local workspace |
| Session or invocation | RSE-T3 dispatch authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, `rg`, dispatch authoring, governance gates |
| Target paths | this GC-018 baseline and paired RSE-T3 work order |
| Allowed scope source | operator RSE role model and the operator scope decisions for RSE-T3 |
| Before status evidence | HEAD `31faa6bc`; clean worktree before dispatch authoring |
| After status evidence | RSE-T3 dispatch artifacts pending pre-dispatch gates |
| Diff evidence | dispatch diff plus AAF helper, dispatch-quality, and pre-dispatch autorun receipts |
| Approval boundary | dispatch authoring only; worker implementation remains no-commit; the work-order reviewer reviews this work order before execution |
| Claim boundary | read-only diagnostic dispatch only; no enforcement, runtime, provider, or public behavior |
| Agent type | dispatcher |
| Invocation ID | `rse-t3-jurisdiction-block-diagnostic-dispatch-2026-06-22` |
| Expected manifest | this baseline; paired RSE-T3 work order |
| Actual changed set | this baseline and paired RSE-T3 work order |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | The helper emits a read-only advisory item when a changed worker-return contains finding or gate-trap language but lacks a `## Worker Return Jurisdiction Block`. |
| AC2 | The helper emits no such item when the worker-return contains the block, or when there is no finding or gate-trap language. |
| AC3 | The diagnostic makes no closure decision, writes no file, adds no exit-nonzero defect, and changes no existing enforce-mode behavior. |
| AC4 | Focused tests cover a positive case, a negative case, the read-only property, and the no-closure property. |
| AC5 | Worker return records actual base, status, changed set, focused tests, gates, the Core Guard Self-Protection block listing both protected paths, and claim boundary, and the worker commits nothing. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_FOR_WORKER_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED`; checklist checked | PASS |
| Worker return | `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_WORKER_RETURN_2026-06-22.md` | `Status: COMPLETE_PENDING_REVIEW` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_COMPLETION_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior authorized | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active session front-door/state/handoff | separate session-sync follows accepted material closure commit | PASS |

## Claim Boundary

RSE-T3 authorizes only one bounded read-only advisory diagnostic added to the
existing AAF helper plus focused tests. It does not authorize closure-blocking
enforcement, a new exit-nonzero defect class, any change to existing enforce-mode
behavior, edits to other checkers or the autorun wiring or the work-order
template, edits to the closed RSE-T0, RSE-T1, or RSE-T2 documents, the remaining
roadmap T3 candidate diagnostics, L3 apply, runtime behavior, provider/live
behavior, CLI/MCP adapter behavior, public-sync, session-sync by the worker,
direct interception, readiness claims, speed/cost claims, or universal
governed-coding control.
