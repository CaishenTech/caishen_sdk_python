from typing import Any, Callable, List
from langchain_core.tools import tool as lc_tool
from ...caishen import CaishenSDK
from tools.get_tools import get_tools

async def create_langchain_tools(sdk: CaishenSDK) -> List[Callable]:
    tools = await get_tools(sdk=sdk)
    langchain_tools = []

    for t in tools.values():
        # Dynamically define a tool function with LangChain's @tool-style decorator
        @lc_tool(name=t.name, description=t.description, args_schema=t.parameters)
        async def tool_func(arg: Any, _tool=t):
            return await _tool.execute(arg)

        langchain_tools.append(tool_func)

    return langchain_tools
