# CVF ACEL G1 T3A-C2 Ceremony Product Local Verification

Memory class: governed-audit

Status: LOCAL_VERIFIED_SOURCE_CREATION_NOT_AUTHORIZED_BY_THIS_ARTIFACT

Date: 2026-09-19

Owner: Local orchestrator/reviewer

## Purpose

Record the secret-safe Local verification of the operator-run Party A Ed25519
ceremony and decide whether its public product is fit to become the sole input
to a separately governed Group 1 source-creation tool.

## Scope / Methodology

The operator ran the committed ceremony as the exact non-admin principal and
returned only `party_a_public_key.json`. Local normalized chat transport
escaping, strictly decoded the unpadded base64url public key, recomputed its
SHA-256 digest, checked the principal binding and validity interval, and
compared all disposition fields with the T3A-C1 and T2F boundaries.

No password, DPAPI blob, plaintext private key or Party A profile was accessed.
Local did not run as Party A and did not create a registry row, lifecycle
receipt, source directory, signature, candidate admission or runtime effect.

## Target / Source

| Source | Authority | Use |
|---|---|---|
| operator-returned `party_a_public_key.json` | ceremony public product | exact field and digest verification |
| `scripts/acel_g1_party_a_key_ceremony.ps1` | accepted ceremony implementation | output semantics and claim boundary |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 1 contract | registry/lifecycle schema and Party A writer boundary |
| `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` | accepted route decision | fresh-key and private-custody choice |

## Verified Public Metadata

```json
{
  "metadataSchema": "cvf.acel.g1.partyAPublicKeyMetadata@1",
  "metadataProfile": "ACEL_G1_T3A_PRINCIPAL_BOUND_CEREMONY",
  "keyId": "partya-44853ea9a690452c",
  "algorithm": "Ed25519",
  "principalName": "LAM-RUBY\\cvf-g1-party-a",
  "principalSid": "S-1-5-21-1644666849-912006174-747199667-1006",
  "publicKeyBytesBase64": "R5AsDnHQNXWgD5WQEpDi3VABiuPZ7E9U5Kir_bgiwNU",
  "publicKeySha256Hex": "5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01",
  "createdAtUtc": "2026-09-19T06:41:05.5102754Z",
  "expiresAtUtc": "2027-09-19T06:41:05.5102754Z",
  "ceremonyDisposition": "CEREMONY",
  "testDisposition": "CEREMONY_PRODUCT_PENDING_LOCAL_VERIFICATION",
  "registryDisposition": "SOURCE_NOT_CREATED",
  "claimBoundary": "public metadata only; no registry row, lifecycle receipt, promotion or admission is claimed"
}
```

This copy is public metadata evidence only. It is not a registry row and does
not change the source disposition by its presence in this audit.

## Verification Evidence

| Check | Observed | Disposition |
|---|---|---|
| base64url canonical shape | 43 unpadded characters | PASS |
| decoded public-key length | 32 bytes | PASS |
| independent SHA-256 | `5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01` | PASS, exact match |
| algorithm | `Ed25519` | PASS |
| principal | `LAM-RUBY\cvf-g1-party-a` | PASS |
| SID | `S-1-5-21-1644666849-912006174-747199667-1006` | PASS |
| validity | 2026-09-19 through 2027-09-19, exactly 365 days | PASS |
| custody | DPAPI CurrentUser path reported by accepted tool; private artifact not returned | PASS_BOUNDARY |
| source state | `SOURCE_NOT_CREATED` | PRESERVED |
| admission state | no promotion or admission claimed | PRESERVED_UNVERIFIED |

Recomputation used strict base64url normalization followed by
`SHA256(decoded_public_key_bytes)`. The 32-byte result and digest both match
the ceremony output; this is independent verification of the public product,
not proof of private-key possession by Local.

## Findings / Position

The ceremony public product is internally coherent, principal-bound and fit
as input to Group 1 source-creation tooling. The operator checkpoint required
before opening Future T3A is satisfied.

T2F still requires Party A exclusively to perform the registry and lifecycle
write. Therefore Local selects a bounded successor: implement and hermetically
test principal-bound Group 1 source-creation tooling, then return to the
operator for the real source write. Direct Local or worker creation of the
operational registry is rejected.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| public metadata mistaken for established source | retain `SOURCE_NOT_CREATED` until Party A creates and Local verifies both governed source files |
| worker impersonates Party A | worker builds tooling and tests only; real execution remains an operator checkpoint |
| private material leaks into repository | successor tool reads only public metadata for registry creation and never copies DPAPI/private material |
| registry row or chain hash drifts from T2F | require exact closed preimages, independently recomputed positive vector and mutation tests |
| source creation overclaims consumer wiring | T3A creates/verifies Group 1 only; candidate admission stays `UNVERIFIED` and T3E remains separate |

## Decision / Disposition

Decision: `CEREMONY_PRODUCT_LOCAL_VERIFIED`.

Successor decision: `OPEN_T3A_C2_GROUP1_SOURCE_CREATION_TOOLING`.

The ceremony checkpoint is closed. Group 1 remains `SOURCE_NOT_CREATED`; no
registry row, lifecycle receipt, key promotion, candidate admission, live
governance proof, public sync or deployment is authorized by this audit.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace plus operator-returned public metadata |
| Session or invocation | ACEL G1 T3A-C2 local verification, 2026-09-19 |
| Working directory | repository root |
| Command or tool surface | governed reads, strict base64url decode, SHA-256 recomputation, bounded searches |
| Target paths | this audit only |
| Allowed scope source | active handoff next move and operator execution of accepted ceremony |
| Before status evidence | ceremony tooling committed; Party A source absent; thirteen parked paths present |
| After status evidence | public verification audit added; source paths still absent |
| Diff evidence | one audit artifact; no credential/source/runtime path changed |
| Approval boundary | Local verification and successor selection only |
| Claim boundary | public metadata verified; private possession and source establishment not claimed |
| Agent type | Local reviewer/decision owner |
| Invocation ID | `acel-g1-t3a-c2-local-verification-20260919` |
| Expected manifest | this audit |
| Actual changed set | this audit |
| Manifest delta | MATCH |

## Claim Boundary

This artifact proves only public-metadata coherence and closes the ceremony
product verification checkpoint. It does not prove or create an operational
source, verifier-consumer wiring, candidate admission, runtime use, public
export or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance for a local principal and a not-yet-created
source; no public artifact is authorized.
