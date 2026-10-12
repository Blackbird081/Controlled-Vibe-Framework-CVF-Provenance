# CVF GC-018 Baseline - NCR Chat History Consistency

Memory class: governed-dispatch-baseline
docType: baseline
Status: READY
Date: 2026-10-12
Batch ID: CVF-NCR-CHAT-HISTORY-20261012
Dispatch base head: 4aabff8808e150f76c371dc7e087b5dad6f186ba
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Make the existing Agent Chat history usable in one open panel: new sessions and message/title counts appear immediately, selecting history shows its own messages, deleting or clearing history removes that data from both chat and persistence without later resurrection. Two actual wrapper/sidebar/history source witnesses fail. Offline client state and synthetic persistence only; no AI governance behavior claim.

## Scope / Target / Owner Boundary

Exactly five files: modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.tsx` and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/chat-history.tsx`; create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatHistoryConsistency.test.tsx`, `docs/reviews/evidence/ncr-chat-history-worker-20261012.json`, `docs/reviews/CVF_NCR_CHAT_HISTORY_WORKER_RETURN_2026-10-12.md`. Actual wrapper145/history289 lines, cap700 each; new test<=650; return<=450 lines/64000 bytes; proof<=128000 bytes. One manual60min invocation includes startup, reads, scaffold, tests and final gates. Ignored .cvf/runtime/ncr-chat-history-worker-20261012 may hold logs. Dashboard layout, AgentChat/hook, Home/export, old tests, checkers/hooks/owners/model ledger/continuity are read-only. No extra helper file, global store/service/event bus, cross-tab sync, schema/migration/import/retention redesign, ID policy, dependencies, provider/server/browser/subagent/public effects. Necessary extra path/split => one consolidated blocker.

## Design Control Gate

Use real AgentChatWithHistory, ChatHistorySidebar and useChatHistory together; do not mock the sidebar or hook for decisive history assertions. One authoritative state for this mounted consumer and storage writer; controlled props or existing callbacks are feasible. Preserve standalone sidebar API and standalone hook callers. Chat leaf may be a disclosed transparent recorder for stored messages/later callbacks. Include at least one real AgentChat/useAgentChat seam using deterministic in-process adapter or no-key presentation with fetch denial retained. Fixture transport proves UI wiring only. No AI governance decision/full-mode/browser/backend-abort claim. No dispatcher product repair.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: independent wrapper/sidebar snapshots | `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | AgentChatWithHistory and ChatHistorySidebar/useChatHistory | ACCEPT |
| EXISTS: stale list and deleted-session resurrection | `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json` | admissionWitness | admissionWitness | actual wrapper/sidebar/hook with Chat leaf recorder | ACCEPT |
| EXISTS: accepted handoff boundary retained | docs/reviews/CVF_NCR_AGENT_HANDOFF_COMPLETION_2026-10-12.md | Claim Boundary | bounded receiving lifecycle | Local technical disposition | ACCEPT |

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
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-CHAT-HISTORY-20261012 --title "NCR Chat History Consistency" --date 2026-10-12 --base 4aabff8808e150f76c371dc7e087b5dad6f186ba --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_AGENT_HANDOFF_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-chat-history-consistency --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: prior verified ready role-contract shape, five paths and witnessed history consistency contract; no copied closure |
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
| Session or invocation | ncr-chat-history-dispatch-20261012 |
| Working directory | repository root and installed Web package |
| Command or tool surface | targeted source/owner/constants reads, actual scaffold/ADIF, bounded admission witness, raw/HEAD pins, dispatch/gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_CHAT_HISTORY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_CHAT_HISTORY_2026-10-12.md`; `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator next under standing manual worker/Local orchestration; outcome-bound existing NCR client maintenance |
| Before status evidence | 4aabff8808e150f76c371dc7e087b5dad6f186ba; clean/staged empty before temporary witness; no production mutation |
| After status evidence | exact11 dispatch material then exact6 continuity; worker not started |
| Diff evidence | git diff --check and exact manifests |
| Approval boundary | one manual shared-workspace worker, offline synthetic data only |
| Claim boundary | actual wrapper/sidebar/history with Chat leaf recorder; no provider or whole NCR exit |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-chat-history-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_CHAT_HISTORY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_CHAT_HISTORY_2026-10-12.md`; `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_CHAT_HISTORY_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_CHAT_HISTORY_2026-10-12.md`; `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required before commit |
| Deletion or rename disposition | N/A with reason: none |

## Epistemic Process Block

Expected Result / Prediction: actual sidebar/chat and persistence represent one current consumer state.
Evidence Comparison: two final source assertions FAIL after seeded controls PASS; Local unsupported matcher and weak title-count oracle corrected, original attempts retained in dispatch JSON.
Contradiction Or Gap Disposition: concrete split-snapshot defect; repair existing wrapper/history only.
Claim Update: bounded offline history repair selected; implementation/independent Local review pending.

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
Rollback boundary: exact11 dispatch and exact6 continuity, prior accepted worker/evidence and21 observations retained; no guard/hook changes.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: selected roadmap/index/inventory, new packet/witness and raw authority projections bind one dispatch; dedicated continuity binds actual SHA.
Rollback boundary: exact11 dispatch.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_CHAT_HISTORY_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_CHAT_HISTORY_2026-10-12.md`
- `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json`
- `docs/roadmaps/README.md`
- `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`
- `.gitattributes`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: packet/witness authored before commit; other material tracked; two worker sources tracked, three future outputs absent.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json` |
| Chain map route | Local composed sidebar/chat history consistency repair -> existing component -> independent Local review |
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

NOT_APPLICABLE_WITH_REASON: named dashboard/chat source and fixture evidence only; no corpus rescan or semantic knowledge-map/retrieval production.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: named UI composition proof, no rescan/intake.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | existing wrapper/sidebar/history and Local worker | five paths, synthetic offline client repair, no commit/effects | dispatch witness and source pins; final review pending | N/A with reason: shared private workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no external consumer selected | no CLI/MCP/runtime effect authority | no external route in this finite outcome | deferred adapter; no implementation selected | DEFERRED_WITH_REASON |

## Claim Boundary

Finite offline chat history consistency only. Incoming lifecycle evidence consumed; no whole NCR/full/browser/backend/provider/AI-governance/R3/R4/public/deploy/model-ranking acceptance. Stop selected outcome.

## Evidence

Paired order contains fixed acceptance ledger, exact paths/source pins and final gates. Source witness in `docs/reviews/evidence/ncr-chat-history-dispatch-20261012.json`; no readiness claim from fixtures.

## Decision / Proposed Tranche

Five outputs, one manual60min offline worker after bound committed release. Paired `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_CHAT_HISTORY_2026-10-12.md`;21 observations unchanged; no automatic successor.
