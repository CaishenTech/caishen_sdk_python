import requests
from typing import Optional, Literal, Dict, Any, Callable
from .constants import BASE_URL
from .cash import cash
from .crypto import crypto

class CaishenSDK:
    def __init__(self, project_key: str):
        if not project_key:
            raise ValueError("Project key is required")
        
        self.project_key: str = project_key
        self.agent_token: Optional[str] = None
        self.user_token: Optional[str] = None
        self.connected_as: Optional[Literal['agent', 'user']] = None
        self.cash = self._bind_module(cash.Cash())
        self.crypto = self._bind_module(crypto.Crypto())

    def _bind_module(self, module: Any) -> Dict[str, Callable]:
        bound = {}
        for key in dir(module):
            fn = getattr(module, key)
            if callable(fn) and not key.startswith("_"):
                def make_wrapper(f):
                    return lambda *args, **kwargs: f(self, *args, **kwargs)
                bound[key] = make_wrapper(fn)
        return bound

    async def connect_as_agent(self, agent_id: Optional[str] = None, user_id: Optional[str] = None) -> str:
        if self.connected_as:
            raise RuntimeError(
                'Already connected as a user or agent. Create a new instance to connect again.'
            )
        
        try:
            response = await requests.post(
                f"{BASE_URL}/auth/agents/connect",
                json={"agentId": agent_id, "userId": user_id},
                headers={"projectKey": self.project_key},
            )
            response.raise_for_status()
            self.agent_token = response.json().get("agentToken")
            self.connected_as = "agent"
            return self.agent_token
        except requests.RequestException as e:
            raise RuntimeError(f"Agent authentication failed: {str(e)}")

    async def connect_as_user(self, provider: str, token: str) -> str:
        if self.connected_as:
            raise RuntimeError(
                'Already connected as a user or agent. Create a new instance to connect again.'
            )
        
        try:
            response = requests.post(
                f"{BASE_URL}/auth/users/connect",
                json={"provider": provider, "token": token},
                headers={"projectKey": self.project_key},
            )
            response.raise_for_status()
            self.user_token = response.json().get("userToken")
            self.connected_as = "user"
            return self.user_token
        except requests.RequestException as e:
            raise RuntimeError(f"User authentication failed: {str(e)}")