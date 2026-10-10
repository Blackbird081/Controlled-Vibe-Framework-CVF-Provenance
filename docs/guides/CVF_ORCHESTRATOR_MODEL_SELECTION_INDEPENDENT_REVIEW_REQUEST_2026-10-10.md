# CVF Orchestrator Model Selection - Independent Design Review Request

Memory class: FULL_RECORD
docType: reference
Status: R2_DESIGN_CONCURRENCE_RECORDED
Date: 2026-10-10
Request ID: CVF-MODEL-SELECTION-DESIGN-REVIEW-20261010
Parent batch: CVF-WORKER-SELECTION-FOUNDATION-20261010

## Purpose

Operator requests independent review and rebuttal of the proposed model-selection
doctrine, contract and system chain. Review the design critically; do not implement
it or infer acceptance from the author's static gate results. This file is the
read-only review brief to transfer to the operator-selected reviewer, not an
implementation work order or an automatic agent/provider invocation.

## Scope / Applies To

Review three DESIGN_DRAFT artifacts as one coherent package. Desired behavior:
the orchestrator chooses an eligible model configuration using version-specific
evidence and learning; the Non coder states outcomes and constraints without
being required to choose a technical model. Further Expense work is parked.

Current workspace HEAD: 807db7d4816878df0b6ea1dd50732e1716ccc615.
The three designs are UNCOMMITTED worktree files and are not present in this HEAD.
Use the exact file bytes below. Git HEAD alone does not identify the review target.

## Current R2 Disposition

The original review and same-reviewer R1 confirmation have been received and preserved.
Local applied the sole R1-B1 correction under conditional CONCUR_WITH_R2; no further
review round is required for this delta. Local response:
`docs/reviews/CVF_MODEL_SELECTION_DESIGN_RECONCILIATION_2026-10-10.md`.
Current R2 hashes and condition verification are in
`docs/reviews/evidence/model-selection-design-review-20261010/r2-evidence.json`.
The R0 pins below and original review instructions are historical. Do not initiate
another original review from them. The next Web context refresh is separately scoped
and has not been performed by this brief.

## Original R0 Target Snapshot

Raw SHA256 over each file's bytes, lowercase hexadecimal:

| Artifact | SHA256 |
|---|---|
| docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_DOCTRINE_DESIGN_2026-10-10.md | 2d0c5f142f21a98c1b150369190a98ff4427e6d674102cf11e345e6b6c8d5fdd |
| docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md | c51f25a5121eb4920871163b641dd5be7f800e801e841901fefb6759aaa6af72 |
| docs/roadmaps/CVF_ORCHESTRATOR_MODEL_SELECTION_SYSTEM_CHAIN_ROADMAP_2026-10-10.md | b9fb2e8d1223fe02e81ea28a08fde2b15d1fc74d6332ead7651a646fca360615 |

For the original R0 review, verify these pins before substantive review. A mismatch means stop review of the
affected file, report the observed hash and ask Local to bind an updated snapshot.
Do not silently review a changed draft. Keep the authored files unchanged.

## Role, Independence And Transfer Boundary

Default route: operator-selected reviewer in the same private workspace is
INTERNAL_AGENT, phase=independent design review, final technical disposition
owner=Local orchestrator with operator scope/assignment authority retained.
The reviewer issues recommendations; it does not ratify frozen doctrine or close
implementation. Provider/model name does not determine internal/external status.

Before transfer, use a separate context that did not author these three drafts.
At review start declare prior involvement and whether any author conclusions or
earlier review findings were visible. If you authored the drafts, decline independent
review and disclose that fact. Prior knowledge need not invalidate ordinary design
review, but disclose it; do not claim a blind experiment or hidden-context proof.
This brief includes hypotheses/questions, not an expected verdict or answer key.

If transferred to Web/remote instead, role=EXTERNAL advisory design reviewer;
phase=advisory critique; final private-CVF verification/decision owner=Local.
Before Web transfer, Local must prepare a public-safe derived review packet using
docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md
and refresh the selected External Agent Read task context. Include the pinned public
GitHub snapshot, current owner/chain map, selected design projection, evidence limits,
open decisions, task binding, manifest/hashes and refresh receipt. Raw private drafts,
private continuity and unpublished internal evidence are not automatically releasable
under this internal brief. Derived files carry their own hashes and disclosed
transformations; they must not claim byte identity with the private target pins above.
Paths and public GitHub alone do not expose these uncommitted private drafts.
Public updates, if selected, go through the sibling public-sync clone and existing
export authorization; publishing this private workspace is forbidden. Web reads the
supplied context and pinned public source before critique. Report unavailable sources
as limits; do not infer private absence or replace them with public versions. The
operator transports the review; Local verifies it against private owners before adoption.
No external repository research or multi-source absorption program is opened.

Coordination owners already apply:
docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_EVIDENCE_RELAY_METHOD.md;
docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md.

## Required Read Order

For a Local reviewer, follow AGENTS.md startup: bootstrap read model,
CVF_SESSION_MEMORY.md and active handoff AGENT_HANDOFF_V63_2026-09-18.md;
use full state only for a targeted missing/contradictory fact. Acknowledge mode,
handoff, next move, parked checkpoint, role, phase and decision owner.

Read docs/reference/guard_orientation/README.md and relevant discovery entry in
docs/reviews/learnings/README.md, especially context eligibility. Then fully read
the three pinned targets. Use these existing owners to test their material claims:

1. docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md
   - Central Rule, Owner Surface Matrix, Receipt Advisory.
2. docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md
   - three registry surfaces and MR-1 through MR-6.
3. docs/reference/CVF_LHW23_T1_MODEL_REGISTRY_SERVICE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md
   and docs/reference/CVF_LHW23_T2_MULTIFACTOR_ROUTING_POLICY_ADVISORY_CONNECTOR_SPEC_2026-05-31.md
   - S2-S4 and documentation-only boundaries.
4. docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md
   - receiving responsibility, total-cost feasibility and Design Control Gate.
5. docs/reference/downstream_gate_profile/CVF_PROJECT_LEARNING_LOOP_STANDARD.md
   - Value Admission, independent states and Forward Application Binding.
6. docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_AND_LEARNING_LOOP_STANDARD.md
   - proof classes and operational versus static claims.
7. docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md
   and docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json
   - six observations, confounds, identity and cost limits; consume without rerunning.
8. docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md
   - reviewer non-duplication and bounded review.

Read more only for a named decision-changing gap. Record actual read scope and
unavailable sources. Provider memory is not canonical evidence.

## Review Questions

These are scrutiny dimensions, not required findings or required architecture.
Challenge the premise or propose simplification where source evidence supports it.

| Dimension | Question to resolve |
|---|---|
| Outcome and Non coder flow | Can the orchestrator make a useful decision without demanding a model choice? Which outcome/budget/rights questions legitimately remain human-owned? |
| Doctrine and owner overlap | Is this a justified composition of existing owners or unnecessary duplication? Does any proposal contradict frozen authority or create a competing registry/receipt/learning owner? |
| Role and admission | Are route authority, method support, task quality and worker/orchestrator/reviewer eligibility truly separate? Can a cheap or assigned model bypass a hard constraint? |
| Version evidence | Are snapshot/alias/channel/effort/harness/tools identified well enough? Can newer versions inherit old scores accidentally? What should happen with unresolved identity or missing papers? |
| Quality uncertainty | Are SUPPORTED/PROVISIONAL/INSUFFICIENT actionable or too subjective? Who may admit provisional use, for which tasks, and what observable acceptance remains required? |
| Cost and latency | Are monetary units, tariffs, subscription allocation, stage timing, unknowns and hard budgets coherent? Can the design choose under sparse telemetry without fabricating optimality? |
| Contract completeness | Do record joins, hash scope, null semantics, enums and transition ownership suffice for the next implementation spec? Which omissions must be resolved before build, and which details may remain implementation-owned? |
| Freeze, drift and fallback | Is the exact pre-dispatch freeze boundary feasible? How are alias movement, changed harness, observed identity mismatch, failed attempt and authorized fallback handled without history rewriting? |
| Learning effectiveness | Does a later decision demonstrate actual application or merely citation? Can a no-change result be legitimate? Do selection states conflict with existing PLL DELIVERY/APPLICATION semantics? |
| Practical system chain | Does each link have an actual future producer/verifier/consumer? Is one real task loop sufficient for a bounded claim? Is the roadmap overengineered or missing an essential boundary? |
| Proof and scope | Are schema validation, actual behavior, independent review and measured savings separated? Does the plan preserve Expense and all parked effects? |

## Adversarial Reasoning Cases

Use thought experiments and source traces, not paid/model executions or fabricated
test PASS results. Select the cases most likely to reveal a substantive design gap:

- No eligible candidate; no relevant quality evidence; only stale/conflicting evidence.
- Moving alias without an exposed snapshot; effort/harness differs from published eval.
- Cheapest model fails one hard quality/method constraint; operator assigns a denied route.
- Published benchmark is strong but Local outcomes conflict; six accepted tasks are related.
- Tokens presented as money; reviewer/rework billing unknown; hard spend cap lacks upper bound.
- Task or tool permissions change after freeze; observed worker model differs from requested.
- Fallback needs a new call but the attempt/effect grant is exhausted.
- Worker observations are used to qualify a reviewer or orchestrator.
- Lesson is cited but no action/result exists; later decision reasonably makes no change.
- Learning application would require touching parked Expense.

For each useful case, explain the expected decision under the draft, whether the
contract forces it, and the smallest change needed if it does not.

## Allowed Actions And Stop Boundary

Allowed: read pinned designs and named sources; verify hashes; inspect exact owner
symbols for a named contradiction; reason about failure cases; write one consolidated
UTF-8 Markdown review to
`.cvf/runtime/cvf-model-selection-design-review-20261010/CLAUDE_REVIEW_RETURN.md`.
This is an ignored transport file under `.gitignore` rule `**/.cvf/runtime/`.
Report its SHA256 in the completion message. Keep review effort bounded and
disclose unavailable timing/token/bill telemetry as unknown. Do not manufacture
a benchmark campaign.

Do not edit the three designs, implementation, checkers, registries, session state,
Expense or learning records; do not commit, push, invoke agents/providers, access
credentials, deploy or activate runtime. No repository-wide scan or live test required.
If an additional effect is needed, report the specific gap and continue independent
read-only critique. Do not write a governed review file under this brief; Local will
verify the transport hash and findings, then preserve its disposition under the
applicable governed artifact rules.

Apply EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Existing 70/70
reviewer-fast PASS is structural evidence only, not independent semantic acceptance.
The roadmap discloses the first structural failure and author read-ahead omission.
Do not repeat all gates just to confirm those author results. Stop after one grouped
review; no autonomous repair/redispatch loop.

## Required Return Format

Return one self-contained Markdown review in this order:

1. Identity/scope: reviewer role/context, prior exposure, target hashes observed,
   sources/read depth, unavailable sources, time/usage where observable.
2. Verdict: READY_FOR_DESIGN_ACCEPTANCE, REVISE_BEFORE_ACCEPTANCE or
   BLOCKED_BY_MISSING_EVIDENCE, with concise reasoning. This is a recommendation,
   not Local closure or execution authority. Separate design-readiness from build-readiness.
3. Consolidated findings table: ID; severity (BLOCKER/MAJOR/MINOR); target path
   and section/line; concrete evidence; failure scenario; consequence; smallest proposed
   correction; existing owner affected; required validation. Distinguish source-backed
   defect, unresolved question and optional improvement. No forced finding count.
4. Rebuttal: strongest alternative to this design, complexity/value tradeoff, and
   any author assumption you reject. Explain what should be removed as well as added.
5. Coverage: each review dimension above assessed or deferred with reason; selected
   adversarial cases and outcomes. Do not claim full repository completeness.
6. Next move: one grouped correction package if needed; what can proceed under design
   authority; what remains held before implementation. No automatic implementation order.
7. Claim boundary: no runtime/provider proof, model ranking, measured savings,
   hidden-context attestation or learning APPLIED claim without evidence.

If no material defect is found, say so with the evidence and limits; do not invent
findings. If evidence is missing, identify which recommendation it blocks rather
than rejecting the entire design by default.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Operator-transfer review brief only. Pins identify current drafts, not a committed
release. No reviewer has yet accepted the package; no invocation is performed by
creating this file. Expense and sourceR2/media/provider/public/deploy/P11 remain parked.
