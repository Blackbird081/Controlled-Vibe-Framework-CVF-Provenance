# CVF GC-018 - MKG2 Deferred Runtime Candidate Triage

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_PLANNING

docType: baseline

Date: 2026-06-01

## Purpose

Open the successor tranche after MKG1. `MKG2` is limited to triaging the `21`
MKG1 deferred assets into source-verified future work packets; it does not
authorize runtime implementation, graph retrieval, Cortex bridge execution,
skill mutation, provider use, public-sync, or live proof.

## Decision

Decision: open planning tranche only.

MKG2 may prepare a dispatchable roadmap/work order for deferred runtime,
bridge, graph-execution, and skill-governance candidates only after the
candidate list cites the MKG1 completion packet and the RESCAN-C manifest JSON
backing.

## Source

- MKG1 completion:
  `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md`
- RESCAN-C manifest:
  `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`
- Manifest hash:
  `ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff`

## Proposed Tranche

MKG2 candidate groups:

| Candidate group | Source family | Asset count | Planning disposition |
| --- | --- | ---: | --- |
| Cortex bridge/runtime | `CVF ADD/cortex-hub` | 11 | HOLD for source-verified runtime-owner map |
| Governed skill evolution | `CVF 16.5/Memento-Skills` | 9 | HOLD for skill-governance boundary review |
| Graph implementation plan | `CVF ADD/code-review-graph` | 1 | HOLD for current graph-runtime owner verification |
| Total |  | 21 | HOLD until dispatch packet is source-verified |

## Required Evidence

- cite the manifest JSON and hash in any future corpus block;
- enumerate all `21` deferred assets from the MKG1 ledger;
- include a Source Verification Block for every claimed current runtime owner;
- include Worker Autonomy / No-Question Rule before any READY/DISPATCHED work
  order;
- keep any live/provider proof in a later explicit tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private planning baseline only. No public-sync remote, public
repository commit, or public artifact path is included.

## Claim Boundary

MKG2 is opened as a planning tranche only. It does not authorize code changes,
runtime behavior, graph retrieval, reinjection, skill mutation, public claims,
hosted readiness, production readiness, or live provider proof.
