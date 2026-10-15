"""Parent protocol owner: phase, immutable work cutoff, one separate cleanup cutoff, atomic operation admission and pending accounting."""
from __future__ import annotations

import itertools
import json
import math
import re
import secrets
import threading
import time

PREPARED, WORK, CLOSING, CLEANUP, FROZEN = "PREPARED", "WORK", "CLOSING", "CLEANUP", "TERMINAL_FROZEN"
QUEUED, REVOKED, DISPATCHED, DONE, FAILED = "QUEUED", "REVOKED", "DISPATCHED", "DONE", "FAILED"
BODY_LIMIT, BODY_CHUNK = 64 * 1024, 8192
CHECKPOINT = re.compile(r"CHECKPOINT (stale|built[12]) (g[0-9a-f]{1,16}) (c[0-9]{1,6})")
OPERATION = re.compile(r"c[0-9]{1,6}")
REQUEST_KEYS = {"n", "op", "generation", "external", "aiPosts"}


class Stop(Exception):
    """Non-retryable stop: cutoff reached, admission refused, wait bound missed or budget exhausted."""


class Deadline(Stop):
    """No positive finite wait remains before the governing cutoff."""


class NotAdmitted(Stop):
    """The phase no longer admits this operation (revoked, fenced or frozen)."""


class WaitBound(Stop):
    """A wait bound was missed. The call was NOT preempted: its outcome is UNKNOWN."""


def bounded_call(label, fn, seconds):
    """Wait bound for an uninterruptible call. Nothing is started without a positive wait; a missed bound is UNKNOWN, never preemption."""
    if not seconds > 0:
        raise Deadline(f"{label}: no remainder; nothing started")
    box = {}

    def target():
        try:
            box["value"] = fn()
        except BaseException as error:
            box["error"] = error
    worker = threading.Thread(target=target, daemon=True)
    worker.start()
    worker.join(seconds)
    if worker.is_alive():
        raise WaitBound(f"{label}: no completion within {seconds:.2f}s; outcome UNKNOWN")
    if "error" in box:
        raise box["error"]
    return box.get("value")


class Op:
    """One tracked effect. QUEUED is revocable; DISPATCHED is committed and stays tracked even before its adapter is entered."""
    def __init__(self, ident, kind, cleanup):
        self.id, self.kind, self.cleanup, self.state = ident, kind, cleanup, QUEUED
        self.inflight_at_close, self.outcome = False, None

    def record(self):
        return {"id": self.id, "kind": self.kind, "cleanup": self.cleanup, "state": self.state, "outcome": self.outcome,
                "inflightAtClose": self.inflight_at_close, "uncertain": self.state == DISPATCHED or self.inflight_at_close}


class Protocol:
    """Single monotonic owner. The admission lock guards state only and is never held across blocking I/O or an adapter call."""
    def __init__(self, clock=time.monotonic, work=900, cleanup=120, generation=None):
        self.clock, self.work, self.cleanup = clock, work, cleanup
        self.generation = generation or "g" + secrets.token_hex(4)
        self.lock, self.ids, self.scope = threading.RLock(), itertools.count(1), threading.local()
        self.state, self.work_end, self.cleanup_end, self.closed_by = PREPARED, None, None, None
        self.ops, self.late = [], []

    def scoped(self, fn):
        """Wrap a cleanup action: only code running inside this scope may queue operations after the fence (cleanup-class). Normal work
        from any other thread is refused at queue time, so a late handler or reply can never be admitted as 'cleanup'."""
        def run():
            self.scope.on = True
            try:
                return fn()
            finally:
                self.scope.on = False
        return run

    def start(self):
        with self.lock:
            if self.state != PREPARED:
                raise RuntimeError("protocol already started")
            self.work_end, self.state = self.clock() + self.work, WORK
        return self

    def _close(self, now, reason):
        """Irreversible fence (caller holds the lock). workEnd is never rewritten; cleanupEnd is fixed exactly once."""
        if self.state not in (PREPARED, WORK):
            return
        self.work_end = now if self.work_end is None else self.work_end
        self.state, self.closed_by = CLOSING, reason
        self.cleanup_end = min(now + self.cleanup, self.work_end + self.cleanup)
        for op in self.ops:
            if op.state == QUEUED and not op.cleanup:
                op.state = REVOKED  # queued normal work is revoked before any wait
            elif op.state == DISPATCHED and not op.cleanup:
                op.inflight_at_close = True  # committed work cannot be proven stopped

    def _tick(self, now):
        if self.state == WORK and now >= self.work_end:
            self._close(now, "WORK_EXPIRED")

    def close(self, reason="CLOSED"):
        with self.lock:
            self._close(self.clock(), reason)

    def begin_cleanup(self):
        with self.lock:
            if self.state == CLOSING:
                self.state = CLEANUP

    @staticmethod
    def _wait(remaining, requested, unit=None):
        """Finite strictly positive wait no greater than the request or the remainder; integer-unit adapters quantize DOWN."""
        wait = min(requested, remaining)
        wait = math.floor(wait / unit) * unit if unit and math.isfinite(wait) else wait
        return wait if math.isfinite(wait) and wait > 0 else None

    def queue(self, kind):
        with self.lock:
            cleanup = self.state != WORK and getattr(self.scope, "on", False)
            if self.state in (PREPARED, FROZEN) or (self.state != WORK and not cleanup):
                raise NotAdmitted(f"{kind}: protocol is {self.state}; no new normal work")
            op = Op(next(self.ids), kind, cleanup)
            self.ops.append(op)
            return op

    def grant(self, op, requested, unit=None):
        """Atomic QUEUED -> DISPATCHED against the operation's own cutoff, with one clock sample. The caller runs the adapter AFTER this
        returns; a refusal means the adapter is never called."""
        with self.lock:
            now = self.clock()
            self._tick(now)
            in_phase = self.state in (CLOSING, CLEANUP) if op.cleanup else self.state == WORK
            if op.state != QUEUED or not in_phase:
                op.state = REVOKED if op.state == QUEUED else op.state
                raise NotAdmitted(f"{op.kind}: {op.state} in phase {self.state}; adapter not called")
            wait = self._wait((self.cleanup_end if op.cleanup else self.work_end) - now, requested, unit)
            if wait is None:
                op.state = REVOKED
                raise Deadline(f"{op.kind}: no positive wait remains; adapter not called")
            op.state = DISPATCHED
            return wait

    def left(self, requested, work_only=False):
        """Fresh finite wait for a step inside an admitted operation or cleanup action; 0.0 means invoke nothing new (no floor, no timeout0)."""
        with self.lock:
            now = self.clock()
            self._tick(now)
            end = self.work_end if work_only or self.state == WORK else self.cleanup_end if self.state in (CLOSING, CLEANUP) else None
            return 0.0 if end is None else self._wait(end - now, requested) or 0.0

    def check(self, op=None):
        """Fresh phase/time recheck of an already granted operation, e.g. after persistence and before a child resumes."""
        with self.lock:
            now = self.clock()
            self._tick(now)
            cleanup = bool(op and op.cleanup)
            if (self.state not in (CLOSING, CLEANUP)) if cleanup else (self.state != WORK):
                raise NotAdmitted(f"phase {self.state} no longer admits this operation")
            remaining = (self.cleanup_end if cleanup else self.work_end) - now
            if remaining <= 0:
                raise Deadline("cutoff reached")
            return remaining

    def complete(self, op, ok=True, outcome=None):
        with self.lock:
            if self.state == FROZEN:  # a late completion never rewrites frozen outcomes or clears uncertainty
                self.late.append({"id": op.id, "kind": op.kind, "ok": ok, "outcome": outcome})
            else:
                op.state, op.outcome = (DONE if ok else FAILED), outcome

    def timed_out(self, op):
        with self.lock:
            op.outcome = "WAIT_BOUND_MISSED"  # state stays DISPATCHED: the call may still be running

    def snapshot(self):
        with self.lock:
            return {"generation": self.generation, "phase": self.state, "closedBy": self.closed_by, "workSeconds": self.work,
                    "cleanupSeconds": self.cleanup, "operations": [op.record() for op in self.ops]}

    def freeze(self):
        with self.lock:
            snap = self.snapshot()
            self.state = FROZEN
            return snap


def run_op(proto, kind, fn, requested, *, unit=None, bounded=False):
    """Queue, atomic grant, then the adapter outside the lock with its finite wait. fn receives that wait."""
    op = proto.queue(kind)
    wait = proto.grant(op, requested, unit)
    try:
        value = bounded_call(kind, lambda: fn(wait), wait) if bounded else fn(wait)
    except WaitBound:
        proto.timed_out(op)
        raise
    except BaseException as error:
        proto.complete(op, False, type(error).__name__)
        raise
    proto.complete(op)
    return value


def read_body(rfile, raw_length, proto, arm=None):
    """Bounded request body. An invalid or oversized Content-Length is refused before any read; every chunk waits at most the remainder of
    the ORIGINAL work cutoff. The read is a tracked operation: a close while it is pending leaves it uncertain even after it returns."""
    if not isinstance(raw_length, str) or not re.fullmatch(r"[0-9]{1,6}", raw_length) or not 0 < int(raw_length) <= BODY_LIMIT:
        raise ValueError("invalid or oversized Content-Length refused before any read")
    need, parts, op = int(raw_length), [], proto.queue("body-read")
    proto.grant(op, 1)
    try:
        while need:
            wait = proto.left(2, work_only=True)
            if wait <= 0:
                proto.timed_out(op)
                raise Deadline("body-read: work cutoff reached; outcome UNKNOWN")
            if arm:
                arm(wait)
            chunk = rfile.read(min(BODY_CHUNK, need))
            if not chunk:
                raise ValueError("body ended before Content-Length")
            parts.append(chunk)
            need -= len(chunk)
    except Deadline:
        raise
    except BaseException as error:
        proto.complete(op, False, type(error).__name__)
        raise
    proto.left(1)  # sample the cutoff while the read is still committed: expiry during the read leaves it uncertain
    proto.complete(op)
    return b"".join(parts)


def child_limits(proto, wall_ms, cleanup_seconds):
    """Advisory child limits derived from the parent's own remainder: absolute epoch cutoffs plus relative budgets. The child may only
    shorten what it waits; its startup delay or a wall-clock rollback can never extend parent authority."""
    work_ms = math.floor(proto.left(proto.work, work_only=True) * 1000)
    if work_ms < 1:
        raise Deadline("no work time left to hand to the child")
    cleanup_ms = int(cleanup_seconds * 1000)
    return {"generation": proto.generation, "deadlineAtMs": wall_ms + work_ms, "workMs": work_ms,
            "cleanupAtMs": wall_ms + work_ms + cleanup_ms, "cleanupMs": cleanup_ms}


def reply(kind, arg, generation, op):
    """Complete parent reply: kind, argument, this run's generation and the request's operation id. The child compares the whole line."""
    return f"{kind} {arg} {generation} {op}"


def parse_request(line, generation, seen):
    """Strict parent-side parse of one child request: exact shape, this generation and a fresh operation id. Returns (reply kind, arg, op, payload)."""
    if line.startswith("EXPORT_GATE_REQUEST "):
        body = json.loads(line.split(" ", 1)[1])
        valid = (type(body) is dict and set(body) == REQUEST_KEYS and type(body["n"]) is int and body["n"] in (1, 2)
                 and type(body["op"]) is str and OPERATION.fullmatch(body["op"]) and body["generation"] == generation)
        kind, arg, op, payload = "EXPORT_GATE_OK", valid and body["n"], valid and body["op"], body
    else:
        found = CHECKPOINT.fullmatch(line)
        valid = bool(found) and found.group(2) == generation
        kind, arg, op, payload = "CHECKPOINT_OK", valid and found.group(1), valid and found.group(3), None
    if not valid or op in seen:
        raise ValueError("unknown, stale, wrong-generation or replayed browser controller output")
    seen.add(op)
    return kind, arg, op, payload
