from typing import Callable, Any, Dict, Tuple
from caishen_sdk_python.caishen import CaishenSDK
from caishen_sdk_python.tools.get_tools import get_tools

# Define the Tool type: a callable that takes any parameters and returns an awaitable result
Tool = Callable[[Any], Any]

async def create_eleven_labs_tools(sdk: CaishenSDK) -> Tuple[list, Dict[str, Tool]]:
    tools = await get_tools(sdk=sdk)

    openai_tool_specs = []
    tool_runners = {}

    for tool in tools.values():
        openai_tool_specs.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters.schema(),
            },
        })

        tool_runners = {
            tool.name: (lambda params, t=tool: t.execute(params))
            for tool in tools.values()
        }

    return openai_tool_specs, tool_runners
