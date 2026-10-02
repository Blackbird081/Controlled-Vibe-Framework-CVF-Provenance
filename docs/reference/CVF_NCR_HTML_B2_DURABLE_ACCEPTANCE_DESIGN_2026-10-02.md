# CVF NCR HTML B2 Durable Acceptance Design

Memory class: POINTER_RECORD

Status: PROPOSAL_NOT_IMPLEMENTED

docType: reference

Date: 2026-10-02

Revision: R1 (rework generation 1), revising the unratified R0 candidate to resolve findings B2D-F01 to B2D-F06.

## Purpose

Specify, as one coherent design for Local review, how an authenticated operator could durably accept one exact immutable version of the HTML review packet, under the selected DESIGN_DIRECTION_ONLY profile: a local single-host single-writer SQLite artifact-store candidate, separate from the governance-event ledger, with commit then readback verification and read-only classification of unknown outcomes. This document adds the selected authority and profile delta over B2a Part 2. It builds nothing: every schema, interface, path, lock and witness below is PROPOSAL_NOT_IMPLEMENTED, and every behavioral case in the paired evidence file is NOT_EXECUTED_DESIGN_ONLY.

## Scope / Applies To

Applies to the HTML export panel and route in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` as consumers, and to the identity helper `src/lib/html-artifact-acceptance-candidate.ts`. Canonical exports, Preview, Print and the accepted B2b-B2f transport evidence are unchanged and are consumed within their own limits. Source locators were read at the selected regions listed in the paired evidence JSON with SHA-256 values; the thirteen R0 source hashes were recomputed at the R1 execution base and none drifted. No database, server, browser, provider or transaction was run, and no real account, data or ledger was read.

## What R1 Changes And Why

R0 declared every table append-only yet required counters to be incremented; let a retry collide with its own attempt row; chose the effective acceptance by skipping revoked versions while promising no fallback; relied on a transaction lock as if it were a writer lifetime; treated an unknown restore as a special case instead of the default; and let one actor's decision answer another actor's intent. These are six views of one state machine, so R1 repairs them together around five design moves:

1. One append-only journal replaces every mutable counter. Commit sequence, writer epoch and restore generation are derived from it, never updated (F01).
2. Every operation has one derived state with terminal outcomes that never reopen, and an intent check in every state (F02).
3. The lineage head is chosen first and its own lifecycle decides effectiveness; nothing is promoted by fallback (F03).
4. A writer lifetime is admitted by an exclusive operating-system lock plus a fresh epoch per lifetime (F04).
5. Freshness is a contract with an external witness over the same journal sequence, and without it the design fails closed for anything that claims "current" (F05). Acknowledgment is bound to the exact submitted intent and a different actor's record is information only (F06).

## Selected-Profile Delta Over B2a Part 2

B2a Part 2 gave a five-step write protocol, an unknown-outcome rule and an open-decision list. It left the actor, the store owner, the writer model, the recovery observation and the lifecycle unspecified. This design adds the following, each traced to a section below.

| Delta | B2a Part 2 position | This design | Section |
|---|---|---|---|
| Actor binding | actor undecided | server-established actor, role and scope bound to operation, version and bytes; client role and receipt ALLOW never grant | 2 |
| Provenance of bytes | actor reviewed exact bytes, no mechanism | export attestation proves the bytes came from this server for this actor | 2 |
| Owner | separate store, owner undecided | new dedicated store adapted from named patterns; four existing owners rejected as acceptance authority | 1, 4 |
| Control metadata | not specified | one append-only hash-chained journal; counters and epoch are derived | 3 |
| Writer model | one writer process | writer lifetime admitted by an exclusive operating-system lock and a fresh epoch per lifetime | 4 |
| Operation lifecycle | commit before ack | total operation state machine with terminal outcomes and an intent check in every state | 5 |
| Durability | commit before ack | synchronous FULL required at open, unlike the existing generic adapter | 1, 4 |
| Recovery observation | look up identity read-only | classification on a scratch byte copy, never opening the live store for write | 6 |
| Absence and currency | absent row means not accepted | only terminal rows and an external freshness witness support negative or current claims | 6, 8 |
| Lifecycle | append-only correction | lineage head first, no fallback, explicit restore with declared loss | 7 |

## Finding-To-Design-To-Case Matrix

Every case id is a planned, unexecuted case in the paired evidence file. Resolution here means the design text is now internally consistent, checked statically; it is not behavioral proof.

| Finding | R0 contradiction in one line | R1 design resolution | Design sections | Planned cases |
|---|---|---|---|---|
| B2D-F01 | append-only schema forbade the counters the protocol had to increment | one append-only journal; sequence, epoch and restore generation derived; bytes and decisions immutable; takeover and restore are appended entries; rollback forbidden by sequence, chain and epoch rules | 3, 4, 8 | B2D-C01, C25, C49, C50, C51, C52 |
| B2D-F02 | retry collided with its own attempt row; existing attempts and aborts were not intent-checked; retry after terminal absence was permitted | total state machine unseen, attempted live, attempted fenced, committed, aborted; terminal states never reopen and need a new operationId; intent compared in every state; shared verified blob reused without a second insert | 3, 5, 6 | B2D-C14, C15, C16, C17, C20, C28, C29, C30, C39, C40, C53, C54, C55, C56, C57, C58, C59, C60, C61 |
| B2D-F03 | highest version skipping a revoked one promoted the older decision | lineage head first; a revoked or expired head leaves no effective acceptance; older decisions stay historical; basedOnDecisionId is the head even when ineffective | 7 | B2D-C08, C09, C43, C44, C45, C62, C63, C64, C65, C66, C67 |
| B2D-F04 | a transaction lock does not admit one writer for its lifetime | exclusive operating-system lock held for the writer lifetime plus a fresh epoch per lifetime; crash, release and takeover rules; second process refused even after the first commits | 4 | B2D-C23, C24, C68, C69, C70, C71, C72, C86 |
| B2D-F05 | an unknown-provenance store was a special case; no witness covered lifecycle, epoch and restore; a stale copy looked valid | witness over the single journal sequence; freshness rule; writer admission and any current or effective claim fail closed without it; terminal rows are prefix-safe; restore declares loss | 6, 7, 8 | B2D-C35, C36, C37, C38, C41, C42, C73, C74, C75, C76, C77, C78, C79, C80, C81 |
| B2D-F06 | refusal wrote nothing yet persisted rows; another actor's decision answered a new intent | pre-write versus post-intent refusal effects tabulated; acknowledgment only for the exact intent; lineage-already-effective is information; intent conflict is its own classification | 2, 5, 6 | B2D-C13, C16, C17, C19, C82, C83, C84, C85 |

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
- No existing source defines `workspace`. The session exposes `orgId` and `teamId`. The mapping is an open prerequisite (section 10); the design treats `workspaceId` as an opaque value the server derives from the session, never from the request body.

Disposition: ADAPT identity from the B2a helper, ADAPT patterns from the governance ledger, REJECT the generic adapter and the v3 ledger as acceptance authority, and PROPOSE the smallest dedicated store, a new TypeScript module in the Web library using the existing dependency. Consumer rationale: the Artifacts panel needs an explicit accept action and a later exact-byte retrieval that no existing owner provides. This is a bounded comparison of named sources, not a repository-wide absence claim.

## 2. Actor And Admission Contract

Only an authenticated operator, acting through a deliberate accept action that is separate from Build and separate from receiving a receipt, can accept. All admission facts are established by the server.

Proposed accept request (client supplies only claims to be checked): `operationId`, `artifactKey`, the exact `html` string the actor reviewed, the displayed `expectedIdentity` (algorithm, hash, length), the `exportAttestation` returned by the export route, and `basedOnDecisionId` or null. A `workspaceId`, role, actor or receipt decision in the body is ignored for authority.

Admission checks, evaluated in order, each with a named refusal. Every check in this table runs before any store write, so a refusal here is a pre-write refusal (rows are listed in section 5).

| Check | Server-established input | Refusal |
|---|---|---|
| Actor present | session from `authorizeRouteGovernanceProof`; `authMode` must be `session` | ACTOR_MISSING; service-token callers get AUTH_MODE_NOT_SESSION, because a service token is not an accepting operator |
| Not impersonated | session carries no impersonation | IMPERSONATED_SESSION; acceptance under impersonation is refused, since the recorded actor would be ambiguous |
| Role permitted | role from session checked by a policy predicate `canAcceptHtmlArtifact(role, workspaceId)`, default deny | ROLE_NOT_PERMITTED; which roles may accept is an operator decision, not made here |
| Scope | `workspaceId` derived from the session, not the body; the attestation and artifact lineage must be in the same workspace | SCOPE_MISMATCH |
| Freshness | session `expiresAt` later than now at first admission; attestation not expired | SESSION_EXPIRED, ATTESTATION_EXPIRED |
| Provenance | attestation verifies and binds the identity, attempt id, build number, actor and workspace | ATTESTATION_INVALID |
| Exact bytes | the server encodes `html` once as UTF-8 with no normalization, computes the B2a identity, and compares with `expectedIdentity` and the attestation | BYTES_MISMATCH; this is how an edit after review is caught |

Version freshness (STALE_BASE) and the second session check are made inside the writer transaction, because they need the lineage head; they are post-intent refusals (section 5).

The export attestation is a proposed addition to the export route response: a server-keyed MAC over the byte identity, attempt id, build number, actor id, workspace and issue time with a short expiry. It proves that these bytes were produced by this server for this actor and prevents accepting bytes the export never made. It is provenance evidence only. It cannot grant acceptance, and the MAC key custody is a real-effect prerequisite (section 10).

Receipt handling: `governanceReceipt` and `governanceState` values such as `RECEIPT_ALLOW_REVIEW_REQUIRED` are stored as opaque supporting evidence and never change admission. A receipt ALLOW without an explicit accept action produces no record.

Acknowledgment is bound to the exact submitted intent. A verified acceptance acknowledgment is issued only when the stored decision carries the same operation id, the same intent digest and the same session actor as the submission. A decision made by another actor or under another operation is never an acknowledgment of the submitted intent, even for identical bytes; it can appear only as lineage information (section 5).

Subsequent changes: an edit after review produces new bytes and therefore a new identity, so the earlier acceptance cannot apply to it. A later change to the actor's role does not rewrite a past decision, which records the role and auth mode as evaluated at decision time; withdrawing an acceptance is an explicit revocation event (section 7). The actual account binding, role set and workspace mapping remain future prerequisites.

## 3. Identity And Schema (PROPOSAL_NOT_IMPLEMENTED)

Identity of an accepted version is the tuple of workspace, artifact key, version number and the byte identity (algorithm label `sha256-utf8-html-bytes/v1`, 64-character lowercase SHA-256, byte length) of the exact canonical `result.html` UTF-8 bytes. There is no trimming, newline conversion, BOM handling, Unicode normalization or re-render, and no Preview or Print derived digest is admissible. The route `sourceHash`, attempt id and receipt ids are stored in separate supporting columns and never consulted for identity.

Control metadata and data are both append-only, which resolves the R0 conflict between immutable tables and counters that had to change. There is no mutable control row. The single source of ordering, epoch and restore history is the journal; commit sequence, current writer epoch and restore generation are derived by reading it.

Proposed logical tables. A trigger aborts any UPDATE or DELETE on every table below, and the design contains no statement that updates or deletes one.

| Table | Purpose | Key constraints |
|---|---|---|
| `journal` | the only ordering and control record | primary key `seq`; `kind` of PROVISION, WRITER_START, WRITER_RELEASE, RESTORE, ATTEMPT, DECISION, ABORT or LIFECYCLE; `ref_id`; `writer_epoch`; `prev_hash`; `entry_hash`; `at`. Insert rules: `seq` equals the previous `seq` plus one; `prev_hash` equals the previous `entry_hash`; `writer_epoch` equals the previous epoch, except WRITER_START and RESTORE which equal it plus one; `entry_hash` covers the entry fields and a digest of the row it references. The PROVISION entry fixes the `store_id` and schema version; `PRAGMA application_id` is set to a dedicated constant so a foreign SQLite file is refused |
| `blobs` | content-addressed exact bytes | primary key (`algorithm`, `blob_sha256`); `byte_length`; `bytes` BLOB; CHECK that length equals `byte_length` |
| `operation_attempts` | positive evidence that an operation started and the intent it started with | primary key `operation_id`; `intent_digest`; `writer_epoch` at start; `journal_seq` |
| `operation_aborts` | terminal evidence that an operation will not commit | primary key `operation_id` referencing its attempt; `reason`; `journal_seq` |
| `decisions` | immutable historical acceptances | primary key `decision_id`; UNIQUE `operation_id` referencing its attempt; UNIQUE (`workspace_id`, `artifact_key`, `version_no`); foreign key to `blobs`; `actor_id`, `role_at_decision`, `auth_mode`, `org_id`, `team_id`, `decided_at`, nullable `expires_at`, `attempt_id`, `build_number`, `source_hash`, `receipt_evidence_json`, `attestation_digest`, `intent_digest`, nullable `supersedes_decision_id`, `journal_seq`. An insert is refused if the operation already has an abort |
| `lifecycle_events` | revocation and deletion requests | primary key `event_id`; `decision_id`; kind of REVOKE or DELETE_REQUEST; actor, reason, time, `journal_seq` |

Derived values, never stored as mutable fields: `commit_seq` is the highest `seq`; the current writer epoch is the epoch of the latest journal entry; the restore generation is the count of RESTORE entries; an operation's state is derived from its rows and the epoch history (section 5); the effective acceptance of a lineage is derived from its head (section 7). Each state-changing row is inserted in the same transaction as its journal entry, so row and ordering cannot diverge.

Operation intent: `intent_digest` is SHA-256 over canonical JSON of `operationId`, `workspaceId`, `artifactKey`, the byte identity, the actor id and `basedOnDecisionId`. It is fixed before any write, stored on the attempt and copied to the decision.

Identity and duplicate rules, which hold together with the state machine in section 5:

- An operation id is bound to exactly one intent for its whole life. Any different bytes, actor, workspace, artifact key or base presented for an existing operation is OPERATION_CONFLICT in every state.
- Content dedup applies to bytes only. A blob row is shared by any number of decisions; the decision row is what records who accepted what, where and when. Same bytes in a different workspace or lineage are separate decisions over one blob row.
- A shared blob is verified and reused, never re-inserted: inside the transaction the writer selects the blob by key, recomputes the hash and length of the stored bytes, and only if the key is absent inserts it. A mismatch is STORE_CORRUPT. There is no insert-or-ignore and no upsert, so a duplicate-key error can never be the way a duplicate is detected.
- Same bytes, same lineage, a different actor or operation while the head is effective with those bytes: the submitted intent is not accepted (post-intent refusal ALREADY_EFFECTIVE_LINEAGE). The head decision is reported only as lineage information. The second actor is not recorded as an acceptance, the first record is not altered, and co-signing is not supported.
- A blob row whose stored bytes do not hash to its key, or whose length differs, is STORE_CORRUPT. It is never overwritten and is routed to the recovery owner.

## 4. Store And Writer

The candidate is one SQLite file on one host with one writer process at a time. This is an architectural judgment, not tested behavior, and no file, schema, lock or witness is created by this design.

Durability and atomic boundary:

- Blob and decision rows and their journal entry commit in one transaction, so exact bytes, acceptance metadata and ordering commit together. The governance-event ledger is a different database and cannot share that transaction; an event emitted after commit is best-effort, non-authoritative, and never a freshness witness.
- `journal_mode = WAL` and `synchronous = FULL` are verified at open and the store refuses to open otherwise, matching the governance ledger (`sqlite_ledger.py` lines 235-236) and unlike the generic adapter. The file must be on a local disk, not a network share. That the host honors fsync is an assumption and is not verified here.
- Bytes are bounded by the same body limit the export route already enforces (`MAX_BODY_BYTES`, 128000 in `route.ts` line 38).
- Creating a store is a separate provisioning function that is never called from read, reconcile, classify or accept. The accept path opens an existing, verified store or fails with STORE_MISSING; it never creates, migrates or repairs one.
- Triggers abort UPDATE and DELETE on every table. This blocks accidental overwrite through the module; it does not defend against file-level tampering, so each read re-verifies bytes against the key hash and the journal chain.

Writer lifetime admission (resolves the gap between a transaction lock and a writer lifetime). `BEGIN IMMEDIATE` only serializes transactions: two processes could each read the same epoch and take the transaction lock one after the other. Admission is therefore a lifetime concept with a named owner and explicit rules, all proposed:

| Aspect | Proposed rule |
|---|---|
| Owner | one writer module inside the Web server process; only that module may hold writer admission |
| Mechanism | an exclusive, non-blocking operating-system file lock on a sidecar lock file, held for the whole writer lifetime and released by the operating system when the process ends, plus a fresh epoch for every lifetime |
| Acquisition | take the lock; open the store; verify settings, store identity, schema, journal chain integrity and witness freshness (section 8); under `BEGIN IMMEDIATE` append a WRITER_START entry whose epoch is the previous epoch plus one; commit; record it with the witness; only then accept writes |
| Per-transaction check | every write transaction first confirms that the latest journal entry's epoch equals the writer's own epoch and that its WRITER_START exists; otherwise it writes nothing and returns WRITER_FENCED |
| Second process | lock acquisition fails and the process is refused for its entire lifetime with WRITER_ALREADY_ADMITTED, including after the first writer has committed; a process that does not hold the lock can never reach a write transaction, so a second same-epoch writer does not exist |
| Crash | the operating system releases the lock; the next process acquires it and appends WRITER_START with the next epoch, which fences every attempt of the dead lifetime |
| Clean release | the writer appends WRITER_RELEASE, then releases the lock; the next acquisition still appends its own WRITER_START |
| Hung process | the lock stays held, so no takeover is possible; the recovery owner must end the process, after which the crash rule applies |
| Takeover | only through acquiring the lock; no other path increments the epoch |
| Read-only users | classification and reconciliation never take the lock and never touch the live store (section 6) |
| Unsupported lock | if the platform or file system cannot provide an exclusive lock, the store refuses writer admission with WRITER_LOCK_UNSUPPORTED |

Limits stated, not hidden: a foreign process that ignores this protocol can still edit the file. That is prevented only by operating-system file permission (a real-effect prerequisite), and is made detectable by the journal chain and by the witness (section 8). The lock assumes one host with honest local-file locking.

## 5. Operation State Machine, Protocol And Refusal Effects

Every operation id has exactly one derived state, computed from rows and from the epoch history. Terminal states never reopen.

| State | Derivation | Terminal |
|---|---|---|
| UNSEEN | no attempt, decision or abort row for the id | no |
| ATTEMPTED_LIVE | attempt row, no decision, no abort, attempt epoch equals the current epoch | no |
| ATTEMPTED_FENCED | attempt row, no decision, no abort, a later WRITER_START or RESTORE entry exists | yes |
| COMMITTED | a decision row exists | yes |
| ABORTED | an abort row exists | yes |

Forward transitions only: UNSEEN to ATTEMPTED_LIVE (first transaction); ATTEMPTED_LIVE to COMMITTED (second transaction succeeds), to ABORTED (post-intent refusal with an abort row), or to ATTEMPTED_FENCED (the writer lifetime ends, derived by the next WRITER_START). Nothing leaves COMMITTED, ABORTED or ATTEMPTED_FENCED. A fresh explicit acceptance after any terminal outcome needs a new operationId and a new intent; no classification or replay grants a retry of the same operation.

Total request handling: same intent means the identical intent digest, conflicting intent means any difference.

| State | Same-intent request | Conflicting-intent request |
|---|---|---|
| UNSEEN | proceed to the first transaction | not applicable |
| ATTEMPTED_LIVE | OPERATION_IN_PROGRESS, no write | OPERATION_CONFLICT, no write |
| ATTEMPTED_FENCED | NEW_OPERATION_REQUIRED, no write | OPERATION_CONFLICT, no write |
| COMMITTED | re-verify and return the original verified acknowledgment, no write | OPERATION_CONFLICT, no write |
| ABORTED | return the stored abort reason with NEW_OPERATION_REQUIRED, no write | OPERATION_CONFLICT, no write |

A conflict response discloses nothing about the stored intent beyond the existence of a conflict.

Write protocol:

1. Admission and byte validation, no write (section 2).
2. First transaction: `BEGIN IMMEDIATE`; confirm the writer epoch; derive the operation state and apply the table above. Only for UNSEEN, insert the `operation_attempts` row and an ATTEMPT journal entry and COMMIT. An existing attempt row is never inserted over, so a replay cannot collide with it.
3. Second transaction: `BEGIN IMMEDIATE`; confirm the epoch again (a stale epoch returns WRITER_FENCED and writes nothing); confirm session freshness; compare `basedOnDecisionId` with the lineage head (section 7); check whether the head is effective with the submitted bytes. On SESSION_EXPIRED, STALE_BASE or ALREADY_EFFECTIVE_LINEAGE, insert the abort row and an ABORT journal entry, commit and refuse. Otherwise verify and reuse or insert the blob (section 3), insert the decision with the next `version_no` and a DECISION journal entry, and COMMIT.
4. Readback on a fresh connection: select the decision joined to its blob, recompute SHA-256 and length over the stored bytes, and compare identity, actor, operation and intent digest with the submission.
5. Record the new journal tail with the witness (section 8). Without a recorded tail the acknowledgment is withheld.
6. Return the verified acknowledgment (decision id, byte identity, `store_id`, `journal_seq`) only after steps 4 and 5 succeed. Any failure returns an unverified outcome treated as UNKNOWN and routed to classification.

Outcome by failure point. No row of this table grants a retry.

| Stage reached | Store holds | Caller learns | Later state and classification |
|---|---|---|---|
| Refused before any write | nothing | refusal | UNSEEN; NOT_FOUND, UNKNOWN unless the witness is fresh |
| Failed before the first transaction commits | nothing | no acknowledgment | UNSEEN |
| First transaction committed, second not started | attempt row | no acknowledgment | ATTEMPTED_LIVE then ATTEMPTED_FENCED after the next WRITER_START |
| Failure inside the second transaction | attempt row only, SQLite rolled back | no acknowledgment | same as above |
| Post-intent refusal | attempt row and abort row | refusal | ABORTED |
| Second transaction committed, readback, witness or response not completed | attempt, blob and decision rows | no verified acknowledgment | COMMITTED, ABSENT claims impossible |
| Readback mismatch | decision present, bytes disagree | unverified outcome | CORRUPT_OR_CONFLICTING |

Refusal effects, distinguishing pre-write from post-intent:

| Refusal | Stage | Rows written | OperationId consumed |
|---|---|---|---|
| ACTOR_MISSING, AUTH_MODE_NOT_SESSION, IMPERSONATED_SESSION, ROLE_NOT_PERMITTED, SCOPE_MISMATCH, SESSION_EXPIRED at admission, ATTESTATION_*, BYTES_MISMATCH | pre-write | none | no |
| STORE_MISSING, STORE_IDENTITY_MISMATCH, STORE_SETTINGS_UNSAFE, STORE_UNWITNESSED, WRITER_ALREADY_ADMITTED, WRITER_LOCK_UNSUPPORTED, WRITER_FENCED | infrastructure | none | no |
| OPERATION_CONFLICT, OPERATION_IN_PROGRESS, NEW_OPERATION_REQUIRED | first-transaction lookup | none | already bound |
| SESSION_EXPIRED at the decision transaction, STALE_BASE, ALREADY_EFFECTIVE_LINEAGE | post-intent | abort row and ABORT journal entry (the attempt row already exists) | yes, terminal |
| STORE_CORRUPT | second transaction | none; the store is untrusted, the operation stays attempted and is later fenced | yes |

Lineage information versus acknowledgment: ALREADY_EFFECTIVE_LINEAGE returns a lineage-information object (head decision id and byte identity, no attribution of an acceptance to the requester, and no actor disclosure unless policy decides otherwise) and is explicitly not an acknowledgment. For actor B with operation B submitting bytes already effective through actor A with operation A, B's operation is ABORTED and its classification is ABSENT_ABORTED, while A's operation remains COMMITTED_VERIFIED for A's exact tuple only.

## 6. Read-Only Classification

Classification binds the exact tuple of `store_id`, workspace, `operationId`, artifact key, byte identity and actor, and answers only about that tuple. It works on a scratch byte copy of the store file and any `-wal` and `-shm` sidecars, exactly as `classify_target` does (`sqlite_ledger.py` lines 119-162), and opens only the copy. It never initializes, creates, migrates, repairs or writes the live store and never takes the writer lock. Every result carries `retryGranted: false` and `authoritative: false`, and separates two facts: whether a historical record exists, and whether currency can be asserted (`currentlyEffective` is one of VERIFIED_FRESH, UNVERIFIED or NOT_EFFECTIVE). A copy cannot be assumed to be a consistent snapshot while a writer is active, so an inconsistent or unreadable copy is UNKNOWN, never a negative.

| Classification | Condition | Needs a fresh witness |
|---|---|---|
| COMMITTED_VERIFIED | store identity and chain verify; a decision for the operation exists whose operation, actor and intent digest equal the tuple; its blob hashes to the key. This is a historical record only | no |
| INTENT_CONFLICT | the operation exists with a different intent than the tuple; nothing is said about the stored intent beyond the conflict | no |
| ABSENT_ABORTED | an abort row exists for the operation under the tuple's intent and no decision | no |
| ABSENT_FENCED | an attempt row under the tuple's intent exists with an epoch older than a later WRITER_START or RESTORE entry, and no decision | no |
| IN_DOUBT_UNKNOWN | an attempt row exists at the latest epoch with no decision and no abort | no |
| NOT_FOUND_AS_OF | no row for the operation, and the witness is fresh; reported as of a stated journal sequence and never as a promise that the operation cannot commit later | yes |
| NOT_FOUND_UNWITNESSED | no row for the operation and no fresh witness | UNKNOWN |
| CORRUPT_OR_CONFLICTING | integrity failure, blob hash mismatch, chain break, or decision and intent disagreement | no |
| STORE_STALE | the store tail is below the witness high-water mark or its hash differs there | UNKNOWN |
| STORE_IDENTITY_MISMATCH, STORE_MISSING, STORE_UNREADABLE, SNAPSHOT_INCONSISTENT | wrong, absent, locked or torn store | UNKNOWN |

Why the terminal negatives need no witness: the journal is a total order and any copy is a prefix of it. A decision for an operation can only be committed while the operation's epoch is current, so it precedes any later WRITER_START or RESTORE entry; every prefix that contains the fencing entry therefore contains that decision if it existed. An abort row is terminal and a decision insert is refused after it. These two negatives are therefore stable under any consistent prefix. What a prefix cannot support is anything about the future of the log: absence of an operation, the lineage head, a later revocation, and currentness, which is why those require witness freshness.

A retry after any classification is a new explicit decision by the actor under a new operationId when the earlier operation is terminal, or no action while it is in progress; classification itself never grants it.

## 7. Lifecycle, Revocation, Expiry And Correction

- Historical versus effective: `decisions` is the immutable history of what was accepted and by whom. Effectiveness is derived, never stored.
- Lineage head first: the head of a lineage is its decision with the highest `version_no`, whatever its lifecycle. The lineage has an effective acceptance only if the head has no REVOKE event and its `expires_at`, when present, is later than now. If the head is revoked or expired, the lineage has no effective acceptance. Older decisions remain historical and are never promoted; there is no fallback to the newest unrevoked version.
- Lifecycle events on a non-head decision are historical annotations and do not change the lineage's effective status.
- `basedOnDecisionId` is the lineage head decision id even when the head is revoked or expired, and null only for an empty lineage. A request based on any other decision is STALE_BASE. An accept on top of a revoked or expired head creates the next version and is the explicit way to restore effectiveness; the new decision's `supersedes_decision_id` is that head. Re-accepting the same bytes after a revocation is therefore allowed, whereas the same bytes under an effective head are ALREADY_EFFECTIVE_LINEAGE.
- Correction: a corrected packet is a new version and decision referencing the earlier head. Nothing is updated or deleted.
- Revocation and expiry: REVOKE is an appended `lifecycle_events` row by an authorized actor with a journal entry and a witness record. Expiry is derived from the decision's `expires_at`, whose period is operator policy and unknown here. Who may revoke is an operator decision.
- Deletion: no physical deletion. A DELETE_REQUEST event records the request; bytes remain until a separately governed purge by the recovery owner, with evidence. Retention is unknown.
- Privilege changes: a past decision keeps the role and auth mode recorded at decision time.
- Recovery owner: a named person or role handles CORRUPT_OR_CONFLICTING, hung-writer termination, restore and purge, and records what was done. Who that is remains an operator decision.

## 8. Freshness Witness Contract (Future Admission Blocker)

A silent restore of an older copy keeps the same `store_id` and schema and is internally consistent, so nothing inside the store can tell that decisions, revocations or fencing history are missing. Freshness therefore needs evidence outside the store's failure domain. This section defines the dependency; implementing the witness, choosing its location and custody and naming its owner are future gates and none is requested or built here. For a synthetic implementation, a clearly labelled SYNTHETIC_WITNESS_ASSUMPTION may stand in; it is never deployed.

What the witness is: an append-only record, outside the store file and outside the store's backup and restore unit, of `(store_id, restore_generation, seq, entry_hash, kind, ref_id)` for journal entries. Because every state change is a journal entry, one sequence covers acceptance, abort, lifecycle, attempt, writer start and release, and restore transitions. A best-effort governance event is not a complete witness: it is not ordered by the journal, can be missing, and shares nothing with this chain.

Write order: after a transaction commits, its journal tail is recorded with the witness before any acknowledgment is returned, and before a lifecycle or restore result is reported. Failure to record leaves the store ahead of the witness. That is the safe direction because nothing was acknowledged; the writer stops admitting new writes with STORE_UNWITNESSED until the next admission brings the witness forward.

Freshness rule: a store snapshot is fresh for a claim only if the witness is reachable, the `store_id` and restore generation match, the snapshot's tail `seq` is at least the witness high-water mark, and the snapshot's entry hash at that mark equals the witness hash.

Fail-closed consequences when freshness is not established, including when no witness exists yet:

| Claim | Without freshness | With freshness |
|---|---|---|
| Writer admission or any write | refused with STORE_UNWITNESSED | allowed |
| Currently effective acceptance | reported EFFECTIVE_UNVERIFIED | VERIFIED_FRESH |
| Lineage head, ALREADY_EFFECTIVE_LINEAGE information, STALE_BASE decision | not issued by a read; the writer relies on its own admitted fresh store | issued |
| Not found | NOT_FOUND_UNWITNESSED, UNKNOWN | NOT_FOUND_AS_OF a stated sequence |
| Historical exact-byte evidence (COMMITTED_VERIFIED), ABSENT_ABORTED, ABSENT_FENCED | still issuable, labelled historical | issuable |

Restore transitions: a restore is performed by the recovery owner while holding the writer lock. The owner verifies the backup's chain and compares its tail with the witness. If the tail is at least the high-water mark and the hash matches, nothing was lost and the writer is admitted with a WRITER_START. If the tail is lower, data would be lost and the owner must record RESTORE_ACCEPTING_LOSS: a RESTORE journal entry carrying the lost range and, from the witness, the identifiers it contained, and a new restore generation recorded with the witness. Until the owner resolves them, any lineage and any operation id named in the lost range read as EFFECTIVE_UNVERIFIED_LOST_RANGE and as an operation whose state is unknown, so a lost decision, a lost revocation or lost fencing history cannot silently reappear as an effective acceptance or as a reusable operation id. A writer that starts on a store whose tail is below the witness mark without an accepted-loss RESTORE entry is refused, which prevents the restored copy from forking the history.

Rollback of control metadata is rejected by construction: a journal entry must carry the next sequence, the previous hash and a non-decreasing epoch, no entry can be updated or deleted, and any file whose tail or hash disagrees with the witness is stale.

## 9. Planned Cases

The evidence file `docs/reviews/evidence/cvf-ncr-html-b2-design-worker-evidence-2026-10-02.json` holds the planned cases with stable IDs from B2D-C01 upward. Each has the source requirement, precondition and input, injection stage, the actor, operation, version and store tuple, the expected record, acknowledgment and classification, and a proposed independent oracle that does not rely on the code under test. Every status is NOT_EXECUTED_DESIGN_ONLY. A table is not test proof, and none of these cases was run. Cases C01 to C48 keep their R0 identifiers; those whose expectations the R1 repairs changed are revised in place and marked, and C49 to C86 are new.

| Group | Case IDs | Covers |
|---|---|---|
| Admission | C01-C13 | valid accept; missing actor; forged role or scope; service token; impersonation; role denied; expired session; stale base; superseded version; edit after review; forged or expired attestation; receipt ALLOW only; pre-write refusals leave the store untouched |
| Identity | C14-C22 | same operation same and different bytes, actor, workspace with exact-intent outcomes; same hash in other workspace and other actor; corrupted shared blob; exact-byte variants; derived digests |
| Store and writer | C23-C27 | second writer after the first commits; stale epoch; immutability; durability settings; schema and foreign file refusal |
| Protocol faults | C28-C34 | failure before, between and during transactions; crash after commit before readback; lost acknowledgment; corrupt readback; event emission failure |
| Recovery | C35-C42 | wrong, missing, unreadable store; no-write reconciliation; fenced and aborted absence; restored store absence and stale decisions |
| Lifecycle | C43-C48 | head-first revocation and expiry; correction; deletion request; privilege change; generic-adapter exclusion |
| F01 metadata | C49-C52 | normal acceptance, takeover and restore transitions against the actual append-only constraints; forbidden rollback |
| F02 operation states | C53-C61 | attempted replay, fenced replay, conflicting intent in attempted and aborted states, abort replay, stale-writer replay, new operation after terminal, shared blob reuse, pre-write refusal not consuming the id |
| F03 lineage head | C62-C67 | D1, D2, D3 with D3 revoked and expired; revocation of a non-head decision; accept on a revoked head; stale base on an older decision; same bytes re-accepted after revocation |
| F04 writer lifetime | C68-C72, C86 | second process after commit, crash release and takeover, clean release, hung writer, foreign non-protocol writer, unsupported lock |
| F05 witness | C73-C81 | no witness, fresh witness, silent restore with lost decision, lost revocation and lost fencing history, fork prevention, witness failure after commit, governance event is not a witness, historical versus current |
| F06 exact intent | C82-C85 | pre-write versus post-intent rows, actor B against actor A, intent conflict classification |

Harness proposal: a seam that is empty in production and set only by tests, modeled on the fault seam in `sqlite_ledger.py` (lines 19-25); a byte-level oracle that hashes the store file, its sidecars and the directory listing before and after a no-write case; a second-process writer for lifetime cases; and a synthetic witness stub. None of these exists today.

## 10. Future Topology And Prerequisites

Existing versus proposed paths. Proposed paths do not exist and nothing here creates them.

| Path | Status | Proposed role |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | existing, reuse unchanged | identity function |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | existing, modify | issue the export attestation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | existing, modify | register the accept route in the proof registry |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | existing, modify | separate Accept action showing identity |
| proposed `src/lib/html-artifact-acceptance-store.ts` under the Web package | proposed new | explicit provisioning, writer admission, accept, read-only classify, effective read |
| proposed `src/lib/html-artifact-acceptance-admission.ts` under the Web package | proposed new | pure admission checks |
| proposed `src/lib/html-artifact-acceptance-witness.ts` under the Web package | proposed new | witness client interface and the labelled synthetic stand-in |
| proposed `src/app/api/artifacts/accept/route.ts` under the Web package | proposed new | accept route |
| proposed unit, fault-injection and browser test files | proposed new | the planned cases |

Consequences to plan for: a new entry in the route proof registry, new GC-051 registry entries for new files, the as-built catalog and route inventory drift checks, a configuration variable naming the store location, ignore rules so a database is never committed, and the public technical catalog rule. No new dependency is needed because `better-sqlite3` is already declared; the operating-system lock needs a Node-compatible mechanism whose choice is an implementation task. Rollback before real data: revert the commits. Deprecation after real data exists: disable the accept route, keep the store read-only, export bytes first, and never delete the file.

Synthetic implementation prerequisites (can be satisfied without real effects): the case harness, a throwaway store in a temporary directory, a stub session issuer, a labelled synthetic witness and an accepted-risk statement that the synthetic MAC key is test-only. Real-effect prerequisites (operator-owned, all UNKNOWN today): the real accepting accounts and roles, the workspace mapping, the real data and its classification, the store location and host, operating-system file permissions, MAC key custody, the real witness (its location outside the store's backup unit, owner, custody, retention and availability), backup location and key custody, retention and deletion schedule, RPO and RTO, cost budget, the recovery owner, and any pilot or live effect. No future dispatch follows automatically from this design.

## Open Design Choices For Local Review

These were resolved inside the selected direction and are listed so Local can ratify or change them: attestation required; impersonated and service-token sessions refused; synchronous FULL required; classification on a scratch copy; two-transaction commit with a positive attempt record; one append-only journal instead of mutable control fields; an operating-system lock held for the writer lifetime and a fresh epoch per lifetime; terminal operations never reopen and need a new operationId; lineage head first with no fallback; a witness over the journal sequence as a hard admission blocker with fail-closed reads; co-signing unsupported; `artifactKey` is new and not derived from existing fields.

## Limitations

SQLite file-level tampering, a foreign process ignoring the protocol, fsync honesty on the host, lock honesty on the file system, copy consistency during classification and the unavailability of a real witness are not defended by this design and are stated rather than assumed away. This is source-based design: no behavior was run, no mechanism exists, and every count of cases is a planned count.

## Claim Boundary

This document is a proposal. It is not artifact acceptance, an implemented owner, store, schema, lock, witness or admission check, an operator decision, proof of any runtime behavior, or authorization for real data, provider or live use, public sync or deployment. Q001 and Q004 remain open and durable B2 and P11 remain parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
