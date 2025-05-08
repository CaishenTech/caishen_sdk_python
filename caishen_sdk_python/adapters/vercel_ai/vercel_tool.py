# vercel_tool.py
from typing import Callable, Type, Awaitable, Any
from pydantic import BaseModel
import openai

class VercelAITool:
    def __init__(
        self,
        description: str,
        parameters: Type[BaseModel],
        execute: Callable[[Any], Awaitable[Any]]
    ):
        self.description = description
        self.parameters = parameters
        self.execute = execute

def tool(description: str, parameters: Type[BaseModel], execute: Callable[[Any], Awaitable[Any]]) -> VercelAITool:
    return VercelAITool(description=description, parameters=parameters, execute=execute)

def generate_text_with_tools(prompt: str, tools: any):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",  # must support tool calls
        messages=[
            {"role": "user", "content": prompt}
        ],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    print("message: ", message)