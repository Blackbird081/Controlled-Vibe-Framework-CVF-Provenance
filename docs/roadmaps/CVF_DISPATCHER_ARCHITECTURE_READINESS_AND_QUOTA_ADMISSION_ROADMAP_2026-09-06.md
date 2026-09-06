# CVF Dispatcher Architecture Readiness And Quota Admission Roadmap

Memory class: governed-roadmap

Status: DARA_T0_EVIDENCE_CAPTURED_T1_DESIGN_REQUIRED

Date: 2026-09-06

Parent roadmap: `docs/roadmaps/CVF_GCLH_GOVERNANCE_CONTROL_LOSS_HARDENING_ROADMAP_2026-08-31.md`

## Authorization And Decision

The operator directed CVF foundation uplift before any further repair of the
parked Phase-04 `WP-ARCH-003` audit findings. This roadmap captures the
incident as bounded evidence, routes it into existing GCLH, SCEC, Review Cost,
work-order and ADIF owners, and establishes a fail-closed interlock.

Decision: `PROCEED_FOUNDATION_FIRST`. The two pending `WP-ARCH-003` worker
outputs remain untracked evidence and receive no acceptance or implementation
authority from this roadmap. No further external repair invocation may be
dispatched until the DARA foundation acceptance criteria below are closed.

## Purpose

Prevent a higher-authority dispatcher or reviewer from consuming repeated
worker quota with an architecture-incomplete work order. Move architecture
binding and semantic review before external invocation while preserving the
existing rule that deterministic machinery does not decide engineering truth.

The control target is:

```text
operator intent
  -> dispatcher architecture binding matrix
  -> deterministic coverage and consistency checks
  -> independent semantic pre-dispatch review for HIGH/CRITICAL work
  -> quota admission
  -> worker execution
  -> evidence-focused review
```

## Scope

In scope:

- the Initial, Rework Round 1, and Rework Round 2 `WP-ARCH-003` dispatch chain;
- dispatcher/reviewer responsibility and worker fault-attribution boundaries;
- architecture completeness before a work order delegates exact path choice;
- external invocation admission and avoidable-invocation accounting;
- composition with the existing work-order template, GCLH, MFRP, SCEC,
  Review Cost, TPGR and ADIF owners;
- historical replay proving that this incident would have stopped before the
  avoidable repair invocations.

## Non-Goals

- No repair or acceptance of the two pending `WP-ARCH-003` outputs.
- No Round 3 external dispatch.
- No implementation of `WP-ARCH-003` or its proposed guard contracts.
- No semantic-scoring model or claim that a machine can decide architecture.
- No new parallel convergence, quota, work-order or reviewer authority owner.
- No source, test, runtime, provider/live, credential, public-sync,
  deployment or production action in DARA-T0/T1.

## Incident Evidence Baseline

Frozen repository base for this roadmap: `17c8fe30fdc4468f6748d67926e3d95224723a7a`.

| Evidence ID | Source | Observed fact | Disposition |
|---|---|---|---|
| DARA-E01 | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md` | initial dispatch declares `reviewRoundCount: 0`, cumulative external invocation count 0 and ceiling 1 | ACCEPT_COMMITTED_AUTHORITY |
| DARA-E02 | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_AMENDMENT_1_2026-09-06.md` | R1 declares invocation 1 before and 2 after execution | ACCEPT_COMMITTED_AUTHORITY |
| DARA-E03 | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_AMENDMENT_2_2026-09-06.md` | R2 declares invocation 2 before and 3 after execution | ACCEPT_COMMITTED_AUTHORITY |
| DARA-E04 | `docs/assessments/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md`, raw SHA-256 `91b2a5c07fcf341c94f3adbcaab040ec7e343a4a7faf523becabad17ec321f27` | pending R2 manifest creates `evaluateAuthorityExpansionApproval` in both Execution Plane and Guard Contract and retains `<date>` evidence-path placeholders | PENDING_INCIDENT_EVIDENCE_NOT_AUTHORITY |
| DARA-E05 | `docs/reviews/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_WORKER_RETURN_2026-09-06.md`, raw SHA-256 `ce137665a13a852c05ed0b03aca60c58c6feb7829ff4fe3e7335f4c3209ba8ac` | exact-two/no-commit/test-ledger discipline is present; SCEC reaches `STOP_REASSESS_ARCHITECTURE` after two non-decreasing transitions | PENDING_INCIDENT_EVIDENCE_NOT_AUTHORITY |
| DARA-E06 | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | sequential reviewer findings consume quota and time; a full record/edge matrix is required before first repair | ACCEPT_EXISTING_RULE_OWNER |
| DARA-E07 | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md` | local gates can pass while the semantic problem boundary moves; SCEC checks evidence shape, not engineering truth | ACCEPT_EXISTING_RULE_OWNER |
| DARA-E08 | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | orchestrator translates roadmap into work orders; implementer executes the order; invented symbols must return to orchestrator | ACCEPT_EXISTING_AUTHORITY |
| DARA-E09 | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | machines validate identity, paths and coverage while reviewers decide semantic correctness and risk | ACCEPT_EXISTING_DESIGN_OWNER |

Measured cost is bounded to three external invocations and two repair turns.
Token or subscription-quota quantity is `UNKNOWN`: the local repository does
not expose a trustworthy token counter for these external sessions. This
roadmap therefore does not invent a token total or monetary cost.

## Root Cause And Fault Attribution

| Cause ID | Cause | Owning role/surface | Worker attribution |
|---|---|---|---|
| DARA-C01 | exact-path requirement was dispatched without a complete owner-to-runtime architecture graph | dispatcher/reviewer; work-order design | NOT_WORKER_DEFECT |
| DARA-C02 | R2 delegated architecture selection to a documentation worker rather than supplying a reviewer-accepted design | dispatcher/reviewer; pre-dispatch admission | NOT_WORKER_DEFECT |
| DARA-C03 | structural gates admitted literal paths without proving single ownership, registration or runtime reachability | machine-coverage gap plus required human semantic review | NOT_WORKER_DEFECT |
| DARA-C04 | SCEC stopped the chain only after two non-decreasing transitions, after the avoidable invocations had occurred | correct late-stage stop; missing left-shifted admission | NOT_WORKER_DEFECT |
| DARA-C05 | pending worker evidence was initially treated as accepted evidence | dispatch/review authority classification | DEPENDENT_WORKER_REPAIR_ONLY |

Current worker compliance retained as counter-evidence: exact-two paths,
unchanged HEAD, empty staging, no worker commit, eight-path test ledger and
28/28 focused canonical-adoption proof. The incident must not be recorded as
two generalized worker failures.

## Existing Owner Composition

| Required capability | Existing owner | Planned enrichment |
|---|---|---|
| work-order authority and source verification | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | require an architecture binding matrix when a worker would otherwise select design-bearing paths |
| phase-input quality and control-loss hardening | GCLH roadmap | add DARA as a subordinate incident/replay lane under T1/T2 |
| machine-first path/coverage verification | MFRP roadmap and future phase-return verifier | validate matrix completeness and contradictions without deciding semantic truth |
| convergence and stop | SCEC standard/checker | consume DARA fault-attribution evidence; do not create a second stop framework |
| review rounds and quota economics | Review Cost standard/checker | distinguish dispatcher-caused repair cost and gate quota before dispatch |
| proportional route/value admission | TPGR | add the architecture-ready receipt as a future P2/P3 external-delegation input only after design acceptance |
| durable defect learning | ADIF-0026 and ADIF-0055 | attach this incident as roadmap/replay evidence; do not duplicate entries until residual novelty is reviewed |

## Design Control Gate

Before any DARA implementation work order, T1 must freeze one Architecture
Binding Matrix schema containing, per acceptance criterion:

| Required binding | Required proof |
|---|---|
| acceptance criterion and invariant ID | canonical source path and unique locator |
| canonical owner | one owner path and overlap search result |
| existing/new symbol | exact path, exact symbol, create/extend disposition |
| data or identity producer | exact producer symbol and trust source |
| context/schema transport | exact type/field and every required adapter boundary |
| export surface | exact barrel/package export path |
| registration | exact registry/factory/composition symbol or `NONE_WITH_REASON` |
| composition root | exact production entrypoint and construction path |
| runtime consumer | exact non-test consumer or explicit contract-only boundary |
| verification | exact positive, negative, bypass and composition test paths |
| compatibility/migration | exact input/output paths or `NONE_WITH_REASON` |
| rollback | exact changed paths and reversible command boundary |
| evidence output | one literal dated repo-relative path, with no placeholder pattern |

Admission rules:

1. HIGH/CRITICAL work using an external worker requires independent semantic
   acceptance of the matrix before invocation 1.
2. A documentation worker may transcribe an accepted matrix but may not select
   a new runtime owner, symbol split, data producer or composition route.
3. Duplicate behavior across packages, a new guard without export/registration,
   or a context field without producer-to-consumer transport blocks dispatch.
4. Literal paths containing placeholders such as `<date>`, unnamed adjacent
   files, path classes or future selection language are not exact paths.
5. Machine verification proves presence, identity, uniqueness candidates and
   coverage only. Reviewer acceptance remains the semantic authority.
6. Missing matrix fields stop before external quota admission; they do not
   become worker discovery tasks.

## Work Plan

| Tranche | Mission | Outputs | Entry | Exit decision |
|---|---|---|---|---|
| DARA-T0 | incident capture and owner reconciliation | this roadmap and immutable evidence IDs DARA-E01 through DARA-E09 | operator foundation-first direction | `T0_EVIDENCE_CAPTURED` or `BLOCK_SOURCE_INTEGRITY` |
| DARA-T1 | architecture-readiness contract design | matrix schema, role/fault taxonomy, semantic reviewer checkpoint and quota-admission contract | independent review of T0 | `DESIGN_ACCEPTED_BOUNDED` or `STOP_NO_SAFE_COMPOSITION` |
| DARA-T2 | minimal foundation implementation | existing-owner template/standard/scaffold/checker changes with protected-path authorization | accepted T1 plus GC-018/work order | `CORE_CONTROL_IMPLEMENTED` or `BLOCK_IMPLEMENTATION_EVIDENCE` |
| DARA-T3 | historical replay | Initial/R1/R2 replay fixture and deterministic receipt showing earliest stop | accepted T2 | `REPLAY_BLOCKS_AVOIDABLE_INVOCATIONS` or `RETURN_TO_DESIGN` |
| DARA-T4 | bounded shadow validation | selected future HIGH/CRITICAL dispatch dual-evaluated without relaxing legacy gates | accepted T3 and operator release | `SHADOW_VALUE_PROVEN` or `ROLLBACK_NO_VALUE` |
| DARA-T5 | projection and activation decision | guard orientation, downstream profile and active-workflow projection | accepted T4 | `ACTIVATE_BOUNDED` or `PARK_FOUNDATION` |

No tranche opens automatically. DARA-T1 requires independent review; DARA-T2
requires a new protected-path work order. Runtime/provider/public actions are
outside this roadmap.

## WP-ARCH-003 Interlock

The pending `WP-ARCH-003` finding chain remains parked. It may reopen only
after all of the following are true:

- DARA-T1 architecture matrix and role/fault taxonomy are accepted;
- DARA-T2 installs the applicable pre-dispatch controls;
- DARA-T3 proves the historical chain would have been blocked before the
  first avoidable rework invocation;
- a fresh reviewer-owned `WP-ARCH-003` architecture matrix identifies one
  canonical owner and the complete producer-to-runtime-consumer path;
- the new dispatch starts from that accepted architecture, not as a narrow
  successor to the stopped SCEC chain.

The two current untracked files must remain preserved as incident evidence
until a separately authorized disposition archives, replaces or rejects them.

## Failure And Escalation Modes

| Failure | Required response |
|---|---|
| matrix becomes another prose checklist | return DARA-T1 to design; require closed fields and exact identities |
| checker pretends to judge semantic correctness | reject implementation; preserve reviewer authority |
| new framework duplicates SCEC/Review Cost/TPGR | collapse into existing owners |
| quota admission trusts worker-authored readiness | fail closed; require independent reviewer acceptance |
| fault attribution assigns dispatcher defects to worker | block closure and correct the incident ledger |
| replay cannot demonstrate an earlier stop | do not activate; reassess which observable pre-dispatch signal is missing |
| control ceremony costs more than avoided repair | simplify or park after safety equivalence is preserved |

## Metrics And Quota Evidence

| Metric | Baseline | Desired direction |
|---|---|---|
| external invocations for this incident | 3 | historical replay admits 1 or blocks before invocation 1 when design is incomplete |
| repair turns | 2 | 0 dispatcher-caused worker repair turns |
| semantic findings first discovered after invocation | at least 3 R2/R3 architecture findings | 0 for matrix-covered zero-tolerance classes |
| exact manifest placeholder escapes | 2 `<date>` evidence paths in R2 | 0 |
| duplicate-owner candidate escapes | one duplicated evaluator plan in R2 | 0 |
| unregistered/unwired component escapes | principal/scope guard path lacks complete production composition chain | 0 |
| token or subscription quota | UNKNOWN | record exact value only when observable; never infer |

Required attribution fields for future design: `dispatcherDefectCount`,
`workerExecutionDefectCount`, `reviewerLateDiscoveryCount`,
`repairIntroducedDefectCount`, `avoidableExternalInvocationCount`, and
`tokenOrQuotaUsage` with an explicit evidence state.

## Acceptance Criteria

- The Architecture Binding Matrix has closed, machine-validated fields and a
  reviewer-owned semantic acceptance state.
- A HIGH/CRITICAL external dispatch cannot consume invocation 1 while any
  required architecture binding is missing, contradictory or self-attested.
- A symbol planned in more than one canonical owner is surfaced before
  dispatch unless an accepted adapter/delegation relationship explains it.
- A new runtime guard cannot be marked architecture-ready without exact
  export, registration, composition-root, context transport and non-test
  consumer bindings.
- Exact-path validation rejects placeholders and path-class prose.
- Fault attribution separates dispatcher, worker, reviewer-late-discovery and
  repair-introduced causes.
- Historical replay blocks the R2 duplicate evaluator, missing wiring and
  placeholder evidence paths before an external repair call.
- SCEC remains the convergence/stop owner and Review Cost remains the
  repair-economics owner.
- No `WP-ARCH-003` finding repair resumes before the interlock closes.

## Verification And Evidence Plan

DARA-T0 verification is documentation-only and provider-free:

```powershell
python governance/compat/check_governed_artifact_checker_read_ahead.py --base 17c8fe30fdc4468f6748d67926e3d95224723a7a --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 17c8fe30fdc4468f6748d67926e3d95224723a7a --head HEAD --all-changed --enforce
python governance/compat/check_roadmap_closure_freshness.py --base 17c8fe30fdc4468f6748d67926e3d95224723a7a --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 17c8fe30fdc4468f6748d67926e3d95224723a7a --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
git diff --check
```

These commands prove document structure and recorded evidence consistency,
not acceptance of DARA-T1 design or effectiveness of an unimplemented gate.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Existing owner | Roadmap action | State |
|---|---|---|---|---|
| higher-authority incomplete design causes worker guesswork | `ORCHESTRATOR_PACKET_GAP` | work-order template plus GCLH | add Architecture Binding Matrix and reviewer checkpoint | DARA_T1_REQUIRED |
| structural PASS coexists with semantic architecture failure | `PHASE_GATE_PLACEMENT_GAP` | MFRP plus GCLH | surface closed matrix coverage before dispatch; retain human semantic decision | DARA_T1_REQUIRED |
| repeated external repairs consume avoidable quota | `RULE_GAP` already represented by ADIF-0026 | Review Cost plus TPGR | add pre-invocation admission and role-attributed cost | DARA_T1_REQUIRED |
| local compliance while problem boundary moves | `RULE_GAP` already represented by ADIF-0055 | SCEC | replay and consume STOP; no parallel stop framework | DARA_T3_REQUIRED |
| worker blamed for dispatcher-created architecture defects | `EVIDENCE_INTERPRETATION_ERROR` | ADIF and review ledger | require causal role attribution before repair dispatch | DARA_T1_REQUIRED |

ADIF-0026 and ADIF-0055 currently carry `roadmapSeedId: NONE`; DARA-T1 must
decide whether to bind this roadmap as their existing-owner seed or create one
new residual ADIF entry only for the higher-authority fault-attribution gap.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | roadmap authorization, Purpose, Scope, Non-Goals, Design Control Gate, Work Plan, Acceptance Criteria, Verification, finding-learning, trace, public disposition and claim boundary |
| gateRunPurpose | confirm the DARA-T0 roadmap shape and evidence bindings after source/checker read-ahead; not first discovery |
| claimBoundary | checker conformance does not accept DARA-T1 design or prove quota savings |

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: the pending worker outputs are local incident
evidence. No external repository, copied folder or third-party corpus is being
absorbed.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this roadmap uses two exact local pending outputs
and committed CVF authority paths as a bounded incident set; it makes no corpus
completeness or external-repository absorption claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | pending result -> reviewer evidence reconstruction -> existing-owner roadmap enrichment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; SCEC, Review Cost, work-order quality and finding-to-governance learning controls |
| Owner surface | GCLH roadmap, Work Order Template, MFRP, SCEC, Review Cost, TPGR and ADIF |
| Disposition | ADAPT verified incident facts; do not promote worker conclusions to authority |
| Claim boundary | no external knowledge absorption, runtime value or worker-output acceptance claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/reviewer |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T0 foundation-first roadmap authoring, 2026-09-06 |
| Working directory | repository root |
| Command or tool surface | startup continuity checks, direct governed-source reads, `rg`, SHA-256, `apply_patch`, roadmap gates and git |
| Target paths | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` |
| Allowed scope source | operator instruction on 2026-09-06 to uplift CVF foundation before continuing findings |
| Before status evidence | base HEAD `17c8fe30fdc4468f6748d67926e3d95224723a7a`; two parked untracked `WP-ARCH-003` outputs preserved and staging empty |
| After status evidence | this roadmap is the only DARA-T0 material path; pending worker outputs remain untouched and untracked |
| Diff evidence | `git status --short`; `git diff --check`; roadmap structural and pre-commit gates |
| Approval boundary | foundation roadmap and evidence capture only; no T1/T2 implementation or external invocation |
| Claim boundary | no worker-output acceptance, implementation, provider/live, public, deployment or production claim |
| Agent type | orchestrator/reviewer |
| Invocation ID | `dara-t0-foundation-first-roadmap-2026-09-06` |
| Expected manifest | this roadmap only |
| Actual changed set | this roadmap only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation design evidence; no public-sync authority.

## Claim Boundary

This roadmap records a bounded governance/control-plane incident and a
foundation-first work sequence. It does not accept the pending worker outputs,
prove an unimplemented control, authorize DARA-T1/T2 automatically, resume
`WP-ARCH-003`, consume another external invocation, mutate runtime/source, or
make provider/live/public/deployment/production claims.
