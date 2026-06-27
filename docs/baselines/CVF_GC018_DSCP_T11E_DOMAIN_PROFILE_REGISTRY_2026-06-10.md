# CVF GC-018 DSCP-T11E Domain Profile Registry Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-10

---

## Authorization

Authorized by operator instruction on 2026-06-10: review and close the
DSCP-T11E worker return, then audit and prepare the next bounded Claude lane.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open DSCP-T11E as a bounded deterministic CPF source tranche.

T11E consumes the already closed DSCP-T10 domain profile contract and DSCP-T11
profile-aware harness evidence. It adds a local in-memory registry and selector
so scan-layer callers can select a domain profile without treating PolicyLocal
as the global default.

## Purpose

DSCP-T11 proved that an explicit profile can flow through local DSCP packaging
surfaces. T11E adds a deterministic local profile registry so the scan layer can
choose among multiple domain profiles by profile ID, domain family, language, or
facet key before profile application.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
|---|---|---|
| DSCP-T10 domain profile contract | `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md`; material commit `0afa8737` | ACCEPT |
| DSCP-T11 profile-aware pipeline harness | `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md`; material commit `4c39ce77` | ACCEPT |
| Packet gate hardening | `governance/compat/check_agent_packet_authority_and_encoding.py`; commit `53a0e192` | ACCEPT |

## Scope / Target / Owner Boundary

In scope:

- Add `DscpDomainProfileRegistry` and
  `createDscpDomainProfileRegistry` in CPF.
- Add deterministic profile selection by `domainProfileId`, `domainFamily`,
  `languageCode`, and `requiredFacetKey`.
- Export the registry through `control.plane.context.barrel.ts`.
- Add focused CPF tests for registration, duplicate handling, replacement,
  unregister, list, exact selection, ambiguous selection, no-match selection,
  facet-key selection, and select-then-apply integration.
- Register the new source and test files in GC-051 JSON and Markdown.
- Close with a worker return and Codex completion review.

Out of scope:

- No external `Policy_Local` workspace edits.
- No corpus ingestion, OCR, body extraction, vector search, retrieval quality,
  semantic ranking, T12 authoring, provider call, API key use, cvf-web route
  change, public-sync, hosted readiness, production readiness, or public
  readiness.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: domain profile ID type | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 8 | `DomainProfileId` | `DomainProfileId` | ACCEPT |
| EXISTS: domain family type | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 12 | `DscpDomainFamily` | `DscpDomainFamily` | ACCEPT |
| EXISTS: domain profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| RUNTIME_BEHAVIOR: profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 92 | `applyDomainProfileToDescriptorInput` | `applyDomainProfileToDescriptorInput` | ACCEPT |
| EXISTS: existing profile helper barrel export | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | line 77 | `applyDomainProfileToDescriptorInput` | `control.plane.context.barrel.ts` | ACCEPT |

New T11E implementation symbols are proposed outputs of this tranche, not
pre-existing source facts. They are verified after implementation by the
completion review and focused tests.

## Evidence / Verification

| Evidence | Required result |
|---|---|
| CPF package check | PASS |
| Focused DSCP-T11E vitest | PASS, 18/18 |
| Reviewer-fast gate | PASS, current chain count |
| GC-051 registry coverage | PASS |
| Forbidden paths | none modified |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_FOR_CLAUDE_2026-06-10.md` | `Status: DISPATCHED` before closure | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_COMPLETION_2026-06-10.md` | reviewer-authored after worker return | PENDING |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_ROADMAP_2026-06-10.md` | `Status: DISPATCHED` before closure | READY |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T11E source/test paths covered | PENDING |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11E quick lookup rows | PENDING |
| Session continuity | active handoff and state registry | reviewer sync after closure | PENDING |

## Claim Boundary

This baseline authorizes only a local deterministic CPF registry and selector.
It does not claim provider behavior, live governance proof, retrieval quality,
semantic correctness, corpus ingestion, OCR, vector search, PolicyLocal T12
readiness, current-law status, legal advice quality, public readiness, hosted
readiness, production readiness, public-sync, memory reinjection, high-risk
promotion, Learning Orchestrator runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.
