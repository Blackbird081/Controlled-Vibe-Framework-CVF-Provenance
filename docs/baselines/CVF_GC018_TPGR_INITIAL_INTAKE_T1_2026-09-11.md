# CVF GC-018 - TPGR Initial Intake Admission

Memory class: governed-dispatch-baseline
docType: baseline
Status: CLOSED_PASS_BOUNDED
Date: 2026-09-11
Batch ID: TPGR-INITIAL-INTAKE-T1
dispatchBaseHead: 00f8e1bd1
Commit mode: WORKER_MUST_NOT_COMMIT
Decision owner: operator agreement of 2026-09-11
Reviewer owner: independent Local reviewer
Worker target: operator-selected internal worker

## Purpose

Authorize one bounded internal maintenance task to add an explicit initial-acquisition/survey stage to existing TPGR metadata routing. The current router rejects absent full-read evidence for selected absorption and absent prior receipt for corpus intake; those rules remain unchanged for ordinary tasks.

## Decision / Baseline

Release only `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_INITIAL_INTAKE_T1_2026-09-11.md` and its six-path implementation manifest. The worker implements and returns uncommitted evidence; Local reviewer independently reviews before any pilot source work. This baseline does not change machine behavior by itself.

## Operator Authorization

Operator explicitly agreed to narrowly supplement initial-intake admission without relaxing evidence or opening runtime authority. Existing role split is retained: Local orchestrator/reviewer, internal worker, operator as cross-workspace relay only.

## Scope / Target / Owner Boundary

Existing TPGR router/schema/standard and focused router/checker tests plus one worker return. Only one active-window registration for the existing TPGR standard is authorized; no hook, catalog, public or runtime mutation. Detailed closed additive contract and test matrix are in the paired work order. No source acquisition in this tranche.

## Acceptance Criteria

Additive opt-in stage; truthful missing initial evidence; explicit planned receipt not prior evidence; no absorption acceptance; P3 minimum and full gates; strict malformed/risky-input rejection; old receipt equivalence; focused and worker-return gates pass; exact six-path uncommitted delta.

## Evidence / Verification

Source rows below establish current rejection, closed sourceEvidence shape, tests and independent review requirement. Read-only diagnostics on 2026-09-11 returned REJECTED_ESCALATED for both full-read=false bounded absorption and receipt=null corpus absorption. That is metadata behavior only, not AI runtime proof. Worker repeats before editing and supplies tests of the additive contract.

## Non-Goals And Stop Conditions

No source acquisition or survey, runtime implementation, provider/live/API/network, dependency installation, credential use, automatic pilot continuation, staging or worker commit. Stop for source contradiction, forbidden-path need or impossible in-scope gate.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Current selected-file route rejects missing full-read confirmation | LOCAL_SOURCE | governance/compat/route_task_governance.py | route_manifest contradiction checks | route_manifest | TPGR router | ACCEPT |
| Current corpus route requires prior receipt | LOCAL_SOURCE | governance/compat/route_task_governance.py | route_manifest contradiction checks | corpusReceiptRef | TPGR router | ACCEPT |
| Source evidence currently has three closed keys | LOCAL_SCHEMA | governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json | sourceEvidence | selectedFilesFullyRead | manifest v1 | ACCEPT |
| Existing regressions preserve selected-read and prior-receipt rules | LOCAL_TEST | governance/compat/test_route_task_governance.py | selected and corpus tests | test_corpus_requires_receipt_and_selects_accounting | deterministic router tests | ACCEPT |
| Work-order activation uses router | LOCAL_SOURCE | governance/compat/check_task_governance_route.py | evaluate | route_manifest | changed active work-order checker | ACCEPT |
| Initial survey precedes selected conversion | LOCAL_STANDARD | docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md | Two-Step Operating Agreement And Proportional Depth | Initial survey for every acquired repository | method 1.2 | ACCEPT |
| Current standard requires independent review of router/schema changes | LOCAL_STANDARD | docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md | Rollback | independent review | TPGR standard | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_task_governance_route.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_worker_return_quality_gate.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_machine_closure_package.py; governance/compat/check_session_mode_consistency.py |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Required Artifact Manifest; WORKER_MUST_NOT_COMMIT; sourceEvidence; closeabilityContractVersion; Self-declared worker-return artifact; Machine Closure Package; Closure item; Required artifact/path; Machine-readable evidence; Final status; Acceptance Receipt Assertion Matrix |
| gateRunPurpose | confirmation of source-verified dispatch and output contracts, not first discovery |
| claimBoundary | dispatch read-ahead does not certify worker implementation or source value |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id TPGR-INITIAL-INTAKE-T1 --title "Initial Intake Admission" --date 2026-09-11 --base 00f8e1bd1 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout |
| generatedProfile | protected-governance-path plus internal no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added closed additive admission contract, negative tests, exact six-path worker scope and independent reviewer boundary; reused existing closeability graph shape. |
| checkerReadAheadConfirmation | Listed checker constants, source keys, routing rejection branches and source-backed tests read before authoring. |
| docOnlyNewFields | initialIntakeAdmission proposed contract; plannedReceiptPath; admission claim boundary |
| claimBoundary | authoring provenance only; proposed machine fields are not currently implemented |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-machine-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class governance-machine-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`.

Returned defect count: 0. Returned defects: NONE_RETURNED. Disclosed defectIds: none.
Dispatch impact: no matching active resolver item; all named guard obligations remain.

## Current Runtime Freshness Verification

Current local source inspected on 2026-09-11: route_manifest in governance/compat/route_task_governance.py rejects missing selected-file full-read confirmation and missing corpusReceiptRef. Source/schema/tests were read at 00f8e1bd1. This is a metadata predicate observation, not an absence claim about a runtime capability. The two deterministic rejection diagnostics are recorded in Evidence / Verification or the paired baseline.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned baseline and work-order paths | Test-Path on each exact path returned False before authoring | NEW_PATHS_CONFIRMED |
| Packet identifier | search roots: docs/work_orders and docs/baselines; command: rg -n -g '*.md' --fixed-strings 'TPGR-INITIAL-INTAKE-T1' docs/work_orders docs/baselines; query TPGR-INITIAL-INTAKE-T1; zero matches, exit 1 before authoring | NO_COLLISION |
| Existing owner | route_task_governance.py, manifest schema and TPGR standard already own routing | ENRICH_EXISTING_OWNER |

## Core Guard Self-Protection Authorization

Operator authorization: 2026-09-11 explicit agreement to supplement initial-intake admission without weakening evidence or opening runtime authority.

Authorized guard-maintenance scope: amend only the existing TPGR source-evidence admission contract, manifest schema, router and focused tests in the worker manifest. Preserve existing hook/catalog semantics, all legacy gates, old-manifest behavior and unrelated value-admission logic. Worker return must repeat this authorization for its changed set.

Protected worker paths:
- governance/compat/route_task_governance.py
- governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json
- governance/compat/test_route_task_governance.py
- governance/compat/test_check_task_governance_route.py
Dispatcher-owned protected path:
- governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json (single binding-reference entry for TPGR standard, added before dispatch; worker read-only)

Canonical standard owner:
- docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md

Rollback boundary: remove only the newly introduced additive admission feature and its tests if rejected; preserve all historical work and legacy rejection behavior. Do not reset, restore unrelated files, change hooks or reinterpret old receipts.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | TPGR manifest/router and this internal work order | deterministic admission metadata only; independent review, no worker commit | current source and required regression proof | internal direct Python caller, not runtime interception | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no new external adapter | advisory research cannot activate initial intake or accept values | operator relay is content transport only | no CLI/MCP/provider adapter implementation authorized | N/A_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator method requirement -> existing TPGR metadata owner -> internal implementation review |
| Matching local-view guard | governance/compat/check_task_governance_route.py |
| Owner surface | existing TPGR standard/schema/router |
| Disposition | ADAPT the operator-approved admission requirement; no source-value acceptance |
| Claim boundary | routing maintenance only, no source acquisition or absorption execution |

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: this packet changes a routing metadata owner; it neither acquires nor absorbs an external source. Future intake tasks need their own entry control.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: no repository survey or source-value decision is performed in this maintenance tranche.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus processed; deterministic routing metadata and tests only.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy source payload is inspected or promoted.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/reviewer |
| Provider or surface | local VS Code workspace |
| Session or invocation | TPGR-INITIAL-INTAKE-T1 dispatch, 2026-09-11 |
| Working directory | repository root |
| Command or tool surface | read-only Git/search, deterministic router diagnostics, apply_patch |
| Target paths | paired baseline, work order and one active-window registration |
| Allowed scope source | operator agreement of 2026-09-11 |
| Before status evidence | clean worktree at 00f8e1bd1 before dispatch authoring; empty staging |
| After status evidence | two dispatcher-owned packets plus one bounded active-window registration; no worker implementation performed |
| Diff evidence | git diff --name-status; git status --short |
| Approval boundary | exact admission amendment worker dispatch only |
| Claim boundary | no implemented behavior or pilot survey claim |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | tpgr-initial-intake-t1-dispatch |
| Expected manifest | paired baseline, work order and one active-window registration |
| Actual changed set | paired baseline, work order and one active-window registration before separate continuity |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic admission metadata implementation dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement claimed |
| receiptEvidence | N/A with reason: routing diagnostics only, not runtime receipts |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: authoring and source inspection only |
| invocationBoundary | internal workspace; no provider or external execution |
| interceptionBoundary | no interception, wrapper or sandbox claim |
| claimLanguage | proposed bounded admission contract, implementation pending |
| forbiddenExpansion | no runtime, provider, public, package, MCP or pilot execution |

## Claim Boundary

This is internal deterministic governance-metadata maintenance, not AI governance runtime proof. No source repository acquisition, research, source-value disposition, corpus completion, implementation of a repo candidate, provider/live call, credential access, package install, CLI/MCP adapter, public sync, push or deployment is authorized. Pilot source acquisition remains outside this packet's authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private internal admission implementation and review; no public export.

## Reviewer Closure Decision

Local reviewer accepts the bounded implementation on 2026-09-11. Reviewer verdict: REVIEWER_ACCEPTED_BOUNDED. The original worker return and its failed aggregate are historical evidence, not the current gate verdict. Four consolidated findings are resolved: planned output is within declared path families; whitespace-only prior references reject; old-router full-output comparisons and actual checker.evaluate integration replace self-comparison; ancestry and gate reporting are corrected.

Reviewer reused the returned 70/70 focused tests and inspected the corrected contract, schema, authority boundary, tests and exact six-path delta. Independent targeted probes rejected out-of-family output and whitespace references and accepted a valid initial-only declaration without absorption authority. No broad duplicate test run or provider call was needed. The dispatch-owned mode defect was corrected separately at c5cf9e480. Worker-return fast and reviewer-fast then passed, including 68/68 reviewer checks. These are deterministic metadata checks, not runtime governance proof.

closureBaseHead: c5cf9e480
executionBaseHead retained: 9066340e776b57072123b425038bf13470371849
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION
successorTrancheOpened: NO

Material commit plan: exactly six worker paths plus the paired work order, baseline closure conversion and continuation-required completion companion. Separate continuity projection follows; no mixed material/session commit. The completion companion is required by check_continuation_chain.py Rule B. No registry mutation, source acquisition, pilot dispatch, external relay, runtime, live call, public sync or push.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_INITIAL_INTAKE_T1_2026-09-11.md | Status: CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_WORKER_RETURN_2026-09-11.md | Reviewer Closure Decision: REVIEWER_ACCEPTED_BOUNDED | PASS |
| Roadmap state | standalone work order; no dedicated roadmap closure | no roadmap transition | N/A with reason: standalone maintenance |
| Registry JSON | existing TPGR registry and active-window entry | no new corpus processed or registry semantics changed; existing registration retained | PASS |
| Registry Markdown | existing TPGR standard | additive initial-only contract aligned with schema/router; no corpus entry required | PASS |
| External evidence digest | no external evidence consumed in implementation | local source and returned test evidence only | N/A with reason: no external source processing |
| System loop interlock | initialIntakeAdmission contract | absorptionAcceptanceAuthorized=false; separate reviewed work order required for next stage | PASS |
| Session continuity | CVF_SESSION_MEMORY.md; AGENT_HANDOFF_V60_2026-09-08.md | mode repair c5cf9e480; post-material projection separately owned by Local closer | PASS - prerequisite fixed; final projection follows material commit |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| initial-only | docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_WORKER_RETURN_2026-09-11.md | absorptionAcceptanceAuthorized | false | false in targeted valid probe and returned tests | PASS |
| unsafe-output | docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_WORKER_RETURN_2026-09-11.md | receiptStatus | REJECTED_ESCALATED | REJECTED_ESCALATED in targeted probe | PASS |
| blank-prior | docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_WORKER_RETURN_2026-09-11.md | receiptStatus | REJECTED_ESCALATED | REJECTED_ESCALATED in targeted probe | PASS |

These assertion rows refer to deterministic test/probe outcomes described in the review, not durable runtime receipts.
