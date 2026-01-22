from langchain.chains import LLMMathChain
from langchain_ollama import ChatOllama
math_chain = LLMMathChain.from_llm(ChatOllama(model="gemma3:270m"))
print(math_chain.invoke("What is 123 * 456?"))
