"""The state module for the research assistant."""
import operator
from dataclasses import dataclass, field

from typing_extensions import Annotated, TypedDict


@dataclass(kw_only=True)
class SummaryState:
    """The state for the summary assistant."""
    research_topic: str = field(default=None)     
    search_query: str = field(default=None)
    web_research_results: Annotated[list, operator.add] = field(default_factory=list) 
    sources_gathered: Annotated[list, operator.add] = field(default_factory=list) 
    research_loop_count: int = field(default=0)
    running_summary: str = field(default=None)

@dataclass(kw_only=True)
class SummaryStateInput(TypedDict):
    """The input for the summary assistant."""
    research_topic: str = field(default=None)   

@dataclass(kw_only=True)
class SummaryStateOutput(TypedDict):
    """The output for the summary assistant."""
    running_summary: str = field(default=None)