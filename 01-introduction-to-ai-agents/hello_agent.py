from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o")
print(llm.invoke("Reasoning loop active. Hello!").content)
