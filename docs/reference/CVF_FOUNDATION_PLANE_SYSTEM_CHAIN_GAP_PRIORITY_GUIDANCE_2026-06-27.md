# CVF Foundation Plane System-Chain Gap Priority Guidance

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference_guidance

Date: 2026-06-27

Owner: Codex

## Purpose

Record the operator-prioritized assessment that the next roadmap or tranche
must target CVF foundation-plane system-chain gaps before downstream use-case,
runtime, provider, or public-surface expansion.

This file is a routing reference for the next GC-018 and work order. It is not
itself a dispatch packet and does not authorize source, registry, runtime,
provider, public-sync, or generated-state mutation.

## Scope / Applies-To

This guidance applies to foundation-plane roadmap selection, GC-018 scoping,
work-order authoring, and tranche sequencing for CVF system-chain completion.

It applies when an agent or operator is deciding whether to open foundation
interlock, checker, runtime, use-case, provider, public-sync, or MPI follow-up
work after the MPI-T5 current-state reconciliation.

It does not apply as implementation authority for registry edits, runtime
changes, provider/live proof, generated state mutation, public export, or
downstream use-case work.

## Operator Direction

The operator direction on 2026-06-27 is:

1. Treat CVF foundation quality and plane-to-system completion as the highest
   priority.
2. Record the current assessment as a governed file so future agents do not
   reopen the same discussion from chat memory.
3. Use this assessment as the guide for the next roadmap or next tranche.
4. Prioritize closing the plane system-chain gaps below.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Master Architecture closure roadmap | `docs/roadmaps/CVF_MASTER_ARCHITECTURE_CLOSURE_ROADMAP_2026-04-05.md` | canonical architecture closure posture for Control, Execution, Governance, and Learning planes |
| Foundation Planes system completion roadmap | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | current FPC status, candidate chain, and FPC-T3-C04+C01 closure update |
| FPC-T1 audit matrix | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | plane-by-plane workflow-chain, interlock, and machine-check posture |
| FPC-T2 decision matrix | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | C01 through C05 interlock candidate evidence and dispositions |
| FPC-T2 completion | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | accepted decision that C01-C04 are proposal-only registry candidates and C05 required C01 first |
| FPC-T3 coverage plan | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | remaining checker/template candidate priorities C02, C03, C05, C06, C07 |
| FPC-T3-C04+C01 completion | `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md` | evidence that C04 template anchor and C01 epistemic process checker are implemented |
| System-loop interlock registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | current registered ACTIVE interlock connections |
| MPI-T5 current-state completion | `docs/reviews/CVF_MPI_T5_CURRENT_STATE_RECONCILIATION_COMPLETION_2026-06-27.md` | current memory-access checker reconciliation and no MPI-T6 runtime reopen boundary |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current next-move and parked-boundary routing |

No provider-specific memory file, chat transcript, external app source tree, or
uncited inference is source authority for this guidance.

## Assessment

The Master Architecture closure roadmap records the core planes as
closure-assessed. That does not mean every plane is already a connected,
interlocked, machine-checked workflow-system chain.

The FPC audit and routing matrices are the more precise current basis for
next-tranche selection: a plane can be architecturally closed and still lack a
system-loop interlock, a machine-check owner, or a claim-update path.

## Current Plane Status Summary

| Plane or lane | Current system-chain posture | Gap disposition |
|---|---|---|
| Governance Layer | `SYSTEM_CHAIN_MACHINE_CHECKED` for hook/checker enforcement | needs formal hook-chain-to-learning interlock visibility |
| Execution Plane | `SYSTEM_CHAIN_MACHINE_CHECKED` for ERH sub-loops | Model Gateway and Sandbox remain deferred; not the immediate priority unless separately authorized |
| Corpus / Scan / Extraction Plane | `SYSTEM_CHAIN_MACHINE_CHECKED` with registered interlocks | adequate for current FPC purposes |
| Public Evaluation / Export Boundary Plane | `SYSTEM_CHAIN_MACHINE_CHECKED` with registered interlock | adequate for current FPC purposes |
| Control Plane | `SYSTEM_CHAIN_STRUCTURAL_GUARDED` | needs formal Control/Governance hook-chain-to-learning interlock |
| Memory / Knowledge Plane | `SYSTEM_CHAIN_STRUCTURAL_GUARDED` | needs Memory-to-Learning and Memory-to-Retrieval interlocks; raw memory invariant should remain machine-check candidate |
| Learning Plane | partial system chain | evidence-to-truth and claim-update promotion remains proposal/structural unless C05 is registered and enforced |
| Evidence / Metadata Resolution Plane | partial system chain | evidence-to-claim-update interlock is now eligible for a narrow follow-up because FPC-T3-C04+C01 exists |
| Document Intelligence foundation lane | partial system chain | DIR/DICE-to-downstream-adapter eligibility interlock and DICE ownership checker remain pending |
| Use-case adapter layer | downstream boundary, not a CVF plane | Policy_Local and Document Translator remain separate fresh-GC-018 use cases after foundation routing gaps are handled |

## Priority Gap List

### P0 - System-Loop Interlock Registry Gap

Open the next roadmap or work order around source-verified registry planning
and, if authorized, registry edits for the currently accepted interlock
candidates:

| Candidate | Required direction | Current basis |
|---|---|---|
| FPC-T2-C01 | Control/Governance hook-chain enforcement loop to Learning/F2G intake | accepted as `ADD_INTERLOCK_ENTRY` proposal-only |
| FPC-T2-C02 | Memory consolidation output loop to Learning signal intake | accepted as `ADD_INTERLOCK_ENTRY` proposal-only |
| FPC-T2-C03 | Memory consolidation / knowledge-graph output loop to Retrieval / answer loop | accepted as `ADD_INTERLOCK_ENTRY` proposal-only |
| FPC-T2-C04 | DIR/DICE authorization gate output loop to downstream adapter eligibility | accepted as `ADD_INTERLOCK_ENTRY` proposal-only |
| FPC-T2-C05 | Evidence collection / worker-return / audit-finding loop to claim update / reviewer decision / learning intake | was `MACHINE_CHECK_FIRST`; FPC-T3-C04+C01 now satisfies the first prerequisite, so C05 is eligible for a narrow source-verified registry-entry decision |

The next tranche should not treat registry shapes in old matrices as already
applied. It must verify the current registry, current checker state, and current
FPC roadmap status before any edit.

### P1 - Machine-Check Coverage Gap

After or alongside P0, prioritize the remaining machine-check candidates that
turn structural plane posture into enforceable workflow-system posture:

| Candidate | Required direction | Why it matters |
|---|---|---|
| FPC-T3-C06 | memory `rawMemoryReleased=false` autorun check | protects Memory/Knowledge plane claim boundary and prevents raw-memory-release drift |
| FPC-T3-C02 | DICE machine-candidate checker | moves DIR/DICE invariants from focused tests into governance workflow visibility |
| FPC-T3-C05 | worker-return fast-gate epistemic fixture | lets no-commit workers catch epistemic packet gaps before reviewer intake |
| FPC-T3-C03 | interlock registry coverage checker extension | detects closed chains that produce downstream signals but lack interlock disposition; requires a stable expected-chain manifest first |

### P2 - Downstream Use-Case Restraint

Policy_Local, Document Translator, DICE runtime expansion, MPI-T6 runtime,
provider/live proof, public-sync, and Model Gateway/Sandbox runtime expansion
should not be selected ahead of P0/P1 unless the next GC-018 explicitly records
why a specific foundation gap is satisfied, inapplicable, or lower value.

## Next Roadmap Shape

The recommended next roadmap should be a foundation-system-chain gap closure
roadmap, not a runtime or use-case roadmap.

Minimum scope:

1. Re-read this guidance, the FPC roadmap, FPC-T1 matrix, FPC-T2 matrix and
   completion, FPC-T3-C04+C01 completion, and the live system-loop interlock
   registry.
2. Source-verify whether FPC-T2-C01 through C04 are still absent from the
   registry and whether their proposed upstream/downstream artifacts still
   exist.
3. Source-verify whether FPC-T2-C05 is now eligible after
   FPC-T3-C04+C01 and `governance/compat/check_epistemic_process_packet.py`.
4. Decide whether the next implementation tranche edits the registry directly,
   authors an expected-chain manifest first, or splits C01-C04 and C05 into two
   smaller work orders.
5. Preserve downstream boundaries: no use-case adapter work, no runtime
   provider proof, no MPI-T6 runtime, no public-sync, no generated state
   mutation except session sync after closure.

Recommended first work order candidate:

`FPC-SCG-T1 Foundation Plane System-Chain Interlock Registry Decision And Edit`

Recommended fallback if registry-edit scope is too broad:

`FPC-SCG-T0 Foundation Plane System-Chain Gap Closure Roadmap`

## Acceptance Criteria For The Next Tranche

The next tranche is correctly aligned only if it:

- starts from the FPC source surfaces above;
- lists the exact interlock candidates it will decide or edit;
- proves whether each candidate is currently absent, present, or superseded in
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- distinguishes architecture closure from workflow-system-chain completion;
- records why any non-gap runtime/use-case lane is not being selected;
- keeps all use-case, provider, runtime, public-sync, and MPI-T6 runtime work
  out of scope unless separately authorized.

## Not Authorized

This guidance does not authorize:

- editing the system-loop interlock registry;
- implementing FPC-T3-C02, C03, C05, or C06;
- opening MPI-T6 runtime work;
- opening Policy_Local or Document Translator source work;
- opening Model Gateway or Sandbox runtime expansion;
- running provider/live proof;
- changing generated session state except through a separate session-sync pass;
- public-sync or push.

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_NA_WITH_REASON: this is a
source-backed routing guidance artifact that records operator priority and
current governed source posture. It does not run a new empirical experiment,
provider proof, runtime test, or prediction-vs-result evaluation.

Expected Result / Prediction: N/A with reason: no empirical prediction is made.

Evidence Comparison Requirement: N/A with reason: source reads are used for
governed routing, not for a new measured comparison.

Contradiction Or Gap Disposition: Current contradiction resolved by distinction:
Master Architecture closure means plane-level architecture posture, while FPC
system-chain completion requires interlock and machine-check coverage.

Claim Update Requirement: This file updates the next-roadmap guidance claim:
the highest-value next tranche should close FPC system-chain gaps before
runtime or downstream use-case expansion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this guidance cites private provenance paths, active session state, and
internal roadmap/tranche identifiers. A public-safe summary would need separate
public-sync authorization and artifact review.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 foundation plane gap priority guidance |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` |
| Allowed scope source | operator instruction to record the assessment as next-roadmap guidance and prioritize the gaps |
| Before status evidence | HEAD `d172fe48`; worktree clean before patch |
| After status evidence | guidance file added; gates run before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | reference guidance only |
| Claim boundary | records next-roadmap priority; no registry edit, checker implementation, runtime/provider/live proof, public-sync, generated state mutation, use-case work, or MPI-T6 runtime work |
| Agent type | single-agent reference author |
| Invocation ID | `foundation-plane-system-chain-gap-priority-guidance-2026-06-27` |
| Expected manifest | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` |
| Actual changed set | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` |
| Manifest delta | MATCH |

## Claim Boundary

This file is guidance for selecting and scoping the next roadmap/tranche. It
does not make a runtime capability claim, does not change source or registry
behavior, and does not certify any plane as complete beyond the cited source
artifacts.
