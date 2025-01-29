"""Configuration class for research assistant."""

import os
from dataclasses import dataclass, fields
from typing import Any, Optional

from langchain_core.runnables import RunnableConfig


@dataclass(kw_only=True)
class Configuration:
    """configuration class for research assistant."""
    max_web_research_loops: int = 3
    local_llm: str = "llama3.2"


    @classmethod
    def from_runnable_config(cls, config: Optional[RunnableConfig]) -> "Configuration":
        """Create a configuration object from a runnable configuration."""
        config_key = "configurable"
        configurable = config[config_key] if config and config_key in config  else {}

        values: dict[str, Any] = {
            f.name: os.environ.get(f.name.upper(), configurable.get(f.name))
            for f in fields(cls)
            if f.init
        }
        return cls(**{k: v for k, v in values.items() if v})
