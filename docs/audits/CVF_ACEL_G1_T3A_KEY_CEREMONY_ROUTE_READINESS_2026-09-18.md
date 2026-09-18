# CVF ACEL G1 T3A Key Ceremony Route Readiness

Memory class: governed-local-audit

docType: audit

Status: ROUTE_SELECTED_IMPLEMENTATION_HOLD

Date: 2026-09-18

Decision base HEAD: `5e955b3a0f723ea90ff1591178a6359dfb2ef32b`

Decision owner: Local orchestrator/reviewer for route selection; operator for concrete principal, custody target, ceremony authorization and any key operation.

## Purpose

Select the next ACEL G1 Group 1 source-establishment route after T2H design-only acceptance, without creating a source, key, principal, credential or implementation work order.

## Target / Source

| Governed source | Decision-relevant evidence |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md` | Dependency 1 and Rejected-Adjacent Candidates: no existing verifier signing-key custody/public-key registry owner found in its bounded search; HMAC and agent-credential mechanisms do not satisfy the asymmetric trust model. |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party A is `CVF Operator / repository owner` for Contracts 1+2, but the appointment explicitly does not provision a principal, key or registry. |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 1 schema, two proposed future paths, `SOURCE_NOT_CREATED`/`UNVERIFIED` disposition and Proposed Implementation Order: T3A requires a concrete Party A principal and key generation/import ceremony authorization before opening. |
| `docs/reviews/CVF_ACEL_G1_T2H_PARTY_B_IMMUTABLE_OBSERVATION_RECONCILIATION_WORKER_RETURN_2026-09-18.md` | Local Reviewer Completion Disposition: Party B observation condition is accepted without operational-source claim. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Current next move permits bounded Local selection; source, principal, key and implementation remain parked. |

## Scope / Methodology

Compared four routes against source existence, provenance, identity separation, implementation prerequisites and reversible documentation scope. Read the above named owner/contract sections and ran a bounded source-code query over `governance` and `EXTENSIONS` for `ed25519|verifier.?key.?registry|key.?ceremony` in Python, TypeScript and JSON files, excluding dependencies/build outputs; it returned no match. Literal `Test-Path` checks for `governance/sources/verifier_key_registry/REGISTRY.json` and `governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl` both returned `False` at the decision base. These checks do not certify global absence outside the searched roots or approve either proposed path for creation.

## Findings / Position

| Route | Decision | Reason |
|---|---|---|
| Reuse the adjacent Web HMAC or agent-credential store | REJECT | T2D already establishes a trust-model mismatch; neither is an Ed25519 public-key registry with source-owned lifecycle evidence. |
| Import an existing signing key | DEFER_WITH_REASON | No external key identity, custodian, provenance, export policy or rotation history was supplied for independent Local verification. Import would silently promote unknown prior custody into Group 1 authority. |
| Generate a fresh dedicated signing key under Party A control | SELECT_DESIGN_ONLY | Starts a distinct lifecycle under the already appointed accountable Party A, permits an explicit genesis receipt and avoids relying on unverified prior custody. This selects the future ceremony route, not a key algorithm implementation, storage provider, principal identifier or permission grant. |
| Open T3A source implementation now | REJECT_CURRENTLY | T2F's explicit checkpoint is not met: a role label is not a concrete write/sign principal, and no custody target or generation ceremony authorization has been recorded. |

## Decision / Disposition

Decision: `SELECT_NEW_KEY_CEREMONY_ROUTE_T3A_HOLD`.

For a future T3A packet, use a newly generated Ed25519 signing key whose private material remains outside the repository and outside governed receipts; Group 1 may publish only the public key and lifecycle evidence under the accepted source contract. Party A remains the accountable owner. A dedicated operator-controlled write/sign principal must be identified and its separation from Party B and Party C evidenced before opening T3A. The exact principal identifier, custody system, generation venue, access policy, rotation/revocation procedure and first ceremony authorization remain operator checkpoints; this audit chooses none of those facts on the operator's behalf. The two Group 1 paths remain `PROPOSED_LOCAL_REVIEW`, not approved operational paths.

No worker work order is dispatchable from this decision. The next permissible action is an operator checkpoint that supplies the concrete Party A principal and custody/ceremony boundary; Local then authors a fresh GC-018 baseline and bounded T3A work order for independent review before any implementation or key operation.

## Risk / Corrective Action

| Risk | Required control |
|---|---|
| role label mistaken for provisioned identity | require exact principal identifier and permission-separation evidence; keep Group 1 `SOURCE_NOT_CREATED` |
| private key committed or echoed in logs/receipts | require a separately approved custody system and secret-safe ceremony; record only public key and non-secret receipt fields |
| imported or pre-existing key accepted on assertion | require independent provenance and custody proof before any future import option can replace the selected route |
| Group 1 build mistaken for G1 admission | T3B-T3E and Local source verification remain separate; candidate admission stays `UNVERIFIED` |
| parked evidence altered during this choice | thirteen pre-existing untracked G1 paths are not owned or modified by this audit |

## Evidence And Claim Boundary

This is a bounded route-selection audit, not a complete repository inventory or a key-management standard. The source query and literal path checks are negative evidence only for the named roots and two exact paths. At the decision base, no private key was accessed, generated, imported, rotated or disclosed; no principal was provisioned; no registry, lifecycle log, verifier consumer or runtime was created or tested.

## Post-Decision Local Test Custody Evidence

After the route decision, the operator stated that no dedicated account or
custody system existed and authorized a temporary private local test setup.
Local created one new Ed25519 test key under the current Windows user, with
the raw private key stored only as a per-user Windows DPAPI-encrypted blob
outside the repository under that user's LocalAppData. A separate public
metadata file identifies it as `CVF_G1_PARTY_A_LOCAL_TEST`, with
`keyId=localtest-f35b819837f7f207` and public-key SHA-256
`f35b819837f7f207378d85bfd53e0dc2778c0e187e422441f687ba29ec8a36c9`.
The exact local custody path is intentionally not a governed source path.

The custody directory has protected ACL inheritance and grants the current
Windows user full control; the encrypted file inherits only that grant. A
fresh process read the ciphertext, decrypted it with the same user's DPAPI
context, reconstructed the public key, matched both public metadata fields,
signed a fixed challenge and verified the Ed25519 signature: PASS. No private
bytes, signature seed, or decrypted key were printed or committed.

This is a `TEST_ONLY_NON_OPERATIONAL` principal, not a new Windows account or
a separated Party A operational identity. Another process running as the same
Windows user could use that user's DPAPI context; filesystem ACLs do not
separate agents sharing the user. The temporary key therefore cannot become
the Group 1 trust anchor merely by copying its public metadata. No registry
row, lifecycle receipt, Party B observation, verifier lookup, candidate
admission, source creation or T3A implementation was authorized or produced.
Group 1 remains `SOURCE_NOT_CREATED`; the operational T3A work-order checkpoint
for a distinct principal, custody and secret-safe ceremony remains open.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision with no public artifact or export authorization.

## Claim Boundary

The selected new-key route is a future design preference subject to operator checkpoint and a fresh governing packet. Group 1 remains `SOURCE_NOT_CREATED`; candidate admission remains `UNVERIFIED`. T2H does not confer operational authority.
