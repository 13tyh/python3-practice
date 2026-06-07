from exercises.basics_repetition.round_30 import merge_params, parse_key_value, to_query_string


def test_round_30() -> None:
    assert parse_key_value("a=1,b=2") == {"a": "1", "b": "2"}
    assert to_query_string({"q": "python", "page": "1"}) == "page=1&q=python"
    assert merge_params({"q": "python"}, {"page": "1", "empty": None}) == {
        "q": "python",
        "page": "1",
    }

