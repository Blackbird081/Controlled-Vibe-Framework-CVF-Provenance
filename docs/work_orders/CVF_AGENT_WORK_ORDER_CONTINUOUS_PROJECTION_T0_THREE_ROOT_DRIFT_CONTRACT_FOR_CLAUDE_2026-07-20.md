# CVF Agent Work Order Continuous Projection T0 Three-Root Drift Contract For Claude

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: CVF-CONTINUOUS-PROJECTION-T0

Dispatch base head: `0145218a2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: delegated source-audit worker.

Canonical packet: this work order and its paired GC-018 baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture the committed dispatch/session-sync HEAD and require
an initially clean worktree.

Current-time notes: Web UX bounded closure `d757fe5ac` satisfies the roadmap's
T0 reopen condition; mapper implementation already exists and must not be
rewritten in T0.

Do-not-misread notes: audit and contract definition only. Do not edit scripts,
policy, tests, cvf-web, either repository root, roadmap, registry, or session.

Required first actions: read startup front doors, guard orientation, literal
gotchas, `DESIGN.md` for audience terminology, paired baseline, roadmap, mapper,
policy, focused tests, prior T2 closure, and cited checkers. Run the mandatory
pre-implementation autorun gate before either output is written.

Return contract: leave exactly two outputs uncommitted and return
`ACCEPTED_BY_REVIEWER_WITH_REPAIRS` after independent closure recomputation.

## Purpose

Produce the terminal T0 contract that maps each governed projection surface to
its semantic owner, target, evidence class, audience, drift disposition, and
review owner across provenance, public-sync, and cvf-web. The result must let a
later T1 work order extend the mapper without guessing or conflating freshness
with presentation quality.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T0 --title "Continuous Projection Three-Root Drift Contract Baseline" --date 2026-07-20 --base 0145218a2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | roles, verified sources, exact scope, roadmap trace, outputs, evidence, and closure routing |
| checkerReadAheadConfirmation | dispatch-quality, handoff, worker-return, machine-closure, public-disposition, file-size, and autorun checkers |
| docOnlyNewFields | `semanticOwner`, `projectionTarget`, `evidenceClass`, `audience`, `driftDisposition`, and future receipt proposals |
| claimBoundary | dispatch authoring provenance only |

## Authority Chain

Operator instruction -> Web UX closure -> continuous-projection roadmap ->
paired GC-018 -> this work order -> no-commit worker -> independent reviewer.

## Agent Roles

Dispatcher owns this packet. Worker owns exactly two review outputs.
Independent reviewer/closer owns evidence recomputation, closure edits,
material commit, roadmap release, and session sync.

## Required First Reads

- `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md`
- `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_2026-07-20.md`
- `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md`
- `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md`
- `scripts/get_cvf_projection_map.ps1`
- `scripts/cvf_projection_policy.json`
- `scripts/test_get_cvf_projection_map.ps1`
- `DESIGN.md`

## Pre-Flight Checks

Confirm executionBaseHead, clean worktree, exact remote identities, existence of
the provenance root, sibling public-sync root, and cvf-web root, and all cited
sources. Run pre-implementation autorun before edits. A dirty foreign root,
missing authority, or source contradiction returns `BLOCKED_WITH_REASON`.

## Write Ownership

Worker may write only the two Allowed paths. The worker must not stage or
commit. Reviewer-owned closure paths remain forbidden to the worker.

## Scope / Target / Owner Boundary

Allowed paths:

1. `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md`
2. `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_WORKER_RETURN_2026-07-20.md`

Every other path is forbidden for mutation, including all source, policy,
test, Web, public-sync, roadmap, baseline, work-order, registry, and session
surfaces.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| Web UX acceptance | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` | `d757fe5ac` | PASS |
| read-only mapper foundation | `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md` | `5df0c6f77` | PASS |
| T0 authoring session release | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `0145218a2` | PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| mapper accepts three explicit roots | EXISTS | `scripts/get_cvf_projection_map.ps1` | parameter block, lines 65-79 | `ProvenanceRoot` | mapper parameter contract | ACCEPT |
| candidate actions are classification labels only | LITERAL_INVARIANT | `scripts/get_cvf_projection_map.ps1` | description, lines 21-28 | `FLAG_SEMANTIC_REVIEW_CHANGED` | mapper action vocabulary | ACCEPT |
| policy parity inspection owner exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 249-328 | `Get-PolicyParityReport` | mapper policy parity read model | ACCEPT |
| cvf-web observation owner exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 330-376 | `Get-CvfWebObservation` | mapper Web observation read model | ACCEPT |
| invalid roots fail closed | RUNTIME_BEHAVIOR | `scripts/get_cvf_projection_map.ps1` | main validation, lines 388-425 | `DIRTY_PROVENANCE_ROOT` | mapper validation path | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | semanticReviewBoundary, lines 138-141 | `autoApproveForbidden` | projection policy schema | ACCEPT |
| focused deterministic proof exists | EXISTS | `scripts/test_get_cvf_projection_map.ps1` | repeated-run assertions, lines 440-441 | `deterministic_repeated_run_receipt_id` | focused mapper proof suite | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
|---|---|---|
| `semanticOwner` | canonical source owner for a projected fact | DOC_ONLY_NEW |
| `projectionTarget` | public-sync or cvf-web destination | DOC_ONLY_NEW |
| `evidenceClass` | source, hash, browser, or reviewer evidence class | DOC_ONLY_NEW |
| `audience` | end user, developer, external agent, or reviewer | DOC_ONLY_NEW |
| `driftDisposition` | terminal T0 classification | DOC_ONLY_NEW |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Output evidence | Disposition |
|---|---|---|---|
| reconcile three roots | direct root, remote, status, owner, and target inspection | root evidence section and terminal rows | PASS |
| define five contract dimensions | populate all fields for every mapped surface | terminal contract table | PASS |
| pin accepted landmarks and hashes | cite commits and secret-free stable hashes | landmark table | PASS |
| separate audiences | apply the four-audience contract without flattening depth | audience coverage table | PASS |
| preserve read-only boundary | prove exact two-path diff and unchanged roots | worker-return evidence | PASS |

## Required Implementation

Create a ledger containing:

1. a three-root identity table with repository role, current origin, clean/dirty
   observation, semantic authority, and mutation prohibition;
2. a landmark table for the mapper foundation, Web UX closure, projection
   policy, and current source hashes where stable and secret-free;
3. terminal rows for every mapped surface, each populated with
   `semanticOwner`, `projectionTarget`, `evidenceClass`, `audience`, and
   `driftDisposition`;
4. one of `CURRENT`, `MISSING_TARGET`, `STALE_TARGET`,
   `AUDIENCE_PRESENTATION_RISK`, `SEMANTIC_REVIEW_REQUIRED`,
   `NOT_APPLICABLE_WITH_REASON`, or `SOURCE_AUTHORITY_BLOCKED` for every row;
5. explicit separation of source freshness, semantic equivalence, hosted
   freshness, and audience presentation acceptance;
6. a proposed T1 read-only receipt schema, deterministic ordering rules,
   negative cases, manual/CI/scheduled seams, and reviewer ownership;
7. reconciled row totals and a T1 release recommendation that cannot authorize
   implementation by itself.

Do not run the mapper against a dirty real root merely to obtain a receipt. T0
may inspect read-only state and reuse accepted proof; it must fail closed on
unsafe prerequisites.

## Acceptance Criteria

- Every seed and discovered governed projection surface has one terminal row.
- All five contract dimensions are non-empty on applicable rows.
- File/hash freshness is not claimed as semantic or presentation equivalence.
- End-user, developer, external-agent, and reviewer needs remain distinct.
- T1 schema and failure cases are source-backed or marked doc-only new.
- No script, policy, test, Web, public-sync, roadmap, registry, or session path
  changes.

## Execution Plan

Capture preflight evidence; inspect roots and sources; build and reconcile the
terminal matrix; define the bounded T1 contract; run worker-fast and file-size;
record exact diff, staged state, and unchanged HEAD; return without commit.

## Evidence Requirements

Record commands without secrets, source line/section, current origin identities,
stable hashes, terminal row totals by disposition/audience/evidence class,
negative cases, exact changed set, empty staged set, and unchanged HEAD.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, missing root or authority,
dirty foreign worktree that prevents safe evidence, required forbidden-path
mutation, or a non-terminal row. Do not invent a corrected source contract.

## Operator Checkpoint

N/A with reason: the operator authorized continuous work-order progression
after review; T0 remains a read-only no-commit worker tranche.

## Worker Autonomy / No-Question Rule

Repair formatting and evidence defects inside the two Allowed paths. Do not ask
for permission to fix allowed-scope defects. Return only on the explicit blocker
conditions above.

## Negative Search And Collision Discipline

Before using `SOURCE_AUTHORITY_BLOCKED`, search the provenance source, policy,
tests, governed reviews, and the sibling public-sync root for the exact claimed
surface and likely aliases. Record query, scope, zero-result evidence, and
collision handling in the ledger. A missing term in one file is not sufficient
evidence, and a similarly named path must not be promoted without source-owner
confirmation.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | repository-local three-root projection contract audit |
| scope classification | read-only source and repository-state inspection |
| risk sensitivity | R1; documentation outputs only |
| escalation condition | source contradiction, missing authority, unsafe dirty root, or forbidden mutation need |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | no-commit worker -> independent reviewer/closer |

## Review Gate

Reviewer independently recomputes root identities, hashes, row totals, source
citations, audience separation, and T1 contract fields before any later
implementation packet may be authored.

## Closure Checklist

- [x] Exactly two worker outputs exist.
- [x] Every contract row is terminal and reconciled after reviewer repair.
- [x] Root identity and no-mutation evidence are command-backed.
- [x] Worker-fast and file-size pass.
- [x] Nothing was staged or committed by the worker.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> independent reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`0145218a2`; executionBaseHead=worker captures final dispatch/session-sync HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exactly two review outputs |
| traceScope(phase, actor) | base, source reads, root observations, rows, totals, commands, diff, staged state, and no-commit evidence |
| commitOwner(phase) | independent reviewer/closer; worker forbidden |
| crossBatchIsolation | initially clean provenance worktree required; foreign changes block execution |
| nextMoveSurfaces | reviewer/session-sync steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_COMPLETION_REVIEW_2026-07-20.md` |
| reviewerOwnedClosurePaths | paired baseline, this work order, roadmap, completion review, and session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`continuous projection three-root baseline audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection three-root baseline audit" --role dispatcher --lifecycle-phase pre-dispatch --json`

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside source is absorbed |
| Matching local-view guard | N/A with reason: direct current source is the authority |
| Owner surface | continuous-projection roadmap and future mapper contract |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | external-agent audience is a consumer class, not an authority source |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and evidence for the T0 no-commit source-audit dispatch |
| claimBoundary | checker compliance confirms packet structure only |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | `docs/reviews/` audit ledger and worker return |
| Storage decision | reuse established dated review locations; no new foundation directory |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | T0 defines a contract in review evidence only; a later implementation requires a fresh packet |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
```

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | T0 completion review | reviewer-accepted bounded with repairs | PASS |
| Roadmap state | continuous-projection roadmap | T0 closed bounded; T1 packet authoring next | PASS |
| Registry JSON | existing GC-051 aggregate | generator drift check passed; no source entry change required | PASS |
| Registry Markdown | existing GC-051 front door | reviewer-fast corpus coverage check passed; no entry change required | PASS |
| External evidence digest | N/A with reason: repository-local roots only | no imported bundle | N/A with reason |
| System loop interlock | N/A with reason: no interlock owner changed | no mutation | N/A with reason |
| Session continuity | protected continuity surfaces | separate post-material sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| T0-REAL-ROOT-RECEIPT | T0 ledger evidence-gap section | N/A with reason: no receipt JSON was emitted | no real-root freshness receipt accepted in T0 | no receipt produced | PASS |

## Current Runtime Freshness Verification

Current mapper source, policy source, mapped-file pairs, public-sync tracked
state, ignored residue, and cvf-web SOT3 identifiers were recomputed during
closure. Commands include `rg -n "Get-AllowGroupMatch|Get-CandidateRow|Get-PolicyParityReport" scripts/get_cvf_projection_map.ps1`, direct policy
read, `git ls-files`, `git check-ignore -v`, `Get-FileHash -Algorithm SHA256`,
and direct package/registry searches. No runtime implementation or completed
real-root receipt is claimed. Disposition: PASS_BOUNDED.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | continuous-projection T0 dispatch, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold helper, apply_patch, governed gates |
| Target paths | roadmap, paired baseline, this work order |
| Allowed scope source | operator continuation instruction and Web UX closure |
| Before status evidence | clean worktree at HEAD `0145218a2` |
| After status evidence | exact three-path dispatch batch pending commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T0 documentation audit dispatch only |
| Claim boundary | no implementation, root mutation, public action, or provider call |
| Agent type | dispatcher |
| Invocation ID | `continuous-projection-t0-dispatch-2026-07-20` |
| Expected manifest | roadmap, paired baseline, this work order |
| Actual changed set | roadmap, paired baseline, this work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | three-root contract audit |
| claimDisposition | N/A with reason: no execution-control implementation |
| receiptEvidence | N/A with reason: T0 proposes future receipt fields only |
| actionEvidence | N/A with reason: source and targets remain read-only |
| invocationBoundary | no-commit documentation worker |
| interceptionBoundary | no provider, IDE, runtime, or wrapper interception |
| claimLanguage | inspect, map, classify, reconcile, and propose only |
| forbiddenExpansion | implementation, semantic edit, apply, commit, push, deploy, public-sync mutation, provider/live, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T0 is a private provenance audit and creates no public-safe export.

## Claim Boundary

This work order authorizes exactly two documentation outputs. It does not
authorize mapper changes or execution on an unsafe root, automatic semantic
decisions, Web/source mutation, commit, push, deployment, public-sync mutation,
provider/live calls, production action, or unattended mutation.
