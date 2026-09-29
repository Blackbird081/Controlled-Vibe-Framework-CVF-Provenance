# CVF SOT3 Downstream Application And Four-Surface Absorption Intake Review

Memory class: FULL_RECORD

Status: OPERATOR_AUTHORIZED_FOR_ROADMAP_AUTHORING

docType: review

Date: 2026-07-15

Review ID: SOT3-APP-INTAKE

External absorption core: REQUIRED

## Purpose

Provide one bounded intake review and integrated independent-critique
classification for two new SOT3-related source roots before CVF authors a new
roadmap, GC-018 baseline, work order, or implementation tranche.

The reviewer position is `SELECTIVE_ADAPT_CANDIDATE_NO_ABSORPTION_YET`.
Independent critique narrowed the original readiness label and identified
additional application-boundary and provenance requirements. This review still
does not authorize a roadmap, direct import, or implementation.

## Target / Source

| Source ID | Literal root | Files | Bytes | Source class | Current authority |
|---|---|---:|---:|---|---|
| SOT3-APP-SRC | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application` | 336 | 238522 | downstream copied-folder application | external input only; not CVF authority |
| SOT3-FSCB-SRC | `.private_reference/legacy/CVF_SOT 10.07/cvf_four_surface_control_boundary_patch` | 37 | 84563 | retained legacy architecture/checker patch | private reference input only; not CVF authority |
| TOTAL | both literal roots above | 373 | 323085 | bounded two-root intake | no authority promotion |

Snapshot evidence was collected from direct recursive filesystem enumeration
at clean repository HEAD `8c1120a4f`. The SOT Application root has no local
`.git` directory and no root lockfile. Its `.cvf` manifest and binding files,
`.env.example`, documentation, and API configuration declare paths into the
existing hidden CVF workspace clone at
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\.Controlled-Vibe-Framework-CVF`.
Static declaration is verified; runtime use of those paths is not yet proven.

## Scope / Methodology

This intake performed:

1. direct recursive enumeration, byte accounting, extension grouping, and
   per-file SHA-256 computation for both roots;
2. targeted body review of root documentation, package manifests, CVF binding
   declarations and adapters, workflows, API middleware/controllers,
   application services, scripts, tests, Four-Surface references, schemas,
   checkers, examples, and existing canonical SOT3 owner surfaces;
3. overlap comparison against the closed SOT3 absorption, T8 packet-binding,
   SOT3 activation, system-chain, governance-control, and architecture-catalog
   surfaces;
4. bounded classification into adapt, package/runtime/checker candidate,
   reject-direct-import, defer, and no-new-value routes.

This is not a 373-row terminal body-read ledger and makes no full-corpus
semantic-completeness claim. A future T0 intake tranche must create that ledger
before any absorption closeout.

No test, build, typecheck, runtime, browser, provider, live, CI, package
installation, public-sync, or source mutation was performed.

## Findings / Position

### F-01 - The two roots need different absorption routes

`SOT-Application` correctly describes itself as a downstream application, not
CVF Core. Its business-domain model, local-first persistence design, scoped SOT
model, authority model, context-dose model, review/freeze flow, impact/recall
flow, and Controlled Quotation use case are useful downstream product inputs.
They are not a reason to copy the complete application into CVF Core.

The Four-Surface patch is an orthogonal logical control view. Its Application
And Intent, Agent Execution, Capability And Resource, and Evidence And
Continuation surfaces can enrich how CVF describes control objects. It must
not create a new physical repository hierarchy or replace the governance
control matrix, system-chain map, as-built catalog, or existing proof classes.

### F-02 - SOT Application does not yet consume the accepted T8 binding

The application-local `TruthKernelPort.evaluatePacket` accepts only a packet
identifier, and `refineryToKernelWorkflow` forwards only `packet.packet_id`.
The accepted CVF T8 owner instead binds Refinery-to-Kernel admission through
the versioned canonical packet-content hash profile
`cvf.sotThreeLayer.refineryPacketHash.v1`.

Disposition: `RUNTIME_CANDIDATE`, not direct import. A new compatibility tranche
must source-verify and consume the current CVF public package contracts rather
than retain parallel application-local packet semantics.

### F-03 - Current integration evidence is structural or mocked

The root binding validator checks binding JSON presence and `required=true`; it
does not verify target symbols, API compatibility, package resolution, runtime
connectivity, receipt identity, or behavior.

The Controlled Quotation script checks fixture presence and explicitly reports
`live_bindings_executed: false`. The failure-injection script constructs rows
whose `passed` values are already true. Several failure-injection tests compare
constants rather than invoking the production failure path.

Disposition: preserve these artifacts as reference scaffolding and negative
evidence. Do not cite them as integration, runtime, or live proof.

### F-04 - API and governance boundaries are reference-only

API controllers mainly return `REFERENCE_IMPLEMENTATION` and echo request
payloads. Identity trusts an `x-actor-id` header. The governance middleware
checks only that `x-cvf-phase` exists and does not source-verify a phase
decision. The middleware send path also lacks an explicit return after the 428
response. These are not authenticated or governed execution boundaries.

The Truth Flow adapter, governed output service, and governed context-package
entity each reject only `BLOCK`. The current code therefore permits `WARN`,
`ESCALATE`, and `REVIEW_REQUIRED` to pass the checked site unless a different
upstream control intervenes. This is a repeated decision-semantics gap, not an
adapter-local observation. A future contract must source-verify which decisions
may continue, which require review or escalation, and which must stop; this
review does not infer that every non-`ALLOW` value has identical semantics.
Freeze construction leaves `source_versions`, `refinery_receipts`, and
`policy_state` empty.

The middleware awaits a 428 response when `x-cvf-phase` is missing or an array,
but does not explicitly return the reply. Static inspection proves the missing
control-flow terminator; it does not by itself prove that Fastify executes the
route handler after the reply is sent. Treat this as a behavior-proof gap that
requires a negative request test, not as established runtime fail-open evidence.

Disposition: `RUNTIME_CANDIDATE` with fail-closed application-boundary repair
before any product proof.

### F-05 - Reproducibility and test ownership are incomplete

The application has ten package manifests. Only the root, API, and Web package
declare test/build/typecheck scripts; seven library packages declare none.
There is no root lockfile and the source root has no local Git provenance.

Disposition: a new product lane must freeze provenance, add reproducible
dependency evidence, and make tests exercise package behavior before it can
claim a buildable downstream reference application.

### F-06 - Four-Surface value is real but its checkers are not import-ready

The patch adds useful dimensions: control object, surface, mode, timing,
mechanism, maturity, implementation/test/evidence paths, known bypass,
failure behavior, and semantic owner. Its four JSON schemas parse successfully.

Direct checker import is rejected because the static checkers validate shape,
path existence, and a small phrase blacklist only. They do not validate cited
symbols, source hashes, receipt identity, invocation evidence, cross-owner
consistency, or compatibility with CVF's existing enforcement/proof taxonomy.
The source also calls its reference canonical without CVF ratification.

Disposition: `DOCTRINE_ADAPTED` plus a later `CHECKER_CANDIDATE` only after a
crosswalk and value test prove that existing guards cannot own the requirement.

### F-07 - Do not reopen SOT3-T8

The older main absorption roadmap retains stale wording that routes toward T8
packet authoring. Current canonical evidence shows T8 closed at material commit
`0ffede4f1`, and the SOT3 activation roadmap is already
`CLOSED_PASS_BOUNDED_LIVE_GOVERNANCE_PROVEN_BOUNDED` for one selected CVF Web
path.

Disposition: this new intake must open a separate downstream-product roadmap.
It must not reopen T8 or broaden the bounded activation claim.

### F-08 - Hidden-clone coupling must be severed or governed

The application declares `../.Controlled-Vibe-Framework-CVF` as its governance
root and as the target for multiple `.cvf` binding files. API configuration
also exposes the same default through `cvfCorePath`. This is a provenance and
authority coupling even though the present targeted read did not prove runtime
resolution through that field.

Disposition: classify the coupling as HIGH until a source-specific intake
tranche either removes it in favor of ratified public contracts or governs it
as an explicit, version-pinned dependency with drift detection. Do not describe
it as a proven live supply-chain path without runtime evidence.

## Risk / Corrective Action

| Risk | Severity | Corrective action before absorption claim |
|---|---|---|
| parallel packet and lifecycle authority | HIGH | source-verify current Refinery, Kernel, Flow, and T8 exports; remove or adapt duplicates |
| fixture/smoke evidence misread as runtime proof | HIGH | replace constant/fixture checks with behavior-path tests and replayable receipts |
| header presence misread as governance | HIGH | bind identity, phase, guard, and evidence decisions through current CVF owners |
| decision semantics are repeated across three consumers and stop only `BLOCK` | HIGH | enumerate every decision-consuming site and ratify an explicit per-decision continuation matrix before application hardening |
| middleware 428 path lacks an explicit return | MEDIUM | add a negative request behavior test; promote to confirmed fail-open only if the handler or downstream side effect executes |
| incomplete freeze provenance | HIGH | bind source versions, Refinery receipts, policy state, Kernel receipts, route decision, review, and hash |
| hidden-clone governance-root and binding coupling | HIGH | sever the paths or govern a version-pinned dependency with owner and drift evidence |
| duplicate Four-Surface taxonomy | MEDIUM | create a crosswalk-derived view over existing owners; no second source of truth |
| weak direct-import checker semantics | MEDIUM | reject direct import; evaluate only as a CVF-native checker candidate |
| no lockfile or local source provenance | MEDIUM | freeze manifest, provenance, dependency lock, and reproducible command evidence |
| stale T8 next-move language | MEDIUM | cite current T8/activation closure and route new work to SOT3-APP |

## Proposed Next Roadmap Lanes

The two roots should have independent dependency and closure paths. The
operator may authorize two roadmap files or one umbrella with independently
closeable lanes; this intake recommends two files to prevent product work from
blocking a doctrine-only crosswalk. Neither proposal is dispatch authority.

Proposed application roadmap: `CVF SOT3 Downstream Application Roadmap`, ID
`SOT3-APP`.

| Tranche | Objective | Required output | Release condition |
|---|---|---|---|
| SOT3-APP-T0 | freeze application intake and provenance | 336-row manifest and terminal processing ledger; aggregate digest; hidden-clone dependency disposition | 336 manifest rows reconcile and every declared hidden-clone path is severed, governed, or explicitly blocked |
| SOT3-APP-T1 | ratify downstream application contracts | owner map for business domain, CVF public adapters, T8 packet binding, decision semantics, evidence and freeze | every runtime/source symbol and decision value is directly source-verified |
| SOT3-APP-T2 | harden application boundaries | identity, phase/guard decisions, all three decision consumers, controller-service wiring, redaction, and freeze | negative paths and non-continuable decisions reach no output/provider lane |
| SOT3-APP-T3 | establish reproducible build and real tests | lockfile, scripts for all owned packages, schema compatibility, request-admission tests, and behavior-path failure injection | build/typecheck/tests are command-backed and non-tautological |
| SOT3-APP-T4 | prove Controlled Quotation locally | real local source-to-freeze-impact-recall slice with replayable receipts | complete identifier/evidence chain survives replay |
| SOT3-APP-T5 | optional operational/live proof | separately authorized real-provider and release evidence | exact bounded claim only; no production or universal SOT3 inference |

Proposed doctrine roadmap: `CVF Four-Surface Control Boundary Adaptation
Roadmap`, ID `FSCB-ADAPT`.

| Tranche | Objective | Required output | Release condition |
|---|---|---|---|
| FSCB-ADAPT-T0 | freeze and reconcile the Four-Surface source | 37-row terminal ledger plus crosswalk to governance control matrix, system-chain map, catalog, proof classes, and existing checkers | all 37 rows reconcile; no parallel authority or physical taxonomy; each checker candidate has a verified owner-gap disposition |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | one downstream copied-folder application plus one retained legacy architecture/checker patch |
| Upstream or source-mirror disposition | `LOCAL_OPERATOR_AUTHORED_INPUT_WITHOUT_UPSTREAM`; SOT Application has no local Git provenance; legacy patch remains private reference input |
| Enumeration or manifest plan | future source-specific T0 tranches directly enumerate 336 application files and 37 Four-Surface files with relative path, bytes, and SHA-256 |
| Per-file terminal-ledger plan | one row for each of 373 files using READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, or BLOCKED_UNREADABLE |
| Owner or overlap route | SOT3-APP-T1 owns application contract mapping; FSCB-ADAPT-T0 owns the doctrine/checker crosswalk to current governance-control, system-chain, catalog, package, runtime, and checker owners |
| Value-disposition route | ABSORB, ADAPT, DEFER, REJECT, BLOCK, or NO_NEW_VALUE followed by reviewer semantic-value audit |
| Claim boundary | intake and external critique only; no direct import, implementation, runtime, provider, public, production, or universal proof |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | copied-folder downstream application and retained `.private_reference/legacy/` patch |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact two-root enumeration followed by a 373-row per-file terminal ledger |
| Blind-spot prevention action | preserve every path and digest; audit deferred, rejected, and no-new-value groups in each source-specific lane |
| Residual gap | 373 file-level terminal decisions remain open; independent critique is classified below |
| Blind-spot verdict | PARTIAL_PENDING_SOURCE_LEDGERS |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | the two literal roots in Target / Source |
| Enumeration command | filesystem-backed direct recursive `Get-ChildItem` enumeration per literal root |
| Manifest artifact or inline manifest | inline Target / Source manifest; future source-specific T0 file-level manifests |
| Processing ledger artifact or inline ledger | inline Findings / Position and Overlap And Novelty Classification tables; future source-specific T0 ledgers |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table below |
| Unresolved items | 373 file-level terminal decisions plus reviewer questions 2, 5, 6, 7, and the exact sequencing portion of question 9 |
| Completion claim boundary | draft intake review only; no corpus-complete absorption, runtime, provider, public, or production claim |

## Corpus Completeness And Report Integrity

- Corpus task class: two-root SOT3 downstream application and control-boundary intake.
- Corpus root: the two literal roots in Target / Source.
- Snapshot time: 2026-07-15 local intake-review session.
- Enumeration command: filesystem-backed direct recursive `Get-ChildItem` per literal root.
- Manifest artifact or inline manifest: Target / Source inline two-root manifest.
- Manifest hash: per-file SHA-256 values were computed during intake; aggregate root digests must be frozen by the source-specific T0 tranches before dispatch.
- Processing ledger artifact or inline ledger: inline Findings / Position and Overlap And Novelty Classification tables; future source-specific T0 ledgers.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=373; ledger_terminal=0 at draft intake; exclusions=0; unresolved=373.
- Unresolved files: 373.
- Targeted-read distinction: files cited in F-02 through F-08 were read and source-verified for those bounded findings, but no per-file row has yet received a formal terminal ledger disposition; the future ledgers triage all 373 files and may reuse cited evidence without treating the remaining files as already reviewed.
- Declared exclusions: none.
- Unreadable or unsupported files: none observed during enumeration.
- Aggregation check: 336 plus 37 equals 373; 238522 plus 84563 equals 323085 bytes.
- Drift check: both source-specific T0 tranches must recompute counts, bytes, relative paths, and aggregate digests before classification.
- Output traceability: source ID, relative path, bytes, SHA-256, processing status, disposition, owner, and reason.
- Adversarial verification: targeted review findings and the classified independent rebuttal cannot substitute for the future per-file ledgers.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| SOT business/domain model | scoped authority, context, output, freeze, impact and recall | `PACKAGE_CANDIDATE` | downstream SOT Application owner | SOT3-APP-T1 contract ratification | not CVF Core; no package activation |
| application CVF ports | fail-closed adapter intent | `RUNTIME_CANDIDATE` | current Refinery, Kernel, Flow, Guard, Phase and evidence owners | source-verified compatibility rewrite | no runtime claim from interface presence |
| Controlled Quotation fixtures | bounded business use case | `PACKAGE_CANDIDATE` | SOT3-APP-T4 | convert fixture harness into real local slice | fixture existence is not execution proof |
| Four-Surface concepts | control object, mode, timing, maturity and evidence map | `DOCTRINE_ADAPTED` | governance control index plus derived system-chain/catalog projection | FSCB-ADAPT-T0 crosswalk | no new physical taxonomy |
| Four-Surface checkers | shape and overclaim checks | `CHECKER_CANDIDATE` | existing governance checker owners | value test after crosswalk | no hook wiring or direct import |
| application-local duplicate contracts and tautological tests | negative compatibility evidence | `REJECT_DIRECT_IMPORT` | SOT3-APP-T1/T3 repair ledger | retain as defects, rewrite against current owners | no reuse as proof |
| presentational duplicates and generated tree summaries | navigation/context only | `NO_PACKAGE_OR_RUNTIME_VALUE` | retained input provenance | confirm per-file in the owning source-specific T0 | no runtime/checker value without delta |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| three-layer core architecture | `docs/reference/sot_three_layer/README.md` | `CONFIRMED_EXISTING` | downstream composition, not a new core owner | consume current public contracts |
| T8 packet binding | `EXTENSIONS/CVF_REFINERY/src/packet-hash/packet-hash.ts` | `REJECT_DIRECT_IMPORT` | application currently forwards only packet ID | replace with source-verified compatibility design |
| SOT3 activation proof | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | `CONFIRMED_EXISTING` | new app is a different downstream product path | do not broaden or reopen activation claim |
| scoped business SOT application | `OWNER_SURFACE_NOT_FOUND` | `OWNER_SURFACE_NOT_FOUND` | complete downstream product owner is not present in CVF Core | retain sibling app; decide owner in SOT3-APP-T1 |
| Four-Surface logical view | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | `ENRICH_EXISTING` | adds object/mode/timing/maturity crosswalk | adapt as derived view in FSCB-ADAPT-T0 |
| Four-Surface static checkers | `governance/compat/check_governed_artifact_checker_read_ahead.py` | `NEW_FINDING` | possible gap in control-claim projection validation | value-test before checker proposal |
| copied UI/API/controller scaffold | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `REJECT_DIRECT_IMPORT` | broad reference shell with weak binding semantics | harden in sibling app only |
| repeated summaries/tree views | `OWNER_SURFACE_NOT_FOUND` | `NO_NEW_VALUE` | navigation aid only unless the owning T0 finds unique semantics | retain as entry surfaces, not authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | intake review -> independent external critique -> Codex classification -> operator decision -> separate SOT3-APP and FSCB-ADAPT roadmap/GC-018 packets if authorized -> source-specific ledgers -> separately authorized implementation |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this integrated draft intake until the operator accepts, revises, or declines the proposed roadmap lanes |
| Disposition | ACCEPT_WITH_CHANGES at critique level; ADAPT selectively at source level; reject direct import and any reopening of closed SOT3-T8 |
| Claim boundary | external-review input only; no absorption completion, implementation, runtime, provider, public, or production claim |

## Independent External Reviewer Challenge

The external reviewer should answer each question with source-backed evidence:

1. Is `SELECTIVE_ABSORPTION_GO_WITH_FIXES` too permissive or too restrictive?
2. Which SOT Application capability is genuinely novel relative to accepted
   SOT3, rather than a duplicate presentation or local contract?
3. Does any current application path actually bind the full T8 packet profile,
   receipt identity, scope, and replay boundary? If yes, cite the exact symbol.
4. Can WARN, ESCALATE, or REVIEW_REQUIRED currently reach context or output
   creation? Identify every path and the correct fail-closed disposition.
5. Which tests execute real production behavior, and which are fixture,
   constant, mocked-port, or structural checks only?
6. Does the Four-Surface model add a necessary owner view, or can all value be
   represented as fields on existing control-matrix/catalog/system-chain rows?
7. Which Four-Surface checker rule is not already owned by current CVF guards?
8. Is SOT3-APP the right roadmap boundary, or should Four-Surface adaptation
   and downstream application productization be separate roadmaps?
9. Which proposed tranche should be removed, split, reordered, or blocked?
10. Identify any security, authority, privacy, evidence, lifecycle, or claim
    boundary defect missed by this intake.

Required external output:

- overall verdict: ACCEPT, ACCEPT_WITH_CHANGES, REJECT, or BLOCKED;
- finding ledger with severity, source path/symbol, agreement or dissent, and
  recommended disposition;
- corrected roadmap sequence;
- explicit direct-import boundary;
- unresolved source questions and stop conditions;
- bounded claim statement.

## Decision / Disposition

Reviewed external rebuttal:
`docs/reviews/CVF_SOT3_APP_INTAKE_REVIEW_CLAUDE_REBUTTAL_FOR_CODEX_2026-07-15.md`.

Overall classification: `ACCEPT_WITH_CHANGES`.

Operator authorization: `ACCEPTED_FOR_ROADMAP_AUTHORING_2026-07-15`.

Authorization scope: author the two proposed roadmaps and dispatch the first
bounded FSCB-ADAPT tranche through fresh GC-018 and a source-verified work
order. This authorization does not bypass pre-dispatch gates and does not
authorize SOT3-APP runtime mutation before its own released implementation
tranche.

The rebuttal successfully narrows readiness, expands the decision-consumer
inventory, exposes declared hidden-clone coupling, and justifies independent
roadmap lanes. Two statements require narrower wording: a missing explicit
middleware return is not static proof that Fastify executes the handler after
sending 428, and declared hidden-clone targets are not proof that runtime paths
have resolved through that clone. Both remain mandatory T0/T3 evidence items.

| Rebuttal item | Codex classification | Resolution |
|---|---|---|
| R-01 factual core | ACCEPT | retain the source-backed intake findings |
| R-02 readiness label | ACCEPT | replace the original GO-adjacent label with `SELECTIVE_ADAPT_CANDIDATE_NO_ABSORPTION_YET` |
| R-03 three decision consumers | ACCEPT_WITH_NARROWING | treat the repeated `BLOCK`-only check as a systemic semantics gap; source-verify the required behavior for every decision rather than presuming all non-`ALLOW` decisions are equivalent |
| R-04 middleware 428 | PARTIAL_REJECT | retain the missing-return observation and require a negative behavior test; do not claim proven runtime fail-open from static source alone |
| R-05 corpus wording | ACCEPT_CLARIFICATION | distinguish bounded source-verified findings from zero formal per-file terminal rows |
| R-06 roadmap boundary | ACCEPT | propose independent SOT3-APP and FSCB-ADAPT closure paths |
| R-07 hidden-clone pointer | ACCEPT_WITH_NARROWING | classify the manifest/config/binding declarations as HIGH provenance and authority coupling; runtime resolution remains unproven |
| R-08 open questions | CORRECTED | questions 1, 3, 4, 8, and 10 now have bounded answers; questions 2, 5, 6, 7, and the exact sequencing part of 9 remain open |

## Required Absorption Table

| External item ID | External claim summary | Source basis | CVF verification surface | CVF disposition | Owner artifact | Next action | Claim boundary |
|---|---|---|---|---|---|---|---|
| R-01 | factual intake core verifies | external rebuttal R-01 | cited application symbols and accepted T8 commit | ACCEPT | this integrated intake review | retain bounded findings | no corpus-complete claim |
| R-02 | readiness label is too permissive | external rebuttal R-02 | intake Purpose and runtime-candidate findings | ACCEPT | this integrated intake review | use narrowed label | no roadmap authorization |
| R-03 | decision gap spans three consumers | external rebuttal R-03 | `truth-flow.adapter.ts`; `governed-output.service.ts`; `context-package.ts` | ACCEPT_WITH_NARROWING | proposed SOT3-APP-T1/T2 | ratify per-decision matrix and enumerate consumers | no inferred decision semantics |
| R-04 | missing middleware return proves fail-open | external rebuttal R-04 | `cvf-governance.middleware.ts` static control flow | PARTIAL_REJECT | proposed SOT3-APP-T3 | execute a negative request behavior test if authorized | no runtime failure claim from static read |
| R-05 | corpus wording is ambiguous | external rebuttal R-05 | Corpus Completeness reconciliation | ACCEPT_CLARIFICATION | this integrated intake review | retain targeted-read distinction | formal ledger remains unresolved |
| R-06 | source roots need independent closure | external rebuttal R-06 | F-01 source-class split | ACCEPT | proposed SOT3-APP and FSCB-ADAPT lanes | operator decides whether to authorize either lane | proposals only |
| R-07 | hidden-clone path is an authority hazard | external rebuttal R-07 | `.cvf` manifest/bindings, `.env.example`, API config | ACCEPT_WITH_NARROWING | proposed SOT3-APP-T0 | sever or version-pin and drift-check every declared path | runtime resolution unproven |
| R-08 | several challenge questions remain open | external rebuttal R-08 | challenge list and classification above | CORRECTED | future source-specific T0 evidence | answer 2, 5, 6, 7, and remaining part of 9 | no invented answers |

## Epistemic Process Block

Expected Result / Prediction: the two roots contain reusable downstream product
and control-model value, but direct import would duplicate owners and overstate
runtime maturity.

Evidence Comparison: targeted source review confirms a useful downstream
domain model and Four-Surface vocabulary, while packet-ID-only Kernel binding,
reference controllers, structural binding validation, fixture-only vertical
slice, tautological failure checks, partial package scripts, and static-only
Four-Surface checkers support the predicted direct-import rejection.

Contradiction Or Gap Disposition: the older SOT3 roadmap's T8-next wording is
stale relative to accepted T8 and activation closure. The independent rebuttal
correctly narrowed the readiness label, expanded the decision-consumer scope,
and exposed hidden-clone coupling. Its middleware runtime-failure claim was
narrowed to a behavior-proof requirement. Full 373-file semantic reconciliation
remains open and blocks absorption completion.

Claim Update: move from external-review-ready intake to
`OPERATOR_AUTHORIZED_FOR_ROADMAP_AUTHORING`, with two independently closeable
proposed lanes, selective-adaptation candidates, and explicit implementation
blockers; no runtime or product claim is upgraded.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Required Absorption Table; External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; External Absorption Core; Corpus Completeness And Report Integrity; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; External Knowledge Intake Routing; PARTIAL; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm integrated intake and rebuttal-classification structure after semantic review; checker PASS is not semantic acceptance |
| claimBoundary | structural reviewability only; no 373-file completion, implementation, runtime, provider, public, or production proof |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-intake and external-review packet; no public-sync
authorization or public-safe artifact set exists.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | intake reviewer and rebuttal classifier |
| Provider or surface | local private provenance workspace and operator-named sibling workspace source |
| Session or invocation | SOT3 new-source intake assessment and rebuttal integration, 2026-07-15 |
| Working directory | repository root |
| Command or tool surface | direct filesystem enumeration, SHA-256 hashing, governed reads, source search, JSON parsing, overlap comparison, apply_patch |
| Target paths | this single draft review artifact |
| Allowed scope source | operator requested the intake review and then supplied the independent rebuttal for Codex classification |
| Before status evidence | clean HEAD `8c1120a4f`; no governed intake artifact for these two roots |
| After status evidence | integrated intake review plus one separate uncommitted external rebuttal packet; source roots unchanged |
| Diff evidence | `git status --short`; `git diff --check`; applicable draft gates |
| Approval boundary | assessment and rebuttal classification only; no roadmap dispatch or implementation |
| Claim boundary | targeted intake findings, external-critique classification, and proposed lanes only |
| Agent type | intake reviewer |
| Invocation ID | sot3-app-four-surface-intake-review-2026-07-15 |
| Expected manifest | `docs/reviews/CVF_SOT3_DOWNSTREAM_APPLICATION_AND_FOUR_SURFACE_ABSORPTION_INTAKE_REVIEW_2026-07-15.md` |
| Actual changed set | same single draft review path |
| Manifest delta | MATCH required before handoff |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This draft records a targeted intake assessment and integrated independent
rebuttal classification. It does not claim all 373 files were semantically read or
terminally dispositioned; does not make either source root canonical; does not
authorize direct import, roadmap dispatch, implementation, package activation,
runtime, provider/live execution, public-sync, release, production readiness,
scale, certification, shipment, or user value; and does not reopen SOT3-T8 or
broaden the accepted bounded SOT3 activation claim.
