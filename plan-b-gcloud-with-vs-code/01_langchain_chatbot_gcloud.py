from dotenv import load_dotenv
load_dotenv()
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# LangChain (Chain-based)
# Google Gemini/Gemma integration
llm = ChatGoogleGenerativeAI(model="gemma-3-27b-it")
prompt = ChatPromptTemplate.from_template("{user_input}")
chain = prompt | llm

print("LangChain Chatbot (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break
    
    response = chain.invoke({"user_input": user_input})
    print(f"AI: {response.content}")