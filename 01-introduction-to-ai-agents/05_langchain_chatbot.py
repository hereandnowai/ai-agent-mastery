from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# LangChain (Chain-based)
# Specialized Ollama integration
llm = ChatOllama(model="gemma3:270m")

prompt = ChatPromptTemplate.from_template("Explain {topic} to a 5-year old.")
chain = prompt | llm

response = chain.invoke({"topic": "autonomous agents"})
print(response.content)
