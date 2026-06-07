from importlib import import_module

target = import_module("exercises.ai_streaming.01_streaming")


def test_streaming() -> None:
    assert target.split_tokens("hello world") == ["hello", "world"]
    assert list(target.stream_text("hello world")) == ["hello", "world"]
    assert target.to_sse_event("hello") == "data: hello\n\n"
