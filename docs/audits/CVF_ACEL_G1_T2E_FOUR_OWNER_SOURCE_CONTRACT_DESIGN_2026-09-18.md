# CVF ACEL G1 T2E Four-Owner Source Contract Design

Memory class: governed-worker-audit

docType: audit

Status: PROPOSED_CONTRACT_DESIGN_ONLY

Date: 2026-09-18

dispatchBaseHead: `af36ed6e04563806c1056ae9f8e298dd3e3096a4`

## Purpose

Design four separately accountable source-owner contracts for the four
operational dependencies T2D found `BLOCKED_SOURCE_NOT_FOUND`
(`docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md`, Owner-Option
Matrix), per the operator-approved four-responsibility model
(`docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_RESPONSIBILITY_LOCAL_DECISION_2026-09-18.md`,
Decision / Disposition). This document proposes role contracts and the
evidence Local would need before treating any named party as verified. It
does not appoint an accountable party, create a key, implement a registry or
observation log, perform a live lookup, or admit any candidate. All four
contracts remain `PROPOSED_OPERATOR_DECISION` and every operational claim
remains `BLOCKED_SOURCE_NOT_FOUND` / `UNVERIFIED`.

## Target Under Review

The four T2D dependencies, now split into four distinct proposed contracts
per the work order's Contract Design Requirements:

1. `VerifierKeyAndRegistryControlOwner` - key custody, generation/import
   ceremony boundaries, rotation, revocation, public-key registry writes.
2. `VerificationAuthoritySpecificationOwner` - versioned authority policy,
   decision approval, canonical bytes/hash production,
   `verificationAuthorityHash` consumer binding.
3. `RegistryObservationOwner` - registry snapshot identity, acquisition time,
   source provenance, append-only observation records, correction chaining,
   rollback resistance.
4. `IssuerRegistryAuthorityOwner` - issuer content, lookup semantics,
   freshness/status responses, correction/revocation, genuine authority
   provenance.

## Scope / Methodology

Documentation-only design task. Per the work order's Negative Search And
Collision Discipline, T2D's bounded source search
(`docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md`, Scope /
Methodology and Owner-Option Matrix) is reused as accepted evidence and not
re-executed; no new broad discovery scan was run. One targeted collision
query was executed before authoring, exactly as specified in the work order
and the GC-018 baseline:

```
rg -n --hidden --no-ignore -i 'ACEL-G1-T2E|VerifierKeyAndRegistryControlOwner|VerificationAuthoritySpecificationOwner|RegistryObservationOwner|IssuerRegistryAuthorityOwner|PROPOSED_OPERATOR_DECISION|BLOCKED_SOURCE_NOT_FOUND|UNVERIFIED' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'
```

Result: the four proposed role-name tokens and `ACEL-G1-T2E` matched only
inside this tranche's own governing packet documents (the T2E work order,
GC-018 baseline, Local decision, and session continuity state that names the
dispatched batch ID), each already disclosed as a same-token collision in
those documents' own Negative Search sections. No occurrence appears in
`governance/compat/*.py` source, `EXTENSIONS` TypeScript source (outside
`node_modules` vendor files), or any other implementation surface. The
generic tokens `PROPOSED_OPERATOR_DECISION`, `BLOCKED_SOURCE_NOT_FOUND`, and
`UNVERIFIED` matched broadly across unrelated governed documents and JSON
state entries, as expected for status/disposition vocabulary used
repository-wide; none of those occurrences is owner or implementation
evidence for this tranche's four contracts, consistent with the work order's
own disclosed collision list for these exact tokens.

Search roots: `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION`,
restricted to `*.md`, `*.json`, `*.py`, `*.ts`. Exclusions: `node_modules`,
`.venv`, `dist`, `build` are not separately excluded in this single targeted
query (unlike T2D's broader source-code query), but the only matches inside
`EXTENSIONS` are vendored `typescript.d.ts` declaration files unrelated to any
of the four proposed roles; no project-authored TypeScript or Python source
matched. This is a bounded, targeted collision check reusing T2D's accepted
search, not a new complete-corpus inventory; it does not certify that every
repository file was read. No external research, network lookup, or provider
memory was used; provider memory is `NOT_CVF_SOURCE`.

## Findings / Position

### Contract 1: `VerifierKeyAndRegistryControlOwner`

- Accountable responsibility: custody of the verifier's Ed25519 (or
  equivalent) private key material; execution and durable logging of
  generation/import, rotation, and revocation ceremonies; sole write
  authority over the public-key registry's key-lifecycle fields
  (`issuedAt`/`expiresAt`/`revokedAt`/`status`).
- Prohibited dual roles: this owner must not also be the
  `RegistryObservationOwner` for the same registry it writes to (a writer
  attesting its own observation is self-approval); may be the same party as
  `VerificationAuthoritySpecificationOwner` only if the operator explicitly
  accepts and records that combination, because both influence what a
  verifier ultimately trusts.
- Source-of-truth form: a durable, versioned public-key registry artifact
  (file, table, or equivalent CVF-governed store) recording one row per key
  with full lifecycle fields; not yet created (`BLOCKED_SOURCE_NOT_FOUND` per
  T2D Dependency 1).
- Decision maker: the named accountable key-governance role; operator-
  appointed, not self-declared.
- Write authority: this owner exclusively; no other role may mutate registry
  key rows.
- Read/verifier consumers: any G1 verifier performing `SignatureValidityCheck`
  (T2C pseudocode); consumers may read but never write.
- Version/identity scheme: each key row keyed by a stable key identifier
  distinct from the key bytes themselves, with an explicit lifecycle state
  machine (`ACTIVE` -> `ROTATING` -> `REVOKED`/`EXPIRED`); no such scheme
  currently exists in source.
- Lifecycle transitions: generation/import -> active -> rotation or
  revocation -> terminal; every transition durably logged with actor and
  timestamp.
- Durable evidence: a signed or append-only log entry per transition; none
  found in current source.
- Correction, rotation, or revocation route: only this owner may initiate;
  route must itself be logged and auditable; not yet specified as an
  implementation.
- Required admission evidence before Local treats a named party as verified:
  (a) an exact governed source path implementing the registry, (b) a named
  accountable role bound to write access on that path, (c) at least one
  consumer reading from it, (d) a durable lifecycle-transition log,
  (e) independent Local verification that (a)-(d) exist and match this
  contract.
- Fail-closed behavior: absent or unreachable registry state must cause the
  verifier to reject, never default-trust; not yet implemented.
- Operator inputs still required: name the accountable party; authorize
  registry creation; decide whether to combine with Contract 2.
- Exact claims still blocked: `BLOCKED_SOURCE_NOT_FOUND` for an existing
  registry or custodian; `UNVERIFIED` for candidate admission.

### Contract 2: `VerificationAuthoritySpecificationOwner`

- Accountable responsibility: authoring, publishing and version-controlling
  the authority specification whose canonical bytes produce
  `verificationAuthorityHash`; proposing each new specification version; and
  binding the independently approved hash to verifier-side consumer code. The
  specification author cannot activate its own version by self-approval.
- Prohibited dual roles: must not be the same party as
  `IssuerRegistryAuthorityOwner`, because an issuer authoring its own
  authority specification and then attesting to it is a circular-authority
  pattern (see Cross-Contract Separation Matrix, Case 2). This combination is
  rejected by this design rather than made available through operator waiver.
  Contract 2 may combine with Contract 1 only with explicit operator sign-off
  and Local conflict-of-duty review (see Contract 1 and Case 10).
- Source-of-truth form: a named, versioned authority-specification document
  under Local/operator control, hashed at each decision round; T2D's second
  targeted query found `verificationAuthorityHash` only inside the T2B/T2C
  design corpus itself, never bound to a concrete specification document
  (`BLOCKED_SOURCE_NOT_FOUND`).
- Decision maker: the operator remains activation decision owner until a
  distinguishable approval authority is explicitly appointed. The named
  specification-owner role may propose and publish canonical bytes but cannot
  approve its own version as trusted authority.
- Write authority: this owner exclusively controls new specification
  versions and their canonical byte representation.
- Read/verifier consumers: T2C's `LookupProvenanceCheck` pseudocode, which
  currently reads `expectedAuthorityHash` as an unimplemented caller-supplied
  parameter.
- Version/identity scheme: monotonic version identifier plus the hash of the
  canonical bytes for that version; no scheme exists yet.
- Lifecycle transitions: draft -> approved -> active -> superseded; each
  transition requires an independent decision-owner approval record, not a
  self-approval by the document's author alone.
- Durable evidence: the approval record and the canonical-bytes hash for
  every version; the only committed hash values found by T2D were two
  non-operational test fixtures in the T2C design document.
- Correction, rotation, or revocation route: a new approved version
  supersedes the prior one; no silent in-place edit of an active
  specification's canonical bytes.
- Required admission evidence: (a) an exact governed specification document
  path, (b) a recorded independent approval distinct from the document's own
  authorship, (c) at least one verifier consumer binding to the resulting
  hash, (d) Local verification that (a)-(c) exist and match.
- Fail-closed behavior: an unbound or unapproved hash must cause verifier
  rejection, not silent trust of the caller-supplied value.
- Operator inputs still required: name the accountable party; name or create
  the specification document; decide whether to combine with Contract 1.
- Exact claims still blocked: `BLOCKED_SOURCE_NOT_FOUND` for an existing
  specification/decision-owner binding; `UNVERIFIED` for candidate admission.

### Contract 3: `RegistryObservationOwner`

- Accountable responsibility: recording, for the key registry and/or issuer
  registry, an independent snapshot identity, acquisition time, and source
  provenance each time the registry is observed; maintaining an append-only
  observation log with correction chaining rather than in-place edits.
- Prohibited dual roles: must not be the same party as the writer of any
  registry it observes: `VerifierKeyAndRegistryControlOwner` for the key
  registry or `IssuerRegistryAuthorityOwner` for the issuer registry. A
  registry writer cannot independently attest to its own writes (Cross-
  Contract Separation Matrix, Case 1). One independent observation owner may
  span both registries only if it remains distinct from both registry writers
  and the operator records that scope explicitly.
- Source-of-truth form: an append-only observation-log store distinct from
  the registries it observes; T2D found no such store, table, or file
  anywhere in `docs`, `governance`, `EXTENSIONS`, or `ECOSYSTEM`
  (`BLOCKED_SOURCE_NOT_FOUND`).
- Decision maker: the named accountable observation role; does not decide
  registry content, only records what it independently observed.
- Write authority: append-only; this owner may append new observation
  records but must never mutate or delete a prior record. Correction is a new
  append-only entry that supersedes, not an in-place rewrite.
- Read/verifier consumers: T2C's `sourceObservationLog.lookup(...)` and
  `.countObservationsFor(...)` pseudocode calls, currently unimplemented.
- Version/identity scheme: each observation record keyed by
  (registry snapshot identity, acquisition timestamp, observer identity);
  rollback resistance requires the log itself to be tamper-evident (e.g.
  hash-chained), not yet specified as an implementation.
- Lifecycle transitions: observation recorded -> optionally superseded by a
  later correction entry; no deletion transition exists.
- Durable evidence: the append-only log itself; none found in current
  source.
- Correction, rotation, or revocation route: a new dated correction entry
  referencing the entry it supersedes; the original entry remains readable
  for audit.
- Required admission evidence: (a) an exact governed append-only store path,
  (b) proof the store is independent of the registry-writer role for the same
  registry, (c) at least one verifier consumer reading from it, (d) evidence
  of tamper-evidence or rollback resistance, (e) Local verification that
  (a)-(d) exist and match.
- Fail-closed behavior: a missing or stale observation record must cause
  verifier rejection, not an assumption of freshness.
- Operator inputs still required: name the accountable party; authorize the
  append-only store's creation; decide whether one observation role spans
  both registries or two separate roles are used.
- Exact claims still blocked: `BLOCKED_SOURCE_NOT_FOUND` for an existing
  snapshot identity/observation log; `UNVERIFIED` for candidate admission.

### Contract 4: `IssuerRegistryAuthorityOwner`

- Accountable responsibility: maintaining genuine issuer registry content;
  defining and operating lookup semantics; producing freshness/status
  responses; handling correction and revocation of issuer entries with
  provable, non-self-asserted authority.
- Prohibited dual roles: must not be the same party as
  `VerificationAuthoritySpecificationOwner` (Contract 2's Case 2 above) or the
  `RegistryObservationOwner` observing this issuer registry (Case 1). It must
  not verify its own issuer assertions as if they were an independent lookup
  result (issuer self-verification is rejected in Case 5).
- Source-of-truth form: a real issuer registry with defined lookup semantics
  distinct from the release-approval-packet posture checker T2D tested and
  rejected
  (`governance/compat/check_cross_family_approval_artifact_external_revocation_issuer_authority.py`,
  which compares two fixed literal strings from a packet's own prose and has
  no key material, registry content, or external lookup call). T2D found no
  qualifying source (`BLOCKED_SOURCE_NOT_FOUND`).
- Decision maker: the named accountable issuer/authority role.
- Write authority: this owner exclusively controls issuer registry entries
  and their status.
- Read/verifier consumers: T2C's `LookupProvenanceCheck` pseudocode call
  `sourceRegistry.lookup(issuerIdentity, issuerAttestedHash,
  snapshot_content)`, currently unimplemented.
- Version/identity scheme: issuer identity plus a monotonic status/version
  per entry (`ACTIVE`/`REVOKED`/`SUPERSEDED`); no scheme exists yet.
- Lifecycle transitions: registered -> active -> corrected or revoked;
  correction/revocation must be independently evidenced, not a bare status
  flip by the issuer itself.
- Durable evidence: a lookup-response log or equivalent durable record of
  what was returned and when; none found in current source.
- Correction, rotation, or revocation route: this owner initiates; the route
  itself must be logged and must not be satisfiable by the issuer's own
  unverified assertion alone.
- Required admission evidence: (a) an exact governed registry/lookup
  implementation path distinct from the rejected posture checker, (b) a named
  accountable role with write access, (c) at least one verifier consumer
  performing a real lookup call, (d) evidence that correction/revocation
  requires more than the issuer's own assertion, (e) Local verification that
  (a)-(d) exist and match.
- Fail-closed behavior: an unreachable or ambiguous lookup result must cause
  verifier rejection, not a default-active assumption.
- Operator inputs still required: name the accountable party; authorize
  issuer registry creation; and appoint or scope a distinct observation owner.
- Exact claims still blocked: `BLOCKED_SOURCE_NOT_FOUND` for an existing
  issuer registry/lookup owner; `UNVERIFIED` for candidate admission.

## Cross-Contract Separation Matrix

| Case | Pattern | Contracts involved | Disposition |
|---|---|---|---|
| 1 | Same party writes a registry and also independently observes/attests to that registry | 1 + 3 for the key registry; 4 + 3 for the issuer registry | `CIRCULAR_AUTHORITY_REJECTED`: a writer cannot be its own independent observer for the same registry |
| 2 | Same party authors the authority specification and also acts as issuer authority attesting to it | 2 + 4 | `CIRCULAR_AUTHORITY_REJECTED`: the specification owner and the issuer attesting to authority derived from that specification must be independent parties |
| 3 | Same-party observation and mutation of the same evidence store | 3 self-combination | `CIRCULAR_AUTHORITY_REJECTED`: the observation log's append-only writer must not be the same party who can mutate the registry it observes without a separate, distinguishable role boundary |
| 4 | Verification authority hash computed from bytes the same party both authors and independently re-hashes as "proof" | 2 self-combination | `CIRCULAR_AUTHORITY_REJECTED`: a specification owner cannot certify its own hash as independently trusted evidence; approval must come from a distinguishable decision-owner step |
| 5 | Issuer's own unverified assertion treated as a genuine lookup result | 4 self-combination | `CIRCULAR_AUTHORITY_REJECTED`: an issuer cannot satisfy its own correction/revocation evidence requirement by simply asserting a new status |
| 6 | Stale evidence presented as current | any contract | Fail-closed: consumer must reject on staleness, not assume freshness; no contract may define an emergency path that treats stale evidence as valid |
| 7 | Evidence source unavailable at verification time | any contract | Fail-closed: unavailability is a rejection condition, not a pass-through; no contract may silently admit a candidate when its source cannot be reached |
| 8 | Conflicting versions of the same evidence (e.g. two specification versions both claim `active`) | 2, 3, 4 | Fail-closed: verifier must reject on an unresolved version conflict; resolution requires a Local-reviewed correction entry, not automatic latest-wins trust |
| 9 | Emergency override bypassing normal admission evidence | any contract | `NO_EMERGENCY_PATH`: this design defines no emergency override; any future emergency route must itself be a separately governed, Local-reviewed packet and must never silently admit a candidate |
| 10 | Contracts 1 and 2 combined under operator's explicit decision | 1 + 2 | `PERMITTED_WITH_EXPLICIT_OPERATOR_ACCEPTANCE`: the only combination this design does not default-reject, because key custody and specification authorship do not create the same self-attestation loop as Cases 1-2 and 4-5; still requires a recorded operator decision and Local conflict-of-duty review before use |

No case above authorizes an actual admission; every disposition here governs
future evidence requirements, not present operational trust.

## Admission Evidence Ledger (Consolidated)

| Contract | Existing owner | Proposed owner option | Admission evidence still required | Disposition |
|---|---|---|---|---|
| `VerifierKeyAndRegistryControlOwner` | none | operator-named key-governance role over a new CVF-governed public-key registry | governed registry path; named write-authority role; at least one verifier consumer; durable lifecycle log; Local verification | `BLOCKED_SOURCE_NOT_FOUND`; any named party is `PROPOSED_OPERATOR_DECISION` |
| `VerificationAuthoritySpecificationOwner` | none | operator-named specification-owner role over a versioned authority document | governed specification path; independent approval record; consumer hash binding; Local verification | `BLOCKED_SOURCE_NOT_FOUND`; any named party is `PROPOSED_OPERATOR_DECISION` |
| `RegistryObservationOwner` | none | operator-named observation role over a new append-only observation-log store | governed append-only store path; independence proof from the registry writer; consumer read; tamper-evidence; Local verification | `BLOCKED_SOURCE_NOT_FOUND`; any named party is `PROPOSED_OPERATOR_DECISION` |
| `IssuerRegistryAuthorityOwner` | none (nearest adjacent candidate rejected in T2D) | operator-named issuer-authority role over a new issuer registry with real lookup semantics | governed registry/lookup path distinct from the rejected posture checker; named write-authority role; consumer lookup call; independent correction/revocation evidence; Local verification | `BLOCKED_SOURCE_NOT_FOUND`; any named party is `PROPOSED_OPERATOR_DECISION` |

No row is `VERIFIED_EXISTING_OWNER`. Candidate admission remains `UNVERIFIED`
for all four contracts.

## Risk / Corrective Action

**Primary risk:** treating this contract design, or any future document
naming a proposed party, as sufficient operational authority without an
independent source-verification step, an explicit operator appointment, and
Local's confirmation that the required admission evidence in the ledger above
actually exists. A second risk specific to this tranche is silently combining
two of the four responsibilities (for example, folding registry observation
into the same party who writes the registry) without the explicit operator
acceptance and Local conflict-of-duty review this design requires.

**Corrective action:** any future implementation or appointment packet must
cite this document's per-contract admission-evidence list, must not mark a
contract `VERIFIED_EXISTING_OWNER` until Local independently confirms every
listed evidence item, and must not combine roles outside Case 10 of the
Cross-Contract Separation Matrix without a separate, explicit operator
decision and Local conflict-of-duty analysis. This document does not perform
any appointment and does not itself become authority evidence for a future
packet beyond recording the proposed contract shapes and their evidence
requirements.

## Claim Boundary

This is a documentation-only, bounded contract-design proposal. It does not
appoint a key custodian, register a public key, create an issuer registry,
implement an observation log, perform a lookup, or make any candidate
admission operational. No contract in the Admission Evidence Ledger is
`VERIFIED_EXISTING_OWNER`. All four contracts remain `PROPOSED_OPERATOR_DECISION`
pending a separate, explicitly authorized operator/Local decision naming an
actual accountable party and independently verifying the required evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private, held four-owner source-contract design packet.
