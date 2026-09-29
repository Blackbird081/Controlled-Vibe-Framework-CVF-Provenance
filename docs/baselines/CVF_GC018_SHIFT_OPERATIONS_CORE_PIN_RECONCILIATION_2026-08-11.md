# CVF GC-018 Baseline - Shift Operations Core Pin Reconciliation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-08-11

Batch ID: SOPR-CP1

Core dispatch base head: `b44c61b7c87484248158747265a1de524f8fd8f1`

Downstream execution base head: `0b835be3ff1ac1fbd1c95e365471887202d718b5`

Hidden public Core target: `2103a38fda01ee827e9fc6c3be38a824fa5d54ad`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator-delegated orchestrator/reviewer

Reviewer owner: independent reviewer/closer

Worker target: provider-neutral implementation worker in shift-operations-workspace

## Purpose

Authorize one bounded downstream governance reconciliation so the manifest,
AGENTS carrier, active continuity and Project Knowledge agree with the already
clean hidden public Core. No product/runtime work or hidden-Core mutation is
authorized.

## Authorization

The operator instructed continuation after ACRC-T3 closure and previously
delegated full orchestrator/reviewer decision authority. The orchestrator
selected the smallest named parked debt: core-pin reconciliation only.

## Dependency Release Evidence

| Dependency | Evidence | Release rule | Disposition |
|---|---|---|---|
| ACRC-T3 closed | target `0b835be3f`; Core material `854cef029`; Core sync `b44c61b7c` | T3 and its review must be closed and both repositories clean | ACCEPT |
| fresh lane authority | operator continuation instruction on 2026-08-11 plus prior full delegation | fresh operator/orchestrator selection required by V59 | ACCEPT |
| hidden public Core truth | `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_SOURCE_VERIFICATION_2026-08-11.md` | clean HEAD must equal local origin/main at one exact commit | ACCEPT |

## Scope

Worker exact-10:

1. `.cvf/manifest.json`
2. `AGENTS.md`
3. `knowledge/manifest.json`
4. `IMPLEMENTATION_STATUS.json`
5. `SESSION/ACTIVE_SESSION_STATE.json`
6. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
7. `SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
8. `SESSION/SESSION_MEMORY.md`
9. `SESSION/handoffs/CORE_PIN_RECONCILIATION_2026-08-11.md`
10. `docs/decisions/SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_WORKER_RETURN_2026-08-11.md`

The worker leaves all paths unstaged and makes no commit. The reviewer may add
one reviewer-owned completion review and convert pending-review continuity to
closed bounded before committing.

## Non-Goals

- no hidden-Core fetch, pull, reset, reconciler, checkout, or file mutation;
- no product/runtime, P4-A/P4-A2, provider/live, RAG/vector, persistence,
  API/UI, catalog, roadmap-feature, deployment, public-sync, push, or release;
- no `.cvf/local-binding.json` edit and no workspace-root wrapper change;
- no claim that local `origin/main` proves current remote state.

## Design Control Gate

Lane split: worker performs exact-10 local governance/continuity edits;
independent reviewer recomputes source truth and owns target commit; Core
session-sync follows dispatch authority in a separate commit.

Risk ceiling: R2. Live proof is not applicable because this tranche makes no
claim that CVF governs AI/agent runtime behavior.

## Baseline Decision

Authorize SOPR-CP1 as a no-commit exact-10 governance/continuity worker batch
at the pinned target base and preimages. Independent review and commit
ownership are mandatory; any broader need blocks this baseline.

## Fresh Protected Preimages

| Path | Required SHA-256 |
|---|---|
| `.cvf/manifest.json` | `955fe3cf98db1be1d9137722ce4d0f3e54112f0323b66468c2da23835eca90a7` |
| `AGENTS.md` | `ce358a2be211404184dbc979365549832530b4cc051d47217bacae48865c0f3f` |
| `knowledge/manifest.json` | `cca3a718de44f31023ec47809ce5ea743edf5f9c422715882f9f46794265d5fe` |
| `IMPLEMENTATION_STATUS.json` | `98e78b46f1467757629c37fd4e21ecda1a23dc79d3aed535b23aadbb8a21b80c` |
| `SESSION/ACTIVE_SESSION_STATE.json` | `7649861a3ee7e7578a9370250793e0758a0e013bd43a61dc0a5380b54e0bc874` |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `b5bba88061893aae98c8c1b7804c48ed8df0cab0cf50b3a538690310007eff11` |
| `SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `58996220bfdaaaea9aab3f7343b8f5355e8cf859b4a4931238ddb73c47f1ed70` |
| `SESSION/SESSION_MEMORY.md` | `77e3404e5f4f50906a38f524525b8222fbbb9a26db24194b1d639a60b9373933` |
| `SESSION/handoffs/T3_ACTIVE_CONTINUITY_READ_COST_2026-08-11.md` | `144679181c0f693b30a9c03c4b4f806df050cbe1db416546b119d800e5899d47` |

The new handoff and worker return must not exist at execution start. Any hash,
base, cleanliness, hidden-Core HEAD/origin, or path-existence mismatch is a
mandatory stop.

## Required Behavior

1. Set manifest `cvfCoreCommit` and AGENTS `CVF Commit` exactly to
   `2103a38fda01ee827e9fc6c3be38a824fa5d54ad`.
2. Do not run the reconciler; the hidden Core is already clean at the target.
3. Set exact post-worker mode
   `shift_operations_core_pin_reconciliation_complete_pending_independent_review`
   across canonical state, compatibility mirror and bootstrap.
4. Rotate active handoff to
   `SESSION/handoffs/CORE_PIN_RECONCILIATION_2026-08-11.md` and keep prior T3
   handoff as a history pointer.
5. Record that target and local origin/main match, doctor core-pin row passes,
   and only the bounded legacy catalog warning may remain.
6. Refresh exactly the Project Knowledge pins for `AGENTS.md`,
   `.cvf/manifest.json`, and `IMPLEMENTATION_STATUS.json`; unrelated pins stay
   byte-exact.
7. Preserve current required-read count at at most 12 and align next move and
   parked checkpoint across active surfaces.
8. Return pending independent review with staged zero and no worker commit.

## Source Verification Block

| Item | Claim type | Canonical source path | Locator | Authoritative source | Evidence basis | Decision |
|---|---|---|---|---|---|---|
| exact target/base/preimages | VALUE_SET | `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_SOURCE_VERIFICATION_2026-08-11.md` | Evidence Ledger | Core-normalized source-verification review | local Git/hash/doctor evidence | ACCEPT |
| separate reviewer commit | ORDERING_RULE | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | Required Commit Sequence | tranche choreography standard | direct source read | ACCEPT |
| transitive pin closure | SOURCE_FIDELITY | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0052.md` | Remediation | active ADIF entry | direct source read | ACCEPT |

## Acceptance Criteria

- AC-01: target HEAD/preimages and hidden-Core exact truth pass before edit.
- AC-02: manifest and AGENTS contain the full exact target commit.
- AC-03: hidden-Core contents and workspace-root surfaces remain unchanged.
- AC-04: exact post-worker mode, handoff, next move and parked boundary agree.
- AC-05: all and only three affected Project Knowledge pins refresh exactly.
- AC-06: session, Knowledge, repository, file-size and doctor checks pass; the
  only allowed doctor note is the pre-existing legacy-catalog warning.
- AC-07: full `tests/cvf` suite passes locally without provider/live calls.
- AC-08: final worker set is exact-10, staged zero, worker commit zero.
- AC-09: worker return is complete for independent review.

## Verification Evidence

Dispatch evidence is the paired Core source-verification digest, exact
preimage table, clean Git states, hidden-Core equality and current workspace
doctor output. Execution evidence must be produced by the worker and
independently recomputed by the reviewer; dispatch evidence is not closure.

## Stop Conditions

Stop for target/base drift, dirty target or hidden Core, HEAD/origin mismatch,
preimage mismatch, missing/new-path collision, need for an eleventh worker
path, any product/runtime or external-effect need, any new doctor warning, or
any gate failure that cannot be repaired inside exact-10.

## Review Gate

Independent reviewer must rerun every acceptance criterion and may not accept
self-reported output alone. Only the reviewer/commit steward may commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOPR-CP1 --title "Shift Operations Core Pin Reconciliation" --date 2026-08-11 --base b44c61b7c87484248158747265a1de524f8fd8f1 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced every placeholder with source-verified target values, exact scope, checks, stops and boundaries |
| checkerReadAheadConfirmation | dispatch, source-intake, ADIF, trace, public-export and file-size checkers read |
| docOnlyNewFields | hiddenPublicCoreTarget; exactPostWorkerMode |
| claimBoundary | dispatch authoring provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 10 of 22 candidates; resolver output was truncated by its
built-in result ceiling.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044 |
| Disclosed defectIds | same ten IDs |
| Dispatch impact | exact manifest; provider-neutral authority; checker read-ahead; protected-path/session split; bounded command ceilings |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch-ready status; source verification columns; ADIF fields; no-commit token; public export token; exact scope |
| gateRunPurpose | confirmation and dispatch evidence, not first discovery |
| claimBoundary | Core packet shape only; downstream behavior requires worker and reviewer proof |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private downstream governance reconciliation; no public-sync authority.

## Claim Boundary

This baseline authorizes only the exact-10 local pin/continuity reconciliation.
It does not claim remote freshness, runtime governance, provider behavior,
product capability, public availability, deployment, push, release, or
production readiness.
