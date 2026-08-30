# CVF GC-018 Baseline - Detached External-Agent Implementation Return And Local Promotion

Memory class: governed-dispatch-baseline

docType: baseline

Status: CONSUMED_BY_REVIEWER_ACCEPTANCE_P0_P3_P4_CHECKPOINTED

Batch ID: DEAR-LP-R1

Dispatch base head: c8483065c

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

Worker target: delegated worker role

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one consolidated no-commit implementation assignment for phases P0
through P3 of DEAR-LP: extend the existing external-agent round-trip owners so
a detached implementation proposal returns manifest-bound real files while
remaining non-authoritative until local verification and promotion review.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id DEAR-LP-R1 --title "Detached External-Agent Implementation Return And Local Promotion" --date 2026-08-30 --base c8483065c --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-surface EXTERNAL_AGENT_CLI_MCP --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --stdout` |
| generatedProfile | mcp-cli-adapter plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced every placeholder with the selected roadmap scope, current-source evidence, exact owner paths, P0-P3 controls, pilot checkpoint and claim boundary. |
| checkerReadAheadConfirmation | Applicable checker sources listed below were inspected before this artifact was written. |
| docOnlyNewFields | No new baseline schema fields. |
| claimBoundary | Dispatch authorization only; no detached return, local promotion, runtime use, pilot, provider, public or production proof. |

## Authority And Decision

The operator selected the DEAR-LP roadmap on 2026-08-30 after its fresh
four-part value gate passed. DSH-WRA-R1 has bounded local reviewer acceptance;
its unrecoverable original pre-edit observation is waived only as low-value
historical evidence and is not rewritten as proof.

This baseline releases D4 for one consolidated worker assignment covering P0
through P3. D5 remains an operator checkpoint. No detached pilot, credential,
provider call, external effect, promotion decision, commit, push or public
projection is authorized.

## Decision

Dispatch one no-commit worker for P0-P3. Preserve P4/P5 inside the same parent
roadmap but stop at the operator checkpoint before any pilot or external
effect. Reviewer/closer retains acceptance, commit and continuity authority.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| DSH-WRA-R1 local closure | `docs/reviews/CVF_DSH_WRA_R1_WHOLE_REPOSITORY_ABSORPTION_AND_RUNTIME_REALIZATION_WORKER_RETURN_2026-08-30.md` records bounded reviewer acceptance and the exact historical-only waiver | local reviewer acceptance with truthful corpus maturity | ACCEPT |
| DEAR-LP value gate | `docs/roadmaps/CVF_DETACHED_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_ROADMAP_2026-08-30.md`, Fresh Four-Part Value Gate | all four gates PASS and operator selects roadmap | ACCEPT |
| Deterministic implementation authority | same roadmap, Design Control Gate D1-D4 | fresh GC-018 plus consolidated no-commit work order | ACCEPT |
| Representative pilot authority | same roadmap, Design Control Gate D5 | separate operator checkpoint after deterministic P0-P3 proof | HOLD_PILOT_CHECKPOINT |

## Scope

Authorized outcomes:

- current-owner and compatibility reconciliation for protocol 1.2.0;
- additive execution-class, detached proposal mode, authority object, return
  status and local-verification semantics;
- strict proposal-tree and target-map validation;
- local-only promotion receipt contract and rejection of any externally
  fabricated equivalent;
- independent state-vector and derived completion projection;
- provider-free deterministic, adversarial, concurrency and idempotence proof;
- permanent `DOCS_ONLY_FALSE_COMPLETION` regression coverage;
- a bounded pilot packet and explicit stop at the operator checkpoint.

The worker must enrich current owners. It must not create a parallel protocol,
copy a proposed return into CVF source, issue a local promotion decision, run a
detached pilot, call a provider or open another tranche.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current local packet helper, validator and reviewer flow | worker may implement P0-P3 under exact path ownership but cannot self-review, promote, commit or run external effects | current protocol/helper/tests plus paired work order | shared-workspace worker implementation is separate from later detached-agent return authority | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | task capsule and detached return-package contract | external output is `EXTERNAL_PROPOSAL`, never CVF SOT; one implementation-worker invocation is admitted, but pilot use remains checkpointed | selected roadmap and strict return validation design | contract and validator only; no automatic promotion, CLI/MCP runtime interception or pilot authorization | `CONTRACT_ONLY` |

## Current Runtime Freshness Verification

Current source inspection on 2026-08-30 confirms protocol version `1.2.0`,
five legacy task modes, fixed legacy expected-return status and the existing
`create_capsule`, `create_capsule_offline` and `validate_return` owners. Exact
search across the current protocol owner roots returned zero matches for the
new detached implementation-proposal and local-promotion tokens recorded in
the paired work order. This proves an owner-local delta candidate, not runtime
or pilot behavior.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | external-agent protocol contract -> existing task-capsule/helper owners -> detached proposal remains non-authoritative -> local reviewer-controlled disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py` |
| Owner surface | `docs/reference/external_agent_review/`; `scripts/external_agent_packet.py` |
| Disposition | ADAPT into existing owners for P0-P3 only; HOLD detached pilot and every promotion decision |
| Claim boundary | This baseline authorizes contract and deterministic local implementation only. It does not absorb external returned content, execute a pilot/provider/network action, promote files, or establish runtime/public/production readiness. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Current protocol version is 1.2.0 | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | Current Protocol Identity | `1.2.0` | protocol representation contract | ACCEPT |
| Capsule has five legacy modes and fixed legacy return status | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | task working-mode properties | `workingMode`; `expectedReturnStatus` | task capsule schema | ACCEPT |
| Existing helper owns capsule generation and return validation | SOURCE_BEHAVIOR | `scripts/external_agent_packet.py` | current function definitions | `create_capsule`; `create_capsule_offline`; `validate_return` | external-agent packet helper | ACCEPT |
| Current return authority fields are manifest-level | LITERAL_INVARIANT | `scripts/external_agent_packet.py` | return validation expectation | `artifactClass`; `authorityStatus`; `secretsReturned` | `validate_return` | ACCEPT |
| Current focused suite is the compatibility baseline | TEST_BASELINE | `scripts/test_external_agent_packet.py` | current test module | `test_validate_return_pass_and_semantic_failure` | external-agent packet tests | ACCEPT |
| Selected roadmap requires one consolidated P0-P3 implementation before pilot | AUTHORITY | `docs/roadmaps/CVF_DETACHED_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_ROADMAP_2026-08-30.md` | Work Plan; Design Control Gate | `DEAR-LP-R1`; `D5 pilot authority` | DEAR-LP roadmap | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Dispatch artifact paths | `Test-Path` returned False for the planned baseline, work order and worker return before authoring | NEW_PATHS_CONFIRMED |
| New contract token collision | `rg -n -e 'DETACHED_EXTERNAL_AGENT\|EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION\|PROPOSED_TARGET_MAP\|LOCAL_PROMOTION_RECEIPT\|DOCS_ONLY_FALSE_COMPLETION\|automaticPromotionAllowed\|ownerPromotionState\|representativeUseProofState' docs/reference/external_agent_review scripts governance/compat` returned exit 1 and zero matches | ZERO_CURRENT_COLLISIONS |
| Owner decision | New semantics extend the existing protocol/schema/helper/test owners; a parallel protocol or return-authority file is forbidden | ENRICH_EXISTING |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-agent-protocol-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external-agent-protocol-implementation" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No resolver-specific defect route; general orientation, literal, convergence and source-verification controls remain binding. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Dual Agent Surface Matrix`; `ADIF Defect Registry Disclosure`; `Checker Source Read-Ahead Block`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | Confirmation and dispatch evidence after source and checker inspection, not first discovery. |
| claimBoundary | Read-ahead establishes packet shape only; it does not prove implementation, external-agent conformance, promotion, runtime use or pilot behavior. |

## Acceptance Criteria

1. Current protocol owners are enriched rather than duplicated.
2. P0-P3 semantics and all roadmap deterministic/adversarial cases are
   implemented and provider-free tests pass.
3. The strongest detached validator success remains local-verification
   readiness and all direct external-to-SOT transitions fail closed.
4. Legacy 1.2 modes remain readable or a source-backed major-version decision
   is returned for reviewer approval.
5. The worker leaves all changes uncommitted and stops before P4.

## Evidence / Verification

Dispatch readiness requires the paired work order source-verification matrix,
exact collision search, current hashes, ADIF resolver result and passing
pre-dispatch autorun gate. Worker evidence requires both focused pytest modules,
Python compile proof, file-size guard, pre-implementation autorun and the full
worker-return fast gate.

## Stop Conditions

Stop and return `BLOCKED_WITH_REASON` if current compatibility cannot be
preserved, a critical invariant requires a new protected checker, any allowed
path cannot be reconciled with its pre-existing dirty content, or completion
would require a pilot, provider call, credential, public mutation, destructive
action, commit or scope expansion.

## Claim Boundary

This baseline authorizes P0-P3 local implementation and deterministic proof
only. It does not authorize or claim detached pilot success, local promotion,
CVF SOT integration, representative use, provider/live behavior, public export,
commit, push, deployment, production readiness or absorption completion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; no public-sync path or public commit is
authorized.
