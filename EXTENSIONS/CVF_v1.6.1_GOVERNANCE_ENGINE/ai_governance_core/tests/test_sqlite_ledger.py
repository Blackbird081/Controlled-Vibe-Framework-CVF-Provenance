"""Synthetic local transaction, migration, restore and real peer proofs."""

import hashlib
import json
import os
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

import pytest

from ledger_layer.block_builder import BlockBuilder
from ledger_layer.sqlite_ledger import SqliteLedger


def _state(ledger):
    chain = ledger.read_chain()
    return (len(chain), chain[-1]["hash"] if chain else "GENESIS",
            [block["event"]["request_id"] for block in chain], chain)


def test_append_rollback_duplicate_and_exact_lookup(tmp_path):
    ledger = SqliteLedger(tmp_path / "candidate.sqlite")
    first = ledger.append_event({"request_id": "one", "artifact_id": "artifact-A"})
    before = _state(ledger)

    def fail_after_acquire():
        raise RuntimeError("AFTER_ACQUIRE_BEFORE_MUTATION")

    with pytest.raises(RuntimeError, match="AFTER_ACQUIRE_BEFORE_MUTATION"):
        ledger.append_event({"request_id": "two"}, after_acquire=fail_after_acquire)
    assert _state(ledger) == before
    assert ledger.lookup_request_id("two") is None
    with pytest.raises(RuntimeError, match="AFTER_INSERT_BEFORE_COMMIT"):
        ledger.append_event({"request_id": "two"}, before_commit=lambda: (_ for _ in ()).throw(RuntimeError("AFTER_INSERT_BEFORE_COMMIT")))
    assert _state(ledger) == before
    assert ledger.append_event({"artifact_id": "artifact-A", "request_id": "one"}) == first
    assert _state(ledger) == before
    with pytest.raises(ValueError, match="Conflicting"):
        ledger.append_event({"request_id": "one", "artifact_id": "artifact-B"})
    assert _state(ledger) == before
    assert ledger.lookup_request_id("one") == first
    assert ledger.append_event({"request_id": "two"})["previous_hash"] == first["hash"]
    assert _state(ledger)[0] == 2  # SUBSEQUENT_PEER_ACQUIRES is tested below.
    assert SqliteLedger(tmp_path / "candidate.sqlite").lookup_request_id("two")["event"]["request_id"] == "two"


def test_incompatible_existing_database_is_not_initialized(tmp_path):
    target = tmp_path / "unknown.sqlite"
    sqlite3.connect(target).close()
    with pytest.raises(ValueError, match="Unversioned"):
        SqliteLedger(target)
    assert target.exists()


@pytest.mark.parametrize("schema", [
    "ordinal TEXT, request_id TEXT NOT NULL, block_json TEXT NOT NULL, block_hash TEXT NOT NULL, UNIQUE(request_id, block_hash)",
    "ordinal INTEGER PRIMARY KEY, request_id TEXT NOT NULL, block_json TEXT NOT NULL, block_hash TEXT NOT NULL, UNIQUE(request_id, block_hash)",
    "ordinal INTEGER PRIMARY KEY, request_id TEXT, block_json TEXT NOT NULL, block_hash TEXT NOT NULL, UNIQUE(request_id)",
])
def test_version_one_incompatible_schema_rejected(tmp_path, schema):
    target = tmp_path / "wrong-schema.sqlite"
    with sqlite3.connect(target) as conn:
        conn.execute(f"CREATE TABLE blocks ({schema})")
        conn.execute("PRAGMA user_version=1")
    with pytest.raises(ValueError, match="schema|uniqueness"):
        SqliteLedger(target)


def test_version_one_partial_request_id_index_rejected(tmp_path):
    target = tmp_path / "partial-schema.sqlite"
    with sqlite3.connect(target) as conn:
        conn.execute("CREATE TABLE blocks (ordinal INTEGER PRIMARY KEY, request_id TEXT NOT NULL, block_json TEXT NOT NULL, block_hash TEXT NOT NULL)")
        conn.execute("CREATE UNIQUE INDEX request_id_partial ON blocks(request_id) WHERE request_id != ''")
        conn.execute("PRAGMA user_version=1")
    with pytest.raises(ValueError, match="uniqueness"):
        SqliteLedger(target)


def test_import_rejects_bad_source_and_restores_clean_backup(tmp_path):
    builder = BlockBuilder()
    one = builder.build_block("GENESIS", {"request_id": "one", "artifact_id": "A"})
    two = builder.build_block(one["hash"], {"request_id": "two", "artifact_id": "B"})
    source = tmp_path / "source-copy.json"
    source.write_text(json.dumps([one, two]), encoding="utf-8")
    raw = source.read_bytes()
    target = tmp_path / "imported.sqlite"
    result = SqliteLedger.import_json(source, target)
    assert result == {"source_sha256": hashlib.sha256(raw).hexdigest(), "count": 2, "tip": two["hash"]}
    assert source.read_bytes() == raw
    ledger = SqliteLedger(target)
    assert ledger.read_chain() == [one, two]
    assert ledger.lookup_request_id("two")["event"]["artifact_id"] == "B"
    with pytest.raises(FileExistsError):
        SqliteLedger.import_json(source, target)
    assert ledger.read_chain() == [one, two]

    bad = tmp_path / "bad.json"
    for chain in ([dict(two, hash="0" * 64)], [one, one], [dict(two, previous_hash="GENESIS")]):
        bad.write_text(json.dumps(chain), encoding="utf-8")
        with pytest.raises(ValueError):
            SqliteLedger.import_json(bad, tmp_path / "rejected.sqlite")
        assert not (tmp_path / "rejected.sqlite").exists()

    backup = tmp_path / "backup.sqlite"
    snapshot = ledger.backup_to(backup)
    assert snapshot == {"count": 2, "tip": two["hash"], "request_ids": ["one", "two"]}
    clean = tmp_path / "clean.sqlite"
    assert SqliteLedger.restore_backup(backup, clean) == snapshot
    restored = SqliteLedger(clean)
    assert restored.read_chain() == [one, two]
    with sqlite3.connect(backup) as conn:
        conn.execute("UPDATE blocks SET block_hash=? WHERE ordinal=2", ("0" * 64,))
    with pytest.raises(ValueError, match="mismatch"):
        SqliteLedger(backup)


def _assert_order(events, release_start_ns, entered_ns):
    # Child occurrence time, rather than parent pipe-read order, decides
    # whether entry preceded release. perf_counter_ns uses the shared OS clock.
    if entered_ns < release_start_ns:
        raise AssertionError("REJECT_ENTRY_BEFORE_PARENT_RELEASE")
    assert events.index("READY") < events.index("START_ATTEMPT") < events.index("ATTEMPTING")
    assert events.index("PARENT_RELEASE") < events.index("ENTERED") < events.index("COMPLETE")


def _run_peer_barrier(path, request_id, *, early_mutant=False):
    parent = sqlite3.connect(path)
    parent.execute("BEGIN IMMEDIATE")
    events = []
    command = [sys.executable, str(Path(__file__).with_name("q001_sqlite_ledger_peer.py")), str(path), request_id]
    if early_mutant:
        command.append("--early-entered-mutant")
    child = subprocess.Popen(command,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True, bufsize=1, cwd=str(Path(__file__).parents[1]),
                             env={**os.environ, "PYTHONPATH": str(Path(__file__).parents[1])})
    try:
        assert child.stdout.readline().strip() == "READY"
        events.append("READY")
        child.stdin.write("START_ATTEMPT\n")
        child.stdin.flush()
        events.append("START_ATTEMPT")
        assert child.stdout.readline().strip() == "ATTEMPTING"
        events.append("ATTEMPTING")
        # The locked parent owns the write transaction. Release is an explicit
        # event, never inferred from a timeout or missing child output.
        release_start_ns = time.perf_counter_ns()
        parent.commit()
        events.append("PARENT_RELEASE")
        entered_line = child.stdout.readline().strip()
        assert entered_line.startswith("ENTERED:")
        entered_ns = int(entered_line.split(":", 1)[1])
        events.append("ENTERED")
        assert child.stdout.readline().strip() == "COMPLETE"
        events.append("COMPLETE")
        assert child.wait(timeout=10) == 0, child.stderr.read()
    finally:
        parent.rollback()
        parent.close()
        if child.poll() is None:
            child.kill()
            child.wait(timeout=10)
    return events, release_start_ns, entered_ns


def test_real_second_process_serializes_and_post_acquire_cleanup(tmp_path):
    path = tmp_path / "peer.sqlite"
    ledger = SqliteLedger(path)
    ledger.append_event({"request_id": "one"})
    _assert_order(*_run_peer_barrier(path, "two"))
    mutant_path = tmp_path / "mutant.sqlite"
    SqliteLedger(mutant_path)
    with pytest.raises(AssertionError, match="REJECT_ENTRY_BEFORE_PARENT_RELEASE"):
        _assert_order(*_run_peer_barrier(mutant_path, "mutant", early_mutant=True))
    assert _state(ledger)[2] == ["one", "two"]

    def fail():
        raise RuntimeError("AFTER_ACQUIRE_BEFORE_MUTATION")

    before = _state(ledger)
    with pytest.raises(RuntimeError, match="AFTER_ACQUIRE_BEFORE_MUTATION"):
        ledger.append_event({"request_id": "fault"}, after_acquire=fail)
    assert _state(ledger) == before
    subsequent = subprocess.run([sys.executable, str(Path(__file__).with_name("q001_sqlite_ledger_peer.py")), str(path), "three"],
                                input="START_ATTEMPT\n", capture_output=True, text=True,
                                cwd=str(Path(__file__).parents[1]), timeout=10,
                                env={**os.environ, "PYTHONPATH": str(Path(__file__).parents[1])})
    assert subsequent.returncode == 0, subsequent.stderr
    assert subsequent.stdout.splitlines()[0:2] == ["READY", "ATTEMPTING"]
    assert subsequent.stdout.splitlines()[2].startswith("ENTERED:")
    assert subsequent.stdout.splitlines()[3] == "COMPLETE"
    assert _state(ledger)[2] == ["one", "two", "three"]  # SUBSEQUENT_PEER_ACQUIRES


def test_api_backend_selection_and_limited_tail(tmp_path, monkeypatch):
    import importlib

    monkeypatch.setenv("CVF_GOVERNANCE_LEDGER_PATH", str(tmp_path / "api.sqlite"))
    import api.server as server
    server = importlib.reload(server)
    try:
        assert isinstance(server._ledger, SqliteLedger)
        for request_id in ("a", "b", "c"):
            server._ledger.append_event({"request_id": request_id})
        import asyncio
        result = asyncio.run(server.ledger(limit=2))
        assert result.data["total_blocks"] == 3
        assert result.data["returned"] == 2
        assert [entry["event"]["request_id"] for entry in result.data["entries"]] == ["b", "c"]
        assert set(result.data["entries"][0]) == {"timestamp", "previous_hash", "event", "hash"}
    finally:
        json_path = tmp_path / "api.json"
        json_path.write_text("[]", encoding="utf-8")
        monkeypatch.setenv("CVF_GOVERNANCE_LEDGER_PATH", str(json_path))
        importlib.reload(server)
