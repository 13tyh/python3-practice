from mastery.langgraph_practice import advise, build_study_graph


def test_advise() -> None:
    assert advise({"topic": "file", "level": 1, "advice": ""})["advice"] == "基礎問題を3問解く"
    assert (
        advise({"topic": "project", "level": 4, "advice": ""})["advice"]
        == "既存コードを読んで修正案を書く"
    )


def test_build_study_graph() -> None:
    app = build_study_graph()
    result = app.invoke({"topic": "typing", "level": 2, "advice": ""})
    assert result["advice"] == "基礎問題を3問解く"
