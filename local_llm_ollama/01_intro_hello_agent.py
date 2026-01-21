from langchain_community.chat_models import ChatOllama
# local llm ministral is already installed in this mac
llm = ChatOllama(model="ministral")
print(llm.invoke("Reasoning loop active. Hello!").content)
