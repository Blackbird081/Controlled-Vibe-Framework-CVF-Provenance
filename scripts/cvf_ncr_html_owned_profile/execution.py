"""One execution owner: safe evidence, protocol-admitted bounded commands, budgets and immutable retained-stage terminal evidence."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import threading
import time
from contextlib import suppress
from pathlib import Path

from .protocol import Deadline, Protocol, Stop, WaitBound, bounded_call, run_op

ACCEPTED, UNKNOWN = "ACCEPTED_RETAINED_STAGE_EVIDENCE", "NOT_ACCEPTED_UNKNOWN"
ONE_SHOT = frozenset({"installed-browser-path"})  # a failed module-path query is never retried or replaced
DRAIN_SECONDS, NATIVE_SECONDS, PERSIST_SECONDS = 2, 15, 10
KEY = r"(?:authorization|bearer|cookie|credential|passwd|password|pwd|secret|token|api[-_]?key|access[-_]?key|private[-_]?key|session)"
SCHEME = r"(?:(?:bearer|basic|digest|token)\s+)?"
# Quoted value, plain or JSON-escaped at any depth, taken whole: the closing quote has the opening backslash run and no extra escape.
QUOTED = (r"""(?P<qd>\\*)"(?:(?!(?<!\\)(?P=qd)").)*(?<!\\)(?P=qd)"|(?P<qs>\\*)'(?:(?!(?<!\\)(?P=qs)').)*(?<!\\)(?P=qs)'""")
BARE = r"""(?:\\*["'])?""" + SCHEME + r"""[^\s,;&}\]"']+"""  # unquoted, or an unterminated quote
# An unclosed recognized quoted value is ambiguous: consume its whole tail, never just its first word.
UNCLOSED = (r"""(?P<ud>\\*)"(?:(?!(?<!\\)(?P=ud)").)*$|(?P<us>\\*)'(?:(?!(?<!\\)(?P=us)').)*$""")
VALUE = r"(?!\[REDACTED\])(?:" + SCHEME + "(?:" + QUOTED + "|" + UNCLOSED + ")|" + BARE + ")"
PAIR = re.compile(r"(?is)(\b[\w.-]*" + KEY + r"[\w.-]*(?:\\*[\"'])?\s*[=:]\s*)" + VALUE)
FLAG = re.compile(r"(?is)((?:^|[\s\"'\\])(?:--?|/)[\w-]*" + KEY + r"[\w-]*(?:\s*[=:]\s*|\s+))" + VALUE)
BEARER = re.compile(r"(?is)(\bbearer\s+)(?!\[REDACTED\])(?:" + QUOTED + "|" + UNCLOSED + r"|[^\s,;&}\]\"']+)")
BARE_FLAG = re.compile(r"(?i)(?:(?:--?|/)[\w-]*" + KEY + r"[\w-]*|bearer|authorization:?)")
TRUNCATED = re.compile(r"\.\.\.\[truncated \d+\]$")


def sha(raw): return hashlib.sha256(raw).hexdigest()


def text_of(raw): return raw.decode("utf-8", "replace") if isinstance(raw, (bytes, bytearray)) else "" if raw is None else str(raw)


def redact(text):
    """Recognized bearer values and values after sensitive names in `name=value`, `"name": "value"`, `--flag value` and `/flag:value` forms,
    quoted, escaped or adjacent. A recognized field with an ambiguous value is redacted as a whole."""
    for pattern in (PAIR, FLAG):
        text = pattern.sub(lambda m: m.group(1) + "[REDACTED]", text)
    return BEARER.sub(lambda m: m.group(1) + "[REDACTED]", text)


class Safe(str):
    """Text that already passed redaction and bounding; serializers pass it through untouched."""


def bounded(raw, limit=2000):
    """Redact first and truncate second, so a cut can never expose part of a secret; bytes and text are treated alike. Idempotent."""
    text = redact(text_of(raw))
    if len(text) <= limit or TRUNCATED.search(text) and len(text) <= limit + 32:
        return Safe(text)
    return Safe(text[:limit] + f"...[truncated {len(text) - limit}]")


def argv_evidence(argv):
    """Executable basename plus bounded redacted arguments; a bare sensitive flag hides its adjacent value."""
    items, args, hide = [text_of(a) for a in argv], [], False
    for item in items[1:13]:
        args.append("[REDACTED]" if hide else bounded(item, 160))
        hide = bool(BARE_FLAG.fullmatch(item.strip()))
    return {"executable": re.split(r"[\\/]", items[0])[-1] if items else "", "args": args, "argc": len(items)}


def safe(value, depth=0):
    """JSON-safe, redacted, bounded evidence for command events, process records and exceptions."""
    if depth > 12:
        return "[DEPTH]"
    if value is None or isinstance(value, (bool, int, float, Safe)):
        return value
    if isinstance(value, BaseException):
        return f"{type(value).__name__}: {bounded(str(value), 180)}"
    if isinstance(value, dict):
        return {str(k): "[REDACTED]" if v is not None and re.search(KEY, str(k), re.I) else safe(v, depth + 1) for k, v in list(value.items())[:128]}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [safe(v, depth + 1) for v in list(value)[:128]]
    return bounded(value)


def dumps(value):
    return json.dumps(safe(value), sort_keys=True, indent=2).encode("utf-8")


def completion(returncode):
    """Only a real int 0 is success; bool, None or any malformed value is UNKNOWN completion."""
    return "UNKNOWN" if type(returncode) is not int else "SUCCESS" if returncode == 0 else "NONZERO_EXIT"


class BudgetExhausted(Stop):
    """Charged readiness budget exhausted."""


class CommandFailure(RuntimeError):
    def __init__(self, kind, failure_class, persist_error=None):
        super().__init__(f"{kind}: {failure_class}; evidence retained")
        self.kind, self.failure_class, self.persist_error = kind, failure_class, persist_error


class Collector:
    """Single owner of persisted, secret-safe command evidence. Every launch takes the parent protocol's final atomic admission AFTER its
    prelaunch persistence, so the runner never sees a stale wait, an expired invocation or a revoked operation."""
    def __init__(self, custody: Path, runner=None, proto=None, sleeper=None):
        self.custody, self.runner, self.events = custody, runner or subprocess.run, []
        self.proto, self.sleeper = proto or Protocol().start(), sleeper or time.sleep
        self.lock, self.local = threading.RLock(), threading.local()
        self.cleanup_errors = []

    def current_op(self):
        return getattr(self.local, "op", None)

    def op(self, kind, fn, requested, **kw):
        return run_op(self.proto, kind, fn, requested, **kw)

    def sleep(self, seconds):
        wait = self.proto.left(seconds, work_only=True)
        if wait <= 0:
            raise Deadline("sleep: work cutoff reached")
        self.sleeper(wait)

    def command(self, kind, argv, *, timeout=10, data=None, parse=None):
        """Persist prelaunch evidence, take the final admission with a fresh finite wait, launch once, classify; never retry or fall back."""
        if kind in ONE_SHOT and any(e["kind"] == kind for e in self.events):
            raise CommandFailure(kind, "REPEAT_REFUSED")
        op, started = self.proto.queue(kind), self.proto.clock()
        with self.lock:
            event = {"seq": len(self.events) + 1, "kind": kind, **argv_evidence(argv), "inputBytes": len(data or ""), "startedAt": started,
                     "timeoutSeconds": None, "state": "QUEUED", "failureClass": None, "exitCode": None, "stdout": "", "stderr": "", "timedOut": False}
            self.events.append(event)
            try:
                self.save(kind, unlaunched=True)  # may block; a failed prelaunch write prevents the invocation
            except CommandFailure:
                self.proto.complete(op, False, "PERSIST")
                raise
        try:
            wait = self.proto.grant(op, timeout)  # fresh phase and time after persistence; QUEUED -> DISPATCHED under the parent lock
        except Stop as error:
            with suppress(CommandFailure):
                self.finish(kind, event, {"stderr": bounded(repr(error))}, "REFUSED")
            raise
        with self.lock:
            event.update(state="STARTED", timeoutSeconds=wait)
        fields, stdout, result, failure, stop, unresolved = {}, "", None, None, None, False
        self.local.op = op
        try:
            p = self.runner(list(argv), input=data, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=wait)
            stdout, code = p.stdout or "", getattr(p, "returncode", None)
            fields = {"exitCode": code if type(code) is int else None, "stdout": bounded(stdout), "stderr": bounded(p.stderr)}
            failure = None if completion(code) == "SUCCESS" else completion(code)
        except subprocess.TimeoutExpired as error:
            fields, failure, unresolved = {"stdout": bounded(error.stdout), "stderr": bounded(error.stderr), "timedOut": True}, "TIMEOUT", getattr(error, "drained", True) is False
            fields["cleanupError"] = getattr(error, "cleanup_error", None)
        except Stop as error:  # the cutoff passed inside the runner: finish the evidence, then keep stopping
            fields, failure, stop = {"stderr": bounded(repr(error))}, "DEADLINE", error
        except Exception as error:
            fields, failure = {"stderr": bounded(repr(error))}, "SPAWN" if isinstance(error, OSError) else "UNKNOWN"
        finally:
            self.local.op = None
        if parse and failure is None:
            try:
                result = parse(stdout)
            except Exception as error:
                fields["parseError"], failure = bounded(repr(error), 200), "PARSE"
        if unresolved:  # the child was told to stop but its exit was not observed: the operation stays UNKNOWN and tracked
            self.proto.timed_out(op)
        else:
            self.proto.complete(op, failure is None, failure)
        self.finish(kind, event, fields, failure)
        if stop:
            raise stop
        if failure:
            raise CommandFailure(kind, failure)
        return stdout if parse is None else result

    def finish(self, kind, event, fields, failure):
        with self.lock:
            event.update(fields, state="NOT_LAUNCHED" if failure == "REFUSED" else "FINISHED", failureClass=failure,
                         elapsedSeconds=round(self.proto.clock() - event["startedAt"], 4))
            try:
                self.save(kind)
            except CommandFailure as persisted:
                if failure:  # the original command failure stays the primary evidence
                    raise CommandFailure(kind, failure, persist_error=persisted.failure_class) from None
                raise

    def save(self, kind, unlaunched=False):
        try:
            self.custody.mkdir(parents=True, exist_ok=True)
            (self.custody / "commands.json").write_bytes(dumps(self.events))
        except (OSError, TypeError, ValueError) as error:
            if unlaunched:
                self.events.pop()  # nothing was launched, so nothing is lost
            raise CommandFailure(kind, "PERSIST") from error


def bounded_communicate(p, c, data=None, timeout=None):
    """communicate() with the granted wait; after a timeout kill this exact child and drain only for the remaining finite wait of ITS OWN
    class (a work command never borrows cleanup time). No floor, no unbounded fallback: output that stays unresolved is unknown."""
    op = None if c is None else c.current_op()
    requested = 10 if timeout is None else timeout
    wait = requested if c is None else min(requested, c.proto.check(op))
    if not wait > 0:
        raise Deadline("communicate: no positive wait; nothing started")
    left = lambda: DRAIN_SECONDS if c is None else c.proto.left(DRAIN_SECONDS, work_only=not (op and op.cleanup))
    try:
        return p.communicate(data, timeout=wait)
    except subprocess.TimeoutExpired as error:
        error.drained = False  # no exit observation: preserve UNKNOWN, even if cancellation was requested
        try:
            if left() > 0:
                p.kill()  # exact creation handle; no newly admitted cancellation after this operation's cutoff
                drain = left()  # kill may itself consume time; never reuse the pre-kill remainder
                if drain > 0:
                    error.stdout, error.stderr = p.communicate(timeout=drain)
                    error.drained = True
        except Exception as cleanup:
            error.cleanup_error = bounded(repr(cleanup), 180)  # original timeout and unresolved child remain primary
        raise


class Budget:
    """Readiness GETs: engine/Web/route buckets inside one global cap; no transfer between buckets or actors."""
    LIMITS, GLOBAL = {"engine": 4, "web": 6, "route": 2}, 12

    def __init__(self, actor):
        self.actor, self.used = actor, dict.fromkeys(self.LIMITS, 0)

    def debit(self, bucket):
        if bucket not in self.LIMITS or self.used[bucket] >= self.LIMITS[bucket] or sum(self.used.values()) >= self.GLOBAL:
            raise BudgetExhausted(f"{self.actor} {bucket} readiness budget exhausted")
        self.used[bucket] += 1


def poll(c, budget, bucket, attempt, tries, delay):
    """Debit before each attempted request, including failures; sleeps are clamped to the work cutoff."""
    for index in range(tries):
        budget.debit(bucket)
        try:
            if attempt():
                return
        except Stop:
            raise
        except (RuntimeError, ValueError, OSError):
            pass
        if index + 1 < tries:
            c.sleep(delay)
    raise RuntimeError(f"{bucket} readiness not reached within its charged budget")


def finalize(ops, failures, c, *, stage=None, before=(), after=(), child=None, child_required=False, persist=None, read_back=None):
    """Retained-stage terminal boundary. The fence closes first; every cleanup action then gets a fresh finite wait from the single cleanup
    remainder and is recorded CONFIRMED, FAILED, UNKNOWN or NOT_ATTEMPTED. Evidence is frozen once, written, read back and acknowledged
    separately. Nothing here removes the stage; disposal eligibility is modeled only."""
    proto = c.proto
    proto.close("TERMINAL")
    proto.begin_cleanup()
    ev = {"errors": list(c.cleanup_errors), "actions": [], "primaryFailures": [safe(f) for f in failures], "ownedIdentities": [], "processQuery": "UNKNOWN",
          "containerQuery": "UNKNOWN", "descendantQuery": "UNKNOWN", "listenerQuery": "UNKNOWN", "disposalTarget": "UNKNOWN", "stageRetained": None,
          "child": {"confirmed": not child_required, "reason": "NOT_LAUNCHED"}}
    if getattr(ops, "container_identity_pending", False):
        ev["errors"].append("container identity unresolved after creation attempt; preserve stage")

    def attempt(label, fn, wait=DRAIN_SECONDS):
        left, outcome, value = proto.left(wait), "CONFIRMED", None
        if left <= 0:
            outcome, detail = "NOT_ATTEMPTED", "NOT_ATTEMPTED: cleanup remainder exhausted"
        else:
            try:
                value = bounded_call(label, proto.scoped(fn), left)
            except WaitBound as error:
                outcome, detail = "UNKNOWN", f"WaitBound: {bounded(error, 180)}"
            except Exception as error:
                outcome, detail = "FAILED", f"{type(error).__name__}: {bounded(error, 180)}"
        ev["actions"].append({"action": label, "outcome": outcome})
        if outcome != "CONFIRMED":
            ev["errors"].append(f"{label}: {detail}")
        return value
    for label, fn in before:
        attempt(label, fn)
    if child:
        ev["child"] = attempt("child-evidence", child, NATIVE_SECONDS) or {"confirmed": False, "reason": "UNRESOLVED"}
    if ops is not None:
        identities = attempt("identity", ops.prepare_kill, NATIVE_SECONDS)
        if identities is not None:
            ev["ownedIdentities"] = identities
            for identity in reversed(identities):  # legacy action label; Native.kill stops its pinned owned handle, not a PID utility
                attempt("taskkill", lambda x=identity: ops.kill(x), NATIVE_SECONDS)
        attempt("container-remove", ops.remove_container, NATIVE_SECONDS)
        pids, containers, members, listeners = (attempt("tasklist", ops.query_processes, NATIVE_SECONDS), attempt("docker-ps", ops.query_containers, NATIVE_SECONDS),
                                                attempt("descendants", ops.members), attempt("listeners", ops.listeners, NATIVE_SECONDS))
        if pids is not None:
            ev["processQuery"] = "LIVE" if set(pids) & {x["pid"] for x in ev["ownedIdentities"]} else "ABSENT"
        if containers is not None and not getattr(ops, "container_identity_pending", False):
            ev["containerQuery"] = "LIVE" if ops.container in containers else "ABSENT"
        if members is not None:
            ev["descendantQuery"] = "LIVE" if members else "ABSENT"
        if listeners is not None:
            ev["listenerQuery"] = "LIVE" if listeners else "ABSENT"
        for label, fn in after:  # reader joins and log closes follow native stop; any error still prevents eligibility
            attempt(label, fn)
        ev["disposalTarget"] = "SAFE" if attempt("disposal-target", ops.verify_disposal_target) else "UNSAFE_OR_UNKNOWN"
        attempt("handle-close", ops.close)
    stage_path = getattr(ops, "stage", stage)
    ev["stageRetained"] = None if stage_path is None else Path(stage_path).exists()
    ev["protocol"] = proto.snapshot()
    ev["uncertainOperations"] = [o["id"] for o in ev["protocol"]["operations"] if o["uncertain"]]
    queries = [ev[k] for k in ("processQuery", "containerQuery", "descendantQuery", "listenerQuery")]
    if ops is None:
        ev["preAckDisposition"] = UNKNOWN if ev["errors"] or ev["uncertainOperations"] else "NOT_STARTED_NO_NATIVE_RESOURCES"
    else:
        clean = (not failures and not ev["errors"] and all(q == "ABSENT" for q in queries) and ev["stageRetained"] and ev["disposalTarget"] == "SAFE"
                 and not ev["uncertainOperations"] and ev["child"].get("confirmed") is True)
        ev["preAckDisposition"] = ACCEPTED if clean else UNKNOWN
    raw = dumps(ev)  # frozen once; the acknowledgment below is a separate record, never a mutation of these bytes
    ack = {"write": "NOT_ATTEMPTED", "readBack": "NOT_ATTEMPTED", "error": None}

    def step(label, fn):
        wait = proto.left(PERSIST_SECONDS)
        if wait <= 0:
            return "NOT_ATTEMPTED", None
        value = bounded_call(label, fn, wait)
        if proto.left(PERSIST_SECONDS) <= 0:
            raise WaitBound(f"{label}: completion observed after cleanup cutoff; outcome UNKNOWN")
        return "OK", value
    if persist:
        try:
            ack["write"] = "ACKNOWLEDGED" if step("terminal-write", lambda: persist(raw))[0] == "OK" else "NOT_ATTEMPTED"
        except WaitBound as error:
            ack.update(write="UNKNOWN", error=str(bounded(error, 180)))
        except Exception as error:
            ack.update(write="FAILED", error=f"{type(error).__name__}: {bounded(error, 180)}")
        if read_back and ack["write"] != "FAILED":
            try:
                state, data = step("terminal-readback", read_back)
                ack["readBack"] = "NOT_ATTEMPTED" if state != "OK" else "MATCH" if data == raw else "MISMATCH"
            except WaitBound as error:
                ack.update(readBack="UNKNOWN", error=ack["error"] or str(bounded(error, 180)))
            except Exception as error:
                ack.update(readBack="UNAVAILABLE", error=ack["error"] or f"{type(error).__name__}: {bounded(error, 180)}")
    proto.freeze()  # later completions are recorded as late and never rewrite these outcomes
    accepted = ev["preAckDisposition"] == ACCEPTED and ack["write"] == "ACKNOWLEDGED" and ack["readBack"] == "MATCH"
    return {"evidence": json.loads(raw), "evidenceSha256": sha(raw), "evidenceBytes": len(raw), "acknowledgment": ack, "accepted": accepted,
            "disposalEligible": accepted and ev["disposalTarget"] == "SAFE", "stageRetained": ev["stageRetained"], "actualDisposal": "NOT_ATTEMPTED"}
