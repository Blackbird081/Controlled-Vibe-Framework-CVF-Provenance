# CVF External Agent Invocation Control Knowledge Readiness Roadmap

Memory class: FULL_RECORD

Status: T2_POLICY_SEMANTICS_CLOSED_PASS_T3_PARKED

docType: roadmap

Date: 2026-07-22

Roadmap ID: CVF-EAIC-KR

## Purpose

Establish the authoritative knowledge and provider-neutral control architecture
required before CVF attempts another external-agent CLI/MCP invocation. This
roadmap is knowledge-first. It does not authorize an agent launch, provider
call, runtime implementation, live proof, or moratorium lift.

## Authorization / Decision

Operator authorization on 2026-07-22 first released T0 packet authoring and
manual dispatch. After accepted T0 closure and the governance-load evidence
audit, the operator approved a bounded T1 official-primary-source intake.
On 2026-07-23, after accepted R1B decision evidence, the operator ratified the
four T2 policy directions and released documentation-only T2 manual dispatch.
T3-T5 remain held by their release rules.

## Operator Decision And Priority Register

The operator accepted the following order on 2026-07-22. Completion of one row
does not automatically release the next row.

| Priority | Lane | Current disposition | Release condition |
| --- | --- | --- | --- |
| 1 | External-agent invocation control knowledge readiness | T2 CLOSED_PASS; T3 PARKED | T2 closed with reviewer repairs; T3 requires fresh operator authorization |
| 2 | Governance-load reduction under MSEA-R72 | PARKED_ORDERED_NEXT | Fresh operator selection after priority 1 reaches a bounded decision point |
| 3 | Operator-approved provider/model assignment and invocation receipts | SUBORDINATE_TO_PRIORITY_1 | Reconcile it as one component of the accepted invocation-control architecture; do not run independently |
| 4 | MAO live/provider value pilot | VALUE_PARKED | Existing measurable reopen conditions and fresh operator authorization are satisfied |
| 5 | Continuous Projection T4 retry | CLOSED_BLOCKED_BOUNDED_NO_RETRY | Existing evidence-based reopen condition and fresh operator authorization are satisfied |

## Current Evidence

- The active invocation-control audit records no effective lifecycle owner for
  an external-agent process and its internal loop.
- Existing Model Gateway owners cover provider/model records, request-level
  receipts, credentials, fallback, and provider execution, but not the whole
  external-agent process tree or cumulative assignment budget.
- The provider/model assignment roadmap is parked by the global reassessment.
- The MAO live pilot closed with value not proven.
- Continuous Projection T4 closed blocked bounded and has no retry authority.

## Scope / Methodology

In scope:

- repo-local authoritative-source inventory and gap classification;
- evidence-class separation for API-key spend, subscription quota, token
  telemetry, estimates, and unknown usage;
- knowledge needs for admission, process identity, descendant termination,
  cancellation, monitoring, cumulative budgets, retry/fallback, reconciliation,
  bypass analysis, and fail-closed behavior;
- an operator-reviewable acquisition manifest for missing primary knowledge;
- later architecture and build-readiness decisions after knowledge intake.

Out of scope:

- agent CLI or MCP invocation;
- provider/API/account-subscription use;
- browser, network, Web research, or external-repository cloning;
- runtime, checker, hook, script, source, test, or session-state implementation;
- secrets, live proof, public-sync, push, deployment, or production action;
- treating provider-local memory or chat history as CVF authority.

## Non-Goals

- no immediate MCP server, external-agent launcher, or supervisor build;
- no provider or model ranking;
- no claim that subscription quota equals API spend;
- no precise token-saving or cost-saving multiplier;
- no automatic transition from knowledge mapping to implementation.

## Design Control Gate

| Control | Disposition |
| --- | --- |
| knowledge before architecture | PASS - T0 and T1 precede contract or owner selection |
| architecture before implementation | PASS - T2-T4 precede any separate build roadmap |
| provider neutrality | PASS - access modes are evidence classes, not preferred providers |
| fail-closed unknown usage | RATIFIED_FOR_T2_DOCUMENTATION - automatic or unattended launch fails closed; implementation remains unauthorized |
| external-service authority | DENIED - requires a later explicit operator checkpoint |

## Agent Internal Autonomy And Invocation Perimeter

CVF governs the parent assignment, separately dispatched sessions, external
CLI/MCP and provider boundaries, aggregate resource envelope, mutations, and
reviewable outcome evidence. It does not permission each provider-native
internal helper, reasoning branch, exploration pass, task decomposition, or
context-management choice inside an already-authorized agent session.

An internal helper becomes a separately governed invocation only when it
independently crosses a process, external service, provider/account,
credential, durable-action, scope, or authority boundary.

## Operator-Ratified T2 Policy Direction

The operator approved the following documentation-level policy direction on
2026-07-23 after reviewing the accepted R1B decision supplement:

| Decision | Operator disposition | Ratified policy direction | Evidence boundary |
| --- | --- | --- | --- |
| EAIC-T2-D1 | REPLACE | deny an automatic external launch unless an approved assignment, cumulative envelope, identity plan, stop conditions, and receipt target exist before launch | operator safety policy with an explicit admission-owner and implementation gap |
| EAIC-T2-D2 | ACCEPT | issue CVF task and invocation IDs before launch, then bind provider session, conversation, and root-process identity when observable; absence stays explicit | no current cross-layer runtime binding is claimed |
| EAIC-T2-D3 | ACCEPT | account retry, resume, fallback, and separately dispatched external children at the parent assignment; provider-native internal helpers remain autonomous and observable aggregate usage is charged to the parent | no current provider-neutral envelope owner or enforcement is claimed |
| EAIC-T2-D4 | ACCEPT | fail closed for automatic or unattended launch when reliable admission-time usage is unavailable; a manual exception requires separate bounded operator authorization | no host is claimed to expose reliable usage universally |

T2 must also separate operator-approved provider/model assignment from the
provider/model observed at execution. A mismatch is explicit, and an
unavailable observation remains unknown. This reconciliation requirement does
not select or hard-code any provider or model.

## Knowledge Sufficiency Stop Rule

No later tranche may manufacture semantics merely to keep the roadmap moving.
If a critical domain remains `MISSING_PRIMARY_SOURCE`, or remains
`OPAQUE_BY_ACCESS_MODE` without enough authority for a safe decision, the lane
returns `PARKED_KNOWLEDGE_GAP`.

External knowledge may be absorbed later through the canonical intake chain
after the operator approves exact source classes, roots, and any network or
source-mirror action. External material remains input for reconciliation, not
automatic CVF authority. Parking is the correct result when the foundation is
insufficient.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | authorized parent agent session | provider-native reasoning, exploration, decomposition, and context management remain autonomous inside parent scope | worker-autonomy, delegation-boundary, and dual-surface standards | internal helpers inherit parent scope; no per-helper adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future invocation supervisor or adapter owner not yet selected | no external launch, provider/account use, or runtime control authority while knowledge is insufficient | predecessor audit and nine-domain knowledge map | adapter owner remains parked behind knowledge and operator approval | `DEFERRED_WITH_REASON` |

## Work Plan

| Tranche | Objective | Status |
| --- | --- | --- |
| T0 | Inventory repo-local authority, classify gaps, and produce an authoritative-source acquisition map | CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIRS_AND_BOUNDARY_CORRECTION |
| T1 | Absorb operator-approved primary sources into a reconciled knowledge ledger | CLOSED_PASS_BOUNDED_PARKED_KNOWLEDGE_GAP |
| T2 | Ratify provider-neutral budget, telemetry, stop, retry/fallback, and receipt semantics | CLOSED_PASS_WITH_REVIEWER_REPAIRS |
| T3 | Select one admission-monitor-stop-reconcile owner architecture and threat model | HOLD_PENDING_OPERATOR_AUTHORIZATION |
| T4 | Produce a build-readiness decision and negative-proof plan | HOLD_UNTIL_T3_PASS |
| T5 | Open a separate implementation roadmap if and only if the operator lifts the moratorium | HOLD_UNTIL_FRESH_OPERATOR_AUTHORIZATION |

## T0 Bounded Objective

T0 reads only current repository-controlled sources. It must distinguish:

1. existing CVF authority;
2. evidence-only or advisory material;
3. selectively absorbed external hypotheses already recorded by CVF;
4. missing primary knowledge requiring later operator-approved acquisition;
5. topics that cannot be normalized across access modes.

T0 must not fetch the missing sources or propose executable implementation.

## Knowledge Domain Matrix

| Domain | T0 question | Required terminal disposition |
| --- | --- | --- |
| launch admission | Which CVF owner can approve or deny an external-agent launch? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |
| process identity | How are caller, process, descendants, task assignment, and receipt bound? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |
| cancellation and termination | What semantics apply to graceful cancel, timeout, and full tree termination? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |
| usage telemetry | Which token, turn, tool, quota, spend, and latency signals are observable by access mode? | OWNED, PARTIAL, OPAQUE_BY_ACCESS_MODE, or MISSING_PRIMARY_SOURCE |
| cumulative budget | Which owner enforces one envelope across retry, resume, fallback, and subagents? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |
| unknown usage | What must fail closed when usage cannot be measured reliably? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |
| bypass and threat surface | Which shell, IDE, browser, plugin, subprocess, and provider-native paths evade mediation? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |
| cost-aware task compilation | Which work can be compiled and checked locally before a paid agent loop? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |
| reconciliation | How do approval, assignment, actual identity, usage, stop reason, and result reconcile? | OWNED, PARTIAL, or MISSING_PRIMARY_SOURCE |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| external-agent lifecycle owner is not currently effective | RUNTIME_BEHAVIOR | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` | Findings / Position; Source ownership map | External agent CLI | invocation-control audit | ACCEPT |
| cumulative budget and in-flight stop are unresolved | RUNTIME_BEHAVIOR | `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` | Quality Findings F-03 and control matrix | F-03 | invocation-control audit | ACCEPT |
| provider/model roadmap is parked | VALUE_SET | `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` | top-level Status | Status | provider/model roadmap | ACCEPT |
| MAO live value is not proven | VALUE_SET | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | top-level Status; Next Allowed Move | Status | MAO value pilot roadmap | ACCEPT |
| Continuous Projection T4 is closed blocked bounded | VALUE_SET | `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md` | top-level Status | Status | Continuous Projection roadmap | ACCEPT |

## Roadmap Release Rules

- T0 is documentation and evidence only.
- T1 requires independent T0 acceptance plus operator approval of every source
  root, network action, or source-mirror action.
- T2 may record an explicit operator-owned normative safety policy where
  external evidence is insufficient, but it must label the evidence gap and
  must not convert policy into a runtime, implementation, or host-capability
  claim.
- T3 cannot choose a runtime owner until T2 defines enforcement semantics.
- T4 must return NOT_READY if any critical domain remains PARTIAL,
  OPAQUE_BY_ACCESS_MODE without a fail-closed policy, or missing authority.
- T5 requires a new roadmap, fresh GC-018, source-verified work order, and an
  explicit operator decision lifting the invocation moratorium.

## Acceptance Criteria

- [x] Priority order and parked dependencies are recorded.
- [x] T0 is bounded to repository-local knowledge mapping.
- [x] CLI/MCP/provider/API/browser/network use is forbidden.
- [x] Provider/model assignment is treated as a subordinate component.
- [x] No implementation or live-proof authority is implied.
- [x] Every later tranche has a checkable release condition.

## Verification / Evidence

T0 dispatch evidence consists of current source paths and status lines, the
paired GC-018 and work order, exact changed manifest, ASCII/file-size checks,
and the pre-dispatch autorun result. These prove dispatch shape only.

## Current Runtime Freshness Verification

Reviewer closure re-read the current system-chain map, GC-009/GC-010 gap
entry, orchestration contract, MAO launcher, MCP contracts/adapters, governed
command launcher, and Model Gateway credential/execution owners at closure
base `1e689ed52`. The nine-domain states remain current repository evidence;
no runtime was invoked or changed.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | Status; Purpose; Scope / Methodology; Source Verification Block; Acceptance Criteria; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm roadmap and paired-dispatch structure after checker read-ahead |
| claimBoundary | checker compliance proves document shape only, not knowledge completeness or runtime control |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: T0 maps existing CVF authority and missing-source classes; it does not ingest new external material |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this roadmap and the T0 source-acquisition map |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | T1 source intake requires fresh operator approval and a separate packet |

## Next Allowed Move

T2 is closed with reviewer repairs. The next bounded move is operator review
of whether to authorize a documentation-only T3 architecture and threat-model
packet. No T3 dispatch is implied by T2 closure. Agent CLI/MCP,
provider/API/account use, process testing, implementation, public-sync, and
every later tranche remain parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private knowledge-readiness planning with no public implementation or
release evidence. The public-sync repository is outside this batch and remains
unchanged.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | paired EAIC-KR-T0 work order | closed bounded reviewer-repair status | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EAIC_KR_T0_COMPLETION_2026-07-22.md` | reviewer decision and operator boundary correction | PASS |
| Roadmap state | this file | `Status: T2_POLICY_SEMANTICS_CLOSED_PASS_T3_PARKED`; T3-T5 held | PASS |
| Registry JSON | corpus registry remains outside this T0 closure scope | no registry mutation authorized | BLOCKED with reason |
| Registry Markdown | corpus registry remains outside this T0 closure scope | no registry mutation authorized | BLOCKED with reason |
| External evidence digest | N/A with reason: T0 ingests no new external source | repository-local evidence only | N/A with reason |
| System loop interlock | T0 knowledge map to future operator source selection | no automatic T1 release | PASS |
| Session continuity | active handoff sync after material commit | reviewer/closer owned | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| T0 domains | 9 terminal rows | 9 terminal rows | PASS |
| critical source-selection rows | 4 | 4 | PASS |
| T1 state | operator-approved manual dispatch | operator-approved manual dispatch | PASS |
| external service use | zero | zero | PASS |
| worker route compliance | no separately dispatched or perimeter-crossing agent | provider-native internal helper only | PASS |

## Claim Boundary

This roadmap orders knowledge and control-design work before implementation.
Its T2 release authorizes only provider-neutral documentation semantics. It
does not control an external agent, measure subscription quota, terminate a
process, select a provider/model, lift the global invocation moratorium, or
establish runtime, public, security, cost, or production readiness.
