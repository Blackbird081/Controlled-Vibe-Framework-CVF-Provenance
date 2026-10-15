"""Nine admitted inert failure classes exercise the same finally collector as runtime."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cvf_ncr_html_owned_profile import profile as P
from cvf_ncr_html_owned_profile.lifecycle import Collector, finalize, parse_docker_ids, parse_tasklist, remove_disposable

SCRATCH = P.ROOT / ".cvf/runtime/ncr-html-integrated-root-build-worker-20261015"
CASES = ("taskkill-nonzero", "tasklist-nonzero", "docker-ps-nonzero", "timeout", "tasklist-malformed",
         "identity-mismatch", "still-live", "unsafe-path", "docker-ps-malformed")


class SubstituteNative:
    """Only identity data are inert. Command exits/timeouts are real finite subprocesses."""
    def __init__(self, case, path):
        self.case, self.container, self.stage = case, "a" * 64, path / "source"
        self.c, self.calls, self.closed, self.disposed = Collector(path), 0, False, False
        self.stage.mkdir(parents=True)

    def command(self, kind, stdout, rc=0, pause=0):
        self.calls += 1
        argv = [sys.executable, "-B", "-c", f"import time,sys;time.sleep({pause});print({stdout!r});sys.exit({rc})"]
        return self.c.command(kind, argv, timeout=.15 if pause else 2)

    def prepare_kill(self):
        if self.case == "identity-mismatch":
            raise RuntimeError("creation identity differs from recorded owner")
        return [{"pid": 43210, "creation100ns": 123, "image": "INERT_NO_PRODUCT"}]

    def kill(self, _identity):
        self.command("taskkill", "", 7 if self.case == "taskkill-nonzero" else 0, 1 if self.case == "timeout" else 0)

    def remove_container(self):
        pass  # no actual engine/container exists in any inert control

    def query_processes(self):
        raw = '"inert.exe","43210","Console","1","1 K"' if self.case == "still-live" else '"system.exe","4","Services","0","1 K"'
        if self.case == "tasklist-malformed":
            raw = "not CSV"
        return parse_tasklist(self.command("tasklist", raw, 9 if self.case == "tasklist-nonzero" else 0))

    def query_containers(self):
        raw = "not-an-id" if self.case == "docker-ps-malformed" else ""
        return parse_docker_ids(self.command("docker-ps", raw, 8 if self.case == "docker-ps-nonzero" else 0).strip())

    def members(self):
        return [43210] if self.case in ("still-live", "identity-mismatch") else []

    def listeners(self):
        return []

    def dispose(self):
        self.disposed = True
        if self.case == "unsafe-path":
            remove_disposable(self.stage, self.stage)  # wrong lexical/resolved parent, never delete
        else:
            self.stage.rmdir()

    def close(self):
        self.closed = True


@pytest.mark.parametrize("case", CASES)
def test_actual_finally_rejects_failed_native_control(case):
    root = SCRATCH / "inert" / case
    root.mkdir(parents=True, exist_ok=False)
    ops = SubstituteNative(case, root)
    try:
        pass  # no product start; the same unconditional runtime finally owns collection
    finally:
        result = finalize(ops, [])
    assert result["disposition"] == "NOT_ACCEPTED_UNKNOWN"
    assert ops.closed and ops.stage.exists()
    assert result["errors"] or result["processQuery"] == "LIVE"
    assert not ops.disposed or case == "unsafe-path"
    payload = {"case": case, "result": result, "substituteStarts": ops.calls,
               "productStarts": 0, "engineStarts": 0, "providerStarts": 0}
    (root / "result.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    existing = [json.loads((SCRATCH / "inert" / x / "result.json").read_text(encoding="utf-8"))
                for x in CASES if (SCRATCH / "inert" / x / "result.json").exists()]
    receipt = {"passed": len(existing), "substituteStarts": sum(x["substituteStarts"] for x in existing),
               "testSourceSha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "cases": existing}
    (SCRATCH / "inert-results.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")


def test_canonical_fixtures_and_native_read_only_path():
    values = P.fixtures()
    assert [len(x["sourceContent"].encode("utf-16-le")) // 2 for x in values] == [650, 726]
    assert values[0]["sourceContent"] != values[1]["sourceContent"]
    assert "?mode=ro" in Path(P.__file__).read_text(encoding="utf-8")


def test_legacy_python_entry_contract_unchanged():
    target = P.ROOT / P.OUTPUTS[0]
    original = subprocess.check_output(["git", "show", "HEAD:" + P.OUTPUTS[0]], cwd=P.ROOT)
    current = target.read_bytes()
    addition = b'    if "--owned-profile-root" in sys.argv:\n        from cvf_ncr_html_owned_profile import cli\n        sys.exit(cli())\n'
    assert current.replace(addition, b"", 1) == original
    spec = importlib.util.spec_from_file_location("owned_legacy_probe", target)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.make_export_body("focused")["memoryClass"] == "FULL_RECORD"
    assert module.hcr_raised(module.hcr_admit_forward, True, 2)
