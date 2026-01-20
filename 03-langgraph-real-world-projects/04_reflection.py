from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

# Define State
class AgentState(TypedDict):
    messages: List[BaseMessage]

# Define Nodes
def generate_node(state: AgentState):
    llm = ChatOpenAI(model="gpt-4-turbo-preview")
    response = llm.invoke(state['messages'] + [HumanMessage(content="Write a short paragraph about the benefits of AI.")])
    return {"messages": [response]}

def reflect_node(state: AgentState):
    llm = ChatOpenAI(model="gpt-4-turbo-preview")
    last_message = state['messages'][-1]
    reflection = llm.invoke([HumanMessage(content=f"Critique the following text and suggest 3 improvements:\n{last_message.content}")])
    return {"messages": [reflection]}

def research_node(state: AgentState):
    # This would simulate a research step based on reflection
    return {"messages": [AIMessage(content="Added more technical details to the content based on critique.")]}

# Build Graph
builder = StateGraph(AgentState)
builder.add_node("generate", generate_node)
builder.add_node("reflect", reflect_node)

builder.set_entry_point("generate")
builder.add_edge("generate", "reflect")
builder.add_edge("reflect", END)

graph = builder.compile()

# Run
if __name__ == "__main__":
    for output in graph.stream({"messages": []}):
        print(output)
