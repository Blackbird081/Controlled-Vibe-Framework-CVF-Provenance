"""Focused tests for the MSEA-R28-T1 MinerU metadata receipt writer."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mineru_metadata_receipt_writer import (  # noqa: E402
    DOWNSTREAM_RELEASE_HELD,
    MineruMetadataReceiptValidationError,
    build_mineru_metadata_receipt,
    mineru_metadata_receipt_payload,
    render_mineru_metadata_receipt_json,
)


VALID_SHA = "sha256:" + ("a" * 64)


def _receipt(**overrides):
    params = {
        "receipt_id": "msea-r28-t1:receipt-001",
        "source_input_slot": "candidate-group-a-private-input",
        "input_sha256": VALID_SHA,
        "output_file_names": [
            "layout.pdf",
            "span.pdf",
            "model.json",
            "middle.json",
            "content_list.json",
            "content_list_v2.json",
            "document.md",
        ],
        "quality_report_ref": "msea-r28-t5:quality-report-001",
        "source_pointer": "msea-r28-t5:source-pointer-001",
    }
    params.update(overrides)
    return build_mineru_metadata_receipt(**params)


def test_receipt_payload_contains_required_r24_r26_metadata_fields() -> None:
    payload = mineru_metadata_receipt_payload(_receipt())

    assert payload["receiptId"] == "msea-r28-t1:receipt-001"
    assert payload["sourceInputSlot"] == "candidate-group-a-private-input"
    assert payload["inputSha256"] == VALID_SHA
    assert payload["outputFileNames"] == [
        "layout.pdf",
        "span.pdf",
        "model.json",
        "middle.json",
        "content_list.json",
        "content_list_v2.json",
        "document.md",
    ]
    assert payload["outputContentRead"] is False
    assert payload["privateOutputDisposition"] == "RECEIPT_METADATA_ALLOWED"
    assert payload["downstreamRelease"] == DOWNSTREAM_RELEASE_HELD
    assert payload["qualityReportRef"] == "msea-r28-t5:quality-report-001"
    assert payload["sourcePointer"] == "msea-r28-t5:source-pointer-001"


def test_json_rendering_is_stable_and_metadata_only() -> None:
    first = render_mineru_metadata_receipt_json(_receipt())
    second = render_mineru_metadata_receipt_json(_receipt())
    payload = json.loads(first)

    assert first == second
    assert first.endswith("\n")
    assert payload["receiptVersion"] == "cvf.mineruMetadataReceipt.r28t5.v2"
    assert '"outputContentRead": false' in first
    assert "extractedText" not in first
    assert "rawOcrText" not in first
    assert "documentBody" not in first
    assert '"text"' not in first


@pytest.mark.parametrize(
    "file_name",
    [
        "layout.pdf",
        "span.pdf",
        "model.json",
        "middle.json",
        "content_list.json",
        "content_list_v2.json",
        "safe-output.md",
    ],
)
def test_allowed_mineru_output_family_names_are_metadata_only(file_name: str) -> None:
    receipt = build_mineru_metadata_receipt(
        receipt_id="receipt-allowed",
        source_input_slot="private-input-slot",
        input_sha256=VALID_SHA,
        output_file_names=[file_name],
        quality_report_ref="msea-r28-t5:quality-report-002",
        source_pointer="msea-r28-t5:source-pointer-002",
    )

    assert receipt.output_file_names == (file_name,)
    assert receipt.output_content_read is False


@pytest.mark.parametrize(
    ("kwargs", "token"),
    [
        ({"receipt_id": ""}, "INVALID_RECEIPT_ID"),
        ({"source_input_slot": "raw:document"}, "INVALID_SOURCE_INPUT_SLOT"),
        ({"input_sha256": "sha256:NOTLOWER"}, "INVALID_INPUT_SHA256"),
        ({"output_file_names": ["../layout.pdf"]}, "INVALID_OUTPUT_FILE_NAME"),
        ({"output_file_names": ["folder/layout.pdf"]}, "INVALID_OUTPUT_FILE_NAME"),
        ({"output_file_names": ["raw:content.txt"]}, "INVALID_OUTPUT_FILE_NAME"),
        ({"output_file_names": ["full_text.txt"]}, "INVALID_OUTPUT_FILE_NAME"),
        ({"output_file_names": []}, "INVALID_OUTPUT_FILE_NAME"),
        ({"output_content_read": True}, "OUTPUT_CONTENT_READ_FORBIDDEN"),
        ({"quality_report_ref": ""}, "QUALITY_OR_SOURCE_POINTER_MISSING"),
        ({"quality_report_ref": "raw:quality-notes"}, "QUALITY_OR_SOURCE_POINTER_MISSING"),
        ({"source_pointer": ""}, "QUALITY_OR_SOURCE_POINTER_MISSING"),
        ({"source_pointer": "text:full-document"}, "QUALITY_OR_SOURCE_POINTER_MISSING"),
    ],
)
def test_invalid_metadata_fails_closed(
    kwargs: dict[str, object],
    token: str,
) -> None:
    params: dict[str, object] = {
        "receipt_id": "receipt-001",
        "source_input_slot": "private-input-slot",
        "input_sha256": VALID_SHA,
        "output_file_names": ["layout.pdf"],
        "quality_report_ref": "msea-r28-t5:quality-report-003",
        "source_pointer": "msea-r28-t5:source-pointer-003",
    }
    params.update(kwargs)

    with pytest.raises(MineruMetadataReceiptValidationError) as exc_info:
        build_mineru_metadata_receipt(**params)

    assert exc_info.value.token == token


def test_downstream_lanes_remain_held_for_future_packets() -> None:
    payload = mineru_metadata_receipt_payload(_receipt())
    boundary = payload["claimBoundary"]

    assert payload["downstreamRelease"] == "HELD_PENDING_RECEIPT_CHECKER_AND_MEMORY_ROUTE"
    assert "runtime readiness" in str(boundary)
    assert "memory ingestion readiness" in str(boundary)
    assert "RAG readiness" in str(boundary)
    assert "production workflow readiness" in str(boundary)
