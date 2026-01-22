
import os
try:
    from google.colab import userdata
    os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
except ImportError:
    from dotenv import load_dotenv
    load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

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
