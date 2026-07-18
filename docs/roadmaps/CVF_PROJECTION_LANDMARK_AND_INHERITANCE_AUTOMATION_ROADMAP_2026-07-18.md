# CVF Projection Landmark And Inheritance Automation Roadmap

Memory class: FULL_RECORD

Status: T0_CLOSED_PASS_BOUNDED_T1_PACKET_AUTHORING_NEXT

Date: 2026-07-18

## Authorization / Decision

Operator authorized retention of the 2026-07-18 projection milestone and a
tool analogous to workspace update automation. Material base: `221698716`.

## Purpose

Make future CVF upgrades discoverably project into private provenance, the
public-sync clone, and cvf-web without repeating a large manual gap audit.

## Scope / Target / Owner Boundary

T0 freezes source seams and a terminal baseline. T1 builds a read-only-first
mapper plus tests and receipts. T2 proves bounded apply planning and closes the
roadmap. Automatic commit, push, provider/live calls, and unattended semantic
rewrites are forbidden.

## Non-Goals

No automatic semantic rewriting, provider call, public commit/push, production
deployment, cvf-web feature implementation, or workspace distribution change.

## Design Control Gate

- default mode: read-only dry-run;
- wrong remote, missing root, or dirty target fails closed;
- output separates mechanical copy candidates from semantic-review items;
- apply requires a later explicit flag and never pushes;
- every run emits a secret-free receipt.

## Tranche Plan

| Tranche | Deliverable | Exit |
|---|---|---|
| T0 | landmark and source-seam ledger | every seed row terminal; T1 contract source-verified |
| T1 | mapper, manifest/schema, focused tests, CLI help | deterministic dry-run and fail-closed negatives PASS |
| T2 | disposable three-root proof, operator guide, closure audit | no push; exact plan/receipt reconciliation PASS |

## Work Plan

1. Inventory existing public-sync allowlists/mappings and workspace updater patterns.
2. Inventory cvf-web registry, package dependency, and operator projection seams.
3. Define mapping units, evidence fields, semantic-review boundary, and receipt schema.
4. Build and test the dry-run mapper only after T0 reviewer acceptance.

## Acceptance Criteria

- AC-01: landmark names closure commits for CVF projection and cvf-web inheritance.
- AC-02: T0 maps provenance, public-sync, and cvf-web seams from direct source.
- AC-03: mapper never equates file presence with semantic inheritance.
- AC-04: dirty/wrong-remote/missing-root states fail closed.
- AC-05: default execution performs no mutation, commit, or push.
- AC-06: receipts are deterministic and secret-free.

## Verification / Evidence

Use direct source reads, exact path manifests, remote/status evidence, focused
tests, worker-fast/reviewer-fast, file-size, and phase-appropriate autorun gates.

## Dependency And Sequence Control

T1 remains held until T0 completion review is committed. T2 remains held until
T1 closure. Public export is a separate batch after this roadmap closes.

## Reverse Architecture Projection Matrix

| Capability | Catalog/GAP owner | Disposition | Target source | Claim class | Evidence |
|---|---|---|---|---|---|
| projection automation | existing public-sync and workspace tooling | UPDATE_EXISTING | `scripts/` plus governed reference manifest | planned | T0 ledger then T1 proof |

## Dual Agent Surface Matrix

| Surface | Interface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local CLI/script | read-only default; explicit apply later | receipt and tests | repository filesystem | ACCEPT |
| EXTERNAL_AGENT_CLI_MCP | documented CLI invocation only | no MCP runtime or provider authority | CLI help/receipt | same local script | DEFER_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`projection automation baseline audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "projection automation baseline audit" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; Agent Handoff Contract Control Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and evidence for roadmap/T0 dispatch shape |
| claimBoundary | documentation planning only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: roadmap and T0 evidence remain private; no public-sync mutation occurs.

## Claim Boundary

This roadmap authorizes bounded audit and later local tooling only. It does not
authorize provider/live behavior, public push, production, or autonomous edits.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | T0 baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | T0 work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | T0 completion review | `Status: REVIEWER_ACCEPTED_BOUNDED` | PASS |
| Worker return | T0 worker return | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| Roadmap state | this roadmap | `Status: T0_CLOSED_PASS_BOUNDED_T1_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | existing GC-051 registry | aggregate drift checked | PASS |
| Registry Markdown | existing registry front door | existing coverage | PASS |
| External evidence digest | local source only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected surfaces | separate sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| T0 receipt state | independently accepted documentation evidence | `ACCEPTED_BY_REVIEWER` | PASS |
| T0 mutation boundary | zero mapper/apply/public mutation | worker and reviewer claim boundaries match | PASS |
| next tranche release | T1 packet authoring only | `T0_CLOSED_PASS_BOUNDED_T1_PACKET_AUTHORING_NEXT` | PASS |
