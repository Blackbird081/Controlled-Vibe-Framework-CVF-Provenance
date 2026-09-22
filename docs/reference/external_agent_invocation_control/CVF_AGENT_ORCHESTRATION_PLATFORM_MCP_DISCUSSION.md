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

Startup anchor: mode `multi_repo_absorption_acel_g1_t2_r2_rejected_parked`;
active handoff `AGENT_HANDOFF_V61_2026-09-16.md`; observed HEAD
`ce3973041`.
G1 T2 có bảy file worker untracked sau khi R2 bị Local từ chối và parked;
bản ghi này không review, sửa hoặc mở lại chúng.

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
| Một host agent giữ nhiều vai và giao helper | Tách việc có lợi không; context đủ chưa; model/effort nào phù hợp | Assignment, evidence, review/rework effort; gate scope phải đối chiếu với worktree scope và worker-owned batch theo `## Gate Scope Reconciliation`; helper count không chứng minh hiệu quả hoặc review independence. |
| Local khởi chạy worker qua CLI/MCP | Admission, phạm vi, giới hạn cộng dồn, stop/retry/fallback authority | Launch identity, tiến độ, usage được cung cấp, kết quả dừng và tác vụ còn chạy; return rejection không hoàn trả quota. |
| Nhiều agent trên platform chung | Platform có thực thi được quyết định CVF ở đường hành động bắt buộc không | Điểm chặn trước hành động, quyền công cụ/credential, cancellation, evidence export và đường bypass. |

### Scenario 1 Expansion: Ba Phạm Vi Không Được Lẫn

Khi một host agent giữ nhiều vai trong workspace dùng chung, ba phạm vi sau
phải được phân biệt trước khi diễn giải kết quả gate. Lẫn ba phạm vi này
dẫn tới hai lỗi ngược chiều: worker nhận nhầm lỗi không phải của mình, hoặc
worker sửa file ngoài quyền ghi để "làm xanh" gate.

| Scope | Định nghĩa | Ai chịu trách nhiệm | Rủi ro khi đọc sai |
| --- | --- | --- | --- |
| Gate scope | Path, changed range, worktree, current state hoặc aggregate mà checker thực sự đánh giá. | Checker owner định nghĩa; dispatcher/worker phải đọc trước khi dùng verdict | Coi verdict của một topology là verdict của topology khác |
| Worktree scope | Toàn bộ thay đổi đang tồn tại trong working tree, gồm cả công việc đồng thời của agent/phiên khác. | Shared-worktree coordinator và từng lane owner | Worker nhận nhầm lỗi của phiên khác thành của mình |
| Worker-owned batch | Đúng tập path mà work order trao quyền ghi cho worker. | Dispatcher định nghĩa; worker tuân thủ | Worker sửa ngoài batch để làm xanh gate, phá Write Ownership |

Quan sát bắt buộc trước khi diễn giải gate cho một batch: mỗi violation row
có đủ locator phải được quy về một phạm vi theo `## Gate Scope Reconciliation`.
Verdict toàn gate vẫn báo cáo nguyên trạng. Có thể ghi riêng disposition của
worker-owned delta, nhưng không được đổi nó thành batch `PASS`; dependency,
authority hoặc current-state failure ngoài path vẫn có thể chặn return/commit.

## Claude Subagent Retrospective Intake

Operator cung cấp phản hồi của Claude về cách nó đã tạo subagent trong phiên
G1 T2. Phản hồi này được intake như `ADVISORY_RETROSPECTIVE`, không phải
runtime receipt, provider truth, accepted design hoặc policy. Local chỉ giữ
những quan sát có ích và ghi riêng các điểm chưa được chứng minh.

### Useful Observations Retained

1. Tách một phần việc có khối lượng đọc/kiểm tra độc lập lớn có thể bảo vệ
   context của parent, nếu deliverable và điểm tích hợp được giới hạn rõ.
2. Nhiệm vụ giao xuống nên có kết quả kiểm chứng được như test, gate hoặc
   evidence packet; nhưng kết quả máy chỉ chứng minh điều nó thực sự kiểm tra.
3. Việc chạm ngưỡng hoặc gate phải đọc luật gate trước khi sửa, bất kể parent
   hay child thực hiện. Parent tự làm không tự động an toàn hơn; quyết định
   phân công chỉ xét context/review cost sau khi đã xác định đúng gate law.
   Kèm theo: sửa tới sát ngưỡng cứng không đủ, vì gate có thể áp thêm luật
   khác trong vùng biên. Trong incident đã nêu, đưa file về đúng 999/1000 vẫn
   kích hoạt `near_hard_statement_compression`; chỉ khi xuống dưới biên
   `hard - 25` thì luật đó mới không còn áp dụng. Nguyên tắc rút ra là xác
   định safety margin từ chính source của checker, không suy từ ngưỡng cứng.
4. Claude tự báo đã để model mặc định cho bốn subagent. Đây là tín hiệu rằng
   model-selection admission chưa xảy ra trước dispatch, không phải bằng chứng
   model mặc định gây ra các lỗi semantic.
5. Claude tự báo một R2 worker tiếp tục spawn child để cắt file và cả hai bị
   rate-limit, làm parent mất dấu tiến độ. Đây là incident signal cho nhu cầu
   giới hạn delegation depth, child count, quota và return/cancellation state;
   chưa đủ để quy toàn bộ quota loss cho nested spawn.
6. Phân biệt semantic/design work với mechanical trimming là một heuristic
   hữu ích để hình thành candidate routing. Nó cần đo bằng comparable tasks,
   review burden và failure outcomes trước khi trở thành policy.

### Claims Not Accepted From The Retrospective

- Không nâng bảng `Opus`/`Sonnet`/`Haiku` thành mapping bắt buộc. Tên model là
  provider-specific; CVF cần mô tả capability/risk tier trước, adapter mới map
  sang model hiện có và ghi model thực tế trong receipt.
- Không coi lời kể "dùng mặc định cả bốn lần" là bằng chứng model identity,
  effort, token usage hoặc chi phí. Cần tool/runtime receipt nếu claim đó ảnh
  hưởng admission, cost accounting hoặc đánh giá chất lượng.
- Không suy rằng model mạnh hơn chắc chắn tránh được lỗi R1/R2. Test xanh vẫn
  có thể đồng tồn tại với implementation sai khi test fixture đã encode sai
  semantic; reviewer independence và design-to-code parity vẫn bắt buộc.
- Không chấp nhận cấm nested subagent vĩnh viễn chỉ từ một incident. Posture
  an toàn hiện tại có thể là deny-by-default hoặc `maxDelegationDepth=1`, nhưng
  quyết định cuối phải xét host observability, quota control và cancellation.
- Không gắn cố định role với model. Một model có thể giữ nhiều role và cùng
  một role có thể cần model khác nhau theo task class, risk và evidence burden.

### Second Retrospective Adjudication

Operator chuyển tiếp phản hồi thứ hai của Claude dưới dạng
`TEXT_RELAY_NOT_BYTE_STABLE`. Đây vẫn là `ADVISORY_RETROSPECTIVE`; provider
memory và tự thuật không phải CVF authority hoặc receipt. Local disposition:

| Proposal | Disposition | Reason / adaptation |
| --- | --- | --- |
| `deliverableSelfValidationBoundary` | `ADAPT_FOR_DISCUSSION` | Có giá trị nếu khai rõ oracle, fixture helper, acceptance rule hoặc test expectation nào do chính worker tạo và mapping nào tới authority có trước. Không tạo owner mới ở bước này; map vào anti-collusion, Source Verification và independent-review evidence. Tự khai báo vẫn là self-report, không thay independent probe. |
| finding sống sót qua gate xanh | `ADAPT_FOR_MEASUREMENT_DESIGN` | Dùng escaped-finding count/rate theo task class để phát hiện gate/oracle yếu. Không nhận chuỗi `4 -> 3 -> 4` làm calibration fact trước khi Local đối chiếu finding identity, severity, gate set, review independence và mẫu số. Round count đơn thuần không chứng minh root cause thuộc model, test generator hay schema. |
| gate scope so với worktree/batch scope | `ACCEPT_FOR_DISCUSSION` | Repo-wide gate có thể báo lỗi ngoài worker-owned delta. Return phải phân loại mỗi failure là `IN_SCOPE`, `PRE_EXISTING_OUT_OF_SCOPE`, `CONCURRENT_OUT_OF_SCOPE` hoặc `UNKNOWN`; worker không được sửa ngoài scope chỉ để làm gate xanh. |
| parent tự làm mechanical threshold work an toàn hơn | `REJECT_AS_GENERAL_RULE` | Incident file-size cho thấy điều kiện chính là đọc đúng checker và safety margin (`hard - 25` trong trường hợp đã nêu), không phải actor identity. |

Candidate measurement nên tách ít nhất:

`independently confirmed escaped material findings / independently reviewed material findings`

và luôn mang task class, gate-set identity, round, severity, oracle provenance,
reviewer independence và comparable-condition marker. Nếu mẫu số hoặc review
độc lập không có, chỉ ghi count quan sát được, không gọi là rate.

### Accumulating Use-Case Ledger

Mục này tích lũy case evidence để roadmap sau có nhiều tình huống thực tế hơn.
Mỗi row là một quan sát bounded, không tự trở thành model-ranking result,
routing policy hoặc architectural requirement. Chỉ promotion khi có owner,
comparable conditions và acceptance evidence riêng.

| Case ID | Task class and evidence | Controls that worked | Independently found escape | Bounded learning | Claims not established | Roadmap promotion condition |
| --- | --- | --- | --- | --- | --- | --- |
| `UC-SEMANTIC-SCHEMA-SELF-ORACLE-01` | G1 T2A documentation-only semantic schema amendment; dispatch `d920a6891`; R1 review `994297076`; terminal R2 review `3a027fa2e`; ten worker/frozen evidence paths remain uncommitted | Exact-path manifest, zero delegation, no worker commit, frozen hashes, GC-026 topology, SCEC correction and non-pooling claim correction held | R1 repair left four material findings: selected required/extras topology not implemented; canonical list/delimiter ambiguity including a concrete receipt collision; accept-time snapshot did not bind later invalidation events; failed required gate was disclosed but terminal label remained COMPLETE | Scope compliance and several corrected claims can coexist with a still-invalid root contract. When blocker count does not decrease, architecture reassessment can be more valuable than another local repair of the same artifacts | Không chứng minh Claude kém, model mặc định gây lỗi, model mạnh hơn sẽ tránh lỗi, delegation là nguyên nhân, hoặc finding count là a model-quality rate | Outcome is `STOP_REASSESS_ARCHITECTURE`; require comparable cases before changing capability tier/model routing, and require a fresh authority/serialization/invalidation architecture before any G1 successor |

Case schema cho các lần bổ sung sau:

- `observedFacts`: path/commit/receipt và điều kiện thực sự quan sát được;
- `controlSuccesses`: control nào đã ngăn scope, effect hoặc authority drift;
- `escapedFindings`: finding độc lập nào gate/self-check trước đó không bắt;
- `causalHypotheses`: giả thuyết cần thử, không ghi như root cause đã biết;
- `rejectedAttributions`: model/provider/actor attribution chưa đủ evidence;
- `promotionThreshold`: bằng chứng bổ sung cần trước khi đổi roadmap/policy;
- `laterOutcome`: rework có đóng finding không và phát sinh finding mới nào.

`laterOutcome` của case trên là `REVIEW_REJECTED_STOP_REASSESS_ARCHITECTURE`
tại Local review `3a027fa2e`. Đây không phải model-failure verdict: review giữ
lại các control/correction đã hoạt động và chỉ bác root-contract authority.
Khi thêm case, giữ cả control thành công lẫn defect để tránh chỉ thu thập
failure story và làm lệch routing decision.

### Candidate Evidence Envelope For Further Discussion

Nếu tiếp tục thiết kế, mỗi delegated assignment nên cân nhắc ghi các trường
sau. Đây là discussion candidate, chưa là schema được chấp nhận:

| Candidate field | Question it must answer |
| --- | --- |
| `delegationReason` | Vì sao giao xuống tốt hơn parent tự làm sau khi tính context/review cost? |
| `roleAndDeliverable` | Child chịu trách nhiệm phần nào và trả artifact/evidence gì? |
| `taskClassAndRisk` | Công việc semantic, mechanical, research hay execution; hậu quả sai là gì? |
| `requiredCapabilityTier` | Năng lực/effort tối thiểu theo provider-neutral vocabulary là gì? |
| `selectedProviderModel` | Model thực tế nào được chọn, bởi ai, dựa trên evidence nào? |
| `delegationDepthAndChildLimit` | Child có được spawn tiếp không; tối đa bao nhiêu tầng/child? |
| `timeTokenQuotaCeiling` | Trần nào quan sát và enforce được; unknown usage fail/route thế nào? |
| `pathToolEffectBoundary` | File, tool, credential, network và external effect nào được phép? |
| `terminalAndStopCondition` | PASS/BLOCKED/timeout/cancel được xác nhận bằng evidence nào? |
| `childExecutionReceipt` | Model/effort/usage/timing/child tree/result thực tế nào đã quan sát được? |
| `deliverableSelfValidationBoundary` | Oracle, fixture helper, acceptance rule hoặc test expectation nào do worker tự tạo; mapping nào tới authority có trước và phần nào cần independent probe? |
| `gateScopeReconciliation` | Gate xét repo/worktree/range nào; failure nào thuộc worker-owned delta, pre-existing, concurrent hay chưa xác định? |
| `parentIntegrationDisposition` | Parent accept, adapt, reject hay require independent review? |

Candidate control sequence để tiếp tục bàn luận:

`task classification -> capability requirement -> candidate selection -> budget admission -> delegation envelope -> bounded execution -> child receipt -> parent integration -> independent review`.

Sequence này không chứng minh mọi bước phải là một service riêng hoặc phải do
CVF Web/MCP thực hiện. Điểm cần xác minh tiếp là host/provider nào có thể cung
cấp và enforce từng receipt/control point, và đường bypass nào vẫn tồn tại.

## Gate Scope Reconciliation

Một số aggregate/current-state gate quan sát ngoài worker-owned batch, nên một
verdict `VIOLATION` không tự chứng minh worker-owned delta có lỗi. Mỗi failure
row có đủ locator trong worker return phải được quy về đúng một trong bốn phân
loại sau. Đây là discussion candidate, chưa phải schema được chấp nhận.

| Classification | Nghĩa | Bằng chứng tối thiểu | Ai xử lý |
| --- | --- | --- | --- |
| `IN_SCOPE` | Violation trỏ vào path thuộc worker-owned batch | Path trong violation message nằm trong Required Artifact Manifest | Worker sửa trước khi return |
| `PRE_EXISTING_OUT_OF_SCOPE` | Violation đã tồn tại trước execution base, không do delta này tạo ra | Cùng checker version và comparable environment chạy tại execution base cho cùng violation | Không sửa ngoài quyền; báo cáo và route cho owner |
| `CONCURRENT_OUT_OF_SCOPE` | Violation do công việc đồng thời của phiên/agent khác trong cùng worktree | Path không thuộc batch; `git status` cho thấy thay đổi ngoài batch; operator hoặc owner khác xác nhận | Không sửa; ghi rõ trong return |
| `UNKNOWN` | Chưa quy được về ba loại trên | Ghi nguyên văn violation và lý do chưa phân loại được | Escalate cho reviewer, không đoán |

Quy tắc bắt buộc kèm theo:

- Worker không được sửa path ngoài worker-owned batch chỉ để làm gate xanh,
  kể cả khi biết cách sửa. Đó là vi phạm Write Ownership.
- Worker không được viết lại full-gate verdict thành `PASS`/`COMPLIANT` khi
  còn failure. Có thể ghi `worker-owned delta has no named violation` nếu có
  evidence, nhưng governing work order quyết định failure ngoài scope có chặn
  return hay material commit hay không.
- `UNKNOWN` không được mặc định coi là ngoài phạm vi. Phân loại sai theo
  hướng có lợi cho worker là một defect class riêng cần reviewer kiểm.
- Phân loại của worker là self-report. Reviewer tiêu thụ evidence hợp lệ và
  chỉ rerun tại boundary bắt buộc hoặc khi có named contradiction, expected
  information gain và cost reason; không broad-rerun chỉ để tái tạo packet.

Quan sát nguồn gốc: ngày 2026-09-17, `run_worker_return_fast_gate.py` báo
`VIOLATION` với ba row (`Delta execution claim boundary`, `foundation storage
layout`, `agent packet authority and encoding`) đều trỏ vào một artifact thảo
luận đồng thời ngoài bảy path của batch G1 T2. Đây là ví dụ
`CONCURRENT_OUT_OF_SCOPE`; nó minh hoạ nhu cầu phân loại nhưng không tự chứng
minh bảng phân loại trên đã đủ hoặc đúng cho mọi gate.

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

### Operator discussion checkpoint — 2026-09-22

The operator elected to defer further MCP/MUO clarification and return to the
active ACEL G1-G6 program. The following points are retained for that later
tranche without changing the current moratorium or opening implementation:

1. Role-to-model assignment is not fixed. A model/effort declaration records
   the current bounded invocation. An operator-mediated model switch in the
   same conversation is `SINGLE_AGENT_MULTI_ROLE` with inherited context and
   does not by itself establish different-actor review independence.
2. Native subagents spawned by an authorized parent remain internal
   orchestration unless they separately cross a process, provider/account,
   credential, durable-action or authority boundary. A separately launched
   CLI/MCP worker crosses the external invocation boundary even when it writes
   into the same VS Code workspace.
3. Cost optimization means total cost to an accepted outcome: worker effort,
   review, failed attempts and rework. A cheaper model that creates more repair
   work may have higher total cost. Model tier is therefore an adaptive routing
   input, not a permanent role label or a quality claim.
4. The accepted HRLTP-T1 naturalistic observation is persisted at
   `docs/reviews/evidence/cvf-hrltp-t1-multi-agent-routing-observation-2026-09-22.json`
   and material commit `dd0e9eed`. It records four lanes, three model/effort
   configurations, test outcomes and reviewer-local repairs. Per-model elapsed
   time, token, quota and currency cost remain unavailable; the observation is
   not comparative superiority evidence or a P4 automatic enrollment.
5. Manual work-order relay currently supplies a human admission and lifecycle
   barrier. Replacing it with CLI/MCP requires machine-observable launch
   identity, cumulative budget, progress, cancellation including process-tree
   termination, exact workspace/path authority, child limits, terminal state,
   execution receipt and result quarantine before reviewer admission.
6. MCP alone is an interface, not a supervisor. A tool that starts a CLI and
   waits for output can repeat the prior time/quota-control failure; timeout or
   client cancellation does not prove that a downstream worker, retry or child
   process stopped.

Disposition: `DEFER_TO_FUTURE_MCP_OR_MUO_TRANCHE`. Continue to preserve the
active external-agent invocation moratorium. This checkpoint authorizes no
CLI/MCP worker launch, automated provider/model routing, runtime supervisor,
live experiment or public/deployment action.

1. Operator duyệt envelope nào để orchestrator tự chọn worker/model bên trong?
2. Khi nào giao việc tạo lợi ích so với một agent thực hiện trực tiếp?
3. Escaped-finding count/rate nào, dưới gate set và comparable conditions nào,
   đủ để đổi capability tier, review-probe requirement hoặc routing theo task class?
4. Đơn vị ngân sách nào thực sự đo/giới hạn được cho từng API/subscription/host?
5. Ai giữ quyền stop; stop tác động đến process tree, remote task và retry thế nào?
6. Host/platform hiện có cung cấp điểm thực thi bắt buộc nào; bypass nào còn ngoài phạm vi?
7. Chọn host + MCP hay platform tích hợp theo tổng chi phí và năng lực đã chứng minh?
8. Evidence nào cần cho một thử nghiệm so sánh có baseline/candidate tương đương?
9. `deliverableSelfValidationBoundary` map vào owner nào đã có (anti-collusion,
   Source Verification, oracle provenance) và khai báo tới mức chi tiết nào thì
   đủ để reviewer chọn điểm probe, mà không biến thành khai báo hình thức?
10. Khi worker khai `CONCURRENT_OUT_OF_SCOPE` hoặc `UNKNOWN`, reviewer cần
    bằng chứng tối thiểu nào để xác nhận phân loại đó, và ai chịu trách nhiệm
    đưa các row ngoài phạm vi về trạng thái sạch trước material commit?
11. Bao nhiêu case comparable và outcome sau rework là đủ để promotion một
    bounded learning thành mandatory review probe hoặc model-routing signal?

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
- Evidence Comparison: operator yêu cầu lưu; các roadmap hiện hữu xác nhận phạm vi parked; MCP specification tách protocol khỏi host orchestration; G1 T2A reviews `994297076` và `3a027fa2e` cung cấp use case đầu tiên nhưng không cung cấp model-comparison evidence.
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
Bản ghi không tự mở provider experiment, worker launch hoặc implementation.
