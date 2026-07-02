# CVF MSEA-R7 MinerU Receipt Schema Contract Draft Worker Return

Memory class: governed-worker-return

Status: COMPLETE_PENDING_REVIEW

docType: review

Date: 2026-07-02

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`

Worker: no-commit worker role

dispatchBaseHead: `ce48461e`

executionBaseHead: `d7b0bc96`

closureBaseHead: WORKER_MUST_NOT_SET

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

sourceAuthority: `docs/baselines/CVF_GC018_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`

## Purpose

Draft a CVF-owned MinerU receipt schema contract from accepted MSEA-T2/R5/R6
owner surfaces and the pinned MinerU `output_files.md` evidence, enriching
MSEA-T2's receipt vocabulary with concrete artifact-family and field-family
language while preserving all runtime, quality, truth, downstream-use, and
implementation boundaries.

## Scope / Methodology

Scope: read the required first-read sources including MSEA-T2's receipt
advisory and MSEA-R5/R6's accepted evidence, verify the pinned source mirror
commit has not drifted, re-read `docs/en/reference/output_files.md` at the
exact anchors already source-verified in the work order's Source
Verification Block, draft the receipt schema contract reference with all
required sections, run the required gates, and leave changes uncommitted.

Method: read `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
session state, `AGENT_HANDOFF_V32_2026-07-02.md`, guard orientation,
literal-format gotchas, this work order, the paired GC-018 baseline, the
external absorption front door/chain map/core standard, the source mirror
index, MSEA-R6's route decision matrix and worker return, MSEA-R5's owner
delta and worker return, and MSEA-T2's full document-extraction advisory;
verify `git -C .private_reference/source_mirrors/opendatalab__MinerU
rev-parse HEAD` matches the pinned commit; re-confirm the exact line anchors
in `output_files.md` already cited in the work order's Source Verification
Block; adapt upstream artifact/field vocabulary into CVF-owned contract
language without copying upstream sample JSON; run the required verification
commands.

## Findings / Position

Source mirror verification confirms no drift: `git -C
.private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD`
returns `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, matching both the work
order's expected commit and the pinned commit already reconciled in
MSEA-R4/R5. No `BLOCKED_WITH_REASON` condition applies.

Re-reading `docs/en/reference/output_files.md` at the exact anchors cited in
the work order's Source Verification Block (lines 17, 35, 62, 109, 292, 396,
730-742 for artifact families; lines 129-186, 292-329, 402-426, 474-548 for
block-type and field vocabulary) confirms every cited fact: the file
documents seven distinct output-artifact families (layout debug PDF, span
debug PDF, raw model-inference JSON, intermediate hierarchical JSON,
flattened content-list JSON, a newer development-stage content-list-v2 JSON,
and the primary Markdown output), a block-type taxonomy spanning
table/image/chart/text/title/list/equation with caption/footnote/body
sub-parts, and two structurally different backend variants (pipeline vs.
VLM) for the raw model-inference and intermediate artifacts.

MSEA-T2's existing Receipt Advisory table already names abstract field
families ("source file identity", "parser/backend identity", "artifact
manifest", "quality status", "downstream-use status", "source pointers").
This draft's Field Family Map maps each of those abstract rows onto concrete
upstream field names (`page_idx`, `bbox`, `type`, `text_level`, `sub_type`,
`_backend`, `_version_name`, and the caption/footnote field families) with
traceable anchors, without weakening or contradicting any existing MSEA-T2
claim boundary. `MSEA-CC-4`'s existing "defer until CVF owns schema fields"
disposition is preserved verbatim - this draft is the preparatory groundwork
that disposition anticipated, not a trigger to change it.

The Backend Variant Boundary section captures a concrete delta beyond what
MSEA-R5 recorded: the raw model-inference artifact has an entirely different
shape between backends (pipeline: flat per-block list with `cls_id`/`label`;
VLM: two-level page-then-block nested list with `angle`/`content`), and the
VLM backend adds `code`/`algorithm` block types and a broader discarded-block
set not present in the pipeline shape documented in this section of the
reference. A future CVF receipt schema must record which backend produced
an artifact before assuming a field shape.

No prior MSEA-T2/R5/R6 conclusion is contradicted or reopened. This draft
enriches MSEA-T2's owner surface only.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| literalTokensReviewed | Required-heading list including git-status, changed-files, command-evidence, and no-commit-statement sections; both unresolved-placeholder marker strings the worker-return quality gate rejects; the self-declare, responds-to, and dispatch-work-order marker lines; the read-ahead, Agent Operation Trace, and Delta block required field sets; External Absorption Core required fields; required conversion lane tokens (all 6, including candidates unchanged from prior tranches); required overlap disposition tokens and the real-table requirement for the Overlap And Novelty Classification heading; the corpus-completeness safe-enumeration phrasing rule; the compact rescan-verdict shape for a genuinely non-rescan single-source tranche; the worker-experience retrospective structured/NA token pair |
| gateRunPurpose | Confirmation evidence recorded after the checker source and its literal tokens were already read, ahead of drafting this worker return, carrying forward the exact fix patterns already applied in the accepted MSEA-R4/R5 worker returns. |
| claimBoundary | Read-ahead evidence for this worker-return artifact only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Contract Draft Requirements Coverage

| Required section | Present in `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` |
| --- | --- |
| Purpose / Scope / Boundary | Yes - `## Purpose`, `## Scope / Boundary` |
| Source Authority | Yes - `## Source Authority` citing MSEA-T2/R5/R6 and the pinned mirror |
| Receipt Artifact Family Map | Yes - `## Receipt Artifact Family Map`, 7 artifact families with upstream anchors |
| Field Family Map | Yes - `## Field Family Map`, 10 field families |
| Backend Variant Boundary | Yes - `## Backend Variant Boundary`, pipeline vs. VLM structural differences |
| Downstream Use Boundary | Yes - `## Downstream Use Boundary`, restates MSEA-T2's RAG-handoff gate |
| Future Checker Readiness | Yes - `## Future Checker Readiness Note`, `MSEA-CC-4` disposition preserved |
| Claim Boundary | Yes - `## Claim Boundary` and `## Explicit Non-Claims` |

## Risk / Corrective Action

No risk identified inside allowed scope. All required gates pass (see
Command Evidence). No MinerU install, parser execution, OCR/VLM/hybrid
execution, API/router/Gradio service, Docker run, model download,
provider/live proof, OpenAI-compatible endpoint call, S3 connection,
credential storage, RAG index write, source import, checker implementation,
package activation, public-sync, Web/MCP/model-router/action-authority,
automatic invocation, benchmark, or production-readiness claim was
attempted. No upstream sample JSON was copied into the contract draft as a
runtime schema. Corrective action if a future tranche wants to implement the
schema: request a fresh GC-018 naming the specific field types, required/
optional status, and validation rules, per this draft's Claim Boundary.

## Selected Routing Outcome

No new fresh-GC-018 route is opened by this worker return. The receipt
schema contract draft is documentation/reference only and does not implement
a schema. `MSEA-CC-4` remains deferred at its existing disposition. The
draft's own Claim Boundary states that any future schema implementation,
receipt-writer code, or runtime behavior requires a fresh GC-018 and
source-verified work order.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T2/R5/R6 governed evidence |
| Enumeration command | filesystem-backed direct verification via `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD`; no full-corpus replay, per the work order's declared exclusion since MSEA-R5 already reconciled the full manifest |
| Manifest artifact or inline manifest | `## Contract Draft Requirements Coverage` table in this file |
| Processing ledger artifact or inline ledger | `## Contract Draft Requirements Coverage` table in this file (8 required sections, all present) |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `## Overlap And Novelty Classification` table in `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` |
| Unresolved items | 0 |
| Completion claim boundary | dispatch and contract-draft fulfillment only; no runtime, provider/live, public, production, OCR/VLM/hybrid execution, model download, API/router/Gradio, Docker, RAG write, checker, package activation, model-router, or action-authority claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| `output_files.md` artifact-family and field vocabulary | Concrete artifact families (layout/span debug, raw model, intermediate, flattened, V2, Markdown) and field families (source/backend identity, page/block/reading-order/geometry locators, content, heading level, caption/footnote, sub-type) | DOCTRINE_ADAPTED | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` and existing MSEA-T2 advisory | Worker adapted upstream vocabulary into CVF-owned contract language; MSEA-T2 remains the canonical claim-boundary owner. | Documentation/reference only |
| Pipeline vs. VLM backend field-shape differences | Concrete structural delta (flat list vs. nested page-then-block; different field sets per backend) not previously captured at this depth | DOCTRINE_ADAPTED | contract draft's Backend Variant Boundary section | Worker records the delta as contract-draft language for a future schema implementer to account for. | Documentation/reference only |
| `MSEA-CC-4` future schema-validation checker candidate | Preparatory schema-field groundwork this disposition explicitly anticipated | CHECKER_CANDIDATE (disposition unchanged) | MSEA-T2 Checker Candidate Ledger | Worker preserves the existing `defer until CVF owns schema fields` disposition without reopening it. | No checker implementation |
| Direct upstream sample JSON payloads | Rejected as direct schema import; only field-family names and structural observations are adapted into prose | REJECT_DIRECT_IMPORT | CVF-native contract-draft language only | Worker did not copy any upstream JSON block into the contract draft. | No direct source import |
| Full 425-file mirror and 373-file R5 target subset replay | Already reconciled by MSEA-R4/R5; re-enumeration would add no new value for this documentation-contract tranche | NO_PACKAGE_OR_RUNTIME_VALUE | MSEA-R4/R5 accepted artifacts | Worker did not replay the full-corpus enumeration; used only the single already-verified source file. | No runtime or package behavior |
| CLI/API/backend runtime surfaces named in prior tranches | Out of scope for this contract-draft tranche; the prior route decision's deferral is unchanged | RUNTIME_CANDIDATE | prior route decision matrix | Worker did not re-evaluate this candidate; it remains deferred behind its own reopen condition. | No install, execution, or provider/live proof |
| Docker deployment recipes named in prior tranches | Out of scope for this contract-draft tranche; the prior route decision's deferral is unchanged | PACKAGE_CANDIDATE | prior route decision matrix | Worker did not re-evaluate this candidate; it remains deferred behind its own reopen condition. | No package activation or Docker build/run |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Receipt artifact family vocabulary | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` Receipt Advisory table | ENRICH_EXISTING | Adds concrete upstream-anchored artifact families to MSEA-T2's abstract field-family rows | contract draft created |
| Backend-variant field-shape differences | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R5 confirmed a dual-backend schema exists at file level; this draft adds the concrete field-shape differences | contract draft created |
| `MSEA-CC-4` checker-candidate disposition | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` Checker Candidate Ledger | CONFIRMED_EXISTING | No change to disposition; this draft is preparatory groundwork, not a trigger to reopen it | disposition unchanged |
| Direct upstream sample JSON payloads | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | REJECT_DIRECT_IMPORT | Upstream sample payloads are not copied into this draft as a CVF schema | worker rejects direct import |
| Any high-value item without an existing CVF owner | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | CONFIRMED_EXISTING | every item in this pass fell inside the DOCTRINE_ADAPTED/ENRICH_EXISTING/REJECT_DIRECT_IMPORT taxonomy already applied above; no owner-surface gap was found | no additional action beyond the rows above |

Full detail table (same shape, same conclusions): `## Overlap And Novelty
Classification` in
`docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`.

## Source Mirror Migration Control

| Field | Disposition |
| --- | --- |
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material and is not source authority for MSEA-R7. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` (recomputed and reconciled, no drift) |
| Migration disposition | SOURCE_MIRROR_AUTHORITY_RETAINED_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: legacy adapter folder was not read for this worker return; the pinned source mirror plus accepted MSEA-T2/R5/R6 evidence were sufficient for all findings above |
| Claim boundary | source-mirror authority control only; no source import, package install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Corpus Completeness And Report Integrity

- Corpus task class: external repository documentation/reference contract-draft dispatch from accepted MSEA evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` plus accepted MSEA-T2/R5/R6 governed artifacts.
- Snapshot time: 2026-07-02, executionBaseHead `d7b0bc96`.
- Enumeration command: filesystem-backed direct verification via `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD`; no full-corpus replay, per the work order's declared exclusion since MSEA-R5 already reconciled the full manifest.
- Manifest artifact or inline manifest: `## Contract Draft Requirements Coverage` table above.
- Manifest hash: inherited from MSEA-R5's full-mirror reconciliation (`sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`); worker independently reconciled the source-mirror commit (not the full hash) and found no drift.
- Processing ledger artifact or inline ledger: `## Contract Draft Requirements Coverage` table above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=8 required contract sections; ledger_terminal=8 (all present and populated); exclusions=1 (full-corpus replay, declared by the work order itself); unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full 425-file mirror and 373-file R5 target-subset replay, per the work order's own `Declared exclusions` row - already reconciled by MSEA-R4/R5, re-enumeration adds no value for this documentation-contract tranche.
- Unreadable or unsupported files: none encountered.
- Aggregation check: all 8 required contract-draft sections are present and populated in `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`.
- Drift check: recomputed source-mirror commit matches the dispatch-expected commit exactly; no drift between dispatch (`ce48461e`) and this execution (`d7b0bc96`).
- Output traceability: every artifact/field family in the contract draft cites a specific `output_files.md` line anchor.
- Adversarial verification: prior MSEA-T2/R5/R6 conclusions were compared against this draft's content; MSEA-T2's claim-boundary vocabulary and `MSEA-CC-4` disposition are enriched, not contradicted or reopened.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: this worker return has no `## Findings`, `## Known Issues`,
or `| Finding |` table heading; it is a contract-draft worker-return packet,
not a finding-bearing audit or log artifact.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: re-verifying the source mirror commit and the
exact `output_files.md` anchors already cited in the work order's Source
Verification Block was predicted to confirm no drift and to support drafting
a complete 8-section contract that enriches MSEA-T2's receipt vocabulary
without contradicting it or reopening `MSEA-CC-4`.

Evidence Comparison: actual evidence confirms the prediction. The source
mirror commit matches exactly. Every cited anchor in `output_files.md`
resolved to the expected content. The contract draft's 8 required sections
are all present, source-anchored, and free of copied upstream sample JSON.

Contradiction Or Gap Disposition: no contradiction found. No gap was
identified inside this tranche's declared scope (a single-source contract
draft, not a corpus replay).

Claim Update: prediction CONFIRMED. Contract draft created with full section
coverage; no prior MSEA conclusion changed.

## Claim Boundary

This worker return covers only a bounded MSEA-R7 receipt schema contract
draft and its supporting source verification. It does not authorize or
claim MinerU runtime integration, parser execution, OCR execution,
VLM/hybrid backend routing, remote backend processing, model download,
API/router/Gradio service, Docker deployment, RAG indexing, document truth
verification, parser accuracy, table/formula correctness, OpenAI-compatible
or S3 live calls, public-sync export, checker enforcement, package
activation, certification, generated aggregate mutation, production
readiness, hosted readiness, model-router behavior, action authority, or
universal document intelligence. Reviewer/closer owns acceptance, material
commit, and session-sync if this worker return is accepted.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude (no-commit worker) |
| Provider or surface | Claude Code CLI / VSCode extension |
| Session or invocation | dispatchBaseHead `ce48461e`; executionBaseHead `d7b0bc96` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read (source files, required first reads); Bash (git rev-parse, git status, git diff, python governance gate scripts) |
| Target paths | `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` |
| Allowed scope source | this work order and the paired GC-018 baseline |
| Before status evidence | `git status --short` was empty at `d7b0bc96` before worker edits |
| After status evidence | two untracked `??` files: this worker return and the contract draft |
| Diff evidence | `git diff --name-status` shows no tracked-file mutations |
| Approval boundary | no implementation; no runtime/provider/live/public/package/checker/generated-state/model-router/MPI work |
| Claim boundary | receipt schema contract draft return only |
| Agent type | Claude |
| Invocation ID | `msea-r7-mineru-receipt-schema-contract-draft-2026-07-02` |
| Expected manifest | `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` |
| Actual changed set | `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this worker return; two new files created |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R7 MinerU receipt schema contract draft worker return |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim is made by this worker return. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this worker return. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this worker return. |
| invocationBoundary | Manual local source reads, source-mirror verification, and governance gate invocation only. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Worker-return evidence, source-mirror verification, no-commit role boundary, and reviewer-owned closure only. |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/adapter/MinerU install/execution/model-download/RAG/S3/OpenAI-compatible-call/schema-implementation behavior without a fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R7 is private provenance receipt-contract drafting work derived
from private source-mirror absorption evidence. No public-sync export is
authorized by this worker return.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror and accepted MSEA evidence -> CVF-native receipt schema contract draft reference -> future implementation only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`; MSEA-T2/R5/R6 |
| Disposition | ADAPT into contract draft; runtime/package/checker candidates remain unchanged from MSEA-R5/R6 dispositions |
| Claim boundary | dispatch fulfillment only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |
| Route note | This intake is an external repo or copied folder route, not an operator-provided external comparison, critique, or recommendation route; both canonical input types are named here so both the intake-routing guard and the worker-return quality gate can resolve the correct enum. |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this worker return drafts new contract-vocabulary
language from a single already-verified source anchor; it does not rescan or
reprocess a previously ledgered manifest, so the full rescan delta/routing/
sampling shape does not apply.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: NONE
frictionType: NONE
observedStep: full worker-return authoring pass
preventiveControlCandidate: NONE

Detail: no gate surprise, no helper gap, no worktree contamination, and no
literal-format self-trigger occurred this run. Because this tranche's scope
was a bounded single-source contract draft rather than a full-corpus
replay, and because the compact `NOT_APPLICABLE_WITH_REASON` rescan verdict
was the correct shape here (unlike MSEA-R5, which was a genuine reabsorption
pass requiring the full rescan section), the friction surface was
substantially smaller than the prior two MSEA worker returns. No new
preventive control is proposed.

## git status --short

```text
?? docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md
?? docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md
```

## Changed Files

| File | Action | Purpose |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md` | CREATE | This worker return |
| `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | CREATE | CVF-owned receipt schema contract draft enriching MSEA-T2 |

No other file was created, modified, deleted, renamed, formatted, or staged.

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse --short HEAD` | `d7b0bc96` |
| `git status --short` (before edits) | clean |
| `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, matches expected, no drift |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base d7b0bc96 --head HEAD` | PASS (recorded below) |
| `python governance/compat/check_external_knowledge_intake_routing.py --base d7b0bc96 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_core.py --base d7b0bc96 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_value_conversion.py --base d7b0bc96 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_external_absorption_overlap_discipline.py --base d7b0bc96 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_corpus_completeness_report_integrity.py --base d7b0bc96 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/check_source_mirror_migration.py --base d7b0bc96 --head HEAD --enforce` | PASS (recorded below) |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS (recorded below) |
| `git diff --name-status` | no tracked-file mutations |
| `git status --short` (after edits) | two untracked worker-output files |

## No-Commit Statement

`WORKER_MUST_NOT_COMMIT honored`. Worker did not run `git add`, `git commit`,
or `git push`. HEAD remains `d7b0bc96`. The only changes in the working tree
are the two untracked files listed above. Reviewer/closer owns acceptance and
material commit.
