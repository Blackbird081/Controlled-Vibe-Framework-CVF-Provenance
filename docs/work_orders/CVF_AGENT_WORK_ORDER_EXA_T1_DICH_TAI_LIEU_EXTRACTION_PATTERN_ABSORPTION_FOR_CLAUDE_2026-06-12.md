# CVF Agent Work Order: EXA-T1 Dich Tai Lieu Extraction Pattern Absorption

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-12

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `d1167f69`

executionBaseHead: `d1167f69`

closureBaseHead: `d1167f69`

completionReviewPath:
`docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_WORKER_RETURN_2026-06-12.md`

reviewerOwnedClosurePaths:
`docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md`;
`docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_WORKER_RETURN_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_EXA_T1_DICH_TAI_LIEU_EXTRACTION_PATTERN_ABSORPTION_2026-06-12.md`

Parent roadmap:
`docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`

External source:
`https://github.com/nclamvn/dich-tai-lieu`

Required external commit:
`92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`

## Purpose

Inspect `nclamvn/dich-tai-lieu` as a pinned external source and return a
bounded scan-layer pattern absorption packet for Codex review.

## Authority Chain

| Authority | Path or source | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 external-source absorption request | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_EXA_T1_DICH_TAI_LIEU_EXTRACTION_PATTERN_ABSORPTION_2026-06-12.md` | DISPATCHED |
| Parent roadmap | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | EXA_T1_DISPATCHED |
| RDA-T4 closure | `docs/reviews/CVF_MEOR_RDA_T4_FOUNDATION_CLOSURE_AND_POLICYLOCAL_SUCCESSOR_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatch and review only |
| Worker | Claude | source-map and classify patterns only |
| Reviewer | Codex | verify worker artifacts before closure |
| Committer | Codex | commit only after review |

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V17_2026-06-07.md`
- this work order
- GC-018 baseline for EXA-T1
- parent EXA roadmap

## Pre-Flight Checks

Before authoring worker artifacts, Claude must verify:

| Check | Required evidence |
| --- | --- |
| CVF workspace base | `git rev-parse --short HEAD` equals or descends from `d1167f69` |
| CVF worktree | `git status --short` recorded |
| External remote | `git remote -v` shows `https://github.com/nclamvn/dich-tai-lieu.git` |
| External commit | `git rev-parse HEAD` equals `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` |
| No commit mode | worker confirms `WORKER_MUST_NOT_COMMIT` |

If the external commit does not match, stop and return
`BLOCKED_EXTERNAL_COMMIT_DRIFT`.

## Write Ownership

Claude may create only:

- `docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md`
- `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_WORKER_RETURN_2026-06-12.md`

Claude must not edit runtime/source files, registries, session state, handoff,
public-sync, or external Policy_Local files.

## Intake Role Routing Decision

- Intake summary: operator identified a public external repository as a
  scan-layer learning candidate before Policy_Local use-case execution.
- Scope classification: source absorption and design evidence only.
- Risk sensitivity: medium, because this touches external code, provider/OCR
  patterns, and downstream legal-policy use-case boundaries.
- routeMode: `MULTI_AGENT_MULTI_ROLE`.
- Worker role: source-map and classify patterns.
- Reviewer role: Codex verifies, repairs if needed, and commits.
- Escalation condition: stop if useful absorption requires code import,
  dependency installation, provider/API-key use, OCR execution, public-sync, or
  Policy_Local mutation.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Source-map pinned external repo | record remote, commit, and file inventory | source map | Codex review |
| Classify reusable scan patterns | ACCEPT/DEFER/REJECT matrix | worker return | Codex review |
| Avoid code import | forbidden scope | changed-path proof | `git status --short` |
| Preserve Policy_Local boundary | no external mutation | worker return | Codex review |
| Prepare CVF-native candidates | candidate recommendation table | worker return | Codex review |

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| External README names Smart Extraction | canonical external source snapshot | external root readme lines 31-32 | `Smart Extraction` | README feature table | VALUE_SET | ACCEPT |
| External README names translation memory and glossary | canonical external source snapshot | external root readme lines 34-35 | `Translation Memory`, `Glossary Management` | README feature table | VALUE_SET | ACCEPT |
| Router records extraction page-route metrics | canonical external source snapshot | external `core/smart_extraction/extraction_router.py` lines 38-52 | `ExtractionResult` | dataclass | EXISTS | ACCEPT |
| Router analyzes before strategy selection | canonical external source snapshot | external `core/smart_extraction/extraction_router.py` line 118 | `self.analyzer.analyze` | `SmartExtractionRouter.extract` | RUNTIME_BEHAVIOR | ACCEPT |
| Router has OCR language route list | canonical external source snapshot | external `core/smart_extraction/extraction_router.py` lines 134-137 | `ocr_supported_langs` | `SmartExtractionRouter.extract` | VALUE_SET | ACCEPT |
| Document analysis exposes page and document signals | canonical external source snapshot | external `core/smart_extraction/document_analyzer.py` lines 33-80 | `PageAnalysis`, `DocumentAnalysis` | dataclasses | EXISTS | ACCEPT |
| Document analysis thresholds exist | canonical external source snapshot | external `core/smart_extraction/document_analyzer.py` lines 100-102 | `TEXT_COVERAGE_THRESHOLD`, `SCANNED_THRESHOLD`, `COMPLEX_PAGE_THRESHOLD` | `DocumentAnalyzer` | VALUE_SET | ACCEPT |
| EQS defines six quality signals | canonical external source snapshot | external `api/services/eqs.py` lines 5-10 | `text_density`, `structure`, `encoding`, `language`, `completeness`, `format_integrity` | module docstring | VALUE_SET | ACCEPT |
| EQS has weighted signal map | canonical external source snapshot | external `api/services/eqs.py` lines 74-80 | `DEFAULT_WEIGHTS` | module constant | VALUE_SET | ACCEPT |
| Feedback loop defines strategy values | canonical external source snapshot | external `api/services/extraction_feedback.py` lines 32-37 | `ExtractionStrategy` | enum | EXISTS | ACCEPT |
| Feedback loop defines fallback chain | canonical external source snapshot | external `api/services/extraction_feedback.py` lines 102-103 | `DEFAULT_FALLBACK_CHAIN` | module constant | EXISTS | ACCEPT |
| OCR language support contains Vietnamese OCR config | canonical external source snapshot | external `api/services/ocr_language_support.py` lines 122-130 | `LANGUAGE_CONFIGS.vi` | module constant | VALUE_SET | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

Claude must complete this block in the worker return:

| Control | Required worker action |
| --- | --- |
| Source depth | inspect source files and tests, not README only |
| Corpus boundary | enumerate every external file read |
| Accept/defer/reject | classify every candidate pattern |
| CVF owner routing | map accepted ideas to CVF scan-layer owner surfaces |
| Adversarial review | identify overclaim, dependency, provider, domain bleed, and license risks |
| Blind-spot delta | list uninspected files and deferred questions |

## Corpus Completeness And Report Integrity

Worker must include a bounded corpus block for the external review set:

- enumeration command;
- file-level processing ledger;
- excluded files with reason;
- unreadable or unsupported files with reason;
- final verdict: `COMPLETE_WITH_DECLARED_EXCLUSIONS`, `PARTIAL`, or
  `BLOCKED`.

Do not claim full repository completeness unless the full repository was
enumerated and reconciled.

- Corpus task class: external-source pattern absorption dispatch.
- Corpus root: `https://github.com/nclamvn/dich-tai-lieu` at `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`.
- Snapshot time: 2026-06-12 dispatch snapshot; worker must refresh from pinned commit before return.
- Enumeration command: worker must run `rg --files --hidden --no-ignore` or equivalent filesystem-backed enumeration against the pinned external clone and record the exact command.
- Manifest artifact or inline manifest: `docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md` must contain the bounded manifest or link to an inline manifest section.
- Manifest hash: N/A with reason: dispatch defines the required worker artifact; worker must compute or explicitly mark N/A with reason in the returned source map.
- Processing ledger artifact or inline ledger: `docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md` must contain a file-level processing ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=required_in_worker_source_map; ledger_terminal=required_in_worker_source_map; exclusions=required_in_worker_source_map; unresolved=1
- Unresolved files: 1
- Declared exclusions: required in worker return; dispatch has no completed external ledger yet.
- Unreadable or unsupported files: required in worker return; dispatch has no completed external ledger yet.
- Aggregation check: worker must show totals add up.
- Drift check: worker must confirm external commit equals `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`.
- Output traceability: worker must map every accepted pattern to source file and line/section evidence.
- Adversarial verification: worker must include an overclaim/dependency/provider risk review.
- Corpus verdict: PARTIAL

Dispatch verdict reason: this work order defines required corpus evidence but
does not itself complete the external corpus review.

## Execution Plan

1. Verify CVF base and external commit.
2. Enumerate relevant external files under:
   - `README.md`
   - `core/smart_extraction/`
   - `api/services/eqs.py`
   - `api/services/extraction_feedback.py`
   - `api/services/ocr_language_support.py`
   - focused tests related to extraction feedback, OCR language support, and
     smart extraction if present.
3. Create the source map artifact.
4. Create the worker return artifact with pattern disposition.
5. Leave artifacts uncommitted and report `git status --short`.

## Pattern Disposition Requirements

Classify at least these patterns:

| Pattern | Required disposition fields |
| --- | --- |
| Strategy router | source evidence, CVF value, risk, disposition |
| Page/document analysis signals | source evidence, CVF value, risk, disposition |
| Extraction quality scoring | source evidence, CVF value, risk, disposition |
| Feedback loop and escalation | source evidence, CVF value, risk, disposition |
| OCR language/script routing | source evidence, CVF value, risk, disposition |
| Translation memory/glossary | source evidence, CVF value or reason to defer, disposition |
| Multi-provider fallback | source evidence, overclaim risk, likely disposition |

Allowed worker dispositions:

- `ACCEPT_AS_CVF_CONTRACT_CANDIDATE`
- `DEFER_REQUIRES_SEPARATE_ROADMAP`
- `REJECT_APP_SPECIFIC`
- `REJECT_GOVERNANCE_RISK`

## Negative Search And Collision Discipline

Claude must not treat tokens that appear only in this work order as existing
CVF runtime fields. The worker must search the current CVF repo before naming a
CVF owner surface and must label proposed fields as candidate names, not source
facts.

Required negative-search checks:

- no CVF source file currently owns `ExtractionStrategy` from the external app;
- no CVF source file currently owns `EQSReport` from the external app;
- no external provider fallback is authorized by existing CVF scan layer;
- no Policy_Local mutation is authorized by EXA-T1.

If a search contradicts this packet, return to Codex with corrected evidence.

## Evidence Reuse And Encoding Plan

verificationMode: `RECOMPUTE_REQUIRED`

recomputeReason: external source absorption must be rebuilt from the pinned
commit instead of relying on chat memory, README-only summaries, or prior
operator description.

externalVerificationArtifact: `https://github.com/nclamvn/dich-tai-lieu`

externalVerificationAnchor: `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`

freshRecomputeRequired: NO for README performance, cost, speed, production, or
accuracy claims. Those claims must be treated as unverified third-party claims
and must not be adopted by CVF.

freshSourceReadRequired: YES for source files listed in this work order and
any extra files Claude cites.

unicodePathHandling: use UTF-8-safe file reads and record any fallback if a
path or source text contains non-ASCII. Do not normalize external filenames or
CVF filenames outside the allowed artifacts.

extractedTextAuthority: `AUXILIARY_ONLY`

Evidence reuse boundary: source lines may support pattern existence only. They
do not prove runtime correctness, production readiness, provider behavior,
accuracy, cost, speed, or Policy_Local readiness.

## Evidence Requirements

Worker return must include:

- external commit evidence;
- external file inventory;
- source verification table;
- pattern disposition matrix;
- CVF candidate recommendation table;
- no-code-import proof;
- no-provider/API-key proof;
- claim boundary;
- Finding-To-Governance Learning Disposition.

## Review Gate

Codex must reject the packet if it:

- copies third-party code;
- instructs installing dependencies;
- claims production, public, performance, cost, or accuracy evidence;
- opens Policy_Local mutation;
- treats provider fallback as allowed runtime behavior;
- lacks corpus completeness or source verification.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope evidence gaps without asking the operator.
Ask only if the repair would require code import, dependency installation,
provider/API-key use, OCR execution, external Policy_Local mutation, public-sync,
or a readiness claim.

## Reviewer Closure Conversion

Claude must return uncommitted artifacts. Codex owns conversion from worker
return to closure. Codex must refresh `closureBaseHead`, rerun reviewer-fast and
pre-closure gates, and decide whether EXA-T2 is warranted.

## Allowed Scope

- Create the two worker artifacts named in Write Ownership.
- Read the pinned external repository.
- Use local shell read/search commands.

## Forbidden Scope

- Commit.
- Modify CVF source/runtime/test code.
- Modify GC-051 or other registries.
- Modify session state, handoff, or memory.
- Modify public-sync repo.
- Modify external Policy_Local workspace.
- Install dependencies.
- Run OCR, Vision, or provider/API-key calls.
- Claim readiness or performance.

## Acceptance Criteria

1. Source map is complete for the bounded review set.
2. Worker return classifies every required pattern.
3. Accepted value is stated as CVF-native candidate, not copied code.
4. Deferred and rejected items include reasons.
5. No forbidden path or action occurs.

## Closure Checklist

| Item | Worker expectation |
| --- | --- |
| Source map authored | required before return |
| Worker return authored | required before return |
| External commit evidence recorded | required before return |
| Pattern matrix complete | required before return |
| Forbidden actions avoided | required before return |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: DISPATCHED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_WORKER_RETURN_2026-06-12.md` | worker return expected | N/A with reason: worker has not returned yet |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | `Status: EXA_T1_DISPATCHED` | PASS |
| Registry JSON | BLOCKED with reason: no source/test corpus added by dispatch | GC-051 update outside dispatch scope | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no source/test corpus added by dispatch | GC-051 update outside dispatch scope | BLOCKED with reason |
| External evidence digest | N/A with reason: worker will produce bounded external source map | expected in worker return | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation | no interlock update required | N/A with reason |
| Session continuity | active state/memory/handoff | Codex session sync after dispatch commit | PASS |

## Return-To-Orchestrator Conditions

Return to Codex if:

- external commit drift is detected;
- relevant files cannot be read;
- source evidence contradicts the work order;
- useful absorption requires code import, dependency installation, provider
  calls, or Policy_Local mutation.

## Operator Checkpoint

No operator checkpoint is required during worker execution unless the worker
needs to exceed scope. Codex review is required before closure or any EXA-T2
roadmap.

## Claim Boundary

This work order authorizes only external pattern absorption. It does not
authorize code import, dependency installation, OCR runtime, provider calls,
Policy_Local mutation, EC activation, retrieval, corpus ingestion, T12,
public-sync, production readiness, public readiness, or third-party performance
claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private external-source absorption dispatch; no public-sync authorized.
