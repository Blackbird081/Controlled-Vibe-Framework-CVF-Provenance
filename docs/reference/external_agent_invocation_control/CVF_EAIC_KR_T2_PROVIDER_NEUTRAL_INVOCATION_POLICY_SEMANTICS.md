# CVF EAIC-KR T2 Provider-Neutral Invocation Policy Semantics

Memory class: FULL_RECORD

docType: reference

Status: OPERATOR_RATIFIED_POLICY_ONLY_NO_RUNTIME_AUTHORITY

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-T2

## Purpose

Record, as provider-neutral documentation only, the operator-ratified
admission, identity, cumulative-envelope, unknown-usage, stop/retry/fallback,
receipt, and provider/model assignment-reconciliation semantics for
external-agent invocation control. This specification defines policy intent.
It does not implement, prove, or claim any runtime enforcement mechanism. It
does not select an architecture owner. The global external-agent CLI/MCP
invocation moratorium remains fully in force.

## Scope / Applies To

Applies only to the four operator-ratified decisions EAIC-T2-D1 through
EAIC-T2-D4 as recorded in the paired GC-018 baseline's Operator-Ratified
Policy Defaults table and the paired work order's Operator Policy Decision
Receipt table. Does not apply to: architecture-owner selection, runtime
implementation, checker wiring, provider/model selection, CLI/MCP execution,
or any T3+ tranche. This specification is not itself an admission mechanism,
identity binder, budget enforcer, or usage meter; every mechanism gap named
below remains open until a separate, source-verified, operator-authorized
implementation tranche closes it.

## Source-Authority Hierarchy And Non-Authority Rules

| Level | Source class | Authority |
| --- | --- | --- |
| 1 | Operator Policy Decision Receipt (this tranche's four ratified rows) | CANONICAL_POLICY |
| 2 | Current CVF authority (T1 ledger, EAIC-KR roadmap, active handoff, Agent Internal Autonomy And Invocation Perimeter) | CANONICAL |
| 3 | Accepted R1B decision evidence and its independent completion review | ACCEPTED_SECONDARY_EVIDENCE |
| 4 | Operator-authored Interaction Projection specifications cited by R1B | OPERATOR_AUTHORED_PROJECTION; creates no CVF authority |

No statement in this specification upgrades Level 3 or Level 4 evidence into
Level 1 policy. Every normative rule below traces to one of the four ratified
decision rows or to existing Level 2 CVF authority; every other point is
recorded as an explicit unknown or deferred item.

## Source Verification

| Claimed item | Source file | Verified section | Disposition |
| --- | --- | --- | --- |
| Four ratified decision rows and exact text | `docs/baselines/CVF_GC018_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md` | Operator-Ratified Policy Defaults | ACCEPT |
| Four decision rows and operator dispositions (REPLACE/ACCEPT) | `docs/work_orders/CVF_AGENT_WORK_ORDER_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md` | Operator Policy Decision Receipt | ACCEPT |
| Supplemental provider/model reconciliation direction | same baseline | Supplemental operator direction (paragraph following Operator-Ratified Policy Defaults) | ACCEPT |
| D1-D4 remain policy-only with implementation/runtime gaps preserved | same baseline | Audit Finding table (`SATISFIED_BY_OPERATOR_POLICY_WITH_IMPLEMENTATION_GAP`, `SATISFIED_BY_OPERATOR_POLICY_WITH_RUNTIME_GAP`, `SATISFIED_BY_OPERATOR_FAIL_CLOSED_POLICY`) | ACCEPT |
| Internal-agent helpers stay autonomous unless they cross the governed perimeter | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Agent Internal Autonomy And Invocation Perimeter | ACCEPT (CURRENT_CVF_AUTHORITY) |
| R1B accepted D1-D4 evidence comparison and independent review results | `docs/reviews/CVF_EAIC_KR_R1B_COMPLETION_REVIEW_2026-07-23.md` | Independent Decision Review | ACCEPT |
| T1 zero domains reached readiness; three PARTIAL_REMAINS, one OPAQUE_REQUIRES_OPERATOR_POLICY | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | Domain terminal-state summary; Domain Readiness Matrix | ACCEPT |
| Cancel/stop states (requested, acknowledged, stopping, stopped, unable-to-stop) | `.private_reference/legacy/CVF 23.07/CVF_INTERACTION_PROJECTION/02_HUMAN_INTERACTION_LAYER/CANCEL_AND_STOP_CONTRACT.md` | Required rules | ACCEPT (OPERATOR_AUTHORED_PROJECTION, cited via R1B) |
| Cost/quota/retry/timeout fail-closed rules | `.private_reference/legacy/CVF 23.07/CVF_INTERACTION_PROJECTION/04_GOVERNANCE_EVIDENCE_PROJECTION/COST_QUOTA_RETRY_TIMEOUT_PROJECTION.md` | Required rules; Fail-closed behavior | ACCEPT (OPERATOR_AUTHORED_PROJECTION, cited via R1B) |
| Receipt correlation rules | `.private_reference/legacy/CVF 23.07/CVF_INTERACTION_PROJECTION/04_GOVERNANCE_EVIDENCE_PROJECTION/RECEIPT_AND_DIAGNOSTIC_PROJECTION.md` | Required rules | ACCEPT (OPERATOR_AUTHORED_PROJECTION, cited via R1B) |
| ADIF-0047 provider-backed-surface accounting rule | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0047.md` | Remediation | ACCEPT |

## D1: Pre-Launch Admission

Operator disposition: `REPLACE` (accepted as operator safety policy with an
explicit admission-owner and implementation gap).

Ratified text: deny an automatic external launch unless an approved
assignment, cumulative envelope, identity plan, stop conditions, and receipt
target are present before launch.

### Normative admission inputs

Before an automatic external-agent CLI/MCP launch may be considered
admissible under this policy, all five of the following must exist:

1. an approved assignment (a governed Work Order or equivalent authority
   record binding the launch to a specific scope);
2. a cumulative envelope (see D3) that the launch will be charged against;
3. an identity plan (see D2) describing which identity layers will be bound
   and which will remain explicitly unavailable;
4. stop conditions (see D5 below) describing how the launch can be
   cancelled or stopped;
5. a receipt target (see D6 below) describing where correlated evidence of
   the launch will be recorded.

### Deny conditions

A launch is denied under this policy when any of the five inputs above is
absent, expired, or cannot be verified. Absence of any one input is
sufficient for denial; this policy does not define a partial-admission
state.

### Admission-owner and implementation gap

This policy states the deny rule. It does not identify, select, or
implement:

- which CVF component evaluates the five inputs and issues an admit/deny
  decision (`OWNER_SURFACE_NOT_FOUND`, per R1B GAP-01, retained unchanged);
- how a launch is technically prevented once denied (no process-launch
  interception mechanism exists in any CVF-governed source examined by T1
  or R1B);
- any UI, CLI flag, or API surface that would present this decision to a
  human or another agent.

## D2: Task/Receipt/Session/Process Identity

Operator disposition: `ACCEPT`.

Ratified text: issue CVF task and invocation IDs before launch, then bind
them to provider session/conversation identity and root process identity
when each becomes observable; absence must remain explicit.

### Identity layers

| Layer | Description | Availability at admission time |
| --- | --- | --- |
| CVF task ID | identifier issued by CVF policy before launch is considered | policy-level; issuance mechanism not implemented by this specification |
| CVF invocation ID | identifier issued by CVF policy for one specific launch attempt | policy-level; issuance mechanism not implemented by this specification |
| Provider session/conversation identity | host-specific identifier (for example, a Claude Code session ID or a Codex chat ID) | host-dependent; T1 found this documented for some hosts (S6, S13, S14) but not bound to any CVF identifier |
| Root process identity | OS-level process-tree identity of the launched external agent | host-dependent; T1 found no primary source binding this to a CVF task/receipt (GAP-02 in R1B, retained unchanged) |

### Binding rule

When a provider session/conversation identity or a root process identity
becomes observable, it must be bound to the CVF task/invocation ID pair
issued for that launch. When any layer is not observable, the record for
that launch must state the layer as explicitly absent. This policy forbids
treating an unavailable identity layer as if it were bound, inferred, or
irrelevant.

### Runtime gap

The T1/R1B source packet identifies no accepted EAIC owner that issues the
task/invocation ID pair and binds it to provider-session and process-tree
identity. Independent T2 review found generic CVF task-ID and receipt-ID
generation in existing Control Plane contracts, so the gap is not a claim
that CVF has no identifier machinery anywhere. The unresolved gap is the
absence of a selected, source-verified EAIC issuance and cross-layer binding
owner. This is a policy-level normative rule, not proof that the required
EAIC binding exists today.

## D3: Cumulative Envelope

Operator disposition: `ACCEPT` (with the existing internal-autonomy
boundary).

Ratified text: account at the parent assignment level across retry, resume,
fallback, and separately dispatched external children; provider-native
internal helpers remain autonomous, while any observable aggregate usage is
charged to the parent.

### Accounting boundary

| Event class | Accounting rule |
| --- | --- |
| Retry of the same launch | charged to the parent assignment's envelope |
| Resume of a previously started launch | charged to the parent assignment's envelope |
| Fallback to an alternate provider/model for the same task | charged to the parent assignment's envelope |
| A separately dispatched external child launched by the parent | charged to the parent assignment's envelope |
| Provider-native internal reasoning/exploration helpers inside the parent's own session | remain autonomous; not separately admission-gated or individually charged under this policy, per the existing Agent Internal Autonomy And Invocation Perimeter boundary |

### Unit separation

Consistent with the accepted R1B evidence (Interaction Projection cost/quota
contract, cited as `OPERATOR_AUTHORED_PROJECTION`, not upstream fact),
subscription/pooled quota and metered per-token cost must be tracked as
distinct units. This policy does not define a conversion rate or a combined
ceiling between them.

### Enforcement gap

No CVF-governed source names a ratified runtime owner that aggregates
retry/resume/fallback/child usage into a single enforced envelope (R1B
GAP-03, retained unchanged). T1 found that host-exposed usage views (Claude
Enterprise pooled quota, Claude API-key pay-as-you-go, Codex plan-dependent
credits) are host-specific and non-interchangeable; no source defines a
provider-neutral aggregation mechanism.

## D4: Unavailable Usage (Fail-Closed)

Operator disposition: `ACCEPT`.

Ratified text: fail closed for unattended or automatic launch when reliable
admission-time usage cannot be obtained; any future manual exception
requires a separate bounded operator authorization.

### Fail-closed state machine

| Usage-availability state at admission time | Automatic/unattended launch | Manual launch |
| --- | --- | --- |
| Reliable usage figure obtained | proceeds to D1 admission evaluation | proceeds to D1 admission evaluation |
| Usage unavailable, untrusted, or stale | DENIED (fail-closed) | requires a separate, bounded, explicit operator authorization not defined by this specification |

### Telemetry gap

T1 found that both examined host families (Claude, Codex) expose interactive
usage state that depends on plan/authentication, with no primary source
guaranteeing a machine-readable value before every launch. This is the one
T1 domain that reached `OPAQUE_REQUIRES_OPERATOR_POLICY` rather than
`PARTIAL_REMAINS`; the operator ratification above resolves the *policy*
question (what to do when usage is unknown) without resolving the
*telemetry* question (whether reliable usage will ever be obtainable for a
given host/plan combination). That telemetry gap remains open.

## D5: Stop, Cancel, and Retry/Fallback Interaction Matrix

Not a separately numbered operator decision; derived from the D1 stop-
condition requirement, the D3 retry/fallback accounting rule, and the
accepted R1B cross-decision consistency check.

### Stop states

Consistent with the accepted R1B evidence (Interaction Projection cancel/
stop contract, `OPERATOR_AUTHORED_PROJECTION`), a stop or cancellation
request must be represented as one of: requested, acknowledged, stopping,
stopped, or unable-to-stop. This policy does not define which CVF component
transitions between these states or how a "stopped" determination is
verified against the actual external process.

### Retry/fallback after a stop

A retry or fallback that follows a stop, cancellation, or fail-closed denial
must be treated as a new launch subject to full D1 admission evaluation. It
is not automatically re-admitted, and its usage is charged per the D3
accounting rule as a new event within the same parent envelope.

### Mapping gap

R1B (GAP-06) identified that the D1-D4 proposed defaults did not specify
which stop state a fail-closed denial or an unknown-usage stop maps to. This
specification resolves that gap at the policy level: a fail-closed D4 denial
and a denied D1 admission are both treated as never having reached
"requested" in the stop-state model above, because no launch occurred. An
in-flight stop request against an already-admitted launch follows the
five-state model independently. Which CVF component implements this mapping
remains an open runtime gap.

## D6: Receipt Schema (Documentation Level)

Derived from the D1 receipt-target requirement and the D2 identity-binding
rule; no new operator decision is introduced.

### Required receipt fields (documentation level only)

| Field | Description | Runtime status |
| --- | --- | --- |
| CVF task ID | see D2 | DOC_ONLY_NEW; no invented runtime field claim |
| CVF invocation ID | see D2 | DOC_ONLY_NEW |
| Admission decision | admit or deny, with the specific D1 input(s) that were absent if denied | DOC_ONLY_NEW |
| Identity binding record | per-layer bound/absent state from D2 | DOC_ONLY_NEW |
| Envelope charge | which parent assignment envelope the event was charged to, per D3 | DOC_ONLY_NEW |
| Usage-availability state | reliable, unavailable, untrusted, or stale, per D4 | DOC_ONLY_NEW |
| Stop-state transitions | sequence of states reached, per D5 | DOC_ONLY_NEW |
| Approved provider/model assignment | see Provider/Model Assignment Reconciliation below | DOC_ONLY_NEW |
| Observed provider/model | see Provider/Model Assignment Reconciliation below | DOC_ONLY_NEW |
| Assignment reconciliation state | `MATCH`, `MISMATCH`, or `UNKNOWN_NOT_EXPOSED` | DOC_ONLY_NEW |

A provider message without CVF correlation to the fields above is not a CVF
receipt, consistent with the accepted R1B evidence (Interaction Projection
receipt contract, `OPERATOR_AUTHORED_PROJECTION`). Existing CVF receipt
contracts and durable receipt stores do not by themselves implement this D6
schema. The T1/R1B/T2 source packet identifies no accepted EAIC owner that
persists and correlates all D6 fields as live runtime data.

## Provider/Model Assignment Reconciliation

Per the paired baseline's supplemental operator direction, this
specification defines three distinct fields and their reconciliation:

- `approvedProvider` / `approvedModel`: the provider and model the operator
  approved for a given assignment, when one was supplied. This
  specification does not select or hard-code a default provider or model;
  the fields exist only to record an operator-supplied value when present.
- `observedProvider` / `observedModel`: the provider and model actually
  observed at execution time, when the execution surface exposes this
  information. When not exposed, this field is recorded as
  `UNKNOWN_NOT_EXPOSED`, never inferred or defaulted to the approved value.
- `assignmentReconciliationState`: exactly one of `MATCH` (approved and
  observed values are equal), `MISMATCH` (both values are known and
  differ), or `UNKNOWN_NOT_EXPOSED` (either value is unavailable, so no
  comparison can be made). A `MISMATCH` state must not be silently resolved
  in either direction; this policy requires the mismatch to remain visible.

## Provider-Backed Surface Accounting (ADIF-0047)

Per `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0047.md`,
this specification requires that any future implementation or worker return
that reports invocation, provider-call, usage, quota, or cost evidence under
this policy separate at least three facts:

1. the host execution surface (for example, "provider-backed CLI session");
2. worker-initiated or policy-initiated outbound/recursive invocations
   (a bounded, directly observable count); and
3. measured host-session usage/quota (from an exposed receipt only, else
   `UNKNOWN_NOT_EXPOSED`).

A zero-count claim is valid only for the specific bounded event class
actually observed (fact 2). It must never be used to imply zero consumption
of fact 3 when fact 3 is not exposed.

## Cross-Decision Consistency Check

| Cross-cutting concern | D1 | D2 | D3 | D4 | Consistency finding |
| --- | --- | --- | --- | --- | --- |
| Admission | primary subject | precondition (identity plan required before launch) | precondition (envelope required before launch) | precondition (usage must be known or fail-closed) | The four decisions form one coherent precondition chain; D1's own ratified text lists identity, envelope, and usage-known/fail-closed as admission prerequisites. No internal contradiction. |
| Identity | referenced as precondition | primary subject | not directly referenced | not directly referenced | Consistent; D2 is the only row defining identity mechanics. |
| Cumulative accounting | referenced as precondition | not directly referenced | primary subject | receipts of usage feed D4's fail-closed check | Consistent; D3 defines the accounting boundary D4's availability check depends on. |
| Retry/resume/fallback | not directly referenced | not directly referenced | explicitly included in the envelope | a retry after a fail-closed stop re-triggers D4 | Consistent; D3's envelope explicitly includes retry/resume/fallback, and D5 applies the same fail-closed boundary. |
| Internal-agent autonomy | not directly referenced | not directly referenced | explicitly preserved | not directly referenced | Consistent with the existing Agent Internal Autonomy And Invocation Perimeter boundary; no ratified row expands CVF control over internal reasoning steps. |
| Stop/cancel | referenced as precondition | not directly referenced | not directly referenced | fail-closed denial is treated as pre-launch, not a stop event | Resolved at the policy level in D5; see Mapping gap above. |
| Receipts | receipt target required before launch | correlation required | envelope charge implies a receipt trail | usage-unavailable stop implies a diagnostic receipt | Consistent; all four decisions converge on the D6 receipt schema. |

## Epistemic Process Block

### Expected Result / Prediction

Translating the four operator-ratified decisions into provider-neutral
documentation was expected to produce one internally consistent policy
contract, because R1B's independent review already found no contradiction
between the four proposed defaults and the accepted evidence base.

### Evidence Comparison

Comparing each ratified decision (D1-D4) against the T1 primary-source
ledger, the accepted R1B evidence, and the existing EAIC-KR roadmap
authority confirmed the prediction: every normative rule in this
specification traces to a ratified decision row or existing Level 2 CVF
authority, and the Cross-Decision Consistency Check found no internal
contradiction across admission, identity, cumulative accounting, retry/
resume/fallback, internal-agent autonomy, stop/cancel, and receipts.

### Contradiction Or Gap Disposition

No contradiction was found between the four ratified decisions or between
this specification and its accepted source evidence. Nine gaps (GAP-01
through GAP-09) remain explicitly open and are preserved rather than
resolved by inference. GAP-01 through GAP-05 are retained unchanged from
R1B. GAP-06 is retained from R1B with its policy mapping refined while its
implementation gap remains open. GAP-07 through GAP-09 were newly identified
while drafting D2/D6 and assignment reconciliation.

### Claim Update

The four operator-ratified decisions, together with the D5 stop-state
mapping and D6 receipt schema derived from them, form a coherent
provider-neutral policy contract. No decision contradicts another. This
specification does not require a further operator decision to be internally
consistent; it does require a separate, source-verified, operator-authorized
implementation tranche before any of the preserved gaps below can be
closed.

## Contradiction And Gap Ledger

| Gap ID | Description | Preserved as | Source |
| --- | --- | --- | --- |
| GAP-01 | No CVF component is identified that evaluates the D1 five admission inputs and issues an admit/deny decision. | admission-owner gap | R1B GAP-01, retained |
| GAP-02 | No source binds CVF task/receipt identity to an OS process tree. | process-binding gap | R1B GAP-02, retained |
| GAP-03 | No source defines a ratified runtime owner that aggregates retry/resume/fallback/child usage into one enforced provider-neutral envelope. | cumulative-enforcement gap | R1B GAP-03, retained |
| GAP-04 | No source guarantees machine-readable pre-launch usage telemetry for every plan/authentication combination. | unknown-usage telemetry gap | R1B GAP-04, retained |
| GAP-05 | No source proves runtime enforcement of any policy rule in this specification. | runtime-proof gap | R1B GAP-05, retained |
| GAP-06 | Which CVF component transitions between the five stop states, and how a "stopped" determination is verified against the actual external process, remains unspecified. | stop-state implementation gap | derived from R1B GAP-06, mapping resolved at policy level above, implementation still open |
| GAP-07 | Existing generic CVF task/receipt identifier machinery is not selected or source-verified as the EAIC owner for issuing one task/invocation ID pair before launch. | EAIC identity-owner gap | new, identified while drafting D2; narrowed by independent T2 review |
| GAP-08 | Existing CVF receipt stores do not establish an accepted EAIC owner that persists and correlates the complete D6 schema. | EAIC receipt-owner gap | new, identified while drafting D6; narrowed by independent T2 review |
| GAP-09 | The accepted T1/R1B/T2 source packet does not expose `observedProvider`/`observedModel` telemetry from the current worker execution surface as a CVF-queryable field. | assignment-observation evidence gap | new, identified while drafting Provider/Model Assignment Reconciliation; bounded to the accepted source packet |

All nine gaps remain open. This specification closes none of them; it only
states the policy that will govern their eventual closure.

## Reviewer Source-Fidelity Addendum

The original worker correctly treated the proposed D6 fields as doc-only,
but its GAP-07 and GAP-08 wording over-expanded a bounded source-packet gap
into a repository-wide absence claim. Independent review established:

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CVF already generates generic task IDs | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/design.contract.ts` | `makeTaskId` implementation | `makeTaskId` | design-task construction | ACCEPT; prevents global absence claim |
| CVF already generates agent execution receipt IDs tied to a task ID | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | `createReceipt` | `receiptId`, `taskId` | `AgentExecutionAuditReceipt` | ACCEPT; not an EAIC task/invocation binding owner |
| CVF already has a durable governed-execution receipt store | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | `GovernedExecutionStore`; `JsonGovernedExecutionStore` | `beginExecution`, `finalizeExecution` | governed execution persistence | ACCEPT; does not implement the complete D6 schema |
| accepted T2 packet selects an EAIC issuance/correlation owner | T1/R1B/T2 accepted source packet | D2/D6 evidence and gap rows | `EAIC_OWNER` | N/A | BLOCKED_SOURCE_NOT_FOUND |

These existing mechanisms are evidence against broad nonexistence, not
authority to reuse them for EAIC. T3 must compare candidate owners and their
contracts before selecting or adapting one.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| D1-D4 ratified policy text | this specification | ENRICH_EXISTING | first documentation-level normative expression of the ratified policy | create this specification |
| Stop-state and receipt schema derivation (D5, D6) | Guard Contract (`governed-capability.contract.ts`, `receipt-envelope.contract.ts`, `runtime-workflow.contract.ts`) named in R1/R1B | ENRICH_EXISTING | documentation-level schema only; no field added to those contracts | secondary evidence only; no schema/runtime import |
| Provider/model assignment reconciliation | Model Gateway/EAIC owner surfaces named in the R1 audit | ENRICH_EXISTING | new `approvedX`/`observedX`/reconciliation-state vocabulary, doc-only | no owner or runtime change |
| Admission-owner mechanism | `OWNER_SURFACE_NOT_FOUND` | REJECT_DIRECT_IMPORT | no accepted mechanism | preserve as GAP-01 |

## Architecture-Owner Decisions Deferred To T3

The following decisions are explicitly out of scope for this documentation
tranche and are deferred to a future, separately authorized T3 architecture
and threat-model tranche:

- which CVF component or extension owns admission evaluation;
- how task/invocation ID issuance is implemented and where IDs are stored;
- how process-tree identity is captured and bound (Windows Job Objects,
  POSIX process groups, or another mechanism, per T1 findings S8-S11);
- how the cumulative envelope is computed, stored, and enforced across
  retry/resume/fallback/children;
- how pre-launch usage telemetry is obtained per host/plan combination, and
  what "reliable" means in machine-checkable terms;
- how stop-state transitions are implemented and verified;
- how the D6 receipt schema is persisted and queried;
- how `observedProvider`/`observedModel` telemetry is captured from a live
  execution surface.

## T2 Runtime Boundary Statement

This specification is `OPERATOR_RATIFIED_POLICY_ONLY_NO_RUNTIME_AUTHORITY`.
It does not implement, prove, or claim: an admission mechanism, an identity
binder, a cumulative-envelope enforcer, a usage meter, a stop-state
supervisor, a receipt store, or a provider/model observation mechanism. The
global external-agent CLI/MCP invocation moratorium remains fully in force.
T3 and all runtime/external-action lanes remain parked pending separate
operator authorization.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | operator-ratified provider-neutral policy documentation for admission, identity, cumulative envelope, unknown usage, stop/retry/fallback, receipts, and provider/model reconciliation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: the D6 receipt schema is a documentation-level field list; no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed. |
| invocationBoundary | manual operator copy/paste into the already chosen worker surface only; worker ran local repository checks but no agent invocation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, process-tree, wrapper, proxy, or runtime interception claim |
| claimLanguage | operator-ratified provider-neutral documentation policy only |
| forbiddenExpansion | runtime/provider/live/public/package/Web/MCP/model-router, implementation, architecture-owner selection, and invocation-moratorium lift |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private operator-ratified policy specification with no
public implementation or release authority.

## Claim Boundary

This specification proves a source-traceable translation of four
operator-ratified policy decisions into provider-neutral documentation. It
does not prove architecture readiness, runtime enforcement capability,
provider behavior, or that any named mechanism exists. It does not select
an implementation owner, authorize CLI/MCP/provider/API/account/network/
browser use, authorize source execution or process testing, lift the
invocation moratorium, or authorize public-sync, push, deployment, or
production action.
