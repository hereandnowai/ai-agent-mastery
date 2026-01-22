from langgraph.graph import StateGraph, START, END
builder = StateGraph(dict)
builder.add_node("a", lambda s: {"c": s["c"] + "a"})
builder.add_node("b", lambda s: {"c": s["c"] + "b"})
builder.add_edge(START, "a")
builder.add_edge("a", "b")
builder.add_edge("b", END)
print(builder.compile().invoke({"c": ""}))
