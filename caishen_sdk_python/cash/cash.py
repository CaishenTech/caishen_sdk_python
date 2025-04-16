from .schema import SendTransactionParams, TransactionResponse, DepositCashParams, WithdrawCashParams, BalanceResponse, Token
from typing import List
import requests
from ..constants import BASE_URL

class Cash:
    async def send(self, sdk, params: SendTransactionParams) -> TransactionResponse:
        auth_token = sdk.user_token or sdk.agent_token
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        url = f"{BASE_URL}/api/cash/send"
        response = requests.post(url, json=params, headers=headers)
        return response.json()

    async def deposit(self, sdk, params: DepositCashParams) -> TransactionResponse:
        auth_token = sdk.user_token or sdk.agent_token
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        url = f"{BASE_URL}/api/cash/deposit"
        response = requests.post(url, json=params, headers=headers)
        return response.json()

    async def withdraw(self, sdk, params: WithdrawCashParams) -> TransactionResponse:
        auth_token = sdk.user_token or sdk.agent_token
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        url = f"{BASE_URL}/api/cash/withdraw"
        response = requests.post(url, json=params, headers=headers)
        return response.json()

    async def get_balance(self, sdk, account: int) -> BalanceResponse:
        auth_token = sdk.user_token or sdk.agent_token
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        url = f"{BASE_URL}/api/cash/balance"
        response = requests.get(url, params={"account": account}, headers=headers)
        return response.json()
    
    async def get_supported_tokens(self, sdk) -> List[Token]:
        auth_token = sdk.user_token or sdk.agent_token
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        url = f"{BASE_URL}/api/cash/tokens"
        response = requests.get(url, headers=headers)
        return response.json()
    
__all__ = ["Cash"]