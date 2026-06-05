# CVF GC-018 - MLW7 Optional External Capability Ingestion

Memory class: FULL_RECORD

Status: GC018_AUTHORIZED_HOLD_FOR_WORK_ORDER

docType: gc018_baseline

Date: 2026-06-05

dispatchBaseHead: `2a21560e`

Commit mode: `WORKER_MUST_NOT_COMMIT` for any delegated worker implementation.

## Purpose

Authorize MLW7 as a bounded continuation candidate for external capability
ingestion after MLW1-MLW6 stabilized the route-visible memory/learning workflow
chain.

MLW7 exists because the T10/T11 corpus found recurring value in Hermes, HF,
cortex, deepagents, external skill/provider, and capability-provider patterns.
Current CVF already has an external-asset governance surface. MLW7 must decide
how these patterns should enter that existing governance path without turning
CVF into an external capability marketplace, package installer, autonomous tool
runner, or unreviewed runtime adapter.

This GC-018 opens the baseline only. It does not dispatch implementation. A
separate source-verified work order is required before code, public-sync, live
route proof, or runtime connector work begins.

## Scope / Target / Owner Boundary

Candidate owner surfaces:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/prepare/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cvf-add-runtime-doctrine.ts`
- `docs/reference/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md`
- T10/T11 source-analysis packets and findings listed in the Source Verification
  Block.

Authorized next output:

- a source-verified MLW7 work order that maps legacy external capability signals
  to current CVF external-asset governance owner surfaces.

Authorized MLW7 work-order themes:

- external capability candidate classification;
- admission-profile normalization;
- capability risk/readiness disposition;
- evidence and provenance fields needed before registry;
- explicit blocked delegation and runtime authority boundaries;
- tests/checkers that prove the mapping is proposal/intake only.

Out of scope for this GC-018 and any first MLW7 work order unless separately
authorized:

- installing packages, plugins, models, skills, MCP servers, or third-party repos;
- executing external capabilities;
- live provider calls;
- new package manager dependencies;
- autonomous worker routing, tool execution, memory reinjection, or policy
  mutation;
- public-sync, public catalog claims, hosted-readiness, production-readiness, or
  public marketplace claims.

Risk ceiling: R1/R2 documentation and source-map baseline. Escalate before any
runtime execution, new dependency, public-sync, or live provider proof.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05: "GC-018 cho MLW7 và MLW8" | ACCEPT |
| MLW roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` row `MLW7` | ACCEPT |
| MLW0 source map | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` row `MLW7 Optional External Capability Ingestion` | ACCEPT |
| T11E secondary scan | `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md` findings `T11E-F1` | ACCEPT |
| T10 cortex finding | `docs/corpus-intelligence/findings/legacy-cvf-add-cortex-hub.md` external capability bridge signal | ACCEPT |
| Current runtime source | External-asset governance source and routes exist at the paths verified below | ACCEPT |

## Decision / Baseline

Decision: MLW7 is authorized as a baseline and work-order candidate, not as a
runtime execution tranche.

Baseline facts at `2a21560e`:

- MLW1-MLW6 route-visible metadata/readout chain is closed bounded, but no
  external capability ingestion was implemented by that chain.
- The current repository already has an external-asset governance pipeline with
  `prepareExternalAssetGovernance`, `ExternalAssetWorkflowStatus`, prepare and
  register API routes, and blocked delegation rationale.
- MLW0 explicitly kept MLW7 optional pending operator decision and fresh GC-018.
- T11E classified external skill/provider ingestion as useful but optional and
  requiring design review.
- MLW7 must reuse and harden the existing external-asset governance surface
  before proposing any new surface.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MLW7 is a planned optional external capability ingestion tranche | EXISTS | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | line 102 | `MLW7` | T11 consolidated roadmap | ACCEPT |
| MLW7 was intentionally deferred until operator decision and fresh GC-018 | EXISTS | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | line 164 | `MLW7 Optional External Capability Ingestion` | MLW0 source verification map | ACCEPT |
| T11E external skill/provider ingestion is useful but optional | EXISTS | `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md` | lines 238, 257 | `T11E-F1` | T11E finding and learning disposition | ACCEPT |
| T10 cortex-hub carries external capability bridge value | EXISTS | `docs/corpus-intelligence/findings/legacy-cvf-add-cortex-hub.md` | line 80 | `external capability provider` | T10 finding artifact | ACCEPT |
| Current external-asset request owner exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | line 73 | `ExternalAssetGovernanceRequest` | external asset governance module | ACCEPT |
| Current external-asset workflow states exist | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | line 83 | `ExternalAssetWorkflowStatus` | external asset governance module | ACCEPT |
| Current external-asset preparation function exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | line 257 | `prepareExternalAssetGovernance` | external asset governance module | ACCEPT |
| Register route re-derives workflow status server-side | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.ts` | lines 16, 68-76 | `workflowStatus` | external-assets register route | ACCEPT |
| Existing governance result blocks delegation authority by default | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` | lines 410-411 | `blockedDelegationReasons` | external asset governance result builder | ACCEPT |

## New Doc-Only Fields

| New field or marker | Purpose | Not sourced from runtime? | Runtime claim blocked? |
| --- | --- | --- | --- |
| `MLW7_GC018_BASELINE` | Marker for this authorization baseline | Yes | Yes |
| `externalCapabilityIngestionCandidate` | Candidate work-order concept for mapping T10/T11 signals into existing external-asset governance | Yes | Yes |
| `runtimeExecutionAuthorized=false` | Explicit claim boundary for MLW7 planning | Yes | Yes |

## Required Work-Order Shape

The next MLW7 work order must include:

| Requirement | Required behavior |
| --- | --- |
| Source Verification Block | Verify every field against current external-asset governance source or canonical contract before implementation |
| Roadmap trace | Map MLW7 roadmap requirement to each proposed artifact |
| Candidate ingestion ledger | Classify Hermes/HF/cortex/deepagents/external-provider signals as accepted, deferred, or rejected with evidence pointers |
| Existing-surface reuse | Prefer `prepareExternalAssetGovernance` and existing routes before adding new runtime surfaces |
| No-execution invariant | Prove external capability intake does not execute, install, register authority, mutate policy, or authorize delegation by itself |
| Public boundary | Make no public catalog or marketplace claim unless public-sync is separately authorized |

## Knowledge Absorption Blind-Spot Control Block

- Prior absorption evidence resolved: T10 cortex-hub finding, T11 consolidated
  roadmap, MLW0 source verification map, T11E secondary scan.
- Detailed source files read: current external-asset governance source and route
  anchors were searched directly; this baseline does not rescan private legacy
  folders.
- Accepted value normalized into existing owner surface: external capability
  signals must first map to external-asset governance, not a new marketplace
  surface.
- Accept/defer/reject disposition: accept as work-order candidate; defer runtime
  implementation; reject any automatic install/execute scope for this baseline.
- Adversarial role review: risk is scope inflation into marketplace/runtime
  execution; boundary blocks package install, live proof, public-sync, and
  autonomous delegation.
- Blind-spot delta: semantic correctness of each Hermes/HF/cortex/deepagents
  pattern still requires the next work-order ledger; this GC-018 is not that
  ledger.
- Verdict: PARTIAL_WITH_LOW_RISK_REASON. The unresolved detail is intentionally
  assigned to the next source-verified work order and does not block opening the
  GC-018 baseline.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this file is an authorization baseline,
  not a fresh corpus inventory or completeness report.
- Corpus root: N/A with reason.
- Snapshot time: N/A with reason.
- Enumeration command: `rg --files --hidden --no-ignore docs/baselines/CVF_GC018_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_2026-06-05.md`
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
  on prior T10/T11/MLW0 artifacts and current source verification.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregation performed.
- Drift check: N/A with reason.
- Output traceability: source facts are cited in the Source Verification Block.
- Adversarial verification: scope-inflation risk reviewed in the blind-spot
  block.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Rescan Intelligence Hardening

- Original source artifact: `docs/corpus-intelligence/findings/legacy-cvf-add-cortex-hub.md`
- Predecessor intake artifact: `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md`
- Delta ledger status: BASELINE_ONLY_WITH_DECLARED_LIMITS
- Routing matrix status: BASELINE_ONLY_WITH_DECLARED_LIMITS
- Semantic sampling status: SOURCE_ANCHOR_SAMPLE_ONLY
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Item | Disposition | Reason |
| --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | MLW7 external capability ingestion remains optional | ACCEPT | Roadmap and MLW0 both require operator decision and fresh GC-018 |
| CHANGED_DISPOSITION | MLW7 moved from optional future candidate to GC-018 baseline | ACCEPT | Operator explicitly requested GC-018 for MLW7 |
| NEW_FINDING | Existing external-asset governance source provides a candidate owner surface | ACCEPT | `prepareExternalAssetGovernance` and external-assets routes exist |
| REMOVED_OR_REJECTED | Runtime install/execute marketplace interpretation | REJECT | Baseline blocks package install, external execution, public marketplace claims |

### Follow-Up Routing Matrix

| Routing lane | MLW7 item | Routed action |
| --- | --- | --- |
| DO_NOW | Source-verified MLW7 work order | Author only if operator asks to proceed after GC-018 |
| SEPARATE_RUNTIME_TRANCHE | Any external capability execution or live proof | Requires separate GC-018 and work order |
| STRATEGIC_OPERATOR_DECISION | Public external capability catalog or marketplace positioning | Operator decision required |
| OUT_OF_SCOPE | Package installation, third-party repo ingestion, autonomous delegation | Excluded from this baseline |
| RESOLVED_BY_DESIGN | Existing register route re-derives workflow status server-side | Preserve current server-side status derivation |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MLW7-S1 | MLW0 line 164 | MLW7 kept optional pending fresh GC-018 | ACCEPT | Could this baseline silently dispatch implementation? | PASS - status holds for work order |
| MLW7-S2 | T11E lines 238 and 257 | External skill/provider ingestion is useful but optional | ACCEPT | Could optional value become public marketplace claim? | PASS - public boundary blocks it |
| MLW7-S3 | external-assets register route lines 16 and 68-76 | Server re-derives workflow status | ACCEPT | Could client self-approval bypass intake? | PASS - existing route rejects non-registry-ready status |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| External capability ingestion can inflate into runtime/marketplace claims | OPERATOR_SCOPE_CLARITY_GAP | governance/control-plane learning | MACHINE_CHECK_CANDIDATE | MLW7 work order must include no-execution and public-boundary checks |

Promotion decision: TEMPLATE_UPDATED_BY_BASELINE. This GC-018 requires the next
work order to carry no-execution, no-install, and public-boundary assertions.

## Evidence / Verification

Required baseline verification before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 2a21560e --head HEAD
```

No live provider proof is required for this baseline because it does not assert
governed runtime behavior.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: MLW7 is private provenance planning only. No public-sync artifact,
public README/catalog claim, public marketplace claim, or hosted-readiness claim
is authorized by this baseline.

## Claim Boundary

This artifact proves only that MLW7 has a source-anchored GC-018 baseline. It
does not prove external capability runtime ingestion, execution safety,
marketplace readiness, package safety, public-readiness, production-readiness,
hosted-readiness, live provider behavior, or autonomous mutation.
