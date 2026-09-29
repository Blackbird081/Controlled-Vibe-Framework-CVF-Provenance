# CVF ACEL G1 T2C Verifier Trust-Anchor Contract Design

Memory class: governed-worker-audit

Status: HYPOTHETICAL_DESIGN_ONLY

Date: 2026-09-17

Dispatch base head: `44a7264d4b1d49404cd10ce18b66daca8f88097a`

## Purpose

Define a bounded, hypothetical documentation-only contract for Ed25519-signed verifier receipts that authenticate issuer identity after a source-verified registry lookup. The contract separates three independent predicates: receipt content integrity, verifier signature validity, and genuine lookup provenance. No existing key registry, signer runtime, or lookup owner is claimed. All operational dependencies remain explicitly unverified.

## Target Under Review

This audit's target is the proposed `VerifierReceiptProfile` contract itself, produced under work order `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` from the Local architecture decision `CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md`. The reviewed surface is the receipt payload shape, preimage construction, key-lifecycle checks, three admission predicates, and adversarial vector matrix defined below; no existing runtime, registry, or signer is under review because none is claimed to exist.

## Architectural Decisions

From Local architecture decision (CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md):

1. Ed25519 asymmetric signing, verifier-controlled key, CVF-governed registry
2. Verifier initiates receipt only after genuine decision-owner registry lookup
3. Signature authenticates verifier key; lookup truth is separately bound
4. Deterministic UTF-8 JCS preimage with domain separation, versioning
5. Key registry independently governed; no receipt-supplied keys accepted
6. TypeScript decision-time and Python persisted-evidence verification are independently specified
7. Historical verification and revocation semantics are explicit

## Scope Limitations

- Hypothetical documentation only; no actual keys, registry, or signer wiring
- Proposed interfaces and decision criteria only
- No implementation, tests, or checker code
- No test receipts signed with operational keys
- No automatic successor or T2B repair
- Thirteen parked paths remain frozen and unaccepted

## Core Contract Specification

### VerifierReceiptProfile - Signed Payload

The receipt is an immutable assertion by the CVF verifier after a lookup. All fields are required; null/empty is fail-closed for each.

```
Profile version: cvf.verifierReceipt.v1

Required fields (UTF-8, JCS ordered):
  - domain (string): fixed literal "cvf.verifierReceipt"; binds this preimage to this exact profile so a signature valid under any other CVF signing context (or a future incompatible schema) can never verify here
  - profileVersion (string): fixed literal "v1" for this specification; a future v2 must use a different literal so a v1 signature can never satisfy a v2 verifier and vice versa
  - receiptId (string): unique, cryptographically random, immutable
  - verificationRound (string): decision round identifier, immutable from lookup observation
  - verificationAuthority (string): authority-body identifier (e.g., "ACEL_G1_DECISION_OWNER")
  - verificationAuthorityHash (string): SHA-256 of authority specification at lookup time
  - issuerIdentity (string): claimed issuer identifier
  - issuerAttestedHash (string): issuer self-supplied hash binding their authority/policy
  - trustedRegistrySnapshotIdentity (string): registry snapshot identifier
  - trustedRegistrySnapshotHash (string): SHA-256 of source-owned registry state at lookup
  - lookupResult (string): verified admission status from registry lookup; one of `IDENTITY_CONFIRMED`, `IDENTITY_REJECTED`, `IDENTITY_UNRESOLVED` (see Admission Outcome Binding below -- a receipt with a valid signature and genuine provenance is never itself sufficient for admission unless this field is exactly `IDENTITY_CONFIRMED`)
  - observationTimeUtc (string): RFC 3339 timestamp when lookup was performed
  - receiptIssuanceTimeUtc (string): RFC 3339 timestamp when receipt was created
  - signatureKeyId (string): identifier selecting public key from trusted verifier registry
```

All other fields in the receipt object are either signature/envelope or verification metadata, never part of the signed preimage. `domain` and `profileVersion` are bound into the signed bytes themselves (see Preimage Construction below), not merely documented as prose labels outside the preimage; a receipt whose `domain`/`profileVersion` fields do not match this contract's exact literals fails Predicate 1 before signature verification is ever attempted.

### Preimage Construction

The canonicalized preimage is:

```
preimage = UTF-8(JCS_CANONICAL_JSON(
  {
    "domain": "cvf.verifierReceipt",
    "profileVersion": "v1",
    "receiptId": <receiptId>,
    "verificationRound": <verificationRound>,
    "verificationAuthority": <verificationAuthority>,
    "verificationAuthorityHash": <verificationAuthorityHash>,
    "issuerIdentity": <issuerIdentity>,
    "issuerAttestedHash": <issuerAttestedHash>,
    "trustedRegistrySnapshotIdentity": <trustedRegistrySnapshotIdentity>,
    "trustedRegistrySnapshotHash": <trustedRegistrySnapshotHash>,
    "lookupResult": <lookupResult>,
    "observationTimeUtc": <observationTimeUtc>,
    "receiptIssuanceTimeUtc": <receiptIssuanceTimeUtc>,
    "signatureKeyId": <signatureKeyId>
  }
))
```

`domain` and `profileVersion` are fixed literals, not receipt-supplied values: every verifier and every checker constructs the preimage with exactly these two literals hard-coded, never read from receipt input. A receipt cannot claim a different domain/version and still verify, because the reconstructed preimage the checker builds always uses this contract's own fixed literals; any receipt actually produced under a different domain/version silently fails signature verification (Predicate 2) because its true signed bytes differ from what this checker reconstructs.

JCS canonicalization per RFC 8785:
  - UTF-8 encoding
  - Lexicographic key ordering (all fourteen keys above, including `domain` and `profileVersion`, sorted by exact key string; example: `domain` < `issuerAttestedHash` < `issuerIdentity` < `lookupResult` < `observationTimeUtc` < `profileVersion` < `receiptId` < `receiptIssuanceTimeUtc` < `signatureKeyId` < `trustedRegistrySnapshotHash` < `trustedRegistrySnapshotIdentity` < `verificationAuthority` < `verificationAuthorityHash` < `verificationRound`)
  - Whitespace elimination
  - Numeric values as canonical decimal strings
  - No comments, no trailing commas
  - Result is unambiguous 1:1 mapping to original object

### Positive Test Vector (Reconstructible)

The following vector is computed directly with a deterministic test-fixture Ed25519 keypair (seed `SHA-256("CVF-T2C-POSITIVE-VECTOR-TEST-FIXTURE-SEED-0001")`, using the `cryptography` library's `Ed25519PrivateKey.from_private_bytes`); it is not an operational key and signs no real registry lookup. Anyone can independently recompute this vector from the inputs below.

Preimage object (pretty-printed for readability; the actual signed bytes are the compact JCS form below):

```json
{
  "domain": "cvf.verifierReceipt",
  "issuerAttestedHash": "b57d8b3795f1bbfd46e1748e7613f916a455c163cd4e5f6000d1373536a46bb9",
  "issuerIdentity": "issuer-test-001",
  "lookupResult": "IDENTITY_CONFIRMED",
  "observationTimeUtc": "2026-09-18T00:00:00Z",
  "profileVersion": "v1",
  "receiptId": "rcpt-20260918-positive-vector-0001",
  "receiptIssuanceTimeUtc": "2026-09-18T00:00:05Z",
  "signatureKeyId": "verifier-key-testvector-0001",
  "trustedRegistrySnapshotHash": "9997d053ab2e26cd4c7108f36daf4728c8a830381f91026a366f1c31dc7817ae",
  "trustedRegistrySnapshotIdentity": "registry-snapshot-testvector-0001",
  "verificationAuthority": "ACEL_G1_DECISION_OWNER",
  "verificationAuthorityHash": "e9f7330d18968fad1209557dae0519620e71d2be87552c14cba8a16d799d9661",
  "verificationRound": "ACEL_G1_T2C_ROUND_TESTVECTOR_001"
}
```

Exact signed bytes (compact JCS, UTF-8, this is `preimage_bytes` passed to `ED25519_SIGN`):

```
{"domain":"cvf.verifierReceipt","issuerAttestedHash":"b57d8b3795f1bbfd46e1748e7613f916a455c163cd4e5f6000d1373536a46bb9","issuerIdentity":"issuer-test-001","lookupResult":"IDENTITY_CONFIRMED","observationTimeUtc":"2026-09-18T00:00:00Z","profileVersion":"v1","receiptId":"rcpt-20260918-positive-vector-0001","receiptIssuanceTimeUtc":"2026-09-18T00:00:05Z","signatureKeyId":"verifier-key-testvector-0001","trustedRegistrySnapshotHash":"9997d053ab2e26cd4c7108f36daf4728c8a830381f91026a366f1c31dc7817ae","trustedRegistrySnapshotIdentity":"registry-snapshot-testvector-0001","verificationAuthority":"ACEL_G1_DECISION_OWNER","verificationAuthorityHash":"e9f7330d18968fad1209557dae0519620e71d2be87552c14cba8a16d799d9661","verificationRound":"ACEL_G1_T2C_ROUND_TESTVECTOR_001"}
```

- `preimage_sha256`: `df941f3f0531b7b50aec1e811987a333103a0d2dcce783781b9dbb0b86dc3f98`
- `publicKey` (raw, base64url, test-fixture only): `RMcYJcHIAYbM9S2L717B9wmMom1ZMEIs-PTJrQRXomw`
- `signature` (base64url): `4ITyotTCCInWOjSkUvtv3M21kIyTsChz25eaQ_cXj4eyvOn-tZZlwfpWe4CvFtxZdj5QF8eQq3HWhVJxEjTtBw`
- `algorithm`: `Ed25519`

Independent reconstruction check performed during authoring: decoding `publicKey` and `signature` from the base64url strings above and calling `Ed25519PublicKey.from_public_bytes(...).verify(signature_bytes, preimage_bytes)` against the exact compact JCS bytes above returns success (`PASS`), using only the published strings. This proves the cryptographic fixture only. No source-owned registry snapshot, observation log or trusted authority specification is published here, so Predicate 3 and actual admission are conditional illustrations, not independently verified positive evidence.

**Negative counterpart, same key, different issuer (proves signature validity alone is not admission):** re-signing the same preimage shape with `receiptId` set to `rcpt-20260918-rejected-vector-0002`, `issuerIdentity` set to `issuer-test-rejected-002`, and `lookupResult` set to `IDENTITY_REJECTED` yields exact signed bytes `{"domain":"cvf.verifierReceipt","issuerAttestedHash":"b57d8b3795f1bbfd46e1748e7613f916a455c163cd4e5f6000d1373536a46bb9","issuerIdentity":"issuer-test-rejected-002","lookupResult":"IDENTITY_REJECTED","observationTimeUtc":"2026-09-18T00:00:00Z","profileVersion":"v1","receiptId":"rcpt-20260918-rejected-vector-0002","receiptIssuanceTimeUtc":"2026-09-18T00:00:05Z","signatureKeyId":"verifier-key-testvector-0001","trustedRegistrySnapshotHash":"9997d053ab2e26cd4c7108f36daf4728c8a830381f91026a366f1c31dc7817ae","trustedRegistrySnapshotIdentity":"registry-snapshot-testvector-0001","verificationAuthority":"ACEL_G1_DECISION_OWNER","verificationAuthorityHash":"e9f7330d18968fad1209557dae0519620e71d2be87552c14cba8a16d799d9661","verificationRound":"ACEL_G1_T2C_ROUND_TESTVECTOR_001"}` with `preimage_sha256` `6b5336fbdc9cc48c07ad773b1f305c6280499eb8de3df5fff721c1f9dfb645cc` and `signature` (base64url) `BnjZSVj46xf8KVXL2xwOInQU6AxylYuSfxC59s6UJ6ggVXaiUPYIzEgQkL_3Riz1kmkxDRM8kJv7L7O_e-IsDw` under the same test-fixture public key. The two signed byte strings and hashes are different and both signatures verify. With a hypothetical source snapshot confirming the first issuer and rejecting the second, both can pass Predicate 3; neither such snapshot nor its source-owned provenance is proved by these cryptographic vectors.

### Signature And Key-ID Envelope

After preimage creation, the verifier computes:

```
ed25519_signature = ED25519_SIGN(preimage_bytes, verifier_private_key)

receipt_envelope = {
  ...preimage_object_fields...,
  "signedBy": {
    "keyId": <signatureKeyId>,
    "signature": <base64url(ed25519_signature)>,
    "algorithm": "Ed25519"
  }
}
```

The signature and signedBy envelope are never part of their own signed preimage.

### Key Identity And Lifecycle

The `signatureKeyId` field value must select a public key from the CVF-governed verifier public-key registry:

```
VerifierPublicKeyRegistry (proposed structure, no existing owner):
  - Owned by: CVF key-governance authority (owner unverified)
  - Located at: <TBD; source-owned path>
  - Contents: array of {keyId, publicKey(Ed25519), role, issuedAt, expiresAt, revokedAt?, status}
  - Write authority: key-governance authority only
  - Lookup semantics: exactly one exact keyId match; no duplicate keyId or public-key aliases; fail closed on ambiguity
```

Verification of key authorization:

```
1. Require `signedBy.keyId == signatureKeyId` from the signed preimage.
2. Resolve exactly one registry record by exact keyId; reject missing, duplicate-ID, or public-key-alias records.
3. Require `status == "ACTIVE"`, `issuedAt <= receiptIssuanceTimeUtc`, and `expiresAt > observationTimeUtc` when expiry is set.
4. Reject when `revokedAt <= receiptIssuanceTimeUtc`; require the role to authorize issuance for this `verificationAuthority`.
5. Only then retrieve the record's publicKey and verify the signature. Every failed or unavailable check returns UNVERIFIED.
```

Receipt-supplied public keys are always rejected. Candidate-provided key paths are always rejected. Self-asserted `verifiedBy` is never a key source.

### Three Independent Admission Predicates

A receipt passes admission only if all three predicates are independently satisfied. Omission of any predicate is fail-closed.

#### Predicate 1: Content Integrity

Verify that the receipt object's required fields are valid UTF-8, properly ordered under JCS, and match their declared types.

```
ContentIntegrityCheck():
  for each required field:
    - Verify UTF-8 encoding
    - Verify field is present and non-null
    - Verify field type matches specification
    - Verify no unknown fields in preimage_object
  Recompute JCS preimage
  Return (integrityValid=true if all checks pass, else false)
```

Omission or malformation of any required field fails this predicate immediately. Content integrity alone does not authenticate the receipt; it is necessary but not sufficient.

#### Predicate 2: Verifier Signature Validity

Verify that the signature was created by the Ed25519 private key corresponding to the trusted public key identified by `signatureKeyId`.

```
SignatureValidityCheck(receipt, verifierRegistry):
  keyId = receipt.signedBy.keyId
  if keyId != receipt.signatureKeyId:
    return false
  // Registry lookup is source-owned, exact, and fail-closed; no receipt or
  // candidate-supplied key or path may replace it.
  records = verifierRegistry.lookupExact(keyId)
  if records unavailable or count(records) != 1:
    return false
  keyRecord = records[0]
  if verifierRegistry.hasDuplicateKeyId(keyId) or
     verifierRegistry.hasPublicKeyAlias(keyRecord.publicKey, keyId):
    return false
  if keyRecord.status != "ACTIVE" or
     keyRecord.issuedAt > receipt.receiptIssuanceTimeUtc or
     (keyRecord.expiresAt and keyRecord.expiresAt <= receipt.observationTimeUtc) or
     (keyRecord.revokedAt and keyRecord.revokedAt <= receipt.receiptIssuanceTimeUtc) or
     not keyRecord.role.authorizesIssuanceFor(receipt.verificationAuthority):
    return false
  publicKey = keyRecord.publicKey

  // domain/profileVersion are never read from the receipt; the checker
  // always reconstructs with its own fixed literals, so a receipt
  // claiming a different domain/version cannot verify here even if it
  // supplies matching-looking domain/profileVersion fields elsewhere.
  reconstructedPreimage = UTF-8(JCS_CANONICAL({
    domain: "cvf.verifierReceipt",
    profileVersion: "v1",
    ...fields_3_through_14  // receiptId through signatureKeyId, per Preimage Construction
  }))
  signature = base64url_decode(receipt.signedBy.signature)
  algorithm = receipt.signedBy.algorithm

  if algorithm != "Ed25519":
    return false

  try:
    ED25519_VERIFY(reconstructedPreimage, signature, publicKey)
    return true
  except:
    return false
```

Signature validity proves only that the verifier who holds the private key authorized the preimage. It does not prove the lookup was genuine or the `lookupResult` is correct.

#### Predicate 3: Genuine Lookup Provenance

Verify that the receipt's lookup-related fields bind a source-owned registry observation and that the observation was made by the decision owner before the receipt was issued.

```
LookupProvenanceCheck(receipt, sourceRegistry, sourceObservationLog,
                       expectedCurrentRound, expectedAuthorityHash, evaluationTimeUtc,
                       freshnessThresholdSeconds):
  snapshotId = receipt.trustedRegistrySnapshotIdentity
  snapshotHash = receipt.trustedRegistrySnapshotHash

  // Round binding: reject cross-round replay before any lookup happens.
  // expectedCurrentRound is supplied by the decision owner at call time,
  // never read from the receipt itself, so a replayed receipt cannot
  // simply assert its own round is still current.
  if receipt.verificationRound != expectedCurrentRound:
    return UNVERIFIED  // ROUND_MISMATCH: receipt round is not the caller's current round
  if not expectedAuthorityHash or receipt.verificationAuthorityHash != expectedAuthorityHash:
    return UNVERIFIED  // AUTHORITY_HASH_MISMATCH: compare with decision-owner trusted authority specification
  if freshnessThresholdSeconds < 0 or timestamps are malformed:
    return UNVERIFIED  // INVALID_VERIFICATION_CONTEXT

  // Lookup provenance: was this snapshot observed by the source?
  observation = sourceObservationLog.lookup(snapshotId)
  if not observation:
    return UNVERIFIED  // No source-owned observation

  // Verify snapshot hash
  if sha256(observation.snapshot_content) != snapshotHash:
    return UNVERIFIED  // Hash mismatch; snapshot was altered

  // Verify temporal ordering
  if observation.observedAt > receipt.observationTimeUtc:
    return UNVERIFIED  // Observation claimed after lookup time

  if observation.observedAt > receipt.receiptIssuanceTimeUtc:
    return UNVERIFIED  // Observation after receipt creation
  if receipt.observationTimeUtc > receipt.receiptIssuanceTimeUtc or
     receipt.receiptIssuanceTimeUtc > evaluationTimeUtc or
     observation.observedAt > evaluationTimeUtc:
    return UNVERIFIED  // INVALID_TIME_ORDER; future-dated observations cannot pass freshness

  // Freshness: reject a stale snapshot even if every other check passes.
  // evaluationTimeUtc is the caller's current time, never receipt-supplied.
  ageSeconds = evaluationTimeUtc - observation.observedAt
  if ageSeconds > freshnessThresholdSeconds:
    return UNVERIFIED  // STALE_SNAPSHOT: observation older than caller's freshness threshold

  // Verify source authority ownership
  if observation.authority != receipt.verificationAuthority:
    return UNVERIFIED  // Authority mismatch

  // Forked-observation check: exactly one source-owned observation may
  // exist for this snapshot identity; more than one is ambiguous.
  if sourceObservationLog.countObservationsFor(snapshotId) > 1:
    return UNVERIFIED  // FORKED_OBSERVATION: snapshot identity has more than one source-owned observation

  // Verify lookup result matches registry content
  registryLookupResult = sourceRegistry.lookup(
    receipt.issuerIdentity,
    receipt.issuerAttestedHash,
    observation.snapshot_content
  )
  if registryLookupResult != receipt.lookupResult:
    return UNVERIFIED  // Lookup result does not match registry state

  return VERIFIED
```

`expectedCurrentRound`, `expectedAuthorityHash`, `evaluationTimeUtc`, and `freshnessThresholdSeconds` are caller-supplied from decision-owner trusted context, never from the receipt; if that context or its source authority is unavailable, verification fails closed. The source-registry lookup must evaluate the issuer identity together with its attested hash against the observed snapshot; a matching identity with a different hash cannot yield `IDENTITY_CONFIRMED`. `VERIFIED` proves the receipt's `lookupResult` genuinely matches that fresh, correctly-scoped, non-forked observation, not that the identity was confirmed; see Admission Outcome Binding. The source-owned observation log and registry are independently maintained and accessed through decision-owner authority only.

### Admission Outcome Binding

The three predicates above prove a receipt is *authentic*: it is well-formed, it was genuinely signed by a trusted verifier key, and its claimed `lookupResult` genuinely matches a fresh, correctly-scoped, source-owned registry observation. None of that proves the identity was actually *confirmed* -- an authentic receipt can just as validly report `IDENTITY_REJECTED` or `IDENTITY_UNRESOLVED`. Final admission therefore requires a fourth, explicit condition, evaluated only after all three predicates return true/VERIFIED:

```
FinalAdmissionCheck(receipt, integrityValid, signatureValid, provenanceValid):
  if not (integrityValid and signatureValid and provenanceValid == VERIFIED):
    return { admitted: false, reason: "PREDICATE_FAILURE" }
  if receipt.lookupResult != "IDENTITY_CONFIRMED":
    return { admitted: false, reason: "LOOKUP_RESULT_NOT_CONFIRMED: " + receipt.lookupResult }
  return { admitted: true, reason: null }
```

An authentic receipt whose `lookupResult` is `IDENTITY_REJECTED` or `IDENTITY_UNRESOLVED` therefore always yields `admitted: false`, distinctly from a predicate failure (`reason: "PREDICATE_FAILURE"` vs. `reason: "LOOKUP_RESULT_NOT_CONFIRMED: ..."`), so a caller can tell "this receipt is real but says no" apart from "this receipt could not be authenticated at all." This closes the exact gap the prior revision left open: a genuinely signed, genuinely provenance-matched receipt for a rejected identity could previously satisfy every predicate and reach the same `{ verified: true }` outcome as a confirmed one, because no step checked the *value* of `lookupResult`, only that it matched the registry. The Positive Test Vector above is `IDENTITY_CONFIRMED` and reaches `admitted: true`; its Negative counterpart is `IDENTITY_REJECTED`, passes Predicates 1 and 2 identically, and is rejected here with `LOOKUP_RESULT_NOT_CONFIRMED: IDENTITY_REJECTED`.

### TypeScript Decision-Time Verification

Decision at candidate-evaluation time (TypeScript, JavaScript runtime):

```
async function verifyCandidateReceipt(
  candidateReceipt: VerifierReceiptProfile,
  trustedVerifierRegistry: VerifierPublicKeyRegistry,
  sourceRegistryClient: RegistryLookup,
  sourceObservationLogClient: ObservationLogLookup,
  expectedCurrentRound: string,
  expectedAuthorityHash: string,
  evaluationTimeUtc: string,
  freshnessThresholdSeconds: number
): Promise<ReceiptVerificationOutcome> {

  // Predicate 1: Content Integrity (includes domain/profileVersion literal check)
  const integrityValid = checkContentIntegrity(candidateReceipt);
  if (!integrityValid) {
    return { verified: false, admitted: false, reason: "INVALID_CONTENT_ENCODING" };
  }

  // Predicate 2: Signature Validity (reconstructs preimage with this
  // contract's own fixed domain/profileVersion literals, never the
  // receipt's claimed values)
  const signatureValid = await checkSignatureValidity(
    candidateReceipt,
    trustedVerifierRegistry
  );
  if (!signatureValid) {
    return { verified: false, admitted: false, reason: "INVALID_SIGNATURE_OR_KEY" };
  }

  // Predicate 3: Lookup Provenance (round-bound, freshness-checked, forked-observation-checked)
  const provenanceValid = await checkLookupProvenance(
    candidateReceipt,
    sourceRegistryClient,
    sourceObservationLogClient,
    expectedCurrentRound,
    expectedAuthorityHash,
    evaluationTimeUtc,
    freshnessThresholdSeconds
  );
  if (provenanceValid !== "VERIFIED") {
    return { verified: false, admitted: false, reason: provenanceValid };
  }

  // All three predicates passed: the receipt is authentic. Authenticity is
  // NOT admission -- an authentic receipt can still report a non-confirming
  // outcome, so the fourth condition below is mandatory and separate.
  if (candidateReceipt.lookupResult !== "IDENTITY_CONFIRMED") {
    return {
      verified: true,
      admitted: false,
      receiptId: candidateReceipt.receiptId,
      reason: `LOOKUP_RESULT_NOT_CONFIRMED: ${candidateReceipt.lookupResult}`,
    };
  }

  return { verified: true, admitted: true, receiptId: candidateReceipt.receiptId };
}

// Return type
interface ReceiptVerificationOutcome {
  verified: boolean;   // true iff all three predicates passed (receipt is authentic)
  admitted: boolean;   // true iff verified AND lookupResult === "IDENTITY_CONFIRMED"
  receiptId?: string;
  reason?: string;  // failure/non-admission reason code when admitted=false
}
```

Decision owner calls this function for every candidate with a receipt. Admission requires `admitted: true`, never `verified: true` alone: a receipt can be `verified: true, admitted: false` when it is authentic but reports `IDENTITY_REJECTED` or `IDENTITY_UNRESOLVED`, which must never be treated as a positive admission outcome.

### Python Persisted-Evidence Verification

At evidence-retrieval or audit time (Python runtime, persisted-evidence checker):

```python
def verify_receipt_evidence(
    receipt_json: dict,
    verifier_registry_snapshot: dict,
    source_registry_snapshot: dict,
    source_observation_log: dict,
    expected_current_round: str,
    expected_authority_hash: str,
    evaluation_time_utc: str,
    freshness_threshold_seconds: int,
) -> ReceiptVerificationOutcome:
    """
    Independently recompute all three predicates, then the separate
    admission-outcome check. Used by persisted-evidence checker and audit
    trails. Returns admitted=False with reason code on any failure or on
    an authentic non-confirming lookupResult.
    """

    # Predicate 1: Content Integrity (includes domain/profileVersion literal check)
    try:
        integrity_valid = check_content_integrity_python(receipt_json)
        if not integrity_valid:
            return ReceiptVerificationOutcome(
                verified=False,
                admitted=False,
                reason="INVALID_CONTENT_ENCODING"
            )
    except Exception as e:
        return ReceiptVerificationOutcome(
            verified=False,
            admitted=False,
            reason=f"INTEGRITY_CHECK_ERROR: {str(e)}"
        )

    # Predicate 2: Signature Validity (reconstructs preimage with this
    # contract's own fixed domain/profileVersion literals, never the
    # receipt's claimed values)
    try:
        signature_valid = check_signature_validity_python(
            receipt_json,
            verifier_registry_snapshot
        )
        if not signature_valid:
            return ReceiptVerificationOutcome(
                verified=False,
                admitted=False,
                reason="INVALID_SIGNATURE_OR_KEY"
            )
    except Exception as e:
        return ReceiptVerificationOutcome(
            verified=False,
            admitted=False,
            reason=f"SIGNATURE_CHECK_ERROR: {str(e)}"
        )

    # Predicate 3: Lookup Provenance (round-bound, freshness-checked, forked-observation-checked)
    try:
        provenance_valid = check_lookup_provenance_python(
            receipt_json,
            source_registry_snapshot,
            source_observation_log,
            expected_current_round,
            expected_authority_hash,
            evaluation_time_utc,
            freshness_threshold_seconds,
        )
        if provenance_valid != "VERIFIED":
            return ReceiptVerificationOutcome(
                verified=False,
                admitted=False,
                reason=provenance_valid
            )
    except Exception as e:
        return ReceiptVerificationOutcome(
            verified=False,
            admitted=False,
            reason=f"PROVENANCE_CHECK_ERROR: {str(e)}"
        )

    # All three predicates passed: the receipt is authentic. Authenticity
    # is NOT admission -- check the actual lookupResult value separately.
    if receipt_json.get("lookupResult") != "IDENTITY_CONFIRMED":
        return ReceiptVerificationOutcome(
            verified=True,
            admitted=False,
            receipt_id=receipt_json.get("receiptId"),
            reason=f"LOOKUP_RESULT_NOT_CONFIRMED: {receipt_json.get('lookupResult')}"
        )

    return ReceiptVerificationOutcome(
        verified=True,
        admitted=True,
        receipt_id=receipt_json.get("receiptId")
    )
```

The Python checker must independently recompute the JCS preimage (using its own fixed `domain`/`profileVersion` literals, never receipt-supplied values) and signature verification without trusting TypeScript decisions or audit summaries. `ReceiptVerificationOutcome.admitted` is the field callers must gate on; `verified=True, admitted=False` is a valid, expected outcome for an authentic non-confirming receipt, never an error.

## Adversarial Vector Matrix

### Vector AV-0: Genuine Confirmed Identity (Positive Control)

**Setup:** The Positive Test Vector above proves preimage/signature consistency. The remaining conditions are hypothetical: caller's round and trusted authority hash match, a fresh singly-observed source snapshot confirms `issuer-test-001` and its attested hash, and the fixture key is trusted and active.

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** PASS -- independently reconstructed and verified, see Positive Test Vector.

**Predicate 3 (Lookup Provenance):** VERIFIED only under the stated hypothetical source-owned snapshot and trusted-context assumptions; the published bytes alone do not prove it.

**Admission Outcome Binding:** `lookupResult == "IDENTITY_CONFIRMED"`, so `FinalAdmissionCheck` returns `{ admitted: true, reason: null }`.

**Admission Result:** VERIFIED and ADMITTED. This is the contract's sole positive-path example; every other vector below is a negative case that must resolve to `admitted: false`, either because a predicate fails (`verified: false`) or because the receipt is authentic but non-confirming (`verified: true, admitted: false`).

### Vector AV-1: Forged Content Hash (Self-Authored)

**Setup:** Attacker constructs a receipt object with all required fields but no verifier signature; computes SHA-256 of the fields.

**Predicate 1 (Content Integrity):** PASS -- fields are well-formed and ordered.

**Predicate 2 (Signature Validity):** FAIL -- `signedBy.signature` is absent or invalid. No Ed25519 verification performed.

**Predicate 3 (Lookup Provenance):** FAIL -- no source-owned observation log entry.

**Admission Result:** UNVERIFIED (predicate 2 failure). Content hash alone never authenticates a receipt.

### Vector AV-2: Signature Under Receipt-Supplied Key

**Setup:** Receipt includes a public key in a supplemental field; signature is valid under that key; claims verifier issuance.

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** FAIL -- key registry lookup fails because `signatureKeyId` does not exist in the trusted registry. Receipt-supplied key is rejected before verification.

**Predicate 3 (Lookup Provenance):** FAIL -- even if provenance check were reached, receipt-provided key authority is not a source-owned observation.

**Admission Result:** UNVERIFIED (predicate 2 failure). Receipt-supplied keys are never accepted.

### Vector AV-3: Valid Signature Under Revoked Key

**Setup:** Receipt is signed with a key that was revoked before receipt issuance; signature is cryptographically valid.

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** FAIL -- the called `SignatureValidityCheck` rejects the key before Ed25519 verification because its registry record has:
  - `revokedAt <= receipt.receiptIssuanceTimeUtc` (true)
  - Result: key was revoked before receipt creation
  - Verification rejected before Ed25519 check

**Predicate 3 (Lookup Provenance):** FAIL -- provenance check never reached.

**Admission Result:** UNVERIFIED (predicate 2 failure on key lifecycle).

### Vector AV-4: Modified Signature keyId

**Setup:** Receipt is valid; attacker modifies `signatureKeyId` to point to a different key; signature still corresponds to original key.

**Predicate 1 (Content Integrity):** PASS -- fields are well-formed.

**Predicate 2 (Signature Validity):** FAIL -- an envelope/preimage key-ID mismatch is rejected before registry lookup. If both IDs are changed consistently, the signed preimage changes and Ed25519 verification fails; duplicate IDs or public-key aliases also fail closed.

**Predicate 3 (Lookup Provenance):** FAIL -- provenance check never reached.

**Admission Result:** UNVERIFIED (predicate 2 failure).

### Vector AV-5: Fabricated Lookup Result

**Setup:** Receipt contains:
  - Valid signature under verifier key
  - `lookupResult = "IDENTITY_CONFIRMED"` (falsely positive)
  - Source-owned snapshot hash that is valid
  - But the actual registry at that snapshot does not contain the issuer, or contains a negative result

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** PASS -- verifier signature is valid.

**Predicate 3 (Lookup Provenance):** FAIL -- source registry lookup is recomputed:
  - Snapshot is retrieved and hash verified
  - Registry is queried for `issuerIdentity` in that snapshot
  - Result does not match `lookupResult = "IDENTITY_CONFIRMED"`
  - Provenance check returns UNVERIFIED

**Admission Result:** UNVERIFIED (predicate 3 failure).

### Vector AV-6: Stale Registry Snapshot

**Setup:** Receipt references a registry snapshot from 30 days ago; current registry state has changed; lookup was never performed on current state.

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** PASS.

**Predicate 3 (Lookup Provenance):** FAIL -- source observation log is checked:
  - Snapshot was observed and hash matches
  - But `observedAt` timestamp is older than configured freshness threshold
  - Provenance check returns UNVERIFIED (STALE_SNAPSHOT)

**Admission Result:** UNVERIFIED (predicate 3 failure on age).

### Vector AV-7: Forked Observation Chain

**Setup:** Verifier creates two receipts for the same issuer in the same round, each binding a different snapshot. One was created after a temporary partition; both have valid signatures and valid snapshots, but only one matches the authoritative source observation log.

**Predicate 1 (Content Integrity):** PASS for both.

**Predicate 2 (Signature Validity):** PASS for both.

**Predicate 3 (Lookup Provenance):** PASS for the receipt that matches source-owned observation; FAIL for the forked receipt:
  - Source observation log does not contain the forked snapshot
  - Provenance check returns UNVERIFIED (SNAPSHOT_NOT_IN_SOURCE_LOG)

**Admission Result:** Only the receipt matching authoritative observation is VERIFIED.

### Vector AV-8: Cross-Round Receipt Replay

**Setup:** Receipt from round N is replayed in round N+1; signature is still valid; `verificationRound` field is unchanged at `N`.

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** PASS.

**Predicate 3 (Lookup Provenance):** FAIL, deterministically -- `LookupProvenanceCheck`'s first step compares `receipt.verificationRound` (`N`) against the caller-supplied `expectedCurrentRound` (`N+1`, the decision owner's actual current round, never read from the receipt). They differ, so the function returns `UNVERIFIED` (`ROUND_MISMATCH`) immediately, before the snapshot/hash/freshness/authority/lookup steps ever run.

**Admission Result:** UNVERIFIED (predicate 3 failure, `ROUND_MISMATCH`), unconditionally -- this is a hard, always-enforced round-binding check, not a conditional or registry-state-dependent outcome.

### Vector AV-9: Invalid JCS Canonicalization

**Setup:** Receipt preimage uses a different JSON canonicalization (e.g., alphabetic vs. sorted-by-frequency); signature was computed over the different preimage.

**Predicate 1 (Content Integrity):** PASS -- individual fields are valid.

**Predicate 2 (Signature Validity):** FAIL -- verification recomputes preimage using RFC 8785 JCS; preimage does not match the signed bytes; Ed25519 verification fails.

**Predicate 3 (Lookup Provenance):** FAIL -- never reached.

**Admission Result:** UNVERIFIED (predicate 2 failure on canonicalization mismatch).

### Vector AV-10: Unavailable Verifier Registry

**Setup:** Verifier registry is inaccessible (network failure, deletion, etc.); receipt exists and is otherwise valid; but `signatureKeyId` cannot be resolved.

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** FAIL -- registry lookup fails; key cannot be retrieved; verification halts with UNVERIFIED (KEY_NOT_FOUND or REGISTRY_UNAVAILABLE).

**Predicate 3 (Lookup Provenance):** FAIL -- never reached.

**Admission Result:** UNVERIFIED (predicate 2 failure). System fail-closed until registry is available.

### Vector AV-11: Authentic Receipt, Genuinely Rejected Identity

**Setup:** The Negative Test Vector counterpart above uses the same key and snapshot identity but a different issuer (`issuer-test-rejected-002`). Under the same hypothetical source-owned snapshot, that issuer and its attested hash resolve to `IDENTITY_REJECTED`; the published bytes alone do not prove the registry state.

**Predicate 1 (Content Integrity):** PASS.

**Predicate 2 (Signature Validity):** cryptographic Ed25519 check PASS under the same published test-fixture key as AV-0; full Predicate 2 additionally assumes a trusted active registry record with the required lifecycle and role checks.

**Predicate 3 (Lookup Provenance):** VERIFIED only under the stated hypothetical trusted context and source-owned snapshot in which the second issuer resolves to `IDENTITY_REJECTED`; the published vector does not itself prove those premises.

**Admission Outcome Binding:** if all three predicates pass under those premises, the receipt is authentic (`verified: true`). But `lookupResult != "IDENTITY_CONFIRMED"`, so `FinalAdmissionCheck` returns `{ admitted: false, reason: "LOOKUP_RESULT_NOT_CONFIRMED: IDENTITY_REJECTED" }`.

**Admission Result:** conditionally verified=true, ADMITTED=false; without trusted registry and observation premises, verified=false and ADMITTED=false. Under the conditional premises, this is the vector that a three-predicate design without outcome binding would incorrectly treat as equivalent to AV-0. The mandatory, separate Admission Outcome Binding check prevents an authentic rejection from being admitted.

## Findings or Position

The three-predicate design (content integrity, signature validity, lookup provenance) closes the specific gap that T2B-RV-F1 identified in the T2B calibration-root contract: a self-authored content hash alone cannot authenticate a verifier claim. Separating signature validity from lookup provenance means a cryptographically valid signature is necessary but never sufficient; admission additionally requires an independently recomputed, source-owned registry observation that matches the receipt's claimed `lookupResult`. A prior revision of this design stopped there and returned `{ verified: true }` as soon as all three predicates passed, which meant an authentic, provenance-matched receipt for a genuinely rejected identity (AV-11) was indistinguishable in outcome from a genuinely confirmed one (AV-0); Codex's review caught this and it is fixed here by the mandatory, separate Admission Outcome Binding step, which requires `lookupResult == "IDENTITY_CONFIRMED"` before `admitted: true` is ever returned. The design also previously left `domain`/`profileVersion` as prose labels outside the signed preimage and left round-binding and freshness checks stated only in adversarial-vector prose rather than as real steps in `LookupProvenanceCheck`; both are now bound directly into the preimage (`domain`, `profileVersion` fields) and the algorithm (`expectedCurrentRound`, `evaluationTimeUtc`, `freshnessThresholdSeconds` parameters), so AV-8 (cross-round replay) and AV-6 (stale snapshot) now resolve deterministically from the pseudocode itself rather than from narrative description alone. Of the twelve adversarial vectors in the matrix above, AV-0 is the sole positive control (`VERIFIED` and `admitted: true`); AV-1 through AV-4, AV-9, and AV-10 fail Predicate 2; AV-5 through AV-8 fail Predicate 3; AV-7's authoritative branch and AV-11 both reach `verified: true`, but AV-11 is correctly denied admission by the Admission Outcome Binding check while AV-7's authoritative branch (whose `lookupResult` is `IDENTITY_CONFIRMED` in that vector's setup) is admitted. The design's position is that this contract is sound as a specification and its own worked positive/negative vectors independently reconstruct and verify, but every operational dependency it relies on (key registry, observation log, issuer registry) remains unverified, so the contract cannot be operated yet.

## Risk / Corrective Action

**Primary risk:** the contract is hypothetical only. Nothing prevents someone from treating a passing content-integrity check, on its own, as sufficient evidence of a genuine verifier claim, unless callers enforce all three predicates conjunctively as specified in the Admission Rule, and unless the separate Admission Outcome Binding check is also applied so that an authentic-but-rejected receipt (AV-11) is never treated as equivalent to a confirmed one (AV-0).

**Repaired defects (this revision):** two review-confirmed gaps are closed above and are not merely documented as future work: (1) admission previously returned `{ verified: true }` for any receipt whose three predicates passed regardless of the actual `lookupResult` value, meaning a genuinely signed, provenance-matched `IDENTITY_REJECTED` receipt was indistinguishable from a confirmed one; this is closed by the mandatory Admission Outcome Binding step and the `verified`/`admitted` field split. (2) the signed preimage previously carried no `domain`/`profileVersion` fields and `LookupProvenanceCheck` had no real round-binding or freshness parameters, so cross-domain replay resistance and round/freshness enforcement existed only as adversarial-vector prose, not as algorithm steps; this is closed by adding `domain`/`profileVersion` to the preimage and `expectedCurrentRound`/`evaluationTimeUtc`/`freshnessThresholdSeconds` to `LookupProvenanceCheck`, and by publishing a reconstructible positive vector (AV-0) alongside its rejected counterpart (AV-11).

**Corrective action:** before any implementation, a separate source-verification tranche must establish a real owner and location for the verifier key registry, the source-owned observation log, and the issuer registry (see Owner Ledger below). Until each of those is source-verified, no keys should be created, no signer wired, and no receipts issued or accepted under this contract.

## Owner Ledger

| Responsibility | Owner | Status |
|---|---|---|
| Verifier private key custody and rotation | CVF key-governance authority | **BLOCKED_SOURCE_NOT_FOUND** |
| Verifier public-key registry creation and write authority | CVF key-governance authority | **BLOCKED_SOURCE_NOT_FOUND** |
| Registry snapshot identity and observation logging | Source-owned authority (decision owner) | **BLOCKED_SOURCE_NOT_FOUND** |
| Issuer registry content and lookup semantics | Issuer/authority decision owner | **BLOCKED_SOURCE_NOT_FOUND** |
| Receipt issuance verification function (TypeScript) | G1 implementation owner (future) | unassigned |
| Receipt evidence verification function (Python) | G1 evidence checker owner (future) | unassigned |
| Receipt archival and historical access | Evidence custody owner (future) | unassigned |
| Key revocation and timeline validation | Key-governance authority | **BLOCKED_SOURCE_NOT_FOUND** |

All operational dependencies remain explicitly unverified. This design specifies interfaces only.

## Parked Evidence Reconciliation

T2B (CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17) proposed a receipt using only content integrity (SHA-256) without verifier signature or source-owned lookup. T2B-RV-F1 demonstrates that a self-authored receipt with a valid content hash alone cannot authenticate a verifier claim. This design rejects T2B's sufficiency claim and introduces signature validity and lookup provenance as separate mandatory predicates.

Ten prior parked G1 evidence paths (T2, T2A) are read-only and unaffected by this hypothetical design. No repair, acceptance or promotion of those paths is authorized.

## Claim Boundary

This is hypothetical documentation only. It does not create keys, operate a registry, authorize signer wiring, perform lookups, or claim an existing CVF owner for any operational dependency. All keys, registry, lookup, and implementation remain explicitly parked until separate source-backed authority is established.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private held design packet; no public-sync authority.
