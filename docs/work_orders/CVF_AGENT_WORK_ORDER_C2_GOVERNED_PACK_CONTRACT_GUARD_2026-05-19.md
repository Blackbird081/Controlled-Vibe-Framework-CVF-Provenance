# CVF Agent Work Order — C2: Governed Pack Contract Guard

Memory class: SUMMARY_RECORD

Status: OPEN — awaiting second Reviewer rebuttal acceptance of V2 roadmap
and GC-018 filing before implementation begins.

GC-018 required: Yes — new enforcement surface.
GC-018 path: `docs/baselines/CVF_GC018_C2_GOVERNED_PACK_CONTRACT_GUARD_2026-05-19.md`

## Purpose

Create `check_governed_pack_contract.py` to enforce the 3-file contract
(Rules A–D) for every governed pack folder. Closes the governance gap where
pack folders could be added without required structure or content invariants.

## Authority Chain

V2 roadmap (`CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`) — C2
section. GC-018 must be filed and accepted before implementation begins.
Second Reviewer rebuttal must return no-blocking verdict.

## Agent Roles

- **Orchestrator** — files GC-018; dispatches work order; accepts completion packet.
- **Worker** — implements all tasks in governance/provenance repo; runs pre-flight
  before any code; files completion review upon closure.

## Scope

**Allowed scope:** Governance/provenance repo — guard script, policy file, test
file, hook-chain wiring for the 3-file pack contract (Rules A–D) only.

**Forbidden scope:** Runtime pack binding, execution semantics, provider lane
assignment, new pack content, public-sync repo edits under this WO.

## Required First Reads

1. `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C2
2. Three governed pack folders under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`
3. `docs/baselines/CVF_GC018_C2_GOVERNED_PACK_CONTRACT_GUARD_2026-05-19.md` (after filing)

## Write Ownership

Worker role owns all file creation under this work order. No modification of
existing pack files. Pre-flight must confirm guard does not already exist.

## Execution Plan

Task 1 (guard script) → Task 2 (policy file) → Task 3 (test file, must pass) →
Task 4 (hook-chain wiring, only after Task 3 passes). Do not wire before tests pass.

## Evidence Requirements

Evidence trace block in completion review: command → stdout → verdict for each
acceptance criterion. All 3 existing packs must show 0 violations in evidence.

## Review Gate

Orchestrator reviews completion packet. No closure without `test_all_existing_packs_pass`
evidence and hook-chain pass confirmed in evidence trace.

## Closure Checklist

- [ ] All 5 acceptance criteria verified with evidence
- [ ] Hook-chain and CI gate wired without breaking existing checks
- [ ] Completion review filed in `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- Any of the 3 expected pack folders is missing on pre-flight
- `check_governed_pack_contract.py` already exists (do not overwrite without authorization)
- Hook-chain wiring causes any existing guard to fail

## Target repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` — C2 section
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/` — 3 existing packs
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/workflow.spec.md` line 39 — `## Workflow` confirmed
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/` — template id sources

## Adjacent guards (must cite in policy file and GC-018)

- `check_template_skill_standard_guard_compat.py` — companion docs; does NOT validate pack 3-file contract
- `check_guard_contract_compat.py` — guard contract SDK; does NOT read governed pack folders

## Source-fidelity pre-flight (Worker role must run before writing any code)

```text
1. Confirm 3 pack folders exist:
   EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/
   EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/
   EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/

2. For each pack, confirm these 3 files exist:
   workflow.spec.md  execution.policy.json  receipt.schema.json

3. For each workflow.spec.md, confirm section heading is ## Workflow (not ## Steps)

4. For each execution.policy.json, confirm templateId field exists and
   its value appears as id: in some templates/*.ts file

5. For each receipt.schema.json, confirm stepTraces property exists

6. Confirm check_governed_pack_contract.py does NOT exist yet in governance/compat/
```

## Implementation tasks

### Task 1 — Guard script

Create `governance/compat/check_governed_pack_contract.py`.

```python
#!/usr/bin/env python3
"""CVF governed pack contract guard.

Validates that every governed pack folder contains the required 3-file
contract and that each file satisfies its content invariants.
"""
```

Pack discovery: scan
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`
for subdirectories.

Implement 4 rules exactly as specified in the V2 roadmap:

- Rule A: `workflow.spec.md`, `execution.policy.json`, `receipt.schema.json` present
- Rule B: `execution.policy.json` valid JSON + `templateId` found in `templates/*.ts`
- Rule C: `workflow.spec.md` contains `## Workflow` section with at least one numbered item
- Rule D: `receipt.schema.json` valid JSON Schema + `stepTraces` property anywhere in tree

Output: `--json` flag emits JSON report; default prints human-readable.
`--enforce` exits non-zero on any violation.

### Task 2 — Policy file

Create `governance/toolkit/05_OPERATION/CVF_GOVERNED_PACK_CONTRACT_GUARD.md`.

Required sections: Purpose, Rule (4 rules), Enforcement Surface, Adjacent
guards cited (C2 adjacent guards listed above), Related Artifacts, Final Clause.

### Task 3 — Test file

Create `governance/compat/test_check_governed_pack_contract.py`.

Required test cases:

- `test_all_existing_packs_pass` — run guard against all 3 real packs → 0 violations
- `test_missing_workflow_spec` — synthetic pack without `workflow.spec.md` → Rule A violation
- `test_missing_templateid` — synthetic pack with `templateId` not in templates → Rule B violation
- `test_missing_workflow_section` — `workflow.spec.md` without `## Workflow` → Rule C violation
- `test_missing_steptraces` — `receipt.schema.json` without `stepTraces` → Rule D violation

Use temporary directories for synthetic broken packs. Do not modify real pack files.

### Task 4 — Hook-chain wiring

Add `check_governed_pack_contract.py` to:

1. `governance/compat/run_local_governance_hook_chain.py` — as a step in the pre-commit hook
2. `scripts/run_cvf_static_ci_gate.py` — as a check in the static CI gate

Add only after Task 3 tests pass locally. Wire-in must not break existing
hook-chain or CI gate behavior.

## Acceptance criteria

- [ ] All 3 existing packs produce 0 violations
- [ ] `test_missing_workflow_spec` → Rule A violation detected
- [ ] `test_missing_templateid` → Rule B violation detected
- [ ] `test_missing_workflow_section` → Rule C violation detected
- [ ] `test_missing_steptraces` → Rule D violation detected
- [ ] Policy file present with all required sections
- [ ] Hook-chain wiring added; `run_local_governance_hook_chain.py --hook pre-commit` passes
- [ ] `scripts/run_cvf_static_ci_gate.py` includes guard; static CI gate passes

## Completion packet

File `docs/reviews/CVF_C2_GOVERNED_PACK_CONTRACT_GUARD_COMPLETION_2026-05-19.md`
with evidence trace (command → result → verdict per acceptance criterion).

Update V10 handoff HEAD SHA per GC-020 after commit.

## Claim boundary

This work order covers only the governed pack 3-file contract validation
(Rules A–D). It does not validate runtime pack binding, execution behavior,
or provider lane assignment. It does not add new pack files or modify
existing pack content.
