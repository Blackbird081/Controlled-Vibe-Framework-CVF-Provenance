# CVF GC-018 - MLW0 Current Source Verification Map

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET

docType: gc018_baseline

Date: 2026-06-05

dispatchBaseHead: `a1a93ed4`

## Purpose

Authorize MLW0 as the mandatory first tranche of the CI1-T11 Memory/Learning
Absorption Consolidated Roadmap.

MLW0 maps the legacy memory/learning concepts surfaced in CI1-T11 scan packets
to current CVF runtime source files, schemas, routes, commands, tests, and
checkers. Every subsequent implementation tranche (MLW1–MLW6) depends on this
map to avoid guessing legacy field names, route symbols, or schema keys that may
have been renamed, moved, or never merged into the active source tree.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05 operator selected option A: open MLW0 Current Source Verification Map | ACCEPT |
| CI1-T11 consolidated roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` status `ROADMAP_READY_FOR_MLW0_SOURCE_VERIFICATION` | ACCEPT |
| CI1-T11 scan wave packet | `docs/audits/CVF_CI1_T11_MEMORY_LEARNING_RELATED_SCAN_WAVE_PACKET_2026-06-05.md` status `SCAN_WAVE_COMPLETE_PENDING_REVIEW` | ACCEPT |
| T11A–T11E deep scan packets | all five packets status `COMPLETE_PENDING_REVIEW` | ACCEPT |
| CI1-T10 cortex-hub packet | `docs/audits/CVF_CI1_T10_CORTEX_HUB_MEMORY_LEARNING_DEEP_SCAN_PACKET_2026-06-05.md` | ACCEPT as legacy boundary input |
| GC-051 Corpus Scan Registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |

## Source / Predecessor Evidence

| Predecessor | Evidence | MLW0 dependency |
| --- | --- | --- |
| CI1-T11 roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | defines MLW0 objectives and exit criteria |
| T11A packet | `docs/audits/CVF_CI1_T11A_LEARNING_PLANE_DEEP_SCAN_PACKET_2026-06-05.md` | Learning Plane truth/evaluation/reputation/adaptation legacy concepts |
| T11B packet | `docs/audits/CVF_CI1_T11B_MEMORY_KNOWLEDGE_STORE_DEEP_SCAN_PACKET_2026-06-05.md` | governed memory gateway, vault, provenance, reinjection, compilation concepts |
| T11C packet | `docs/audits/CVF_CI1_T11C_RAG_CONTEXT_CONTROL_DEEP_SCAN_PACKET_2026-06-05.md` | router/fusion/packager/profile/cache/capability context concepts |
| T11D packet | `docs/audits/CVF_CI1_T11D_EXECUTION_AUDIT_LEARNING_DEEP_SCAN_PACKET_2026-06-05.md` | execution continuity, planner trace, audit feedback concepts |
| T11E packet | `docs/audits/CVF_CI1_T11E_SECONDARY_RELATED_STRUCTURAL_SCAN_PACKET_2026-06-05.md` | secondary skill/provider/efficiency boundary signals |
| T11-F3 finding | CI1-T11 wave packet `Findings` table | legacy W7/runtime field names are unverified until source-verified |
| MKG7 memory plane | `docs/reviews/` MKG7 completion record | existing LPF memory runtime is the current ownership baseline |

## Legacy Spec Scan Block

- Registry read: `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- Legacy folders scanned: T11A–T11E cover all primary CI1-T11 roots; T10 covers cortex-hub
- Relevant source specs found: W7MemoryRecord, W7TraceRecord, W7ArtifactRecord,
  W7PlannerRecord, W7DecisionRecord, AgentLedger, MemoryGateway, ContextProfile,
  CapabilityRegistry, LearningSignalIntakeRecord mentioned across T11A-D packets
- Existing absorption evidence checked:
  - MKG1-MKG7: `docs/reviews/` — memory plane runtime implemented as LPF
  - KGR1: knowledge graph builder/store implemented
  - MKE1: memory enforcement E1/E2/E3 complete
  - LHW13: Memory Continuity Level Advisory connector spec
- Absorbed in this tranche: source-verification map only; no runtime implementation
- Explicitly deferred: all runtime implementation (MLW1–MLW8)
- Out of scope: public-sync, live proof, autonomous mutation
- Blindspot risk verdict: CLEAR

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_MLW0_SOURCE_VERIFICATION_MAP_ONLY

MLW0 is a documentation-only, source-analysis tranche. It produces a
Source Verification Map document that classifies legacy concepts as
ACCEPT (current symbol found), REJECT (no current equivalent), or
BLOCKED (legacy name only, no current source match). No runtime file,
route, test, or schema is modified by MLW0.

Risk ceiling: R1 (documentation analysis and cross-reference only).

## Scope

Allowed:

- reading current runtime source files to verify symbol existence;
- reading current schema, route, and test files;
- producing one Source Verification Map document with ACCEPT/REJECT/BLOCKED
  rows for each legacy concept from T11A–T11D packets;
- updating GC-051 corpus scan registry to record MLW0 as a cross-reference scan;
- authoring a MLW0 completion review;
- updating session state and front door with MLW0 closure.

Forbidden:

- modifying any runtime source file (`*.ts`, `*.py`, route files, test files);
- creating new runtime modules, routes, schemas, or checkers;
- claiming runtime behavior, live governance proof, public readiness,
  production readiness, or hosted readiness;
- public-sync;
- autonomous memory, learning, policy, provider, or prompt mutation;
- opening MLW1–MLW8 work orders without operator authorization.

## Worker Autonomy / No-Question Rule

The worker must complete allowed-scope remediation without escalating to the
operator. Routine gate failures inside the allowed scope must be repaired
and re-run. Operator escalation is required only for: scope expansion beyond
this work order, claim-boundary changes, HOLD release, risk-level changes,
public-sync, live/provider proof, secrets/quota, forbidden paths, or
destructive operations.

## Exit Criteria

MLW0 is closed when:

1. Source Verification Map document exists at the path named in the work order,
   with all T11A–T11D legacy concept rows classified as ACCEPT, REJECT, or
   BLOCKED with evidence.
2. Each ACCEPT row includes the current runtime path and verified symbol/field.
3. Each BLOCKED row includes the legacy name and explicit no-source-found note.
4. Tranche dependency order for MLW1–MLW8 is updated based on map findings.
5. Completion review exists and pre-closure autorun gate passes.
6. Session state and front door are updated with MLW0 closure.

## Evidence / Verification

Required dispatch verification:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base a1a93ed4 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base a1a93ed4 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base a1a93ed4 --head HEAD
```

Required pre-closure verification:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base a1a93ed4 --head HEAD
```

## Corpus Completeness And Report Integrity

- Corpus task class: GC-018_DISPATCH_BASELINE — source-verification analysis authorization; no new corpus scan initiated
- Corpus root: N/A — MLW0 reads existing CI1-T11 scan packets and current EXTENSIONS/ runtime source; no new root scanned
- Snapshot time: 2026-06-05
- Enumeration command: `rg --files --hidden --no-ignore EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` (worker runs in Phase 1; CI1-T11 wave already enumerated legacy roots)
- Manifest artifact or inline manifest: N/A — prior manifests: CI1-T11 wave packet `Corpus Wave Boundary` hash `98e0ba8bd575297832e35055aba638a2045973c4bcb92b102c2382619ee5ef10`
- Manifest hash: N/A_INHERITED_FROM_CI1_T11_WAVE
- Processing ledger artifact or inline ledger: N/A — file-level ledger produced by worker in Source Verification Map Phase 1 output
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: N/A — reconciliation produced by worker in Source Verification Map; prior CI1-T11 reconciliation: manifest=191; ledger_terminal=191; exclusions=1; unresolved=0
- Unresolved files: 0 (inherited from CI1-T11 wave; MLW0 adds no new corpus files)
- Declared exclusions: one `.pyc` in Knowledge Base_Palace (inherited from CI1-T11 wave)
- Unreadable or unsupported files: none beyond prior exclusion
- Aggregation check: N/A — no new file aggregation; MLW0 reads existing scan packets
- Drift check: PASS at baseline creation time
- Output traceability: worker Source Verification Map `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md`
- Adversarial verification: adversarial sampling is inherited from CI1-T11 wave packet samples CI1-T11-S1 through CI1-T11-S5; worker must source-verify each concept against live `rg` output
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Claim Boundary

This GC-018 authorizes source-analysis documentation only. It does not
authorize runtime implementation, route changes, schema changes, test creation,
live governance proof, public-sync, hosted readiness, production readiness,
public readiness, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MLW0 reads `.private_reference/legacy/` source concepts and current
private runtime source. No public-sync artifact is produced by MLW0.
