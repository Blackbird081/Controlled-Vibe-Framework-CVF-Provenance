# CVF Agent Work Order GFS-PY T1 Dispatch-Quality Helper Split For Worker

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-25

docType: work_order

Batch ID: GFS-PY-T1-SPLIT

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: GFS-PY T1 no-commit worker; behavior-preserving table-parser extraction.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead `47a473fc` (capture actual with `git rev-parse --short HEAD` at start).

Current-time notes: current dispatch date is 2026-06-25; record actual local start time in the worker-return packet.

Do-not-misread notes: this is a behavior-preserving refactor only. Extract ONLY
the named pure markdown-table parsing helpers. Do NOT move any `_validate_*`
function or any rule/threshold logic. Do NOT change any failure message, any
threshold, any check behavior, or any test expectation. Do NOT let
`governance/compat/check_work_order_dispatch_quality.py` stay the same size or
grow - it is a frozen registry exception and the Python size guard will fail the
touch unless it shrinks; you must also lower its registry `approvedMaxLines` to
the new line count. Do NOT commit. Do NOT scope into T2-T4 (lifecycle/status,
source-verification, or token-collision validators).

Required first actions: read front door/state/handoff/guard orientation
documents, this work order, the GC-018 baseline, and the monolith
`check_work_order_dispatch_quality.py` around the named line numbers; capture
`git status --short`; run the full dispatch-quality suite once to record the
green baseline before any change.

Return contract: return `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` without
committing.

You are the GFS-PY T1 worker. Extract the pure table-parsing helpers into a new
module, re-import them into the monolith so every call site is unchanged, lower
the monolith's registry cap to its new line count, add a focused test for the
extracted module, run the full dispatch-quality suite green, and author the
worker-return packet. You must not commit. Return `COMPLETE_PENDING_REVIEW` only
with the required artifacts present and the full suite green, or
`BLOCKED_WITH_REASON` if a gate fails outside allowed scope.

## Purpose

Extract the pure markdown-table parsing helpers out of the dispatch-quality
monolith into a dedicated module, behavior-preserving, as the first GFS-PY split
tranche, and ratchet the monolith's frozen size exception down.

## Core Guard Self-Protection Authorization

| Field | Disposition |
| --- | --- |
| Authorized guard-maintenance scope | GFS-PY T1 creates one NEW module `governance/compat/check_work_order_dispatch_quality_tables.py` and one NEW focused test file; it modifies `governance/compat/check_work_order_dispatch_quality.py` by removing the named pure parsers and importing them back (net shrink only); and it lowers the `check_work_order_dispatch_quality.py` exception `approvedMaxLines` in `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`. It weakens no check, hook, or autorun entry |
| Protected paths | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/test_check_work_order_dispatch_quality_tables.py` |
| Operator authorization | operator selected GFS-PY T1 with a Codex-worker / Claude-reviewer route on 2026-06-25 |
| Rollback boundary | the worker creates the new module and test and edits the monolith and registry only; revert is deletion of the new files and restoration of the monolith and registry cap |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution (WORKER_MUST_NOT_COMMIT)`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: the worker
  names only the specific helpers and files it touches, not a folder
  enumeration.
- ADIF-0002 - Provider-local interaction accepted as authority: the worker
  makes no provider-local claim; this is a local behavior-preserving refactor.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class:
  the worker avoids bare gate-trigger tokens in exclusion prose.

Resolver query: taskClass=`Completion review authoring`, role=`reviewer`, lifecyclePhase=`pre-closure`

Returned defects:

- ADIF-0009 - Backtick-quoted heading name truncates real section: the reviewer
  completion must not backtick-quote any literal heading string in prose.

## Scope / Target / Owner Boundary

Target: one bounded no-commit worker-return extracting the pure table-parsing
helpers from the dispatch-quality monolith, re-importing them, lowering the
registry cap, and adding a focused test.

Owner boundary:

- this work order names the dispatcher (Claude), the worker (Codex), and the
  reviewer/closer (Claude);
- the worker owns only the paths in Write Ownership below;
- the monolith split T2-T4 is owned by the held roadmap, not this work order.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap tranche | Work order | Disposition |
| --- | --- | --- |
| GFS-PY T1 (split markdown table-parsing helpers) | this work order | dispatched |
| GFS-PY T2-T4 | none | HOLD_UNTIL_PREDECESSOR_PASS; no work order authored |

## Authority Chain

| Authority | Path | Disposition |
| --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md` | authorizes this work order |
| Roadmap | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | sequences T1 and holds T2-T4 |
| Split target | `governance/compat/check_work_order_dispatch_quality.py` | the monolith |
| Test suite | `governance/compat/test_check_work_order_dispatch_quality.py` | the regression anchor |
| Python size guard | `governance/compat/check_python_automation_size.py` | enforces the shrink-on-touch rule |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | packet shape |

## Agent Roles

| Role | Assignment |
| --- | --- |
| Dispatcher | Claude (authored this packet) |
| Worker | Codex (`WORKER_MUST_NOT_COMMIT`) |
| Reviewer | Claude (independent behavior-preservation check) |
| Closer | Claude |
| Operator | selects the tranche and the route |

Dispatch-authorship does not by itself grant execution; the operator granted
this Codex-worker / Claude-reviewer route on 2026-06-25.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Scope classification | internal code-refactor tranche derived from the GFS-PY roadmap; no external or legacy intake |
| Selected role route | `MULTI_AGENT_SINGLE_ROLE`: Codex worker (no commit), Claude reviewer/closer |
| Risk sensitivity | MEDIUM: the monolith gates every governed work order, so a behavior change would be high-impact; the behavior-preserving constraint plus full-suite regression keeps the executed risk bounded |
| Escalation condition | escalate to the operator only if a clean extraction is impossible without a behavior change, or if a repair would exceed Allowed scope or scope into T2-T4 |
| Worker role | implement the extraction, tests, monolith re-import, lowered cap, and worker-return |
| Reviewer role | independently rerun the full suite, confirm behavior preservation and net-shrink, and close |
| Routing authority | operator selection of GFS-PY T1 with this route on 2026-06-25 |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: GFS-PY T1 absorbs no legacy or external source; it
extracts pure parsing helpers from one local module per the GFS-PY roadmap, so
no legacy absorption coverage-index row applies.

## Required First Reads

- `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, the active handoff;
- `docs/baselines/CVF_GC018_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md`;
- `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md`;
- `governance/compat/check_work_order_dispatch_quality.py` around lines 519 and 815-908.

## Pre-Flight Checks

- capture `git status --short` and `git rev-parse --short HEAD`;
- run `python -m pytest governance/compat/test_check_work_order_dispatch_quality.py -q` and record the green baseline BEFORE any change;
- confirm no existing `check_work_order_dispatch_quality_tables.py` collision.

## Write Ownership

The worker owns exactly:

- `governance/compat/check_work_order_dispatch_quality_tables.py` (new module)
- `governance/compat/test_check_work_order_dispatch_quality_tables.py` (new focused test)
- `governance/compat/check_work_order_dispatch_quality.py` (remove the named parsers, import them back; net shrink only)
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` (lower the monolith exception `approvedMaxLines` to the new line count only)
- the worker-return packet at `docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_WORKER_RETURN_2026-06-25.md`

The worker must not touch any other file and must not commit.

## Required Artifact Manifest

| Artifact | Path | Status |
| --- | --- | --- |
| New table-parsing module | `governance/compat/check_work_order_dispatch_quality_tables.py` | PENDING |
| New focused test | `governance/compat/test_check_work_order_dispatch_quality_tables.py` | PENDING |
| Monolith with re-imports | `governance/compat/check_work_order_dispatch_quality.py` | PENDING |
| Lowered registry cap | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | PENDING |
| Worker-return packet | `docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_WORKER_RETURN_2026-06-25.md` | PENDING |

## Work-Order Fulfillment Manifest

| Deliverable | Fulfillment status at dispatch |
| --- | --- |
| New table-parsing module | PENDING_WORKER |
| New focused test | PENDING_WORKER |
| Monolith re-import + net-shrink | PENDING_WORKER |
| Lowered registry cap | PENDING_WORKER |
| Full dispatch-quality suite green | PENDING_WORKER |
| Worker-return packet | PENDING_WORKER |

## Forbidden Path Manifest

- any `_validate_*` function or rule/threshold logic in the monolith;
- any failure-message, threshold, or test-expectation change;
- any file outside Write Ownership;
- any commit by the worker;
- any T2-T4 scope (lifecycle/status, source-verification, token-collision validators).

## Required Proof Manifest

| Proof | Required literal |
| --- | --- |
| Full suite green after split | `test_check_work_order_dispatch_quality.py` |
| Focused module test | `test_check_work_order_dispatch_quality_tables.py` |
| Monolith net-shrink + cap lowered | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` |
| Guard COMPLIANT with lowered cap | `governance/compat/check_python_automation_size.py` |

## Execution Plan

1. read first reads; capture `git status --short`; run the full dispatch-quality suite green as the baseline.
2. create `check_work_order_dispatch_quality_tables.py` and move into it `_parse_markdown_tables`, `_parse_any_markdown_tables`, `_normalize_table_key`, `_row_value`, `_section_tables`, `_truthy_cell`, and `_clean_manifest_path`, moving or cleanly importing `_extract_section` so `_section_tables` still resolves with no circular import.
3. in the monolith, replace the moved definitions with an import of those names so every existing call site is unchanged.
4. lower the monolith exception `approvedMaxLines` in the registry to the new monolith line count.
5. add `test_check_work_order_dispatch_quality_tables.py` covering the extracted parsers (at least one table-parse, one row-value, one truthy-cell, one manifest-path case).
6. run the full dispatch-quality suite and confirm it passes unchanged; run the Python size guard and confirm COMPLIANT with the lowered cap.
7. author the worker-return packet with before/after line counts and suite results; do not commit.

## Evidence Requirements

- the green full-suite run BEFORE and AFTER the split (same pass count);
- the monolith line count before and after (after must be strictly smaller);
- the lowered registry `approvedMaxLines` equal to the new line count;
- the Python size guard COMPLIANT output with the lowered cap;
- the focused module test result.

## Review Gate

The reviewer (Claude) independently reruns the full dispatch-quality suite,
confirms it passes unchanged, confirms the monolith shrank and its cap was
lowered to match, confirms no `_validate_*`/rule logic moved and no message
changed, and only then closes.

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_COMPLETION_2026-06-25.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_COMPLETION_2026-06-25.md`
- `docs/baselines/CVF_GC018_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md` (status conversion only)
- this work order (status conversion only)
- `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` (T1 done, T2-T4 held)
- session front-door/state/handoff paths only if Claude changes current mode or next allowed move

The worker (Codex) authors only the worker-return packet and the code; the
reviewer (Claude) owns the completion review, all status conversions, and any
session-sync after the closing commit.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker (Codex) repairs its own gate failures and
proceeds without asking the operator. The worker asks only when a clean
extraction is impossible (hidden coupling forcing a behavior change), or when a
repair would exceed Allowed scope, move validator logic, change a failure
message or threshold, grow the monolith, require a worker commit, or scope into
T2-T4. A blocked extraction is returned as `BLOCKED_WITH_REASON`, not silently
reshaped.

## Worker Return Packet Shape Contract

The worker returns `docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_WORKER_RETURN_2026-06-25.md`
with these exact-heading sections, each on its own line:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position (including any hidden-coupling NEW_FINDING)
- Risk / Corrective Action
- Required Artifact Manifest (with before/after line counts and before/after suite results captured after `git status --short`)
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Epistemic Process Block
- Finding-To-Governance Learning Disposition
- Public Export Disposition
- Machine Closure Package
- Acceptance Receipt Assertion Matrix
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Claim Boundary

The worker records the actual `executionBaseHead` captured at start. For any
conditional block that does not apply, the worker writes `N/A with reason` (or
`NOT_APPLICABLE_WITH_REASON`) rather than omitting it. The worker must not commit
and must not edit any closed artifact.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | the extracted module imported by the dispatch-quality checker | grants no authority and changes no validation behavior | the new module, unchanged call sites, full suite | no adapter implemented | `IMPLEMENTED_AFTER_RETURN` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no CLI/MCP surface created or changed | N/A with reason: no external surface | N/A with reason: no adapter scope | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` cited for routing-format conformance only; N/A with reason: no external or legacy source is ingested |
| Input type | operator-provided external comparison, critique, or recommendation |
| Required route | the roadmap T1 routes directly into this work order; no external corpus is consulted |
| Chain map route | GFS-PY-T0 closure -> roadmap T1 -> T1 work order -> worker extraction -> reviewer closure |
| Matching local-view guard | N/A with reason: no external-knowledge-intake-scoped ingestion occurs |
| Owner surface | the dispatch-quality monolith and its split sequence |
| Disposition | refactor-only; no external intake |
| Claim boundary | the work originates from this repository's own monolith and roadmap |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
| --- | --- |
| Finding | the dispatch-quality monolith concentrated pure table-parsing helpers and validator logic in one 3056-line file, frozen as tracked debt by GFS-PY-T0 |
| Defect class | MACHINE_GATE_GAP |
| Learning lane | GOVERNANCE_CONTROL_PLANE |
| Learning disposition | RULE_EXISTS |
| Runtime/provider/cost lane | N/A_WITH_REASON: behavior-preserving authoring-time refactor with no runtime, provider, latency, token, or cost behavior |
| Promotion direction | the GFS-PY size guard and split roadmap already exist; T1 executes the first split so the monolith's exception can ratchet down |
| Next control action | T2 splits lifecycle/status validators once T1 passes |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: references internal governance checker internals and the GFS-PY split roadmap.

## Acceptance Criteria

- [ ] the named pure parsers are extracted into one new module and re-imported so call sites are unchanged;
- [ ] `_extract_section` resolves with no circular import;
- [ ] no `_validate_*`/rule logic, failure message, threshold, or test expectation changed;
- [ ] the full dispatch-quality suite passes unchanged (same pass count);
- [ ] the monolith line count is strictly smaller after the split;
- [ ] the registry `approvedMaxLines` is lowered to the new line count;
- [ ] the Python size guard is COMPLIANT with the lowered cap;
- [ ] a focused test file covers the extracted module;
- [ ] the worker did not commit and did not edit any closed artifact.

## Fail Conditions

- [ ] no `_validate_*`/rule logic moved (confirms ABSENCE);
- [ ] no failure message or threshold changed (confirms ABSENCE);
- [ ] the monolith did not stay the same size or grow (confirms ABSENCE);
- [ ] the registry cap was not left at 3056 (confirms ABSENCE).

## Closure Checklist

- [ ] new module and focused test created;
- [ ] monolith re-imports parsers; call sites unchanged;
- [ ] monolith net-shrink confirmed; registry cap lowered to match;
- [ ] full dispatch-quality suite green (unchanged pass count);
- [ ] Python size guard COMPLIANT with lowered cap;
- [ ] worker-return packet authored; no worker commit;
- [ ] reviewer independently reran the suite and confirmed behavior preservation;
- [ ] roadmap T1 moved to done; T2-T4 still held;
- [ ] GC-018 and work order closed;
- [ ] session continuity synced after the closing commit.

## Operator Checkpoint

N/A with reason: the operator confirmed the route and scope before dispatch; no
mid-pass operator checkpoint is parked.

## Return-To-Orchestrator Conditions

The worker (Codex) returns to the orchestrator/reviewer (Claude) with
`COMPLETE_PENDING_REVIEW` when all required artifacts exist and the full suite
is green, or `BLOCKED_WITH_REASON` if a clean extraction is impossible (e.g.
hidden coupling) or a gate fails outside allowed scope. The worker does not
commit and does not close.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two agents, one role each: Codex implements the extraction/tests/worker-return; Claude reviews and closes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=47a473fc`; `executionBaseHead` confirmed by Codex at start; `closureBaseHead` set by Claude before closure commit |
| changedSetScope(phase) | Codex creates the module, the test, the monolith re-import, the lowered cap, and the worker-return; Claude owns review/closure/session-sync |
| traceScope(phase, actor) | one Codex worker-return trace covers the extraction; one Claude trace covers review and closure |
| commitOwner(phase) | Codex commits nothing (`WORKER_MUST_NOT_COMMIT`); Claude owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix GFS-PY T1 with T2-T4, non-governance Python, provider/live, public-sync, or runtime work |
| Before status evidence | clean worktree at dispatch base `47a473fc` |
| nextMoveSurfaces | Claude updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | Claude is the designated reviewer and closer |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| Dispatch status | `DISPATCH_READY` | `DISPATCH_READY` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | one module, re-import, lowered cap, focused test, worker-return | as specified | PASS |
| Behavior change | none | forbidden by work order | PASS |
| Monolith size | strictly smaller, cap lowered | required | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | `governance/compat/` checker module and focused test |
| Storage decision | add one new module and one new test; shrink one existing module; lower one registry cap |
| Existing aggregate impact | none: no generated aggregate is added or changed |
| Generated state impact | none during worker execution |
| Durable governance boundary | the registry remains the single source for Python size exceptions; no hidden state store is added |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | GFS-PY T1 table-parser extraction only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - behavior-preserving extraction with before/after suite and line-count evidence |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-dispatch autorun receipt before dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-sequenced, operator-authorized work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded behavior-preserving table-parser extraction worker-return |
| forbiddenExpansion | no validator-logic move, no behavior/message/threshold change, no monolith growth, no cap retention at 3056, no T2-T4 scope, no worker commit, no external network or provider invocation |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | GFS-PY T1 work-order dispatch, 2026-06-25 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, file authoring, governance gates |
| Target paths | this work order; matching GC-018 baseline |
| Allowed scope source | operator selection of GFS-PY T1 with Codex-worker/Claude-reviewer route on 2026-06-25 |
| Before status evidence | clean worktree at HEAD `47a473fc` |
| After status evidence | GFS-PY T1 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no extraction performed by this dispatch |
| Agent type | dispatcher |
| Invocation ID | `cvf-gfs-py-t1-dispatch-quality-helper-split-for-worker-2026-06-25` |
| Expected manifest | this work order; matching GC-018 baseline |
| Actual changed set | this work order; matching GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order covers the GFS-PY T1 table-parser extraction worker-return only.
It changes no validation behavior, moves no validator logic, changes no failure
message or threshold, does not grow the monolith, does not keep the size
exception frozen at 3056, opens no T2-T4 scope, authorizes no worker commit, and
claims no runtime, provider, live, or public behavior.
