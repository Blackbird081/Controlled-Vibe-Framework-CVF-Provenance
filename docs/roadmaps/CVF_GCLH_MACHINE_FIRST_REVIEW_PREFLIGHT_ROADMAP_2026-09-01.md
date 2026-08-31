# CVF GCLH Machine-First Review Preflight Roadmap

Memory class: governed-roadmap

Status: DRAFT_FOR_CLAUDE_CRITIQUE_IMPLEMENTATION_HOLD

docType: roadmap

Date: 2026-09-01

Roadmap ID: GCLH-MFRP

Planning base head: `90c2952b642e962c274e07f1f1f5b7cda03d4451`

## Authorization / Decision

The operator authorized a detailed roadmap and one Claude critique before any
implementation. This packet therefore authorizes planning and external
critique only.

Current decision: `HOLD_IMPLEMENTATION_PENDING_CLAUDE_CRITIQUE_AND_CVF_RECONCILIATION`.

No standard, template, checker, schema, hook, runtime, downstream workspace,
provider, public, deployment, or production mutation is authorized by this
roadmap.

## Purpose

Create a durable machine-first review control for every returned result in:

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

The control should reduce reviewer latency, token/quota consumption, repeated
work, and AI-on-AI self-attestation while increasing deterministic evidence
integrity. Machine helpers verify facts that can be determined mechanically;
the reviewer retains semantic evaluation and disposition authority.

## Scope

In scope: a cross-phase envelope/receipt design, deterministic verifier trust,
exception-focused reviewer readout, evidence reuse, replay/canary activation,
rollback, cost telemetry and one external critique/reconciliation cycle.

## Non-Goals

- No AI semantic-scoring verifier or autonomous closure decision.
- No replacement of reviewer judgment, Truth Foundation, SOT3, SCEC, Review
  Cost, AAF, work-order authority or commit stewardship.
- No global SOT3 runtime activation, daemon, watcher, queue or arbitrary
  command executor.
- No implementation, downstream adoption, provider/live, public-sync,
  deployment or production work in P0.

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: P0 changes governed planning and
external-review context only. No runtime source, helper, checker, schema, hook,
provider configuration or product behavior was inspected as proof of current
execution, modified or executed. The current implementation state therefore
remains unverified by this roadmap, and no runtime behavior claim is made.

## Design Control Gate

The design may proceed from P0 only when external critique plus CVF
reconciliation confirms non-duplicative owner placement, fail-closed verifier
trust, bounded machine authority, measurable cost value, hostile replay and
rollback. Otherwise revise or stop before P1.

## Governing Principles

1. `trust != agent count + role labels + provider identity + orchestration shape`.
2. A governed phase return is the reviewer-facing control root, but it is not
   automatically true; its SOT references and evidence must resolve.
3. Machine code verifies identity, shape, bindings, deterministic results and
   declared coverage; it does not judge semantic truth or business value.
4. Reviewer work is evaluation of the return, not repetition of the producing
   role's work.
5. Broad reruns are default-forbidden and require a named evidence gap or
   contradiction, a bounded claim, expected information gain and cost reason.
6. Unknown, stale, conflicted, unmapped or uninspectable states fail closed or
   escalate; they never silently reduce verification.
7. A worker must not gain trust by modifying the verifier used to accept the
   same worker return.

## Current Owner Map And Non-Duplication

| Concern | Current owner | MFRP relationship |
|---|---|---|
| source authority, provenance, obligations, verification and claim movement | `docs/reference/truth_foundation/` | reuse; do not create another truth doctrine |
| Refinery/Kernel/Flow authority topology | `docs/reference/sot_three_layer/` | adapt bounded semantics; do not claim global SOT3 runtime activation |
| dispatch and worker-return shape | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | enrich phase-return requirements |
| convergence and stable problem identity | `docs/reference/semantic_convergence_control/` | consume outcomes; do not create a parallel stop owner |
| review economics and single-pass review | `docs/reference/review_cost_control/` | extend with machine/preflight telemetry only if value-proven |
| read-only helper/readout/scaffold | `governance/compat/run_agent_automation_assist.py` | extend or compose; do not create a competing orchestration helper |
| commit/range classification | `governance/compat/run_agent_commit_steward_preflight.py` | reuse exact path plan and split-range logic |
| lifecycle phase gates | `governance/compat/run_agent_autorun_workflow_gate.py` | integrate only after shadow/replay evidence |
| downstream projection freshness | GCLH T1 plus GLP owner | remain parked until Core closure |

Owner-placement question for critique: a cross-phase `Phase Return Envelope`
needs one narrow interface-contract owner. The current recommendation is a new
reference family only if template-only enrichment would scatter or duplicate
the contract. Such a family would own envelope shape and machine receipt
semantics, not truth authority, phase authority, reviewer judgment or runtime.

## Target Control Flow

```text
producing role(s)
    -> governed Phase Return Envelope
    -> deterministic identity/SOT/manifest/coverage verifier
    -> content-bound Machine Verification Receipt
    -> exception-focused Reviewer Readout
    -> reviewer semantic evaluation and disposition
    -> accepted next-phase return or fail-closed return/block
```

The helper never repairs the product, edits an existing review, makes a
closure decision, changes a claim label, or authorizes the next phase.

## Proposed Phase Return Envelope

The existing T1 design is the input contract. Proposed machine-checkable
minimums are:

| Group | Required content | Machine responsibility |
|---|---|---|
| identity | schema version, phase, return ID, batch/problem ID | validate vocabulary and uniqueness boundary |
| predecessor | prior return path/ID/digest and accepted disposition | resolve and compare exact identity |
| authority | canonical owner paths, commit/version, locator, byte-domain digest | resolve, reject archive/non-authority/stale refs |
| claims | stable claim IDs, provenance labels and claim boundaries | validate labels and referential coverage, not correctness |
| obligations | hard/soft obligations and required evidence/verification | identify missing or unverified hard obligations |
| evidence | paths/receipts/results, method/version, inputs and limitations | validate existence, identity and stated result shape |
| constraints | frozen parent constraints and projection digest | compare declared drift and unauthorized changes |
| manifest | expected and actual artifacts with exact identity | reconcile against Git/filesystem changed set |
| costs | provider calls, reruns, elapsed time when available, quota/token evidence | record without inventing unavailable values |
| attribution | agents, roles, providers and invocation surfaces | preserve provenance; never grant trust |
| disposition | readiness, unresolved contradictions, waivers and next requested action | validate vocabulary; reviewer selects semantic disposition |

## Proposed Machine Verification Receipt

The receipt should be canonical, content-addressed and bounded to one envelope
and one verifier closure:

```text
receiptSchemaVersion
phaseReturnDigest
predecessorDigest
repositoryTreeOrCommit
verifierSetDigest
verifierVersions[]
inputDigests[]
deterministicResults[]
claimCoverageSummary
hardObligationFailures[]
manifestReconciliation
exceptions[]
limitations[]
cacheDisposition
receiptDigest
```

Wall-clock fields may be recorded outside the canonical digest or normalized
so identical inputs produce an identical authoritative receipt. The exact
canonicalization profile and byte domain must be fixed before implementation.

## Machine Versus Reviewer Authority Matrix

| Question | Machine/helper | Reviewer |
|---|---|---|
| Do paths, hashes, manifests and predecessor bindings match? | decide deterministically | inspect exceptions only |
| Do authority refs resolve to allowed current owners? | decide structural/currentness rules | judge disputed owner meaning |
| Is every hard obligation linked to evidence/result? | decide coverage | judge whether evidence is substantively sufficient |
| Did focused deterministic tests pass? | execute/parse when authorized | assess limitations and relevance |
| Is a claim semantically correct? | never decide | decide from evidence |
| Is a contradiction material? | surface | decide |
| Is risk acceptable or waiver justified? | never decide | decide within authority |
| Is closure/next phase authorized? | never decide | decide after machine receipt |

## Verification Tiers

### Always-On Core

- envelope schema and phase vocabulary;
- predecessor identity and chain integrity;
- source/authority resolution and freshness;
- expected-versus-actual manifest reconciliation;
- hard-obligation coverage;
- protected-path and external-effect escalation;
- verifier-set/version binding;
- secret-safe output and no raw sensitive evidence;
- receipt self-integrity and exception completeness.

### Phase-Specific Packs

| Phase | Deterministic pack candidates |
|---|---|
| INTAKE | source identity, byte-domain hashes, selected-scope reconciliation, provenance labels |
| DESIGN | capability-evidence presence, source locators, alternatives/unknowns declaration, negative-probe receipts |
| SPEC | invariant/constraint IDs, acceptance traceability, contradiction and nullability/schema checks |
| WORK ORDER | exact manifest, authority, protected paths, rollback, checker read-ahead and dispatch quality |
| BUILD | actual diff, constraint drift, focused tests, dependency and external-effect receipts |
| REVIEW | finding/waiver reconciliation, minimal-verification telemetry, rerun justification and convergence state |
| FREEZE | committed range, immutable artifact identities, closure receipt, continuity and projection freshness |

### Escalation To Broader Verification

Escalate when an always-on check fails, a verifier is unmapped or changed, an
authority boundary changes, an external effect is involved, evidence is
stale/conflicted/unreadable, a focused probe contradicts the return, or a
high-risk acceptance contract explicitly requires broad reproduction.

## Reviewer Minimal Sufficient Verification

The default reviewer readout contains:

- machine PASS/FAIL/BLOCK summary with receipt identity;
- only unresolved exceptions and material claims;
- claims without sufficient non-self-referential verification;
- changed constraints and authority boundaries;
- recommended focused probes with expected information gain;
- explicit statement that no rerun is needed when machine evidence is
  complete and no material contradiction exists.

The reviewer may not use helper PASS as semantic truth. Conversely, the
reviewer should not rerun already-valid deterministic checks merely to produce
a second AI-generated explanation.

## Independence And Anti-Self-Attestation Controls

1. Verifier/checker paths are protected and outside ordinary worker scope.
2. Every receipt pins verifier source/version or a verifier-set digest.
3. If a batch changes a verifier used by its own receipt, that receipt is
   non-admissible for closure; use the pre-change trusted verifier where safe
   and route the verifier change through a separate protected tranche.
4. Generated receipts are immutable inputs to review and cannot be hand-edited.
5. Machine code and fixtures require hostile tests for fail-open behavior,
   spoofed paths, stale receipts, omitted manifests and digest-domain drift.
6. For high-risk canonicalization or authority checks, use an independent
   standard implementation or second deterministic verifier where the added
   cost is justified.
7. A machine receipt proves only its method, inputs, version and limitations.

This creates execution independence from AI narrative at review time. It does
not claim that code is epistemically infallible.

## Cache And Evidence Reuse

Content-addressed reuse may reduce repeated checks only when all of these match:

- phase-return digest;
- repository tree/commit and relevant environment fingerprint;
- verifier-set digest and configuration;
- authority/source digests;
- test inputs and dependency-lock identity;
- no expiry, revocation, checker hardening or contradiction invalidation.

Cache misses or ambiguous invalidation run the relevant verifier; they do not
silently accept an old receipt. Provider/live results are not replayable merely
because local inputs match unless their own evidence contract allows reuse.

## Work Plan / Proposed Delivery Tranches

| Tranche | Mission | Outputs | Exit decision |
|---|---|---|---|
| MFRP-P0 | Claude adversarial critique | external critique plus CVF absorption/reconciliation | `REVISE`, `ACCEPT_DESIGN_DIRECTION`, or `STOP_NO_SAFE_VALUE` |
| MFRP-P1 | owner and contract ratification | exact owner map, envelope/receipt contract, threat model, cost baseline | `CONTRACT_ACCEPTED_BOUNDED` |
| MFRP-P2 | schema and pure deterministic kernel | proposed schema, canonicalization, verifier library and hostile unit tests | `KERNEL_LOCAL_PASS_BOUNDED` |
| MFRP-P3 | helper/readout composition | extend AAF or one non-competing entrypoint; exception-focused reviewer readout | `HELPER_SHADOW_READY` |
| MFRP-P4 | historical replay | representative phase-return fixtures, known defects, false-negative/positive ledger | `REPLAY_PASS` or `RETURN_TO_DESIGN` |
| MFRP-P5 | shadow canary | current bounded tranches run machine preflight without changing authority | `CANARY_PASS` or `ROLLBACK_SHADOW` |
| MFRP-P6 | selective gate activation | earliest applicable gates, trusted receipt admission and fail-closed escalation | `CORE_MACHINE_FIRST_ACTIVE_BOUNDED` |
| MFRP-P7 | seven-phase and downstream adoption | phase templates, workspace projection freshness and adoption proof | `ADOPTION_PROVEN_BOUNDED` |

No tranche opens automatically. P2 and later require an exact protected-path
work order. P7 cannot start before Core closure and explicit downstream release.

## Historical Replay And Hostile Test Matrix

Minimum replay families:

- clean documentation-only phase return;
- same-agent/multi-role return;
- multi-agent/multi-role return;
- missing predecessor and predecessor digest mismatch;
- stale/non-authority/archive source reference;
- expected/actual manifest omission and unauthorized path;
- worker-modified verifier used for self-acceptance;
- stale receipt after checker hardening;
- unrecognized hash byte-domain or normalization recipe;
- hard obligation with only `LLM_INFERRED` support;
- fabricated/missing test receipt;
- constraint drift hidden by passing narrow test;
- secret-bearing evidence or unsafe diagnostic;
- cache hit with exact identity and cache invalidation after one bound input
  changes;
- focused probe contradiction requiring escalation;
- high-risk/live/public/destructive task forced to conservative verification.

Zero tolerance categories: authority bypass, unauthorized paths, secret
exposure, destructive/irreversible action, verifier self-attestation,
predecessor-chain forgery and closure without hard-obligation evidence.

## Metrics And Value Test

Measure before activation and compare against a bounded baseline:

| Metric | Desired direction | Guard against gaming |
|---|---|---|
| reviewer elapsed minutes | down | never waive critical defects |
| reviewer provider calls and token/quota usage | down | unavailable values remain explicit |
| repeated deterministic commands | down | cache reuse requires exact bindings |
| focused probes per review | stable or down | probe count alone is not quality |
| broad reruns | materially down | required release reruns remain allowed |
| machine exception precision | up | record false positives and ignored noise |
| seeded-defect recall | 100% for zero-tolerance classes | fixed test set before canary |
| escaped material defects | zero for zero-tolerance classes | any escape triggers rollback |
| review reversals caused by machine error | zero target | classify checker defect separately |

Activation requires demonstrated latency/quota reduction or equivalent control
value without a material false-negative increase. If telemetry cost exceeds
the saved review cost, simplify or stop.

## Rollback And Kill Conditions

Immediate rollback to the current full trusted review route when:

- any zero-tolerance defect is missed;
- a receipt is accepted after verifier/source invalidation;
- verifier self-modification or receipt forgery succeeds;
- exception filtering hides a material contradiction;
- cache reuse crosses a changed authority/environment boundary;
- machine-first routing causes closure that the legacy route would block.

Rollback must be config/routing based where possible, require no provider or
deployment, preserve receipts for diagnosis, and never erase the failed
evidence. Reactivation repeats replay and canary; operator override alone is
insufficient.

## Cost And Complexity Budgets

- one canonical envelope contract and one canonical receipt contract;
- reuse existing path classification, gate catalogs and helper entrypoint;
- no daemon, watcher, queue, background runtime or arbitrary-command executor;
- no semantic-scoring model or reviewer replacement;
- no provider call in P0-P4;
- no new telemetry field unless it changes a routing, stop, cost or audit
  decision;
- no per-checker metadata program unless replay proves simpler group-level
  mapping insufficient;
- one material plus at most one continuity commit per accepted tranche by
  default.

## Acceptance Criteria

- Claude critique is source-bound, adversarial and reconciled before P1.
- Ownership does not duplicate Truth Foundation, SOT3, SCEC, Review Cost, AAF
  or commit stewardship.
- Every phase can produce a predecessor-bound, SOT-resolvable envelope.
- Machine receipt is canonical, version-bound, tamper-evident and limitation-
  bounded.
- Worker cannot self-authorize by changing verifier or receipt.
- Reviewer readout contains exceptions and material claims, not a duplicate
  narrative of the whole task.
- Broad reruns require explicit evidence and cost justification.
- Historical replay achieves zero misses in zero-tolerance categories.
- Shadow canary shows no unexplained divergence from the trusted route.
- Rollback is tested before activation.
- Downstream remains parked until Core closure and projection proof.

## Claude Critique Questions

1. Is a new narrow Phase Return interface owner justified, or should the
   contract live entirely in existing templates/standards?
2. Which proposed machine checks risk pretending to judge semantic truth?
3. Can the receipt canonicalization and verifier-set binding be simpler
   without creating replay or stale-receipt gaps?
4. Is the anti-self-attestation rule sufficient when verifier code changes in
   the same repository?
5. Which always-on checks are truly invariant across all seven phases?
6. Which phase-specific packs are over-broad or missing a zero-tolerance case?
7. Can cache invalidation be proven without building a costly dependency graph?
8. What historical replay sample is the minimum credible basis for activation?
9. Which metrics can be measured cheaply and which invite ceremony/gaming?
10. Where could exception-focused readout hide a semantic or authority defect?
11. Is the rollout/rollback sequence sufficiently fail-closed?
12. Final disposition: `ACCEPT_DESIGN_DIRECTION`, `REVISE_BEFORE_P1`, or
    `STOP_NO_SAFE_VALUE`, with the three strongest failure modes.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent packet request |
| Chain map route | CVF roadmap -> bounded Claude critique -> external finding absorption -> CVF reconciliation -> operator decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` after return |
| Owner surface | this roadmap plus the paired Claude critique packet |
| Disposition | external output advisory until CVF reconciliation |
| Claim boundary | no implementation or authority transfer to Claude |

## Epistemic Process Block

### Expected Result / Prediction

Machine-first verification should reduce repeated deterministic review work and
AI quota while preserving semantic reviewer authority, if verifier trust,
receipt freshness and false-negative rollback are controlled.

### Evidence Comparison

Current CVF already has AAF readouts, scaffolds, commit stewardship, broad
autorun guards, SOT/Truth contracts and review-cost controls. The missing
integration is a canonical cross-phase return/receipt and exception-focused
reviewer preflight, not a lack of machine checks.

### Contradiction Or Gap Disposition

The proposal could create a second governance system, an expensive dependency
map, or false confidence from machine PASS. P0 critique and P1 owner decision
must resolve those risks before code.

### Claim Update

This roadmap is a critique-ready design hypothesis, not an accepted
implementation plan.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_truth_foundation_claim_guard.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | roadmap structural groups; external-intake seven-row table; Truth Foundation claim boundaries; active-roadmap public disposition; size thresholds |
| gateRunPurpose | confirm roadmap shape after direct owner/helper inspection |
| claimBoundary | checker PASS cannot accept the architecture or replace Claude/CVF review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator / roadmap author |
| Provider or surface | local private provenance repository |
| Session or invocation | GCLH-MFRP P0 planning, 2026-09-01 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, `apply_patch`, focused machine checks |
| Target paths | this roadmap; paired Claude critique packet; GCLH master roadmap |
| Allowed scope source | operator request for detailed roadmap and Claude critique before implementation |
| Before status evidence | clean worktree at `90c2952b642e962c274e07f1f1f5b7cda03d4451` |
| After status evidence | critique-ready planning artifacts only; implementation held |
| Diff evidence | exact three-path material changed set before commit |
| Approval boundary | roadmap and critique packet authoring only |
| Claim boundary | no implementation, downstream, provider/live, public, deploy or production authority |
| Agent type | orchestrator / roadmap author |
| Invocation ID | `gclh-mfrp-p0-roadmap-2026-09-01` |
| Expected manifest | this roadmap; paired Claude critique packet; GCLH master roadmap |
| Actual changed set | same three paths |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: long-horizon private Core governance planning and critique context;
public-sync is not authorized.

## Claim Boundary

This roadmap proposes a machine-first review architecture for critique. It does
not accept that architecture, implement a helper/checker/schema/hook, activate
SOT3 globally, modify downstream workspaces, or authorize provider/live,
public-sync, deployment, release or production behavior.
