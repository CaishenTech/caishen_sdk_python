from typing import Callable, Type, TypedDict, Any
from pydantic import BaseModel

class ToolBase(TypedDict):
    name: str
    description: str
    parameters: Type[BaseModel]
    execute: Callable[[BaseModel], Any]

def tool_base(name: str, description: str, parameters: Type[BaseModel], execute: Callable[[BaseModel], Any]) -> ToolBase:
    return {
        "name": name,
        "description": description,
        "parameters": parameters,
        "execute": execute,
    }
