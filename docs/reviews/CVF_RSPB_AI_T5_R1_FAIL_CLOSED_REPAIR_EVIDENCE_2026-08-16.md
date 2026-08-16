# CVF RSPB-AI-T5-R1 Fail-Closed Repair Evidence

Memory class: governed-repair-evidence

Status: COMPLETE_PENDING_INDEPENDENT_REVIEW

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_RSPB_AI_T5_CAPABILITY_CASE_AND_DOMAIN_EVIDENCE_PROJECTION_KERNEL_2026-08-16.md`

Repair base: `2133f5cb9b0583655a785d4e41f5005fe4763212`

## Purpose

Record one consolidated reviewer-owned repair round after independent
adversarial review rejected the original RSPB-AI-T5 worker implementation.
The repair keeps the tranche pure, hermetic, projection-only, and within the
reviewer's permitted source/test/export/evidence paths. It does not accept or
close T5; a distinct independent reviewer must re-review the repaired diff.

## Target / Source

Target: the uncommitted RSPB-AI-T5 projection kernel, tests, barrel export, and
worker return produced from execution base `2133f5cb9`. Governing sources are
the T5 work order and paired GC-018 baseline, plus the current T3 controlled-
acquisition and T4 route/readiness contracts consumed by the kernel.

## Scope / Methodology

The reviewer read the complete worker implementation and focused tests,
checked its four-path manifest, then added independent adversarial probes for
throwing accessors, unresolved evidence, secret-shaped values, actual
multi-item reordering, route/readiness lookalikes, and collection bounds. The
first independent run passed 18 of 26 tests and failed eight. One consolidated
repair then hardened the existing kernel and expanded the focused suite to 27
tests. No second speculative feature pass was performed.

## Findings / Position

The original `COMPLETE_PENDING_REVIEW` claim was not review-acceptable. Eight
material fail-closed or determinism expectations failed independently:

1. accessed getters could throw despite the documented never-throw contract;
2. malformed acquisition objects could throw through an accessor;
3. unresolved finding references left the overall disposition `READY`;
4. secret-rejection issues also left the overall disposition `READY`;
5. a standalone `sk-*` provider-key-shaped value was admitted;
6. genuinely reordered multi-item inputs produced different digests;
7. route/readiness lookalikes lacking canonical authority invariants were
   accepted as sufficient inputs; and
8. an oversized top-level collection was accepted without a bound.

The worker's original reordering test did not exercise reordering: it reversed
a one-element array and compared projections built from equivalent untouched
singletons. The repair replaces this with a two-item permutation test.

## Risk / Corrective Action

One bounded repair round made the following corrections:

- reject Proxies, accessor-bearing records/arrays, sparse arrays, and arrays
  exceeding 256 entries before property traversal;
- require canonical route/readiness schema versions, identity bindings,
  evidence-only/no-execution authority literals, bounded collections, and
  valid timestamps;
- require optional controlled-acquisition evidence to retain its canonical
  result shape and an explicit bounded source reference;
- treat every non-staleness validation issue as `currentDisposition:
  'INVALID'` while preserving the distinct `STALE` result;
- reject standalone provider-key-shaped values without echoing them;
- sort evidence, findings, paths, finding references, and issues by a stable
  code-point comparator before digesting; and
- replace the false-positive reorder test and retain the new adversarial
  regression coverage.

The repair adds no I/O, adapter, executor, filesystem export, ambient clock,
credential access, network call, provider call, MCP/CLI activation, public
sync, deployment, or authority promotion.

## Decision / Disposition

`COMPLETE_PENDING_INDEPENDENT_REVIEW`. The original review verdict was
`REVIEW_REJECTED_REPAIR_REQUIRED`; the disclosed defects are repaired and the
hermetic evidence is green. Acceptance, material commit, closure, continuity
promotion, and public export remain unauthorized until a distinct reviewer
reproduces and accepts the repaired state.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | governed repair status; required structural headings; agent trace fields; learning disposition; one allowed Public Export Disposition token; claim boundary |
| gateRunPurpose | validate repair-evidence packet shape after semantic repair; checker results do not substitute for distinct independent re-review |
| claimBoundary | read-ahead and gates cover local artifact structure and hermetic checks only |

## Verification Evidence

| Verification | Result |
|---|---|
| initial independent adversarial focused run | FAIL as expected: 18 passed, 8 failed, 26 total; failures correspond exactly to the eight findings above |
| repaired focused T5 suite | PASS: 27/27 |
| repaired six-file kernel/export suite | PASS: 104/104 across T3, T4, T5, barrel, package-boundary, and boundary-signal tests |
| TypeScript `npm run check` | PASS: no type errors |
| full Guard Contract package suite with known live/provider opt-ins cleared | PASS: 624 passed, 5 skipped, 629 total across 40 files; skipped tests are provider-live tests |
| `git diff --check` | PASS |
| provider/live/network calls | zero |

The final counts supersede the worker-time counts only for the repaired state;
the original worker return is intentionally unchanged as historical evidence.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| happy-path-looking tests did not prove fail-closed behavior or real permutation invariance | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | retain independent adversarial reviewer probes and require a distinct post-repair re-review before commit |

runtimeProviderCostLearningLane: N/A_WITH_REASON - all verification was local
and hermetic; no provider or live execution occurred.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer acting as bounded repair steward |
| Provider or surface | local private provenance repository |
| Session or invocation | RSPB-AI-T5-R1 review/repair, 2026-08-16 |
| Working directory | repository root and `EXTENSIONS/CVF_GUARD_CONTRACT` |
| Command or tool surface | governed reads, patch edits, Vitest, TypeScript check, diff and governance gates |
| Target paths | T5 contract, T5 test, barrel export, original worker return as read-only evidence, and this reviewer-owned repair evidence |
| Allowed scope source | T5 work order reviewer permissions and paired baseline |
| Before status evidence | four uncommitted worker paths at execution base `2133f5cb9`; no worker commit |
| After status evidence | repaired T5 source/test/export plus unchanged worker return and this new repair-evidence file |
| Diff evidence | local five-path changed set relative to execution base; no deletion or rename |
| Approval boundary | one consolidated reviewer repair round only; no acceptance, closure, stage, commit, or push |
| Claim boundary | pure local projection behavior and hermetic verification only |
| Agent type | reviewer/repair steward |
| Invocation ID | `rspb-ai-t5-r1-fail-closed-repair-20260816` |
| Expected manifest | four worker paths plus one reviewer-owned repair-evidence path |
| Actual changed set | four worker paths plus one reviewer-owned repair-evidence path |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the worker's green suite would likely conceal
boundary failures because its adversarial coverage was too shallow in several
claim-critical areas.

Evidence Comparison: eight of 26 independent probes failed before repair,
including actual permutation invariance, getter safety, canonical authority
binding, secret rejection, and boundedness. After one consolidated repair,
27/27 focused, 104/104 composed, 624/624 non-skipped package tests, and the
TypeScript check passed.

Contradiction Or Gap Disposition: the original completeness claim is retained
only as worker-time evidence and is superseded for the repaired state by this
packet. No remaining known semantic defect was observed in the bounded scope,
but epistemic independence requires a different reviewer to verify that
conclusion.

Claim Update: repaired and locally verified; not independently accepted and
not commit-ready until the distinct re-review returns an accepting verdict.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private, uncommitted repair evidence pending distinct
independent re-review. No public sync or push is authorized.

## Claim Boundary

This evidence authorizes no execution, mutation, router, adapter, acquisition,
credential access, filesystem export, provider/live call, network access,
MCP/CLI activation, public sync, deployment, or production-readiness claim.
It does not accept or close RSPB-AI-T5 and does not authorize a material
commit. The next allowed move is a distinct independent review of the repaired
five-path worktree against the work order, baseline, original worker return,
and this repair evidence.
