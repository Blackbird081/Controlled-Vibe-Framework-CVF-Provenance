"""Fail-closed unknown-outcome reconciliation tests for Q001."""

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reconcile_cvf_q001_receipt_attempt as reconciler


def block(previous: str, request_id: str, timestamp: str) -> dict:
    value = {
        "timestamp": timestamp,
        "previous_hash": previous,
        "event": {"request_id": request_id, "decision": {"final_decision": "ALLOW"}},
    }
    value["hash"] = hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()
    return value


class ReconcileTests(unittest.TestCase):
    def test_found_missing_and_duplicate_never_authorize_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            first = block("GENESIS", "artifact-proof-one", "2026-09-29T00:00:00")
            path.write_text(json.dumps([first]), encoding="utf-8")
            found = reconciler.reconcile(path, "artifact-proof-one")
            self.assertEqual(found["status"], "FOUND_ONE")
            self.assertEqual(found["decision"], "ALLOW")
            self.assertFalse(found["safeToRetry"])
            absent = reconciler.reconcile(path, "artifact-proof-other")
            self.assertEqual(absent["status"], "NOT_FOUND_IN_SNAPSHOT")
            self.assertFalse(absent["safeToRetry"])
            second = block(first["hash"], "artifact-proof-one", "2026-09-29T00:00:01")
            path.write_text(json.dumps([first, second]), encoding="utf-8")
            duplicated = reconciler.reconcile(path, "artifact-proof-one")
            self.assertEqual(duplicated["status"], "DUPLICATE_OR_CONFLICT")
            self.assertFalse(duplicated["safeToRetry"])

    def test_invalid_or_unreadable_snapshot_cannot_be_treated_as_absent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            self.assertEqual(reconciler.reconcile(path, "artifact-proof-one")["status"], "INVALID_SNAPSHOT")
            valid = block("GENESIS", "artifact-proof-one", "2026-09-29T00:00:00")
            valid["event"]["decision"]["final_decision"] = "DENY"
            path.write_text(json.dumps([valid]), encoding="utf-8")
            invalid = reconciler.reconcile(path, "artifact-proof-one")
            self.assertEqual(invalid["status"], "INVALID_SNAPSHOT")
            self.assertFalse(invalid["safeToRetry"])
            malformed = block("GENESIS", "artifact-proof-one", "2026-09-29T00:00:00")
            malformed["event"]["decision"] = None
            malformed["hash"] = hashlib.sha256(json.dumps({key: malformed[key] for key in (
                "timestamp", "previous_hash", "event"
            )}, sort_keys=True).encode()).hexdigest()
            path.write_text(json.dumps([malformed]), encoding="utf-8")
            self.assertEqual(reconciler.reconcile(path, "artifact-proof-one")["status"], "INVALID_SNAPSHOT")


if __name__ == "__main__":
    unittest.main()
