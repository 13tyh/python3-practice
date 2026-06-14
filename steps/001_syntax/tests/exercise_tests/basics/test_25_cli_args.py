from importlib import import_module

target = import_module("exercises.basics.25_cli_args")


def test_cli_args_tasks() -> None:
    parser = target.build_parser()
    parsed = parser.parse_args(["--name", "Aki", "--count", "3"])
    assert parsed.name == "Aki"
    assert parsed.count == 3
    assert target.parse_name(["--name", "Ren"]) == "Ren"
    assert target.parse_count(["--count", "5"]) == 5
