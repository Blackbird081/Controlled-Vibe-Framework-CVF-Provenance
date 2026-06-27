# CVF Agent Work Order: LPCI2 EX-T3 Through EX-T6 Extraction Pipeline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-11

Worker: Codex

Reviewer: Codex

Commit mode: WORKER_MAY_COMMIT

executionBaseHead: `041cb307`

closureBaseHead: `041cb307`

completionReviewPath:

`docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md`

---

## Purpose

Implement and close the unblocked EX-T3 through EX-T6 extraction foundation
roadmap rows as a local deterministic tranche.

## Authority Chain

- Operator instruction: 2026-06-11, use single-agent multi-role and complete
  related roadmap work.
- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`.
- Parent roadmap:
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`.
- GC-018:
  `docs/baselines/CVF_GC018_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md`.

## Agent Roles

| Role | Agent | Responsibility |
| --- | --- | --- |
| Operator | Human | Authorizes single-agent multi-role completion |
| Orchestrator | Codex | Bound the unblocked roadmap rows |
| Worker | Codex | Implement local deterministic source/tests and registry updates |
| Reviewer | Codex | Run tests/gates, close packet, and update continuity |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator asked Codex to complete all related roadmap work using the prior multi-role rule. |
| Scope classification | Bounded local extraction foundation implementation and closure. |
| Risk sensitivity | R2 because OCR and legal-policy content could be overclaimed if boundaries are loose. |
| Selected canonical route mode | SINGLE_AGENT_MULTI_ROLE. |
| Role separation basis | Scope is local deterministic source/tests/docs only; no provider, external mutation, OCR model download, public-sync, or corpus ingestion. |
| Escalation condition | Stop or close blocked if work requires OCR dependency install, external Policy_Local mutation, EC-02 runtime disclosure, public-sync, or provider proof. |

## Single-Agent Multi-Role Control Block

roleMode: `SINGLE_AGENT_MULTI_ROLE`

allowedBecause: bounded source/test/docs closure with machine gates, no external
workspace mutation, no live/provider proof, and no production/public claim.

roleSeparationMechanism:

- source verification table;
- focused pytest evidence;
- GC-051 registry coverage;
- reviewer-fast and pre-commit hook chains;
- explicit claim boundary.

forbiddenSelfApprovalClaims:

- no OCR quality or OCR dependency readiness claim;
- no corpus ingestion or external Policy_Local mutation claim;
- no governed retrieval behavior claim;
- no current-law/legal-quality claim;
- no production/public readiness.

## Scope / Target / Owner Boundary

Allowed scope:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`;
- `docs/baselines/CVF_GC018_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_FOR_CODEX_2026-06-11.md`;
- `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md`;
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`;
- `CVF_SESSION_MEMORY.md`;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- `AGENT_HANDOFF_V17_2026-06-07.md`.

Forbidden scope:

- no package/lockfile edit;
- no OCR dependency install or model download;
- no external Policy_Local edit;
- no corpus ingestion or generated corpus mutation;
- no provider/API-key use;
- no public-sync;
- no EC-02 runtime disclosure or `QUERY_CLASS_GATED` activation.

## Required First Reads

| File | Purpose |
| --- | --- |
| `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | confirm EX-T3 through EX-T6 rows |
| `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | confirm OCR dependency status and language mapping evidence |
| `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md` | confirm Tier 1 predecessor boundary |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | confirm Tier 1 result and threshold symbols |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | confirm DSCP profile handoff owner |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | confirm downstream profile selection owner |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EX-T3 through EX-T6 rows | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 487-490 | `EX-T3`; `EX-T4`; `EX-T5`; `EX-T6` | parent roadmap | ACCEPT |
| VALUE_SET: MIN_CHARS threshold is 100 | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | line 19 | `MIN_CHARS_PER_PAGE` | Tier 1 extractor module | ACCEPT |
| EXISTS: Tier 1 escalation signal | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | lines 55 and 131 | `below_min_chars_flag` | Tier 1 extractor result | ACCEPT |
| VALUE_SET: EasyOCR mapping is direct for `en` and `vi` | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | `ocrLanguageMapping.entries` | `easyocrCode` | EX-T1 dependency audit summary | ACCEPT |
| VALUE_SET: Tesseract mapping is `en->eng`, `vi->vie` | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | `ocrLanguageMapping.entries` | `tesseractCode` | EX-T1 dependency audit summary | ACCEPT |
| EXISTS: DSCP domain profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 96 | `applyDomainProfileToDescriptorInput` | DSCP domain profile contract | ACCEPT |
| EXISTS: DSCP profile selection adapter | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | line 57 | `selectAndApplyDscpDomainProfile` | DSCP profile selection adapter | ACCEPT |
| DOC_ONLY_NEW: local extraction pipeline symbols | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 143, 168, 216, 255, and 299 | `map_ocr_language_codes`; `extract_tier2_ocr`; `evaluate_extraction_quality`; `chunk_extracted_pages`; `build_extraction_dscp_descriptor_inputs` | EX-T3 through EX-T5 local pipeline | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:

- `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json`
- `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md`
- `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md`

priorVerificationAnchor: EX-T1 dependency audit and EX-T2 Tier 1 closure.

freshRecomputeRequired: `NO`

recomputeReason: `N/A with reason - no external source binaries are opened.`

unicodePathHandling: `N/A with reason - no external Unicode paths are opened.`

extractedTextAuthority: `N/A with reason`

## Current Runtime Freshness Verification

Runtime freshness command:

`rg -n "def map_ocr_language_codes|def extract_tier2_ocr|def evaluate_extraction_quality|def chunk_extracted_pages|def build_extraction_dscp_descriptor_inputs|MIN_CHARS_PER_PAGE|applyDomainProfileToDescriptorInput|selectAndApplyDscpDomainProfile" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src -S`

Observed result:

- Tier 1 threshold and escalation signal exist in `tier1_extractor.py`.
- New pipeline symbols exist in `extraction_pipeline.py`.
- Downstream DSCP profile application and selection symbols exist in CPF.

Freshness disposition: `SOURCE_VERIFIED_LOCAL_DETERMINISTIC`.

## External Artifact Hash Manifest

| Artifact | sha256 | Role |
| --- | --- | --- |
| `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | `46caff533ab8e4d8bc0cfa68070abdf69b7eb205e420c66d9b5db2729109492c` | dependency audit summary |
| `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | `6e6ee6e640275a85541bcd32a4f9290585fb6d30debc5780df10ef2ea6491e9d` | dependency audit report |
| `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md` | `5e118d33e888176d0f7dc9657602ec041197a46699767d3aa11fe0a48b01a2c9` | Tier 1 predecessor closure |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order handling | Disposition |
| --- | --- | --- |
| EX-T3 Tier 2 OCR fallback | Add adapter boundary, OCR language mapping, and confidence capture without model download | PASS_BOUNDED |
| EX-T4 quality gate and chunk schema | Add quality flags and fixed-window chunk schema | PASS_BOUNDED |
| EX-T5 DSCP pipeline wire-in | Add descriptor-shaped handoff for downstream DSCP profile application | PASS_BOUNDED |
| EX-T6 GC-051 coverage | Update registry JSON and Markdown for new source/test surfaces | PASS |

## Pre-Flight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Base HEAD captured | `git rev-parse --short HEAD` | `041cb307` |
| Worktree scope | `git status --short` | no unrelated tracked edits before implementation |
| Source freshness | `rg` command in Current Runtime Freshness Verification | expected symbols present |
| Focused pytest | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q` | PASS |

## Write Ownership

Codex owns only the allowed paths listed above. Any expansion into dependency
installation, model download, external workspace mutation, public-sync, or
provider/live proof requires a separate governed packet.

## Execution Plan

1. Add the extraction pipeline module with OCR adapter boundary, quality gate,
   chunk schema, and DSCP descriptor handoff.
2. Add focused deterministic tests.
3. Update GC-051 JSON/Markdown registry coverage.
4. Update the roadmap EX rows and closure packet.
5. Run pytest, reviewer-fast, pre-commit, and sync session continuity.

## Evidence Requirements

| Evidence | Required result |
| --- | --- |
| Focused pytest | all extraction foundation tests pass |
| Python compile | `py_compile` passes for Tier 1 and pipeline modules |
| Registry coverage | GC-051 JSON/Markdown entries cover new source and test files |
| Claim boundary | no OCR dependency/model, corpus ingestion, provider, public, legal-quality, or production claim |

## Review Gate

Reject closure if package files change, OCR dependencies are installed, external
Policy_Local paths are modified, generated corpus files are written, or tests
and governance gates fail.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md` | final closure review | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | EX-T3 through EX-T6 closed; EC side still blocked | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entries for pipeline source/test | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | quick lookup rows for pipeline source/test | PASS |
| External evidence digest | EX-T1 summary/report and EX-T2 completion | sha256:46caff533ab8e4d8bc0cfa68070abdf69b7eb205e420c66d9b5db2729109492c; sha256:6e6ee6e640275a85541bcd32a4f9290585fb6d30debc5780df10ef2ea6491e9d; sha256:5e118d33e888176d0f7dc9657602ec041197a46699767d3aa11fe0a48b01a2c9 | PASS |
| System loop interlock | no system-loop mutation | local extraction foundation only | N/A with reason: no runtime loop changed |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned final sync | PASS |

## Closure Checklist

- [x] Source verification complete.
- [x] Evidence reuse plan complete.
- [x] Focused tests pass.
- [x] GC-051 coverage updated.
- [x] Roadmap rows updated.
- [x] Claim boundary preserved.

## Return-To-Orchestrator Conditions

Return blocked if any requested continuation requires OCR dependency
installation, model download, external corpus mutation, public-sync,
provider/live proof, or EC-02 runtime retrieval disclosure.

## Operator Checkpoint

No extra operator decision is required for this local deterministic foundation
batch. Operator approval is still required for dependency installation, OCR
model download, external Policy_Local mutation, public-sync, provider/API-key
proof, or EC successor activation.

## Acceptance Criteria

- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q` passes.
- New module avoids hard dependency on OCR packages.
- New DSCP handoff descriptor records `rawContentReleased=false`.
- Roadmap and session continuity distinguish EX closure from blocked EC lanes.

## Claim Boundary

This work order closes local extraction foundation surfaces only. It does not
prove OCR accuracy, model availability, corpus ingestion, Policy_Local runtime
update, governed retrieval behavior, legal answer quality, production
readiness, public readiness, or T12 readiness.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorized.
