import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

system_prompt="You are a chatbot that answers clearly and concisely. Your name is Swapna."

chat_hotsory = [
    {"role": "system", "content":system_prompt}
]

def chat_with_groq(user_message):
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    chat_hotsory.append({"role": "user", "content": user_message})

    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": chat_hotsory
    }

    response = requests.post(url=url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"
    
    result = response.json()

    if "choices" in result and len(result["choices"]) > 0:
        reply = result["choices"][0]["message"]["content"]
        chat_hotsory.append({"role": "assistant", "content": reply})
        return reply
    else:
        return f"Unexpected response Format: {result}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat_with_groq(user_input)
        print("Bot: ", reply)

