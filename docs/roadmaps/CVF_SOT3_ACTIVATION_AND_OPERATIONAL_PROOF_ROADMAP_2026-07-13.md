# CVF SOT3 Activation And Operational Proof Roadmap

Memory class: FULL_RECORD

Status: A3_CLOSED_PASS_BOUNDED_A4_PACKET_NEXT

docType: roadmap

Roadmap ID: SOT3-ACT

Date: 2026-07-13

## Purpose

Activate SOT3 in one bounded CVF product path and produce the local, durable,
failure-boundary, and real-provider evidence needed for the exact claim
`LIVE_GOVERNANCE_PROVEN_BOUNDED`.

After that claim this roadmap stops. User feedback, field value, production
scale, and post-shipment learning belong to a later product-validation lane.

## Authority And Starting State

- Operator instruction on 2026-07-13 authorizes A0 first and design of A1-A5.
- SOT3 absorption and package implementation are closed boundedly.
- T8 packet binding closed at material commit `0ffede4f1`.
- Session closure was recorded at `2628213b7`.
- Current honest claim: `DURABLE_EVIDENCE_REPLAY_PROVEN_LOCAL`.
- Activation, persistence, provider/live, and public work were outside the
  absorption lane and require fresh tranche authorization here.

## Authorization / Decision

The operator authorized A0 architecture work and A1-A5 design on 2026-07-13.
A0 is accepted boundedly by this roadmap. Runtime implementation remains
unauthorized until each tranche receives its own GC-018 and source-verified
work order with fresh dependency-release evidence.

## Scope / Target / Owner Boundary

Target: one controlled knowledge-context path in CVF Web, from tenant-scoped
retrieval through SOT3 approval and durable evidence to a real provider call.

Owner boundary: existing retrieval owns tenant filtering; Refinery owns
deterministic source preparation; Kernel owns truth evaluation and reference
issuance; Flow owns scoped distribution lifecycle; CVF Web owns the product
adapter and provider invocation. No layer may absorb another layer's authority.

## A0 Architecture Decision

Canonical decision:
`docs/reference/sot_three_layer/CVF_SOT3_ACTIVATION_ARCHITECTURE_DECISION.md`

A0 selects scoped knowledge context in `/api/execute` after tenant-aware
retrieval and before `buildKnowledgeSystemPrompt` and `executeAI`.

A0 disposition: `A0_PASS_BOUNDED`

## Target Architecture

```text
scoped knowledge chunks
        |
        v
SOT3 product adapter
        |
        +-- Refinery: deterministic source preparation
        +-- Kernel: evidence decision, receipt, active reference
        +-- Flow: scoped delivery, consumption, acknowledgement
        |
        v
approved context + durable evidence projection
        |
        v
/api/execute -> real provider -> governed response
```

The provider is downstream of Truth Flow. It cannot create, approve, mutate,
or supersede truth state.

## Design Control Gate

| Control | Roadmap decision |
|---|---|
| Scope boundary | one controlled knowledge collection and one representative execute scenario |
| Non-goals | no universal SOT3 runtime, prompt truth classification, provider-output authority, or public export |
| Lane split | A0 architecture; A1 adapter; A2 persistence; A3 live happy path; A4 failure/recovery; A5 release proof |
| Dependency plan | each tranche needs accepted predecessor closure evidence before dispatch |
| Source verification | every packet verifies current route, package, store, test, and release symbols |
| Claim boundary | final claim is bounded to the selected path, scenario, provider lane, environment, and evidence window |
| Acceptance evidence | local tests, durable replay, provider evidence, zero-call rejection evidence, release manifest |
| Dispatch readiness | A1 closed boundedly; A2 requires fresh GC-018 and a source-verified work order |

## Tranche Plan

| Tranche | Objective | Required output | Release condition |
|---|---|---|---|
| A0 | select and source-verify activation architecture | decision, owner map, seam, modes, claim ladder, cost control | decision records `A0_PASS_BOUNDED` |
| A1 | wire a route-size-safe knowledge adapter | adapter, dependencies, activation modes, audit projection, local tests | `OFF` preserves behavior and `ENFORCE` never injects rejected raw chunks |
| A2 | make evidence durable and replayable | atomic store, schema/version, lookup, restart and corruption tests | full identifier chain resolves after process restart |
| A3 | prove enforce-mode happy path with a real provider | controlled fixture, live test, diagnostic, correlated receipt | provider consumes only Flow-approved context |
| A4 | prove failure and recovery boundaries | invalid/stale/cross-packet/revoked cases, restart, duplicate, rollback | rejected context never reaches provider; recovery is bounded |
| A5 | add release-quality proof and close claim | release-runner wiring, bundle execution, manifest, completion review | canonical release command passes with SOT3 evidence |

## A1 Detailed Design

A1 must:

- add direct private file dependencies from CVF Web to the three SOT3 owner
  packages after package-resolution verification;
- create a focused adapter module instead of adding lifecycle logic to
  `route.ts`;
- preserve collection, chunk, organization, and team identity;
- use public APIs from Refinery, Kernel, and Flow;
- keep the existing tenant scope filter upstream and authoritative;
- expose `OFF`, `SHADOW`, and `ENFORCE`, with `OFF` as initial default;
- emit explicit outcomes for no chunks, accepted chunks, and rejected chunks;
- add only a thin execute-route invocation and evidence projection;
- preserve current behavior in `OFF` and forbid raw fallback in `ENFORCE`;
- run package tests, adapter and route tests, TypeScript check, build, and
  governed file-size enforcement.

A1 must not use the scenario-shaped vertical-slice orchestrator as product
policy owner. Provisional risk is R2 because provider input construction
changes; the fresh A1 GC-018 controls the final classification.

## A2 Detailed Design

A2 defines a dedicated SOT3 activation evidence record correlating:

- request and actor scope;
- source collection and chunk identifiers;
- Refinery packet identifier and content hash;
- Kernel decision, receipt, reference, policy, and rule versions;
- Flow package, recipient scope, lifecycle state, and acknowledgement;
- activation mode, outcome, timestamps, and diagnostic class;
- schema version and integrity projection for replay checks.

The first bounded proof may follow the existing atomic local-file pattern. It
must not silently swallow persistence failure. A2 proves restart lookup,
duplicate handling, corrupt-file behavior, and partial-write safety. A database
or distributed ledger is not required. Provisional risk: R2.

## A3 Detailed Design

A3 uses a real DashScope-compatible provider key through the existing
secret-safe environment bootstrap. The controlled scenario must:

1. retrieve scoped chunks from one collection;
2. reach `READY_FOR_KERNEL`;
3. receive an eligible receipt and active reference;
4. create, deliver, consume, and acknowledge a Flow package;
5. inject exactly the approved context in `ENFORCE`;
6. complete one provider response;
7. correlate provider evidence with the persisted SOT3 record.

Call budget: one planned call and one diagnostic-gated retry. Output quality is
not tuned or scored in this lane. Provisional risk: R2 live proof.

## A4 Detailed Design

A4 must cover:

- empty and structurally invalid source input;
- evidence bound to the wrong packet;
- expired, recalled, retired, or inactive reference;
- wrong recipient, role, phase, task, dose, or expiry;
- duplicate request and replay attempt;
- evidence-store restart and valid recovery;
- corrupt or partial store write;
- rollback from `ENFORCE` to `OFF`.

Cases that reject before provider execution must assert zero provider calls.
A4 uses operator-unmetered Alibaba calls only after local negative proof. A
failed or unclear live attempt requires a secret-safe diagnostic and a
result-changing action before retry; diminishing-return controls remain
binding. Provisional risk: R2.

## A5 Detailed Design

A5 extends the canonical release-quality gate so SOT3 live proof is required,
then runs:

```text
python scripts/run_cvf_release_gate_bundle.py --json
```

The run must use a real provider key, include SOT3 in JSON and the live evidence
manifest, and fail if SOT3 proof is absent, skipped, mocked, or not correlated
with durable evidence.

The final review may state `LIVE_GOVERNANCE_PROVEN_BOUNDED` only after A1-A5
closure evidence is accepted and the canonical release command passes.
Provisional risk: R2 release-quality proof.

## Roadmap-To-Future-Work-Order Trace Matrix

| Requirement | Future packet | Mandatory proof |
|---|---|---|
| adapter and activation modes | A1 | source verification, tests, route-size evidence |
| no raw fallback in enforce mode | A1 | rejection test shows knowledge block absent |
| durable replayable evidence | A2 | restart, duplicate, corruption, atomic-write tests |
| real-provider approved-context path | A3 | live receipt correlated to SOT3 identifiers |
| zero-call negative boundary and recovery | A4 | provider call-count evidence and recovery receipt |
| canonical release inclusion | A5 | release JSON and live evidence manifest |
| final exact claim | A5 review | reviewer disposition and claim-boundary table |

## Dependency Release Discipline

- A1 stays unready until its GC-018 and source-verified work order pass.
- A2 requires the A1 completion review and closure commit.
- A3 requires A2 durable restart evidence.
- A4 requires accepted A3 live evidence and diagnostics.
- A5 requires accepted A4 failure and recovery evidence.
- No worker may infer release evidence from chat or provider-local memory.

## Work Plan

1. Preserve the ratified A0 seam and claim ladder.
2. Author and review the A1 GC-018 and work order before runtime edits.
3. Close A1 locally before opening durable evidence work in A2.
4. Close A2 restart and integrity proof before spending provider quota.
5. Execute A3 through the runner-only permit with diagnostic discipline.
6. Prove A4 rejection and recovery boundaries, favoring zero-call negatives.
7. Add A5 to the canonical release bundle, run it once, and independently
   review the exact bounded claim.

## Acceptance Criteria

- AC-01: A0 selects one bounded seam without runtime or provider mutation.
- AC-02: A1 keeps SOT3 lifecycle logic out of the near-limit execute route.
- AC-03: `OFF` preserves pre-activation behavior.
- AC-04: `ENFORCE` cannot inject raw chunks after SOT3 rejection.
- AC-05: Refinery retains no AI, agent, prompt, or provider responsibility.
- AC-06: provider remains a downstream Flow consumer.
- AC-07: A2 evidence survives restart and detects corrupt or partial state.
- AC-08: A3 correlates a real provider result to the approved context and full
  SOT3 identifier chain.
- AC-09: A4 expected rejections prove zero provider calls.
- AC-10: live failures are diagnosed before quota-consuming reruns.
- AC-11: A5 release bundle passes and emits a live evidence manifest.
- AC-12: final review uses the exact bounded claim and states its scope.
- AC-13: each packet passes applicable autorun, commit-steward, file-size,
  source-fidelity, handoff, and closure-quality gates.

## Verification / Evidence

| Tranche | Required evidence class |
|---|---|
| A0 | source map, line-count evidence, architecture decision, clean governed diff |
| A1 | package resolution, unit tests, route integration tests, typecheck, build, file-size gate |
| A2 | atomic-write, restart, replay, duplicate, corruption, and partial-write test evidence |
| A3 | secret-safe live diagnostic plus provider receipt correlated to durable SOT3 identifiers |
| A4 | negative-case decision evidence, provider call-count assertion, recovery and rollback evidence |
| A5 | canonical release JSON, live evidence manifest, final completion review, committed-range gates |

## Stop Conditions

- an existing field, path, or symbol cannot be source-verified;
- A1 needs substantial lifecycle logic inside the near-limit execute route;
- `ENFORCE` can fall back to raw context;
- persistence silently loses or rewrites authority state;
- a negative case invokes the provider when it should reject locally;
- a live failure is repeated without a diagnostic;
- the live key is unavailable after checking the governed local environment;
- the release bundle skips or mocks SOT3 proof;
- closure language expands to production, public, universal, or user-value
  validation.

## Cost And Value Control

Stop branch expansion when a proposed case does not change context admission,
authority binding, distribution permission, or durable recovery. Park
near-duplicate cases after each boundary has one positive and one meaningful
negative proof. Provider-call budgets are binding; reruns need a new diagnostic
or a result-changing repair.

## Non-Goals

- no full CVF runtime conversion to SOT3;
- no truth classification of arbitrary prompts or model outputs;
- no autonomous source-score or truth mutation;
- no provider inside Refinery, Kernel, or Flow;
- no database, distributed ledger, multi-region, load, or scale claim;
- no output-quality parity or prompt-tuning lane;
- no public-sync, production-readiness, or hosted-readiness claim;
- no claim of real-user value before shipment and field feedback.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance activation and live proof only. No public-sync
repository mutation is authorized; public export needs a separate decision
after closure.

## Claim Boundary

`LIVE_GOVERNANCE_PROVEN_BOUNDED` will mean only that, for the selected CVF Web
knowledge-context path, controlled scenario, provider lane, environment, and
evidence window, all three SOT3 layers governed context before a real provider
call and required failure boundaries were observed.

It will not mean production readiness, universal coverage, correctness of all
sources or outputs, scale, certification, public availability, product-market
fit, or user validation.

## Next Allowed Move

Create a fresh A4 GC-018 and source-verified work order for zero-call rejection
and bounded recovery proof. Do not execute A4 directly from this roadmap.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status:`; `Authorization / Decision`; `Scope / Target / Owner Boundary`; `Design Control Gate`; `Work Plan`; `Acceptance Criteria`; `Verification / Evidence`; `Public Export Disposition`; `Machine Closure Package` |
| gateRunPurpose | confirmation and evidence after source-backed roadmap design; not first discovery |
| claimBoundary | A0 architecture and roadmap planning only; no runtime or live proof |

## Epistemic Process Block

### Expected Result / Prediction

The scoped knowledge-context seam should exercise all three SOT3 layers before
a real provider call while remaining small enough to prove and roll back.

### Evidence Comparison

Current source shows tenant-aware retrieval immediately before prompt
construction, while the SOT3 packages expose the required deterministic public
APIs. No current product adapter or durable SOT3 evidence store exists.

### Contradiction Or Gap Disposition

The existing prompt helper calls retrieved context pre-governed, but retrieval
scope alone is not a Kernel truth decision. A1 must close this semantic gap
without weakening retrieval scope or moving authority into the provider.

### Claim Update

A0 raises no runtime claim. It replaces an unspecified activation gap with a
bounded, dependency-ordered A1-A5 proof path.

## ADIF Defect Registry Disclosure

Query:
`python governance/compat/run_adif_defect_resolver.py --task-class architecture-design --role architect-reviewer --lifecycle-phase implementation --surface-selector sot-three-layer --risk-ceiling HIGH --max-results 20 --json`

Returned defectIds: none.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_COMPLETION_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this roadmap | `Status: A3_CLOSED_PASS_BOUNDED_A4_PACKET_NEXT`; A0-A3 closed; A4-A5 open | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/README.md` | existing registry front door | PASS |
| External evidence digest | N/A with reason: A2 is local non-live implementation | N/A | N/A with reason |
| System loop interlock | N/A with reason: no automated loop edge | N/A | N/A with reason |
| Session continuity | separate post-material session sync | pending until material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| A2 durable evidence claim remains local | atomic local-file, restart, integrity, duplicate, corruption, and partial-write proof only | PASS |
| A3 owns real-provider correlation | accepted recovery receipt correlates provider, governance, and SOT3 IDs | PASS |
| A4-A5 live/release acceptance remains unclaimed | failure/recovery and release tranches remain open | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | architect/reviewer; A3 reviewer/closer amendment |
| Provider or surface | local private provenance repository |
| Session or invocation | SOT3-ACT roadmap, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, line-count inspection, `apply_patch` |
| Target paths | A3 recovery and closure material manifest |
| Allowed scope source | operator instruction to execute A0 and design A1-A5 |
| Before status evidence | no activation roadmap; live/provider work parked |
| After status evidence | A0-A3 closed; A4 is the next fresh packet-authoring move |
| Diff evidence | material changed-set captured before commit |
| Approval boundary | A3 bounded recovery and roadmap state transition only |
| Claim boundary | A3 `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED`; no A4/A5/final claim |
| Agent type | architect/reviewer |
| Invocation ID | `sot3-act-roadmap-2026-07-13` |
| Expected manifest | `scripts/run_cvf_sot3_a3_live_proof.py`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-launch-diagnostic-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-receipt-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-manifest-2026-07-13.json`; `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` |
| Actual changed set | `scripts/run_cvf_sot3_a3_live_proof.py`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-launch-diagnostic-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-receipt-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-manifest-2026-07-13.json`; `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` |
| Manifest delta | MATCH |
