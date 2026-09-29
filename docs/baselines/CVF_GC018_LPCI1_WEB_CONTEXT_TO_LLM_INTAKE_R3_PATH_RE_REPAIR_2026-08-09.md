# CVF GC-018 LPCI1 Web Context-To-LLM Intake R3 PATH_RE Repair

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_BOUNDED_IMPLEMENTATION

Date: 2026-08-09

docType: gc018_baseline

Batch ID: LPCI1-WEB-CONTEXT-TO-LLM-INTAKE-R3-PATH-RE-REPAIR

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 95340497fe4ca835ee85d44f311f651632b9c606

executionBaseHead: 95340497fe4ca835ee85d44f311f651632b9c606

closureBaseHead: N/A_PENDING_REVIEWER_COMMIT

## Purpose

Authorize the smallest checker-maintenance repair needed for the LPCI1 intake
to cite a real repository path containing the balanced Next.js route-group
segment `(dashboard)` without splitting or disguising the path.

## Authority Chain

- `AUTHORIZE_FRESH_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_ROADMAP_DOCUMENTATION_ONLY`
- `AUTHORIZE_BOUNDED_PATH_RE_PARENTHESIZED_SOURCE_PATH_CHECKER_REPAIR`
- Attached operator authority dated 2026-08-09.
- Active handoff: `AGENT_HANDOFF_V55_2026-08-05.md`.

These tokens authorize only the exact manifest and proof boundary below.

## Scope / Target / Owner Boundary

Allowed paths:

- `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md`
- `docs/reviews/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_WORKER_RETURN_2026-08-09.md`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality_source.py`
- `docs/baselines/CVF_GC018_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_R3_PATH_RE_REPAIR_2026-08-09.md`

Forbidden: every other path; LPCI runtime/test/config; Model Gateway runtime;
provider/API-key/network/live execution; persistence/vector/RAG/non-public
grants; session/handoff/catalog/registry/public/deployment changes; staging and
commit.

## Baseline Decision

Decision: `AUTHORIZE_BOUNDED_PATH_RE_REPAIR`.

The active `PATH_RE` may accept balanced parenthesized segments inside already
allowed repository-relative roots. Missing paths, unbalanced parentheses,
root widening, ACCEPT-row existence weakening, and unrelated dispatch-rule
changes remain forbidden.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`checker-maintenance`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Resolver result: zero candidates; `truncated=false`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active source-path extractor exists | `governance/compat/check_work_order_dispatch_quality_source.py` | `PATH_RE` definition | `PATH_RE` | source-verification helper | EXISTS | ACCEPT |
| ACCEPT rows call the extractor and retain existence checks | `governance/compat/check_work_order_dispatch_quality_source.py` | `_validate_accepted_source_rows` | `_validate_accepted_source_rows` | source-verification helper | RUNTIME_BEHAVIOR | ACCEPT |
| Existing focused helper tests are owned by one module | `governance/compat/test_check_work_order_dispatch_quality_source.py` | full file | `test_accepted_source_row_missing_source_file_fails` | pytest module | EXISTS | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or authority requirement | Work-order handling | Verification | Status |
|---|---|---|---|
| Restore one contiguous dashboard path | roadmap R3 repair | dispatch-quality checker | REQUIRED |
| Preserve UC-01 runnable query and UC-02 counterexample framing | documentation-only semantic review | focused text inspection | REQUIRED |
| Bind UC-04 to Model Gateway reuse/composition AND config contract | documentation-only semantic review | focused text inspection | REQUIRED |
| Repair only active PATH_RE | one helper source edit | focused pytest | REQUIRED |
| Preserve missing/malformed rejection | negative tests | focused pytest | REQUIRED |

## Evidence / Verification

- Pre-dispatch and pre-implementation autorun must pass before source/test edits.
- Focused source-helper pytest must cover existing, missing, ordinary, and
  unbalanced path cases.
- Worker-return fast gate, Core Guard gate, file-size guard, `git diff --check`,
  manifest comparison, and staged-empty evidence are mandatory.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | baseline evidence heading; Source Verification columns; ADIF exact query; Core Guard fields; AHB fields |
| gateRunPurpose | confirm the conditional R3 dispatch packet before checker implementation; not first discovery of checker requirements |
| claimBoundary | packet readiness only; no implementation or reviewer acceptance claim |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify only the active source-path parser
and its focused test module so balanced parenthesized route-group segments are
parsed without widening repository roots or weakening existence validation.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality_source.py`

Operator authorization: `AUTHORIZE_BOUNDED_PATH_RE_PARENTHESIZED_SOURCE_PATH_CHECKER_REPAIR`.

Rollback boundary: revert only these checker/test changes if regression or
scope widening is detected; do not revert the intake roadmap, prior LPCI
closures, or unrelated governance history.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | one no-commit worker authors/implements; independent Codex reviewer closes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE |
| baseHeadFor(phase) | dispatchBaseHead and executionBaseHead are `95340497fe4ca835ee85d44f311f651632b9c606`; closureBaseHead is reviewer-owned |
| changedSetScope(phase) | worker exact six-path manifest; reviewer-owned closure paths only after return |
| traceScope(phase, actor) | worker records dispatch/execution evidence; reviewer independently records closure evidence |
| commitOwner(phase) | worker owns no commit; reviewer owns any accepted material and closure commit |
| crossBatchIsolation | exact LPCI1 R3 batch only; unrelated worktree paths forbidden |
| nextMoveSurfaces | reviewer-owned and unchanged unless accepted closure changes current mode or next move |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | no-commit worker |
| Provider or surface | local repository tools |
| Session or invocation | LPCI1 intake R3 bounded PATH_RE repair, 2026-08-09 |
| Working directory | repository root |
| Command or tool surface | file reads, apply_patch, pytest, governance gates, Git read-only evidence |
| Target paths | exact six-path allowed manifest |
| Allowed scope source | the two literal operator authority tokens above |
| Before status evidence | HEAD `95340497fe4ca835ee85d44f311f651632b9c606`; clean worktree for unrelated paths; exactly two authorized intake docs were already untracked |
| After status evidence | pending no-commit worker return |
| Diff evidence | `git status --short --untracked-files=all`; `git diff --name-status`; `git diff --no-index /dev/null <untracked-file>` as needed |
| Approval boundary | bounded checker/test and paired R3 documentation repair only |
| Claim boundary | local parser behavior and deterministic tests only |
| Agent type | Codex worker subagent |
| Invocation ID | `lpci1-r3-path-re-worker-2026-08-09` |
| Expected manifest | this baseline; paired work order; intake roadmap; intake worker return |
| Actual changed set | same four dispatch-authoring documentation paths before implementation |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance checker maintenance; no public-sync authority.

## Claim Boundary

This baseline authorizes only the exact six-path R3 repair. It proves no LPCI
runtime behavior, provider/live execution, public readiness, deployment, or
reviewer acceptance.
