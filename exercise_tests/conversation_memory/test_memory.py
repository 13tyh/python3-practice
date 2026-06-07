from importlib import import_module

target = import_module("exercises.conversation_memory.01_memory")


def test_count_by_role() -> None:
    messages = [{"role": "system", "content": "s"}, {"role": "user", "content": "u"}]

    assert target.count_by_role(messages) == {"system": 1, "user": 1}


def test_trim_messages_keeps_system_and_recent_messages() -> None:
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "old message"},
        {"role": "assistant", "content": "new"},
    ]

    assert target.trim_messages(messages, max_chars=9) == [
        {"role": "system", "content": "rules"},
        {"role": "assistant", "content": "new"},
    ]


def test_memory_summary() -> None:
    assert target.memory_summary([{"role": "user", "content": "hello"}]) == "messages=1 roles=1"
