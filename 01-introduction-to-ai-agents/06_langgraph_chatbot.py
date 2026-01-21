from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

# LangGraph (State-graph based)
class State(TypedDict):
    content: str

llm = ChatOllama(model="gemma3:270m")

def call_model(state: State):
    res = llm.invoke(state["content"])
    return {"content": res.content}

builder = StateGraph(State)
builder.add_node("chatbot", call_model)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()
response = graph.invoke({"content": "Hi from LangGraph!"})
print(response["content"])
