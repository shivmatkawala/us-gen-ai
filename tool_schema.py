"""
Tool Definitions for OpenAI Function Calling

This file tells the LLM:
1. What tools are available
2. What each tool does
3. What parameters each tool requires
"""

tools = [
    # ======================================================
    # WEATHER TOOL
    # ======================================================
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": (
                "Get the current weather information for any city. "
                "Use this whenever the user asks about weather, "
                "temperature, humidity, climate or wind."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    },
    # ======================================================
    # NEWS TOOL
    # ======================================================
    {
        "type": "function",
        "function": {
            "name": "get_news",
            "description": (
                "Fetch the latest news headlines. "
                "Use this whenever the user asks for "
                "latest news, breaking news, technology news "
                "or current events."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": (
                            "News category such as technology, business, "
                            "sports, health, science."
                        ),
                        "default": "technology"
                    }
                }
            }
        }
    },
    # ======================================================
    # IMAGE GENERATION TOOL
    # ======================================================
    {
        "type": "function",
        "function": {
            "name": "generate_image",
            "description": (
                "Generate an AI image from a user's prompt. "
                "Use this whenever the user asks to draw, "
                "create, generate, design or illustrate an image."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": (
                            "Detailed prompt describing the image to generate."
                        )
                    }
                },
                "required": ["prompt"]
            }
        }
    }
]