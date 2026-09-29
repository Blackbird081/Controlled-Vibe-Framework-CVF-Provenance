# CVF Brigade EARTR Local Reconciliation And Absorption Closure

Memory class: governed-external-absorption-closure

Status: ABSORPTION_COMPLETE_USE_PROVEN

docType: review

Date: 2026-08-29

Batch ID: BRIGADE-EARTR-R1

Mixed-origin derived synthesis: REQUIRED

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

External absorption core: REQUIRED

External knowledge intake routing: REQUIRED

External absorption review: REQUIRED

Delta execution claim boundary: REQUIRED

## Purpose

Close the Brigade EARTR 1.2 intake and runtime absorption by validating the returned
package, pinning the upstream repository, mapping all fourteen candidates to
current Local CVF owners, preserving source-backed residual value, and
rejecting duplicate owner creation or direct implementation import.

## Target / Source

- External return root:
  `.private_reference/legacy/CVF 13.08/BRIGADE_EARTR_SOURCE_PACK_2026-08-29/`.
- Upstream repository: `https://github.com/spinabot/brigade.git`.
- Pinned upstream commit: `e084f08dfb9aafa01e991c738cfd88e4c554ab4d`.
- Pinned package identity: `@spinabot/brigade` 1.33.0.
- Local source mirror: `.private_reference/source_mirrors/spinabot__brigade/`.
- External return manifest SHA-256:
  `cf5d923e7e0268909da68191e0bedbd068f79336be91a66c6d788a27ed2ff690`.
- EARTR protocol: `cvf.external-agent-round-trip@1.2.0`.

## Scope / Methodology

- Enumerated the source-pack root with hidden/no-ignore-equivalent filesystem
  reads and reconciled 11 regular files and 93,583 bytes.
- Read the source-pack validator before running it. Positive validation and
  the forbidden cross-lane negative self-test both passed.
- Created an ignored, detached source mirror and verified the exact upstream
  pin, 1,382 tracked files, MIT license, and package version.
- Read the nine named Brigade source/doc surfaces directly at the pinned
  mirror; no upstream dependency, build, test, installer, gateway, provider,
  tool, or runtime path was executed.
- Compared each candidate against current Learning Plane, Control Plane,
  Guard Contract, Execution Plane, Model Gateway, MAO, truth-foundation, and
  external-round-trip owners. Novelty was actively challenged at invariant
  and failure-case level.
- Applied the serious, source-backed, non-duplicate, and value-exceeds-cost
  gate separately to knowledge retention and implementation readiness.

## Findings / Position

`ABSORPTION_COMPLETE_USE_PROVEN`

The bounded knowledge intake passes: source identity, integrity, owner mapping,
and current-value disposition are complete. All four admitted existing-owner
capability clusters are runtime-integrated and representative-use proven. Two
source patterns were already materially owned and close as `NO_NEW_VALUE`.
Separately tracked CVF defects receive no Brigade innovation credit.

No Brigade code is copied and no parallel owner is created. The admitted
semantics are integrated into existing Learning, Guard, Control and Execution
Plane consumers. Representative proof covers the real delegation launcher and
durable restart path plus protected-memory trust, durable exact origin, typed
correction, exactly-once approval settlement with execution binding,
tool-result compaction, unsafe-late-compaction refusal, and a real Alibaba call.

## Decision / Disposition

Source reconciliation, knowledge normalization, CVF-native runtime conversion,
deterministic regression proof, and representative operator-authorized use
proof are complete. No Brigade value cluster remains parked. Repository-wide
release readiness remains a separate claim and is not implied here.

## Source Verification

| Claim | Source evidence | Verification | Result |
| --- | --- | --- | --- |
| upstream identity | `https://github.com/spinabot/brigade.git` | detached mirror `git rev-parse HEAD` and commit subject | matched `e084f08dfb9aafa01e991c738cfd88e4c554ab4d` |
| package and license | pinned `package.json`; pinned `LICENSE` | direct file inspection and SHA-256 | `@spinabot/brigade` 1.33.0; MIT; license SHA-256 `90de96446a6fd073cdb6a8f5276c9e8dca8da013108e3d870b667f53a4ba7fc8` |
| memory cluster | pinned `docs/tideline.md` | direct flow, record, graph, governance, and security-boundary inspection | source claims confirmed with single-operator limits retained |
| approval and execution cluster | pinned `src/agents/approval-bridge.ts`; `src/agents/exec-gate.ts` | direct contract and negative-path inspection | source claims confirmed |
| delegation cluster | pinned `src/agents/subagent-policy.ts`; `subagent-budget.ts`; `subagent-abort-cascade.ts`; `subagent-completion-bridge.ts` | direct constants, reservation, lifecycle, and completion inspection | source claims confirmed; executable max-depth default is 3, not the stale comment's 1 |
| compaction cluster | pinned `src/agents/smart-compaction.ts` | direct decision and two-pass tool-result logic inspection | source claim confirmed |
| security boundary | pinned `SECURITY.md` | direct trust-boundary inspection | single-operator, trusted in-process extension, and non-authorization memory assumptions retained as non-transferable limits |

## Required Absorption Table

| External item ID | External claim summary | Source basis | CVF verification surface | CVF disposition | Owner artifact | Next action | Claim boundary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ESC-001 | source-trust admission protects sensitive memory writes | pinned Tideline write flow | Controlled Memory capture and provenance gates | USE_PROVEN | `controlled.memory.gateway.contract.ts`; `controlled.memory.trust.contract.ts` | protected identity/preference/correction writes reject untrusted sources | no parallel memory owner |
| ESC-002 | durable origin isolation prevents cross-principal recall | pinned Tideline recall flow and security boundary | Controlled Memory plus file-backed durable store | USE_PROVEN | `controlled.memory.gateway.contract.ts`; `durable-memory-store.ts` | exact origin enforced in-memory and through restart with actor/principal separation | legacy unbound records receive no origin claim |
| ESC-003 | typed memory links distinguish correction, supersession, contradiction and derivation | pinned Tideline typed graph and maintenance flow | Controlled Memory lifecycle owner | USE_PROVEN | `controlled.memory.trust.contract.ts`; `controlled.memory.gateway.contract.ts` | typed same-origin links persist; trusted correction/supersession contradicts prior record | no foreign graph import |
| ESC-004 | append-only mutation events plus inspect, retention, purge and export | pinned Tideline governance section | memory event hooks, controlled receipts, retention and durable store | NO_NEW_VALUE | current Learning Plane memory owners | close; current owners materially cover the governance value | no second event log or governance facade |
| ESC-005 | learning changes require evaluation, human approval and revert | pinned Tideline self-improvement flow | adaptation policy A1-A6, evaluation threshold and rollback owners | NO_NEW_VALUE | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/adaptation-policy-engine.ts` and evaluation contracts | close; current governed learning path already owns the pattern | no second learning loop |
| ESC-006 | pending approval bridge settles by attributed decision, timeout or abort | pinned approval bridge | Guard Contract governed execution runtime | USE_PROVEN | `runtime/approval-execution-bridge.ts`; `runtime/agent-execution-runtime.ts` | decision, timeout and abort share one cleanup path; late/double settlement fails closed | no UI/MCP transport owner created |
| ESC-007 | authorization binds command meaning to cwd, environment, actor and session | pinned exec gate | Guard Contract governed execution runtime | USE_PROVEN | approval bridge plus `AgentExecutionRuntime.runAwaitingApproval` | context drift blocks before provider; unchanged binding executes once | exact pending execution only |
| ESC-008 | child depth/count/timeout/tool limits are atomically reserved before spawn | pinned subagent policy | MAO task graph authority, delegation adapter and launcher | ENRICH_EXISTING_OWNER | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts`; `delegation.adapter.contract.ts` | park in delegation cluster; require a reservation race or leaf-tool failure | no Brigade subagent policy import |
| ESC-009 | one cross-parent semaphore enforces global child concurrency | pinned subagent budget | MAO max-concurrent-role budget and operational launcher | ENRICH_EXISTING_OWNER | MAO task graph and launcher | park in delegation cluster; require a cross-graph oversubscription failure | semaphore is not promoted as a new owner |
| ESC-010 | parent termination cascades to descendants and frees budget | pinned abort cascade | MAO cancel tracker and operational cancellation | ENRICH_EXISTING_OWNER | `mao/lifecycle.controller.contract.ts`; `mao/operational.worker.launcher.ts` | park in delegation cluster; require an orphan-descendant or release failure | no process-kill or runtime cascade implementation |
| ESC-011 | sibling completions serialize per parent and wake once | pinned completion bridge | MAO durable ledger, idempotent launcher and batch consumer surfaces | DEFER | existing MAO coordination/lifecycle route | reopen only on duplicate or interleaved parent continuation evidence | no new event bus or completion runtime |
| ESC-012 | cap tool-result share before compaction and refuse unsafe late compaction | pinned smart compaction | Control Plane context packager | USE_PROVEN | `context.tool-result.compaction.contract.ts`; `context.packager.contract.ts` | two-pass caps preserve head/tail evidence; unsafe late compaction emits an explicit refusal | no provider summarizer introduced |
| CID-001 | portable snapshot has stale provider posture at its own public pin | returned snapshot plus pinned current README/provider matrix | current operator-local snapshot and current CVF provider truth | NEW_FINDING | future portable snapshot generation owner | repair only in a separate governed packet-generation tranche | no provider certification change and no Brigade credit |
| CID-002 | portable snapshot has stale RC posture at a public GA pin | returned snapshot plus pinned CHANGELOG | current operator-local snapshot and current release truth | NEW_FINDING | future portable snapshot generation owner | pair with CID-001 after exact source owner is found | no release-state change and no Brigade credit |

## Existing Owner Map

| Candidate cluster | Resolved current owner | Authority overlap | Implementation overlap | Final classification |
| --- | --- | --- | --- | --- |
| ESC-001/002/003 | Learning Plane Controlled Memory and durable store | substantial | full for admitted trust/origin/link semantics | USE_PROVEN |
| ESC-004/005 | Learning Plane event, retention, evaluation and rollback owners | full | full | NO_NEW_VALUE |
| ESC-006/007 | Guard Contract approval and execution runtime | substantial | full for settlement/context-binding composition | USE_PROVEN |
| ESC-008/009/010/011 | MAO task graph, delegation, launcher, lifecycle and durable event owners | substantial | full for admitted cross-parent/cascade/serialization composition | USE_PROVEN |
| ESC-012 | Control Plane context packaging | substantial | full for admitted tool-output compaction/refusal order | USE_PROVEN |
| CID-001/002 | EARTR portable snapshot generation and public truth projection | current defect confirmed | no repair in this tranche | NEW_FINDING, separated from source value |

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | structured external-agent return plus pinned upstream Git repository |
| Upstream or source-mirror disposition | `CLONED_PINNED` at `.private_reference/source_mirrors/spinabot__brigade/`; mirror is authority for Brigade facts and the return pack remains secondary mixed-origin interpretation |
| Enumeration or manifest plan | 11-file return manifest plus clean 1,382-file upstream mirror identity; only named source clusters are semantically selected |
| Per-file terminal-ledger plan | all 11 return files receive terminal `READ`; 14 semantic candidates receive final dispositions in the Required Absorption Table |
| Owner or overlap route | existing Learning Plane, Control Plane, Guard Contract, Execution Plane, Model Gateway, MAO and EARTR projection owners |
| Value-disposition route | four capability clusters `USE_PROVEN`; two source patterns `NO_NEW_VALUE`; internal CVF defects remain separately routed |
| Claim boundary | complete bounded source, semantic and runtime-use absorption; no direct import, public release, deployment, production or repository-wide release authority |

## Mandatory Blind-Spot Control Block

Candidate value was not inferred from filenames, pack confidence, schema PASS,
or hashes. Every source candidate was checked against pinned upstream symbols
and current Local CVF owners. `NO_NEW_VALUE` applies only where current owner
and implementation evidence materially cover the source pattern. All admitted
residual gaps now have consumer, deterministic and representative runtime
proof. Internal CVF defects are not counted as Brigade innovation.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | immutable return manifest -> pinned upstream mirror verification -> current CVF owner/overlap reconciliation -> value conversion -> conditional reopen or terminal closure |
| Matching local-view guard | `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | this closure and the current Learning Plane, Guard Contract, Control Plane and Execution Plane paths named below |
| Disposition | ADAPT ten source candidates into four use-proven existing-owner compositions; close two duplicates; keep unrelated CVF defects separate |
| Claim boundary | returned output remains candidate evidence; source facts use the pinned mirror and CVF-native implementations retain authority |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `https://github.com/spinabot/brigade.git` at `e084f08dfb9aafa01e991c738cfd88e4c554ab4d`; local mirror and return root named above |
| Enumeration command | filesystem-backed recursive enumeration of the return root with ordinal forward-slash paths; upstream `git ls-files` at the pinned mirror |
| Manifest artifact or inline manifest | `docs/audits/CVF_BRIGADE_EARTR_SOURCE_PACK_MANIFEST_2026-08-29.json` |
| Processing ledger artifact or inline ledger | inline 11-file ledger below and Required Absorption Table |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE; actual file processing READ=11 |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE; semantic result existing-owner enrichment=9, DEFER=1, NO_NEW_VALUE=2, internal finding=2 |
| Owner-surface map | inline Existing Owner Map with current source paths |
| Unresolved items | 0 Brigade value clusters; unrelated repository-wide release defects are deferred outside this absorption claim |
| Absorption maturity | USE_PROVEN |
| Named runtime consumer | `MaoOperationalWorkerLauncher`; `ControlledMemoryGatewayContract`; file-backed durable memory store; `AgentExecutionRuntime.runAwaitingApproval`; `ContextPackagerContract.pack` |
| Integration evidence | CVF-native coordinator/launcher composition; Controlled Memory trust and durable origin binding; approval bridge consumed by Agent Execution Runtime; tool-result compactor consumed by Context Packager; TypeScript and package regressions PASS |
| Use proof | `docs/reviews/evidence/brigade-atomic-delegation-runtime-pilot-2026-08-29.json`; `docs/reviews/evidence/brigade-residual-absorption-runtime-pilot-2026-08-29.json`; `docs/reviews/evidence/mao-live-t1-comparative-receipt-2026-08-29.json`; secret-safe diagnostics beside those receipts |
| Operator checkpoint | OPERATOR_CHECKPOINT_SATISFIED: delegation runtime proof and Alibaba cost/control pilot authorized on 2026-08-29; remaining safe local absorption explicitly continued by operator |
| Absorption completion status | ABSORPTION_COMPLETE_USE_PROVEN |
| Completion claim boundary | all admitted Brigade value is use-proven in CVF-native consumers; unrelated CVF release defects, public export, deployment and production readiness remain outside the claim |

### Eleven-File Processing Ledger

| File | SHA-256 | Processing status | Role |
| --- | --- | --- | --- |
| `CANDIDATE_LEDGER.md` | `96181d6e0419c89b17818c43054581d2c9e6175a64bf5aad81aa3dc0854fb59c` | READ | candidate detail |
| `CLAIM_BOUNDARY.md` | `b3f76de98133367bf2b434d7975c2924697c482d01f45bfdf9dabc2427ffd9d5` | READ | authority boundary |
| `DECISION_LOG.md` | `cf7539e1b23f064f932b12bc0b6dfb7c07f2358a47db58b3316244b5e7588695` | READ | producer decisions |
| `EXTERNAL_AGENT_RETURN_MANIFEST.json` | `cf5d923e7e0268909da68191e0bedbd068f79336be91a66c6d788a27ed2ff690` | READ | strict-v1 return |
| `FILE_INVENTORY.sha256` | `0fb9d09be1334b40b4c847c066dba0c5997942ce18ee5bf9c1668f04c7adca5e` | READ | supplied integrity ledger |
| `GATE_A_SOURCE_OWNER_OVERLAP.md` | `290fb0f5d6ec3a5253a3b38226cd91e1eb7a84b7ed113e119567be3d973de87a` | READ | source-pack gate |
| `LOCAL_RECONCILIATION_HANDOFF.md` | `fd370f8897562c14c1969a98eb873e5386b6fd9b4c140398e394d4718585d98b` | READ | Local questions |
| `README.md` | `5a628155989e7dd8d677fe7c5e4edfbf73147d57126642c4fafd5dd870fbdbb5` | READ | packet front door |
| `SOURCE_MANIFEST.md` | `31070747026dab41143b86bdee2183f093d4366577d163f414cd3055ae932766` | READ | immutable sources |
| `TEST_EVIDENCE.md` | `e12f5285d76ad33f84aeb8828ff7df0f3818e4069a35614b1f93200dd34dc899` | READ | producer validation |
| `scripts/validate_source_pack.py` | `d3df4cd9bc125485f60bf26f3df9e6da33be4386054f7016dcf73f5ac277dda3` | READ | inspected and executed validator |

## Corpus Completeness And Report Integrity

- Corpus task class: structured external-agent return and pinned-upstream absorption.
- Corpus root: `.private_reference/legacy/CVF 13.08/BRIGADE_EARTR_SOURCE_PACK_2026-08-29/`.
- Snapshot time: 2026-08-29 local reconciliation session.
- Enumeration command: filesystem-backed recursive regular-file enumeration; relative paths normalized to forward slashes, sorted by ordinal Unicode code point, UTF-8 encoded, joined with LF, with one trailing LF.
- Manifest artifact or inline manifest: `docs/audits/CVF_BRIGADE_EARTR_SOURCE_PACK_MANIFEST_2026-08-29.json`.
- Manifest hash: `e52530da25bb780e4eb8d48ce782dca733a523b9cf6e6f7e2e5ccb43856ddd05`.
- Processing ledger artifact or inline ledger: inline Eleven-File Processing Ledger and Required Absorption Table.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=11; ledger_terminal=11; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: 11 files and 93,583 bytes match the immutable local snapshot; all supplied self-excluding inventory digests passed.
- Drift check: any return path/hash or mirror HEAD change invalidates reuse and requires named-drift refresh.
- Output traceability: each candidate maps to source evidence, current owner, disposition and next action.
- Adversarial verification: strict-v1 validation proves structure only; upstream and current-owner inspection supplied semantic decisions.
- Corpus verdict: COMPLETE_VERIFIED

## Knowledge System Reconciliation

- Knowledge task class: external-source candidate corpus to current-owner reconciliation.
- Source manifest: `docs/audits/CVF_BRIGADE_EARTR_SOURCE_PACK_MANIFEST_2026-08-29.json`.
- Source manifest hash: `e52530da25bb780e4eb8d48ce782dca733a523b9cf6e6f7e2e5ccb43856ddd05`.
- Enumeration safety: filesystem-backed direct reads with deterministic relative-path hashing.
- Intake registry or ledger: Eleven-File Processing Ledger and `docs/corpus-intelligence/registry/entries/brigade-eartr-source-pack-absorption.json`.
- Authority assets: pinned Brigade mirror and current CVF owner sources in the Required Absorption Table.
- Derived views: this closure and the conditional reopen index.
- Semantic region ledger: fourteen mapped candidates grouped into six capability/defect regions.
- Region reconciliation: assets=14; mapped=14; deferred=0; unmapped=0.
- Orphan or unmapped assets: none.
- Cross-region links: memory candidates join Controlled Memory, Truth and context; approval joins capability evidence and tool trace; delegation joins MAO graph and lifecycle; snapshot defects join public truth and EARTR projection.
- Drift check: PASS
- Rebuildability check: the registry aggregate rebuilds from the source entry; the closure rebuilds from the immutable manifest, mirror pin and cited owners.
- Retrieval boundary: review and later source lookup only; no runtime retrieval or admission authority.
- Adversarial verification: Local novelty was challenged; partial overlap did not become a new owner or automatic implementation.
- Knowledge-map verdict: RECONCILED_VERIFIED

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| Brigade owner-first reconciliation | source pinning, trust-boundary preservation and split knowledge/runtime decisions | DOCTRINE_ADAPTED | this closure and existing absorption standards | reuse the evidence without changing doctrine owners | no runtime behavior |
| no standalone package delta | source patterns map to existing Learning, Guard, Control and Execution packages | NO_PACKAGE_OR_RUNTIME_VALUE | existing packages only | no package creation | no package activation |
| four retained capability clusters | memory trust/origin/links, approval execution binding, delegation lifecycle and context compaction | RUNTIME_CANDIDATE | existing Learning, Guard, Execution and Control owners | closed after consolidated runtime proof | CVF-native behavior active; no foreign dependency |
| portable snapshot drift | two stale fields revealed missing posture reprojection in refresh | DOCTRINE_ADAPTED | `scripts/external_agent_packet.py`; `scripts/external_agent_snapshot_projection.py` | generator repaired fail-closed with source-hash receipt evidence and focused negative tests | no runtime/provider behavior |
| Brigade implementation | foreign runtime and single-operator assumptions are evidence only | REJECT_DIRECT_IMPORT | CVF-native owner surfaces | never copy authority or architecture wholesale | no dependency or source import |
| ESC-004 and ESC-005 | already-owned memory audit/retention and human-gated learning/rollback | NO_PACKAGE_OR_RUNTIME_VALUE | Learning Plane current owners | close as NO_NEW_VALUE | no duplicate runtime or package |

The central conditional reopen index rows `BRIGADE-memory-trust-origin-transition`,
`BRIGADE-approval-execution-context-binding`,
`BRIGADE-delegation-concurrency-cancellation-completion`, and
`BRIGADE-tool-output-aware-context-compaction` remain current as terminal
`CLOSED_USE_PROVEN` records, not open candidates.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| ESC-004/005 | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`; `adaptation.policy.ts` | CONFIRMED_EXISTING | source corroborates materially existing capability | close NO_NEW_VALUE |
| ESC-001/002/003 | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`; durable store | ENRICH_EXISTING | protected admission, exact durable origin and typed transitions are composed | close USE_PROVEN |
| ESC-006/007 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/approval-execution-bridge.ts`; Agent Execution Runtime | ENRICH_EXISTING | exactly-once settlement and context-bound execution are composed | close USE_PROVEN |
| ESC-008/009/010/011 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`; coordinator/lifecycle owners | ENRICH_EXISTING | atomic reservation, cascade and completion serialization are composed | close USE_PROVEN |
| ESC-012 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`; tool-result compactor | ENRICH_EXISTING | two-pass compaction and late refusal are composed | close USE_PROVEN |
| CID-001/002 | `README.md`; `CHANGELOG.md`; `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | NEW_FINDING | two current representation drifts, unrelated to Brigade innovation | record registry findings and route separately |
| foreign runtime design | existing governed owner paths in the rows above | REJECT_DIRECT_IMPORT | direct import would duplicate authority and transfer unsafe assumptions | retain source mirror only |

## Mixed-Origin Derived Synthesis Provenance

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Brigade source behaviors | UPSTREAM_REPOSITORY_BACKED | pinned mirror `e084f08d` | upstream fact | direct source inspection | external source authority only | READ |
| preliminary CVF owner map | CVF_PUBLIC_DERIVED | public pin `d7860138` | owner hypothesis | current Local CVF source comparison | current owner paths above | ADAPTED |
| absorption request | OPERATOR_REQUIREMENT | operator instruction dated 2026-08-29 | scope authority | startup and boundary reconciliation | operator | ACCEPT |
| atomic candidate decomposition | NOVEL_SYNTHESIS | EARTR manifest and ledger | interpretation | Local semantic review | this closure only | ADAPTED |
| final cluster/value decisions | OPERATOR_AGENT_CO_DESIGNED | source pack plus current owner evidence | governed disposition | value gate and checker confirmation | existing CVF owners | ADAPTED |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | ABSORB_BOUNDED | all fourteen candidates source-verified and owner-mapped | documentation, mirror index and registry only |
| Direct import | REJECT | foreign source is reference-only and overlaps existing owners | no dependency, code copy or architecture transfer |
| Runtime activation | ABSORB_USE_PROVEN | four residual clusters have named consumers, adversarial tests and representative proof | no additional Brigade tranche |
| Authority promotion | REJECT | external pack and source remain non-authoritative inputs | CVF current owners remain authoritative |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| memory admission and retrieval | pinned Tideline plus Learning Plane memory sources | trust/origin/transition composition integrated | ABSORBED | USE_PROVEN | none |
| memory governance and learning | pinned Tideline plus Learning Plane events/adaptation | owner and implementation exist | NO_NEW_VALUE | CLOSED | none |
| approval and execution grant | pinned approval/exec source plus Guard runtime | exact settlement/context composition integrated | ABSORBED | USE_PROVEN | none |
| delegation lifecycle | pinned subagent source plus MAO owners | cross-parent/cascade composition integrated | ABSORBED | USE_PROVEN | none |
| context packing | pinned compaction source plus Control context owner | tool-output sequence and refusal integrated | ABSORBED | USE_PROVEN | none |
| portable projection | current operator-local snapshot plus public truth | representation owner unresolved in this tranche | NEW_FINDING | SEPARATE_REPAIR_REQUIRED | route F5/F6 together |

## Absorption Efficiency And Provenance Reuse

manifestLedgerReuse: REUSE_IF_FRESH

semanticReviewUnit: CAPABILITY_CLUSTER

defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED

additionalValueProbe: REQUIRED_WITH_NAMED_GAP

latencyBudget: SINGLE_PASS_BOUNDED

intakePriority: LOCAL_SYNTHESIZED_PACK_FIRST

localSemanticInspection: FILE_AND_USE_CASE_CONTENT_REQUIRED

mappingAction: DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS

deliverySequence: WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER

namePatternInference: FORBIDDEN_AS_VALUE_DISPOSITION

upstreamConsultation: TARGETED_FOR_PROVENANCE_OR_GAP

The fresh manifest and terminal ledger were reused after independent integrity
validation. Semantic review operated by capability cluster while retaining the
file ledger for completeness. Additional probes were limited to named owner and
gap questions that could change disposition.

## Tranche Admission And Continuation Value Gate

| Gate | Evidence | Result |
| --- | --- | --- |
| serious | memory poisoning, cross-scope privacy, approval drift, concurrency, cancellation and context crowd-out are material failure classes | PASS for evaluation |
| source-backed | exact upstream pin and named source symbols verified | PASS |
| non-duplicate | two candidates fully duplicate; four clusters enrich existing owners only | PASS; no new owner created |
| value exceeds cost | all admitted runtime deltas have named failures, consumers, bounded changes and adversarial proof | PASS for consolidated runtime absorption |

## Finding-To-Governance Learning Disposition

F1-F4 are now `USE_PROVEN`. Knowledge normalization, CVF-native runtime
composition, deterministic adversarial proof, durable restart evidence and
representative live use proof are complete in one consolidated closure.

F5-F6 are accepted `DOCUMENTATION_GAP` findings in the
`DOCUMENTATION_ONLY_LEARNING` lane. Operator-authorized follow-up repaired the
actual packet generator, added source-posture hashes and focused negative
tests, then refreshed the operator-local packet without changing public truth.

No new governance rule is promoted from one source. Repeated uncaught failures
may justify a checker only after an existing owner and a deterministic negative
case are identified.

## Operator-Authorized Post-Absorption Conversion

The operator explicitly authorized immediate conversion on 2026-08-29.

| Item | Result | Evidence | Remaining boundary |
| --- | --- | --- | --- |
| CID-001 provider snapshot drift | RESOLVED | refresh now projects Alibaba `qwen-flash` `EXPERIMENTAL`, DeepSeek `deepseek-chat` `CERTIFIED`, and OpenAI `gpt-4o-mini` `EXPERIMENTAL` from the pinned public readiness matrix | no provider certification or live call |
| CID-002 release snapshot drift | RESOLVED | refresh now projects `v4.0.0` and `GA_LOCAL_FIRST_APPROVED` from pinned public `CHANGELOG.md` | no release/public mutation |
| Generator recurrence control | RESOLVED | `scripts/external_agent_snapshot_projection.py`; focused positive, missing-provider and template-drift negative tests; receipt binds three public source hashes | no generic external checker claimed |
| ESC-008/009/010/011 delegation lifecycle | USE_PROVEN | real launcher/store/ledger pilot with restart, serialized completion, one wake and leaf-first abort; 31 focused and 1,981 full tests; separate Alibaba cost/control receipt | no remaining Brigade runtime-use boundary |
| ESC-001/002/003 memory trust/origin/links | USE_PROVEN | protected poisoning rejection, exact principal recall, typed correction and file-backed restart proof in the residual pilot | no remaining Brigade runtime-use boundary |
| ESC-006/007 approval execution | USE_PROVEN | decision/timeout/abort cleanup, drift suppression and one bound Alibaba execution through `runAwaitingApproval` | no remaining Brigade runtime-use boundary |
| ESC-012 context packing | USE_PROVEN | real packager compacts oversized tool results with tail preservation and refuses unsafe late compaction | no remaining Brigade runtime-use boundary |

The refreshed operator-local receipt remains outside the repository at
`D:\UNG DUNG AI\EXTERNAL_AGENT_READ\CVF_EXTERNAL_AGENT_PACKET_REFRESH_RECEIPT.json`.
It records `REFRESHED_LIVE_PUBLIC_MAIN` at public commit `d7860138350130d6d105826ce186f1beeaba3c2d`.

## Runtime Realization Proposal

Proposal ID: `BRIGADE-MAO-R1`

Recommendation: COMPLETE; operator-authorized representative runtime pilot passed and the admitted Brigade value is use-proven.

| Field | Proposal |
| --- | --- |
| Named consumer | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` (`MaoOperationalWorkerLauncher`) |
| New bounded owner | implemented at `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/atomic.delegation.lifecycle.coordinator.ts` |
| Existing integrations | MAO task graph, lifecycle controller, durable run store, event ledger and local barrel only |
| Required behavior | atomic parent/global reservation; close-admission-before-cascade; leaf-first descendant settlement; exactly-once release; per-parent ordered completion and single wake |
| Deterministic tests | 31 focused atomic-delegation adversarial cases pass; full execution-plane 1,981/1,981; TypeScript PASS |
| Runtime use proof | `docs/reviews/evidence/brigade-atomic-delegation-runtime-pilot-2026-08-29.json` exercises the real launcher/store/ledger with restart, two serialized settlements, exactly one parent wake, leaf-first abort cascade, and replay to zero active capacity; Alibaba cost/control comparison is separately recorded at `docs/reviews/evidence/mao-live-t1-comparative-receipt-2026-08-29.json` |
| Operator checkpoint | OPERATOR_CHECKPOINT_SATISFIED by the operator's 2026-08-29 instruction to finish both boundaries and use available Alibaba API credentials |
| Rollback | remove the new coordinator/tests/export and revert only launcher/store/ledger integration hunks; retain source manifest and knowledge standard |
| Expected value | prevents oversubscription, orphan descendants, double budget release, duplicate parent wake and order-dependent continuation decisions |
| Forbidden expansion | no provider, process kill, daemon, global queue, public sync, deployment, secrets or production claim |

The consolidated residual batch is complete. No additional Brigade tranche is
open; any future work requires new upstream drift or a newly reproduced gap.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement the operator's 2026-08-29 rule
that docs-only normalization cannot close foundation-uplift absorption and
that useful reversible owner-local work proceeds proactively until a runtime
execution or other external-effect checkpoint is reached. The same operator
instruction authorizes one bounded review-convergence hardening batch after
Brigade implementation review, without another rework tranche.

Protected paths:

- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `governance/compat/check_external_absorption_core.py`
- `governance/compat/test_check_external_absorption_core.py`
- `governance/compat/check_review_cost_control.py`
- `governance/compat/test_check_review_cost_control.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/review_convergence_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`

Operator authorization: the operator explicitly required runtime-usable value,
proactive absorption, consultation at the runtime execution boundary, and
automatic prevention of avoidable review-by-drip and uncontrolled external
MCP/CLI re-dispatch cost.

Rollback boundary: revert only the new maturity fields, lifecycle validation,
tests and routing language if they misclassify absorption artifacts, plus the
review-convergence standard/template/orientation/checker/test/catalog changes
as one batch if rejected; retain accepted Brigade runtime implementation.

## Large-Scope Change Authorization

The operator explicitly authorized closing both remaining Brigade boundaries
in one consolidated pass and required avoiding further artificial tranches.
The changed-file count combines the already reviewed absorption/runtime batch,
review-convergence guard hardening, responsibility-based file splits, and two
final runtime evidence artifacts; it is not authorization for unrelated work.

Changed-file ceiling: authorized up to 50 changed files for this consolidated
Brigade closure batch.

Rename/delete ceiling: zero renames and zero deletes are authorized.

Operator authorization: the operator instructed the reviewer/orchestrator to
finish both boundaries, use the available Alibaba credentials for live proof,
and not reopen work that can be closed in the same pass.

Rollback boundary: revert only the Brigade absorption/runtime, bounded
review-cost governance hardening, responsibility splits, and their evidence;
preserve unrelated pre-existing worktree changes.

This large-scope authorization does not itself expand runtime authority. The
later operator instruction separately authorized the completed bounded Alibaba
proof. Deployment, public mutation, push, destructive effects, credential
disclosure, and unrelated runtime work remain unauthorized.

## Rescan Intelligence Hardening

- Original source artifact: Brigade EARTR source pack and pinned upstream mirror named in Target / Source.
- Predecessor intake artifact: producer `GATE_A_SOURCE_OWNER_OVERLAP.md` and `LOCAL_RECONCILIATION_HANDOFF.md` inside the immutable return.
- Delta ledger status: complete inline classification across all four required categories.
- Routing matrix status: complete inline routing across all five required lanes.
- Semantic sampling status: source-backed adversarial samples cover duplicate, residual, deferred, unsafe-assumption, and internal-defect decisions.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Local result | Disposition |
| --- | --- | --- |
| UNCHANGED_FROM_INTAKE | external candidates remain non-authoritative | retained |
| CHANGED_DISPOSITION | nine preliminary ADAPT rows become four existing-owner clusters; two preliminary duplicate rows remain duplicate | narrowed and clustered |
| NEW_FINDING | both portable snapshot hypotheses are current defects | routed separately |
| REMOVED_OR_REJECTED | direct import, automatic owner creation and automatic implementation | rejected |

### Follow-Up Routing Matrix

| Routing lane | Routed subject | Result or reopen condition |
| --- | --- | --- |
| DO_NOW | immutable provenance, owner map, registry and conditional value | fulfilled by this closure |
| SEPARATE_RUNTIME_TRANCHE | none | all admitted clusters closed in the consolidated batch |
| STRATEGIC_OPERATOR_DECISION | future upstream drift or newly reproduced gap only | no current Brigade decision pending |
| OUT_OF_SCOPE | source import, upstream execution, provider/live, public/deploy | remains prohibited |
| RESOLVED_BY_DESIGN | source research versus Local novelty/authority separation | EARTR 1.2 design retained |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| BRG-SMP-01 | Tideline write/recall | memory controls are new | ENRICH_EXISTING_OWNER | current Controlled Memory owned the surface; residual trust/origin/link composition is now use-proven | ABSORBED_EXISTING_OWNER |
| BRG-SMP-02 | Tideline governance | event log and gated learning are new | NO_NEW_VALUE | current event, retention, evaluation and rollback owners materially cover them | CONFIRMED_EXISTING |
| BRG-SMP-03 | subagent lifecycle | Brigade runtime should be adopted | ENRICH_EXISTING_OWNER | MAO retained authority and absorbed only reproduced failure semantics | ABSORBED_EXISTING_OWNER |
| BRG-SMP-04 | smart compaction | fixed thresholds should be copied | ENRICH_EXISTING_OWNER | fixed thresholds were not copied; bounded share/order/refusal semantics were integrated | ABSORBED_SEMANTICS_ONLY |
| BRG-SMP-05 | portable snapshot | Brigade reveals provider/release innovation | NEW_FINDING | both mismatches are CVF representation defects independent of Brigade | DEFECT_SEPARATED_FROM_SOURCE_VALUE |

## Risk / Corrective Action

The main residual risk is overclaiming Brigade's single-operator and
trusted-extension assumptions as CVF security guidance; those assumptions
remain explicitly non-transferable. Future upstream drift does not reopen this
closure automatically.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `check_external_agent_absorption_table.py`; `check_absorption_blindspot_control_presence.py`; `check_external_absorption_core.py`; `check_external_absorption_value_conversion.py`; `check_external_absorption_overlap_discipline.py`; `check_mixed_origin_derived_synthesis_absorption.py`; `check_corpus_completeness_report_integrity.py`; `check_corpus_to_knowledge_map_reconciliation.py`; `check_rescan_intelligence_hardening.py`; `check_delta_execution_claim_boundary.py`; `check_source_mirror_migration.py`; `check_corpus_scan_registry.py` |
| literalTokensReviewed | Required Absorption Table; Absorption maturity; Named runtime consumer; Integration evidence; Use proof; Operator checkpoint; Absorption completion status; ABSORPTION_COMPLETE_USE_PROVEN; ABSORPTION_NOT_COMPLETE; External Repository Absorption Entry Control; Corpus verdict; Knowledge-map verdict; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; Mixed-Origin Derived Synthesis Provenance; Absorption Decision Vector; System-Chain Value Review; Rescan intelligence verdict; claimDisposition; forbiddenExpansion |
| gateRunPurpose | confirm source-reviewed artifact shape and record closure evidence; gates are confirmation, not first discovery |
| claimBoundary | read-ahead covers this bounded documentation, mirror-index and registry closure only; it proves no runtime, provider, public or implementation behavior |

## Epistemic Process Block

Epistemic Process Applicability: APPLICABLE: this closure updates novelty,
overlap and current-value claims using pinned upstream and current CVF evidence.

Expected Result / Prediction: most source patterns would overlap current Local
CVF owners, while a smaller number of failure-semantics clusters would retain
bounded option value.

Evidence Comparison: two of twelve source candidates were already fully owned;
the remaining ten reduced to four existing-owner runtime compositions and are
now use-proven. Internal CVF defects do not count as external-source value.

Contradiction Or Gap Disposition: preliminary labels were advisory. Local
evidence narrowed, clustered, or rejected them without creating a parallel
owner.

Claim Update: Brigade source reconciliation, knowledge normalization, all
admitted runtime compositions, and representative use are complete under
`ABSORPTION_COMPLETE_USE_PROVEN`.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | Brigade source reconciliation, knowledge normalization, four bounded CVF-native runtime compositions, and representative operator-authorized use proof |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | CVF_RECEIPT_PRESENT: atomic-delegation, residual-absorption, Alibaba comparison and secret-safe diagnostic receipts under `docs/reviews/evidence/` |
| actionEvidence | ACTION_EVIDENCE_PRESENT: real launcher/store/ledger restart; durable memory restart; approval-bound live provider execution; real context packager compaction/refusal; deterministic regressions |
| invocationBoundary | this continuation used 12 Alibaba calls: 3 residual-pilot attempts and 9 configured live-test calls across necessary Learning Plane regression runs; no revision-agent or MCP re-dispatch calls were used |
| interceptionBoundary | no IDE, shell, Git, filesystem, provider, model or tool interception claim |
| claimLanguage | source reconciliation, runtime integration, and representative use-proven maturity for all admitted Brigade value |
| forbiddenExpansion | source import, public export, deployment and production readiness remain unclaimed; repository-wide release remains blocked by the separately recorded release-gate failures |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local reviewer/closer role |
| Provider or surface | local CVF workspace and read-only Git upstream |
| Session or invocation | BRIGADE-EARTR-R1 reconciliation, 2026-08-29 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | pack validator, Git pin/mirror reads, local file reads, `rg`, `apply_patch`, governance generators and checkers |
| Target paths | this closure, absorption core/guards, return manifest, corpus registry, source-mirror/conditional index, snapshot generator, and existing MAO launcher composition |
| Allowed scope source | operator instruction to evaluate and absorb `spinabot/brigade` using the new rules |
| Before status evidence | clean private provenance HEAD `c8483065c`; validated return existed only under private legacy reference; no Brigade mirror or registry row existed |
| After status evidence | source pinned; fourteen candidates reconciled; four existing-owner runtime compositions use-proven; package checks PASS; Learning 1,948/1,948, Guard 953 passed with 5 skipped, Control 3,799/3,799; atomic and residual representative pilots PASS |
| Diff evidence | exact governed changed set reviewed after generation and before handoff |
| Approval boundary | operator checkpoint satisfied for the bounded Alibaba live pilot; no public sync, deployment, push, or production authority |
| Claim boundary | all admitted Brigade value is use-proven; no repository-wide release, public, deployment or production claim |
| Agent type | reviewer/closer |
| Invocation ID | `brigade-eartr-r1-absorption-2026-08-29` |
| Expected manifest | existing Brigade provenance/governance/MAO paths plus the bounded Learning, Guard and Control owner-local residual implementation, tests, pilot and evidence paths |
| Actual changed set | prior Brigade absorption set plus `controlled.memory.trust.contract.ts`, Controlled Memory gateway/durable store and tests; `approval-execution-bridge.ts`, Agent Execution Runtime, package boundary and tests; `context.tool-result.compaction.contract.ts`, Context Packager/barrel and tests; `scripts/run-brigade-residual-absorption-runtime-pilot.ts`; two residual evidence receipts; this closure and active handoff |
| Manifest delta | MATCH_BOUNDED_ABSORPTION_SCOPE: no Brigade dependency/source import, public sync, deployment or production mutation; unrelated dirty-worktree paths remain user-owned |

## Claim Boundary

This closure proves bounded return integrity, upstream pin verification,
current Local CVF owner reconciliation, semantic disposition, deterministic
integration, and representative operator-authorized runtime use of all
admitted Brigade value through existing CVF consumers. It does not claim
upstream Brigade execution, repository-wide release, public export, deployment,
or production readiness.

`rawMemoryReleased=false`; no raw memory or retrieval payload is released.

`ABSORPTION APPROVAL != IMPLEMENTATION AUTHORITY`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
