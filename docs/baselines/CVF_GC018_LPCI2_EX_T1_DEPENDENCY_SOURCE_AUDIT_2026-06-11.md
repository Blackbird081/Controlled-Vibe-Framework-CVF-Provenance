# CVF GC-018 LPCI2 EX-T1 Dependency Source Audit Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-11

---

## Authorization

Authorized by operator instruction on 2026-06-11: create the next work order
under the new governed work design-control foundation.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open LPCI2 EX-T1 as an audit-only child lane for the reusable CVF scan and
extraction foundation.

EX-T1 must produce source-backed dependency evidence before CVF chooses any
document extraction stack. This baseline authorizes only evidence collection,
local feasibility probes, and a worker return packet. It does not authorize
extractor implementation.

## Purpose

Establish a source-backed dependency and environment decision base for future
CVF document-to-text extraction work. The audit must compare the composed stack
and LiteParse candidate path without adding repo dependencies or changing
runtime behavior.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
|---|---|---|
| Governed work design-control hardening | material commit `84217223`; session sync `8b6bd04d` | ACCEPT |
| LPCI2 Extraction and EC-02 Refinement roadmap | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | ACCEPT |
| T11D readiness gate | `docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_COMPLETION_2026-06-07.md`; material commit `bd36e808` | ACCEPT |
| DSCP-T11F profile selection adapter material packet | material commit `be6a0a17`; closure pending | ACCEPT_AS_EXISTING_LOCAL_CONTEXT |

## Scope / Target / Owner Boundary

In scope:

- Audit official or primary dependency sources for the candidate extraction
  stacks named by the roadmap.
- Run bounded local install/import feasibility probes in a temporary
  environment when safe.
- Verify Windows and CI constraints for candidate dependency stacks.
- Verify OCR language-code mapping requirements from DSCP profile language
  codes to candidate OCR engine codes.
- Produce report and worker-return artifacts for Codex review.

Out of scope:

- No extractor implementation.
- No repo dependency addition or lockfile update.
- No OCR model download.
- No corpus ingestion, chunking, retrieval, T12 authoring, or EC-02 semantic
  change.
- No provider calls, API keys, public-sync, hosted readiness, production
  readiness, public readiness, legal-quality claim, or current-law claim.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: parent roadmap dispatch boundary | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 163 | `Dispatch Boundary` | parent roadmap | ACCEPT |
| EXISTS: EX-T1 audit tranche | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 461 | `EX-T1` | parent roadmap work plan | ACCEPT |
| EXISTS: minimum EX-T1 source checks | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 252 | `Minimum EX-T1 source checks` | parent roadmap | ACCEPT |
| EXISTS: DSCP domain profile | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| EXISTS: profile language codes | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 31 | `languageCodes` | `DscpDomainProfile` | ACCEPT |
| EXISTS: profile boundary rules | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 46 | `boundaryRules` | `DscpDomainProfile` | ACCEPT |
| EXISTS: design-control gate requirement | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | line 93 | `Design Control Gate` | lifecycle standard | ACCEPT |
| EXISTS: work-order design carry-forward requirement | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 965 | `Design Control Carry-Forward` | work-order template | ACCEPT |

## Evidence / Verification

| Evidence | Required result |
|---|---|
| EX-T1 audit report | present with source-backed dependency matrix |
| EX-T1 machine summary JSON | present with candidate verdicts and hashes where applicable |
| Local probe ledger | present; no repo dependency files modified |
| OCR language-code mapping table | present; values source-backed from primary docs |
| Reviewer-fast gate | PASS before return |
| Forbidden path scan | no runtime/source/public/corpus path modified |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_FOR_CLAUDE_2026-06-11.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Audit report | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | worker-created report | PASS |
| Machine summary | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | worker-created JSON | PASS |
| Worker return | `docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md` | worker return packet with reviewer remediation | PASS |
| Session continuity | active handoff and state registry | reviewer sync in closure batch | PASS |

## Claim Boundary

This baseline authorizes only dependency/source audit, temporary local
feasibility probes, and report artifacts. It does not prove extraction runtime,
OCR quality, parser fitness, retrieval quality, corpus ingestion, EC-02 runtime
behavior, T12 eligibility, provider behavior, public readiness, hosted
readiness, production readiness, public-sync, memory reinjection, high-risk
promotion, Learning Orchestrator runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.
