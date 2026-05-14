# CVF EA Enhancement Roadmap — 2026-05-12

**Status:** DRAFT — PENDING CODEX REVIEW BEFORE EXECUTION
**Author:** Claude (provenance workspace)
**Audience:** Codex (peer reviewer) + user (decision)
**Scope:** 5 EA enhancement tracks derived from governance-benchmark advisory review
**Document class:** ROADMAP — has phases, gates, dependencies, exit criteria
**Management model:** SEPARATE from QBS track (see §7 for rationale)

---

## 0. Câu hỏi quản lý: Tách riêng hay gộp chung với QBS?

### Quyết định đề xuất: TÁCH RIÊNG — 2 roadmap độc lập

**Lý do:**

| Tiêu chí | QBS track | EA Enhancement track |
|---|---|---|
| Mục tiêu | Chứng minh output quality không bị hạ bởi governance | Nâng cao khả năng đo lường và vận hành của framework |
| Blocker hiện tại | Reviewer agreement (kappa gate) | Không có blocker — greenfield |
| Dependency | Cần hoàn tất R10 để có L4/L5 claim | Độc lập với QBS score |
| Risk nếu gộp | EA work bị block nếu QBS tiếp tục fail | QBS bị phân tán focus |
| Audience | Developer / benchmark reviewer | Owner / Admin / noncoder |
| Execution order | QBS-33 → R10 (sequence cứng) | Track A-E có thể song song với QBS |

**Kết luận:** QBS roadmap tiếp tục theo sequence đã locked (QBS-33 → QBS-39 → checkpoint → R10). EA Enhancement roadmap chạy **song song** trên public-sync clone, không đụng đến QBS artifacts. Chúng hội tụ ở checkpoint R10 khi cả hai cần ra artifact công khai.

**Điều kiện để gộp lại sau này:** Nếu Track D (Multi-provider Policy Engine) cần QBS benchmark data để validate provider routing quality — thì tại thời điểm đó mới liên kết, không phải bây giờ.

---

## 1. Tổng quan 5 Tracks

| Track | Tên | Priority | Effort | GC-018 cần? |
|---|---|---|---|---|
| **A** | Governance Tax Measurement | Cao | Thấp-Trung | Không |
| **B** | QBS Benchmark Dashboard (Web) | Trung | Thấp | Không |
| **C** | Audit Receipt Integrity | Trung | Thấp | Không |
| **D** | Multi-provider / Multi-agent Policy Engine | Cao (dài hạn) | Cao | Có |
| **E** | DLP Quality Benchmark | Thấp-Trung (dài hạn) | Trung | Có |

**Execution order đề xuất:** A → B → C đồng thời (low-risk, greenfield), sau đó D, sau đó E.

---

## 2. Track A — Governance Tax Measurement

### Mục tiêu

Đo overhead latency mà CVF thêm vào trên mỗi request: `pre-processing + policy engine + post-processing`. Không đo provider latency. Thiết lập fitness function: **Governance Tax < 10% total request time**.

### Vấn đề EA cần giải quyết

CVF hiện có `claim-ladder` (L4/L5) cho output quality nhưng **không có SLA cho overhead của chính framework**. Đây là missing fitness function — CVF không thể tự chứng minh nó không làm bottleneck.

### Điều kiện tiên quyết

- [ ] `/api/execute` route phải đang hoạt động (đã có — QBS-38 confirmed)
- [ ] Có ít nhất 1 provider key (đã có)
- [ ] Không cần thay đổi governance contract hay hard gate logic

### Scope kỹ thuật

**Đo 3 phase trong pipeline `/api/execute`:**

```
Request nhận vào
  → [Phase 1] Pre-processing: DLP scan + intent classification
  → [Phase 2] Policy Engine: risk scoring + approval check + family mapping
  → [Phase 3] Provider call (excluded từ "tax")
  → [Phase 4] Post-processing: output validation + receipt generation
  → Response ra
```

**Output format (JSONL per request):**
```json
{
  "request_id": "...",
  "ts": "ISO8601",
  "phase_ms": {
    "pre_processing": 12,
    "policy_engine": 8,
    "provider": 450,
    "post_processing": 5
  },
  "governance_tax_ms": 25,
  "governance_tax_pct": 5.3,
  "decision": "ALLOW|BLOCK|CLARIFY|NEEDS_APPROVAL"
}
```

**Fitness function gate:**
- GREEN: tax_pct < 10%
- AMBER: 10–20%
- RED: > 20% — trigger optimization review

### Files cần thay đổi

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` — thêm timing instrumentation
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts` — wrap từng phase với `performance.now()`
- Mới: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governance-tax-logger.ts`
- Mới: `docs/benchmark/governance-tax/governance-tax-fitness-function.md`

### Boundary

- Không thay đổi governance decision logic
- Không expose raw timing ra public API response (chỉ log nội bộ)
- Không cần live provider call để validate — có thể test với mock AI mode

### Exit criteria

- [ ] JSONL log được emit cho mỗi request qua `/api/execute`
- [ ] Script `scripts/analyze_governance_tax.py` đọc JSONL và in fitness function status
- [ ] Test: timing wrapper không làm thay đổi governance decision
- [ ] `npm run build`: PASS
- [ ] `python scripts/check_public_surface.py`: PASS

### Estimated effort: 2–3 ngày

---

## 3. Track B — QBS Benchmark Dashboard (Web Tab)

### Mục tiêu

Thêm tab "📈 Benchmark" vào trang `/governance` (đã có tab pattern), hiển thị QBS run history, current status, và per-family quality delta. Phục vụ Owner/Admin nhìn thấy trust evidence của framework trực quan.

### Vấn đề EA cần giải quyết

CVF có 35+ QBS artifacts ở `docs/benchmark/qbs-1/` nhưng chỉ readable qua raw JSON/Markdown. Không có visual evidence layer cho non-developer. **Governance Transparency** là một Quality Attribute EA quan trọng — framework phải tự minh bạch về hiệu quả của nó.

### Điều kiện tiên quyết

- [ ] QBS artifacts đã có ở `docs/benchmark/qbs-1/` (đã có — R5-R9 complete)
- [ ] `/governance` page đã có tab pattern `GovTab` (đã confirmed trong source)
- [ ] Không cần live provider call — chỉ đọc static JSON files
- [ ] GC-023: kiểm tra line count `/governance/page.tsx` (hiện 185 lines — an toàn nếu tách component riêng)

### Scope kỹ thuật

**Tab mới: `benchmark` (thứ 6 trong GovTab)**

Component: `EXTENSIONS/.../cvf-web/src/components/QBSBenchmarkPanel.tsx`

**Section 1 — Run Summary Table:**
```
| Run | Status | Hard Gates | Reviewer kappa | CFG-B delta | Date |
| R5  | PASS   | ✅         | 0.714          | -0.25       | ...  |
| R6  | FAIL   | ✅         | 0.504          | -0.125      | ...  |
| R7  | FAIL   | ✅         | 0.464          | -0.125      | ...  |
| R8  | FAIL   | ✅         | 0.500          | -0.125      | ...  |
| R9  | FAIL   | ✅         | 0.372          | -0.125      | ...  |
```

**Section 2 — Per-family Quality Delta (Bar chart, R9 data):**
- Dùng SVG native hoặc CSS bar — không import Recharts/Chart.js (giữ bundle nhỏ)
- Màu: GREEN nếu delta ≥ 0, RED nếu delta < 0
- Families: 8 families từ QBS-25 post-score analysis

**Section 3 — Current Status Badge:**
- Đọc từ `docs/benchmark/qbs-1/qbs1-powered-single-provider-20260511-alibaba-r9/claim-statement.md`
- Hiển thị: `QBS39_FAMILY_CONDITIONAL_ALLOW_OUTPUT_CONTRACT_READY_NO_NEW_SCORE`

**Data source:** API route mới `/api/benchmark/qbs-summary` đọc từ static JSON files trong `docs/benchmark/qbs-1/`. Không có database. Không có live call.

### Files cần thay đổi / tạo mới

- Mới: `EXTENSIONS/.../cvf-web/src/components/QBSBenchmarkPanel.tsx`
- Mới: `EXTENSIONS/.../cvf-web/src/app/api/benchmark/qbs-summary/route.ts`
- Sửa: `EXTENSIONS/.../cvf-web/src/app/(dashboard)/governance/page.tsx` — thêm tab entry
- Mới: `EXTENSIONS/.../cvf-web/src/components/QBSBenchmarkPanel.test.tsx`

### GC-023 compliance

`governance/page.tsx` hiện 185 lines. Thêm tab entry (~5 lines). Component mới tách riêng. Không vi phạm.

### Boundary

- Không mutate bất kỳ QBS artifact nào
- Data là read-only từ static files
- Tab chỉ visible với role Owner/Admin (dùng permission check hiện có)
- Không có "chạy benchmark từ UI" — display only

### Exit criteria

- [ ] Tab "📈 Benchmark" hiển thị đúng trong `/governance`
- [ ] Run summary table hiển thị R5-R9 với đúng kappa/delta values
- [ ] Per-family bar chart render không có JS error
- [ ] Status badge đọc đúng từ file
- [ ] `npm run test:run` (unit test component): PASS
- [ ] `npm run build`: PASS
- [ ] `npm run lint`: PASS (max-warnings=0)

### Estimated effort: 2–3 ngày

---

## 4. Track C — Audit Receipt Integrity

### Mục tiêu

Document và optionally implement Git-as-hash-chain như một **intentional design decision** cho Audit Receipt integrity. Đảm bảo mọi evidence artifact có thể được verified là không bị mutate sau khi committed.

### Vấn đề EA cần giải quyết

CVF có Audit Trail nhưng **không có integrity proof** — evidence có thể bị sửa mà không bị phát hiện nếu Git history bị rewrite. Đây là **Auditability** gap — một trong những trụ cột của governance framework ở cấp enterprise/compliance.

### Điều kiện tiên quyết

- [ ] Git history intact (đã có — từ trước)
- [ ] `docs/evidence/` structure tồn tại
- [ ] Không cần thay đổi bất kỳ governance logic nào

### Scope kỹ thuật (2 phase)

**Phase C.1 — Document Git-as-hash-chain (bắt buộc):**

Viết `docs/reference/CVF_AUDIT_RECEIPT_INTEGRITY_MODEL.md` documenting:
- Git commit SHA = content-addressable hash chain
- Mọi QBS artifact sau khi pushed là immutable từ governance perspective
- Cách verify: `git log --oneline docs/benchmark/` trace được về từng thay đổi
- Limitation: requires private key for GPG signing — hiện tại chưa có, đây là known gap

**Phase C.2 — Optional: SHA manifest cho evidence files (nếu user approve):**

Script `scripts/generate_evidence_manifest.py`:
- Walk `docs/benchmark/qbs-1/` và `docs/evidence/`
- Tính SHA-256 cho mỗi file
- Output: `docs/evidence/MANIFEST_SHA256.json` với `{filepath: sha256, generated_at: ISO8601, git_commit: HEAD}`
- Để verify sau này: `python scripts/verify_evidence_manifest.py`

### Boundary

- Không retroactively mutate QBS artifacts
- Manifest là additive metadata, không thay thế Git history
- GPG signing deferred — đây là known limitation, documented explicitly

### Exit criteria

- [ ] `docs/reference/CVF_AUDIT_RECEIPT_INTEGRITY_MODEL.md` written và reviewed
- [ ] (Phase C.2 nếu approved) Manifest script generates valid JSON
- [ ] (Phase C.2) Verify script catches intentional mutation
- [ ] `python scripts/check_public_surface.py`: PASS

### Estimated effort: 1 ngày (C.1) + 1 ngày (C.2 nếu approved)

---

## 5. Track D — Multi-provider / Multi-agent Policy Engine

### Mục tiêu

Thiết kế và implement **Provider Strategy Pattern** trong CVF gateway: user đề xuất preference (provider/model/role), governance engine quyết định routing dựa trên risk profile, quota, và policy. Phục vụ cả dev (flexibility) và noncoder (simple choice UI).

### Vấn đề EA cần giải quyết

CVF hiện hardcode "1 provider per request" trong `/api/execute`. Không có runtime support cho:
1. **Multi-provider failover**: nếu Alibaba lỗi, tự động chuyển sang DeepSeek
2. **Role-based model routing**: dùng `qwen-turbo` cho Executor, `qwen3-max` cho Reviewer
3. **User preference + governance override**: user chọn "fast/cheap" hay "accurate/safe", governance quyết định final provider

### Điều kiện tiên quyết — PHẢI HOÀN TẤT TRƯỚC KHI BẮT ĐẦU

- [ ] **Track A phải complete** — cần governance tax baseline trước khi thêm routing layer (để biết overhead của routing)
- [ ] **GC-018 candidate phải được tạo và approved** — đây là architectural change cho runtime execution contract
- [ ] `governance/toolkit/05_OPERATION/` cần review — routing logic phải không bypass bất kỳ guard nào
- [ ] Model manifest format từ QBS-36 (`adjudicator-model-manifest-qbs36.json`) có thể tái dụng làm schema
- [ ] User phải approve: provider routing có được governance-overridable không? (doctrine question)

### Scope kỹ thuật

**Architecture:**

```
User Request
  {
    prompt: "...",
    provider_preference: "fast" | "accurate" | "local" | null,
    model_hint: "qwen-turbo" | null,   // hint, not command
    topology: "single" | "review-chain" | "failover"
  }
       ↓
CVF Provider Policy Engine (mới)
  - Đọc risk score từ Policy Engine (đã có)
  - Áp dụng Provider Selection Policy:
      R0 (safe)    → dùng provider_preference nếu có, default sinlge
      R1 (low)     → cho phép user preference, log routing decision
      R2 (medium)  → override về approved provider list, user preference ignored
      R3 (high)    → single approved provider only, no user override
  - Output: resolved_provider, resolved_model, topology, routing_reason
       ↓
Provider Adapter (đã có — Alibaba/OpenAI/DeepSeek)
```

**Topologies hỗ trợ:**

| Topology | Mô tả | Use case |
|---|---|---|
| `single` | 1 provider, 1 model (hiện tại) | Default cho mọi request |
| `failover` | Provider A → fallback Provider B nếu lỗi | Reliability |
| `review-chain` | Provider A (Executor) → Provider B (Reviewer) | Builder handoff quality |

**UI (Web):**

Trong Settings page hoặc Agent chat — thêm "Provider Preference" selector:
- "Tiết kiệm / Fast" → hint: cheap model
- "Chính xác / Accurate" → hint: capable model
- "Tự động / Auto" → governance decides (default)

Noncoder không thấy provider names — chỉ thấy preference tier.

### Files cần thay đổi / tạo mới

- Mới: `EXTENSIONS/.../cvf-web/src/lib/provider-policy-engine.ts`
- Mới: `EXTENSIONS/.../cvf-web/src/lib/provider-policy-engine.test.ts`
- Sửa: `EXTENSIONS/.../cvf-web/src/app/api/execute/route.ts` — wire provider policy engine
- Sửa: `EXTENSIONS/.../cvf-web/src/lib/ai/types.ts` — thêm topology + routing metadata
- Mới: `docs/benchmark/qbs-1/provider-routing-policy.md` — governance policy document
- Sửa: Settings UI — thêm provider preference selector

### GC-018 requirement

Đây là **architectural change cho runtime execution contract** — cần GC-018 với:
- Scope: Provider Policy Engine — routing layer above adapters
- Risk: R1 (thêm routing logic không thay đổi guard contract)
- Exit criteria: Track A complete + governance tax baseline established + routing overhead < 5% additional tax

### Boundary

- Provider Policy Engine KHÔNG override hard gates (BLOCK/CLARIFY/NEEDS_APPROVAL)
- Provider Policy Engine chỉ quyết định WHICH provider/model khi decision là ALLOW
- Noncoder không thấy provider names — abstracted qua preference tiers
- Topology `review-chain` deferred đến Phase D.2 (sau Phase D.1 single/failover stable)

### Exit criteria

**Phase D.1 (single + failover):**
- [ ] GC-018 approved
- [ ] Provider Policy Engine unit tests: PASS
- [ ] Routing decision logged trong governance receipt
- [ ] Failover tested với mock provider failure
- [ ] Governance tax tăng không quá 5% so với baseline từ Track A
- [ ] `npm run build`: PASS
- [ ] `python scripts/check_public_surface.py`: PASS

**Phase D.2 (review-chain):**
- [ ] Phase D.1 stable ≥ 1 tuần
- [ ] QBS R10 hoặc sau có data về builder-handoff quality improvement
- [ ] Separate GC-018 candidate

### Estimated effort: D.1 = 5–7 ngày, D.2 = 3–5 ngày (sau D.1)

---

## 6. Track E — DLP Quality Benchmark

### Mục tiêu

Thiết lập benchmark đo chất lượng của chính module DLP/Redaction: false positive rate (block nội dung an toàn), false negative rate (để lọt PII thật). Đây là meta-benchmark — CVF đo AI output, nhưng ai đo CVF?

### Vấn đề EA cần giải quyết

CVF có `admin/dlp` page nhưng **không có benchmark về chất lượng DLP**. Đây là **Verifiability** gap — framework phải tự chứng minh control của nó hoạt động đúng, không chỉ tuyên bố "có DLP". Trong môi trường production nghiêm túc, false negative rate là một architectural risk phải được quantify.

### Điều kiện tiên quyết — PHẢI HOÀN TẤT TRƯỚC KHI BẮT ĐẦU

- [ ] **Track A phải complete** — cần biết DLP phase latency (từ governance tax logger) trước khi benchmark nó
- [ ] **GC-018 candidate phải được tạo và approved**
- [ ] Cần define PII test corpus — không dùng real PII, dùng synthetic data
- [ ] User phải approve synthetic PII corpus policy: loại dữ liệu nào cần test (email, phone, API key, CCCD, etc.)
- [ ] Review `admin/dlp` implementation để hiểu DLP engine hiện tại dùng gì (regex? model?)

### Scope kỹ thuật

**Test corpus (synthetic):**

```
Category 1: True PII (phải bị redact)
  - Email: test@example.com (pattern rõ)
  - API Key: sk-1234567890abcdef... (pattern rõ)
  - Phone VN: 0912345678 (pattern rõ)
  - CCCD: 079201234567 (pattern VN)

Category 2: False PII (không được block)
  - Số version: v1.2.3
  - Code snippet chứa string giống key
  - Tên biến: email_validator
  - URL: https://example.com/api/key-value-store

Category 3: Adversarial (prompt injection-style)
  - PII được encode: base64, leetspeak, spaces
  - PII trong code comment
```

**Metrics:**

```
precision = true_redacted / (true_redacted + false_redacted)
recall    = true_redacted / (true_redacted + false_passed)
f1        = harmonic_mean(precision, recall)
```

**Output:** `docs/benchmark/dlp/dlp-benchmark-v1.json` + `scripts/run_dlp_benchmark.py`

### Boundary

- Không dùng real PII trong corpus — synthetic only
- Corpus files không được commit nếu chứa bất kỳ real identifier nào
- Benchmark là offline/local — không cần live provider call
- Không thay đổi DLP logic trong tranche này — chỉ đo, không sửa

### Exit criteria

- [ ] GC-018 approved
- [ ] Synthetic corpus reviewed và approved bởi user
- [ ] `scripts/run_dlp_benchmark.py` chạy và output metrics
- [ ] Baseline F1 score documented
- [ ] Memory footprint của DLP scan measured (heapUsed before/after)
- [ ] `python scripts/check_public_surface.py`: PASS

### Estimated effort: 3–4 ngày (sau Track A complete)

---

## 7. Sequencing & Dependency Map

```
QBS Track (hiện tại, độc lập):
  QBS-33 → QBS-34 → QBS-35 → QBS-36 → QBS-37 → QBS-38 → QBS-39
  → Checkpoint → R10 pre-registration → R10 live (với --confirm-live-cost)

EA Enhancement Track (song song, độc lập):

  Ngay bây giờ (parallel với QBS-3x):
  ┌─────────────────────────────────────┐
  │  Track A: Governance Tax            │  2–3 ngày
  │  Track B: Benchmark Dashboard Web  │  2–3 ngày  (có thể song song với A)
  │  Track C: Audit Receipt Integrity   │  1–2 ngày  (có thể song song với A,B)
  └─────────────────────────────────────┘
           ↓ (A phải complete)
  ┌─────────────────────────────────────┐
  │  Track D: Multi-provider Engine     │  5–7 ngày  (cần GC-018)
  └─────────────────────────────────────┘
           ↓ (A phải complete + D.1 optional)
  ┌─────────────────────────────────────┐
  │  Track E: DLP Quality Benchmark     │  3–4 ngày  (cần GC-018)
  └─────────────────────────────────────┘

Điểm hội tụ với QBS:
  Sau R10 → nếu Track D (review-chain topology) cần validate quality improvement
  → link QBS family data với routing decision logs
```

---

## 8. Risk Registry

| Risk | Track | Mức độ | Mitigations |
|---|---|---|---|
| Track A timing instrumentation làm chậm request | A | Thấp | `performance.now()` overhead < 0.1ms; test với mock mode trước |
| Track B dashboard expose sensitive QBS data | B | Thấp | Role-gate (Owner/Admin only); data từ artifacts đã public trên GitHub |
| Track C manifest script tính nhầm SHA | C | Thấp | Unit test với known fixtures |
| Track D routing engine bypass governance guard | D | **Cao** | Routing chỉ active sau ALLOW decision; guard contract test phải bao gồm routing cases |
| Track D provider preference create new attack surface | D | Trung | Preference là hint only; governance override ở R2/R3; log mọi routing decision |
| Track E synthetic corpus leak real PII | E | Trung | Review trước khi commit; `.gitignore` corpus folder until reviewed |
| Track D/E scope creep vào QBS timeline | D, E | Trung | Tách riêng clone/branch; không touch QBS artifacts |

---

## 9. Câu hỏi cần Codex phản biện

1. **Track A:** `performance.now()` trong Next.js API route có đủ độ chính xác để đo governance overhead hay cần Node.js `process.hrtime.bigint()`?

2. **Track B:** Data source là static JSON files đọc trực tiếp trong API route có ổn không (file I/O mỗi request), hay cần cache ở module level?

3. **Track D:** CVF doctrine nói "governance-first" — provider preference từ user có vi phạm doctrine không? Hay đây là acceptable user agency trong governance boundary?

4. **Track D:** `review-chain` topology (Executor → Reviewer) có tạo ra circular governance risk không — nếu Reviewer model cũng phải qua CVF gateway thì governance overhead có nhân đôi không?

5. **Track E:** DLP benchmark nên chạy ở unit test level (mocked DLP) hay integration test level (thật)? Nếu unit test thì benchmark không phản ánh thực tế; nếu integration test thì mỗi lần CI chạy đều tốn resource.

6. **Quản lý chung:** 2 roadmap riêng biệt — có cần một "coordination gate" chính thức (document/meeting) trước khi bắt đầu EA track, hay author (Claude/Codex) có thể bắt đầu Track A+B+C ngay sau khi Codex approve proposal này?

---

## 10. Không thuộc scope roadmap này

- Prometheus / Grafana / external monitoring — không justify cho local-first framework
- Concurrency stress test (50-100 agents) — không phản ánh threat model CVF
- Gemini / Anthropic provider expansion — deferred per QBS locked decision
- Human review cho DLP corpus — deferred; model-only là acceptable với documented boundary
- Re-running bất kỳ QBS scored run nào — thuộc QBS track, không thuộc đây
- Thay đổi governance hard gates (BLOCK/CLARIFY/NEEDS_APPROVAL logic) — out of scope

---

*Document này sẵn sàng để Codex review trước khi bắt đầu bất kỳ track nào.*
