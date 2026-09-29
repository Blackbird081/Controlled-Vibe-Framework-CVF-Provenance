# CVF Semantic Convergence Control - Folder Index

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-08-31

**Applies to:** any dispatcher, worker, reviewer, or closer authoring or
validating a Semantic Convergence And Escalation Control (SCEC) block on a
governed baseline, work order, or worker return.

## Purpose

This folder is the canonical front door for the Semantic Convergence And
Escalation Control (SCEC) foundation. SCEC constrains whether a declared
problem chain has enough evidence to continue, must consolidate into one
integrated root contract, or must stop for architectural reassessment. It does
not inspect private reasoning, score semantic truth, or prescribe how an agent
works.

## Scope / Applies To

Applies to any CVF-governed artifact that declares an SCEC block. Every new
or changed governed work order and worker return after activation must carry
exactly one `cvf.semanticConvergenceControl.v1` block. Does not apply to
product/runtime source, provider/live execution, or public-sync artifacts.

## Canonical Standard

`docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

This file defines the exact block schema, activation rule, set-algebra
invariants, escalation triggers, claim-to-proof mapping, and claim boundary.
All other surfaces route to it; they do not restate its semantics.

## Machine Surfaces

| Surface | Path |
|---|---|
| Fail-closed checker | `governance/compat/check_semantic_convergence_control.py` |
| Focused unit tests | `governance/compat/test_check_semantic_convergence_control.py` |
| Historical regression fixture | `governance/compat/fixtures/semantic_convergence_control/gc010_t1j_r1_r3_replay.json` |
| Shared autorun binding | `governance/compat/agent_autorun_command_catalog.py` (`_common_commands`) |
| Local hook bindings | `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` |
| Dispatch scaffold emission | `governance/compat/build_dispatch_packet_scaffold.py` |
| Worker-return scaffold emission | `governance/compat/build_worker_return_skeleton_scaffold.py`; `governance/compat/run_worker_return_scaffold.py` |

## Related Learning Record

`docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md` records
the repeated defect class this foundation answers: local document gates
passing while a declared problem boundary kept moving across the GC-010
T1J-R1-through-R3 chain.

## Orientation Routing

`docs/reference/guard_orientation/README.md` and
`docs/reference/work_order_template/README.md` route dispatchers and workers
to this folder; they do not duplicate the schema, invariants, or proof
mapping defined here.

## Claim Boundary

This index is a navigation pointer only. It does not implement enforcement,
does not claim semantic-truth scoring, and does not authorize product/runtime,
provider/live, public-sync, or deployment behavior. The canonical standard and
checker in this folder are the enforcement authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation reference. Public export, if
ever desired, requires a separate reviewed public-sync batch.
