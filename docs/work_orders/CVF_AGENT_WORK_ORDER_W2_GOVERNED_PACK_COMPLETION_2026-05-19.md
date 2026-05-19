# CVF Agent Work Order — W2: Governed-Pack Completion

Memory class: SUMMARY_RECORD

Status: OPEN

GC-018 required: Yes — new TypeScript governance artifact class introduced.
GC-018 path: `docs/baselines/CVF_GC018_W2_GOVERNED_PACK_COMPLETION_2026-05-19.md`

## Purpose

Complete the 3 existing governed packs (`strategy_analysis`, `documentation`,
`app_builder_complete`) that already have `execution.policy.json`,
`receipt.schema.json`, and `workflow.spec.md` — add the missing
`failure-recovery.ts` to each pack and create a typed TypeScript registry
(`WorkflowPackRegistry` interface + `getGovernedPack(templateId)` loader in
`governed-packs/index.ts`).

Closes: Review CVF Problem B (workflow pack governance foundation — per-slice).

## Authority Chain

`docs/roadmaps/CVF_PHASE3_REVIEW_CLOSURE_ROADMAP_V2_2026-05-19.md` — W2 section.
GC-018 filed and AUTHORIZED at:
`docs/baselines/CVF_GC018_W2_GOVERNED_PACK_COMPLETION_2026-05-19.md`

Worker must not begin implementation without confirming GC-018 is AUTHORIZED.

## Agent Roles

- **Orchestrator** — filed GC-018; dispatches work order; accepts completion packet.
- **Worker** — implements all tasks in cvf-web lib only; runs pre-flight before
  any code; files completion review upon closure.

## Scope

**Files Worker may CREATE:**

- `cvf-web/src/types/workflow-pack.ts` (≤ 60 lines)
- `cvf-web/src/lib/governed-packs/strategy_analysis/failure-recovery.ts` (≤ 50 lines)
- `cvf-web/src/lib/governed-packs/documentation/failure-recovery.ts` (≤ 50 lines)
- `cvf-web/src/lib/governed-packs/app_builder_complete/failure-recovery.ts` (≤ 50 lines)
- `cvf-web/src/lib/governed-packs/index.ts` (≤ 80 lines)
- `cvf-web/src/lib/governed-packs/index.test.ts` (≤ 100 lines)

**Files Worker must NOT touch:**

- `governed-packs/strategy_analysis/execution.policy.json` — READ ONLY
- `governed-packs/strategy_analysis/receipt.schema.json` — READ ONLY
- `governed-packs/strategy_analysis/workflow.spec.md` — READ ONLY
- `governed-packs/documentation/execution.policy.json` — READ ONLY
- `governed-packs/documentation/receipt.schema.json` — READ ONLY
- `governed-packs/documentation/workflow.spec.md` — READ ONLY
- `governed-packs/app_builder_complete/execution.policy.json` — READ ONLY
- `governed-packs/app_builder_complete/receipt.schema.json` — READ ONLY
- `governed-packs/app_builder_complete/workflow.spec.md` — READ ONLY
- `src/app/api/execute/route.ts` — no route change authorized
- `src/lib/execute-role-resolver.ts` — no enforcement surface change
- Any file outside `cvf-web/src/lib/governed-packs/` and `cvf-web/src/types/`

## Write Ownership

Worker owns: `workflow-pack.ts` types, 3 `failure-recovery.ts` files, `index.ts` registry, `index.test.ts`. No other files.

## Required First Reads

1. `cvf-web/src/lib/governed-packs/strategy_analysis/execution.policy.json` — read `packId` field
2. `cvf-web/src/lib/governed-packs/documentation/execution.policy.json` — read `packId` field
3. `cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json` — read `packId` field
4. `cvf-web/src/lib/governed-packs/strategy_analysis/workflow.spec.md` — read pack name/purpose
5. GC-018 baseline: `docs/baselines/CVF_GC018_W2_GOVERNED_PACK_COMPLETION_2026-05-19.md`
6. This work order — done criteria and invariants

## Source-Fidelity Pre-Flight (Worker must verify before writing)

```text
1. Confirm strategy_analysis/execution.policy.json exists — read packId value
2. Confirm documentation/execution.policy.json exists — read packId value
3. Confirm app_builder_complete/execution.policy.json exists — read packId value
4. Confirm NO failure-recovery.ts exists in any of the 3 pack dirs
5. Confirm NO governed-packs/index.ts exists
6. Confirm NO WorkflowPackRegistry type exists in cvf-web/src/types/
7. Confirm npm run build currently passes (baseline before changes)
```

## Execution Plan

Task 1 → Task 2 → Task 3 → Task 4 → Task 5 → Task 6 in sequence.

### Task 1 — `cvf-web/src/types/workflow-pack.ts`

Define the shared type interfaces:

```typescript
export interface WorkflowPackRef {
  packId: string;
  version: string;
}

export interface FailureRecoveryStep {
  step: number;
  action: string;
  escalate?: boolean;
}

export interface FailureRecoveryPolicy {
  packId: string;
  recoverySteps: FailureRecoveryStep[];
  escalationPath: string;
}

export interface WorkflowPackRegistry {
  packId: string;
  templateId: string;
  version: string;
  specPath: string;
  policyPath: string;
  receiptSchemaPath: string;
  failureRecovery: FailureRecoveryPolicy;
}
```

File must be ≤ 60 lines. No imports from cvf-web internal lib (types only).

### Task 2 — `strategy_analysis/failure-recovery.ts`

```typescript
import type { FailureRecoveryPolicy } from '../../../../types/workflow-pack';

export const strategyAnalysisFailureRecovery: FailureRecoveryPolicy = {
  packId: '<packId from execution.policy.json>',
  recoverySteps: [
    { step: 1, action: 'Retry with reduced context window' },
    { step: 2, action: 'Fall back to structured template output' },
    { step: 3, action: 'Emit governance receipt with decision=degraded', escalate: true },
  ],
  escalationPath: 'OPERATOR review required — strategy analysis pack failed after 3 recovery steps',
};
```

File must be ≤ 50 lines. `packId` must match the value read from `execution.policy.json`.

### Task 3 — `documentation/failure-recovery.ts`

Same pattern as Task 2. `packId` from `documentation/execution.policy.json`.

```typescript
export const documentationFailureRecovery: FailureRecoveryPolicy = {
  packId: '<packId from execution.policy.json>',
  recoverySteps: [
    { step: 1, action: 'Retry with simplified output schema' },
    { step: 2, action: 'Emit partial documentation artifact with coverage annotation' },
    { step: 3, action: 'Emit governance receipt with decision=degraded', escalate: true },
  ],
  escalationPath: 'OPERATOR review required — documentation pack failed after 3 recovery steps',
};
```

### Task 4 — `app_builder_complete/failure-recovery.ts`

Same pattern as Task 2. `packId` from `app_builder_complete/execution.policy.json`.

```typescript
export const appBuilderFailureRecovery: FailureRecoveryPolicy = {
  packId: '<packId from execution.policy.json>',
  recoverySteps: [
    { step: 1, action: 'Retry with minimal spec output (summary only)' },
    { step: 2, action: 'Emit partial app spec with missing sections marked' },
    { step: 3, action: 'Emit governance receipt with decision=degraded', escalate: true },
  ],
  escalationPath: 'OPERATOR review required — app builder pack failed after 3 recovery steps',
};
```

### Task 5 — `governed-packs/index.ts`

```typescript
import type { WorkflowPackRegistry } from '../../../types/workflow-pack';
import { strategyAnalysisFailureRecovery } from './strategy_analysis/failure-recovery';
import { documentationFailureRecovery } from './documentation/failure-recovery';
import { appBuilderFailureRecovery } from './app_builder_complete/failure-recovery';

export type { WorkflowPackRegistry } from '../../../types/workflow-pack';
export type { FailureRecoveryPolicy, FailureRecoveryStep, WorkflowPackRef } from '../../../types/workflow-pack';

const GOVERNED_PACK_REGISTRY: WorkflowPackRegistry[] = [
  {
    packId: strategyAnalysisFailureRecovery.packId,
    templateId: 'strategy_analysis',
    version: '1.0.0',
    specPath: './strategy_analysis/workflow.spec.md',
    policyPath: './strategy_analysis/execution.policy.json',
    receiptSchemaPath: './strategy_analysis/receipt.schema.json',
    failureRecovery: strategyAnalysisFailureRecovery,
  },
  {
    packId: documentationFailureRecovery.packId,
    templateId: 'documentation',
    version: '1.0.0',
    specPath: './documentation/workflow.spec.md',
    policyPath: './documentation/execution.policy.json',
    receiptSchemaPath: './documentation/receipt.schema.json',
    failureRecovery: documentationFailureRecovery,
  },
  {
    packId: appBuilderFailureRecovery.packId,
    templateId: 'app_builder_complete',
    version: '1.0.0',
    specPath: './app_builder_complete/workflow.spec.md',
    policyPath: './app_builder_complete/execution.policy.json',
    receiptSchemaPath: './app_builder_complete/receipt.schema.json',
    failureRecovery: appBuilderFailureRecovery,
  },
];

export function getGovernedPack(templateId: string): WorkflowPackRegistry | undefined {
  return GOVERNED_PACK_REGISTRY.find((pack) => pack.templateId === templateId);
}

export { strategyAnalysisFailureRecovery, documentationFailureRecovery, appBuilderFailureRecovery };
```

File must be ≤ 80 lines. No circular imports — pack subdirs must not import from `index.ts`.

### Task 6 — `governed-packs/index.test.ts`

```typescript
import { describe, expect, it } from 'vitest';
import { getGovernedPack, strategyAnalysisFailureRecovery,
         documentationFailureRecovery, appBuilderFailureRecovery } from './index';

describe('governed-packs registry', () => {
  it('returns strategy_analysis pack by templateId', () => { ... });
  it('returns documentation pack by templateId', () => { ... });
  it('returns app_builder_complete pack by templateId', () => { ... });
  it('returns undefined for unknown templateId', () => {
    expect(getGovernedPack('unknown_template')).toBeUndefined();
  });
  it('all packs have non-empty recoverySteps', () => {
    [strategyAnalysisFailureRecovery, documentationFailureRecovery, appBuilderFailureRecovery]
      .forEach((policy) => {
        expect(policy.recoverySteps.length).toBeGreaterThan(0);
        expect(policy.escalationPath.length).toBeGreaterThan(0);
      });
  });
  it('all packs have matching packId in registry entry', () => { ... });
});
```

File must be ≤ 100 lines. All tests must PASS.

## Acceptance Criteria

- [ ] `cvf-web/src/types/workflow-pack.ts` created (≤ 60 lines) with `WorkflowPackRef`, `WorkflowPackRegistry`, `FailureRecoveryStep`, `FailureRecoveryPolicy`
- [ ] `strategy_analysis/failure-recovery.ts` created (≤ 50 lines), `packId` matches `execution.policy.json`
- [ ] `documentation/failure-recovery.ts` created (≤ 50 lines), `packId` matches `execution.policy.json`
- [ ] `app_builder_complete/failure-recovery.ts` created (≤ 50 lines), `packId` matches `execution.policy.json`
- [ ] `governed-packs/index.ts` created (≤ 80 lines), exports `getGovernedPack`, all 3 failure-recovery policies
- [ ] `governed-packs/index.test.ts` created (≤ 100 lines), all tests PASS
- [ ] `npm run build` PASS — no type errors
- [ ] `npm run test:run -- src/lib/governed-packs/index.test.ts` PASS
- [ ] Existing JSON/MD artifacts unmodified — `git diff` shows no changes to `.json` or `.spec.md` files in governed-packs

## Evidence Requirements

Completion review must include:

1. `npm run test:run -- src/lib/governed-packs/index.test.ts` — all tests PASS
2. `npm run build` — PASS
3. Line count for each new file (must be within limits)
4. `git diff --name-only` confirming no JSON/MD pack artifacts were modified
5. `packId` cross-check: confirm each failure-recovery.ts `packId` matches the value in the corresponding `execution.policy.json`

## Review Gate

Orchestrator reviews completion packet. No closure without:

- All 6 new files created and within line limits
- `npm run build` PASS
- `npm run test:run -- src/lib/governed-packs/index.test.ts` PASS
- `git diff --name-only` confirms no JSON/MD pack artifacts modified
- `packId` cross-check confirmed for all 3 failure-recovery files

## Closure Checklist

- [ ] GC-018 filed and AUTHORIZED before implementation
- [ ] `cvf-web/src/types/workflow-pack.ts` created ≤ 60 lines
- [ ] `strategy_analysis/failure-recovery.ts` created ≤ 50 lines, packId confirmed
- [ ] `documentation/failure-recovery.ts` created ≤ 50 lines, packId confirmed
- [ ] `app_builder_complete/failure-recovery.ts` created ≤ 50 lines, packId confirmed
- [ ] `governed-packs/index.ts` created ≤ 80 lines
- [ ] `governed-packs/index.test.ts` created ≤ 100 lines, all tests PASS
- [ ] `npm run build` PASS
- [ ] Existing JSON/MD artifacts NOT modified (git diff confirmed)
- [ ] Completion review filed in CVF `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- Any new file would exceed its line limit — report and stop
- `execution.policy.json` does not contain a `packId` field — source has changed; report
- `npm run build` fails after type addition — report type error and stop
- Circular import detected between `index.ts` and any pack subdir — restructure before proceeding

## Target Repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/` and
`cvf-web/src/types/` only.

## Claim Boundary

W2 covers TypeScript governance artifact completion for 3 existing governed packs.
It does not modify existing JSON/MD artifacts, change route or enforcement surfaces,
add provider execution, or touch any memory policy contracts.
