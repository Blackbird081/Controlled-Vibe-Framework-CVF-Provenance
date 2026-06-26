# CVF Agent Work Order: WODS-T2 Dispatch And Worker-Return Scaffold Hardening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-26

docType: work_order

Batch ID: WODS-T2

dispatchBaseHead: c3363887

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex for returned worker artifacts.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_FOR_CLAUDE_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: ASSF-PIC-T2 is closed bounded with
`CERTIFICATION_HELD_WITH_REASON`; ASSF-PIC-T3 remains held. WODS-T1 improved
the first worker-return friction sources, but T2 exposed remaining scaffold and
template defects. This work order fixes those authoring surfaces only.

Do-not-misread notes: do not dispatch ASSF-PIC-T3, create package roots,
`SKILL.md`, `skill.source.json`, registry entries, generated index changes,
resolver changes, Web runtime changes, CLI/MCP adapter behavior, provider/live
proof, public-sync, push, package activation, lifecycle state mutation,
session-sync, or commits.

Required first actions: read this work order, read the paired GC-018 baseline,
read `CVF_SESSION_MEMORY.md`, read
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read `AGENT_HANDOFF_V22_2026-06-22.md`,
read `docs/reference/guard_orientation/README.md`, read
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
then record actual `executionBaseHead` and `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with uncommitted artifacts
only, actual `executionBaseHead`, actual `git status --short`, changed paths,
source inventory, focused tests/gate evidence, effectiveness measurement, and
no commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact source,
scope, or gate that blocks completion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator request to continue WODS hardening and evaluate improvement after T2 |
| Scope classification | bounded governance-helper/template/report-shape hardening |
| Intake role | worker implements bounded source/docs/test changes and returns no-commit evidence |
| Reviewer role | Codex reviewer/closer validates artifacts, gates, boundaries, and commits accepted material |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker returns uncommitted artifacts |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require ASSF-PIC-T3 movement, package work, registry/generated-index/resolver/Web/runtime/adapter/provider/public/session-sync scope, push, destructive action, or a broader governance redesign |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher creates packet; worker executes WODS-T2 source/docs/test hardening and returns no-commit evidence; reviewer/closer reviews, commits accepted material, and records any dedicated session-sync with material SHA evidence |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=c3363887`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | execution changes only Write Ownership paths; closer owns status conversion, completion review, accepted material commit, and later session-sync |
| traceScope(phase, actor) | worker-return trace covers pending WODS-T2 artifacts only; reviewer trace covers review/closure; session-sync trace covers continuity only |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material, closure, or session-sync commit |
| crossBatchIsolation | do not mix this tranche with ASSF-PIC-T3, package integration, generated-index/resolver/Web/runtime/adapter/provider/public-sync work, or another dispatch batch |
| Before status evidence | dispatchBaseHead `c3363887`; clean worktree evidence: `git status --short` returned no paths before dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only in a dedicated session-sync commit with the accepted material SHA if mode or next allowed move changes |
| Closer designation | Codex reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | this work order; paired GC-018 baseline; worker-return artifact; reviewer completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | Codex reviewer/closer role |

## Purpose

Implement the next WODS hardening tranche for defects observed during
ASSF-PIC-T2. The goal is to remove repeated worker/report authoring traps by
fixing the scaffold and template source that caused them.

Success means future workers should start from scaffold/template output that
already matches the machine gates for external knowledge routing, required
review sections, and common maintenance-phrase wording.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-26 request to issue next tranche and evaluate hardening improvement | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active session bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active session state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_2026-06-26.md` | ACCEPT |
| ASSF-PIC-T2 completion review | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` | ACCEPT |
| ASSF-PIC-T2 worker return | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md` | ACCEPT |
| WODS-T1 completion review | `docs/reviews/CVF_WODS_T1_WORK_ORDER_DISPATCH_SCAFFOLD_OPTIMIZATION_COMPLETION_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | Codex dispatch author role |
| Worker | Claude implementation/test/no-commit return role |
| Reviewer | Codex reviewer role for returned worker artifacts |
| Closer | Codex closer role for accepted worker evidence |
| Session-sync steward | Codex session-sync role in a dedicated continuity commit if next move changes |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `docs/baselines/CVF_GC018_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_2026-06-26.md` | READ | authorization, scope, and claim boundary |
| `CVF_SESSION_MEMORY.md` | READ | active front door and current next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup read model |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | current generated aggregate and active handoff pointer |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff and current session continuity |
| `docs/reference/guard_orientation/README.md` | READ | task-first guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | pre-write checklist for gate-parsed artifacts |
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` | READ | reviewer closure and WODS follow-up routing |
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md` | READ | detailed T2 scaffold/template defect evidence |
| `docs/reviews/CVF_WODS_T1_WORK_ORDER_DISPATCH_SCAFFOLD_OPTIMIZATION_COMPLETION_2026-06-26.md` | READ | prior hardening evidence and boundaries |
| `governance/compat/run_worker_return_scaffold.py` | READ | scaffold source to fix |
| `governance/compat/test_run_worker_return_scaffold.py` | READ | scaffold focused tests |
| `governance/compat/check_external_knowledge_intake_routing.py` | READ | required external-routing table shape |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | READ | template source to harden |
| `governance/compat/check_markdown_structural_completeness.py` | READ | review structural requirements |
| `governance/compat/check_epistemic_process_packet.py` | READ | epistemic review section requirement |
| `governance/compat/check_rescan_intelligence_hardening.py` | READ | maintenance-phrase filtering source |
| `governance/compat/test_check_rescan_intelligence_hardening.py` | READ | rescan focused tests |

## Pre-Flight Checks

The worker must run these before editing. For commands using
`<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Test-Path docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_WORKER_RETURN_2026-06-26.md
```

The expected `Test-Path` result for the worker-return artifact before scaffold
creation is `False`. If it already exists, stop and return
`BLOCKED_WITH_REASON` unless the reviewer explicitly directs reuse.

## Worker Return Packet Shape Contract

The worker-return artifact must be scaffold-first. The scaffold helper supplies
the starting shape, and the completed worker return must retain or complete
the sections listed below so reviewer-fast can diagnose issues before closure:

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

If any section is not applicable, include the section with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

### Worker Return Scaffold-First Requirement

Before writing long report content, create the worker return from the scaffold:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_WORKER_RETURN_2026-06-26.md --title "CVF WODS-T2 Dispatch And Worker-Return Scaffold Hardening Worker Return"
```

Then fill the scaffold completely. Do not leave `TODO` strings in the returned
artifact. The worker return must include:

- `dispatchWorkOrder: ` followed by this work order path in backticks;
- `## Source Inventory` with real paths and bare action tokens;
- `receiptEvidence: CVF_RECEIPT_PRESENT - ...`;
- `Corpus verdict: NOT_APPLICABLE_WITH_REASON - ...`;
- `Defect class:` with a valid value used by the finding-to-governance guard;
- `Actual changed set` listing real changed paths, not shorthand prose;
- `Core Guard Self-Protection Authorization` naming every protected changed
  path from this work order;
- worker-return scaffold measurement fields.

Important: because this tranche edits `governance/compat/` and
`docs/reference/` protected surfaces, the worker-return file itself must
contain the `Core Guard Self-Protection Authorization` block. Do not rely on
this work order or handoff as the only authorization block in the worker range.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check, source-inventory,
packet-shape, focused-command, and worker-return fast-gate failures and rerun
the required checks without asking the operator. Ask the operator only if
remediation would exceed Allowed scope, change the claim boundary, require
ASSF-PIC-T3 movement, package work, registry/generated-index/resolver/Web/
runtime/adapter/provider/public/session-sync scope, push, destructive action,
or another roadmap batch.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_worker_return_scaffold.py` | worker | fix scaffold table shape |
| `governance/compat/test_run_worker_return_scaffold.py` | worker | focused scaffold-shape regression tests |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker | add review-section and separated-range guidance |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | worker | record T2-discovered literal-format traps |
| `governance/compat/check_rescan_intelligence_hardening.py` | worker | focused maintenance-phrase filtering if source-verified |
| `governance/compat/test_check_rescan_intelligence_hardening.py` | worker | focused tests for maintenance-phrase gap |
| `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_WORKER_RETURN_2026-06-26.md` | worker | create scaffold-first no-commit worker return |
| `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` | Codex reviewer/closer | create only when Codex accepts the worker return |
| this work order | Codex reviewer/closer | status conversion only when Codex accepts the worker return |
| paired GC-018 baseline | Codex reviewer/closer | status conversion only when Codex accepts the worker return |
| session-sync surfaces | Codex session-sync steward | update only in a dedicated continuity commit with material SHA evidence |

Worker may create or modify only these execution paths:

- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/test_check_rescan_intelligence_hardening.py`
- `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_WORKER_RETURN_2026-06-26.md`

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
advance `uatState`, advance `certificationState`, dispatch ASSF-PIC-T3, or
claim final certification.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance files changed by worker | existing helper, guard, focused test, and reference-template files listed in Write Ownership |
| New generated aggregate | N/A with reason: no generated aggregate mutation is authorized |
| New source layout | N/A with reason: no new generated source layout, package root, registry source family, resolver source, Web source, or adapter source is authorized |
| Index or registry mutation | N/A with reason: ASSF generated index, registry entries, and resolver source remain out of scope |
| Storage owner | governance helper/checker/test/reference files plus one worker-return review |
| Closure disposition required | reviewer verifies changed paths exactly match Write Ownership before material commit |

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

## Implementation Requirements

| ID | Requirement |
|---|---|
| R1 | Change `run_worker_return_scaffold.py` so `## External Knowledge Intake Routing` emits a valid `Field`/`Value` table with rows for `Chain map`, `Input type`, `Chain map route`, `Matching local-view guard`, `Owner surface`, `Disposition`, and `Claim boundary`. |
| R2 | Add focused tests in `test_run_worker_return_scaffold.py` that fail on the old 5-column table and pass on the required row-label shape. |
| R3 | Update `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` so no-commit work orders that require a `docs/reviews/` review artifact name `Risk / Corrective Action`, `External Knowledge Intake Routing`, and `Epistemic Process Block` in the review artifact shape or explicitly require N/A sections. |
| R4 | Update the same template to say material gate ranges and later session-sync gate ranges should be recorded separately when session-sync is separate from material closure. |
| R5 | Harden `check_rescan_intelligence_hardening.py` only as needed to exclude self-referential maintenance phrases observed in T2 while preserving failure for real rescan/intake outputs that misuse compact N/A. |
| R6 | Add focused rescan tests covering the T2 maintenance-phrase false trigger and preserving enforcement for real outputs. |
| R7 | Add the new table-shape and maintenance-phrase traps to the literal-format gotchas checklist. |
| R8 | Worker return must measure whether this tranche is likely improving authoring friction using first/final fast-gate results, repair count, and residual defects. |

## Effectiveness Measurement Requirement

The worker return must include a short, evidence-backed assessment with these
fields:

| Measurement | Required value source |
|---|---|
| WODS-T1 carried-forward fixes | cite WODS-T1 completion and T2 worker-return comparison |
| T2 defects targeted | list the scaffold table shape, missing UAT-review sections, maintenance-phrase false trigger, and mixed-range wording |
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
2. Inspect current scaffold, guards, tests, template, and gotchas files.
3. Patch the scaffold table shape and focused scaffold tests.
4. Patch work-order template guidance for review sections and separated
   material/session-sync range wording.
5. Patch the rescan guard and tests only for the source-verified
   self-reference false trigger.
6. Update literal-format gotchas for the two newly observed traps.
7. Create the worker return from the scaffold before long prose.
8. Run focused tests and required return commands; repair allowed-scope packet
   defects and rerun.
9. Return `COMPLETE_PENDING_REVIEW` with no commit when all allowed-scope
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
- direct external routing guard and rescan guard results when relevant;
- `git diff --check`;
- `git diff --name-status`;
- explicit no-commit statement;
- explicit statement that no ASSF-PIC-T3 dispatch, package instance,
  lifecycle mutation, generated-index mutation, resolver mutation, Web runtime,
  CLI/MCP adapter, provider/live proof, public-sync, push, activation,
  session-sync, or final certification occurred.

## Required Commands Before Return

Run and record results:

```powershell
git status --short
python -m pytest governance/compat/test_run_worker_return_scaffold.py governance/compat/test_check_rescan_intelligence_hardening.py
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_rescan_intelligence_hardening.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
```

If `run_worker_return_fast_gate.py` fails because the worker-return artifact is
still malformed, repair the artifact and rerun it. If it fails because of an
out-of-scope pre-existing violation, record the exact failing command and
return `BLOCKED_WITH_REASON`.

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
| Worker-return scaffold | read current source | `run_worker_return_scaffold.py` lines 76-82 show old 5-column external-intake table | stale shape found |
| External routing guard | read current source | `check_external_knowledge_intake_routing.py` lines 27-37 require seven row labels | current |
| WODS follow-up source | read T2 completion and worker return | T2 routes the defects to WODS hardening | current |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This work order cites bounded files and exact planned artifacts
  only; worker must list real changed paths.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Scope exclusions are boundaries, not evidence claims.
- ADIF-0006: Verified path or symbol cells contain only paths, fields,
  functions, sections, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request and Claude T2 feedback routed to governed WODS source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this WODS-T2 work order and paired GC-018 baseline |
| Disposition | local dispatch/scaffold hardening only; no external material absorbed |
| Claim boundary | source facts must cite CVF-governed files and command evidence |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or checkpoint requirement | Work-order coverage | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| ASSF-PIC-T3 remains held after T2 certification hold | Forbidden Changed Paths And Actions | no T3/package path in Write Ownership | reviewer closure | READY |
| T2 process defects move to WODS hardening | Implementation Requirements | scaffold/template/guard/gotchas updates | focused tests and worker return | READY |
| Work-order dispatch hardening must be evidence-backed | Effectiveness Measurement Requirement | worker return measurement rows | reviewer closure | READY |
| Session-sync must stay separate from material work | Agent Handoff Contract Control Block | no session paths in worker Write Ownership | git diff name-status | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | WODS-T2 scaffold/template/checker hardening | internal agents may use the hardened scaffold and template after reviewer acceptance; no package lifecycle, resolver, Web, registry, provider, or adapter behavior is granted | this work order, paired baseline, focused tests, worker return | no internal loader, resolver, generator, Web bridge, package root, or adapter is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external agent package surface | external agents cannot use this tranche as package or adapter evidence | Dual Agent Surface Accounting Standard and explicit forbidden scope | adapter implementation is out of scope | `DEFERRED_WITH_REASON` |

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
| No finding is removed or rejected by this dispatch packet | REMOVED_OR_REJECTED | N/A with reason: reviewer closure will decide from worker evidence |

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

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker-return scaffold emits a valid `External Knowledge Intake Routing` `Field`/`Value` table with the seven guard-required row labels. |
| AC2 | Focused scaffold tests fail on the old 5-column table shape and pass on the fixed shape. |
| AC3 | Work-order template guidance names the three review sections missed in T2 when a work order asks for a `docs/reviews/` review artifact. |
| AC4 | Work-order template guidance instructs separate material and session-sync ranges when session-sync is separate from material closure. |
| AC5 | Rescan guard/test changes cover the T2 maintenance-phrase false trigger and preserve enforcement for real outputs. |
| AC6 | Literal-format gotchas records the newly observed table-shape and maintenance-phrase traps. |
| AC7 | Worker return includes effectiveness measurement and no-commit evidence. |

## Review Gate

Codex reviewer/closer must verify the worker return against Write Ownership,
review source/test/docs diffs for bounded behavior, run focused tests and
applicable gates, confirm no ASSF-PIC-T3/package/session-sync mutation
occurred, and only then convert accepted material into a completion review and
material commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when implementation, tests, worker return,
and required commands are present, worker-return fast gate passes, and changed
files remain inside Write Ownership.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, or the repair would require forbidden package,
runtime, provider, public, session-sync, lifecycle, adapter, or broader
governance scope.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would
require ASSF-PIC-T3 movement, package instance creation, lifecycle state
advancement, generated-index mutation, resolver mutation, Web runtime, CLI/MCP
adapter behavior, provider/live proof, public-sync, push, package activation,
secrets/quota, destructive action, or a change to the claim boundary.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_FOR_CLAUDE_2026-06-26.md` | `Status: DISPATCH_READY` at dispatch | PENDING |
| Completion or reviewer artifact | `docs/reviews/CVF_WODS_T2_DISPATCH_AND_WORKER_RETURN_SCAFFOLD_HARDENING_COMPLETION_2026-06-26.md` | reviewer-owned for accepted worker return | PENDING |
| Roadmap state | N/A with reason: WODS-T2 is not ASSF-PIC-T3 | T3 remains held | N/A with reason |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized by WODS-T2 | worker must not change registry JSON | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized by WODS-T2 | worker must not change registry Markdown | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external evidence artifact is created by this local hardening tranche | no external artifact hash applies | N/A with reason |
| System loop interlock | worker return and reviewer completion | no package activation, runtime loop, provider call, public-sync, or worker commit occurs | PENDING |
| Session continuity | N/A with reason: session-sync is separate from material closure | active session paths excluded from worker changed set | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | WODS-T2 scaffold/template/checker hardening dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch authorization only |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned artifact manifest |
| invocationBoundary | governed local documentation and focused source/test work only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit WODS hardening by worker |
| forbiddenExpansion | no ASSF-PIC-T3 dispatch, package instance, lifecycle mutation, generated-index mutation, resolver mutation, registry-source mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, session-sync, or worker commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | WODS-T2 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, rg, ADIF resolver import, apply_patch |
| Target paths | this work order; paired baseline |
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

## Closure Checklist

| Check | Required resolution |
|---|---|
| Worker status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Changed paths | stay inside Write Ownership |
| Scaffold table shape | focused tests and external routing guard pass |
| Work-order template guidance | review-section and separated-range guidance updated or blocker recorded |
| Rescan maintenance-phrase handling | focused tests and direct guard command pass or blocker recorded |
| Worker return | created through `run_worker_return_scaffold.py --write` |
| Required commands | recorded with PASS or blocking reason |
| Worker boundary | no commit, push, public-sync, provider/live proof, registry mutation, generated-index mutation, resolver mutation, Web mutation, adapter mutation, active session state mutation, lifecycle mutation, package certification, or ASSF-PIC-T3 movement |

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

This work order authorizes WODS-T2 only. It does not release ASSF-PIC-T3,
certify any package, mutate generated indexes or registries, implement runtime
or adapter behavior, run live proof, public-sync, push, update session
continuity, or allow worker commits.
