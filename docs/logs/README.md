# CVF Logs Archive

Memory class: POINTER_RECORD

Trạng thái: archive taxonomy cho append-only operational logs đã rollover khỏi active window.

## Purpose

- giữ lịch sử log dài hạn ở vị trí chuẩn, dễ tra soát
- giảm kích thước của active log đang được dùng hằng ngày
- bảo toàn append-only evidence chain mà không làm active file quá dài

## Scope

This folder holds bounded operational/session logs and archived long-running log
windows. It is not the default home for roadmap completion reviews, work
orders, or canonical standards.

## Owner Surface

Owner surface: CVF operational evidence, test-log archive, and mixed-session
execution traceability.

## What Belongs Here

- archived windows của `CVF_INCREMENTAL_TEST_LOG.md`
- các log chain dài hạn khác khi đã có rule rotation chính thức
- bounded multi-provider session execution logs when the operator explicitly
  needs post-session attribution, quality, cost, or tool-surface traceability

## Protocol

Logs in this folder should be append-safe or session-bounded, secret-safe, and
clear about whether claims are operator-reported, command-backed, receipt-backed,
or git-verified.

## Naming Rule

Archive log files trong folder này phải tuân thủ naming guard của CVF.

Ví dụ:

- `CVF_INCREMENTAL_TEST_LOG_ARCHIVE_2026_PART_01.md`
- `CVF_MULTI_PROVIDER_EXECUTION_LOG_2026-05-29_NIGHT_SESSION.md`

## Current Scope

Hiện tại folder này được chuẩn hóa trước hết cho:

- `CVF_INCREMENTAL_TEST_LOG.md`
- bounded mixed-provider execution logs governed by
  `docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md`

Các trace/review logs theo scope vẫn tiếp tục ở `docs/reviews/<scope>/` cho đến khi CVF ban hành rotation guard riêng cho từng trace chain đó.

## Enforcement

New governed Markdown logs must satisfy the structural completeness and docs
governance compatibility gates before they are used as closure evidence.

## Boundaries

This folder records evidence and operational traces. It does not by itself prove
runtime behavior, provider behavior, production readiness, public readiness, or
hidden agent reasoning.

## Related Artifacts

- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
- `docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md`
- `CVF_INCREMENTAL_TEST_LOG.md`

## Claim Boundary

Logs here are evidence pointers. Their claim strength depends on the receipts,
commands, diffs, and operator reports they cite.
