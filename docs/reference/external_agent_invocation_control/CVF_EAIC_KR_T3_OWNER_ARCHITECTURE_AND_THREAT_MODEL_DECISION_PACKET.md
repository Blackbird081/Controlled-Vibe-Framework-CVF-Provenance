# CVF EAIC-KR T3 Owner Architecture And Threat Model Decision Packet

Memory class: FULL_RECORD

docType: reference

Status: ARCHITECTURE_DIRECTION_OPERATOR_ACCEPTED_NO_BUILD_AUTHORITY

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-T3

## Purpose

Compare four candidate accountable-owner architecture patterns for one
admission-monitor-stop-reconcile external-agent invocation control point,
recommend one pattern as decision support without ratifying it, map the
recommendation against the T2 D1-D6 policy and its nine preserved gaps,
produce a threat model, and define the negative-proof evidence a future T4
tranche would need. This packet implements nothing. It selects no runtime
owner. It does not authorize CLI/MCP invocation, provider/API/account use,
network, browser, process control, or moratorium lift.

## Scope / Applies To

Applies only to architecture-comparison decision support for the T3 tranche
of the CVF-EAIC-KR roadmap. Does not apply to runtime implementation, final
owner ratification, provider/model selection, T4/T5 release, or any external
action. The operator accepted CANDIDATE-D on 2026-07-23.
`operatorSelectionState` is `ACCEPTED`; this selection does not authorize T4,
implementation, or any external action.

## Bounded Recommendation

CANDIDATE-D (a new EAIC coordinator composing existing primitives) is
recommended as decision support, not as a ratified owner. The rubric
comparison below finds that CANDIDATE-A, CANDIDATE-B, and CANDIDATE-C each
own real bounded primitives (receipt-gated command execution, session policy
evaluation, and provider/quota routing respectively) but none owns the
external-agent process lifecycle, cross-component cumulative envelope, or
stop-state supervision that D1-D6 require together. Promoting any one of
them to universal owner would require stretching it across a trust boundary
it does not currently cross, which the Cross-Decision Consistency Check in
the T2 specification and the Contradiction Handling Requirement in this
packet's Epistemic Process Block both treat as a downgrade condition, not a
gap to silently absorb. CANDIDATE-D avoids that overreach by naming one new
accountable interface above the existing launcher, session contract,
receipt/execution stores, and Model Gateway, while explicitly deferring the
interface, storage, adapter, monitoring, stop, and proof design that do not
yet exist. This recommendation does not authorize building that interface;
it only names the least-overreaching shape for a future, separately
authorized T4/T5 tranche to evaluate against negative proof.

## Source Verification

| Claimed item | Source file | Verified section/lines | Verified path or symbol | Disposition |
| --- | --- | --- | --- | --- |
| T3 objective is owner architecture and threat-model selection | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan, T3 row | `T3` | ACCEPT |
| T2 defines policy but selects no architecture owner | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS.md` | D1 Admission-owner and implementation gap | `OWNER_SURFACE_NOT_FOUND` | ACCEPT |
| D1-D6 policy text and GAP-01 through GAP-09 | same file | D1 through D6; Contradiction And Gap Ledger | `GAP-01` through `GAP-09` | ACCEPT |
| internal helpers remain autonomous until they cross a governed perimeter | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Agent Internal Autonomy And Invocation Perimeter | `INTERNAL_AGENT` | ACCEPT |
| launcher accepts a preflight receipt, resolves a governed workspace path, and starts/finalizes a durable execution record; does not claim external interception | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 168-186 (interfaces), 274-282 (`buildGovernedCommandAction`), 284-359 (`launchGovernedCommand`) | `launchGovernedCommand`; `externalInterceptionProved: false` | ACCEPT |
| preflight evaluates one action through the guard engine, persists a secret-safe audit entry, and fails closed on persistence failure; explicitly does not prove execution | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 181-283 (`preflightGovernanceAction`) | `preflightGovernanceAction`; `governedActionClaimAllowed` | ACCEPT |
| receipt-consumption store claims one receipt with create-exclusive file semantics; marker records no raw action content | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 36-80 (`JsonReceiptConsumptionStore.claimReceipt`) | `claimReceipt` | ACCEPT |
| governed execution store begins and finalizes a durable per-command execution receipt keyed by `consumptionId`, with `externalInterceptionProved: false` on the receipt shape itself | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | lines 1-65 (`GovernedExecutionReceipt`; `JsonGovernedExecutionStore`) | `beginExecution`; `finalizeExecution` | ACCEPT |
| session contract evaluates one action request against a registered agent, permission profile, and risk-ordered limits, and issues a deterministic-hash execution audit receipt; the request has no provider or process field, while the receipt has optional provider/model labels but no process or CLI/MCP identity and does not prove observed execution identity | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | lines 1-60 (`AgentGovernedActionRequest`); lines 141-174 (`AgentExecutionAuditReceipt`); lines 212-280 (`evaluateAction`); lines 322-384 (`createReceipt`) | `AgentGovernedSessionContract` | ACCEPT |
| provider router decides ALLOW/DENY/ESCALATE and selects one provider by policy; it explicitly does not call providers directly (doctrine-cited) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/provider.router.contract.ts` | lines 1-60 (doctrine comment; `ProviderSelection`); lines 140-160 (default/fallback selection) | `selectedProviderId` | ACCEPT |
| gateway execution bridge routes to one adapter, checks quota, executes, records health/quota, and builds one gateway receipt per call; no field represents a parent-assignment cumulative envelope across separate calls, no field represents an OS process or CLI/MCP session | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 59-77 (`ProviderExecutionBridge` construction); lines 78-224 (`execute`) | `ProviderExecutionBridge.execute` | ACCEPT |
| quota ledger tracks per-provider/per-model daily request and token counters only; no cross-retry, cross-fallback, or cross-child aggregation field exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | lines 1-75 (`QuotaUsage`; `QuotaLedger.canUse`) | `QuotaLedger` | ACCEPT |
| gateway receipt carries provider/model/decision/quota/credential-fingerprint fields; no task ID, invocation ID, or stop-state field exists on the receipt shape | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | lines 1-65 (`GatewayReceiptInput`; `GatewayReceipt`; `GatewayReceiptBuilder`) | `GatewayReceipt` | ACCEPT |

## Candidate Matrix

Common rubric applied to all four candidates: policy fit, process binding,
cumulative envelope, telemetry, stop completeness, receipt correlation,
provider neutrality, bypass resistance, internal-agent autonomy,
implementation surface, negative-proof feasibility.

| Rubric criterion | CANDIDATE-A (launcher-centric) | CANDIDATE-B (session-contract-centric) | CANDIDATE-C (Model-Gateway-centric) | CANDIDATE-D (new EAIC coordinator) |
| --- | --- | --- | --- | --- |
| Policy fit (D1-D4) | PARTIAL: launcher already gates one command behind a preflight receipt (D1-shaped), but the receipt is per-command, not per-assignment | PARTIAL: session contract already evaluates admission against a permission profile (D1-shaped), but has no process/provider fields to admit an external launch against | PARTIAL: gateway already fails closed on quota/credential/health (D4-shaped), but only for one provider call, not pre-launch usage | UNPROVEN_BY_SOURCE: no current source implements the coordinator; policy fit would be inherited by composition, not proven today |
| Process binding (D2) | PARTIAL: launcher owns `workspaceRoot`/`cwd` resolution and a child-process runner for registered profiles, but no field binds a CVF task/invocation ID to an OS process tree for an external agent | ABSENT: session contract has no process, PID, or OS-level field at all | ABSENT: gateway bridge calls an in-process adapter function, not an external process; no process-tree field exists | UNPROVEN_BY_SOURCE: would need a new binding mechanism; GAP-02/GAP-07 remain open regardless of which candidate is chosen |
| Cumulative envelope (D3) | ABSENT: launcher and its stores are scoped to one command's admission/execution lifecycle, not a parent assignment across retry/resume/fallback/children | ABSENT: session contract evaluates one action request per call; no envelope aggregation field | PARTIAL: quota ledger aggregates per-provider/per-model daily usage, but not per-parent-assignment across retry/fallback/children, and not across non-Gateway external launches | UNPROVEN_BY_SOURCE: composing existing stores does not by itself create a parent-envelope aggregator; this remains GAP-03 regardless of candidate |
| Telemetry (D4) | PARTIAL: execution receipt records exit code/signal/diagnostic per command; no pre-launch usage-availability field | ABSENT: no usage-telemetry field on the session contract | PARTIAL: quota ledger and health monitor expose request/token counts and health state, but only for Model-Gateway-mediated calls, not CLI/MCP host sessions | UNPROVEN_BY_SOURCE: GAP-04 (no source guarantees pre-launch usage telemetry for every host/plan) is a telemetry gap no candidate closes by architecture choice alone |
| Stop completeness (D5) | PARTIAL: launcher's runner has a timeout/kill path for the one child process it spawned, but no five-state (requested/acknowledged/stopping/stopped/unable-to-stop) model and no descendant-tree guarantee | ABSENT: session contract has no stop or cancellation concept | ABSENT: gateway bridge has no in-flight cancellation path for an adapter call already in progress | UNPROVEN_BY_SOURCE: the five-state model in T2 D5 has no current owner; this is GAP-06's implementation half |
| Receipt correlation (D6) | PARTIAL: launcher/execution-store receipts correlate `receiptId`/`consumptionId`/`bindingHash` for one command, but carry no provider/model or approved-vs-observed fields | PARTIAL: session-contract receipt correlates `sessionId`/`taskId`/`receiptId`/`traceId` and optional `providerName`/`modelName`, but has no process, envelope, or stop-state fields | PARTIAL: gateway receipt correlates `traceId`/provider/model/quota/credential fields, but has no CVF task ID, invocation ID, or stop-state field | UNPROVEN_BY_SOURCE: the full D6 field list (task ID, invocation ID, admission decision, identity binding, envelope charge, usage-availability, stop-state transitions, approved/observed provider-model, reconciliation state) exists nowhere as one schema today; GAP-08 |
| Provider neutrality | PASS: launcher has no provider-specific branch | PASS: session contract has optional free-text `providerName`/`modelName` fields only, no selection logic | AT_RISK_IF_STRETCHED: gateway bridge inherently selects/executes a provider; extending it to own CLI/MCP process lifecycle risks collapsing "which provider" with "which external process," which the baseline's Audit Finding explicitly warns against | PASS_BY_DESIGN: a composed coordinator can depend on the provider router's ALLOW/DENY/ESCALATE decision without owning provider execution itself |
| Bypass resistance | PARTIAL: only registered command profiles route through the launcher; any external agent launched outside this launcher is not mediated at all | ABSENT: session contract is a pure evaluation function; nothing calls it automatically before an external launch | PARTIAL: only Model-Gateway-routed provider calls are quota-checked; a CLI/MCP process spawned outside the Gateway is not mediated | UNPROVEN_BY_SOURCE: a new coordinator does not, by existing today, close the "nothing currently intercepts an arbitrary external launch" gap; GAP-01 and GAP-05 remain open under every candidate |
| Internal-agent autonomy | PRESERVED: launcher only governs explicit external command profiles it is invoked for; does not touch parent-session reasoning | PRESERVED: session contract only evaluates explicit action requests submitted to it | PRESERVED: gateway bridge only governs explicit provider-execution requests routed to it | PRESERVED_BY_DESIGN: composition over the same primitives does not add per-helper governance inside the parent session, consistent with the roadmap's Agent Internal Autonomy And Invocation Perimeter |
| Implementation surface if selected | SMALL_BUT_WRONG_SHAPE: extending the launcher to universal EAIC owner means adding parent-assignment, cross-command, and provider-session fields to a component whose contract is currently one-command-scoped | SMALL_BUT_WRONG_SHAPE: extending the session contract to own process/provider fields means adding responsibilities orthogonal to its current pure-evaluation contract | MEDIUM_BUT_BOUNDARY_RISK: extending the gateway bridge to own CLI/MCP process lifecycle means merging "provider execution owner" and "external process owner" into one component, contradicting the baseline's explicit warning against exactly that collapse | LARGEST_BUT_BOUNDARY_CLEAN: a new coordinator is the most implementation work (interface, storage, adapters, monitoring, stop, proof all need to be built), but each existing component keeps its current bounded contract |
| Negative-proof feasibility | FEASIBLE_FOR_NARROW_CLAIM: could prove "launcher denies/executes one registered command per its existing receipt contract," but cannot prove parent-envelope or cross-launch denial because those fields do not exist | FEASIBLE_FOR_NARROW_CLAIM: could prove "session contract denies one action request lacking a registered agent/profile," but cannot prove an external-launch admission decision because no caller wires it to a launch event | FEASIBLE_FOR_NARROW_CLAIM: could prove "gateway denies a provider call over quota," but cannot prove denial of an external CLI/MCP launch that never goes through the gateway | NOT_YET_FEASIBLE: no coordinator exists to test; T4 negative proof under this candidate would first require the T4/T5-authorized minimal build this packet does not authorize |

Overall candidate disposition: CANDIDATE-A, CANDIDATE-B, and CANDIDATE-C are
each `PROVEN_BOUNDED_COMPONENT, NOT_PROVEN_UNIVERSAL_OWNER`. CANDIDATE-D is
`ARCHITECTURALLY_PREFERRED, NOT_YET_IMPLEMENTED`. No candidate reaches
`PROVEN_COMPLETE_OWNER`; this is consistent with the baseline's Audit
Finding and does not by itself require `PARKED_KNOWLEDGE_GAP` or
`NOT_READY`, because the comparison itself is the T3 deliverable, not a
build claim (see Required Decision Packet Content item 10 in the paired
work order).

## Accountable-Owner Responsibility Map

One accountable coordination-accountability pattern (CANDIDATE-D, as
recommended) would compose the following responsibilities. Cells marked
`EXISTING_BOUNDED` name a current source component already proven for a
narrower scope; cells marked `PROPOSED_NEW` name a responsibility with no
current source and would require separate T4/T5 authorization to design and
build.

| Responsibility | Proposed accountable component | Current status |
| --- | --- | --- |
| Admission (D1 five-input deny rule) | new EAIC coordinator, consuming session-contract-style evaluation | PROPOSED_NEW; session contract's `evaluateAction` is the closest bounded analog (`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` lines 219-280) but has no process/envelope/usage fields |
| Identity issuance and binding (D2) | new EAIC coordinator, issuing task/invocation IDs and recording session/process identity when observed | PROPOSED_NEW; `AgentGovernedActionRequest.sessionId`/`taskId` (same file, lines 48-49) is the closest existing identifier pair, not a binding mechanism |
| Launch (external CLI/MCP process start) | new EAIC coordinator, delegating to an adapter modeled on the governed command launcher's child-process runner | PROPOSED_NEW; `launchGovernedCommand`'s runner (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` lines 168-186) is the closest bounded analog, scoped to one registered command profile, not an arbitrary external agent |
| Monitor (in-flight liveness/telemetry) | new EAIC coordinator | PROPOSED_NEW; no current source polls or streams state for an external CLI/MCP process |
| Cumulative usage (D3 envelope) | new EAIC coordinator, reading Model-Gateway quota ledger as one input among several | PROPOSED_NEW; `QuotaLedger` (`EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` lines 30-75) is a real per-provider/per-model input but not a parent-assignment aggregator |
| Stop (D5 five-state model) | new EAIC coordinator | PROPOSED_NEW; no current source implements the five-state model |
| Reconciliation (approved-vs-observed provider/model; D6 fields) | new EAIC coordinator | PROPOSED_NEW; `GatewayReceipt` (`EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` lines 26-49) carries `providerId`/`selectedModelId` but no `approvedProvider`/`observedProvider` reconciliation pair |
| Persistence (durable receipt/record store) | new EAIC coordinator, reusing store patterns from `JsonGovernedExecutionStore` and `JsonReceiptConsumptionStore` | EXISTING_BOUNDED pattern reusable; both stores are scoped to one command's lifecycle today (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` lines 42-48; `.../json-receipt-consumption.store.ts` lines 36-39) |
| Review (operator/reviewer readout of the above) | reviewer/closer and operator, through existing governed-artifact review conventions | EXISTING_BOUNDED; this is a documentation/process pattern, not a runtime component |

## D1-D6 And GAP-01 Through GAP-09 Coverage Matrix

| Decision or gap | T2 disposition | T3 architecture treatment |
| --- | --- | --- |
| D1 (pre-launch admission) | `REPLACE`, five-input deny rule | mapped to the proposed Admission responsibility above; no candidate today evaluates all five inputs together |
| D2 (identity layering) | `ACCEPT` | mapped to the proposed Identity responsibility above; existing `sessionId`/`taskId` fields are a partial building block, not a binding mechanism |
| D3 (cumulative envelope) | `ACCEPT` | mapped to the proposed Cumulative usage responsibility above; `QuotaLedger` is a bounded input, not the envelope owner |
| D4 (fail-closed unknown usage) | `ACCEPT` | mapped to the proposed Admission responsibility; gateway bridge's quota/credential/health fail-closed pattern (`ProviderExecutionBridge.execute`, lines 109-155) is the closest proven fail-closed shape but scoped to one provider call |
| D5 (stop-state mapping) | derived, policy-level only | mapped to the proposed Stop responsibility above; no runtime owner exists |
| D6 (receipt schema) | derived, documentation-level only | mapped to the proposed Reconciliation and Persistence responsibilities above; no single schema unifying all ten D6 fields exists in current source |
| GAP-01 (no admission-owner component) | open | remains open under every candidate; CANDIDATE-D names where this owner would live but does not create it |
| GAP-02 (no process-tree binding source) | open | remains open under every candidate; process binding is a `PROPOSED_NEW` responsibility above |
| GAP-03 (no cumulative-enforcement owner) | open | remains open; `QuotaLedger` narrows but does not close this gap, per Source Verification above |
| GAP-04 (no guaranteed pre-launch usage telemetry) | open | remains open; this is a telemetry gap, not an architecture-selection gap, and no candidate closes it by composition alone |
| GAP-05 (no runtime-enforcement proof) | open | remains open by definition; this packet performs no runtime action and proves nothing at runtime |
| GAP-06 (stop-state implementation owner) | open, policy-level mapping resolved in T2 | remains open; mapped to the proposed Stop responsibility above |
| GAP-07 (no EAIC-specific task/invocation ID issuance owner) | open | remains open; existing generic `sessionId`/`taskId`/`receiptId` fields are reused as building blocks, not as a closing mechanism |
| GAP-08 (no receipt store or correlation mechanism for the full D6 schema) | open | remains open; existing stores are reusable patterns, not the missing schema |
| GAP-09 (no `observedProvider`/`observedModel` telemetry field from the current worker execution surface) | open | remains open; `GatewayReceipt` exposes `providerId`/`selectedModelId` only for Gateway-routed calls, not for the worker's own host execution surface |

All nine gaps remain open after this packet. This packet closes none of
them; it only names where, architecturally, a future closing mechanism
would attach.

## Trust-Boundary And Data-Flow Sequence

Proposed sequence from an approved assignment to a final reconciled receipt,
under the recommended (not ratified) CANDIDATE-D shape. Every step past
"Approved assignment exists" is `PROPOSED_NEW` unless marked otherwise.

1. Approved assignment exists (a governed Work Order or equivalent
   authority record) - `EXISTING_BOUNDED` pattern (this very packet is one
   instance).
2. Trust boundary 1 - `ASSIGNMENT_TO_ADMISSION`: the coordinator reads the
   assignment and evaluates the D1 five inputs (assignment, envelope,
   identity plan, stop conditions, receipt target). `PROPOSED_NEW`.
3. Admission decision (admit or deny) is recorded with the specific absent
   input if denied. `PROPOSED_NEW`, D6-shaped.
4. Trust boundary 2 - `ADMISSION_TO_IDENTITY`: on admit, task/invocation IDs
   are issued. `PROPOSED_NEW`.
5. Trust boundary 3 - `IDENTITY_TO_LAUNCH`: the coordinator delegates to a
   launch adapter (conceptually similar to `launchGovernedCommand`, but for
   an arbitrary external agent rather than one registered command profile).
   `PROPOSED_NEW`.
6. Trust boundary 4 - `LAUNCH_TO_PROVIDER_SESSION`: when the external agent
   opens a provider session, that session/conversation identity is observed
   and bound to the CVF task/invocation ID pair when exposed, or recorded as
   explicitly absent when not. `PROPOSED_NEW`.
7. Trust boundary 5 - `PROVIDER_SESSION_TO_MONITOR`: the coordinator (or a
   delegated monitor) observes in-flight state; provider-native internal
   helpers inside that session remain autonomous and are not individually
   gated, per the Agent Internal Autonomy And Invocation Perimeter.
   `PROPOSED_NEW` for the monitor; the autonomy boundary itself is
   `EXISTING_BOUNDED` roadmap policy.
8. Trust boundary 6 - `MONITOR_TO_ENVELOPE`: observable usage (from
   Model-Gateway quota ledger when the call is Gateway-routed, or recorded
   as `UNKNOWN_NOT_EXPOSED` otherwise) is charged to the parent assignment's
   envelope. `PROPOSED_NEW` aggregation; `QuotaLedger` is an
   `EXISTING_BOUNDED` partial input.
9. Trust boundary 7 - `EVENT_TO_STOP_STATE`: a stop/cancel/completion event
   transitions through the five-state model (requested, acknowledged,
   stopping, stopped, unable-to-stop). `PROPOSED_NEW`.
10. Trust boundary 8 - `STOP_TO_RECONCILIATION`: approved-vs-observed
    provider/model, final usage state, and stop outcome are reconciled into
    one `MATCH`/`MISMATCH`/`UNKNOWN_NOT_EXPOSED` record. `PROPOSED_NEW`.
11. Final reconciled receipt is persisted (pattern reusable from
    `JsonGovernedExecutionStore`/`JsonReceiptConsumptionStore`, generalized
    beyond one command's lifecycle). `PROPOSED_NEW` schema over an
    `EXISTING_BOUNDED` storage pattern.

## Threat Model

| threatId | Threat | Mitigation | mitigationOwner | Evidence need | Residual gap |
| --- | --- | --- | --- | --- | --- |
| THREAT-01 | Spoofed assignment: a launch is initiated citing a Work Order or authority record that does not actually authorize it | admission step verifies the assignment record against the actual governed-artifact source, not a free-text claim | proposed EAIC coordinator (Admission) | negative-proof case: launch attempt citing a non-existent or mismatched assignment ID is denied | GAP-01: no current owner implements this check |
| THREAT-02 | Receipt replay: a previously issued admission or execution receipt is reused to justify a second launch or a second usage charge | one-time claim semantics, modeled on `JsonReceiptConsumptionStore.claimReceipt`'s create-exclusive file write (lines 73-80) | proposed EAIC coordinator (Persistence), reusing the existing claim-once pattern | negative-proof case: replaying a claimed receipt ID is rejected | GAP-08: no current schema extends this pattern to the full D6 receipt |
| THREAT-03 | Double consumption: usage from one external launch is charged to the envelope more than once (for example, once by a Gateway-routed sub-call and again by the coordinator's own monitor) | single source-of-truth envelope ledger with idempotent charge keys per observed event | proposed EAIC coordinator (Cumulative usage) | negative-proof case: replaying the same observed-usage event does not increase the envelope total | GAP-03: no current owner aggregates across sources at all, so double-counting cannot yet be tested |
| THREAT-04 | Launch bypass: an external agent is started through a path that does not go through the coordinator at all (shell, IDE task runner, ad hoc script) | none currently exists; this is an architecture-level open threat, not a mitigated one | `OWNER_SURFACE_NOT_FOUND` | negative-proof case: an out-of-band launch attempt is observed and denied or logged as a bypass | GAP-01 and GAP-05: no interception mechanism exists in any CVF-governed source examined by T1, R1B, or this packet |
| THREAT-05 | Process escape / descendant survival: a stopped or denied launch leaves child or descendant processes running | descendant-tree termination, modeled conceptually on the launcher's runner-level kill/timeout path but extended to process groups/job objects | proposed EAIC coordinator (Stop), informed by T1 findings on Windows Job Objects / POSIX process groups | negative-proof case: after a stop event reaches `stopped`, no descendant process from that launch remains running | GAP-02 and GAP-06: no source binds CVF identity to a process tree or implements the stop-state transitions |
| THREAT-06 | Provider-session mismatch: the provider/conversation session observed during monitoring does not match the session the coordinator believes it bound at launch | explicit binding check at Trust boundary 4; absence or mismatch is recorded, never silently accepted | proposed EAIC coordinator (Identity) | negative-proof case: a session-identity mismatch is recorded as `MISMATCH`, not silently treated as `MATCH` | GAP-02, GAP-07: no current binding mechanism exists to mismatch-check against |
| THREAT-07 | Approved-versus-observed provider/model mismatch | reconciliation field set to `MISMATCH` and surfaced, per T2's Provider/Model Assignment Reconciliation section | proposed EAIC coordinator (Reconciliation) | negative-proof case: launching with an approved provider/model different from the one actually observed produces a visible `MISMATCH`, not a silent pass | GAP-09: no current source exposes `observedProvider`/`observedModel` from the worker's own execution surface as a queryable field |
| THREAT-08 | Quota opacity: usage is unavailable, untrusted, or stale at admission time, but the launch proceeds anyway | D4 fail-closed rule: automatic/unattended launch is denied when usage is not reliably known | proposed EAIC coordinator (Admission), informed by `ProviderExecutionBridge`'s existing quota-check-then-deny pattern (lines 141-155) as a partial analog | negative-proof case: an automatic launch attempt with `UNKNOWN_NOT_EXPOSED` usage is denied, not admitted | GAP-04: no source guarantees machine-readable usage for every host/plan combination, so this remains a telemetry gap even after admission-policy is implemented |
| THREAT-09 | Retry/fallback budget evasion: a denied or failed launch is retried or falls back to another provider/model in a way that resets or evades the cumulative envelope | D3 rule: retry, resume, and fallback are charged to the same parent envelope, and D5 rule: a post-stop retry is a new launch subject to full D1 admission | proposed EAIC coordinator (Cumulative usage, Admission) | negative-proof case: a retry after denial is still charged against the original parent envelope and re-evaluated under D1, not silently re-admitted | GAP-03, GAP-06: no current owner enforces either rule |
| THREAT-10 | Cancellation failure: a stop/cancel request is accepted but the external process does not actually stop | five-state model requires `stopped` to reflect a verified external-process state, not merely an acknowledged request | proposed EAIC coordinator (Stop) | negative-proof case: after a `stopped` state is recorded, independent verification confirms the process is not running; a still-running process blocks the `stopped` transition | GAP-06: which component verifies "stopped" against the actual process is unspecified |
| THREAT-11 | Forged completion: an external agent or intermediary reports task completion without a correlated, durably persisted receipt | a completion claim without a D6-correlated receipt is not treated as a CVF receipt, per T2's D6 section | proposed EAIC coordinator (Persistence, Reconciliation) | negative-proof case: a completion message lacking a matching persisted receipt is rejected as unverified, not accepted at face value | GAP-08: no current store implements the full D6 correlation |
| THREAT-12 | Durable-store failure: the receipt/record store fails to persist (disk error, crash, concurrent write) and a launch or charge is claimed anyway | fail-closed persistence pattern, modeled on `preflightGovernanceAction`'s explicit `AUDIT_PERSISTENCE_FAILED` fail-closed branch (lines 239-263), which returns a denied/invalid result rather than a false-positive receipt | proposed EAIC coordinator (Persistence), reusing this proven fail-closed pattern | negative-proof case: a simulated persistence failure during admission or charge produces a denial or explicit failure state, never a silently accepted claim | GAP-08 remains: the fail-closed pattern is proven only for the bounded preflight store and is not yet bound to a full D6 coordinator schema |
| THREAT-13 | Over-governance of provider-native internal helpers: the coordinator or a reviewer treats an internal reasoning/exploration step inside an already-admitted parent session as if it required its own separate admission | explicit non-goal: internal helpers inherit parent scope and are not individually gated unless they independently cross a process/external-service/provider-account/credential/durable-action/scope/authority boundary, per the roadmap's Agent Internal Autonomy And Invocation Perimeter | operator and reviewer, enforcing the existing roadmap boundary during any future implementation review | negative-proof case: an internal helper that stays inside the parent session is not admission-gated, denied, or separately charged; only a helper that crosses the stated boundary is | none; this boundary is `EXISTING_BOUNDED` current CVF authority, not a new gap |

## Proposed Mitigations, Owners, Evidence Needs, And Residual Gaps

The Threat Model table above already carries `mitigationOwner`, evidence
need, and `residualGap` per row. Every `mitigationOwner` other than
`operator and reviewer` (THREAT-13) or `OWNER_SURFACE_NOT_FOUND`
(THREAT-04) is the same proposed EAIC coordinator named in the Bounded
Recommendation, consistent with the "one accountable pattern" requirement.
THREAT-04's `OWNER_SURFACE_NOT_FOUND` is preserved deliberately: no
candidate in the Candidate Matrix, including the recommended one, currently
intercepts an out-of-band launch, and this packet does not manufacture a
mitigation where none is source-backed.

## T4 Negative-Proof Plan

A future, separately authorized T4 tranche would need deterministic
pass/fail evidence for at least the following cases before any build
authorization could be considered evidence-based rather than aspirational.
Every row below is a proof the coordinator does not yet exist to run; this
plan defines what T4 must demonstrate, not a claim that it has been
demonstrated.

| Proof case | Setup | Expected fail-closed result | Evidence artifact | Deterministic verdict rule |
| --- | --- | --- | --- | --- |
| NP-01 admission denial on missing input | admit request with one of the five D1 inputs (assignment, envelope, identity plan, stop conditions, receipt target) deliberately absent | DENIED, naming the specific absent input | structured denial record citing the missing input | PASS only when every missing-input variant is denied with the correct reason; otherwise FAIL and T4 `NOT_READY` |
| NP-02 fail-closed on unknown usage | admit request where usage-availability state is `UNKNOWN_NOT_EXPOSED` and the launch is automatic/unattended | DENIED (fail-closed) | structured denial record with usage-availability state | PASS only on explicit denial before launch; otherwise FAIL and T4 `NOT_READY` |
| NP-03 launch bypass detection | an external agent process is started outside the coordinator's launch path | bypass is detected and recorded as unmediated before it can produce an accepted governed result | detection record; `NOT_DETECTED` is retained as failure evidence, never an acceptable result | PASS only when detected and rejected or quarantined; `NOT_DETECTED` is FAIL and forces T4 `NOT_READY` |
| NP-04 descendant survival after stop | a stop request reaches `stopped` for a launch with at least one descendant process | zero descendant processes from that launch remain running | process-tree enumeration before and after the stop event | PASS only when independent enumeration finds zero bound descendants; otherwise FAIL and T4 `NOT_READY` |
| NP-05 envelope double-charge resistance | the same observed-usage event is submitted to the envelope ledger twice | envelope total reflects the event exactly once | envelope ledger state before and after the duplicate submission | PASS only when the second submission changes no charged total; otherwise FAIL and T4 `NOT_READY` |
| NP-06 retry re-admission | a denied launch is retried | the retry is evaluated under full D1 admission again, not automatically re-admitted, and is charged to the same parent envelope if eventually admitted | admission decision record for the retry; envelope charge record | PASS only when both re-admission and parent-envelope continuity are proven; otherwise FAIL and T4 `NOT_READY` |
| NP-07 provider/model mismatch surfacing | approved provider/model differs from the value observed at execution | reconciliation state is recorded as `MISMATCH`, not silently resolved to either value | reconciliation record | PASS only on explicit `MISMATCH` with both values retained; otherwise FAIL and T4 `NOT_READY` |
| NP-08 persistence-failure fail-closed | the receipt/record store is made to fail during an admission or charge write | the operation returns denied/failed, never a false-positive success claim | operation result plus store-failure diagnostic | PASS only when no admitted/success receipt is emitted; otherwise FAIL and T4 `NOT_READY` |
| NP-09 internal-helper non-interference | a provider-native internal helper runs inside an already-admitted parent session without crossing the stated boundary | the helper is not separately admission-gated, denied, or charged | correlation scan proving no separate admission or charge record for that helper | PASS only when the trace contains the parent record and no child admission/charge record; otherwise FAIL and T4 `NOT_READY` |

T4 must return `NOT_READY` if any of NP-01 through NP-09 cannot be executed
deterministically once a candidate architecture is actually implemented, per
the roadmap's Roadmap Release Rules for T4.

## Operator Decision Row

| Field | Value |
| --- | --- |
| candidateId | CANDIDATE-D |
| accountableOwnerPattern | new EAIC coordinator composing existing launcher, session-contract, receipt/execution-store, and Model-Gateway primitives |
| operatorSelectionState | `ACCEPTED` |
| operatorDecisionDate | `2026-07-23` |
| operatorDecisionSource | explicit operator response `ok, accept` following independent T3 review |
| reviewer authority | reviewer may accept this packet as adequate evidence for operator review; reviewer acceptance does not itself ratify the owner |
| operator authority | operator accepted CANDIDATE-D as the architecture direction; this does not release T4 or implementation |

## Authorization Boundary Statement

Operator acceptance of CANDIDATE-D does not authorize build, invocation,
provider use, or moratorium lift. It selects the architecture direction only.
T4 and every implementation or external-action lane remain held pending fresh
operator authorization and a fresh source-verified work order.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Candidate Matrix and Responsibility Map | governed command launcher, session contract, Model Gateway bridge/quota/receipt sources | ENRICH_EXISTING | first side-by-side comparison of these four surfaces against one EAIC rubric | create this packet |
| Trust-boundary sequence and D6 schema mapping | T2 policy semantics (D6 field list) | ENRICH_EXISTING | first architecture-level sequencing of the D6 fields against concrete source components | no schema activation |
| Threat model and T4 negative-proof plan | none; no prior EAIC threat model exists in this roadmap | NEW_FINDING | first threat catalog and negative-proof plan for this control point | reviewer verifies threat/gap coverage |
| New EAIC coordinator interface | `OWNER_SURFACE_NOT_FOUND` | REJECT_DIRECT_IMPORT | no accepted mechanism; recommended only as a name for a future design, not built here | preserve as `PROPOSED_NEW` throughout; do not import or activate |

## Epistemic Process Block

### Expected Result / Prediction

A composed EAIC coordinator was expected to provide the cleanest
accountability boundary while existing launcher, session-contract,
store, and gateway components remain bounded collaborators rather than
being stretched into universal owners.

### Evidence Comparison

Direct source inspection of all four candidate surfaces (governed command
launcher, governance-action preflight, receipt-consumption store,
governed-execution store, agent-governed session contract, provider router,
provider-execution bridge, quota ledger, gateway receipt) confirmed that
each existing component is real and bounded, but none owns the external
process lifecycle, a cross-component cumulative envelope, or stop-state
supervision. This matches the prediction: composition over these primitives
is architecturally preferable to expanding any single existing component
past its current contract.

### Contradiction Or Gap Disposition

No candidate was found to already satisfy the full rubric, so no candidate
was downgraded from a false-positive complete-owner claim; the Candidate
Matrix records `PARTIAL`/`ABSENT`/`UNPROVEN_BY_SOURCE` per cell rather than
silently rounding up. CANDIDATE-C's Model-Gateway-centric option carries the
specific contradiction risk the baseline's Audit Finding warned about
(collapsing provider execution ownership with external process ownership);
this packet keeps that risk explicit in the Candidate Matrix and Trust
Boundary rows rather than resolving it by assumption. All nine T2 gaps
remain open and are re-confirmed, not re-derived, by the D1-D6/GAP coverage
matrix above.

### Claim Update

The prediction held: CANDIDATE-D is recommended as the least-overreaching
shape. This packet does not upgrade that recommendation into a ratified
owner, a proof of runtime capability, or a build authorization. The
conclusion is bounded to architecture comparison and threat-model
production, exactly as the paired work order's Purpose defines T3.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | authorized parent agent session | internal reasoning, exploration, decomposition, and context management remain autonomous within parent scope | EAIC-KR roadmap Agent Internal Autonomy And Invocation Perimeter | independent governance begins only when a helper crosses the external/process/provider/account/credential/durable-action boundary, per THREAT-13 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | proposed EAIC coordinator (not built) and existing launcher/session/gateway primitives it would compose | no invocation, provider/account use, process action, implementation, or live proof is authorized by this packet | Candidate Matrix and Responsibility Map above | this packet documents adapter needs only; a later, separately authorized roadmap owns any implementation | `DEFERRED_WITH_REASON` |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| worker output path existence | both required worker outputs were absent at authoring time, confirmed by Glob before writing | ACCEPT |
| current universal EAIC owner | no source-backed component cited in this packet is claimed to cover every D1-D6 row and every GAP-01 through GAP-09 row; the Candidate Matrix records `PARTIAL`/`ABSENT`/`UNPROVEN_BY_SOURCE`, never `PROVEN_COMPLETE_OWNER` | ACCEPT |
| proposed field collision | `candidateId`, `accountableOwnerPattern`, `componentRole`, `trustBoundary`, `threatId`, `mitigationOwner`, `residualGap`, `operatorSelectionState` are used only as doc-only fields in this packet, not claimed as existing runtime interfaces | ACCEPT |
| provider/model hard-code | no provider or model is chosen or defaulted anywhere in this packet | ACCEPT |
| internal helper overreach | THREAT-13 explicitly rejects gating internal helpers that stay inside the parent session | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON: this packet uses current repo-local governed sources and absorbs no new external material |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_invocation_control/` |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | external knowledge acquisition requires a separate operator-approved intake packet |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | one documentation-only architecture comparison, recommendation, threat model, and T4 negative-proof plan |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this packet |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | no agent CLI/MCP, provider, browser, network, or process invocation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, process-tree, wrapper, proxy, or runtime interception claim |
| claimLanguage | recommendation, proposed architecture, threat, mitigation, residual gap, and negative-proof need |
| forbiddenExpansion | runtime control, live proof, owner ratification, provider/model selection, cost claim, public claim, or moratorium lift |

## T3 Runtime Boundary Statement

This packet is `ARCHITECTURE_DIRECTION_OPERATOR_ACCEPTED_NO_BUILD_AUTHORITY`.
It does not implement, prove, or claim: an admission mechanism, an identity
binder, a cumulative-envelope enforcer, a usage meter, a stop-state
supervisor, a receipt store, or a provider/model observation mechanism for
the proposed EAIC coordinator. The global external-agent CLI/MCP invocation
moratorium remains fully in force. T4, T5, and all runtime/external-action
lanes remain parked pending separate operator authorization.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private architecture decision-support packet with no
public implementation or release evidence.

## Claim Boundary

This packet proves a source-traceable comparison of four candidate owner
architectures against one common rubric, records operator acceptance of
CANDIDATE-D, and defines a threat model with named mitigations, owners, and a
T4 negative-proof plan. It does not prove
architecture readiness, runtime enforcement capability, provider behavior,
or that any proposed mechanism exists. It does not instantiate an
implementation owner, authorize CLI/MCP/provider/API/account/network/
browser use, authorize source execution or process testing, lift the
invocation moratorium, or authorize public-sync, push, deployment, or
production action.
