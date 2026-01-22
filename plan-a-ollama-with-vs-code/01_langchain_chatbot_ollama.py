from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# LangChain (Chain-based)
# Specialized Ollama integration
llm = ChatOllama(model="gemma3:270m")

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