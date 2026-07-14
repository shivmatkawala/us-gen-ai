import json

from config import client
from tool_schema import tools
from tools import get_weather, get_news, generate_image


def execute_tool(tool_name, arguments):
    """
    Executes the requested tool and returns the result.
    """
    if tool_name == "get_weather":
        city = arguments["city"]
        return get_weather(city)
    elif tool_name == "get_news":
        category = arguments.get("category", "technology")
        return get_news(category)
    elif tool_name == "generate_image":
        prompt = arguments["prompt"]
        return generate_image(prompt)
    else:
        return {"error": "Unknown Tool"}


def run_agent(user_query):
    messages = [
        {
            "role": "system",
            "content": """
You are a helpful AI Assistant.

You have access to these tools:
1. Weather Tool
2. Technology News Tool
3. Image Generation Tool

Rules:
- If user asks weather, use get_weather().
- If user asks latest news, use get_news().
- If user asks to create/draw/generate an image, use generate_image().
- Never guess live weather or latest news.
- Always use the appropriate tool.
"""
        },
        {
            "role": "user",
            "content": user_query
        }
    ]

    ###############################################
    # First OpenAI Call
    ###############################################
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tools
    )

    assistant_message = response.choices[0].message

    ##################################################
    # No Tool Required
    ##################################################
    if not assistant_message.tool_calls:
        return assistant_message.content

    ##################################################
    # Tool Calling
    ##################################################
    # IMPORTANT: append a plain dict (not the raw SDK object).
    # This guarantees tool_calls are serialized correctly for
    # the follow-up request, regardless of openai-python version.
    messages.append({
        "role": "assistant",
        "content": assistant_message.content,
        "tool_calls": [
            {
                "id": tool_call.id,
                "type": "function",
                "function": {
                    "name": tool_call.function.name,
                    "arguments": tool_call.function.arguments
                }
            }
            for tool_call in assistant_message.tool_calls
        ]
    })

    for tool_call in assistant_message.tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        tool_result = execute_tool(tool_name, arguments)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(tool_result)
        })

    ##################################################
    # Second OpenAI Call
    ##################################################
    final_response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tools
    )

    return final_response.choices[0].message.content