# CVF GC-018 Baseline - ACEL G1 T3D C0 Group 4 Contract Coherence Amendment

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-22

Batch ID: ACEL-G1-T3D-C0-GROUP4-CONTRACT-COHERENCE-AMENDMENT

Dispatch base HEAD: `e341a9021`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id ACEL-G1-T3D-C0-GROUP4-CONTRACT-COHERENCE-AMENDMENT --title "ACEL G1 T3D C0 Group 4 Contract Coherence Amendment" --date 2026-09-22 --base e341a9021 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | GC-018 documentation-only dispatch baseline |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated the exact four-gap byte, authority, DACL, lifecycle, vector and non-claim decisions |
| checkerReadAheadConfirmation | structural-completeness, scaffold-provenance, closeability and public-export checker sources reviewed |
| docOnlyNewFields | `canonicalContentBytesBase64` and its exact non-circular issuer-authority content contract |
| claimBoundary | baseline authors contract only; no tooling, source, transaction or consumer execution |

## Purpose

Freeze the four previously implicit Group 4 decisions before any issuer-registry
or lookup-response tooling is dispatched: immutable published-registry bytes,
non-circular issuer-content bytes, separated write authority, and the bounded
T3D-to-T3E establishment lifecycle. This amendment is the authoritative
addendum to the accepted T2F Group 4 contract; it does not create a second
operational-source contract.

## Scope / Owner Boundary

This baseline authorizes contract amendment only. A future worker may implement
only after a separately accepted T3D-C1 work order. Party C is the exact local
principal `S-1-5-21-1644666849-912006174-747199667-1010`; Party B is the exact
local principal `S-1-5-21-1644666849-912006174-747199667-1009`; Local is the
exact local principal ending `-1001`. Party A and the Contract 2 Approver have
no Group 4 file access. A shared-workspace worker remains an `INTERNAL_AGENT`;
Local is the final decision owner and reviewer.

## Decision / Baseline / Proposed Tranche

Decision: `AMEND_CONTRACT_THEN_STOP_FOR_SEPARATE_IMPLEMENTATION_AUTHORITY`.

Baseline: the T2F Source Group 4 schema, T2C lookup binding, and immutable
Party B observation model remain controlling except where this amendment makes
the previously unspecified byte, authority, and lifecycle rules explicit.

Proposed tranche: T3D-C0 produces this contract amendment only. T3D-C1 may
create tooling and a first local-verification source only after its own
authority. T3E alone owns the first real verifier lookup and the final
consumer-binding evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Disposition |
|---|---|---|---|---|
| Four decision-changing Group 4 gaps require one amendment | REVIEWED_DECISION | `docs/audits/CVF_ACEL_G1_T3D_GROUP4_PRE_IMPLEMENTATION_CONTRACT_GAP_AUDIT_2026-09-22.md` | Findings / Position, G4-GAP-01 through G4-GAP-04; Selected Route | ACCEPT |
| Existing Group 4 envelope, row, response, lookup, and establishment fields | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 4; T2C Consumer-Binding Table; Establishment Evidence Required | ACCEPT_WITH_AMENDMENT |
| Party C exact principal is Local verified but Group 4 is not established | LOCAL_VERIFICATION | `docs/audits/CVF_ACEL_G1_T3D_PARTY_C_PRINCIPAL_LOCAL_VERIFICATION_2026-09-22.md` | Findings / Position; Claim Boundary | ACCEPT |
| Current tranche permits one consolidated C0 baseline and work order only | CURRENT_SESSION_AUTHORITY | `AGENT_HANDOFF_V63_2026-09-18.md` | Next Allowed Move | ACCEPT |

## Schema Amendments

### GAP1 - Published Registry Envelope Bytes

`REGISTRY.json` is exactly one UTF-8 RFC 8785 JCS serialization of one JSON
object with exactly these fields: `registrySnapshotId`,
`registrySnapshotVersion`, `writeTimestamp`, and `rows`. It has no UTF-8 BOM,
leading or trailing whitespace, or terminal newline. No parser-normalized,
pretty-printed, reserialized, reconstructed, or subset representation is the
published registry envelope.

`registrySnapshotHashHex` is the lowercase SHA-256 hexadecimal digest of those
exact published bytes. Party B's Group 3 `snapshot_content` is the strict,
unpadded base64url encoding of exactly those bytes; after strict decode, its
bytes and SHA-256 must equal the published bytes and
`registrySnapshotHashHex`, respectively. A lookup response must carry that
same snapshot ID, version, and digest.

Positive vector `G4-SNAPSHOT-JCS-POSITIVE-01` has the required digest
`d31e0c206da091bc408005d490e69f7aa0eae733dac4b03c67edd280034827f2`.
The acceptance fixture must construct its byte preimage only by the preceding
JCS recipe and recompute this value; a copied digest is not evidence.

Its exact published UTF-8 bytes are the bytes of this single line, excluding
the Markdown fence delimiters and with no terminal newline:

```json
{"registrySnapshotId":"issuer-registry-snapshot-test-0001","registrySnapshotVersion":1,"rows":[{"canonicalContentBytesBase64":"eyJhdXRob3JpdHkiOiJBQ0VMX0cxX0RFQ0lTSU9OX09XTkVSIiwiaXNzdWVySWRlbnRpdHkiOiJpc3N1ZXItdGVzdC0wMDEiLCJwb2xpY3lWZXJzaW9uIjoxfQ","canonicalContentHashHex":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","correctedAt":null,"entryVersion":1,"issuerAttestedHash":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","issuerIdentity":"issuer-test-001","registeredAt":"2026-09-22T00:00:00Z","revokedAt":null,"status":"ACTIVE"}],"writeTimestamp":"2026-09-22T00:00:01Z"}
```

Reject before observation or response append: a BOM, any leading/trailing
whitespace or newline, a non-JCS serialization, a missing/extra envelope
field, a non-lowercase or mismatched digest, padded base64url, whitespace or
non-base64url alphabet, noncanonical base64url, decoded-byte mismatch, or
snapshot ID/version mismatch.

### GAP2 - Issuer Canonical Content Bytes

Every issuer row must add required `canonicalContentBytesBase64`. It is the
strict unpadded base64url encoding of the UTF-8 RFC 8785 JCS bytes of the
issuer canonical-content object. `canonicalContentHashHex` is the lowercase
SHA-256 hexadecimal digest of the strictly decoded value, not a digest of the
row, not a digest of a caller-supplied attestation, and not a self-referential
preimage. The registry independently recomputes it before it may write the
row or issue a lookup result.

Positive vector `G4-ISSUER-CONTENT-JCS-POSITIVE-01` uses canonical content
`{"authority":"ACEL_G1_DECISION_OWNER","issuerIdentity":"issuer-test-001","policyVersion":1}`
and requires digest
`db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca`.

Validation order is mandatory: (1) field presence/type and the exact strict
base64url alphabet/no-padding form; (2) decode exactly once; (3) decoded bytes
are valid UTF-8 JSON and byte-identical to its RFC 8785 JCS serialization;
(4) recompute lowercase SHA-256; (5) compare with `canonicalContentHashHex`;
(6) require `claimedIssuerHash == issuerAttestedHash ==
canonicalContentHashHex`; (7) only then verify the registry snapshot and Party
B exact-byte observation binding; (8) only then apply issuer identity,
version, status, and lookup predicates.
Reject at the first failed step. In particular reject padded or whitespace
encoding, non-JCS decoded content, invalid UTF-8/JSON, uppercase/non-hex or
mismatched digest, missing content bytes, an attempt to hash the complete row,
or a caller claim substituted for the recomputation.

### GAP3 - Separated Principals And Exact Protected DACLs

The future registry file is `governance/sources/issuer_registry/REGISTRY.json`;
the future response log is
`governance/sources/issuer_registry/LOOKUP_RESPONSES.jsonl`. Each file has a
protected DACL: inheritance disabled and inherited ACEs removed. The listed
ACEs are the complete DACL; no implicit principal, group, deny ACE, or extra
allow ACE is permitted. Owner is recorded separately and is not a substitute
for its listed access ACE.

| File | Owner | Exact protected DACL ACEs | Prohibited identities |
|---|---|---|---|
| `REGISTRY.json` | Party C `S-1-5-21-1644666849-912006174-747199667-1010` | Party C: Allow `FullControl`; `NT AUTHORITY\\SYSTEM`: Allow `FullControl`; `BUILTIN\\Administrators`: Allow `FullControl`; Party B `...-1009`: Allow `Read`; Local `...-1001`: Allow `Read` | Party A and Approver: no ACE and no effective access |
| `LOOKUP_RESPONSES.jsonl` | Party B `S-1-5-21-1644666849-912006174-747199667-1009` | Party B: Allow `FullControl`; `NT AUTHORITY\\SYSTEM`: Allow `FullControl`; `BUILTIN\\Administrators`: Allow `FullControl`; Local `...-1001`: Allow `Read` | Party C, Party A, and Approver: no ACE and no effective access |

Party C is the exclusive registry owner/writer. Party B is the exclusive
response-log appender and cannot alter the registry. Local is read-only in
both matrices. Party C cannot append lookup responses, so query evidence is
not self-authored. The Approver and Party A have no read, append, write, owner,
or DACL-modification access to either Group 4 file.

Required negative/rollback tests are: Party B registry write and DACL change
are denied; Party C response append and DACL change are denied; Party A and
Approver cannot read, write, append, take ownership, or alter either DACL;
Local cannot write, append, take ownership, or alter either DACL. For a
failed write, append, owner, or DACL validation attempt, the implementation
must restore and compare the prior file bytes, owner, protection state, and
complete ordered ACE matrix byte-for-byte/semantically exactly as captured
before the attempt; no partial file, response line, widened ACE, or ownership
change may remain.

### GAP4 - Establishment Lifecycle Boundary

The only permitted sequence is:

`TOOLING_ACCEPTED_SOURCE_NOT_CREATED` ->
`SOURCE_CREATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING` ->
`CONSUMER_BINDING_EXECUTED_PENDING_LOCAL_VERIFICATION` ->
`SOURCE_ESTABLISHED_LOCAL_VERIFIED_CONSUMER_BOUND`.

T3D-C0 ends at `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`. A future T3D-C1 may
reach only `SOURCE_CREATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING` after
Local verifies paths, exact bytes, digests, owners, DACLs, and non-live
negative/rollback tests. T3E, not T3D, performs the first real verifier
consumer lookup and records only
`CONSUMER_BINDING_EXECUTED_PENDING_LOCAL_VERIFICATION`; Local verification of
that evidence alone may advance to
`SOURCE_ESTABLISHED_LOCAL_VERIFIED_CONSUMER_BOUND`. T3D must not claim a real
lookup, consumer binding, or source-established disposition.

## Acceptance Criteria

1. The future implementation contract repeats the two exact byte recipes,
   positive vectors, validation orders, and rejection conditions without
   weakening them.
2. Independent recomputation proves both stated positive SHA-256 vectors and
   proves Party B's decoded snapshot bytes equal the published registry bytes.
3. The two-file owner/DACL matrices match exactly, and every forbidden-access
   and rollback test passes without residue.
4. T3D evidence is capped at
   `SOURCE_CREATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`; T3E retains the
   first real lookup and final consumer-binding route.
5. No source, tooling, response, observation, consumer call, credential,
   provider call, public export, staging, or commit is performed by this C0
   baseline itself.

## Evidence / Verification Boundary

Local must verify a future C1 return against the literal bytes, independently
recomputed SHA-256 values, complete DACL matrices, and all negative rollback
receipts. A checker pass or an account's existence does not establish a Group
4 source or consumer binding.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | baseline Source, Decision, Evidence, Claim Boundary, and Public Export Disposition headings; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm authored baseline shape, not create implementation or source evidence |
| claimBoundary | contract amendment only; gate conformity is not source establishment |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Local contract amendment; no public-sync action or public
artifact is authorized.

## Claim Boundary

This baseline freezes only a future Group 4 implementation contract. It does
not create `REGISTRY.json` or `LOOKUP_RESPONSES.jsonl`, perform an observation
or lookup, bind a verifier consumer, establish a source, promote a key, admit
a candidate, invoke a provider, activate runtime behavior, export publicly,
deploy, stage, or commit.
