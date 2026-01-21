from langgraph.graph import StateGraph, START, END

def agent1(s): return {"m": s["m"] + ["A1 (Gemma) done"]}
def agent2(s): return {"m": s["m"] + ["A2 (Gemma) done"]}
builder = StateGraph(dict)
builder.add_node("A1", agent1)
builder.add_node("A2", agent2)
builder.add_edge(START, "A1")
builder.add_edge("A1", "A2")
builder.add_edge("A2", END)
print("Tiny Multi-Agent (Gemma 2 logic):", builder.compile().invoke({"m": []}))
