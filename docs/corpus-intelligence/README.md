# docs/corpus-intelligence/

Memory class: POINTER_RECORD

Status: ACTIVE

docType: policy

## Purpose

This folder is the **Corpus Intelligence Index** for CVF and all CVF-governed
projects.

## Scope / Target / Owner Boundary

Applies to: all agents and operators working on any CVF-governed project.
Owner: CVF governance control chain.

## Rule

Any agent must read `CVF_CORPUS_SCAN_REGISTRY.json` before scanning any corpus.

## Allowed / Forbidden / Requirements

Allowed: reading registry, updating registry after scan, adding new entries.
Forbidden: scanning a corpus without checking the registry first; re-scanning a
`SCANNED` corpus without operator authorization.
Required: update registry and findings folder after every corpus scan.

## Exceptions

None. All corpus types require a registry entry.

## Enforcement Surface

`governance/compat/check_corpus_scan_registry.py` — wired into autorun and pre-commit.

## Related Artifacts

Standard: `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
Guard: `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

## Claim Boundary

This README claims: folder structure, navigation, and agent startup rule.
Does not claim: semantic correctness of registry entries; production readiness.

---

This folder is the **Corpus Intelligence Index** for CVF and all CVF-governed
projects. It is the single place any agent must consult before scanning,
classifying, or absorbing knowledge from any corpus — legacy folders, project
source trees, policy documents, company documentation, or external sources.

## Why this folder exists

Without a shared registry, agents re-scan the same corpus, miss prior findings,
and cannot detect blind spots from previous waves. This folder eliminates that
problem by making corpus scan state **machine-readable, searchable, and
cross-referenced** across all agents and sessions.

## Contents

| File | Purpose |
| --- | --- |
| `README.md` | This file — folder purpose and navigation |
| `CVF_CORPUS_SCAN_REGISTRY.json` | Machine-readable registry of all scanned corpora |
| `CVF_CORPUS_SCAN_REGISTRY.md` | Human-readable companion and finding index |
| `findings/` | Per-corpus finding packets (named by corpus slug) |
| `manifests/` | Per-corpus filesystem manifests (JSON, with hash) |

## Agent startup rule

**Before scanning any corpus, read `CVF_CORPUS_SCAN_REGISTRY.json` first.**

If the corpus is already listed with status `SCANNED` or `PARTIALLY_SCANNED`,
inherit the prior scan state and findings instead of starting from zero.

See: `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
Guard: `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`
Checker: `governance/compat/check_corpus_scan_registry.py`
