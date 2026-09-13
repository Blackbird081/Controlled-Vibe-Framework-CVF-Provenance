# CVF GC-018 - Umbrella Seed And Historical Obligation Reconciliation

Memory class: governed-dispatch-baseline
docType: baseline
Status: APPROVED_FOR_EXECUTION
Date: 2026-09-13
Batch ID: UMBRELLA-SEED-RECONCILIATION-T1
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: dfae47c8c0feaf7e0508d08f4d02438a41ef98c6

## Purpose

Release docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_2026-09-13.md for local historical metadata joins after the original input was recovered. Operator requested autonomous continuation of the broader program.

## Decision / Baseline

APPROVED_FOR_EXECUTION after pre-dispatch PASS and dedicated continuity activation. No successor to the stopped three-repo recovery chain; no source scan.

## Core Guard Self-Protection Authorization

Operator authorization: explicit instruction to record the larger program and
issue the next worker packet; standing autonomous orchestrator/reviewer mandate.
Authorized guard-maintenance scope: Local-only dispatch/closure continuity and
currentAuthority baseline/work-order fingerprints, with no checker logic change.
Protected paths / exact scope:
- CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json
- CVF_SESSION/state/entries/nextAllowedMove.json
- CVF_SESSION/state/entries/domainPilotSelectedReviewDecision20260912.json
- CVF_SESSION/ACTIVE_SESSION_STATE.json
- CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json
- CVF_SESSION_MEMORY.md
- AGENT_HANDOFF_V60_2026-09-08.md
Rollback boundary: revert only this packet's projection if rejected; preserve
accepted history. Edit session sources then regenerate aggregates. Worker cannot
write any protected path. Local may update the pair's lifecycle and coupled
currentAuthority hashes at return; authority repair is never delegated to worker.


## Scope / Target / Owner Boundary

Worker owns docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json and docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md only. Local owns the pair, docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json, docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md and the seven continuity paths above. External inputs remain unchanged.

## Source Verification Block

| Fact | Source file | Verified section | Disposition |
|---|---|---|---|
| Original ZIP located and hash matched | docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json | packageSha256 and inputs | ACCEPT |
| Historical scoped acceptance available | docs/reviews/CVF_MULTI_REPO_ACCEPTANCE_HISTORY_TRIAGE_2026-09-13.md | Target / Source | ACCEPT |

## Acceptance Criteria

Paired work order controls 54 source IDs, 68 obligation IDs, honest scoped acceptance, unresolved search evidence and next nomination. No fabricated source-value or current freshness decisions.

## Evidence / Verification

dfae47c8c0feaf7e0508d08f4d02438a41ef98c6 was clean. Archive member hashes 7/7 match. Source IDs unique 54/54; 40 Git rows use 39 distinct URLs. Historical backlog unique IDs 68/68, including three XD rows. Standalone backlog provenance remains distinct from ZIP binding. Pre-dispatch and normal pre-commit must pass; split closure receipts follow continuity.

## Non-Goals And Stop Conditions

No source import or execution, implementation, network acquisition, provider/live/public/deploy, worker commit or alteration of stopped-chain blockers. Input drift or outside-scope mutation returns a precise blocker to Local.

## Checker Source Read-Ahead Block
| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| conditionalTriggersReviewed | work_order structure, active dispatch lifecycle, historical metadata versus current acceptance |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; PARTIAL; required work_order heading families |
| gateRunPurpose | Confirmation and evidence of the prepared document; not first discovery or source certification |
| claimBoundary | Document read-ahead only; no runtime or source-value claim |
| disposition | Source and contract review complete; pre-dispatch governs worker release |

## Epistemic Process Block

Expected Result / Prediction: recovered payload resolves membership uncertainty.
Evidence Comparison: exact ZIP digest and seven member digests match prior reference.
Contradiction Or Gap Disposition: historical joins and standalone backlog provenance still need worker evidence.
Claim Update: identity recovered, current absorption unproven.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: metadata joins only; exact input identity and scope are in paired work order. External content is advisory, no execution authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY: private provenance only.

## Claim Boundary

Historical metadata work only. The old chain remains STOP_REASSESS_ARCHITECTURE / NO_SUCCESSOR. This baseline does not authorize source execution or current-source acquisition.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption`, role=`reviewer`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption --role reviewer --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`.
Returned defect count: 0. Returned defects: NONE_RETURNED.
Disclosed defectIds: none. Truncated: false.
Disposition: no matching registry item; mandatory guards still apply.


## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id UMBRELLA-SEED-RECONCILIATION-T1 --title "Umbrella Seed Provenance And Historical Obligation Reconciliation" --date 2026-09-13 --base dfae47c8c0feaf7e0508d08f4d02438a41ef98c6 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Adapted existing intake lifecycle after generating the generic-worker-dispatch scaffold; replaced source, ownership, evidence and continuation contracts |
| checkerReadAheadConfirmation | Source shape, gate-to-role, lifecycle, intake, routing and handoff requirements reviewed |
| docOnlyNewFields | Doc-only provenance receipt fields; no runtime schema authority |
| claimBoundary | Generation provenance only; no source-read or runtime claim |


## Mandatory Blind-Spot Control Block

SKIPPED_WITH_REASON: baseline only; paired metadata work order binds required worker blind-spot checks.

## Corpus Completeness And Report Integrity

- Corpus task class: metadata reconciliation preparation.
- Corpus root: exact inputs listed in docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json.
- Snapshot time: receipt checkedAtUtc.
- Enumeration command: filesystem-backed direct file reads and ZIP member listing.
- Manifest artifact or inline manifest: receipt inputs and packageEntries.
- Manifest hash: per-input SHA256 values in receipt; no aggregate corpus claim.
- Processing ledger artifact or inline ledger: receipt readDepth; worker audit planned.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=7; ledger_terminal=2; exclusions=0; unresolved=5 for local input processing: ZIP/backlog metadata parsed, five domain ledgers hash-only pending semantic read. 54 source IDs, 68 historical obligation IDs, seven local input files; different units never added. Source semantic corpus is excluded.
- Unresolved files: 5 domain-ledger content reads; semantic Local mappings are worker work.
- Declared exclusions: current upstream source contents, network freshness and runtime.
- Unreadable or unsupported files: none encountered during metadata reads.
- Aggregation check: unique IDs independently parsed; current disposition pending.
- Drift check: rehash before and after worker reads.
- Output traceability: receipt to planned audit and return.
- Adversarial verification: membership does not imply absorption.
- Corpus verdict: PARTIAL - metadata preparation only.

