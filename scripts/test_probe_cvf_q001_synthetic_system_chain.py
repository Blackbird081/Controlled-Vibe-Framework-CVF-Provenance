"""Safety and negative-oracle tests for the disposable Q001 system-chain probe."""

from __future__ import annotations

import sys
import tempfile
import threading
from unittest.mock import patch
from unittest.mock import Mock
import subprocess
import pytest
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
        current_helper = ROOT / "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/bounded-request-body.ts"
        if current_helper.exists():
            assert (stage / current_helper.relative_to(ROOT)).read_bytes() == current_helper.read_bytes()


def test_staging_includes_untracked_and_excludes_credentials_and_deletions():
    import scripts.probe_cvf_q001_synthetic_system_chain as probe
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory) / 'root'; root.mkdir()
        stage = Path(directory) / 'stage'
        files = [probe.WEB / 'src/lib/new-helper.ts', probe.WEB / '.env.local', probe.ENGINE / 'ledger_layer/ledger_chain.json', probe.WEB / 'deleted.ts']
        for relative in files[:-1]:
            target = root / relative; target.parent.mkdir(parents=True, exist_ok=True); target.write_text('synthetic', encoding='utf-8')
        raw = b'\0'.join(str(p).encode() for p in files) + b'\0'
        with patch.object(probe, 'ROOT', root), patch.object(probe.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, stdout=raw)) as run:
            assert probe.stage_tracked_source(stage) == 1
            assert '--others' in run.call_args.args[0]
            assert '--exclude-standard' in run.call_args.args[0]
        assert (stage / files[0]).read_text() == 'synthetic'
        assert not (stage / files[1]).exists()
        assert not (stage / files[2]).exists()


def test_docker_cleanup_checks_owned_container_even_when_client_already_exited():
    import scripts.probe_cvf_q001_synthetic_system_chain as probe
    process = Mock(cvf_docker_name='cvf-q001-web-owned', poll=Mock(return_value=0))
    with patch.object(probe.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, stdout=b'', stderr=b'')) as run:
        probe.stop(process)
        assert run.call_args_list[0].args[0] == ['docker', 'container', 'inspect', 'cvf-q001-web-owned']
        assert run.call_args_list[1].args[0] == ['docker', 'rm', '-f', 'cvf-q001-web-owned']
        process.wait.assert_not_called()


def test_docker_cleanup_distinguishes_already_removed_from_unverifiable():
    import scripts.probe_cvf_q001_synthetic_system_chain as probe
    process = Mock(cvf_docker_name='cvf-q001-web-owned', poll=Mock(return_value=0))
    for error, rejected in [(b'Error: No such container', False), (b'Daemon unavailable', True)]:
        with patch.object(probe.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, stderr=error)) as run:
            if rejected:
                with pytest.raises(RuntimeError, match='Cannot verify'):
                    probe.stop(process)
            else:
                probe.stop(process)
            assert run.call_count == 1
    process.cvf_docker_name = 'unrelated-user-container'
    with patch.object(probe.subprocess, 'run') as run, pytest.raises(RuntimeError, match='Refusing cleanup'):
        probe.stop(process)
    run.assert_not_called()


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
