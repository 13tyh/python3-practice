"""dataclassの基礎深掘り。"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class User:
    """変更不可のuser。"""

    user_id: str
    name: str
    tags: tuple[str, ...] = ()


@dataclass
class BatchResult:
    """default_factoryでlist共有バグを避ける。"""

    success_ids: list[str] = field(default_factory=list)
    failed_ids: list[str] = field(default_factory=list)


def create_user(user_id: str, name: str, tags: list[str]) -> User:
    """listのtagsをtupleに変換してUserを作る。"""
    # TODO
    raise NotImplementedError


def add_success(result: BatchResult, item_id: str) -> BatchResult:
    """成功IDを追加して同じresultを返す。"""
    # TODO
    raise NotImplementedError


def success_rate(result: BatchResult) -> float:
    """成功率を返す。件数0なら0.0。"""
    # TODO
    raise NotImplementedError
