# CVF Agent Work Order: WODS-T3 Delta Block Table Shape And Template Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-26

docType: work_order

Batch ID: WODS-T3

dispatchBaseHead: `d09ea747`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex for returned worker artifacts.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_FOR_CLAUDE_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: ASSF-PIC-T3 is closed bounded with
`INTEGRATION_DEFERRED_CERTIFICATION_HELD`; ASSF-PIC-T4 is
`HOLD_WODS_REOPEN_AFTER_PIC_T3`. WODS-T2 fixed two T2-found scaffold and
guard defects from the prior cycle, but T3 exposed a new prose-vs-table
scaffold gap and a template pre-drafting guidance gap. This work order fixes
those authoring surfaces only.

Do-not-misread notes: do not dispatch ASSF-PIC-T4, create package roots,
`SKILL.md`, `skill.source.json`, registry entries, generated index changes,
resolver changes, Web runtime changes, CLI/MCP adapter behavior,
provider/live proof, public-sync, push, package activation, lifecycle state
mutation, session-sync, or commits.

Required first actions: read this work order, read the paired GC-018
baseline, read `CVF_SESSION_MEMORY.md`, read
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read
`AGENT_HANDOFF_V22_2026-06-22.md`, read
`docs/reference/guard_orientation/README.md`, read
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
then record actual `executionBaseHead` and `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with uncommitted artifacts
only, actual `executionBaseHead`, actual `git status --short`, changed
paths, source inventory, focused tests/gate evidence, effectiveness
measurement, and no commit. If blocked, return `BLOCKED_WITH_REASON` and name
the exact source, scope, or gate that blocks completion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator request to create a fresh source-verified WODS follow-up before ASSF-PIC-T4 |
| Scope classification | bounded governance-helper/template/report-shape hardening |
| Intake role | worker implements bounded source/docs/test changes and returns no-commit evidence |
| Reviewer role | Codex reviewer/closer validates artifacts, gates, boundaries, and commits accepted material |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker returns uncommitted artifacts |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require ASSF-PIC-T4 movement, package work, registry/generated-index/resolver/Web/runtime/adapter/provider/public/session-sync scope, push, destructive action, or a broader governance redesign |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher creates packet; worker executes WODS-T3 source/docs/test hardening and returns no-commit evidence; reviewer/closer reviews, commits accepted material, and records any dedicated session-sync with material SHA evidence |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=d09ea747`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | execution changes only Write Ownership paths; closer owns status conversion, completion review, accepted material commit, and later session-sync |
| traceScope(phase, actor) | worker-return trace covers pending WODS-T3 artifacts only; reviewer trace covers review/closure; session-sync trace covers continuity only |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material, closure, or session-sync commit |
| crossBatchIsolation | do not mix this tranche with ASSF-PIC-T4, package integration, generated-index/resolver/Web/runtime/adapter/provider/public-sync work, or another dispatch batch |
| Before status evidence | dispatchBaseHead `d09ea747`; clean worktree evidence: `git status --short` returned no paths before dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only in a dedicated session-sync commit with the accepted material SHA if mode or next allowed move changes |
| Closer designation | Codex reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | this work order; paired GC-018 baseline; worker-return artifact; reviewer completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | Codex reviewer/closer role |

## Purpose

Implement the next WODS hardening tranche for defects observed during
ASSF-PIC-T3. The goal is to remove repeated worker/report authoring traps by
fixing the scaffold default and template guidance source that caused them.

Success means a future decision-review worker should start from scaffold
output that already passes the Delta Execution Claim Boundary table-shape
gate, and from template guidance that names the generic structural sections
a review-classified artifact needs before drafting begins.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-26 request to create a fresh WODS follow-up before ASSF-PIC-T4 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active session bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active session state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_2026-06-26.md` | ACCEPT |
| ASSF-PIC-T3 completion review | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` | ACCEPT |
| ASSF-PIC-T3 worker return | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_WORKER_RETURN_2026-06-26.md` | ACCEPT |
| WODS-T2 completion review | `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | Claude dispatch author role (operator-authorized one-off for this tranche) |
| Worker | Claude implementation/test/no-commit return role |
| Reviewer | Codex reviewer role for returned worker artifacts |
| Closer | Codex closer role for accepted worker evidence |
| Session-sync steward | Codex session-sync role in a dedicated continuity commit if next move changes |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `docs/baselines/CVF_GC018_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_2026-06-26.md` | READ | authorization, scope, and claim boundary |
| `CVF_SESSION_MEMORY.md` | READ | active front door and current next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup read model |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | PARTIAL_READ | current generated aggregate and active handoff pointer |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff and current session continuity |
| `docs/reference/guard_orientation/README.md` | PARTIAL_READ | task-first guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | pre-write checklist for gate-parsed artifacts |
| `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` | FULL_READ | reviewer closure and WODS follow-up routing |
| `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_WORKER_RETURN_2026-06-26.md` | READ | detailed T3 scaffold/template defect evidence |
| `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` | READ | prior hardening evidence and boundaries |
| `governance/compat/run_worker_return_scaffold.py` | FULL_READ | scaffold source to fix |
| `governance/compat/test_run_worker_return_scaffold.py` | FULL_READ | scaffold focused tests |
| `governance/compat/check_delta_execution_claim_boundary.py` | FULL_READ | required Delta block table shape |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | PARTIAL_READ | template source to harden |
| `governance/compat/check_markdown_structural_completeness.py` | FULL_READ | review structural requirements |
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | FULL_READ | canonical ASCII and punctuation discipline |

## Pre-Flight Checks

The worker must run these before editing. For commands using
`<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Test-Path docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_WORKER_RETURN_2026-06-26.md
```

The expected `Test-Path` result for the worker-return artifact before
scaffold creation is `False`. If it already exists, stop and return
`BLOCKED_WITH_REASON` unless the reviewer explicitly directs reuse.

## Worker Return Packet Shape Contract

The worker-return artifact must be scaffold-first. The scaffold helper
supplies the starting shape, and the completed worker return must retain or
complete the sections listed below so reviewer-fast can diagnose issues
before closure:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Worker Return Scaffold Effectiveness Measurement`
- `Machine Closure Package`
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- command evidence
- no commit statement

If any section is not applicable, include the section with `N/A with
reason` or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of
omitting it.

### Worker Return Scaffold-First Requirement

Before writing long report content, create the worker return from the
scaffold:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_WORKER_RETURN_2026-06-26.md --title "CVF WODS-T3 Delta Block Table Shape And Template Hardening Worker Return"
```

Then fill the scaffold completely. Do not leave `TODO` strings in the
returned artifact. The worker return must include:

- `dispatchWorkOrder: ` followed by this work order path in backticks;
- `## Source Inventory` with real paths and bare action tokens;
- `receiptEvidence: CVF_RECEIPT_PRESENT - ...`;
- `Corpus verdict: NOT_APPLICABLE_WITH_REASON - ...`;
- `Defect class:` with a valid value used by the finding-to-governance
  guard;
- `Actual changed set` listing real changed paths, not shorthand prose;
- `Core Guard Self-Protection Authorization` naming every protected changed
  path from this work order;
- worker-return scaffold measurement fields.

Important: because this tranche edits `governance/compat/` and
`docs/reference/` protected surfaces, the worker-return file itself must
contain the `Core Guard Self-Protection Authorization` block. Do not rely on
this work order or handoff as the only authorization block in the worker
range.

Important (ASCII discipline): the ASSF-PIC-T3 operator report named an
ASCII em-dash violation as one of the six authoring troubles. Do not use an
em-dash character anywhere in the worker-return artifact or in any edited
source/docs file; use ` - ` instead, per the existing em-dash rule already
in `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check,
source-inventory, packet-shape, focused-command, and worker-return fast-gate
failures and rerun the required checks without asking the operator. Ask the
operator only if remediation would exceed Allowed scope, change the claim
boundary, require ASSF-PIC-T4 movement, package work,
registry/generated-index/resolver/Web/runtime/adapter/provider/public/
session-sync scope, push, destructive action, or another roadmap batch.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_worker_return_scaffold.py` | worker | fix Delta Execution Claim Boundary Control Block default table shape |
| `governance/compat/test_run_worker_return_scaffold.py` | worker | focused Delta-block-shape regression test |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker | add pre-drafting structural-section guidance for review-classified artifacts |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | worker | record T3-discovered literal-format and tool/encoding traps |
| `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_WORKER_RETURN_2026-06-26.md` | worker | create scaffold-first no-commit worker return |
| `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_COMPLETION_2026-06-26.md` | Codex reviewer/closer | create only when Codex accepts the worker return |
| this work order | Codex reviewer/closer | status conversion only when Codex accepts the worker return |
| paired GC-018 baseline | Codex reviewer/closer | status conversion only when Codex accepts the worker return |
| session-sync surfaces | Codex session-sync steward | update only in a dedicated continuity commit with material SHA evidence |

Worker may create or modify only these execution paths:

- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_WORKER_RETURN_2026-06-26.md`

## Forbidden Changed Paths And Actions

The worker must not change:

- `CVF_SESSION/**`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `CVF_SESSION_MEMORY.md`
- `docs/reference/agent_system_skills/registry/entries/*.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `governance/compat/run_assf_skill_resolver.py`
- `governance/compat/generate_assf_skill_index.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**`
- public-sync clone files or remotes.

The worker must not commit, push, run live/provider proof, create package
roots, create `SKILL.md`, create `skill.source.json`, activate a package,
advance `uatState`, advance `certificationState`, dispatch ASSF-PIC-T4, or
claim final certification.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance files changed by worker | existing helper, focused test, and reference-template files listed in Write Ownership |
| New generated aggregate | N/A with reason: no generated aggregate mutation is authorized |
| New source layout | N/A with reason: no new generated source layout, package root, registry source family, resolver source, Web source, or adapter source is authorized |
| Index or registry mutation | N/A with reason: ASSF generated index, registry entries, and resolver source remain out of scope |
| Storage owner | governance helper/test/reference files plus one worker-return review |
| Closure disposition required | reviewer verifies changed paths exactly match Write Ownership before material commit |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: WODS-T3 may modify only the listed
governance helper, focused test, and reference-template files to reduce
dispatch and worker-return authoring loops.

Protected paths:

- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

Operator authorization: the operator requested creating a fresh
source-verified WODS follow-up before ASSF-PIC-T4 dispatch, per the
value-parked WODS reopen condition that fired in the ASSF-PIC-T3 completion
review.

Rollback boundary: revert only WODS-T3 material and matching session-sync
commits if needed; do not revert WODS-T1, WODS-T2, ASSF-PIC-T2, or
ASSF-PIC-T3 closure history.

## Implementation Requirements

| ID | Requirement |
|---|---|
| R1 | Change `run_worker_return_scaffold.py` so `## Delta Execution Claim Boundary Control Block` emits a valid `Field`/`Disposition` table with rows for `claimScope`, `claimDisposition`, `receiptEvidence`, `actionEvidence`, `invocationBoundary`, `interceptionBoundary`, `claimLanguage`, and `forbiddenExpansion`. |
| R2 | Add a focused test in `test_run_worker_return_scaffold.py` that fails on the old prose-only body and passes on the required table-row shape. |
| R3 | Update `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` so it names, near the no-commit worker-return guidance, the generic structural sections `check_markdown_structural_completeness.py` expects for a `review`-classified decision artifact (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition), so a future dispatcher writes them into the work order's own Required Shape section up front. |
| R4 | Add the prose-vs-table Delta block trap and the operator-reported `write_to_file` long-content/backtick parsing friction (plus the ASCII em-dash violation) to the literal-format gotchas checklist as concrete, numbered items. |
| R5 | Worker return must measure whether this tranche is likely improving authoring friction using first/final fast-gate results, repair count, and residual defects, compared explicitly against T1, T2, and T3 observations. |

## Effectiveness Measurement Requirement

The worker return must include a short, evidence-backed assessment with
these fields:

| Measurement | Required value source |
|---|---|
| WODS-T1/T2 carried-forward fixes | cite WODS-T2 completion and T3 worker-return/completion-review comparison |
| T3 defects targeted | list the Delta-block prose-vs-table gap, missing pre-drafting structural-section guidance, and the operator-reported tool/encoding friction |
| First worker-return fast-gate result | command result before manual repair, or reason if blocked |
| Final worker-return fast-gate result | final command result |
| Manual repair count | number of gate-driven repair rounds after initial scaffold fill |
| Remaining authoring defects | NONE or concrete follow-up item |
| Improvement verdict | one of `CLEARLY_IMPROVED`, `IMPROVED_BUT_NOT_SOLVED`, `NO_CLEAR_IMPROVEMENT`, `BLOCKED_WITH_REASON` |

Do not claim "solved" unless the scaffold output and template guidance pass
their focused tests and the worker-return fast gate completes without a new
same-class scaffold/template defect.

## Execution Plan

1. Complete all Required First Reads and Pre-Flight Checks.
2. Inspect the current scaffold, template, and gotchas files.
3. Patch the scaffold's Delta block table shape and add the focused
   regression test.
4. Patch the work-order template's pre-drafting structural-section
   guidance.
5. Update literal-format gotchas for the three newly observed traps.
6. Create the worker return from the scaffold before long prose.
7. Run focused tests and required return commands; repair allowed-scope
   packet defects and rerun.
8. Return `COMPLETE_PENDING_REVIEW` with no commit when all allowed-scope
   checks pass, or `BLOCKED_WITH_REASON` with exact blocker evidence.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- exact changed paths;
- source inventory for every file read or changed;
- scaffold command and scaffold-created result;
- first and final `run_worker_return_fast_gate.py` results;
- manual format repairs after first fast gate, or `NONE`;
- focused test commands and results;
- direct Delta execution claim boundary guard result when relevant;
- `git diff --check`;
- `git diff --name-status`;
- explicit no-commit statement;
- explicit statement that no ASSF-PIC-T4 dispatch, package instance,
  lifecycle mutation, generated-index mutation, resolver mutation, Web
  runtime, CLI/MCP adapter, provider/live proof, public-sync, push,
  activation, session-sync, or final certification occurred.

## Required Commands Before Return

Run and record results:

```powershell
git status --short
python -m pytest governance/compat/test_run_worker_return_scaffold.py
python governance/compat/check_delta_execution_claim_boundary.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
```

If `run_worker_return_fast_gate.py` fails because the worker-return artifact
is still malformed, repair the artifact and rerun it. If it fails because of
an out-of-scope pre-existing violation, record the exact failing command and
return `BLOCKED_WITH_REASON`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T3 closure routes 4 residual defects to WODS follow-up and holds T4 | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` | lines 164-171 | `REOPEN_CONDITION_FIRED` | ASSF-PIC-T3 completion review | VALUE_SET | ACCEPT |
| Scaffold's Delta Execution Claim Boundary Control Block default body is prose, not a table | `governance/compat/run_worker_return_scaffold.py` | lines 154-161 | `Delta Execution Claim Boundary Control Block` | worker-return scaffold helper | RUNTIME_BEHAVIOR | ACCEPT |
| Delta execution claim boundary guard parses only markdown table rows for required fields | `governance/compat/check_delta_execution_claim_boundary.py` | lines 218-228 and 248-265 | `_field_rows` | Delta execution claim boundary guard | RUNTIME_BEHAVIOR | ACCEPT |
| Markdown structural completeness requires risk/corrective action and other generic sections for review-classified artifacts | `governance/compat/check_markdown_structural_completeness.py` | lines 142 and 217-223 | `SECTION_GROUPS` | markdown structural completeness guard | LITERAL_INVARIANT | ACCEPT |
| Agent-authored governed artifacts default to ASCII; em dashes use a hyphen or colon instead | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | lines 33-42 | `## Rule` | text encoding and symbol discipline standard | LITERAL_INVARIANT | ACCEPT |
| Literal-format gotchas checklist currently ends at item 22 | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | lines 201-226 | item 22 | governed artifact literal gotchas | EXISTS | ACCEPT |
| Work-order template's no-commit worker-return guidance is the prior WODS-T2 edit point | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 899-960 | no-commit worker-return guidance | work-order template | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Worker-return scaffold | read current source | `run_worker_return_scaffold.py` lines 154-161 show prose-only Delta block body | stale shape found |
| Delta execution claim boundary guard | read current source | `check_delta_execution_claim_boundary.py` lines 218-228 require table rows | current |
| WODS follow-up source | read T3 completion and worker return | T3 routes the defects to WODS hardening before T4 | current |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This work order cites bounded files and exact planned
  artifacts only; worker must list real changed paths.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Scope exclusions are boundaries, not evidence claims.
- ADIF-0006: Verified path or symbol cells contain only paths, fields,
  functions, sections, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request and the T3 completion review's operator-reported friction routed to governed WODS source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this WODS-T3 work order and paired GC-018 baseline |
| Disposition | local dispatch/scaffold hardening only; no external material absorbed |
| Claim boundary | source facts must cite CVF-governed files and command evidence |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or checkpoint requirement | Work-order coverage | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| ASSF-PIC-T4 remains held after T3 WODS reopen | Forbidden Changed Paths And Actions | no T4/package path in Write Ownership | reviewer closure | READY |
| T3 process defects move to WODS hardening | Implementation Requirements | scaffold/template/gotchas updates | focused tests and worker return | READY |
| Work-order dispatch hardening must be evidence-backed | Effectiveness Measurement Requirement | worker return measurement rows | reviewer closure | READY |
| Session-sync must stay separate from material work | Agent Handoff Contract Control Block | no session paths in worker Write Ownership | git diff name-status | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | WODS-T3 scaffold/template hardening | internal agents may use the hardened scaffold and template after reviewer acceptance; no package lifecycle, resolver, Web, registry, provider, or adapter behavior is granted | this work order, paired baseline, focused tests, worker return | no internal loader, resolver, generator, Web bridge, package root, or adapter is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external agent package surface | external agents cannot use this tranche as package or adapter evidence | Dual Agent Surface Accounting Standard and explicit forbidden scope | adapter implementation is out of scope | `DEFERRED_WITH_REASON` |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this work order authorizes bounded governance
helper and template hardening; it is not a rescan, intake-refresh, or
source-backed reassessment output.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker-return scaffold emits a valid `Delta Execution Claim Boundary Control Block` `Field`/`Disposition` table with all eight required row labels. |
| AC2 | Focused scaffold test fails on the old prose-only body and passes on the fixed table shape. |
| AC3 | Work-order template guidance names the generic structural sections a review-classified decision artifact needs near the no-commit worker-return guidance. |
| AC4 | Literal-format gotchas records the newly observed prose-vs-table Delta block trap and the operator-reported tool/encoding friction. |
| AC5 | Worker return includes effectiveness measurement and no-commit evidence. |

## Review Gate

Codex reviewer/closer must verify the worker return against Write
Ownership, review source/test/docs diffs for bounded behavior, run focused
tests and applicable gates, confirm no ASSF-PIC-T4/package/session-sync
mutation occurred, and only then convert accepted material into a
completion review and material commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when implementation, tests, worker return,
and required commands are present, worker-return fast gate passes, and
changed files remain inside Write Ownership.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required
gate cannot pass inside Allowed scope, or the repair would require
forbidden package, runtime, provider, public, session-sync, lifecycle,
adapter, or broader governance scope.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation
inside this work order. Operator checkpoint is required only if execution
would require ASSF-PIC-T4 movement, package instance creation, lifecycle
state advancement, generated-index mutation, resolver mutation, Web
runtime, CLI/MCP adapter behavior, provider/live proof, public-sync, push,
package activation, secrets/quota, destructive action, or a change to the
claim boundary.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_FOR_CLAUDE_2026-06-26.md` | `Status: DISPATCH_READY` at dispatch | PENDING |
| Completion or reviewer artifact | `docs/reviews/CVF_WODS_T3_DELTA_BLOCK_TABLE_SHAPE_AND_TEMPLATE_HARDENING_COMPLETION_2026-06-26.md` | reviewer-owned for accepted worker return | PENDING |
| Roadmap state | N/A with reason: WODS-T3 is not ASSF-PIC-T4 | T4 remains held | N/A with reason |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized by WODS-T3 | worker must not change registry JSON | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized by WODS-T3 | worker must not change registry Markdown | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external evidence artifact is created by this local hardening tranche | no external artifact hash applies | N/A with reason |
| System loop interlock | worker return and reviewer completion | no package activation, runtime loop, provider call, public-sync, or worker commit occurs | PENDING |
| Session continuity | N/A with reason: session-sync is separate from material closure | active session paths excluded from worker changed set | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch; no public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | WODS-T3 scaffold/template hardening dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch authorization only |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned artifact manifest |
| invocationBoundary | governed local documentation and focused source/test work only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit WODS hardening by worker |
| forbiddenExpansion | no ASSF-PIC-T4 dispatch, package instance, lifecycle mutation, generated-index mutation, resolver mutation, registry-source mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, session-sync, or worker commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | WODS-T3 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, grep, ADIF resolver import |
| Target paths | this work order; paired baseline |
| Allowed scope source | operator request to create a fresh WODS follow-up before ASSF-PIC-T4 |
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

## Closure Checklist

| Check | Required resolution |
|---|---|
| Worker status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Changed paths | stay inside Write Ownership |
| Delta block table shape | focused test and direct guard command pass |
| Work-order template guidance | pre-drafting structural-section guidance updated or blocker recorded |
| Worker return | created through `run_worker_return_scaffold.py --write` |
| Required commands | recorded with PASS or blocking reason |
| Worker boundary | no commit, push, public-sync, provider/live proof, registry mutation, generated-index mutation, resolver mutation, Web mutation, adapter mutation, active session state mutation, lifecycle mutation, package certification, or ASSF-PIC-T4 movement |

## Epistemic Process Block

Expected Result: WODS-T3 should reduce the next ASSF-PIC tranche's repeat
fast-gate repair-round count below T3's 3 rounds by fixing the scaffold
default and template guidance defects directly.

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

This work order authorizes WODS-T3 only. It does not release ASSF-PIC-T4,
certify any package, mutate generated indexes or registries, implement
runtime or adapter behavior, run live proof, public-sync, push, update
session continuity, or allow worker commits.
