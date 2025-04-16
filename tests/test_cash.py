# tests/test_hello.py

import unittest
from caishen_sdk_python import CaishenSDK
from dotenv import load_dotenv
import os

load_dotenv()

class TestCashFunction(unittest.IsolatedAsyncioTestCase):
    async def test_cash_send(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        await sdk.connect_as_user(
            provider,
            token
        )
        self.assertEqual(sdk.connected_as, "user")

    async def test_cash_deposit(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        await sdk.connect_as_user(
            provider,
            token
        )
        self.assertEqual(sdk.connected_as, "user")

    async def test_cash_withdraw(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        await sdk.connect_as_user(
            provider,
            token
        )
        self.assertEqual(sdk.connected_as, "user")

    async def test_cash_get_balance(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        await sdk.connect_as_user(
            provider,
            token
        )
        self.assertEqual(sdk.connected_as, "user")

    async def test_cash_get_supported_tokens(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')
        await sdk.connect_as_user(
            provider,
            token
        )
        self.assertEqual(sdk.connected_as, "user")

if __name__ == '__main__':
    unittest.main()