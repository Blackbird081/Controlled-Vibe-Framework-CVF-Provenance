# CVF ACEL G1 T3C-C2 Group 3 Source Local Verification

Memory class: governed-audit

docType: audit

Status: SOURCE_CREATED_LOCAL_VERIFIED

Date: 2026-09-22

Batch ID: ACEL-G1-T3C-C2-GROUP3-SOURCE-LOCAL-VERIFICATION

Review base head: `21904183d`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record Local's independent acceptance of the one-time Party B Group 3 genesis
observation after direct content, cryptographic, identity and Windows security
verification. This closes T3C-C2 only; it does not open Group 4 or consumer
wiring.

## Target / Source

| Source | Verified role |
|---|---|
| `governance/sources/registry_observation_log/LOG.jsonl` | real Group 3 immutable observation log |
| `governance/sources/verifier_key_registry/REGISTRY.json` | exact Group 1 snapshot bytes bound by the observation |
| `governance/compat/check_acel_g1_registry_observation_log.py` | independent structural/hash/chain checker |
| `docs/reviews/evidence/cvf-acel-g1-t3c-c2-local-verification-2026-09-22.json` | detached Local verification receipt |
| `scripts/acel_g1_party_b_group3_observation_writer.ps1` | corrected future writer security postcondition |

## Scope / Methodology

Local read the real file directly from the ordinary non-elevated reviewer
session, executed the independent Python checker in validate/count/lookup
modes, and separately recomputed the cryptographic bindings using an
independently authored Python path. The separate path decoded unpadded
base64url without JSON round-tripping, compared decoded bytes with the exact
Group 1 registry bytes, recomputed SHA-256 over those bytes, reconstructed the
closed canonical entry preimage, serialized it with sorted compact UTF-8 JSON,
and recomputed the entry digest.

Local separately read back owner, protection state and every explicit ACE as a
complete semantic tuple. Party B account posture was re-read from Windows.
The writer's hermetic suite was rerun after correcting its Windows rights
normalization oracle.

## Findings / Position

| Check | Observed evidence | Disposition |
|---|---|---|
| source shape | exactly one nonblank JSONL record | PASS |
| snapshot identity | `snap-9037220e94434acaa4909cb1cba2e2fc-eec908be7c0243d4`; count `1`; lookup returned the sole record | PASS |
| registry | `verifier_key_registry`, version `1` | PASS |
| observer separation | Party B SID `S-1-5-21-1644666849-912006174-747199667-1009`, distinct from Party A writer SID ending `-1006` | PASS |
| snapshot byte binding | decoded `snapshot_content` byte-identical to `REGISTRY.json` | PASS |
| snapshot digest | `87594cdcf8a1e0c3c4b439434aeda39444ff54a432674d97403f1980c995d883` | PASS |
| genesis chain | `priorEntryHashHex` is JSON null | PASS |
| entry digest | `a97f1066cc5fe33409eff6539c2ca68dcf72f794209c8de5df93a7f81dc6e1c3` | PASS |
| whole-file digest | `e1d9dfd747df33eaf1b85664c22e19a49edcb521fbbc07a0c53f6c13636d8629` | PASS |
| independent checker | validation PASS; count `1`; lookup exact | PASS |
| owner | exact Party B SID ending `-1009` | PASS |
| DACL | protected; Party B/SYSTEM/Administrators FullControl; exact Local SID ending `-1001` Read plus Windows-normalized Synchronize; no deny, inherited or extra ACE | PASS |
| Party B posture | enabled, password required, expiry 2026-10-21, distinct standard principal | PASS |
| writer suite | 56/56 | PASS |
| source bytes through final Local receipt | before/after SHA-256 equal | PASS |

## Security Normalization Correction

`FileSystemAccessRule(Read, Allow)` is represented by Windows as numeric rights
`1179785` (`Read, Synchronize`), not the unnormalized enum value `131209`.
The first repair probe rejected this legitimate representation. The corrected
writer and repair verifier derive the expected numeric rights from an actual
`FileSystemAccessRule` constructor and still compare the complete tuple.

The final receipt records `daclMutationPerformed: false`: by that final run the
four-ACE target state was already present. Earlier evidence establishes an
initial Local read failure and one or more elevated repair launches, but does
not independently identify which process transition first made the Local ACE
effective. Therefore this audit claims only the fully verified final state and
byte invariance, not a stronger transition-attribution claim.

## Risk / Corrective Action

The accepted Group 3 source is immutable and must not receive a second record
without a new governed authorization. Future writer invocations now require
the exact four-principal policy and use the normalized read-right tuple.

Group 4 issuer-registry/lookup-response establishment and T3E consumer wiring
remain separate, closed tranches. No key promotion or candidate evaluation is
authorized by this observation.

## Independent Probe Evidence

| Probe | Result |
|---|---|
| checker validation | `result: PASS`, `entryCount: 1` |
| checker count | `count: 1` for the expected snapshot ID |
| checker lookup | sole record returned with exact expected hashes |
| separate canonical recomputation | `independentRecompute: PASS` |
| direct Local read | 1388 bytes; whole-file SHA-256 `e1d9df...d8629` |
| ACL tuple readback | owner Party B; protected; exactly four expected allow ACEs |
| detached receipt | `LOCAL_VERIFICATION_PASS`; source bytes unchanged |

## Decision / Disposition

`SOURCE_CREATED_LOCAL_VERIFIED`.

ACEL G1 T3C-C2 is closed bounded. The Group 3 source is admitted as an
independently verified source dependency. `successorTrancheOpened` remains
`NO` in this artifact; successor selection requires separate continuity and
dependency review.

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| raw enum versus Windows-normalized ACE rights | REVIEWER_ORACLE_ERROR | GOVERNANCE_CONTROL_PLANE | LOCAL_FIX_AND_REUSABLE_LEARNING | security tuple verifiers must compare OS-normalized rights emitted by the actual rule constructor |
| durable source absence used as a permanent self-test oracle | TEST_LIFECYCLE_ERROR | GOVERNANCE_CONTROL_PLANE | LOCAL_FIX_COMPLETE | self-tests prove path isolation and non-mutation instead of assuming a governed source never exists |
| source contract reader omitted from original writer policy | IMPLEMENTATION_CONTRACT_GAP | GOVERNANCE_CONTROL_PLANE | LOCAL_FIX_COMPLETE_AND_PARKED_LEARNING | enumerate writer, reviewer and recovery principals before real-source authorization |

## Epistemic Process Block

### Expected Result / Prediction

One Party B genesis record should bind exact Group 1 bytes, validate through an
independent checker, remain readable by Local and expose no excess ACE.

### Evidence Comparison

All content, identity, chain, hash and final security checks match. The only
review contradiction was the probe's use of an unnormalized rights constant;
direct inspection showed the fourth ACE was the expected Local reader.

### Contradiction Or Gap Disposition

The rights-oracle contradiction was corrected and rerun. Transition attribution
is bounded explicitly; final state, content and byte invariance are proven.

### Claim Update

Group 3 advances from `OBSERVATION_APPENDED_PENDING_LOCAL_VERIFICATION` to
`SOURCE_CREATED_LOCAL_VERIFIED`. No downstream source or consumer claim moves.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_acel_g1_registry_observation_log.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | exact entry fields, canonical preimage, Group 3 result, learning fields, epistemic comparison, trace, public disposition and claim boundary |
| gateRunPurpose | confirm the independently inspected source and completion evidence; gates are confirmation evidence, not first discovery |
| claimBoundary | checker and local proofs establish only this Group 3 source, not Group 4, T3E or candidate admission |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Group 3 source | `governance/sources/registry_observation_log/LOG.jsonl` | independent checker PASS, count 1 | PASS |
| Local receipt | `docs/reviews/evidence/cvf-acel-g1-t3c-c2-local-verification-2026-09-22.json` | `LOCAL_VERIFICATION_PASS` | PASS |
| writer regression | `scripts/acel_g1_party_b_group3_observation_writer.ps1` | 56/56 | PASS |
| checker regression | `governance/compat/test_check_acel_g1_registry_observation_log.py` | 42/42 | PASS |
| Group 4 | separate future tranche | none | CLOSED |
| T3E consumer wiring | separate future tranche | none | CLOSED |
| session continuity | active handoff/state | separate sync commit | PENDING_SEPARATE_SYNC |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: replace the Group 3 checker test's
pre-establishment-only real-log-absence assertion with a lifecycle-safe,
read-only byte-invariance assertion that works both before and after legitimate
source creation.

Protected path:

- `governance/compat/test_check_acel_g1_registry_observation_log.py`.

Operator authorization: standing Local reviewer/fixer authority within the
operator-directed continuation of ACEL G1-G6, after the real T3C-C2 source made
the old absence oracle invalid. Rollback boundary: revert only this test and
the paired lifecycle finding if rejected; preserve the real source, receipt,
writer correction and all parked paths.

Not authorized: no checker semantic relaxation, hook wiring, second
observation, Group 4/T3E implementation, provider/live call, public sync,
deployment or production action.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | ACEL G1 T3C-C2 Group 3 source verification, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | direct byte reads, independent Python checker, separate hash recomputation, Windows ACL/account readback, PowerShell self-test, apply_patch and Git |
| Target paths | Group 3 log, detached receipt, corrected writer/repair script and this audit |
| Allowed scope source | committed T3C-C2 execution decision plus standing Local reviewer/closer authority |
| Before status evidence | Group 3 result pending Local verification; thirteen parked paths preserved |
| After status evidence | exact one-record source, receipt and Local audit ready for material commit |
| Diff evidence | exact source/receipt/audit, rights-normalization correction and lifecycle-safe checker test; parked thirteen excluded |
| Approval boundary | close T3C-C2 only and route next selection separately |
| Claim boundary | no second observation, Group 4, T3E, promotion, admission, provider/live, public or deployment effect |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3c-c2-group3-source-local-verification-20260922` |
| Expected manifest | source log; Local receipt; this audit; repaired reviewer decision; writer and repair-script normalization correction; checker lifecycle test |
| Actual changed set | `governance/sources/registry_observation_log/LOG.jsonl`; `docs/reviews/evidence/cvf-acel-g1-t3c-c2-local-verification-2026-09-22.json`; this audit; `docs/reviews/CVF_ACEL_G1_T3C_C2_LOCAL_READABILITY_REPAIR_DECISION_2026-09-22.md`; `scripts/acel_g1_party_b_group3_observation_writer.ps1`; `scripts/acel_g1_t3c_c2_local_read_acl_repair.ps1`; `governance/compat/test_check_acel_g1_registry_observation_log.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | failure diagnostic removed after successful final verification; no governed source deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local source and verification evidence; no public-sync authority.

## Claim Boundary

This audit establishes one Local-verified Group 3 genesis observation only. It
does not authorize another append, establish Group 4, wire T3E consumers,
promote a key, evaluate or admit a candidate, call a provider, export publicly,
deploy, or claim production readiness.
