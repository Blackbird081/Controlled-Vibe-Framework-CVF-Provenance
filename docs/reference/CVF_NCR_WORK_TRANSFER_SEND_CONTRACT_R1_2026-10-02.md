# CVF NCR Work Transfer Send Contract R1

Memory class: POINTER_RECORD

Status: DESIGN_PROPOSAL_PENDING_REVIEW

docType: reference

Date: 2026-10-02

## Purpose

Integrated same-root repair of the unratified send-contract proposal. It addresses all four findings D01 to D04 of the controlling review `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_COMPLETION_2026-10-02.md` together and clarifies the open choices OC-1 to OC-5. It is a logical design only. Every field, state, refusal code, obligation and gate is a proposal for Local review. Nothing was executed, imported, requested or changed. No send exists; this contract does not create one, and executing the order that produced it does not approve any detailed policy. The original proposal `docs/reference/CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_2026-10-02.md`, its evidence and its 62 planned cases stay immutable historical inputs.

## Scope / Applies To

Applies to the send action only: sender confirmation, sender, recipient and workspace binding with provenance, packet identity, scoped request identity, same-workspace read policy, failure and outcome finality, existing-owner comparison and future gates. Out of scope and not defined: recipient acknowledgment, artifact acceptance, storage selection, schema or migration, route or UI work, real accounts, workspaces, membership, admin binding, backup, retention, custody, cost and recovery (all UNKNOWN). rawMemoryReleased=false: no memory, runtime store, `.env`, credential or Downloads content was read.

Independence: not a B2 successor. B2 stays STOP_REASSESS_ARCHITECTURE/NO_SUCCESSOR. No witness, OS lock, restore, acceptance store or renamed successor is proposed (R1-REQ-24).

Source basis: clean released base `d404542690b84ec623ef909e32a2f2f4afba2368`. Named source hashes were refreshed; of the 14 original sealed sources only the roadmap changed (its D083 and D084 entries), the 13 others are byte-identical, so the original locators still hold. The source graph remains the accepted partial graph; no producer rescan and no repository-wide absence claim.

## 1. Stage Model And Non-Equivalence

| Stage | Meaning | Is it a send? |
|---|---|---|
| S0 Draft or intent | Client-local form values or an editable export draft | No |
| S1 Submitted request | Server received untrusted claims; an attempt may be in flight | No |
| S2 Recorded send | Verified binding, packet, identity and a distinct verifier confirmed existence | Yes, the only business send |
| S3 Recipient acknowledgment | Recipient confirms receipt | Not defined here |
| S4 Artifact acceptance | Artifact accepted as the work product | Not defined here |

R1-REQ-01 One send action. A send is one authenticated sender's explicit confirmation of one packet identity to one designated recipient in one workspace. One logical request produces at most one recorded send.

R1-REQ-02 Stage separation. Draft, submitted request, recorded send, recipient acknowledgment and artifact acceptance are distinct stages with distinct evidence. This contract defines S0 to S2 only.

R1-REQ-03 Non-equivalence. A validator ALLOW or WARN, an audit event, an admin-seeded row, an HTTP success status or a history row is never the send by itself. Source basis: the validator checks supplied values (`agent-handoff-validator.ts` line 209); the page says checking creates no record (`page.tsx` line 39); the audit POST takes actor from the body (`audit/route.ts` line 32).

R1-REQ-04 No inferred downstream stage. No acknowledgment, acceptance or delivery is inferred from a recorded send or from anyone reading it.

R1-REQ-05 Explicit confirmation. A send needs a per-packet, per-recipient confirmation act bound to the sender's session, the packet identity and the recipient, carried in the same request. Defaults, auto-fill, batch confirmation, replayed or foreign-session confirmations are refused (R1-RF-14).

## 2. Logical Send Record

Names are logical. They are not a schema, migration or storage layout; no physical path is selected.

| Logical field | Origin | Trust |
|---|---|---|
| sendId, recordedAt | server | trusted; caller values ignored |
| senderRef, workspaceRef | server-derived from a verified binding | trusted only with verified provenance (section 3) |
| recipientRef | submitted, then verified inside the workspace | trusted after verification |
| packetRef, packetVersion, packetEvidence | submitted, then classified (section 5) | trusted only as classified |
| confirmation | submitted act | untrusted until bound to the session |
| requestId | submitted | untrusted; one half of the scoped key (section 6) |
| requestFingerprint | server-computed | trusted; immutable once stored |
| stage, contractVersion | server | trusted |

R1-REQ-15 Trusted versus submitted. Only server-derived values and server observations are authority. Where a submitted claim disagrees with a server-derived value the request is refused (R1-RF-09), not silently corrected.

## 3. Identity, Binding And Provenance

R1-REQ-06 Sender is server-derived from the authenticated session, never from the body (`middleware-auth.ts` lines 20-30; contrast `audit/route.ts` lines 32-33).

R1-REQ-07 Recipient is verified inside the workspace through a membership resolver (UNKNOWN, gate G-BIND). A nonexistent recipient and a foreign-workspace recipient get the same refusal (R1-RF-07) so there is no enumeration oracle.

R1-REQ-08 Workspace is bound at record level. A record without a verified workspace reference is unreadable to every principal (R1-RF-25). The audit event type has no org, team or workspace field (`control-plane-events.ts` line 33) while the cost event does (line 46).

R1-REQ-09 Caller-supplied actor, role, organization, team, workspace or admin flags are never authority, including the internal-secret header path (`audit/route.ts` line 19).

R1-REQ-10 Workflow role is not enterprise permission. AgentRole values (`agent-handoff-validator.ts` line 53) describe workflow steps, TeamRole values (`enterprise-access.ts` line 3) are access roles; the word reviewer is in both and means two things. Neither grants the other's authority; a workflow role never grants send or read.

R1-REQ-13 Special callers. Impersonated sessions (`middleware-auth.ts` line 166), delegated sends, service or internal callers and break-glass sessions (`admin-session.ts` line 13) cannot send (R1-RF-10 to R1-RF-13).

R1-REQ-20 Binding provenance, not spelling (repairs D03). A binding is admissible only if its provenance is VERIFIED: it was resolved by the trusted verified-identity source, not substituted by a client-only or token fallback. The decision depends on provenance, never on the string value.

| Case | Decision |
|---|---|
| Verified source returns org_cvf and team_eng | Admissible; a default-looking value is legitimate when verified |
| Fallback or unverified source yields the same strings | Refused (R1-RF-04) |
| Same strings from a verified source but the verified identity contract marks the user value unknown-user as a sentinel | Refused only if that contract says so; otherwise UNKNOWN, decided at G-BIND |
| Missing, empty or malformed field | Refused (R1-RF-03) |
| Revoked or inactive membership | Refused (R1-RF-05) |
| No verified workspace | Refused (R1-RF-06) |

Source observation that motivates this: in the session code the production binding is looked up only outside development and test; in those two modes it is null and the token or the literal fallbacks (`unknown-user`, developer, `org_cvf`, `team_eng`) are used (`middleware-auth.ts` lines 97-109 and 117-129). So every development or test session has unverified provenance under this rule. Any future test therefore needs a verified-binding test double; that need is recorded as an UNKNOWN gate (G-BIND, G-CASE), not solved here. Whether production binding is complete is UNKNOWN.

| Status item | State |
|---|---|
| Account to person mapping, workspace definition, membership, per-workspace admin binding, real store | UNKNOWN; the session has orgId and teamId and no workspace field, so workspaceRef stays opaque |

## 4. Read Policy

R1-REQ-11 A principal may read a recorded send only if: authenticated by a real session; the binding provenance is VERIFIED; the record has a verified workspace reference equal to the principal's verified workspace; and the principal is the sender, the designated recipient or an authorized owner or admin of that same workspace.

R1-REQ-12 No cross-workspace administrator inheritance, no arbitrary recipient lookup, no break-glass inheritance. Missing identity, provenance or scope fails closed.

| Principal | Same verified workspace | Decision | Refusal |
|---|---|---|---|
| Sender | yes | ALLOW | none |
| Designated recipient | yes | ALLOW; reading is not acknowledgment | none |
| Owner or admin, verified provenance | yes | ALLOW, oversight read | none |
| Owner or admin, unverified provenance | yes | DENY | R1-RF-28 |
| Owner or admin | no | DENY | R1-RF-24 |
| Other role, neither party nor admin | yes | DENY | R1-RF-23 |
| Unauthenticated | not applicable | DENY | R1-RF-22 |
| Record without verified workspace | not applicable | DENY | R1-RF-25 |
| Break-glass | not applicable | DENY by default | R1-RF-26 |
| Service or internal-secret caller | not applicable | DENY | R1-RF-12 |

The existing admin audit read returns the whole audit list for owner, admin or break-glass with no scope filter (`audit/route.ts` line 8) and must not be reused as the transfer read.

## 5. Packet Reference And Version Identity

R1-REQ-14 Every send names one packet identity (reference, version, evidence list). Only PK-VERIFIED may be recorded: resolver confirms the reference and version and a server-observed digest matches a pinned digest. PK-UNVERIFIED and PK-MUTABLE are refused (R1-RF-17), PK-NONEXISTENT (R1-RF-16), PK-MISSING (R1-RF-15), PK-VERSION-MISMATCH (R1-RF-18).

R1-REQ-16 No immutable provenance from existing anchors. A source hash or the editable export draft anchor (`page.tsx` line 118) is not immutable provenance; a hash of submitted bytes proves only those bytes hash to that value. The handoff index's artifact, writer and verifier invariant (`docs/reference/agent_handoff/README.md` line 67) is a principle with an offline contract, not a Web store. No resolver or version registry exists in the inspected graph, so today every send would classify PK-UNVERIFIED or PK-MUTABLE and be refused; that is the intended fail-closed outcome.

## 6. Scoped Request Identity (repairs D02)

R1-REQ-18 Scoped key and fingerprint.

- Key namespace: the trusted pair (workspaceRef, senderRef) from a verified binding. Scoped key = namespace plus the submitted requestId. A requestId is meaningful only inside its namespace; the same requestId from another sender or in another workspace is a different, independent key and reveals nothing about the first.
- Logical request fingerprint: computed by the server at first admission from a canonical form of the logical fields only: verified recipientRef, packetRef, packetVersion, the packet digest as classified, and the normalized evidence pointer set (sorted, duplicates removed). Equality means byte equality of that canonical form. Once stored it is immutable; later edits to labels or drafts never change it.
- Excluded from the fingerprint and from equality: transport timestamps, client clock, retry counters, header order, language, evidence pointer ordering, and the requestId itself.
- No physical hash algorithm, schema or backend is selected.

R1-REQ-19 Reuse and conflict scope.

| Situation under the scoped key | Outcome |
|---|---|
| Same key, same fingerprint | Idempotent replay: return the existing attempt outcome; never a second send |
| Same key, different packet version, recipient, packet or evidence set | Refused, KEY_REUSED_WITH_CHANGED_REQUEST (R1-RF-19); never duplicate success |
| Same requestId, different sender or different verified workspace | Different key; independent |
| Different requestId, same packet version, different recipient | Independent logical send evaluated on its own bindings and permissions; no global per-packet-version recipient ban |
| Different requestId, identical fingerprint | Independent logical send in this contract; an advisory duplicate warning is an unresolved owner choice (U-3), not a refusal |
| Same fingerprint with an unresolved earlier attempt in the sender's scope | Refused, PRIOR_ATTEMPT_UNRESOLVED (R1-RF-20); a different recipient is not blocked |
| Batch or multi-recipient request | Refused; one recipient per logical send (OC-4) |

Concurrent replays of one key must yield exactly one attempt, and concurrent different requests under one key must yield exactly one winner. That needs an atomic conditional insert on the scoped key, which the inspected adapters do not provide (the file adapter appends unconditionally, `storage-adapter.ts` line 144; the caller may supply the event id, `control-plane-events.ts` line 122). This is a future obligation (gate G-IDEMP), UNKNOWN today; no guarantee is claimed.

## 7. Existing Owner Comparison

| Owner | Responsibility today | Mandatory call path | Failure boundary | Adaptable | Separately authorized change |
|---|---|---|---|---|---|
| Work Transfer page and validator | Local context check, admin audit consumer, editable draft | client-side check; one GET (`page.tsx` line 147) | issue list; error state | host confirm action and scoped list | server producer call; history relabel |
| Enterprise access | role names and owner or admin predicate (`enterprise-access.ts` line 11) | called by admin session | unknown role gets no access | predicate as half of read rule | workspace-scoped admin binding |
| Admin session | admin admission, break-glass branch, denial event (line 245) | per admin route | 401, 403 plus denial event | session derivation pattern | break-glass exclusion; non-admin sender admission |
| Audit route and control-plane events | append and read audit rows | POST takes body actor; GET returns all audit rows | append rejects on store error; SIEM forward not awaited (line 151) | possible side-evidence emitter | typed scope, server actor, record-level read |
| Storage adapter | list and key-value persistence | chosen by environment | file append is read, push, write and reports non-atomic (line 165); sqlite reports atomic local append (line 330); thirty-day retention constant (line 62) | nothing automatic | store with conditional insert, scoped read, terminal evidence, retention, recovery |
| Handoff completion contract | principle: artifact, writer, verifier distinct | governance only | not a runtime | producer, verifier, consumer split | runtime verifier if wanted |

R1-REQ-17 Adaptation boundary. Only the Adaptable column is adaptable here; everything in the last column is a separately authorized owner change. No store, schema, backend or adapter is selected.

Proposed joins and manifest (proposals only, none existing): producer send route that derives sender and workspace from a verified binding; verifier distinct from the producer that checks binding provenance, recipient, packet class, scoped key and fingerprint and the finality obligations of section 8; consumer scoped read route plus page history. Future manifest: producer route; verifier; membership and workspace resolver; packet resolver; scoped store behavior; page confirm action and list; a test set built from the planned cases with a verified-binding test double.

## 8. Failure, Unknown Outcome And Finality (repairs D01)

R1-REQ-21 Failure classes.

| Class | Condition | Outcome |
|---|---|---|
| Admission or validation failure | binding, recipient, packet, confirmation or context check fails | REFUSED with a code; nothing was started |
| Persistence failure with terminal evidence | store reported failure and obligations E1 to E5 hold | REFUSED, PERSISTENCE_FAILED_TERMINAL (R1-RF-27) |
| Persistence failure without terminal evidence, timeout, lost response | ambiguous | OUTCOME_UNKNOWN; no blind retry |

R1-REQ-22 A missing lookup row never establishes that no send was recorded. The row may be absent because the attempt is still in flight, because the read is stale or from an untrusted source, or because a late commit has not landed. Outcome classes: in flight (stays submitted), stale or untrusted read, unknown outcome, recorded outcome, and an authoritative terminal no-record result. The last needs all logical evidence obligations:

| Obligation | Meaning |
|---|---|
| E1 Writer terminality | The attempt for this identity is known finished or abandoned and cannot commit later (no late write) |
| E2 Freshness | The read reflects a consistent point at or after the writer's terminal point, not a stale replica or cache |
| E3 Matching identity | The lookup used the full scoped key and the request fingerprint, not a partial match |
| E4 Authority | The result comes from the authoritative verifier or store authority, not from the client or a caller claim |
| E5 Scope | The lookup ran inside the sender's verified scope under a verified binding |

If any obligation is absent the classification is INDETERMINATE. Under INDETERMINATE there is no automatic retry and no new request for the same fingerprint (R1-RF-20). Replay under the same key after a terminal no-record result is allowed only under a separately specified atomic idempotency guarantee (G-IDEMP), never inferred from absence; without it a fresh submission is a new attempt with a new requestId.

R1-REQ-23 Recorded-send acknowledgment gate. Reporting a send as recorded needs distinct verifier evidence that the record exists, read fresh and authoritatively (E2 to E5). A producer success status is not enough, and the names G-IDEMP, G-VERIFY and a read-after-write check do not prove protection against races, stale reads or a late commit. No design, report or UI may state that a real send or durable record exists until separate proof exists.

Finality gate status. The mechanism that could supply E1 and E2 (writer fencing or a no-late-write guarantee, a fresh authoritative read) is not provided by any inspected owner, and a witness, OS lock or restore step is exactly the stopped B2 problem. No independent non-B2 proof is available, so gate G-TERMINAL is NOT_ADMITTED and implementation stays blocked. No mechanism is synthesized here.

## 9. State Machine

| State | Meaning | Is a record |
|---|---|---|
| R1-ST-01 DRAFT | client-local intent | No |
| R1-ST-02 SUBMITTED | request received, attempt may be in flight | No |
| R1-ST-03 REFUSED | terminal refusal with a code | No |
| R1-ST-04 SEND_RECORDED | verified recorded send | Yes, the only one |
| R1-ST-05 OUTCOME_UNKNOWN | outcome cannot be told | No claim |
| R1-ST-06 RECONCILED_RECORDED | fresh authoritative lookup matched the record | Same as R1-ST-04 |
| R1-ST-07 RECONCILED_NO_RECORD_TERMINAL | all of E1 to E5 hold and no record exists | No |
| R1-ST-08 INDETERMINATE | any obligation absent, including a missing row alone | No claim |
| R1-OOS-01 RECIPIENT_ACKNOWLEDGED | not defined here | out of scope |
| R1-OOS-02 ARTIFACT_ACCEPTED | not defined here | out of scope |

| Transition | From | To | Condition |
|---|---|---|---|
| R1-TR-01 | R1-ST-01 | R1-ST-02 | explicit confirmation (R1-REQ-05) |
| R1-TR-02 | R1-ST-02 | R1-ST-03 | any refusal in section 10 |
| R1-TR-03 | R1-ST-02 | R1-ST-04 | all checks pass and verifier confirms existence |
| R1-TR-04 | R1-ST-02 | R1-ST-05 | outcome ambiguous |
| R1-TR-05 | R1-ST-05 | R1-ST-06 | fresh authoritative matching lookup finds the record |
| R1-TR-06 | R1-ST-05 | R1-ST-07 | E1 to E5 all satisfied and no record |
| R1-TR-07 | R1-ST-05 | R1-ST-08 | any of E1 to E5 absent, or a missing row alone |
| R1-TR-08 | R1-ST-03 | R1-ST-01 | user edits and starts over |
| R1-TR-09 | R1-ST-07 | R1-ST-02 | new attempt with a fresh requestId; same-key replay only under a future atomic guarantee |
| R1-TR-10 | R1-ST-08 | R1-ST-06 | later fresh authoritative evidence finds the record |
| R1-TR-11 | R1-ST-08 | R1-ST-07 | later all of E1 to E5 satisfied |

Forbidden: R1-ST-01 straight to R1-ST-04; R1-ST-05 to R1-ST-07 by absence alone; R1-ST-08 to R1-ST-02 automatically; R1-ST-04 to any earlier state; any state to R1-OOS-01 or R1-OOS-02 by inference.

## 10. Refusal Catalog

A refusal is a fail-closed decision with a code and is not a send. A denial audit event may be written; it is not a send record.

| Code | Name | Trigger |
|---|---|---|
| R1-RF-01 | NO_SESSION | no authenticated session |
| R1-RF-02 | SESSION_INVALID_OR_EXPIRED | session fails verification or expired |
| R1-RF-03 | BINDING_MISSING_OR_MALFORMED | missing, empty or malformed binding field |
| R1-RF-04 | BINDING_PROVENANCE_UNVERIFIED | binding from fallback, client-only or unverified source, whatever its values |
| R1-RF-05 | BINDING_REVOKED_OR_INACTIVE | membership revoked or inactive |
| R1-RF-06 | WORKSPACE_UNBOUND | no verified workspace |
| R1-RF-07 | RECIPIENT_UNRESOLVED_OR_FOREIGN | unknown, inactive or foreign recipient; one uniform response |
| R1-RF-08 | RECIPIENT_IS_SENDER | recipient equals sender (OC-5) |
| R1-RF-09 | CALLER_AUTHORITY_MISMATCH | submitted actor, role or workspace differs from server value |
| R1-RF-10 | IMPERSONATED_SESSION | impersonation present |
| R1-RF-11 | DELEGATED_SEND | on-behalf-of confirmation |
| R1-RF-12 | SERVICE_OR_INTERNAL_CALLER | internal-secret or service call |
| R1-RF-13 | BREAK_GLASS_SEND | break-glass attempts to send |
| R1-RF-14 | CONFIRMATION_ABSENT | no explicit bound confirmation |
| R1-RF-15 | PACKET_REF_MISSING | PK-MISSING |
| R1-RF-16 | PACKET_REF_NONEXISTENT | PK-NONEXISTENT |
| R1-RF-17 | PACKET_UNVERIFIED_OR_MUTABLE | PK-UNVERIFIED or PK-MUTABLE (OC-2) |
| R1-RF-18 | PACKET_VERSION_MISMATCH | version differs from resolver |
| R1-RF-19 | KEY_REUSED_WITH_CHANGED_REQUEST | same scoped key, different fingerprint |
| R1-RF-20 | PRIOR_ATTEMPT_UNRESOLVED | same fingerprint with an unresolved earlier attempt in the sender's scope |
| R1-RF-21 | CONTEXT_CHECK_BLOCK | workflow context check returned BLOCK |
| R1-RF-22 | READ_UNAUTHENTICATED | read without session |
| R1-RF-23 | READ_NON_PARTY_SAME_WORKSPACE | same workspace, neither party nor admin |
| R1-RF-24 | READ_ADMIN_FOREIGN_WORKSPACE | owner or admin of another workspace |
| R1-RF-25 | READ_RECORD_SCOPE_MISSING | record lacks verified workspace |
| R1-RF-26 | READ_BREAK_GLASS_DEFAULT_DENY | break-glass read (OC-1) |
| R1-RF-27 | PERSISTENCE_FAILED_TERMINAL | store failure with E1 to E5 satisfied |
| R1-RF-28 | READ_BINDING_UNVERIFIED | reader provenance unverified |

## 11. Gates

| Gate | Obligation | Status |
|---|---|---|
| G-BIND | real account, person, workspace definition, membership, per-workspace admin binding, verified-provenance source, verified-binding test double | UNKNOWN |
| G-PACKET | resolver and version registry yielding PK-VERIFIED with pinned digest | UNKNOWN |
| G-STORE | store (separate authorization) with conditional insert, scoped read, retention, backup, recovery, cost, custody | UNKNOWN |
| G-IDEMP | scoped-key uniqueness and fingerprint immutability under concurrency | UNKNOWN |
| G-TERMINAL | independent non-B2 proof for E1 to E5 | NOT_ADMITTED; implementation blocked |
| G-VERIFY | verifier distinct from producer with fresh authoritative read | UNKNOWN |
| G-CASE | planned cases turned into executed tests | UNKNOWN; all NOT_EXECUTED_PLANNED now |
| G-OPERATOR | real data, accounts, pilot, provider, public sync, deployment | parked |

Known dependency: any proof for E1 or E2 that needs a witness, OS lock or restore step depends on stopped B2 architecture. It is disclosed here and left NOT_ADMITTED; it is not renamed as transfer work (R1-REQ-24).

R1-REQ-24 B2 boundary and unknowns. If a gate would depend on the stopped B2 problem or on an actual authority or store selection, disclose it and stop for architecture reassessment. Real bindings, backend, retention, backup, custody, cost and recovery remain UNKNOWN.

## 12. Open Choices OC-1 To OC-5 (all unratified)

R1-REQ-25 Status of the choices. OC-1, OC-2 and OC-5 are Local conservative recommendations for design review. OC-3 is a source-backed comparison with no selection. OC-4 states a design cardinality. None is an operator ratification, and executing this order approves none.

| OC | Operator direction | Local recommendation | Unresolved operator or owner gate | Alternative and consequence |
|---|---|---|---|---|
| OC-1 break-glass read | none beyond: same-workspace read, fail closed, no cross-workspace admin inheritance | deny (R1-RF-26) | whether a separate approved emergency read procedure exists | allow under a procedure: widens read to a fixed owner identity tied to one org and team, so scope proof is lost |
| OC-2 unverified-packet send | selected: identify a work artifact and version without fabricating proof; missing evidence fails closed | refuse (R1-RF-17) | whether a permanently labelled unverified send is wanted | allow labelled send: sends could proceed before a resolver exists but carry no provenance |
| OC-3 owner shape | none; existing owners are comparison targets | none selected | operator and owner authorization of any store or schema | A extend the event list: existing adapters, but no scope fields, no conditional insert, shared store key, retention only on Redis. B sibling store: needs new authorization and schema. C handoff artifact principle: offline contract, no Web runtime. No runtime availability is claimed for any |
| OC-4 cardinality | selected: one designated recipient | one recipient per logical send; a different recipient is a distinct send judged independently on its own scoped identity and permission; no batch endpoint; no per-packet-version recipient ban | whether batch or multi-recipient is ever wanted | batch: needs partial-failure and per-recipient identity rules not designed here |
| OC-5 self-send | none | refuse (R1-RF-08) | whether self-send as a save-for-later is wanted | allow: blurs sender and recipient and the read table |

Unresolved owner choice U-3: advisory duplicate warning for identical fingerprints under different requestIds.

## 13. Disposition Of D01 To D04

| Finding | Disposition in R1 |
|---|---|
| D01 finality | sections 8 and 9: missing row is never terminal; obligations E1 to E5; INDETERMINATE default; no automatic retry; G-TERMINAL NOT_ADMITTED |
| D02 request identity | section 6: scoped key, immutable fingerprint, changed-request refusal, per-send conflict scope, concurrency obligation |
| D03 binding fallback | section 3: provenance decides; verified default-looking values admitted, unverified refused |
| D04 evidence | the original contract, evidence, seal and 62 cases are untouched. The original seal planned 23 refusal identifiers and the final document had 27; that post-seal expansion is disclosed, not resealed, and the scratchpad scanner invocation and original chronology are not claimed as reproduced. R1 has its own canonical seal, an original-to-R1 identifier and case map, and an embedded cross-check, all in the R1 evidence JSON |

## 14. Coverage Statement

Every R1 requirement, refusal, state, out-of-scope state and transition identifier is mapped to at least one planned case in the R1 evidence JSON, and every case names an existing identifier. Every case is NOT_EXECUTED_PLANNED. The cross-check is static and is `PASS_STATIC_ONLY`; it is neither semantic acceptance nor behavioral proof of send, access or provenance.

## Claim Boundary

Design proposal for Local review. No real send, acknowledgment, artifact acceptance, durable record, real binding, backend, store, cost or recovery claim; no runtime, HTTP, browser, database or provider execution; no policy ratification. Implementation is NOT_ADMITTED and the root TRANSFER_SEND_IDENTITY_SCOPE_CONTRACT_UNSPECIFIED is not declared resolved. Q001 and Q004 stay open, B2 stays STOP, P11, effects, public sync and deployment stay parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Local Review Qualification

Local accepts bounded documentation repair/source/static reconciliation only, not ratification or implementation. Cases 106 and 117 remain hypothetical positive classification plans with no admitted mechanism. All 100 cases are NOT_EXECUTED_PLANNED. G-BIND/G-CASE remain UNKNOWN; development/test base-session resolver branches skip productionBinding, so under the proposed provenance rule their token/fallback values are unverified. This is a source observation under the proposed rule, not an executed access result or a claim that every possible caller/session path was audited. A future verified-binding test double proves synthetic behavior only and cannot establish actual production membership/binding.

U-3 is an unratified advisory duplicate-warning choice, not a refusal. Different requestId/same fingerprint denotes a distinct logical send subject to the prior-unresolved-attempt rule; no global per-packet recipient restriction is approved. OC-1..5 remain unratified, physical owner/store unselected. No real identity, recipient, workspace, resolver, concurrency, finality or scoped-read behavior is proven.

Seal digest/canonical byte equality and current hashes are reproducible; a timestamp plus hash does not independently attest when the worker authored the payload or contract. Local does not attest pre-authoring chronology. Source absence and owner limitations are restricted to the inspected graph; a general OS lock or witness is not thereby proven to be a B2 mechanism. Any actual stopped-B2 dependency remains barred, and no alternative architecture is selected here.

The root TRANSFER_SEND_IDENTITY_SCOPE_CONTRACT_UNSPECIFIED remains retained. Controlling Local R1 completion review records chain ordinal 2/non-decreasing transition 2, STOP_REASSESS_ARCHITECTURE / NO_SUCCESSOR. No automatic R2, implementation, root rename/reset or fresh execution under this historical packet. This qualification controls the bounded acceptance; D01-D04 documentation repair is not full root closure.
