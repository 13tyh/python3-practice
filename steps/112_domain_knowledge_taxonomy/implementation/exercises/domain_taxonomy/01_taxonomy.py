"""業務taxonomyの練習。"""

SYNONYMS = {"自治体": "municipality", "市区町村": "municipality", "契約": "subscription"}
ALLOWED_CATEGORIES = {"municipality", "subscription", "user", "group"}


def normalize_label(label: str) -> str:
    """空白除去、小文字化、synonym変換を行う。"""
    # TODO
    raise NotImplementedError


def is_allowed_category(label: str) -> bool:
    """taxonomyで許可されたカテゴリならTrue。"""
    # TODO
    raise NotImplementedError


def canonical_terms(labels: list[str]) -> list[str]:
    """重複なしのcanonical termを昇順で返す。"""
    # TODO
    raise NotImplementedError
