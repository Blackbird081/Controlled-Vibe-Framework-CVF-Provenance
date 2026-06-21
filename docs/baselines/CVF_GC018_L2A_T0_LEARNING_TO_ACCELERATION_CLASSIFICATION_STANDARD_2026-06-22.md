# CVF GC-018 - L2A-T0 Learning-To-Acceleration Classification Standard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: baseline

dispatchBaseHead: 667c1a65

Batch ID: L2A-T0

## Purpose

Authorize L2A-T0 as a bounded governance-learning foundation tranche. The
tranche turns the operator finding into a CVF-owned classification standard:
when repeated agent friction is captured through Finding-To-Governance, CVF
must classify not only prevention work, but also whether the lesson can become
a safe acceleration helper, scaffold, patch preview, or template.

This baseline deliberately keeps MPI parked while this learning-control layer
is clarified. It does not implement the closure-conversion helper itself; that
future helper is one use case of the broader Learning-To-Acceleration loop.

## Operator Authorization

The operator approved pausing MPI and processing the learning layer first on
2026-06-22. The operator explicitly reframed AAF-T7A as a use case rather than
the whole concept: real CVF learning should transform repeated findings into
prevention and acceleration, not only into late-stage correction.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 instruction to pause MPI and dispatch learning work | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Finding-To-Governance trigger standard | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | ACCEPT |
| Agent error learning philosophy | `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |
| AAF-T5 closure | `docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_COMPLETION_2026-06-20.md` | ACCEPT |
| Work-order machine closure addendum | `docs/reference/work_order_template/CVF_WORK_ORDER_MACHINE_CLOSURE_PACKAGE_ADDENDUM.md` | ACCEPT |

Provider-specific memory and external-agent prose are not CVF authority. The
operator/Claude exchange is input; this baseline and paired work order are the
CVF-governed dispatch authority for L2A-T0.

## Scope / Owner Boundary

Allowed worker scope:

- create `docs/reference/learning_to_acceleration/README.md`;
- create `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md`;
- update `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
  with a compact pointer to the new L2A classification standard;
- create `docs/reviews/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD_WORKER_RETURN_2026-06-22.md`;
- define classification vocabulary for reminder, checker, phase-gate,
  accelerator, scaffold, template, and no-automation outcomes;
- state safe automation levels: read-only suggestion, scaffold generation,
  patch preview, and tightly allowlisted apply as future work only;
- keep the standard documentation/reference only.

Forbidden worker scope:

- no edits to `governance/compat/**`, session state, active handoff, root
  startup routers, public-sync, runtime/provider routes, `.github/**`, web UI,
  MCP packages, dependency manifests, or generated JSON aggregates;
- no implementation of AAF-T6, AAF-T7A, closure-conversion helper, scaffold
  generator, checker, hook wiring, autorun wiring, queue, daemon, watcher,
  wrapper/proxy, direct IDE/shell/git/filesystem interception, arbitrary
  command execution, EDIT/COMMIT execution, provider/live proof, public-sync,
  vector/durable store, or runtime Learning Plane mutation;
- no claim that future agents are automatically accelerated or controlled;
- no reopening of MPI-T3/MPI-T4 until operator reselects MPI after L2A work.

Risk ceiling: R0/R1 documentation/reference classification standard only.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `docs/reference/learning_to_acceleration/README.md`
- `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md`
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
- `docs/reviews/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD_WORKER_RETURN_2026-06-22.md`

No commit is authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: L2A-T0 is ready for worker dispatch as the first
Learning-To-Acceleration foundation tranche.

Proposed tranche: `L2A-T0 Learning-To-Acceleration Classification Standard`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker creates the reference standard, index, pointer update, and
worker-return artifact without committing; reviewer/closer reviews and commits
accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Worker execution must include packet-shape sections and no commit | `docs/reference/guard_orientation/README.md` | Task Class Guard Map, Worker execution row | `WORKER_MUST_NOT_COMMIT`; worker-return packet shape | Guard Orientation Index | ACCEPT |
| Work-order dispatch requires source verification and handoff controls | `docs/reference/guard_orientation/README.md` | Task Class Guard Map, Work-order authoring row | Source Verification Block; Agent Handoff Contract Control Block | Guard Orientation Index | ACCEPT |
| F2G standard requires each material finding to record defect class, lane, disposition, next action, and handled/deferred state | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Protocol | `## Finding-To-Governance Learning Disposition` | Finding-To-Governance standard | ACCEPT |
| F2G standard accepts rule, template, standard, machine-check, phase-gate, and design-review promotions | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Generalizable finding promotion; Minimum disposition values | `RULE_ADDED`; `TEMPLATE_UPDATED`; `STANDARD_ADDED`; `MACHINE_CHECK_ADDED`; `PHASE_GATE_PLACEMENT_GAP`; `DESIGN_REVIEW_REQUIRED` | Finding-To-Governance standard | ACCEPT |
| F2G standard says reusable findings cannot remain documentation-only worker commentary | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Generalizable finding promotion | reusable CVF control promotion | Finding-To-Governance standard | ACCEPT |
| Agent-error learning philosophy defines repeated agent error as a governance training sample | `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | Core Philosophy | repeated agent error as training sample | Agent-error learning philosophy | ACCEPT |
| Agent-error learning philosophy escalates from rule to machine check to earliest phase gate | `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | Escalation Ladder | earliest applicable autorun phase gate | Agent-error learning philosophy | ACCEPT |
| AAF-T5 closure records helper/checker learning and deferred AAF-T7 helper/index hardening | `docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_COMPLETION_2026-06-20.md` | Finding-To-Governance Learning Disposition; Follow-Up Routing Matrix | AAF-T7 helper/index friction hardening | AAF-T5 closure | ACCEPT |
| Work-order closure addendum defines Machine Closure Package and Acceptance Receipt Assertion Matrix ownership | `docs/reference/work_order_template/CVF_WORK_ORDER_MACHINE_CLOSURE_PACKAGE_ADDENDUM.md` | Purpose; Machine Closure Package Table | Machine Closure Package; Acceptance Receipt Assertion Matrix | Work-order template addendum | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in L2A-T0 | Runtime status | Reason |
|---|---|---|---|
| `Learning-To-Acceleration` | new L2A reference standard | DOC_ONLY_NEW | names the loop that classifies repeated findings into prevention and acceleration outcomes |
| `accelerationDisposition` | new L2A reference standard | DOC_ONLY_NEW | records whether a finding can become a helper, scaffold, patch preview, template, or no automation |
| `REMINDER_ONLY` | new L2A taxonomy | DOC_ONLY_NEW | existing helper/readout style: surface the lesson early without blocking |
| `CHECKER_CANDIDATE` | new L2A taxonomy | DOC_ONLY_NEW | candidate for machine validation or existing F2G machine-check route |
| `PHASE_GATE_CANDIDATE` | new L2A taxonomy | DOC_ONLY_NEW | candidate for earlier autorun/hook placement |
| `ACCELERATOR_CANDIDATE` | new L2A taxonomy | DOC_ONLY_NEW | candidate for repeat-work reduction through safe helper behavior |
| `SCAFFOLD_CANDIDATE` | new L2A taxonomy | DOC_ONLY_NEW | candidate for generated skeletons or templates |
| `PATCH_PREVIEW_CANDIDATE` | new L2A taxonomy | DOC_ONLY_NEW | candidate for non-mutating patch-preview assistance |
| `NO_ACCELERATION_APPLICABLE` | new L2A taxonomy | DOC_ONLY_NEW | explicit reason that no acceleration is safe or worthwhile |

These are classification terms only. They are not runtime fields, JSON schema
fields, CLI/MCP contract fields, or current checker-enforced values until a
future governed tranche explicitly implements them.

## Required L2A Standard Contract

The worker must define a standard that answers these questions for each
repeated or generalizable finding:

| Question | Required treatment |
|---|---|
| What was the repeated friction? | short source-backed finding statement |
| Is prevention needed? | map to reminder, rule, checker, or phase-gate outcome |
| Is acceleration possible? | classify helper/scaffold/patch-preview/template/no-automation |
| What is the safe automation level? | read-only, generated skeleton, patch preview, or future allowlisted apply |
| What must remain human-reviewed? | review boundary and postcondition checker |
| What future tranche, if any, should implement it? | name candidate lane without dispatching it |

The worker must explicitly include AAF-T7A closure-conversion assistance as an
example use case, not as the whole L2A lane.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `667c1a65`.
- `git status --short` was clean before L2A-T0 dispatch authoring.
- Source verification used direct file reads and `rg -n` lookups against
  current repository files.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 667c1a65 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 667c1a65 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 667c1a65 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 667c1a65 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | returned critique to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | L2A-T0 learning-to-acceleration standard |
| Disposition | ADAPT as CVF-owned classification standard |
| Claim boundary | external-agent output remains input only until classified and promoted through governed CVF artifacts |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: L2A-T0 dispatch authorizes documentation/reference work only |
| Runtime behavior claimed | N/A_WITH_REASON |
| Helper/checker implementation claimed | N/A_WITH_REASON |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no runtime, provider, helper/checker, public-sync, or generated aggregate behavior is claimed by this dispatch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | L2A-T0 dispatch and reference-standard authoring only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed documentation/reference classification only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | learning classification and acceleration candidate taxonomy only |
| forbiddenExpansion | helper implementation, scaffold generator, patch application, wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Repeated reviewer/closer text churn is not only a defect source; it is also acceleration opportunity | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | L2A-T0 must define classification for acceleration candidates | handled by this dispatch |
| Existing F2G ladder emphasizes rule/checker/phase placement but not productivity accelerators | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | Add L2A classification standard and pointer from F2G | handled by this dispatch |
| Closure-conversion helper is a useful accelerator use case but too narrow as the whole concept | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | record AAF-T7A as later use case after L2A-T0 | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this dispatch | handled |

## Rescan Intelligence Hardening

- Original source artifact: operator/Claude/Codex learning critique exchange on
  2026-06-22.
- Predecessor intake artifact: AAF-T5 closure and existing F2G standard.
- Delta ledger status: `CHANGED_DISPOSITION` because the finding is promoted
  from one helper use case into a foundation classification standard.
- Routing matrix status: `DO_NOW` for L2A-T0 reference standard; `DEFER` for
  AAF-T6A early diagnostic wire-in and AAF-T7A closure-conversion helper;
  `SEPARATE_RUNTIME_TRANCHE` for any helper apply mode, runtime mutation,
  public-sync, provider/live, or CLI/MCP behavior.
- Semantic sampling status: sampled F2G standard, agent-error learning
  philosophy, AAF-T5 closure, guard orientation index, and work-order closure
  addendum.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | F2G remains the existing learning disposition surface. |
| CHANGED_DISPOSITION | Learning must now classify acceleration opportunities, not only prevention. |
| NEW_FINDING | Repeated mechanical closure/review edits are candidates for safe helper or scaffold acceleration. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception/helper-apply scope remains rejected for L2A-T0. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | L2A-T0 classification standard and F2G pointer. |
| RESOLVED_BY_DESIGN | Existing F2G remains the source learning surface; L2A adds an acceleration classification layer rather than replacing F2G. |
| DEFER | AAF-T6A early diagnostic wire-in. |
| DEFER | AAF-T7A closure-conversion acceleration helper foundation. |
| STRATEGIC_OPERATOR_DECISION | Operator decides whether to run AAF-T6A or AAF-T7A once the L2A-T0 completion review exists, then whether to resume MPI. |
| SEPARATE_RUNTIME_TRANCHE | checker enforcement, scaffold generator, patch preview/apply helper, CLI/MCP adapter, runtime mutation. |
| OUT_OF_SCOPE | public-sync, provider/live proof, direct interception, universal control, MPI continuation during this tranche. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| L2A-T0-RS1 | F2G Protocol | findings need defect class, lane, disposition, next action, and handled/deferred state | DO_NOW | Does L2A replace F2G? | PASS - L2A is a pointer/classification extension only |
| L2A-T0-RS2 | Agent-error Escalation Ladder | late machine checks should move earlier | DEFER | Does dispatch implement phase-gate wiring now? | PASS - AAF-T6A remains deferred |
| L2A-T0-RS3 | AAF-T5 Follow-Up Routing Matrix | AAF-T7 helper/index hardening is deferred | DEFER | Does L2A-T0 implement AAF-T7A? | PASS - only an example use case is authorized |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded governance-reference tranche.
- Corpus root: repo-local source files named in Authority Chain and Source Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus targeted `rg -n` lookups.
- Manifest artifact or inline manifest: Authority Chain and Source Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Authority Chain and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo scan and generated registry mutation out of scope; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no `.private_reference/legacy` scan, no MPI route/source scan, no runtime/provider/web/MCP/public-sync corpus scan.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated.
- Drift check: N/A with reason: no generated aggregate edited.
- Output traceability: L2A-T0 baseline maps operator finding to work order deliverables.
- Adversarial verification: file-existence drift was checked for cited active/archive standards.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: L2A-T0 is private provenance governance-learning foundation work. No
public-sync repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local Codex session |
| Session or invocation | L2A-T0 dispatch authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, `rg`, apply_patch, governance gates |
| Target paths | this GC-018 baseline and paired L2A-T0 work order |
| Allowed scope source | operator instruction to pause MPI and dispatch learning layer |
| Before status evidence | HEAD `667c1a65`; clean worktree before dispatch authoring |
| After status evidence | dispatch artifacts pending pre-dispatch gates and commit |
| Diff evidence | dispatch diff and gate receipts |
| Approval boundary | dispatch only; worker implementation remains no-commit |
| Claim boundary | reference-standard dispatch only; no helper/checker/runtime implementation |
| Agent type | dispatcher |
| Invocation ID | `l2a-t0-dispatch-2026-06-22` |
| Expected manifest | `docs/baselines/CVF_GC018_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD_2026-06-22.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD_FOR_CLAUDE_2026-06-22.md` |
| Actual changed set | `docs/baselines/CVF_GC018_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD_2026-06-22.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD_FOR_CLAUDE_2026-06-22.md` |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Work order dispatches a `WORKER_MUST_NOT_COMMIT` documentation/reference tranche only. |
| AC2 | Worker deliverables define L2A classification without implementing helper/checker/scaffold code. |
| AC3 | F2G standard receives only a compact pointer to the new L2A standard. |
| AC4 | AAF-T7A closure-conversion helper is recorded as a future use case, not implemented. |
| AC5 | MPI remains parked until operator reselects it after learning work. |
| AC6 | Required worker checks and worker-return packet shape are explicit. |

## Claim Boundary

L2A-T0 authorizes only a CVF-owned classification standard and front-door
reference for learning-to-acceleration routing. It does not implement,
validate, or enforce any accelerator, scaffold, patch preview, checker,
phase-gate, runtime behavior, provider behavior, CLI/MCP behavior, public-sync,
or universal governed-coding control.
