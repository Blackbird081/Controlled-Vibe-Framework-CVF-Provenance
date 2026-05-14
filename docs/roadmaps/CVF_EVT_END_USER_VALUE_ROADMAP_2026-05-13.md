# CVF End-User Value Track (EVT) Roadmap — 2026-05-13

**Status:** DRAFT — CODEX REVIEW RECORDED; PENDING USER APPROVAL BEFORE EXECUTION
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

EVT roadmap giải quyết trực tiếp 4 gaps này.

---

## 1. Tổng quan 4 Tracks

| Track | Tên | GC-018? | Effort | Priority |
|---|---|---|---|---|
| **EVT-1** | False Positive Audit | Không | Thấp (1–2 ngày) | Cao |
| **EVT-2** | Governance Latency Optimization | Có thể | Thấp–Trung (1–5 ngày) | Trung |
| **EVT-3** | NEEDS_APPROVAL UX Improvement | Không | Thấp–Trung (2–3 ngày) | Cao |
| **EVT-4** | Output Quality A/B Baseline | Có | Trung (3–5 ngày) | Thấp–Trung |

**Thứ tự đề xuất:** EVT-1 + EVT-3 song song (không cần GC-018) → EVT-2 (sau khi có
live traffic data) → EVT-4 (cần GC-018 riêng).

---

## 2. Track EVT-1 — False Positive Audit

### Vấn đề

Không có số liệu về tỷ lệ người dùng bị BLOCK/CLARIFY oan. Đây là điểm đau số 1
của mọi governance framework — nếu nó chặn quá nhiều, người dùng bỏ đi. CVF hiện
tại không thể trả lời câu hỏi: "Bao nhiêu % BLOCK của tôi là đúng?"

### Scope kỹ thuật

- Thêm field `falsePositiveReported: boolean` vào governance receipt (GovernanceEvidenceReceipt)
- Thêm button "Report as false positive" trong UI khi response trả về BLOCK hoặc CLARIFY
  (không hiện với ALLOW hay NEEDS_APPROVAL)
- Log false positive report vào JSONL (dùng governance-tax-logger pattern)
- Script `scripts/analyze_false_positive_rate.py` đọc log: tỷ lệ FP / tổng BLOCK+CLARIFY

### Files cần thay đổi / tạo mới

- Sửa: `src/app/api/execute/route.ts` — thêm field vào receipt
- Mới: component button (nhỏ, inline với result display)
- Mới: `scripts/analyze_false_positive_rate.py`
- Không đụng enforcement.ts, hard gates, hay bất kỳ governance decision logic nào

### Boundary

- KHÔNG thay đổi enforcement logic
- Report là log thụ động — không trigger auto-unblock hay bypass
- Button chỉ hiện sau BLOCK/CLARIFY, không phải ALLOW

### Exit criteria

- [ ] Button render đúng sau BLOCK/CLARIFY response
- [ ] Report được log vào JSONL
- [ ] Script analyze chạy và in tỷ lệ FP/total
- [ ] `npm run test:run` PASS, lint PASS, tsc PASS

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

- Audit NEEDS_APPROVAL user journey end-to-end (không code trước, audit trước)
- Thêm vào response khi NEEDS_APPROVAL:
  - Estimated context: "Yêu cầu đã được gửi đến Admin để xem xét"
  - Rewrite hint: gợi ý ngắn cách đơn giản hóa request để tránh trigger approval
    (ví dụ: "Thử bỏ phần X để request được xử lý ngay")
- Không thay đổi approval logic, không thay đổi ai là approver, không thay đổi threshold

### Boundary (quan trọng)

- Rewrite hint là suggestion ngắn dựa trên lý do approval được trigger
- KHÔNG phải hướng dẫn bypass governance
- KHÔNG expose nội dung các R2/R3 patterns
- Nếu không thể viết hint an toàn → bỏ hint, chỉ thêm context message

### Câu hỏi cho Codex

"Rewrite suggestion" có nguy cơ dạy user cách bypass governance không? Ranh giới
giữa "helpful communication" và "governance evasion guide" ở đâu? Nếu rủi ro
cao, có nên bỏ hoàn toàn suggestion và chỉ cải thiện context message không?

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

- [ ] GC-018 candidate phải được tạo và approved
- [ ] User approve: tập 20 prompts nào được dùng cho A/B (cần curate)
- [ ] Không được reopen QBS infrastructure — dùng reviewer mới nếu cần

### Scope kỹ thuật

**Config A (ungoverned):** Bare Alibaba/DashScope `qwen-turbo` call, không qua CVF
**Config B (governed):** Cùng prompt qua CVF `/api/execute`, R1, preference=auto

20 prompts × 2 configs = 40 executions. Reviewer: model-assisted (OpenAI gpt-4o
hoặc DeepSeek deepseek-reasoner — không dùng gpt-4o-mini/deepseek-chat đã fail
kappa gate).

**Metric:** quality delta CFG-B vs CFG-A.
**Hypothesis:** CVF governance không làm giảm output quality với R0/R1 prompts.

### Exit criteria

- [ ] GC-018 approved
- [ ] 20 prompts curated và user-approved
- [ ] 40 executions completed
- [ ] Reviewer score documented
- [ ] Claim statement: "CVF governance overhead [does/does not] reduce output quality
  for R0/R1 requests — delta = X, confidence interval = Y"

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
