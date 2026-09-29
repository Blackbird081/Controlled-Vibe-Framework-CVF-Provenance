# CVF Agent Work Order - CADP AI T5 R1 External Readout Authority Foundation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Batch ID: CADP-AI-T5-R1

Date: 2026-08-15

Dispatch base head: `576af12fba91bb6972e1e7646d63fe1d30d7b7d2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker (contract/fixture/negative-proof foundation role)

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_WORKER_RETURN_2026-08-15.md`

## Dispatch Prompt Envelope

Role: delegated worker for CADP-AI-T5-R1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START` (run `git rev-parse --short HEAD` immediately before the first edit).

Current-time notes: artifact date is 2026-08-15; T5 adapter implementation
stays deferred for the whole of this tranche.

Do-not-misread notes: this packet does not authorize an MCP tool, a CLI
command, external-agent invocation, credential access, provider calls,
network access, state mutation, hook/autorun/CI wiring, public sync,
deployment, production claims, or a lifted invocation moratorium. A worker
return that claims implementation readiness for a live external entry point
is out of scope and must be returned `BLOCKED_WITH_REASON`.

Required first actions: read `AGENTS.md`, `docs/reference/guard_orientation/README.md`,
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
this work order, the paired GC-018 baseline
(`docs/baselines/CVF_GC018_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md`),
and every checker source listed in the Checker Source Read-Ahead Block below,
before writing or editing any file.

Return contract: create the worker return artifact at the path above, run
every required gate, leave all changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Authorize a documentation-and-contract-only foundation tranche that adds one
new CVF-native, pure, deterministic TypeScript contract module inside the
existing Guard Contract owner, plus focused positive/negative tests, one new
fixture entry, and a standalone negative-proof plan, so an independent
reviewer can judge whether the nine `MISSING_AUTHORITY` prerequisites
recorded by the accepted CADP-AI-T5 deferral may move toward
`SATISFIED_BOUNDED`. No external entry point, credential, network, state
mutation, or moratorium change is authorized.

## 1. Mission

Add a CVF-native, pure, deterministic TypeScript contract foundation inside
the existing Guard Contract owner that source-verifiably satisfies rows 1-7
and 9 of the nine `MISSING_AUTHORITY` prerequisites recorded by the accepted
CADP-AI-T5 deferral, plus focused positive/negative tests and a standalone
negative-proof plan, without creating, registering, or invoking any external
entry point, without touching credentials, network, or state, and without
implying the invocation moratorium is lifted. Success means: the new
contract module typechecks, its focused and hermetic tests pass, the T4
drift checker still passes unchanged, and the worker return packet gives an
independent reviewer everything needed to judge whether each row may move to
`SATISFIED_BOUNDED`.

## 2. Authority Chain

- Operator instruction: dispatch authoring instruction for CADP-AI-T5-R1,
  2026-08-15
- Active session state: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
  `nextAllowedMove`
- Decision pack / review authority: `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_COMPLETION_2026-08-14.md`
- Roadmap: `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`
- Roadmap design-control gate: Design Control Gate table in the roadmap above
- Spec / contract / machine-readable semantics: `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`
  (existing surface schema pattern to extend, not to edit)
- GC-018 requirement: already filed at
  `docs/baselines/CVF_GC018_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md`
- Active handoff: `AGENT_HANDOFF_V59_2026-08-11.md`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and
  reconcile before implementation.

## 3. Agent Roles

- Orchestrator / dispatcher: operator-directed dispatch author (this batch)
- Implementer: delegated worker
- Reviewer: independent reviewer/closer
- Operator approval required for: any scope expansion, transport
  registration, moratorium lift, credential/provider/network action, or
  claim-boundary change

## Scope

Allowed scope:

- add the new TypeScript contract module at
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts`
  containing only pure,
  deterministic types and validator/constructor functions; no filesystem,
  network, process, or provider import;
- define, inside that module: an exact read-only metadata field allowlist
  type; an external caller identity **input contract** (shape only: caller
  identifier, requested scope, request timestamp; no credential
  resolution/validation logic); an ingress schema/size validator (fail
  closed on unknown fields and oversize input); a redaction function that
  rejects the existing T1 secret/private-provenance field names from any
  allowlisted payload; a deterministic external error/receipt contract
  extending the T1 `DeterministicCadpReceipt` explicit-time pattern; and a
  replay/freshness contract using explicit issued-at/expiry fields;
- export the new module's public symbols from
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` using the same
  named-export style already used for the CADP T1 symbols, but only when the
  worker confirms (and records in the worker return) that the added export
  names introduce no ambient authority, transport, or activation claim;
- add the focused Vitest test file at
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.test.ts`
  with positive and adversarial negative cases per the Adversarial Test
  Matrix below;
- add exactly one new fixture entry describing the new module's
  `falseAuthorityFields`/`requiredExportSymbols`/`forbiddenSeamTokens` to
  `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` as
  an additional `surfaces[]` array entry, without editing any existing
  entry's fields;
- add the standalone negative-proof plan document at
  `docs/reference/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_NEGATIVE_PROOF_PLAN_2026-08-15.md`
  naming the adversarial classes this foundation must resist and how the new
  test file proves each one;
- create the worker return packet at the path named in the header;
- run every command in the Pre-Flight Checks and Evidence Requirements
  sections and record real output.

Forbidden scope:

- no MCP tool registration; no CLI command addition; no change to
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` registration or any MCP/CLI transport
  file;
- no invocation of any MCP tool, CLI command, or external agent process;
- no credential access, resolution, storage, or environment-variable read
  beyond what already exists in the repository's own test tooling;
- no provider API call of any kind;
- no network call or live test;
- no state mutation (no database, no queue, no external file outside the
  Allowed scope paths);
- no activation, certification, or execution authority field set to
  anything other than `false`/absent in any new type;
- no hook, autorun phase, or CI wiring change;
- no public sync, deploy, or production action;
- no claim that a T5 adapter is implementation-ready;
- no attempt to lift or narrow the invocation moratorium;
- no edit to `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, or `AGENT_HANDOFF*.md`,
  including specifically `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and `AGENT_HANDOFF_V59_2026-08-11.md`;
- no edit to any existing CADP T1/T3A/T3B/T4 contract file, the T2A grant
  file, or any existing entry in the T4 fixture;
- no edit to `governance/compat/check_cadp_authority_boundary_drift.py` or
  any other `governance/compat/check_*.py` checker;
- no commit of any kind.

Risk ceiling:

- R1

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`worker`, lifecyclePhase=`pre-implementation`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role worker --lifecycle-phase pre-implementation --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added ADIF constraint; canonical source, no-runtime, and moratorium boundaries in the Scope section remain mandatory |

## Operator Checkpoint

Operator approval is required before this work order may proceed past its
Allowed scope for: transport registration, moratorium lift, credential or
provider access, network action, state mutation, hook/CI wiring, public
sync, deployment, or production claim. Routine allowed-scope gate
remediation, documentation format repair, and required evidence-block
completion do not require operator confirmation per Section 6C Worker
Autonomy / No-Question Rule.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | operator-selected continuation of the accepted, deferred CADP-AI-T5 decision into a bounded R1 foundation-contract tranche inside the existing Guard Contract owner |
| Scope classification | control-plane/documentation-and-contract tranche; no runtime endpoint, no public surface |
| Risk sensitivity | public-sync: none; provider/live proof: none; secrets: none; legal/current-law: none; production: none; readiness claim: forbidden (foundation only, not implementation-ready) |
| Selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| Role separation basis | worker (implementation) and independent reviewer/closer (row-conversion acceptance and commit) remain separate passes even when the same agent performs both across different turns, per the Agent Handoff Contract Control Block and Reviewer Closure Conversion sections below |
| Escalation condition | any need to touch a forbidden path, register a transport, access a credential, or claim implementation readiness stops the worker and returns to the orchestrator |

## Single-Agent Multi-Role Control Block

| Field | Value |
| --- | --- |
| Role separation ledger | worker role: author contract/fixture/test/plan files and the worker return, per Section 4 Allowed scope; reviewer/closer role: independently re-read the new contract/test/fixture, decide row conversions, and own any commit, per Reviewer Closure Conversion |
| Evidence basis independent of memory-only claims | typecheck output, focused Vitest output, and the T4 drift-checker output required in Section 9 Evidence Requirements; not the worker's own prose claim alone |
| Self-review boundary | the worker's own return may only propose `WORKER_PROPOSED_PENDING_REVIEW` row dispositions; it must not self-declare independent review or a closed-equivalent status |
| Escalation conditions | risk-ceiling change, scope change, public-sync, provider/live proof, secrets, destructive action, or claim-boundary change stop the agent and return to the orchestrator |
| Gate sequence | worker-return fast gate at handoff; reviewer runs `pre-closure` on the real committed range before any closed-equivalent status is recorded |

## Foundation Storage Layout Block

N/A with reason: this tranche adds one new contract module beside the
existing Guard Contract owner, one new fixture entry, one new test file, and
one new dated reference document; it does not create, split, relocate, or
refactor a durable governance foundation folder or index.

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
| --- | --- | --- | --- |
| no external CADP-named HTTP/CLI/MCP entry point exists today | `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md`, Existing CADP Interface Inventory | no external CADP entry point found in the bounded search | PASS |
| `check_dual_agent_surface_matrix.py` does not exist as a wired checker today | direct path check `ls governance/compat/check_dual_agent_surface_matrix.py` | path absent | PASS |
| the T4 drift checker is unwired to any hook/autorun/CI trigger today | `governance/compat/check_cadp_authority_boundary_drift.py`, module docstring | checker source confirms unwired, hermetic status | PASS |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: operator selected a repo-local governed foundation lane and supplied no external artifact |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired baseline |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | CVF-governed repository sources remain the only authority for this dispatch |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id CADP-AI-T5-R1 --title "CADP AI T5 R1 External Readout Authority Foundation" --date 2026-08-15 --base 576af12fba91bb6972e1e7646d63fe1d30d7b7d2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T5 decision accepted bounded and deferred at ef84a1f6a" --dependency "CADP-AI-T6 live compatibility accepted bounded at 2599ff10e" --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus `WORKER_MUST_NOT_COMMIT` no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | resolved every generated placeholder cell with the exact allowed-path manifest, the adversarial test matrix, the Agent Handoff Contract Control Block route, the Reviewer Closure Conversion owners, and the foundation-only claim boundary |
| checkerReadAheadConfirmation | checker sources listed below were read before this work order was authored |
| docOnlyNewFields | `foundationRowConversion`; no runtime schema field is introduced by this work order itself |
| claimBoundary | dispatch authoring provenance only; no runtime/provider/live/public/MCP/CLI/model-router behavior claim |

## 5. Required First Reads

Before filing GC-018 or editing files, read:

- `docs/baselines/CVF_GC018_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md` - the paired baseline; states the exact nine-row disposition plan and reconciliation
- `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md` - names the nine gaps and the exact reopen conditions this tranche partially satisfies
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` - the exact T1 pattern (false-authority fields, strict record types, deterministic receipt) to extend
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` - the existing owner-binding pattern; identity input contract must not duplicate or bypass this
- `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` - exact fixture schema for a new `surfaces[]` entry
- `governance/compat/check_cadp_authority_boundary_drift.py` - exact checks the new fixture entry and contract module must satisfy without modification to the checker itself

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 576af12fba91bb6972e1e7646d63fe1d30d7b7d2 --head HEAD --serial
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 576af12fba91bb6972e1e7646d63fe1d30d7b7d2 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 576af12fba91bb6972e1e7646d63fe1d30d7b7d2 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base 576af12fba91bb6972e1e7646d63fe1d30d7b7d2 --head HEAD --enforce
```

Expected results:

- `git rev-parse HEAD` exactly matches the clean execution-base SHA supplied
  in the orchestrator dispatch prompt before any edit; record the captured
  value as `executionBaseHead`
- `git status --short` is empty before any edit
- pre-dispatch and pre-implementation autorun gates PASS
- dispatch-quality and ADIF disclosure checks PASS

If a pre-flight check fails, stop and record the failed command and result.
The worker must not continue past a failed autorun phase gate.

Mandatory Gate-Failure Remediation Protocol:

- Allowed-scope failures are mandatory remediation. Complete the remediation
  and execute the failed gate again.
- Escalation is reserved for remediation that would exceed Allowed scope,
  change the claim boundary, release a `HOLD_*` prerequisite, change risk
  level, open public-sync, run live/provider proof, consume secrets/quota,
  touch forbidden paths, or perform destructive/irreversible actions.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1 defines strict record types with literal-`false` authority fields | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` | lines 69-108 | `CapabilityAdmissionRecord`; `CapabilityDistributionManifest` | Guard Contract CADP contract | ACCEPT |
| T1 barrel index re-exports CADP contract symbols by name | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` | lines 257-280 | `CADP_CONTRACT_VERSION`; `createDeterministicCadpReceipt` | Guard Contract barrel index | ACCEPT |
| T2A owner-binding contract exposes an opaque-handle read path, not a caller-suppliable credential object | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | exported symbols `isBoundCapabilityOwner`, `readBoundArtifact`, `readBoundGrantIdentity` | `readBoundGrantIdentity` | Guard Contract owner-binding contract | ACCEPT |
| T4 fixture requires exact keys `surfaceId`, `contractPath`, `packageRootPath`, `versionSymbol`, `versionValue`, `falseAuthorityFields`, `requiredExportSymbols`, `requiredExportModule`, `forbiddenSeamTokens` per surface entry | RUNTIME_BEHAVIOR | `governance/compat/check_cadp_authority_boundary_drift.py` | `_SURFACE_REQUIRED_KEYS` | `_SURFACE_REQUIRED_KEYS` | CADP authority boundary drift checker | ACCEPT |
| T4 fixture's existing three surfaces (T1, T3A, T3B) forbid the same seam tokens (`child_process`, `node:net`, `fetch(`, `process.env`, etc.) | EXISTS | `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` | `surfaces[0].forbiddenSeamTokens` through `surfaces[2].forbiddenSeamTokens` | `forbiddenSeamTokens` | CADP authority boundary contract fixture | ACCEPT |

### Source-Fidelity Freshness Note

Current runtime freshness verification for this dispatch is consolidated in
the top-level `## Current Runtime Freshness Verification` section below; the
same three checks (no external CADP entry point, `check_dual_agent_surface_matrix.py`
absent, T4 checker unwired) apply to this Source-Fidelity Pass.

### Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact path existence for both target artifacts | both paths ABSENT before authoring (recorded in the paired GC-018 baseline) | ABSENT_BEFORE_AUTHORING |
| exact title token search | `rg -n --fixed-strings "T5-R1" docs CVF_SESSION`; `rg -n --fixed-strings "EXTERNAL_READOUT_AUTHORITY_FOUNDATION" docs CVF_SESSION`; both returned only session-state prose naming this exact selected next move, no `docs/baselines/` or `docs/work_orders/` collision | NO_EXACT_COLLISION |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| T5 requires auth, ingress, mutation, redaction and dual-surface proof before implementation-ready | Section 4 Allowed scope | new contract module + fixtures | focused Vitest run named in Section 9 | PASS after worker evidence |
| adapter implementation stays deferred until fresh GC-018/work order plus moratorium lift | Non-Goals; Forbidden scope | this work order itself | no transport/registration path in Allowed scope | PASS |
| every roadmap acceptance item has a row or `N/A with reason` | this matrix | N/A | this row set | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope: reading named files, running listed
gates, repairing allowed-scope checker-shape failures, and completing
required evidence blocks. Escalation is reserved for actions that would
exceed Allowed scope, touch a forbidden path, require credentials/network/
provider access, or change the claim boundary.

## 7. Write Ownership

Owned files or modules (worker-owned; create-only unless noted):

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts`
  (create-only contract module)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` (modify-listed:
  append new named exports only; no removal or edit of existing export
  lines)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.test.ts`
  (create-only test file)
- `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`
  (modify-listed: append one new `surfaces[]` array entry only; no edit to
  any existing entry)
- `docs/reference/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_NEGATIVE_PROOF_PLAN_2026-08-15.md`
  (create-only negative-proof plan document)
- `docs/reviews/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_WORKER_RETURN_2026-08-15.md`
  (create-only; worker return packet)

Reviewer-owned closure/registry/session paths are listed in the Forbidden
paths list below; the worker must not touch them under this work order.

Forbidden paths:

- `governance/compat/check_*.py` (any existing checker)
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/**`
- any existing CADP T1/T3A/T3B contract file (modification forbidden; new
  file only)
- `governance/capability-grants/**`
- any hook, CI workflow, or autorun catalog file
- `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`
  (reviewer-owned closure path)
- `docs/reviews/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_COMPLETION_2026-08-15.md`
  (optional completion review; reviewer-owned only, per gotcha 30)
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` (reviewer/session-sync-steward owned)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (reviewer/session-sync-steward owned)
- `CVF_SESSION_MEMORY.md` (reviewer/session-sync-steward owned)
- `AGENT_HANDOFF_V59_2026-08-11.md` (or its successor; reviewer/session-sync-steward owned)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (reviewer/session-sync-steward owned)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` (reviewer/session-sync-steward owned)

Write mode: create-only for new files; modify-listed (append-only) for
`index.ts` and the T4 fixture JSON as described above.

Any file outside ownership requires an updated work order or operator
approval. If the closure diff shows files outside Allowed scope or
ownership, the worker must stop and return to the orchestrator.

## Required Artifact Manifest

| Required output | Path | Required at dispatch | Exists |
| --- | --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md` | Yes | Yes |
| Worker work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md` | Yes | Yes |

## Work-Order Fulfillment Manifest

### Planned Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts` | Yes | new external-readout foundation contract module |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` | Yes | append new named exports |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.test.ts` | Yes | positive/negative Vitest coverage |
| `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` | Yes | one new `surfaces[]` entry for the foundation module |
| `docs/reference/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_NEGATIVE_PROOF_PLAN_2026-08-15.md` | Yes | standalone negative-proof plan |
| `docs/reviews/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_WORKER_RETURN_2026-08-15.md` | Yes | worker return packet |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `governance/compat/check_*.py` | checker semantics must not be authored or altered by this worker |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/**` | no MCP transport/registration change is authorized |
| `governance/capability-grants/**` | no new or modified capability grant is authorized |
| `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md` | reviewer/session-sync-steward owned only |

### Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/**` new CADP tool file | ABSENT | ABSENT (verified: no CADP-named tool found in bounded search) | N/A |
| `governance/capability-grants/cadp-ai-t5-r1*.json` | ABSENT | ABSENT | N/A |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| new module exports contain no `true`-valued or absent authority-widening field | new contract module | every new authority-adjacent field is typed as literal `false` | Yes |
| T4 drift checker still passes unchanged against the three existing surfaces plus the new entry | `governance/compat/check_cadp_authority_boundary_drift.py` output | `PASS` with zero violations | Yes |
| adversarial negative tests fail closed | new `*.contract.test.ts` file | each Adversarial Test Matrix row below has a corresponding failing-closed assertion | Yes |

## Adversarial Test Matrix

| Adversarial class | Attempted input | Required proof-of-fail-closed behavior |
| --- | --- | --- |
| authority widening | payload sets any authority-adjacent field (e.g. an `executionAuthorized`-style key) to `true` | validator/type rejects or the field is structurally unrepresentable (literal `false` type) |
| unknown fields | ingress payload includes a field not in the exact allowlist | ingress validator rejects with a typed issue, does not silently pass through |
| oversize input | ingress payload exceeds the defined size/shape bound | size validator rejects before allowlist/redaction logic runs |
| secret / private provenance | payload includes a field name matching the T1 secret/private-provenance rejection set | redaction function strips or rejects the field; output never contains it |
| replay | freshness contract given a request whose issued-at/expiry indicates a repeat outside the allowed window | freshness check returns explicit invalid/expired disposition |
| stale request | freshness contract given a request timestamp older than an explicit staleness bound | freshness check returns explicit stale disposition |
| identity mismatch | identity input contract given a caller identifier that does not match an expected shape/format | identity input validator rejects with a typed issue; no silent acceptance |
| mutation/activation/execution/provider flags | any new type includes a mutation, activation, execution, or provider-call flag | type-level test asserts the field is absent or literal `false`; no test exercises an actual mutation, activation, execution, or provider call |

## 8. Execution Plan

Steps must be sequential unless explicitly marked parallel-safe.

1. Capture `executionBaseHead` with `git rev-parse HEAD`; confirm
   `git status --short` is empty. Input: repository state. Output: recorded
   base head. Validation: exactly matches the clean execution-base SHA supplied
   in the orchestrator dispatch prompt. Stop condition: HEAD mismatch or dirty
   worktree -> return `BLOCKED_WITH_REASON`.
2. Read every file in Section 5 plus the checker sources in the Checker
   Source Read-Ahead Block. Input: named paths. Output: none (reading only).
   Validation: worker return Source Inventory records each as `READ` or
   `SOURCE_VERIFIED`. Stop condition: a named source path does not exist ->
   return `BLOCKED_WITH_REASON`.
3. Author
   `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts`
   (identity input contract, ingress
   validator, allowlist type, redaction function, receipt/error contract,
   freshness contract) as pure TypeScript with no side-effecting imports.
   Input: T1/T2A source patterns. Output: new `.ts` file. Validation:
   `tsc --noEmit` on the Guard Contract package. Stop condition: any
   side-effecting import (`fs`, `net`, `http`, `child_process`, `fetch`,
   `process.env`) appears -> remove it before proceeding.
4. Append the new module's public symbols to
   `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` as new named
   exports only. Input: new module's exported symbol names. Output: updated
   `index.ts`. Validation: run `git diff --no-index` (or `git diff`) against
   the file's pre-edit state and confirm disposition `MATCH` for every
   pre-existing export line, with only appended lines showing as additions.
   Stop condition: any pre-existing export line shows as changed -> revert
   and redo as append-only.
5. Author
   `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.test.ts`
   covering positive cases and
   every row of the Adversarial Test Matrix. Input: new contract module.
   Output: new test file. Validation: focused Vitest run (Section 9) passes
   including every adversarial row. Stop condition: any adversarial case
   passes when it should fail closed -> fix the contract, not the test.
6. Append exactly one new `surfaces[]` entry to
   `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`
   describing the new module, following the exact schema in
   `_SURFACE_REQUIRED_KEYS`. Input: new module's exported symbols and
   version constant. Output: updated fixture JSON. Validation:
   `python governance/compat/check_cadp_authority_boundary_drift.py`
   passes with zero violations across all four surfaces. Stop condition:
   any existing surface entry's fields differ from before this edit ->
   revert and redo as append-only.
7. Author
   `docs/reference/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_NEGATIVE_PROOF_PLAN_2026-08-15.md`
   naming each Adversarial Test Matrix row and the test
   that proves it. Input: Adversarial Test Matrix; new test file. Output:
   new reference document. Validation: every matrix row is named with a
   corresponding test reference. Stop condition: a matrix row has no
   corresponding test -> add the test first.
8. Create the worker return packet from the worker-return fast-gate
   skeleton, then fill every required section, running the fast gate once
   on the skeleton and once after content is complete. Input: all prior
   steps' evidence. Output: worker return Markdown file. Validation:
   `python governance/compat/run_worker_return_fast_gate.py` passes.
   Stop condition: any required section remains a placeholder -> fill it
   before returning `COMPLETE_PENDING_REVIEW`.
9. Record final `git status --short` and confirm HEAD is unchanged from
   `executionBaseHead`. Input: repository state. Output: final evidence
   block in the worker return. Validation: HEAD unchanged; no commit
   exists. Stop condition: HEAD changed or a commit exists -> report the
   discrepancy in the worker return and do not claim
   `COMPLETE_PENDING_REVIEW`.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| Scope boundary | roadmap Non-Goals | Section 4 Forbidden scope repeats and narrows the roadmap boundary to foundation-only work | PASS |
| Non-goals | roadmap Non-Goals; T5 assessment Reopen Conditions | this work order opens only reopen conditions 2-8; conditions 1 and 9 remain reviewer/operator-owned | PASS |
| Lane split | roadmap Work Plan T5 row | this work order executes the R1 foundation slice of T5, not full T5 implementation | PASS |
| Dependency/source-verification plan | T5D completion review; T4 fixture/checker | Source Verification Block above cites exact files/symbols | PASS |
| Claim boundary | T5D assessment Claim Boundary | Section 11 and Delta block below inherit the same no-implementation-readiness boundary | PASS |
| Acceptance criteria | Section 10 below | observable via typecheck, focused tests, and drift-checker PASS | PASS |
| Verification/evidence | Section 9 below | commands and artifacts listed | PASS |
| Dispatch-readiness decision | GC-018 baseline Nine-Row Prerequisite Foundation Disposition | dispatch is ready because rows 1-7 and 9 have a concrete, bounded, testable foundation action | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | one agent may perform dispatcher (already complete) then worker roles across separate turns; reviewer/closer must be a distinct pass, whether the same or a different agent, applying independent scrutiny before any closed-equivalent status is recorded |
| phase | pre-implementation through worker handoff |
| baseHeadFor(phase) | dispatchBaseHead=`576af12fba91bb6972e1e7646d63fe1d30d7b7d2`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | worker phase touches only the Planned Artifact Manifest paths; reviewer phase may touch only completion/closure paths listed under Reviewer-owned closure/registry/session paths |
| traceScope(phase, actor) | worker records Agent Operation Trace Block in the worker return; reviewer records its own trace block if a completion review is created |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; reviewer/closer owns any commit |
| crossBatchIsolation | this batch does not read or depend on any other in-flight `WORKER_MUST_NOT_COMMIT` packet |
| nextMoveSurfaces | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION_MEMORY.md`; active handoff (reviewer/session-sync-steward owned, separate commit) |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_COMPLETION_2026-08-15.md` (optional; prefer repairing evidence inside the worker return per gotcha 30; create only if the reviewer cannot safely carry the disposition inside the worker return) |
| reviewerOwnedClosurePaths | the optional completion review above; `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` T5 row refresh if the reviewer records any row as `SATISFIED_BOUNDED`; session-sync surfaces in a separate handoff-sync commit |
| closureOwner | independent reviewer/closer only; the worker must not author or claim the reviewer's row-conversion disposition |
| workerCommitPermission | FORBIDDEN |

Reviewer-only authority: only the independent reviewer may convert any of the
nine-row table's `MISSING_AUTHORITY`/foundation-pending dispositions into
`SATISFIED_BOUNDED`, and only after re-reading the worker's new contract
module, test file, and fixture entry directly. The worker's own return may
propose a disposition but must label it `WORKER_PROPOSED_PENDING_REVIEW`, not
a closed-equivalent value.

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for
that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| `docs/reference/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_NEGATIVE_PROOF_PLAN_2026-08-15.md` | derive exact reference headings such as Scope / Applies To, Source, and claim-boundary labels before writing |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_WORKER_RETURN_2026-08-15.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## 9. Evidence Requirements

Required evidence:

- `tsc --noEmit` result for the Guard Contract package
- focused Vitest run for the new test file and the existing CADP T1/T3A/T3B
  test files (to confirm no regression)
- `python governance/compat/check_cadp_authority_boundary_drift.py` result
  across all four fixture surfaces
- complete Agent Operation Trace Block

Evidence Trace Block requirements:

- Claim:
- Command:
- Result:
- Key path:
- Verdict:

Base-anchor evidence:

- `dispatchBaseHead`: `576af12fba91bb6972e1e7646d63fe1d30d7b7d2`
- `executionBaseHead`: `WORKER_MUST_CAPTURE_AT_START`
- `closureBaseHead`: `N/A - pending review`
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Pending-artifact component gates: worker-return fast gate, focused Vitest,
  `tsc --noEmit`, T4 drift checker
- Worker Pending-Return Gate table: recorded inside the worker return
- Worker-return fast gate:
  `python governance/compat/run_worker_return_fast_gate.py`
- Committed-range `pre-closure`: `N/A - pending review`

## 10. Acceptance Criteria

- [ ] `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts`
  exists, is pure/deterministic, and
  imports no side-effecting Node module
- [ ] `index.ts` change is append-only with no existing export line changed
- [ ] `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.test.ts`
  passes and covers every Adversarial Test Matrix row
- [ ] `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`
  gains exactly one new `surfaces[]` entry with no existing entry changed
- [ ] `python governance/compat/check_cadp_authority_boundary_drift.py`
  passes with zero violations
- [ ] `docs/reference/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_NEGATIVE_PROOF_PLAN_2026-08-15.md`
  exists and names every adversarial class with its proving test
- [ ] Worker return packet exists, passes the worker-return fast gate, and
  proposes (does not claim) row-conversion dispositions

Criteria must be observable through files, commands, tests, or review
records.

Fail conditions:

- [ ] any new type field represents mutation, activation, certification, or
  execution authority as anything other than absent or literal `false`
- [ ] any existing CADP T1/T3A/T3B contract file, the T4 checker, the T2A
  grant, or any existing T4 fixture entry is modified
- [ ] any MCP/CLI transport file, registration, or invocation is added or
  attempted
- [ ] any credential, network, or provider call is attempted
- [ ] worker return claims T5 adapter implementation readiness or a lifted
  moratorium

Closure is blocked if any fail condition is present.

## 11. Review Gate

Implementation may proceed only after:

- GC-018 filed and this work order dispatched
- `pre-dispatch` autorun gate passed before dispatch
- `pre-implementation` autorun gate passed before material edits

Closure may proceed only after:

- independent reviewer confirms no fail condition is present and records
  which (if any) of rows 1-7 and 9 convert to `SATISFIED_BOUNDED`
- `pre-closure` autorun gate passed and result recorded by the reviewer

For `WORKER_MUST_NOT_COMMIT` mode, worker handoff is not closure. The
reviewer or committer must approve disposition, commit the reviewed owned
diff, and run the committed-range `pre-closure` gate before changing status
to a closed-equivalent value.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_cadp_authority_boundary_drift.py` |
| literalTokensReviewed | `work_order` structural class requires authority chain, agent roles, allowed/forbidden scope, required first reads, pre-flight checks, write ownership, execution plan, evidence requirements, acceptance criteria, review gate, closure checklist, return conditions, and operator checkpoint headings; dispatch-scaffold-provenance rejects the two placeholder tokens in the Scaffold Provenance Block table; Agent Operation Trace Block requires all seventeen labels in one real table; agent-handoff-boundary requires a clean-worktree Before status evidence line for dispatch-ready work orders; foundation-storage-layout requires its own block whenever `foundation` and a creation/refactor action word co-occur |
| gateRunPurpose | confirm this work order satisfies its own structural, dispatch-quality, trace, handoff-boundary, and foundation-storage shape before the pre-dispatch autorun gate runs |
| claimBoundary | checker source read-ahead proves structural shape only; it does not itself prove the worker's future contract/fixture/test evidence will satisfy any of the nine prerequisite rows |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | independent dispatch reviewer/repair author; worker and reviewer/closer roles execute in later turns |
| Provider or surface | local private provenance repository |
| Session or invocation | CADP-AI-T5-R1 execution-anchor repair, 2026-08-15 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed file reads, `rg`, direct file writes, governance gate commands, `git status`/`git rev-parse` |
| Target paths | this work order only |
| Allowed scope source | active session bootstrap read model `nextAllowedMove`; active handoff `AGENT_HANDOFF_V59_2026-08-11.md` |
| Before status evidence | `git rev-parse HEAD` = `2f27887440d8a0eae0ab4ee5d645b88eee005ae9`; `git status --short` showed a clean worktree before this repair began |
| After status evidence | `git status --short` shows only this repaired work order; worker implementation remains absent |
| Diff evidence | `git diff --name-status` against `2f27887440d8a0eae0ab4ee5d645b88eee005ae9` shows only this work order modified |
| Approval boundary | dispatch authority repair only; no worker implementation or reviewer closure performed |
| Claim boundary | dispatch-shape and source-verification evidence only; no runtime, provider, MCP/CLI, or moratorium-lift claim |
| Agent type | dispatcher / dispatch author |
| Invocation ID | `cadp-ai-t5-r1-dispatch-2026-08-15` |
| Expected manifest | N/A with reason: this is a reviewer correction to an already committed dispatch artifact; the sole repaired path is recorded in Target paths and Diff evidence |
| Actual changed set | N/A with reason: this is a reviewer correction to an already committed dispatch artifact; the sole repaired path is recorded in Target paths and Diff evidence |
| Manifest delta | N/A with reason: one in-place work-order repair, with no worker-output manifest yet |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this dispatch batch |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 576af12fba91bb6972e1e7646d63fe1d30d7b7d2 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_cadp_authority_boundary_drift.py
git status --short
```

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | contract/fixture/negative-proof foundation only; no transport, tool, or command is registered or invoked by this work order |
| No-runtime-overclaim | this packet does not claim any new module executes, intercepts, wraps, launches, or serves an external caller |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | new CADP external-readout foundation contract module under `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` | internal agents may read/test the new pure contract only; no commit, activation, or mutation authority is granted by this work order | worker-produced tests and drift-checker PASS once returned | N/A with reason: internal contract module only, no adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | candidate future CADP external read/query surface; not implemented, registered, or invoked | no external caller may authenticate, request, mutate, activate, or execute anything through this work order | GC-018 baseline Nine-Row Prerequisite Foundation Disposition table | deferred adapter owner; transport registration and moratorium lift both remain out of Allowed scope | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Routing

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| T5 deferral left nine prerequisite rows with no concrete, testable foundation action, only a reopen-condition list | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | this work order converts each reopen condition into an exact Allowed-scope action and Adversarial Test Matrix row |
| `check_dual_agent_surface_matrix.py` remains a candidate checker, not yet wired | N/A_WITH_REASON | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | no new control action; this work order still supplies the full six-column matrix manually per the standard |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | CADP-AI-T5-R1 foundation contract, fixture, and negative-proof dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this work order itself |
| actionEvidence | N/A with reason: this work order authorizes future worker action; it records no action evidence itself |
| invocationBoundary | local repository TypeScript authoring, Vitest execution, and governed document authoring only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | foundation-contract dispatch only; T5 adapter implementation stays deferred |
| forbiddenExpansion | no MCP/CLI implementation, external-agent invocation, provider/live action, credentials, network, state mutation, hook/CI wiring, public sync, deployment, production, or moratorium lift |

## 12. Closure Checklist

- [ ] All acceptance criteria satisfied or explicitly marked N/A with reason
- [ ] Required tests or evidence commands run
- [ ] Autorun `pre-closure` gate passed:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD`
- [ ] Commit mode recorded as `WORKER_MUST_NOT_COMMIT`
- [ ] `dispatchBaseHead`, `executionBaseHead`, and closure-stage base
  evidence recorded without treating a stale dispatch anchor as current
  worker proof
- [ ] Pending handoff used a non-closed status, recorded actual
  `git status --short`, and left committed-range `pre-closure` to
  reviewer/committer
- [ ] Worker Pending-Return Gate results are recorded
- [ ] Worker-return fast gate result is recorded
- [ ] Agent Operation Trace Block is present and complete
- [ ] Changed-file set from `git diff --name-status` (once committed) is
  inside this work order's Allowed scope
- [ ] No open checkbox residue remains
- [ ] Public catalog updated or explicitly N/A with reason

## 13. Return-To-Orchestrator Conditions

Return to orchestrator without continuing if:

- pre-flight fails and cannot be repaired inside Allowed scope;
- any autorun phase gate fails outside Allowed scope;
- source-fidelity pass finds a missing path, invented symbol, or unverified
  role/template mapping;
- scope conflict is discovered;
- implementation would require touching a forbidden path or exceeding risk
  ceiling R1;
- reviewer raises a structural blocking objection;
- the worker cannot satisfy an Adversarial Test Matrix row without widening
  authority.

## Claim Boundary

This work order authorizes foundation contract, fixture, and negative-proof
work only, inside the existing Guard Contract owner. It does not authorize
or prove an MCP tool, a CLI command, external-agent invocation,
authentication, live redaction effectiveness, transport registration,
provider behavior, credential resolution, network access, state mutation,
public-sync readiness, deployment, production use, or a lifted invocation
moratorium. The worker may propose row-conversion dispositions; only the
independent reviewer may accept them.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-contract work order; no public
artifact or sync action is authorized.
