"""Explicit single-host SQLite ledger with transactional append and snapshot reads."""

import hashlib
import json
import os
import sqlite3
from pathlib import Path

from .block_builder import BlockBuilder
from .hash_engine import HashEngine


SCHEMA_VERSION = 1


def _request_id(event):
    if not isinstance(event, dict):
        raise ValueError("Ledger event must be an object")
    value = event.get("request_id")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Ledger event requires a nonempty request_id")
    return value


def _event_bytes(event):
    _request_id(event)
    return json.dumps(event, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _validate_chain(chain):
    if not isinstance(chain, list):
        raise ValueError("Ledger chain must be a block list")
    prior = "GENESIS"
    ids = set()
    for block in chain:
        if not isinstance(block, dict) or set(block) != {"timestamp", "previous_hash", "event", "hash"}:
            raise ValueError("Ledger block schema mismatch")
        if not isinstance(block["timestamp"], str) or not block["timestamp"]:
            raise ValueError("Ledger block timestamp invalid")
        request_id = _request_id(block["event"])
        _event_bytes(block["event"])
        if request_id in ids:
            raise ValueError("Duplicate request_id in ledger chain")
        ids.add(request_id)
        if block["previous_hash"] != prior:
            raise ValueError("Ledger predecessor mismatch")
        expected = HashEngine.generate_hash({key: block[key] for key in ("timestamp", "previous_hash", "event")})
        if block["hash"] != expected:
            raise ValueError("Ledger block hash mismatch")
        prior = expected
    return prior


class SqliteLedger:
    """One SQLite database per local ledger; no implicit JSON cutover."""

    def __init__(self, ledger_path, *, timeout=10.0):
        self.ledger_path = os.fspath(ledger_path)
        if Path(self.ledger_path).suffix.lower() != ".sqlite":
            raise ValueError("SQLite ledger requires an explicit .sqlite path")
        self.timeout = timeout
        self.builder = BlockBuilder()
        os.makedirs(os.path.dirname(os.path.abspath(self.ledger_path)), exist_ok=True)
        existed = os.path.exists(self.ledger_path)
        conn = self._connect()
        try:
            version = conn.execute("PRAGMA user_version").fetchone()[0]
            if version == 0:
                if existed or conn.execute("SELECT count(*) FROM sqlite_master WHERE type='table'").fetchone()[0]:
                    raise ValueError("Unversioned SQLite database is not a ledger")
                conn.execute("CREATE TABLE blocks (ordinal INTEGER PRIMARY KEY, request_id TEXT NOT NULL UNIQUE, block_json TEXT NOT NULL, block_hash TEXT NOT NULL)")
                conn.execute(f"PRAGMA user_version={SCHEMA_VERSION}")
            elif version != SCHEMA_VERSION:
                raise ValueError("Unsupported SQLite ledger schema version")
            self._check_schema(conn)
            conn.commit()
        finally:
            conn.close()
        self.read_chain()

    def _connect(self):
        conn = sqlite3.connect(self.ledger_path, timeout=self.timeout)
        try:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA synchronous=FULL")
            return conn
        except BaseException:
            conn.close()
            raise

    @staticmethod
    def _check_schema(conn):
        if conn.execute("PRAGMA user_version").fetchone()[0] != SCHEMA_VERSION:
            raise ValueError("SQLite ledger schema version mismatch")
        columns = conn.execute("PRAGMA table_xinfo(blocks)").fetchall()
        expected = [
            ("ordinal", "INTEGER", 0, 1),
            ("request_id", "TEXT", 1, 0),
            ("block_json", "TEXT", 1, 0),
            ("block_hash", "TEXT", 1, 0),
        ]
        actual = [(row[1], row[2].upper(), row[3], row[5]) for row in columns]
        if actual != expected or any(row[6] != 0 for row in columns):
            raise ValueError("SQLite ledger schema mismatch")
        indexes = conn.execute("PRAGMA index_list(blocks)").fetchall()
        if not any(
            row[2] == 1 and row[4] == 0
            and [col[0] for col in conn.execute(
                "SELECT name FROM pragma_index_info(?) ORDER BY seqno", (row[1],)
            )] == ["request_id"]
            for row in indexes
        ):
            raise ValueError("SQLite ledger request_id uniqueness missing")

    @staticmethod
    def _decode_rows(rows):
        chain = []
        for expected, (ordinal, request_id, raw, block_hash) in enumerate(rows, 1):
            if ordinal != expected:
                raise ValueError("SQLite ledger ordinal gap")
            block = json.loads(raw)
            if not isinstance(block, dict):
                raise ValueError("SQLite ledger block schema mismatch")
            if _request_id(block.get("event")) != request_id or block.get("hash") != block_hash:
                raise ValueError("SQLite ledger index and block mismatch")
            chain.append(block)
        _validate_chain(chain)
        return chain

    def read_chain(self):
        conn = self._connect()
        try:
            conn.execute("BEGIN")
            self._check_schema(conn)
            rows = conn.execute("SELECT ordinal, request_id, block_json, block_hash FROM blocks ORDER BY ordinal").fetchall()
            chain = self._decode_rows(rows)
            conn.commit()
            return chain
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def lookup_request_id(self, request_id):
        if not isinstance(request_id, str) or not request_id:
            raise ValueError("request_id required")
        return next((block for block in self.read_chain() if block["event"]["request_id"] == request_id), None)

    def append_event(self, event_payload, *, after_acquire=None, before_commit=None):
        event_raw = _event_bytes(event_payload)
        request_id = event_payload["request_id"]
        conn = self._connect()
        try:
            conn.execute("BEGIN IMMEDIATE")
            if after_acquire is not None:
                after_acquire()
            self._check_schema(conn)
            rows = conn.execute("SELECT ordinal, request_id, block_json, block_hash FROM blocks ORDER BY ordinal").fetchall()
            chain = self._decode_rows(rows)
            existing = next((block for block in chain if block["event"]["request_id"] == request_id), None)
            if existing is not None:
                if _event_bytes(existing["event"]) != event_raw:
                    raise ValueError("Conflicting event for existing request_id")
                conn.commit()
                return existing
            block = self.builder.build_block(chain[-1]["hash"] if chain else "GENESIS", event_payload)
            conn.execute("INSERT INTO blocks (ordinal, request_id, block_json, block_hash) VALUES (?, ?, ?, ?)",
                         (len(chain) + 1, request_id, json.dumps(block, sort_keys=True, allow_nan=False), block["hash"]))
            if before_commit is not None:
                before_commit()
            conn.commit()
            return block
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    @classmethod
    def import_json(cls, source_path, target_path):
        """Import a copied quiescent source into a new database path."""
        source = Path(source_path)
        target = Path(target_path)
        if target.exists() or any(Path(str(target) + suffix).exists() for suffix in ("-wal", "-shm")):
            raise FileExistsError("Migration target must be absent")
        raw = source.read_bytes()
        chain = json.loads(raw)
        tip = _validate_chain(chain)
        ledger = cls(target)
        conn = ledger._connect()
        try:
            conn.execute("BEGIN IMMEDIATE")
            for ordinal, block in enumerate(chain, 1):
                conn.execute("INSERT INTO blocks (ordinal, request_id, block_json, block_hash) VALUES (?, ?, ?, ?)",
                             (ordinal, block["event"]["request_id"], json.dumps(block, sort_keys=True, allow_nan=False), block["hash"]))
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        if ledger.read_chain() != chain or source.read_bytes() != raw:
            raise ValueError("Migration verification failed")
        return {"source_sha256": hashlib.sha256(raw).hexdigest(), "count": len(chain), "tip": tip}

    def backup_to(self, target_path):
        target = Path(target_path)
        if target.exists() or any(Path(str(target) + suffix).exists() for suffix in ("-wal", "-shm")):
            raise FileExistsError("Backup target must be absent")
        source = self._connect()
        destination = sqlite3.connect(target)
        try:
            source.backup(destination)
        finally:
            destination.close()
            source.close()
        restored = type(self)(target)
        actual = restored.read_chain()
        return {"count": len(actual), "tip": _validate_chain(actual), "request_ids": [block["event"]["request_id"] for block in actual]}

    @classmethod
    def restore_backup(cls, backup_path, target_path):
        """Verify a backup and restore it to an absent local database path."""
        if not Path(backup_path).is_file():
            raise FileNotFoundError("Backup source is absent")
        source = cls(backup_path)
        expected = source.read_chain()
        target = Path(target_path)
        if target.exists() or any(Path(str(target) + suffix).exists() for suffix in ("-wal", "-shm")):
            raise FileExistsError("Restore target must be absent")
        source_conn = source._connect()
        target_conn = sqlite3.connect(target)
        try:
            source_conn.backup(target_conn)
        finally:
            target_conn.close()
            source_conn.close()
        actual = cls(target).read_chain()
        if actual != expected:
            raise ValueError("Restored chain differs from backup")
        return {"count": len(actual), "tip": _validate_chain(actual), "request_ids": [block["event"]["request_id"] for block in actual]}
