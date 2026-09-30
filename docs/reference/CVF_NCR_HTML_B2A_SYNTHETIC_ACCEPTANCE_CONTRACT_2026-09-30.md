# CVF NCR HTML B2a Synthetic Acceptance Contract

Memory class: POINTER_RECORD

Status: PROPOSAL_NOT_IMPLEMENTED

docType: reference

Date: 2026-09-30

## Purpose

Define, for the operator's later decision, what exact artifact identity means for the HTML review packet and what a future single-host, one-writer acceptance store could look like. Part 1 is implemented as an isolated synthetic candidate. Part 2 is a proposal only: nothing in it is built, wired, authorized or accepted.

## Scope / Applies To

Applies to the HTML export panel and route in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` and to the isolated helper `src/lib/html-artifact-acceptance-candidate.ts`. It does not touch the route, the receipt helper, any page, any database or any real data. The Local B2 audit found no authorized exact-HTML acceptance owner; this contract does not create one.

## Part 1 - Implemented Synthetic Identity Contract

The candidate identifies an artifact by the SHA-256 of the UTF-8 bytes of the exact HTML string returned by an export attempt. The rules below are what the focused synthetic tests check.

| Rule | Meaning |
|---|---|
| Exact bytes | The hash covers every byte of the returned string, including the generated timestamp, title, boundary text and embedded source hash. No trimming, newline conversion, BOM handling or Unicode normalization is applied. |
| No re-render | Verification hashes the string it is given. It never rebuilds HTML from request fields. |
| sourceHash is not identity | The route's `sourceHash` covers source text only, so two packets with the same source text and different title, boundary or timestamp share it. It is recorded as a separate supporting value and is never consulted to verify identity. |
| Distinct identifiers | HTML hash, `sourceHash`, local attempt ID and receipt or receipt-attempt ID are four different values and are stored in different fields. |
| Encoding | A string with a lone surrogate has no exact UTF-8 form and is refused rather than silently substituted. |
| State | A candidate is always `DRAFT_UNACCEPTED`. Verification rejects any other state. No function in the helper accepts, approves, persists or commits. |
| Receipt is evidence | A receipt with decision `ALLOW`, `APPROVED` or any other text is stored as opaque evidence and cannot change the state. |

Limits: the helper is pure and unconnected. It proves that the identity function and its verification behave as described on synthetic strings. It does not prove durability, actor authority, the browser UI or live governance behavior.

## Part 2 - Proposed Future Store Contract (Not Implemented)

Everything here is a proposal for operator decision. None of it exists in code, none is approved, and a separate work order is required before any of it is built.

### Proposed actor

Only an operator-designated accepting actor could accept a version, through an explicit action that is separate from generating HTML and separate from receiving a receipt. The actor identity source and authority are undecided (see Open Decisions).

### Proposed version and record model

- An immutable version record per accepted artifact: HTML hash, byte length, algorithm label, attempt ID, build number, `sourceHash`, receipt evidence copy, the actor, a decision time and the HTML bytes themselves.
- Records are append-only. A correction is a new version that references the earlier one; nothing is updated or deleted in place.
- The store would be a separate authoritative artifact store, not the governance ledger and not the pending-execution store. The existing single-node SQLite store owned by pending execution is a design precedent only, not an owner for this data.

### Proposed write protocol

1. Read the exact bytes that the actor reviewed and recompute the identity. Refuse if it differs from the identity the actor was shown.
2. Begin one local transaction on one host with one writer process.
3. Insert the version record and its bytes in that transaction. A duplicate identity is not an error to overwrite; it resolves to the existing version.
4. Commit before acknowledging. The caller is told "accepted" only after commit.
5. Read back the committed row, recompute the hash over the stored bytes and compare with the identity. Only a matching readback allows the acknowledgment to be reported as verified.

### Unknown outcome and reconciliation

If the process is interrupted or the response is lost after step 3, the outcome is unknown. The proposal is: never retry blindly; look up the identity in the store read-only; a matching committed and verified row means the outcome was "accepted", an absent row means "not accepted", and a row whose bytes fail the hash means "corrupt, needs owner recovery". Reconciliation reports what it found and does not itself grant permission to retry or accept.

### Proposed recovery ownership

A named recovery owner would handle corrupt or ambiguous rows, restore from backup, and record what was done. Backup, key custody and restore drills are not defined here.

## Open Operator Decisions

These are not answered by this contract or by the candidate:

- The real accepting actor or account, and how their authority is established.
- The real data source, instance and classification of what may be accepted.
- Store location, host, and the single-writer and fencing model.
- Backup location, key custody and restore ownership.
- Retention and deletion schedule.
- RPO and RTO targets.
- Cost budget.
- Whether and when any pilot or live effect is allowed.
- Whether Profile B or C applies instead of the synthetic Profile A.

## Claim Boundary

This document is a proposal and a description of an isolated synthetic helper. It is not artifact acceptance, an accepted design, a durable store, an operator decision, proof of any runtime behavior, or authorization for real data, provider or live use, public sync or deployment. Q001 and Q004 remain open.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
