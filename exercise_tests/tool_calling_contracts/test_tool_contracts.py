from importlib import import_module

target = import_module("exercises.tool_calling_contracts.01_tool_contracts")


def test_is_allowed_tool() -> None:
    assert target.is_allowed_tool("search_docs", {"search_docs"}) is True
    assert target.is_allowed_tool("delete_all", {"search_docs"}) is False


def test_missing_arguments() -> None:
    assert target.missing_arguments({"query": "x"}, {"query", "limit"}) == ["limit"]


def test_validate_tool_call() -> None:
    call = {"name": "search_docs", "arguments": {"query": "python"}}

    assert target.validate_tool_call(call, {"search_docs"}, {"query"}) is True
    assert target.validate_tool_call(call, {"read_file"}, {"query"}) is False
