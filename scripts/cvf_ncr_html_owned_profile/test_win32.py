"""Win32 contract faults without kernel calls or children; assertions precede source repair."""
import ctypes
import os
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cvf_ncr_html_owned_profile import lifecycle as L


@pytest.fixture
def rig(monkeypatch):
    calls, error = [], {"code": 5}

    def winerror(code):
        exc = OSError(code, f"synthetic error {code}")
        exc.winerror = code
        return exc

    monkeypatch.setattr(L.C, "get_last_error", lambda: error["code"], raising=False)
    monkeypatch.setattr(L.C, "WinError", winerror, raising=False)
    api = object.__new__(L.Win32)
    api.cleanup_errors = []

    def close(handle):
        calls.append(("close", handle))
        return 1

    api.k = SimpleNamespace(CloseHandle=close)
    return api, calls, error


def enumeration(rig, rows=((501, 41, 28),), *, first_error=None, next_error=18, previous=1, close_fail=()):
    api, calls, error = rig
    pending = iter(rows)

    def step(which, entry):
        calls.append((which,))
        try:
            pid, tid, size = next(pending)
        except StopIteration:
            error["code"] = first_error if which == "first" and first_error is not None else next_error
            return 0
        entry._obj.pid, entry._obj.tid, entry._obj.size = pid, tid, size
        return 1

    def close(handle):
        calls.append(("close", handle))
        error["code"] = 9
        return 0 if handle in close_fail else 1

    api.k.CreateToolhelp32Snapshot = lambda *_: 101
    api.k.Thread32First = lambda _, e: step("first", e)
    api.k.Thread32Next = lambda _, e: step("next", e)
    api.k.OpenThread = lambda access, inherit, tid: calls.append(("open-thread", tid)) or 201
    api.k.GetProcessIdOfThread = lambda _h: 501
    def resume(handle):
        calls.append(("resume", handle))
        if previous == 0xFFFFFFFF:
            error["code"] = 5
        return previous

    api.k.ResumeThread = resume
    api.k.CloseHandle = close
    return api


@pytest.mark.parametrize("handle", [0, ctypes.c_void_p(-1).value])
def test_snapshot_failure_never_enumerates_or_closes_invalid_handle(rig, handle):
    api = enumeration(rig)
    api.k.CreateToolhelp32Snapshot = lambda *_: handle
    with pytest.raises(OSError) as caught:
        api.resume(501)
    assert caught.value.winerror == 5
    assert rig[1] == []


@pytest.mark.parametrize("status,expected", [(0, True), (258, False)])
def test_wait_observations_are_exact(rig, status, expected):
    api, _, _ = rig
    api.k.WaitForSingleObject = lambda *_: status
    assert api.exited(101) is expected


@pytest.mark.parametrize("status,exception", [(0xFFFFFFFF, OSError), (128, RuntimeError), (7, RuntimeError)])
def test_unknown_wait_never_reaches_owned_stop(rig, status, exception):
    api, calls, _ = rig
    api.k.WaitForSingleObject = lambda *_: status
    api.k.TerminateProcess = lambda *_: calls.append(("terminate",)) or 1
    ops = object.__new__(L.Native)
    ops.api, ops.retained = api, {501: 101}
    with pytest.raises(exception):
        ops.kill({"pid": 501})
    assert calls == []


def test_complete_enumeration_precedes_exact_single_resume(rig):
    api = enumeration(rig, [(999, 3, 28), (501, 41, 28), (999, 4, 28)])
    api.resume(501)
    assert rig[1] == [("first",), ("next",), ("next",), ("next",),
                      ("open-thread", 41), ("resume", 201), ("close", 201), ("close", 101)]


@pytest.mark.parametrize("rows,first_error,next_error,exception", [
    ([], 5, 18, OSError), ([], 18, 18, RuntimeError),
    ([(501, 41, 28)], None, 5, OSError), ([(501, 41, 28)], None, 0, OSError),
    ([(501, 41, 0)], None, 18, RuntimeError),
    ([(999, 41, 28)], None, 18, RuntimeError),
    ([(501, 41, 28), (501, 42, 28)], None, 18, RuntimeError),
])
def test_incomplete_or_ambiguous_thread_list_does_not_resume(rig, rows, first_error, next_error, exception):
    api = enumeration(rig, rows, first_error=first_error, next_error=next_error)
    with pytest.raises(exception):
        api.resume(501)
    assert not any(c[0] in ("open-thread", "resume") for c in rig[1])
    assert rig[1][-1] == ("close", 101)


@pytest.mark.parametrize("previous", [0, 2, 0xFFFFFFFE, 0xFFFFFFFF])
def test_only_prior_suspend_count_one_confirms_resume(rig, previous):
    api = enumeration(rig, previous=previous)
    with pytest.raises(OSError if previous == 0xFFFFFFFF else RuntimeError):
        api.resume(501)
    assert rig[1][-2:] == [("close", 201), ("close", 101)]


@pytest.mark.parametrize("close_fail", [(201,), (101,), (201, 101)])
def test_resume_primary_survives_all_secondary_close_failures(rig, close_fail):
    api = enumeration(rig, previous=0xFFFFFFFF, close_fail=close_fail)
    with pytest.raises(OSError) as caught:
        api.resume(501)
    assert caught.value.winerror == 5
    assert len(api.cleanup_errors) == len(close_fail)
    assert rig[1][-2:] == [("close", 201), ("close", 101)]


def test_enumeration_primary_survives_snapshot_close_failure(rig):
    api = enumeration(rig, next_error=5, close_fail=(101,))
    with pytest.raises(OSError) as caught:
        api.resume(501)
    assert caught.value.winerror == 5 and len(api.cleanup_errors) == 1


def test_successful_resume_with_failed_close_is_not_success(rig):
    api = enumeration(rig, close_fail=(201,))
    with pytest.raises(OSError) as caught:
        api.resume(501)
    assert caught.value.winerror == 9 and rig[1][-1] == ("close", 101)


@pytest.mark.parametrize("owner", [0, 999])
def test_opened_thread_owner_failure_or_reuse_never_resumes(rig, owner):
    api = enumeration(rig)

    def owner_of(_handle):
        rig[2]["code"] = 5
        return owner

    api.k.GetProcessIdOfThread = owner_of
    with pytest.raises(OSError if owner == 0 else RuntimeError):
        api.resume(501)
    assert ("resume", 201) not in rig[1]
    assert rig[1][-2:] == [("close", 201), ("close", 101)]


def identity_calls(rig, *, times=True, image=True, close=True):
    api, calls, error = rig
    api.k.OpenProcess = lambda *_: calls.append(("open-process",)) or 101

    def get_times(_, creation, *_args):
        calls.append(("times",))
        creation._obj.value = 4321
        return int(times)

    def get_image(_, _flags, name, _size):
        calls.append(("image",))
        name.value = "synthetic-python.exe"
        return int(image)

    def close_handle(handle):
        calls.append(("close", handle))
        error["code"] = 9
        return int(close)

    api.k.GetProcessTimes, api.k.QueryFullProcessImageNameW = get_times, get_image
    api.k.CloseHandle = close_handle
    return api


@pytest.mark.parametrize("handle", [0, -1, ctypes.c_void_p(-1).value])
def test_invalid_supplied_handle_never_falls_back_to_pid(rig, handle):
    api = identity_calls(rig)
    with pytest.raises(ValueError):
        api.identity(501, handle)
    assert rig[1] == []


@pytest.mark.parametrize("borrowed", [False, True])
def test_identity_ownership_is_explicit(rig, borrowed):
    api = identity_calls(rig)
    assert api.identity(501, 101 if borrowed else None) == {
        "pid": 501, "creation100ns": 4321, "image": "synthetic-python.exe"}
    assert ("open-process",) in rig[1] if not borrowed else ("open-process",) not in rig[1]
    assert (("close", 101) in rig[1]) is (not borrowed)


@pytest.mark.parametrize("times,image", [(False, True), (True, False)])
def test_identity_primary_survives_owned_close_failure(rig, times, image):
    api = identity_calls(rig, times=times, image=image, close=False)
    with pytest.raises(OSError) as caught:
        api.identity(501)
    assert caught.value.winerror == 5 and len(api.cleanup_errors) == 1
    assert (("image",) in rig[1]) is times


def test_job_policy_failure_survives_job_close_failure():
    collector = SimpleNamespace(cleanup_errors=[])

    def fail(code):
        raise OSError(code, f"synthetic {code}")

    api = SimpleNamespace(create_job=lambda: 101, set_limits=lambda *_: fail(5), close=lambda *_: fail(9))
    with pytest.raises(OSError) as caught:
        L.Native(collector, [], Path("unused"), Path("unused"), api=api)
    assert caught.value.errno == 5 and len(collector.cleanup_errors) == 1


@pytest.mark.skipif(os.name != "nt", reason="Windows binding constructor has an explicit host guard")
def test_thread_function_signatures_are_declared_without_loading_kernel(monkeypatch):
    class Kernel:
        def __getattr__(self, name):
            fn = lambda *_: 1
            setattr(self, name, fn)
            return fn

    kernel = Kernel()
    monkeypatch.setattr(L.C, "WinDLL", lambda *_a, **_kw: kernel)
    L.Win32()
    for name in ("Thread32First", "Thread32Next"):
        fn = getattr(kernel, name)
        assert fn.restype is L.W.BOOL and len(fn.argtypes) == 2


@pytest.mark.parametrize("name,args", [
    ("CreateJobObjectW", ()), ("OpenProcess", (501,)), ("TerminateProcess", (101,)),
    ("AssignProcessToJobObject", (101, 201)), ("CloseHandle", (101,)),
])
def test_existing_null_and_bool_failures_stay_fail_closed(rig, name, args):
    api, _, _ = rig
    setattr(api.k, name, lambda *_: 0)
    method = {"CreateJobObjectW": api.create_job, "OpenProcess": api.open, "TerminateProcess": api.terminate,
              "AssignProcessToJobObject": api.assign, "CloseHandle": api.close}[name]
    with pytest.raises(OSError) as caught:
        method(*args)
    assert caught.value.winerror == 5
