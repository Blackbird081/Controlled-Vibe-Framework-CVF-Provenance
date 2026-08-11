# CVF Agent Instruction Carrier Routing Index

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-08-11

Batch ID: ACRC-T2B

**Applies to:** every agent resolving a governance rule that used to live as a
full section inside a root instruction carrier.

EPISTEMIC_PROCESS_NA_WITH_REASON: routing index - it maps existing canonical
owners and does not compare evidence or update an empirical claim.

## Purpose

Carry the complete binding map for the three CVF instruction carriers after
T2B compaction. The compact carriers keep the routing spine and the direct
machine literals; this index keeps the full per-heading owner map so no
canonical rule becomes unreachable when a carrier stops restating it.

Compaction moved prose. It did not repeal a rule. Every row below still
governs; the Canonical owner column is where the binding text now lives.

## Scope / Applies To

In scope: root `AGENTS.md`, provider-local `CLAUDE.md`, the downstream
template `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`,
their three dated preimage archives, and the approved T2B budgets.

Out of scope: existing downstream repositories, public-sync clones, runtime or
provider behavior, and session history.

## Carrier Budget

| Surface | carrierBudget lines | carrierBudget bytes |
|---|---:|---:|
| `AGENTS.md` | 220 | 20480 |
| `CLAUDE.md` (`NOT_CVF_SOURCE`) | 160 | 16384 |
| `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | 180 | 20480 |
| `docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md` | 300 | 32768 |

Machine owner of these budgets:
`governance/compat/check_agent_instruction_carriers.py`.

## Preimage Archive Binding

Archives are historical evidence and `NOT_ACTIVE_AUTHORITY`. They record the
exact pre-compaction bytes and must never be cited as current authority.

| Source family | Archive path | preimageSha256 |
|---|---|---|
| AGENTS | `docs/reference/archive/AGENTS_FULL_PRE_T2B_2026-08-11.md` | `605b32534c7898117f0cbfd7747253243c342cf1619df02e96a4691507573855` |
| CLAUDE | `docs/reference/archive/CLAUDE_FULL_PRE_T2B_2026-08-11.md` | `5d918333045b248beb1d3acbe9fb984da45298cf5348abe0a107593ee0c8c7c1` |
| downstream template | `docs/reference/archive/CVF_DOWNSTREAM_AGENTS_TEMPLATE_FULL_PRE_T2B_2026-08-11.md` | `7f545fa243754cd3066f3b4264959f4b7f9bd3fa2f348bd1b99cc21483e34a74` |

## Binding Class Vocabulary

- `ROUTE`: the compact carrier may point to the canonical owner; no literal is
  required in the carrier itself.
- `RETAIN_LITERAL`: a machine reader requires the named marker directly inside
  the carrier; removing it breaks an existing checker.
- `ROUTE_AND_RETAIN_LITERAL`: both apply.

## AGENTS Heading Routing Map

All 38 pre-compaction `AGENTS.md` level-two headings, each with its canonical
owner and bindingClass.

| Source heading | Canonical owner | bindingClass |
|---|---|---|
| Session Memory Front Door | `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`; `CVF_SESSION_MEMORY.md` | ROUTE_AND_RETAIN_LITERAL |
| Mandatory Startup Acknowledgment | `CVF_SESSION_MEMORY.md` plus the compact AGENTS startup contract | ROUTE_AND_RETAIN_LITERAL |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ROUTE |
| Mandatory Provider-Specific Agent Memory Boundary | `governance/compat/check_agent_packet_authority_and_encoding.py` | ROUTE |
| Mandatory F-1 Diminishing Returns Stop Rule | `docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md` | ROUTE |
| Mandatory Public Export Disposition Guard | `docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | ROUTE_AND_RETAIN_LITERAL |
| Critical Repository Boundary | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | ROUTE |
| UI / Web Design Contract | `DESIGN.md` | ROUTE |
| Mandatory Live Governance Proof | `scripts/run_cvf_release_gate_bundle.py` | ROUTE |
| Mandatory Live Run Diagnostics | `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | ROUTE |
| Mandatory ADIF Defect Registry Disclosure | `governance/compat/check_adif_defect_registry_disclosure.py` | ROUTE |
| Mandatory Value-Parked Lane Reopen Discipline | `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` | ROUTE |
| Mandatory Work Order Source Verification | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ROUTE |
| Governed Artifact Literal-Format Gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | ROUTE |
| Mandatory Work Order Closure Quality Gate | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | ROUTE |
| Mandatory Roadmap Closure Freshness Guard | `docs/reference/roadmap_closure_freshness/README.md` | ROUTE |
| Mandatory Work Order Dependency Release Evidence | `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md` | ROUTE |
| Mandatory Governed File Maintainability Planning | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | ROUTE |
| Mandatory Text Encoding And Symbol Discipline | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | ROUTE |
| Mandatory JSON Generated Aggregate Discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | ROUTE |
| Mandatory Agent Autorun Workflow Control | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | ROUTE |
| Mandatory Agent Handoff Boundary Contract Guard | `docs/reference/agent_handoff/README.md` | ROUTE |
| Mandatory Agent Interaction Workspace Design Boundary | `docs/reference/agent_workspace/README.md` | ROUTE |
| Mandatory Agent Workspace State Generated Aggregate Guard | `governance/compat/check_agent_workspace_state.py` | RETAIN_LITERAL |
| Mandatory Agent Workspace Skeleton Guard | `governance/compat/check_agent_workspace_skeleton.py` | RETAIN_LITERAL |
| Mandatory Agent Workspace Runtime Boundary Guard | `governance/compat/check_agent_workspace_runtime_boundary.py` | RETAIN_LITERAL |
| Mandatory IDE Extension Multi-Provider Execution Log Guard | `docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md` | ROUTE |
| Mandatory Finding-To-Governance Learning Trigger Guard | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | ROUTE |
| Mandatory Learning Signal Intake Bridge | `docs/reference/CVF_LEARNING_SIGNAL_INTAKE_BRIDGE_STANDARD_2026-05-29.md` | ROUTE |
| Mandatory External Repository Absorption Entry Rule | `governance/compat/check_absorption_blindspot_control_presence.py` | ROUTE |
| Mandatory Knowledge Absorption Blind-Spot Prevention | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | ROUTE |
| Mandatory Corpus Completeness And Report Integrity | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | ROUTE_AND_RETAIN_LITERAL |
| Mandatory Corpus-To-Knowledge-Map Reconciliation | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | ROUTE_AND_RETAIN_LITERAL |
| Mandatory Corpus Intelligence Classification | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ROUTE |
| Mandatory Corpus Search And Filter Readiness | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ROUTE |
| Mandatory Corpus Scan Registry Consultation | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | ROUTE |
| Mandatory System Loop Interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | ROUTE |
| Latest Closed Continuation Roadmap | `CVF_SESSION/ACTIVE_SESSION_STATE.json` next-move fields | ROUTE |

## Direct Machine Reader Tokens

Each token below is required inside the named carrier by an existing checker.
Removing one breaks that checker; they are not decorative prose.

| Reader | Carrier | Required literal |
|---|---|---|
| `governance/compat/check_active_session_state.py` | `AGENTS.md`; `CLAUDE.md` (`NOT_CVF_SOURCE`) | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| `governance/compat/check_agent_workspace_state.py` | `AGENTS.md` | `Mandatory Agent Workspace State Generated Aggregate Guard`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `governance/compat/check_agent_workspace_state.py`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json` |
| `governance/compat/check_agent_workspace_skeleton.py` | `AGENTS.md` | `Mandatory Agent Workspace Skeleton Guard`; `CVF_SESSION/agent_workspace/workspace/README.md`; `governance/compat/check_agent_workspace_skeleton.py` |
| `governance/compat/check_agent_workspace_runtime_boundary.py` | `AGENTS.md` | `Mandatory Agent Workspace Runtime Boundary Guard`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`; `CVF_SESSION/agent_workspace/runtime_queue/README.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`; `governance/compat/check_agent_workspace_runtime_boundary.py` |
| `governance/compat/check_public_export_disposition.py` | `AGENTS.md` | `governance/compat/check_public_export_disposition.py` |
| `governance/compat/check_corpus_completeness_report_integrity.py` | `AGENTS.md`; `CLAUDE.md` (`NOT_CVF_SOURCE`) | `governance/compat/check_corpus_completeness_report_integrity.py` |
| `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | `AGENTS.md`; `CLAUDE.md` (`NOT_CVF_SOURCE`) | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| `governance/compat/check_agent_packet_authority_and_encoding.py` | `CLAUDE.md` (`NOT_CVF_SOURCE`) | `NOT_CVF_SOURCE` boundary |
| `governance/compat/check_index_classification.py` | `CLAUDE.md` (`NOT_CVF_SOURCE`) | provider-private classification |
| `scripts/check_cvf_workspace_agent_enforcement.ps1` | downstream template | seven role tokens; phase chain; rehydration tokens |
| `scripts/test_cvf_golden_downstream_bootstrap.ps1` | downstream template | one governance-latency heading; five literal phrases |
| `scripts/new-cvf-workspace.ps1` | downstream template | `{{...}}` substitution tokens |

## Downstream Template Literal Contract

The generated downstream carrier must retain these exact literals:

- phase chain `INTAKE -> DESIGN -> SPEC -> WORK_ORDER -> BUILD -> REVIEW -> FREEZE`;
- roles `ORCHESTRATOR`, `SPEC_AUTHOR`, `WORK_ORDER_AUTHOR`,
  `IMPLEMENTATION_WORKER`, `REVIEWER`, `CLOSER`, `SESSION_SYNC_STEWARD`;
- rehydration `Mandatory Continuity Rehydration`, `new or resumed chat/session`,
  `new tranche or work order`, `Do not rely on chat history`,
  `BLOCKED_CONTINUITY_DRIFT`;
- latency `### Governance Latency and Approval Continuity`,
  `dependent same-scope repairs`, `real boundary change`,
  `consolidated review of relevant records`, `REVIEW_COST_ESCALATION_REQUIRED`,
  `avoidable operator wait`.

## Read Budget Discipline

The compact carriers must not reintroduce unconditional full-state or
full-history read mandates. Continuity reads stay progressive: bootstrap read
model first, then the compact front door and active handoff, then only the
current-authority paths those surfaces name. The full state registry is a
targeted lookup for a missing or contradictory current fact.

Machine owner of that wording rule:
`governance/compat/active_continuity_read_budget.py`, enforced through
`governance/compat/check_active_session_state.py`.

## Claim Boundary

This index is a routing and binding map only. It does not create new
governance semantics, does not supersede any canonical standard or machine
checker, and does not itself enforce a rule. It makes no runtime, provider,
live, downstream-migration, deployment, public-sync, or production claim. The
archives it names are historical evidence, never current authority.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | implementation worker |
| Provider or surface | local private CVF Core workspace |
| Session or invocation | ACRC-T2B instruction-carrier compaction, 2026-08-11 |
| Working directory | repository root at `bc5be598e82a812df4689e5119721159029a88a8` |
| Command or tool surface | progressive reads, heading extraction, checker constant resolution, raw SHA-256, governed patch authoring |
| Target paths | three carriers, three archives, this routing index, new checker/tests, five gate bindings |
| Allowed scope source | ACRC-T2B Work Order V2 exact-15 manifest |
| Before status evidence | clean worktree at `bc5be598e`; staged zero |
| After status evidence | exact-15 uncommitted worker changed set |
| Diff evidence | `git diff --name-status` over the exact-15 manifest |
| Approval boundary | exact-15 compaction and machine enforcement only |
| Claim boundary | no T3, downstream mutation, external call, commit, or push |
| Agent type | implementation worker |
| Invocation ID | `active-continuity-read-cost-t2b-worker-v2-2026-08-11` |
| Expected manifest | exact 15 Work Order V2 paths |
| Actual changed set | same exact 15 paths, uncommitted |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this batch |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance instruction routing. Public projection requires a
separate authorized public-sync batch.
