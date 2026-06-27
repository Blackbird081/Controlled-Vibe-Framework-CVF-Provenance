# CVF Agent Work Order: EXA-T2 Scan Signal And Route Decision Contracts

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-12

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `8376a31a`

executionBaseHead: `5a3d1262`

closureBaseHead: `5a3d1262`

completionReviewPath:
`docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`

reviewerOwnedClosurePaths:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`;
`docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_WORKER_RETURN_2026-06-12.md`;
`docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`;
`docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`;
`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`

GC-018:
`docs/baselines/CVF_GC018_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_2026-06-12.md`

Parent roadmap:
`docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`

## Purpose

Implement deterministic CVF-owned scan-signal and route-decision contracts for
the extraction foundation, using EXA-T1 as prior learning and current CVF
extraction owners as source authority.

Success means the worker returns uncommitted source, tests, registry updates if
needed, and evidence proving that route decisions are deterministic,
domain-agnostic, and do not execute OCR, providers, Policy_Local mutation, or
retrieval.

## Closure Result

Codex reviewed the Claude no-commit return, repaired two allowed-scope issues,
and accepted EXA-T2 as `CLOSED_PASS_BOUNDED`.

Accepted implementation:

- `DocumentScanSignals` frozen dataclass;
- `ScanRouteDecision` frozen dataclass;
- four stable route dispositions;
- deterministic `decide_scan_route()` mapping for current extraction quality
  statuses;
- fail-closed escalation for invalid or contradictory scan signals;
- GC-051 source/test registry coverage.

Verification:

- `python -m py_compile EXTENSIONS\CVF_EXTRACTION_FOUNDATION\src\scan_route_decision.py` PASS;
- focused pytest PASS 23/23;
- extraction-foundation pytest PASS 105/105;
- reviewer-fast PASS 12/12.

## Authority Chain

| Authority | Path or source | Status |
| --- | --- | --- |
| Operator instruction | 2026-06-12 next-road direction after external repo absorption | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current next allowed move is EXA-T2 authorization |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | requires fresh EXA-T2 authorization |
| GC-018 | `docs/baselines/CVF_GC018_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_2026-06-12.md` | DISPATCHED |
| Parent roadmap | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | EXA-T2 DISPATCHED |
| EXA-T1 completion | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| Reviewer-fast hardening | `docs/reviews/CVF_REVIEWER_FAST_RESCAN_GATE_PLACEMENT_HARDENING_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |

Authority boundary:

- this work order does not authorize work outside the cited authority chain;
- if a source fact conflicts with current runtime source, stop and return to
  Codex with corrected evidence;
- worker must not release a held downstream Policy_Local, EC, or T12 lane.

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatch packet, scope, and closure review |
| Worker | Claude | implement allowed source/test/registry artifacts only |
| Reviewer | Codex | review pending artifacts and decide closure |
| Committer | Codex | commit approved batch after review |

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION_MEMORY.md`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V18_2026-06-12.md`
5. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
6. `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`
7. `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md`
8. this work order
9. EXA-T2 GC-018 baseline
10. EXA-T1 source map and completion review

## Pre-Flight Checks

Before material edits, Claude must record:

| Check | Required evidence |
| --- | --- |
| Startup ack | active mode, active handoff, next allowed move, parked checkpoint |
| Execution anchor | `git rev-parse --short HEAD` as `executionBaseHead` |
| Worktree state | `git status --short` before edits |
| Dispatch ancestry | HEAD equals or descends from `8376a31a` |
| Commit mode | explicit `WORKER_MUST_NOT_COMMIT` acknowledgment |

If HEAD does not descend from `8376a31a`, stop with
`BLOCKED_BASE_DRIFT_REQUIRES_CODEX_REFRESH`.

## Write Ownership

Claude may create or modify only:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/__init__.py` only if an export is
  required
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only if new
  source/test files require GC-051 rows
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` only if new source/test
  files require GC-051 rows
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_WORKER_RETURN_2026-06-12.md`

Claude must not edit:

- external Policy_Local files;
- EC, T12, retrieval, provider, public-sync, or session-state files;
- the EXA roadmap or this work order during worker execution;
- external repository files;
- dependency manifests unless Codex issues a new authorization.

## Intake Role Routing Decision

- Intake summary: operator wants CVF scan-layer foundation strengthened from
  direct GitHub-link absorption before Policy_Local use-case work.
- Scope classification: bounded source implementation in CVF extraction
  foundation.
- Risk sensitivity: medium, because route decisions can be mistaken for OCR,
  provider, or Policy_Local readiness.
- routeMode: `MULTI_AGENT_MULTI_ROLE`.
- Worker role: implement deterministic source/test artifacts only.
- Reviewer role: Codex reviews, commits, and closes.
- Escalation condition: stop if implementation needs dependency installation,
  OCR execution, provider/API-key use, external Policy_Local mutation, public
  claim, or new legal-policy domain semantics.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Implement EXA-T2 deterministic scan strategy contract | create `DocumentScanSignals` and `ScanRouteDecision` contracts | source file | focused tests |
| Reuse current quality and reporting owners | import or accept existing `ExtractionQualityReport` and report-compatible signals | source/tests | source verification and tests |
| Avoid parallel quality/reporting stack | no new competing quality report or operator report class | source diff | Codex review |
| Preserve OCR/provider boundary | decisions may recommend eligibility/review but must not execute OCR/providers | tests | no-call assertions or source proof |
| Keep Policy_Local downstream | no external Policy_Local files touched | git status | reviewer proof |
| Register new source/test files | GC-051 JSON/Markdown rows if files are added | registry updates | GC-051/reviewer-fast |

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `ExtractionQualityReport` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | dataclass | EXISTS | ACCEPT |
| `evaluate_extraction_quality()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 235 | `evaluate_extraction_quality` | function | EXISTS | ACCEPT |
| `map_ocr_language_codes()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 162 | `map_ocr_language_codes` | function | EXISTS | ACCEPT |
| OCR execution requires a caller adapter | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 187-200 | `extract_tier2_ocr` | function | RUNTIME_BEHAVIOR | ACCEPT |
| `ExtractionStorageBoundary` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 152 | `ExtractionStorageBoundary` | dataclass | EXISTS | ACCEPT |
| `build_extraction_storage_boundary()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 424 | `build_extraction_storage_boundary` | function | EXISTS | ACCEPT |
| `ScanOutcomeReport` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 43 | `ScanOutcomeReport` | dataclass | EXISTS | ACCEPT |
| `build_scan_outcome_report()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 131 | `build_scan_outcome_report` | function | EXISTS | ACCEPT |
| EXA-T1 recommends EXA-T2 deterministic contracts | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md` | lines 472-476 | `DocumentScanSignals`, `ScanRouteDecision` | completion recommendation | DOC_ONLY_NEW | ACCEPT |

## New Doc-Only Fields

Worker may implement these names as new local contracts. They are not source
facts until implemented.

| Proposed item | Required meaning | Required boundary |
| --- | --- | --- |
| `DocumentScanSignals` | normalized pre-extraction or supplied extraction signals such as source type, language codes, page count, text presence, page coverage, mean OCR confidence, and quality flags | no raw text, no OCR execution, no provider call |
| `ScanRouteDecision` | deterministic route recommendation plus reason codes and operator action | no runtime extraction execution, no Policy_Local mutation |
| `LOCAL_TEXT_EXTRACTION_RECOMMENDED` | local digital/native extraction path is acceptable from supplied signals | no readiness claim |
| `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` | OCR may be needed, but operator or later authorized adapter must decide | no automatic OCR |
| `ESCALATE_OR_ABSTAIN` | insufficient, contradictory, or ambiguous signals require review | no guessing |
| `BLOCKED_UNSUPPORTED` | unsupported language, source type, or boundary condition blocks route | no fallback provider |

## Current Runtime Freshness Verification

Worker must rerun these or stricter checks before return:

| Runtime surface | Required check | Required disposition |
| --- | --- | --- |
| Proposed names not currently owned | `rg -n "DocumentScanSignals|ScanRouteDecision" EXTENSIONS/CVF_EXTRACTION_FOUNDATION governance --hidden --no-ignore` before edits | no source owner before implementation |
| External app tokens not imported | search changed source for `ExtractionStrategy`, `EQSReport`, provider fallback, automatic retry | no copied external runtime vocabulary unless explicitly explained as rejected |
| Existing quality owner reused | source imports or type usage show reuse of `ExtractionQualityReport` or its stable status values | PASS |
| Existing scan report compatible | route result can be converted to additional `ScanOutcomeFinding` or documented operator action without creating a parallel report system | PASS |

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:
`docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md`

priorVerificationAnchor:
`92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`

reuseReason: EXA-T1 already verified the external source snapshot and accepted
only CVF-native deterministic candidate value. EXA-T2 is source implementation
inside CVF, not another external corpus absorption pass.

freshRecomputeRequired: NO

freshRecomputeRequiredReason: external repo hashes, large external files,
README production claims, performance claims, OCR quality claims, and provider
behavior are not EXA-T2 source authority.

freshRuntimeVerificationRequired: YES for changed CVF source/test/registry
files.

extractedTextAuthority: N/A with reason

extractedTextAuthorityReason: EXA-T2 does not consume extracted document text
as source authority.

unicodePathHandling: use literal paths and UTF-8-safe readers. Non-ASCII test
filenames are allowed only when proving path handling and must record an
exception comment.

## Export Surface Decision

Export Surface Decision: EXPORTED

Required export proof:

- if `scan_route_decision.py` is created, the work must expose an explicit
  import path through the source module itself and update `src/__init__.py`
  only if local package convention requires it;
- focused tests must import the new contracts from the chosen owner path;
- downstream consumer boundary must state that Policy_Local cannot consume the
  surface until a later PL-S or EC authorization.

## Work-Order Fulfillment Manifest

Required artifacts:

| Artifact | Required status |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | created or worker must justify same-domain alternative |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py` | created |
| GC-051 JSON/Markdown | updated if new files are created |
| worker return review | created under `docs/reviews/` |

## Required Artifact Manifest

| Path | Purpose | Required at handoff | Status |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | EXA-T2 source contract | YES | PASS |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py` | focused EXA-T2 tests | YES | PASS |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 machine registry rows | YES | PASS |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | GC-051 human registry rows | YES | PASS |
| `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_WORKER_RETURN_2026-06-12.md` | worker return packet | YES | PASS |
| `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md` | Codex completion review | YES | PASS |
| `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | parent roadmap closure state | YES | PASS |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md` | work order closure state | YES | PASS |

Forbidden proof literals in changed source/tests:

- `provider fallback`
- `auto retry`
- `Policy_Local`
- `production ready`
- `public ready`
- `release ready`

These may appear only in worker return claim-boundary or forbidden-scope prose.

## Execution Plan

1. Capture `executionBaseHead` and initial `git status --short`.
2. Rerun the required freshness and negative-search checks.
3. Implement the smallest same-domain extraction-foundation source surface for
   `DocumentScanSignals` and `ScanRouteDecision`.
4. Add focused tests for deterministic route decisions and no OCR/provider/raw
   content release.
5. Update GC-051 JSON/Markdown if new source/test files are added.
6. Run pending-return gates.
7. Create the worker return packet and leave all artifacts uncommitted.

## Implementation Requirements

Worker must implement a deterministic function or equivalent API that:

1. accepts `DocumentScanSignals`;
2. returns `ScanRouteDecision`;
3. maps existing quality statuses `PASS`, `NEEDS_TIER2_OCR`,
   `OCR_LOW_CONFIDENCE`, `PARTIAL_EXTRACTION`, and `EMPTY` into stable route
   dispositions;
4. treats unsupported languages as blocked or escalated using current
   `map_ocr_language_codes()` behavior, without executing OCR;
5. includes reason codes and operator action strings that are stable and
   domain-agnostic;
6. does not expose raw extracted text;
7. does not import external repository code.

## Acceptance Criteria

1. Focused tests cover local pass route, OCR-eligible route, low-confidence
   escalation, partial/empty extraction escalation, unsupported language or
   unsupported source blocking, deterministic repeatability, and no raw-content
   release.
2. Existing extraction-foundation tests pass.
3. Changed Python files compile.
4. New source/test files have GC-051 coverage if created.
5. Worker return includes pre-flight evidence, changed files, gates run,
   findings or N/A, claim boundary, public export disposition, and no-commit
   status.

## Evidence Requirements

Worker return must include:

- startup acknowledgement and `executionBaseHead`;
- actual changed file list from `git status --short`;
- source verification update for any changed source/test/registry path;
- focused tests and compile results;
- GC-051 result when registry files change;
- no OCR/provider/API-key execution evidence;
- no external Policy_Local mutation evidence;
- Finding-To-Governance Learning Disposition if findings, defects, risks, or
  quality gaps are recorded;
- claim boundary and public export disposition.

## Review Gate

Codex must reject or return the packet if it:

- imports external code or new dependencies;
- executes OCR, providers, retrieval, Policy_Local mutation, or EC/T12 release;
- creates a parallel quality report or parallel operator report stack;
- lacks focused tests for route decisions;
- omits GC-051 coverage for new source/test files;
- records closure-equivalent status before reviewer commit;
- uses non-ASCII without an explicit allowed exception.

## Pending-Return Gates

Because this work order is `WORKER_MUST_NOT_COMMIT`, Claude must run and record
working-tree-aware component gates before return:

| Gate | Command or evidence | Required result |
| --- | --- | --- |
| Execution anchor | `git rev-parse --short HEAD` before edits | `executionBaseHead=<hash>` |
| Pending worktree | `git status --short` | actual pending file list |
| Compile changed source | `python -m py_compile EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` or same-domain alternative | PASS |
| Focused tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py -q` | PASS |
| Extraction foundation tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q` | PASS or BLOCKED with command-backed reason |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS or expected pending-finality issue with reason |

Do not record `pre-closure PASS` before Codex commits the approved range.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_WORKER_RETURN_2026-06-12.md`
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`
- `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
- active session continuity files if Codex closes the tranche

pendingStatusTokensAllowedBeforeReview:
`COMPLETE_PENDING_REVIEW`, `IMPLEMENTATION_COMPLETE_PENDING_REVIEW`, `DRAFT`,
`HOLD_*`

forbiddenClosedEquivalentResidue: worker pending-return, not-executed,
pre-closure-not-run, expected-pending-finality, and dispatched-current-status
language must not remain as final current status in Codex closure artifacts.

predecessorClosureFactSource: stable EXA-T1 completion review and reviewer-fast
hardening completion, not mutable session state alone.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope component gate failures without asking the
operator. Ask only when the repair would require dependency installation, OCR
execution, provider/API-key use, public-sync, external Policy_Local mutation,
EC/T12 release, broad refactor, destructive action, or a claim-boundary change.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope implementation. Return to
operator through Codex only if the work would require dependency installation,
OCR execution, provider/API-key use, external Policy_Local mutation,
public-sync, EC/T12 release, destructive action, or a claim-boundary change.

## Allowed Scope

Allowed:

- create the scan route decision source/test files;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py`;
- use existing extraction foundation imports and dataclasses;
- update GC-051 for new source/test files;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`;
- create the worker return packet;
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_WORKER_RETURN_2026-06-12.md`;
- create the Codex completion review;
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`;
- close this work order and parent roadmap state;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`;
- `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`;
- record bounded findings and learning disposition if defects are found.

Forbidden:

- external code copy;
- dependency installation;
- OCR execution or provider call;
- automatic retry or provider fallback;
- Policy_Local mutation;
- EC activation, retrieval change, corpus ingestion, or T12 unlock;
- public-sync or readiness claim.

## Return-To-Orchestrator Conditions

Return blocked to Codex if:

- existing source owners cannot support the contract without broad refactor;
- route decisions require provider/OCR execution to be meaningful;
- new dependencies are needed;
- source/test files exceed governed maintainability thresholds;
- GC-051 coverage cannot be updated inside allowed scope;
- any required component gate fails outside allowed repair scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md` | reviewer-owned completion created | PASS |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | EXA-T2 closed bounded | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | EXA-T2 source/test rows added | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | EXA-T2 source/test quick-lookup rows added | PASS |
| External evidence digest | EXA-T1 source map | `sha256:e1bdc496a12c5d313098e7ee45166f0706a84162065bf71c24ca25b9decec603`; prior verification reused, no new external source read required | PASS |
| System loop interlock | N/A with reason: no loop mutation authorized | no interlock update required | N/A with reason |
| Session continuity | active session files | Codex-owned follow-up sync after material closure commit | N/A with reason |

## Closure Checklist

- [x] Worker return includes actual pending file list.
- [x] Focused tests pass.
- [x] Existing extraction-foundation tests pass or have a command-backed
  out-of-scope blocker.
- [x] Changed Python source compiles.
- [x] GC-051 coverage is updated if new source/test files are created.
- [x] No OCR/provider/API-key, Policy_Local, EC, retrieval, corpus ingestion,
  public-sync, or readiness claim is introduced.
- [x] Codex commits the approved range.
- [x] Codex runs pre-closure with a non-empty committed range before marking
  closure.

## Claim Boundary

This work order authorizes deterministic local scan-signal and route-decision
implementation only. It does not prove extraction accuracy, OCR quality,
provider behavior, Policy_Local readiness, EC activation, retrieval quality,
current-law status, production readiness, public readiness, release readiness,
memory reinjection, high-risk promotion, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation dispatch; public-sync is not authorized.
