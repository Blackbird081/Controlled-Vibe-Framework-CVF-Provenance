# CVF GC-018 Baseline - Q001 SQLite Migration Recovery Rehearsal

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-Q001-SQLITE-MIGRATION-RECOVERY-REHEARSAL

Decision owner: Local reviewer/closer

Dispatch base head: `b592df835`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

## Purpose

Rehearse, on disposable synthetic data only, how the accepted local SQLite ledger candidate behaves when validated import, consistent backup and clean restore are interrupted at deterministic fault points. The tranche observes and classifies; it repairs nothing. Its output is a set of classified observations plus an oracle shown to discriminate a deliberately defective mutant, so Local can decide whether a separate repair packet or a real-data cutover packet is warranted.

## Authority And Source

The operator directed continued bounded Q001 work and Local accepted the post-chain gap audit as the basis for one further packet. That audit was delivered in chat and is not a repository artifact; every source fact below is re-verified against the governed files named in the paired work order Source Verification Block. Roadmap decisions D024, D028, D029, D030 and row Q001 in `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` keep migration, recovery under failure, retention, RPO/RTO and Q001/R0 exit open. `docs/reference/CVF_NCR_Q001_LEDGER_DURABILITY_FAILURE_PROFILE_2026-09-29.md` states the acceptance cases that a later cutover packet must still satisfy.

## Source / Predecessor Evidence

Accepted and consumed without rerun: the local transaction store completion review `docs/reviews/CVF_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_COMPLETION_2026-09-29.md` (bounded acceptance of append, rollback, peer barrier, schema rejection and one clean backup restore) and the synthetic chain completion review `docs/reviews/CVF_CVF_NCR_Q001_SYNTHETIC_SYSTEM_CHAIN_COMPLETION_2026-09-29.md`. The post-SQLite gap review `docs/reviews/CVF_CVF_NCR_Q001_POST_SQLITE_GAP_REVIEW_2026-09-29.md` ranks real-ledger migration and recovery after the synthetic chain. Neither accepted review injected a fault into import, backup or restore, ran a peer append during backup, or recorded on-disk target state after a failed migration step; that delta is this tranche. No accepted suite is rerun.

## Decision / Baseline / Proposed Tranche

Decision: author one proof-only, single-host, synthetic rehearsal. Baseline: `SqliteLedger.import_json`, `backup_to` and `restore_backup` pass clean-path and corrupted-input tests, while failure-time file state is not yet observed. Proposed output: a reproducible probe, a focused test proving the classification oracle discriminates, machine-readable observations, and a worker return for independent Local review. `DISPATCH_READY` describes reviewed packet content only; worker execution still requires a paired material commit, a continuity release and a bound pre-dispatch PASS.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py`, methods `import_json`, `backup_to` and `restore_backup`, exercised only through the existing public interface and the existing peer script. The worker creates exactly four paths: one probe, one focused test, one worker return and one evidence JSON. The owner file, its accepted tests and the peer script are read-only. Any defect the rehearsal exposes is reported as a finding and routed to a separate repair packet; this packet never edits the owner file. Local reviewer owns the independent probe and acceptance. The operator owns every checkpoint listed under Operator Checkpoints.

## Acceptance Invariants

1. Positive round trip: a synthetic N-block chain, N fixed at 12 in the work order, imports from a copied JSON source, backs up, and restores. A raw SQL and hash oracle, independent of the product reader, checks ordinal continuity, request ID, predecessor link, block hash and tip at each stage.
2. Faults are injected before target creation, after target creation, inside the insert loop and after commit at verification for import; before and after copy for backup and restore. The worker attempts a true mid-copy interruption only if it can show the production `sqlite3.Connection.backup` call was entered and the copy was incomplete. Otherwise it records `NOT_INDUCIBLE_WITHOUT_OWNER_HOOK`; a simulated replacement for the backup call is labeled simulation and cannot prove mid-copy product behavior. For every fault the record holds the exception class, a redacted message, whether the call returned or raised, the target and sidecar state on disk, and the outcome of a retry against the same target path.
3. Target state uses one fixed vocabulary: clean (target and sidecars absent), partial (present but not equal to the expected chain, whether openable or not), usable (opens, schema and hash chain valid, chain equal to expected), or sidecar-only. Partial, sidecar-only and usable-after-reported-failure outcomes are findings, never silently normalized.
4. Source and backup integrity before and after each isolated scenario: JSON source SHA-256 must be identical. Simulated post-commit verification mismatch changes only the probe's read result, never the source file. For SQLite files record both the raw-file SHA-256 and a logical digest over ordered ordinal, request ID and block hash. An input that is meant to remain unchanged retains its logical digest; the peer-append case separately records the expected source change. Raw-byte change on open is recorded, not asserted equal.
5. Oracle discrimination: at least one mutant that deliberately leaves a partial target after a fault, one that returns success with a short chain, and one that alters the source logical digest must each be detected by the oracle, alongside clean, usable and unopenable control fixtures classified correctly. An oracle that cannot reject its mutant makes the tranche return blocked.
6. Peer concurrency: a real second process, driven by the existing barrier events READY, START_ATTEMPT, ATTEMPTING, PARENT_RELEASE, ENTERED and COMPLETE, appends while a backup is taken. The result must be a complete valid chain equal to either the pre-append or post-append state, never a mixture, and the early-entry mutant must be rejected. If a peer commit between backup steps cannot be induced deterministically without editing the owner file, that inability is itself a recorded finding, not a skipped case.
7. After each backup or restore fault, a subsequent real peer process acquires and appends to the source ledger, showing no stranded lock.
8. No finding observed under fault may be restated as a claim that migration, backup or restore is safe, ready for cutover, or durable. The return may state observations, classifications and open findings only.
9. The independent Local reviewer separately runs at least one import fault, one restore-from-corrupted-backup case and one peer-during-backup case through a distinct assertion path, and owns acceptance. The worker returns the probe as pending.

## Forbidden Scope

No edit to the owner file, its accepted tests, the peer script or any engine or Web source. No access to the current GitHub JSON ledger, `.env.local`, OAuth configuration, operator artifacts or any real data; no real ledger migration or cutover; no provider invocation, external runtime, public sync, deployment, pilot effect, artifact acceptance, P11 or Q001/R0 exit; no automatic retry policy; no stage, commit or stash. No claim of retention, RPO/RTO, backup location or key custody, authoritative instance, cost, P08 coverage, power-loss durability, hosted or multi-host behavior.

## Operator Checkpoints

Undecided and not requested here: real GitHub ledger cutover; backup location and key custody; retention and deletion schedule; RPO and RTO targets (the roadmap values are proposals awaiting confirmation); authoritative engine instance and store; cost budget; P08 scope reconciliation; artifact acceptance owner and metric; pilot or live effect; P11; deployment. The rehearsal needs none of these decisions and must not set any of them by implication.

## Deferred Findings Outside This Tranche

Recorded from the accepted audit so they are not lost, and each needs its own packet: absence of an HTTP exact-ID query and of engine-side authentication evidence on the ledger routes (`EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py`, routes at lines 143-250); a same-ID engine replay that appears to conflict because the orchestrator stamps a fresh timestamp into the event (`EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core_orchestrator.py`, lines 195-208) against the identical-bytes rule in `sqlite_ledger.py` lines 161-165, source-derived and not executed; and millisecond-resolution attempt IDs in the export receipt helper. None is repaired or probed here.

## Evidence / Verification

At authoring, source reads and static packet checks are the only evidence. Worker proof later comprises the probe output, focused test result, the observation JSON and the return, with detached exact-byte return digests before and after the final required gate. Reviewer acceptance requires a separately executed probe. Static admission does not establish any observed behavior.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_COMPLETION_2026-09-29.md` |
| Chain map route | Local source-derived rehearsal under the existing ledger owner |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | External advisory is not private-CVF proof. |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; result 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | `Status`; `Batch ID`; `WORKER_MUST_NOT_COMMIT`; `acceptance-ledger-json`; `High-Risk Local Transaction Proof Applicability`; `DR-01` through `DR-07`; `Task Governance Routing Manifest` |
| gateRunPurpose | Confirmation of a source-backed held packet shape; gate output is evidence, not first discovery |
| claimBoundary | Static packet validation is not an observed rehearsal result or dispatch authorization |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-Q001-SQLITE-MIGRATION-RECOVERY-REHEARSAL --title "Q001 SQLite Migration Recovery Rehearsal" --date 2026-09-30 --base b592df835 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch with no-commit worker profile; previewed to stdout only |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | replaced placeholder skeleton with a source-backed baseline modeled on the accepted Q001 packets |
| checkerReadAheadConfirmation | read dispatch quality, release readiness, acceptance ledger, high-risk transaction and task routing checker sources |
| docOnlyNewFields | N/A with reason: no new field contract introduced |
| claimBoundary | Scaffold provenance is authoring evidence only, not a release or observation. |

## Claim Boundary

This baseline defines observation requirements. No worker has been released, no rehearsal has been run, and nothing here establishes that migration, backup or restore is safe, that any failure mode is acceptable, or that a real-ledger cutover may proceed. Q001/R0 stays open, P11 stays parked, and the HTML artifact stays `DRAFT_UNACCEPTED`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
