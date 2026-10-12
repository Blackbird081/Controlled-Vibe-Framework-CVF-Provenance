# CVF GC-018 Baseline - NCR Agent Handoff Lifecycle

Memory class: governed-dispatch-baseline
docType: baseline
Status: READY
Date: 2026-10-12
Batch ID: CVF-NCR-AGENT-HANDOFF-20261012
Dispatch base head: f0199132050799c293f6b34db8c27b535694baed
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Repair the receiving side of the accepted Working Brief handoff: incoming prompt opens the correct isolated Agent Chat session; minimize/restore preserves that same session and never replays an already delivered prompt; a new explicit handoff is received while a chat is already open. Existing source has two witnessed lifecycle failures. Offline client/session binding only, not AI governance correctness.

## Scope / Target / Owner Boundary

Exactly four worker files: existing `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx` modify, new `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx`/`docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json`/`docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md` create. Wrapper, history store, AgentChat/hook, Home/export, old tests and governed owners are read-only. Existing layout378 lines, cap700; new test<=600; return<=450 lines/64000 bytes; proof<=128000 bytes. One manual60min invocation including reads/tests/gates. Ignored runtime ncr-agent-handoff-worker-20261012 may hold logs. No new helper, schema, session-ID policy, history-limit/retention rule, provider, server/browser, dependency install, new gate, subagent or other production path. Required out-of-scope repair => one consolidated blocked return.

## Design Control Gate

Use actual DashboardLayout, AgentChatWithHistory and persisted useChatHistory at decisive event/session boundaries. Preserve normal navigation, history and close behavior. Chat leaf may be a transparent synthetic recorder to isolate initialPrompt/message callbacks and minimize/close; disclose it. Include one real AgentChat/hook receiving case with in-process deterministic provider-adapter stub or no-key presentation; retain shared fetch/network denial. Transport mocks prove client wiring only; no AI governance decisions, full-mode certification, real provider/HTTP/backend cancellation or browser claim. No source change by dispatcher.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: incoming event mount/minimize route | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | actual DashboardLayout event and modal render | ACCEPT |
| EXISTS: prompt session binds on mount | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | AgentChatWithHistory/useChatHistory | ACCEPT |
| EXISTS: deferred once-send cleanup controls | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | useAgentChat timer/ref and tests | ACCEPT |
| EXISTS: two scoped UI lifecycle failures | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | admissionWitness | admissionWitness | actual shell/wrapper/history with disclosed Chat recorder | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | previous bounded dispatch; WORKER_MUST_NOT_COMMIT; INTERNAL_AGENT; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; SECTION_GROUPS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of selected packet structure; not a dispatch or implementation proof |
| claimBoundary | targeted current checker constants/required sections and ready-state predicates read; not an all-lines reading claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-AGENT-HANDOFF-20261012 --title "NCR Agent Handoff Lifecycle" --date 2026-10-12 --base f0199132050799c293f6b34db8c27b535694baed --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_DRAFT_EXPORT_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-agent-handoff-lifecycle --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: prior verified ready role-contract shape, four paths and witnessed receiving lifecycle contract; no copied closure |
| checkerReadAheadConfirmation | current dispatch/closeability/scaffold/read-ahead constants; retained verified role/trace/ledger/probe bindings, scoped read only |
| docOnlyNewFields | source witness and consumer repair contract; no new schema |
| claimBoundary | packet preparation and scoped source witness only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order" --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated. This query does not prove absence of all applicable defects; refresh the final task class at release if classification changes.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT orchestrator/dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-agent-handoff-dispatch-20261012 |
| Working directory | repository root and installed Web package |
| Command or tool surface | targeted source/owner reads, actual scaffold/ADIF, bounded two-case inspection witness, source pins, dispatch/gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator next following manual worker role assignment; existing outcome-bound lifecycle |
| Before status evidence | HEAD f0199132050799c293f6b34db8c27b535694baed; clean/staged empty; temporary Local witness removed |
| After status evidence | exact11 dispatch material then dedicated exact6 continuity; worker not started |
| Diff evidence | git diff --check and exact manifests |
| Approval boundary | manual shared-workspace worker; offline client source only |
| Claim boundary | two synthetic leaf-boundary failures witnessed; no provider or AI governance claim |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-agent-handoff-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required before commit |
| Deletion or rename disposition | N/A with reason: none |

## Epistemic Process Block

Expected Result / Prediction: each explicit incoming handoff owns one fresh ready chat; shell minimize/restore preserves it, while new handoff changes session.
Evidence Comparison: existing mount controls consumed; distinct two-case shell/history witness initial A passes then desired2/2 fail (replay A, lost B); source/log in dispatch JSON. No production mutation by dispatcher.
Contradiction Or Gap Disposition: concrete receiving-session lifecycle defect, distinct from accepted prompt emission; repair layout only or consolidated blocker.
Claim Update: bounded offline client repair selected; worker implementation and independent Local review pending.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch and offline proof only; no publication grant.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local dispatch raw authority projection then exact6 continuity. Worker cannot edit protected paths.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: next under standing manual worker/Local orchestrator-reviewer roles,2026-10-12.
Rollback boundary: exact11 dispatch and exact6 continuity, prior accepted worker/evidence and20 observations retained; no guard/hook changes.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: selected roadmap/index/inventory, new packet/witness and raw authority projections bind one dispatch; dedicated continuity binds actual material SHA.
Rollback boundary: exact11 dispatch below.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`
- `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`
- `docs/roadmaps/README.md`
- `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`
- `.gitattributes`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: packet/witness authored before commit; other material paths tracked. Existing worker layout tracked; three future worker outputs absent.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` |
| Chain map route | Local Home visible recovered-handoff lifecycle coverage gap -> existing component -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing UI lifecycle/source-fidelity/closure owners |
| Disposition | internal existing product composition proof; no external research |
| Claim boundary | Local private source verification and final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named consumer/test evidence only; no repository/corpus scan.

## Knowledge System Applicability

NOT_APPLICABLE_WITH_REASON: named Home/DynamicForm source and fixture evidence only; no corpus rescan or semantic knowledge-map/retrieval production.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: named UI composition proof, no rescan/intake.

## Claim Boundary

Incoming client/session lifecycle repair only. Accepted export/emission evidence consumed; no whole NCR/full/app-builder/wizard/browser/backend/live/AI-governance/public/deploy/model-winner claim. Provider effects remain forbidden. Stop after selected outcome.

## Decision / Proposed Tranche

Finite incoming handoff/session repair, four paths, one offline60min manual worker, no auto successor. Paired order `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`; requested Sonnet5.5 high metadata only;20 prior observations unchanged.

## Evidence / Verification

`docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` binds source hashes and actual Local inspection witness: initial A control PASS, desired2/2 FAIL. Synthetic Chat leaf, no AI/governance/transport claim; temporary source removed. Worker produces independently authored repair/regressions and actual final gates; Local review later.

## Finding-To-Governance Learning Disposition

Defect class: ORCHESTRATOR_PACKET_GAP
Learning lane: GOVERNANCE_CONTROL_PLANE
Disposition: RULE_EXISTS - first Local authoring preflight exposed envelope/fence/baseline-shape omissions and UI session-binding risk-word ambiguity; one consolidated packet correction, failure preserved in dispatch JSON.
Next action: apply existing checker literals and finite source contract before transfer; no new checker, worker quiz or scope.
