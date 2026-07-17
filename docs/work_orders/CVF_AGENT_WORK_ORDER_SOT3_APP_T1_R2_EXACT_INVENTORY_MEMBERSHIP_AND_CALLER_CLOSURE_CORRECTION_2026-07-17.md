# CVF Agent Work Order - SOT3-APP-T1-R2 Exact Inventory Membership And Caller Closure Correction

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: SOT3-APP-T1-R2

dispatchBaseHead: `20a4be366`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_SOT3_APP_T1_R2_WORKER_RETURN_2026-07-17.md`

## Dispatch Prompt Envelope

Role: delegated downstream contract-ratification worker.

Canonical packet: this file.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: execute only from the clean committed post-dispatch HEAD;
the copied SOT-Application folder remains read-only and is not CVF authority.

Do-not-misread notes: exactly two new review outputs; documentation only; no
source mutation, test/build/run, provider/live action, T2 work, registry edit,
roadmap edit, protected continuity, public-sync, commit, or push.

Required first actions: read startup front doors and active handoff; guard
orientation; literal gotchas; roadmap; paired baseline; this packet; accepted
T0B completion and ledger; cited SOT3/current-owner sources; then capture HEAD,
clean status, and output-path absence before writing.

Return contract: leave exactly two uncommitted paths and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce an exact membership and caller-closure correction that removes the two
remaining T1 completeness defects without reopening accepted R1 semantics.

## Authority Chain

Operator standing continuation instruction -> SOT3-APP roadmap -> T0B closure
`577237cba` -> MAO-OA closure `fef756a14` -> T1 review `ef9b09648` -> T1-R1
review `1300c3505` -> paired T1-R2 GC-018 -> this work order.

## Agent Roles

- Worker reads and documents only; worker does not commit.
- Independent reviewer recomputes every source anchor and matrix row.
- Designated closer owns accepted material changes and the completion review.
- Session-sync steward updates protected continuity in a separate batch.

## Required First Reads

- `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and the
  active handoff named there.
- `docs/reference/guard_orientation/README.md`.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
- `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md`.
- paired GC-018 and this work order.
- `docs/reviews/CVF_SOT3_APP_T1_R1_COMPLETION_REVIEW_2026-07-17.md`.
- `docs/reviews/CVF_SOT3_APP_T1_R1_CONTRACT_RATIFICATION_COMPLETENESS_AND_BINDING_CORRECTION_2026-07-17.md` as retained semantic evidence.
- `docs/reviews/CVF_SOT3_APP_T0B_COMPLETION_2026-07-16.md` and the accepted
  T0B full-corpus ledger.
- `docs/reference/sot_three_layer/README.md` and its contract-chain and
  invariants documents.
- every current CVF and downstream source path named below.

## Pre-Flight Checks

Capture `executionBaseHead`; require clean status; verify both output paths are
absent; verify the copied-folder root still exists; compare the objective file
set and digest anchors with accepted T0B evidence; stop on drift or collision.

## Write Ownership

Exactly two new files in the fulfillment manifest. Every existing file and the
entire copied SOT-Application root are read-only for the worker.

## Evidence Requirements

Use direct file, line, section, symbol, import/export, and caller evidence for
every contract claim. Record exact searches and denominators for the
contract-bearing path inventory and decision consumers. Separate current CVF
authority, downstream local behavior, compatibility design, and later
implementation requirements. Back the exact changed set, unchanged HEAD, and
nothing-staged claims with Git commands.

## Target / Source

Read-only source root:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Current CVF owner surfaces are only those directly evidenced in committed CVF
source. The copied folder's `.cvf` target strings and local adapter names are
claims to compare, not proof of compatibility or runtime binding.

## Scope / Target / Owner Boundary

T1 covers business-domain ownership, local CVF adapter ports, current CVF
public exports, T8 packet binding, continuation decisions, evidence, and
freeze. It produces a compatibility design and blocker ledger, not code.

## Operator Checkpoint

Standing authority releases this documentation worker. Any source mutation,
application execution, provider/live proof, public export, or T2 hardening
requires later governed authorization.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| routing mode | `MULTI_AGENT_MULTI_ROLE` |
| intake summary | source-backed downstream contract ratification after accepted copied-folder intake |
| scope classification | documentation-only contract and compatibility assessment |
| risk sensitivity | authority duplication, enum conflation, unsafe continuation, hidden-clone coupling, evidence/freeze overclaim |
| selected role route | dispatcher, no-commit worker, independent reviewer/closer, session-sync steward |
| escalation condition | drift, missing source, contradictory current owner, collision, or need for forbidden mutation |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T0B accepted predecessor | `docs/reviews/CVF_SOT3_APP_T0B_COMPLETION_2026-07-16.md`; material commit `577237cba` | accepted full-corpus semantic/provenance evidence exists | ACCEPT |
| MAO-OA completion | closed roadmap at material commit `fef756a14` | separately required roadmap complete | ACCEPT |
| T1-R1 review | `docs/reviews/CVF_SOT3_APP_T1_R1_COMPLETION_REVIEW_2026-07-17.md`; material commit `1300c3505`; `REVIEWED_NOT_ACCEPTED_R2_REQUIRED` | one correction packet must resolve exact membership and caller closure | ACCEPT |
| clean dispatch base | `20a4be366`; `git status --short` empty before authoring | no cross-batch residue | ACCEPT |
| T2 release | explicitly excluded | T1-R2 must close through independent review first | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T1-R2 --title "Exact Inventory Membership And Caller Closure Correction" --date 2026-07-17 --base 20a4be366 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T1-R1 review 1300c3505 requires exact membership and caller closure" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source families, two-path output, external-source controls, owner/consumer matrices, T8/evidence/freeze compatibility design |
| checkerReadAheadConfirmation | applicable dispatch, source, handoff, trace, external-absorption, worker-return, public, freshness, and size checkers reviewed |
| docOnlyNewFields | continuation disposition tokens listed below |
| claimBoundary | scaffold use does not ratify contracts or prove behavior |

## Worker Autonomy / No-Question Rule

Repair allowed-scope documentation or checker-shape defects directly. Return
to the orchestrator only for source drift, contradiction, missing authority,
collision, or a required action outside the two-path write boundary. Do not
fill evidence gaps from chat, provider memory, or naming similarity.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`downstream contract inventory caller closure correction`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "downstream contract inventory caller closure correction" --role worker --lifecycle-phase pre-implementation --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_roadmap_closure_freshness.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; exact manifests; external-source controls; Dual Agent Surface Matrix; handoff route; reviewer conversion; worker-return shape; trace; public disposition; claim boundary |
| gateRunPurpose | confirm packet shape before worker execution |
| claimBoundary | source-code review and gate PASS do not establish downstream compatibility |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 objective and release rule | EXISTS | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | Work Plan; Acceptance Criteria | `SOT3-APP-T1-R2` | SOT3-APP roadmap | ACCEPT |
| consolidated R2 findings | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T1_R1_COMPLETION_REVIEW_2026-07-17.md` | F1; F2; Root-Cause Consolidation Matrix | `REVIEWED_NOT_ACCEPTED_R2_REQUIRED` | independent T1-R1 reviewer | ACCEPT |
| packet identity and hash are distinct | VALUE_SET | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/refinery-packet.ts` | `RefineryPacketRef` | `refinery_packet_id; content_hash` | Truth Kernel Refinery packet reference | ACCEPT |
| evaluation identity and hash are distinct | VALUE_SET | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `EvaluateInput` | `packetReference; packetHash` | Truth Kernel evaluation input | ACCEPT |
| local CVF entry adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\cvf-entry.adapter.ts` | exported adapter class | `CVFEntryAdapter` | downstream local binding | ACCEPT |
| local Refinery adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\refinery.adapter.ts` | exported adapter class | `RefineryAdapter` | downstream local binding | ACCEPT |
| local Kernel adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\truth-kernel.adapter.ts` | exported adapter class | `TruthKernelAdapter` | downstream local binding | ACCEPT |
| local Flow adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\truth-flow.adapter.ts` | exported adapter class | `TruthFlowAdapter` | downstream local binding | ACCEPT |
| local Guard adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\guard-contract.adapter.ts` | exported adapter class | `GuardContractAdapter` | downstream local binding | ACCEPT |
| local phase adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\phase-governance.adapter.ts` | exported adapter class | `PhaseGovernanceAdapter` | downstream local binding | ACCEPT |
| local governed-execution adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\governed-execution.adapter.ts` | exported adapter class | `GovernedExecutionAdapter` | downstream local binding | ACCEPT |
| local evidence adapter | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\evidence.adapter.ts` | exported adapter class | `EvidenceAdapter` | downstream local binding | ACCEPT |
| local binding barrel exports eight adapters | VALUE_SET | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\index.ts` | export statements | `cvf-entry; refinery; truth-kernel; truth-flow; guard-contract; phase-governance; governed-execution; evidence` | downstream binding barrel | ACCEPT |
| binding-health owner | EXISTS | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\binding-health.ts` | pure binding-health function | `buildBindingHealth` | downstream local binding utility | ACCEPT |
| Refinery-to-Kernel workflow consumer | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\workflows\src\refinery-to-kernel.workflow.ts` | workflow return | `kernel.evaluatePacket` | downstream workflow | ACCEPT |
| Kernel-to-SOT workflow consumer | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\workflows\src\kernel-to-sot.workflow.ts` | workflow invocation | `KernelToSOTWorkflow` | downstream workflow | ACCEPT |
| five downstream route-decision values | VALUE_SET | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\contracts\src\types\context-package.ts` | line 16 | `route_decision` | downstream `ContextPackage` | ACCEPT |
| local Truth Flow adapter returns every non-BLOCK value | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\truth-flow.adapter.ts` | lines 17-36 | `TruthFlowAdapter.route` | downstream local adapter | ACCEPT |
| context builder persists route decision and evidence | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\application\src\services\context-builder.service.ts` | lines 26-54 | `ContextBuilderService.build` | downstream application service | ACCEPT |
| governed output stops only BLOCK before execution | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\application\src\services\governed-output.service.ts` | lines 19-26 | `GovernedOutputService.create` | downstream application service | ACCEPT |
| context usability stops only BLOCK or expiry | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\domain\src\entities\context-package.ts` | lines 6-10 | `GovernedContextPackage.assertUsable` | downstream domain entity | ACCEPT |
| downstream Kernel decision values are a distinct set | VALUE_SET | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\truth-kernel.adapter.ts` | lines 3-7 | `KernelEvaluationResult.decision` | downstream local Kernel adapter | ACCEPT |
| downstream binding targets are relative and unpinned | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T0B_FULL_CORPUS_SEMANTIC_AND_PROVENANCE_LEDGER_2026-07-16.md` | declaration ledger DEC-05 through DEC-11 | `BINDING_TARGET` | accepted T0B provenance ledger | ACCEPT |
| T8 profile value is canonical and Refinery-owned | VALUE_SET | `EXTENSIONS/CVF_REFINERY/src/packet-hash/packet-hash.ts` | lines 18-19; 181-183 | `REFINERY_PACKET_HASH_PROFILE` | Refinery packet-hash owner | ACCEPT |
| T8 hash is a public Refinery export | EXISTS | `EXTENSIONS/CVF_REFINERY/src/index.ts` | lines 36-43 | `computeRefineryPacketHash` | Refinery public barrel | ACCEPT |
| current Kernel public export | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts` | lines 4-46 | `TruthKernel` | Truth Kernel public barrel | ACCEPT |
| current Flow public exports do not declare the local five-value decision interface | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts` | lines 4-33 | `DistributionEngine` | Truth Flow public barrel | ACCEPT |
| current Guard public entry surface | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | lines 12-130 | `createGuardEngine` | Guard Contract barrel/factory | ACCEPT |
| canonical SOT3 owner chain | LITERAL_INVARIANT | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | Layer Boundary Decisions; contract sections | `KernelDecision` | SOT3 contract chain | ACCEPT |
| review/freeze local service requires approvals and phase gate | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\application\src\services\review-freeze.service.ts` | lines 12-34 | `ReviewFreezeService.freeze` | downstream application service | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `CONTINUE` | ratified matrix says the caller may proceed without a newly required review hold | NONE |
| `CONTINUE_WITH_OBLIGATIONS` | proceed only while named obligations remain attached and enforced by a later implementation | NONE |
| `HOLD_FOR_REVIEW` | do not enter output/provider/freeze lane before named review resolves | NONE |
| `STOP` | no downstream continuation | NONE |
| `SOURCE_CONTRADICTION` | direct sources do not support one safe semantic disposition | NONE |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | SOURCE_VISIBLE_BEHAVIOR_ONLY |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | current committed CVF source and direct external source reads |
| requiredExecutionBase | clean post-dispatch HEAD |
| liveAction | N/A with reason: T1 performs no run or provider call |

## Negative Search And Collision Discipline

Before create, run `Test-Path` for both outputs and exact-title searches across
`docs/reviews`, `docs/work_orders`, `docs/baselines`, `docs/roadmaps`, and
`CVF_SESSION`. Any existing target or conflicting active T1 owner blocks.

## Evidence Reuse And Encoding Plan

Accepted T0B evidence may supply corpus identity and provenance anchors only.
Every T1 symbol, value, consumer, and owner comparison must be re-read from
direct source. Write ASCII and quote non-ASCII only if direct evidence requires
it.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | operator-authored downstream copied folder already accepted through T0B intake |
| Upstream or source-mirror disposition | `LOCAL_OPERATOR_AUTHORED_INPUT_WITHOUT_UPSTREAM`; hidden clone is a declared target, not authority |
| Enumeration or manifest plan | consume accepted 336-file T0B identity; freshly enumerate every contract/consumer path reached by exact symbol searches |
| Per-file terminal-ledger plan | not a new 336-file rescan; contract-bearing path inventory must reach zero unresolved consumers |
| Owner or overlap route | current CVF owner, downstream business owner, compatibility-rewrite owner, or source contradiction |
| Value-disposition route | ADAPT_CONTRACT, REJECT_DIRECT_IMPORT, DEFER_TO_T2, or NO_NEW_VALUE |
| Claim boundary | documentation compatibility design only |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | contract-bearing subset of accepted 336-file copied folder |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact symbol searches plus import/export/caller traversal for each named interface and decision field |
| Blind-spot prevention action | enumerate every producer, transformer, persistence edge, consumer, output gate, review gate, and freeze gate |
| Residual gap | behavior proof and mutation remain T2/T3 work |
| Blind-spot verdict | ZERO_UNRESOLVED_DECISION_CONSUMERS_REQUIRED |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | literal read-only SOT-Application root |
| Enumeration command | hidden-inclusive `rg`/filesystem search limited to contract symbols, values, exports, imports, and callers |
| Manifest artifact or inline manifest | accepted T0B 336-row ledger; T1 inline contract-bearing path inventory |
| Processing ledger artifact or inline ledger | T1 ratification artifact |
| Ledger terminal statuses | SOURCE_VERIFIED, OWNER_MAPPED, REJECT_DIRECT_IMPORT, DEFER_TO_T2, SOURCE_CONTRADICTION |
| Disposition taxonomy | ADAPT_CONTRACT, REJECT_DIRECT_IMPORT, DEFER_TO_T2, NO_NEW_VALUE |
| Owner-surface map | T1 business/CVF/T8/evidence/freeze owner matrix |
| Unresolved items | zero allowed at worker completion; contradiction must be terminal and blocking |
| Completion claim boundary | contract ratification evidence only |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| local business/domain contracts | downstream product meaning | ADAPT_CONTRACT | sibling application design | T2 may implement only reviewer-ratified semantics | no mutation in T1 |
| local CVF-shaped adapters | interface candidates | REJECT_DIRECT_IMPORT unless exact current owner match | current CVF public exports | compatibility rewrite design | no import |
| five-value route enum | downstream continuation vocabulary | ADAPT_CONTRACT | explicit consumer matrix | T2 negative behavior | no runtime proof |
| packet-ID-only Kernel forwarding | binding gap | REJECT_DIRECT_IMPORT | Refinery T8 packet hash owner | explicit compatibility design | no T8 reopening |
| evidence/freeze shapes | downstream evidence pattern | ADAPT_CONTRACT or DEFER_TO_T2 | current evidence/review/phase owners | reviewer-ratified mapping | no freeze claim |

## Overlap And Novelty Classification

| Source group | Existing owner checked | Overlap disposition | Delta | Action |
|---|---|---|---|---|
| business-domain entities/services | SOT3 core owner chain | DOWNSTREAM_OWNER | product-specific orchestration | retain outside Core |
| local Refinery/Kernel/Flow adapters | current extension public barrels | REJECT_DIRECT_IMPORT | interface and decision mismatch | design compatibility layer |
| T8 binding | Refinery packet-hash public export | CONFIRMED_EXISTING | application forwards packet ID only | consume owner API later |
| evidence/freeze | current phase/guard/evidence owners | ENRICH_EXISTING | local release-state patterns | map without authority duplication |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | operator intent -> T0A/T0B intake -> T1 contract ratification -> independent review |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | SOT3-APP roadmap and T1 ratification artifact |
| Disposition | ADAPT contract evidence only |
| Claim boundary | provider-local memory and copied-folder declarations are not CVF authority |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - T1 does not claim a fresh full
  336-file corpus rescan; accepted T0B owns that denominator.
- T1 completeness denominator: every file returned by exact searches for
  `route_decision`, `TruthFlowResult`, `TruthFlowAdapter`, `ContextPackage`,
  `KernelEvaluationResult`, `TruthKernelAdapter`, `refinery_packet`, evidence,
  review, and freeze symbols, followed through imports/exports/callers.
- T1 completion requires a terminal inventory with zero unresolved decision
  consumers and an explicit source-drift comparison against T0B anchors.
- Any unreadable contract-bearing path or unexplained consumer blocks return.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| applicability | NOT_APPLICABLE_WITH_REASON |
| reason | exactly two markdown review outputs; no storage, cache, database, index, mirror, or aggregate |
| owner boundary | established `docs/reviews/` artifact family |
| future trigger | source/runtime/generated-state work requires a later packet |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | committed packet and exact two outputs | read sources, write docs, no commit | direct-source matrices and command evidence | local filesystem only | ACTIVE_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | no downstream external adapter ratified | no CLI/MCP ingress, runtime dependency resolution, or product claim | explicit absence | future source-verified adapter packet | DEFERRED_WITH_REASON |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Worker control | Required evidence |
|---|---|---|
| business-domain owner map | map each entity/service/workflow to downstream versus CVF authority | owner matrix |
| current CVF public adapters | compare each local binding port with exact current public exports | adapter compatibility matrix |
| T8 packet binding | contrast packet-ID-only path with Refinery hash profile/export | T8 compatibility design |
| five decision semantics | classify every value at every consumer | continuation matrix |
| evidence and freeze | map evidence creation, review prerequisites, phase gate, hash, and authority ceiling | evidence/freeze matrix |
| no source mutation | exactly two documentation paths | Git evidence |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_SOT3_APP_T1_R2_EXACT_INVENTORY_MEMBERSHIP_AND_CALLER_CLOSURE_CORRECTION_2026-07-17.md` | create complete source-verified ratification and compatibility design |
| `docs/reviews/CVF_SOT3_APP_T1_R2_WORKER_RETURN_2026-07-17.md` | create exact two-path no-commit worker return |

## Required Artifact Manifest

| Artifact group | Owner | Required status |
|---|---|---|
| two worker paths | worker | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON |
| completion review and packet/roadmap closure edits | independent reviewer/closer | REVIEWER_TO_DECIDE |
| protected continuity | session-sync steward | REVIEWER_TO_DECIDE |

## Execution Plan

1. Capture clean base, output absence, and T1-R1 review continuity.
2. Rerun the exact 80-file seed search and publish all 80 normalized relative
   paths individually, sorted, with group and terminal classification columns.
3. Derive group counts from the explicit membership ledger. Counts must show
   commands=10, domain=4, SQLite repositories=7, docs/fixtures/samples=7, and
   all group totals must sum to 80 without offsetting errors.
4. Preserve the 14-file literal-match set under the exact label
   `LITERAL_MATCH_SET`, never `decision-consumer subset`.
5. Build `CALLER_CLOSURE_SET` through a documented second-stage traversal of
   adapter/service method definitions, imports, constructor injection,
   invocations, returned results, field inspection, persistence/projection,
   workflow edges, and tests. Include `refinery-to-kernel.workflow.ts` and
   `sot-to-context.workflow.ts` even though they are outside the 14 literals.
6. Give every caller edge one terminal row with producer, method/symbol,
   caller, operation, inspected-or-pass-through result, and source anchor.
7. Cite the accepted R1 adapter/hash/continuation matrices as retained facts;
   do not rewrite or broaden them unless direct source drift is found.
8. Run the full worker-return fast gate and Git evidence; leave exactly two
   uncommitted paths.

## Consolidated T1-R2 Correction Mandate

| Finding | Required terminal correction | Fail condition |
|---|---|---|
| offsetting membership/count defects | exact 80-row ledger and machine-derived totals | representative-only paths, manual totals, omitted file, or offsetting errors |
| literal search mislabeled as consumer closure | separate `LITERAL_MATCH_SET` and traversal-derived `CALLER_CLOSURE_SET` | calling 14 literals a consumer denominator or omitting caller edges |
| retained R1 semantic facts | cite accepted sections without reopening them | unnecessary rework or semantic drift without new source evidence |

## Required Ratification Structure

The main artifact must contain: Executive Disposition; Authority And Source
Snapshot; Exact 80-File Membership Ledger; Derived Group Count Reconciliation;
Literal Match Set; Caller Closure Method; Caller Closure Edge Ledger; Retained
R1 Fact Index; Zero-Unresolved Reconciliation; Machine Closure Package;
Epistemic Process; Agent Operation Trace; Public Export Disposition; Claim
Boundary.

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned review artifact, read the checker source for
its path, status, docType, conditional external-source terms, trace, delta,
public disposition, and worker-return shape. Do not place heading-shaped
checklist literals before the real sections.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_APP_T1_R2_WORKER_RETURN_2026-07-17.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include the execution base, exact two-path manifest, commands,
path-inventory reconciliation, decision-consumer denominator, no-commit proof,
and terminal status.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher, documentation worker, independent reviewer/designated closer, session-sync steward |
| phase | `EXECUTION` |
| baseHeadFor(phase) | dispatchBaseHead=`20a4be366`; executionBaseHead=worker captures committed post-dispatch HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | execution is exactly two new review paths |
| traceScope(phase, actor) | worker records source inventory/matrices/Git proof; reviewer recomputes; closer commits; steward syncs |
| commitOwner(phase) | worker forbidden; reviewer owns material commit |
| crossBatchIsolation | T0B and MAO-OA are closed; T2/later, T6B, runtime, public, and continuity work excluded |
| Before status evidence | clean worktree required at execution start |
| nextMoveSurfaces | worker cannot edit; reviewer may release T2 packet authoring only after accepted T1 closure |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T1_R2_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | accepted two worker outputs; completion review; paired baseline/work-order dispositions; SOT3-APP roadmap T1 closure state |
| closureOwner | independent reviewer/designated closer |
| workerCommitPermission | FORBIDDEN |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git status --short --untracked-files=all
git diff --cached --name-only
git rev-parse --short HEAD
```

## Acceptance Criteria

- Exact two-path output and unchanged worker HEAD.
- Exact seed command reproduces 80 paths and the artifact lists all 80 individually.
- Derived group counts match exact membership with 10 commands, 4 domain files, 7 SQLite repositories, and 7 docs/fixtures/samples.
- The 14-file literal set is labeled only as `LITERAL_MATCH_SET`.
- Caller closure is separately traversed and includes every adapter/service/workflow/test edge, including both previously omitted workflows.
- Every caller edge has one terminal row and zero unresolved edges remain.
- Accepted R1 adapter/hash/continuation facts are retained without unsupported expansion.
- No source/runtime/live/public or integration claim is made.

## Review Gate

The reviewer must rerun searches, open every cited source, recompute consumer
counts and matrices, challenge the proposed semantics, and reject any row that
uses naming similarity or local declaration as compatibility proof.

## Closure Diff Gate

Missing consumer, conflated Flow/Kernel vocabulary, unverified current owner,
packet-ID-only T8 acceptance, vague evidence/freeze authority, unexplained
drift, extra path, staged content, or worker commit fails closure.

## Closure Checklist

- Dependency evidence is current and source-backed.
- Exactly two worker output paths are present.
- Contract-bearing path and decision-consumer reconciliations are complete.
- Five-value Flow and distinct Kernel matrices are source-backed.
- T8, evidence, and freeze boundaries are explicit.
- No copied-folder, CVF source, runtime, registry, continuity, or public write
  occurred.
- Independent reviewer owns acceptance, material commit, and T1 closure.
- T2 remains parked until accepted closure evidence exists.

## Return-To-Orchestrator Conditions

Return blocked on snapshot drift, missing/unreadable contract source,
irreconcilable owner contradiction, nonzero unresolved consumers, output-path
collision, or any required mutation outside the exact two paths.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | SOT3-APP-T1-R2 dispatch, 2026-07-17 |
| Working directory | repository root plus read-only copied-folder source |
| Command or tool surface | direct source reads, searches, resolver, scaffold, patch, gates |
| Target paths | paired baseline, work order, SOT3-APP roadmap |
| Allowed scope source | operator sequence, accepted T0B, MAO-OA closure, SOT3-APP roadmap |
| Before status evidence | clean worktree at `20a4be366` |
| After status evidence | source-verified T1 dispatch packet |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring and two-path documentation execution |
| Claim boundary | no worker result or contract ratification at dispatch |
| Agent type | dispatcher |
| Invocation ID | `sot3-app-t1-dispatch-2026-07-17` |
| Expected manifest | baseline, work order, roadmap |
| Actual changed set | baseline, work order, roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only contract ratification dispatch |
| claimDisposition | CLAIM_REJECTED: no application execution or contract compatibility is proven at dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | read-only source inspection and two review outputs only |
| interceptionBoundary | no runtime gate, wrapper, proxy, provider, IDE, MCP, Web, or production interception |
| claimLanguage | source-visible behavior and compatibility design only |
| forbiddenExpansion | source mutation, test/build/run, provider/live, T2, public-sync, push, production |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_APP_T1_R2_COMPLETION_REVIEW_2026-07-17.md` | N/A with reason: independent reviewer creates it after worker return | N/A with reason |
| Roadmap state | SOT3-APP roadmap | `Status: SOT3_APP_T1_R2_DISPATCHED_WORKER_NEXT` | PASS |
| Registry JSON | existing GC-051 corpus registry | aggregate drift and registry checks pass; T1 adds no source/test path | PASS |
| Registry Markdown | existing GC-051 registry documentation contract | unchanged; registry checks pass | PASS |
| External evidence digest | accepted T0B ledger sha256 `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee` plus planned T1 contract inventory | accepted snapshot retained; no new full-corpus claim | PASS |
| System loop interlock | T1-R1 review -> T1-R2 execution and independent review | T2 parked | PASS |
| Session continuity | N/A with reason: separate steward batch follows material commit | no protected continuity mutation in this packet | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public export is authorized.

## Claim Boundary

This packet authorizes exactly two documentation outputs. It does not ratify
contracts in advance, accept local adapters as CVF owners, reopen SOT3-T8,
authorize application mutation or T2, run tests/build/provider/live work,
change registries or continuity, export public artifacts, or claim integration,
runtime governance, user value, production readiness, certification, shipment,
or scale.
