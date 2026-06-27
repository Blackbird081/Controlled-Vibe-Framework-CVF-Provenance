# CVF GC-018 GFS-PY T1 Dispatch-Quality Helper Split Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: gc018_baseline

Batch ID: GFS-PY-T1-SPLIT

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 47a473fc

executionBaseHead: 47a473fc

closureBaseHead: 9035df3c

## Purpose

Authorize GFS-PY T1, the first behavior-preserving split tranche of the
dispatch-quality monolith `governance/compat/check_work_order_dispatch_quality.py`
(3056 lines, frozen at `approvedMaxLines=3056` in the Python size registry).
T1 extracts the pure markdown-table parsing helpers into a dedicated module,
imports them back into the monolith so no behavior changes, and ratchets the
monolith's `approvedMaxLines` down to its new (smaller) line count so the
exception tightens rather than merely persists.

This tranche is a pure-helper extraction only. It does not change any
validation logic, any failure message, any check threshold, any dispatch-quality
rule, or any test expectation. The full existing dispatch-quality test suite is
the regression anchor and must pass unchanged.

## Source / Predecessor Evidence

The predecessor is GFS-PY-T1 (T0) governed Python file size coverage, closed at
material commit `fad16208`, which seeded the dispatch-quality monolith as a
frozen legacy exception with `requiredFollowup` pointing at the GFS-PY split
roadmap T1-T4. The roadmap
`docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md`
sequences T1 as "split markdown table parsing / source verification helpers"
and holds it `HOLD_UNTIL_T0_PASS`; T0 has passed, so T1 may open.

## Authority Chain

| Authority | Path | Disposition |
| --- | --- | --- |
| Active session front door | `CVF_SESSION_MEMORY.md` | T1 is an operator-selected split tranche opened after GFS-PY-T0 closure |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current mode records GFS-PY-T1 (T0) closed and T2-T4 held; this baseline opens the first split |
| GFS-PY roadmap | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | sequences T1 and holds T2-T4 |
| Python size registry | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | holds the monolith's frozen exception whose approvedMaxLines T1 ratchets down |
| Python size guard | `governance/compat/check_python_automation_size.py` | enforces the touch rule that requires the monolith to shrink, not grow, on this touch |
| Split target | `governance/compat/check_work_order_dispatch_quality.py` | the monolith from which the pure parsing helpers are extracted |
| Dispatch-quality test suite | `governance/compat/test_check_work_order_dispatch_quality.py` | the behavior-preserving regression anchor |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source Verification and dispatch packet shape |
| GC-018 template | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | continuation and blind-spot controls |
| ADIF resolver | `governance/compat/run_adif_defect_resolver.py` | defect registry queried below |

## Decision / Baseline / Proposed Tranche

Decision: dispatch GFS-PY T1 as a no-commit worker tranche (Codex worker,
Claude reviewer/closer). Baseline: the worker creates one new module
`governance/compat/check_work_order_dispatch_quality_tables.py` containing the
pure markdown-table parsing helpers `_parse_markdown_tables`,
`_parse_any_markdown_tables`, `_normalize_table_key`, `_row_value`,
`_section_tables`, `_truthy_cell`, and `_clean_manifest_path` (with
`_extract_section` either moved alongside them or imported, whichever keeps the
extraction behavior-identical), re-imports those names into
`check_work_order_dispatch_quality.py` so every existing call site is unchanged,
and ratchets the monolith's registry `approvedMaxLines` down to its new line
count. The worker also adds a focused test file for the extracted module. No
validator logic moves; no failure message changes; the full dispatch-quality
suite passes unchanged.

## Evidence / Verification

Verification for dispatch uses the Source Verification Block below, the ADIF
disclosure gate, the dispatch-prompt-envelope gate, the markdown structural
completeness gate, the work-order dispatch quality gate, the agent handoff
boundary gate, the corpus completeness gate, and the autorun pre-dispatch gate.
Worker execution evidence (full suite green, monolith net-shrink, guard
COMPLIANT with the lowered cap) belongs in the worker-return artifacts.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: this baseline
  names specific helper functions and one new module path, not a folder
  enumeration.
- ADIF-0002 - Provider-local interaction accepted as authority: this tranche
  makes no provider-local claim; it is a behavior-preserving local refactor.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class:
  exclusion prose avoids bare gate-trigger tokens that would signal a different
  evidence class than a code-refactor tranche.
- ADIF-0006 - Source Verification symbol cell contains a value/type: every
  Source Verification row below puts only a bare symbol name in the symbol
  column.

Resolver query: taskClass=`Closure`, role=`closer`, lifecyclePhase=`pre-closure`

Returned defects:

- ADIF-0003 - Closed GC-018 lacks Machine Closure Package: a complete Machine
  Closure Package appears below.
- ADIF-0008 - Reusable lesson remains only in provider memory: the split
  sequence and ratchet rule are recorded in the roadmap, the registry, and this
  baseline, not only in session memory.
- ADIF-0004 - Decided roadmap retains same-tranche parked residue: on T1
  closure the roadmap moves T1 to done and leaves no T1 open residue.
- ADIF-0005 - Closed artifact retains pending-gate residue: closure status and
  acceptance checkboxes are reconciled before the closed claim.
- ADIF-0009 - Backtick-quoted heading name truncates real section: this
  baseline does not backtick-quote any literal heading string in prose.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| The monolith defines the pure table parser to extract | `governance/compat/check_work_order_dispatch_quality.py` | line 813 | `_parse_markdown_tables` | dispatch-quality checker | EXISTS | ACCEPT |
| The monolith defines the generic table parser to extract | `governance/compat/check_work_order_dispatch_quality.py` | line 854 | `_parse_any_markdown_tables` | dispatch-quality checker | EXISTS | ACCEPT |
| The monolith defines the table-key normalizer to extract | `governance/compat/check_work_order_dispatch_quality.py` | line 881 | `_normalize_table_key` | dispatch-quality checker | EXISTS | ACCEPT |
| The monolith defines the row accessor to extract | `governance/compat/check_work_order_dispatch_quality.py` | line 885 | `_row_value` | dispatch-quality checker | EXISTS | ACCEPT |
| The monolith defines the section-table reader to extract | `governance/compat/check_work_order_dispatch_quality.py` | line 894 | `_section_tables` | dispatch-quality checker | EXISTS | ACCEPT |
| The section-table reader depends on the section extractor | `governance/compat/check_work_order_dispatch_quality.py` | line 517 | `_extract_section` | dispatch-quality checker | RUNTIME_BEHAVIOR | ACCEPT |
| The monolith defines the truthy-cell helper to extract | `governance/compat/check_work_order_dispatch_quality.py` | line 899 | `_truthy_cell` | dispatch-quality checker | EXISTS | ACCEPT |
| The monolith defines the manifest-path cleaner to extract | `governance/compat/check_work_order_dispatch_quality.py` | line 904 | `_clean_manifest_path` | dispatch-quality checker | EXISTS | ACCEPT |
| The monolith is a frozen registry exception that must shrink, not grow, on touch | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | `check_work_order_dispatch_quality.py` exception entry | `approvedMaxLines` | Python size registry | VALUE_SET | ACCEPT |
| The Python size guard fails an excepted file that grows on touch | `governance/compat/check_python_automation_size.py` | exception-touch branch | `exception_file_grew_on_touch` | Python size guard | RUNTIME_BEHAVIOR | ACCEPT |

## Continuation Decision

| Field | Disposition |
| --- | --- |
| Selected tranche | GFS-PY T1 - dispatch-quality pure table-parsing helper split |
| Dispatch status | CLOSED_PASS_BOUNDED |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closer | Claude reviewer/closer |
| Reason for no worker commit | the monolith is the central dispatch-quality checker that gates every governed work order; the reviewer must independently confirm the extraction is behavior-identical and the full suite passes before it is committed |
| Relationship to T2-T4 | T1 only; T2-T4 remain held until their predecessor passes |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap tranche | Work order | Disposition |
| --- | --- | --- |
| GFS-PY T1 | `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md` | dispatched by this baseline |
| GFS-PY T2-T4 | none | HOLD_UNTIL_PREDECESSOR_PASS; no work order authored |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | the extracted table-parsing module imported by the dispatch-quality checker | the extraction grants no authority and changes no validation behavior | the new module, the unchanged call sites, and the full suite | no adapter implemented | `IMPLEMENTED_AFTER_RETURN` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no CLI/MCP surface is created or changed | N/A with reason: no external surface | N/A with reason: no adapter scope | `NOT_APPLICABLE_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Disposition |
| --- | --- |
| Legacy scan classification | NOT_APPLICABLE_WITH_REASON |
| Scan root | N/A with reason: T1 scans no external or legacy corpus; it extracts helpers from one local module |
| Required worker action | extract only the named pure parsing helpers; keep all validator logic in place |
| Forbidden shortcut | do not change any validation behavior, failure message, or test expectation; do not grow the monolith |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control |
| --- | --- |
| Hidden behavior change during extraction | the full dispatch-quality suite is the regression anchor and must pass unchanged; the worker must run it before and after |
| Moving validator logic by mistake | only the named pure parsing helpers move; `_validate_*` and rule logic stay in the monolith |
| Circular import on `_extract_section` | the worker must move `_extract_section` alongside the parsers or import it cleanly so no circular import is introduced |
| Monolith not actually shrinking | the registry `approvedMaxLines` must be lowered to the new line count; the Python size guard fails the touch if the file grows |
| Scope creep into T2-T4 | only table-parsing helpers move; lifecycle/status, source-verification, and token-collision validators are T2-T4 |

## Corpus Completeness And Report Integrity

- Corpus task class: GOVERNANCE_CHECKER_REFACTOR.
- Corpus root: the dispatch-quality monolith, its test suite, the Python size
  registry, and the GFS-PY roadmap.
- Snapshot time: 2026-06-25.
- Enumeration command: `rg --files --hidden --no-ignore governance/compat` to
  confirm no existing `check_work_order_dispatch_quality_tables.py` collision
  before dispatch.
- Manifest artifact or inline manifest: this baseline and the matching work
  order define the required output manifest.
- Manifest hash: N/A with reason: dispatch packet only; no corpus snapshot is
  owned by this tranche.
- Processing ledger artifact or inline ledger: the worker-return's required
  artifact manifest plus the before/after suite runs and monolith line counts.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=new_module_plus_monolith_import_plus_registry_plus_tests; schema=extracted_pure_parsers; ledger_terminal=before_after_suite_and_line_count; exclusions=validator_logic_move_or_behavior_change_or_monolith_growth; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no validator logic moved; no behavior or message change;
  no monolith growth; no scope into T2-T4; no network/provider call.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: T1 creates no generated aggregate.
- Drift check: N/A with reason: T1 creates no generated aggregate.
- Output traceability: each extracted helper maps to a named Source
  Verification line in the monolith.
- Adversarial verification: the reviewer must independently run the full
  dispatch-quality suite, confirm it passes unchanged, and confirm the monolith
  shrank and its registry cap was lowered to match.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` cited for routing-format conformance only; N/A with reason: no external or legacy source is ingested |
| Input type | operator-provided external comparison, critique, or recommendation |
| Required route | the GFS-PY roadmap T1 routes directly into this GC-018 as a bounded refactor tranche; no external corpus is consulted |
| Chain map route | GFS-PY-T0 closure -> roadmap T1 hold lifted -> T1 GC-018 -> worker extraction -> reviewer closure |
| Matching local-view guard | N/A with reason: no external-knowledge-intake-scoped ingestion occurs |
| Owner surface | the dispatch-quality monolith and its split sequence |
| Disposition | refactor-only; no external intake |
| Claim boundary | the work originates from this repository's own monolith and roadmap |

## Rescan Intelligence Hardening

- Original source artifact: `governance/compat/check_work_order_dispatch_quality.py`
- Predecessor intake artifact: N/A with reason: no predecessor governed
  reference document is rescanned; this tranche extracts helpers from one local
  module per the roadmap
- Delta ledger status: worker must record the before/after monolith line counts
  and the full-suite result in the worker-return packet
- Routing matrix status: worker must refresh in the worker-return packet
- Semantic sampling status: worker must include at least three samples in the
  worker-return packet
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch treatment |
| --- | --- |
| `UNCHANGED_FROM_INTAKE` | every validation rule, failure message, threshold, and test expectation is kept identical |
| `CHANGED_DISPOSITION` | the pure table-parsing helpers move from the monolith into a dedicated module and are re-imported |
| `NEW_FINDING` | any hidden coupling that prevents a clean extraction (e.g. a parser that secretly reads module state) must be raised as a finding, not silently reshaped |
| `REMOVED_OR_REJECTED` | any validator-logic move, behavior change, message change, monolith growth, or T2-T4 scope is rejected |

### Follow-Up Routing Matrix

| Routing lane | Dispatch treatment |
| --- | --- |
| `DO_NOW` | extract the named pure parsers, re-import them, lower the registry cap, add the focused test, run the full suite, and author the worker-return |
| `SEPARATE_RUNTIME_TRANCHE` | lifecycle/status validators (T2), source-verification/token-collision validators (T3), and the orchestrator-shell reduction (T4) are later tranches |
| `STRATEGIC_OPERATOR_DECISION` | the order and timing of T2-T4 is the operator's to sequence |
| `OUT_OF_SCOPE` | any behavior change, network/provider call, runtime/provider/live behavior, or public-sync |
| `RESOLVED_BY_DESIGN` | behavior preservation is proven by the unchanged full dispatch-quality suite, not by reviewer opinion |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| GFS-PY-T1-SPLIT-S1 | monolith line 815 | `_parse_markdown_tables` is a pure function of its text argument | extracted module reproduces identical rows | could the parser secretly depend on a module-level constant | reject - the worker must confirm the parser reads only its argument and `re`, else raise a NEW_FINDING |
| GFS-PY-T1-SPLIT-S2 | monolith line 896 | `_section_tables` calls `_extract_section` | extraction keeps the call resolvable with no circular import | could moving the parsers but not `_extract_section` break the import graph | reject - the worker must move `_extract_section` with them or import it cleanly |
| GFS-PY-T1-SPLIT-S3 | registry exception | the monolith is frozen and must shrink on touch | registry approvedMaxLines is lowered to the new count | could the worker keep the cap at 3056 and let the file merely not grow | reject - T1 must ratchet the cap down to the new line count |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this tranche references internal governance checker internals and the
GFS-PY split roadmap.

## Acceptance Criteria

- The named pure table-parsing helpers are extracted into one new module and
  re-imported so every existing call site is unchanged.
- No validator logic, failure message, threshold, or test expectation changes.
- The full `test_check_work_order_dispatch_quality.py` suite passes unchanged.
- The monolith's line count drops and its registry `approvedMaxLines` is lowered
  to the new count.
- The Python size guard is COMPLIANT with the lowered cap.
- A focused test file covers the extracted module.
- T1 does not open or alter T2-T4.

## Fail Conditions

Fail dispatch or return if the worker moves any `_validate_*` or rule logic,
changes any failure message or threshold, changes any test expectation, leaves
the monolith the same size or larger, keeps the registry cap at 3056, commits
anything, introduces a circular import, or scopes into T2-T4.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Roadmap state | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | T1 dispatched by this baseline; T2-T4 held | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | monolith approvedMaxLines lowered to the new count after return | PASS |
| Registry Markdown | N/A with reason | the Python size guard has no companion markdown registry | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported | N/A with reason |
| System loop interlock | this baseline | T0 closure was required before T1; T1 closure is required before T2 | PASS |
| Session continuity | active session sync after the closing commit | separate session-sync lane | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| Closure status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | one new module, re-import, lowered cap, focused test, worker return | as specified | PASS |
| Behavior change | none | 86/86 suite unchanged | PASS |
| Monolith size | strictly smaller, cap lowered | 3056 -> 2972, cap 2972 | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | GFS-PY T1 dispatch baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - behavior-preserving helper-split worker-return lane, dispatch-ready |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-dispatch autorun receipt captured before dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-sequenced, operator-authorized work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded behavior-preserving table-parser extraction worker-return |
| forbiddenExpansion | no validator-logic move, no behavior/message/threshold change, no monolith growth, no cap retention at 3056, no T2-T4 scope, no commit by worker, no network/provider call |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | GFS-PY T1 work-order dispatch, 2026-06-25 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, file authoring, governance gates |
| Target paths | this baseline; matching GFS-PY T1 work order |
| Allowed scope source | operator selection of GFS-PY T1 with Codex-worker/Claude-reviewer route on 2026-06-25 |
| Before status evidence | clean worktree at HEAD `47a473fc` |
| After status evidence | GFS-PY T1 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no extraction performed by this dispatch |
| Agent type | dispatcher |
| Invocation ID | `cvf-gfs-py-t1-dispatch-quality-helper-split-dispatch-2026-06-25` |
| Expected manifest | this baseline; matching GFS-PY T1 work order |
| Actual changed set | this baseline; matching GFS-PY T1 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes GFS-PY T1 worker-return execution only. It does not
extract any helper, change the monolith, lower the registry cap, run the test
suite, close T1, commit anything, or open or alter T2-T4. The worker must not
commit; the reviewer closes after independently confirming behavior preservation
and the monolith net-shrink.
