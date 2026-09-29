# CVF Agent Work Order - MSEA-R70A Workspace Overlay Standards Catalog Profile Definitions

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS

Dispatch base head: b65ad7c76

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_WORKER_RETURN_2026-07-07.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_2026-07-07.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-07; PR #20 is closed and unmerged
at dispatch authoring time, but GitHub metadata and file contents may drift and
must be refreshed read-only at execution time.

Do-not-misread notes: this work order authorizes proposed definitions only; it
does not authorize overlay engine scripts, wrapper integration, installer
changes, merge, push, public-sync mutation, provider/live proof, runtime/source
edits, tests, checker edits, or public-release claims.

Required first actions: read required startup files, guard orientation,
literal gotchas, this packet, the paired GC-018 baseline, the critical
repository boundary, R70 accepted worker return, R71 reference storage standard
and index, and all checker source listed in the Checker Source Read-Ahead Block
before writing any artifact.

Return contract: create worker-owned definition artifacts and the worker
return, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute a bounded no-commit R70A definition tranche. The worker must author
fresh CVF-owned proposed workspace overlay definitions from source-verified PR
#20 candidate material: one reference standard, one catalog JSON, eleven profile
JSON files, one R71 reference artifact index update, and one worker return.

## Scope / Target / Owner Boundary

Allowed worker-owned outputs in this provenance workspace:

- `docs/reference/CVF_WORKSPACE_OVERLAY_PIPELINE_STANDARD_2026-07-07.md`
- `workspace_overlay_catalog.json`
- `workspace_overlay_profiles/premium-authoring.json`
- `workspace_overlay_profiles/premium-boundary.json`
- `workspace_overlay_profiles/premium-extended-workspace.json`
- `workspace_overlay_profiles/premium-governance.json`
- `workspace_overlay_profiles/premium-operator-runbook.json`
- `workspace_overlay_profiles/premium-orientation.json`
- `workspace_overlay_profiles/premium-skill-enablement.json`
- `workspace_overlay_profiles/premium-workspace.json`
- `workspace_overlay_profiles/provenance-continuity-local.json`
- `workspace_overlay_profiles/provenance-extended-local.json`
- `workspace_overlay_profiles/provenance-local.json`
- `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md`
- `docs/reviews/CVF_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_WORKER_RETURN_2026-07-07.md`

Allowed no-commit investigation scope:

- refresh PR #20 metadata, file list, and definition file contents through
  read-only GitHub CLI commands;
- use the PR #20 definition files only as candidate input, not as direct merge
  or cherry-pick authority;
- create a proposed overlay standard that distinguishes public-core,
  premium-workspace, and provenance-local definition lanes without claiming
  runtime installation or public release;
- create or adapt the overlay catalog and profile JSON files as static
  definitions;
- update `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` with one storage-class
  row for the new overlay pipeline reference standard, following R71;
- run static JSON/profile validation available from built-in shell or Python
  tooling, without editing checkers or scripts;
- return source-backed evidence, changed-path evidence, and gate results.

Forbidden scope:

- no GitHub merge, reopen, close, branch mutation, PR approval, or PR comment;
- no public-sync or provenance push;
- no worker commit;
- no cherry-pick, patch-apply, or bulk import of PR #20 commits;
- no overlay engine script, validation script, apply script, wrapper installer,
  bootstrap/update script, public-sync script, runtime source, test, or checker
  edit;
- no provider/live proof, no secrets or paid quota consumption;
- no public production/release/readiness claim;
- no provider status, provider routing, OpenAI certification, Known
  Limitations, README certification, or docs index certification edit;
- no direct external source import beyond read-only PR #20 candidate content;
- no private/generated MinerU output read;
- no production Memory/RAG, retrieval, vectorization, P3 reopen,
  use-case/legal workflow, hosted/public/production claim, or historical
  rename/move sweep;
- no session/front-door/handoff edit by the worker.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker, formatting, JSON-shape, and
worker-return packet defects directly by reading the failing checker source and
matching the literal required shape. Worker must not treat allowed-scope
machine-gate failures as preference questions. If the PR content is
unavailable, if a definition requires script/runtime integration to be truthful,
or if public/private lane separation cannot be source-backed, return
`BLOCKED_WITH_REASON` with exact evidence.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS --title "MSEA-R70A Workspace Overlay Standards Catalog Profile Definitions" --date 2026-07-07 --base b65ad7c76 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | public-sync plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled the scaffold from R70 accepted split evidence, R71 reference-storage requirements, PR #20 refreshed metadata, target-path absence checks, and current operator continuation. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | R70A definition-only tranche row; R70A reference-index classification row requirement; R70A PR #20 file-surface evidence row |
| claimBoundary | Dispatch authoring provenance only; no implementation, merge, push, runtime/provider/live, public release, wrapper installation, or broad overlay acceptance claim. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | section name: Dispatch Prompt Envelope; section name: Source Verification Block; section name: ADIF Defect Registry Disclosure; section name: Checker Source Read-Ahead Block; section name: Agent Handoff Contract Control Block; section name: Reviewer Closure Conversion; section name: Worker Return Packet Shape Contract; section name: Foundation Storage Layout Block; enum: DISPATCH_READY; enum: WORKER_MUST_NOT_COMMIT; enum: DEFERRED_PRIVATE_ONLY; field: completionReviewPath; field: reviewerOwnedClosurePaths |
| gateRunPurpose | Confirmation evidence before dispatch; not first discovery. |
| claimBoundary | Read-ahead covers R70A dispatch artifacts only; worker-created output must perform its own checker read-ahead before writing. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF defectId is required for this exact resolver query. |

## 5. Required First Reads

| File | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V38_2026-07-06.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/baselines/CVF_GC018_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_2026-07-07.md` | READ |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_2026-07-07.md` | READ |
| `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | READ |
| `docs/reviews/CVF_MSEA_R70_WORKSPACE_OVERLAY_PIPELINE_FEATURE_SPLIT_AND_REVIEW_DECISION_WORKER_RETURN_2026-07-07.md` | READ |
| `docs/reference/reference_artifact_storage/CVF_REFERENCE_ARTIFACT_STORAGE_CLASS_STANDARD.md` | READ |
| `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` | READ |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator said to continue after R70 acceptance and current next move | ACCEPT |
| Current session next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` key `nextAllowedMove` names fresh R70A packet authoring only | ACCEPT |
| R70 accepted worker return | R70 return recommends Tranche 1 as standards and catalog definitions, with scripts and integration forbidden | ACCEPT |
| R71 accepted reference storage standard | R71 standard and index require forward-only reference artifact classification | ACCEPT |
| Public/provenance boundary | critical repository boundary standard section `Critical Repository Boundary - 2026-05-09` | ACCEPT |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | R70 accepted PR #20 residual overlay pipeline as valuable only when split; R70A executes the first split as definition-only work. |
| scope classification | STATIC_DEFINITION_AUTHORING_NO_COMMIT |
| risk sensitivity | public/provenance boundary sensitive; no runtime, no public-sync, no provider/live proof, no scripts or wrappers |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| role separation basis | dispatcher authors packet, worker creates definitions no-commit, reviewer/closer accepts and commits if valid |
| escalation condition | PR source unavailable, profile lane leak, JSON/schema contradiction, requirement to edit scripts/runtime/checkers, public-sync need, or failing required gates outside allowed repair |
| Intake type | residual closed PR feature bundle split into definition-only tranche |
| Source role | dispatcher using R70/R71 accepted evidence |
| Target role | no-commit worker for R70A definition authoring |
| Routing disposition | ADAPT_TO_NO_COMMIT_DEFINITION_PACKET |
| Reason | definitions are valuable and separable from implementation, but must remain private/provenance until later public-safe review. |
| Claim boundary | This routing decision does not import PR #20 as authority, merge a branch, or authorize public/runtime behavior. |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | human operator | authorizes scope and later merge/push decisions if any |
| Dispatcher | dispatcher role | authors R70A baseline/work order and runs pre-dispatch gates |
| Worker | delegated worker role | authors no-commit R70A definition artifacts |
| Reviewer/closer | reviewer/closer role | reviews worker return, commits accepted material, and syncs session state after acceptance |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | one new dated active reference standard plus one existing reference index update |
| Storage decision | create `docs/reference/CVF_WORKSPACE_OVERLAY_PIPELINE_STANDARD_2026-07-07.md` as the authorized R70A reference standard path; do not rename, move, or create a stable alias in this tranche |
| Reference index requirement | update `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` with one row for the new standard, selecting `LEGACY_DATED_ACTIVE_REFERENCE` or a source-backed worker-defined equivalent class |
| Existing aggregate impact | no generated JSON aggregate impact; root catalog/profile JSON files are worker-authored static definitions, not generated state aggregates |
| Generated state impact | none; worker must not edit `CVF_SESSION/**` |
| Durable governance boundary | R70A can create proposed definition artifacts only; engine scripts, installation, validation automation, and public export require later tranches |

## Write Ownership

| Path or lane | Worker permission | Notes |
| --- | --- | --- |
| `docs/reference/CVF_WORKSPACE_OVERLAY_PIPELINE_STANDARD_2026-07-07.md` | CREATE_UNCOMMITTED | proposed reference standard |
| `workspace_overlay_catalog.json` | CREATE_UNCOMMITTED | static catalog definition |
| `workspace_overlay_profiles/premium-authoring.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/premium-boundary.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/premium-extended-workspace.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/premium-governance.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/premium-operator-runbook.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/premium-orientation.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/premium-skill-enablement.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/premium-workspace.json` | CREATE_UNCOMMITTED | static profile definition |
| `workspace_overlay_profiles/provenance-continuity-local.json` | CREATE_UNCOMMITTED | private/local profile definition |
| `workspace_overlay_profiles/provenance-extended-local.json` | CREATE_UNCOMMITTED | private/local profile definition |
| `workspace_overlay_profiles/provenance-local.json` | CREATE_UNCOMMITTED | private/local profile definition |
| `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` | MODIFY_UNCOMMITTED | add only the R70A standard storage-class row |
| `docs/reviews/CVF_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_WORKER_RETURN_2026-07-07.md` | CREATE_UNCOMMITTED | required worker return |
| GitHub PR #20 metadata and file contents | READ_ONLY | refresh through `gh` commands only; no branch mutation |
| public-sync clone | FORBIDDEN | no read/write needed in R70A worker execution |
| `CVF_SESSION_MEMORY.md`, `CVF_SESSION/`, `AGENT_HANDOFF_V38_2026-07-06.md` | FORBIDDEN_TO_WORKER | reviewer/session-sync steward only after acceptance |
| scripts, runtime source, tests, checkers | FORBIDDEN | not authorized in R70A |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=b65ad7c76; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch author changes only the R70A GC-018 baseline and R70A work order; worker may create or modify only the R70A worker-owned outputs uncommitted |
| traceScope(phase, actor) | R70A work order Agent Operation Trace Block for dispatch; worker return Agent Operation Trace Block for execution |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any accepted material commit; session-sync steward owns continuity commit |
| crossBatchIsolation | clean worktree was verified before R70A authoring; worker must preserve one-batch-per-worktree discipline and leave HEAD unchanged |
| nextMoveSurfaces | reviewer/session-sync steward updates front door, active state, and handoff only after accepted R70A return |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_COMPLETION_2026-07-07.md` (optional; prefer repairing evidence in the worker return unless a separate completion packet is required) |
| reviewerOwnedClosurePaths | `docs/reference/CVF_WORKSPACE_OVERLAY_PIPELINE_STANDARD_2026-07-07.md`; `workspace_overlay_catalog.json`; all worker-created profile JSON files; `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md`; `docs/reviews/CVF_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_WORKER_RETURN_2026-07-07.md`; session state/front door/handoff only after reviewer acceptance |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: later session-sync only after R70A material
acceptance, if the reviewer/closer accepts the worker return.

Protected paths:

| Path | Purpose |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | record R70A acceptance and next-move routing only after reviewer acceptance |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | generated compact startup facts only after accepted session-state source update |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | regenerated aggregate only after accepted session-state source update |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | update current mode only after reviewer acceptance |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | route the next move only after reviewer acceptance |
| `AGENT_HANDOFF_V38_2026-07-06.md` | record accepted R70A continuity only after reviewer acceptance |

Operator authorization: operator asked to continue from the accepted R70 split
decision. This does not authorize implementation, public push, or GitHub merge.

Rollback boundary: revert only later R70A session-sync if rejected; do not
revert R70/R71 acceptance, R69 closure, PR #3 merge, PR #21 merge, or public-sync
state.

## 6. Pre-Flight Checks

1. Capture provenance `executionBaseHead` with `git rev-parse --short HEAD`.
2. Run provenance `git status --short --branch`.
3. Refresh PR #20 metadata with `gh pr view 20 --repo Blackbird081/Controlled-Vibe-Framework-CVF-Provenance --json number,state,title,url,baseRefName,headRefName,baseRefOid,headRefOid,commits,files,statusCheckRollup,mergeStateStatus,closedAt,mergedAt`.
4. Refresh PR #20 changed paths with `gh pr diff 20 --repo Blackbird081/Controlled-Vibe-Framework-CVF-Provenance --name-only`.
5. Fetch candidate file contents read-only through `gh pr diff 20` or `gh api repos/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance/contents/<path>?ref=b4676d09bbe689b3f92b85f1ebb83236bea7e2ff`.
6. Confirm no merge, push, reopen, cherry-pick, apply, script edit, or commit is performed.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Current session next move authorizes fresh R70A standards/catalog/profile-definition packet authoring only | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | key `nextAllowedMove` | nextAllowedMove | active session bootstrap read model | ACCEPT |
| R70 worker return recommends Tranche 1 as standard, catalog, and profile definitions with script execution and integration forbidden | `docs/reviews/CVF_MSEA_R70_WORKSPACE_OVERLAY_PIPELINE_FEATURE_SPLIT_AND_REVIEW_DECISION_WORKER_RETURN_2026-07-07.md` | section `Split & Follow-Up Tranche Plan` | Tranche 1: Standards and Catalog Definitions | R70 accepted worker return | ACCEPT |
| R70 worker return selected split acceptance, not direct implementation or merge | `docs/reviews/CVF_MSEA_R70_WORKSPACE_OVERLAY_PIPELINE_FEATURE_SPLIT_AND_REVIEW_DECISION_WORKER_RETURN_2026-07-07.md` | section `Decision Matrix` | split acceptance recommendation | R70 accepted worker return | ACCEPT |
| Public-facing changes must use the sibling public-sync clone and remote verification | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | section `Critical Repository Boundary - 2026-05-09` | public-sync clone | critical repository boundary standard | ACCEPT |
| Reference artifacts created on or later than 2026-07-07 require storage-class classification and index guidance | `docs/reference/reference_artifact_storage/CVF_REFERENCE_ARTIFACT_STORAGE_CLASS_STANDARD.md` | section `Scope / Applies To` | reference artifact storage class taxonomy | R71 accepted storage-class standard | ACCEPT |
| Reference artifact index defines how to add rows | `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` | row-addition instructions | Reference Artifact Index table | R71 accepted reference artifact index | ACCEPT |
| Work order template requires dispatch envelope and source-verification surfaces used here | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | sections `Dispatch Prompt Envelope Placement Rule` and `Source Verification Block` | Dispatch Prompt Envelope | work order template | ACCEPT |
| No-commit work orders must include Reviewer Closure Conversion | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | section `Review Gate` | Reviewer Closure Conversion | work order template | ACCEPT |
| ADIF resolver returned no defects for this dispatch-authoring query | canonical-contract marker: `governance/compat/run_adif_defect_resolver.py` | command output recorded in this packet | NONE_RETURNED | ADIF resolver invocation | ACCEPT |

## GitHub PR Evidence Block

| Evidence item | Command or source | Observed result | Disposition |
| --- | --- | --- | --- |
| PR #20 state | `gh pr view 20 --repo Blackbird081/Controlled-Vibe-Framework-CVF-Provenance --json number,state,title,url,baseRefName,headRefName,baseRefOid,headRefOid,commits,files,statusCheckRollup,mergeStateStatus,closedAt,mergedAt` | state `CLOSED`; `mergedAt` null; head `b4676d09b`; base `77f9b15f`; `mergeStateStatus` `DIRTY` | COMMAND_VERIFIED |
| PR #20 target definition files | same PR metadata command plus `gh pr diff 20 --repo Blackbird081/Controlled-Vibe-Framework-CVF-Provenance --name-only` | one overlay standard, `workspace_overlay_catalog.json`, and eleven profile JSON files are present in the PR file surface | COMMAND_VERIFIED |
| PR #20 excluded files | same PR metadata command | scripts, installer, public-sync, docs guide touchpoints, and update/bootstrap files are present but excluded from R70A | COMMAND_VERIFIED |
| Current local target-path absence | `Test-Path` and `rg --files` for the R70A definition targets | target standard, catalog, and profile folder are absent in HEAD before dispatch authoring | COMMAND_VERIFIED |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch path existence before authoring | `Test-Path` returned `False` for the R70A GC-018 and work-order target paths before authoring | ACCEPT |
| Definition target absence before authoring | `Test-Path` returned `False` for the target standard, target catalog, and profile folder before authoring | ACCEPT |
| Dispatch collision search | `rg -n "MSEA_R70A|MSEA-R70A|WORKSPACE_OVERLAY_STANDARDS_CATALOG|CVF_GC018_MSEA_R70A|CVF_AGENT_WORK_ORDER_MSEA_R70A" docs/baselines docs/work_orders docs/reviews CVF_SESSION/state CVF_SESSION_MEMORY.md AGENT_HANDOFF_V38_2026-07-06.md` | existing hits are only current-session next-move references, not prior R70A dispatch or review artifacts | ACCEPT |
| Collision decision | R70A artifact identifiers were unused in active baseline, work-order, and review surfaces before this dispatch | ACCEPT |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return artifact | derive exact review headings, worker-return quality terms, trace labels, Delta block labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference standard | derive exact reference headings, storage/index metadata expectations, source verification, claim-boundary, and public export disposition before writing |
| catalog and profile JSON files | derive valid JSON parsing and profile-lane consistency checks before writing; do not invent runtime semantics without source text |
| reference artifact index | derive the six row fields from R71 index and preserve existing rows without rename/move sweep |

Literal-shape reminders: do not list required worker-output sections as heading
syntax before the real section; write source-not-found disposition spelling
instead of the exact blocked enum in literalTokensReviewed; avoid broad
dependency-placeholder wording unless a dependency-release row cites the
accepted artifact path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| Overlay pipeline reference standard | create proposed reference standard with `Memory class`, `Status`, `docType`, `Purpose`, `Scope / Applies To`, `Claim Boundary`, and `Public Export Disposition` |
| Overlay catalog JSON | create valid JSON catalog with lane/profile metadata and clear public/premium/provenance separation |
| Premium profile JSON files | create valid JSON profiles for the eight premium lanes named in Write Ownership |
| Provenance-local profile JSON files | create valid JSON profiles for the three provenance-local lanes named in Write Ownership, with private/local claim boundary |
| Reference artifact index row | update only the R70A standard row in `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` |
| Worker return | create no-commit worker return with gate evidence and changed-path evidence |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_WORKER_RETURN_2026-07-07.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must include:

- Status line with exactly `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- `executionBaseHead` captured at worker start.
- Changed-path evidence from `git status --short --untracked-files=all` and
  `git diff --name-status`.
- Source Verification Block or explicit command-evidence block for PR #20 facts.
- Source Inventory with bare action tokens only: `READ`, `FULL_READ`,
  `PARTIAL_READ`, or `SOURCE_VERIFIED`.
- Checker Source Read-Ahead Block.
- Agent Operation Trace Block.
- Public/provenance boundary statement.
- JSON validation evidence for catalog and profile files.
- Reference artifact index classification evidence.
- Worker-return fast gate evidence.
- Exact claim boundary and no-commit confirmation.

## Execution Plan

1. Read all Required First Reads.
2. Capture `executionBaseHead`, provenance status, and PR #20 metadata.
3. Retrieve the target PR #20 definition file contents read-only.
4. Write the reference standard as a CVF-owned proposed standard, not a direct
   merge artifact.
5. Write valid JSON catalog/profile files and preserve explicit lane
   separation between public-core, premium-workspace, and provenance-local.
6. Update only the R70A row in `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md`.
7. Run JSON parsing and any static profile consistency checks feasible without
   scripts/runtime changes.
8. Run worker-return fast gate.
9. Leave all changes uncommitted and return the exact result token.

## Evidence Requirements

| Evidence | Required content | Failure disposition |
| --- | --- | --- |
| PR #20 metadata and definition content | number, URL, state, head, target files, content source command | BLOCKED_WITH_REASON if unavailable |
| Definition path manifest | exact created/modified paths and no extra paths | BLOCKED_WITH_REASON if drifted |
| JSON validity | command evidence that catalog and all profiles parse as JSON | BLOCKED_WITH_REASON if invalid |
| Lane separation | profile/catalog text distinguishes public-core, premium-workspace, and provenance-local without public/private leakage | BLOCKED_WITH_REASON if unsafe |
| R71 index update | exactly one row for the new reference standard, storage class source-backed | BLOCKED_WITH_REASON if unclear |
| Boundary evidence | no scripts, runtime, tests, checkers, public-sync, provider/live, merge, push, or commit | BLOCKED_WITH_REASON if violated |
| Gate evidence | worker-return fast gate output and any additional static checks run | BLOCKED_WITH_REASON if required gate fails outside allowed repair |

## Verification Commands

Worker must run these commands before returning:

```powershell
git rev-parse --short HEAD
git status --short --branch
gh pr view 20 --repo Blackbird081/Controlled-Vibe-Framework-CVF-Provenance --json number,state,title,url,baseRefName,headRefName,baseRefOid,headRefOid,commits,files,statusCheckRollup,mergeStateStatus,closedAt,mergedAt
gh pr diff 20 --repo Blackbird081/Controlled-Vibe-Framework-CVF-Provenance --name-only
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
```

Worker must also run a JSON parse check for `workspace_overlay_catalog.json` and
every worker-created profile JSON file. If PowerShell or Python JSON parsing is
unavailable, return `BLOCKED_WITH_REASON` rather than claiming JSON validity.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| No mutation beyond worker-owned outputs | HEAD unchanged and only allowed worker-owned outputs are uncommitted |
| PR #20 evidence refreshed | worker return includes current PR state, target file list, and content source commands |
| Definition-only scope preserved | no scripts, runtime source, tests, checkers, public-sync, merge, push, or wrapper integration |
| JSON validity proven | catalog and profiles parse successfully |
| Public/provenance lane separation explicit | premium and provenance-local profiles do not silently become public-safe claims |
| R71 index updated narrowly | reference artifact index adds exactly the R70A standard row and preserves existing rows |
| No public/runtime overclaim | no public release, production, provider/live, runtime behavior, hosted readiness, or enforcement claim is made |

## Review Gate

Reviewer/closer must not accept R70A unless the worker return:

- preserves no-commit execution;
- names exact PR #20 evidence and content-source commands;
- creates only allowed definition artifacts;
- proves JSON validity;
- updates the reference index row safely;
- does not silently implement overlay behavior;
- passes worker-return fast gate or returns a source-backed block reason.

## Closure Checklist

| Item | Required closure disposition |
| --- | --- |
| Worker-owned output manifest matches work order | PASS or BLOCKED_WITH_REASON |
| Worker return exists at required path | PASS or BLOCKED_WITH_REASON |
| Worker return gate evidence present | PASS or BLOCKED_WITH_REASON |
| JSON validation evidence present | PASS or BLOCKED_WITH_REASON |
| R71 index row evidence present | PASS or BLOCKED_WITH_REASON |
| Reviewer owned commit decision | PASS, HOLD, or REJECT |
| Session-sync need determined | PASS or N/A with reason |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when:

- all worker-owned outputs are created or updated at the exact allowed paths;
- PR #20 metadata/path/content evidence is refreshed;
- JSON validity and lane separation are proven;
- reference index row update is source-backed;
- required gates pass;
- HEAD remains unchanged by the worker.

Return `BLOCKED_WITH_REASON` when:

- PR #20 evidence or target file contents cannot be fetched;
- the definition set cannot be separated from script/runtime behavior;
- public/provenance lane separation conflicts;
- JSON validation fails and cannot be repaired inside Allowed scope;
- worker-return gates fail outside allowed worker repair scope;
- any action would require merge, push, cherry-pick, implementation, runtime edit,
  public-sync mutation, checker edit, test edit, or provider/live proof.

## Operator Checkpoint

No operator checkpoint is required for the worker to perform this no-commit
definition tranche. Operator authorization is required later for any merge,
push, implementation, public-sync mutation, broad overlay-pipeline acceptance,
or downstream script/integration tranche.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | R70A dispatch authoring at base `b65ad7c76` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, GitHub CLI, apply_patch, governance gates |
| Target paths | R70A GC-018 baseline and R70A work order |
| Allowed scope source | accepted R70 split decision and session next move after commit `b65ad7c76` |
| Before status evidence | clean worktree before R70A authoring; base `b65ad7c76` |
| After status evidence | R70A dispatch artifacts authored; pre-dispatch gates to run before commit |
| Diff evidence | `git diff --name-status` and pre-dispatch gate output |
| Approval boundary | dispatch authoring only; no implementation, merge, push, public-sync mutation, provider/live proof, runtime/source/test/checker edit |
| Claim boundary | repo-local dispatch trace only; no OS/user attribution, runtime behavior, public-release posture, or provider behavior claim |
| Agent type | Codex |
| Invocation ID | r70a-overlay-standards-catalog-profile-definitions-dispatch-2026-07-07 |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_2026-07-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_2026-07-07.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_2026-07-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R70A_WORKSPACE_OVERLAY_STANDARDS_CATALOG_PROFILE_DEFINITIONS_2026-07-07.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | R70A definition-only dispatch packet |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | local governed document and JSON authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, wrapper, proxy, or public repository interception claim |
| claimLanguage | dispatches proposed definition authoring only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router behavior, implementation, merge, push, public-sync, wrapper installation, checker edit, or source/test edit without fresh source-verified authorization |

## Public/Provenance Boundary

| Field | Value |
| --- | --- |
| Provenance repo | this workspace is the private provenance repository |
| Public-sync boundary | public-facing changes require a separate public-sync packet and remote verification; R70A worker must not touch public-sync |
| Export disposition | see `## Public Export Disposition` below |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch packet. It does not change
public-sync, push public branches, or publish public artifacts. Any later
public surface change requires a separate public-sync governed packet.

## Claim Boundary

This work order authorizes only no-commit definition authoring for R70A. It
does not authorize implementation, merge, push, cherry-pick, public-sync
mutation, provider/live proof, runtime/source/test edit, checker edit, wrapper
installation, public release claim, or direct downstream release.
