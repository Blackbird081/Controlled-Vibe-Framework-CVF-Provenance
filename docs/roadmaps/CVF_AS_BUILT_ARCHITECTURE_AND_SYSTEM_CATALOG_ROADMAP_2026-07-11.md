# CVF As-Built Architecture And System Catalog Roadmap

Memory class: FULL_RECORD

Status: PROPOSED

Date: 2026-07-11

Roadmap ID: MSEA-ASC

## Purpose

Convert the source-backed R90-R99 system-chain reconstruction into one durable
as-built architecture control surface. Future contributors and agents must be
able to determine what CVF contains, who owns each responsibility, how planes
connect, which edges execute, where evidence is retained, and which gaps are
open without reconstructing the answer from historical reviews.

## Target / Source

Target: a human-readable architecture front door, machine-readable system
catalog, indexed gap ledger, deterministic validation/freshness controls, and
governed admission rules for new layers, modules, mappings, and absorbed value.

Primary sources:

- `docs/reference/system_chain/README.md`
- `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`
- `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md`
- `docs/reference/system_chain/CVF_SYSTEM_DEFINITION.md`
- `docs/reference/CVF_MODULE_INVENTORY.md`
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `ARCHITECTURE.md`
- R90-R99 audits, reviews, and closure evidence.

## Authorization / Decision

This roadmap is planning authority only. Each implementation tranche requires
a fresh GC-018 baseline and work order. The operator authorizes detailed
roadmap authoring and external reviewer critique, not implementation, public
export, runtime mutation, or automatic semantic rewriting.

## Scope

In scope:

- model the repository's current as-built planes, modules, owners, interfaces,
  execution edges, enforcement, evidence, operator surfaces, and maturity;
- distinguish declared, implemented, and executed/evidenced edges;
- create a stable `README.md` front door and machine index for gap retrieval;
- define terminal gap status and measurable close/reopen conditions;
- bind new module/layer/absorption admission to catalog reconciliation;
- reuse R91 freshness rather than create competing freshness semantics;
- provide generated human projections where deterministic generation adds
  value, while preserving reviewable source records.

## Non-Goals

- no L4 promotion without its parked evidence trigger;
- no runtime, provider, Web dashboard, public-sync, or release implementation;
- no automatic claim that file existence proves execution;
- no replacement of frozen doctrine, `ARCHITECTURE.md`, module inventory, or
  control matrix;
- no import of legacy/external prose as authority;
- no universal semantic checker for architectural correctness;
- no second independent freshness owner.

## Design Control Gate

Before any tranche is dispatched, its packet must source-verify existing paths,
fields, enums, owners, and interfaces. New catalog fields must be declared as
DOC_ONLY_NEW until implemented. A tranche stops if it needs runtime mutation,
new governance semantics, public export, or an authority decision not granted
by its packet.

The architecture catalog is a control surface, not a presentation artifact.
Every accepted edge must carry an evidence class and every gap must carry a
terminal status plus owner/action conditions.

## Architecture Model

The catalog must represent at least these entity types:

| Entity | Required meaning |
|---|---|
| PLANE | responsibility domain in the actual system chain |
| MODULE | bounded implementation, governance, evidence, or operator owner |
| INTERFACE | contract, schema, registry, command, API, file protocol, or handoff boundary |
| EDGE | directed relationship between owners or planes |
| CONTROL | blocking, advisory, informational, or documentation-only enforcement |
| EVIDENCE_OWNER | receipt, test, audit, log, ledger, or review surface |
| OPERATOR_SURFACE | where a human discovers, invokes, or interprets the result |
| GAP | missing, partial, intentionally separated, parked, or unresolved connection |

Each catalog record must include stable ID, name, type, plane, owner paths,
status/maturity, authority class, inbound/outbound edges, evidence citations,
operator route, claim boundary, freshness inputs, and last-reviewed evidence.

## Edge Proof Taxonomy

| Edge class | Minimum proof | Allowed claim |
|---|---|---|
| DECLARED_EDGE | current doctrine, contract, architecture, or registry declaration | intended relationship only |
| IMPLEMENTED_EDGE | source implementation plus owning symbol/path | implementation exists; invocation unproven |
| INVOKED_EDGE | source-backed caller, scenario, hook, workflow, or parameterized registry route | execution path exists |
| EXECUTED_AND_EVIDENCED_EDGE | invocation plus test/receipt/log and evidence owner | bounded operational connection |
| OPERATOR_VISIBLE_EDGE | executed/evidenced result plus discoverable operator surface | bounded end-to-end visible connection |
| INTENTIONAL_SEPARATION | authority-backed reason and prohibited inference | separation is deliberate, not an untracked gap |

No lower class may be silently promoted to a higher class. Capability is not
invocation; file existence is not connection; historical PASS is not a current
live receipt.

## Gap Ledger Front Door And Index

The gap system must be easy to inspect without opening every audit.

Planned stable front door:

`docs/reference/system_chain/gaps/README.md`

Planned machine index:

`docs/reference/system_chain/gaps/CVF_SYSTEM_CHAIN_GAP_INDEX.json`

Planned compact source records:

`docs/reference/system_chain/gaps/entries/`

The README must provide:

- counts by plane, severity, status, and edge class;
- tables for open, parked, intentionally separated, and recently closed gaps;
- direct links to entry, owner, evidence, roadmap/work order, and next action;
- search examples by `gapId`, plane, owner, status, and reopen trigger;
- vocabulary and rules for adding/updating an entry;
- a clear statement that historical reviews are evidence, not the active index.

The machine index must be generated from compact source entries rather than
hand-edited as a monolith. Each entry requires:

| Field | Requirement |
|---|---|
| gapId | stable unique identifier |
| sourcePlane / targetPlane | directed location in the chain |
| sourceOwner / targetOwner | current governed paths or explicit NONE_WITH_REASON |
| missingEdge | exact absent or partial relationship |
| currentStatus | canonical terminal status |
| proofClass | highest currently proven edge class |
| evidence | file/symbol/command-backed citations |
| impact | bounded consequence, not speculative severity inflation |
| closeCondition | measurable evidence required to close |
| reopenCondition | measurable trigger for a parked/closed gap |
| actionOwner | roadmap, tranche, role, or PARKED_WITH_REASON |
| freshnessInputs | files whose drift requires review |
| lastReviewed | date and accepted review artifact |

Canonical initial statuses:

- `OPEN_CONFIRMED_GAP`
- `PARTIAL_CHAIN_WITH_BOUNDARY`
- `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE`
- `IMPLEMENTED_NOT_INVOCATION_PROVEN`
- `EVIDENCED_NOT_OPERATOR_VISIBLE`
- `INTENTIONAL_SEPARATION_WITH_REASON`
- `VALUE_PARKED_WITH_REOPEN_CONDITIONS`
- `CLOSED_WITH_EVIDENCE`

## Catalog Admission Rules

Any future change that adds or materially remaps a plane, layer, module,
interface, execution edge, evidence owner, operator surface, or absorbed owner
must include a catalog disposition:

- `ENRICH_EXISTING_OWNER`
- `NEW_OWNER_JUSTIFIED`
- `REFERENCE_ONLY`
- `IMPLEMENTATION_CANDIDATE`
- `INTENTIONAL_SEPARATION`
- `DUPLICATE_REJECTED`
- `VALUE_PARKED_WITH_REOPEN_CONDITIONS`

External absorption must identify the destination plane and existing owner
before value is adapted. `NEW_OWNER_JUSTIFIED` requires overlap evidence,
interface mapping, authority boundary, evidence route, and freshness ownership.

## Work Plan

### ASC-T0 - Source Schema And Reconciliation Contract

Deliver:

- catalog schema and field vocabulary;
- stable IDs and authority/maturity enums;
- reconciliation rules against system map, module inventory, control matrix,
  doctrine route map, and gap index;
- generated-source layout decision;
- bounded migration plan from R90-R99 evidence.

Exit: schema is human-reviewable, machine-parseable, and rejects proof-class
inflation.

### ASC-T1 - As-Built Plane And Module Inventory

Inventory all active top-level architectural planes and material owner modules.
For each, record responsibility, authority, maturity, interfaces, evidence, and
operator route. Historical/legacy material may support provenance but cannot
become an active owner without a separate decision.

Exit: every in-scope owner is terminally cataloged or explicitly excluded with
reason; counts reconcile with the canonical module inventory.

### ASC-T2 - Interface And Edge Graph

Trace plane-to-plane and owner-to-owner edges. Assign the highest proven edge
class only after caller/registry/workflow/test/evidence verification. Sampled
claims must remain marked sampled; no aggregate connected claim from partial
rows.

Exit: every cataloged owner has dispositioned inbound/outbound edges or an
explicit terminal isolation reason.

### ASC-T3 - Indexed System-Chain Gap Ledger

Create the `gaps/README.md`, compact entry records, generator, JSON index, and
initial migration of active R90-R99 gaps. Include L4 as
`VALUE_PARKED_WITH_REOPEN_CONDITIONS`, not an implementation task.

Exit: every active gap is retrievable by ID, plane, owner, status, proof class,
and trigger; README/index/entries reconcile deterministically.

### ASC-T4 - Human As-Built Architecture Front Door

Reconcile `docs/reference/system_chain/README.md` as the human architecture
front door. Add the smallest useful diagrams/tables generated or checked
against the catalog. Show planes, direction, proven edge class, gaps, and
operator/evidence routes. Avoid decorative diagrams without source links.

Exit: a new contributor can answer owner, edge, evidence, gap, and next-action
questions using the front door and direct links.

### ASC-T5 - Freshness And Admission Enforcement

Extend or reuse the R91 freshness mechanism so catalog sources, projections,
and gap index drift are detected. Add admission checks only after the catalog
shape stabilizes and evidence shows a checker is necessary. Prefer extending
an existing guard to creating a parallel checker.

Exit: changed governed owners cannot silently leave stale catalog/gap claims;
no automatic semantic verdict rewrite occurs.

### ASC-T6 - Independent Review And Closure

An external reviewer may critique coverage, proof taxonomy, false equivalence,
gap terminality, and usability. The internal reviewer must re-verify every
accepted criticism against CVF-governed sources. Close only after reconciliation
counts, deterministic generation, freshness, and retrieval tests pass.

## Priority And Sequence

`T0 -> T1 -> T2 -> T3 -> T4 -> T5 -> T6`

T0-T2 establish truth before presentation. T3 implements the operator-requested
README/index retrieval surface. T4 projects the verified catalog. T5 hardens
maintenance only after stable evidence. T6 challenges the integrated result.

## Acceptance Criteria

- One machine catalog is the source for as-built plane/module/edge records.
- One human front door routes to catalog, gaps, evidence, and operator surfaces.
- Gap README and JSON index reconcile with compact source entries.
- Every edge has exactly one highest proven proof class.
- Every gap has terminal status, evidence, close condition, and action owner.
- Parked gaps have measurable reopen conditions.
- New layer/module/absorption work has an explicit catalog disposition.
- R91 freshness is reused or extended, not duplicated.
- Human diagrams cannot drift silently from machine records.
- No public, runtime, provider, or production claim is inferred.

## Verification / Evidence

Expected tranche evidence includes deterministic generation/drift checks,
schema validation, unique-ID checks, owner/path resolution, edge citation
validation, README/index count reconciliation, retrieval queries, source
fingerprints, changed-range governance gates, and adversarial review records.

Representative retrieval tests:

- find all gaps from Contract to Runtime;
- find all `IMPLEMENTED_NOT_INVOCATION_PROVEN` edges;
- find owner and operator surface for a module;
- find every parked item whose reopen condition is now satisfied;
- find absorbed values admitted as `NEW_OWNER_JUSTIFIED`;
- trace a control from doctrine/contract to evidence/operator surface.

## Roadmap-To-Work-Order Trace Matrix

| Tranche | Fresh packet required | Primary output | Dependency |
|---|---|---|---|
| ASC-T0 | yes | schema and reconciliation contract | roadmap accepted |
| ASC-T1 | yes | as-built plane/module inventory | T0 accepted |
| ASC-T2 | yes | interface and edge graph | T1 accepted |
| ASC-T3 | yes | gap README, entries, generator, JSON index | T2 accepted |
| ASC-T4 | yes | human architecture front door | T2 and T3 accepted |
| ASC-T5 | yes | freshness/admission enforcement | T0-T4 stable |
| ASC-T6 | yes | independent critique and closure | T0-T5 terminal |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | dispatcher, worker, reviewer, closer | governed packets, source tree, gates | CVF-governed sources control | citations, ledgers, deterministic checks | ALLOWED_WITH_FRESH_PACKET |
| EXTERNAL_AGENT_CLI_MCP | optional critic | bounded roadmap/catalog evidence packet | advisory only; no mutation authority | dissent with source references re-verified internally | DEFERRED_UNTIL_T6_PACKET |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | `Status:`; `Design Control Gate`; `Work Plan`; `Acceptance Criteria`; `Verification / Evidence`; `Roadmap-To-Work-Order Trace Matrix`; `Public Export Disposition`; `PROPOSED` |
| gateRunPurpose | confirmation and evidence after source-backed roadmap design; not first discovery |
| claimBoundary | roadmap planning only; no implementation or closure claim |

## Epistemic Process Block

### Expected Result / Prediction

R90-R99 evidence is sufficient to define the catalog model and initial gap
vocabulary, but not sufficient to claim all modules and edges are already
inventoried.

### Evidence Comparison

The current five-lane map proves several bounded connections and gaps, while
the module inventory, control matrix, doctrine route map, and architecture
front doors remain separate views without one reconciled catalog/index.

### Contradiction Or Gap Disposition

No contradiction requires discarding existing maps. They become source views
feeding a stricter catalog and indexed gap ledger. L4 remains parked because
current evidence does not support promotion.

### Claim Update

The next high-value task is architecture/catalog consolidation and maintenance
control, not another speculative gap repair.

## Fail Conditions

Stop a tranche if it:

- promotes a declared or implemented edge to executed without caller evidence;
- creates a second authority hierarchy or freshness owner;
- copies legacy/external material into active authority without intake proof;
- creates an owner solely to make the diagram complete;
- hides unresolved items behind aggregate PASS/counts;
- leaves gap entries without terminal status or measurable conditions;
- hand-edits only a generated aggregate;
- expands into runtime, public, provider, Web, or L4 implementation without
  fresh authorization.

## Next Allowed Move

Obtain external reviewer critique of this proposed roadmap. After critique is
internally source-verified and folded or rejected with reason, author a fresh
GC-018 baseline and work order for ASC-T0 only. Do not dispatch later tranches
from this roadmap text alone.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture planning; no public-sync authorization.

## Claim Boundary

This roadmap defines a governed path to an as-built architecture catalog and
indexed gap ledger. It does not claim the catalog already exists, does not
close current gaps, and does not authorize runtime, public, provider, Web, or
product promotion work.
