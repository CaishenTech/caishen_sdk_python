from typing import Callable, Any, Awaitable, Dict
from ...caishen import CaishenSDK
from tools.get_tools import get_tools

# Define the Tool type: a callable that takes any parameters and returns an awaitable result
Tool = Callable[[Any], Awaitable[Any]]

async def create_eleven_labs_tools(sdk: CaishenSDK) -> Dict[str, Tool]:
    tools = await get_tools(sdk=sdk)

    # Build a dictionary of tools where each tool is a function that executes the tool's execute method
    return {
        tool.name: (lambda params, t=tool: t.execute(params))
        for tool in tools.values()
    }
