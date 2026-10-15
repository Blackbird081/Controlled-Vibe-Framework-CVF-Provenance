"""Owned Windows process identities, exact handle ownership and the native half of the retained-stage terminal boundary."""
from __future__ import annotations

import csv
import ctypes as C
import io
import json
import os
import re
import subprocess
from contextlib import contextmanager, nullcontext, suppress
from ctypes import wintypes as W
from pathlib import Path

from .execution import argv_evidence, bounded, bounded_communicate, completion, dumps, sha

JOB_LIMIT, ACTIVE, BREAKAWAY, SILENT, KILL_CLOSE, EXTENDED = 32, 0x8, 0x800, 0x1000, 0x2000, 9


def parse_tasklist(raw):
    rows = list(csv.reader(io.StringIO(raw)))
    if not rows or any(len(r) != 5 or not r[1].isdigit() for r in rows):
        raise RuntimeError("tasklist query was malformed, not proof of absence")
    return {int(r[1]) for r in rows}


def parse_docker_ids(raw):
    rows = raw.splitlines()
    if any(not re.fullmatch(r"[a-f0-9]{64}", r) for r in rows):
        raise RuntimeError("Docker query was malformed, not proof of absence")
    return set(rows)


def no_reparse(path: Path):
    if path.is_symlink() or (path.exists() and getattr(path.lstat(), "st_file_attributes", 0) & 0x400):
        raise RuntimeError(f"reparse path refused: {path.name}")


def check_disposable(stage: Path, namespace: Path, dependency=None):
    """Modeled disposal eligibility only: verify the exact target and the dependency link identity. Nothing is ever deleted here;
    actual deletion is a separate future admitted action that must cite accepted terminal evidence."""
    no_reparse(namespace)
    no_reparse(stage)
    if stage.resolve() != namespace.resolve() / "source" or not (namespace / "owner.json").is_file():
        raise RuntimeError("unsafe disposal target")
    link = None
    if dependency:
        link, target = dependency
        if link.exists() and (link.resolve() != target.resolve() or not link.is_relative_to(stage)):
            raise RuntimeError("dependency link identity changed")
    for base, dirs, files in os.walk(stage, followlinks=False):
        for name in dirs + files:
            if Path(base) / name != link:  # the one admitted junction is identity-checked above and never traversed
                no_reparse(Path(base) / name)
    return True


def child_evidence(read, exit_code, claim):
    """Parent-side verification of the child's saved snapshot: bytes and hash recomputed here, exit independently observed. The child's
    stdout claim is only compared, never trusted, and a snapshot never certifies its own save."""
    ev = {"confirmed": False, "exit": completion(exit_code), "snapshot": "MISSING", "claimMatch": False, "teardown": None}
    try:
        raw = read()
        snap = json.loads(raw)
    except (OSError, ValueError) as error:
        return {**ev, "reason": f"{type(error).__name__}: {bounded(error, 120)}"}
    teardown = snap.get("teardown") if isinstance(snap, dict) else None
    ev.update(snapshot="READ", bytes=len(raw), sha256=sha(raw), claimMatch=claim == f"{sha(raw)} {len(raw)}", teardown=teardown)
    steps = isinstance(teardown, dict) and {"contextClose", "stdinDestroy"} <= set(teardown) and all(v == "OK" for v in teardown.values())
    ev["confirmed"] = ev["exit"] == "SUCCESS" and ev["claimMatch"] and bool(steps)
    return ev


class BasicLimit(C.Structure):
    _fields_ = [("UserTime", C.c_int64), ("JobUserTime", C.c_int64), ("LimitFlags", W.DWORD), ("MinWs", C.c_size_t), ("MaxWs", C.c_size_t),
                ("ActiveProcessLimit", W.DWORD), ("Affinity", C.c_size_t), ("PriorityClass", W.DWORD), ("SchedulingClass", W.DWORD)]


class ExtLimit(C.Structure):
    _fields_ = [("Basic", BasicLimit), ("Io", C.c_uint64 * 6), ("ProcessMemory", C.c_size_t), ("JobMemory", C.c_size_t),
                ("PeakProcess", C.c_size_t), ("PeakJob", C.c_size_t)]


class ThreadEntry(C.Structure):
    _fields_ = [("size", W.DWORD), ("usage", W.DWORD), ("tid", W.DWORD), ("pid", W.DWORD),
                ("priority", W.LONG), ("delta", W.LONG), ("flags", W.DWORD)]


class Win32:
    """Kernel32 contracts for the admitted native profile; offline tests inject calls, not OS effects."""
    def __init__(self):
        if os.name != "nt":
            raise RuntimeError("this admitted native profile requires Windows")
        self.k, self.cleanup_errors = C.WinDLL("kernel32", use_last_error=True), []
        signatures = {
            "CreateJobObjectW": ([C.c_void_p, W.LPCWSTR], W.HANDLE), "OpenProcess": ([W.DWORD, W.BOOL, W.DWORD], W.HANDLE),
            "GetProcessTimes": ([W.HANDLE, C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p], W.BOOL),
            "QueryFullProcessImageNameW": ([W.HANDLE, W.DWORD, W.LPWSTR, C.POINTER(W.DWORD)], W.BOOL),
            "TerminateProcess": ([W.HANDLE, W.UINT], W.BOOL), "IsProcessInJob": ([W.HANDLE, W.HANDLE, C.POINTER(W.BOOL)], W.BOOL),
            "AssignProcessToJobObject": ([W.HANDLE, W.HANDLE], W.BOOL), "WaitForSingleObject": ([W.HANDLE, W.DWORD], W.DWORD),
            "SetInformationJobObject": ([W.HANDLE, C.c_int, C.c_void_p, W.DWORD], W.BOOL),
            "QueryInformationJobObject": ([W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p], W.BOOL),
            "CloseHandle": ([W.HANDLE], W.BOOL), "CreateToolhelp32Snapshot": ([W.DWORD, W.DWORD], W.HANDLE),
            "Thread32First": ([W.HANDLE, C.POINTER(ThreadEntry)], W.BOOL), "Thread32Next": ([W.HANDLE, C.POINTER(ThreadEntry)], W.BOOL),
            "GetProcessIdOfThread": ([W.HANDLE], W.DWORD),
            "OpenThread": ([W.DWORD, W.BOOL, W.DWORD], W.HANDLE), "ResumeThread": ([W.HANDLE], W.DWORD)}
        for name, (args, result) in signatures.items():
            getattr(self.k, name).argtypes, getattr(self.k, name).restype = args, result

    def _ok(self, value, invalid=None):
        if not value or value == invalid:
            raise C.WinError(C.get_last_error())
        return value

    @contextmanager
    def _owned(self, handle):
        try:
            yield handle
        except BaseException:
            try:
                self.close(handle)
            except Exception as cleanup:
                self.cleanup_errors.append("handle-close: " + bounded(cleanup, 180))
            raise
        else:
            self.close(handle)

    def create_job(self):
        return self._ok(self.k.CreateJobObjectW(None, None))

    def set_limits(self, job, active):
        info = ExtLimit()
        info.Basic.LimitFlags, info.Basic.ActiveProcessLimit = ACTIVE | KILL_CLOSE, active
        self._ok(self.k.SetInformationJobObject(job, EXTENDED, C.byref(info), C.sizeof(info)))

    def query_limits(self, job):
        info = ExtLimit()
        self._ok(self.k.QueryInformationJobObject(job, EXTENDED, C.byref(info), C.sizeof(info), None))
        flags = info.Basic.LimitFlags
        return {"active": info.Basic.ActiveProcessLimit if flags & ACTIVE else None, "killOnClose": bool(flags & KILL_CLOSE),
                "breakaway": bool(flags & BREAKAWAY), "silentBreakaway": bool(flags & SILENT)}

    def members(self, job):
        raw = C.create_string_buffer(65536)
        self._ok(self.k.QueryInformationJobObject(job, 3, raw, len(raw), None))
        assigned, count = C.cast(raw, C.POINTER(W.DWORD))[:2]
        if count != assigned:
            raise RuntimeError("descendant query was truncated")
        return list((C.c_size_t * count).from_buffer(raw, 8))

    def open(self, pid):
        return self._ok(self.k.OpenProcess(0x1 | 0x1000 | 0x100000, False, pid))

    def identity(self, pid, handle=None):
        if handle is not None and handle in (0, -1, C.c_void_p(-1).value):
            raise ValueError("invalid retained process handle")
        with self._owned(self.open(pid)) if handle is None else nullcontext(handle) as h:
            values, name, size = [C.c_ulonglong() for _ in range(4)], C.create_unicode_buffer(32768), W.DWORD(32768)
            self._ok(self.k.GetProcessTimes(h, *(C.byref(v) for v in values)) and self.k.QueryFullProcessImageNameW(h, 0, name, C.byref(size)))
            return {"pid": pid, "creation100ns": values[0].value, "image": name.value}

    def exited(self, handle):
        status = self.k.WaitForSingleObject(handle, 0)
        if status == 0xFFFFFFFF:
            raise C.WinError(C.get_last_error())
        if status not in (0, 258):
            raise RuntimeError(f"unexpected process wait status: {status}")
        return status == 0

    def in_job(self, handle, job):
        member = W.BOOL()
        self._ok(self.k.IsProcessInJob(handle, job, C.byref(member)))
        return bool(member.value)

    def terminate(self, handle):
        self._ok(self.k.TerminateProcess(handle, 1))

    def assign(self, job, handle):
        self._ok(self.k.AssignProcessToJobObject(job, handle))

    def resume(self, pid):
        snapshot = self._ok(self.k.CreateToolhelp32Snapshot(4, 0), C.c_void_p(-1).value)
        with self._owned(snapshot) as snap:
            entry, tids, step = ThreadEntry(), [], self.k.Thread32First
            while True:
                entry.size = C.sizeof(entry)
                if not step(snap, C.byref(entry)):
                    error = C.get_last_error()
                    if error != 18:  # ERROR_NO_MORE_FILES alone proves complete enumeration
                        raise C.WinError(error)
                    break
                if entry.size < ThreadEntry.pid.offset + C.sizeof(W.DWORD):
                    raise RuntimeError("thread record does not cover ownership fields")
                if entry.pid == pid:
                    tids.append(entry.tid)
                step = self.k.Thread32Next
            if len(tids) != 1:
                raise RuntimeError("unexpected suspended thread count")
            with self._owned(self._ok(self.k.OpenThread(0x802, False, tids[0]))) as thread:
                if self._ok(self.k.GetProcessIdOfThread(thread)) != pid:
                    raise RuntimeError("opened thread is not owned by the pinned process")
                previous = self.k.ResumeThread(thread)
                if previous == 0xFFFFFFFF:
                    raise C.WinError(C.get_last_error())
                if previous != 1:
                    raise RuntimeError(f"unexpected prior suspend count: {previous}")

    def close(self, handle):
        self._ok(self.k.CloseHandle(handle))

class Native:
    """Job membership owns descendants; retained process handles pin creation identity. API and Popen are injectable."""
    def __init__(self, collector, docker_prefix, stage, namespace, *, api=None, popen=None):
        self.c, self.docker, self.api, self.popen = collector, docker_prefix, api or Win32(), popen or subprocess.Popen
        self.stage, self.namespace, self.dependency, self.job = stage, namespace, None, None
        self.roots, self.container, self.container_identity, self.ports = [], None, None, []
        self.container_identity_pending, self.retained = False, {}
        if isinstance(self.api, Win32):
            self.api.cleanup_errors = self.c.cleanup_errors
        job = self.api.create_job()
        try:  # configure and read back the policy before any utility query or child can exist
            self.api.set_limits(job, JOB_LIMIT)
            if self.api.query_limits(job) != {"active": JOB_LIMIT, "killOnClose": True, "breakaway": False, "silentBreakaway": False}:
                raise RuntimeError("owned job safety policy was not confirmed")
        except BaseException:
            try:
                self.api.close(job)
            except Exception as cleanup:
                self.c.cleanup_errors.append("job-close: " + bounded(cleanup, 180))
            raise
        self.job = job

    def identity(self, pid, handle=None):
        return self.api.identity(pid, handle)

    def _record(self):
        rows = [{"identity": x["identity"], **x["evidence"]} for x in self.roots]
        (self.c.custody / "process-roots.json").write_bytes(dumps(rows))  # one safe serializer: no raw argv reaches custody

    def _spawn(self, argv, *, admitted=False, **kw):
        """Final admission, suspended create, job assign, exact identity, persist it, then a FRESH phase/time check before resume. A failed or
        refused step never resumes the child; only the exact owned creation handle is stopped, within the remaining finite wait."""
        proto, own = self.c.proto, None
        op = self.c.current_op() if admitted else None
        if op is None:
            own = op = proto.queue("launch")
            proto.grant(op, 1)
        p = self.popen(argv, creationflags=0x00000004, **kw)  # Windows CREATE_SUSPENDED
        root = {"p": p, "identity": None, "evidence": argv_evidence(argv)}
        self.roots.append(root)
        try:
            self.api.assign(self.job, int(p._handle))
            root["identity"] = self.api.identity(p.pid, int(p._handle))
            self._record()  # identity persistence may block or consume the whole cutoff
            proto.check(op)
            self.api.resume(p.pid)
        except BaseException as error:
            try:
                if proto.left(5) > 0 and p.poll() is None and proto.left(5) > 0:
                    p.kill()  # fresh cleanup admission; the exact creation handle cannot target a reused PID
                wait = proto.left(5)
                if wait > 0:
                    with suppress(subprocess.TimeoutExpired):
                        p.wait(timeout=wait)
            except Exception as cleanup:
                self.c.cleanup_errors.append(f"spawn-cleanup: {type(cleanup).__name__}: {bounded(cleanup, 180)}")
            if own:
                proto.complete(own, False, type(error).__name__)
            raise
        if own:
            proto.complete(own)
        return p

    def launch(self, argv, *, cwd, env, stdout, stdin=None):
        return self._spawn(argv, cwd=cwd, env=env, stdout=stdout, stderr=subprocess.STDOUT, stdin=stdin,
                           text=stdin is not None, encoding="utf-8" if stdin is not None else None)

    def run_utility(self, argv, *, input=None, timeout=None, **_ignored):
        """Collector runner: utility children share the job; a timeout kills only this exact child and drains within the remaining wait."""
        p = self._spawn(argv, admitted=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
        out, err = bounded_communicate(p, self.c, input, timeout)
        return subprocess.CompletedProcess(argv, p.returncode, out, err)

    def prepare_kill(self):
        owned = set(self.api.members(self.job))
        for x in self.roots:
            if x["p"].poll() is None and self.api.identity(x["p"].pid, int(x["p"]._handle)) != x["identity"]:
                raise RuntimeError("root process creation identity changed")
        identities = []
        for pid in sorted(owned):
            handle = self.retained[pid] = self.api.open(pid)
            if not self.api.in_job(handle, self.job):
                raise RuntimeError("opened process is not a member of the owned job")
            identities.append(self.api.identity(pid, handle))
        (self.c.custody / "descendants-before-cleanup.json").write_bytes(dumps(identities))
        return identities

    def kill(self, identity):
        handle = self.retained[identity["pid"]]
        if self.api.exited(handle):
            return  # the retained creation handle proves this exact owned process already exited
        if self.api.identity(identity["pid"], handle) != identity:
            raise RuntimeError("retained handle identity changed before stop")
        self.c.op("owned-handle-stop", lambda wait: self.api.terminate(handle), 5, bounded=True)

    def remove_container(self):
        if self.container:
            actual = self.c.command("container-identity", [*self.docker, "inspect", self.container], parse=lambda raw: json.loads(raw)[0])
            if [actual["Id"], actual["Image"], actual["Name"]] != self.container_identity:
                raise RuntimeError("container identity changed before removal")
            self.c.command("container-remove", [*self.docker, "rm", "-f", self.container], timeout=15)

    def query_processes(self):
        return self.c.command("tasklist", ["tasklist", "/NH", "/FO", "CSV"], timeout=10, parse=parse_tasklist)

    def query_containers(self):
        if not self.docker:
            return set()  # no Docker context was admitted, so no container can exist
        return self.c.command("docker-ps", [*self.docker, "ps", "-a", "--no-trunc", "--format", "{{.ID}}"], timeout=10, parse=parse_docker_ids)

    def members(self):
        return self.api.members(self.job)

    def listeners(self):
        def parse(raw):
            rows = [r.split() for r in raw.splitlines() if r.strip().startswith("TCP")]
            if any(len(r) != 5 or not r[4].isdigit() for r in rows):
                raise RuntimeError("native listener query malformed")
            return [{"address": r[1], "pid": int(r[4])} for r in rows if r[3] == "LISTENING" and int(r[1].rsplit(":", 1)[1]) in self.ports]
        return self.c.command("netstat", ["netstat", "-ano", "-p", "tcp"], timeout=10, parse=parse)

    def verify_disposal_target(self):
        return check_disposable(self.stage, self.namespace, self.dependency)

    def close(self):
        errors = []
        for handle in [*self.retained.values(), self.job]:  # every exact handle is attempted; a close error stays a failure
            try:
                self.api.close(handle)
            except Exception as error:
                errors.append(f"{type(error).__name__}: {str(error)[:80]}")
        if errors:
            raise RuntimeError("exact-handle close failed: " + "; ".join(errors))
