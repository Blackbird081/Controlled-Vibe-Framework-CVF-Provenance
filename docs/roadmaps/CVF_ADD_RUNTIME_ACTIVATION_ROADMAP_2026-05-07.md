# CVF ADD Runtime Activation Roadmap

Memory class: SUMMARY_RECORD

Status: RT0-RT8 RUNTIME ACTIVATION DELIVERED.

Date: 2026-05-07

## Purpose

This roadmap defines how the CVF ADD absorbed doctrine should become live CVF
behavior after official docs absorption.

Docs absorption is complete. Runtime activation must be narrow, owner-bound,
and evidence-bound.

## Preconditions

- Official docs absorption complete:
  - `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md`
  - `docs/reference/CVF_BOUNDARY_FIRST_GOVERNANCE_DOCTRINE_2026-05-07.md`
  - `docs/reference/CVF_GOVERNED_CONTEXT_PROFILE_METADATA_DOCTRINE_2026-05-07.md`
  - `docs/reference/CVF_AGENT_CONTINUITY_AND_DELEGATION_DOCTRINE_2026-05-07.md`
  - `docs/reference/CVF_SCOPED_KNOWLEDGE_PROVIDER_BOUNDARY_DOCTRINE_2026-05-07.md`
- `AGENT_HANDOFF.md` reflects docs absorption status.
- No runtime change is started from private `REVIEW FOLDER` material.

## Runtime Phase RT0 — Owner Surface Audit

Goal: identify exact code surfaces before changing behavior.

Status: DELIVERED 2026-05-07.

Candidate surfaces:

- external asset/governed registry code;
- policy/risk classification code;
- context builder / knowledge injection code;
- execution continuity and handoff-related helper code;
- provider/tool adapter boundaries;
- W7/evidence receipt schema.

Deliverable:

- runtime owner map with files, tests, and claim boundaries.

Delivered surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts`

## Runtime Phase RT1 — Governed Capability Intake Record

Goal: add a small runtime-readable doctrine/record shape for capability intake
without broadening execution permissions.

Status: DELIVERED 2026-05-07.

Expected behavior:

- record capability provenance, class, owner, risk, sandbox posture, evidence
  requirement, and evaluation state;
- reject or defer candidates without owner binding;
- do not execute external tools by default.

Proof:

- unit tests for record validation;
- no live provider proof unless connected to governance behavior claims.

Delivered files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cvf-add-runtime-doctrine.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cvf-add-runtime-doctrine.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/external-assets/prepare/route.test.ts`

## Runtime Phase RT2 — Boundary-First Governance Metadata

Goal: expose policy class metadata for hard prohibition, soft constraint,
communication policy, and restricted execution path.

Status: DELIVERED 2026-05-07.

Expected behavior:

- policy decisions can carry class metadata;
- no policy weakening;
- no claim of enforcement unless live proof is added.

Proof:

- unit tests for policy class serialization;
- live-governance proof if `/api/execute` behavior changes.

Delivered behavior:

- `prepareExternalAssetGovernance()` now returns `boundaryFirstGovernance`
  with policy class, required agent behavior, operator-decision flag, and W7
  candidate signals.

## Runtime Phase RT3 — Context Profile Metadata

Goal: allow advisory context profile metadata to assist context packaging.

Status: DELIVERED 2026-05-07.

Expected behavior:

- profile fields remain advisory;
- existing owners retain authority;
- hidden memory writes are blocked.

Proof:

- unit tests for profile validation and owner binding.

Delivered behavior:

- `prepareExternalAssetGovernance()` now returns `governedContextProfile`
  with `advisoryOnly: true`.

## Runtime Phase RT4 — Continuity / Delegation Record

Goal: make handoff and delegated worker continuity more structured.

Status: DELIVERED 2026-05-07.

Expected behavior:

- phase completion records include canonical artifacts, verification, blockers,
  and next phase;
- worker/delegation records remain bounded and do not grant execution authority.

Proof:

- handoff guard compatibility check;
- unit/static tests if helper code is added.

Delivered behavior:

- `prepareExternalAssetGovernance()` now returns `continuityDelegation`
  with checkpoint/handoff metadata and delegation blocked by default.

## Runtime Phase RT5 — Scoped Knowledge Provider Boundary

Goal: make knowledge-provider scope and provenance explicit where indexed or
graph-like knowledge enters context.

Status: DELIVERED 2026-05-07.

Expected behavior:

- provider metadata includes scope, freshness, confidence, source class, and
  `policy_authority: false`;
- private/ignored sources are not promoted into public runtime context.

Proof:

- unit tests for metadata and filtering.

Delivered behavior:

- `prepareExternalAssetGovernance()` now returns `scopedKnowledgeProvider`
  with `policyAuthority: false`.

## Release Proof Rule

If any runtime phase changes governance behavior, the release-quality proof
command is required:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Docs-only or static-schema changes may use narrower tests, but must not claim
live governance behavior.

## RT0-RT5 Verification Sync

Sync record:

- `docs/baselines/CVF_GC026_CVF_ADD_RUNTIME_ACTIVATION_SYNC_2026-05-07.md`

## Runtime Phase RT6 — Registry Persistence

Status: DELIVERED 2026-05-07.

Goal: persist CVF ADD runtime metadata after prepare-time derivation so the
governed asset registry can return the absorbed doctrine record later.

Delivered behavior:

- `registerAsset()` accepts and stores:
  - `governedCapability`
  - `boundaryFirstGovernance`
  - `governedContextProfile`
  - `continuityDelegation`
  - `scopedKnowledgeProvider`
- `/api/governance/external-assets/register` passes the server-derived metadata
  from `prepareExternalAssetGovernance()` into the append-only registry entry.
- GET registry/list/detail paths return the metadata as part of the entry.

Verification sync:

- `docs/baselines/CVF_GC026_CVF_ADD_RUNTIME_REGISTRY_PERSISTENCE_SYNC_2026-05-07.md`

## Runtime Phase RT7 — Operator/UI Readout

Status: DELIVERED 2026-05-07.

Goal: expose the persisted CVF ADD runtime metadata in the existing External
Asset Governance UI.

Delivered behavior:

- Prepare result shows `CVF ADD Runtime Readout` after governance pipeline
  execution.
- Registry entries show the same readout after registration.
- The readout surfaces capability, boundary, W7 candidates, context profile,
  continuity/delegation state, and scoped knowledge authority.
- `policyAuthority: false` is visible as `Context only`.

Verification sync:

- `docs/baselines/CVF_GC026_CVF_ADD_RUNTIME_UI_READOUT_SYNC_2026-05-07.md`

## Runtime Phase RT8 — Metadata Query Filters

Status: DELIVERED 2026-05-07.

Goal: make the persisted CVF ADD runtime metadata machine-queryable through the
existing governed registry GET route.

Delivered behavior:

- `/api/governance/external-assets/register` GET accepts:
  - `capability_class`
  - `boundary_policy_class`
  - `policy_authority=true|false`
- `filterRegistryEntries()` can filter entries by governed capability class,
  boundary policy class, and scoped knowledge provider policy authority.
- Existing status/source/type filters remain unchanged and can be ANDed with
  the new metadata filters.

Verification sync:

- `docs/baselines/CVF_GC026_CVF_ADD_RUNTIME_METADATA_QUERY_SYNC_2026-05-07.md`
