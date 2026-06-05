# CVF GC-018 - MLW8 Efficiency And Overconstraint Feedback

Memory class: FULL_RECORD

Status: GC018_AUTHORIZED_HOLD_FOR_WORK_ORDER

docType: gc018_baseline

Date: 2026-06-05

dispatchBaseHead: `2a21560e`

Commit mode: `WORKER_MUST_NOT_COMMIT` for any delegated worker implementation.

## Purpose

Authorize MLW8 as a bounded continuation candidate for treating efficiency,
context cost, verbosity, and governance friction as learning feedback signals.

MLW8 exists because the T11E corpus showed useful efficiency and
anti-overconstraint patterns, while MLW2/MLW3/MLW4/MLW5/MLW6 now expose
metadata-only route readouts that can support feedback. The critical boundary:
efficiency feedback must not become automatic quality cutting, evidence
trimming, policy relaxation, or autonomous prompt/runtime mutation.

This GC-018 opens the baseline only. It does not dispatch implementation. A
separate source-verified work order is required before runtime code, live proof,
public-sync, or closure claims.

## Scope / Target / Owner Boundary

Candidate owner surfaces:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-guard.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/context-budget-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/learning-plane-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw-runtime-chain-readouts.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-response-readouts.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts`
- T11E source-analysis packet and consolidated roadmap listed in the Source
  Verification Block.

Authorized next output:

- a source-verified MLW8 work order that defines an efficiency/overconstraint
  feedback lane using existing metadata readouts and Learning Plane proposal
  boundaries.

Authorized MLW8 work-order themes:

- context budget and token-pressure signal normalization;
- governance friction and overconstraint advisory classification;
- quality/evidence preservation guardrails;
- feedback-lane readout or ledger with `autonomousMutationAuthorized=false`;
- tests/checkers proving no automatic prompt shortening, policy relaxation, or
  evidence removal.

Out of scope for this GC-018 and any first MLW8 work order unless separately
authorized:

- automatic prompt optimization, context compression, or response shortening;
- reducing evidence, audit fields, receipt fields, DLP/safety checks, or
  approval gates;
- relaxing policy, provider risk ceilings, route gates, or validation;
- live provider calls;
- model tuning, benchmark reruns, public-sync, hosted-readiness,
  production-readiness, or public cost/performance claims.

Risk ceiling: R1/R2 feedback-lane planning. Escalate before live proof, runtime
optimization, policy change, public-sync, or cost/quality claim.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05: "GC-018 cho MLW7 và MLW8" | ACCEPT |
| MLW roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` row `MLW8` | ACCEPT |
| MLW0 source map | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` rows for context budget and MLW8 | ACCEPT |
| T11E secondary scan | `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md` findings `T11E-F4` and `T11E-F5` | ACCEPT |
| Current runtime source | Context budget, learning-plane, and MLW4-MLW6 route readouts exist at the paths verified below | ACCEPT |

## Decision / Baseline

Decision: MLW8 is authorized as a baseline and work-order candidate, not as an
optimization or policy-relaxation tranche.

Baseline facts at `2a21560e`:

- MLW0 identified current context budget owners and kept MLW8 optional until
  core stabilization or operator pull-forward.
- T11E accepted efficiency/compaction and anti-overconstraint as feedback
  signals only.
- Current runtime has context budget policy, guard, and route-visible
  `contextBudgetReadout`.
- Current runtime has Learning Plane readout and MLW4-MLW6 readouts that can
  support proposal-only feedback evidence.
- No current source authorizes autonomous mutation, automatic policy
  relaxation, or quality-reducing optimization for MLW8.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MLW8 is a planned efficiency and overconstraint feedback tranche | EXISTS | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | line 103 | `MLW8` | T11 consolidated roadmap | ACCEPT |
| MLW8 was optional pending core stabilization or operator pull-forward | EXISTS | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | line 165 | `MLW8 Efficiency And Overconstraint Feedback` | MLW0 source verification map | ACCEPT |
| Context budget current owners exist | EXISTS | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | lines 86, 126, 148 | `ContextBudgetPolicy`, `checkContextBudgetGuard`, `ContextBudgetReadout` | MLW0 source verification map | ACCEPT |
| T11E requires efficiency/overconstraint as learning signals, not immediate mutation | EXISTS | `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md` | line 71 | `efficiency/overconstraint feedback` | T11E scope boundary | ACCEPT |
| T11E flags quality-cutting automation as a risk | EXISTS | `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md` | lines 79, 155 | `efficiency must preserve quality` | T11E risk and sampling ledger | ACCEPT |
| T11E flags policy relaxation as a risk | EXISTS | `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md` | lines 80, 156 | `overconstraint and governance friction can be feedback signals` | T11E risk and sampling ledger | ACCEPT |
| Context budget policy interface exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-policy.ts` | line 25 | `ContextBudgetPolicy` | LPF context budget policy | ACCEPT |
| Context budget guard exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context-budget-guard.ts` | line 35 | `checkContextBudgetGuard` | LPF context budget guard | ACCEPT |
| Route context budget readout exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/context-budget-readout.ts` | lines 11, 21 | `ContextBudgetReadout`, `buildContextBudgetReadout` | cvf-web context budget readout | ACCEPT |
| `/api/execute` response readouts include context budget readout | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-response-readouts.ts` | lines 9, 48 | `buildContextBudgetReadout` | execute response readouts | ACCEPT |
| Learning Plane readout exists for advisory feedback | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/learning-plane-readout.ts` | lines 17, 50 | `LearningPlaneReadout`, `buildLearningPlaneReadout` | cvf-web learning plane readout | ACCEPT |
| MLW4-MLW6 route readout chain exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw-runtime-chain-readouts.ts` | lines 24, 43, 89, 141, 200, 376 | `ExecutionContinuityHandoffReadout`, `AuditFeedbackValidationReadout`, `SimulationFailureGateReadout` | MLW runtime chain readouts | ACCEPT |

## New Doc-Only Fields

| New field or marker | Purpose | Not sourced from runtime? | Runtime claim blocked? |
| --- | --- | --- | --- |
| `MLW8_GC018_BASELINE` | Marker for this authorization baseline | Yes | Yes |
| `efficiencyFeedbackCandidate` | Candidate work-order concept for context/cost/verbosity feedback | Yes | Yes |
| `overconstraintFeedbackCandidate` | Candidate work-order concept for governance friction feedback | Yes | Yes |
| `autonomousMutationAuthorized=false` | Explicit MLW8 planning invariant | Yes | Yes |

## Required Work-Order Shape

The next MLW8 work order must include:

| Requirement | Required behavior |
| --- | --- |
| Source Verification Block | Verify every runtime field/readout against current source before implementation |
| Roadmap trace | Map MLW8 roadmap requirement to each proposed artifact |
| Feedback taxonomy | Classify context pressure, verbosity, cost pressure, missing evidence, no-match, overconstraint, and operator friction without policy relaxation |
| Preservation guards | Prove evidence, audit, safety, DLP, approval, and receipt fields are not removed or weakened |
| Mutation boundary | Set `autonomousMutationAuthorized=false` or equivalent invariant on every feedback surface |
| Proof threshold | If runtime work is later authorized, require deterministic tests first; live proof only if a governed behavior claim is made |

## Knowledge Absorption Blind-Spot Control Block

- Prior absorption evidence resolved: T11E scan, T11 consolidated roadmap, MLW0
  source verification map, MLW2/MLW3/MLW4-MLW6 route-visible readout closures.
- Detailed source files read: current context-budget policy, guard, readout,
  execute response readout, Learning Plane readout, and MLW runtime-chain
  readouts were searched directly.
- Accepted value normalized into existing owner surface: efficiency and
  overconstraint enter as feedback signals on existing readout/learning surfaces.
- Accept/defer/reject disposition: accept as work-order candidate; defer runtime
  optimization; reject automatic quality cuts and policy relaxation.
- Adversarial role review: risk is converting efficiency into weaker governance;
  baseline requires preservation guards and mutation boundary.
- Blind-spot delta: exact feedback taxonomy and any route wiring remain for the
  next source-verified work order.
- Verdict: PARTIAL_WITH_LOW_RISK_REASON. The unresolved detail is intentionally
  assigned to the next source-verified work order and does not block opening the
  GC-018 baseline.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this file is an authorization baseline,
  not a fresh corpus inventory or completeness report.
- Corpus root: N/A with reason.
- Snapshot time: N/A with reason.
- Enumeration command: `rg --files --hidden --no-ignore docs/baselines/CVF_GC018_MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_2026-06-05.md`
- Manifest artifact or inline manifest: N/A with reason - no fresh corpus
  enumeration performed.
- Manifest hash: N/A with reason - no fresh corpus manifest generated.
- Processing ledger artifact or inline ledger: N/A with reason - no fresh corpus
  processing performed.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=1; unresolved=0.
- Unresolved files: N/A with reason.
- Declared exclusions: fresh legacy corpus rescan excluded; this baseline relies
  on prior T11E/MLW0 artifacts and current source verification.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregation performed.
- Drift check: N/A with reason.
- Output traceability: source facts are cited in the Source Verification Block.
- Adversarial verification: quality-cutting and policy-relaxation risks reviewed
  in the blind-spot block.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Rescan Intelligence Hardening

- Original source artifact: `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md`
- Predecessor intake artifact: `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md`
- Delta ledger status: BASELINE_ONLY_WITH_DECLARED_LIMITS
- Routing matrix status: BASELINE_ONLY_WITH_DECLARED_LIMITS
- Semantic sampling status: SOURCE_ANCHOR_SAMPLE_ONLY
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Item | Disposition | Reason |
| --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | Efficiency and overconstraint remain learning signals only | ACCEPT | T11E line 71 blocks immediate mutation |
| CHANGED_DISPOSITION | MLW8 moved from optional future candidate to GC-018 baseline | ACCEPT | Operator explicitly requested GC-018 for MLW8 |
| NEW_FINDING | Existing context-budget and MLW runtime-chain readouts provide candidate owner surfaces | ACCEPT | Current source exposes budget, Learning Plane, and MLW4-MLW6 metadata readouts |
| REMOVED_OR_REJECTED | Automatic cost optimization or policy relaxation | REJECT | Baseline blocks quality cuts, evidence trimming, and policy relaxation |

### Follow-Up Routing Matrix

| Routing lane | MLW8 item | Routed action |
| --- | --- | --- |
| DO_NOW | Source-verified MLW8 work order | Author only if operator asks to proceed after GC-018 |
| SEPARATE_RUNTIME_TRANCHE | Runtime route wiring or live proof | Requires separate implementation scope and proof plan |
| STRATEGIC_OPERATOR_DECISION | Public cost/performance claim threshold | Operator decision required |
| OUT_OF_SCOPE | Prompt shortening, evidence reduction, DLP/safety weakening, policy relaxation | Excluded from this baseline |
| RESOLVED_BY_DESIGN | Existing context budget guard is advisory and non-mutating | Preserve advisory boundary |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MLW8-S1 | T11E line 71 | Efficiency/overconstraint are feedback signals, not immediate mutation | ACCEPT | Could this become automatic prompt optimization? | PASS - mutation boundary blocks it |
| MLW8-S2 | T11E lines 79 and 155 | Efficiency must preserve quality, relevance, governance, and measurable successful resolution | ACCEPT | Could evidence be trimmed for token savings? | PASS - preservation guards required |
| MLW8-S3 | T11E lines 80 and 156 | Overconstraint and governance friction can be feedback signals but cannot relax hard policies | ACCEPT | Could friction become policy relaxation? | PASS - policy relaxation excluded |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Efficiency feedback can degrade evidence, safety, or quality if treated as automatic optimization | COST_ECONOMICS_SIGNAL_GAP | cost/economics learning | MACHINE_CHECK_CANDIDATE | MLW8 work order must include preservation guards |
| Anti-overconstraint feedback can be misused to weaken hard policies | OPERATOR_SCOPE_CLARITY_GAP | governance/control-plane learning | MACHINE_CHECK_CANDIDATE | MLW8 work order must prove policy relaxation is out of scope |

Promotion decision: TEMPLATE_UPDATED_BY_BASELINE. This GC-018 requires the next
work order to include preservation guards, mutation boundary, and policy
relaxation exclusions.

## Evidence / Verification

Required baseline verification before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 2a21560e --head HEAD
```

No live provider proof is required for this baseline because it does not assert
governed runtime behavior.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: MLW8 is private provenance planning only. No public-sync artifact,
public README/catalog claim, public cost claim, public performance claim, or
hosted-readiness claim is authorized by this baseline.

## Claim Boundary

This artifact proves only that MLW8 has a source-anchored GC-018 baseline. It
does not prove runtime optimization, cost reduction, quality improvement,
policy relaxation, public-readiness, production-readiness, hosted-readiness,
live provider behavior, or autonomous mutation.
