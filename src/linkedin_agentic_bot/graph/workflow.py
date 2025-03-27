from functools import lru_cache

from langgraph.graph import END, START, StateGraph


@lru_cache(maxsize=1)
def build_graph():
    graph_builder = StateGraph(State)

    # Nodes
    # planner
    # drafter
    # finalizer

    # Edges
    # planner -> drafter
    # drafter -> finalizer
    # finalizer -> END

    return graph_builder
