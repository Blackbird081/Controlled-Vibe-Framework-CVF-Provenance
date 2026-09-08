# CVF WP-ARCH-003 RABA F01-F02 Root Evidence Reassessment Roadmap

Memory class: governed-roadmap

Status: OPERATOR_AUTHORIZED_EXTERNAL_RELAY_READY

docType: roadmap

Date: 2026-09-08

Roadmap ID: WP-ARCH-003-RABA-F01-F02

Material base HEAD: `75b73edac5c914f9cef3e2be0f22e49cc7b04e2a`

## Authorization / Decision

The operator authorized handling the two RABA-T0 reviewer findings before any
broader reassessment or repository-absorption topic. This is a new bounded
finding-reconciliation parent. It is not a RABA-T0 redispatch, does not reset
the exhausted RABA-T0 budget, and authorizes only one fresh external evidence
invocation after manual operator relay.

Decision: `PROCEED_TO_RABA_F01_F02_EXTERNAL_RELAY`

The paired GC-018 baseline and work order are released with this roadmap for
manual operator relay. The worker may change only the two new evidence outputs.

## Purpose

Determine whether CVF has, or can truthfully designate, a trusted root for:

1. approval of authority expansion; and
2. principal-to-task-to-file-scope binding consumed by a real runtime path.

The roadmap replaces proposal-first repair with evidence-first ownership. It
must stop when a trustworthy producer, verifier, composition root, or non-test
consumer cannot be named from current source.

## Two Finding Contract

| Finding | Required correction | Acceptance boundary |
|---|---|---|
| `WP-ARCH-003-RABA-T0-R1-01` | classify Web approval, provider execution grant, delegation and mutating-profile approval candidates in the exact source ledger, owner matrix and rejected-alternative analysis | every candidate has producer, verifier, current consumer, broken edges and one evidence disposition; no broad absence claim exceeds the search |
| `WP-ARCH-003-RABA-T0-R1-02` | produce a machine-parseable operation trace with literal repository-local paths and truthful gate-cause attribution | `Expected manifest` and `Actual changed set` each list the exact two new paths; the final mandatory gate passes in the isolated active worker view |

Finding R1-03 is not a third repair item. It is the retained fail-closed safety
outcome if the reassessment still cannot source the integrated trust chain.

## Scope

In scope:

- current authority-envelope, task-graph and role-resolution contracts;
- the current guard request context and guard composition root;
- the current MCP evaluation entrypoint;
- current delegated-write boundary behavior;
- trusted approval provenance, principal identity, task identity, scope
  binding, expiry/replay handling and fail-closed omission behavior;
- one exact producer-to-verifier-to-runtime-consumer map;
- a conditional decision on whether a fresh WP-ARCH-003 design may later open.

The accepted bounded consumer correction for `ARCH-ABS-021` is reused as
evidence and is not re-reviewed unless a named contradiction appears.

## Non-Goals

- No implementation or test mutation.
- No edit, repair, acceptance or commit of rejected AR1 or RABA-T0 worker artifacts.
- No `AR1-R2`, third same-parent invocation, or implicit budget reset.
- No new guard, receipt, database, service, adapter, registry row or runtime
  wiring.
- No DARA-T5, MFRP mutation, credential use, provider call, public sync,
  deployment or production action.
- No claim that an integrity hash proves who approved an authority change.
- No optional caller field may be treated as trusted identity or scope.

## Evidence Baseline

| Evidence | Current fact admitted by this roadmap | Disposition |
|---|---|---|
| `docs/reviews/CVF_WP_ARCH_003_AR1_R1_CANONICAL_OWNER_RUNTIME_PATH_DESIGN_REWORK_COMPLETION_2026-09-08.md` - Risk / Corrective Action and Decision / Disposition | AR1 R1 is terminally rejected; the remaining root defects concern trusted approval provenance, principal/scope binding and exact manifest reconciliation | ACCEPT_CURRENT_AUTHORITY |
| `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` - WP-ARCH-003 Interlock | implementation requires reviewer-owned accepted architecture and a complete producer-to-runtime-consumer path | ACCEPT_CURRENT_AUTHORITY |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` - `MaoAuthorityEnvelopeInput`, `buildAuthorityEnvelope`, `verifyAuthorityEnvelope` | approval checkpoints are input data covered by a deterministic content hash; current source does not identify an approving issuer | ACCEPT_CURRENT_SOURCE |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` - `MaoRoleResolutionReceipt`, `resolveRole` | the receipt binds its decision to a task graph but currently carries no principal-to-task scope proof | ACCEPT_CURRENT_SOURCE |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` - `GuardRequestContext` | the universal guard input carries caller-facing role, agent and target-file data but no trusted upstream scope receipt | ACCEPT_CURRENT_SOURCE |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` - `buildContext`, `cvf_evaluate_full` | the runtime entrypoint constructs guard context from tool arguments and calls the guard engine | ACCEPT_CURRENT_SOURCE |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts` - `evaluateDelegatedWriteBoundary` | current delegated-write evaluation is deny-by-default outside declared ownership, but it does not authorize authority expansion | ACCEPT_CURRENT_SOURCE |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` and `src/app/api/execute/route.ts` | authenticated admin decision and actor/hash/expiry/status/one-use consumption are current candidates, not proof of the complete RABA chain | ACCEPT_CURRENT_CANDIDATE |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` - `ProviderExecutionGrant` and `DelegationContract` | current provider-budget/expiry and parent-task/file-scope fields must be classified with their trust-source and consumer gaps | ACCEPT_CURRENT_CANDIDATE |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` and governed launcher | fixed action/target approval and expiry are current candidates; caller-supplied `approvedBy` must not be treated as authenticated issuer proof | ACCEPT_CURRENT_CANDIDATE |

The source set is bounded and named. This roadmap makes no repository-wide
completeness claim.

## Root Questions

RABA-F01-F02 must answer all of these from current source evidence:

| ID | Question | Required evidence | Fail-closed outcome |
|---|---|---|---|
| RABA-Q01 | Who is permitted to approve authority expansion? | exact producer symbol or governed owner, issuer identity class and higher-authority relation | `PARK_NO_TRUTHFUL_APPROVAL_ISSUER` |
| RABA-Q02 | What exactly was approved? | bound subject, parent authority, requested delta, action/resource scope, budget and decision | `PARK_UNBOUND_APPROVAL` |
| RABA-Q03 | How is approval authenticity and freshness checked? | verifier, immutable receipt reference, expiry or sequence and replay/forgery rejection | `PARK_UNVERIFIABLE_APPROVAL` |
| RABA-Q04 | How is a principal bound to one task and file scope? | trusted producer, principal ID, task graph ID, task ID, scope and receipt hash/ID | `PARK_SELF_ATTESTED_SCOPE` |
| RABA-Q05 | Where is that binding consumed? | exact non-test entrypoint, composition root, guard invocation and downstream action decision | `PARK_NO_RUNTIME_CONSUMER` |
| RABA-Q06 | Who owns each contract? | one canonical package/symbol owner and rejected-alternative rationale | `PARK_AMBIGUOUS_OWNER` |

An input field supplied by the same caller requesting permission is evidence
of a request, not proof of identity, approval or owned scope.

## Target Trust Chain

The future design may proceed only if T0 can source every edge below:

`authority issuer -> approval receipt -> receipt verifier -> task/principal scope binding -> guard composition -> runtime action decision`

Required invariants:

- issuer authority is strictly above the requested delta;
- approval binds subject, action, resource, scope, budget and parent authority;
- principal scope comes from a verified task/admission artifact, not a request
  argument;
- missing, malformed, expired, replayed, forged or mismatched evidence denies;
- omission cannot preserve the old allow path for an action that requires the
  new proof;
- a content hash supplies integrity only and is never promoted to approval
  provenance;
- there is exactly one owner and one real composition path for each decision.

## Design Control Gate

Lifecycle state remains `DESIGN_REASSESSMENT`. RABA-F01-F02 is evidence and owner
selection only.

| Gate | Pass condition | Failure action |
|---|---|---|
| DC-01 New-parent boundary | packet identity is RABA-F01-F02 and does not cite AR1 as its parent assignment | stop and correct dispatch identity |
| DC-02 Approval root | Q01-Q03 have current, non-circular source evidence | park authority-expansion design |
| DC-03 Principal scope root | Q04 has a non-self-attested producer and exact binding | park principal-scope design |
| DC-04 Runtime composition | Q05 names a real current consumer or a separately justified runtime owner | park; do not create a contract-only orphan |
| DC-05 Owner uniqueness | Q06 selects one owner per responsibility without duplicate behavior | return to root owner selection |
| DC-06 Fail-closed semantics | omission, mismatch, forgery, expiry and replay all have DENY outcomes | return to integrated contract design |
| DC-07 Evidence reconciliation | matrix, narrative and future manifest use the same paths and symbols | return to design |

## Work Plan

| Tranche | Work | Output | Terminal decision |
|---|---|---|---|
| RABA-F01-F02 | verify current authority producers, identity/scope producers, verifiers, composition roots and non-test consumers | governed assessment, exact source ledger, owner decision and worker return under a fresh GC-018/work order | `PROCEED_TO_INTEGRATED_ROOT_CONTRACT_DESIGN` or `PARK_NO_TRUTHFUL_AUTHORITY_ROOT` |
| RABA-T1 | conditionally design one integrated approval-and-principal-scope root contract | closed architecture matrix, trust-boundary record, rejected alternatives and exact future manifest | `PROCEED_TO_RUNTIME_COMPOSITION_DESIGN` or `RETURN_TO_ROOT_ARCHITECTURE` |
| RABA-T2 | conditionally prove the proposed composition and adversarial denial matrix at design level | producer-to-consumer map, bypass matrix, rollback plan and implementation entry criteria | `PROCEED_TO_FRESH_WP_ARCH_003_DESIGN` or `PARK_ARCHITECTURE` |
| RABA-T3 | independent review and reopen decision | reviewer disposition and continuity update | `WP_ARCH_003_FRESH_DESIGN_ALLOWED` or `WP_ARCH_003_RETAIN_PARKED` |

Each tranche requires its own source-verified packet. No later tranche opens
automatically from worker self-report.

## Invocation And Review Budget

- AR1 same-parent usage remains exhausted at 2/2 and is historical evidence
  only.
- This roadmap authoring consumes zero delegated-worker invocations.
- A future RABA-F01-F02 work order must declare a fresh parent assignment, a finite
  cumulative ceiling and the exact operator relay checkpoint before execution.
- A third turn on any RABA parent cannot auto-dispatch; root reassessment or an
  operator decision is required.
- Reviewer work consumes returned evidence and does not recreate worker
  implementation or rerun broad proof without a named contradiction and
  expected information gain.

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority / risk boundary | Required evidence | Adapter boundary / disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | orchestrator/reviewer, dispatch author, closer | local governed files and local gates | may author and review roadmap/T0 packets; may not execute implementation | committed roadmap, source verification, gate receipts and separate continuity sync | `ALLOWED_LOCAL_GOVERNED_AUTHORING` |
| `EXTERNAL_AGENT_CLI_MCP` | future bounded worker | operator-relayed packet only | zero authority from this roadmap; no call until a fresh T0 work order and operator checkpoint | execution base, exact manifest, invocation counter, unstaged no-commit return | `PARKED_PENDING_FRESH_DISPATCH` |
| adapter boundary | none active | no direct adapter or provider route | cannot infer authority from manual transfer or returned prose | governed packet plus independent review | `NO_RUNTIME_ADAPTER_AUTHORIZED` |

## Acceptance Criteria

RABA-F01-F02 is acceptable only when:

1. all six Root Questions have exact source-backed answers or an explicit park
   outcome;
2. approval provenance is distinct from content integrity;
3. principal/task/scope binding cannot be supplied or omitted by the permission
   requester to bypass enforcement;
4. the complete current or proposed consumer chain is named without claiming
   absent symbols as current;
5. one canonical owner is selected for every responsibility;
6. missing/invalid/stale/replayed/forged/mismatched cases are fail-closed;
7. the accepted ARCH-ABS-021 correction is reused without duplicate review;
8. the exact future manifest equals the union of proposed matrix paths;
9. no source, test, runtime or external effect is introduced; and
10. the terminal decision is exactly one of the two RABA-F01-F02 outcomes.

## Verification And Evidence Plan

- Directly read every named current source and record symbol-level evidence.
- Use bounded `rg` queries to locate every producer, verifier, export,
  composition site and non-test consumer for the selected symbols.
- Separate current symbols from proposed symbols in the architecture matrix.
- Recompute any manifest/path-set digest with an explicit UTF-8, LF,
  forward-slash, ordinal-sort and trailing-LF recipe.
- Run the roadmap and dispatch-phase governance gates as confirmation evidence,
  not as first discovery of required artifact shape.
- Independent review decides semantic sufficiency; structural PASS alone cannot
  establish a trustworthy authority root.

## Stop Conditions

Stop and park the roadmap when any of these is true:

- no truthful higher-authority issuer exists in the current architecture;
- the only approval evidence is caller-populated data plus its integrity hash;
- the only principal/scope evidence originates from the permission request;
- no runtime consumer exists and no governed owner accepts responsibility for
  one;
- ownership requires duplicate evaluators across packages;
- the proposed guard remains optional for actions it claims to protect;
- the source ledger and future manifest cannot reconcile exactly.

## Epistemic Process Block

### Expected Result / Prediction

Current source will either expose one defensible authority root and runtime
chain, or prove that WP-ARCH-003 must remain parked before another design call.

### Evidence Comparison

AR1 R1 demonstrated that integrity hashing and caller-carried fields are
insufficient substitutes for approval provenance and trusted scope binding.
Current source reads confirm those missing semantics while preserving the
bounded ARCH-ABS-021 consumer correction.

### Contradiction Or Gap Disposition

The contradiction is architectural, not a missing prose row: an approval list
can be integrity-protected without proving the approver, and a scope list can
be transported without proving the principal/task binding. RABA-F01-F02 must find a
trusted source or terminate `PARK_NO_TRUTHFUL_AUTHORITY_ROOT`.

### Claim Update

The prior claim that AR1 could be repaired within the same design parent is
withdrawn. The supported claim is narrower: only a fresh root-authority
reassessment may decide whether a new WP-ARCH-003 design is viable.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | roadmap Authorization, Purpose, Scope, Non-Goals, Design Control Gate, Work Plan, Acceptance Criteria, Verification, top Status, checker fields, trace labels, public disposition and Claim Boundary |
| gateRunPurpose | confirmation evidence for the source-read roadmap shape and boundary; not first discovery |
| claimBoundary | checker PASS cannot prove a truthful authority issuer, accept a future root contract, open RABA-T1 or authorize execution |

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: only local CVF-governed evidence and current
repository source are used. No third-party repository or copied corpus is in
scope.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this is a bounded named-source architecture
reassessment and makes no corpus-completeness or source-absorption claim.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/reviewer and roadmap author |
| Provider or surface | local private CVF workspace |
| Session or invocation | WP-ARCH-003-RABA-F01-F02 roadmap authoring, 2026-09-08 |
| Working directory | repository root at `75b73edac5c914f9cef3e2be0f22e49cc7b04e2a` |
| Command or tool surface | progressive governed reads, bounded source inspection, `rg`, `apply_patch`, governance gates and git |
| Target paths | `docs/roadmaps/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_ROADMAP_2026-09-08.md`; `docs/baselines/CVF_GC018_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md` |
| Allowed scope source | operator instruction to handle the two findings first on 2026-09-08 |
| Before status evidence | committed continuity at `75b73edac5c914f9cef3e2be0f22e49cc7b04e2a`; four rejected worker artifacts present; staging empty |
| After status evidence | three new dispatch packet artifacts; rejected artifacts preserved byte-exact outside the active repository view; no worker execution or external effect |
| Diff evidence | `git status --short`; `git diff --check`; roadmap structural, reviewer-fast and pre-commit gates |
| Approval boundary | RABA-F01-F02 packet materialization and manual relay release only |
| Claim boundary | no RABA worker execution, architecture acceptance, WP implementation, DARA-T5, provider/live/public/deploy claim |
| Agent type | orchestrator/reviewer |
| Invocation ID | `wp-arch-003-raba-f01-f02-roadmap-authoring-2026-09-08` |
| Expected manifest | `docs/roadmaps/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_ROADMAP_2026-09-08.md`; `docs/baselines/CVF_GC018_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md` |
| Actual changed set | `docs/roadmaps/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_ROADMAP_2026-09-08.md`; `docs/baselines/CVF_GC018_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private architecture reassessment roadmap; no public-sync batch is
authorized.

## Next Allowed Move

Relay only the committed RABA-F01-F02 baseline and work order to the external
worker. The manual relay consumes the fresh parent invocation count 1/1.
RABA-T1, fresh WP-ARCH-003 design, implementation, DARA-T5 and external effects
remain parked pending independent reviewer acceptance.

## Claim Boundary

This roadmap authorizes the RABA-F01-F02 packet and one manual relay only. It records no accepted root
authority design, no principal-scope implementation, no runtime behavior, no
provider or credential use, no public export, no deployment and no production
readiness. The rejected AR1 artifacts remain evidence, not active design
authority.
