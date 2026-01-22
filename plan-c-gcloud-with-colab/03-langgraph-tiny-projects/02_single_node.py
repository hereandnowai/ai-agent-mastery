
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langgraph.graph import StateGraph, START, END
def node(state): return {"count": state["count"] + 1}
builder = StateGraph(dict)
builder.add_node("n", node)
builder.add_edge(START, "n")
builder.add_edge("n", END)
print(builder.compile().invoke({"count": 0}))
