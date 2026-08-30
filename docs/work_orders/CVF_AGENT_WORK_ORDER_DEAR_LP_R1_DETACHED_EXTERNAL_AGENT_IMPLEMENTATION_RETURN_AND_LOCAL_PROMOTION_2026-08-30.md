# CVF Agent Work Order - Detached External-Agent Implementation Return And Local Promotion

Memory class: governed-worker-dispatch

docType: work_order

Status: CLOSED_PASS_BOUNDED

Batch ID: DEAR-LP-R1

Dispatch base head: c8483065c

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: orchestrator/reviewer

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_WORKER_RETURN_2026-08-30.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for DEAR-LP-R1 P0-P3.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_2026-08-30.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture current HEAD before edits and record the complete
dirty state; dispatch anchor is `c8483065c`.

Current-time notes: packet authored 2026-08-30 against the current dirty
private provenance workspace; current bytes, not a clean-tree assumption, are
the implementation input.

Do-not-misread notes: prompt transport through an external surface does not
make this shared-workspace implementation a detached return. P4 pilot,
provider/live, promotion, commit, public sync and deployment are forbidden.

Required first actions: read startup continuity, guard orientation, literal
gotchas, paired baseline, selected roadmap, this work order and every current
owner/checker listed below; capture HEAD, status and hashes before editing.

Return contract: complete P0-P3, create the worker return, run all required
tests and gates, leave changes uncommitted, and return exactly
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the provider-neutral contract, schema, helper and deterministic
proof needed for manifest-bound detached implementation proposals, while
preserving legacy protocol compatibility and the local-only authority boundary.
Prepare the P4 checkpoint inputs but do not execute the pilot.

## Agent Roles

| Role | Owner | Authority |
|---|---|---|
| Operator | human operator | selects roadmap and controls pilot/external-effect checkpoint |
| Dispatcher | orchestrator | authors GC-018/work order and admits one worker invocation |
| Worker | delegated implementation worker | edits exact owned paths, tests and returns pending evidence; no commit or closure |
| Reviewer/closer | orchestrator/reviewer | independently reviews, repairs bounded defects, decides acceptance and owns any commit/continuity sync |

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator selection | 2026-08-30 instruction to select this roadmap and prepare the implementation prompt | ACCEPT |
| Active continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; mode `dear_lp_selected_pending_gc018_and_work_order` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_DETACHED_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_ROADMAP_2026-08-30.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_2026-08-30.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V59_2026-08-11.md` | ACCEPT |
| Pilot checkpoint | roadmap Design Control Gate D5 | CHECKPOINT_PRESERVED_NOT_EXECUTED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id DEAR-LP-R1 --title "Detached External-Agent Implementation Return And Local Promotion" --date 2026-08-30 --base c8483065c --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-surface EXTERNAL_AGENT_CLI_MCP --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --stdout` |
| generatedProfile | mcp-cli-adapter plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled exact roles, sources, ownership, dirty-state boundaries, P0-P3 plan, tests, return contract and checkpoint. |
| checkerReadAheadConfirmation | Current checker sources listed in the read-ahead block were inspected before authoring. |
| docOnlyNewFields | No new work-order schema fields. |
| claimBoundary | Dispatch packet only; no implementation or pilot evidence is claimed here. |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: EXTERNAL_AGENT_CLI_MCP
parentAssignmentId: DEAR-LP-R1
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 1
usageAvailability: KNOWN_FOR_ADMISSION
quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

This copied prompt is the single admitted external worker invocation under the
parent assignment. Rework is not automatically admitted. The reviewer must
first produce one consolidated finding digest and re-evaluate the cumulative
ceiling.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| DSH-WRA-R1 | accepted local reviewer closure at the path cited by the baseline; historical-only waiver explicit | local acceptance with truthful maturity | ACCEPT |
| Roadmap D1-D3 | selected roadmap Design Control Gate | source-backed PASS rows | ACCEPT |
| Roadmap D4 | paired GC-018 plus this consolidated work order | dispatch packet complete and pre-dispatch gate passes | ACCEPT |
| Roadmap D5 | operator checkpoint after deterministic proof | worker prepares evidence and stops before pilot | CHECKPOINT_PRESERVED_NOT_EXECUTED |

## Worker Autonomy / No-Question Rule

The worker proceeds autonomously for non-destructive work inside Allowed scope,
including current-source reads, exact owner-local edits, focused tests, negative
tests, deterministic receipt checks and allowed-scope gate remediation.

Return to the orchestrator only for a source contradiction, forbidden-path
need, scope or claim-boundary expansion, destructive action, pilot, external
effect, credential, provider/live use, public sync, commit or genuinely
unrepairable allowed-scope failure.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator-selected CVF roadmap and current first-party protocol owners |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | R2 existing-owner protocol/helper implementation |
| selected role route | dispatcher authors; separate worker implements without commit; orchestrator independently reviews/closes |
| Runtime/source modification | exact Write Ownership paths only |
| External evidence intake | no external factual source; the copied prompt is transport only |
| Disposition | one no-commit P0-P3 implementation invocation admitted |
| escalation condition | forbidden path, breaking compatibility, pilot/provider/public/destructive action, secret/quota use or claim expansion |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "DEAR-LP-R1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [".private_reference", "AGENT_HANDOFF_V59_2026-08-11.md", "CVF_SESSION", "CVF_SESSION_MEMORY.md", "EXTENSIONS", "docs", "governance", "scripts"],
  "claims": ["detached implementation proposals can be packaged and validated without receiving CVF authority"],
  "requiredProof": ["legacy compatibility tests", "strict schema validation", "path and authority-forgery negative tests", "state-transition regression proof", "independent review"],
  "operatorCheckpoints": ["P4 detached pilot", "provider or network use", "local promotion", "commit", "public sync"],
  "forbiddenEffects": ["worker commit", "provider call", "network access", "detached pilot", "automatic promotion", "public sync", "push", "deploy", "automatic successor"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`; shadow routing only. The full legacy governance
bundle and exact Write Ownership remain authoritative.

The broad `pathFamilies` array accounts for the pre-existing operator-owned
dirty workspace seen by the shadow router. It does not expand worker write
authority beyond the exact Write Ownership section.

## Single-Agent Multi-Role Control Block

| Field | Decision |
|---|---|
| Single agent owns implementation and review | NO |
| Role separation ledger | delegated worker owns implementation and worker return; orchestrator owns independent review, closure, commit and continuity |
| Self-review boundary | worker may run tests and self-audit but cannot accept or close its own work |
| Gate sequence | dispatcher pre-dispatch; worker pre-implementation/focused/fast gates; reviewer reviewer-fast and committed-range closure |
| Escalation conditions | scope expansion, forbidden paths, pilot, provider/live, secrets, public sync, destructive action or commit request |
| Worker | delegated implementation worker |
| Reviewer / committer | orchestrator/reviewer/closer |
| Human escalation checkpoint | P4 pilot or any external effect |
| Collusion boundary | reviewer must inspect the real diff and reproduce evidence before acceptance |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-agent-protocol-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external-agent-protocol-implementation" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | General source-verification, convergence, literal-shape and review-cost controls remain binding. |

## Required First Reads

| Source | Required use | Action |
|---|---|---|
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | current mode and next move | READ |
| `CVF_SESSION_MEMORY.md` | continuity front door | READ |
| `AGENT_HANDOFF_V59_2026-08-11.md` | active boundary | READ |
| `docs/reference/guard_orientation/README.md` | worker guard routing | FULL_READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | literal gate traps | FULL_READ |
| paired GC-018 baseline | exact authorization | FULL_READ |
| selected DEAR-LP roadmap | complete design and acceptance contract | FULL_READ |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | protocol identity and compatibility | FULL_READ |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | strict capsule schema | FULL_READ |
| `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | maturity boundary | FULL_READ |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | promotion route | FULL_READ |
| `docs/reference/external_agent_review/README.md` | owner front door | FULL_READ |
| `scripts/external_agent_packet.py` | current implementation owner | FULL_READ |
| `scripts/test_external_agent_packet.py` | compatibility and negative baseline | FULL_READ |
| `scripts/Update-CVF-External-Agent-Packet.ps1` | operator wrapper parity | FULL_READ |

## Pre-Flight Checks

Before material edits the worker must run and record:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
python -m pytest scripts/test_external_agent_packet.py -q
rg -n -e 'DETACHED_EXTERNAL_AGENT|EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION|PROPOSED_TARGET_MAP|LOCAL_PROMOTION_RECEIPT|DOCS_ONLY_FALSE_COMPLETION|automaticPromotionAllowed|ownerPromotionState|representativeUseProofState' docs/reference/external_agent_review scripts governance/compat
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected results: current baseline tests pass; new-token search still has zero
current-owner matches or any drift is explicitly reconciled; pre-implementation
gate passes. An allowed-scope defect must be repaired and rerun. A contradiction
or forbidden-scope need returns `BLOCKED_WITH_REASON`.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; worker must additionally inspect every checker applicable to its output files before writing them |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Dispatch Prompt Envelope`; `Review-Dispatch Convergence Control: REQUIRED`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; planned artifact/proof manifest labels; forbidden-scope labels; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | Confirmation and evidence after current source inspection, not first discovery. |
| claimBoundary | Dispatch-shape read-ahead only; semantic implementation and compatibility remain worker/reviewer evidence obligations. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Protocol owner is currently 1.2.0 | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | Current Protocol Identity | `1.2.0` | protocol representation contract | ACCEPT |
| Capsule mode enum has five current values | VALUE_SET | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | `task` properties | `workingMode` | task capsule schema | ACCEPT |
| Legacy expected return is fixed | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | `task` properties | `expectedReturnStatus` | task capsule schema | ACCEPT |
| Packet helper owns current protocol version | SOURCE_BEHAVIOR | `scripts/external_agent_packet.py` | module constants | `PROTOCOL_VERSION` | packet helper | ACCEPT |
| Packet helper owns capsule creation | SOURCE_BEHAVIOR | `scripts/external_agent_packet.py` | function definitions | `create_capsule`; `create_capsule_offline` | packet helper | ACCEPT |
| Packet helper owns return validation and receipt | SOURCE_BEHAVIOR | `scripts/external_agent_packet.py` | function definition | `validate_return` | packet helper | ACCEPT |
| Return authority is currently manifest-level | SOURCE_BEHAVIOR | `scripts/external_agent_packet.py` | candidate/return validators | `artifactClass`; `authorityStatus`; `secretsReturned` | return validator | ACCEPT |
| Existing test module is legacy compatibility baseline | TEST_BASELINE | `scripts/test_external_agent_packet.py` | test collection | `test_validate_return_pass_and_semantic_failure` | pytest module | ACCEPT |
| Wrapper currently projects operator commands | INTERFACE | `scripts/Update-CVF-External-Agent-Packet.ps1` | parameter and mode dispatch | `Mode` | PowerShell wrapper | ACCEPT |

## Current Runtime Freshness Verification

Fresh current-source inspection confirms the owners above. The exact collision
search below returns zero matches across current external-agent reference,
script and guard roots. The worker must repeat this search at execution start
and revise the compatibility decision if current bytes changed.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact new-token query | `rg -n -e 'DETACHED_EXTERNAL_AGENT\|EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION\|PROPOSED_TARGET_MAP\|LOCAL_PROMOTION_RECEIPT\|DOCS_ONLY_FALSE_COMPLETION\|automaticPromotionAllowed\|ownerPromotionState\|representativeUseProofState' docs/reference/external_agent_review scripts governance/compat` returned exit 1 and zero matches on 2026-08-30 | NEW_OWNER_DELTA_CONFIRMED |
| Planned dispatch paths | all three planned artifact paths were absent before authoring | NO_PATH_COLLISION |
| Existing-owner route | protocol/schema/helper/tests/wrapper are extended; no new parallel protocol, return-authority owner or promotion authority is allowed | ENRICH_EXISTING |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | external-agent protocol contract -> existing task-capsule/helper owners -> detached proposal remains non-authoritative -> local reviewer-controlled disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py` |
| Owner surface | `docs/reference/external_agent_review/`; `scripts/external_agent_packet.py`; focused tests under `scripts/` |
| Disposition | ADAPT into existing owners for accepted P0-P3 only; preserve the P4 checkpoint and every promotion decision |
| Claim boundary | The worker implements and tests a provider-neutral proposal-return contract. No external returned content is accepted into CVF, and no pilot, provider/network action, automatic promotion, runtime/public/production claim or successor is authorized. |

## Scope

Allowed scope:

- P0 fresh owner and protocol compatibility reconciliation;
- P1 additive protocol/schema/reference semantics;
- P2 provider-neutral helper and validator implementation;
- P3 deterministic/adversarial/concurrency/idempotence tests;
- pilot packet preparation and an explicit P4 stop record;
- worker-return evidence and allowed-scope gate remediation.

Forbidden scope:

- P4 detached pilot execution or any second external invocation;
- provider call, credential, secret, network refresh or external effect;
- local promotion decision, self-review or terminal absorption claim;
- public guide/projection mutation, public sync, push, deploy or production;
- source-mirror mutation, package installation or new dependency;
- session/handoff mutation, checker/hook/autorun mutation, commit or successor;
- editing or staging any path not explicitly owned below.

Risk ceiling: R2 - local protocol/helper implementation with strict authority
and path-safety behavior; no external effects.

## Write Ownership

Write mode: modify-listed plus create-listed.

Owned existing paths:

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json`
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/external_agent_review/README.md`
- `scripts/external_agent_packet.py`
- `scripts/test_external_agent_packet.py`
- `scripts/Update-CVF-External-Agent-Packet.ps1`

Owned create paths:

- `scripts/external_agent_return_contract.py`
- `scripts/test_external_agent_detached_return.py`
- `docs/reviews/CVF_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_WORKER_RETURN_2026-08-30.md`

Forbidden paths: every path not listed above, including the roadmap, baseline,
this work order, session state, active handoff, guard/checker files, public
surfaces and all unrelated dirty files.

## Pre-Existing Dirty Path Exemptions

These current bytes are valid implementation inputs, not clean-tree evidence.
The worker may edit the four owned dirty paths below but must record a fresh
pre-edit hash and preserve unrelated content. Every other dirty path is an
ignore-only exemption and must not be edited, staged or claimed.

| Path | Status at dispatch | SHA-256 at dispatch | Exemption boundary |
|---|---|---|---|
| `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | M | `27c5fe660e28a3f324cedb1a1d56ffdf9dd61466765bec8090c66bfcbffc06a3` | owned current bytes; preserve existing changes |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | M | `6e1040df8d0ad2999bf60bc1c96403fa5183dc7394cce1ddd574d9bf85effab4` | owned current bytes; preserve existing changes |
| `docs/reference/external_agent_review/README.md` | M | `3133212d6fdc1fdc9d309501933c0eea36cd7136f9b5585102c81c8de9beacbd` | owned current bytes; preserve existing changes |
| `scripts/external_agent_packet.py` | M | `2da9daf78085e2974e6fe4816666807059e006a79998bcc03a36eb56f0b952e0` | owned current bytes; preserve existing changes and extract new responsibility |
| all other pre-existing dirty/untracked paths | mixed | recorded by worker's initial `git status --short --untracked-files=all` | do not edit, stage, delete, normalize or claim |

## Near-Threshold Owner Maintainability Plan

Active owner entrypoint: `scripts/external_agent_packet.py`.

Current line count: 706. The entrypoint has crossed the 700-line advisory
threshold. Extract detached-return authority, path and state-vector logic into
`scripts/external_agent_return_contract.py` and keep orchestration/CLI wiring in
the current owner.

Minimum shrink target: 50 lines

Post-change proof: record both line counts and run
`python governance/compat/check_governed_file_size.py --enforce`. The existing
entrypoint is explicitly in Allowed scope.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | stable `docs/reference/external_agent_review/` owner family plus `scripts/` implementation helpers |
| Storage decision | enrich the existing stable reference owners; extract detached-return logic into one narrow sibling helper without creating a parallel protocol owner |
| Canonical entrypoint | `scripts/external_agent_packet.py` remains the CLI/orchestration entrypoint |
| Extracted helper | `scripts/external_agent_return_contract.py` owns detached-return authority, path and state-vector validation only |
| Test placement | retain legacy compatibility in `scripts/test_external_agent_packet.py`; add focused detached-return cases in `scripts/test_external_agent_detached_return.py` |
| Existing aggregate impact | no generated state or registry aggregate is created or hand-edited |
| Durable governance boundary | reference owners remain canonical; helper code implements their contract and creates no independent authority store |
| Index/export behavior | update the existing external-agent-review README/chain map only as needed; no dated duplicate reference owner or public export |

## Planned Worker Fulfillment Manifest

## Planned Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `scripts/external_agent_return_contract.py` | Yes | detached return authority/path/state contract |
| `scripts/test_external_agent_detached_return.py` | Yes | focused permanent adversarial matrix |
| `scripts/external_agent_packet.py` | Yes | current owner integration and CLI/receipt path |
| `scripts/test_external_agent_packet.py` | Yes | legacy 1.2 compatibility proof |
| Existing protocol/schema/reference owner paths listed in Write Ownership | Yes | coherent 1.3 or justified major representation |
| Worker return artifact named at the top of this packet | Yes | complete no-commit evidence packet |

## Forbidden Scope Manifest

| Path | Reason |
|---|---|
| `CVF_SESSION/**` | reviewer/closer continuity only |
| `AGENT_HANDOFF_V59_2026-08-11.md` | active handoff is reviewer/closer owned |
| `governance/compat/**` | checker mutation is not authorized |
| `docs/guides/**` | public-facing projection requires separate authorization |
| `.private_reference/**` | source/evidence inputs are immutable |
| every unlisted path | outside exact ownership; pre-existing changes remain ignore-only |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `LOCAL_PROMOTION_RECEIPT.json` inside any detached return fixture root | ABSENT | ABSENT in governed source tree | reject fixture/return as authority forgery |
| new parallel return-authority schema owner | ABSENT | ABSENT by exact collision search | stop; enrich current manifest/validator owner |

## Planned Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| detached emitter authority | `scripts/external_agent_return_contract.py` | `DETACHED_EXTERNAL_AGENT` | Yes |
| maximum external success | `scripts/external_agent_return_contract.py` | `EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION` | Yes |
| non-authority boundary | `scripts/external_agent_return_contract.py` | `NOT_CVF_SOT` | Yes |
| false-completion regression | `scripts/test_external_agent_detached_return.py` | `DOCS_ONLY_FALSE_COMPLETION` | Yes |
| local-only receipt rejection | `scripts/test_external_agent_detached_return.py` | `LOCAL_PROMOTION_RECEIPT.json` | Yes |
| legacy alias | `scripts/test_external_agent_packet.py` | `COMPLETE_PENDING_LOCAL_RECONCILIATION` | Yes |

## Planned Proof Atomic Literal Discipline

Each proof row above carries one atomic required literal. Do not combine or
substitute prose for the exact sentinel.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| D1 dependency | Dependency Release Evidence | accepted DSH closure reference | reviewer artifact inspection | PASS |
| D2 current-owner freshness | Source Verification; P0 | worker-return P0 decision | exact source reads/searches | PASS |
| D3 no duplicate owner | Negative Search And Collision Discipline | owner/delta map | exact zero-token search plus reviewer diff | PASS |
| D4 scope authorization | Authority Chain; Write Ownership | paired baseline and work order | pre-dispatch autorun | PASS |
| D5 pilot authority | Operator Checkpoint | checkpoint record only | reviewer confirms no pilot occurred | PASS |
| two execution classes | Acceptance Criteria | protocol/schema/helper/tests | focused pytest | PASS |
| detached package and target map | Planned Artifact/Proof manifests | generator/validator implementation | focused pytest | PASS |
| authority/status/local receipt | Acceptance Criteria | strict helper contract | adversarial pytest | PASS |
| independent state vector | Acceptance Criteria | helper contract and tests | focused pytest | PASS |
| legacy compatibility | Compatibility Decision | existing and new tests | combined pytest | PASS |
| false-completion regression | Acceptance Criteria | permanent focused test | deliberate regression demonstration | PASS |
| P4/P5 boundary | Operator Checkpoint; Claim Boundary | pilot input plus stop record | reviewer inspection | PASS |

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`

Reason: this tranche extends current first-party protocol owners. It does not
enumerate, absorb or claim coverage of a legacy repository or corpus.

## Execution Plan

| Step | Input | Required output | Validation | Stop condition |
|---|---|---|---|---|
| P0 owner reconciliation | all required first reads and current hashes | exact compatibility/owner decision in worker return | source searches plus legacy baseline | owner conflict or breaking change without justified version decision |
| P1 contract/schema | protocol contract, capsule schema, roadmap semantics | additive mode, authority object, status and state-vector contract | schema/example validation | any direct promotion or widened external authority |
| P2 helper/validator | current packet helper and new extracted module | strict generation/validation, deterministic receipt and collision preview | focused unit tests | write/promotion side effect or unbounded path behavior |
| P3 adversarial proof | roadmap test matrix | permanent negative, concurrency, idempotence and regression proof | both focused pytest modules | missing fail-closed case or compatibility regression |
| P4 checkpoint preparation | deterministic P0-P3 PASS | pilot input manifest and explicit stop record, no pilot execution | reviewer inspection | any external invocation, credential or provider requirement |

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | Purpose; Work Plan | P0-P3 only, one owner-local tranche | PASS |
| Non-goals | Non-Goals; Failure And Stop Conditions | automatic promotion, provider/public/commit and duplicate owners forbidden | PASS |
| Lane split | Work Plan P0-P5 | implement P0-P3 and prepare P4 checkpoint without execution | PASS |
| Dependency/source verification | Design Control Gate D1-D4; Required First Reads | accepted dependency and fresh current owners recorded | PASS |
| Claim boundary | Authority By State And Artifact | external proposal cannot become CVF SOT without local review | PASS |
| Acceptance criteria | roadmap Acceptance Criteria | deterministic subset mapped below; pilot-dependent rows remain checkpointed | PASS |
| Verification/evidence | Evidence Requirements; test matrix | exact focused commands, regression demonstration and worker return required | PASS |
| Dispatch readiness | Design Control Gate | D1-D4 satisfied; D5 explicitly withheld | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | shared-workspace worker edits exact local owner paths | no self-review, promotion, commit or session mutation | work order, local tests and worker return | implementation role is separate from detached return emitter | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | capsule plus detached proposal return contract | external result stays non-authoritative and at local-verification readiness | protocol/schema/helper/test outputs | contract/validator only; P4 transport and runtime integration remain checkpointed | `CONTRACT_ONLY` |

## MCP/CLI Adapter Boundary

| Field | Value |
|---|---|
| Adapter scope | Provider-neutral task-capsule and return-package generation/validation only. |
| No-runtime-overclaim | The implementation does not intercept, wrap, execute or promote any runtime command and does not prove an MCP runtime adapter. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator transports prompt; delegated worker implements; orchestrator/reviewer independently reviews and closes |
| phase | worker implementation P0-P3 pending review |
| baseHeadFor(phase) | dispatchBaseHead=c8483065c; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact Write Ownership paths only |
| traceScope(phase, actor) | worker records invocation, commands, before/after status, hashes and exact diff; reviewer records independent review |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any later material commit |
| crossBatchIsolation | all unrelated dirty files remain untouched and unclaimed |
| nextMoveSurfaces | worker return only; roadmap/session/handoff are reviewer/closer owned |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_COMPLETION_2026-08-30.md` (optional reviewer-owned conventional path; prefer worker-return reviewer addendum when sufficient) |
| reviewerOwnedClosurePaths | roadmap, baseline, work order, worker-return reviewer addendum, session continuity and active handoff |
| closureOwner | orchestrator/reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, inspect current checker source by docType, path
family and conditional content. The worker return must include real sections
named Purpose, Reviewed Target / Source, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Decision / Disposition, Checker Source
Read-Ahead Block, Agent Operation Trace Block, Delta Execution Claim Boundary
Control Block, External Knowledge Intake Routing, Rescan Intelligence
Hardening, Corpus Completeness And Report Integrity, Finding-To-Governance
Learning Disposition, Epistemic Process Block, Public Export Disposition,
Claim Boundary, git status --short, Changed Files, Command Evidence and
No-Commit Statement. Use a reason-bearing non-applicable value where truthful.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_WORKER_RETURN_2026-08-30.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Create the worker-return skeleton before long prose with the governed helper,
then replace every placeholder with current evidence. Record the real pending
git status after the return exists.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the current 1.2 owner can accept an additive
minor extension that strictly separates detached proposal readiness from local
promotion and preserves all legacy modes.

Evidence Comparison Requirement: the worker return compares actual current
source, compatibility tests and negative cases against this prediction.

Contradiction Handling Requirement: any breaking requirement, owner collision
or unverifiable authority boundary receives a Contradiction Or Gap Disposition
and narrows or blocks the claim.

Claim Update Requirement: the worker return records whether additive minor
compatibility is confirmed, revised to a justified major migration, narrowed or
invalidated.

## Evidence Requirements

The worker return must record execution base, complete before/after status,
pre-edit hashes for every owned dirty file, exact changed set, compatibility
decision, generated schema examples, proposal inventory/digest receipts,
authority-forgery rejection, state-vector projection, all focused commands and
results, deliberate regression demonstration, line-count proof, pilot stop
record, provider/external invocation counts and no-commit statement.

Every evidence claim uses command, result, key path and verdict. A pending
artifact must not claim a clean worktree or committed-range closure.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local protocol/schema/helper/test implementation for detached proposal packaging and validation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: deterministic local validation receipts required; no pilot or runtime-use receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local file generation/validation and test output only |
| invocationBoundary | one shared-workspace worker invocation transported through an external agent surface |
| interceptionBoundary | no IDE, shell, Git, filesystem, CLI/MCP runtime or provider interception claim |
| claimLanguage | provider-neutral contract and validation behavior tested locally; external result remains proposal-only |
| forbiddenExpansion | pilot, automatic promotion, local reviewer authority, runtime use, provider/live, public sync, commit, push, deploy and production remain forbidden |

## Acceptance Criteria

- [x] P0 records fresh owner, collision and protocol-version evidence.
- [x] Existing owners are extended and no parallel protocol/authority owner is created.
- [x] `SHARED_WORKSPACE_DELEGATED_WORKER` and `DETACHED_EXTERNAL_AGENT` are machine-readable and authority-distinct.
- [x] New implementation-proposal mode requires a manifest-bound proposal tree and target map.
- [x] Manifest authority object is strict, mode-scoped and fail-closed.
- [x] Strongest detached success is `EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION` with `NOT_CVF_SOT` and `ABSORPTION_NOT_COMPLETE`.
- [x] New producers never emit the legacy positive status containing `COMPLETE`; legacy readers normalize it only as compatibility input.
- [x] External return roots reject `LOCAL_PROMOTION_RECEIPT.json` and equivalent authority forgery.
- [x] Independent state vector and derived projection enforce all non-implication transitions.
- [x] Paths reject absolute, traversal, device, ambiguous normalization, symlink and inventory bypass cases.
- [x] Source/capsule/public pins, file inventory and digests reconcile deterministically.
- [x] Secret-like material is rejected or safely redacted without echoing values.
- [x] Legacy 1.2 modes and focused baseline tests remain compatible.
- [x] Concurrent/repeated validation produces no partial or cross-return receipt corruption.
- [x] `DOCS_ONLY_FALSE_COMPLETION` rejects every direct external-to-SOT/promotion/runtime/completion transition.
- [x] Deliberately disabling one new authority/transition guard makes its target regression fail; restoration disposition is MATCH by recorded SHA-256 command evidence and all tests pass again.
- [x] Helper entrypoint shrinks by at least 50 lines and governed file-size guard passes.
- [x] Pilot packet/checkpoint inputs are prepared, but P4 is not executed.
- [x] Worker return carries exact commands, results, hashes, status, diff and consolidated self-audit.
- [x] `WORKER_MUST_NOT_COMMIT` and `successorTrancheOpened: NO` are honored.

Fail conditions are evaluated and must be absent:

- [x] NOT_OCCURRED: no detached return can directly claim SOT, integration, runtime use or terminal absorption.
- [x] NOT_OCCURRED: structural validation is not treated as semantic local acceptance.
- [x] NOT_OCCURRED: no local-only receipt can originate inside a detached return root.
- [x] NOT_OCCURRED: existing 1.2 producers/readers did not break.
- [x] NOT_OCCURRED: no proposed path can escape, overwrite current source, bypass inventory or cause validator-side promotion.
- [x] NOT_OCCURRED: no provider, credential, network, pilot, public, destructive, commit or forbidden-path action occurred.
- [x] NOT_OCCURRED: unrelated dirty content was not reverted, normalized, staged or claimed.
- [x] NOT_OCCURRED: the worker opened no successor tranche and did not self-approve closure.

## Verification Commands

Run after the final material edit:

```powershell
python -m pytest scripts/test_external_agent_packet.py scripts/test_external_agent_detached_return.py -q
python -m py_compile scripts/external_agent_packet.py scripts/external_agent_return_contract.py
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py --pytest-target scripts/test_external_agent_detached_return.py
git diff --check
git status --short --untracked-files=all
```

The worker must not run `pre-closure`; committed-range closure belongs to the
reviewer/closer after acceptance.

## Operator Checkpoint

Checkpoint state: `P4_NOT_AUTHORIZED`.

The worker may prepare an immutable pilot input manifest and transport
instructions. It must stop before sending a packet to another workspace,
invoking any additional external agent, using credentials, making a provider
call or producing representative-use evidence. Only the operator can release
this checkpoint after reviewer acceptance of P0-P3.

## Worker Pending-Return Gate

| Gate | Required worker evidence | Pending-return disposition |
|---|---|---|
| focused pytest | both named modules PASS after final edit | PASS or BLOCKED with reason |
| compile | both implementation modules compile | PASS or BLOCKED with reason |
| file-size guard | no governed file-size violation | PASS or BLOCKED with reason |
| pre-implementation autorun | exact execution base and pending worktree | PASS or BLOCKED with reason |
| worker-return fast gate | full contract with both focused targets | PASS or BLOCKED with reason |
| committed-range pre-closure | reviewer/closer only | N/A_WITH_REASON_NO_COMMIT_REVIEW; reviewer-fast PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/orchestrator |
| Provider or surface | local private provenance workspace |
| Session or invocation | DEAR-LP-R1 dispatch authoring, 2026-08-30 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, hashes, scaffold helper, apply_patch and pre-dispatch gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator roadmap selection and active next-allowed-move authority |
| Before status evidence | HEAD `c8483065c`; clean worktree is not claimed; complete dirty workspace is preserved and planned dispatch paths were absent |
| After status evidence | dispatch artifacts pending and worker implementation not started |
| Diff evidence | `git diff --name-status` plus untracked dispatch paths |
| Approval boundary | dispatch authoring and one admitted no-commit worker invocation only |
| Claim boundary | no implementation, pilot, provider/live, commit or public evidence |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `dear-lp-r1-dispatch-2026-08-30` |
| Expected manifest | paired GC-018 baseline; this work order |
| Actual changed set | paired GC-018 baseline; this work order |
| Manifest delta | MATCH for dispatcher-owned artifacts; pre-existing workspace changes excluded and preserved |
| Deletion or rename disposition | N/A with reason: dispatch authoring deletes or renames nothing |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every deterministic P0-P3 acceptance
item is evidenced, every fail condition is absent, the pilot checkpoint is
explicitly unexecuted, all final commands pass and the complete pending diff is
inside ownership. Return `BLOCKED_WITH_REASON` for an actual source,
compatibility, authority or forbidden-scope blocker. Do not ask the operator
routine implementation preferences.

## Review Gate

Implementation proceeds only after the paired GC-018 exists and the exact
pre-dispatch autorun gate passes. Worker handoff is not closure. Reviewer must
inspect the full dependency class in one pass, reproduce focused proof, issue
one consolidated finding digest if needed and retain cumulative invocation
accounting. P4 remains blocked until explicit operator release.

## Closure Checklist

- [x] Worker captured execution base, full dirty state and pre-edit owned hashes.
- [x] All P0-P3 acceptance criteria are evidenced after bounded reviewer repair.
- [x] Combined focused tests and Python compile pass after final edit.
- [x] File-size guard and minimum shrink target pass.
- [x] Final worker-return fast gate passes; earlier worker pre-implementation exception remains truthfully disclosed in the return.
- [x] Worker pending changed set remained inside Write Ownership.
- [x] P4 pilot is recorded as not executed.
- [x] Provider/live, credential, public, destructive and forbidden actions are zero.
- [x] Worker return records its actual historical status and diff.
- [x] `WORKER_MUST_NOT_COMMIT` and `successorTrancheOpened: NO` are honored.
- [x] Reviewer/closer completed local closure conversion without commit.

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Worker return | present with historical `COMPLETE_PENDING_REVIEW` status | PASS |
| Reviewer decision | named completion review accepts bounded P0-P3 after repair | PASS |
| P4 evidence | not authorized and not produced | N/A_WITH_REASON |
| Automatic promotion | forbidden and not performed | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_COMPLETION_2026-08-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DETACHED_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_ROADMAP_2026-08-30.md` | P0-P3 reviewer accepted; P4 checkpoint pending | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check passed; this protocol-helper lane requires no new entry | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | aggregate drift check passed; this protocol-helper lane requires no new row | PASS |
| External evidence digest | N/A with reason: reviewer consumed no external evidence artifact | local repository proof only | N/A with reason |
| System loop interlock | N/A with reason: no system-loop owner changed | protocol-helper boundary only | N/A with reason |
| Session continuity | active memory, handoff, and generated state | bounded P0-P3 closure and P4 checkpoint synchronized | PASS |

## Claim Boundary

This work order authorizes current-owner P0-P3 implementation and provider-free
proof. It does not authorize or establish detached pilot success, semantic
promotion, CVF SOT integration, representative use, absorption completion,
provider/live behavior, public export, commit, push, deploy or production
readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private no-commit implementation packet; public projection requires a
separate authorized public-sync batch.
