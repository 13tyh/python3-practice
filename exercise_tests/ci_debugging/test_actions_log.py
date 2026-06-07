from importlib import import_module

ci = import_module("exercises.ci_debugging.01_actions_log")


def test_failed_steps_returns_run_command_before_error() -> None:
    log = """
Run poetry run lint
ok
Run poetry run test
FAILED exercise_tests/basics/test_01_values.py::test_add_tax
##[error]Process completed with exit code 1.
"""

    assert ci.failed_steps(log) == ["poetry run test"]


def test_pytest_failures_extracts_failed_lines() -> None:
    log = """
FAILED exercise_tests/basics/test_01_values.py::test_add_tax - AssertionError
PASSED exercise_tests/basics/test_02_if.py::test_status
FAILED exercise_tests/api/test_app.py::test_post - ValueError
"""

    assert ci.pytest_failures(log) == [
        "exercise_tests/basics/test_01_values.py::test_add_tax",
        "exercise_tests/api/test_app.py::test_post",
    ]
