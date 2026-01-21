from langgraph.graph import StateGraph, START, END

# Note: This logic is pure Python state management, model-agnostic.
def loop(s): return "a" if s["c"] < 3 else END
builder = StateGraph(dict)
builder.add_node("a", lambda s: {"c": s["c"] + 1})
builder.add_edge(START, "a")
builder.add_conditional_edges("a", loop)
print("State Cycle (Gemma-ready logic):", builder.compile().invoke({"c": 0}))
