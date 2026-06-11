"""
CVF Extraction Foundation - EX-T3 through EX-T5 local pipeline.

Claim boundary: deterministic local extraction pipeline contracts only. This
module does not install OCR dependencies, download OCR models, mutate corpus
records, call providers, or perform legal/current-status evaluation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from statistics import mean
from typing import Callable, Literal

from tier1_extractor import MIN_CHARS_PER_PAGE, Tier1ExtractorResult, Tier1PageResult

OCR_CONFIDENCE_THRESHOLD: float = 0.75
PAGE_COVERAGE_THRESHOLD: float = 0.80
DEFAULT_CHUNK_MAX_CHARS: int = 512

OcrEngineName = Literal["easyocr", "tesseract"]
ExtractionTier = Literal["TIER1_DIGITAL", "TIER2_OCR"]
ExtractionStatus = Literal[
    "PASS",
    "NEEDS_TIER2_OCR",
    "OCR_LOW_CONFIDENCE",
    "PARTIAL_EXTRACTION",
    "EMPTY",
]

_EASYOCR_LANGUAGE_MAP = {"en": "en", "vi": "vi"}
_TESSERACT_LANGUAGE_MAP = {"en": "eng", "vi": "vie"}


class UnsupportedOcrLanguageError(ValueError):
    """Raised when a profile language lacks a governed OCR mapping."""


class OcrDependencyUnavailableError(RuntimeError):
    """Raised when OCR execution is requested without an OCR engine adapter."""


@dataclass(frozen=True)
class OcrLanguageMapping:
    """Extractor-native language codes derived from DSCP profile language codes."""

    engine: OcrEngineName
    profile_language_codes: list[str]
    ocr_language_codes: list[str]
    joined_code: str


@dataclass(frozen=True)
class Tier2OcrPageInput:
    """A rendered page handle supplied by a caller-owned renderer."""

    page_num: int
    image_ref: str


@dataclass(frozen=True)
class Tier2OcrPageResult:
    """Per-page OCR output with confidence captured by the OCR adapter."""

    page_num: int
    text: str
    char_count: int
    confidence: float
    extraction_method: str


@dataclass(frozen=True)
class Tier2OcrExtractorInput:
    """Tier 2 OCR request using a caller-supplied OCR adapter."""

    pages: list[Tier2OcrPageInput]
    language_codes: list[str]
    engine: OcrEngineName = "easyocr"


@dataclass(frozen=True)
class Tier2OcrExtractorResult:
    """Tier 2 OCR result with confidence and language mapping evidence."""

    status: str
    pages: list[Tier2OcrPageResult]
    total_char_count: int
    avg_chars_per_page: float
    mean_confidence: float | None
    below_min_chars_flag: bool
    language_codes: list[str]
    ocr_language_codes: list[str]
    extraction_method: str


@dataclass(frozen=True)
class ExtractionQualityReport:
    """Tier 3 quality gate result for an extraction output."""

    status: ExtractionStatus
    quality_flags: list[ExtractionStatus]
    page_count: int
    pages_with_output: int
    page_coverage_ratio: float
    total_char_count: int
    avg_chars_per_page: float
    mean_ocr_confidence: float | None
    thresholds: dict[str, float]


@dataclass(frozen=True)
class ExtractionChunk:
    """Governed chunk schema produced after extraction quality evaluation."""

    chunk_id: str
    source_artifact_id: str
    source_hash: str
    page_start: int
    page_end: int
    text: str
    char_count: int
    extraction_tier: ExtractionTier
    extraction_method: str
    quality_flags: list[ExtractionStatus]
    language_codes: list[str]
    extraction_status: ExtractionStatus
    provenance: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class ExtractionDscpDescriptorInput:
    """Python-side descriptor shape handed to the DSCP profile/descriptor layer."""

    artifact_id: str
    source_hash: str
    artifact_role: str
    content_class: str
    governance_gates: dict[str, object]
    metadata: dict[str, str]


def map_ocr_language_codes(
    language_codes: list[str],
    engine: OcrEngineName = "easyocr",
) -> OcrLanguageMapping:
    """Map DSCP profile language codes to extractor-native OCR language codes."""

    mapping = _EASYOCR_LANGUAGE_MAP if engine == "easyocr" else _TESSERACT_LANGUAGE_MAP
    ocr_codes: list[str] = []
    for code in language_codes:
        try:
            ocr_codes.append(mapping[code])
        except KeyError as exc:
            raise UnsupportedOcrLanguageError(
                f"No governed {engine} OCR mapping for profile language code '{code}'"
            ) from exc

    joiner = "," if engine == "easyocr" else "+"
    return OcrLanguageMapping(
        engine=engine,
        profile_language_codes=list(language_codes),
        ocr_language_codes=ocr_codes,
        joined_code=joiner.join(ocr_codes),
    )


def extract_tier2_ocr(
    input: Tier2OcrExtractorInput,
    ocr_engine: Callable[[Tier2OcrPageInput, OcrLanguageMapping], tuple[str, float]] | None,
) -> Tier2OcrExtractorResult:
    """
    Execute Tier 2 through a caller-supplied OCR adapter.

    The adapter boundary is explicit so this module can be tested without
    installing OCR libraries or downloading models. Passing None is a hard stop.
    """

    if ocr_engine is None:
        raise OcrDependencyUnavailableError(
            "Tier 2 OCR requires a caller-supplied OCR adapter; no OCR model is bundled."
        )

    language_mapping = map_ocr_language_codes(input.language_codes, input.engine)
    page_results: list[Tier2OcrPageResult] = []
    for page in input.pages:
        text, confidence = ocr_engine(page, language_mapping)
        page_results.append(
            Tier2OcrPageResult(
                page_num=page.page_num,
                text=text,
                char_count=len(text),
                confidence=confidence,
                extraction_method=f"{input.engine}-adapter",
            )
        )

    total = sum(page.char_count for page in page_results)
    page_count = len(page_results)
    avg = total / page_count if page_count else 0.0
    confidences = [page.confidence for page in page_results]
    mean_conf = mean(confidences) if confidences else None
    return Tier2OcrExtractorResult(
        status="EMPTY" if total == 0 else "OK",
        pages=page_results,
        total_char_count=total,
        avg_chars_per_page=avg,
        mean_confidence=mean_conf,
        below_min_chars_flag=avg < MIN_CHARS_PER_PAGE,
        language_codes=list(input.language_codes),
        ocr_language_codes=language_mapping.ocr_language_codes,
        extraction_method=f"{input.engine}-adapter",
    )


def evaluate_extraction_quality(
    pages: list[Tier1PageResult] | list[Tier2OcrPageResult],
    mean_ocr_confidence: float | None = None,
) -> ExtractionQualityReport:
    """Evaluate EX-T4 quality gates over extracted page results."""

    page_count = len(pages)
    pages_with_output = sum(1 for page in pages if page.char_count > 0)
    total = sum(page.char_count for page in pages)
    coverage = pages_with_output / page_count if page_count else 0.0
    avg = total / page_count if page_count else 0.0

    flags: list[ExtractionStatus] = []
    if total == 0:
        flags.append("EMPTY")
    if avg < MIN_CHARS_PER_PAGE:
        flags.append("NEEDS_TIER2_OCR")
    if coverage < PAGE_COVERAGE_THRESHOLD:
        flags.append("PARTIAL_EXTRACTION")
    if mean_ocr_confidence is not None and mean_ocr_confidence < OCR_CONFIDENCE_THRESHOLD:
        flags.append("OCR_LOW_CONFIDENCE")

    return ExtractionQualityReport(
        status="PASS" if not flags else flags[0],
        quality_flags=flags,
        page_count=page_count,
        pages_with_output=pages_with_output,
        page_coverage_ratio=coverage,
        total_char_count=total,
        avg_chars_per_page=avg,
        mean_ocr_confidence=mean_ocr_confidence,
        thresholds={
            "MIN_CHARS_PER_PAGE": float(MIN_CHARS_PER_PAGE),
            "OCR_CONFIDENCE": OCR_CONFIDENCE_THRESHOLD,
            "PAGE_COVERAGE": PAGE_COVERAGE_THRESHOLD,
        },
    )


def chunk_extracted_pages(
    *,
    source_artifact_id: str,
    source_hash: str,
    pages: list[Tier1PageResult] | list[Tier2OcrPageResult],
    extraction_tier: ExtractionTier,
    language_codes: list[str],
    quality_report: ExtractionQualityReport,
    max_chars: int = DEFAULT_CHUNK_MAX_CHARS,
) -> list[ExtractionChunk]:
    """Create fixed-window governed chunks without language inference."""

    chunks: list[ExtractionChunk] = []
    for page in pages:
        text = page.text
        if not text:
            continue
        for offset in range(0, len(text), max_chars):
            chunk_text = text[offset : offset + max_chars]
            seed = f"{source_artifact_id}:{page.page_num}:{offset}:{sha256(chunk_text.encode('utf-8')).hexdigest()}"
            chunk_id = f"chunk-{sha256(seed.encode('utf-8')).hexdigest()[:16]}"
            chunks.append(
                ExtractionChunk(
                    chunk_id=chunk_id,
                    source_artifact_id=source_artifact_id,
                    source_hash=source_hash,
                    page_start=page.page_num,
                    page_end=page.page_num,
                    text=chunk_text,
                    char_count=len(chunk_text),
                    extraction_tier=extraction_tier,
                    extraction_method=page.extraction_method,
                    quality_flags=list(quality_report.quality_flags),
                    language_codes=list(language_codes),
                    extraction_status=quality_report.status,
                    provenance={
                        "chunkingStrategy": "fixed-window-chars",
                        "maxChars": str(max_chars),
                    },
                )
            )
    return chunks


def build_extraction_dscp_descriptor_inputs(
    chunks: list[ExtractionChunk],
    *,
    domain_family: str,
    domain_profile_id: str,
) -> list[ExtractionDscpDescriptorInput]:
    """
    Build descriptor-shaped records for downstream DSCP profile application.

    This function prepares the handoff surface only; it does not apply a domain
    profile, build a receipt, call a provider, or release raw content.
    """

    descriptors: list[ExtractionDscpDescriptorInput] = []
    for chunk in chunks:
        descriptors.append(
            ExtractionDscpDescriptorInput(
                artifact_id=chunk.chunk_id,
                source_hash=chunk.source_hash,
                artifact_role="corpus_candidate",
                content_class="extracted_chunk",
                governance_gates={
                    "freshnessGate": "UNKNOWN",
                    "classificationGate": "CONDITIONAL",
                    "eligibilityGate": (
                        "CONDITIONAL" if chunk.extraction_status == "PASS" else "NO"
                    ),
                    "customGates": {
                        "extractionStatus": chunk.extraction_status,
                    },
                },
                metadata={
                    "sourceArtifactId": chunk.source_artifact_id,
                    "domainFamily": domain_family,
                    "domainProfileId": domain_profile_id,
                    "languageCodes": ",".join(chunk.language_codes),
                    "extractionTier": chunk.extraction_tier,
                    "extractionMethod": chunk.extraction_method,
                    "qualityFlags": ",".join(chunk.quality_flags),
                    "pageStart": str(chunk.page_start),
                    "pageEnd": str(chunk.page_end),
                    "rawContentReleased": "false",
                },
            )
        )
    return descriptors
