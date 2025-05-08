from typing import Callable, Any, Awaitable, Dict, Tuple, List
from caishen_sdk_python.caishen import CaishenSDK
from caishen_sdk_python.tools.get_tools import get_tools

# Define the Tool type: a callable that takes any parameters and returns an awaitable result
Tool = Callable[[Any], Awaitable[Any]]

async def create_eleven_labs_tools(sdk: CaishenSDK) -> Tuple[Dict[str, Tool], List[Dict]]:
    tools = get_tools(sdk=sdk)

    # LangChain-style callable functions
    langchain_tools = {
        tool_name: (lambda params, t=tool: t["execute"](params))
        for tool_name, tool in tools.items()
    }

    # OpenAI-compatible JSON tool definitions
    openai_tools = [
        {
            "type": "function",
            "function": {
                "name": tool_name,
                "description": tool.get("description", "No description provided."),
                "parameters": tool["parameters"].schema(),  # Assuming parameters are Pydantic schemas
            }
        }
        for tool_name, tool in tools.items()
    ]

    return langchain_tools, openai_tools
