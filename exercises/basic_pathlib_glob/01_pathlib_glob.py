"""pathlibとglobの基礎練習。"""

from pathlib import Path


def has_suffix(path: Path, suffix: str) -> bool:
    """pathのsuffixが一致するか返す。"""
    # TODO
    raise NotImplementedError


def file_names(paths: list[Path]) -> list[str]:
    """Pathのnameだけを返す。"""
    # TODO
    raise NotImplementedError


def filter_by_suffix(paths: list[Path], suffix: str) -> list[Path]:
    """suffixが一致するPathだけ返す。"""
    # TODO
    raise NotImplementedError
