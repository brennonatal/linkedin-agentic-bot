from functools import lru_cache

from langgraph.graph import END, START, StateGraph

from src.linkedin_agentic_bot.graph.nodes import drafter, finalizer, planner
from src.linkedin_agentic_bot.graph.state import State


@lru_cache(maxsize=1)
def build_graph():
    graph_builder = StateGraph(State)

    # Nodes
    graph_builder.add_node("planner", planner)
    graph_builder.add_node("drafter", drafter)
    graph_builder.add_node("finalizer", finalizer)

    # Edges
    graph_builder.add_edge(START, "planner")
    graph_builder.add_edge("planner", "drafter")
    graph_builder.add_edge("drafter", "finalizer")
    graph_builder.add_edge("finalizer", END)

    return graph_builder
