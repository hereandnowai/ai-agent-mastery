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

print("LangGraph Chatbot (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break
        
    response = graph.invoke({"content": user_input})
    print(f"AI: {response['content']}")