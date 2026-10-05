# Kịch bản giả lập operator: learning home và intake CVF

Memory class: FULL_RECORD
Status: ACTIVE_REFERENCE
docType: reference
Date: 2026-10-04

## Purpose

Dùng các bước của operator làm kịch bản kiểm chứng nội bộ cho learning home và
intake. Một Local actor thực hiện vai operator/reviewer trên workspace dùng một
lần, ghi kết quả CLI thật và giới hạn kiểm chứng. Đây không phải tài liệu đào tạo
operator hoặc bổ sung chuẩn, trạng thái, intake engine hay quyền thực thi.

## Scope / Applies To

Dành cho dự án mới đã được bootstrap theo profile1.1 và có learning home.
Project orchestrator quản lý discovery và source records; Local parent reviewer
quyết định value/dedup/admission; project owner cho phép application.

Nếu chưa có home hoặc đang dùng profile cũ, dùng
[migration contract](CVF_DOWNSTREAM_GATE_PROFILE_MIGRATION.md). Không tự tạo
lock, sửa Core template hoặc chạy upgrade chỉ để theo hướng dẫn này. Tạo mới
workspace từ provenance clone dùng entrypoint `Initialize-CVF-Operator-Workspace.ps1`
và giữ lựa chọn profile tương tác trừ khi operator đã chọn path/profile cụ thể.
CCMA và các lane parked không được mở bởi tài liệu này.

## Workflow

1. **Tìm record liên quan.** Đọc `docs/reviews/learnings/README.md` trong dự án.
   Theo trigger của công việc, đọc record liên quan trước repair/review/intake.
   Inventory rỗng là hợp lệ; không tạo learning chỉ để lấp chỗ trống.
2. **Ghi quan sát.** Dùng `LEARNING_RECORD_TEMPLATE.md` trong home để tạo record
   dự án. Ghi trigger, expected/observed, source revision/hash, evidence locator,
   confidence, action/result và claim limits. Tách quan sát trực tiếp khỏi lời
   thuật lại; giữ FAIL, timeout, SKIP và NOT RUN. Không đưa secret/customer payload
   vào record; provider memory chỉ là gợi ý để xác minh.
3. **Tìm owner trước khi đề xuất sửa.** So sánh với rule, template/checker và
   record cùng mechanism. Rule đã có nhưng chưa được áp dụng là application gap,
   không tự kết luận thiếu rule. Cập nhật record cùng mechanism thay vì tạo bản
   trùng. Parent đánh giá source confidence, reusable mechanism, existing coverage,
   incremental value và bounded proof theo [PLL standard](CVF_PROJECT_LEARNING_LOOP_STANDARD.md).
4. **Đưa record vào discovery.** Thêm link cùng trigger vào README của home;
   thêm pointer vào session memory/handoff và artifact catalog theo owner của dự
   án khi record trở thành active. Không hand-edit generated views hoặc aggregate.
5. **Chuẩn bị intake khi có value đề xuất.** Markdown record là source journal;
   JSON finding input là đầu vào khác. Dùng
   [finding input template](DOWNSTREAM_FINDING_INTAKE_TEMPLATE.json), thay mọi
   placeholder, bao gồm source SHA thực và evidence locators thực. Giữ findingId
   của dự án ổn định; không tự mint ADIF ID hoặc parent admission.
6. **Generate và kiểm tra riêng từng lệnh.** Khi project owner cho phép ghi
   intake trong dự án, dùng pinned runner theo khung lệnh phía dưới. Intake
   generation chỉ tạo exchange record; nó không gửi lên parent, không admit hoặc
   promote finding. Nếu lệnh từ chối, giữ output và sửa đầu vào trong scope;
   không xóa intake cũ để vượt qua `INTAKE_EXISTS_DIFFERENT`.
7. **Local parent review.** Chuyển source record, revision/hash, generated intake
   và đề xuất coverage/value qua handoff được phép. Không có automatic submission.
   Parent reviewer quyết định accept/merge/defer/decline với lý do và control link;
   chỉ parent owner ghi admission/back-links theo F2G. `validate-intake` thành công
   chỉ chứng minh shape/coherence/digest, không chứng minh source claim đúng.
8. **Theo dõi delivery/application riêng.** Giữ `NOT_RETURNED` và `NOT_APPLIED`
   đến khi có evidence phù hợp. Parent implementation xong không đồng nghĩa đã
   delivery; delivery không đồng nghĩa application đã được kiểm chứng. Dự án
   parked giữ `PARKED_BY_OPERATOR`; không ghi, test hoặc migrate dự án đó.

### Khung lệnh intake

Đây là command template; walkthrough đã chạy tương đương trên dự án giả lập
dùng một lần, chưa chạy trên dự án thật.
Thay cả bốn giá trị bằng path/ID đã được project owner cho phép. Finding input
phải là JSON theo template, không phải Markdown learning record.

```powershell
$projectRoot = '<absolute project path>'
$runnerPath = '<project>/scripts/cvf_gates/cvf_downstream_gate_runner.py'
$findingInput = '<absolute finding-input.json path>'
$findingId = '<project-local findingId from input>'

python -B $runnerPath intake --project-root $projectRoot --finding $findingInput
```

Kiểm tra exit code và thông báo `INTAKE: WRITTEN` trước khi chạy lệnh tiếp theo:

CLI khai báo exit0 cho PASS, exit2 cho gate refusal và exit3 cho blocked/internal
invalid input. Không dùng quy ước exit1 cho các ca refusal của runner này; giữ
actual output cùng code để phân biệt lỗi input với lỗi harness.

Sau khi generate thành công mới chạy `validate-intake`; kiểm tra exit0 cùng
`INTAKE_RECORD: VALID`. Không suy acceptance từ riêng thông báo VALID.

```powershell
$recordPath = Join-Path $projectRoot "docs/learning_intake/$findingId.intake.json"
python -B $runnerPath validate-intake --record $recordPath
```

Kết quả generation dự kiến có `acceptance=NOT_ACCEPTED_GENERATION_ONLY`,
`parentDisposition=PENDING_PARENT_ADMISSION`, các `parentLinks` rỗng. Không sửa
các giá trị đó để biến hồ sơ thành accepted. Profile/runner phải khớp phiên bản
đã được pin; xem [profile standard](CVF_DOWNSTREAM_GATE_PROFILE_STANDARD.md).

## Worked Example

**ILLUSTRATIVE_ONLY:** operator đang review một báo cáo chỉ có danh sách file
nhưng câu kết luận nói dữ liệu đã lưu và có thể resume. Đây không phải sự cố
production hoặc finding đã được parent admit. Một biến thể fixture được cố ý
inject và thực thi tại mục Step 3 And 4 Result bên dưới; không chuyển kết quả
fixture thành bằng chứng sự cố lịch sử.

| Trường trong learning record | Nội dung minh họa |
|---|---|
| Trigger / Observation | Review phát hiện kết luận vượt evidence: enumeration bị dùng như storage/checkpoint proof |
| Source / Evidence | Khi xảy ra thật, ghi revision/hash và locator đoạn báo cáo; hiện chưa có source incident |
| Project Action / Verification | Đề xuất sửa kết luận về enumeration; ghi actual diff/result khi được phép và đã làm |
| Parent Value / Dedup | So với CVF_BUILD_LEARNING_EVIDENCE_CHECKLIST.md, Sync Coverage And Claims; rule đã có |
| Value proposal | Có thể chỉ là application mistake; chưa có incremental control value thì giữ local hoặc đề xuất decline có lý do |
| Project finding/action | OPEN cho đến khi có verification thật |
| Parent value decision | PENDING_PARENT_ASSESSMENT; không ghi ACCEPT từ ví dụ |
| Parent implementation | NOT_IMPLEMENTED cho đề xuất này; không suy owner cũ là proof của proposal mới |
| Return / Application | NOT_RETURNED / NOT_APPLIED; nếu operator park thì ghi PARKED_BY_OPERATOR |

Ví dụ không cần generate JSON intake. Chỉ tạo intake khi finding có source,
evidence và value proposal cụ thể. Không biến văn bản minh họa thành receipt
`OBSERVED_LOCAL` hoặc dùng SHA placeholder như provenance.

## Audit / Source Verification

Audit giới hạn ở các nguồn được nêu dưới đây tại base `26dfe4d6a30fdccd3afe1e0669cfca4e9918bcc8`.
Các owner đã có workflow contract, shared-home template, JSON generator và typed
parent evidence. Bổ sung này tập hợp kịch bản giả lập và một ví dụ; không
claim thiếu intake/control trên toàn CVF hoặc chứng minh operator đã dùng được.

| Claim | Source file | Section / symbol | Disposition |
|---|---|---|---|
| Home/discovery, năm value checks và independent states | docs/reference/downstream_gate_profile/CVF_PROJECT_LEARNING_LOOP_STANDARD.md | Shared Home And Discovery; Value Admission; Loopback And Independent States | ACCEPT |
| Project journal và empty inventory | scripts/lib/downstream_governance/project_learning_home.template.md | Contract; Record Index | ACCEPT |
| Record fields và feedback states | scripts/lib/downstream_governance/project_learning_record.template.md | Source / Evidence; Feedback State And Links | ACCEPT |
| Explicit upgrade, preserve project content | docs/reference/downstream_gate_profile/CVF_DOWNSTREAM_GATE_PROFILE_MIGRATION.md | Upgrade | ACCEPT |
| JSON input vocabulary và placeholders | docs/reference/downstream_gate_profile/DOWNSTREAM_FINDING_INTAKE_TEMPLATE.json | finding input object | ACCEPT as input template only |
| Intake CLI và structural validation | scripts/lib/downstream_governance/cvf_downstream_gate_runner.py | main: intake; validate-intake | ACCEPT |
| Refusal và blocked exit codes | scripts/lib/downstream_governance/cvf_downstream_gate_runner.py | EXIT_PASS, EXIT_GATE_FAIL, EXIT_BLOCKED | ACCEPT |
| Generation states, identity và overwrite refusal | scripts/lib/downstream_governance/cvf_dg_intake.py | build_record; build_intake; validate_record | ACCEPT within named symbols |
| Existing coverage example | docs/reference/downstream_gate_profile/CVF_BUILD_LEARNING_EVIDENCE_CHECKLIST.md | Sync Coverage And Claims | ACCEPT |
| Parent admission và typed receipt limits | docs/reference/downstream_gate_profile/CVF_PROJECT_LEARNING_PARENT_EVIDENCE_CONTRACT.md | T2 Validation Binding; Claim Boundary | ACCEPT |
| Parent disposition owner | docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md | Protocol; Boundaries | ACCEPT |

## Verification / Acceptance Criteria

- References resolve to the named existing owners; command flags match the CLI.
- Markdown journal, finding input and generated intake remain separate artifacts.
- Example is marked illustrative and creates no observed incident/admission.
- Shape/hash validation does not become semantic acceptance or delivery/application.
- README exposes this guide; canonical standards, templates, registry and projects
  receive no behavior/state change from this documentation batch.

Author and source reviewer are one Local actor. No distinct independent review,
real-user walkthrough or real-project invocation is claimed. Reuse PLL/FR2
accepted evidence for context; the new bounded CLI composition below does not
recreate their implementation tests.

## Walkthrough Result

Evidence: [CLI simulation receipt](../../reviews/evidence/cvf-project-learning-operator-simulation-2026-10-04.json).
First attempt: [harness exit-code correction](../../reviews/evidence/cvf-project-learning-operator-simulation-first-attempt-2026-10-04.json).

Twelve scenario checks passed after three setup commands. The fresh disposable
project installed the current Core profile, indexed a synthetic learning record,
and invoked its installed runner for generation/validation. No network/provider
was invoked. TemporaryDirectory cleanup removed the exact disposable project.

| Case group | Actual observation | Boundary |
|---|---|---|
| Fresh install / home | FRESH_INSTALLED; home README/template exist | disposable Windows file-control behavior |
| Generate / validate / repeat | WRITTEN; VALID; repeat preserves exact record bytes | acceptance stays NOT_ACCEPTED_GENERATION_ONLY; parent links null |
| Changed same findingId | INTAKE_EXISTS_DIFFERENT, exit2; original unchanged | overwrite refusal |
| Markdown as finding input | INTAKE_INVALID, exit2 | journal is not JSON input |
| Stale digest / missing field with new digest | CONTENT_IDENTITY_MISMATCH / MISSING_FIELD, exit2 | digest alone does not establish schema validity |
| ACCEPTED without admission link | STATE_LINK_INCOHERENT, exit2 | declaration coherence only |
| ACCEPTED with nonexistent admission link and coherent digest | VALID, exit0 | known limit: validator does not authenticate or resolve parent admission |
| Restore / cleanup | original pending record VALID and unchanged; disposable project removed | no real project or parent registry effect |

First attempt stopped because the harness expected exit1 for gate refusal;
the runner declares EXIT_GATE_FAIL=2. The behavior was correct. Only the harness
expectation was corrected; the failed attempt remains evidence, not product FAIL.

The nonexistent-link case is an intentional limit probe. Its VALID result is
not genuine parent acceptance. Source `validate_record` checks link shape,
state coherence and digest; semantic review and parent admission remain external
to this command. No new validator/authentication change is justified by this
documented limit alone.

## Step 3 And 4 Result

Evidence: [bounded file-chain snapshots and CLI outputs](../../reviews/evidence/cvf-project-learning-file-chain-simulation-2026-10-04.json).
Status: PASS_FIXTURE_ONLY. Fourteen named checks passed; one fixture repair round.
Earlier twelve CLI scenarios were reused, not rerun. This scope is deterministic
file-control evidence, not live AI governance or a new production release gate.

| Stage | Actual result | Owner / limit |
|---|---|---|
| Admission | Declared three named inputs, artifact criteria and forbidden effects; source pinned in disposable Git | Local simulated operator; declaration is not a sandbox or real tranche admission |
| Artifact | Three inventory paths/hashes plus deliberately adverse storage/checkpoint claims | Local simulated author; injected test case, not product incident |
| Review / repair | Rejected unsupported claims; one repair preserved all rows/hashes and changed unsupported layers to NOT RUN | Same Local actor; semantic judgment is manual, not independent or automatic enforcement |
| Acceptance | Accepted repaired fixture report with exact artifact hash and prior rejected hash | ACCEPTED_LOCAL_FIXTURE_ONLY; not production acceptance |
| Learning intake | Existing Core runner wrote and validated a new synthetic finding input | Real CLI; pending record remains NOT_ACCEPTED_GENERATION_ONLY |
| Value / dedup | Five value checks; DECLINE_NEW_PARENT_CHANGE_FIXTURE_ONLY / RULE_EXISTS | Existing coverage table suffices; no parent registry admission or new control |
| Finality | Harness compared accepted report/review/decision hashes; post-review edit mismatched; restored bytes matched | Harness byte assertion, not an installed CVF mutation interceptor |
| Boundary / cleanup | Parent registry bytes unchanged; disposable project removed | CCMA and parked lanes untouched |

Step 4 repair is limited to the rejected fixture artifact, observed harness
exit-code mismatch and snapshot serialization clarity. The scenario now records
source-defined codes explicitly. A separate snapshot replay initially assumed LF;
original Windows JSON files used CRLF. Artifact bytes already matched; review and
decision hashes matched with CRLF. Evidence now states encoding, newline and key
order so raw hashes can be replayed; no CLI or historical proof was rerun.
Review/decision JSON do harness ghi dùng CRLF; generated intake do runner ghi
bằng canonical JSON sorted keys và LF. Hai dạng có serializer riêng; không áp
quy ước CRLF của harness vào digest intake.
The nonexistent admission link remains a documented structural-validation limit,
not a newly inferred production defect. No canonical standard/checker/template
change is justified by these results; stop rather than invent another control.

Machine timing is recorded per phase in the evidence JSON; the original harness
execution took 0.797 seconds. This excludes authoring/review time, tool scheduling and gate
runtime. Human/agent role time, tokens, money and opportunity cost remain UNKNOWN.
No saving or cost superiority is inferred from the fixture latency.

Generated intake, fixture learning decision and fixture closure are separate
snapshots. The parent implementation stays NOT_IMPLEMENTED and delivery/application
stay NOT_RETURNED / NOT_APPLIED; a declined new-control proposal needs no fabricated
loopback receipt. These fixtures do not authorize FLAL T4/T5 or close a CVF work order.

## Finding-To-Governance Learning Disposition

| Observation | Defect class | Learning lane | Disposition | Next control action / handled |
|---|---|---|---|---|
| VALID can carry a nonexistent syntactic admission link | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Preserve semantic/structural distinction from profile and parent evidence contracts; demonstrated and documented here, no checker rewrite |
| Wrong refusal exit-code expectation in simulation harness | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | Local harness-only mistake, not a missing CVF rule; corrected to source-defined exit2 and first attempt retained |
| Injected enumeration/storage/checkpoint overclaim in full-chain fixture | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Existing coverage table applied; fixture repaired and byte-bound acceptance recorded, no new control proposal admitted |
| Snapshot QA assumed LF for original CRLF JSON files | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Record exact serialization under existing byte-identity discipline; review/decision hashes replayed correctly without rerunning CLI |

## Text Encoding Exception

UTF-8 Vietnamese operator-facing prose is intentional under the user-facing-copy
exception. Identifiers/commands retain ASCII punctuation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: local operator documentation; no public projection or push.

## Claim Boundary

Source-backed scenario and disposable CLI shape/digest proof only. No live
governance proof, real project intake,
semantic parent acceptance, returned delivery/application, runtime execution,
CCMA adoption, FLAL T4/T5 activation or public readiness is established here.
