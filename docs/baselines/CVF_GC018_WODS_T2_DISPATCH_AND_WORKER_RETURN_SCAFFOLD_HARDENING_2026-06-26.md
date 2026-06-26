# CVF GC-018 Baseline: WODS-T2 Dispatch And Worker-Return Scaffold Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-26

docType: baseline

Batch ID: WODS-T2

dispatchBaseHead: c3363887

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex for the returned worker packet.

Canonical packet:
`docs/baselines/CVF_GC018_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_2026-06-26.md`

Paired work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_FOR_CLAUDE_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Current-time notes: ASSF-PIC-T2 closed bounded at material commit `ee5f2c42`
with `CERTIFICATION_HELD_WITH_REASON`. ASSF-PIC-T3 remains held. This
baseline releases only WODS hardening for the T2-discovered dispatch and
worker-return scaffold defects.

Do-not-misread notes: this baseline does not release ASSF-PIC-T3, create a
package instance, certify a package, mutate ASSF generated indexes or
registries, change resolver or Web runtime behavior, implement CLI/MCP adapter
behavior, run provider/live proof, public-sync, push, or session-sync.

## Proposed Tranche

Tranche: WODS-T2 Dispatch And Worker-Return Scaffold Hardening.

Baseline decision: authorize a bounded no-commit Claude worker tranche to fix
the concrete authoring-friction defects observed during ASSF-PIC-T2:

- worker-return scaffold `External Knowledge Intake Routing` table shape does
  not match its own machine guard;
- UAT-review template guidance omitted three sections required by generic
  review gates;
- rescan guard self-reference filtering still misses narrow compound or
  wrapped maintenance phrasing;
- dispatch guidance should say material and session-sync evidence ranges stay
  separate when session-sync is performed after a material commit.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: PENDING_WORKER_RETURN
- Reviewer verdict: PENDING_REVIEW

## Purpose

Reduce repeat work-order and worker-return authoring loops by fixing the source
templates, scaffold defaults, focused tests, and literal-format guidance that
caused Claude to spend multiple fast-gate rounds on familiar report-shape
defects during T2.

This tranche is process/tooling hardening only. It is not an ASSF package
integration task and it does not advance the package certification lane.

## Evidence / Verification

Dispatch evidence is limited to current CVF-governed source surfaces:

- ASSF-PIC-T2 completion review and worker return;
- WODS-T1 completion review;
- worker-return scaffold helper and tests;
- external knowledge intake routing guard;
- markdown structural completeness and epistemic process gates;
- rescan intelligence hardening guard and tests;
- canonical work-order template and literal-format gotchas checklist.

Worker-created implementation diffs and worker-return evidence do not exist at
dispatch time and must not be claimed as complete until the worker returns
uncommitted artifacts and Codex accepts them.

## Scope / Applies To

Applies to:

- worker-return scaffold table shape and focused tests;
- work-order template guidance for review artifacts and no-commit worker
  returns;
- literal-format gotchas guidance for the new report-shape traps;
- focused rescan guard self-reference filtering and tests;
- worker evidence that measures whether this tranche improved authoring
  friction against T1/T2 observations.

Does not apply to:

- ASSF-PIC-T3 dispatch or execution;
- package instance creation, activation, instruction execution, certification,
  generated-index mutation, resolver mutation, registry-source mutation, Web
  runtime mutation, CLI/MCP adapter behavior, provider/live proof, public-sync,
  push, or session-sync.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-PIC-T2 reviewer closure exists and keeps T3 held | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` lines 17-24 and 196-206 |
| T2 closure routes WODS follow-up defects to a separate hardening lane | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` lines 60-69 and 165-167 |
| T2 worker return records the exact scaffold/template/guard defects | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md` lines 311-371 |
| WODS-T1 closed bounded and improved the first two friction sources | SATISFIED | `docs/reviews/CVF_WODS_T1_WORK_ORDER_DISPATCH_SCAFFOLD_OPTIMIZATION_COMPLETION_2026-06-26.md` lines 46-54 and 112-117 |
| Dispatch worktree isolation before WODS-T2 authoring | SATISFIED | `git status --short` returned no paths before authoring |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T2 closure keeps package certification held and routes WODS follow-up | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` | lines 17-24 and 60-69 | `CERTIFICATION_HELD_WITH_REASON` | ASSF-PIC-T2 completion review | VALUE_SET | ACCEPT |
| T2 worker measured WODS-T1 as improved but incomplete | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md` | lines 321-371 | `Worker-Return Scaffold Effectiveness Assessment For The Operator` | ASSF-PIC-T2 worker return | VALUE_SET | ACCEPT |
| Worker-return scaffold currently emits wrong external-intake table columns | `governance/compat/run_worker_return_scaffold.py` | lines 76-82 | `External Knowledge Intake Routing` | worker-return scaffold helper | RUNTIME_BEHAVIOR | ACCEPT |
| External knowledge routing guard requires `Field` and `Value` row-label table content | `governance/compat/check_external_knowledge_intake_routing.py` | lines 27-37 and 269-278 | `REQUIRED_FIELDS` | external knowledge routing guard | LITERAL_INVARIANT | ACCEPT |
| Existing scaffold test checks heading presence but not the table row shape | `governance/compat/test_run_worker_return_scaffold.py` | lines 20-29 | `test_scaffold_text_has_required_headings` | worker-return scaffold tests | EXISTS | ACCEPT |
| Markdown structural completeness requires risk/corrective action for review artifacts | `governance/compat/check_markdown_structural_completeness.py` | lines 217-227 | `review` | markdown structural completeness guard | LITERAL_INVARIANT | ACCEPT |
| Epistemic process gate checks review artifacts for Epistemic Process Block evidence or N/A token | `governance/compat/check_epistemic_process_packet.py` | lines 57 and 235-243 | `Epistemic Process Block` | epistemic process packet guard | LITERAL_INVARIANT | ACCEPT |
| Current rescan guard has explicit maintenance phrase filtering and regex cleanup points | `governance/compat/check_rescan_intelligence_hardening.py` | lines 255-297 | `non_rescan_discussion_phrases` | rescan intelligence hardening guard | RUNTIME_BEHAVIOR | ACCEPT |
| Work-order template already requires scaffold-first worker returns and worker-return fast gate | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 899-917 | `run_worker_return_scaffold.py` | work-order template | LITERAL_INVARIANT | ACCEPT |
| Literal-format gotchas already documents proximity and equivalence trigger traps | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | lines 77-91 | `Proximity-based false-trigger phrases` | governed artifact literal gotchas | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Active session next move | read current front door, bootstrap model, generated state, and active handoff | next allowed move is WODS hardening and ASSF-PIC-T3 remains held | current |
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
| Chain map route | operator request and Claude T2 feedback routed to governed WODS source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this WODS-T2 baseline and paired work order |
| Disposition | dispatch-authoring hardening only; no external artifact import or package certification |
| Claim boundary | Claude feedback is treated as process evidence and re-verified against CVF-governed files before dispatch |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: worker must read current source files, implement bounded
changes, and rerun focused tests/gates instead of relying on chat memory.

unicodePathHandling: literal path or UTF-8 reader required.

extractedTextAuthority: N/A with reason

priorVerificationUse: T2 worker return and completion review are defect-source
evidence only; implementation correctness must be proven by focused tests and
current gates.

encodingBoundary: agent-authored artifacts default to ASCII.

## Planned Artifact Manifest

| Path | Owner | Purpose |
|---|---|---|
| `governance/compat/run_worker_return_scaffold.py` | worker | fix External Knowledge Intake Routing scaffold table shape |
| `governance/compat/test_run_worker_return_scaffold.py` | worker | add focused regression tests for scaffold table shape |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker | add review-section and separate material/session-sync range guidance |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | worker | record newly observed literal-format traps |
| `governance/compat/check_rescan_intelligence_hardening.py` | worker | close narrow self-reference phrase gap if source-verified |
| `governance/compat/test_check_rescan_intelligence_hardening.py` | worker | add focused tests for the rescan maintenance-phrase gap |
| `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_WORKER_RETURN_2026-06-26.md` | worker | scaffold-first no-commit return |
| `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` | Codex reviewer/closer | completion review only if accepted |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: WODS-T2 may modify only the listed
governance helper, guard, focused test, and reference-template files to reduce
dispatch and worker-return authoring loops.

Protected paths:

- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/test_check_rescan_intelligence_hardening.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

Operator authorization: the operator requested continuing WODS hardening and
asked to evaluate whether the hardening is improving after T2.

Rollback boundary: revert only WODS-T2 material and matching session-sync
commits if needed; do not revert ASSF-PIC-T2 closure, WODS-T1 closure, or
unrelated session history.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Worker-return scaffold emits a valid `External Knowledge Intake Routing` `Field`/`Value` table with the seven required row labels. | focused scaffold test and external routing guard |
| AC2 | Work-order template tells future UAT/review artifacts to include `Risk / Corrective Action`, `External Knowledge Intake Routing`, and `Epistemic Process Block` when docs/reviews artifacts are required. | template diff and worker return source verification |
| AC3 | Rescan guard or guidance handles the compound/wrapped maintenance-phrase false trigger observed in T2 while preserving enforcement for real outputs. | focused rescan tests and direct guard command |
| AC4 | Literal-format gotchas records the new scaffold table-shape and self-reference phrase traps. | docs diff |
| AC5 | Worker return measures first/final fast-gate results, repair count, remaining defects, and T1/T2 comparison. | worker-return measurement section |
| AC6 | Worker returns uncommitted artifacts only under `WORKER_MUST_NOT_COMMIT`. | worker return and git status evidence |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| Worker return | `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_WORKER_RETURN_2026-06-26.md` |
| Completion review | `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` |
| Closure decision | reviewer determines from the worker return |
| Session-sync disposition | required only in a dedicated commit tied to the accepted material closure SHA if current mode or next allowed move changes |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired work order | `Status: DISPATCH_READY` at dispatch | PENDING |
| Completion or reviewer artifact | completion review path | created only by reviewer if accepted | PENDING |
| Roadmap state | N/A with reason: WODS-T2 is a follow-up hardening lane, not ASSF-PIC-T3 | N/A with reason | N/A with reason |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized | no registry mutation in planned manifest | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no markdown registry mutation is authorized | no registry mutation in planned manifest | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external evidence artifact import is authorized | N/A with reason | N/A with reason |
| System loop interlock | focused tests and governance gates | worker/reviewer evidence | PENDING |
| Session continuity | N/A with reason: session-sync is separate from the material commit | active session paths excluded from material dispatch commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch; no public-sync authorization.

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md`
- Predecessor intake artifact: `docs/reviews/CVF_WODS_T1_WORK_ORDER_DISPATCH_SCAFFOLD_OPTIMIZATION_COMPLETION_2026-06-26.md`
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS
- Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS
- Semantic sampling status: COMPLETE_WITH_DECLARED_LIMITS
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Finding | Delta category | Disposition |
|---|---|---|
| Worker-return scaffold section coverage improved from T1 to T2 | CHANGED_DISPOSITION | route to WODS-T2 measurement |
| External Knowledge Intake Routing table shape still mismatches the guard | NEW_FINDING | DO_NOW |
| T2 did not remove any prior WODS-T1 finding from evidence | UNCHANGED_FROM_INTAKE | preserve in worker measurement |
| No finding is removed or rejected by this dispatch packet | REMOVED_OR_REJECTED | N/A with reason: reviewer closure will decide after worker evidence |

### Follow-Up Routing Matrix

| Finding | Routing lane | Action |
|---|---|---|
| Scaffold table-shape defect | DO_NOW | fix scaffold helper and focused tests |
| Package lifecycle or adapter work | OUT_OF_SCOPE | keep ASSF-PIC-T3 and package work held |
| Any broader governance redesign | STRATEGIC_OPERATOR_DECISION | return to operator if discovered |
| Resolved WODS-T1 section-heading issue | RESOLVED_BY_DESIGN | preserve tests |
| Runtime or package integration requests | SEPARATE_RUNTIME_TRANCHE | not part of WODS-T2 |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| WODS-T2-RS-01 | T2 worker-return effectiveness assessment | WODS-T1 improved but did not solve authoring friction | source-backed routing | Could this dispatch overclaim a fix before implementation? | bounded dispatch only |
| WODS-T2-RS-02 | current scaffold helper | default external-intake table shape is wrong | source-backed routing | Could the worker fix docs only and leave scaffold broken? | AC1 and AC2 require source/test fix |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | WODS-T2 dispatch authorization only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch packet and source verification |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned artifact manifest |
| invocationBoundary | governed local documentation and focused helper/checker source work only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit WODS hardening by worker |
| forbiddenExpansion | no ASSF-PIC-T3 dispatch, package instance, certification decision, generated-index mutation, resolver mutation, registry-source mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, session-sync, or worker commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | WODS-T2 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, rg, ADIF resolver import, apply_patch |
| Target paths | this baseline; paired work order |
| Allowed scope source | operator request to continue WODS hardening after ASSF-PIC-T2 review |
| Before status evidence | dispatchBaseHead `c3363887`; clean worktree evidence: `git status --short` returned no paths before authoring |
| After status evidence | dispatch artifacts pending gate and commit |
| Diff evidence | `git diff --name-status` before material dispatch commit |
| Approval boundary | dispatch packet only; worker execution follows after material dispatch |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `wods-t2-dispatch-and-worker-return-scaffold-hardening-2026-06-26` |
| Expected manifest | `docs/baselines/CVF_GC018_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_FOR_CLAUDE_2026-06-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_FOR_CLAUDE_2026-06-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

Expected Result: WODS-T2 should reduce future worker-return and review-artifact
format repair loops by fixing scaffold/template defaults instead of asking the
worker to remember hand-written corrections.

Evidence Comparison Requirement: worker return must compare first and final
fast-gate results with T1/T2 observed friction and state whether the change
appears improved, unchanged, or blocked by a new defect.

Contradiction Handling Requirement: if focused tests pass but a live scaffolded
worker return still fails on the same table shape or missing review sections,
the worker must mark the improvement claim revised or blocked.

Claim Update Requirement: reviewer closure must either confirm bounded
improvement, narrow it, or record the next concrete defect.

## Claim Boundary

This baseline authorizes WODS-T2 dispatch only. It does not certify any ASSF
package, release ASSF-PIC-T3, mutate generated indexes or registries, implement
runtime or adapter behavior, run live proof, public-sync, push, update session
continuity, or allow worker commits.
