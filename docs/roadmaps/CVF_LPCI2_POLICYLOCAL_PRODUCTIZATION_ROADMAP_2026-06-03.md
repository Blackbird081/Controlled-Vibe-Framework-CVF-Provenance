# CVF LPCI2 PolicyLocal Productization Roadmap

Memory class: FULL_RECORD

Status: T1_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-03

executionBaseHead: `3ff90651`

## Purpose

Convert the closed LPCI1 governance and template chain into a product-facing
PolicyLocal build path. PolicyLocal is the local-first legal/policy corpus
intelligence application target for users who want to search, cite, and query
their own law, policy, notice, decision, SOP, or internal governance corpus.

This roadmap starts after LPCI1-T1 through LPCI1-T7 are
`CLOSED_PASS_BOUNDED`. It is not a continuation of worker dispatch; it is a
self-executed productization control path until the operator reopens external
worker delegation.

## Scope / Applies To

Applies to: PolicyLocal productization, local workspace adoption, future
production-corpus pilot planning, and any later UI/API implementation for the
legal/policy chatbot use case.

Owner surface: CVF governance layer; LPCI product surface; PolicyLocal local
workspace.

## Authority Chain

| Authority | Path | Disposition |
| --- | --- | --- |
| Operator instruction | chat instruction on 2026-06-03 to let Codex hold multiple roles and finish without external worker handoff | ACCEPT |
| LPCI1 MVP roadmap | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | ACCEPT |
| LPCI1-T7 template packaging spec | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | ACCEPT |
| PolicyLocal frontend handoff | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CLAUDE_BUILD_HANDOFF.md` | ACCEPT as external workspace input |
| Codex PolicyLocal addendum | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CODEX_POLICYLOCAL_SPEC_REVIEW_2026-06-02.md` | ACCEPT as external workspace input |

## Roadmap

| Tranche | Goal | Output | Status |
| --- | --- | --- | --- |
| LPCI2-T1 | PolicyLocal build control packet | repo reference packet plus workspace copy tying Claude spec to LPCI1 rules | CLOSED_PASS_BOUNDED |
| LPCI2-T2 | Product scaffold readiness decision | decide whether to scaffold Next.js app now, defer, or require production-corpus pilot first | PROPOSED |
| LPCI2-T3 | Production-corpus pilot planning | define first real corpus, GC-051 registration, legal/policy domain fields, and sampling plan | PROPOSED |
| LPCI2-T4 | Local runtime implementation | implement bounded local app only after T2/T3 decision | HOLD_UNTIL_T2_T3_PASS |

## Work Plan

| Step | Action | Output | Status |
| --- | --- | --- | --- |
| W1 | Create PolicyLocal build-control packet | repo reference plus external workspace copy | CLOSED_PASS_BOUNDED |
| W2 | Decide scaffold readiness | future T2 readiness decision | PROPOSED |
| W3 | Plan production-corpus pilot | future T3 pilot plan | PROPOSED |
| W4 | Implement bounded local runtime | future T4 app implementation | HOLD_UNTIL_T2_T3_PASS |

## Decision

Proceed with LPCI2-T1 only in this batch. The immediate risk is not lack of UI
ideas. The risk is that a polished app could be built while CVF/LPCI controls
remain implied. T1 closes that gap by creating an explicit build control packet.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| LPCI1 inheritance preserved | packet cites T1-T7 specs and answer-boundary rules |
| PolicyLocal handoff constrained | Claude frontend spec is accepted only with CVF addendum gates |
| External workspace copy present | packet saved under `CVF-Workspace\PolicyLocal` |
| Runtime boundary preserved | no app code, API route, DB file, provider call, corpus ingestion, or public-sync |
| Next move clear | T2/T3/T4 dependency order recorded |

## Verification Evidence

| Evidence | Path |
| --- | --- |
| Work order | `docs/work_orders/CVF_WO_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Repo build-control packet | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Completion review | `docs/reviews/CVF_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_COMPLETION_2026-06-03.md` |
| Session sync authorization | `docs/reviews/CVF_LPCI2_T1_SESSION_SYNC_AUTH_2026-06-03.md` |
| Workspace copy | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal\CVF_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |

## Non-Goals

- Build the PolicyLocal app.
- Import a real legal/policy corpus.
- Run provider calls or live legal answer tests.
- Claim legal advice, current law status, production readiness, or public
  release readiness.
- Push or sync artifacts to the public CVF repository.

## Claim Boundary

This roadmap claims only that LPCI2-T1 created a reusable build control packet
and copied it to the local PolicyLocal workspace.

It does not claim runtime implementation, production corpus readiness, legal
answer correctness, hosted readiness, or public export.

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` - after LPCI1 closure, PolicyLocal had a strong
frontend handoff but no single product build control packet that made LPCI
rules mandatory for implementation.

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` - LPCI2-T1 creates the productization packet and
records the no-external-worker self-execution boundary.

Next control action: `CLOSED` for T1; T2/T3/T4 remain proposed and must not be
treated as implemented.

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: LPCI2-T1 is documentation and productization control only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap references a private local workspace path and internal
LPCI governance chain. A sanitized public-facing guide may be prepared later as
a separate public-sync batch.
