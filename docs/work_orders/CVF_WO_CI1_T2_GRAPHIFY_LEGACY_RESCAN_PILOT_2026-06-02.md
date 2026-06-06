# CVF Work Order - CI1-T2 Graphify Legacy Rescan Pilot

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

## Purpose

Apply the CI1-T1 readiness packet template to the Graphify legacy corpus
family (`.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`,
5 files) and produce a filled readiness packet, corpus intelligence
classification ledger, and completion review. This is the first real corpus
execution under the new CI1 workflow.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 direction: CI1-T2 on Graphify | ACCEPT |
| CI1-T2 GC-018 | `docs/baselines/CVF_GC018_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_2026-06-02.md` | ACCEPT |
| CI1 parent GC-018 | `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md` | ACCEPT |
| CI1-T1 template | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | ACCEPT |
| CI1 roadmap | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | ACCEPT |
| GC-047 standard | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | ACCEPT |
| GC-048 standard | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | ACCEPT |
| GC-050 standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACCEPT |
| Search/filter standard | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Dispatch CI1-T2 after GC-018 exists | no corpus reading |
| Worker | Read all 5 Graphify files; fill full CI1-T1 packet template; produce completion review | no files outside scope; no commit/push |
| Reviewer | Verify packet is filled, gates pass, claim boundary respected | reject incomplete ledger |

## Scope

Allowed scope:

- read all 5 files under `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`;
- produce `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` (filled packet);
- produce `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md`;
- update `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  CI1-T2 row status only;
- run required governance gates and repair allowed-scope gate failures.

Forbidden scope:

- reading any file outside `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`;
- modifying runtime TypeScript, Python checker code, hook chain, or guard files;
- implementing a vector database, indexer, chatbot UI, or retrieval route;
- public-sync, push, or commit;
- claiming semantic correctness, production readiness, hosted readiness, or public readiness.

Risk ceiling: R1 read-only legacy scan.

## Required First Reads

1. `docs/baselines/CVF_GC018_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_2026-06-02.md`
2. `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`
3. `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
4. `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`
5. `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
6. `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
7. All 5 corpus files (in order):
   - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPHIFY_CLI_COMMAND_SPEC.md`
   - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_DATA_MODEL.md`
   - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_GUARD_SPEC.md`
   - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_LAYER_SPEC.md`
   - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/Thong_tin.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD          # must be 662b673b or later
git status --short                  # must be clean
python governance/compat/check_work_order_dispatch_quality.py --base 662b673b --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 662b673b --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Disposition |
| --- | --- | --- | --- | --- |
| Graphify folder exists | N/A — filesystem path, not a source file | filesystem `ls` before GC-018 | `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` (5 files) | ACCEPT |
| CI1-T1 template exists | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | full document | `CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | ACCEPT |
| GC-047 checker exists | `governance/compat/check_corpus_completeness_report_integrity.py` | `def main` | `main` | ACCEPT |
| GC-048 checker exists | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | `def main` | `main` | ACCEPT |
| GC-050 checker exists | `governance/compat/check_corpus_intelligence_classification.py` | `def main` | `main` | ACCEPT |
| baseHead at dispatch | N/A — git commit reference | `git rev-parse --short HEAD` | `662b673b` | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Apply CI1-T1 template to Graphify corpus | Scope + Execution Plan | filled readiness packet | GC-047/048/050 gates | READY |
| Filesystem-backed manifest (all 5 files READ) | Execution Plan §3.2 | manifest + ledger in packet | GC-047 gate PASS | READY |
| GC-048 knowledge-map reconciliation | Execution Plan §3.3 | semantic region ledger | GC-048 gate PASS | READY |
| GC-050 classification ledger | Execution Plan §3.5 | classification ledger | GC-050 gate PASS | READY |
| Adversarial sampling (≥5 rows) | Execution Plan §3.6 | sampling table | reviewer check | READY |
| Negative search evidence | Execution Plan §3.4 | zero-result table | reviewer check | READY |
| Completion review | Scope | completion review | dispatch quality gate | READY |

## Worker Autonomy / No-Question Rule

Proceed autonomously with reading the 5 corpus files, filling the readiness
packet template, running gates, and repairing allowed-scope gate failures.

Ask only for:

- scope expansion beyond the 5 Graphify files;
- forbidden path edits;
- live/provider proof;
- public-sync, push, or commit;
- secrets/quota use;
- destructive actions.

## Pending Artifact Evidence Finality

Do not commit. Record `git status --short` in the completion review.
Do not cite committed-only or empty ranges as proof for pending files.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | No (produced during execution) | filled readiness packet — all 15 CI1-T1 template sections |
| `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md` | No (produced during execution) | completion review |
| `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | Optional update | CI1-T2 row status only |

## Write Ownership

Owned:

- `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
- `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md`
- `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` (CI1-T2 row only)

Forbidden:

- runtime TypeScript or Python source;
- governance checker, hook, or guard files;
- any file outside `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` for reading;
- public-sync clone;
- any file outside the owned list above for writing.

Write mode: additive documentation only.

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `.private_reference/legacy/CVF_Important/` files outside `Knowledge Base_Graphify/` | out of T2 scope |
| `.private_reference/legacy/CVF Edit/`, `CVF ADD/`, `CVF_Restructure/`, `CVF 16.5/`, `CVF 17.05/`, `CVF 25.05/`, `CVF 28.05/` | other legacy families — separate tranches |
| `App onboarding/` | out of scope |
| runtime TypeScript (`*.ts`, `*.tsx`) | no runtime edits authorized |
| Python checker/guard scripts | no guard edits authorized |
| public-sync clone | out of scope |

## Forbidden Filesystem State At Dispatch

| Forbidden path | State at dispatch (baseHead `662b673b`) | Outcome |
| --- | --- | --- |
| Files outside `Knowledge Base_Graphify/` folder | no pending reads or writes outside folder | COMPLIANT |
| Public-sync clone changes | no pending public-sync export | COMPLIANT |

## Execution Plan

### §3.1 Capture baseHead

```powershell
git rev-parse --short HEAD
```

Record the output. This is `baseHead` for all gate commands.

### §3.2 Filesystem Discovery + GC-047 Manifest

Enumerate the corpus using:

```powershell
rg --files --hidden --no-ignore ".private_reference/legacy/CVF_Important/Knowledge Base_Graphify/"
```

Expected output: 5 files. Record each file in the processing ledger with
status `READ`. Compute a manifest hash over the sorted file list.

Fill CI1-T1 template §2 (Source Corpus Evidence):

- Corpus Completeness And Report Integrity block;
- filesystem discovery index;
- processing ledger (all 5 files with READ status);
- manifest hash.

GC-047 compliance requirements for the filled packet:

- `Corpus task class:` must be present;
- `Reconciliation:` must use `manifest=5 ledger_terminal=5 exclusions=0 unresolved=0` format;
- `Unresolved files: 0`;
- `Corpus verdict: COMPLETE_VERIFIED`.

### §3.3 Read All 5 Files + GC-048 Knowledge-Map Block

Read each file fully. For each file, record:

- what knowledge domain it covers (graph data model, CLI spec, guard spec, layer spec, or info);
- which CVF owner surfaces it relates to;
- what semantic region it belongs to.

Fill CI1-T1 template §3 (Knowledge-Map Reconciliation):

- Knowledge System Reconciliation block;
- semantic region ledger (one row per file);
- region reconciliation (`assets=5; mapped=N; deferred=D; unmapped=0`).

GC-048 compliance requirements:

- `Enumeration safety:` must cite `rg --files --hidden --no-ignore`;
- `Region reconciliation:` must use `assets=N; mapped=N; deferred=N; unmapped=N` format;
- `Knowledge-map verdict:` must be `RECONCILED_VERIFIED` or `RECONCILED_WITH_DECLARED_GAPS`.

### §3.4 Fill Template §4 + §5: Search/Filter Readiness + Negative Search

Fill CI1-T1 template §4 (Corpus Search And Filter Readiness):

- common facet schema;
- legacy corpus domain extensions.

Fill CI1-T1 template §5 (Negative Search Evidence):

- for each file, record any concepts mentioned but not implemented or absent;
- zero-result terms table.

### §3.5 GC-050 Classification Ledger

For each file, complete one row in the GC-050 classification ledger:

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer | answerClass | domainFields |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use only allowed values from:

- `processingStatus`: `READ_DEEP`, `READ_SURFACE`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`
- `disposition`: `ACCEPT`, `DEFER`, `REJECT`, `ESCALATE`
- `answerClass`: `DIRECT_CITED_ANSWER`, `SUMMARY_WITH_SOURCE`, `PROCEDURAL_GUIDANCE`, `ESCALATE_OR_ABSTAIN`

Fill CI1-T1 template §9 (Corpus Intelligence Classification block):

- `Classification task class:` (use `LEGACY_CORPUS_ABSORPTION`)
- `Response Boundary:` on a single line (GC-050 checker is single-line)
- `Classification verdict:` (`CLASSIFIED_STRUCTURAL_PASS` or `CLASSIFIED_WITH_GAPS`)

### §3.6 Fill Templates §6–§8: Derived Trace, Query Receipt, Adversarial Sampling

Fill CI1-T1 template §6 (Derived Trace): manifest → map → classification → retrieval trace.

Fill CI1-T1 template §7 (Query Receipt Model): minimum 1 sample receipt.

Fill CI1-T1 template §8 (Adversarial Sampling Plan): minimum 5 rows across
accepted, deferred, rejected, and zero-result categories.

### §3.7 Fill Templates §10–§15: Disposition Matrix, Gate Commands, Summary, Claim Boundary

Fill the remaining CI1-T1 template sections:

- §10 Disposition Matrix;
- §11 Gate Commands (with actual `baseHead` substituted);
- §12 Final Readiness Summary (gate evidence table);
- §13 Public Export Disposition (`DEFERRED_PRIVATE_ONLY`);
- §14 Finding-To-Governance Learning Disposition;
- §15 Claim / Final / Verification Boundary.

### §3.8 Produce Completion Review

Create `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md`
with:

- Scope / Target / Owner Boundary;
- Target / Source;
- Source Verification Block;
- Roadmap-To-Work-Order Trace Matrix;
- Gate Evidence table;
- Working Tree Status At Handoff (`git status --short`);
- Acceptance Criteria Check;
- Finding-To-Governance Learning Disposition (with `Learning lane:`, `Disposition:`, `N/A_WITH_REASON` for runtime/provider/cost);
- Corpus Completeness And Report Integrity block (fill with actual values, not N/A — this is a real scan);
- Knowledge System Reconciliation block (fill with actual values);
- Corpus Intelligence Classification block;
- Findings / Position;
- Risk / Corrective Action;
- Claim / Final / Verification Boundary.

**Known pitfall from CI1-T1:** the GC-047/048 blocks in the completion
review must use real numeric values (manifest=5, ledger_terminal=5, etc.),
not N/A, because CI1-T2 is a real corpus scan. The `Enumeration safety:`
field must cite `rg --files --hidden --no-ignore`. The `Region reconciliation:`
must use `assets=N; mapped=N; deferred=N; unmapped=N` format.

### §3.9 Run Required Gates

```powershell
python governance/compat/check_corpus_completeness_report_integrity.py --base 662b673b --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 662b673b --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 662b673b --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 662b673b --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 662b673b --head HEAD --enforce
python governance/compat/check_core_guard_self_protection.py --enforce
python governance/compat/check_forbidden_filesystem_state.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 662b673b --head HEAD
```

Repair all allowed-scope gate failures before returning to orchestrator.
Pre-closure autorun will expect uncommitted files — record the expected
FAIL reason in the completion review.

## Evidence Requirements

- `git status --short` recorded in completion review;
- all gate commands run and results recorded;
- manifest hash recorded in packet (from `rg --files` output);
- processing ledger shows all 5 files with READ status;
- GC-050 ledger has one row per file;
- adversarial sampling table has ≥5 rows.

## Acceptance Criteria

- [ ] All 5 Graphify files read and recorded with READ status in ledger
- [ ] Corpus manifest hash present and derived from `rg --files --hidden --no-ignore`
- [ ] GC-047 block in packet: `manifest=5 ledger_terminal=5 exclusions=0 unresolved=0`, `Corpus verdict: COMPLETE_VERIFIED`
- [ ] GC-048 block in packet: `assets=5; mapped=N; deferred=D; unmapped=0`, valid `Knowledge-map verdict:`
- [ ] GC-050 classification ledger: 5 rows with valid enum values
- [ ] Adversarial sampling: ≥5 rows across accepted/deferred/rejected/zero-result categories
- [ ] Negative search evidence: zero-result terms table present
- [ ] Completion review exists with all required sections
- [ ] GC-047/048/050 gates PASS on completion review
- [ ] Worker did not commit, push, or touch forbidden paths
- [ ] No semantic correctness, production readiness, or public readiness claim

## Closure Checklist

- [ ] Readiness packet produced with all 15 CI1-T1 template sections filled
- [ ] Completion review produced
- [ ] All gates run and results recorded
- [ ] CI1 roadmap CI1-T2 row updated to `COMPLETE_PENDING_REVIEW`
- [ ] Working tree status recorded in completion review
- [ ] Worker did not commit

Return pending implementation and review packet for orchestrator/reviewer.

## Current Runtime Freshness Verification

CI1-T2 is a documentation-only corpus scan. No runtime implementation is
claimed or required. The absence claims in this work order (no runtime
indexing, no vector database, no LPCI implementation) are scope boundary
statements, not claims about the current state of CVF runtime source.

Verified at baseHead `662b673b`:

- `runtimeExecutionAuthorized: false` — CI1-T2 is R1 read-only corpus scan
- No new runtime TypeScript files are produced by CI1-T2
- No governance checker or guard scripts are modified

## Review Gate

CI1-T2 may be returned for orchestrator/reviewer review only after:

- the readiness packet exists at `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` with all 15 CI1-T1 template sections filled;
- the completion review exists with all required structural sections;
- GC-047, GC-048, and GC-050 gates PASS on both the packet and the completion review;
- the GC-047 manifest records all 5 Graphify files with READ status;
- no forbidden paths have been touched.

## Return-To-Orchestrator Conditions

Return if T2 requires:

- reading corpus files outside the Graphify folder;
- changing guard/checker code;
- modifying runtime source;
- touching public-sync;
- making production readiness claims;
- consuming secrets or quota.

## Operator Checkpoint

Operator confirmed Graphify as the CI1-T2 pilot corpus on 2026-06-02.
This is a small (5-file), well-scoped corpus already referenced in KGR1.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Public-sync boundary: no CI1-T2 artifacts are to be copied to the
public-sync remote until a separate governed public readiness review
authorizes it.

Reason: CI1-T2 reads private legacy corpus. No public-sync remote, public
repository commit, public artifact path, hosted proof, or public README
claim is included.

## Corpus Intelligence Classification

- Classification task class: LEGACY_CORPUS_ABSORPTION
- Source corpus evidence: `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` — 5 files, filesystem-confirmed at dispatch
- Knowledge map evidence: to be produced during CI1-T2 execution; not claimed at dispatch
- Classification ledger: to be produced during CI1-T2 execution; not claimed at dispatch
- Legal/policy corpus: NO
- Domain fields: N/A — knowledge graph specification corpus, not legal/policy
- Response Boundary: DIRECT_CITED_ANSWER | SUMMARY_WITH_SOURCE | PROCEDURAL_GUIDANCE | ESCALATE_OR_ABSTAIN (this work order answers structural dispatch queries; full Graphify content classification belongs in the worker-produced packet)
- Adversarial sampling plan: to be produced during CI1-T2 execution
- Classification verdict: CLASSIFIED_STRUCTURAL_PASS (dispatch-level only; full classification to be produced by worker)

### Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer | answerClass | domainFields |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPHIFY_CLI_COMMAND_SPEC.md` | DEFERRED | KNOWLEDGE_GRAPH | PRIVATE_PROVENANCE | DEFER | to be read by worker | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_DATA_MODEL.md` | DEFERRED | KNOWLEDGE_GRAPH | PRIVATE_PROVENANCE | DEFER | to be read by worker | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_GUARD_SPEC.md` | DEFERRED | KNOWLEDGE_GRAPH | PRIVATE_PROVENANCE | DEFER | to be read by worker | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_LAYER_SPEC.md` | DEFERRED | KNOWLEDGE_GRAPH | PRIVATE_PROVENANCE | DEFER | to be read by worker | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/Thong_tin.md` | DEFERRED | KNOWLEDGE_GRAPH | PRIVATE_PROVENANCE | DEFER | to be read by worker | SUMMARY_WITH_SOURCE | N/A |

## Claim Boundary

CI1-T2 claims:

- bounded corpus intelligence readiness evidence for the 5-file Graphify
  legacy family;
- GC-047 complete verified scan;
- GC-048 knowledge-map reconciliation;
- GC-050 classification ledger for all 5 files.

CI1-T2 does NOT claim:

- semantic correctness of any classification;
- runtime retrieval quality;
- LPCI implementation;
- production, hosted, or public readiness;
- coverage of any other legacy family.
