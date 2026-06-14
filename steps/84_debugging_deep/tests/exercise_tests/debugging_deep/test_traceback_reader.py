from importlib import import_module

target = import_module("exercises.debugging_deep.01_traceback_reader")

TRACEBACK = """
Traceback (most recent call last):
  File "app/service.py", line 10, in run
    divide()
  File "app/math.py", line 3, in divide
    1 / 0
ZeroDivisionError: division by zero
"""


def test_exception_name() -> None:
    assert target.exception_name(TRACEBACK) == "ZeroDivisionError"


def test_last_file_line() -> None:
    assert target.last_file_line(TRACEBACK) == ("app/math.py", 3)


def test_investigation_note() -> None:
    note = target.investigation_note(TRACEBACK)

    assert "ZeroDivisionError" in note
    assert "app/math.py:3" in note
