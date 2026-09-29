# CVF GC-018 Baseline - DARA-T3 WP-ARCH-003 Historical Replay

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-07

Batch ID: DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY

Dispatch base head: `42ba4db4311e98d6401e25989f392533765f0a54`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

Worker target: one bounded external replay worker reached only by operator manual relay

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Authorize one deterministic, provider-free historical replay of the
`WP-ARCH-003` Initial/R1/R2 dispatch chain against the accepted DARA-T2B
architecture-readiness controls. The replay must identify the earliest
pre-invocation stop and measure whether the known dispatcher-created defect
classes would have escaped. It does not repair or accept `WP-ARCH-003`.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | DARA-T3 replays Initial/R1/R2 and exits only as `REPLAY_BLOCKS_AVOIDABLE_INVOCATIONS` or `RETURN_TO_DESIGN`. |
| `docs/reviews/CVF_DARA_T2B_INTERNAL_RECOVERY_COMPLETION_REVIEW_2026-09-07.md` | DARA-T2B is `CLOSED_PASS_BOUNDED`; DARA-T3 remained parked until fresh operator direction. |
| operator continuation instruction, 2026-09-07 | opens DARA-T3 only; no WP implementation, provider/live, public-sync, deployment or production authority. |
| `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | current DARA schema and fail-closed admission rules are the replay oracle. |

## Decision / Baseline

DARA-T3 is an offline measurement tranche. It creates exactly five worker
artifacts: one frozen JSON fixture, one read-only replay helper, one focused
test module, one frozen result ledger and one worker return. The helper may
import accepted DARA validation functions but may not edit, wrap, register or
wire the active checker.

The replay has two layers:

1. Raw historical replay: preserve the three work-order byte identities and
   show the first current DARA admission result for each historical dispatch.
2. Seeded counterfactual replay: derive named cases from committed findings to
   test whether duplicate ownership, missing producer/consumer links,
   placeholders, self-acceptance, rollback drift and exhausted quota fail
   closed before an external invocation.

Raw results are counterfactual measurements, not retroactive invalidation of
historical commits. Seeded cases must cite their source artifact and finding;
they may not be represented as verbatim historical packets.

## Frozen Replay Source Set

| ID | Source artifact | SHA-256 | Replay role |
|---|---|---|---|
| DARA-T3-S01 | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md` | `bfd11e6d69154f5ad090e707643669edd2e6034395336fdf38946babce78fb8a` | Initial dispatch |
| DARA-T3-S02 | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_AMENDMENT_1_2026-09-06.md` | `7d9cdd4104aeca8c93ea56954c29c08300ef7fbb8296e1566851b9bd734202a2` | Rework Round 1 dispatch |
| DARA-T3-S03 | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_AMENDMENT_2_2026-09-06.md` | `b3f7e5039602ee7f1e8c41af18007a82d8ccae9b11cc71a4e046b9659c00faa4` | Rework Round 2 dispatch |
| DARA-T3-S04 | `docs/assessments/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md` | `91b2a5c07fcf341c94f3adbcaab040ec7e343a4a7faf523becabad17ec321f27` | final parked assessment and manifest evidence |
| DARA-T3-S05 | `docs/reviews/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_WORKER_RETURN_2026-09-06.md` | `014eebd65e8e5271e907a99a103687b8e7761b80d2399103cc402c7ab4ed8f98` | preserved Initial/R1/R2 finding history |
| DARA-T3-S06 | `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | `6c3e5a0028de1bed7cb3427faa040febbe85fd4295a0636dbf45d1b3e77c9688` | accepted replay oracle contract |
| DARA-T3-S07 | `docs/reviews/CVF_DARA_T2B_INTERNAL_RECOVERY_COMPLETION_REVIEW_2026-09-07.md` | `8c01aad53d4184a233bfb23b3635f8da2a86d644d4757b0f675f2aacf19438bd` | accepted T2B boundary and known residual learning |

Source drift is fail closed. The worker must not refresh these hashes. A
legitimate mismatch returns `BLOCKED_WITH_REASON` for reviewer disposition.

## Required Artifact Manifest

| Path | Worker action |
|---|---|
| `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json` | CREATE frozen source identities, raw cases, seeded cases and expected outcomes. |
| `governance/compat/dara_t3_historical_replay.py` | CREATE deterministic read-only replay helper with JSON output and no arbitrary command execution. |
| `governance/compat/test_dara_t3_historical_replay.py` | CREATE source-drift, earliest-stop, zero-tolerance, idempotence and reporting tests. |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md` | CREATE pre-replay frozen case ledger and final reconciliation. |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md` | CREATE full no-commit return. |

No sixth path may change. Historical sources, DARA production checkers,
roadmap, baseline, work order, hooks, session state and `WP-ARCH-003` artifacts
are read-only to the worker.

## Minimum Replay Contract

- Exactly three raw historical dispatch cases: Initial, R1 and R2.
- At least twelve total cases.
- Seeded cases must cover duplicate behavior identity, missing registration,
  missing runtime consumer, incomplete producer/trust link, placeholder
  evidence path, rollback outside manifest, self-authored semantic acceptance,
  unknown usage, reached external ceiling and unclassified machine result.
- Every case records source ID, derivation class, invocation ordinal, expected
  earliest stop, expected violation class and actual result.
- Zero-tolerance recall is 100% for authority bypass, duplicate owner,
  missing closed-chain link, fabricated acceptance, manifest escape and quota
  bypass. Any miss returns `RETURN_TO_DESIGN`.
- Fixture and ledger are written and hashed before the first replay command.
  After first replay, changing either is forbidden in this worker pass.
- Two identical runs must produce byte-identical normalized JSON results.

## Reviewer Strategy

The reviewer consumes the returned fixture, ledger and command evidence;
recomputes seven source hashes; samples one case per zero-tolerance class; and
reruns only the focused helper/tests plus standard fast gates. The reviewer
must not recreate the fixture, helper or full case-by-case worker analysis.

## Evidence / Verification

Dispatch evidence is limited to the seven committed source identities, the
absence of all five worker-owned paths at the dispatch base, and the
pre-dispatch gate result. Replay effectiveness is deliberately unverified at
this stage and remains worker-produced, reviewer-accepted evidence.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local repository helper/tests and reviewer readout | offline read-only replay; reviewer owns acceptance and commits | this baseline and exact five-path manifest | local process only; no provider adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | operator manually relays committed baseline/work order to one external worker | one new T3 parent invocation, 0 before and ceiling 1; no credentials or provider action from repository | committed dispatch packet and returned exact-five evidence | text relay only; no CLI/MCP invocation by orchestrator | CONTRACT_ONLY |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 mission and exit | roadmap contract | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | Work Plan; Metrics And Quota Evidence | `DARA-T3`; `REPLAY_BLOCKS_AVOIDABLE_INVOCATIONS` | DARA roadmap | ACCEPT |
| T2B prerequisite | committed review | `docs/reviews/CVF_DARA_T2B_INTERNAL_RECOVERY_COMPLETION_REVIEW_2026-09-07.md` | Decision / Disposition; Claim Boundary | `CLOSED_PASS_BOUNDED`; `483176267` | DARA reviewer closure | ACCEPT |
| replay oracle | active standard | `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | Closed-Chain Machine Contract; Quota And Admission Progression | `cvf.dara.architectureBindingMatrix.v1` | DARA standard | ACCEPT |
| historical chain inputs | committed work orders | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_AMENDMENT_1_2026-09-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_AMENDMENT_2_2026-09-06.md` | top metadata and convergence/admission blocks | Initial/R1/R2 | historical dispatch evidence | ACCEPT |
| known semantic defect sources | committed parked evidence | `docs/assessments/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md`; `docs/reviews/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_WORKER_RETURN_2026-09-06.md` | terminal finding tables; SCEC outcome | R1-01 through R2-03 | incident evidence only | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-readiness historical replay`,
role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "architecture-readiness historical replay" --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF-specific requirement; the roadmap findings and exact replay contract remain binding |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | deterministic offline replay of frozen committed inputs; no runtime/provider/live behavior is claimed |

## Negative Search And Collision Discipline

All five worker paths returned `False` from `Test-Path` at HEAD `42ba4db43`.
Search `rg -n "DARA-T3|DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY" docs CVF_SESSION governance/compat`
found only the roadmap/continuity references and no competing active T3
fixture, helper, tests, ledger or return. Disposition:
`NO_ACTIVE_DARA_T3_REPLAY_OWNER_COLLISION`.

## Core Guard Self-Protection Authorization

Authorized protected paths for the worker batch:

- `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json`
- `governance/compat/dara_t3_historical_replay.py`
- `governance/compat/test_dara_t3_historical_replay.py`

Operator authorization: fresh continuation instruction after DARA-T2B closure.
Authorized scope: new offline replay artifacts only; no edit to active guards,
hook catalogs, production dispatch code or session state. Rollback removes only
the exact five worker artifacts after reviewer disposition.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch status, external surface, architecture applicability, convergence fields, exact manifest, protected paths, trace labels, private export disposition |
| gateRunPurpose | confirm packet shape before dispatch; replay implementation has not begun |
| claimBoundary | checker structure does not prove replay correctness or authorize downstream work |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY --title "DARA T3 WP-ARCH-003 Historical Replay" --date 2026-09-07 --base 42ba4db4311e98d6401e25989f392533765f0a54 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --new-independent-critical-evidence NONE --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit return skeleton |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with frozen sources, exact-five manifest, replay contract, quota boundary and role-neutral evidence |
| checkerReadAheadConfirmation | checker sources named above were read before authoring |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only; no replay result claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline; no public-sync authority.

## Machine Closure Package

This is a dispatch baseline, not a closure artifact. The table records that
terminal evidence remains reviewer-owned without presenting a not-yet-run
result as accepted evidence.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired DARA-T3 work order | dispatch authorization only; terminal status is reviewer-owned | N/A with reason: execution has not occurred |
| Completion or reviewer artifact | DARA-T3 completion review | created only by reviewer after returned evidence | N/A with reason: no return exists |
| Roadmap state | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | T3 is the currently authorized measurement tranche | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | unchanged; this bounded replay makes no registry claim | PASS |
| Registry Markdown | `docs/corpus-intelligence/registry/` | unchanged; this bounded replay makes no registry claim | PASS |
| External evidence digest | exact-five worker manifest | no returned external evidence exists at dispatch | N/A with reason: worker has not executed |
| System loop interlock | active system-loop surfaces | no runtime or production interlock mutation is authorized | N/A with reason: offline replay only |
| Session continuity | active handoff/bootstrap/state | synchronized by closer after the dispatch material commit | N/A with reason: material commit must precede continuity sync |

## Claim Boundary

This baseline authorizes one offline exact-five historical replay. It does not
accept or implement `WP-ARCH-003`, open DARA-T4, alter P4-C1, run a provider or
live call, expose credentials, publish, deploy, push or claim production
readiness.
