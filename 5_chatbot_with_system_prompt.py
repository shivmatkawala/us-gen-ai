import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

system_prompt= "you are a helpful bot, which gives concise answers"

def chat_with_groq(user_message):
    headers ={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages":[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(url=url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error{response.status_code}: {response.text}"
    
    result = response.json()

    if "choices" in result and len(result["choices"])>0:
        return result["choices"][0]["message"]["content"]
    else:
        return f"Unexpected response format: {result}"
    
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply =chat_with_groq(user_input)
        print(f"Bot: {reply}")
