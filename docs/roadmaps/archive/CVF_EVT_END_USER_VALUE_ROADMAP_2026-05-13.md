# CVF End-User Value Track (EVT) Roadmap — 2026-05-13

**Status:** EVT ROADMAP COMPLETE; EVT-4 RESULT NEGATIVE FOR QUALITY-DELTA RULE
**Author:** Claude (provenance workspace)
**Audience:** Codex (peer reviewer) + user (decision)
**Scope:** 4 tracks to convert CVF's operator-infrastructure gains into measurable end-user value
**Document class:** ROADMAP
**Parent context:** EA Enhancement Tracks A–E COMPLETE (public-sync commit `8aa7e97`)
**Codex review:** `docs/reviews/CVF_EVT_ROADMAP_CODEX_REVIEW_2026-05-14.md`

---

## 0. Bối cảnh và động lực

EA Tracks A–E (2026-05-13) đã hoàn thành toàn bộ observability và infrastructure
layer của CVF. Đánh giá sau EA:

> CVF đo được chính nó rất tốt, nhưng chưa chứng minh được nó cải thiện trải
> nghiệm người dùng cuối. EA work là operator/infrastructure value — gián tiếp
> với end user.

Gaps chưa có dữ liệu (as of 2026-05-13):

| Gap | Tác động với end user |
|---|---|
| False positive rate (BLOCK/CLARIFY oan) | User bị chặn workflow vô lý |
| Governance latency thực tế | User chờ lâu hơn bare API không có lý do |
| NEEDS_APPROVAL UX | User không biết phải làm gì tiếp theo |
| Output quality delta | Không biết CVF có làm giảm chất lượng output không |
| Task recovery / abandonment | Không biết user có tiếp tục sau BLOCK/CLARIFY/NEEDS_APPROVAL không |

EVT roadmap giải quyết trực tiếp 4 gaps này.

---

## 1. Tổng quan 4 Tracks

| Track | Tên | GC-018? | Effort | Priority |
|---|---|---|---|---|
| **EVT-1** | False Positive Audit | Không | Thấp (1–2 ngày) | Cao |
| **EVT-2** | Governance Latency Optimization | Có thể | Thấp–Trung (1–5 ngày) | Trung |
| **EVT-3** | NEEDS_APPROVAL UX Improvement | Không | Thấp–Trung (2–3 ngày) | Cao |
| **EVT-4** | Output Quality A/B Baseline | Có | Trung (3–5 ngày) | Thấp–Trung |
| **EVT-5** | Task Recovery / Abandonment | Không | Thấp | Cao |

**Thứ tự đề xuất:** EVT-1 + EVT-3 song song (không cần GC-018) → EVT-2 (sau khi có
live traffic data) → EVT-4 (cần GC-018 riêng).

### Implementation update — 2026-05-14

User approved Codex's 5/5 roadmap corrections and authorized implementation.
EVT-1 and EVT-3 are implemented with the corrected architecture:

- EVT-1: false-positive reports are append-only events linked by `receiptId`;
  `GovernanceEvidenceReceipt` remains immutable point-in-time evidence.
- EVT-1: report control lives in `ProcessingScreen` so BLOCK/CLARIFY users can
  actually see it; it is not placed in `ResultViewer`.
- EVT-1: reportable BLOCK/CLARIFY decisions are passively logged as denominator
  events; FP claims are separate numerator events.
- EVT-3: existing `ProcessingScreen` NEEDS_APPROVAL flow was hardened; no
  greenfield rewrite.
- EVT-3: approval hints are deterministic static templates. If a trigger has no
  safe static hint, no hint is shown. There is no AI-generated hint fallback.

EVT-2 remains measure-first: do not optimize route ordering before real phase
data. EVT-4 remains gated on GC-018 and a preregistered A/B protocol.

### Completion update — 2026-05-14

Remaining EVT tracks were completed in order:

- EVT-2.1 live measurement: 20/20 live `/api/execute` requests on Alibaba lane.
  Median governance tax = `1.57%`, fitness = `GREEN`, low-N caveat = `false`.
  Per roadmap, EVT-2.2 optimization was not executed because no AMBER/RED
  bottleneck was measured.
- EVT-5 added: browser-local analytics now records `task_recovery_prompted` and
  `task_recovery_started`; noncoder metrics/report/readout now include task
  recovery rate and governance-abandonment rate.
- EVT-4 completed under fresh GC-018 and preregistration:
  `docs/reviews/CVF_GC018_EVT4_OUTPUT_QUALITY_AB_BASELINE_2026-05-14.md` and
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PREREGISTRATION_2026-05-14.md`.
  Live run completed 20/20 pairs with OpenAI `gpt-4o` reviewer. Median normalized
  delta `CFG-B - CFG-A = -0.28`; decision rule not met. Bounded conclusion:
  current governed documentation-template path reduced output quality on this
  corpus, while preserving live receipts and safety.

---

## 2. Track EVT-1 — False Positive Audit

### Vấn đề

Không có số liệu về tỷ lệ người dùng bị BLOCK/CLARIFY oan. Đây là điểm đau số 1
của mọi governance framework — nếu nó chặn quá nhiều, người dùng bỏ đi. CVF hiện
tại không thể trả lời câu hỏi: "Bao nhiêu % BLOCK của tôi là đúng?"

### Scope kỹ thuật

**Codex correction applied 2026-05-14:** The original "add
`falsePositiveReported` to receipt" proposal is superseded. Receipt mutation is
architecturally wrong because the receipt is point-in-time execution evidence.
False-positive reports are separate append-only events linked by `receiptId`.

- Thêm button "Report as false positive" trong `ProcessingScreen` khi response trả về BLOCK hoặc CLARIFY
  (không hiện với ALLOW hay NEEDS_APPROVAL)
- Log reportable decision observed + false positive report vào JSONL
- Script `scripts/analyze_false_positive_rate.py` đọc log: tỷ lệ FP / tổng BLOCK+CLARIFY

### Files cần thay đổi / tạo mới

- Sửa: `src/app/api/execute/route.ts` — passive denominator logging only
- Sửa: `src/components/ProcessingScreen.tsx` — BLOCK/CLARIFY report control
- Mới: `src/lib/false-positive-report.ts`
- Mới: `src/app/api/governance/false-positive-report/route.ts`
- Mới: `scripts/analyze_false_positive_rate.py`
- Không đụng enforcement.ts, hard gates, hay bất kỳ governance decision logic nào

### Boundary

- KHÔNG thay đổi enforcement logic
- Report là log thụ động — không trigger auto-unblock hay bypass
- Button chỉ hiện sau BLOCK/CLARIFY, không phải ALLOW

### Exit criteria

- [x] Button render đúng sau BLOCK/CLARIFY response
- [x] Report được log vào JSONL
- [x] Script analyze chạy và in tỷ lệ FP/total
- [x] Targeted `npm run test:run` PASS; `npm run lint` PASS; `npx tsc --noEmit` PASS

### Câu hỏi cho Codex

"Report false positive" có nên trigger một async review process (notification đến
Admin) không, hay chỉ log thụ động đủ rồi cho giai đoạn này?

---

## 3. Track EVT-2 — Governance Latency Optimization

### Vấn đề

Track A đã có baseline đo được governance tax. Nhưng baseline đó được đo với mock
requests trong test. Chưa có dữ liệu thật từ live traffic. Chưa biết phase nào là
bottleneck. Chưa optimize gì.

### Điều kiện tiên quyết

- Track A COMPLETE (đã có — commit `158309f`)
- Cần N ≥ 20 live requests qua `/api/execute` để có dữ liệu thực tế
- Chạy `python scripts/analyze_governance_tax.py` trên log thật

### Scope kỹ thuật (2 phase)

**Phase EVT-2.1 — Measure (không cần GC-018):**
- Chạy N live requests, collect JSONL
- Analyze: phase nào AMBER/RED?
- Candidate bottleneck rõ nhất: intent classification (chạy sync?) và DLP scan (có
  thể parallelize không?)

**Phase EVT-2.2 — Optimize (cần GC-018 nếu thay đổi execution order):**
- Nếu GREEN ngay: document và đóng (không làm gì thêm)
- Nếu AMBER/RED: implement targeted optimization cho phase bottleneck
- Ví dụ: parallelize DLP + intent classification nếu không vi phạm audit trail order

### EVT-2 completion — 2026-05-14

- [x] `scripts/run_evt2_live_latency_measurement.js` added.
- [x] `scripts/analyze_governance_tax.py` added.
- [x] 20 live requests collected:
  `docs/assessments/CVF_EVT2_LIVE_LATENCY_MEASUREMENT_2026-05-14.jsonl`.
- [x] Analysis summary:
  `docs/assessments/CVF_EVT2_LIVE_LATENCY_MEASUREMENT_2026-05-14.md`.
- [x] Fitness = GREEN (`1.57%` median governance tax). No optimization made.

### Câu hỏi cho Codex

Parallelize DLP + intent classification có vi phạm governance contract không?
Thứ tự xử lý (DLP trước hay intent trước) có ý nghĩa gì với audit trail integrity?
Nếu DLP miss PII nhưng intent đã classify xong — có race condition governance nào không?

---

## 4. Track EVT-3 — NEEDS_APPROVAL UX Improvement

### Vấn đề

Khi enforcement trả về `NEEDS_APPROVAL`, end user hiện tại thấy gì? Flow audit
trong `route.ts` cho thấy có approval record, expiry, status check — nhưng không
rõ UI communicate điều này như thế nào với noncoder.

Nếu user nhận được "pending" và không biết: chờ bao lâu? Ai approve? Có thể làm
gì khác không? — đây là dead-end UX tệ nhất.

### Scope kỹ thuật

- Audit NEEDS_APPROVAL user journey end-to-end. Codex verified this already
  lives in `ProcessingScreen`; harden the existing journey, do not rewrite it.
- Thêm vào response khi NEEDS_APPROVAL:
  - Estimated context: "Yêu cầu đã được gửi đến Admin để xem xét"
  - Deterministic safe hint: gợi ý ngắn từ static template map nếu trigger có
    safe template đã audit
- Không thay đổi approval logic, không thay đổi ai là approver, không thay đổi threshold

### Boundary (quan trọng)

- Rewrite hint là suggestion ngắn dựa trên lý do approval được trigger
- KHÔNG phải hướng dẫn bypass governance
- KHÔNG expose nội dung các R2/R3 patterns
- Nếu không thể viết hint an toàn → bỏ hint, chỉ thêm context message
- Không dùng AI-generated/runtime rewrite hint fallback

### Exit criteria

- [x] NEEDS_APPROVAL screen có context message rõ
- [x] User biết next step
- [x] No exposure of hard gate internals
- [x] Test coverage cho NEEDS_APPROVAL render
- [x] Static hint only; no AI-generated fallback

### Câu hỏi cho Codex

"Rewrite suggestion" có nguy cơ dạy user cách bypass governance không? Ranh giới
giữa "helpful communication" và "governance evasion guide" ở đâu? Nếu rủi ro
cao, có nên bỏ hoàn toàn suggestion và chỉ cải thiện context message không?

---

## 4.5. Track EVT-5 — Task Recovery / Abandonment

### Vấn đề

False positive rate đo CVF có quyết định sai không. Task recovery đo câu hỏi
business-value quan trọng hơn: sau khi CVF chặn/làm rõ/yêu cầu phê duyệt, user
có tiếp tục workflow hay bỏ cuộc?

### Scope kỹ thuật

- Thêm analytics event `task_recovery_prompted` khi user gặp
  BLOCK/CLARIFY/NEEDS_APPROVAL có receipt.
- Thêm analytics event `task_recovery_started` khi user thực hiện bước phục hồi
  như false-positive report hoặc approval request.
- Mở rộng noncoder metrics với:
  - `taskRecoveryRate`
  - `governanceAbandonmentRate`
- Mở rộng rollout readout với lane `task_recovery`.

### Exit criteria

- [x] Recovery prompt/action events wired in `ProcessingScreen`.
- [x] Metric computation and report include recovery/abandonment.
- [x] Noncoder health readout includes Task Recovery lane.
- [x] Unit coverage added.

---

## 5. Track EVT-4 — Output Quality A/B Baseline

### Vấn đề

CVF tuyên bố governance-first nhưng không có dữ liệu nào chứng minh output của
CVF không kém hơn bare API call. Đây là câu hỏi business value quan trọng nhất:
**CVF có cost gì về output quality?**

**Lưu ý:** Track này KHÔNG phải QBS rerun. QBS đo governance control quality (hard
gates, BLOCK/ALLOW decisions). EVT-4 đo output quality (nội dung câu trả lời có
tốt không so với không governance). Hai câu hỏi khác nhau.

### Điều kiện tiên quyết — PHẢI HOÀN TẤT TRƯỚC KHI BẮT ĐẦU

- [x] GC-018 candidate phải được tạo và approved
- [x] User approve: tập 20 prompts nào được dùng cho A/B (cần curate)
- [x] Không được reopen QBS infrastructure — dùng reviewer mới nếu cần

### Scope kỹ thuật

**Config A (ungoverned):** Bare Alibaba/DashScope `qwen-turbo` call, không qua CVF
**Config B (governed):** Cùng prompt qua CVF `/api/execute`, R1, preference=auto

20 prompts × 2 configs = 40 executions. Reviewer: model-assisted (OpenAI gpt-4o
hoặc DeepSeek deepseek-reasoner — không dùng gpt-4o-mini/deepseek-chat đã fail
kappa gate).

**Metric:** quality delta CFG-B vs CFG-A.
**Hypothesis:** CVF governance không làm giảm output quality với R0/R1 prompts.

### Exit criteria

- [x] GC-018 approved
- [x] 20 prompts curated và user-approved
- [x] 40 executions completed
- [x] Reviewer score documented
- [x] Claim statement: "CVF governance overhead [does/does not] reduce output quality
  for R0/R1 requests — delta = X, confidence interval = Y"

### EVT-4 completion — 2026-05-14

- GC-018: `docs/reviews/CVF_GC018_EVT4_OUTPUT_QUALITY_AB_BASELINE_2026-05-14.md`
- Preregistration:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PREREGISTRATION_2026-05-14.md`
- Runner: `scripts/run_evt4_output_quality_ab.js`
- Evidence:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_EVIDENCE_2026-05-14.json`
- Summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SUMMARY_2026-05-14.md`

Result: 20/20 CFG-A direct Alibaba and CFG-B CVF-governed pairs completed.
CFG-B produced 20/20 live receipts and 0 safety failures. OpenAI `gpt-4o`
reviewer scored median normalized delta `CFG-B - CFG-A = -0.28`; preregistered
decision rule was not met. Bounded claim: for this R0/R1 corpus and current
documentation-template governed path, CVF governance preserved audit/safety but
materially reduced output usefulness/completeness/specificity versus direct
Alibaba. This should trigger a follow-up template/prompt-quality remediation
track, not a QBS rerun.

### Câu hỏi cho Codex

1. Nếu CFG-B < CFG-A (governed output kém hơn) ở một số task family, CVF có vấn
   đề kiến trúc không, hay chỉ là system prompt/template engineering cần fix?
   Ranh giới quyết định ở đâu — delta bao nhiêu là "acceptable cost of governance"?

2. 20 prompts có đủ không? Hay cần tối thiểu N khác?

3. Dùng gpt-4o làm reviewer đơn lẻ (không paired) có chấp nhận được không, hay
   cần 2 reviewer để tránh bias?

---

## 6. Sequencing & Dependency Map

```
Ngay bây giờ (parallel, không cần GC-018):
┌──────────────────────────────────────┐
│  EVT-1: False Positive Audit         │  1–2 ngày
│  EVT-3: NEEDS_APPROVAL UX            │  2–3 ngày
└──────────────────────────────────────┘
         ↓ (có live traffic data từ EVT-1)
┌──────────────────────────────────────┐
│  EVT-2: Latency Optimization         │  1–5 ngày (tùy baseline)
└──────────────────────────────────────┘
         ↓ (cần GC-018 riêng + user approve prompt set)
┌──────────────────────────────────────┐
│  EVT-4: Output Quality A/B           │  3–5 ngày
└──────────────────────────────────────┘
```

---

## 7. Không thuộc scope roadmap này

- QBS rerun (suspended — conditions chưa met: reviewer model upgrade + calibration pass)
- AI-assisted DLP (model-based redaction) — separate GC-018, separate roadmap
- Multi-tenant / cloud deployment — deferred per GA_LOCAL_FIRST_APPROVED boundary
- Track D Phase 2 (review-chain topology) — reopen trigger: D.1 stable ≥ 1 week + GC-018
- Bất kỳ thay đổi nào với hard gate logic, BLOCK/CLARIFY/NEEDS_APPROVAL thresholds,
  hay guard contract

---

## 8. Risk Registry

| Risk | Track | Mức | Mitigation |
|---|---|---|---|
| "Report FP" button dạy user cách kháng governance | EVT-1 | Thấp | Log thụ động, không trigger bypass |
| Parallelize DLP+intent tạo race condition | EVT-2 | Trung | Codex review trước khi implement |
| Rewrite hint trở thành bypass guide | EVT-3 | Trung-Cao | Giới hạn hint đến context message nếu rủi ro cao |
| EVT-4 kết quả CFG-B < CFG-A → architectural crisis | EVT-4 | Trung | Pre-define acceptable delta threshold trước khi chạy |
| Scope creep EVT-3 thành full AI feature | EVT-3 | Trung | Giới hạn cứng: không AI call trong rewrite suggestion |

---

## 9. Câu hỏi tổng quan cho Codex

1. **Priority:** Trong 4 tracks, track nào quan trọng nhất với một team 5–10 người
   deploy CVF? False positive rate (EVT-1) hay output quality (EVT-4)?

2. **Missing track:** Có end-user value gap nào quan trọng hơn 4 tracks trên mà
   roadmap này bỏ qua không?

3. **EVT-4 architecture risk:** Nếu A/B cho thấy governed output kém hơn ở một
   số task family — CVF nên làm gì? Accept + document, hay trigger redesign cycle?

4. **EVT-2 parallelize risk:** Thứ tự xử lý DLP → intent → risk → provider có
   phải là hard architectural requirement của CVF doctrine không?

---

*Roadmap này sẵn sàng để Codex review. Không implement bất kỳ track nào trước
khi có phản hồi từ Codex và user approve.*
