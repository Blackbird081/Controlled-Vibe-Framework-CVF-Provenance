# CVF ACEL G1 T3C-C2 Local Readability Repair Decision

Memory class: governed-review

docType: review

Status: REWORK_REQUIRED_OPERATOR_REPAIR_READY

Date: 2026-09-22

Batch ID: ACEL-G1-T3C-C2-LOCAL-READABILITY-REPAIR

Review base head: `2c492efffe`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record Local's review of the one-time Party B Group 3 ceremony return and the
bounded correction required before the created source can be accepted. The
ceremony reported one observation, but the created file's exact protected DACL
omitted the Local reviewer reader required by the governing T2F contract.

## Target / Source

| Source | Review use |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 3 allows `Local for audit` |
| `scripts/acel_g1_party_b_group3_observation_writer.ps1` | production DACL and postcondition implementation |
| `governance/compat/check_acel_g1_registry_observation_log.py` | independent content/hash/chain verifier |
| `governance/sources/registry_observation_log/LOG.jsonl` | real Party B ceremony product, pending Local verification |
| operator ceremony output | provisional snapshot, entry and observer identifiers; not acceptance evidence by itself |

## Scope / Methodology

Local compared the accepted source contract with the executable DACL builder
and postcondition, then attempted a direct read through both PowerShell and the
independent Python checker. Both reads failed with access denied. The parent
directory remained reachable and the source file existed, isolating the
failure to the file security policy rather than source absence.

The correction changes the future writer policy and supplies a one-time,
elevated, byte-preserving DACL repair. The repair accepts only the exact old
three-ACE state, verifies the observation with the independent checker before
mutation, adds only the exact Local SID read ACE, verifies the exact four-ACE
post-state and checker result, and requires byte-identical source content. Any
post-mutation failure restores the captured access descriptor.

## Findings / Position

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| T3C-C2-RV-1 | HIGH | The production writer granted FullControl to Party B, SYSTEM and Administrators only. The current non-elevated Local reviewer token therefore could not read `LOG.jsonl`, contradicting the T2F `Local for audit` reader contract. | REPAIR_REQUIRED |
| T3C-C2-RV-2 | MEDIUM | The hermetic test asserted that the real output must be absent, so the suite became permanently red after a legitimate ceremony. | REPAIRED_TO_ISOLATION_ORACLE |

The operator-reported identifiers are retained as expected values only:

- snapshotId: `snap-9037220e94434acaa4909cb1cba2e2fc-eec908be7c0243d4`
- snapshotHashHex: `87594cdcf8a1e0c3c4b439434aeda39444ff54a432674d97403f1980c995d883`
- entryHashHex: `a97f1066cc5fe33409eff6539c2ca68dcf72f794209c8de5df93a7f81dc6e1c3`
- observerIdentity: `S-1-5-21-1644666849-912006174-747199667-1009`

## Risk / Corrective Action

Run `scripts/run_cvf_g1_t3c_c2_local_verification_as_admin.cmd` once and accept
the UAC prompt. The launcher executes
`scripts/acel_g1_t3c_c2_local_read_acl_repair.ps1`; it does not request or store
any account password. No second Party B observation is authorized.

After the elevated transaction reports
`T3C_C2_LOCAL_VERIFICATION_AND_ACL_REPAIR_PASS`, Local must independently read
the now-readable source, rerun the checker and recompute both the decoded
snapshot hash and closed-preimage entry hash before any source-establishment
claim or successor tranche is opened.

## Independent Probe Evidence

| Probe | Result | Disposition |
|---|---|---|
| direct Local file read | access denied | DEFECT_CONFIRMED |
| Python checker against real log | `LOG_UNREADABLE` / access denied | DEFECT_CONFIRMED |
| corrected writer hermetic suite | 56/56 PASS | RETAINED_PENDING_REAL_PROBE |
| independent checker self-test | PASS | RETAINED_PENDING_REAL_PROBE |
| elevated DACL repair and real-source verification | not yet run | OPERATOR_UAC_CHECKPOINT |

## Decision / Disposition

`REWORK_REQUIRED_OPERATOR_REPAIR_READY`.

The Group 3 source remains
`OBSERVATION_APPENDED_PENDING_LOCAL_VERIFICATION`. T3C-C2 is not closed and no
T3D/T3E action is opened until Local completes the post-repair independent
probe.

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| writer security policy omitted a declared reviewer reader | ORCHESTRATOR_AND_IMPLEMENTATION_CONTRACT_GAP | GOVERNANCE_CONTROL_PLANE | RECORDED_FOR_EXISTING_PARKED_LEARNING_TRANCHE | require principal/DACL matrices to enumerate writer, reviewer and recovery principals before real-source authorization |
| self-test assumed durable source absence forever | TEST_ORACLE_LIFECYCLE_GAP | GOVERNANCE_CONTROL_PLANE | LOCAL_REPAIR_SUFFICIENT | assert self-test isolation/non-mutation, not global absence after establishment |

## Epistemic Process Block

### Expected Result / Prediction

The real source should have been readable by Local immediately after Party B
completed the ceremony because the governing source contract explicitly names
Local as an allowed audit reader.

### Evidence Comparison

The source exists, but both direct and checker reads fail. Source inspection
shows the writer's accepted DACL is exactly three FullControl ACEs and contains
no Local read ACE.

### Contradiction Or Gap Disposition

The operator output is insufficient for acceptance. The mismatch is resolved
through a byte-preserving, rollback-capable DACL repair followed by a separate
Local content and cryptographic verification.

### Claim Update

Group 3 creation is provisionally observed but remains unverified. No source
establishment, downstream binding or admission claim is accepted yet.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_acel_g1_registry_observation_log.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | review status, findings, independent probe, learning disposition, epistemic comparison, trace, public disposition and claim boundary |
| gateRunPurpose | confirm the already-inspected bounded correction tooling before operator elevation and preserve the pending Local-review boundary; gates are evidence, not first discovery |
| claimBoundary | static and hermetic checks do not establish the real source or prove the elevated repair ran |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| writer correction | `scripts/acel_g1_party_b_group3_observation_writer.ps1` | 56/56 hermetic suite | PASS |
| one-time repair | `scripts/acel_g1_t3c_c2_local_read_acl_repair.ps1` | syntax and fail-closed elevation check | PASS_PENDING_ELEVATED_RUN |
| operator launcher | `scripts/run_cvf_g1_t3c_c2_local_verification_as_admin.cmd` | one UAC-mediated invocation | READY |
| real source | `governance/sources/registry_observation_log/LOG.jsonl` | independent checker and receipt | PENDING |
| successor tranche | T3D/T3E | none | CLOSED |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance workspace |
| Session or invocation | ACEL G1 T3C-C2 post-ceremony Local review, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | contract/source reads, access probes, apply_patch, PowerShell and Python hermetic checks, Git |
| Target paths | writer, one-time repair, launcher and this decision; real log content remains unchanged |
| Allowed scope source | standing Local reviewer/fixer authority and operator request to continue G1-G6 |
| Before status evidence | HEAD `2c492efffe`; real log present but unreadable to Local; thirteen parked paths preserved |
| After status evidence | corrected writer and repair transaction prepared; real log still pending elevated repair and Local verification |
| Diff evidence | exact four-path correction manifest plus untracked real log; parked thirteen excluded |
| Approval boundary | bounded reviewer repair and one operator UAC checkpoint only |
| Claim boundary | no second observation, establishment, admission, T3E, provider/live, public or deployment effect |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3c-c2-local-readability-repair-20260922` |
| Expected manifest | this decision; writer; repair script; launcher |
| Actual changed set | pending final reconciliation before commit |
| Manifest delta | pending final reconciliation before commit |
| Deletion or rename disposition | none |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: replace only the Group 3 checker test's
pre-establishment-only real-log-absence assertion with a lifecycle-safe,
read-only byte-invariance assertion after legitimate source creation.

Protected path authorized for mutation:

- `governance/compat/test_check_acel_g1_registry_observation_log.py`.

Protected paths present only because they are pre-existing parked untracked
worktree evidence and therefore listed for changed-set accounting:

- `governance/compat/check_task_class_calibration_owner_evidence.py`;
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`.

Operator authorization: standing Local reviewer/fixer authority within the
operator-directed continuation of ACEL G1-G6. Rollback boundary: revert only
the Group 3 lifecycle-test correction and its paired completion evidence if
rejected; preserve the real source and every parked path.

The two task-class paths are explicitly excluded from mutation, staging and
commitment by this authorization. No checker-semantic relaxation, hook wiring,
second observation, Group 4/T3E implementation, provider/live call, public
sync, deployment or production action is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local-source correction; no public-sync authorization.

## Claim Boundary

This decision authorizes and documents only a byte-preserving DACL correction
and its Local verification checkpoint. It does not establish Group 3, append a
second observation, open T3D/T3E, bind a consumer, promote a key, admit a
candidate, call a provider, export publicly, deploy, or claim production
readiness.
