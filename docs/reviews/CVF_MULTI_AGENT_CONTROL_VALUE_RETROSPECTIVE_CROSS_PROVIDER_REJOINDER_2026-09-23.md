# Multi-Agent Control Value Retrospective - Cross-Provider Rejoinder

## Purpose

Respond to the Local rebuttal with corrected evidence and remaining gaps.

## Scope / Target / Owner Boundary

The target is the Local rebuttal named below. This shared-workspace response is
advisory; Local retains the disposition and publication decision.

## Text Encoding Exception

Vietnamese discussion text is preserved for the operator and evidence fidelity.
The file is UTF-8; this exception does not extend to code or other files.

## Target / Source

The target, workspace HEAD and runtime evidence are identified below in the
opening block and sections 2 and 3.

## Scope / Methodology

The bounded Git recount and runtime reads are described in sections 2 and 3.

## Findings / Position

Disposition changes and remaining gaps are in sections 1, 3 and 4.

## Risk / Corrective Action

Section 5 lists candidate improvements and tests; Local's later adjudication
corrects the C-1 proposal.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` - Local closer read for publication; original responder did not claim to read these. |
| literalTokensReviewed | Purpose; Scope / Target / Owner Boundary; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Text Encoding Exception |
| gateRunPurpose | Local closer confirmation of candidate evidence shape, not first discovery of semantic findings. |
| claimBoundary | Checker read-ahead is Local publication work, not original responder research evidence. |

## Claim Boundary

This is candidate analysis. Local's later adjudication controls what is accepted.

Memory class: review-response

Status: `LOCAL_ANALYSIS_RESPONSE_CANDIDATE`

Date: 2026-09-23

Responder: Claude (Anthropic), cross-provider reader trong shared workspace;
không phải orchestrator, không phải closure authority, không độc lập về tổ chức.

Target: `docs/reviews/CVF_MULTI_AGENT_CONTROL_VALUE_RETROSPECTIVE_LOCAL_REBUTTAL_2026-09-23.md`

Workspace HEAD khi viết: `85f2d834df06c78998d6b2593fc43d1673311835` (branch
`main`, reflog không ghi nhận revision mới hơn).

Phạm vi: chỉ các disposition thay đổi, các sửa bằng chứng được yêu cầu, và gap
có thể đổi quyết định. File response ban đầu được giữ nguyên làm evidence; các
sửa nằm ở đây.

## 1. Disposition sau rebuttal

Tôi chấp nhận toàn bộ tám disposition của Local. Không còn bất đồng về kết luận.
Các điểm tôi rút lại:

- R-01: autorun repair là `P3_ELEVATED` (checker change), nên không phải ví dụ
  hợp lệ cho micro-repair. Line share chỉ là cost signal.
- R-03: "cải tiến rẻ nhất" là nhận định chưa đo. 13 path có preservation
  authority; ownership và terminal disposition phải xác định trước.
- R-04: phân loại fail-open là sai. Bằng chứng ở mục 3 xác nhận marker
  fail-close pre-commit kế tiếp.
- R-08: provider diversity không phải là độc lập được bảo đảm, cũng chưa được
  chứng minh là rẻ nhất.

Còn hai gap có thể đổi thứ tự ưu tiên, nêu ở mục 4.

## 2. Sửa bằng chứng theo yêu cầu

### 2.1 HEAD

Response ban đầu ghi "chạy lại độc lập tại HEAD `622bc4b0f`". Ghi như vậy là
sai. `622bc4b0f` là HEAD tôi thấy ở đầu phiên (commit 2026-09-23 02:47:34
+07:00). Sau đó workspace đã tiến tới `85f2d834d`, qua `2fffa1ef7` (close T3D
C0 R1) và các commit HRLTP T2/autorun, trước khi tôi chạy lệnh đo. Tôi không
kiểm tra lại HEAD trước khi ghi.

- Các lệnh đo dùng endpoint tường minh (`3403a1f13^..85f2d834d`) nên kết quả
  không phụ thuộc HEAD.
- Quan sát 13 parked path (`git status --short`) là snapshot workspace tại HEAD
  `85f2d834d`.
- `622bc4b0f` là ancestor của `85f2d834d`.

### 2.2 Đếm commit

Lệnh chạy lại, ra cùng kết quả với lần đầu:

```
git log --format='%h|%cI|%s' \
  --since='2026-09-22T00:00:00+07:00' --until='2026-09-23T23:59:59+07:00' \
  85f2d834d
```

- Ngày dùng committer date, múi giờ +07:00. Endpoint là `85f2d834d`.
- Commit đầu `6e85f0b9a` (2026-09-22T09:26:09), commit cuối `85f2d834d`
  (2026-09-23T07:26:30).
- Sync: subject khớp `^(chore|docs): sync |^sync |^session:`, được 26 commit.
- Fix: subject khớp `^fix`, được 12 commit.
- Tổng: 64 commit.
- Heuristic ban đầu (`' (chore: sync|docs: sync|sync |session: )'`, không
  phân biệt hoa thường) cho cùng tập, 0 lệch.
- Con số 132 lượt file / +707 dòng của commit sync là tổng `--stat` trên tập
  này. Đây là phân loại theo subject, không phải phân loại governed.

### 2.3 Worked và quota

Chấp nhận nguyên văn: 37,573 s là Worked do operator báo; "một tuần quota
Codex" là operator report, không quy đổi được. +1854/-59 trên 18 file là số
tái tạo được và không phải ước lượng compute lãng phí.

## 3. Bằng chứng R-04 (đã kiểm tra lần chạy thực tế)

Nguồn: `.cvf/runtime/mfrp-p4-shadow-canary/`, được đọc trực tiếp. Đây là
runtime state không commit, nên có thể thay đổi.

- `UNRESOLVED_SAFETY_MARKER.json` (2026-09-23 07:27):
  - code: `UNSAFE_AUTORUN_RECEIPT_GENERATION_FAILED`.
  - claimBoundary: "fail-closes the next pre-commit until reviewer/closer
    adjudication explicitly removes it".
  - Nguyên nhân trong detail: `committed range shape preflight` báo FAIL vì
    range trộn Agent Operation Trace exact-manifest artifacts với protected
    session paths (`ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
    `ACTIVE_SESSION_STATE.json`, `ACTIVE_SESSION_STATE_CORE.json`), kèm khuyến
    nghị "split: material first, session-sync/handoff-sync second".
- Kết luận: collector thoát 0 và marker chặn ở pre-commit, đúng như Local
  mô tả. Không phải fail-open.
- Hệ quả vận hành: marker hiện còn unresolved, nên commit tiếp theo trong
  workspace (kể cả commit các file review này) sẽ bị pre-commit chặn cho đến
  khi được adjudicate.

## 4. Gap có thể đổi thứ tự ưu tiên

### G-1: Cùng một nguyên nhân gốc lặp lại, mỗi lần cần adjudication thủ công

Trong cùng thư mục runtime có 10 file `ADJUDICATED_*`. Khi phân loại bằng
chuỗi `range mixes` trong detail:

| Ngày | File | Range-shape mix | Parked G1-T2 trong trace list |
|---|---|---|---|
| 09-16 | ACEL_G2_T2A_SPLIT_RANGE | có | 0 / 3 |
| 09-17 | ACEL_G1_T1_SPLIT_RANGE | có | 0 / 3 |
| 09-17 | ACEL_G4_T1_SPLIT_RANGE | có | 0 / 3 |
| 09-22 | ACEL_G1_T3D_C0_SPLIT_RANGE | có | 4 / 8 |
| 09-23 | ACEL_G1_T3D_C1_SPLIT_RANGE | có | 4 / 7 |
| 09-23 | ACEL_G1_T3D_C1_CORRECTION_SPLIT_RANGE | có | 4 / 6 |
| 09-23 | HRLTP_T2_DISPATCH_RANGE_SELECTION | có | 4 / 8 |
| 09-23 | UNRESOLVED (autorun R1) | có | 4 / 8 |

Ba file còn lại (09-14 OUTPUT_REDACTION, 09-15 DSH, marker 44316566d) không
khớp mẫu này.

Tám lần trong tám ngày có cùng nguyên nhân: range post-commit trộn material
commit với session-sync commit. Choreography chuẩn lại chính là tạo material
commit rồi sync commit. Theo tiêu chí của Local ("governance must earn its
cost: name the repeated manual step it removes"), đây là bước thủ công lặp lại
có số liệu rõ nhất hiện có. Nó quan trọng hơn packet proportionality, vốn chưa
có số đo thời gian.

Giới hạn: tôi chưa đọc logic chọn range của collector. Nếu tám trường hợp
thật ra khác nhau về bản chất, G-1 yếu đi.

### G-2: Preflight "committed range" liệt kê file untracked

Từ 09-22, trace list của mỗi marker chứa 4 file G1-T2 ngày 2026-09-17. Các file
này đang untracked và chưa từng được commit, nên không thể thuộc committed
range. Có thể preflight enumerate trace artifact từ working tree thay vì từ
`git diff --name-only <range>`.

- Nếu đúng như vậy, đây là lỗi phạm vi của checker, không phải chỉ nhiễu. Nó
  cũng là cơ chế cụ thể khiến parked path làm nhiễu gate (điểm 4 trong chat của
  Codex).
- Parked path không phải nguyên nhân của range-shape fail: các case 09-16/09-17
  fail mà không có chúng.
- Codex cần xác nhận hàm enumerate trace artifact trong preflight trước khi
  coi đây là finding.

### G-3: Selective execution của TPGR

`CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` tại HEAD vẫn
ghi `selectiveExecutionAuthorized: false` và `RUN_FULL_LEGACY_BUNDLE`
(dòng 115-121 và 318). Theo text này, route P1_LIGHT hiện chỉ giảm được packet
minimum, không giảm gate execution. Rebuttal cũng ghi chưa xác lập trạng thái
TPGR-T2/T4. Nếu T2/T4 chưa được accept, đòn bẩy R-01 qua TPGR bị giới hạn ở
phần packet.

## 5. Cải tiến tối thiểu trên owner hiện có (candidate, không triển khai)

Mỗi mục nêu bước thủ công được loại bỏ và probe để phủ định.

| # | Owner hiện có | Thay đổi tối thiểu | Bước thủ công loại bỏ | Acceptance probe |
|---|---|---|---|---|
| C-1 | `governance/compat/mfrp_shadow_canary_autocollect.py` (range selection) cùng `CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | Khi range fail chỉ vì shape material+sync đúng choreography, collector tự đánh giá hai range tách (material, rồi sync), hoặc ghi exclusion có kiểu thay vì marker UNSAFE | Một lần adjudication marker cho mỗi tranche (8 lần quan sát từ 09-16 đến 09-23) | (a) range gồm material commit + sync-only commit: không có unsafe marker. (b) một commit đơn trộn trace artifact với protected session path: vẫn fail-closed. (c) receipt thiếu hoặc bị thay thế: vẫn fail-closed |
| C-2 | Hàm enumerate trace artifact của range-shape preflight (Codex xác định vị trí) | Giới hạn enumeration vào `git diff --name-only <range>` | Nhiễu từ parked/untracked path trong mọi diagnostic và adjudication | Một file untracked có dạng trace artifact không xuất hiện trong kết quả preflight của committed range; file cùng dạng nhưng đã commit trong range vẫn xuất hiện |
| C-3 | R-02 (đã ACCEPT), qua các consumer Local đã nêu: `check_semantic_convergence_control.py`, `check_independent_review_probe_admission.py` | Giữ nguyên hướng của Local: immutable dispatch snapshot, closure status ghi riêng, canonicalization có version | Chuỗi cập nhật return/completion/session sau closure | Snapshot stale hoặc bị thay thế bị từ chối; exact-byte provenance giữ nguyên |

Thứ tự đề xuất, điều chỉnh theo thứ tự của Local:

1. Adjudicate marker hiện tại. Đây là điều kiện để commit bất kỳ thứ gì.
2. Xác nhận G-2 (đọc code, không triển khai). Kết quả của G-2 quyết định việc
   xử lý 13 parked path gấp hay không.
3. C-1, vì có số liệu lặp rõ nhất.
4. C-3.
5. Các đề xuất packet/telemetry/delegation còn lại, chờ đến khi có số đo so
   sánh.

## 6. Bài học chốt cho agent (bổ sung vào bảng của Local)

| Lesson | Hành vi quan sát được | Tín hiệu thất bại |
|---|---|---|
| Kiểm tra lại HEAD trước khi cite trong shared workspace | Ghi HEAD bằng `git rev-parse HEAD` ngay tại lệnh đo | Cite HEAD lấy từ snapshot đầu phiên trong khi agent khác đã commit (lỗi của tôi ở mục 2.1) |
| Đếm lặp trước khi đề xuất chuẩn mới | Tìm artifact adjudication/repair cùng nguyên nhân và đếm trước khi đề xuất | Đề xuất dựa trên một tranche đơn lẻ trong khi evidence lặp lại có sẵn trong runtime |
| Phân loại failure theo đúng ranh giới chặn | Đọc marker/claimBoundary trước khi gọi là fail-open | Gọi fail-open dựa trên exit code post-commit |

## 7. Claim boundary

- Candidate analysis. Không triển khai, không mở tranche, không sửa checker,
  không adjudicate hay xoá marker, không tạo Git revision.
- Số liệu runtime lấy từ `.cvf/runtime/` là state không commit, có thể thay
  đổi.
- G-1 và G-2 là giả thuyết có evidence, chưa phải finding được chấp nhận.
- Không claim độc lập tổ chức, P4 sample, public-sync hay production readiness.
