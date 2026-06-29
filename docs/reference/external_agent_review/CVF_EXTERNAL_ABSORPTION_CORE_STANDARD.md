# CVF External Absorption Core Standard

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-06-29

## Purpose

Define the invariant core for any CVF work that absorbs an external repository,
copied folder, archived external pack, or retained legacy source folder.

Different repositories may contain different value. The core process is not
different: every external absorption output must prove what corpus existed,
what was read, what value was dispositioned, where accepted value maps in CVF,
and what remains unresolved.

## Scope / Applies To

This standard applies to governed roadmaps, baselines, work orders, reviews,
audits, and external-agent reference artifacts that absorb, audit, reabsorb,
reopen, classify, or close value from an external repository, copied folder,
archived external pack, or retained legacy source folder.

It does not apply to internal-only CVF maintenance that does not consume an
external source set. It also does not apply to guard-maintenance completion
reviews that implement this checker without claiming any external corpus
absorption.

## Central Core

External absorption is not complete because an agent says it inspected the
source. It is complete only within a bounded corpus after the artifact records:

- a filesystem-backed or source-backed manifest;
- a file-level processing ledger;
- an absorption disposition ledger;
- an owner-surface map for accepted value;
- unresolved, deferred, rejected, and blocked items;
- a claim boundary that prevents runtime, provider, public, or production
  expansion without fresh governed work.

This standard extends the external knowledge chain map. It does not make
external material canonical, authorize implementation, execute providers,
install plugins, mutate runtime, publish public artifacts, or prove semantic
quality by itself.

## Required Artifact Block

Any governed artifact that absorbs, audits, reabsorbs, reopens, classifies, or
closes value from an external repo or copied folder must include this block:

```text
## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | <repo URL, commit, local root, or bounded file list> |
| Enumeration command | <filesystem-backed command or structured source listing> |
| Manifest artifact or inline manifest | <path or inline table> |
| Processing ledger artifact or inline ledger | <path or inline table with file-level rows> |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | <CVF owner reference, roadmap, work order, source path, or BLOCKED_SOURCE_NOT_FOUND> |
| Unresolved items | <0 or explicit list> |
| Completion claim boundary | <bounded claim; no runtime/provider/public/production expansion> |
```

Do not use placeholder text in the block. Do not use
`NOT_APPLICABLE_WITH_REASON` for the paired `Corpus Completeness And Report Integrity` block when the artifact is actually absorbing an external repo or copied folder.

## Required Ledger Semantics

The processing ledger proves that each manifest item reached a terminal
processing status. The disposition ledger proves what CVF did with the value.

Allowed processing statuses:

| Status | Meaning |
|---|---|
| `READ` | The file was opened or parsed and considered. |
| `ADAPTED` | Value was rewritten into CVF language or owner surfaces. |
| `DEFERRED` | Value is real but intentionally parked with a reopen condition. |
| `REJECTED` | Direct adoption is rejected with a reason. |
| `NO_NEW_VALUE` | File was read but adds no new value beyond existing owner surfaces. |
| `BLOCKED_UNREADABLE` | File could not be processed and must stay visible. |

Allowed disposition outcomes:

| Disposition | Meaning |
|---|---|
| `ABSORB` | Promote directly into a CVF-owned artifact in this tranche. |
| `ADAPT` | Rewrite the concept into CVF terms or an existing owner surface. |
| `DEFER` | Park for a future governed tranche with a concrete reopen condition. |
| `REJECT` | Reject direct use and keep only as contrast or evidence. |
| `BLOCK` | Stop or return because source authority or access is missing. |
| `NO_NEW_VALUE` | No meaningful delta after reading the source. |

## Machine Guard

Machine guard:

`governance/compat/check_external_absorption_core.py`

The guard is forward-only and range-aware. It checks changed active governed
Markdown artifacts that reference external absorption sources, external
repository URLs, copied-folder intake, or the explicit marker:

`External absorption core: REQUIRED`

The guard requires the external absorption core block, corpus completeness
evidence that is not `NOT_APPLICABLE_WITH_REASON`, external knowledge intake
routing, non-empty manifest and ledger fields, allowed status vocabulary, and
an owner-surface map.

The guard does not prove semantic understanding. It makes the corpus and
disposition evidence reviewable and blocks narrative-only closure.

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_NA_WITH_REASON: canonical
governance standard definition; no empirical corpus result, provider behavior,
runtime behavior, or external-source absorption claim is asserted by this
standard.

Expected Result / Prediction: N/A - standard definition artifact.

Evidence Comparison: N/A with reason: direct evidence belongs to the paired
checker tests and completion review, not this reference definition.

Contradiction Or Gap Disposition: N/A with reason: future absorption artifacts
may reveal semantic-quality gaps, but this standard only defines the required
evidence shape.

Claim Update: no predicted corpus or runtime claim is updated by this
reference artifact.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> external absorption core -> corpus manifest and ledger -> owner-surface disposition -> GC-018/work order/source verification if implementation is needed |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Disposition | ADAPT as central external absorption core standard and machine-check candidate |
| Claim boundary | routing and evidence-shape standard only; no semantic-completeness, runtime, provider, public, or production claim |

## Claim Boundary

This standard defines required evidence shape for external absorption work. It
does not claim that any external source has been fully absorbed, does not make
external material canonical, does not install runtime behavior, does not prove
provider or live behavior, and does not authorize public-sync or production
readiness.
