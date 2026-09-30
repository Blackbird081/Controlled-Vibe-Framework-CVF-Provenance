# CVF NCR Q001 Post-Rehearsal Target Publication Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_NO_DISPATCH

Date: 2026-09-30

Batch ID: CVF-NCR-Q001-SQLITE-TARGET-PUBLICATION-CORRECTION-PROPOSAL

## Purpose

Choose one bounded corrective packet from the accepted SQLite migration/recovery rehearsal findings. This is a Local technical routing decision, not an implementation order or real-ledger cutover approval.

## Target / Source

- Accepted rehearsal and independent probe: `docs/reviews/CVF_CVF_NCR_Q001_SQLITE_MIGRATION_RECOVERY_REHEARSAL_COMPLETION_2026-09-30.md`, material commit `1e0fc7ec1`.
- Worker observations: `docs/reviews/CVF_CVF_NCR_Q001_SQLITE_MIGRATION_RECOVERY_REHEARSAL_WORKER_RETURN_2026-09-30.md` and `docs/reviews/evidence/cvf-ncr-q001-sqlite-migration-recovery-rehearsal-worker-2026-09-30.json`.
- Decision owner: `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D031 and Q001.
- Product owner: `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py`, `import_json` at line 181, `backup_to` at line 207 and `restore_backup` at line 223 at HEAD `010c09d07`.
- Existing focused tests: `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_sqlite_ledger.py`.
- Earlier recovery contract: `docs/reference/CVF_NCR_Q001_LEDGER_DURABILITY_FAILURE_PROFILE_2026-09-29.md`, Technical Disposition And Next Contract.

## Scope / Methodology

Startup acknowledged: mode=`cvf_ncr_p10_closed_p11_parked`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=audit Q001 post-rehearsal findings and propose one corrective packet; role=Local reviewer/steward; phase=post-rehearsal audit; decision owner=Local; parked checkpoint=real ledger cutover, pilot/live, P11, external runtimes, public sync and deployment. The shared-workspace Claude worker, if dispatched later, is `INTERNAL_AGENT`. I consumed the accepted observations and read the three current product methods and existing tests. I did not rerun the 28-case worker matrix or access the GitHub ledger. This is a named-owner audit, not a complete-corpus scan.

## Findings / Position

| Evidence | Current source cause | Decision consequence |
|---|---|---|
| Import F2/F3 leaves an openable empty target, and the same-path retry raises `FileExistsError` | `import_json` constructs `SqliteLedger(target)` before the insert transaction; target creation precedes completion | Prepare at a unique sibling staging path and keep the final target absent until the staged chain is verified |
| Import F4 and backup/restore post-copy faults can raise with a complete final target | Final-target creation or copy precedes a fallible read/verification step | Perform all expected-chain validation before publication; define the success-return boundary and do not turn post-publication cleanup failure into a misleading operation failure |
| Kill after target creation left a zero-byte target, sometimes with a journal, in the observed trials | `backup_to` and `restore_backup` open the final target before `Connection.backup` finishes | A kill may leave attempt-owned staging residue, but must not expose a partial final target; crash after publication may still leave a complete final target with no response |
| Existing final targets or sidecars were unchanged in observed rejection cases | Methods check existence, but a check followed by later creation does not itself reserve the name | Publication must be no-clobber under a competing creator; preserve pre-existing bytes and sidecars and fail closed on a race |
| Mid-copy interruption and a peer commit between backup steps were not induced | Current backup call has no owner-owned progress barrier | Include a proportionate deterministic seam only if the corrective packet can keep it internal and demonstrate real production-call traversal; otherwise retain the unobserved boundary |

The worker's F3 connection subclass duplicates two `_connect` pragmas; that limits F3's generality but does not erase the independently reproduced post-creation empty-target finding. The two added pre-existing-target tags are accepted evidence vocabulary. Kill/race trial counts and `-journal` occurrence vary and are not acceptance thresholds.

## Proposed Bounded Corrective Packet

Proposed batch: `CVF-NCR-Q001-SQLITE-TARGET-PUBLICATION-CORRECTION`. The dispatcher should author a fresh GC-018 baseline, work order and independent packet review before release. The worker may change only the SQLite ledger owner, its focused tests, and explicitly named worker-return/evidence paths after the work order binds an exact manifest. Local remains the independent reviewer and commit owner; worker mode should be `WORKER_MUST_NOT_COMMIT`.

The contract to be bound by that packet is:

1. `import_json`, `backup_to` and `restore_backup` build a candidate at a unique sibling staging path on the same filesystem. Verify version, schema, ordered request IDs, block hashes, predecessor links and expected chain or snapshot before publishing. Preserve the existing return fields on success. The dispatcher must define what input stability is assumed for an import source and backup source; concurrent source mutation must not be silently treated as a verified copy.
2. Publish a verified, closed SQLite file to an absent final path with a no-clobber operation. A prior target file or SQLite sidecar and a competing creator must remain unchanged. A simple `exists()` check followed by overwrite-capable rename is insufficient. Show that the chosen operation works on the supported single-host Windows profile; cross-device movement and unsupported filesystems fail closed.
3. For handled faults before publication, the final target remains absent and source bytes remain unchanged. Clean up only staging files demonstrably owned by this attempt. Failed cleanup is disclosed as residue, never used as proof that the final path is safe. No automatic deletion of an unknown, pre-existing or ambiguous final target is permitted.
4. After publication, the target is complete and independently readable. A lost response or process kill after publication remains an ambiguous outcome; same-path retry is not automatically authorized. Provide a read-only classification/reconciliation procedure that distinguishes absent, complete expected target, partial/invalid target, sidecar-only and unknown/pre-existing ownership, without returning `safeToRetry=true` or promoting a target to authoritative use.
5. Focused synthetic tests cover import before first insert, mid-insert rollback, verification failure, backup/restore copy and post-copy failures, pre-existing target/sidecars, a competing target creator, and process termination at a proven before/after-publication barrier where inducible. Use raw SQLite plus independent hash/link checks for the Local probe; distinguish observed crash states from guarantees. Mid-copy and peer-between-steps remain `NOT_INDUCIBLE_WITHOUT_OWNER_HOOK` unless a real barrier proves them.

The dispatcher must consult `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` and its machine guard. This is a high-risk local transaction repair, so a real peer process, deterministic ordering, fault/rollback proof, independent Local probe and exact evidence hash are required where applicable. One packet should fix this target-publication cluster; retention and off-machine recovery are separate decisions.

## Risk / Corrective Action

There is no general way for the caller to infer from a missing response that publication did not occur. An exception before publication, a killed process, and a lost response after publication need distinct evidence. A read-only complete-chain check can classify bytes but cannot prove who created a pre-existing target or grant it authority. The correction must fail closed on unknown origin or cleanup state. Do not claim power-loss durability, atomic directory persistence, multi-host safety, online cutover, bounded RPO/RTO or backup custody from a local synthetic test.

## Decision / Disposition

`REVIEW_COMPLETE_NO_DISPATCH`. Propose exactly the target-publication correction packet above. It is not yet a work order; implementation waits for its paired GC-018, source verification, independent packet review, acceptance ledger and pre-dispatch gate. Q001/R0 remains open. The operator still owns real GitHub-ledger cutover, authoritative instance, backup location/key custody, retention, RPO/RTO, cost, P08, artifact acceptance, pilot/live, P11 and deployment.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | review target, scope, findings, risk, decision, epistemic and claim-boundary headings; `REVIEW_COMPLETE_NO_DISPATCH` |
| gateRunPurpose | Confirm source-derived proposal shape after reviewing accepted evidence and owner code; checker execution is confirmation, not first discovery |
| claimBoundary | Static checks do not authorize or prove the proposed repair |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_Q001_SQLITE_MIGRATION_RECOVERY_REHEARSAL_COMPLETION_2026-09-30.md` |
| Chain map route | Local private-CVF finding-to-packet routing |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | SQLite ledger product owner cited above |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No remote or public evidence is used as private CVF proof |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT` for any later worker. Phase: Local post-rehearsal audit now; internal correction is a proposed next phase. Decision owner: Local.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - only the named owner methods, tests and accepted rehearsal evidence were reviewed; no all-files claim is made.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Finding | Disposition | Next control action |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | Final target can exist in partial or complete-but-reported-failed state after an interrupted call | RULE_EXISTS: high-risk local transaction proof and separate correction packet are already required | Bind no-clobber publication and outcome-classification acceptance in a fresh work order; do not add a new universal rule based on this one owner |

## Epistemic Process Block

### Expected Result / Prediction

Creating a final target before verification allows a failed call to leave a partial or complete target; staging and no-clobber publication should remove the handled pre-publication partial-final state without solving lost-response ambiguity.

### Evidence Comparison

The accepted rehearsal observed empty and zero-byte final targets after selected faults, complete targets after post-copy verification faults, and same-path retry refusal. Source inspection shows final-path creation before the fallible operations. No corrective code has run yet.

### Contradiction Or Gap Disposition

No contradiction to the bounded rehearsal. Mid-copy, peer-between-steps, power loss and unknown target origin remain unproven and must be tracked separately.

### Claim Update

The next useful step is one high-risk, synthetic target-publication correction packet, followed by independent Local review. No migration or recovery safety claim is made now.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex Local reviewer/steward |
| Provider or surface | private CVF shared workspace |
| Session or invocation | post-rehearsal Q001 finding audit, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | read-only governed evidence/source reads; review artifact authoring; applicable local checks |
| Target paths | `docs/reviews/CVF_CVF_NCR_Q001_POST_REHEARSAL_TARGET_PUBLICATION_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Allowed scope source | active handoff and bootstrap next allowed move `AUDIT_Q001_POST_REHEARSAL_FINDINGS` |
| Before status evidence | clean worktree at HEAD `010c09d07` |
| After status evidence | new untracked audit and modified roadmap pending Local commit |
| Diff evidence | exact review and roadmap two-path material delta |
| Approval boundary | proposal only; separate packet authoring and release required |
| Claim boundary | no owner change, worker execution or real-ledger mutation |
| Agent type | Local reviewer/steward |
| Invocation ID | cvf-ncr-q001-post-rehearsal-audit-20260930 |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_Q001_POST_REHEARSAL_TARGET_PUBLICATION_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_Q001_POST_REHEARSAL_TARGET_PUBLICATION_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This review proposes a corrective contract; it does not release a worker, accept a repaired implementation, authorize real-ledger cutover, set operator policy, or close Q001/R0. The accepted rehearsal remains bounded evidence with its nondeterministic and unobserved cases.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
