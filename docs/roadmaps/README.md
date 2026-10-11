# CVF Roadmap Management Index

Memory class: POINTER_RECORD
docType: reference
INDEX type: IDX-2 PLANE_OWNER_MAP
Source authority: AGENTS.md; docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md; governed decision sources linked in each row.
Status: ACTIVE_REFERENCE
Date: 2026-10-12
Human-reviewable: YES
Claim boundary: Navigation and dated Local decision projection; source artifacts and current session authority control execution.
Public Export Disposition: DEFERRED_PRIVATE_ONLY

Text Encoding Exception: Vietnamese operator-facing navigation and instructions, UTF-8 text only.

## Purpose

Một cửa vào để biết **đang ưu tiên gì, còn dang dở gì, vì sao dừng và khi nào
được xem xét lại**. Local đối chiếu bảng điều hành ngày 2026-10-12;
[danh mục tra cứu](CVF_ROADMAP_INVENTORY.md) giữ các đường dẫn còn lại nhìn thấy được.
Đọc bảng trước, chỉ mở nguồn của luồng liên quan; không đọc lại toàn corpus.

## Scope / Source Authority

Operator ngày 2026-10-12 yêu cầu index quản lý roadmap để tránh lộn xộn và dễ
quên. Local orchestrator thực hiện documentation/index trong phạm vi này.
Thư mục chứa kế hoạch, phase, dependency, gate và exit criteria. Assessment,
review và permanent reference giữ owner riêng; [archive](archive/) là lịch sử.

Khi mâu thuẫn, theo hierarchy trong [AGENTS.md](../../AGENTS.md), đối chiếu
quyết định/closure mới nhất của **đúng scope** và [bootstrap hiện hành](../../CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json).
Header Status cũ hoặc child closure không đủ để kết luận cả chương trình đã
đóng hay được dispatch. Index dẫn về nguồn quyết định, không thay thế nó.

| Nhãn quản lý | Cách dùng |
|---|---|
| ACTIVE_DELIVERY | Ưu tiên đầu ra hiện tại; từng bước vẫn theo authority hiện hành |
| SUPPORTING | Phục vụ công việc thực đã chọn; không mở chương trình phụ |
| PARKED | Còn follow-up, chưa mở; điều kiện nằm ở nguồn |
| STOPPED | Có quyết định dừng; xem xét lại khi blocker hoặc giá trị thay đổi |
| CLOSED_BOUNDED | Phạm vi đã nghiệm thu; không đồng nghĩa toàn hệ thống/production ready |
| DEFERRED_NOT_RECONCILED | Có trong danh mục, chưa đối chiếu semantic trạng thái hiện hành; không suy ra active |

## Current Delivery And Supporting Work

| Luồng / roadmap | Nhãn quản lý | Đầu ra / nguồn quyết định / bước tiếp theo |
|---|---|---|
| [NCR - noncoder controlled runtime](CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md#current-delivery-checkpoint---2026-10-12) | ACTIVE_DELIVERY | Một local job: ý tưởng xác nhận -> run-bound result -> preview/revision/export -> cancel/error/recovery hiểu được. [Gói History recovery đã chọn](../work_orders/CVF_AGENT_WORK_ORDER_NCR_HISTORY_RECOVERY_2026-10-12.md): click History → đúng saved result → review/export/follow-up; actual Home/History có 1 control PASS và 2 assertion FAIL. Worker chạy sau committed release; chọn Sonnet 5.5 high, chưa tự khởi động. Integrated offline journey/full provider R3 chưa nghiệm thu; P11 parked. |
| [Model selection](CVF_ORCHESTRATOR_MODEL_SELECTION_SYSTEM_CHAIN_ROADMAP_2026-10-10.md#current-delivery-priority---2026-10-12) | SUPPORTING | Chất lượng, severity, self-repair, Local repair, procedure và thời gian trên việc thực. [Evidence owner](../reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json): 17 task observations ở checkpoint này, gồm Haiku/Sonnet/Luna. Ghi sau Local review; cost deferred, không mở benchmark hoặc xếp hạng từ index. |
| [MFRP - machine-first review preflight](CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md) | SUPPORTING | P4-C1 activated theo [AGENTS.md](../../AGENTS.md), review M5/M10/safety/M20. [Collection design closure](../reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_COMPLETION_2026-10-11.md): structural change deferred. [P5 amendment](../baselines/CVF_MFRP_P4_SAMPLE_GATED_P5_REOPEN_AMENDMENT_2026-09-02.md): 20 eligible natural returns cần nhưng chưa đủ; P5/P6 chưa released. Model task observations không phải eligible MFRP samples. |

## Unfinished Foundation And Conditional Reopen

| Luồng / roadmap | Nhãn quản lý | Phần còn giữ / điều kiện mở lại / nguồn trạng thái |
|---|---|---|
| [CSCC - canonical system chain](CVF_CANONICAL_SYSTEM_CHAIN_COMPOSITION_ROADMAP_2026-09-02.md) | STOPPED | [T2A closure](../../CVF_SESSION/state/entries/csccR1T2ASafeCanonicalCutoverStop20260903.json): STOP_NO_SAFE_CANONICAL_CUTOVER; T2B/T3 chưa mở. Cần source-verified route-build exclusion/packaging cho direct/canonical builds. Header ACTIVE_PLANNING là cũ. |
| [FLAL - learning admission / loopback](CVF_FOUNDATION_LEARNING_ADMISSION_AND_LOOPBACK_ROADMAP_2026-10-04.md) | PARKED | [T3 completion](../reviews/CVF_FLAL_T3_OFFLINE_COMPOSITION_COMPLETION_2026-10-04.md) accepted bounded; T4/T5 production admission/project loopback parked. Cần use case, authority và incremental value cụ thể; learning intake không tự thành production admission. |
| [FPC/FMS - foundation maintenance](CVF_FPC_FMS_T2_CURRENT_REGISTRY_EVIDENCE_RECONCILIATION_AND_NEXT_CANDIDATE_SELECTION_ROADMAP_2026-06-28.md) | STOPPED | Roadmap Decision: HOLD_FOUNDATION_MAINTENANCE_NO_CURRENT_SOURCE_BACKED_GAP, không có implementation candidate được chọn. Chỉ quay lại với gap source-backed hoặc explicit FPC-T4 strategic decision; không mở lại C01-C05 từ header READY. |
| [MFE - future memory enrichment](CVF_MFE_T0_MEMORY_FOUNDATION_FUTURE_ENRICHMENT_ROADMAP_2026-07-02.md) | STOPPED | [R1 closure](../../CVF_SESSION/state/entries/mfeR1MemoryFoundationFutureEnrichmentSourceVerificationClosure20260702.json): closed bounded, NO_NEW_VALUE. Cần nguồn cụ thể đã chọn và giá trị mới so với owner; header READY_FOR_MFE_R1 là cũ. |
| [MAO - lifecycle adapter uplift](CVF_MAO_PROVIDER_NEUTRAL_AGENT_HOST_LIFECYCLE_ADAPTER_FOUNDATION_UPLIFT_ROADMAP_2026-08-09.md) | STOPPED | Current roadmap: CLOSED_T0_CANCEL_UPLIFT_NO_FACADE_VALUE. Cần demand và material value thay đổi trước khi xem xét lại; không tự tạo facade. |
| Model selection runtime / S5 / scoring / PLL / Gateway | PARKED | [Current Delivery Priority](CVF_ORCHESTRATOR_MODEL_SELECTION_SYSTEM_CHAIN_ROADMAP_2026-10-10.md#current-delivery-priority---2026-10-12) và bootstrap: manual/offline companions có bounded acceptance; full runtime chain chưa mở. Chỉ xem xét khi có nhu cầu từ đầu ra thực. |
| ACEL G1-G7 / source R2 / media / Expense / public / deploy | STOPPED / PARKED theo từng nguồn | [Active handoff](../../AGENT_HANDOFF_V63_2026-09-18.md) và bootstrap: G1 stopped, G2-G6 parked, G7 research closed; checkpoint khác giữ riêng. Fresh demand/authority phải đúng lane, không có automatic successor. |

## Inventory And Maintenance

[CVF_ROADMAP_INVENTORY.md](CVF_ROADMAP_INVENTORY.md) và [CSV tra cứu](CVF_ROADMAP_INVENTORY.csv) được sinh từ path, header và content hash, có
processing ledger/reconciliation. Luồng ngoài bảng vẫn nhìn thấy trong danh
mục, với semantic disposition DEFERRED_NOT_RECONCILED. Khi chọn một luồng đó,
Local đối chiếu closure/continuity đúng scope rồi thêm row và trigger cụ thể.

**Owner: Local orchestrator / roadmap maintainer.** Trong selection, dispatch
hoặc closure hiện có, cập nhật row liên quan khi priority, accepted scope,
blocker, next useful action hoặc reopen condition đổi. Ghi ngày đối chiếu và
nguồn quyết định, trong scope tài liệu được phép. Khi tạo/đổi/di chuyển roadmap:

```powershell
python scripts/generate_roadmap_inventory.py
python scripts/generate_roadmap_inventory.py --check
```

`--check` so với nguồn hiện có, exit 1 khi stale, không ghi file. Đây là lệnh
opt-in cho maintainer; không thêm hook, gate worker hay yêu cầu đọc toàn corpus.
Generator không tự chọn việc, đổi status nguồn hoặc mở lane. Không mở tranche
chỉ để làm đẹp index; ưu tiên đầu ra hữu ích hữu hạn.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | governance/compat/check_index_classification.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_corpus_completeness_report_integrity.py; governance/compat/check_corpus_to_knowledge_map_reconciliation.py; governance/compat/check_active_session_state.py; governance/compat/check_machine_closure_package.py; governance/compat/check_closure_packaging_preflight.py; governance/compat/check_docs_governance_compat.py; governance/compat/check_public_export_disposition.py |
| literalTokensReviewed | INDEX type, Source authority, Status, Date, Human-reviewable, Claim boundary, Public Export Disposition; reference Purpose/Scope/Claim Boundary; Text Encoding Exception; Corpus verdict/Knowledge-map verdict; READ/SKIPPED_WITH_REASON/DEFERRED/BLOCKED_UNREADABLE; GC-020 HEAD/parent-only-sync rule |
| gateRunPurpose | Confirmation of corrected final packet; first commit attempt exposed missed naming/conditional literals, failure log retained. Checker sources re-read before revision. |
| claimBoundary | Static navigation and selected dated reconciliation; PASS cannot prove semantic reading or whole foundation/runtime acceptance. |

## Claim Boundary

Roadmap/baseline/work order/closure và current authority quyết định việc được
làm. Bảng là dated projection của selected sources; metadata inventory không
phải audit semantic toàn bộ roadmap. Không có runtime, provider/live,
production, public export, automatic dispatch hoặc model ranking claim.

## Bounded Foundation Closures

| Roadmap / family | Nhãn quản lý | Nguồn đóng / giới hạn |
|---|---|---|
| [LHW22/LHW23/LHW24 - agent intelligence](CVF_LHW22_LHW23_LHW24_AGENT_INTELLIGENCE_ROADMAP_2026-05-31.md) | CLOSED_BOUNDED | Roadmap CLOSED_PASS_BOUNDED; LHW24 là latest closed wave trong continuity. |
| [MKG7 - memory plane](CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md) | CLOSED_BOUNDED | Roadmap CLOSED_PASS_BOUNDED; không tự mở runtime follow-up. |
| [Pre-runtime cleanup / pilot](CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md) | CLOSED_BOUNDED | ROADMAP_CLOSED_PASS_BOUNDED_RUNTIME_PARKED. |
| [GFC - governance foundation](CVF_GOVERNANCE_FOUNDATION_CONSOLIDATION_ROADMAP_2026-06-18.md) | CLOSED_BOUNDED | GFC_T1_T5_CLOSED_PASS_BOUNDED_RUNTIME_PARKED. |
| [FPC - planes / workflow chain](CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md) | CLOSED_BOUNDED cho accepted chain | [FPC-SCG T7 acceptance ledger](../reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json): closure chain/downstream reopen gates; header cũ không bao phủ toàn chain. FPC-T4 strategic decision vẫn riêng. |
| [ACEL applied owner enrichment](CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md) | CLOSED_BOUNDED | Roadmap CLOSED_PASS_BOUNDED, handoff xác nhận; không tự mở post-AKOE successor. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Private navigation/index; không có public-sync hoặc push grant từ yêu cầu này.
