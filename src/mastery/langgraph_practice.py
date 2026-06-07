from __future__ import annotations

from typing import TypedDict


class StudyState(TypedDict):
    topic: str
    level: int
    advice: str


def advise(state: StudyState) -> StudyState:
    level = state["level"]
    advice = "基礎問題を3問解く" if level < 3 else "既存コードを読んで修正案を書く"
    return {**state, "advice": advice}


class _FallbackStudyGraph:
    def invoke(self, state: StudyState) -> StudyState:
        return advise(state)


def build_study_graph() -> object:
    try:
        from langgraph.graph import END, StateGraph
    except (ImportError, TypeError):
        return _FallbackStudyGraph()

    graph = StateGraph(StudyState)
    graph.add_node("advise", advise)
    graph.set_entry_point("advise")
    graph.add_edge("advise", END)
    return graph.compile()
