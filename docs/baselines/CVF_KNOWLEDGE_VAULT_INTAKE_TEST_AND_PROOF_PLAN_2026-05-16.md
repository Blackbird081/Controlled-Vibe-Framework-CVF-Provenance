Memory class: SUMMARY_RECORD

# CVF Knowledge Vault Intake Test And Proof Plan - 2026-05-16

Status: ACTIVE TEST PLAN.

## Purpose

Define the proof required to close Knowledge Vault Intake as a living CVF
Control Plane contract.

## Scope

Target package:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

Runtime files:

- `src/knowledge.vault.intake.contract.ts`
- `src/knowledge.vault.intake.types.ts`

Test file:

- `tests/knowledge.vault.intake.contract.test.ts`

## Source

Source folder:

- `.private_reference/legacy/CVF 16.5/tolaria/`

Predecessor evidence:

- `docs/baselines/CVF_GC018_KNOWLEDGE_VAULT_INTAKE_AUTHORIZATION_2026-05-16.md`
- `docs/baselines/CVF_ADR_KNOWLEDGE_VAULT_INTAKE_RUNTIME_OWNERSHIP_2026-05-16.md`
- `docs/baselines/CVF_KNOWLEDGE_VAULT_INTAKE_SOURCE_ADOPTION_MATRIX_2026-05-16.md`

## Decision

Use deterministic local tests as the proof source for this tranche.

No live provider proof is required because the claim is local Control Plane
classification, packaging, receipt, and gating behavior.

## Test Matrix

| Behavior | Required proof | Status |
|---|---|---|
| Markdown intake | normalized metadata, registry entry, provenance receipt | required |
| Raw-file boundary | incomplete metadata is not silently trusted | required |
| Restricted content | restricted assets are blocked from context eligibility | required |
| Knowledge graph | explicit frontmatter edges and derived wikilink edges | required |
| Context snapshot | included/excluded assets and receipt | required |
| Governance filters | review-required, superseded, conflicted, and over-budget exclusions | required |
| Drift signal | recommendation only, no auto-apply | required |
| Reinjection | allowed low-risk metadata proposal; forbidden mutation blocked | required |
| Tool gate | read allowed; direct raw write and missing receipt blocked | required |

## Evidence

Required evidence at closure:

- focused vitest result for `tests/knowledge.vault.intake.contract.test.ts`;
- Control Plane `npm run check`;
- governed file-size check after GC-023 split;
- full pre-push chain result;
- closure note preserving claim boundary.

## Commands

```bash
cd EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION
npm run check
npx vitest run tests/knowledge.vault.intake.contract.test.ts --config vitest.config.ts
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

## Claim Boundary

Passing this plan proves deterministic local Control Plane behavior. It does not
prove live provider governance, live vault file mutation, or live MCP execution.
