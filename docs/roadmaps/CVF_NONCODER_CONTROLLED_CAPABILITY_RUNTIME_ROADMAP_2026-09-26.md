# CVF Roadmap: Năng lực cộng đồng, thực thi có kiểm soát, trải nghiệm non-coder

Memory class: FULL_RECORD

docType: roadmap

Status: ACCEPTED_DIRECTION_PARKED

Date: 2026-09-26

Program ID: CVF-NCR

Version: 1.1

Revision disposition: ACCEPTED_WITH_MINOR_NOTES_RESOLVED

Decision owner: operator về định hướng/phạm vi; Local reviewer về đối chiếu kỹ thuật và nghiệm thu.

## Purpose

Đưa CVF từ nền tảng đã hấp thụ các pattern hữu ích tới những quy trình người dùng thực sự sử dụng được: người dùng nói mục tiêu, chọn agent/tài khoản, cấp quyền phù hợp, xem kết quả và quyết định sử dụng. CVF tận dụng năng lực cộng đồng qua skill, MCP, API, CLI và runtime upstream, đồng thời giữ quyền sở hữu độc lập đối với hợp đồng công việc, ranh giới quyền, bằng chứng và tiêu chí chấp nhận.

Đối tượng chính là người dùng không chuyên lập trình, làm việc theo cách vibe coding. Họ không phải hiểu repository, work order, manifest, hash, terminal hay các trạng thái nội bộ để hoàn thành công việc thông thường.

Đích đến không phải một bộ tài liệu lớn hơn, cũng không phải một agent framework mới. Đích đến là các công việc có giá trị, chạy được, biết giới hạn, phục hồi được và chuyển được từ máy cá nhân sang môi trường phù hợp.

### Đọc nhanh cho người dùng

- Bạn nói việc muốn làm; không cần biết lập trình hoặc tự cấu hình hệ thống.
- Bạn chọn trợ lý AI, mô hình và tài khoản mình muốn dùng trong số kết nối được hỗ trợ rõ ràng.
- CVF tận dụng các công cụ sẵn có, chỉ cho làm trong phạm vi bạn đã đồng ý.
- Bạn xem bản nháp, yêu cầu sửa bằng lời nói và quyết định khi nào gửi hoặc xuất bản.
- Kết quả và lịch sử được lưu; lỗi phải có cách xử lý dễ hiểu, không bắt bạn đọc mã kỹ thuật.
- Thử ổn định trên máy cá nhân trước, sau đó chuyển sang máy chủ để dùng từ nhiều nơi và bảo vệ dữ liệu.
- Có thể bổ sung tính năng, nhưng không đổi mục tiêu phục vụ người không chuyên hoặc ép bạn dùng một nhà cung cấp.

## Authorization / Decision

Operator yêu cầu tổng hợp thảo luận thành một roadmap chi tiết, cho phép bổ sung để hoàn thiện nhưng không làm lệch hướng. Yêu cầu này cho phép tạo tài liệu định hướng; không tự mở implementation, cài dependency, dùng credential, gọi provider, thực thi upstream, deployment hay public sync.

Roadmap này là định hướng kế tiếp, không sửa trạng thái đóng của ACEL-AKOE-R1 và không hồi sinh các lane G1-G7 đã dừng/đóng. Khi triển khai, mỗi tranche phải có phạm vi và thẩm quyền tương ứng theo các owner hiện hành. Không suy ra quyền chạy từ việc một giai đoạn được liệt kê ở đây.

Startup acknowledged: current mode=`acel_applied_knowledge_owner_enrichment_closed_bounded`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; canonical next allowed move summary=hold for the post-AKOE operator checkpoint; parked checkpoint=implementation, provider/live, credentials, deployment and public sync. Role=Local orchestrator; phase=roadmap revision; final technical decision owner=Local; scope decision owner=operator.

Canonical bootstrap excerpt: `NEXT_ACTION_CLASS=HOLD_FOR_OPERATOR_CHECKPOINT_POST_AKOE`; `NEXT_STEP=OPERATOR_DECIDES_ANY_SUCCESSOR`; `EXPANSION_ALLOWED=false`. Đây là các trường trích từ nextAllowedMove, không phải toàn bộ giá trị. Tách biệt với trạng thái đó, operator đã yêu cầu tạo roadmap và nay cho phép sửa theo phản biện đã đối chiếu để review vòng hai. Quyền sửa tài liệu này không cập nhật bootstrap hoặc mở R0/runtime.

## Scope

- Trải nghiệm non-coder, hợp đồng công việc, lựa chọn agent/provider/model và kết nối tài khoản.
- Hai luồng bổ trợ: tiếp tục chuyển pattern có giá trị vào owner CVF; tích hợp năng lực upstream có chọn lọc để sử dụng thực tế.
- Quản lý nguồn, capability, adapter, môi trường chạy, dữ liệu, secret, bằng chứng và phục hồi.
- Lộ trình local pilot, VPS/cloud/hybrid, sử dụng từ nhiều nơi và bảo quản dữ liệu.
- Machine gate ở đúng ranh giới thực thi; tự động hóa điều phối/kiểm tra kỹ thuật và quản trị theo mức rủi ro.
- Các giai đoạn, điều kiện vào/ra, chỉ số nghiệm thu và quy tắc kiểm soát thay đổi.

## Non-Goals

- Không biến CVF thành IDE, no-code builder, model platform hoặc agent framework thay thế upstream. Trải nghiệm thuận tiện là lớp truy cập governance cho các công cụ đó.
- Không tải/copy mọi repository, tự viết lại mọi runtime, hoặc xây/mở rộng marketplace năng lực mới trước khi có use case được chứng minh. Route marketplace hiện có được giữ nguyên; đối chiếu ở R0, không bị xóa hay được cấp quyền mở rộng bởi roadmap này.
- Không ép provider/model, bán quyền truy cập thay upstream, đọc lén phiên đăng nhập hoặc coi subscription là API entitlement.
- Không kiểm soát suy luận nội bộ của agent, phiên làm việc ngoài CVF hoặc quyền sử dụng tài khoản riêng của user.
- Không tuyên bố đã kiểm soát toàn bộ agent khi chỉ nhận packet hoặc một phần sự kiện từ adapter.
- Không coi absorb pattern, contract, unit test hoặc demo mock là bằng chứng production/live readiness.
- Không sửa frozen doctrine hoặc thêm plane/owner song song để tránh đối chiếu owner hiện có.

## Design Control Gate

Các bất biến dưới đây là tiêu chí kiểm tra cho mọi tranche của roadmap, không thay thế authority cấp cao hơn.

| ID | Hướng cố định | Cách kiểm tra |
|---|---|---|
| I01 | Non-coder first | Luồng chính hoàn thành không cần sửa code/config, chạy terminal hay hiểu governance jargon |
| I02 | CVF độc lập, upstream thay thế được | Policy, job, data, evidence có định danh/schema CVF; adapter không trở thành nguồn thẩm quyền |
| I03 | Tự do chọn agent/provider/model/account | Hỗ trợ qua giao diện mở; công bố khả năng thực tế; không ép chuyển provider hoặc loại tài khoản |
| I04 | Chỉ kiểm soát công việc/tài nguyên trong phạm vi CVF | Ranh giới quan sát/enforcement được ghi rõ; hoạt động ngoài phạm vi không bị nhận vơ hoặc can thiệp |
| I05 | Giá trị sử dụng song hành với hấp thụ pattern | Mỗi tích hợp có user outcome, consumer, invocation và bằng chứng sử dụng, không chỉ sơ đồ kiến trúc |
| I06 | Quyền theo tác động, không theo tên repo | Cấp quyền tối thiểu cho tool/action, dữ liệu, môi trường, thời hạn và ngân sách |
| I07 | Kết quả được kiểm chứng, không tự chấp nhận | Worker completion là đầu vào review; công bố/gửi/xóa/chi tiền giữ checkpoint phù hợp |
| I08 | Portable và phục hồi được | Không gắn nguồn sự thật vào một laptop, đường dẫn tuyệt đối hoặc một cloud |
| I09 | Governance tương xứng | Tái dùng evidence hợp lệ; không bắt user xử lý lỗi cơ học hoặc duyệt lặp các bước rủi ro thấp |
| I10 | Không thăng cấp ngầm | Source reviewed, pattern absorbed, integrated, tested, enabled và production là các quyết định khác nhau |
| I11 | Tự động hóa không phụ thuộc người đứng xem | Dispatch đủ điều kiện mới giao worker; lỗi phải có owner, trạng thái, đường phục hồi và giới hạn retry |
| I12 | Bổ sung để đạt đích, không đổi đích ngầm | Mọi bổ sung chỉ ra invariant/use case/acceptance gap; đổi định hướng cần quyết định operator |

## Existing Baseline And Source Authority

Đây là đối chiếu các owner và bằng chứng đã có để lập kế hoạch, không phải kiểm kê đầy đủ hệ thống hoặc kết luận mọi consumer đã được wiring. Những thiếu hụt triển khai dưới đây là câu hỏi cần xác minh ở R0, trừ nơi nguồn đã tuyên bố contract-only.

| Nguồn/owner | Điều kế thừa | Ranh giới |
|---|---|---|
| `ECOSYSTEM/doctrine/CVF_PRODUCT_POSITIONING.md`, mục Mission / What CVF Is / What CVF Is NOT | CVF là governance infrastructure, bổ trợ framework và công cụ | UX non-coder không đổi CVF thành builder/framework |
| `ECOSYSTEM/operating-model/CVF_VOM_QUICK_START.md`; `ECOSYSTEM/operating-model/CVF_AGENT_OPERATING_MODEL.md` | Entry points để R0 đối chiếu luồng user và trách nhiệm agent | Không tạo operating model thứ hai |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` | Consumer UI hiện có: dashboard approvals, artifacts, workspace, runtime, skills, marketplace, history, governance; API providers, execute, sessions, integrations/test, approvals, artifacts/export | Đối chiếu và tái dùng trước thiết kế mới; có route/code không đồng nghĩa toàn tuyến đã chạy được hoặc đủ quyền runtime |
| `docs/corpus-intelligence/registry/entries/legacy-cvf-app-onboarding.json`, trường scopePaths[0] là locator thư mục App onboarding trong kho legacy | UI design reference legacy; registry ghi NOT_STARTED; dùng để đối chiếu mockup khi phù hợp | Dùng locator canonical trong registry, không thư mục App onboarding ở repo root; không coi mockup là active design authority hoặc capability đã nghiệm thu; DESIGN.md và owner hiện hành vẫn điều khiển |
| `docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md`; `docs/reviews/CVF_ACEL_AKOE_P4_COMMON_LOCAL_RECONCILIATION_COMPLETION_2026-09-26.md` | AKOE đóng bounded; 19 candidate thuộc sáu nguồn: 5 ADAPT, 8 CONFIRMED_EXISTING, 3 DEFER_WITH_TRIGGER, 2 REJECT_DIRECT_IMPORT, 1 source-blocked | Không suy ra toàn bộ repo đã đọc hoặc capability đã chạy live |
| `EXTENSIONS/CVF_MODEL_GATEWAY/README.md`; `docs/reference/model_gateway/README.md` | Gateway owner cho provider, routing, credential và receipt | Tái dùng, kiểm tra consumer/support matrix; không khẳng định mọi login subscription đã có |
| `docs/reference/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md`, Purpose / S1 | Đã có contract tiếp nhận skill/MCP/CLI/repo/database | Contract nói rõ Phase A; runtime enforcement cần authority riêng |
| `docs/reference/agent_system_skills/CVF_ASSF_BEHAVIORAL_EVALUATION_CONTRACT.md`; `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | Judgment, evaluation, promotion evidence | Không tự kích hoạt skill hoặc tự nâng quyền |
| `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Owner để đối chiếu adapter/readout ngoài host | Readout không đồng nghĩa interception |
| `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | Runtime/launcher owner hiện có | Không xây scheduler thứ hai trước khi xác định gap |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | Tách workspace skeleton, read model và runtime | Skeleton không cấp quyền mở daemon/dispatcher/UI |
| `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_WORKFLOW_CHAIN_2026-06-05.md` | Entry points để kiểm tra storage/durability trước khi chọn backend | Không coi tên contract là bằng chứng hệ thống backup/cloud đã vận hành |
| `DESIGN.md`; `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | UX và governance theo mức công việc | Tối giản trải nghiệm, không bỏ kiểm soát cần thiết |

UI locators để bắt đầu R0: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/marketplace/page.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/providers/route.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingWizard.tsx`. Marketplace page hiện gọi TemplateMarketplace; chưa có cơ sở coi đây là marketplace thực thi capability mới của roadmap. Giữ route hiện tại, chỉ thay đổi consumer được chọn sau khi có gap và scope cụ thể.

### Sáu nguồn đã thảo luận và lane Unreal

| Nhóm | Giá trị đã có trong baseline AKOE | Hướng dùng tiếp, chưa phải activation |
|---|---|---|
| Jev / TypeSafe skills | Judgment context, candidate space, no-match và evidence-only | Bổ trợ chọn capability và đánh giá; không dùng confidence để cấp quyền |
| WikiSkill | Proposal, strict improvement, impact và rollback evidence | Cải tiến skill có đánh giá và version; không tự sửa policy hoặc tự promote |
| HyperFrames | Artifact graph, scope, batch và assembly/completion | Ứng viên vertical slice tạo sản phẩm media; phải kiểm tra dependency, resource và consumer thực |
| Human Boundary handoff | Phân biệt làm, kiểm tra, chấp nhận, trách nhiệm | Thiết kế checkpoint dễ hiểu, tránh người dùng chỉ bấm duyệt máy móc |
| Positioning handoff | Giữ CVF là lớp governance độc lập | Tích hợp upstream bằng adapter; không nhập bản sắc/authority của upstream |
| Async handoff | CVF-native durable-run correction và offline composition | Đối chiếu restart, retry, cancel, ownership và trạng thái công việc |
| ACEL-AKOE-U1 / Unreal Agent | Mã/phạm vi read-only do operator nêu trong hội thoại; chưa có packet/continuity tương ứng để viện dẫn làm active dispatch | Pin mục tiêu `unreallabsai/unreal-agent@1b9f778`; không phải nguồn thứ bảy của ledger AKOE cũ; mirror không thay thế Local acceptance |

U1 là cách gọi tắt của phạm vi operator đã nêu trong hội thoại: "intake Local read-only", chỉ pin/license/source verification và reconciliation; không import code hoặc sửa runtime. Session canonical vẫn gọi đây là optional Unreal source intake đang parked. Cần đối chiếu và ghi nhận chỉ đạo đó vào packet/continuity theo quy trình trước khi dispatch hoặc tiếp tục tác vụ nguồn; không suy từ thiếu mã tracked rằng operator chưa từng chỉ đạo, cũng không dùng đoạn roadmap này thay release authority. Lần sửa hiện tại không mở hoặc tiếp tục U1. Nếu câu hỏi nguồn còn thiếu, dùng relay Web hiện có với câu hỏi cụ thể, pin, locator và điều kiện trả về. Local quyết định cuối cùng. Không để U1 chặn một pilot độc lập không dùng Unreal; không sửa ngược lịch sử source-blocked của AKOE chỉ vì có thêm nguồn sau này.

### Nhóm use case ưu tiên sau nâng cấp

Sau khi các phần nền tảng của CVF cần cho roadmap này được nâng cấp và tranche tương ứng được operator mở, chính các repository/capability đã tạo ra evidence AKOE sẽ là nhóm use case ưu tiên: Jev / TypeSafe skills cho đánh giá và chọn năng lực; WikiSkill cho cải tiến skill có proposal/impact/rollback; HyperFrames cho artifact graph và quy trình tạo sản phẩm; Unreal Agent chỉ được cân nhắc sau Q002 và Local disposition. Mục tiêu là chứng minh CVF có thể dùng năng lực cộng đồng thật qua owner/adapter hiện có, đồng thời giữ ranh giới quyền, evidence và khả năng thay thế upstream.

Đây là thứ tự ưu tiên để R0 chọn một vertical slice, không phải lệnh kích hoạt toàn bộ repo, import code hoặc chạy đồng thời bốn hệ thống. R0 vẫn phải xác minh consumer, license, dependency, resource, auth và mức L1/L2/L3 của từng use case; chỉ một slice nhỏ nhất được chọn trước. Kết quả của slice đầu tiên quyết định việc mở use case tiếp theo.

## Target Operating Model

### Hành trình người dùng

1. Người dùng mô tả kết quả muốn đạt và đưa tài liệu cần dùng.
2. CVF cùng agent tóm tắt kết quả dự kiến, phạm vi dữ liệu, chi phí có thể phát sinh và tác động cần xin phép.
3. Người dùng chọn tài khoản/agent đã kết nối hoặc dùng lựa chọn đã lưu; cài đặt nâng cao được mở khi cần.
4. Agent thực hiện phần đã được ủy quyền. Người dùng thấy tiến độ có ý nghĩa, có thể tạm dừng/hủy hoặc bổ sung yêu cầu.
5. CVF trình bày bản xem trước, kiểm tra nào đã qua, giới hạn còn lại và thay đổi so với phiên bản trước.
6. Người dùng yêu cầu sửa bằng ngôn ngữ tự nhiên, chấp nhận kết quả hoặc thực hiện hành động có tác động như xuất bản.
7. Kết quả, lịch sử và điểm phục hồi được lưu; chuyển thiết bị không làm mất công việc.

Ví dụ lời hỏi phù hợp: "Cho phép dùng các ảnh đã chọn để tạo bản nháp video? Chưa đăng lên mạng." Không hỏi người dùng chọn mutex, sửa schema hay tìm material SHA. Khi cần gửi dữ liệu ra ngoài phải nói nơi nhận, loại dữ liệu và lựa chọn từ chối.

User view ưu tiên: "Đang làm", "Cần bạn quyết định", "Có bản xem trước", "Chưa xác định được kết quả", "Có thể thử lại". Mã trạng thái kỹ thuật nằm trong chi tiết chẩn đoán. Không che lỗi dưới thông báo thành công.

### Phân công trách nhiệm

| Thành phần | Trách nhiệm | Không sở hữu |
|---|---|---|
| User/operator | Mục tiêu, lựa chọn tài khoản, quyền, ngân sách, quyết định có tác động | Không phải người sửa lỗi gate cơ học hoặc kiểm chứng code thay reviewer |
| Agent | Hiểu yêu cầu, lập kế hoạch, chọn tool trong phạm vi, thực hiện và sửa lỗi được phép | Không tự tăng quyền, tự xác nhận độc lập hoặc tự công bố |
| CVF | Job contract, resource boundary, policy/evidence/acceptance, trạng thái và khả năng phục hồi | Không sở hữu suy luận riêng hay quyền subscription của agent/user |
| Upstream capability/runtime | Năng lực chuyên biệt qua giao diện được khai báo | Không quyết định policy, trust hoặc acceptance của CVF |
| Reviewer/verifier | Kiểm tra kết quả theo rủi ro và bằng chứng | Không lặp toàn bộ công việc worker khi không có mâu thuẫn cụ thể |

Orchestrator/worker/reviewer/learning là trách nhiệm logic, không bắt buộc bốn agent cho mỗi việc. Việc đơn giản có thể dùng một agent và kiểm tra xác định; công việc có rủi ro cần sự độc lập theo owner hiện hành. CVF quy định scope, quyền, evidence và kết quả, không quy định chain-of-thought, prompt nội bộ hay thứ tự suy nghĩ của agent.

### Ba mức kết nối, ba mức bảo đảm

| Mức | Cách dùng | CVF có thể kiểm soát | Phần phải công khai là ngoài bảo đảm |
|---|---|---|---|
| L1 Packet relay | Gửi nhiệm vụ, nhận kết quả thủ công hoặc qua host | Hợp đồng đầu vào, tính hợp lệ và review kết quả nhận về | Không chặn được tool/action bên trong agent ngoài CVF |
| L2 Adapter-connected | Host/CLI/API/MCP adapter có giao diện quan sát và điều khiển | Những event/action thực sự đi qua adapter, theo support matrix | Tool bên ngoài adapter hoặc event không được host cung cấp |
| L3 Managed execution | Worker chạy trong môi trường cô lập có gateway tài nguyên | Quyền filesystem/network/process được enforcement tại boundary đã kiểm thử | Không mở rộng bảo đảm sang tài khoản/ứng dụng khác; không mặc định container đủ chống mọi bypass |

Không hạ từ L3 xuống L1 âm thầm khi kết nối lỗi. Giữ trạng thái chưa hoàn thành, giải thích mức kiểm soát thay đổi và chỉ tiếp tục nếu policy cùng user cho phép. Tên mức là vocabulary thiết kế của roadmap; R0 ánh xạ vào enum/owner đang có trước khi đưa vào code.

## Provider, Model And Account Freedom

- Đường kết nối dự kiến: API key/custom endpoint; đăng nhập subscription qua luồng chính thức khi provider/host hỗ trợ; CLI/agent host đã đăng nhập hợp lệ; local/self-hosted model.
- Quyền subscription và API là hai khả năng cần xác minh riêng. Không hứa mọi subscription dùng được trong gateway API, không trích cookie/token riêng tư để giả lập hỗ trợ.
- User chọn provider/model, nơi xử lý dữ liệu và tài khoản. CVF chỉ áp dụng các giới hạn công việc, tài nguyên và chính sách workspace mà user đã biết/chấp thuận.
- Nếu một provider không phù hợp policy của một job, giải thích xung đột và các lựa chọn; không khóa quyền dùng provider đó bên ngoài CVF.
- Không fallback ngầm sang model/provider khác hoặc từ subscription sang API có phí. Chỉ dùng fallback đã được user cấu hình, với phạm vi dữ liệu và trần chi phí tương ứng.
- Support matrix phải tách provider, model, auth mode, host/version, OS, tools, cancellation, usage reporting, streaming, session resume và mức L1/L2/L3. Không có bằng chứng thì ghi chưa hỗ trợ/chưa kiểm chứng.
- Secret tách theo user/workspace/connection; inject qua secret reference, quyền tối thiểu, log đã che, có revoke/rotation. Không lưu raw key trong job, Git, artifact hay prompt.
- Chuyển cloud không tự sao chép phiên đăng nhập laptop. Dùng re-auth/delegation được hỗ trợ; công bố khi upstream bắt buộc tương tác người dùng.
- Usage/cost không quan sát được phải ghi "chưa đo được", không ghi 0 hoặc bịa hạn mức. Trước mỗi adapter mới, kiểm tra tài liệu chính thức hiện hành; roadmap không chứng nhận provider cụ thể.

## Capability And Source Management

### Tải gì, đặt ở đâu

| Loại | Cần local download? | Cách quản lý |
|---|---|---|
| Skill | Thường cần nội dung instruction và tài nguyên/script mà host sử dụng | Version/pin, instruction review, dependency và quyền của script; skill không phải sandbox |
| Local MCP / CLI | Cần executable/package/container ở môi trường worker | Pin/digest, build/install có kiểm soát, giới hạn tools và egress |
| Remote MCP / API | Không cần tải server về CVF | Endpoint, auth, tool schema, data policy, timeout và support matrix |
| Upstream runtime | Chỉ cài phần runtime cần cho use case được chọn | Adapter, môi trường riêng, compatibility và rollback |
| Source phục vụ audit | Mirror read-only theo quy trình nguồn hiện có | Pin/license/locator, phân biệt source audit với dependency runtime |

Ba lớp logic: source mirror để đối chiếu; registry để quản lý capability được biết/được phép; execution environment để chạy bản đã chọn. Không dùng source mirror trực tiếp như runtime mutable. "Không tải mọi repo để vận hành" không bãi bỏ quy tắc Local source acquisition cho repo thực sự đã vào chương trình nghiên cứu.

Registry tái dùng owner hiện có; tối thiểu phải ánh xạ được: capability ID, user outcome, source/license/pin/digest, adapter/transport, schema input-output, dependency, OS/resource, auth, quyền và egress, data retention, test receipt, support level, owner, activation/revocation và rollback version. Các trường chưa có chỉ bổ sung khi R0 chứng minh gap.

Trạng thái nguồn và trạng thái sử dụng là các trục độc lập: source-reviewed không có nghĩa integrated; pattern-absorbed không có nghĩa installed; pilot-passed không có nghĩa user-enabled; suspended không xóa provenance. Không gộp thành một badge "đã absorb, dùng được".

Version mới không được tự thay version đang chạy. Upgrade phải đánh giá schema/quyền/license/dependency thay đổi, chạy compatibility test và cho phép rollback. Prompt injection từ skill/repo/tool output là dữ liệu không đáng tin; không được sửa policy, yêu cầu đọc secret hoặc mở quyền chỉ bằng nội dung instruction.

## Execution, Isolation And Machine Gates

- Job có ID ổn định, scope, input/output contract, capability version, quyền, budget, checkpoint và terminal outcome. UI đọc projection, không là nguồn sự thật thay receipt/ledger.
- Trước side effect phải có intent/admission bền vững theo owner. Dùng idempotency khi downstream hỗ trợ; không hứa exactly-once cho mọi dịch vụ.
- Restart/retry cần lease/ownership, timeout, retry budget và reconciliation. Nếu timeout sau khi có thể đã gửi/xuất bản/thanh toán, chuyển sang kết quả chưa xác định và kiểm tra downstream trước khi thử lại.
- Cancel là yêu cầu cần phản hồi: phân biệt dừng trước tác động, đang dừng, đã có tác động. Rollback dữ liệu nội bộ khác compensation cho tác động ngoài; email đã gửi không thể "undo" bằng khôi phục Git.
- Worker chỉ ghi vùng được giao. Policy, secret store, evidence đã chấp nhận và backup không nằm trong quyền ghi của worker.
- Mỗi worker dùng workspace/worktree tách biệt; có một integrator chịu trách nhiệm hợp nhất. Cấm dùng shared-worktree stash, reset hoặc cleanup để cô lập việc của mình khi có thay đổi người khác.
- Gate tĩnh kiểm tra packet/schema không thay thế runtime enforcement. Quyền phải được kiểm tra ở nơi tài nguyên được truy cập; thử bypass bằng đường dẫn, subprocess, network và adapter khác trong phạm vi môi trường.
- Dispatch không được hiện "sẵn sàng" trước khi packet được commit, dependency release thỏa, continuity marker/read model đồng bộ và pre-dispatch gate qua. Đối chiếu checker hiện có trước khi thêm gate mới.
- Không đẩy lỗi orchestrator như thiếu marker/packet chưa commit xuống worker hoặc non-coder. Orchestrator sửa phần cơ học trong phạm vi của mình, có retry ceiling; vượt thẩm quyền thì lưu blocker và thông báo người có quyền.
- Khi không có user online: tiếp tục phần đã được ủy quyền; checkpoint có tác động phải pause an toàn, lưu trạng thái, gửi thông báo theo kênh đã cấu hình. Không tự duyệt thay user để tránh "treo".

## Portability, Data Protection And Deployment

### Cấu trúc mục tiêu

Tách logic giao diện user, control services, worker/executor, durable job state, artifact storage, secret store và backup. Đây là trách nhiệm triển khai, không phải quyết định tạo thêm bảy CVF plane.

- Bắt đầu local với một workload nhỏ. Giữ ID/path logic, config môi trường và interface storage rõ ràng ngay từ đầu; không hard-code ổ D: hoặc phụ thuộc phiên desktop.
- Chọn backend sau khi kiểm tra owner/consumer: PostgreSQL và object storage tương thích S3 là phương án đánh giá, không phải quyết định rewrite hay tuyên bố đã có.
- Ưu tiên deployment đơn giản, một host/Compose nếu phù hợp pilot; không đặt Kubernetes làm điều kiện tiên quyết. Windows-specific tool có thể giữ worker Windows riêng khi control services lên VPS.
- VPS/cloud/hybrid giữ cùng job/evidence contract. Mỗi OS cần kiểm chứng quyền thực tế; không coi Windows ACL và Linux permission/container policy tự tương đương.
- Truy cập từ nhiều nơi qua kết nối bảo mật, xác thực, phân quyền workspace và quản lý phiên; yêu cầu MFA cho quản trị/đường truy cập nhạy cảm theo khả năng hệ thống.
- Laptop tắt: cloud worker có thể tiếp tục job đã chuyển đúng cách; job cần local worker phải báo chờ thiết bị, không giả vờ đang chạy trên cloud.
- Xuất dữ liệu/artifact/schema ở định dạng được mô tả; có đường rời provider/cloud, không giữ dữ liệu user trong adapter độc quyền.

### Backup không đồng nghĩa sync hoặc đặt trên cloud

Giữ bản sao được mã hóa và tách khỏi quyền worker, có version/retention, tối thiểu một vị trí độc lập với máy/host đang chạy. Đánh giá immutable backup khi nền tảng hỗ trợ. Đồng bộ lỗi/xóa sang cloud không được coi là phục hồi.

Phạm vi backup: durable state, artifact được chấp nhận, cấu hình/policy/version, metadata capability, evidence và source/build artifact cần để tái tạo bản đã pin. Mirror bị Git ignore không tự được bảo vệ bởi provenance Git. Secret có cơ chế bảo quản riêng; recovery key không chỉ nằm cùng bản backup đã mã hóa.

RPO/RTO đề xuất cho pilot: artifact đã chấp nhận phải có bản sao bền vững trước thông báo "đã lưu an toàn"; với job/config đang thay đổi, mục tiêu RPO <= 24 giờ và RTO <= 4 giờ trong diễn tập. Đây là mục tiêu cần R0 xác nhận theo chi phí và dữ liệu, chưa phải SLA. Dữ liệu cần bảo vệ nghiêm ngặt hơn phải đặt mục tiêu riêng trước sử dụng.

Restore drill phải dùng môi trường sạch, kiểm tra snapshot/manifest nhất quán giữa DB-artifact-evidence, quyền, khả năng mở artifact và resume an toàn. Có backup mà chưa thử restore không đạt gate di chuyển.

Cutover: drain/pause job phù hợp, snapshot, chuyển state, chỉ một writer/lease có hiệu lực, revoke hoặc fence worker cũ, kiểm tra kết quả chưa xác định rồi mới nhận job mới. Rollback xét tương thích schema và dữ liệu mới; không bật lại cả hai phía hoặc copy DB cũ đè kết quả mới.

## Work Plan

Mọi giai đoạn dưới đây hiện là PLANNED_NOT_DISPATCHED. Các bước cùng giai đoạn là gói công việc để tạo work order giới hạn, không phải lệnh thi công sẵn. Thời gian/ngân sách được chốt theo slice ở R0; không đặt lịch hoàn thành giả khi chưa biết provider, workload và hạ tầng.

### R0 - Chốt consumer, owner và pilot nhỏ nhất

- ID: NCR-R0. Vai trò: orchestrator + Local reviewer. Đầu vào: roadmap này và evidence AKOE hiện có.
- Việc làm: lần theo một luồng user đến consumer thực; phân loại owner đã có/contract-only/wiring chưa rõ/gap đã chứng minh; đối chiếu catalog và system-chain GAP hiện có, không tạo inventory cạnh tranh.
- Điểm xuất phát UI là cvf-web hiện có: approvals, artifacts, workspace, runtime, skills, marketplace, history, governance và các API providers, execute, sessions, integrations/test, approvals, artifacts/export. Lần theo route/component/service/owner của luồng được chọn; ghi reuse/change/defer và bằng chứng cho từng đoạn liên quan, không audit lại toàn web platform. Đối chiếu mockup legacy ở đúng path trong bảng baseline, không thăng cấp mockup thành authority.
- Chọn một use case có giá trị non-coder, input dễ giới hạn, đầu ra xem trước được, ít side effect. Ứng viên: tạo một artifact nội dung/media ngắn bằng capability sẵn có; HyperFrames chỉ được chọn khi điều kiện dependency/license/resource phù hợp. Không mở nhiều demo cùng lúc.
- Chốt provider/auth đầu tiên từ kết nối user muốn dùng và host hỗ trợ; ngân sách chi phí/retry, dữ liệu mẫu, metric, threat model và RPO/RTO. Lựa chọn đầu tiên không trở thành khóa provider dài hạn.
- U1 chỉ được đối chiếu về chỉ đạo read-only và phần packet/continuity còn thiếu; không tự mở intake. Câu hỏi Web chỉ mở khi quyết định pilot/owner thực sự phụ thuộc câu trả lời và có task-bound authority.
- Chốt kế hoạch người thử theo Q003: nguồn tuyển, người phụ trách, consent, dữ liệu mẫu và retention trước khi mời/chạy thử; đây là dependency thật của nghiệm thu non-coder, không giao agent giả làm người dùng.
- Đầu ra: bảng owner-consumer-gap có locator; acceptance scenario; scope/effect envelope; danh sách quyết định còn mở; packet cho R1 hoặc tranche nhỏ hơn theo routing hiện hành.
- Nghiệm thu/exit: một kết quả user rõ, các đoạn chưa wiring rõ, zero duplicate owner không có lý do. Không cần quét lại toàn bộ corpus. Dừng nếu chỉ còn lý do "repo nổi tiếng" mà không có user outcome.

### R1 - Hợp đồng job và trải nghiệm non-coder

- ID: NCR-R1. Phụ thuộc: R0 chọn use case. Vai trò: product/UX worker và contract reviewer.
- Việc làm: map goal, input, preview, sửa, accept, cancel, pending approval, lỗi và recovery vào owner workspace/operating model hiện có; dùng progressive disclosure theo DESIGN.md.
- Bắt đầu từ route/component, OnboardingWizard và consumer đã đối chiếu ở R0; tham khảo mockup legacy khi còn phù hợp. Chỉ thiết kế delta thiếu, không tạo dashboard/chooser/approval flow song song. Đầu ra phải ghi rõ phần tái dùng, phần sửa và lý do.
- Hoàn thiện capability card và provider/account chooser trên surface đã chọn; hiển thị mức kiểm soát, dữ liệu gửi ra ngoài, chi phí biết/chưa biết; không yêu cầu user nhập enum hay đọc log.
- Đầu ra: flow/prototype, job/evidence field mapping, support matrix ban đầu và kiểm thử ngôn ngữ/tính dễ hiểu.
- Nghiệm thu: người dùng thử giải thích được kết quả sắp tạo, quyền sắp cấp và tác động chưa thực hiện. Mock chỉ chứng minh cấu trúc UI, không governance behavior.
- Exit: UX và contract đủ dùng cho đúng một slice. Không viết lại agent host; không mở credential/live trong giai đoạn này nếu chưa được cấp riêng.

### R2 - Adapter và execution boundary tối thiểu

- ID: NCR-R2. Phụ thuộc: R1. Vai trò: integration worker; reviewer độc lập theo rủi ro.
- Việc làm: cài/đóng gói đúng capability được duyệt; nối adapter vào gateway/admission/execution owners; job workspace riêng; permission/secret references; durable intent; receipt và cancel semantics.
- Chọn L2 hoặc L3 theo khả năng host; L1 có thể giữ như lựa chọn tương thích nhưng không được dùng để nghiệm thu enforcement của L3.
- Đầu ra: consumer gọi được adapter, registry mapping, supported-version record, threat/negative tests, uninstall/revoke và rollback bản trước.
- Nghiệm thu: chặn ngoài scope, thiếu approval/secret, pin sai, input lỗi và event giả; worker không sửa policy/evidence đã chấp nhận; retry/timeout không tự tạo duplicate effect.
- Exit: offline integration và isolation test phù hợp đã qua, đủ điều kiện xin một live pilot giới hạn. Gate fail thì giữ capability disabled; không bypass để chạy demo.

### R3 - Vertical slice thực, kết quả user thực

- ID: NCR-R3. Phụ thuộc: R2 và authority riêng cho provider/live, credential, dependency và effect cần thiết.
- Việc làm: chạy toàn tuyến user goal -> selected agent -> admitted capability -> artifact -> verification -> preview -> user acceptance. Dùng đúng provider/auth được chọn và input an toàn; không công bố ra ngoài mặc định.
- Đầu ra: artifact mở được, receipt gắn run/version/input/output, chi phí thực hoặc UNKNOWN, giới hạn mức kiểm soát và kết quả kiểm thử non-coder.
- Nghiệm thu: user tạo rồi sửa sản phẩm bằng lời tự nhiên, không cần terminal; refresh UI không mất job; denial/cancel được giải thích; không có fallback hoặc side effect ngầm.
- Governance behavior phải có real-provider proof theo chuẩn hiện hành. Release-quality proof dùng `python scripts/run_cvf_release_gate_bundle.py --json` dưới authority tương ứng; thất bại/timeout phải diagnostic trước retry. Receipt cũ không thay proof mới.
- Exit: một use case dùng được với claim bounded. Nếu auth subscription không hỗ trợ, ghi giới hạn và xin user chọn đường khác; không lén dùng API trả phí.

### R4 - Pilot local bền vững và chứng minh khả năng thay thế

- ID: NCR-R4. Phụ thuộc: R3. Vai trò: reliability/integration worker và reviewer.
- Việc làm: restart/crash/reconnect/duplicate submission/unknown-effect recovery; cap concurrency; kiểm tra workspace chéo; backup/restore lần đầu; resume từ thiết bị khác trong phạm vi đã cấu hình.
- Kiểm tra cùng job contract với ít nhất hai kết nối độc lập khả dụng. Mục tiêu có API và official account/host mode; nếu chưa có luồng account được hỗ trợ, giữ phần đó pending với evidence, không tuyên bố đủ tự do kết nối.
- Đầu ra: test matrix có fault injection, measured latency/cost, restore receipt, support matrix cập nhật và onboarding/recovery hướng dẫn bằng tiếng Việt.
- Nghiệm thu: không mất artifact đã nhận; không duplicate tác động ở các tình huống đã định nghĩa; user hiểu điểm cần quyết định; không yêu cầu đọc log để dùng bình thường.
- Exit: pilot local ổn định trong bộ scenario đã chốt. Không dùng một lần chạy thành công để kết luận production.

### R5 - VPS/cloud/hybrid, truy cập mọi nơi và bảo quản data

- ID: NCR-R5. Phụ thuộc: R4; operator chọn host, ngân sách, vùng dữ liệu, quyền deployment và phương án secret.
- Việc làm: triển khai profile portable, remote authentication, workspace isolation, encrypted backup độc lập; thực hiện restore từ môi trường sạch và cutover một-writer.
- Đầu ra: deployment/config profile tái tạo được, migration/rollback runbook, data export, cost/retention policy, restore/cutover evidence và health/alert vận hành.
- Nghiệm thu: người dùng mở và tiếp tục công việc từ máy khác; laptop tắt không làm mất cloud job; local-dependent job báo đúng; mất host vẫn phục hồi trong mục tiêu đã chọn.
- Exit: bounded hosted pilot được chấp nhận. Public endpoint, production hoặc public catalog chỉ mở khi có authority/gate riêng; không suy ra từ việc VPS đã chạy.

### R6 - Mở rộng capability có chọn lọc và cải tiến có kiểm chứng

- ID: NCR-R6. Phụ thuộc: R3-R5 đủ bằng chứng cho môi trường của capability mới; không bắt capability local chờ toàn bộ cloud rollout.
- Việc làm: thêm từng capability theo nhu cầu user; reuse intake/source ledger và adapter conformance suite; quản lý upgrade, deprecate, revoke, usage và hỗ trợ.
- Jev hỗ trợ evidence cho chọn/đánh giá; WikiSkill hỗ trợ proposal cải tiến có kiểm tra tác động/rollback; không tự promote. Cân nhắc Unreal chỉ khi U1 đã có Local disposition và use case yêu cầu.
- Đầu ra: mỗi capability có người dùng/consumer, owner, support level, receipt và rollback; catalog phân biệt tested/enabled/deferred.
- Nghiệm thu: năng lực mới cải thiện user outcome đo được, không phá invariant hoặc tạo owner trùng. Chỉ tăng concurrency/số nguồn theo khả năng review và vận hành.
- Exit: từng capability đóng bounded; chương trình không biến thành nghiên cứu vô hạn. Không xây/mở rộng marketplace năng lực, Kubernetes hoặc new plane nếu chưa có quyết định riêng dựa trên nhu cầu; route marketplace hiện có giữ disposition đã nêu trong baseline.

## Acceptance Criteria

Các số dưới đây là mục tiêu đề xuất cho pilot, phải chốt trước R3 và giữ nguyên trong một đợt đo. Điều chỉnh phải có lý do, không hạ ngưỡng sau thất bại rồi gọi PASS.

Q003 phải được giải quyết trước thử nghiệm có người tham gia, kể cả ở R1: operator chỉ định người phụ trách tuyển và phê duyệt nguồn tuyển; người thử biết mục tiêu, dữ liệu được thu và có quyền từ chối/dừng. Mặc định dùng dữ liệu mẫu không nhạy cảm, không thu credential; chỉ ghi hình/ghi âm nếu có đồng ý riêng. Kế hoạch chốt nơi lưu, người được truy cập, thời hạn giữ/xóa và cách xử lý yêu cầu rút dữ liệu. Chưa tuyển đủ thì A01 là NOT_EVALUATED, không PASS; có thể làm proof kỹ thuật đã được phép nhưng không kết luận pilot đạt nghiệm thu non-coder hoặc tăng quy mô dựa trên kết quả đó.

| ID | Tiêu chí | Bằng chứng cần |
|---|---|---|
| A01 | Ít nhất 5 người dùng non-coder thử luồng chính; >= 80% hoàn thành tạo/sửa/accept không cần hỗ trợ kỹ thuật | Script cố định, quan sát thực, ghi rõ hỗ trợ đã dùng; mẫu nhỏ không đại diện toàn thị trường |
| A02 | Zero yêu cầu dùng terminal/sửa config trong luồng chính được nghiệm thu | Session usability; onboarding nâng cao được tách riêng |
| A03 | Trước tác động nhạy cảm, mọi người thử giải thích đúng việc sắp xảy ra và cách từ chối | Comprehension check; không chỉ đếm nút đã bấm |
| A04 | Có đầu ra thực mở được, sửa được, gắn đúng input/run/version | Live bounded receipt + artifact verification |
| A05 | Không có write/egress/spend ngoài scope trong bộ negative tests | Enforcement test tại boundary thực; không suy rộng thành an toàn tuyệt đối |
| A06 | Timeout/crash/cancel không dẫn đến retry mù hoặc mất quyền sở hữu run | Fault scenarios, unknown-result reconciliation, lease/fencing evidence |
| A07 | Đổi kết nối được mà không đổi hợp đồng user/job | Hai adapter/connection conformance receipts; auth giới hạn được công bố |
| A08 | Không lộ secret trong log/artifact/export; revoke có hiệu lực theo semantics đã công bố | Secret-safe inspection và negative/revocation test |
| A09 | Phục hồi được dữ liệu/job trên môi trường sạch | Restore drill đạt RPO/RTO đã chốt, kiểm tra artifact và tính nhất quán |
| A10 | UI có trạng thái rõ, thao tác bằng bàn phím, tiếng Việt dễ hiểu và layout phù hợp màn hình nhỏ | UX/accessibility check theo DESIGN.md; không tuyên bố certification khi chưa audit |
| A11 | Không cần user quan sát để sửa lỗi dispatch cơ học | Packet release/continuity preflight; retry ceiling; blocker/notification drill |
| A12 | Governance không triệt tiêu giá trị sử dụng | Đo time-to-first-preview, success rate, review overhead và tổng cost; so với baseline R0 trước quyết định scale |

Time-to-first-preview phải tách thời gian setup, provider và governance. Ngưỡng latency/cost cụ thể phụ thuộc workload R0, chưa có số đo thì ghi UNKNOWN. Track tỷ lệ cần trợ giúp, retry/rework, false block, recovery success và giá trị artifact được user chấp nhận; không dùng số packet/test/repo làm proxy duy nhất cho giá trị.

## Risks And Stop Conditions

| Rủi ro | Cách xử lý / điều kiện dừng |
|---|---|
| UI quá nhiều thuật ngữ khiến non-coder trở thành operator kỹ thuật | Dừng scale, sửa flow và kiểm thử lại A01-A03; không giải quyết bằng thêm hướng dẫn dài |
| Adapter không quan sát/chặn được tool của host | Hạ claim về mức đã chứng minh, xin lựa chọn khi mức bảo đảm đổi; không dán nhãn L3 |
| Upstream license/auth/version không phù hợp | Disable candidate; giữ provenance và chọn phương án khác, không workaround credential |
| Capability bị prompt injection hoặc supply-chain change | Pin, review delta, hạn quyền, verify digest và quarantine/revoke |
| Recovery tạo tác động trùng hoặc state split-brain | Dừng effect mới, giữ evidence, reconcile; không tự retry vô hạn |
| Cloud làm tăng chi phí/lộ dữ liệu | Budget/egress/retention rõ; user quyết định data region và connection; không log secret |
| Bổ sung governance liên tục nhưng không có consumer | Trả việc về use case và owner gap; không mở checker/plane mới chỉ để quản lý tài liệu |
| Worker bị mất thay đổi do thao tác chung worktree | Cô lập workspace; integrator duy nhất; cấm stash/cleanup ảnh hưởng công việc khác |

## Change Control And Direction Preservation

Mỗi đề xuất bổ sung phải ghi ngay tại change log của roadmap: ID, vấn đề/bằng chứng, invariant/acceptance liên quan, owner hiện có, phần thay đổi, phần giữ nguyên, dependency/cost, phép thử và điều kiện rollback. Không bắt buộc tạo một tài liệu governance mới cho mỗi chi tiết.

- Loại A - làm rõ/sửa lỗi trong hướng đã chọn: bổ sung negative case, UX copy, compatibility hoặc repair trong scope hiện có. Local xử lý trong thẩm quyền, lưu rationale và evidence.
- Loại B - thêm capability/environment/permission hoặc tăng chi phí/phạm vi dữ liệu: operator chọn scope mới; work order giới hạn riêng trước thực thi.
- Loại C - đổi đối tượng user, định vị, authority hierarchy, provider freedom hoặc bất biến: không coi là cải tiến thường lệ; cần quyết định operator và quy trình owner cấp cao tương ứng. Roadmap không được tự sửa doctrine.

Không đổi thứ tự chỉ vì công nghệ mới hấp dẫn. Có thể điều chỉnh trình tự nếu vẫn giữ prerequisite an toàn và rút ngắn đường tới user outcome; ghi rõ dependency được thay thế bằng evidence nào. Deferred phải có trigger và owner; bị block một capability không tự block mọi capability độc lập.

### Decision And Change Log

| ID | Ngày | Quyết định / trạng thái | Lý do / bước tiếp |
|---|---|---|---|
| D001 | 2026-09-26 | Hướng non-coder + capability reuse + CVF-independent governance | Tổng hợp yêu cầu operator; I01-I12 là mốc đối chiếu |
| D002 | 2026-09-26 | Local là pilot, portability/backup từ thiết kế đầu | Không khóa dữ liệu vào laptop; cloud triển khai sau proof phù hợp |
| D003 | 2026-09-26 | Provider/model/account do user chọn; hỗ trợ dựa trên giao diện chính thức | Không hứa login chung cho mọi nhà cung cấp |
| D004 | 2026-09-26 | Authoring only; R0-R6 chưa dispatch | Không chuyển yêu cầu viết roadmap thành quyền runtime |
| D005 | 2026-09-26 | Version 1.1, Loại A: sửa theo F1-F7 sau Local đối chiếu, chờ review vòng hai | Giữ I01-I12 và R0-R6; thêm consumer UI, làm rõ authority/evidence và dependency người thử; không tăng quyền thực thi |
| D006 | 2026-09-26 | ACCEPTED_DIRECTION_PARKED; R2 chấp nhận F1-F7, N1/N2 đã sửa và gate chạy lại | Lưu roadmap và hai review; dùng Jev/TypeSafe skills, WikiSkill, HyperFrames và Unreal có điều kiện làm nhóm use case ưu tiên sau nâng cấp; không mở R0/runtime từ commit này |
| Q001 | OPEN_R0 | Chọn pilot, provider/auth, budget, metric, RPO/RTO | Local đề xuất dựa owner/consumer; operator quyết định phần tác động/chi phí |
| Q002 | OPEN_R0 | Đối chiếu chỉ đạo U1 read-only trong hội thoại với optional Unreal intake ở session; xác định packet/continuity và source evidence còn thiếu | Chưa dispatch từ roadmap; không import/runtime; không sửa ngược lịch sử AKOE |
| Q003 | OPEN_BEFORE_USER_TEST | Nguồn tuyển >= 5 non-coder, người phụ trách, consent, dữ liệu mẫu, quyền truy cập và thời hạn lưu/xóa | Chốt ở R0 trước thử nghiệm có người tham gia; thiếu người thử thì A01 chưa được đánh giá, không thay bằng agent hoặc tự hạ ngưỡng |

### Independent Review Response - Revision 1.1

Input: `docs/reviews/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_INDEPENDENT_REVIEW_2026-09-26.md`; review vòng một giữ nguyên. Roadmap trước sửa có SHA-256 `2a2ccea42392dffef4c1b080e4c2b40c4be2bf824ce6c2eb2251d8c685f47cfa`. Bảng dưới là disposition của tác giả sau đối chiếu, chưa phải independent acceptance vòng hai.

| ID | Disposition | Sửa ở đâu / lý do giữ khác biệt |
|---|---|---|
| F1 | FIXED_WITH_QUALIFICATION | Baseline, Non-Goals, R0/R1/R6: ưu tiên cvf-web hiện có; marketplace giữ nguyên, không mở rộng mặc định. App onboarding dùng đúng path legacy và registry NOT_STARTED, không gọi là active official design |
| F2 | CLARIFIED_PARTIAL_ACCEPTANCE | Bảng Unreal, đoạn U1, R0 và Q002: chỉ đạo hội thoại read-only có thật; packet/continuity chưa phản ánh. Không chấp nhận suy luận thiếu mã tracked đồng nghĩa chưa có chỉ đạo; không tự cấp dispatch |
| F3 | FIXED | Program ID là CVF-NCR; phase NCR-R0 tới NCR-R6; trace dùng revision-v1.1, không dùng program ID trùng đuôi phase R1 |
| F4 | CLARIFIED_PARTIAL_ACCEPTANCE | Authorization: tách canonical hold, excerpt bootstrap và quyền sửa tài liệu mới. AGENTS.md cho phép summary, không có nghĩa vụ chép toàn bộ nextAllowedMove |
| F5 | FIXED | Verification và trace: bỏ số đếm thiếu định nghĩa/tool-transcript dependency; thêm phép kiểm tra tái chạy và trạng thái hai file untracked, phân biệt delta của tác giả |
| F6 | FIXED | Q003, R0 và Acceptance: nguồn tuyển/owner/consent/data lifecycle; thiếu mẫu thì chưa nghiệm thu, không hạ ngưỡng |
| F7 | FIXED | Đọc nhanh cho người dùng: bảy ý tiếng Việt thông thường, giữ chi tiết kỹ thuật phía sau |

Change impact: I01/I09/I12 và A01-A03/A11 được làm rõ, không thay đích, permission, provider choice hoặc trình tự giai đoạn. Existing owners: cvf-web, DESIGN.md, startup contract và registry legacy nêu trên. Chi phí thêm: lập kế hoạch tuyển người thử trong R0; chưa có chi phí/live call ở lần sửa. Reviewer vòng hai đối chiếu các section theo F1-F7, kiểm tra authority và consumer mapping; nếu bác bỏ, sửa lại đúng delta bị chỉ ra từ preimage hash, không dùng shared stash/reset hoặc đụng file review.

## Verification / Evidence

Evidence baseline: HEAD `3ff8d9e16b1773daa2622186d911257f27ebb1f2`. Lần authoring đầu bắt đầu từ worktree sạch; đầu revision 1.1 có hai file untracked là roadmap và independent review. Chỉ roadmap thuộc write scope lần sửa này. Đã đối chiếu bootstrap/front door, active handoff, source locators và independent review; không audit toàn bộ implementation.

Revision verification: các phép kiểm tra bên dưới áp dụng tài liệu, không có provider/live, dependency installation, migration hoặc runtime mutation. Không dùng gate PASS để tự thay trạng thái REVISED_PENDING_INDEPENDENT_REVIEW.

Lịch sử v1.0: gate lần đầu thiếu Delta Execution Claim Boundary Control Block; đã sửa trong roadmap, không sửa checker. Kết quả 69/69 và preimage hash của v1.0 được independent review vòng một ghi nhận, không chuyển thành proof cho v1.1.

Reference check recipe (PowerShell từ repo root): lấy các token trong backtick bắt đầu bằng docs/, ECOSYSTEM/, EXTENSIONS/, governance/, CVF_SESSION/, .private_reference/ hoặc đúng AGENTS.md/DESIGN.md; loại command, kiểm tra mỗi token là file/directory bằng Test-Path -LiteralPath, distinct trước khi đếm. Đây chỉ là kiểm tra locator trong tài liệu, không quét hoặc đọc toàn bộ nội dung nguồn.

```powershell
$roadmapPath = 'docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md'
$roadmapText = [IO.File]::ReadAllText((Join-Path (Get-Location) $roadmapPath))
$localRefs = @([regex]::Matches($roadmapText, '`([^`\r\n]+)`') | ForEach-Object { $_.Groups[1].Value } | Where-Object { $_ -match '^(docs/|ECOSYSTEM/|EXTENSIONS/|governance/|CVF_SESSION/|\.private_reference/|AGENTS\.md$|DESIGN\.md$)' } | Sort-Object -Unique)
$missingRefs = @($localRefs | Where-Object { -not (Test-Path -LiteralPath $_) })
[pscustomobject]@{ ReferenceCount=$localRefs.Count; Missing=$missingRefs; ReplacementCharacter=$roadmapText.Contains([char]0xfffd); TrailingWhitespaceLines=[regex]::Matches($roadmapText, '(?m)[ \t]+\r?$').Count }
```

Validation results for revision 1.1, 2026-09-26 (local author verification, not independent acceptance):

| Check / reproducible command | Measured result |
|---|---|
| Reference/encoding/whitespace recipe above | 35 distinct local path tokens, including this roadmap; missing=[], replacement character=false, trailing whitespace lines=0 |
| Set CVF_COMPAT_BASE=HEAD, then `python governance/compat/run_worker_return_fast_gate.py` | Exit 0, COMPLIANT; reviewer-fast 69/69 PASS; git diff whitespace PASS |
| `python governance/compat/check_governed_file_size.py --enforce` | Exit 0, violations=0; 71 repository-wide advisories, not a claim they were repaired |
| `git status --short` | Exactly two untracked Markdown files: this roadmap and the pre-existing independent review; no tracked delta |
| SHA-256 of independent review, before and after revision | `fcdfee249a87997767bd8a34f7d05b65119d600b2c5c5db5362e00ee5ad0c4d8`; unchanged |

Get-FileHash -Algorithm SHA256 on the roadmap provides the reviewer the final revision identity. Its self-hash is not embedded in its own bytes; the independent reviewer should bind the hash they read to their next review. Reference recipe checks untracked content explicitly because git diff alone does not include it.

Validation correction (N1): bốn checker chặn lần chạy đầu v1.1 là `governance/compat/check_external_knowledge_intake_routing.py`, `governance/compat/check_external_absorption_core.py`, `governance/compat/check_external_absorption_value_conversion.py` và `governance/compat/check_external_absorption_overlap_discipline.py`. Repair read-ahead: đã đọc applicability, SOURCE_MARKERS/INTAKE_TEXT_MARKERS và required-section checks của bốn checker khi chẩn đoán lỗi v1.1, trước khi sửa locator; đây là read-ahead cho repair, không phải trước lần authoring đầu. Legacy root trực tiếp kích hoạt ba absorption guard; intake guard còn khớp cụm từ mô tả phép quét dù câu đang phủ định việc quét. Vì sửa roadmap không thực hiện intake/absorption, baseline dùng registry entry và scopePaths[0] làm locator canonical, đồng thời mô tả đúng phép kiểm tra locator bằng tiếng Việt; không tạo processing ledger hoặc maturity claim giả. Không đổi checker hoặc giấu hoạt động nguồn; review mockup sâu vẫn là việc R0 theo scope tương lai. Bảng kết quả và trace v1.1 phía trên/dưới là snapshot trước sửa N1/N2 đã được R2 kiểm chứng; bổ sung bốn checker làm tập locator thay đổi, không sửa ngược số đo lịch sử 35.

Future evidence reuse: dùng receipt hợp lệ và kiểm tra freshness theo owner; chỉ chạy lại khi có mâu thuẫn, expected information gain và cost reason. Không tái tạo review từng hàng để tăng số test. Live/production/governance claims tương lai phải có proof đúng loại, không mượn gate PASS của roadmap.

## External Repository Absorption Entry Control

| Field | Disposition |
|---|---|
| Source type | Existing CVF-governed absorption evidence and operator design direction |
| Upstream or source-mirror disposition | No acquisition or upstream execution in this revision; U1 is a conversation-scoped read-only task not released by this roadmap; legacy mockup is a reference only |
| Enumeration or manifest plan | Reuse prior accepted inventories; future selected source investigation follows existing intake owners |
| Per-file terminal-ledger plan | No new file-level absorption claim; preserve historical ledgers and deferred regions |
| Owner or overlap route | Existing Baseline table; R0 consumer/owner reconciliation before new implementation |
| Value-disposition route | Pattern reuse and capability integration are separate decisions; no automatic promotion |
| Claim boundary | Planning only, no new absorption completion or runtime activation |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this task synthesizes a direction roadmap, not a new source scan. Unread upstream regions, unresolved U1 evidence, contract-to-consumer wiring and host control limitations remain explicit investigation boundaries, not assertions of no value.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - roadmap commit records direction only; it makes no new all-files-read claim, and AKOE counts remain attributed to the existing bounded completion.

## Knowledge System Reconciliation

- Knowledge task class: ROADMAP_PLANNING_NO_NEW_CORPUS_MAP
- Source manifest: existing AKOE roadmap/completion evidence cited in Existing Baseline; no new source manifest in this commit
- Source manifest hash: N/A with reason - no new source manifest or corpus snapshot is created
- Enumeration safety: filesystem-backed locator validation only; no source enumeration claim
- Intake registry or ledger: existing AKOE terminal evidence remains authoritative; Q002 remains open for the not-opened U1 direction
- Authority assets: existing CVF owners and accepted AKOE evidence cited above
- Derived views: this roadmap's planning tables and R0-R6 sequence only
- Semantic region ledger: no new semantic-region ledger; future R0 must use existing owner/catalog/GAP routes
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0 for new knowledge assets introduced by this commit
- Orphan or unmapped assets: none in this zero-new-asset planning batch; unresolved future work remains Q001-Q003
- Cross-region links: six historical input families remain linked through existing AKOE evidence; U1 read-only direction is not opened and awaits Q002
- Drift check: NOT_RUN_PLANNING_ONLY; no current-map claim
- Rebuildability check: roadmap can be rebuilt from cited CVF owners, AKOE completion and the two independent reviews
- Retrieval boundary: planning locators only; no retrieval-readiness claim
- Adversarial verification: independent reviews R1 and R2; N1/N2 repair gate rerun
- Knowledge-map verdict: PARTIAL

This block accounts only for the zero new knowledge assets created by committing the planning artifact. It does not promote, remove or declare the cited source families semantically covered. Runtime gaps require owner/catalog/GAP reconciliation in R0; an integration proposal is not an as-built catalog entry.

## External-Local Coordination Binding

External research stays advisory and ends before internal implementation/review/closure. Shared-workspace workers are INTERNAL_AGENT regardless of provider. Local owns private-CVF verification and final technical disposition; external shortlist is not the Local coverage boundary. Reuse `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_EVIDENCE_RELAY_METHOD.md` and `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md`; no parallel process is introduced.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; repair read-ahead: `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; pre-commit repair read-ahead: `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| literalTokensReviewed | roadmap headings: Authorization, Purpose, Scope, Non-Goals, Design Control Gate, Work Plan, Acceptance Criteria, Verification; applicableCheckersRead, literalTokensReviewed, gateRunPurpose, claimBoundary; Text Encoding Exception; NOT_APPLICABLE_WITH_REASON |
| gateRunPurpose | Confirmation of document shape and evidence boundaries, not first discovery of required literals or runtime proof |
| claimBoundary | One planning artifact; no dispatched worker, implementation, activation, live or deployment claim |

## Text Encoding Exception

User-facing Vietnamese roadmap requires Vietnamese characters for the non-coder operator. Use UTF-8, ordinary punctuation and ASCII technical IDs/paths. Exception follows `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`, user-facing target-language clause; no invisible formatting characters or decorative symbols intended.

## Delta Execution Claim Boundary Control Block

| Field | Evidence |
|---|---|
| claimScope | Future L1/L2/L3 execution boundaries are design requirements, not current enforcement claims |
| claimDisposition | CLAIM_REJECTED for any present universal runtime-control claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or provider invocation in roadmap authoring |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no capability activation or controlled external action executed |
| invocationBoundary | Only document authoring and local validation; future invocation requires scoped authority |
| interceptionBoundary | No current direct interception asserted; future adapters prove only their actual controlled paths |
| claimLanguage | Proposed implementation direction; runtime integration and guarantees remain unproven here |
| forbiddenExpansion | No universal agent control, provider support, runtime safety, live or production readiness inferred |

Repair read-ahead: `governance/compat/check_delta_execution_claim_boundary.py`, REQUIRED_SECTION, REQUIRED_FIELDS and CLAIM_REJECTED markers reviewed before adding this block; this conditional checker was missed in initial read-ahead and discovered by the first validation run.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator / roadmap author |
| Provider or surface | Local coding-agent workspace |
| Session or invocation | CVF-NCR roadmap revision-v1.1, 2026-09-26 |
| Working directory | Private CVF provenance repository root |
| Command or tool surface | Read-only file/Git inspection, apply_patch, document/governance checks |
| Target paths | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Allowed scope source | Operator requested roadmap revision using accepted review points for a second independent review |
| Before status evidence | HEAD `3ff8d9e16b1773daa2622186d911257f27ebb1f2`; two untracked files: this roadmap and the independent review cited above |
| After status evidence | Two untracked files remain; only roadmap content edited in this revision; no runtime/owner/session mutation |
| Diff evidence | `git status --short`; explicit inspection of the new file because ordinary git diff omits untracked contents |
| Approval boundary | Document authoring only; future implementation/effects require scoped authority |
| Claim boundary | Proposed direction and staged acceptance criteria, not completed capability |
| Agent type | INTERNAL_AGENT, orchestrator authoring role |
| Invocation ID | cvf-ncr-roadmap-revision-v1.1-2026-09-26 |
| Expected manifest | This roadmap only |
| Actual changed set | This roadmap only for the author delta; independent review is pre-existing untracked material and must remain byte-identical |
| Manifest delta | Expected author delta MATCH: roadmap only; whole worktree also contains the pre-existing independent review, not authored or modified by this revision |
| Deletion or rename disposition | None; no stash, deletion, rename or unrelated cleanup authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY: private planning artifact. No public-sync, public catalog, deployment or production claim.

## Claim Boundary

Roadmap tổng hợp hướng đã thống nhất và đề xuất trình tự thực hiện. Tài liệu không chứng minh capability đã tích hợp, agent đã bị enforcement, provider subscription đã được hỗ trợ, dữ liệu đã backup hoặc cloud đã sẵn sàng. Bước triển khai kế tiếp là NCR-R0 khi được giao phạm vi; không tự phát hành worker work order từ sự tồn tại của file này.
