# CVF Agent Orchestration, Platform And MCP Discussion Record

Memory class: FULL_RECORD

Status: DISCUSSION_ONLY_PENDING_OPERATOR_CONVERGENCE

docType: reference

Date: 2026-09-17

Text Encoding Exception: operator-facing Vietnamese discussion requires UTF-8
Vietnamese text under the user-facing-copy exception of the encoding standard.
This exception covers this record only; machine tokens and identifiers remain ASCII.

## Purpose

Ghi lại trao đổi của operator và Local orchestrator để các phiên sau tiếp tục
đúng vấn đề, không phụ thuộc lịch sử chat. Đây là bản tổng hợp có phân biệt
ý kiến operator, đề xuất Local và evidence đã kiểm tra; không phải transcript.

## Scope / Applies To

Áp dụng khi tiếp tục thảo luận phân vai, chọn model, giao việc, giám sát chi phí
và phương án host/platform/MCP. Owner quyết định kỹ thuật là Local; operator
quyết định phạm vi và quyền thực thi. Pha hiện tại: discussion and recording.

Operator yêu cầu lưu thành file và bàn luận kỹ hơn trước khi thực hiện.
Việc lưu này không mở implementation, work order thi công, CLI tự động,
provider experiment, runtime hoặc gỡ moratorium. Không tự mở successor khi
G1 T2 hoàn tất. G1 và G4 vẫn là hai audit question độc lập.

Startup anchor: mode `multi_repo_absorption_acel_g1_t2_implementation_dispatched`;
active handoff `AGENT_HANDOFF_V61_2026-09-16.md`; observed HEAD
`45e71b8906f146a737bfbc254fe6cb8e27daf047`.
G1 T2 vẫn có bảy file worker untracked; bản ghi này không review hoặc sửa chúng.

## Operator Positions

1. CVF không can thiệp vào suy nghĩ, cách tổ chức nội bộ hoặc sự thông minh
   của agent/provider. Provider-native helpers trong phiên được phép vẫn thuộc
   trách nhiệm của phiên cha; cần quản lý các assignment CVF thực sự giao.
2. Một agent có thể giữ nhiều vai. Trước khi giao subagent cần đánh giá có nên
   giao hay tự làm, chọn model/effort phù hợp và dự kiến chi phí review/rework.
3. Đường Local gọi agent khác qua CLI từng mất kiểm soát thời gian/quota.
   Hiện operator chuyển work order thủ công cho worker trong cùng workspace
   VS Code. Việc worker dùng provider khác không biến nó thành web research agent.
4. Có thể dùng platform chung làm nền vận hành; các model đảm nhiệm vai trò
   điều phối, thực thi và review; CVF kiểm soát quyền, evidence và kết quả.
   AICoworker là ví dụ cần khảo sát, chưa được chọn làm dependency.
5. Cần so sánh phương án MCP trước khi chọn nền vận hành. Chỉ ghi nhận và
   tiếp tục bàn luận ở bước này.

## Existing CVF Authority And Evidence

| Existing owner | Evidence inspected | Implication for the discussion |
| --- | --- | --- |
| `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | Topology Invariance Rule; role assignment flow | Vai trò không cố định theo model; operator chọn topology; tài liệu không chứng minh tự động chọn model hoặc runtime enforcement. |
| `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | Core Principle; Mandatory Delegation Packet; Claim Boundary | Đã có owner cho delegation và phân biệt helper nội bộ với invocation vượt ranh giới. |
| `docs/reference/project_role_provider_delegation/README.md` | Operator Approval Envelope | Đã có nơi khai báo role/provider lane và trần chi phí; chưa phải automated selector. |
| `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` | Global Invocation-Control Reassessment Override; T0 Invocation-Cost Incident | Roadmap đang parked; một lệnh CLI không tương đương một model response hoặc đơn vị chi phí cố định. |
| `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Status; Operator Decision And Priority Register | Knowledge/design đóng bounded; T5 chưa mở; không suy implementation authority từ discussion. |
| `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_NP03_LAUNCH_INTERCEPTION_ARCHITECTURE_COMPLETION_DECISION.md` | Narrow result-admission decision; covered/excluded launch surfaces | Loại kết quả thiếu evidence không chứng minh đã ngăn hoặc dừng tiến trình tạo kết quả đó. |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Invocation budget control; Worker Return Convergence Self-Proof | Có owner cho chi phí và return evidence; usage không được cung cấp không được ghi thành zero. |
| `docs/reference/CVF_PIPELINE_CHAIN_ORCHESTRATOR_CONTRACT.md` | Scope; Claim Boundary | Pipeline contract/interface không chứng minh đang chạy scheduler hoặc spawn runtime. |

Historical incident attribution: hồ sơ ghi hạn mức phiên Claude bị cạn và có
nhiều model responses/context reads. Chưa đủ evidence để quy toàn bộ hao phí
cho subagent. UI quota, token usage và API dollars là các đơn vị khác nhau.

## Three Operating Scenarios

| Scenario | What needs a decision | What must be observed before a control claim |
| --- | --- | --- |
| Một host agent giữ nhiều vai và giao helper | Tách việc có lợi không; context đủ chưa; model/effort nào phù hợp | Assignment, evidence, review/rework effort; helper count không chứng minh hiệu quả hoặc review independence. |
| Local khởi chạy worker qua CLI/MCP | Admission, phạm vi, giới hạn cộng dồn, stop/retry/fallback authority | Launch identity, tiến độ, usage được cung cấp, kết quả dừng và tác vụ còn chạy; return rejection không hoàn trả quota. |
| Nhiều agent trên platform chung | Platform có thực thi được quyết định CVF ở đường hành động bắt buộc không | Điểm chặn trước hành động, quyền công cụ/credential, cancellation, evidence export và đường bypass. |

## MCP And Platform Alternatives

MCP là giao thức kết nối host, client và server; server cung cấp tools,
resources và prompts, còn host chịu trách nhiệm điều phối và ranh giới quyền.
Vì vậy MCP riêng lẻ không thay thế toàn bộ platform kiểu AI Coworker.

Phương án cần tiếp tục so sánh:

- Platform tích hợp: platform vận hành agent và cung cấp điểm tích hợp CVF;
  MCP có thể là một trong các giao diện của platform.
- Host hiện có + MCP: IDE/agent host giữ phiên và giao diện; MCP kết nối các
  dịch vụ CVF; thành phần supervisor/worker adapter thực thi vòng đời và ngân sách.
- Host/service chuyên dụng + MCP: tự xây các phần runtime còn thiếu; phải tính
  cả chi phí duy trì, bảo mật, telemetry và kiểm thử tương thích.

Ví dụ định hướng, chưa phải API đã có: admission -> dispatch -> status/usage
-> cancel -> submit evidence -> review. Tên tool và schema chưa được thiết kế.
Lệnh cancel hay MCP timeout không tự chứng minh downstream worker đã dừng.
Một MCP tool chỉ gọi CLI rồi chờ trả về vẫn có thể lặp lại sự cố cũ.

## CVF Web As The Operator Portal

Operator follow-up on 2026-09-17: dùng CVF Web làm cổng tương tác trung gian
có thể ít tính năng hơn platform thương mại nhưng chủ động hơn về kết nối
và kiểm soát. Local đánh giá đây là ứng viên đáng ưu tiên khảo sát, chưa là
lựa chọn được phê duyệt hoặc quyền triển khai.

Phân trách nhiệm được đề xuất:

- CVF Web: nhập mục tiêu, xem kế hoạch/phân vai/model đề xuất, duyệt quyền và
  ngân sách, theo dõi tiến độ/evidence, gửi yêu cầu dừng, review kết quả.
- Backend CVF: kiểm tra assignment, quản lý trạng thái bền vững, thực thi
  giới hạn và đối chiếu kết quả theo các owner đã có.
- Worker adapter/supervisor: quản lý worker thực tế, usage quan sát được,
  cancellation và tác vụ con; báo rõ phần không thể kiểm soát.
- MCP hoặc API: giao diện kết nối tùy năng lực của host/provider; không là
  điều kiện bắt buộc cho mọi đường chạy.

Targeted source observations (source inspection only; no tests/live run):

| Local source | Observed symbol or boundary | Bounded implication |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `POST`; `verifySessionCookie`; `verifyServiceTokenRequest`; unauthorized branch returns 401 | Đã có API execution và authentication logic; không chứng minh lifecycle control cho worker CLI. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | `PipelineStage`; `PIPELINE_STAGE_ROLE`; receipt interfaces | Có vocabulary/interface cho pipeline và role; không tự chứng minh scheduler chạy. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` | `buildPendingAgentExecutionRuntime`; explicit route/provider/audit boundary | Có composition cho pending execution/store; không được suy đã nối vào web execution route. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts` | `runPendingAgentExecutionLocalHarness` | Có caller local harness; không đồng nghĩa production worker dispatcher. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/canonical-web-gateway-execution.ts` | `NON_VISION_EXECUTION_PATH_SELECTION = 'direct'` | Port-backed adapter tồn tại nhưng chưa là đường non-vision mặc định trong source đã xem. |

Điểm cần bàn: backend giữ quyền thực thi ở đâu; Web local hay hosted; worker
truy cập workspace bằng cơ chế nào; đóng tab có làm mất giám sát không; quyền
trực tiếp ngoài cổng có bypass được không. Nút Stop cần phân biệt yêu cầu đã
gửi, worker đã xác nhận và việc thực thi đã dừng; không đổi trạng thái UI
thành stopped rồi coi là bằng chứng.

Tiến độ của thảo luận: CVF Web là phương án ứng viên bổ sung. Khả năng kiểm
soát tốt hơn phụ thuộc backend và đường hành động thực tế, không chỉ quyền sở
hữu giao diện. Tái sử dụng source cần đánh giá integration/readiness riêng;
không mở lại CLI, đổi route, hoặc triển khai runtime từ bản ghi này.

## External Reference Boundary

Primary pages consulted on 2026-09-17:

- [MCP architecture, specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/architecture): host/client/server responsibilities; protocol-level evidence only.
- [AICoworker official overview](https://aicoworker.net/): vendor describes multi-agent workspaces/models and usage/cost insights; not independently verified runtime control.

COMPARISON_ONLY_NO_ABSORPTION: chỉ đối chiếu khái niệm từ trang chính thức,
không intake/absorb repository, không cài phần mềm, không chốt license hoặc
dependency, không kết luận đầy đủ về platform. Nội dung web có thể thay đổi;
cần pin/version và source verification riêng nếu chuyển sang nghiên cứu tích hợp.

## Open Questions For The Next Discussion

1. Operator duyệt envelope nào để orchestrator tự chọn worker/model bên trong?
2. Khi nào giao việc tạo lợi ích so với một agent thực hiện trực tiếp?
3. Cần evidence nào để chọn cấu hình theo task class và cập nhật lựa chọn?
4. Đơn vị ngân sách nào thực sự đo/giới hạn được cho từng API/subscription/host?
5. Ai giữ quyền stop; stop tác động đến process tree, remote task và retry thế nào?
6. Host/platform hiện có cung cấp điểm thực thi bắt buộc nào; bypass nào còn ngoài phạm vi?
7. Chọn host + MCP hay platform tích hợp theo tổng chi phí và năng lực đã chứng minh?
8. Evidence nào cần cho một thử nghiệm so sánh có baseline/candidate tương đương?

Local proposal, not ratified: ưu tiên ADAPT các owner hiện hữu; chỉ thêm trách
nhiệm kiến trúc nếu chứng minh không map được. Model mạnh/rẻ và mức effort là
cấu hình ứng viên, không phải bằng chứng chất lượng hoặc tiết kiệm.

Prior chat demonstration: Local requested one native helper with
`gpt-5.6-luna` / `xhigh`, subsequently interrupted it without an accepted return.
This is conversation-reported context, not a persisted runtime receipt or a
CVF calibration result. Actual model identity, usage and hard-budget enforcement
were not independently established. Do not reuse it as readiness/value proof.

## Resume And Decision Boundary

Phiên sau đọc bản ghi này cùng các owner đang được dẫn trước khi tiếp tục
thảo luận. Bắt đầu từ Open Questions, không chạy lại nghiên cứu hoặc thử nghiệm
chỉ để tái tạo lịch sử. Cập nhật kết luận đã thống nhất và câu hỏi còn mở tại đây.

Next move for this discussion: tiếp tục bàn luận với operator. Không tự tạo
work order thi công, không tự gỡ moratorium, không tự khởi chạy thí nghiệm.
Các nhiệm vụ đang có của CVF vẫn theo authority riêng của chúng.

## Epistemic Process Block

- Expected Result / Prediction: một bản ghi có owner links và câu hỏi mở giúp tiếp tục thảo luận qua phiên chat mà không biến đề xuất thành quyền thực thi.
- Evidence Comparison: operator yêu cầu lưu; các roadmap hiện hữu xác nhận phạm vi parked; MCP specification tách protocol khỏi host orchestration.
- Contradiction or Gap Disposition: nhận định trước rằng cần bắt đầu một cơ chế hoàn toàn mới là quá rộng; đã có EAIC và provider/model assignment owners. Runtime suitability của AICoworker chưa được xác minh.
- Claim Update: discussion được lưu để tra cứu; chưa có lựa chọn platform, thiết kế được phê duyệt hoặc implementation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator discussion record; no public export requested.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | discussion capture and navigation only |
| claimDisposition | CLAIM_REJECTED: no implemented execution-control capability claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: discussion is not a runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no worker execution or protected runtime action authorized |
| invocationBoundary | local documentation recording only |
| interceptionBoundary | no OS, IDE, provider, CLI or MCP interception claim |
| claimLanguage | pending operator discussion; existing owner evidence remains bounded |
| forbiddenExpansion | implementation, automatic dispatch, live experiment, moratorium lift, public deployment |

## Claim Boundary

Bản ghi phục vụ continuity của thảo luận, không là standard mới, accepted
design, implementation order, gate result hoặc runtime readiness proof.
Không có commit, provider experiment hay worker launch được yêu cầu bởi bản ghi.
