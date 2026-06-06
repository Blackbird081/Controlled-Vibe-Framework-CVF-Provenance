# CVF GC-018 Continuation Candidate

## CCG-1 Corpus Completeness And Report Integrity Guard

Memory class: BASELINE_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-06-01

## Purpose

Authorize a bounded governance-hardening tranche that generalizes the legacy
scan failure into a reusable corpus-completeness control for any agent task
that reads, audits, compares, extracts, migrates, inventories, or reports from
an enumerable project source set.

## Scope / Target / Owner Boundary

Target contract: `cvf.corpusCompletenessReportIntegrity.ccg1.v1`.

Owner: CVF governance compatibility layer and agent workflow documentation.

Allowed change:

- add a general corpus-completeness and report-integrity standard;
- add `GC-047` operational guard;
- implement a repository checker and focused tests;
- wire the checker into autorun, local hooks, and documentation CI;
- route agent front doors and GC-018 authoring through the new protocol;
- correct the 2026-06-01 legacy failure audit's command-backed counts and
  continuity state.

Forbidden scope:

- no legacy concept absorption or implementation;
- no runtime provider, prompt, memory, route, or receipt behavior changes;
- no public-sync update;
- no claim that machine checks prove semantic understanding of every file.

## Source / Predecessor Evidence

- Operator authorization: 2026-06-01 instruction to implement a general guard
  for agent work performed on behalf of non-coder users.
- Failure audit:
  `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- Specialized standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Autorun standard:
  `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- Closure standard:
  `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Legacy audit records filesystem self-report failure | `EXISTS` | `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md` | Root cause and Gate 7 sections | `CVF_Important` | Legacy failure audit | ACCEPT |
| Specialized Gate 1 requires filesystem listing | `EXISTS` | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Gate 1 sub-rule | `FILESYSTEM_LISTING_REQUIRED` | Blind-spot standard | ACCEPT |
| Specialized Gate 7 requires cross-check | `EXISTS` | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Gate 7 sub-rule | `COMPLETENESS_CROSS_CHECK` | Blind-spot standard | ACCEPT |
| Autorun wrapper owns phase bundles | `EXISTS` | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `_common_commands` | Autorun wrapper | ACCEPT |
| Local hook chain owns local enforcement | `EXISTS` | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `HOOK_CHAINS` | Local hook chain | ACCEPT |
| Documentation workflow owns CI enforcement jobs | `EXISTS` | `.github/workflows/documentation-testing.yml` | workflow jobs | `knowledge-absorption-priority-guard` | Documentation workflow | ACCEPT |

## New Proposed Fields And Symbols

| Proposed item | Intended owner | Purpose | Runtime status now |
| --- | --- | --- | --- |
| `Corpus Completeness And Report Integrity` | corpus-derived governed artifact | Required evidence section | DOC_ONLY_NEW |
| `COMPLETE_VERIFIED` | corpus verdict vocabulary | Zero unresolved corpus items | DOC_ONLY_NEW |
| `COMPLETE_WITH_DECLARED_EXCLUSIONS` | corpus verdict vocabulary | Bounded result with visible exclusions | DOC_ONLY_NEW |
| `check_corpus_completeness_report_integrity.py` | governance compatibility layer | Machine evidence-shape checker | DOC_ONLY_NEW |

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED by explicit operator instruction.

Baseline: legacy absorption audit exposed a repeated omission failure that the
specialized prose standard did not hard-enforce.

Proposed tranche: add general `GC-047`, checker, tests, bindings, front-door
routing, and audit/continuity remediation.

## Evidence / Verification

Required before closure:

```powershell
python -m pytest governance/compat/test_check_corpus_completeness_report_integrity.py -q
python governance/compat/check_corpus_completeness_report_integrity.py --base fe29b4d6 --head HEAD --enforce
python governance/compat/check_guard_registry.py --enforce
python governance/compat/check_guard_authoring_standard.py --base fe29b4d6 --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. Public-sync requires a
separate authorized batch.

## Claim Boundary

This baseline authorizes repository governance enforcement and documentation
only. It does not authorize legacy concept implementation, provider calls,
runtime behavior changes, public publication, or claims of perfect semantic
understanding.

