# CVF Agent Work Order - ACEL G1 T3A-C2 Group 1 Source-Creation Tooling

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3A-C2-GROUP1-SOURCE-CREATION-TOOLING

Dispatch base HEAD: `835dfc39d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker role: shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md`

## Dispatch Prompt Envelope

Role: internal security/source-tooling worker. Build a fail-closed,
principal-bound Group 1 source writer plus Local checker and hermetic tests;
do not perform the real Party A source write.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture committed HEAD, full status and staging before edits.

Current-time notes: Local independently verified public key
`R5AsDnHQNXWgD5WQEpDi3VABiuPZ7E9U5Kir_bgiwNU`, key ID
`partya-44853ea9a690452c`, digest
`5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01`,
Party A SID `S-1-5-21-1644666849-912006174-747199667-1006`, and 365-day
validity. These are public inputs, not an established source.

Do-not-misread notes: never request credentials, use run-as, access the Party
A profile or DPAPI blob, generate another key, execute the real source write,
create either future source file, mutate the thirteen parked paths, stage,
commit, wire a live verifier, claim admission, public sync or deploy.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, T2F Group 1, T3A-C2 verification audit
and every checker named below. Freeze the thirteen parked paths before edits.

Return contract: satisfy C2-01 through C2-10, run required gates, leave
staging empty, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

R1 redispatch note: the initial worker correctly stopped before implementation
because a broad-base pre-implementation gate exposed two dispatcher-owned
packet defects. Local repaired both defects in place: the routing manifest now
covers the dispatch continuity paths, and the worker-return contract now
contains every checker-required literal. On redispatch, capture the current
committed HEAD as `executionBaseHead` and use that exact SHA as the
pre-implementation `--base`; do not reuse the original dispatch base.

R2 redispatch note: Local accepted the R1 execution discipline and the valid
36/36 PowerShell, 37/37 Python and cross-tool evidence, but independent
adversarial review disproved the completion claim. The checker returned
`VALIDATED` for wrong role, invalid timestamps, padded/non-canonical base64url,
genesis versions 5->6, wrong actor, and a chained entry with a different key ID
and false prior status. The writer also lacks an exact verified-product binding,
accepts an arbitrary real-mode repository root and cannot guarantee removal of
the file whose own write/flush fails. Repair the complete R2 matrix below in one
pass; do not narrow it to the six demonstrated probes.

R3 redispatch note: R2 materially improved the tooling: PowerShell now passes
39/39, Python passes 62/62, the original six reviewer probes reject, the real
destination is script-derived and the demonstrated post-create rollback works.
Local nevertheless rejects completion because R2 did not overwrite the fourth
required output and did not close the whole correction matrix. Source inspection
shows the writer still accepts the old nine-field self-consistent metadata shape
instead of the exact verified fourteen-field product. Independent checker probes
also returned `VALIDATED` for (a) a duplicate transition ID plus a wrong actor on
a later entry, (b) an invalid ACTIVE->ACTIVE transition with cross-record time
disagreement, and (c) an entirely caller-selected substitute product. Complete
the consolidated R3 matrix below in one pass; preserve every already-passing R2
regression and do not reduce R3 to the three demonstrated probes.

Operator-escalation resolution: after the mandatory round-three stop was
surfaced with the desired outcome, contradictions, risk and bounded repair
scope, the operator explicitly directed Local to continue on 2026-09-19. The
prior assignment therefore ends at escalation and this document now dispatches
a fresh operator-authorized R3 completion assignment. Its dispatch counters
start at zero; that reset does not erase or relabel the R1/R2 evidence retained
above and below. Scope, authority ceiling, four output paths, no-commit rule and
all parked effects remain unchanged.

R3-R1 redispatch note: Local reproduced the worker's 50/50 PowerShell and
81/81 Python results, then rejected completion using two new source-derived
probes. The real writer still lets a caller-controlled environment variable
replace the fixed verified product, and the raw duplicate-member scanner does
not decode JSON escapes before comparing member names. Complete the consolidated
R3-R1 matrix below in one pass; preserve every passing R2/R3 regression.

## Purpose

Implement deterministic tooling that a later operator can run under the exact
Party A principal to create the first Group 1 registry snapshot and genesis
lifecycle receipt from the already-verified public ceremony metadata. Supply
a Local checker/consumer and hermetic positive/negative tests without creating
the operational sources during worker execution.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3A-C2-GROUP1-SOURCE-ESTABLISHMENT --title "ACEL G1 T3A-C2 Group 1 Source Establishment" --date 2026-09-19 --base 9eabacc8b1daf58fe96cd9da34104c6095f912c5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch; internal INITIAL; no-commit |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | narrowed real source establishment to exact principal-bound tooling, four outputs, C2 matrix and operator checkpoint |
| checkerReadAheadConfirmation | dispatch, convergence, closeability, structural, scaffold and worker-return checker paths |
| docOnlyNewFields | `SOURCE_CREATED_PENDING_LOCAL_VERIFICATION` is tool result language, not a T2F source-state replacement |
| claimBoundary | scaffold use does not execute Party A or create Group 1 sources |

## Authority Chain And Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| Group 1 contract | T2F Source Group 1 and closed preimages | preserve exact fields, hashes, roles and paths | ACCEPT |
| ceremony product | T3A-C2 verification audit, commit `835dfc39d` | strict decode=32 bytes and digest match | ACCEPT |
| Party A identity | name/SID in verified metadata | tool must compare both to current process | ACCEPT_TOOLING_ASSUMPTION |
| real source write | Party A exclusive writer | accepted tooling then separate operator invocation | PARKED_OPERATOR_EXECUTION |
| consumer wiring | Future T3E | checker may consume/validate but no production wiring claim | DEFERRED_WITH_REASON |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | principal-bound Group 1 source-creation tooling and hermetic checker evidence |
| scope | bounded code, hermetic tests and evidence return |
| risk | source-integrity and secret-adjacent, but public input only |
| selected role route | `SINGLE_AGENT_MULTI_ROLE`: one no-commit `INTERNAL_AGENT`, then Local review |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE` |
| separation | worker cannot use Party A credentials or accept/commit its output |
| escalation | stop only for credential need, real alternate-user execution, source creation, extra path or authority contradiction |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3A-C2-R3-OPERATOR-ESCALATED-COMPLETION

reviewRoundCount: 1

priorFindingSetDigest: 2428e1c14c177f7734fdaf7464275595b47b246d5cd4cc4d78d304beebaa9ff7

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: T3A-C2-R3-R1-01,T3A-C2-R3-R1-02

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: acel-g1-t3a-c2-r3-authority-and-json-normalization

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3A-C2-GROUP1-SOURCE-CREATION-TOOLING","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"CREDENTIAL_REFERENCE","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["scripts/","governance/compat/","docs/reviews/","docs/baselines/CVF_GC018_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md","AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json","CVF_SESSION/ACTIVE_SESSION_STATE.json","CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json","CVF_SESSION/state/entries/nextAllowedMove.json","CVF_SESSION_MEMORY.md","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md","docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md","governance/compat/check_task_class_calibration_owner_evidence.py","governance/compat/test_check_task_class_calibration_owner_evidence.py"],"claims":["principal-bound Group 1 source-creation tooling and hermetic tests only"],"requiredProof":["C2-01 through C2-10","exact four-path delta","parked hashes","worker-return fast gate"],"operatorCheckpoints":["actual Party A source write","Local source verification","key promotion","consumer wiring"],"forbiddenEffects":["credential access","alternate-user execution","operational source creation","worker commit","candidate admission","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

Expected route: `P3_ELEVATED`; shadow routing only. Full legacy gates apply.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3a-c2-group1-source-creation-tooling","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":["real_party_a_ceremony_not_executed","group1_source_not_created"],"resolved":["real_party_a_ceremony_not_executed"],"retained":["group1_source_not_created"],"new":["group1_source_creation_tooling_not_implemented"],"reopened":[],"current":["group1_source_creation_tooling_not_implemented","group1_source_not_created"]},"resolutionEvidence":{"real_party_a_ceremony_not_executed":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md","sha256":"81b507d19e934c451a4d74ecca9c519f01dfceae42649a59ae4692624db99d3f","locator":"Decision / Disposition","claimId":"ACEL-G1-T3A-CEREMONY-PRODUCT-VERIFIED"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3A-CEREMONY-PRODUCT-VERIFIED","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md"},{"claimId":"ACEL-G1-T3A-C2-TOOLING-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_2026-09-19.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

## Consolidated R2 Correction Matrix

### T3A-C2-R2-01 - Exact Ceremony Product And Strict Metadata Binding

The writer must reject before confirmation or output unless the metadata has
exactly the closed public-metadata field set and every immutable value equals
the independently verified T3A product: profile, key ID, algorithm, principal
name/SID, public-key bytes/digest, creation/expiry timestamps, three
dispositions and claim boundary. Reject missing, extra and duplicate JSON
members. Base64url must use only the unpadded URL-safe alphabet, decode to 32
bytes and reproduce byte-for-byte after canonical re-encoding. Add independent
negative tests for each field class, substitution of a self-consistent but
different key, standard-base64 characters, padding and duplicate keys.

### T3A-C2-R2-02 - Exact Destination And Failure-Atomic Two-File Write

Real mode must resolve the repository from the committed script location and
must not accept an operator-selectable alternate repository root. Fixture-root
injection may exist only in internal self-test functions. Preserve collision
fail-closed behavior. A failure during create, write or durable flush of either
file must remove every file created by that invocation, including the file
whose own write failed; it must never remove a pre-existing file. Remove any
newly-created empty source directory on rollback when it did not pre-exist.
Add deterministic injected-failure tests for first-file and second-file
create/write/flush boundaries plus pre-existing collision preservation.

### T3A-C2-R2-03 - Complete Checker Semantics And Cross-Record Chain

The checker must reject duplicate JSON members and non-canonical base64url,
validate strict types/non-empty identifiers, exact `Ed25519`, exact
`verificationAuthority` role, RFC3339 UTC timestamps and the T2F temporal
rules. Operational/default validation must be hard-bound to the verified
public product rather than making expected key/public-key arguments optional.
For lifecycle validation enforce: genesis exactly 0->1, `NOT_PRESENT` to
`ACTIVE`, null prior hash, exact Party A actor; every later entry has the same
key ID, unique transition ID, prior hash equal to the prior entry digest,
`priorStatus` equal to the prior entry's `newStatus`, contiguous versions and
non-decreasing timestamps. The envelope snapshot version must equal the chain
tip version; envelope/row/chain key, status and applicable timestamps must
agree. Public-key alias comparison uses decoded bytes, never only the encoded
string.

### T3A-C2-R2-04 - Machine Regression And Automated Cross-Tool Proof

Turn every R2 condition into a focused negative with an asserted stable
taxonomy. At minimum, the six reviewer probes that currently return acceptance
must return rejection: wrong role; invalid timestamps; padded base64url;
genesis 5->6; wrong actor; and a valid-hash second lifecycle entry carrying a
different key ID and false prior status while the envelope version disagrees.
Make the PowerShell-writer-output -> Python-checker validation an automated
test command, not a manually reported step. Both isolated suites and the
cross-tool suite must fail when any R2 mutation is reintroduced.

### R2 Claim Boundary

R2 is still tooling-only. It must not execute as Party A, read Party A private
material, create either real Group 1 source, promote a key, wire T3E, admit a
candidate, call a provider, public-sync or deploy. The exact four output paths
remain unchanged; overwrite the existing worker-return path with the R2 return.

## Consolidated R3 Correction Matrix

### T3A-C2-R3-01 - Writer Exact Product Binding And Strict JSON Intake

The writer must accept only the exact fourteen-member JSON object independently
verified in the T3A-C2 audit: `metadataSchema`, `metadataProfile`, `keyId`,
`algorithm`, `principalName`, `principalSid`, `publicKeyBytesBase64`,
`publicKeySha256Hex`, `createdAtUtc`, `expiresAtUtc`, `ceremonyDisposition`,
`testDisposition`, `registryDisposition` and `claimBoundary`. Reject every
missing, extra or duplicate member before confirmation or output. Enforce JSON
types, exact immutable values from the verified product, exact `Ed25519`, strict
unpadded canonical base64url with byte-for-byte re-encoding, 32 decoded bytes
and the exact verified digest. A self-consistent substitute key, altered time,
altered disposition, standard-base64 character, padding or duplicate member
must each have a focused negative test. Fixture metadata may differ only inside
an explicitly test-only validator/input path; the real execution path must be
cryptographically and literally bound to the verified product.

### T3A-C2-R3-02 - Checker Product Authority Must Not Be Caller-Selectable

The operational/default checker must carry or load the immutable verified T3A
public product from a fixed CVF-governed authority and must not let CLI arguments
redefine the expected key ID, public key or actor. Remove the three caller-
selectable `--expected-*` authority arguments from the operational CLI. Bind the
row to the exact key ID, decoded public-key bytes, `issuedAt` and `expiresAt`,
and bind every lifecycle actor to the exact Party A principal. A private
test-only entry point may inject fixture expectations, but its name, visibility
and call graph must prevent it from being mistaken for operational validation.
Add a regression proving that an internally consistent alternate key/product
cannot be made valid by supplying matching caller expectations.

### T3A-C2-R3-03 - Complete Lifecycle State Machine And Cross-Record Time Rules

Enforce unique non-empty `transitionId` values across the complete log and the
exact Party A actor on every entry, not only genesis. Enforce only the T2F
transition graph: genesis `NOT_PRESENT -> ACTIVE`; then `ACTIVE -> ROTATING`;
then `ROTATING -> REVOKED` or `ROTATING -> EXPIRED`; terminal states have no
successor and no self-transition is valid. Parse timestamps to UTC instants
before comparison. For this genesis source writer/checker, require row
`issuedAt` and `expiresAt` to equal the verified product, `issuedAt <=` genesis
timestamp, genesis timestamp equal to the envelope `writeTimestamp`, chain-tip
timestamp equal to the envelope `writeTimestamp`, and the write/tip instant to
precede the non-null expiry. Preserve contiguous versions, prior-hash linkage,
prior-status linkage, same key ID, envelope-tip version/status agreement and all
strict-shape/digest checks. Add focused negatives for duplicate transition ID,
wrong later actor, every illegal state edge, terminal resurrection, non-UTC or
chronologically decreasing time, and every stated cross-record disagreement.

### T3A-C2-R3-04 - Complete Atomic Failure-Injection Matrix

The two-file orchestration, not only the low-level single-file helper, must expose
test-only deterministic failure points for first-file and second-file create,
write and durable-flush boundaries. Exercise all six boundaries through
`Write-GroupOneOutput`; after each failure assert that every file created by the
invocation is absent, a newly-created empty directory is removed, and every
pre-existing collision/directory/sentinel remains byte-identical. Test-only
injection must be unreachable from the real CLI and must not weaken exclusive
create or real durable flush.

### T3A-C2-R3-05 - Complete Four-Path Return

Overwrite the worker-return artifact for this actual R3 execution. It must name
execution base `7be9ae7b5`, R3 generation 3, final case counts, automated
producer-to-consumer proof, the reviewer-probe outcomes, exact hashes of all
three implementation files, empty staging, unchanged thirteen parked paths and
continued absence of both real source files. Historical R1/R2 claims must not
be presented as the current result.

## Consolidated R3-R1 Correction Matrix

### T3A-C2-R3-R1-01 - Remove Caller-Controlled Real-Mode Authority Override

The real `-ExecuteWrite` call graph must always bind directly to
`$script:VerifiedPartyAProduct`. Remove
`CVF_G1_WRITER_TEST_EXPECTED_PRODUCT_JSON` and every equivalent environment,
process, file or argument override from the real-mode path. A label such as
"test-only" does not make a caller-controlled input unreachable. Fixture
authority injection may exist only through an internal test function that the
script entry point and `Invoke-GroupOneWrite` cannot call or observe.

Repair the non-interactive test without weakening this boundary. It may test
`Assert-InteractiveConfirmation` directly in a non-interactive child, or use a
separate hermetic test harness, but must not make operational metadata authority
replaceable. Add a regression which sets the former environment-variable name
to a complete alternate product and proves that real-mode expected-product
resolution remains the fixed `partya-44853ea9a690452c` product. Add a source/
call-graph assertion that `Invoke-GroupOneWrite` has no authority-override
input. Preserve the no-Party-A and no-real-source boundary.

Reviewer proof to close:

```text
FIXED_KEY=partya-44853ea9a690452c
RESOLVED_KEY=caller-selected
AUTHORITY_REDEFINED=True
```

The corrected result must be `AUTHORITY_REDEFINED=False` or the override must
be absent altogether.

### T3A-C2-R3-R1-02 - Decode JSON Member Names Before Duplicate Comparison

Replace the raw escape-preserving top-level member-name scan with a strict JSON
reader or an equivalent tokenizer that compares decoded JSON member names.
Reject duplicates after JSON escape normalization and before any last-value
wins object materialization. This must cover ordinary duplicates and escaped
aliases of all fourteen allowed names, not only the demonstrated `keyId` case.
Do not use regex matching over raw JSON as the acceptance authority.

Add at least these focused negatives:

1. `"keyId":"wrong","key\u0049d":"<verified-key-id>"`;
2. `"metadataSchema":"wrong","metadata\u0053chema":"<verified-schema>"`;
3. the existing literal duplicate-member case.

Reviewer proof currently accepted the escaped alias:

```text
ACCEPTED={"keyId":"right"}
```

All three corrected probes must reject with
`METADATA_DUPLICATE_JSON_MEMBER`. Re-run the complete PowerShell and Python
suites and overwrite the same worker return with the R3-R1 result, exact new
case counts, three implementation hashes, empty staging, unchanged parked
paths and both real sources absent.

### R3 Claim Boundary

R3 remains tooling-only and no-commit. It must not execute as Party A, read
Party A private material, create either real Group 1 source, promote a key,
wire T3E, admit a candidate, call a provider, public-sync or deploy.

## Acceptance Matrix

| ID | Required contract | Positive and negative proof |
|---|---|---|
| C2-01 | writer requires exact Party A name/SID and rejects elevation before any source mutation | exact-current hermetic pass; wrong-name, wrong-SID and elevated probes reject |
| C2-02 | input is strict `cvf.acel.g1.partyAPublicKeyMetadata@1`; base64url is canonical, 32 bytes, digest recomputes, algorithm/key/principal/dispositions match | verified vector passes; one-field mutations reject before output |
| C2-03 | registry row uses exactly T2F `cvf.keyRegistryRow` closed preimage and `cvf.source-record-canonicalization@1`; role=`verificationAuthority`, status=`ACTIVE`, nullable fields present | publish exact preimage bytes and independently recomputed `rowHashHex`; omission/extra/mutation reject |
| C2-04 | envelope contains fresh `registrySnapshotId`, version 1, RFC3339 write time and exactly one row; duplicate key and public-key alias checks fail closed | deterministic fixture plus duplicate/alias negatives |
| C2-05 | genesis lifecycle row uses exact closed preimage: fresh transition ID, versions 0 to 1, prior status `NOT_PRESENT`, new status `ACTIVE`, actor exact Party A, timestamp, `priorEntryHashHex:null`; own `entryHashHex` excluded | exact preimage/digest and chain recomputation tests |
| C2-06 | real-mode output paths are exactly T2F proposed registry and lifecycle paths; repository containment, reparse, collision and partial-write failures reject/clean up | disposable-repository sandbox only in tests; real paths remain absent |
| C2-07 | default mode is hermetic self-test; actual write requires explicit flag plus typed confirmation after all guards | default creates no durable sources; noninteractive execute rejects |
| C2-08 | Local checker reads both files, validates schemas, strict field sets, hashes, chain, uniqueness, alias, time/status/role and expected public product; no warning-pass | positive fixture plus taxonomy negatives, exit codes asserted |
| C2-09 | worker never runs as Party A, reads no Party A profile/private material, and never creates operational source | trace, searches and final absence checks |
| C2-10 | exact four worker outputs, empty staging and thirteen parked paths byte-identical | before/after status, hashes and manifest reconciliation |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_a_group1_source_writer.ps1` | UPDATE the pending uncommitted writer to close all R3 findings while preserving every R2 pass; real mode remains operator-only |
| `governance/compat/check_acel_g1_verifier_key_registry.py` | UPDATE the pending uncommitted Local checker to close all R3 findings while preserving every R2 pass |
| `governance/compat/test_check_acel_g1_verifier_key_registry.py` | UPDATE the pending uncommitted focused suite with every R3 regression and automated cross-tool proof |
| `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md` | OVERWRITE the stale committed R1 return with complete R3 evidence |

## Work-Order Fulfillment Manifest

The table above is the exact worker output set. In particular, the worker must
not create `governance/sources/verifier_key_registry/REGISTRY.json` or
`governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl`; those are
operator-run Party A outputs after Local accepts this tooling.

## Allowed Scope / Forbidden Scope

Allowed: update and test exactly the four pending manifest paths using
disposable fixtures, overwrite the worker-return evidence, and repair failures
confined to those paths. Forbidden: Party A credentials/profile/private blob, run-as,
real source files, existing governed source mutation, parked paths, staging,
commit, T3E wiring, live/provider/public/deployment effects.

## Write Ownership

Worker owns uncommitted edits to the exact four manifest paths, including the
three pending implementation files and the existing return that R3 must
overwrite. Local owns review, bounded evidence repair, staging and commits.
Every other existing path, both future source files and the thirteen parked
paths are read-only.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | retains Party A password and later real source-write authority |
| Local dispatcher | commits packet and preserves principal/source boundary |
| INTERNAL_AGENT worker | implements exact tooling/checker/tests/return without credentials or commit |
| Local reviewer/closer | reviews invariants, runs bounded probes and decides acceptance |
| session-sync steward | updates continuity after Local disposition |

## Required First Reads

1. Startup front door, bootstrap model, active handoff, guard orientation and literal gotchas.
2. This order, paired baseline, T2F Group 1 and T3A-C2 verification audit.
3. Applicable checker sources, the accepted C1 tool's repaired process/ACL patterns, and output-specific worker-return rules.

## Pre-Flight Checks

- Capture execution HEAD, full status, empty staging and hashes of all thirteen parked paths.
- Confirm the R3 dispatch commit exists, the exact four pending worker outputs
  are the only active-lane delta, and both real source paths are absent.
- Confirm no Party A credential/private artifact is present or requested.
- Run the pre-implementation autorun gate before editing.

## Implementation Contract

- Use only PowerShell/.NET functionality available to the clean Party A
  profile; resolve any required executable by absolute machine path or avoid
  it. Do not repeat the C1 current-user PATH defect.
- Construct DACL-only security descriptors; do not request or persist SACL
  sections requiring `SeSecurityPrivilege`.
- Use UTF-8 without BOM, exclusive create and rollback of partial two-file
  writes. Never overwrite an existing source.
- Canonical JSON preimages must be compact and lexicographically key ordered.
  Publish exact bytes/digests in hermetic evidence and recompute independently
  in the Python checker.
- `issuedAt` and `expiresAt` come exactly from verified ceremony metadata;
  `revokedAt` and `rotatedFromKeyId` are JSON null.
- Real output is still `SOURCE_CREATED_PENDING_LOCAL_VERIFICATION`, never
  admission or T3E consumer wiring. Tool output text must say so explicitly.

## Worker Autonomy / No-Question Rule

Repair all allowed-scope implementation and gate failures directly. Stop only
for credentials, alternate-user/real-source execution, a fifth output, parked
drift or a source-authority contradiction.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | two pending standalone `governance/compat/` checker/test files plus one PowerShell operator tool and one worker return |
| Storage decision | repair the existing four-path pending lane in place; create no additional folder, registry, queue, aggregate or runtime store |
| Existing aggregate impact | none during worker execution |
| Generated state impact | none during worker execution |
| Durable governance boundary | checker remains read-only; operational Group 1 sources remain absent and operator-gated |

## ADIF Defect Registry Disclosure

Dispatcher query `CODE_CHANGE`/`dispatcher`/`dispatch` returned zero defects.
Worker must rerun for `CODE_CHANGE`/`worker`/`implementation` and disclose the
actual result in the return.

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | exact section headings, controlled disposition tokens, trace labels, no-commit and changed-set evidence |
| gateRunPurpose | confirm authored output after source-driven design |
| claimBoundary | structure and governed-path compatibility only; not proof the worker read them |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| exact Group 1 fields/preimages | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Closed Preimage Field Lists; Source Group 1 | `cvf.keyRegistryRow`; `cvf.keyLifecycleReceipt` | Group 1 contract | ACCEPT |
| exclusive Party A writer | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 1 Write Principal/Forbidden Roles | Party A | Group 1 access contract | ACCEPT |
| real public input | `docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md` | Verified Public Metadata; Verification Evidence | key ID and public key digest | ceremony public-product receipt | ACCEPT |
| actual sources absent | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Literal Proposed-Path Collision Ledger | both proposed Group 1 paths, freshly re-probed | Local source boundary (`SOURCE_NOT_CREATED`) | ACCEPT |

## Negative Search And Collision Discipline

All four worker paths were absent at initial dispatch and now comprise the
returned R1 lane delta; both future source paths remain absent. Exact batch/key
searches found only the committed verification audit and the active T3A-C2
packet/return. Any other collision is a stop condition unless it is one of the
four lane-owned outputs being repaired by this worker.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline/work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline/work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return ADIF disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned four paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | six continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> no-commit INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | T3A-C2 source-creation tooling; actual Party A source write excluded |
| baseHeadFor(phase) | dispatchBaseHead=`835dfc39d`; executionBaseHead captured by worker; closureBaseHead set by Local |
| changedSetScope(phase) | exact four required outputs |
| traceScope(phase, actor) | reads, commands, tests, hashes, status, cleanup and absence of real sources |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths byte-identical |
| nextMoveSurfaces | Local review, then separate Party A operator source-write checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT T3A-C2 tooling worker after operator forwards this packet

laneOwnedPaths: exact four paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and parked reconciliation

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace `INTERNAL_AGENT` worker |
| role set | PowerShell source-tooling implementer, Python checker/test implementer and evidence author; not reviewer/closer |
| delegation depth | zero |
| evidence basis | governed T2F/T3A sources and public metadata only; never provider memory or private material |
| gate sequence | pre-implementation, focused tests, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit its output |
| role separation ledger | worker returns pending; Local evaluates and commits |
| escalation condition | credentials, alternate-user/real-source execution, fifth output, parked drift or authority contradiction |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-19.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Target / Source;
Findings / Position; Risk / Corrective Action; Decision / Disposition; Claim
Boundary; Changed Files; Command Evidence; No-Commit Statement; Agent Operation
Trace Block; Delta Execution Claim Boundary Control Block; Machine Closure
Package; Public Export Disposition. Use `N/A with reason` for conditional
blocks that do not apply.

Checker-required literal checklist for the returned packet:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- executionBaseHead
- git status --short
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Every conditional item must appear as a real section or an explicit `N/A with
reason` disposition.

## Execution Plan

1. Freeze state, parked hashes, the exact four-path pending delta and real-source absence; run pre-implementation gate.
2. Repair the PowerShell writer against every R3 exact-product and complete atomic-failure requirement while preserving R2 behavior.
3. Repair the independent Python checker and focused tests against every R3 product-authority, state-machine and cross-record-time requirement.
4. Publish exact preimage bytes/digests and run all positive/negative cases, including every R2 and R3 reviewer probe.
5. Automate the cross-tool proof, overwrite the evidence return, run fast gate, reconcile exact outputs and leave staging empty.

## Evidence Requirements

Return C2-01 through C2-10 with command/result evidence, exact hashes, negative
taxonomy, cleanup/absence proof, empty staging and parked-file reconciliation.
Never include credentials, DPAPI bytes, private-key material or a real source.

## Acceptance Criteria

All C2 rows pass; default invocation is non-mutating; wrong principal,
elevation, malformed metadata, digest drift, unsafe path, collision and
noninteractive execution fail before output. Exactly four worker paths change.

## Review Gate

Local inspects guard ordering, DACL and two-file rollback, consumes valid
returned evidence and runs bounded checker/mutation probes. Local will not run
the real Party A source write during worker review.

## Closure Checklist

- [ ] C2-01 through C2-10 reviewed.
- [ ] Exact four paths and all parked hashes reconcile.
- [ ] Worker-return fast and reviewer preflight pass.
- [ ] Both real Group 1 source paths remain absent.
- [ ] No credential/private/alternate-user action occurred.
- [ ] Material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a credential need, Party A or real-source
execution, fifth output, parked drift, source-authority contradiction or an
irreparable mandatory gate failure. Otherwise return
`COMPLETE_PENDING_REVIEW`, never source/admission readiness.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
pwsh -NoProfile -File scripts/acel_g1_party_a_group1_source_writer.ps1
python governance/compat/test_check_acel_g1_verifier_key_registry.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

The self-test must use disposable paths only and prove the two real source
paths remain absent. No provider/live release-gate call applies: this tranche
does not assert CVF AI governance behavior or production readiness.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING_COMPLETION_2026-09-19.md` (optional; prefer bounded evidence repair in the worker return) |
| reviewerOwnedClosurePaths | exact four worker outputs plus necessary bounded evidence repair |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | T3A-C2 tooling dispatch, 2026-09-19 |
| Working directory | repository root |
| Command or tool surface | governed reads, ceremony metadata recomputation, scaffold/read-ahead, apply_patch and gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | T2F Group 1 plus committed T3A-C2 Local verification |
| Before status evidence | HEAD `835dfc39d`; tracked worktree clean; staging empty; thirteen pre-existing parked untracked paths isolated |
| After status evidence | exact paired dispatch paths pending before commit; parked paths unchanged |
| Diff evidence | paired packet staged alone before dispatch commit |
| Approval boundary | tooling and hermetic tests only |
| Claim boundary | no credential, Party A execution, operational source, admission, live/runtime/public effect |
| Agent type | Local dispatcher and later reviewer/closer |
| Invocation ID | `acel-g1-t3a-c2-source-tooling-dispatch-20260919` |
| Expected manifest | paired T3A-C2 baseline and work order |
| Actual changed set | reconciled before dispatch commit |
| Manifest delta | pending exact staging reconciliation |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | source-creation tooling and hermetic validation only |
| claimDisposition | CLAIM_REJECTED for real source creation, runtime enforcement, admission or consumer wiring |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker return does not yet exist |
| actionEvidence | ACTION_EVIDENCE_PRESENT: paired dispatch only |
| invocationBoundary | no Party A or real-mode invocation by worker |
| interceptionBoundary | no runtime wrapper/proxy or agent-control claim |
| claimLanguage | tooling implemented/tested; source remains not created |
| forbiddenExpansion | credentials, alternate user, actual sources, T3E wiring, live/public/deployment |

## Claim Boundary

This order authorizes tooling and hermetic tests only. It does not authorize
the worker to create operational source files, touch private material, claim
Party A authority, promote the key, admit a candidate, wire T3E, run live AI
governance proof, public-sync or deploy.

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`

Reason: bounded first-party Windows and local-source tooling; no legacy or
external corpus is ingested, mapped or absorbed.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md` |
| Chain map route | N/A with reason: direct operator ceremony output -> Local verification -> bounded INTERNAL_AGENT tooling |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 1 contract and T3A-C2 Local verification audit |
| Disposition | local first-party implementation only |
| Claim boundary | no external source authority, external corpus, remote implementation or provider claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-control tooling bound to a local principal and a
not-yet-created private source.

## Operator Checkpoint

After Local accepts the worker tooling, the operator alone runs its explicit
real mode under `LAM-RUBY\cvf-g1-party-a`. Key promotion, Local source
verification, T3E consumer wiring and candidate admission remain later
checkpoints; this dispatch opens none of them.
