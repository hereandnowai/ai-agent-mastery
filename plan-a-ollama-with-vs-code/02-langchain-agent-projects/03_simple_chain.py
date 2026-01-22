from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
chain = ChatPromptTemplate.from_template("{t}") | ChatOllama(model="gemma3:270m")
print(chain.invoke({"t": "what does ai stand for?"}).content)