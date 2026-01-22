
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langgraph.graph import StateGraph, START, END
def route(s): return "b" if s["i"] > 0 else END
builder = StateGraph(dict)
builder.add_node("a", lambda s: s)
builder.add_node("b", lambda s: {"i": 0})
builder.add_edge(START, "a")
builder.add_conditional_edges("a", route)
builder.add_edge("b", END)
print(builder.compile().invoke({"i": 1}))
