# CVF Roadmap: Năng lực cộng đồng, thực thi có kiểm soát, trải nghiệm non-coder

Memory class: FULL_RECORD

docType: roadmap

Status: ACCEPTED_UNIFIED_ROADMAP_R0_W01_ACCEPTED_PILOT_SCOPE_PENDING

Date: 2026-09-26

Program ID: CVF-NCR

Version: 2.2

Revision disposition: OPERATOR_APPROVED_CORE_SKILLS_DESIGN_INCORPORATED

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

Ngày 2026-09-26, operator yêu cầu đưa bản hợp nhất CVF-NCR + audit R2 đã qua phản biện external vào **roadmap NCR hiện có** để chuẩn bị thi công. Quyền này cho phép sửa và kiểm roadmap, đồng thời chuẩn bị phạm vi NCR-R0/W00; nó không tự cấp work-order dispatch, sửa production owner, cài dependency, credentials/provider/live, thay settings, deployment, public-sync hay production. Roadmap v2.0 là kế hoạch thống nhất; từng hành động sau R0 vẫn cần authority và gate của owner hiện hành.

Historical v2.0 startup acknowledged: current mode=`acel_applied_knowledge_owner_enrichment_closed_bounded`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; canonical next allowed move summary=hold for the post-AKOE-U1 operator checkpoint; parked checkpoint=work-order dispatch, implementation, provider/live, credentials, deployment and public sync. Role=Local reviewer/roadmap author; phase=operator-requested roadmap incorporation; final technical decision owner=Local; scope decision owner=operator.

Historical v2.0 bootstrap excerpt: `NEXT_ACTION_CLASS=HOLD_FOR_OPERATOR_CHECKPOINT_POST_AKOE_U1`; `NEXT_STEP=OPERATOR_DECIDES_ANY_SUCCESSOR`; `EXPANSION_ALLOWED=false`. Đây là các trường trích từ nextAllowedMove tại lần hợp nhất v2.0, không phải trạng thái hiện hành. Startup v2.1 bên dưới ghi mốc hiện tại; dispatch vẫn phải thỏa authority và continuity theo owner.

Historical v2.1 startup acknowledged: current mode=`cvf_ncr_r0_w01_profile_accepted_scope_pending`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=post-W01 document-only scope preparation, now limited by operator to incorporating the agreed capability/plugin design; parked checkpoint=new worker dispatch, pilot effects, runtime, dependency, credentials/provider/live, settings, deployment and public sync. Role=Local orchestrator/reviewer; phase=design incorporation; decision owner=Local for technical disposition and operator for scope/data/effect/expense. Operator đã đồng ý tích hợp delta sau Web final return; tiếp tục tạm dừng giao work order mới cho worker theo chỉ đạo trước đó. Đồng ý sửa roadmap không tự gỡ tạm dừng hoặc mở implementation.

Current v2.2 startup acknowledged: current mode at entry=`cvf_ncr_r1_w01_html_ux_copy_accepted_web_research_hold`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; role=Local orchestrator/reviewer; phase=external research closed, internal planning; next allowed move=incorporate D013 and prepare bounded internal work order for operator relay. Operator ngày 2026-09-27 chuyển trách nhiệm sang Local sau Web closeout; điều kiện chờ nghiên cứu ở D012 đã được giải quyết. Quyết định kỹ thuật thuộc Local; dữ liệu/effect/expense thuộc operator. Không mở host exposure, lifecycle promotion, provider/live, public hoặc production từ quyết định này.

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
| `docs/guides/CVF_QUICK_ORIENTATION.md`; `docs/GET_STARTED.md`; `docs/HOW_TO_APPLY_CVF.md`; `docs/reference/CVF_INTERNAL_USER_GUIDE.md` | Các hướng dẫn/entry point hiện có để đối chiếu nội dung user guide tổng quan | Không gọi là thiếu hoàn toàn guide; một số nội dung dài, kỹ thuật hoặc mang trạng thái lịch sử, phải đối chiếu authority và trạng thái hiện hành trước khi tái dùng |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` | Consumer UI hiện có: dashboard approvals, artifacts, workspace, runtime, skills, marketplace, history, governance; API providers, execute, sessions, integrations/test, approvals, artifacts/export | Đối chiếu và tái dùng trước thiết kế mới; có route/code không đồng nghĩa toàn tuyến đã chạy được hoặc đủ quyền runtime |
| `docs/corpus-intelligence/registry/entries/legacy-cvf-app-onboarding.json`, trường scopePaths[0] là locator thư mục App onboarding trong kho legacy | UI design reference legacy; registry ghi NOT_STARTED; dùng để đối chiếu mockup khi phù hợp | Dùng locator canonical trong registry, không thư mục App onboarding ở repo root; không coi mockup là active design authority hoặc capability đã nghiệm thu; DESIGN.md và owner hiện hành vẫn điều khiển |
| `docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md`; `docs/reviews/CVF_ACEL_AKOE_P4_COMMON_LOCAL_RECONCILIATION_COMPLETION_2026-09-26.md` | AKOE đóng bounded; 19 candidate thuộc sáu nguồn: 5 ADAPT, 8 CONFIRMED_EXISTING, 3 DEFER_WITH_TRIGGER, 2 REJECT_DIRECT_IMPORT, 1 source-blocked | Không suy ra toàn bộ repo đã đọc hoặc capability đã chạy live |
| `EXTENSIONS/CVF_MODEL_GATEWAY/README.md`; `docs/reference/model_gateway/README.md` | Gateway owner cho provider, routing, credential và receipt | Tái dùng, kiểm tra consumer/support matrix; không khẳng định mọi login subscription đã có |
| `docs/reference/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md`, Purpose / S1 | Đã có contract tiếp nhận skill/MCP/CLI/repo/database | Contract nói rõ Phase A; runtime enforcement cần authority riêng |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`; `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | T1 ánh xạ identity/composition/risk/authority/rollback; T4 intake provenance/license/security; T5 dependency/conflict/order/capability boundary | T1 `ACTIVE_REFERENCE`; T4/T5 `CANDIDATE`. Contract không chứng minh importer hoặc runtime control; loading/dependency không tự cấp quyền. D011 làm rõ cách áp dụng, không promote owner |
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
| ACEL-AKOE-U1 / Unreal Agent | Local read-only source reconciliation đã đóng bounded tại `docs/reviews/CVF_ACEL_AKOE_U1_UNREAL_AGENT_LOCAL_SOURCE_RECONCILIATION_2026-09-26.md`; status `SOURCE_RECONCILED_DEFER_WITH_TRIGGER` | Pin `unreallabsai/unreal-agent@1b9f778453f411c029b39b85102aaefb95e7e48d`; chưa import/runtime-enabled; không phải nguồn thứ bảy của ledger AKOE cũ |

U1 đã có Web advisory return được Local kiểm nguồn, license và owner overlap tại pin trên; việc pin/license/source reconciliation không được giao lại. Trigger để xem xét tiếp là một non-coder controlled-runtime consumer có nhu cầu durability/retry/cancel cụ thể và đối chiếu owner hiện có chỉ ra gap chưa giải quyết. Khi trigger xảy ra, Local đề xuất đúng phần adaptation/test còn thiếu dưới authority mới; không suy từ source reconciliation thành import, runtime integration hoặc provider proof. U1 không chặn pilot độc lập không dùng Unreal và không sửa ngược ledger AKOE sáu nguồn đã đóng.

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

### Capability bundle và tác động theo vòng đời

Một capability có thể gồm nhiều thành phần và dependency, với tác động phát sinh ở setup, load/enable, invoke, reload/update, reconnect hoặc revoke. Manifest là một nguồn mô tả; cần ánh xạ thành phần thực, dependency đã resolve, host/profile và đường phát sinh tác động bằng các owner ASSF, intake, composition, admission và support matrix hiện có. Trạng thái contract/candidate không được trình bày thành runtime control đã được chứng minh.

Tách kiểm tra nguồn, admission, cài đặt, enable/load, invoke và nghiệm thu. Trước mỗi chuyển trạng thái có effect, áp dụng quyền, control và evidence tương ứng; không chờ tới tool call đầu tiên. Không biết tác động không đồng nghĩa không có tác động. Nếu thiếu điều kiện bắt buộc, chặn đường đó; đường thay thế chỉ được tiếp tục khi đáp ứng policy và authority riêng. Hạ mức claim không tự cho phép continuation. Kiểm tự động trong quyền đã cấp không mặc định cần thêm một lần duyệt Human; khi mức bảo đảm thay đổi, công bố và lấy quyết định user theo boundary đã quy định.

Evidence phải chỉ đúng bản thực đang nạp: nguồn/version hoặc digest phù hợp, dependency đã resolve, host/profile và cấu hình liên quan tới quyền/tác động; secret chỉ dùng reference. Với remote service, ghi đúng giới hạn quan sát; digest local không chứng minh server bất biến. Thay đổi binding phải đánh giá lại evidence chịu ảnh hưởng trước effect tiếp theo; bản cập nhật không tự thay bản đang chạy. Reuse registry/receipt/upgrade owner; chỉ thêm field sau khi chứng minh gap, không mặc định dựng watcher mới.

Thu hồi quyền gọi mới, vô hiệu hóa capability, dừng tiến trình đang chạy và xử lý tác động đã xảy ra là các kết quả khác nhau. Chỉ báo dừng/revoke thành công trong phạm vi đã xác minh; effect không đảo ngược phải có disposition theo owner recovery/compensation. Mức L1/L2/L3 dựa trên boundary được thử, không suy từ badge marketplace hoặc tên sandbox của host.

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

## Foundation Readiness And Audit Alignment

Roadmap này hợp nhất định hướng CVF-NCR với **nhánh củng cố nền theo đường chạy được chọn**. Audit external R2 V0.9 (`CVF_R2_RESPONSE_AND_ROADMAP_20260915.zip`, SHA-256 `780113c24694f3bad2f8438bf1602ea792616a638a6a1f00d046711574c7b912`) và review alignment (`CVF_TWO_ROADMAP_ALIGNMENT_REVIEW_20260926.zip`, SHA-256 `0320dce601d4dd2ca66df530173cf582482b9e47df5e9d48db98267bc9a664d0`; revised review `CVF_ALIGNMENT_REVISED_REVIEW_20260926.zip`, SHA-256 `eb041a077b442caf0c5d0df4b748273825172322dd7d63231149acaf7dd3dd93`) là **advisory input**, không là CVF source authority hoặc kết luận private runtime. Operator đã yêu cầu nhập bản hợp nhất vào roadmap hiện có; Local chịu trách nhiệm xác minh finding, owner và acceptance trên source/profile/candidate thực trước work order. Không mở lại ACK D01–D06.

Audit W00–W06 là các work package nền; W07 được hấp thụ vào R0/R1/R3/R4 và A01–A12, không là điều kiện đóng P01–P10 mặc định. Bảng dưới là chỉ mục lập việc, không thay test T01–T10 chi tiết của R2; work order phải dẫn đúng tiêu chí gốc áp dụng hoặc ghi lý do không áp dụng. Mỗi finding có ba kết luận riêng: trạng thái tại mốc audit, khả năng ảnh hưởng route hiện tại, và evidence đủ cho gate đang xin. `NOT_APPLICABLE_WITH_REASON` của Web không chứng minh route thay thế an toàn; `NEEDS_EVIDENCE` không thành PASS; containment phải chặn/loại tác động có kiểm chứng, owner và mốc rà lại, không đổi finding thành `FIXED`.

| Finding / work package | Đưa vào chặng và gate | Proof hoặc quyết định phải giữ |
|---|---|---|
| P01 + P05 / W01 | R0 xác định CI/dependency cần cho slice; R1 hoặc tranche nền được cấp quyền sửa; candidate/release dùng required checks đúng SHA | Clean dependency closure, typecheck/test/build đúng profile; required job fail/skip/cancel/absent không thành PASS; code workflow và GitHub settings là hai quyền riêng. |
| P04 / W02-A | R2 nếu trace tới `cvf-web` execute route | Prompt sau DLP/SAF1 phải tới call boundary ở initial/retry/vision; BLOCK 0 invocation; binding/policy không đổi âm thầm. Route khác cần chứng minh control tương đương, không chỉ đổi tên adapter. |
| P03 / W02-B | R2 pre-live nếu route dùng Web approval/effect; R4 tăng fault coverage | Durable approval claim fail-closed, actor/hash/expiry, concurrency một operation, restart/unknown outcome, writer và migration/rollback theo profile. MAO durable run-store AKOE-P2-R2 **không đóng** Web approval P03. |
| P06 / W02-C | R2 trước effect trên ingress áp dụng | Validate schema/type/size trước normalization, raw signature giữ đúng, invalid input 0 invocation, valid fixtures không vỡ. |
| P02 / W03-A | Khi tạo candidate/public projection ở bất kỳ R2–R6 | Pending và committed-tree residue, base/head, policy, mapped/overlaid artifact sau projection, candidate SHA/hash; không giả định phải đợi hosted R5. |
| P08 / W03-B | Secret scan cho candidate/artifact đang dùng; secret-safe live evidence không đợi public export | Exemption fixture chính xác, không blanket skip test tree; synthetic secret ngoài allowlist bị bắt, báo scanned/skipped/unreadable và không in secret. |
| P09 / W03-C | Ngay khi kết luận dựa vào release runner; W03-B/C tích hợp tuần tự | Console/JSON/file/exit thống nhất cho required PASS/FAIL/SKIP/ABSENT; dry-run và non-release exception đúng scope; không dùng mock để cấp release proof. |
| P07 + P10 / W04 | R0/R1 chốt data/cost contract theo profile; trước effect hoặc hosted claim phụ thuộc | P07 inventory sink/retention/access/backup trước khi chọn encryption; approval expiry khác deletion. P10 phân biệt estimate/attempt limit với hard USD cap; hard cap chỉ thiết kế reserve/reconcile nếu contract thật yêu cầu. |
| W05 | R2 exit/R3 entry cho phần pre-live; R4 tăng recovery | Integration theo chuỗi validation→binding→claim→transform→attempt→invoke→receipt/recovery; proof tại effect boundary, migration/rollback trên data copy khi áp dụng. Không còn P1 tác động trong pilot chưa xử lý hoặc containment có evidence. |
| W06 | R3 live proof khi được cấp quyền; artifact/release/publish theo event riêng ở bất kỳ R phù hợp | Provider/model/corpus/call-cost/stop đúng authority; release-quality governance proof dùng real provider theo chuẩn hiện hành. Artifact sau projection, publishing và hosted deployment là các quyết định khác nhau. |

**AL-01–AL-06 là chỉnh lý gate:** AL-01 yêu cầu trace entry→bridge/dependency/retry/fallback→effect và proof của route thay thế; AL-02 đưa durable admission, claim một operation, timeout/cancel/unknown và migration khi có vào R2 exit/R3 entry trước live; AL-03 tách hosted proof R5 khỏi artifact/public proof theo event; AL-04 giữ hai kết nối độc lập và A07 ở R4, không ép vào live R3 đầu; AL-05 giữ I01–I12/A01–A12 và metric/baseline chốt trước đợt đo áp dụng, với bằng chứng người dùng thật chỉ khi mở đợt đánh giá tương ứng theo D008; AL-06 bổ sung threat/metric, writer/RPO/RTO, quyền tách biệt và hosted decision vào Q/D hiện có, không tạo register khác.

**Evidence đã đóng cần tái dùng đúng phạm vi:** `docs/reviews/CVF_ACEL_AKOE_P2_R2_DURABLE_RUN_STORE_REVIEWER_CORRECTION_COMPLETION_2026-09-25.md` đóng bounded MAO concurrent terminal race và reviewer gate correction; `docs/reviews/CVF_ACEL_AKOE_P3_PROVIDER_FREE_INTEGRATED_APPLICATION_PROOF_COMPLETION_2026-09-25.md` đóng bounded provider-free composition; U1 source review đóng read-only intake. Không giao lại các phần đã giải quyết. `docs/reference/CVF_DISPATCH_RELEASE_READINESS_MACHINE_STANDARD_2026-09-25.md` đã sở hữu pre-dispatch binding/material/continuity gate; authoring trước commit và final worker release là hai pha. Các receipt này không chứng minh Web P03, provider/live, UX acceptance hay production.

**CI tại baseline `4567d750087d47f369939a0e9891ca6fcb596034`:** `.github/workflows/cvf-ci.yml` đã có bước cài SOT3 workspace dependency; `.github/workflows/cvf-web-ci.yml` đã có bước cài Execution Plane dependency. Job-level readout của GitHub Actions tại SHA này còn failure ở CVF CI, CVF CI Pipeline và Static CI Gate; riêng Pipeline dừng tại Governance Hook Chain, Static tại install SOT3. Sự tồn tại của workflow mới không là PASS; job/step failure chưa là root cause P01/P05. Trước mỗi work order, Local đối chiếu HEAD/remote/delta chưa push/dirty, failed-step diagnostics an toàn, required-check/settings profile, route/writer/data/provider profile, owner và candidate SHA. Không tái chạy rộng nếu không có mâu thuẫn và information gain rõ.

## Work Plan

Các giai đoạn dưới đây là kế hoạch, trừ NCR-R0/W00 đã được Local nghiệm thu bounded ở `docs/reviews/CVF_CVF_NCR_R0_W00_PILOT_SELECTION_WORKER_RETURN_2026-09-26.md`. Operator đã chọn HTML review packet làm ứng viên pilot nội bộ đầu tiên; việc chọn ứng viên không cấp quyền chạy pilot hoặc sửa runtime. Các bước còn lại là gói công việc để tạo work order giới hạn, không phải lệnh thi công sẵn. Thời gian/ngân sách được chốt theo slice ở R0; không đặt lịch hoàn thành giả khi chưa biết provider, workload và hạ tầng. Không tạo work order sửa toàn P01–P10 trước khi biết route/profile và finding áp dụng.

Current W01 update: `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md` đã được Local nghiệm thu `ACCEPTED_BOUNDED_SOURCE_PROFILE_PACKET` tại `d9b43a6f6deff7fb19710b5a9a4f50bf2a6015b6`. Ngoại lệ đối với mô tả kế hoạch phía trên gồm cả W00 và W01; chưa chứng minh UI walkthrough, route runtime/provider/live. Các vấn đề profile/effect ở Q001 vẫn mở. Work package audit W01 về dependency/CI trong R1 khác NCR-R0/W01 source/profile packet; không dùng chung nhãn để suy đã sửa CI. Giao mới tạm dừng theo operator.

### R0 - Chốt consumer, owner và pilot nhỏ nhất

- ID: NCR-R0. Vai trò: orchestrator + Local reviewer. Đầu vào: roadmap này và evidence AKOE hiện có.
- Việc làm: lần theo một luồng user đến consumer thực; phân loại owner đã có/contract-only/wiring chưa rõ/gap đã chứng minh; đối chiếu catalog và system-chain GAP hiện có, không tạo inventory cạnh tranh.
- D011: dùng ánh xạ T1/T4/T5/admission và maturity trong baseline để kiểm component/dependency/effect của consumer được chọn theo mục Capability bundle. Chỉ kích hoạt xác minh source/profile/runtime khi consumer và authority yêu cầu; không giao lại W00/W01 hoặc promote contract từ research plugin.
- Điểm xuất phát UI là cvf-web hiện có: approvals, artifacts, workspace, runtime, skills, marketplace, history, governance và các API providers, execute, sessions, integrations/test, approvals, artifacts/export. Lần theo route/component/service/owner của luồng được chọn; ghi reuse/change/defer và bằng chứng cho từng đoạn liên quan, không audit lại toàn web platform. Đối chiếu mockup legacy ở đúng path trong bảng baseline, không thăng cấp mockup thành authority.
- Quyết định sau W00: dùng luồng HTML review packet hiện có qua Work Transfer UI làm ứng viên pilot đầu. W00 đã xác minh consumer UI/form/preview/download và route; chưa xác minh thao tác UI thực, độ sâu P06/P08 hoặc profile receipt-helper theo cấu hình. Video không là slice pilot đầu và không là bằng chứng media pipeline; xem nhánh user guide/video tổng quan bên dưới. Không mở nhiều demo cùng lúc.
- W00: lập entry→bridge/dependency/retry/fallback→effect trace cho ứng viên; phân biệt P01–P10 tại mốc audit, applicability trên route/profile và evidence đủ cho gate. Ghi `CONFIRMED`, `CHANGED`, `NOT_APPLICABLE_WITH_REASON` hoặc `NEEDS_EVIDENCE` với locator; không tái test toàn finding hoặc gọi N/A từ tên route. Kế thừa AKOE-P2-R2/P3, U1 và dispatch readiness đúng claim đã đóng.
- Chốt provider/auth đầu tiên từ kết nối user muốn dùng và host hỗ trợ; ngân sách chi phí/retry, dữ liệu mẫu, metric, threat model và RPO/RTO. Lựa chọn đầu tiên không trở thành khóa provider dài hạn.
- U1 đã `SOURCE_RECONCILED_DEFER_WITH_TRIGGER`; R0 chỉ kiểm consumer/trigger nếu slice cần Unreal và đối chiếu owner cho thấy gap. Không lặp pin/license/source intake, không import hoặc chạy runtime từ roadmap.
- Chốt Q003 cho pilot nội bộ: agent mô phỏng góc nhìn người mới bằng walkthrough hoặc thao tác UI thực trong quyền user; operator tham gia ở góc nhìn Human khi cần lựa chọn, góp ý hoặc quyết định thuộc thẩm quyền. Ghi rõ lượt mô phỏng, thao tác thực và hỗ trợ đã dùng; không gọi agent là người thử thật. Tuyển người ngoài, consent và retention của nghiên cứu có người chỉ chuẩn bị khi operator mở đợt đó sau này, không là dependency của R0–R3 nội bộ.
- Đầu ra: bảng owner-consumer-gap có locator; một slice, mức L1/L2/L3, acceptance scenario, scope/effect/threat envelope, kế hoạch baseline và mô phỏng nội bộ, map finding/work package tối thiểu; danh sách quyết định còn mở; packet cho R1 hoặc tranche nhỏ hơn theo routing hiện hành. Thiếu số đo ghi `UNKNOWN`, không bịa baseline.
- Nghiệm thu/exit: một kết quả user rõ, các đoạn chưa wiring rõ, zero duplicate owner không có lý do. Không cần quét lại toàn bộ corpus. Dừng nếu chỉ còn lý do "repo nổi tiếng" mà không có user outcome.

### R1 - Hợp đồng job và trải nghiệm non-coder

- ID: NCR-R1. Phụ thuộc: R0 chọn use case. Vai trò: product/UX worker và contract reviewer.
- Việc làm: map goal, input, preview, sửa, accept, cancel, pending approval, lỗi và recovery vào owner workspace/operating model hiện có; dùng progressive disclosure theo DESIGN.md.
- Bắt đầu từ route/component, OnboardingWizard và consumer đã đối chiếu ở R0; tham khảo mockup legacy khi còn phù hợp. Chỉ thiết kế delta thiếu, không tạo dashboard/chooser/approval flow song song. Đầu ra phải ghi rõ phần tái dùng, phần sửa và lý do.
- Hoàn thiện capability card và provider/account chooser trên surface đã chọn; hiển thị mức kiểm soát, dữ liệu gửi ra ngoài, chi phí biết/chưa biết; không yêu cầu user nhập enum hay đọc log.
- D011: giải thích bằng ngôn ngữ user điều xảy ra khi cài/bật so với khi gọi, dependency liên quan, dữ liệu/quyền/chi phí và giới hạn dừng/thu hồi; tái dùng UI hiện hữu, không đưa tên field nội bộ vào luồng chính.
- Đầu ra: flow/prototype, job/evidence field mapping, support matrix ban đầu và kiểm thử ngôn ngữ/tính dễ hiểu.
- Nghiệm thu: agent mô phỏng thử tìm và giải thích kết quả sắp tạo, quyền sắp cấp và tác động chưa thực hiện; operator góp ý ở góc nhìn Human khi cần. Đây là kiểm tra luồng/copy nội bộ, không là bằng chứng người mới thật đã hiểu. Mock chỉ chứng minh cấu trúc UI, không governance behavior.
- W01 sửa dependency/CI theo tập test cần cho slice khi được cấp quyền; W04 chốt P07/P10 theo data/cost profile. Nếu sau này mở thử nghiệm có người ngoài, Q003 phải được quyết định trước khi mời/chạy thử. Không bắt mọi package chưa dùng xanh trước wireframe, nhưng required checks của candidate phải đúng SHA/profile trước claim.
- Trước pilot HTML có effect: kiểm `NEXTAUTH_URL` thực của receipt helper, điểm nhận và loại dữ liệu gửi ra, retention, độ trễ, chi phí, khả năng từ chối/giới hạn effect; làm UI-interaction walkthrough riêng với source-reading của W00; xác minh phần còn thiếu của P06/P08 và route-specific gates. Nếu profile chưa rõ, chỉ làm đối chiếu read-only và giữ pilot chưa chạy.
- Exit: UX và contract đủ dùng cho đúng một slice. Không viết lại agent host; không mở credential/live trong giai đoạn này nếu chưa được cấp riêng.

### R2 - Adapter và execution boundary tối thiểu

- ID: NCR-R2. Phụ thuộc: R1. Vai trò: integration worker; reviewer độc lập theo rủi ro.
- Việc làm: cài/đóng gói đúng capability được duyệt; nối adapter vào gateway/admission/execution owners; job workspace riêng; permission/secret references; durable intent; receipt và cancel semantics.
- D011: nếu capability được chọn có effect khi setup/load/reload/update/reconnect hoặc ngoài tool path, work order phải chỉ rõ đường effect, quyền/control, evidence và negative case trước thực thi theo mục Capability bundle. Kiểm chứng gắn bản đang nạp và dependency thực; test intent trong roadmap không cấp quyền tự chạy.
- Chọn L2 hoặc L3 theo khả năng host; L1 có thể giữ như lựa chọn tương thích nhưng không được dùng để nghiệm thu enforcement của L3.
- Đầu ra: consumer gọi được adapter, registry mapping, supported-version record, threat/negative tests, uninstall/revoke và rollback bản trước.
- Nghiệm thu: chặn ngoài scope, thiếu approval/secret, pin sai, input lỗi và event giả; worker không sửa policy/evidence đã chấp nhận; retry/timeout không tự tạo duplicate effect.
- Nếu trace tới Web, W02-A/B/C xử lý P04/P03/P06 tuần tự trên route/binding chung; nếu không, Local chứng minh control tương đương của route thay thế tại effect boundary. W03 được xử lý khi candidate/artifact/release pipeline áp dụng, không mặc định đợi hosted. Diagnostics sandbox có authority có thể tái hiện lỗi; chưa qua gate live thì capability có effect giữ disabled.
- Exit để xin live: offline integration/isolation phù hợp đã qua; durable intent/admission trước effect; write failure không cấp quyền; một operation claim, timeout/cancel/unknown outcome không replay mù. Nếu đổi schema, thử migration/rollback trên bản sao an toàn trước dữ liệu thật. W05 phần pre-live kiểm chuỗi validation→binding→claim→transform→attempt→invoke→receipt/recovery. Không dùng L1 để nghiệm thu L2/L3.

### R3 - Vertical slice thực, kết quả pilot nội bộ

- ID: NCR-R3. Phụ thuộc: R2 và authority riêng cho provider/live, credential, dependency và effect cần thiết.
- Việc làm: chạy toàn tuyến user goal -> selected agent -> admitted capability -> artifact -> verification -> preview -> user acceptance. Dùng đúng provider/auth được chọn và input an toàn; không công bố ra ngoài mặc định.
- Đầu ra: artifact mở được, receipt gắn run/version/input/output, chi phí thực hoặc UNKNOWN, giới hạn mức kiểm soát và kết quả pilot nội bộ được phân loại theo mô phỏng agent, đánh giá operator và phép đo kỹ thuật.
- Nghiệm thu: agent ở vai user tạo rồi sửa sản phẩm bằng lời tự nhiên qua UI, không cần terminal; operator tham gia khi có lựa chọn hoặc góp ý cần Human; refresh UI không mất job; denial/cancel được giải thích; không có fallback hoặc side effect ngầm.
- Governance behavior phải có real-provider proof theo chuẩn hiện hành. Release-quality proof dùng `python scripts/run_cvf_release_gate_bundle.py --json` dưới authority tương ứng; thất bại/timeout phải diagnostic trước retry. Receipt cũ không thay proof mới.
- Entry trước call/effect đầu tiên: R2/W05 pre-live đã qua trong scope; không còn P1 có thể tác động chưa xử lý hoặc containment được kiểm; Q004/Q005 và các quyền provider/model/auth/call-cost/data/stop riêng đã chốt. W06-live không tự bao gồm artifact publishing.
- Exit: một use case dùng được với claim bounded và A01–A06, A08, A10–A12 theo scope nội bộ. Agent mô phỏng đi luồng chính không dùng terminal/config và kiểm khả năng nhận biết tác động trước effect; phép kiểm hệ thống và operator decision vẫn độc lập với persona. Không yêu cầu tuyển non-coder thật hay ngưỡng 5 người/80% để đóng pilot nội bộ; kết quả usability trên người mới thật ghi `NOT_EVALUATED`, không suy từ mô phỏng thành mức sẵn sàng cho quần thể người dùng. Nếu auth subscription không hỗ trợ, ghi giới hạn và xin user chọn đường khác; không lén dùng API trả phí.

### R4 - Pilot local bền vững và chứng minh khả năng thay thế

- ID: NCR-R4. Phụ thuộc: R3. Vai trò: reliability/integration worker và reviewer.
- Việc làm: tăng fault coverage sau minimum pre-live đã chứng minh: restart/crash/reconnect/cancel/duplicate submission/unknown-effect recovery; cap concurrency; kiểm tra workspace chéo; backup/restore sạch; resume từ thiết bị khác trong phạm vi đã cấu hình.
- Kiểm tra cùng job contract với ít nhất hai kết nối độc lập khả dụng. Mục tiêu có API và official account/host mode; nếu chưa có luồng account được hỗ trợ, giữ phần đó pending với evidence, không tuyên bố đủ tự do kết nối.
- Đầu ra: test matrix có fault injection, measured latency/cost, restore receipt, support matrix cập nhật và onboarding/recovery hướng dẫn bằng tiếng Việt.
- Nghiệm thu: không mất artifact đã nhận; không duplicate tác động ở các tình huống đã định nghĩa; restore đạt RPO/RTO đã chốt; ít nhất hai kết nối độc lập có A07 conformance receipts cùng job/user contract; user hiểu điểm cần quyết định; không yêu cầu đọc log để dùng bình thường. Không dùng MAO run-store proof để đóng Web approval P03.
- Exit: pilot local ổn định trong bộ scenario đã chốt. Không dùng một lần chạy thành công để kết luận production.

### R5 - VPS/cloud/hybrid, truy cập mọi nơi và bảo quản data

- ID: NCR-R5. Phụ thuộc: R4; operator chọn host, ngân sách, vùng dữ liệu, quyền deployment và phương án secret.
- Việc làm: triển khai profile portable, remote authentication/session, workspace và OS isolation, secret/revoke, encrypted backup độc lập worker; thực hiện restore nhất quán state–artifact–evidence từ môi trường sạch, cutover một-writer/fencing, rollback và health/alert.
- Đầu ra: deployment/config profile tái tạo được, migration/rollback runbook, data export, cost/retention policy, restore/cutover evidence và health/alert vận hành.
- Nghiệm thu: người dùng mở và tiếp tục công việc từ máy khác; laptop tắt không làm mất cloud job; local-dependent job báo đúng; mất host vẫn phục hồi trong mục tiêu đã chọn.
- Exit: bounded hosted pilot được chấp nhận theo RPO/RTO, auth/isolation/restore/cutover evidence của profile thực. W03/W06-public là gate theo sự kiện tạo artifact/release/publish ở bất kỳ chặng phù hợp, không thay hosted proof và không mặc định đợi R5. Public endpoint, production hoặc public catalog chỉ mở khi có authority/gate riêng; không suy ra từ việc VPS đã chạy.

### R6 - Mở rộng capability có chọn lọc và cải tiến có kiểm chứng

- ID: NCR-R6. Phụ thuộc: R3-R5 đủ bằng chứng cho môi trường của capability mới; không bắt capability local chờ toàn bộ cloud rollout.
- Việc làm: thêm từng capability theo nhu cầu user; reuse intake/source ledger và adapter conformance suite; quản lý upgrade, deprecate, revoke, usage và hỗ trợ.
- D011: tiếp nhận từng bundle theo consumer/outcome và effect lifecycle đã xác minh; Claude plugin là case tham khảo có điều kiện, không cam kết import mọi plugin. Capability/môi trường/quyền/dữ liệu/chi phí mới phải qua Change Control trước thi công.
- Jev hỗ trợ evidence cho chọn/đánh giá; WikiSkill hỗ trợ proposal cải tiến có kiểm tra tác động/rollback; không tự promote. Cân nhắc Unreal chỉ khi U1 đã có Local disposition và use case yêu cầu.
- Đầu ra: mỗi capability có người dùng/consumer, owner, support level, receipt và rollback; catalog phân biệt tested/enabled/deferred.
- Nghiệm thu: năng lực mới cải thiện user outcome đo được, không phá invariant hoặc tạo owner trùng. Chỉ tăng concurrency/số nguồn theo khả năng review và vận hành.
- Exit: từng capability đóng bounded; chương trình không biến thành nghiên cứu vô hạn. Không xây/mở rộng marketplace năng lực, Kubernetes hoặc new plane nếu chưa có quyết định riêng dựa trên nhu cầu; route marketplace hiện có giữ disposition đã nêu trong baseline.

### D013 - Core skills thực hành và conflict/host delivery trong NCR

Đây là phần bổ sung cho R0 owner reconciliation, R1 hướng dẫn thực hành và R2 admission/delivery của cùng roadmap; không tạo roadmap hoặc plane mới. Hai stream: nội dung CVF-owned giúp agent hoàn thành công việc đúng quyền; và kiểm soát xung đột trước khi skill được đưa vào tập agent có thể chọn. Tên skill, prefix hay quyền sở hữu CVF không tự chứng minh an toàn hoặc host isolation.

| Bước thuộc NCR | Đầu ra và điều kiện đóng bounded | Boundary |
|---|---|---|
| NCR-R0/S01 - Local source/owner reconciliation | Đối chiếu promotion/review và body/registry/source/truth của đúng TDD, code-review và discovery; chốt applicability của behavioral-evaluation owner; trả patch proposal và case/expected-outcome design có locator | Một worker return, read-only đối với owner; không audit lại toàn catalog, sửa status cho giống nhau hoặc chạy skill |
| R1 skill-content tranche, scope sau review S01 | Candidate test-evidence-audit theo SOP; enrich discovery trong skill-selection/context-routing/governance-orientation; workflow skill riêng chỉ khi có consumer/input/output/trigger riêng | Author nội dung/case ngoài discovery trước; chưa cài/nạp/activate; metadata candidate không tự cho phép tạo runtime body |
| R2 conflict/delivery tranche, scope sau owner mapping | Admission/exposure decision theo host/profile/version/identity, full package/config/resource review; projection giữ restriction; rollback/stale/revoke và evidence theo phase | Pilot một host có phạm vi thực được xác minh; shared discovery root hoặc prefix không là cơ chế cô lập; provider built-ins không bị CVF ghi đè |
| Evaluation rồi Local review | Tách content explicit, selector, host implicit discovery, body delivery và receipt; đo artifact đúng source/quyền/claim và rework/cost khi quan sát được | Chỉ chạy trong authority cụ thể; kết quả candidate không tự thành activation, production hoặc runtime governance proof |

NCR-R0/S01 `CLOSED_PASS_BOUNDED`: Local đã nghiệm thu source/owner reconciliation và case design tại `docs/reviews/CVF_CVF_NCR_R0_S01_CORE_SKILLS_LOCAL_REVIEW_FINDINGS_2026-09-27.md`; worker return material `5f8addf3922c6dbee7dea33e451b2a4e29fbc247`. R1/S01 đã chỉnh hai `SKILL.md` để phân biệt ACTIVE source state, bounded adapter và live exemplar của skill khác; Local áp dụng reviewer-local repair cho các lỗi còn lại thay vì mở thêm lượt worker, theo completion `docs/reviews/CVF_CVF_NCR_R1_S01_SKILL_LIFECYCLE_BODY_COMPLETION_2026-09-27.md`. Hai README front door còn lệch với ASCP-P1-P3 và được ghi là dependent documentation gap ngoài phạm vi hai body. Behavioral contract vẫn CANDIDATE, T5 composition rules chưa có enforcement qua hai implementation đã kiểm tra. Không nâng trạng thái host/runtime từ S01 hay R1/S01.

R1/S02 content/case đã được Local review tại `docs/reviews/CVF_CVF_NCR_R1_S02_TEST_EVIDENCE_AUDIT_CONTENT_COMPLETION_2026-09-27.md`: nhận candidate tài liệu sau chỉnh lý reviewer về đúng năm nhãn, ranh giới ADD/DEFER và baseline đánh giá công bằng. Worker đã chạy fixture và pytest dù work order cấm test execution; đây là scope violation được giữ trong original return, không tính là bằng chứng thực thi được ủy quyền và không gọi tranche là clean PASS. Theo yêu cầu operator ở lượt review, Local cũng chỉnh hai README TDD/code-review cho khớp ACTIVE source và bounded ASCP-P1-P3 executor/CLI-MCP; không sửa package body, registry, truth hay host. Skill reviewer mới chỉ được Local đọc và áp dụng thủ công, chưa có receipt chứng minh runtime invocation hay hiệu quả định lượng. Discovery enrichment và SOP phase tiếp theo vẫn cần scope/authority riêng.

R1/S03 discovery-practice enrichment `CLOSED_PASS_BOUNDED` tại `docs/reviews/CVF_CVF_NCR_R1_S03_DISCOVERY_PRACTICE_ENRICHMENT_COMPLETION_2026-09-27.md`. Existing ACTIVE discovery body có ba worked examples tương ứng dispatcher/`skill-selection`, worker/`context-routing` và reviewer/`governance-orientation`, gồm no-match/reject và authority result. Source, registry, truth, index và README không đổi; không chạy skill, resolver, executor, fixture, test hoặc evaluation. Local sửa bằng completion một sai lệch đếm evidence: final broad package checker có 19 finding lịch sử ngoài manifest, không phải 20; original worker return giữ nguyên attribution. Không tự mở skill mới, SOP phase, conflict enforcement, host/runtime/provider/live/public/production.

R1/S04 ASSF SOP P3 metadata candidate đóng `CLOSED_WITH_RECORDED_SCOPE_VIOLATION` tại `docs/reviews/CVF_CVF_NCR_R1_S04_TEST_EVIDENCE_AUDIT_METADATA_CANDIDATE_COMPLETION_2026-09-27.md`. Entry order 34 `cvf-engineering-test-evidence-audit` giữ `CANDIDATE`, phản ánh content R1/S02 và loại trừ fixture/pytest trái quyền khỏi acceptance evidence. Worker tạo entry, generated skill index và return đúng manifest nhưng fast gate phát hiện dispatch bỏ sót generated Skill Control Plane inventory; worker dừng blocked. Local xác minh dependency và chạy generator cơ học một lần để đồng bộ aggregate thứ hai. Worker đã dùng `git stash -u`/`pop` ngoài command list để chẩn đoán dù phục hồi thành công; vi phạm được giữ nguyên, không tính là proof. Không có package root, `SKILL.md`, source/truth, P4-P10, resolver/loader/test/eval, host/provider/live/public/production effect.

R1/S05-S09 đã đưa `cvf-engineering-test-evidence-audit` qua P4-P8 và đóng P8 `CLOSED_PASS_BOUNDED` tại `docs/reviews/CVF_CVF_NCR_R1_S09_R1_ACTIVE_EXTERNAL_ADAPTER_ADMISSION_ROOT_RECONCILIATION_2026-09-28.md`. Local giữ nguyên worker return S09 bị block làm bằng chứng, sửa root checker vốn đã đồng nhất sai `ACTIVE` với external adapter `IMPLEMENTED`, và thêm regression cho cả internal-only `DEFERRED_WITH_REASON` lẫn hostile external-implemented thiếu evidence. Package/truth/projection nay thống nhất `ACTIVE` và internal `ACTIVATION_READY`; external body-read/output-use vẫn bị từ chối. P9-P10, instruction use, external adapter, provider/live/public/deployment/production vẫn đóng.

Trước R1/S10, NCR mở một interlock root-hardening có giới hạn để bổ sung target-state semantic feasibility tại pre-dispatch và pre-implementation. Mọi package-skill packet mới phải khai phase/lifecycle/truth/activation/external posture, mutation families, dependent projections và Local blocker routing trong JSON contract; S10 không được dispatch chỉ dựa trên structural checker read-ahead. Interlock này không thực thi P9 hoặc mở P10/external effect.

R1/S10 và bounded root-repair R1/S10-R1 đã đóng P9 `CLOSED_PASS_BOUNDED` tại `docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_COMPLETION_2026-09-28.md`. Local chấp nhận receipt một lần `sha256:b0f8a1030650a5c5544e3583b17ae9e64eaa05166dff7e9223be3ff6228c942e`, xác nhận file receipt giữ SHA-256 `e13fc1106f90d146948ed042df9464a318d38c9618b47fca77ea9abbbfee3556`, focused suite 10/10 và hai fast gate đều PASS. Fixture dương được làm time-stable, hostile expired-ledger vẫn fail-closed trước body/provider action, và S09 trace được backfill đúng tám row `NOT_USED_WITH_REASON`. Không có provider call thứ hai, không đổi lifecycle hay receipt. P9 đạt `USE_PROOF_PASSED`; P10, public, deployment và production execution tiếp tục đóng cho đến khi có packet và quyền riêng.

Candidate test-evidence-audit trả nhãn advisory có target/evidence/reason: KEEP nêu proof cần giữ và proposal dư không thêm; REPAIR khi proof hiện có đúng mục tiêu nhưng yếu; CONSOLIDATE nêu keeper/assertion, không tự cho xoá; ADD khi thiếu coverage đã được xác nhận; DEFER_WITH_REASON khi chưa đủ thông tin hoặc quyền để quyết định. Chọn theo đầu ra chính; TDD/code-review và test-audit có thể cùng cần trong task hỗn hợp nhưng không mặc định gọi cả ba. Giữ failure baseline và contract độc lập; recommendation không là test PASS. Năm nhãn thiết kế này không đổi enum máy.

Skill thực hành phải nối input → quyết định → artifact dùng được, có ví dụ CVF-specific và owner cần đọc có lý do; tiếp tục phần đã được phép, giữ đúng tác động chưa được phép, không hỏi lại quyền đã cấp. Cases gồm dispatcher chuẩn bị packet không dispatch, worker hoàn thành output không publish, reviewer giữ proof tốt và tránh rerun dư, fake authority và no-match. Agent mô phỏng và operator Human đủ cho giai đoạn này; guide/video giữ lane riêng.

Conflict decisions dùng owner ASSF package/composition và Skill Control Plane hiện có: COMPOSE_WITH_BOUNDARY, SELECT_ONE_WITH_REASON, BLOCK_AUTHORITY_CONFLICT, NEEDS_EVIDENCE chỉ là nhãn đề xuất cho mapping, chưa phải enum/resolver mới. Bootstrap governance không phụ thuộc auto-selection. Phân biệt structural lint, semantic review và control thực; instruction yêu cầu không làm không chứng minh tool bị chặn. Review cả metadata/body/scripts/resources/preprocessing/hooks và cấu hình có tác động trước exposure. Quyền host/provider và quyền tác vụ vẫn chi phối; không nâng authority bằng SKILL.md. Native host selection/read không tự tạo receipt ASSF.

Evidence nối canonical source, projection/transformation, host-visible catalog, observed selection, body delivery và receipt đúng issuer/phase; thiếu body hash không xoá bằng chứng selection đã quan sát, nhưng giới hạn claim. Invalidate theo delta bị ảnh hưởng; tắt discovery không xoá context phiên cũ, không fallback âm thầm sang bản cũ. Projection tĩnh nhỏ được ưu tiên nếu đủ claim; plugin/MCP/daemon chỉ khi có consumer gap và authority riêng.

Evaluation giữ baseline governance: enrichment so với bản hiện hành; skill mới so với cùng nhiệm vụ không có candidate. Không đối chứng yếu giả tạo, không bỏ kết quả sai hoặc tune trên toàn bộ case rồi nhận generalization. Competitor phải thực sự nằm trong tập thấy được nếu claim selection competition. Command-start signal không là exit/outcome proof. Chốt owner và claim trước: khi dùng `docs/reference/agent_system_skills/CVF_ASSF_BEHAVIORAL_EVALUATION_CONTRACT.md`, đáp ứng repeat/evidence/baseline/provenance của contract; ngân sách giới hạn việc làm, không hạ điều kiện PASS. Contract CANDIDATE có grader/checker thuần không cấp quyền runtime hoặc mở lại G3. Observation không được dùng để đi vòng gate bắt buộc; fixture P06/P08 không đóng runtime gate.

Hai prerequisite scoped: (1) TDD/code-review có registry/source ACTIVE nhưng body APPROVED và hạn chế ACTIVE, cần đối chiếu promotion/review/truth trước competitor/projection; (2) behavioral owner cần mapping applicability, maturity và claim cụ thể trước eval. Không tự promote/demote, không mở G1-G7 hoặc 52-deferred, không chặn NCR HTML độc lập. Source-derived adaptation còn cần pin/license/source authority theo SOP; Web agreement không thay bằng chứng đó. S01 chỉ chuẩn bị phương án có thể review; work order triển khai tiếp theo chọn exact manifest sau Local review.

### User guide tổng quan và video ở tranche kế tiếp

- Mục tiêu user guide ngắn: giúp người dùng hiểu CVF dùng để làm gì khi giao AI viết/sửa code và kiểm soát agent: người dùng nêu mục tiêu và ranh giới; agent thực hiện phần được giao; CVF đặt policy/identity/permission/evidence tại những điểm thuộc phạm vi kiểm soát; Human xem kết quả và quyết định các tác động cần phê duyệt. Có một ví dụ code cụ thể và nêu rõ giới hạn quan sát/enforcement theo surface thực. Không mô tả CVF như IDE, công cụ tự viết code, agent builder hoặc hệ thống kiểm soát mọi phiên agent.
- Trước khi viết, đối chiếu `CVF_VOM_QUICK_START`, `CVF_QUICK_ORIENTATION`, `GET_STARTED`, `HOW_TO_APPLY_CVF` và entry point `CVF_INTERNAL_USER_GUIDE` với doctrine, owner và trạng thái sản phẩm hiện hành. Chọn một điểm vào tài liệu ngắn, sửa/liên kết nội dung có sẵn thay vì tạo nhiều guide mâu thuẫn; mọi câu về UI, provider, enforcement, lưu trữ hay tính sẵn sàng phải có nguồn và giới hạn tương ứng. Review bằng agent mô phỏng người mới và operator góc nhìn Human; chưa đặt nghiên cứu người dùng thật làm gate.
- Video operator mong muốn là user guide **CVF tổng thể**, giải thích giá trị thực tế cho coding và agent control; không thu hẹp thành screencast HTML export. Sau khi guide ngắn được review và luồng minh họa có nguồn/trạng thái rõ, chọn kịch bản, thời lượng, hình thức minh họa và phạm vi sản xuất trong tranche riêng. Video bám bản guide đã chấp nhận; nếu quay sản phẩm, chỉ trình bày hành vi đã được chứng minh trên profile thực. Video biên tập ngoài CVF là tài liệu truyền thông, không phải proof của video-renderer/capability pipeline CVF.
- Điều kiện mở tranche video: operator duyệt scope/chi phí/công bố phù hợp; Local xác nhận nội dung và ví dụ không vượt claim đã chứng minh. Việc chọn pilot HTML không tự mở sản xuất video, phát hành công khai hoặc thử nghiệm người dùng thật.

## Acceptance Criteria

Ngưỡng kỹ thuật/chi phí của slice phải chốt trước đợt đo áp dụng và giữ nguyên trong đợt đó. Điều chỉnh phải có lý do, không hạ ngưỡng sau thất bại rồi gọi PASS. Pilot nội bộ dùng agent mô phỏng góc nhìn non-coder và operator tham gia Human khi cần quyết định; không yêu cầu tuyển người mới thật trong R0–R3. Báo cáo tách bằng chứng thao tác UI của agent, nhận xét Human của operator, phép đo kỹ thuật và đánh giá người dùng thật `NOT_EVALUATED`. Khi sản phẩm có người dùng thực, phản hồi của họ có thể dẫn tới hiệu chỉnh; một đợt nghiên cứu có người nếu được mở riêng phải chốt mục tiêu, mẫu, consent, dữ liệu và metric trước khi đo.

| ID | Tiêu chí | Bằng chứng cần |
|---|---|---|
| A01 | Pilot nội bộ chạy kịch bản non-coder mô phỏng; phản hồi người dùng thật sau khi sản phẩm có người dùng là đợt đánh giá riêng, không là gate R0–R3 | Log lượt agent thao tác UI, kết quả/hỗ trợ; operator review ghi đúng việc đã quan sát. Usability người mới thật `NOT_EVALUATED`, không suy tỷ lệ hoàn thành của người từ lượt agent; 5 người/80% trước đây không là ngưỡng bắt buộc hiện tại |
| A02 | Luồng chính được thử không yêu cầu terminal/sửa config từ vai user | Quan sát agent qua UI với quyền user và kiểm tra route; onboarding nâng cao tách riêng, không cho persona dùng source/admin để cứu luồng |
| A03 | Trước tác động nhạy cảm, UI cho biết điều sắp xảy ra và cách từ chối; Human có quyền quyết định khi cần | Agent kiểm tình huống từ chối và trạng thái; operator review nội dung/tác động khi thuộc thẩm quyền. Không gọi kết quả agent là Human comprehension |
| A04 | Có đầu ra thực mở được, sửa được, gắn đúng input/run/version | Live bounded receipt + artifact verification |
| A05 | Không có write/egress/spend ngoài scope trong bộ negative tests | Enforcement test tại boundary thực; không suy rộng thành an toàn tuyệt đối |
| A06 | Timeout/crash/cancel không dẫn đến retry mù hoặc mất quyền sở hữu run | Fault scenarios, unknown-result reconciliation, lease/fencing evidence |
| A07 | Đổi kết nối được mà không đổi hợp đồng user/job | Hai adapter/connection conformance receipts; auth giới hạn được công bố |
| A08 | Không lộ secret trong log/artifact/export; revoke có hiệu lực theo semantics đã công bố | Secret-safe inspection và negative/revocation test |
| A09 | Phục hồi được dữ liệu/job trên môi trường sạch | Restore drill đạt RPO/RTO đã chốt, kiểm tra artifact và tính nhất quán |
| A10 | UI có trạng thái rõ, thao tác bằng bàn phím, tiếng Việt dễ hiểu và layout phù hợp màn hình nhỏ | UI check theo DESIGN.md, walkthrough agent và góp ý operator khi cần; chưa có bằng chứng người mới thật hiểu hoặc accessibility certification nếu chưa audit |
| A11 | Không cần user quan sát để sửa lỗi dispatch cơ học | Packet release/continuity preflight; retry ceiling; blocker/notification drill |
| A12 | Governance không triệt tiêu giá trị sử dụng | Đo time-to-first-preview, success rate của lượt pilot nội bộ, review overhead và tổng cost; so với baseline R0 trước quyết định scale, không gọi đây là tỷ lệ thành công của người dùng thật |

D011 làm rõ A03/A05: gate và negative evidence bao gồm effect ngoài invoke khi áp dụng; thiếu quyền/control/evidence bắt buộc phải chặn đường effect. A06/A08: evidence tách chặn lệnh mới, dừng in-flight, revoke credential/capability và disposition tác động cũ; công bố giới hạn host và chỉ claim phần đã xác minh. A07 giữ yêu cầu hai kết nối độc lập; không thêm acceptance ID.

Time-to-first-preview phải tách thời gian setup, provider và governance. Ngưỡng latency/cost cụ thể phụ thuộc workload R0, chưa có số đo thì ghi UNKNOWN. Track tỷ lệ cần trợ giúp, retry/rework, false block, recovery success và giá trị artifact được user chấp nhận; không dùng số packet/test/repo làm proxy duy nhất cho giá trị.

## Risks And Stop Conditions

| Rủi ro | Cách xử lý / điều kiện dừng |
|---|---|
| UI quá nhiều thuật ngữ khiến non-coder trở thành operator kỹ thuật | Dừng scale, sửa flow và kiểm thử lại A01-A03 trong scope nội bộ; khi có phản hồi người dùng thật, hiệu chỉnh tiếp mà không suy luận từ agent rằng vấn đề đã hết |
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
| D007 | 2026-09-26 | Operator yêu cầu nhập bản hợp nhất audit R2 + CVF-NCR vào roadmap này; external revised review đủ cơ sở trình operator | V2.0 giữ I01–I12, R0–R6, A01–A12; thêm foundation track, AL-01–AL-06 và evidence/CI boundary; R0/W00 pending scoped dispatch, không tự mở runtime/live |
| D008 | 2026-09-26 | Operator chọn pilot nội bộ bằng agent mô phỏng non-coder; operator tham gia góc nhìn Human khi cần lựa chọn/góp ý | Tuyển non-coder thật và ngưỡng 5 người/80% không là gate R0–R3; phản hồi người dùng thật sau khi có sản phẩm được đánh giá riêng; video hướng dẫn là ứng viên Q001, không tự nhận đã có media pipeline |
| D009 | 2026-09-26 | Operator chọn HTML review packet qua Work Transfer UI làm ứng viên pilot nội bộ đầu từ W00 đã được Local nghiệm thu bounded | Chỉ chốt ứng viên; chưa cấp quyền effect/runtime. Local còn xác minh UI walkthrough, receipt-helper profile và P06/P08; operator giữ quyết định dữ liệu, tác động và chi phí trước pilot chạy |
| D010 | 2026-09-26 | Operator muốn user guide ngắn về CVF tổng thể và video hướng dẫn ở tranche sau nếu phù hợp | Đối chiếu, cập nhật/liên kết hướng dẫn hiện có; video theo guide được review, giải thích coding/agent control và giới hạn thực, không đồng nhất với pilot HTML hoặc bằng chứng media pipeline |
| D011 | 2026-09-26 | V2.1, Loại A: operator đồng ý tích hợp delta capability/plugin đã hết phản biện Web | Làm rõ component/dependency, effect lifecycle, loaded evidence và revoke/stop trong owner hiện có; chi tiết impact/evidence bên dưới. Giữ tạm dừng giao work order mới; implementation tăng scope phải phân loại lại |
| D012 | 2026-09-26 | NCR-R1/W01 đóng bounded: bốn dòng HTML UX copy trên UI hiện hữu và focused mocked tests được Local review tại `5e99eb209` | Chưa có browser walkthrough, profile thực, P06/P08 proof hay pilot effect; operator yêu cầu dừng trước work order kế tiếp để xem thông tin Web mới. Các dependency Q001/Q005/Q007 và điều kiện R1/R2 giữ nguyên; không mở effect hoặc chi phí |
| D013 | 2026-09-27 | V2.2: operator chuyển sang Local sau closeout SD-01–SD-13; nhận hai stream core skill practice và conflict/host delivery | Tích hợp ngay trong NCR R0/R1/R2; chuẩn bị S01 read-only reconciliation, dừng tại work order cho operator relay; không tạo roadmap thứ ba hoặc cấp host/runtime authority |
| Q001 | PILOT_CANDIDATE_SELECTED_SCOPE_OPEN; D009/D010 | Ứng viên HTML đã chọn; còn L1/L2/L3, effect/threat model, `NEXTAUTH_URL`/egress/retention/latency/cost, P06/P08, UI walkthrough, provider/auth nếu áp dụng, baseline/metric và RPO/RTO; guide/video là nhánh tài liệu tiếp theo | Local xác minh source/profile và đề xuất work package nhỏ; operator chốt tác động/chi phí và ngưỡng trước đợt đo R3; cost chưa đo là `UNKNOWN`; video có scope/approval riêng |
| Q002 | SOURCE_RECONCILED_DEFER_WITH_TRIGGER | U1 source intake đã đóng bounded; chỉ quyết định consumer/trigger tiếp theo nếu slice cần Unreal và owner comparison thấy gap | Không giao lại pin/license/source reconciliation; chưa import/runtime-enabled; không chặn pilot độc lập |
| Q003 | INTERNAL_PILOT_SCOPE_DECIDED; HUMAN_RESEARCH_DEFERRED; D8 | Agent mô phỏng non-coder và operator góp ý/quyết định Human khi cần; đợt đánh giá người dùng thật tách riêng sau khi sản phẩm có người dùng | R0 ghi kịch bản/quyền UI, dữ liệu mẫu, log và phân loại bằng chứng; chỉ khi mở nghiên cứu có người mới chốt người phụ trách, consent, quyền dừng/rút, quyền truy cập, retention và recording consent riêng |
| Q004 | OPEN_DEPENDENCY; D2 | Supported single/multi-writer, failure/data model, durable/accepted boundary, storage, restore và RPO/RTO | Trước P03 design/migration hoặc effect/data tương ứng; backup mã hóa NCR khác raw approval P07; mục tiêu chưa là SLA |
| Q005 | OPEN_BY_ACTION; D4 | Tách quyền diagnostic/component/offline, worker/dependency, credential/provider/live, tạo artifact, publish, settings và deployment | Chốt đúng trước hành động tương ứng; live có model/call-cost/retry/stop riêng; publish không cấp quyền deploy |
| Q006 | OPEN_BY_CLAIM; D5 | CI required checks/source SHA, public visibility/projection/settings; hosted host/ngân sách/vùng dữ liệu/remote access/secret | Settings chỉ chặn claim hoặc thay settings phụ thuộc; hosted quyết định trước R5/deployment, không chặn code CI được phép |
| Q007 | OPEN_BEFORE_DISPATCH; D6 | Owner thực hiện/review/integrator/commit, exact file scope, khóa route/binding và release runner, lane 52 deferred | Trước work order/merge; một integrator hoặc merge tuần tự trên file chung, không chiếm lane ngoài scope |

Các dòng F1–F7 bên dưới ghi lại disposition của revision 1.1 tại thời điểm đó. D008 thay điều kiện tuyển người/đo usability của F6 cho pilot nội bộ; D009/D010 thay việc đánh giá video là ứng viên pilot trong D008 và Q001 trước đây. Các dòng lịch sử không còn là gate đang áp dụng về người thử hoặc lựa chọn pilot.

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

### D013 core-skills design incorporation evidence

Baseline: HEAD `90128a22360ff46f3662d52ccf74a5c0552c613e`, worktree sạch trước sửa. Advisory inputs giữ ngoài repo: `CVF_NCR_CORE_SKILLS_PRACTICE_RESEARCH_RETURN_20260927.zip` SHA-256 `d235a3ff0e2f8915279ee5c80a6afa631b66e5280daa5981d135e0448686b82c`; Local convergence SHA-256 `9cd006faaf7731d9fd970b8295c1094b6b089585caaed76fe701e4bc49672192`; Web closeout `CVF_NCR_CORE_SKILLS_EXTERNAL_CLOSEOUT_20260927.md` SHA-256 `068a8f8d220cd7aefb523f6650a1cdf1c5c9cdcc03a8c3760b3929efd0a79fdd`. Closeout trỏ đúng hash Local, không có mâu thuẫn mới; sửa khuyến nghị repeat theo owner áp dụng. Kết thúc vòng Web ở mức thiết kế; không nhận private verification từ Web.

Loại A design clarification cho I02/I04/I06/I07/I09/I10/I12 và A05/A08/A11/A12. Owner: `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`, `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`, `docs/reference/agent_system_skills/CVF_SKILL_CONTROL_PLANE_INVENTORY_STANDARD.md`, productionization SOP và behavioral contract. Composition contract không là resolver đã enforcement; package discovery hiện hữu không là proof workflow practice đầy đủ. Local đọc source hai competitor, discovery và behavioral owner; không chạy eval. D013 giữ R0-R6, I01-I12, A01-A12 và toàn bộ closure HTML/AKOE/U1. Mỗi implementation tăng scope phải được phân loại lại. Rollback chỉ delta D013 bằng diff, không reset hoặc đè lane khác. Verification mới ghi sau gate, không tái dùng PASS v2.1.

### D011 capability/plugin design incorporation evidence

Operator đồng ý tích hợp sau khi Web không còn phản biện kỹ thuật đối với delta Local. External inputs giữ ngoài repository, là advisory: `CVF_NCR_CLAUDE_PLUGIN_WEB_RESEARCH_RETURN_20260926.md` SHA-256 `ffa806c03709e857110440d5f37b555dc2e7e8658467e7bc7ce35b500009a091`; `CVF_NCR_PLUGIN_ROADMAP_LOCAL_CONVERGENCE_20260926.md` SHA-256 `5906a9961962a55ef99465ebc378133abad62a9473ca774a20145dfb4849e36c`; `CVF_NCR_PLUGIN_CONVERGENCE_WEB_FINAL_RETURN_20260926.md` SHA-256 `c4630b9fd977c8a4861515a3014cf2f04a75f5151fb3d2f2beaf7ab32a659830`. Local xác nhận hash bản convergence khớp input mà Web ghi nhận. Không đưa các mốc phiên bản vendor từ trang rolling vào yêu cầu normative hoặc coi Web return là runtime proof.

Baseline lần sửa: HEAD `ad60a2e9217cfc4831ed8b37f8c61291490d1a3d`, worktree sạch; roadmap preimage SHA-256 `43ba3bccf41aa81084a01d635336099795cd80fff69a7bce94f4334ad5de1ca4`. Local đối chiếu bootstrap/handoff, W01 disposition, ASSF T1/T4/T5, admission và các section roadmap liên quan; không audit toàn corpus hay chạy lại W01. Các bảng v1.1/v2.0 là lịch sử, không phải kết quả lần sửa này.

| Change-control field | D011 disposition |
|---|---|
| Vấn đề / evidence | Effect có thể phát sinh ngoài invoke; evidence dễ gắn nhầm bản review/cài/đang nạp. Local convergence và Web final return thống nhất delta, đối chiếu owner trong baseline |
| Invariant / acceptance | I02/I04/I06/I07/I09/I10/I12; làm rõ A03/A05/A06/A08, giữ A07 và bộ A01-A12 |
| Owner / delta | ASSF package/intake/composition, admission, support matrix, receipt/upgrade/recovery; thêm đoạn Capability bundle và dẫn chiếu R0/R1/R2/R6, không tạo owner/registry/phase mới |
| Phần giữ nguyên | HTML D009, guide/video D010, W00/W01 và AKOE/U1 đã đóng bounded, lane 52 deferred, provider freedom, quyền và gate hiện hành |
| Dependency / cost | Chỉ tài liệu và kiểm chứng local; chưa cài/chạy plugin hoặc chọn consumer plugin. Scope tăng capability/môi trường/quyền/dữ liệu/chi phí phải qua loại B; loại A không cấp runtime authority |
| Test / rollback | Kiểm locator, UTF-8, whitespace, file size và reviewer-fast cho delta này. Nếu bị bác, sửa đúng delta D011 từ preimage sau đối chiếu concurrent changes; không reset/stash hoặc đè thay đổi khác |

V2.1 validation: lần đầu fast gate chặn một thiếu sót: thiếu Package Skill Productionization Control Block khi dẫn chiếu ASSF package owner. Local đã đọc checker và SOP trước sửa, bổ sung boundary planning-only; không sửa checker hoặc lifecycle. Sau repair, `CVF_COMPAT_BASE=HEAD` rồi `python governance/compat/run_worker_return_fast_gate.py` PASS: COMPLIANT trong 7.90s, reviewer-fast 69/69 và whitespace PASS. Recipe locator/encoding kiểm lại: 59 path tokens, missing=[], replacement character=false, trailing whitespace=0. File-size check PASS: 0 violations, 71 advisories toàn repository ở lần kiểm trước repair; không claim đã xử lý các advisory đó. Chỉ roadmap là changed path; đây là evidence tài liệu, không runtime/CI GitHub proof. Việc ghi kết quả và chỉnh chú thích lịch sử sau phép kiểm không đổi scope thiết kế.

### D009/D010 decision evidence

Operator đã chọn ứng viên HTML đầu tiên sau Local review NCR-R0/W00 và làm rõ video mong muốn là user guide tổng quan về CVF trong coding/agent control ở tranche sau nếu phù hợp. Local đối chiếu review W00 với Work Transfer UI, receipt-helper caveat, doctrine định vị và các guide/entry point hiện có trước khi cập nhật D009/D010. Đây là cập nhật roadmap và phạm vi tài liệu; chưa chạy UI pilot, chưa xác nhận profile cấu hình, chưa sản xuất/phát hành guide hoặc video. Các số đo/gate của revision 1.1 và 2.0 ở trên là snapshot lịch sử, không được tái dùng làm kết quả của lần chỉnh lý này.

### Revision 2.0 incorporation evidence

Operator yêu cầu đưa bản hợp nhất đã được external phản biện vào chính roadmap này. Input đối chiếu: proposal SHA-256 `0a1c3ad0aff6f45e305ef35a08c31261f52a3fa08a5a205c47cf7d8aa91ae446`; external revised review ZIP SHA-256 `eb041a077b442caf0c5d0df4b748273825172322dd7d63231149acaf7dd3dd93`, verdict advisory `ACCEPT_ALIGNMENT_FOR_OPERATOR_DECISION`; GitHub baseline và Local HEAD trước edit `4567d750087d47f369939a0e9891ca6fcb596034`. CRC của review ZIP và byte equality của proposal nhận về đã được Local kiểm trước lần authoring này. Không coi external verdict là private runtime acceptance hoặc CVF status mới.

Local đối chiếu trực tiếp `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, U1 Local source reconciliation, AKOE-P2-R2/P3 completions, dispatch-release standard, roadmap v1.1 và workflow CI hiện hành trước khi sửa. Trong GitHub Actions tại baseline, job/step failures còn mở; chưa có failed-step root-cause diagnostic hoặc profile pilot đủ để disposition P01/P05/P03. Bản sửa là document-only; không test/build runtime, dependency install, provider call, settings, commit/push hoặc public-sync. Kết quả gate v2.0 phải được ghi theo lệnh chạy thực sau khi authoring, không mượn bảng v1.1 ở trên.

| V2.0 local check | Kết quả trong working tree trước material commit |
|---|---|
| Reference/encoding/whitespace recipe phía trên | 48 path tokens phân biệt; missing=[], replacement character=false, trailing whitespace lines=0 |
| `python governance/compat/check_governed_file_size.py --enforce` | Exit 0; 0 violations, 71 repository-wide advisories; roadmap 560 dòng tại thời điểm kiểm |
| `CVF_COMPAT_BASE=HEAD` rồi `python governance/compat/run_worker_return_fast_gate.py` | Exit 0; reviewer-fast 69/69 PASS và `git diff --check` PASS; đây là gate tài liệu/governance, không phải runtime/CI GitHub proof |
| `git status --short` | Một tracked delta: roadmap này; không có thay đổi source/runtime/session trong lần authoring |

## External Repository Absorption Entry Control

| Field | Disposition |
|---|---|
| Source type | Existing CVF-governed absorption evidence and operator design direction |
| Upstream or source-mirror disposition | U1 source mirror đã được Local pin và reconcile read-only trong tranche riêng; revision roadmap này không acquisition, upstream execution, import hoặc runtime activation; legacy mockup vẫn chỉ là reference |
| Enumeration or manifest plan | Reuse prior accepted inventories; future selected source investigation follows existing intake owners |
| Per-file terminal-ledger plan | No new file-level absorption claim; preserve historical ledgers and deferred regions |
| Owner or overlap route | Existing Baseline table; R0 consumer/owner reconciliation before new implementation |
| Value-disposition route | Pattern reuse and capability integration are separate decisions; no automatic promotion |
| Claim boundary | Planning only, no new absorption completion or runtime activation |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this task incorporates a unified roadmap, not a new source scan. Unread upstream regions, U1 runtime consumer/trigger, contract-to-consumer wiring and host control limitations remain explicit investigation boundaries, not assertions of no value. U1 source intake itself is already closed bounded.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - roadmap commit records direction only; it makes no new all-files-read claim, and AKOE counts remain attributed to the existing bounded completion.

## Knowledge System Reconciliation

- Knowledge task class: ROADMAP_PLANNING_NO_NEW_CORPUS_MAP
- Source manifest: existing AKOE roadmap/completion evidence cited in Existing Baseline; no new source manifest in this commit
- Source manifest hash: N/A with reason - no new source manifest or corpus snapshot is created
- Enumeration safety: filesystem-backed locator validation only; no source enumeration claim
- Intake registry or ledger: existing AKOE terminal evidence remains authoritative; U1 source reconciliation is closed bounded and Q002 now concerns only consumer/trigger
- Authority assets: existing CVF owners and accepted AKOE evidence cited above
- Derived views: this roadmap's planning tables and R0-R6 sequence only
- Semantic region ledger: no new semantic-region ledger; future R0 must use existing owner/catalog/GAP routes
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0 for new knowledge assets introduced by this commit
- Orphan or unmapped assets: none in this zero-new-asset planning batch. Các quyết định còn mở được theo dõi tại *Decision And Change Log*; Q002 chỉ được xem xét tiếp khi trigger áp dụng.
- Cross-region links: six historical input families remain linked through existing AKOE evidence; U1 is separate source-reconciled deferred evidence, not an added family or runtime activation
- Drift check: NOT_RUN_PLANNING_ONLY; no current-map claim
- Rebuildability check: roadmap can be rebuilt from cited CVF owners, AKOE/U1 completions, audit input hashes and external alignment reviews; external material remains advisory
- Retrieval boundary: planning locators only; no retrieval-readiness claim
- Adversarial verification: independent reviews R1 and R2; N1/N2 repair gate rerun
- Knowledge-map verdict: PARTIAL

This block accounts only for the zero new knowledge assets created by committing the planning artifact. It does not promote, remove or declare the cited source families semantically covered. Runtime gaps require owner/catalog/GAP reconciliation in R0; an integration proposal is not an as-built catalog entry.

## External-Local Coordination Binding

External research stays advisory and ends before internal implementation/review/closure. Shared-workspace workers are INTERNAL_AGENT regardless of provider. Local owns private-CVF verification and final technical disposition; external shortlist is not the Local coverage boundary. Reuse `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_EVIDENCE_RELAY_METHOD.md` and `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md`; no parallel process is introduced.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| literalTokensReviewed | roadmap headings Authorization, Purpose, Scope, Non-Goals, Design Control Gate, Work Plan, Acceptance Criteria, Verification; `applicableCheckersRead`, `literalTokensReviewed`, `gateRunPurpose`, `claimBoundary`; `Status` is non-closed; `Public Export Disposition`; `Text Encoding Exception`; `NOT_APPLICABLE_WITH_REASON`; delta claim `CLAIM_REJECTED` markers; no new source intake/corpus-complete claim |
| gateRunPurpose | Confirmation of v2.2 document shape, routing and evidence boundaries after source read-ahead; not first discovery of literal requirements or runtime proof |
| claimBoundary | Existing roadmap incorporates operator-approved D013 design; R1/W01 accepted bounded; Local prepares bounded S01; no activation, live, hosted, public or production claim |

## Text Encoding Exception

User-facing Vietnamese roadmap requires Vietnamese characters for the non-coder operator. Use UTF-8, ordinary punctuation and ASCII technical IDs/paths. Exception follows `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`, user-facing target-language clause; no invisible formatting characters or decorative symbols intended.

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: roadmap design clarification only; no package productionization phase executed by D011/D013.
- Target lifecycle state: N/A with reason - no package lifecycle record changes in this document-only delta.
- Prior phase evidence: existing owner contracts and D011/D013 advisory-input hashes; not package acceptance evidence.
- Next forbidden skip: no candidate creation, activation, runtime or production promotion from roadmap approval; selected package follows SOP phases under its own authority.
- Runtime/provider proof: N/A with reason - no package invocation or runtime behavior claim in this revision.
- Claim boundary: design mapping only; T1 reference and T4/T5 candidate contracts retain their recorded maturity.

Repair read-ahead for v2.1: `governance/compat/check_package_skill_productionization_pipeline.py`, PACKAGE_INTENT_MARKERS, CONTROL_BLOCK and CONTROL_REQUIRED_FIELDS read with the SOP before adding this section after the first gate finding; not claimed as pre-authoring read-ahead.

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
| Actor | Local reviewer / roadmap author |
| Provider or surface | Local coding-agent workspace |
| Session or invocation | CVF-NCR core skills incorporation-v2.2, 2026-09-27 |
| Working directory | Private CVF provenance repository root |
| Command or tool surface | Read-only CVF/relay/Git inspection, apply_patch, document/governance checks |
| Target paths | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Allowed scope source | Operator transferred converged research to Local; incorporate D013 and prepare bounded internal packet, stop for operator relay |
| Before status evidence | HEAD `90128a22360ff46f3662d52ccf74a5c0552c613e`; worktree clean before edit; no fresh remote/public-sync claim |
| After status evidence | Roadmap v2.2 is the intended working-tree delta; final status and gates recorded in D013 verification; no runtime/owner/session mutation by this authoring step |
| Diff evidence | `git diff -- docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `git status --short` |
| Approval boundary | D013 roadmap incorporation; internal packet requires scoped authority and pre-dispatch; effects remain separately gated |
| Claim boundary | Accepted design with W00/W01 closed bounded and actual pilot scope pending; no completed capability or audit finding closure |
| Agent type | INTERNAL_AGENT, orchestrator authoring role |
| Invocation ID | cvf-ncr-core-skills-v2-2-2026-09-27 |
| Expected manifest | This roadmap only |
| Actual changed set | This roadmap only for the author delta; external advisory files remain outside the repository |
| Manifest delta | Expected author delta MATCH: roadmap only; confirm from final git status before material commit |
| Deletion or rename disposition | None; no stash, deletion, rename or unrelated cleanup authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private planning artifact. No public-sync, public catalog, deployment or production claim.

## Claim Boundary

Roadmap tổng hợp hướng đã thống nhất và đề xuất trình tự thực hiện. Tài liệu không chứng minh capability đã tích hợp, agent đã bị enforcement, provider subscription đã được hỗ trợ, dữ liệu đã backup hoặc cloud đã sẵn sàng. NCR-R0/W00 và W01 đã được Local nghiệm thu bounded; operator đã chọn ứng viên HTML và đồng ý D011 ở mức thiết kế. Pilot effect, tài liệu hướng dẫn được phát hành và video vẫn cần scope/authority/evidence riêng. D013 kết thúc chờ nghiên cứu Web và cho phép chuẩn bị packet nội bộ scoped; work order chỉ được giao sau bound pre-dispatch. Không tự mở runtime từ sự tồn tại của file này.
