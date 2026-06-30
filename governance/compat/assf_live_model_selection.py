"""ASSF live-provider free-quota model selection helpers."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


AUTO_FREE_QUOTA_MODEL = "AUTO_FROM_ALIBABA_FREE_QUOTA_LEDGER"


@dataclass(frozen=True)
class ModelSelection:
    requested_model: str
    resolved_model: str | None
    status: str
    ledger_path: Path
    expiration_date: str | None = None
    free_quota_remaining: int | None = None
    diagnostic_rerun_result: str | None = None
    reason: str | None = None

    def to_dict(self, *, relative_to: Path | None = None) -> dict[str, Any]:
        ledger_path = self.ledger_path
        if relative_to is not None:
            try:
                ledger_path_text = ledger_path.relative_to(relative_to).as_posix()
            except ValueError:
                ledger_path_text = ledger_path.as_posix()
        else:
            ledger_path_text = ledger_path.as_posix()
        return {
            "requestedModel": self.requested_model,
            "resolvedModel": self.resolved_model,
            "status": self.status,
            "ledgerPath": ledger_path_text,
            "expirationDate": self.expiration_date,
            "freeQuotaRemaining": self.free_quota_remaining,
            "diagnosticRerunResult": self.diagnostic_rerun_result,
            "reason": self.reason,
        }


def _parse_ledger_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _ledger_entry_model_id(entry: dict[str, Any]) -> str | None:
    model_id = entry.get("modelCode") or entry.get("modelId")
    return model_id if isinstance(model_id, str) and model_id.strip() else None


def _diagnostic_result(entry: dict[str, Any]) -> str | None:
    rerun = entry.get("diagnosticRerun")
    if isinstance(rerun, dict):
        result = rerun.get("result")
        return str(result) if result else None
    result = entry.get("diagnosticRerunResult")
    return str(result) if result else None


def _load_free_quota_models(ledger_path: Path) -> list[dict[str, Any]]:
    data = json.loads(ledger_path.read_text(encoding="utf-8"))
    models = data.get("models") if isinstance(data, dict) else None
    if not isinstance(models, list):
        raise ValueError("Alibaba free-quota ledger missing models array")
    return [entry for entry in models if isinstance(entry, dict)]


def _entry_to_selection(
    *,
    requested_model: str,
    entry: dict[str, Any],
    ledger_path: Path,
    status: str,
    reason: str | None = None,
) -> ModelSelection:
    model_id = _ledger_entry_model_id(entry)
    remaining = entry.get("freeQuotaRemaining")
    if remaining is None:
        remaining = entry.get("freeQuotaRemainingAtCapture")
    return ModelSelection(
        requested_model=requested_model,
        resolved_model=model_id,
        status=status,
        ledger_path=ledger_path,
        expiration_date=str(entry.get("expirationDate", "")) or None,
        free_quota_remaining=remaining if isinstance(remaining, int) else None,
        diagnostic_rerun_result=_diagnostic_result(entry),
        reason=reason,
    )


def resolve_free_quota_model(
    *,
    requested_model: str,
    ledger_path: Path,
    today: date | None = None,
) -> ModelSelection:
    now = today or date.today()
    models = _load_free_quota_models(ledger_path)
    by_model = {
        model_id: entry
        for entry in models
        if (model_id := _ledger_entry_model_id(entry)) is not None
    }

    def is_usable(entry: dict[str, Any]) -> bool:
        expiration = entry.get("expirationDate")
        if not isinstance(expiration, str):
            return False
        parsed = _parse_ledger_date(expiration)
        return parsed is not None and now <= parsed

    if requested_model != AUTO_FREE_QUOTA_MODEL:
        entry = by_model.get(requested_model)
        if entry is None:
            return ModelSelection(
                requested_model=requested_model,
                resolved_model=None,
                status="MODEL_FREE_QUOTA_NOT_VERIFIED",
                ledger_path=ledger_path,
                reason="model is absent from the Alibaba free-quota ledger models array",
            )
        if not is_usable(entry):
            return _entry_to_selection(
                requested_model=requested_model,
                entry=entry,
                ledger_path=ledger_path,
                status="MODEL_FREE_QUOTA_EXPIRED",
                reason="model expiration date is before the current run date",
            )
        return _entry_to_selection(
            requested_model=requested_model,
            entry=entry,
            ledger_path=ledger_path,
            status="MODEL_FREE_QUOTA_USABLE",
        )

    candidates = [entry for entry in models if is_usable(entry)]
    if not candidates:
        return ModelSelection(
            requested_model=requested_model,
            resolved_model=None,
            status="NO_USABLE_FREE_QUOTA_MODEL",
            ledger_path=ledger_path,
            reason="no unexpired models were found in the Alibaba free-quota ledger",
        )

    def sort_key(entry: dict[str, Any]) -> tuple[int, date, int, str]:
        expiration = _parse_ledger_date(str(entry.get("expirationDate", "")))
        remaining = entry.get("freeQuotaRemaining")
        if remaining is None:
            remaining = entry.get("freeQuotaRemainingAtCapture")
        diagnostic_pass = 1 if _diagnostic_result(entry) == "PASS" else 0
        return (
            diagnostic_pass,
            expiration or date.min,
            remaining if isinstance(remaining, int) else 0,
            _ledger_entry_model_id(entry) or "",
        )

    selected = max(candidates, key=sort_key)
    return _entry_to_selection(
        requested_model=requested_model,
        entry=selected,
        ledger_path=ledger_path,
        status="MODEL_FREE_QUOTA_USABLE",
        reason="auto-selected from unexpired Alibaba free-quota ledger entries",
    )
