# NCR C1 E1 Metadata Result
Memory class: FULL_RECORD
docType: reference
Status: E1_FINISHED_PARTIAL_WITH_DECLARED_LIMITS
Date: 2026-10-08
Batch ID: CVF-NCR-C1-OFFLINE-PRODUCTION-READINESS-20261008
executionBaseHead: 6e1302dbf410373262573b1b2363a51bfdb356d4

## Purpose

Return the one admitted bounded E1 metadata attempt, source deltas and a joined residual manifest decision. Attempt finished at the request cap; source intake is partial. No request-cap increase or rerun.

## Scope / Applies To

Local INTERNAL_AGENT direct executor and self-checker; no delegated worker or independent review claim. Operator approval is bound in `docs/reference/CVF_NCR_C1_E1_EXECUTION_CONTRACT_2026-10-08.json`; admission in `docs/baselines/CVF_GC018_NCR_C1_E1_METADATA_ADMISSION_2026-10-08.md`. Companion `docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.json` retains exact160 response identities, four unrequested rows,78 wheel metadata comparisons,57 npm response rows, collector bytes and pre-execution baseline snapshot. Production, supervisor and S1-S9 remain held.

## Outcome And Budget

| Measure | Observed | Ceiling or disposition |
|---|---|---|
| request count | 160 | 160; stopped before URL161 |
| response body bytes received/retained | 2939306 | 16777216 B for each body total |
| elapsed wall seconds | 66.531 | 1200 s |
| largest request seconds | 0.797 | 15 s |
| HTTP status | 145x200;1x404;14x405 | all retained bodies hash-checked; negative responses not absence proof |
| queued URLs / unrequested | 164 /4 | tzdata2025.2,urllib3 2.5.0,uvicorn0.38.0,websockets15.0.1 |
| retries / redirects followed / credentials | 0 /0 /none | no ambient proxy or provider invocation |

Gate history: two pre-implementation FAILs from incomplete ADIF disclosure grammar, corrected offline; final full pre-implementation PASS before the first HTTP request. Logs retained in the existing ignored review directory. No effect executed while gate failed. Current source-ledger self-check PASS; it is not an independent acceptance probe or network-monitoring proof.

## Source Deltas And Manifest Candidate

- Exact model revision61b85e3d937fbbacb387714180e8182823512523 and codec revisionceff0d0749bfb3fa2d61149794ec6feef0d1e1ae MATCH. Pinned model/codec card text is now retained; both metadata records declare apache-2.0. This supplies missing publisher text, not cleared consent or verified weight/codec rights.
- Four small-file metadata rows now have declared size and Git blob IDs; none supplies an acquired-payload SHA-256. OB-06 remains open. The model/card and codec/card raw response SHA values are in the immutable request ledger.
- HyperFrames selected commit5c52f72399e21f8dcf3ede2bf2d24978c6522a94 MATCH. Observed main4a335aa6a1daf7bea766d9bbacc0cb6d43b1ad46 differs. npm hyperframes0.8.113 declares gitHeadaca4bc2f492c2b038d87c875cd7d53a80dfb4bb1, two CLI bins and33408618 unpacked bytes. Source-to-package join remains unresolved; no silent repin or upgrade.
- 78 wheel exact-filename/declared-SHA comparisons MATCH; four rows were not queried. Every comparison remains metadata-only; no wheel acquired or installed. Licence classifiers are preserved as publisher declarations.
- 57 npm locator rows returned200;14 nested-lock locator strings produced405. The separate @hyperframes/cli seed produced404 while the hyperframes package declares its own CLI bin. This identifies a queue-construction defect: the approximate lock table was not a canonical package-name manifest. Local normalization candidates are recorded without requery; no resolver-validated closure is claimed.
- FFmpeg release discovery returned id405793771, rolling tag latest. No immutable asset/build selected or encoder executed. Browser binary terms, font hashes/coverage and licence/notice texts remain incomplete.

## Negative Endpoint Ledger

| Ordinal | Source label | HTTP | Disposition |
|---|---|---|---|
| 9 | separate CLI seed | 404 | negative endpoint evidence; no absence claim |
| 19 | @puppeteer/browsers/yargs | 405 | negative endpoint evidence; no absence claim |
| 20 | @puppeteer/browsers/yargs/cliui | 405 | negative endpoint evidence; no absence claim |
| 21 | @puppeteer/browsers/yargs/cliui/strip-ansi | 405 | negative endpoint evidence; no absence claim |
| 22 | @puppeteer/browsers/yargs/cliui/strip-ansi/ansi-regex | 405 | negative endpoint evidence; no absence claim |
| 23 | @puppeteer/browsers/yargs/cliui/wrap-ansi | 405 | negative endpoint evidence; no absence claim |
| 24 | @puppeteer/browsers/yargs/cliui/wrap-ansi/ansi-styles | 405 | negative endpoint evidence; no absence claim |
| 25 | @puppeteer/browsers/yargs/string-width | 405 | negative endpoint evidence; no absence claim |
| 26 | @puppeteer/browsers/yargs/string-width/emoji-regex | 405 | negative endpoint evidence; no absence claim |
| 27 | @puppeteer/browsers/yargs/string-width/strip-ansi | 405 | negative endpoint evidence; no absence claim |
| 28 | @puppeteer/browsers/yargs/string-width/strip-ansi/ansi-regex | 405 | negative endpoint evidence; no absence claim |
| 29 | @puppeteer/browsers/yargs/yargs-parser | 405 | negative endpoint evidence; no absence claim |
| 36 | chromium-bidi/zod | 405 | negative endpoint evidence; no absence claim |
| 69 | puppeteer-core/ws | 405 | negative endpoint evidence; no absence claim |
| 73 | sharp/semver | 405 | negative endpoint evidence; no absence claim |

These responses are evidence about the requested endpoint at the recorded time. They do not prove a package was removed or justify treating nested dependency paths as publisher package names. The collector intentionally retained404/405 response text and continued the finite queue; its request-failure stop means transport exceptions, while credential demand, redirects, content and budget violations also stop. This interpretation is visible in the pre-bound collector source; no retrospective rerun or rewriting of its contract/source occurred.

## Joined Obligation Disposition

All29 obligations stay OPEN. E1 added evidence to OB-05/06/09/10/11/17 but did not close their downstream rights, payload or execution prerequisites. OB-12/13 remain incomplete. OB-22 freeze and historical custody gap unchanged. P1/Hai Dang remain design assumptions; approval of E1 is not preset consent or native-control admission. Host/Docker remain REPORTED_UNBOUND until admitted S2 measurement. The two selected10GiB/8GiB limits are retained.

Next admitted independent work: one consolidated local manifest/control proposal using current metadata and the corrected locator interpretation; no new network request, helper-source/OS effect or payload acquisition inferred. Before S1, present exact helper paths and prospective OS proof scope for the explicit freeze-boundary disposition. Before S3, supply immutable manifest, rights and S2 proof. Hold dependent effects only, and do not ask again for the completed E1 envelope.

## Verification / Epistemic Process Block

Expected Result / Prediction: grouped public metadata can strengthen a concrete manifest under fixed cost without performing production effects.
Evidence Comparison: actual160 responses/2939306 B/66.531 s; exact-body SHA/byte joins and declared78 wheel identities checked;164 input URLs reconcile160 requested plus4 unread.
Contradiction or Gap Disposition: fourteen nested locators were incorrectly translated into registry names and the separate CLI seed failed; preserve original negatives and correct the local manifest interpretation, without spending another network attempt. Fresh producer head and package/source commit difference remain visible. Two local analysis-script assumptions (default encoding and JSON object shape) were corrected with UTF-8/type checks, no network replay.
Claim Update: finite E1 attempt completed with partial metadata,29 obligations open, nine production/source stages held. Nothing promoted to rights, payload, enforced controls or live CVF governance proof.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_epistemic_process_packet.py; governance/compat/check_adif_defect_registry_disclosure.py |
| literalTokensReviewed | reference; Purpose; Scope; Verification; Claim Boundary; ASCII; Expected Result/Evidence Comparison/Gap Disposition/Claim Update; exact trace paths |
| gateRunPurpose | confirm finite return and evidence structure, not independent acceptance |
| claimBoundary | public metadata observations only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local direct executor/steward |
| Provider or surface | private shared workspace and admitted public HTTP endpoints |
| Session or invocation | ncr-c1-e1-direct-local-20261008 |
| Working directory | repository root |
| Command or tool surface | SHA-bound collector, local JSON/hash analysis, finite documentary outputs and gates |
| Target paths | `docs/baselines/CVF_GC018_NCR_C1_E1_METADATA_ADMISSION_2026-10-08.md`; `docs/reference/CVF_NCR_C1_E1_EXECUTION_CONTRACT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.md` |
| Allowed scope source | explicit E1 operator approval and pre-gated baseline/command contract |
| Before status evidence | clean base 6e1302dbf410373262573b1b2363a51bfdb356d4; before network two admission files plus ignored collector |
| After status evidence | four governed paths; ignored attempt receipt and160 public body files; no model/package binary |
| Diff evidence | exact four-path Git status;160 body/hash/byte joins and receipt SHA in result JSON |
| Approval boundary | E1 only; future native/control/payload/media/public effects held |
| Claim boundary | no independent production acceptance or AI live-governance proof |
| Agent type | INTERNAL_AGENT single-role |
| Invocation ID | ncr-c1-e1-direct-local-20261008 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_C1_E1_METADATA_ADMISSION_2026-10-08.md`; `docs/reference/CVF_NCR_C1_E1_EXECUTION_CONTRACT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_C1_E1_METADATA_ADMISSION_2026-10-08.md`; `docs/reference/CVF_NCR_C1_E1_EXECUTION_CONTRACT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: new packet/result files only; no deletion |

## Corpus Completeness And Report Integrity

- Corpus root: immutable164-URL queue in bound command contract; excludes all repository/upstream payload corpora.
- Manifest artifact or inline manifest: docs/reference/CVF_NCR_C1_E1_EXECUTION_CONTRACT_2026-10-08.json,queueSha256 65fcae512af19178a51f0bbb49389dcd913f662f6c968a4a644f4b0d7e6d81b1.
- Processing ledger artifact or inline ledger: docs/reference/CVF_NCR_C1_E1_METADATA_RESULT_2026-10-08.json,receipt.rows and receipt.unrequestedRows.
- Reconciliation:164 planned =160 retained/processed request rows +4 unread at cap;145 positive +15 negative =160.
- Declared exclusions: payload binaries, full repositories, archive/install/licence semantic clearance.
- Unreadable or unsupported files: four not requested at cap; fifteen negative endpoints retained as text, not successful package metadata.
- Aggregation check: actual row counts/body SHA/bytes reconciled; no self-reported corpus total without ledger.
- Drift check: frozen contract queue/collector/source hashes retained; HTTP freshness applies only to recorded observation time.
- Corpus verdict: PARTIAL - bounded request manifest only, no repository-wide completeness.

## Knowledge System Reconciliation

NOT_APPLICABLE_WITH_REASON: metadata readiness evidence, no knowledge-map transformation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Public reads only; private governed result, no public write/export.

## Claim Boundary

E1_FINISHED_PARTIAL_WITH_DECLARED_LIMITS, not production closure. Runtime NO_GO, verified rights/consent/payload/enforced controls all0. No source helper, retry/reset, credential/provider, install, voice/render or public/deploy effect. S0 originals and historical STOP/custody/freeze unchanged. Current self-check never becomes an independent reviewer result.
