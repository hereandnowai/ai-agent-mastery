from langchain_ollama import ChatOllama
llm = ChatOllama(model="gemma3:270m")
for chunk in llm.stream("Write a 3-sentence poem about AI"):
    print(chunk.content, end="|", flush=True)
