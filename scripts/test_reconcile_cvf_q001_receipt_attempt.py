"""Fail-closed unknown-outcome reconciliation tests for Q001."""

import hashlib
import json
import sqlite3
import subprocess
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
    def test_migrate_backup_restore_and_cli_reconcile_same_attempt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, target, backup, restored = [root / name for name in ('source.json', 'target.sqlite', 'backup.sqlite', 'restored.sqlite')]
            first = block('GENESIS', 'artifact-proof-one', '2026-10-06T00:00:00')
            first['event']['private_note'] = 'do-not-print-this-user-content'
            first['hash'] = reconciler._block_hash(first)
            source.write_text(json.dumps([first]), encoding='utf-8')
            original = source.read_bytes()
            reconciler.reconcile(target, 'artifact-proof-one')  # Load the existing owner only.
            from ledger_layer.sqlite_ledger import SqliteLedger
            SqliteLedger.import_json(source, target)
            SqliteLedger(target).backup_to(backup)
            SqliteLedger.restore_backup(backup, restored)
            self.assertEqual(source.read_bytes(), original)
            for path in (target, backup, restored):
                process = subprocess.run([sys.executable, str(Path(reconciler.__file__)), '--ledger', str(path), '--attempt-id', 'artifact-proof-one', '--json'], capture_output=True, text=True, timeout=15)
                self.assertEqual(process.returncode, 0, process.stderr)
                result = json.loads(process.stdout)
                self.assertEqual(result['blockHash'], first['hash'])
                self.assertFalse(result['safeToRetry'])
                self.assertNotIn('do-not-print-this-user-content', process.stdout + process.stderr)
            missing = subprocess.run([sys.executable, str(Path(reconciler.__file__)), '--ledger', str(restored), '--attempt-id', 'artifact-proof-absent', '--json'], capture_output=True, text=True, timeout=15)
            self.assertEqual(missing.returncode, 2)
            self.assertFalse(json.loads(missing.stdout)['safeToRetry'])

    def sqlite_fixture(self, path, chain):
        conn = sqlite3.connect(path)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA user_version=1")
        conn.execute("CREATE TABLE blocks (ordinal INTEGER PRIMARY KEY, request_id TEXT NOT NULL UNIQUE, block_json TEXT NOT NULL, block_hash TEXT NOT NULL)")
        for ordinal, item in enumerate(chain, 1):
            conn.execute("INSERT INTO blocks VALUES (?,?,?,?)", (ordinal, item['event']['request_id'], json.dumps(item), item['hash']))
        conn.commit()
        return conn

    def test_sqlite_reads_committed_wal_and_never_grants_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'ledger.sqlite'
            first = block('GENESIS', 'artifact-proof-one', '2026-10-06T00:00:00')
            conn = self.sqlite_fixture(path, [first])
            try:
                before = path.read_bytes()
                found = reconciler.reconcile(path, 'artifact-proof-one')
                self.assertEqual(found['status'], 'FOUND_ONE')
                self.assertEqual(found['blockHash'], first['hash'])
                self.assertIsNone(found['ledgerSha256'])
                self.assertFalse(found['safeToRetry'])
                self.assertFalse(found['authoritative'])
                self.assertEqual(path.read_bytes(), before)
                self.assertEqual(reconciler.reconcile(path, 'artifact-proof-absent')['status'], 'NOT_FOUND_IN_SNAPSHOT')
                conn.execute('BEGIN IMMEDIATE')
                second = block(first['hash'], 'artifact-proof-two', '2026-10-06T00:00:01')
                conn.execute('INSERT INTO blocks VALUES (?,?,?,?)', (2, second['event']['request_id'], json.dumps(second), second['hash']))
                self.assertEqual(reconciler.reconcile(path, 'artifact-proof-two')['status'], 'NOT_FOUND_IN_SNAPSHOT')
                conn.commit()
                self.assertEqual(reconciler.reconcile(path, 'artifact-proof-two')['status'], 'FOUND_ONE')
            finally:
                conn.close()

    def test_sqlite_missing_corrupt_and_incompatible_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'ledger.sqlite'
            self.assertEqual(reconciler.reconcile(path, 'artifact-proof-one')['status'], 'INVALID_SNAPSHOT')
            self.assertFalse(path.exists())
            path.write_bytes(b'corrupt')
            self.assertEqual(reconciler.reconcile(path, 'artifact-proof-one')['status'], 'INVALID_SNAPSHOT')
            path.unlink()
            first = block('GENESIS', 'artifact-proof-one', '2026-10-06T00:00:00')
            conn = self.sqlite_fixture(path, [first])
            try:
                for mutation in ["PRAGMA user_version=2", "PRAGMA user_version=1", "UPDATE blocks SET request_id='artifact-proof-changed'"]:
                    conn.execute(mutation); conn.commit()
                    expected = 'FOUND_ONE' if mutation == 'PRAGMA user_version=1' else 'INVALID_SNAPSHOT'
                    self.assertEqual(reconciler.reconcile(path, 'artifact-proof-one')['status'], expected)
            finally:
                conn.close()

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
