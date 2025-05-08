import unittest
from caishen_sdk_python import CaishenSDK
from dotenv import load_dotenv
import os
from caishen_sdk_python.adapters import create_eleven_labs_tools
import openai

load_dotenv()

class TestAuthFunction(unittest.IsolatedAsyncioTestCase):

    async def test_agent_auth(self):
        project_key = os.getenv('PROJECT_KEY')
        sdk = CaishenSDK(project_key)
        provider = os.getenv('USER_PROVIDER')
        openai_key = os.getenv('OPENAI_API_KEY')
        token = os.getenv('USER_TOKEN')

        # Connect as agent
        auth_token = await sdk.connect_as_agent(provider, token)
        print("auth token: ", auth_token)
        self.assertEqual(sdk.connected_as, "agent")

        # Create LangChain tools and OpenAI tools
        langchain_tools, openai_tools = await create_eleven_labs_tools(sdk)

        # Setup OpenAI client
        client = openai.OpenAI(api_key=openai_key)

        # Test message
        elevenLabs_input_text = "Hello, please give me the balance of account 15!"

        # Send chat completion
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": elevenLabs_input_text}
            ],
            tools=openai_tools,  # ✅ Correct: pass tool specs, not functions
            tool_choice="auto"
        )

        print(response.choices[0].message.content)

if __name__ == '__main__':
    unittest.main()
