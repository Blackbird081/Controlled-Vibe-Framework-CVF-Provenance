# CVF Agent Work Order - RSPB-AI-T13 ASSF Package Metadata To Capability Preflight Candidate Binding Kernel

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: RSPB-AI-T13

Dispatch base head: `f25420cf2d852a653206bb901b06f10267eb13ae`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: external implementation worker

Reviewer/closer: current orchestrator/reviewer

Worker return path: `docs/reviews/CVF_RSPB_AI_T13_ASSF_PACKAGE_METADATA_TO_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_KERNEL_WORKER_RETURN_2026-08-17.md`

rawMemoryReleased=false

## Dispatch Prompt Envelope

Role: external implementation worker for RSPB-AI-T13.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_RSPB_AI_T13_ASSF_PACKAGE_METADATA_TO_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_KERNEL_2026-08-17.md`

Paired baseline: `docs/baselines/CVF_GC018_RSPB_AI_T13_ASSF_PACKAGE_METADATA_TO_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_KERNEL_2026-08-17.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: packet date is 2026-08-17; repository evidence controls.

Do-not-misread notes: pure caller-supplied metadata only; registry/index and
package-body reads, resolution, activation, loading, execution, mutation,
provider/live, external adapter, public sync, deployment, or production claim.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, selected source, canonical ASSF contracts, current
Guard Contract owners/barrels, and named checker sources; capture clean HEAD
and verify the selected hash.

Return contract: change exactly five worker paths, never stage or commit, and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement one pure TypeScript evaluator that validates caller-supplied ASSF
package metadata and emits an immutable capability-preflight candidate binding
whose authority remains `CANDIDATE_ONLY` on every path.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RSPB-AI-T13",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "EXTERNAL_ABSORPTION",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [
    "docs/baselines/",
    "docs/work_orders/",
    "docs/reviews/",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts"
  ],
  "claims": ["pure ASSF metadata to capability-preflight candidate binding"],
  "requiredProof": ["focused hostile tests", "ASSF boundary cases", "TypeScript", "full legacy gate"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["registry or generated-index read/write", "package activation or loading", "filesystem/environment/network/provider/live", "external adapter, public write, deploy, or production"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, profile `P2_BOUNDED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation, tests, exports, and worker-return defects
directly. Stop only for hash drift, dirty owned paths, authority contradiction,
or a necessary sixth path. Never stage or commit.

## Authorization / Source

The operator authorized the current orchestrator to select and dispatch the
next high-value cluster. The paired baseline is the exact value decision.

## Authority Chain

Doctrine -> active CVF standards -> TPGR-T0 -> paired baseline/work order ->
canonical ASSF contracts -> accepted Guard Contract owners -> worker evidence
-> independent reviewer decision.

## Agent Roles

- Dispatcher/reviewer: current orchestrator; owns review, repair, commit, closure.
- Worker: external implementation role; exact-five write scope; no commit.
- Operator: owns any boundary expansion.

## Required First Reads

| Source | Action |
| --- | --- |
| `AGENTS.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION_MEMORY.md` | READ |
| `AGENT_HANDOFF_V59_2026-08-11.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| paired T13 baseline and this work order | READ |
| selected mixed-origin source and canonical ASSF package/composition contracts | FULL_READ |
| Guard Contract T7/T12 source/tests and both barrels | FULL_READ |
| checker sources named below | FULL_READ |

## Pre-Flight Checks

Require clean exact owned paths, record `executionBaseHead`, recompute the one
candidate hash, confirm it matches the paired baseline, and run the
pre-implementation gate before editing.

## Write Ownership

Worker owns exactly the five paths in the fulfillment manifest. Reviewer owns
any system-chain or continuity refresh. Candidate, ASSF, registry/index,
existing contracts/tests, checkers, session surfaces, and all other paths are
read-only.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T13 --title "ASSF Package Metadata To Capability Preflight Candidate Binding Kernel" --date 2026-08-17 --base c5ad52456eda067d7616dff657753ca4388639bf --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| scaffoldHelperVersion | current repository helper |
| generatedProfile | generic-worker-dispatch plus no-commit and package-skill trigger stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| placeholdersReplaced | YES |
| manualEditsAfterScaffold | exact scope, selected hash, ASSF field binding, false authority, proportional evidence |
| checkerReadAheadConfirmation | completed before authoring |
| docOnlyNewFields | T13 result vocabulary only |
| claimBoundary | pure contract only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption-implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector EXTENSIONS/CVF_GUARD_CONTRACT --risk-ceiling MEDIUM --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Work-Order Fulfillment Manifest; Task Governance Routing Manifest; Agent Operation Trace Block |
| gateRunPurpose | confirmation/evidence after source inspection |
| claimBoundary | gates do not establish semantic acceptance, package use, or runtime authority |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| selected binding idea | DOCUMENTATION | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/agent_system_skills/CVF_ASSF_PREFLIGHT_BINDING_CONTRACT.md` | complete file | `authorityStatus` | mixed-origin proposal | REJECT |
| ASSF metadata field families | VALUE_SET | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `skillId`; `status`; `riskCeiling`; `authorityCeiling`; `dependencies`; `conflicts`; `platformCompatibility` | ASSF package contract | ACCEPT |
| no self-activation | LITERAL_INVARIANT | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Self-Activation Invariant | `status` | ASSF composition contract | ACCEPT |
| current registry entry shape | SCHEMA | `docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json` | complete object | `skillId`; `candidateState`; `externalCliMcpDisposition` | ASSF registry source | ACCEPT |
| T7 profile selection owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-preflight-profile-policy.contract.ts` | exported evaluator | `evaluateCapabilityPreflightProfilePolicy` | Guard Contract T7 | ACCEPT |
| T12 closure boundary owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-bootstrap-closure-evidence-bundle.contract.ts` | exported result | `authorityStatus`; `taskAuthorityGranted` | Guard Contract T12 | ACCEPT |

## Selected Source Hash

| Local ledger path | SHA-256 | Worker use |
| --- | --- | --- |
| `docs/reference/agent_system_skills/CVF_ASSF_PREFLIGHT_BINDING_CONTRACT.md` | `984ec80802dbcfa304eaecc254963e976dceee9530982294c4fabfabaf1929d9` | design comparison only; never import |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact T13 artifacts | `Test-Path` before authoring returned false | NEW_PATHS |
| binding symbols | `rg -n -i "ASSF.*preflight.*candidate|preflight.*ASSF.*binding" EXTENSIONS/CVF_GUARD_CONTRACT/src docs/reference/agent_system_skills governance/compat` | no pure Guard Contract evaluator found |
| integrity, secret, promotion candidates | T9, T5/T9/T12, and T6 owners inspected | NO_NEW_VALUE |
| collision decision | enrich Guard Contract with one mapping seam; preserve ASSF owners | ENRICH_EXISTING |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher/reviewer distinct from external worker |
| phase | implementation pending independent review |
| baseHeadFor(phase) | dispatchBaseHead=`f25420cf2`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START |
| changedSetScope(phase) | exact five worker paths |
| traceScope(phase, actor) | selected hash, tests, before/after status, staging, exact manifest |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns commits |
| crossBatchIsolation | clean worktree required; no ASSF, candidate, existing T7/T12, checker, session, or unrelated edits |
| Before status evidence | clean worktree at dispatch base `f25420cf2` |
| nextMoveSurfaces | worker return then independent review |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | one fully read mixed-origin file; duplicate clusters rejected; one retained seam |
| scope classification | P2 bounded named-file cluster; exact five worker paths; no external effects |
| roleRouteMode | MULTI_AGENT_MULTI_ROLE |
| selectedRoleRoute | dispatcher -> external no-commit worker -> independent reviewer/closer |
| riskSensitivity | MEDIUM: lifecycle/authority misprojection risk, no effects |
| escalationCondition | hash drift, authority contradiction, dirty owned path, or necessary sixth path |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RSPB_AI_T13_ASSF_PACKAGE_METADATA_TO_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_KERNEL_COMPLETION_2026-08-17.md` |
| reviewerOwnedClosurePaths | completion review, system-chain freshness if required, work-order closure conversion, continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/assf-capability-preflight-candidate-binding.contract.ts` | create pure strict evaluator |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/assf-capability-preflight-candidate-binding.contract.test.ts` | create focused hostile and lifecycle tests |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` | export T13 exactly once |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | export T13 exactly once |
| `docs/reviews/CVF_RSPB_AI_T13_ASSF_PACKAGE_METADATA_TO_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_KERNEL_WORKER_RETURN_2026-08-17.md` | create complete no-commit worker return |

Forbidden: every sixth path; candidate or ASSF edits/imports; registry/index,
resolver, loader, checker, session, package-body, adapter, runtime, provider/live,
public, deploy, or production work.

## Required Artifact Manifest

| Required artifact | Expected state at worker return |
| --- | --- |
| T13 source | new uncommitted file |
| T13 test | new uncommitted file |
| contracts barrel | one T13 export delta |
| package root barrel | one T13 export delta |
| worker return | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |

## Functional Contract

The exported evaluator must accept `unknown`, use only caller-supplied values,
and return one deeply immutable deterministic result. It must validate a
bounded exact-key envelope and a bounded ASSF metadata projection including:

- stable package identity/version and explicit expected package identity;
- lifecycle status and candidate/approval/UAT/certification evidence;
- bounded task classes, platform evidence, dependencies, and conflicts;
- risk ceiling, authority ceiling, external CLI/MCP disposition, capability
  boundary, and source-artifact references.

The evaluator must reject unknown keys, malformed or unsafe strings, raw
secret-like content, duplicate values, self-dependency, dependency/conflict
overlap, impossible lifecycle combinations, package-ID mismatch, oversized or
sparse collections, inherited/prototype/accessor/Proxy/symbol inputs, and any
attempt to supply output/authority fields.

Allowed binding statuses:
`CANDIDATE_BINDING_ACCEPTED`, `CANDIDATE_BINDING_REJECTED`, and
`CANDIDATE_BINDING_BLOCKED`.

Accepted output remains evidence-only and must carry literal
`authorityStatus: CANDIDATE_ONLY`. `routingEligible` may be true only when the
supplied lifecycle evidence is already eligible under canonical ASSF rules;
it never means activation or permission. Deprecated, retired, rejected,
unapproved, uncertified where certification is required, contradictory, or
unknown lifecycle evidence must fail closed or remain ineligible.

Every return path must contain literal false values for `activationAuthorized`,
`loadingAuthorized`, `instructionBodyReadAuthorized`, `executionAuthorized`,
`mutationAuthorized`, `acquisitionAuthorized`, `externalAdapterAuthorized`,
`providerCallAuthorized`, `publicWriteAuthorized`, and `taskAuthorityGranted`.

No ambient time, filesystem, environment, registry/index, resolver, loader,
network, provider, process, dynamic import, callback, or mutable global state.

## Acceptance Tests

Require at minimum:

- one accepted active/approved source-backed metadata projection and one
  candidate-only non-routable projection;
- every ineligible lifecycle state and contradictory lifecycle evidence;
- identity mismatch, missing source refs, authority/risk weakening, forbidden
  external-adapter claim, self-dependency, conflict overlap, duplicates;
- secret-like values at every free-text/list boundary;
- unknown keys, prototype pollution, inherited object, accessor, Proxy,
  symbol, sparse/oversized arrays, control/NUL strings;
- deterministic repeated output, caller mutation isolation, deep freeze;
- both-barrel import proof and T7/T12 regression.

## Acceptance Criteria

Exactly five worker paths; selected hash matches; pure API only; no ASSF or
registry/index change; all false grants literal; focused/composed/package/
TypeScript gates pass; worker return truthfully reports uncommitted state.

## Execution Plan

1. Preflight, clean-state capture, selected hash verification.
2. Read canonical owners and implement the smallest pure evaluator.
3. Add focused hostile tests and both exports.
4. Run focused, T7/T12 regression, package, TypeScript, and return gates.
5. Leave staging empty and return uncommitted evidence.

## Evidence Requirements

Record execution base, selected SHA-256 match, exact changed paths, focused and
regression counts, full package count, TypeScript, `git diff --check`, HEAD
unchanged, staging empty, and all implementation iterations.

## Review Gate

Only the independent reviewer may accept, stage, commit, or close T13.

## Operator Checkpoint

NO_CHECKPOINT_REQUIRED. Stop only when scope, authority, effects, or a required
sixth worker path changes.

## Evidence Reuse And Encoding Plan

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | accepted T0 205-row ledger |
| priorVerificationAnchor | exact selected path and SHA-256 row |
| recomputeReason | dispatch requires selected local bytes to match |
| encodingPlan | authored prose/code defaults to ASCII; retained path spaces are filesystem names |

verificationMode: RECOMPUTE_REQUIRED

## Worker Output Checker Read-Ahead Mandate

Before authoring the return, read current checker sources for a changed
`docs/reviews` worker-return packet and reproduce their exact required headings
and tables. Do not treat this work order as a substitute for checker read-ahead.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RSPB_AI_T13_ASSF_PACKAGE_METADATA_TO_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_KERNEL_WORKER_RETURN_2026-08-17.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Include Purpose, Target / Source, Scope / Methodology, Findings / Position,
Risk / Corrective Action, Source Verification Block, Checker Source Read-Ahead
Block, Source Inventory, Gate Evidence, Agent Operation Trace Block, Delta
Execution Claim Boundary Control Block, absorption/corpus blocks, Epistemic
Process Block, Public Export Disposition, Claim Boundary, hashes, tests,
diff/status/staging evidence, and the exact return token.

## Verification Commands

Use package-local Vitest/TypeScript commands already proven by T12, then:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
git diff --cached --name-only
git rev-parse HEAD
```

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: T13 consumes caller-supplied metadata and does
not create or change any ASSF package, registry entry, generated index, skill
body, lifecycle state, resolver, loader, or use-proof receipt.

Target lifecycle state: N/A with reason: output is always evidence-only
`CANDIDATE_ONLY` and cannot advance a package.

Prior phase evidence: canonical ASSF package and composition contracts cited
in Source Verification.

Next forbidden skip: no promotion, activation, load, projection, or runtime
eligibility claim follows from this packet.

Runtime/provider proof: N/A with reason: no runtime/provider action authorized.

Claim boundary: metadata-binding contract only, not package productionization.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | RSPB-AI-T13 dispatch, 2026-08-17 |
| Working directory | repository root at `f25420cf2` |
| Command or tool surface | ledger parsing, selected source read, canonical-owner comparison, Git |
| Target paths | paired baseline, this work order, reviewer-owned continuity surfaces |
| Allowed scope source | operator request to create next no-commit work order |
| Before status evidence | clean worktree at `f25420cf2` |
| After status evidence | dispatch artifacts prepared; worker implementation not started |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | dispatch only; no worker or runtime action by dispatcher |
| Claim boundary | pure T13 contract scope only |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `rspb-ai-t13-dispatch-2026-08-17` |
| Expected manifest | paired baseline; this work order; reviewer-owned continuity surfaces |
| Actual changed set | reviewer verifies before dispatch commit |
| Manifest delta | reviewer verifies before dispatch commit |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | pure caller-supplied ASSF metadata to candidate evidence projection |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no package use or execution receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no action is authorized |
| invocationBoundary | explicit pure function invocation with supplied metadata only |
| interceptionBoundary | registry, filesystem, resolver, loader, provider, tool, and runtime interception are forbidden |
| claimLanguage | candidate evidence projection only |
| forbiddenExpansion | activation, loading, body reads, mutation, execution, adapter, provider/live, public, deploy, production |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | ledger -> one file -> canonical ASSF comparison -> pure T13 kernel |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | ASSF references and Guard Contract |
| Disposition | ADAPT one seam; reject duplicate/effectful interpretations |
| Claim boundary | no source runtime dependency or authority transfer |

## Mandatory Blind-Spot Control Block

One selected file was fully read; the remaining 204 ledger rows retain prior
dispositions and are not claimed processed by T13.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | selected mixed-origin copied-folder file |
| Upstream or source-mirror disposition | accepted predecessor evidence reused; no fetch |
| Enumeration or manifest plan | accepted 205-file ledger plus one named selection |
| Per-file terminal-ledger plan | paired baseline exact hash |
| Owner or overlap route | ASSF package/composition contracts -> Guard Contract |
| Value-disposition route | pure mapping now; runtime/activation rejected |
| Claim boundary | no rescan, direct import, registry edit, loader, or execution |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | retained local Capability Preflight Bootstrap folder |
| Enumeration command | predecessor `rg --files --hidden --no-ignore`; one named selection |
| Manifest artifact or inline manifest | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json`; paired baseline |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | ASSF package/composition contracts; Guard Contract |
| Unresolved items | 0 selected rows; implementation pending |
| Completion claim boundary | selected one-file cluster only |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| binding draft | candidate-only normalization | PACKAGE_CANDIDATE | T13 source/test | rewrite CVF-native | no loader/activation |
| lifecycle rule | ineligible remains ineligible | DOCTRINE_ADAPTED | T13 invariants | fail closed | no state change |
| composition metadata | dependency/conflict evidence | PACKAGE_CANDIDATE | bounded output | validate only | no graph resolution |
| runtime interpretations | resolver/loader opportunity | RUNTIME_CANDIDATE | separate future owner | defer unless operator opens runtime tranche | no runtime in T13 |
| checker interpretations | metadata conformance opportunity | CHECKER_CANDIDATE | existing ASSF checker family | reject duplicate checker tranche | no checker edit |
| direct proposal source | unreviewed draft implementation authority | REJECT_DIRECT_IMPORT | none | rewrite CVF-native | no import |
| adapter language | authority denial | NO_PACKAGE_OR_RUNTIME_VALUE | false grants | preserve | no CLI/MCP |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| integrity, secret, promotion | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-acquisition-receipt-verification.contract.ts`; `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/capability-learning-candidate-projection.ts` | NO_NEW_VALUE | already enforced | reject duplicate tranche |
| ASSF package metadata | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; registry sources | CONFIRMED_EXISTING | canonical fields already owned | consume caller-supplied subset |
| lifecycle/composition authority | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | CONFIRMED_EXISTING | stronger current boundary | preserve unchanged |
| ASSF-to-preflight candidate seam | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`; package root barrel | ENRICH_EXISTING | pure evaluator is the retained delta | implement T13 |

## Mixed-Origin Derived Synthesis Provenance

Selected candidate origin is `MIXED_ORIGIN` and non-authoritative. Worker
output becomes CVF evidence only after independent review.

## Absorption Efficiency And Provenance Reuse

Reuse the accepted T0 manifest/ledger and recompute one selected hash. Do not
rescan 205 files or rerun unrelated corpus/runtime/public evidence.

## Absorption Decision Vector

ADAPT candidate-only mapping; REJECT direct draft import, registry/index reads,
lifecycle mutation, resolution/loading, external adapter, and runtime behavior.

## Dual Agent Surface Matrix

| Agent type | Interface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | copied work order | exact-five pure source scope | worker return | no adapter | AUTHORIZED_NO_COMMIT |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP invocation or package authority | none | separate future packet required | DEFERRED_WITH_REASON |

## Corpus Completeness And Report Integrity

- Corpus task class: selected capability-cluster absorption.
- Corpus root: one selected local file.
- Snapshot time: 2026-08-17 dispatch.
- Enumeration command: predecessor `rg --files --hidden --no-ignore` plus named selection.
- Manifest artifact or inline manifest: paired baseline Selected Cluster Evidence.
- Manifest hash: exact selected SHA-256 in paired baseline.
- Processing ledger artifact or inline ledger: accepted T0 205-row ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=1; ledger_terminal=1; exclusions=204; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: 204 files outside this cluster.
- Unreadable or unsupported files: none selected.
- Aggregation check: 1 + 204 = 205.
- Drift check: worker recomputes one hash.
- Output traceability: one selected source to exact five paths.
- Adversarial verification: lifecycle, authority, hostile input, bounds, determinism, freeze.
- Corpus verdict: PARTIAL

## Rescan Intelligence Hardening

- Original source artifact: accepted T0 205-file ledger.
- Predecessor intake artifact: RSPB-AI-T0 dual-corpus intake audit.
- Delta ledger status: reused with one fresh hash.
- Routing matrix status: one-file ASSF binding cluster selected.
- Semantic sampling status: selected file fully read.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Evidence |
| --- | --- |
| UNCHANGED_FROM_INTAKE | 204 rows retain prior dispositions |
| CHANGED_DISPOSITION | one ASSF binding row selected for adaptation |
| NEW_FINDING | pure candidate-binding evaluator absent |
| REMOVED_OR_REJECTED | duplicate and runtime interpretations rejected |

### Follow-Up Routing Matrix

| Route | Disposition |
| --- | --- |
| DO_NOW | exact-five pure T13 kernel |
| SEPARATE_RUNTIME_TRANCHE | registry resolver/loader or activation |
| STRATEGIC_OPERATOR_DECISION | lifecycle mutation or external adapter |
| OUT_OF_SCOPE | provider/live, public, deploy, production |
| RESOLVED_BY_DESIGN | caller input and false grants |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RSPB-T13-S1 | complete draft | normalize ASSF metadata | ADAPT | invented authority | REQUIRE_CANDIDATE_ONLY |
| RSPB-T13-S2 | lifecycle rule | readiness cannot override lifecycle | ADAPT | ineligible package marked routable | REQUIRE_FAIL_CLOSED |

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`: no legacy coverage index changes; the accepted
T0 ledger and paired baseline carry the selected-row coverage.

## Foundation Storage Layout Block

N/A with reason: T13 adds one ordinary Guard Contract module/test, two exports,
and one worker return; no foundation/index relocation or split.

## Closure Checklist

- [ ] Worker records a clean execution base and matching selected hash.
- [ ] Worker changes exactly five allowed paths with staging empty and HEAD unchanged.
- [ ] Focused, T7/T12 regression, package, TypeScript, and return gates pass.
- [ ] Independent reviewer inspects semantics and hostile boundaries.
- [ ] Reviewer alone owns any bounded fix, stage, commit, completion review, and closure.

## Epistemic Process Block

### Expected Result / Prediction

The missing seam can be implemented as a pure candidate evidence projection
without package activation, loading, or authority expansion.

### Evidence Comparison

Canonical ASSF sources own metadata and lifecycle rules; Guard Contract has no
equivalent ASSF-to-preflight candidate evaluator.

### Contradiction Or Gap Disposition

Duplicate checker concepts were rejected. The retained seam is narrowed to
caller-supplied metadata and false grants.

### Claim Update

Implementation remains pending independent worker execution and reviewer proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Return-To-Orchestrator Conditions

Return only `COMPLETE_PENDING_REVIEW` with exact-five uncommitted evidence or
`BLOCKED_WITH_REASON` with the concrete source/scope blocker.

## Claim Boundary

This packet authorizes only exact-five pure T13 implementation. It authorizes
no ASSF registry/index edit, package creation/productionization, lifecycle
change, resolution, loading, instruction-body read, execution, mutation,
external adapter, provider/live call, public sync, deployment, or production.
