# CVF GC-018 Baseline - Three-Repo Deferred Semantic Reconciliation T1

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: THREE-REPO-DEFERRED-RECONCILIATION-T1

Dispatch base head: 26221c78cd8a4541ca3b8889e993b1ebebeb234c

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local orchestrator/reviewer

Reviewer owner: Local reviewer/closer

Worker target: INTERNAL_AGENT worker in the shared private workspace

## Purpose

Reconcile the existing 52 deferred decisions across QM, Agentgateway and
DeepSeek Harness into one disjoint, source-preserving semantic-group ledger.
This is decision/evidence accounting only: identify real current CVF consumers,
owners, blockers, duplicates and no-value outcomes before any implementation.

## Decision / Baseline / Proposed Tranche

Authorize one P2 bounded INTERNAL_AGENT accounting tranche with exactly two
outputs and no implementation. Accepted source ledgers already reconcile the
52 inputs; this tranche creates one cross-source semantic decision surface for
Local review.

## Evidence / Verification

Verify all named authority hashes, exact 42+7+3 membership, unique source-
qualified keys, final-disposition totals, exact two-path changed set,
worker-return fast gate and zero provider/network/commit effects.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id THREE-REPO-DEFERRED-RECONCILIATION-T1 --title "Three-Repo Deferred Semantic Reconciliation T1" --date 2026-09-15 --base 26221c78cd8a4541ca3b8889e993b1ebebeb234c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bound the 52-record source set, exact two-path worker manifest, semantic groups, decision taxonomy, evidence rules and no-implementation boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `recordKey`; `semanticGroup`; `currentOwnerDisposition`; `consumerDisposition`; `reconciliationDisposition`; `implementationPriority` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external absorption deferred reconciliation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external absorption deferred reconciliation" --role worker --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE |
| Dispatch impact | no defect-specific expansion; all packet and corpus guards still apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; corpus terminal vocabularies; knowledge-map reconciliation fields; canonical external input type; `ROUTED_SHADOW`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm this source-accounting baseline shape and evidence contract after reading requirements; gates are not first discovery |
| claimBoundary | structural confirmation only; semantic classification remains evidence-bound and Local-reviewed |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| 52 deferred decisions are disjoint | count/reconciliation | `docs/reviews/CVF_THREE_REPO_PILOT_FINAL_ASSESSMENT_AND_RECOVERY_2026-09-15.md` | Three-repository operational state; recovery sequence item 3 | 42 QM + 7 Agentgateway + 3 DSH | active recovery authority | ACCEPT |
| QM contributes 42 | terminal ledger | `docs/reviews/CVF_QM_SOURCE_TERMINAL_ACCOUNTING_2026-09-14.md` | Findings / Position | six unselected adapt candidates plus 36 deferred records | QM R1-R4 audit family | ACCEPT |
| Agentgateway contributes 7 | terminal ledger | `docs/reviews/CVF_AGENTGATEWAY_SOURCE_TERMINAL_ACCOUNTING_2026-09-14.md` | Findings / Position | seven named deferred candidates | Agentgateway terminal accounting | ACCEPT |
| DSH contributes 3 | terminal ledger | `docs/reviews/CVF_DEEPSEEK_HARNESS_SOURCE_TERMINAL_ACCOUNTING_2026-09-15.md` | Findings / Position | DSH-001, DSH-005, DSH-UC-03 | DSH terminal accounting | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for "Three-Repo Deferred Semantic Reconciliation T1" artifacts | both intended output paths returned False before authoring | PASS_NO_COLLISION |
| Token search for "Three-Repo Deferred Semantic Reconciliation T1" (2026-09-15) | `rg -n "THREE-REPO-DEFERRED-RECONCILIATION-T1|deferred semantic reconciliation" docs CVF_SESSION` excluding this authority pair returned no prior packet | PASS_NO_COLLISION |
| Collision decision | new bounded reconciliation identity is distinct from source-terminal accounting | CREATE_NEW_PACKET |

## Source-Intake Decision Packet Fields (trigger stub)

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Negative search performed | exact packet identity and output-path collision checks above |
| Disposition | ADAPT |

## Reconciliation Contract

The input universe is exactly 52 disjoint decision records:

| Source | Record construction | Count |
|---|---|---:|
| QM | 36 existing `DEFER_WITH_TRIGGER` rows plus six unselected `ADAPT_CANDIDATE` rows from R1-R4 | 42 |
| Agentgateway | `ESC-001`, `ESC-002`, `ESC-004`, `ESC-005`, `ESC-006`, `ESC-007`/AGW-UC-01, AGW-UC-02 | 7 |
| DeepSeek Harness | DSH-001, DSH-005, DSH-UC-03 | 3 |
| Total | disjoint source-qualified record keys | 52 |

Every output row must preserve its source-qualified original ID, original
disposition, original trigger, source evidence path, and current Local owner
search. Final reconciliation uses exactly one of:
`NATIVE_CONVERSION_CANDIDATE`, `EVIDENCE_OR_OWNER_BLOCKED`,
`DUPLICATE_OR_ALREADY_OWNED`, `NO_CURRENT_VALUE`, or
`RETAIN_DEFERRED_WITH_TRIGGER`. A conversion candidate additionally requires a
named current CVF owner, named non-test consumer, user/operational outcome,
failure behavior, implementation path, proof path and rollback boundary.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained three-repository external-source decision corpus |
| Upstream or source-mirror disposition | reuse accepted immutable pins and Local ledgers; no mirror refresh or mutation |
| Enumeration or manifest plan | enumerate the exact decision arrays and named terminal rows; construct source-qualified keys |
| Per-file terminal-ledger plan | one output row per retained decision with one final reconciliation disposition |
| Owner or overlap route | source mechanism -> current private-CVF owner search -> Local final review |
| Value-disposition route | conversion candidate, blocked, duplicate/already-owned, no-current-value, or retained trigger |
| Claim boundary | decision reconciliation only; no implementation or complete source-corpus claim |

## Mandatory Blind-Spot Control Block

The pass must inspect all 52 records, not only attractive candidates; challenge
stale no-consumer claims against current non-test workflows; preserve adverse
and failure evidence; and prevent one semantic group from hiding independently
valuable source-specific behavior.

## Corpus Completeness And Report Integrity

- Corpus task class: exact deferred-decision corpus reconciliation.
- Corpus root: four QM audit ledgers plus Agentgateway and DSH terminal rows.
- Snapshot time: 2026-09-15 at dispatch base `26221c78cd8a4541ca3b8889e993b1ebebeb234c`.
- Enumeration command: filesystem-backed direct file reads and JSON array enumeration over named authority paths.
- Manifest artifact or inline manifest: inline 42+7+3 source table above.
- Manifest hash: worker must produce deterministic SHA-256 for its normalized 52-key list.
- Processing ledger artifact or inline ledger: required worker-owned JSON output.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=52; ledger_terminal=52; exclusions=0; unresolved=0; required exact equality 52=42+7+3 with no duplicate source-qualified key.
- Unresolved files: 0 allowed among named authority files; source contradictions must block.
- Declared exclusions: source mirrors beyond cited evidence, rejected/accepted records outside the 52, runtime implementation.
- Unreadable or unsupported files: 0 expected; any nonzero value blocks completion.
- Aggregation check: counts by source, original disposition, semantic group and final disposition must all sum to 52.
- Drift check: recompute all named authority hashes at worker start and return.
- Output traceability: every row cites original authority and current-owner evidence.
- Adversarial verification: test duplicate IDs, missing rows, stale consumer assumptions and conversion claims without failure paths.
- Corpus verdict: PARTIAL
- Verdict reason: this dispatch baseline defines the contract; worker evidence must earn COMPLETE_VERIFIED.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | retained Local ledgers -> semantic grouping -> current owner/consumer verification -> bounded next-action shortlist |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| Owner surface | worker JSON decision ledger; Local completion/recovery accounting after review |
| Disposition | ADAPT retained decisions into an executable Local accounting surface |
| Claim boundary | external evidence is input; Local owns final technical disposition |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_THREE_REPO_PILOT_FINAL_ASSESSMENT_AND_RECOVERY_2026-09-15.md"
}
```


## Claim Boundary

This baseline authorizes one internal, no-commit, two-output accounting pass
over exactly 52 retained decisions. It does not authorize source-mirror edits,
runtime or test changes, implementation, provider/live calls, external agent
research, public sync, deployment, new repositories or program closure.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private recovery accounting; no public artifact or public-sync action.
