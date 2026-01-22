from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemma-3-27b-it")

print("--- AI Agent Intro (Cloud) ---")
print("Type 'exit' or 'quit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    response = llm.invoke(user_input)
    print(f"AI: {response.content}")
