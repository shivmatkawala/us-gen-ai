from openai import OpenAI

client = OpenAI(api_key="")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain transformers in  simple words."
)

print(response.output_text)