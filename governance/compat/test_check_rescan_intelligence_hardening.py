from governance.compat.check_rescan_intelligence_hardening import check_text


VALID_BLOCK = """
# External Review Rescan

Status: CLOSED_PASS_BOUNDED

## Rescan Intelligence Hardening

- Original source artifact: docs/assessments/source.docx
- Predecessor intake artifact: docs/assessments/intake.md
- Delta ledger status: COMPLETE
- Routing matrix status: COMPLETE
- Semantic sampling status: COMPLETE
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Current | Prior | Category | Reason |
| --- | --- | --- | --- |
| RS-01 | F1 | UNCHANGED_FROM_INTAKE | Still valid. |
| RS-02 | F2 | CHANGED_DISPOSITION | Split into narrower findings. |
| RS-03 | N/A | NEW_FINDING | Found during full rescan. |
| RS-04 | F4 | REMOVED_OR_REJECTED | Rejected by source evidence. |

### Follow-Up Routing Matrix

| Finding | Lane | Action |
| --- | --- | --- |
| RS-01 | DO_NOW | Dispatch implementation. |
| RS-02 | SEPARATE_RUNTIME_TRANCHE | Separate runtime tranche. |
| RS-03 | STRATEGIC_OPERATOR_DECISION | Operator decision. |
| RS-04 | OUT_OF_SCOPE | Not technical work. |
| RS-05 | RESOLVED_BY_DESIGN | Already covered. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| S-01 | section 4.4 | architecture gap | routed | Could be buried. | PASS |
| S-02 | section 7 | benchmark gap | routed | Could be overclaimed. | PASS |
| S-03 | section 10 | recommendation | routed | Could mix lanes. | PASS |
"""


def test_valid_rescan_block_passes():
    assert check_text("docs/assessments/CVF_RESCAN_SAMPLE.md", VALID_BLOCK) == []


def test_missing_delta_category_fails():
    text = VALID_BLOCK.replace("REMOVED_OR_REJECTED", "REMOVED")
    violations = check_text("docs/assessments/CVF_RESCAN_SAMPLE.md", text)
    assert any(item["type"] == "delta_category_missing" for item in violations)


def test_missing_routing_lane_fails():
    text = VALID_BLOCK.replace("RESOLVED_BY_DESIGN", "DONE")
    violations = check_text("docs/assessments/CVF_RESCAN_SAMPLE.md", text)
    assert any(item["type"] == "routing_lane_missing" for item in violations)


def test_non_rescan_doc_is_not_applicable():
    assert check_text("docs/assessments/CVF_PLAIN_NOTE.md", "# Plain Note\n\nNo bounded corpus claim.\n") == []


def test_runtime_work_order_reference_to_external_review_is_not_applicable():
    text = """
# Runtime Work Order

Status: CLOSED_PASS_BOUNDED

## Purpose

Convert one external-review architecture finding into runtime hardening.
"""
    assert check_text("docs/work_orders/CVF_WO_RUNTIME_DURABILITY_2026-06-05.md", text) == []


def test_rescan_keyword_inside_code_fence_is_not_applicable():
    text = """
# Plain Note

Status: CLOSED_PASS_BOUNDED

```text
this is a rescan example used only as fenced sample text
```
"""
    assert check_text("docs/reviews/CVF_PLAIN_NOTE.md", text) == []


def test_rescan_keyword_inside_na_line_is_not_applicable():
    text = """
# Plain Note

Status: CLOSED_PASS_BOUNDED

- Rescan applicability: N/A with reason: not a rescan or knowledge absorption output
"""
    assert check_text("docs/reviews/CVF_PLAIN_NOTE.md", text) == []


def test_rescan_keyword_in_real_prose_still_applicable():
    text = """
# Real Rescan Note

Status: CLOSED_PASS_BOUNDED

This document performs a full rescan of the prior intake findings.
"""
    violations = check_text("docs/reviews/CVF_REAL_RESCAN.md", text)
    assert any(item["type"] == "rescan_hardening_section_missing" for item in violations)


def test_complete_claim_cannot_use_not_applicable():
    text = VALID_BLOCK.replace("COMPLETE_WITH_DELTA_ROUTING_SAMPLE", "NOT_APPLICABLE_WITH_REASON")
    violations = check_text("docs/assessments/CVF_RESCAN_SAMPLE.md", text)
    assert any(item["type"] == "not_applicable_used_for_completion_claim" for item in violations)
