# CVF ACEL G1 T2D Source-Owner Options

Memory class: governed-worker-audit

docType: audit

Status: HYPOTHETICAL_OPTIONS_ANALYSIS_ONLY

Date: 2026-09-18

dispatchBaseHead: `e8a446e9c11a6912dd1d593e73369402e56a3190`

## Purpose

Produce a source-backed, four-dependency owner-option analysis for the T2C
accepted hypothetical verifier trust-anchor contract
(`docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`,
Owner Ledger). This document does not appoint an operational owner, create a
key, perform a live lookup, or admit any candidate. Operator retains all
accountable-role assignment.

## Target Under Review

The four unresolved operational dependencies named in T2C's Owner Ledger:
(1) verifier signing-key custody, rotation and public-key registry write
authority; (2) an independently trusted `verificationAuthorityHash`
specification and decision-owner binding; (3) source-owned registry snapshot
identity and observation log; (4) genuine issuer registry content and lookup
semantics. Per the work order, key custody and registry write authority are
analyzed as separable accountable questions where their owners could
plausibly differ.

## Scope / Methodology

Documentation-only current-repository search. Search roots: `docs`,
`governance`, `EXTENSIONS`, `ECOSYSTEM`. The source-code query executed was
exactly:

```
rg -n --hidden --no-ignore -i 'ed25519|createPublicKey|verifySignature|jwks|issuer.?registry|verifier.?registry' EXTENSIONS governance -g '*.py' -g '*.ts' -g '!**/node_modules/**' -g '!**/.venv/**' -g '!**/dist/**' -g '!**/build/**'
```

Result: exit code 1, no matching line. A second targeted query,
`rg -l --hidden --no-ignore -i 'verificationAuthorityHash|trustedRegistrySnapshotIdentity|sourceObservationLog|VERIFIED_BY_LIVE_REGISTRY_LOOKUP'`
over `docs governance EXTENSIONS ECOSYSTEM`, returned only G1 T2B/T2C
audit/review documents (nine document paths, all under `docs/audits/` and
`docs/reviews/`), none under `governance/compat/` or the searched source
subtrees beneath `EXTENSIONS`. A third targeted query over `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
and `docs/reference/CVF_MODULE_INVENTORY.md` for
`key.?registry|public.?key|PKI|signing.?key|key.?custody|issuer` returned no
matches in either governed architectural surface. A fourth targeted query
over `docs/reference` and `governance` for
`key.?governance.?authority|decision.?owner.?registry|observation.?log|issuer.?authority`
returned three files, of which one
(`docs/reference/CVF_ENTERPRISE_EVIDENCE_PACK.md`) names a checker,
`governance/compat/check_cross_family_approval_artifact_external_revocation_issuer_authority.py`,
inspected in full below as a fourth candidate.

Exclusions and unread regions: `node_modules`, `.venv`, `dist`, `build` were
excluded from the source-code query by design. This is a bounded, focused
search over the four named roots and named reference surfaces; it is not a
complete-corpus inventory and does not certify that every file in the
repository was read. No external research, network lookup, or provider
memory was used as evidence; provider memory is `NOT_CVF_SOURCE`.

## Findings / Position

### Dependency 1: Verifier signing-key custody, rotation and public-key registry write authority

- Decision-maker: unresolved; T2C names "CVF key-governance authority" as a
  role label only, with no located source.
- Source-of-truth candidate: none found. The source-code query for
  `ed25519|createPublicKey|...` returned exit 1 (no match) across
  `EXTENSIONS` and `governance`.
- Write authority: unresolved; no registry schema, no write-path code, no
  key-lifecycle implementation exists in current source.
- Verifier/consumer: none; T2C's own `SignatureValidityCheck` pseudocode is
  hypothetical and unwired to any concrete registry.
- Update and revocation/correction route: none exists; T2C specifies
  `revokedAt`/`expiresAt` fields in a proposed schema only.
- Durable evidence: none; no committed registry file, database schema, or
  configuration surface was found.
- Failure behavior: undefined in practice; T2C's own spec is fail-closed by
  design but has no implementation to fail closed within.
- Remaining operator choice: the operator must either name an existing
  out-of-repository key-management system as source-of-truth (not
  discoverable by this repository-scoped search) or authorize creation of a
  new CVF-governed registry and assign its accountable owner.

Disposition: `BLOCKED_SOURCE_NOT_FOUND`.

### Dependency 2: Independently trusted `verificationAuthorityHash` specification and decision-owner binding

- Decision-maker: unresolved; T2C requires the hash to come from
  "decision-owner trusted context," but no such context object or file is
  bound anywhere in current source.
- Source-of-truth candidate: none found by the second targeted query;
  `verificationAuthorityHash` appears only inside the T2B/T2C design and
  review documents themselves, never in `governance/compat/*.py` or
  searched TypeScript source files beneath `EXTENSIONS`.
- Write authority: unresolved.
- Verifier/consumer: T2C's `LookupProvenanceCheck` pseudocode reads
  `expectedAuthorityHash` as a caller-supplied parameter; no caller
  implementation exists to supply it.
- Update and revocation/correction route: none exists.
- Durable evidence: none; the only committed hash values found are the two
  test-fixture vectors in the T2C design document itself, which the design
  document explicitly labels non-operational.
- Failure behavior: undefined in practice.
- Remaining operator choice: the operator must identify or create the
  authoritative specification document/process whose hash this field would
  bind to, and name its accountable owner and update procedure.

Disposition: `BLOCKED_SOURCE_NOT_FOUND`.

### Dependency 3: Source-owned registry snapshot identity and observation log

- Decision-maker: unresolved; T2C labels this "source-owned authority
  (decision owner)" without naming a concrete source.
- Source-of-truth candidate: none found. `trustedRegistrySnapshotIdentity`
  and `sourceObservationLog` (and its exact-cased variant used in T2C
  pseudocode) appear only within the T2B/T2C design/review corpus.
- Write authority: unresolved; T2C's `sourceObservationLog.lookup(...)` and
  `.countObservationsFor(...)` are pseudocode method calls on an object with
  no concrete implementation.
- Verifier/consumer: none in current source; the calling contract exists
  only as specification.
- Update and revocation/correction route: none exists.
- Durable evidence: none; no observation-log file, table, or append-only
  store was found in `docs`, `governance`, `EXTENSIONS`, or `ECOSYSTEM`.
- Failure behavior: undefined in practice.
- Remaining operator choice: the operator must authorize and name an
  accountable owner for a real, source-owned observation-logging mechanism,
  separate from the key-custody owner in Dependency 1 if the operator
  intends different accountable parties.

Disposition: `BLOCKED_SOURCE_NOT_FOUND`.

### Dependency 4: Issuer registry content and lookup semantics

- Decision-maker: unresolved; T2C labels this "Issuer/authority decision
  owner" without naming a concrete source.
- Source-of-truth candidate: none found by the primary source-code query.
  A fourth candidate was independently tested:
  `governance/compat/check_cross_family_approval_artifact_external_revocation_issuer_authority.py`
  (found via the `issuer.?authority` reference-surface query). Full-file
  inspection shows this checker compares two fixed literal strings
  (`self-governed-revocation-authority`/`unbound` and
  `verified-self-issued-only`/`unbound`) extracted from a release-approval
  packet's own prose fields against a posture policy computed from the same
  packet's `packet type`/`decision` fields. It has no key material, no
  public-key or issuer registry, no external lookup call, and no
  source-owned observation log; its "issuer authority" wording is a
  same-token collision on the word "issuer," not a G1 issuer-registry
  mechanism. It governs release-approval-packet self-consistency, not
  identity/issuer confirmation for candidate admission.
- Write authority: unresolved for an actual issuer registry.
- Verifier/consumer: T2C's `LookupProvenanceCheck` calls
  `sourceRegistry.lookup(issuerIdentity, issuerAttestedHash,
  snapshot_content)` as pseudocode; no concrete registry or lookup function
  exists.
- Update and revocation/correction route: none exists.
- Durable evidence: none.
- Failure behavior: undefined in practice.
- Remaining operator choice: the operator must identify or create a real
  issuer registry with defined lookup semantics and name its accountable
  owner, distinct from Dependencies 1-3 if the operator intends separate
  accountable parties.

Disposition: `BLOCKED_SOURCE_NOT_FOUND`.

## Rejected-Adjacent Candidates

| Candidate | Exact path/section | Role mismatch | Why it cannot satisfy the G1 requirement |
|---|---|---|---|
| Web service-token HMAC | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`, `computeServiceRequestSignature` (line 27) and `verifyServiceTokenRequest` (line 88) | symmetric shared-secret authentication vs. asymmetric verifier-key registry | Uses a single `configuredToken` with HMAC-SHA256 (`createHmac('sha256', token)`), not Ed25519 public/private key pairs; there is no public-key registry, no per-key lifecycle (`issuedAt`/`expiresAt`/`revokedAt`/`status`), and no issuer lookup. It authenticates a caller holding a shared token, not a verifier's independent registry observation. Satisfies none of the four dependencies. |
| Agent identity credential store | `EXTENSIONS/CVF_ECO_v2.3_AGENT_IDENTITY/src/identity.manager.ts`, `IdentityManager.verify` (line 27) | agent-credential association vs. verifier signature + independent registry lookup | `verify()` checks an `AgentRegistry` entry and a `CredentialStore`-issued token value for equality and ownership; it has no cryptographic signature verification, no Ed25519 keys, and no separately observed source registry distinct from the credential issuer itself. It answers "is this agent's credential valid," not "did an independent source observe this issuer identity." Satisfies none of the four dependencies. |
| Cross-family approval-artifact external revocation issuer authority checker | `governance/compat/check_cross_family_approval_artifact_external_revocation_issuer_authority.py`, `_build_expectations` (line 38), `build_report` (line 78) | packet-prose literal-consistency check vs. genuine issuer registry and lookup | Compares a release-approval packet's self-declared `transition-approval-artifact-external-revocation-issuer-authority` string field against one of two fixed literals (`self-governed-revocation-authority` or `unbound`) chosen by the packet's own `packet type`/`decision` text. No key, no registry content, no lookup against an external or independently observed source; a packet author sets its own compared value. Satisfies none of the four dependencies. |
| T2B/T2C design and review documents themselves | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`, `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | hypothetical specification vs. operational owner | These documents define the pseudocode contract the four dependencies must satisfy; they are the requirement, not a satisfying implementation or owner. T2C's own Claim Boundary and Owner Ledger explicitly disclaim any existing owner. |

## Owner-Option Matrix

| Dependency | Existing owner found | Proposed owner option (operator decision required) | Disposition |
|---|---|---|---|
| (1) Verifier key custody, rotation, public-key registry write authority | none | A new CVF-governed `VerifierPublicKeyRegistry` module, with an accountable key-governance role the operator names explicitly; separable from Dependency 3's observation-log owner if the operator wants different accountable parties | `BLOCKED_SOURCE_NOT_FOUND`; any named module is `PROPOSED_OPERATOR_DECISION`, never `VERIFIED_EXISTING_OWNER` |
| (2) Independently trusted `verificationAuthorityHash` specification/decision-owner binding | none | A named, versioned authority-specification document under Local/operator control, hashed at each decision round, with the decision owner as its accountable party | `BLOCKED_SOURCE_NOT_FOUND`; any named document is `PROPOSED_OPERATOR_DECISION` |
| (3) Registry snapshot identity and source-owned observation log | none | A new append-only observation-log module, accountable to a source-owned role the operator names explicitly; may or may not share an owner with Dependency 1, operator's choice | `BLOCKED_SOURCE_NOT_FOUND`; any named module is `PROPOSED_OPERATOR_DECISION` |
| (4) Issuer registry content and lookup semantics | none (nearest adjacent candidate rejected above) | A new issuer registry with defined lookup semantics, accountable to an issuer/authority decision owner the operator names explicitly | `BLOCKED_SOURCE_NOT_FOUND`; any named module is `PROPOSED_OPERATOR_DECISION` |

No row in this matrix is `VERIFIED_EXISTING_OWNER`. No source path, field
name, test key, or passing signature found during this search is owner
evidence by itself, per the work order's explicit instruction. A source not
found in this bounded search is not proof of global nonexistence outside
this repository.

## Risk / Corrective Action

**Primary risk:** treating any of the rejected-adjacent candidates, or a
future proposed-owner document, as sufficient operational authority without
an independent source-verification step and explicit operator assignment.
The HMAC and credential-association mechanisms above use fundamentally
different trust models (shared secret; credential-store lookup) and cannot
be reinterpreted as satisfying an Ed25519 public-key registry, an
independently trusted authority-hash specification, a source-owned
observation log, or a genuine issuer lookup, no matter how their code is
wrapped.

**Corrective action:** before any implementation, the operator must
separately authorize and name an accountable owner for each of the four
dependencies (or explicitly accept a smaller number of owners covering
multiple dependencies, if intended). Each such assignment requires its own
governed packet and Local review; this document does not perform that
assignment and does not itself become authority evidence for a future
packet beyond recording what was and was not found.

## Claim Boundary

This is a documentation-only, bounded source-search analysis. It does not
appoint a key custodian, register a public key, create an issuer registry,
perform a lookup, or make any candidate admission operational. No row in the
Owner-Option Matrix is `VERIFIED_EXISTING_OWNER`. All four dependencies
remain `BLOCKED_SOURCE_NOT_FOUND` for an existing owner; any named option is
`PROPOSED_OPERATOR_DECISION` only, pending a separate, explicitly authorized
operator/Local decision.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private, held source-owner analysis packet.
