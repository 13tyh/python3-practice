"""argparseで実務CLIを作る練習。"""

from argparse import ArgumentParser, Namespace


def build_parser() -> ArgumentParser:
    """input, limit, dry-runを受け取るparserを返す。"""
    # TODO
    raise NotImplementedError


def parse_args(argv: list[str]) -> Namespace:
    """testしやすいようにargvを外から受け取る。"""
    # TODO
    raise NotImplementedError


def summarize_args(args: Namespace) -> dict[str, object]:
    """Namespaceを内部処理で使いやすいdictに変換する。"""
    # TODO
    raise NotImplementedError
