# CVF GC-018 - AAF-T6A Early Diagnostic Wire-in

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: baseline

dispatchBaseHead: d11e0522

Batch ID: AAF-T6A

## Purpose

Authorize a narrow automation-foundation tranche that wires the existing
read-only AAF helper into the earliest applicable autorun phase. AAF-T6A moves
`run_agent_automation_assist.py --json --enforce` from an optional helper into
the `pre-implementation` autorun gate so a worker sees local helper-detectable
packet, corpus, worker-experience, and signal-readout defects before writing
material files.

This tranche implements only early diagnostic wire-in. It does not implement
the full AAF-T6 read-receipt gate, AAF-T7A acceleration helper, scaffold
generation, helper mutation, patch application, runtime behavior, live proof,
or public-sync.

## Operator Authorization

The operator accepted the learning principle that repeated late-stage agent
defects should become early proactive assistance, and directed creation of an
AAF-T6A work order for Early Diagnostic Wire-in after REF-T0 active reference
path repair closed.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 create AAF-T6A Early Diagnostic Wire-in work order | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Agent Autorun Workflow Control Standard | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | ACCEPT |
| Agent Error To Governance Learning Philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |
| Existing AAF helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Existing autorun gate | `governance/compat/run_agent_autorun_workflow_gate.py` | ACCEPT |

Provider-specific memory is not CVF authority. This dispatch is based on
repo-local standards, helper source, and autorun gate source.

## Scope / Owner Boundary

Allowed worker scope:

- update `governance/compat/run_agent_autorun_workflow_gate.py`;
- update `governance/compat/test_run_agent_autorun_workflow_gate.py`;
- update `governance/compat/test_run_agent_automation_assist.py` only if a
  focused contract fixture is strictly needed for the wire-in;
- create
  `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_WORKER_RETURN_2026-06-22.md`.

Reviewer/closer closure scope:

- update this GC-018 status and paired work order status;
- create
  `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_COMPLETION_2026-06-22.md`;
- repair allowed-scope packet, manifest, source-verification, or test evidence
  defects required by machine gates before commit.

Forbidden worker scope:

- no full AAF-T6 Guard Orientation Read-Receipt Gate;
- no AAF-T7A reviewer/closer acceleration helper;
- no ledger store, source directory, generator, drift checker, durable store,
  runtime Learning Plane mutation, provider/live proof, CLI/MCP adapter
  behavior, public-sync, wrapper/proxy enforcement, direct IDE/shell/git/
  filesystem interception, arbitrary command execution, EDIT/COMMIT execution,
  queue, daemon, watcher, readiness, full-hook equivalence, cost optimization
  claim, or universal governed-coding-control claim;
- no scaffold template generator, patch preview/apply, helper file mutation,
  route schema edits, runtime/product behavior, dependency installation, or
  generated aggregate edits.

Risk ceiling: R0/R1 guard wiring and focused tests only.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- optional:
  `governance/compat/test_run_agent_automation_assist.py`
- `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_WORKER_RETURN_2026-06-22.md`

No commit is authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: AAF-T6A is ready for worker dispatch as a bounded early
diagnostic wire-in.

Proposed tranche: `AAF-T6A Early Diagnostic Wire-in`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker performs guard wiring and focused tests without committing;
reviewer/closer reviews and commits accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Pre-implementation is the autorun phase before file edits | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | lines 62, 145-148, 210 | `pre-implementation` | autorun workflow standard | ACCEPT |
| Late machine checks should move into earliest applicable autorun phase | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | line 78 | earliest applicable autorun phase gate | learning philosophy | ACCEPT |
| Existing autorun gate builds phase command list in `_run_phase` | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 578-619 | `_run_phase` | autorun gate runner | ACCEPT |
| Existing autorun gate has focused tests | `governance/compat/test_run_agent_autorun_workflow_gate.py` | file exists; test module | `test_range_shape_preflight_blocks_exact_manifest_session_mix` | unittest module | ACCEPT |
| Existing AAF helper supports JSON and enforce mode | `governance/compat/run_agent_automation_assist.py` | lines 839-877 | `--json`; `--enforce`; `report.defects` | AAF helper CLI | ACCEPT |
| Existing AAF helper emits defects and signal readout | `governance/compat/run_agent_automation_assist.py` | lines 491-532, 710-776 | `defects`; `signalReadout` | AAF helper report | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in AAF-T6A | Runtime status | Reason |
|---|---|---|---|
| `Early Diagnostic Wire-in` | AAF-T6A baseline/work order | DOC_ONLY_NEW | names the bounded wiring of existing read-only helper diagnostics into pre-implementation autorun |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `d11e0522`.
- `git status --short` was clean before AAF-T6A dispatch authoring.
- `rg -n` verified the autorun standard, learning philosophy, existing AAF
  helper CLI flags, and existing autorun gate insertion point.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base d11e0522 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base d11e0522 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base d11e0522 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base d11e0522 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator critique about late reviewer defects to governed early diagnostic wire-in |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; reviewer-fast gate |
| Owner surface | AAF-T6A Early Diagnostic Wire-in |
| Disposition | ADAPT as CVF-owned autorun pre-implementation diagnostic wiring |
| Claim boundary | operator/external critique remains input only until promoted through this governed dispatch |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_automation_assist.py`; focused test modules |
| Runtime behavior claimed | N/A_WITH_REASON: governance compatibility helper/gate invocation only; no product runtime, provider route, web route, CLI/MCP adapter, or Learning Plane mutation |
| Helper/checker implementation claimed | BOUNDED: invoke existing read-only helper from pre-implementation autorun and add focused tests |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are out of scope and untouched; AAF-T6A makes no provider registry absence, hardcoded-provider, provider-selection, or live-governance claim |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded governance helper/gate wiring only; no provider, public-sync, runtime product behavior, or generated aggregate behavior is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T6A dispatch and early diagnostic wire-in only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed autorun helper invocation only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | early diagnostic wire-in only |
| forbiddenExpansion | scaffold generation, patch application, wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, cost optimization, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Repeated worker-return packet defects can be caught only late when AAF helper is optional | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_PROMOTED | Wire existing helper into pre-implementation autorun | handled by this dispatch |
| Agents need faster repeated-error repair assistance, not only blocking gates | ACCELERATION_GAP | LEARNING_TO_ACCELERATION | SEPARATE_TRANCHE | AAF-T7A acceleration helper remains next after AAF-T6A | deferred |
| Full read-receipt proof would require a larger gate | CONTROL_PROOF_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | Full AAF-T6 read-receipt gate remains parked unless separately authorized | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: operator critique and Claude report about B19-B22
  late defects and optional AAF diagnostics.
- Predecessor intake artifact: L2A-T0 closure, REF-T0 closure, existing AAF
  helper source, autorun standard, and learning philosophy.
- Delta ledger status: `CHANGED_DISPOSITION` because optional helper guidance
  becomes mandatory pre-implementation diagnostic wiring.
- Routing matrix status: `DO_NOW` for AAF-T6A; `DEFER` for AAF-T7A and full
  AAF-T6 read-receipt gate; `SEPARATE_RUNTIME_TRANCHE` for any provider,
  runtime, CLI/MCP, scaffold, patch, queue, watcher, or public-sync behavior.
- Semantic sampling status: sampled autorun phase standard, learning philosophy,
  existing helper CLI, and autorun gate insertion point.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | AAF helper remains read-only and local-diagnostic only. |
| CHANGED_DISPOSITION | Helper moves from opt-in command to pre-implementation autorun command. |
| NEW_FINDING | Focused autorun tests should prove the helper command appears only in pre-implementation common commands. |
| REMOVED_OR_REJECTED | Read-receipt proof, scaffold generation, patch/apply, runtime/provider/public behavior, and AAF-T7A acceleration are rejected from AAF-T6A. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Wire read-only AAF helper into pre-implementation autorun and test command presence/failure propagation. |
| RESOLVED_BY_DESIGN | Existing helper already emits JSON, defects, and signal readout; AAF-T6A reuses it. |
| DEFER | AAF-T7A reviewer/closer acceleration helper and full AAF-T6 read-receipt gate. |
| STRATEGIC_OPERATOR_DECISION | Operator decides after AAF-T6A closure whether AAF-T7A or MPI continuation comes next. |
| SEPARATE_RUNTIME_TRANCHE | runtime/product behavior, provider/live proof, CLI/MCP adapter behavior, scaffold generator, patch apply, queue/daemon/watcher, public-sync. |
| OUT_OF_SCOPE | direct interception, universal governed-coding control, speed/cost claims, durable memory store, Learning Plane runtime mutation. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T6A-RS1 | Autorun standard `pre-implementation` | Worker runs this gate before material edits | DO_NOW | Should helper stay optional? | PASS - pre-implementation is earliest applicable phase |
| AAF-T6A-RS2 | Learning philosophy | Late machine check should move earlier | DO_NOW | Should this wait for full read-receipt? | PASS - bounded helper wire-in is separable |
| AAF-T6A-RS3 | AAF helper CLI | `--json --enforce` already exists | RESOLVED_BY_DESIGN | Should worker build a new helper? | PASS - reuse existing helper |
| AAF-T6A-RS4 | Autorun gate `_run_phase` | phase-specific command insertion exists | DO_NOW | Should helper run in every phase? | PASS - work order limits it to pre-implementation |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for bounded autorun helper
  wire-in.
- Corpus root: repo-local files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus targeted
  `rg -n` checks.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=Authority Chain and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo scan, generated registry mutation, runtime/provider/web/MCP/public-sync corpus scan; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no full `.private_reference/legacy` scan, no runtime/
  provider/web/MCP/public-sync corpus scan, no generated aggregate edit.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: AAF-T6A baseline maps operator finding to worker
  deliverables.
- Adversarial verification: source lines identify existing helper CLI and
  autorun insertion point.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T6A is private provenance governance-helper wiring. No public-sync
repository work or public catalog claim is authorized.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify the autorun workflow gate and its
focused tests to run the existing AAF read-only helper in the
`pre-implementation` phase.

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- optional:
  `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator directed proactive helper reminders at
the start of worker execution to reduce repeated late defects. AAF-T6A applies
that decision to the existing autorun pre-implementation phase.

Rollback boundary: revert the accepted AAF-T6A material closure commit to
remove the helper command insertion and focused tests together.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local Codex session |
| Session or invocation | AAF-T6A dispatch authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, `rg`, apply_patch, governance gates |
| Target paths | this GC-018 baseline and paired AAF-T6A work order |
| Allowed scope source | operator instruction to create AAF-T6A Early Diagnostic Wire-in work order |
| Before status evidence | HEAD `d11e0522`; clean worktree before dispatch authoring |
| After status evidence | AAF-T6A dispatch artifacts pending pre-dispatch gates and commit |
| Diff evidence | dispatch diff and gate receipts |
| Approval boundary | dispatch only; worker implementation remains no-commit |
| Claim boundary | early diagnostic wire-in dispatch only; no read-receipt/scaffold/runtime/provider/public behavior |
| Agent type | dispatcher |
| Invocation ID | `aaf-t6a-early-diagnostic-wire-in-dispatch-2026-06-22` |
| Expected manifest | this baseline; paired AAF-T6A work order |
| Actual changed set | checked by dispatch gates before commit |
| Manifest delta | MATCH_PENDING_COMMIT |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | `pre-implementation` autorun runs `governance/compat/run_agent_automation_assist.py --base <base> --head <head> --json --enforce`. |
| AC2 | Focused tests prove the helper command is included in `pre-implementation` and not introduced as a broad all-phase helper. |
| AC3 | Focused tests prove helper command failure contributes to pre-implementation gate failure through existing command-result aggregation. |
| AC4 | Existing AAF helper remains read-only and is not changed to mutate files, run provider/live proof, or execute arbitrary commands. |
| AC5 | Worker return records actual base, status, changed set, focused tests, gates, and claim boundary. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_FOR_WORKER_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_WORKER_RETURN_2026-06-22.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_COMPLETION_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior authorized | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active session front-door/state/handoff | session-sync follows accepted material closure commit | N/A with reason |

## Claim Boundary

AAF-T6A authorizes only bounded early diagnostic wire-in of the existing
read-only AAF helper into `pre-implementation` autorun plus focused tests. It
does not authorize full AAF-T6 read-receipt proof, AAF-T7A acceleration,
scaffold generation, patch preview/apply behavior, helper mutation, runtime
behavior, provider/live behavior, CLI/MCP adapter behavior, public-sync,
session-sync by worker, direct interception, readiness claims, speed/cost
claims, or universal governed-coding control.
