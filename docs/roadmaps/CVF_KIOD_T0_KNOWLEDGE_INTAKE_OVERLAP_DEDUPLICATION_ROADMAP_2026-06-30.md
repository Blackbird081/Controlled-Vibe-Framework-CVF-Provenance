# CVF KIOD-T0 Knowledge Intake Overlap Deduplication Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_KIOD_R1_OWNER_SURFACE_TAXONOMY

docType: roadmap

Date: 2026-06-30

Batch ID: KIOD-T0

External knowledge intake routing: REQUIRED

## Purpose

Define the next governed roadmap for knowledge-intake deduplication after
KIOD-T1 added the overlap and novelty checker.

The goal is to make future repo or folder intake compare source value against
existing CVF owner surfaces before opening a new doctrine, package, runtime,
checker, adapter, or dashboard lane. The roadmap turns the operator-approved
discipline into a staged pipeline: classify overlap first, enrich existing
surfaces when possible, require negative search before new-owner claims, and
pilot the method on the next selected source.

## Authorization / Decision

Operator decision: proceed with the deduplication roadmap proposed after
KIOD-T1.

Roadmap decision:
`OPEN_KIOD_R1_OWNER_SURFACE_TAXONOMY`

Recommended next:
`AUTHOR_KIOD_R1_GC018_FOR_KNOWLEDGE_INTAKE_OWNER_SURFACE_TAXONOMY`

This roadmap authorizes planning only. It does not authorize new checker
implementation, source-mirror mutation, package activation, runtime work,
provider/live proof, public-sync, dashboard work, MCP/CLI adapter expansion, or
production-readiness claims.

## Scope

In scope:

- define a staged roadmap for future knowledge-intake deduplication;
- route each future source group through existing owner-surface comparison;
- require a pre-scan packet before a repo/folder closeout claims novelty;
- specify when existing surfaces are confirmed, enriched, or found missing;
- preserve the KIOD-T1 overlap dispositions as the central classification set.

Out of scope:

- absorbing a specific upstream repository or copied folder;
- changing any runtime source, package registry, generated index, or Web data;
- implementing a new checker beyond the already-closed KIOD-T1 guard;
- creating a new source mirror;
- making a public, provider, runtime, benchmark, adapter, or production claim.

## Non-Goals

- No direct import from external sources.
- No package lifecycle mutation or package activation.
- No automatic skill invocation or resolver behavior change.
- No runtime/MCP/watcher/daemon/SQLite work.
- No provider/live proof.
- No public-sync export.
- No dashboard or console build.
- No broad claim that machine gates prove semantic completeness.

## Design Control Gate

| Control | Required disposition |
|---|---|
| Existing owner-surface priority | KIOD-R1 must list current CVF owner surfaces before any new-owner lane can be proposed. |
| KIOD-T1 overlap discipline | Future intake artifacts must use `CONFIRMED_EXISTING`, `ENRICH_EXISTING`, `NEW_FINDING`, `REJECT_DIRECT_IMPORT`, `NO_NEW_VALUE`, or `OWNER_SURFACE_NOT_FOUND`. |
| New-owner claims | KIOD-R3 or later must require negative-search evidence before `NEW_FINDING` becomes a new owner surface. |
| External-source authority | External material stays advisory until source-verified and mapped to a CVF-owned surface. |
| Runtime and package boundary | Runtime, package, adapter, public, and provider behavior remain parked unless a later GC-018 authorizes them. |

## Work Plan

| Tranche | Status | Objective | Boundary |
|---|---|---|---|
| KIOD-T0 | ROADMAP_READY_FOR_KIOD_R1_OWNER_SURFACE_TAXONOMY | Create the deduplication roadmap after KIOD-T1 guard closure | planning only |
| KIOD-R1 | PROPOSED | Author the owner-surface taxonomy for knowledge intake across doctrine, runtime, package skills, checkers, Web/UI, provider/model, MCP/CLI, memory/state, corpus, and public-sync | reference map only |
| KIOD-R2 | PROPOSED | Define the pre-scan packet for future repo/folder intake: source groups, feature clusters, overlap candidates, novelty candidates, rejection reasons, and expected owner surfaces | packet template/reference only |
| KIOD-R3 | PROPOSED | Define the overlap routing matrix that converts source groups into confirmed-existing, enrich-existing, new-finding, direct-import-reject, no-new-value, or owner-missing actions | no implementation |
| KIOD-R4 | PROPOSED | Decide whether negative-search evidence needs a checker or can remain a required packet block; if a checker is proposed, open a fresh GC-018 | no checker now |
| KIOD-R5 | PROPOSED | Pilot the pipeline on the next operator-selected repo/folder and measure whether it reduces overlap and missed-value defects | no runtime or public claim |

## Acceptance Criteria

| Criterion | Evidence | Status |
|---|---|---|
| Roadmap names a concrete next tranche | `OPEN_KIOD_R1_OWNER_SURFACE_TAXONOMY` | PASS |
| Roadmap preserves KIOD-T1 overlap dispositions | Design Control Gate and Overlap And Novelty Classification | PASS |
| Roadmap avoids immediate checker or runtime expansion | Non-Goals and Claim Boundary | PASS |
| Roadmap includes external knowledge intake routing | `## External Knowledge Intake Routing` | PASS |
| Roadmap gives future agents a pre-warning path before gate failure | KIOD-R1 through KIOD-R3 plan owner taxonomy, pre-scan packet, and routing matrix | PASS |

## Verification / Evidence

| Evidence item | Result |
|---|---|
| Base head before roadmap authoring | `fdcc88b6` |
| Pre-implementation autorun | PASS on `fdcc88b6..HEAD` before material edit |
| Current KIOD-T1 material commit | `211645e8` |
| Current session-sync commit | `fdcc88b6` |
| Expected material changed set | this roadmap only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| External knowledge intake must route through the chain map before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `Mandatory Chain`; `Input Type Router` | `External/corpus/repo input -> input router` | external knowledge chain map | LITERAL_INVARIANT | ACCEPT |
| KIOD-T1 overlap discipline requires owner-surface comparison before new lanes | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | `Overlap And Novelty Classification Rule`; `Allowed overlap dispositions` | `## Overlap And Novelty Classification` | external absorption core standard | EXISTS | ACCEPT |
| KIOD-T1 checker is the current machine guard for overlap discipline | `governance/compat/check_external_absorption_overlap_discipline.py` | constants `OVERLAP_SECTION`; `REQUIRED_COLUMNS`; `ALLOWED_DISPOSITIONS` | `check_text` | overlap discipline checker | EXISTS | ACCEPT |
| Guard orientation warns future agents against duplicate owner surfaces | `docs/reference/guard_orientation/README.md` | `External knowledge absorption`; `Common Failure Patterns` | `check_external_absorption_overlap_discipline.py` | guard orientation index | EXISTS | ACCEPT |
| Active session state records KIOD-T1 as closed and wired | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `kiodT1ExternalAbsorptionOverlapDisciplineGuardClosure20260630` | `checker`; `allowedDispositions` | active session state registry | VALUE_SET | ACCEPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| KIOD-T1 overlap checker | `governance/compat/check_external_absorption_overlap_discipline.py` | CONFIRMED_EXISTING | Machine guard already exists for artifact-level overlap tables. | Keep checker as the enforcement baseline. |
| Owner-surface taxonomy | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `docs/reference/guard_orientation/README.md` | ENRICH_EXISTING | Existing standard requires comparison, but does not yet provide a compact owner-surface lookup map. | Open KIOD-R1 as a reference taxonomy. |
| Pre-scan packet | `docs/reference/external_agent_review/README.md` | ENRICH_EXISTING | Current authoring flow warns agents, but future repo scans need a reusable packet shape before closeout. | Open KIOD-R2 as a packet/template reference. |
| Negative-search evidence before new owner claims | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | NEW_FINDING | KIOD-T1 records owner-surface comparison, but a stricter negative-search decision point is not yet standardized. | Route to KIOD-R3/R4 before any checker implementation. |
| Next repo/folder pilot | existing governed intake roadmaps | NO_NEW_VALUE | A pilot is useful only after R1-R3 define the taxonomy and packet shape. | Park until KIOD-R5. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator decision -> KIOD roadmap -> owner-surface taxonomy -> pre-scan packet -> overlap routing matrix -> future repo/folder pilot or fresh GC-018 if implementation is needed |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` |
| Disposition | ADAPT operator-approved overlap discipline into a staged roadmap for future knowledge-intake deduplication |
| Claim boundary | roadmap and routing only; no source corpus absorption, runtime, package, provider, public, checker implementation, dashboard, adapter, or production claim |

## Risk / Corrective Action

| Risk | Corrective action | Status |
|---|---|---|
| Future agents duplicate owner surfaces because a repo feels novel | KIOD-R1 creates owner-surface taxonomy before more intake closeouts | PLANNED |
| Future agents mark value as no-new-value too quickly | KIOD-R2 requires source groups and feature clusters before closeout | PLANNED |
| New finding claims are made without negative search | KIOD-R3/R4 define negative-search evidence and decide whether a checker is warranted | PLANNED |
| A checker is implemented before the doctrine is stable | KIOD-R4 is a decision tranche, not automatic implementation | PLANNED |
| Pilot repo work widens into runtime or package activation | KIOD-R5 remains intake-pipeline proof only unless fresh GC-018 authorizes implementation | PLANNED |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: NOT_APPLICABLE_WITH_REASON - KIOD-T0 is a roadmap for
knowledge-intake deduplication and does not mutate ASSF registry entries,
package roots, truth packets, generated indexes, runtime eligibility, or skill
usage receipts.

Target lifecycle state: NOT_APPLICABLE_WITH_REASON - no package skill lifecycle
state is changed by this roadmap.

Prior phase evidence: KIOD-T1 material commit `211645e8` added overlap
discipline for intake artifacts; no package production tranche is opened here.

Next forbidden skip: future intake may classify a package candidate, but no
future agent may skip ASSF package productionization SOP, UAT, certification,
truth packet, usage receipt, resolver, or live/provider proof requirements.

Runtime/provider proof: N/A with reason: no runtime, package, provider, model,
or live governance behavior is claimed.

Claim boundary: package-skill references in this roadmap are routing examples
only; no package conversion, lifecycle mutation, activation, adapter behavior,
or production-readiness claim is made.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | KIOD-T0 knowledge-intake deduplication roadmap only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | local roadmap authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, browser, MCP, or adapter interception claim |
| claimLanguage | planning and routing only |
| forbiddenExpansion | no runtime, provider/live, public-sync, source-mirror mutation, package activation, checker implementation, dashboard build, MCP/CLI adapter, direct import, benchmark, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance planning roadmap. Public-safe publication would
require a separate public-sync decision and claim-boundary review.

## Claim Boundary

KIOD-T0 is a roadmap and routing artifact only. It does not claim that a new
external source has been absorbed, does not make external material canonical,
does not implement a new checker, does not mutate runtime or package state,
does not run providers, does not publish public artifacts, and does not prove
semantic completeness for future intake. Each future tranche requires its own
GC-018, source verification, autorun gates, and closure evidence.
