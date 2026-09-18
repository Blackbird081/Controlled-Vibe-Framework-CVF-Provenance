# CVF GC-018 Baseline - ACEL G1 T2F R1 Contract Coherence Correction

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-18

Batch ID: ACEL-G1-T2F-R1-CONTRACT-COHERENCE-CORRECTION

Dispatch base HEAD: `bcc346d0c15f5270ec350736b6407f72023650ef`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer

Worker target: one shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize one consolidated R1 correction of the two existing uncommitted T2F
documentation outputs. The correction closes T2F-R1-01 through T2F-R1-05
without creating any operational source, schema/code implementation, key,
credential, runtime behavior or successor tranche.

## Decision / Baseline

The initial return's scope, no-commit evidence, parked-path ledger,
owner-separation matrix and source-not-created boundary are retained. Its
canonical hash, schema completeness, consumer joins, activation semantics and
proposed-path collision evidence are rejected by the Local review at
`docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md`,
SHA-256 `d84f6bd23f9fa9e52c71b0aeeb924a4af89b0b7b31263f2231fb465e39b0f4b0`.

One R1 may modify the same audit and worker-return paths in place. It may not
create a third worker artifact or an operational path.

## Consolidated Correction Contract

| Finding | Required outcome |
|---|---|
| T2F-R1-01 | one RFC 8785 JCS, UTF-8, no-BOM, domain-separated SHA-256 profile; every stored digest excluded from its own preimage; exact field/framing rules and mutation probes |
| T2F-R1-02 | every referenced version, snapshot, role, integrity and receipt field appears in the declared schema; Group 1 gains an exact lifecycle-receipt path/contract; Group 4 gains registry-snapshot and lookup-response bindings |
| T2F-R1-03 | Group 1/3/4 schemas satisfy the exact T2C key and provenance consumer joins, including snapshot identity/content/hash, authority, observation time, key role, active-head/fork rules and lookup-result binding |
| T2F-R1-04 | approval, activation and supersession are explicit append-only events; at most one active specification; no automatic latest-wins resolution |
| T2F-R1-05 | a literal per-path/path-family collision ledger records existence and token-search results for every proposed operational location |

## Exact Worker Manifest

The worker modifies exactly:

1. `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`;
2. `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md`.

Both paths already exist untracked. All other files are read-only. The thirteen
pre-existing parked G1 paths remain byte-identical and uncommitted.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| initial T2F return | exact two uncommitted outputs at execution base `bcc346d0c` | retained as repair target, not authority | ACCEPT_AS_REWORK_INPUT |
| consolidated Local review | completion review SHA-256 `d84f6bd23f9fa9e52c71b0aeeb924a4af89b0b7b31263f2231fb465e39b0f4b0` | five findings frozen before repair | ACCEPT |
| accepted T2C consumer | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | R1 must satisfy its exact consumer fields and ordering | ACCEPT |
| source creation or implementation | no authorization | separate future operator/Local packet | PARKED_NO_SOURCE_CREATION_AUTHORITY |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| initial return has five consolidated design defects | REVIEWED_DECISION | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md` | Findings / Position | T2F-R1-01 through T2F-R1-05 | Local reviewer | ACCEPT |
| T2C requires exact key-role and observation fields | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Signature And Key-ID Envelope; Genuine Lookup Provenance | `SignatureValidityCheck`; `LookupProvenanceCheck` | accepted T2C design | ACCEPT |
| operational sources already exist | SOURCE_EXISTENCE | initial T2F audit | all four group dispositions | proposed operational paths | future source owners | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact path probes | `Test-Path -LiteralPath docs/baselines/CVF_GC018_ACEL_G1_T2F_R1_CONTRACT_COHERENCE_CORRECTION_2026-09-18.md` and the corresponding exact work-order-path probe each returned `False` before authoring | ACCEPT_NO_COLLISION |
| exact token query | `rg -n --hidden --no-ignore -F "ACEL-G1-T2F-R1-CONTRACT-COHERENCE-CORRECTION" docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'` | ACCEPT_QUERY_RECORDED |
| query roots and coverage | roots `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION`; Markdown, JSON, Python and TypeScript source/test/evidence surfaces | ACCEPT_NAMED_COVERAGE |
| token result | only the newly authored Local review and paired dispatch packet references; the pre-existing T2C path token is an authoritative input occurrence, not an R1 output-path collision | ACCEPT_PLANNED_REFERENCE_ONLY |
| absent-versus-collision disposition | exact new paths were absent at the pre-authoring probe; subsequent occurrences are the one intentional packet family | ACCEPT_NO_COLLISION |
| worker outputs | both existing untracked paths are modified in place; no duplicate return | REUSE_EXACT_PATHS |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2F-R1-CONTRACT-COHERENCE-CORRECTION --title "ACEL G1 T2F R1 Contract Coherence Correction" --date 2026-09-18 --base bcc346d0c15f5270ec350736b6407f72023650ef --commit-mode WORKER_MUST_NOT_COMMIT --dependency ACEL-G1-T2F-INITIAL-RETURN-REJECTED --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id acel-g1-t2f-source-contract-design-first-authoring --prior-finding-set-digest d84f6bd23f9fa9e52c71b0aeeb924a4af89b0b7b31263f2231fb465e39b0f4b0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence T2F-R1-01,T2F-R1-02,T2F-R1-03,T2F-R1-04,T2F-R1-05 --scec-problem-key acel-g1-t2f-r1-contract-coherence --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --stdout` |
| generatedProfile | held-dependency, internal REWORK and no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated frozen review, exact two-path repair, five finding outcomes and source/runtime prohibitions |
| checkerReadAheadConfirmation | dispatch-quality, convergence, closeability, review-cost, worker-return, trace and structural checker sources |
| docOnlyNewFields | canonical-profile contract; active-head/fork semantics; lookup-response binding; per-path collision ledger |
| claimBoundary | scaffold and baseline authorize documentation repair only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | REWORK convergence scalars; SCEC initial-chain fields; closeability phases; worker-return headings; baseline structural headings |
| gateRunPurpose | confirm the already-authored R1 packet shape before dispatch |
| claimBoundary | checker PASS does not repair or accept the worker outputs |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched ADIF entry; the Local five-finding review remains binding.

## Evidence / Verification Boundary

Before release require exact Local three-path staging, worker/parked-path
exclusion, pre-dispatch PASS and material commit. Worker execution begins only
from the committed R1 packet and synchronized handoff. Machine conformity is
not semantic acceptance or source establishment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private internal rework dispatch with no public authority.

## Claim Boundary

This baseline authorizes correction of two documentation outputs only. It
does not authorize creation of any proposed source path, key, credential,
schema/code implementation, lookup, candidate admission, runtime, provider,
public-sync or deployment effect.
