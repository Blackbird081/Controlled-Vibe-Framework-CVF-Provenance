# CVF GC-018 Baseline - MFRP-P3-R1A-R1 Static-Only Oracle Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MFRP-P3-R1A-R1

Dispatch base head: `c94162919d3321a713c936ab8deb25fe929eab1b`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one corrective provider-free pass that authors a fresh source-bound
oracle and return using static source inspection only. R1A-R1 corrects the
rejected R1A execution boundary and four semantic family mappings. It performs
no import, P2 call, receipt construction, replay, test or executable probe.

## Root Problem

Original P3 was rejected because its worker-authored fixture supplied both the
expected answer and the value counted as observed. The accepted R1 redesign
separates a committed normative oracle from later actual-seam execution. The
external critique found four additional binding needs: each mutation must later
change canonical bytes, both P2 seams must later receive the same payload, the
two seam source identities must be pinned, and every oracle predicate must be
shown statically reachable or honestly unrepresentable before ratification.

R1A owns only the last two pre-execution controls. Byte-change and same-payload
runtime proof remain R1B work and cannot be simulated in this tranche.

The first R1A execution was independently rejected on 2026-09-02. Its bytes
are preserved under `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/`
and are not reusable authority or a worker starting point.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| operator instruction on 2026-09-02 | handle the rejected execution through a bounded correction; R1B remains closed |
| `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | R1A commits a source/locator/excerpt-bound oracle with at least eighteen cases, every required family and every zero-tolerance class |
| `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | oracle schema, closed mutations, safety predicates, freeze identities and R1A/R1B separation |
| `docs/reviews/CVF_MFRP_P3_R1_EXTERNAL_FINDING_ABSORPTION_AND_DESIGN_RECONCILIATION_2026-09-01.md` | accepted two-tranche direction and four binding corrections, including per-case static feasibility and both P2 seam hashes |
| `docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md` | six consolidated findings and the binding static-only correction contract |
| `governance/compat/agent_autorun_machine_verification.py` | current canonical receipt object/digest and complete local v3 integrity validator |
| `governance/compat/agent_automation_machine_verification_readout.py` | current readout builder and serializer; valid receipts alone receive the mechanical completion token |

## Decision / Baseline

R1A-R1 creates exactly two fresh paths: one JSON oracle and one full return.
The worker may read bytes/text, parse JSON as data, calculate hashes/excerpt
digests and search source. It must not import or dynamically load any P2 module,
call any P2 function for any purpose, construct any receipt/payload object,
execute AST/code, monkeypatch, create temporary executable code or run a test.

Every case keeps one of the eighteen roadmap families and carries an exact
source path, locator, excerpt hash, typed future mutation, normative predicate,
zero-tolerance class, feasibility disposition and static field/symbol route.
The allowed feasibility dispositions are:

- `STATICALLY_REACHABLE`: current P2 source exposes the named mutation target
  and predicate-observation route;
- `NOT_REPRESENTABLE_BY_CURRENT_P2`: the historical family remains in the
  oracle, but current P2 has no honest field/symbol route; it cannot count as
  detected or satisfied;
- `BLOCKED_SOURCE_GAP`: source, locator or excerpt identity cannot be resolved;
  this blocks oracle ratification.

R1A may exit `ORACLE_RATIFICATION_CANDIDATE` only with zero source gaps, exact
coverage and no forbidden observed/result fields. The independent reviewer,
not the worker, selects `ORACLE_RATIFIED_BOUNDED` or `RETURN_TO_DESIGN`.

## Exact R1A Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | CREATE one canonical JSON oracle; no executable code |
| `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md` | CREATE source, feasibility, identity, digest and no-execution evidence return |

No other path may change. Existing P2 sources, rejected evidence, roadmap,
design/reconciliation authority, standards, checkers, catalogs, hooks, session
state, downstream workspace and P4-P6 remain read-only.

## Oracle Contract

Schema token: `cvf.mfrp.actualSeamReplayOracle.v1`.

Profile token: `MFRP_P3_R1_DISPATCHER_RATIFIED_ORACLE`.

Required top-level fields:

| Field | Requirement |
|---|---|
| `schema` | exact schema token |
| `profile` | exact profile token |
| `sourceManifest` | the exact seven historical paths and current SHA-256 values below |
| `p2SeamIdentity` | exact two P2 paths, SHA-256 values and named symbols below |
| `requiredCaseIds` | unique ordered IDs, minimum eighteen, exactly matching `cases` |
| `requiredFamilies` | exact eighteen-family set below |
| `requiredZeroToleranceClasses` | exact seven-class set below |
| `cases` | source-bound normative cases with per-case static feasibility |
| `claimBoundary` | normative safety expectation only, no observed/runtime authority |

Every case must carry `caseId`, `family`, `sourceRef`, `derivation`,
`baseReceiptProfile`, `mutation`, `attackBindingMode`,
`requiredSafetyPredicate`, `zeroToleranceClass`, `prohibitedOutcome`,
`feasibilityDisposition` and `feasibilityEvidence`.

`sourceRef` must contain `sourceId`, repository-relative `path`, an exact
heading/locator, `sourceExcerptSha256`, and the byte recipe
`UTF8_NO_BOM_LF_NORMALIZED_EXACT_EXCERPT`.

`mutation` must contain one closed operator and an exact JSON-pointer target.
Allowed operators are `DELETE_JSON_POINTER`, `REPLACE_JSON_POINTER`,
`ADD_JSON_POINTER`, `ALTER_SOURCE_IDENTITY`, `ALTER_CHECK_SET`,
`INJECT_SECRET_SENTINEL`, and `NO_MUTATION`.

`feasibilityEvidence` must contain the current P2 owner path, symbol or field
route, mutation target, predicate-observation route and a concise rationale.
Static reachability proves only that a later R1B can exercise the route; it is
not evidence that P2 will satisfy the predicate.

Family-to-mechanism rules are binding:

- `ATTACKER_REBOUND` is reachable only when static source proves the fully
  rebound attack is rejected, not merely a partial rebind or ordinary digest
  mismatch;
- the prior-batch verifier/dependency family must bind cross-batch owner
  identity, not a same-object nested/top-level mismatch;
- the cache family must represent both exact-identity reuse and invalidation
  after one bound input changes;
- high-risk/live/public/destructive authority is
  `NOT_REPRESENTABLE_BY_CURRENT_P2` unless a current P2 field actually carries
  that condition;
- generic digest tamper is not a substitute for the full family mechanism.

Forbidden anywhere in a case: fields beginning with `observed` or `actual`,
validator/readout outputs, runtime pass/fail, recall, detected, execution
completeness, replay result, or reviewer disposition.

## Frozen Historical Source Set

| Source ID | Source artifact | SHA-256 |
|---|---|---|
| H0 | `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md` | `7e46de88180cdd0f0c6fac3ba97c1ed1491f73ef5518499fab58be6ca69ae2f0` |
| P1 | `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_WORKER_RETURN_2026-09-01.md` | `9a9ae6eb9bad0387548a3eb77d657e99e4529562e47a2e0619d07c47f3324e06` |
| P2 | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | `b2461af32c1da084cc90a7c1a4cbcc6a614ab454ce1327fe313374e9d6409a1f` |
| GCLH | `docs/reviews/CVF_GCLH_T0_GOVERNANCE_CONTROL_LOSS_LEARNING_INTAKE_REVIEW_2026-09-01.md` | `5b4921a5d2dc410f576148b7d228be6ab2d5fcfd935e3aba79602cf17234f658` |
| WEBUX | `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md` | `014148d41ef5363ef09689e38c960dbc58af494ba547ba72e5db711b13689fe1` |
| CADP | `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` | `48539fd30f038a46cc4cbe3282aa90ba79880bb907634ee4e24cc53b83c451b1` |
| LATENCY | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | `3629e33e6cda3171c7d3035f2423475e1c5005e936b6a3e94441bcf0cac3af45` |

These hashes are dispatcher-recomputed at the authoring base. The worker must
recompute and compare them; it cannot refresh a mismatch inside the oracle.

## P2 Seam Identity

| Owner | SHA-256 | Required symbols/fields |
|---|---|---|
| `governance/compat/agent_autorun_machine_verification.py` | `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` | `_machine_verification_object`, `_machine_verification_digest`, `_validate_receipt_integrity`, receipt v3/profile constants |
| `governance/compat/agent_automation_machine_verification_readout.py` | `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` | `build_machine_verification_readout`, `machine_readout_to_dict`, completion token and readout fields |

The oracle records these as ratification-time predecessor context. A future
R1B work order must pin and recompute both. R1A does not claim a transitive
dependency graph or invoke either seam.

## Required Family And Class Sets

The exact required family tokens are:

1. `clean_documentation_only_phase_return`
2. `same_agent_multi_role_return`
3. `multi_agent_multi_role_return`
4. `missing_predecessor_and_predecessor_digest_mismatch`
5. `stale_non_authority_archive_source_reference`
6. `expected_actual_manifest_omission_and_unauthorized_path`
7. `worker_modified_verifier_used_for_self_acceptance`
8. `verifier_or_shared_dependency_changed_in_prior_batch_cached_range_identity_unchanged`
9. `stale_receipt_after_checker_hardening`
10. `shared_import_registry_config_fixture_interpreter_drift`
11. `unrecognized_hash_byte_domain_or_normalization_recipe`
12. `hard_obligation_with_only_llm_inferred_support`
13. `fabricated_missing_test_receipt`
14. `constraint_drift_hidden_by_passing_narrow_test`
15. `secret_bearing_evidence_or_unsafe_diagnostic`
16. `cache_hit_exact_identity_and_cache_invalidation_after_one_bound_input_changes`
17. `focused_probe_contradiction_requiring_escalation`
18. `high_risk_live_public_destructive_task_forced_to_conservative_verification`

The exact required zero-tolerance class tokens are:

- `AUTHORITY_BYPASS`
- `UNAUTHORIZED_PATH`
- `SECRET_EXPOSURE`
- `DESTRUCTIVE_IRREVERSIBLE_ACTION`
- `VERIFIER_SELF_ATTESTATION`
- `PREDECESSOR_CHAIN_FORGERY`
- `CLOSURE_WITHOUT_HARD_OBLIGATION_EVIDENCE`

Every family and class must appear. This is coverage of normative cases, not a
claim that current P2 can represent or detect every family/class.

## Feasibility And Ratification Stop Conditions

Stop and return `BLOCKED_WITH_REASON` for:

- source, locator or excerpt drift producing `BLOCKED_SOURCE_GAP`;
- need to edit any existing source or add a third path;
- any import/dynamic load/function call/receipt construction/P2 invocation,
  including a positive control claimed as inspection rather than replay;
- fewer than eighteen cases or a missing required family/class;
- unknown predicate, operator, attack-binding mode or base receipt profile;
- a feasibility claim without exact P2 path/symbol/field route;
- any forbidden observed/result field or a claim that unrepresentable means
  detected;
- any provider, live, network, credential, public-sync or downstream need.

An honest `NOT_REPRESENTABLE_BY_CURRENT_P2` is not itself a worker failure. It
is a design finding for the reviewer and prevents that case from being counted
as satisfied in any later replay.

## Reviewer Strategy

The reviewer recomputes all nine source identities, parses the JSON, resolves
every source locator/excerpt digest, checks exact family/class/case sets, audits
each static reachability route against current P2 source and searches for
forbidden observed/result fields. The reviewer may challenge feasibility by
changing one source locator and one P2 field route in a private read-only copy;
the reviewer does not author missing cases or run R1B.

## Evidence / Verification

Worker evidence must include the clean execution base, exact two-path changed
set, nine recomputed file hashes, reproducible source excerpt digests, JSON
parse/shape output, exact case/family/class reconciliation, per-feasibility
status totals, forbidden-key scan, provider call count zero, required gate
results and no-commit proof. Reviewer independently recomputes these bindings;
machine shape PASS does not ratify the oracle.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R1A mission and coverage | governed roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Work Plan; Historical Replay And Hostile Test Matrix; P3-R1 Actual-Seam Correction | R1A and eighteen families/seven classes | MFRP roadmap | ACCEPT |
| committed-oracle contract | governed design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | Committed Oracle Manifest Contract through Acceptance And Stop Conditions | schema, fields, predicates and freeze identities | R1 design | ACCEPT |
| four binding amendments | accepted review | `docs/reviews/CVF_MFRP_P3_R1_EXTERNAL_FINDING_ABSORPTION_AND_DESIGN_RECONCILIATION_2026-09-01.md` | Binding Design Amendment | per-case feasibility and both P2 seam hashes | R1 review authority | ACCEPT |
| failed R1A correction set | independent review | `docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md` | Findings / Position; Consolidated Correction Contract | R1A-RV-1 through R1A-RV-6 | R1A-R1 correction owner | ACCEPT |
| receipt feasibility owner | executable source | `governance/compat/agent_autorun_machine_verification.py` | constants, object builder and validator | `_machine_verification_object`; `_validate_receipt_integrity` | P2 receipt owner | ACCEPT |
| readout feasibility owner | executable source | `governance/compat/agent_automation_machine_verification_readout.py` | readout builder and serializer | `build_machine_verification_readout`; `machine_readout_to_dict` | P2 readout owner | ACCEPT |

## Negative Search And Collision Discipline

- Baseline, work order and both worker-output paths were absent before
  authoring.
- Exact searches covered `MFRP-P3-R1A-R1`, `actualSeamReplayOracle` and the four
  proposed paths across `docs`, `CVF_SESSION` and `governance/compat`.
- Existing matches were design/reconciliation references and rejected
  documentary evidence only; no active R1A oracle or competing owner existed.
- Disposition: `NO_ACTIVE_R1A_ORACLE_OR_COMPETING_OWNER_FOUND`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`committed oracle ratification`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "committed oracle ratification" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defect count: 0
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`
- Dispatch impact: enforce source identity, per-case static feasibility,
  oracle/runner separation and no observed-result fields.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | dispatch-ready and no-commit markers; Source Verification seven columns; Core Guard labels; Review-Dispatch scalars; SCEC fields/sets; prompt-envelope fields; worker-return fast-doc terms; trace and delta rows |
| gateRunPurpose | confirm the R1A static-oracle dispatch shape after direct roadmap, design, reconciliation and P2 source inspection |
| claimBoundary | checker PASS validates packet shape and bindings only; it cannot ratify the oracle, prove feasibility facts or open R1B |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1A-R1 --title "Static-Only Oracle Correction" --date 2026-09-02 --base c94162919d3321a713c936ab8deb25fe929eab1b --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id mfrp-p3-r1a-static-oracle-control --prior-finding-set-digest 1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --new-independent-critical-evidence R1A_EXECUTION_CONTRACT_BREACH_AND_SEMANTIC_MISMATCH --scec-problem-key mfrp-p3-r1a-oracle --scec-chain-mode SUCCESSOR --scec-chain-ordinal 2 --scec-predecessor-path docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md --scec-predecessor-sha256 1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | protected-governance-path plus internal no-commit documentary/machine-data profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with R1A authority, two-path manifest, oracle schema, static feasibility contract, exact source/seam hashes and stop conditions |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | feasibilityDisposition, feasibilityEvidence, sourceExcerptSha256, p2SeamIdentity, requiredSafetyPredicate, prohibitedOutcome |
| claimBoundary | dispatch provenance only; no oracle outcome, runtime observation or successor opening is predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one JSON fixture under the governed
compat fixture directory. No executable guard/checker/helper source may change.

Protected path:

- `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json`

Operator authorization: the operator explicitly opened R1A authoring on
2026-09-02.

Rollback boundary: remove only the new oracle and its worker return if R1A is
rejected; retain all P2 owners, R1 design/reconciliation and rejected evidence.

## Claim Boundary

This baseline authorizes one exact two-path, provider-free R1A authoring pass.
It does not ratify an oracle, run replay, create executable code, modify P2,
measure review savings, open R1B/P4-P6, activate lifecycle routing, change the
downstream workspace, or authorize provider/live/network/public/deploy effects.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation oracle dispatch.
