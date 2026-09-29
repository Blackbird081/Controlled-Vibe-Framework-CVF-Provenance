"""Safety and negative-oracle tests for the disposable Q001 system-chain probe."""

from __future__ import annotations

import sys
import tempfile
import threading
from pathlib import Path

from scripts.probe_cvf_q001_synthetic_system_chain import (
    ENGINE,
    EngineProxy,
    ROOT,
    free_port,
    inspect_store,
    request_json,
    stage_tracked_source,
)


def test_staging_uses_tracked_source_without_env_or_current_json_ledger():
    with tempfile.TemporaryDirectory() as directory:
        stage = Path(directory)
        count = stage_tracked_source(stage)
        assert count > 100
        assert (stage / "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts").is_file()
        assert (stage / ENGINE / "api/server.py").is_file()
        assert not list(stage.rglob(".env.local"))
        assert not list(stage.rglob("ledger_chain.json"))


def test_exact_id_oracle_rejects_wrong_id_and_wrong_store():
    sys.path.insert(0, str(ROOT / ENGINE))
    try:
        from ledger_layer.sqlite_ledger import SqliteLedger
        with tempfile.TemporaryDirectory() as directory:
            store = Path(directory) / "one.sqlite"
            other = Path(directory) / "other.sqlite"
            SqliteLedger(store).append_event({"request_id": "test-exact", "decision": {"final_decision": "ALLOW"}})
            correct = inspect_store(ROOT, store, "test-exact")
            wrong_id = inspect_store(ROOT, store, "wrong-test-exact")
            wrong_store = inspect_store(ROOT, other, "test-exact")
            assert correct["exactIdFound"] and correct["count"] == 1 and correct["chainValid"]
            assert not wrong_id["exactIdFound"] and wrong_id["count"] == 1
            assert not wrong_store["exactIdFound"] and wrong_store["count"] == 0
    finally:
        sys.path.pop(0)


def test_malformed_and_unavailable_proxy_modes_do_not_forward_engine_calls():
    proxy = EngineProxy(free_port(), free_port())
    thread = threading.Thread(target=proxy.serve_forever, daemon=True)
    thread.start()
    try:
        url = f"http://127.0.0.1:{proxy.server_port}/api/v1/evaluate"
        proxy.mode = "malformed"
        malformed_status, malformed = request_json(url, {"request_id": "one"})
        proxy.mode = "unavailable"
        unavailable_status, unavailable = request_json(url, {"request_id": "two"})
        assert malformed_status == 200 and malformed["data"]["not_a_report"] is True
        assert unavailable_status == 503 and unavailable == {}
        assert proxy.forwarded == 0
    finally:
        proxy.shutdown()
        proxy.server_close()
        thread.join(timeout=3)
