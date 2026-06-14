from exercises.basics_repetition.round_10 import Todo, active_titles, complete, completion_rate


def test_round_10() -> None:
    todo = Todo("learn")
    complete(todo)
    assert todo.done
    todos = [Todo("a"), Todo("b", True)]
    assert active_titles(todos) == ["a"]
    assert completion_rate(todos) == 0.5
    assert completion_rate([]) == 0.0
