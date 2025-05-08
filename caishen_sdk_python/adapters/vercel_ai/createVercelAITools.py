from typing import Any, Callable, Awaitable, Dict
from caishen_sdk_python.adapters.vercel_ai.vercel_tool import tool
from caishen_sdk_python.caishen import CaishenSDK
from caishen_sdk_python.tools.get_tools import get_tools


ToolSet = Dict[str, Callable[[Any], Awaitable[Any]]]

async def create_vercel_ai_tools(sdk: CaishenSDK) -> ToolSet:
    tools = await get_tools(sdk=sdk)

    vercel_ai_tools: ToolSet = {}

    for t in tools.values():
        # Define tool metadata and execution logic
        vercel_ai_tools[t.name] = tool(
            description=t.description,
            parameters=t.parameters,  # Should be a Pydantic model
            execute=lambda params, _t=t: _t.execute(params)
        )

    return vercel_ai_tools
