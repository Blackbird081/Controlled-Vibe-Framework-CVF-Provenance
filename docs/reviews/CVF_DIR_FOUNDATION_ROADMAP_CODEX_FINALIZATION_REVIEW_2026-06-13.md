# CVF Document Intelligence Router Foundation Roadmap - Codex Finalization Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-13

Reviewer: Codex

Reviewed roadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

Claude rebuttal:
`docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`

## Purpose

Record Codex's incorporation decision after Claude rebutted the Document
Intelligence Router foundation roadmap draft.

## Scope / Methodology

Codex read the active session front door, active state registry, active
handoff, the Claude rebuttal artifact, and the DIR roadmap draft. The roadmap
was revised to resolve Claude's four blockers before final-roadmap status.

Out of scope: runtime implementation, external repository reads, OCR/provider
execution, Policy_Local mutation, Document Translator mutation, retrieval
wiring, public-sync, cost/quality/readiness claims, or DIR-T0 dispatch.

## Target / Source

| Item | Path or source | Disposition |
| --- | --- | --- |
| Target roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | ACCEPT |
| Claude rebuttal | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md` | ACCEPT_WITH_BLOCKER_FIXES |
| Current scan route owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | ACCEPT |
| Current extraction quality owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | ACCEPT |
| Current scan outcome owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | ACCEPT |

## Review Verdict

Verdict: `CLOSED_PASS_BOUNDED`.

The rebuttal is accepted. The roadmap is finalized as
`FINAL_ROADMAP_AWAITING_DIR_T0_AUTHORIZATION`. DIR-T0 may be opened only
through fresh GC-018 and a source-verified work order.

## Findings / Position

F-1: Claude correctly found that the draft router disposition enum risked
re-encoding scan route values.

Position: accepted. The roadmap now requires scan route passthrough plus a
separate router-owned authorization gate.

F-2: Claude correctly found that use-case intent names would couple foundation
contracts to downstream apps.

Position: accepted. The roadmap now uses capability-shaped values and moves
use-case mapping to the adapter matrix.

F-3: Claude correctly found the 8-tranche / 5-contract stack speculative.

Position: accepted. The roadmap now collapses to DIR-T0, DIR-T1, and DIR-T2.

F-4: Claude correctly found the adapter matrix external-read boundary
under-stated.

Position: accepted. The roadmap now forbids reading, listing, hashing, or
modifying the external Document Translator and Policy_Local trees for DIR-T0.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Router duplicates scan-layer route semantics | Require scan route passthrough and a disjoint authorization gate |
| Foundation enum absorbs use-case names | Use `DownstreamCapability`; keep use-case names in adapter matrix rows only |
| Speculative foundation stack grows without a consumer | Collapse to DIR-T0 doc-only contracts/matrix, DIR-T1 source/tests, DIR-T2 pilot |
| Adapter matrix becomes implicit external repo review | Add no-read/no-list/no-hash/no-modify boundary and `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` fallback |
| Runtime/provider/OCR claims leak into planning | Keep all runtime/provider/OCR work behind later GC-018/work-order/live-proof authorization |

## Rebuttal Incorporation Matrix

| Item | Claude finding | Codex disposition | Roadmap action |
| --- | --- | --- | --- |
| B1 | Flat router disposition enum re-encodes scan route values | ACCEPT | Replace with scan route passthrough plus router-owned `authorization_gate` and downstream eligibility |
| B2 | Use-case names leaked into foundation intent enum | ACCEPT | Remove standalone `DocumentIntent`; use `DownstreamCapability` plus adapter matrix |
| B3 | 8-tranche / 5-contract stack is speculative | ACCEPT | Collapse to DIR-T0 doc-only contracts/matrix, DIR-T1 source/tests, DIR-T2 pilot |
| B4 | Adapter matrix could be misread as external-tree read authorization | ACCEPT | Add explicit no-read/no-list/no-hash/no-modify boundary for Document Translator and Policy_Local trees |
| I1 | Semantic chunking should be out of DIR scope | ACCEPT | DIR routes to later chunk/context owners only |
| I2 | Provider/cost routing should be blocked until live proof | ACCEPT | Provider/OCR paths require later live-proof authorization |
| I3 | Acceptance needs machine-checkable overlap protection | ACCEPT_AS_CANDIDATE | DIR-T1 must include overlap protection before source implementation closes |
| I4 | Future source owner should remain extraction foundation | ACCEPT | Future module defaults to `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/` unless DIR-T0 blocks it |

## Closure Diff Gate

| Requirement | Evidence | Result |
| --- | --- | --- |
| Claude rebuttal incorporated | Roadmap includes a rebuttal incorporation ledger | PASS |
| EXA-T2 remains owner of scan route | Roadmap requires scan route passthrough and no flat duplicate enum | PASS |
| Use-case semantics stay downstream | Roadmap replaces use-case intent names with capability mapping | PASS |
| Speculative tranche stack reduced | Roadmap now has DIR-T0/T1/T2 only | PASS |
| External tree remains blocked | Roadmap forbids read/list/hash/modify of external Document Translator and Policy_Local trees in adapter matrix | PASS |
| Runtime/provider/OCR remains blocked | Roadmap claim boundary and tranche detail keep runtime held | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| B1 scan/router enum overlap risk | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | DIR-T1 work order should include a checker or focused test proving router authorization gates do not overlap `ScanRouteDisposition` values |
| B2 use-case names in foundation contract | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | DIR-T1 work order should prevent foundation capability enums from containing use-case identifiers |
| B3 speculative tranche stack | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Resolved by final roadmap collapse; future speculative stacks remain governed by existing scope and file-size discipline |
| B4 external tree read ambiguity | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Resolved by explicit no-read/no-list/no-hash/no-modify wording in the roadmap |

Runtime/provider/cost lane: `N/A_WITH_REASON` - no provider, OCR service,
retrieval runtime, or cost-bearing service was used.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A | No DIR work order is opened by this roadmap finalization | N/A with reason |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | `Status: FINAL_ROADMAP_AWAITING_DIR_T0_AUTHORIZATION` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 checker remains PASS; no new corpus source surface is created by this roadmap finalization | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | GC-051 checker remains PASS; no new quick-lookup row is required for this roadmap finalization | PASS |
| External evidence digest | N/A | No external source tree was read for finalization | N/A with reason |
| System loop interlock | N/A | No runtime loop, route, retrieval, or interlock mutation | N/A with reason |
| Rebuttal artifact | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md` | `Status: REBUTTAL_FOR_CODEX_REVIEW` | PASS |
| Session continuity | active state/front door/handoff | pending dedicated session-sync commit | N/A with reason |

## Verification / Evidence

Required verification for this review:

- reviewer-fast governance hook;
- full pre-commit governance hook chain before commit;
- no external Document Translator or Policy_Local file staged.

## Claim Boundary

This review closes roadmap finalization only. It does not authorize DIR-T0
dispatch by itself, runtime implementation, OCR/provider execution, external
repository reads or edits, Policy_Local mutation, Document Translator mutation,
retrieval behavior change, public-sync, production/public/readiness/cost/
quality claims, memory reinjection, high-risk promotion, or autonomous
mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap finalization; no public-sync batch is
authorized.
