from langgraph.graph import StateGraph, START, END
builder = StateGraph(dict)
builder.add_node("agent", lambda s: {"out": "Hello from LangGraph"})
builder.add_edge(START, "agent"); builder.add_edge("agent", END)
print(builder.compile().invoke({"in": ""}))
