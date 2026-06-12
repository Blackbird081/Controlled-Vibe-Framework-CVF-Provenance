# CVF GC-018 Baseline: MEOR-RDA-T3 Cross-Domain Conformance

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-06-12

Owner: Codex

baseHead: `ae3f3386`

## Purpose

Authorize a bounded conformance tranche proving that the regulated-domain
adapter remains profile-scoped across legal-policy and non-regulatory domain
profiles.

## Scope / Target / Owner Boundary

In scope:

- focused CPF conformance tests for RDA-T2 adapter behavior;
- proof that non-regulatory profiles do not inherit regulated lifecycle
  requirements;
- proof that cross-profile regulated requirement bleed fails closed through
  the existing DSCP metadata requirement bridge;
- GC-051 registry coverage for new conformance test surfaces;
- Codex review, closure, roadmap, and continuity updates after worker return.

Out of scope:

- source behavior changes unless explicitly returned as blocked;
- external Policy_Local mutation;
- candidate metadata correction;
- EC-T5/EC-T6 activation or `QUERY_CLASS_GATED` write;
- retrieval, OCR, corpus ingestion, provider/API-key use;
- public-sync, production readiness, public readiness;
- memory reinjection, high-risk promotion, autonomous mutation.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Post-T2 audit | `docs/audits/CVF_MEOR_RDA_POST_T2_NEXT_TRANCHE_AUDIT_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| RDA roadmap | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | ACTIVE_RDA_T3_DISPATCHED |
| RDA-T2 completion | `docs/reviews/CVF_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| RDA-T2 material commit | git commit `1c47d125` | ACCEPT |
| RDA-T2 session sync | git commit `ae3f3386` | ACCEPT |

## Source / Predecessor Evidence

Dependency release evidence:

- RDA-T2 completion status: `CLOSED_PASS_BOUNDED`;
- material commit: `1c47d125`;
- session sync commit: `ae3f3386`;
- parent roadmap row: RDA-T3 `READY_FOR_FRESH_AUTHORIZATION`;
- pre-closure autorun over `6a9a5703..ae3f3386`: PASS.

## Decision / Baseline / Proposed Tranche

Decision: authorize RDA-T3 as a bounded conformance tranche.

Baseline:

- worker mode: `WORKER_MUST_NOT_COMMIT`;
- implementation surface: CPF tests only by default;
- reviewer-owned closure: Codex;
- next tranche after RDA-T3, if closed, is RDA-T4 foundation closure and
  Policy_Local successor readiness decision.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

- exercise the RDA-T2 adapter through the CPF context barrel;
- use synthetic profile fixtures only;
- prove exact regulated requirement presence for legal-policy profile with
  `supportsDocumentStatus=true`;
- prove no generated regulated requirements for company-docs,
  technical-project, governance-docs, mixed-corpus, and legal-policy profiles
  without the support flag;
- prove bridge rejection for cross-profile requirement ownership mismatch.

Rejected design:

- editing RDA-T2 adapter behavior before conformance fails;
- using real Policy_Local files;
- using OCR/retrieval/provider paths;
- claiming legal/current status or metadata truth.

## Dispatch Boundary

This baseline authorizes dispatch of a source-verified RDA-T3 work order only.
Any need to mutate runtime source, external Policy_Local, EC gate values,
retrieval, OCR, provider/API-key paths, public-sync, or readiness claims must
return to Orchestrator.

## Acceptance Criteria

1. Tests import RDA-T2 adapter through the CPF context barrel.
2. Regulated legal-policy profile with `supportsDocumentStatus=true` produces
   exactly four regulated requirements.
3. Non-regulatory profiles produce zero generated requirements.
4. Legal-policy profile without the support flag produces zero generated
   requirements.
5. Cross-profile attachment of regulated requirements fails closed with
   `OWNER_PROFILE_MISMATCH`.
6. Test fixtures remain synthetic and do not read external Policy_Local files.
7. Focused CPF tests pass.
8. GC-051 registry covers any new conformance test file.

## Evidence / Verification

Required verification:

- focused CPF conformance test command and result;
- `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`;
- reviewer-fast before Codex closure review;
- pre-closure autorun before final closed claim;
- changed-path proof excluding external Policy_Local and EC activation paths.

## Claim Boundary

This baseline authorizes only local deterministic conformance tests for the
regulated-domain adapter. It does not prove metadata truth, legal/current
status, source authenticity, Policy_Local readiness, EC activation, retrieval
quality, provider behavior, production readiness, public readiness, or
autonomous correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private conformance dispatch baseline; no public-sync authorized.
