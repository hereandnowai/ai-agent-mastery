from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
for chunk in llm.stream("Write a 3-sentence poem about AI"):
    print(chunk.content, end="|", flush=True)
