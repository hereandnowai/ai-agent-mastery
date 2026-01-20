from langgraph.graph import StateGraph, START, END
def agent1(s): return {"m": s["m"] + ["A1 done"]}
def agent2(s): return {"m": s["m"] + ["A2 done"]}
builder = StateGraph(dict)
builder.add_node("A1", agent1); builder.add_node("A2", agent2)
builder.add_edge(START, "A1"); builder.add_edge("A1", "A2"); builder.add_edge("A2", END)
print(builder.compile().invoke({"m": []}))
