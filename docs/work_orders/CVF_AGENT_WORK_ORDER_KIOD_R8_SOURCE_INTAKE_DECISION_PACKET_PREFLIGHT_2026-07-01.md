# CVF Agent Work Order - KIOD-R8 Source Intake Decision Packet Preflight

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: KIOD-R8

Dispatch base head: d77d5f52

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated external agent

Reviewer/closer: Codex

Completion review path: `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_COMPLETION_2026-07-01.md`

Worker return path: `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_WORKER_RETURN_2026-07-01.md`

## Dispatch Prompt Envelope

Role: delegated external worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_2026-07-01.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: d77d5f52.

Current-time notes: artifact date is 2026-07-01; worker must use repository files as authority, not chat memory.

Do-not-misread notes: this is a source-intake decision packet preflight tranche only; do not absorb a real outside source.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the GC-018 baseline, and applicable checker source before writing.

Return contract: create the worker return artifact, run required gates, leave changes uncommitted.

## Purpose

Create the KIOD-R8 standard, checker, tests, and catalog wiring needed to block
future source-intake worker dispatches that omit decision-packet evidence.

## 1. Authority Chain

| Authority | Path or value | Disposition |
| --- | --- | --- |
| Operator decision | KIOD-R8 source-intake decision packet preflight | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V30_2026-07-01.md` | ACCEPT |
| Active session mode | `kiod_r7_dispatch_packet_lifecycle_hygiene_closed_pass_bounded_pending_operator_next_lane_selection` | ACCEPT |
| Dispatch base | d77d5f52 | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_2026-07-01.md` | ACCEPT |

## 2. Agent Roles

| Role | Actor | Authority |
| --- | --- | --- |
| Dispatcher | Codex | Creates GC-018 baseline and work order. |
| Worker | delegated external agent | Implements only allowed artifacts and writes worker return. |
| Reviewer/closer | Codex | Reviews worker return, repairs if accepted, commits material batch, and performs session sync. |

## 3. Transfer Objective

Implement a source-intake decision packet standard and a range-aware preflight
checker so future repo/folder knowledge-intake dispatches are blocked unless
they explicitly record source owner surfaces, pre-scan evidence, overlap
routing, negative-search evidence, value-conversion routing, worker output
paths, forbidden scope, and claim boundaries before a worker starts writing.

This is a governance-foundation tranche. Do not absorb a real outside source in
this tranche.

## 4. Required First Reads

Worker must read these before writing any governed artifact:

| Read order | Required file or command |
| --- | --- |
| 1 | `CVF_SESSION_MEMORY.md` |
| 2 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| 3 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| 4 | Active handoff named by state: `AGENT_HANDOFF_V30_2026-07-01.md` |
| 5 | `docs/reference/guard_orientation/README.md` |
| 6 | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` |
| 7 | This work order and the KIOD-R8 GC-018 baseline |
| 8 | All checkers listed in `## Checker Source Read-Ahead Block` |

## 5. Pre-Flight Checks

| Check | Required worker action |
| --- | --- |
| Base anchor | Confirm execution base is d77d5f52 before editing. |
| Scope | Confirm planned edits match Allowed Artifact Manifest. |
| Checker vocabulary | Read checker constants before authoring standard, checker, tests, and worker return. |
| Path collision | Confirm planned output paths do not already exist, unless modifying the exact allowed catalog files. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need, or
missing authority that makes completion impossible.

## 6. Worker Operating Mode

| Rule | Required behavior |
| --- | --- |
| Commit mode | WORKER_MUST_NOT_COMMIT |
| Worker return | Create only `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_WORKER_RETURN_2026-07-01.md`. |
| No-question rule | Resolve checker failures by reading the checker source and repairing allowed-scope artifacts. Ask only if the work order is logically impossible. |
| Checker-first rule | Read all applicable checker source before writing the first governed artifact line. |
| Scope discipline | Stay inside the allowed artifact list. Do not edit runtime, package skills, Web, public-sync, MCP/CLI adapters, model routing, provider config, or session state. |

## Write Ownership

| Surface | Owner |
| --- | --- |
| Worker implementation files | Worker may create or modify only allowed artifacts. |
| Worker return | Worker owns authoring; reviewer owns acceptance. |
| Material commit | Reviewer only. |
| Session state, front door, active handoff | Reviewer/closer only after accepted material commit. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific defect rows are required for this work order. Worker must still treat checker read-ahead as mandatory. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_package_skill_productionization_pipeline.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `## External Knowledge Intake Routing`; `## Source Verification Block`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Core Guard Self-Protection Authorization`; `Worker Return Packet Shape Contract`; `Intake Role Routing Decision`; `Source intake decision packet: REQUIRED` |
| gateRunPurpose | Pre-dispatch confirmation evidence, not first discovery. |
| claimBoundary | This block records dispatcher read-ahead. The worker must repeat checker read-ahead before implementation and list it in the worker return. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| KIOD owner-surface taxonomy is the canonical local owner surface source. | EXISTS | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | lines 30-55 | `Owner Surface Taxonomy` | KIOD-R1 taxonomy standard | ACCEPT |
| KIOD pre-scan packet standard requires a bounded pre-scan packet before knowledge intake. | EXISTS | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | lines 30-57 | `Required Pre-Scan Packet` | KIOD-R2 pre-scan standard | ACCEPT |
| KIOD overlap routing matrix defines allowed overlap dispositions. | VALUE_SET | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | lines 28-37 | `CONFIRMED_EXISTING; ENRICH_EXISTING; NEW_FINDING; REJECT_DIRECT_IMPORT; NO_NEW_VALUE; OWNER_SURFACE_NOT_FOUND` | KIOD-R3 overlap routing matrix | ACCEPT |
| Core block fields and disposition taxonomy exist for outside-source intake artifacts. | EXISTS | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | lines 102-145 | `## External Absorption Core` | External Absorption Core Standard | ACCEPT |
| Value-conversion columns and allowed lane tokens exist. | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | lines 160-181 | `DOCTRINE_ADAPTED; PACKAGE_CANDIDATE; RUNTIME_CANDIDATE; CHECKER_CANDIDATE; REJECT_DIRECT_IMPORT; NO_PACKAGE_OR_RUNTIME_VALUE` | External Absorption Core Standard | ACCEPT |
| Overlap classification columns and allowed disposition tokens exist. | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | lines 195-223 | `CONFIRMED_EXISTING; ENRICH_EXISTING; NEW_FINDING; REJECT_DIRECT_IMPORT; NO_NEW_VALUE; OWNER_SURFACE_NOT_FOUND` | External Absorption Core Standard | ACCEPT |
| Intake routing guard already checks required routing fields and input-type vocabulary. | EXISTS | `governance/compat/check_external_knowledge_intake_routing.py` | constants near lines 22-52 | `REQUIRED_FIELDS; ALLOWED_INPUT_TYPES` | `check_external_knowledge_intake_routing.py` | ACCEPT |
| Checker read-ahead field names are machine-checked. | VALUE_SET | `governance/compat/check_governed_artifact_checker_read_ahead.py` | constants near lines 20-39 | `applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary` | `check_governed_artifact_checker_read_ahead.py` | ACCEPT |
| Handoff boundary guard checks WORKER_MUST_NOT_COMMIT and reviewer closure conversion. | EXISTS | `governance/compat/check_agent_handoff_boundary.py` | constants and validation around lines 38-54 and 305-320 | `Reviewer Closure Conversion` | `check_agent_handoff_boundary.py` | ACCEPT |
| Work order template includes source verification, roadmap trace, guard self-protection, execution plan, evidence, review gate, and claim-boundary blocks. | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 392-1082 | `Source Verification Block; Roadmap-To-Work-Order Trace Matrix; Core Guard Self-Protection Authorization; Execution Plan; Evidence Requirements; Review Gate; Delta Execution Claim Boundary Control Block` | Work order template | ACCEPT |
| Existing catalogs use checker path strings as wiring owner surfaces. | EXISTS | `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` | current catalog entries include external intake and KIOD-R7 guards | `governance/compat/check_external_absorption_core.py` | Governance command catalogs | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R8 token collision search | `rg -n "KIOD-R8|SOURCE_INTAKE_DECISION_PACKET|Source Intake Decision Packet|Absorption Decision Packet" docs governance CVF_SESSION AGENTS.md` returned only synthetic R7 checker test fixture lines. | ACCEPT |
| Planned path existence | `Test-Path` returned `False` for the planned baseline, work order, standard, and checker paths. | ACCEPT |
| Collision decision | No existing source-intake decision packet standard or checker is present. | ACCEPT |

Search command: `rg -n "KIOD-R8|SOURCE_INTAKE_DECISION_PACKET|Source Intake Decision Packet|Absorption Decision Packet" docs governance CVF_SESSION AGENTS.md`

Search roots: `docs`; `governance`; `CVF_SESSION`; `AGENTS.md`

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `external knowledge intake routing guard implementation` |
| Chain map route | Guard-foundation work for source-intake routing and decision discipline. |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/` and `governance/compat/` |
| Disposition | GOVERNANCE_GUARD_FOUNDATION_ONLY |
| Claim boundary | This work order authorizes a preflight guard. It does not authorize absorbing any outside source in this tranche. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or decision source | Requirement | Work-order instruction | Disposition |
| --- | --- | --- | --- |
| Operator-selected next tranche after KIOD-R7 | Strengthen pre-dispatch discipline for future source intake. | Create standard, checker, tests, and catalog wiring. | ACCEPT |
| KIOD-R1/R2/R3 foundation | Preserve owner-surface, pre-scan, and overlap routing discipline. | Source-verify and require these fields in the new packet standard/checker. | ACCEPT |
| KIOD-R7 lifecycle hygiene | Prevent stale dispatch state and role-boundary drift. | Keep worker in WORKER_MUST_NOT_COMMIT and require reviewer closure conversion. | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher_to_worker_to_reviewer |
| phase | pre-dispatch_to_worker_implementation_to_reviewer_closure |
| baseHeadFor(phase) | dispatchBaseHead=d77d5f52; executionBaseHead=d77d5f52; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Allowed Artifact Manifest only during worker phase; reviewer may add completion review and session-sync paths after acceptance. |
| traceScope(phase, actor) | Worker return must include command evidence for required gates and manifest diff; reviewer completion must include closure evidence. |
| commitOwner(phase) | Worker must not commit; reviewer owns material commit and session-sync commit. |
| crossBatchIsolation | Do not mix KIOD-R8 with DEFER candidates, EverOS intake, CodeGraph intake, Web/dashboard, MCP/CLI, model gateway, public-sync, or package-skill runtime work. |
| nextMoveSurfaces | Worker must not edit active session state, front door, or active handoff. Reviewer/closer owns next-move surface updates after acceptance. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_COMPLETION_2026-07-01.md` |
| reviewerOwnedClosurePaths | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/current_mode.json`; `CVF_SESSION/state/handoff.json`; `CVF_SESSION/state/latest_commits.json`; `CVF_SESSION/state/latest_material.json`; `CVF_SESSION/state/next_allowed_move.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; active handoff successor if V30 approaches size limit |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake role | governance guard-foundation worker |
| Route | Worker implements standard/checker/tests/catalog wiring; reviewer handles commit and session sync. |
| canonical route mode | MULTI_AGENT_SINGLE_ROLE |
| selected role route | worker return to reviewer/closer closure conversion |
| scope classification | governance-foundation checker tranche |
| risk sensitivity | high: packet-shape and source-intake discipline gate future governed absorption work |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require forbidden scope, weaker checker behavior, source absorption pilot, runtime/provider/live proof, package-skill mutation, public-sync, or session-state edits |
| Reason | The tranche creates decision-packet preflight infrastructure, not source content intake. |
| Boundary | No outside-source absorption pilot is authorized. |

## Core Guard Self-Protection Authorization

| Protected surface | Authorized change | Guardrail |
| --- | --- | --- |
| `docs/reference/external_agent_review/` | Add the KIOD-R8 source-intake decision packet standard only. | Must be source-verified and ASCII-only. |
| `governance/compat/check_source_intake_decision_packet_preflight.py` | Add a new range-aware checker. | Must support `--base`, `--head`, and `--enforce`. |
| `governance/compat/test_source_intake_decision_packet_preflight.py` | Add focused unit tests. | Must cover pass and fail cases. |
| Governance command catalogs | Wire the new checker into autorun, reviewer-fast, pre-commit, and pre-push catalogs. | Must preserve existing catalog entries. |

## Allowed Artifact Manifest

| Path | Worker disposition |
| --- | --- |
| `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` | CREATE |
| `governance/compat/check_source_intake_decision_packet_preflight.py` | CREATE |
| `governance/compat/test_source_intake_decision_packet_preflight.py` | CREATE |
| `governance/compat/agent_autorun_command_catalog.py` | MODIFY |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | MODIFY |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | MODIFY |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | MODIFY |
| `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_WORKER_RETURN_2026-07-01.md` | CREATE |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Standard source | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Front door | `docs/reference/foundation_storage/README.md` |
| Durable governance folder | `docs/reference/external_agent_review/` |
| New durable file | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` |
| Index action | N/A with reason: existing external-agent review folder already acts as the owner surface for KIOD governance references in this bounded tranche. |
| Claim boundary | Adds one bounded KIOD reference standard; no folder migration, generated aggregate, or public index mutation is authorized. |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: KIOD-R8 does not create, promote, certify, or activate a package skill.

Target lifecycle state: N/A with reason: no package-skill lifecycle state changes.

Prior phase evidence: N/A with reason: no package-skill prior phase applies.

Next forbidden skip: package-skill productionization, certification, activation, CLI/MCP adapter expansion, or package runtime eligibility claims.

Runtime/provider proof: N/A with reason: no runtime or provider behavior is changed or claimed.

Claim boundary: This block is a negative scope control only; KIOD-R8 is source-intake governance preflight work.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: Worker implementation must recompute checker/test/gate evidence after creating KIOD-R8 artifacts.

unicodePathHandling: use literal paths and UTF-8-safe readers for any path or text evidence.

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| Evidence reuse mode | RECOMPUTE_REQUIRED for worker implementation; dispatcher source-verification evidence is for dispatch only. |
| verificationMode | RECOMPUTE_REQUIRED |
| unicodePathHandling | N/A with reason: no Unicode-path evidence is used as source authority in this tranche. |
| extractedTextAuthority | N/A with reason: no extracted text is used as source authority in this tranche. |
| External evidence reuse | N/A with reason: no outside source bundle, extracted text, Unicode-path evidence, or T11B evidence is reused in this tranche. |
| Encoding plan | ASCII-only for worker-authored governed artifacts unless an existing source path requires otherwise. |
| Claim boundary | This plan prevents evidence-reuse ambiguity; it does not authorize source intake completion. |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| Runtime files changed | N/A with reason: no runtime files are in allowed scope. |
| Runtime claim | N/A with reason: the work order makes no current runtime behavior claim. |
| Freshness command | N/A with reason: runtime verification is not applicable to this governance-foundation dispatch. |
| Claim boundary | Runtime, provider, package, Web, MCP, CLI, and public-sync behavior remain outside this tranche. |

## Forbidden Scope

Do not modify runtime source, package skills, Web/UI/dashboard files, MCP or CLI
adapters, model gateway or provider registry code, public-sync repositories,
session state, active handoff, unrelated reviews, archived handoffs, generated
JSON aggregates, or any outside-source intake artifacts.

Do not absorb `EverMind-AI/EverOS`, `colbymchenry/codegraph`, or any other
outside source in this tranche.

## Required Standard Shape

The new standard must define:

| Required item | Required token or behavior |
| --- | --- |
| Applicability marker | `Source intake decision packet: REQUIRED` |
| Required section | `## Source Intake Decision Packet` |
| Required fields | `Decision packet standard`; `Input root or repository`; `Bounded scope`; `Enumeration authority`; `Owner-surface taxonomy`; `Pre-scan packet source`; `Overlap routing matrix`; `Negative-search evidence`; `Core disposition`; `Value conversion requirement`; `Overlap classification requirement`; `Worker output path`; `Forbidden scope`; `Claim boundary` |
| Required co-sections | `## External Knowledge Intake Routing`; `## External Absorption Core`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification` |
| Escalation rule | If `OWNER_SURFACE_NOT_FOUND` or `NEW_FINDING` appears, the artifact must include negative-search evidence and a concrete next governed action. |
| Claim boundary | The packet is pre-dispatch evidence only. It is not proof that source intake has been completed. |

## Required Checker Behavior

The new checker must:

| Requirement | Expected behavior |
| --- | --- |
| Range awareness | Accept `--base` and `--head`; skip unchanged files. |
| Enforce mode | Accept `--enforce`; nonzero exit on violations. |
| Applicability | Apply only to changed governed files that contain `Source intake decision packet: REQUIRED`. |
| Required fields | Fail when any required packet field is missing or blank. |
| Co-section discipline | Fail when required source-intake co-sections are absent. |
| Escalation discipline | Fail when `OWNER_SURFACE_NOT_FOUND` or `NEW_FINDING` appears without negative-search evidence and a concrete next governed action. |
| Output | Print actionable file/path messages suitable for dispatcher and worker repair. |

## Execution Plan

| Step | Worker action | Evidence required |
| --- | --- | --- |
| 1 | Re-read this work order, the baseline, guard orientation, literal-format gotchas, and all applicable checkers. | Worker return read-ahead table. |
| 2 | Create the KIOD-R8 standard. | New standard path and summary. |
| 3 | Implement the checker. | Checker path and behavior summary. |
| 4 | Add focused tests. | Unit test command output. |
| 5 | Wire the checker into autorun and local hook catalogs. | Catalog diff summary. |
| 6 | Run required verification commands. | Command log with pass/fail and remediation notes. |
| 7 | Write worker return. | Worker return path, no commit. |

## Evidence Requirements

Worker must run and report:

| Command | Required result |
| --- | --- |
| `python -m unittest governance.compat.test_source_intake_decision_packet_preflight` | PASS |
| `python governance/compat/check_source_intake_decision_packet_preflight.py --enforce` | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base d77d5f52 --head HEAD` | PASS or explicit blocker caused only by out-of-scope pre-existing residue |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base d77d5f52 --head HEAD` | PASS or explicit blocker caused only by out-of-scope pre-existing residue |
| `git diff --name-status d77d5f52..HEAD` | Must contain only allowed artifact paths plus worker return. |
| `git status --short` | Must show uncommitted worker changes only; worker must not commit. |

## Acceptance Criteria

| Criterion | Required disposition |
| --- | --- |
| KIOD-R8 standard exists | New standard contains required marker, section, fields, co-section discipline, escalation rule, and claim boundary. |
| Checker exists | New checker is range-aware, enforce-capable, and emits actionable violations. |
| Tests exist | Unit tests cover passing packet, missing field, missing co-section, escalation without negative-search evidence, and range skipping. |
| Catalogs wired | Autorun, reviewer-fast, pre-commit, and pre-push catalogs include the checker. |
| Worker return complete | Worker return includes source read-ahead, command evidence, diff evidence, and no commit. |

## Review Gate

Reviewer must reject or repair if:

| Failure condition | Reviewer action |
| --- | --- |
| Worker edited forbidden scope. | Reject or surgically remove out-of-scope edits before any commit. |
| Checker was debugged by repeated blind gate runs instead of checker read-ahead. | Add defect note or require worker repair. |
| Standard omits required fields or co-sections. | Repair before commit. |
| Checker is not range-aware or not wired into catalogs. | Repair before commit. |
| Worker return lacks literal command evidence. | Reject pending evidence repair. |
| Worker committed. | Stop and return to reviewer for repository repair. |

## Worker Return Packet Shape Contract

Worker return must include these headings and fields:

| Required surface | Required worker content |
| --- | --- |
| `Status:` | `COMPLETE_PENDING_REVIEW` or `BLOCKED_RETURN_TO_ORCHESTRATOR` |
| `executionBaseHead` | Exact value from `git rev-parse --short HEAD` at worker start. |
| `git status --short` | Exact output after worker changes; worker must not report a false empty status. |
| Purpose | One-paragraph statement of completed KIOD-R8 scope. |
| Scope / Methodology | Required. |
| Findings / Position | Required. |
| Risk / Corrective Action | Required. |
| Checker Source Read-Ahead Block | Applicable checker paths, literal tokens, gate-run purpose, and claim boundary. |
| Source Verification Block | Source rows for any runtime/source/checker/canonical facts used. |
| Implementation Summary | Files created or modified, with no runtime/package/public claims. |
| Verification Evidence | Commands and results. |
| Agent Operation Trace Block | Complete trace labels matching the operation trace checker. |
| Delta Execution Claim Boundary Control Block | Canonical Delta claim rows with bounded or N/A dispositions. |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` unless reviewer later authorizes public-sync. |
| External Knowledge Intake Routing | Required because this tranche changes intake guard foundations. |
| Rescan Intelligence Hardening | Include `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` if not applicable. |
| Corpus Completeness And Report Integrity | Include `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` if not applicable. |
| Finding-To-Governance Learning Disposition | Include `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` if not applicable. |
| Epistemic Process Block | Include `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` if not applicable. |
| Machine Closure Package | Include worker-level N/A or pending-review status without claiming reviewer closure. |
| Claim Boundary | No outside-source intake completion, runtime, package, public-sync, provider/live, Web, MCP, CLI, or model-router claim. |

Conditional worker-return sections that do not apply must still be present with
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON`.

## Closure Checklist

| Closure item | Required status before reviewer commit |
| --- | --- |
| Worker stayed inside allowed scope | REQUIRED |
| Worker return exists and is complete | REQUIRED |
| New checker unit tests pass | REQUIRED |
| New checker enforce run passes | REQUIRED |
| Pre-closure autorun passes or records only out-of-scope pre-existing residue | REQUIRED |
| Reviewer completion review created | REVIEWER_ONLY |
| Session sync completed after material commit | REVIEWER_ONLY |

## Return-To-Orchestrator Conditions

| Condition | Required return action |
| --- | --- |
| Required source contradiction | Stop and report exact files/lines. |
| Need to edit forbidden scope | Stop with blocker report naming exact forbidden path or authority gap. |
| Applicable checker cannot be satisfied without weakening governance | Stop and report checker, failing message, and proposed governance decision. |
| Missing authority for standard field or checker requirement | Stop with `BLOCKED_SOURCE_NOT_FOUND`. |

## Human Dispatch Checkpoint

operator.checkpoint.waiver

| Field | Value |
| --- | --- |
| Required before worker execution | No additional human checkpoint is required; the requested work order has been created. |
| Required before commit | Reviewer acceptance of worker return. |
| Required before future source-intake pilot | Fresh human selection of target source and scope. |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | KIOD-R8 source-intake decision packet preflight governance artifacts only. |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: GC-018 baseline, work order, source verification, and required worker command evidence. |
| invocationBoundary | local governed documentation, checker, test, and catalog edits only. |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, daemon, or public-sync interception claim. |
| claimLanguage | Guard-foundation preflight only; no source intake completion or runtime enforcement claim. |
| forbiddenExpansion | no outside-source pilot, runtime/package/Web/MCP/CLI/model-router/public-sync/provider-live change, package activation, production-readiness, or automatic invocation claim. |

## Agent Operation Trace Block

| Field | Value |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local PowerShell and repository filesystem |
| Session or invocation | KIOD-R8 dispatch authoring on 2026-07-01 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Test-Path`; `apply_patch`; autorun pre-dispatch |
| Target paths | GC-018 baseline and this work order |
| Allowed scope source | Human approval for KIOD-R8 and GC-018 baseline |
| Before status evidence | dispatchBaseHead=d77d5f52; `git status --short` produced no output before edits; clean worktree at dispatch start |
| After status evidence | pre-dispatch pending after packet repair |
| Diff evidence | `git diff --name-status d77d5f52..HEAD` plus untracked dispatch artifact status before commit |
| Approval boundary | Operator approved creating the work order; worker commit remains forbidden. |
| Claim boundary | Dispatch-packet creation only; worker implementation and closure remain pending. |
| Agent type | dispatcher/reviewer |
| Invocation ID | KIOD-R8-source-intake-decision-packet-preflight |
| Expected manifest | `docs/baselines/CVF_GC018_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_2026-07-01.md` |
| Actual changed set | `docs/baselines/CVF_GC018_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_2026-07-01.md` |
| Manifest delta | MATCH |
| dispatchBaseHead | d77d5f52 |
| executionBaseHead | d77d5f52 |
| closureBaseHead | REVIEWER_TO_SET |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | This work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_PREFLIGHT_COMPLETION_2026-07-01.md` | Reviewer completion created after worker return acceptance | PASS |
| Roadmap state | Operator-selected KIOD-R8 lane | No standalone roadmap file for this bounded tranche | N/A with reason: operator-selected continuation from KIOD-R7 |
| Registry JSON | N/A | No GC-051 or generated registry JSON mutation is authorized by this governance-checker preflight tranche | BLOCKED with reason: separate registry mutation work order required |
| Registry Markdown | N/A | No corpus or scan registry Markdown mutation is authorized by this governance-checker preflight tranche | BLOCKED with reason: separate registry mutation work order required |
| External evidence digest | N/A | No outside source is absorbed in KIOD-R8 dispatch | N/A with reason: guard-foundation dispatch only |
| System loop interlock | Active session state/front door/handoff | No system-loop registry mutation; reviewer closes material and syncs session separately | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; active handoff | Reviewer/closer performs dedicated session sync after material commit | PASS |
| Source verification | Work order and worker return | Source Verification Block rows | PASS |
| File diff | `git diff --name-status d77d5f52..HEAD` | Changed path list | PASS |
| Tests | `governance.compat.test_source_intake_decision_packet_preflight` | Focused unit tests passed after worker implementation and reviewer repair | PASS |
| Catalog wiring | Four governance command catalogs | Path-string entries for new checker present in all four catalogs | PASS |
| Commit ownership | Git history | Worker no-commit evidence recorded; reviewer owns material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| Worker commit mode | WORKER_MUST_NOT_COMMIT | PASS |
| Dispatch base | d77d5f52 | PASS |
| Public-sync claim | DEFERRED_PRIVATE_ONLY | PASS |

## Claim Boundary

This work order dispatches KIOD-R8 only. It does not certify outside-source
intake, does not complete any CodeGraph or EverOS absorption lane, and does not
claim runtime, package, Web, MCP, CLI, model-router, public-sync, provider-live,
or production-readiness behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: KIOD-R8 is private provenance governance-foundation work. Public-sync is
outside this tranche.
