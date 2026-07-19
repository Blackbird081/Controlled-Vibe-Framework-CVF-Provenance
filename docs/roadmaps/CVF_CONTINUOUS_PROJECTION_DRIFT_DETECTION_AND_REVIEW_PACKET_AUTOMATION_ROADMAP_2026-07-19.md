# CVF Continuous Projection Drift Detection And Review-Packet Automation Roadmap

Memory class: governed-roadmap

Status: T0_DISPATCH_READY

Date: 2026-07-19

## Purpose

Turn the accepted read-only projection mapper into a repeatable drift detector
and review-packet preparation workflow without allowing unattended semantic
edits, commits, pushes, deployments, or provider calls.

This recovered roadmap also records the presentation lesson from the 2026-07-18
public projection: source-truth propagation and audience-ready presentation are
separate acceptance dimensions. A technically current projection may still be
unfit for a public reader or an external agent.

## Authority And Recovery Evidence

- Projection automation foundation closure: commit `5df0c6f77`.
- SOT3/CVF projection roadmap closure: commit `9f7c92663`.
- Latest provenance build repairs: commits `ee208c753` and `0cae3289f`.
- Matching public repair commits: `620016275` and `0d3fec3ca`.
- UX audit material and closure: `9f9d7f6d7` and `93c2663a6`.
- Recovery reason: the earlier untracked draft disappeared during delegated UX
  audit repair rounds; this file restores the governed roadmap as a separate
  reviewer-owned artifact rather than attributing the loss to a committed diff.

## Authorization / Decision

Roadmap restoration and parked planning are authorized by the operator's
instruction to preserve the projection-automation lesson while prioritizing
CVF Web remediation. Execution remains unreleased.

## Scope / Target / Owner Boundary

Target: deterministic, reviewer-controlled drift detection between provenance,
public-sync, and cvf-web projection surfaces.

Owner boundary: the recorded UX reopen condition passed at material commit
`d757fe5ac`; T0 documentation audit is dispatch-ready. Reviewers own semantic
decisions; automation owns only read-only comparison and draft evidence
preparation.

## Scope

The roadmap may prepare deterministic drift receipts and draft review packets.
It must remain read-only against semantic source surfaces.

Forbidden automation:

- editing README, architecture, catalog, Web, or public content automatically;
- committing, pushing, deploying, or applying to a real root unattended;
- copying secrets or provider-local memory;
- using provider calls to decide semantic truth;
- treating a passing hash comparison as proof of audience clarity.

## Non-Goals

- no automatic content rewriting or architecture decisions;
- no replacement of existing projection owners;
- no public README redesign inside this parked roadmap;
- no provider-based semantic adjudication;
- no commit, push, deployment, or production mutation authority.

## Design Control Gate

Any future Web or README-facing projection must apply `DESIGN.md`, preserve
progressive disclosure, distinguish end-user and external-agent depth, and use
localhost browser proof before public projection acceptance.

## Audience Projection Contract

| Audience | Front-door need | Permitted depth | Acceptance evidence |
|---|---|---|---|
| End user | value, outcomes, difference, first action | progressive disclosure | short visual scan plus clear next action |
| Developer | architecture, extension seams, setup | linked technical depth | source-backed paths and runnable commands |
| External agent | logic, catalog, evidence, authority boundary | full machine-readable context | source verification and evidence locators |
| Reviewer/operator | drift, provenance, decision and rollback | full governed detail | receipts, hashes, changed range, disposition |

One README or one projection payload must not flatten these audiences into the
same information density. Public front doors stay concise; deeper developer and
agent routes carry the catalog, logic, and evidence.

## Work Plan

### T0 - Drift Contract And Three-Root Baseline

Reconcile provenance, public-sync, and cvf-web roots. Define semantic owner,
projection target, evidence class, audience, and drift disposition for every
mapped surface. Pin the repair commits above and record secret-free hashes.

### T1 - Read-Only Drift Receipt

Extend the accepted mapper with deterministic receipts for changed owner,
missing target, stale target, and audience-presentation risk. Provide manual,
CI, and scheduled invocation seams. No apply mode is allowed.

### T2 - Governed Review-Packet Drafting

Generate a draft packet that lists source facts, affected projections,
recommended reviewer actions, public/provenance boundary, and evidence. The
packet must remain review-required and uncommitted.

### T3 - Audience And Presentation Gate

Require public README and Web projections to pass progressive-disclosure,
language, navigation, and external-agent-context checks in addition to source
freshness. Reuse accepted UX-remediation evidence rather than inventing a new
visual doctrine.

### T4 - Bounded Pilot And Closure

Run on a disposable three-root fixture, then one reviewer-authorized real-root
read-only scan. Measure false positives, missed drift, reviewer effort, and
packet usefulness. Close only if no automatic semantic mutation occurred.

## Acceptance Criteria

- [x] Roadmap authority and recovery reason are explicit.
- [x] Projection execution remains parked behind a checkable UX condition.
- [x] End-user, developer, external-agent, and reviewer needs are separated.
- [x] Automatic semantic edits, commits, pushes, deploys, and provider calls
  are forbidden.
- [x] Each future tranche has a bounded output and independent review point.

## Verification / Evidence

- `Test-Path` confirmed this roadmap was absent before recovery.
- Current session state names restoration before UX roadmap authoring.
- Closure commits and public repair anchors are listed above.
- Governed structural, file-size, and pre-commit gates must pass before the
  recovered roadmap is treated as durable.

## Release And Reopen Condition

The CVF Web UX remediation roadmap reached reviewer-accepted bounded closure at
`d757fe5ac` with localhost current-source browser evidence for task-first
navigation, audience separation, language clarity, and responsive behavior.
The release condition is satisfied. T0 now has a fresh GC-018 baseline and
source-verified no-commit work order; T1-T4 remain dependency-held.

## Learning Carried Forward

1. Source freshness does not imply good presentation.
2. Public README is an attention-limited product surface, not a provenance dump.
3. External agents need a deeper logic/catalog/evidence route than end users.
4. Hosted and current-source evidence must be reported separately.
5. Browser proof must use localhost current source before a public projection is
   accepted as visually inherited.
6. Untracked roadmap drafts are not durable continuity; governed planning must
   be committed before unrelated delegated execution begins.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_roadmap_closure_freshness.py` |
| literalTokensReviewed | roadmap status; parked release condition; public disposition; no closed-equivalent claim |
| gateRunPurpose | confirm recovered roadmap structure and parked lifecycle before commit |
| claimBoundary | checker compliance confirms packet shape only; cited closures and source artifacts support roadmap authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside repository, critique packet, or provider output is absorbed |
| Matching local-view guard | N/A with reason: no outside finding is promoted; current CVF source and governed closures remain authority |
| Owner surface | this roadmap records audience requirements without promoting external material to authority |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | the external-agent audience is a product consumer class, not an external authority source |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: roadmap execution is parked behind CVF Web UX remediation. A later
reviewed public projection may export only public-safe artifacts through the
sibling public-sync repository.

## Claim Boundary

This roadmap restores and governs future planning only. It does not authorize
implementation, real-root apply, semantic edits, commit, push, deployment,
provider/live use, or unattended mutation.
