# CVF Continuous Projection Drift Detection And Review-Packet Automation Roadmap

Memory class: governed-roadmap

Status: T2_CLOSED_PASS_WITH_REVIEWER_REPAIRS_PROVIDER_MODEL_ROADMAP_NEXT

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

Roadmap restoration and bounded T0-T2 execution were authorized by the
operator. T2 is now closed with reviewer repairs. Continuous Projection T3-T4
remain unreleased; the operator-selected next planning lane is a separate,
provider-neutral roadmap for operator-approved provider/model assignment and
invocation receipts.

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

Disposition: `CLOSED_PASS_BOUNDED`. Independent review corrected tracked
public content versus ignored local residue, reduced every terminal row to the
seven-token contract vocabulary, confirmed all three mapped-file pairs by
SHA-256, and identified six target-only allowed root files whose semantic
source remains blocked. T1 packet authoring is released; implementation is not.

### T1 - Read-Only Drift Receipt

Extend the accepted mapper with deterministic receipts for changed owner,
missing target, stale target, and audience-presentation risk. Provide manual,
CI, and scheduled invocation seams. No apply mode is allowed.

Disposition: `CLOSED_PASS_WITH_REVIEWER_REPAIRS`. The accepted implementation
at `a394d635c` emits the frozen 16-surface schema, consumes mapper candidate
signals for `MISSING_TARGET`, `STALE_TARGET`, and `CURRENT`, preserves the six
target-only `SOURCE_AUTHORITY_BLOCKED` decision, separates tracked denied files
from git-confirmed ignored residue, and fails closed on bounded mapper timeout.
The reviewer repaired schema fidelity, mapped-handoff exclusion, git-ignore
classification, and live-signal consumption before the 53/53 fixture suite
passed. T2 packet authoring is released; T2 implementation and T3-T4 remain
parked.

### T2 - Governed Review-Packet Drafting

Generate a draft packet that lists source facts, affected projections,
recommended reviewer actions, public/provenance boundary, and evidence. The
packet must remain review-required and uncommitted.

Disposition: `CLOSED_PASS_WITH_REVIEWER_REPAIRS`. The accepted implementation
at `f350b925a` emits a deterministic stdout-only draft, validates frozen enums
ordinally and booleans by JSON type, detects duplicate affected-surface
identity independently, and passes 91/91 disposable-fixture assertions. The
reviewer consolidated and repaired three fail-closed gaps before closure. No
generated review draft, real-root scan, or public mutation occurred.

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
The release condition is satisfied. T0 is closed bounded through its fresh
GC-018, source-verified no-commit work order, corrected ledger, worker return,
and independent completion review. T1 is closed with reviewer repairs through
implementation commit `a394d635c` and 53/53 disposable-fixture proof. T2 is
closed with reviewer repairs through implementation commit `f350b925a`, 91/91
disposable-fixture proof, and independent completion review. The next allowed
move is to author only the separate provider-neutral operator-approved
provider/model assignment and invocation-receipt roadmap. Continuous
Projection T3-T4 remain parked.

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

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | T2 work order | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Completion or reviewer artifact | T2 completion review | `Status: REVIEWER_ACCEPTED_WITH_REPAIRS` | PASS |
| Roadmap state | this roadmap | `Status: T2_CLOSED_PASS_WITH_REVIEWER_REPAIRS_PROVIDER_MODEL_ROADMAP_NEXT` | PASS |
| Implementation evidence | T2 scripts plus worker return | private commit `f350b925a`; 91/91 disposable-fixture proof | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate drift check remains clean; no entry change required | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | existing human registry remains unchanged; T1 adds no corpus record | PASS |
| External evidence digest | N/A with reason: repository-local roots only | no imported bundle | N/A with reason |
| System loop interlock | N/A with reason: no interlock owner changed | no mutation | N/A with reason |
| Session continuity | protected continuity surfaces | separate post-material sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| T0-REAL-ROOT-RECEIPT | T0 ledger evidence-gap section | N/A with reason: no receipt JSON was emitted | no real-root freshness receipt accepted in T0 | no receipt produced | PASS |
| T2-DRAFT-STATUS | disposable-fixture review draft | `draftStatus` | `REVIEW_REQUIRED_UNCOMMITTED` | `REVIEW_REQUIRED_UNCOMMITTED` | PASS |
| T2-NO-DECISION | disposable-fixture review draft | `authorizesDecision` | `false` boolean | `false` boolean | PASS |
| T2-ENUM-CASE | malformed fixture diagnostic | `errors[0].code` | `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | PASS |
| T2-BOOLEAN-TYPE | malformed fixture diagnostic | `errors[0].code` | `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | PASS |
| T2-CARDINALITY | duplicate-surface fixture diagnostic | `errors[0].code` | `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | PASS |

## Current Runtime Freshness Verification

T2 closure re-read the receipt-to-draft implementation and focused proof,
then independently reran 91/91 disposable-fixture assertions. The T4-owned
real-root recursive invocation was not run, so this roadmap does not claim
tree-scale freshness or runtime completion. Continuous Projection T3-T4 remain
parked. Disposition: PASS_BOUNDED.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2 closure is private provenance evidence. A later reviewed public
projection may export only public-safe artifacts through the sibling
public-sync repository.

## Claim Boundary

This roadmap closes T2 with reviewer repairs. It releases only authoring of a
separate provider-neutral roadmap for operator-approved provider/model
assignment and invocation receipts. It does not authorize that roadmap's
implementation, Continuous Projection T3-T4, the T4 real-root scan, real-root
apply, semantic edits, push, deployment, provider/live use, public-sync
mutation, or unattended mutation.
