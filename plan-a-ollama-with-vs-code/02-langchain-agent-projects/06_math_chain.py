from langchain.chains import LLMMathChain
from langchain_openai import ChatOpenAI
math_chain = LLMMathChain.from_llm(ChatOpenAI())
print(math_chain.invoke("What is 123 * 456?"))
