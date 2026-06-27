# CVF GC-018 LPCI2 EC-T5 DSCP Gate Value Update Block Decision

Memory class: FULL_RECORD

Status: CLOSED_BLOCKED_BOUNDED

docType: baseline

Date: 2026-06-11

executionBaseHead: `b815fcf9`

---

## Purpose

Authorize Codex to close EC-T5 as a bounded block decision instead of applying
`ec02Gate: "QUERY_CLASS_GATED"` to DSCP domain profiles.

EC-T5 was originally scoped as a DSCP gate value update after EC-T4. EC-T4
returned `PARKED_PENDING_OPERATOR_METADATA`; the proposed metadata backfill
keeps all six records on `BLOCKED_UNTIL_2026-07-01`, all six records require
operator confirmation, and four records remain `UNKNOWN_OR_AMBIGUOUS`.

The current runtime contract also treats only `BLOCKED*` and `PROHIBITED`
boundary rule values as blocking values. Therefore applying
`QUERY_CLASS_GATED` now would create a non-blocking custom gate value before
query-class routing and disclosure behavior are wired.

## Authorization

Operator instruction on 2026-06-11 authorized Codex to:

- raise the checker for prior-verification reuse and Unicode evidence handling;
- switch roles and complete EC-T5;
- preserve CVF foundation quality instead of forcing an unsafe tranche through.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Close EC-T5 as `CLOSED_BLOCKED_BOUNDED`.

Do not modify DSCP profiles, runtime source, external Policy_Local data, corpus
records, retrieval behavior, public-sync, or EC-T2 semantics.

Record a machine-readable block decision so a later EC-T5 successor can reopen
only after both conditions are satisfied:

- operator-confirmed metadata resolves the EC-T4 gaps; and
- the runtime/query layer has a source-verified plan that treats
  `QUERY_CLASS_GATED` as a gated routing signal rather than a flat pass.

## Scope / Target / Owner Boundary

In scope:

- create this GC-018 block-decision baseline;
- create a source-verified Codex work order for the bounded decision;
- create a machine-readable EC-T5 block-decision JSON artifact;
- create a completion review with claim boundary;
- update the parent roadmap and session continuity.

Out of scope:

- no `EXTENSIONS/**` runtime or test changes;
- no DSCP profile value changes;
- no external `Policy_Local` changes;
- no corpus ingestion or generated corpus mutation;
- no provider/API-key call, live governance proof, OCR model download, public
  sync, current-law/legal-quality claim, production/public readiness, memory
  reinjection, high-risk promotion, or autonomous mutation.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EC-T5 was planned as DSCP gate value update | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 629 | `EC-T5` | parent roadmap | ACCEPT |
| VALUE_SET: EC-T5 target token | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | line 5 | `ec02GateToken` | EC-T2 machine semantics | ACCEPT |
| LITERAL_INVARIANT: EC-T5 token is active only after operator supplied effective dates | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | line 56 | `ec02GateTokenActiveFrom` | EC-T2 machine semantics | ACCEPT |
| VALUE_SET: EC-T4 proposed backfill retained blocked gate for all six records | `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json` | lines 38, 62, 86, 110, 134, and 158 | `ec02GateRetained` | EC-T4 proposed metadata JSON | ACCEPT |
| VALUE_SET: EC-T4 requires operator confirmation for all six records | `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json` | lines 39, 63, 87, 111, 135, and 159 | `operatorConfirmationRequired` | EC-T4 proposed metadata JSON | ACCEPT |
| VALUE_SET: four EC-T4 records remain unknown or ambiguous | `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json` | lines 53, 101, 125, and 149 | `currentStatusEvidenceClass` | EC-T4 proposed metadata JSON | ACCEPT |
| RUNTIME_BEHAVIOR: current profile apply code blocks only blocked/prohibited boundary values | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 104-106 | `applyDomainProfileToDescriptorInput` | CPF DSCP domain profile contract | ACCEPT |
| RUNTIME_BEHAVIOR: gate values are copied from boundary rules into custom gates | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 151-154 | `profile.domainGateKeys`; `profile.boundaryRules` | CPF DSCP domain profile contract | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:

- `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md`
- `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json`

priorVerificationAnchor: EC-T4 Codex reviewer recomputed six T11B hashes and
sizes and parked EC-T4 on metadata gaps.

freshRecomputeRequired: `NO`

recomputeReason: `N/A with reason - EC-T5 consumes EC-T4 reviewer evidence and
does not read or mutate external binary source files.`

unicodePathHandling: `N/A with reason - EC-T5 does not open Unicode external
paths or extracted text.`

extractedTextAuthority: `N/A with reason`

## Closure Boundary

This baseline closes only the EC-T5 decision that the gate value update must
not be applied yet. It does not close EC-T6, does not unblock T12, does not
prove current-law status, and does not claim runtime retrieval behavior.

## Claim Boundary

This baseline is a governance authorization and block-decision record only. It
does not prove provider behavior, runtime routing, corpus quality, legal
correctness, production readiness, public readiness, or release readiness.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; no public-sync authorized.
