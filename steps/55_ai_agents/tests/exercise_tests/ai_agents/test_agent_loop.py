from importlib import import_module

target = import_module("exercises.ai_agents.01_agent_loop")


def test_ai_agents() -> None:
    assert target.choose_next_step("please search", []) == "tool"
    assert target.choose_next_step("final answer", []) == "answer"
    assert target.choose_next_step("needs approval", []) == "human_review"
    call = target.ToolCall("search", {"q": "python"})
    assert target.validate_tool_call(call, {"search"})
    assert not target.validate_tool_call(call, {"write_file"})
    assert target.update_memory(["a", "b"], "c", 2) == ["b", "c"]
