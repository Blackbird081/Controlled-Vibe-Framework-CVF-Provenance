# CVF Agent Work Order LPCI1 Web Context-To-LLM Intake R3 PATH_RE Repair

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-08-09

docType: work_order

Batch ID: LPCI1-WEB-CONTEXT-TO-LLM-INTAKE-R3-PATH-RE-REPAIR

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 95340497fe4ca835ee85d44f311f651632b9c606

executionBaseHead: 95340497fe4ca835ee85d44f311f651632b9c606

closureBaseHead: N/A_PENDING_REVIEWER_COMMIT

## Dispatch Prompt Envelope

Role: bounded checker-maintenance worker; the root reviewer remains independent reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `95340497fe4ca835ee85d44f311f651632b9c606`.

Current-time notes: the two intake docs were already untracked; the first
pre-implementation gate failed 75/77 on corpus block shape, then passed after
the allowed repair. No provider/live/network action is authorized.

Do-not-misread notes: repair only active `PATH_RE`; do not edit the duplicate
monolithic regex, widen roots, weaken file existence validation, stage, or
commit. Never use the roadmap as `dispatchWorkOrder`.

Required first actions: read startup/state/handoff, guard orientation, literal
gotchas, Core Guard rules, this packet, checker and focused test in full; run
the ADIF query and lifecycle gates.

Return contract: `COMPLETE_PENDING_REVIEW` or exact governed blocker with
manifest, test counts, gates, R3 ledger, and `WORKER_MUST_NOT_COMMIT`.

## Purpose

Repair balanced parenthesized repo-path extraction and complete the bounded R3
semantic corrections in the paired intake roadmap and worker return.

## Authority Chain

- `AUTHORIZE_FRESH_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_ROADMAP_DOCUMENTATION_ONLY`
- `AUTHORIZE_BOUNDED_PATH_RE_PARENTHESIZED_SOURCE_PATH_CHECKER_REPAIR`
- GC-018: `docs/baselines/CVF_GC018_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md`.
- Roadmap: `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md`.
- Active handoff: `AGENT_HANDOFF_V55_2026-08-05.md`.

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatch author and worker | assigned subagent | exact six-path no-commit execution |
| Independent reviewer/closer | root reviewer agent | independent diff/test/gate review and any accepted commit |
| Operator | human authority owner | any scope, risk, live, public, or destructive expansion |

## Scope / Target / Owner Boundary

Allowed paths:

- `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md`
- `docs/reviews/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_WORKER_RETURN_2026-08-09.md`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality_source.py`
- `docs/baselines/CVF_GC018_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md`

Forbidden scope: every other path; LPCI runtime/test/config; Model Gateway
runtime; any other checker; provider/API-key/network/live execution;
persistence/vector/RAG/non-public grants; session/handoff/catalog/registry/
public/deployment changes; staging or commit.

Risk ceiling: bounded governance checker maintenance only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`checker-maintenance`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Resolver result: zero candidates; `truncated=false`.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V55_2026-08-05.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `governance/toolkit/05_OPERATION/CVF_CORE_GUARD_SELF_PROTECTION_GUARD.md`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality_source.py`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active source-path parser is defined in the extracted helper | `governance/compat/check_work_order_dispatch_quality_source.py` | `PATH_RE` definition | `PATH_RE` | source-verification helper | EXISTS | ACCEPT |
| Accepted source rows use extracted paths and explicit existence validation | `governance/compat/check_work_order_dispatch_quality_source.py` | `_validate_accepted_source_rows` | `_validate_accepted_source_rows` | source-verification helper | RUNTIME_BEHAVIOR | ACCEPT |
| Existing missing-path test proves ACCEPT-row rejection | `governance/compat/test_check_work_order_dispatch_quality_source.py` | `test_accepted_source_row_missing_source_file_fails` | `test_accepted_source_row_missing_source_file_fails` | pytest module | EXISTS | ACCEPT |

New focused parenthesis tests are planned outputs, not pre-existing source
facts, and therefore are not represented as ACCEPT rows.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or authority requirement | Work-order instruction | Output | Verification | Status |
|---|---|---|---|---|
| Full contiguous dashboard path | remove split-backtick workaround and checker-gaming prose | roadmap | dispatch-quality gate | REQUIRED |
| Runnable UC-01 and UC-02 counterexample framing | preserve exact semantics | roadmap | focused semantic inspection | REQUIRED |
| One lifecycle only | DESIGN acceptance precedes separate provider/live authority | roadmap | focused semantic inspection | REQUIRED |
| UC-04 AND rule | reuse/compose Model Gateway owner AND document config contract | both docs | focused semantic inspection | REQUIRED |
| Balanced parenthesized paths | repair active parser only | source helper | focused pytest | REQUIRED |
| Missing/malformed paths rejected | add negative tests | focused tests | focused pytest | REQUIRED |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | work-order structure; completion path; Verification Commands; Intake Role Routing Decision; Core Guard fields; AHB fields; scaffold provenance fields |
| gateRunPurpose | confirm dispatch readiness and lifecycle before protected checker implementation; not first discovery of checker requirements |
| claimBoundary | dispatch evidence only; no source/test completion or reviewer acceptance claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | manual bounded GC-018 plus WORKER_MUST_NOT_COMMIT work-order profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | packet was authored with apply_patch from canonical template and checker read-ahead because the exact R3 conditional paths were operator-fixed |
| checkerReadAheadConfirmation | work-order dispatch quality, structural completeness, checker read-ahead, Core Guard, AHB, and scaffold-provenance checkers read |
| docOnlyNewFields | N/A with reason: no runtime or schema field is introduced by this dispatch packet |
| claimBoundary | scaffold provenance only; no implementation correctness claim |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | attached R3 authority with two literal authorization tokens |
| Intake role | worker authors the conditional packet and executes the bounded checker/docs repair |
| Reviewer role | independent reviewer validates diff, tests, gates, and closure conversion |
| Routing decision | `WORKER_MUST_NOT_COMMIT` |
| Public route | `DEFERRED_PRIVATE_ONLY` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | no-commit worker return to independent reviewer closure conversion |
| escalation condition | packet commit requirement, forbidden path, scope expansion, provider/live/public action, or destructive action |

## Worker Autonomy / No-Question Rule

Repair and rerun allowed-scope failures without operator questions. Stop for
scope expansion, forbidden paths, live/provider/public action, destructive
action, or a lifecycle requirement for reviewer packet commit.

## Pre-Flight Checks

- Capture `git rev-parse HEAD` and exact `git status --short`.
- Run ADIF resolver with the exact disclosed query.
- Run pre-dispatch after this packet exists.
- If lifecycle requires packet commit before implementation, return
  `BLOCKED_PENDING_PACKET_COMMIT`.
- Otherwise rerun pre-implementation before source/test edits.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify only the active source-path parser
and focused test module to accept balanced parenthesized path segments while
preserving roots, malformed-path rejection, and ACCEPT-row existence checks.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality_source.py`

Operator authorization: `AUTHORIZE_BOUNDED_PATH_RE_PARENTHESIZED_SOURCE_PATH_CHECKER_REPAIR`.

Rollback boundary: revert only these checker/test changes if regression or
scope widening is detected; do not revert intake documentation or prior LPCI
closures.

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | no-commit subagent worker plus independent root reviewer/closer |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE |
| baseHeadFor(phase) | dispatchBaseHead and executionBaseHead `95340497fe4ca835ee85d44f311f651632b9c606`; closureBaseHead reviewer-owned |
| changedSetScope(phase) | dispatch docs, then exact six-path execution manifest, then reviewer-owned closure paths |
| traceScope(phase, actor) | worker traces dispatch/execution; reviewer traces independent closure |
| commitOwner(phase) | no worker commit; reviewer owns accepted material/closure commit |
| crossBatchIsolation | clean worktree for unrelated paths; only the exact LPCI1 R3 manifest may be dirty |
| nextMoveSurfaces | reviewer-owned; no worker session-sync mutation |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_COMPLETION_2026-08-09.md`

reviewerOwnedClosurePaths: any completion review, accepted status conversion,
material commit, and session synchronization are reviewer-only and outside the
worker changed set.

## Execution Plan

1. Pass pre-dispatch and pre-implementation lifecycle gates.
2. Replace only active `PATH_RE` with balanced-parenthesis-safe extraction.
3. Add tests for existing/missing parenthesized path, ordinary path, and
   malformed/unbalanced parentheses.
4. Apply roadmap and worker-return R3 semantic repairs.
5. Run focused tests, required gates, manifest comparison, staged-empty check,
   and return pending review without commit.

## Evidence Requirements

- `python -m pytest governance/compat/test_check_work_order_dispatch_quality_source.py -q`
- `python governance/compat/run_worker_return_fast_gate.py`
- `python governance/compat/check_core_guard_self_protection.py --base 95340497fe4ca835ee85d44f311f651632b9c606 --head HEAD --enforce`
- `python governance/compat/check_governed_file_size.py --enforce`
- `git diff --check`
- exact expected-versus-actual manifest and empty staged set.

## Verification Commands

- `python -m pytest governance/compat/test_check_work_order_dispatch_quality_source.py -q`
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_work_order_dispatch_quality_source.py`
- `python governance/compat/check_core_guard_self_protection.py --base 95340497fe4ca835ee85d44f311f651632b9c606 --head HEAD --enforce`
- `python governance/compat/check_governed_file_size.py --enforce`
- `git diff --check`

## Acceptance Criteria

- Existing balanced `(dashboard)` path is extracted and accepted.
- Same path fails when absent.
- Ordinary paths still pass.
- Unbalanced parentheses do not bypass validation.
- Repository roots and existence validation remain unchanged.
- R3 documentation ledger resolves every attached semantic finding.
- Provider/live/network calls remain zero; staged set remains empty.

Fail conditions: any forbidden path, root widening, existence-check weakening,
unresolved semantic finding, failed required gate, provider/live/network call,
stage, commit, or reviewer-acceptance claim.

## Work-Order Fulfillment Manifest

| Output | Owner | Required disposition |
|---|---|---|
| six allowed paths | worker | changed only as needed and returned uncommitted |
| independent closure evidence | reviewer | reviewer-owned after return |

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/baselines/CVF_GC018_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md` | Yes | conditional authority baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md` | Yes | file-backed dispatch packet |
| `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | Yes | repaired R3 intake roadmap |
| `docs/reviews/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_WORKER_RETURN_2026-08-09.md` | Yes | worker evidence and repair ledger |
| `governance/compat/check_work_order_dispatch_quality_source.py` | Yes | bounded active parser repair |
| `governance/compat/test_check_work_order_dispatch_quality_source.py` | Yes | focused regression coverage |

## Foundation Storage Layout Block

N/A with reason: this batch neither creates nor relocates a durable governance
foundation. It changes one existing extracted checker helper, its focused test,
and bounded dispatch/intake documents at their established owner locations.

## Write Ownership

Worker owns only the six allowed paths. The conventional completion review,
any material commit, closure conversion, and session synchronization are owned
only by the independent reviewer.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required worker-return terms: Purpose; Scope / Methodology; Findings / Position;
Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block;
Public Export Disposition; executionBaseHead; git status --short.

- Delta Execution Claim Boundary Control Block
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Every conditional term must be included with evidence or `N/A with reason` /
`NOT_APPLICABLE_WITH_REASON`; omission is forbidden.

## External Knowledge Intake Routing

Chain map reference: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
|---|---|
| Chain map | canonical path above was reviewed |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_TRIGGERED |
| Matching local-view guard | N/A with reason: no external knowledge absorption occurs |
| Owner surface | existing CVF checker and focused test owner |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | local checker maintenance only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE.

Expected Result / Prediction: a balanced parser can accept parentheses inside
one allowed-root path without relaxing missing or malformed path rejection.

Evidence Comparison Requirement: focused positive and negative tests compare
actual extraction/validation with this prediction.

Contradiction Handling Requirement: any widening or bypass blocks return as
complete and requires rollback inside the two protected files.

Claim Update Requirement: worker return records confirmed, narrowed, or
rejected outcome from test evidence.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded PATH_RE and paired R3 documentation repair |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: deterministic local checker tests create no live receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT through diff, tests, and gates |
| invocationBoundary | governed local source/test/document editing only |
| interceptionBoundary | no provider/network/live interception claim |
| claimLanguage | balanced path parsing plus bounded intake semantic repair |
| forbiddenExpansion | no LPCI/Model Gateway runtime, other checker, provider/live, public, deployment, staging, or commit |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/test_check_work_order_dispatch_quality_source.py` |
| Runtime behavior claimed | N/A_WITH_REASON: no LPCI product runtime behavior was changed or claimed |
| Helper/checker implementation claimed | PASS: bounded parenthesis validation is covered by the focused 11-test suite |
| Provider/live proof claimed | N/A_WITH_REASON: no provider or live action was authorized or run |
| Provider registry surfaces | N/A_WITH_REASON: Model Gateway and provider configuration remain outside this repair |
| Public-sync claimed | PASS_BOUNDED: only the checker/test subset plus public authorization receipt was exported at public commit `2103a38f` |
| Freshness disposition | PASS - checker implementation and tests were directly reviewed after worker return |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | no-commit worker |
| Provider or surface | local repository tools |
| Session or invocation | LPCI1 R3 PATH_RE worker, 2026-08-09 |
| Working directory | repository root |
| Command or tool surface | read, apply_patch, pytest, governance gates, Git read-only evidence |
| Target paths | exact six-path allowed manifest |
| Allowed scope source | attached operator authority and paired GC-018 |
| Before status evidence | HEAD `95340497fe4ca835ee85d44f311f651632b9c606`; clean worktree for unrelated paths; exact two authorized intake docs already untracked |
| After status evidence | dispatch packet pending pre-dispatch gate |
| Diff evidence | `git status --short --untracked-files=all`; `git diff --name-status` |
| Approval boundary | exact bounded checker/test and documentation repair |
| Claim boundary | repo-local parser/test/document evidence only |
| Agent type | OTHER: worker subagent |
| Invocation ID | `lpci1-r3-path-re-worker-2026-08-09` |
| Expected manifest | baseline; work order; roadmap; worker return |
| Actual changed set | same four dispatch-authoring documentation paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_R3_PATH_RE_REPAIR_COMPLETION_2026-08-09.md` | reviewer verdict and exact commit receipts | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | intake accepted bounded; fresh DESIGN-only authority remains required | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | unchanged generated aggregate; corpus checker reported 160 corpora and 0 violations | BLOCKED with reason: registry mutation was outside this bounded repair |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no registry classification or readiness change was authorized | BLOCKED with reason: registry mutation was outside this bounded repair |
| External evidence digest | N/A with reason: repository-local source and Git evidence only | no external artifact was absorbed | N/A with reason |
| System loop interlock | roadmap and reviewer completion | next phase remains parked before fresh DESIGN authority | PASS |
| Session continuity | separate reviewer-owned session-sync commit | generated state and active handoff are updated only after material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| worker execution route | `WORKER_MUST_NOT_COMMIT` | PASS |
| worker manifest | exact six authorized paths | PASS |
| focused regression result | 11 of 11 tests passed | PASS |
| worker provider/live/network calls | 0 | PASS |
| reviewer material commit | `a59e8649e` | PASS |
| reviewer completion | `docs/reviews/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_R3_PATH_RE_REPAIR_COMPLETION_2026-08-09.md` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker maintenance; no public-sync.

## Review Gate

Worker returns only `COMPLETE_PENDING_REVIEW` or an exact blocker. Independent
reviewer owns acceptance, commit, closure conversion, and session sync.

## Closure Checklist

| Item | Required disposition |
|---|---|
| Exact six-path manifest | worker records actual status; reviewer verifies |
| Focused tests and required gates | PASS or exact governed blocker |
| Provider/live/network count | zero |
| Staged set | empty |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Reviewer acceptance | reviewer-owned after worker return |

## Operator Checkpoint

N/A with reason: both bounded authority tokens are already issued. A new
operator checkpoint is required only for scope, risk, live/provider, public,
destructive, or forbidden-path expansion.

## Return-To-Orchestrator Conditions

Return exact blocker if pre-dispatch or pre-implementation cannot pass inside
allowed scope, packet commit is required, or any required repair exceeds the
six-path manifest.

## Claim Boundary

This work order authorizes only the exact six-path no-commit R3 repair. It
does not authorize runtime/provider/live/public/deployment behavior or worker
acceptance/closure claims.
