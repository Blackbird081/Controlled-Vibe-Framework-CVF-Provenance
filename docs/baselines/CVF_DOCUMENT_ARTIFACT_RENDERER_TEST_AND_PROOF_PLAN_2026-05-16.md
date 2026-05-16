Memory class: GOVERNANCE_BASELINE

# CVF Document Artifact Renderer Test And Proof Plan - 2026-05-16

Status: active proof plan for bounded runtime adoption.

## Purpose

Define the proof required to close Document Artifact Renderer as living CVF
knowledge.

## Scope

Required proof:

- focused Vitest tests for the new contract;
- package typecheck;
- governed file-size guard;
- full pre-push governance chain before push.

## Source

The proof plan comes from the CVF 16.5 renderer verification checklist and CVF
runtime adoption norms.

## Test Matrix

| Area | Required proof |
|---|---|
| Metadata | artifact id, source path/hash, renderer policy, root authority |
| Governance visibility | risk, approval, evidence state, failed checks |
| Claims boundary | no evidence invention and limitation remains visible |
| Component catalog | approved components selected, forbidden widgets fail |
| Security | remote script and credential/tracking patterns fail |
| Template | single-file HTML contains metadata, claims, content, verification, provenance |
| Preview | sandbox preview note is explicit when requested |
| Determinism | same input/timestamp gives same artifact identity |

## Baseline

No live provider proof is required because the contract is deterministic and
does not assert live provider enforcement.

## Evidence

Evidence will be recorded in the closure packet.

## Verification

Commands:

```bash
cd EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION
npm run check
npx vitest run tests/document.artifact.renderer.contract.test.ts --config vitest.config.ts
```

Repository-level checks:

```bash
python governance/compat/check_governed_file_size.py
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

## Claim Boundary

Passing this plan supports a `runtime-owned` claim only. It does not support
claims about live renderer UI, screenshot fidelity, or generated benchmark
evidence.
