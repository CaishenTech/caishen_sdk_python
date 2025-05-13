from langchain.agents import Tool, initialize_agent
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import AgentAction, AgentFinish
from typing import Optional, Union
from caishen_sdk_python import CaishenSDK
from dotenv import load_dotenv
import os
import unittest
from caishen_sdk_python.adapters import create_langchain_tools

load_dotenv()

class TestLangchainTools(unittest.IsolatedAsyncioTestCase):

    async def test_langchain_tool(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        token = os.getenv('USER_TOKEN')

        # Connect as agent
        auth_token = await sdk.connect_as_agent(provider, token)
        self.assertEqual(sdk.connected_as, "agent")
        message = "Hello, please give me the balance of cash account 15"
        # Create LangChain tools and OpenAI tools
        langchain_tools = await create_langchain_tools(sdk)
        # Initialize your LLM (GPT-4 in this example)
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        openai_api_key = os.getenv('OPENAI_API_KEY')
        llm.openai_api_key = openai_api_key

        # Initialize agent with options
        agent_executor = initialize_agent(
            tools=langchain_tools,
            llm=llm,
            agent_type="openai-functions",  # Use "openai-tools" if you're using OpenAI tool calling models
            verbose=True
        )
        # Run the agent
        result = await agent_executor.ainvoke({"input": message}) 
        print(result)

if __name__ == '__main__':
    unittest.main()



