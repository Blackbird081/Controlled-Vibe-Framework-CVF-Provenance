# CVF Document Intelligence Router Foundation Roadmap - Claude Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FOR_CODEX_REVIEW

docType: review

Date: 2026-06-13

For: Codex (roadmap author, for confirmation or revision)

Authority: Independent adversarial review of
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`
(Status: DRAFT_FOR_CLAUDE_REBUTTAL)

Claim boundary: this artifact is a planning critique only. It does not prove
document intelligence behavior, authorize runtime/OCR/provider work, edit any
external repository, or claim production/public/cost/quality readiness. It
inherits every boundary of the draft it reviews.

---

## Purpose

Independent adversarial rebuttal of the DIR Foundation Roadmap draft before
finalization. Identifies blockers, proposes concrete contract-level fixes, and
records what the rebuttal agrees with so Codex can confirm or reject each point
before DIR-T0 opens.

## Scope

Reviewed source:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

Methodology: re-verified all 11 Source Verification rows against current
extraction foundation source; grepped for proposed router names; audited
`ExtractionQualityReport` field set as the deciding fact for tranche-collapse
decision; answered each of the 10 rebuttal questions in the draft.

Out of scope: runtime implementation, external repo reads, provider/OCR
execution, Policy_Local or Document Translator source inspection.

## Findings

Overall disposition: **ACCEPT with 4 blockers.** Source Verification 11/11
PASS. Claim-boundary discipline is sound. Four structural problems require
roadmap revision before DIR-T0 opens: disposition enum duplication (B1),
use-case semantics in foundation contract (B2), speculative 8-tranche stack
(B3), and under-stated external-read prohibition (B4). Detailed findings,
proposed contract shapes, and per-question ledger in Parts 1-5 below.

## Required Corrective

Codex must revise
`CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` to
incorporate or explicitly reject B1-B4 (with source-grounded reasoning for any
rejection) before advancing to FINAL_ROADMAP status and opening DIR-T0 with
a fresh GC-018. No implementation or dispatch is authorized until that
revision is complete.

---

## Executive Summary

Overall disposition: **ACCEPT with 4 blockers.**

The DIR draft is architecturally sound and source-honest. Its strongest
property is claim-boundary discipline; its biggest risk is **speculative
abstraction** - a 5-contract / 8-tranche stack proposed before any consumer
needs it. The duplication risk the draft worries about (Q1) is real but
narrow and fixable; the over-scoping risk (Q2, Q10) is the one that should
drive the revision.

Requested action: Codex reviews this rebuttal and for each item either
**confirms agreement** (and revises the draft) or **confirms disagreement**
with specific reasoning (we debate further). DIR-T0 should not open until B1-B4
are resolved in the final roadmap.

---

## Source Verification (independent)

I re-verified every row of the draft's Source Verification table (lines
128-140) against current source, plus the symbols the draft promises to
preserve.

| Claimed symbol | Source file | Cited line | Verify result |
| --- | --- | --- | --- |
| `SCAN_ROUTE_DECISION_VERSION` | `scan_route_decision.py` | 20 | PASS |
| `DocumentScanSignals` | `scan_route_decision.py` | 40 | PASS |
| `ScanRouteDecision` | `scan_route_decision.py` | 58 | PASS |
| `decide_scan_route` | `scan_route_decision.py` | 71 | PASS |
| `ExtractionStatus` | `extraction_pipeline.py` | 27 | PASS (Literal alias, not class) |
| `ExtractionQualityReport` | `extraction_pipeline.py` | 101 | PASS |
| `ExtractionStorageBoundary` | `extraction_pipeline.py` | 152 | PASS |
| `map_ocr_language_codes` | `extraction_pipeline.py` | 162 | PASS |
| `evaluate_extraction_quality` | `extraction_pipeline.py` | 235 | PASS |
| `ScanOutcomeReport` | `scan_outcome_report.py` | 43 | PASS |
| `build_scan_outcome_report` | `scan_outcome_report.py` | 131 | PASS |

Additional checks:

- `ScanRouteDisposition` literal values confirmed at `scan_route_decision.py:31-36`:
  `LOCAL_TEXT_EXTRACTION_RECOMMENDED`, `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED`,
  `ESCALATE_OR_ABSTAIN`, `BLOCKED_UNSUPPORTED`. The semantics the draft promises
  to preserve (lines 318-319) are real.
- Proposed router names (`DocumentProfile`, `DocumentIntent`,
  `DocumentStructureSignals`, `DocumentIntelligenceRouteDecision`,
  `DocumentIntelligenceReviewPacket`) exist **nowhere** in
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION`. The `PROPOSED` labels (lines 187-195)
  are honest - no collision, no falsely-cited runtime field.

**Result: rebuttal questions 1 (source) and 6 -> satisfied. No source owner is
missing from the table.**

---

## Part 1 - What Codex Got Right (preserve in any revision)

1. **Claim-boundary discipline is excellent.** The no-runtime boundary is
   repeated in Scope, Non-Goals, Design Gate, every tranche, Dispatch Boundary,
   and Claim Boundary. DIR-T6/T7 are correctly gated behind fresh GC-018. I
   found **no language that accidentally authorizes** OCR, provider calls,
   retrieval, external-repo edits, or Policy_Local mutation (Q4 -> clean).
2. **Composition intent over duplication is stated and source-true.** Line 155
   forbids a parallel extraction confidence stack; the Foundation Relationship
   table (lines 146-151) correctly assigns scan-truth to the existing layer.
3. **PROPOSED fields are labeled PROPOSED.** No speculative field is cited as an
   existing runtime fact (Q5 acceptance criterion -> met).
4. **Rebuttal gate exists before finalization.** Intellectually honest;
   DIR-T0 explicitly waits on incorporated critique.
5. **Use cases declared downstream.** Design Gate rule 5 and Non-Goals keep
   Policy_Local / Document Translator as adapter consumers (the *intent* is
   right; B2 below is where the *implementation* leaks).

These should survive the revision unchanged.

---

## Part 2 - Blockers (must resolve before DIR-T0 opens)

### B1 - Router disposition enum re-encodes scan disposition (Q1)

**Disagreement with draft as written.** DIR-T3 dispositions (lines 309-314)
include `OCR_ELIGIBLE_BUT_NOT_AUTHORIZED` and `ABSTAIN_INSUFFICIENT_EVIDENCE`.
The scan layer already owns `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` and
`ESCALATE_OR_ABSTAIN` (`scan_route_decision.py:31-36`). A flat router enum that
re-encodes these is the second confidence stack line 155 forbids - just spelled
differently.

**My solution: replace the flat enum with a composition decision of three
independent axes.** The router owns exactly one new axis (authorization); it
passes scan disposition through verbatim and adds downstream eligibility.

```python
# Axis 1: scan disposition - imported verbatim, NOT redefined
#   scan_route: ScanRouteDisposition   (from scan_route_decision.py)

# Axis 2: the ONLY new axis the router is allowed to own - execution authority
AuthorizationGate = Literal[
    "LOCAL_DETERMINISTIC_ALLOWED",       # local logic only, no OCR/provider
    "OCR_REQUIRES_SEPARATE_AUTH",        # scan says OCR-eligible, no live-proof WO yet
    "PROVIDER_REQUIRES_SEPARATE_AUTH",   # provider needed, not authorized
    "OPERATOR_REVIEW_REQUIRED",          # router cannot self-decide
    "BLOCKED",                           # scan already blocked
]

# Axis 3: which downstream capability may receive the handoff (capability, not app name)

@dataclass(frozen=True)
class DocumentIntelligenceRouteDecision:
    decision_version: str
    scan_route: ScanRouteDisposition         # PASSTHROUGH - never modified
    authorization_gate: AuthorizationGate     # the only new axis
    downstream_eligibility: tuple[str, ...]
    operator_action: str
    scan_decision_digest: str                # sha256 of source ScanRouteDecision
    claim_boundary: str
```

Deterministic derivation table (no new confidence logic - a total map from 4
scan values to gate):

| Source `scan_route` | Derived `authorization_gate` |
| --- | --- |
| `LOCAL_TEXT_EXTRACTION_RECOMMENDED` | `LOCAL_DETERMINISTIC_ALLOWED` |
| `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` | `OCR_REQUIRES_SEPARATE_AUTH` |
| `ESCALATE_OR_ABSTAIN` | `OPERATOR_REVIEW_REQUIRED` |
| `BLOCKED_UNSUPPORTED` | `BLOCKED` |

The router never upgrades `scan_route`; it only maps one-way. This is what makes
it "compose, not duplicate" - provable because the table is a total function
from the 4 scan values.

### B2 - DIR-T1 `DocumentIntent` lets a use case define foundation semantics (Q2, Q5)

**Disagreement with draft as written.** The DIR-T1 intent values (lines
254-259) `TRANSLATION_PREP` and `POLICY_EVIDENCE_REVIEW` are use-case names
baked into a foundation contract. This contradicts the draft's own Design Gate
rule 5 (line 178: use cases are adapter consumers, not router owners). Adding a
new use case would force a foundation-enum edit - the exact coupling the draft
says it forbids.

**My solution: split into two layers. The foundation enum holds only
capability shapes; the use-case mapping lives in the adapter matrix.**

```python
# FOUNDATION (DIR-T1) - capability shape only, no app names
DownstreamCapability = Literal[
    "STRUCTURED_TEXT_HANDOFF",
    "EVIDENCE_CITATION_HANDOFF",
    "CORPUS_SCAN_HANDOFF",
    "OPERATOR_REVIEW_ONLY",
    "ABSTAIN_OR_BLOCK",
]
```

Use-case -> capability mapping lives in the adapter matrix, NOT in the enum:

| Use-case lane | Required capability | Defined where |
| --- | --- | --- |
| Document Translator DT-CVF | `STRUCTURED_TEXT_HANDOFF` | adapter matrix |
| Policy_Local PL-S | `EVIDENCE_CITATION_HANDOFF` | adapter matrix |
| Corpus intelligence | `CORPUS_SCAN_HANDOFF` | adapter matrix |

A new use case becomes one matrix row, foundation contract untouched. This is a
hard blocker, not a preference - the draft cannot both forbid (rule 5) and
encode (DIR-T1) use-case semantics in foundation.

### B3 - 8-tranche / 5-contract stack is speculative; collapse it (Q2, Q10)

**Agreement with my own initial critique, but the corrective is decided by
audit below, not by a flat "collapse everything."** Nothing today consumes a
`DocumentIntelligenceRouteDecision`. Eight tranches and five contract families
before a single live consumer is a speculative stack.

The decision of *how far* to collapse turned on one audited fact:

**Audit finding (source-verified):** `ExtractionQualityReport`
(`extraction_pipeline.py:101-113`) contains 10 fields - all quality/coverage
(`page_coverage_ratio`, `mean_ocr_confidence`, `pages_with_output`,
`thresholds`, ...) and **zero structure fields**. `DocumentScanSignals`
(`scan_route_decision.py:40-54`) likewise has zero structure fields. The scan
layer knows extraction *quality*; it knows nothing about document *shape*
(tables, images, formulas, layout risk).

| Concept | Varies by use case? | Overlaps scan layer? | Verdict |
| --- | --- | --- | --- |
| intent | YES (it *is* the use case) | no | gap, **collapse into profile field** |
| structure | NO (intrinsic to artifact) | no (scan has 0 structure fields) | gap, **keep as own contract** |
| quality/coverage | no | YES (owned by scan) | **do not redefine - reuse** |

**My solution (the optimal one I selected on operator instruction to audit and
choose):** collapse intent, keep structure separate.

```python
@dataclass(frozen=True)
class DocumentProfile:
    # metadata (genuinely new)
    source_artifact_id: str
    source_hash: str
    source_type: str
    language_hints: tuple[str, ...]
    page_count: int
    declared_artifact_role: str
    domain_hint: str
    # intent collapsed to ONE field (capability-shaped, per B2)
    requested_capability: DownstreamCapability

@dataclass(frozen=True)
class DocumentStructureSignals:
    # kept separate - scan layer has none of these; parallel input to router
    has_tables: bool
    has_images: bool
    has_formulas: bool
    layout_preservation_risk: Literal["LOW", "MEDIUM", "HIGH"]
    # MUST NOT redefine coverage/confidence - reuse ExtractionQualityReport
    # via a `from_quality_report()` constructor that pulls scan-owned coverage
```

Why intent collapses but structure does not (this reverses my own first-pass
"collapse everything" suggestion):

1. **Intent varies by use case** -> must not be its own foundation family, or
   B2 reappears. One field, capability-typed, mapping in the matrix.
2. **Structure is intrinsic and parallel to scan, not inside it.**
   `DocumentScanSignals` (quality) and `DocumentStructureSignals` (shape) are
   two peer inputs to the router. Folding shape into `DocumentProfile`
   (metadata + intent) would mix three concerns in one dataclass and make it
   hard for the router to reason "scan quality good but layout risk high."
3. **Structure must map to `ExtractionQualityReport`** (draft line 287). A
   dedicated dataclass with a `from_quality_report()` constructor makes that
   relationship explicit, instead of scattering scan-derived fields through the
   profile.
4. **Structure is the one thing likely to grow** (multi-column, footnotes,
   table complexity) once a pilot runs. A separate dataclass absorbs growth
   without bloating `DocumentProfile`.

Resulting stack: **3 contract families** (`DocumentProfile` with an intent
field, `DocumentStructureSignals` separate, `DocumentIntelligenceRouteDecision`)
- down from 5, and **3 tranches** instead of 8:

| New tranche | Replaces draft | Content |
| --- | --- | --- |
| DIR-T0 | old T0-T5 | collision ledger + 3 contracts + adapter matrix as a table |
| DIR-T1 (needs fresh GC-018) | old T6 | `document_intelligence_router.py` + focused tests |
| DIR-T2 (needs separate auth) | old T7 | bounded local/live pilot |

Structure stays at status `KEEP_SEPARATE_BUT_COLLAPSIBLE_AT_T1`: if, when
writing T1 tests, `DocumentStructureSignals` shows no independent variation, T1
may fold it into a profile field. I will not pre-commit that collapse at design
time without the test evidence.

### B4 - DIR-T5 readiness matrix risks reading the external use-case trees (Q5)

**Agreement with the draft's intent, disagreement that it is stated strongly
enough.** Out-of-scope (lines 68-69) forbids editing
`...\Document_Translator` and Policy_Local, but DIR-T5 (now a table in T0) does
not restate it, so a future worker could read "readiness matrix" as license to
inspect those trees.

**My solution: exact wording to insert into the adapter matrix tranche.**

> The adapter eligibility matrix references only the **already-published
> contract names** of each lane (for example, the capability DT-CVF declares it
> requires). This tranche does **not read, list, hash, or modify** any file
> under `D:\...\CVF-Workspace\Document_Translator` or the Policy_Local source
> tree. If a capability is not yet published by that lane, the matrix row records
> `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` - it is never inferred from external
> source.

---

## Part 3 - Improvements (non-blocking)

| Ref | Draft question | My disposition |
| --- | --- | --- |
| I1 | Q7 - semantic chunking earlier/later/out? | **Out of DIR scope.** DIR routes *to* a chunker; it does not chunk. Adding it re-triggers B3. |
| I2 | Q8 - cost/provider advisory forever, or blocked until live-proof? | **Blocked until live-proof, not advisory-forever.** Encode as `PROVIDER_REQUIRES_SEPARATE_AUTH` (B1 axis 2). State it explicitly so it is not read as permanent. |
| I3 | Q9 - acceptance machine-checkable enough? | **Not yet.** Most acceptance bullets are prose. Add the B1 overlap checker (below). |
| I4 | DIR-T0 package decision (line 222) | **New module inside `CVF_EXTRACTION_FOUNDATION/src/`, not a new package.** The router composes three modules in that package; a separate package would invert the dependency. |

### I3 detail - the machine check that enforces B1

```python
# governance/compat/check_dir_disposition_no_scan_overlap.py
# FAIL if any AuthorizationGate value also appears in ScanRouteDisposition.
from scan_route_decision import ScanRouteDisposition   # scan-owned
# AuthorizationGate from the router module

scan_values = set(literal_args(ScanRouteDisposition))
gate_values = set(literal_args(AuthorizationGate))
overlap = scan_values & gate_values
assert not overlap, f"Router gate re-encodes scan disposition: {overlap}"
# Must PASS: the two sets are fully disjoint (gate = authority, scan = quality)
```

Wire into the local hook chain like other `governance/compat/` checkers. This
turns B1 from a prose rule into a phase gate, per the agent-error-to-governance
philosophy.

---

## Part 4 - Per-Question Disposition Ledger

| Q | Draft rebuttal question | Disposition |
| --- | --- | --- |
| 1 | Does the router duplicate EXA-T2 routing? | **PARTIAL DUPLICATION at the disposition enum** -> B1. Composition elsewhere is sound. |
| 2 | Are profile/intent/structure scoped too broadly? | **YES for intent (B2), YES for the tranche count (B3).** Structure scope is correct. |
| 3 | Which tranche is doc-only vs source/test? | T0 doc-only; T1 source+test (fresh GC-018); T2 pilot (separate auth). |
| 4 | Does any language accidentally authorize OCR/provider/etc? | **NO.** Clean. |
| 5 | Are use cases sufficiently isolated? | **Intent isolation leaks (B2); matrix read-boundary under-stated (B4).** Otherwise yes. |
| 6 | Any current owner missing from Source table? | **NO.** All 11 rows verified; no missing owner. |
| 7 | Semantic chunking earlier/later/out? | **Out of scope (I1).** |
| 8 | Cost/provider advisory forever or blocked-until-proof? | **Blocked until live-proof (I2).** |
| 9 | Acceptance machine-checkable enough? | **Not yet (I3)** - add the overlap checker. |
| 10 | Smallest useful DIR-T0? | 3 contracts + matrix table in one T0 (B3), not an 8-tranche design pass. |

---

## Part 5 - Recommended Final-Roadmap Edits

1. **DIR-T3:** rewrite dispositions as the 3-axis composition (B1); add the
   overlap checker (I3).
2. **DIR-T1:** recast intent values as `DownstreamCapability`; move
   use-case mapping to the adapter matrix (B2).
3. **Tranche plan:** collapse old T0-T5 into one DIR-T0; old T6 -> DIR-T1
   (fresh GC-018), old T7 -> DIR-T2 (separate auth) (B3). Fold `DocumentIntent`
   into a `DocumentProfile` field; keep `DocumentStructureSignals` separate at
   `KEEP_SEPARATE_BUT_COLLAPSIBLE_AT_T1`.
4. **Adapter matrix:** insert the no-external-read restatement (B4).
5. **DIR-T0 package deliverable:** recommend a new module inside
   `CVF_EXTRACTION_FOUNDATION/src/` (I4).

---

## Part 6 - Boundaries I Will Not Move (for the debate)

These are not preferences; moving them breaks ownership or the draft's own
rules:

- **Intent must collapse** (B2): foundation cannot both forbid and encode
  use-case semantics.
- **Structure must not collapse into the scan layer**: the scan layer has zero
  structure fields (source-verified); shape is not a scan concern.
- **Quality/coverage must not be redefined**: it is scan-owned
  (`ExtractionQualityReport`); the router reuses it.

The only genuinely open design question is *structure as its own dataclass vs a
profile field* - and I resolved it to "separate, collapsible at T1 on test
evidence." That single point is the most reasonable thing for Codex to push
back on.

---

## Action Requested

Codex, for each of B1-B4 and I1-I4, either:

- **Confirm agreement** and revise
  `CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`
  accordingly, then advance to FINAL_ROADMAP -> fresh GC-018 for DIR-T0; or
- **Confirm disagreement** with specific source-grounded reasoning, and we
  debate the open point (structure dataclass vs profile field) further.

DIR-T0 should not open until B1-B4 are incorporated or explicitly rejected with
reasons.

---

## Verification / Evidence

- Re-read `CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`
  (full) for the draft under review.
- Re-verified all 11 Source Verification rows against
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`,
  `extraction_pipeline.py`, and `scan_outcome_report.py` (lines cited in the
  table above).
- Confirmed `ScanRouteDisposition` values (`scan_route_decision.py:31-36`) and
  `ExtractionQualityReport` fields (`extraction_pipeline.py:101-113`) - the
  audit fact behind B3.
- Grep confirmed the 5 proposed router names exist nowhere in
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` (no collision; PROPOSED labels honest).

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| B1 - router disposition enum re-encodes scan layer | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Draft forbids a parallel confidence stack (line 155) in prose; if this recurs, promote the B1 overlap-grep checker (I3 in this review) to a pre-commit gate that diffs new disposition enums against existing scan-layer Literals |
| B2 - use-case names baked into foundation enum | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Design Gate rule 5 exists but is prose; if a future agent violates it again, promote to an import-graph check that fails when a foundation contract imports use-case identifiers |
| B3 - 8-tranche speculative stack before live consumer | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | CVF GC-023 and tranche-size governance already bound scope; Codex should cite these explicitly when approving future foundation roadmaps with no live consumer |
| B4 - external-tree read boundary under-stated | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Out-of-scope section already exists; wording supplied in B4 fix; no new rule needed |

Runtime/provider/cost lane: `N/A_WITH_REASON` - no provider, OCR service,
retrieval runtime, or cost-bearing service was used in this rebuttal.

## Claim Boundary

This rebuttal proposes contract shapes and tranche structure for critique. It
does not prove document intelligence behavior, extraction accuracy, OCR/provider
behavior, routing correctness, Policy_Local or Document Translator readiness,
public/production/release readiness, or cost/quality. No source implementation,
external-repo edit, or dispatch is authorized by this artifact.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance rebuttal for Codex review; no public-sync batch is
authorized.
