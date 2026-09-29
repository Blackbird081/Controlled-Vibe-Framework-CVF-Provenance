# CVF GC-018 Baseline - ACEL G1 T2B Calibration Root Contract Architecture Reassessment

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T2B-CALIBRATION-ROOT-CONTRACT-ARCHITECTURE-REASSESSMENT

Dispatch base head: `762ec1be1ba13d8c6f2e1f3771d680038ac0b449`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer

Reviewer owner: Local orchestrator/reviewer

Worker target: one shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize one fresh documentation-only root-contract design from four Local
architecture decisions after T2A reached `STOP_REASSESS_ARCHITECTURE`. This is
not a repair of the rejected T2A outputs and does not authorize implementation.

## Architecture Decision

| Decision | Selected architecture | Rejected alternative |
|---|---|---|
| Fixture authority | immutable `HeldOutFixtureSetAuthority` issued before evaluation by the calibration-round decision owner; binds task class, partition/comparability identity, exact required members and authority hash; each candidate references the exact hash | candidate-authored or hash-only fixture declaration |
| Evidence topology | separate `requiredEvidence[]` and `supplementalEvidence[]`; only required evidence can affect admission, preference and regression binding | extras inside a field named required evidence |
| Canonicalization | new versioned profile using SHA-256 over UTF-8 RFC 8785 JCS canonical JSON, fixed named fields, deterministic array ordering and published positive/collision test vectors | delimiter joining or unspecified list hashing |
| Invalidation | immutable acceptance binding plus append-only `OperatingPointInvalidationReceipt`; current validity derives from the latest verified receipt and current-state observation | pretending a later readiness/budget change mutates an historical acceptance fingerprint |

The worker may refine field names but must not change these four decisions.

## Proposed Tranche

Open one documentation-only T2B tranche in which a single `INTERNAL_AGENT`
authors the human contract, its machine-readable manifest and the worker-return
packet. The tranche has no implementation, provider call or nested delegation
authority, and the ten parked G1 paths remain frozen inputs.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_R2_INDEPENDENT_REVIEW_2026-09-17.md` | SHA-256 `71c2d060e97ee752bd3d26a67712fee5b8a56abb471dcc6386164d609f40c750`; terminal `PARKED_ARCHITECTURE_REASSESSMENT_REQUIRED` | Local must select all four architecture choices before a fresh tranche | RELEASED_BY_THIS_BASELINE |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T2B-CALIBRATION-ROOT-CONTRACT-ARCHITECTURE-REASSESSMENT --title "ACEL G1 T2B Calibration Root Contract Architecture Reassessment" --date 2026-09-17 --base 762ec1be1ba13d8c6f2e1f3771d680038ac0b449 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_R2_INDEPENDENT_REVIEW_2026-09-17.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --root-cause-cluster-id NOT_APPLICABLE_INITIAL_DISPATCH --prior-finding-set-digest NOT_APPLICABLE_INITIAL_DISPATCH --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key acel-g1-t2b-root-contract-architecture --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | four Local architecture decisions, exact sources, three fresh output paths, ten-path freeze and no-delegation boundary |
| checkerReadAheadConfirmation | work-order dispatch, prompt envelope, SCEC, gate closeability, markdown, trace and Delta checkers |
| docOnlyNewFields | `HeldOutFixtureSetAuthority`; `requiredEvidence`; `supplementalEvidence`; canonical profile; `OperatingPointInvalidationReceipt` |
| claimBoundary | dispatch documentation only; no implementation/runtime/provider/live claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status; prompt placement; SCEC controlled values; closeability table fields; trace and Delta labels |
| gateRunPurpose | confirm packet conformance after architecture selection, not discover architecture |
| claimBoundary | checker conformance does not prove the selected design is correct |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified locator | Disposition |
|---|---|---|---|---|
| T2A is terminally rejected and requires architecture reassessment | REVIEW_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_R2_INDEPENDENT_REVIEW_2026-09-17.md` | Architecture Reassessment Requirement | ACCEPT |
| accepted G1 T1 design remains predecessor evidence, not implementation authority | DESIGN_AUTHORITY | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | SHA-256 `c8c1f6899e50513141e69113b8ac9faf37669b1fcd785bc2df3b88d8e894505b` | ACCEPT_WITH_REASSESSMENT |
| CVF has a source-backed JCS canonical-hash pattern with test-vector discipline | PATTERN_EVIDENCE | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | Invariant 5; SHA-256 `14709f0b7b302201c8f55d9a1b2146e147bbc90ccfb971154358e4cb62fed1e4` | ADAPT_PATTERN_ONLY |
| SOT3 profile ownership does not transfer to G1 | AUTHORITY_BOUNDARY | `docs/reference/sot_three_layer/README.md` | Kernel ownership table | ACCEPT |

## Negative Search And Collision Discipline

All paired baseline, work-order and three worker-output paths returned
`Test-Path=False` before authoring. Exact batch-ID/title search returned zero
matches. Therefore T2B is a fresh tranche, not a name collision or hidden T2A
repair.

## Evidence / Verification Boundary

Dispatch acceptance requires source-hash reconciliation, exact-path scope,
human/JSON parity and passing governed gates. Those facts establish only that
the selected architecture was represented faithfully. They do not prove a
future implementation, checker, empirical calibration or operating point.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private G1 architecture dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes only the paired work order and three fresh design
outputs. It does not accept or modify the ten untracked G1 evidence paths,
implement code, run calibration, invoke a provider, open G4/runtime, mutate
configuration, publish or deploy.
