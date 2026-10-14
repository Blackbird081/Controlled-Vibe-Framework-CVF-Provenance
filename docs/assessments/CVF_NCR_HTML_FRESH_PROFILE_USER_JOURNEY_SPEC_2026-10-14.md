# CVF NCR HTML Fresh Profile User Journey SPEC

Memory class: governed-source-assessment
docType: assessment
Status: DESIGN_ONLY_SPEC_PENDING_REVIEW
Date: 2026-10-14
Batch ID: CVF-NCR-HTML-FRESH-PROFILE-USER-JOURNEY-SPEC-20261014
executionBaseHead: c1e1b48d0ae09f6b690a4f6ed08b007d67d4f385
Role: INTERNAL_AGENT design-only SPEC worker (shared workspace); WORKER_MUST_NOT_COMMIT
Decision owner: Local technical disposition; operator owns actual-data, business-acceptance and provider decisions

Text Encoding Exception: the Vietnamese fixture (section REQ-02) and the Vietnamese walkthrough (section REQ-04) are intentional user-facing text for a Vietnamese newcomer audience, stored as UTF-8 in NFC form. The governance envelope around them is ASCII. Verified by an exact byte-for-byte fixture comparison recorded in the worker proof JSON.

## Purpose

Give Local one actionable design packet for a fresh, explicitly chosen synthetic HTML job entered through the existing /artifacts page: the complete seven-field input and an edited second version, the owned synthetic profile and effect map with actual deployment kept UNKNOWN, a plain Vietnamese walkthrough, and the acceptance/proof map with decision dispositions. Audience: the Local reviewer who decides later admission. This is a design decision packet, not an implementation, a run, or a pilot grant.

## Source / Target

Mandatory targeted scopes were read before writing (ledger in the proof JSON `readLedger`): the /artifacts page, KnowledgeJourneyNav, ArtifactExportPanel, the export route and proof helper, the Work Transfer page, admin audit route, admin-session, enterprise-access, the Home page execution-complete and revision handlers, execute route and final-response telemetry call, execute-telemetry, control-plane-events, storage-adapter, siem-forwarder, policy-reader; also the evaluate route, route-governance-proof and governance-engine (needed to follow the receipt hop). Governed inputs: the Local prerequisites reassessment and its JSON, the NCR roadmap Current Delivery Checkpoint and stage rows, the retained cleanup completion review findings, DESIGN.md accessibility and language rules, the work-order source-verification addendum and the lifecycle Agent Continuation And Action Readiness section. Target: this SPEC plus the return and proof JSON, nothing else.

## Scope / Methodology

Source-only. No browser, Next process, engine, container, provider, test runtime, environment value, key, user store or artifact build was started or opened (all counters 0). Facts below carry file and symbol locators from current tracked source at the released base; each fact is tagged LOCKED_SOURCE_FACT, PROPOSED_DESIGN_CHOICE or OPEN_BY_ACTION. Fixture lengths and hashes are deterministic computations over the documentary text, not runtime observations. Doc-only proposal fields: fixtureVersion, profileDisposition, effectMap, journeyCase, designDecisionDisposition, futureAdmissionEvidence.

## Findings / Position

Source facts (LOCKED_SOURCE_FACT unless explicitly classified as a source-derived inference or proposal; paths under EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src):

| ID | Fact | Locator |
|---|---|---|
| F-01 | /artifacts renders KnowledgeJourneyNav currentStep 4 and ArtifactExportPanel unconditionally with starterRequest (Customer Onboarding demo, status Ready for review); no selected audit needed. | app/(dashboard)/artifacts/page.tsx:42-64,74,121 |
| F-02 | Navigation step 4 ("4. Đóng gói" / "4. Export") links /artifacts, step 5 links /work-transfer; Sidebar item links /artifacts; the Home browse card links /artifacts and its description says "with an audit record", but the export route appends no audit event. | components/KnowledgeJourneyNav.tsx:19-20; components/Sidebar.tsx:198-200; components/home/HomeBrowseExperience.tsx:418; app/api/artifacts/export/route.ts |
| F-03 | Seven request fields: title, sourcePath, sourceContent, memoryClass (FULL_RECORD or POINTER_RECORD), status, claimBoundary, receiptAnchor. normalizeRequest overlays the caller's values on DEFAULT_REQUEST. Build is disabled only while sourceContent or receiptAnchor is blank; any other blank field gets a 400 from the route. | components/ArtifactExportPanel.tsx:20-30,99-117,328,679-680,741 |
| F-04 | Build is explicit (button), POSTs the full seven fields as JSON to /api/artifacts/export; a pre-generate disclosure says a short excerpt may go to a review-checking service depending on deployment. | ArtifactExportPanel.tsx:147,203,500-504 |
| F-05 | Result state is React state only: no storage API, no abort controller, no cancel control, no unload warning in the panel; reload or navigation loses preview, receipt and checks. Identical in-flight snapshot is ignored; a newer build supersedes an older one whose response is then never shown. | ArtifactExportPanel.tsx:419-432,483-529; zero persistence/abort/unload matches |
| F-06 | Staleness: the displayed result keeps the submitted snapshot; the version tag is current when all seven fields still equal it, stale after any edit, unknown for an initial result; preview, receipt, checks, copy, download and print all refer to the displayed build. | ArtifactExportPanel.tsx:332,434-449,874-905 |
| F-07 | Route limits: title 200, sourcePath 500, sourceContent 100000, status 100, claimBoundary 2000, receiptAnchor 150 characters, body 128000 bytes; fields are trimmed; unknown keys, bad memoryClass, secret-like patterns return 400. | app/api/artifacts/export/route.ts:31-55,295-335 |
| F-08 | Rendering: heading levels 1-3, dash/star lists, bold and code spans, paragraphs; no numbered lists or tables. Output filename and anchor use a slug that keeps only a-z and 0-9, so Vietnamese diacritics are dropped. sourceHash is SHA-256 of the trimmed sourceContent in UTF-8 and appears in the HTML meta block. HTML is always lang="en" and always carries DRAFT / UNACCEPTED. | route.ts:74-137,199-255,347 |
| F-09 | Eight readiness checks; "Self-contained HTML" fails if the rendered HTML contains script, http(s):// or @import text, so a URL in source text fails that check. | route.ts:148-197 |
| F-10 | Route auth accepts any valid session (no role test) or a service token, else 401; registry risk R1 for surface artifact-export. | route.ts:271-276; lib/route-governance-proof.ts:27-33,136-290 |
| F-11 | Receipt hop is awaited inside Build: NEXTAUTH_URL plus /api/governance/evaluate; if no absolute URL the status is NOT_CONFIGURED and nothing is sent; default timeout 4000 ms (env 1000-30000); request id artifact-proof-<anchor slug>-<epoch ms>; body carries content sourceContent.slice(0,500) (500 UTF-16 code units), phase REVIEW, risk R0; header x-cvf-service-token only when CVF_SERVICE_TOKEN is set; no retry. | app/api/artifacts/export/proof.ts:2-3,20-25,56-95 |
| F-12 | The evaluate route accepts a session cookie or an equal service token; the server-side hop forwards no cookie, so the proposed same-app hop needs a matching app service token for authentication (source-derived inference; actual value UNKNOWN). Token presence alone does not establish PRESENT; a valid engine response is also needed. The app-to-engine client sends Content-Type only and does not forward this token. Engine URL env default is localhost:8000, enabled unless GOVERNANCE_ENGINE_ENABLED is false, timeout env default 5000 ms; unavailable engine gives 503. | app/api/governance/evaluate/route.ts:21-31; lib/governance-engine.ts:30-32 |
| F-13 | Receipt statuses PRESENT, NOT_CONFIGURED, TIMED_OUT, UNAVAILABLE, INVALID_RESPONSE; engine decision ALLOW shows "not artifact approval"; governanceState RECEIPT_ALLOW_REVIEW_REQUIRED needs legacy decision APPROVED plus all checks passed, otherwise DRAFT_UNACCEPTED; the attempt id is shown when no receipt. | proof.ts:97-156; route.ts:351-375; ArtifactExportPanel.tsx:796-824 |
| F-14 | Work Transfer renders the same panel only for a selected audit record from fetch /api/admin/audit; GET needs an owner or admin session (or break-glass); recordToExportRequest builds a metadata draft with anchor transfer-<record id>. | app/(dashboard)/work-transfer/page.tsx:100-120,147,166-173,276-279; app/api/admin/audit/route.ts:8-16; lib/admin-session.ts:206-216,245-268; lib/enterprise-access.ts:4,11 |
| F-15 | Successful Home execution calls emitExecutionTelemetry only for success with output, inside a catch that downgrades failure to a warning; it appends a cost event, then optional soft-cap audit, then EXECUTION_COMPLETED audit with provider, model, tokens, cost, skill ids; no output text, source or version; actor defaults apply without a session. | app/api/execute/route.ts:904; app/api/execute/route-final-response.ts:218-231; lib/execute-telemetry.ts:35-38,105-122 |
| F-16 | Home has a local stop (marks the attempt failed, returns to draft), a saved receipt archive, and follow-up refinement; no handler transfers Home output into /artifacts (grep of the Home page and browse component finds only the /artifacts link). | app/(dashboard)/home/page.tsx:441-474,489-545 |
| F-17 | Event store path: env override or .cvf/runtime file under the working directory; adapter file (default), sqlite or redis by env, unknown value throws. File init creates the directory and writes an empty list when unreadable, readAll initialises and on parse failure writes a corrupt-backup copy and rewrites; append is read-all plus rewrite (not atomic); SQLite init creates the table; File and SQLite advertise retentionSeconds null and ignore the 30-day caller constant; only a configured Redis client has the constant. | lib/control-plane-events.ts:101-105,125; lib/storage-adapter.ts:62,107-190,262-274,324-335,463-474,515-533 |
| F-18 | Every audit append fires SIEM forwarding without awaiting it; forwarding reads the active SIEM config from policy events in the same store (so a read can initialise it) and POSTs a signed event to the configured webhook only when enabled and filtered in; failure is logged only. | control-plane-events.ts:143-156; siem-forwarder.ts:18-43; policy-reader.ts:119-124 |

Position: the existing /artifacts page already supports the whole fresh-source journey; no new entry, audit producer, storage schema or runtime capability is proposed, and no source contradiction was found. Three profile prerequisites sharpen the earlier reassessment: the proposed same-app receipt hop needs matching app service-token authentication, not an engine token (F-12), the Vietnamese title must be ASCII for a readable filename (F-08), and Build latency includes the awaited receipt hop (F-11).

## REQ-01 Entry and producer

Primary entry (LOCKED_SOURCE_FACT): /artifacts through navigation step 4, the sidebar item, or the Home card (F-01, F-02). A newcomer needs a valid login only (F-10), no owner/admin role and no seeded audit. Work Transfer is an optional variant that appears useful only when an owner or admin session can list at least one audit record (F-14); the draft it creates is metadata, never the generated output (F-15). Successful Home telemetry is conditional: it needs a successful nonempty provider output and a working store, and any failure is swallowed (F-15). Negative assertions: no missing entry or producer is invented; no automatic Home-output-to-HTML join exists (F-16); the Home card claim of an audit record is recorded as an unverified UI text mismatch, not corrected here.

## REQ-02 Complete synthetic job

Job: a Vietnamese new-employee first-day guide for the fictional shop "Hoa Sen" (synthetic, no customer or personal data), replacing the starter Customer Onboarding example in every field. Status stays "Draft for review" (the starter's "Ready for review" would imply readiness); the generated page keeps DRAFT_UNACCEPTED. Intended result: one downloaded HTML review draft per version. Intended receiver: the Local reviewer, or an operator-named reviewer, reading it as a draft; nothing is sent (send/B2 parked). Enum values come from current source: memoryClass FULL_RECORD. Source Hash expected in the HTML meta block is the sourceContentSha256 below. The text avoids URLs, script/import words, secret patterns, numbered lists and tables (F-08, F-09), and exceeds 500 code units so the excerpt cut is meaningful.

fixtureVersion v1 (PROPOSED_DESIGN_CHOICE), fields in panel order:

| Field | Value |
|---|---|
| title | Huong dan nhan vien moi - ban ra soat v1 |
| sourcePath | synthetic/onboarding/huong-dan-nhan-vien-moi-v1.md |
| memoryClass | FULL_RECORD |
| status | Draft for review |
| receiptAnchor | onboarding-synth-v1 |
| claimBoundary | Chỉ là gói HTML để rà soát. Dữ liệu giả lập, không phải quy định thật, chưa được duyệt và không thay thế quyết định của người phụ trách. |
| sourceContent | (block below) |

```text
# Hướng dẫn nhân viên mới - ngày đầu tiên

Record type: Complete review record

Review status: Draft for review

## Tóm tắt

Đây là ví dụ tổng hợp cho cửa hàng giả định **Hoa Sen**. Bản này liệt kê ba việc cần làm trong ngày đầu của nhân viên mới để người phụ trách đọc lại trước khi dùng.

## Việc cần làm ngày đầu

- Nhận thẻ ra vào và đọc nội quy an toàn.
- Gặp người hướng dẫn và xem bảng phân công ca làm việc.
- Cuối ngày ghi lại một câu hỏi chưa rõ để hỏi lại vào sáng hôm sau.

## Review Boundary

Đây là bản nháp để rà soát, không phải quy định chính thức và chưa được ai phê duyệt. Mọi tên và quy trình trong bản này đều là dữ liệu giả lập.
```

fixtureVersion v2 (edited input; the other fields are unchanged from v1): title "Huong dan nhan vien moi - ban ra soat v2"; sourcePath synthetic/onboarding/huong-dan-nhan-vien-moi-v2.md; status "Revised draft for review"; receiptAnchor onboarding-synth-v2; sourceContent = v1 with "Review status: Revised draft for review", "ba việc" changed to "bốn việc", and one added list item after the last bullet: "- Báo cho người phụ trách biết mình đã đọc xong bản hướng dẫn này." Distinct anchors make the receipt request id and filename distinguish the versions (F-08, F-11).

| Computed (documentary, not observed) | v1 | v2 |
|---|---|---|
| sourceContent UTF-16 code units / UTF-8 bytes | 650 / 834 | 726 / 935 |
| expected Source Hash (SHA-256 of trimmed UTF-8) | a078550b8cf59759d4eb78413e019ab4f412c5f8fd885bbce5fdb7a721e7a7bd | cf39b5355aab4603131a4468845881b5d5d9c2ca01ac96a967ff42b5124a1edd |
| expected download filename | huong-dan-nhan-vien-moi-ban-ra-soat-v1.html | huong-dan-nhan-vien-moi-ban-ra-soat-v2.html |
| expected anchor slug | onboarding-synth-v1 | onboarding-synth-v2 |

All strings are NFC; the proof JSON holds the exact fixture strings and the 500-code-unit excerpt hashes. Typed re-entry in another normalization form would change the hash and is a future-run stop condition.

## REQ-03 Profile and effect map

profileDisposition. owned_local_synthetic is PROPOSED_ONLY: an isolated, freshly created origin, session, stores and recipients owned by Local, loaded only with fixtures v1 and v2, with no provider key and no real ledger copy. actual_operator_profile is UNKNOWN for every row; no live env, config, store or key value was read, and none is needed for this design. Source reading is not permission to open a store: File reads can create or rewrite a store (F-17).

| Topic | Proposed owned_local_synthetic | Actual deployment | Source / owner | Admission evidence (futureAdmissionEvidence) | Stop condition |
|---|---|---|---|---|---|
| Origin and evaluate destination | one loopback origin set as NEXTAUTH_URL; evaluate hop resolves to it, then to an owned real governance engine (source/report/ledger contract; no response stand-in) | UNKNOWN | F-11, F-12 / Local | recorded host:port category, no outbound route to other hosts | any other destination category |
| Session identity and roles | one fresh non-privileged test session for Export; one owner session only if the Work Transfer variant is run | UNKNOWN | F-10, F-14 / Local | identity/role declared before start | real accounts, production roles |
| Service token | fresh run-scoped matching token on the sending app and receiving app evaluate route; the engine client does not forward it | UNKNOWN | F-12 / Local | presence-only check, value never recorded | token shared with any real system; token assumed forwarded to engine |
| Data leaving the browser | full seven fields (about 1.3-1.4 KB per build) to the owned app | UNKNOWN | F-04, F-07 / Local | fixture hash equals the declared hash | content differs from v1/v2 |
| Data leaving the app | app-to-evaluate: request id, artifact/anchor slug, the first 500 UTF-16 code units of sourceContent, phase REVIEW and risk R0, plus the app token header; evaluate-to-engine: payload/phase/risk identifiers via JSON, no app token header | UNKNOWN | F-11 / Local | recipient is the owned engine only | any other recipient |
| Engine and ledger identifiers | fresh engine instance and fresh ledger namespace; request id and artifact id are the join keys | UNKNOWN | F-11, F-13 / Local | namespace empty at start | pre-existing rows, real ledger |
| Event store path/adapter | fresh path via the path env, adapter chosen explicitly (file or sqlite); the Export route itself appends no event | UNKNOWN | F-17 / Local | path outside the repo, empty, owned | shared or real path; unknown adapter |
| SIEM destinations | none: a fresh store holds no SIEM config, so forwarding is skipped | UNKNOWN | F-18 / Local | store scan shows no SIEM policy event | any enabled webhook |
| Retention and deletion | no retention is claimed: File and SQLite report null and ignore the 30-day constant; deletion is cleanup of the owned namespace | UNKNOWN | F-17 / Local | cleanup plan with exit-code-checked steps | any claim of a deployed 30-day guarantee |
| Timeouts, cancel, ambiguous retry | receipt hop 4000 ms and engine 5000 ms by default; no Export cancel; TIMED_OUT/UNAVAILABLE is ambiguous, so no automatic retry and the attempt id is recorded first | UNKNOWN | F-05, F-11, F-12 / Local | declared caps | any retry beyond the admitted budget |
| Latency and cost observation | wall-clock per Build and per hop; provider cost is zero because HTML export calls no model | UNKNOWN | F-11 / Local | zero provider starts recorded | any provider call |
| Cleanup | owned processes, stores and containers removed after the run, each command exit code checked and surfaced | UNKNOWN | retained blocked cleanup finding / Local | reviewed cleanup that cannot report ok after a failed step | silent cleanup failure |
| Fail-closed admission | a new finite effect budget (maximum builds, evaluate arrivals and wall time, set by Local at admission) and input consent; none is inherited from earlier harness budgets or unresolved cleanup | UNKNOWN | lifecycle readiness rule / Local | signed budget, consent and source-to-version binding | any missing item |

retentionSeconds null in File and SQLite never becomes a deployed 30-day guarantee. Zero effects are admitted by this SPEC.

futureAdmissionEvidence (inputs a later Local release would need; no grant here):

1. A paired packet naming the profile rows above with their reviewed values, the finite effect budget (maximum builds, evaluate arrivals, wall time) and the cleanup plan whose failed steps cannot report success.
2. Input consent and a source-to-version binding: the exact fixture strings, their NFC check and the expected hashes of REQ-02.
3. A before-effect check that origin, recipients, engine namespace, store path and SIEM state match the profile, with presence-only checks for the service token.
4. A distinct Local oracle and fixture for every REQ-05 case; the worker harness is not its own oracle.
5. A statement of what stays unproved: actual profile, business acceptance, durable intent, restart and full R3/R4.

## REQ-04 Vietnamese walkthrough

AGENT_SIMULATION_PROPOSED: a documentary simulation by an agent, not an executed human or business walkthrough, and not usability research. Tags: [NGUỒN] is current source behavior; [ĐỀ XUẤT] is a proposed usability improvement that needs separate product authorization. The interface language must be set to Vietnamese; otherwise English labels appear.

1. Đăng nhập, rồi mở mục "4. Đóng gói" ở thanh hành trình (hoặc mục Artifacts ở thanh bên). Trang "Biến phần đã duyệt thành gói HTML để rà soát" hiện ra cùng một biểu mẫu "Xuất gói rà soát" đã điền sẵn ví dụ mẫu. [NGUỒN]
2. Thay toàn bộ ví dụ mẫu bằng bản v1: Tiêu đề, Nguồn tham chiếu, Loại bản ghi = "Bản đầy đủ", Trạng thái rà soát, Mã receipt, Ranh giới rà soát, Ghi chú nguồn. Không để lại chữ nào của ví dụ cũ. [NGUỒN: bảy ô; ĐỀ XUẤT: thêm nút "Xóa ví dụ mẫu"]
3. Đọc ô cảnh báo màu vàng: việc tạo gói có thể gửi một đoạn ngắn nội dung tới dịch vụ kiểm tra. Nếu không đồng ý thì dừng, không bấm gì thêm. [NGUỒN]
4. Bấm "Tạo HTML" đúng một lần. Nút đổi thành "Đang tạo"; hãy chờ, đừng bấm lại. Hiện không có nút Hủy. [NGUỒN; ĐỀ XUẤT: nút "Dừng chờ"]
5. Đọc kết quả: dòng "BẢN NHÁP / CHƯA ĐƯỢC CHẤP NHẬN", mã #onboarding-synth-v1, một ghi chú về receipt, thẻ "Lần tạo #1 · khớp biểu mẫu", khung "Xem trước" và danh sách "Kiểm tra sẵn sàng". Chữ "ALLOW" hay "đã duyệt" của receipt không phải là nghiệm thu. [NGUỒN]
6. Bấm "Tải HTML" để lưu tệp huong-dan-nhan-vien-moi-ban-ra-soat-v1.html. Có thể thử "Sao chép HTML" hoặc "Xem bản in". Tải về không có nghĩa là đã được chấp nhận. [NGUỒN]
7. Sửa nội dung (thay bằng bản v2 hoặc chỉ sửa một ô). Thông báo "Phiên bản cũ (lần tạo #1)" hiện ra; bản xem trước, receipt, nút sao chép/tải/in vẫn thuộc lần #1. [NGUỒN]
8. Bấm "Tạo HTML" lần nữa để có lần #2 khớp biểu mẫu, rồi tải tệp v2. Hai tệp v1 và v2 phải khác nhau. [NGUỒN]

Tình huống đặc biệt:
- Thiếu thông tin: "Tạo HTML" mờ đi khi "Ghi chú nguồn" hoặc "Mã receipt" trống; ô khác trống thì máy chủ báo "Một số trường bắt buộc còn trống". [NGUỒN]
- Có chuỗi giống khóa bí mật: báo "Nội dung này có vẻ chứa khóa riêng tư hoặc mã token"; xóa chuỗi đó rồi thử lại. [NGUỒN]
- Bị từ chối: "Kiểm tra chưa phê duyệt gói này"; gói vẫn là bản nháp, có thể xem nhưng không được dùng như bản duyệt. [NGUỒN]
- Không có dịch vụ kiểm tra: "chưa cấu hình địa chỉ kiểm tra rà soát" nghĩa là không gửi gì; "hết thời gian" hoặc "không sẵn sàng" hiện kèm mã lần thử, yêu cầu có thể đã tới nơi nên đừng bấm lại ngay, hãy ghi lại mã và nhờ người vận hành kiểm tra. [NGUỒN]
- Tải lại hoặc rời trang: bản xem trước, receipt và kiểm tra biến mất, tệp đã tải vẫn còn, và không có cảnh báo trước khi mất. [NGUỒN; ĐỀ XUẤT: cảnh báo "kết quả chưa lưu sẽ mất"]
- Dừng hoặc kết quả không rõ: không có cách hủy; bấm "Tạo HTML" khi biểu mẫu đã khác sẽ thay lần chờ cũ ("đã bị thay bằng lần tạo mới hơn") nhưng không chứng minh máy chủ đã dừng; ghi lại giờ, mã và chờ người vận hành xác minh. [NGUỒN; ĐỀ XUẤT: nút hủy phía người dùng]

## REQ-05 Acceptance and proof map

Every row is a documentary proposal: no runtime PASS, request id, receipt or provider result exists or is implied. Oracles are independent of this worker (Local reviewer or later independent probe); owners: Local reviewer for technical checks, operator for business acceptance.

| Case | Expected (source-backed) | Future independent oracle / evidence | Owner | Failure condition |
|---|---|---|---|---|
| C-01 v1 build | 200; filename and anchor as computed; DRAFT_UNACCEPTED; eight checks listed; one evaluate arrival | raw route response, decoded HTML Source Hash, SQL request row at checkpoints | Local reviewer | hash, filename or anchor differs; extra arrival |
| C-02 download | downloaded bytes equal the route html bytes (UTF-8, no BOM) | SHA-256 of the saved file against the raw response | Local reviewer | any byte difference |
| C-03 edit after build | stale tag, old preview and receipt retained, no new POST | UI capture plus request count unchanged | Local reviewer | silent refresh or extra request |
| C-04 rebuild v2 | new build number, distinct anchor and hash, new request id | v2 hash and anchor in HTML; second request row | Local reviewer | v1 identifiers reused |
| C-05 denial | engine decision not ALLOW gives the denied note and still DRAFT_UNACCEPTED | owned real engine response observed as DENY; inability to induce DENY stays unresolved, not simulated proof; UI note | Local reviewer | accepted state shown |
| C-06 fallback | NOT_CONFIGURED sends nothing; UNAVAILABLE and TIMED_OUT show the attempt id | recipient capture shows zero or one arrival as stated | Local reviewer | undisclosed send |
| C-07 reload loss | preview, receipt and checks disappear, no warning, no extra POST | UI capture before and after reload; request count | Local reviewer | hidden persistence or phantom row |
| C-08 stop and ambiguity | no cancel control; ambiguous outcome recorded, no automatic retry | UI inventory and attempt-id record | Local reviewer | retry beyond budget |
| C-09 refusals | missing field and secret-like text give the stated 400 messages, no receipt | route response and UI recovery text | Local reviewer | receipt requested for refused input |
| C-10 Work Transfer variant | needs an owner/admin session and a selectable record; draft is metadata | session role record; record list | Local reviewer | output claimed as full result |
| C-11 business acceptance | out of scope here | named artifact and version, operator criteria | operator | any fixture result used as acceptance |

Join (documentary): sent seven fields -> trimmed sourceContent SHA-256 -> HTML Source Hash -> anchor slug (also the HTML element id and engine artifact id) -> governanceReceiptAttemptId (artifact-proof-<slug>-<epoch ms>, also the receipt id and engine request id) -> filename from the title slug -> saved file bytes. The engine event carries request id, decision and timestamp but not the artifact id or the 500-unit payload (roadmap source convergence note), so the artifact id comes from the engine response and excerpt equality needs a recipient-side capture, otherwise it stays OPEN_BY_ACTION. SQL observation is finite (admission, stop, final checkpoints); continuous absence and exactly-once are not claimed.

## REQ-06 Decision and roadmap boundary

| ID | Decision | Disposition | Owner / action / evidence |
|---|---|---|---|
| D-01 | Use /artifacts as the fresh-source entry; Work Transfer stays the audited variant | LOCKED_SOURCE_FACT | F-01, F-14 |
| D-02 | HTML export itself calls no model; configured export -> app evaluate -> engine has two HTTP hops, not one | LOCKED_SOURCE_FACT | F-04, F-11; roadmap Q008/D015 |
| D-03 | Receipt ALLOW is not acceptance; audit metadata is not full output or a version transfer | LOCKED_SOURCE_FACT | F-13, F-15 |
| D-04 | The proposed same-app hop uses matching app service-token auth; the engine client does not forward it; valid report/ledger response still required for PRESENT | PROPOSED_DESIGN_CHOICE, source-derived inference from F-11/F-12 | Local verifies owned profile at future admission |
| D-05 | ASCII title and anchor, NFC text, no URLs, headings and dash lists only | PROPOSED_DESIGN_CHOICE | F-08, F-09; Local reviewer |
| D-06 | Separate versions with distinct anchors and titles | PROPOSED_DESIGN_CHOICE | Local reviewer |
| D-07 | Single-pass walkthrough labelled AGENT_SIMULATION_PROPOSED | PROPOSED_DESIGN_CHOICE | Local reviewer |
| D-08 | Cancel control, reload warning, clear-demo control and Home card wording are product changes | OPEN_BY_ACTION | operator/Local product decision; separate authorization and evidence |
| D-09 | Actual profile values (origin, auth, engine, store, SIEM, retention, latency, cost) | OPEN_BY_ACTION | Local can select a fresh owned synthetic profile in a later paired scope; actual deployment or sensitive values require their own admission. Values remain UNKNOWN here |
| D-10 | Full real-AI R3 job: Home generation or revision through a real provider plus explicit transfer of the exact chosen output and version into /artifacts | OPEN_BY_ACTION | separate provider, model, auth, cost and stop authority; F-16 shows no automatic join |
| D-11 | Business acceptance, real data/custody, send/B2, P11, public, deploy | OPEN_BY_ACTION | operator checkpoints, parked |
| D-12 | Cleanup control cluster stays BLOCKED, no third control BUILD, no counter reset | LOCKED_SOURCE_FACT | retained completion review |

R1 and R2 remain partial, R3 and R4 open, R5 and R6 deferred (roadmap stage rows). This SPEC is not a new grant and not a repair of the blocked cleanup cluster; the retired provider grants stay retired.

## Risk / Corrective Action

- The Home card says an audit record is included while Export appends none (F-02); no correction is made here.
- Without matching app service-token auth or a forwarded session, the standard app evaluate hop returns 401 mapped to UNAVAILABLE (F-12). NOT_CONFIGURED still sends nothing; token presence is not sufficient for PRESENT. Admission checks matching auth and a valid engine response, without logging the token.
- Vietnamese diacritics in the title silently degrade the filename and anchor (F-08); the fixture uses ASCII there.
- Build repetition, not a single Build, is the effect risk: each Build creates a new request id and no cancel exists (F-05, F-11).
- Corrective action: Local dispositions are action-specific: D-08 improvements are deferred and do not gate a current-source synthetic rehearsal; D-09 needs a separately admitted owned profile; D-10 needs a separate full R3 provider/output-version join; D-11 operator checkpoints gate their named effects. They do not gate acceptance of this documentary SPEC.

## Decision / Disposition

Local-corrected documentary projection of the worker submission; terminal technical disposition is in the Local completion review. The original worker return/proof and final-gate bytes remain preserved. Any rehearsal needs its own paired packet, finite effect budget and cleanup admission; no successor is opened here.

## Evidence / Verification

Source pins before and after (31 inputs, all unchanged) and the read ledger are in `docs/reviews/evidence/ncr-html-fresh-profile-user-journey-spec-worker-20261014.json`; seven proof entries (PROOF-REQ-01..07) map each requirement to its SPEC section, source locators and remaining action. Structural checks do not prove reading, runtime behavior or acceptance.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Entry and starter | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/artifacts/page.tsx` | lines 42-121 | ArtifactsPage | existing page | ACCEPT |
| Seven fields, stale, no cancel | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | lines 20-30, 328-529 | handleGenerate | existing panel | ACCEPT |
| Slug, hash, checks, auth | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | lines 74-376 | POST | export route | ACCEPT |
| Receipt hop | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | lines 56-156 | fetchGovernanceReceipt | proof helper | ACCEPT |
| Audit access | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/admin-session.ts` | lines 206-268 | requireAdminApiSession | admin session | ACCEPT |
| Store and retention | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | lines 107-190, 262-335 | FileEventListAdapter | event adapters | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_finding_to_governance_learning.py; governance/compat/check_rescan_intelligence_hardening.py; governance/compat/check_epistemic_process_packet.py; governance/compat/check_public_export_disposition.py; governance/compat/check_work_order_acceptance_ledger.py |
| literalTokensReviewed | baseline section groups; Text Encoding Exception marker; Source Verification row symbol rule; Findings heading and learning section; defect class, lane and disposition enums; epistemic block labels; DEFERRED_PRIVATE_ONLY reason |
| gateRunPurpose | confirmation/evidence after targeted constants were read before writing; structural validation is not runtime proof |
| claimBoundary | targeted constants and predicates only; no claim that every checker body was read |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Home card text promises an audit record that Export does not write | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | Local decides wording under D-08 | deferred, product change |
| Receipt hop depends on a service token that the earlier source summary did not list | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | token presence added to the admission checklist | handled in REQ-03 |
| Slug drops Vietnamese diacritics from filename and anchor | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | ASCII title chosen for the fixture | handled in REQ-02, product behavior deferred |

Runtime/provider/cost learning lane: N/A_WITH_REASON - documentary design, no runtime observation.

## Epistemic Process Block

Expected Result / Prediction: the existing /artifacts source supports a bounded synthetic journey design; deployment values, future proof and business acceptance remain unknown.
Evidence Comparison: current source confirmed the entry, the seven fields and the awaited receipt hop, and added the service-token, slug and ASCII-title facts missing from the earlier summary; no source contradicted the reassessment. Local source review corrected app-versus-engine authentication, two-hop topology and real-engine proof wording; original worker bytes/proof remain in frozen custody.
Contradiction Or Gap Disposition: the Home card wording and the absence of cancel and reload warning are recorded as source facts, not corrected; deployment values stay UNKNOWN.
Claim Update: design completeness only; no runtime, profile, walkthrough or acceptance claim.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: finite named-source design packet, not a corpus rescan or intake refresh.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named targeted sources only, no complete scan or all-files-read claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design packet in the provenance workspace; no public-sync authorization or export action.

## Claim Boundary

DOCUMENTATION_ONLY; PROPOSAL_ONLY_NO_RUNTIME_READINESS. Receipt ALLOW is not artifact acceptance; metadata audit is not full output or version transfer; the agent simulation is not a human or business walkthrough. Actual profile, origin, auth, engine, store, SIEM, retention, latency and cost are unverified. R1/R2 partial, R3/R4 open, R5/R6 deferred; actual-data/custody, business acceptance, send/B2, P11, public and deploy remain parked; LHW24 retained; no provider call is allowed and the retired provider grants stay retired.
