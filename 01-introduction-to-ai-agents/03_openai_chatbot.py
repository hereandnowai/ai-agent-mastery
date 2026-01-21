from openai import OpenAI

# OpenAI SDK (Simple)
# Connecting to local Ollama instance
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="gemma3:270m",
    messages=[{"role": "user", "content": "How's the weather in the world of AI?"}]
)

print(f"Gemma 3: {response.choices[0].message.content}")
