# CVF ACEL G1 T3D-C1-R2 Reservation-Compatible Tooling Worker Return

Memory class: governed-worker-return

docType: worker-return

Status: COMPLETE_PENDING_REVIEW

Date: 2026-09-23

Batch ID: ACEL-G1-T3D-C1-R2-RESERVATION-COMPATIBLE-TOOLING-CORRECTION

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md`

executionBaseHead: `8537cdedb002323ee767313835811e4262ab2021`

Commit mode: `WORKER_MUST_NOT_COMMIT` (respected; no commit made)

Decision owner: Local orchestrator/reviewer

independentProbeDisposition: PENDING_REVIEWER_EXECUTION

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md`

Correction round: 3 (addresses Local finding RV12; RV01-RV11 are resolved and
unchanged in this round -- the writers, the disposable harness and their
self-tests were not touched).

## Purpose

Correct a single recovery-integrity defect, RV12, found by a fourteenth Local
probe case after RV06-RV11 closed: `Invoke-Recovery` whitelisted a sibling
file by trusting an unvalidated `tempName` from a different, malformed
transaction row. This round's write scope is narrowed to
`scripts/acel_g1_group4_admin_recovery.ps1` and this return. RV01 (packet
repair) remains Local-owned and untouched; the writers and disposable harness
are unchanged from round 2. No new tranche is opened.

## Target / Source

| Source | Disposition |
|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md` | dispatch authority; read, not modified by the worker |
| `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | controlling reservation, Local preflight/postflight and recovery contract |
| `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_LOCAL_REVIEW_2026-09-23.md` | finding RV12 (RV01-RV11 resolved); read, not modified |
| `docs/reviews/evidence/cvf-acel-g1-t3d-c1-r2-local-probe-2026-09-23.ps1` | Local probe (14 cases, including `recovery-malformed-other-binding-does-not-whitelist`); executed unmodified from the worker seat as self-verification only |

## Scope / Methodology

Role: operator-selected distinct shared-workspace `INTERNAL_AGENT` worker
(Claude). Local (Codex) remains reviewer, probe executor and closer. Only the
two round-3 manifest paths were edited:
`scripts/acel_g1_group4_admin_recovery.ps1` and this return. The two writer
scripts and the disposable harness were not opened or modified this round.
All execution used current-token TestPolicy fixtures in `%TEMP%` disposable
roots; no Party B/C execution, credentials, elevation, provider call,
subagent, real Group 4 source access or commit.

## Findings / Position

### Design summary

1. One ledger contract (`cvf.g4.recoveryLedger.v2`) for both writers: every
   row carries the exact 19-field binding -- transaction ID, contiguous
   sequence, phase, UTC millisecond timestamp, writer SID, writer process ID
   and process start time, target kind/name/path, parent path and parent file
   identity, complete target prestate (file identity, length, SHA-256, link
   count, attributes, owner, protection, complete ordered-ACE security
   digest), temp name, temp role, expected temp SHA-256, expected temp
   security digest, and temp file identity (null until flushed).
2. Writers generate the unique temp name, append a complete TEMP_PLANNED row
   durably, and only then create the temp. The ledger append refuses a
   planning row for a name that already exists. The temp name is held in an
   immutable per-transaction binding and never cleared, so PRE_MOVE,
   PUBLISHED, RELEASED and DISCARDED rows carry the same non-empty name. This
   applies to the registry candidate, the response candidate, every append
   capture, and both writers' rollback temps.
3. Recovery validates the exact schema and field semantics, applies a strict
   per-temp phase grammar, requires independently checkable termination of the
   exact recorded writer process instance, then -- holding the writer's own
   transaction guard -- compares residue identity, content hash, link count and
   complete security digest, and the target against its exact prestate (or a
   bound published poststate). It captures target, other reservation, parent
   identity/security and parent inventory before and after removal and
   appends terminal RECOVERED rows.
4. The Local boundary lives in the existing disposable harness: preflight
   holds a parent-scoped Local guard, records both reservations and the parent
   in a Local-only record, hashes that record into an authorization reference,
   and issues a per-writer view containing only the writer's own-target
   fields. Writers accept a view only if its exact field set, transaction,
   target, parent identity, held guard and own-target state match. Postflight
   verifies parent, the exact two-name inventory, other-target invariance and
   own-target poststate, and records PASS or FAIL.
5. The protected parent is modeled as the closed set `REGISTRY.json`,
   `LOOKUP_RESPONSES.jsonl`, plus only the current transaction's bound temps.
   A writer checks only the name, entry type and reparse state of the other
   reservation; it never reads that file's content or security.

### Withdrawn claim

The round-1 statement `REVIEWED_NO_DEFECT_FOUND` for the empty PUBLISHED temp
binding is withdrawn. Local was correct: both writers cleared `$temp` before
building the PUBLISHED row. That is fixed and covered by RV08 regressions.

### RV12 root cause and fix

`Invoke-Recovery` computed `$otherBound` by reading the raw `tempName` field
off every ledger row whose `transactionId` differed from the primary
transaction, with no validation of that row or its transaction. Local's probe
added a two-field row (`transactionId`, `tempName` only) naming an unrelated
file `unexpected.bin`; recovery treated that name as known residue, removed
the primary transaction's legitimately bound temp, and reported
`RECOVERY_RESIDUE_REMOVED_LEDGER_VERIFIED` while the actually-unknown sibling
remained untouched and unreported.

The fix collects the distinct set of other transaction IDs present in the
provided ledgers, then calls the existing `Get-TransactionBinding` -- the same
function that validates the primary transaction's exact v2 schema, identity,
hash, phase-sequence and ambiguity rules -- once per other transaction ID.
`Get-TransactionBinding` already throws (`Stop-Recovery`) on any malformed,
incomplete, contradictory or ambiguous row, and that throw is not caught here,
so an invalid other-transaction row now fails the entire recovery call closed
before the transaction guard is even acquired -- no file is read, matched or
removed, and no ledger row is appended. Only temp names belonging to a
transaction that validates cleanly, and whose binding's last phase is
non-terminal (`TEMP_PLANNED`, `TEMP_FLUSHED` or `PRE_MOVE`), are recognized as
known residue for the inventory check.

## RV06-RV11 Matrix (round 2, unchanged this round)

| Finding | Implementation | Test / assertion | Result | Limitation |
|---|---|---|---|---|
| RV06 unbound ledger | Recovery `Get-TransactionBinding`: exact 19-field row set and 8-field prestate set; schema literal; targetKind/targetName/path-leaf/parent agreement; UTC ms timestamp format, not future, non-decreasing; contiguous sequence; constant writer/target/prestate binding; per-temp role/hash/digest constancy; phase grammar; temp-name pattern by kind and role; `Assert-WriterTerminated` (PID plus exact start time) before cleanup | Recovery self-test RECOVERY-03 wrong schema, -04 targetName mismatch, -05 timestamp, -06 phase order and sequence gap, -07 alive writer, -13 missing/extra field, -18 complete-but-unbound; harness PROBE-RV06-ALIVE-WRITER-PRESERVED and PROBE-RV06-RECOVERED-AFTER-TERMINATION against a real crashed writer; Local probe `recovery-complete-but-unbound`, `recovery-unverified-binding`, `recovery-traversal-binding`, `recovery-missing-binding-control` | PASS | Termination evidence is process-table based. If the start time of a live process cannot be read, recovery refuses (fail closed). The ledger file is not signed; a principal able to write the ledger path could forge a fully consistent row, so the real ledger directory ACL remains an operator-checkpoint dependency. |
| RV07 precreation binding | `Register-LedgerTemp` appends TEMP_PLANNED before `CreateNew`; `Add-LedgerRow` refuses TEMP_PLANNED if the file exists; Party B `Write-HardenedTemp` now binds every capture/candidate before creation; Party B and Party C rollback temps are also bound | T3D-C1-C-07-PLAN-BEFORE-CREATE, T3D-C1-C-07-BINDING-AFTER-CREATE, T3D-C1-B-01-PLAN-BEFORE-CREATE, T3D-C1-B-01-BINDING-AFTER-CREATE, T3D-C1-B-01-CAPTURE-BOUND, T3D-C1-B-01-CAPTURE-ORDER, T3D-C1-C-POST-REPLACE-LEDGER | PASS | A crash between TEMP_PLANNED and TEMP_FLUSHED can leave a partially written or not-yet-hardened temp. Its hash/digest will not match, so recovery preserves it and the tooling cannot clear it; C0-R1 allows this fail-closed outcome but it needs a separately reviewed remediation. |
| RV08 empty PUBLISHED binding | Immutable `$tempName` binding per transaction; PUBLISHED written right after the atomic move with the same binding | T3D-C1-C-06-LEDGER-PHASES/-SEQUENCE/-TEMPNAME/-SCHEMA/-HASH/-FILEID/-WRITER; T3D-C1-B-01-LEDGER-PHASES/-SEQUENCE/-TEMPNAME/-SCHEMA/-FILEID; T3D-C1-C-07-EMPTY-TEMPNAME, T3D-C1-B-01-EMPTY-TEMPNAME; recovery RECOVERY-11 changed/empty temp name | PASS | none known |
| RV09 exact recovery state | Recovery captures full file state records (identity, bytes hash, length, link count, attributes, owner, protection, complete ACE digest) for residue, target and other reservation plus parent identity/security and inventory; all revalidation after acquiring the transaction guard; exact pre/post invariance; RECOVERED rows | RECOVERY-01 (target exact, other exact, inventory, recorded, idempotent), -08 content mismatch, -09 complete-ACE mismatch with same owner/protection, -10 target drift, -15 unknown sibling, -16 hardlink, -17 same-content different identity; harness PROBE-RV09-TARGET-EXACT, -LEDGER-RECOVERED, -CLAIMABLE-AFTER-RECOVERY | PASS | Recovery reads the other reservation because it runs as the Local/Administrator actor; writers never do. Cross-ledger residue (both writers crashed together) needs both ledgers passed to recovery. |
| RV10 Local boundary | `acel_g1_group4_disposable_acl_probe.ps1` rewritten as the Local disposable harness: `Invoke-LocalPreflight`, per-writer authorization view, `Invoke-LocalPostflight`; writers gained `Assert-WriterAuthorization` and real modes now require `-AuthorizationPath` and `-TransactionId` | PROBE-RV10-C-VIEW-OWN-ONLY, -C-REF-BINDS-RECORD, -C-POSTFLIGHT, -C-LEDGER-BOUND, -B-VIEW-OWN-ONLY, -B-POSTFLIGHT, NEG-WRONG-TRANSACTION, NEG-DISCLOSURE, NEG-GUARD-ABSENT, NEG-OWN-DRIFT, POSTFLIGHT-OTHER-DRIFT | PASS | (a) Local preflight/postflight exist only for disposable roots; the real-parent Local entrypoint is an operator checkpoint outside this tranche. (b) The writer verifies that the Local parent guard object exists and has the expected name, not that Local owns it; named kernel objects are not an authority boundary between processes of one token. (c) Party B append (T3E) does not take a Local authorization view. |
| RV11 shared parent | `Assert-ParentSiblingSet` in both writers: exactly the two reservation names (regular, non-reparse) plus current bound temps; re-checked before the move | T3D-C1-C-07-SHARED-PARENT, -THIRD-SIBLING, -PEER-NOT-FILE, -SIBLING; T3D-C1-B-01-SHARED-PARENT, -THIRD-SIBLING, T3D-C1-B-SIBLING; harness PROBE-RV11-PREFLIGHT-THIRD-SIBLING, -MISSING-PEER; Local probe `c-shared-parent-positive`, `b-shared-parent-positive`, `c-unknown-sibling`, `b-unknown-sibling` | PASS | A writer does not require the other reservation to be present (the Local probe `c-positive`/`b-positive` cases require single-reservation success); presence of both is enforced by Local preflight. The Party B append path keeps its pattern-based residue check because test fixtures co-locate observation and request files. |

## RV12 Matrix

| Finding | Implementation | Test / assertion | Result | Limitation |
|---|---|---|---|---|
| RV12 unvalidated other-transaction whitelist | `Invoke-Recovery` now calls `Get-TransactionBinding` (full v2 schema/identity/hash/phase-sequence/ambiguity validation) once per distinct other transaction ID found in the ledgers, instead of trusting raw `tempName` fields; an invalid other-transaction row throws before the guard is acquired; only non-terminal (`TEMP_PLANNED`/`TEMP_FLUSHED`/`PRE_MOVE`) temps of a cleanly validated other transaction are recognized as known residue | Recovery self-test RECOVERY-19-MALFORMED-OTHER-BINDING (asserts: recovery throws `RECOVERY_LEDGER_ENTRY_INCOMPLETE`; primary residue preserved; unknown sibling preserved; target/other-reservation/parent unchanged; no RECOVERED row appended); Local probe `recovery-malformed-other-binding-does-not-whitelist` | PASS | The fix validates every distinct other transaction ID present in the supplied ledger paths, which in this tooling's real deployment is exactly the registry and response ledgers Local passes to recovery. If a caller omits a ledger that contains a legitimate other-transaction's rows, that transaction is invisible to this check entirely (its rows are simply absent), which is a caller-scope concern, not a validation-bypass; it is noted for Local's awareness. |

### Counts

| Suite | Assertions | Result |
|---|---|---|
| Party C writer self-test | 74 (unchanged this round; not rerun per dispatch scope) | PASS (round 2) |
| Party B writer self-test | 80 (unchanged this round; not rerun per dispatch scope) | PASS (round 2) |
| Admin recovery self-test | 28 (27 round-2 assertions + 1 new RV12 regression) | PASS |
| Local disposable harness | 21 (unchanged this round; not rerun per dispatch scope) | PASS (round 2) |
| Local probe (unmodified, worker-seat run) | 14 cases | `failed: 0` |

Per the correction dispatch, only the admin recovery self-test and the
unmodified Local probe were rerun this round; the writer and harness self-test
counts above are carried from the round-2 return and were not re-executed
since neither the writers nor the harness were touched. The admin recovery
self-test was run three times consecutively (28/28 each run) and the Local
probe twice (14/14, `failed: 0` each run).

## Risk / Corrective Action

Open items from round 2 are unchanged and are listed in the RV06-RV11 matrix
Limitation column above; they are not claimed closed by this round. RV12
introduces one new limitation, noted in the RV12 matrix row above (ledger-set
scoping is a caller concern, not a bypass in the validation logic itself).

## Decision / Disposition

`COMPLETE_PENDING_REVIEW`. The admin recovery self-test (28/28, three
consecutive runs), the unmodified Local probe (14/14 cases, `failed: 0`, two
consecutive runs), the required worker-return gate and `git diff --check` all
pass on the final changed set. `independentProbeDisposition` remains
`PENDING_REVIEWER_EXECUTION`. The return's `READY_WITH_EXECUTABLE_PROOF` SCEC
disposition records that each resolved blocker is bound to executable
evidence; acceptance remains a Local decision.

## Claim Boundary

Hermetic, disposable-root, current-token evidence only. No claim about real
Party B/C effective rights, the real Group 4 source, T3E, admission,
provider, public-sync or deployment.

## Changed Files

```text
 M scripts/acel_g1_group4_admin_recovery.ps1
```

This round's write scope is exactly `scripts/acel_g1_group4_admin_recovery.ps1`
and this return; the writers and disposable harness carry their round-2
content, unchanged and not re-hashed here.

Final script SHA-256 (the return's own digest is reported in the hand-off
message, not here):

| Path | SHA-256 |
|---|---|
| scripts/acel_g1_group4_admin_recovery.ps1 (round 3) | ffb359ad078783f64802eb29582f363066c38b5b5d6ea69ff6d8f34ed955c480 |
| scripts/acel_g1_party_c_group4_registry_writer.ps1 (round 2, unchanged) | df596d1e1f57d02fbe65c369506a325038b344dd95201f930dd0edbe27781513 |
| scripts/acel_g1_party_b_group4_lookup_response_writer.ps1 (round 2, unchanged) | 49c8321b46cc1c0b409f29349d1d9145eadb360d035dcfa6faabe951c03c1678 |
| scripts/acel_g1_group4_disposable_acl_probe.ps1 (round 2, unchanged) | 15d92e5c6e14ad3e2af8b8d29fc759b233d64b90138ee7c58e6a6ce12953d0ed |
| docs/reviews/evidence/cvf-acel-g1-t3d-c1-r2-local-probe-2026-09-23.ps1 (Local-owned, updated to 14 cases) | 846429bc95fcb46a084c3cc3231fc35c85375b664316519a73c855811d7cb15a |
| docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_LOCAL_REVIEW_2026-09-23.md (Local-owned, RV12 added) | 5e109156f0cf62a869e327fe3c43929f62b91ad7b83ab378646070245b4e83bc |

Note: the Local probe hash above was captured before this correction was
rerun against it; the probe file itself is unmodified across the run, only
its result content changed (14/14 satisfied instead of 13/14).

## Command Evidence

```text
$ git rev-parse HEAD
8537cdedb002323ee767313835811e4262ab2021

$ pwsh -NoProfile -NonInteractive -File scripts/acel_g1_group4_admin_recovery.ps1 -SelfTest
{"result":"PASS","tests":28,"sourceMutation":false}                exit 0
(repeated twice more: identical PASS, tests=28)

$ pwsh -NoProfile -NonInteractive -File docs/reviews/evidence/cvf-acel-g1-t3d-c1-r2-local-probe-2026-09-23.ps1 -RepositoryRoot <repo-root>
failed=0 cases=14 satisfied=14                                     exit 0
(repeated once more: identical failed=0, cases=14)

$ git diff --check
exit 0 (only an LF/CRLF notice on the Local-owned work order)

$ python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md
[CVF hook] All reviewer-fast governance checks passed.
PASS: git diff whitespace check
COMPLIANT: worker-return fast gate passed                          exit 0
```

Timing note: an earlier gate run in this round, made before this return was
rewritten to round 3, failed only on `semantic convergence and escalation
control` because the return still bound the round-2 recovery-script hash.
That run is superseded; the command evidence above reflects the run made
after the last edit to this file.

## No-Commit Statement

`WORKER_MUST_NOT_COMMIT honored`. No commit was made. Staging is empty.

## git status --short

```text
 M docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_CORRECTION_2026-09-23.md
 M scripts/acel_g1_party_b_group4_lookup_response_writer.ps1
 M scripts/acel_g1_party_c_group4_registry_writer.ps1
?? docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_LOCAL_REVIEW_2026-09-23.md
?? docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_WORKER_RETURN_2026-09-23.md
?? docs/reviews/evidence/cvf-acel-g1-t3d-c1-r2-local-probe-2026-09-23.ps1
?? scripts/acel_g1_group4_admin_recovery.ps1
?? scripts/acel_g1_group4_disposable_acl_probe.ps1
```

The work order, Local review and Local probe are Local-owned and were not
edited by the worker.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

N/A with reason: bounded correction of four already-named script paths; no
corpus, inventory or unfamiliar-path rescan was performed or required.

## Corpus Completeness And Report Integrity

N/A with reason: no corpus scan, inventory claim or completeness report is in
scope.

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded five-path correction only; no complete-corpus claim was made.

## Return-Time Closeability Recheck

Rechecked at return time on execution HEAD
`8537cdedb002323ee767313835811e4262ab2021`: worker-owned focused tests and the
required worker-return gate pass on the exact five-path manifest. Reviewer
gates (independent probe, reviewer-fast, pre-commit, terminal review) remain
Local-owned. No committed range exists.

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: N/A

workerRedispatchAllowed: NO

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3D-C1-R2-RESERVATION-COMPATIBLE-TOOLING-CORRECTION
reviewRoundCount: 3
priorFindingSetDigest: 5e109156f0cf62a869e327fe3c43929f62b91ad7b83ab378646070245b4e83bc
dependencyAuditDisposition: COMPLETE_ALL_KNOWN_DEPENDENCIES
reworkFindingDisposition: RV12_ADDRESSED
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: TARGETED_NEGATIVE_TESTS_ADDED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: PENDING_LOCAL_REVIEW
rootCauseClusterId: acel-g1-t3d-c1-r2-reservation-boundary-defect-cluster-rv02-rv05
reworkGeneration: 3
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: scripts/acel_g1_group4_admin_recovery.ps1 sha256 ffb359ad078783f64802eb29582f363066c38b5b5d6ea69ff6d8f34ed955c480 (round-3 change); scripts/acel_g1_party_c_group4_registry_writer.ps1 sha256 df596d1e1f57d02fbe65c369506a325038b344dd95201f930dd0edbe27781513 (round-2, unchanged); scripts/acel_g1_party_b_group4_lookup_response_writer.ps1 sha256 49c8321b46cc1c0b409f29349d1d9145eadb360d035dcfa6faabe951c03c1678 (round-2, unchanged); scripts/acel_g1_group4_disposable_acl_probe.ps1 sha256 15d92e5c6e14ad3e2af8b8d29fc759b233d64b90138ee7c58e6a6ce12953d0ed (round-2, unchanged)
adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
internalAgentInvocationCount: 1
externalAgentInvocationCount: 0
providerCallCount: 0
tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no provider meter is surfaced to this INTERNAL_AGENT worker seat
terminalReadinessVerdict: READY_FOR_REVIEW

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
- frictionLevel: LOW
- frictionType: OTHER
- observedStep: the new RV12 regression's cleanup pass initially failed StrictMode because ConvertFrom-Json on the deliberately malformed two-field other-transaction row has no `phase` property; fixed by checking property presence before reading it when scanning the ledger for RECOVERED rows in the assertion, not in production code.
- preventiveControlCandidate: NONE

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `READY_WITH_EXECUTABLE_PROOF`; `EXECUTABLE_IMPLEMENTATION`; `sameClaimCorrections`; structured retro field names; `WORKER_MUST_NOT_COMMIT honored` |
| gateRunPurpose | confirmation of the final return shape after implementation; not discovery of semantic findings |
| claimBoundary | gate results only; no Windows actual-token or Party B/C claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | operator-selected distinct shared-workspace `INTERNAL_AGENT` worker (Claude) |
| Provider or surface | private CVF workspace, Windows local host |
| Session or invocation | ACEL-G1-T3D-C1-R2 correction round 3 (RV12), 2026-09-23 |
| Invocation ID | acel-g1-t3d-c1-r2-worker-correction-round3-20260923 |
| Working directory | repository root |
| Command or tool surface | file read/write, `pwsh` self-tests, Python governance gates, `git status`/`git diff --check`/`git rev-parse` (read-only) |
| Target paths | exact two-path round-3 manifest: `scripts/acel_g1_group4_admin_recovery.ps1` and this return |
| Allowed scope source | operator correction dispatch for RV12 naming these two paths only |
| Before status evidence | HEAD `8537cdedb002323ee767313835811e4262ab2021`; recovery script and this return at round-2 state |
| After status evidence | recovery script and this return corrected for RV12; writers and harness unchanged; real Group 4 source path still absent |
| Diff evidence | `git status --short` above; `git diff --name-status` shows `M` on `scripts/acel_g1_group4_admin_recovery.ps1` only among the two round-3 paths, no rename or delete |
| Expected manifest | the two paths named in the round-3 correction dispatch |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |
| Approval boundary | bounded worker correction; no commit, Party B/C execution or credential use |
| Claim boundary | hermetic disposable-root evidence; the worker-seat Local probe run is self-verification, not independent review |
| Agent type | `INTERNAL_AGENT` worker |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | round-3 correction of one script (RV12) plus this return |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: hermetic self-tests create no production receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: 28 admin-recovery self-test assertions (three runs); unmodified Local probe 14/14 (two runs) |
| invocationBoundary | disposable `%TEMP%\cvf-g4-recovery-*` roots only this round |
| interceptionBoundary | no IDE, shell, Git, filesystem or provider interception claim |
| claimLanguage | corrected tooling with executable evidence pending Local review |
| forbiddenExpansion | credentials, alternate principal, real source, Group 4 establishment, T3E, admission, provider/live/public/deploy -- none exercised |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_LOCAL_REVIEW_2026-09-23.md` |
| Chain map route | N/A with reason: internal correction dispatched from Local's review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 4 contract via C0-R1 and this work order |
| Disposition | local first-party correction only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3d-c1-r2-reservation-tooling-correction-round3","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":["RV12_UNVALIDATED_OTHER_TRANSACTION_WHITELIST","ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN","REAL_PARENT_LOCAL_PREFLIGHT_OPERATOR_CHECKPOINT","PARENT_GUARD_PRESENCE_NOT_OWNERSHIP","LEDGER_DIRECTORY_ACL_OPERATOR_CHECKPOINT"],"resolved":["RV12_UNVALIDATED_OTHER_TRANSACTION_WHITELIST"],"retained":["ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN","REAL_PARENT_LOCAL_PREFLIGHT_OPERATOR_CHECKPOINT","PARENT_GUARD_PRESENCE_NOT_OWNERSHIP","LEDGER_DIRECTORY_ACL_OPERATOR_CHECKPOINT"],"new":["LEDGER_SET_SCOPING_IS_CALLER_RESPONSIBILITY"],"reopened":[],"current":["ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN","REAL_PARENT_LOCAL_PREFLIGHT_OPERATOR_CHECKPOINT","PARENT_GUARD_PRESENCE_NOT_OWNERSHIP","LEDGER_DIRECTORY_ACL_OPERATOR_CHECKPOINT","LEDGER_SET_SCOPING_IS_CALLER_RESPONSIBILITY"]},"resolutionEvidence":{"RV12_UNVALIDATED_OTHER_TRANSACTION_WHITELIST":{"evidenceClass":"EXECUTABLE_PROOF","evidencePath":"scripts/acel_g1_group4_admin_recovery.ps1","sha256":"ffb359ad078783f64802eb29582f363066c38b5b5d6ea69ff6d8f34ed955c480","locator":"RECOVERY-19-MALFORMED-OTHER-BINDING","claimId":"C1R2-RV12-CROSS-TRANSACTION-VALIDATION"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":3,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"C1R2-RV12-CROSS-TRANSACTION-VALIDATION","claimClass":"SCHEMA_COMPATIBILITY","proofClass":"EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST","evidenceRef":"scripts/acel_g1_group4_admin_recovery.ps1"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Epistemic Process Block

### Expected Result / Prediction

Before rerunning Local's probe: the fourteenth case,
`recovery-malformed-other-binding-does-not-whitelist`, would pass (recovery
throws instead of removing valid residue and whitelisting the unknown
sibling), and the thirteen cases that passed in round 2 would still pass, for
14 of 14.

### Evidence Comparison

The unmodified probe returned `failed=0`, 14 cases, 14 satisfied, matching the
prediction exactly. `recovery-malformed-other-binding-does-not-whitelist` now
throws `RECOVERY_LEDGER_ENTRY_INCOMPLETE` (the malformed other-transaction row
fails `Get-TransactionBinding`'s exact-field-set check) with both the primary
residue and the unknown sibling preserved. The thirteen round-2 cases produced
identical results to their round-2 run. The new admin recovery self-test
regression (RECOVERY-19-MALFORMED-OTHER-BINDING) was run three times
consecutively with identical results (28/28 each time); the Local probe was
run twice consecutively with identical results (14/14 each time).

### Contradiction Or Gap Disposition

No contradiction remains between the recovery self-test and the Local probe.
RV12's fix introduces one new limitation (ledger-set scoping is the caller's
responsibility, not a gap in the validation logic itself), recorded as a new
SCEC blocker and not claimed resolved. All round-2 limitations (RV06-RV11
matrix) remain open exactly as stated in round 2; this round did not touch the
writers or harness and makes no new claim about them.

### Claim Update

This return claims that RV12 is corrected with executable evidence: an
unvalidated other-transaction row can no longer cause recovery to whitelist
an unrelated sibling or remove valid residue while reporting success. It does
not claim anything new about RV01-RV11 (unchanged from round 2) or about real
Party B/C effective rights.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| RV06 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Corrected against C0-R1 recovery requirements |
| RV07 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Corrected against R2-05 precreation binding |
| RV08 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Corrected; earlier no-defect claim withdrawn |
| RV09 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Corrected against R2-05/R2-06 exact-state requirement |
| RV10 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Implemented within the existing harness path |
| RV11 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Corrected against the C0-R1 two-name parent |
| RV12 | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | Cross-transaction ledger rows now revalidated through the same schema/identity/hash/phase-sequence contract before they can whitelist inventory; added as a permanent regression (RECOVERY-19-MALFORMED-OTHER-BINDING) and as the Local probe's 14th case |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: bounded local correction; decision owner:
Local reviewer. No external research or provider input was used.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local Windows tooling correction.
