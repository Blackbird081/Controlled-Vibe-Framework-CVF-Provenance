"""Deterministic offline schedules for the parent protocol. Injected clocks and recording adapters only: no child, socket, native API or deletion."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
import types
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cvf_ncr_html_owned_profile as H
from cvf_ncr_html_owned_profile import execution as E
from cvf_ncr_html_owned_profile import lifecycle as L
from cvf_ncr_html_owned_profile import profile as P
from cvf_ncr_html_owned_profile import protocol as PR

if {"CVF_NCR_ALLOWED_PORTS", "CVF_HCR_EGRESS_LOG"} & set(os.environ):
    raise RuntimeError("inherited network-guard activation is refused in the pure test environment")
SCRATCH = P.ROOT / ".cvf/runtime/ncr-html-root-local-repair-20261016" / ("proto-" + os.urandom(8).hex())  # fresh per invocation


class Clock:
    """Injected monotonic clock that counts samples."""
    def __init__(self, now=0.0):
        self.now, self.samples = now, 0

    def __call__(self):
        self.samples += 1
        return self.now


def make(work=10, cleanup=5):
    clock = Clock()
    return clock, PR.Protocol(clock, work, cleanup, "g1").start()


@pytest.fixture
def scratch(request):
    path = SCRATCH / "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in request.node.name)[-80:]
    path.mkdir(parents=True)  # fixture trees are preserved: this suite never disposes of anything
    return path


def refuse(exc, fn, *args, **kw):
    with pytest.raises(exc) as caught:
        fn(*args, **kw)
    return caught.value


def record(proto, op):
    return {o["id"]: o for o in proto.snapshot()["operations"]}[op.id]


class TestPhaseAndTime:
    def test_cleanup_cutoff_is_the_minimum_fixed_once_and_work_end_is_never_renewed(self):
        refuse(PR.NotAdmitted, PR.Protocol(Clock()).queue, "x")  # PREPARED admits nothing
        clock, p = make()
        refuse(RuntimeError, p.start)
        clock.now = 3
        p.close("early")
        assert p.left(100) == 5  # close(3)+5 < workEnd(10)+5
        clock.now = 4
        p.close("again")
        p.begin_cleanup()
        assert p.left(100) == 4 and p.closed_by == "early" and p.work_end == 10  # fixed once; later closes change nothing
        clock, expired = make()
        clock.now = 12  # persistence consumed the whole work window; the expiry tick is the close
        refuse(PR.NotAdmitted, expired.grant, expired.queue("x"), 5)
        assert expired.left(100) == 3 and expired.work_end == 10  # min(12+5, 10+5): no fresh five seconds

    def test_grant_is_one_clock_sample_with_a_finite_positive_wait(self):
        clock, p = make()
        op, before = p.queue("probe"), clock.samples
        assert p.grant(op, 30) == 10 and clock.samples - before == 1 and op.state == PR.DISPATCHED
        assert p.left(30) == 10 and clock.samples - before == 2
        for requested in (0, -1, float("nan")):
            refuse(PR.Deadline, p.grant, p.queue("bad"), requested)
        clock.now = 9.6  # remainder .4: an integer-unit adapter is refused, never rounded up and never turned into an unlimited 0
        refuse(PR.Deadline, p.grant, p.queue("units"), 5, unit=1)
        clock.now = 7.3
        assert p.grant(p.queue("units"), 5, unit=1) == 2
        clock.now = 10
        assert p.left(5, work_only=True) == 0.0 and p.state == PR.CLOSING  # the same sample that finds expiry fences the protocol

    def test_only_a_cleanup_scope_may_queue_after_the_fence(self):
        clock, p = make()
        p.close("x")
        refuse(PR.NotAdmitted, p.queue, "engine-POST")
        op = p.scoped(lambda: p.queue("tasklist"))()
        assert op.cleanup and p.grant(op, 100) == 5 and p.check(op) == 5 and p.scoped(lambda: p.queue("again"))().cleanup and not getattr(p.scope, "on", False)
        clock.now = 5
        refuse(PR.Deadline, p.check, op)  # a cleanup operation is rechecked against the cleanup cutoff


class TestAdmission:
    def test_close_revokes_queued_work_but_tracks_committed_work_even_before_its_adapter_runs(self):
        clock, p = make()
        queued, committed = p.queue("reply"), p.queue("write")
        p.grant(committed, 5)  # committed BEFORE the fence; its adapter has not been entered
        p.close("failure")
        assert queued.state == PR.REVOKED and committed.state == PR.DISPATCHED
        refuse(PR.NotAdmitted, p.grant, queued, 5)
        refuse(PR.NotAdmitted, p.queue, "follow-on")  # no follow-on normal work
        p.complete(committed)  # the late completion records DONE but cannot clear the uncertainty
        assert record(p, committed)["uncertain"] and record(p, committed)["inflightAtClose"] and record(p, queued)["state"] == PR.REVOKED
        p.freeze()
        p.complete(committed, False, "later")  # after the freeze: appended as late, frozen outcome untouched
        assert p.late == [{"id": committed.id, "kind": "write", "ok": False, "outcome": "later"}] and record(p, committed)["state"] == PR.DONE

    def test_queued_reply_is_revoked_at_close_and_its_adapter_never_runs(self):
        clock, p = make()
        writes, op = [], p.queue("controller-reply")  # QUEUED, not yet committed
        p.close("child-failure")
        refuse(PR.NotAdmitted, p.grant, op, 10)
        refuse(PR.NotAdmitted, PR.run_op, p, "controller-reply", writes.append, 10)
        assert writes == [] and op.state == PR.REVOKED and not p.snapshot()["operations"][-1]["uncertain"]

    def test_close_during_or_after_the_write_leaves_a_tracked_unknown_that_late_completion_cannot_upgrade(self):
        _, a = make()
        op = a.queue("write")
        a.grant(op, 5)
        a.close("x")  # between commit and adapter entry
        a.complete(op)
        _, b = make()
        PR.run_op(b, "write", lambda wait: b.close("during"), 5)  # the fence arrives while the adapter is inside its write
        _, c = make()
        gate = threading.Event()
        refuse(PR.WaitBound, PR.run_op, c, "pipe", lambda wait: gate.wait(), .05, bounded=True)  # an unfinished write is UNKNOWN, not preempted
        gate.set()
        assert record(a, op)["uncertain"] and b.snapshot()["operations"][0]["uncertain"]
        assert c.snapshot()["operations"][0]["state"] == PR.DISPATCHED and c.snapshot()["operations"][0]["outcome"] == "WAIT_BOUND_MISSED"


class TestBudgets:
    def test_buckets_accept_the_exact_boundary_refuse_the_next_attempt_and_never_transfer(self):
        a, b = E.Budget("worker"), E.Budget("local")
        for bucket, limit in (("engine", 4), ("web", 6), ("route", 2)):
            [b.debit(bucket) for _ in range(limit)]
            refuse(E.BudgetExhausted, b.debit, bucket)
        [a.debit("engine") for _ in range(4)]
        refuse(E.BudgetExhausted, a.debit, "engine")
        assert sum(b.used.values()) == 12 and a.used == {"engine": 4, "web": 0, "route": 0}  # unused allowance never lends; actors are independent

    def test_poll_debits_before_each_attempt_and_clamps_sleeps_to_the_work_cutoff(self, scratch):
        sleeps, attempts, (clock, p) = [], [], make(work=1)
        c, budget = E.Collector(scratch, sleeper=sleeps.append, proto=p), E.Budget("worker")
        down = lambda: (attempts.append(budget.used["engine"]), (_ for _ in ()).throw(OSError("down")))
        refuse(RuntimeError, E.poll, c, budget, "engine", down, 4, 5)
        assert attempts == [1, 2, 3, 4] and sleeps == [1, 1, 1]  # charged before each request, sleeps clamped, none after the last
        refuse(E.BudgetExhausted, E.poll, c, budget, "engine", down, 1, 0)
        clock.now = 5
        refuse(PR.Deadline, c.sleep, 1)  # an expired cutoff sleeps zero seconds

class Rfile:
    def __init__(self, data, hook=None):
        self.data, self.hook, self.reads = data, hook, 0

    def read(self, n):
        self.reads += 1
        if self.hook:
            self.hook()
        out, self.data = self.data[:n], self.data[n:]
        return out


class TestBodyAndForward:
    def test_invalid_or_oversized_content_length_is_refused_before_any_read(self):
        _, p = make()
        for raw in (None, "", "abc", "-1", "0", "65537", "12 ", "1e3"):
            rfile = Rfile(b"x" * 10)
            refuse(ValueError, PR.read_body, rfile, raw, p)
            assert rfile.reads == 0
        assert not p.ops

    def test_each_chunk_waits_at_most_the_original_work_cutoff(self):
        clock, p = make(work=10)
        waits = []
        data = b"a" * (PR.BODY_CHUNK + 5)
        assert PR.read_body(Rfile(data), str(len(data)), p, arm=waits.append) == data and waits == [2, 2]
        clock, p = make(work=10)
        slow = Rfile(data, hook=lambda: setattr(clock, "now", clock.now + 11))  # the first chunk crosses the cutoff
        refuse(PR.Deadline, PR.read_body, slow, str(len(data)), p)
        op = p.snapshot()["operations"][0]
        assert slow.reads == 1 and op["outcome"] == "WAIT_BOUND_MISSED" and op["uncertain"]

    def test_pending_body_at_close_refuses_the_forward_and_retains_the_pending_read(self, scratch):
        sent, ran = [], []

        def drive(hook):
            clock, p = make()
            body = json.dumps({"request_id": "r1", "artifact_id": "a", "payload": {"content": "x"}, "cvf_phase": "REVIEW", "cvf_risk_level": "R0"}).encode()

            def runner(argv, **kw):
                ran.append(kw["timeout"])
                return subprocess.CompletedProcess(argv, 0, json.dumps({"status": 200, "body": json.dumps({"data": 1})}), "")
            server = types.SimpleNamespace(lock=threading.Lock(), arrived=0, attempts=0, observed={}, failure=None, cap=2, prefix=["docker"],
                                           container="c" * 64, c=E.Collector(scratch / f"c{len(ran)}{len(sent)}", runner, proto=p))
            me = types.SimpleNamespace(server=server, path="/api/v1/evaluate", headers={"Content-Length": str(len(body))}, rfile=Rfile(body, lambda: hook(clock, p)),
                                       connection=types.SimpleNamespace(settimeout=lambda wait: None), close_connection=False, wfile=types.SimpleNamespace(write=sent.append),
                                       send_response=lambda status: sent.append(("status", status)), send_header=lambda *a: None, end_headers=lambda: None,
                                       send_error=lambda code: sent.append(("error", code)))
            H.Handler.do_POST(me)
            return server, me, p
        server, me, p = drive(lambda clock, proto: None)  # positive control: the forward happens once
        assert ran == [5] and ("status", 200) in sent and "r1" in server.observed and server.failure is None
        for hook in (lambda clock, proto: proto.close("child-failed"), lambda clock, proto: setattr(clock, "now", clock.now + 20)):
            before = len(ran)
            server, me, p = drive(hook)  # close, or the cutoff passing, while the body read is pending
            body_op = p.snapshot()["operations"][0]
            assert len(ran) == before and server.failure.startswith("engine hop failed/ambiguous: NotAdmitted") and me.close_connection is True
            assert body_op["kind"] == "body-read" and body_op["uncertain"] and body_op["inflightAtClose"] and server.observed == {}


class TestChildContract:
    def test_ipc_request_and_reply_are_complete_identity_bound_and_replay_safe(self):
        seen, request = set(), {"n": 1, "op": "c1", "generation": "g1", "external": [], "aiPosts": []}
        good = "EXPORT_GATE_REQUEST " + json.dumps(request)
        kind, arg, op, _ = PR.parse_request(good, "g1", seen)
        assert (kind, arg, op) == ("EXPORT_GATE_OK", 1, "c1") and PR.reply(kind, arg, "g1", op) == "EXPORT_GATE_OK 1 g1 c1"
        assert PR.parse_request("CHECKPOINT built2 g1 c2", "g1", seen)[:3] == ("CHECKPOINT_OK", "built2", "c2")
        bad = [good, "EXPORT_GATE_REQUEST " + json.dumps({**request, "op": "c3", "generation": "g2"}), "EXPORT_GATE_REQUEST " + json.dumps({**request, "op": "c4", "n": True}),
               "EXPORT_GATE_REQUEST " + json.dumps({**request, "op": "c5", "n": 3}), "EXPORT_GATE_REQUEST " + json.dumps({**request, "op": "c6", "extra": 1}),
               "EXPORT_GATE_REQUEST " + json.dumps({**request, "op": "x7"}), "EXPORT_GATE_REQUEST [1]", "EXPORT_GATE_REQUEST not json", "CHECKPOINT built3 g1 c8",
               "CHECKPOINT stale g1 c9 tail", "CHECKPOINT stale g2 c9", "CHECKPOINT stale g1 c2", "ANYTHING ELSE", ""]
        for line in bad:
            refuse(ValueError, PR.parse_request, line, "g1", seen)
        assert seen == {"c1", "c2"}

    def test_child_limits_derive_from_the_parent_remainder_and_only_shorten(self):
        clock, p = make(work=900)
        first = PR.child_limits(p, 1_000_000, 120)
        assert first == {"generation": "g1", "deadlineAtMs": 1_900_000, "workMs": 900_000, "cleanupAtMs": 2_020_000, "cleanupMs": 120_000}
        clock.now = 300
        later = PR.child_limits(p, 1_300_000, 120)  # the same absolute cutoff and a smaller relative budget: a late child is never given more
        assert later["deadlineAtMs"] == first["deadlineAtMs"] and later["workMs"] == 600_000
        clock.now = 899.9996  # sub-millisecond remainder: nothing is handed over
        refuse(PR.Deadline, PR.child_limits, p, 0, 120)

    @pytest.mark.parametrize("variant", ("confirmed", "missing", "wrong-bytes", "exit-unknown", "exit-nonzero", "teardown-failed", "self-save-claim", "readback-failed", "late-write", "late-readback"))
    def test_parent_acceptance_needs_independent_child_bytes_exit_teardown_and_a_separate_readback(self, scratch, variant):
        clock, p = make(work=10, cleanup=60)
        teardown = {"contextClose": "OK", "stdinDestroy": "FAILED: boom" if variant == "teardown-failed" else "OK"}
        if variant == "self-save-claim":  # a snapshot asserting its own save is not evidence; the missing teardown outcome still blocks it
            teardown = {"contextClose": "OK"}
        snap = json.dumps({"partial": False, "teardown": teardown, **({"saved": True} if variant == "self-save-claim" else {})}).encode()
        claim = f"{E.sha(snap)} {len(snap)}" if variant != "wrong-bytes" else f"{'0' * 64} {len(snap)}"
        code = {"exit-unknown": None, "exit-nonzero": 3}.get(variant, 0)
        read = (lambda: snap) if variant != "missing" else raising(FileNotFoundError("gone"))
        saved = {}
        def persist(raw):
            saved["raw"] = raw
            if variant == "late-write":
                clock.now = 61
        def readback():
            if variant == "late-readback":
                clock.now = 61
            return saved["raw"]
        ops = types.SimpleNamespace(stage=scratch, container=None, container_identity_pending=False, prepare_kill=lambda: [], remove_container=lambda: None,
                                    query_processes=lambda: set(), query_containers=lambda: set(), members=lambda: [], listeners=lambda: [],
                                    verify_disposal_target=lambda: True, close=lambda: None)
        out = E.finalize(ops, [], E.Collector(scratch, proto=p), child_required=True, child=lambda: L.child_evidence(read, code, claim),
                         persist=persist, read_back=raising(OSError("gone")) if variant == "readback-failed" else readback)
        assert out["accepted"] is (variant == "confirmed") and out["disposalEligible"] is (variant == "confirmed")
        assert out["stageRetained"] is True and out["actualDisposal"] == "NOT_ATTEMPTED" and Path(scratch).exists()
        if variant != "confirmed":
            assert out["evidence"]["child"]["confirmed"] is False or variant in ("readback-failed", "late-write", "late-readback")
            assert out["acknowledgment"]["readBack"] == {"readback-failed": "UNAVAILABLE", "late-write": "NOT_ATTEMPTED", "late-readback": "UNKNOWN"}.get(variant, "MATCH")


def test_retained_handle_stop_ignores_reused_pid_and_refuses_nonmember_handle(scratch):
    calls, identity = [], {"pid": 9, "creation100ns": 1, "image": "owned"}
    ops = L.Native.__new__(L.Native)
    ops.c, ops.retained, ops.roots, ops.job = E.Collector(scratch), {9: 55}, [], 7
    def identify(pid, handle=None):
        calls.append(("identity", handle))
        return identity if handle == 55 else {**identity, "creation100ns": 2}
    ops.api = types.SimpleNamespace(exited=lambda h: False, identity=identify,
        terminate=lambda h: calls.append(("terminate", h)), members=lambda j: [9],
        open=lambda pid: 66, in_job=lambda h, j: False)
    ops.kill(identity)
    assert calls == [("identity", 55), ("terminate", 55)] and ops.c.events == []
    with pytest.raises(RuntimeError, match="not a member"):
        ops.prepare_kill()
    assert calls == [("identity", 55), ("terminate", 55)]


def raising(error):
    def runner(*_args, **_kw):
        raise error
    return runner


class Ops:
    """Recording terminal ops whose first step consumes the whole cleanup remainder."""
    container, container_identity_pending = None, False

    def __init__(self, clock, stage):
        self.calls, self.clock, self.stage = [], clock, stage
        stage.mkdir(parents=True)

    def prepare_kill(self):
        self.calls.append("prepare_kill")
        self.clock.now += 6
        return []

    def __getattr__(self, name):
        return lambda *a, **k: self.calls.append(name) or ([] if name in ("members", "listeners") else set() if name.startswith("query") else True)


def test_first_cleanup_step_consuming_the_remainder_leaves_every_later_step_not_attempted(scratch):
    clock, p = make(work=10, cleanup=5)
    ops, written = Ops(clock, scratch / "source"), []
    out = E.finalize(ops, [], E.Collector(scratch, proto=p), persist=written.append, read_back=lambda: b"")
    actions = {a["action"]: a["outcome"] for a in out["evidence"]["actions"]}
    assert ops.calls == ["prepare_kill"] and written == []  # no floor, no timeout 0, no replenished window
    assert actions["identity"] == "CONFIRMED" and {actions[k] for k in ("tasklist", "docker-ps", "disposal-target", "handle-close")} == {"NOT_ATTEMPTED"}
    assert out["acknowledgment"] == {"write": "NOT_ATTEMPTED", "readBack": "NOT_ATTEMPTED", "error": None} and not out["accepted"] and out["stageRetained"] is True
    assert out["evidence"]["preAckDisposition"] == E.UNKNOWN and any("NOT_ATTEMPTED" in e for e in out["evidence"]["errors"])
