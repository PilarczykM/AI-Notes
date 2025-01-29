"""Model module for the assistant package."""

from langchain_core.runnables import RunnableConfig
from langchain_core.tools import ToolException
from langchain_ollama import ChatOllama

from src.assistant.configuration import Configuration


def create_model_from_config(
    config: RunnableConfig, temperature=0, format=""
):
    """Create a model from a runnable configuration."""
    configurable = Configuration.from_runnable_config(config)

    llm = ChatOllama(model=configurable.local_llm, temperature=temperature, format=format)

    try:
        llm.invoke("warmup")
    except Exception as e:
        raise ToolException(f"Error warming up: {e}")

    return llm
