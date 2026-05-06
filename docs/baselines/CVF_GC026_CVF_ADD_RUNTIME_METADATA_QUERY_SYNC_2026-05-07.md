# CVF GC-026 Tracker Sync — CVF ADD Runtime Metadata Query

Memory class: SUMMARY_RECORD

Date: 2026-05-07

Status: RT8 METADATA QUERY FILTERS DELIVERED.

## Scope

RT8 makes CVF ADD runtime metadata queryable from the existing governed asset
registry GET route.

RT0-RT7 made the metadata runtime-readable, registry-persisted, and visible in
the operator UI. RT8 adds machine-facing filters so agents and tools can query
the registry by absorbed doctrine fields.

## Delivered Runtime Scope

Files changed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/asset-registry.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/asset-registry.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/register/route.test.ts`

New GET filters:

- `capability_class`
- `boundary_policy_class`
- `policy_authority=true|false`

## Boundary

RT8 is read-model/query only. It does not add new registry write authority,
does not execute external tools, does not widen provider behavior, and does not
claim live governance proof.

## Verification

Passed:

```bash
npx vitest run src/lib/cvf-add-runtime-doctrine.test.ts src/app/api/governance/external-assets/prepare/route.test.ts src/app/api/governance/external-assets/register/route.test.ts src/lib/server/asset-registry.test.ts
```

Result: 4 files passed, 63 tests passed.

Targeted ESLint passed for:

- `src/app/api/governance/external-assets/register/route.ts`
- `src/lib/server/asset-registry.ts`

