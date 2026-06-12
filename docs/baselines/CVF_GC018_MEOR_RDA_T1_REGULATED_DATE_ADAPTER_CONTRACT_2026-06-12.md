# CVF GC-018 Baseline: MEOR-RDA-T1 Regulated-Date Adapter Contract

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-06-12

Author: Codex

baseHead: `d1140459`

## Purpose

Authorize a specification-only tranche that defines how regulated-date
concepts map into the generic MEOR metadata evidence and operator resolution
contract.

## Scope / Target / Owner Boundary

Allowed:

- author an adapter contract and machine-readable semantics;
- source-verify MEOR, DSCP, LPCI, and EC-02 source surfaces;
- record synthetic examples and invalid combinations;
- update the parent RDA roadmap and session continuity.

Forbidden:

- runtime/source implementation;
- external Policy_Local workspace edits;
- candidate metadata correction;
- EC-T5/EC-T6 activation;
- retrieval, OCR, corpus ingestion, provider/API-key use;
- public-sync, production readiness, or public readiness.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Result |
| --- | --- | --- | --- |
| MEOR foundation closure | `docs/reviews/CVF_MEOR_T5_FOUNDATION_CLOSURE_AND_DOWNSTREAM_READINESS_COMPLETION_2026-06-12.md` | `6c2ad2b3` | PASS |
| MEOR session sync | active state/memory/handoff | `d1140459` | PASS |
| Parent RDA roadmap | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | this dispatch batch | ACTIVE_RDA_T1_DISPATCHED |

## Source / Predecessor Evidence

- MEOR contract and semantics define the generic evidence, resolution, and
  downstream disposition vocabulary.
- MEOR-T5 closure releases only the regulated-domain adapter lane.
- DSCP profile contract exposes profile-scoped `metadataRequirements` and
  `supportsDocumentStatus`.
- LPCI types expose regulated lifecycle fields, but EC-T1 keeps those fields
  out of non-regulatory domains by default.
- EC-02 semantics retain the hard date boundary and do not authorize runtime
  gate activation in this tranche.

## Decision

RDA-T1 may proceed as a docs-only specification tranche. It must not implement
runtime behavior or touch external Policy_Local paths.

## Required Evidence

- Source Verification Block for every existing field, enum, function, schema,
  or path referenced;
- New Doc-Only Fields table for proposed adapter contract fields;
- adapter contract and JSON semantics;
- examples covering regulated and non-regulatory profiles;
- no runtime/source or external Policy_Local changes;
- reviewer-fast and pre-dispatch autorun gate evidence.

## Claim Boundary

This baseline authorizes contract authoring only. It does not authorize
adapter implementation, Policy_Local mutation, metadata correction, EC
activation, retrieval, provider behavior, production readiness, public
readiness, or public-sync.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private adapter baseline and dispatch package; no public-sync
authorized.
