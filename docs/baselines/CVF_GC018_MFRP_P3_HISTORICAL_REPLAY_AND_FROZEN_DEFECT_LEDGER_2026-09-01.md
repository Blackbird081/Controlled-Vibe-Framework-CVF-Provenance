# CVF GC-018 Baseline - MFRP-P3 Historical Replay And Frozen Defect Ledger

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MFRP-P3

Dispatch base head: `2628a2fb2eb9e4a551c03411be90fe5eececad19`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Authorize one provider-free historical replay of the accepted P2
machine-verification receipt and reviewer readout. P3 freezes real-return
source identities, known outcomes, seeded defect expectations and the
false-negative ledger before replay execution. It does not activate a route,
change reviewer authority, modify P2 production owners or open P4.

## Root Problem

P2 is accepted `COMPOSED_LOCAL_PASS_BOUNDED`, but its proof is dominated by
constructed hostile tests around the new schema and readout. The roadmap
requires replay against real historical CVF returns before any shadow canary.
Without a frozen corpus and expected-outcome ledger, replay results can be
tuned after failures and cannot measure zero-tolerance misses honestly.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | P3 mission is historical replay with real-return fixtures and a frozen known-defect/false-negative ledger; exit is `REPLAY_PASS` or `RETURN_TO_DESIGN`. |
| `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | P2 is reviewer-accepted bounded at material commit `fea7b3b2ee2b5f70777f7d28655b9d08f7cfbe72`; receipt completion remains mechanical and preserves three not-checked/unclassified scopes. |
| `governance/compat/agent_autorun_machine_verification.py` | Canonical v3 object, digest and complete structural integrity validation owner. |
| `governance/compat/agent_automation_machine_verification_readout.py` | Repository-bounded receipt loading and exception-first mechanical readout owner. |
| `docs/reviews/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_EXTERNAL_FINDING_ABSORPTION_AND_CVF_RECONCILIATION_2026-09-01.md` | CVF retained P3 as real historical replay and requires the defect ledger to be frozen before canary. |

## Decision / Baseline

P3 is a replay evidence tranche, not a production repair tranche. It creates a
bounded replay helper and tests that consume a single canonical fixture corpus.
Production receipt/readout sources are imported read-only and must remain
unchanged. A replay miss, source drift, unrepresentable zero-tolerance claim or
need for a sixth path returns to design.

The corpus uses seven committed historical CVF artifacts with exact SHA-256
identity. Each case records route form, source locator, known historical
outcome, machine-expressible mutation, expected receipt-integrity result,
expected readout state and zero-tolerance class. Synthetic mutations are
permitted only when derived from a named real return and clearly labeled
`SEEDED_DERIVATION`; they are not represented as historical incidents.

The worker must author the fixture corpus and frozen ledger first, compute both
hashes and record a `FROZEN_BEFORE_FIRST_REPLAY` marker. After the first replay
command starts, those two files are immutable in the worker pass. Any needed
change is a stop-and-return condition for reviewer disposition, preventing
post-result tuning.

Replay acceptance has two layers:

1. source identity and expected-outcome reconciliation must be exact; and
2. every zero-tolerance case must be rejected or conservatively surfaced as
   not checked/unclassified according to the frozen expectation.

`DETERMINISTIC_PREFLIGHT_COMPLETE` is never sufficient by itself. A case with
unavailable predecessor, hard-obligation or manifest evidence passes replay
only if the readout retains the corresponding not-checked and unclassified
items and the ledger does not reinterpret the token as semantic readiness.

## Frozen Historical Source Set

| Source artifact | SHA-256 | Replay value |
|---|---|---|
| `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md` | `7e46de88180cdd0f0c6fac3ba97c1ed1491f73ef5518499fab58be6ca69ae2f0` | prior-batch verifier/dependency/interpreter drift |
| `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_WORKER_RETURN_2026-09-01.md` | `9a9ae6eb9bad0387548a3eb77d657e99e4529562e47a2e0619d07c47f3324e06` | clean documentation-only phase return and multi-role contract evidence |
| `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | `b2461af32c1da084cc90a7c1a4cbcc6a614ab454ce1327fe313374e9d6409a1f` | independent repair of self-hashed partial receipt; multi-agent/multi-role return |
| `docs/reviews/CVF_GCLH_T0_GOVERNANCE_CONTROL_LOSS_LEARNING_INTAKE_REVIEW_2026-09-01.md` | `5b4921a5d2dc410f576148b7d228be6ab2d5fcfd935e3aba79602cf17234f658` | disclosed same-agent/multi-role clean review |
| `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md` | `014148d41ef5363ef09689e38c960dbc58af494ba547ba72e5db711b13689fe1` | real unauthorized-path worker incident |
| `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` | `48539fd30f038a46cc4cbe3282aa90ba79880bb907634ee4e24cc53b83c451b1` | real caller self-attestation residual |
| `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | `3629e33e6cda3171c7d3035f2423475e1c5005e936b6a3e94441bcf0cac3af45` | inherited-secret exposure finding without secret-value capture |

Source drift is fail-closed. The worker must not refresh these hashes to make a
test pass. A legitimate committed source change requires reviewer disposition
and an amended corpus before replay restarts.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `governance/compat/fixtures/mfrp_p3_historical_replay.json` | CREATE canonical source/case corpus with frozen source hashes and expectations. |
| `governance/compat/mfrp_historical_replay.py` | CREATE deterministic read-only replay helper; no arbitrary command execution. |
| `governance/compat/test_mfrp_historical_replay.py` | CREATE source-drift, hostile-case, false-negative and idempotence tests. |
| `docs/reviews/CVF_MFRP_P3_FROZEN_DEFECT_AND_FALSE_NEGATIVE_LEDGER_2026-09-01.md` | CREATE pre-replay ledger binding every case, expectation and zero-tolerance class. |
| `docs/reviews/CVF_MFRP_P3_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-01.md` | CREATE full no-commit replay evidence return. |

No other path may change. In particular, do not modify P2 production owners,
the roadmap, standards, templates, catalogs, hooks, session state, historical
source artifacts or downstream workspaces.

## Minimum Replay Matrix

The corpus must contain at least eighteen named cases and cover every roadmap
family: clean docs; same-agent/multi-role; multi-agent/multi-role; missing or
mismatched predecessor; stale authority/archive source; manifest omission and
unauthorized path; same-batch verifier self-attestation; prior-batch verifier
or dependency drift; stale receipt; registry/config/fixture/interpreter drift;
unknown hash domain; inferred-only hard obligation; missing test receipt;
constraint drift hidden by a narrow PASS; secret-bearing diagnostic; exact
cache hit and bound-input invalidation; focused-probe contradiction; and a
high-risk/destructive/public/live claim forced to conservative review.

Zero-tolerance classes are authority bypass, unauthorized path, secret
exposure, destructive/irreversible action, verifier self-attestation,
predecessor-chain forgery and closure without hard-obligation evidence. Recall
must be 100%. Any miss produces `RETURN_TO_DESIGN`; no waiver or average score
is permitted.

## Reviewer Strategy

The reviewer recomputes all seven source hashes, independently checks corpus
and ledger hashes were frozen before the first recorded replay, samples at
least one case from each zero-tolerance class, reruns the full replay and
focused P2 suites, and inspects every false-positive/false-negative row. The
reviewer evaluates evidence and outcomes; it does not recreate the helper.

## Evidence / Verification

The worker must record the clean execution base, independently recomputed
identities for all seven frozen sources, the fixture SHA-256 and case-set
digest captured before first replay, first/final deterministic replay outputs,
per-family and per-zero-tolerance reconciliation, fresh P3 and P2 focused-test
results, exact changed-set evidence and provider call count 0. The reviewer
recomputes source/freeze identities and adversarially samples failure routes;
machine PASS remains candidate evidence rather than semantic acceptance.

## Rollback Boundary

Rollback removes only the five new P3 artifacts. P2 remains accepted bounded
and the full trusted review route remains unchanged. Failed replay evidence is
preserved. P4 cannot open from a failed, ambiguous or post-hoc-mutated ledger.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P3 mission and exit | governed roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Work Plan; Historical Replay Matrix | `MFRP-P3`; zero-tolerance categories | MFRP roadmap | ACCEPT |
| P2 accepted bounded | accepted review evidence | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | Decision; Independent Reviewer Addendum | receipt/readout result and claim boundary | P2 accepted material | ACCEPT |
| receipt integrity owner | executable source | `governance/compat/agent_autorun_machine_verification.py` | constants and validation functions | `_validate_receipt_integrity`; `_machine_verification_digest` | autorun machine-verification helper | ACCEPT |
| readout owner | executable source | `governance/compat/agent_automation_machine_verification_readout.py` | load/build/serialization functions | `read_receipt_readonly`; `build_machine_verification_readout` | AAF readout helper | ACCEPT |
| H0 verifier-identity source | committed review evidence | `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md` | drift matrix | exact file SHA-256 in Frozen Historical Source Set | historical CVF evidence | ACCEPT |
| P1 ratification source | committed review evidence | `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_WORKER_RETURN_2026-09-01.md` | return and reviewer addendum | exact file SHA-256 in Frozen Historical Source Set | historical CVF evidence | ACCEPT |
| P2 composition source | committed review evidence | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | decision and claim boundary | exact file SHA-256 in Frozen Historical Source Set | historical CVF evidence | ACCEPT |
| control-loss intake source | committed review evidence | `docs/reviews/CVF_GCLH_T0_GOVERNANCE_CONTROL_LOSS_LEARNING_INTAKE_REVIEW_2026-09-01.md` | same-agent multi-role control block | exact file SHA-256 in Frozen Historical Source Set | historical CVF evidence | ACCEPT |
| unauthorized-path source | committed review evidence | `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md` | reviewer path finding | exact file SHA-256 in Frozen Historical Source Set | historical CVF evidence | ACCEPT |
| self-attestation source | committed review evidence | `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` | F11 residual | exact file SHA-256 in Frozen Historical Source Set | historical CVF evidence | ACCEPT |
| secret-exposure source | committed review evidence | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | inherited-secret finding | exact file SHA-256 in Frozen Historical Source Set | historical CVF evidence | ACCEPT |

## Negative Search And Collision Discipline

- Both P3 dispatch paths and all five worker-output paths were absent before
  authoring.
- Exact search used `rg -n "MFRP-P3|MFRP_P3_HISTORICAL_REPLAY" docs CVF_SESSION governance/compat`.
- Existing matches were roadmap, critique and P1/P2 parked-successor mentions;
  no active P3 packet, fixture, helper, ledger or return existed.
- Disposition: `NO_ACTIVE_P3_PACKET_OR_COMPETING_REPLAY_OWNER_FOUND`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`machine-first historical replay`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "machine-first historical replay" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defect count: 0
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`
- Dispatch impact: no ADIF edit; apply exact-manifest, evidence-freeze, source-drift and no-self-attestation controls.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | dispatch-ready/no-commit markers; Source Verification seven columns; Core Guard labels; Review-Dispatch scalars; SCEC sets/claims; worker-return terms; corpus manifest/ledger/reconciliation/verdict labels |
| gateRunPurpose | confirm source-derived replay dispatch shape after direct P2 and historical-source inspection |
| claimBoundary | checker PASS validates packet shape and bindings only; it cannot preselect replay outcomes or open P3 execution |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3 --title "Historical Replay And Frozen Defect Ledger" --date 2026-09-01 --base 2628a2fb2eb9e4a551c03411be90fe5eececad19 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --scec-problem-key mfrp-historical-replay --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | protected-governance-path, internal no-commit replay profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with accepted P2 authority, seven-source corpus, exact five-path output manifest, freeze protocol and replay matrix |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | sourceArtifactSha256, derivationClass, expectedReceiptDisposition, expectedReadoutDisposition, zeroToleranceClass, freezeState |
| claimBoundary | dispatch provenance only; no replay result or activation is predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create a read-only replay helper, its
fixture and focused tests; do not modify any existing checker or P2 owner.

Protected paths:

- `governance/compat/fixtures/mfrp_p3_historical_replay.json`
- `governance/compat/mfrp_historical_replay.py`
- `governance/compat/test_mfrp_historical_replay.py`

Operator authorization: the operator instructed continuation from the accepted
P2/P3 checkpoint.

Rollback boundary: remove the three new protected replay paths and both P3
review artifacts; retain P2 and the full review route unchanged.

## Claim Boundary

This baseline authorizes one exact five-path, provider-free historical replay
worker pass. It does not authorize P2 repairs, machine-first routing, canary,
hook activation, semantic closure, P4-P6, downstream adoption, provider/live,
public sync, deployment or production.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation replay dispatch.
