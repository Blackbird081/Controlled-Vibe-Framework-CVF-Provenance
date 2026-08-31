# CVF GC-018 SCEC-T1 Semantic Convergence And Escalation Control Foundation Baseline

Memory class: governed-baseline

- Status: `READY_FOR_DISPATCH`
- Date: `2026-08-31`
- Execution base: `9bdc372a43f91be54a1302f6d1a1493ab1ad8793`
- Task ID: `SCEC-T1`
- Problem key: `cvf-semantic-convergence-and-escalation-control`
- Governing work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_2026-08-31.md`
- Commit authority: orchestrator/reviewer only
- Worker commit authority: none

## Purpose

Raise the CVF foundation so repeated semantic defects become machine-observable
progression constraints. The control must not inspect private reasoning, decide
semantic truth, or prescribe how an agent works. It must decide only whether a
problem chain has enough declared evidence to continue, must consolidate into
an integrated root contract, or must stop for architectural reassessment.

The first real acceptance case after this foundation closes is the parked
GC-010 successor T1J-R4. No GC-010 product/runtime tranche is opened by this
baseline.

## Root Problem

The current system contains strong structural and cost controls, but it does
not bind semantic progression to a stable problem identity, blocker-set
reconciliation, or claim-specific executable proof. In the GC-010 T1J chain:

1. T1J-R2 reduced the remainder to one connection-lifecycle gap.
2. Reviewer correction added missing payload/environment/policy requirements.
3. T1J-R3 then asserted two exactly-once mechanisms.
4. Reviewer correction rejected delete-as-single-winner and again expanded the
   production contract.

Each packet could satisfy its local document gates while the semantic problem
boundary continued to move. More narrow decision tranches would measure
document compliance, not convergence.

## Accepted Authority

| Authority | Accepted rule |
|---|---|
| `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | A repeated defect is a governance training sample and should progress from written rule to machine check to earliest applicable phase gate. |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Review-cost control governs dispatch economics and explicitly does not decide semantic truth. |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | New authority and checker work is elevated local governance work. |
| `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md` | A new guard requires registry-compatible, fail-closed, testable integration. |
| `governance/toolkit/05_OPERATION/CVF_GUARD_AUTHORING_STANDARD_GUARD.md` | Guard changes require explicit authorization, focused tests, negative fixtures, and phase placement. |
| `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Contract and implemented behavior must be separately declared for local and external surfaces. |

## Decision / Baseline

Dispatch one integrated governance implementation tranche. The worker must
deliver the canonical rule, machine checker, historical replay, earliest gate
bindings, scaffold defaults, tests, ADIF learning entry, and full return in one
bounded change set. GC-010 product work stays parked until this tranche closes.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Repeated defects must become rules, checks, then early gates | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | `Repeated Error Escalation`; ordered promotion rule | canonical document | learning philosophy | `ACCEPT` |
| Review-cost checker is not a semantic-quality scorer | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | claim boundary and machine-checkable limits | canonical document | review-cost standard | `ACCEPT` |
| R2 worker narrowed the remainder to connection lifecycle | `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` | worker findings | terminal and blocker statement | T1J-R2 worker return | `ACCEPT_AS_HISTORICAL_INPUT` |
| R2 reviewer expanded payload/policy requirements | `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` | reviewer correction | reviewer addendum | T1J-R2 reviewer | `ACCEPT_AS_REGRESSION_EVIDENCE` |
| R3 worker asserted two exactly-once mechanisms | `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` | worker evidence | exactly-once claim | T1J-R3 worker return | `ACCEPT_AS_HISTORICAL_INPUT` |
| R3 reviewer corrected the production contract again | `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` | reviewer correction | reviewer addendum | T1J-R3 reviewer | `ACCEPT_AS_REGRESSION_EVIDENCE` |
| Autorun catalog is the earliest shared dispatch gate carrier | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | command catalog | autorun gate | `ACCEPT` |
| Dispatch and worker-return scaffolds are default packet generators | `governance/compat/build_dispatch_packet_scaffold.py`; `governance/compat/build_worker_return_skeleton_scaffold.py`; `governance/compat/run_worker_return_scaffold.py` | build/main entry points | scaffold builders | packet scaffolding | `ACCEPT` |

## Semantic Convergence Control Seed

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "cvf-semantic-convergence-and-escalation-control",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [
      "SC-001_STRUCTURAL_GATES_DO_NOT_CONTROL_PROGRESSION",
      "SC-002_BLOCKER_SET_EXPANSION_NOT_ESCALATED",
      "SC-003_RUNTIME_CLAIMS_NOT_BOUND_TO_PROOF_CLASS",
      "SC-004_SCAFFOLDS_DO_NOT_EMIT_CONVERGENCE_STATE"
    ],
    "reopened": [],
    "current": [
      "SC-001_STRUCTURAL_GATES_DO_NOT_CONTROL_PROGRESSION",
      "SC-002_BLOCKER_SET_EXPANSION_NOT_ESCALATED",
      "SC-003_RUNTIME_CLAIMS_NOT_BOUND_TO_PROOF_CLASS",
      "SC-004_SCAFFOLDS_DO_NOT_EMIT_CONVERGENCE_STATE"
    ]
  },
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

This seed is the first dogfood instance. The worker must turn its contract into
a canonical standard, checker, tests, scaffold output, and early gate binding.

## Required Control Semantics

The implementation must establish all of these invariants:

1. `problemKey` is stable across a successor chain.
2. A successor names its predecessor path and SHA-256 content hash.
3. Blockers reconcile as sets: current equals retained plus new plus reopened;
   prior equals resolved plus retained, with declared sets pairwise valid.
4. Two partial-ready closures, one reviewer scope expansion, or a repeated
   correction of the same claim requires `ROOT_CONTRACT_REQUIRED`.
5. Two consecutive non-decreasing blocker transitions requires
   `STOP_REASSESS_ARCHITECTURE`.
6. Once escalation is required, a narrow successor is invalid.
7. Runtime-readiness claims cannot use documentation-only proof.
8. Concurrency, crash recovery, ordering, and schema compatibility claims map
   to named observable proof classes.
9. Historical unchanged packets remain valid; the rule applies forward from
   activation. Historical evidence may be replayed as a regression fixture.
10. The checker validates declared evidence shape, hashes, set algebra, and
    disposition. It does not infer semantic truth or inspect reasoning traces.

## Claim-To-Proof Minimums

| Claim class | Minimum proof class |
|---|---|
| `CONCURRENCY_EXACTLY_ONCE` | `EXECUTABLE_ADVERSARIAL_CONCURRENCY_TEST` |
| `CRASH_RECOVERY` | `EXECUTABLE_STATE_TRANSITION_CRASH_TEST` |
| `ORDERING` | `EXECUTABLE_SEQUENCE_ASSERTION` |
| `SCHEMA_COMPATIBILITY` | `EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST` |
| `DOCUMENTATION_ONLY` | `PROPOSAL_ONLY_NO_RUNTIME_READINESS` |
| `OTHER` | `NAMED_OBSERVABLE_PROOF` |

## Escalation Outcomes

Only these progression outcomes are permitted:

- `CONTINUE_BOUNDED`
- `ROOT_CONTRACT_REQUIRED`
- `STOP_REASSESS_ARCHITECTURE`
- `READY_WITH_EXECUTABLE_PROOF`

Only these successor scopes are permitted:

- `INITIAL_BOUNDED`
- `INTEGRATED_ROOT_CONTRACT`
- `NO_SUCCESSOR`
- `EXECUTABLE_IMPLEMENTATION`

There is deliberately no post-escalation narrow-gap token.

## Required Deliverable Families

The worker must deliver one integrated change set containing:

1. canonical SCEC standard and orientation routing;
2. fail-closed checker plus focused unit tests;
3. the GC-010 T1J-R1-through-R3 historical replay fixture;
4. autorun, reviewer-fast, pre-commit, and pre-push bindings;
5. dispatch and worker-return scaffold support;
6. scaffold regression tests and golden fixture update;
7. one ADIF entry recording this repeated failure class;
8. one full worker return packet.

## Acceptance Strategy

Foundation acceptance is not based on prose alone. It requires:

- a negative replay showing that the R2-to-R3 narrow continuation would be
  rejected once reviewer scope expansion is declared;
- positive and negative tests for every invariant above;
- proof that the checker appears exactly once in each required command catalog;
- proof that new scaffolds emit convergence state by default;
- all pre-existing gates still enabled and passing;
- no product/runtime, provider, live-run, deployment, or public-sync change.

After reviewer closure and orchestrator commit, GC-010 T1J-R4 becomes the first
live-use validation tranche. Its packet must use the new SCEC contract. If the
new control allows another unjustified narrow chain or fails to expose a
machine-observable defect, the next authorized action is to harden SCEC before
continuing GC-010.

## Evidence / Verification

Dispatch evidence consists of the source-verification ledger, historical
R2/R3 correction sequence, exact artifact manifest in the paired work order,
and successful pre-dispatch gates. Implementation evidence is deferred to the
worker return and must include executable negative replay plus independent
reviewer reruns.

## Dual Agent Surface Matrix

| Surface | Contract state | Implemented state | Evidence | Disposition | Owner |
|---|---|---|---|---|---|
| Local Codex dispatcher/reviewer | Baseline and work order define SCEC-T1 | No foundation implementation exists at dispatch time | this baseline and governing work order | `CONTRACT_ONLY` | orchestrator/reviewer |
| External Claude worker | Operator-mediated file transfer requires exact packet execution and local revalidation | No runtime adapter or hidden MCP transport is claimed | governing work order and future worker return | `CONTRACT_ONLY` | external worker under operator transfer |

## ADIF Defect Registry Disclosure

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`
- Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
- Applied entries: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`
- New planned learning entry: `ADIF-0055`
- Disposition: `APPLIED`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | `Status: READY_FOR_DISPATCH`; `Commit mode: WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Scaffold Provenance Block`; authorization tokens; route manifest fields; review-cost INITIAL sentinels |
| gateRunPurpose | Gates confirm the packet against checker rules already read; they are not the first discovery mechanism. |
| claimBoundary | Checker read-ahead proves structural preparation only, not future SCEC implementation or semantic correctness. |

## Scaffold Provenance Block

- scaffoldHelperCommand: `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id SCEC-T1 --title "Semantic Convergence And Escalation Control Foundation" --date 2026-08-31 --base 9bdc372a43f91be54a1302f6d1a1493ab1ad8793 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --include-worker-return-skeleton --stdout`
- generatedProfile: `protected-governance-path`
- generatedSkeletonStatus: `GENERATED_BUT_REPLACED`
- manualEditsAfterScaffold: `YES - replaced generic skeleton with the bounded SCEC-T1 authority, manifests, proof model, and self-protection scope`
- checkerReadAheadConfirmation: `COMPLETE`
- docOnlyNewFields: `semantic convergence seed is contract-only until the worker implements the checker and scaffolds`
- claimBoundary: `dispatch authority only; no implemented SCEC or GC-010 runtime readiness claim`

## Claim Boundary

This baseline authorizes a governance foundation implementation packet. It does
not claim that SCEC is implemented, that semantic truth can be automatically
scored, that GC-010 is production ready, or that any provider/live/deployment
path exists. No successor product tranche is opened here.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is private provenance dispatch authority, not a closed public
catalog artifact.
