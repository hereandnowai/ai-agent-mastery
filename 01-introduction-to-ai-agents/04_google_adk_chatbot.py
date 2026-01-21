import requests
import json

# Google ADK / Raw API style
# Accessing Ollama directly via HTTP
url = "http://localhost:11434/api/generate"
payload = {
    "model": "gemma3:270m",
    "prompt": "What is the specialized role of an AI Agent?",
    "stream": False
}

response = requests.post(url, json=payload)
data = response.json()

print(f"Gemma 3 (Raw API): {data['response']}")
