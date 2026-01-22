from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
messages = [HumanMessage(content="Hi"), AIMessage(content="Hello!")]
print(ChatOpenAI().invoke(messages + [HumanMessage(content="How are you?")]).content)
