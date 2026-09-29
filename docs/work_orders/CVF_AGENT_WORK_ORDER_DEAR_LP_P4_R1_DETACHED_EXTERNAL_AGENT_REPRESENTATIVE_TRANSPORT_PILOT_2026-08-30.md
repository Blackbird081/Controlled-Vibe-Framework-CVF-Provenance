# CVF Agent Work Order - DEAR-LP P4 Representative Detached Transport Pilot

Memory class: governed-worker-dispatch

docType: work_order

Status: BLOCKED_ENVIRONMENT_NOT_DETACHED

Batch ID: DEAR-LP-P4-R1

Dispatch base head: c8483065c

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: detached external implementation-proposal worker for DEAR-LP-P4-R1.

Canonical packet: this work order plus the exact task capsule named below.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: NOT_APPLICABLE_DETACHED_WORKSPACE.

closureBaseHead: REVIEWER_TO_SET.

Current-time notes: capsule was created offline on 2026-08-30 from the
operator-pinned public commit; it was not live-refreshed.

Do-not-misread notes: success means a structurally valid non-authoritative
return ready for local verification. It never means CVF acceptance,
integration, promotion, runtime proof, or completion.

Required first actions: create a fresh directory outside the private CVF
workspace; copy only the capsule and this prompt into it; verify capsule
SHA-256; do not inspect parent directories or any private CVF path.

Return contract: create exactly one `DEAR_LP_P4_R1_RETURN` folder, validate its
JSON and hashes locally, return the folder/archive plus a short summary, and
stop. Do not commit or open a successor.

Worker: detached external worker

Reviewer/closer: orchestrator/reviewer

Paired GC-018 baseline: `docs/baselines/CVF_GC018_DEAR_LP_P4_R1_DETACHED_EXTERNAL_AGENT_REPRESENTATIVE_TRANSPORT_PILOT_2026-08-30.md`

Task capsule: `docs/work_orders/DEAR_LP_P4_R1_PACKET/CVF_EXTERNAL_AGENT_TASK_CAPSULE.json`

External return root: `DEAR_LP_P4_R1_RETURN`

Reviewer intake path: `docs/reviews/CVF_DEAR_LP_P4_R1_DETACHED_EXTERNAL_AGENT_REPRESENTATIVE_TRANSPORT_PILOT_WORKER_RETURN_2026-08-30.md`

providerExecutionAuthority: FORBIDDEN_FOR_CVF_API_AND_CREDENTIALS

externalAgentInvocationAuthority: ONE_OPERATOR_MEDIATED_INVOCATION

## Purpose

Exercise the new detached implementation-return contract through one real
operator-mediated transport. Produce one documentation-only proposal and all
machine-bound return artifacts needed for the local reviewer to run the
P0-P3 validator without promotion.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id DEAR-LP-P4-R1 --title "Detached External-Agent Representative Transport Pilot" --date 2026-08-30 --base c8483065c --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface EXTERNAL_AGENT_CLI_MCP --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --stdout` |
| generatedProfile | generic no-commit external-agent dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled detached workspace, capsule hash, exact return layout, authority object, target map, transport, validator, and stop controls. |
| checkerReadAheadConfirmation | Applicable dispatch, convergence, trace, external-intake, lifecycle, and return-validator sources were read. |
| docOnlyNewFields | No runtime/schema field added; dispatch-only invocation authority separates the one operator interaction from forbidden CVF API calls. |
| claimBoundary | Dispatch authoring evidence only; no pilot result or promotion claim. |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: EXTERNAL_AGENT_CLI_MCP
parentAssignmentId: DEAR-LP-P4-R1
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

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| P0-P3 implementation | `docs/reviews/CVF_DEAR_LP_R1_DETACHED_EXTERNAL_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_COMPLETION_2026-08-30.md` | local validator implementation accepted before transport | PASS_RELEASED |
| P4 operator checkpoint | operator message `ok, next` after the completion decision and explicit P4/new-roadmap fork | one bounded pilot only | PASS_RELEASED |
| Strict task capsule | capsule SHA-256 `31ef26fb63ae80b928174680b1aa8621c9067d5125cfbb572f36af9631d2b1e2` | detached class, exact pins, four contexts, forbidden authority envelope | PASS |

## Worker Autonomy / No-Question Rule

The worker may repair files inside its detached return root to satisfy this
contract. It must stop and return `BLOCKED_WITH_REASON` for a capsule hash
mismatch, need to inspect the private workspace, need for network/credentials,
second agent invocation, or any requested authority expansion.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-agent pilot dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external-agent pilot dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No additional ADIF control beyond the current packet and external-agent protocol. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `scripts/external_agent_return_contract.py` |
| literalTokensReviewed | dispatch and convergence fields; dependency evidence; exact operation-trace labels; external-intake route; return root artifacts; authority object; dispatch binding; target map; inventory; stop status |
| gateRunPurpose | Confirm dispatch and return-contract shape after P4 value selection. |
| claimBoundary | Checker read-ahead is not evidence that the external worker or return will comply. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P4 expected result | roadmap authority | `docs/roadmaps/CVF_DETACHED_AGENT_IMPLEMENTATION_RETURN_AND_LOCAL_PROMOTION_ROADMAP_2026-08-30.md` | Work Plan P4 | transported generated files plus local verification | roadmap | ACCEPT |
| Strict detached capsule | schema and helper | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_TASK_CAPSULE.schema.json` | detached-mode condition | four contexts and execution class | strict JSON schema | ACCEPT |
| Required return root | executable source | `scripts/external_agent_return_contract.py` | detached root constants | `DETACHED_RETURN_REQUIRED_ROOT_ARTIFACTS` | validator | ACCEPT |
| Exact dispatch binding | executable source | `scripts/external_agent_return_contract.py` | binding field and validation | `dispatchBinding` | validator | ACCEPT |
| Local CLI receipt | executable source | `scripts/external_agent_packet.py` | command parser | `validate-detached-return` | packet helper | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Named dispatch paths | `Test-Path` returned false before authoring | NO_COLLISION |
| Batch tokens | exact `rg` search found no existing DEAR-LP-P4-R1 owner | NO_PARALLEL_BATCH |
| Owner decision | parent roadmap and P0-P3 owners remain canonical; this packet adds no protocol or validator owner | PASS |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | copies this prompt and capsule to one detached workspace, returns the resulting folder/archive, and authorizes no other effect |
| Detached external worker | writes only the detached return root and supplies local hash evidence |
| Orchestrator/reviewer | recomputes capsule/return hashes, runs the local validator, records the transport and review decision |
| Reviewer/closer | may reject or defer the proposed value; no automatic P5 or commit |

## Intake Role Routing Decision

- Intake summary: one offline-pinned capsule and one external proposal return.
- Scope classification: representative detached transport, not repository absorption or runtime execution.
- Risk sensitivity: external interaction and file transport with public-only task data; no credentials, private source, network retrieval, provider API, public mutation, or deployment.
- Selected role route: routeMode=MULTI_AGENT_MULTI_ROLE.
- Role separation basis: the detached worker produces non-authoritative bytes; the local orchestrator independently validates and decides value.
- Escalation condition: stop on pin drift, private-context need, second invocation, validator failure, or authority expansion.

## Dual Agent Surface Matrix

| Surface | Supported input | Allowed output | Forbidden interpretation |
|---|---|---|---|
| INTERNAL_AGENT | locally available capsule, returned folder, validator source | local validation receipt and reviewer decision | may not fabricate the detached worker result |
| EXTERNAL_AGENT_CLI_MCP | this work order and exact capsule only | one proposal-only returned folder | cannot claim private current-owner knowledge, CVF authority, promotion, integration, or use proof |
| adapter boundary | operator copy/attachment/archive transport | byte-preserving transfer record | transport is not an authority upgrade or runtime adapter |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "DEAR-LP-P4-R1",
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
  "claims": ["one detached proposal return can be transported and validated without receiving CVF authority"],
  "requiredProof": ["exact capsule digest", "complete returned-file inventory", "local detached-return validation receipt", "independent reviewer decision"],
  "operatorCheckpoints": ["one external-agent interaction", "returned-byte transport", "P5 remains parked"],
  "forbiddenEffects": ["private repository access by detached worker", "second external invocation", "provider API call", "credential use", "promotion", "commit", "public sync", "deployment"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap control | Work-order binding | Evidence expected | Disposition |
|---|---|---|---|
| P4 representative detached pilot | exact capsule plus Copy/Paste Prompt | one transported return root | BOUND |
| no automatic promotion | authority object and local-only receipt prohibition | validator receipt outside return root | BOUND |
| independent local review | operator transport followed by local CLI validation | receipt and reviewer intake record | BOUND |
| P5 separately governed | fail conditions and claim boundary | no integration/use-proof action | PARKED |

## Scope / Target / Owner Boundary

Allowed read set in the detached workspace:

- this work order text;
- `docs/work_orders/DEAR_LP_P4_R1_PACKET/CVF_EXTERNAL_AGENT_TASK_CAPSULE.json` copied as a standalone attachment;
- files created by the worker inside its fresh detached directory.

Allowed write set:

- exactly one `DEAR_LP_P4_R1_RETURN/` directory outside the private CVF workspace.

Required proposed target:

- `PROPOSED_CVF_CHANGESET/docs/examples/external_agent_pilot/DEAR_LP_P4_OPERATOR_CHECKLIST.md`.

Forbidden: reading or changing the private repository, following parent paths,
network retrieval, credentials, API calls, subagents, symlinks, archives inside
the return, local-only receipts, commit, push, publication, deployment, or any
second external invocation.

## Authority Chain

1. operator `ok, next` instruction releases the P4/new-roadmap checkpoint;
2. active DEAR-LP roadmap P4 row;
3. paired GC-018 baseline;
4. this work order;
5. strict capsule and local validator;
6. local orchestrator/reviewer decision after transport.

## Required First Reads

- this work order in full;
- the attached `CVF_EXTERNAL_AGENT_TASK_CAPSULE.json`;
- no private CVF file or parent directory.

## Pre-Flight Checks

- capsule SHA-256 matches the exact dispatch value;
- detached directory is a fresh clean worktree or non-repository directory;
- only this prompt and capsule are present before work;
- external invocation count is one and subagent count is zero.

## Write Ownership

Write mode: detached-output-root-only.

Owned path: `DEAR_LP_P4_R1_RETURN/` in the fresh detached workspace.

Forbidden paths: every path outside that root, including the private CVF
repository and the copied capsule.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | dispatch-only packet directory under `docs/work_orders/DEAR_LP_P4_R1_PACKET/`; detached return remains outside CVF |
| Storage decision | store immutable context and capsule together; do not create a new protocol, registry, runtime store, or authority owner |
| Existing aggregate impact | none beyond normal active-session regeneration |
| Generated state impact | current-authority pointers only; generated aggregate rebuilt by dispatcher |
| Durable governance boundary | packet is dispatch evidence; external returned bytes remain non-authoritative and separately reviewed |

## Execution Plan

1. verify capsule bytes and create the exact return tree;
2. write the one proposed checklist;
3. bind manifest and target-map hashes;
4. generate and independently verify the full inventory;
5. return the bytes and counters once, then stop.

## Evidence Requirements

Provide capsule hash, proposed-file hash, full relative file list, total byte
count, JSON parse results, independent inventory verification, zero-symlink
statement, and exact invocation counters.

## Required Artifact Manifest

Work-Order Fulfillment Manifest: REQUIRED

| Artifact | Required worker action |
|---|---|
| `README.md` | include the three required status statements and concise return summary |
| `EXTERNAL_AGENT_RETURN_MANIFEST.json` | emit the exact strict authority object, dispatch binding, return status, and state vector below |
| `SOURCE_MANIFEST.md` | record only capsule and prompt sources plus their bounded use |
| `DECISION_LOG.md` | record proposal rationale, overlap risk, and unresolved local facts |
| `TEST_EVIDENCE.md` | record exact local JSON/hash commands and results |
| `CLAIM_BOUNDARY.md` | deny CVF authority, promotion, integration, runtime use, and completion |
| `PROPOSED_TARGET_MAP.json` | contain exactly one entry for the required proposed target |
| `PROPOSED_CVF_CHANGESET/.../DEAR_LP_P4_OPERATOR_CHECKLIST.md` | documentation-only operator checklist candidate |
| `FILE_INVENTORY.sha256` | sorted SHA-256 inventory of every returned file except itself |

## Exact Return Contract

`EXTERNAL_AGENT_RETURN_MANIFEST.json` must contain only this top-level shape
with the exact capsule-bound values; `taskCapsuleSha256` is the hash of the
attached capsule bytes:

```json
{
  "schema": "cvf.externalAgentReturn.v1",
  "emitterClass": "DETACHED_EXTERNAL_AGENT",
  "authorityObject": {
    "emitterClass": "DETACHED_EXTERNAL_AGENT",
    "authorityClass": "EXTERNAL_PROPOSAL",
    "cvfSot": false,
    "localSemanticReviewRequired": true,
    "automaticPromotionAllowed": false,
    "absorptionComplete": false,
    "runtimeUseProven": false
  },
  "dispatchBinding": {
    "taskCapsuleSha256": "31ef26fb63ae80b928174680b1aa8621c9067d5125cfbb572f36af9631d2b1e2",
    "taskId": "DEAR-LP-P4-R1",
    "protocolVersion": "1.3.0",
    "sourceRepository": "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git",
    "sourceCommit": "d7860138350130d6d105826ce186f1beeaba3c2d",
    "cvfPublicRepository": "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git",
    "cvfPublicCommit": "d7860138350130d6d105826ce186f1beeaba3c2d"
  },
  "returnStatus": "EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION",
  "stateVector": {
    "sourceCoverageVerdict": "PARTIAL",
    "sourceReconciliationState": "PENDING_LOCAL_RECONCILIATION",
    "ownerPromotionState": "EXTERNAL_PROPOSAL",
    "runtimeRealizationState": "NOT_APPLICABLE_WITH_REASON",
    "representativeUseProofState": "NOT_REQUIRED_WITH_REASON"
  }
}
```

`PROPOSED_TARGET_MAP.json` must contain only `entries`. Its single entry must
use operation `add`, the exact proposed/intended owner path above, the actual
lowercase SHA-256 of the proposed file, at least one source/finding ID, at
least one evidence item, an explicit overlap/unresolved-local-facts list, and
literal booleans `runtimeIntegrationPending: true` and `useProofPending: true`.

The proposed checklist must be useful but bounded: 8-15 checklist items for
pre-transport, detached-workspace, pre-return, and post-return operator steps.
It must explicitly say the return is a proposal and local validation does not
promote it. Do not copy large source passages.

## Validation And Transport Evidence

The worker must record:

1. capsule SHA-256 recomputation matching the dispatch value;
2. JSON parse success for manifest and target map;
3. proposed-file digest matching the target map;
4. complete sorted inventory generated only after every other file is final;
5. a second independent inventory verification;
6. zero symlinks and zero files outside the return root;
7. the final relative file list and byte count;
8. externalAgentInvocationCount=1, internalAgentInvocationCount=0,
   providerApiCallCount=0, subagentInvocationCount=0.

The operator must preserve the returned bytes without editing them. The local
reviewer will run:

```powershell
python scripts/external_agent_packet.py validate-detached-return --return-root <transported-return-root> --task-capsule docs/work_orders/DEAR_LP_P4_R1_PACKET/CVF_EXTERNAL_AGENT_TASK_CAPSULE.json --receipt docs/reviews/evidence/CVF_DEAR_LP_P4_R1_LOCAL_VALIDATION_RECEIPT_2026-08-30.json
```

The receipt path must remain outside the returned root.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one detached external worker, then one local reviewer |
| phase | P4 representative transport pilot |
| baseHeadFor(phase) | dispatchBaseHead=c8483065c; external execution has no private-repo HEAD; closure base reviewer-owned |
| changedSetScope(phase) | detached return root only |
| traceScope(phase, actor) | capsule hash, transported bytes, file inventory, invocation counts, local validation receipt |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer commit not authorized by this packet |
| crossBatchIsolation | no P5, no other roadmap, no second external invocation |
| nextMoveSurfaces | worker returns folder and summary to operator; reviewer records PASS, RETURN_FOR_REPAIR, or BLOCKED |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_DEAR_LP_P4_R1_DETACHED_EXTERNAL_AGENT_REPRESENTATIVE_TRANSPORT_PILOT_COMPLETION_2026-08-30.md` only if reviewer acceptance requires a separate artifact |
| reviewerOwnedClosurePaths | reviewer intake record, local validation receipt, roadmap P4 state, active continuity surfaces |
| closureOwner | orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `DEAR_LP_P4_R1_RETURN/`
contractProfile: WORKER_RETURN_FULL_GATE_V1
detachedAdapterProfile: DETACHED_IMPLEMENTATION_PROPOSAL_V1_3
requiredGate: local JSON and SHA checks followed by CVF-local `validate-detached-return`
requiredFastGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The full-gate worker-return terms apply to the local reviewer intake record;
the detached adapter maps the returned folder and chat summary into that
record without granting the external worker access to `docs/reviews/`.

Required terms in the returned `README.md`:
`EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION`, `NOT_CVF_SOT`,
`ABSORPTION_NOT_COMPLETE`, `EXTERNAL_PROPOSAL`, and
`NON_AUTHORITATIVE_UNTIL_REVIEWED`.

## Verification Commands

Detached worker, inside the fresh detached directory:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath .\CVF_EXTERNAL_AGENT_TASK_CAPSULE.json
python -m json.tool .\DEAR_LP_P4_R1_RETURN\EXTERNAL_AGENT_RETURN_MANIFEST.json
python -m json.tool .\DEAR_LP_P4_R1_RETURN\PROPOSED_TARGET_MAP.json
```

Local reviewer after byte-preserving transport:

```powershell
python scripts/external_agent_packet.py validate-detached-return --return-root <transported-return-root> --task-capsule docs/work_orders/DEAR_LP_P4_R1_PACKET/CVF_EXTERNAL_AGENT_TASK_CAPSULE.json --receipt docs/reviews/evidence/CVF_DEAR_LP_P4_R1_LOCAL_VALIDATION_RECEIPT_2026-08-30.json
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Acceptance Criteria

- [ ] Operator transports only this work order and the exact capsule.
- [ ] Exactly one detached external-agent invocation occurs.
- [ ] Worker reads no private CVF path and writes only the return root.
- [ ] All nine required returned artifacts exist with no extras or symlinks.
- [ ] Capsule, source, and public pins match exactly.
- [ ] Proposed-file and full inventory digests reconcile.
- [ ] Strict authority object and state vector remain non-authoritative.
- [ ] Local validator returns `EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION`.
- [ ] Local receipt remains outside the return root.
- [ ] Reviewer records transport integrity and proposal-value disposition.
- [ ] No promotion, P5, provider API, credential, commit, public, or deployment action occurs.

## Review Gate

The local reviewer must preserve returned bytes, run `validate-detached-return`,
inspect the receipt and proposal value, and issue one consolidated decision.
Structural PASS never implies promotion or P5 authority.

## Closure Checklist

- [ ] Returned bytes are preserved unchanged.
- [ ] Local receipt status and errors are recorded.
- [ ] Transport count and capsule digest reconcile.
- [ ] Proposal value is accepted, rejected, or deferred explicitly.
- [ ] No second invocation, promotion, P5, commit, public, or deployment effect occurred.

## Return-To-Orchestrator Conditions

Return `EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION` only with the exact
folder and evidence summary. Return `BLOCKED_WITH_REASON` on any fail
condition. No rework is automatic because the cumulative ceiling is one.

## Operator Checkpoint

The operator performs one copy/attachment action and returns the resulting
folder/archive unchanged. Any request for a second attempt, network access,
private context, credentials, promotion, or P5 stops for new authority.

## Fail Conditions

- capsule digest or any pin differs;
- private workspace access is required or reported;
- a local-only authority receipt or forbidden completion claim appears;
- inventory, JSON, digest, path, symlink, or secret validation fails;
- more than one external invocation, any subagent, provider API, credential,
  network retrieval, commit, public, promotion, or deployment action occurs;
- the worker returns prose without the exact file tree.

On any fail condition, stop as `BLOCKED_WITH_REASON`; do not repair by widening
authority or requesting another worker invocation.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | detached proposal return to local validation and semantic review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `scripts/external_agent_return_contract.py` |
| Owner surface | DEAR-LP protocol, capsule, validator, reviewer intake and receipt |
| Disposition | proposal-only transport; reviewer may accept, reject, defer, or return for repair without promotion |
| Claim boundary | external bytes remain input evidence; only local owners can make later authority decisions |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: the pilot creates one explicitly manifested
documentation proposal and does not absorb a repository.

## External Absorption Core

This packet transports one first-party CVF task capsule and expects one
proposal-only return. It does not enumerate or absorb an external repository.

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | one operator-transported task capsule and later detached return root |
| Enumeration command | exact Required Artifact Manifest plus local filesystem walk during validation |
| Manifest artifact or inline manifest | `docs/work_orders/DEAR_LP_P4_R1_PACKET/CVF_EXTERNAL_AGENT_TASK_CAPSULE.json` plus inline Required Artifact Manifest |
| Processing ledger artifact or inline ledger | inline Required Artifact Manifest and future `docs/reviews/evidence/CVF_DEAR_LP_P4_R1_LOCAL_VALIDATION_RECEIPT_2026-08-30.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/external_agent_review/`; `scripts/external_agent_return_contract.py`; reviewer intake |
| Unresolved items | 1 before return: detached transport outcome |
| Absorption maturity | NO_RUNTIME_VALUE_WITH_REASON |
| Named runtime consumer | N/A_NO_RUNTIME_VALUE_WITH_REASON: documentation-only transport pilot |
| Integration evidence | N/A_NO_RUNTIME_VALUE_WITH_REASON: promotion and P5 are forbidden |
| Use proof | pending P4 transport receipt only; not runtime use proof |
| Operator checkpoint | exactly one external interaction |
| Absorption completion status | NO_RUNTIME_VALUE_WITH_REASON |
| Completion claim boundary | a valid return proves transport and local-verification eligibility only |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| one detached checklist proposal | evidence that the 1.3 return contract survives operator transport | `NO_PACKAGE_OR_RUNTIME_VALUE`; `DOCTRINE_ADAPTED`, `PACKAGE_CANDIDATE`, `RUNTIME_CANDIDATE`, `CHECKER_CANDIDATE`, and `REJECT_DIRECT_IMPORT` remain reviewer dispositions | DEAR-LP reviewer intake and local receipt | validate, then accept/reject/defer proposal value without promotion | documentation proposal only; no runtime or package activation |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| detached operator-checklist proposal | `docs/guides/CVF_EXTERNAL_AGENT_ROUND_TRIP_KIT.md`; `docs/reference/external_agent_review/README.md` | `ENRICH_EXISTING` candidate, subject to local review | representative transport evidence is new; checklist content may duplicate existing owners | validate transport first; reviewer later rejects, defers, or adapts content |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded four-artifact dispatch packet plus one future manifested return.
- Corpus root: paired baseline, work order, context JSON, and capsule JSON.
- Snapshot time: 2026-08-30 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of the four named dispatch artifacts.
- Manifest artifact or inline manifest: Agent Operation Trace Expected manifest.
- Manifest hash: `31ef26fb63ae80b928174680b1aa8621c9067d5125cfbb572f36af9631d2b1e2` for the immutable task capsule.
- Processing ledger artifact or inline ledger: Source Verification and Required Artifact Manifest; returned bytes are pending.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=4; ledger_terminal=4; exclusions=0; unresolved=0 for dispatch artifacts.
- Unresolved files: 0 in dispatch packet; future return does not exist yet.
- Declared exclusions: private repository content and all paths outside the named packet.
- Unreadable or unsupported files: none among dispatch artifacts.
- Aggregation check: four named dispatch artifacts equal four dispositioned artifacts.
- Drift check: exact capsule SHA-256 and pinned commits recorded.
- Output traceability: capsule creation receipt, work order, and future local validation receipt.
- Adversarial verification: pin mismatch, missing artifact, extra file, symlink, secret, authority, path, and digest failures are fail-closed.
- Corpus verdict: PARTIAL - dispatch packet is reconciled; future detached return and any wider repository are outside this verdict.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: repository URL and commit are dispatch pins;
network enumeration and absorption are forbidden.

## Epistemic Process Block

### Expected Result / Prediction

Prediction: the exact capsule and contract should be sufficient for one
detached worker to produce a validator-acceptable return without private
workspace access or authority inflation.

### Evidence Comparison

Not yet available at dispatch. The reviewer must compare transported bytes,
local receipt, invocation count, and worker friction against the prediction.

### Contradiction Or Gap Disposition

Any validator failure, missing field, private-context need, or second
invocation is a real P4 gap and blocks acceptance; it is not silently repaired.

### Claim Update

Dispatch only. No pilot success claim exists before local validation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | local orchestrator/dispatcher |
| Provider or surface | private shared CVF workspace; zero provider/API calls |
| Session or invocation | DEAR-LP-P4-R1 dispatch authoring, 2026-08-30 |
| Working directory | active private CVF repository root |
| Command or tool surface | PowerShell read-only inspection, governed scaffold preview, apply_patch, offline capsule helper |
| Target paths | paired baseline, this work order, task context, generated capsule, roadmap and active continuity dispatch state |
| Allowed scope source | operator `ok, next` instruction plus current P4 checkpoint |
| Before status evidence | P0-P3 accepted; dispatcher dirty worktree preserved; detached worker must start in a fresh clean worktree and no P4 packet existed |
| After status evidence | one strict capsule and one no-commit, one-invocation dispatch packet prepared |
| Diff evidence | `git diff --name-status` and untracked-path inspection before pre-dispatch gate |
| Approval boundary | dispatch preparation only; external execution occurs only when operator copies this prompt |
| Claim boundary | no pilot result, promotion, provider API, public, runtime, or production claim |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `dear-lp-p4-r1-dispatch-codex-2026-08-30` |
| Expected manifest | paired baseline, this work order, context JSON, capsule JSON, roadmap and continuity dispatch sync |
| Actual changed set | expected dispatch artifacts only; pre-existing unrelated dirty files preserved |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one operator-mediated detached folder-return pilot |
| claimDisposition | CLAIM_REJECTED: dispatch does not prove execution or enforcement. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: capsule offline-creation receipt exists, but no detached-return receipt exists yet |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch files created locally; external action remains pending operator copy |
| invocationBoundary | cumulative external ceiling one; CVF API/provider calls zero |
| interceptionBoundary | no runtime wrapper, proxy, interception, or automatic dispatch is claimed |
| claimLanguage | packet is ready to transport, not pilot-proven |
| forbiddenExpansion | no P5, promotion, runtime, provider API, credential, public, commit, deploy, or successor |

## Copy/Paste Prompt For The Detached Worker

You are the single detached external worker for `DEAR-LP-P4-R1`.

Use only this prompt and the attached
`CVF_EXTERNAL_AGENT_TASK_CAPSULE.json`. Work in a fresh directory outside the
private CVF repository. Do not inspect parent directories, the private CVF
workspace, Git remotes, the internet, credentials, or provider APIs. Do not
spawn subagents. Your only write target is `DEAR_LP_P4_R1_RETURN/`.

First recompute the capsule SHA-256. It must equal
`31ef26fb63ae80b928174680b1aa8621c9067d5125cfbb572f36af9631d2b1e2`.
If it does not, stop with `BLOCKED_WITH_REASON` and create no return.

Then implement the exact Required Artifact Manifest and Exact Return Contract
in this work order. Create the one proposed operator-checklist file, compute
its digest for the target map, finalize all other files, and generate the
sorted full inventory last. Independently verify every inventory entry a
second time. Do not create any local promotion/authority receipt or any extra
file in the return root.

Return the complete folder or an archive that preserves its bytes, followed
by a short summary containing the final relative file list, total bytes,
capsule hash, proposed-file hash, and these exact counters:

`externalAgentInvocationCount=1`
`internalAgentInvocationCount=0`
`providerApiCallCount=0`
`subagentInvocationCount=0`

Terminal chat status: `EXTERNAL_RETURN_READY_FOR_LOCAL_VERIFICATION` if all
local checks pass; otherwise `BLOCKED_WITH_REASON`. Stop after returning it.

## Claim Boundary

This work order authorizes only generation of a non-authoritative detached
return root. It does not authorize reading or changing CVF, semantic local
acceptance, promotion, P5 integration/use proof, provider API calls,
credentials, network access, commit, push, publication, deployment, or a
successor dispatch.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator-mediated pilot; no public-sync or public artifact
mutation is authorized.
