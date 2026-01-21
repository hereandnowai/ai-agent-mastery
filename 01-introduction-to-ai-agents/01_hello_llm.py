from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o")
print(llm.invoke("Hello, who are you?").content)
