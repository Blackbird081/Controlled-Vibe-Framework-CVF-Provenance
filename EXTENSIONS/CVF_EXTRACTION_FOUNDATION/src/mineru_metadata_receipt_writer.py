"""Metadata-only MinerU receipt writer for CVF Extraction Foundation.

This helper accepts caller-supplied metadata and renders a stable receipt
payload. It does not read source documents, generated MinerU output content,
or execute MinerU.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from json import dumps
import re
from typing import Literal, Sequence


RECEIPT_VERSION = "cvf.mineruMetadataReceipt.r28t5.v2"
PRIVATE_OUTPUT_DISPOSITION = "RECEIPT_METADATA_ALLOWED"
DOWNSTREAM_RELEASE_HELD = "HELD_PENDING_RECEIPT_CHECKER_AND_MEMORY_ROUTE"
CLAIM_BOUNDARY = (
    "This receipt records caller-supplied MinerU metadata only. It does not "
    "prove extraction accuracy, document truth, legal quality, current-law "
    "correctness, runtime readiness, memory ingestion readiness, RAG readiness, "
    "or production workflow readiness."
)

ALLOWED_OUTPUT_FILE_NAMES = frozenset(
    {
        "layout.pdf",
        "span.pdf",
        "model.json",
        "middle.json",
        "content_list.json",
        "content_list_v2.json",
    }
)

MineruPrivateOutputClass = Literal[
    "PRIVATE_INPUT_ONLY",
    "PRIVATE_RUNTIME_COPY",
    "PRIVATE_GENERATED_OUTPUT",
]

FailureToken = Literal[
    "INVALID_RECEIPT_ID",
    "INVALID_SOURCE_INPUT_SLOT",
    "INVALID_INPUT_SHA256",
    "INVALID_OUTPUT_FILE_NAME",
    "OUTPUT_CONTENT_READ_FORBIDDEN",
    "QUALITY_OR_SOURCE_POINTER_MISSING",
]

_SAFE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_SAFE_MARKDOWN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\.md$")
_SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
_BOUNDARY_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_UNSAFE_TEXT_MARKERS = ("raw:", "text:", "ocr:", "content:")


class MineruMetadataReceiptValidationError(ValueError):
    """Fail-closed validation error with a stable R28-T1 token."""

    def __init__(self, token: FailureToken, message: str) -> None:
        super().__init__(message)
        self.token = token


@dataclass(frozen=True)
class MineruMetadataReceipt:
    """A metadata-only receipt for a private MinerU extraction output set."""

    receipt_id: str
    source_input_slot: str
    input_sha256: str
    output_file_names: tuple[str, ...]
    quality_report_ref: str
    source_pointer: str
    private_output_class: MineruPrivateOutputClass = "PRIVATE_GENERATED_OUTPUT"
    private_output_disposition: str = PRIVATE_OUTPUT_DISPOSITION
    output_content_read: bool = False
    downstream_release: str = DOWNSTREAM_RELEASE_HELD
    receipt_version: str = RECEIPT_VERSION
    claim_boundary: str = CLAIM_BOUNDARY


@dataclass(frozen=True)
class MineruQualityReportSourcePointer:
    """Metadata-only references produced from caller-owned quality evidence."""

    quality_report_ref: str
    source_pointer: str


def _fail(token: FailureToken, message: str) -> None:
    raise MineruMetadataReceiptValidationError(token, message)


def _validate_safe_id(value: str, *, field_name: str, token: FailureToken) -> None:
    if not _SAFE_ID_RE.fullmatch(value):
        _fail(token, f"{field_name} must be a bounded metadata identifier")
    lowered = value.casefold()
    if any(marker in lowered for marker in _UNSAFE_TEXT_MARKERS):
        _fail(token, f"{field_name} must not contain raw-content markers")


def _validate_output_file_name(name: str) -> None:
    if "/" in name or "\\" in name or name in {"", ".", ".."}:
        _fail("INVALID_OUTPUT_FILE_NAME", "output file names must be basenames")
    if name != name.strip() or "\n" in name or "\r" in name:
        _fail("INVALID_OUTPUT_FILE_NAME", "output file names must be stable strings")
    lowered = name.casefold()
    if any(marker in lowered for marker in _UNSAFE_TEXT_MARKERS):
        _fail(
            "INVALID_OUTPUT_FILE_NAME",
            "output file names must not encode output content",
        )
    if lowered in ALLOWED_OUTPUT_FILE_NAMES or _SAFE_MARKDOWN_RE.fullmatch(name):
        return
    _fail(
        "INVALID_OUTPUT_FILE_NAME",
        "output file name is not an allowed MinerU metadata family",
    )


def _validate_quality_source_pointer(quality_report_ref: str, source_pointer: str) -> None:
    for field_name, value in (
        ("quality_report_ref", quality_report_ref),
        ("source_pointer", source_pointer),
    ):
        if not _SAFE_ID_RE.fullmatch(value):
            _fail(
                "QUALITY_OR_SOURCE_POINTER_MISSING",
                f"{field_name} must be a bounded metadata identifier",
            )
        lowered = value.casefold()
        if any(marker in lowered for marker in _UNSAFE_TEXT_MARKERS):
            _fail(
                "QUALITY_OR_SOURCE_POINTER_MISSING",
                f"{field_name} must not contain raw-content markers",
            )


def build_mineru_quality_report_source_pointer(
    *,
    receipt_id: str,
    source_input_slot: str,
    input_sha256: str,
    quality_report_status: str,
    boundary_sha256: str,
    chunk_count: int,
) -> MineruQualityReportSourcePointer:
    """Build deterministic metadata refs without reading extraction content."""

    _validate_safe_id(
        receipt_id,
        field_name="receipt_id",
        token="INVALID_RECEIPT_ID",
    )
    _validate_safe_id(
        source_input_slot,
        field_name="source_input_slot",
        token="INVALID_SOURCE_INPUT_SLOT",
    )
    _validate_safe_id(
        quality_report_status,
        field_name="quality_report_status",
        token="QUALITY_OR_SOURCE_POINTER_MISSING",
    )
    if not _SHA256_RE.fullmatch(input_sha256):
        _fail("INVALID_INPUT_SHA256", "input_sha256 must be sha256:<64 lowercase hex>")
    if not _BOUNDARY_SHA256_RE.fullmatch(boundary_sha256):
        _fail(
            "QUALITY_OR_SOURCE_POINTER_MISSING",
            "boundary_sha256 must be a lowercase 64-character metadata digest",
        )
    if chunk_count < 0:
        _fail(
            "QUALITY_OR_SOURCE_POINTER_MISSING",
            "chunk_count must be a non-negative metadata count",
        )

    seed = "|".join(
        (
            receipt_id,
            source_input_slot,
            input_sha256,
            quality_report_status,
            boundary_sha256,
            str(chunk_count),
        )
    )
    digest = sha256(seed.encode("utf-8")).hexdigest()[:24]
    refs = MineruQualityReportSourcePointer(
        quality_report_ref=f"quality-report:{digest}",
        source_pointer=f"source-pointer:{digest}",
    )
    _validate_quality_source_pointer(refs.quality_report_ref, refs.source_pointer)
    return refs


def build_mineru_metadata_receipt(
    *,
    receipt_id: str,
    source_input_slot: str,
    input_sha256: str,
    output_file_names: Sequence[str],
    quality_report_ref: str,
    source_pointer: str,
    private_output_class: MineruPrivateOutputClass = "PRIVATE_GENERATED_OUTPUT",
    output_content_read: bool = False,
) -> MineruMetadataReceipt:
    """Build a validated metadata receipt without reading files or content."""

    _validate_safe_id(
        receipt_id,
        field_name="receipt_id",
        token="INVALID_RECEIPT_ID",
    )
    _validate_safe_id(
        source_input_slot,
        field_name="source_input_slot",
        token="INVALID_SOURCE_INPUT_SLOT",
    )
    if not _SHA256_RE.fullmatch(input_sha256):
        _fail("INVALID_INPUT_SHA256", "input_sha256 must be sha256:<64 lowercase hex>")
    if output_content_read is not False:
        _fail(
            "OUTPUT_CONTENT_READ_FORBIDDEN",
            "R28-T1 receipts must keep output_content_read false",
        )
    if not output_file_names:
        _fail(
            "INVALID_OUTPUT_FILE_NAME",
            "at least one MinerU output file name is required",
        )
    _validate_quality_source_pointer(quality_report_ref, source_pointer)

    normalized_names = tuple(output_file_names)
    for name in normalized_names:
        _validate_output_file_name(name)

    return MineruMetadataReceipt(
        receipt_id=receipt_id,
        source_input_slot=source_input_slot,
        input_sha256=input_sha256,
        output_file_names=normalized_names,
        quality_report_ref=quality_report_ref,
        source_pointer=source_pointer,
        private_output_class=private_output_class,
    )


def mineru_metadata_receipt_payload(
    receipt: MineruMetadataReceipt,
) -> dict[str, object]:
    """Return the stable camelCase receipt payload."""

    return {
        "claimBoundary": receipt.claim_boundary,
        "downstreamRelease": receipt.downstream_release,
        "inputSha256": receipt.input_sha256,
        "outputContentRead": receipt.output_content_read,
        "outputFileNames": list(receipt.output_file_names),
        "privateOutputClass": receipt.private_output_class,
        "privateOutputDisposition": receipt.private_output_disposition,
        "qualityReportRef": receipt.quality_report_ref,
        "receiptId": receipt.receipt_id,
        "receiptVersion": receipt.receipt_version,
        "sourceInputSlot": receipt.source_input_slot,
        "sourcePointer": receipt.source_pointer,
    }


def render_mineru_metadata_receipt_json(receipt: MineruMetadataReceipt) -> str:
    """Render deterministic JSON with a trailing newline."""

    return dumps(
        mineru_metadata_receipt_payload(receipt),
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"
