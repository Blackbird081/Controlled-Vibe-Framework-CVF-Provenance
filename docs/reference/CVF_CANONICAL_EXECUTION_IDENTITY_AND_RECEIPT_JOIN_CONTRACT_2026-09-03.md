# CVF Canonical Execution Identity And Receipt Join Contract

Memory class: FULL_RECORD

docType: reference

Status: CLOSED_PASS_BOUNDED

Batch ID: CSCC-R1-T1

Date: 2026-09-03

executionBaseHead: `a232e2e7a`

## Purpose

Freeze exactly one canonical execution identity field name and its
source, cardinality, validation, propagation path, optional-transition-window
behavior, and terminal-path behavior across the four current evidence owners
named by CSCC-R1-T0A: `GatewayReceipt`, `MaterialContextManifest`,
`Sot3ActivationEvidenceRecord`, and Web's `GovernanceEvidenceReceipt`. This
document names a join field and a hash/reference join mechanism only; it does
not add the field to any of the four schemas' actual TypeScript source.

## Scope / Applies To

Applies to a planned additive field on
`EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` (`GatewayReceipt`),
`EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts`
(`MaterialContextManifest`),
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts`
(`Sot3ActivationEvidenceRecord`), and the `GovernanceEvidenceReceipt` type
consumed by
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`.
Does not apply to and does not modify any of those four files, any test file,
or any package export. Does not authorize provider/live proof or T2
implementation.

## Current Runtime Freshness Verification

Exact search results re-run at `executionBaseHead` `a232e2e7a`:

1. `envelopeId|WebGovernanceEnvelope|GovernanceEvidenceReceipt` over
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` (files-with-matches mode)
   returns 53 files, including `web-governance-envelope.ts` (the owner),
   `route.ts`, `web-governance-envelope.test.ts`, and 50 other consumers.
   Direct read of `web-governance-envelope.ts` confirms `envelopeId` is
   declared on `WebGovernanceEnvelope` (line 26), generated exactly once per
   request in `buildGovernanceEnvelope` (line 85-103) as
   `` `env-${ts.toString(36)}-${rand}` `` (line 89), and copied verbatim onto
   `GovernanceEvidenceReceipt.envelopeId` inside `buildEvidenceReceipt`
   (line 263). This matches T0A's seam-1 finding unchanged.
2. `Sot3ActivationEvidenceRecord|requestId` over
   `sot3-activation-evidence-store.ts` (content mode) returns matches at
   lines 52-366; `Sot3ActivationEvidenceRecord` (line 52) currently declares
   `requestId: string` (line 54) as one of exactly thirteen fields enforced
   by an exact-keys schema check (`recordSchemaIssue`, lines 170-234,
   `hasExactKeys` against the literal thirteen-field list at lines 173-176).
   No `canonicalExecutionId` or equivalent field exists on this record today.
   `route-knowledge-context.ts` was named in the work order's search target
   but does not currently exist at that exact path under
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`; T0A's
   assessment cites it as the caller of `resolveKnowledgeContext` where
   SOT3's `requestId` is minted (T0A Seam 1 row, Required Decision Question
   1). This is a citation-path note, not a source contradiction: the
   `requestId` field and its exact-keys schema on `Sot3ActivationEvidenceRecord`
   itself were directly verified in `sot3-activation-evidence-store.ts`.
3. `CanonicalExecutionPort|canonicalExecutionId|beforeProviderInvoke` across
   `EXTENSIONS` (excluding `node_modules`) returns zero files, matching the
   paired port contract's freshness verification. No competing symbol or
   already-claimed field name exists.

No newly existing competing symbol and no changed field shape were found. The
`Sot3ActivationEvidenceRecord` exact-keys schema check is a fresh finding this
document accounts for directly in the Optional Transition Window section
below (an additive field there must extend the exact-keys list, not merely be
"optional" in the TypeScript sense).

## Selected Canonical Identity Field

**Canonical field name: `canonicalExecutionId`.**

This exact spelling is the only canonical identity field name used anywhere
in this document and in the paired
`docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md`
(`CanonicalExecutionPortRequest.canonicalExecutionId`,
`CanonicalExecutionAttemptBoundaryInput.canonicalExecutionId`,
`CanonicalExecutionPortResult.canonicalExecutionId`). Both documents agree on
this spelling byte-for-byte; see the Cross-Document Agreement Check section.

| Property | Value |
| --- | --- |
| Source | `WebGovernanceEnvelope.envelopeId` (`web-governance-envelope.ts` line 26, generated at line 89 inside `buildGovernanceEnvelope`, called once from `route.ts` line 140 per T0A's verified citation). `canonicalExecutionId` is not a new identity generator; it is the name under which `envelopeId`'s value is carried once it leaves the Web-internal envelope and crosses into Gateway/SOT3/receipt-join territory. |
| Cardinality | Exactly one `canonicalExecutionId` value per governed request, generated exactly once (T0A seam 1, matching the existing exactly-once `envelopeId` generation). A retry that starts a fresh port execution (per the paired port contract's Retry row) reuses the same `canonicalExecutionId` as the original request; only the port-internal `attemptIndex` is fresh per retry, never the identity. |
| Validation | A non-empty string matching the existing `envelopeId` format `env-<timestamp-base36>-<random>` (`web-governance-envelope.ts` line 89) when originated at the Web envelope. A consumer that receives `canonicalExecutionId` as an input parameter (Gateway, SOT3) must treat it as an opaque non-empty string and must not re-derive, reformat, or re-validate its internal shape; only the originating Web envelope owns the format. |
| Propagation path | `WebGovernanceEnvelope.envelopeId` is the single origin and fans out without regeneration: (a) Web passes it as `canonicalExecutionId` into the pre-provider SOT3 knowledge-context lane, which records `Sot3ActivationEvidenceRecord.canonicalExecutionId` alongside the retained `requestId`; (b) Web then places the same value on `CanonicalExecutionPortRequest`, whose concrete adapter maps it 1:1 to both `GatewayExecuteRequest.traceId` and the additive optional `GatewayExecuteRequest.canonicalExecutionId` carrier; the bridge uses that explicit carrier for `CanonicalExecutionAttemptBoundaryInput`, `GatewayReceipt.canonicalExecutionId`, and `MaterialContextManifest.canonicalExecutionId`; and (c) Web sets `GovernanceEvidenceReceipt.canonicalExecutionId` equal to the same receipt's existing `envelopeId`. SOT3 precedes the port in the canonical Web chain; neither the port nor Gateway creates SOT3 evidence. |

## Four-Owner Propagation And Additive-Field Matrix

The four evidence owners below receive the identity through an explicit
internal carrier: T2 adds `canonicalExecutionId?: string` to
`GatewayExecuteRequest`. `CanonicalExecutionAdapter` sets it equal to the
port request identity as well as mapping that value to the existing required
`traceId`. The bridge propagates the optional carrier and never infers it from
legacy `traceId` alone.

| Owner | Current identity field(s) | Additive field | Cardinality after addition | Terminal-path behavior |
| --- | --- | --- | --- | --- |
| `GatewayReceipt` (`gateway-receipt.ts`, interface at line 25) | `traceId: string` (required, line 27) | `canonicalExecutionId?: string` (new optional field) | One `canonicalExecutionId` per receipt when the underlying `GatewayExecuteRequest.canonicalExecutionId` carrier is present (port-composed calls); absent (`undefined`) for a legacy Gateway request that omits the carrier, even though that request still has a required `traceId`. | On every terminal receipt path inside `ProviderExecutionBridge.execute` (`buildStoppedResult`, `buildShieldedErrorResult`, `buildManifestFailureResult`, and both branches of the try/catch at lines 212-266), the field is populated whenever the originating request carried one, with no separate terminal-only code path; a pre-adapter stop's receipt carries the same `canonicalExecutionId` as an adapter-success receipt would, because the identity is set at request entry, not at outcome time. |
| `MaterialContextManifest` (`material-context-manifest.ts`, interface at line 64) | `traceId: string` (required, line 66) | `canonicalExecutionId?: string` (new optional field) | One `canonicalExecutionId` per manifest when the explicit Gateway request carrier is present; absent otherwise. Legacy `traceId` alone is never treated as proof of canonical composition. | `buildMaterialContextManifest` (line 264) and its digest computation (`digestOf`, `unsignedManifest`) must include `canonicalExecutionId` in the same canonicalization path as every other manifest field so `manifestDigest` and `validateMaterialContextManifest`'s rebuild-and-compare check (line 312-331) stay authoritative over the new field once T2 implements it; this document does not change the digest algorithm itself, only names the field it must eventually cover. |
| `Sot3ActivationEvidenceRecord` (`sot3-activation-evidence-store.ts`, interface at line 52) | `requestId: string` (required, line 54) | `canonicalExecutionId?: string` (new optional field) | One `canonicalExecutionId` per record, present when the record's originating request flowed through the canonical port; `requestId` is retained unchanged and is not renamed, removed, or superseded (T0A seam 1 retirement/compatibility rule: SOT3 stops self-generating only once it accepts the canonical identity as an input, but its own field is retained for backward-compatible internal bookkeeping). | T2 must make `recordSchemaIssue` accept exactly either the existing thirteen-key v1 shape or that same shape plus `canonicalExecutionId`; when present, the new value must be a non-empty string. Existing thirteen-key records remain valid. `deriveSot3EvidenceRecordId` remains unchanged so adding the join field does not change an existing record's stable ID. `computeSot3EvidenceRecordIntegrityHash` already canonicalizes every field except `integrityHash`, so the new field is included automatically whenever present and remains absent from the preimage for legacy records. This exact dual-shape rule is the selected transition design, not a T2 choice. |
| `GovernanceEvidenceReceipt` (Web; type imported into `web-governance-envelope.ts` line 1 from `@/lib/ai`, built at `buildEvidenceReceipt` line 242) | `envelopeId: string` (line 263, copied from `input.envelope.envelopeId`) | `canonicalExecutionId?: string` (new optional field, set equal to `envelopeId`'s value at construction) | One `canonicalExecutionId` per receipt, always equal to the same receipt's `envelopeId` (they are the same underlying value under two field names during the transition window). `envelopeId` is retained unchanged; no existing consumer of `GovernanceEvidenceReceipt.envelopeId` is broken. | `buildEvidenceReceipt` (line 242-283) would set both `envelopeId` and `canonicalExecutionId` from the same `input.envelope.envelopeId` source value at construction time, on every branch (no separate terminal-only assignment), so a denial-path receipt and a success-path receipt both carry the identity identically. |

## Reference/Hash Join Mechanism

Every cross-schema join uses `canonicalExecutionId` as a plain string
equality join key, plus the existing per-schema content-integrity hash each
owner already computes for its own record:

- `GatewayReceipt` and `MaterialContextManifest` are joined to each other and
  to `GovernanceEvidenceReceipt` by exact `canonicalExecutionId` string
  equality. `MaterialContextManifest.manifestDigest` (already computed via
  SHA-256 over the manifest's own canonical form, `material-context-manifest.ts`
  line 181-187) remains the integrity anchor for manifest content; a reader
  that holds a `canonicalExecutionId` and a `manifestDigest` can verify it
  received the correct, unmodified manifest for that identity without needing
  any other schema's fields.
- `Sot3ActivationEvidenceRecord` is joined to the other three by exact
  `canonicalExecutionId` string equality (once added) or by its existing
  `requestId` during the transition window before the additive field is
  populated. `Sot3ActivationEvidenceRecord.integrityHash`
  (`computeSot3EvidenceRecordIntegrityHash`, lines 139-142) remains that
  record's own independent integrity anchor.
- `GovernanceEvidenceReceipt.receiptIntegrity` (built by
  `buildReceiptIntegrityAnchor` when `input.receiptIntegrity` is supplied,
  `web-governance-envelope.ts` line 278-280) remains the Web receipt's own
  integrity anchor.

No join ever recomputes, merges, or re-hashes another schema's content into
its own digest. Each owner keeps its own independent integrity hash over its
own fields; `canonicalExecutionId` is the only value copied across schema
boundaries, and it is a short opaque identifier, never a hash of another
schema's payload.

## Explicit Prohibition On Payload Copying

The join mechanism above never copies, embeds, or re-serializes any of the
following across a schema boundary: raw `prompt` or `systemPrompt` text,
provider request/response payload bodies, any credential value (raw API key,
`CredentialReference`, or `CredentialMetadata` beyond the already-shielded
`keyId`/`fingerprint` fields `GatewayReceipt` already carries), or any
`Sot3ActivationEvidenceRecord.traces[]` entry's `kernelDecision`,
`truthReceipt`, `truthReference`, or `flowPackage` detail. A reader that
wants SOT3 activation detail for a given `canonicalExecutionId` looks it up
in the SOT3 store by that identity; it does not find a duplicated copy
embedded inside `GatewayReceipt` or `GovernanceEvidenceReceipt`. This mirrors
the existing `sanitizeReceiptMetadata` redaction pattern already present in
`gateway-receipt.ts` (lines 116-128) and the existing credential-like-key
rejection already present in `material-context-manifest.ts`'s canonicalizer
(`isCredentialLikeKey`, lines 98-105); this document does not change either
mechanism, it only confirms the new field does not need to bypass them
because it never carries payload content.

## Optional Transition Window

`canonicalExecutionId` is additive and optional on all four schemas for the
duration of the transition window (from T2's first implementation until every
call site that can populate it does so). During the window:

- Any existing reader that does not know about `canonicalExecutionId` sees an
  absent/`undefined` field and continues to function exactly as it does
  today, because no existing required field is renamed or removed on any of
  the four schemas.
- Any existing writer that does not yet populate `canonicalExecutionId`
  (every Gateway caller other than the future canonical Web port composition,
  per the paired port contract's Compatibility / Rollback Matrix) produces
  records identical to today's, with the new field simply absent.
- `Sot3ActivationEvidenceRecord` uses the exact dual-shape validation rule
  frozen in the owner matrix: the existing thirteen-key shape remains valid;
  the fourteen-key shape is valid only when `canonicalExecutionId` is a
  non-empty string. No `null` placeholder and no schema-version split is
  introduced. The existing record-ID projection stays unchanged, while the
  generic integrity-hash projection covers the new field whenever present.

## Terminal-Path Behavior Summary

For all four owners, a terminal (denial, error, or success) record populates
`canonicalExecutionId` identically to a non-terminal record for the same
request, because the identity is attached at request entry (Web envelope
construction, or the port request built from it), never derived from or
gated on the outcome. This mirrors the existing pattern already used for
`traceId` on `GatewayReceipt` and `MaterialContextManifest` (both are set on
every branch of `ProviderExecutionBridge.execute`, including
`buildStoppedResult` and `buildShieldedErrorResult`) and for `envelopeId` on
`GovernanceEvidenceReceipt` (set once in `buildEvidenceReceipt` regardless of
`decision`).

## Cross-Document Agreement Check

The following names and version tokens are spelled identically in this
document and in
`docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md`:

| Shared name | Spelling used in both documents |
| --- | --- |
| Canonical identity field | `canonicalExecutionId` |
| Port owner package | `CVF_MODEL_GATEWAY` |
| Identity seed source | `WebGovernanceEnvelope.envelopeId` |
| Bridge additive option field | `beforeProviderInvoke` |
| Gateway request identity carrier | `GatewayExecuteRequest.canonicalExecutionId` |
| Receipt schema | `GatewayReceipt` |
| Manifest schema | `MaterialContextManifest` |
| SOT3 schema | `Sot3ActivationEvidenceRecord` |
| Web receipt schema | `GovernanceEvidenceReceipt` |
| Batch ID | `CSCC-R1-T1` |
| Execution base head | `a232e2e7a` |

This check was performed by direct side-by-side re-read of both files
immediately before finishing this tranche; no automated diff tool exists for
this pair, so the comparison is a manual literal-string check across the two
tables above and the corresponding field tables in the paired port contract.

## Claim Boundary

This document freezes exactly one canonical identity field name
(`canonicalExecutionId`), its source, propagation path, additive/optional
transition-window behavior, and a reference/hash join mechanism across four
named schemas. It does not implement any field addition on
`GatewayReceipt`, `MaterialContextManifest`, `Sot3ActivationEvidenceRecord`,
or `GovernanceEvidenceReceipt`, does not modify any digest or integrity-hash
algorithm, does not invoke a provider, and does not authorize T2, MAO launch,
or any runtime composition.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only contract design; public sync is forbidden
per the governing work order and baseline.
