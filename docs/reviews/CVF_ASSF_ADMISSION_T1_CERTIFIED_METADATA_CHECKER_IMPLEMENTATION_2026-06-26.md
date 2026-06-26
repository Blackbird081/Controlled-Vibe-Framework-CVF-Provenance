# CVF Review: ASSF Admission T1 Certified Metadata Checker Implementation

Memory class: FULL_RECORD

Status: COMPLETE

Date: 2026-06-26

docType: review

Batch ID: ASSF-CERTIFIED-METADATA-ADMISSION

## Purpose

Record implementation of the read-only ASSF certified metadata admission
checker and focused tests.

## Target / Source

Target checker: `governance/compat/check_assf_certified_metadata_admission.py`.
Target tests:
`governance/compat/test_check_assf_certified_metadata_admission.py`.

## Scope / Methodology

Created `check_assf_certified_metadata_admission.py`, created focused unit
tests, and kept the checker as a direct material gate.

## Findings / Position

The checker validates certified entries against UAT pass, review artifact
existence, generated index consistency, non-active status, metadata-only
resolver/loader boundary text, and adapter claim honesty fields. It does not
write any registry or generated index file.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| checker could become a mutator | implementation uses read-only JSON loads and existing drift validation |
| hook wiring could overreach | wiring adds only the direct checker command |
| tests could depend on repo artifacts | tests use temporary registry/index roots and temp review artifacts |

## Verification / Evidence

| Command | Result |
|---|---|
| `python -m unittest governance.compat.test_check_assf_certified_metadata_admission` | PASS - 6 tests |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |

## Decision / Disposition

T1 disposition: COMPLETE. Proceeded to T2 gate execution and read-model proof.

## Claim Boundary

T1 changes governance checker/test/hook surfaces only. It does not mutate ASSF
registry source, generated index data, resolver source, Web runtime, adapters,
provider/live proof, public-sync, or session state.
