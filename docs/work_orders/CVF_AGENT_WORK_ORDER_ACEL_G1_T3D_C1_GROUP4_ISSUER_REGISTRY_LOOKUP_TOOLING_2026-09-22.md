# CVF Agent Work Order - ACEL G1 T3D-C1 Group 4 Issuer Registry And Lookup Tooling

Memory class: governed-worker-dispatch

docType: work_order

Status: CLOSED

Date: 2026-09-22

Batch ID: ACEL-G1-T3D-C1-GROUP4-ISSUER-REGISTRY-LOOKUP-TOOLING

Dispatch base HEAD: `72f769e5d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` worker

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md`

## Dispatch Prompt Envelope

Role: `INTERNAL_AGENT` worker for bounded T3D-C1 hermetic tooling.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: T3D-C0 is accepted at `e14722e17`; Party C and Party B are
Local verified; both Group 4 source paths and all five worker outputs were
absent at dispatch authoring.

Do-not-misread notes: tooling and disposable fixtures only. Do not use
credentials or `runas`; do not execute as Party B/C; do not create a real
registry, response log, second observation, launcher or verifier lookup; do not
stage or commit.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, this order, all authority sources and checker sources;
capture HEAD/status/staging, all thirteen parked hashes and forbidden-path state;
then run the pre-implementation gate before edits.

Return contract: create the exact worker return, complete all required tests
and final hash binding, leave every worker output uncommitted, and return only
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

High-Risk Local Transaction Proof Applicability: REQUIRED

## Purpose

Implement and hermetically prove the accepted Group 4 issuer-registry and
lookup-response tooling without creating a real source. Produce two
principal-bound PowerShell tools, one independent checker, focused tests, and
one checker-safe worker return.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | internal first-party Group 4 source-tooling implementation |
| scope classification | bounded code/evidence change with cryptographic, transaction and local-security sensitivity |
| risk sensitivity | exact canonical bytes plus two-principal durable writes and DACL mutation |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one implementation worker, separate Local reviewer/probe executor |
| role separation basis | worker cannot use credentials, execute real modes, accept its return, stage or commit |
| escalation condition | authority contradiction, sixth path, parked drift, credentials or real-source need |

## Authority Chain

| Authority | Path | Binding |
|---|---|---|
| T3D-C1 dispatch authority | `docs/baselines/CVF_GC018_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md` | exact five-path tooling-only scope |
| Group 4 owner contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | exact envelope, row, lookup, receipt, DACL and lifecycle semantics |
| C0 terminal review | `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md` | four repaired joins accepted; implementation separately gated |
| Party C verification | `docs/audits/CVF_ACEL_G1_T3D_PARTY_C_PRINCIPAL_LOCAL_VERIFICATION_2026-09-22.md` | exact account/SID and non-admin separation |
| Party B and Group 3 verification | `docs/audits/CVF_ACEL_G1_T3C_C2_GROUP3_SOURCE_LOCAL_VERIFICATION_2026-09-22.md` | exact observer SID and immutable observation source boundary |
| Current control state | `AGENT_HANDOFF_V63_2026-09-18.md` | T3D-C1 packet authoring only before dispatch commit |

## Agent Roles

| Role | Owner | Authority |
|---|---|---|
| dispatcher | Local orchestrator/reviewer | packet, corrections and dispatch commit |
| implementer | shared-workspace `INTERNAL_AGENT` | exact five worker paths, no commit |
| reviewer/probe executor | Local, not implementation worker | returned evidence, independent process/security probes and closure |
| operator | human operator | passwords and any later alternate-principal execution |
| session-sync steward | Local | post-material continuity only |

## Scope / Target / Owner Boundary

Allowed: create and test exactly the five manifest paths with disposable
temporary fixtures; repair failures confined to those paths. Forbidden:
credentials, alternate-user execution, real source paths, existing Group 3
mutation, second observation, launcher creation, T3E, admission, provider/live,
public sync, deployment, staging, commit, and mutation of parked paths.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3D-C1-GROUP4-ISSUER-REGISTRY-LOOKUP-TOOLING","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_INTERFACE"},"pathFamilies":["AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","docs/audits/","docs/baselines/","docs/reference/","docs/reviews/","docs/work_orders/","governance/compat/","governance/sources/issuer_registry/","scripts/"],"claims":["hermetic Group 4 tooling implements the accepted contract; no source is created"],"requiredProof":["two writer self-tests","focused Python tests","checker self-test","real second-process exclusion","semantic DACL rollback","final return hash binding","13/13 parked-path hashes"],"operatorCheckpoints":["T3D-C1 Local acceptance","Party C registry creation","Party B response-log initialization and issuer observation","T3E first real lookup","candidate admission"],"forbiddenEffects":["credential access","alternate-user execution","real source creation","second observation","real lookup","worker commit","provider/live/network","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files only","completenessClaimChanged":false}}
```

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3D-C1-GROUP4-ISSUER-REGISTRY-LOOKUP-TOOLING

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: INITIAL_DISPATCH

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-g1-t3d-c1-group4-tooling-problem",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "ACEL-G1-T3D-C1-TOOLING-DISPATCH",
      "claimClass": "OTHER",
      "proofClass": "NAMED_OBSERVABLE_PROOF",
      "evidenceRef": "docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: Local independently rebuilds both JCS preimages, exact hashes,
registry snapshot binding, one response chain, and exact owner/DACL semantics
using disposable fixtures and real second-process peers.

negativeMutationClasses: base64url/JCS/UTF-8 drift, hash and schema drift,
duplicate active versions, observation mismatch, response-chain break,
principal collision, early peer entry, post-acquire failure, extra/deny/inherited
ACE, wrong owner, partial append, and rollback residue.

expectedInformationGain: distinguish worker self-consistency from independently
observed byte, process, chain and security behavior.

rerunCostReason: focused disposable probes provide decision-changing evidence
without repeating the full worker suite.

reviewerDecisionOwner: LOCAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact five worker paths | hermetic implementation/tests only; no credentials, source, staging or commit | this packet and paired baseline | local PowerShell/Python tooling | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner | no external ingress, authentication, mutation, receipt, runtime or public claim | no authority | fresh source-verified packet required | DEFERRED_WITH_REASON |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace `INTERNAL_AGENT` worker |
| role set | PowerShell tooling, Python checker/test and evidence author; not reviewer/closer |
| delegation depth | zero |
| evidence basis | governed T2F/T3D sources only; never provider memory or credentials |
| gate sequence | pre-implementation, focused tests, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit output |
| role separation ledger | worker returns pending; Local independently evaluates and commits |
| escalation condition | credentials, alternate-user/real-source execution, sixth output, parked drift or authority contradiction |

## Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| Group 4 outer contract | accepted T2F T3D-C0 amendment | terminal Local review at `e14722e17` | RELEASED |
| Party C role/principal | T2E appointment and Local OS verification | exact SID ending `-1010` remains current | RELEASED_FOR_TOOLING |
| Party B role/principal | T2E appointment and T3C Local verification | exact SID ending `-1009` remains current | RELEASED_FOR_TOOLING |
| Group 3 source model | Local-verified log | worker uses disposable equivalent fixtures only | RELEASED_FOR_HERMETIC_TOOLING |
| Group 4 real source | paths absent; operator execution not authorized | separate reviewed tooling and source packet | PARKED |
| T3E lookup | consumer binding remains closed | separate explicit T3E authority | PARKED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C1-GROUP4-ISSUER-REGISTRY-LOOKUP-TOOLING --title "ACEL G1 T3D-C1 Group 4 Issuer Registry And Lookup Tooling" --date 2026-09-22 --base 72f769e5d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact five-path manifest, T3D-C0 contract, transaction proof and negative oracles |
| checkerReadAheadConfirmation | every checker listed below was inspected before final packet authoring |
| docOnlyNewFields | none; no schema extension is authorized |
| claimBoundary | dispatch authoring only; no source or runtime effect |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_c_group4_registry_writer.ps1` | create Party C-bound atomic registry writer with default non-mutating self-test and explicit real mode |
| `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | create Party B-bound response-log initializer/lookup appender with default non-mutating self-test and explicit gated modes |
| `governance/compat/check_acel_g1_issuer_registry.py` | create independent read-only registry/response/schema/hash/chain/identity/security checker |
| `governance/compat/test_check_acel_g1_issuer_registry.py` | create disposable positive, negative, concurrency and rollback tests |
| `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md` | create checker-safe evidence return |

## Work-Order Fulfillment Manifest

The preceding table is the complete worker output set. No extra helper,
launcher, receipt, fixture, source, log, copy, alternate return or side-channel
artifact may remain in the repository.

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `governance/sources/issuer_registry/REGISTRY.json` | real Party C source creation is a later operator checkpoint |
| `governance/sources/issuer_registry/LOOKUP_RESPONSES.jsonl` | real Party B initialization/lookup is a later checkpoint |
| `governance/sources/registry_observation_log/LOG.jsonl` | accepted Group 3 source is immutable in this tranche |
| `scripts/run_as_cvf_g1_party_c.cmd` | launchers are Local/operator-owned after tooling acceptance |
| `scripts/run_as_cvf_g1_party_b.cmd` | existing operator launcher is outside worker scope |
| `AGENT_HANDOFF_V63_2026-09-18.md` | active handoff is Local-owned |

The worker remained forbidden from all `CVF_SESSION/**` mutation. At terminal
closure, Local may update only the generated current-authority projection
needed to bind this work order's closed hash; that projection is closer-owned
and remains separate from worker scope.

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `governance/sources/issuer_registry/REGISTRY.json` | ABSENT | ABSENT | stop; return to orchestrator |
| `governance/sources/issuer_registry/LOOKUP_RESPONSES.jsonl` | ABSENT | ABSENT | stop; return to orchestrator |
| `scripts/run_as_cvf_g1_party_c.cmd` | ABSENT | ABSENT | stop; return to orchestrator |

## Pre-Existing Dirty Path Exemptions

These thirteen untracked paths predate dispatch. Hash each before and after;
do not edit, stage, delete, rename, claim or commit them:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts`
- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md`
- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json`
- `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md`
- `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json`
- `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md`
- `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md`
- `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md`
- `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md`
- `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

## Planned Worker Proof Matrix

| Proof | Path | Required literal or outcome | Required at return |
|---|---|---|---|
| Registry writer self-test | `scripts/acel_g1_party_c_group4_registry_writer.ps1` | exact JCS/hash, real peer, security rollback PASS | Yes |
| Response writer self-test | `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | receipt/chain, real peer, security rollback PASS | Yes |
| Independent checker self-test | `governance/compat/check_acel_g1_issuer_registry.py` | all positive and adversarial fixtures PASS | Yes |
| Focused tests | `governance/compat/test_check_acel_g1_issuer_registry.py` | zero failures after final edit | Yes |
| Worker return binding | canonical return | MATCH: SHA-256 before/after final required gate and `NO_POST_GATE_MUTATION` | Yes |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, bootstrap read model and active handoff.
2. `docs/reference/guard_orientation/README.md` and literal-format gotchas.
3. Paired T3D-C1 baseline, this order, T2F Group 4 and C0 completion review.
4. Party B/C verification surfaces and accepted T3C transaction architecture.
5. Every checker in Checker Source Read-Ahead Block before writing outputs.

## Pre-Flight Checks

Capture `git rev-parse HEAD`, `git status --short --untracked-files=all`, empty
staging, all thirteen parked SHA-256 values, absence of five outputs and three
forbidden paths. Run pre-implementation autorun from `executionBaseHead`. Stop
on source contradiction, non-empty staging, parked drift or path collision.

## Write Ownership

Owned files: exactly the five rows in Required Artifact Manifest.

Write mode: create-only, uncommitted. No rename, copy, deletion, stage or commit.
Every other repository path is read-only.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | two scripts, one focused checker/test pair and one return |
| Storage decision | create exact files only; temporary fixtures outside governed source paths |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | real Group 4 paths stay absent; no source or receipt is created |

## Implementation Contract

### Shared strict primitives

- Implement RFC 8785 JCS for the closed Group 4 envelope, issuer-row and
  response shapes without relying on PowerShell hashtable enumeration order.
  Reject noncanonical input bytes. Do not claim a general-purpose JCS engine.
- Admit issuer-authority content only under profile
  `ACEL_G1_ISSUER_AUTHORITY_CONTENT_V1`: exactly `authority` fixed to
  `ACEL_G1_DECISION_OWNER`, `issuerIdentity` equal to the row and matching
  `[A-Za-z0-9._:-]+`, and integer `policyVersion` in `1..2147483647`. Reject
  extra/missing keys, other types, Unicode/escaped aliases and unsupported
  numeric forms. Future inner schemas require a contract amendment.
- Strict unpadded base64url rejects `=`, whitespace, invalid alphabet and
  noncanonical re-encoding. Decode once; require UTF-8 JSON and JCS byte identity.
- SHA-256 fields are exactly 64 lowercase hexadecimal characters and are
  recomputed from the controlling byte preimages, never trusted from callers.
- Stable errors distinguish schema, encoding, canonicalization, hash, snapshot,
  chain, authority, access, concurrency and rollback failures.

### Party C registry writer

- Default invocation is non-mutating `-SelfTest`. Real mode requires an explicit
  `-ExecuteRegistryWrite`, exact account `LAM-RUBY\cvf-g1-party-c`, exact SID
  ending `-1010`, exact confirmation, repository-root canonicalization and
  exact target `governance/sources/issuer_registry/REGISTRY.json`.
- Accept one closed envelope with exactly four fields and rows with exactly the
  T2F fields. Enforce one active version per issuer, monotonic positive versions,
  legal timestamps/transitions, terminal revocation, and non-circular content.
- This tranche implements initial creation only: target absence is mandatory;
  publish is exclusive/no-overwrite. Correction, revocation, replacement and
  rotation transactions are forbidden and deferred to separate authority.
- Produce exact no-BOM/no-newline JCS bytes and direct snapshot hash. Create a
  same-directory temporary file, write/flush it, set exact Party C ownership and
  protected ordered DACL, and read back bytes/security before atomic no-overwrite
  publication. Then read back the target bytes/security under the same guard.
  The target name must never be visible under an ambient or incomplete DACL.
- Never read/write response log or observation log. On any failure restore exact
  pre-existing content/existence and complete semantic security state.

### Party B response writer

- Default invocation is non-mutating `-SelfTest`. Real modes require exact
  account `LAM-RUBY\cvf-g1-party-b`, exact SID ending `-1009`, exact confirmation,
  canonical root and exact registry/response/observation paths.
- `-InitializeResponseLog` may create only an empty protected response log and
  is not a lookup. `-ExecuteLookupAppend` exists but must not be invoked in this
  tranche; it is reserved for a fresh T3E work order.
- Preserve the pure T2C evaluator call
  `lookup(issuerIdentity, issuerAttestedHash, snapshot_content)`. The durable
  wrapper separately requires a T3E-minted UUID `lookupId`, `consumerIdentity`
  and `observedSnapshotId`, resolves exactly one immutable Group 3 record, and
  passes only that record's strictly decoded `snapshot_content` to the evaluator.
  Never trust caller-supplied snapshot bytes, result, digest, entry version,
  timestamps or chain fields.
- Before one append, read exact registry bytes once under the guard; verify
  envelope JCS/digest, strict issuer content, exact Group 3 observation bytes,
  snapshot ID/version/hash equality, issuer/version/status and claimed hashes in
  the mandatory order. Malformed/incomplete input appends nothing. Once the
  complete response schema is available, append exactly one terminal response.
- Validate the entire existing response chain and duplicate lookup IDs before
  mutation. Hash the closed response preimage under `cvf.issuerLookupResponse`.
  Direct in-place append is forbidden: build a same-directory copy-on-write temp
  containing exact prior bytes plus one row, flush, pre-harden/read back the
  exact Party B/SYSTEM/Administrators FullControl plus Local Read protected
  DACL, validate the complete chain, atomically replace, then re-read target
  bytes/security under the same guard. Party C has no ACE.

### Exactly-once adapter, framing and first-failure taxonomy

- Under the same response-log guard, use `lookupId` as the idempotency key.
  Existing ID plus the identical immutable tuple (`issuerIdentity`,
  `claimedIssuerHash`, `consumerIdentity`, `observedSnapshotId`) returns the
  fully revalidated stored row without append. Existing ID plus any tuple drift
  fails `LOOKUP_ID_CONFLICT` in memory with no mutation. Concurrent identical
  retries must leave exactly one row.
- An empty response log is exactly zero bytes. Each appended row is one compact
  RFC 8785 JCS object including stored `entryHashHex`, UTF-8 without BOM, then
  exactly one LF byte. Reject CRLF, blank/partial lines, leading separators and
  non-JCS rows. Prior file bytes must remain an exact prefix after append.
- The closed hash preimage uses `profile`, domain `cvf.issuerLookupResponse`,
  then exactly the thirteen T2F fields from `lookupId` through
  `priorEntryHashHex`; it excludes only stored `entryHashHex`.
- Stop at first failure. `MALFORMED_REQUEST`, `INCOMPLETE_REQUEST`,
  `SOURCE_UNAVAILABLE`, `SOURCE_SCHEMA_INVALID`, `ISSUER_NOT_FOUND`,
  `AMBIGUOUS_ACTIVE_VERSION`, and `LOOKUP_ID_CONFLICT` are in-memory/no-append
  classes because the complete closed receipt cannot be populated.
- A schema-complete hash/status mismatch appends one `IDENTITY_REJECTED` row
  with JSON null `errorCode`. A schema-complete observation/policy uncertainty
  appends one `IDENTITY_UNRESOLVED` row whose `errorCode` is exactly one of
  `OBSERVATION_BINDING_UNRESOLVED`, `FRESHNESS_UNRESOLVED`, or
  `AUTHORITY_UNRESOLVED`. `IDENTITY_CONFIRMED` also requires null `errorCode`.

### Cross-process and rollback proof

- Each real mutation path uses one named cross-process guard starting before
  directory/file creation, pre-state capture or any mutation and ending only
  after byte/security validation or exact rollback.
- Self-tests launch the same writer in a real second `pwsh` process with unique
  READY/START_ATTEMPT/ATTEMPTING/PARENT_RELEASE/ENTERED/COMPLETE events. A peer
  entering before release is a hard failure; timeouts are deadlock bounds only.
- Inject failure immediately after acquisition and before mutation; a second
  process must subsequently acquire. Dispose handles/processes in `finally`.
- Normalize owner, protection, inheritance and every ACE as complete semantic
  tuples preserving multiplicity. Exercise extra allow, deny, inherited and
  wrong-owner adversaries; compare captured and restored bytes/existence plus
  semantic descriptor exactly.
- Preserve two security oracles: the exact canonical ordered explicit ACE vector
  as listed in T3D-C0, including multiplicity, and a separately sorted complete
  semantic tuple multiset for effective access. Applying, final validation and
  rollback must pass both; never sort away the ordered-vector requirement.
- Inject deterministic termination/failure at prepublication, after temp flush/
  hardening, and immediately before atomic replace. No source filename may be
  visible with a non-final descriptor; no partial response line or orphan temp/
  lock may remain; a subsequent invocation must recover or proceed safely.

## High-Risk Local Transaction Proof Contract

```json
{
  "transactionTarget": "Party C atomic issuer-registry publish and Party B durable response-log initialization or append with exact security rollback",
  "productionPathPeer": {
    "kind": "REAL_SECOND_PROCESS",
    "invocationPath": "scripts/acel_g1_party_c_group4_registry_writer.ps1 and scripts/acel_g1_party_b_group4_lookup_response_writer.ps1",
    "mutationPath": "guarded registry publish and guarded response-log initialization or append transaction"
  },
  "deterministicBarrierProtocol": {
    "events": ["READY", "START_ATTEMPT", "ATTEMPTING", "PARENT_RELEASE", "ENTERED", "COMPLETE"],
    "timeoutRole": "DEADLOCK_SAFETY_ONLY"
  },
  "enteredBeforeReleaseOracle": "REJECT_ENTRY_BEFORE_PARENT_RELEASE",
  "postAcquireFailureInjection": {
    "point": "AFTER_ACQUIRE_BEFORE_MUTATION",
    "cleanupProof": "SUBSEQUENT_PEER_ACQUIRES"
  },
  "semanticSecurityTuple": {
    "fields": ["ownerSid", "protectionState", "inheritanceState", "aces"],
    "aceFields": ["sid", "rights", "accessType", "isInherited", "inheritanceFlags", "propagationFlags"],
    "normalization": "SORT_COMPLETE_ACE_TUPLES"
  },
  "rollbackExactness": {
    "comparison": "SEMANTIC_PRESTATE_EQUALS_POST_ROLLBACK",
    "adversaries": ["EXTRA_ALLOW", "DENY", "INHERITED", "WRONG_OWNER"]
  },
  "finalEvidenceHashBinding": {
    "algorithm": "SHA256",
    "scope": "EXACT_RETURN_BYTES",
    "capture": "BEFORE_AND_AFTER_FINAL_REQUIRED_GATE",
    "equality": "REQUIRED",
    "postGateMutation": "FORBIDDEN"
  },
  "independentProbeRequired": {
    "required": true,
    "owner": "LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER",
    "workerReturnDisposition": "PENDING_REVIEWER_EXECUTION"
  }
}
```

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures and rerun without asking. Stop only for a source
contradiction, sixth path requirement, parked drift, credentials, alternate-user
or real-source need, or irreparable mandatory failure outside owned paths.

## Core Guard Self-Protection Authorization

| Field | Value |
|---|---|
| Authorized guard-maintenance scope | create one Group 4 source-specific read-only checker and its focused tests; no hook/catalog/general checker change |
| Protected paths | `governance/compat/check_acel_g1_issuer_registry.py`; `governance/compat/test_check_acel_g1_issuer_registry.py` |
| Operator authorization | standing instruction to continue G1-G6 and delegate bounded implementation |
| Rollback boundary | all five worker paths remain uncommitted and may be rejected wholesale; accepted sources and thirteen parked paths remain untouched |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional historical defect overlay; current contract and high-risk proof still control |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; split implementation modules loaded by it; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | active status, exact source columns, closeability gate IDs/dependencies, high-risk declaration and nine-key JSON, protected-path authorization, required return headings, trace fields and export enum |
| gateRunPurpose | confirmation of source-verified packet and output shape; not first discovery and not runtime proof |
| claimBoundary | T3D-C1 hermetic tooling only |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: exact C0 vectors, source hashes, principal bindings and every
implementation result must be fresh at the worker execution base.

priorVerificationArtifact: `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md`

priorVerificationAnchor: material commit `e14722e17`

freshRecomputeRequired: both JCS vectors, current authority-source SHA-256,
every focused test, exact changed set and all thirteen parked hashes.

unicodePathHandling: use repository root plus literal paths and UTF-8-safe
readers; never relocate or reconstruct the workspace path from lossy output.

extractedTextAuthority: direct repository bytes and command output only;
screenshots, chat summaries and provider memory are contextual, not authority.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Exact Group 4 schemas, hash domains, validation order and lifecycle | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 4; T3D-C0 amendment; T2C Consumer-Binding Table | `cvf.issuerRegistryRow`; `cvf.issuerLookupResponse` | Source Group 4 contract | ACCEPT |
| Four gaps closed with bounded C1 successor | TERMINAL_REVIEW | `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md` | Findings / Position; Decision / Disposition | accepted T2F hash | Local review | ACCEPT |
| Party C exact principal | LOCAL_VERIFICATION | `docs/audits/CVF_ACEL_G1_T3D_PARTY_C_PRINCIPAL_LOCAL_VERIFICATION_2026-09-22.md` | Findings / Position | `LAM-RUBY\cvf-g1-party-c`; SID ending `-1010` | Party C | ACCEPT |
| Party B exact principal and observation boundary | LOCAL_VERIFICATION | `docs/audits/CVF_ACEL_G1_T3C_C2_GROUP3_SOURCE_LOCAL_VERIFICATION_2026-09-22.md` | Findings / Position | SID ending `-1009`; `LOG.jsonl` | Party B / Group 3 | ACCEPT |
| High-risk transaction evidence shape | ACTIVE_STANDARD | `docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md` | Contract Shape; Evidence Semantics | nine-field proof contract | governance control chain | ACCEPT |
| Dispatch is current allowed action | CURRENT_SESSION_AUTHORITY | `AGENT_HANDOFF_V63_2026-09-18.md` | Next Allowed Move | T3D-C1 tooling dispatch | Local | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Packet and five output paths | `Test-Path` returned false for all seven planned new paths before authoring | NO_COLLISION |
| Real source paths | `Test-Path` returned false for registry and response log | VERIFIED_ABSENT |
| Token search | `rg -n "T3D-C1|GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING|acel_g1_issuer_registry|party_c_group4_registry|party_b_group4_lookup" docs CVF_SESSION governance scripts` found only predecessor/continuity references | NO_IMPLEMENTATION_COLLISION |
| Collision decision | use exact new paths; no existing owner is displaced | ACCEPT |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | T3D-C1 baseline and order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | T3D-C1 packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact five worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | canonical worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact five worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | canonical return and owned code | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| final_return_hash | REVIEW | worker | WORKER_RETURN | canonical return | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned five paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | final_return_hash |
| independent_peer_security_probe | PRE_MATERIAL_COMMIT | reviewer | REVIEW | disposable fixtures only | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted five paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | independent_peer_security_probe |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split material and continuity ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher/reviewer; one bounded implementation worker; independent Local probe executor; Local closer/session-sync steward |
| phase | DISPATCH_TO_WORKER_RETURN |
| baseHeadFor(phase) | dispatchBaseHead=`72f769e5d`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | exact five worker paths |
| traceScope(phase, actor) | each actor records invocation, paths, commands, result and boundary |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local closer only |
| crossBatchIsolation | thirteen parked paths and every non-manifest path remain read-only/unstaged |
| nextMoveSurfaces | worker return to Local; no successor opens automatically |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: one shared-workspace INTERNAL_AGENT worker after committed dispatch and continuity

laneOwnedPaths: exactly five paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact manifest reconciliation, empty staging and 13/13 parked hashes

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded local implementation has no discovery-audit manifest

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_acel_g1_issuer_registry.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain Purpose, Target / Source, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Decision / Disposition, Source Inventory,
Changed Files, Command Evidence, No-Commit Statement, Return-Time Closeability
Recheck, Checker Source Read-Ahead Block, Agent Operation Trace Block, Delta
Execution Claim Boundary Control Block, Machine Closure Package, External
Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus Completeness
And Report Integrity, Finding-To-Governance Learning Disposition, Epistemic
Process Block, Public Export Disposition, Claim Boundary, executionBaseHead,
full git status and `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`.
Non-applicable sections remain present with an explicit reason.

## Execution Plan

1. Freeze execution base, forbidden/parked state and empty staging; run pre-implementation gate.
2. Create checker-safe return skeleton before long prose.
3. Implement strict shared primitives and read-only checker with disposable tests.
4. Implement both principal-bound tools and their real peer/rollback self-tests.
5. Run all commands after final code edit; finish return and changed-set audit.
6. Capture return hash, run final active-work-order gate, recapture identical hash,
   make no later edit, and return uncommitted.

## Evidence Requirements

- independently recomputed content digest
  `db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca`;
- independently recomputed 618-byte registry digest
  `d31e0c206da091bc408005d490e69f7aa0eae733dac4b03c67edd280034827f2`;
- positive registry, empty-response initialization and one receipt-eligible
  response chain in disposable paths;
- duplicate identical `lookupId` is idempotent, conflicting ID is no-append,
  and concurrent retry produces exactly one row;
- empty/one/multi-row LF framing preserves prior bytes exactly and rejects BOM,
  CRLF, blank or partial rows;
- malformed/incomplete no-append and schema-complete rejected/unresolved
  exactly-one-append outcomes;
- real second-process barriers, post-acquire cleanup, atomicity and exact
  security rollback for both tools;
- pre-harden-before-publish and termination barriers proving no insecure target
  visibility, partial row, orphan temp or lost prior prefix;
- exact ordered ACE vectors plus separately normalized semantic access tuples;
- exact three-field issuer-content profile rejection of every other shape;
- all forbidden principals/ACEs denied and no residue;
- exact five-path delta, empty real source paths, empty staging, 13/13 parked
  hashes, no alternate artifacts, exact test counts and final return hash pair.

## Acceptance Criteria

- [x] Both tools default to non-mutating self-test and enforce exact real-mode principal/path/confirmation gates.
- [x] Strict schemas, RFC 8785 bytes, base64url, hashes, validation order, receipt eligibility and chain semantics match T2F exactly.
- [x] UUID idempotency, three-argument evaluator adaptation, exact LF JSONL framing and first-failure taxonomy are deterministic.
- [x] Registry and response DACLs/owners are exact, distinct and read back semantically.
- [x] Registry publication and response replacement are pre-hardened, same-volume and crash-atomic with no insecure visibility window.
- [x] Exact ordered ACE vectors and separate semantic effective-access tuples both pass on success and rollback.
- [x] The exact three-field issuer-content profile is enforced without broad RFC 8785 overclaim.
- [x] Real second processes prove exclusion, cleanup and exact rollback without sleep-as-proof.
- [x] Checker is read-only and all focused positive/adversarial tests pass.
- [x] Exactly five worker paths change; all forbidden and parked state remains intact.
- [x] Final active-work-order gate exits zero and return SHA-256 is unchanged across it.
- [x] Return declares `COMPLETE_PENDING_REVIEW` with reviewer probe still pending.

Closure fails on copied digest evidence, parser-only equality, missing closed
field, self-observation, widened access, partial append, timing-only proof,
mutex leak, rollback mismatch, sixth path, real source effect, staging, commit,
parked drift, failed gate or post-gate return mutation.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m py_compile governance/compat/check_acel_g1_issuer_registry.py governance/compat/test_check_acel_g1_issuer_registry.py
python -m pytest governance/compat/test_check_acel_g1_issuer_registry.py -q
python governance/compat/check_acel_g1_issuer_registry.py --self-test
pwsh -NoProfile -File scripts/acel_g1_party_c_group4_registry_writer.ps1 -SelfTest
pwsh -NoProfile -File scripts/acel_g1_party_b_group4_lookup_response_writer.ps1 -SelfTest
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_acel_g1_issuer_registry.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

Final binding sequence after the return is otherwise complete:

```powershell
$returnPath = 'docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md'
$preGateHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $returnPath).Hash.ToLowerInvariant()
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_acel_g1_issuer_registry.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md
if ($LASTEXITCODE -ne 0) { throw 'FINAL_WORKER_RETURN_GATE_FAILED' }
$postGateHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $returnPath).Hash.ToLowerInvariant()
if ($preGateHash -cne $postGateHash) { throw 'FINAL_WORKER_RETURN_HASH_DRIFT' }
$postGateHash
```

## Review Gate

Local verifies the return digest, consumes valid aggregate evidence, and runs
separate JCS/hash, chain, real-peer, post-acquire and semantic-security probes.
Local must not use credentials, alternate principals or real source paths.
Acceptance requires reviewer-fast, independent probe, full pre-commit and
truthful material/continuity closure. Worker evidence cannot self-certify Local.

## Pre-Dispatch Gate Disposition

Required command:

`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 72f769e5d --head HEAD`

Disposition: `LANE_SCOPED_PASS_WITH_PARKED_OUT_OF_LANE_FINDINGS`.

Author run on 2026-09-22: the aggregate command completed 82 of 83 checks and
exited 1 solely because `independent review probe admission` also diagnosed
three pre-existing untracked worker returns in the operator-parked thirteen-path
lane. Those paths are outside this dispatch, are byte-preserved, and are not
authorized for repair here. The canonical lane-scoped invocation below passed
and classified all three as out-of-lane known findings; the current T3D-C1
baseline/work order had zero violations across every targeted checker and an
independent adversarial contract re-review.

`python governance/compat/check_independent_review_probe_admission.py --base 72f769e5d --head HEAD --enforce --changed-lane-only --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md`

This bounded disposition authorizes only the exact T3D-C1 lane. Any in-lane
failure, parked-path drift, or additional aggregate failure keeps the packet
undispatched.

## Closure Checklist

- [x] source/claim/manifest integrity and exact focused tests pass;
- [x] return-time closeability recheck has no outside-authority blocker;
- [x] worker-return fast, reviewer-fast, pre-commit and split-range closure pass;
- [x] no open checkbox in terminal evidence, failed gate or unowned path remains;
- [x] final disposition is at most `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`;
- [x] material and continuity commits are separate and truthful.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_COMPLETION_2026-09-22.md` if a distinct reviewer artifact is needed |
| reviewerOwnedClosurePaths | accepted five worker paths plus optional completion review; continuity separately |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| exact response admission | strict receipt eligibility, stored-row replay and first-failure taxonomy | Python 82/82 and checker 9/9 | PASS |
| registry publication | guarded, pre-hardened, create-only and crash-atomic | Party C 53/53 | PASS |
| lookup append | guarded, idempotent, copy-on-write and publication-owned rollback | Party B 51/51 | PASS |
| independent review | distinct read-only actor and exact terminal hashes | completion review records `PASS_INDEPENDENT_PROBE` | PASS |
| source boundary | no operational registry or response source in T3D-C1 | both real source paths absent | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED` | PASS |
| Worker return | canonical return path | `COMPLETE_PENDING_REVIEW`; exact hash bound | PASS |
| Completion or reviewer artifact | reviewer-owned completion path | `CLOSED_PASS_BOUNDED`; independent probe PASS | PASS |
| Roadmap state | active ACEL continuity | T3D-C1 closes; T3D-C2 remains separately gated | PASS |
| Focused tooling | four code/test paths | Python 82/82; checker 9/9; Party C 53/53; Party B 51/51 | PASS |
| Registry JSON | real Group 4 source | absent | BLOCKED with reason: later operator checkpoint |
| Registry Markdown | source registry mutation | no source mutation | BLOCKED with reason: no source in C1 |
| External evidence digest | external input | no external evidence | N/A with reason: internal evidence only |
| System loop interlock | source creation, second observation, T3E | all remain closed | PASS |
| Session continuity | active handoff/state | separate post-material commit | BLOCKED with reason: pending material commit SHA |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private shared CVF workspace |
| Session or invocation | ACEL G1 T3D-C1 dispatch authoring, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | governed reads, targeted search, path checks, ADIF resolver, apply_patch, governance gates and Git |
| Target paths | paired baseline and this work order |
| Allowed scope source | active handoff next move and standing Local orchestrator authority |
| Before status evidence | clean worktree boundary after explicit exemption: HEAD `72f769e5d`; only thirteen parked untracked paths; staging empty; planned/source paths absent |
| After status evidence | exact two-path dispatch packet prepared; no source/tooling output created |
| Diff evidence | `git diff --name-status`; exact paired packet before commit |
| Approval boundary | dispatch authoring and commit only |
| Claim boundary | no worker execution, source, lookup, observation, admission, provider/public/deployment effect |
| Agent type | Local orchestrator/reviewer |
| Invocation ID | `acel-g1-t3d-c1-group4-tooling-dispatch-20260922` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order before dispatch commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | five-path hermetic tooling implementation and disposable proof only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: worker return and command evidence required |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact source/test diffs and hermetic test outputs required |
| invocationBoundary | local repository code/test editing and disposable process execution only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception or mandatory-wrapper claim |
| claimLanguage | tooling may be accepted without source creation only after Local review |
| forbiddenExpansion | no credential, alternate principal, real source, second observation, T3E, provider/live, public sync or deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md` |
| Chain map route | N/A with reason: direct Local-to-internal implementation route |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T3D-C1 baseline and this order |
| Disposition | local first-party implementation only |
| Claim boundary | no remote research authority, external corpus, CLI/MCP adapter or provider claim |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: implementation and no-commit return; decision
owner: Local. External research is closed. Public absence is irrelevant to
private implementation coverage. No MCP/CLI adapter or remote agent is authorized.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the closed C0 contract can be implemented in five
paths with exact byte/security semantics and no source effect.

Evidence Comparison Requirement: return compares all actual positive,
adversarial, concurrency and rollback evidence with this prediction.

Contradiction Handling Requirement: any mismatch requires a Contradiction Or
Gap Disposition and narrowed claim; no inferred contract choice is allowed.

Claim Update Requirement: record confirmed, revised, narrowed or invalidated.

## Finding-To-Governance Learning Disposition

Existing rules cover the known packet-gap and high-risk transaction classes.
Worker must classify any new repeated/root defect; isolated implementation
errors may be repaired in scope without opening a foundation tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local-principal tooling and source-security semantics; no public-sync authority.

## Claim Boundary

This order authorizes only five uncommitted hermetic tooling outputs. It does
not create `REGISTRY.json`, `LOOKUP_RESPONSES.jsonl`, a launcher, observation,
or real lookup; use a password or alternate account; bind a consumer; establish
a source; promote/admit; invoke a provider; export; deploy; or claim production readiness.

## Operator Checkpoint

No operator action is required for hermetic worker implementation. After Local
accepts C1, any real Party C/Party B execution requires a new source-creation
packet and explicit operator action; T3E requires another separate packet.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for source contradiction, required sixth path,
parked drift, forbidden credential/principal/source need, or a mandatory failure
outside allowed scope. Otherwise repair in scope, rerun, and return
`COMPLETE_PENDING_REVIEW` without committing.
