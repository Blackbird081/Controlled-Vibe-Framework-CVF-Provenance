# CVF Runtime Findings Closure Roadmap

Memory class: governed-roadmap

Status: ACTIVE_R7B_DISPATCHED_PENDING_WORKER_RETURN

docType: roadmap

Date: 2026-08-24

Roadmap base head: `e196899548d04f88ee5bc40cfce1ddf268a29d6b`

## Authorization / Decision

The operator directed CVF to resolve the verified findings before further
absorption or feature coding and assigned the current agent as
orchestrator/reviewer, with worker packets copied to separate external agents.

## Purpose

Close verified runtime authority, gateway, MCP, provenance, and isolation gaps
through bounded CVF-native tranches. Every implementation tranche requires its
own GC-018, no-commit worker order, independent review, material commit, and
separate continuity sync when applicable.

## Scope / Target / Owner Boundary

| Tranche | Findings | Existing owner | Target outcome |
|---|---|---|---|
| R0 | all | governance dispatch/review | persist verification, roadmap, R1 baseline and work order |
| R1 | F1 | Guard Contract | mutating BUILD fails closed without accepted SPEC, valid WORK ORDER and bounded scope |
| R2 | F2-F4 | Guard Contract and Mandatory Gateway | immutable mandatory guards/config plus exact canonical bypass matching |
| R3 | F8 | MCP server, Model Gateway, Execution Plane | MCP invocation obtains native CVF admission; caller policy data cannot authorize execution |
| R4 | F5 | Model Gateway, context/evidence and Truth owners | secret-safe material-context manifest linked to invocation evidence |
| R5 | F9 | Execution/isolation owner | declared isolation dimensions match actual adapter guarantees and unsupported claims reject |
| R6 | all | independent reviewer/closer | adversarial cross-owner re-audit and bounded closure |

## Non-Goals

No new subsystem, phase-enum expansion, provider/live call, credential use,
deployment, public sync, external corpus absorption, unrelated feature work, or
worker commit. F6, F7 and F10 may inform existing-owner enrichment but do not
open implementation tranches here.

## Design Control Gate

- Keep the canonical five runtime phases.
- Represent SPEC and WORK ORDER as typed authority evidence for BUILD, not new
  phases.
- Reuse `hasModifyIntent` for mutation classification.
- Every denial is fail-closed and must have negative tests.
- Provider/capability compatibility never grants trust or invocation authority.
- Evidence manifests must be secret-safe; raw prompts, credentials and signed
  headers are forbidden.

## Work Plan

| Order | Entry criteria | Required proof | Exit state |
|---|---|---|---|
| R0 | operator remediation instruction | review, roadmap, R1 GC-018/work order; pre-dispatch gates | R1 dispatch committed |
| R1 | R0 committed | 41/41 guard tests, 122/122 composed tests, 936 package tests plus 5 skips, TypeScript and reviewer gates pass | F1 `CLOSED_PASS_BOUNDED` at `a670343706c4fa21427a55a9c2ba464b9cef6cd4` |
| R2 | R1 independently accepted | 62/62 focused tests, 949 package tests plus 5 skips, TypeScript, freshness, file-size and reviewer-fast pass | F2-F4 `CLOSED_PASS_BOUNDED` at `84d44889fe2724e574241b5fb74d371e900fd6e3` |
| R3 | R2 independently accepted | 31/31 focused, 748/748 package, TypeScript and reviewer proof; caller policy cannot authorize | F8 `CLOSED_PASS_BOUNDED` at `a18ba512f` |
| R4 | R3 independently accepted | 58/58 focused, 288/288 package, TypeScript and reviewer proof; all material context classes and invocation/receipt bindings exact | F5 `CLOSED_PASS_BOUNDED` at `8ec399aa50158474c3d5ccf0c3cd9d33bfaf72f0` |
| R5 | R4 independently accepted | Safety Runtime 61/61, adapter focused 49/49, package 91/91, TypeScript and reviewer adversarial proof across all eight dimensions | F9 `CLOSED_PASS_BOUNDED` at `82a0073b2fca002fd7999ed70905166295946515` |
| R6 | R5 independently accepted | complete finding matrix, negative suite, manifest reconciliation and reviewer gates | `AUDIT_COMPLETE_REMEDIATION_REQUIRED`: F3/F4/F7/F9 closed; F1/F2/F5/F6/F8/F10 retained with reason; roadmap closure withheld |
| R7A | R6 audit accepted; operator approved recommended split | make all MCP production roots adopt canonical `cvf-guard-contract`; preserve MCP-local session phase without a replacement factory | `CLOSED_PASS_BOUNDED`: canonical roots adopted; self-attestation/action-label findings closed after one repair round; 777/780 package tests with only three R7B failures |
| R7B | R7A independently accepted and material closure committed | repair optional-field composition seam while preserving strict fail-closed material-context validation | `DISPATCHED_PENDING_WORKER_RETURN`: exact-two implementation files plus one no-commit worker return |

No tranche begins from worker assertion alone. Repair round three escalates to
operator/design review instead of silently widening scope.

## Dispatch Boundary

R1 is closed bounded at `a670343706c4fa21427a55a9c2ba464b9cef6cd4`.
R2 is closed bounded at `84d44889fe2724e574241b5fb74d371e900fd6e3`.
R3 is independently closed bounded at `a18ba512f`. R4 is independently closed
bounded at `8ec399aa5`. R5 is independently closed bounded at `82a0073b2` with
continuity `ad5edc2b4`. The reviewer accepts R6 as a completed read-only audit,
but withholds roadmap closure after independently reproducing two source
defects: live MCP admission bypasses the canonical guard contract through a
stale local fork, and the R4/R3 optional-field seam fails 3 of 31 focused MCP
tests. No implementation repair or external effect is released. Fresh
remediation authority is required before either source owner may be edited.
The operator approved the recommended split. R7A is independently accepted
after one consolidated repair round: all production engine/factory roots use
the canonical contract, launcher self-attestation is removed, action labels
are truthful, and unsupported authority remains fail-closed. R7B may receive a
fresh bounded dispatch packet after the R7A material closure commit. No live,
provider, deployment, public-sync or push effect is released by this roadmap
transition.

R7A material closure is committed at `1512374e8` and its continuity sync at
`e66a21554`. The fresh R7B packet dated 2026-08-25 authorizes only the existing
Model Gateway manifest source, its dedicated test and one no-commit return.
The unchanged MCP composition proof is acceptance evidence, not worker scope.

## Acceptance Criteria

- F1, F5 and F8 have independent negative runtime/test proof before absorption
  resumes;
- F2-F4 and F9 are either closed or explicitly retained with bounded risk and
  operator decision;
- no implementation creates a competing owner;
- all worker returns preserve unchanged HEAD and empty staging;
- material commits precede separate session-sync commits;
- R6 reconciles every finding to `CLOSED`, `RETAINED_WITH_REASON`, or
  `BLOCKED_WITH_REASON`.

## Verification / Evidence

Each tranche runs its focused tests, package typecheck where applicable,
governed file-size and relevant fast gates, `git diff --check`, exact manifest
comparison, and reviewer-authored adversarial probes. Live governance claims,
if introduced later, require the canonical real-provider release gate; none are
authorized by this roadmap.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| verified finding set and severity | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position | F1-F10 matrix | governed review | ACCEPT |
| repeated mistakes become rules and gates | GOVERNANCE_RULE | `AGENTS.md` | Task Class Routing | error-to-governance learning route | canonical instruction carrier | ACCEPT |
| runtime implementation requires work order | GOVERNANCE_RULE | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | template control blocks | no-commit worker/reviewer split | work-order standard | ACCEPT |
| closure follows separated commit choreography | GOVERNANCE_RULE | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | material and session-sync sequence | reviewer/closer choreography | closure standard | ACCEPT |

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Earliest gate target | Roadmap disposition |
|---|---|---|---|
| F1 | `RULE_GAP` | Guard Contract evaluation | R1 |
| F2-F4 | `MACHINE_GATE_GAP` | registration/bootstrap/config | R2 |
| F8 | `MACHINE_GATE_GAP` | MCP invocation admission | R3 |
| F5 | `RUNTIME_SIGNAL_GAP` | Model Gateway invocation assembly | R4 |
| F9 | `RUNTIME_SIGNAL_GAP` | execution adapter admission | R5 |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R4_MATERIAL_CONTEXT_MANIFEST_2026-08-24.md` | committed authority `9660fb5a1` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RFR_R4_MATERIAL_CONTEXT_MANIFEST_COMPLETION_2026-08-24.md` | bounded reviewer acceptance pending material identity | PASS |
| Roadmap state | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md` | R4 accepted bounded; R5 remains dependency-gated | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate covers both new R4 source/test paths | PASS |
| Registry Markdown | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md` | canonical human-readable tranche state | PASS |
| External evidence digest | N/A | no external evidence was used for RFR-R4 remediation beyond governed worker return | N/A with reason: local source and test evidence only |
| System loop interlock | this roadmap | R5-R6 dependency order remains closed and external effects remain parked | PASS |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | exact RFR-R4 material SHA must follow the material commit | BLOCKED with reason: material commit identity is not available pre-commit |
| R1 BUILD authority | `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md` | material commit `a670343706c4fa21427a55a9c2ba464b9cef6cd4` | PASS_BOUNDED |
| R2 immutable mandatory core | `docs/reviews/CVF_RFR_R2_IMMUTABLE_MANDATORY_CORE_COMPLETION_2026-08-24.md` | material commit `84d44889f`; reviewer repair included | PASS_BOUNDED |
| R3 native MCP admission | `docs/reviews/CVF_RFR_R3_NATIVE_MCP_ADMISSION_COMPLETION_2026-08-24.md` | material `a18ba512f`; 31 focused; 748 package pass; reviewer repair included | PASS_BOUNDED |
| R4 material context manifest | `docs/reviews/CVF_RFR_R4_MATERIAL_CONTEXT_MANIFEST_COMPLETION_2026-08-24.md` | 58 focused; 288 package pass; reviewer repair included | PASS_BOUNDED_PENDING_MATERIAL_COMMIT |
| R5-R6 | later tranche authority | dependency chain remains closed | PARKED_DEPENDENCY_GATED |
| external effects | roadmap boundary | zero provider/live/public/deploy/push actions | PARKED |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| material-context evidence | exact complete manifest; hostile/invalid input calls adapter zero times | 58/58 focused tests pass | PASS |
| Package proof | Model Gateway package remains green | 288/288 package tests pass | PASS |
| Material identity | exact reviewed commit recorded in continuity | unavailable until material commit is created | BLOCKED with reason: post-material continuity sync owns the SHA receipt |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | verified external findings -> existing-owner remediation tranches |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | the existing owner named for each R1-R5 tranche |
| Disposition | ADAPT only verified deltas; no external subsystem import |
| Claim boundary | roadmap ordering is not external-source authority, implementation or closure |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | `Status:`; `Authorization / Decision`; `Purpose`; `Scope / Target / Owner Boundary`; `Non-Goals`; `Design Control Gate`; `Dispatch Boundary`; `Acceptance Criteria`; `Verification / Evidence`; `Public Export Disposition` |
| gateRunPurpose | confirm roadmap and dependent-dispatch literals before authoring |
| claimBoundary | roadmap conformance does not prove implementation or closure |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private remediation authority only; public synchronization requires a
later explicit public-sync disposition and sibling-clone proof.

## Claim Boundary

This roadmap authorizes bounded local remediation sequencing. It does not claim
that any finding is fixed, that later tranches are dispatched, or that the
private repository may be pushed to the public remote.
