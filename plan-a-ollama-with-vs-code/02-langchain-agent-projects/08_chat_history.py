from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama
messages = [HumanMessage(content="Hi"), AIMessage(content="Hello!")]
print(ChatOllama(model="gemma3:270m").invoke(messages + [HumanMessage(content="How are you?")]).content)
