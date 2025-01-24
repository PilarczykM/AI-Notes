"""This module contains the nodes for the assistant's state machine."""
import json
from typing import Literal

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig

from src.assistant.configuration import Configuration
from src.assistant.model import create_model_from_config
from src.assistant.prompts import (
    QUERY_WRITER_TEMPLATE,
    REFLECTION_TEMPLATE,
    SUMMARIZER_TEMPLATE,
)
from src.assistant.state import SummaryState
from src.assistant.utils import (
    deduplicate_and_format_sources,
    format_sources,
    tavily_search,
)


def generate_query(state: SummaryState, config: RunnableConfig):
    """Generate a query for web search."""
    # Format the prompt
    query_writer_instructions_formatted = QUERY_WRITER_TEMPLATE.format(
        research_topic=state.research_topic
    )

    # Generate a query
    llm_json_mode = create_model_from_config(config, format="json")

    result = llm_json_mode.invoke(
        [
            SystemMessage(content=query_writer_instructions_formatted),
            HumanMessage(content="Generate a query for web search:"),
        ]
    )
    query = json.loads(result.content)

    return {"search_query": query["query"]}


def web_research(state: SummaryState):
    """Gather information from the web."""
    # Search the web
    search_results = tavily_search(
        state.search_query, include_raw_content=True, max_results=1
    )

    # Format the sources
    search_str = deduplicate_and_format_sources(
        search_results, max_tokens_per_source=1000
    )
    return {
        "sources_gathered": [format_sources(search_results)],
        "research_loop_count": state.research_loop_count + 1,
        "web_research_results": [search_str],
    }


def summarize_sources(state: SummaryState, config: RunnableConfig):
    """Summarize the gathered sources."""
    # Existing summary
    existing_summary = state.running_summary

    # Most recent web research
    most_recent_web_research = state.web_research_results[-1]

    # Build the human message
    if existing_summary:
        human_message_content = (
            f"Extend the existing summary: {existing_summary}\n\n"
            f"Include new search results: {most_recent_web_research} "
            f"That addresses the following topic: {state.research_topic}"
        )
    else:
        human_message_content = (
            f"Generate a summary of these search results: {most_recent_web_research} "
            f"That addresses the following topic: {state.research_topic}"
        )

    # Run the LLM
    llm = create_model_from_config(config)
    result = llm.invoke(
        [
            SystemMessage(content=SUMMARIZER_TEMPLATE),
            HumanMessage(content=human_message_content),
        ]
    )

    running_summary = result.content

    # TODO: This is a hack to remove the <think> tags w/ Deepseek models
    # It appears very challenging to prompt them out of the responses
    while "<think>" in running_summary and "</think>" in running_summary:
        start = running_summary.find("<think>")
        end = running_summary.find("</think>") + len("</think>")
        running_summary = running_summary[:start] + running_summary[end:]

    return {"running_summary": running_summary}


def reflect_on_summary(state: SummaryState, config: RunnableConfig):
    """Reflect on the summary and generate a follow-up query."""
    # Generate a query
    llm_json_mode = create_model_from_config(config, format="json")
    result = llm_json_mode.invoke(
        [
            SystemMessage(
                content=REFLECTION_TEMPLATE.format(
                    research_topic=state.research_topic
                )
            ),
            HumanMessage(
                content=f"Identify a knowledge gap and generate a follow-up web search query based on our existing knowledge: {state.running_summary}"
            ),
        ]
    )
    follow_up_query = json.loads(result.content)

    # Overwrite the search query
    return {"search_query": follow_up_query["follow_up_query"]}


def finalize_summary(state: SummaryState):
    """Finalize the summary."""
    # Format all accumulated sources into a single bulleted list
    all_sources = "\n".join(source for source in state.sources_gathered)
    state.running_summary = (
        f"## Summary\n\n{state.running_summary}\n\n ### Sources:\n{all_sources}"
    )
    return {"running_summary": state.running_summary}


def route_research(
    state: SummaryState, config: RunnableConfig
) -> Literal["finalize_summary", "web_research"]:
    """Route the research based on the follow-up query."""
    configurable = Configuration.from_runnable_config(config)
    if state.research_loop_count <= configurable.max_web_research_loops:
        return "web_research"
    else:
        return "finalize_summary"

