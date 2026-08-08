# CVF LPCI Current-Owner Grounding And Clearance Defect Intake Roadmap

Memory class: FULL_RECORD

Status: LPCI_CONFORMANCE_SPEC_ACCEPTED_BOUNDED_HOLD_BEFORE_BUILD

docType: roadmap

Date: 2026-08-08

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_docs_governance_compat.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | `Status:`; `## Authorization / Decision`; `## Purpose`; `## Scope / Target / Owner Boundary`; `## Current Runtime Freshness Verification`; `## Negative Search And Collision Discipline`; `## Design Control Gate`; `## Dispatch Boundary`; `## Acceptance Criteria`; `## Public Export Disposition`; `DEFERRED_PRIVATE_ONLY`; `claimBoundary` |
| gateRunPurpose | confirm and record gate evidence for one already source-reviewed documentation-only INTAKE without releasing later lifecycle phases; gates are not the first discovery mechanism |
| claimBoundary | source and canonical-contract reconciliation only; no runtime, test, provider, persistence, vector/RAG, public, or deployment action |

## Authorization / Decision

Operator authority received on 2026-08-08:

`AUTHORIZE_FRESH_LPCI_DEFECT_INTAKE_DOCUMENTATION_ONLY`

This authority opens only this fresh LPCI current-owner defect intake. It does
not inherit or imply lifecycle DESIGN, SPEC, WORK ORDER, BUILD, provider/model
selection, provider invocation, live proof, persistence, vector/RAG, runtime
mutation, test execution, public-sync, deployment, or readiness authority.

Three read-only workers inspected grounding, sensitivity authorization, and
canonical LPCI owner/history surfaces. The reviewer independently reverified
accepted findings against current source and canonical CVF artifacts. Worker
notes are leads, not canonical authority.

## Purpose

Determine, without designing a solution, whether the existing LPCI T5 query
owner has two source-backed defect boundaries:

1. positive-answer evidence-text grounding; and
2. actor-bound, corpus-aware sensitivity clearance.

The intake also records the linked no-provider response-minimization and proof
coverage questions needed before any later lifecycle decision.

## Non-Goals

This intake does not select a solution, evidence payload, entitlement store,
provider, persistence mechanism, vector/RAG architecture, or cross-owner
retrieval composition. It does not authorize runtime or test changes, test or
live execution, provider calls, public-sync, deployment, or a readiness claim.

## Scope / Target / Owner Boundary

Scope: documentation-only current-source and canonical-contract reconciliation.

Target: the existing LPCI query surface under
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`.

Current owner: the LPCI1-T5 cvf-web route/library/UI/test family originally
assigned by `docs/work_orders/CVF_WO_LPCI1_T5_CHATBOT_PROTOTYPE_2026-06-03.md`.

Owner boundary: this is not a generic governed-retrieval, Control Plane,
Memory, KGR, vector, or provider lane. P4-A1 remains
`NO_CROSS_OWNER_DESIGN_JUSTIFIED`.

## Source Authority Inventory

| Source | Accepted authority | Intake boundary |
|---|---|---|
| `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | canonical filter order, content-snippet display-hint boundary, and sensitivity authorization rules | specification authority; no current runtime behavior proof |
| `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | retrieval receipt, answer assembly, receipt, abstention, freshness, conflict, and response-boundary contract | documentation contract; does not itself identify the safe model-bound evidence projection |
| `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `public`, `restricted`, `confidential`, `classified`, and `unknown` treatment | classification authority; no actor entitlement store is selected here |
| `docs/work_orders/CVF_WO_LPCI1_T5_CHATBOT_PROTOTYPE_2026-06-03.md` | original cvf-web LPCI owner, allowed runtime family, and T5 requirements | historical dispatch authority, not fresh implementation authority |
| `docs/reviews/CVF_LPCI1_T5_CHATBOT_PROTOTYPE_COMPLETION_2026-06-03.md` | bounded citation, response-boundary, receipt, route, build, test, and historical live-output evidence | does not prove that current positive-answer facts were grounded in model-bound retrieved text |
| `docs/reviews/CVF_LPCI1_T6_ADVERSARIAL_EVALUATION_2026-06-03.md` and its completion | bounded observed adversarial outcomes | positive-answer evaluator coverage does not substitute for current prompt-payload inspection |
| current LPCI TypeScript source | current route, filter, retrieval, receipt, UI, authentication, and test behavior | direct source controls current behavior claims |
| `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` and registry entry | current synthetic four-record pilot, all rows marked `public` | no production, classified, confidential, restricted, or actual-release proof |

## Current Runtime Freshness Verification

| Freshness item | Current verification | Disposition |
|---|---|---|
| Verification date and base | 2026-08-08; starting HEAD `9020295e5` | current for this intake pass |
| Grounding path | direct read of `route.ts`, `retrieval.ts`, `types.ts`, route tests, UI, T3/T4 contracts, T5/T6 closures, and route history | current prompt-payload finding accepted |
| Clearance path | direct read of `route.ts`, `filter-pipeline.ts`, `route-governance-proof.ts`, `middleware-auth.ts`, `service-token-auth.ts`, tests, and T2/T3 contracts | current actor-binding and classification mismatch accepted |
| Corpus path | direct read of the only current `*-index.json` and its generated-registry source entry | current pilot is synthetic and public-only |
| Provider context | provider branch source was inspected only; no credential, network, model, or live call was used | no provider-quality or live-governance claim |
| Freshness boundary | repository source and governed artifacts only | no deployed-state or external-caller claim; repeat before later dispatch |

## Defect Intake Ledger

| ID | Finding | Direct current-source fact | Canonical comparison | Intake disposition |
|---|---|---|---|---|
| `LPCI-DI-01` | positive-answer grounding | `buildAnswerBoundaryPrompt()` supplies path, status, and effective date; the provider messages contain that prompt plus the user query, but no `contentSnippet` or other evidence text | T4 already requires the retrieval receipt as model context and requires summaries/guidance grounded in retrieved text | `PREVIOUSLY_DECIDED_REQUIREMENT_WITH_T5_CONFORMANCE_CONFLICT` |
| `LPCI-DI-02` | actor-bound sensitivity clearance | request `filters` flow unchanged into `sensitivityClearance`; `true` permits classified rows; authenticated actor/session/service identity is not used by the filter | T2/T3 already require distinct actor/corpus authorization for classified, confidential, restricted, and unknown records | `PREVIOUSLY_DECIDED_AUTHORIZATION_REQUIREMENT_WITH_RUNTIME_AND_RECEIPT_GAP` |
| `LPCI-DI-03` | sensitivity-level coverage | current filter explicitly excludes only `classified` when clearance is false; confidential, restricted, and unknown are not handled by their canonical rules | T2/T3 require corpus- and authorization-specific treatment, with unknown treated restrictively | `CONFIRMED_BOUNDED_SOURCE_CONTRACT_MISMATCH` |
| `LPCI-DI-04` | no-provider response minimization | phase-2 `NO_PROVIDER_CONFIGURED` returns the full retrieval receipt; matched records retain the full index-row shape including snippets | original T5 work order required only receipt type and query for the no-provider response; UI uses only matched-path count | `SOURCE_LEVEL_DISCLOSURE_REVIEW_CANDIDATE` |
| `LPCI-DI-05` | proof coverage | route logic test uses a copied simulator; no focused test asserts model-bound evidence or actor-bound clearance; T6 positive-answer checks have a nested-receipt blind spot | historical closures prove bounded observed mechanics but do not prove current grounding or sensitivity entitlement | `HISTORICAL_CLAIM_NARROWING_REQUIRED` |

## Reviewer Findings

### Grounding

The current internal retrieval receipt retains full matched index records, but
the private prompt builder deliberately narrows each record to metadata. The
model-bound branch therefore receives no retrieved evidence text from current
source. This conflicts with the T4 expectation that the LLM receives retrieval
context and answers from retrieved text.

The intake does not select `contentSnippet` as the correction. T3 calls that
field a display hint capped at 512 characters. Sending it, another field, or a
minimized receipt is a later authority decision. Passing the full retrieval
receipt is also not assumed safe.

The grounding requirement itself is not reopened. T4 already selects the
retrieval receipt as the LLM context payload. The remaining design question is
how that previously decided requirement can be honored without creating an
unbounded provider or client disclosure surface.

### Clearance

The route-governance owner already authenticates session and signed service
token callers and emits an actor ID. The LPCI route does not bind that identity,
session role, org/team, impersonation state, service identity, corpus, or a
governed grant to sensitivity filtering.

The current boolean is a client assertion, not entitlement evidence. It also
collapses the canonical multi-level policy into classified-versus-other. This
is a current source/contract mismatch.

### Current Impact Boundary

The only current index is a synthetic test corpus with four public records.
This intake therefore does not claim actual sensitive-data release,
exploitation, production exposure, legal-answer correctness, or provider
disclosure. The clearance defect is dormant but source-verifiable.

The historical T5/T6 closures remain bounded evidence of their recorded
mechanics and observed outputs. Their positive-answer evidence must be narrowed:
it is not proof that answer facts came from model-bound retrieved evidence.
This intake does not rewrite or reopen those historical artifacts.

## Owner And History Reconciliation

| Item | Current evidence | Reviewer disposition |
|---|---|---|
| canonical LPCI1 roadmap | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` is `ALL_TRANCHES_CLOSED_PASS_BOUNDED` | retain as canonical historical roadmap; conformance defects do not silently reopen it |
| older product proposal | `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md` remains `PROPOSED` | stale planning input; not current authority |
| defect origin | `git blame` and commit `47519c152` show both current behaviors originate in the T5 implementation | current-owner LPCI1-Web conformance scope |
| later corpus-boundary hardening | commit `a9bbbcd3c` changed LPCI boundary/receipt source but retained both findings | not closure evidence for these defects |
| later route authentication | commit `40c3c10df` added route actor identity and proof but did not bind LPCI clearance | identity prerequisite exists; entitlement mapping remains absent |
| LPCI2 PolicyLocal | separate corpus/search runtime owner and closure family | do not merge into LPCI1-Web design or defect claims |

Reviewer disposition:

- grounding requirement: previously decided, current T5 conformance conflict;
- sensitivity authorization: previously decided, current runtime and receipt
  evidence gap;
- linked no-provider response: minimization conflict requiring bounded design;
- cross-owner retrieval: remains `NO_CROSS_OWNER_DESIGN_JUSTIFIED`.

## Ambiguity And Decision Ledger

| Decision question | Current evidence | Intake posture |
|---|---|---|
| Is model-bound retrieved evidence required? | T4 already requires the retrieval receipt as context and grounded summaries/guidance | `PREVIOUSLY_DECIDED_REQUIREMENT` |
| What bounded projection safely honors that requirement? | D1 selects a minimized public-only snippet projection candidate plus metadata-only abstention; T3/T4 conflict remains | `CONDITIONAL_ON_SPEC_RECONCILIATION` |
| May any full retrieval receipt reach a provider or no-provider client? | D1 excludes full receipts from both surfaces and retains only minimized projections | `DESIGN_DECIDED_SPEC_REQUIRED` |
| Who owns actor-to-sensitivity and actor-to-corpus grants? | authentication identity exists; no current LPCI entitlement owner is source-backed | `OWNER_NOT_SELECTED` |
| Where is restricted-corpus retrieval authorization stored and read? | T3 refers to GC-051-time authorization; current registry presence is not entitlement proof | `SOURCE_OWNER_REQUIRED` |
| How are service-token and impersonated-session actors treated? | D1 treats identity as non-authoritative and keeps every actor public-only until a grant owner exists | `PUBLIC_ONLY_FAIL_CLOSED` |
| What proof is required later? | D1 defines positive grounding, minimization, forged-clearance, mixed-record, missing-evidence, and injection cases | `SYNTHETIC_PROOF_MATRIX_DEFINED_NO_EXECUTION` |

## Design Control Gate

Gate status: `SPEC_ACCEPTED_BOUNDED_HOLD_BEFORE_BUILD`.

Operator release received on 2026-08-08:

`LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN`

The DESIGN release was bounded to documentation-only DESIGN under its fresh
GC-018 and source-verified work order. The later operator token
`AUTHORIZE_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_DOCUMENTATION_ONLY`
released a separate documentation-only SPEC packet. That SPEC is now
reviewer-accepted. BUILD, runtime/test mutation or execution,
provider/model/live action, persistence, vector/RAG, public-sync, deployment,
and readiness authority remain withheld.

| Gate question | Current answer | Effect |
|---|---|---|
| Are the two primary defect boundaries source-backed? | Yes, bounded | accepted as current-owner conformance design inputs |
| Is the safe evidence projection selected? | Conditionally | minimized public-only snippet projection is a SPEC candidate; T3/T4 reconciliation is still required |
| Is an entitlement owner selected? | No | no authorization interface or schema design |
| Is DESIGN authorized? | Completed and reviewer-accepted, bounded | design audit and corrected worker return are the accepted outputs |
| Is SPEC authorized? | Completed and reviewer-accepted, bounded | reference SPEC and completion review are the accepted outputs |
| Is an implementation WORK ORDER authorized? | No | no BUILD dispatch packet |
| Is BUILD or test execution authorized? | No | no source/test mutation or execution |
| Is provider/live work authorized? | No | no key, model, endpoint, call, or proof |

The operator decisions released only the bounded DESIGN and later bounded SPEC
questions named by this intake. Each used its own paired fresh GC-018 and
source-verified work order. Reviewer acceptance does not release BUILD or any
external-effect phase.

## Dispatch Boundary

The operator authorized three read-only evidence workers for this intake. They
had no file-edit, commit, test, provider, network, design, or implementation
authority. A later no-commit design worker operated only under the paired D1
GC-018 and work order; the primary reviewer owns integration and closeout.

No implementation worker is dispatched. The accepted child specification is
`docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`.
No BUILD GC-018/work order, runtime edit, test run, provider call, public
action, or deployment is authorized by this roadmap.

## Work Plan

| Step | Documentation-only action | Output | Stop condition |
|---|---|---|---|
| `LPCI-DI-T0.1` | reverify current grounding and response shapes | source evidence table | stop before choosing evidence fields |
| `LPCI-DI-T0.2` | reverify actor and sensitivity semantics | source/contract comparison | stop before defining entitlement interfaces |
| `LPCI-DI-T0.3` | reconcile original owner and historical proof boundaries | owner/history ledger | stop before reopening historical closures |
| `LPCI-DI-T0.4` | return bounded defect and ambiguity dispositions | reviewer intake decision | stop before DESIGN |

## Acceptance Criteria

| ID | Criterion | Required disposition |
|---|---|---|
| `AC-01` | operator authority is recorded as documentation-only INTAKE | `PASS_REQUIRED` |
| `AC-02` | current source and canonical LPCI contracts are distinguished | `PASS_REQUIRED` |
| `AC-03` | grounding gap is recorded without selecting `contentSnippet` or another solution | `PASS_REQUIRED` |
| `AC-04` | actor-bound clearance mismatch covers all canonical sensitivity levels | `PASS_REQUIRED` |
| `AC-05` | current public-only pilot prevents actual sensitive-release overclaim | `PASS_REQUIRED` |
| `AC-06` | T5/T6 historical evidence is narrowed without wholesale reopening | `PASS_REQUIRED` |
| `AC-07` | accepted DESIGN remains bounded and every later lifecycle or external-effect lane remains blocked | `PASS_REQUIRED` |

## Negative Search And Collision Discipline

- Search roots: current LPCI cvf-web source and tests, canonical LPCI docs,
  corpus-intelligence index/registry sources, and route-auth owners.
- Search commands: exact `rg` queries for `buildAnswerBoundaryPrompt`,
  `contentSnippet`, `sensitivityClearance`, classified/confidential/restricted/
  unknown treatment, route callers, prompt assertions, and receipt assertions.
- Coverage: source, tests, docs, JSON, historical reviews, and current registry
  sources; generated dependency trees and Git internals were excluded.
- Same-token collision results: grounding, content, sensitivity, clearance,
  receipt, and authorization terms occur across contracts, runtime, tests, and
  historical reviews with different claim classes.
- Disposition: those occurrences are non-authoritative for current behavior
  unless confirmed in current source. Absence claims are bounded to the stated
  search roots and exact symbols.

Observed negative results:

| Query | Bounded result | Disposition |
|---|---|---|
| focused current prompt assertion | no focused source test asserts evidence text in the model-bound prompt | coverage gap only; no test authoring authority |
| `sensitivityClearance: true` in current LPCI tests | no exact test case returned | positive-clearance coverage gap only |
| current LPCI actor-to-clearance binding | authentication identity exists, but no route/filter binding symbol or entitlement lookup returned | owner/policy input required before DESIGN |
| current sensitive index corpus | only the synthetic public-only LPCI index is present | no actual sensitive-release claim |

## Verification / Evidence

| Evidence item | Source or command class | Observed result |
|---|---|---|
| Starting worktree | `git status --short` | clean |
| Material base | `git log -1 --oneline` | session-sync HEAD `9020295e5`; parent material recommendation `127d2410e` |
| Prompt construction | current LPCI query route | metadata-only source list reaches provider prompt; evidence text does not |
| Retrieval receipt | current LPCI retrieval/types source | matched records retain full index rows |
| No-provider response | current query route and UI | HTTP response returns full retrieval receipt; current UI uses path count and minimized AuditReceipt |
| Sensitivity filter | current route/filter/types source | client boolean flows into filter; only classified is conditionally excluded |
| Actor identity | route-governance, middleware-auth, and service-token source | actor/session/service identity exists but is not clearance-bound |
| Canonical policy | LPCI T2/T3/T4 references | multi-level authorization and grounded-answer expectations exceed current source behavior |
| Current corpus | pilot index and registry entry | four synthetic public records; no production corpus claim |
| Historical proof | T5/T6 work order and reviews | bounded mechanics/output evidence exists; grounding and entitlement proof do not |

## Epistemic Process Block

Expected Result / Prediction: direct source review would either reject the two
P4-A1 candidates as false alarms or confirm current-owner gaps without proving
production harm.

Evidence Comparison: current source confirms a model-bound grounding gap and a
client-asserted, incomplete sensitivity policy. Canonical T2/T3/T4 requirements
make both material. Current public-only pilot evidence prevents escalation to
an actual disclosure or production-impact claim.

Contradiction Or Gap Disposition: the grounding behavior conflicts with T4
context expectations, but T3 leaves the safe evidence class ambiguous. The
clearance behavior directly conflicts with canonical multi-level authorization
rules. Historical live output is retained as observed output, not evidence that
retrieved text was supplied to the model.

Claim Update: the documentation-only S1 specification is reviewer-accepted as
`SPEC_ACCEPTED_BOUNDED_HOLD_BEFORE_BUILD`. It reconciles T3/T4 narrowly,
defines public-only Stage 1 admission, a deterministic minimized evidence
projection, fail-closed evidence limits, minimized response variants, and
response-local audit correlation. This is not current runtime conformance or
BUILD readiness.

The next operator checkpoint is fresh explicit BUILD authority. Any BUILD must
use a fresh GC-018, current source verification, a separate implementation work
order, deterministic tests, and the normal lifecycle gates. Provider/live,
persistence, vector/RAG, non-public grant ownership, public-sync, deployment,
and readiness remain separately withheld.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this intake contains private provenance paths, internal source/history
reconciliation, and no public-safe export packet. No public mutation or claim
is authorized.

## Claim Boundary

This roadmap records one documentation-only LPCI current-owner defect intake.
It confirms current source/contract gaps for evidence grounding and actor-bound
sensitivity clearance while explicitly withholding any solution choice,
runtime behavior change, test execution, provider action, sensitive-data
release claim, production claim, public action, deployment, or readiness claim.
