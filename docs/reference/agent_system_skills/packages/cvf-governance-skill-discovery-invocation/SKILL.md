# CVF ASSF Package: Governance Skill Discovery And Invocation

Memory class: FULL_RECORD

Status: ACTIVE

docType: assf_package

Batch ID: AGSK-R3; ASCP-P4-P6

skillId: cvf-governance-skill-discovery-invocation

## Purpose

Guide metadata-first skill discovery, invocation boundaries, and skill selection without global instruction loading or authority expansion.

Use when a governed CVF task matches the `using-agent-skills` package pattern after explicit package selection and receipt-backed production execution. Do not use as autonomous runtime authority, provider routing authority, public-sync proof, merge approval, commit permission, or permission to bypass active CVF work-order gates.

## Scope / Applies-To

| Field | Value |
|---|---|
| Package root | `docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/` |
| Owner surface | ASSF package proposal evidence under AGSK-R3 and production scale-up evidence under ASCP-P4-P6 |
| Applies to | ACTIVE receipt-backed production package execution through CVF adapters after explicit request |
| Does not apply to | automatic invocation, full MCP server behavior, provider router mutation, public-sync, merge execution, commit authority, filesystem/browser authority, or downstream action authority |

## Invocation Boundary

| Field | Value |
|---|---|
| Allowed task classes | skill-selection, context-routing, governance-orientation |
| Allowed roles | dispatcher, worker, reviewer |
| Allowed phases | INTAKE, DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE |
| Allowed surfaces | docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/, registry entries, truth packets, review artifacts |
| Risk ceiling | R0 |
| Authority ceiling | bounded advisory package guidance; loading never authorizes commit, merge, provider routing, public, production action, filesystem, browser, or external actions |

## Inputs And Outputs

| Field | Value |
|---|---|
| Inputs | operator request or governed task context; source mirror file `.private_reference/source_mirrors/addyosmani__agent-skills/skills/using-agent-skills/SKILL.md`; active CVF authority and allowed-scope boundaries |
| Outputs | bounded package guidance after explicit production executor request; risk trigger notes; recommended CVF owner-surface routing; receipt-backed source-truth trace for package use |
| Acceptance evidence | AGSK-R3 worker return; AGSK-R5 eligibility audit; SCPL-T2 selection profile coverage; ASCP-P4-P6 production scale-up completion; generated index checks; representative live proof |
| Trigger patterns | using agent skills, skill discovery, skill invocation, which skill applies, meta skill |

## Worked Discovery Practice Examples

These three examples translate the abstract `skill-selection`,
`context-routing`, and `governance-orientation` task classes above into
concrete input/decision/output/authority steps. They illustrate existing
metadata-selection guidance only; they introduce no new task class,
trigger pattern, registry field, or runtime behavior, and none of them
authorizes package invocation, execution, or action beyond what the
Invocation Boundary above already states.

### Example 1: Dispatcher, `skill-selection`

- **Input**: a candidate task description ("author a work order for a
  bounded package-content enrichment") and the active work-order scope
  under authoring.
- **Evidence/match**: the dispatcher compares the task description
  against this registry entry's `triggerPatterns` ("using agent skills",
  "skill discovery", "skill invocation", "which skill applies", "meta
  skill") and `taskClasses`. If the candidate task is itself about
  choosing or citing a package for a work order, `skill-selection`
  matches; if the task instead concerns, for example, database schema
  design, no `triggerPatterns` match and no `taskClasses` apply.
- **Decision**: on a match, the dispatcher selects this package as one
  Allowed Read for the work order. On no match, the dispatcher records a
  correct no-match and does not force a best-effort selection.
- **Output**: a recommended package citation added to the work order's
  Allowed Reads section (metadata selection only), or, on no match, no
  citation at all.
- **Authority result**: selection grants only a recommended Allowed Read.
  It does not create a new Allowed Write, execution authority, or
  invocation permission; those remain separately governed by the work
  order the dispatcher is authoring.

### Example 2: Worker, `context-routing`

- **Input**: a work order that already names this package (or another
  specific package) among its Allowed Reads, dispatched to the worker.
- **Evidence/match**: the worker reads the work order's Allowed Reads
  list and confirms which package(s) the dispatcher already authorized,
  then opens the matching package body to confirm it is the one the
  dispatcher intended (for example, checking `skillId` and `Package
  root` against the work order's citation).
- **Decision**: the worker routes to the already-named package body only.
  The worker does not use `context-routing` to discover or add a package
  the dispatcher did not name, and does not treat this package's own
  guidance as authority to expand the work order's scope.
- **Output**: confirmation, internal to the worker's own execution
  trace, that the correct already-authorized package body was consulted.
- **Authority result**: no new selection authority is created. The
  worker's Allowed Reads and Allowed Writes remain exactly what the
  dispatching work order already states.

### Example 3: Reviewer, `governance-orientation`

- **Input**: a worker return that cites having consulted this package
  (or another specific package) during the worker's execution.
- **Evidence/match**: the reviewer compares the citation against the
  governing work order's Allowed Reads, and against this package's own
  Invocation Boundary fields (`Allowed roles`, `Allowed phases`, `Risk
  ceiling`), to check whether the citation was in-bounds.
- **Decision**: three outcomes are possible. (a) The citation matches the
  work order's Allowed Reads and this package's Invocation Boundary: the
  reviewer accepts the citation. (b) The citation is broader than what
  actually applied (for example, the worker claims a `reviewer`-role use
  while filing as `worker`): the reviewer narrows the claim rather than
  accepting it as stated. (c) The citation names a package the work order
  never authorized as an Allowed Read: the reviewer rejects the citation
  as out-of-scope package use.
- **Output**: an accept, narrow, or reject disposition recorded in the
  reviewer's own completion evidence, without the reviewer re-deriving or
  re-executing the worker's original task.
- **Authority result**: the reviewer's disposition governs only whether
  the citation is accepted as compliant; it does not itself grant, retract,
  or expand any package's Invocation Boundary, and it does not recreate
  the worker's implementation.

## Risk And Authority

| Field | Value |
|---|---|
| Risk class | R0 |
| Authority ceiling | bounded advisory package guidance only |
| Side effects | none from metadata or package-body loading; actions require separate governed authorization |
| Rollback | restore this package root and registry entry to pre-ASCP-P4-P6 PROPOSED state; remove matching truth packet; regenerate generated indexes |
| Safe stop | stop if ACTIVE source checks, receipt checks, provider diagnostics, or governed work-order authority are missing |
| Policy bindings | ASCP-P4-P6 permits explicit receipt-backed production execution only; no automatic invocation or action authority |

## Progressive Disclosure

| Stage | Accessible fields |
|---|---|
| Metadata selection | skillId, name, domain, purpose, triggerPatterns, riskCeiling, sourceArtifacts |
| Production dry-run | package body may be read only with explicit receipt-backed loader request |
| Production live proof | provider output may be consumed only as proof evidence with usage, policy, use-proof, and production execution receipts |

## Evidence And UAT

| Field | Value |
|---|---|
| Required evidence | AGSK-R3 worker return; AGSK-R5 runtime eligibility audit; SCPL-T2 selection guidance; ASCP-P4-P6 completion review; anatomy checker PASS; certified metadata admission checker PASS; truth packet checker PASS |
| UAT binding | PASSED for explicit receipt-backed production package execution |
| Validation hooks | ASSF anatomy checker; certified metadata admission checker; truth packet checker; package productionization pipeline checker; generated-index drift checker |
| Review evidence | docs/reviews/CVF_ASCP_P4_P6_REMAINING_PACKAGE_PRODUCTION_SCALE_UP_COMPLETION_2026-06-30.md |

## External Disposition

| Field | Value |
|---|---|
| External CLI/MCP disposition | IMPLEMENTED: bounded CLI/MCP envelope delegates to CVF production package executor |
| Adapter contract | docs/reference/agent_system_skills/CVF_ASSF_PRODUCTION_PACKAGE_SCALE_UP_STANDARD.md |
| Adapter evidence | docs/reviews/CVF_ASCP_P4_P6_REMAINING_PACKAGE_PRODUCTION_SCALE_UP_COMPLETION_2026-06-30.md |
| External mutation boundary | external CLI/MCP wrapper may return receipt-backed package execution envelopes only; no external mutation, daemon behavior, public API, provider routing, public-sync, commit, or merge authority is permitted |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace plus representative Alibaba DashScope-compatible live model proof |
| Session or invocation | ASCP-P4-P6 package production scale-up, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | mechanical package source rewrite, generated indexes, dry-run smoke, live provider proof, governance gates |
| Target paths | `docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_P4_P6_REMAINING_PACKAGE_PRODUCTION_SCALE_UP_2026-06-30.md` |
| Before status evidence | package root existed in PROPOSED state before ASCP-P4-P6 |
| After status evidence | package root exists in ACTIVE state with receipt-backed production execution boundary |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | ASCP-P4-P6 remaining-package production scale-up only |
| Claim boundary | ACTIVE package-root production evidence only; no automatic invocation or action authority |
| Agent type | reviewer/closer |
| Invocation ID | `ascp-p4-p6-package-cvf-governance-skill-discovery-invocation-2026-06-30` |
| Expected manifest | `SKILL.md`; `skill.source.json`; `README.md`; registry entry; truth packet |
| Actual changed set | `SKILL.md`; `skill.source.json`; `README.md`; registry entry; truth packet |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

### Expected Result / Prediction

An ACTIVE ASSF package root should preserve useful upstream workflow discipline while keeping CVF authority, lifecycle, and runtime boundaries explicit.

### Evidence Comparison

The package cites the pinned upstream source mirror, AGSK-R3 package-root creation, AGSK-R5 eligibility audit, SCPL-T2 selection guidance, and ASCP-P4-P6 production scale-up evidence. The package is ACTIVE for explicit receipt-backed production execution only and does not claim automatic invocation, provider routing, public export, or action authority.

### Contradiction Or Gap Disposition

ASCP-P4-P6 resolves the prior UAT, certification, internal-disposition, truth-packet, and adapter-evidence gaps for this package. Full MCP server behavior, provider registry mutation, public export, and downstream action authority remain separate future work.

### Claim Update

The package claim is updated to CVF-owned ACTIVE production package evidence with receipt-backed execution only.

## Claim Boundary

This package root is an ACTIVE CVF adaptation sourced from the upstream `using-agent-skills` skill at pinned commit `aba7c4e9695c363e65cb59effe926c7f1d1abe3d`. It may be opened only through CVF receipt-backed production package adapters under active governed work-order authority. It does not execute actions autonomously, trigger merges, mutate provider routing, publish public artifacts, or claim automatic invocation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this package root cites private source mirror, private provenance registry surfaces, and production package proof evidence. Public-safe publication requires separate redaction and public-sync authorization.
