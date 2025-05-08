from typing import Callable, Any, Awaitable, Dict
from caishen_sdk_python.caishen import CaishenSDK
from caishen_sdk_python.tools.get_tools import get_tools

Tool = Callable[[Any], Awaitable[Any]]

async def create_eleven_labs_tools(sdk: CaishenSDK) -> Dict[str, Tool]:
    tools = get_tools(sdk=sdk)

    return {
        tool_name: (lambda params, t=tool: t["execute"](params))
        for tool_name, tool in tools.items()
    }
