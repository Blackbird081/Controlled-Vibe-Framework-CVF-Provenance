# CVF Agent Work Order - SOT3-RCS-T1 Review Cost Systemization

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Work Order ID: SOT3-RCS-T1-WO

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `db99f4ebd`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: no-commit governance checker worker.

Canonical packet: this work order and paired GC-018 baseline.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture HEAD and full status before edits.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Current-time notes: SOT3-RAP-T0 is accepted at `d394b6018`; T1 packet
authoring is released, but no runtime/provider/public work is authorized.

Do-not-misread notes: enforce evidence shape, not semantic truth, reviewer
quality, criticality, or automatic stop decisions.

Required first actions: read startup surfaces, roadmap, GC-018, this work
order, ADIF-0026, reviewer guidance, checker precedents, tests, and hook catalogs;
capture execution HEAD/status; run pre-implementation.

Return contract: exactly eight planned outputs, one
`COMPLETE_PENDING_REVIEW` return, unchanged HEAD, and no commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-RCS-T1 --title "Review Cost Systemization" --date 2026-07-12 --base db99f4ebd --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit governance-checker worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added source verification, telemetry contract, round-three rule, hook wiring, handoff, and protected-path authorization. |
| checkerReadAheadConfirmation | dispatch-quality, structural, scaffold, core-guard, handoff, worker-return, and file-size checkers |
| docOnlyNewFields | review-cost declaration and stop-disposition vocabulary |
| claimBoundary | dispatch only; no checker behavior or semantic-value proof |

## Purpose

Implement the bounded SOT3-RCS-T1 review-cost evidence-shape standard and
forward-only checker authorized by the paired baseline.

## Target / Source

Roadmap: `docs/roadmaps/CVF_SOT3_REVERSE_ARCHITECTURE_PROJECTION_AND_REVIEW_COST_SYSTEMIZATION_ROADMAP_2026-07-12.md`.

Baseline: `docs/baselines/CVF_GC018_SOT3_RCS_T1_REVIEW_COST_SYSTEMIZATION_2026-07-12.md`.

## Scope / Methodology

Author the reference contract first, implement a narrow checker from that
contract, add focused tests for applicability and stop rules, wire the checker
into three existing hook catalogs, and return without committing.

## Authority Chain

- operator continuation after T0 closure;
- roadmap dependency order;
- T0 accepted material `d394b6018`;
- ADIF-0026 reviewer-cost guidance;
- paired GC-018 and this work order.

## Agent Roles

Operator authorizes scope; dispatcher owns source fidelity; worker implements
without commit; reviewer/closer independently validates semantics and commits.

## Worker Autonomy / No-Question Rule

Repair in-scope test or checker defects autonomously. Stop only for source
drift, a required new protected path, semantic-value automation pressure, or
scope expansion.

## Required First Reads

1. startup/session front doors and active handoff;
2. Guard Orientation and governed-artifact literal gotchas;
3. roadmap, paired baseline, and this work order;
4. ADIF-0026 and accepted T0 completion review;
5. worker-experience checker/tests and three hook catalogs;
6. core-guard, file-size, structural, and worker-return checker sources.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | CVF-owned ADIF-0026 and accepted T0 completion evidence |
| Scope classification | INTERNAL_GOVERNANCE_HARDENING |
| Intake role | no-commit checker worker |
| Risk sensitivity | HIGH: checker overreach could block valid reviews |
| Provider surface | provider-neutral local role; no provider authority |
| Reviewer role | independently validate applicability and semantic boundary |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | semantic scoring, new protected path, or scope expansion |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> checker worker -> reviewer/closer |

## Allowed Scope

Exactly the eight paths/classes in the baseline Planned Artifact Manifest.

## Forbidden Scope

SOT3 runtime/schema/package work, Catalog/GAP edits, session/handoff edits,
provider/live calls, public-sync, Web/UI, broad reviewer scoring, token
estimation, or changes to autorun orchestration outside the three catalogs.

## Source Verification Block

The paired baseline Source Verification Block is incorporated by exact path.
The worker must re-open each source before editing.

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| eight telemetry signals are canonical guidance | VALUE_SET | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Remediation signal table | `reviewRoundCount`; `valueDelta` | ADIF-0026 | ACCEPT |
| round-three escalation rule exists | LITERAL_INVARIANT | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Mandatory stop control item 2 | `REVIEW_COST_ESCALATION_REQUIRED` | ADIF-0026 | ACCEPT |
| applicability must be narrow | RUNTIME_BEHAVIOR | `governance/compat/check_worker_experience_retrospective.py` | eligibility function | `is_eligible_worker_return` | checker precedent | ACCEPT |
| hook command lists are locally owned | EXISTS | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | catalog declaration | `REVIEWER_FAST_CHECKS` | reviewer-fast catalog | ACCEPT |
| hook command lists are locally owned | EXISTS | `governance/compat/local_governance_hook_catalog_pre_commit.py` | catalog declaration | `PRE_COMMIT_CHECKS` | pre-commit catalog | ACCEPT |
| hook command lists are locally owned | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | catalog declaration | `PRE_PUSH_CHECKS` | pre-push catalog | ACCEPT |

## New Doc-Only Fields

| Field | Meaning |
|---|---|
| `Review-Cost Telemetry: REQUIRED` | declaration-shape applicability marker for a changed completion review |
| `stopDisposition` | bounded reviewer route token; not a semantic score |

## Required Review-Cost Contract

The standard and checker must require these fields in an applicable changed
completion review:

- `reviewRoundCount`
- `workerRepairTurnCount`
- `newRootCauseCountThisRound`
- `dependentFindingCountThisRound`
- `elapsedReviewMinutes`
- `providerCallCount`
- `tokenOrQuotaUsage`
- `valueDelta`
- `stopDisposition`

Numeric fields accept a non-negative integer or an explicit unavailable reason
only where ADIF-0026 permits unavailable evidence. `valueDelta` must be a
non-empty reviewer statement, not an automatically scored number.

Allowed `stopDisposition` values:

- `CONTINUE_NEW_CRITICAL_EVIDENCE`
- `CONSOLIDATE_SINGLE_REPAIR`
- `PARK_LOW_INCREMENTAL_VALUE`
- `COMPLETE_REVIEW`
- `REVIEW_COST_ESCALATION_REQUIRED`

If `reviewRoundCount >= 3`, only `REVIEW_COST_ESCALATION_REQUIRED` or
`CONTINUE_NEW_CRITICAL_EVIDENCE` is accepted. The checker must not decide
whether the evidence is truly critical.

## Applicability Boundary

Forward-only changed `docs/reviews/*.md` completion reviews opt in through an
exact standalone declaration `Review-Cost Telemetry: REQUIRED`. The checker
must not trigger on quoted/backticked markers in standards, baselines, work
orders, tests, or its own source. Tests must cover both true declaration and
quoted-marker non-applicability.

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | governed Markdown and local checker CLI | may write only allowed local paths; no commit by worker | worker return and checker output | direct local process only |
| EXTERNAL_AGENT_CLI_MCP | external worker candidate | same work-order packet and CLI command shape | no external provider authority and no MCP/runtime integration claim | returned files must be revalidated locally | NOT_IMPLEMENTED_WITH_REASON: separate adapter authorization required |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durable family | `docs/reference/review_cost_control/` |
| stable front door | `docs/reference/review_cost_control/README.md` |
| canonical owner | undated standard in the same family |
| generated aggregate | NOT_APPLICABLE_WITH_REASON: two-file reference family, no aggregate |
| index/update route | family README updated in the same worker batch |
| claim boundary | storage layout only; no runtime or public owner claim |

## ADIF Defect Registry Disclosure

Query:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Direct mandatory source: ADIF-0026.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit checker worker -> reviewer/closer |
| phase | SOT3-RCS-T1 review-cost systemization |
| contractSource | canonical archive-qualified contract citation immediately above |
| baseHeadFor(phase) | dispatch=`db99f4ebd`; execution=worker-captured HEAD; closure=reviewer-captured base |
| changedSetScope(phase) | exactly eight planned outputs |
| traceScope(phase, actor) | contract, checker, tests, hook wiring, gates, status, no-commit evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | no SOT3 runtime, Catalog/GAP, session, provider, or public paths |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_SOT3_RCS_T1_COMPLETION_REVIEW_2026-07-12.md`

reviewerOwnedClosurePaths: completion review and accepted eight-path material;
continuity only in a separate session-sync commit.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence |
|---|---|---|
| recompute T0 value/cost | use accepted T0 0-round/0-live evidence as bounded input | standard rationale and worker return |
| machine-enforce only narrow shape | required field and escalation validation | checker tests |
| semantic judgment remains reviewer-owned | forbid semantic scoring | standard claim boundary and negative tests |
| T1 separate from T0 | exactly eight new/changed T1 paths | git status and operation trace |

## Execution Plan

1. Capture execution HEAD/status and run pre-implementation.
2. Write the standard/front door with declaration, field, vocabulary,
   applicability, stop, and claim-boundary rules.
3. Implement the forward-only checker without semantic scoring.
4. Add focused tests for valid first pass, missing fields, invalid values,
   round-three escalation, quoted-marker non-trigger, and historical exclusion.
5. Wire the checker into reviewer-fast, pre-commit, and pre-push catalogs.
6. Run focused tests, reviewer-fast, worker-return fast gate, diff/status, and
   return without commit.

## Write Ownership

Worker owns exactly eight planned outputs. Reviewer owns completion review,
accepted material commit, and separate session sync.

## Core Guard Self-Protection Authorization

Operator authorization: continue into the roadmap-authorized T1 governance
hardening after accepted T0 and machine-enforce only review-cost evidence shape.

Protected paths authorized for this worker batch:

- `governance/compat/check_review_cost_control.py`
- `governance/compat/test_check_review_cost_control.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`

Rollback boundary: revert only the T1 checker, tests, catalogs, and matching
standard/front-door/worker-return batch; retain T0 closure `d394b6018`.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python -m pytest governance/compat/test_check_review_cost_control.py -q
python governance/compat/check_review_cost_control.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Review Gate

Reviewer independently reads checker semantics and tests, adds adversarial
fixtures for any missing applicability/round boundary, runs the full committed
pre-closure range, and rejects any semantic-scoring behavior.

## Evidence Requirements

Exact eight-path status, unchanged worker HEAD, focused test counts, direct
checker output, reviewer-fast and worker-return fast-gate output, hook-catalog
diffs, file-size PASS, and explicit no-live/no-runtime evidence.

## Acceptance Criteria

- the standard owns all nine fields and five stop tokens;
- checker applicability is exact declaration-shape and forward-only;
- round-three rule is deterministic and tested;
- semantic root-cause/value classification remains reviewer-owned;
- all three catalogs invoke the checker;
- worker returns without commit and all gates pass.

## Operator Checkpoint

No checkpoint is needed for the exact shape-only implementation. Stop if the
work requires semantic scoring, automatic criticality judgment, provider/live
usage capture, another protected path, or a broader hook/orchestrator change.

## Closure Checklist

- [ ] standard and front door are complete;
- [ ] checker is forward-only and declaration-shaped;
- [ ] all nine fields and five stop tokens are tested;
- [ ] round-three rule is tested;
- [ ] quoted marker does not trigger;
- [ ] three hook catalogs are wired;
- [ ] no semantic scoring, live calls, or forbidden paths;
- [ ] worker HEAD unchanged and no commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
or `BLOCKED_WITH_REASON`; never a closed-equivalent worker status.

## Worker Return Conditions

Return only after all verification commands pass or one source-backed blocker
is recorded. Do not commit.

## Return / Escalation Conditions

Escalate a required semantic-value classifier, new hook/orchestrator path,
source drift, or scope expansion. Repair owned checker/test defects directly.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Reviewer Closure Conversion; Roadmap-to-Work-Order Trace Matrix; Core Guard Self-Protection Authorization; Public Export Disposition |
| gateRunPurpose | confirm source-derived dispatch and protected-path authorization before implementation |
| claimBoundary | machine gates do not establish semantic review quality or value |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-RCS-T1 packet authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, ADIF resolver, apply_patch, pre-dispatch gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator continuation after accepted T0 and roadmap T1 release condition |
| Before status evidence | HEAD `db99f4ebd`; clean worktree; T0 accepted |
| After status evidence | T1 implementation packet authored; worker execution remains gated by pre-dispatch |
| Diff evidence | exact two-path dispatch packet diff before commit |
| Approval boundary | packet authoring and bounded checker dispatch only |
| Claim boundary | no checker implementation proof, semantic scoring, runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-rcs-t1-dispatch-authoring-2026-07-12` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | CVF-owned accepted learning -> local governance standard -> bounded shape checker |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | review-cost-control reference family and local checker catalogs |
| Disposition | NOT_APPLICABLE_WITH_REASON: no new external knowledge is ingested |
| Claim boundary | internal governance hardening only; no external source authority or runtime import |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening packet.

## Claim Boundary

This work order authorizes one bounded no-commit checker implementation. It
does not automate semantic review value, consume live quota, or implement SOT3.
