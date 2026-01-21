from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="ministral")
print(llm.invoke("Hello, who are you?").content)
