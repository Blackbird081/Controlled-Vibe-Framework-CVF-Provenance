# CVF ASSF Package: Engineering Code Review And Quality

Memory class: FULL_RECORD

Status: ACTIVE

docType: assf_package

Batch ID: AGSK-R3; AGSK-R6

skillId: cvf-engineering-code-review-quality

## Purpose

Guide multi-axis code review across correctness, readability, architecture, security, and performance, with structured findings categorized by severity. Use when a governed CVF task requires reviewing code before merge, evaluating agent-produced code, or assessing quality against project conventions after explicit package-loader selection. Do not use when: autonomous runtime activation, automated merge execution, provider/live proof, or authority beyond the active governed work order is required.

## Scope / Applies-To

| Field | Value |
|---|---|
| Package root | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/` |
| Owner surface | ASSF proposal evidence under AGSK-R3, bounded AGSK-R6 promotion evidence, and current ASCP-P1-P3 ACTIVE production package contract |
| Applies to | ACTIVE receipt-backed production package execution through CVF adapters after explicit request |
| Does not apply to | automatic invocation, CLI/MCP adapter beyond the implemented receipt-backed wrapper, provider/live proof, public-sync, merge execution, commit authority, or production readiness |

## Invocation Boundary

| Field | Value |
|---|---|
| Allowed task classes | code-review, quality-assessment, refactor-review, security-review, architecture-review |
| Allowed roles | dispatcher, worker, reviewer |
| Allowed phases | INTAKE, DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE |
| Allowed surfaces | docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/, registry entries, review artifacts |
| Risk ceiling | R1 |
| Authority ceiling | bounded advisory review guidance; loading never authorizes commit, merge, provider, public, production, or external actions |

## Inputs And Outputs

| Field | Value |
|---|---|
| Inputs | operator request or governed task context; source mirror file `.private_reference/source_mirrors/addyosmani__agent-skills/skills/code-review-and-quality/SKILL.md`; active CVF authority and allowed-scope boundaries |
| Outputs | bounded code-review guidance; five-axis review framework notes; severity classification discipline; recommended CVF owner-surface routing |
| Acceptance evidence | AGSK-R3 proposal, AGSK-R5 eligibility audit, AGSK-R6 promotion and loader smoke; ASCP-P1-P3 six-package ACTIVE source admission, focused executor/CLI-MCP tests, and one live exemplar for a different skill ID |

## Review Procedure

This bounded procedure fulfills the five-axis outputs declared above. It is
advisory guidance for a human or agent reviewer already authorized by an
active governed work order; loading this body never grants edit, merge,
commit, provider, public, or production authority (see CR6).

1. Establish intent: read the exact base/head range, the allowed scope, and
   the project's existing conventions before opening the diff.
2. Inspect tests first, then enough surrounding implementation to understand
   actual behavior; tests reveal intent and coverage gaps that the diff alone
   does not show.
3. Review across the five axes -- correctness, readability/simplicity,
   architecture, security, and performance -- leading with correctness,
   security, lifecycle, and any broken required behavior before style or
   preference feedback. For the architecture axis, explicitly determine
   whether a refactor reduces complexity or merely relocates it: count the
   concepts a reader must hold before and after the change. When the count is
   unchanged or a structural risk is present (added coupling, a moved but not
   removed branch, a new indirection layer), name that risk and propose at
   least one concrete structural remedy rather than a general "cleaner"
   verdict -- for example, separating orchestration from business logic,
   moving feature-specific logic to its canonical owning module, reusing an
   existing canonical helper instead of a near-duplicate, collapsing
   redundant branches into one clearer flow, introducing an explicit type
   boundary so downstream branching disappears, or deleting a pass-through
   wrapper that adds indirection without clarifying the API (see CR5).
4. For an authorization or enforcement change, trace every denial branch to
   the operation it protects, and exercise direct and alternate callers that
   might bypass a schema, prompt, facade, wrapper, or listener-ordering layer.
   A passing facade-level test is not sufficient when another caller can still
   reach the protected operation directly (see CR1/CR2).
5. Classify every finding as Critical, Required, Optional/Consider, Nit, or
   FYI, and support each blocking finding with an exact path/symbol and its
   concrete failure consequence rather than a general impression.
6. Verify the verification story itself (what was run, what passed, what a
   screenshot or manual check covered) and return one bounded verdict.
   Package loading and this review grant no edit, merge, commit, provider,
   public, or production authority beyond the active governed work order.

### Enforcement-Path Tracing (Supplemental)

For changes that add or modify authorization, permission, or denial logic,
apply this supplemental check in addition to Step 4 above: do not accept a
single enforcement point as sufficient coverage without confirming every
caller actually converges on it. Concretely:

- Follow each denial path forward to the exact operation it is meant to
  prevent, not just to the point where a check returns a boolean.
- Enumerate alternate entry points (a direct service call, an internal
  helper, a second route, a differently ordered listener) that could reach
  the same protected operation, and confirm each one is covered by the same
  enforcement or an equivalent one.
- Treat a route- or facade-level test that only exercises the primary caller
  as incomplete evidence when a bypass-capable alternate caller exists (CR1);
  when every caller is confirmed to converge on one enforcement point, record
  the traced path as evidence rather than inventing a blocker (CR2).

## Risk And Authority

| Field | Value |
|---|---|
| Risk class | R1 |
| Authority ceiling | bounded advisory review guidance only |
| Side effects | none from metadata reading; merge decisions, commit actions, or production changes require separate authorization |
| Rollback | revert only a later authorized change under its owning work order and review; this guidance does not authorize demoting the existing ACTIVE package to AGSK-R3 PROPOSED |
| Safe stop | stop if ACTIVE source checks, required receipts, or governed work-order authority are missing; automated merge, production changes, or broader external action requires separate authorization |
| Policy bindings | AGSK-R6 and ASCP-P1-P3 establish the bounded ACTIVE production package path; the active governed work order, activation policy, required receipts, and production runtime standard remain binding |

## Progressive Disclosure

| Stage | Accessible fields |
|---|---|
| Metadata-only (CANDIDATE/PROPOSED) | skillId, name, status, purpose, triggerPatterns, riskCeiling, sourceArtifacts |
| Post-reviewer-acceptance (historical APPROVED, AGSK-R6) | full five-axis review guidance through explicit runtime package-loader request; reviewer decision gate already satisfied |
| Runtime (ACTIVE, current) | full instructions readable through the receipt-backed production package loader under a governed work order; ASCP-P1-P3 established six-package ACTIVE admission and focused adapter tests, with one live exemplar for `cvf-engineering-spec-driven-development`, not a code-review-specific live run; no automatic invocation |

## Evidence And UAT

| Field | Value |
|---|---|
| Required evidence | AGSK-R3 worker return with source reads and 24-candidate coverage table; AGSK-R5 runtime eligibility audit; AGSK-R6 package-loader body-read smoke; anatomy and certified metadata checkers PASS; ASCP-P1-P3 six-package ACTIVE admission and focused production executor/CLI-MCP tests; its live E2E exemplar used `cvf-engineering-spec-driven-development`, not this package |
| UAT binding | PASSED for receipt-backed production package execution through CVF adapters |
| Validation hooks | ASSF anatomy checker; certified metadata admission checker; generated-index drift checker; reviewer-fast gate |
| Review evidence | docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md; docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md; docs/reviews/CVF_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_COMPLETION_2026-06-30.md; docs/reviews/CVF_ASCP_P1_P3_RUNTIME_PACKAGE_SKILLS_PRODUCTIONIZATION_COMPLETION_2026-06-30.md |

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
| Target paths | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` |
| Before status evidence | package root did not exist before AGSK-R3 worker execution |
| After status evidence | package root exists in APPROVED state for explicit internal package-loader body read only |
| Diff evidence | `git diff --name-status` over AGSK-R3 range |
| Approval boundary | WORKER_MUST_NOT_COMMIT; reviewer/closer owns acceptance and commit |
| Claim boundary | APPROVED package-loader body-read evidence only; no ACTIVE runtime activation claim |
| Agent type | worker plus reviewer packet-shape repair |
| Invocation ID | `agsk-r3-package-cvf-engineering-code-review-quality-2026-06-29` |
| Expected manifest | `SKILL.md`; `skill.source.json`; `README.md` |
| Actual changed set | `SKILL.md`; `skill.source.json`; `README.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

**Historical record (AGSK-R6, 2026-06-30).** The sub-sections below record
the epistemic reasoning at the AGSK-R6 promotion step, when this package was
APPROVED but not yet ACTIVE. ASCP-P1-P3 (2026-06-30) subsequently promoted
this package to ACTIVE with a receipt-backed production executor and CLI/MCP
adapter (see Claim Boundary); this historical block is preserved for
provenance and is not a current-state claim.

### Expected Result / Prediction

An APPROVED ASSF package root should preserve the upstream skill's useful
workflow discipline while keeping CVF authority, lifecycle, and runtime
boundaries explicit.

### Evidence Comparison

The package cites the pinned upstream source mirror, the AGSK-R2 source-mirror
backfill review, the AGSK-R3 baseline, the AGSK-R3 worker return, the AGSK-R5
eligibility audit, and the AGSK-R6 promotion review. At the AGSK-R6 step, the
package was APPROVED for explicit internal package-loader body reads only and
did not yet claim ACTIVE resolver behavior, provider behavior, public export,
or external adapter support.

### Contradiction Or Gap Disposition

AGSK-R6 resolved the prior reviewer-acceptance, UAT, certification, and
internal-disposition gap for this pilot package. At that step, ACTIVE
resolver behavior, CLI/MCP adapter support, provider proof, public export,
and production readiness remained blockers for later promotion; ASCP-P1-P3
subsequently established ACTIVE source admission, the bounded production
executor, CLI/MCP wrapper, and receipt path (see Claim Boundary and External
Disposition). Automatic package selection was not demonstrated; public export and full
production readiness beyond the bounded ASCP-P1-P3 scope remain separate,
still-unopened blockers.

### Claim Update

At the AGSK-R6 step, the package claim was narrowed to CVF-owned APPROVED
package-loader body-read evidence only, not ACTIVE activation evidence.
ASCP-P1-P3 subsequently updated this claim to ACTIVE receipt-backed
production package execution; see Claim Boundary for the current claim.

## AGSK-R6 And ASCP-P1-P3 Lifecycle Promotion

AGSK-R6 (2026-06-30) promoted this package to APPROVED, UAT PASSED,
certification CERTIFIED, and internal-agent disposition IMPLEMENTED for
explicit internal runtime-loader body reads only; at that step it did not
make the package ACTIVE. ASCP-P1-P3 (2026-06-30) subsequently promoted this
package to ACTIVE with a receipt-backed production executor and CLI/MCP
adapter (see External Disposition). Neither promotion authorizes merge,
commit, provider routing, public export, or production actions beyond the
receipt-backed production adapter boundary.

## Source Attribution

| Source | Role | Pin | License |
|---|---|---|---|
| `addyosmani/agent-skills` `code-review-and-quality` | Primary source: five-axis review framework and review process | `aba7c4e9695c363e65cb59effe926c7f1d1abe3d` | MIT (full notice below) |
| `deepseek-ai/deepseek-harness` `dsh-code-review` | Supplemental source: enforcement-path/alternate-caller bypass tracing only (Enforcement-Path Tracing section above) | `cd5ef8148158c3a752a658978873241fdf8e2bbc` | MIT (full notice below) |

This package remains an Addy-derived primary adaptation; DeepSeek supplies one
bounded supplemental concept and is not a co-primary or replacement source.
Repository-specific DeepSeek commands, tooling, and policies (for example its
`pnpm --silent run change-scope` invocation and its own repository AGENTS.md
conventions) are excluded; only the source-independent enforcement-path
concept is imported (CR7).

### Addy Agent-Skills MIT Notice

Verbatim from `.private_reference/source_mirrors/addyosmani__agent-skills/LICENSE`:

```
MIT License

Copyright (c) 2025 Addy Osmani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### DeepSeek Harness MIT Notice

Verbatim from `.private_reference/source_mirrors/deepseek-ai__deepseek-harness/LICENSE`:

```
MIT License

Copyright (c) 2026 DeepSeek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Claim Boundary

This package root is an ACTIVE CVF adaptation sourced primarily from the upstream `code-review-and-quality` skill at pinned commit `aba7c4e9695c363e65cb59effe926c7f1d1abe3d`, with one bounded supplemental enforcement-path concept adapted from `deepseek-ai/deepseek-harness` `dsh-code-review` at pinned commit `cd5ef8148158c3a752a658978873241fdf8e2bbc` (see Source Attribution). It may be opened only through CVF receipt-backed production package adapters under active governed work-order authority. It does not execute code reviews autonomously, trigger merges, mutate provider routing, publish public artifacts, or claim automatic invocation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this package root cites private source mirror and private provenance registry surfaces.
