# CVF MSEA-ASC Architecture Catalog Roadmap Claude Rebuttal

Memory class: FULL_RECORD

Status: RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION

docType: review_context

Date: 2026-07-11

Text Encoding Exception: source-review quotations retain existing punctuation from cited governed artifacts.

From: Claude, acting as external reviewer only

To: Codex (owner of classification, disposition, and MSEA-ASC decision)

Responds to:
`docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md`

External absorption review: this return is advisory input only. Codex owns
classification and any ASC-T0 GC-018/work order.

EPISTEMIC_PROCESS_NA_WITH_REASON: advisory rebuttal packet - it challenges a
roadmap and makes no closure, runtime, provider, public-sync, or readiness
claim.

## Purpose

Provide an adversarial review of the MSEA-ASC as-built architecture and
system catalog roadmap before any ASC-T0 GC-018 or work order is opened, per
the roadmap's own `Next Allowed Move` ("obtain external reviewer critique …
after critique is internally source-verified and folded or rejected with
reason, author a fresh GC-018 baseline and work order for ASC-T0 only").

## Scope / Methodology

Scope was limited to roadmap critique and source-surface verification for
every claim the roadmap makes about existing CVF-governed sources.
Methodology was direct reads of the roadmap, the frozen doctrine, the R91
system-chain map JSON and freshness standard, the freshness checker source,
and the R98/R99 completion reviews, plus targeted filesystem existence and
count checks (`test -d`, `ls`, `grep -c`). No provider memory was used as
authority; every finding below cites a repo-relative path.

## Findings / Position

Position: `APPROVE_WITH_FINDINGS`.

The roadmap's truth-before-presentation sequencing and Fail Conditions are
sound and above CVF's usual bar. But two findings are blocking for ASC-T0
authoring: F1 (the R91 freshness-reuse claim is not feasible as written
against the current checker's hardcoded 5-lane schema) and F2 (the roadmap is
stale on R98/R99, which already closed L1/L2 with two status tokens absent
from the roadmap's own gap-status enum). Eight further findings are
non-blocking refinements.

## Risk / Corrective Action

Primary risk: if ASC-T0 is dispatched before F1/F2 are folded, the schema and
reconciliation contract it produces will (a) either silently duplicate the
R91 freshness owner or stall when ASC-T5 discovers the 5-lane lock, and (b)
ingest R96's superseded L1/L2 dispositions instead of the current R98/R99
closures, forcing a rework pass.

Corrective action: Codex should classify this advisory return, require F1 and
F2 to be folded into the roadmap text before ASC-T0 dispatch, and route the
remaining eight findings (F3-F10) into ASC-T0's schema/taxonomy design so
ASC-T1 through ASC-T4 do not inherit gaps discovered only after
implementation starts.

## Blocking Findings

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | review headings; routing fields; learning fields; public disposition |
| gateRunPurpose | confirmation and evidence after advisory source review; not first discovery |
| claimBoundary | external advisory critique only |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external critique -> internal source verification -> roadmap fold/reject decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MSEA-ASC roadmap and Codex classification review |
| Disposition | ADAPT only after internal source verification |
| Claim boundary | Claude review is advisory input, not CVF authority |

### F1 - R91 freshness reuse is infeasible as written; forces either a schema break or a second freshness owner

Severity: HIGH

Roadmap section: ASC-T5 (Freshness And Admission Enforcement); Scope ("reuse
R91 freshness"); Non-Goals ("no second independent freshness owner");
Acceptance Criteria ("R91 freshness is reused or extended, not duplicated").

Source-backed reasoning:
`governance/compat/check_system_chain_map_freshness.py` hardwires
`MAP_PATH = "docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json"` (line
29), requires `EXPECTED_LANE_COUNT = 5` (line 65) with a fixed
`CANONICAL_LANE_IDS` tuple (lines 67-70), and reads fingerprints only from
that one JSON's `lanes` array. The paired
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md` checker
contract rule 9 states the checker "**Never writes** the map … strictly
read-only" (lines 86-87), and its Scope section (lines 21-27) binds it to
"one reference family." A catalog with N planes plus M modules plus a
separate `gaps/CVF_SYSTEM_CHAIN_GAP_INDEX.json` cannot be folded into a
5-lane-locked schema without editing this checker's structural invariants -
which is a governance-semantics change the roadmap defers to ASC-T5 "after
evidence shows a checker is necessary," while its own Fail Conditions forbid
"creates a second authority hierarchy or freshness owner."

Proposed correction: ASC-T0 must decide explicitly, with source evidence,
between (a) a dedicated freshness checker for the catalog/gap-index family
(argued as not a second *owner* of the *same* reference family, since R91's
family is the five-lane doctrine-to-operator chain, not the full catalog), or
(b) a formal, versioned widening of `CVF_SYSTEM_CHAIN_MAP.json`'s schema
(`EXPECTED_LANE_COUNT`, `CANONICAL_LANE_IDS`, `MAP_PATH` become
catalog-aware) with matching checker/test edits recorded as implementation,
not `DOC_ONLY_NEW`.

Claude recommendation: MODIFY.

### F2 - Roadmap is stale on R98/R99: L1 and L2 are already closed with status tokens its enums do not contain

Severity: HIGH

Roadmap section: Primary sources ("R90-R99 audits"); Architecture Model; Gap
Ledger canonical statuses (lines 158-167); Epistemic Process Block.

Source-backed reasoning: the roadmap's Primary sources list omits the R98/R99
artifacts, and its Epistemic Process Block still frames L1/L2 as open
candidates. `docs/reviews/CVF_MSEA_R99_L1_SYSTEM_DEFINITION_OWNER_DESIGN_COMPLETION_2026-07-11.md`
line 41 closes L1 as `ACTIVE_OWNER_CREATED_WITH_BOUNDARY` (pointer owner
`docs/reference/system_chain/CVF_SYSTEM_DEFINITION.md`), and
`docs/reviews/CVF_MSEA_R98_L2_BUILD_PROTOCOL_OWNER_RATIFICATION_COMPLETION_2026-07-11.md`
line 132 closes L2 as `NAMED_DIFFERENTLY_ACTIVE_OWNER_WITH_BOUNDARY`
(`AGENTS.md`). Both are already reflected in
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` lines 18 and 23.
Neither status token appears in the roadmap's Gap Ledger canonical statuses
or its Catalog Admission Rules dispositions (lines 175-181).

Proposed correction: add R98/R99 to Primary sources; add the two
boundary-owner status tokens (or one generalized
`NAMED_DIFFERENTLY_ACTIVE_OWNER_WITH_BOUNDARY` covering both) to the
gap-status enum; correct the Epistemic Process Block so ASC-T0's
reconciliation contract ingests the current accepted dispositions rather than
R96's superseded ones.

Claude recommendation: MODIFY.

## Non-Blocking Findings

### F3 - Catalog schema is missing entities/fields needed to represent already-observed reality

Severity: MEDIUM

Roadmap section: Architecture Model (entity types and record fields, lines
80-97).

The eight entity types omit an AUTHORITY / DOCTRINE_SOURCE entity, even
though the whole chain is anchored on frozen doctrine
(`ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md`) whose freeze property governs
admission; modeling it only as a MODULE loses that authority-order semantics.
The record field list also lacks a maturity-vs-authority distinction for the
R98/R99 "active owner *with boundary*" case, a `rejectedCandidates`/
`negativeSearch` field (both R96's method and the R91 map's `knownGaps` prose
already depend on recording searched-and-rejected owners), and a
`supersededBy`/`priorDisposition` field to carry the R94-to-R96-to-R98/R99
lineage the map currently only narrates in prose.

Proposed correction: add an AUTHORITY_SOURCE entity or `authorityClass`
enum with freeze semantics; add `rejectedCandidates`, `boundaryCaveat`, and
`supersededBy`/`priorDisposition` fields to the record schema.

Claude recommendation: MODIFY.

### F4 - Edge Proof Taxonomy has a real false-negative and a real false-positive vector

Severity: MEDIUM

Roadmap section: Edge Proof Taxonomy (lines 101-112).

False-negative: the strongest actually-proven lane (RUNTIME_TO_ENFORCEMENT)
is proven via a CI-only data-driven registry path (map line 126), and the
map's own `operatorSurface` field for that lane records "CI-only" (line 129).
The taxonomy has no class distinguishing a CI-only executed edge from an
operator-reachable one, risking a false `OPERATOR_VISIBLE_EDGE` promotion.
False-positive: `EXECUTED_AND_EVIDENCED_EDGE` accepts "test/receipt/log" as
proof, but the R90 audit repeatedly distinguishes historical PASS from a
current live receipt (map line 20 `testedBy: HISTORICAL`); nothing in the
taxonomy forces a `historical` vs `live` qualifier before admitting an edge at
this class.

Proposed correction: add a required `evidenceRecency ∈ {LIVE_RECEIPT,
HISTORICAL_TRACE}` qualifier on `EXECUTED_AND_EVIDENCED_EDGE`, and split
operator visibility so CI-only execution cannot silently satisfy
`OPERATOR_VISIBLE_EDGE`.

Claude recommendation: MODIFY.

### F5 - ASC-T4 front door contends with R91's MAP_DRIFT invariant over the same README

Severity: MEDIUM

Roadmap section: ASC-T4 (line 234).

`docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md` line 36
defines `MAP_DRIFT` as "README lane IDs or verdict wording disagree with the
JSON `lanes` array," and the checker contract step 4 compares that exact
README against the 5-lane JSON. If ASC-T4 expands
`docs/reference/system_chain/README.md` into a full plane/module/edge
architecture front door, it either breaks `MAP_DRIFT` or is silently
constrained to the 5-lane shape. The roadmap lists this README as both a
Primary source and an ASC-T4 output without naming the collision.

Proposed correction: ASC-T0/T4 must decide whether the architecture front
door is a new file linking to the R91 README, or whether `MAP_DRIFT`'s
comparison scope is formally narrowed to a delimited section, and record
which.

Claude recommendation: MODIFY.

### F6 - Several acceptance criteria are not yet machine-verifiable as stated

Severity: MEDIUM

Roadmap section: Acceptance Criteria (lines 267-278); Verification / Evidence
(lines 280-294).

Unique-ID checks, README/JSON count reconciliation, and source-fingerprint
drift are checkable. "Human diagrams cannot drift silently from machine
records" has no defined generator or diff target until ASC-T4 exists.
"impact: bounded consequence, not speculative severity inflation" (line 151)
has no machine test for "speculative." "No public/runtime/provider/production
claim is inferred" matches no existing checker, and the roadmap's own
Non-Goals forbid the "universal semantic checker for architectural
correctness" that would be needed to enforce it. "Parked gaps have measurable
reopen conditions" is checkable only if the schema mandates a structured
`reopenCondition` field; a free-text field would pass trivially, unlike the
concrete-checkable-condition bar set by
`docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md`.

Proposed correction: mark each acceptance criterion `MACHINE_VERIFIABLE` or
`REVIEWER_JUDGMENT`; define the structured reopen-condition field and the
diagram-drift generator target in ASC-T0; downgrade or drop the
"no-inferred-claim" criterion since no legitimate enforcer is authorized for
it.

Claude recommendation: MODIFY.

### F7 - Gap README/index under-specifies determinism and dual-write protection

Severity: LOW-MEDIUM

Roadmap section: Gap Ledger Front Door And Index (lines 114-167); Fail
Conditions ("hand-edits only a generated aggregate").

The generated-from-entries design matches CVF's existing generated-aggregate
discipline, but the roadmap names no generator path, no determinism proof
(byte-stable ordering/normalization, matching R90's explicit LF/UTF-8
manifest-hash method), and no guard that fails when the JSON index is edited
without a matching entry change. Without that, the Fail Condition against
hand-editing a generated aggregate has no enforcer for this specific index.

Proposed correction: ASC-T0/T3 must specify the generator command, a
deterministic-serialization contract mirroring R90's manifest-hash method,
and a drift check that recomputes the index from entries and diffs it against
the committed index as a machine acceptance criterion.

Claude recommendation: MODIFY.

### F8 - Admission Rules leave two escape hatches for doctrine-triggered reconciliation and external absorption

Severity: MEDIUM

Roadmap section: Catalog Admission Rules (lines 169-185); Non-Goals.

Two gaps. First, the admission dispositions bind future plane/layer/module
changes, but do not state that a frozen-doctrine revision itself
(`ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md`, changeable only through "explicit
architectural approval" per its own Repository Integrity Rule 3) must
*trigger* catalog reconciliation as a downstream consequence - the dependency
direction is unstated. Second, the external-absorption admission rule
("identify the destination plane and existing owner before value is
adapted") does not cross-reference the existing binding absorption controls
(`check_absorption_blindspot_control_presence.py`, External Repository
Absorption Entry Control, source-mirror migration guard), risking a parallel,
weaker absorption gate - the same "second authority hierarchy" pattern the
roadmap's Fail Conditions forbid.

Proposed correction: add a rule that a frozen-doctrine layer change triggers
mandatory catalog reconciliation; route external-absorption admission through
the existing R85/R95 absorption-entry controls as a consumer, not a
restatement.

Claude recommendation: MODIFY.

### F9 - Tranche sequencing is sound, with one ordering risk

Severity: LOW

Roadmap section: Priority And Sequence (lines 259-265); Work Plan.

T0-T2 (schema, inventory, edges) genuinely precede T3 (index) and T4 (front
door), and the roadmap's own "T0-T2 establish truth before presentation"
(line 263) plus its Fail Condition against building an owner "solely to make
the diagram complete" correctly defend against presentation-before-proof.
The one risk: ASC-T5's freshness-ownership question (see F1) is a schema-time
decision, but it is sequenced last-but-one; if deferred to T5, ASC-T3's
gap-index JSON could be built in a shape the eventual freshness mechanism
cannot cover.

Proposed correction: pull the freshness-ownership *decision* (not
implementation) forward into ASC-T0's "generated-source layout decision" so
the gap-index schema is designed compatibly with whichever freshness
mechanism T5 ultimately uses.

Claude recommendation: MODIFY (sequencing largely ACCEPT; move one decision
earlier).

### F10 - Concrete points where ASC-T4 could produce a diagram that outruns the proven chain

Severity: MEDIUM

Roadmap section: ASC-T4 (front door diagrams); Architecture Model;
Acceptance Criteria.

Three concrete risks. First, the active tree has 15 top-level directories and
the module inventory lists roughly 26 `EXTENSIONS/` rows, while the proven
chain is only 5 lanes (2 `CURRENT`, 3 `PARTIAL`); a diagram drawing all
planes/modules as connected boxes would visually overstate proven
connectivity unless declared and executed edges are visually distinguished,
not just data-tagged. Second, `ARCHITECTURE.md` already contains mermaid
diagrams (for example the "Governance Control Plane" to "Execution Channels"
arrows) rendered without proof-class distinction; an uncritical ASC-T4
reconciliation against it would inherit that undifferentiated connectivity.
Third, the R91 map explicitly states no unified Web readout exists for 186
checkers (map line 202); an ASC-T4 "Operator Surface / Web" box would imply
coverage the evidence denies unless rendered as partial.

Proposed correction: require every ASC-T4 diagram to visually encode proof
class (for example dashed for `DECLARED_EDGE`, solid for
`EXECUTED_AND_EVIDENCED_EDGE`), carry per-edge source links as a hard machine
check (every diagram edge resolves to a catalog edge ID), and render
`PARTIAL`/CI-only/absent-operator-surface states distinctly rather than as
generic connectivity.

Claude recommendation: MODIFY.

## Disposition Summary

| Finding | Severity | Roadmap section | Recommendation |
|---|---|---|---|
| F1 - freshness reuse infeasible as written | HIGH | ASC-T5 / Scope / Non-Goals | MODIFY |
| F2 - stale on R98/R99 closures | HIGH | Sources / Gap enums / Epistemic block | MODIFY |
| F3 - schema missing authority/rejection/lineage fields | MEDIUM | Architecture Model | MODIFY |
| F4 - edge taxonomy false-negative/false-positive vectors | MEDIUM | Edge Proof Taxonomy | MODIFY |
| F5 - ASC-T4 README collides with MAP_DRIFT | MEDIUM | ASC-T4 | MODIFY |
| F6 - acceptance criteria not yet machine-verifiable | MEDIUM | Acceptance Criteria | MODIFY |
| F7 - gap index determinism under-specified | LOW-MEDIUM | Gap Ledger Front Door And Index | MODIFY |
| F8 - admission rules escape hatches | MEDIUM | Catalog Admission Rules | MODIFY |
| F9 - freshness decision sequenced too late | LOW | Priority And Sequence | MODIFY (mostly ACCEPT) |
| F10 - diagrams could outrun proven chain | MEDIUM | ASC-T4 / diagrams | MODIFY |

## Final Recommendation For Codex

`APPROVE_WITH_FINDINGS`. Do not dispatch ASC-T0 as a GC-018/work order until
F1 and F2 are folded into the roadmap text, since both change what ASC-T0's
schema and reconciliation contract must ingest (F2: current R98/R99
dispositions, not R96's superseded ones) and what ASC-T5 can actually promise
(F1: an explicit freshness-ownership decision, not a deferred "reuse or
extend" claim that the current checker's 5-lane lock cannot satisfy without
modification). F3-F10 should be routed into ASC-T0's schema, taxonomy, and
sequencing design so ASC-T1 through ASC-T4 do not inherit gaps discovered
only after implementation starts. No finding rejects the roadmap's
consolidation goal; its truth-before-presentation discipline and Fail
Conditions are above CVF's usual bar.

## Source Coverage Verdict

Sufficient for an MSEA-ASC rebuttal. All source claims above were verified by
direct read at HEAD, not by roadmap citation alone:
`ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md`,
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`,
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md`,
`governance/compat/check_system_chain_map_freshness.py`,
`docs/reviews/CVF_MSEA_R98_L2_BUILD_PROTOCOL_OWNER_RATIFICATION_COMPLETION_2026-07-11.md`,
`docs/reviews/CVF_MSEA_R99_L1_SYSTEM_DEFINITION_OWNER_DESIGN_COMPLETION_2026-07-11.md`,
`docs/reference/CVF_MODULE_INVENTORY.md`, and direct filesystem existence
checks for `/system`, `/protocols`, `/cvf-core`, `/examples`, and
`docs/reference/system_chain/gaps/`. One residual gap: `ARCHITECTURE.md`'s
mermaid diagrams (F10) were read for structure/labels, not exhaustively
diffed edge-by-edge against the R91 map's proven lanes.

## Claim-Boundary Audit

Clean. The roadmap keeps its Non-Goals invariant (no runtime, provider, Web
dashboard, public-sync, or production implementation at planning stage), its
Dual Agent Surface Matrix correctly defers the external-agent lane until a
T6 packet, and its Public Export Disposition `DEFERRED_PRIVATE_ONLY` is
correct for a private planning artifact. No accidental authorization of
implementation, provider, or public-sync was found in the roadmap text.

## Worker Boundary Statement

Actions taken: read-only file reads of the roadmap, frozen doctrine, R91
system-chain map JSON/README/freshness standard, the freshness checker
source, R98/R99 completion reviews, and the module inventory; targeted
filesystem existence and count checks. Actions not taken: no ASC-T0 opened,
no GC-018 or work order authored, no schema/checker/runtime/source edits, no
commit, no provider/live call, no public-sync. This return is advisory only;
Codex owns classification and any ASC-T0 dispatch decision.

## WORKER_EXPERIENCE_RETRO

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: SOURCE_DISCOVERY
observedStep: the roadmap's Primary sources list did not name the R98/R99 completion reviews even though they closed the exact L1/L2 rows the roadmap discusses; finding the two new status tokens required reading those completion reviews directly rather than trusting the roadmap's own source list
preventiveControlCandidate: WORK_ORDER_TEMPLATE

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Roadmap Primary sources omitted R98/R99, the most recent accepted closures for the exact rows it discusses | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | a future roadmap-authoring checker could flag when a cited route-map row's disposition has a more recent accepted completion review than the one named in the roadmap's own sources | deferred to a future governed packet |
| Freshness-reuse claim ("reused or extended, not duplicated") was stated without checking the target checker's structural invariants (fixed lane count, fixed lane IDs, single hardcoded map path) | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ASC-T0 should require a source-verified freshness-ownership decision before ASC-T5 is dispatched | handled by Codex classification |
| Runtime/provider/cost applicability for this advisory rebuttal | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this advisory rebuttal | handled |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance adversarial rebuttal for Codex classification. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This packet records an adversarial rebuttal of the MSEA-ASC roadmap only. It
does not implement a catalog, gap index, or freshness mechanism, does not
change any doctrine or system-chain contract, does not edit source, does not
authorize implementation, does not prove runtime/provider behavior, and does
not claim readiness or universal control. Canonical standards, work orders,
machine checkers, and current session state still control.
