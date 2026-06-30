# CVF GC-018 - KIOD-R4 Negative Search Evidence Decision

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-30

docType: baseline

dispatchBaseHead: b510be26

Batch ID: KIOD-R4

## Purpose

Authorize a narrow KIOD-R4 decision tranche before the next source repo/folder
intake pilot. KIOD-R4 decides whether missing-owner negative-search evidence
must become a machine-enforced checker requirement now, remain a required
packet/reference block for now, or stay blocked pending a concrete pilot.

This tranche is decision and worker-return only. It does not authorize checker
implementation, a new owner surface, runtime behavior, MCP or CLI adapter work,
provider/live proof, public-sync, dashboard work, source import, or production
readiness claims.

## Operator Authorization

The operator directed the next tranche after KIOD-R1 through KIOD-R3 and asked
for a work order for Claude to execute. This baseline treats Claude as the
operator-selected worker surface while preserving CVF's role-neutral worker,
reviewer, closer, and session-sync boundaries.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-30 next tranche and work order for Claude | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V29_2026-06-30.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| KIOD-R1 owner-surface taxonomy | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | ACCEPT |
| KIOD-R2 pre-scan packet standard | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | ACCEPT |
| KIOD-R3 overlap routing matrix | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | ACCEPT |
| External knowledge intake routing guard | `governance/compat/check_external_knowledge_intake_routing.py` | ACCEPT |
| External overlap discipline guard | `governance/compat/check_external_absorption_overlap_discipline.py` | ACCEPT |
| Agent Handoff Contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |
| Dual Agent Surface Accounting Standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | ACCEPT |

Provider-local files were not used as authority. This dispatch is based on
repo-local standards, active continuity surfaces, and KIOD-R1 through KIOD-R3.

## Scope / Owner Boundary

Allowed worker scope:

- create `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_WORKER_RETURN_2026-06-30.md`;
- inspect KIOD-R1 through KIOD-R3 and the current guard surfaces cited in this
  baseline and paired work order;
- return a decision recommendation using exactly one of
  `CHECKER_REQUIRED_NOW`, `PACKET_BLOCK_REQUIRED_NOW`, or
  `BLOCKED_PENDING_PILOT_EVIDENCE`.

Reviewer/closer scope:

- review the worker return and decide whether to close KIOD-R4 as accepted,
  return it for repair, or open a follow-up checker/reference tranche;
- update this baseline, the paired work order, completion review, and
  session-sync surfaces only if closure or next-move state changes.

Forbidden worker scope:

- no checker implementation or hook wiring;
- no new owner surface, roadmap tranche, runtime behavior, source import, MCP
  or CLI adapter, provider/live proof, public-sync, dashboard, generated
  aggregate, dependency install, or production-readiness claim;
- no edits to `CVF_SESSION/**`, active handoff, `AGENTS.md`, KIOD-R1, KIOD-R2,
  KIOD-R3, or the KIOD-T0 roadmap.

Risk ceiling: R0/R1 documentation decision only.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON` with only this worker-owned artifact created:

- `docs/reviews/CVF_KIOD_R4_NEGATIVE_SEARCH_EVIDENCE_DECISION_WORKER_RETURN_2026-06-30.md`

No commit is authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: KIOD-R4 is ready for worker dispatch as a bounded
negative-search evidence decision tranche.

Proposed tranche: `KIOD-R4 Negative Search Evidence Decision`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; Claude executes as worker without committing; reviewer/closer reviews,
repairs only allowed-scope packet defects, and commits accepted material if
gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| KIOD-R1 routes missing owner cases to R4-style decision | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | lines 44, 61, 69 | `OWNER_SURFACE_NOT_FOUND` | KIOD-R1 owner-surface taxonomy | ACCEPT |
| KIOD-R2 says novelty candidates are blocked when negative-search evidence is absent | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | lines 37, 40, 51, 62, 71 | negative-search evidence | KIOD-R2 pre-scan packet standard | ACCEPT |
| KIOD-R3 requires routing to KIOD-R4 before a new owner is created | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | lines 34, 37, 45, 54, 63 | `NEW_FINDING` | KIOD-R3 overlap routing matrix | ACCEPT |
| External knowledge intake routing artifacts must include seven routing fields | `governance/compat/check_external_knowledge_intake_routing.py` | lines 29-38 | `REQUIRED_FIELDS` | external knowledge intake routing guard | ACCEPT |
| Routing input type for operator comparison is allowed | `governance/compat/check_external_knowledge_intake_routing.py` | lines 38-48 | operator-provided external comparison, critique, or recommendation | external knowledge intake routing guard | ACCEPT |
| Overlap classification allows missing-owner and new-finding tokens | `governance/compat/check_external_absorption_overlap_discipline.py` | lines 65-78, 384-387 | `OWNER_SURFACE_NOT_FOUND`; `NEW_FINDING` | external overlap discipline guard | ACCEPT |
| WORKER_MUST_NOT_COMMIT requires reviewer closure conversion fields | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | lines 235-248, 315-326 | `Reviewer Closure Conversion` | Agent Handoff Contract | ACCEPT |
| Dual agent accounting requires internal and external CLI/MCP rows before dispatch | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in KIOD-R4 | Runtime status | Reason |
|---|---|---|---|
| `CHECKER_REQUIRED_NOW` | KIOD-R4 worker decision vocabulary | DOC_ONLY_NEW | recommends a follow-up checker tranche; does not implement the checker |
| `PACKET_BLOCK_REQUIRED_NOW` | KIOD-R4 worker decision vocabulary | DOC_ONLY_NEW | keeps negative-search evidence as required packet/reference content for now |
| `BLOCKED_PENDING_PILOT_EVIDENCE` | KIOD-R4 worker decision vocabulary | DOC_ONLY_NEW | blocks the decision until a concrete pilot reveals the evidence shape |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`knowledge-intake-deduplication`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

Resolver command:

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class knowledge-intake-deduplication --role dispatcher --lifecycle-phase dispatch --json
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | KIOD-R1 through KIOD-R4 governed packet chain | internal worker/reviewer decision guidance only; no runtime mutation or commit by worker | this GC-018 and paired work order | N/A with reason: internal governed-document workflow only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP intake adapter surface | no external adapter behavior is authorized in KIOD-R4 | Dual Agent Surface Accounting Standard and KIOD-R4 forbidden scope | DEFERRED_WITH_REASON: adapter design needs a separate source-verified tranche | DEFERRED_WITH_REASON |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Missing-owner negative-search evidence discipline | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md`; `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md`; `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | ENRICH_EXISTING | R1-R3 identify the gap but do not yet decide checker versus packet block | dispatch KIOD-R4 decision before any next source repo/folder intake pilot |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request to tighten knowledge-intake de-duplication after CodeGraph scan findings to KIOD-R4 decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | KIOD-R4 Negative Search Evidence Decision |
| Disposition | ADAPT as CVF-owned negative-search evidence decision discipline |
| Claim boundary | operator critique remains input only until promoted through this governed dispatch and reviewer closure |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `b510be26`.
- `git status --short` was clean before KIOD-R4 dispatch authoring.
- ADIF resolver returned zero defects for the KIOD-R4 dispatch query.
- Source verification was refreshed against KIOD-R1, KIOD-R2, KIOD-R3, routing
  guard, overlap guard, handoff contract, and dual-agent standard.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b510be26 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base b510be26 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base b510be26 --head HEAD --enforce
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: KIOD-R4 is a private provenance governance decision dispatch. Public
export requires a separate public-sync tranche from the sibling public-sync
repository.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | KIOD-R4 negative-search evidence decision dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed document dispatch and worker-return review only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or runtime interception claim |
| claimLanguage | decision discipline only; not checker implementation |
| forbiddenExpansion | no checker, runtime, MCP/CLI adapter, provider/live, public-sync, dashboard, source import, or production-readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local workspace |
| Session or invocation | KIOD-R4 dispatch authoring, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | source reads, rg, ADIF resolver, apply_patch, governance gates |
| Target paths | this baseline and paired KIOD-R4 work order |
| Allowed scope source | operator request for next tranche and work order for Claude after KIOD-R1-R3 |
| Before status evidence | clean HEAD `b510be26` |
| After status evidence | pending pre-dispatch gate evidence before commit |
| Diff evidence | real-range name-status and governance gate output before commit |
| Approval boundary | decision dispatch only |
| Claim boundary | no checker implementation, runtime, source import, provider/live, public-sync, or adapter behavior |
| Agent type | dispatch author |
| Invocation ID | `cvf-kiod-r4-negative-search-evidence-decision-dispatch-2026-06-30` |
| Expected manifest | this baseline; paired work order |
| Actual changed set | pending dispatch authoring |
| Manifest delta | pending pre-dispatch review |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes only the KIOD-R4 worker decision. It does not decide
the final governance outcome by itself, implement a checker, open a new owner
surface, or authorize the next source repo/folder intake pilot.
