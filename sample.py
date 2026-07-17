from deepagents import create_deep_agent
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str) -> str:
    """Returns the current weather for a city."""
    print(f"🔧 Tool Invoked: get_weather({city})")
    return f"The weather in {city} is sunny and 28°C."


def get_currency(country: str) -> str:
    """Returns the currency used in a country."""
    print(f"🔧 Tool Invoked: get_currency({country})")

    currencies = {
        "India": "Indian Rupee (INR)",
        "United States": "US Dollar (USD)",
        "Japan": "Japanese Yen (JPY)",
        "France": "Euro (EUR)",
    }

    return currencies.get(country, "Currency not found")


def suggest_activity(weather: str) -> str:
    """Suggests an activity based on the weather."""
    print("🔧 Tool Invoked: suggest_activity()")

    if "sunny" in weather.lower():
        return "Go for a walk or visit a park."
    return "Stay indoors and read a book."


agent = create_deep_agent(
    model="openai:gpt-5.5",
    tools=[
        get_weather,
        get_currency,
        suggest_activity,
    ],
    system_prompt="""
    You are an intelligent travel assistant.
    Think step by step.
    Use tools whenever necessary.
    Never guess if a tool can provide the answer.
    """,
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": """
I'm planning a trip to India.
Tell me:
1. What's the weather in Delhi?
2. What's the currency?
3. Suggest an outdoor activity.
""",
            }
        ]
    }
)

print("\n========== FINAL ANSWER ==========\n")

final = response["messages"][-1]

if isinstance(final.content, str):
    print(final.content)
else:
    print(final.content[0]["text"])