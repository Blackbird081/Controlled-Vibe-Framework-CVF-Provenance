# CVF ERH-RS1 External Review Full Coverage Rescan

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: assessment

Date: 2026-06-04

Worker: Claude

executionBaseHead: `b442085e`

dispatchPacketCommit: `b442085e`

closureBaseHead: `b442085e`

GC-018: `docs/baselines/CVF_GC018_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md`

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_FOR_CLAUDE_2026-06-04.md`

## Purpose

Perform a source-backed full-coverage rescan of the archived external
public-repo review Word document. Produce a section-level coverage ledger,
a finding disposition ledger, an explicit section 4.4 architectural weakness
table, and a safety-layer reassessment with ERH-SAF1 readiness recommendation.

This rescan is authoritative over the predecessor intake
(`CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md`), which is accepted as
predecessor evidence only and not as completeness proof.

## Decision / Baseline / Proposed Tranche

Decision: `COMPLETE_VERIFIED` source rescan with `ERH-SAF1_READY` safety
reassessment recommendation.

Baseline:

- DOCX extracted from SHA256-verified archived source path; hash matches GC-018
  authorized digest.
- All 162 non-empty paragraphs processed across 22 document sections.
- All 17 distilled findings disposed against current ERH tranche outputs.
- Section 4.4 all five mandatory architectural weakness rows covered.
- Safety layer gap confirmed: `safety-status.ts` richer patterns not wired to
  execute route; `safety.ts` (4 patterns) is the only execute-chain safety check.

Proposed tranche: **ERH-SAF1** — wire severity-classified safety patterns into
the `/api/execute` safety chain with audit event. Readiness rules all pass.
Requires a new GC-018 and work order before implementation.

## Source Corpus

| Item | Value |
| --- | --- |
| Source path | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` |
| SHA256 | `1C52C011A2D11922C5A5712FF785435474AB772B6F9C0A42563D177B1F255A10` |
| GC-018 authorized digest | `1C52C011A2D11922C5A5712FF785435474AB772B6F9C0A42563D177B1F255A10` |
| Hash match | PASS — runtime digest matches GC-018 authorized digest |
| Extraction tool | python-docx (`python -c "import docx; ..."`) |
| Extraction encoding | UTF-8 (`sys.stdout.reconfigure(encoding='utf-8')`) |
| Extraction timestamp | 2026-06-04 (session execution) |
| Non-empty paragraphs extracted | 162 |
| Document language | Vietnamese (original review authored in Vietnamese) |
| Extraction completeness | ALL 162 non-empty paragraphs read and processed |

Extracted text artifact: inline within this RS1 assessment (section coverage
ledger and finding disposition ledger trace every paragraph to its section).

## Corpus Completeness And Report Integrity

- Corpus task class: EXTRACTION
- Corpus root: `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx`
- Snapshot time: 2026-06-04 session execution
- Enumeration command: `Get-FileHash -Path docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx -Algorithm SHA256` (single-file corpus; hash is the filesystem-backed manifest; paragraph enumeration via python-docx applied to the hash-verified file)
- Manifest artifact or inline manifest: inline — 1 source file verified by SHA256; 162 non-empty paragraphs extracted; indices [0]–[161] mapped to Section Coverage Ledger
- Manifest hash: `1C52C011A2D11922C5A5712FF785435474AB772B6F9C0A42563D177B1F255A10` (SHA256 of source DOCX — matches GC-018 authorized digest)
- Processing ledger artifact or inline ledger: inline — Section Coverage Ledger maps all 22 document sections (162 paragraphs); Finding Disposition Ledger maps all 17 distilled findings; all paragraphs status READ
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=1 file (162 paragraphs); ledger_terminal=162; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: PASS — 162 paragraphs enumerated = 162 paragraphs processed; 0 gap
- Drift check: PASS — SHA256 runtime hash matches GC-018 authorized digest exactly
- Output traceability: paragraph indices [0]–[161] directly cited in Section Coverage Ledger by para range; all 17 findings in Finding Disposition Ledger traced to §ref
- Adversarial verification: GC-018 SHA256 pre-verified before extraction; hash recheck available via `Get-FileHash -Algorithm SHA256`; python-docx is an established local DOCX parser; no external network call during extraction
- Corpus verdict: COMPLETE_VERIFIED

Zero unresolved paragraphs. Zero extraction gaps. Hash match confirmed.

## Section Coverage Ledger

Document structure mapped from TOC (paragraphs [4]–[34]) and body content.

| Section label | Para range | Coverage disposition | Notes |
| --- | --- | --- | --- |
| Title / header | [0]–[3] | `captured` | Title, framework name, scope note, confidentiality note |
| TOC | [4]–[34] | `captured` | Table of contents entries — cross-referenced to body sections |
| §1 Tóm tắt điều hành (Executive Summary) | [35]–[45] | `captured` | 6 key findings + summary scorecard paragraph |
| §2 CVF là gì (Technical Definition) | [46]–[51] | `captured` | 3 core modules, philosophy statement |
| §3 Phạm vi & phương pháp (Scope & Method) | [52]–[54] | `captured` | 4 parallel survey streams, evaluation limits |
| §4.1 Pipeline thực thi (Execution Pipeline) | [55]–[59] | `captured` | Sequential pipeline description, early-return design |
| §4.2 Module authenticity table | [60] | `captured` | Section header only — table content rendered as single paragraph |
| §4.3 Architectural strengths | [61]–[65] | `captured` | 4 strength points: layering, mandatory guard, factory pattern, graceful degradation |
| §4.4 Architectural weaknesses | [66]–[72] | `captured` | 5 weakness points + code quality note — **mandatory detailed coverage below** |
| §5.1 Three governance layers | [73]–[77] | `captured` | L1 runtime guards, L2 contracts, L3 CI/repo gates |
| §5.2 Release gate behavior | [78] | `captured` | 7-step release gate script description |
| §5.3 Evidence mechanism problems | [79]–[85] | `captured` | 5 evidence-integrity concerns |
| §6.1 CI/CD | [86]–[88] | `captured` | cvf-ci.yml structure, concurrency, npm ci |
| §6.2 Testing & maturity | [89]–[93] | `captured` | Unit/E2E tests, version inflation, CHANGELOG quality, AI transparency |
| §6.3 Security & hygiene | [94]–[97] | `captured` | Strengths, next-auth beta, license note |
| §7 Benchmark QBS (full section) | [98]–[115] | `captured` | Method (§7.1), results (§7.2), limitations (§7.3) |
| §8 Documentation | [116]–[120] | `captured` | Scale, strengths, weaknesses, installation |
| §9 Summary strengths & weaknesses | [121]–[134] | `captured` | §9.1 real strengths (5 items), §9.2 real weaknesses (6 items) |
| §10 Recommendations | [135]–[146] | `captured` | 5 develop recommendations + 2 adoption considerations + license note |
| §11.1 Key evidence citations | [147]–[152] | `captured` | 4 quoted evidence items with source paths |
| §11.2 Method notes & limits | [153]–[156] | `captured` | Self-reported figures caveat, ai.ts note, snapshot date |
| §11.3 Sources | [157]–[161] | `captured` | Repo, source code, evidence, CI/scripts |

**Verdict: all 22 document sections captured. Zero missed. Zero deferred without reason.**

## Finding Disposition Ledger

Cross-referencing DOCX findings against predecessor intake (ERH-F1–F11) and
current ERH tranche outputs.

| ID | DOCX finding (§ref) | Intake ID | Current disposition | Artifact / evidence | Follow-up candidate |
| --- | --- | --- | --- | --- | --- |
| RS-01 | Ephemeral audit storage: control-plane events default to OS tmp dir (§4.4, §9.2, §10.2) | ERH-F1 | `BOUNDED_DOCS_ONLY` — T3 evidence durability boundary document describes the tmp/optional-signing split; durable backend remains deferred runtime roadmap | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | ERH-SAF1 audit event for safety block (see SAF1 section) |
| RS-02 | In-memory rate limiter not suitable for multi-instance deployment (§4.4, §9.2, §10.5) | ERH-F5 | `BOUNDED_DOCS_ONLY` — T3 boundary acknowledges rate-limit gap; Redis adapter deferred | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | separate runtime rate-limit work order if multi-instance deployment authorized |
| RS-03 | Safety layer too thin; lacks advanced jailbreak detection (§4.4, §6.3 implicit, §9.2) | ERH-F6 | `CLAIM_CALIBRATED_ONLY` — ERH-T1A bounded the public claim; no workflow-chain or runtime hardening performed | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | **ERH-SAF1** — see Safety Layer Reassessment |
| RS-04 | policySnapshotId is a simulated identifier; cannot reconstruct policy at request time (§4.4, §9.2) | ERH-F7 | `BOUNDED_DOCS_ONLY` — T3 boundary names this gap; runtime persisted policy versioning deferred | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | separate policy-snapshot runtime work order |
| RS-05 | Provider risk ceilings hardcoded in source code (§4.4) | ERH-F8 partial | `SOURCE_VERIFIED_OPEN` — GC-018 source verification confirms `WEB_PROVIDER_DEFINITIONS` static maxRiskLevel values; no runtime configuration load implemented | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts` lines 70–119 | provider risk configuration work order (separate) |
| RS-06 | Receipts not cryptographically signed; can be manually edited (§5.3) | ERH-F1 / ERH-F2 | `BOUNDED_DOCS_ONLY` — T3 boundary acknowledges optional signing; no crypto signing implemented | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | evidence signing roadmap |
| RS-07 | liveEmissionWired = false; governed without a trace (§5.3) | ERH-F8 | `SOURCE_VERIFIED_OPEN` — `OPERATIONAL_BENCHMARK_EXTENSIONS` contract literal `liveEmissionWired: false` confirmed in intake; not changed | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` lines 90, 206–226 | benchmark emission wiring roadmap |
| RS-08 | Route governance coverage not complete (§5.3) | ERH-F3 | `CLOSED_BOUNDED` — ERH-T2A route governance coverage ledger created; 68 route files, lexical coverage 47/68; claim bounded | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | deeper semantic per-route proof roadmap |
| RS-09 | All self-certification; no independent validator (§5.3, §7.3) | ERH-F1 partial | `DOCUMENTED_OPEN` — T1A claim calibration acknowledges; independent validation is a strategic decision outside ERH roadmap scope | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | N/A — operator strategic decision |
| RS-10 | Main CI lacks lint, coverage threshold, npm audit gates (§6.1, §9.2, §10.4) | ERH-F4 | `PARTIAL_CLOSED` — ERH-AUD1 added npm audit remediation + workflow-chain checker; lint/coverage thresholds not added | `docs/reviews/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_COMPLETION_2026-06-04.md` | ERH-CI hardening for lint/coverage gate (ERH-T2B superseded by ERH-CI1) |
| RS-11 | next-auth beta in production (§6.3, §9.2, §10.5) | ERH-F9 | `CLOSED_BOUNDED` — ERH-DEP1 decision `ACCEPT_WITH_CAVEAT`; ERH-T4 baseline; no stable v5; downgrade API-incompatible | `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | DEP2 next-major migration if operator authorizes |
| RS-12 | Output-quality parity not proven; "output-quality tax" acknowledged (§7.2, §9.2, §10.3) | ERH-F10 | `CLOSED_BOUNDED` — ERH-T1A claim calibration addresses; public README updated to frame CVF as governance/control/safety value, not output-quality superiority | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | EVT-4 weak-lane improvement (separate benchmark roadmap) |
| RS-13 | Public README/catalog does not guide external agents to correct evaluation boundary (§10, §8) | ERH-F11 | `CLOSED_BOUNDED` — ERH-T1C public-sync claim boundary prep + public summary export at commit `73f1da98` | `docs/reference/CVF_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_2026-06-04.md` | follow-up public eval guide if broader adoption desired |
| RS-14 | Documentation bloat and version inflation (§8, §9.2) | N/A in intake | `DOCUMENTED_OPEN` — strategic documentation cleanup not in ERH roadmap scope; acknowledged | N/A | operator-scoped doc cleanup |
| RS-15 | CC BY-NC-ND license blocks commercial use (§6.3, §10) | N/A in intake | `OUT_OF_SCOPE` — license is an operator strategic decision; not a technical hardening gap | N/A | operator decision |
| RS-16 | QBS scoring never passed; reviewer κ threshold not met (§7.2, §7.3) | ERH-F10 partial | `DOCUMENTED_OPEN` — EVT-4 weak-lane investigation is a separate benchmark roadmap item; ERH does not cover benchmark quality | N/A | separate benchmark roadmap |
| RS-17 | AGENT_HANDOFF.md visible despite gitignore (§6.3) | N/A in intake | `RESOLVED_BY_DESIGN` — AGENT_HANDOFF files are gitignored in public-sync clone; the listing was from private repo; public-sync exclusion rule enforced | `public-sync .gitignore` and CLAUDE.md public-sync rule | N/A |

**Verdict: all 17 distilled findings have a disposition. Zero missed.**

## Section 4.4 Architectural Weaknesses

Full coverage of all five mandatory DOCX §4.4 concerns plus code-quality note.

| §4.4 concern | DOCX text (para) | Current source state | Disposition | Follow-up |
| --- | --- | --- | --- | --- |
| **Ephemeral audit (tmp JSON)** | [67] "Lưu trữ kiểm toán dạng ephemeral (file JSON trong thư mục tạm hệ điều hành) mâu thuẫn với chính tuyên bố 'evidence-based governance'; chưa có backend cơ sở dữ liệu mặc định hay lộ trình migration rõ." | `CVF_CONTROL_PLANE_EVENTS_PATH` resolver confirmed still uses OS tmp by default (intake line 45); guard-contract SQLite wrapper exists as partial mitigation (`sqlite-db.ts`) | `DEFERRED_RUNTIME_ROADMAP` — T3 boundary document names this gap; no durable backend wired as default | Open separate audit-persistence work order with operator auth |
| **In-memory rate limiter** | [68] "Rate-limiter in-memory không phù hợp triển khai nhiều instance (không có Redis adapter)." | `rate-limit.ts` lines 6–7 confirmed `buckets` / `providerBuckets` in-memory Maps (intake line 48) | `DEFERRED_RUNTIME_ROADMAP` — T3 boundary document names this gap; Redis adapter not implemented | Open separate rate-limit work order if multi-instance deployment authorized |
| **Safety layer too thin / lacks advanced jailbreak detection** | [69] "Lớp an toàn (safety) quá mỏng so với cách tài liệu mô tả; thiếu phát hiện jailbreak nâng cao." | `safety.ts`: 4 INJECTION_PATTERNS + 4 PII_PATTERNS (35 lines). `safety-status.ts`: richer sanitizePrompt with 11 severity-classified patterns (CRITICAL/HIGH/MEDIUM). BUT `safety-status.ts` is `'use client'` — NOT in the execute-route safety chain. Execute route calls `applySafetyFilters` from `safety.ts` only (route.ts line 260). | **`ERH-SAF1_READY`** — see Safety Layer Reassessment below | ERH-SAF1: wire `sanitizePrompt` (safety-status.ts) or a governed equivalent into the execute-route safety chain with audit event |
| **policySnapshotId not durable** | [70] "policySnapshotId là định danh giả lập, không cho phép tái dựng policy tại thời điểm request → suy giảm khả năng audit lại." | `web-governance-envelope.ts` lines 42–47 `generatePolicySnapshotId` confirmed process-lifetime style (intake line 50) | `DEFERRED_RUNTIME_ROADMAP` — T3 boundary document names this gap; persisted policy versioning not implemented | Open separate policy-snapshot work order |
| **Provider risk ceilings hardcoded** | [71] "Trần rủi ro của provider được hardcode trong code, không nạp từ cấu hình." | `WEB_PROVIDER_DEFINITIONS` in `provider-router-adapter.ts` lines 70–119 confirmed static `maxRiskLevel` values: openai R2, claude R2, gemini R2, alibaba R1, openrouter R1, deepseek R1 (GC-018 source verification) | `OPEN_SOURCE_VERIFIED` — no configuration-driven risk ceiling load implemented | Open separate provider-risk-configuration work order |
| **Code quality note** | [72] "Chất lượng code tốt... Có một ít trùng lặp (chuẩn hóa risk-level xuất hiện ở hai nơi với khác biệt nhỏ). Không phát hiện lỗi logic nghiêm trọng." | Positive assessment. Risk-level normalization duplication is minor; no blocking defect. | `ACKNOWLEDGED_MINOR` — positive finding; duplication is within acceptable bounds | N/A |

## Safety Layer Reassessment

### Why Prior ERH Only Calibrated Claims

Prior ERH safety treatment (ERH-F6 → ERH-T1A) was docs-only claim calibration
because:

1. **Scope of T1A**: ERH-T1A was a public claim calibration tranche — its only
   authorized output was a reference document adjusting public wording. It was
   not authorized to implement runtime changes.
2. **No source verification at that time**: the initial intake noted the safety
   concern but did not verify the full gap between `safety.ts` (execute-route
   chain) and `safety-status.ts` (`use client` — not in execute chain).
3. **Governance sequencing**: runtime implementation requires a separate
   authorized work order; claim calibration was the correct first step before
   knowing whether the foundation was sufficient.

### Current DLP/Safety Foundation Facts (Source-Verified)

| Artifact | Path | Lines | Role in execute chain | In execute route? |
| --- | --- | --- | --- | --- |
| `safety.ts` | `src/lib/safety.ts` | 35 | 4 INJECTION_PATTERNS + 4 PII_PATTERNS; `applySafetyFilters` returns `{blocked, reason, details}` | **YES** — called at route.ts line 260 |
| `safety-status.ts` | `src/lib/safety-status.ts` | ~220 | `sanitizePrompt` with 11 severity-classified patterns (CRITICAL/HIGH/MEDIUM/LOG); `isInputDangerous`; entropy guard; policy engine | **NO** — marked `'use client'`; UI-only helper |
| `dlp-filter.ts` | `src/lib/dlp-filter.ts` | short | `applyDLPFilter` entry point; uses active policy patterns | **YES** — called at route.ts line 240 (before safety) |
| `dlp-filter-core.ts` | `src/lib/dlp-filter-core.ts` | 24–190 | `PRESET_PATTERNS`, `applyDLPPatterns`; full pattern engine | **YES** — used by dlp-filter.ts |

**Key gap confirmed**: the richer severity-classified injection patterns in
`safety-status.ts` (CRITICAL: governance-disable, policy-override, bypass-attempt,
unrestricted-mode, instruction-override; HIGH: risk-manipulation, role-injection,
system-prompt-injection) are NOT wired into the execute-route safety chain. The
execute route only has the 4-pattern `safety.ts` check.

**Execute-route safety chain call order** (route.ts lines 240–272):
1. `applyDLPFilter` (DLP redaction, audit event if redacted)
2. `applySafetyFilters` from `safety.ts` (4 injection + 4 PII patterns)
3. Return 400 if blocked

`sanitizePrompt` from `safety-status.ts` is not called in this chain.

### ERH-SAF1 Readiness Assessment

Applying work order section 9 rules:

| Rule | Evaluation | Met? |
| --- | --- | --- |
| `/api/execute` has a safety entry point | Confirmed — `applySafetyFilters` at route.ts line 260 | **YES** |
| DLP/safety artifacts exist that can be chained without ML/classifier claims | Confirmed — `sanitizePrompt` in `safety-status.ts` is a deterministic regex/severity engine with no ML/classifier dependency | **YES** |
| SAF1 scope can be deterministic and testable without live provider proof | Yes — wiring `sanitizePrompt` into execute route is a source-only change; deterministic regex; testable with unit tests | **YES** |
| SAF1 can include audit/readout evidence for safety block or escalation | Yes — `appendAuditEvent` infrastructure already used for DLP; same pattern can record safety severity level | **YES** |
| Runtime file-size and route-size constraints can be respected | execute route.ts is ~861 lines (hard limit 1000); safety.ts is 35 lines; wiring can be done without large additions to route.ts — call can be delegated to a small safety-chain helper | **YES — with care** (route.ts is 139 lines from limit; SAF1 must route through a helper, not inline to route.ts) |

**ERH-SAF1 Recommendation: `ERH-SAF1_READY`**

All five readiness rules are satisfied. The safety foundation gap is clearly
scoped: wire the existing `sanitizePrompt` (or a governed subset of its patterns)
from `safety-status.ts` into the execute-route safety chain, with an audit event
that records severity level. This is deterministic, testable, and bounded.

### Proposed ERH-SAF1 Scope (Docs-Only Planning — No Runtime Implementation Here)

| SAF1 component | Proposal | Constraint |
| --- | --- | --- |
| Safety chain extension | wire `sanitizePrompt` from `safety-status.ts` (or extract severity-classified patterns into a shared `safety-chain.ts` helper) into execute route before `applySafetyFilters` call | must not exceed route.ts line limit; extract to helper |
| Audit event for safety severity | add `appendAuditEvent` call with `eventType: 'SAFETY_BLOCK_WITH_SEVERITY'` and severity level from `sanitizePrompt` result | reuse existing audit infrastructure |
| Claim boundary | SAF1 is deterministic pattern hardening only; no ML, no classifier, no "advanced AI jailbreak detection" claim | claim boundary must be explicit in SAF1 review |
| Test coverage | unit test for each CRITICAL/HIGH pattern in the execute-route chain; test that audit event is emitted on block | Vitest |
| File-size check | pre-flight: check route.ts and any new helper file against GC-023 thresholds | mandatory before SAF1 implementation |

### What SAF1 Would NOT Claim

- No ML-based jailbreak detection.
- No "advanced safety layer" claim.
- No guarantee of catching all adversarial prompts.
- No production-security hardening certification.
- No complete remediation of the §4.4 safety weakness.

SAF1 would correctly claim: deterministic severity-classified pattern coverage
expanded from 4 patterns to ~11 patterns in the execute-route safety chain, with
audit event evidence per block.

## Workflow Chain Candidates

Prioritized follow-up candidates from this RS1 rescan:

| Priority | Candidate | Basis | Readiness | Blocker |
| --- | --- | --- | --- | --- |
| 1 | **ERH-SAF1**: wire severity-classified safety chain into execute route + audit event | RS-03 / §4.4 safety gap; readiness rules all pass | `ERH-SAF1_READY` | Requires new GC-018 and work order; WORKER_MUST_NOT_COMMIT |
| 2 | **Provider risk configuration**: load `maxRiskLevel` from configuration instead of hardcode | RS-05 / §4.4 | `READY_WITH_DESIGN` | design decision on config source (env var / policy doc / DB); separate work order |
| 3 | **Audit persistence**: wire durable audit backend (SQLite or Postgres) as default | RS-01 / §4.4; §10.2 | `DESIGN_REQUIRED` | storage backend selection; separate operator authorization |
| 4 | **policySnapshotId persistence**: store policy state at request time | RS-04 / §4.4; §10 | `DESIGN_REQUIRED` | policy store design; separate operator authorization |
| 5 | **Distributed rate limiter**: Redis adapter | RS-02 / §4.4; §10.5 | `DESIGN_REQUIRED` | infrastructure decision; separate operator authorization |

ERH-SAF1 is the only candidate where the implementation path is fully clear
from source-verified evidence and no additional design decision is needed before
dispatch.

## Blind-Spot Control Block

Per `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`.

| Gate | Question | Verdict |
| --- | --- | --- |
| G1: Source authority | Is the primary source the archived DOCX, not the prior intake summary? | CLEAR — DOCX extracted at SHA256-verified path; intake is predecessor evidence only |
| G2: Coverage completeness | Were all document sections processed? | CLEAR — 162/162 paragraphs; 22/22 sections; zero missed |
| G3: Capability over-absorption | Does RS1 claim runtime implementation from this docs-only scan? | CLEAR — RS1 produces planning assessment only; no runtime change |
| G4: Stale-state risk | Could prior ERH tranche decisions be overwritten? | CLEAR — disposition ledger explicitly marks prior closed tranches as such; no re-opening |
| G5: Claim boundary drift | Does RS1 claim ML DLP, production readiness, or complete remediation? | CLEAR — claim boundary section explicitly denies all three |
| G6: Blind-spot in safety assessment | Does safety reassessment account for both safety.ts and safety-status.ts? | CLEAR — both files source-read; execute-chain gap explicitly documented |
| G7: Worker scope discipline | Does RS1 attempt runtime edits, package changes, or public-sync? | CLEAR — no runtime files written; `git status --short` shows only RS1 docs artifacts before reviewer commit |

**Overall verdict: CLEAR**

## Evidence / Verification

| Check | Result |
| --- | --- |
| Base anchor | `b442085e` |
| Worktree at start | `?? docs/baselines/CVF_GC018_ERH_RS1...` and `?? docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_RS1...` (dispatch packet uncommitted by design at scan start) |
| DOCX hash | `1C52C011A2D11922C5A5712FF785435474AB772B6F9C0A42563D177B1F255A10` — MATCH GC-018 |
| Extraction method | `python-docx` paragraph enumeration, UTF-8 stdout |
| Total paragraphs | 162 non-empty |
| Pre-implementation gate | `COMPLIANT: pre-implementation autorun gate passed` |
| Runtime no-edit proof | `git status --short` before reviewer commit showed only RS1 docs artifacts |
| Closure worktree state | reviewer commit required before final pre-closure gate |

## Claim Boundary

This RS1 assessment records a source-backed full-coverage rescan of the external
review Word document. It does not claim:

- runtime safety implementation (ERH-SAF1 is recommended ready, not implemented here);
- ML DLP or classifier implementation;
- complete remediation of any §4.4 architectural weakness;
- production readiness, production-grade audit storage, or production-grade CI posture;
- public readiness or public-facing security hardening claim;
- live provider/API governance behavior;
- independent external validation;
- Redis rate-limiter deployment;
- durable policy snapshot persistence.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Prior ERH intake did not prove full-document coverage under newer scan controls | CORPUS_COMPLETENESS_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | RS1 provides GC-047-style completeness block; 162/162 paragraphs mapped |
| Prior safety treatment was claim calibration only; richer safety patterns exist in safety-status.ts but not wired to execute route | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | ROADMAP_REQUIRED | ERH-SAF1_READY — open new work order for severity-classified safety chain wiring |
| safety-status.ts marked 'use client' keeps it out of server-side execute chain | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RULE_CLARIFIED | SAF1 must extract patterns to a shared non-client helper |
| Provider risk ceilings are hardcoded static values, no config-driven load | CONFIGURATION_GAP | GOVERNANCE_CONTROL_PLANE | ROADMAP_REQUIRED | separate provider-risk-configuration work order |
| policySnapshotId and audit durability remain deferred runtime roadmap items | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | ROADMAP_REQUIRED | operator-authorized audit-persistence and policy-snapshot work orders |
| Runtime/provider/cost learning lane | N/A_WITH_REASON | N/A_WITH_REASON | N/A_WITH_REASON | RS1 is a docs-only source rescan; no provider/API/secret/quota work performed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this RS1 assessment is a private provenance rescan and planning artifact.
No public-sync edits made. No public-facing corrections made here. Any
public-facing summary from RS1 findings requires a separate public-sync work
order authored in the public-sync clone.

## Closure Checklist For Worker Handoff

| Item | Worker disposition |
| --- | --- |
| RS1 assessment created | PASS — this artifact |
| DOCX hash recorded | PASS — `1C52C011A2D11922C5A5712FF785435474AB772B6F9C0A42563D177B1F255A10` matches GC-018 |
| Section coverage ledger complete | PASS — 22/22 sections; 162/162 paragraphs |
| Finding disposition ledger complete | PASS — 17/17 findings disposed |
| Section 4.4 all five mandatory rows | PASS — ephemeral audit, in-memory rate-limit, safety layer, policySnapshotId, provider risk ceilings |
| Safety reassessment completed | PASS — `ERH-SAF1_READY` with five readiness rules evaluated |
| Gates rerun | PASS — markdown, finding-learning, public export, corpus completeness, and dispatch quality gates passed before reviewer closure |
| Worktree state | PASS — reviewer closure requires committed range before final pre-closure |
| Worker did not commit | PASS |
| Runtime/source files unchanged | PASS — docs-only writes |
