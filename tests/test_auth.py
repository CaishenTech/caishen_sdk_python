import unittest
from caishen_sdk_python import CaishenSDK
from dotenv import load_dotenv
import os
from caishen_sdk_python.adapters import create_eleven_labs_tools
import openai
import json

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
        messages = [{"role": "user", "content": "Hello, please give me the balance of cash account 15"}]
        # Create LangChain tools and OpenAI tools
        openai_tools, tool_runners = await create_eleven_labs_tools(sdk)
        # Setup OpenAI client
        client = openai.AsyncOpenAI(api_key=openai_key)
        # Test message
        elevenLabs_input_text = "Hello, please give me the balance of cash account 15"

        # Send chat completion
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=openai_tools,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message.model_dump())

        if assistant_message.tool_calls:
            # Only one tool call for simplicity
            tool_call = assistant_message.tool_calls[0]
            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            # Run the corresponding Python function
            result = await tool_runners[tool_name](args)

            # Add tool response to messages
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

            # Final response after tool execution
            final_response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            print("Final assistant reply:", final_response.choices[0].message.content)
        else:
            # No tool call was triggered
            print("Assistant reply:", assistant_message.content)

if __name__ == '__main__':
    unittest.main()
