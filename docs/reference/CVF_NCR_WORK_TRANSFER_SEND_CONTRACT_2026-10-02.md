# CVF NCR Work Transfer Send Contract

Memory class: POINTER_RECORD

Status: DESIGN_PROPOSAL_PENDING_REVIEW

docType: reference

Date: 2026-10-02

## Purpose

Define, as a logical contract only, what it means for an authenticated sender to confirm sending one identified work packet to one designated recipient inside one workspace, who may read that send record afterwards, and how the contract separates a send from a validator result, an audit event, a recipient acknowledgment and an artifact acceptance. The operator selected this direction in `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_PRODUCT_SCOPE_CHECKPOINT_2026-10-02.md`; that selection ratifies direction, not this text. Every field, state, refusal code and gate below is a proposal for Local review. Nothing was executed, imported, requested or changed, and every behavior statement is a reading of source or a design rule. No send exists today; this contract does not create one.

## Scope / Applies To

Applies to: the send action only. In scope: sender confirmation, sender, recipient and workspace binding, packet reference and version identity, same-workspace read policy, duplicate, conflict and unknown-outcome handling, existing-owner comparison, future gates.

Out of scope and not defined here: recipient acknowledgment, HTML artifact acceptance, any durable acceptance, storage selection, schema or migration, route or UI implementation, real accounts, workspaces, membership, admin binding, backup, retention, custody, cost and recovery. Those stay UNKNOWN. rawMemoryReleased=false: no memory, runtime store, `.env`, credential or Downloads content was read.

Independence: this is not a B2 successor. B2 stays terminal STOP_REASSESS_ARCHITECTURE/NO_SUCCESSOR; no acceptance store, witness, OS lock, backup mechanism or renamed successor is proposed (SC-REQ-21).

Source basis: clean released base `3e1b6cb9a7003cad6b723717b5894bc3d50601d2`; source hashes and a pre-authoring seal are in `docs/reviews/evidence/cvf-ncr-work-transfer-send-contract-worker-evidence-2026-10-02.json`. Source graph depth is the accepted partial graph of `docs/reviews/CVF_CVF_NCR_HTML_WORK_TRANSFER_SOURCE_RECORD_REACHABILITY_COMPLETION_2026-10-02.md` plus the named owners read at the locators below. No producer rescan and no repository-wide absence claim is made.

## 1. Stage Model And Non-Equivalence

| Stage | Meaning | Is it a send? | Exists today |
|---|---|---|---|
| S0 Draft or intent | Values in the page form or an editable export draft | No | Yes, client-local state only (`page.tsx` lines 127-143) |
| S1 Submitted request | A server received a request that asks for a send; all fields untrusted | No | No |
| S2 Recorded send | The server verified bindings, packet identity and duplicates and a verifier confirmed the record exists | Yes, the only business send | No |
| S3 Recipient acknowledgment | The recipient confirms receipt | Not defined here | No |
| S4 Artifact acceptance | An artifact is accepted as the work product | Not defined here | No |

SC-REQ-01 One send action. A send is one authenticated sender's explicit confirmation of one packet identity to one designated recipient in one workspace. One request produces at most one recorded send.

SC-REQ-02 Stage separation. Draft, submitted request, recorded send, recipient acknowledgment and artifact acceptance are distinct stages with distinct evidence. This contract defines only S0 to S2.

SC-REQ-03 Non-equivalence. None of the following is the business send on its own: a validator ALLOW or WARN, an audit event of any kind, an admin-seeded audit row, an HTTP success status, or a rendered history row. Source basis: `validateHandoff` checks supplied task and context values only (`agent-handoff-validator.ts` lines 209-250); the page states that checking context does not save or create a transfer record (`page.tsx` lines 39 and 70); the admin audit POST accepts caller-supplied actor and action (`audit/route.ts` lines 29-42), so an audit row cannot prove who sent what.

SC-REQ-04 No inferred downstream stage. No acknowledgment, acceptance, delivery or read receipt may be inferred from a recorded send, from a recipient reading it, or from an admin reading it. Reading a record by the recipient is not acknowledgment.

SC-REQ-05 Explicit confirmation. A send requires a per-packet, per-recipient confirmation act by the sender in the same request that names the packet identity and recipient. Defaults, auto-fill, batch confirmation, replayed confirmations and confirmations carried by a different session are refused (SC-RF-14).

## 2. Logical Send Record

Field names are logical and illustrative. They are not a schema, a migration or a storage layout, and no physical store path is selected.

| Logical field | Origin | Trust | Rule |
|---|---|---|---|
| sendId | server | trusted | Server-generated identifier; a caller-supplied identifier is ignored |
| recordedAt | server | trusted | Server clock at recording; caller timestamp ignored |
| senderRef | server-derived from the authenticated session | trusted | Never taken from the request body |
| workspaceRef | server-derived from the verified sender binding | trusted | Opaque; its mapping to org, team or another unit is UNKNOWN (see section 4) |
| recipientRef | submitted, then verified | trusted only after verification | Must resolve inside the same workspaceRef |
| packetRef, packetVersion | submitted, then classified | trusted only as classified in section 6 | Classification is recorded with the record |
| packetEvidence | submitted pointers plus server observations | pointers untrusted; observations trusted | Each pointer carries its own classification |
| confirmation | submitted act | untrusted until bound to the session | Bound to senderRef, recipientRef and packet identity |
| requestId | submitted | untrusted | Used only for idempotent replay (section 8) |
| stage | server | trusted | One of the states in section 9 |
| contractVersion | server | trusted | Version of this contract the record was admitted under |

SC-REQ-15 Trusted versus submitted. Only server-derived values and server observations are authority. Submitted values are claims that must be verified or refused. Where a submitted claim disagrees with a server-derived value the request is refused (SC-RF-09), not silently corrected, so tampering is visible.

## 3. Identity And Binding

SC-REQ-06 Sender is server-derived. The sender is the principal the server authenticated for this request. Source basis: the session carries userId, role, orgId, teamId and authMode (`middleware-auth.ts` lines 20-30). The audit POST shows the failure pattern to avoid: actorId and actorRole come from the body before the session (`audit/route.ts` lines 32-33).

SC-REQ-07 Recipient is verified inside the workspace. The recipient must resolve through a workspace membership resolver to an active member of the sender's workspace. The resolver does not exist in the inspected graph and is an UNKNOWN future gate (G-BIND). A recipient that does not exist and a recipient in a foreign workspace produce the same refusal (SC-RF-07) so the response is not an account-enumeration oracle. Arbitrary recipient lookup by free text is not part of this design.

SC-REQ-08 Workspace is bound at record level. Every recorded send carries a verified workspaceRef. A record without one is unreadable to every principal (SC-RF-25). The existing audit event type has no org, team or workspace field (`control-plane-events.ts` lines 33-44), while the neighboring cost event does (lines 46-58); an audit-event row cannot be assumed to carry a scope.

SC-REQ-09 Caller-supplied authority is not authority. Actor, role, organization, team, workspace and admin flags in a request body, query or header are never used to decide admission or scope. This includes the internal-call header path of the audit POST (`audit/route.ts` lines 19-24), which bypasses the session by shared secret and is not a transfer identity.

SC-REQ-10 Workflow role is not enterprise permission. AgentRole values (orchestrator, architect, builder, reviewer) describe workflow steps and are looked up from a fixed table with an orchestrator fallback for an unknown agent id (`agent-handoff-validator.ts` lines 53-78 and 186-194). TeamRole values (owner, admin, developer, reviewer, viewer) are enterprise access roles (`enterprise-access.ts` lines 3-4). The name reviewer appears in both vocabularies and means two different things. Neither maps to the other; a workflow role never grants send or read, and a team role never satisfies a workflow sequence.

SC-REQ-13 Special callers. Impersonated sessions, delegated or on-behalf-of sends, service or internal callers and break-glass sessions cannot send. Source basis: an impersonated session presents the impersonated user's userId and role plus realUserId (`middleware-auth.ts` lines 159-175); the break-glass session is a fixed owner identity bound to a fixed organization and team that passes every admin check (`admin-session.ts` lines 13-31 and 206-216). A sender confirmation must come from the person, so these are refused (SC-RF-10, SC-RF-11, SC-RF-12, SC-RF-13).

Binding sourcing rule: a sender binding that came from a fallback default is not a binding. In development and test the session falls back to userId unknown-user, role developer, org_cvf and team_eng when the token lacks fields (`middleware-auth.ts` lines 97-109 and 117-129). A request whose binding is the fallback is refused (SC-RF-04). Whether production binding is complete is UNKNOWN and is not claimed.

## 4. Workspace And Membership Status

| Item | Status | Basis |
|---|---|---|
| Account to person mapping | UNKNOWN | Only a mock enterprise user table and an optional production binding helper appear in the graph; real mapping not inspected |
| Workspace definition | UNKNOWN | The session has orgId and teamId, no workspace field; the operator has not said which unit is the workspace |
| Membership resolution | UNKNOWN | No resolver in the inspected graph |
| Admin binding per workspace | UNKNOWN | The only admin predicate is a role check with no scope (`enterprise-access.ts` lines 6-14) |
| Real store and its contents | UNKNOWN | Adapter chosen by environment; not read |

The contract keeps workspaceRef opaque so the operator can later bind it to exactly one unit without rewriting the rules.

## 5. Read Policy

SC-REQ-11 Design read policy. A principal may read a recorded send only if all hold: authenticated by a real session; the record has a verified workspaceRef; the principal's verified workspace equals the record's workspaceRef; and the principal is the sender, the designated recipient, or an authorized owner or admin of that same workspace.

SC-REQ-12 No overrides. No cross-workspace administrator inheritance, no arbitrary recipient lookup, and no break-glass inheritance. Missing identity or missing scope fails closed.

| Principal | Same workspace as record | Decision | Refusal code |
|---|---|---|---|
| Sender | yes | ALLOW | none |
| Designated recipient | yes | ALLOW, read only, not acknowledgment | none |
| Owner or admin (by role predicate and verified binding) | yes | ALLOW, oversight read | none |
| Owner or admin | no | DENY | SC-RF-24 |
| Developer, reviewer or viewer who is neither sender nor recipient | yes | DENY | SC-RF-23 |
| Unauthenticated | not applicable | DENY | SC-RF-22 |
| Any principal, record without verified workspaceRef | not applicable | DENY | SC-RF-25 |
| Break-glass session | not applicable | DENY by default | SC-RF-26 |
| Impersonated session | evaluated as the effective principal only | follows the rows above; realUserId is recorded | per row |
| Service or internal-secret caller | not applicable | DENY | SC-RF-12 |

The existing admin audit read must not be reused as the transfer read. It returns the whole audit list for any owner, admin or break-glass session with no actor, organization or team filter (`audit/route.ts` lines 8-16, `control-plane-events.ts` lines 167-170). Reusing it would turn a same-workspace oversight rule into store-wide oversight.

Open choice OC-1 for the operator: whether break-glass may read transfer records under a separate approved procedure. The default in this contract is DENY.

## 6. Packet Reference And Version Identity

SC-REQ-14 Every send names one packet identity: packetRef, packetVersion and an evidence list. The server classifies the identity; only the first class below may be recorded as a send, every other class is refused.

| Class | Meaning | Admission |
|---|---|---|
| PK-VERIFIED | Reference resolves through a trusted resolver, the version exists, and a server-observed digest matches a pinned digest | Admissible (needs G-PACKET) |
| PK-UNVERIFIED | A reference and version are named but no resolver or verifier confirmed them | Refused (SC-RF-17) |
| PK-MUTABLE | The reference points at something editable, such as the form text or an audit-derived draft | Refused (SC-RF-17) |
| PK-NONEXISTENT | The reference does not resolve | Refused (SC-RF-16) |
| PK-MISSING | No reference supplied | Refused (SC-RF-15) |
| PK-VERSION-MISMATCH | Named version differs from what the resolver reports | Refused (SC-RF-18) |

SC-REQ-16 No provenance from existing anchors. Neither a source hash nor an editable draft anchor is immutable provenance. The current export draft is built from seven record fields, drops event type and payload, and every field is editable (`page.tsx` lines 100-120); its `receiptAnchor` is the string `transfer-` plus the row id. The page copy already labels it an editable draft that is not proof of a completed transfer. A hash that was computed from submitted bytes proves only that those bytes hash to that value, not that the packet existed before the send or was not changed afterwards.

Comparison with the handoff invariant. The ratified handoff index states that a delegated item is complete only when its declared artifact exists with a non-empty content hash, the recorded writer matches the assigned write owner, and a named assembly verifier verified it, and that a worker may not promote its own notification into that claim (`docs/reference/agent_handoff/README.md` Artifact Completion Evidence). Mapped to a send: the sender's request is the notification; the recorded send is complete only after a distinct verifier checks it. That index is a governance principle with an offline contract; it is not a Web store or a page producer.

Current state today: no packet resolver, packet version registry or pinned-digest source exists in the inspected graph, so every send would currently classify as PK-UNVERIFIED or PK-MUTABLE and be refused. This is the intended fail-closed outcome, not a defect of the contract. Open choice OC-2: whether the operator later accepts a send of an unverified packet that is permanently labelled unverified; the default is refuse.

## 7. Existing Owner Comparison

| Owner | Responsibility today | Mandatory call path today | Failure boundary today | Adaptable for send | Needs separately authorized change |
|---|---|---|---|---|---|
| Work Transfer page and validator | Local context check and an admin audit consumer with an editable export draft | Page computes the check client-side; one GET to the audit route | Check failure shows an issue; fetch failure shows an error state | Page can host a confirm action and a scoped list | A new server producer call; relabel of history |
| Enterprise access | Role names and an owner or admin predicate | Called by admin session admission | Unknown role returns no access | Admin predicate is a candidate half of the read rule | A workspace-scoped admin binding |
| Admin session | Session admission for admin routes, break-glass branch, denial event | Per admin route call | Denied callers get 401 or 403 and a denial event is appended | Session derivation pattern | Break-glass exclusion; non-admin sender admission |
| Audit route and control-plane events | Append and read audit rows | POST accepts body-supplied actor; GET returns all audit rows | Append rejects on store error; SIEM forward is fire-and-forget (`control-plane-events.ts` lines 151-153) | Possible side evidence emitter | Typed scope, server-derived actor, record-level read |
| Storage adapter | List and key-value persistence by environment | Chosen at module load | File adapter appends by read, push, write and reports atomicAppend false (`storage-adapter.ts` lines 144-148 and 159-169); SQLite reports atomic local; Redis applies retention (lines 441-470) | Nothing automatic | A store selection with atomic conditional insert, scoped read, retention and recovery (G-STORE) |
| Handoff completion contract | Principle: artifact, writer and verifier distinct | Governance only | Not a runtime | The producer, verifier, consumer split | A runtime verifier, if the operator wants one |

Findings that shape the contract:

- The store adapter by itself proves no scope, no transactional send and no provenance. The event list has no query by key and no conditional insert.
- The retention constant is thirty days and applies to the Redis adapter; the file adapter reports no retention. An audit row therefore cannot stand as a durable send record.
- The store key is a single list shared by every event kind.

SC-REQ-17 Adaptation boundary. The contract adapts the existing owners only as listed in the Adaptable column. Any change in the last column is a separately authorized owner change. No new store, schema, backend or adapter is selected here. Candidate shapes, none selected: A extend the existing event list with a typed send kind plus scope fields; B a sibling store; C a path under the handoff artifact principle. Each needs its own admission (open choice OC-3).

### Proposed joins and manifest (proposals only)

- Producer: a send route that derives sender and workspace from the session and accepts only submitted claims (proposed, not existing).
- Verifier: a distinct step that checks binding, recipient membership, packet class, duplicate state and read-after-write existence before the record is called recorded (proposed, not existing).
- Consumer: a scoped read route plus the Work Transfer page history, replacing store-wide admin audit as the transfer view (proposed, not existing).
- Future manifest, each item subject to its own gate: the producer route; the verifier; the membership and workspace resolver; the packet resolver; the scoped store behavior; the page confirm action and list; a test suite built from the case plan in the evidence JSON.

## 8. Idempotency, Duplicate, Conflict, Failure And Unknown Outcome

SC-REQ-18 Logical duplicate rule. Define dedupeKey as senderRef, workspaceRef, recipientRef, packetRef and packetVersion taken together. A second request with the same requestId and the same dedupeKey returns the existing record and creates none (idempotent replay). A request with the same dedupeKey and a different requestId is refused as a duplicate (SC-RF-19) with a pointer to the existing record; it is not a second send. The same packet version to a different recipient is refused as a recipient conflict (SC-RF-20) until the operator decides multi-recipient (open choice OC-4). A different version to the same recipient is a separate send; no automatic supersession is claimed.

The existing adapters cannot enforce this rule. The file adapter appends unconditionally (`storage-adapter.ts` lines 144-148) and the event identifier may be caller-supplied (`control-plane-events.ts` lines 120-124). A uniqueness guarantee needs a conditional insert that is UNKNOWN today (G-IDEMP). No durable guarantee is claimed.

SC-REQ-19 Failure classes.

| Class | Condition | Outcome | Retry |
|---|---|---|---|
| Admission failure | Session, binding, recipient or workspace check fails | REFUSED with a code | New request after the cause is fixed |
| Validation failure | Packet class not PK-VERIFIED, confirmation absent, context check BLOCK | REFUSED with a code (SC-RF-21 for a context BLOCK) | New request |
| Definite persistence failure | The store reported failure and a read-only check shows no record | REFUSED (SC-RF-27) | New request |
| Unknown outcome | Timeout, lost response or ambiguous store result | SEND_UNKNOWN_OUTCOME | No blind retry |

Reconciliation is read-only: the sender looks up the record by requestId and dedupeKey within the sender's own scope. The result is one of three classes: RECONCILED_RECORDED, RECONCILED_NOT_RECORDED, RECONCILE_INDETERMINATE. A retry is allowed only after RECONCILED_NOT_RECORDED and only with the same requestId; under RECONCILE_INDETERMINATE nothing is retried and no send is reported. Reconciliation never creates, edits or deletes a record. No witness, OS lock or backup mechanism is proposed.

SC-REQ-20 Recorded-send acknowledgment gate. Reporting a send to a user as recorded requires verifier evidence that the record exists after the write (read-after-write by the verifier, not the producer's success status). Existing evidence cannot justify this today: the file adapter's append can fail after reading and its reported capability disclaims distributed durability, and the SIEM forward is not awaited. The named future gates are G-STORE, G-IDEMP and G-VERIFY. Until separate proof exists, no design, report or UI may state that a real send or a durable record exists.

## 9. State Machine

| State | Meaning | Is a record |
|---|---|---|
| SC-ST-01 DRAFT | Client-local intent | No |
| SC-ST-02 SUBMITTED | Server received an untrusted request | No |
| SC-ST-03 REFUSED | Terminal refusal with a code | No; a denial audit event is not a send |
| SC-ST-04 SEND_RECORDED | Verified recorded send | Yes, the only one |
| SC-ST-05 SEND_UNKNOWN_OUTCOME | Outcome cannot be told | No claim |
| SC-ST-06 RECONCILED_RECORDED | Read-only check found the record | Same as SC-ST-04 |
| SC-ST-07 RECONCILED_NOT_RECORDED | Read-only check found none | No |
| SC-ST-08 RECONCILE_INDETERMINATE | Read-only check could not decide | No claim |
| SC-OOS-01 RECIPIENT_ACKNOWLEDGED | Not defined by this contract | Out of scope |
| SC-OOS-02 ARTIFACT_ACCEPTED | Not defined by this contract | Out of scope |

| Transition | From | To | Condition |
|---|---|---|---|
| SC-TR-01 | SC-ST-01 | SC-ST-02 | Explicit confirmation act (SC-REQ-05) |
| SC-TR-02 | SC-ST-02 | SC-ST-03 | Any refusal in section 10 |
| SC-TR-03 | SC-ST-02 | SC-ST-04 | All checks pass and verifier confirms existence |
| SC-TR-04 | SC-ST-02 | SC-ST-05 | Outcome ambiguous |
| SC-TR-05 | SC-ST-05 | SC-ST-06 | Read-only lookup finds the record |
| SC-TR-06 | SC-ST-05 | SC-ST-07 | Read-only lookup definitively finds none |
| SC-TR-07 | SC-ST-05 | SC-ST-08 | Lookup cannot decide |
| SC-TR-08 | SC-ST-03 | SC-ST-01 | The user edits and starts over; a new request is a new SC-ST-02 |
| SC-TR-09 | SC-ST-07 | SC-ST-02 | Retry with the same requestId |

Forbidden transitions: SC-ST-01 straight to SC-ST-04; any state to SC-OOS-01 or SC-OOS-02 by inference; SC-ST-04 back to any earlier state or to deletion in this contract; SC-ST-08 to a retry.

## 10. Refusal Catalog

Every refusal is a fail-closed decision with a code. A refused request is not a send. A denial audit event may be written for a refusal; it is not a send record.

| Code | Name | Trigger |
|---|---|---|
| SC-RF-01 | NO_SESSION | No authenticated session |
| SC-RF-02 | SESSION_INVALID_OR_EXPIRED | Session fails verification or is expired |
| SC-RF-03 | SENDER_BINDING_MISSING | No sender binding resolved |
| SC-RF-04 | SENDER_BINDING_FALLBACK_DEFAULT | Binding is the unknown-user or default org and team fallback |
| SC-RF-05 | SENDER_BINDING_REVOKED_OR_INACTIVE | Sender membership revoked or inactive |
| SC-RF-06 | WORKSPACE_UNBOUND | Sender has no verified workspace |
| SC-RF-07 | RECIPIENT_UNRESOLVED_OR_FOREIGN | Recipient unknown, inactive or in another workspace; one uniform response |
| SC-RF-08 | RECIPIENT_IS_SENDER | Recipient equals sender (default refuse; OC-5) |
| SC-RF-09 | CALLER_AUTHORITY_MISMATCH | Submitted actor, role or workspace differs from server-derived value |
| SC-RF-10 | IMPERSONATED_SESSION | Session carries an impersonation |
| SC-RF-11 | DELEGATED_SEND | On-behalf-of or delegated confirmation |
| SC-RF-12 | SERVICE_OR_INTERNAL_CALLER | Internal-secret or service token call |
| SC-RF-13 | BREAK_GLASS_SEND | Break-glass session attempts to send |
| SC-RF-14 | CONFIRMATION_ABSENT | No explicit, bound confirmation |
| SC-RF-15 | PACKET_REF_MISSING | PK-MISSING |
| SC-RF-16 | PACKET_REF_NONEXISTENT | PK-NONEXISTENT |
| SC-RF-17 | PACKET_UNVERIFIED_OR_MUTABLE | PK-UNVERIFIED or PK-MUTABLE |
| SC-RF-18 | PACKET_VERSION_MISMATCH | PK-VERSION-MISMATCH |
| SC-RF-19 | DUPLICATE_DIFFERENT_REQUEST | Same dedupeKey, different requestId |
| SC-RF-20 | CONFLICT_RECIPIENT | Same packet version already sent to another recipient |
| SC-RF-21 | CONTEXT_CHECK_BLOCK | The workflow context check returned BLOCK |
| SC-RF-22 | READ_UNAUTHENTICATED | Read without a session |
| SC-RF-23 | READ_NON_PARTY_SAME_WORKSPACE | Same-workspace principal who is neither party nor admin |
| SC-RF-24 | READ_ADMIN_FOREIGN_WORKSPACE | Owner or admin of another workspace |
| SC-RF-25 | READ_RECORD_SCOPE_MISSING | Record has no verified workspaceRef |
| SC-RF-26 | READ_BREAK_GLASS_DEFAULT_DENY | Break-glass read (default; OC-1) |
| SC-RF-27 | PERSISTENCE_FAILED_DEFINITE | Store failed and a read-only check shows no record |

## 11. Unknowns, Future Gates And Open Choices

| Gate | What it must prove before any send is claimed |
|---|---|
| G-BIND | Account to person, workspace definition, membership resolution and per-workspace admin binding, using real bindings chosen by the operator |
| G-PACKET | A resolver and version registry that can classify a packet as PK-VERIFIED with a pinned digest |
| G-STORE | A store, chosen with separate authorization, that offers atomic conditional insert, record-level scoped read, retention, backup and recovery; its cost and custody are UNKNOWN |
| G-IDEMP | The dedupe rule of section 8 holds under concurrent requests |
| G-VERIFY | A verifier distinct from the producer confirms existence after the write |
| G-CASE | The case plan in the evidence JSON is turned into executed tests; all are NOT_EXECUTED_PLANNED now |
| G-OPERATOR | Any real data, account, pilot, provider call, public sync or deployment needs explicit operator action |

Open choices (default stated): OC-1 break-glass read, default deny; OC-2 unverified-packet send, default refuse; OC-3 physical owner shape A, B or C, none selected; OC-4 multi-recipient, default one recipient per packet version; OC-5 self-send, default refuse.

SC-REQ-21 B2 boundary and unknowns. If any gate above would depend on the stopped B2 acceptance, witness or restore problem, that dependency must be disclosed and work must stop for architecture reassessment; it must not be renamed as transfer work. Real bindings, backend, retention, backup, custody, cost and recovery remain UNKNOWN.

## 12. Coverage Statement

Each SC-REQ, SC-RF, SC-ST and SC-TR identifier in this document is mapped to at least one planned case in the evidence JSON, and every planned case names an existing identifier. Every case is NOT_EXECUTED_PLANNED. The cross-check is a static document and evidence comparison, `PASS_STATIC_ONLY`; it is not behavioral proof of send, access or provenance.

## Claim Boundary

Design proposal for Local review. No real send, recipient acknowledgment, artifact acceptance, durable record, real identity, workspace or membership binding, backend, store, cost or recovery claim. No runtime, HTTP, browser, database or provider execution. Q001 and Q004 stay open; B2 stays STOP; P11, effects, public sync and deployment stay parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Local Review Qualification

Controlling Local review: `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_COMPLETION_2026-10-02.md`. DESIGN_NOT_RATIFIED; accepted bounded only as proposal/source/static-coverage evidence. No implementation readiness, business send, read-authority or detailed policy approval.

- D01 Retry/finality gap: one lookup finding no row does not prove an earlier request cannot commit later, nor that the read is authoritative/fresh. SC-CASE-050/SC-TR-06/09 do not justify retry as written. Future design must establish terminal no-late-write/no-record evidence or remain INDETERMINATE. No witness/store mechanism is selected and no B2 dependency may be hidden.
- D02 Request/conflict binding gap: reuse of the same requestId with a different logical request/dedupeKey has no refusal rule or case. Request identity/fingerprint and conflict namespace (sender/workspace versus global packet restriction) must be explicit before implementation; do not infer idempotency from the current map.
- D03 False-denial gap: verified identity/membership may legitimately equal org_cvf/team_eng. Reject fallback-origin/unverified binding, not equality to a default-looking identifier. SC-RF-04/SC-CASE-029 currently conflate provenance and value; require positive verified-value collision coverage later.
- D04 Seal/provenance qualification: sealed plan proposed refusal range SC-RF-01..23; draft contains 27 refusals. This is a disclosed post-seal expansion, not a rewritten seal. The 14 source hashes and 32 locator substrings match, and 62 planned case IDs reconcile; that does not certify semantic coverage. Original seal.json bytes/canonical byte recipe and scanner source are not tracked, so their execution/chronology/seal digest is worker-reported, not independently reproduced by Local.

OC-1/2/5 deny/refuse defaults remain recommendations only. OC-3 physical owner is unselected. OC-4 one recipient per packet version is more restrictive than the operator-selected one recipient per send; no cross-send restriction ratified. Local recommends one recipient per logical send and explicit scoped conflict semantics, subject to the later consolidated contract disposition. No operator choice is required to record this review; detailed choices must precede implementation. All 62 cases remain NOT_EXECUTED_PLANNED. Source absence/existence statements apply only to the inspected graph, not all repository/runtime data. Original preAuthoringSeal and case ledger remain intact; this qualification overrides readiness/complete-design claims.
