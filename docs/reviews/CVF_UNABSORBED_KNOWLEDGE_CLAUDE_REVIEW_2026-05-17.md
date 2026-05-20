# CVF Unabsorbed Knowledge Claude Review - 2026-05-17

Memory class: FULL_RECORD

Status: APPROVE_WITH_CHANGES

## Purpose

Trả lời packet review của Codex tại
`docs/reviews/CVF_UNABSORBED_KNOWLEDGE_CLAUDE_REVIEW_PACKET_2026-05-17.md`.

Review này đánh giá hai mảng tách biệt:

1. tính chính xác và đầy đủ của
   `docs/reviews/archive/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`;
2. tính hợp lý của reporting correction được đề xuất trong
   `docs/roadmaps/CVF_UNABSORBED_KNOWLEDGE_REPORTING_CORRECTION_ROADMAP_2026-05-17.md`.

Review không authorize implementation, doctrine promotion, hay public claim
change nào.

## Scope

Trong scope:

- inventory accuracy spot-check chống lại nguồn private và runtime-owned
  closure packets;
- priority assignment cho 10 actionable items;
- corrective rule shape và trigger conditions;
- chọn first authorized roadmap;
- claim boundary cho future agents.

Ngoài scope:

- absorption thực sự của bất kỳ item nào;
- promotion ADD-A/ADD-D doctrine;
- mở GC-018 cho Observability Plane;
- public README changes.

## Source

Đã đọc:

- `docs/reviews/archive/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
- `docs/reviews/CVF_OPERATOR_PROGRESS_AND_UNABSORBED_KNOWLEDGE_REPORT_2026-05-17.md`
- `docs/roadmaps/CVF_UNABSORBED_KNOWLEDGE_REPORTING_CORRECTION_ROADMAP_2026-05-17.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_REPORTING_CORRECTION_REBUTTAL_2026-05-17.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_CLAUDE_REVIEW_PACKET_2026-05-17.md`
- `docs/baselines/archive/CVF_16_5_LIVING_INTEGRATION_CLASSIFICATION_SUMMARY_2026-05-16.md`
- `.private_reference/legacy/CVF 16.5/abtop/CVF_OBSERVABILITY_PLANE_FOUNDATION/README.md`
- `.private_reference/legacy/CVF ADD/REVIEW FOLDER/` (8 synthesis files)

Đã spot-check:

- `EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/evolution_engine/` (7 files,
  549 LOC tổng, 1 contract + 6 helpers)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` (67 files)
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/` (20+ agent/orchestration
  contracts)
- `EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME/observability/`
  (11 files với observe-only signal contract)

## Findings / Position

### Vị trí tổng thể

Inventory là một bước đúng và cần thiết. Reporting correction packet (roadmap
+ rebuttal + Claude review gate) thể hiện đúng governance discipline mà CVF
yêu cầu. Tôi approve nhưng cần một số chỉnh sửa accuracy trước khi inventory
được dùng làm input cho roadmap selection.

### Inventory accuracy findings

**Overstated items (cần downgrade):**

1. **GAP-AGENT overstated.** Tôi (phiên bản inventory) claim "Agent registry,
   Permission profiles, Structured handoff contract, Orchestration rules đều
   chưa có". Spot-check thực tế cho thấy CPF đã có:

   - `agent.registration.batch.contract.ts` (registry)
   - `agent.definition.boundary.contract.ts` (permission profile)
   - `agent.definition.capability.batch.contract.ts` (capability)
   - `agent.definition.audit.batch.contract.ts` (audit)
   - `agent.scope.resolution.batch.contract.ts` (scope)
   - `orchestration.contract.ts` + 3 pipeline variants (orchestration rules)

   GAP-AGENT thực tế **không tồn tại** ở dạng đã claim. Cái còn thiếu là
   structured handoff contract và một kiểm chứng tích hợp giữa các contracts
   hiện có. Item này phải remove khỏi inventory hoặc rewrite hoàn toàn.

2. **GAP-MEM partially overstated.** Tôi claim "9 sub-contracts còn thiếu".
   Thực tế LPF có 67 files, trong đó:

   - `controlled.memory.gateway.contract.ts` (gateway)
   - `learning.reinjection.contract.ts` + pipeline variants (reinjection)
   - `feedback.ledger.contract.ts` (ledger)
   - 60+ contracts khác cho governance signals, evaluation, observability

   Phần thực sự thiếu là **memory-specific** sub-contracts: privacy filter,
   capture adapter, retention policy. Không phải 9 như claim. Số chính xác
   là **3-4 sub-contracts** cần thêm, không phải 9.

3. **GAP-SKILL slightly overstated.** Skill Evolution Loop có 7 files:

   - `governed.skill.evolution.contract.ts` (411 LOC, đầy đủ)
   - 6 helpers ngắn (13-40 LOC mỗi) — không phải "stub ~300 bytes", thực tế
     là **minimal executable implementations**, không phải placeholder

   Đây là design choice có chủ ý: contract là authority, helpers là execution
   skeleton. Không phải gap nghiêm trọng. Cần rewrite thành "executable
   components nhỏ, cần được expanded khi skill governance scenarios cần"
   thay vì "stub chưa implement".

**Understated items (cần upgrade):**

4. **OBS-1 understated value.** Inventory cho OBS-1 4 sao. Spot-check spec
   cho thấy đây là cái duy nhất mà:

   - không có owner surface CVF nào hiện đang gánh
   - hoàn toàn read-only theo design (R0)
   - cung cấp visibility mà operator hiện không có cách nào khác lấy được
   - spec 9 file đã ready

   Đáng 5 sao. OBS-1 là implementation candidate có giá trị/risk ratio tốt
   nhất trong toàn inventory.

**Accurate items:**

- ADD-A, ADD-D, ADD-B, ADD-C1, ADD-C2, ADD-E1, ADD-PROVIDER đều được phân loại
  chính xác theo synthesis Codex/Claude trước.
- Nhóm 4 (excluded) đúng và đầy đủ.

**Đã absorbed nhưng vẫn liệt kê (cần remove):**

- Không phát hiện. Inventory không claim sai về việc gì đã absorbed.

**Omitted valuable items (cần thêm vào inventory):**

5. **Brief Normalization Doctrine** từ Phase A synthesis — bị tôi gộp vào
   ADD-D nhưng thực ra là một item riêng đáng track. Synthesis Phase A nói
   nó nên về layer planning/roadmap/agent operating contract. Đáng track
   riêng nếu mở doctrine promotion packet.

6. **W7 signal candidates** (`path_lock_signal`, `minimal_response_match`,
   `restricted_path_count`) — đã mention trong ADD-D nhưng đáng là item
   riêng vì có thể absorb vào evidence receipt schema mà không cần promote
   toàn bộ ADD-D doctrine.

### Priority challenge findings

- **ADD-A + ADD-D as doc-only immediate:** Approve. Đây là quyết định chính
  xác. Synthesis Phase A từ 2026-05-07 đã rõ ràng đề xuất "first and only
  public promotion candidate". Không có rủi ro runtime.

- **OBS-1 as highest-value implementation candidate:** Approve và upgrade.
  Read-only design + spec đầy đủ + không overlap với owner surface nào hiện
  có = candidate sạch nhất. Cần là roadmap thứ hai sau ADD-A/D.

- **Memory, Skill, Agent, Provider as separate roadmaps:** Approve "separate"
  decision nhưng cần adjustment dựa trên accuracy findings ở trên:

  - GAP-AGENT phải close hoặc rewrite, không cần roadmap mới
  - GAP-MEM scope thu hẹp xuống 3-4 sub-contracts cụ thể
  - GAP-SKILL không phải priority vì stubs đủ để giữ boundary
  - ADD-PROVIDER vẫn là roadmap riêng đáng làm

- **Deferred status for B, C1, C2, E1:** Approve. Lý do defer trong synthesis
  vẫn còn nguyên giá trị. Không có thay đổi nào cần.

### Reporting correction findings

Reporting correction proposed trong roadmap là **chính xác và cần thiết**,
NHƯNG cần narrow hơn so với bản hiện tại:

- Trigger phải rõ ràng: chỉ apply cho (a) external-knowledge absorption
  closure, (b) GA/RC release, (c) tranche-series closure (≥3 tranches cùng
  scope). Không apply cho mọi closure.

- Required summary fields đã đủ.

- Còn thiếu **enforcement surface**: rule này không có gì enforce nó. Đề
  xuất bổ sung: thêm một line item vào release-gate checklist hoặc tranche
  closure template để kiểm tra "đã có operator-facing summary cho unabsorbed
  reviewed knowledge?". Không cần code, chỉ cần checklist.

- Risk "có thể bị mistake cho implementation authorization" đã được Codex
  rebuttal handle đầy đủ qua các non-goal statements.

## Rebuttal

### Đối với Codex rebuttal

Codex rebuttal đã challenge 5 điểm và tự trả lời. Tôi đồng ý với 4/5:

1. **"Is this overcorrection?"** Codex nói "Yes if applied broadly".
   Tôi đồng ý nhưng yêu cầu **trigger conditions phải explicit trong rule
   text**, không chỉ trong commentary.

2. **"Did operator report absorb too quickly?"** Codex nói "First version
   risked that interpretation". Tôi đồng ý mitigation đã đủ.

3. **"Promote ADD-A/ADD-D immediately?"** Codex nói "Not from this correction
   packet alone". Tôi đồng ý — packet này không phải doctrine promotion.

4. **"Open Observability Plane immediately?"** Codex nói "Not from this
   correction packet alone". Tôi đồng ý — phải là GC-018 riêng.

5. **"Does this change CVF governance?"** Codex nói "Not yet". Tôi đồng ý.

### Điểm Codex chưa challenge

- **Inventory accuracy chính nó.** Codex assume inventory đúng. Spot-check
  của tôi cho thấy 3 items overstated. Phải fix trước khi dùng inventory
  làm roadmap input.

- **Brief Normalization và W7 signals omitted.** Codex không nhắc đến.

- **Reporting rule enforcement surface.** Codex chỉ nói "rule cần narrow",
  không nói rule cần enforce ở đâu.

## Required Changes

Trước khi inventory được dùng làm roadmap input, cần:

**RC-1: Sửa inventory accuracy.**

- Remove GAP-AGENT hoặc rewrite thành "Agent contract integration audit"
  (kiểm tra xem các agent contracts hiện có đã tích hợp đúng chưa).
- Rewrite GAP-MEM: scope xuống 3-4 sub-contracts cụ thể (privacy filter,
  capture adapter, retention policy), không phải 9.
- Rewrite GAP-SKILL: "executable component expansion" thay vì "stubs chưa
  implement". Downgrade priority.

**RC-2: Thêm 2 items.**

- Add `ADD-BRIEF` (Brief Normalization Doctrine).
- Add `ADD-W7-SIGNALS` (3 W7 signal candidates) — có thể absorb riêng vào
  evidence schema.

**RC-3: Narrow reporting rule.**

- Trigger conditions phải explicit trong proposed rule text.
- Add enforcement surface: line item trong release-gate checklist hoặc
  tranche closure template.

**RC-4: Update OBS-1 priority.**

- Upgrade từ 4 sao lên 5 sao.
- Confirm OBS-1 là first implementation candidate sau ADD-A/D promotion.

## Recommended First Roadmap

**Chọn:** doc-only ADD-A + ADD-D promotion packet.

Lý do:

1. R0 — không có runtime risk.
2. Synthesis Phase A đã rõ ràng đề xuất đây là "first and only public
   promotion candidate" từ 2026-05-07.
3. Cần ADD-A (Governed Capability Intake Doctrine) làm framework để đánh
   giá các absorption tiếp theo, bao gồm cả OBS-1.
4. Có thể hoàn thành nhanh vì synthesis đã đủ.

**Roadmap thứ hai (sau khi ADD-A/D đã promote):** Observability Plane
Foundation GC-018.

**Không khuyến nghị làm song song:** roadmap ADD-A/D phải close trước khi
mở OBS-1, vì OBS-1 implementation cần ADD-A doctrine làm framework để định
nghĩa Observability Plane là một governed capability mới.

**Không khuyến nghị làm:** Memory/Skill/Agent gap roadmaps cho đến khi
inventory accuracy được fix (RC-1).

## Risk

R0 cho review này: documentation only.

Residual risks:

- Nếu inventory không được fix (RC-1, RC-2), roadmap selection sẽ dựa trên
  thông tin sai và có thể mở roadmap cho gap không tồn tại (GAP-AGENT).
- Nếu reporting rule không có enforcement surface, rule sẽ bị quên giống
  như inventory đã bị quên.
- Nếu ADD-A/D không promote trước OBS-1, OBS-1 sẽ thiếu doctrine framework
  để định nghĩa scope.

## Decision

**Status: APPROVE_WITH_CHANGES**

Approve:

- inventory existence và overall structure;
- corrective roadmap + rebuttal + Claude review gate process;
- separate-roadmap principle;
- claim boundary discipline;
- recommendation rằng ADD-A/D là first promotion candidate;
- recommendation rằng OBS-1 là first implementation candidate;
- deferred status cho B/C1/C2/E1.

Required before next absorption roadmap opens:

- RC-1 (fix accuracy: GAP-AGENT, GAP-MEM, GAP-SKILL);
- RC-2 (add Brief Normalization và W7 signals);
- RC-3 (narrow reporting rule + add enforcement surface);
- RC-4 (upgrade OBS-1 priority).

Operator decision needed:

1. Accept Required Changes (RC-1 → RC-4) và mở doc-only ADD-A/D promotion
   packet?
2. Hay yêu cầu thêm audit trước khi accept Required Changes?

Trả lời câu hỏi 4 của Codex packet (Absorption Gate): **doc-only ADD-A +
ADD-D promotion packet** là first authorized roadmap, sau khi inventory
được fix theo RC-1/RC-2.

## Claim Boundary

Review này:

- **không** authorize implementation runtime nào;
- **không** authorize public claim change nào;
- **không** authorize doctrine promotion (chỉ recommend ADD-A/D là next
  candidate);
- **không** require live provider proof (vì không có runtime claim);
- **pending operator decision** cho: accept Required Changes, mở ADD-A/D
  promotion packet, accept reporting rule với narrow scope.

Review này authorize:

- update inventory theo RC-1, RC-2 (chỉ accuracy fix, không phải absorption);
- update roadmap theo RC-3 (narrow rule + enforcement surface);
- update inventory theo RC-4 (priority adjustment).

Review không thay đổi:

- GA posture (`GA_LOCAL_FIRST_APPROVED`);
- 10 lanes đã `runtime-owned`;
- public README hay CHANGELOG;
- release gate.

## Related Artifacts

- `docs/reviews/archive/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_CLAUDE_REVIEW_PACKET_2026-05-17.md`
- `docs/reviews/CVF_OPERATOR_PROGRESS_AND_UNABSORBED_KNOWLEDGE_REPORT_2026-05-17.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_REPORTING_CORRECTION_REBUTTAL_2026-05-17.md`
- `docs/roadmaps/CVF_UNABSORBED_KNOWLEDGE_REPORTING_CORRECTION_ROADMAP_2026-05-17.md`
- `docs/baselines/archive/CVF_16_5_LIVING_INTEGRATION_CLASSIFICATION_SUMMARY_2026-05-16.md`
- `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_PHASE_A_GOVERNED_CAPABILITY_AND_BOUNDARY_GOVERNANCE_SYNTHESIS_2026-05-07.md`
