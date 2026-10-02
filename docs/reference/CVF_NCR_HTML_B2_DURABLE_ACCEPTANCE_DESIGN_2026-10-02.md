# CVF NCR HTML B2 Durable Acceptance Design

Memory class: POINTER_RECORD

Status: PROPOSAL_NOT_IMPLEMENTED

docType: reference

Date: 2026-10-02

## Purpose

Specify, as one coherent design for Local review, how an authenticated operator could durably accept one exact immutable version of the HTML review packet, under the selected DESIGN_DIRECTION_ONLY profile: a local single-host single-writer SQLite artifact-store candidate, separate from the governance-event ledger, with commit then readback verification and read-only classification of unknown outcomes. This document adds the selected authority and profile delta over B2a Part 2. It builds nothing: every schema, interface, path and SQL shape below is PROPOSAL_NOT_IMPLEMENTED, and every behavioral case in the paired evidence file is NOT_EXECUTED_DESIGN_ONLY.

## Scope / Applies To

Applies to the HTML export panel and route in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` as consumers, and to the identity helper `src/lib/html-artifact-acceptance-candidate.ts`. Canonical exports, Preview, Print and the accepted B2b-B2f transport evidence are unchanged and are consumed within their own limits. Source locators were read at the selected regions listed in the paired evidence JSON with SHA-256 values at executionBaseHead `17ae5b9586ee1fdd0fe6a73d0f37b4ab4419f8a2`. No database, server, browser, provider or transaction was run, and no real account, data or ledger was read.

## Selected-Profile Delta Over B2a Part 2

B2a Part 2 gave a five-step write protocol, an unknown-outcome rule and an open-decision list. It left the actor, the store owner, the writer model, the recovery observation and the lifecycle unspecified. This design adds the following, each traced to a section below.

| Delta | B2a Part 2 position | This design | Section |
|---|---|---|---|
| Actor binding | actor undecided | server-established actor, role and scope bound to operation, version and bytes; client role and receipt ALLOW never grant | 2 |
| Provenance of bytes | actor reviewed exact bytes, no mechanism | export attestation proves the bytes came from this server for this actor | 2 |
| Owner | separate store, owner undecided | new dedicated store adapted from named patterns; four existing owners rejected as acceptance authority | 1, 4 |
| Writer model | one writer process | single-writer discipline plus a fencing epoch checked inside every transaction | 4 |
| Commit shape | one transaction | attempt record then decision transaction, so an in-doubt operation leaves positive evidence | 5 |
| Durability | commit before ack | synchronous FULL required at open, unlike the existing generic adapter | 1, 4 |
| Recovery observation | look up identity read-only | classification on a scratch byte copy, never opening the live store for write | 5 |
| Absence | absent row means not accepted | absence is definitive only with positive evidence; a missing row alone is UNKNOWN | 5 |
| Lifecycle | append-only correction | historical versus effective acceptance, revocation, expiry, tombstone, restore handling | 6 |

## 1. Owner And Overlap

Five candidate owners were compared on the facts that matter for acceptance: who consumes it, what authority it carries, how long its state lives, what read and write actually do, and what identity, transaction and recovery capability it has. Locators are at executionBaseHead.

| Owner | Consumer and authority | Lifetime | Actual read and write semantics | Reusable part | Missing delta |
|---|---|---|---|---|---|
| B2a/B2b identity helper, `html-artifact-acceptance-candidate.ts` | no caller; pure helper; state is the constant `DRAFT_UNACCEPTED` (line 22) | in memory | `computeHtmlBytesIdentity` hashes exact UTF-8 bytes and refuses lone surrogates (lines 76-96); `verifyHtmlArtifactCandidate` rejects any state other than `DRAFT_UNACCEPTED` (line 169) | identity function, algorithm label `sha256-utf8-html-bytes/v1` (line 20), length-before-hash check | no actor, decision, workspace, operation, persistence; the candidate type cannot represent acceptance, so acceptance must be a separate record and never a mutation of the candidate |
| Web generic SQLite adapters, `storage-adapter.ts` | generic CVF evidence and snapshot stores; no acceptance authority | file-lifetime | `openSQLiteDatabase` creates the directory and database on any open and sets `synchronous = NORMAL` (lines 241-248); `SQLiteKeyValueAdapter.read` calls `init` first, which runs `CREATE TABLE IF NOT EXISTS` (lines 345-355, 368-370); `write` is an upsert, `ON CONFLICT(id) DO UPDATE` (lines 357-365); key is `id` only and the path is derived from a caller directory (lines 341-343) | the `better-sqlite3` dependency already in `package.json` (^12.6.2) and its loader pattern (lines 236-239) | read creates storage, so a wrong or missing directory returns null and manufactures a false absence; write overwrites; NORMAL synchronous in WAL can lose the latest committed transaction on power loss; no schema check, no actor, no workspace, no immutability |
| v3 `ArtifactLedger`, `artifact.ledger.ts` | v3 staging and ledger tests; no Web consumer; ACCEPTED status comes from staging | process memory (lines 44-50) | `commit` returns the existing entry when `contentHash` already exists, regardless of artifact id or commit (lines 66-70); entry holds hash, version and previous hash but no bytes, no actor, no workspace (lines 21-38); the header says duplicates throw while the code returns the existing entry | append-only lineage idea: version number and previous hash (lines 32-37) | not durable; content-hash dedup erases actor, workspace and version distinctions, which is the exact defect this design must avoid; no bytes |
| Governance-event SQLite ledger, `sqlite_ledger.py` | Q001 governance event candidate; records events, not artifact bytes | file-lifetime | table `blocks` holds request id, block JSON and block hash (line 222); `append_event` uses `BEGIN IMMEDIATE`, returns the existing block for an identical event and raises for a conflicting event with the same request id (lines 306-317); `synchronous=FULL` (line 236); strict schema check (lines 243-264); constructor creates directory and table (lines 214-223); every connection sets `journal_mode=WAL` (line 235), so its read path is not write-free either | patterns, not code: unique operation id, `BEGIN IMMEDIATE`, FULL synchronous, same-id conflict rule, strict schema check, and `classify_target`, which classifies a target on a scratch copy and never grants retry or authority (lines 119-162) | not a byte store, different runtime (Python) from the Web consumer, whole-chain read per append (line 310); the B2 audit already forbids retrofitting it as an HTML byte store |
| Route and session, `export/route.ts`, `route-governance-proof.ts`, `middleware-auth.ts` | export route authenticates then returns transient HTML; `DRAFT_UNACCEPTED` or `RECEIPT_ALLOW_REVIEW_REQUIRED` (route lines 358-364) | request | proof carries `authMode` of `session` or `service_token` and `actorId`; the session carries `userId`, `role`, `orgId`, `teamId`, `expiresAt` and optional impersonation (`middleware-auth.ts` lines 20-31) | the server-established session as the only admissible actor source | the route writes nothing; no accept route; no mapping from `orgId` and `teamId` to a workspace; no stable artifact key (see below) |

Findings the other documents did not record:

- The read-init gap and the upsert gap are both real in the generic adapter. Neither can be used to read back an acceptance: a read can create the store it is supposed to report on, and a write can replace accepted bytes.
- No existing source defines a stable artifact lineage key. `receiptAnchor` in the export route is the HTML section id of the rendered receipt (route lines 150-151, 200, 240), not an artifact key, and the title is user text. B2a carries only `attemptId` and `buildNumber`, both local to one panel session. This design therefore introduces `artifactKey` as a new, validated, workspace-scoped slug supplied by the accepting flow. It is not derived from `receiptAnchor` or the title.
- No existing source defines `workspace`. The session exposes `orgId` and `teamId`. The mapping is an open prerequisite (section 8); the design treats `workspaceId` as an opaque value the server derives from the session, never from the request body.

Disposition: ADAPT identity from the B2a helper, ADAPT patterns from the governance ledger, REJECT the generic adapter and the v3 ledger as acceptance authority, and PROPOSE the smallest dedicated store, a new TypeScript module in the Web library using the existing dependency. Consumer rationale: the Artifacts panel needs an explicit accept action and a later exact-byte retrieval that no existing owner provides. This is a bounded comparison of named sources, not a repository-wide absence claim.

## 2. Actor And Admission Contract

Only an authenticated operator, acting through a deliberate accept action that is separate from Build and separate from receiving a receipt, can accept. All admission facts are established by the server.

Proposed accept request (client supplies only claims to be checked): `operationId`, `artifactKey`, the exact `html` string the actor reviewed, the displayed `expectedIdentity` (algorithm, hash, length), the `exportAttestation` returned by the export route, and `basedOnDecisionId` or null. A `workspaceId`, role, actor or receipt decision in the body is ignored for authority.

Admission checks, evaluated in order, each with a named refusal and no store write:

| Check | Server-established input | Refusal |
|---|---|---|
| Actor present | session from `authorizeRouteGovernanceProof`; `authMode` must be `session` | ACTOR_MISSING; service-token callers get AUTH_MODE_NOT_SESSION, because a service token is not an accepting operator |
| Not impersonated | session carries no impersonation | IMPERSONATED_SESSION; acceptance under impersonation is refused, since the recorded actor would be ambiguous |
| Role permitted | role from session checked by a policy predicate `canAcceptHtmlArtifact(role, workspaceId)`, default deny | ROLE_NOT_PERMITTED; which roles may accept is an operator decision, not made here |
| Scope | `workspaceId` derived from the session, not the body; the attestation and artifact lineage must be in the same workspace | SCOPE_MISMATCH |
| Freshness | session `expiresAt` later than now at the first admission and again at the decision transaction; attestation not expired | SESSION_EXPIRED, ATTESTATION_EXPIRED |
| Provenance | attestation verifies and binds the identity, attempt id, build number, actor and workspace | ATTESTATION_INVALID |
| Exact bytes | the server encodes `html` once as UTF-8 with no normalization, computes the B2a identity, and compares with `expectedIdentity` and the attestation | BYTES_MISMATCH; this is how an edit after review is caught |
| Version freshness | `basedOnDecisionId` equals the latest effective decision of the lineage, checked inside the transaction | STALE_BASE |

The export attestation is a proposed addition to the export route response: a server-keyed MAC over the byte identity, attempt id, build number, actor id, workspace and issue time with a short expiry. It proves that these bytes were produced by this server for this actor and prevents accepting bytes the export never made. It is provenance evidence only. It cannot grant acceptance, and the MAC key custody is a real-effect prerequisite (section 8). Without it the accepting actor could submit bytes that no export produced; that alternative is rejected.

Receipt handling: `governanceReceipt` and `governanceState` values such as `RECEIPT_ALLOW_REVIEW_REQUIRED` are stored as opaque supporting evidence and never change admission. A receipt ALLOW without an explicit accept action produces no record.

Refusal leaves the draft: a refusal is returned to the caller, writes nothing to the acceptance store, and leaves the version `DRAFT_UNACCEPTED`. Refusals may be reported to the governance-event ledger as non-authoritative events; their absence never changes the store.

Subsequent changes: an edit after review produces new bytes and therefore a new identity, so the earlier acceptance cannot apply to it. A later change to the actor's role does not rewrite a past decision, which records the role and auth mode as evaluated at decision time; withdrawing an acceptance is an explicit revocation event (section 6). The actual account binding, role set and workspace mapping remain future prerequisites.

## 3. Identity And Schema (PROPOSAL_NOT_IMPLEMENTED)

Identity of an accepted version is the tuple of workspace, artifact key, version number and the byte identity (algorithm label `sha256-utf8-html-bytes/v1`, 64-character lowercase SHA-256, byte length) of the exact canonical `result.html` UTF-8 bytes. There is no trimming, newline conversion, BOM handling, Unicode normalization or re-render, and no Preview or Print derived digest is admissible. The route `sourceHash`, attempt id and receipt ids are stored in separate supporting columns and never consulted for identity.

Proposed logical tables. All are append-only; triggers abort any UPDATE or DELETE on them.

| Table | Purpose | Key constraints |
|---|---|---|
| `store_meta` | store identity and fencing | `store_id` fixed at provisioning, `writer_epoch`, `commit_seq`, `restore_generation`; SQLite `user_version` set to the schema version and `application_id` set to a dedicated constant so a foreign SQLite file is refused |
| `blobs` | content-addressed exact bytes | primary key (`algorithm`, `blob_sha256`); `byte_length`; `bytes` BLOB; CHECK that length equals `byte_length`; plain INSERT only, never OR IGNORE or upsert |
| `operation_attempts` | positive evidence that an operation started | primary key `operation_id`; `intent_digest`; `writer_epoch` at start; `started_at` |
| `operation_aborts` | positive evidence that an operation will not commit | primary key `operation_id`; reason; `writer_epoch`; `at` |
| `decisions` | immutable historical acceptances | primary key `decision_id`; UNIQUE `operation_id`; UNIQUE (`workspace_id`, `artifact_key`, `version_no`); foreign key to `blobs`; `actor_id`, `role_at_decision`, `auth_mode`, `org_id`, `team_id`, `decided_at`, `attempt_id`, `build_number`, `source_hash`, `receipt_evidence_json`, `attestation_digest`, `intent_digest`, nullable `supersedes_decision_id`, `commit_seq` |
| `lifecycle_events` | revocation, expiry, tombstone | primary key `event_id`; `decision_id`; kind of REVOKE, EXPIRE or DELETE_REQUEST; actor, reason, time |

Operation intent: `intent_digest` is SHA-256 over canonical JSON of `operationId`, `workspaceId`, `artifactKey`, the byte identity, the actor id and `basedOnDecisionId`. It is fixed before any write and stored on the attempt and on the decision.

Duplicate and conflict rules, which must hold together:

- Same `operationId`, same intent digest: idempotent; the existing decision is verified and returned, nothing is written.
- Same `operationId`, any different bytes, actor, workspace or base: OPERATION_CONFLICT; nothing is written; the existing record is untouched.
- Same bytes, different workspace or lineage: separate decisions that share one blob row. Content dedup applies to bytes only; the decision row is what records who accepted what, where and when.
- Same bytes, same workspace and lineage, different actor while the latest effective decision already holds those bytes: ALREADY_EFFECTIVE, returning the original decision. The second actor is not recorded as an acceptance and the first record is not altered; co-signing is not supported.
- A blob row whose stored bytes do not hash to its key, or whose length differs: STORE_CORRUPT. It is never overwritten or re-inserted over; it is routed to the recovery owner.

## 4. Store And Writer

The candidate is one SQLite file on one host with one writer process. This is an architectural judgment, not tested behavior, and no file, schema or lock is created by this design.

- Atomic boundary: blob and decision rows are inserted in one transaction, so exact bytes and acceptance metadata commit together. The governance-event ledger is a different database and cannot share that transaction; an event emitted after commit is best-effort and non-authoritative, and a missing event never negates a committed acceptance.
- Durability assumptions: `journal_mode = WAL` and `synchronous = FULL` are verified at open and the store refuses to open otherwise, matching the governance ledger (`sqlite_ledger.py` lines 235-236) and unlike the generic adapter. The store file must be on a local disk, not a network share. That the host honors fsync is an assumption and is not verified here.
- Writer admission: exactly one writer module owns a single serialized write connection per process. Each write transaction starts with `BEGIN IMMEDIATE`, checks `store_meta.writer_epoch` against the epoch the writer was started with, and aborts on mismatch. A second process that opens the file for write finds the lock busy (mapped to WRITER_BUSY, never success and never a retry grant) or presents a stale epoch (WRITER_FENCED). Taking over as writer is an explicit recovery-owner action that increments the epoch. SQLite cannot stop a foreign process that ignores this protocol from editing the file; the real control is operating-system file permission, which is a real-effect prerequisite.
- Explicit provisioning: creating a store is a separate provisioning function that is never called from read, reconcile or accept. The accept path opens an existing, verified store or fails with STORE_MISSING; it never creates, migrates or repairs. This is the direct answer to the generic adapter's read-init defect.
- Immutability: triggers abort UPDATE and DELETE on every table. This blocks accidental overwrite through the module; it does not defend against file-level tampering, so each read also re-verifies bytes against the key hash.
- Size: bytes are bounded by the same body limit the export route already enforces (`MAX_BODY_BYTES`, 128000 in `route.ts` line 38).

## 5. Protocol, Outcomes And Classification

Write protocol (each step names what the caller may be told):

1. Admission and byte validation, no write (section 2). Failure returns a refusal.
2. Transaction one: `BEGIN IMMEDIATE`; check store identity, schema, durability settings and epoch; if the operation already has a decision, verify the intent digest and return it, or return OPERATION_CONFLICT; otherwise insert the `operation_attempts` row and COMMIT. This makes an in-doubt operation visible.
3. Transaction two: `BEGIN IMMEDIATE`; recheck epoch (a stale epoch aborts the transaction with WRITER_FENCED and writes nothing); recheck session freshness and check `basedOnDecisionId` against the latest effective decision, and on SESSION_EXPIRED or STALE_BASE write an `operation_aborts` row, commit and refuse; insert the blob with plain INSERT, verifying the existing bytes if the key already exists; insert the decision with the next `version_no`; increment `commit_seq`; COMMIT.
4. Readback on a fresh connection: select the decision joined to its blob, recompute SHA-256 and length over the stored bytes, and compare identity and metadata with the operation intent.
5. Only after step 4 matches, return the verified acknowledgment (decision id, byte identity, `store_id`, `commit_seq`). Any readback failure returns an unverified outcome that is treated as UNKNOWN and routed to classification.

Outcome by failure point. No row of this table grants a retry.

| Stage reached | What the store holds | Caller learns | Later classification |
|---|---|---|---|
| Refused in step 1 | nothing | refusal | NOT_FOUND_UNWITNESSED, which is UNKNOWN |
| Failed before transaction one commits | nothing | no acknowledgment | NOT_FOUND_UNWITNESSED, which is UNKNOWN |
| Transaction one committed, transaction two not | attempt row only | no acknowledgment | IN_DOUBT until fenced or aborted |
| Failure during transaction two | attempt row only, SQLite rolls back | no acknowledgment | IN_DOUBT until fenced or aborted |
| Transaction two committed, readback or acknowledgment not delivered, or response lost | attempt and decision rows | no verified acknowledgment | COMMITTED_VERIFIED when the bytes hash correctly |
| Readback mismatch | decision rows present, bytes disagree | unverified outcome | CORRUPT_OR_CONFLICTING |

Read-only classification binds the exact tuple of `store_id`, workspace, `operationId`, artifact key, byte identity and actor. It works on a scratch byte copy of the store file and any `-wal` and `-shm` sidecars, exactly as `classify_target` does (`sqlite_ledger.py` lines 119-162), and opens only the copy. It never initializes, creates, migrates, repairs or writes the live store. Every result carries `retryGranted: false` and `authoritative: false`. A copy cannot be assumed to be a consistent snapshot while a writer is active, so an inconsistent or unreadable copy is UNKNOWN, never a negative.

| Classification | Condition | Meaning for the actor |
|---|---|---|
| COMMITTED_VERIFIED | store identity matches; integrity check passes; decision for the operation exists; its blob bytes hash to the key; metadata equals the intent digest | the version was accepted |
| ABSENT_ABORTED | an `operation_aborts` row exists for the operation and no decision | positively not accepted |
| ABSENT_FENCED | an attempt row exists with an epoch older than the store epoch, and no decision | positively not accepted, because a stale writer can no longer commit |
| IN_DOUBT_UNKNOWN | an attempt row exists at the current epoch with no decision and no abort | unknown; a recovery-owner fencing step is needed before any negative |
| NOT_FOUND_UNWITNESSED | no attempt, decision or abort row for the operation | unknown, not a negative |
| CORRUPT_OR_CONFLICTING | integrity failure, blob hash mismatch, or decision and intent disagreement | needs owner recovery; nothing is trusted |
| STORE_IDENTITY_MISMATCH, STORE_MISSING, STORE_UNREADABLE, SNAPSHOT_INCONSISTENT | wrong, absent, locked or torn store | all UNKNOWN; absence from a missing, wrong or restored store is never definitive |

A retry after any classification is a new explicit decision by the actor with the same `operationId`, which the store treats idempotently; classification itself never grants it.

## 6. Lifecycle, Revocation, Expiry And Restore

- Historical versus effective: `decisions` is the immutable history of what was accepted and by whom. The effective acceptance of a lineage is derived, never stored as a mutable flag: the highest `version_no` whose decision has no later REVOKE or EXPIRE event.
- Correction: a corrected packet is a new version and a new decision that references the earlier one through `supersedes_decision_id`. Nothing is updated or deleted.
- Revocation and expiry: both are appended `lifecycle_events` by an authorized actor or by an expiry policy. After a revocation the lineage has no effective acceptance. The design does not fall back to an older version automatically, because that would promote a stale decision; a person must accept again. The expiry period and who may revoke are operator policy, not decided here.
- Deletion: no physical deletion. A DELETE_REQUEST event records the request; bytes remain until a separately governed purge procedure by the recovery owner, with evidence. Retention rules are UNKNOWN.
- Privilege changes: a past decision keeps the role and auth mode recorded at decision time. Later role changes do not rewrite it.
- Older backup restore: restoring an older copy must not promote stale effective decisions. A restore is performed only by the recovery owner, who increments `writer_epoch` and `restore_generation` and appends the event. An inside-the-store view cannot detect a silent restore by itself, because a lower `commit_seq` is only meaningful against an independent witness of the highest acknowledged sequence, such as retained verified acknowledgments or governance-event records. Until that witness exists, effective reads from a store with unknown provenance are reported as EFFECTIVE_UNVERIFIED and a missing decision there is UNKNOWN. Backup location, key custody, retention, RPO and RTO remain UNKNOWN future gates and are not solved here.
- Recovery owner: a named person or role handles CORRUPT_OR_CONFLICTING, IN_DOUBT fencing, restore and purge, and records what was done. Who that is remains an operator decision.

## 7. Planned Cases

The evidence file `docs/reviews/evidence/cvf-ncr-html-b2-design-worker-evidence-2026-10-02.json` holds 48 planned cases with stable IDs B2D-C01 to B2D-C48. Each has the source requirement, precondition and input, injection stage, the actor, operation, version and store tuple, the expected record, acknowledgment and classification, and a proposed independent oracle that does not rely on the code under test. Every status is NOT_EXECUTED_DESIGN_ONLY. A table is not test proof, and none of these cases was run.

| Group | Case IDs | Covers |
|---|---|---|
| Admission | C01-C13 | valid accept; missing actor; forged role or scope; service token; impersonation; role denied; expired session; stale base; superseded version; edit after review; forged or expired attestation; receipt ALLOW only; refusal leaves draft |
| Identity | C14-C22 | same operation same and different bytes, actor, workspace; same hash different workspace and actor; corrupted same-hash blob; exact-byte variants; derived Preview or Print digest |
| Store and writer | C23-C27 | concurrent writers; foreign writer and stale epoch; immutability; durability settings; schema and foreign file refusal |
| Protocol faults | C28-C34 | failure before, between and during transactions; crash after commit before readback; lost acknowledgment; corrupt readback; event emission failure |
| Recovery | C35-C42 | wrong, missing, unreadable store; no-write reconciliation; fenced and aborted absence; restored store absence and stale decisions |
| Lifecycle | C43-C48 | revocation; expiry; correction; deletion request; privilege change; generic-adapter exclusion |

Harness proposal: a seam that is empty in production and set only by tests, modeled on the fault seam in `sqlite_ledger.py` (lines 19-25); a byte-level oracle that hashes the store file, its sidecars and the directory listing before and after a no-write case; and a second-process writer for concurrency cases. None of these exists today.

## 8. Future Topology And Prerequisites

Existing versus proposed paths. Proposed paths do not exist and nothing here creates them.

| Path | Status | Proposed role |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | existing, reuse unchanged | identity function |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | existing, modify | issue the export attestation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | existing, modify | register the accept route in the proof registry |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | existing, modify | separate Accept action showing identity |
| proposed `src/lib/html-artifact-acceptance-store.ts` under the Web package | proposed new | explicit provisioning, accept, read-only classify, effective read |
| proposed `src/lib/html-artifact-acceptance-admission.ts` under the Web package | proposed new | pure admission checks |
| proposed `src/app/api/artifacts/accept/route.ts` under the Web package | proposed new | accept route |
| proposed unit, fault-injection and browser test files | proposed new | the 48 planned cases |

Consequences to plan for: a new entry in the route proof registry, new GC-051 registry entries for new files, the as-built catalog and route inventory drift checks, a configuration variable naming the store location, ignore rules so a database is never committed, and the public technical catalog rule. No new dependency is needed because `better-sqlite3` is already declared. Rollback before real data: revert the commits. Deprecation after real data exists: disable the accept route, keep the store read-only, export bytes first, and never delete the file.

Synthetic implementation prerequisites (can be satisfied without real effects): the case harness, a throwaway store in a temporary directory, a stub session issuer, and an accepted-risk statement that the synthetic MAC key is test-only. Real-effect prerequisites (operator-owned, all UNKNOWN today): the real accepting accounts and roles, the workspace mapping, the real data and its classification, the store location and host, operating-system file permissions, MAC key custody, backup location and key custody, retention and deletion schedule, RPO and RTO, cost budget, and any pilot or live effect. No future dispatch follows automatically from this design.

## Open Design Choices For Local Review

These were resolved inside the selected direction and are listed so Local can ratify or change them: attestation required; impersonated and service-token sessions refused; synchronous FULL required; classification on a scratch copy; two-transaction commit with a positive attempt record; one effective version per lineage without automatic fallback; co-signing unsupported; `artifactKey` is new and not derived from existing fields.

## Limitations

SQLite file-level tampering, a foreign process ignoring the protocol, fsync honesty on the host, copy consistency during classification and silent restore without an independent witness are not defended by this design and are stated rather than assumed away. This is source-based design: no behavior was run, and all counts of cases are planned counts.

## Claim Boundary

This document is a proposal. It is not artifact acceptance, an implemented owner, store, schema or admission check, an operator decision, proof of any runtime behavior, or authorization for real data, provider or live use, public sync or deployment. Q001 and Q004 remain open and durable B2 and P11 remain parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
