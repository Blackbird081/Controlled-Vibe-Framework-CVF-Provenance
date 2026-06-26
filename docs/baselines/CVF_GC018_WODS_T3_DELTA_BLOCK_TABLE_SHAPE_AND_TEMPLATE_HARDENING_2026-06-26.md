# CVF GC-018 Baseline: WODS-T3 Delta Block Table Shape And Template Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: WODS-T3

dispatchBaseHead: `d09ea747`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex for the returned worker packet.

Canonical packet:
`docs/baselines/CVF_GC018_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_2026-06-26.md`

Paired work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_FOR_CLAUDE_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Current-time notes: ASSF-PIC-T3 closed bounded at material commit `9c621ba6`
with `INTEGRATION_DEFERRED_CERTIFICATION_HELD`. ASSF-PIC-T4 is
`HOLD_WODS_REOPEN_AFTER_PIC_T3`. This baseline releases only WODS hardening
for the four concrete T3-observed authoring defects; it does not release
ASSF-PIC-T4.

Do-not-misread notes: this baseline does not release ASSF-PIC-T4, create a
package instance, certify a package, mutate ASSF generated indexes or
registries, change resolver or Web runtime behavior, implement CLI/MCP
adapter behavior, run provider/live proof, public-sync, push, or
session-sync.

## Proposed Tranche

Tranche: WODS-T3 Delta Block Table Shape And Template Hardening.

Baseline decision: authorize a bounded no-commit Claude worker tranche to
fix the four concrete authoring-friction defects Codex's ASSF-PIC-T3
completion review recorded in its Finding-To-Governance Learning
Disposition table:

- the worker-return scaffold's `Delta Execution Claim Boundary Control
  Block` default body is plain `key: value` prose, not the `Field`/`Value`
  table the checker's row-parser actually requires;
- decision-review-shaped work orders do not pre-emptively guide the worker
  toward the generic structural headings `check_markdown_structural_completeness.py`
  expects for a `review`-classified artifact, so the gap is discovered only
  during live fast-gate repair rounds rather than avoided up front;
- the literal-format gotchas checklist does not yet record either of the
  above two traps, or the long-content/backtick `write_to_file`-style
  argument-parsing friction the operator reported during T3 execution;
- the work-order template's ASCII-encoding guidance is not restated close
  enough to the decision-review-shape section to prevent a worker from
  drafting an em-dash before the agent-packet-authority-and-encoding gate
  catches it.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: COMPLETE_PENDING_REVIEW_ACCEPTED
- Reviewer verdict: CLOSED_PASS_BOUNDED

## Purpose

Reduce the fourth consecutive cycle of work-order/scaffold authoring-friction
discovery (T1->WODS-T1, T2->WODS-T2, T3->this WODS-T3) by fixing the
scaffold default and template guidance gaps that caused Claude's ASSF-PIC-T3
worker execution to need 3 fast-gate repair rounds for already-familiar
defect classes (missing structural sections, prose-shaped Delta block,
ASCII violation).

This tranche is process/tooling hardening only. It is not an ASSF package
integration task and it does not advance ASSF-PIC-T4 or the package
certification lane.

## Evidence / Verification

Dispatch evidence is limited to current CVF-governed source surfaces:

- ASSF-PIC-T3 completion review and worker return;
- WODS-T2 completion review (prior hardening cycle and its own residual
  risk note);
- worker-return scaffold helper;
- Delta execution claim boundary guard;
- markdown structural completeness guard;
- canonical work-order template and literal-format gotchas checklist.

Worker-created implementation diffs and worker-return evidence do not exist
at dispatch time and must not be claimed as complete until the worker
returns uncommitted artifacts and Codex accepts them.

## Scope / Applies To

Applies to:

- worker-return scaffold `Delta Execution Claim Boundary Control Block`
  default body and a focused regression test for its table shape;
- work-order template guidance that names the generic structural sections a
  `review`-classified decision artifact needs before drafting, not only
  after a gate failure;
- literal-format gotchas guidance for the newly observed prose-vs-table trap
  and the operator-reported tool/encoding friction;
- worker evidence that measures whether this tranche reduces repeat
  fast-gate repair rounds compared to T1/T2/T3 observations.

Does not apply to:

- ASSF-PIC-T4 dispatch or execution;
- package instance creation, activation, instruction execution,
  certification, generated-index mutation, resolver mutation,
  registry-source mutation, Web runtime mutation, CLI/MCP adapter behavior,
  provider/live proof, public-sync, push, or session-sync.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-PIC-T3 reviewer closure exists and keeps T4 held | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` lines 56-71 and 164-171 |
| T3 closure routes WODS follow-up defects to a separate hardening lane before T4 | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` lines 91 and 197-201 |
| T3 worker return and completion review record the exact scaffold/template defects | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` lines 62-71 and 164-171 |
| WODS-T2 closed bounded and improved the first two friction sources from the prior WODS-T1 cycle | SATISFIED | `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` lines 52-68 |
| Dispatch worktree isolation before WODS-T3 authoring | SATISFIED | `git status --short` returned no paths before authoring |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T3 closure routes 4 residual defects to WODS follow-up and holds T4 | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` | lines 164-171 | `REOPEN_CONDITION_FIRED` | ASSF-PIC-T3 completion review | VALUE_SET | ACCEPT |
| Scaffold's Delta Execution Claim Boundary Control Block default body is prose, not a table | `governance/compat/run_worker_return_scaffold.py` | lines 154-161 | `Delta Execution Claim Boundary Control Block` | worker-return scaffold helper | RUNTIME_BEHAVIOR | ACCEPT |
| Delta execution claim boundary guard parses only markdown table rows for required fields | `governance/compat/check_delta_execution_claim_boundary.py` | lines 218-228 and 248-265 | `_field_rows` | Delta execution claim boundary guard | RUNTIME_BEHAVIOR | ACCEPT |
| Markdown structural completeness requires risk/corrective action and other generic sections for review-classified artifacts | `governance/compat/check_markdown_structural_completeness.py` | lines 142 and 217-223 | `SECTION_GROUPS` | markdown structural completeness guard | LITERAL_INVARIANT | ACCEPT |
| Agent-authored governed artifacts default to ASCII; em dashes use a hyphen or colon instead | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | lines 33-42 | `## Rule` | text encoding and symbol discipline standard | LITERAL_INVARIANT | ACCEPT |
| Literal-format gotchas checklist currently ends at item 22 with no table-shape or tool-parsing trap recorded | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | lines 201-226 | item 22 | governed artifact literal gotchas | EXISTS | ACCEPT |
| Work-order template's no-commit worker-return guidance section exists and is the prior WODS-T2 edit point | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 899-960 | no-commit worker-return guidance | work-order template | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Active session next move | read current bootstrap read model | next allowed move is a fresh WODS follow-up before ASSF-PIC-T4 | current |
| ADIF resolver disclosure | ran resolver import for dispatch task class | returned ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006 | disclosed below |
| Worktree isolation | checked before authoring | `git status --short` returned no paths | clean at dispatch start |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This baseline names bounded files and avoids directory-total
  claims.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Exclusion prose is marked as boundary text, not evidence of a
  performed scan or package action.
- ADIF-0006: Verified path or symbol cells contain only fields, functions,
  sections, paths, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request and the T3 completion review's operator-reported worker-experience friction routed to the governed WODS source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this WODS-T3 baseline and paired work order |
| Disposition | dispatch-authoring hardening only; no external artifact import or package certification |
| Claim boundary | operator-reported friction is treated as process evidence and re-verified against CVF-governed source files before dispatch |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: worker must read current source files, implement bounded
changes, and rerun focused tests/gates instead of relying on chat memory.

unicodePathHandling: literal path or UTF-8 reader required.

extractedTextAuthority: N/A with reason

priorVerificationUse: T3 worker return and completion review are
defect-source evidence only; implementation correctness must be proven by
focused tests and current gates.

encodingBoundary: agent-authored artifacts default to ASCII; the worker must
avoid em-dash characters per the T3-observed encoding violation.

## Planned Artifact Manifest

| Path | Owner | Purpose |
|---|---|---|
| `governance/compat/run_worker_return_scaffold.py` | worker | fix Delta Execution Claim Boundary Control Block default body to a `Field`/`Value` table |
| `governance/compat/test_run_worker_return_scaffold.py` | worker | add a focused regression test for the Delta block table shape |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker | add pre-drafting guidance naming the generic structural sections a review-classified decision artifact needs |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | worker | record the prose-vs-table Delta block trap and the tool/encoding friction as new gotchas |
| `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_WORKER_RETURN_2026-06-26.md` | worker | scaffold-first no-commit return |
| `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_COMPLETION_2026-06-26.md` | Codex reviewer/closer | completion review only if accepted |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: WODS-T3 may modify only the listed
governance helper, focused test, and reference-template files to reduce
dispatch and worker-return authoring loops.

Protected paths:

- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

Operator authorization: the operator requested creating this fresh
source-verified WODS follow-up GC-018/work order before any ASSF-PIC-T4
dispatch, per the value-parked WODS reopen condition that fired in the
ASSF-PIC-T3 completion review.

Rollback boundary: revert only WODS-T3 material and matching session-sync
commits if needed; do not revert WODS-T1, WODS-T2, ASSF-PIC-T2, or
ASSF-PIC-T3 closure history.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Worker-return scaffold emits a valid `Delta Execution Claim Boundary Control Block` `Field`/`Disposition` table with all eight required row labels. | focused scaffold test and direct guard command |
| AC2 | Work-order template guidance names the generic structural sections a `review`-classified decision artifact needs before drafting begins, citing `check_markdown_structural_completeness.py`'s section groups. | template diff and worker return source verification |
| AC3 | Literal-format gotchas records the new prose-vs-table Delta block trap and the operator-reported tool/encoding friction as concrete gotchas. | docs diff |
| AC4 | Worker return measures first/final fast-gate results, repair count, remaining defects, and T1/T2/T3 comparison. | worker-return measurement section |
| AC5 | Worker returns uncommitted artifacts only under `WORKER_MUST_NOT_COMMIT`. | worker return and git status evidence |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| Worker return | `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_WORKER_RETURN_2026-06-26.md` |
| Completion review | `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_COMPLETION_2026-06-26.md` |
| Closure decision | reviewer determines from the worker return |
| Session-sync disposition | required only in a dedicated commit tied to the accepted material closure SHA if current mode or next allowed move changes |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired work order | `Status: CLOSED_PASS_BOUNDED` after reviewer acceptance | PASS |
| Completion or reviewer artifact | completion review path | `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_COMPLETION_2026-06-26.md` | PASS |
| Roadmap state | N/A with reason: WODS-T3 is a follow-up hardening lane, not ASSF-PIC-T4 | N/A with reason | N/A with reason |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized | no registry mutation in planned manifest | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no markdown registry mutation is authorized | no registry mutation in planned manifest | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external evidence artifact import is authorized | N/A with reason | N/A with reason |
| System loop interlock | focused tests and governance gates | reviewer evidence in completion review | PASS |
| Session continuity | N/A with reason: session-sync is separate from the material commit | active session paths excluded from material dispatch commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch; no public-sync
authorization.

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Worker return status | `COMPLETE_PENDING_REVIEW`, reviewed by Codex | PASS |
| Worker commit mode | no worker commit; material closure owned by reviewer | PASS |
| Delta table-shape evidence | focused scaffold regression and direct guard pass | PASS |
| Completion review | reviewer-owned completion review exists | PASS |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this baseline authorizes bounded governance helper
and template hardening; it is not a corpus rescan, external-review
intake-refresh, or comparable source-backed reassessment output.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | WODS-T3 dispatch authorization only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch packet and source verification |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned artifact manifest |
| invocationBoundary | governed local documentation and focused helper/template source work only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit WODS hardening by worker |
| forbiddenExpansion | no ASSF-PIC-T4 dispatch, package instance, certification decision, generated-index mutation, resolver mutation, registry-source mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, session-sync, or worker commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | WODS-T3 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, grep, ADIF resolver import |
| Target paths | this baseline; paired work order |
| Allowed scope source | operator request to create a fresh source-verified WODS follow-up before ASSF-PIC-T4 |
| Before status evidence | dispatchBaseHead `d09ea747`; clean worktree evidence: `git status --short` returned no paths before authoring |
| After status evidence | dispatch artifacts pending gate and commit |
| Diff evidence | `git diff --name-status` before material dispatch commit |
| Approval boundary | dispatch packet only; worker execution follows after material dispatch |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `wods-t3-delta-block-table-shape-and-template-hardening-2026-06-26` |
| Expected manifest | `docs/baselines/CVF_GC018_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_FOR_CLAUDE_2026-06-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_FOR_CLAUDE_2026-06-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

Expected Result: WODS-T3 should reduce the next ASSF-PIC tranche's repeat
fast-gate repair-round count below T3's 3 rounds by fixing the scaffold
default and template guidance defects directly, instead of leaving the
worker to discover them live again.

Evidence Comparison Requirement: worker return must compare first and final
fast-gate results with T1/T2/T3 observed friction and state whether the
change appears improved, unchanged, or blocked by a new defect.

Contradiction Handling Requirement: if focused tests pass but a live
scaffolded worker return still fails on the same Delta-block table shape or
missing structural sections, the worker must mark the improvement claim
revised or blocked.

Claim Update Requirement: reviewer closure must either confirm bounded
improvement, narrow it, or record the next concrete defect.

## Claim Boundary

This baseline authorizes WODS-T3 dispatch only. It does not certify any ASSF
package, release ASSF-PIC-T4, mutate generated indexes or registries,
implement runtime or adapter behavior, run live proof, public-sync, push,
update session continuity, or allow worker commits.
