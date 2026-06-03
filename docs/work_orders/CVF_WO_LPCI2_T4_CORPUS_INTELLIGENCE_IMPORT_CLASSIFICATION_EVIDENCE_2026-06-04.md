# CVF Work Order - LPCI2-T4 Corpus Intelligence Import Classification Evidence

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-04

executionBaseHead: `10e9eae2`

dispatchBaseHead: `10e9eae2`

closureBaseHead: `10e9eae2`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Execute the next bounded PolicyLocal tranche as Corpus Intelligence evidence,
not chatbot product implementation.

The task is to extract text locally from the two DOCX files currently under
`Policy_Local\data_input`, create machine-readable corpus records, populate
legal/policy classification fields with conservative evidence, and run the
corpus governance checks needed before any search or chat runtime can be
considered.

## Scope / Target / Owner Boundary

Target local workspace:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`

Target input folder:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input`

Owner boundary: Codex may execute orchestrator, worker, reviewer, and closer
roles for this bounded evidence tranche. If delegated to another worker, that
worker must not commit unless separately authorized by the operator.

This work order is not a product-build authorization. PolicyLocal remains a test
use case for proving CVF Corpus Intelligence as a reusable foundation
capability.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04 chat instruction: PolicyLocal is a test use case to prove Corpus Intelligence, not a production chatbot target now | ACCEPT |
| T4S smoke completion | `docs/reviews/CVF_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md` | ACCEPT |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT |
| Corpus Intelligence standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACCEPT |
| LPCI1 T1 corpus intake spec | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | ACCEPT |
| LPCI1 T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | ACCEPT |
| LPCI1 T4 retrieval boundary spec | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | ACCEPT |
| GC-051 registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| PolicyLocal has two hash-only DOCX input records | `docs/reviews/CVF_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md` | Evidence Trace Block | data_input/116_2025_QH15_666020.docx; data_input/148_2025_QH15_675262.docx | LPCI2-T4S completion | ACCEPT |
| Per-file SHA-256 sourceHash is required | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | Source Hash Policy | sourceHash | LPCI1 T1 intake | ACCEPT |
| normalizedPath is required | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | NR-05 normalizedPath Adoption | normalizedPath | LPCI1 T1 intake | ACCEPT |
| Legal/policy domain fields are required for real records | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | Gap-to-LPCI Productization Matrix | legalPolicy domain fields | LPCI1 T1 intake | ACCEPT |
| Jurisdiction unknown forces abstention boundary | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | Jurisdiction Taxonomy | jurisdiction | LPCI1 T2 classification | ACCEPT |
| answerClass must use canonical values | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | Response-Boundary Classes | answerClass | GC-050 structural standard | ACCEPT |
| Search/chat must not exceed answer boundary | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | Answer Assembly Rules | answerClass | LPCI1 T4 retrieval boundary | ACCEPT |
| GC-051 registry owns corpus registration | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | corpora entry | policylocal-production-corpus-dropzone | Corpus scan registry | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T4 action | Evidence |
| --- | --- | --- |
| Continue after T4S hash-only proof | Read T4S manifest and re-verify the two DOCX source hashes | local manifest plus completion review |
| Convert hash-only records into corpus evidence | Extract DOCX text locally and produce corpus records | generated corpus records JSON |
| Populate legal/policy fields | Fill fields only when supported by source text or conservative metadata; otherwise keep `unknown` and abstain | classification ledger |
| Preserve Corpus Intelligence boundary | Do not build search/chat/runtime/provider path | completion claim boundary |
| Feed learning and scan loops | Update GC-051 registry and record any reusable checker/template findings | registry plus Finding-To-Governance block |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex unless reassigned |
| Implementer | Codex or explicitly delegated worker |
| Reviewer | Codex reviewer role after implementation |
| Closer | Codex closer role after gates pass |
| Worker commit boundary | WORKER_MUST_NOT_COMMIT unless operator explicitly promotes the worker to closer |

## Worker Autonomy / No-Question Rule

The assigned agent must fix allowed-scope gate failures without asking the
operator. Ask only if a fix would exceed Allowed Scope, touch forbidden paths,
consume provider quota, change the claim boundary, require legal interpretation
beyond source extraction/classification, or start runtime/product work.

The agent must stop instead of improvising if DOCX extraction cannot be done
with local deterministic tooling. In that case, close as `BLOCKED` with a
diagnostic and do not infer legal content from filenames.

## Allowed Scope

- Add or update local scripts under
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts`.
- Read local input files under `Policy_Local\data_input`.
- Generate local evidence under `Policy_Local\data\generated`.
- Generate a local completion note under `Policy_Local`.
- Update repo governance docs for this tranche:
  - `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md`
  - `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
  - `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
  - `CVF_SESSION_MEMORY.md`
  - `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  - `AGENT_HANDOFF_V15_2026-05-29.md`
- Run local Node/Python checks and CVF governance gates.

## Forbidden Scope

- Do not build a chatbot, UI runtime, API route, database layer, vector store,
  embedding pipeline, provider call, hosted deployment, or public-sync batch.
- Do not claim legal advice correctness, latest-law status, production
  readiness, or public release readiness.
- Do not infer statute meaning from filenames or model memory.
- Do not bypass sourceHash, normalizedPath, domain field, or answerClass
  evidence.
- Do not treat this test use case as higher priority than unfinished
  Memory/Knowledge legacy absorption.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/reviews/CVF_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md`
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md`
- `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md`
- `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md`

## Pre-Flight Checks

Before implementation, record:

| Check | Required action |
| --- | --- |
| Base head | `git rev-parse --short HEAD` and compare to `dispatchBaseHead` |
| Worktree scope | `git status --short --branch` |
| Local input folder | list `Policy_Local\data_input` and confirm the two DOCX files |
| T4S manifest | read `Policy_Local\data\generated\policylocal-data-input-manifest.json` |
| Dependency release | confirm T4S is `CLOSED_PASS_BOUNDED` |

## Write Ownership

Owned external workspace paths:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md`

Owned repo paths:

- `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Do not touch runtime source, public-sync, provider config, or unrelated legacy
absorption files in this tranche.

## Execution Plan

1. Run pre-flight checks and compare local files to the T4S manifest.
2. Add or update deterministic local DOCX extraction tooling.
3. Extract text locally and compute `textHash`.
4. Build corpus records plus Classification Ledger.
5. Update GC-051 with the new corpus state and findings.
6. Write completion evidence and local workspace note.
7. Run required gates.
8. Stop for reviewer/closer disposition without worker commit if delegated.

## Implementation Requirements

1. Recompute SHA-256 for both DOCX files and compare with T4S manifest.
2. Extract DOCX text locally with deterministic tooling.
3. Write a generated corpus records file with at least:
   - `sourcePath`
   - `normalizedPath`
   - `sourceHash`
   - `sourceHashAlgorithm`
   - `byteLength`
   - `processingStatus`
   - `extractionStatus`
   - `textLength`
   - `textHash`
   - `documentType`
   - `jurisdiction`
   - `authorityLevel`
   - `issuingBody`
   - `effectiveDate`
   - `status`
   - `sourceAuthority`
   - `rawDisposition`
   - `dispositionAlias`
   - `answerClass`
   - `evidencePointer`
4. Write a Classification Ledger compatible with GC-050.
5. Keep records at `ESCALATE_OR_ABSTAIN` unless all required fields and source
   evidence justify a stricter answer class under LPCI1-T2/T4.
6. Update GC-051 registry with the new status and findings.
7. Close with a review packet containing Corpus Completeness, Corpus
   Intelligence Classification, Source Verification, Finding-To-Governance,
   Public Export Disposition, and Claim Boundary sections.

## Required Outputs

| Output | Path |
| --- | --- |
| Generated corpus records | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json` |
| Extraction/classification report | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` |
| Completion review | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` |
| Registry update | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |

## Required Gates

Run from the provenance repo unless the command path says Policy_Local:

```powershell
node scripts/policylocal-import-smoke.mjs
```

```powershell
node scripts/validate-cvf-prototype-schema.mjs
```

```powershell
python governance/compat/check_corpus_scan_registry.py --base 10e9eae2 --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base 10e9eae2 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 10e9eae2 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 10e9eae2 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 10e9eae2 --head HEAD
```

## Review Gate

Reviewer must verify:

- both DOCX files have sourceHash and textHash evidence;
- domain fields are source-backed or explicitly `unknown`;
- no answerClass exceeds the evidence boundary;
- GC-047 and GC-050 evidence blocks are present;
- no search/chat/runtime/provider/product work was added.

## Return Conditions

Return to orchestrator without implementation closure if:

- deterministic DOCX extraction fails;
- local files drift and hashes cannot be reconciled;
- domain fields would require legal interpretation rather than source-backed
  classification;
- required gates fail outside Allowed Scope;
- implementation would require runtime/product work.

## Operator Checkpoint

Operator checkpoint is required only before any later move from evidence work
to runtime/product implementation. No checkpoint is required for allowed-scope
repairs inside this T4 evidence tranche.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Source hashes reverified | both DOCX SHA-256 values match or drift is documented |
| Text extracted locally | corpus records include textLength and textHash for each readable DOCX |
| Domain fields populated conservatively | unsupported fields stay `unknown` with abstain boundary |
| Classification ledger present | GC-050 structural fields exist for each source file |
| Runtime boundary preserved | no search/chat/provider/product readiness claim |
| Learning promoted | reusable finding candidates are classified instead of blamed on worker |

## Closure Checklist

- [x] Work order has source verification.
- [x] Work order has roadmap trace.
- [x] Work order has Worker Autonomy / No-Question Rule.
- [x] Work order forbids product chatbot implementation.
- [x] Work order keeps Memory/Knowledge legacy absorption as a higher-level
  readiness dependency.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private local workspace files and a private
operator corpus.

## Claim Boundary

This work order authorizes only local Corpus Intelligence import and
classification evidence for the two current PolicyLocal DOCX files.

It does not authorize chatbot product implementation, search runtime, provider
calls, hosted deployment, public export, legal advice correctness, latest-law
status, production readiness, or any claim that legacy Memory/Knowledge
absorption is complete.
