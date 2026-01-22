
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
builder = StateGraph(dict)
builder.add_node("a", lambda s: {"c": s["c"] + 1})
builder.set_entry_point("a")
builder.set_finish_point("a")
graph = builder.compile(checkpointer=MemorySaver())
print(graph.invoke({"c": 0}, {"configurable": {"thread_id": "1"}}))
