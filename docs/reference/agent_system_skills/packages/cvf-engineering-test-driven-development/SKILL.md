# CVF ASSF Package: Engineering Test-Driven Development

Memory class: FULL_RECORD

Status: ACTIVE

docType: assf_package

Batch ID: AGSK-R3; AGSK-R7

skillId: cvf-engineering-test-driven-development

## Purpose

Guide failing-test-first development discipline: write a failing test before writing the code that makes it pass; reproduce bugs with tests before fixing them. Tests are proof  -  "seems right" is not done. Use when a governed CVF task needs to implement new logic, fix bugs, modify existing functionality, or handle edge cases. Do not use when: runtime activation, automated test execution without oversight, live test runner integration, provider/live proof, or authority beyond the active governed work order is required.

## Scope / Applies-To

| Field | Value |
|---|---|
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-test-driven-development/` |
| Owner surface | ASSF proposal evidence under AGSK-R3, bounded AGSK-R7 promotion evidence, and current ASCP-P1-P3 ACTIVE production package contract |
| Applies to | ACTIVE receipt-backed production package execution through CVF adapters after explicit request |
| Does not apply to | automatic invocation, CLI/MCP adapter beyond the implemented receipt-backed wrapper, provider/live proof, public-sync, test execution authority, commit authority, or production readiness |

## Invocation Boundary

| Field | Value |
|---|---|
| Allowed task classes | test-authoring, tdd-implementation, bug-reproduction, regression-testing |
| Allowed roles | dispatcher, worker, reviewer |
| Allowed phases | INTAKE, DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE |
| Allowed surfaces | docs/reference/agent_system_skills/packages/cvf-engineering-test-driven-development/, registry entries, review artifacts |
| Risk ceiling | R1 |
| Authority ceiling | bounded advisory package guidance through the receipt-backed loader; loading never authorizes automated test runner execution, CI integration, or external actions |

## Inputs And Outputs

| Field | Value |
|---|---|
| Inputs | operator request or governed task context; source mirror file `.private_reference/source_mirrors/addyosmani__agent-skills/skills/test-driven-development/SKILL.md`; active CVF authority and allowed-scope boundaries |
| Outputs | bounded failing-test-first guidance, Prove-It Pattern, and test structure notes after explicit authorized package use; recommended CVF owner-surface routing |
| Acceptance evidence | AGSK-R3 proposal and AGSK-R7 promotion reviews; ASCP-P1-P3 six-package ACTIVE source admission, focused executor and CLI/MCP tests, and one live exemplar for a different skill ID |

## Risk And Authority

| Field | Value |
|---|---|
| Risk class | R1 |
| Authority ceiling | bounded advisory package guidance only; package use does not grant test-runner, CI, commit, provider, public, or external-action authority |
| Side effects | none from metadata reading; automated test execution, CI wiring, or commit requires separate authorization |
| Rollback | revert only a later authorized change under its owning work order and review; this guidance does not authorize deleting or demoting the existing ACTIVE package |
| Safe stop | stop if ACTIVE source checks, required receipts, or governed work-order authority are missing; automated test execution, CI integration, or broader action authority requires separate authorization |
| Policy bindings | AGSK-R7 and ASCP-P1-P3 establish the bounded ACTIVE production package path; the active governed work order, activation policy, required receipts, and production runtime standard remain binding |

## Progressive Disclosure

| Stage | Accessible fields |
|---|---|
| Metadata-only (CANDIDATE/PROPOSED) | skillId, name, status, purpose, triggerPatterns, riskCeiling, sourceArtifacts |
| Post-reviewer-acceptance (historical APPROVED, AGSK-R6/R7) | full failing-test-first protocol and Prove-It Pattern; reviewer decision gate already satisfied |
| Runtime (ACTIVE, current) | full instructions readable through the receipt-backed production package loader under a governed work order; ASCP-P1-P3 established six-package ACTIVE admission and focused adapter tests, with one live exemplar for `cvf-engineering-spec-driven-development`, not a TDD-specific live run |

## Evidence And UAT

| Field | Value |
|---|---|
| Required evidence | AGSK-R3 worker return with source reads and 24-candidate coverage table; anatomy checker PASS; ASCP-P1-P3 six-package ACTIVE admission and focused production executor/CLI-MCP tests; its live E2E exemplar used `cvf-engineering-spec-driven-development`, not this package |
| UAT binding | PASSED for receipt-backed production package execution through CVF adapters |
| Validation hooks | ASSF anatomy checker; certified metadata admission checker; generated-index drift checker; reviewer-fast gate |
| Review evidence | docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md; docs/reviews/CVF_AGSK_R7_RUNTIME_PACKAGE_BATCH_PROMOTION_COMPLETION_2026-06-30.md; docs/reviews/CVF_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_COMPLETION_2026-06-30.md |

## External Disposition

| Field | Value |
|---|---|
| External CLI/MCP disposition | IMPLEMENTED: bounded CLI/MCP envelope delegates to the CVF production package executor (ASCP-P1-P3) |
| Adapter contract | `docs/reference/agent_system_skills/CVF_ASSF_PRODUCTION_PACKAGE_RUNTIME_STANDARD.md` |
| Adapter evidence | `docs/reviews/CVF_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_COMPLETION_2026-06-30.md` |
| External mutation boundary | external CLI/MCP wrapper may return receipt-backed package execution envelopes only; no external mutation, daemon behavior, public API, provider routing, public-sync, commit, or merge authority is permitted |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | AGSK-R3 worker with reviewer packet-shape repair |
| Provider or surface | Local workspace |
| Session or invocation | AGSK-R3 package proposal execution, 2026-06-29 |
| Working directory | Repository root |
| Command or tool surface | PowerShell, repo-local Python governance checkers, apply_patch |
| Target paths | `docs/reference/agent_system_skills/packages/cvf-engineering-test-driven-development/` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` |
| Before status evidence | package root did not exist before AGSK-R3 worker execution |
| After status evidence | package root exists in PROPOSED state pending reviewer acceptance |
| Diff evidence | `git diff --name-status` over AGSK-R3 range |
| Approval boundary | WORKER_MUST_NOT_COMMIT; reviewer/closer owns acceptance and commit |
| Claim boundary | Historical AGSK-R3 package-root evidence only; no runtime activation claim before AGSK-R7 |
| Agent type | worker plus reviewer packet-shape repair |
| Invocation ID | `agsk-r3-package-cvf-engineering-test-driven-development-2026-06-29` |
| Expected manifest | `SKILL.md`; `skill.source.json`; `README.md` |
| Actual changed set | `SKILL.md`; `skill.source.json`; `README.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

**Historical record (AGSK-R7, 2026-06-30).** The sub-sections below record
the epistemic reasoning at the AGSK-R7 promotion step, when this package was
APPROVED but not yet ACTIVE. ASCP-P1-P3 (2026-06-30) subsequently promoted
this package to ACTIVE with a receipt-backed production executor and CLI/MCP
adapter (see Claim Boundary); this historical block is preserved for
provenance and is not a current-state claim.

### Expected Result / Prediction

An APPROVED ASSF package root should preserve the upstream skill's useful
workflow discipline while keeping CVF authority, lifecycle, and runtime
boundaries explicit.

### Evidence Comparison

The package cites the pinned upstream source mirror, AGSK-R2 source-mirror
backfill review, AGSK-R3 package-root worker return, AGSK-R6 pilot pattern, and
AGSK-R7 batch promotion review. At the AGSK-R7 step, the package was APPROVED
for explicit internal package-loader body reads only and did not yet claim
ACTIVE resolver behavior, provider behavior, public export, or external
adapter support.

### Contradiction Or Gap Disposition

AGSK-R7 resolved the prior reviewer-acceptance, UAT, certification, and
internal-disposition gap for this batch package. At that step, ACTIVE
resolver behavior, CLI/MCP adapter support, provider proof, public export,
and production readiness remained blockers for later promotion; ASCP-P1-P3
subsequently established ACTIVE source admission, the bounded production
executor, CLI/MCP wrapper, and receipt path (see Claim Boundary and External
Disposition). Automatic package selection was not demonstrated; public export and full
production readiness beyond the bounded ASCP-P1-P3 scope remain separate,
still-unopened blockers.

### Claim Update

At the AGSK-R7 step, the package claim was narrowed to CVF-owned APPROVED
package-loader body-read evidence only, not ACTIVE activation evidence.
ASCP-P1-P3 subsequently updated this claim to ACTIVE receipt-backed
production package execution; see Claim Boundary for the current claim.
## Claim Boundary

This package root is an ACTIVE CVF adaptation sourced from the upstream `test-driven-development` skill at pinned commit `aba7c4e9695c363e65cb59effe926c7f1d1abe3d`. It may be opened only through CVF receipt-backed production package adapters under active governed work-order authority. It does not run test suites automatically, wire CI integrations, trigger merges, mutate provider routing, publish public artifacts, or claim automatic invocation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this package root cites private source mirror and private provenance registry surfaces.
