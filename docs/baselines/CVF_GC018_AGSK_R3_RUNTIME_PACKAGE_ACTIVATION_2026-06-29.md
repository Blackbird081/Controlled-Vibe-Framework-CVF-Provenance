# CVF GC-018 Baseline: AGSK-R3 Runtime And Package Activation Opening

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-29

docType: baseline

Batch ID: AGSK-R3

dispatchBaseHead: 3e53eba5

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | open a governed package-activation enablement lane for the 24 AGSK-R2 upstream skill candidates |
| Baseline | AGSK-R2 closed at `50689173` with 24 metadata-only `CANDIDATE` entries and regenerated ASSF skill index |
| Proposed tranche | AGSK-R3 runtime/package activation readiness and package-root proposal |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Closure posture | dispatch baseline only; closure requires worker return and reviewer acceptance |

## Purpose

Authorize a bounded worker tranche that turns the AGSK-R2 metadata-only
candidate inventory into source-verified package-activation evidence. The
worker may propose CVF-owned package roots and `PROPOSED` lifecycle source
updates for the same 24 upstream `skills/*/SKILL.md` candidates, then
regenerate the generated ASSF skill index from registry sources.

This baseline opens the lane. It does not itself activate a runtime resolver,
set any package to `APPROVED` or `ACTIVE`, execute upstream instructions, or
claim automatic skill invocation.

## Scope / Methodology

Allowed AGSK-R3 worker scope:

- read all 24 pinned upstream source mirror `skills/*/SKILL.md` files;
- read the 24 matching ASSF registry entries created or updated by AGSK-R2;
- create CVF-owned package-root proposals under
  `docs/reference/agent_system_skills/packages/<skill-id>/` only for the 24
  AGSK-R2 upstream skills;
- write package-root `SKILL.md` and `skill.source.json` files only as CVF
  adaptations, not direct upstream runtime imports;
- update the 24 matching registry sources only to `PROPOSED` if and only if
  the package-root proposal is created and source-verified;
- regenerate `docs/reference/agent_system_skills/generated/skill-index.json`
  with `python governance/compat/generate_assf_skill_index.py --generate`;
- create one worker-return review packet with activation readiness evidence,
  generated-index drift proof, and stop conditions for runtime resolver work.

Forbidden AGSK-R3 worker scope:

- setting `status`, `candidateState`, `approvalState`, `uatState`, or
  `certificationState` to `APPROVED`, `ACTIVE`, `PASSED`, or `CERTIFIED`;
- editing `governance/compat/*.py`, resolver source, hook catalogs, runtime
  source, provider/live code, public-sync files, or session state;
- copying upstream instruction bodies as authoritative CVF runtime behavior;
- claiming runtime activation, automatic invocation, CLI/MCP adapter support,
  provider/live proof, public export, production readiness, or package
  execution;
- touching non-AGSK-R2 registry entries except generated-index aggregation.

## Findings / Position

AGSK-R2 proved the source inventory and metadata conversion, but intentionally
left package bodies, lifecycle promotion, and resolver/runtime activation
parked. The operator now asks to open that lane. Current ASSF authority supports
opening a package-root and `PROPOSED` source-state tranche, but does not support
direct `ACTIVE` status or runtime resolver mutation before reviewer decision
and UAT evidence.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Metadata candidates could be mistaken for active skills | Require package-root evidence and keep lifecycle ceiling at `PROPOSED` |
| Upstream `SKILL.md` text could be imported as direct authority | Require CVF adaptation and source verification, not direct runtime import |
| Runtime resolver activation could bypass UAT | Forbid resolver source mutation and `ACTIVE` state in AGSK-R3 |
| Generated index could drift from sources | Require generator use and drift check after registry edits |
| External CLI/MCP support could be inferred | Keep external disposition deferred and require separate adapter work order |

## Large-Scope Change Authorization

Changed-file ceiling: authorized above the default 40-file agent threshold because AGSK-R3 intentionally materializes 24 package roots, each with a package body, source evidence, and required front-door README, plus 24 scoped registry source updates, one generated index, the worker return, and paired dispatch artifacts.

Rename/delete ceiling: no rename or delete is authorized.

Operator authorization: operator requested runtime/package activation opening for the 24 AGSK-R2 upstream skill candidates, with package-root proposal work bounded by AGSK-R3 and no runtime activation.

Rollback boundary: revert AGSK-R3 package roots, the 24 scoped registry entry updates, generated skill index regeneration, worker return, and paired dispatch artifacts only; do not touch resolver/runtime, public-sync, provider keys, or unrelated CVF surfaces.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update `governance/compat/check_docs_governance_compat.py` to recognize `SKILL.md` as an approved generic filename because ASSF package topology requires `packages/<skill-id>/SKILL.md` under `docs/reference/agent_system_skills/packages/`.

Protected paths:
- `governance/compat/check_docs_governance_compat.py`

Operator authorization: operator authorized AGSK-R3 package activation enablement for 24 AGSK-R2 skill candidates; reviewer repair requires keeping ASSF `SKILL.md` package roots compatible with docs-governance naming.

Rollback boundary: revert only the `SKILL.md` allowlist addition if ASSF package topology changes; do not change package roots, registry entries, generated index, resolver/runtime, CLI/MCP adapter, provider/live proof, public-sync, or unrelated governance checkers.

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Startup front door | AGSK-R2 closed at `50689173`; activation remained forbidden until fresh operator instruction |
| Paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` |
| Source inventory | AGSK-R2 review records all 24 upstream skill candidates and regenerated index |
| Lifecycle boundary | ASSF package and composition contracts allow proposal/review paths but block self-activation |
| Required worker proof | worker return must record source reads, package-root evidence, registry readback, generated-index drift proof, and gates |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch-authoring`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/baselines`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this dispatch authoring query.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| AGSK-R2 converted 24 upstream `skills/*/SKILL.md` packages into metadata-only candidates | `docs/reviews/CVF_AGSK_R2_AGENT_SKILLS_SOURCE_MIRROR_FULL_PACKAGE_BACKFILL_2026-06-29.md` | Purpose; Upstream Skill Package Backfill Ledger | `24 upstream skills/*/SKILL.md` | AGSK-R2 review | VALUE_SET | ACCEPT |
| AGSK-R2 regenerated the ASSF generated index | `docs/reviews/CVF_AGSK_R2_AGENT_SKILLS_SOURCE_MIRROR_FULL_PACKAGE_BACKFILL_2026-06-29.md` | Machine Closure Package | `docs/reference/agent_system_skills/generated/skill-index.json` | AGSK-R2 review | VALUE_SET | ACCEPT |
| `CANDIDATE` means not usable as active package | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Package lifecycle states | `CANDIDATE` | ASSF package contract | VALUE_SET | ACCEPT |
| `APPROVED` and `ACTIVE` are higher lifecycle states | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Package lifecycle states | `APPROVED`; `ACTIVE` | ASSF package contract | VALUE_SET | ACCEPT |
| no self-activation is allowed without reviewer decision and UAT for ACTIVE | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Self-Activation Invariant | `APPROVED`; `ACTIVE`; `UAT` | ASSF composition contract | LITERAL_INVARIANT | ACCEPT |
| registry entries are source files and generated index must be regenerated | `docs/reference/agent_system_skills/registry/README.md` | Purpose; Adding A New Entry | `entries`; `generate_assf_skill_index.py --generate` | ASSF registry source family | RUNTIME_BEHAVIOR | ACCEPT |
| generator writes the generated index from registry entries | `governance/compat/generate_assf_skill_index.py` | `generate_index` | `generate_index` | ASSF generated index generator | EXISTS | ACCEPT |
| resolver returns read-only metadata and does not activate a skill | `governance/compat/run_assf_skill_resolver.py` | module docstring; `resolve_skill_packet` | `resolve_skill_packet` | ASSF metadata resolver | RUNTIME_BEHAVIOR | ACCEPT |
| conditional reopen index parks AGSK runtime resolver until package promotion exists | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | Candidate Index | `AGSK-activation-resolver-runtime` | external absorption reopen index | VALUE_SET | ACCEPT |
| package storage topology includes future `packages/<skill-id>/SKILL.md` and `skill.source.json` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Storage Topology | `packages/<skill-id>/SKILL.md`; `skill.source.json` | ASSF package contract | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`; `docs/reference/agent_system_skills/registry/README.md`; `governance/compat/generate_assf_skill_index.py`; `governance/compat/run_assf_skill_resolver.py`; `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` |
| Package roots exist before AGSK-R3 | N/A with reason: no `docs/reference/agent_system_skills/packages/` package roots existed at dispatch read time |
| Runtime behavior claimed | N/A_WITH_REASON: this baseline opens source/package proposal work only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current source supports package-root proposal and `PROPOSED` metadata ceiling, not direct runtime activation |

## Planned Artifact Manifest

| Artifact | Required owner | Status |
|---|---|---|
| AGSK-R3 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` | DISPATCH_READY |
| Worker return | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | planned |
| Package-root proposals | `docs/reference/agent_system_skills/packages/<skill-id>/` for 24 AGSK-R2 candidates | planned |
| Registry source updates | 24 AGSK-R2 registry entries only | planned |
| Generated index | `docs/reference/agent_system_skills/generated/skill-index.json` | planned regeneration |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator activation request -> AGSK-R2 source-mirror candidate inventory -> AGSK-R3 package-root proposal and lifecycle source-state dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this GC-018 baseline, AGSK-R3 work order, ASSF package roots, registry sources, and generated index |
| Disposition | open bounded package-activation enablement with runtime resolver activation blocked until later evidence |
| Claim boundary | private provenance dispatch only; no runtime, provider, public, CLI/MCP, or production claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | proposed ASSF package roots plus registry/generated metadata | internal agents may review proposed package bodies after worker return; no activation or execution authority is granted by this baseline | AGSK-R2 review, ASSF package contract, registry README, generated-index checker | no runtime loader or resolver mutation in AGSK-R3 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents cannot mutate, activate, or execute packages through AGSK-R3 | external disposition remains deferred in registry entries | separate adapter contract/work order required before any CLI/MCP support | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Required evidence |
|---|---|---|
| AC1 | Worker accounts for all 24 AGSK-R2 upstream skill candidates | 24-row package activation coverage table |
| AC2 | Any package-root proposal is CVF-adapted and source-verified | `SKILL.md`, `skill.source.json`, and source-artifact citations |
| AC3 | Registry updates, if any, stop at `PROPOSED` and do not claim UAT/certification | JSON readback evidence |
| AC4 | Generated skill index is regenerated from sources | generator command output and drift PASS |
| AC5 | Runtime resolver activation remains blocked until a later approval/UAT tranche | worker return claim boundary and conditional reopen handling |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline cites private source mirror and private provenance
registry surfaces. Public-safe publication requires separate redaction and
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-R3 runtime/package activation opening baseline |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - dispatch authorization for package-root proposal and metadata lifecycle source-state work only |
| receiptEvidence | CVF_RECEIPT_PRESENT - source verification table and planned generator/drift proof |
| actionEvidence | ACTION_EVIDENCE_PRESENT - work order dispatch and bounded planned outputs |
| invocationBoundary | governed local documentation, package-root proposal, registry source update, and generated-index regeneration only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web, or runtime interception claim |
| claimLanguage | opens package activation enablement; does not implement runtime activation |
| forbiddenExpansion | no `APPROVED` or `ACTIVE` lifecycle state, no resolver source mutation, no runtime behavior, no automatic invocation, no CLI/MCP adapter, no provider/live proof, no public-sync, no production-readiness claim |

## Claim Boundary

This baseline opens AGSK-R3 as a governed dispatch lane. It does not activate
any skill, run any package, mutate resolver/runtime code, implement an
external adapter, publish public artifacts, or certify production readiness.
