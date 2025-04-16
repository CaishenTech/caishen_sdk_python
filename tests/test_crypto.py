# tests/test_hello.py

import unittest
from caishen_sdk_python import CaishenSDK
from dotenv import load_dotenv
import os

load_dotenv()

class TestCryptoFunction(unittest.IsolatedAsyncioTestCase):
    async def test_get_wallet(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        auth_token = await sdk.connect_as_user(
            provider,
            token
        )
        print("auth token: ", auth_token)
        self.assertEqual(sdk.connected_as, "user")

    async def test_send(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        auth_token = await sdk.connect_as_agent(
            provider,
            token
        )
        print("auth token: ", auth_token)
        self.assertEqual(sdk.connected_as, "agent")

    async def test_get_balance(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        auth_token = await sdk.connect_as_agent(
            provider,
            token
        )
        print("auth token: ", auth_token)
        self.assertEqual(sdk.connected_as, "agent")

if __name__ == '__main__':
    unittest.main()