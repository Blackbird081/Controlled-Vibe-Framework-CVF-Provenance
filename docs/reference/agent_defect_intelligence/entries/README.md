# CVF ADIF Entries - Front Door

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-06-23

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This front door
points to the compact per-entry source files in this folder; it does not
itself enumerate, map, or project CVF state as a generated aggregate.

**Applies to:** any agent or operator reading or extending the ADIF seed
dictionary.

## Purpose

This folder holds one compact source file per ADIF entry, following
`docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`.
ADIF-T2 closed the read-only task/role/phase resolver at
`governance/compat/run_adif_defect_resolver.py`; it discovers any
`CVF_ADIF-*.md` file in this folder by filename glob, so no separate
registry edit is required when adding a new entry beyond this table.

## Current Entries

| File | defectId | defectCategory | enforcementLevel |
|---|---|---|---|
| `CVF_ADIF-0001.md` | ADIF-0001 | SOURCE_FIDELITY | MACHINE_CHECKED |
| `CVF_ADIF-0002.md` | ADIF-0002 | AUTHORITY_BOUNDARY | MACHINE_CHECKED |
| `CVF_ADIF-0003.md` | ADIF-0003 | CLOSURE_EVIDENCE | MACHINE_CHECKED |
| `CVF_ADIF-0004.md` | ADIF-0004 | STATE_CONTINUITY | MACHINE_CHECKED |
| `CVF_ADIF-0005.md` | ADIF-0005 | CLOSURE_EVIDENCE | MACHINE_CHECKED |
| `CVF_ADIF-0006.md` | ADIF-0006 | SOURCE_FIDELITY | MACHINE_CHECKED |
| `CVF_ADIF-0007.md` | ADIF-0007 | GATE_TRIGGER_FRICTION | PARTIAL_CHECK |
| `CVF_ADIF-0008.md` | ADIF-0008 | AUTHORITY_BOUNDARY | MACHINE_CHECKED |
| `CVF_ADIF-0009.md` | ADIF-0009 | GATE_TRIGGER_FRICTION | PARTIAL_CHECK |
| `CVF_ADIF-0010.md` | ADIF-0010 | GATE_TRIGGER_FRICTION | MACHINE_CHECKED |
| `CVF_ADIF-0011.md` | ADIF-0011 | GATE_TRIGGER_FRICTION | MACHINE_CHECKED |
| `CVF_ADIF-0012.md` | ADIF-0012 | CLOSURE_EVIDENCE | MACHINE_CHECKED |
| `CVF_ADIF-0013.md` | ADIF-0013 | STATE_CONTINUITY | MACHINE_CHECKED |
| `CVF_ADIF-0014.md` | ADIF-0014 | SOURCE_FIDELITY | GUIDANCE_ONLY |
| `CVF_ADIF-0015.md` | ADIF-0015 | AUTHORITY_BOUNDARY | GUIDANCE_ONLY |
| `CVF_ADIF-0016.md` | ADIF-0016 | GATE_TRIGGER_FRICTION | GUIDANCE_ONLY |
| `CVF_ADIF-0017.md` | ADIF-0017 | SCOPE_AND_OWNERSHIP | PARTIAL_CHECK |
| `CVF_ADIF-0018.md` | ADIF-0018 | GATE_TRIGGER_FRICTION | GUIDANCE_ONLY |
| `CVF_ADIF-0019.md` | ADIF-0019 | CLOSURE_EVIDENCE | PARTIAL_CHECK |
| `CVF_ADIF-0020.md` | ADIF-0020 | GATE_TRIGGER_FRICTION | MACHINE_CHECKED |

## Claim Boundary

This front door is a navigation pointer only. It does not implement a
resolver, generator, checker, or hook, and it does not claim defect
comprehension or prevention effectiveness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance reference front door. No public-sync repository
work or public catalog claim is authorized.
