from typing import List, Dict, Optional
import requests
from ..constants import BASE_URL, PublicRpcEndpoints, ChainIds

class Crypto:
    async def get_wallet(self, sdk, chain_type: str, account: int, chain_id: Optional[int] = None) -> dict:
        if not chain_type or account is None:
            raise ValueError('chainType and account number are required')

        auth_token = sdk.user_token or sdk.agent_token
        if not auth_token:
            raise ValueError('Authenticate as an agent or user before fetching wallets')

        try:
            response = requests.get(
                f"{BASE_URL}/api/crypto/wallets",
                params={"chainType": chain_type, "account": account, "chainId": chain_id},
                headers={"Authorization": f"Bearer {auth_token}"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise ValueError(f"Failed to get wallet: {error.response.json().get('message', error)}") from error

    async def send(self, sdk, wallet: Dict, payload: Dict) -> str:
        auth_token = sdk.user_token or sdk.agent_token
        if not auth_token:
            raise Exception('Authentication required. Connect as user or agent first.')

        try:
            headers = {
                "Authorization": f"Bearer {auth_token}"
            }
            url = f"{BASE_URL}/api/crypto/send"
            response = requests.post(url, json={'wallet': wallet, 'payload': payload}, headers=headers)
            return response['data']
        except Exception as e:
            raise Exception(f"Failed to send transaction: {str(e)}")

    async def get_balance(self, sdk, wallet: Dict, payload: Dict) -> str:
        auth_token = sdk.user_token or sdk.agent_token
        if not auth_token:
            raise Exception('Authentication required. Connect as user or agent first.')
        
        try:
            headers = {
                "Authorization": f"Bearer {auth_token}"
            }
            url = f'{BASE_URL}/api/crypto/balance'
            response = requests.get(url, params={**wallet, 'tokenAddress': payload.get('token')}, headers=headers)
            return response['data']
        except Exception as e:
            raise Exception(f"Failed to get balance: {str(e)}")

    async def swap(self, sdk, wallet: Dict, payload: Dict) -> dict:
        auth_token = sdk.user_token or sdk.agent_token
        if not auth_token:
            raise Exception('Authentication required. Connect as user or agent first.')

        try:
            headers = {"Authorization": f"Bearer {auth_token}"}
            url = f"{BASE_URL}/api/crypto/swap"
            response = requests.post(url, json={'wallet': wallet, 'payload': payload}, headers=headers)
            return response
        except Exception as e:
            raise Exception(f"Failed to execute the swap route: {str(e)}")

    async def get_swap_route(self, sdk, wallet: Dict, payload: Dict) -> dict:
        auth_token = sdk.user_token or sdk.agent_token
        if not auth_token:
            raise Exception('Authentication required. Connect as user or agent first.')

        try:
            headers = {"Authorization": f"Bearer {auth_token}"}
            url = f"{BASE_URL}/api/crypto/swap-route"
            response = requests.post(url, json={'wallet': wallet, 'payload': payload}, headers=headers)
            return response
        except Exception as e:
            raise Exception(f"Failed to get route to execute: {str(e)}")

    async def get_supported_chain_types(self, sdk) -> list:
        try:
            auth_token = sdk.user_token or sdk.agent_token
            if not auth_token:
                raise ValueError('Authenticate as an agent or user before fetching wallets')

            response = requests.get(
                f"{BASE_URL}/api/crypto/wallets/supported",
                headers={"Authorization": f"Bearer {auth_token}"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise ValueError("Failed to get supported chain types") from error

    async def get_rpc(chain_id: ChainIds) -> str:
        if chain_id.value not in PublicRpcEndpoints:
            raise ValueError(f"RPC for {chain_id} not supported")
        return PublicRpcEndpoints[chain_id.value]        
    
__all__ = ["Crypto"]