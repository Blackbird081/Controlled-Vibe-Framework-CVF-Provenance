# CVF GC-018 Baseline: MEOR-T1 Metadata Evidence Resolution Contract

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-12

Author: Codex

baseHead: `eb4ad235`

## Purpose

Authorize specification-only authoring for the first tranche of the CVF
Metadata Evidence And Operator Resolution Foundation.

## Scope / Target / Owner Boundary

Target: a domain-agnostic metadata requirement, evidence basis, resolution,
and downstream disposition contract.

Allowed:

- one canonical Markdown contract;
- one machine-readable JSON semantics artifact;
- synthetic regulated and non-regulated examples;
- governance review and closure artifacts.

Forbidden:

- Python or TypeScript implementation;
- Policy_Local candidate correction or external workspace changes;
- OCR, corpus ingestion, EC activation, retrieval, provider use, or public-sync.

## Predecessor Evidence

| Evidence | Path or commit | Result |
| --- | --- | --- |
| Foundation roadmap | `docs/roadmaps/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_FOUNDATION_ROADMAP_2026-06-12.md` | `ACTIVE_FOUNDATION_FIRST_T1_SPEC_PENDING` at `80761d50` |
| EX-T9 report completion | `docs/reviews/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_COMPLETION_2026-06-12.md` | `CLOSED_PASS_BOUNDED` |
| EC-T4 operator report | `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.md` | accepted as use-case evidence only |

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Generic finding record exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 32 | `ScanOutcomeFinding` | dataclass | ACCEPT |
| Report accepts additional findings | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 131-144 | `additional_findings` | `build_scan_outcome_report` | ACCEPT |
| Deterministic JSON renderer exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 202 | `render_scan_outcome_report_json` | function | ACCEPT |
| Domain profile owns scoped metadata maps | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 23-53 | `DscpDomainProfile` | interface | ACCEPT |
| Regulated lifecycle fields are LPCI-specific | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 20, 40-42 | `DocumentStatus` | LPCI types | ACCEPT |
| EC-02 semantics are domain extension evidence | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | `documentStatusEnum`, `queryClassMatrix` | `ec02GateToken` | JSON contract | ACCEPT |

## Decision

MEOR-T1 is specification-only. The contract must define exact allowed values,
invalid combinations, failure tokens, claim boundaries, and cross-domain
examples before implementation begins.

## Required Semantics

- observed states: `PRESENT`, `MISSING`, `AMBIGUOUS`, `CONFLICTING`,
  `UNSUPPORTED`, `NOT_APPLICABLE`;
- evidence bases: `SOURCE_EMBEDDED`, `OPERATOR_SUPPLIED`, `DERIVED_HINT`,
  `NONE`;
- resolution states: `RESOLVED`, `OPERATOR_ACTION_REQUIRED`, `BLOCKED`;
- downstream dispositions: `RETAIN_BLOCK`, `ELIGIBLE_FOR_REEVALUATION`;
- source/operator provenance must remain distinct;
- no raw source content is released;
- report generation never mutates downstream state.

## Required Evidence

- JSON parse PASS;
- contract/JSON value alignment PASS;
- regulated and non-regulated examples PASS;
- no runtime/source paths changed;
- reviewer-fast and pre-closure gates PASS.

## Stop Conditions

Stop if the contract requires legal-specific fields, global domain defaults,
external workspace edits, runtime implementation, provider use, or autonomous
metadata correction.

## Claim Boundary

This baseline authorizes contract authoring only. It does not prove runtime
behavior, metadata correctness, source authenticity, Policy_Local readiness,
retrieval quality, production readiness, or public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private specification baseline; no public-sync authorized.
