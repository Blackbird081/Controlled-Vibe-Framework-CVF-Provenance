"""Focused tests for the MSEA-R28-T1 MinerU metadata receipt writer."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mineru_metadata_receipt_writer import (  # noqa: E402
    DOWNSTREAM_RELEASE_HELD,
    MEMORY_WRITE_NOT_AUTHORIZED_BY_T12,
    MineruMetadataReceiptValidationError,
    MineruMetadataReceipt,
    MineruMemorySafeCandidateContract,
    build_mineru_metadata_receipt,
    build_mineru_memory_owner_admission_readout,
    build_mineru_memory_safe_candidate_contract,
    build_mineru_quality_report_source_pointer,
    mineru_memory_owner_admission_readout_payload,
    mineru_memory_safe_candidate_contract_payload,
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


def test_quality_report_source_pointer_helper_is_deterministic_and_receipt_compatible() -> None:
    refs = build_mineru_quality_report_source_pointer(
        receipt_id="msea-r28-t7:receipt-001",
        source_input_slot="candidate-group-a-private-input",
        input_sha256=VALID_SHA,
        quality_report_status="PASS",
        boundary_sha256="b" * 64,
        chunk_count=7,
    )
    repeated = build_mineru_quality_report_source_pointer(
        receipt_id="msea-r28-t7:receipt-001",
        source_input_slot="candidate-group-a-private-input",
        input_sha256=VALID_SHA,
        quality_report_status="PASS",
        boundary_sha256="b" * 64,
        chunk_count=7,
    )

    assert refs == repeated
    assert refs.quality_report_ref.startswith("quality-report:")
    assert refs.source_pointer.startswith("source-pointer:")
    assert "candidate-group-a-private-input" not in refs.quality_report_ref
    assert "candidate-group-a-private-input" not in refs.source_pointer

    receipt = build_mineru_metadata_receipt(
        receipt_id="msea-r28-t7:receipt-001",
        source_input_slot="candidate-group-a-private-input",
        input_sha256=VALID_SHA,
        output_file_names=["layout.pdf", "document.md"],
        quality_report_ref=refs.quality_report_ref,
        source_pointer=refs.source_pointer,
    )
    payload = mineru_metadata_receipt_payload(receipt)

    assert payload["qualityReportRef"] == refs.quality_report_ref
    assert payload["sourcePointer"] == refs.source_pointer
    assert payload["outputContentRead"] is False
    assert payload["downstreamRelease"] == DOWNSTREAM_RELEASE_HELD
    assert "extractedText" not in payload
    assert "rawOcrText" not in payload
    assert "documentBody" not in payload


def test_quality_report_source_pointer_helper_changes_with_quality_metadata() -> None:
    passed = build_mineru_quality_report_source_pointer(
        receipt_id="msea-r28-t7:receipt-002",
        source_input_slot="private-input-slot",
        input_sha256=VALID_SHA,
        quality_report_status="PASS",
        boundary_sha256="c" * 64,
        chunk_count=1,
    )
    partial = build_mineru_quality_report_source_pointer(
        receipt_id="msea-r28-t7:receipt-002",
        source_input_slot="private-input-slot",
        input_sha256=VALID_SHA,
        quality_report_status="PARTIAL_EXTRACTION",
        boundary_sha256="c" * 64,
        chunk_count=1,
    )

    assert passed != partial


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


@pytest.mark.parametrize(
    ("kwargs", "token"),
    [
        ({"quality_report_status": "raw:PASS"}, "QUALITY_OR_SOURCE_POINTER_MISSING"),
        ({"boundary_sha256": "sha256:" + ("b" * 64)}, "QUALITY_OR_SOURCE_POINTER_MISSING"),
        ({"chunk_count": -1}, "QUALITY_OR_SOURCE_POINTER_MISSING"),
        ({"input_sha256": "sha256:NOTLOWER"}, "INVALID_INPUT_SHA256"),
    ],
)
def test_quality_report_source_pointer_helper_fails_closed(
    kwargs: dict[str, object],
    token: str,
) -> None:
    params: dict[str, object] = {
        "receipt_id": "msea-r28-t7:receipt-003",
        "source_input_slot": "private-input-slot",
        "input_sha256": VALID_SHA,
        "quality_report_status": "PASS",
        "boundary_sha256": "d" * 64,
        "chunk_count": 3,
    }
    params.update(kwargs)

    with pytest.raises(MineruMetadataReceiptValidationError) as exc_info:
        build_mineru_quality_report_source_pointer(**params)

    assert exc_info.value.token == token


def test_downstream_lanes_remain_held_for_future_packets() -> None:
    payload = mineru_metadata_receipt_payload(_receipt())
    boundary = payload["claimBoundary"]

    assert payload["downstreamRelease"] == "HELD_PENDING_RECEIPT_CHECKER_AND_MEMORY_ROUTE"
    assert "runtime readiness" in str(boundary)
    assert "memory ingestion readiness" in str(boundary)
    assert "RAG readiness" in str(boundary)
    assert "production workflow readiness" in str(boundary)


def test_memory_safe_candidate_contract_is_deterministic_and_metadata_only() -> None:
    contract = build_mineru_memory_safe_candidate_contract(_receipt())
    repeated = build_mineru_memory_safe_candidate_contract(_receipt())
    payload = mineru_memory_safe_candidate_contract_payload(contract)

    assert contract == repeated
    assert contract.candidate_id.startswith("memory-safe-candidate:")
    assert payload == mineru_memory_safe_candidate_contract_payload(repeated)
    assert payload["receiptId"] == "msea-r28-t1:receipt-001"
    assert payload["qualityReportRef"] == "msea-r28-t5:quality-report-001"
    assert payload["sourcePointer"] == "msea-r28-t5:source-pointer-001"
    assert payload["downstreamRelease"] == DOWNSTREAM_RELEASE_HELD
    assert payload["outputContentRead"] is False
    assert payload["memoryWriteAuthorized"] is False
    assert payload["memoryWriteDisposition"] == "MEMORY_WRITE_NOT_AUTHORIZED_BY_T9_DISPATCH"
    assert "outputFileNames" not in payload
    assert "extractedText" not in payload
    assert "rawOcrText" not in payload
    assert "documentBody" not in payload
    assert "memoryRecordBody" not in payload
    assert "vectorContent" not in payload


def test_memory_safe_candidate_contract_changes_with_source_pointer_metadata() -> None:
    first = build_mineru_memory_safe_candidate_contract(
        _receipt(source_pointer="msea-r28-t5:source-pointer-001")
    )
    second = build_mineru_memory_safe_candidate_contract(
        _receipt(source_pointer="msea-r28-t5:source-pointer-002")
    )

    assert first.candidate_id != second.candidate_id


@pytest.mark.parametrize(
    ("receipt", "token"),
    [
        (
            MineruMetadataReceipt(
                receipt_id="msea-r28-t9:receipt-content-read",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                output_file_names=("layout.pdf",),
                quality_report_ref="msea-r28-t5:quality-report-004",
                source_pointer="msea-r28-t5:source-pointer-004",
                output_content_read=True,
            ),
            "OUTPUT_CONTENT_READ_FORBIDDEN",
        ),
        (
            MineruMetadataReceipt(
                receipt_id="msea-r28-t9:receipt-unsafe-ref",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                output_file_names=("layout.pdf",),
                quality_report_ref="raw:quality-notes",
                source_pointer="msea-r28-t5:source-pointer-005",
            ),
            "QUALITY_OR_SOURCE_POINTER_MISSING",
        ),
        (
            MineruMetadataReceipt(
                receipt_id="msea-r28-t9:receipt-released",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                output_file_names=("layout.pdf",),
                quality_report_ref="msea-r28-t5:quality-report-006",
                source_pointer="msea-r28-t5:source-pointer-006",
                downstream_release="MEMORY_WRITE_READY",
            ),
            "DOWNSTREAM_RELEASE_NOT_HELD",
        ),
    ],
)
def test_memory_safe_candidate_contract_fails_closed_for_unsafe_receipts(
    receipt: MineruMetadataReceipt,
    token: str,
) -> None:
    with pytest.raises(MineruMetadataReceiptValidationError) as exc_info:
        build_mineru_memory_safe_candidate_contract(receipt)

    assert exc_info.value.token == token


def test_memory_owner_admission_readout_is_deterministic_and_metadata_only() -> None:
    contract = build_mineru_memory_safe_candidate_contract(_receipt())
    readout = build_mineru_memory_owner_admission_readout(contract)
    repeated = build_mineru_memory_owner_admission_readout(contract)
    payload = mineru_memory_owner_admission_readout_payload(readout)

    assert readout == repeated
    assert payload == mineru_memory_owner_admission_readout_payload(repeated)
    assert payload["readoutVersion"] == "cvf.mineruMemoryOwnerAdmission.r28t12.v1"
    assert payload["admissionDisposition"] == "MEMORY_OWNER_ADMISSION_READY_FOR_REVIEW"
    assert payload["candidateId"] == contract.candidate_id
    assert payload["receiptId"] == "msea-r28-t1:receipt-001"
    assert payload["qualityReportRef"] == "msea-r28-t5:quality-report-001"
    assert payload["sourcePointer"] == "msea-r28-t5:source-pointer-001"
    assert payload["downstreamRelease"] == DOWNSTREAM_RELEASE_HELD
    assert payload["outputContentRead"] is False
    assert payload["memoryWriteAuthorized"] is False
    assert payload["memoryWriteDisposition"] == MEMORY_WRITE_NOT_AUTHORIZED_BY_T12
    assert payload["futureAuthorityRequired"] == "FUTURE_MEMORY_WRITE_WORK_ORDER_REQUIRED"
    assert "outputFileNames" not in payload
    assert "extractedText" not in payload
    assert "rawOcrText" not in payload
    assert "documentBody" not in payload
    assert "memoryRecordBody" not in payload
    assert "vectorContent" not in payload


def test_memory_owner_admission_readout_changes_with_candidate_metadata() -> None:
    first = build_mineru_memory_owner_admission_readout(
        build_mineru_memory_safe_candidate_contract(
            _receipt(source_pointer="msea-r28-t5:source-pointer-001")
        )
    )
    second = build_mineru_memory_owner_admission_readout(
        build_mineru_memory_safe_candidate_contract(
            _receipt(source_pointer="msea-r28-t5:source-pointer-002")
        )
    )

    assert first.candidate_id != second.candidate_id


@pytest.mark.parametrize(
    ("contract", "token"),
    [
        (
            MineruMemorySafeCandidateContract(
                candidate_id="memory-safe-candidate:content-read",
                receipt_id="msea-r28-t12:receipt-content-read",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                quality_report_ref="msea-r28-t5:quality-report-007",
                source_pointer="msea-r28-t5:source-pointer-007",
                output_content_read=True,
            ),
            "OUTPUT_CONTENT_READ_FORBIDDEN",
        ),
        (
            MineruMemorySafeCandidateContract(
                candidate_id="memory-safe-candidate:write-ready",
                receipt_id="msea-r28-t12:receipt-write-ready",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                quality_report_ref="msea-r28-t5:quality-report-008",
                source_pointer="msea-r28-t5:source-pointer-008",
                memory_write_authorized=True,
            ),
            "MEMORY_WRITE_ALREADY_AUTHORIZED",
        ),
        (
            MineruMemorySafeCandidateContract(
                candidate_id="memory-safe-candidate:released",
                receipt_id="msea-r28-t12:receipt-released",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                quality_report_ref="msea-r28-t5:quality-report-009",
                source_pointer="msea-r28-t5:source-pointer-009",
                downstream_release="MEMORY_WRITE_READY",
            ),
            "DOWNSTREAM_RELEASE_NOT_HELD",
        ),
        (
            MineruMemorySafeCandidateContract(
                candidate_id="memory-safe-candidate:unsafe-ref",
                receipt_id="msea-r28-t12:receipt-unsafe-ref",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                quality_report_ref="raw:quality-notes",
                source_pointer="msea-r28-t5:source-pointer-010",
            ),
            "QUALITY_OR_SOURCE_POINTER_MISSING",
        ),
        (
            MineruMemorySafeCandidateContract(
                candidate_id="memory-safe-candidate:no-boundary",
                receipt_id="msea-r28-t12:receipt-no-boundary",
                source_input_slot="private-input-slot",
                input_sha256=VALID_SHA,
                quality_report_ref="msea-r28-t5:quality-report-011",
                source_pointer="msea-r28-t5:source-pointer-011",
                claim_boundary="",
            ),
            "CLAIM_BOUNDARY_MISSING",
        ),
    ],
)
def test_memory_owner_admission_readout_fails_closed_for_unsafe_candidates(
    contract: MineruMemorySafeCandidateContract,
    token: str,
) -> None:
    with pytest.raises(MineruMetadataReceiptValidationError) as exc_info:
        build_mineru_memory_owner_admission_readout(contract)

    assert exc_info.value.token == token
