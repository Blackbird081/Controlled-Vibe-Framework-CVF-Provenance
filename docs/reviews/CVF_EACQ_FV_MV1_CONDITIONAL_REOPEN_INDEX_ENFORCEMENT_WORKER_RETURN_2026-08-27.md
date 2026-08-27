# CVF EACQ-FV MV1 Conditional Reopen Index Enforcement Worker Return

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_2026-08-27.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_2026-08-27.md`

Memory class: FULL_RECORD

docType: review

Date: 2026-08-27

## Purpose

Implement one deterministic compatibility checker that prevents a changed
absorption closeout from silently dropping a conditional forward-value
candidate from the central reopen index, per EACQ-FV-MV1. This return
delivers exactly the checker, its focused test module, and this worker
return, and records the exact-command verification results, including one
finding worth reviewer attention and one pinned-command drift.

## Scope / Methodology

Worker role: delegated no-commit implementation worker. Commit mode:
`WORKER_MUST_NOT_COMMIT`. Write ownership was exactly three new paths;
every existing governed file, including the core standard and the
conditional reopen index, was read-only for this tranche.

Methodology: read every Required First Read source, recompute all six
pinned input hashes, confirm dispatch-base ancestry and a clean/empty
starting worktree, implement the checker and tests against the existing
Conditional Reopen Index Rule vocabulary only (no new candidate categories),
build the mandated MPA negative regression fixture first, then the full
Focused Case Matrix, then run every pinned verification command and record
exact output.

## Source Inventory

| Source | Action |
| --- | --- |
| `AGENTS.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION_MEMORY.md` | READ |
| `AGENT_HANDOFF_V59_2026-08-11.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_2026-08-27.md` | FULL_READ |
| `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | SOURCE_VERIFIED |
| `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | FULL_READ |
| `governance/compat/check_fpc_parked_reopen_inventory.py` | FULL_READ |
| `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py` | FULL_READ |
| `governance/compat/check_external_absorption_core.py` | PARTIAL_READ |
| `governance/compat/test_check_external_absorption_core.py` | PARTIAL_READ |
| `governance/compat/test_check_kiod_runtime_candidate_reopen_inventory.py` | PARTIAL_READ |
| `governance/compat/check_core_guard_self_protection.py` | PARTIAL_READ |
| `governance/compat/check_closure_packaging_preflight.py` | PARTIAL_READ |

## Findings / Position

### Finding 1 - checker correctly enforces the rule against the actual MV-1 dispatch range, and surfaces one live citation gap

Running the new checker with the pinned command
`python governance/compat/check_external_absorption_conditional_reopen_index.py --base f10c3e4188c22b72797651bd1cac5b1e4b5726f9 --head HEAD --enforce`
returns exit code 1 with one violation:
`docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md`
records the conditional candidate tokens `CHECKER_CANDIDATE`, `DEFERRED`,
`PACKAGE_CANDIDATE`, `RUNTIME_CANDIDATE`, but in this changed range it
neither adds/updates a matching central-index row, cites a specific
existing matching row by its exact backtick-quoted candidate id with a
currency statement, nor states the exact
`NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON` marker.

Investigation: the matching row
`MPA-AI-utility-under-attack-evaluation-precursor` does exist, is current,
and is correctly `RUNTIME_CANDIDATE` / `DEFERRED_FORWARD_VALUE_PRESERVED` at
`docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md:157`.
The roadmap's own body, however, never quotes that exact candidate id
anywhere; it only references "the MPA conditional reopen index row" in
prose at line 483. This holds even across the full range from the original
roadmap-proposal commit `0da3b4c4d252652db1862a1f276be36ffc15c04c` through
HEAD (also tested; 2 violations there, including the paired disposition
packet for the same reason). The index file itself was not part of the
narrower `f10c3e418..HEAD` changed set at all, so outcome 1 (add/update in
the same changed set) does not apply either.

This is not a bug fixed by loosening the citation matcher: the existing
core-standard rule requires a closeout to "cite the existing row in this
index and state why it remains current," and the work order explicitly
states "a bare path to the index, a row-like label without a resolvable
matching row, or generic 'already covered' prose must fail." The roadmap's
current prose is exactly that generic label, not a resolvable citation.
Treating this as a pass would have reintroduced the original MPA-class gap
this tranche exists to close. This finding is reported for reviewer
disposition; the roadmap is a read-only file outside this worker's write
ownership, so no repair was made to it.

### Finding 2 - pinned autorun phase name has drifted from the work order text

The work order's Verification Commands list
`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-review --base <head> --head HEAD`.
The current script only accepts
`{pre-dispatch, pre-implementation, pre-closure, pre-push}`; `pre-review` is
rejected with `argument --phase: invalid choice`. This worker did not
substitute a different phase as a silent repair, since the phase argument
is outside the three-path write ownership. As a supplementary check only
(not a substitute for the pinned command), `--phase pre-implementation`
was run against the same range and failed on 5 gates, all of which concern
paths this worker did not touch and cannot repair (`AGENT_HANDOFF_V59_2026-08-11.md`,
`CVF_SESSION/*.json`, `CVF_SESSION_MEMORY.md`, and the two dispatch
authoring artifacts committed by the orchestrator before this dispatch).
Reported for reviewer awareness; not treated as a worker-scope defect.

## Risk / Corrective Action

Risk: the checker's whole-file, content-presence scanning (adapted directly
from the FPC/KIOD precedent pattern per the work order) can flag a file
whose relevant candidate-disposition table rows are unchanged in the
current diff, if that file happens to be touched for an unrelated reason
and its citation of the matching index row is generic prose rather than an
exact id. This was observed directly (Finding 1) and is not a false
positive: the underlying citation gap is real. Corrective action available
to the reviewer, not taken by this worker: either accept the finding and
have a future revision of the roadmap/disposition quote the exact
candidate id, or accept the current prose reference as sufficient and treat
this checker run as advisory pending a scoped follow-up decision. No
checker code change is proposed to relax this behavior, because relaxing it
would reduce the guard's ability to catch the exact MPA-class failure mode
it exists to prevent.

## Implementation Location

- `governance/compat/check_external_absorption_conditional_reopen_index.py`
  - `check_text(path, text, ...)` - per-document validator; entry point for
    both the CLI range-aware path and isolated unit tests.
  - `run(base, head)` - changed-set discovery plus per-file validation;
    resolves the central index at `base` and at the current worktree to
    detect a same-batch row add/update.
  - `_mentions_conditional_candidate` - detects the seven existing candidate
    tokens (`PACKAGE_CANDIDATE`, `RUNTIME_CANDIDATE`, `CHECKER_CANDIDATE`,
    `DEFER_WITH_REOPEN_CONDITION`, `DEFERRED_WITH_REOPEN_CONDITION`,
    `DEFERRED`, `VALUE_PARKED`) with word-boundary matching; introduces no
    new vocabulary.
  - `_extract_index_candidate_ids` - parses backtick-quoted Candidate ID
    cells from `## Candidate Index` and source-family cells from
    `## Terminal Source-Family Closures`.
  - `_cites_existing_row` / `_has_no_entry_marker_with_reason` - the two
    non-same-batch semantic outcomes.
  - `main` - CLI entry point with `--base`, `--head`, `--enforce`.

## MPA Regression Test

`governance/compat/test_check_external_absorption_conditional_reopen_index.py::NegativeCaseTests::test_negative_mpa_omission_regression`
models the actual MPA deferred closeout (a `DEFERRED` utility-under-attack
candidate with the pre-repair index state, which had no matching row) and
asserts exactly one violation of type
`conditional_reopen_index_candidate_disappeared`, with the message
containing `DEFERRED`. This is the primary regression named in the work
order, not an incidental malformed-file test.

## Focused Case Names

| Case | Test |
| --- | --- |
| positive matching row add/update | `ThreeOutcomePositiveTests::test_outcome_one_add_or_update_matching_row_in_same_changed_set` |
| positive cited existing matching row plus current rationale | `ThreeOutcomePositiveTests::test_outcome_two_cites_existing_matching_row_with_currency_statement`, `test_outcome_two_cites_terminal_source_family_closure_row` |
| positive exact no-entry marker, each reason class | `ThreeOutcomePositiveTests::test_outcome_three_no_entry_marker_reason_fully_adapted`, `test_outcome_three_no_entry_marker_reason_rejected_no_remaining_value`, `test_outcome_three_no_entry_marker_reason_already_owned_elsewhere` |
| negative MPA omission | `NegativeCaseTests::test_negative_mpa_omission_regression` |
| negative bare index-path citation | `NegativeCaseTests::test_negative_bare_index_path_citation_is_not_evidence` |
| negative missing/non-matching row identifier | `NegativeCaseTests::test_negative_missing_non_matching_row_identifier` |
| negative empty/unsupported no-entry reason | `NegativeCaseTests::test_negative_empty_no_entry_reason`, `test_negative_unsupported_short_no_entry_reason` |
| archive-only non-applicability | `ArchiveSafetyTests::test_archive_path_is_not_applicable`, `test_non_governed_prefix_is_not_applicable`, `test_the_index_and_standard_themselves_are_exempt` |
| committed-range plus staged/unstaged/untracked discovery | `RangeAndWorktreeDiscoveryTests::test_committed_range_discovery`, `test_staged_unstaged_and_untracked_discovery` (real isolated temporary Git repositories; no governed repository evidence mutated) |
| deterministic repeated output and CLI exit status | `DeterministicCliTests::test_repeated_run_over_clean_worktree_is_deterministic`, `test_cli_exit_code_zero_on_clean_worktree` |
| candidate-token detection and word-boundary safety | `ConditionalCandidateDetectionTests` (3 tests) |
| index table parsing | `IndexParsingTests` (3 tests) |

24 focused tests total, 24 passed.

## Command Evidence

```text
$ git merge-base --is-ancestor f10c3e4188c22b72797651bd1cac5b1e4b5726f9 HEAD
exit code: 0 (ancestry confirmed)

$ python governance/compat/run_adif_defect_resolver.py --task-class "checker implementation" --role worker --lifecycle-phase pre-implementation --surface-selector governance/compat --risk-ceiling HIGH --json
{"items": [], "truncated": false, "totalCandidates": 0, ...}
exit code: 0 (matches dispatch-time NONE_RETURNED; no overlay)

$ python -m pytest governance/compat/test_check_external_absorption_conditional_reopen_index.py -q
24 passed in 1.99s
exit code: 0

$ python governance/compat/check_external_absorption_conditional_reopen_index.py --base f10c3e4188c22b72797651bd1cac5b1e4b5726f9 --head HEAD --enforce
=== CVF External Absorption Conditional Reopen Index Enforcement Guard ===
Range: f10c3e4188c22b72797651bd1cac5b1e4b5726f9..HEAD
Violations: 1
  - docs/roadmaps/CVF_EXTERNAL_AGENT_CODING_QUALITY_AND_FORWARD_VALUE_ABSORPTION_ROADMAP_2026-08-27.md: records conditional candidate token(s) CHECKER_CANDIDATE, DEFERRED, PACKAGE_CANDIDATE, RUNTIME_CANDIDATE but neither adds/updates a matching row ... (no cited candidate id resolves to a current central-index row)
VIOLATION - a conditional forward-value candidate disappeared from the reopen index.
exit code: 1 (see Finding 1; this is the checker working as designed against a read-only file this worker cannot repair)

$ python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_external_absorption_conditional_reopen_index.py
[first run, worker return not yet in changed set] pytest target: 24 passed; bundled gate FAIL on 2 items requiring a `Core Guard Self-Protection Authorization` block in a changed file naming both new checker paths.
[after adding that block to this worker return] bundled gate FAIL on 3 new items surfaced once this file became scannable: worker-experience retrospective (missing token), worker-return quality gate (gateRunPurpose self-trigger, missing `git diff --name-status` in trace, missing Delta receipt/action tokens, missing no-commit literal), finding-to-governance learning (disposition/next-action/runtime-lane vocabulary).
[final run, after repairing all five items in this file] `[CVF hook] All reviewer-fast governance checks passed.` / `PASS: reviewer-fast governance gate (3.47s)` / `COMPLIANT: worker-return fast gate passed in 6.06s.`
exit code: 0 (final)

$ python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-review --base f10c3e4188c22b72797651bd1cac5b1e4b5726f9 --head HEAD
argument --phase: invalid choice: 'pre-review' (choose from 'pre-dispatch', 'pre-implementation', 'pre-closure', 'pre-push')
exit code: 2 (see Finding 2; pinned command drift, not a worker-scope defect)

$ python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base f10c3e4188c22b72797651bd1cac5b1e4b5726f9 --head HEAD
VIOLATION: pre-implementation blocked by 5 failing gate(s) in 5.11s.
(supplementary only; all 5 failures reference paths outside this worker's write ownership - AGENT_HANDOFF_V59_2026-08-11.md, CVF_SESSION/*.json, CVF_SESSION_MEMORY.md, and the pre-existing dispatch-authoring commits)

$ git diff --check
(no output; exit code 0)

$ git diff --name-status
(no output - no tracked file modified)

$ git diff --name-only
(no output - no unstaged changes to tracked files)

$ git diff --cached --name-only
(no output - staging area empty)

$ git status --short
?? governance/compat/check_external_absorption_conditional_reopen_index.py
?? governance/compat/test_check_external_absorption_conditional_reopen_index.py
?? docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_WORKER_RETURN_2026-08-27.md
```

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `check_dispatch_prompt_envelope.py`; `check_worker_return_quality_gate.py`; `check_governed_artifact_checker_read_ahead.py`; `check_core_guard_self_protection.py`; `check_closure_packaging_preflight.py`; `check_task_governance_route.py`; `check_agent_operation_trace.py`; precedents `check_fpc_parked_reopen_inventory.py`, `check_kiod_runtime_candidate_reopen_inventory.py`, `check_external_absorption_core.py` |
| literalTokensReviewed | `Self-declared worker-return artifact: yes`; `Responds to work order:`; `Core Guard Self-Protection Authorization`; `Authorized guard-maintenance scope`; `Protected paths`; `Operator authorization`; `Rollback boundary`; `NO_CONDITIONAL_REOPEN_INDEX_ENTRY_WITH_REASON`; required worker-return heading set |
| gateRunPurpose | Confirm dispatch, self-protection, and worker-return contracts before and after implementation; gate runs are confirmation and evidence-recording, run only after the required reads above were already completed. |
| claimBoundary | Source read-ahead is preparation evidence only and does not establish checker correctness or closure. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create exactly the new conditional-reopen
compatibility checker and its focused test module; no existing guard,
runner, hook chain, catalog, standard, index, or policy was modified.

Protected paths:

- `governance/compat/check_external_absorption_conditional_reopen_index.py`
- `governance/compat/test_check_external_absorption_conditional_reopen_index.py`

Operator authorization: explicit EACQ-FV-MV1 opening and orchestrator/worker
role split on 2026-08-27, recorded in
`docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_2026-08-27.md`
"Core Guard Self-Protection Authorization" section.

Rollback boundary: if rejected, remove only the two new code/test files;
retain the R0 review, disposition, roadmap, index, and this worker return as
provenance evidence. This worker did not edit any existing guard, runner,
hook chain, catalog, standard, index, or policy file.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit implementation worker |
| Provider or surface | local private-provenance workspace |
| Session or invocation | EACQ-FV-MV1 worker execution, 2026-08-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, Bash (`git`, `python`, `pytest`), governance gates |
| Target paths | the three exact Write Ownership paths named in the work order |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_2026-08-27.md` |
| Before status evidence | clean worktree and empty staging at execution head `75e21242bde1f82f0fa5d204dbdcb42f2f719a25`; all three writable paths absent |
| After status evidence | exactly three new untracked paths; no staged changes; no existing file modified |
| Diff evidence | `git diff --name-status` (empty; no tracked file modified) plus `git status --short` before and after, recorded above and in Command Evidence |
| Approval boundary | three-path no-commit implementation only; no closure, hook wiring, provider, public, or production claim |
| Claim boundary | no runtime/provider/live/public/production claim; this is local deterministic checker and test implementation pending independent review |
| Agent type | delegated no-commit implementation worker |
| Invocation ID | `eacq-fv-mv1-worker-2026-08-27` |
| Expected manifest | `governance/compat/check_external_absorption_conditional_reopen_index.py`; `governance/compat/test_check_external_absorption_conditional_reopen_index.py`; this worker return |
| Actual changed set | `governance/compat/check_external_absorption_conditional_reopen_index.py`; `governance/compat/test_check_external_absorption_conditional_reopen_index.py`; this worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | NONE |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local checker implementation and focused tests only |
| claimDisposition | N/A with reason: no agent-control or runtime-execution claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider/runtime receipt is required or claimed by this return |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no external action is claimed; local file/test evidence only, recorded above under Command Evidence |
| invocationBoundary | this return does not assert mandatory invocation or wrapper coverage |
| interceptionBoundary | no interception, proxy, hook, or universal control is authorized or claimed |
| claimLanguage | implementation remains pending independent review; not self-closed |
| forbiddenExpansion | no universal governed-coding, runtime, provider, public, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public artifact, remote, commit, or path is authorized or claimed by this
worker return.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed R0 finding -> revised roadmap -> bounded MV-1 enforcement work order -> this worker return |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing absorption core standard and conditional reopen index |
| Disposition | ADAPT only as enforcement of the existing rule |
| Claim boundary | no new external knowledge, doctrine, provider, or effectiveness claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: bounded implementation of an existing rule against a
  fixed source set; no source reassessment is performed by this worker.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded named-owner checker
  implementation; no corpus inventory or completeness claim is made by this
  return.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| Roadmap and disposition packet reference the matching central-index row only by generic prose ("the MPA conditional reopen index row"), not by its exact backtick candidate id, even in the current committed state | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Next action: reviewer decides whether future closeouts must quote the exact candidate id, or whether an unambiguous named prose reference is sufficient; this worker makes no rule change and no repair to the read-only roadmap. |
| Work order's pinned `--phase pre-review` autorun command does not match the current `run_agent_autorun_workflow_gate.py` accepted phase set (`pre-dispatch`, `pre-implementation`, `pre-closure`, `pre-push`) | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | RUNTIME_LEARNING_CANDIDATE, N/A_WITH_REASON for any live/provider/cost claim - this is a CLI-argument mismatch, not a runtime/provider/cost defect | Next action: reviewer/dispatcher reconciles the work-order verification-command template against the current autorun script's accepted `--phase` values; outside this worker's write ownership to resolve. |

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: LOW

frictionType: ENUM_OR_TOKEN_MISMATCH

observedStep: running the pinned `run_agent_autorun_workflow_gate.py --phase pre-review` command from the Verification Commands section, which the current script rejects because its accepted `--phase` choices are `pre-dispatch`, `pre-implementation`, `pre-closure`, `pre-push`

preventiveControlCandidate: WORK_ORDER_TEMPLATE

## Epistemic Process Block

Expected Result / Prediction: adapting the FPC/KIOD parked-reopen-inventory
pattern to a changed-doc scan against the existing central index, using only
the existing rule's three semantic outcomes, would deterministically catch
the MPA-class omission without inventing new doctrine.

Evidence Comparison: the MPA regression fixture reproduces the omission and
fails for the correct reason (candidate token present, no valid disposition
found). Run against the real MV-1 dispatch range, the checker additionally
surfaced a live, unresolved instance of the same failure class in the
current roadmap/disposition prose (Finding 1), which was not anticipated at
dispatch time but is consistent with the rule as written.

Contradiction Or Gap Disposition: no contradiction; the additional live
finding is evidence the checker generalizes correctly beyond the specific
fixture it was built to reproduce, rather than a design defect requiring
repair inside this worker's scope.

Claim Update: the checker enforces the existing rule; it does not itself
resolve Finding 1, does not claim absorption-quality improvement beyond this
one enforcement gate, and does not claim hook-wired or CI-enforced status.

## Claim Boundary

This return delivers exactly three paths under `WORKER_MUST_NOT_COMMIT`: a
new deterministic conditional-reopen-index enforcement checker, its focused
test module (24/24 passing), and this worker return. It implements no new
candidate vocabulary, doctrine, index, hook wiring, catalog change, session
mutation, provider/network/live call, public sync, deployment, or push. It
makes no closure claim; commit, repair-or-accept, and continuity update
remain reviewer-owned per the work order's Reviewer Closure Conversion and
Review Gate sections. Finding 1 is reported, not resolved, because its
target (the roadmap) is outside this worker's write ownership.

## git status --short

```text
?? governance/compat/check_external_absorption_conditional_reopen_index.py
?? governance/compat/test_check_external_absorption_conditional_reopen_index.py
?? docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_WORKER_RETURN_2026-08-27.md
```

## Changed Files

- `governance/compat/check_external_absorption_conditional_reopen_index.py` (new)
- `governance/compat/test_check_external_absorption_conditional_reopen_index.py` (new)
- `docs/reviews/CVF_EACQ_FV_MV1_CONDITIONAL_REOPEN_INDEX_ENFORCEMENT_WORKER_RETURN_2026-08-27.md` (new, this file)

No existing file was modified, staged, or committed.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: this worker did not run `git add`, `git
commit`, `git push`, or any staging command at any point in this tranche.
All three output paths remain untracked in the working tree. `git status
--short` above is the exact observed state after the final verification
run. Commit, repair, closure, and continuity-state update are reserved for
the designated reviewer/closer per the work order's Commit Mode And
Base-Anchor Lifecycle and Reviewer Closure Conversion sections.

## Independent Reviewer Addendum

Reviewer disposition: `ACCEPT_AFTER_BOUNDED_REPAIR`.

The worker's exact three-path/no-commit manifest was independently confirmed.
The original 24 tests passed, but semantic review found three blocking false
pass classes inside the authorized checker/test scope:

1. any newly added index row satisfied every changed candidate document,
   without proving that the row matched the document or candidate class;
2. the no-entry outcome accepted any reason of eight or more characters,
   rather than one of the three source-owned reason classes;
3. applicability treated roadmap/work-order planning vocabulary as absorption
   closeout disposition evidence.

Reviewer repair narrowed applicability to current non-archive audit/review
artifacts carrying the current absorption-core required marker and canonical
value-conversion owner section. It now:

- matches a changed index row by exact cited candidate id or exact closeout
  path and, when a package/runtime/checker class is declared, matching class;
- detects both newly added and modified existing candidate rows;
- validates the three source-owned no-entry reason classes and requires the
  marker inside the candidate-disposition section;
- requires the existing-row currency statement near the resolvable citation;
- rejects multiple simultaneous outcomes because the work order requires
  exactly one; and
- excludes planning-only roadmap/work-order surfaces and candidate vocabulary
  quoted outside the canonical value-conversion section.

Nine reviewer regressions were added, bringing focused evidence to 33/33:
unrelated row change, wrong candidate class, existing-row update, long
unsupported reason, marker outside disposition, distant currency prose,
multiple outcomes, vocabulary outside owner section, and planning-surface
non-applicability. The repaired checker passes the actual dispatch range
`f10c3e4188c22b72797651bd1cac5b1e4b5726f9..HEAD` with zero violations.

The worker's Finding 1 is therefore superseded: it arose from over-broad
applicability, not a roadmap citation defect within MV-1's closeout/audit/review
contract. Finding 2 remains a valid dispatcher evidence defect: the work order
quoted unsupported autorun phase `pre-review`. It does not affect checker
semantics; reviewer verification uses the current `pre-closure` phase and the
template/dispatch learning remains separately reportable.

Reviewer claim boundary: this addendum accepts only the repaired standalone,
unwired local checker and tests. It adds no hook/catalog binding, doctrine,
candidate vocabulary, provider/public/runtime effect, successor authority, or
production claim.
