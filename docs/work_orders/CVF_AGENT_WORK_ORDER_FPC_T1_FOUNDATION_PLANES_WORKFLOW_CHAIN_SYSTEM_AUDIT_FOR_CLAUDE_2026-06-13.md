# CVF Agent Work Order - FPC-T1 Foundation Planes Workflow-Chain System Audit

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `148a59ff`

executionBaseHead: `148a59ff`

closureBaseHead: `WORKER_MUST_NOT_SET`

sourceAuthority:
`docs/baselines/CVF_GC018_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_COMPLETION_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

## Purpose

Produce a source-backed FPC-T1 Plane-to-Chain matrix spine that shows which CVF
foundation planes and foundation lanes already operate as workflow-chain systems,
which are machine-checked, which are structural-only, which need FPC-T2 interlock
decisions, and which need FPC-T3 checker/template planning.

This work order is audit-only. It does not authorize FPC-T2 or FPC-T3 execution.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked whether FPC-T2/T3 must wait and directed Codex to let Claude do parallelizable work now | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | ACCEPT |
| Claude rebuttal | `docs/reviews/CVF_FPC_T1_T3_FOUNDATION_PLANES_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md` | ACCEPT |
| Claude remediation proposals | `docs/reviews/CVF_FPC_T1_T3_FOUNDATION_PLANES_ROADMAP_CLAUDE_REMEDIATION_PROPOSALS_2026-06-13.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches GC-018 and this work order |
| Worker | Claude | authors allowed-scope audit matrix and worker-return packet only |
| Reviewer / closer | Codex | reviews worker return, runs gates, commits, and decides next FPC-T2/T3 packet |

## Intake Role Routing Decision

Intake summary: FPC roadmap is finalized after Claude rebuttal remediation.
The operator wants parallelizable work to start without waiting unnecessarily.

Scope classification: read-only governed audit with bounded output artifacts.

Risk sensitivity: medium governance risk because the audit can influence later
interlock/checker work, but no runtime or registry mutation is authorized.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude executes under `WORKER_MUST_NOT_COMMIT`; Codex
reviews, closes, and commits.

Escalation condition: return `BLOCKED_SCOPE_EXPANSION` if Claude needs runtime
source edits, interlock registry edits, generated aggregate edits, session-state
edits, external app source access, provider/OCR/API/live proof, public-sync, or
claim expansion beyond audit/map output.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`
5. `docs/baselines/CVF_GC018_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_2026-06-13.md`
6. `docs/reviews/CVF_FPC_T1_T3_FOUNDATION_PLANES_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`
7. `docs/reviews/CVF_FPC_T1_T3_FOUNDATION_PLANES_ROADMAP_CLAUDE_REMEDIATION_PROPOSALS_2026-06-13.md`
8. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md`
9. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
10. `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
11. `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md`
12. `docs/reviews/CVF_MLW3_RT1_EVIDENCE_TO_LEARNING_RUNTIME_PROOF_COMPLETION_2026-06-05.md`
13. this work order

Claude may read other CVF governed roadmap, completion, reference, source, or
checker files only as needed to fill matrix cells. Claude must not read external
Document Translator or Policy_Local source trees.

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=fpc_t1_foundation_planes_workflow_chain_system_audit_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=FPC-T1; next allowed move=Claude performs read-only FPC-T1 foundation audit matrix under WORKER_MUST_NOT_COMMIT and returns uncommitted artifacts; parked checkpoint=FPC-T2/FPC-T3 execution, DT-CVF-T0, Policy_Local PL-S1, external Document Translator source, OCR/provider/live proof, retrieval, public-sync, T12, readiness/cost/quality claims remain parked.`

## Pre-Flight Checks

Claude must complete these checks before authoring artifacts:

1. Read every Required First Reads file.
2. Record `git rev-parse --short HEAD`.
3. Record `git status --short`.
4. Stop with `BLOCKED_UNEXPECTED_FILESYSTEM_STATE` if unrelated staged or
   uncommitted files are present before work.
5. Confirm `WORKER_MUST_NOT_COMMIT`.
6. Confirm allowed artifacts are limited to the two deliverables in this work
   order, plus this work order only if adding worker-return evidence is
   necessary.

## Write Ownership

Claude owns only worker-authored FPC-T1 audit artifacts under
`WORKER_MUST_NOT_COMMIT`.

Codex owns dispatch packet edits, completion review, session-state sync,
roadmap closure conversion, final gates, and commit.

Claude must not edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, active handoff
files, generated aggregates, runtime/source/test trees, interlock registries,
checker scripts, public-sync files, external app clones, or provider/live-proof
surfaces.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope gate failures without asking the operator.
Claude must return to Codex only when repair would require forbidden paths,
runtime/source mutation, interlock registry mutation, generated aggregate
mutation, session-state mutation, external app source access, live/provider/API
proof, public-sync, claim expansion, destructive action, or a new operator
decision.

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `148a59ff` | Codex | ACCEPT |
| executionBaseHead | `148a59ff` | Claude | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record worker-return base/head and
`git status --short` output in the worker-return packet.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_FOR_CLAUDE_2026-06-13.md`
- `docs/baselines/CVF_GC018_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_2026-06-13.md`
- `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_COMPLETION_2026-06-13.md`
- `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

pendingStatusTokensAllowedBeforeReview: resolved by Codex reviewer before
closure.

forbiddenClosedEquivalentResidue: resolved by Codex reviewer before closure.

## Forbidden Filesystem State At Dispatch

Dispatch must begin from clean worktree state except for this committed dispatch
package. If Claude sees unrelated uncommitted or staged files before work, Claude
must stop and return `BLOCKED_UNEXPECTED_FILESYSTEM_STATE` with `git status
--short` evidence.

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| FPC roadmap finalized | roadmap status `FPC_T1_T3_ROADMAP_REBUTTAL_REMEDIATED_READY_FOR_FPC_T1_GC018`; commit `f62a8bff` | ACCEPT |
| Claude rebuttal complete | rebuttal artifact recorded and incorporated by Codex | ACCEPT |
| Claude remediation complete | remediation proposal artifact recorded and incorporated by Codex | ACCEPT |
| Operator selected parallelizable next work | 2026-06-13 operator instruction in chat | ACCEPT |
| Fresh FPC-T1 baseline | `docs/baselines/CVF_GC018_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_2026-06-13.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC roadmap ready for FPC-T1 | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | Status | `FPC_T1_T3_ROADMAP_REBUTTAL_REMEDIATED_READY_FOR_FPC_T1_GC018` | FPC roadmap | ACCEPT |
| EXISTS: FPC-T1 required matrix spine | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T1 output structure` | Plane-to-Chain matrix | FPC roadmap | ACCEPT |
| EXISTS: FPC-T1 required outputs | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `Required outputs` | outputs 1-8 | FPC roadmap | ACCEPT |
| EXISTS: FPC-T1 forbidden runtime/source edits | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T1 must not` | runtime/source files | FPC roadmap | ACCEPT |
| EXISTS: FPC-T1 forbidden interlock edits | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T1 must not` | interlock registry | FPC roadmap | ACCEPT |
| EXISTS: FPC-T1 forbidden use-case source inspection | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T1 must not` | external Document Translator / Policy_Local source | FPC roadmap | ACCEPT |
| EXISTS: system-loop interlock registry owner | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | `## Registry` | `CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | interlock standard | ACCEPT |
| EXISTS: interlock registry connections shape | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | top-level object | `connections` | interlock registry | ACCEPT |
| EXISTS: corpus completeness required for inventory/audit | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | canonical standard | Corpus Completeness And Report Integrity | corpus completeness standard | ACCEPT |
| EXISTS: MLW3 reconciliation input | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | `## Workflow` / `## Failure Modes` | `proposalAction`, `autonomousMutationAuthorized` | MLW3 contract | ACCEPT |

## New Doc-Only Fields

The worker may introduce these doc-only columns in the FPC-T1 matrix output:

| New doc-only field | Meaning |
| --- | --- |
| `Plane or lane` | audited CVF plane, foundation lane, or downstream adapter boundary |
| `Primary owner surface` | source/doc/checker/registry owner path |
| `Current closure posture` | current governed status with artifact path |
| `Workflow-chain artifacts` | roadmap/work order/completion/contract evidence |
| `System-loop interlock status` | registered, candidate, not mapped, or N/A with reason |
| `Machine-check status` | checker path, hook phase, structural-only, or N/A with reason |
| `Epistemic process status` | FPC epistemic coverage class |
| `Evidence uptake control` | how contrary evidence triggers update/escalation |
| `Deferred capability` | intentional future work if any |
| `Next action` | no action, FPC-T2 candidate, FPC-T3 candidate, or blocked |

These are doc-only audit fields. They must not be represented as existing runtime
fields or source symbols.

## Current Runtime Freshness Verification

| Source fact | Verification command or evidence | Disposition |
| --- | --- | --- |
| Dispatch base is current | `git rev-parse --short HEAD` observed by Codex as `148a59ff` after session sync | ACCEPT |
| Runtime mutation not authorized | this work order Allowed/Forbidden scope | ACCEPT |
| Existing source facts must be current | Claude must cite path plus section/line or mark the matrix cell not mapped/N/A | ACCEPT |
| Private agent memory exclusion | roadmap and this work order forbid private Codex/Claude memory as cross-agent source of truth | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Roadmap evidence | Work-order section | Verification |
| --- | --- | --- | --- |
| FPC-T1 audit precedes FPC-T2/T3 | FPC roadmap Work Plan | Purpose; Parallelization Decision | worker returns only audit matrix |
| Emit Plane-to-Chain matrix spine | FPC-T1 output structure | Authorized Artifact Set; Required Deliverables | matrix file exists |
| Include interlock, machine-check, epistemic, deferred, and next-action views | FPC-T1 required outputs | Required Deliverables | required columns present |
| Per-cell source evidence or explicit non-claim | FPC-T1 output structure | Matrix Cell Evidence Rule | no inference-only cells |
| Keep use cases downstream | FPC-T1 must not | Forbidden Path Manifest | no external use-case source read/write |
| Keep runtime/checker/registry edits out | FPC-T1 must not | Forbidden Scope | `git diff --name-status` contains only allowed files |
| Include Corpus Completeness block | Roadmap-To-Work-Order Expectations | Corpus Completeness And Report Integrity Block | block present in matrix and worker return |
| Preserve private-memory exclusion | Source Authority | Required First Reads; Claim Boundary | no private memory source citations |

## Allowed Artifact Set

Claude may create or update only:

- `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_WORKER_RETURN_2026-06-13.md`;
- this work order only if adding worker-return evidence is necessary.

## Forbidden Path Manifest

Claude must not create, edit, or import from:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator\**`;
- any external Document Translator clone;
- any external Policy_Local source tree;
- `CVF_SESSION/**` except read-only startup/state verification required by this
  work order;
- `CVF_SESSION_MEMORY.md` except read-only startup verification required by this
  work order;
- `AGENT_HANDOFF*.md` except read-only startup verification required by this
  work order;
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- `docs/corpus-intelligence/registry/**`;
- `governance/compat/**`;
- runtime/source/test trees under `EXTENSIONS/**`;
- public-sync clone paths.

Claude may cite CVF governed docs/source/checker files in this repo as evidence,
but may not modify them.

## Parallelizable FPC-T1 Work Lanes

Claude may run these lanes independently, then merge them into the matrix spine:

| Lane | Task | Output into matrix |
| --- | --- | --- |
| Lane A | Plane and owner-surface inventory | `Plane or lane`, `Primary owner surface`, `Current closure posture` |
| Lane B | System-loop interlock coverage inventory | `System-loop interlock status`, FPC-T2 candidate flags |
| Lane C | Machine-check and autorun phase inventory | `Machine-check status`, FPC-T3 candidate flags |
| Lane D | Epistemic-process coverage inventory | `Epistemic process status`, `Evidence uptake control` |

No lane may close independently. All lanes must reconcile into the same matrix
spine before worker return.

## Execution Plan

1. Establish pre-flight state and record startup acknowledgment.
2. Build a bounded source manifest from Required First Reads plus any extra
   in-repo governed files needed to support matrix cells.
3. Execute Lane A through Lane D as independent read-only inventory passes.
4. Reconcile all lane observations into one Plane-to-Chain matrix spine.
5. Convert uncertain cells into `NOT_MAPPED`, `OUT_OF_SCOPE_WITH_REASON`,
   `EPISTEMIC_PROCESS_ABSENT`, or `EPISTEMIC_PROCESS_NA_WITH_REASON` rather
   than inference.
6. Emit source-backed FPC-T2 and FPC-T3 candidate lists without authorizing
   implementation.
7. Run required worker verification.
8. Return uncommitted artifacts to Codex.

## Required Deliverables

1. `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`
   with:
   - Purpose;
   - Scope / Target / Owner Boundary;
   - Source Authority;
   - Corpus Completeness And Report Integrity block;
   - Plane-to-Chain matrix spine;
   - FPC-T2 candidate list;
   - FPC-T3 candidate list;
   - deferred capability list;
   - claim boundary;
   - Public Export Disposition.
2. `docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_WORKER_RETURN_2026-06-13.md`
   with:
   - worker disposition `WORKER_RETURN_SUBMITTED_UNCOMMITTED`;
   - changed files;
   - commands run;
   - gate output summary;
   - known findings;
   - Finding-To-Governance Learning Disposition;
   - Public Export Disposition;
   - `rawMemoryReleased=false`.

## Matrix Cell Evidence Rule

Every matrix row must follow this rule:

- machine-checked claims cite checker path, hook phase, test path, or command
  evidence;
- structural-guarded claims cite standard/template/roadmap/registry path;
- interlock claims cite the interlock registry row or mark candidate/not mapped;
- epistemic-process claims cite section/template/checker evidence or mark
  `EPISTEMIC_PROCESS_ABSENT` / `EPISTEMIC_PROCESS_NA_WITH_REASON`;
- unknown cells must be `NOT_MAPPED` or `OUT_OF_SCOPE_WITH_REASON`;
- no cell may be filled from private agent memory, chat memory, or inference
  alone.

## Corpus Completeness And Report Integrity

- Corpus task class: INVENTORY_AUDIT

- Corpus root: repository-scoped governed CVF artifacts listed in Required
  First Reads plus any additional in-repo governed files Claude cites in the
  matrix.

- Snapshot time: worker records local execution timestamp in the matrix or
  worker return.

- Enumeration command: `rg --files --hidden --no-ignore CVF_SESSION_MEMORY.md CVF_SESSION AGENT_HANDOFF_V18_2026-06-12.md docs/reference docs/roadmaps docs/reviews docs/baselines docs/work_orders governance/compat`

- Manifest artifact or inline manifest: matrix file must include an inline
  manifest of every file used.

- Manifest hash: N/A_WITH_REASON for inline manifest in governed markdown;
  worker may provide a hash if emitting a separate manifest inside the allowed
  matrix.

- Processing ledger artifact or inline ledger: matrix file must include an
  inline ledger with terminal status for each file.

- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.

- Reconciliation: manifest=worker_inline_manifest_required; ledger_terminal=worker_inline_ledger_required; exclusions=declared_below; unresolved=0

- Unresolved files: 0

- Declared exclusions: external Document Translator, external Policy_Local,
  OCR/provider/live proof, runtime source/test edits, generated aggregates,
  session-state mutation, interlock registry mutation, corpus registry mutation,
  and public-sync.

- Unreadable or unsupported files: none

- Aggregation check: worker must state how Lane A through Lane D findings
  aggregate into one matrix spine.

- Drift check: worker must record `git status --short` and base/head before
  return.

- Output traceability: every matrix row or cell cites path/section/line or uses
  a non-claim disposition.

- Adversarial verification: worker must sample at least one row from each lane A
  through D for source-backed correctness and drift risk.

- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

The matrix output must include the same fields above. Worker may tighten the
verdict to `COMPLETE_VERIFIED` only if there are zero declared exclusions and
zero unresolved files, which is not expected for this bounded audit.

Allowed verdicts: `COMPLETE_VERIFIED`, `COMPLETE_WITH_DECLARED_EXCLUSIONS`,
`PARTIAL`, `BLOCKED`, or `STALE_SNAPSHOT`.

## Evidence Requirements

Required evidence:

- source manifest and file-level processing ledger;
- Plane-to-Chain matrix with per-cell evidence or non-claim disposition;
- FPC-T2 candidate list with source-backed reason and no registry-edit
  authorization;
- FPC-T3 candidate list with source-backed reason and no checker/template-edit
  authorization;
- deferred capability list with explicit reason;
- `git status --short`;
- `git diff --check`;
- reviewer-fast result or blocked reason;
- Finding-To-Governance Learning Disposition for any finding-bearing worker
  return;
- Public Export Disposition.

Private memory, chat memory, intuition, or uncited inference is not acceptable
evidence.

## Negative Search And Collision Discipline

This work order makes no absent-token claim for any runtime token, field, enum,
schema key, failure token, config key, or source path.

Negative search roots: N/A_WITH_REASON - FPC-T1 is a positive, source-backed
audit and candidate-mapping task, not a token absence claim.

Negative search command: N/A_WITH_REASON - this dispatch packet makes no
absent-token claim.

Coverage across source, tests, docs, JSON, and external evidence:
N/A_WITH_REASON - worker must cite positive source evidence for matrix cells or
use a non-claim disposition.

Same-token collision results: N/A_WITH_REASON - no same-token absence claim is
made.

Absent-versus-collision disposition: N/A_WITH_REASON - if Claude encounters an
unverified source fact, Claude must return a source-not-found block to Codex
instead of marking an absent runtime token as verified.

## Acceptance Criteria

FPC-T1 is acceptable only if:

1. Every target plane or foundation lane from the roadmap is represented or
   explicitly excluded with reason.
2. Every matrix cell has source evidence or a non-claim disposition.
3. FPC-T2 candidates are source-backed and do not pre-authorize registry edits.
4. FPC-T3 candidates are source-backed and do not pre-authorize checker edits.
5. Document Translator and Policy_Local remain downstream and are not inspected.
6. No runtime/source/checker/registry/session/public-sync files are edited.
7. The worker-return packet records worker gates and `git status --short`.
8. The worker returns uncommitted artifacts for Codex review.

## Required Worker Verification

Claude should run:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
git diff --check
git status --short
```

If available and applicable, Claude may also run:

```powershell
python governance/compat/run_worker_return_fast_gate.py --base 148a59ff --head HEAD
```

If any required gate fails within allowed scope, Claude must repair and rerun.
If repair requires forbidden scope, Claude must return `BLOCKED_SCOPE_EXPANSION`.

## Review Gate

Codex reviewer must not accept the worker return unless:

- changed files are limited to allowed artifacts;
- worktree state is reported;
- reviewer-fast either passes or the failure is inside forbidden reviewer-owned
  closure scope;
- matrix cells contain source evidence or explicit non-claim dispositions;
- FPC-T2/FPC-T3 outputs are candidates only;
- no downstream use-case, runtime, live-proof, or public-sync claim is made.

## Closure Checklist

- [ ] Allowed artifact set only.
- [ ] Corpus Completeness And Report Integrity block present.
- [ ] Plane-to-Chain matrix spine present.
- [ ] Source manifest and processing ledger reconciled.
- [ ] FPC-T2 candidates recorded without registry authorization.
- [ ] FPC-T3 candidates recorded without checker/template authorization.
- [ ] Finding-To-Governance Learning Disposition present if findings exist.
- [ ] Public Export Disposition present.
- [ ] `WORKER_MUST_NOT_COMMIT` honored.
- [ ] Codex reviewer converts checklist before any closed-equivalent claim.

## Return-To-Orchestrator Conditions

Return `WORKER_RETURN_SUBMITTED_UNCOMMITTED` when all allowed deliverables are
created and worker verification has been run or blocked with reason.

Return `BLOCKED_SCOPE_EXPANSION` when completion requires forbidden scope.

Return `BLOCKED_UNEXPECTED_FILESYSTEM_STATE` when unrelated files exist before
worker changes.

Return `SOURCE_FACT_UNRESOLVED` when a required source fact cannot be verified
and no explicit non-claim disposition is valid.

## Operator Checkpoint

No operator checkpoint is required for FPC-T1 execution if work remains within
allowed scope.

Operator checkpoint is required before FPC-T2, FPC-T3, DT-CVF, Policy_Local,
OCR/provider/live proof, retrieval, public-sync, readiness/cost/quality claims,
or runtime/checker/interlock implementation.

## Worker Return Schema

Claude must return:

```text
FPC-T1 Worker Return
Status: WORKER_RETURN_SUBMITTED_UNCOMMITTED
Base: 148a59ff
Artifacts:
- docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md
- docs/reviews/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_WORKER_RETURN_2026-06-13.md
Gate summary:
- reviewer-fast: PASS or FAIL with reason
- diff-check: PASS or FAIL with reason
Known findings:
- none, or numbered finding list with learning disposition
Commit mode honored: WORKER_MUST_NOT_COMMIT
```

## Claim Boundary

This work order authorizes read-only FPC-T1 audit output only. It does not
authorize FPC-T2 registry edits, FPC-T3 checker/template implementation, runtime
behavior changes, provider/OCR/live proof, external app source work, public-sync,
production/public/readiness/cost/quality claims, memory reinjection, high-risk
promotion, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet. Public-sync is not authorized.

rawMemoryReleased=false
