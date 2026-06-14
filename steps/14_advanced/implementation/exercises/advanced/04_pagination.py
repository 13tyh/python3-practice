"""ページング処理の応用。"""


def paginate(items: list[str], page: int, per_page: int) -> list[str]:
    # TODO
    raise NotImplementedError


def total_pages(total_count: int, per_page: int) -> int:
    # TODO
    raise NotImplementedError


def build_page_info(total_count: int, page: int, per_page: int) -> dict[str, int | bool]:
    # TODO
    raise NotImplementedError
