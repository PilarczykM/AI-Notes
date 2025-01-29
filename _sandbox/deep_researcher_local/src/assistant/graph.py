"""Define the state graph for the assistant."""

from langgraph.constants import END, START
from langgraph.graph import StateGraph

from src.assistant.configuration import Configuration
from src.assistant.nodes import (
    finalize_summary,
    generate_query,
    reflect_on_summary,
    route_research,
    summarize_sources,
    web_research,
)
from src.assistant.state import SummaryState, SummaryStateInput, SummaryStateOutput


def build_graph() -> StateGraph:
    """Build the state graph for the assistant."""
    builder = StateGraph(
        SummaryState,
        input=SummaryStateInput,
        output=SummaryStateOutput,
        config_schema=Configuration,
    )
    builder.add_node("generate_query", generate_query)
    builder.add_node("web_research", web_research)
    builder.add_node("summarize_sources", summarize_sources)
    builder.add_node("reflect_on_summary", reflect_on_summary)
    builder.add_node("finalize_summary", finalize_summary)

    # Add edges
    builder.add_edge(START, "generate_query")
    builder.add_edge("generate_query", "web_research")
    builder.add_edge("web_research", "summarize_sources")
    builder.add_edge("summarize_sources", "reflect_on_summary")
    builder.add_conditional_edges("reflect_on_summary", route_research)
    builder.add_edge("finalize_summary", END)

    return builder.compile()