"""Offline model and fault matrix for the execution owner. Every double records; nothing starts a child, calls a native API or removes a tree."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import threading
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cvf_ncr_html_owned_profile import execution as E
from cvf_ncr_html_owned_profile import lifecycle as L
from cvf_ncr_html_owned_profile import profile as P
from cvf_ncr_html_owned_profile import protocol as PR

if {"CVF_NCR_ALLOWED_PORTS", "CVF_HCR_EGRESS_LOG"} & set(os.environ):
    raise RuntimeError("inherited network-guard activation is refused in the pure test environment")
SCRATCH = P.ROOT / ".cvf/runtime/ncr-html-root-local-repair-20261016" / ("exec-" + os.urandom(8).hex())  # fresh per invocation
DONE = subprocess.CompletedProcess


class Tick:
    now = 0.0  # injected monotonic clock
    __call__ = lambda self: self.now


@pytest.fixture
def scratch(request):
    path = SCRATCH / "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in request.node.name)[-90:]
    path.mkdir(parents=True)  # fixture trees are preserved: this suite never disposes of anything
    return path


@pytest.fixture
def no_delete(monkeypatch):
    for owner, attr in ((shutil, "rmtree"), (os, "rmdir"), (Path, "rmdir")):
        monkeypatch.setattr(owner, attr, raising(AssertionError("actual filesystem disposal is not admitted in this phase")))


def raising(error):
    def runner(*_args, **_kw):
        raise error
    return runner


def refuse(exc, fn, *args, **kw):
    with pytest.raises(exc) as caught:
        fn(*args, **kw)
    return caught.value


def events(path):
    return json.loads((path / "commands.json").read_bytes())


def timed(work=10, cleanup=5):
    clock = Tick()
    return clock, PR.Protocol(clock, work, cleanup, "g1").start()


def persisting(collector, advance):
    real = collector.save
    collector.save = lambda kind, unlaunched=False: (setattr(collector.proto.clock, "now", collector.proto.clock.now + advance) if unlaunched else None, real(kind, unlaunched))[1]
    return collector


class TestSafeEvidence:
    SECRETS = ["Authorization: Bearer abc123", b"Authorization Bearer abc123", "curl -H 'Authorization: Basic abc123' x", 'password="hunter2" ok', "token=abc123&x=1",
               "--password hunter2 --verbose", "/token:abc123 /v", "C:\\bin\\tool.exe --api-key abc123", '{"secret": "abc123", "n": 1}', b"x \xff Bearer abc123",
               'Authorization: "Bearer abc123"', "Bearer 'abc123'", 'Bearer \\"abc123\\"', '{\\"Authorization\\": \\"Bearer abc 123\\"}', 'password="two words abc123"',
               "--password \"two words abc123\"", "/password:'abc123 x'", 'x token="abc123', "-token=abc123", "api_key: 'abc123'", '{"token": "abc123"}', "cookie=abc123; x=1", r'{\"Authorization\":\"Bearer \\\"abc123\\\"\"}', r'{"token": "sec\"abc123 x"}', 'Authorization: Bearer "abc123"']

    SECRETS += ['Authorization: Bearer "first abc123', "Bearer 'first abc123", 'token="first abc123',
                "/password:'first abc123", r'Authorization: Bearer \"first abc123', r'{\"token\":\"first abc123']

    @pytest.mark.parametrize("raw", SECRETS)
    def test_quoted_escaped_adjacent_and_bearer_credentials_are_redacted_in_text_and_bytes(self, raw):
        out = E.bounded(raw)
        assert "abc123" not in out and "hunter2" not in out and "[REDACTED]" in out and E.bounded(out) == out

    def test_serializer_redacts_before_truncating_and_keeps_basename_and_counts(self):
        evidence = E.argv_evidence(["C:\\Tools\\bin\\tool.exe", "--password", "hunter2", "-H", "Authorization:", "Bearer", "abc123", "--name=x", "/token", "tok-9", "plain"])
        text = json.dumps(evidence)
        assert evidence["executable"] == "tool.exe" and evidence["argc"] == 11 and "plain" in text and "C:" not in text and not {"hunter2", "abc123", "tok-9"} & set(text.replace('"', " ").replace(",", " ").split())
        for tail in ("password=hunter2 tail", 'token="hunter2'):  # a cut can never expose part of a secret
            out = E.bounded("x" * 1990 + " " + tail)
            assert "hunt" not in out and "truncated" in out and json.loads(E.dumps([out]))[0] == out
        assert E.safe({"password": ["hunter2"], "token": {"v": "abc123"}, "ok": True, "n": [{"token": "abc"}]}) == {
            "password": "[REDACTED]", "token": "[REDACTED]", "ok": True, "n": [{"token": "[REDACTED]"}]}


class TestCommands:
    @pytest.mark.parametrize("code,expected", [(0, "SUCCESS"), (3, "NONZERO_EXIT")] + [(v, "UNKNOWN") for v in (None, False, True, "0", 0.0)])
    def test_only_int_zero_succeeds_any_other_value_is_unknown(self, scratch, code, expected):
        assert E.completion(code) == expected
        if expected == "UNKNOWN":  # an unknown exit is a retained failure, never a success
            error = refuse(E.CommandFailure, E.Collector(scratch, lambda argv, **kw: DONE(argv, code, "incomplete", "")).command, "probe", ["tool"])
            assert error.failure_class == "UNKNOWN" and events(scratch)[-1]["exitCode"] is None and events(scratch)[-1]["state"] == "FINISHED"

    def test_runner_receives_a_fresh_finite_wait_after_prelaunch_persistence_and_nothing_once_expired(self, scratch):
        clock, p = timed()
        seen = []
        c = persisting(E.Collector(scratch, lambda argv, **kw: seen.append((kw["timeout"], events(scratch)[-1]["state"])) or DONE(argv, 0, "ok", ""), proto=p), 8)
        assert c.command("probe", ["tool"], timeout=10) == "ok" and seen == [(2, "QUEUED")]  # persisted QUEUED; the wait is the fresh remainder, not 10
        clock2, p2 = timed()
        c2 = persisting(E.Collector(scratch / "late", lambda argv, **kw: pytest.fail("launched after the cutoff"), proto=p2), 11)
        refuse(PR.NotAdmitted, c2.command, "probe", ["tool"])  # persistence consumed the whole work window
        assert events(scratch / "late")[-1]["state"] == "NOT_LAUNCHED" and events(scratch / "late")[-1]["failureClass"] == "REFUSED" and p2.state == PR.CLOSING
        refuse(PR.NotAdmitted, c2.command, "after", ["tool"])  # and nothing new is admitted afterwards

    def test_failed_prelaunch_persistence_prevents_the_invocation_and_final_failure_never_replaces_the_original(self, scratch):
        (scratch / "blocked").write_text("a file, so custody cannot be created", encoding="utf-8")
        blocked = E.Collector(scratch / "blocked", raising(AssertionError("launched")))
        assert refuse(E.CommandFailure, blocked.command, "probe", ["tool"]).failure_class == "PERSIST" and blocked.events == []

        def flaky(c):  # the prelaunch write succeeds, the final write fails
            real = c.save
            c.save = lambda kind, unlaunched=False: real(kind, unlaunched) if unlaunched else (_ for _ in ()).throw(E.CommandFailure(kind, "PERSIST"))
            return c
        error = refuse(E.CommandFailure, flaky(E.Collector(scratch, lambda argv, **kw: DONE(argv, 5, "", "boom"))).command, "probe", ["tool"])
        assert (error.failure_class, error.persist_error) == ("NONZERO_EXIT", "PERSIST")
        assert refuse(E.CommandFailure, flaky(E.Collector(scratch / "ok", lambda argv, **kw: DONE(argv, 0, "", ""))).command, "probe", ["tool"]).failure_class == "PERSIST"

    @pytest.mark.parametrize("runner,expected,kw", [
        (raising(FileNotFoundError("missing")), "SPAWN", {}), (raising(ValueError("odd")), "UNKNOWN", {}), (lambda argv, **k: DONE(argv, 3, "partial", "bad"), "NONZERO_EXIT", {}),
        (lambda argv, **k: DONE(argv, 0, "ok", ""), "PARSE", {"parse": json.loads}),
        (raising(subprocess.TimeoutExpired(["tool"], 1, output=b"token=abc123 " + b"x" * 5000, stderr=b"")), "TIMEOUT", {})])
    def test_failure_classes_are_distinct_bounded_and_secret_safe(self, scratch, runner, expected, kw):
        error = refuse(E.CommandFailure, E.Collector(scratch, runner).command, "probe", ["tool"], **kw)
        event = events(scratch)[-1]
        assert error.failure_class == event["failureClass"] == expected and len(event["stdout"]) < 2100 and "abc123" not in json.dumps(event)
        assert event["timedOut"] is (expected == "TIMEOUT") and (expected != "TIMEOUT" or event["stdout"].startswith("token=[REDACTED]") and "truncated" in event["stdout"])

    def test_the_one_shot_module_query_never_retries_or_falls_back(self, scratch):
        c = E.Collector(scratch, lambda argv, **kw: DONE(argv, 5, "", ""))
        refuse(E.CommandFailure, c.command, "installed-browser-path", ["node"])
        assert refuse(E.CommandFailure, c.command, "installed-browser-path", ["node"]).failure_class == "REPEAT_REFUSED" and len(c.events) == 1


class Double:
    # Recording fake used as terminal ops, kernel API and Popen child: logs ordered calls and fails the named step; nothing native exists.
    container, container_identity_pending, pid, _handle, returncode = None, False, 77, 5, 0
    OUT = {"create_job": "job", "members": [], "listeners": [], "query_processes": set(), "query_containers": set(),
           "prepare_kill": [{"pid": 9}], "verify_disposal_target": True}

    def __init__(self, path=None, fail=None, policy=None, slow=False):
        self.calls, self.fail, self.custody, self.roots, self.killed, self.slow, self.waits, self.timeouts = [], fail, path, None, False, slow, [], []
        self.policy = policy or {"active": 32, "killOnClose": True, "breakaway": False, "silentBreakaway": False}
        self.stage = path and path / "source"
        if path:
            self.stage.mkdir(parents=True)

    def act(self, name, *args):
        self.calls.append(name)
        self.killed = self.killed or name == "kill"
        if name == "resume" and self.custody and (self.custody / "process-roots.json").is_file():
            self.roots = (self.custody / "process-roots.json").read_text(encoding="utf-8")
        if name == self.fail:
            raise OSError("fault " + name)
        return {**self.OUT, "query_limits": self.policy, "identity": {"pid": args[0] if args else 0, "creation100ns": 1, "image": "inert"}}.get(name)

    def __getattr__(self, name):
        return lambda *args, **_kw: self.act(name, *args)

    poll = lambda self: 1 if self.killed else None
    wait = lambda self, timeout=None: self.waits.append(timeout)

    def communicate(self, data=None, timeout=None):
        self.timeouts.append(timeout)
        if self.slow and (not self.killed or self.slow == "hang"):
            raise subprocess.TimeoutExpired("x", timeout)
        return ("late", "") if self.killed else ("out", "err")


class TestDeadlines:
    @pytest.mark.parametrize("fault", ("kill", "drain"))
    def test_cancellation_fault_keeps_primary_timeout_and_unknown_child(self, scratch, fault):
        child, c = Double(slow=True), E.Collector(scratch)
        if fault == "kill":
            child.kill = raising(OSError("SECONDARY_KILL"))
        else:
            def communicate(data=None, timeout=None):
                if not child.killed:
                    raise subprocess.TimeoutExpired("inert", timeout)
                raise OSError("SECONDARY_DRAIN")
            child.communicate = communicate
        c.runner = lambda argv, **kw: E.bounded_communicate(child, c, kw.get("input"), kw["timeout"])
        error = refuse(E.CommandFailure, c.command, "probe", ["inert"], timeout=1)
        assert error.failure_class == "TIMEOUT" and c.proto.snapshot()["operations"][-1]["uncertain"] is True
        assert "SECONDARY" in c.events[-1]["cleanupError"] and c.events[-1]["failureClass"] == "TIMEOUT"

    def test_timeout_drain_uses_only_the_remaining_finite_wait_with_no_floor_and_no_unbounded_fallback(self, scratch):
        clock, p = timed(work=100)
        c, child, hung = E.Collector(scratch, proto=p), Double(slow=True), Double(slow="hang")
        error = refuse(subprocess.TimeoutExpired, E.bounded_communicate, child, c, None, 1)
        assert child.killed and child.timeouts == [1, 2] and (error.stdout, error.stderr) == ("late", "")
        refuse(subprocess.TimeoutExpired, E.bounded_communicate, hung, c, None, 1)
        assert hung.timeouts == [1, 2]  # exactly one bounded drain after the kill, never a third call
        clock.now, late = 99.7, Double(slow=True)
        refuse(subprocess.TimeoutExpired, E.bounded_communicate, late, c, None, 1)
        assert late.killed and late.timeouts == [pytest.approx(.3), pytest.approx(.3)]
        clock.now, expired = 100, Double(slow=True)
        refuse(PR.NotAdmitted, E.bounded_communicate, expired, c, None, 1)
        assert not expired.killed and expired.timeouts == []
        refuse(PR.Deadline, PR.bounded_call, "none", lambda: pytest.fail("started"), 0)  # no remainder: nothing is started

def native(path, kernel=None, proto=None):
    kernel = kernel or Double(path)
    return L.Native(E.Collector(path, proto=proto), [], path / "source", path, api=kernel, popen=lambda argv, **kw: kernel.calls.append("spawn:%s" % kw["creationflags"]) or kernel), kernel


class TestOwnership:
    @pytest.mark.parametrize("fault", ("kill", "wait"))
    def test_failed_spawn_keeps_original_error_and_records_secondary_cleanup(self, scratch, fault):
        ops, k = native(scratch, Double(scratch, "identity"))
        setattr(k, fault, raising(OSError("SECONDARY_CLEANUP")))
        error = refuse(OSError, ops.launch, ["inert"], cwd=scratch, env={}, stdout=None)
        assert str(error) == "fault identity" and "SECONDARY_CLEANUP" in ops.c.cleanup_errors[0]
        terminal = E.finalize(None, [str(error)], ops.c, stage=k.stage)
        assert terminal["evidence"]["primaryFailures"] == ["fault identity"]
        assert "SECONDARY_CLEANUP" in terminal["evidence"]["errors"][0] and not terminal["accepted"]

    def test_utility_wait_is_refreshed_after_identity_persistence(self, scratch):
        clock, p = timed()
        ops, k = native(scratch, proto=p)
        ops.c.runner = ops.run_utility
        ops._record = lambda: setattr(clock, "now", 8)
        assert ops.c.command("probe", ["inert"], timeout=10) == "out"
        assert k.timeouts == [2] and "resume" in k.calls

    def test_exhausted_cleanup_never_kills_or_waits_after_failed_resume_admission(self, scratch):
        clock, p = timed()
        ops, k = native(scratch, proto=p)
        ops._record = lambda: setattr(clock, "now", 20)
        refuse(PR.NotAdmitted, ops.launch, ["inert"], cwd=scratch, env={}, stdout=None)
        assert "resume" not in k.calls and not k.killed and k.waits == []
        assert p.snapshot()["operations"][0]["uncertain"] is True

    def test_job_policy_is_read_back_before_any_child_and_safe_identity_is_persisted_before_resume(self, scratch):
        ops, k = native(scratch)
        assert k.calls == ["create_job", "set_limits", "query_limits"]
        ops.launch(["inert", "--password", "hunter2"], cwd=scratch, env={}, stdout=None)
        assert k.calls[3:] == ["spawn:4", "assign", "identity", "resume"]  # suspended create; identity persisted, then rechecked, before resume
        roots = json.loads(k.roots)
        assert roots[0]["identity"]["pid"] == 77 and roots[0]["executable"] == "inert" and "hunter2" not in k.roots
        off = {"active": 32, "killOnClose": False, "breakaway": False, "silentBreakaway": False}
        for fail, policy in (("create_job", None), ("set_limits", None), ("query_limits", None), (None, off), (None, {**off, "killOnClose": True, "breakaway": True})):
            bad = Double(None, fail, policy)
            refuse((OSError, RuntimeError), L.Native, E.Collector(scratch), [], scratch, scratch, api=bad, popen=lambda *a, **k: pytest.fail("child before policy"))
            assert ("close" in bad.calls) is (fail != "create_job")  # the job handle is closed when policy setup fails
        ops.retained, k.fail = {1: "h1", 2: "h2"}, "close"
        assert "exact-handle close failed" in str(refuse(RuntimeError, ops.close)) and k.calls.count("close") == 3  # every exact handle is attempted

    @pytest.mark.parametrize("fail", ("assign", "identity", "persist", "resume"))
    def test_a_failed_ownership_step_kills_only_the_exact_child_and_never_resumes_before_it(self, scratch, fail):
        ops, k = native(scratch, Double(scratch, None if fail == "persist" else fail))
        if fail == "persist":
            (scratch / "blocked").write_text("file", encoding="utf-8")
            ops.c.custody = scratch / "blocked"
        refuse(OSError, ops.launch, ["inert"], cwd=scratch, env={}, stdout=None)
        assert k.killed and ("resume" in k.calls) is (fail == "resume") and not any("taskkill" in str(e) for e in ops.c.events) and k.waits == [5]

    def test_persistence_consuming_the_cutoff_refuses_resume_and_stops_only_the_exact_child_within_the_cleanup_remainder(self, scratch):
        clock, p = timed()
        ops, k = native(scratch, proto=p)
        ops._record = lambda: setattr(clock, "now", 11)  # identity persistence blocks past the work cutoff
        refuse(PR.NotAdmitted, ops.launch, ["inert"], cwd=scratch, env={}, stdout=None)
        assert "resume" not in k.calls and k.killed and k.waits == [4]  # min(11+5, 10+5) - 11: no fresh five seconds, no PID or name kill
        assert [o["state"] for o in p.snapshot()["operations"]] == [PR.FAILED]

    def test_utility_commands_share_the_job_and_an_expired_owner_admits_no_child(self, scratch):
        clock, p = timed()
        ops, k = native(scratch, proto=p)
        ops.c.runner = ops.run_utility
        assert ops.c.command("probe", ["tool"]) == "out" and k.calls[3:] == ["spawn:4", "assign", "identity", "resume"]
        for name, mode, unobserved in (("second", True, False), ("third", "hang", True)):
            slow = Double(scratch / name, slow=mode)
            ops2, _ = native(scratch / name, slow, p)
            ops2.c.runner = ops2.run_utility
            assert refuse(E.CommandFailure, ops2.c.command, "probe", ["tool"], timeout=1).failure_class == "TIMEOUT" and slow.killed
            assert p.snapshot()["operations"][-1]["uncertain"] is unobserved and (events(scratch / name)[-1]["stdout"] == "late") is not unobserved  # a stopped child whose exit was never seen stays UNKNOWN
        clock.now = 10
        refuse(PR.NotAdmitted, ops.launch, ["inert"], cwd=scratch, env={}, stdout=None)
        refuse(PR.NotAdmitted, ops.run_utility, ["inert"])
        assert k.calls.count("spawn:4") == 1


class TestRetainedStageTerminal:
    FAULTS = (None, "primary_only", "prepare_kill", "kill", "remove_container", "query_processes", "query_containers", "members", "listeners", "verify_disposal_target", "close")

    @pytest.mark.parametrize("fault", FAULTS)
    def test_each_injected_fault_is_preserved_never_accepted_and_never_skips_later_actions(self, scratch, no_delete, fault):
        ops, saved = Double(scratch, None if fault == "primary_only" else fault), {}
        out = E.finalize(ops, [] if fault is None else ["primary failure"], E.Collector(scratch), persist=lambda raw: saved.update(raw=raw), read_back=lambda: saved["raw"])
        assert {"remove_container", "query_processes", "query_containers", "members", "listeners", "verify_disposal_target", "close"} <= set(ops.calls)
        assert out["actualDisposal"] == "NOT_ATTEMPTED" and ops.stage.exists() and out["stageRetained"] is True  # the recording stage model is never removed
        assert E.sha(saved["raw"]) == out["evidenceSha256"] and json.loads(saved["raw"]) == out["evidence"]  # returned evidence is the frozen bytes
        assert (out["accepted"], out["disposalEligible"]) == ((True, True) if fault is None else (False, False))
        if fault:  # the primary failure alone blocks acceptance; a teardown fault is retained under its own label beside it
            assert out["evidence"]["primaryFailures"] == ["primary failure"] and out["evidence"]["preAckDisposition"] == E.UNKNOWN and (fault == "primary_only") is (out["evidence"]["errors"] == [])

    def test_write_readback_and_timeout_faults_are_distinct_unacceptable_acknowledgments(self, scratch, monkeypatch):
        monkeypatch.setattr(E, "PERSIST_SECONDS", .05)
        saved, gate = {}, threading.Event()

        def ack(name, **kw):
            return E.finalize(Double(scratch / name), [], E.Collector(scratch), **kw)
        failed = ack("w", persist=raising(OSError("disk")), read_back=lambda: b"never")
        assert (failed["acknowledgment"]["write"], failed["acknowledgment"]["readBack"], failed["accepted"]) == ("FAILED", "NOT_ATTEMPTED", False)
        mismatch = ack("m", persist=lambda raw: saved.update(raw=raw), read_back=lambda: b"other")
        assert (mismatch["acknowledgment"]["readBack"], mismatch["accepted"]) == ("MISMATCH", False)
        missing = ack("u", persist=lambda raw: None, read_back=raising(OSError("gone")))
        assert (missing["acknowledgment"]["readBack"], missing["accepted"]) == ("UNAVAILABLE", False)
        hung = ack("h", persist=lambda raw: gate.wait(), read_back=lambda: b"")
        gate.set()
        assert hung["acknowledgment"]["write"] == "UNKNOWN" and "outcome UNKNOWN" in hung["acknowledgment"]["error"] and hung["accepted"] is False

    def test_proxy_reader_and_log_faults_are_attempted_independently_and_pending_work_blocks_acceptance(self, scratch, no_delete):
        ran, ops, saved, c = [], Double(scratch), {}, E.Collector(scratch)
        op = c.proto.queue("body-read")
        c.proto.grant(op, 1)  # committed work that never reports completion
        out = E.finalize(ops, [], c, before=[("proxy-shutdown", raising(OSError("boom"))), ("proxy-close", lambda: ran.append("proxy-close"))],
                         after=[("reader-join", raising(OSError("boom"))), ("log-0", lambda: ran.append("log-0"))], persist=lambda raw: saved.update(raw=raw), read_back=lambda: saved["raw"])
        assert ran == ["proxy-close", "log-0"] and "close" in ops.calls and not out["accepted"]
        assert [e.split(":")[0] for e in out["evidence"]["errors"]] == ["proxy-shutdown", "reader-join"] and out["evidence"]["uncertainOperations"] == [op.id]

    def test_no_native_resource_run_keeps_its_primary_failure_and_never_claims_acceptance(self, scratch):
        out = E.finalize(None, ["Prerequisite: boom"], E.Collector(scratch), stage=scratch / "source", persist=lambda raw: None, read_back=lambda: b"")
        assert out["evidence"]["preAckDisposition"] == "NOT_STARTED_NO_NATIVE_RESOURCES" and out["stageRetained"] is False and not out["accepted"]
