# CVF ACEL G1 T2F Operational Source Establishment Contract

Memory class: governed-worker-audit

docType: audit

Status: PROPOSED_CONTRACT_DESIGN_ONLY

Date: 2026-09-18

executionBaseHead: `c743bb37a08a29efebf9381e86792088c9105ce3`

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_2026-09-18.md`; the committed paired baseline is `docs/baselines/CVF_GC018_ACEL_G1_T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_2026-09-18.md`. Unlike R2 and R3, this T2G tranche is a properly committed dispatch (see Claim Boundary)

reworkGeneration: 0 (T2G is a new `INITIAL` architecture tranche per its own SCEC block, not a numbered rework of the T2F-R1/R2/R3 correction-model chain)

priorAuditSha256: `33f258d4a1fa6f6b389b309e45de526fbde1b5cc7468520c43ac839e4878bc15` (R3-final, before this T2G architecture replacement)

Worker role: one shared-workspace `INTERNAL_AGENT`

## Purpose

Design one integrated, implementation-neutral establishment contract for the
four T2E operational source groups so Local can later issue source-specific
implementation work orders without inventing paths, schemas, identity/version
rules, access boundaries or admission evidence. This document does not create,
populate or operate any source. Every source group remains `SOURCE_NOT_CREATED`
and every candidate admission remains `UNVERIFIED`.

R1 revision: this document was rejected by
`docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md`
for five findings (T2F-R1-01 through T2F-R1-05: ambiguous/self-referential
canonical hashing, incomplete schemas, unsatisfied T2C consumer joins,
incoherent activation semantics, missing literal path-collision evidence) and
is corrected here in place. See the Finding-To-Repair Locator Ledger below.

R2 revision: R1's own positive-vector digest was an asserted, not actually
computed, hash, and mixed fields from two different declared schemas
(T2F-R2-01); R1's single-parent `correctionOf` design could not resolve a
multi-head fork in one entry despite claiming it could (T2F-R2-02). Both are
corrected here in place with actually-recomputed digests and a redesigned,
array-based `correctionOf` field verified against a concrete multi-head
test.

R3 revision: independent review found three further contract-level
contradictions in R2's own evidence: `specHashHex` was defined twice with
two mutually incompatible preimages (T2F-R3-01); R2's fork-resolution
algorithm silently redefined T2C's literal "more than one source-owned
observation" semantic without disclosing the change as a decision
(T2F-R3-02); and the `correctionOf` union algorithm lacked a snapshot-scope
and liveness check while `snapshot_content` left three incompatible byte
representations undetermined (T2F-R3-03). All three are corrected here in
place; the corrected `countObservationsFor` design was re-verified against
R2's own multi-parent fork test to confirm no regression.

T2G revision (committed work order, not a numbered rework): a Local reviewer
found R3's own `correctionOf` liveness rule contradicted R3's own D/E
regression test, a third consecutive correction-model defect after R1's
self-referential hash and R2's silently-redefined count semantic. Rather
than dispatch a fourth repair round on the same correction/fork-merge
architecture, the operator selected a materially simpler design: immutable,
write-once `snapshotId` values with exactly one original observation per ID
and no correction, supersession, merge, or active-head mechanism of any
kind. An erroneous or stale observation is never repaired in place; a new
observation always receives a brand-new `snapshotId`, and any receipt bound
to an old ID is never implicitly rebound. See Immutable Snapshot Identity
(T2G-01 through T2G-05) below, which replaces the prior Active-Head And Fork
Resolution subsection and its `entryKind`/`correctionOf` schema fields
entirely.

## Target / Source

| Source | Verified locator | Use |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Contracts 1-4; Cross-Contract Separation Matrix; Admission Evidence Ledger | required source forms, prohibited combinations, admission evidence |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party A Appointment Contract | Contract 1 plus Contract 2 accountable identity and forbidden combinations |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B Appointment Contract | Contract 3 accountable identity, two-registry observation scope |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party C Appointment Contract | Contract 4 accountable identity, issuer authority scope |
| `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Activation Approver Appointment Contract | independent exact-version/canonical-bytes/hash activation authority |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md` | Decision / Disposition | selected integrated-tranche scope |
| `docs/baselines/CVF_GC018_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Proposed Tranche | exact two-output authorization |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Contract Requirements; Required Handoff Evidence | field-level requirements this audit must satisfy |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md` | Findings / Position T2F-R1-01 through T2F-R1-05 | frozen R1 correction contract this revision must close |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2F_R1_CONTRACT_COHERENCE_CORRECTION_2026-09-18.md` | Consolidated R1 Correction Matrix | exact R1 field-level requirements |
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Key Identity And Lifecycle; Three Independent Admission Predicates; Preimage Construction | accepted consumer contract this revision must join field-for-field |

## Scope / Methodology

Documentation-only design task. Local's T2F readiness decision already
selected one integrated contract over four separate designs and over direct
implementation (`docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md`,
Option Assessment). This audit reuses that accepted decision rather than
re-deriving it, and reuses T2E's accepted source-form findings rather than
re-running T2D's original source search. One targeted collision query was
executed before authoring, per the work order's Negative Search And Collision
Discipline:

```
rg -n --hidden --no-ignore -i "ACEL-G1-T2F|OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT" docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'
```

Result: matches occur only inside the T2F decision, baseline and work order
(the three governing packet documents already disclosing this same collision
in their own Negative Search sections). No occurrence exists in
`governance/compat/*.py` source, project-authored `EXTENSIONS` TypeScript
source, or any other implementation surface. This is a bounded, targeted
collision check, not a new complete-corpus inventory.

Search roots: `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION`,
restricted to `*.md`, `*.json`, `*.py`, `*.ts`. No external research, network
lookup, or provider memory was used; provider memory is `NOT_CVF_SOURCE`.

## T2E-Requirement-To-T2F-Field Reconciliation

| T2E requirement | T2F contract field satisfying it | Group(s) |
|---|---|---|
| accountable responsibility named | Accountable Owner row | 1, 2, 3, 4 |
| prohibited dual roles | Cross-Source Identity And Access Matrix | 1, 2, 3, 4 |
| source-of-truth form not yet created | proposed exact future path plus `SOURCE_NOT_CREATED` disposition | 1, 2, 3, 4 |
| decision maker / write authority | Write Principal row | 1, 2, 3, 4 |
| read/verifier consumers | Source-To-Consumer Binding Matrix | 1, 2, 3, 4 |
| version/identity scheme | Version / Snapshot / Canonical Hash Matrix | 1, 2, 3, 4 |
| lifecycle transitions | Lifecycle / State Transitions row | 1, 2, 3, 4 |
| durable evidence | Durable Receipt row | 1, 2, 3, 4 |
| correction/rotation/revocation route | Correction, Rotation, Supersession, Revocation row | 1, 2, 3, 4 |
| required admission evidence | Establishment Evidence Checklist | 1, 2, 3, 4 |
| fail-closed behavior | Validation Order And Failure Taxonomy row | 1, 2, 3, 4 |
| Party A forbidden from Party B/C | Cross-Source Identity And Access Matrix, Case 1/2/4/10 | 1, 2 |
| Party B independence from both writers | Cross-Source Identity And Access Matrix, Case 1/3 | 3 |
| Party C non-self-verification | Cross-Source Identity And Access Matrix, Case 5 | 4 |
| activation approver distinct from Parties A/B/C | Contract 2 Write Principal plus Access row | 2 |
| circular authority, stale/unavailable/conflicting data, in-place rewrite, caller-supplied unbound hash, emergency bypass | Negative Cases | 1, 2, 3, 4 |
| implementation split without opening a successor | Proposed Implementation Order; `successorTrancheOpened: NO` | 1, 2, 3, 4 |

## Finding-To-Repair Locator Ledger

| Finding | Repair locator | Disposition |
|---|---|---|
| T2F-R1-01: canonical hash profile ambiguous and self-referential | `cvf.source-record-canonicalization@1` profile section below; applied in every group's Canonicalization / Hashing Rule row | RESOLVED |
| T2F-R1-02: declared schemas incomplete | Group 1 registry envelope plus lifecycle-receipt schema; Group 2 specification/decision-event fields; Group 3 snapshot/log fields; Group 4 registry-snapshot and lookup-response fields, all below | RESOLVED |
| T2F-R1-03: proposed sources cannot satisfy accepted T2C consumer | T2C Consumer-Binding Table below; per-group schema fields renamed/added to match | RESOLVED |
| T2F-R1-04: automatic latest-wins activation contradicts fail-closed conflict handling | Group 2 Explicit Activation Events subsection below | RESOLVED |
| T2F-R1-05: proposed operational paths not collision-checked | Literal Proposed-Path Collision Ledger below | RESOLVED |
| T2F-R2-01: R1's positive recomputation vector was not an actually recomputed digest, and mixed registry-envelope fields into a key-row preimage | Closed Preimage Field Lists subsection; corrected Positive Recomputation Example with two independently recomputed digests; corrected Negative Mutation Probes with actually recomputed drift/omission digests | RESOLVED |
| T2F-R2-02: R1's single-parent `correctionOf` field could not resolve a multi-head fork in one correction entry, contradicting the claim that it could | `correctionOf` redefined as an array field; Active-Head And Fork Resolution subsection rewritten with a concrete A->{B,C}->D verified test | RESOLVED |
| T2F-R3-01: `specHashHex` was defined twice with two incompatible preimages (direct content bytes versus a JCS metadata envelope) | Two Distinct Group 2 Hashes subsection; `specHashHex` (raw content) separated from `specFileRecordHashHex` (JCS envelope) | RESOLVED |
| T2F-R3-02: R2's `countObservationsFor` silently redefined T2C's literal "more than one source-owned observation" to count only un-superseded correction-chain heads, not disclosed as a semantic decision | `entryKind` (`original`\|`correction`) added; unified active-head resolution counts independent originals as a real fork; T2C interface reconciliation corrected to state the semantic was preserved, not silently changed | RESOLVED |
| T2F-R3-03: `correctionOf` union algorithm had no snapshot-scope or liveness-at-append-time check, and `snapshot_content` left three incompatible representations undetermined | `correctionOf` scope-and-liveness rule added with a rejected cross-snapshot test case; `snapshot_content` pinned to base64url-encoded raw JSON bytes, one representation only | RESOLVED (superseded by T2G-01 through T2G-05, which remove the `correctionOf` mechanism entirely) |
| T2G-01 through T2G-07: R3's liveness rule contradicted its own regression test, escalating three rounds of same-ID correction/fork-merge repair; the operator selected a materially simpler immutable-snapshot-ID architecture instead of a fourth repair round | `#### Immutable Snapshot Identity (T2G-01 through T2G-05)` subsection below; Group 3 and dependent Group 4/matrices/checklist reconciled to the new model; every `entryKind`/`correctionOf`/active-head mechanism removed from normative text | RESOLVED |

## Canonicalization Profile: `cvf.source-record-canonicalization@1`

This profile governs every new source-record digest defined in Groups 1-4
below. It does not govern or alter the already-accepted T2C
`cvf.verifierReceipt` RFC 8785 JCS profile, which remains exactly as T2C
defines it.

| Field | Rule |
|---|---|
| `profile` | fixed literal `cvf.source-record-canonicalization@1`; included as a normal JCS field inside every preimage, never merely a document label |
| `domain` | one fixed literal per record kind (for example `cvf.keyRegistryRow`, `cvf.keyLifecycleReceipt`, `cvf.specDecisionEvent`, `cvf.observationLogEntry`, `cvf.issuerRegistryRow`, `cvf.issuerLookupResponse`); included as a normal JCS field, never a prose-only label |
| Canonicalization | RFC 8785 JCS (JSON Canonicalization Scheme) over the named JSON object; UTF-8 encoding; no BOM; lexicographic key ordering by exact key string at every object level, including nested objects; arrays preserve semantic (not sorted) order; numeric values as canonical decimal strings; no comments, no trailing commas |
| Digest | lowercase 64-hex-character SHA-256 of the compact JCS byte sequence |
| Preimage field list | each record kind below declares its exact, closed preimage field list; no field outside that list may appear in the preimage; no field on the list may be omitted |
| Stored digest exclusion | the record's own stored digest field (for example `rowHashHex`, `entryHashHex`, `decisionHashHex`) is never included in its own preimage; it is computed after the preimage is fixed and stored alongside it, outside the hashed object |
| Chained records | a chained record includes `priorEntryHashHex` as a normal JCS field inside its own preimage, using the exact literal string `null` (JSON null) for the genesis record; this makes the hash chain unambiguous JCS, not byte concatenation with a lower-level framing rule |
| Fail-closed rejection | reject: (a) a preimage that declares a `profile` literal other than `cvf.source-record-canonicalization@1`, (b) a preimage with any field not on the record kind's declared field list (extra field), (c) a preimage missing any declared field, (d) a digest that is not exactly 64 lowercase hex characters, (e) a duplicate stable identity for the same record kind, (f) a recomputation whose result does not exactly match the stored digest |

### Closed Preimage Field Lists (T2F-R2-01)

Every record kind's preimage is exactly `profile` + `domain` + the fields
listed below, in this closed set, no more and no fewer. Nullability is
explicit; a nullable field is still required on the list (present with JSON
`null`), never omitted. The record's own stored digest is listed separately
below each closed set for clarity, but `priorEntryHashHex` (where a record
kind is hash-chained) is itself part of the closed preimage list, per the
Canonicalization Profile's chained-record rule; only the record's own stored
digest (`rowHashHex`, `entryHashHex`, `decisionHashHex`) is excluded from
its own preimage. Group 3's `cvf.observationLogEntry` carries no
correction/fork-merge chain-link field of any kind; `snapshotId` is
immutable and write-once, so no record ever supersedes another (see
Immutable Snapshot Identity, T2G-01 through T2G-05).

| Record kind | Closed preimage fields (beyond `profile`, `domain`) | Nullable fields | Stored digest (excluded from own preimage) |
|---|---|---|---|
| `cvf.keyRegistryRow` (Group 1 registry row) | `keyId`, `publicKeyBytesBase64`, `algorithm`, `role`, `issuedAt`, `expiresAt`, `revokedAt`, `status`, `rotatedFromKeyId` | `expiresAt`, `revokedAt`, `rotatedFromKeyId` | `rowHashHex` |
| `cvf.keyLifecycleReceipt` (Group 1 lifecycle row) | `transitionId`, `keyId`, `registrySnapshotVersionBefore`, `registrySnapshotVersionAfter`, `priorStatus`, `newStatus`, `actor`, `timestamp`, `priorEntryHashHex` | none | `entryHashHex` |
| `cvf.specFile` (Group 2 spec file) | `specVersion`, `canonicalBytesBase64`, `authorId`, `proposedAt`, `specHashHex` (see below; included as a normal field here, not excluded, because it is not this record kind's own stored digest) | none | `specFileRecordHashHex` |
| `cvf.specDecisionEvent` (Group 2 decision event) | `decisionEventId`, `eventType`, `specVersion`, `recomputedHashHex`, `approverId`, `decidedAt`, `priorEntryHashHex` | none | `entryHashHex` |
| `cvf.observationLogEntry` (Group 3 log entry) | `snapshotId`, `registryName`, `registrySnapshotVersion`, `snapshotHashHex`, `observedAt`, `authority`, `observerIdentity`, `priorEntryHashHex` | none | `entryHashHex` |
| `cvf.issuerRegistryRow` (Group 4 registry row) | `issuerIdentity`, `entryVersion`, `issuerAttestedHash`, `canonicalContentHashHex`, `status`, `registeredAt`, `correctedAt`, `revokedAt` | `correctedAt`, `revokedAt` | none stored on this row; the row is read live, not hash-chained |
| `cvf.issuerLookupResponse` (Group 4 lookup response) | `lookupId`, `issuerIdentity`, `claimedIssuerHash`, `registrySnapshotId`, `registrySnapshotHashHex`, `registrySnapshotVersion`, `entryVersion`, `result`, `errorCode`, `queriedAt`, `consumerIdentity`, `observedSnapshotId`, `priorEntryHashHex` | `errorCode` | `entryHashHex` |

`snapshot_content` for Group 3 is deliberately excluded from
`cvf.observationLogEntry`'s hashed preimage: it is the large observed
payload, bound in only via `snapshotHashHex` (the field on the closed list),
so the preimage stays a bounded-size commitment rather than embedding the
full snapshot bytes.

### Two Distinct Group 2 Hashes (T2F-R3-01)

R2 defined `specHashHex` twice with two different preimages that cannot
share one digest: once as "SHA-256 of `canonicalBytesBase64` decoded bytes"
(a raw-content hash) and once as the `cvf.specFile` domain's JCS preimage
digest under `cvf.source-record-canonicalization@1` (a metadata-envelope
hash including `authorId`/`proposedAt`). These are corrected here as two
separately named fields with two separately named purposes:

- **`specHashHex`** is exactly SHA-256 of the raw bytes decoded from
  `canonicalBytesBase64`, nothing else. This is the value T2C's
  `verificationAuthorityHash` binds to (`docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`,
  `verificationAuthorityHash` field: "SHA-256 of authority specification at
  lookup time"). It identifies the specification's *content* only, so two
  spec-file records with byte-identical `canonicalBytesBase64` but different
  `authorId`/`proposedAt` metadata must produce the identical `specHashHex`;
  content identity must not depend on publishing metadata. `specHashHex` is
  never itself hashed under the `cvf.source-record-canonicalization@1`
  profile; it is computed directly and independently of that profile,
  exactly as T2C already specifies for `verificationAuthorityHash`.
- **`specFileRecordHashHex`** is the `cvf.specFile` closed-preimage digest
  under `cvf.source-record-canonicalization@1`, covering `specVersion`,
  `canonicalBytesBase64`, `authorId`, `proposedAt`, and `specHashHex` as a
  normal field value (not re-hashing `specHashHex`'s own preimage, simply
  including the already-computed value as one field among several). This is
  the record kind's own stored digest, used for spec-file-record integrity
  and inclusion in any future record-level chaining; it is never read by
  T2C and never substituted for `specHashHex` in the `verificationAuthorityHash`
  binding.

Every reference elsewhere in this document to "`specHashHex` = SHA-256 of
`canonicalBytesBase64` decoded bytes" and to "`verificationAuthorityHash` ==
`specHashHex`" refers to the raw-content hash defined here, never to
`specFileRecordHashHex`.

### Positive Recomputation Example (Group 1 Key-Registry Row)

This vector reconciles exactly with the `cvf.keyRegistryRow` closed preimage
field list above: it contains `profile`, `domain`, and only the nine
Group-1-key-row fields (`keyId`, `publicKeyBytesBase64`, `algorithm`, `role`,
`issuedAt`, `expiresAt`, `revokedAt`, `status`, `rotatedFromKeyId`). It
excludes registry-envelope-only fields (`registrySnapshotId`,
`registrySnapshotVersion`, `writeTimestamp`), which belong to the envelope's
own preimage, not the row's.

Preimage object (pretty-printed for readability; the actual hashed bytes are
the compact JCS form below):

```json
{
  "profile": "cvf.source-record-canonicalization@1",
  "domain": "cvf.keyRegistryRow",
  "keyId": "key-testvector-0001",
  "publicKeyBytesBase64": "RMcYJcHIAYbM9S2L717B9wmMom1ZMEIs-PTJrQRXomw",
  "algorithm": "Ed25519",
  "role": "verificationAuthority",
  "issuedAt": "2026-09-18T00:00:00Z",
  "expiresAt": "2027-09-18T00:00:00Z",
  "revokedAt": null,
  "status": "ACTIVE",
  "rotatedFromKeyId": null
}
```

Compact JCS bytes (this is `preimage_bytes` passed to `SHA256`; produced by
`json.dumps(preimage, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode("utf-8")`
in Python, which is RFC 8785 JCS-equivalent for this ASCII-only, non-nested,
no-duplicate-key object):

```
{"algorithm":"Ed25519","domain":"cvf.keyRegistryRow","expiresAt":"2027-09-18T00:00:00Z","issuedAt":"2026-09-18T00:00:00Z","keyId":"key-testvector-0001","profile":"cvf.source-record-canonicalization@1","publicKeyBytesBase64":"RMcYJcHIAYbM9S2L717B9wmMom1ZMEIs-PTJrQRXomw","revokedAt":null,"role":"verificationAuthority","rotatedFromKeyId":null,"status":"ACTIVE"}
```

Byte length of the compact form: 360 bytes.

`rowHashHex` (SHA-256 of the bytes above): `0c798661caf02b0d3537b845ca6b95f94c3ad4af4221ca4502d508dba17d3061`

Independent recomputation performed twice with two separate tools against
the exact compact-JCS byte string above:

1. Python `hashlib.sha256(preimage_bytes).hexdigest()` on the
   `json.dumps`-produced bytes: `0c798661caf02b0d3537b845ca6b95f94c3ad4af4221ca4502d508dba17d3061`.
2. GNU coreutils `sha256sum` on a file containing the identical byte string
   written via `printf '%s'` (no trailing newline): `0c798661caf02b0d3537b845ca6b95f94c3ad4af4221ca4502d508dba17d3061`.

Both recomputations match exactly and equal the digest above; the digest is
64 lowercase hex characters. This digest is computed only for
design-consistency illustration; it is not a claim that the key registry
exists, that this key was issued, or that any signature verifies against it.

### Negative Mutation Probes

Each probe below was independently constructed and, where a hash is at
stake, actually recomputed against the positive vector's fields to confirm
the claimed result, not asserted from prose alone.

| Probe | Mutation | Verified result |
|---|---|---|
| self-hash | preimage includes its own `rowHashHex` as a field | reject: extra field not on the closed `cvf.keyRegistryRow` list; the profile forbids a stored digest inside its own preimage |
| prior-hash tamper | (applies to chained record kinds, e.g. `cvf.keyLifecycleReceipt`) `priorEntryHashHex` changed to a different valid-looking hex string not matching the actual prior record's `entryHashHex` | recomputed chain digest from genesis no longer matches; reject |
| field omission | `rotatedFromKeyId` removed entirely from the preimage object (not set to `null`, physically absent) | actually recomputing the JCS bytes without this field yields digest `5d15fd86077982e829fe79aa1b1e2f1d159cb2eedc5c7a9d8ccefe38b4a63ec3`, which differs from the correct digest and is also structurally invalid (missing declared field, even though nullable); reject on missing-field check before any hash comparison |
| canonicalization drift | preimage serialized with keys in declaration order (`profile`, `domain`, `keyId`, ...) instead of lexicographic JCS order | actually recomputing the declaration-order bytes yields digest `f0c32e4f2d7a2ddacd188039f9c14346bd96f6beb677441fce89055e586343d5`, which differs from the correct digest `0c798661caf02b0d3537b845ca6b95f94c3ad4af4221ca4502d508dba17d3061`; reject on mismatch |
| profile drift | `profile` literal changed to an unversioned or different string | reject: unknown/mismatched profile literal, checked before any digest comparison |

## Findings / Position

### Source Group 1: Verifier Public-Key Registry And Key-Lifecycle Receipts

| Field | Value |
|---|---|
| Proposed exact future path (registry) | `governance/sources/verifier_key_registry/REGISTRY.json` (`PROPOSED_LOCAL_REVIEW`) |
| Proposed exact future path (lifecycle receipts) | `governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl` (`PROPOSED_LOCAL_REVIEW`) |
| Format / schema (registry envelope) | JSON object: `registrySnapshotId` (string, global snapshot identity), `registrySnapshotVersion` (monotonic integer), `writeTimestamp` (RFC 3339), `rows` (array of key rows) |
| Format / schema (key row) | `keyId` (string, stable identity), `publicKeyBytesBase64` (string, Ed25519), `algorithm` (fixed literal `"Ed25519"`), `role` (string; must authorize issuance for a named `verificationAuthority`, matching T2C's `keyRecord.role.authorizesIssuanceFor(...)` check), `issuedAt`/`expiresAt`/`revokedAt` (RFC 3339 or `null`), `status` (`ACTIVE`\|`ROTATING`\|`REVOKED`\|`EXPIRED`), `rowHashHex` (stored digest, excluded from its own preimage), `rotatedFromKeyId` (nullable) |
| Format / schema (lifecycle receipt row) | `transitionId` (string, stable identity), `keyId`, `registrySnapshotVersionBefore`, `registrySnapshotVersionAfter`, `priorStatus`, `newStatus`, `actor` (Party A identity), `timestamp` (RFC 3339), `priorEntryHashHex` (`null` at genesis), `entryHashHex` (stored digest, excluded from its own preimage) |
| Duplicate/alias rejection | reject a write that would create a second row with the same `keyId`; reject a write whose `publicKeyBytesBase64` already exists under a different `keyId` (public-key alias) |
| Stable source identity | `keyId` (per row); `registrySnapshotId` (per registry envelope) |
| Monotonic version/snapshot identity | `registrySnapshotVersion`, incremented on every registry write |
| Accountable owner | Party A (`CVF Operator / repository owner`), per Contract 1 |
| Write principal | Party A exclusively for the registry; Party A exclusively for lifecycle-receipt entries (the actor of its own transitions) |
| Allowed readers | any G1 verifier performing `SignatureValidityCheck`; Party B for observation-only reads |
| Forbidden roles | Party B may not write; Party C may not write or read for its own issuer purposes |
| Canonicalization / hashing rule | `cvf.source-record-canonicalization@1`; registry row preimage domain `cvf.keyRegistryRow`; lifecycle-receipt preimage domain `cvf.keyLifecycleReceipt`; see Canonicalization Profile above |
| Lifecycle / state transitions | `generation_or_import` to `ACTIVE`; `ACTIVE` to `ROTATING` to `REVOKED` or `EXPIRED`; terminal states are final |
| Durable receipt | one append-only `LIFECYCLE_LOG.jsonl` entry per transition, hash-chained via `priorEntryHashHex`/`entryHashHex` |
| Correction, rotation, supersession, revocation | only Party A may initiate; a rotation creates a new `keyId` with `rotatedFromKeyId` set; no in-place rewrite of an existing row's key bytes |
| Named verifier consumer | G1 verifier `SignatureValidityCheck` (T2C pseudocode) |
| Validation order and failure taxonomy | (1) registry reachable, (2) exactly one `keyId` match (reject on missing, duplicate-ID, or public-key-alias), (3) `status == ACTIVE`, `issuedAt <= receiptIssuanceTimeUtc`, `expiresAt` unset or `> observationTimeUtc`, `revokedAt` unset or `> receiptIssuanceTimeUtc`, (4) `role.authorizesIssuanceFor(verificationAuthority)` true, (5) signature valid against `publicKeyBytesBase64`; any failed step is `REJECT`, never `PASS_WITH_WARNING` |
| Establishment evidence required | (a) registry path exists and is CVF-governed, (b) Party A write access proven, (c) at least one verifier consumer reads it, (d) lifecycle log exists, hash-chain verifies, and matches, (e) Local independently verifies (a)-(d) |
| Disposition | `SOURCE_NOT_CREATED`; admission `UNVERIFIED` |

### Source Group 2: Versioned Verification-Authority Specification And Independent Activation-Decision Record

| Field | Value |
|---|---|
| Proposed exact future path (specification) | `governance/sources/verification_authority_spec/SPEC_v{n}.json`, one immutable file per version (`PROPOSED_LOCAL_REVIEW`) |
| Proposed exact future path (decision events) | `governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl`, append-only (`PROPOSED_LOCAL_REVIEW`) |
| Format / schema (spec file) | `specVersion` (monotonic integer), `canonicalBytesBase64`, `authorId` (Party A identity), `proposedAt` (RFC 3339), `specHashHex` (SHA-256 of `canonicalBytesBase64` decoded bytes only; see Two Distinct Group 2 Hashes below), `specFileRecordHashHex` (stored digest, excluded from its own preimage) |
| Format / schema (decision event row) | `decisionEventId` (string, stable identity), `eventType` (`APPROVED`\|`REJECTED`\|`ACTIVATED`\|`SUPERSEDED`), `specVersion`, `recomputedHashHex`, `approverId` (activation-approver identity), `decidedAt` (RFC 3339), `priorEntryHashHex` (`null` at genesis), `entryHashHex` (stored digest) |
| Stable source identity | `specVersion` (spec file); `decisionEventId` (decision event) |
| Monotonic version/snapshot identity | `specVersion` doubles as the version identity; `verificationAuthorityHash` == `specHashHex` |
| Accountable owner | Party A, per Contract 2, for authorship; the independent activation approver for every decision event |
| Write principal | Party A exclusively for new `SPEC_v{n}.json` files; the activation approver exclusively for `ACTIVATION_DECISIONS.jsonl` rows |
| Allowed readers | verifier consumers binding to an active `verificationAuthorityHash`; Local for review |
| Forbidden roles | Party A cannot append a decision event for its own authored version (Cross-Source Identity And Access Matrix, Case 4); Party C is excluded from both files |
| Canonicalization / hashing rule | Two distinct hashes, see Two Distinct Group 2 Hashes above: `specHashHex` is the direct SHA-256 of `canonicalBytesBase64` decoded bytes (not under the `cvf.source-record-canonicalization@1` profile); `specFileRecordHashHex` is the `cvf.specFile` domain's closed-preimage digest under `cvf.source-record-canonicalization@1`. Decision-event preimage domain `cvf.specDecisionEvent`; see Canonicalization Profile above. The approver must independently recompute `specHashHex` from `canonicalBytesBase64` rather than trust a caller-supplied value |
| Lifecycle / state transitions | `draft` (spec file created) then exactly one `APPROVED` or `REJECTED` decision event, then (only from `APPROVED`) exactly one `ACTIVATED` decision event, then later exactly one `SUPERSEDED` decision event when a newer version activates |
| Durable receipt | the decision event row itself, immutable once appended, hash-chained via `priorEntryHashHex`/`entryHashHex` |
| Correction, rotation, supersession, revocation | a new `specVersion` requires its own `APPROVED` then `ACTIVATED` event; no in-place edit of `canonicalBytesBase64` for an existing version |
| Named verifier consumer | T2C `LookupProvenanceCheck` pseudocode, which reads `expectedAuthorityHash` (bound to the current `ACTIVATED` specification's `specHashHex`) |
| Validation order and failure taxonomy | (1) exactly one `ACTIVATED` decision event exists for the cited `specVersion` with no later `SUPERSEDED` event for that same version, (2) recomputed `specHashHex` matches `verificationAuthorityHash`, (3) `approverId` differs from `authorId`, (4) exactly zero or one specification is active across the whole `ACTIVATION_DECISIONS.jsonl` history at query time; any failed step, including two simultaneously active versions, is `REJECT`, never resolved by latest timestamp or largest version |
| Establishment evidence required | (a) spec document path exists, (b) an `ACTIVATED` decision event exists with an `approverId` distinct from `authorId`, (c) at least one verifier consumer binds to the resulting hash, (d) Local independently recomputes the hash and confirms the match, (e) the unique-active invariant holds across the full decision-event history |
| Disposition | `SOURCE_NOT_CREATED`; admission `UNVERIFIED` |

#### Explicit Approval, Activation And Supersession (T2F-R1-04)

Replaces the initial return's automatic "most recent approved becomes active"
rule, which the R1 review found to contradict fail-closed conflict handling.

- Approval never implies activation. A specification version that is
  `APPROVED` remains inactive until a **separate** `ACTIVATED` decision event
  is appended by the activation approver.
- Only the independently appointed activation approver may append an
  `ACTIVATED` or `SUPERSEDED` event, and only over an exact `specVersion` plus
  its independently recomputed `specHashHex`. Party A may never append either
  event type (self-activation is rejected, per Cross-Contract Separation
  Matrix Case 4 and the activation-approver appointment's forbidden
  combination).
- Deterministic ordering: decision events for a given `specVersion` must occur
  in the order `APPROVED` (or `REJECTED`, terminal) then optionally
  `ACTIVATED` then optionally `SUPERSEDED`. An `ACTIVATED` event appended
  without a prior `APPROVED` event for that `specVersion` is invalid and
  rejected.
- Immutable decision identity: each `decisionEventId` is unique and, once
  appended, is never edited, reordered or deleted; a correction is a new
  event, not an edit.
- Unique-active invariant: at any query time, scanning the full
  `ACTIVATION_DECISIONS.jsonl` history for `ACTIVATED` events not yet followed
  by a `SUPERSEDED` event for the same `specVersion` must yield exactly zero
  or exactly one result. Two simultaneous `ACTIVATED`-without-`SUPERSEDED`
  results for different versions is a conflict state.
- Conflict resolution is never automatic. Two active heads, duplicate or
  contradictory decision events for the same `specVersion`, an author
  attempting self-activation, or a decision event whose `recomputedHashHex`
  does not match the cited spec file's `specHashHex` must all be rejected by
  the verifier consumer. Resolution requires a new, Local-reviewed
  `SUPERSEDED` event explicitly naming which version remains active; the
  verifier never resolves a conflict by latest timestamp or largest version
  number.

### Source Group 3: Tamper-Evident Append-Only Observation Log Covering Both Registries

| Field | Value |
|---|---|
| Proposed exact future path | `governance/sources/registry_observation_log/LOG.jsonl` (`PROPOSED_LOCAL_REVIEW`) |
| Format / schema | one JSON object per line: `snapshotId` (string, immutable, globally unique, never reused or aliased -- the value T2C's `sourceObservationLog.lookup(snapshotId)` keys on; see Immutable Snapshot Identity below), `registryName` (`verifier_key_registry`\|`issuer_registry`), `registrySnapshotVersion`, `snapshot_content` (exactly one fixed stored representation: raw UTF-8 registry-snapshot JSON bytes encoded as base64url with no padding; never a bare artifact reference or unencoded text; excluded from the record-hash preimage and bound through `snapshotHashHex`), `snapshotHashHex` (SHA-256 of strictly decoded `snapshot_content` bytes), `observedAt` (RFC 3339, T2C's `observation.observedAt`), `authority` (string, T2C's `observation.authority`, compared against `receipt.verificationAuthority`), `observerIdentity` (Party B), `priorEntryHashHex` (`null` at genesis), `entryHashHex` (stored digest). The observation-log adapter strictly decodes the stored field before returning `observation.snapshot_content` as bytes to T2C; T2C itself hashes those bytes without a decoding step. |
| Stable source identity | `snapshotId` alone; there is no separate per-line identity, because each `snapshotId` corresponds to exactly one durable record for the life of the log |
| Monotonic version/snapshot identity | `(registryName, registrySnapshotVersion, observedAt)` tuple per entry; the log itself is hash-chained via `priorEntryHashHex`/`entryHashHex` |
| Accountable owner | Party B (`CVF Independent Registry Observer / dedicated separate audit identity`), per Contract 3, scoped to both registries |
| Write principal | Party B exclusively; append-only, never mutates or deletes a prior line |
| Allowed readers | T2C `sourceObservationLog.lookup(snapshotId)` and `.countObservationsFor(snapshotId)` consumers; Local for audit |
| Forbidden roles | Party A may not write to this log for the key registry it writes; Party C may not write to this log for the issuer registry it writes (Cross-Source Identity And Access Matrix, Case 1) |
| Canonicalization / hashing rule | `cvf.source-record-canonicalization@1`; preimage domain `cvf.observationLogEntry`; see Canonicalization Profile above |
| Lifecycle / state transitions | `observed` (appended once for a given `snapshotId`); terminal and immutable; no `corrected`, `superseded`, or any other transition exists for an existing `snapshotId`; see Immutable Snapshot Identity below |
| Durable receipt | the hash-chained log line itself |
| Correction, rotation, supersession, revocation | none, ever, for an existing `snapshotId`. An incorrect or stale observation is never repaired in place. Party B instead records a new observed snapshot under a brand-new `snapshotId`, and a verifier issues a new receipt bound to that new ID and its hash; the old record and any receipt bound to the old ID remain durable, unchanged, and are never rebound. See Immutable Snapshot Identity below |
| Named verifier consumer | T2C `sourceObservationLog.lookup(snapshotId)` and `.countObservationsFor(snapshotId)` |
| Validation order and failure taxonomy | (1) log reachable, (2) hash chain verifies from genesis to the cited line, (3) `observerIdentity` differs from the registry's write principal for `registryName`, (4) exactly one record bears the cited `snapshotId` (see Immutable Snapshot Identity below), (5) `snapshotHashHex` matches recomputed `sha256(base64url_decode(snapshot_content))`, (6) `observedAt` not stale beyond the bound Contract 2 activated specification's freshness field, or Local-set fallback if none is bound; any failed step is `REJECT` |
| Establishment evidence required | (a) log path exists, (b) Party B independence from both registry writers proven, (c) at least one verifier consumer reads it, (d) hash-chain tamper-evidence verified, (e) write-time duplicate-`snapshotId` rejection proven, (f) Local independently verifies (a)-(e) |
| Disposition | `SOURCE_NOT_CREATED`; admission `UNVERIFIED` |

#### Immutable Snapshot Identity (T2G-01 through T2G-05)

This subsection replaces the prior same-`snapshotId` correction/fork-merge
model entirely. R1 permitted multiple unresolved observations per snapshot.
R2 introduced a `correctionOf` array to merge forks under one shared ID. R3
found R2's merge semantics silently diverged from T2C's literal count and
added a liveness rule that a Local reviewer then found self-contradicting
against R3's own regression test. The operator, after that second escalation,
selected a materially simpler architecture: **no correction, merge, or
active-head resolution mechanism exists for an existing `snapshotId` at all.**
A `snapshotId` is a write-once, immutable identity. There is exactly one
record per ID, permanently, or the ID does not exist yet.

**T2G-01: uniqueness and single-binding.** `snapshotId` is generated fresh
for every genuinely new observed snapshot (recommended: a cryptographically
random identifier chosen by Party B at observation time; a hash of metadata
alone is insufficient because distinct observations can share that metadata).
The write path rejects, at write time, any attempt to
append a second record bearing an already-used `snapshotId`; the duplicate
attempt never enters the durable log. Exactly one Party B original
observation is therefore ever bound to one `snapshotId`, with exactly one
`snapshot_content`/`snapshotHashHex` pair.

**T2G-02: no correction/merge vocabulary remains normative.** No `entryKind`,
`correctionOf`, active-head, multi-parent, or same-ID fork-resolution field,
rule, or algorithm exists in the current schema or in any dependent matrix,
checklist, or negative-case table below. Every remaining mention of that
vocabulary in this document is confined to this historical-explanation
paragraph and the Finding-To-Repair Locator Ledger's finding descriptions,
which describe rejected prior designs, never a current rule.

**T2G-03: error and staleness handling via new IDs, never in-place repair.**
If Party B's original observation is later found erroneous, or the observed
registry content genuinely changes, no correction, supersession, or
in-place repair of the existing `snapshotId`'s record is ever performed.
Party B appends a wholly new record under a freshly generated `snapshotId`,
with its own new `snapshot_content`/`snapshotHashHex`/`observedAt`. A
verifier that needs the corrected or current state issues a new receipt
bound to the new `snapshotId` and its hash. Any receipt previously issued
against the old `snapshotId` remains bound to that old ID and its original
`snapshotHashHex`/`observedAt` forever. The receipt cannot be rewritten to
cite the new ID/hash without invalidating its signature; no implicit
rebinding occurs. T2C's `LookupProvenanceCheck` has no caller-supplied
expected-current-snapshot-ID input: an unchanged old receipt may still verify
against its old observation while its round and freshness window remain
valid. A new snapshot alone does not revoke it. Rejection of an old receipt
requires an existing T2C condition such as round mismatch, stale observation,
or a genuine lookup-result mismatch; this contract does not assert an
immediate-revocation rule that T2C does not implement.

**T2G-04: `lookup`/`countObservationsFor` are literal record counts, not
head resolution.** `lookup(snapshotId)` returns the sole record bearing that
exact `snapshotId`, or nothing if no record bears it; there is no active-head
computation, because there is nothing to resolve among -- at most one record
can ever legitimately exist per ID. `countObservationsFor(snapshotId)`
counts every durable record bearing that exact `snapshotId` (which, under a
correctly functioning write-time uniqueness check, is always `0` or `1`) and
returns that literal count; it never excludes, merges, or otherwise
special-cases any record as "historical" or "superseded," because no such
category exists. If a duplicate-ID record were ever to reach the durable log
despite the write-time check (log corruption, a bypassed write path, or a
bug), `countObservationsFor` returns `2` (or more), `LookupProvenanceCheck`'s
existing `> 1` check fails closed with `FORKED_OBSERVATION`/`UNVERIFIED`
exactly as T2C already specifies, and this is never treated as two valid
observations to be administratively merged; it is treated as a fault in the
write-time uniqueness guarantee, requiring a separate, Local-reviewed
integrity investigation of the log, not a merge.

**T2G-05: `snapshot_content` remains one fixed representation.** As stated
in the schema row above, `snapshot_content` is exactly one representation
(base64url-encoded raw JSON bytes, no padding); `snapshotHashHex` hashes the
decoded bytes; the observation-log adapter returns those bytes to T2C via
`observation.snapshot_content`, never the encoded string or an unresolved
reference. Strict decoding rejects padding, whitespace, non-base64url
characters, noncanonical encodings, and invalid UTF-8/JSON before a record
is admitted. For a reproducible illustrative snapshot, the exact UTF-8
preimage bytes are `{"registrySnapshotVersion":2}` (29 bytes), the stored
unpadded base64url value is
`eyJyZWdpc3RyeVNuYXBzaG90VmVyc2lvbiI6Mn0`, and SHA-256 of the decoded
29 bytes is
`ecaddf2e1d99632e213b69f00240de3e4414ba3be1253a40946374624dd9949e`.
The padded mutation `eyJyZWdpc3RyeVNuYXBzaG90VmVyc2lvbiI6Mn0=` is
rejected as malformed, not silently normalized. This is a design vector,
not an assertion that a source snapshot exists.

**Documentary replacement pointer (optional, non-normative).** A future
implementation may optionally record, purely as documentary provenance, that
a new `snapshotId` was created because a specific prior `snapshotId` was
found erroneous or stale (for example an out-of-band audit note or a
`replacesSnapshotId` field carried only in an operational runbook, never in
the `cvf.observationLogEntry` closed preimage). Any such pointer is
informational only: it changes no identity, no receipt binding, no count
semantics, and no admission outcome. `lookup` and `countObservationsFor`
never read it, and a verifier consumer must never treat it as a lookup
alias, an implicit rebinding of an old receipt, or evidence that the old
`snapshotId`'s record is invalid. This document does not add such a field to
the closed preimage list; it is recorded here only to state explicitly that
one may exist outside the hashed schema without changing any semantic above.

**Concrete tests (T2G-01, T2G-03, T2G-04).**

| Step | Action | `countObservationsFor` result | Outcome |
|---|---|---|---|
| 1 | Party B appends one original record for `snapshotId = SNAP-0001` | `1` | `lookup("SNAP-0001")` returns that sole record; unambiguous |
| 2 | A second write attempt reuses `snapshotId = SNAP-0001` | rejected at write time; never appended | the durable log is unchanged; `countObservationsFor("SNAP-0001")` still returns `1` |
| 3 (integrity-fault case) | a duplicate-ID record is hypothetically forced into the log bypassing the write-time check | `2` | `LookupProvenanceCheck`'s existing `> 1` check returns `UNVERIFIED` (`FORKED_OBSERVATION`); no administrative merge is performed; this is treated as a log-integrity fault requiring separate Local investigation |
| 4 | the registry content genuinely changes; Party B appends a new original record under `snapshotId = SNAP-0002` | `countObservationsFor("SNAP-0001") = 1`; `countObservationsFor("SNAP-0002") = 1` | both IDs remain independently resolvable; `SNAP-0001`'s record is untouched |
| 5 | a verifier receipt issued against `SNAP-0001` is offered as evidence for `SNAP-0002` | not applicable to `countObservationsFor` | the signed receipt still cites `SNAP-0001`; modifying it to cite `SNAP-0002` invalidates its signature. Unmodified, it is checked only against `SNAP-0001` and may still verify while its round/freshness conditions hold; a new ID alone does not force `UNVERIFIED` |
| 6 | `lookup("SNAP-9999")` for an ID that was never observed | `0` | `lookup` returns nothing; `UNVERIFIED`, matching T2C's `if not observation: return UNVERIFIED` |

Verified programmatically (direct simulation, run twice independently):
step 1 yields count `1` and a resolvable lookup; step 2's rejected duplicate
leaves the count at `1`, unchanged; step 3's hypothetical bypass yields count
`2`, matching T2C's existing fail-closed `> 1` branch with no merge path
available to reach it; step 4 confirms two distinct IDs coexist
independently with no cross-effect; step 6 confirms a missing ID yields
count `0`. This is a strict simplification of, not a new special case beyond,
the T2C interface: `lookup` and `countObservationsFor` keep exactly the
signatures and return-shape T2C already calls, with a materially simpler,
directly reproducible resolution rule replacing the rejected correction
model.

**T2C interface reconciliation.** T2C's `LookupProvenanceCheck` comment
("exactly one source-owned observation may exist for this snapshot
identity; more than one is ambiguous") is satisfied exactly and literally:
under the write-time uniqueness guarantee, `countObservationsFor(snapshotId)`
is always `0` or `1` for any legitimately reachable state, and the existing
`> 1` fail-closed branch is preserved unchanged for the fault case. No
amendment to the accepted T2C pseudocode text is required; T2C's `lookup`
and `countObservationsFor` signatures, return shapes, and every other
predicate (hash, temporal ordering, freshness, authority match) are
unchanged by this design.

### Source Group 4: Issuer Registry, Real Lookup Semantics, And Durable Lookup-Response Records

| Field | Value |
|---|---|
| Proposed exact future path (registry) | `governance/sources/issuer_registry/REGISTRY.json` (`PROPOSED_LOCAL_REVIEW`) |
| Proposed exact future path (lookup responses) | `governance/sources/issuer_registry/LOOKUP_RESPONSES.jsonl` (`PROPOSED_LOCAL_REVIEW`) |
| Format / schema (registry envelope) | JSON object: `registrySnapshotId` (global snapshot identity), `registrySnapshotVersion` (monotonic integer), `writeTimestamp`, `rows` (array of issuer rows) |
| Format / schema (issuer row) | `issuerIdentity` (stable identity), `entryVersion` (monotonic integer per `issuerIdentity`), `issuerAttestedHash`, `canonicalContentHashHex` (SHA-256 of the issuer's canonical content bytes, recomputed by the registry, distinct from the issuer's own attested hash), `status` (`registered`\|`ACTIVE`\|`corrected`\|`REVOKED`), `registeredAt`/`correctedAt`/`revokedAt` |
| Format / schema (lookup response row) | `lookupId` (stable identity), `issuerIdentity`, `claimedIssuerHash` (the `issuerAttestedHash` the caller supplied), `registrySnapshotId`, `registrySnapshotHashHex`, `registrySnapshotVersion`, `entryVersion`, `result` (`IDENTITY_CONFIRMED`\|`IDENTITY_REJECTED`\|`IDENTITY_UNRESOLVED`), `errorCode` (nullable, populated only when `result` is `IDENTITY_UNRESOLVED`), `queriedAt`, `consumerIdentity`, `observedSnapshotId` (the immutable Group 3 `snapshotId` whose `snapshot_content` was consulted for this response), `priorEntryHashHex` (`null` at genesis), `entryHashHex` (stored digest) |
| Stable source identity | `issuerIdentity` (registry row); `lookupId` (response row) |
| Monotonic version/snapshot identity | `entryVersion` per `issuerIdentity`; `registrySnapshotVersion` for the whole registry envelope |
| Accountable owner | Party C (`CVF Issuer Registry Authority / dedicated issuer-governance identity`), per Contract 4 |
| Write principal | Party C exclusively for the registry; the lookup path itself appends to `LOOKUP_RESPONSES.jsonl` on every real query |
| Allowed readers | verifier consumers calling `sourceRegistry.lookup(issuerIdentity, issuerAttestedHash, snapshot_content)`; Party B for observation-only reads |
| Forbidden roles | Party C's own status assertion cannot satisfy correction/revocation evidence without independent observation (Cross-Source Identity And Access Matrix, Case 5); Party A is excluded from this registry |
| Canonicalization / hashing rule | `cvf.source-record-canonicalization@1`; registry-row preimage domain `cvf.issuerRegistryRow`; lookup-response preimage domain `cvf.issuerLookupResponse`; see Canonicalization Profile above. `issuerAttestedHash` is caller-supplied and never trusted alone; the registry independently recomputes `canonicalContentHashHex` and a lookup response must compare that recomputed value, not the caller's claim |
| Lifecycle / state transitions | `registered` to `ACTIVE` to `corrected` (new `entryVersion`, same `issuerIdentity`) or `REVOKED`; `REVOKED` is terminal |
| Durable receipt | one `LOOKUP_RESPONSES.jsonl` line per real query, immutable once appended, hash-chained via `priorEntryHashHex`/`entryHashHex` |
| Correction, rotation, supersession, revocation | Party C initiates; the route must produce independent Party B observation evidence, not a bare Party C status flip alone |
| Named verifier consumer | T2C `LookupProvenanceCheck` pseudocode call `sourceRegistry.lookup(issuerIdentity, issuerAttestedHash, snapshot_content)`, which evaluates the issuer identity together with its attested hash against the observed snapshot content |
| Validation order and failure taxonomy | (1) registry reachable, else `result: IDENTITY_UNRESOLVED`, (2) exactly one `issuerIdentity` match at the current `entryVersion`, else `IDENTITY_UNRESOLVED`, (3) status `ACTIVE`, else `IDENTITY_REJECTED`, (4) recomputed `canonicalContentHashHex` matches the caller-supplied `issuerAttestedHash` evaluated against `snapshot_content`, else `IDENTITY_REJECTED`, (5) an independent Party B observation (Group 3 record identified by `observedSnapshotId`) exists and is bound into the response; any unreachable, ambiguous, or unresolvable condition returns `IDENTITY_UNRESOLVED` rather than defaulting to confirmed |
| Establishment evidence required | (a) registry/lookup path exists distinct from the rejected posture checker, (b) Party C write access proven, (c) at least one verifier consumer performs a real lookup call, (d) evidence that correction/revocation required more than Party C's own assertion, (e) every lookup response binds a real `observedSnapshotId`, (f) Local independently verifies (a)-(e) |
| Disposition | `SOURCE_NOT_CREATED`; admission `UNVERIFIED` |

## Cross-Source Identity And Access Matrix

| Case | Pattern | Groups involved | Disposition |
|---|---|---|---|
| 1 | writer of a registry also independently observes/attests to that same registry | 1 plus 3 for the key registry; 4 plus 3 for the issuer registry | `CIRCULAR_AUTHORITY_REJECTED` |
| 2 | authority-specification author also acts as issuer authority attesting to it | 2 plus 4 | `CIRCULAR_AUTHORITY_REJECTED` |
| 3 | same party both appends the observation log and can mutate the registry it observes without a distinguishable role boundary | 3 self-combination | `CIRCULAR_AUTHORITY_REJECTED` |
| 4 | specification author certifies its own hash as independently trusted evidence | 2 self-combination | `CIRCULAR_AUTHORITY_REJECTED` |
| 5 | issuer's own unverified assertion treated as a genuine lookup or correction result | 4 self-combination | `CIRCULAR_AUTHORITY_REJECTED` |
| 6 | stale evidence presented as current | 1, 2, 3, 4 | fail-closed reject, no exception |
| 7 | evidence source unavailable at verification time | 1, 2, 3, 4 | fail-closed reject, no exception |
| 8 | conflicting versions of the same evidence both claim active (two `ACTIVATED`-without-`SUPERSEDED` decision events for Group 2; a duplicate-`snapshotId` integrity fault for Group 3, per Immutable Snapshot Identity; two `ACTIVE` Group 4 entry versions) | 2, 3, 4 | fail-closed reject; for Group 2, resolution requires a Local-reviewed `SUPERSEDED` decision event, never automatic latest-wins; for Group 3, a duplicate-ID fault is a log-integrity issue requiring separate Local investigation, never an administrative merge |
| 9 | emergency override bypassing normal admission evidence | 1, 2, 3, 4 | `NO_EMERGENCY_PATH`; any future emergency route must be a separately governed, Local-reviewed packet |
| 10 | Party A holds both Contract 1 and Contract 2 under explicit operator acceptance | 1 plus 2 | `PERMITTED_WITH_EXPLICIT_OPERATOR_ACCEPTANCE`; already recorded in the Party A appointment |
| 11 | Party B observes both registries as one identity | 3 spanning key and issuer registries | `PERMITTED_WITH_EXPLICIT_OPERATOR_ACCEPTANCE`; already recorded in the Party B appointment, provided Party B remains distinct from both writers |
| 12 | activation approver collapses with Party A, B, or C | 2 activation authority | `CIRCULAR_AUTHORITY_REJECTED`; already recorded as a required-independence row in the activation-approver appointment |

## T2C Consumer-Binding Table (T2F-R1-03)

Every row below cites the exact T2C input, the exact T2F source field now
providing it, and the exact failure result when the field is missing,
mismatched, stale or ambiguous. This replaces the initial return's narrative
similarity claim with field-for-field joins.

| T2C input (from `SignatureValidityCheck` / `LookupProvenanceCheck`) | Exact T2F source field | Failure result if missing/mismatched |
|---|---|---|
| `receipt.signedBy.keyId` / `signatureKeyId` resolution | Group 1 key row `keyId`, exact match, duplicate/alias rejection | `false` (Predicate 2 fails); UNVERIFIED |
| `keyRecord.status == "ACTIVE"`, `issuedAt`, `expiresAt`, `revokedAt` | Group 1 key row `status`, `issuedAt`, `expiresAt`, `revokedAt` | `false` (key lifecycle check fails) |
| `keyRecord.role.authorizesIssuanceFor(verificationAuthority)` | Group 1 key row `role` | `false` (role does not authorize issuance) |
| `expectedAuthorityHash` binding | Group 2 current `ACTIVATED` decision event's cited `specVersion` -> spec file `specHashHex` | UNVERIFIED (`AUTHORITY_HASH_MISMATCH`) if no active spec, or recomputed hash differs |
| `sourceObservationLog.lookup(snapshotId)` -> `observation` | Group 3's sole immutable record bearing that exact `snapshotId` (see Immutable Snapshot Identity) | UNVERIFIED (no observation) if zero records bear that ID |
| `observation.snapshot_content` | Group 3 record's `snapshot_content` | N/A (direct field) |
| `sha256(observation.snapshot_content) == snapshotHash` | Group 3 record's `snapshotHashHex`, recomputed | UNVERIFIED (hash mismatch; snapshot altered) |
| `observation.observedAt` (temporal order, freshness) | Group 3 record's `observedAt` | UNVERIFIED (`INVALID_TIME_ORDER` or `STALE_SNAPSHOT`) |
| `observation.authority == receipt.verificationAuthority` | Group 3 record's `authority` | UNVERIFIED (authority mismatch) |
| `sourceObservationLog.countObservationsFor(snapshotId) > 1` | literal count of Group 3 records bearing that exact `snapshotId` (always 0 or 1 under the write-time uniqueness guarantee; see Immutable Snapshot Identity) | UNVERIFIED (`FORKED_OBSERVATION`) on the fault case only |
| `sourceRegistry.lookup(issuerIdentity, issuerAttestedHash, snapshot_content)` | Group 4 lookup response `result` field, computed against Group 3's `snapshot_content` | UNVERIFIED (`IDENTITY_UNRESOLVED`) on unreachable/ambiguous; `IDENTITY_REJECTED` on hash/status mismatch |
| `registryLookupResult != receipt.lookupResult` | Group 4 lookup response `result` compared to the receipt's claimed `lookupResult` | UNVERIFIED (lookup result does not match registry state) |

## Negative Probes (T2F-R1-03)

| Probe | Scenario | Required fail-closed behavior |
|---|---|---|
| missing snapshot | `sourceObservationLog.lookup(snapshotId)` finds zero records bearing that ID | UNVERIFIED; never treated as confirmed |
| duplicate-ID write attempt | a write appends a second record for a `snapshotId` that already has one durable record | rejected at write time; the durable log is unchanged; the attempted duplicate never appears in `countObservationsFor` |
| duplicate-ID integrity fault (bypassed write check) | `countObservationsFor(snapshotId)` finds more than one record bearing the same `snapshotId` despite the write-time check | UNVERIFIED (`FORKED_OBSERVATION`); no administrative merge; treated as a log-integrity fault requiring separate Local investigation, never resolved by a correction/merge entry |
| hash mismatch | recomputed `sha256(base64url_decode(snapshot_content))` differs from `snapshotHashHex` | UNVERIFIED; snapshot treated as altered |
| stale observation | `observedAt` older than the freshness bound bound to the Group 2 active specification | UNVERIFIED (`STALE_SNAPSHOT`) |
| wrong authority | Group 3 entry `authority` differs from the receipt's `verificationAuthority` | UNVERIFIED (authority mismatch) |
| old-receipt substitution for a new snapshot | a receipt signed for the old `snapshotId` is altered to cite a newer ID/hash | signature verification fails; if left unaltered, T2C evaluates only the old ID and may verify it until round/freshness or another existing predicate fails; no implicit rebinding or immediate revocation is claimed |
| malformed snapshot encoding | stored `snapshot_content` has forbidden padding, whitespace, invalid alphabet, noncanonical base64url, or invalid decoded UTF-8/JSON | reject before hashing or returning `observation.snapshot_content`; never normalize malformed input into an accepted observation |
| wrong key role | Group 1 key row `role` does not authorize issuance for the cited `verificationAuthority` | reject at Predicate 2 before signature verification |
| duplicate key/alias | Group 1 registry write would create a duplicate `keyId` or a public-key alias | reject at write time; registry never stores the duplicate |
| response-to-snapshot mismatch | Group 4 lookup response's `observedSnapshotId` does not reference the `snapshotId` actually used for the query | reject; response is not bound to the queried snapshot, treated as `IDENTITY_UNRESOLVED` |

## Source-To-Consumer Binding Matrix

| Source group | Consumer contract | Consumer call | Binding requirement |
|---|---|---|---|
| 1: key registry | G1 verifier | `SignatureValidityCheck` (T2C pseudocode) | consumer resolves `keyId` to `status: ACTIVE`, checks `role.authorizesIssuanceFor(...)`, before trusting a signature |
| 2: authority specification | G1 verifier | `LookupProvenanceCheck` reading `expectedAuthorityHash` | consumer binds only to a hash with a current `ACTIVATED` (not `SUPERSEDED`) `ACTIVATION_DECISIONS.jsonl` event |
| 3: observation log | G1 verifier | `sourceObservationLog.lookup(snapshotId)`, `.countObservationsFor(snapshotId)` | consumer rejects if zero or more than one durable record bears the cited immutable `snapshotId` |
| 4: issuer registry | G1 verifier | `sourceRegistry.lookup(issuerIdentity, issuerAttestedHash, snapshot_content)` | consumer rejects on unreachable, ambiguous, or hash-mismatched response; never defaults to confirmed |

## Version / Snapshot / Canonical Hash Matrix

| Source group | Version field | Snapshot identity | Canonical hash rule |
|---|---|---|---|
| 1: key registry | `registrySnapshotVersion` (monotonic integer) | `(registrySnapshotId, registrySnapshotVersion, writeTimestamp)` | `cvf.source-record-canonicalization@1`, domain `cvf.keyRegistryRow` |
| 2: authority specification | `specVersion` (monotonic integer) | `(specVersion, decisionEventId, decidedAt)` | `verificationAuthorityHash` = `specHashHex` = SHA-256 of `canonicalBytesBase64` decoded bytes |
| 3: observation log | `registrySnapshotVersion` per entry | `(snapshotId, registryName, registrySnapshotVersion, observedAt)` | `cvf.source-record-canonicalization@1`, domain `cvf.observationLogEntry` |
| 4: issuer registry | `entryVersion` (monotonic integer per `issuerIdentity`) | `(issuerIdentity, entryVersion)` | `cvf.source-record-canonicalization@1`, domain `cvf.issuerRegistryRow`; caller-supplied `issuerAttestedHash` always independently recomputed as `canonicalContentHashHex` |

## Establishment Evidence Checklist

- [ ] Group 1: governed registry path exists; Party A write access proven; at least one verifier consumer reads it; lifecycle log exists, hash-chain verifies, and matches; Local independently verifies.
- [ ] Group 2: governed spec path exists; an `ACTIVATED` decision event exists with an `approverId` distinct from `authorId`; the unique-active invariant holds; a verifier consumer binds to the resulting hash; Local independently recomputes the hash.
- [ ] Group 3: governed log path exists; Party B independence from both registry writers proven; a verifier consumer reads it; hash-chain tamper-evidence verified; write-time duplicate-`snapshotId` rejection proven; Local independently verifies.
- [ ] Group 4: governed registry/lookup path exists distinct from the rejected posture checker; Party C write access proven; a verifier consumer performs a real lookup call; every lookup response binds a real Group 3 `observedSnapshotId`; correction/revocation evidence requires more than Party C's own assertion; Local independently verifies.
- [ ] Cross-source: no case in the Cross-Source Identity And Access Matrix is violated by the concrete principals eventually provisioned.
- [ ] Every row above remains `SOURCE_NOT_CREATED` until Local checks the box after independent verification; this audit checks none of them.

## Negative Cases

| Case | Scenario | Required fail-closed behavior |
|---|---|---|
| self-approval | Party A attempts to append an `ACTIVATED` decision event for its own authored specification version | reject; `approverId` must differ from `authorId` |
| writer/self-observation | Party A or Party C attempts to append an observation-log entry for the registry it writes | reject at write time; Party B is the sole observation-log write principal |
| issuer self-verification | Party C's own new status assertion is presented as correction/revocation proof | reject; require an independent Party B observation entry for the same `entryVersion` |
| stale evidence | a verifier consumer receives an observation or lookup response older than the freshness bound bound to the Group 2 active specification | reject; never assume freshness by default |
| unavailable evidence | the key registry, specification decision file, observation log, or issuer registry is unreachable at verification time | reject; unavailability is never a pass-through |
| conflicting evidence | two `ACTIVATED`-without-`SUPERSEDED` Group 2 decision events, or two `ACTIVE` Group 4 issuer entry versions, both claim active | reject; Group 2 requires a Local-reviewed `SUPERSEDED` decision event, never automatic latest-wins trust; Group 3's immutable `snapshotId` design makes this class of conflict structurally impossible per-ID (see Immutable Snapshot Identity), so it applies only to Groups 2 and 4 |
| in-place history rewrite | any attempt to edit a published `SPEC_v{n}.json`, a prior observation-log line, or an issuer registry row's history in place | reject; every source is append-only or version-superseding, never mutated in place |
| caller-supplied unbound hash | a verifier consumer receives `expectedAuthorityHash` or `issuerAttestedHash` from the caller without independent recomputation | reject; the consumer must recompute the hash from the cited canonical bytes, not trust a caller-supplied value |
| emergency bypass | any proposed emergency override that would admit a candidate without the Establishment Evidence Checklist | reject; `NO_EMERGENCY_PATH` per Cross-Source Identity And Access Matrix, Case 9 |

## Literal Proposed-Path Collision Ledger (T2F-R1-05)

Executed as a dedicated per-path/family check, distinct from the generic
tranche-token query in Scope / Methodology, which cannot detect collisions
for these specific operational paths. Absence at these exact paths is
evidence of no current collision; it is not creation, implementation, or
source-existence proof.

| Proposed path/family | `Test-Path -LiteralPath` result | Token searched | `rg -n --hidden --no-ignore -F` roots | Matches | Collision classification | Local-review disposition |
|---|---|---|---|---|---|---|
| `governance/sources/verifier_key_registry/REGISTRY.json` | `False` | `verifier_key_registry` | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION` | only this tranche's own prose (this audit, the R1 completion review) and an unrelated T2C blocker-token name `g1_verifier_key_registry_owner_not_source_verified` | `NO_FILESYSTEM_OR_IMPLEMENTATION_COLLISION`; blocker-token match is a distinct identifier, not this path | `ACCEPT_PROPOSED_PENDING_LOCAL_REVIEW` |
| `governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl` | `False` | `LIFECYCLE_LOG` | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION` | zero | `NO_COLLISION` | `ACCEPT_PROPOSED_PENDING_LOCAL_REVIEW` |
| `governance/sources/verification_authority_spec/` (family: `SPEC_v{n}.json`, `ACTIVATION_DECISIONS.jsonl`) | `False` (directory absent) | `verification_authority_spec` | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION` | only this tranche's own prose (this audit) | `NO_FILESYSTEM_OR_IMPLEMENTATION_COLLISION` | `ACCEPT_PROPOSED_PENDING_LOCAL_REVIEW` |
| `governance/sources/registry_observation_log/LOG.jsonl` | `False` | `registry_observation_log` | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION` | only this tranche's own prose (this audit) | `NO_FILESYSTEM_OR_IMPLEMENTATION_COLLISION` | `ACCEPT_PROPOSED_PENDING_LOCAL_REVIEW` |
| `governance/sources/issuer_registry/REGISTRY.json` | `False` | `issuer_registry` | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION` | this tranche's own prose (this audit, worker return), the T2E successor SCEC block's unrelated blocker token `issuer_registry_lookup_source_not_created`, and T2C's unrelated blocker token `g1_issuer_registry_owner_not_source_verified` | `NO_FILESYSTEM_OR_IMPLEMENTATION_COLLISION`; blocker-token matches are distinct identifiers, not this path | `ACCEPT_PROPOSED_PENDING_LOCAL_REVIEW` |
| `governance/sources/issuer_registry/LOOKUP_RESPONSES.jsonl` | `False` | `LOOKUP_RESPONSES` | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION` | only this tranche's own prose (this audit) | `NO_COLLISION` | `ACCEPT_PROPOSED_PENDING_LOCAL_REVIEW` |

Reminder: `Test-Path` returning `False` and `rg` returning only this
tranche's own governed prose proves absence of a current filesystem or
implementation collision at these exact locations. It does not prove the
path is correct, final, or ready for creation; it does not create the path,
directory, or file; and it does not authorize implementation. Every row
remains `PROPOSED_LOCAL_REVIEW` pending a separate Local decision and, later,
operator authorization for actual creation.

## Proposed Implementation Order

| Tranche | Scope | Operator checkpoint required before opening |
|---|---|---|
| Future T3A | Group 1 key registry schema plus lifecycle log implementation | concrete Party A principal, key generation/import ceremony authorization |
| Future T3B | Group 2 specification document plus activation-decision file implementation | concrete activation-approver principal, first specification version content |
| Future T3C | Group 3 observation-log implementation, hash-chain code | concrete Party B principal, credential-separation proof from Party A and Party C |
| Future T3D | Group 4 issuer registry plus lookup implementation | concrete Party C principal, issuer content source, credential-separation proof |
| Future T3E | consumer wiring: `SignatureValidityCheck`, `LookupProvenanceCheck`, `sourceObservationLog` calls bound to the four real sources | all of T3A-T3D independently verified by Local |

Each future tranche is independently reviewable and requires a separate Local
readiness decision and operator authorization. No tranche listed here opens
automatically from this audit's acceptance.

`successorTrancheOpened: NO`

## Risk / Corrective Action

| Risk | Control |
|---|---|
| this contract design is mistaken for source creation | every group row carries `SOURCE_NOT_CREATED`; no registry, specification, log, or lookup file was created by this audit |
| proposed paths are treated as final without Local review | every proposed path is marked `PROPOSED_LOCAL_REVIEW`; a future implementation work order must re-confirm or revise them |
| a future implementation tranche silently combines two source groups outside the permitted cases | Cross-Source Identity And Access Matrix enumerates every permitted and rejected combination; only Cases 10 and 11 are pre-permitted |
| a future tranche opens automatically from this design's acceptance | `successorTrancheOpened: NO`; each future tranche requires separate Local readiness and operator authorization |
| a verifier consumer trusts a caller-supplied hash instead of recomputing it | Negative Cases table requires independent recomputation for every hash-bearing source group |

## Decision / Disposition

Decision: `T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_ADOPTED`.

All five R1 findings, both R2 findings, all three R3 findings, and all seven
T2G acceptance rows are closed per the Finding-To-Repair Locator Ledger. The
R1-R3 lineage (non-self-referential `cvf.source-record-canonicalization@1`
hash profile with a positive recomputation example actually recomputed
twice with two independent tools
(`0c798661caf02b0d3537b845ca6b95f94c3ad4af4221ca4502d508dba17d3061`);
complete per-group schemas; field-for-field T2C consumer joins; explicit
append-only Group 2 activation events with a unique-active invariant; a
collision-checked path ledger; and the T2F-R3-01 `specHashHex`/`specFileRecordHashHex`
separation) remains valid and unchanged by this T2G revision, except for
Group 3's identity model, which this revision fully replaces.

**T2G supersedes the entire correction/fork-merge history for Group 3.**
R1's same-ID multiple-observation permission, R2's single-parent
`correctionOf` design, and R3's multi-parent array with a liveness rule that
a Local reviewer found self-contradicting are all superseded, not amended,
by the Immutable Snapshot Identity design (T2G-01 through T2G-05): a
`snapshotId` is write-once and immutable; exactly one Party B original
observation ever binds to one ID; an error or content change is never
repaired in place, only recorded under a fresh `snapshotId` with a fresh
receipt; `lookup`/`countObservationsFor` are literal per-ID record counts,
not any form of active-head resolution; and no `entryKind`, `correctionOf`,
or fork-merge field, rule, or algorithm remains normative anywhere in this
document. T2C's `LookupProvenanceCheck` -- ordering, freshness, authority,
hash, and lookup checks, including its existing `countObservationsFor(...)
> 1` fail-closed branch -- is unchanged; the T2G design satisfies that
existing branch exactly rather than redefining it, so no T2C amendment was
required and `BLOCKED_WITH_REASON` was not triggered.

All four source groups now have a proposed exact path, complete schema,
identity and version scheme, access matrix entry, lifecycle, correction
route, durable receipt, named consumer, fail-closed validation order, and
establishment evidence checklist. Every group remains `SOURCE_NOT_CREATED`;
every candidate admission remains `UNVERIFIED`. No registry, specification,
log, or lookup instance was created. No key or credential was generated,
imported, or referenced with real material. No live lookup was performed.

This correction does not appoint a new party, does not supersede any T2E
appointment, and does not open a successor implementation tranche. Local
independently reviews this corrected contract before any future
implementation work order may cite it as design authority.

## T2G-01 Through T2G-07 Acceptance Ledger

| ID | Required contract | Locator | Positive/negative evidence |
|---|---|---|---|
| T2G-01 | `snapshotId` unique, immutable, never reused/aliased; exactly one Party B original observation per ID | Group 3 schema row, `snapshotId` field; Immutable Snapshot Identity, "T2G-01: uniqueness and single-binding" | Concrete Test step 1 (one original gives count 1); step 2 (duplicate-ID write attempt rejected at write time, never inserted) |
| T2G-02 | no `correctionOf`, `entryKind`, active-head, or fork-resolution mechanism remains normative | Immutable Snapshot Identity, "T2G-02: no correction/merge vocabulary remains normative" | targeted source search confirms remaining occurrences of the rejected vocabulary are confined to Purpose's R1-R3 revision history, the Finding-To-Repair Locator Ledger's finding descriptions, and this section's own historical-explanation paragraph, never a current schema field or rule |
| T2G-03 | error/changed content receives a new `snapshotId`, new original observation, new receipt; old receipt stays bound to old ID and cannot be substituted for the new ID; rejection of the unchanged old receipt depends on an existing T2C predicate | Group 3 schema row, "Correction, rotation, supersession, revocation"; Immutable Snapshot Identity, "T2G-03" | Concrete Test steps 4-5 (new ID coexists; altered receipt fails signature, unchanged old receipt may remain valid for old ID); Negative Probes, "old-receipt substitution for a new snapshot" row |
| T2G-04 | `lookup(snapshotId)` yields the one original or none; `countObservationsFor(snapshotId)` counts every record bearing that ID, 0/1/>1, without excluding history | Group 3 schema row, "Validation order and failure taxonomy"; Immutable Snapshot Identity, "T2G-04" | Concrete Test step 3 (hypothetical bypassed-duplicate case yields count 2, `FORKED_OBSERVATION`/UNVERIFIED, never an administrative merge); Negative Probes, "duplicate-ID integrity fault" row |
| T2G-05 | one exact `snapshot_content` bytes/encoding recipe; `snapshotHashHex` hashes decoded raw bytes; T2C receives decoded bytes, not encoded text or an unresolved reference | Group 3 schema row, `snapshot_content` field; Immutable Snapshot Identity, "T2G-05" | published 29-byte preimage, base64url value and digest independently recomputable; padded negative value rejected before hashing; Negative Probes, "malformed snapshot encoding" row |
| T2G-06 | preserve Group 1 vector and Group 2 dual-hash distinction; reconcile all four groups, T2C table, negative cases, checklist, and worker return to the new identity model | Positive Recomputation Example (unchanged from R2/R3); Two Distinct Group 2 Hashes (unchanged from R3); T2C Consumer-Binding Table, Negative Probes, Establishment Evidence Checklist, Cross-Source Identity And Access Matrix Case 8, all updated below; paired worker return | cross-section sweep performed during this revision; no row anywhere claims `SOURCE_ESTABLISHED` or any operational existence; every group row still states `SOURCE_NOT_CREATED` / `UNVERIFIED` |
| T2G-07 | thirteen parked paths byte-identical; worker edits exactly the existing two paths; never stages/commits | Frozen Parked-Path Integrity Reconciliation below; paired worker return's Frozen-Path Reconciliation, `git status`, and No-Commit Statement | before/after SHA-256 ledger recomputed at `executionBaseHead`; `git status --short --untracked-files=all` shows the same fifteen untracked paths before and after; empty index throughout |

## Source Inventory

| Path | Action | Purpose |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | FULL_READ | Contracts 1-4, Cross-Contract Separation Matrix, Admission Evidence Ledger |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | FULL_READ | Party A appointment terms and restrictions |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | FULL_READ | Party B appointment terms and restrictions |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | FULL_READ | Party C appointment terms and restrictions |
| `docs/reviews/CVF_ACEL_G1_T2E_CONTRACT_2_ACTIVATION_APPROVER_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | FULL_READ | activation-approver appointment terms and restrictions |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_READINESS_LOCAL_DECISION_2026-09-18.md` | FULL_READ | selected tranche scope and required output shape |
| `docs/baselines/CVF_GC018_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | FULL_READ | exact two-output authorization and forbidden effects |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | FULL_READ | field-level Source Contract Requirements and Required Handoff Evidence |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal-format gate-trap checklist applied while drafting |
| `AGENT_HANDOFF_V63_2026-09-18.md` | FULL_READ | active handoff, protected paths, next allowed move |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md` | FULL_READ | R1 five-finding correction contract this revision closes |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2F_R1_CONTRACT_COHERENCE_CORRECTION_2026-09-18.md` | FULL_READ | exact R1 field-level requirements |
| `docs/baselines/CVF_GC018_ACEL_G1_T2F_R1_CONTRACT_COHERENCE_CORRECTION_2026-09-18.md` | FULL_READ | R1 dispatch authorization and exact two-path manifest |
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | FULL_READ | accepted consumer contract joined field-for-field in this revision; re-read for R2 to confirm `lookup`/`countObservationsFor` are opaque interface calls; re-read for R3 to verify the exact literal "more than one source-owned observation" comment text |
| this audit's own R1-final content at SHA-256 `89651f08e30d5c0b9d961dd9380bd4362bf08b907350c1dfff1159e664d1be2c` | FULL_READ | source of the R2-corrected positive vector and fork-resolution defects |
| this audit's own R2-final content at SHA-256 `97b6105ef0e51b1549bdee5c1e5b40dc89d1ee59ee3e8162ba19a9b4d4850e22` | FULL_READ | source of the R3-corrected specHashHex, countObservationsFor semantic, and correctionOf scope/liveness defects |
| this audit's own R3-final content at SHA-256 `33f258d4a1fa6f6b389b309e45de526fbde1b5cc7468520c43ac839e4878bc15` | FULL_READ | source of the self-contradicting liveness rule/regression-test defect that triggered the T2G architecture replacement |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_2026-09-18.md` | FULL_READ | committed T2G work order; T2G-01 through T2G-07 acceptance matrix |
| `docs/baselines/CVF_GC018_ACEL_G1_T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_2026-09-18.md` | FULL_READ | committed T2G paired baseline; Architecture Decision And Acceptance Boundary |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `Target / Source`, `Scope / Methodology`, `Findings / Position`, `Risk / Corrective Action`, `Decision / Disposition` structural headings; Source Inventory action-cell vocabulary (`READ`, `FULL_READ`); `SOURCE_NOT_CREATED` and `UNVERIFIED` disposition tokens; `PROPOSED_LOCAL_REVIEW` path marker; Agent Operation Trace Block label set |
| gateRunPurpose | confirmation of output shape before Local review, not source discovery or implementation proof |
| claimBoundary | checker PASS cannot create or approve an operational source |

## Frozen Parked-Path Integrity Reconciliation

| Field | Value |
|---|---|
| Ledger basis | the R3 worker return's Frozen-Path Reconciliation table already recorded a SHA-256 manifest for these thirteen paths; this T2G revision recomputes and diffs against it |
| Method | `sha256sum` over each of the thirteen exact paths, at `executionBaseHead` `c743bb37a08a29efebf9381e86792088c9105ce3` |
| Result | 13/13 present and readable; zero unreadable; zero missing; zero edits made by this T2G revision |
| Comparison to prior ledger | recomputed hashes match the R3 worker return's Frozen-Path Reconciliation table exactly, path for path |
| Disposition | `ZERO_MISMATCHES` against both the work order's implied path list and every prior tranche's recorded ledger |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | INTERNAL_AGENT worker |
| Provider or surface | shared private CVF workspace |
| Session or invocation | T2G immutable snapshot identity architecture replacement, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, `sha256sum`, `python3 -c` (`hashlib`/`json`, resolution simulation), governance gates, file edit |
| Target paths | this audit (modified in place) and the paired worker return |
| Allowed scope source | committed work order `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_2026-09-18.md`, dispatch commit `5fd66d35f`, continuity commit `c743bb37a` |
| Before status evidence | HEAD `c743bb37a08a29efebf9381e86792088c9105ce3`; thirteen parked untracked paths present; staging empty; this audit's pre-T2G (R3-final) SHA-256 `33f258d4a1fa6f6b389b309e45de526fbde1b5cc7468520c43ac839e4878bc15` |
| After status evidence | this audit modified in place; worker return modified next; parked paths unchanged; no commit made |
| Diff evidence | `git diff --name-status` before and after shows zero tracked-file changes; `git status --short --untracked-files=all` shows the same two paths, now modified in place, plus the same thirteen parked paths |
| Approval boundary | documentation-only T2G architecture replacement of two existing outputs |
| Claim boundary | no source, key, credential, implementation, live/runtime/public effect |
| Agent type | INTERNAL_AGENT contract designer executing the operator-selected immutable-snapshot architecture |
| Invocation ID | `acel-g1-t2g-immutable-snapshot-identity-worker-20260918` |
| Expected manifest | this audit plus the worker return, both modified in place |
| Actual changed set | this audit; worker return follows |
| Manifest delta | pending worker-return completion |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | integrated operational-source establishment contract design |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime or source receipt is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: contract design documentation only |
| invocationBoundary | internal shared-workspace documentation task |
| interceptionBoundary | no IDE, provider, CLI/MCP or runtime interception claim |
| claimLanguage | source-contract design is not source creation or implementation |
| forbiddenExpansion | keys, credentials, source/schema/code creation, live lookup, admission, runtime, public sync, deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | accepted T2E design/appointments to Local readiness to T2F work order to this worker return |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this audit and the paired worker return |
| Internal source | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source is admitted |
| Claim boundary | internal inputs do not prove source existence or implementation |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one integrated contract would expose coherent
source identities, access boundaries, and evidence gates for all four groups
while keeping every source uncreated.

Evidence Comparison Requirement: every T2E admission requirement and
appointment restriction compared above against an explicit T2F contract field
or negative case; see T2E-Requirement-To-T2F-Field Reconciliation. Every R1
finding compared against its exact repair locator; see Finding-To-Repair
Locator Ledger.

Contradiction Handling Requirement: no contradiction between T2E's accepted
contract shapes and this corrected design was found; all four groups remained
consistent with their T2E-defined prohibited combinations. The R1 review's
five findings were confirmed as real defects, not invented, and are closed
by exact locators rather than reasserted with different wording.

Claim Update Requirement: this document is a confirmed, R1-corrected
contract-design proposal; every implementation claim remains unresolved and
disclosed as `SOURCE_NOT_CREATED`. Corrected design coherence (recomputable
hashes, complete schemas, satisfied consumer joins, explicit activation,
collision-checked paths) is distinguished from future source existence,
operational verification and candidate admission, none of which this
revision claims.

## Finding-To-Governance Learning Disposition

| Finding cluster | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| initial contract design used an ambiguous, self-referential canonical hash and incomplete schemas (T2F-R1-01, T2F-R1-02) | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | the `cvf.source-record-canonicalization@1` profile and per-group complete schema tables above are the added rule; future source-design tranches must cite this profile rather than inventing a new ad hoc hashing scheme |
| initial contract design did not join the accepted T2C consumer field-for-field and used automatic latest-wins activation (T2F-R1-03, T2F-R1-04) | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | the T2C Consumer-Binding Table and Explicit Approval, Activation And Supersession subsection above are the added rule; future implementation work orders must reuse these exact field bindings |
| initial contract design reused a generic tranche-token query as path-collision evidence (T2F-R1-05) | `EVIDENCE_INTERPRETATION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_EXISTS` | the per-path/family collision discipline already governed elsewhere in this repository now has a worked example in the Literal Proposed-Path Collision Ledger above; no new machine rule needed |
| R1's own "positive recomputation vector" and "negative mutation probes" were asserted digests, not actually computed ones, and one vector mixed fields from two different declared schemas (T2F-R2-01) | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | future cryptographic vectors in this repository must be produced by running an actual hash function twice with independent tools and cross-checking field membership against a closed preimage list, not asserted from a plausible-looking hex string; the Closed Preimage Field Lists table above is the reusable control |
| R1 claimed a single-parent correction field could resolve a multi-head fork, which is structurally impossible (T2F-R2-02) | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | future append-only correction/fork designs in this repository must use a multi-parent (array) supersession field and demonstrate a concrete multi-head-to-one-head test, not assert single-entry resolution without checking the field's cardinality |
| R2 defined `specHashHex` twice with two mutually incompatible preimages (T2F-R3-01) | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | future dual-purpose hash fields (a content-identity hash consumed by an accepted external contract, plus a record-integrity hash under a local canonicalization profile) must be split into two separately named fields immediately; the Two Distinct Group 2 Hashes subsection above is the reusable pattern |
| R2's fork-resolution algorithm silently redefined an accepted external contract's literal semantic ("more than one source-owned observation") without disclosing the change as a decision (T2F-R3-02) | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | "opaque interface" reasoning about an accepted external contract must be checked against that contract's own literal comments/requirements, not just its function signature; a storage-representation choice must preserve every literal semantic the external contract states, or the change must be disclosed as an explicit, reviewed semantic decision, not asserted as harmless |
| R2's `correctionOf` union algorithm had no cross-reference scope or liveness check, and `snapshot_content` left three incompatible byte representations undetermined (T2F-R3-03) | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | any reference field naming another record (a "supersedes," "correctionOf," or similar pointer) must be scope-checked (same partition/identity key) and liveness-checked (target still active at append time) before being accepted into a durable log; any field whose bytes are hashed by an external contract must be pinned to exactly one encoding, never left as "string or bytes or reference" |
| three consecutive repair rounds (R1, R2, R3) each patched a same-ID correction/fork-merge mechanism and each introduced or left a new defect, culminating in R3's own liveness rule contradicting its own regression test | `PHASE_GATE_PLACEMENT_GAP` | `GOVERNANCE_CONTROL_PLANE` | `DESIGN_REVIEW_REQUIRED` | the operator's decision to replace the architecture outright, rather than dispatch a fourth same-model repair, is the corrective action; a reusable lesson is that three consecutive same-mechanism repair rounds each finding a new defect in the mechanism itself is a signal to reassess the mechanism, not to keep patching it; no machine rule is proposed here, but this pattern should inform future review-cost/escalation guidance |
| runtime/provider/cost applicability | N/A_WITH_REASON | N/A_WITH_REASON | N/A_WITH_REASON | this document's mentions of provider, live, runtime and network are exclusion statements (no provider/live/runtime effect claimed), not a runtime, provider, or cost-economics finding; no runtime/provider/cost learning lane applies |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-contract design with no public-sync authorization.

## Claim Boundary

This document proposes an integrated, implementation-neutral operational-
source establishment contract for four source groups, corrected under R1 to
close five Local-review findings, under R2 to close two further correctness
defects found in R1's own evidence, under R3 to close three contract-level
contradictions found by independent review of R2's own evidence, and under
this T2G tranche to replace Group 3's entire same-ID correction/fork-merge
architecture (R1, R2 and R3 in sequence) with an operator-selected immutable
snapshot identity model, after a Local reviewer found R3's own liveness rule
self-contradicting. It does not create, populate, or operate any registry,
specification, observation log, or issuer lookup. It does not generate or
import a key, provision a credential, perform a live lookup, or admit any
candidate. Every source group remains `SOURCE_NOT_CREATED` and every
candidate admission remains `UNVERIFIED`. All proposed paths and schemas are
`PROPOSED_LOCAL_REVIEW`, not approved implementation targets. The Literal
Proposed-Path Collision Ledger's absence evidence is not creation or
implementation proof. No successor tranche opens from this document alone;
Local review remains required before this corrected design becomes citable
implementation authority.

R2/R3 dispatch-provenance disclosure (historical, resolved by T2G): unlike
the T2F and T2F-R1 tranches, neither the R2 correction nor the R3 correction
was authorized by a committed `docs/baselines/CVF_GC018_...` plus
`docs/work_orders/...` pair; both were dispatched as direct,
fully-specified operator/orchestrator instructions to this INTERNAL_AGENT
worker, with R2's gap explicitly confirmed via the executing agent's own
blocking question. This T2G tranche is a properly committed dispatch
(`docs/baselines/CVF_GC018_ACEL_G1_T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_2026-09-18.md`
plus `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2G_IMMUTABLE_SNAPSHOT_IDENTITY_CONTRACT_2026-09-18.md`,
committed at `5fd66d35f` and `c743bb37a`), so the recurring
missing-committed-packet pattern from R2/R3 does not apply to this return.
Local's independent review of this T2G return, including whether the
immutable-ID architecture itself is semantically sound and whether the R2/R3
dispatch-provenance history requires any retrospective remediation, remains
required and has not occurred.
