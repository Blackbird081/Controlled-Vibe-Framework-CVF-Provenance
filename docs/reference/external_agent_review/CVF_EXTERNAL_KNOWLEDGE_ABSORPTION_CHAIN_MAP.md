# CVF External Knowledge Absorption Chain Map

Memory class: FULL_RECORD

Status: ACTIVE_CHAIN_MAP

docType: reference

## Purpose

Define the single CVF-owned sequence for absorbing external knowledge before it
can influence CVF standards, roadmaps, work orders, source, runtime claims, or
operator decisions.

This chain map connects the older legacy/corpus/blind-spot controls with the
new external-agent review folder and the existing GC-018, work-order,
source-verification, and autorun gates.

## Scope / Target / Owner Boundary

Target inputs:

- external repository or copied folder;
- legacy source family under `.private_reference/legacy/`;
- external-agent review packet or returned review output;
- public/simple CVF summary, public README, or public vocabulary assumption;
- corpus scan, extraction, registry, or intake evidence;
- operator-provided external comparison, critique, or recommendation.

Owner boundary: this artifact owns routing and required evidence order. It does
not make external material canonical, authorize public-sync, implement runtime
behavior, run providers, mutate source, create durable execution control, or
claim public/production/release/readiness.

## Central Core

CVF remains the source of truth.

External material is advisory until it is classified, source-verified, mapped
to a CVF owner surface, dispositioned, and promoted through a governed artifact.
No external file, copied repo, provider-local memory, public summary, or chat
claim can become CVF authority by itself.

## Mandatory Chain

Every external knowledge intake must follow this order unless a later governed
standard grants a narrower exception:

1. Identify input type.
2. Apply old authority, blind-spot, corpus, and provider-memory boundary
   guards that match the input.
3. If asking an external agent to review CVF, prepare the packet through
   `CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md` and
   `CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md`.
4. If absorbing returned external-agent output, classify each item through
   `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`.
5. Map accepted or deferred value to an existing CVF owner surface.
6. Record accept, adapt, defer, reject, or block disposition.
7. If implementation, source mutation, runtime claim, or roadmap execution is
   needed, open fresh GC-018 and a source-verified work order.
8. Execute the matching autorun gates before dispatch, implementation,
   closure, commit, or push.

Short form:

`External/corpus/repo input -> input router -> old authority/blind-spot/corpus guards -> external-agent packet/checklist when applicable -> returned-output absorption table when applicable -> promote/adapt/defer/reject/block -> GC-018/work order/source verification/autorun when implementation or governed action is needed`

## Input Type Router

| Input type | Required first route | Required owner surface | Minimum disposition |
| --- | --- | --- | --- |
| Legacy source family | Knowledge Absorption Blind-Spot Control Block and legacy coverage index lookup | Existing plane, workflow-chain, roadmap, or reference owner | `ACCEPT_NOW`, `ACCEPT_AS_DOCTRINE`, `ACCEPT_AS_OWNER_MAP`, `DEFER_DEMAND_GATED`, `REJECT_DIRECT`, or `OUT_OF_SCOPE` |
| External repo or copied folder | Root/folder lifecycle classification plus absorption map when retained | CVF-owned reference, map, roadmap, or work order | `ABSORB`, `ADAPT`, `DEFER`, `REJECT`, or `BLOCK` |
| External-agent packet request | External-agent review front door, context standard, packet template, and authoring checklist | External-agent review packet | `PACKET_READY`, `REWRITE_REQUIRED`, or `REJECT_RAW_REQUEST` |
| External-agent returned output | External finding absorption workflow and Required Absorption Table | Finding, standard, roadmap, work order, review, or absorption map | Matrix disposition from the absorption workflow |
| Public/simple CVF vocabulary | Public workflow-chain review context before using as evidence | Public-safe summary or governed internal standard | `QUESTION_OR_HYPOTHESIS` until source-verified |
| Corpus scan or extraction intake | Corpus scan registry standard and generated registry discipline | Corpus registry, scan packet, or extraction owner | `REGISTER`, `RECONCILE`, `DEFER`, `REJECT`, or `BLOCKED_SOURCE_NOT_FOUND` |
| Runtime/provider/MCP/readiness claim | Current runtime proof, live proof, MCP boundary, and work-order source verification | Runtime standard, completion review, receipt, or blocked finding | `BLOCKED_UNTIL_CVF_PROOF` unless current proof exists |

## Existing Guard Map

| Chain stage | Existing CVF surface | Enforcement state |
| --- | --- | --- |
| Authority boundary | `AGENTS.md`, `CVF_SESSION_MEMORY.md`, active state, active handoff | Machine-checked for session/front-door continuity |
| Provider-local memory boundary | `AGENTS.md` provider-specific memory boundary | Policy-bound; checked by review/gates where applicable |
| Knowledge blind-spot prevention | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Binding standard; work-order evidence required when applicable |
| Corpus registry | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Machine-checked generated aggregate |
| Legacy coverage visibility | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | Governed reference index; not yet a universal router |
| External review packet authoring | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md` | Reference/checklist |
| Returned-output classification | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Partial machine enforcement through required absorption table guard |
| Work-order source verification | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` and work-order dispatch-quality gate | Machine-checked for dispatch-ready work orders |
| Closure and autorun | Agent autorun workflow and closure-quality standards | Machine-checked in local hooks and autorun gates |

## Enforcement Gap

This chain map records a known gap: CVF has several machine checks for parts of
the sequence, but it does not yet have one universal trigger/router that
machine-enforces every external repo, review, corpus, or legacy intake through
this full chain.

Until that future router exists, agents must treat this chain map as the
required Central Core and use the most specific existing guard for each local
view.

## Machine-Check Candidate

A future checker may enforce:

- changed external knowledge intake artifacts cite this chain map;
- external-return reviews include the Required Absorption Table;
- legacy-adjacent implementation work orders include blind-spot control
  evidence and a legacy coverage index disposition;
- corpus-derived claims cite registry source and generated aggregate status;
- runtime/provider/MCP/readiness claims are blocked unless current CVF proof is
  cited.

That future checker requires a separate GC-018 and work order. This artifact
does not implement the checker.

## Claim Boundary

This chain map is a governance routing artifact. It does not prove complete
legacy absorption, public readiness, runtime behavior, provider governance,
MCP execution control, durable audit, or universal bypass prevention.
