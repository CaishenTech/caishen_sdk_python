# tests/test_hello.py

import unittest
from caishen_sdk_python import CaishenSDK
from dotenv import load_dotenv
import os
from ..caishen_sdk_python.adapters import create_eleven_labs_tools
import openai
# import { ChatOpenAI } from "@langchain/openai";
# import { initializeAgentExecutorWithOptions } from "langchain/agents";

load_dotenv()

class TestAuthFunction(unittest.IsolatedAsyncioTestCase):
    async def test_user_auth(self):
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

    async def test_agent_auth(self):
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
        elevenLabsData = await create_eleven_labs_tools({sdk})    
        # elevenLabs_input_text = "Hello, please give me the balance of account 15!"
        # elevenLabsData_result = await generateText({
        #     model: openai("gpt-4o-mini"),
        #     tools: tools,
        #     maxSteps: 10, 
        #     prompt: elevenLabs_input_text,
        # })
        
if __name__ == '__main__':
    unittest.main()