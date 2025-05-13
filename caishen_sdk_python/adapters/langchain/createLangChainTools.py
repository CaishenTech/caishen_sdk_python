from typing import Any, Callable, List
from langchain.tools import Tool
from caishen_sdk_python.caishen import CaishenSDK
from caishen_sdk_python.tools.get_tools import get_tools

async def create_langchain_tools(sdk: CaishenSDK) -> List[Callable]:
    tools = await get_tools(sdk=sdk)
    langchain_tools = []

    for t in tools.values():
        # Define a tool function that wraps the async execute
        async def tool_func(arg: Any, _tool=t):
            return await _tool.execute(arg)

        # Wrap it in LangChain's Tool class
        langchain_tool = Tool(
            name=t.name,
            description=t.description,
            func=tool_func,           # async function
            coroutine=tool_func       # required for async
        )

        langchain_tools.append(langchain_tool)

    return langchain_tools
