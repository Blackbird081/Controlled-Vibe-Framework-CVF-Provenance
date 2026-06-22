# ADIF-0007 - Gate Keyword In Exclusion Prose Triggers Wrong Evidence Class

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0007
title: Gate keyword in exclusion prose triggers wrong evidence class
defectCategory: GATE_TRIGGER_FRICTION
defectClass: PHASE_GATE_PLACEMENT_GAP
defectRole: NOT_APPLICABLE_WITH_REASON: this entry is a general pattern, not a single finding row
severity: MEDIUM
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (WORKER_MUST_NOT_COMMIT)
roles: dispatcher; worker
lifecyclePhases: pre-dispatch; pre-implementation
surfaceSelectors: N/A reasons, out-of-scope disclaimers, and boundary-prose sentences in any GC-018, work order, worker return, or completion review
detectionSignals: a scope-exclusion sentence uses a bare trigger word (e.g. "scan", "classification", "corpus", "readiness", "receipt", "provider call") that a keyword-based gate reads as a positive evidence-class claim rather than an exclusion
enforcementLevel: PARTIAL_CHECK
checkerBindings: governance/compat/check_corpus_scan_registry.py; governance/compat/check_finding_to_governance_learning.py (keyword-trap surfaces named in FPRC; not all trigger classes have a dedicated test asserting the false-positive itself)
promotionState: STANDARD_ADDED
supersedes: NONE
lastVerifiedCommit: 0fde5cf2
roadmapSeedId: ADIF-SEED-007
```

## Purpose

Record one observed defect pattern so an agent can recognize it before
writing a scope-exclusion sentence that contains a bare keyword-gate trigger
word.

## Scope / Applies To

Applies to N/A reasons, out-of-scope disclaimers, and boundary-prose
sentences in any GC-018, work order, worker return, or completion review.
Does not apply to runtime, provider, or public-sync behavior.

## Bad Example

> "no corpus scan or readiness classification required" - the bare words
> "scan", "corpus", "readiness", and "classification" force the corpus scan
> registry gate to demand Registry JSON/Markdown evidence that was never
> intended.

## Good Example

> "doc-only scope; file-system enumeration not used" - states the same
> exclusion without the trigger tokens.

## Canonical Sources

- `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
  (Boundary-Prose Trigger Discipline: known keyword trigger classes table
  and compliant-alternative phrasing table)

## Remediation

When declaring a scope exclusion, use the FPRC-compliant alternative
phrasing that avoids the literal trigger token. If a sentence must be
technical and cannot avoid a trigger word, place it in a section header or
summary-table row outside scanned prose body and cite the FPRC standard as
the reason.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T1 execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool |
| Target paths | this entry file |
| Allowed scope source | ADIF-T1 GC-018 baseline and paired work order |
| Before status evidence | file did not exist before this tranche |
| After status evidence | entry created with cited canonical evidence |
| Diff evidence | new-file creation in the ADIF-T1 checkpoint commit |
| Approval boundary | ADIF-T1 child scope only |
| Claim boundary | records an observed defect pattern only; no checker implementation |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t1-execution-2026-06-23` |
| Expected manifest | this entry, part of the ADIF-T1 eight-entry batch |
| Actual changed set | this entry |
| Manifest delta | MATCH |

## Claim Boundary

This entry records an observed defect pattern and points to the FPRC
standard that documents it. `enforcementLevel` is `PARTIAL_CHECK` because
several keyword-trap classes are caught by existing gates as a side effect
of their normal evidence checks, but no single checker exhaustively tests
every trigger-word class named in the FPRC table.
