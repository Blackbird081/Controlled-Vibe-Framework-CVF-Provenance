# CVF ACEL G1 T2C Verifier Trust Anchor Local Architecture Decision

Memory class: governed-local-architecture-decision

docType: review

Status: DECIDED_DESIGN_ONLY

Date: 2026-09-17

Decision owner: Local orchestrator/reviewer

Review base HEAD: `eec5f01825cfdea258b53f6a663b2237f476dd18`

## Purpose

Select the missing issuer-authentication architecture after G1 T2B was
terminally parked. This decision is planning authority for a separate
documentation-only T2C packet, not an implementation or live-key grant.

## Target / Source

| Source | Verified locator | Use |
|---|---|---|
| `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_INDEPENDENT_REVIEW_2026-09-17.md` | T2B-RV-F1 and read-only counterexample | controlling Local rejection and required trust boundary |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | IssuerVerificationReceipt and Checker And Test Contract | rejected advisory design, not authority to implement |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `computeServiceRequestSignature`, `verifyServiceTokenRequest` | source-visible example that authentication requires a verifier-held secret plus timestamp; not a G1 owner or direct import |
| `docs/work_orders/CVF_WO_RTA1_RECEIPT_TRACE_ANCHOR_2026-06-06.md` | receipt integrity and claim boundary | content hash and optional HMAC are distinct from external issuer proof |
| RFC 8032 (`https://www.rfc-editor.org/info/rfc8032/`) | Ed25519 signing, verification, test vectors | external algorithm pattern only, not CVF owner authority |

## Scope / Methodology

Local compared the T2B forged-receipt counterexample with existing CVF
authentication and receipt-integrity patterns. The decision separates content
integrity, signer authentication and lookup truth. It does not assert an
existing G1 verifier key registry, signer runtime, private key or live lookup.
The thirteen untracked G1 evidence paths remain untouched.

Role: Local orchestrator/reviewer. Phase: post-T2B architecture selection.
Decision owner: Local. A future shared-workspace worker would be an
`INTERNAL_AGENT`, not an external research agent.

## Findings / Position

An ordinary SHA-256 digest over receipt fields is publicly recomputable and
cannot authenticate `verifiedBy` or `lookupResult`. A second role literal or
separate receipt object does not change that. The existing service-token
source demonstrates a different, scoped authentication mechanism: verification
uses secret-held HMAC and time, not the public hash alone. It is not a G1
issuer-verification owner. RTA1 likewise keeps local receipt integrity from
external proof. An asymmetric signature is selected for the T2C design
because a future Python persisted-evidence checker can verify with a trusted
public key without holding the signer's private key. RFC 8032 supplies the
Ed25519 algorithm and vectors; it does not supply CVF key governance.

## Local Architecture Decision

Select `Ed25519`-signed verifier receipts with a separately governed,
verifier-controlled signing key and a locally trusted public-key registry.
The future T2C design must satisfy all of the following; omission is
fail-closed, not a documentation note:

1. The verifier, not the candidate or authority issuer, creates the receipt
   only after a genuine decision-owner registry lookup. Signature alone
   authenticates the verifier-held key, not the truth of the lookup; the
   design must separately bind a source-owned lookup result and provenance.
2. Sign one domain-separated, versioned, deterministic UTF-8 canonical
   preimage binding round identity, exact authority hash, issuer identity,
   authority-attestation hash, registry snapshot identity/hash, lookup result,
   observation time, receipt issuance time, and unique receipt identity.
   The signature and key ID are not part of their own signed preimage.
3. A `keyId` may only select a public key from a trusted CVF-owned verifier
   key registry supplied independently of candidate, authority and receipt
   content. Never accept a receipt-supplied public key, candidate-provided
   registry path, self-asserted `verifiedBy`, or self-computed SHA-256 as
   authentication.
4. Both TypeScript decision-time admission and Python persisted-evidence
   checking verify the Ed25519 signature against the same specified preimage,
   key identity, role, validity interval and revocation state. Unknown,
   revoked, expired, malformed, mismatched or unavailable trust material is
   `UNVERIFIED` and bars candidate evaluation. Historical verification and
   later revocation semantics must be explicit, never inferred from a hash.
5. The key registry's owner, source path, write authority, rotation and
   revocation mechanism are not established by this decision. A T2C worker
   must source-verify them or return `BLOCKED_SOURCE_NOT_FOUND`; it must not
   invent a live registry, generate a key or silently reuse Web service-token
   credentials. Key creation, storage, rotation and live signer wiring require
   their own operator-governed implementation authority.

The rejected alternatives are a public content hash plus role literal; a
bare mutable verification-status flag; a receipt that includes its own
untrusted public key; and direct use of the existing Web HMAC token as a G1
signing credential. The selected path adds no live/secret capability now.

## Acceptance Boundary For A Later T2C Design Packet

The next documentation-only packet may define schema, exact preimage,
trusted-registry lookup contract, independent TypeScript/Python verification
responsibilities, key-lifecycle and negative vectors. It must include a
forged-receipt test: self-authored fields with a valid SHA-256 content hash
but no verifier signature fail admission. It must also reject a valid
signature under a receipt-supplied or revoked key. It may not claim an
implemented lookup, signer, key registry or accepted G1 root contract. No
T2B worker repair or automatic implementation successor is authorized.

## Risk / Corrective Action

Ed25519 prevents the specific public-hash forgery only when the verifier's
private key is protected and the public key is obtained from a trusted,
independently governed source. The key owner and lifecycle are currently
unverified; the corrective action is a separate source-verification/design
tranche, with fail-closed return if those owners cannot be established.

## Negative Search And Collision Discipline

- Exact search roots: `docs`, `governance`, `EXTENSIONS`, and targeted
  `CVF_SESSION` continuity pointers. Coverage included source, tests, docs,
  JSON and current Local evidence; no external repository corpus is claimed.
- Exact search command: `rg -n --hidden 'verifierKeyRegistry|issuerVerifierPublicKey|issuerVerifierPrivateKey|VERIFIED_BY_LIVE_REGISTRY_LOOKUP|IssuerVerificationReceipt|Ed25519' docs governance EXTENSIONS CVF_SESSION`.
- Search boundary: focused `rg -n --hidden` over `docs`, `governance`, and
  `EXTENSIONS` for `verifierKeyRegistry`, `issuerVerifierPublicKey`,
  `issuerVerifierPrivateKey`, `VERIFIED_BY_LIVE_REGISTRY_LOOKUP`,
  `IssuerVerificationReceipt`, and `Ed25519`; session-state copies were
  excluded from owner selection. This is a targeted owner search, not a
  complete-corpus absence claim.
- Positive collision: T2B audit/manifest and worker-return documents define
  an `IssuerVerificationReceipt` and use the derived verification-status
  literal. The independent Local review proves that this design permits a
  forged receipt; these paths cannot be promoted to trust-anchor authority.
- Same-token collision disposition: `T2C` occurs in unrelated historical
  tranche identifiers elsewhere in the repository; those occurrences are
  non-authoritative for this ACEL G1 trust-anchor decision, not evidence that
  this exact design owner already exists. T2B's receipt/status literals are
  collisions with the rejected design, not an authenticated verifier owner.
- Adjacent but non-owner collision: Web `service-token-auth.ts` authenticates
  requests with HMAC under a different purpose; RTA1 addresses local receipt
  integrity. Neither establishes a G1 verifier-key registry or live issuer
  lookup owner.
- Negative result: the targeted search found no source-verified G1
  `verifierKeyRegistry`, `issuerVerifierPublicKey`, or
  `issuerVerifierPrivateKey` owner. Therefore registry location, key custody,
  rotation, revocation and lookup provenance remain `BLOCKED_SOURCE_NOT_FOUND`
  for a later design packet. This is not a claim that such material cannot
  exist elsewhere in the private corpus or operating environment.
- Absent-versus-collision disposition: exact G1 verifier-key owner symbols
  were absent in the searched roots; related receipt/status terms collided
  with T2B's rejected proposal and unrelated `T2C` labels. None supplies
  the independently governed key or genuine lookup provenance required here.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | review status, Purpose/Target/Scope/Findings/Risk/Claim headings; Agent Operation Trace labels; Delta Execution eight-field labels |
| gateRunPurpose | confirm packet shape after Local source and trust-boundary decision |
| claimBoundary | checker pass does not create a key owner, lookup or signer |

## Gate And Commit Disposition

The T2C artifact's markdown-structure, epistemic-process, operation-trace,
delta-claim and dispatch-quality gates pass. A separate, narrow retrospective
annotation to the tracked G2 fresh-direct-calibration work order records that
its dispatch-time filesystem state was not observed, then distinguishes the
recoverable worker-start/Git evidence from that gap. It does not claim a
prospective dispatch check or reopen G2. No T2C work order or worker dispatch
is authorized by this decision.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace; RFC Editor read-only standard reference |
| Session or invocation | G1 T2C trust-anchor architecture selection, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | current continuity and T2B review reads, focused owner search, RFC 8032 read, apply_patch and governance gates |
| Target paths | this Local decision only; thirteen G1 evidence paths read-only |
| Allowed scope source | operator request to continue after T2B terminal parking; next allowed move is Local separate trust-anchor architecture decision only |
| Before status evidence | HEAD `eec5f0182`; thirteen frozen untracked G1 evidence paths; staging empty |
| After status evidence | this decision-only document pending review/commit; no key material or implementation created |
| Diff evidence | exact one-path decision artifact |
| Approval boundary | architecture choice and future documentation-packet input only |
| Claim boundary | no implementation, key creation, registry lookup, provider/live, runtime, public sync or deployment |
| Agent type | Local decision owner |
| Invocation ID | `acel-g1-t2c-verifier-trust-anchor-local-decision-20260917` |
| Expected manifest | this decision path only |
| Actual changed set | this decision path only |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Epistemic Process Block

- Expected Result / Prediction: separating verifier-held signing authority
  from public content hashing should defeat the T2B self-authored receipt.
- Evidence Comparison: T2B's complete forged receipt had a valid SHA-256 but
  no secret/private-key proof; current CVF Web HMAC checks a held secret,
  while RFC 8032 defines independently verifiable public-key signatures.
- Contradiction or Gap Disposition: select Ed25519 as future design direction,
  but mark CVF key-registry ownership and lifecycle unverified; a later
  packet must fail closed rather than treating algorithm choice as an owner.
- Claim Update: Local architecture selected; no T2C work order, signer,
  live registry, key or G1 implementation is authorized by this artifact.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Local trust-anchor architecture decision only |
| claimDisposition | CLAIM_REJECTED: no implemented authentication claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no verifier signature or live registry receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused source review and architecture selection only |
| invocationBoundary | local documentation and read-only RFC access |
| interceptionBoundary | no runtime, provider, OS, CLI-worker or MCP interception claim |
| claimLanguage | Ed25519 is a selected future design direction, not a CVF capability |
| forbiddenExpansion | keys, live lookup, implementation, G4, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Local architecture decision; no public-sync authority.

## Claim Boundary

This document selects a future trust-anchor topology only. It does not make
T2B accepted, prove a key registry exists, authorize key/secret handling, or
dispatch a worker. All later implementation and live authority remain parked.
