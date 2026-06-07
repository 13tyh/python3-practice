"""正規表現の実務基礎。"""

import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
ZIP_PATTERN = re.compile(r"^\d{3}-\d{4}$")


def is_valid_email(value: str) -> bool:
    """簡易email形式ならTrue。"""
    # TODO
    raise NotImplementedError


def normalize_phone(value: str) -> str:
    """数字以外を除去する。"""
    # TODO
    raise NotImplementedError


def extract_hashtags(text: str) -> list[str]:
    """#tag を小文字で抽出する。"""
    # TODO
    raise NotImplementedError


def mask_zip_code(text: str) -> str:
    """郵便番号形式を***-****へ置換する。"""
    # TODO
    raise NotImplementedError
