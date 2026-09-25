# CVF GC-018 Baseline - ACEL AKOE-P3 Provider-Free Integrated Application Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-AKOE-P3

Dispatch base head: `b138dcf4ef0837d4304407d4f1b51fb4f32d8c90`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer/closer

Reviewer owner: Local reviewer/closer distinct from the worker phase

Worker target: shared-workspace `INTERNAL_AGENT` offline-integration-proof role

## Purpose

Authorize one bounded provider-free, reversible synthetic proof that composes
the six already-accepted AKOE input families through existing CVF owners. The
proof must keep judgment, proposal, execution, verification, acceptance, and
accountability visibly separate and return all work uncommitted for Local
review.

## Authorization / Decision

The operator said `next` on 2026-09-25 after AKOE-P2 closed bounded at material
commit `390ca4ce8c835d133da9df6b0bf500a91af15c0e` and continuity commit
`b138dcf4ef0837d4304407d4f1b51fb4f32d8c90`. This satisfies the roadmap's
fresh checkpoint only for authoring, committing, releasing, and executing the
exact paired P3 packet.

This baseline does not open AKOE-P4, common Local closure, a real provider or
external runtime, public sync, deployment, production action, or any new
runtime/package/authority owner.

## Scope

Allowed:

- build one deterministic synthetic scenario from current accepted owner APIs;
- exercise bounded judgment, one atomic candidate decision, full-scope artifact
  completion, restart/replay, non-authoritative projection, independent
  verification planning, evidence-backed human acceptance, and rejection;
- create one proof runner, one focused test, one generated evidence receipt,
  one corpus-registry source entry plus its generated aggregate, and one worker
  return;
- repair only those six worker-owned paths until focused and governed gates
  pass;
- use temporary local fixture directories that are removed by the test/runner.

Forbidden:

- changing any accepted P0/P1/P2 production owner, public export, package
  manifest, dependency, checker, hook, roadmap, dispatch artifact, session
  surface, or active handoff;
- treating judgment confidence, a proposal, a child notification, runtime
  completion, or operator projection as acceptance authority;
- invoking Jev, WikiSkill, HyperFrames, Unreal Agent, any model/provider,
  browser/network service, MCP/CLI external adapter, or live release path;
- installing dependencies, staging, committing, pushing, publishing,
  deploying, certifying, or opening a successor tranche.

## Baseline Invariants

1. The scenario is synthetic and provider-free; current CVF functions and
   schemas are the only executable owners.
2. Judgment binds exact state/candidate evidence and remains
   `EVIDENCE_ONLY`; it cannot approve its own proposal.
3. Exactly one candidate proposal is compared with an incumbent. Rejection
   restores the incumbent while preserving proposal/evaluation evidence.
4. Capped scheduling may limit concurrency but must not narrow the declared
   artifact graph or omit assembly verification.
5. Restart/replay preserves the same authority, scope, graph identity, and
   evidence chain; operator projection remains non-authoritative.
6. Execution success, independent verification, human acceptance, and
   accountable ownership are distinct terminal receipt fields.
7. Human acceptance is required only for the scenario's declared risk route
   and fails closed when evidence or rejection opportunity is absent.
8. The worker does not self-supply the independent Local reviewer result.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| AKOE roadmap | `docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md`, SHA-256 `3071c82365cad63dc4f7f6b1c9419f711e3a631b0f62b06edaf7019abe559361`, defines the eight-part provider-free P3 scenario | packet preserves all eight parts and no-production boundary | SATISFIED |
| AKOE-P1 closure | `docs/reviews/CVF_ACEL_AKOE_P1_HUMAN_CONTROL_AND_POSITIONING_RECONCILIATION_COMPLETION_2026-09-25.md`, SHA-256 `27d3c3dbbdddf425f6a7803aa2705c91613f20d238404f7e94d50eacb00ba29d`, commit `af0e9a199` | P3 must reuse, not reopen, the accepted human/positioning disposition | SATISFIED |
| AKOE-P2 closure | `docs/reviews/CVF_ACEL_AKOE_P2_R2_DURABLE_RUN_STORE_REVIEWER_CORRECTION_COMPLETION_2026-09-25.md`, SHA-256 `ff80b2c71a1972e9efd7eb145f115a4e4f7f96b248b41d6c737020cee9f471b4`, material `390ca4ce8`, continuity `b138dcf4e` | P3 may consume the corrected local durable owner only | SATISFIED |
| operator checkpoint | operator said `next` after continuity recorded P2 closed and held before P3 | authority is limited to this exact P3 packet and its internal execution | SATISFIED |
| dispatch continuity | paired packet must be materially committed and the active handoff must record its material SHA before worker edits | dispatcher completes release and runs the bound machine gate before handoff | SATISFIED_FOR_DISPATCH |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| bounded judgment is evidence-only and has complete/incomplete candidate-space rules | current implementation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | lines 72-74, 286-308, 491, 753, 833 | `candidateSpaceMode`; `noMatchOutcome`; `judgmentAuthority`; graders/admission functions | ASSF behavioral evaluation owner | ACCEPT |
| proposal decision exposes strict improvement and evidence-preserving rejection impact | current implementation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/proposal-impact-rollback.evidence.contract.ts` | lines 51-56, 78, 107-155 | `evaluateProposalImpactRollback`; `strictImprovement`; `rollbackImpact` | Learning Plane proposal evidence owner | ACCEPT |
| artifact completion requires exact scope and assembly verifier identity | current implementation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/artifact.completion.scope.contract.ts` | lines 47-65, 138-260 | `evaluateArtifactCompletionScope`; `assemblyVerifierId`; `scopePreserved` | MAO artifact-completion owner | ACCEPT |
| local restart/replay is available from the accepted durable store | current implementation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 114-264 | `MaoFileRunStore`; `createRun`; `resumeRun`; `appendEvent` | MAO durable-run-store owner | ACCEPT |
| workspace readout is an operator projection, not execution authority | current implementation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts` | lines 93-113, 149-224 | `buildOperationalOperatorProjection`; `MaoOperationalOperatorProjection` | MAO projection owner | ACCEPT |
| human-control/positioning constraints are accepted with no owner mutation | accepted Local decision | `docs/reviews/CVF_ACEL_AKOE_P1_HUMAN_CONTROL_AND_POSITIONING_RECONCILIATION_COMPLETION_2026-09-25.md` | Findings, Acceptance Receipt Assertion Matrix, Claim Boundary | P1 terminal disposition | Local reviewer/closer | ACCEPT |
| corrected durable behavior is accepted bounded | accepted Local decision | `docs/reviews/CVF_ACEL_AKOE_P2_R2_DURABLE_RUN_STORE_REVIEWER_CORRECTION_COMPLETION_2026-09-25.md` | Findings, Independent Review Probe, Decision | P2 terminal disposition | Local reviewer/closer | ACCEPT |

## Required Scenario Acceptance Matrix

| Proof facet | Required observation | Forbidden shortcut |
|---|---|---|
| judgment | exact state hash, candidate-space disposition, no-match behavior, `EVIDENCE_ONLY` | judgment approves action |
| proposal | one candidate versus incumbent and strict-improvement decision | multiple hidden proposals or mutation before decision |
| artifact graph | full declared graph retained under capped scheduling | completion inferred from child notification |
| execution/restart | exact identity survives local replay | projection or process return becomes truth |
| verification | artifact plus assembly verifier result | worker self-acceptance |
| human acceptance | evidence availability, decision opportunity, rejection authority, accountable owner | bare approval token |
| rejection | incumbent restored; raw evidence and learned knowledge retained | evidence deletion or state ambiguity |
| terminal receipts | separate execution, verification, acceptance, accountability fields | one aggregate success boolean |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| paired packet and return paths | `Test-Path` returned `False` for both packet paths and the worker return before authoring | CLEAR |
| packet identity search | exact command `rg -n "ACEL-AKOE-P3|Provider-Free Integrated Application Proof" docs CVF_SESSION AGENT_HANDOFF_V63_2026-09-18.md`; one expected roadmap owner at line 243 | CLEAR_EXPECTED_ROADMAP_OWNER |
| owner collision | all production responsibilities map to accepted existing owners; the new script is proof-only and not exported as runtime API | REUSE_EXISTING_OWNERS |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | provider-free synthetic local proof; no provider, live route, deployment, production behavior, or runtime-owner mutation is claimed |
| requiredFutureAction | any live/provider/production proof requires a fresh operator checkpoint and separate GC-018 packet |

## Evidence / Verification

- Paired packet author-fast and pre-dispatch autorun must pass before material
  commit.
- Material pre-commit must pass against the exact two-path dispatch batch.
- A later continuity commit must record the real P3 material SHA in the active
  handoff and regenerate active session projections.
- Dispatch release and bound pre-implementation gates must pass from the clean
  committed continuity head before the worker may edit any owned path.
- Worker evidence remains pending Local independent verification and acceptance.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| literalTokensReviewed | `DISPATCH_READY`; Source Verification table columns; task-routing JSON; convergence fields; closeability graph; `independentProbeRequired`; high-risk applicability declaration; trace labels; external/local binding |
| gateRunPurpose | confirm the completed packet after source/literal inspection; not first discovery or semantic acceptance |
| claimBoundary | static dispatch admission only; no P3 proof result, integration correctness, or closure is established |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`offline-integration-proof`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "offline-integration-proof" --role worker --lifecycle-phase implementation --max-results 12 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | exact manifest, authority separation, independent Local probe, and worker no-commit boundary remain mandatory |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded provider-free P3 proof.
Decision owner: Local. External research is closed; no public source question
or external implementation lane is opened.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md"}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-AKOE-P3 --title "ACEL AKOE-P3 Provider-Free Integrated Application Proof" --date 2026-09-25 --base b138dcf4ef0837d4304407d4f1b51fb4f32d8c90 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md --dependency docs/reviews/CVF_ACEL_AKOE_P2_R2_DURABLE_RUN_STORE_REVIEWER_CORRECTION_COMPLETION_2026-09-25.md --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key acel-akoe-p3-provider-free-integration --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition READY_WITH_EXECUTABLE_PROOF --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | generic worker initial dispatch with no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact P3 authority, owner, scenario, path, evidence, independence, and stop contracts |
| checkerReadAheadConfirmation | dispatch, routing, convergence, closeability, handoff, lifecycle, probe, transaction, external-routing, encoding, and prompt-envelope checkers inspected |
| docOnlyNewFields | Required Scenario Acceptance Matrix only |
| claimBoundary | dispatch provenance only; no worker result, live runtime, external action, or closure claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: P3 is private-provenance offline proof planning with no public-sync
remote, commit, artifact path, or publication authority.

## Claim Boundary

This baseline authorizes only one internal no-commit worker to create the exact
offline proof artifacts named by the paired work order. It does not certify
the proof, mutate accepted production owners, invoke an external system,
accept its own evidence, open P4/common closure, or authorize public,
provider/live, deployment, or production effects.
