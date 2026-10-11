# CVF Orchestrator Model Selection Doctrine Design

Memory class: FULL_RECORD
docType: reference
Status: DESIGN_DRAFT
Date: 2026-10-10
Batch ID: CVF-WORKER-SELECTION-FOUNDATION-20261010
Revision: R3 - post-Web design delta (CVF-MS-WEB-01/04/06) over R2; R2 bytes and conditional concurrence remain historical evidence for R2 only

## Purpose

Design an optional orchestrator capability that selects an eligible model
configuration for a governed task using version-specific evidence and learning.
The Non coder supplies the desired outcome and meaningful constraints. Technical
model choice is the orchestrator's responsibility where assigned or delegated by
the operator; no model picker is required.

## Scope / Applies To

Private design for future model-selection decisions. This is a doctrine proposal
under existing owners, not a new frozen doctrine in ECOSYSTEM/doctrine, an active
standard, runtime selector, provider grant or dispatched implementation order.
Expense remains PARKED_BY_OPERATOR. Existing operator assignments are preserved.

## Selection Surfaces And Delegated Choice

Surface B, AGENT_SEAT, is the first use case: a worker in an operator-started IDE
or agent session. Existing work-order, dispatch-envelope and delegation owners
admit this task and record the selection rationale. Its availability, tool access
and configuration are evidenced by that seat; it need not have a Model Gateway
provider entry, health response or GatewayReceipt. Manual declarations and review
are cooperative controls, not interception of host actions or hidden model changes.

Surface A, GATEWAY_API, is deferred: an actual API route through Model Gateway.
PINT-T2, policy, provider/capability registry, health and GatewayReceipt apply there.
A GatewayReceipt companion still requires fresh GC-018. Neither surface's admission
or receipts substitute for the other's. No gateway call is a prerequisite of B.

Operator controls topology and may assign a model explicitly or delegate technical
choice within a named seat/role and allowed set, per task or standing policy. Record
that choice authority in the task before SELECT; selection authority never grants
invocation authority. For an explicit operator assignment, absence of predictive quality history
alone does not hold selection. The evidence-gap exception covers only that missing
history. SELECT records
`operatorAssignmentDisposition=HONORED_WITH_EVIDENCE_GAP`, the confidence limit and
mandatory independent acceptance against the unchanged observable floor. Preserve
the evidence gap; selection does not upgrade quality evidence to SUPPORTED.
Hold an explicit assignment for unavailability, authority/policy/method/context
conflicts, or a known failed hard requirement. Existing task/budget/effect admission
still applies; missing quality history is not itself a known failed requirement.
The exception never waives a mandatory context, authority, budget or effect proof. Such
proof stays pending with its existing owner, so a selection record can stand while
dispatch is held until admission; the gap label is never recorded as PASS for it.
An unassigned seat without delegated choice may receive a recommendation, but cannot
SELECT autonomously. A standing delegation avoids repeated technical questions to the
Non coder. The current design request authorizes design only, not a new live delegation.
The active orchestrator cannot select or replace its own seat under this capability.

## Source Authority And Owner Composition

| Responsibility | Existing owner and anchor | Design disposition |
|---|---|---|
| Supreme authority | ECOSYSTEM/doctrine/ via AGENTS.md Authority Hierarchy | No frozen owner change; proposal subordinate to current hierarchy |
| Topology and model-choice scope | docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md, Topology Invariance Rule | Operator topology/assignment or bounded delegated choice; no automatic-routing claim from this owner |
| Agent-seat task and decision home | docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md; docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md; docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md | Surface B rationale in the existing work order; admitted tools, role/context, return and separate effect grants |
| Intelligence versus route authority | docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md, Central Rule and Receipt Advisory | Intelligence advises; policy and registry admit; receipt records |
| Capability-first candidate discovery | docs/reference/CVF_LHW23_T1_MODEL_REGISTRY_SERVICE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md, S2-S4 | Reuse task -> capability -> registry -> candidate |
| Multiple decision factors | docs/reference/CVF_LHW23_T2_MULTIFACTOR_ROUTING_POLICY_ADVISORY_CONNECTOR_SPEC_2026-05-31.md, S2-S4 | Reuse factors; no active scoring weights inferred |
| Static/runtime/dynamic registry separation | docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md, MR-1 through MR-6 | Enrichment cannot replace supported-method or routability owners |
| Receiving responsibility and delivery cost | docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md, Agent Continuation And Action Readiness | Resolve technical choices within authority; count preparation, execution, review and rework |
| Review cost | docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md | Consume valid returned evidence; avoid duplicate proof |
| Learning admission and application | docs/reference/downstream_gate_profile/CVF_PROJECT_LEARNING_LOOP_STANDARD.md, Value Admission and Forward Application Binding | F2G/PLL only for reusable admitted findings/controls; performance observations stay outcome evidence |
| Operational proof | docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_AND_LEARNING_LOOP_STANDARD.md, Orthogonal Proof Model | Contract linkage and actual system behavior remain separate |
| Current Local observations | docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md, Decision / Disposition | Six worker observations; operator-reported identity; cost unknown; no ranking |

The three gateway/registry rows above concern surface A and advisory discovery
patterns only. For this B proposal, LHW23 factors inform hard-filter-then-reasoned
comparison; weighted adaptive scoring and automatic rollback are not adopted.
Those historical documentation-only specs are preserved, not amended or invalidated.
`EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`, resolveProviderForRole,
uses a supplied role/provider map with a fallback. It is a separate CLI provider
resolver, not evidence of seat admission or of an invoked Gateway path; A integration
must trace its real caller/consumer before reuse.

## Proposed Doctrine Principles

1. Outcome and authority precede optimization. Define the task's acceptance floor,
   methods/tools, integration scope, data/risk boundary, time and spend limits.
   Explicit operator configuration constrains selection but cannot bypass admission.
2. Select a configuration, not a family name: provider, model ID, immutable version
   if exposed, channel, effort, agent harness, tool permissions and evidence window.
   A worker outcome does not qualify the same model as orchestrator or reviewer.
3. Treat authority, method support and quality as distinct dimensions. A healthy,
   routable provider is not automatically competent for the task. Cheap candidates
   cannot compensate for failed hard constraints with a higher weighted score.
4. Use official technical reports, papers, system/model cards and original benchmark
   methods as configuration-bound evidence. Keep provider-reported, independent
   publisher and Local reviewed observations separate. Headline scores are priors,
   not Local acceptance or proof of the selected effort/harness.
5. Doctrine survives model upgrades; evidence does not transfer automatically.
   Keep old results under their original identity. Assess changed version, effort,
   harness, tool set and tariff at the next admitted decision; record applicability.
6. Optimize defensible total accepted-delivery cost among adequately supported
   candidates. Include orchestration, preparation, execution, independent review,
   repairs and probable failure burden. Unknown values stay null. Official tariff
   estimates, subscription charges and measured invoices are different evidence.
7. Prefer a transparent bounded rationale over an invented numeric quality score.
   Use comparable evidence where available; explain confidence and confounds.
   Missing comparison data permits a reasoned choice, never a measured-savings claim.
8. Freeze the decision and source identities before dispatch. Material drift requires
   reassessment before a dependent action. Preserve amendments and previous decisions.
   Fallback/retry/reviewer replacement are new decisions within the existing grant.
9. Learn from accepted, rejected, blocked and stopped returns. Separate technical
   output, process adherence, worker repairs, dispatcher defects and review cost.
   Do not discard failures or blame a worker for an upstream packet contradiction.
10. Prove learning use in a later decision: cite the applicable control/evidence,
    the resulting action or reasoned no-change, and actual verification. A populated
    receipt or learning-plan join proves declaration only.

## Decision Procedure And Uncertainty

Filter hard constraints first: role/choice authority, scope, data policy, the relevant
surface's admission (registered route for A, seat/task/context admission for B),
required methods/tools, quality floor and any hard budget. Preserve each rejection.
Compare the remaining configurations on relevant quality evidence, reliability,
delivery cost and latency with explicit uncertainty. Do not assign fixed task-to-model
rules or assume increasing effort always improves results.

Quality dispositions are SUPPORTED, PROVISIONAL or INSUFFICIENT for the named task.
SUPPORTED requires a relevant observable acceptance floor, applicable reviewed or
published evidence (EXACT or justified PARTIAL), and no unresolved material conflict
affecting that floor. It is not identity verification or universal certification.
PROVISIONAL can be selected without a further human model question only within
recorded choice authority and the proposed bounded envelope: read-only or reversible
local documentation/pure implementation, no protected-control/auth/credential or
external/production effects, adequate tool access, observable independent acceptance
and admitted budgets. It still needs relevant positive evidence; reviewer presence
does not compensate for missing authority or a known failed hard requirement.
Outside that envelope, route the unresolved risk to the existing technical/authority
owner for an explicit allowance or hold. No new risk taxonomy or live grant is created.
For delegated selections, INSUFFICIENT or absent quality evidence yields an evidence
hold or a supported alternative. For an explicit assignment, the evidence-gap clause
above takes precedence; retain INSUFFICIENT if warranted and honor the assignment
with independent acceptance. Known failed hard requirements still hold both branches. In that explicit-assignment
clause, "evidence gap" means predictive quality history only; an unproven mandatory
context, authority, budget or effect precondition stays pending with its owner and is
never closed by the gap label.
These are design-level admission semantics; operational use needs its admitted task.

No eligible configuration means HOLD_NO_ELIGIBLE_CANDIDATE, with the precise gap
and decision owner. Ask the Non coder only about unresolved outcome, budget, rights
or scope choices that materially change the next action. Technical lookup and
ordinary configuration decisions remain with the orchestrator. An unavailable
assigned model produces a hold or an authorized substitution; never silent override.

Missing papers are recorded with the available official evidence and search window;
they neither create fabricated proof nor a universal ban. Stale/conflicting evidence
is retained and narrowed or refreshed for a named decision-changing gap. When an
alias cannot be resolved, use at most PARTIAL evidence with an explicit window,
known configuration and refresh triggers. The contract defines observable identity
and admission separately; a hidden snapshot is not invented to make the tuple complete.

## Cost And Evidence Discipline

Express monetary estimates in a declared currency and tariff unit; tokens are usage,
not money. Record input/output/cache/reasoning units only where the channel exposes
them. Keep estimated worker cost separate from measured accepted-delivery cost.
Time uses matching boundaries; incomplete durations cannot rank models. Do not infer
failure probabilities from the six accepted, related worker observations.
Capacity may instead be measured in quota units, rate limits or wall-clock budgets;
compare a hard cap only to evidence in its own unit/window. Unknown marginal money
is not zero; a monetary cap still needs a supported upper bound. Do not convert
subscription capacity to currency without a declared method and evidence. Outcome
records keep the initial worker return and its first disposition, repair or assistance
attribution, failed or abandoned attempts and remaining parent-task spend apart from
the accepted final artifact; an accepted artifact does not validate the originally
selected configuration.

Existing pipeline cost, quality-proxy, latency and price-fallback limitations are
dated observations in docs/reviews/evidence/cvf-expense-legibility-local-review-2026-10-10.json,
selectionFoundationAudit. Revalidate exact affected source before an implementation
proposal; this design does not repair those paths or treat them as an operating selector.

## Evidence Refresh And Learning

Refresh only evidence affected by new version, changed configuration, stale window,
contradiction or a relevant later outcome. Freeze a selected evidence snapshot rather
than silently substituting a moving web page. Store locator, retrieval time, section,
source revision plus a bounded cited excerpt/summary and its hash where available,
claim, method/configuration and limitations. Retain full third-party content only
where permitted; do not bulk-copy pages by default. Hashes identify retained bytes,
not unseen current web content. A hash without retained content cannot reconstruct it.
No new market lookup or current price/ranking assertion is made by this design.

Use the existing project learning home and typed F2G/PLL parent path when a reusable
gap has incremental value. Covered execution mistakes remain RULE_EXISTS. Preserve
independent resolution, implementation, return and application states. Expense being
parked prevents editing or testing it for loopback; future admitted tasks may consume
the retained evidence without reopening Expense.

The existing six-row tranche ledger is a preserved legacy LOCAL_REVIEWED_OUTCOME
source, with no fabricated decision joins. Its provisionalRoleRouting is historical
eligibility guidance, not active routing authority. Future outcomes have one canonical
home in their task's existing review/evidence record; selection links reference it.
Do not also append a duplicate outcome store to the legacy ledger. Ordinary performance
evidence may inform later decisions without promotion into an F2G/PLL lesson.
Consumption is recorded by each later decision, so zero or many later uses do not
reopen or mutate the earlier frozen decision. Before a later decision consumes an
immutable source, it checks current supersession or retraction and applicability; a
retracted or superseded source may be cited only as historical context. Only the admitted parent-control branch
can claim PLL DELIVERY/APPLICATION; local observations use separately named dispositions.
Reviewer eligibility also requires the dispatch context-eligibility checks; model
quality or a different model name cannot establish independence.

## Related Design Outputs

- docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md
- docs/roadmaps/CVF_ORCHESTRATOR_MODEL_SELECTION_SYSTEM_CHAIN_ROADMAP_2026-10-10.md

## Epistemic Process Block

Expected Result / Prediction: configuration-bound evidence and total-cost reasoning
can make model choice reviewable without burdening the Non coder.
Evidence Comparison: existing owners support the composition; six worker observations
support bounded eligibility and retain unknown identity verification, bills and confounds.
Contradiction Or Gap Disposition: current end-to-end selector and learning effectiveness
are unproven; future implementation and admitted use proof remain separate.
Claim Update: DESIGN_DRAFT only; no model ranking, saving or behavioral adoption claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

One Local INTERNAL_AGENT authored this proposal; phase=internal design; decision owner=Local.
R0 critique and same-context R1 confirmation are retained. Local verified the R1-B1
correction under the reviewer's conditional CONCUR_WITH_R2; no second review occurred.
R3 is an INTERNAL_AGENT worker design delta applying CVF-MS-WEB-01/04/06; it has no
independent acceptance until Local review, and the R2 concurrence does not extend to R3 bytes.
No frozen doctrine ratification, runtime/subagent activation,
provider call, current market certification, public-sync or deployment evidence.
