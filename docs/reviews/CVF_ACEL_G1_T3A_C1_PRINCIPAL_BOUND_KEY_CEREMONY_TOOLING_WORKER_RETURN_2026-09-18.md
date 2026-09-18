# CVF ACEL G1 T3A-C1 Principal-Bound Key Ceremony Tooling Worker Return

Memory class: FULL_RECORD

docType: review

Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md`

executionBaseHead: `e0c461e60e1c7e09878882400b9d98aae61ec082`

rawMemoryReleased=false

contractProfile: WORKER_RETURN_FULL_GATE_V1

Date: 2026-09-18

Batch ID: ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING

## Source Inventory

| File | Action |
|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md` | READ |
| `docs/baselines/CVF_GC018_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md` | READ |
| `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` | READ |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | READ (Source Group 1 section) |
| `CVF_SESSION_MEMORY.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `governance/compat/run_worker_return_scaffold.py` | READ |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | READ |
| `governance/compat/check_governed_file_size.py` | READ (extension scope) |
| `scripts/acel_g1_party_a_key_ceremony.ps1` | CREATED |
| `scripts/acel_g1_party_a_key_ceremony.js` | CREATED |
| `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md` | CREATED |

## Rework Convergence Self-Proof

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: NOT_APPLICABLE_WITH_REASON: tooling tranche makes no production, runtime or source-readiness binding
adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
internalAgentInvocationCount: 1
externalAgentInvocationCount: 0
providerCallCount: 0
tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: internal-agent shared-workspace execution has no provider usage meter; zero provider or external quota was consumed
terminalReadinessVerdict: READY_FOR_REVIEW

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-g1-t3a-c1-principal-bound-key-ceremony-tooling",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": ["ceremony_tooling_not_implemented", "real_party_a_ceremony_not_executed", "group1_source_not_created"],
    "resolved": ["ceremony_tooling_not_implemented"],
    "retained": ["real_party_a_ceremony_not_executed", "group1_source_not_created"],
    "new": [],
    "reopened": [],
    "current": ["real_party_a_ceremony_not_executed", "group1_source_not_created"]
  },
  "resolutionEvidence": {
    "ceremony_tooling_not_implemented": {
      "evidenceClass": "EXECUTABLE_PROOF",
      "evidencePath": "scripts/acel_g1_party_a_key_ceremony.ps1",
      "sha256": "5731949c29c676a47e34e64f55281999742100ceb3b36b77bfd842aeebf584dd",
      "locator": "function Invoke-SelfTest",
      "claimId": "ACEL-G1-T3A-C1-TOOLING-IMPLEMENTED"
    }
  },
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "ACEL-G1-T3A-C1-TOOLING-IMPLEMENTED",
      "claimClass": "OTHER",
      "proofClass": "NAMED_OBSERVABLE_PROOF",
      "evidenceRef": "docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "NO_SUCCESSOR"
}
```

The two retained blockers are intentional. This tranche was authorized to build
tooling only; executing the ceremony and creating the Group 1 source remain
separate operator and Local checkpoints.

## Purpose

Implement the exact three authorized outputs for ACEL-G1-T3A-C1: a fail-closed
PowerShell ceremony wrapper, a minimal Node Ed25519 generator helper, and this
evidence return. The wrapper must be able to perform a later operator-run,
principal-bound key ceremony without exposing private bytes, while proving its
guards now under the current worker identity using only ephemeral material.

This return does not claim that any Party A ceremony occurred, that a Group 1
source exists, or that the tooling has been accepted.

## Target / Source

| Target | Source authority |
|---|---|
| exact three worker outputs | Required Artifact Manifest, work order |
| C1-01 through C1-10 contracts | Acceptance Matrix, work order |
| Ed25519 public row and lifecycle boundary | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`, Source Group 1 |
| new-key route, private material outside repository | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md`, Decision / Disposition |
| expected principal facts | paired baseline, Decision / Baseline / Proposed Tranche |
| hermetic test and cleanup requirement | paired baseline, Evidence / Verification Boundary |

Expected principal per the paired baseline: `cvf-g1-party-a`, SID
`S-1-5-21-1644666849-912006174-747199667-1006`. The worker did not log on as,
authenticate as, read the profile of, or modify that account.

## Scope / Methodology

1. Froze execution state: captured HEAD, full untracked status, empty staging,
   and SHA-256 for all thirteen parked paths before any edit.
2. Probed the three output paths for collision; all three were absent.
3. Read the work order, paired baseline, T3A route audit, T2F Source Group 1,
   startup surfaces and guard orientation.
4. Ran the pre-implementation autorun gate before writing any file.
5. Verified platform primitives independently before designing around them:
   Node v22.17.0 Ed25519 shapes and PowerShell 7.5.4 DPAPI CurrentUser
   roundtrip.
6. Implemented the Node helper, then the PowerShell wrapper.
7. Ran the hermetic self-test, repaired the defects it exposed, and re-ran to a
   clean pass.
8. Ran an independent out-of-band negative probe invoking the real ceremony
   path with the actual expected Party A name and SID from the worker identity.
9. Recomputed parked hashes, confirmed empty staging and unchanged HEAD, and
   authored this return.

Delegation depth was zero; no subagent, provider or external surface was used.

## Findings / Position

### Implemented behavior

`scripts/acel_g1_party_a_key_ceremony.js` generates one Ed25519 key pair using
Node core `crypto`, validates the PKCS8 DER length, cross-checks the raw public
key taken from the SPKI tail against the JWK coordinate, re-imports the exact
PKCS8 bytes the caller will persist, proves sign/verify, and emits a single
JSON object on stdout. It accepts no arguments, writes no file, reads no
existing key, and has no standalone logging path; on any failure it writes only
error text to stderr and exits non-zero.

`scripts/acel_g1_party_a_key_ceremony.ps1` runs guards in a fixed order so that
no key can exist until all of them pass: exact account name, exact SID,
non-elevated context, expected-account readability and state, output-path
resolution, collision refusal, then interactive typed confirmation. Only after
all of those does it invoke the helper, protect the PKCS8 with DPAPI
CurrentUser, and write an exclusive-create ciphertext blob plus non-secret
public metadata, cleaning up partial writes on failure.

### Local reviewer findings and repairs

The Local reviewer found three connected safety-proof defects before acceptance:

| ID | Finding | Severity | Reviewer repair |
|---|---|---|---|
| T3A-C1-RV-01 | `Invoke-KeyGeneratorHelper` used `Start-Process -RedirectStandardOutput` to a temporary file. That file contained the helper JSON and therefore plaintext private PKCS8 before DPAPI protection, directly contradicting C1-05 and the return's no-plaintext-file claim. Best-effort overwrite/delete did not make the original write compliant. | CRITICAL | Replaced filesystem redirection with `System.Diagnostics.ProcessStartInfo` anonymous stdout/stderr pipes and in-memory reads; added C1-04-D with isolated TEMP/TMP and zero-file evidence. |
| T3A-C1-RV-02 | C1-08-C launched the non-interactive child with a deliberately wrong principal, so it stopped at `PRINCIPAL_NAME_MISMATCH` and could not prove the repaired confirmation guard was reached. The return overclaimed that this child validated the `Read-Host` boundary. | HIGH | The child now uses the exact current non-elevated account name and SID, passes the earlier guards, and must exit non-zero with `NONINTERACTIVE_EXECUTION_REJECTED` plus zero output files. |
| T3A-C1-RV-03 | The ceremony ignored a false return from `Set-CeremonyDirectoryAcl`; an ACL-hardening failure emitted only a warning and key generation continued, contradicting the fail-closed custody posture. | HIGH | Actual ceremony now raises `ACL_HARDENING_FAILED` before helper invocation; C1-03-F verifies protected inheritance and no unexpected allow SID on the sandbox. |

Both repairs are localized to the existing reviewer-owned three-path set and
preserve the objective, algorithm, authority ceiling, external-effect class
and commit ownership. No re-dispatch or operator checkpoint was warranted.

### Defects found and repaired during implementation

| # | Defect | Detection | Repair |
|---|---|---|---|
| 1 | Helper used one `Ed25519` constant for both Node's key-generation type name and the JWK curve name; Node requires lowercase `ed25519` for generation, so generation threw | first helper shape run | split into separate `NODE_KEY_TYPE`, `JWK_CURVE` and `ALGORITHM` constants |
| 2 | `Start-Process -ArgumentList @($HelperPath)` did not quote the path; this workspace root contains spaces, so Node received `D:\UNG` and failed `MODULE_NOT_FOUND` | first full self-test run | explicit quoting of the helper path in the argument list |
| 3 | Non-interactive detection relied on `[System.Environment]::UserInteractive`, which on Windows reports the window station and stays `$true` under `pwsh -NonInteractive` and under redirected stdin; an automated run would have passed the guard | direct platform probe after the first clean pass | detection moved onto `Read-Host` itself, which throws `PSInvalidOperationException` in NonInteractive mode; any failure to obtain a typed answer, and any empty answer, is now rejected |
| 4 | Entry-point error handler prefixed an already-prefixed guard message, producing `[GUARD] [GUARD] ...` | out-of-band negative probe output | handler now adds a prefix only for genuinely unhandled exceptions |

Defect 3 is the substantive one. The original self-test asserted only that the
guard was *reachable*, which would have passed while the guard itself was
ineffective. It was replaced by a test that spawns this script in a real
`pwsh -NonInteractive` child and requires a non-zero exit with zero files
produced.

### Acceptance matrix disposition

| ID | Required contract | Evidence | Disposition |
|---|---|---|---|
| C1-01 | exact name and SID compared to current identity before generation | `Assert-ExpectedPrincipal` runs before any helper call; cases C1-01-A (wrong name rejected `PRINCIPAL_NAME_MISMATCH`), C1-01-B (correct name, wrong SID rejected `PRINCIPAL_SID_MISMATCH`), C1-01-C (exact match accepted) | PASS |
| C1-02 | reject elevated context and disabled/expired expected account | C1-02-A rejects a mocked elevated principal with `ELEVATED_CONTEXT_REJECTED`; C1-02-B rejects an unreadable account with `ACCOUNT_STATE_UNREADABLE`; `Assert-ExpectedAccountUsable` is read-only `Get-LocalUser` and additionally rejects `ACCOUNT_DISABLED` and `ACCOUNT_EXPIRED`; no local account was created or modified | PASS |
| C1-03 | output outside repository, under LocalAppData; traversal and collision reject | C1-03-A through C1-03-E cover repository, traversal, relative, empty and accepted sandbox paths; repaired C1-03-F verifies protected inheritance and current-SID-only allow rules; actual ceremony fails `ACL_HARDENING_FAILED` before generation | PASS_AFTER_REVIEWER_REPAIR |
| C1-04 | Node core crypto Ed25519; PKCS8 DER plus raw 32-byte public key through captured output only | C1-04-A PKCS8 48 bytes and raw public key 32 bytes; C1-04-B base64url roundtrip; C1-04-C `HELPER_MISSING`; C1-04-D isolated TEMP/TMP stayed empty while anonymous process pipes captured helper output | PASS_AFTER_REVIEWER_REPAIR |
| C1-05 | DPAPI CurrentUser protection before disk; only encrypted blob written; references cleared | reviewer removed the plaintext temporary stdout file; C1-05-A ciphertext differs from plaintext; C1-05-B unprotect reproduced PKCS8; C1-05-C recovered key signed and verified; C1-07-B found no plaintext under the sandbox | PASS_AFTER_REVIEWER_REPAIR |
| C1-06 | public metadata carries required fields, never private material | C1-06-A all 12 required fields present; C1-06-B secret-pattern scan found no private DER, no DPAPI blob and no secret-shaped field name; C1-06-C self-test output marked `TEST_ONLY_NON_OPERATIONAL` | PASS |
| C1-07 | exclusive create and failure cleanup; partial files cannot look successful | C1-07-A both files created; C1-07-C `OUTPUT_TARGET_COLLISION`; C1-07-D `EXCLUSIVE_CREATE_FAILED` on `FileMode::CreateNew`; C1-07-E injected metadata-write failure removed the already-written private-key blob | PASS |
| C1-08 | default is dry-run/self-test; real ceremony needs explicit flag, exact principal and interactive confirmation; noninteractive execute rejects | C1-08-A default parameter set is `SelfTest`; C1-08-B no durable output; repaired C1-08-C uses exact current name/SID and observes exit 1, `NONINTERACTIVE_EXECUTION_REJECTED`, zero files; C1-08-D independently exercises the same guard | PASS_AFTER_REVIEWER_REPAIR |
| C1-09 | worker never invokes the real ceremony or Party A context, and never accesses any existing local test key | C1-09-A self-test ran as `LAM-RUBY\DELL` (SID `...-1001`), not the expected Party A principal (SID `...-1006`); out-of-band probe with the real expected name and SID was rejected `PRINCIPAL_NAME_MISMATCH` before any directory or key was created; the prior DELL-user test key path was never read; command ledger below | PASS |
| C1-10 | exact three outputs, empty staging, thirteen parked paths unchanged | `git status --short --untracked-files=all` shows exactly the three new paths plus the thirteen pre-existing parked entries; staging empty; all thirteen parked SHA-256 values byte-identical before and after | PASS |

### Self-test result

32 cases total, 32 passed, 0 failed, exit code 0 after reviewer repair.

## Risk / Corrective Action

| Risk | Status | Control |
|---|---|---|
| same-user DPAPI context is not agent isolation | ACCEPTED_AND_DISCLOSED | any process running as the ceremony user can invoke that user's DPAPI context; the ACL hardening is defense in depth only, and this is documented in the script rather than claimed as isolation |
| best-effort memory clearing is not guaranteed erasure | ACCEPTED_AND_DISCLOSED | `Clear-ByteArray` zeroes buffers it can reach; the .NET runtime may retain copies, and the doc comment says so |
| `-ExecuteCeremony` still depends on the operator running it as the right principal | CONTROLLED | the tool cannot itself elevate or switch user; it refuses unless the running identity already matches exactly on both name and SID |
| a self-test artifact could be mistaken for a real ceremony product | CONTROLLED | self-test metadata carries `ceremonyDisposition: SELF_TEST` and `testDisposition: TEST_ONLY_NON_OPERATIONAL`, and the sandbox is deleted |
| metadata could drift toward carrying secret-shaped fields | CONTROLLED | C1-06-B scans the serialized metadata for the private DER, the DPAPI ciphertext and secret-shaped field names on every run |
| Group 1 field-name alignment is not yet verified against a live registry | DEFERRED_TO_LOCAL | the metadata uses `publicKeyBytesBase64`, `keyId` and `algorithm` consistent with the Source Group 1 contract, but carries `registryDisposition: SOURCE_NOT_CREATED`; no registry row or lifecycle receipt is produced or implied |

No corrective action remains open. Local notes that the
tool encodes the public key as base64url while the Source Group 1 row field is
named `publicKeyBytesBase64`; if Group 1 is later created expecting standard
base64, that conversion is a source-creation decision, not a tooling defect,
and is deliberately left to the source-establishment tranche.

## Decision / Disposition

`ACCEPTED_BY_REVIEWER_WITH_REPAIRS`.

The three authorized outputs exist and are uncommitted. All ten acceptance
rows pass with named observable evidence after the three disclosed Local repairs. The worker did not stage, commit,
access any credential, run as any alternate user, create a real Party A key,
create a Group 1 registry or lifecycle file, or claim source readiness.

Local completed the review and evidence repair and owns the material commit.
The actual Party A ceremony remains a separate operator checkpoint.

## Local Review Dependency-Closure Matrix

| Review dimension | Evidence examined | Final disposition |
|---|---|---|
| contract and schema | C1-01 through C1-10; T2F Group 1 key fields | PASS after bounded repairs; base64url is the existing contract encoding despite the legacy field name |
| authority and source claims | work order, baseline, T3A route audit, worker return | PASS; no ceremony, source, admission or custody claim added |
| path and repository boundary | exact three output paths plus thirteen parked hashes | PASS; no fourth path and no parked mutation |
| private-material boundary | helper launch/capture, DPAPI order, output writes | PASS after removal of plaintext temporary redirection |
| negative cases | wrong name/SID, elevation, paths, collision, partial write, non-interactive execution | PASS; final non-interactive child reaches the confirmation guard under exact current identity |
| custody hardening | output directory ACL before helper launch | PASS after fail-closed ACL repair and C1-03-F |
| test adequacy | final hermetic run and syntax checks | PASS: 32/32, zero durable ceremony output |
| closure range and commit plan | three owned paths; material commit then continuity commit | PASS; one material and at most one continuity commit planned |

## Review-Dispatch Convergence Control

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_IMPLEMENTED

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: RETURN_FOR_LOCAL_REVIEW

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## P4 Automatic Evidence Observation Block

p4ObservationEligibility: AUTO
p4ObservationPhase: N/A with reason: not a natural P4 observation candidate
p4HardObligationLocator: N/A with reason: not a natural P4 observation candidate
p4HardObligationPattern: N/A with reason: not a natural P4 observation candidate
p4SourceAuthorityLocator: N/A with reason: not a natural P4 observation candidate

## Architecture Readiness Echo

architectureMatrixSchema: NOT_APPLICABLE_WITH_REASON: dispatching work order did not declare Architecture-Readiness Admission: REQUIRED
architectureMatrixCanonicalDigest: N/A with reason: no accepted architecture matrix to echo
architectureSemanticReviewPath: N/A with reason: no accepted architecture matrix to echo
architectureSemanticReviewCommit: N/A with reason: no accepted architecture matrix to echo
architectureSemanticReviewFileSha256: N/A with reason: no accepted architecture matrix to echo
architectureBindingEchoDisposition: N/A with reason: no accepted architecture matrix to echo

## Claim Boundary

This accepted return claims exactly one thing: the authorized ceremony tooling
exists and its repaired guards behave as specified under hermetic test on this
machine at this execution base.

It does not claim that a Party A ceremony was performed, that a principal-bound
operational key exists, that Group 1 is created or verified, that any candidate
is admitted, or that the tooling has executed a real ceremony. It makes no runtime, live-proof,
provider, deployment, public-sync or production readiness claim. Gate and
self-test passes are behavioral evidence, not custody or source proof. No
credential was requested, received, stored or used.

## Return-Time Closeability Recheck

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: REVIEWER_LOCAL_REPAIR

workerRedispatchAllowed: NO

returnTimeRecheckResult: CONFIRMED_UNCHANGED

The retained ceremony and source blockers are parked operator/Local checkpoints
outside this tranche's declared scope, not outside-authority blockers on
closing the tooling tranche itself.

| gateId | mustPassBy | worker disposition |
|---|---|---|
| pre_implementation_autorun | WORKER_RETURN | PASS: COMPLIANT in 7.35s before any edit |
| focused_checker_tests | WORKER_RETURN | PASS: 32/32 hermetic self-test cases after reviewer repair, exit 0 |
| adif_integrity | WORKER_RETURN | PASS: resolver returned 0 defects for worker/implementation |
| worker_return_fast | REVIEW | PASS after final reviewer repairs |
| reviewer_fast | PRE_MATERIAL_COMMIT | PASS: 68/68 after final reviewer repairs |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer-owned; enforced by material commit hook |
| terminal_completion_review | PRE_MATERIAL_COMMIT | PASS: Local dependency-closure matrix and bounded disposition above |

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT held; no
fourth file was required and no path family expanded.

## Frozen-Path Reconciliation

All thirteen parked untracked paths were hashed before implementation and
rehashed after. Every value is byte-identical; no parked path was opened for
write, renamed, deleted or staged.

| Parked path | SHA-256 before and after |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | `5c26e2bc732da98082ed3b0c1ed4c35fdcb40c5c5b16023e281ea6a3a741a37f` |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | `24302b66728de7de3173b4fcb999034412ef4a47c8c27f5e17fbf581352b8046` |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | `02b97f0db77b6518000c13aff30bc131b88b426809f9f8aa43c89bad2b5ebbda` |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json` | `0bf99eeaf3e8a979000ffc411639a987abf60d1d5ff556dad38ba354b24f137e` |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | `5147bf905113e4c750f6b7f4aa84e1aeb4575417299258ad10dcf8ebbbb5575a` |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json` | `5bfe577495bac91b99344827172d859ff0389cf1f67e14097d5af113a16eaeb9` |
| `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md` | `97510bff2a40e4868625d1f016e87d2bbaab9812380ded5a20c2f24b65625708` |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | `3ddb27af5abf0d8197bfdaa28eac2e7b83c422c3342a4b3acb2abf25b65cdb86` |
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md` | `f12688934bcb1ef0fdaaea1ae45186cce14cfcba69fc5061334abbee8e8462f6` |
| `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md` | `25963195262048746436daee2ab4b2304fa96d54c8197ed375ab98e5e7dd29ce` |
| `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md` | `1ac61b304063f57eda3f7db2a8ec3681a0af3d6c8e58ec04c3d5228e7f759594` |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | `761eefa1f093e4cdddb4e73496b04f9694a15622a5ce34dd685d4acae3498d0f` |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | `ac85ed1b6ad5288c95aeada7baab45782c58f97bbdfd45cb4a126ea6a124eeec` |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/run_worker_return_scaffold.py`; `governance/compat/build_worker_return_skeleton_scaffold.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_adif_defect_resolver.py` |
| literalTokensReviewed | `WORKER_RETURN_FULL_GATE_V1` contract profile; scaffold section order and headings; `rawMemoryReleased=false`; `executionBaseHead`; scaffold TODO placeholder tokens that must not survive; `CODE_EXTENSIONS` scope in the file-size checker |
| gateRunPurpose | confirm the return's required shape from generated scaffold source before drafting, then use the fast gate as confirmation rather than as a discovery loop |
| claimBoundary | this read-ahead covers the worker-return artifact shape and the two script paths' size scope only; it does not cover reviewer, closure or session-sync surfaces, and a gate PASS proves shape, not custody |

## Gate Evidence

| Command | Result |
|---|---|
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base e0c461e60e1c7e09878882400b9d98aae61ec082 --head HEAD` | PASS (COMPLIANT in 7.35s) |
| `pwsh -NoProfile -File scripts/acel_g1_party_a_key_ceremony.ps1 -SelfTest` | historical worker run PASS (30/30 cases, exit 0); superseded by final reviewer rerun below |
| `python governance/compat/run_worker_return_fast_gate.py` | FAIL on first run (7 checkers), then PASS after repair: `COMPLIANT: worker-return fast gate passed in 4.21s` |
| final `python governance/compat/run_worker_return_fast_gate.py` after Local repair | PASS: reviewer-fast 68/68 and worker-return bundle COMPLIANT |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base e0c461e60e1c7e09878882400b9d98aae61ec082 --head HEAD --enforce` | PASS; valid returned evidence consumed, exact owned commit subset retained despite parked worktree entries |
| `git diff --check` | PASS (no whitespace errors) |
| `git status --short --untracked-files=all` | PASS (exact three new paths; staging empty) |

receiptEvidence: CVF_RECEIPT_PRESENT - `.cvf/runtime/autorun-receipts/pre-implementation.json`

## Actual Changed Set

- `scripts/acel_g1_party_a_key_ceremony.ps1`
- `scripts/acel_g1_party_a_key_ceremony.js`
- `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md`

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: this tranche created two
new script paths and one review artifact; no core guard, checker or governance
automation file was modified.

Protected paths:
- N/A with reason: no protected guard path was touched

Operator authorization: N/A with reason: no guard-maintenance authorization was
required or requested

Rollback boundary: N/A with reason: all three outputs are new untracked files;
deleting them restores the execution base state exactly

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | operator authorization plus Local Windows verification -> INTERNAL_AGENT tooling -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this worker return |
| Internal source | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source was admitted; all facts come from governed files and local command results |
| Claim boundary | CVF source authority remains repo-governed surfaces only; Local remains final decision owner |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md"}
```

No external agent participated in this tranche; the binding is echoed from the
parent work order so the invariants remain explicit and Local remains the final
decision owner.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this worker return is a bounded implementation return,
not a rescan, intake-refresh, or source-backed reassessment output.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: bounded
  named-file implementation tranche; no corpus inventory, no "all files read"
  claim, and no corpus-derived knowledge map is asserted in this worker return.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| `[System.Environment]::UserInteractive` is not a valid non-interactive signal on Windows; it stays true under `pwsh -NonInteractive` and redirected stdin. This is a generalizable trap for any future agent writing a fail-closed interactive guard. | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | record that interactive-confirmation guards must be proven by a real non-interactive child process, not by a property read | deferred to Local ADIF disposition |
| A negative test that asserts a guard is merely "reachable" can pass while the guard itself is ineffective; this is a systemic test-strength trap, not a one-off. | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | prefer end-to-end rejection proof over property assertion for any fail-closed control | deferred to Local ADIF disposition |
| Windows paths containing spaces break `Start-Process -ArgumentList` without explicit quoting; this workspace root contains spaces, so it recurs for any future worker spawning a child process here. | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | work order's `unicodePathHandling` clause already covers it; quoting applied and covered by the self-test helper path | handled |
| The worker-return scaffold emits placeholder field values (`COMPLETE_INITIAL_ACCEPTANCE_MATRIX`, `BASELINE_NEGATIVE_TESTS_IMPLEMENTED`, a string-valued `resolutionEvidence` binding, a prose-only retrospective) that seven enforcing checkers reject; a future worker following the scaffold faithfully still fails the first fast-gate run. | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | align `run_worker_return_scaffold.py` defaults with the enforcing checker vocabularies, or have the scaffold emit the required section set for the declared contract profile | deferred to Local ADIF disposition |
| Provider/cost lane applicability | RUNTIME_SIGNAL_GAP | COST_ECONOMICS_LEARNING | N/A_WITH_REASON | N/A with reason: internal-agent tranche consumed zero provider calls and zero external quota, so no provider-output or cost-economics finding exists | handled |

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_APPLICABLE.

### Expected Result

Before implementation the worker predicted that: Node core `crypto` would
produce a 48-byte PKCS8 DER and a 32-byte raw Ed25519 public key; DPAPI
CurrentUser would be reachable from PowerShell 7 and would round-trip those
bytes; a `.ps1` plus `.js` pair could satisfy every C1 row without a fourth
file; and that guarding on `[System.Environment]::UserInteractive` would be
sufficient to refuse unattended execution.

### Evidence Comparison

| Prediction | Actual evidence | Outcome |
|---|---|---|
| PKCS8 DER 48 bytes, raw public key 32 bytes | direct Node probe, then self-test case C1-04-A | CONFIRMED |
| DPAPI CurrentUser reachable and lossless under PowerShell 7.5.4 | direct probe (262-byte ciphertext, roundtrip true), then C1-05-A/C1-05-B | CONFIRMED |
| two script files satisfy all C1 rows with no fourth output | final 32/32 self-test cases across C1-01..C1-09; manifest delta MATCH | CONFIRMED_AFTER_REVIEWER_REPAIR |
| `UserInteractive` is a valid non-interactive signal | probe showed it returns `True` under `pwsh -NonInteractive` and under redirected stdin | CONTRADICTED |
| helper path could be passed unquoted to `Start-Process` | first full self-test run failed `MODULE_NOT_FOUND` on `D:\UNG` | CONTRADICTED |
| one `Ed25519` constant serves both Node generation and JWK curve naming | generation threw: Node requires lowercase `ed25519` | CONTRADICTED |

### Contradiction Or Gap Disposition

Three predictions were contradicted by direct evidence and all three were
repaired rather than rationalized, with the repairs recorded in Findings.

The `UserInteractive` contradiction is the material one: it was discovered only
because the worker continued probing after the suite was already green, and it
would have shipped an ineffective fail-closed control that a passing test
asserted was working. The replacement proof spawns a real `pwsh -NonInteractive`
child and requires a non-zero exit with zero files produced.

Remaining gap, disclosed not closed: the public-key encoding is base64url while
the Source Group 1 row field is named `publicKeyBytesBase64`. This is not
resolvable inside a tooling tranche because the registry does not exist; it is
routed to the source-establishment tranche and flagged for Local in Risk /
Corrective Action.

### Claim Update

Claim narrowed. The initial framing "the ceremony tool enforces interactive
confirmation" was narrowed to "the tool refuses to proceed whenever the host
cannot supply a typed confirmation, proven by a real non-interactive child
process." No claim in this return rests on provider memory; every asserted fact
traces to a command result captured in this session. Claim boundaries on
custody, ceremony execution and source readiness are unchanged and remain
negative.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private principal-bound ceremony tooling in the private provenance
workspace; no public-sync authorization exists for these paths.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: HELPER_GAP
observedStep: worker-return authoring after `run_worker_return_scaffold.py --emit`; the generated checker-safe skeleton omits three sections the work order's Worker Return Packet Shape Contract requires (Target / Source, Return-Time Closeability Recheck, Frozen-Path Reconciliation) and emits placeholder field values that seven enforcing checkers reject, so the first fast-gate run failed and seven repairs were needed despite following the scaffold
preventiveControlCandidate: HELPER_DIAGNOSTIC

The scaffold helper removed most shape-discovery cost, but not all of it: the
generated skeleton is section-complete for its own template yet its default
field values do not satisfy the enforcing checkers, so one gate-failure round
was still required. Reading each failing checker's source for its exact allowed
vocabulary, rather than guessing from the failure text, made that single round
sufficient. The work order's `unicodePathHandling` clause was directly
predictive; the space-in-path defect it warned about did occur, and reading
that clause beforehand made the failure immediately recognizable rather than
mysterious. The most valuable step was probing platform behavior after the
first clean pass instead of stopping at green, which is what exposed the
ineffective non-interactive guard.

## Worker Return Scaffold Effectiveness Measurement

| Measurement | Result |
|---|---|
| scaffoldUsedBeforeLongDraft | YES |
| scaffoldMissingSectionFound | Target / Source, Return-Time Closeability Recheck, Frozen-Path Reconciliation (required by the work order's Worker Return Packet Shape Contract but absent from the generated scaffold; added manually) |
| firstWorkerReturnFastGateResult | FAIL |
| postScaffoldManualRepairCount | 7 |

## Worker Return Jurisdiction Block

| Field | Disposition |
|---|---|
| capturedArtifacts | `scripts/acel_g1_party_a_key_ceremony.ps1`; `scripts/acel_g1_party_a_key_ceremony.js`; `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md` |
| capturedOperations | governed file reads; pre-implementation autorun gate; Node and PowerShell platform probes; hermetic self-test; out-of-band negative ceremony probe; hashing and status capture |
| deferredOperations | reviewer-fast, pre-commit, terminal completion review, material commit, continuity commit; all reviewer or closer owned |
| outOfScopeRequests | N/A with reason: no credential, alternate-user execution, account mutation, real ceremony, source creation or fourth output was requested or performed |
| reviewerActionNeeded | reviewer completed bounded source/evidence repair and acceptance; material commit remains reviewer-owned |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | INTERNAL_AGENT T3A-C1 tooling worker |
| Provider or surface | private CVF workspace, shared worktree |
| Session or invocation | T3A-C1 tooling implementation, 2026-09-18 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed file reads; `git` status/hash/diff; `python governance/compat/*`; `node`; `pwsh`; `sha256sum` |
| Target paths | the exact three declared worker outputs |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md` Required Artifact Manifest and `laneOwnedPaths` |
| Before status evidence | HEAD `e0c461e60e1c7e09878882400b9d98aae61ec082`; tracked worktree clean; staging empty; thirteen parked untracked paths hashed |
| After status evidence | HEAD unchanged; staging empty; three new untracked paths; thirteen parked hashes byte-identical |
| Diff evidence | `git diff --name-status HEAD` empty (no tracked file modified); `git diff --check` clean; all three outputs are new untracked files |
| Approval boundary | tooling and hermetic tests only; no credential, no alternate-user execution, no real ceremony, no source creation, no staging, no commit |
| Claim boundary | no custody, ceremony, registry, admission, runtime, provider, public-sync or deployment claim |
| Agent type | worker |
| Invocation ID | `acel-g1-t3a-c1-tooling-worker-20260918` |
| Expected manifest | `scripts/acel_g1_party_a_key_ceremony.ps1`; `scripts/acel_g1_party_a_key_ceremony.js`; this worker return |
| Actual changed set | exactly those three paths |
| Manifest delta | MATCH: expected set equals actual set; no fourth output |
| Deletion or rename disposition | N/A with reason: no file was deleted or renamed; self-test temporary directories were created and removed outside the repository under the current user's LocalAppData |

### Command ledger: Party A non-contact evidence

No command in this session supplied a password, invoked `runas`, used
`Start-Process -Credential`, opened a `cvf-g1-party-a` profile path, or read the
pre-existing DELL-user test key custody path. The only commands naming the
expected principal were: the read-only `Get-LocalUser` guard exercised against a
deliberately nonexistent probe account, and one out-of-band negative probe that
passed the expected name and SID as *expected* values and was rejected with
`PRINCIPAL_NAME_MISMATCH` before any directory or key was created.

## Local Reviewer Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer/closer |
| Provider or surface | private CVF workspace, shared worktree |
| Session or invocation | T3A-C1 returned-result review, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, source inspection, apply_patch, PowerShell parser, Node syntax check, hermetic self-test, worker-return and reviewer gates, Git |
| Target paths | exact three worker outputs |
| Allowed scope source | work order Reviewer Closure Conversion: exact three returned paths plus necessary Local evidence repair |
| Before status evidence | HEAD `e0c461e60`; three worker outputs untracked; thirteen parked paths untracked; staging empty |
| After status evidence | exact same three owned paths plus thirteen parked paths; no alternate-user or ceremony output; staging reconciled only for Local material commit |
| Diff evidence | T3A-C1-RV-01 through RV-03 and final 32/32 focused test; exact three-path material manifest |
| Approval boundary | reviewer-local correction within unchanged objective, paths, risk, authority and external-effect class |
| Claim boundary | tooling acceptance only; no Party A ceremony, operational key/source, live/runtime/public/deployment effect |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3a-c1-local-review-20260918` |
| Expected manifest | exact three T3A-C1 returned paths |
| Actual changed set | exact three T3A-C1 returned paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | principal-bound ceremony tooling implementation and hermetic guard proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: `.cvf/runtime/autorun-receipts/pre-implementation.json`; no ceremony receipt exists because no ceremony was performed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: three created paths, self-test transcript, negative probe results, before/after hashes |
| invocationBoundary | shared-workspace tooling under the current worker identity `LAM-RUBY\DELL` only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim; no credential, run-as or account interception |
| claimLanguage | implemented, reviewer-repaired and hermetically tested tooling accepted bounded; not ceremony-executed and not source-ready |
| forbiddenExpansion | real key generation for Party A, alternate-user execution, account mutation, registry or lifecycle creation, key promotion, verifier integration, candidate admission, provider or live use, public sync, deployment |

## git status --short

```
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts
?? docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md
?? docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json
?? docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md
?? docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json
?? docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md
?? docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md
?? docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md
?? docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md
?? docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md
?? docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md
?? governance/compat/check_task_class_calibration_owner_evidence.py
?? governance/compat/test_check_task_class_calibration_owner_evidence.py
?? scripts/acel_g1_party_a_key_ceremony.js
?? scripts/acel_g1_party_a_key_ceremony.ps1
```

Thirteen of these sixteen entries are the pre-existing parked paths, unchanged.
The three remaining entries are this tranche's authorized outputs.

## Changed Files

`git diff --name-status HEAD` returns no rows: no tracked file was modified.
All three outputs are new untracked files at the execution base.

| Path | Status | SHA-256 | Lines |
|---|---|---|---|
| `scripts/acel_g1_party_a_key_ceremony.ps1` | added (untracked), reviewer-repaired | `5731949c29c676a47e34e64f55281999742100ceb3b36b77bfd842aeebf584dd` | 1331 |
| `scripts/acel_g1_party_a_key_ceremony.js` | added (untracked) | `3c921b715bcb81e805c62dcf8308ce772f4d76504ead855bf7fe62a66034eac1` | 139 |
| `docs/reviews/CVF_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_WORKER_RETURN_2026-09-18.md` | added (untracked) | recorded by Local at review time | this file |

The two script hashes are the post-repair final versions recomputed by Local
after the final source edit.

## Command Evidence

| Command | Result |
|---|---|
| `git rev-parse HEAD` | `e0c461e60e1c7e09878882400b9d98aae61ec082` before and after implementation |
| `git log --oneline 40f6a8b51..HEAD` | two commits: `a4463a2e6` dispatch, `e0c461e60` session lane open; no worker-lane drift |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base e0c461e60e1c7e09878882400b9d98aae61ec082 --head HEAD` | COMPLIANT in 7.35s |
| `node --version` | `v22.17.0` |
| `pwsh -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'` | `7.5.4` |
| `node --check scripts/acel_g1_party_a_key_ceremony.js` | PASS (syntax valid) |
| PowerShell `Parser::ParseFile` on the wrapper | PASS (0 parse errors) |
| `pwsh -NoProfile -File scripts/acel_g1_party_a_key_ceremony.ps1 -SelfTest` | reviewer rerun PASS: 32 cases total, 32 passed, 0 failed, exit code 0; ACL hardening verified; exact-current-principal noninteractive child reached `NONINTERACTIVE_EXECUTION_REJECTED`; helper-capture TEMP/TMP remained empty |
| `pwsh -NoProfile -NonInteractive -File scripts/acel_g1_party_a_key_ceremony.ps1 -ExecuteCeremony -ExpectedAccountName "LAM-RUBY\cvf-g1-party-a" -ExpectedAccountSid "S-1-5-21-1644666849-912006174-747199667-1006" -OutputDirectory "<disposable LocalAppData probe path>"` | REJECTED `PRINCIPAL_NAME_MISMATCH`, exit 1, probe directory never created |
| `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role worker --lifecycle-phase implementation` | 0 candidates, 0 returned defects |
| `python governance/compat/run_worker_return_fast_gate.py` | first run FAIL (semantic convergence, worker experience retrospective, review cost control, gate-to-role closeability, finding-to-governance learning, external knowledge intake routing, epistemic process packet); final run COMPLIANT in 4.21s |
| `git diff --check` | clean |
| `git diff --cached --name-only` | empty (staging empty) |
| `git status --short --untracked-files=all` | sixteen untracked entries: thirteen parked plus three authorized outputs |
| `sha256sum` over the thirteen parked paths, before and after | all thirteen byte-identical |
| residue check of `%LOCALAPPDATA%\CVF_ACEL_G1_KEY_CEREMONY_SELFTEST_*` | none present; all self-test sandboxes removed |
| residue check of `%LOCALAPPDATA%\CVF\ACEL_G1\party_a_key` | absent; no durable ceremony output was ever created |

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: HEAD unchanged at
`e0c461e60e1c7e09878882400b9d98aae61ec082`; staging empty; no `git add`,
`git commit`, `git stash` or any other index or history mutation was performed
by the worker. Reviewer/closer owns material commit.

## Machine Closure Package

| Artifact | Evidence | Disposition |
|---|---|---|
| Worker return status | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS` | Local accepted after three bounded source/evidence repairs |
| Work order status | `dispatchWorkOrder: docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3A_C1_PRINCIPAL_BOUND_KEY_CEREMONY_TOOLING_2026-09-18.md` | N/A with reason: reviewer/closer owns closure conversion |
| Changed set | `## Actual Changed Set` | exactly three real paths listed |
| Gate evidence | `## Gate Evidence` | pre-implementation COMPLIANT; final self-test 32/32; reviewer/closure gates recorded after final edit |
