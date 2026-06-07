from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, StateGraph


class StudyState(TypedDict):
    topic: str
    level: int
    advice: str


def advise(state: StudyState) -> StudyState:
    level = state["level"]
    advice = "基礎問題を3問解く" if level < 3 else "既存コードを読んで修正案を書く"
    return {**state, "advice": advice}


def build_study_graph() -> object:
    graph = StateGraph(StudyState)
    graph.add_node("advise", advise)
    graph.set_entry_point("advise")
    graph.add_edge("advise", END)
    return graph.compile()

