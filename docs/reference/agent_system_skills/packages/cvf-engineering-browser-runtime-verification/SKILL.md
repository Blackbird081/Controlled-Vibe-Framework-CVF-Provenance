# CVF ASSF Package: Engineering Browser Runtime Verification

Memory class: FULL_RECORD

Status: PROPOSED

docType: assf_package

Batch ID: AGSK-R3

skillId: cvf-engineering-browser-runtime-verification

## Purpose

Guide real-browser verification practices including DOM inspection, console error capture, network analysis, and performance profiling. Use when a governed CVF task needs to verify browser-rendered output, diagnose UI issues, or confirm that a fix works in a live browser context. Do not use when: the upstream MCP server dependency (Chrome DevTools MCP) is required as runtime authority, CLI/MCP execution, provider/live proof, production invocation, or authority beyond the active governed work order is required.

CVF adaptation note: the upstream skill requires a chrome-devtools MCP server. This package root records that dependency as an upstream source fact; no MCP server installation, configuration, or invocation is authorized by this PROPOSED package. MCP adapter support requires a separate ASSF adapter work order.

## Scope / Applies-To

| Field | Value |
|---|---|
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-browser-runtime-verification/` |
| Owner surface | ASSF package proposal evidence under AGSK-R3 |
| Applies to | Metadata-only advisory package review, not runtime execution |
| Does not apply to | `APPROVED`, `ACTIVE`, resolver/runtime mutation, CLI/MCP adapter, provider/live proof, public-sync, or production readiness |

## Invocation Boundary

| Field | Value |
|---|---|
| Allowed task classes | browser-testing, ui-verification, runtime-debugging, performance-profiling |
| Allowed roles | dispatcher, worker, reviewer |
| Allowed phases | INTAKE, DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE |
| Allowed surfaces | docs/reference/agent_system_skills/packages/cvf-engineering-browser-runtime-verification/, registry entries, review artifacts |
| Risk ceiling | R1 |
| Authority ceiling | metadata-only advisory; loading never authorizes MCP installation, browser automation, runtime execution, or external actions |

## Inputs And Outputs

| Field | Value |
|---|---|
| Inputs | operator request or governed task context; source mirror file `.private_reference/source_mirrors/addyosmani__agent-skills/skills/browser-testing-with-devtools/SKILL.md`; active CVF authority and allowed-scope boundaries |
| Outputs | proposed package-body guidance (awaiting reviewer acceptance); browser verification discipline notes; recommended CVF owner-surface routing |
| Acceptance evidence | AGSK-R3 worker return with package-root proposal evidence; reviewer-fast gate PASS; anatomy checker PASS; MCP adapter boundary documented |

## Risk And Authority

| Field | Value |
|---|---|
| Risk class | R1 |
| Authority ceiling | metadata-only advisory selection; upstream MCP dependency is NOT granted as CVF runtime authority |
| Side effects | none from metadata reading; browser automation, MCP server installation, or DevTools invocation requires separate authorization and adapter work order |
| Rollback | delete this package root and revert registry entry to CANDIDATE; regenerate generated index |
| Safe stop | stop and open a fresh ASSF MCP-adapter or runtime tranche if chrome-devtools MCP configuration, browser automation, or authority above the active work order is needed |
| Policy bindings | none until APPROVED or ACTIVE lifecycle state with separate reviewer authorization; MCP adapter requires dedicated adapter work order |

## Progressive Disclosure

| Stage | Accessible fields |
|---|---|
| Metadata-only (CANDIDATE/PROPOSED) | skillId, name, status, purpose, triggerPatterns, riskCeiling, sourceArtifacts; MCP dependency noted as source fact only |
| Post-reviewer-acceptance (APPROVED) | full package-body guidance excluding MCP runtime invocation; requires reviewer decision gate |
| Runtime (ACTIVE) | full instructions with active resolver; MCP adapter requires separate adapter work order regardless of lifecycle state |

## Evidence And UAT

| Field | Value |
|---|---|
| Required evidence | AGSK-R3 worker return with source reads and 24-candidate coverage table; anatomy checker PASS |
| UAT binding | NOT_STARTED; APPROVED tranche requires UAT evidence and reviewer acceptance; MCP integration requires additional UAT scope |
| Validation hooks | ASSF anatomy checker; generated-index drift checker; reviewer-fast gate |
| Review evidence | docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md |

## External Disposition

| Field | Value |
|---|---|
| External CLI/MCP disposition | DEFERRED_WITH_REASON: upstream skill's Chrome DevTools MCP dependency is not imported as CVF adapter; separate MCP adapter work order required |
| Adapter contract | N/A with reason: MCP adapter not authored in AGSK-R3; upstream MCP server config is not CVF runtime authority |
| Adapter evidence | N/A with reason: no adapter implemented |
| External mutation boundary | no MCP server install, browser automation, DevTools invocation, CLI/MCP export, or package activation until separate ASSF adapter or runtime work order accepted |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | AGSK-R3 worker with reviewer packet-shape repair |
| Provider or surface | Local workspace |
| Session or invocation | AGSK-R3 package proposal execution, 2026-06-29 |
| Working directory | Repository root |
| Command or tool surface | PowerShell, repo-local Python governance checkers, apply_patch |
| Target paths | `docs/reference/agent_system_skills/packages/cvf-engineering-browser-runtime-verification/` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` |
| Before status evidence | package root did not exist before AGSK-R3 worker execution |
| After status evidence | package root exists in PROPOSED state pending reviewer acceptance |
| Diff evidence | `git diff --name-status` over AGSK-R3 range |
| Approval boundary | WORKER_MUST_NOT_COMMIT; reviewer/closer owns acceptance and commit |
| Claim boundary | PROPOSED package-root evidence only; no runtime activation claim |
| Agent type | worker plus reviewer packet-shape repair |
| Invocation ID | `agsk-r3-package-cvf-engineering-browser-runtime-verification-2026-06-29` |
| Expected manifest | `SKILL.md`; `skill.source.json`; `README.md` |
| Actual changed set | `SKILL.md`; `skill.source.json`; `README.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

### Expected Result / Prediction

A PROPOSED ASSF package root should preserve the upstream skill's useful workflow discipline while keeping CVF authority, lifecycle, and runtime boundaries explicit.

### Evidence Comparison

The package cites the pinned upstream source mirror, the AGSK-R2 source-mirror backfill review, the AGSK-R3 baseline, and the AGSK-R3 worker return. The package remains PROPOSED and does not claim APPROVED, ACTIVE, UAT, certification, runtime execution, provider behavior, or external adapter support.

### Contradiction Or Gap Disposition

No contradiction is resolved inside the package root. Any missing reviewer acceptance, UAT, certification, runtime loader, CLI/MCP adapter, provider proof, public export, or production-readiness evidence remains a blocker for later promotion.

### Claim Update

The package claim is narrowed to CVF-owned PROPOSED package-root evidence only. It is not activation evidence.
## Claim Boundary

This package root is a PROPOSED CVF adaptation sourced from the upstream `browser-testing-with-devtools` skill at pinned commit `aba7c4e9695c363e65cb59effe926c7f1d1abe3d`. The upstream MCP server dependency is recorded as a source fact, not imported as CVF runtime authority. This package does not activate the skill, install MCP servers, invoke Chrome DevTools, authorize browser automation, implement a CLI/MCP adapter, or claim automatic invocation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this package root cites private source mirror and private provenance registry surfaces. Public-safe publication requires separate redaction and public-sync authorization.


