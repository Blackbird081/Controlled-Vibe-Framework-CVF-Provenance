# CVF Agent Work Order - FPC-T3 Foundation Checker Template Coverage Plan

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `6047e18f`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `77098b23`

sourceAuthority:
`docs/baselines/CVF_GC018_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_COMPLETION_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

FPC-T1 matrix:
`docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`

FPC-T2 matrix:
`docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`

FPC-T2 completion:
`docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md`

## Purpose

Produce a source-backed FPC-T3 coverage plan that ranks foundation
checker/template/standard candidates and recommends the smallest safe next
implementation tranche for later separate authorization.

This work order is planning-only. It does not authorize checker implementation,
template mutation, registry mutation, runtime/source/test mutation, downstream
use-case work, operating-system audit installation, agent computer-control
changes, live/provider/OCR proof, public-sync, readiness/cost/quality claims,
memory reinjection, high-risk promotion, or autonomous mutation.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator agreed to proceed with the recommendation and requested a Claude work order under Codex control | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | ACCEPT |
| FPC-T1 matrix | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | ACCEPT |
| FPC-T2 matrix | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | ACCEPT |
| FPC-T2 completion | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | ACCEPT |
| FPC-T3 GC-018 | `docs/baselines/CVF_GC018_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | ACCEPT |
| Work-order finality addendum | `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md` | ACCEPT |
| Closure-quality standard | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches GC-018 and this work order |
| Worker | Claude | authors allowed-scope coverage plan and worker-return packet only |
| Reviewer / closer | Codex | reviews worker return, runs gates, commits, and decides any separate implementation or registry-edit packet |

## Intake Role Routing Decision

Intake summary: FPC-T2 closed bounded and routed C05 to FPC-T3-C01 before any
C05 registry entry. The operator also raised a workspace-integrity and
agent-attribution concern after a transient protected-directory visibility
incident and agreed to include that control need in the next FPC-T3 planning
work order.

Scope classification: read-only governed planning packet with bounded output
artifacts.

Risk sensitivity: high governance risk if FPC-T3 silently becomes an
implementation or OS-control tranche; medium risk if the plan overclaims what a
deterministic checker can prove.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude executes under `WORKER_MUST_NOT_COMMIT`; Codex
reviews, closes, and commits.

Escalation condition: return `BLOCKED_SCOPE_EXPANSION` if Claude needs checker
implementation, template mutation, registry mutation, runtime/source/test
mutation, generated aggregate mutation, session-state mutation, operating-system
audit configuration, file watcher service creation, destructive broker design,
agent computer-control permission changes, external app source access,
provider/OCR/API proof, public-sync, claim expansion, destructive action, or a
new operator decision.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `AGENTS.md`
5. `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`
6. `docs/baselines/CVF_GC018_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`
7. `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`
8. `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`
9. `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md`
10. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
11. `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md`
12. `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
13. `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md`
14. `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`
15. `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md`
16. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md`
17. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
18. `governance/compat/run_local_governance_hook_chain.py`
19. `governance/compat/run_worker_return_fast_gate.py`
20. `governance/compat/check_active_session_state.py`
21. `governance/compat/check_core_guard_self_protection.py`
22. `governance/compat/check_forbidden_filesystem_state.py`
23. this work order

Claude may read other CVF-governed roadmap, completion, reference, source, or
checker files only as needed to verify candidate evidence. Claude must not read
external Document Translator or Policy_Local source trees. Claude must not cite
provider-specific agent memory or guidance files as CVF source authority.

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=fpc_t3_foundation_checker_template_coverage_plan_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=FPC-T3; next allowed move=Claude produces FPC-T3 coverage plan and worker-return packet under WORKER_MUST_NOT_COMMIT; parked checkpoint=checker implementation, template mutation, registry edits, OS audit installation, agent computer-control changes, DT-CVF-T0, Policy_Local PL-S1, OCR/provider/live proof, retrieval, public-sync, T12, readiness/cost/quality claims remain parked.`

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
7. Confirm `docs/roadmaps` exists before and after the worker run; if it
   disappears or shows unrelated deletions, stop with
   `BLOCKED_PROTECTED_PATH_VISIBILITY_INCIDENT` and record `git status --short`.

## Write Ownership

Claude owns only worker-authored FPC-T3 planning artifacts under
`WORKER_MUST_NOT_COMMIT`.

Claude may create or update only:

- `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`;
- `docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_WORKER_RETURN_2026-06-13.md`;
- this work order only if adding worker-return evidence is necessary.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`
- `docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_COMPLETION_2026-06-13.md`
- `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

pendingStatusTokensAllowedBeforeReview:
COMPLETE_PENDING_REVIEW, IMPLEMENTATION_COMPLETE_PENDING_REVIEW, DRAFT, HOLD_*

closedEquivalentResidueDisposition:
Reviewer conversion completed by Codex. Pending worker-return status remains
historical worker evidence only; this work order current status is
`CLOSED_PASS_BOUNDED`.

predecessorClosureFactSource:
`docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md`
and material commit `c12c65b1`, not mutable active-session currentMode.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| FPC-T2 closure complete | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md`; material commit `c12c65b1` | ACCEPT |
| FPC-T2 session sync complete | session-sync commit `6047e18f`; active state and handoff point to FPC-T2 closed boundary | ACCEPT |
| FPC-T3 eligibility source-backed | parent roadmap row says FPC-T3 depends on FPC-T2 closure plus fresh GC-018/work order | ACCEPT |
| FPC-T3-C01 required by FPC-T2 | FPC-T2 completion says C05 needs FPC-T3-C01 before a C05 registry entry | ACCEPT |
| Paired GC-018 exists | `docs/baselines/CVF_GC018_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC-T3 purpose and plan-first boundary | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `## FPC-T3 - Foundation Checker Coverage Plan` | plan first, implementation second | FPC roadmap | ACCEPT |
| EXISTS: FPC-T3 candidate vocabulary | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | `## FPC-T3 Candidate List` | `FPC-T3-C01` through `FPC-T3-C06` | FPC-T1 matrix | ACCEPT |
| EXISTS: FPC-T3-C01 prerequisite for C05 | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | `Finding-To-Governance Learning Disposition` | `FPC-T3-C01` | FPC-T2 completion | ACCEPT |
| EXISTS: FPC-T2 dependency notes for C01-C06 | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | `## FPC-T3 Dependency Notes` | `FPC-T3-C01`; `FPC-T3-C02`; `FPC-T3-C06` | FPC-T2 matrix | ACCEPT |
| EXISTS: worker-return fast gate command builder | `governance/compat/run_worker_return_fast_gate.py` | function definition | `build_commands` | worker-return gate | ACCEPT |
| EXISTS: reviewer-fast hook chain | `governance/compat/run_local_governance_hook_chain.py` | hook chain definitions | `reviewer-fast` | local governance hook chain | ACCEPT |
| EXISTS: active-session compatibility checker | `governance/compat/check_active_session_state.py` | script path constant | `THIS_SCRIPT_PATH` | active session state gate | ACCEPT |
| EXISTS: core guard self-protection checker | `governance/compat/check_core_guard_self_protection.py` | script path constant | `THIS_SCRIPT` | core guard self-protection gate | ACCEPT |
| EXISTS: forbidden filesystem state checker | `governance/compat/check_forbidden_filesystem_state.py` | check function definition | `_check` | forbidden filesystem state gate | ACCEPT |
| EXISTS: work-order template requires source verification | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `Source Verification Block` | `Claimed item`; `Disposition` | canonical work-order template | ACCEPT |
| EXISTS: no-commit worker return evidence required | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | no-commit worker return evidence section | `Worker Pending-Return Gate` | worker autonomy standard | ACCEPT |
| EXISTS: closure conversion required | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | `Reviewer Closure Conversion` | `completionReviewPath`; `reviewerOwnedClosurePaths` | closure-quality standard | ACCEPT |
| EXISTS: no-commit boundary defined | `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md` | `WORKER_MUST_NOT_COMMIT` rows | `WORKER_MUST_NOT_COMMIT` | finality addendum | ACCEPT |
| EXISTS: system-loop interlock registry owner | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | `## Registry` | `CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | system-loop interlock standard | ACCEPT |
| EXISTS: provider-specific agent files are not CVF authority | `AGENTS.md` | `Mandatory Provider-Specific Agent Memory Boundary` | `NOT_CVF_SOURCE` | agent front-door instructions | ACCEPT |

## New Doc-Only Fields

The worker may introduce these doc-only fields in the FPC-T3 coverage plan:

| Field | Purpose |
| --- | --- |
| `Candidate ID` | FPC-T3 candidate identifier |
| `Candidate name` | candidate label |
| `Candidate source` | source artifact or observed current-session control need |
| `Control target` | checker, template, standard, gate fixture, or audit/control plane |
| `Earliest phase target` | pre-dispatch, worker-return fast gate, reviewer-fast, pre-closure, pre-push, or separate OS/control-plane tranche |
| `Repeated-defect risk` | high, medium, or low |
| `Operator time saved` | high, medium, or low |
| `False-positive risk` | high, medium, or low |
| `Protected-path impact` | none, read-only, protected write, or external-control |
| `Deterministic-test availability` | available, partial, unknown, or blocked |
| `Recommended disposition` | one approved planning disposition |
| `Next implementation owner` | future Codex, Claude worker, reviewer, or operator-decision lane |
| `Claim boundary` | what the candidate can and cannot prove |

Approved planning dispositions:

- `IMPLEMENT_FIRST_CANDIDATE_LATER`
- `IMPLEMENT_AFTER_PREREQUISITE`
- `TEMPLATE_UPDATE_LATER`
- `CHECKER_EXTENSION_LATER`
- `WORKER_GATE_FIXTURE_LATER`
- `CONTROL_DESIGN_ONLY`
- `DEFER_WITH_REASON`
- `REJECT_WITH_REASON`
- `SOURCE_GAP_BLOCKS_DISPATCH`

## Negative Search And Collision Discipline

Exact search roots: repo-root governed docs, source, tests, and JSON surfaces.

Exact search command or query: worker must use `rg` for any candidate symbol
that may be absent, including a candidate checker name or proposed control
field, before assigning `SOURCE_GAP_BLOCKS_DISPATCH`.

Coverage across source/tests/docs/JSON/external evidence: current FPC-T3 is
limited to CVF-governed repo surfaces. External evidence and provider-specific
memory files are not CVF authority.

Same-token collision result: if a searched token occurs elsewhere with a
different or non-authoritative meaning, the worker must record the collision
and explain why it is not binding.

Absent-versus-collision disposition: `SOURCE_GAP_BLOCKS_DISPATCH` is allowed
only when the required source fact is absent from authoritative CVF-governed
surfaces after the exact search; same-token collisions must be labeled
non-authoritative or different meaning.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Source section | Work-order instruction | Acceptance evidence |
| --- | --- | --- | --- |
| FPC-T3 turns gaps into prioritized checker/template/standard plan | FPC roadmap `## FPC-T3` | Purpose; Required Deliverables | coverage plan ranks every candidate |
| Default FPC-T3 scope is plan first | FPC roadmap FPC-T3 claim boundary | Forbidden Scope; Authorized Artifact Set | no checker/template/runtime/source/test mutation |
| FPC-T3-C01 gates C05 registry viability | FPC-T2 completion | Candidate Requirements | C01 dependency and C05 registry boundary present |
| Rank by defect risk, operator time, phase, false positives, protected path, deterministic tests | FPC roadmap FPC-T3 ranking rules | Ranking Rules | ranking matrix has every factor |
| Preserve no-commit worker finality | finality addendum and closure-quality standard | Reviewer Closure Conversion Block | worker return has pending status and actual worktree |
| Add workspace-integrity/audit control as bounded candidate | operator request and current-session incident | FPC-T3-C07 Candidate Requirements | C07 row is design-only and does not configure OS controls |

## Candidate Requirements

Claude must evaluate at least:

| Candidate ID | Candidate | Minimum required disposition logic |
| --- | --- | --- |
| FPC-T3-C01 | `check_epistemic_process_packet.py` | Treat as prerequisite candidate for FPC-T2-C05; identify checker inputs, required sections, output signal, false-positive risk, and earliest safe phase. |
| FPC-T3-C02 | `check_dice_machine_candidates.py` | Determine whether DICE machine-candidate invariants can be enforced by autorun without touching downstream adapters. |
| FPC-T3-C03 | interlock registry coverage checker extension | Determine how to detect closed workflow chains with downstream signals but no interlock disposition without causing broad false positives. |
| FPC-T3-C04 | work-order template epistemic block | Determine whether a template update should precede C01 implementation for high-evidence work orders. |
| FPC-T3-C05 | worker-return fast gate epistemic fixture | Determine dependency on C01 and how no-commit workers would run the check before return. |
| FPC-T3-C06 | memory `rawMemoryReleased=false` autorun check | Determine the narrowest source-backed invariant and whether it belongs in reviewer-fast or pre-closure. |
| FPC-T3-C07 | workspace-integrity and agent-operation-audit control | Design-only candidate for protected-folder disappearance detection, operation logging, lease/branch/worktree discipline, and rollback evidence. It must not configure Windows auditing, Sysmon, file watchers, destructive brokers, or agent computer-control permissions in this tranche. |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within the
Allowed Artifact Set must be repaired and rerun by Claude before return. Claude
must ask the operator only when repair would exceed Allowed scope, change the
claim boundary, require protected-path mutation, configure operating-system
audit/control surfaces, consume provider quota/secrets, run live proof, touch
public-sync, or perform destructive or irreversible actions.

## Commit Prompt Readiness

This section exists because the packet contains no-commit boundary language.
Claude must not commit. Codex may commit the dispatch package only after the
dispatch gates pass.

- Diff scope: PASS
- Tests: PASS
- Gates: PASS
- Untracked unrelated: NONE
- Forbidden touched paths: NONE

## Execution Plan

1. Complete the Required First Reads and Pre-Flight Checks.
2. Build a source-backed candidate ledger for FPC-T3-C01 through FPC-T3-C07.
3. Rank each candidate using the roadmap factors and the new protected-path
   impact factor.
4. Identify dependencies among candidates, especially C01 before any C05
   registry-entry route.
5. Recommend one smallest safe first implementation tranche for later separate
   authorization.
6. Create the coverage plan and worker-return packet only.
7. Run worker-return gates, repair allowed-scope defects, and return pending
   artifacts uncommitted.

## Evidence Requirements

Claude must cite source-backed evidence for each candidate row. Evidence may
come from the Required First Reads, current CVF-governed guard source, current
CVF-governed standards, FPC-T1/FPC-T2 artifacts, and current-session
operator-reported incident context only as a design trigger for C07. Provider
memory, hidden IDE history, and external app source are not authority.

For C07, Claude must separate repo-local detection evidence from OS-level
attribution evidence. Repo-local checks may detect changed/deleted paths; they
cannot prove who used the physical machine without separate OS or endpoint audit
evidence.

## Acceptance Criteria

- All seven candidates are present in the coverage plan.
- Every candidate has a source-backed or explicitly design-triggered evidence
  row.
- C01 is ranked as prerequisite for C05 registry viability unless Claude records
  a source-backed contradiction.
- C07 is classified `CONTROL_DESIGN_ONLY` or a stricter deferred disposition
  unless a current CVF-governed source already implements the control.
- The recommended first implementation tranche is bounded to one checker,
  template update, or control-design follow-up.
- No forbidden path or action is touched.
- Worker-return gate evidence is included.

## Review Gate

Codex must review the worker return before any commit. Reviewer-fast must pass
before Codex accepts the pending artifacts. Codex owns the completion review,
pre-closure gate on a committed non-empty range, and any session-state sync.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when the allowed artifacts are complete,
pending in the worktree, and worker-return gates have either passed or are
blocked with explicit out-of-scope reason.

Return `BLOCKED_SCOPE_EXPANSION` if useful work requires checker/template/source
implementation, registry mutation, protected-path mutation, OS audit setup,
agent computer-control changes, external source inspection, live proof,
public-sync, or operator policy decision.

Return `BLOCKED_PROTECTED_PATH_VISIBILITY_INCIDENT` if `docs/roadmaps` or
another protected path disappears, shows unrelated deletion, or cannot be
verified during the worker run.

## Operator Checkpoint

No operator checkpoint is required for Claude to produce the two allowed
planning artifacts. A new operator checkpoint is required before any later
checker implementation, template mutation, registry edit, OS/endpoint audit
configuration, file watcher service, destructive broker, agent
computer-control permission change, public-sync, live proof, or downstream
use-case work.

## FPC-T3-C07 Design Boundary

FPC-T3-C07 must answer:

1. What deterministic repo-local signals can detect protected-folder
   disappearance or unrelated mass deletion before staging or commit?
2. What operation-log evidence should a future agent-control plane require to
   attribute high-risk filesystem actions by actor, command/tool surface,
   timestamp, cwd, changed paths, and approval boundary?
3. Which parts belong inside CVF repo guards, and which require separate
   operator-approved OS or endpoint audit setup?
4. What is the rollback evidence model: git status, branch/worktree snapshot,
   protected-path lease, artifact digest, or external audit log?
5. What claim boundary prevents CVF from pretending repo-local checks can prove
   who used the physical machine without OS-level audit already enabled?

## Required Deliverables

Claude must create:

1. `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`
2. `docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_WORKER_RETURN_2026-06-13.md`

The coverage plan must include:

- Purpose;
- Scope / Target / Owner Boundary;
- Source Verification Summary;
- Candidate ranking matrix for FPC-T3-C01 through FPC-T3-C07;
- dependency map showing which candidates depend on C01;
- recommended first implementation tranche;
- FPC-T3-C07 design boundary and future authorization requirements;
- rejected or deferred candidates with reason;
- claim boundary;
- Public Export Disposition.

The worker-return packet must include:

- Purpose;
- Scope / Target / Owner Boundary;
- Target / Source;
- Scope / Methodology;
- Findings / Position;
- Risk / Corrective Action;
- Worker Pending-Return Gate;
- Evidence Trace;
- Finding-To-Governance Learning Disposition;
- Claim Boundary;
- Public Export Disposition.

## Worker Pending-Return Gate

Claude must include this table in the worker-return packet:

| Gate | Applies when | Command or evidence | Worker result |
| --- | --- | --- | --- |
| Execution anchor | every worker run | `git rev-parse --short HEAD` before edits | `executionBaseHead=<hash>` |
| Pending worktree | every no-commit return | `git status --short` | actual pending file list |
| Protected roadmap directory check | every worker run | `Test-Path docs/roadmaps`; `git status --short -- docs/roadmaps` | `PASS` or `BLOCKED_PROTECTED_PATH_VISIBILITY_INCIDENT` |
| Worker-return fast gate | every no-commit return before handoff | `python governance/compat/run_worker_return_fast_gate.py` | `PASS` or `BLOCKED` |
| Markdown structural completeness | changed governed markdown | `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or `BLOCKED` |
| Finding-To-Governance learning | worker-return findings | `python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or `BLOCKED` |
| Machine Closure Package | if closure-equivalent wording appears | `python governance/compat/check_machine_closure_package.py --base <executionBaseHead> --head HEAD --enforce` | `PASS`, `N/A with reason`, or `BLOCKED` |
| Dispatch quality | if work order is touched | `python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce` | `PASS`, `N/A with reason`, or `BLOCKED` |

Claude must not claim pre-closure PASS.

## Forbidden Scope

FPC-T3 authorizes no checker implementation, template mutation, interlock
registry edit, runtime/source/test implementation, generated aggregate edit,
session-state edit, active handoff edit, front-door edit, external Document
Translator source inspection, Policy_Local source inspection, OCR/provider/API
live proof, retrieval route wiring, corpus ingestion, public-sync, readiness
claim, cost claim, quality claim, provider-specific memory-as-source claim,
Windows audit installation, Sysmon installation, file watcher service creation,
destructive broker implementation, agent computer-control permission change,
memory reinjection, high-risk promotion, or autonomous mutation.

## Exit Criteria

FPC-T3 worker return is acceptable only if:

- all seven candidates are evaluated;
- FPC-T3-C01 is treated as the prerequisite for any future C05 registry entry;
- C07 remains a control-design candidate only;
- the plan recommends one smallest safe first implementation tranche for later
  authorization;
- no runtime/source/test/template/registry/session-state/public-sync mutation is
  made;
- worker-return fast gate evidence is recorded or blocked with explicit reason;
- worker leaves artifacts uncommitted.

## Closure Checklist

- [x] GC-018 baseline exists for FPC-T3.
- [x] Source Verification Block is present.
- [x] Roadmap-to-Work-Order Trace Matrix is present.
- [x] Dependency Release Evidence cites FPC-T2 closure and session-sync commits.
- [x] Reviewer Closure Conversion Block is present.
- [x] Worker Pending-Return Gate is defined.
- [x] Forbidden Scope excludes implementation and OS-control actions.
- [x] Public Export Disposition is present.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; closure checklist checked | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `Status: FPC_T3_CLOSED_PASS_BOUNDED` | PASS |
| Coverage plan | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | C01-C07 ranked; C04+C01 recommendation; C07 design-only boundary | PASS |
| Worker return | `docs/reviews/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_WORKER_RETURN_2026-06-13.md` | worker return gate evidence and Negative Search And Collision Discipline | PASS |
| Registry JSON | BLOCKED with reason | FPC-T3 did not authorize GC-051 registry mutation | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | FPC-T3 did not authorize registry Markdown mutation | BLOCKED with reason |
| System loop interlock | N/A with reason | FPC-T3 did not authorize interlock registry mutation | N/A with reason |
| Corpus registry | BLOCKED with reason | FPC-T3 added no runtime/source/test owner surface requiring GC-051 coverage | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source tree, OCR/provider/API/live proof, OS audit, or retained external artifact was used | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V18_2026-06-12.md` | reviewer-owned follow-up after material closure commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Claim Boundary

FPC-T3 decides only planning priority and implementation sequencing. It does not
prove checker correctness, implement a checker, update templates, mutate the
system-loop registry, prove semantic truth, prove OS-level attribution, prove
agent computer-control safety, run live provider proof, open downstream
use-case work, or authorize autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance FPC-T3 dispatch work order. Public-sync is not
authorized by this tranche.
