# CVF SOT3-APP-T0A Corpus Metadata And Sample Ledger

Memory class: FULL_RECORD

Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS

docType: review

Date: 2026-07-16

Batch ID: `SOT3-APP-T0A`

Source intake decision packet: REQUIRED

Self-declared worker-return artifact: yes

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md`

dispatchWorkOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md`

executionBaseHead: `120c0f90a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md`

dispatchWorkOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md`

## Purpose

Freeze objective metadata for all 336 physical files of the SOT-Application
source root, enumerate every hidden-clone declaration occurrence with
candidate-only routing, and calibrate semantic disposition on the exact
20-file reviewer-selected sample. Preserve a machine-reconcilable boundary
that 316 file-level semantic decisions and all terminal declaration decisions
remain open for T0B.

## Scope / Methodology

Source root, read-only:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Enumeration used direct recursive filesystem walk with hidden files included,
producing a UTF-8 relative path (forward-slash normalized), byte length, and
lowercase SHA-256 for each of the 336 physical files. Aggregate input rows
were sorted by ordinal code-point comparison over the normalized relative
path (not case-insensitive, not locale-aware) and encoded exactly as
`relativePath<TAB>bytes<TAB>sha256<LF>` in UTF-8 without BOM, then SHA-256
hashed to produce the aggregate receipt.

Hidden-clone declaration search used an exact fixed-string, hidden-inclusive
search for `.Controlled-Vibe-Framework-CVF` across the full source root,
retaining every physical occurrence line separately.

The 20 fixed reviewer-selected sample files (SAM-01 through SAM-20) were each
read in full and assigned one processing status, disposition, value class,
overlap class, owner route, reason, and adversarial challenge. No semantic
rubric was propagated to the remaining 316 files.

## Findings / Position

All committed dispatch anchors reproduced exactly from the current physical
source. Reviewer recomputation then found a declaration-detail defect outside
those fixed anchors: three declared extension targets do not exist in the
literal hidden clone at `a78b35c`.

| Evidence item | Dispatch expectation | Recomputed value | Result |
|---|---|---|---|
| physical file count | 336 | 336 | MATCH |
| total bytes | 238522 | 238522 | MATCH |
| aggregate SHA-256 | `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee` | `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee` | MATCH |
| hidden-clone declaration occurrences | 13 | 13 | MATCH |
| all 20 sample hashes | fixed table below | recomputed identical | MATCH (20/20) |
| hidden target HEAD | `a78b35c` | `a78b35c` | MATCH |
| hidden target remote | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | MATCH |
| hidden target working tree | clean | clean | MATCH |

No dispatch-anchor stop condition was triggered. Execution proceeded to
metadata freeze, declaration inventory, and sample calibration. Reviewer
closure corrected DEC-05, DEC-06, and DEC-08 and narrowed runtime wording as
recorded below.

## Risk / Corrective Action

Reviewer corrective action was required and completed inside reviewer-owned
closure paths: three false `targetExists=true` values were changed to `false`,
their drift candidates were made explicit, and SAM-07, SAM-12, and SAM-15 were
narrowed to the evidence actually proved by static source. Residual risk is
the 316 un-sampled semantic file decisions and all 13 declarations' terminal
provenance dispositions, both explicitly deferred to T0B per the committed
work order.

## Source Intake Decision Packet

| Field | Value |
|---|---|
| Decision packet standard | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` |
| Input root or repository | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application` |
| Bounded scope | 336 metadata rows, complete 13-row hidden-clone declaration inventory, exact SAM-01 through SAM-20 semantic calibration |
| Enumeration authority | direct recursive hidden-inclusive filesystem enumeration, per-file byte/SHA-256 reads, ordinal normalized-path aggregate, exact fixed-string declaration search |
| Owner-surface taxonomy | CONFIRMED_EXISTING, ENRICH_EXISTING, NEW_FINDING, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, OWNER_SURFACE_NOT_FOUND |
| Pre-scan packet source | accepted scope review `55007483c`, SOT3-APP roadmap, paired T0A GC-018, and this work order |
| Overlap routing matrix | see Overlap And Novelty Classification below; every sample row maps to a current CVF owner, pending downstream owner, or OWNER_SURFACE_NOT_FOUND with a concrete next governed action |
| Negative-search evidence | negative-search command `rg -n "SOT3-APP-T0A\|SOT3_APP_T0A" docs CVF_SESSION` returned only predecessor/dispatch references; both exact output paths were absent (`Test-Path`-equivalent `ls` check) before creation |
| Core disposition | ADAPT objective full-corpus metadata and sample-calibration evidence only |
| Value conversion requirement | every sample row below receives one valueClass and one nextGovernedAction |
| Overlap classification requirement | every sample row below receives overlapClass plus ownerRoute and a concrete next governed action; no owner promotion in T0A |
| Worker output path | `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md` and `docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md` |
| Forbidden scope | semantic propagation to 316 un-sampled files, terminal declaration disposition, T0B release, mutation, runtime, live, or public action |
| Claim boundary | partial intake calibration only; no full absorption or product-readiness claim |

## Aggregate Receipt

| Field | Value |
|---|---|
| fileCount | 336 |
| totalBytes | 238522 |
| aggregateSha256 | `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee` |
| snapshotTime | 2026-07-16 worker execution start |
| executionBaseHead | `120c0f90a` |
| enumerationMethod | recursive hidden-inclusive filesystem walk; ordinal code-point sort on forward-slash normalized relative path; `relativePath<TAB>bytes<TAB>sha256<LF>` UTF-8 no-BOM encoding; SHA-256 over concatenated rows |

## 336-Row Corpus Metadata Table

Every row uses `metadataState=METADATA_FROZEN`, which records objective
path/byte/hash evidence only and is not a semantic terminal decision. Rows
are ordered by ordinal code-point sort of the normalized relative path,
matching the aggregate-receipt sort order.

| sourceId | relativePath | bytes | sha256 | metadataState |
|---|---|---:|---|---|
| SRC-001 | .cvf/bindings/cvf-entry.binding.json | 249 | d5acbb3c36e54eb2531361208c34e7edeaa800e17a381491c1efde64c4b98780 | METADATA_FROZEN |
| SRC-002 | .cvf/bindings/evidence.binding.json | 230 | 1dbda50c32f80733deda4fba704856981cef1c9e5d5064fab098a8d8fc8d9afe | METADATA_FROZEN |
| SRC-003 | .cvf/bindings/guard-contract.binding.json | 189 | d1af88b5e43f517823bae09f7a434bfc47e5a8fc8dbdbb3ad001073e82009e47 | METADATA_FROZEN |
| SRC-004 | .cvf/bindings/phase-governance.binding.json | 311 | 5355522088504d1d77bcedcc130e8ee038be4a8c9d0eb5b86db334fe42fa4089 | METADATA_FROZEN |
| SRC-005 | .cvf/bindings/refinery.binding.json | 298 | 08b9eb7f7c61e1d299c9eaefc505a715402ed6b24f0504757d09690d06db8603 | METADATA_FROZEN |
| SRC-006 | .cvf/bindings/truth-flow.binding.json | 289 | 238b416f4eeb85c656b06e85545dd737a96dd57d74095c06ce5a9e4c51505b79 | METADATA_FROZEN |
| SRC-007 | .cvf/bindings/truth-kernel.binding.json | 287 | a696ddbef39870bd8b6c633c6354c61da039b2bef94d992e0bd65505ccc39666 | METADATA_FROZEN |
| SRC-008 | .cvf/manifest.json | 567 | 21d1ab9073f154f15d30784b4044437b650c9b645f76f1a2f4aa9fdf0e2958dc | METADATA_FROZEN |
| SRC-009 | .cvf/phases/build.phase.json | 197 | a5bb79c177cf481d3b820af72bf557419603434231cf9e2ebdd982f6a3582f72 | METADATA_FROZEN |
| SRC-010 | .cvf/phases/design.phase.json | 241 | 3d98e1151c9d91a056d3e1bbff111fd10e4f66d1d40ce7885db17e9a13680326 | METADATA_FROZEN |
| SRC-011 | .cvf/phases/freeze.phase.json | 232 | 46b700b0c777084d82b446ce0a6020ddcc81ebbb0f9d83e8bc1bf0e2e66ad90d | METADATA_FROZEN |
| SRC-012 | .cvf/phases/intake.phase.json | 236 | ffad258a4a177729277029e90caf864604de86a696280d9740808da481ada3a9 | METADATA_FROZEN |
| SRC-013 | .cvf/phases/review.phase.json | 216 | 67a13bb23edb2c31a2efce53582071c5eea3576e431b98cdc5dda3ba941629b7 | METADATA_FROZEN |
| SRC-014 | .cvf/phases/spec.phase.json | 230 | 8bdf2175f56a4980fd32c76afc29ebd8df917e6f6d1f805170150f776b9f018f | METADATA_FROZEN |
| SRC-015 | .cvf/phases/work-order.phase.json | 240 | 54a4aba6edfe487eb4090eaa2f372409410cdf494e1cb3b2b4012bc3d5bc7036 | METADATA_FROZEN |
| SRC-016 | .cvf/policy.json | 757 | c1ab621fc57371dbcca2d357ba6bc87a3d5ae2e4dc13059086e02e03a4c8ae6e | METADATA_FROZEN |
| SRC-017 | .cvf/rule-pack.lock.json | 250 | 1a32df73ea9f97855e8f415c1bab2258a1048b8d15beb40b543831e34a12bdab | METADATA_FROZEN |
| SRC-018 | .env.example | 321 | 3a369c5ed83c1618740f371cfb9772776b86451d643e89b40b07006757059667 | METADATA_FROZEN |
| SRC-019 | .gitignore | 79 | 172bf4ce3fc6b8b0e88c6b4b8f92d602f90ee3228c45a15d0d24c08d2163866f | METADATA_FROZEN |
| SRC-020 | AGENTS.md | 1425 | 082fd81ec58cdef8088bf3170a1ea7977f508dd155890e4b2d84518bc5b480f5 | METADATA_FROZEN |
| SRC-021 | README.md | 17279 | 5d01f41b7e9de5c7f86a42a1f36d533bcd7bf0aba7c7f2bedc8ec69a6f95be8b | METADATA_FROZEN |
| SRC-022 | TREEVIEW.md | 21342 | 208f4b0708f20f9115450cac7035cc2e47ff85010a313808fd5a370801265bce | METADATA_FROZEN |
| SRC-023 | apps/api/package.json | 568 | bbec25909e85daa6309bae2c3fb628ed6fc300a576f4b8eb6731de59ff0af732 | METADATA_FROZEN |
| SRC-024 | apps/api/src/app.ts | 1919 | 41111c32971bf50d12dcc77c142b4ed806efd527c61b7531e5a612b3d137dd1c | METADATA_FROZEN |
| SRC-025 | apps/api/src/config.ts | 717 | 22ae2e2f83c600bfdcf9fffd8ad948e68bc75ccb01d717ab3013247d9dc12fba | METADATA_FROZEN |
| SRC-026 | apps/api/src/controllers/conflict.controller.ts | 879 | 72939dc6705df1e265bc820381aa0534d70d74d0dacbfcf316eba0bd757e599f | METADATA_FROZEN |
| SRC-027 | apps/api/src/controllers/context.controller.ts | 870 | 9df5065fe327a9adf31fbe9bcea4be5a36c9373c1b407935bb93ac156914a05f | METADATA_FROZEN |
| SRC-028 | apps/api/src/controllers/freeze.controller.ts | 869 | 20ccb0aaf804b01cba5c90a8715f8fa35fa0468768b96dd6f5951783ff000ffc | METADATA_FROZEN |
| SRC-029 | apps/api/src/controllers/impact.controller.ts | 869 | 81158cfc8efc01d6e8f968b290c1b890597aaca2e9e76917d4737d54a549b868 | METADATA_FROZEN |
| SRC-030 | apps/api/src/controllers/output.controller.ts | 869 | 9e6bd40ad5170abcc75676449d9ea75d08ce21bdc87f90c36f46f70e4fe6a1d8 | METADATA_FROZEN |
| SRC-031 | apps/api/src/controllers/recall.controller.ts | 1254 | 7d6c8f2f21d20af4acbdb0bc10c2ed77026c501819bf2230d543bc910090bc36 | METADATA_FROZEN |
| SRC-032 | apps/api/src/controllers/refinery.controller.ts | 875 | 72472b3dd033fe452a848e8d9727b478204c0e67ba47c296e94c65fabc114c6a | METADATA_FROZEN |
| SRC-033 | apps/api/src/controllers/review.controller.ts | 871 | fa01307e7541d72e2d719ba1c14caf8812a1c54bf01a44b741b09cc549802d96 | METADATA_FROZEN |
| SRC-034 | apps/api/src/controllers/sot-record.controller.ts | 1269 | 6c0155025fe963e144d431a72091c5db5ee99f67375eb26301608f56d849ad43 | METADATA_FROZEN |
| SRC-035 | apps/api/src/controllers/source.controller.ts | 871 | d3bf03d68f32aeda55c8489cc6590485df3090e8e07adf2dab14a37657451d63 | METADATA_FROZEN |
| SRC-036 | apps/api/src/middleware/cvf-governance.middleware.ts | 541 | 830c354ca3e2d1cf09ca6ac38b1cbbd071562067919f300bc01db5a6f1baf1b8 | METADATA_FROZEN |
| SRC-037 | apps/api/src/middleware/error.middleware.ts | 491 | 5bed8f166cd40f1bbe7ec50e9b287e6f9b055e87b9926f34dddedb3c421aa78e | METADATA_FROZEN |
| SRC-038 | apps/api/src/middleware/identity.middleware.ts | 525 | 704ba03505f609ebfa5ac15a5509e1a7f9982ec6c32f4f7fc27136475ce51755 | METADATA_FROZEN |
| SRC-039 | apps/api/src/middleware/request-context.middleware.ts | 538 | 19f5c10966d8b6631f84cf667aa9c6a2c7b2d475d8bafdb938c36454a13e5ecb | METADATA_FROZEN |
| SRC-040 | apps/api/src/routes/audit.routes.ts | 276 | 36117b83b13b02be0b04cdce395e69ca041c634d9eac36fb8854e77fffc4d0d5 | METADATA_FROZEN |
| SRC-041 | apps/api/src/routes/conflicts.routes.ts | 446 | 3dfe3a292fd4ade66b7fbb6166106c9f6b38001c535dc9bcd70d4692b4346021 | METADATA_FROZEN |
| SRC-042 | apps/api/src/routes/contexts.routes.ts | 427 | 008d9ea19b9300fc7679e55fed4a5760e14e2f916474aae93d4633bd6f9d8199 | METADATA_FROZEN |
| SRC-043 | apps/api/src/routes/freezes.routes.ts | 420 | 2ed74008598f36b4c1e9f87ea51b99fd39e72c9b38c8764053b79be48fd1ed05 | METADATA_FROZEN |
| SRC-044 | apps/api/src/routes/health.routes.ts | 198 | 0628348a1338648fa3c8e61ef488049f33edcaef119bce0ed1613f5979792246 | METADATA_FROZEN |
| SRC-045 | apps/api/src/routes/impacts.routes.ts | 420 | 6a65b89669dae09fdc1fee6d3aaa31a0674ea4b93707df96d11e89318b99f623 | METADATA_FROZEN |
| SRC-046 | apps/api/src/routes/outputs.routes.ts | 420 | ed3a70749100be7c290b21200ae18ea300d288ceb37a272935bbf83eca38be2e | METADATA_FROZEN |
| SRC-047 | apps/api/src/routes/recalls.routes.ts | 502 | d3bf26ef96aeac11060875c979993d875131bb265cf4414401fb542d5ff04ffa | METADATA_FROZEN |
| SRC-048 | apps/api/src/routes/refinery.routes.ts | 434 | b4f9f880bc1d7292bcffbd73350ba3f65fa24ac57f6fe918010ab6748148995a | METADATA_FROZEN |
| SRC-049 | apps/api/src/routes/reviews.routes.ts | 417 | 8a4c112b82d1dbce5b6a303d236061db13d5f89710fc6d6ef460f907a0cf1ac5 | METADATA_FROZEN |
| SRC-050 | apps/api/src/routes/sot-records.routes.ts | 540 | d0b2b3df47ac8a30e91670a55c0b2aeb69626e1ab60246aa22217614fdd1b92d | METADATA_FROZEN |
| SRC-051 | apps/api/src/routes/sources.routes.ts | 417 | b89c8dd3c919925629740da091057e81cda6a0a791571e92918fb350d1f151b5 | METADATA_FROZEN |
| SRC-052 | apps/api/src/server.ts | 271 | 619cbf410e3908de0eea478b9a5aa35d46dcb9e77c85f4235adb5ecd0b206891 | METADATA_FROZEN |
| SRC-053 | apps/api/tsconfig.json | 153 | 9bed61ee71eef1e5523a79b9a25b364ae18590d9e5e6eef052d2eb06b0036b6e | METADATA_FROZEN |
| SRC-054 | apps/web/index.html | 302 | dbc1af9ef8c71d2d57e0095d855f091ed69fa5db32b2afd7a1a0a238c12a0738 | METADATA_FROZEN |
| SRC-055 | apps/web/package.json | 572 | 93a2a5d4b8a671dbfe11989c3e70a503aadc8cf6180c83eefa4054ee3a430650 | METADATA_FROZEN |
| SRC-056 | apps/web/src/api/client.ts | 534 | eaff41a93ef6c06ae9791af90a7055c4c2e0b29c7cd1d402b68cbacb594282cf | METADATA_FROZEN |
| SRC-057 | apps/web/src/api/conflicts.api.ts | 330 | 897a2aaed6816b538046f24ffd9350e2b54540ec9388c7c526995cb97a44a3cd | METADATA_FROZEN |
| SRC-058 | apps/web/src/api/contexts.api.ts | 312 | 866e8acf7917b76d6c1e1bbb8dc8b2b1b5d64f6a6c1f37c048c1f79ea534e149 | METADATA_FROZEN |
| SRC-059 | apps/web/src/api/impacts.api.ts | 307 | 1c5aece967ab92d8ccfe3de7ea41d9ec96fe8befca18e7e7d8023d45866715a2 | METADATA_FROZEN |
| SRC-060 | apps/web/src/api/outputs.api.ts | 309 | f42cb7cf8b2f53abc01899410d98dc67a78c11097819045247ae887f9f15e2d5 | METADATA_FROZEN |
| SRC-061 | apps/web/src/api/recalls.api.ts | 273 | 4a4199bbee2d527b0c91c04fc8276e3235aa3d61ba9c1903c8fec62e34a103f3 | METADATA_FROZEN |
| SRC-062 | apps/web/src/api/reviews.api.ts | 275 | ab1bbac5e406b4614979eb0a3ac9f7a5843606faa4d092ee9064dbefbec01ae0 | METADATA_FROZEN |
| SRC-063 | apps/web/src/api/sot-records.api.ts | 244 | 04eff3b3e8b00b6ec6af86678b0a8b0cf417fac4c5ee298fe963985cf042fe64 | METADATA_FROZEN |
| SRC-064 | apps/web/src/api/sources.api.ts | 275 | c32f4be65818b9656ba4c36977e0aae997f21d9a5fc1b3a167b1deec00892ce8 | METADATA_FROZEN |
| SRC-065 | apps/web/src/app.tsx | 108 | 4ab7cb3cd2f5fce968a13da2ee1c22ef57de1f0f5463c3b755d70caa4dcac3ed | METADATA_FROZEN |
| SRC-066 | apps/web/src/components/conflicts/conflict-candidate-table.tsx | 260 | b177651ebecddeff28618419505d8e1d5cf3daf5ac01e02b56fb52f57f30272a | METADATA_FROZEN |
| SRC-067 | apps/web/src/components/conflicts/conflict-resolution-form.tsx | 196 | 17f86bb50c37308f584e8b5e80ea0041547c075c59338dfc121a83d0d7cc7b28 | METADATA_FROZEN |
| SRC-068 | apps/web/src/components/conflicts/conflict-set-card.tsx | 202 | 4dec4261a10099cd2bd3996f643b85894bfac700ca3b05d3eaac6963d7c94661 | METADATA_FROZEN |
| SRC-069 | apps/web/src/components/context/context-package-preview.tsx | 166 | 09f717d2703c5ce22bfec052f054b13e0e6f0837a1c6b280c9efa2d4b708f9bc | METADATA_FROZEN |
| SRC-070 | apps/web/src/components/context/information-dose-panel.tsx | 207 | 5e8aa304f87ba79ba8eb72bb8da2868bc6d0bb289eb85cd5b7272050e5f65300 | METADATA_FROZEN |
| SRC-071 | apps/web/src/components/context/recipient-policy-panel.tsx | 178 | f5d41ac83801a1ab19ed39e5b49d4a8212307ded9fbd37500cf99c37ddd46b17 | METADATA_FROZEN |
| SRC-072 | apps/web/src/components/governance/approval-panel.tsx | 184 | 1598ebc406f7db97d2e3b59a0e4888dd1e01c44b610b65388e3c97e422b1f0c3 | METADATA_FROZEN |
| SRC-073 | apps/web/src/components/governance/cvf-decision-banner.tsx | 276 | 2bb91f13cb42ea2e5afd8366efaa426f9b86d8e140b9c0d7685729dea4732255 | METADATA_FROZEN |
| SRC-074 | apps/web/src/components/governance/evidence-receipt-card.tsx | 190 | 51a264a6ac3a810374ba24b591a69ee0878533e818af5556dfeae7a397e32724 | METADATA_FROZEN |
| SRC-075 | apps/web/src/components/governance/phase-status.tsx | 143 | 86699e4cb0264fce26939e23a03fc906be2b78f0d334251a728f375c61f3194c | METADATA_FROZEN |
| SRC-076 | apps/web/src/components/impact/affected-output-list.tsx | 144 | a771cbfc46a7c10bd914bf51be4ddf67552a43a68d68d2de219e6edb0ffa964a | METADATA_FROZEN |
| SRC-077 | apps/web/src/components/impact/impact-graph.tsx | 172 | 5d1f3c65bd96493a49e4e7b0fda95c83dfb3ba75b629613155cea327fa78b057 | METADATA_FROZEN |
| SRC-078 | apps/web/src/components/impact/recall-status-card.tsx | 178 | 1302c5cc6691647a8152642af906c79e527414019560c6c23495d97c17f4e088 | METADATA_FROZEN |
| SRC-079 | apps/web/src/components/outputs/freeze-summary.tsx | 231 | d77353ea0ec180fdc487766d67c8a61c049874d9ff7edc59a2593974cd827bd2 | METADATA_FROZEN |
| SRC-080 | apps/web/src/components/outputs/governed-output-editor.tsx | 254 | 8f5a7120da808ebe99926e9157d63635f16bdc8920adaae8be978d8ec91320c3 | METADATA_FROZEN |
| SRC-081 | apps/web/src/components/outputs/output-source-map.tsx | 244 | 1d581ce53178a9c28a59d23710da28a3129511babbefd1019c8db2f1e64ddf8c | METADATA_FROZEN |
| SRC-082 | apps/web/src/components/outputs/review-findings.tsx | 196 | ab9f1dd7a5a36e4421ea4fe36ef294c7bda4b701cd3f8e031bdde8dab6a57539 | METADATA_FROZEN |
| SRC-083 | apps/web/src/components/sot/authority-badge.tsx | 135 | 999d4cda14fe0c57e618e062e4a4c755f6a4e58685c6e0a1ca667f91c9aafb30 | METADATA_FROZEN |
| SRC-084 | apps/web/src/components/sot/scope-badge.tsx | 119 | e3324765d111864358c1a4c5b5621b53c9d7239911efaaaab9c9e6be43a5b0a1 | METADATA_FROZEN |
| SRC-085 | apps/web/src/components/sot/sot-record-detail.tsx | 158 | 697801be343d518989c0fe8e76cd64f946d2bc66fd3d9c212155811edd708bbb | METADATA_FROZEN |
| SRC-086 | apps/web/src/components/sot/sot-record-table.tsx | 371 | bfe92f748dd0559b0439ceea517e17da20679bb46a5005050a4185e9731eef16 | METADATA_FROZEN |
| SRC-087 | apps/web/src/components/sot/validity-timeline.tsx | 236 | 091c727039ae2b6bf10c92f71c63b007a717aa25ec5559231d45055e86100ca4 | METADATA_FROZEN |
| SRC-088 | apps/web/src/components/source/source-envelope-card.tsx | 204 | 2ba3b0034cc946cefcee3571123b06e6b2978c1f6b03464b2e5a5e42a2aa90b8 | METADATA_FROZEN |
| SRC-089 | apps/web/src/components/source/source-intake-form.tsx | 675 | f5468226ca23187dd8892ed804c3e117538cd7a45998282053f776db106192ba | METADATA_FROZEN |
| SRC-090 | apps/web/src/components/source/source-quality-findings.tsx | 228 | 0d59494bbf5df5c46620550ac9ada22bcf667add03f1d87ec1457e41365c919f | METADATA_FROZEN |
| SRC-091 | apps/web/src/layouts/application-layout.tsx | 939 | f64722c15fd5283265ca9e13da36c1074b6e30bb19e7bebdb94e0264fd55c2ac | METADATA_FROZEN |
| SRC-092 | apps/web/src/layouts/governed-workspace-layout.tsx | 531 | 3b1e5beed7633f0196654851ea4d178b57883302ae31d486a381ec8607f8a539 | METADATA_FROZEN |
| SRC-093 | apps/web/src/main.tsx | 419 | 930958841847c9af133049feac0508bdf730958c5b37c4b823302ebedc22aee8 | METADATA_FROZEN |
| SRC-094 | apps/web/src/pages/agent-workspace.page.tsx | 421 | 31ce34bf18415e512fcd49566c2a2aa83be89a06e810ee3cd32fcc80a20cbdc4 | METADATA_FROZEN |
| SRC-095 | apps/web/src/pages/audit-trail.page.tsx | 373 | 61ba2697f2e54ce946524ab6b62da89c555c65ada9fb4f6da07463f160a95a5c | METADATA_FROZEN |
| SRC-096 | apps/web/src/pages/conflicts.page.tsx | 389 | 53c28798e2228b9148e9585766b518ea2a1bca76b74dd2b695ce5241727aef01 | METADATA_FROZEN |
| SRC-097 | apps/web/src/pages/context-builder.page.tsx | 403 | eb1314bd22e0478238ca40d998c77eed79622c5f1a4e5241e3961255518ddb14 | METADATA_FROZEN |
| SRC-098 | apps/web/src/pages/dashboard.page.tsx | 414 | b8c7c1eb481414b678dc369f6e53d8f2a564dde370f4e315611c229de24b4473 | METADATA_FROZEN |
| SRC-099 | apps/web/src/pages/environment-sot.page.tsx | 405 | 2942beac2387d365d27287365e40354d5361e9b21b802238e987b66f1418b55e | METADATA_FROZEN |
| SRC-100 | apps/web/src/pages/impact-analysis.page.tsx | 431 | 0fe4c1af95ed7d74dd627554b6dc9055f26db4714dc7cb7aa25bf7f368c832e6 | METADATA_FROZEN |
| SRC-101 | apps/web/src/pages/internal-sot.page.tsx | 372 | d476317eedd4c83576a7767bdf6d1c7c89dd2626b705c34fe8734e4b8d0b0395 | METADATA_FROZEN |
| SRC-102 | apps/web/src/pages/output-review.page.tsx | 407 | 931650f8d67be81a707ea1aa213516a753cac2edfa71816a16b90ffeb66ab6bd | METADATA_FROZEN |
| SRC-103 | apps/web/src/pages/project-sot.page.tsx | 398 | f3b0dc7a1e8c0068006f23aca3cd92117022bceaa4ae1d22e9a18fcfb14f80e0 | METADATA_FROZEN |
| SRC-104 | apps/web/src/pages/recall-cases.page.tsx | 390 | f4ca2851002d292608f0f7a1b26d53549087193b5e5ac97e1aa00eef47d6b569 | METADATA_FROZEN |
| SRC-105 | apps/web/src/pages/refinery-review.page.tsx | 424 | d62a369abc3783702d64acfdbb53198cae841f46e80325e781cda3d19bcc0ded | METADATA_FROZEN |
| SRC-106 | apps/web/src/pages/source-intake.page.tsx | 422 | 93715fd19e4f40bb7fdc5336d01507f6ed4cd3933f7c003615095f4aef61b823 | METADATA_FROZEN |
| SRC-107 | apps/web/src/router.tsx | 2063 | 2fddec033fc92478bc04b77cd5c272a6a9e51a619a4d432a9b8c01ef7880c3e3 | METADATA_FROZEN |
| SRC-108 | apps/web/src/state/governance.store.ts | 428 | e492043a0fba997ecda7bebad816641a402bee63817d9a0956a73e514587dd0d | METADATA_FROZEN |
| SRC-109 | apps/web/src/state/session.store.ts | 370 | 5bfa7788569f13e99ecc25f43d70ca5a8df4b05c6972db783dd83328a88440db | METADATA_FROZEN |
| SRC-110 | apps/web/src/state/workspace.store.ts | 346 | 918d40ca9c0cbc5c5aa406cdcd083e31e7cdbf74806bb1604eef4f6dbf86296c | METADATA_FROZEN |
| SRC-111 | apps/web/src/styles/global.css | 1402 | eedfe71f2cac60240d821218831034296b7c09ed5a2ada4905dc9eb04d09ca2f | METADATA_FROZEN |
| SRC-112 | apps/web/tsconfig.json | 265 | 96ec74e0aae2560c2bca868000a5b76a1788beda122410bed7cd64f8d2e77f75 | METADATA_FROZEN |
| SRC-113 | apps/web/vite.config.ts | 181 | d82ba8a99b7dd21dd4db553209569047ec2024f26e61f8ec1fca42c99250cc0d | METADATA_FROZEN |
| SRC-114 | config/authority/authority-domains.yaml | 570 | e468fdf974464726a14063b7e1cff9755c1661e8801bf632b29bb9604076e024 | METADATA_FROZEN |
| SRC-115 | config/authority/environment-authority.yaml | 266 | efcd40e6664edc74ddf76f7bded393405147d355a4e698d6a03e3a05d4dc98c8 | METADATA_FROZEN |
| SRC-116 | config/authority/internal-authority.yaml | 390 | 426d7fc28d0bb7b1a2dc6af29f95d058f00f09b55b3df9106ab692327e9d40c5 | METADATA_FROZEN |
| SRC-117 | config/authority/project-authority.yaml | 342 | 2f69c04ab44245324ad0c8906876753783846705ba63fbc39fae8b489de638ce | METADATA_FROZEN |
| SRC-118 | config/information-dose/agent-task.yaml | 235 | d35d8824495a03aea134817f5064dc5cc092851afe72df1fcc5c3c4984b8e788 | METADATA_FROZEN |
| SRC-119 | config/information-dose/engineering-full.yaml | 200 | c0956a74e1d3ed9fac4b6814d7117bf8802bc6a8d80996be6a591fb7d413b23b | METADATA_FROZEN |
| SRC-120 | config/information-dose/executive-summary.yaml | 222 | ca878fe6b26a5e9cbe8b6565cfd663bc19b27974bb9d6df5f77f36b996efb841 | METADATA_FROZEN |
| SRC-121 | config/information-dose/operator-action.yaml | 232 | 84e84ee5268d9207faa9240db8b495f865bad1ca0b6aeb5e5e9861ab23f6a6d2 | METADATA_FROZEN |
| SRC-122 | config/lifecycle/expiry-policy.yaml | 190 | 8f44f60c31e59a832a462d6322a3affd3949a7c14e69167637fd15ddc5a12ac2 | METADATA_FROZEN |
| SRC-123 | config/lifecycle/recall-policy.yaml | 347 | fa3c8a3fdb0fde10137197972bbd73b431176cc0ca00d5c0ecdda738b857cd84 | METADATA_FROZEN |
| SRC-124 | config/lifecycle/retention-policy.yaml | 248 | 151dfbd9691c60a2fc6d6b0628280be065e3e12564752173e4419214d56a99ee | METADATA_FROZEN |
| SRC-125 | config/lifecycle/supersession-policy.yaml | 229 | 5c0da442d16b0224e4f6d08f3a5da1e8d8203037f3256d6a2abea74ea97eceab | METADATA_FROZEN |
| SRC-126 | config/review/commercial-review.yaml | 312 | caa438dc52d12ec664b1d5916cade26116b6a4d8b6e02f7ae5d1c83d260ad11c | METADATA_FROZEN |
| SRC-127 | config/review/freeze-policy.yaml | 294 | a7b7da948be5b4d3cdfcca9b56addd44083ee043724e947e00777887fc77a170 | METADATA_FROZEN |
| SRC-128 | config/review/legal-review.yaml | 280 | c98657c3ed2bfd6b7c98c9509a633cbf1eb7a8ae6feae13c5c88ed0e424dc87c | METADATA_FROZEN |
| SRC-129 | config/review/technical-review.yaml | 266 | 96968ec8c8459db8ba92cfea6426431bb0a185a0f17353d85a60e694be2a7713 | METADATA_FROZEN |
| SRC-130 | config/routing/context-eligibility.yaml | 281 | 40d7fc94820273fc39a06e00e906496ceef3389459dbdc558dd847bd712760ed | METADATA_FROZEN |
| SRC-131 | config/routing/recipient-policies.yaml | 436 | c67c7f14b3666158a7dc1c83328cfde73f5d057e9c913d8cc9cdcffbee3db097 | METADATA_FROZEN |
| SRC-132 | config/routing/sequence-policies.yaml | 437 | f3658eda65d428c8f0dedb8673c0eab3e24751e15c8fcbc179a844674498c517 | METADATA_FROZEN |
| SRC-133 | docs/AGENT_EXECUTION_BOUNDARY.md | 791 | f00fa6a363f66451d901d594ac9764f2e6377bc3d7e441d6bf4312d1bd99460d | METADATA_FROZEN |
| SRC-134 | docs/ARCHITECTURE.md | 1464 | 1cff0111b87b1849b2deae8023c62ba54fec6b71f7204eea63d930c0d76cedf9 | METADATA_FROZEN |
| SRC-135 | docs/AUTHORITY_MODEL.md | 885 | 16de904b65a57b332a4dbcff4b1c5a36f140aa400315d43df8a86343dfe4747a | METADATA_FROZEN |
| SRC-136 | docs/CLAIM_BOUNDARY.md | 1042 | fb2b3b5faf6a2e3c313aac3d63623e21b31003a122b956cbcad9b22e11143886 | METADATA_FROZEN |
| SRC-137 | docs/CONTEXT_DISTRIBUTION.md | 676 | de3c17e14ea8e522d1ab2fc44f670c91d30147a89e7b54d95a547c960f916d52 | METADATA_FROZEN |
| SRC-138 | docs/DOMAIN_MODEL.md | 1294 | 0a40e1cf3048e2abdb8fb8f6fc524e3d2ab420b05443de2abc95a7c403a1c626 | METADATA_FROZEN |
| SRC-139 | docs/FAILURE_TOKENS.md | 909 | eba317d93a190fa4e4883889db56beea8705f292f1d8afd8edaf661f8a9a98fa | METADATA_FROZEN |
| SRC-140 | docs/IMPACT_RECALL_PROTOCOL.md | 701 | 1930f69aed46baaf7ba974c2a2cbc511d171ac5fdbbf2244fecb1e4994169eb6 | METADATA_FROZEN |
| SRC-141 | docs/INFORMATION_LIFECYCLE.md | 836 | 38c4e30b2d6d018ef9b5ae3737505e7372ba46c245d876bc015f65648c86bace | METADATA_FROZEN |
| SRC-142 | docs/LOCAL_FIRST_OPERATIONS.md | 668 | fdf8b45714965601f5f02e9b3119c6460702039aec97688a154af8532bbee34c | METADATA_FROZEN |
| SRC-143 | docs/PRODUCT_DOCTRINE.md | 1469 | bbd12fa92143c1100ab29f9f33c20c12aa989ece851031cca1fd6255975c5c77 | METADATA_FROZEN |
| SRC-144 | docs/REVIEW_FREEZE_PROTOCOL.md | 844 | 60da0585588db647aa7249af8516cdeae1848c6c952a2a3582265e5d6154623e | METADATA_FROZEN |
| SRC-145 | docs/SECURITY_AND_PRIVACY.md | 884 | f588f106e6e073502a6994b4d537a396f797dd2fc762b3ab862d725473128cab | METADATA_FROZEN |
| SRC-146 | docs/SOT_SCOPE_MODEL.md | 720 | 7813d57a6880f3f733e14ce7854d73be3e5a9fafeea70787535a420b216be106 | METADATA_FROZEN |
| SRC-147 | docs/phases/PHASE_1_FOUNDATION_AND_CONTRACTS.md | 758 | 2b8355a977f930807b913307616d6ca0e5a1192c9592ffd6a21f8b1d132d5ba6 | METADATA_FROZEN |
| SRC-148 | docs/phases/PHASE_2_MULTI_SOT_AND_AUTHORITY.md | 660 | 2bfa3d4a3231f88f28a6b6041b1322ae0da121c065067ea04bac5b48ebefa0da | METADATA_FROZEN |
| SRC-149 | docs/phases/PHASE_3_CVF_INTEGRATION.md | 577 | 080e801ab3440492ff167f998e0d4bfb07342c28f094e4b9389289f8ce40d4f6 | METADATA_FROZEN |
| SRC-150 | docs/phases/PHASE_4_GOVERNED_WORKSPACE_AND_OUTPUTS.md | 590 | f32cf0e9b9cc1f403256dde4d56e46a82f7e90cb723a505eed47cb5dfca4b085 | METADATA_FROZEN |
| SRC-151 | docs/phases/PHASE_5_IMPACT_RECALL_AND_HARDENING.md | 620 | 3151316a8a77ddec179494b12f41ee9efd219933c7eb33e4a9079bf6265cc75c | METADATA_FROZEN |
| SRC-152 | evidence/README.md | 600 | 2b5140808802dd98584d8c76fe9fa3090e280e015ccee812c9c5205d538ad249 | METADATA_FROZEN |
| SRC-153 | evidence/claim-boundary.md | 596 | 238b8bb876dd0692cfbab86690dc24281596ec746274b0478ca768683afdae07 | METADATA_FROZEN |
| SRC-154 | evidence/evidence-manifest.schema.json | 1209 | a7e41adfe7a793c3091f4a311593e734381c9c0aaea123590f5a9d35d2a13634 | METADATA_FROZEN |
| SRC-155 | evidence/samples/sample-context-trace.yaml | 376 | 6945f2f162b832ecbd1c14b1b1b152e101f582dcf1ad959703831b44a94f6f24 | METADATA_FROZEN |
| SRC-156 | evidence/samples/sample-freeze-package.yaml | 439 | f9cdece7d41a998b27cdde16de09d388fb9ece5791acd88d5d44477cbaa3f108 | METADATA_FROZEN |
| SRC-157 | evidence/samples/sample-output-trace.yaml | 429 | 9909f15934ac914272c8bcd7ac4fe21f4f05ef32d45a53fcf194893d87e6d698 | METADATA_FROZEN |
| SRC-158 | evidence/samples/sample-source-trace.yaml | 381 | 3a2382186279223cfd498397a1c33e462a6491cd1bf21756eef44da35c8bb0e1 | METADATA_FROZEN |
| SRC-159 | fixtures/controlled-quotation/customer-requirement.yaml | 303 | 4689ecf1fa76c77552beca244cf50b0df4f1710ae1593879e1912c543aef73e9 | METADATA_FROZEN |
| SRC-160 | fixtures/controlled-quotation/expected-context-package.yaml | 579 | bc310603abe88a60c9d7d557cc127a69ff3c54d79dc298af954d018c51496f18 | METADATA_FROZEN |
| SRC-161 | fixtures/controlled-quotation/expected-draft-output.md | 632 | 9e63ef2b9b736c1d4cf73566f560f62d1cfe74883ca2f34fcb481fe0e7a2b3a7 | METADATA_FROZEN |
| SRC-162 | fixtures/controlled-quotation/expected-freeze-record.yaml | 840 | 33a25d2d28ef7502fed8b6aaf64ef652d770f0ce59ea32de0d4ef5412f7f13f7 | METADATA_FROZEN |
| SRC-163 | fixtures/controlled-quotation/expected-impact-case.yaml | 352 | c71af73658a8f73f7adb8f614aaf151cdf9cd02a403d6e73deb7f02235986b37 | METADATA_FROZEN |
| SRC-164 | fixtures/controlled-quotation/expected-kernel-decision.yaml | 247 | 443c86650639e618167ea489d25894fb5548e53780808bd5a5e3b9c64ce01873 | METADATA_FROZEN |
| SRC-165 | fixtures/controlled-quotation/expected-refinery-findings.yaml | 450 | 3fdf5422427b4b5e6e60d3cb954b6c7ab52af8bb498ad5413e61cda3e72ed2d9 | METADATA_FROZEN |
| SRC-166 | fixtures/controlled-quotation/expected-review-record.yaml | 307 | eb42ce8e453088d30c3c16c1939f65150759d8c374f157465849ccee2695705c | METADATA_FROZEN |
| SRC-167 | fixtures/controlled-quotation/internal-price-source.yaml | 592 | cdb46d076c751c78cef3fdbed2c78087264da2b4905136f2fe9e39f0b3778346 | METADATA_FROZEN |
| SRC-168 | fixtures/controlled-quotation/market-reference-source.yaml | 635 | 2e38ce5aeee6d5fd7bd218e136b812ad797b44b47b04ea2f9e13e721d65ffc12 | METADATA_FROZEN |
| SRC-169 | fixtures/controlled-quotation/project-price-source.yaml | 617 | 0a04d768686640e7c9ce44415e5ff7510a2765c4a7876d7101284b0b6fd2b17b | METADATA_FROZEN |
| SRC-170 | package.json | 1015 | 981144baebb81aa64bc390f19714021a92288f08e182e516f0c0410dd03c0866 | METADATA_FROZEN |
| SRC-171 | packages/application/package.json | 255 | fa495c8b8a695b34d915c3cb454fc8d70b69edc2302c1f8ce69b852ccc8e18f1 | METADATA_FROZEN |
| SRC-172 | packages/application/src/commands/build-context-package.command.ts | 205 | e9ae491b84d1ac1b444d8373598465339e652ec62b47644034ffef9a121f49ab | METADATA_FROZEN |
| SRC-173 | packages/application/src/commands/freeze-output.command.ts | 197 | 9a8f1b57a34310a309a0daccd69df838e09abacded894e7fa1504a308a6509f0 | METADATA_FROZEN |
| SRC-174 | packages/application/src/commands/intake-source.command.ts | 197 | 9f0020860749750699f1442ec17af5e18d75598c86c65c47b9b82f99868601c9 | METADATA_FROZEN |
| SRC-175 | packages/application/src/commands/open-impact-case.command.ts | 199 | 9d162aabacc868d74ec0a2c8873588fd95cf5a6dbf49664872fa579b7d52790f | METADATA_FROZEN |
| SRC-176 | packages/application/src/commands/open-recall-case.command.ts | 199 | e989c96272365ddb6d8052b23caa8a7f8097473c5c260904cf6a1a23cf586c67 | METADATA_FROZEN |
| SRC-177 | packages/application/src/commands/register-sot-record.command.ts | 202 | c204896032edd10f12d5f61e6ad681d94be395512cb5b7861c5482b7b9363622 | METADATA_FROZEN |
| SRC-178 | packages/application/src/commands/request-governed-output.command.ts | 206 | ad49ae15a55a05a78a9ba47bf0865069ab7fc9d64e3a4641dee217df4db1c709 | METADATA_FROZEN |
| SRC-179 | packages/application/src/commands/resolve-conflict.command.ts | 202 | ab6138bb1b64e5294380e53727b0dbb48ffd6b8d8fdcb3688960971325200ba3 | METADATA_FROZEN |
| SRC-180 | packages/application/src/commands/submit-refinery-packet.command.ts | 205 | 522e7134bc21cefba557279c00938f633ef843440a4716f30ecc8765bac4f000 | METADATA_FROZEN |
| SRC-181 | packages/application/src/commands/submit-review.command.ts | 197 | 91a766904f9c5df4cb231d52a998b4723be62d83cad04d9416f97497c4f45412 | METADATA_FROZEN |
| SRC-182 | packages/application/src/index.ts | 1317 | 56740c82b5b66cd59688e741bccfae5ac8c9202680460846772e16e70d548911 | METADATA_FROZEN |
| SRC-183 | packages/application/src/queries/get-context-package.query.ts | 209 | 580187923829c3796f85df9c81795f6305657e63bdb6b52f40b5b6faee18ce1a | METADATA_FROZEN |
| SRC-184 | packages/application/src/queries/get-impact-graph.query.ts | 206 | a179c568b0385dbc9281db1c6e4c6b0d35a89fdc236d1cf5512e83b44219c381 | METADATA_FROZEN |
| SRC-185 | packages/application/src/queries/get-output-trace.query.ts | 206 | 9befe6052bed301d68d5c79ac659f4dc25ab2e107c0a4a887747947d990f5269 | METADATA_FROZEN |
| SRC-186 | packages/application/src/queries/get-sot-record.query.ts | 204 | 5c6551688837840075534f06824015ba2a4f62098ca5623b38fa91f4d03b35a8 | METADATA_FROZEN |
| SRC-187 | packages/application/src/queries/list-conflicts.query.ts | 205 | 0d06cbd23beb00cad5852ca2159d15c6b3838e09d7837f4d5a0628c104e1e5c4 | METADATA_FROZEN |
| SRC-188 | packages/application/src/queries/list-recall-cases.query.ts | 207 | 2aa1eef10ebeb7a095d292f453f86cca634b93e0876f6b2547e90b735afa45ec | METADATA_FROZEN |
| SRC-189 | packages/application/src/queries/list-sot-records.query.ts | 206 | 64a7162ea01c0b886effc904a1230e26beaf26a131e15f3d13b1a56245551287 | METADATA_FROZEN |
| SRC-190 | packages/application/src/queries/list-sources.query.ts | 203 | 3a052e1373dc41f266aea855722bb9f933579fa7abd12152daca5ac8a1f50a24 | METADATA_FROZEN |
| SRC-191 | packages/application/src/services/context-builder.service.ts | 1858 | 339dd7d45bda7f2c9e35bc76b11a11cb7e6767584a750d6240798894e38c0c7b | METADATA_FROZEN |
| SRC-192 | packages/application/src/services/governed-output.service.ts | 1672 | 6b6e63bf914d09d65fb0fcb0a3f110c08d001e5d6b71738d1cfe2efa01e3f377 | METADATA_FROZEN |
| SRC-193 | packages/application/src/services/impact-recall.service.ts | 449 | 439f08ef1863db237c31a0ecb8ba51765800aaa4cfde5b1b1223fc5a8a4c2fd7 | METADATA_FROZEN |
| SRC-194 | packages/application/src/services/review-freeze.service.ts | 1598 | 133d29763e75de265f4d12d30597398e03a77409ca41b8ee16b6a7057b5f6f6b | METADATA_FROZEN |
| SRC-195 | packages/application/src/services/sot-registration.service.ts | 611 | c125e639a2e9730ad7fccff85f28c7478ee0f0853bfd64bebf22a2b41dba8829 | METADATA_FROZEN |
| SRC-196 | packages/application/src/services/source-intake.service.ts | 611 | 2292b91b8af91de0d1da97ec59fde17ad4fef18d0718770084cca802ad5cbedd | METADATA_FROZEN |
| SRC-197 | packages/contracts/package.json | 164 | daea100ceed271fd279b0240ef9500f7bb1918851deb125f42306ff1e72ee88c | METADATA_FROZEN |
| SRC-198 | packages/contracts/src/index.ts | 471 | 103d47334cf6451cec95697f74ce16940accb0d9aec1e0a236941c476a26e7b8 | METADATA_FROZEN |
| SRC-199 | packages/contracts/src/schemas/authority-record.schema.json | 1387 | 05b58ac90c22c56fa6006d40560c39ae343b3dc4e4f189b3a9af3115f8e3dabd | METADATA_FROZEN |
| SRC-200 | packages/contracts/src/schemas/context-package.schema.json | 1667 | 2a9b9a7adcb86829f67e57acfc26b469896250108a47ec25a114ae23306a7da6 | METADATA_FROZEN |
| SRC-201 | packages/contracts/src/schemas/decision-record.schema.json | 1092 | 64edb73d938b5f47ff22481af00b6be1dcb2ada68ff608c83ae3cac566a767f1 | METADATA_FROZEN |
| SRC-202 | packages/contracts/src/schemas/freeze-record.schema.json | 1505 | a95f2cb09c45adb173b03c7b29c824fbbda338ab85cb80ccbb06dfac7f0309e5 | METADATA_FROZEN |
| SRC-203 | packages/contracts/src/schemas/impact-record.schema.json | 1263 | eaa2e29f0503477d30ecd68870e323313fc9f8904b5ae69bdb6d6d42120dbbf3 | METADATA_FROZEN |
| SRC-204 | packages/contracts/src/schemas/output-artifact.schema.json | 1761 | 8071c06970557c4c6289ef756fb983dc15b59730053286ddd50ca6495d826eca | METADATA_FROZEN |
| SRC-205 | packages/contracts/src/schemas/recall-case.schema.json | 1629 | 214d2306c2292c90d0e546dafaafd5e347cc85333c4959c4544029c44677fe1d | METADATA_FROZEN |
| SRC-206 | packages/contracts/src/schemas/review-record.schema.json | 965 | 4d8a9ce99fcea2ec25e94440c76a03b38634078feb8055c1ec540755807a8f9a | METADATA_FROZEN |
| SRC-207 | packages/contracts/src/schemas/sot-record.schema.json | 2248 | 75bd734dc07169731ab3aa424ff4f589bce465ec8528b46127617921ded631b8 | METADATA_FROZEN |
| SRC-208 | packages/contracts/src/schemas/source-record.schema.json | 2161 | 5ffede78cf31a01e9911b0a9536465dc2370169fdbf15a0de19e4f647e1238d3 | METADATA_FROZEN |
| SRC-209 | packages/contracts/src/types/authority-record.ts | 518 | 149eb2a9ae24eb98ede63fb95d57d095a68a66991d1e421c07befc346a62a4fd | METADATA_FROZEN |
| SRC-210 | packages/contracts/src/types/context-package.ts | 583 | ade2d5f9e0a2a6b569443c57476ccaeeeaef7d36f6fdf469bdfc3902a06fbfa8 | METADATA_FROZEN |
| SRC-211 | packages/contracts/src/types/decision-record.ts | 344 | ce6f33e1677b35dc94a537c6f5ca899a0e5039c21cc61a39aa4da254134d4351 | METADATA_FROZEN |
| SRC-212 | packages/contracts/src/types/evidence-reference.ts | 335 | fb3b66745dc99e66e7601265ee38b58d34fe102b00be7dbd7e9bf9dd3ad7bc81 | METADATA_FROZEN |
| SRC-213 | packages/contracts/src/types/freeze-record.ts | 473 | 8407517b12e86a822264ca9e8d4338a074de27c7555c09364a813662c03cfcab | METADATA_FROZEN |
| SRC-214 | packages/contracts/src/types/impact-record.ts | 479 | ba6657034edadd3f920124f6efe5a7063e249c81d54bb5bfaaacb29702b8afbd | METADATA_FROZEN |
| SRC-215 | packages/contracts/src/types/output-artifact.ts | 663 | f13d2dcbcd3a1987d1eb9b4e78de398ce148e38089b4120081e18b96dd729f35 | METADATA_FROZEN |
| SRC-216 | packages/contracts/src/types/recall-case.ts | 568 | 3a1f5f6cf5610e1126eb034724016cdb7818bf831cf55ee3c953de3572ee339c | METADATA_FROZEN |
| SRC-217 | packages/contracts/src/types/review-record.ts | 492 | 3c1197ea080c41da4ddcb08ed2f55bde7a1f0c2db5747bd6df0fee85e243a322 | METADATA_FROZEN |
| SRC-218 | packages/contracts/src/types/sot-record.ts | 912 | 8d9f47feb6be1b40cfbe27679cc56cb3359593c724311a17f60596bb7ef041d0 | METADATA_FROZEN |
| SRC-219 | packages/contracts/src/types/source-record.ts | 802 | 399329b0958ca16fbd9d6da0e91084935b0d9607e4f2b73503863010e4babca3 | METADATA_FROZEN |
| SRC-220 | packages/cvf-bindings/package.json | 182 | 470458ba2dc0bc393c30c5e0205c31cfdc0698853cf96d40d96b1d78236d9607 | METADATA_FROZEN |
| SRC-221 | packages/cvf-bindings/src/binding-errors.ts | 419 | ec2a52624a95da096fa75229dfa46bfa674ccd9b24a1222e58c2ed9b8e62a9a4 | METADATA_FROZEN |
| SRC-222 | packages/cvf-bindings/src/binding-health.ts | 645 | 72c8c600e26d1d157727cbb4e912a15d8553aab8981518ca8d4964c448112633 | METADATA_FROZEN |
| SRC-223 | packages/cvf-bindings/src/cvf-entry.adapter.ts | 795 | 7ef9b66ba24758e4b1b0434d09f5433583070f2242571871ca28f8784a9992d2 | METADATA_FROZEN |
| SRC-224 | packages/cvf-bindings/src/evidence.adapter.ts | 961 | 73645bd968c42ae708c47126d0fe252ae3c6020d34be682b5db88c1138494733 | METADATA_FROZEN |
| SRC-225 | packages/cvf-bindings/src/governed-execution.adapter.ts | 974 | 9001a56843a1c209d7a715e5edced7a644eb81fcf0a9360998b78e9df6f8e99a | METADATA_FROZEN |
| SRC-226 | packages/cvf-bindings/src/guard-contract.adapter.ts | 766 | 8315bdfd0cd5001a0a4bb811ebd77fb926f7b717dbc5e05b47fd23bb3c4bcfe1 | METADATA_FROZEN |
| SRC-227 | packages/cvf-bindings/src/index.ts | 417 | 3fec067c704a6a866bbaefbc499f3611d5d0e4a9d933c3de44189dd1e37437fb | METADATA_FROZEN |
| SRC-228 | packages/cvf-bindings/src/phase-governance.adapter.ts | 1124 | b992cb3cc1744ad8e4d1721970e38f414f9bc7a530bb05eb693cfbcf9157da26 | METADATA_FROZEN |
| SRC-229 | packages/cvf-bindings/src/refinery.adapter.ts | 793 | 341dc6c508b149a89662b62d7f9e2e1495663a3b36bbe3275951991e0b1f2f67 | METADATA_FROZEN |
| SRC-230 | packages/cvf-bindings/src/truth-flow.adapter.ts | 1061 | ca3e5720fd2adece259ebf7c6722033ba90336abddb0561c52816a3852a61222 | METADATA_FROZEN |
| SRC-231 | packages/cvf-bindings/src/truth-kernel.adapter.ts | 1001 | 32fbc200bc2717fc7c7c3477334590fada1d3547ccaa067ba9809d76c38189da | METADATA_FROZEN |
| SRC-232 | packages/domain/package.json | 176 | 82563a7c382fe21a90757df708e197ca70da55b193bafd0cc1ece7a30d340996 | METADATA_FROZEN |
| SRC-233 | packages/domain/src/entities/authority.ts | 485 | e45a2ccd55b0bf8b149b2c70142586decdacd3645fd830f579c7701d11a060c9 | METADATA_FROZEN |
| SRC-234 | packages/domain/src/entities/context-package.ts | 403 | 00811b6be6d4c59e8c656de47f1119e59c40be1e4ac53407c5cfef681109a39d | METADATA_FROZEN |
| SRC-235 | packages/domain/src/entities/governed-output.ts | 446 | 253e60cd358bb252fa20e3e73835dc64c3ca95cca10557af0eeb1158b5cc4190 | METADATA_FROZEN |
| SRC-236 | packages/domain/src/entities/impact-edge.ts | 435 | c1d88deb01935c3c17ab6bc23459ff7db496c5e04f7b0a326fdd1afaa6291b82 | METADATA_FROZEN |
| SRC-237 | packages/domain/src/entities/recall-case.ts | 445 | c2e7fbc5d78fe9208a5fa74862bd44ba4416a1ecb509d4ad3f56c646ee23515c | METADATA_FROZEN |
| SRC-238 | packages/domain/src/entities/sot-record.ts | 533 | 0c93059a156a7b35c04edd85ed7a6bade4a4941752b76916b2f374a26ac9f40d | METADATA_FROZEN |
| SRC-239 | packages/domain/src/entities/source.ts | 512 | 7aa700b92494fe08ba292d5717063023830af24e32483cbbdd2fe754e6ddadd9 | METADATA_FROZEN |
| SRC-240 | packages/domain/src/index.ts | 1227 | 64a2432599752fbc6a96c84aeb3b4a9b08fd5903261dc0fa4df2b8cb007b686d | METADATA_FROZEN |
| SRC-241 | packages/domain/src/policies/authority-resolution.policy.ts | 775 | be3f80bd50400cd2a32d5362b3717dbdbd76d5affe4f531d17ba9cec494688b0 | METADATA_FROZEN |
| SRC-242 | packages/domain/src/policies/context-eligibility.policy.ts | 720 | ea8c7cc8f3545cb99e13ef21532a473917918a1171cc7f054c0496a6246967f7 | METADATA_FROZEN |
| SRC-243 | packages/domain/src/policies/publication.policy.ts | 682 | 562cd4d19255b3a7b5a9405dee1b924b39866549dad35db5637abf2146329940 | METADATA_FROZEN |
| SRC-244 | packages/domain/src/policies/recall-required.policy.ts | 297 | 3badd92d30668d66b9fc7b9b6ab8de846b6e9825348fd84be537b4f7104c6c4b | METADATA_FROZEN |
| SRC-245 | packages/domain/src/policies/review-required.policy.ts | 316 | 3ef43cc3f73b4c3c2c4d26a8d23fbaa13082f859784bd0b26cdffe28335484ed | METADATA_FROZEN |
| SRC-246 | packages/domain/src/policies/scope-overlap.policy.ts | 480 | 84898434035be21100c189f981c606b1007015d9a8819c415c20b56287f84fcd | METADATA_FROZEN |
| SRC-247 | packages/domain/src/services/authority-resolver.ts | 1141 | 3403deb2e09290ff455231551d1b20c161ae0db3641467f2b99fc8745a393f01 | METADATA_FROZEN |
| SRC-248 | packages/domain/src/services/context-eligibility.ts | 527 | b7c58ad131ad830772938ff8bef3571ec05c10bad0f10db33367fa466fb314be | METADATA_FROZEN |
| SRC-249 | packages/domain/src/services/impact-resolver.ts | 1179 | 4053631d5cda596c1f91e49e2e7a21951d4d898d754fff56b6292113a6f60ed4 | METADATA_FROZEN |
| SRC-250 | packages/domain/src/services/recall-planner.ts | 959 | 73b8a6032fe853ccbbcc5a4e85687e19c97203011c38a2224527f27cefec4010 | METADATA_FROZEN |
| SRC-251 | packages/domain/src/services/sot-record-classifier.ts | 388 | 6aa2b811943481bdfa912e8cf8a02a935d0745781a3cf8cc9b6225e6e3975f71 | METADATA_FROZEN |
| SRC-252 | packages/domain/src/value-objects/authority-level.ts | 529 | 7dc4dbdf72f8b380aaeb58ef542ef4fb0f1e4feb02144eba71cad6b5232c7461 | METADATA_FROZEN |
| SRC-253 | packages/domain/src/value-objects/confidentiality.ts | 411 | f4908ffff96a7a967cf47ad9319f6dd5b975cd9578e58e7c2855e76f70d58955 | METADATA_FROZEN |
| SRC-254 | packages/domain/src/value-objects/information-state.ts | 903 | 876a32d1feaad959178609e6f5148426884e516fc995463e0108112e90ddd971 | METADATA_FROZEN |
| SRC-255 | packages/domain/src/value-objects/known-time.ts | 274 | 540ccd06bd0a3817db9bc5539ef4bc3ea8e80ef0084be3adc6d5b2c8c63e1afe | METADATA_FROZEN |
| SRC-256 | packages/domain/src/value-objects/permitted-purpose.ts | 354 | b4773877da101f9e4d6c6c9542e47e0745196905628202a7efa93869785076dd | METADATA_FROZEN |
| SRC-257 | packages/domain/src/value-objects/sot-scope.ts | 821 | 91b7ad6455ca2f00976b6d0cb456055b3e1cba2d09efa974da412536cf5cb799 | METADATA_FROZEN |
| SRC-258 | packages/domain/src/value-objects/valid-time.ts | 708 | 5fa2fcef711f1a6f1012b1c11b2061b42e713ad14a935233698f831c17e2a8cb | METADATA_FROZEN |
| SRC-259 | packages/evidence/package.json | 178 | 023ebd4f1e66adcb77773fe949c597bb5262b5f04bb6ed61da5848a8adc13259 | METADATA_FROZEN |
| SRC-260 | packages/evidence/src/decision-trace.ts | 307 | 5e40340a0ad14ad86904a333f541b3339c28ea552d452382ea3a9dffa4103f05 | METADATA_FROZEN |
| SRC-261 | packages/evidence/src/evidence-envelope.ts | 840 | 7ee9e6d55cefed5effc87ff4304fbea0d63b79771e9489cedee086a5a3ca02f5 | METADATA_FROZEN |
| SRC-262 | packages/evidence/src/evidence-exporter.ts | 342 | 559e74e55693efcae4296603f25b2f5378250bb3b71c063fae6e8f1c25f6a5a8 | METADATA_FROZEN |
| SRC-263 | packages/evidence/src/freeze-package.ts | 792 | bb6d98ce161afff12c315a1172d14eef5d68bc48e6009d863912122ddcafbd5a | METADATA_FROZEN |
| SRC-264 | packages/evidence/src/index.ts | 264 | 66f444a01271cb5309ea6746445ee0343260c48d82ed2fc310f1f17fa65d6fab | METADATA_FROZEN |
| SRC-265 | packages/evidence/src/output-trace.ts | 262 | 7abaa575e6a66fb0d630c23631118e2771d61f8b6a9498eba60ce00603d2c769 | METADATA_FROZEN |
| SRC-266 | packages/evidence/src/receipt-integrity.ts | 435 | bbb2b3aeb2e203fc7b9409937dc413a68d2eb1b37884fc14e4bdc1c705f2ce66 | METADATA_FROZEN |
| SRC-267 | packages/evidence/src/source-trace.ts | 271 | 4aca8dc3edaa8669099b12d4f5e2f7dc1ff86db00eea73ba2837c4aef00ccdcb | METADATA_FROZEN |
| SRC-268 | packages/persistence-sqlite/migrations/001_initial_schema.sql | 787 | 1a410d7101d7b88825700c4976e23b40c2137c1c62df2cdce15284214f7c4c1f | METADATA_FROZEN |
| SRC-269 | packages/persistence-sqlite/migrations/002_authority_and_scope.sql | 1423 | 76c1dfb753dde63436bb134d6aa2a42f5caa14c48dcad871ea28b50ee0ff9dae | METADATA_FROZEN |
| SRC-270 | packages/persistence-sqlite/migrations/003_context_and_outputs.sql | 1711 | 5f8c86baa4f0dc8936acef8c17ddf33cf82f162402343ae2184bd54083848b42 | METADATA_FROZEN |
| SRC-271 | packages/persistence-sqlite/migrations/004_impact_and_recall.sql | 884 | 1287ef0a3c010d3565426641e2b26e9a9cdea81c63b30fa5723ca9305bc053bb | METADATA_FROZEN |
| SRC-272 | packages/persistence-sqlite/package.json | 288 | 51914706dffb9bdc6da90d9b89372298a834ad489ee673226b4f101145cf120a | METADATA_FROZEN |
| SRC-273 | packages/persistence-sqlite/src/database.ts | 267 | 8d7f4ce0ac31052c72a323562624349160ad07234793bebd7256a806659caa3c | METADATA_FROZEN |
| SRC-274 | packages/persistence-sqlite/src/index.ts | 694 | 8e5a35b85579817f112d22f4c9c9ec4c30069a0fdeffb68aac973e62f1789488 | METADATA_FROZEN |
| SRC-275 | packages/persistence-sqlite/src/repositories/audit.repository.ts | 1165 | acc9b99eed9296edf81a5c5b702b863179b605fa5d55e53e7263b2b139b08fbc | METADATA_FROZEN |
| SRC-276 | packages/persistence-sqlite/src/repositories/authority.repository.ts | 1786 | e5c93a6b8779bfa9efd192bc1678773eb4c9257f574afb8b97ba0f620aac5557 | METADATA_FROZEN |
| SRC-277 | packages/persistence-sqlite/src/repositories/conflict.repository.ts | 961 | 011ebba2e02e6b9096fb8486af2d4cff0fe80fdea44aed58d0b3afbeeaccaf12 | METADATA_FROZEN |
| SRC-278 | packages/persistence-sqlite/src/repositories/context-package.repository.ts | 2298 | f5f6031a530f57863f24b9d74e2c29cec152dff20886e1626afe2d7a23c7e6c5 | METADATA_FROZEN |
| SRC-279 | packages/persistence-sqlite/src/repositories/freeze.repository.ts | 827 | cc6b50163230934734daa1d735f1bd65536d0c9ed5acd491c7e669132f3d34b6 | METADATA_FROZEN |
| SRC-280 | packages/persistence-sqlite/src/repositories/impact.repository.ts | 1396 | b6b98ef3f4ab0082cb8dfe676cc581e8aa4926330c983c01a0d70b2ec985c12d | METADATA_FROZEN |
| SRC-281 | packages/persistence-sqlite/src/repositories/output.repository.ts | 2103 | e1a4974800731d56c770f31bf6c8376262ad239c88d40057ef3cf3310aa574f0 | METADATA_FROZEN |
| SRC-282 | packages/persistence-sqlite/src/repositories/recall.repository.ts | 1962 | f3f79322423c074e85d6ba630361626045a48ff70f99c28a4af18eec86398456 | METADATA_FROZEN |
| SRC-283 | packages/persistence-sqlite/src/repositories/review.repository.ts | 1364 | 90e549d1ef048544ed89970d011f54e5314472aa9583f8d9490c74fac13ba040 | METADATA_FROZEN |
| SRC-284 | packages/persistence-sqlite/src/repositories/sot-record.repository.ts | 3185 | 901ebe22f2dc686460c760e8b0ebb43bca40348d3e8ab3af0732c005d0d61304 | METADATA_FROZEN |
| SRC-285 | packages/persistence-sqlite/src/repositories/source.repository.ts | 2398 | 96db355307d9cfc9f8857fcafcd2bb31718d75b0fbcacf04ef98287cb6493cb8 | METADATA_FROZEN |
| SRC-286 | packages/persistence-sqlite/src/schema.ts | 863 | ee3729432e6c386311d9faba6bab8a715c30bb7f1dc5b536bff4183866b20f37 | METADATA_FROZEN |
| SRC-287 | packages/persistence-sqlite/src/transaction.ts | 162 | 95e473c7bfcbfc8764c428b3b0caff979a8f48ef2da68b0f012ce055fd0017d6 | METADATA_FROZEN |
| SRC-288 | packages/workflows/package.json | 292 | 2835de61dd56ff96c823c4deb8f6ce4a2cc416266ec4a9109af440c6ac5bca54 | METADATA_FROZEN |
| SRC-289 | packages/workflows/src/feedback.workflow.ts | 795 | b65ea2cf65d29db0b2de5b3a58211d49d142ca337a421acc61f781b06285fc27 | METADATA_FROZEN |
| SRC-290 | packages/workflows/src/governed-output.workflow.ts | 509 | 1e453f3e743d0ad88aa717c00ad31d2947bd67e7ad20029df102d7eac6a0dce5 | METADATA_FROZEN |
| SRC-291 | packages/workflows/src/index.ts | 417 | 4b4fc37053ab01e59e84f96f130e11dab18cb2afc03afb0e89a8a0159a617bcb | METADATA_FROZEN |
| SRC-292 | packages/workflows/src/kernel-to-sot.workflow.ts | 544 | d83c1b99310bd33973d6a8a5cbab90cff3ac677f4af18ea4bf1a3a706eaec9ff | METADATA_FROZEN |
| SRC-293 | packages/workflows/src/recall.workflow.ts | 281 | 98e57ecb8cbc60750274269562354f878ae943d1a560618dc6a26e2e611a3638 | METADATA_FROZEN |
| SRC-294 | packages/workflows/src/refinery-to-kernel.workflow.ts | 346 | 2f7f33d334d3ab9258b2a33f097bcf4ad7f2436f8260cbaa03b72036f5f894a0 | METADATA_FROZEN |
| SRC-295 | packages/workflows/src/review-and-freeze.workflow.ts | 347 | b9b60b4214a2e3583553f3f9ec74e0eba5ff4fd3b850dc3e2da12d7ad6d6e145 | METADATA_FROZEN |
| SRC-296 | packages/workflows/src/sot-to-context.workflow.ts | 297 | 59f2b5469c9c8a2e2d65509526f4b9bdbaa7311d4a8b9c607e470f133f081de2 | METADATA_FROZEN |
| SRC-297 | packages/workflows/src/source-change-impact.workflow.ts | 273 | 37bde35da1f6a2fa3aba44116f687166a43184784fd30209944a95aae681cbae | METADATA_FROZEN |
| SRC-298 | packages/workflows/src/source-to-refinery.workflow.ts | 467 | 7914d8a3727efda54e5cef87ee805ec842648db74c5d614e86a72bf756de21f4 | METADATA_FROZEN |
| SRC-299 | pnpm-workspace.yaml | 40 | 08d75840c97ab0e72d1d9b5b84a17e47a2e06cb159a5fbec5ee0a6a56682dad7 | METADATA_FROZEN |
| SRC-300 | scripts/bootstrap.ts | 1126 | 992888b4c7b8c653e4fdedf5faf8d3585437ceb97bfa222f57d63bd327cfae89 | METADATA_FROZEN |
| SRC-301 | scripts/doctor.ts | 1234 | fb810eaa8e455fbf866ec3378d5e72880c1e0e6345c9a1b87e21870ff5452a5c | METADATA_FROZEN |
| SRC-302 | scripts/export-evidence.ts | 830 | 89071d30581ee073d168540668725dc08f16f8d9f8c67654d48c18b5d9fc80af | METADATA_FROZEN |
| SRC-303 | scripts/migrate.ts | 387 | f37298e8ca46f7d7ec6cd1c31e3b6f6ef300bc33dda778c1f66d88aa050f41a3 | METADATA_FROZEN |
| SRC-304 | scripts/run-controlled-quotation.ts | 1059 | 11184318e2bcfc77cad8451c30eb2e9b7ef317f89cc5bbd82f42f18a13ecade8 | METADATA_FROZEN |
| SRC-305 | scripts/run-failure-injection.ts | 886 | 60381646fc5f33cd16f413337dab6570a3dd6fb9b8e41b13f77a9318887f9f0c | METADATA_FROZEN |
| SRC-306 | scripts/seed.ts | 758 | d137f3e5ef4ea2252deb6a101d35e012505bcf11a9d02db73f541d43cebc1d4a | METADATA_FROZEN |
| SRC-307 | scripts/validate-config.ts | 1216 | 73e9dee6739926d02f0b40012cbaebc628f49724650e528da61976d960737fe4 | METADATA_FROZEN |
| SRC-308 | scripts/validate-cvf-bindings.ts | 982 | 5e3106915083fd21ff4c9512d572fe71ca77d1b283e5af6daff86cfe2f199815 | METADATA_FROZEN |
| SRC-309 | tests/e2e/controlled-quotation.e2e.test.ts | 734 | 7ee0122074d813427e744ed33322db425a413826872ac61a58da706b9e65eea6 | METADATA_FROZEN |
| SRC-310 | tests/failure-injection/claim-as-fact.test.ts | 277 | 4975067231aeba1dbe5aeef99d2f5160fafb42a6f2d75e68898738df4239b1ed | METADATA_FROZEN |
| SRC-311 | tests/failure-injection/guard-rejection.test.ts | 289 | 6f0080d5face04e12cf8dbdf812c03dde3356e79592da11cf31c5d4845c89ff3 | METADATA_FROZEN |
| SRC-312 | tests/failure-injection/invalid-freeze.test.ts | 296 | b926cc2393d9d4ede02ecc9a39b0a45515c98912ae1f5f4c8101bd587852968f | METADATA_FROZEN |
| SRC-313 | tests/failure-injection/kernel-unavailable.test.ts | 291 | 37c066250b483e6fcf5620477ff9b0a8c29aff12a3ea99608b6dd6ffb16413d8 | METADATA_FROZEN |
| SRC-314 | tests/failure-injection/missing-owner.test.ts | 267 | 0f049efbfcd0b81e02239b4451ab1a825b7f412dae347b5cd5dcc0304ff1b9ff | METADATA_FROZEN |
| SRC-315 | tests/failure-injection/missing-review.test.ts | 277 | f451414a0cdfde42f84bbb1684765aa131e6065c0c6d5a62d8d5e268d618d1d6 | METADATA_FROZEN |
| SRC-316 | tests/failure-injection/revoked-reference.test.ts | 279 | f347b7d02e115747669ab5aca05b70a3bd33a38d6fc29c27c40d4a3cbc3440fd | METADATA_FROZEN |
| SRC-317 | tests/failure-injection/scope-leak.test.ts | 294 | e135845efcfdf91ef349a6eea9d7ad2af4006b48b1f3701aff04e627f8cdf2df | METADATA_FROZEN |
| SRC-318 | tests/failure-injection/source-tampering.test.ts | 310 | f8a6de8b7efed20c3e655f9f7a19d8cee2bf7acb79d200a55844625b5f753519 | METADATA_FROZEN |
| SRC-319 | tests/failure-injection/stale-source.test.ts | 321 | 0f203d84375d4d619b1102529f9e4aeec5552a7404e06f7cd02d3a637c5d4892 | METADATA_FROZEN |
| SRC-320 | tests/integration/impact-recall.test.ts | 419 | 681bd983d3654779c434c5084ce89851f8ab13c84185330b8f965a6aa260b4ee | METADATA_FROZEN |
| SRC-321 | tests/integration/phase-governance-binding.test.ts | 552 | 6ba19727f7bc6fcb31a86dbcdf22db2ceab8d4c4d40aecf1cb906807d387b2f6 | METADATA_FROZEN |
| SRC-322 | tests/integration/refinery-binding.test.ts | 369 | 397e75e75e7e0603b9d762ec3f4c7ff241981d39afb0f190ee25c376abde1e4e | METADATA_FROZEN |
| SRC-323 | tests/integration/review-freeze.test.ts | 1195 | 44585356c9c791b6e0e2cc74a9d488b1bb29eefe46bb9f571af1d152ed768b63 | METADATA_FROZEN |
| SRC-324 | tests/integration/sot-to-context.test.ts | 884 | ee96599583592e130c0db9a968c9e20e67721b1a00af8de6447287f4511ebce0 | METADATA_FROZEN |
| SRC-325 | tests/integration/source-to-sot.test.ts | 1217 | 4a8f7c8ae67a08700a4bf57ab9ec03e9ce4fcac2e14a14204ad45d2e68caf109 | METADATA_FROZEN |
| SRC-326 | tests/integration/truth-flow-binding.test.ts | 739 | 9c99907dbc7ab33c1577effdb520c725d419c5b6880da737e81ca1c0d7927571 | METADATA_FROZEN |
| SRC-327 | tests/integration/truth-kernel-binding.test.ts | 551 | b1801152ceba1b254ad738e09111cd07c1867ed4f527fbb848642929e3cfe8cd | METADATA_FROZEN |
| SRC-328 | tests/unit/authority-resolver.test.ts | 879 | 6adf89fe0cd502093f5194e9de74a78c072b63264bee316706e9250585f13ce0 | METADATA_FROZEN |
| SRC-329 | tests/unit/context-eligibility.test.ts | 1044 | 52e797b52763afd759bd648e9057a00294842af2bae8bd73806fe08cbfba5544 | METADATA_FROZEN |
| SRC-330 | tests/unit/impact-resolver.test.ts | 458 | 1e61ce90899d557b40e3ed0e4d0b21cfeb272c88d12f1c07cab7e81b40a286e6 | METADATA_FROZEN |
| SRC-331 | tests/unit/publication-policy.test.ts | 884 | c6dbbc8fa27d350c7612f7222c9a934e827b3de843cbf595e5cec57a2759499b | METADATA_FROZEN |
| SRC-332 | tests/unit/recall-planner.test.ts | 541 | c922e29c70db3e430fe3fae70102fbf36d1a0747c12914d854ae83418e46caa1 | METADATA_FROZEN |
| SRC-333 | tests/unit/scope-overlap.test.ts | 427 | ef5e4f48a2aa3e4311305e3eccc7ece16ea6ebc95f84186cb4b843c1be3b039f | METADATA_FROZEN |
| SRC-334 | tests/unit/sot-record-classifier.test.ts | 623 | 3ab9f13158c5ebf759a16cabad8c101360fde0c34e611241653c7d8c0dba234d | METADATA_FROZEN |
| SRC-335 | tsconfig.base.json | 947 | 2b6a15abe9d9b89bd971929ad7c34b7a3e871f7548ae352444628784c8078dde | METADATA_FROZEN |
| SRC-336 | vitest.workspace.ts | 139 | ccbbdcd8da005f58903265c016d170f07e8efeeb72ce14a8df3db7a685b9dc99 | METADATA_FROZEN |

## Complete Hidden-Clone Declaration Inventory

Exactly 13 physical occurrences of the fixed-string target
`.Controlled-Vibe-Framework-CVF` were found. Candidate routing below is
non-terminal; T0B retains all final provenance dispositions per the work
order.

| declarationId | sourcePath | sourceLine | literalTarget | declarationClass | resolvedTarget | targetExists | candidateOwnerRoute | candidateDriftDisposition | candidateRuntimeUseDisposition | t0aState |
|---|---|---:|---|---|---|---|---|---|---|---|
| DEC-01 | README.md | 11 | `.Controlled-Vibe-Framework-CVF/` | TREEVIEW_REFERENCE | `../.Controlled-Vibe-Framework-CVF` (implied by sibling tree diagram) | true | DOWNSTREAM_APP_ONLY | candidate: informational only, no version pin | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-02 | .cvf/manifest.json | 5 | `../.Controlled-Vibe-Framework-CVF` | MANIFEST_ROOT | `../.Controlled-Vibe-Framework-CVF` | true | SOT3_APP_T1 | candidate: single unversioned governance-root pointer | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-03 | TREEVIEW.md | 3 | `.Controlled-Vibe-Framework-CVF/` | TREEVIEW_REFERENCE | `../.Controlled-Vibe-Framework-CVF` (implied by sibling tree diagram) | true | DOWNSTREAM_APP_ONLY | candidate: informational only, no version pin | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-04 | .env.example | 8 | `../.Controlled-Vibe-Framework-CVF` | ENVIRONMENT_DEFAULT | `../.Controlled-Vibe-Framework-CVF` | true | SOT3_APP_T1 | candidate: unpinned relative-path env default | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-05 | .cvf/bindings/truth-kernel.binding.json | 4 | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_TRUTH_KERNEL` | BINDING_TARGET | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_TRUTH_KERNEL` | false | SOT3_APP_T1 | candidate: declared target missing at hidden-clone HEAD `a78b35c`; active provenance workspace has a same-named current owner but is not the resolved target | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-06 | .cvf/bindings/refinery.binding.json | 4 | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_REFINERY` | BINDING_TARGET | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_REFINERY` | false | SOT3_APP_T1 | candidate: declared target missing at hidden-clone HEAD `a78b35c`; active provenance workspace has a same-named current owner but is not the resolved target | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-07 | .cvf/bindings/guard-contract.binding.json | 4 | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_GUARD_CONTRACT` | BINDING_TARGET | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_GUARD_CONTRACT` | true | SOT3_APP_T1 | candidate: unversioned binding-target pointer, no pinned commit/tag | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-08 | .cvf/bindings/truth-flow.binding.json | 4 | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_TRUTH_FLOW` | BINDING_TARGET | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_TRUTH_FLOW` | false | SOT3_APP_T1 | candidate: declared target missing at hidden-clone HEAD `a78b35c`; active provenance workspace has a same-named current owner but is not the resolved target | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-09 | .cvf/bindings/phase-governance.binding.json | 4 | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` | BINDING_TARGET | `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` | true | SOT3_APP_T1 | candidate: unversioned binding-target pointer, no pinned commit/tag | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-10 | .cvf/bindings/cvf-entry.binding.json | 4 | `../.Controlled-Vibe-Framework-CVF` | BINDING_TARGET | `../.Controlled-Vibe-Framework-CVF` | true | SOT3_APP_T1 | candidate: unversioned binding-target pointer, no pinned commit/tag | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-11 | .cvf/bindings/evidence.binding.json | 4 | `../.Controlled-Vibe-Framework-CVF` | BINDING_TARGET | `../.Controlled-Vibe-Framework-CVF` | true | SOT3_APP_T1 | candidate: unversioned binding-target pointer, no pinned commit/tag | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-12 | docs/ARCHITECTURE.md | 7 | `.Controlled-Vibe-Framework-CVF/` | TREEVIEW_REFERENCE | `../.Controlled-Vibe-Framework-CVF` (implied by sibling tree diagram) | true | DOWNSTREAM_APP_ONLY | candidate: informational only, no version pin | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |
| DEC-13 | apps/api/src/config.ts | 18 | `env.CVF_CORE_PATH ?? "../.Controlled-Vibe-Framework-CVF"` | CODE_DEFAULT | `../.Controlled-Vibe-Framework-CVF` (fallback default) | true | SOT3_APP_T1 | candidate: unpinned code-level fallback default mirrors env default | DECLARED_ONLY_NOT_EXECUTED | DECLARATION_ENUMERATED |

Declaration search command:
`rg -n --hidden --no-ignore -F ".Controlled-Vibe-Framework-CVF" .` executed
from the literal source root; result count 13, matching the committed
dispatch baseline exactly. `CVF_CORE_PATH` occurs at `.env.example:8` (DEC-04)
and `apps/api/src/config.ts:18` (DEC-13); `CVF_WORKSPACE_ROOT=..` occurs at
`.env.example:7` but does not itself contain the literal fixed-string target
and is not counted as a fourteenth occurrence.

Reviewer path-resolution recomputation used each declared path relative to
the literal SOT-Application root. The hidden repository root exists and is
clean at `a78b35c`, but its `EXTENSIONS/` directory lacks
`CVF_TRUTH_KERNEL`, `CVF_REFINERY`, and `CVF_TRUTH_FLOW`. Therefore DEC-05,
DEC-06, and DEC-08 are missing-target evidence, not validated bindings. The
same-named directories in the active provenance workspace do not satisfy the
sibling application's literal relative paths.

## Reviewer-Selected Semantic Calibration Sample (SAM-01 through SAM-20)

Every sample hash below was independently recomputed from the current
physical file and matched the committed dispatch expectation exactly
(20/20 MATCH; see Findings / Position).

| sampleId | sampleGroup | sourcePath | sourceSha256 | processingStatus | disposition | valueClass | overlapClass | ownerRoute | nextGovernedAction | reason | adversarialChallenge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SAM-01 | doctrine | README.md | 5d01f41b7e9de5c7f86a42a1f36d533bcd7bf0aba7c7f2bedc8ec69a6f95be8b | READ | ADAPT | DOCTRINE_ADAPTED | ENRICH_EXISTING | `docs/reference/sot_three_layer/README.md` | source-verify against current three-layer doctrine in T1; no CVF Core promotion | defines a full downstream business lifecycle (source, authority, context, output, review, freeze, impact, recall) consistent with SOT3 doctrine intent and explicitly disclaims public-runtime/production claims | challenge: could this be dismissed as marketing prose with no package/runtime value; rejected because it defines a concrete responsibility split (SOT Application owns business domain; CVF owns execution boundaries) and a "must not" list (no ungoverned provider calls, no bypassing Guard Contract) that is directly checkable against later code, so latent doctrine value is retained rather than defaulting to NO_NEW_VALUE |
| SAM-02 | doctrine | docs/ARCHITECTURE.md | 1cff0111b87b1849b2deae8023c62ba54fec6b71f7204eea63d930c0d76cedf9 | READ | ADAPT | DOCTRINE_ADAPTED | CONFIRMED_EXISTING | `docs/reference/sot_three_layer/README.md` | source-verify downstream/core dependency direction in T1 | states dependency is one-way from SOT Application to CVF and lists concrete package layers (contracts, domain, application, cvf-bindings, workflows, persistence-sqlite, evidence) matching the README's responsibility split | challenge: is this just a duplicate of the README's architecture section; rejected because it adds a distinct "Trust rule" (transport/UI/DB/model/provider are not trust sources) that SAM-01's text does not state, so this is ADAPTED_WITH_REASON rather than pure duplication and is not NO_NEW_VALUE |
| SAM-03 | doctrine | docs/CLAIM_BOUNDARY.md | fb2b3b5faf6a2e3c313aac3d63623e21b31003a122b956cbcad9b22e11143886 | READ | ADAPT | DOCTRINE_ADAPTED | ENRICH_EXISTING | `docs/CVF_ARCHITECTURE_DECISIONS.md` (claim-boundary discipline pattern) | compare claim-boundary wording pattern against CVF's own claim-boundary discipline in T1 | defines an explicit evidence ladder (specs/schemas -> unit/migration tests -> CVF adapter integration tests -> governed e2e vertical slice with replayable receipts -> operational deployment/sustained audit) gating what can be claimed at each stage | challenge: is this generic disclaimer boilerplate with no new value; rejected because the evidence ladder is a concrete, orderable checklist that could directly inform CVF's own claim-boundary tooling, so ENRICH_EXISTING is retained instead of NO_NEW_VALUE |
| SAM-04 | doctrine | docs/REVIEW_FREEZE_PROTOCOL.md | 60da0585588db647aa7249af8516cdeae1848c6c952a2a3582265e5d6154623e | READ | ADAPT | DOCTRINE_ADAPTED | ENRICH_EXISTING | `docs/reference/sot_three_layer/README.md` (REVIEW/FREEZE phase concepts) | source-verify freeze_record schema fields against any current CVF freeze/evidence contract in T1 | defines a concrete freeze_record YAML shape (freeze_id, output_id, output_hash, receipts, routing_decisions, policy_state, review_records, approvers, actor_and_execution_lane, freeze_hash) and states freeze is append-only | challenge: could this schema merely duplicate SAM-20's fixture without independent value; rejected because this file is the doctrine-level schema definition while SAM-20 is a filled sample instance, so they serve different roles (contract vs. example) and both retain distinct value |
| SAM-05 | no-new-value control | TREEVIEW.md | 208f4b0708f20f9115450cac7035cc2e47ff85010a313808fd5a370801265bce | READ | NO_NEW_VALUE | NO_PACKAGE_OR_RUNTIME_VALUE | NO_NEW_VALUE | none; navigation artifact only | retain as evidence only; no further action | pure directory-tree navigation listing duplicating the file-layout information already implied by the physical manifest and ARCHITECTURE.md | challenge (required by work order): does the tree order or grouping reveal a latent doctrine/package boundary not stated elsewhere; reviewed line-by-line and found the file adds no annotation, rationale, or grouping beyond alphabetical/structural directory order already fully reconstructible from the 336-row metadata table, so NO_PACKAGE_OR_RUNTIME_VALUE is confirmed rather than defaulted |
| SAM-06 | provenance | .cvf/manifest.json | 21d1ab9073f154f15d30784b4044437b650c9b645f76f1a2f4aa9fdf0e2958dc | READ | DEFER | RUNTIME_CANDIDATE | OWNER_SURFACE_NOT_FOUND | none found; candidate future provenance/adapter owner | terminal provenance disposition and owner ratification in T0B/T1 | declares `governance_root: "../.Controlled-Vibe-Framework-CVF"` (DEC-02), lists 7 required bindings, and asserts `fail_closed: true`; reviewer recomputation shows three declared extension targets are absent from the literal hidden clone | challenge: DEFER remains honest because T0A proves declaration and missing-target state but does not prove runtime loading; T0B must decide whether to sever, update, version-pin, or block each path rather than treating manifest intent as integration |
| SAM-07 | provenance | .cvf/bindings/truth-kernel.binding.json | a696ddbef39870bd8b6c633c6354c61da039b2bef94d992e0bd65505ccc39666 | READ | DEFER | RUNTIME_CANDIDATE | OWNER_SURFACE_NOT_FOUND | current owner candidate: `EXTENSIONS/CVF_TRUTH_KERNEL` in the active provenance workspace; literal declared target is missing | terminal missing-target and version/provenance decision in T0B/T1; separately compare the local accepted_decisions list with the current owner contract | declares a required target at `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_TRUTH_KERNEL` (DEC-05), which does not exist at hidden-clone HEAD `a78b35c`; its decision list text matches SAM-11's locally declared interface, but no source proves the binding file is loaded by that adapter | challenge: the matching vocabulary does not establish runtime consumption; the missing literal target makes the provenance gap concrete, so DEFER is retained rather than inventing integration or discarding the declaration as NO_NEW_VALUE |
| SAM-08 | provenance | .cvf/bindings/truth-flow.binding.json | 238b416f4eeb85c656b06e85545dd737a96dd57d74095c06ce5a9e4c51505b79 | READ | DEFER | RUNTIME_CANDIDATE | OWNER_SURFACE_NOT_FOUND | current owner candidate: `EXTENSIONS/CVF_TRUTH_FLOW` in the active provenance workspace; literal declared target is missing | terminal missing-target and version/provenance decision in T0B/T1; separately source-verify decision semantics against the current owner | declares a required target at `../.Controlled-Vibe-Framework-CVF/EXTENSIONS/CVF_TRUTH_FLOW` (DEC-08), which does not exist at hidden-clone HEAD `a78b35c`, plus `default_route: "BLOCK"` and a local decision list matching SAM-12's interface vocabulary | challenge: the BLOCK default is declarative and the missing target prevents it from proving any active fail-closed behavior; T0B must retain the gap rather than treating the declaration as safe integration |
| SAM-09 | provenance | .env.example | 3a369c5ed83c1618740f371cfb9772776b86451d643e89b40b07006757059667 | READ | DEFER | RUNTIME_CANDIDATE | OWNER_SURFACE_NOT_FOUND | none found; candidate future provenance/config owner | terminal provenance disposition for CVF_CORE_PATH/CVF_WORKSPACE_ROOT defaults in T0B | declares `CVF_WORKSPACE_ROOT=..`, `CVF_CORE_PATH=../.Controlled-Vibe-Framework-CVF` (DEC-04), `CVF_BINDING_MODE=local`, `CVF_FAIL_CLOSED=true`, `CVF_PROVIDER_CALLS_ENABLED=false` | challenge: is an example env file inherently low-value and safe to mark NO_NEW_VALUE; rejected because `CVF_PROVIDER_CALLS_ENABLED=false` combined with `CVF_FAIL_CLOSED=true` is a concrete fail-closed default posture worth carrying forward as provenance/config evidence, not discarding |
| SAM-10 | provenance | apps/api/src/config.ts | 22ae2e2f83c600bfdcf9fffd8ad948e68bc75ccb01d717ab3013247d9dc12fba | READ | DEFER | RUNTIME_CANDIDATE | OWNER_SURFACE_NOT_FOUND | none found; candidate future provenance/config owner | terminal provenance disposition alongside SAM-09 and DEC-13 in T0B | `loadConfig()` reads `env.CVF_CORE_PATH ?? "../.Controlled-Vibe-Framework-CVF"` (DEC-13) as a code-level fallback default mirroring `.env.example`, and reads `CVF_FAIL_CLOSED` defaulting to `"true"` | challenge: is a fallback default merely defensive coding with no provenance risk; rejected because an unpinned relative-path fallback baked directly into application code (not just an example file) is a stronger coupling signal than SAM-09 alone, so it is tracked as a distinct declaration rather than merged/dropped |
| SAM-11 | runtime candidate | packages/cvf-bindings/src/truth-kernel.adapter.ts | 32fbc200bc2717fc7c7c3477334590fada1d3547ccaa067ba9809d76c38189da | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `EXTENSIONS/CVF_TRUTH_KERNEL` (current T8 contract, not yet cross-verified) | do not import directly; T1/T2 must source-verify this adapter's `KernelEvaluationResult` shape against the current CVF_TRUTH_KERNEL contract before any reuse | defines `TruthKernelAdapter` with `evaluatePacket`/`assertReferences` methods and a `failClosed` helper invoked when `this.port` is undefined, i.e. fails closed on missing binding | challenge: does fail-closed behavior make this adapter safe to adopt as-is; rejected as premature ADAPT because the adapter is written against a locally-declared `TruthKernelPort` interface that has not been cross-verified against the actual current `EXTENSIONS/CVF_TRUTH_KERNEL` contract in this repository, so REJECT_DIRECT_IMPORT is the honest, non-overclaiming disposition pending T1 verification, not outright REJECT of all value |
| SAM-12 | runtime candidate | packages/cvf-bindings/src/truth-flow.adapter.ts | ca3e5720fd2adece259ebf7c6722033ba90336abddb0561c52816a3852a61222 | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `EXTENSIONS/CVF_TRUTH_FLOW` (current contract, not cross-verified here) | do not import directly; T1/T2 must source-verify each decision's required continuation semantics and every downstream consumer | defines `TruthFlowAdapter.route()`, which throws only for `BLOCK` and otherwise returns `WARN`, `ESCALATE`, or `REVIEW_REQUIRED` to its caller; static source does not prove those outcomes are safe to continue | challenge: the integrated intake review accepted rebuttal R-03 only with narrowing: the repeated BLOCK-only checks are a systemic semantics gap, but T0A must not presume all non-ALLOW decisions are equivalent; REJECT_DIRECT_IMPORT is retained pending a source-verified continuation matrix |
| SAM-13 | runtime candidate | packages/application/src/services/governed-output.service.ts | 6b6e63bf914d09d65fb0fcb0a3f110c08d001e5d6b71738d1cfe2efa01e3f377 | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `packages/application` (downstream owner; no current CVF Core equivalent) | do not import directly; T1 must verify whether `execution.execute()` performs any governance check equivalent to SAM-12's route decision before output creation | `create()` throws only when `input.context.route_decision === "BLOCK"`, then unconditionally calls `this.execution.execute(...)` and returns an artifact with `state: "REVIEW_REQUIRED"` | challenge: does setting state to REVIEW_REQUIRED by itself provide adequate governance; rejected as sufficient on its own, because the same single-string `"BLOCK"` check pattern from SAM-12 is repeated here with no independent secondary gate, so this is flagged as a second instance of the same continuation-risk pattern rather than treated as an isolated, low-risk file |
| SAM-14 | runtime candidate | packages/application/src/services/context-builder.service.ts | 339dd7d45bda7f2c9e35bc76b11a11cb7e6767584a750d6240798894e38c0c7b | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `packages/application` (downstream owner; no current CVF Core equivalent) | do not import directly; T1 must verify whether `eligibleRecords()` domain filtering plus `flow.route()` result is sufficient before context distribution regardless of route decision | calls `eligibleRecords()` for clearance filtering, then `this.flow.route(...)` (SAM-12's adapter), and returns a `ContextPackage` carrying `route_decision` for the caller to interpret | challenge: since this only builds a package and returns route_decision rather than acting on it, is it out of scope for the fail-open concern; rejected as out of scope, because it is the direct upstream caller of SAM-12's adapter and its return value is exactly what SAM-13's consumer must check, so all three files (SAM-12, SAM-13, SAM-14) form one continuation-risk chain that must be evaluated together in T1, not independently |
| SAM-15 | runtime candidate | apps/api/src/middleware/cvf-governance.middleware.ts | 830c354ca3e2d1cf09ca6ac38b1cbbd071562067919f300bc01db5a6f1baf1b8 | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `apps/api` (downstream owner; no current CVF Core equivalent) | do not import directly; T3 must run an authorized negative request test for missing and array-valued `x-cvf-phase` before making any continuation or fail-open claim | the async preHandler sends and awaits an HTTP 428 `SOT_PHASE_BINDING_REJECTED` reply but has no explicit `return`; static source proves that shape, not whether Fastify executes the route handler afterward | challenge: the integrated intake review classified rebuttal R-04 as PARTIAL_REJECT and explicitly prohibited a runtime fail-open conclusion from static source; this row therefore retains a behavior-proof gap and direct-import rejection without claiming observed fall-through |
| SAM-16 | evidence candidate | packages/evidence/src/freeze-package.ts | bb6d98ce161afff12c315a1172d14eef5d68bc48e6009d863912122ddcafbd5a | READ | ADAPT | DOCTRINE_ADAPTED | ENRICH_EXISTING | `docs/REVIEW_FREEZE_PROTOCOL.md` (SAM-04) freeze_record shape | source-verify `buildFreezePackage()` output-id/freeze-id consistency check against any current CVF freeze/evidence contract in T1 | `buildFreezePackage()` throws `SOT_FREEZE_OUTPUT_MISMATCH` when `output.output_id !== freeze.output_id`, and stamps `claim_boundary: "HISTORICAL_RELEASE_STATE_NOT_FUTURE_VALIDITY_GUARANTEE"` on every package | challenge: is the mismatch check trivial input validation with no doctrine value; rejected because embedding an explicit, machine-checkable claim-boundary string directly in the evidence structure (not just in a markdown doctrine file) is a concrete implementation pattern CVF's own evidence packages could adapt, so ENRICH_EXISTING is retained |
| SAM-17 | test-quality | tests/e2e/controlled-quotation.e2e.test.ts | 7ee0122074d813427e744ed33322db425a413826872ac61a58da706b9e65eea6 | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `tests/e2e` (downstream owner; no current CVF Core equivalent) | do not treat as behavior proof; T1/T3 must add a real end-to-end assertion or rename/relabel the file to avoid overclaiming | test named `controlled-quotation.e2e.test.ts` and described as "controlled quotation fixture harness" asserts only that 11 named fixture files `existsSync(...)` under `fixtures/controlled-quotation/` | challenge: does the `.e2e.test.ts` filename plus "e2e" describe-block risk being cited later as proof of governed end-to-end behavior; this is exactly the claim-boundary risk SAM-01/SAM-03's own doctrine warns against ("file existence... do not prove live governance"), so this is flagged as a naming/proof-strength defect (fixture existence check mislabeled as e2e) rather than accepted as REJECT_DIRECT_IMPORT solely for being a test file |
| SAM-18 | test-quality | tests/integration/truth-kernel-binding.test.ts | b1801152ceba1b254ad738e09111cd07c1867ed4f527fbb848642929e3cfe8cd | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `EXTENSIONS/CVF_TRUTH_KERNEL` (current T8 contract, not yet cross-verified) | do not treat as binding proof against the current CVF_TRUTH_KERNEL contract; T1 must re-run against the real contract, not this local mock port | constructs a `TruthKernelAdapter` with an inline mock port object (`evaluatePacket`/`assertReferences` returning hardcoded `REJECT`/`false`) and asserts `assertReferences(["KR1"])` rejects with `token: "SOT_REFERENCE_REVOKED"` | challenge: does exercising the real `TruthKernelAdapter` class (SAM-11) rather than a bare mock give this stronger proof value than SAM-17; acknowledged as stronger than SAM-17 (it does exercise real adapter logic, not just file existence), but still only proves the adapter's own internal fail-closed branch against a hand-authored mock port, not the actual current CVF_TRUTH_KERNEL contract, so REJECT_DIRECT_IMPORT as binding proof is retained while noting its comparatively higher proof quality for T1's benefit |
| SAM-19 | negative-proof | tests/failure-injection/missing-review.test.ts | f451414a0cdfde42f84bbb1684765aa131e6065c0c6d5a62d8d5e268d618d1d6 | READ | REJECT | REJECT_DIRECT_IMPORT | REJECT_DIRECT_IMPORT | `tests/failure-injection` (downstream owner; no current CVF Core equivalent) | do not treat as fail-closed proof; T1/T3 must replace with a real assertion that a missing-review condition actually blocks output freeze in code | test body only asserts `expect([]).toHaveLength(0)` and `expect(failureToken).toBe("SOT_REVIEW_INCOMPLETE")` against a local string literal; it does not invoke any review/freeze service or assert a thrown/blocked outcome | challenge: could this be dismissed as simply an early scaffold with placeholder intent, thus low priority; the finding is flagged with elevated priority precisely because the file name and describe block claim negative fail-closed proof ("detects SOT_REVIEW_INCOMPLETE") while the assertions prove nothing about actual system behavior, mirroring the same test-quality gap pattern as SAM-17 and warranting a T3 test-quality repair lane, not silent NO_NEW_VALUE |
| SAM-20 | fixture | fixtures/controlled-quotation/expected-freeze-record.yaml | 33a25d2d28ef7502fed8b6aaf64ef652d770f0ce59ea32de0d4ef5412f7f13f7 | READ | ADAPT | DOCTRINE_ADAPTED | ENRICH_EXISTING | `docs/REVIEW_FREEZE_PROTOCOL.md` (SAM-04) freeze_record shape | retain as a worked example alongside SAM-04's schema; T1 must confirm no test currently asserts this fixture's values against real freeze output | fills SAM-04's freeze_record schema with concrete sample values, all content/output/freeze hashes are literal all-`d`/`b`/`e` placeholder digests, and the file explicitly self-labels `claim_boundary: "sample_only_not_live_freeze_evidence"` | challenge: does this fixture's explicit self-labeled claim boundary make it definitionally safe to accept without further scrutiny; the self-label is exactly the discipline the doctrine sample asks for, so it is accepted as a positive worked example of claim-boundary hygiene (DOCTRINE_ADAPTED/ENRICH_EXISTING) rather than being either uncritically absorbed as a runtime fixture or dismissed as NO_NEW_VALUE |

## Reconciliation

- manifest=336
- metadata_frozen=336
- sample=20
- semantic_unresolved=316
- declaration_occurrences=13
- missing_paths=0
- duplicate_paths=0

All 336 physical paths have exactly one metadata row. Exactly SAM-01 through
SAM-20 have complete semantic rows; the remaining 316 files carry
`metadataState=METADATA_FROZEN` only and no semantic disposition. All 13
hidden-clone declaration occurrences are enumerated with candidate-only
routing; none is described as terminally resolved.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | post-SOT3 operator-authored downstream copied-folder gap response |
| Upstream or source-mirror disposition | `LOCAL_OPERATOR_AUTHORED_INPUT_WITHOUT_UPSTREAM`; hidden clone is a declared dependency target, not source authority |
| Enumeration or manifest plan | T0A full physical 336-row metadata freeze using path, bytes, SHA-256, and ordinal aggregate |
| Per-file terminal-ledger plan | T0A metadata for 336 and semantic terminal decisions for exact 20; T0B retains remaining 316 |
| Owner or overlap route | sample rows route to current CVF owner, pending downstream owner, or explicit no-owner escalation |
| Value-disposition route | ABSORB, ADAPT, DEFER, REJECT, BLOCK, or NO_NEW_VALUE plus valueClass and adversarial review |
| Claim boundary | T0A partial evidence only; no source mutation, full absorption, runtime, or product claim |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | operator-named 336-file downstream copied folder |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | full 336 metadata freeze plus exact reviewer-stratified 20-file semantic sample |
| Blind-spot prevention action | preserved all 336 file identities, enumerated all 13 declarations separately without deduplication, retained T0B obligation explicitly, and adversarially challenged every DEFER/REJECT/NO_NEW_VALUE sample row above |
| Residual gap | 316 semantic rows and all 13 declarations' terminal provenance dispositions |
| Blind-spot verdict | PARTIAL_T0A_ACCEPTED_T0B_REQUIRED |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application` |
| Enumeration command | direct recursive hidden-inclusive filesystem enumeration; `rg -n --hidden --no-ignore -F ".Controlled-Vibe-Framework-CVF" .` for declaration search |
| Manifest artifact or inline manifest | this file, 336-row metadata table and Aggregate Receipt above |
| Processing ledger artifact or inline ledger | this file, 20-row Reviewer-Selected Semantic Calibration Sample table plus 13-row Complete Hidden-Clone Declaration Inventory table |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE; `metadataState=METADATA_FROZEN` is a separate objective field |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | see Overlap And Novelty Classification below and `docs/reference/sot_three_layer/README.md` |
| Unresolved items | 316 un-sampled semantic decisions and all 13 declarations' terminal provenance dispositions |
| Completion claim boundary | T0A partial calibration; no full external absorption completion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| 336-file metadata (all files) | reproducible corpus identity | DOCTRINE_ADAPTED | this T0A ledger | freeze and reviewer-verify; propagate semantic rubric in T0B | no runtime/package claim |
| SAM-01, SAM-02, SAM-03, SAM-04 doctrine sample | downstream lifecycle, architecture split, claim-boundary, and review/freeze doctrine | DOCTRINE_ADAPTED | `docs/reference/sot_three_layer/README.md` and CVF claim-boundary discipline | source-verify before T0B propagation | no CVF Core promotion |
| SAM-01 through SAM-04 doctrine sample, taken as a candidate downstream product lane | scoped downstream business lifecycle worth tracking as its own package candidate, not only doctrine | PACKAGE_CANDIDATE | pending downstream owner (`packages/application`, `packages/domain`) | calibrate package boundary before T0B; no package activation | no package activation |
| SAM-06 through SAM-10 provenance sample | hidden-clone manifest/binding/env/config coupling evidence, including three missing declared extension targets | RUNTIME_CANDIDATE | current owner or future T0B/T1 owner map | candidate route only; terminal missing-target/provenance decision in T0B | no binding validation, no dependency activation |
| SAM-11 through SAM-15 runtime-shaped sample | adapter/service decision-semantics gaps plus a separate middleware behavior-proof gap | RUNTIME_CANDIDATE | future T1/T2/T3 source-verified owner map | source-verify the decision matrix per accepted rebuttal R-03 and behavior-test SAM-15 per partially rejected R-04 | no behavior proof, no runtime execution |
| SAM-11 through SAM-15 adapter/service/middleware sample, taken as a direct-import candidate | locally-declared adapters/services are not yet cross-verified against current T8 contracts | REJECT_DIRECT_IMPORT | `EXTENSIONS/CVF_TRUTH_KERNEL`, `EXTENSIONS/CVF_TRUTH_FLOW` (current T8 contracts, not yet cross-verified) | do not import directly; T1/T2 must source-verify before any reuse | no import, no runtime execution |
| SAM-17, SAM-18, SAM-19 test/proof sample | test-naming versus actual assertion-strength evidence | CHECKER_CANDIDATE | future T3 evidence/test-quality owner | distinguish fixture-existence and mock-based checks from true behavior proof before any checker wiring | no test execution performed by this worker |
| SAM-17, SAM-18, SAM-19 test/proof sample, taken as a direct-import candidate | tests assert against local mocks or bare fixture existence, not the current CVF contract | REJECT_DIRECT_IMPORT | future T3 test-quality repair lane | do not treat as behavior/binding proof; T1/T3 must replace with real assertions | no proof reuse, no test execution |
| SAM-16, SAM-20 evidence/fixture sample | freeze-package claim-boundary implementation pattern and worked schema example | DOCTRINE_ADAPTED | `docs/REVIEW_FREEZE_PROTOCOL.md` (SAM-04) | retain as bounded evidence; confirm no test currently asserts fixture values as live proof | no CVF Core promotion |
| SAM-05 TREEVIEW navigation sample | none found beyond duplicated directory listing | NO_PACKAGE_OR_RUNTIME_VALUE | this T0A ledger | retain terminal reason only; no further action | no package/runtime value claim |
| 13 hidden-clone declarations | provenance and authority coupling evidence; DEC-05/06/08 resolve to absent directories | RUNTIME_CANDIDATE | T0A/T0B provenance route | enumeration complete; terminally disposition missing and existing targets in T0B | no dependency activation, no version pin |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| SAM-01 through SAM-04 doctrine sample | `docs/reference/sot_three_layer/README.md` | ENRICH_EXISTING | application-level lifecycle/claim-boundary doctrine consistent with, not duplicating, existing three-layer doctrine | source-verify overlap detail in T1; no core doctrine copy |
| SAM-06 through SAM-10 provenance sample | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | unratified hidden-clone dependency/version coupling; three declared extension targets are absent from the literal hidden clone | record missing-target evidence and terminal provenance disposition in T0B; no owner promotion here |
| SAM-11, SAM-12 (Kernel/Flow adapters) | `EXTENSIONS/CVF_TRUTH_KERNEL`; `EXTENSIONS/CVF_TRUTH_FLOW` | REJECT_DIRECT_IMPORT | locally-declared adapter ports/interfaces are not cross-verified against current contracts; SAM-12 preserves the systemic BLOCK-only semantics gap under accepted-with-narrowing rebuttal R-03 | record incompatibility/verification-gap candidate; no import; re-examine in T1 with an explicit continuation matrix |
| SAM-13, SAM-14, SAM-15 (output/context/middleware) | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | possible new downstream sibling-product owner surface for `packages/application` and `apps/api`; SAM-15 is a behavior-proof gap, not proven 428 fall-through | keep pending T1 owner ratification; route SAM-15 negative request proof to T3; no owner promotion here |
| SAM-17, SAM-18, SAM-19 test/proof sample | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` (proof-quality discipline) | NO_NEW_VALUE candidate, adversarially reviewed | naming/assertion-strength gap (test name implies stronger proof than assertions deliver) is itself a negative-proof finding worth a T3 test-quality repair lane, not zero value | route to future T3 test-quality evidence lane; no checker wiring in T0A |
| SAM-05 TREEVIEW navigation sample | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | NO_NEW_VALUE | pure directory-tree duplication of information already present in the 336-row metadata table and ARCHITECTURE.md | terminal reason only; no further action |

## Reverse Architecture Projection Matrix

| Accepted value group | Catalog/GAP owner check | Disposition before T0A closure | Target source | Claim class | Evidence |
|---|---|---|---|---|---|
| downstream SOT product owner (README/ARCHITECTURE doctrine sample) | current as-built catalog | DEFER_PENDING_ACCEPTANCE | future existing entity update or proposed GAP | product candidate | SAM-01, SAM-02 plus T1 owner map required |
| application integration risks (SAM-11 through SAM-15) | current runtime owners and GAP registry | DEFER_PENDING_ACCEPTANCE | future owner update or GAP; distinguish R-03 decision semantics from R-04 middleware behavior proof | runtime candidate | source text only; no behavior proof |
| control-boundary doctrine | accepted FSCB crosswalk | NOT_APPLICABLE_WITH_REASON: T0A processes SOT-Application only; Four-Surface root is out of this packet's scope | separate FSCB owner surface already exists | doctrine evidence only | no Four-Surface mutation in T0A |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | operator intent -> intake review -> scope split -> T0A metadata/sample calibration -> reviewer checkpoint -> fresh T0B decision |
| Matching local-view guard | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | SOT3-APP roadmap and the paired T0A dispatch packet |
| Disposition | ADAPT metadata and sample evidence only |
| Claim boundary | no full absorption, runtime, public, or product completion |

This tranche processes an external repo or copied folder (the SOT-Application source root); it is not routed as an operator-provided external comparison, critique, or recommendation.

## Corpus Completeness And Report Integrity

- Corpus task class: downstream SOT application intake calibration.
- Corpus root: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.
- Snapshot time: 2026-07-16 worker execution start.
- Enumeration command: direct recursive hidden-inclusive filesystem walk plus per-file byte/hash reads, ordinal normalized-path aggregate, and `rg -n --hidden --no-ignore -F ".Controlled-Vibe-Framework-CVF" .` fixed-string declaration search.
- Manifest artifact or inline manifest: 336-row metadata table and Aggregate Receipt in this file.
- Manifest hash: `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee`.
- Processing ledger artifact or inline ledger: exact 20-row semantic table and 13-row declaration inventory in this file.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=336; ledger_terminal=20; metadata_frozen=336; semantic_sample_terminal=20; unresolved=316; declaration_occurrences=13; exclusions=0.
- Unresolved files: 316 semantic dispositions remain T0B-owned.
- Declared exclusions: none from metadata; 316 files are intentionally outside T0A semantic sampling and remain enumerated in the metadata table.
- Unreadable or unsupported files: zero; every one of the 336 files plus all 20 sample files was read successfully.
- Aggregation check: file_count=336; total_bytes=238522; aggregate matches; missing_paths=0; duplicate_paths=0.
- Drift check: reviewer confirmed zero drift in the fixed dispatch anchors (corpus, sample hashes, declaration count, hidden-target HEAD/remote/cleanliness) and separately corrected three declaration rows whose literal extension targets are absent.
- Output traceability: every physical file maps to one metadata row; each sample row maps to path, hash, decision, and reason; each declaration row maps to path, line, and candidate routing.
- Adversarial verification: this worker adversarially challenged every DEFER, REJECT, and NO_NEW_VALUE sample result inline (see adversarialChallenge column); independent reviewer/closer must re-audit all 20 rows per the work order's Review Gate.
- Corpus verdict: PARTIAL

## Epistemic Process Block

Expected Result / Prediction: the source preserves useful downstream
lifecycle intent but mixes doctrine, copied contracts, runtime-shaped code,
fixtures, tests, and hidden-clone coupling that require owner-aware semantic
calibration.

Evidence Comparison: T0A compared that prediction against all 336 objective
file identities, all 13 current declaration occurrences, and the exact
reviewer-selected 20-file cross-family sample. The prediction held: doctrine
files (SAM-01 through SAM-04) carry enrichable lifecycle claims, provenance
files (SAM-06 through SAM-10) carry unversioned hidden-clone coupling, and
runtime-shaped files (SAM-11 through SAM-14) carry a repeated BLOCK-only
decision-semantics gap, while SAM-15 carries a separate negative-test proof
obligation; neither grouping proves runtime behavior in T0A.

Contradiction Or Gap Disposition: no contradiction was found between the
predicted mixed-value corpus and the observed sample. Test-quality files
(SAM-17 through SAM-19) revealed a specific gap not fully anticipated in the
prediction: test/describe-block naming implies stronger behavioral proof
than the assertions actually deliver, which is recorded as a distinct
test-quality finding rather than folded into the runtime-risk group.

Claim Update: T0A calibrates a rubric and identifies candidate owner routes
for the 20-file sample. Only independent review may accept this rubric for
fresh T0B packet authoring and full-corpus semantic propagation.

## Finding-To-Governance Learning Disposition

No new repeated, non-obvious dispatch or gate defect was discovered during
this execution; the work order's pre-flight checks, sample hashes, and
declaration-count baseline all reproduced exactly on first attempt. The
reviewer/closer independently separated the systemic decision-semantics gap
across SAM-12/SAM-13/SAM-14 from SAM-15's middleware behavior-proof gap. Both
are already governed by the integrated intake review and rebuttal; neither is
a new governance-learning event in this tranche.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| applicability | NOT_APPLICABLE_WITH_REASON |
| reason | T0A creates two governed markdown evidence files only and does not create or alter application/runtime storage, cache, index, database, source mirror, or generated aggregate layout |
| owner boundary | existing `docs/reviews/` governed artifact family |
| future trigger | any later durable application storage or source-mirror proposal requires fresh GC-018 and source verification |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private copied-folder source-intake worker output; no public-sync
authorization or public-safe artifact set exists for this tranche.

## Claim Boundary

This ledger provides objective metadata for all 336 SOT-Application source
files, a complete inventory of all 13 current hidden-clone declaration
occurrences with candidate-only routing, and semantic calibration for
exactly the 20 reviewer-selected sample files. It does not provide semantic
disposition for the remaining 316 files, terminal provenance disposition for
any hidden-clone declaration, T0B release, source or hidden-clone mutation,
dependency install/sync, binding validation, build, typecheck, test, CI,
runtime, API, server, browser, provider/live proof, Catalog/GAP/ADIF/session
or checker mutation, package activation, CVF Core promotion, public-sync,
full absorption, production readiness, or user-value claims.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: this is a first-attempt T0A ledger authored against a freshly
  committed dispatch packet with no prior T0A ledger, sample, or worker
  return to compare against; the paired worker return's negative-search
  command confirmed zero pre-existing worker-return or completion path for
  this batch, so there is no predecessor artifact to build a delta ledger,
  routing matrix, or semantic-sampling comparison against.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `## Source Intake Decision Packet`; `## External Absorption Core`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## External Knowledge Intake Routing`; `## Corpus Completeness And Report Integrity`; required field names for each section; `Status: COMPLETE_PENDING_REVIEW`; `Self-declared worker-return artifact: yes`; `Responds to work order:`; `dispatchWorkOrder:`; `WORKER_MUST_NOT_COMMIT honored` |
| gateRunPurpose | confirm exact governed-artifact shape after checker-source review before writing; gates provide confirming proof, run after requirements were already read |
| claimBoundary | checker conformance does not prove corpus semantics, provenance safety, runtime behavior, or product quality |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated source-intake worker |
| Provider or surface | local private provenance repository |
| Session or invocation | SOT3-APP-T0A worker execution, 2026-07-16 |
| Working directory | repository root |
| Command or tool surface | governed reads, direct filesystem enumeration/hashing (Python), `rg` fixed-string search, read-only hidden-target Git metadata, governance gates |
| Target paths | this ledger and the paired worker return under `docs/reviews/` |
| Allowed scope source | committed T0A work order and paired GC-018 at `executionBaseHead=120c0f90a` |
| Before status evidence | clean `git status --short` at `120c0f90a`; both output paths absent |
| After status evidence | exactly two new untracked files; no other path changed; source and hidden-clone roots untouched |
| Diff evidence | `git diff --name-status` (empty, no tracked-file changes); `git status --short` (two untracked additions) |
| Approval boundary | T0A metadata freeze, declaration inventory, and 20-file semantic calibration only; no T0B, mutation, or runtime action |
| Claim boundary | source freeze and bounded sample calibration evidence only; no runtime, provenance-acceptance, or product proof |
| Agent type | delegated worker |
| Invocation ID | `sot3-app-t0a-worker-2026-07-16` |
| Expected manifest | this ledger; paired worker return |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | SOT3-APP-T0A documentation-only metadata/declaration/sample ledger |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no application/runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no application/runtime action is executed or observed |
| invocationBoundary | manual filesystem reads, hashing, parsing, read-only Git metadata, and governance checks only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, binding resolution, or agent coding control |
| claimLanguage | objective source identity and bounded semantic-calibration evidence only |
| forbiddenExpansion | runtime/provider/live/public/package/Web/MCP/checker behavior requires fresh source-verified authorization |

## git status --short

Before first write (captured at pre-flight, `executionBaseHead=120c0f90a`):

```text
(clean)
```

After both outputs created (current):

```text
?? docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md
?? docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md
```

## Changed Files

- `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md` (created)
- `docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md` (created)

No other file was created, modified, or deleted. No source, hidden-clone,
application, runtime, session, checker, or public-sync path was touched.

## Command Evidence

| Command | Result |
|---|---|
| `git rev-parse --short HEAD` | `120c0f90a` - PASS |
| direct recursive filesystem enumeration of source root (336 files) | 336 files, 238522 bytes - PASS |
| per-file SHA-256 plus ordinal aggregate | `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee` - PASS (MATCH) |
| per-file SHA-256 recomputation for SAM-01 through SAM-20 | 20/20 MATCH - PASS |
| `rg -n --hidden --no-ignore -F ".Controlled-Vibe-Framework-CVF" .` in source root | 13 occurrence lines - PASS (MATCH) |
| hidden-target `git rev-parse`/`status --short --branch`/`remote -v` | HEAD `a78b35c`, clean, `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` - PASS (MATCH) |

Full command evidence, including negative-search and governance-gate
results, is recorded in the paired worker return.

## No-Commit Statement

`WORKER_MUST_NOT_COMMIT honored`. This worker created exactly two untracked
files and ran zero `git add`, `git commit`, `git push`, or history-mutating
command. The worktree remains uncommitted for independent reviewer/closer
acceptance.

WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond normal gates; no gate surprise, no helper gap, no worktree contamination this return
