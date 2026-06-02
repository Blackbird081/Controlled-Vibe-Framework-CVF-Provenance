# CVF GC-018 - CSA1 Corpus Standard Authoring (NR-05 / NR-11)

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-02

baseHead: `8e7d1770`

dispatchBaseHead: `8e7d1770`

## Purpose

Authorize CSA1 to author the two written governance standards that CI1-T6
decided were `STANDARD_REQUIRED_FIRST` precursors to any machine checker:

- NR-05 — CVF Corpus Path Normalization Algorithm
- NR-11 — canonical disposition merge rule (DEFER vs ACCEPT_SUMMARY_ONLY)

These standards are the precondition that unblocks the deferred NR-05 and
NR-11 checker spec stubs recorded in the CI1-T6 decision artifact, and they
are inherited obligations for any future LPCI ingest/query/classification
implementation per the CI1-T7 intake bridge.

CSA1 is a documentation-only standards-authoring tranche. It does not
implement any checker, runtime, LPCI component, or provider call.

## Source

- CI1-T6 decision artifact:
  `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`
- CI1-T7 intake bridge:
  `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`
- T4 cross-corpus index model (NR-05 normalizedPath, NR-11 disposition):
  `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- Existing classification standard (NR-11 extension target):
  `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
- Readiness packet template (NR-05 algorithm reference target):
  `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`

## Decision

Proceed with a bounded documentation-only tranche that creates:

- `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md`
  — NR-05 canonical path normalization algorithm
- a NR-11 canonical disposition merge rule, authored as a new section in
  `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
  (extension of the existing classification standard, not a new file)
- a scoped work order
- this GC-018 baseline
- a bounded completion review

No checker code is written. The standards are the written precursors; the
NR-05 and NR-11 checker spec stubs from CI1-T6 remain deferred to a separate
checker-implementation roadmap.

## Scope / Target / Owner Boundary

Worker may:

- read the CI1-T6 decision artifact, CI1-T7 intake bridge, and T4 model;
- read the existing classification standard and readiness packet template;
- create `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md`;
- add a bounded NR-11 disposition merge rule section to
  `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`;
- create the work order, this baseline, and a completion review;
- repair allowed-scope documentation defects.

Worker must not:

- implement any Python checker, TypeScript guard, or test file;
- edit `governance/compat/`, `governance/toolkit/`, hook chains, guard docs,
  session front doors, active handoff, or state registry (worker only);
- modify the T4 model JSON beyond what an authored standard requires (the
  NR-05/NR-11 vocabulary itself is already present; no model edit is needed);
- implement any LPCI component, runtime, provider call, or live proof;
- enumerate or scan any new legacy root or sibling folder;
- public-sync, commit, or push.

Risk ceiling: R1 documentation-only standards authoring.

## Standards Contract

### NR-05 Path Normalization Algorithm — required content

| Section | Requirement |
| --- | --- |
| Canonical form | forward-slash separator, all lowercase, no trailing separator, relative to corpus root |
| Application rule | how a packet author computes `normalizedPath` per classification-ledger row |
| Edge cases | spaces, non-ASCII, Windows backslash paths, case-insensitive filesystems |
| Checker readiness note | states the NR-05 checker stub becomes implementable once this standard exists |
| Claim boundary | standard is authoring guidance; no runtime path resolution is claimed |

### NR-11 Disposition Merge Rule — required content

| Section | Requirement |
| --- | --- |
| Canonical merge value | DEFER (T2 style) and ACCEPT_SUMMARY_ONLY (T3 style) both resolve to `ACCEPT_DEFERRED` for cross-packet queries |
| Raw preservation | original packet value preserved as `rawDisposition` |
| Application rule | when a packet author must annotate `dispositionAlias` |
| Checker readiness note | states the NR-11 checker stub becomes implementable once this rule exists |
| Claim boundary | merge rule is cross-packet query guidance; no runtime routing is claimed |

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| NR-05 standard created | canonical form + application + edge cases + checker-readiness note present |
| NR-11 merge rule added | canonical `ACCEPT_DEFERRED` value + `rawDisposition` preservation present |
| Checker stubs referenced | both standards cite the matching CI1-T6 checker stub as the deferred follow-on |
| No checker code written | `governance/compat/` not modified |
| No runtime artifacts | no TS, py, or test files created |
| Claim boundary present | no checker-enforcement, runtime, LPCI, or public claim |

## Source Verification Table

| Token | Verified path or symbol |
| --- | --- |
| `CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` |
| `CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` |
| `CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` |
| `CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` |
| `normalizedPath` | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` normalizationRules NR-05 |

## Evidence

| Evidence | Requirement |
| --- | --- |
| NR-05 standard present | canonical algorithm + checker-readiness note |
| NR-11 merge rule present | `ACCEPT_DEFERRED` + `rawDisposition` |
| No checker code | `governance/compat/` and `EXTENSIONS/` not modified |
| Pre-closure gates PASS | content-checking autorun gates PASS over committed range |

## Claim Boundary

This baseline authorizes CSA1 documentation-only standards authoring only.
It does not authorize checker implementation, runtime control changes, LPCI
implementation, provider calls, live proof, public-sync, commit, or push.
The NR-05 and NR-11 checker spec stubs remain deferred to a separate
checker-implementation roadmap.

## Commit Mode

WORKER_MAY_COMMIT

The dispatching session (this session, acting as orchestrator) may author the
standards directly and commit them as a single governed batch, because CSA1 is
a bounded R1 documentation-only tranche with no protected-file, checker, or
runtime scope. Session continuity sync follows the dedicated session-sync
pattern.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
