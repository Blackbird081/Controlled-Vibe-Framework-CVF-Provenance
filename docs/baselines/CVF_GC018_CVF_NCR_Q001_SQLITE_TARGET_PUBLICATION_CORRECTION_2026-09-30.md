# CVF GC-018 Baseline - Q001 SQLite Target Publication Correction

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-Q001-SQLITE-TARGET-PUBLICATION-CORRECTION

Decision owner: Local reviewer/closer

Dispatch base head: `a473a290f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

## Purpose

Correct the synthetic single-host SQLite migration, backup and restore target-publication boundary revealed by the accepted rehearsal. A final target must not be exposed as partial when an operation fails before publication. A lost response after publication remains ambiguous and cannot silently authorize a retry or cutover.

## Authority And Source

The operator approved continuation to packet authoring. The active bootstrap next move names this corrective packet and keeps implementation behind independent packet review, committed authority and bound pre-dispatch PASS. The source-backed audit `docs/reviews/CVF_CVF_NCR_Q001_POST_REHEARSAL_TARGET_PUBLICATION_AUDIT_2026-09-30.md` at `62e22ec59` supplies the bounded decision. Roadmap D031/D032 and Q001 in `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` retain the real-ledger cutover and Q001/R0 checkpoint.

## Source / Predecessor Evidence

Consume the Local-accepted rehearsal `docs/reviews/CVF_CVF_NCR_Q001_SQLITE_MIGRATION_RECOVERY_REHEARSAL_COMPLETION_2026-09-30.md` without rerunning its full matrix. Import F2/F3 left a schema-valid empty final target; F4 and backup/restore post-copy faults could report failure with a complete target; kill trials observed zero-byte targets; same-path retries were refused. F3's connection subclass duplicated two `_connect` pragmas. The independent Local probe corroborated the post-creation empty target, corrupt-restore rejection and peer-consistent backup. Kill/race counts were nondeterministic and mid-copy and peer-between-steps cases stayed unobserved. The paired work order verifies every current source fact against the product owner and tests.

## Decision / Baseline / Proposed Tranche

Decision: one high-risk, code-and-test correction packet for `SqliteLedger.import_json`, `backup_to` and `restore_backup` on disposable synthetic files. Baseline: each method currently creates the final target before all fallible work and verification complete. The worker prepares and validates a sibling staged candidate, publishes to an absent final path without clobbering, and supplies a read-only outcome classification procedure. This is `DISPATCH_READY` content only; implementation requires the paired packet review, material commit, continuity binding and bound pre-dispatch PASS.

## Scope / Target / Owner Boundary

The product owner is `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py`. The worker may edit that owner, its focused test file, and create the exact probe, evidence and return paths in the paired work order. The existing peer script is read-only. All exercise files live in a new ignored disposable root. The shared-workspace worker is `INTERNAL_AGENT`; Local owns independent review and material commit. No Web, engine API, operator ledger, authorization or policy file changes are in scope.

## Acceptance Invariants

1. Existing method signatures and success return fields stay stable. A valid synthetic import, consistent backup and clean restore produce a complete chain, independently verified by raw SQLite rows and recomputed hashes. Source input stability is declared: JSON import uses a copied quiescent source; restore uses a quiescent backup; online peer backup must yield one complete snapshot rather than a mixed chain.
2. Before publication, an injected or natural handled failure leaves the final path and its SQLite sidecars absent, except a pre-existing target or sidecar, whose bytes and names remain unchanged. Staging is unique, sibling, same-filesystem and attempt-owned. Cleanup touches only that staging set; cleanup failure is disclosed, not erased with a wildcard delete.
3. Publication is no-clobber against an existing target or a competing target-file creator. The staged database has all writes finished, connections closed, WAL checkpointed or otherwise reconciled, and no required sidecar dependency before publication. An unsupported filesystem or failed publication remains fail-closed. No claim is made for uncooperative concurrent sidecar creation across multiple names.
4. No fallible validation follows publication that can report a completed target as a failed operation. A kill or lost response after publication may leave a complete target with no response; it is classified read-only and never grants `safeToRetry=true`. Unknown provenance, partial/invalid and sidecar-only states stay blocked for operator disposition.
5. Focused fault cases exercise import before insertion, mid-insert rollback, pre-publication verification failure, backup and restore copy/post-copy failure, existing target and sidecars, a competing creator, and process termination on both sides of a proven publication barrier where inducible. A real second-process peer and negative ordering oracle preserve the high-risk contract. Inducibility limits are findings, never silent passes.
6. Worker leaves only the exact five-path manifest uncommitted and returns `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`. Local uses a separate raw-SQL/hash assertion path and keeps Q001/R0 open regardless of this synthetic result.

## Forbidden Scope

No real GitHub JSON ledger migration or cleanup, no automatic retry, no source or backup mutation, no owner/DACL change, no credential access, no provider/live call, no external runtime, no public sync or deployment. Do not edit the earlier rehearsal proof or its evidence. Do not infer power-loss durability, off-machine recovery, multi-host support, retention compliance, artifact acceptance or cutover readiness.

## Operator Checkpoints

The operator retains real-ledger cutover, authoritative instance, backup destination/key custody, retention/deletion, RPO/RTO, cost budget, P08 scope, artifact acceptance, pilot/live effects, P11 and deployment. This packet chooses none of them.

## Deferred Findings Outside This Tranche

True mid-copy interruption and a peer commit between backup steps were not induced in the rehearsal. This correction tests them only if an owner-internal, production-call barrier proves the boundary; otherwise the return keeps `NOT_INDUCIBLE_WITHOUT_OWNER_HOOK`. Process kill distributions are observations. Retention, backup custody, power loss, hosted storage and actual GitHub-ledger rollback are separate packets.

## Evidence / Verification

The five worker paths and proof IDs are bound in the paired order's acceptance ledger. Require focused tests, a reproducible disposable probe with per-case source/target/sidecar observations, a real peer barrier, mutant rejection, a final exact-return hash transcript, the full worker-return fast gate and an independent Local probe before acceptance. The reviewer decides whether implementation meets this contract; passing a static gate alone does not prove behavior.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_Q001_POST_REHEARSAL_TARGET_PUBLICATION_AUDIT_2026-09-30.md` |
| Chain map route | Local finding-to-correction routing |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No external advisory is private CVF proof |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; source ACCEPT rows; acceptance ledger; high-risk applicability; read-budget and release barrier |
| gateRunPurpose | Confirm source-backed packet content after design and reviewer challenge, not first discovery |
| claimBoundary | Checker results do not authorize execution before committed continuity release or prove repaired behavior |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-Q001-SQLITE-TARGET-PUBLICATION-CORRECTION --title "Q001 SQLite Target Publication Correction" --date 2026-09-30 --base a473a290f --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | replaced placeholders with bounded source-backed correction and five-path worker manifest |
| checkerReadAheadConfirmation | read the dispatch, release, acceptance-ledger, high-risk and structural checker source |
| docOnlyNewFields | N/A with reason: no new governed field contract |
| claimBoundary | Scaffold is authoring evidence only |

## Claim Boundary

This baseline authorizes only a synthetic single-host code/test correction after the paired release barrier. It does not make any migration, recovery, retention, RPO/RTO, provider, public or production claim. Q001/R0 remains open.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
