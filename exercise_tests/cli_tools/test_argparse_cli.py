from argparse import Namespace
from importlib import import_module

cli = import_module("exercises.cli_tools.01_argparse_cli")


def test_parse_required_input_and_defaults() -> None:
    args = cli.parse_args(["--input", "data/users.csv"])

    assert args.input == "data/users.csv"
    assert args.limit == 100
    assert args.dry_run is False


def test_parse_limit_and_dry_run() -> None:
    args = cli.parse_args(["--input", "data/users.csv", "--limit", "5", "--dry-run"])

    assert args.limit == 5
    assert args.dry_run is True


def test_summarize_args() -> None:
    summary = cli.summarize_args(Namespace(input="data/users.csv", limit=10, dry_run=True))

    assert summary == {"input": "data/users.csv", "limit": 10, "mode": "dry-run"}
