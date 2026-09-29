# CVF GC-018 Baseline - SOT3-APP-T0A Corpus Freeze And Semantic Calibration

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-16

Batch ID: `SOT3-APP-T0A`

Dispatch base head: `e7f45e120`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated source-intake worker role

Source intake decision packet: REQUIRED

## Purpose

Authorize the first phase of the full-corpus SOT Application intake: freeze
objective metadata for all 336 files, enumerate every hidden-clone declaration,
and calibrate semantic disposition on an exact reviewer-selected 20-file sample
before any 336-row semantic propagation or application mutation.

## Operator Source Intent And Chronology

The operator attests that both named source folders were authored after the
SOT3 work to respond to two remaining gaps. This is source-intent evidence, not
a claim that either folder is CVF authority and not an exact filesystem date
claim.

| Source root | Operator-attested source class | Gap-response purpose | Authority boundary |
|---|---|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application` | `POST_SOT3_DOWNSTREAM_PRODUCT_GAP_RESPONSE` | test whether bounded SOT3 governance can support a complete downstream business lifecycle from source and authority through context, output, review, freeze, impact, and recall | external operator-authored evidence input only |
| `.private_reference/legacy/CVF_SOT 10.07/cvf_four_surface_control_boundary_patch` | `POST_SOT3_CONTROL_BOUNDARY_GAP_RESPONSE` | make controlled object, control mode, timing, maturity, evidence, bypass, and failure semantics explicit | private reference evidence input only; its storage under `legacy` is not semantic or chronological classification |

This T0A packet processes only the SOT-Application root. The Four-Surface root
remains governed by its separate accepted FSCB ledger/crosswalk. Local file
modification times may support diagnostics but are not authorship or chronology
authority. No source concept becomes canonical until a CVF-owned owner surface
accepts it through a later governed decision.

## Scope / Target / Owner Boundary

Read-only source root:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Read-only hidden dependency target, Git metadata only:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\.Controlled-Vibe-Framework-CVF`.

Writable outputs are exactly the two review artifacts named in the work order.
T0A owns objective corpus freeze, declaration enumeration, and sample
calibration only. T0B owns full-body semantic disposition for all 336 files and
remains dependency-held. CVF canonical contracts and owner surfaces remain the
authority; the source folders are evidence inputs.

## Proposed Tranche / Decision

Decision: `PROCEED_WITH_T0A_FULL_METADATA_AND_SAMPLE_CALIBRATION`.

The 50-100-file reduced-corpus completion option is rejected. T0A retains all
336 files in the metadata ledger while limiting semantic judgment to the exact
20-file sample below. Metadata completion must not be described as semantic
absorption completion.

## Dependency Release Evidence

| Dependency | Accepted artifact | Material commit | Final disposition | Release result |
|---|---|---|---|---|
| operator intake authorization | `docs/reviews/CVF_SOT3_DOWNSTREAM_APPLICATION_AND_FOUR_SURFACE_ABSORPTION_INTAKE_REVIEW_2026-07-15.md` | `24d50f0d7` | `OPERATOR_AUTHORIZED_FOR_ROADMAP_AUTHORING` | PASS |
| scope-split decision | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | `55007483c` | `ACCEPT_TWO_PHASE_FULL_CORPUS_WITH_CHANGES` | PASS for T0A packet authoring |
| continuity release | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `e7f45e120` | `sot3_app_t0_scope_split_packet_authoring_next` | PASS for T0A packet authoring |
| roadmap T0A route | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | current dispatch batch | `T0A_DISPATCH_READY` | PASS for T0A only |

T0B is not released by these rows. It requires accepted T0A reviewer evidence
and a fresh dependency-backed packet.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| scope review selected a two-phase full-corpus route | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | Decision / Disposition | `ACCEPT_TWO_PHASE_FULL_CORPUS_WITH_CHANGES` | governed scope-blocker review | ACCEPT |
| T0A requires 336 metadata rows and a stratified 20-row sample | VALUE_SET | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | Work Plan | `SOT3-APP-T0A` | SOT3-APP roadmap | ACCEPT |
| T0B remains dependency-held | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | Decision / Disposition | `T0B release` | governed scope-blocker review | ACCEPT |
| external absorption requires a manifest, processing ledger, value conversion, and owner map | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Central Core | `External Absorption Core` | external absorption standard | ACCEPT |
| corpus evidence requires safe enumeration and explicit reconciliation | LITERAL_INVARIANT | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | Corpus Manifest; Processing Ledger; Reconciliation | `Corpus Completeness And Report Integrity` | corpus completeness standard | ACCEPT |
| source-intake packets require bounded scope and overlap routing | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` | Required Packet Fields | `Source Intake Decision Packet` | source-intake packet standard | ACCEPT |
| current physical snapshot contains 336 files and 238522 bytes | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | External Absorption Core | `Manifest artifact or inline manifest` | retained corrected snapshot evidence | ACCEPT |
| current canonical aggregate uses ordinal normalized-path ordering | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T0_BLOCKED_RETURN_REVIEW_2026-07-15.md` | Findings / Position | `canonical ordinal aggregate` | independent digest review | ACCEPT |

The operator chronology attestation is intentionally not represented as an
existing runtime/source fact in this table. It is recorded in the dedicated
source-intent section and must be treated as operator-provided provenance.

## New Doc-Only Fields

| Output | New fields | Classification | Boundary |
|---|---|---|---|
| 336-row metadata ledger | sourceId, relativePath, bytes, sha256, metadataState | DOC_ONLY_NEW | metadata evidence only; `metadataState=METADATA_FROZEN` is not a semantic terminal status |
| 20-row calibration ledger | sampleId, sampleGroup, sourcePath, sourceSha256, processingStatus, disposition, valueClass, overlapClass, ownerRoute, nextGovernedAction, reason, adversarialChallenge | DOC_ONLY_NEW | sample judgment only; no propagation to un-sampled rows |
| hidden-clone inventory | declarationId, sourcePath, sourceLine, literalTarget, declarationClass, resolvedTarget, targetExists, candidateOwnerRoute, candidateDriftDisposition, candidateRuntimeUseDisposition, t0aState | DOC_ONLY_NEW | complete declaration enumeration; terminal provenance decisions remain T0B-owned |
| aggregate receipt | fileCount, totalBytes, aggregateSha256, snapshotTime, executionBaseHead | DOC_ONLY_NEW | reproducibility evidence only |
| source-intent record | operatorAttestation, sourceClass, gapResponsePurpose, authorityBoundary | DOC_ONLY_NEW | operator provenance; not runtime authority |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned baseline path | exact `Test-Path` before authoring returned false | CLEAR |
| planned work-order path | exact `Test-Path` before authoring returned false | CLEAR |
| both planned worker output paths | exact `Test-Path` before authoring returned false | CLEAR |
| optional completion path | exact `Test-Path` before authoring returned false | CLEAR_OPTIONAL_NOT_CREATED |
| token search | `rg -n "SOT3-APP-T0A|SOT3_APP_T0A" docs CVF_SESSION` before authoring found only roadmap/session planning references | EXPECTED_PREDECESSOR_REFERENCES_ONLY |
| collision decision | no T0A baseline, work order, ledger, worker return, or completion review existed | CREATE_NEW_BOUNDED_PACKET |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md

priorVerificationAnchor: 55007483c

freshRecomputeRequired: true

unicodePathHandling: preserve literal filesystem paths; sort normalized relative paths with ordinal comparison only for the aggregate receipt

extractedTextAuthority: direct file bytes and direct decoded text are evidence; rendered summaries and provider memory are not source authority

Prior counts, hashes, declarations, and semantic observations are navigation
evidence only. The worker must recompute every T0A acceptance fact from the
current physical source and record any drift rather than copying a prior value.

## Source Intake Decision Packet

| Field | Value |
|---|---|
| Decision packet standard | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` |
| Input root or repository | literal SOT-Application source root in Scope / Target / Owner Boundary |
| Bounded scope | 336 metadata rows, complete hidden-clone declaration inventory, exact 20-row semantic calibration sample |
| Enumeration authority | physical filesystem using `rg --files --hidden --no-ignore`, per-file byte/hash reads, and ordinal normalized-path aggregation |
| Owner-surface taxonomy | CONFIRMED_EXISTING, ENRICH_EXISTING, NEW_FINDING, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, OWNER_SURFACE_NOT_FOUND |
| Pre-scan packet source | scope review `55007483c`, current roadmap, this GC-018, and paired work order |
| Overlap routing matrix | exact sample rows must map to current CVF owner, pending downstream owner, or no-owner route and record a concrete next governed action |
| Negative-search evidence | negative-search command `rg -n "SOT3-APP-T0A|SOT3_APP_T0A" docs CVF_SESSION`, collision table above, and worker recheck before creating either output |
| Core disposition | ADAPT full-corpus metadata and sample-calibration evidence only |
| Value conversion requirement | every sample row receives a canonical conversion lane and next governed action |
| Overlap classification requirement | every sample row receives an owner/novelty classification; no new owner is promoted in T0A |
| Worker output path | metadata/sample ledger plus no-commit worker return named by the paired work order |
| Forbidden scope | un-sampled semantic disposition, T0B release, source mutation, runtime/build/test/live/public action |
| Claim boundary | partial intake calibration only; no full absorption or product-readiness claim |

## Current External Source Snapshot

Dispatcher recomputation from the literal source root on 2026-07-16 produced:

| Evidence item | Current value | Method | Claim class |
|---|---|---|---|
| physical file count | 336 | recursive hidden-inclusive filesystem enumeration | FILESYSTEM_SNAPSHOT |
| total bytes | 238522 | sum of physical file lengths | FILESYSTEM_SNAPSHOT |
| aggregate SHA-256 | `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee` | ordinal sort of `relativePath<TAB>bytes<TAB>sha256<LF>`, forward slashes, UTF-8 no BOM | REPRODUCIBILITY_SNAPSHOT |
| hidden-clone declaration occurrences | 13 | `rg -n --hidden --no-ignore -F '.Controlled-Vibe-Framework-CVF'` | DECLARATION_INVENTORY_BASELINE |
| hidden target HEAD | `a78b35c` | read-only Git metadata | REPOSITORY_METADATA_ONLY |
| hidden target remote | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | read-only `git remote -v` | REPOSITORY_METADATA_ONLY |
| hidden target working tree | clean | read-only `git status --short` | REPOSITORY_METADATA_ONLY |

Any mismatch at worker start is a stop condition. Count and byte parity do not
override an aggregate mismatch.

## Reviewer-Selected Semantic Calibration Sample

The worker must process exactly these 20 paths. Replacement, convenience
sampling, or sample-size reduction is forbidden without a fresh packet.

| Sample ID | Group | Relative path | Dispatch SHA-256 | Calibration purpose |
|---|---|---|---|---|
| SAM-01 | doctrine | `README.md` | `5d01f41b7e9de5c7f86a42a1f36d533bcd7bf0aba7c7f2bedc8ec69a6f95be8b` | product boundary and full lifecycle claim |
| SAM-02 | doctrine | `docs/ARCHITECTURE.md` | `1cff0111b87b1849b2deae8023c62ba54fec6b71f7204eea63d930c0d76cedf9` | downstream/core ownership split |
| SAM-03 | doctrine | `docs/CLAIM_BOUNDARY.md` | `fb2b3b5faf6a2e3c313aac3d63623e21b31003a122b956cbcad9b22e11143886` | overclaim and evidence boundary |
| SAM-04 | doctrine | `docs/REVIEW_FREEZE_PROTOCOL.md` | `60da0585588db647aa7249af8516cdeae1848c6c952a2a3582265e5d6154623e` | review/freeze semantics |
| SAM-05 | no-new-value control | `TREEVIEW.md` | `208f4b0708f20f9115450cac7035cc2e47ff85010a313808fd5a370801265bce` | navigation duplication and latent-value challenge |
| SAM-06 | provenance | `.cvf/manifest.json` | `21d1ab9073f154f15d30784b4044437b650c9b645f76f1a2f4aa9fdf0e2958dc` | hidden governance root declaration |
| SAM-07 | provenance | `.cvf/bindings/truth-kernel.binding.json` | `a696ddbef39870bd8b6c633c6354c61da039b2bef94d992e0bd65505ccc39666` | Kernel binding declaration and version gap |
| SAM-08 | provenance | `.cvf/bindings/truth-flow.binding.json` | `238b416f4eeb85c656b06e85545dd737a96dd57d74095c06ce5a9e4c51505b79` | Flow binding declaration and version gap |
| SAM-09 | provenance | `.env.example` | `3a369c5ed83c1618740f371cfb9772776b86451d643e89b40b07006757059667` | environment default coupling |
| SAM-10 | provenance | `apps/api/src/config.ts` | `22ae2e2f83c600bfdcf9fffd8ad948e68bc75ccb01d717ab3013247d9dc12fba` | application default coupling |
| SAM-11 | runtime candidate | `packages/cvf-bindings/src/truth-kernel.adapter.ts` | `32fbc200bc2717fc7c7c3477334590fada1d3547ccaa067ba9809d76c38189da` | local adapter versus current T8 contract |
| SAM-12 | runtime candidate | `packages/cvf-bindings/src/truth-flow.adapter.ts` | `ca3e5720fd2adece259ebf7c6722033ba90336abddb0561c52816a3852a61222` | decision semantics and continuation risk |
| SAM-13 | runtime candidate | `packages/application/src/services/governed-output.service.ts` | `6b6e63bf914d09d65fb0fcb0a3f110c08d001e5d6b71738d1cfe2efa01e3f377` | output creation after Flow decision |
| SAM-14 | runtime candidate | `packages/application/src/services/context-builder.service.ts` | `339dd7d45bda7f2c9e35bc76b11a11cb7e6767584a750d6240798894e38c0c7b` | context construction after Flow decision |
| SAM-15 | runtime candidate | `apps/api/src/middleware/cvf-governance.middleware.ts` | `830c354ca3e2d1cf09ca6ac38b1cbbd071562067919f300bc01db5a6f1baf1b8` | phase-gate response and fall-through risk |
| SAM-16 | evidence candidate | `packages/evidence/src/freeze-package.ts` | `bb6d98ce161afff12c315a1172d14eef5d68bc48e6009d863912122ddcafbd5a` | freeze evidence completeness |
| SAM-17 | test-quality | `tests/e2e/controlled-quotation.e2e.test.ts` | `7ee0122074d813427e744ed33322db425a413826872ac61a58da706b9e65eea6` | E2E naming versus actual behavior proof |
| SAM-18 | test-quality | `tests/integration/truth-kernel-binding.test.ts` | `b1801152ceba1b254ad738e09111cd07c1867ed4f527fbb848642929e3cfe8cd` | binding test versus current contract proof |
| SAM-19 | negative-proof | `tests/failure-injection/missing-review.test.ts` | `f451414a0cdfde42f84bbb1684765aa131e6065c0c6d5a62d8d5e268d618d1d6` | missing-review fail-closed evidence |
| SAM-20 | fixture | `fixtures/controlled-quotation/expected-freeze-record.yaml` | `33a25d2d28ef7502fed8b6aaf64ef652d770f0ce59ea32de0d4ef5412f7f13f7` | fixture value versus runtime proof boundary |

## Acceptance Criteria

- all 336 physical paths have one unique metadata row;
- file count, byte total, every per-file hash, and aggregate reconcile;
- metadata rows use `METADATA_FROZEN` and do not masquerade as semantic
  terminal decisions;
- all 13 current hidden-clone occurrences are enumerated with physical line,
  literal target, resolved target, and candidate owner/drift/runtime-use route;
- exactly SAM-01 through SAM-20 are fully read and semantically calibrated;
- every sample row uses one canonical processing status, disposition, value
  conversion lane, owner route, reason, and adversarial challenge;
- sample results explicitly challenge `DEFERRED`, `REJECTED`, and
  `NO_NEW_VALUE` for latent doctrine/package/runtime/checker value;
- reconciliation reports metadata=336, sample=20, semantic unresolved=316,
  declaration occurrences=13, and zero missing/duplicate path;
- corpus verdict remains `PARTIAL`;
- T0B remains held.

## Stop Conditions

Return `BLOCKED_WITH_REASON` without a completion claim when source count,
bytes, aggregate, a sample hash, or hidden declaration count drifts; an input
is unreadable; an exact output path collides; a sample replacement is needed;
the hidden target metadata cannot be read; source mutation or application
execution is required; or a semantic row cannot be source-backed.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | post-SOT3 operator-authored downstream copied-folder gap response |
| Upstream or source-mirror disposition | `LOCAL_OPERATOR_AUTHORED_INPUT_WITHOUT_UPSTREAM`; no local Git provenance; hidden dependency is a separate public clone and not source authority for the application |
| Enumeration or manifest plan | all 336 paths with bytes and SHA-256 plus ordinal aggregate |
| Per-file terminal-ledger plan | T0A metadata state for 336 plus canonical semantic decisions for exact 20-file sample; T0B retains full 336 semantic obligation |
| Owner or overlap route | sample rows map to existing owner, pending downstream owner, reject-direct-import, no-new-value, or no-owner route |
| Value-disposition route | ADAPT metadata evidence and calibrate sample; no full-corpus ABSORB claim |
| Claim boundary | partial intake calibration only; no application/runtime/public completion |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | operator-authored copied-folder gap response |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | complete 336-file metadata plus exact 20-row semantic sample and complete declaration search |
| Blind-spot prevention action | reviewer-selected stratification, full metadata retention, adversarial review of low-value/reject/defer sample rows, T0B full-corpus obligation retained |
| Residual gap | 316 un-sampled semantic decisions and all final declaration dispositions remain T0B-owned |
| Blind-spot verdict | PARTIAL_PENDING_T0A_EXECUTION |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | literal SOT-Application root; local operator-authored input without upstream |
| Enumeration command | `rg --files --hidden --no-ignore` plus filesystem byte/hash reads |
| Manifest artifact or inline manifest | `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md`, planned 336-row metadata table and aggregate receipt |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md`, planned exact 20-row semantic table plus declaration inventory |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table plus `docs/reference/sot_three_layer/README.md` |
| Unresolved items | expected 316 un-sampled semantic file decisions and final declaration dispositions |
| Completion claim boundary | T0A partial calibration; no full external absorption completion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| 336-file metadata | reproducible corpus identity | `DOCTRINE_ADAPTED` | T0A ledger | freeze and reviewer-verify | no runtime/package claim |
| sample doctrine/product files | downstream lifecycle and claim boundaries | `PACKAGE_CANDIDATE` | SOT3-APP roadmap/T1 owner map | calibrate only | no package activation |
| sample adapter/service/middleware files | integration and fail-open candidates | `RUNTIME_CANDIDATE` | future T1/T2 source-verified packet | calibrate owner/risk only | no runtime execution |
| sample test/fixture files | possible proof-quality guard value | `CHECKER_CANDIDATE` | future T3 evidence owner | distinguish behavior-path checks from fixture-only assertions | no checker wiring |
| sample test/fixture files | proof-strength boundary | `REJECT_DIRECT_IMPORT` | future T3 test-quality repair | distinguish fixture/smoke from behavior proof | no proof reuse |
| sample TREEVIEW | navigation or possible latent doctrine | `NO_PACKAGE_OR_RUNTIME_VALUE` candidate | T0A adversarial review | accept only if no latent value is found | no package/runtime value claim |
| hidden-clone declarations | provenance coupling | `RUNTIME_CANDIDATE` | T0A/T0B provenance route | enumerate now; terminally disposition in T0B | no dependency activation |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| three-layer core contracts | `docs/reference/sot_three_layer/README.md` | CONFIRMED_EXISTING | downstream consumer only | sample current compatibility; no core copy |
| T8 packet binding | `EXTENSIONS/CVF_REFINERY/src/packet-hash/packet-hash.ts` | REJECT_DIRECT_IMPORT | application-local binding is not current T8 proof | record incompatibility candidate only |
| downstream business lifecycle | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | post-SOT3 product gap response | keep pending T1 owner ratification |
| Flow decision consumption | `docs/reference/sot_three_layer/README.md` | NEW_FINDING | possible multi-consumer fail-open pattern | calibrate sample; implementation deferred |
| hidden-clone dependency | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | unratified dependency/version owner | enumerate; final disposition deferred |
| navigation/fixtures | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | NO_NEW_VALUE candidate | possible summary/test support only | adversarially challenge before acceptance |

## Reverse Architecture Projection Matrix

| Accepted value group | Catalog/GAP owner check | Disposition before T0A closure | Target source | Claim class | Evidence |
|---|---|---|---|---|---|
| downstream SOT product owner | current as-built catalog | `DEFER_PENDING_ACCEPTANCE` | future existing entity update or proposed GAP | product candidate | sample plus T1 owner map required |
| application integration risks | current runtime owners and GAP registry | `DEFER_PENDING_ACCEPTANCE` | future owner update or GAP | runtime candidate | T0A sample only; no behavior proof |
| control-boundary doctrine | accepted FSCB crosswalk | `NOT_APPLICABLE_WITH_REASON` | separate FSCB owner surface already exists | doctrine evidence only | no Four-Surface mutation in T0A |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | operator intent -> intake review -> scope split -> T0A metadata/sample calibration -> reviewer checkpoint -> fresh T0B decision |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | SOT3-APP roadmap and this paired dispatch packet |
| Disposition | ADAPT metadata and sample evidence only |
| Claim boundary | no full absorption, runtime, public, or product completion |

## Corpus Completeness And Report Integrity

- Corpus task class: full metadata freeze plus semantic calibration for a
  downstream copied-folder application.
- Corpus root: literal SOT-Application source root.
- Snapshot time: dispatcher recomputation on 2026-07-16 at `e7f45e120`.
- Enumeration command: `rg --files --hidden --no-ignore` plus filesystem-backed
  direct byte/hash reads.
- Manifest artifact or inline manifest: current 336-file/238522-byte/aggregate
  snapshot above; worker output will contain all physical rows.
- Manifest hash: `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee`.
- Processing ledger artifact or inline ledger: planned exact 20-row sample
  calibration inside the metadata/sample ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE, ADAPTED, REJECTED, NO_NEW_VALUE.
- Reconciliation: manifest=336; ledger_terminal=0; exclusions=0; unresolved=336 before execution.
- Unresolved files: 336 semantic decisions before execution.
- Declared exclusions: no source file is excluded from metadata; 316 paths are
  intentionally outside T0A semantic sampling and remain visible for T0B.
- Unreadable or unsupported files: none observed at dispatch.
- Aggregation check: 336 files, 238522 bytes, ordinal aggregate matched.
- Drift check: worker must freshly recompute all fields before output authoring.
- Output traceability: physical path/hash for all rows; sample ID and owner/value
  reasoning for the exact 20 semantic rows.
- Adversarial verification: reviewer audits every sample low-value, reject, and
  defer result before permitting T0B packet authoring.
- Corpus verdict: PARTIAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | committed T0A GC-018/work order | may read source and write exactly two review outputs | metadata, hashes, declaration inventory, sample calibration, gates | local filesystem and read-only Git metadata only | ACTIVE_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | no downstream adapter ratified | no external ingress, CLI, MCP, execution, or dependency-resolution claim | explicit absence of adapter proof | fresh source-verified adapter roadmap required | DEFERRED_WITH_REASON |

## Legacy Absorption Coverage Index Disposition

N/A with reason: T0A processes the operator-authored post-SOT3
SOT-Application root. The Four-Surface folder is named only to preserve the
operator's two-gap chronology and remains covered by its separate accepted
FSCB ledger/crosswalk. No legacy corpus is absorbed, widened, or reclassified
by this packet.

## Provider Memory Authority Boundary

Provider-local memory, chat summaries, `CLAUDE.md`, and Codex memory may guide
navigation only. They are not accepted source authority. Every count, path,
hash, declaration, dependency fact, and semantic disposition used by T0A must
be re-verified from the governed packet or the literal read-only source root.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`External knowledge absorption`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "External knowledge absorption" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: ADIF-0016; ADIF-0020; ADIF-0021; ADIF-0027

| DefectId | Dispatch application |
|---|---|
| ADIF-0016 | reusable metadata/sample/declaration fields are explicit and T0B sequencing is durable |
| ADIF-0020 | applicable checker sources were read before writing and are disclosed below |
| ADIF-0021 | source-intake applicability uses the exact standalone marker and real section headings |
| ADIF-0027 | reverse architecture projection retains owner/GAP decisions without premature promotion |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_roadmap_closure_freshness.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Negative Search And Collision Discipline; Source Intake Decision Packet; External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; Reverse Architecture Projection Matrix; External Knowledge Intake Routing; Corpus Completeness And Report Integrity; PARTIAL; Dual Agent Surface Matrix; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm packet structure, source fidelity, dependency release, and partial-corpus claim boundaries before dispatch; gates provide evidence rather than first discovery |
| claimBoundary | checker conformance does not prove worker execution, semantic correctness, runtime behavior, or absorption completion |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id SOT3-APP-T0A --title "SOT3 Application Corpus Freeze And Semantic Calibration" --date 2026-07-16 --base e7f45e120 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SOT3-APP-T0 R1 scope-blocker review material commit 55007483c" --stdout --include-worker-return-skeleton` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact dependencies, operator source intent, current 336-file snapshot, 13-declaration baseline, fixed 20-path sample, two-output manifest, partial-corpus boundary, and T0B hold |
| checkerReadAheadConfirmation | dispatch, handoff, ADIF, source-intake, absorption, corpus, worker-return, and roadmap checker sources reviewed |
| docOnlyNewFields | metadata, sample calibration, declaration inventory, aggregate receipt, and source-intent fields listed above |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | SOT3-APP-T0A packet authoring, 2026-07-16 |
| Working directory | repository root |
| Command or tool surface | governed reads, filesystem enumeration/hashing, read-only Git metadata, apply_patch, governance gates |
| Target paths | this baseline, paired work order, and SOT3-APP roadmap |
| Allowed scope source | session next move at `e7f45e120` and operator instruction to create the T0A packet |
| Before status evidence | clean worktree at `e7f45e120` |
| After status evidence | exact three-path material dispatch packet; no external source mutation |
| Diff evidence | `git diff --name-status e7f45e120..HEAD` after material commit; staged diff before commit |
| Approval boundary | T0A dispatch authoring only |
| Claim boundary | no worker execution, T0A acceptance, T0B release, source/runtime/public mutation, or product claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-app-t0a-packet-authoring-2026-07-16` |
| Expected manifest | this baseline; paired work order; SOT3-APP roadmap |
| Actual changed set | same three paths required before material commit |
| Manifest delta | MATCH required before material commit |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private downstream source-intake dispatch; no public-sync authorization
or public-safe artifact set exists.

## Claim Boundary

This baseline authorizes only a no-commit T0A metadata/declaration/sample
calibration worker. It does not authorize semantic disposition of the remaining
316 paths, T0B, source mutation, hidden-clone mutation or synchronization,
dependency install, binding validation, runtime, build, typecheck, test, CI,
provider, browser, server, package activation, CVF Core promotion,
Catalog/GAP/ADIF mutation, public-sync, production readiness, or user-value
claims.
