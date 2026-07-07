# CVF MSEA R64-R70 Public Trust And Agent Loop Absorption Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_R64_DISPATCH

Date: 2026-07-07

docType: roadmap

## Purpose

Define the governed lane for absorbing the operator-provided external critique
folder named `Gop y CVF` without treating that folder as CVF authority. The
lane first verifies public-facing drift, then routes accepted value into public
documentation, policy/schema surfaces, and optional future checker decisions.

## Scope

Allowed scope for this roadmap:

- classify the external critique as advisory input;
- verify public-facing drift against the sibling public-sync clone;
- create governed packets for public P0 drift fixes, agent-loop discipline
  policy/schema, public trust doctrine, public threat modeling, and later
  validator feasibility;
- keep public-sync changes in the sibling public-sync clone only after a
  separate public-sync work order authorizes them.

Forbidden scope for this roadmap:

- no runtime/source/test implementation;
- no checker implementation;
- no provider/live/MCP proof;
- no production Memory/RAG release;
- no retrieval or vectorization release;
- no private or generated MinerU output read;
- no use-case/legal workflow;
- no direct import of external pack files as canonical CVF authority;
- no public-sync mutation until an authorized public-sync tranche opens.

## Authorization / Decision

Operator approved turning the `Gop y CVF` external critique into a roadmap and
work order after audit. R60/R63 left the current mode at stop/checkpoint unless
a fresh source-verified target is selected. This roadmap selects the fresh
target class:

`PUBLIC_TRUST_EXTERNAL_CRITIQUE_INTAKE_AND_AGENT_LOOP_POLICY_ABSORPTION`

## Why

The external critique surfaced public-facing trust issues that are cheap to
verify and materially affect CVF credibility:

- public workflow wording may drift between the README and catalog;
- provider certification wording may conflict across public docs;
- public docs index/current snapshot pointers may be stale;
- provider routing examples may look like public provider support claims;
- BUILD-stage agent behavior needs an auditable micro-loop policy before any
  future runtime enforcement is considered.

The roadmap preserves CVF's claim-boundary style: fix public contradictions
first, admit policy/schema next, and avoid runtime claims until tests, receipts,
or release gates exist.

## Non-Goals

- Do not copy the external folder into governed docs.
- Do not accept third-party article claims as CVF evidence without source
  verification.
- Do not create a global no-date filename rule for all governed CVF artifacts.
- Do not claim measured user trust, cost reduction, or runtime enforcement.
- Do not modify public-sync from this roadmap alone.
- Do not widen the completed MinerU foundation chain.

## Design Control Gate

| Design control | Roadmap handling | Verdict |
| --- | --- | --- |
| Scope boundary | Roadmap is intake/public-doc/policy-schema planning only | PASS |
| Non-goals | Runtime, checker, provider/live, production, and use-case lanes remain parked | PASS |
| Lane split | R64 intake decision; R65 public drift fix; R66 policy/schema; R67 trust/threat; R68 validator decision; R69 public snapshot; R70 provenance sync | PASS |
| Dependency/source-verification plan | R64 worker must recompute public drift evidence from current public-sync clone and classify every external item | PASS |
| Claim boundary | External critique remains advisory until CVF-owned artifacts accept or defer value | PASS |
| Acceptance criteria | Each tranche has observable artifacts and gate evidence | PASS |
| Verification/evidence | Roadmap requires source verification, external intake routing, and autorun gates before dispatch/closure | PASS |
| Dispatch-readiness decision | R64 may dispatch because it is docs-only intake/classification and does not mutate public-sync | PASS |

## Work Plan

| Tranche | Title | Objective | Primary output | Boundary |
| --- | --- | --- | --- | --- |
| R64 | External Critique Intake And Public Drift Decision | Classify the `Gop y CVF` pack, verify public drift candidates, and decide R65-R68 routing | worker return plus classification matrix | no public-sync edit, no runtime, no checker |
| R65 | Public P0 Drift Fix Execution | Repair verified public trust drift in the sibling public-sync clone | public docs patch and public-sync evidence | public-sync only; no new policy module beyond drift fixes |
| R66 | Agent Loop Discipline Policy And Schema Admission | Add BUILD-stage micro-loop doctrine, receipt schema, metrics, work-order addendum, and example | policy/schema docs | policy/schema-defined only, not runtime-enforced |
| R67 | Product Trust Doctrine And Public Threat Model | Add product-feeling doctrine, five-minute trust demo, threat model, and cost-loop posture | public trust docs | no measured UX or safety claim |
| R68 | Agent Loop Validator Feasibility Decision | Decide whether to implement receipt validator/checker or hold at schema level | decision packet | no checker until fresh authorization |
| R69 | Public Snapshot Refresh | Refresh public current-state/evidence index after accepted public docs changes | public snapshot/catalog evidence | public-safe summary only |
| R70 | Provenance Closure And Session Sync | Close the absorption lane, sync session state, and push appropriate repos | closure/session-sync | no new material scope |

## Acceptance Criteria

| Criterion | Evidence required | Status |
| --- | --- | --- |
| R64 dispatch packet exists | GC-018 baseline and work order under governed paths | READY_BY_THIS_ROADMAP |
| External critique is classified before action | R64 Required Absorption Table and classification matrix | PENDING_R64 |
| Public drift fixes happen only after verification | R65 source-verified public-sync work order | PENDING_R65 |
| Agent-loop discipline is bounded | R66 status uses policy/schema language, not runtime enforcement language | PENDING_R66 |
| Trust doctrine is bounded | R67 records no measured UX/safety claim without evidence | PENDING_R67 |
| Checker/runtime decision is separate | R68 release-or-hold decision before checker work | PENDING_R68 |
| Public/provenance boundary preserved | public-sync clone used for public changes; provenance stores private decision evidence | PENDING_R65_R70 |

## Verification / Evidence

Required lane-level verification:

- pre-dispatch autorun gate for each dispatch packet;
- worker-return fast gate for `WORKER_MUST_NOT_COMMIT` returns;
- reviewer-return commit steward for accepted returns;
- public-sync remote verification before public edits or push;
- separate material and session-sync commits in provenance when session state
  changes.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-provided critique -> external finding absorption workflow -> R64 classification matrix -> R65/R66/R67/R68 governed packets as needed |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this roadmap plus R64 work order and worker return |
| Disposition | ADAPT as governed roadmap and intake decision lane |
| Claim boundary | external critique is advisory input only; no external pack file becomes canonical authority by itself |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Roadmap/work-order/review packets in provenance | may read and classify external critique under governed work order | this roadmap and R64 dispatch packet | N/A with reason: internal governed docs lane only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | Public docs and future external-agent review guidance | public readers may see public-safe outcomes only after public-sync | future R65/R69 public artifacts if authorized | deferred adapter owner; no CLI/MCP runtime in this roadmap | DEFERRED_WITH_REASON |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | R64-R70 public trust and agent-loop absorption roadmap |
| claimDisposition | N/A with reason: roadmap-only sequencing and decision authority |
| receiptEvidence | N/A with reason: no runtime receipt in roadmap |
| actionEvidence | N/A with reason: downstream tranches must produce their own evidence |
| invocationBoundary | governed documentation and public-sync read-only planning |
| interceptionBoundary | no provider, runtime, public repository mutation, or checker interception claim |
| claimLanguage | sequence external critique absorption into bounded future packets |
| forbiddenExpansion | direct public-sync mutation, runtime/source/test/checker edits, provider/live proof, private-output read, and production readiness claims remain forbidden |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Purpose; Scope; Authorization / Decision; Why; Non-Goals; Design Control Gate; Work Plan; Acceptance Criteria; Verification / Evidence; External Knowledge Intake Routing; Dual Agent Surface Matrix; Public Export Disposition; Claim Boundary; ROADMAP_READY_FOR_R64_DISPATCH; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Gate runs are confirmation/evidence after checker source read-ahead, not first discovery. |
| claimBoundary | Read-ahead covers this roadmap and the immediate R64 dispatch lane only. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap is private provenance planning. Public-sync export may
occur only through a later authorized public-sync tranche from the sibling
public-sync clone.

## Claim Boundary

This roadmap authorizes R64 dispatch authoring and a docs-only external critique
classification lane. It does not authorize public-sync mutation, source/test
edits, runtime/provider/MCP proof, checker implementation, production
Memory/RAG release, private-output read, retrieval/vectorization, use-case/legal
workflow, direct external source import, hosted/public/production readiness
claim, or direct downstream release.
