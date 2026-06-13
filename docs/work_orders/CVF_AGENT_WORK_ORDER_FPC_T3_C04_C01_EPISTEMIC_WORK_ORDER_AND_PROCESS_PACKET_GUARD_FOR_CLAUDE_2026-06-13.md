# CVF Agent Work Order - FPC-T3-C04+C01 Epistemic Work-Order And Process Packet Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `0101eddf`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `0101eddf`

sourceAuthority:
`docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md`

rawMemoryReleased=false

plannedWorkerReturn:
`docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_WORKER_RETURN_2026-06-13.md`

plannedCompletionReview:
`docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

## Purpose

Implement the paired FPC-T3-C04+C01 governance foundation tranche.

The implementation must add a narrow epistemic block to the work-order template
and a deterministic checker that validates the corresponding process evidence
in evidence-heavy worker-return and completion packets. The checker must catch
wrong-block or missing-block PASS illusions while avoiding blanket friction for
mechanical or evidence-light work.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator authorization | operator agreed to Codex recommendation to proceed with this FPC-T3-C04+C01 work order for Claude | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` records AOT-T2-C01+C02 closure and permits fresh FPC implementation/registry work by separate source-verified work order | ACCEPT |
| FPC-T3 coverage plan | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | ACCEPT |
| FPC-T2 decision matrix | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | ACCEPT |
| FPC-T1 audit matrix | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |
| AOT standard | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | ACCEPT |
| AOT trace checker | `governance/compat/check_agent_operation_trace.py` | ACCEPT for narrow reviewer-approved trace-boundary repair only |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches this source-verified work order and owns final acceptance |
| Worker | Claude | implements allowed files only under `WORKER_MUST_NOT_COMMIT` |
| Reviewer / closer | Codex | reviews pending return, may repair allowed reviewer issues, commits, runs closure gates, and syncs session continuity if accepted |

## Intake Role Routing Decision

Intake summary: the operator approved Codex's recommendation to implement the
FPC-T3-C04+C01 pair after AOT-T2-C01+C02 closure exposed a guard-quality risk:
a PASS-looking guard can miss the intended evidence block.

Scope classification: bounded governance-control implementation with protected
`governance/compat/*.py` paths and canonical template update.

Risk sensitivity: medium-high. The tranche must catch wrong-block or
missing-block evidence early, but must not force every mechanical task through
epistemic paperwork.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude implements under `WORKER_MUST_NOT_COMMIT`; Codex
reviews, commits, and runs closure gates.

Escalation condition: return `BLOCKED_SCOPE_EXPANSION` if useful progress
requires registry mutation, runtime/provider work, public-sync, OS audit,
endpoint telemetry, external app mutation, session-state mutation, or a broader
checkpoint policy than this work order authorizes.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `AGENTS.md`
5. `docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md`
6. `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`
7. `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`
8. `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md`
9. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
10. `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md`
11. `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
12. `governance/compat/check_agent_operation_trace.py`
13. `governance/compat/check_markdown_structural_completeness.py`
14. `governance/compat/check_work_order_dispatch_quality.py`
15. `governance/compat/run_local_governance_hook_chain.py`
16. `governance/compat/run_worker_return_fast_gate.py`
17. `governance/compat/test_run_local_governance_hook_chain.py`
18. `governance/compat/test_run_worker_return_fast_gate.py`
19. `governance/compat/test_check_markdown_structural_completeness.py`
20. `governance/compat/test_check_work_order_dispatch_quality.py`
21. this work order

Provider-specific memory files may be read only as local operating guidance.
They are not CVF source authority.

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=fpc_t3_c04_c01_epistemic_work_order_and_process_packet_guard_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=FPC-T3-C04+C01; next allowed move=Claude implements bounded epistemic template/checker/gate/tests under WORKER_MUST_NOT_COMMIT; parked checkpoint=registry edits, FPC-T4, AOT deeper hardening, OS audit, endpoint monitoring, agent computer-control changes, public-sync, runtime/provider/live proof, external Document Translator, Policy_Local, T12, readiness/cost/quality claims remain parked.`

## Pre-Flight Checks

Claude must complete these checks before edits:

1. Read every Required First Reads file.
2. Record `git rev-parse --short HEAD`.
3. Record `git status --short`.
4. Stop with `BLOCKED_UNEXPECTED_FILESYSTEM_STATE` if unrelated staged or
   uncommitted files are present before work.
5. Confirm `WORKER_MUST_NOT_COMMIT`.
6. Confirm `docs/roadmaps` exists with `Test-Path docs/roadmaps`.
7. Run negative search from the GC-018 Negative Search And Collision Discipline.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC-T3 recommends C04+C01 as first implementation tranche | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | line 316 | `Recommended First Implementation Tranche` | FPC-T3 coverage plan | ACCEPT |
| EXISTS: C01 is the hard prerequisite in the FPC-T3 chain | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | line 321 | `FPC-T3-C01` | FPC-T3 coverage plan | ACCEPT |
| EXISTS: C04 is the work-order template epistemic block candidate | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | line 276 | `FPC-T3-C04` | FPC-T3 coverage plan | ACCEPT |
| EXISTS: C01 structural scope and claim boundary | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 367 | `check_epistemic_process_packet.py` | FPC-T1 audit matrix | ACCEPT |
| EXISTS: FPC-T2-C05 requires C01 before registry entry | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | line 497 | `FPC-T2-C05` | FPC-T2 decision matrix | ACCEPT |
| EXISTS: work-order template source verification requirement | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 344 | `Source Verification Block` | canonical work-order template | ACCEPT |
| EXISTS: roadmap-to-work-order trace matrix requirement | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 506 | `Roadmap-To-Work-Order Trace Matrix` | canonical work-order template | ACCEPT |
| EXISTS: protected-path authorization carrier requirement | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 868 | `Protected-Path Authorization Carrier` | canonical work-order template | ACCEPT |
| EXISTS: worker pending-return gate for no-commit workers | `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md` | line 106 | `Worker Pending-Return Gate` | finality addendum | ACCEPT |
| EXISTS: reviewer-fast hook-chain list | `governance/compat/run_local_governance_hook_chain.py` | line 24 | `REVIEWER_FAST_CHECKS` | local governance hook chain | ACCEPT |
| EXISTS: hook-chain map | `governance/compat/run_local_governance_hook_chain.py` | line 90 | `HOOK_CHAINS` | local governance hook chain | ACCEPT |
| EXISTS: worker-return fast gate command builder | `governance/compat/run_worker_return_fast_gate.py` | line 28 | `build_commands` | worker-return fast gate | ACCEPT |
| EXISTS: protected path detector for dispatch quality | `governance/compat/check_work_order_dispatch_quality.py` | line 447 | `_is_protected_authorization_path` | dispatch quality checker | ACCEPT |
| EXISTS: protected carrier validator for dispatch quality | `governance/compat/check_work_order_dispatch_quality.py` | line 467 | `_validate_protected_path_authorization_carrier` | dispatch quality checker | ACCEPT |
| EXISTS: trace block required for agent execution evidence | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 54 | `Agent Operation Trace Block` | AOT standard | ACCEPT |
| EXISTS: trace checker required labels | `governance/compat/check_agent_operation_trace.py` | line 27 | `TRACE_REQUIRED_LABELS` | agent operation trace checker | ACCEPT |
| EXISTS: trace artifact classifier owns reference-template trace eligibility | `governance/compat/check_agent_operation_trace.py` | line 154 | `is_trace_artifact` | agent operation trace checker | ACCEPT |
| EXISTS: trace violation scanner owns manifest-delta candidate selection | `governance/compat/check_agent_operation_trace.py` | line 347 | `find_trace_violations` | agent operation trace checker | ACCEPT |

## Current Runtime Freshness Verification

| Source fact | Verification command or evidence | Disposition |
| --- | --- | --- |
| `check_epistemic_process_packet.py` is not an implemented checker yet | `rg -n "check_epistemic_process_packet" governance docs EXTENSIONS scripts` shows planning-document references and no current `governance/compat/check_epistemic_process_packet.py` file | ACCEPT |
| The authorized implementation is governance/checker/template plus narrow AOT false-positive repair only | Write Ownership and Protected paths list restrict edits to `docs/reference/`, `governance/compat/`, and worker return; AOT checker changes are limited to template trace eligibility and manifest-delta candidate selection | ACCEPT |
| No runtime/provider/public/OS-control work is authorized | Forbidden Scope excludes runtime/provider/live proof, public-sync, OS audit, endpoint monitoring, and external app mutation | ACCEPT |

## New Doc-Only Fields

Claude may add these labels to the canonical work-order template and matching
checker fixtures:

| Field | Purpose |
| --- | --- |
| `Epistemic Process Applicability` | high-evidence, evidence-light, or mechanical classification |
| `Expected Result / Prediction` | expected outcome to compare against actual evidence |
| `Evidence Comparison Requirement` | required comparison between expectation and observed evidence |
| `Contradiction Handling Requirement` | required disposition when evidence contradicts the initial expectation |
| `Claim Update Requirement` | required final claim-update statement |
| `EPISTEMIC_PROCESS_NA_WITH_REASON` | explicit not-applicable escape for mechanical or low-evidence work |

These fields must remain document/checker fields only.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Claude may create the new epistemic process
packet checker, add focused tests, and wire it into existing local hook/fast
gate surfaces only as needed for FPC-T3-C01. Claude may update the canonical
work-order template only for the FPC-T3-C04 epistemic block. Claude may apply
a narrow AOT trace-boundary repair if the new template section causes false
positive trace or manifest-delta failures. Claude must not change protected-path
definitions, session-state semantics, active handoff rules, core guard bypass
logic, or unrelated hook behavior.

Protected paths:

- `governance/compat/check_epistemic_process_packet.py`
- `governance/compat/test_check_epistemic_process_packet.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/test_run_local_governance_hook_chain.py`
- `governance/compat/test_run_worker_return_fast_gate.py`
- `governance/compat/test_check_markdown_structural_completeness.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `governance/compat/check_agent_operation_trace.py`
- `CVF_SESSION_MEMORY.md`

Self-protection rationale: this work intentionally creates and wires a new
governance checker under `governance/compat/`. Without this carrier, Claude
would be forced to synthesize protected-path authorization mid-task.

Rollback boundary: if the checker or wiring fails dispatch/return gates, revert
 only the FPC-T3-C04+C01 template/checker/test/hook edits, the narrow AOT
 trace-boundary repair, and the paired worker return. Do not revert unrelated
 operator or agent changes.

## Write Ownership

Claude may create or modify only:

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `governance/compat/check_epistemic_process_packet.py`
- `governance/compat/test_check_epistemic_process_packet.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/test_run_local_governance_hook_chain.py`
- `governance/compat/test_run_worker_return_fast_gate.py`
- `governance/compat/test_check_markdown_structural_completeness.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `governance/compat/check_agent_operation_trace.py`
- `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_WORKER_RETURN_2026-06-13.md`

Claude must not edit:

- `CVF_SESSION/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF*.md`
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
- public-sync clone files
- external Document Translator or Policy_Local trees
- runtime/provider/live-proof surfaces

## Implementation Requirements

### FPC-T3-C04 Template Update

Update the canonical work-order template with a bounded epistemic process block.
The block must:

- apply to high-evidence governed work orders;
- require expected-result/prediction evidence before worker execution;
- require contradiction handling and claim-update instructions;
- allow `EPISTEMIC_PROCESS_NA_WITH_REASON` for mechanical or evidence-light
  work;
- state that the block checks process structure only, not semantic truth.

### FPC-T3-C01 Checker

Create `governance/compat/check_epistemic_process_packet.py`.

Minimum behavior:

- scan changed governed markdown in worker returns and completion reviews;
- trigger on evidence-heavy execution vocabulary, including worker-return,
  completion, finding, claim, review, or evidence-update language;
- require structurally recognizable sections or table rows for expected result,
  actual evidence comparison, contradiction/gap disposition, and claim update;
- accept `EPISTEMIC_PROCESS_NA_WITH_REASON` only with an explicit reason;
- avoid triggering on purely mechanical docs, baseline-only dispatch docs, and
  low-evidence template maintenance unless the document claims evidence-heavy
  review or closure;
- report missing or wrong-block evidence with path-specific messages.

The checker must not attempt to score reasoning quality or semantic truth.

### Hook And Fast-Gate Wiring

Wire the checker into the local governance flow with the smallest useful scope:

- reviewer-fast is the primary target;
- pre-commit may inherit the checker through shared hook-chain structure only
  if that is the existing pattern;
- worker-return fast gate should pick it up through reviewer-fast. Modify
  `run_worker_return_fast_gate.py` only if necessary for testability or explicit
  command registration.

Do not add broad repo scans that materially slow unrelated mechanical work.

### Narrow AOT Trace-Boundary Repair

If required for this tranche to pass the existing Agent Operation Trace gate,
repair only these AOT checker boundaries:

- canonical work-order template files must not self-trigger trace requirements
  only because they contain worker-instruction vocabulary;
- manifest-delta validation should prefer complete `docs/reviews/` trace
  artifacts over dispatch work orders when both are present in the same batch.

This does not authorize deeper AOT hardening, new trace labels, protected-path
semantics changes, session-state edits, or public/runtime behavior changes.

### Tests

Add focused deterministic tests for:

- PASS: evidence-heavy packet contains all required epistemic process fields;
- FAIL: packet contains a generic PASS claim but omits the actual expected vs
  actual evidence comparison block;
- FAIL: packet contains evidence sections in the wrong block or wrong artifact
  type;
- PASS: `EPISTEMIC_PROCESS_NA_WITH_REASON` with explicit reason;
- FAIL: `EPISTEMIC_PROCESS_NA_WITH_REASON` without a reason;
- PASS: mechanical or low-evidence work avoids the checker;
- PASS: hook-chain/worker-return fast gate wiring remains stable;
- PASS: dispatch-quality tests accept this work order's protected-path carrier.

## Execution Plan

1. Complete Required First Reads and Pre-Flight Checks.
2. Run the negative search and record collisions in the worker return.
3. Update the canonical work-order template with the narrow epistemic block.
4. Implement `check_epistemic_process_packet.py` with structural-only checks.
5. Add focused checker fixtures covering pass, fail, NA, and false-positive
   behavior.
6. Wire the checker into reviewer-fast with the smallest useful scope.
7. Update worker-return fast gate or related tests only if the existing
   reviewer-fast delegation does not exercise the new checker.
8. Run focused tests and worker-return gates.
9. Create the worker-return packet with Agent Operation Trace Block and actual
   pending worktree evidence.
10. Return uncommitted artifacts to Codex.

## Evidence Requirements

Claude must record:

- execution base HEAD;
- pre-work and post-work `git status --short`;
- negative search command and collision disposition;
- focused pytest command and result;
- worker-return fast gate command and result;
- changed-file manifest with expected/actual/delta fields;
- explicit `EPISTEMIC_PROCESS_NA_WITH_REASON` false-positive evidence;
- any blocker with `BLOCKED_*` disposition and return-to-orchestrator action.

No evidence may rely on provider-specific memory files as CVF authority.

## Acceptance Criteria

- The work-order template contains a bounded high-evidence epistemic block.
- The checker enforces expected-result, evidence-comparison,
  contradiction/gap disposition, and claim-update structure for triggered
  evidence-heavy packets.
- The checker accepts `EPISTEMIC_PROCESS_NA_WITH_REASON` only with a reason.
- The checker does not trigger on mechanical or evidence-light work fixtures.
- Reviewer-fast or equivalent local hook placement runs the checker.
- Focused tests for checker and touched hook/fast-gate behavior pass.
- Worker return includes Agent Operation Trace Block and Worker Pending-Return
  Gate evidence.
- Any AOT checker edit is limited to template self-trigger prevention and
  review-packet manifest-delta candidate selection, with AOT regression tests
  passing.
- No forbidden scope is touched.

## Review Gate

Codex must review the worker return before any commit. Reviewer-fast must pass
before Codex accepts the pending artifacts. Codex owns the completion review,
committed-range pre-closure gate, and session continuity sync if the worker
return is accepted.

## Operator Checkpoint

No operator checkpoint is required for Claude to implement the allowed
template/checker/test/hook tranche. A new operator checkpoint is required before
registry mutation, OS/endpoint audit configuration, agent computer-control
changes, public-sync, runtime/provider/live proof, external app mutation,
FPC-T4, or broader checkpoint policy changes.

## Roadmap-to-Work-Order Trace Matrix

| Source requirement | Source evidence | Work-order instruction | Acceptance evidence |
| --- | --- | --- | --- |
| Implement C04 before or with C01 | FPC-T3 coverage plan line 316 | Template update plus checker in one tranche | template diff and checker tests |
| C01 must define process-packet output signal before C05 registry viability | FPC-T2 matrix line 497 | checker enforces structural expected/actual/claim-update evidence | focused checker tests |
| Avoid over-tightening | operator instruction and FPC-T3 false-positive note | NA escape plus mechanical-work false-positive tests | focused false-positive tests |
| Keep co_work under CVF supervision, not product development | AOT standard and operator boundary | trace and manifest evidence only; no provider feature work | worker return trace block |
| Protect guarded paths | template section 7A and dispatch checker | Core Guard Self-Protection Authorization block | dispatch-quality gate PASS |

## Worker Autonomy / No-Question Rule

Any gate failure inside the Allowed Artifact Set must be repaired and rerun by
Claude before return. Claude must ask the operator only when repair would exceed
Allowed scope, change the claim boundary, require session-state or handoff
mutation, require registry mutation, configure OS/endpoint controls, consume
provider quota/secrets, run live proof, touch public-sync, inspect external app
source, or perform destructive or irreversible actions.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_FOR_CLAUDE_2026-06-13.md`
- `docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md`
- `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

pendingStatusTokensAllowedBeforeReview:
COMPLETE_PENDING_REVIEW, IMPLEMENTATION_COMPLETE_PENDING_REVIEW, DRAFT, HOLD_*

closedEquivalentResidueDisposition:
Codex owns conversion from worker pending return to closure. Claude must not
mark this work order or worker return `CLOSED`, `CLOSED_PASS`, or
`CLOSED_PASS_BOUNDED`.

## Worker Pending-Return Gate

Claude must include this table in the worker-return packet:

| Gate | Applies when | Command or evidence | Worker result |
| --- | --- | --- | --- |
| Execution anchor | every worker run | `git rev-parse --short HEAD` before edits | `executionBaseHead=<hash>` |
| Pending worktree | every no-commit return | `git status --short` | actual pending file list |
| Protected roadmap directory check | every worker run | `Test-Path docs/roadmaps`; `git status --short -- docs/roadmaps` | `PASS` or `BLOCKED_PROTECTED_PATH_VISIBILITY_INCIDENT` |
| Focused tests | checker/template/hook changes | `python -m pytest governance/compat/test_check_epistemic_process_packet.py governance/compat/test_run_local_governance_hook_chain.py governance/compat/test_run_worker_return_fast_gate.py -q` | `PASS` or `BLOCKED` |
| Worker-return fast gate | every no-commit return | `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_epistemic_process_packet.py` | `PASS` or `BLOCKED` |
| Markdown structural completeness | changed governed markdown | `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or `BLOCKED` |
| Finding-To-Governance learning | worker-return findings | `python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or `BLOCKED` |
| Agent operation trace | changed work order / worker return | `python governance/compat/check_agent_operation_trace.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or `BLOCKED` |
| Diff hygiene | every worker run | `git diff --check` | `PASS` or `BLOCKED` |

Claude must not claim committed-range pre-closure PASS.

## Required Deliverables

Claude must return uncommitted artifacts including:

1. template update;
2. checker implementation;
3. focused tests;
4. hook/fast-gate wiring if required by the implementation;
5. worker-return packet with Agent Operation Trace Block and Worker Pending-Return Gate.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex CLI |
| Session or invocation | dispatchBaseHead `0101eddf` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | repo-local file creation through Codex apply_patch |
| Target paths | `docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_FOR_CLAUDE_2026-06-13.md` |
| Allowed scope source | operator authorization in chat plus FPC-T3 coverage plan |
| Before status evidence | `git status --short` clean before dispatch packet creation |
| After status evidence | pending dispatch packet files in `git status --short` |
| Diff evidence | `git diff --name-status` after packet creation |
| Approval boundary | operator authorized Codex to proceed with the recommended FPC-T3-C04+C01 work order for Claude |
| Claim boundary | repo-local trace only; no OS/user attribution or endpoint telemetry claim |
| Agent type | Codex |
| Invocation ID | `dispatchBaseHead=0101eddf` |
| Expected manifest | `docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_FOR_CLAUDE_2026-06-13.md` |
| Actual changed set | `docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_FOR_CLAUDE_2026-06-13.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatch creates new governed packet files and deletes or renames no protected path |

## Forbidden Scope

This work order authorizes no registry edit, FPC-T2 C01-C04 registry mutation,
FPC-T2 C05 registry entry, FPC-T4, AOT deeper hardening, session-state edit,
active handoff edit, front-door edit, public-sync, runtime/provider/live proof,
external Document Translator inspection or mutation, Policy_Local inspection or
mutation, OCR/provider/API use, retrieval route wiring, corpus ingestion, T12,
OS audit installation, Sysmon installation, endpoint monitoring, file watcher
service, destructive broker, agent computer-control permission change,
readiness/cost/quality claim, raw memory release, high-risk promotion, or
autonomous mutation.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all allowed artifacts are complete,
all focused tests pass, worker-return fast gate evidence is recorded, the
Agent Operation Trace Block is complete, and artifacts remain uncommitted.

Return `BLOCKED_SCOPE_EXPANSION` if useful progress requires a forbidden path
or action.

Return `BLOCKED_OVERCONSTRAINT_RISK` if the only viable checker design would
force every governed artifact, trivial mechanical fix, or low-evidence note to
carry epistemic process fields.

## Closure Checklist

- [x] GC-018 baseline exists.
- [x] Source Verification Block is present.
- [x] New Doc-Only Fields are separated from Source Verification ACCEPT rows.
- [x] Roadmap-to-Work-Order Trace Matrix is present.
- [x] Protected-path carrier is present for `governance/compat/*.py` scope.
- [x] Worker Pending-Return Gate is defined.
- [x] Agent Operation Trace Block is present.
- [x] Forbidden Scope excludes runtime/provider/public/OS/control expansion.
- [x] Codex reviewer accepted the narrow AOT trace-boundary repair as bounded
      false-positive remediation, not broader AOT hardening.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED`; `docType: completion_review` | PASS |
| Roadmap state | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `Status: FPC_T3_C04_C01_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A | `N/A with reason: no registry JSON edit authorized or performed` | PASS |
| Registry Markdown | N/A | `N/A with reason: no registry Markdown edit authorized or performed` | PASS |
| External evidence digest | N/A | `N/A with reason: no external evidence digest authorized or produced` | N/A with reason |
| System loop interlock | N/A | `N/A with reason: no interlock registry entry authorized or performed` | PASS |
| Session continuity | reviewer-owned post-material sync | `PENDING_SESSION_SYNC_AFTER_MATERIAL_COMMIT` | PASS |
| GC-018 baseline | `docs/baselines/CVF_GC018_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_WORKER_RETURN_2026-06-13.md` | `Status: WORKER_RETURN_SUBMITTED_UNCOMMITTED` | PASS |
| Closure trace | completion review | `Manifest delta: MATCH` | PASS |
| Public export | this file and completion review | `DEFERRED_PRIVATE_ONLY` | PASS |

## Claim Boundary

This work order authorizes structural governance evidence controls only. A
passing implementation may prove that required evidence sections exist in the
right kind of packet. It does not prove semantic correctness, reasoning quality,
provider quality, production readiness, public readiness, OS-level attribution,
endpoint telemetry, or autonomous mutation safety.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control work order. Public-sync is not
authorized by this tranche.
