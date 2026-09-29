# CVF GC-018 Baseline - ACEL G1 T2G Immutable Snapshot Identity Contract

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-18

Batch ID: ACEL-G1-T2G-IMMUTABLE-SNAPSHOT-IDENTITY-CONTRACT

Dispatch base HEAD: `57309fc6d5ff8c8b7a2e8523814e90cb069b5f7f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator selected immutable snapshot identity in this conversation after Local R3 rejection.

Reviewer/closer: Local orchestrator/reviewer.

Worker: one shared-workspace `INTERNAL_AGENT`.

## Purpose

Replace the uncloseable same-snapshot correction/fork model in the uncommitted
T2F contract with one immutable observation per snapshot ID. This is a new
architecture decision after round-three escalation, not an automatic fourth
REWORK dispatch or source-creation authorization.

## Scope / Owner Boundary

The worker may modify in place only the existing T2F audit and its existing
worker-return file. Thirteen parked G1 files, accepted T2C, committed
dispatch/review/continuity and proposed operational paths are read-only. Local
alone reviews, stages and commits. The operator retains any future operational
source, implementation, key, credential, live or deployment decision.

## Architecture Decision And Acceptance Boundary

1. A `snapshotId` is immutable, globally unique within the source-observation
   authority, and identifies exactly one original observed snapshot. No second
   observation, correction, supersession, alias or fork merge can reuse it.
2. Incorrect or stale observation remains durable as historical evidence but
   cannot be repaired under the same `snapshotId`. Party B records a new
   observed snapshot with a new `snapshotId`; a verifier creates a new receipt
   bound to that new ID and hash. Existing receipts are never rebound.
3. `sourceObservationLog.lookup(snapshotId)` returns the sole original record
   or no record. `countObservationsFor(snapshotId)` counts all records with that
   exact ID, not active heads; 0 means missing, 1 unambiguous, >1 fails closed.
4. T2C's ordering, freshness, authority, hash and lookup checks remain
   unchanged. The worker must show a direct field-by-field join and positive,
   duplicate-ID, stale, mismatch and old-receipt replay negative cases.
5. Preserve the independently verified Group 1 positive vector and distinct
   Group 2 content/record hashes unless direct recomputation reveals an error.
   Remove obsolete `entryKind`, `correctionOf`, active-head, multi-parent and
   same-ID fork-resolution assertions from every schema, matrix and return.
6. Keep `snapshot_content` as one unambiguous encoded-byte representation,
   pin decoding before hashing, and bind the observed snapshot's ID/hash to
   registry lookup and durable response records.

## Decision / Baseline / Proposed Tranche

Decision: release only the T2G immutable-snapshot documentation design to one
no-commit internal worker. Baseline: accepted T2C remains unchanged; R3's
same-ID correction model remains rejected. Proposed tranche: repair exactly
the two existing T2F documents, then obtain independent Local review. No
operational source or successor implementation tranche opens here.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| accepted T2C consumer | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`, `LookupProvenanceCheck` | preserve exact one-observation semantics | ACCEPT |
| R3 worker evidence | existing T2F audit SHA-256 `33f258d4a1fa6f6b389b309e45de526fbde1b5cc7468520c43ac839e4878bc15`; existing return SHA-256 `772a577ac555d8887144a6e90efa932d9d336e342a1ff5b6ede8e8a9e71314ce` | repair input only, not accepted authority | ACCEPT_AS_REWORK_INPUT |
| round-three stop | R3 audit's liveness rule contradicts its D/E test; Local reviewer found the contradiction | operator selected a new immutable-ID architecture | RELEASE_NEW_ARCHITECTURE_DESIGN_ONLY |
| operational source creation | no source-creation authorization | separate future governed decision | PARKED_NO_SOURCE_CREATION_AUTHORITY |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2C rejects multiple observations per snapshot ID | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | `LookupProvenanceCheck`, forked-observation check | `countObservationsFor(snapshotId)` | T2C verifier | ACCEPT |
| R3 liveness test is internally contradictory | REVIEWED_DECISION | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Active-Head And Fork Resolution, liveness rule and test step 4 | `D:[C]` followed by `E:[C]` | Local reviewer | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact new baseline and work-order paths | `Test-Path -LiteralPath` returned `False` for each exact path before authoring | ACCEPT_NO_COLLISION |
| exact batch-token query | `rg -n --hidden --no-ignore -F 'ACEL-G1-T2G-IMMUTABLE-SNAPSHOT-IDENTITY-CONTRACT' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'` returned no occurrence before authoring | ACCEPT_NO_COLLISION |
| roots and coverage | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION`; Markdown, JSON, Python and TypeScript | BOUNDED_NAMED_SEARCH |
| existing worker outputs | both exact T2F paths exist untracked and will be modified in place | REUSE_EXACT_PATHS |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2G-IMMUTABLE-SNAPSHOT-IDENTITY-CONTRACT --title "ACEL G1 T2G Immutable Snapshot Identity Contract" --date 2026-09-18 --base 57309fc6d5ff8c8b7a2e8523814e90cb069b5f7f --commit-mode WORKER_MUST_NOT_COMMIT --dependency ACEL-G1-T2F-R3-REVIEW-REJECTED --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --scec-problem-key acel-g1-t2g-immutable-snapshot-identity --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --stdout` |
| generatedProfile | held-dependency, new operator-selected architecture, internal no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | immutable-ID decision, exact existing pair, rejected R3 dependency and no-source boundary |
| checkerReadAheadConfirmation | dispatch-quality, review-cost, convergence, closeability, worker-return and structural checker sources |
| docOnlyNewFields | immutable `snapshotId`; `replacesSnapshotId` may be documentary provenance only and is never a T2C lookup alias |
| claimBoundary | documentation-design dispatch only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | INITIAL, round zero, Source Verification Block, Dependency Release Evidence, Public Export Disposition, exact worker return path |
| gateRunPurpose | confirm the authored design-only packet before dispatch |
| claimBoundary | machine shape does not prove semantic acceptance or source existence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched entry; the Local architecture decision remains binding.

## Evidence / Verification Boundary

Before dispatch require exact two-path Local staging, exclusion of the worker
outputs and thirteen parked paths, pre-dispatch PASS and a material commit.
After return, Local must verify every immutable-ID acceptance row semantically;
machine conformity alone does not establish any operational source.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private contract-design dispatch; no public export authorization.

## Claim Boundary

This baseline authorizes only a new documentation model. It creates no source,
key, registry, log, verifier implementation, live proof, candidate admission,
runtime behavior, public sync or deployment effect.
