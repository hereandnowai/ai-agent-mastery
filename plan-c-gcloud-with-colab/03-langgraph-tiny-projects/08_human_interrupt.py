
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langgraph.graph import StateGraph
builder = StateGraph(dict)
builder.add_node("a", lambda s: s)
builder.set_entry_point("a")
builder.set_finish_point("a")
graph = builder.compile(interrupt_before=["a"])
# This will stop before node 'a'
print("Graph compiled with interruption")
