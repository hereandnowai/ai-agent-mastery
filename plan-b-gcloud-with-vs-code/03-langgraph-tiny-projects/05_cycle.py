from dotenv import load_dotenv
load_dotenv()
from langgraph.graph import StateGraph, START, END
def loop(s): return "a" if s["c"] < 3 else END
builder = StateGraph(dict)
builder.add_node("a", lambda s: {"c": s["c"] + 1})
builder.add_edge(START, "a")
builder.add_conditional_edges("a", loop)
print(builder.compile().invoke({"c": 0}))
