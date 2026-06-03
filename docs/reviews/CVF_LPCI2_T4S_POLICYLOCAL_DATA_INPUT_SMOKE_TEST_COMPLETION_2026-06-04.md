# CVF LPCI2-T4S PolicyLocal Data Input Smoke Test Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-04

executionBaseHead: `e5c18554`

## Purpose

Close the bounded PolicyLocal data-input smoke test after the operator supplied
two real local files.

## Scope / Applies To

Applies to: PolicyLocal local data-input folder naming, hash smoke test, and
GC-051 registry update.

## Evidence Trace Block

| Evidence | Result |
| --- | --- |
| Folder rename | `Policy_Local\uploads` renamed to `Policy_Local\data_input` |
| Files detected | `data_input/116_2025_QH15_666020.docx`; `data_input/148_2025_QH15_675262.docx` |
| File sizes | `36528` bytes; `27881` bytes |
| Normalized paths | `data_input/116_2025_qh15_666020.docx`; `data_input/148_2025_qh15_675262.docx` |
| Source hashes | `sha256:df714c0b29b2fa74483961d133c7334cb19c2d0f5c8b4e829d6a209a1a5ac5a7`; `sha256:4ffafd1533348d80debe3e9565f6be06ebfa709381b7b354daee5cbc8ddc9eb5` |
| Processing status | `HASHED_ONLY` |
| Extraction status | `DEFERRED_DOCX_TEXT_EXTRACTION` |
| Answer boundary | `ESCALATE_OR_ABSTAIN` |
| Local manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-data-input-manifest.json` |
| Script check | `node --check scripts/policylocal-import-smoke.mjs` PASS |
| Smoke test | `node scripts/policylocal-import-smoke.mjs` PASS, 2 files hashed |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T3 allows import-first work when real files exist | `docs/reference/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLAN_2026-06-03.md` | T4 Release Conditions | Import-first T4 | LPCI2-T3 plan | ACCEPT |
| Registry entry updated | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | corpora entry | policylocal-production-corpus-dropzone | GC-051 registry | ACCEPT |
| Hash boundary required before runtime | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | Source Hash Policy | sourceHash | LPCI1 T1 intake | ACCEPT |

## Completion Summary

The local folder name has been changed from `uploads` to `data_input` to match
the product's local-first privacy posture. Two operator-supplied DOCX files were
enumerated and hashed locally. A manifest was generated with `sourceHash`,
`normalizedPath`, size, extension, and conservative answer boundary fields.

The smoke test deliberately stops before DOCX text extraction. Therefore the
record remains `HASHED_ONLY`, domain fields remain `unknown`, and answerClass is
`ESCALATE_OR_ABSTAIN`.

## Findings / Position

Position: `CLOSED_PASS_BOUNDED`.

Finding: the first real files prove the local data-input/hash path works, but
DOCX text extraction and legal/policy classification are still absent.

## Risk / Corrective Action

Risk: a future runtime worker could mistake a hash-only record for a source text
record and answer from filename or prior knowledge.

Corrective action: future T4 import/classification must extract DOCX text
locally, populate domain fields, run GC-047/GC-050, and keep answerClass
`ESCALATE_OR_ABSTAIN` until source text and evidence pointers exist.

## Closure Diff Gate

| Requirement | Output | Disposition |
| --- | --- | --- |
| Rename local corpus folder | `data_input` exists with two files | PASS |
| Produce per-file sourceHash | SHA-256 in manifest | PASS |
| Produce normalizedPath | `data_input/116_2025_qh15_666020.docx`; `data_input/148_2025_qh15_675262.docx` | PASS |
| Preserve no-answer boundary | `ESCALATE_OR_ABSTAIN`, no text extraction | PASS |

## Finding-To-Governance Learning Disposition

Defect class: `RUNTIME_SIGNAL_GAP`

Learning lane: `RUNTIME_BEHAVIOR_LEARNING`

Disposition: `MACHINE_CHECK_CANDIDATE` - future runtime import should have a
checker that blocks answer/search readiness when records are only
`HASHED_ONLY` or `DEFERRED_DOCX_TEXT_EXTRACTION`.

Next control action: open a bounded T4 import/classification tranche for local
DOCX text extraction, domain field population, GC-047/GC-050 checks, and
sampling before chat runtime.

Runtime/provider/cost learning: `RUNTIME_BEHAVIOR_LEARNING`

Reason: this smoke test found the next runtime readiness boundary: hash-only
records are not answerable records.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this completion references a private local workspace file and a local
manifest path.

## Claim Boundary

This completion claims only local folder rename and hash-only import smoke test
success for two DOCX files.

It does not claim DOCX text extraction, semantic classification, search index
readiness, retrieval behavior, provider proof, legal advice correctness,
latest-law status, production readiness, hosted readiness, or public export.
