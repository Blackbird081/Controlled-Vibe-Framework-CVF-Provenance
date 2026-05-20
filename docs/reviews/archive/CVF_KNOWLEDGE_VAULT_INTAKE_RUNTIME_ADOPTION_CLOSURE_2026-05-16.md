Memory class: FULL_RECORD

# CVF Knowledge Vault Intake Runtime Adoption Closure - 2026-05-16

Status: CLOSED - RUNTIME-OWNED.

## Purpose

Close the Knowledge Vault Intake absorption tranche and record what is now alive
inside CVF.

## Target And Source

Target:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

Source:

- `.private_reference/legacy/CVF 16.5/tolaria/`

## Scope And Methodology

Method:

- use `tolaria` markdown-vault doctrine as source pattern;
- implement a CVF-owned deterministic Control Plane contract;
- split types to satisfy GC-023 without an exception;
- test intake, graph, context snapshot, drift, reinjection, and tool gating.

Structural review:

- `docs/reviews/CVF_GC019_KNOWLEDGE_VAULT_INTAKE_STRUCTURAL_CHANGE_REVIEW_2026-05-16.md`

## Findings And Position

Position: Knowledge Vault Intake is now a living CVF runtime primitive.

Delivered:

- `KnowledgeVaultIntakeContract`;
- normalized metadata and registry candidate;
- provenance receipts;
- graph view with explicit and derived edges;
- governed context snapshot with exclusions;
- drift signal with `autoApplyAllowed: false`;
- governed reinjection proposal;
- MCP-style knowledge tool gate.

## Risk And Corrective Action

Residual risk:

- no live file I/O is wired;
- no full YAML parser dependency is introduced;
- no live MCP execution is claimed.

Corrective action:

- keep the claim at `runtime-owned`;
- require a future GC-018 and live proof for live file mutation, live MCP
  execution, or user-facing vault UI.

## Verification

Executed:

```bash
cd EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION
npm run check
npx vitest run tests/knowledge.vault.intake.contract.test.ts --config vitest.config.ts
npm run test -- --run
python governance/compat/check_governed_file_size.py
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

Result:

- Control Plane typecheck PASS;
- focused Knowledge Vault Intake vitest PASS, 1 file / 10 tests;
- full Control Plane vitest PASS, 123 files / 3390 tests;
- governed file-size PASS after GC-023 split.
- full pre-push chain PASS after adding `AGENT_HANDOFF_V7_2026-05-16.md` to
  the root file exposure registry.

## Decision And Recommendation

Decision: close Knowledge Vault Intake as `runtime-owned`.

Recommendation: next absorption should choose Document Artifact Renderer if the
next product need is public evidence presentation, or OpenSpec Change Adapter if
the next governance need is proposal/delta/task workflow mapping.

## Claim Boundary

This closure does not claim live vault file mutation, autonomous memory, raw file
agent context, or live MCP knowledge tool execution.

## Final Clause

The Knowledge Vault Intake knowledge is no longer only reviewed; it is now an
executable CVF Control Plane contract with tests.
