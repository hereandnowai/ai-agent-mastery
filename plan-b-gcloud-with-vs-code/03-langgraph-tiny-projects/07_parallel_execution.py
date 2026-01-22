from dotenv import load_dotenv
load_dotenv()
from langgraph.graph import StateGraph, START, END
builder = StateGraph(dict)
builder.add_node("a", lambda s: {"res": "a"})
builder.add_node("b", lambda s: {"res": "b"})
builder.add_edge(START, "a")
builder.add_edge(START, "b")
builder.add_edge(["a", "b"], END)
print(builder.compile().invoke({}))
