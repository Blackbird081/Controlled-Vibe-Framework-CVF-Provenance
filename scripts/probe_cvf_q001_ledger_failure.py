#!/usr/bin/env python3
"""Characterize current JSON ledger write failure on disposable local files only."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import threading
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parent.parent
ENGINE_ROOT = REPO_ROOT / "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core"
sys.path.insert(0, str(ENGINE_ROOT))

import ledger_layer.immutable_ledger as ledger_module  # noqa: E402
from ledger_layer.immutable_ledger import ImmutableLedger  # noqa: E402


def run_probe() -> dict:
    scratch_root = (REPO_ROOT / ".cvf/runtime").resolve()
    scratch_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="q001-ledger-failure-", dir=scratch_root) as directory:
        scratch = Path(directory).resolve()
        if not scratch.is_relative_to(scratch_root):
            raise RuntimeError("probe path escaped ignored runtime")

        ledger_path = scratch / "failure.json"
        ledger = ImmutableLedger(str(ledger_path))
        ledger.append_event({"request_id": "synthetic-seed", "decision": {"final_decision": "ALLOW"}})
        before = ledger_path.read_bytes()

        def fail_after_truncation(_value, file, **_kwargs):
            file.write("[")
            file.flush()
            raise OSError("synthetic failure after truncation")

        injected = False
        with patch.object(ledger_module.json, "dump", fail_after_truncation):
            try:
                ledger.append_event({"request_id": "synthetic-second"})
            except OSError:
                injected = True
        after = ledger_path.read_bytes()
        restart_rejected = False
        try:
            ImmutableLedger(str(ledger_path))
        except (ValueError, json.JSONDecodeError):
            restart_rejected = True

        reader_path = scratch / "reader.json"
        reader = ImmutableLedger(str(reader_path))
        reader.append_event({"request_id": "synthetic-reader-seed"})
        entered = threading.Event()
        release = threading.Event()
        worker_error: list[str] = []
        original_dump = ledger_module.json.dump

        def pause_after_truncation(value, file, **kwargs):
            entered.set()
            if not release.wait(5):
                raise TimeoutError("barrier safety timeout")
            return original_dump(value, file, **kwargs)

        def writer():
            try:
                reader.append_event({"request_id": "synthetic-reader-second"})
            except Exception as error:
                worker_error.append(type(error).__name__)

        with patch.object(ledger_module.json, "dump", pause_after_truncation):
            thread = threading.Thread(target=writer)
            thread.start()
            if not entered.wait(5):
                release.set()
                thread.join(5)
                raise RuntimeError("writer did not reach barrier")
            observed_during_append = reader_path.read_bytes()
            release.set()
            thread.join(5)
            if thread.is_alive():
                raise RuntimeError("writer did not complete after release")
        final_chain = json.loads(reader_path.read_text(encoding="utf-8"))

        return {
            "scope": "DISPOSABLE_LOCAL_COPY_ONLY",
            "injectedFailureObserved": injected,
            "beforeBytes": len(before),
            "afterBytes": len(after),
            "beforeSha256": hashlib.sha256(before).hexdigest(),
            "afterSha256": hashlib.sha256(after).hexdigest(),
            "priorCommittedBytesPreserved": before == after,
            "restartRejectedCorruptSnapshot": restart_rejected,
            "readerSawBytesDuringSuccessfulAppend": len(observed_during_append),
            "successfulAppendFinalBlocks": len(final_chain),
            "successfulAppendWorkerError": worker_error,
        }


if __name__ == "__main__":
    print(json.dumps(run_probe(), sort_keys=True))
