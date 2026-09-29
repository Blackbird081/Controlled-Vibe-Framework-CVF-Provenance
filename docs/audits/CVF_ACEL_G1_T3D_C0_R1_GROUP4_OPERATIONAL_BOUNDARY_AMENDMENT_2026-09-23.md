# CVF ACEL G1 T3D-C0-R1 Group 4 Operational Boundary Amendment

Memory class: FULL_RECORD

docType: audit

Status: CONTRACT_ACCEPTED_BOUNDED_SOURCE_NOT_CREATED

Date: 2026-09-23

Parent authority: `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`

Authority boundary: responsibility-specific subordinate incorporated by the parent T2F contract; not a duplicate operational-source owner.

## Purpose

Carry the reviewed T3D-C0-R1 Group 4 operational-boundary clauses as a
responsibility-specific subordinate after GC-023 extraction from the T2F root.

## Target / Source

| Source | Binding |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | sole parent/root operational-source owner; incorporates this artifact by reference |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | amendment and reviewer-extraction authority |
| `docs/audits/CVF_ACEL_G1_T3D_C2_SOURCE_CREATION_READINESS_GAP_AUDIT_2026-09-23.md` | three readiness gaps closed at contract level |

## Scope / Methodology

The operational text below is the semantically unchanged amendment reviewed
under the C0-R1 work order. Extraction changes storage responsibility only:
T2F remains the sole root owner, this child carries the bounded Group 4 detail,
and any conflict resolves in favor of T2F outside this amendment's exact scope.

## Findings / Position

The conditional shared-directory design is contract-complete but still
requires separately authorized real-token proof. Cross-target verification,
crash recovery, exact Windows rights, fresh input, issuer observation and
lifecycle ceilings remain fail-closed as specified below.

## Risk / Corrective Action

No tooling or Windows result is inferred. Any failed future proof stops source
authority and requires the split-path or privileged-mediator reassessment
defined by this amendment.

## Decision / Disposition

`CONTRACT_ACCEPTED_BOUNDED_SOURCE_NOT_CREATED`. This subordinate creates no
successor authority and no operational source.

## Claim Boundary

Documentation contract only: no account, credential, ACL, writer execution,
source, observation, response, lookup, consumer binding, provider, public or
deployment effect is claimed.

## T3D-C0-R1 Group 4 Operational Boundary Amendment

This subsection is the controlling operational amendment to G4-GAP-01 through
G4-GAP-04. It does not implement the model or supersede the accepted hermetic
T3D-C1 evidence. Its shared-directory design is
`FEASIBLE_WITH_REQUIRED_WINDOWS_PROOF`: no real source authority exists until
the complete later C1-R2 implementation and the real-token proof below are
independently accepted. If any required Windows proof fails, the system must
stop for a separately reviewed path-layout or privileged-mediator amendment;
it must not widen an ACE, weaken a negative case, silently change paths, or
treat an administrative run as proof of a Party B or Party C token.

##### Protected Parent Directory And Administrative Reservation

The exact protected parent is
`governance/sources/issuer_registry/`. Before Party B or Party C receives any
execution authority, an administrative reservation step must create the
directory and both exact final target names as zero-byte regular-file
placeholders. The step is configuration only; it does not create an accepted
Group 4 source, publish a registry, initialize consumer binding, append an
observation, or perform a lookup.

The directory security candidate is complete and closed:

| Property | Required candidate value |
|---|---|
| owner | `BUILTIN\\Administrators` (`S-1-5-32-544`) |
| inheritance | protected; inherited ACEs removed; child inheritance flags are `None` on every listed ACE |
| `NT AUTHORITY\\SYSTEM` | Allow `FullControl` |
| `BUILTIN\\Administrators` | Allow `FullControl` |
| Party C `S-1-5-21-1644666849-912006174-747199667-1010` | Allow exactly directory `ReadAndExecute`, `CreateFiles`, and `Synchronize` |
| Party B `S-1-5-21-1644666849-912006174-747199667-1009` | Allow exactly directory `ReadAndExecute`, `CreateFiles`, and `Synchronize` |
| Local `S-1-5-21-1644666849-912006174-747199667-1001` | Allow exactly directory `ReadAndExecute` and `Synchronize` for traverse/read verification |
| every other principal | no ACE and no effective access |

For Party B and Party C, the directory DACL explicitly withholds
`CreateDirectories`, `DeleteSubdirectoriesAndFiles` (`DeleteChild`),
directory `Delete`, `ChangePermissions` (`WriteDac`), and `TakeOwnership`
(`WriteOwner`). No generic `Modify`, `Write`, or `FullControl` ACE may be used
as a shorthand for their directory access. Extra allow ACEs, deny ACEs,
inherited ACEs, non-`None` inheritance or propagation flags, an unprotected
DACL, a wrong owner, or effective access through another group fail closed.
The later proof must resolve the actual Windows access mask and effective group
membership; matching these display names alone is not evidence.

The administrative reservation step must complete as one closed, fail-closed
Local-verified checkpoint. This contract does not claim cross-object filesystem
atomicity: if setup stops after creating or hardening only part of the parent/
placeholder set, the administrator must remove only that incomplete setup and
restart before either principal receives execution authority. The completed
checkpoint must satisfy all of the following together:

1. create the protected parent with the exact owner/DACL above and reject any
   reparse point or junction in the repository-root-to-parent traversal;
2. create exactly `REGISTRY.json` and `LOOKUP_RESPONSES.jsonl`, each as a
   zero-byte regular file with link count one, no alternate stream relied on,
   no reparse attribute, and no sibling temporary artifact;
3. set `REGISTRY.json` to the exact Party C owner and file DACL in G4-GAP-03,
   and `LOOKUP_RESPONSES.jsonl` to the exact Party B owner and file DACL in
   G4-GAP-03, with inheritance disabled and inherited ACEs removed;
4. verify the parent, both placeholder identities, zero-byte contents, owners,
   protected states, complete ACE vectors, link counts, and exact child names
   from a Local read-only token; and
5. deny worker execution if either reservation is missing, nonempty, replaced,
   renamed, linked, security-drifted, or accompanied by an unexpected sibling.

An exact target name is therefore already owned before either publishing
principal starts. Directory `CreateFiles` permits creation of a uniquely named
same-directory transaction temporary file; it does not confer a right to
replace or delete the other principal's reserved target. The writer-owned
target file's own `Delete` right, combined with directory `CreateFiles`, is the
candidate mechanism for own-target atomic replacement. Whether Windows grants
exactly that behavior, while denying every cross-target operation, is a proof
obligation and not a conclusion of this document.

##### C1-R2 Reservation Claim And Publication Semantics

A later C1-R2 must replace the accepted C1 `target absent` / `RequireAbsent`
precondition with an exact reservation claim. Each attempt must allocate a
globally unique transaction ID and acquire one parent-scoped exclusive guard
that covers the Local preflight, the writer mutation, and the Local postflight.
While that guard is held and before any temporary-file creation, a Local
read-only verifier, not Party B or Party C, must verify the canonical
repository root, non-reparse traversal, exact parent identity and security,
the two-name closed sibling set, and both reserved targets. Local must capture
each target's file identity, link count, bytes/hash, owner, DACL protection,
complete semantic ACE vector, attributes and last-write state in a preflight
record bound to the transaction ID, parent identity, and both reservation
identities. The writer receives only the pass/fail authorization reference and
the own-target fields that its DACL permits it to inspect; the record must not
disclose the other target's bytes or security descriptor to that writer.

The writer independently verifies its own reserved target and the parent facts
it is permitted to observe. Local rechecks the complete two-target record under
the same guard immediately before publication and performs the complete
postflight afterward. Party C is never required or permitted to read the
content or security descriptor of Party B's response target. Party B's
accepted read access to Party C's registry remains available only for the
issuer-observation and later lookup purposes already defined by G4-GAP-03; it
does not authorize registry mutation or DACL/owner access beyond that accepted
file DACL. Missing reservation, identity drift, security drift, nonzero
response bytes before
initialization, unexpected sibling, alternate hardlink, reparse point, stale
transaction temporary, concurrent replacement, or a Local record/transaction
binding mismatch fails before mutation.

Each writer may create only its own random, collision-resistant,
same-directory temporary name. The temporary file must be created with
`CreateNew`, written and durably flushed, assigned the final target's exact
owner/protected DACL before becoming visible as a candidate, checked for link
count one and non-reparse state, validated byte-for-byte, and atomically moved
over only that writer's reserved target. During an ordinary transaction, the
writer must never use or clean a temporary file it did not create in that
transaction. A stale or unexpected temporary is evidence of drift and blocks
ordinary publication; it is not deleted opportunistically.

Hard-termination recovery is a distinct administrative operation, not a
successor writer transaction. Before any temporary is created, the later
C1-R2 tooling must durably register with a Local/Administrator-controlled
recovery ledger outside the protected source parent: the transaction ID,
writer SID, target name and captured target file identity, unique temporary
name, expected prestate hashes/security digest, and transaction phase. After
the writer is confirmed terminated, an Administrator recovery process may
acquire the same exclusive guard and remove only the exact ledger-bound
temporary or roll back only that writer's own target. Local must verify the
ledger binding, temporary identity, owner, DACL, link count, non-reparse state,
target prestate-or-complete-poststate, other-target invariance, and final
residue inventory. The recovery record is closed only after that verification.
If the durable binding is absent, ambiguous, or mismatched, the object is an
unknown stale artifact: it remains untouched, source authority stays blocked,
and a separately reviewed remediation is required.

Publication ownership begins only after the atomic replace succeeds. Failure
before that point removes only the transaction's own temporary file and leaves
both reservations unchanged. Failure after that point may roll back only the
target published by that transaction, using captured exact bytes and semantic
security state; it must not delete, recreate, restore, or normalize the other
principal's target. Every success and ordinary catchable failure path must end
with no transaction-owned residue and with the parent and non-target
reservation byte/security state unchanged. A hard termination may temporarily
leave only the exact ledger-bound residue described above; no source state may
advance until the distinct recovery operation ends residue-free and Local
verifies the same invariants.

For the registry, Party C's first publication replaces its own zero-byte
reservation with the freshly generated canonical registry bytes. For the
response log, Party B's initialization is a target-preserving atomic claim of
its own already-zero-byte reservation: it publishes exactly zero bytes through
the same hardened transaction path and creates no lookup row. The first
nonempty response append belongs only to T3E. Neither initialization is a
consumer-binding event.

##### Hermetic Fixture Versus Fresh Operational Input

`G4-SNAPSHOT-JCS-POSITIVE-01`, `G4-ISSUER-CONTENT-JCS-POSITIVE-01`, their
618-byte envelope, `issuer-registry-snapshot-test-0001`, `issuer-test-001`, and
the fixed `2026-09-22T00:00:00Z` / `2026-09-22T00:00:01Z` instants are
hermetic test data only. They remain accepted for deterministic self-tests and
must not be copied, renamed, time-shifted, or treated as an operational source.
Real mode rejects the exact fixture bytes, either reserved test identity, and
either fixed test timestamp before a target transaction begins.

Operational input must be built inside the later governed publication path
from approved issuer-authority content, not accepted as a pre-hashed registry
blob. It must:

1. generate a fresh globally unique `registrySnapshotId` that has never
   appeared in a fixture, source, observation or response;
2. generate `registeredAt` and `writeTimestamp` internally as current RFC 3339
   UTC instants, require `registeredAt <= writeTimestamp`, and reject stale,
   future, caller-supplied or fixed-fixture time values;
3. construct the issuer-authority content object from approved operational
   fields, serialize it to exact RFC 8785 JCS UTF-8 bytes, compute
   `canonicalContentBytesBase64` by strict unpadded base64url, and independently
   recompute `canonicalContentHashHex`;
4. set `issuerAttestedHash` only from the verified approved attestation input
   and require it to equal the recomputed content hash before publication;
5. construct the complete registry envelope, serialize it once to exact RFC
   8785 JCS UTF-8 bytes, and independently recompute the snapshot digest from
   those exact bytes; and
6. reject any caller-supplied digest, timestamp, canonical byte string or
   snapshot identity that differs from the internally generated/recomputed
   value, even if its syntax is valid.

The existing fixed hashes and vectors are not changed by this amendment; they
retain only their hermetic roles. Operational identity, time and content must
be newly evidenced for each authorized creation attempt.

##### Dedicated Party B Issuer-Registry Observation Path

The accepted Group 3 writer is bound to
`governance/sources/verifier_key_registry/REGISTRY.json` and literal
`registryName=verifier_key_registry`; it must not be parameter-substituted or
reused as the issuer route. C1-R2 must provide a separately testable Party B
production path whose input is exactly the published
`governance/sources/issuer_registry/REGISTRY.json` and whose emitted Group 3
record has literal `registryName=issuer_registry`.

That path must reuse, not weaken, the accepted Group 3 immutable-log contract:
one fresh globally unique `snapshotId`; exact published registry bytes encoded
as strict unpadded base64url `snapshot_content`; `snapshotHashHex` recomputed
from those bytes; exact registry version; current internally generated
`observedAt`; approved authority; Party B observer identity; duplicate-ID
rejection; prior-entry hash-chain continuity; protected owner/DACL checks;
real peer-process serialization; durable flush; copy-on-write append; and
publication-owned rollback with exact byte/security restoration. It may append
one issuer observation only after Local has verified Party C's publication.
It cannot append a response, invoke T2C, perform a lookup, or claim source
establishment.

##### Ordered Operational Lifecycle And Status Ceilings

The only permitted order is:

1. Local accepts this C0-R1 amendment at no higher than
   `CONTRACT_ACCEPTED_BOUNDED_SOURCE_NOT_CREATED`.
2. A separately dispatched and independently reviewed C1-R2 implements the
   parent/reservation, fresh-input and issuer-observation contract and may end
   only at `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`.
3. An administrative checkpoint creates both reservations; Local verifies the
   exact parent, targets and effective rights. Status remains
   `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`.
4. A separately authorized operator checkpoint prepares fresh operational
   input; Local verifies its identity, time, canonical bytes and recomputed
   hashes before any Party C write. Status remains
   `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`.
5. Party C claims and atomically publishes only `REGISTRY.json`; Local verifies
   exact bytes, snapshot digest, owner, DACL, target identity, parent security
   and residue-free completion. No source-created status is available yet.
6. Party B uses the dedicated issuer path to append exactly one immutable
   `issuer_registry` observation. Local verifies the observation's exact
   decoded bytes, digest, snapshot ID/version, time, authority, Party B
   identity, chain link, owner/DACL and uniqueness. No source-created status is
   available yet.
7. Party B claims and initializes only its reserved
   `LOOKUP_RESPONSES.jsonl` as exact zero bytes; Local jointly verifies both
   targets, the observation, parent security, cross-principal denials and no
   residue. Only then may T3D-C2 record
   `SOURCE_CREATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`.
8. T3E exclusively performs the first real lookup and first nonempty response
   append, then may record only
   `CONSUMER_BINDING_EXECUTED_PENDING_LOCAL_VERIFICATION`.
9. Only Local verification of the exact response-to-registry-to-observation-to-
   consumer binding may advance to
   `SOURCE_ESTABLISHED_LOCAL_VERIFIED_CONSUMER_BOUND`.

No step may be reordered, combined by inference, or promoted on the strength
of a later step. C0-R1 creates no source; C1-R2 creates no source; reservation
is not publication; registry publication without observation is incomplete;
observation without response reservation is incomplete; an empty response log
is not a lookup; T3D performs no real lookup; and no state here promotes a key
or admits a candidate.

##### Required Actual-Token Proof Matrix

Before any real source authority, a non-elevated process running under the
exact verified Party C token and a separate non-elevated process running under
the exact verified Party B token must execute the following probes against a
disposable directory carrying the exact proposed parent and file security
descriptors. Administrator/SYSTEM setup and Local read-only verification are
separate; their success cannot substitute for either principal's result.

| Probe class | Party C required result | Party B required result | Required postcondition |
|---|---|---|---|
| own-target publication | atomically replace reserved `REGISTRY.json` with validated fresh bytes | atomically replace reserved `LOOKUP_RESPONSES.jsonl` with exact zero bytes and later prove guarded append in a T3E-only fixture | exact bytes and final owner/DACL; no owned temp residue |
| cross-target delete/rename/overwrite/replace | every operation against `LOOKUP_RESPONSES.jsonl` fails | every operation against `REGISTRY.json` fails | non-target file identity, bytes, owner and DACL unchanged |
| owner/DACL mutation | cannot change response owner, protection or ACEs | cannot change registry owner, protection or ACEs | both descriptors semantically identical to prestate |
| parent mutation | cannot create a directory, exercise directory `FILE_DELETE_CHILD`, delete/rename the parent, change parent DACL, take ownership, or delete/rename/replace the other final target | same | parent identity/security and the other reserved name unchanged; deletion of the transaction's own temp or replacement of its own target is allowed only through that file's individual `Delete` right |
| allowed temporary | may create/harden/remove only its own unique registry temp | may create/harden/remove only its own unique response temp | other-principal and unexpected siblings untouched |
| reparse/junction | any reparse component or target blocks before mutation | same | no traversal outside the disposable root |
| hardlink | own or cross target with link count other than one is rejected | same | no linked-path mutation and no normalization |
| sibling drift | unexpected file, directory, stream relied on by the transaction, or stale temp blocks publication | same | drift preserved for investigation; the writer deletes nothing outside its current transaction and only the distinct journal-bound recovery operation may remove proven prior-transaction residue |
| security drift | inherited, extra, deny or reordered/noncanonical ACE; wrong owner; unprotected DACL; or widened effective group access is rejected | same | exact prestate retained |
| concurrency | same-target real peer process cannot enter before release; cross-target processes cannot use one target to alter the other | same | one winner per target, deterministic successor, no partial state |
| crash/rollback | hard termination after acquire, after durable temp flush and before/after replace has an exact ledger-bound administrative recovery or remains fail-closed without cleanup | same | target is exact prestate or exact complete poststate, never partial; accepted recovery leaves no transaction-owned residue, while absent/ambiguous binding preserves the artifact and blocks source authority |

Each negative probe must record the attempted operation, actual token SID,
resolved access mask, expected denial, observed failure, pre/post file IDs,
bytes/hashes, owner, protection state, complete semantic ACE sets, link counts,
parent state and residue inventory. A thrown exception without verified
postconditions is not sufficient. The proof is accepted only if every
own-target positive succeeds and every cross-target/parent negative fails
under the intended real token.

##### Failure And Fallback Boundary

Any failure to prove the shared-directory candidate, including an own-target
atomic replace that Windows denies, a cross-target operation that succeeds, a
required denial that depends on elevation or ambient group membership, or a
cleanup/rollback state that cannot be distinguished exactly, leaves Group 4 at
`TOOLING_ACCEPTED_SOURCE_NOT_CREATED`. The next move is a new Local-reviewed
contract selecting either separate protected parent paths or a narrowly
specified privileged mediator. Neither fallback is authorized or designed by
this amendment, and no real source action may occur before one is accepted.
