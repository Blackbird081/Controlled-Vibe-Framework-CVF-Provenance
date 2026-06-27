# CVF GC-018 EQC-T1 Worker Return Equivalence Claim Evidence Linter Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: gc018_baseline

Batch ID: EQC-T1

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: a63de6d3

executionBaseHead: a63de6d3

closureBaseHead: a63de6d3

## Purpose

Authorize a bounded, narrow EQC-T1 worker-return lane that builds a single
new static-pattern checker detecting unverified source-equivalence claims in
governed worker-return and completion-review markdown. This closes the
governance signal the ASSF-T4 reviewer raised: a worker-return self-reports
that a clause, field, or value "is the same as," "verbatim," or otherwise
unchanged from a cited source, without an adjacent literal evidence command
(`rg`, `git diff --no-index`, or an explicit line-by-line table) proving it.
This pattern occurred twice in the ASSF lane (T3 implicitly, T4 explicitly)
and was caught only by manual reviewer re-derivation both times.

This tranche is checker-authoring-only. It does not implement any retroactive
rewrite of existing closed worker-returns, does not change any ASSF tranche
status, does not implement an LLM-judge or any provider/network call, and
does not implement a per-step or per-role gate.

## Source / Predecessor Evidence

The predecessor evidence is the ASSF-T4 completion review's
Finding-To-Governance Learning Disposition escalation
(`docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`),
which raised the disposition from `RULE_EXISTS` to `MACHINE_CHECK_CANDIDATE`
and recorded a concrete linter proposal: flag equivalence language used about
a named source file when no adjacent literal evidence-command pair is
present. The operator subsequently bound this proposal to a no-bottleneck
constraint requiring one checker, one full-diff pass at an existing gate
phase, static pattern matching only (no LLM/network call), and
role-count-invariant behavior, recorded in operator-memory
`project_assf_lane_2026-06-23` (not itself a CVF-governed artifact; this
GC-018 promotes the constraint into governed scope by binding it to the
work order's Allowed Scope and Forbidden Scope).

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | EQC-T1 is an operator-selected micro-governance tranche opened before ASSF-T5 |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current lane records ASSF-T4 closed; this baseline opens the EQC-T1 side lane |
| ASSF-T4 completion review | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md` | source of the `MACHINE_CHECK_CANDIDATE` disposition this tranche resolves |
| ASSF roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | records the same escalation in its Finding-To-Governance Learning Disposition section |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source Verification and dispatch packet shape |
| GC-018 template | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | continuation and blind-spot controls |
| Rescan-intelligence checker precedent | `governance/compat/check_rescan_intelligence_hardening.py` | structural and CLI precedent this tranche's checker mirrors (changed-range diff, `--base`/`--head`, violations list, `main()` exit code) |
| ADIF resolver | `governance/compat/run_adif_defect_resolver.py` | defect registry queried below for this dispatch's own task class |
| ADIF-0009 entry | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0009.md` | governs heading-literal-in-prose risk this checker's own pattern list must avoid triggering |
| Hook chain registry | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS` list this tranche's checker is wired into |

## Decision / Baseline / Proposed Tranche

Decision: dispatch EQC-T1 as a no-commit, checker-authoring-only
worker-return tranche that builds one new file,
`governance/compat/check_equivalence_claim_evidence.py`, wires it as a single
new entry into `REVIEWER_FAST_CHECKS`, and adds focused tests. Baseline: the
checker scans changed `docs/reviews/*.md` files plus any changed file under
the work-orders directory containing a worker-return block, for a closed set of
equivalence-claim phrases ("verbatim", "identical", "no new field", "maps to
existing", "unchanged", "same as", "reused exactly") appearing within the
same paragraph as a reference to a named source file or contract. When such a
co-occurrence is found, the checker requires, within a bounded character
window, either a fenced/inline command-and-result pair (`rg`, `git diff
--no-index`, or equivalent) or an explicit disposition token (`MATCH`,
`ADAPTED_WITH_REASON`, `NEW_FIELD_INTRODUCED`, `NOT_LITERAL_WITH_REASON`).
Absence of both fails the check. The checker proves nothing about whether the
underlying claim is true; it only fails when an equivalence claim lacks
adjacent evidence.

## Evidence / Verification

Verification for dispatch uses the Source Verification Block below, the
ADIF defect registry disclosure gate, the dispatch-prompt-envelope gate, the
markdown structural completeness gate, the work-order dispatch quality gate,
the agent handoff boundary gate, the corpus completeness gate, and the
autorun pre-dispatch gate. Worker execution evidence belongs in the
worker-return artifacts.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: this
  dispatch makes no exhaustive-directory claim; it names one new file path
  and one registry-list edit, not a folder enumeration.
- ADIF-0002 - Provider-local interaction accepted as authority: the checker
  itself enforces the opposite of this defect (it rejects unverified
  provider/source claims); this dispatch makes no provider-local claim of its
  own.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class:
  this dispatch's Forbidden Scope and exclusion prose avoid bare gate-trigger
  tokens (`corpus`, `classification`, `readiness`, `rescan`) where they would
  falsely signal a different evidence class than checker-authoring.
- ADIF-0009 - Backtick-quoted heading name truncates real section: this
  baseline and its work order must not quote any literal `## <Exact Heading
  Text>` string inside backticks in prose; verified by reading this file back
  before dispatch (no such pattern appears below).
- ADIF-0006 - Source Verification symbol cell contains a value/type: every
  row in the Source Verification Block below puts only a bare field/path/
  symbol name in the `Verified path or symbol` column, never a value
  assignment or type annotation.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| `check_rescan_intelligence_hardening.py` uses a changed-range diff pattern with `--base`/`--head` args, a `main()` entry point, and a violations list this new checker should mirror | `governance/compat/check_rescan_intelligence_hardening.py` | function definitions block | `_get_changed_name_status`; `_add`; `main` | rescan-intelligence checker | RUNTIME_BEHAVIOR | ACCEPT |
| `REVIEWER_FAST_CHECKS` is the list this tranche's checker entry must be appended to | `governance/compat/run_local_governance_hook_chain.py` | line 24 | `REVIEWER_FAST_CHECKS` | hook chain runner | RUNTIME_BEHAVIOR | ACCEPT |
| The ADIF resolver exposes `resolve_defect_packet` taking `task_class`, `role`, `lifecycle_phase`, `surface_selector`, `risk_ceiling` keyword args | `governance/compat/run_adif_defect_resolver.py` | function definition | `resolve_defect_packet` | ADIF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| The known taskClasses/roles in the ADIF registry include `Work-order authoring / dispatch` and role `dispatcher` | `governance/compat/run_adif_defect_resolver.py` (entries loaded via `load_entries`) | entry `task_classes`/`roles` fields | `load_entries` | ADIF resolver | VALUE_SET | ACCEPT |
| The ASSF-T4 completion review escalated the disposition to `MACHINE_CHECK_CANDIDATE` and recorded the concrete linter proposal this tranche implements | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md` | Finding-To-Governance Learning Disposition | MACHINE_CHECK_CANDIDATE | ASSF-T4 completion review | LITERAL_INVARIANT | ACCEPT |
| The work order template requires a `## Dispatch Prompt Envelope` as the first `##` section, no later than line 25 | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | Envelope Placement | Dispatch Prompt Envelope | dispatch prompt envelope standard | LITERAL_INVARIANT | ACCEPT |

## Continuation Decision

| Field | Disposition |
|---|---|
| Selected tranche | EQC-T1 - Worker Return Equivalence Claim Evidence Linter (checker-authoring-only) |
| Dispatch status | CLOSED_PASS_BOUNDED |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closer | Claude reviewer/closer |
| Reason for no worker commit | a new checker wired into `REVIEWER_FAST_CHECKS` affects every future governed worker-return; the reviewer must independently confirm the pattern list does not false-fire on the existing closed-tranche corpus before it is committed |
| Relationship to ASSF-T5 | independent micro-governance tranche; does not block or require ASSF-T5 selection |

## Roadmap-To-Work-Order Trace Matrix

N/A with reason: EQC-T1 is not derived from a roadmap tranche; it is a
direct operator-authorized micro-governance response to a completion-review
finding. The Source / Predecessor Evidence and Decision sections above serve
the same trace function this matrix would otherwise provide.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `check_equivalence_claim_evidence.py` running inside `REVIEWER_FAST_CHECKS` | the checker only flags missing evidence; it grants no agent additional authority and blocks no path beyond the reviewer-fast gate | checker source and tests | no adapter implemented | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | none | this tranche exposes no CLI/MCP surface; the checker runs only inside the existing local hook chain | N/A with reason: no external surface created | N/A with reason: no adapter scope exists for this tranche | `NOT_APPLICABLE_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Disposition |
|---|---|
| Legacy scan classification | NOT_APPLICABLE_WITH_REASON |
| Scan root | N/A with reason: EQC-T1 does not scan `.private_reference/legacy/` or any external corpus; it authors one new local checker |
| Required worker action | mirror the existing `check_rescan_intelligence_hardening.py` structural pattern; do not invent a new diff/range-resolution approach |
| Forbidden shortcut | do not register a second standalone autorun phase entrypoint when one `REVIEWER_FAST_CHECKS` list entry is sufficient |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control |
|---|---|
| Scope creep into a per-step or per-role gate | Forbidden Scope below explicitly bars wiring the checker into more than one `REVIEWER_FAST_CHECKS` entry or into any per-agent/per-role-count loop |
| False-positive risk against existing closed corpus | worker must run the new checker against the full `docs/reviews/` and the work-orders directory history (read-only dry run) and report any false-fire before the checker is wired as enforcing |
| Heading-literal-in-prose trap (ADIF-0009) | the checker's own pattern list and this dispatch's prose must not backtick-quote any real `## Heading` string |
| Evidence-requirement scope creep | the checker proves only adjacency of an evidence-command-or-disposition-token; it must not attempt to execute the cited `rg`/`git diff` command itself or verify the claim's truth |
| LLM-judge scope creep | Forbidden Scope below bars any network or provider call from the checker |

## Corpus Completeness And Report Integrity

- Corpus task class: GOVERNANCE_CHECKER_AUTHORING.
- Corpus root: this GC-018 baseline, the matching EQC-T1 work order, the
  ASSF-T4 completion review, and the rescan-intelligence checker precedent.
- Snapshot time: 2026-06-25.
- Enumeration command: `rg --files --hidden --no-ignore governance/compat` to
  confirm no existing `check_equivalence_claim_evidence.py` collision before
  dispatch.
- Manifest artifact or inline manifest: this baseline and the matching work
  order define the required output manifest.
- Manifest hash: N/A with reason: dispatch packet only; no corpus snapshot is
  owned by this tranche.
- Processing ledger artifact or inline ledger: the worker-return's Required
  Artifact Manifest and the false-positive dry-run report.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=checker_plus_tests_plus_worker_return; schema=new_checker_pattern_list; ledger_terminal=dry_run_report_in_worker_return; exclusions=retroactive_rewrite_or_llm_judge_or_per_step_gate; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no retroactive edit of any existing closed
  worker-return or completion review; no second checker entrypoint; no
  network/provider call; no per-step or per-role gate.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: EQC-T1 creates no generated aggregate.
- Drift check: N/A with reason: EQC-T1 creates no generated aggregate.
- Output traceability: the worker-return maps the checker's pattern list and
  evidence-window logic to the ASSF-T4 completion review's concrete proposal.
- Adversarial verification: the reviewer must confirm the checker does not
  false-fire on any existing closed-tranche worker-return or completion
  review, and that it remains a single full-diff-pass static-pattern check,
  not a per-step or per-role gate.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` cited for routing-format conformance only; N/A with reason: this tranche ingests no external or legacy source through that chain map, it authors a local checker from an internal completion-review finding |
| Input type | operator-provided external comparison, critique, or recommendation |
| Required route | the ASSF-T4 reviewer finding routes directly into this GC-018 as a bounded checker-authoring tranche; no external corpus is consulted |
| Chain map route | ASSF-T4 completion review finding -> operator no-bottleneck constraint -> EQC-T1 GC-018 -> checker -> reviewer-fast gate |
| Matching local-view guard | N/A with reason: no `governance/compat/check_external_knowledge_intake_routing.py`-scoped intake occurs in this tranche |
| Owner surface | EQC-T1 checker and any future EQC-T2 widening tranche |
| Disposition | checker-authoring only; no external intake |
| Claim boundary | the finding originates from this repository's own governed completion review, not an external or legacy source |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: N/A with reason: no predecessor governed
  reference document is being rescanned; this tranche responds to a
  completion-review finding, not a corpus rescan
- Delta ledger status: worker must refresh in the worker-return packet.
- Routing matrix status: worker must refresh in the worker-return packet.
- Semantic sampling status: worker must include at least three samples in the
  worker-return packet.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch treatment |
|---|---|
| `UNCHANGED_FROM_INTAKE` | the ASSF-T4 reviewer's concrete linter proposal (phrase list, evidence-window requirement, disposition tokens) is implemented as specified, not redesigned |
| `CHANGED_DISPOSITION` | the finding moves from a recorded `MACHINE_CHECK_CANDIDATE` disposition to an implemented, tested, enforcing checker |
| `NEW_FINDING` | any equivalence-claim phrasing or evidence form the worker discovers in real closed worker-returns that the original proposal did not anticipate must be raised as a checker-design gap, not silently absorbed |
| `REMOVED_OR_REJECTED` | any design that would require a network/provider call, a per-step or per-role gate, or retroactive editing of existing closed artifacts is rejected |

### Follow-Up Routing Matrix

| Routing lane | Dispatch treatment |
|---|---|
| `DO_NOW` | author the checker, wire it into `REVIEWER_FAST_CHECKS`, write tests, run the false-positive dry run, and author the worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | widening the scanned-file set beyond `docs/reviews/*.md` and worker-return blocks in the work-orders directory is a future EQC-T2 decision |
| `STRATEGIC_OPERATOR_DECISION` | whether to retroactively annotate any pre-existing closed worker-return that the dry run flags is deferred to the operator |
| `OUT_OF_SCOPE` | LLM-judge verification of claim truth, per-step/per-role gating, runtime/provider/live behavior, public-sync |
| `RESOLVED_BY_DESIGN` | the single-checker, single-gate-phase, static-pattern, role-count-invariant constraint is satisfied by construction, not by later repair |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| EQC-T1-S1 | ASSF-T4 completion review Finding-To-Governance Learning Disposition | equivalence claims need an adjacent evidence-command pair | checker requires evidence window or disposition token | could a worker satisfy the checker by writing the word "verbatim" next to an unrelated `rg` command for a different file | reject - checker must require the evidence reference to name the same source path as the claim |
| EQC-T1-S2 | operator no-bottleneck constraint (recorded in this baseline's Decision section) | one checker, one gate phase, static pattern only | checker design uses no network/provider call and one `REVIEWER_FAST_CHECKS` entry | could a future worker split this into a pre-dispatch AND pre-closure duplicate entry | reject - Forbidden Scope below bars a second autorun wiring point |
| EQC-T1-S3 | ADIF-0009 entry | backtick-quoted heading text falsely matches section-extraction logic | this checker does not use heading-based section extraction at all; it scans paragraph-bounded text windows | could the checker's own phrase list (e.g. quoting "verbatim" in backticks within this baseline) trip another checker's literal-match logic | reject - this baseline quotes the phrases in prose without backticks around any `##` heading string |

| Requirement | Dispatch control |
|---|---|
| Avoid repeated omission | the checker must cover both `docs/reviews/*.md` and worker-return blocks inside the work-orders directory, not only one of the two surfaces named in the ASSF-T4 finding |
| Preserve useful evidence detail | the checker's failure message must name the matched phrase, the cited source path, and the missing-evidence reason so a worker can repair without guessing |
| Convert review friction into learning | the worker must record any phrase or evidence-form gap discovered while authoring the checker as a Finding-To-Governance disposition |
| Keep machine-check candidate visible | the worker must state in the return whether a future EQC-T2 should widen the scanned-file set |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this tranche references internal completion-review and ASSF lane
governance findings. Public-facing documentation of the checker, if any, is a
later public-sync decision out of this tranche's scope.

## Acceptance Criteria

- EQC-T1 work order is source-verified against the rescan-intelligence
  checker precedent, the hook-chain registry, the ADIF resolver, and the
  ASSF-T4 completion review.
- Worker return is constrained to authoring exactly one new checker file,
  one `REVIEWER_FAST_CHECKS` entry, paired tests, and the worker-return
  packet; no commit, no retroactive edit of existing closed artifacts, no
  second autorun entrypoint, no network/provider call.
- The checker implements the no-bottleneck constraint by construction: one
  checker, one full-diff pass at the existing `reviewer-fast` gate phase,
  static pattern matching only, identical behavior regardless of declared
  route mode or role count.
- The checker is run as a read-only dry run against the existing
  `docs/reviews/` and the work-orders directory history and any false-fire is
  reported in the worker return before the entry is wired as enforcing.
- EQC-T1 does not block, require, or alter ASSF-T5 selection.

## Fail Conditions

Fail dispatch or return if the packet registers more than one new
`governance/compat/check_*.py` file, wires the checker into more than one
`REVIEWER_FAST_CHECKS` (or any other autorun phase list) entry, adds a
network/provider/LLM-judge call to the checker, retroactively edits any
existing closed worker-return or completion review, or designs the checker
to run once per agent/role/step rather than once per full-diff pass.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | the ASSF roadmap is cited only as the source of the ASSF-T4 finding this tranche resolves; EQC-T1 does not modify the ASSF roadmap's tranche status, ASSF-T5 selection, or any roadmap field | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_FOR_WORKER_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md` | `Status: COMPLETE_PENDING_REVIEW`, accepted after reviewer field-label repair | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: EQC-T1 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: EQC-T1 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported | N/A with reason |
| System loop interlock | this baseline | the ASSF-T4 completion review's escalation was required before this tranche; this tranche's checker becomes a reusable gate for all future worker-returns; no automatic retroactive enforcement on past closed artifacts | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch status | `DISPATCH_READY` | `DISPATCH_READY` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | one new checker, one hook-chain entry, tests, worker return only | as specified | PASS |
| No-bottleneck constraint | one checker, one gate phase, static pattern, role-count-invariant | required by work order | PASS |
| Network/provider call | forbidden | forbidden by work order | PASS |
| Retroactive edit of closed artifacts | forbidden | forbidden by work order | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | EQC-T1 dispatch baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - checker-authoring worker-return lane, dispatch-ready |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-dispatch autorun receipt captured below before dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-independent, operator-authorized work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded worker-return equivalence-claim-evidence checker |
| forbiddenExpansion | no second checker entrypoint, no network/provider/LLM-judge call, no per-step/per-role gate, no retroactive edit of closed artifacts, no runtime/provider/live or public-sync behavior |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | EQC-T1 work-order dispatch, 2026-06-25 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, file authoring, governance gates |
| Target paths | this baseline; matching EQC-T1 work order |
| Allowed scope source | operator instruction to scope and author the EQC-T1 dispatch after agreeing the no-bottleneck constraint |
| Before status evidence | clean worktree at HEAD `a63de6d3` (`git status --short` empty before this dispatch pair) |
| After status evidence | EQC-T1 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no checker authoring performed by this dispatch |
| Agent type | dispatcher |
| Invocation ID | `cvf-eqc-t1-worker-return-equivalence-claim-evidence-linter-dispatch-2026-06-25` |
| Expected manifest | this baseline; matching EQC-T1 work order |
| Actual changed set | this baseline; matching EQC-T1 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes EQC-T1 worker-return execution only. It does not
author the checker, wire the hook-chain entry, write tests, close EQC-T1,
edit any existing closed worker-return or completion review, run any
network/provider/LLM-judge call, or authorize any per-step or per-role gate.
