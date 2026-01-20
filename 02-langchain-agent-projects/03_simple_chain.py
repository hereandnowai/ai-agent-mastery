from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
chain = ChatPromptTemplate.from_template("{t}") | ChatOpenAI()
print(chain.invoke({"t": "Hi"}).content)
